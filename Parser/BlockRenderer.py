#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Style import Style

class BlockRenderer(object):
  def __init__(self, style, text_storage, env_storage):
    self.style = Style.with_identifier(style)
    self.text_storage = text_storage
    self.env_storage = env_storage

  def render(self, blocks):
    blocks_rendered = []
    # For each processed block
    for block in blocks:
      rendered = block.render(
        self.style._identifier, self.text_storage, self.env_storage)
      for inline_rule_cls in self.style.inline_rules_for_block_rule(
        block.__class__):
        rendered = inline_rule_cls.render(
          rendered, self.style, self.text_storage, self.env_storage)
      blocks_rendered.append(self.text_storage.recover(rendered).strip())

    return '\n'.join(blocks_rendered)
