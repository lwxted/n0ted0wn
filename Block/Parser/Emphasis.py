#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.Base import Base

class Emphasis(Base):
  """Implements parsing for the following block format.

  + Sentence to be emphasized...
  """

  def __init__(self, raw, text, style_cls):
    super(Emphasis, self).__init__(raw, style_cls)
    self.text = text

  @classmethod
  def parse(cls, raw, style_cls):
    raw = raw.strip()
    if raw[0:2] != '+ ':
      return None
    return cls(raw, raw[2:], style_cls)
