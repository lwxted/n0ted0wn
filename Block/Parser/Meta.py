#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.Base import Base

class Meta(Base):
  """
  Ignores meta block:

  ---
  meta_content
  ---
  """
  def __init__(self, raw, meta_content, style_cls):
    super(Meta, self).__init__(raw, style_cls)
    self.meta_content = meta_content

  @classmethod
  def parse(cls, raw, style_cls):
    raw_stripped = raw.strip()
    if not raw_stripped.startswith('---') or not raw_stripped.endswith('\n---'):
      return None
    first_line_break_index = raw_stripped.find('\n')
    meta_content = raw_stripped[first_line_break_index + 1:-4]
    if not meta_content:
      return None
    return Meta(raw, meta_content, style_cls)
