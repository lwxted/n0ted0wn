#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from n0ted0wn.Style.StyleBase import StyleBase
from n0ted0wn.Style.StyleBlogPost import StyleBlogPost

"""Upon the addition of a style class, the style class should be imported and
added into this array."""
all_styles = [
  StyleBase,
  StyleBlogPost
]

class Style(object):
  @classmethod
  def with_identifier(cls, identifier):
    assert identifier in cls.__all_style_mapping()
    return cls.__all_style_mapping()[identifier]

  __all_style_map = None

  @classmethod
  def __all_style_mapping(cls):
    if cls.__all_style_map is None:
      cls.__all_style_map = {
        style._identifier : style for style in all_styles
      }
    return cls.__all_style_map
