#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.BlockBase import BlockBase
from n0ted0wn.Storage.EnvironmentStorage import Environment
from n0ted0wn.Util import Util
from n0ted0wn.Util.Identifier import StyleId

def renderer_blog_post(header_obj, storage, env_storage):
  header_counter = env_storage.get(
    Environment.CURRENT_HEADER_LEVEL, BlockHeaderCounter())
  header_counter.advance(header_obj.level)

  toc = env_storage.get(Environment.TABLE_OF_CONTENTS, list())
  toc.append(header_obj)

  counter_span = """<span class="counter section-counter">{0}</span> """\
    .format(header_counter) if header_obj.numbered else ''

  return """<h{0}>{1}{2}</h{0}>"""\
    .format(
      header_obj.level,
      counter_span,
      Util.f(storage.insert(header_obj.title)))


class BlockHeaderCounter(object):
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


class BlockHeader(BlockBase):
  _renderers = {
    StyleId.BLOG_POST : renderer_blog_post
  }

  def __init__(self, raw, numbered, level, title):
    super(BlockHeader, self).__init__(raw)
    self.level = level
    self.title = title
    self.numbered = numbered

  @classmethod
  def parse(cls, raw):
    raw = raw.strip('\n')
    if '\n' in raw or (raw[0] != '#' and raw[0] != '='):
      return None
    header_identifier = raw[0]
    header_numbered = (header_identifier == '#')
    level = 1
    while level < 6:
      if len(raw) < level + 1:
        break
      if raw[level] == header_identifier:
        level += 1
      else:
        break
    if level >= len(raw) or raw[level] != ' ':
      return None
    return BlockHeader(
      raw, header_numbered, level, raw[level + 1:])

