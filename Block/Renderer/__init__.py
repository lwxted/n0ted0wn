#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
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
      res = self.style_cls.renderers_for_block_rule(block.__class__)\
        (self.style_cls).render(block, self.text_storage, self.env_storage)
      rendered = ''
      storage_keys = set()
      if isinstance(res, str):
        rendered = res
      elif isinstance(res, tuple):
        rendered = res[0]
        storage_keys = res[1]
      for inline_unprocessed_key in storage_keys:
        inline_processed = self.text_storage.get(inline_unprocessed_key)
        for inline_rule_cls in self.style_cls.inline_rules_for_block_rule(
          block.__class__):
          inline_processed = inline_rule_cls.render(
            inline_processed, self.style_cls._final_process, \
            self.text_storage, self.env_storage)
        self.text_storage.update(inline_unprocessed_key, inline_processed)
      blocks_rendered.append(self.text_storage.recover(
        rendered, storage_keys).strip())

    return '\n'.join(blocks_rendered)
