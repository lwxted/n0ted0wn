#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Parser.Base import Base
from n0ted0wn.Block.Parser.StdEnv import StdEnv

class Image(Base):
  """
  Implements parsing for the following block format.

  ![Caption text](Image URL)
  """

  def __init__(self, raw, alt_caption, image_url, style_cls):
    super(Image, self).__init__(raw, style_cls)
    self.alt_caption = alt_caption
    self.image_url = image_url
    self.description = ''
    self.numbered = False

  @classmethod
  def parse(cls, raw, style_cls):
    raw = raw.strip()
    if raw[0:2] != '![' or raw[-1:] != ')':
      return None
    sep_index = raw.find('](')
    if sep_index == -1:
      return None
    return cls(raw, raw[2:sep_index], raw[sep_index + 2:-1], style_cls)


class ImageStdEnv(StdEnv):
  """
  Implements parsing for the following block formats.

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

  3. Specify whether or not the image should be numbered.
     {img:no#}
     path/to/image.png
     Description that must fit into one line.
     {img}
  """

  _block_type = 'img'

  def __init__(self, raw, params, content, style_cls):
    super(ImageStdEnv, self).__init__(raw, params, content, style_cls)
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
    self.numbered = 'no#' not in self._params
    return self
