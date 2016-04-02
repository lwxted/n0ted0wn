#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.converter import convert

if __name__ == '__main__':
  print convert(u"""
---
Meta_content...
---

# This is serious...

## But this is only a test

### This also

### That also

## How about this?

# Any problems?

#### What about this???

{note}
Take note:
绝大多数时候，凑合着做完，比完美地半途而废要好。
绝大多数时候，决定要做就直接开始，比自认为准备充分了再开始要好。
脑内山水千万里，不如脚下一步。哪怕是跌出去的一步。

这个思维方式是我花了很长时间很大精力去养成的，至今都没有完全贯彻到行动中去，但多少有点进步。如果能真正实行，拖延症估计就好了吧。
{note}

{toc}
{toc}
""", u'style_blog_post', {})

# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

# from n0ted0wn.converter import convert

# if __name__ == '__main__':
#   print convert("""
# # Test only!

# ## Test here

# == Or here?

# {ol}
# 1. __This is to demonstrate how we'll approach this list block!!!__
# 2. There can be one-line strings
# 3. Or multiline
#    strings
# 4. Or multiple

#    paragraphs
# 5. Or even blocks within blocks! Like this:

#    {img}
#    https://upload.wikimedia.org/wikipedia/commons/a/ae/Facebook_Headquarters_Entrance_Sign_Menlo_Park.jpg
#    Seriously amazing!
#    {img}

#    ```
#    And other blocks

#    Like this!!
#    ```
# 6. And finally, another list block within this!

#    {ol}
#    1. Like this 1
#    2. Like this 2
#    {ol}
# {ol}

# {ul}
# * This is to demonstrate how we'll approach this list block
# * There can be one-line strings
# * Or multiline
#   strings
# * Or multiple

#   paragraphs
# * Or even blocks within blocks! Like this:

#   {img}
#   https://upload.wikimedia.org/wikipedia/commons/a/ae/Facebook_Headquarters_Entrance_Sign_Menlo_Park.jpg
#   Seriously amazing!
#   {img}

#   ```
#   And other blocks

#   Like this!!
#   ```
# * And finally, another list block within this!

#   {ol}
#   1. Like this 1
#   2. Like this 2
#   {ol}
# {ul}

# The only way we know that we are out is by looking at the indentation that we
# are actually out.


# """, 'style_blog_post')

