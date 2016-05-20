#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Inline.Renderer.Base import Base
from n0ted0wn.Util import Util

class RendererItalic(Base):
  @classmethod
  def _render(cls, inline, final_process):
    return u'<em>{0}</em>'.format(final_process(inline.content))

class RendererBold(Base):
  @classmethod
  def _render(cls, inline, final_process):
    return u'<b>{0}</b>'.format(final_process(inline.content))

class RendererBoldItalic(Base):
  @classmethod
  def _render(cls, inline, final_process):
    return u'<b><em>{0}</em></b>'.format(final_process(inline.content))

class RendererCode(Base):
  @classmethod
  def _render(cls, inline, final_process):
    return u'<code>{0}</code>'.format(final_process(inline.content))

class RendererDel(Base):
  @classmethod
  def _render(cls, inline, final_process):
    return u'<del>{0}</del>'.format(final_process(inline.content))

class RendererMathInline(Base):
  @classmethod
  def _render(cls, inline, final_process):
    return u'<mathjax>\\({0}\\)</mathjax>'.format(final_process(inline.content))

class RendererNewline(Base):
  @classmethod
  def _render(cls, inline, final_process):
    return u'<br />\n'

class RendererRuby(Base):
  @classmethod
  def _render(cls, inline, final_process):
    return u'<ruby>{0}<rt>{1}</rt></ruby>'.format(
      final_process(inline.content[0]), final_process(inline.content[1]))

class RendererHyperlink(Base):
  @classmethod
  def _render(cls, inline, final_process):
    return u'<a href="{0}">{1}</a>'.format(
      Util.html_attribute(inline.content[0]), final_process(inline.content[1]))
