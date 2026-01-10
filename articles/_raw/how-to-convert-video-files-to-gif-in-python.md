---
title: How to Convert Video Files to a Gif in Python
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-03-31T16:06:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-video-files-to-gif-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/convert.png
tags:
- name: gif
  slug: gif
- name: Python
  slug: python
- name: video
  slug: video
seo_title: null
seo_desc: 'Recently, I was able to convert some video files to a gif as I needed them
  in gif format for some of my articles.

  I decided to show you how I did it in 3 lines of code, so you can save yourself
  the extra effort of looking up a Saas to do it for you.

  ...'
---

Recently, I was able to convert some video files to a gif as I needed them in gif format for some of my articles.

I decided to show you how I did it in 3 lines of code, so you can save yourself the extra effort of looking up a Saas to do it for you.

## How to Convert Video to a Gif in Python

To convert video to gif in Python, you need to install a package called `moviepy` with pip by opening your terminal and running `pip install moviepy`.

This module has several methods with which you can edit and enhance videos.
![ss1-3](https://www.freecodecamp.org/news/content/images/2022/03/ss1-3.png)

After successfully installing `moviepy`, you need to import a method called `VideoFileClip` from it. This is the method with which you will be able to specify the name of the video file and its relative path.

```py
from moviepy.editor import VideoFileClip
```

The next thing you need to do is to specify the relative path of the video you want to convert to a gif inside the VideoFileClip method. Then you need to assign it to a variable. 

In the code snippet below, I call that variable `videoClip`:

```py
videoClip = VideoFileClip("my-life.mp4")
```

To finally convert the video to gif, you need to bring in the `videoClip` variable and use the `write_gif()` method on it, then specify the name you want to give to the gif inside it.
```py
videoClip.write_gif("my-life.gif")
```
Open the terminal and run the file:
![ss2-1](https://www.freecodecamp.org/news/content/images/2022/03/ss2-1.png)

Check the folder inside which the video file is located and you should see the gif file. If you’re using VS Code, open the sidebar by pressing `CTRL + B` and you should see the gif file.
![ss3-1](https://www.freecodecamp.org/news/content/images/2022/03/ss3-1.png)

You can open the gif with VS Code too.

The whole code that did the conversion looks like this:

```py
from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("my-life.mp4")

videoClip.write_gif("my-life.gif")
```

You can learn more about the `moviepy` module on [their official website](https://zulko.github.io/moviepy/).

If you have any questions, feel free to contact me on [Twitter](https://twitter.com/Ksound22).

Thank you for reading.


