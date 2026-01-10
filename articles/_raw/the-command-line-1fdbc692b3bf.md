---
title: A Brief History of the Command Line
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-21T09:55:28.000Z'
originalURL: https://freecodecamp.org/news/the-command-line-1fdbc692b3bf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uIU5dRHM7WFi1EFds5XD3Q.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Gitter

  This post by Andy Trevorah, Engineer at Gitter, has been adapted from a talk that
  he originally gave at codebar, a non-profit initiative that facilitates the growth
  of a diverse tech community by running regular programming workshops.

  This ...'
---

By Gitter

_This post by [Andy Trevorah](https://www.freecodecamp.org/news/the-command-line-1fdbc692b3bf/undefined), Engineer at [Gitter](http://gitter.im), has been adapted from a talk that he originally gave at_ [codebar](http://codebar.io/)_, a non-profit initiative that facilitates the growth of a diverse tech community by running regular programming workshops._

This post is in two parts: a little history, followed by some live command line examples.

#### A Brief History

Way back in the 1960s — 70s, computers were becoming more than just calculators. They could save files to disk and have multiple running applications with multiple users. But these things were difficult to control and easy to break. Thankfully, there was a very smart idea to cover all these internal bits in a nice, usable shell.

![Image](https://cdn-media-1.freecodecamp.org/images/8dQXHBemVAUp4xgVzFqgEHGyNjCsQT0usHBw)

These shells have since evolved to be Windows desktop, Mac OS, and all the touchy screeny bits of your phone. Basically all the user interaction stuff. They make your computer easy to use and (reasonably) hard to break.

But before these shells started looking pretty and graphical, they were just a command line. You would type something in, and you would get a response. They looked like this:

![Image](https://cdn-media-1.freecodecamp.org/images/z6KVS8d-ygTOk6nf25pzAas6NhWtxu01Iw8P)

Here’s a shell running the _cal_ command and printing out a calendar.

This particular shell is called _bash_ which is short for [“Bourne Again SHell”](https://en.wikipedia.org/wiki/Bash_%28Unix_shell%29) because before that there was the [“Bourne Shell”](https://en.wikipedia.org/wiki/Bourne_shell) by Stephen Bourne. Never let a software engineer name something that will end up lasting.

There’s a rich history of shells, and these “[Unix](https://en.wikipedia.org/wiki/Unix) style” shells began with [Unix System 1’s shell](https://en.wikipedia.org/wiki/History_of_Unix#1969) in 1969. But even that was influenced by older programs such as [RUNCOM](https://en.wikipedia.org/wiki/Run_commands). If you’ve ever noticed that some config files end in “rc” (e.g ._vimrc_), thats why.

If these shells have changed since the 1960s, then why do developers keep on using them?

![Image](https://cdn-media-1.freecodecamp.org/images/eKIIYJsqGQIaqkkd7NRrKfNpWN2AirtM6ius)

**_Because_** they haven’t really changed since the 60s. Graphical interfaces for your phone or computer fashionably change with every update (with usability improvements), but command line shells don’t. When you are scripting things or dealing with an entire farm of servers, you really don’t want your (user) interface to change, as it will break your scripts.

Thankfully, both command line and graphical shells are both shells around the same thing, so we can use them both interchangeably. Here’s some examples to show what command line shells can do.

#### Shells in Action

We can start small and just get the computer to repeat what we say:

```
bash-3.2$ echo hello  hello
```

The computer also has some special words like $RANDOM:

```
bash-3.2$ echo $RANDOM  23914
```

Bear in mind that almost all of these commands are just little programs that accept some input and emit output. You can find out where they are using _which_:

```
bash-3.2$ which echo  /bin/echo
```

With Mac OS, we can even make the computer _say_ stuff:

```
bash-3.2$ say hello  ["hello" comes from the speakers]
```

```
bash-3.2$ say butts butts butts  ["butts butts butts" comes from the speakers without complaint]
```

There’s also _cat_ which will print out file contents. It’s from 1971.

```
bash-3.2$ cat cool_websites.txt  Some websites that I like:
```

```
http://codebar.io  http://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt
```

We can use it to read some built in files on your computer:

```
bash-3.2$ cat /usr/share/dict/words  [skip a few thousand lines]zymotically  zymotize  zymotoxic  zymurgy  Zyrenian  Zyrian  Zyryan  zythem  Zythia  zythum  Zyzomys  Zyzzogeton
```

That’s every word that your computer knows! That list is pretty long (almost too long to scroll!), but we can use the _head_ command to see the top of it:

```
bash-3.2$ head /usr/share/dict/words  A  a  aa  aal  aalii  aam  Aani  aardvark  aardwolf  Aaron
```

And there is an opposite command, _tail_:

```
bash-3.2$ tail /usr/share/dict/words  zymotoxic  zymurgy  Zyrenian  Zyrian  Zyryan  zythem  Zythia  zythum  Zyzomys  Zyzzogeton
```

It would be neat to just get the last word. _tail_ can do this, but requires a special argument. We can look it up using _man_:

```
bash-3.2$ man tail
```

```
TAIL(1)                   BSD General Commands Manual
```

```
NAME       tail -- display the last part of a file
```

```
SYNOPSIS       tail [-F | -f | -r] [-q] [-b number | -c number | -n number] [file ...]
```

```
DESCRIPTION       The tail utility displays the contents of file or, by default, its stan-     dard input, to the standard output.
```

```
     The display begins at a byte, line or 512-byte block location in the     input.  Numbers having a leading plus (`+') sign are relative to the     beginning of the input, for example, ``-c +2'' starts the display at the     second byte of the input.  Numbers having a leading minus (`-') sign or     no explicit sign are relative to the end of the input, for example, ``-n     2'' displays the last two lines of the input.  The default starting loca-     tion is ``-n 10'', or the last 10 lines of the input.
```

```
     The options are as follows:
```

```
:
```

Ah! The argument is _-n_ (you press “q” to exit the manual btw):

```
bash-3.2$ tail -n 1 /usr/share/dict/words  Zyzzogeton
```

I have no idea how to pronounce “Zyzzogeton”, but we can get the computer to do it using the say command. We just pipe the output of _tail_ into the input of _say_ using the pipe character (|):

```
bash-3.2$ tail -n 1 /usr/share/dict/words | say  ["Zyzzogeton" comes from the speakers]
```

Neat! We can even have multiple pipes. We can pipe _cat_ into _tail_ into _say_ and get the same result:

```
bash-3.2$ cat /usr/share/dict/words | tail -n 1 | say  ["Zyzzogeton" comes from the speakers]
```

Now if we wanted to get a random word, we could get all the words up to a random point and then get the last word of that. We can do that with _head_ and _tail_:

```
bash-3.2$ cat /usr/share/dict/words | head -n $RANDOM | tail -n 1 | say  ["atmological" comes from the speakers]
```

_cat_ reads files from your hard drive, but we can use _curl_ to read files from the internet. Here’s a url for a file that contains the full works of shakespeare:

```
bash-3.2$ curl -s http://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt  [skip a few thousand lines]  Would yet again betray the fore-betrayed,  And new pervert a reconciled maid.'
```

```
THE END
```

```
<<THIS ELECTRONIC VERSION OF THE COMPLETE WORKS OF WILLIAM  SHAKESPEARE IS COPYRIGHT 1990-1993 BY WORLD LIBRARY, INC., AND IS  PROVIDED BY PROJECT GUTENBERG ETEXT OF ILLINOIS BENEDICTINE COLLEGE  WITH PERMISSION.  ELECTRONIC AND MACHINE READABLE COPIES MAY BE  DISTRIBUTED SO LONG AS SUCH COPIES (1) ARE FOR YOUR OR OTHERS  PERSONAL USE ONLY, AND (2) ARE NOT DISTRIBUTED OR USED  COMMERCIALLY.  PROHIBITED COMMERCIAL DISTRIBUTION INCLUDES BY ANY  SERVICE THAT CHARGES FOR DOWNLOAD TIME OR FOR MEMBERSHIP.>>
```

```
End of this Etext of The Complete Works of William Shakespeare
```

If we used this _curl_ as an input to our random word pipes, we can get the computer to quote us random lines of Shakespeare!

```
bash-3.2$ curl -s http://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt | head -n $RANDOM | tail -n 1 | say  ["The sister to my wife, this gentlewoman" comes from the speakers]
```

We can achieve quite a lot with only a few commands. This philosophy of having small reusable programs that can be combined together has lasted for a long time, much like lego bricks. By combining the right ones, you can make quite an impressive program!

