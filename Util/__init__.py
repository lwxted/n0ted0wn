#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Util(object):
  @staticmethod
  def format_inline_key(n):
    return u'\\{0}'.format(n)

  f = format_inline_key

  @staticmethod
  def html_attribute(s, quote=True):
    """
    Replace special characters "&", "<" and ">" to HTML-safe sequences.
    If the optional flag quote is true (the default), the quotation mark
    characters, both double quote (") and single quote (') characters are also
    translated.

    Source: https://hg.python.org/cpython/file/3.5/Lib/html/__init__.py
    """
    s = s.replace("&", "&amp;") # Must be done first!
    s = s.replace("<", "&lt;")
    s = s.replace(">", "&gt;")
    if quote:
        s = s.replace('"', "&quot;")
        s = s.replace('\'', "&#x27;")
    return s
