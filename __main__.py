#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.converter import convert

if __name__ == '__main__':
  print convert("""
== test

# Only

```
only
a
test
`

test
```

Of course this is only a test.

Don't take it too seriously...
For real....

{code}
Does this even work??
{code}

{code:c}
How about this?

OR this crazy shit?

```
d
```


asdgas
{code}
""", 'blog_post')
