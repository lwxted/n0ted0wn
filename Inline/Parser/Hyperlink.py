#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator
import re

from n0ted0wn.Inline.Parser.Base import Base

class Hyperlink(Base):
  __url_regex = r'(?:https?:\/\/)?(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}' + \
                r'\.[a-z]{2,6}\b(?:[-a-zA-Z0-9@:%_\+.~#?&//=]*)'

  @classmethod
  def parse(cls, raw):
    l1 = [cls(\
      raw, m.span(), (raw[slice(*m.span(2))], raw[slice(*m.span(1))])) \
      for m in re.finditer(\
        r'\[(.+?)\]\((' + Hyperlink.__url_regex + r')\)', raw, re.UNICODE)]
    l2 = [cls(\
      raw, m.span(), (raw[slice(*m.span(1))], raw[slice(*m.span(1))])) \
      for m in re.finditer(\
        r'(?:^|\s+)(' + Hyperlink.__url_regex + r')(?:$|\s+)', raw, re.UNICODE)]
    return sorted(l1 + l2, key=operator.attrgetter('span'))
