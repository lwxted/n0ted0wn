#!/usr/bin/env python
# -*- coding: utf-8 -*-

class StyleBase(object):
  _identifier = 'base'

  _inline_rules = [
    # InlineRuleCls1,
    # InlineRuleCls2,
  ]

  _block_inline_rules = [
    # (BlockRuleCls1, None),            # None will assume default inline rules
    # (BlockRuleCls2, [InlineRuleCls2]),
  ]

  __block_inline_rules = None
  __block_rules = None
  __block_inline_rules_mapping = None

  @classmethod
  def block_inline_rules(cls):
    if cls.__block_inline_rules is None:
      cls.__block_inline_rules = [\
        (br, cls._inline_rules if ir is None else ir) \
        for (br, ir) in cls._block_inline_rules\
      ]
    return cls.__block_inline_rules

  @classmethod
  def block_rules(cls):
    if cls.__block_rules is None:
      cls.__block_rules = [rule[0] for rule in cls._block_inline_rules]
    return cls.__block_rules

  @classmethod
  def inline_rules_for_block_rule(cls):
    if cls.__block_inline_rules_mapping is None:
      cls.__block_inline_rules_mapping = dict(cls.__block_inline_rules)
    return cls.__block_inline_rules_mapping
