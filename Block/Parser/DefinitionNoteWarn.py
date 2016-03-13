#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.StdEnv import StdEnv

class DefinitionStdEnv(StdEnv):
  """Implements parsing for the following block formats.

  {def}
  Title
  Explanation that may span
  multiple lines

  Can also include blocks here...
  {def}
  """

  _block_type = 'def'

  def __init__(self, raw, params, content, style_cls):
    super(DefinitionStdEnv, self).__init__(raw, params, content, style_cls)
    self.title = ''
    self.explanation_blocks_list = []

  def _transform_args(self):
    first_line_break = self.content.find('\n')
    if first_line_break == -1:
      return None
    self.title = self.content[:first_line_break]
    from n0ted0wn.Block.Parser import Parser
    self.explanation_blocks_list = Parser(self.style_cls, 0)\
      .parse(self.content[first_line_break + 1:])
    return self

class NoteStdEnv(StdEnv):
  """Implements parsing for the following block formats.

  {note}
  Title
  Explanation that may span
  multiple lines

  Can also include blocks here...
  {note}
  """

  _block_type = 'note'

  def __init__(self, raw, params, content, style_cls):
    super(NoteStdEnv, self).__init__(raw, params, content, style_cls)
    self.title = ''
    self.explanation_blocks_list = []

  def _transform_args(self):
    first_line_break = self.content.find('\n')
    if first_line_break == -1:
      return None
    self.title = self.content[:first_line_break]
    from n0ted0wn.Block.Parser import Parser
    self.explanation_blocks_list = Parser(self.style_cls, 0)\
      .parse(self.content[first_line_break + 1:])
    return self

class WarnStdEnv(StdEnv):
  """Implements parsing for the following block formats.

  {warn}
  Title
  Explanation that may span
  multiple lines

  Can also include blocks here...
  {warn}
  """

  _block_type = 'warn'

  def __init__(self, raw, params, content, style_cls):
    super(WarnStdEnv, self).__init__(raw, params, content, style_cls)
    self.title = ''
    self.explanation_blocks_list = []

  def _transform_args(self):
    first_line_break = self.content.find('\n')
    if first_line_break == -1:
      return None
    self.title = self.content[:first_line_break]
    from n0ted0wn.Block.Parser import Parser
    self.explanation_blocks_list = Parser(self.style_cls, 0)\
      .parse(self.content[first_line_break + 1:])
    return self
