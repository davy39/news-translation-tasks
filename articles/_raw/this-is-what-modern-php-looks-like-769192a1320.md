---
title: This is what modern PHP looks like
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-12T23:29:01.000Z'
originalURL: https://freecodecamp.org/news/this-is-what-modern-php-looks-like-769192a1320
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NAnxO5afaagm6GqHFfDEVw.jpeg
tags:
- name: coding
  slug: coding
- name: language
  slug: language
- name: PHP
  slug: php
- name: software
  slug: software
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Felipe Lopes

  The title is really pretentious, isn’t? Yeah, it is. Although I’ve been working
  with PHP for years, how could I state what are the best practices and tools for
  the job? I couldn’t, but I’m going to do so.

  I’m seeing a real change in t...'
---

By Felipe Lopes

The title is really pretentious, isn’t? Yeah, it is. Although I’ve been working with PHP for years, how could I state what are the best practices and tools for the job? I couldn’t, but I’m going to do so.

I’m seeing a real change in the way developers are doing their job with PHP, not only is the language drastically changing to become more mature and robust with new versions and improvements, but the entire ecosystem around it is changing.

New tools, libraries, frameworks and articles are being created, patterns are being defined to make code more elegant and easy to understand. Several people are thinking about ways to make the work (and your life as a developer) more productive, clean and fun.

I’m not an early adopter of new trends, actually, I only adopt a new tool when I’m sure there is a community behind it and I really think it will improve my work. What I always do is try to write my code following the best practices.

Because of that, It took me time to start using things like Composer and PHPUnit. About a year ago, more or less, I’ve opened my heart to all those shiny new things.

PSR came first, then Composer, PHPUnit, Travis-ci and several other libraries and amazing tools. I’m even using an IDE now (Vim FTW, but PHPStorm with XDebug integration is a must for a sane workflow)!

### What is modern?

