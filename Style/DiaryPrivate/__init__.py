#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from n0ted0wn.Block.Parser.Hide import HideStdEnv

from n0ted0wn.Style.Diary import StyleDiary
from n0ted0wn.Style.DiaryPrivate.block_renderers import RendererHide

class StyleDiaryPrivate(StyleDiary):

  _identifier = 'style_diary_private'

  _block_renderers = StyleDiary._block_renderers.copy()

StyleDiaryPrivate._block_renderers[HideStdEnv] = RendererHide
