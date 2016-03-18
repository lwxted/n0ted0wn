#!/usr/bin/env python
# -*- coding: utf-8 -*-

class HeaderCounter(object):
  def __init__(self):
    self.__data = [0] * 6

  def advance(self, level):
    self.__data[level - 1] += 1
    for i in xrange(level, 6):
      self.__data[i] = 0

  def current_level(self):
    return self.__data

  def __repr__(self):
    highest_level = 5
    while highest_level >= 0 and self.__data[highest_level] == 0:
      highest_level -= 1
    return '.'.join(unicode(self.__data[i]) for i in xrange(0, highest_level + 1))

class ImageCounter(object):
  def __init__(self):
    self.__count = 0

  def advance(self):
    self.__count += 1

  def __repr__(self):
    return unicode(self.__count)
