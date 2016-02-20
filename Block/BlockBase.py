#!/usr/bin/env python
# -*- coding: utf-8 -*-

class BlockBase(object):
  """Base class for block rules.

  Attributes:
    raw: Raw block markup
  """

  _renderers = dict()

  def __init__(self, raw):
    """Initializes a block object.

    Args:
      raw: Raw text that supposedly corresponds to a block of this type.
    """
    self.raw = raw

  @classmethod
  def parse(cls, raw):
    """Parses the given raw text and return a block object representation, if
    applicable.

    Args:
      raw: Raw text to parse against

    Returns:
      None if the given raw text cannot be interpretated as a block of this
      type. Otherwise, returns the corresponding block object.
    """
    return cls(raw)

  def render(self, style, storage, env_storage):
    """Renders the block, given style class and storage object.

    Args:
      style_cls: Style class that identifies the style in which the rendering
                 should be in.
      storage: Storage singleton in which raw text that need further treatment
               should be stored.
      env_storage: Environment storage singleton that keeps track of any global
                   environment variables.

    Returns:
      Text representation of the block.
      str
    """
    if self.__class__ is BlockBase or style not in self._renderers:
      return self.raw
    return self._renderers[style](self, storage, env_storage)

BlockBase.NOT_COMPLETE = BlockBase(None)
