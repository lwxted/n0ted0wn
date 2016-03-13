#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Inline.Renderer.Base import Base

class RendererDel(Base):
  @classmethod
  def _render(cls, inline, final_process):
    return '<del>{0}</del>'.format(final_process(inline.content))
