#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.UnorderedList import UnorderedListStdEnv
from n0ted0wn.Block.Renderer.Base import Base as RendererBase

class RendererUnorderedList(RendererBase):
  def _render(self, obj, storage, env_storage):
    assert isinstance(obj, UnorderedListStdEnv)
    from n0ted0wn.Block.Renderer import Renderer

    li_markups = []
    ul_markup = """<ul>{0}</ul>"""

    for block_objs in obj.parsed_blocks_list:
      li_markup = """<li>{0}</li>""".format(
        Renderer(self.style_cls, storage, env_storage).render(block_objs))
      li_markups.append(li_markup)

    return ul_markup.format('\n'.join(li_markups))
