#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.converter import convert

if __name__ == '__main__':
  print convert(u"""
```
Article markup:

---
type:     diary
title:    #InnoDxMtTeam
author:   Ted Li
time:     2016/03/21 10:20:00 UTC+0400
modified: 2016/03/22 10:20:00 UTC+0400
---

[MetaInfo module]: meta information -->
  1. parses and understands meta info
     --> title, author, time, modified, type
     makes available to post_obj = Post(title...)

[HTMLGathering module]: type -->
  1. gather necessary resources based on a pre-defined map:
     - based on configs, choose correct n0ted0wn style + option
     - gather: html template, (S)CSS files, JS files based on a mapping
  2. These gathered info will be made available to flask by something like:
     render_template(
       MI.html, css_resources=MI.css, js_resources=MI.js, post=post_obj)

[n0ted0wn module]: style + markup + (options) --> rendered content
<div class="content">
  [rendered content]
</div>
```
""", u'style_blog_post')

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

