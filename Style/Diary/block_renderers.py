#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Renderer.Base import Base as RendererBase
from n0ted0wn.Storage.Namespace import Environment, Option
from n0ted0wn.Storage.EnvironmentStorage import EnvironmentStorage

from n0ted0wn.Style.Diary.counters import MonthDayCounter
from n0ted0wn.Style.HTML.counters import TodoCounter

import datetime

def month_section_id(m):
  return u'm{0}'.format(m)

def day_div_id(m, d):
  return u'm{0}-d{1}'.format(m, d)

class RendererMonth(RendererBase):
  def _render(self, obj, storage, env_storage):
    month = datetime.date(1900, obj.month, 1).strftime('%B')
    month_day_counter = env_storage.get(Environment.MONTH_DAY,
      MonthDayCounter())
    month_day_counter.add_month(obj.month)
    month_str = unicode(month)
    month_title = u"""<div class="month-title"><h1>{0}</h1></div>"""\
      .format(month_str)
    from n0ted0wn.Block.Renderer import Renderer
    block_renderer = Renderer(self.style_cls, storage, env_storage)
    days_content = block_renderer.render(obj.content_blocks_list)
    return u"""
<section class="month" id="{2}">
  {0}
  <div class="days">{1}</div>
</section>""".format(month_title, days_content, month_section_id(obj.month))


class RendererDay(RendererBase):
  def _render(self, obj, storage, env_storage):
    month_day_counter = env_storage.get(Environment.MONTH_DAY,
      MonthDayCounter())
    month_day_counter.add_day(obj.day, obj.important)
    from n0ted0wn.Block.Renderer import Renderer
    # Sets up new environment storage every time, except we still wish to retain
    # the todo item counter for cbi consistency.
    env_storage_new = EnvironmentStorage.with_identical_options(env_storage)
    env_storage_new.set(Environment.TODO_ITEM_COUNTER, \
      env_storage.get(Environment.TODO_ITEM_COUNTER, TodoCounter()))
    block_renderer = Renderer(self.style_cls, storage, env_storage_new)
    contents = block_renderer.render(obj.content_blocks_list)
    return u"""
<div class="day">
  <div class="circle"></div>
  <span class="day-counter{3}" id="{2}">{0}</span>
  <div class="content">
    {1}
  </div>
</div>""".format(\
  obj.day,
  contents,
  day_div_id(month_day_counter.current_month(), obj.day),
  ' important-day' if obj.important else '')

class RendererTOC(RendererBase):
  def _render(self, obj, storage, env_storage):
    month_lis = []
    month_day_counter = env_storage.get(Environment.MONTH_DAY,
      MonthDayCounter())
    for (m, ds) in month_day_counter.get_month_days():
      month = datetime.date(1900, m, 1).strftime('%B')
      month_str = unicode(month)
      li_entry = u"""
<li>
  <a href="#{0}">{1}</a>
  <ul>
    {2}
  </ul>
</li>
""".format(month_section_id(m), month_str, '\n'.join(u"""<li{2}>
  <a href="#{1}">{0:0=2d}</a>
</li>""".format(
  d, day_div_id(m, d), ' class="important"' if im else '') \
  for (d, im) in sorted(list(ds))))
      month_lis.append(li_entry)

    return u"""
<div class="toc">
  <ul>{0}</ul>
</div>""".format('\n'.join(month_lis))
