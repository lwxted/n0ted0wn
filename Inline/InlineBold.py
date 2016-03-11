#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Inline.InlineBase import InlineBase

class InlineBold(InlineBase):

  @staticmethod
  def render(raw_text, final_process_func, storage, env_storage):
    return raw_text
