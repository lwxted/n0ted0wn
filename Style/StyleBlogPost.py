#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.BlockCode import BlockCode, BlockCodeStdEnv
from n0ted0wn.Block.BlockHeader import BlockHeader
from n0ted0wn.Block.BlockImage import BlockImage, BlockImageStdEnv
from n0ted0wn.Block.BlockOrderedList import BlockOrderedListStdEnv
from n0ted0wn.Block.BlockParagraph import BlockParagraph
from n0ted0wn.Block.BlockUnorderedList import BlockUnorderedListStdEnv
from n0ted0wn.Util.Identifier import StyleId
from n0ted0wn.Style.StyleBase import StyleBase

class StyleBlogPost(StyleBase):

  _identifier = StyleId.BLOG_POST

  _block_inline_rules = [
    (BlockHeader, None),
    (BlockOrderedListStdEnv, None),
    (BlockUnorderedListStdEnv, None),
    (BlockCode, None),
    (BlockCodeStdEnv, None),
    (BlockImage, None),
    (BlockImageStdEnv, None),
    (BlockParagraph, None),
  ]
