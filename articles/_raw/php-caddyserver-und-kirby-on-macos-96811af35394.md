---
title: How to set up PHP, CaddyServer, and Kirby on MacOS — and why you should do
  it
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-03T07:32:22.000Z'
originalURL: https://freecodecamp.org/news/php-caddyserver-und-kirby-on-macos-96811af35394
coverImage: https://cdn-media-1.freecodecamp.org/images/0*A-xWmyVxuvS0GqWQ
tags:
- name: Apple
  slug: apple
- name: development
  slug: development
- name: PHP
  slug: php
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Philipp Haidenbauer

  Recently Kirby Version 3.0 was released. As I have worked with Version 2 for quite
  some time in the past, I figured why not give it a try?

  Just before Christmas, I bought a brand new MacBook Air, so it was obvious that
  I would ...'
---

By Philipp Haidenbauer

Recently [Kirby Version](https://getkirby.com/) 3.0 was released. As I have worked with Version 2 for quite some time in the past, I figured why not give it a try?

Just before Christmas, I bought a brand new MacBook Air, so it was obvious that I would like to try Kirby right away on it. I stumbled upon a great [article](https://simonecarletti.com/blog/2016/05/caddy-server-php-macosx/) on how to set up [CaddyServer](https://caddyserver.com/) and PHP on MacOS. But I changed some of it.

### CaddyServer, PHP and Kirby

Let’s get started with a brief overview of what software I’m talking about.

#### [PHP](http://www.php.net/)

I don’t think I have much to say about PHP. It’s probably one of the oldest Scripting Languages out there in the WebWorld. PHP was “the” language for making your website “dynamic”. And it was also the first language I discovered and learned to play around with.

#### [CaddyServer](https://caddyserver.com/)

Is a small but very powerful Web-Server which I discovered a few months ago. It has some really nice features like automatic SSL / HTTPs and a really easy configuration file (which you will see later). And it’s blazing fast. :)

#### [Kirby](https://getkirby.com/)

Another great tool I discovered a few years ago. Basically, it’s a CMS (Content Management System) based on a simple FileStructure. Even if you don’t know much about PHP, it’s relatively simple to get into creating templates for pages and extending the whole functionality.

#### Why?

Now that you know about all three projects, you might be asking why you should use them together. Well, there are multiple reasons for it:

* MacOS comes with a default [apache2](https://httpd.apache.org/) installation, but as you might know, Apache is one of the biggest HTTP servers out there. It’s widely adopted, but it has one downside. It eats memory and CPU like no other web-server out there. So if you’re on the go, it also eats battery like crazy and I don’t like that.
* Caddy is very lightweight and doesn’t really use much Memory / CPU / Battery.
* Kirby, as I’ve said is easy to customize and extend. As it’s a CMS, you don’t need to worry about a database or application-specific logic from the beginning. That way you can prototype pretty fast, which leads to faster results and more satisfaction as you get things done. :)

Without further ado, let’s get into setting it up:

### First of all

It’s essential to have [homebrew](https://brew.sh/index_de) installed, as package management get’s a whole lot easier with it.

You can install it with a simple command:

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### PHP

Now that we have a package manager, it’s time to install the correct PHP-version. Kirby needs at least PHP7.1 so I installed 7.2 :)

```
brew install php@7.2
```

There are also some extensions which are needed:

```
brew install freetype jpeg libpng gd
```

### CaddyServer

Now that we have PHP and some dependencies installed we can now install CaddyServer.

Simply download the suitable Version from [https://caddyserver.com/download](https://caddyserver.com/download).

You will receive a zip file. Extract it and copy the executable to a path inside your $PATH (in my case `/Users/phaidenbauer/bin/`):

```
unzip caddy_v0.11.2_darwin_amd64_personal.zipcp caddy /Users/phaidenbauer/bin/caddy
```

### Kirby

Next one is Kirby. Again download the zip from [https://getkirby.com/try](https://getkirby.com/try).  
Extract it somewhere you have your projects. In my case that’s `/Users/phaidenbauer/development/`.

The next essential thing to get this whole thing running is the Caddyfile which tells Caddy what to do :)

```
localhost:8080tls offroot ./gzip
```

```
rewrite {    r .*    to {path} {path}/ /index.php?{path}&{query}}
```

```
fastcgi / 127.0.0.1:9000 phpon startup launchctl load -w /Users/phaidenbauer/Library/LaunchAgents/homebrew.mxcl.php@7.2.pliston shutdown launchctl unload -w /Users/phaidenbauer/Library/LaunchAgents/homebrew.mxcl.php@7.2.plist
```

Let’s go through it:

`localhost:8080` tells it on which Port it should listen. If you don't want to run it as root (or via `set_cap`) you should use something above 1024.

`tls off` disables the built-in SSL / HTTPS feature, as we are only working locally.

`root ./` sets the root-path of the serving directory.

`gzip` enables the gzip-compression for responses.

`rewrite { r .* to {path} {path}/ /index.php?{path}&{query} }` rewrites all incoming URLs to suite Kirby’s needs. (It’s probably not the best solution but it works fine for my development environment.)

`fastcgi / 127.0.0.1:9000 php` tells caddy to forward requests to a FastCGI-server. Which is, in our, case PHP.

Now we have two special functions.

```
on startup launchctl load -w /Users/phaidenbauer/Library/LaunchAgents/homebrew.mxcl.php@7.2.pliston shutdown launchctl unload -w /Users/phaidenbauer/Library/LaunchAgents/homebrew.mxcl.php@7.2.plist
```

As I mentioned earlier it is just a MacBook Air, so I don’t want to have PHP running all the time. Especially when I don’t need it. The great thing is caddy can run commands on events. In this case, we use the startup and shutdown event to start and stop PHP. Great! No more waste of RAM and CPU while checking emails.

### Start the whole thing :)

Now we are pretty much set. The last thing to do is start them all together and start working:

```
cd /Users/phaidenbauer/development/fly.phaidenbauer.comcaddy
```

You should see something like this:

```
Activating privacy features... done.http://localhost:8080WARNING: File descriptor limit 4864 is too low for production servers. At least 8192 is recommended. Fix with `ulimit -n 8192`.
```

And that's it. Take your favorite browser and surf to [http://localhost:8080](http://localhost:8080). Depending on if you downloaded the Kirby-Plainkit or Kirby-Starter kit you should see a simple “Hello” or a simple gallery.

And that’s it. Happy hacking :)

