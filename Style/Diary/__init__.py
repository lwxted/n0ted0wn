#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from n0ted0wn.Block.Parser.Hide import HideStdEnv
from n0ted0wn.Block.Parser.MonthDay import DayStdEnv, MonthStdEnv
from n0ted0wn.Block.Parser.TOC import TOCStdEnv

from n0ted0wn.Style.Diary.block_renderers import RendererDay, RendererHide, \
  RendererMonth, RendererTOC

from n0ted0wn.Style.HTML import StyleHTML

class StyleDiary(StyleHTML):

  _identifier = 'style_diary'

  _block_inline_rules = [
    (HideStdEnv, None),
    (MonthStdEnv, None),
    (DayStdEnv, None),
  ]

  _block_renderers = {
    MonthStdEnv : RendererMonth,
    DayStdEnv : RendererDay,
    HideStdEnv : RendererHide,
    TOCStdEnv : RendererTOC,
  }

StyleDiary._block_renderers = dict(StyleHTML._block_renderers.items() + \
  StyleDiary._block_renderers.items())
StyleDiary._block_inline_rules += StyleHTML._block_inline_rules
