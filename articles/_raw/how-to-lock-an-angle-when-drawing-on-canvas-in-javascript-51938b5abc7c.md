---
title: How to lock an angle when drawing on canvas in JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-18T16:16:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-lock-an-angle-when-drawing-on-canvas-in-javascript-51938b5abc7c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cWcey5rf6AkuNtkVZ7ywwg.png
tags:
- name: canvas
  slug: canvas
- name: geometry
  slug: geometry
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Thang Minh Vu

  In many drawing tools (Adobe Photoshop, Sketch, and so on), if we hold the SHIFT
  button when drawing a line, we can create perfectly straight lines horizontally
  or vertically.

  Recently, I tried implementing this feature in canvas by ...'
---

By Thang Minh Vu

In many drawing tools ([Adobe Photoshop](https://www.adobe.com/products/photoshop.html), [Sketch](https://www.sketchapp.com/), and so on), if we hold the SHIFT button when drawing a line, we can create perfectly straight lines horizontally or vertically.

Recently, I tried implementing this feature in canvas by JavaScript. The process is really interesting. I would like to share the progress of how I approach it.

**Demo**: To easier understand the idea, you can check a demo version at the [demo page](https://ittus.github.io/draw-lock-angle/).

### Requirements

**Input**

* A base point (B)
* Current mouse position (M)

**Output**

* Projection of current mouse position on x-axis or y-axis (P)

For convenience, in all graphs, we will mark the base point by a red circle and the current mouse point by a green circle.

![Image](https://cdn-media-1.freecodecamp.org/images/zvt4t9MmiO6Uxc3zAyLDxUOta3S-j4Nl7JvE)
_Problem: Decide which projection is better_

### Simple solution

As I tackle the problem, it’s intuitive to see we can calculate the distance between the current mouse position with the horizontal line and vertical line. If the mouse position is nearer the horizontal line than the vertical line, we will take the projection on the horizontal line, and vice versa.

![Image](https://cdn-media-1.freecodecamp.org/images/F-mQyWvLknInihDnYTgeS2CYyiHljKRB-P1R)

The calculation is quite simple — here is the Javascript code:

![Image](https://cdn-media-1.freecodecamp.org/images/AmQiLZ6chh1YF30QhI6MXs0Qrpwq1SkXAdti)

### Extended Problem

How about if we want to project on the bisector line between the horizontal line and vertical line (similar with [Sketch](https://www.sketchapp.com/))? That means users can project the mouse position on the horizontal line, vertical line, 45-degree angle line, or 135-degree angle line.

The approach is similar. This time we need to calculate the distance between the mouse position to 4 lines: horizontal line, vertical line, and 2 bisector lines (45-degree line and 135-degree line). But the calculation is more complex.

We still can divide it into 2 steps:

1. Determine which line is nearest with mouse position
2. Calculate the projection of mouse position on the nearest line

![Image](https://cdn-media-1.freecodecamp.org/images/yRRlpXpZg16PFuGjohkEwMBRTQ074yN4UmvH)

#### Step 1: Determine which line is nearest with mouse position

First, we need to determine line formulation of 4 lines above. Because we already know the base point (x0, y0) and the line angle, it’s easy to figure out the formulation of each line.

> Example: To calculate the formula of the 45-degree bisector, we already know that the line will go through the base point (x0, y0) and (x0 + 1, y0 + 1). Using the [Find-the-Equation-of-a-Line](https://www.wikihow.com/Find-the-Equation-of-a-Line) method, we can figure out the line formula.

Finally, we will have 4 lines’ formulas:

![Image](https://cdn-media-1.freecodecamp.org/images/ngaxjDK6zWtgP74BOXPwMU2jZY014c7L-lu6)

To calculate the distance between the base mouse position to each line, we can use a popular math formula:

![Image](https://cdn-media-1.freecodecamp.org/images/C4Tk7kqRbwGbPtYFwK-HDSRlmVnGTRunxAso)
_Distance from a point to a line_

![Image](https://cdn-media-1.freecodecamp.org/images/Adk5BQAv15Jy4IuGUBSyKiSxkU68gEgsdh7z)
_Finding the nearest line_

#### Step 2: Calculate the orthogonal projection of mouse position on the nearest line

Now the problem becomes calculating the orthogonal projection of the mouse position (M) to the nearest line with the formula: ax + by + c = 0 (L)

There are multiple ways to solve this problem. I took a simple way: First, calculate the formula of the line which contains mouse position M and perpendicular to line L, called L'. Then, solve the system of equations to get the intersection point between line L and L', which is the projection point which we are finding.

After some calculation, I figured out the formula of L’, which goes through M (x0, y0) and perpendicular to L (ax + by + c = 0):

![Image](https://cdn-media-1.freecodecamp.org/images/BwlHT2VPl2baMMHQtQYI2vGkCUq0jl0ZpiLz)

Now to find the intersection, we need to solve the system of equations:

![Image](https://cdn-media-1.freecodecamp.org/images/4nJ1rFj7FrXEwZ0KK3MLEGo10DMJDUrchUxB)

Using [Cramer’s rule](https://en.wikipedia.org/wiki/Cramer%27s_rule) and matrix determinant, we can solve this equation easily:

![Image](https://cdn-media-1.freecodecamp.org/images/YeHWX9l70xghLPvDkqTZA19RSbRGyRIZq4WJ)
_Solve simultaneous equations_

### Boundary

There is a situation when we want to limit the boundary of projection.

Example:

![Image](https://cdn-media-1.freecodecamp.org/images/3WNRAcorUIwF9lwihmXCjAna8DovCrhgmUxi)
_The projection point is outside of the boundary_

In this case, we want to limit the projection in the white rectangle area, but using the discussed method, the projection point can be outside of the boundary area.

In this situation, we can simply get the intersection point of line L’ to the boundary (called P’).

![Image](https://cdn-media-1.freecodecamp.org/images/Zl5D-QVbgmra2XCyD6khtLSFE1sF9VzPz49c)
_Support boundary of the projection_

### **Full source code**

You can check out the demo and source code on [Github](https://github.com/ittus/draw-lock-angle).

Happy Coding!

