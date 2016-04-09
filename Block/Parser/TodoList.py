#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.Base import Base
from n0ted0wn.Block.Parser.StdEnv import StdEnv

class TodoList(Base):
  """
  Implements parsing for the following block format.

  * [ ] Todo 1
  * [ ] Todo 2
  * [x] Done item
  * [X] Also done
    with multiline description...
  """

  def __init__(self, raw, parsed_items, style_cls):
    super(TodoList, self).__init__(raw, style_cls)
    self.parsed_items = parsed_items

  @classmethod
  def parse(cls, raw, style_cls):
    lines = raw.strip().split('\n')
    items = []
    for l in lines:
      if l.startswith('* [ ] '):
        items.append((False, l[6:], []))
      elif l.startswith('* [x] ') or l.startswith('* [X] '):
        items.append((True, l[6:], []))
      elif l.startswith('  '):
        if not items:
          return None
        else:
          items[-1] = (items[-1][0], items[-1][1] + '\n' + l[2:], items[-1][2])
      else:
        return None
    return cls(raw, items, style_cls)


class TodoListStdEnv(StdEnv):
  """
  Implements parsing for the following block format.

  {todo}
  * [ ] Todo 1
  * [ ] Todo 2

    * [ ] With neseted todos...
    * [ ] Like this...

    Or even some other blocks...

  * [ ] Todo 3
  {todo}
  """

  _block_type = 'todo'

  def __init__(self, raw, params, content, style_cls):
    super(TodoListStdEnv, self).__init__(raw, params, content, style_cls)
    self.parsed_items = []

  def _transform_args(self):
    if '* [ ] ' not in self.content and \
       '* [x] ' not in self.content and \
       '* [X] ' not in self.content:
      return None
    lines = self.content.split('\n')
    parsed_items = []
    for l in lines:
      if l.startswith('  ') or not l.strip():
        parsed_items[-1][2].append(l)
      else:
        item_marker_len = len('* [ ] ')
        done = l.startswith('* [x] ') or l.startswith('* [X] ')
        if not l.startswith('* [ ] ') and not done:
          return None
        # Starts with * [ ] or * [x] or * [X]
        parsed_items.append((done, l[item_marker_len:], []))

    from n0ted0wn.Block.Parser import Parser

    for (done, label, lines) in parsed_items:
      self.parsed_items.append(
        (done, label, Parser(self.style_cls, 2).parse('\n'.join(lines)))
      )

    return self