![Image](https://cdn-media-1.freecodecamp.org/images/YZBaPT1Lru14OBbpx3EVkSF18fLAhwhsPRUs)
_By [http://creativecommons.org/licenses/by/2.0](https://www.flickr.com/photos/karen_roe/" rel="noopener" target="_blank" title="Go to Karen Roe's photostream">Karen Roe</a> (Flickr) [CC BY 2.0 (<a href="http://creativecommons.org/licenses/by/2.0" rel="noopener" target="_blank" title="))]_

There are tons of articles around the web about how awful PHP is, how your life would be terrible if you had to work with PHP code, how the language is ugly and whatever else you could think of!

If you are going to work with legacy code, maybe your life will not be that good, but if you have the opportunity to work on a new project and are able to use all the new tools, you’re going to see this new PHP I’m gonna talk about.

I have several problems working with PHP on a daily basis, but one cannot close their eyes to the changes taking place in the language, community and the ecosystem. There is a long road ahead, but things are getting mature in the land of PHP.

I started creating an SDK for an internal API in the company I work for, just as a pet project, and decided to follow best practices. Most of them I was already doing, but I’ve made few changes in the way I do some things. Those changes and what I learned in the last year are the subject of this article and what I call Modern PHP.

### Let’s start with the workflow

![Image](https://cdn-media-1.freecodecamp.org/images/OxFTdnqCE2r6crD78HLRRgtwsvv01ctxu7aT)
_TRIO FABRIKKER — [https://nos.twnsnd.co](https://nos.twnsnd.co" rel="noopener" target="_blank" title=")_

As I said, I’m a newcomer to this IDE-thing, but it was love at first sight. PHPStorm is a great-great piece of software. It is my first and only IDE. It was my fist try and I don’t even needed to try any other.

The integration with XDebug is perfect, PHP namespace resolution, composer integration, git integration, auto-complete, code generating, code refactoring. I could keep going on and on.

I don’t think you must use an IDE, actually, this point is completely personal. You should use whatever suits your needs - Vim, Atom, Emacs, Bracket, NetBeans, PHPStorm, Eclipse, whatever. Two important points here are productivity and ergonomics. Your IDE/text editor must be there to help you.

However, for me, a great point is debugger integration. To write code for big projects (actually for the small ones too) you have to use a decent debugger. Let’s forget those var_dumps and print_rs. You need to poke those variables at runtime, analyze stack traces, set breakpoints. These things are essential and make development and refactoring easier.

I don’t even know if there are other options here, XDebug has everything you need. Do you have a few minutes? If you haven’t done this yet, take a moment to setup XDebug and integrate it into your IDE or text editor. Start debugging your code using the right tools.

The other tool I want to bring your attention to is GitHub. Another entire article could be written about how good Git and GitHub are and why you must start keeping your code under a versioning system. But I wanna show you another reason.

The focus here is integration.

There are several tools which integrate with GitHub and you should start using them. Those tools can generate metrics, run tests, run jobs for you during a continuous integration process and do all sorts of things in your workflow. Integration is a good reason for you to start using GitHub, all the others are subject for another moment.

### Dependency management

![Image](https://cdn-media-1.freecodecamp.org/images/TQqLDoQvKV730jefjQIuEyaUOSYyAY596Tzg)
_INSTITUTO PASTEUR. LISBOA, PORTUGAL — [https://nos.twnsnd.co](https://nos.twnsnd.co" rel="noopener" target="_blank" title=")_

Another point in this modern PHP ecosystem is dependency management, and Composer is the tool for the job.

Composer is 5 years old, but it seems to me that massive adoption took place a couple of years ago. Maybe because I’m not an early adopter or maybe because PHP developers are reluctant to change.

This tool provides a front end to Packagist, which is a PHP package repository consisting of PHP libraries, projects and tools, whose source code is stored in Github (or other places like BitBucket).

All the libraries I’m talking about in this article, and maybe one of those pet projects of yours, can be added to your project with a simple

```
$ composer require package_vendor/package_name
```

If you don’t know the vendor of a package, you can `search` for a package to find and install the right one.

```
$ composer search package_name
```

Composer would be a great tool if it just did this work, manage dependencies, but it does a lot more. Take a time to install Composer and read the [documentation](https://getcomposer.org/doc/).

### Command line interface done right

I really like to try ideas quickly using CLI interfaces. For me, one of the greatest REPL tools is the [IPython](https://ipython.org/). It helps you autocomplete your code, let you easily define functions, ease the access to the documentation and several other amazing features. The downside for us, the tool is for Python, not PHP.

In the PHP world we have something called “interactive mode” which can be accessed by terminal, just typing

```
$ php -aInteractive mode enabled
```

```
php >
```

At this point, you are in the interactive mode and can start testing something. It works, but the tool is just too unintuitive. I’ve tried it several times but, since I knew what IPython was able to do, I could not keep using it.

To our luck, there is a cool new CLI (command line interface) on the block and its name is Psysh. Psysh is an amazing tool, full of interesting features and can be installed globally or per project using composer.

The nicest Psysh feature for me is inline documentation. Accessing the doc for a PHP function without heading over to Php.net is great. The downside is that you need to do few things before it is fully functional.

After installing it, type the following commands (I’m using Debian here, this may not work for everyone) in order to get it working properly

```
$ apt-get install php7.1-sqlite3$ mkdir /usr/local/share/psysh$ wget http://psysh.org/manual/en/php_manual.sqlite -o /usr/local/share/psysh/php_manual.sqlite
```

The first command is not mandatory and if you have the Sqlite already installed you can skip this step. The second command creates the directory to store the documentation and the third line downloads and save the doc into the previously created directory. Remember, all these commands must run as root.

Now you have this

![Image](https://cdn-media-1.freecodecamp.org/images/PLyALiyVTXJ5076Iq7s9f085JJxWdJWGqo-X)
_Screenshot of psysh doc in action, showing information about json_decode_

Head to [Psysh](http://psysh.org) and learn more about this awesome tool.

### You should start testing

This a mantra I’m saying to myself every day. Like lots of people, I don’t test my code as much as TDD suggests. I’m getting into testing now and have been doing so for the past half a year, and there is a long road ahead.

I decided to learn about tests when working with a complex legacy project. The code was so fragile and rigid that anytime we added some code it broke something. New feature? Implement and break something! Fixing a bug? Create another one.

That was a big problem, which I discussed in [another article](https://medium.freecodecamp.org/few-thoughts-on-legacy-hell-e229f76529e0), and made me start giving tests a chance.

The first tool I was presented was [PHPUnit](https://phpunit.de/). As stated in the official site

> PHPUnit is a programmer-oriented testing framework for PHP.  
> It is an instance of the xUnit architecture for unit testing frameworks.

So, PHPUnit is a framework for helping you create tests for your projects, unitary tests. It gives you several functions to test the outcome of your code and generate a nice output with the result from those tests.

Since I started thinking about tests, reading and talking to people about it, I’ve discovered another great tool, which complements the work you’ve put in those unitary tests, it is calle Behat, which is a BDD framework for PHP.

BDD (Behavior-Driven Development) is a development process which came from TDD (Test-Driven Development). Those acronyms are not important now, what is important is that you can specify your tests using a more natural language, a language that non-technical folks can understand.

This language is called Gherkin and is used to describe the expected behavior being tested. A test description, using Gherkin, looks like this

![Image](https://cdn-media-1.freecodecamp.org/images/m0wRKIZ8qPUqDcmhRejF4pes2rLYVJoR4mRJ)

Behind those lines there is PHP code that is called whenever there is a match between a line and a regex pattern specified in the PhpDoc of the method. This code implements those steps and what a real user would do, using your SDK, application or web system.

The workflow with Behat is so smooth. After everything properly configured, you start writing all possible scenarios for testing a feature. The first time you run Behat, it gives you all the method templates you should add to your PHP Context class in order to implement each step in a scenario.

After that, you start writing the actual code for each step and keep repeating this cycle.

* Implement PHP code for a step
* Run tests
* If everything is fine, write PHP code for another step
* If something is broken, fix it

After half an hour of configuring and reading documentation, you are prepared to use Behat, you’ll see that in the end it is all PHP code and you already know how to program with it.

### Continuous Integration

Continuous integration (CI) is a process - a way to do something, and this thing, for us software engineers, is creating software.

In plain English, it is the act of incorporating small chunks of code constantly (maybe several times a day) into your code base. Code which has been tested and did not break anything. CI helps you automate the building, testing and deployment of your applications.

With a few clicks you can integrate your GitHub project with Travis CI and every push to your repository will run those tests you created with PHPUnit and Behat, telling you whether the the last feature you’ve implemented is ready, or not, to be merged. Besides that, you can use Travis CI to deploy your code to production and staging.

Having a nice pipeline of work with a well defined process is great and Travis CI can help you with this job. Follow this nice [Getting started](https://docs.travis-ci.com/user/getting-started/) and discover how interesting it is to think about the process of software development, not just the code itself.

### Adhere to PSR-1 and PSR-2

If you don’t know what PSR is, you should. Actually, PSR stands for PHP Standard Recommendations and is proposed by [PHP-FIG](http://www.php-fig.org/) (PHP Framework Interop Group), a consortium formed by members from the biggest PHP projects, frameworks and CMSs, which are thinking about the future of the language, ecosystem and discussing standards to be followed.

For a long time, PHP had no coding style. I’m not that old, but every time I looked into someone’s project or library, it was following a different style. Sometimes the bracket was left in one position, sometimes it was put in the next line, different approaches were used to deal with long lines and every other combination of style and preference you could think of. It was a mess.

PHP-FIG does many other jobs, but by proposing a single unity of code, they are saying “Let’s stop worrying about code style, let’s everyone follow a standard and start thinking about creating great software”. Now, whenever you take a look at someone’s code you just worry about understanding how it works, not blaming the format, the structure.

There are, until the end of this article, 9 accepted PSRs proposing common solutions for common problems. But if you don’t know anything about those standards, start with the [PSR-1](http://www.php-fig.org/psr/psr-1/) and [PSR-2](http://www.php-fig.org/psr/psr-2/).

These standards propose the modern PHP coding style. Make sure you read them before start using them. Don’t think you’ll remember all of them when coding, it is a process, but to make you sure, there are tools to help you with it.

[PHP CodeSniffer](https://packagist.org/packages/squizlabs/php_codesniffer) is a tool you can find on Packagist that you can install with Composer. I don’t think the repository name was the best choice, because it ships two different tools, phpcs and phpcbf.

Phpcs is the code sniffer, it will scan your entire code, looking for parts that are not following the configured coding standard.

You can use several coding standards with phpcs and you can even create your own. At the end of the code scan, phpcs shows you a list of the pieces of code not following the standard. It is great.

Now, how to change everything which is wrong? You could open every file, change the code, run phpcs again, see the error not being shown, and repeat the process. It’ll be extra boring.

To solve this problem, PHP CodeSniffer came with another tool, called phpcbf, or PHP Code Beautifier. You run phpcbf, following the same rule set and, voilá, it fixes everything for you, or it tries to do its best without breaking your code.

Try to create the habit of running phpcs and phpcbf before pushing any changes in your code to the repository, this will ensure that all of your code adhere to the standards and if someone likes your tool/project and wants to contribute, they will have no problem reading it.

### Frameworks

I’m not going to dedicate too much time discussing frameworks. There are several good ones out there, each one with its ups and downs. Personally, I prefer not to use those big frameworks, with everything inside. I like the idea that you must use just what you need.

If you need a HTTP client, use Guzzle. If you need a template engine, use Twig. If you need a router, find a good component which suits your needs and use it. Glue these components together and create your application.

[Symfony](https://symfony.com/) is doing a great job towards this concept. You can use the entire framework for a project, or you can just take whatever you want and use it. Simple as that.

However, whenever I need a framework to write an application, I chose one of the so called microframeworks. They are really small, offer just the basics and are easy to customize and easier to make them follow your project structure.

My microframework of choice is [Slimframework](https://www.slimframework.com/) and I think you should read about it. It is simple for doing small projects, but it gets a bit more complex for bigger ones.

By the way, and this is for those who are starting with programming, I really think that before adopting a framework and dying for it, you should try to create your own. This will give you the understanding of the whole mechanism and ease the adoption of a big one.

### The Modern PHP Toolset

Let’s finish this article with a list of links. To me, these components, tools and libraries represent a great deal of what Modern PHP is:

* [Slimframework](https://www.slimframework.com/): a nice and cool microframework
* [Symfony](http://symfony.com/): a bigger framework which is filled with great and reusable components
* [Guzzle](http://docs.guzzlephp.org/en/stable/): a simple and easy to use HTTP client
* [PHPUnit](https://phpunit.de/): a framework for unitary testing
* [Behat](http://behat.org/en/latest/): a framework for Behavior-Driven Development
* [PHPCS/CBF](https://github.com/squizlabs/PHP_CodeSniffer): code sniffer and code beautifier
* [Faker](https://github.com/fzaninotto/Faker): fake data generator
* [Psysh](http://psysh.org/): a runtime developer console (CLI) full of amazing features
* [Composer](https://getcomposer.org/): dependency management and other useful features
* [Packagist](https://packagist.org/): package repository
* [Twig](https://twig.symfony.com/): template engine

The title was really pretentious, I know. What I really wanted to show here is that PHP is evolving and the ecosystem is evolving at the same (maybe faster) pace.

