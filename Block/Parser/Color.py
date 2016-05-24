#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.StdEnv import StdEnv

class ColorStdEnv(StdEnv):
  """Implements parsing for the following block formats.

  1. Specify color using hex
  {color:#444}
  content
  {color}

  2. Specify color using color name
  {color:gray}
  content
  {color}
  """

  _block_type = 'color'

  def __init__(self, raw, params, content, style_cls):
    super(ColorStdEnv, self).__init__(raw, params, content, style_cls)
    self.color = ''
    self.blocks_list = []

  def _transform_args(self):
    if not self._params:
      return None
    self.color = self._params[0]
    from n0ted0wn.Block.Parser import Parser
    self.blocks_list = Parser(self.style_cls, 0).parse(self.content)
    return self

class TrivialStdEnv(StdEnv):
  """Implements parsing for the following block formats.

  {trivial}
  Trivial content that may not be of great importance
  {trivial}
  """

  _block_type = 'trivial'

  def __init__(self, raw, params, content, style_cls):
    super(TrivialStdEnv, self).__init__(raw, params, content, style_cls)
    self.blocks_list = []

  def _transform_args(self):
    from n0ted0wn.Block.Parser import Parser
    self.blocks_list = Parser(self.style_cls, 0).parse(self.content)
    return self
