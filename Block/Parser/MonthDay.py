#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.StdEnv import StdEnv

class MonthStdEnv(StdEnv):
  """
  Implements parsing for the following block formats.

  1. Month
  {month:7}
  {day:19}
  Content here...
  {day}
  {month}
  """

  _block_type = 'month'

  def __init__(self, raw, params, content, style_cls):
    super(MonthStdEnv, self).__init__(raw, params, content, style_cls)
    self.content_blocks_list = []
    self.month = 0

  def _transform_args(self):
    from n0ted0wn.Block.Parser import Parser
    if not self._params:
      return None
    try:
      self.month = int(self._params.keys()[0])
    except ValueError:
      return None
    self.content_blocks_list = Parser(self.style_cls, 0).parse(self.content)
    return self


class DayStdEnv(StdEnv):
  _block_type = 'day'

  def __init__(self, raw, params, content, style_cls):
    super(DayStdEnv, self).__init__(raw, params, content, style_cls)
    self.content_blocks_list = []
    self.day = 0
    self.important = False

  def _transform_args(self):
    from n0ted0wn.Block.Parser import Parser
    if not self._params:
      return None
    try:
      self.day = int(self._params.keys()[0])
      self.important = len(self._params.keys()) > 1 and \
        self._params.keys()[1] == '!'
    except ValueError:
      return None
    self.content_blocks_list = Parser(self.style_cls, 0).parse(self.content)
    return self
