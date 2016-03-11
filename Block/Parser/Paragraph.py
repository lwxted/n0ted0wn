#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.Base import Base

class Paragraph(Base):

  def __init__(self, raw, style_cls):
    super(Paragraph, self).__init__(raw, style_cls)

  @classmethod
  def parse(cls, raw, style_cls):
    return Paragraph(raw, style_cls)
