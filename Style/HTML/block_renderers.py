#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from n0ted0wn.Block.Renderer.Base import Base as RendererBase
from n0ted0wn.Storage.Namespace import Environment
from n0ted0wn.Style.HTML.counters import HeaderCounter, ImageCounter
from n0ted0wn.Util import Util

def header_id(header_counter_str, header_obj):
  return u"""s{0}""".format(header_counter_str.replace('.', '-'))

class RendererPre(RendererBase):
  def _render(self, obj, storage, env_storage):
    lang = u' lang="{0}"'.format(obj.lang) if obj.lang else ''
    return u"""<pre{0}><code>{1}</code></pre>"""\
      .format(lang, self._format_key(storage.insert(obj.content)))

class RendererHeader(RendererBase):
  def _render(self, obj, storage, env_storage):
    header_counter = env_storage.get(
      Environment.CURRENT_HEADER_LEVEL, HeaderCounter())
    header_counter.advance(obj.level)

    toc = env_storage.get(Environment.TABLE_OF_CONTENTS, list())
    toc.append((str(header_counter), obj))

    counter_span = u"""<span class="counter section-counter">{0}</span> """\
      .format(header_counter) if obj.numbered else ''

    return u"""<h{0} id="{3}">{1}{2}</h{0}>"""\
      .format(
        obj.level + 1,
        counter_span,
        self._format_key(storage.insert(obj.title)),
        header_id(str(header_counter), obj))

class RendererImage(RendererBase):
  def _render(self, obj, storage, env_storage):
    if obj.numbered:
      image_counter = env_storage.get(Environment.CURRENT_IMAGE, \
        ImageCounter())
      image_counter.advance()

    figure_counter_span = u"""
      <div class="image-counter-block">
        <span class="counter image-counter">Figure {0}</span>
      </div>""".format(image_counter) if obj.numbered else ''

    caption_span = u"""
      <span class="caption-text">{0}</span>"""\
      .format(self._format_key(storage.insert(obj.description))) \
      if obj.description else ''

    caption_div = u"""
    <div class="caption">{0}{1}
    </div>""".format(figure_counter_span, caption_span) \
      if figure_counter_span or caption_span else ''

    return u"""
  <div class="figure clearfix">
    <div class="img clearfix">
      <img src="{0}" alt="{1}" />
    </div>{2}
  </div>""".format(
      obj.image_url,
      Util.html_attribute(obj.alt_caption),
      caption_div)

class RendererOrderedList(RendererBase):
  def _render(self, obj, storage, env_storage):
    from n0ted0wn.Block.Renderer import Renderer

    block_renderer = Renderer(self.style_cls, storage, env_storage)
    li_markups = []
    ol_markup = u"""<ol start="{0}">{1}</ol>"""

    for block_objs in obj.parsed_blocks_list:
      li_markup = u"""<li>{0}</li>""".format(block_renderer.render(block_objs))
      li_markups.append(li_markup)

    return ol_markup.format(obj.start_index, '\n'.join(li_markups))

class RendererUnorderedList(RendererBase):
  def _render(self, obj, storage, env_storage):
    from n0ted0wn.Block.Renderer import Renderer

    block_renderer = Renderer(self.style_cls, storage, env_storage)
    li_markups = []
    ul_markup = u"""<ul>{0}</ul>"""

    for block_objs in obj.parsed_blocks_list:
      li_markup = u"""<li>{0}</li>""".format(block_renderer.render(block_objs))
      li_markups.append(li_markup)

    return ul_markup.format('\n'.join(li_markups))

class RendererParagraph(RendererBase):
  def _render(self, obj, storage, env_storage):
    return u"""<p>{0}</p>"""\
    .format(self._format_key(storage.insert(obj.raw)))

class RendererDefinition(RendererBase):
  def _render(self, obj, storage, env_storage):
    from n0ted0wn.Block.Renderer import Renderer

    block_renderer = Renderer(self.style_cls, storage, env_storage)
    explanation_markups = block_renderer.render(obj.explanation_blocks_list)
    return u"""
<div class="definition">
  <div class="title">{0}</div>
  <div class="explanation">
    {1}
  </div>
</div>""".format(obj.title, explanation_markups)

