#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class Base(object):
  """Base class for inline rules.

  Attributes:
    raw: Raw text of the original string to be parsed
    span: Tuple containing the start and end positions of matched inline string.
  """

  def __init__(self, raw, span, content):
    self.raw = raw
    self.span = span
    self.content = content

  @classmethod
  def parse(cls, raw):
    """Parses the given raw text and return a list of inline objects,
    if applicable.

    Args:
      raw: Raw text to parse against

    Returns:
      Empty list if the given raw text contains no matching inline
      representation. Otherwise, returns a list of inline objects.
    """
    return []

class SlashNum(Base):
  """Created for dealing with our internal transform. (We are replacing stuff
  with backslash (\\) followed by a number. To prevent accidental
  transformations, we would like escape them upfront.)
  """

  @classmethod
  def parse(cls, raw):
    return [cls(raw, m.span(), raw[slice(*m.span(0))]) for m in \
      re.finditer(r'\\[1-9][0-9]*', raw)]
