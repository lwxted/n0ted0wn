#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.Base import Base as ParserBase
from n0ted0wn.Block.Renderer.Base import Base as RendererBase
from n0ted0wn.Inline.InlineBase import InlineBase

class StyleBase(object):

  """override"""
  _identifier = 'base'

  """override"""
  _default_inline_rules = [
    # InlineRuleCls1,
    # InlineRuleCls2,
    InlineBase
  ]

  """override"""
  _block_inline_rules = [
    # (BlockRuleCls1, None),            # None will assume default inline rules
    # (BlockRuleCls2, [InlineRuleCls2]),
    (ParserBase, None)
  ]

  """override"""
  _renderers = {
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
    if block_rule_cls is ParserBase:
      return []
    if cls.__intn_block_inline_rules_mapping is None:
      cls.__intn_block_inline_rules_mapping = dict(cls.block_inline_rules())
    return cls.__intn_block_inline_rules_mapping[block_rule_cls]

  @classmethod
  def renderers_for_block_rule(cls, block_rule_cls):
    if block_rule_cls is ParserBase and ParserBase not in cls._renderers:
      return RendererBase
    assert block_rule_cls in cls._renderers
    return cls._renderers[block_rule_cls]

