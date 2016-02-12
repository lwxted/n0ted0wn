#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.BlockBase import BlockBase
from n0ted0wn.Block.BlockHeader import BlockHeader
from n0ted0wn.Style.StyleBase import StyleBase

class StyleBlogPost(StyleBase):

  _identifier = 'blog_post'

  _block_inline_rules = [
    (BlockHeader, None),
    (BlockBase, None),
  ]
