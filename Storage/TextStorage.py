#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Util import Util

class TextStorage(object):
  """Temporary storage for text."""

  __data = {}
  __next_index = 0

  def retrieve(self, index):
    return self.__data.pop(index)

  def insert(self, s):
    assert isinstance(s, str)
    index = self.__next_index
    self.__data[self.__next_index] = s
    self.__next_index += 1
    return index

  def recover(self, s):
    for n in self.__data.keys():
      key = Util.f(n)
      if key not in s:
        continue
      s = s.replace(key, self.__data[n])
      del self.__data[n]
    return s
