#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.converter import convert

if __name__ == '__main__':
  print convert(u"""
{todo}
* [ ] Test only
* [x] Another test
* [X] Here is one more
* [ ] Another one
  .
  This?&"<>
  Test only...

  * [ ] Another nested todo list!
  * [x] Like this 1
  * [X] Like this 2
{todo}
""", u'style_diary', {'diary_display_hidden' : True})

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

