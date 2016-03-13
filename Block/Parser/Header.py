#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.Base import Base

class Header(Base):
  """
  Implements parsing for the following block formats.

  1. Numbered header
  # Level 1
  ## Level 2
  ### Level 3
  #### Level 4
  ##### Level 5
  ###### Level 6

  2. Unnumbered header
  = Level 1
  == Level 2
  === Level 3
  ==== Level 4
  ===== Level 5
  ====== Level 6

  3. Quick subtitle
  + Title
  """

  def __init__(self, raw, numbered, level, title, style_cls):
    super(Header, self).__init__(raw, style_cls)
    self.level = level
    self.title = title
    self.numbered = numbered

  @classmethod
  def parse(cls, raw, style_cls):
    raw = raw.strip('\n')
    if '\n' in raw or (raw[0] != '#' and raw[0] != '=' and raw[0] != '+'):
      return None
    header_identifier = raw[0]
    header_numbered = (header_identifier == '#')
    level = 1
    while level < 6:
      if len(raw) < level + 1:
        break
      if raw[level] == header_identifier:
        level += 1
      else:
        break
    if level >= len(raw) or raw[level] != ' ':
      return None
    if header_identifier != '+':
      return Header(raw, header_numbered, level, raw[level + 1:], style_cls)
    else:
      return Header(raw, False, 5, raw[2:], style_cls)
