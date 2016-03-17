#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.StdEnv import StdEnv

class HideStdEnv(StdEnv):
  """
  Hide content in some cases...

  {hide}
  Content to hide in some cases...
  {hide}
  """

  _block_type = 'hide'

  def __init__(self, raw, params, content, style_cls):
    super(HideStdEnv, self).__init__(raw, params, content, style_cls)
    self.content_blocks_list = []

  def _transform_args(self):
    from n0ted0wn.Block.Parser import Parser
    self.content_blocks_list = Parser(self.style_cls, 0).parse(self.content)
    return self
