#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Util import Util

class Base(object):
  """Base class for inline renderers.

  Each style is expected to implement its own renderers that should subclass
  this base class.
  """

  """override"""
  @classmethod
  def _render(cls, inline, final_process):
    return inline.raw[slice(*inline.span)]

  #############################################################################
  #############################################################################
  #############################################################################

  @classmethod
  def _format_key(cls, n):
    return Util.f(n)

  @classmethod
  def render(cls, inline, final_process):
    return cls._render(inline, final_process)
