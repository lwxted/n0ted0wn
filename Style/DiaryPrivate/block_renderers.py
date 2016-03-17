#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Renderer.Base import Base as RendererBase

class RendererHide(RendererBase):
  def _render(self, obj, storage, env_storage):
    from n0ted0wn.Block.Renderer import Renderer
    block_renderer = Renderer(self.style_cls, storage, env_storage)
    contents = block_renderer.render(obj.content_blocks_list)
    return contents
