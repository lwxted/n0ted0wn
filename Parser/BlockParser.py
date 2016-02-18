#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.BlockBase import BlockBase

class BlockParser(object):
  def __init__(self, style, text_storage, env_storage, indent_level=0):
    self.style = style
    self.text_storage = text_storage
    self.env_storage = env_storage
    self.indent_level = indent_level

  def convert(self, markup):
    # Dedent first
    if self.indent_level != 0:
      markup_lines = markup.split('\n')
      for line in markup_lines:
        for c in line[0:self.indent_level]:
          if c != ' ':
            # Block not standardized, thus we don't even attempt to convert
            return markup
      markup = '\n'.join(line[self.indent_level:] for line in markup_lines)

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
      matched_block_rule = None

      for block_rule in self.style.block_rules():
        match_obj = block_rule.parse(block_raw)
        if match_obj is not None:
          matched_block_rule = block_rule
          break

      if match_obj is None:
        # Treat block as dummy block if no block rule matches.
        blocks_processed.append(BlockBase(block_raw))
      elif match_obj is not BlockBase.NOT_COMPLETE:
        # Append to block list if some block rule matches and is a complete
        # block.
        blocks_processed.append(match_obj)
      else:
        # If block is not complete, attempt to merge with the next block, and
        # then reevaluate until either no more blocks are available, or when
        # the block is considered to be completed.
        block_completed = False
        while True:
          next_block = next(blocks_raw_iterator, None)
          if next_block is None:
            break
          block_raw += '\n\n' + next_block
          match_obj = matched_block_rule.parse(block_raw)
          if match_obj is not BlockBase.NOT_COMPLETE:
            block_completed = True
            break
        blocks_processed.append(\
          match_obj if block_completed else BlockBase(block_raw))

    blocks_rendered = []

    # For each processed block
    for block in blocks_processed:
      rendered = block.render(
        self.style._identifier, self.text_storage, self.env_storage)
      for inline_rule_cls in self.style.inline_rules_for_block_rule(
        block.__class__):
        rendered = inline_rule_cls.render(
          rendered, self.style, self.text_storage, self.env_storage)
      blocks_rendered.append(self.text_storage.recover(rendered).strip())

    return '\n'.join(blocks_rendered)
