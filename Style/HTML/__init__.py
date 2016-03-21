#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

# Block rules
from n0ted0wn.Block.Parser.DefinitionNoteWarn import \
  DefinitionStdEnv, NoteStdEnv, WarnStdEnv
from n0ted0wn.Block.Parser.Header import Header
from n0ted0wn.Block.Parser.Image import Image, ImageStdEnv
from n0ted0wn.Block.Parser.OrderedList import OrderedListStdEnv
from n0ted0wn.Block.Parser.Paragraph import Paragraph
from n0ted0wn.Block.Parser.Pre import Pre, PreStdEnv
from n0ted0wn.Block.Parser.UnorderedList import UnorderedListStdEnv

# Inline rules
from n0ted0wn.Inline.Parser.Base import Base as InlineParserBase
from n0ted0wn.Inline.Parser.Bold import Bold
from n0ted0wn.Inline.Parser.BoldItalic import BoldItalic
from n0ted0wn.Inline.Parser.Code import Code
from n0ted0wn.Inline.Parser.Del import Del
from n0ted0wn.Inline.Parser.Italic import Italic
from n0ted0wn.Inline.Parser.MathInline import MathInline
from n0ted0wn.Inline.Parser.Newline import Newline

# Block renderers
from n0ted0wn.Style.HTML.block_renderers import \
  RendererDefinition, RendererNote, RendererPre, RendererHeader, \
  RendererImage, RendererOrderedList, RendererParagraph, \
  RendererUnorderedList, RendererWarn

# Inline renderers
from n0ted0wn.Style.HTML.inline_renderers import \
  RendererBold, RendererBoldItalic, RendererCode, RendererDel, RendererItalic, \
  RendererMathInline, RendererNewline

from n0ted0wn.Style.StyleBase import StyleBase

class StyleHTML(StyleBase):

  _identifier = 'style_blog_post'

  _default_inline_rules = [
    Code,
    MathInline,
    BoldItalic,
    Bold,
    Italic,
    Del,
    Newline,
  ]

  _block_inline_rules = [
    (Header, None),
    (DefinitionStdEnv, None),
    (NoteStdEnv, None),
    (WarnStdEnv, None),
    (OrderedListStdEnv, None),
    (UnorderedListStdEnv, None),
    (Pre, [InlineParserBase]),
    (PreStdEnv, [InlineParserBase]),
    (Image, None),
    (ImageStdEnv, None),
    (Paragraph, None),
  ]

  _block_renderers = {
    Header : RendererHeader,
    OrderedListStdEnv : RendererOrderedList,
    UnorderedListStdEnv : RendererUnorderedList,
    Pre : RendererPre,
    PreStdEnv : RendererPre,
    Image : RendererImage,
    ImageStdEnv : RendererImage,
    Paragraph : RendererParagraph,
    DefinitionStdEnv : RendererDefinition,
    NoteStdEnv : RendererNote,
    WarnStdEnv : RendererWarn,
  }

  _inline_renderers = {
    Bold : RendererBold,
    BoldItalic : RendererBoldItalic,
    Code : RendererCode,
    Del : RendererDel,
    Italic : RendererItalic,
    MathInline : RendererMathInline,
    Newline : RendererNewline,
  }

  _escapeTable = [
    ('&', '&amp;'),   # & must be escaped first.
    ('<', '&lt;'),
    ('>', '&gt;'),
    ('"', '&quot;'),
    ('\'', '&#x27;'),
  ]

  @staticmethod
  def _final_process(s):
    """
    Reference: https://hg.python.org/cpython/file/3.4/Lib/html/__init__.py
    Replace special characters (&<>'") to HTML-safe sequences.
    """
    for (a, b) in StyleHTML._escapeTable:
      s = s.replace(a, b)
    return s
