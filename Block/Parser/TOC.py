#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.StdEnv import StdEnv

class TOCStdEnv(StdEnv):
  """
  Table of contents

  {toc}
  {toc}
  """

  _block_type = 'toc'

  def __init__(self, raw, params, content, style_cls):
    super(TOCStdEnv, self).__init__(raw, params, content, style_cls)

  def _transform_args(self):
    return self
