#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Environment(object):
  CURRENT_HEADER_LEVEL = 'block_current_header_level_counter'
  CURRENT_IMAGE = 'image_counter'
  TABLE_OF_CONTENTS = 'table_of_contents'
  MONTH_DAY = 'month_day'

  __all_environments = None

  @classmethod
  def all(cls):
    if cls.__all_environments is None:
      cls.__all_environments = set([\
        attr for attr in dir(cls) if not callable(attr) and \
        not attr.startswith("__")])
    return cls.__all_environments

class Option(object):
  DIARY_DISPLAY_HIDDEN = 'diary_display_hidden'

  __all_options = None

  @classmethod
  def all(cls):
    if cls.__all_options is None:
      cls.__all_options = set([\
        attr for attr in dir(cls) if not callable(attr) and \
        not attr.startswith("__")])
    return cls.__all_options

