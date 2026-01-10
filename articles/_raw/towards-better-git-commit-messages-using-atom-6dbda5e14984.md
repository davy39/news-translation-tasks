---
title: Get Better Git Commit Messages with Atom
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-12-20T21:22:01.000Z'
originalURL: https://freecodecamp.org/news/towards-better-git-commit-messages-using-atom-6dbda5e14984
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5El6ItJ_0MabNL0UXNvShw.jpeg
tags:
- name: Git
  slug: git
- name: Life lessons
  slug: life-lessons
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Hasit Mistry

  Recently, I came across two enlightening posts about writing better Git commit messages.
  These posts give suggestions about how a well structured commit message should look
  like, and provide clear examples.


  Better Commit Messages wit...'
---

By Hasit Mistry

Recently, I came across two enlightening posts about writing better Git commit messages. These posts give suggestions about how a well structured commit message should look like, and provide clear examples.

* [Better Commit Messages with a .gitmessage Template](https://robots.thoughtbot.com/better-commit-messages-with-a-gitmessage-template) by [Matthew Summer](http://appallingfarrago.com/)
* [How to Write a Git Commit Message](http://chris.beams.io/posts/git-commit/) by [Chris Beams](http://chris.beams.io/)

These two blog posts made me go back to my repositories and read my commit messages. And to be honest, I felt a little ashamed of my past then.

You may ask, “why are commit messages even important?” If you find yourself asking that question, you are like the one-week-younger version of me.

Just to give you an idea, Figure 1 shows some of the commit messages from my project [licensethis](https://github.com/hasit/licensethis/). I promise that the code is much better than the commit messages.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qlezTXx2CxPpbS4wa4XKqg.png)
_Figure 1. [licensethis](https://github.com/hasit/licensethis/" rel="noopener" target="_blank" title=") commit messages from earlier this year._

It’s unsurprising how little these commit messages actually tell me about my past work. That’s because I didn’t take writing them seriously.

In order to actually understand which changes each commit contributed, I had to go into each commit and read the changes line-by-line. This is tedious to say the least.

At the time of authoring these commit messages, I invariably blurted out whatever made sense to me at that moment, with no consideration of how I — or anyone else for that matter — would understand the text at a later stage.

First, let’s synthesize all the information we’ve absorbed from the above-mentioned blog posts. Then I’ll give working tips on how [Atom](https://atom.io/) can be used as a tool for writing better commit messages for myself and others who are interested in doing the same.

Note that I am not going to write about _how_ to write a good commit message. [Chris Beams](http://chris.beams.io/)’s wonderful post on [How to Write a Git Commit Message](http://chris.beams.io/posts/git-commit/) explains just that and more in seven rules.

Before we begin, let us look at this following text block to understand what is considered as a properly-structured, purposeful, and well-written commit message:

```
# Subject in (preferably) less than 50 charactersThis is the subject of this commit message
```

```
# Body in greater detailThis is the body of this commit message. The body is written after the subject line with one blank line in between. The blank line is used by various tools (such as 'git log', 'git show', etc.) to differentiate subject from body. Further paragraphs are also separated by blank lines.
```

```
Explain the problem being solved by this commit. More importantly, explain why these changes are being made, as opposed to how. The 'why' part is your responsibility, the 'how' part is code's responsibility.
```

```
- You can also use bullets like this.- Or, like this.
```

Some great examples of such commit messages can be found over at the [Linux](https://github.com/torvalds/linux) and [Git](https://github.com/git/git) repositories on [GitHub](https://github.com/).

Now, it is understandable that not every commit brings big changes to the repository. Some commits would be for fixing typos, and others for changing line order or indentation. In such cases, a subject line by itself should suffice.

Atom is a text editor that I use for everything! I use it to take notes in class, complete writing assignments in [Markdown](https://daringfireball.net/projects/markdown/) (unless I absolutely require the super powers of MS Word), and for programming projects on a daily basis.

I keep tweaking Atom little-by-little every time I learn something new, it’s fun to watch my config files slowly grow in size.

So let us start by setting Atom as our default commit editor for git, and checking if the same has happened correctly using the following commands in your terminal:

```
git config --global core.editor "atom --wait"
```

```
git config --get core.editor
```

```
# Which should give you the output: atom --wait
```

#### Change the color of the subject line according to its length

First, we will set up Atom so that it changes the color of the subject line to orange if the length exceeds 50 characters and to red if the length exceeds 65 characters. You can read more about git integrations for Atom at [Git Integration](http://blog.atom.io/2014/03/13/git-integration.html).

Open up your Atom’s styles.less file, which is under the “Atom” menu option:

![Image](https://cdn-media-1.freecodecamp.org/images/1*zkgNf5LtktODM49BOgVQ2g.jpeg)

Write the following lines of code into Atom’s styles.less file:

```
atom-text-editor::shadow { .git-commit.invalid.deprecated.line-too-long {  color: @text-color-warning;  text-decoration: none; }
```

```
 .git-commit.invalid.illegal.line-too-long {  color: @text-color-selected;  background: @background-color-error;  opacity: 0.9; }}
```

Once you’ve made the changes and saved the file, Atom will behave as shown in Figure 2.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LrrcnjYYKGNePP0T-79uCQ.gif)
_Figure 2. Commit message subject line behaviour in Atom._

#### Write a snippet for commit message structure

Second, we will write a short snippet for commit messages. This snippet will provide placeholders for subject line and body that can be navigated using TAB key.

![Image](https://cdn-media-1.freecodecamp.org/images/1*U8y5zf56tzuPQx0kTn3L2Q.jpeg)

Write the following lines of code into Atom’s snippets.cson:

```
'.text.git-commit':  'commit-message':    'prefix': 'comm'    'body': """      ${1:Subject < 50 chars}
```

```
      ${2:Body in detail}    """
```

After you make the changes and save the snippets file, the next time you open your commit message, you just need to type **comm** and press TAB to expand your snippet.

Once the snippet has been expanded, you can press TAB again to jump the cursor from ‘subject line’ to ‘body’. Figure 3 shows this snippet in action.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dSJ0TgQUPX2ukRwgZi9RBQ.gif)
_Figure 3. ‘comm’ snippet in action._

These little code snippets have sure improved my git commit workflow, and I’m confident they can improve yours.

If you have any other committing-related snippets that you use in Atom, please be sure to post them. I’d love to have a look and maybe incorporate them into my workflow.

Also — for those curious — here’s a list of themes and packages I’ve used in the above figures:

* UI Theme — [Nucleus Dark](https://atom.io/themes/nucleus-dark-ui)
* Syntax Theme — [Atom Dark Fusion](https://atom.io/themes/atom-dark-fusion-syntax)
* Git editing support for Atom — [language-git](https://atom.io/packages/language-git)

