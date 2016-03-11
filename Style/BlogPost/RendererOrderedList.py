#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.OrderedList import OrderedListStdEnv
from n0ted0wn.Block.Renderer.Base import Base as RendererBase

class RendererOrderedList(RendererBase):
  def _render(self, obj, storage, env_storage):
    assert isinstance(obj, OrderedListStdEnv)
    from n0ted0wn.Block.Renderer import Renderer

    li_markups = []
    ol_markup = """<ol start="{0}">{1}</ol>"""

    for block_objs in obj.parsed_blocks_list:
      li_markup = """<li>{0}</li>""".format(
        Renderer(self.style_cls, storage, env_storage).render(block_objs))
      li_markups.append(li_markup)

    return ol_markup.format(obj.start_index, '\n'.join(li_markups))
