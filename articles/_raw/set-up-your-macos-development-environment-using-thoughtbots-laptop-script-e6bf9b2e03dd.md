---
title: Set up your macOS development environment using Thoughtbot’s Laptop script
subtitle: ''
author: Fatos Morina
co_authors: []
series: null
date: '2018-02-08T15:12:22.000Z'
originalURL: https://freecodecamp.org/news/set-up-your-macos-development-environment-using-thoughtbots-laptop-script-e6bf9b2e03dd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cNXpArTQUERq8nbe9nllqw.jpeg
tags:
- name: education
  slug: education
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'One of the things that may prevent us from changing or even thinking of
  changing our working environment is the necessity to do all the installations and
  the configurations that we have already set up for software development.

  Fortunately, there is a...'
---

One of the things that may prevent us from changing or even thinking of changing our working environment is the necessity to do all the installations and the configurations that we have already set up for software development.

Fortunately, there is a cure for this *pain*. *Laptop* is a script that prepares your working macOS machine for web and mobile development.

![Image](https://cdn-media-1.freecodecamp.org/images/TYlh5-0uZtwVDI1AstOGORoIqEBT5OIAyYVM align="left")

The script setup is made up of:

1. macOS tools:
    

* [Homebrew](http://brew.sh/) for managing operating system libraries.
    

2. Unix tools:
    

* [Exuberant Ctags](http://ctags.sourceforge.net/) for indexing files for vim tab completion
    
* [Git](https://git-scm.com/) for version control
    
* [OpenSSL](https://www.openssl.org/) for Transport Layer Security (TLS)
    
* [RCM](https://github.com/thoughtbot/rcm) for managing company and personal dotfiles
    
* [The Silver Searcher](https://github.com/ggreer/the_silver_searcher) for finding things in files
    
* [Tmux](http://tmux.github.io/) for saving project state and switching between projects
    
* [Watchman](https://facebook.github.io/watchman/) for watching for filesystem events
    
* [Zsh](http://www.zsh.org/) as your shell
    

3. Heroku tools:
    

* [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and [Parity](https://github.com/thoughtbot/parity) for interacting with the Heroku API
    

4. GitHub tools:
    

* [Hub](http://hub.github.com/) for interacting with the GitHub API
    

5. Image tools:
    

* [ImageMagick](http://www.imagemagick.org/) for cropping and resizing images
    

6. Testing tools:
    

* [Qt 5](http://qt-project.org/) for headless JavaScript testing via [Capybara Webkit](https://github.com/thoughtbot/capybara-webkit)
    

7. Programming languages, package managers, and configuration:
    

* [ASDF](https://github.com/asdf-vm/asdf) for managing programming language versions
    
* [Bundler](http://bundler.io/) for managing Ruby libraries
    
* [Node.js](http://nodejs.org/) and [NPM](https://www.npmjs.org/), for running apps and installing JavaScript packages
    
* [Ruby](https://www.ruby-lang.org/en/) stable for writing general-purpose code
    
* [Yarn](https://yarnpkg.com/en/) for managing JavaScript packages
    

8. Databases:
    

* [Postgres](http://www.postgresql.org/) for storing relational data
    
* [Redis](http://redis.io/) for storing key-value data
    

Its installation is pretty straightforward and can be done very quickly.

First, you need to download the script:

```python
curl --remote-name https://raw.githubusercontent.com/thoughtbot/laptop/master/mac
```

You should review the script before you run it:

```python
less mac
```

Then you can execute the downloaded script:

```python
sh mac 2>&1 | tee ~/laptop.log
```

Finally, you can review the log:

```python
less ~/laptop.log
```

It should take less than 15 minutes to install (depends on your machine).

macOS versions that are supported at the time of this writing are:

* macOS Mavericks (10.9)
    
* macOS Yosemite (10.10)
    
* macOS El Capitan (10.11)
    
* macOS Sierra (10.12)
    

According to the Laptop’s [description](https://github.com/thoughtbot/laptop), older versions of macOS may work but aren’t regularly tested.

Laptop is an open source project, initiated and maintained by [Thoughtbot](https://thoughtbot.com/?utm_source=github). You can view more information about it and its implementation and also have the opportunity to contribute to it by visiting its GitHub [page](https://github.com/thoughtbot/laptop).

*This article was initially published on my blog,* [*FatosMorina.com*](http://www.fatosmorina.com/set-macos-development-environment-using-thoughtbots-laptop-script/)
