#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

import operator
import re

from n0ted0wn.Style import Style

class Renderer(object):
  def __init__(self, style_cls, text_storage, env_storage):
    self.style_cls = style_cls
    self.text_storage = text_storage
    self.env_storage = env_storage

  def render(self, blocks):
    blocks_rendered = []
    # For each processed block
    for block in blocks:
      block_renderer = self.style_cls.renderer_for_block_rule(block.__class__)(self.style_cls)
      res = block_renderer.render(block, self.text_storage, self.env_storage)
      rendered = ''
      storage_keys = set()
      if isinstance(res, str):
        rendered = res
      elif isinstance(res, tuple):
        rendered = res[0]
        storage_keys = res[1]
      final_process = self.style_cls.final_process_func()
      # Loop through each unprocessed text and feed into the inline parser + renderer
      for inline_unprocessed_key in storage_keys:
        inline_processed = self.text_storage.get(inline_unprocessed_key)
        inline_rules = self.style_cls.inline_rules_for_block_rule(block.__class__)
        sliced_segments_list = []
        for rule in inline_rules:
          inline_matches = sorted(rule.parse(inline_processed), key=operator.attrgetter('span'))
          sliced_segments_list = []
          proc_index = 0
          for inline_match in inline_matches:
            prev_segment = inline_processed[proc_index:inline_match.span[0]]
            sliced_segments_list.append(prev_segment)
            inline_rendered = self.style_cls.renderer_for_inline_rule(rule).render(inline_match, final_process)
            sliced_segments_list.append('\\' + str(self.text_storage.insert(inline_rendered)))
            proc_index = inline_match.span[1]
          final_segment = inline_processed[proc_index:]
          sliced_segments_list.append(final_segment)
          inline_processed = ''.join(sliced_segments_list)
        # Before we are done, we loop through once more and make sure that all segments have been *final processed*.
        for i in xrange(len(sliced_segments_list)):
          if re.match(r'^\\[0-9]+$', sliced_segments_list[i]) is None:
            sliced_segments_list[i] = final_process(sliced_segments_list[i])
        inline_processed = ''.join(sliced_segments_list)
        self.text_storage.update(inline_unprocessed_key, inline_processed)
      blocks_rendered.append(self.text_storage.recover(rendered, storage_keys).strip())

    return '\n'.join(blocks_rendered)
