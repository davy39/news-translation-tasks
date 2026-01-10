---
title: How to build an image type convertor in six lines of Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-13T16:26:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-image-type-convertor-in-six-lines-of-python-d63c3c33d1db
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qzCM-NW3YK5gYx0tXTMJgQ.jpeg
tags:
- name: coding
  slug: coding
- name: image processing
  slug: image-processing
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By AMR

  One of the advantage of being a programmer is your ability to build utility tools
  to improve your life. Unlike a non-programmer, you are probably not spending hours
  digging through multiple Google search result pages to find a tool that, in th...'
---

By AMR

One of the advantage of being a programmer is your ability to build utility tools to improve your life. Unlike a non-programmer, you are probably not spending hours digging through multiple Google search result pages to find a tool that, in the first place, was supposed to improve your productivity (_irony wins_). This likely makes you feel more powerful knowing a programming language — especially if that Programming language is as versatile and awesome as Python is.

One of the points in the [The Zen of Python](https://www.python.org/dev/peps/pep-0020/#id3) says:

> Simple is better than complex.

With this philosophy in place, a lot of niche tool development using Python can be done so succinctly that it makes me wonder if it’s worth calling it a tool at all. Sometimes the word `script` would be more accurate. Either way, we’re setting out here to build one such `script` that converts images from one file format (image type) to another — in just 6 lines of Python code.

> _Disclaimer: The number of lines (6) excludes empty lines and comments_

In this tutorial, we’re going to build an image type convertor that converts a PNG image to a JPG image. Before your grey matter cells are rushing to judge whether I’m crazy to build this tool, let me say that this is not just for one image — but for all the images inside a folder. That’d definitely require more manual effort to do without coding _(I know you can smell `bash` ing)._

#### Python Package

We’re going to use the Python package `PIL` (which stands for Python Image Library) for this purpose. The original `PIL` didn’t get any updates for the latest Python version, so some good souls have created [a friendly fork called `Pillow`](https://python-pillow.org/) that supports even > Python 3.0.

Install it using `pip3 install Pillow`.

#### **Beginning Script**

There are two primary sections in this code. The first section is where we import the required packages, and the second section is where the actual operation happens. The actual operation can be further broken down as follows:

* Iterate through all the files with the given extension — in our case `.png` — and repeat all the following:
* Open the image file (as an image file)
* Convert the image file to a different format ( `RGB` )
* Finally save the file — with the new extension `.jpg`

**Lines 1 and 2:**

```
from PIL import Image  # Python Image Library - Image Processing
```

```
import glob
```

This section just imports the required packages. `PIL` for Image Processing and `glob` for iterating through files of the given folder in the OS.

**Lines 3–6:**

```
# based on SO Answer: https://stackoverflow.com/a/43258974/5086335
```

```
for file in glob.glob("*.png"):
```

```
 im = Image.open(file)
```

```
 rgb_im = im.convert('RGB')
```

```
 rgb_im.save(file.replace("png", "jpg"), quality=95)
```

#### FIN

So that’s the end of our tool! You can save these 6 lines as a `.py` file and then invoke them in your computer where you’ve got images to convert.

#### Further Development

If you are planning on to improve this script further, you can convert this entire script into a Command Line Interface Tool — then all these details like `File Format` and `Folder Path` can be given as arguments thus extending its power further.

#### **References**

* The complete code used here is available on [my github](https://github.com/amrrs/py_img_convertor)
* [Zen of Python](https://www.python.org/dev/peps/pep-0020/#id3)
* [Pillow](https://python-pillow.org/)

