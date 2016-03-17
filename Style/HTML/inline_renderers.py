#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Inline.Renderer.Base import Base

class RendererItalic(Base):
  @classmethod
  def _render(cls, inline, final_process):
    return '<em>{0}</em>'.format(final_process(inline.content))

class RendererBold(Base):
  @classmethod
  def _render(cls, inline, final_process):
    return '<b>{0}</b>'.format(final_process(inline.content))

class RendererBoldItalic(Base):
  @classmethod
  def _render(cls, inline, final_process):
    return '<b><em>{0}</em></b>'.format(final_process(inline.content))

class RendererCode(Base):
  @classmethod
  def _render(cls, inline, final_process):
    return '<code>{0}</code>'.format(final_process(inline.content))

class RendererDel(Base):
  @classmethod
  def _render(cls, inline, final_process):
    return '<del>{0}</del>'.format(final_process(inline.content))

class RendererMathInline(Base):
  @classmethod
  def _render(cls, inline, final_process):
    return '<mathjax>\\({0}\\)</mathjax>'.format(final_process(inline.content))

class RendererNewline(Base):
  @classmethod
  def _render(cls, inline, final_process):
    return '<br />\n'
