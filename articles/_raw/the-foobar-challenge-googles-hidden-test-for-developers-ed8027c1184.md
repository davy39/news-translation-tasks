---
title: 'The Foobar challenge: Google’s hidden test for developers'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-27T01:02:39.000Z'
originalURL: https://freecodecamp.org/news/the-foobar-challenge-googles-hidden-test-for-developers-ed8027c1184
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MirHqdGmQeG2kH_CuAkyow.jpeg
tags:
- name: coding
  slug: coding
- name: Google
  slug: google
- name: General Programming
  slug: programming
- name: recruiting
  slug: recruiting
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Daniel Simmons

  You’re just sitting at your desk, minding your own business, trying to get some
  work done. Then, as inevitably happens, you hit a minor roadblock: your code throws
  a cryptic error message.

  “No problem” you think. This isn’t your fir...'
---

By Daniel Simmons

You’re just sitting at your desk, minding your own business, trying to get some work done. Then, as inevitably happens, you hit a minor roadblock: your code throws a cryptic error message.

“No problem” you think. This isn’t your first rodeo. So you copy and paste the error message verbatim into Google and see what you get.

No luck.

There are plenty of search results, but none of them fit your situation closely enough to really provide a useful answer.

And so begins the creative Googling process. You try several combinations of the error + the context that you’re using it in. You try including the name of the library that you’re using. You know you’re getting closer…

Now on your sixth attempt, you try another combination of search terms and hit return. The page loads and you’ve just begun skimming over the results when, suddenly, your browser window splits open and you see this:

![Image](https://cdn-media-1.freecodecamp.org/images/SGTMxvXNNEOLVst2tM8KUMqC47UCvoPblaHy)

> “You’re speaking our language. Up for a challenge?”

“Wait, what?”

“Where did this come from?”

“Some sort of challenge from Google… Is this based on my search history?”

You forget about the bug in your code entirely. You are now completely engrossed in the bizarre situation that you find yourself in. And, as interesting as all of this already is, you notice something that only adds to the intrigue. Alongside the message, you see that the first button says:

> “I want to play”

Oh, so this is a **game**? Interesting…

Overcome with curiosity, you accept. The split in your browser window slowly grows to reveal a large black screen, which then fades away. You are then redirected to [www.google.com/foobar/](http://www.google.com/foobar/?eid=...). A black screen fades in and some text appears. It looks like a Unix shell.

The aesthetic of the page (the retro computer font, the hidden terminal, the lack of a modern UI) combined with the “007 — Your mission, should you choose to accept it” feel of this whole experience makes you feel like you’ve been drawn into a secret world. You are now completely engrossed.

There is some text at the top of the screen:

> “Google has a code challenge ready for you”

Just below, there is a paragraph of blueish text that sets the stage for a sci-fi adventure:

> “Success! You’ve managed to infiltrate Commander Lambda’s evil organization, and finally earned yourself an entry-level position as a Minion on her space station. From here, you just might be able to subvert her plans to use the LAMBCHOP doomsday device to destroy Bunny Planet. Problem is, Minions are the lowest of the low in the Lambda hierarchy. Better buck up and get working, or you’ll never make it to the top…”

![Image](https://cdn-media-1.freecodecamp.org/images/gQefNspuqe9bRP2e88JFcL6qfJdriFbE5jLg)

“Alright, then. So it looks like I can either explore the terminal or start the challenge…”

Your curiosity gets the better of you again and you think “I can’t just start the game without snooping around a bit”. So you type “help” and hit return. A list of shell commands pops up.

![Image](https://cdn-media-1.freecodecamp.org/images/Mva-DSMeGRFz543CL8DIdKI3t2ZEEx6wLxA-)

“Very interesting. So we’re clearly going to be working with a file system. But this is a pretty limited list of options.”

You decide to see if any of the unlisted common commands are available, so you try something simple:

```
foobar:~/guest$ pwd
```

It works! You see:

```
/home/guest
```

Awesome.

“Alright, let’s take a look at that home directory. There’s bound to be some more interesting stuff there”

So you try:

```
foobar:~/guest$ cd ..
```

And…

Nothing.

You get a new line with no error but when you run `pwd` again, just to check, you still see `/home/guest`. Ok so this thing probably isn’t the open-world unix shell chocked full of easter eggs that you’d hoped it was. So you decide to just get on with the challenge.

You type in the word “request” and hit return.

A prompt appears, warning you that this is a timed challenge and you will have 48 hours to complete it.

“Wow. Ok, so it’s timed…”

You agree and proceed.

![Image](https://cdn-media-1.freecodecamp.org/images/rb6AaixRYZyeczg-5-JNvv-EgLsdh82HPADW)

More sci-fi narrative, and then you see that something called `solar_doomsday` was added to your home folder. So you navigate to the folder, open it, and find four files:

```
constraints.txtreadme.txtsolution.javasolution.py
```

Readme seems like the obvious place to start. You open the readme file and see the following:

![Image](https://cdn-media-1.freecodecamp.org/images/9ElOQQfX6u4iACgoptqIXS3yT1uBH5WO3RXm)

“Ok” you think “when you strip away the narrative, they want me to write a function that returns a sorted array of all the square numbers (including 1) that add up to a given number, starting with the largest.” Pretty cool.

“So this is the kind of challenge that Google uses to test problem solving ability?”

“Well, I’ve already gone this far. Might as well give it a shot!”

#### About the Foobar challenge

The above is a description of Google’s Foobar challenge: a kind of easter egg in Chrome that is ostensibly used to source new talent for Google’s engineering team; although Google doesn’t seem to have acknowledged Foobar in any meaningful way (at least, not that I’ve found). There are, however, plenty of first hand accounts by developers who went through the process that make it clear this is what it’s all about.

The unique thing about the Foobar challenge is that **it** finds **you**. And not in the way that an unsolicited recruiting email or salesy text message “finds you”. It finds you by tracking your search activity and (seemingly) matching it to known needs in Google’s engineering departments. Furthermore, the sudden visual disruption of something that is otherwise so constant & unchanging, the Google search results page, is jarring enough to really draw you in — certainly a very clever use of Google’s assets.

Given Google’s access to (1) your personal browsing activity and (2) the platform that you are browsing the internet on, they really do have the perfect opportunity to snag talented people no matter where they are in a really direct and engaging way. They seem to try and suss out your basic skill level & area(s) of competency based on your search history, and then try to engage you to enter their talent funnel with this “game”, which, if completed successfully, might or might not lead to an interview invitation.

The first mention of the Foobar challenge seems to have been [this post](https://news.ycombinator.com/item?id=8588080) on HackerNews from back in 2014.

#### Side note: withgoogle.com

When you’re on the Foobar challenge page, if you open devtools and look at the DOM, you will see that the whole page is in an iFrame, whose source is: [https://foobar.withgoogle.com/?eid=...](https://foobar.withgoogle.com/?eid=...) When I first saw this I thought “Withgoogle.com? What on Earth is that?”

Again, this is a total aside from the whole topic of the Foobar challenge, but it turns out that the challenge itself lives on google’s “side project domain” called “withgoogle.com”. If you dig into this a bit you will find some other pretty interesting projects. Here are just a few that I came across:

[Paper Signals](https://papersignals.withgoogle.com/), [Quickdraw](https://quickdraw.withgoogle.com/), [CSFirst](https://csfirst.withgoogle.com/), [QiblaFinder](https://qiblafinder.withgoogle.com/), [AIYProjects](https://aiyprojects.withgoogle.com/), [ScienceJournal](https://sciencejournal.withgoogle.com/)

