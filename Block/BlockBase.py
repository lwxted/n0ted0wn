#!/usr/bin/env python
# -*- coding: utf-8 -*-

class BlockBase(object):
  """Base class for block rules.

  Attributes:
    __raw: Raw block markup
    data: Data field that may be used to represent the block object.
  """

  __raw = ''

  data = None

  def __init__(self, raw_text):
    """Initializes a block object.

    Args:
      raw_text: Raw text that supposedly corresponds to a block of this type.
    """
    self.__raw = raw_text

  @staticmethod
  def is_complete(s):
    """Checks whether the block that has a specific block type is complete.

    Optional block end check. If implemented, when the block rule is evaluated,
    the converter engine will check whether the end of block is encountered. If
    not, the converter will attempt to look for a next block, merge the two
    blocks and then resolve the merged block.

    Args:
      s: Text block to check against.

    Returns:
      Whether block is complete.
      bool
    """
    return True

  @classmethod
  def parse(cls, raw_text):
    """Parses the given raw text and return a block object representation, if
    applicable.

    Args:
      raw_text: Raw text to parse against

    Returns:
      None if the given raw text cannot be interpretated as a block of this
      type. Otherwise, returns the corresponding block object.
    """
    return cls(raw_text)

  def render(self, style_cls, storage):
    """Renders the block, given style class and storage object.

    Args:
      style_cls: Style class that identifies the style in which the rendering
                 should be in.
      storage_cls: Storage class in which raw text that need further treatment
                   should be stored.

    Returns:
      Text representation of the block.
      str
    """
    return self.__raw
