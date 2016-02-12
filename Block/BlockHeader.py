#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.BlockBase import BlockBase
from n0ted0wn.Util import Util

class BlockHeader(BlockBase):

  def __init__(self, raw_text, header_level, title):
    super(BlockHeader, self).__init__(raw_text)
    self.header_level = header_level
    self.title = title

  @classmethod
  def parse(cls, raw_text):
    raw_text = raw_text.strip('\n')
    if '\n' in raw_text or raw_text[0] != '#':
      return None
    header_level = 1
    while header_level < 6:
      if len(raw_text) < header_level + 1:
        break
      if raw_text[header_level] == '#':
        header_level += 1
      else:
        break
    if header_level >= len(raw_text) or raw_text[header_level] != ' ':
      return None
    return BlockHeader(raw_text, header_level, raw_text[header_level + 1:])

  # FIXME: identifier shit
  def render(self, style_cls, storage):
    if style_cls._identifier not in renderers:
      return self.raw
    return renderers[style_cls._identifier](self, storage)

def renderer_blog_post(header_obj, storage):
  return '<h{0}>{1}</h{0}>\n'.format(
    header_obj.header_level, Util.f(storage.insert(header_obj.title)))

renderers = {
  'blog_post' : renderer_blog_post
}

