#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from n0ted0wn.Style.StyleBase import StyleBase
from n0ted0wn.Style.HTML import StyleHTML
from n0ted0wn.Style.Diary import StyleDiary
from n0ted0wn.Style.DiaryPrivate import StyleDiaryPrivate

"""Upon the addition of a style class, the style class should be imported and
added into this array."""
all_styles = [
  StyleBase,
  StyleHTML,
  StyleDiary,
  StyleDiaryPrivate
]

class Style(object):
  @classmethod
  def all_identifers(cls):
    return cls.__all_style_mapping().keys()

  @classmethod
  def with_identifier(cls, identifier):
    assert identifier in cls.__all_style_mapping()
    return cls.__all_style_mapping()[identifier]

  __all_style_map = None

  @classmethod
  def __all_style_mapping(cls):
    if cls.__all_style_map is None:
      cls.__all_style_map = {
        unicode(style._identifier) : style for style in all_styles
      }
    return cls.__all_style_map
