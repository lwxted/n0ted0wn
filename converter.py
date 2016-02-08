#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Parses and converts the notedown markup to specified styles
"""

from n0ted0wn.Block.BlockBase import BlockBase
from n0ted0wn.Storage.TextStorage import TextStorage
from n0ted0wn.Style import Style

def convert(markup, flavor):
  style = Style.with_identifier(flavor)
  text_storage = TextStorage()

  blocks_raw = markup.split('\n\n')
  blocks_processed = []
  blocks_raw_iterator = iter(blocks_raw)

  # For each block
  for block_raw in blocks_raw_iterator:
    block_stripped = block_raw.strip()

    # Discard block if the block is empty after whitespaces around the string
    # are stripped.
    if not block_stripped:
      continue

    match_obj = None

    for block_rule in style.block_rules():
      match_obj = block_rule.parse(block_raw)
      if match_obj:
        break

    if match_obj is None:
      # Treat block as dummy block if no block rule matches.
      blocks_processed.append(BlockBase(block_raw))
    elif match_obj.is_complete(block_raw):
      # Append to block list if some block rule matches and is a complete block.
      blocks_processed.append(match_obj)
    else:
      # If block is not complete, attempt to merge with the next block, and then
      # reevaluate until either no more blocks are available, or when the block
      # is considered to be completed.
      block_completed = False
      while True:
        next_block = next(blocks_raw_iterator, None)
        if next_block is None:
          break
        block_raw += '\n\n' + next_block
        if match_obj.is_complete(block_raw):
          block_completed = True
          break
      blocks_processed.append(\
        match_obj if block_completed else BlockBase(block_raw))

  # For each processed block
  for block in blocks_processed:
    rendered = block.render(style, text_storage)
    for inline_rule_cls in style.inline_rules_for_block_rule(block.__class__):
      rendered = inline_rule_cls.render(rendered, style, text_storage)

  text_recovered = text_storage.recover(rendered)
  return text_recovered
