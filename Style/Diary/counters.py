#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MonthDayCounter(object):
  def __init__(self):
    self.__months_days = []

  def add_month(self, m):
    self.__months_days.append((m, set()))

  def add_day(self, d, important=False):
    self.__months_days[-1][1].add((d, important))

  def get_month_days(self):
    return self.__months_days

  def current_month(self):
    return self.__months_days[-1][0]
