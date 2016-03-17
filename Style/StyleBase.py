#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.Base import Base as BlockParserBase
from n0ted0wn.Block.Renderer.Base import Base as BlockRendererBase
from n0ted0wn.Inline.Parser.Base import Base as InlineParserBase, SlashNum
from n0ted0wn.Inline.Renderer.Base import Base as InlineRendererBase

class StyleBase(object):

  """override"""
  _identifier = 'base'

  """override"""
  _default_inline_rules = [
    # InlineRuleCls1,
    # InlineRuleCls2,
    InlineParserBase
  ]

  """override"""
  _block_inline_rules = [
    # (BlockRuleCls1, None),            # None will assume default inline rules
    # (BlockRuleCls2, [InlineRuleCls2]),
    (BlockParserBase, None)
  ]

  """override"""
  _block_renderers = {
    # Renderers
  }

  """override"""
  _inline_renderers = {
    # Renderers
  }

  """override"""
  @staticmethod
  def _final_process(s):
    """Gives users an opportunity to performent a final processing on any
    text that will be committed.

    This can be used, for example in the case of an HTML style, to escape
    any necessary characters.
    """
    return s

  #############################################################################
  #############################################################################
  #############################################################################

  __intn_block_inline_rules = None
  __intn_block_rules = None
  __intn_block_inline_rules_mapping = None

  @classmethod
  def block_inline_rules(cls):
    cls._default_inline_rules = [SlashNum] + cls._default_inline_rules
    if cls.__intn_block_inline_rules is None:
      cls.__intn_block_inline_rules = [\
        (br, cls._default_inline_rules if ir is None else ir) \
        for (br, ir) in cls._block_inline_rules\
      ]
    return cls.__intn_block_inline_rules

  @classmethod
  def block_rules(cls):
    if cls.__intn_block_rules is None:
      cls.__intn_block_rules = [rule[0] for rule in cls.block_inline_rules()]
    return cls.__intn_block_rules

  @classmethod
  def inline_rules_for_block_rule(cls, block_rule_cls):
    if block_rule_cls is BlockParserBase:
      return []
    if cls.__intn_block_inline_rules_mapping is None:
      cls.__intn_block_inline_rules_mapping = dict(cls.block_inline_rules())
    return cls.__intn_block_inline_rules_mapping[block_rule_cls]

  @classmethod
  def renderer_for_block_rule(cls, block_rule_cls):
    if block_rule_cls is BlockParserBase and \
      BlockParserBase not in cls._block_renderers:
      return BlockRendererBase
    assert block_rule_cls in cls._block_renderers
    return cls._block_renderers[block_rule_cls]

  @classmethod
  def renderer_for_inline_rule(cls, inline_rule_cls):
    if inline_rule_cls is SlashNum:
      return InlineRendererBase
    if inline_rule_cls is InlineParserBase and \
      InlineParserBase not in cls._inline_renderers:
      return InlineRendererBase
    assert inline_rule_cls in cls._inline_renderers
    return cls._inline_renderers[inline_rule_cls]

  @classmethod
  def final_process_func(cls):
    return cls._final_process
