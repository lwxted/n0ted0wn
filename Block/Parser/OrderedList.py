#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.Base import Base
from n0ted0wn.Block.Parser.StdEnv import StdEnv


class OrderedList(Base):
  """
  Implements parsing for the following block format.

  1. Item 1
  2. Item 2
     with multiple lines

  And the starting index can be non-default (1).

  9. Item 9
  10. Item 10
  """

  def __init__(self, raw, start_index, parsed_blocks_list, style_cls):
    super(OrderedList, self).__init__(raw, style_cls)
    self.start_index = start_index
    self.parsed_blocks_list = parsed_blocks_list

  @classmethod
  def parse(cls, raw, style_cls):
    raw = raw.strip()
    first_dot_index = raw.find('. ')
    if first_dot_index == -1:
      return None
    start_index_str = raw[0:first_dot_index]
    if not start_index_str.isdigit():
      return None
    start_index = int(start_index_str)
    current_index = start_index
    items = []
    lines = raw.split('\n')
    for l in lines:
      content_marker = unicode(current_index) + '. '
      if l.startswith(content_marker):
        items.append(l[len(content_marker):])
        current_index += 1
      else:
        prev_content_marker_str_len = len(unicode(current_index - 1)) + 2
        if l.startswith(' ' * prev_content_marker_str_len):
          if not items:
            return None
          else:
            items[-1] += '\n' + l[prev_content_marker_str_len:]
        else:
          return None
    from n0ted0wn.Block.Parser import Parser
    return OrderedList(raw, start_index, \
      [Parser(style_cls, 0).parse(item) for item in items], style_cls)


class OrderedListStdEnv(StdEnv):
  """
  Implements parsing for the following block format.

  {ol}
  1. This is to demonstrate how we'll parse this list block
  2. There can be one-line strings
  3. Or multiline
     strings
  4. Or multiple

     paragraphs
  5. Or even blocks within blocks! Like this:

     {img}
     https://upload.wikimedia.org/wikipedia/commons/a/ae/Facebook_Headquarters_Entrance_Sign_Menlo_Park.jpg
     Seriously amazing!
     {img}

     ```
     And other blocks

     Like this!!
     ```
  6. And finally, another list block within this!

     {ol}
     1. Like this 1
     2. Like this 2
     {ol}
  {ol}
  """

  _block_type = 'ol'

  def __init__(self, raw, params, content, style_cls):
    super(OrderedListStdEnv, self).__init__(raw, params, content, style_cls)
    self.start_index = 0
    self.parsed_blocks_list = []

  def _transform_args(self):
    first_dot_index = self.content.find('. ')
    if first_dot_index == -1:
      return None
    start_index_str = self.content[0:first_dot_index]
    if not start_index_str.isdigit():
      return None
    self.start_index = int(start_index_str)

    current_index = self.start_index
    lines = self.content.split('\n')
    grouped_lines = []
    for l in lines:
      counter_marker = unicode(current_index) + '. '
      if l.startswith(counter_marker):
        grouped_lines.append((current_index, [' ' * len(counter_marker) + \
          l[len(counter_marker):]]))
        current_index += 1
      elif l.startswith(' ' * (len(unicode(current_index - 1)) + 2)) or \
        not l.strip():
        if not grouped_lines:
          return None
        grouped_lines[-1][1].append(l)
      else:
        return None

    from n0ted0wn.Block.Parser import Parser

    for (index, lines) in grouped_lines:
      self.parsed_blocks_list.append(
        Parser(self.style_cls, len(unicode(index)) + 2)
        .parse('\n'.join(lines)))
    return self
