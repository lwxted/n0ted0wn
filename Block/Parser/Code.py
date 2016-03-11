#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.Base import Base
from n0ted0wn.Block.Parser.StdEnv import StdEnv

class Code(Base):
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
    super(Code, self).__init__(raw, style_cls)
    self.lang = lang
    self.content = content

  @classmethod
  def parse(cls, raw, style_cls):
    raw_stripped = raw.strip()
    if raw_stripped[0:3] != '```':
      return None
    if raw.strip()[-4:] != '\n```':
      return Base.NOT_COMPLETE
    first_line_break_index = raw_stripped.find('\n')
    lang = raw_stripped[3:first_line_break_index].strip()
    content = raw_stripped[first_line_break_index + 1:-4]
    if not content:
      return None
    return Code(raw, lang, content, style_cls)


class CodeStdEnv(StdEnv):
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

  def __init__(self, raw, params, content, style_cls):
    super(CodeStdEnv, self).__init__(raw, params, content, style_cls)
    self.lang = ''

  def _transform_args(self):
    if self._params:
      self.lang = self._params[0]
    return self
