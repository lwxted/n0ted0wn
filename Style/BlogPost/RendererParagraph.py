#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.Paragraph import Paragraph
from n0ted0wn.Block.Renderer.Base import Base as RendererBase

class RendererParagraph(RendererBase):
  def _render(self, obj, storage, env_storage):
    assert isinstance(obj, Paragraph)
    return """<p>{0}</p>"""\
    .format(self._format_key(storage.insert(obj.raw)))
