#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from n0ted0wn.Block.Parser.Base import Base

class Parser(object):
  def __init__(self, style_cls, indent_level=0):
    self.style_cls = style_cls
    self.indent_level = indent_level

  def parse(self, markup):
    # Dedent first
    if self.indent_level != 0:
      markup_lines = markup.split('\n')
      should_start_with = ' ' * self.indent_level
      for line in markup_lines:
        if line.strip() and not line.startswith(should_start_with):
          # Block not standardized, thus we don't even attempt to convert
          return [Base(markup, self.style_cls)]
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

      for block_rule in self.style_cls.block_rules():
        match_obj = block_rule.parse(block_raw, self.style_cls)
        if match_obj is not None:
          matched_block_rule = block_rule
          break

      if match_obj is None:
        # Treat block as dummy block if no block rule matches.
        blocks_processed.append(Base(block_raw, self.style_cls))
      elif match_obj is not Base.NOT_COMPLETE:
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
          match_obj = matched_block_rule.parse(block_raw, self.style_cls)
          if match_obj is None:
            break
          elif match_obj is not Base.NOT_COMPLETE:
            block_completed = True
            break
        blocks_processed.append(\
          match_obj if block_completed else Base(block_raw, self.style_cls))
    return blocks_processed
