#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.BlockBase import BlockBase
from n0ted0wn.Inline.InlineBase import InlineBase

class StyleBase(object):

  """override"""
  _identifier = 'base'

  """override"""
  _inline_rules = [
    # InlineRuleCls1,
    # InlineRuleCls2,
    InlineBase
  ]

  """override"""
  _block_inline_rules = [
    # (BlockRuleCls1, None),            # None will assume default inline rules
    # (BlockRuleCls2, [InlineRuleCls2]),
    (BlockBase, None)
  ]

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
        (br, cls._inline_rules if ir is None else ir) \
        for (br, ir) in cls._block_inline_rules\
      ]
    return cls.__intn_block_inline_rules

  @classmethod
  def block_rules(cls):
    if cls.__intn_block_rules is None:
      cls.__intn_block_rules = [rule[0] for rule in cls.block_inline_rules()]
    return cls.__intn_block_rules

  @classmethod
  def inline_rules_for_block_rule(cls, block_rule):
    if cls.__intn_block_inline_rules_mapping is None:
      cls.__intn_block_inline_rules_mapping = dict(cls.block_inline_rules())
    return cls.__intn_block_inline_rules_mapping[block_rule]
