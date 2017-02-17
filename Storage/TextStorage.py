#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Util import Util

class TextStorage(object):
  """Temporary storage for text."""

  def __init__(self):
    super(TextStorage, self).__init__()
    self.__data = {}
    self.__next_index = 0

  def get(self, index):
    assert index in self.__data
    return self.__data[index]

  def insert(self, s):
    assert isinstance(s, unicode)
    index = self.__next_index
    self.__data[self.__next_index] = s
    self.__next_index += 1
    return index

  def update(self, n, s):
    assert isinstance(n, int) and isinstance(s, unicode) and n in self.__data
    self.__data[n] = s

  def recover(self, s, storage_keys=None):
    """Attempt to replace any placeholder substring with its original string. If
    `storage_keys` is specified, it will only look into the specified keys.

    Args:
      s: String to recover
      storage_keys: Specific storage keys to look into (default: {None})

    Returns:
      Recovered string
      str
    """
    if storage_keys is None:
      storage_keys = self.__data.keys()
    for n in storage_keys:
      key = Util.f(n)
      if key not in s:
        continue
      s = s.replace(key, self.recover(self.__data.pop(n)))
    return s
