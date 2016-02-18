#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Parses and converts the notedown markup to specified styles
"""

from n0ted0wn.Parser.BlockParser import BlockParser
from n0ted0wn.Storage.TextStorage import TextStorage
from n0ted0wn.Storage.EnvironmentStorage import EnvironmentStorage
from n0ted0wn.Style import Style

def convert(markup, flavor):
  style = Style.with_identifier(flavor)
  text_storage = TextStorage()
  env_storage = EnvironmentStorage()

  return BlockParser(style, text_storage, env_storage).convert(markup)
