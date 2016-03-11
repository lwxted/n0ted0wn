#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Util import Util

class Base(object):
  """Base class for block renderers.

  Each style is expected to implement its own renderers that should subclass
  this base class.

  Attributes:
    storage_keys: Stores text storage keys that should be recovered.
  """

  def __init__(self, style_cls):
    super(Base, self).__init__()
    self._storage_keys = set()
    self.style_cls = style_cls

  """override"""
  def _render(self, block, storage, env_storage):
    return block.raw

  #############################################################################
  #############################################################################
  #############################################################################

  def _format_key(self, n):
    self._storage_keys.add(n)
    return Util.f(n)

  def render(self, block, storage, env_storage):
    """Renders the block, given block object and storage objects. Note that any
    text that is expected to be further processed by inline rules should be
    stored in the text storage.

    Args:
      block: The block to be rendered
      storage: Storage singleton in which raw text that need further treatment
               should be stored.
      env_storage: Environment storage singleton that keeps track of any global
                   environment variables.

    Returns:
      A tuple containing: (1) text representation of the block, (2) a set of
      stored keys that should be further processed and recovered.
    """
    return (self._render(block, storage, env_storage), self._storage_keys)
