#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.Base import Base

class Separator(Base):
  def __init__(self, raw, style_cls):
    super(Separator, self).__init__(raw, style_cls)

  @classmethod
  def parse(cls, raw, style_cls):
    if raw.strip() == '---':
      return cls(raw, style_cls)
    else:
      return None
