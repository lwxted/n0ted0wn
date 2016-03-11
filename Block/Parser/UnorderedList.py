#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.StdEnv import StdEnv

class UnorderedListStdEnv(StdEnv):
  """Implements parsing for the following block format."""

  _block_type = 'ul'

  def __init__(self, raw, params, content, style_cls):
    super(UnorderedListStdEnv, self).__init__(raw, params, content, style_cls)
    self.parsed_blocks_list = []

  def _transform_args(self):
    item_marker_index = self.content.find('* ')
    if item_marker_index == -1:
      return None

    lines = self.content.split('\n')
    grouped_lines = []
    for l in lines:
      if l.startswith('  ') or not l.strip():
        grouped_lines[-1].append(l)
      else:
        counter_marker = '* '
        if not l.startswith(counter_marker):
          return None
        grouped_lines.append([' ' * len(counter_marker) + \
          l[len(counter_marker):]])

    from n0ted0wn.Block.Parser import Parser

    for lines in grouped_lines:
      self.parsed_blocks_list.append(
        Parser(self.style_cls, 2).parse('\n'.join(lines)))
    return self
