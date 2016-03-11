#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from n0ted0wn.Block.Parser.Code import Code, CodeStdEnv
from n0ted0wn.Block.Parser.Header import Header
from n0ted0wn.Block.Parser.Image import Image, ImageStdEnv
from n0ted0wn.Block.Parser.OrderedList import OrderedListStdEnv
from n0ted0wn.Block.Parser.Paragraph import Paragraph
from n0ted0wn.Block.Parser.UnorderedList import UnorderedListStdEnv

from n0ted0wn.Inline.InlineBase import InlineBase
from n0ted0wn.Inline.InlineBold import InlineBold

from n0ted0wn.Style.BlogPost.RendererHeader import RendererHeader
from n0ted0wn.Style.BlogPost.RendererOrderedList import RendererOrderedList
from n0ted0wn.Style.BlogPost.RendererUnorderedList import RendererUnorderedList
from n0ted0wn.Style.BlogPost.RendererCode import RendererCode
from n0ted0wn.Style.BlogPost.RendererImage import RendererImage
from n0ted0wn.Style.BlogPost.RendererParagraph import RendererParagraph

from n0ted0wn.Style.StyleBase import StyleBase

class StyleBlogPost(StyleBase):

  _identifier = 'style_blog_post'

  _default_inline_rules = [
    InlineBold,
    InlineBase
  ]

  _block_inline_rules = [
    (Header, None),
    (OrderedListStdEnv, None),
    (UnorderedListStdEnv, None),
    (Code, None),
    (CodeStdEnv, None),
    (Image, None),
    (ImageStdEnv, None),
    (Paragraph, None),
  ]

  _renderers = {
    Header : RendererHeader,
    OrderedListStdEnv : RendererOrderedList,
    UnorderedListStdEnv : RendererUnorderedList,
    Code : RendererCode,
    CodeStdEnv : RendererCode,
    Image : RendererImage,
    ImageStdEnv : RendererImage,
    Paragraph : RendererParagraph,
  }

  @staticmethod
  def _final_process(s):
    return s
