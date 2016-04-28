#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator
import re

from n0ted0wn.Inline.Parser.Base import Base

class Ruby(Base):
  @classmethod
  def parse(cls, raw):
    l1 = [cls(\
      raw, m.span(), (raw[slice(*m.span(1))], raw[slice(*m.span(2))])) \
      for m in re.finditer(r'\[(\w+?)\]<(\w+?)>', raw, re.UNICODE)]
    l2 = [cls(\
      raw, m.span(), (raw[slice(*m.span(1))], raw[slice(*m.span(2))])) \
      for m in re.finditer(ur'【(\w+?)】《(\w+?)》', raw, re.UNICODE)]
    l3 = [cls(\
      raw, m.span(), (raw[slice(*m.span(1))], raw[slice(*m.span(2))])) \
      for m in re.finditer(ur'「(\w+?)」＜(\w+?)＞', raw, re.UNICODE)]
    return sorted(l1 + l2 + l3, key=operator.attrgetter('span'))
