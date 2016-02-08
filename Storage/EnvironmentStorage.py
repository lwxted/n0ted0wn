#!/usr/bin/env python
# -*- coding: utf-8 -*-

class EnvironmentStorage(object):
  """Used for storing global environment variables / states, including but not
  limited to counters. Note that keys must be of str type."""

  __data = {}

  def retrieve(self, key):
    assert isinstance(key, str) and key in self.__data
    return self.__data[key]

  def insert(self, key, value):
    assert isinstance(key, str)
    self.__data[key] = value
