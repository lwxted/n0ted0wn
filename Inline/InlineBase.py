#!/usr/bin/env python
# -*- coding: utf-8 -*-

class InlineBase(object):
  """Base class for inline rules."""

  @staticmethod
  def render(raw_text, style_cls, storage):
    """Apply inline rule to the input `raw_text`.

    Replaces any occurrences of strings in `raw_text` that matches to this
    inline rule with a placeholder in the format of `\1` or `\12`. The number of
    the placeholder should correspond to an item in the input `storage` object.

    Args:
      raw_text: Raw text to which the inline rule should be applied against.
      style_cls: Style class that specifies the output style.
      storage: Storage object in which any intermediary text may be stored.

    Returns:
      Rendered text possibly with placeholders.
      str
    """
    return raw_text
