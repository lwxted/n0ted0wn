#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Base(object):
  """Base class for block rules.

  Attributes:
    raw: Raw block markup
  """

  def __init__(self, raw, style_cls):
    """Initializes a block object.

    Args:
      raw: Raw text that supposedly corresponds to a block of this type.
    """
    super(Base, self).__init__()
    self.raw = raw
    self.style_cls = style_cls

  @classmethod
  def parse(cls, raw, style_cls):
    """Parses the given raw text and return a block object representation, if
    applicable.

    Args:
      raw: Raw text to parse against

    Returns:
      None if the given raw text cannot be interpretated as a block of this
      type. Otherwise, returns the corresponding block object.
    """
    return cls(raw, style_cls)

Base.NOT_COMPLETE = Base(None, None)
