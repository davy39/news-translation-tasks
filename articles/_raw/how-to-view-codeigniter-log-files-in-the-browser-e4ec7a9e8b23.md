---
title: How to View CodeIgniter Log Files in the Browser
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-17T23:09:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-view-codeigniter-log-files-in-the-browser-e4ec7a9e8b23
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gmHGclQeDOJ1jUM3zhfXKg.jpeg
tags:
- name: codeigniter
  slug: codeigniter
- name: logging
  slug: logging
- name: open source
  slug: open-source
- name: PHP
  slug: php
- name: General Programming
  slug: programming
seo_title: null
seo_desc: 'By Seun Matt

  Just like any other page, it is now possible to read CodeIgniter log files in the
  browser. My Sweet Goodness!


  Example view of code igniter log files

  I began using CodeIgniter in my day to day coding after joining an awesome company.
  The...'
---

By Seun Matt

Just like any other page, it is now possible to read CodeIgniter log files in the browser. My Sweet Goodness!

![Image](https://cdn-media-1.freecodecamp.org/images/d-k2Dfg0rgazIaeVdTY2NdzxgYN-2nUJxiQJ)
_Example view of code igniter log files_

I began using CodeIgniter in my day to day coding after joining an awesome company. The company’s tech stack includes the PHP Framework — among others. Hitherto now, I’ve used (_and still use_) Laravel to build some awesome apps.

Laravel has a great logging system that is simple and elegant. Furthermore, there’s a [library](https://github.com/rap2hpoutre/laravel-log-viewer) for showing the logs in the browser. Being able to read the logs in the browser is good for application debugging and insight. Especially in a production environment.

So here I am in the world of CodeIgniter and couldn’t find an equivalent library to read my logs for debugging and insight.

So I took up the challenge and created my first Open Source project of the year — [codeigniter-log-viewer](https://github.com/SeunMatt/codeigniter-log-viewer).

### Usage

First, let’s add it to a dependency. We can do that by executing:

```
composer require seunmatt/codeigniter-log-viewer
```

Then, we can create a CodeIgniter application controller, _LogViewerController.php_:

```
private $logViewer;
```

```
public function __construct() {    $this->logViewer = new \CILogViewer\CILogViewer();    //...}
```

```
public function index() {    echo $this->logViewer->showLogs();    return;}
```

What we did is to instantiate _$logViewer_ in the constructor and then echo the result of _showLogs()_ in the _index()_ function.

The _showLogs()_ method of [codeigniter-log-viewer](https://github.com/SeunMatt/codeigniter-log-viewer) will parse the content of the log files in _application/logs_ _._ It will return it for display on the browser.

Finally, we can map any route of our choice to the _index()_ we created above. This can be done by adding an entry to the _$route_ array in _application/config/routes.php:_

```
$route['logs'] = "logViewerController/index";
```

Now we can visit _/logs_ on the browser and see all the log files there. It’s also possible to delete and download the log files.

**Note**: It is advisable to use a protected route in production environment to avoid general public access.

### How it works

Internally, the library read the name of all the log files that are available in the default logs directory into an array and reverse it. If no file is specified in the URL query parameters, the latest log file is processed for display by default.

Processing of a log file for display involves reading its contents, using regex to determine the log level and the CSS class and icon of each entry.

Each entry is also checked to know if it’s a new log line or a continuation of the previous line (_due to a newline character_).

Finally, the log entries are processed into HTML content that is then sent to the browser for display.

The complete source code is available on Github if you want to play around with it or/and adapt it for use in other frameworks.

### **Conclusion**

Now it’s easier and faster to debug CodeIgniter application — even in production. Spread the word around to friends and colleagues at work.

I want to hear about your experience (_and opinions_) of using the library in the comment section. Thanks!

Visit the [Github Link](https://github.com/SeunMatt/codeigniter-log-viewer)

