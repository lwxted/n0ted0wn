#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.BlockBase import BlockBase
from n0ted0wn.Block.BlockStdEnv import BlockStdEnv
from n0ted0wn.Util.Identifier import StyleId
from n0ted0wn.Util import Util

def renderer_blog_post(code_obj, storage, env_storage):
  lang = ' lang="{0}"'.format(code_obj.lang) if code_obj.lang else ''
  return """<pre><code{0}>{1}</code></pre>"""\
    .format(lang, Util.f(storage.insert(code_obj.content)))


class BlockCode(BlockBase):
  """
  Implements parsing for the following block formats.

  1. Specify only the code block
  ```
  code_content
  ```

  2. Specify the code block + the language
  ```code_lang
  code_content
  ```
  """

  _renderers = {
    StyleId.BLOG_POST : renderer_blog_post
  }

  def __init__(self, raw, lang, content):
    super(BlockCode, self).__init__(raw)
    self.lang = lang
    self.content = content

  @classmethod
  def parse(cls, raw):
    raw_stripped = raw.strip()
    if raw_stripped[0:3] != '```':
      return None
    if raw.strip()[-4:] != '\n```':
      return BlockBase.NOT_COMPLETE
    first_line_break_index = raw_stripped.find('\n')
    lang = raw_stripped[3:first_line_break_index].strip()
    content = raw_stripped[first_line_break_index + 1:-4]
    if not content:
      return None
    return BlockCode(raw, lang, content)


class BlockCodeStdEnv(BlockStdEnv):
  """
  Implements parsing for the following block formats.

  1. Specify only the code block
  {code}
  code_content
  {code}

  2. Specify the code block + the language
  {code:code_lang}
  code_content
  {code}
  """

  _block_type = 'code'

  _renderers = {
    StyleId.BLOG_POST : renderer_blog_post
  }

  def __init__(self, raw, params, content):
    super(BlockCodeStdEnv, self).__init__(raw, params, content)
    self.lang = ''

  def _transform_args(self):
    if self._params:
      self.lang = self._params[0]
    return self
