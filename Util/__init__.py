#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Util(object):
  @staticmethod
  def format_inline_key(n):
    return '\\{0}'.format(n)

  f = format_inline_key

  @staticmethod
  def html_attribute(s):
    # FIXME
    return s
