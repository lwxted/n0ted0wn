#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.BlockBase import BlockBase

class BlockStdEnv(BlockBase):
  """BlockStdEnv parases the block of a standardized format as follows:

  {block_type:param1:param2}
  Content lines...
  {block_type}
  """

  _block_type = ''

  def __init__(self, raw, params, content):
    super(BlockStdEnv, self).__init__(raw)
    self.content = content
    self._params = params

  def _transform_args(self):
    return self

  @classmethod
  def parse(cls, raw):
    raw = raw.strip()
    first_line_break = raw.find('\n')
    if first_line_break == -1:
      return None
    first_line = raw[0:first_line_break]
    if first_line[0] != '{' or first_line[-1] != '}':
      return None
    args = first_line[1:-1].split(':')
    if args[0] != cls._block_type:
      return None
    if not raw.endswith('\n{' + cls._block_type + '}'):
      return BlockBase.NOT_COMPLETE
    last_line_break = raw.rfind('\n')
    obj = cls(raw, args[1:], raw[first_line_break + 1:last_line_break])
    return obj._transform_args()
