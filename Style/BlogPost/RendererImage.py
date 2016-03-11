#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.Image import Image, ImageStdEnv
from n0ted0wn.Block.Renderer.Base import Base as RendererBase
from n0ted0wn.Storage.EnvironmentStorage import Environment
from n0ted0wn.Util import Util

class ImageCounter(object):
  def __init__(self):
    self.__count = 0

  def advance(self):
    self.__count += 1

  def __repr__(self):
    return str(self.__count)

class RendererImage(RendererBase):
  def _render(self, obj, storage, env_storage):
    assert isinstance(obj, Image) or isinstance(obj, ImageStdEnv)
    if obj.numbered:
      image_counter = env_storage.get(Environment.CURRENT_IMAGE, ImageCounter())
      image_counter.advance()

    figure_counter_span = """
      <div class="image-counter-block">
        <span class="counter image-counter">Figure {0}</span>
      </div>""".format(image_counter) if obj.numbered else ''

    caption_span = """
      <span class="caption-text">{0}</span>"""\
      .format(self._format_key(storage.insert(obj.description))) \
      if obj.description else ''

    caption_div = """
    <div class="caption">{0}{1}
    </div>""".format(figure_counter_span, caption_span) \
      if figure_counter_span or caption_span else ''

    return """
  <div class="figure clearfix">
    <div class="img clearfix">
      <img src="{0}" alt="{1}" />
    </div>{2}
  </div>""".format(
      obj.image_url,
      Util.html_attribute(obj.alt_caption),
      caption_div)
