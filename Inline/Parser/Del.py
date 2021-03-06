#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from n0ted0wn.Inline.Parser.Base import Base

class Del(Base):
  @classmethod
  def parse(cls, raw):
    return [cls(raw, m.span(), raw[slice(*m.span(1))]) for m in \
      re.finditer(r'~~(.+?)~~', raw)]
