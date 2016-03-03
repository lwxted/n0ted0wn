#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.BlockStdEnv import BlockStdEnv
from n0ted0wn.Util.Identifier import StyleId

def renderer_blog_post(list_obj, storage, env_storage):
  from n0ted0wn.Parser.BlockRenderer import BlockRenderer

  li_markups = []
  ul_markup = """<ul>{0}</ul>"""

  for block_objs in list_obj.parsed_blocks_list:
    li_markup = """<li>{0}</li>""".format(
      BlockRenderer(StyleId.BLOG_POST, storage, env_storage).render(block_objs))
    li_markups.append(li_markup)

  return ul_markup.format('\n'.join(li_markups))

class BlockUnorderedListStdEnv(BlockStdEnv):
  """
  Implements parsing for the following block format.
  """

  _block_type = 'ul'

  _renderers = {
    StyleId.BLOG_POST : renderer_blog_post
  }

  def __init__(self, raw, params, content):
    super(BlockUnorderedListStdEnv, self).__init__(raw, params, content)
    self.parsed_blocks_list = []

  def _transform_args(self):
    item_marker_index = self.content.find('* ')
    if item_marker_index == -1:
      return None

    lines = self.content.split('\n')
    grouped_lines = []
    for l in lines:
      if l.startswith('  ') or not l.strip():
        grouped_lines[-1].append(l)
      else:
        counter_marker = '* '
        if not l.startswith(counter_marker):
          return None
        grouped_lines.append([' ' * len(counter_marker) + \
          l[len(counter_marker):]])

    from n0ted0wn.Parser.BlockParser import BlockParser

    for lines in grouped_lines:
      self.parsed_blocks_list.append(
        BlockParser(StyleId.DEFAULT, 2).parse('\n'.join(lines)))
    return self
