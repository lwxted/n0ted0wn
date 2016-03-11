#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.StdEnv import StdEnv

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
      if l.startswith(' ' * (len(str(current_index)) + 2)) or not l.strip():
        grouped_lines[-1][1].append(l)
      else:
        counter_marker = str(current_index) + '. '
        if not l.startswith(counter_marker):
          return None
        grouped_lines.append((current_index, [' ' * len(counter_marker) + \
          l[len(counter_marker):]]))
        current_index += 1

    from n0ted0wn.Block.Parser import Parser

    for (index, lines) in grouped_lines:
      self.parsed_blocks_list.append(
        Parser(self.style_cls, len(str(index)) + 2)
        .parse('\n'.join(lines)))
    return self
