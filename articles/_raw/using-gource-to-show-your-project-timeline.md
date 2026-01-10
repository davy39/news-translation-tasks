---
title: How to use Gource to show your project's timeline
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T23:17:24.000Z'
originalURL: https://freecodecamp.org/news/using-gource-to-show-your-project-timeline
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/gource.jpg
tags:
- name: Git
  slug: git
- name: gource
  slug: gource
- name: terminal
  slug: terminal
seo_title: null
seo_desc: 'By Leonardo Faria

  The first time I heard about Gource was in 2013. At the time I watched this cool
  video showing Ruby on Rails source code evolution:

  https://www.youtube.com/watch?v=r0ji8FDNTj0&feature=emb_title

  At Thinkific we have (almost) monthly ...'
---

By Leonardo Faria

The first time I heard about [Gource](https://github.com/acaudwell/Gource) was [in 2013](https://leonardofaria.net/2013/01/20/gource-uma-forma-estilosa-de-ver-logs-do-seu-controle-de-versao/). At the time I watched this cool video showing Ruby on Rails source code evolution:

%[https://www.youtube.com/watch?v=r0ji8FDNTj0&feature=emb_title]

At [Thinkific](https://www.thinkific.com/) we have (almost) monthly Product Town Halls, which we use to communicate product decisions and keep all product teams (Designers, Engineers, Product Managers and QAs) on the same page. 

We like to start the keynote with some gource video of our projects. Here is how we are doing:

`gource --hide dirnames,filenames --seconds-per-day 0.1 --auto-skip-seconds 1 -1280x720 -o - | ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i - -vcodec libx264 -preset ultrafast -pix_fmt yuv420p -crf 1 -threads 0 -bf 0 gource.mp4`

The [README](https://github.com/acaudwell/Gource/blob/master/README) of Gource has all the options you can customize in your video. Tied to [ffmpeg](https://www.ffmpeg.org/), we create a mp4 file that can be used inside Google Slides or YouTube. Here's the output of the example above:

%[https://youtu.be/hYvWaA5cCJg]

_Also posted on [my blog](http://bit.ly/2FWop4N). If you like this content, follow me on [Twitter](https://twitter.com/leozera) and [GitHub](https://github.com/leonardofaria)._

By the way - Thinkific is [hiring](https://bit.ly/thnk-senior-front-end-eng) [for](https://bit.ly/thnk-senior-full-stack-eng) [several positions](https://www.thinkific.com/careers/) if you are interested.

