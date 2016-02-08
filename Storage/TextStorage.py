#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TextStorage(object):
  """Temporary storage for text."""

  __data = {}
  __next_index = 0

  def retrieve(self, index):
    return self.__data.pop(index)

  def insert(self, s):
    assert isinstance(s, str)
    self.__data[self.__next_index] = s
    self.__next_index += 1

  def recover(self, s):
    # TODO
    return s
