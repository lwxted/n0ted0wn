#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.Base import Base

class StdEnv(Base):
  """StdEnv parases the block of a standardized format as follows:

  {block_type:param1:param2}
  Content lines...
  {block_type}

  Or when the block itself is short and not supposed to contain any
  content, the ending block marker is not required:

  {block_type:param1:param2}
  """

  _block_type = ''

  def __init__(self, raw, params, content, style_cls):
    super(StdEnv, self).__init__(raw, style_cls)
    self.content = content
    self._params = params
    self.style_cls = style_cls

  def _transform_args(self):
    return self

  @classmethod
  def parse(cls, raw, style_cls):
    raw = raw.strip()
    first_line_break = raw.find('\n')
    first_line = raw
    if first_line_break != -1:
      first_line = raw[0:first_line_break]
    if first_line[0] != '{' or first_line[-1] != '}':
      return None
    args = first_line[1:-1].split(':')
    if args[0] != cls._block_type:
      return None
    last_line_break = raw.rfind('\n')
    if first_line_break == -1 and last_line_break == -1:
      obj = cls(raw, args[1:], '', style_cls)
      return obj._transform_args()
    if not raw.endswith('\n{' + cls._block_type + '}'):
      return Base.NOT_COMPLETE
    obj = cls(
      raw, args[1:], raw[first_line_break + 1:last_line_break], style_cls)
    return obj._transform_args()
