#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

class EnvironmentStorage(object):
  """Used for storing global environment variables / states, including but not
  limited to counters. Note that keys must be of str type."""

  def __init__(self, options=None):
    self.__data = {}
    if options is None:
      self.__options = {}
    else:
      assert isinstance(options, dict)
      self.__options = copy.deepcopy(options)

  def get(self, key, default_value):
    assert isinstance(key, str)
    if key not in self.__data:
      self.__data[key] = default_value
    return self.__data[key]

  def set(self, key, value):
    assert isinstance(key, str)
    self.__data[key] = value

  def get_option(self, key):
    assert isinstance(key, str)
    return self.__options.get(key, None)
