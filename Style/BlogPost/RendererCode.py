#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.Code import Code, CodeStdEnv
from n0ted0wn.Block.Renderer.Base import Base as RendererBase

class RendererCode(RendererBase):
  def _render(self, obj, storage, env_storage):
    assert isinstance(obj, Code) or isinstance(obj, CodeStdEnv)
    lang = ' lang="{0}"'.format(obj.lang) if obj.lang else ''
    return """<pre{0}><code>{1}</code></pre>"""\
      .format(lang, self._format_key(storage.insert(obj.content)))
