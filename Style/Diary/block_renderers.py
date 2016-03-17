#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.Block.Renderer.Base import Base as RendererBase
from n0ted0wn.Storage.EnvironmentStorage import Environment

from n0ted0wn.Style.Diary.counters import MonthDayCounter

import datetime

def month_section_id(m):
  month = datetime.date(1900, m, 1).strftime('%B')
  month_str = str(month)
  return 'diary_month-' + month_str

def day_div_id(m, d):
  month = datetime.date(1900, m, 1).strftime('%B')
  month_str = str(month)
  return 'diary_day-{0}-{1}'.format(month_str, d)

class RendererMonth(RendererBase):
  def _render(self, obj, storage, env_storage):
    month = datetime.date(1900, obj.month, 1).strftime('%B')
    month_day_counter = env_storage.get(Environment.MONTH_DAY,
      MonthDayCounter())
    month_day_counter.add_month(obj.month)
    month_str = str(month)
    month_title = """<div class="month-title"><h1>{0}</h1></div>"""\
      .format(month_str)
    from n0ted0wn.Block.Renderer import Renderer
    block_renderer = Renderer(self.style_cls, storage, env_storage)
    days_content = block_renderer.render(obj.content_blocks_list)
    return """
<section class="month" id="{2}">
  {0}
  <div class="days">{1}</div>
</section>""".format(month_title, days_content, month_section_id(obj.month))


class RendererDay(RendererBase):
  def _render(self, obj, storage, env_storage):
    month_day_counter = env_storage.get(Environment.MONTH_DAY,
      MonthDayCounter())
    month_day_counter.add_day(obj.day)
    from n0ted0wn.Block.Renderer import Renderer
    block_renderer = Renderer(self.style_cls, storage, env_storage)
    contents = block_renderer.render(obj.content_blocks_list)
    return """
<div class="day">
  <div class="circle"></div>
  <span class="day-counter" id="{2}">{0}</span>
  <div class="content">
    {1}
  </div>
</div>""".format(\
  obj.day, contents, day_div_id(month_day_counter.current_month(), obj.day))

class RendererHide(RendererBase):
  def _render(self, obj, storage, env_storage):
    return ''

class RendererTOC(RendererBase):
  def _render(self, obj, storage, env_storage):
    month_lis = []
    month_day_counter = env_storage.get(Environment.MONTH_DAY,
      MonthDayCounter())
    for (m, ds) in month_day_counter.get_month_days():
      month = datetime.date(1900, m, 1).strftime('%B')
      month_str = str(month)
      li_entry = """
<li>
  <a href="#{0}">{1}</a>
  <ul>
    {2}
  </ul>
</li>
""".format(month_section_id(m), month_str, '\n'.join("""<li>
  <a href="#{1}">{0}</a>
</li>""".format(d, day_div_id(m, d)) for d in ds))
      month_lis.append(li_entry)

    return """
<div class="toc">
  <ul>{0}</ul>
</div>""".format('\n'.join(month_lis))