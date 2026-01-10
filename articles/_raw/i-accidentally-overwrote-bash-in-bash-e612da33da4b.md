---
title: That time I accidentally overwrote Bash… in Bash
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-13T04:04:01.000Z'
originalURL: https://freecodecamp.org/news/i-accidentally-overwrote-bash-in-bash-e612da33da4b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FIjDPNm9zRO_ESbUiGmCXA.png
tags:
- name: Linux
  slug: linux
- name: mac
  slug: mac
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
seo_title: null
seo_desc: 'By Jacob Evelyn

  “I know what I’m doing.”

  Five years ago, a few weeks into my very first Programming Job™, I was tinkering
  around in bash trying to get some code to run.

  I was becoming increasingly frustrated. Why wasn’t that file in my $PATH? It shou...'
---

By Jacob Evelyn

### _“I know what I’m doing.”_

Five years ago, a few weeks into my very first Programming Job™, I was tinkering around in `bash` trying to get some code to run.

I was becoming increasingly frustrated. Why wasn’t that file in my `$PATH`? It should have been, I felt certain of that.

But, growing more and more desperate to get _something_ to work, I moved the file to a folder I _knew_ was in the `$PATH`:

```
> mv ./file.whatever /bin
```

At least, that’s what I _meant_ to type. In reality what I typed was:

```
> mv ./file.whatever /bin/bash
```

My employer-provided MacBook Pro yelled at me, like any good UNIX system:

```
mv: rename ./file.whatever to /bin/bash: Operation not permitted
```

And like any good programmer, I blindly added a `sudo` and typed in my password as quickly as I could. _Stupid computer, thinking it knows better than me._

Having just unknowingly overwritten the very shell I was using, I was shocked to find my code still wouldn’t run.

### “I don’t know what I’m doing but it’s okay.”

I opened a new OS X Terminal tab to try a new approach to getting my code running, and instead saw this:

```
> permission denied: ./file.whatever
```

```
[Process completed]
```

_Hmm, that’s weird. Not sure why `bash` isn’t working, but at least it’s doing something with my file!_

I switched back to my previously-open `bash` shell and continued trying a few commands. They still worked, of course, because the `bash` program was already in memory at the time I overwrote its executable.

_So some Terminal tabs aren’t working, but others are. Probably ghosts in the machines._

To sort out this weird-but-definitely-probably-not-a-big-deal `bash` behavior I decided to do the tried-and-true cure-all: quit the app (Terminal) and open it again.

### “Oh god! what have I done?”

Out of nowhere, the reality of what had happened hit me like a snowball to the face. _Oh no oh no oh no I just overwrote Bash._

![Image](https://cdn-media-1.freecodecamp.org/images/4Mt5wOpqo6cWWlPWw-uY-bUFZw6kxWpRVEQL)

I no longer cared about getting my code to run. All I wanted to do was go back to the way things were.

### “This is probably fixable…”

I spent a long time Googling things like “deleted bash” and “download new bash OS X” and got nowhere. I was in too much of a panic to think about using other shells — which I vaguely knew about, but didn’t realize were already installed on my machine. (And I certainly didn’t realize these shells were also usable by just changing a setting in the Terminal app. #facepalm)

Eventually, I sheepishly confessed to some coworkers what I had done and after we all had a good chuckle I got one of them to email me a copy of his `bash` program so I could manually move it back into the `/bin` folder in Finder. (Hooray for point-and-click interfaces!)

Except… Finder wouldn’t let me go to the `/bin` folder. OS X (that version of it, at least) hid `/bin` and other system folders it deemed unsafe for meddling users like me to see. _Stupid computer, thinking it knows better than me._

So I Googled some more, this time for things like “view hidden folders in Finder.” I found a handful of different ways to do that, but _every single one of them_ required me to type some magic command… into `bash`, which I could no longer open. Kids: if you delete your shell but have an instance of it open, don’t close it!

### “OK… this is maybe fixable…”

At a loss for what to do next, I found an old internal Q&A system the company had and posted a quick description of my problem, trying to strike that balance in tone between _heh what a funny but probably not uncommon situation, right everyone?_ and _please someone anyone help me I’m panicking_. The site looked like it wasn’t ever used anymore but I was hoping someone got an email when a question was posted.

Lo and behold, my Hail Mary quickly got a response: someone recommended booting from a Linux [Live CD](https://en.wikipedia.org/wiki/Live_CD) (this was back when computers had CD drives), and then from within Linux accessing my OS X file system to add `bash` back to its rightful place. I understood about a third of the suggestion, but went ahead anyway — what other options did I have? I found a Linux CD, did a bunch of things I didn’t understand to get it to work, and waited impatiently as the machine went through all of the myriad setup steps until — _voilà!_ A desktop appeared!

I Googled around until I found out how to mount the OS X filesystem, and eagerly opened `bash` (what a good feeling!) to copy that machine’s `bash` executable back over to OS X… only to encounter an error message: the OS X partition was read-only from Linux. I did find out about a way to make it writable, but that required restarting back in OS X and — you guessed it — running a command in `bash`.

I tried a few different Linux Live CDs (each of which took about forty minutes of impatient pacing to boot), but each had the same result. Once again: if you delete your shell but have an instance of it open, **_don’t_** close it!

### “What does fixable even mean anyway?”

Unsure where to go from there, I reached out to coworkers again and _eureka!_ — someone knew of a way to navigate to any folder — even hidden ones — within Finder. All I had to do was restart in OS X again, copy the emailed `bash` executable to `/bin`, and everything would be gravy. So I shut down Linux, removed the Live CD, restarted in OS X, and…

Hmm. I couldn’t log in, because, well, the OS X login process uses a shell under the hood, and guess which shell that is?

Was I doomed to spend the rest of my career living off of Linux Live CDs? I pictured myself years in the future, a babbling hermit kept around to scare the new kids: _“Don’t delete bash or you’ll end up like crazy old Jake.”_

![Image](https://cdn-media-1.freecodecamp.org/images/L3idR4cUHdlM2acBE01yx7PyhgsuELGt38j8)

### “I’ve never been happier to see an error message”

I had given up all hope, when another coworker (goodness, these people knew so much!) told me about [single-user mode](https://en.wikipedia.org/wiki/Single_user_mode), a special OS X startup mode that helps you resolve login (and other) errors. Single-user mode let me boot a bare-bones, command-line version of OS X through a different shell (`/bin/sh`, I think). From there, it was just a matter of finding the right incantations to get the `bash` executable back into `/bin` and off of a USB drive (where I put it in another painfully slow iteration of the Linux Live CD boot).

Once that was done, I restarted the Mac and all was finally well again! Well, except that of course my code still didn’t run.

