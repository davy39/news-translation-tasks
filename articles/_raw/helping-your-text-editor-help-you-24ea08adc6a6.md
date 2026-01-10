---
title: How to help your text editor help you
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T15:23:06.000Z'
originalURL: https://freecodecamp.org/news/helping-your-text-editor-help-you-24ea08adc6a6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ia2Y_ugGsTSSMf3KV4gbcA.png
tags:
- name: Design
  slug: design
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Evy

  Tips & tricks for writing more efficient and enjoyable code


  Over six internships, I’ve had lots of lovely mentors who have watched me code and
  let me watch them code. (I ? pair programming!) Thanks to them, there are lots of
  things I’ve learn...'
---

By Evy

#### Tips & tricks for writing more efficient and enjoyable code

![Image](https://cdn-media-1.freecodecamp.org/images/sU6v-eVAoUsJZFAPquJ7NDaWXIlffjPVSlqM)

Over six internships, I’ve had lots of lovely mentors who have watched me code and let me watch them code. (I ? p[air programming!](https://content.pivotal.io/blog/pair-programming-considered-extremely-beneficial)) Thanks to them, there are lots of things I’ve learned on the job that have made my work more efficient and enjoyable.

Some of these things are text editor tips and tricks, and I want to share some of what I’ve learned with you!

**This is not a blog post about which text editor you should use**. I’ll be sharing some examples in the editor I use these days (Sublime Text on a Mac) — but many text editors are customizable. That means that many of these tips & tricks can be probably be set up in your editor (and I’d love to see comments explaining how!) Let’s get rid of the “this tool is the best” discourse, and just learn how to help our tools help us better. ✨

### Automatically lint your code

Linters can be great for making code cleaner and easier to read, and for catching mistakes. Sometimes I run a linter after I finish a set of changes, or let a linter run online after I open a pull request on GitHub. But I got much faster at writing linter-passing code when the linter ran… as I wrote my code! I have not only stopped making boring tweaks for several minutes before submitting code. I’m also now training myself to fix issues before they even happen.

![Image](https://cdn-media-1.freecodecamp.org/images/MOw7rJCjUU--NZ8yk2uB7EBHZmtzykiLkrSu)
_The [linter](http://www.sublimelinter.com/en/latest/index.html" rel="noopener" target="_blank" title=") tells me right away: a variable is undefined, and I’m missing a semicolon_

### 80 character ruler

Speaking of arbitrary rules, lots of style guides like lines to be at most 80 characters long (or 100, or something else). Most text editors have a way to add a little line to remind you when you’re at that limit, whatever it is.

![Image](https://cdn-media-1.freecodecamp.org/images/CGUAYQQrt4GIhkJ8g6BUkD8LoccxYp9RsWxP)
_In Sublime Text, you can turn this on from View &gt; Ruler_

### Automatically follow some whitespace conventions

A lot of style guides prefer files to have no trailing whitespace and exactly one new line at the end of each file. It can be hard to remember to do this, so it’s nice when my text editor does it for me! Sublime has this in its user settings: `“ensure_newline_at_eof_on_save”` and `“trim_trailing_white_space_on_save”`.

### Search (and replace) over the whole codebase

When I’m dealing with a codebase of many files, it’s nice to search within it to see all the places something is used or referred to (`⌘ shift F` on MacOS in Sublime). It’s extra awesome to have the option to search specifically within a certain folder or file type. Sometimes I find it helpful to turn case sensitivity on/off or to use regular expressions — though I don’t use those features often.

### Quickly find function definitions

Sure, I could search through the codebase for a function name, find its definition, and _then_ figure out how it works. But wouldn’t it be nice to have a way to get there faster?

![Image](https://cdn-media-1.freecodecamp.org/images/He6pNBtDumRVhUlHH0twAwZnSxCUPgNmQlVo)
_right click, goto definition, and …aha! **that’s** what that does_

### Quickly find files

I often want to find and open a file but don’t remember where exactly it is in the codebase. I love being able to enter the filename in a search bar and see all possible files I am looking for, which lets me open new files quickly. I love the added bonus of a really flexible search input. I can make a whole bunch of typos or leave out parts of the filename and Sublime still can figure out what I want! (I bet the tech behind that search algorithm, often called “[fuzzy search](https://github.com/junegunn/fzf)”, is pretty interesting!)

![Image](https://cdn-media-1.freecodecamp.org/images/M5A7Qc4qL8pbVwKOzs944SvbcdBcjkTQx40E)
_In Sublime Text, you can bring up this search bar with ⌘P_

### Move line(s) up and down

To move a line of code (or a whole function) below another, I used to use a lot of select + copy + paste. I’ve since figured out how to move lines up and down with a shortcut. It’s a small change, but I find it feels _so much_ nicer (kinda like how amazing [three finger drag](https://support.apple.com/en-us/HT204609) feels).

![Image](https://cdn-media-1.freecodecamp.org/images/Xt3p6XFHzhT0jjrIIbGJNRW7LjvpozLwnccd)
_control+ ⌘ + up/down (on MacOS) in Sublime Text_

### Syntax highlighting

Syntax highlighting makes reading and scanning code much easier. But it also helps catch mistakes as they’re being typed — if it doesn’t look like it’s colored right, it might be a mistake.

Sometimes syntax is highlighted by default. Sometimes only certain languages/technologies are in your default settings. I got a new work laptop and knew I needed to [install a package](http://gunnariauvinen.com/getting-es6-syntax-highlighting-in-sublime-text/) to get `jsx` highlighting. Yet I _still_ procrastinated it for a few months while working with many `jsx` files. After I took a minute to install it, things got so much better.

![Image](https://cdn-media-1.freecodecamp.org/images/DeRG0dUpyd8w0xB3VHcLbMwaOmU3pJtv83js)

![Image](https://cdn-media-1.freecodecamp.org/images/89b8ZaIYbqfGixOrU3z0CJg5gfOqJlmlg8wG)
_Before and after adding syntax highlighting for React .jsx files_

### Git stuff

Lastly, if you use git in your workflow, you can add some support to your text editor to tell you git-related things. One thing I like to see is what lines have been added/deleted/modified since my last commit (a lightweight `git diff`). I also sometimes use a tool (built around the [poorly named](https://gitlab.com/gitlab-org/gitlab-ce/issues/34469) `[git blame](https://git-scm.com/docs/git-blame)`) to see who last changed a line in a file.

![Image](https://cdn-media-1.freecodecamp.org/images/tcxOLrCgNk3C3xsjYh4aL43Mliapxp-bnFYc)
_the markers in the left margins are thanks to the [GitGutter](https://github.com/jisaacks/GitGutter" rel="noopener" target="_blank" title=") package_

### And more!

There are lots of cool things your text editor can do for you! I’m sure I’ll continue to learn about tools that will help me be more efficient and help my work be more enjoyable. And I don’t plan on starting to use them all at once — over time I will pick and choose tools as I get excited about them or find the need for them.

Hopefully some of these tips & tricks were exciting or helpful to you! I’d love to hear in the comments about what sorts of text editor features you love to use. ?

