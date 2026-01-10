---
title: How to Display PHP Errors and Enable Error Reporting
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-22T19:35:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-display-php-errors-and-enable-error-reporting
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c95ea740569d1a4ca0ee2.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: PHP
  slug: php
seo_title: null
seo_desc: 'By Jonathan Bossenger

  I still vividly remember the first time I learned about PHP error handling.

  It was in my fourth year of programming, my second with PHP, and I''d applied for
  a developer position at a local agency. The application required me to ...'
---

By Jonathan Bossenger

I still vividly remember the first time I learned about PHP error handling.

It was in my fourth year of programming, my second with PHP, and I'd applied for a developer position at a local agency. The application required me to send in a code sample (GitHub as we know it didn't exist back then) so I zipped and sent a simple custom CMS I'd created the previous year. 

The email I got back from the person reviewing the code still chills my bones to this day.

"I was a bit worried about your project, but once I turned error reporting off, I see it actually works pretty well".

That was the first time I searched "PHP error reporting", discovered how to enable it, and died inside when I saw the stream of errors that were hidden from me before.

PHP errors and error reporting are something that many developers new to the language might miss initially. This is because, on many PHP based web server installations, PHP errors may be suppressed by default. This means that no one sees or is even aware of these errors. 

For this reason, it's a good idea to know where and how to enable them, especially for your local development environment. This helps you pick up errors in your code early on.

## How to show PHP errors

If you Google "PHP errors" one of the first results you will see is a link to the [error_reporting](https://www.php.net/manual/en/function.error-reporting.php) function documentation. 

This function allows you to both set the level of PHP error reporting, when your PHP script (or collection of scripts) runs, or retrieve the current level of PHP error reporting, as defined by your PHP configuration. 

The `error_reporting` function accepts a single parameter, an integer, which indicates which level of reporting to allow. Passing nothing as a parameter simply returns the current level set. 

There is a long list of possible values you can pass as a parameter, but we'll dive into those later. 

For now it's important to know that each possible value also exists as a PHP predefined constant. So for example, the constant `E_ERROR` has the value of 1. This means you could either pass `1`, or `E_ERROR` to the error_reporting function, and get the same result.

As a quick example, if we create a `php_error_test.php` PHP script file, we can see the current error reporting level set, as well as set it to a new level.

```
<?php
// echo the current error reporting level
echo error_reporting();
```

```
<?php
// report all Fatal run-time errors.
echo error_reporting(1);
```

## Error reporting configuration

Using the `error_reporting` function in this way is great when you just want to see any errors related to the piece of code you're currently working on. 

But it would be better to control which errors are being reported on in your local development environment, and log them somewhere logical, to be able to review as you code. This can be done inside the PHP initialization (or `php.ini`) file.

The `php.ini` file is responsible for configuring all the aspects of PHP's behavior. In it you can set things like how much memory to allocate to PHP scripts, what size file uploads to allow, and what `error_reporting` level(s) you want for your environment.

If you're not sure where your `php.ini` file is located, one way to find out is to create a PHP script which uses the [phpinfo](https://www.php.net/manual/en/function.phpinfo.php) function. This function will output all the information relative to your PHP install.

```
<?php
phpinfo();

As you can see from my phpinfo, my current `php.ini` file is located at `/etc/php/7.3/apache2/php.ini`.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/phpinfo.png)

Once you've found your `php.ini` file, open it in your editor of choice, and search for the section called 'Error handling and logging'. Here's where the fun begins!

## Error reporting directives

The first thing you'll see in that section is a section of comments which include a detailed description of all the Error Level Constants. This is great, because you'll be using them later on to set your error reporting levels. 

Fortunately these constants are also [documented in the online PHP Manual](https://www.php.net/manual/en/errorfunc.constants.php), for ease of reference.

Below this list is a second list of Common Values. This shows you how to set some commonly used sets of error reporting value combinations, including the default values, the suggested value for a development environment, and the suggested values for a production environment.

```
; Common Values:
;   E_ALL (Show all errors, warnings and notices including coding standards.)
;   E_ALL & ~E_NOTICE  (Show all errors, except for notices)
;   E_ALL & ~E_NOTICE & ~E_STRICT  (Show all errors, except for notices and coding standards warnings.)
;   E_COMPILE_ERROR|E_RECOVERABLE_ERROR|E_ERROR|E_CORE_ERROR  (Show only errors)
; Default Value: E_ALL & ~E_NOTICE & ~E_STRICT & ~E_DEPRECATED
; Development Value: E_ALL
; Production Value: E_ALL & ~E_DEPRECATED & ~E_STRICT
```

Finally, at the bottom of all the comments is the current value of your `error_reporting` level. For local development, I'd suggest setting it to `E_ALL`, so as to see all errors.

```
error_reporting = E_ALL
```

This is usually one of the first things I set when I set up a new development environment. That way I'll see any and all errors that are reported.

After the error_reporting directive, there are some additional directives you can set. As before, the php.ini file includes descriptions of each directive, but I'll give a brief description of the important ones below.

The `display_errors` directive allows you to toggle whether PHP outputs the errors or not. I usually have this set to On, so I can see errors as they happen.

```
display_errors=On
```

The `display_startup_errors` allows for the same On/Off toggling of errors that may occur during PHP's startup sequence. These are typically errors in your PHP or web server configuration, not specifically your code. It's recommended to leave this Off, unless you're debugging a problem and you aren't sure what's causing it.

The `log_errors` directive tells PHP whether or not to log errors to an error log file. This is always On by default, and is recommended. 

The rest of the directives can be left as the default, except for maybe the `error_log` directive, which allows you to specify where to log the errors, if `log_errors` is on. By default it will log the errors wherever your web server has defined them to be logged. 

## Custom error logging

I use the Apache web server on Ubuntu, and my project-specific virtual host configurations use the following to determine the location for the error log.

```
ErrorLog ${APACHE_LOG_DIR}/project-error.log
```

This means it will log to the default Apache log directory, which is `/var/log/apache2`, under a file called `project-error.log`. Usually I replace `project` with the name of the web project it relates to. 

So, depending on your local development environment you may need to tweak this to suit your needs. Alternatively, if you can't change this at the web server level, you can set it at the `php.ini` level to a specific location.

```
error_log = /path/to/php.log
```

It is worth noting that this will log all PHP errors to this file, and if you're working on multiple projects that might not be ideal. However, always knowing to check that one file for errors might work better for you, so your mileage may vary.

## Find and fix those errors

If you've recently started coding in PHP, and you decide to turn error reporting on, be prepared to deal with the fallout from your existing code. You may see some things you didn't expect, and need to fix. 

The advantage though, is now that you know how to turn it all on at the server level, you can make sure you see these errors when they happen, and deal with them before someone else sees them!

Oh, and if you were wondering, the errors I was referring to at the start of this post were related to the fact that I was defining constants incorrectly, by not adding quotes around the constant name.

```
define(CONSTANT, 'Hello world.');
```

PHP allowed (and might still allow) this, but it would trigger a notice.

```
Notice: Use of undefined constant CONSTANT - assumed 'CONSTANT' 
```

This notice was triggered every time I defined a constant, which for that project was about 8 or 9 times. Not great for someone to see 8 or 9 notices at the top of each page...

