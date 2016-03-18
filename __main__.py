#!/usr/bin/env python
# -*- coding: utf-8 -*-

from n0ted0wn.converter import convert

if __name__ == '__main__':
  print convert(u"""
{month:3}
{day:18}
+ The long awaited brand-new blog is actually happening.

+ Current time is 1:56AM.

+ Signing out and actually getting some rest for the coming days.
{day}
{month}

{toc}
""", u'style_diary')

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

"""![](http://tedli.me/blog/api/uploads/1425582333_pipeline.png)

Vertex operations: lighting, shading, transformation, clipping [Own vertex shader]
Primitive assembly: make geometry points / lines / triangles
Rasterization: geometry objects turned into pixels
Fragment operations: [Own fragment shader]
Image assembly: stencil buffer, accumulation buffer

# Basic math for Computer graphics

## Points and vectors

Usually represented in column-vector forms.
In OpenGL, Point representation: $\\left[
\\begin{array}{c}x\\\\y\\\\z\\\\1\\end{array}\\right]$, Vector representation: $\\left[\\begin{array}{c}x\\\\y\\\\z\\\\0\\end{array}\\right]$.

### Dot product

$\\mathbf{a}\\cdot\\mathbf{b} = a_xb_x+a_yb_y+a_zb_z = ||\\mathbf{a}||||\\mathbf{b}||\\cos\\theta$
$\\theta=\\cos^{-1}\\dfrac{\\mathbf{a}\\mathbf{b}}{||\\mathbf{a}||||\\mathbf{b}||}$.

__Projection of vector $\\mathbf{b}$ on vector $\\mathbf{a}$__:
$||\\mathbf{b}\\rightarrow\\mathbf{a}|| = ||\\mathbf{b}||\\cos\\theta = \\dfrac{\\mathbf{a}\\cdot\\mathbf{b}}{||\\mathbf{a}||}$
$\\mathbf{b}\\rightarrow\\mathbf{a} = ||\\mathbf{b}\\rightarrow\\mathbf{a}||\\dfrac{\\mathbf{a}}{||\\mathbf{a}||} = \\dfrac{\\mathbf{a}\\cdot\\mathbf{b}}{||\\mathbf{a}||^2}\\mathbf{a}$

__Projection of a point on a plane__:
Let $\\mathbf{a}$ be a point on the plane, $\\mathbf{q}$ be the point to be projected, $\\hat{\\mathbf{n}}$ be the normal vector that characterize the surface. Then the vector that represents the projection of $\\mathbf{q}$ is $\\mathbf{q'} = \\mathbf{a} + (\\mathbf{q} - [(\\mathbf{q} - \\mathbf{a})\\cdot\\hat{\\mathbf{n}}]\\hat{\\mathbf{n}})$

Applications in CG:

{ul}
* Find angle between two vectors (e.g., cosine of angle between light sources and surface for shading)
* Find projection of one vector on another (e.g. coordinates of point in arbitrary coordinate system)
{ul}

### Cross product

$\\textbf{u} \\times \\textbf{v} = -\\textbf{v} \\times \\textbf{u}$.
$\\mathbf{u}\\times\\mathbf{v}=\\left|\\begin{array}{ccc} \\mathbf{i} & \\mathbf{j} & \\mathbf{k} \\\\ u_1 & u_2 & u_3\\\\ v_1 & v_2 & v_3\\end{array}\\right|$, $||\\mathbf{u}\\times\\mathbf{v}|| = ||\\mathbf{u}||||\\mathbf{v}||\\sin\\theta$. Direction satisfies right hand rule.

### Constructing a basis from one vector

Given vector $\\mathbf{a}$, construct an orthonormal basis $\\mathbf{w,u,v}$:
Let $\\mathbf{w}=\\dfrac{\\mathbf{w}}{||\\mathbf{w}||}$ Choose any non-colinear vector $\\mathbf{t}$, let $\\mathbf{u}=\\dfrac{\\mathbf{t}\\times\\mathbf{w}}{||\\mathbf{t}\\times\\mathbf{w}||}$. Then finally $\\mathbf{w} = \\mathbf{u}\\times\\mathbf{v}$.

### Testing of how well explanation blocks work.

{def}
Lemma 1 (Access Lemma)
Let $\\mathbf{a}$ be a point on the plane, $\\mathbf{q}$ be the point to be projected, $\\hat{\\mathbf{n}}$ be the normal vector that characterize the surface. Then the vector that represents the projection of $\\mathbf{q}$ is $\\mathbf{q'} = \\mathbf{a} + (\\mathbf{q} - [(\\mathbf{q} - \\mathbf{a})\\cdot\\hat{\\mathbf{n}}]\\hat{\\mathbf{n}})$.

Also, this is frequently used.
{def}

{note}
Lemma 1 (Access Lemma)
Let $\\mathbf{a}$ be a point on the plane, $\\mathbf{q}$ be the point to be projected, $\\hat{\\mathbf{n}}$ be the normal vector that characterize the surface. Then the vector that represents the projection of $\\mathbf{q}$ is $\\mathbf{q'} = \\mathbf{a} + (\\mathbf{q} - [(\\mathbf{q} - \\mathbf{a})\\cdot\\hat{\\mathbf{n}}]\\hat{\\mathbf{n}})$.

Also, this is frequently used.
{note}

{warn}
Lemma 1 (Access Lemma)
Let $\\mathbf{a}$ be a point on the plane, $\\mathbf{q}$ be the point to be projected, $\\hat{\\mathbf{n}}$ be the normal vector that characterize the surface. Then the vector that represents the projection of $\\mathbf{q}$ is $\\mathbf{q'} = \\mathbf{a} + (\\mathbf{q} - [(\\mathbf{q} - \\mathbf{a})\\cdot\\hat{\\mathbf{n}}]\\hat{\\mathbf{n}})$.

Also, this is frequently used.

{ol}
1. __This is to demonstrate how we'll approach this list block!!!__
2. There can be one-line strings
3. Or multiline
   strings
4. Or multiple
   paragraphs
5. Or even blocks within blocks! Like this...

   {def}
   Lemma 1
   Given vector $\\mathbf{a}$, construct an orthonormal basis $\\mathbf{w,u,v}$:
   Let $\\mathbf{w}=\\dfrac{\\mathbf{w}}{||\\mathbf{w}||}$ Choose any non-colinear vector $\\mathbf{t}$, let $\\mathbf{u}=\\dfrac{\\mathbf{t}\\times\\mathbf{w}}{||\\mathbf{t}\\times\\mathbf{w}||}$. Then finally $\\mathbf{w} = \\mathbf{u}\\times\\mathbf{v}$.
   {def}

   Sadly however, image doesn't quite work? Or does it...

   {img}
   https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
   Test only... __Should it be robust?__
   {img}

6. And finally, another list block within this!

   {ol}
   1. Like this 1
   2. Like this 2
   {ol}

   {note}
   Take note:
   However things can fail...
   {note}
{ol}
{warn}
"""
