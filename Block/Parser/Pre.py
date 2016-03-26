#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.Base import Base
from n0ted0wn.Block.Parser.StdEnv import StdEnv

class Pre(Base):
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
  def __init__(self, raw, lang, content, style_cls):
    super(Pre, self).__init__(raw, style_cls)
    self.lang = lang
    self.content = content

  @classmethod
  def parse(cls, raw, style_cls):
    raw_stripped = raw.strip()
    if not raw_stripped.startswith('```'):
      return None
    if not raw_stripped.endswith('\n```'):
      return Base.NOT_COMPLETE
    first_line_break_index = raw_stripped.find('\n')
    lang = raw_stripped[3:first_line_break_index].strip()
    content = raw_stripped[first_line_break_index + 1:-4]
    if not content:
      return None
    return Pre(raw, lang, content, style_cls)


class PreStdEnv(StdEnv):
  """Implements parsing for the following block formats.

  1. Specify only the code block
  {pre}
  code_content
  {pre}

  2. Specify the code block + the language
  {pre:code_lang}
  code_content
  {pre}
  """

  _block_type = 'pre'

  def __init__(self, raw, params, content, style_cls):
    super(PreStdEnv, self).__init__(raw, params, content, style_cls)
    self.lang = ''

  def _transform_args(self):
    if self._params:
      self.lang = self._params[0]
    return self
