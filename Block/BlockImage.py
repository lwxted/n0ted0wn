#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.BlockStdEnv import BlockStdEnv
from n0ted0wn.Storage.EnvironmentStorage import Environment
from n0ted0wn.Util import Util

def renderer_blog_post(image_obj, storage, env_storage):
  if image_obj.numbered:
    image_counter = env_storage.get(Environment.CURRENT_IMAGE, ImageCounter())
    image_counter.advance()

  figure_counter = """
    <div class="image-counter-block">
      <span class="counter image-counter">Figure {0}</span>
    </div>""".format(image_counter) if image_obj.numbered else ''

  return """
<div class="figure clearfix">
  <div class="img clearfix">
    <img src="{0}" alt="{1}" />
  </div>
  <div class="caption">{2}
    <span class="caption-text">{3}</span>
  </div>
</div>""".format(
    image_obj.image_url,
    Util.html_attribute(image_obj.alt_caption),
    figure_counter,
    Util.f(storage.insert(image_obj.description)))

class ImageCounter(object):
  def __init__(self):
    self.__count = 0

  def advance(self):
    self.__count += 1

  def __repr__(self):
    return str(self.__count)

class BlockImageStdEnv(BlockStdEnv):
  """
  Implements parsing for the following formats.

  1. Simple url / description
     {img}
     path/to/image.png
     Description that must fit into one line.
     {img}

  2. Full format url + alt + description
     {img}
     url: path/to/image.png
     alt: Some alt
     desc: Some description that should fit into one line.
     {img}
  """

  _block_type = 'img'

  _renderers = {
    'blog_post' : renderer_blog_post
  }

  def __init__(self, raw, params, content):
    super(BlockImageStdEnv, self).__init__(raw, params, content)
    self.image_url = ''
    self.alt_caption = ''
    self.description = ''
    self.numbered = True

  def _transform_args(self):
    lines = self.content.split('\n')
    full_format = False
    if len(lines) >= 3 and \
      lines[0].startswith('url: ') and \
      lines[1].startswith('alt: ') and \
      lines[2].startswith('desc: '):
      full_format = True
    if not full_format:
      self.image_url = lines[0]
      if len(lines) > 1:
        self.description = lines[1]
    else:
      self.image_url = lines[0][5:]
      self.alt_caption = lines[1][5:]
      self.description = lines[2][6:]
    self.numbered = 'nonum' not in self._params
