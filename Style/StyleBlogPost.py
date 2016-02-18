#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.BlockCode import BlockCode, BlockCodeStdEnv
from n0ted0wn.Block.BlockImage import BlockImageStdEnv
from n0ted0wn.Block.BlockParagraph import BlockParagraph
from n0ted0wn.Block.BlockHeader import BlockHeader
from n0ted0wn.Style.StyleBase import StyleBase

class StyleBlogPost(StyleBase):

  _identifier = 'blog_post'

  _block_inline_rules = [
    (BlockHeader, None),
    (BlockCode, None),
    (BlockCodeStdEnv, None),
    (BlockImageStdEnv, None),
    (BlockParagraph, None),
  ]
