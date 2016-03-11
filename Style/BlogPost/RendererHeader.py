#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.Header import Header
from n0ted0wn.Block.Renderer.Base import Base as RendererBase
from n0ted0wn.Storage.EnvironmentStorage import Environment

class HeaderCounter(object):
  def __init__(self):
    self.__data = [0] * 6

  def advance(self, level):
    self.__data[level - 1] += 1
    for i in xrange(level, 6):
      self.__data[i] = 0

  def current_level(self):
    return self.__data

  def __repr__(self):
    highest_level = 5
    while highest_level >= 0 and self.__data[highest_level] == 0:
      highest_level -= 1
    return '.'.join(str(self.__data[i]) for i in xrange(0, highest_level + 1))

class RendererHeader(RendererBase):
  def _render(self, obj, storage, env_storage):
    assert isinstance(obj, Header)
    header_counter = env_storage.get(
      Environment.CURRENT_HEADER_LEVEL, HeaderCounter())
    header_counter.advance(obj.level)

    toc = env_storage.get(Environment.TABLE_OF_CONTENTS, list())
    toc.append(obj)

    counter_span = """<span class="counter section-counter">{0}</span> """\
      .format(header_counter) if obj.numbered else ''

    return """<h{0}>{1}{2}</h{0}>"""\
      .format(
        obj.level + 1,
        counter_span,
        self._format_key(storage.insert(obj.title)))
