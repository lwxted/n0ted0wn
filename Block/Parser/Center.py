#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.StdEnv import StdEnv

class CenterStdEnv(StdEnv):
  """Implements parsing for the following block format.

  {center}
  Text or content to be placed in center
  {center}
  """

  _block_type = 'center'

  def __init__(self, raw, params, content, style_cls):
    super(CenterStdEnv, self).__init__(raw, params, content, style_cls)
    self.content_blocks_list = []

  def _transform_args(self):
    from n0ted0wn.Block.Parser import Parser
    self.content_blocks_list = Parser(self.style_cls, 0).parse(self.content)
    return self
