#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Environment(object):
  CURRENT_HEADER_LEVEL = 'block_current_header_level'
  TABLE_OF_CONTENTS = 'table_of_contents'

  __all_environments = None

  @classmethod
  def all(cls):
    if cls.__all_environments is None:
      cls.__all_environments = set([\
        attr for attr in dir(cls) if not callable(attr) and \
        not attr.startswith("__")])
    return cls.__all_environments


class EnvironmentStorage(object):
  """Used for storing global environment variables / states, including but not
  limited to counters. Note that keys must be of str type."""

  __data = {}

  def get(self, key, default_value):
    assert isinstance(key, str)
    if key not in self.__data:
      self.__data[key] = default_value
    return self.__data[key]

  def set(self, key, value):
    assert isinstance(key, str)
    self.__data[key] = value
