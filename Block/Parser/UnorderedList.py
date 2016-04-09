#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.Base import Base
from n0ted0wn.Block.Parser.StdEnv import StdEnv


class UnorderedList(Base):
  """
  Implements parsing for the following block format.

  * Item 1
  * Item 2
  * Item 3
  """

  def __init__(self, raw, parsed_blocks_list, style_cls):
    super(UnorderedList, self).__init__(raw, style_cls)
    self.parsed_blocks_list = parsed_blocks_list

  @classmethod
  def parse(cls, raw, style_cls):
    lines = raw.strip().split('\n')
    items = []
    for l in lines:
      if l.startswith('* '):
        items.append(l[2:])
      elif l.startswith('  '):
        if not items:
          return None
        else:
          items[-1] += '\n' + l[2:]
      else:
        return None
    from n0ted0wn.Block.Parser import Parser
    return cls(raw, \
      [Parser(style_cls, 0).parse(item) for item in items], style_cls)


class UnorderedListStdEnv(StdEnv):
  """
  Implements parsing for the following block format.

  {ul}
  * Item 1
  * Item 2
    with new lines
  * Item 3

    with blocks
  {ul}
  """

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
        if not grouped_lines:
          return None
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