class RendererNote(RendererBase):
  def _render(self, obj, storage, env_storage):
    from n0ted0wn.Block.Renderer import Renderer

    block_renderer = Renderer(self.style_cls, storage, env_storage)
    explanation_markups = block_renderer.render(obj.explanation_blocks_list)
    return u"""
<div class="note">
  <div class="title">{0}</div>
  <div class="explanation">
    {1}
  </div>
</div>""".format(obj.title, explanation_markups)

class RendererWarn(RendererBase):
  def _render(self, obj, storage, env_storage):
    from n0ted0wn.Block.Renderer import Renderer

    block_renderer = Renderer(self.style_cls, storage, env_storage)
    explanation_markups = block_renderer.render(obj.explanation_blocks_list)
    return u"""
<div class="warn">
  <div class="title">{0}</div>
  <div class="explanation">
    {1}
  </div>
</div>""".format(obj.title, explanation_markups)

class RendererColor(RendererBase):
  def _render(self, obj, storage, env_storage):
    from n0ted0wn.Block.Renderer import Renderer

    block_renderer = Renderer(self.style_cls, storage, env_storage)
    markups = block_renderer.render(obj.blocks_list)
    return u"""<div style="color: {0};">{1}</div>""".format(
      Util.html_attribute(obj.color), markups)

class RendererTrivial(RendererBase):
  def _render(self, obj, storage, env_storage):
    from n0ted0wn.Block.Renderer import Renderer

    block_renderer = Renderer(self.style_cls, storage, env_storage)
    markups = block_renderer.render(obj.blocks_list)
    return u"""<div style="color: gray;">{0}</div>""".format(markups)

class RendererEmphasis(RendererBase):
  def _render(self, obj, storage, env_storage):
    return u"""<div class="emph">{0}</div>""".format(
      self._format_key(storage.insert(obj.text)))

class RendererCenter(RendererBase):
  def _render(self, obj, storage, env_storage):
    from n0ted0wn.Block.Renderer import Renderer

    block_renderer = Renderer(self.style_cls, storage, env_storage)
    markups = block_renderer.render(obj.blocks_list)
    return u"""<div class="center">{0}</div>""".format(markups)

class RendererMeta(RendererBase):
  def _render(self, obj, storage, env_storage):
    return u""

class RendererSeparator(RendererBase):
  def _render(self, obj, storage, env_storage):
    return u"\n<hr />\n"

class RendererTOC(RendererBase):
  def __render_toc(self, toc, cnt, storage, env_storage):
    start_level = toc[cnt][1].level
    li_list = []
    while cnt < len(toc):
      (header_counter, header_obj) = toc[cnt]
      if header_obj.level < start_level:
        break
      elif header_obj.level == start_level:
        li_list.append(u"""
<li>
  <a href="#{0}"><span class="counter toc-counter">{1}</span> {2}</a>
</li>
"""\
          .format(
            header_id(header_counter, header_obj),
            header_counter,
            self._format_key(storage.insert(header_obj.title))
          )
        )
        cnt += 1
      elif header_obj.level > start_level:
        (prev_header_counter, prev_header_obj) = toc[cnt - 1]
        (new_cnt, rendered_children) = self.__render_toc(
          toc, cnt, storage, env_storage)
        li_list[-1] = u"""
<li>
  <a href="#{0}"><span class="counter toc-counter">{1}</span> {2}</a>
  <ul>{3}</ul>
</li>
"""\
        .format(
          header_id(prev_header_counter, prev_header_obj),
          prev_header_counter,
          self._format_key(storage.insert(prev_header_obj.title)),
          rendered_children
        )
        cnt = new_cnt
    return (cnt, '\n'.join(li_list))

  def _render(self, obj, storage, env_storage):
    toc = env_storage.get(Environment.TABLE_OF_CONTENTS, list())
    (_, rendered) = self.__render_toc(toc, 0, storage, env_storage)
    return u"""
<div class="toc">
  <ul>{0}</ul>
</div>""".format(rendered)
