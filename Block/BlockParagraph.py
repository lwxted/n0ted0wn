#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.BlockBase import BlockBase
from n0ted0wn.Util import Util


def renderer_blog_post(p_obj, storage, env_storage):
  return """<p>{0}</p>""".format(Util.f(storage.insert(p_obj.raw)))


class BlockParagraph(BlockBase):
  _renderers = {
    'blog_post' : renderer_blog_post
  }

  def __init__(self, raw):
    super(BlockParagraph, self).__init__(raw)

  @classmethod
  def parse(cls, raw):
    return BlockParagraph(raw)
