#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Parses and converts the notedown markup to specified styles
"""

from n0ted0wn.Block.Parser import Parser
from n0ted0wn.Block.Renderer import Renderer
from n0ted0wn.Storage.TextStorage import TextStorage
from n0ted0wn.Storage.EnvironmentStorage import EnvironmentStorage
from n0ted0wn.Style import Style

def convert(markup, flavor, options=None):
  text_storage = TextStorage()
  env_storage = EnvironmentStorage(options)
  style_cls = Style.with_identifier(flavor)

  block_parser = Parser(style_cls)
  block_renderer = Renderer(style_cls, text_storage, env_storage)

  return block_renderer.render(block_parser.parse(markup))
