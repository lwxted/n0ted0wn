#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

# Block rules
from n0ted0wn.Block.Parser.Center import CenterStdEnv
from n0ted0wn.Block.Parser.Color import ColorStdEnv, TrivialStdEnv
from n0ted0wn.Block.Parser.DefinitionNoteWarn import \
  DefinitionStdEnv, NoteStdEnv, WarnStdEnv
from n0ted0wn.Block.Parser.Emphasis import Emphasis
from n0ted0wn.Block.Parser.Header import Header
from n0ted0wn.Block.Parser.Image import Image, ImageStdEnv
from n0ted0wn.Block.Parser.Meta import Meta
from n0ted0wn.Block.Parser.OrderedList import OrderedList, \
  OrderedListStdEnv
from n0ted0wn.Block.Parser.Paragraph import Paragraph
from n0ted0wn.Block.Parser.Pre import Pre, PreStdEnv
from n0ted0wn.Block.Parser.Separator import Separator
from n0ted0wn.Block.Parser.TOC import TOCStdEnv
from n0ted0wn.Block.Parser.TodoList import TodoList, TodoListStdEnv
from n0ted0wn.Block.Parser.UnorderedList import UnorderedList, \
  UnorderedListStdEnv

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
  RendererCenter, RendererColor, RendererDefinition, RendererEmphasis, \
  RendererNote, RendererPre, RendererHeader, RendererImage, \
  RendererMeta, RendererOrderedList, RendererParagraph, RendererSeparator, \
  RendererTrivial, RendererUnorderedList, RendererWarn, RendererTOC, \
  RendererTodoList

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
    (Meta, [InlineParserBase]),
    (TOCStdEnv, []),
    (CenterStdEnv, None),
    (Header, None),
    (Emphasis, None),
    (DefinitionStdEnv, None),
    (NoteStdEnv, None),
    (WarnStdEnv, None),
    (TrivialStdEnv, None),
    (ColorStdEnv, None),
    (TodoList, None),
    (TodoListStdEnv, None),
    (OrderedListStdEnv, None),
    (OrderedList, None),
    (UnorderedListStdEnv, None),
    (UnorderedList, None),
    (Separator, [InlineParserBase]),
    (Pre, [InlineParserBase]),
    (PreStdEnv, [InlineParserBase]),
    (Image, None),
    (ImageStdEnv, None),
    (Paragraph, None),
  ]

  _block_renderers = {
    Header : RendererHeader,
    OrderedListStdEnv : RendererOrderedList,
    OrderedList : RendererOrderedList,
    UnorderedListStdEnv : RendererUnorderedList,
    UnorderedList : RendererUnorderedList,
    Pre : RendererPre,
    PreStdEnv : RendererPre,
    Image : RendererImage,
    ImageStdEnv : RendererImage,
    Paragraph : RendererParagraph,
    DefinitionStdEnv : RendererDefinition,
    NoteStdEnv : RendererNote,
    WarnStdEnv : RendererWarn,
    ColorStdEnv : RendererColor,
    TrivialStdEnv : RendererTrivial,
    Emphasis : RendererEmphasis,
    CenterStdEnv : RendererCenter,
    Meta : RendererMeta,
    Separator : RendererSeparator,
    TOCStdEnv : RendererTOC,
    TodoList : RendererTodoList,
    TodoListStdEnv : RendererTodoList,
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
