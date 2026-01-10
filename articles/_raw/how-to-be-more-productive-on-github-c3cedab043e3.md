---
title: How to be more productive on GitHub
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-22T16:16:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-be-more-productive-on-github-c3cedab043e3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-Mc_lCYQhg5p45VrhbdfJQ.png
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Darren Burns

  With the recent announcement by GitHub of unlimited private repositories, let’s
  take a few minutes before we push our code we don’t want anyone else to see to the
  cloud, and make sure we’re making the most of what GitHub has to offer....'
---

By Darren Burns

With the recent announcement by GitHub of [unlimited private repositories](https://blog.github.com/2019-01-07-new-year-new-github), let’s take a few minutes before we push our code we don’t want anyone else to see to the cloud, and make sure we’re making the most of what GitHub has to offer.

GitHub is built with some extremely helpful shortcuts and productivity-boosting features. From personal experience, however, it’s clear that these often fall under the radar amongst developers.

If I’ve ever witnessed a specific GitHub feature surprise or assist someone, it’s on this page. That said, what follows is by no means an exhaustive list.

#### Quick fuzzy file search in repositories

This is, without doubt, the fastest way to browse a repository when you know what you’re looking for. Open up any repository and press `t`. You can now search for the name of any file in the repository, and use the arrow keys on your keyboard to move through the results. Press `Enter` to open the file.

![Image](https://cdn-media-1.freecodecamp.org/images/sN3jhoDd0p1mUiroNYprj8EyqoBVqv3I5TpA)

#### Code change suggestions in pull requests

When commenting on a piece of code in a pull request, you can suggest alternative code using the “Suggested Changes” feature. The author of the pull request will be able to apply your suggestion instantly without leaving GitHub. To make the suggestion, surround a code snippet with a multi-line Markdown snippet and add the tag “suggestion”:

![Image](https://cdn-media-1.freecodecamp.org/images/tFxJgPwY4B6I1ph7J18jxpOXoeRlR0JPvVtQ)
_Suggesting a change in a pull request…_

Now that you’ve made the suggestion, the author of the pull request can immediately apply it to their branch, without the hassle of manually changing the file!

![Image](https://cdn-media-1.freecodecamp.org/images/Qr1oLWlkwLYRsRC8POcEgEj3SYQznU8kgqLN)
_…and then applying that change!_

#### Navigate the code tree like in an IDE

This one requires an unofficial Chrome extension, but it’s a slightly more familiar way to navigate your code, compared to the default interface. The [Octotree extension](https://chrome.google.com/webstore/detail/octotree/bkhaagjahfmjljalopjnoealnfndnagc) lets you browse GitHub repositories with a sidebar tree view similar to what you get in applications like VS Code.

![Image](https://cdn-media-1.freecodecamp.org/images/EvBpPVgtggPwadfc4ptsKe6mxm0Lla8V96yS)

#### Jump to a function when reviewing code

Unless you’re reviewing a single function, a code review often involves a lot of jumping between function calls and their definitions (and therefore a lot of scrolling up and down). GitHub lets you jump to a symbol by pressing `t` when you’re looking at files in a pull request.

![Image](https://cdn-media-1.freecodecamp.org/images/GtVvg9u3g5LxiMrQFKUJvnwBxSKJnqBIusRn)

#### Creating a permalink to a file

When viewing a file or directory, press `y`, and the URL will be converted to a permalink, which you can share safely in the knowledge that the contents of the file will never change.

If you send a link to a file or directory on GitHub without making it into a permalink, you’ll need to accept the possibility that the file could disappear tomorrow, breaking the link!

#### Viewing the blame and change recency heatmap

When viewing a file, you can press `b` to view the Git blame and a heatmap showing how recently each line was changed. It’ll tell you who most recently changed each line of code, and give you a clickable link taking you to the full commit the change was part of.

On the right-hand side of the gutter (which contains the commit message and author), you’ll notice an orange vertical bar. The more vivid this bar is, the more recent the change, meaning you can easily scan the file to find the freshest code!

![Image](https://cdn-media-1.freecodecamp.org/images/FR-8iyQXhZK6JQJFpAgZHwvNNZ3Id5wJLimf)

#### Powerful code search

GitHub indexes most code and offers powerful search functionality over it. If you need to find something in a repository, but don’t plan on making any changes to it. There’s usually no need to check the repository out. Press `/`to search all the code in the repository.

![Image](https://cdn-media-1.freecodecamp.org/images/l8wrWB-R4yR8PuIt1v5-P9OnlZsRfQkjsCLx)

If your search contains multiple words and you want to search for occurrences of your specific search query, put the quotations around the query. You can filter your searches by other things too, such as file size, extension, the path the file is on, and much more.

#### Saved replies

If you ever find yourself repeating the same comments, you’ll save some time by creating a [saved reply](https://github.com/settings/replies). The next time you find you’re going to type that comment again, you can instead just select it from a drop-down menu:

![Image](https://cdn-media-1.freecodecamp.org/images/VTyPo1p4GAYysIzfHuYTzKsWi3fEUrK-JjHW)

To perform the above action without using my mouse, I can do `ctrl` + `/` followed by `ctrl`+ `1`.

#### Conclusion

Thanks for reading. I hope you found at least one thing on this page that will make you a more productive GitHub user. If you enjoyed this post or have any feedback in general, let me know!

If you’re interested in more content like this, follow me on [Twitter](https://twitter.com/_darrenburns).

Originally posted on my [blog](https://darrenburns.net/posts/github-tips).

**P.S.** You can make your own Octocat for sharing like the one in the cover photo at [myoctocat.com](https://myoctocat.com)!

