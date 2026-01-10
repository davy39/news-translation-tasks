---
title: Laravel Valet Performance – How to Prevent 504 Errors and Speed Up Valet
subtitle: ''
author: Sule-Balogun Olanrewaju
co_authors: []
series: null
date: '2023-01-02T23:12:30.000Z'
originalURL: https://freecodecamp.org/news/speed-up-performance-in-laravel-valet
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-jonathan-petersson-399636.jpg
tags:
- name: error
  slug: error
- name: Laravel
  slug: laravel
- name: PHP
  slug: php
seo_title: null
seo_desc: "Last week, I decided to install Laravel Valet on my Mac. But after the\
  \ installation, the performance of the microservice architecture application I had\
  \ it on was quite slow. \nI wondered if it was an M1 issue or because I had yet\
  \ to shut the machine d..."
---

Last week, I decided to install Laravel Valet on my Mac. But after the installation, the performance of the microservice architecture application I had it on was quite slow. 

I wondered if it was an M1 issue or because I had yet to shut the machine down. I shut down, and the problem persisted. And I couldn't find anything online indicating that it was an issue with M1. So how could I fix it?

**In this tutorial, you'll learn:**

* Why does the Error 504 occur?
* What is Laravel Valet and how does it work?
* Valet commands you should know
* How to fix the 504 error and speed up performance in Valet

## Why does the Error 504 occur?



![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-145.png)
_Error 504 Nginx_

Error 504, also known as "Gateway timeout", is an error that occurs when a server takes longer than usual to respond to an HTTP request. This makes it unable to complete the request cycle. 

The Gateway timeout is a server-side error caused by several things. It can result from network connectivity issues when the server exceeds the default limit of **256M** or an execution time of **60 seconds**, an overloaded server, firewall, and so on. 

This error happens with local servers, too, such as XAMPP, WAMP and Valet, during the local development lifecycle. 

This article will help you fix this problem on Valet by adding some configurations to speed up the server request lifecycle.

## What is Laravel Valet and How Does It Work?

Laravel Valet is a development environment for macOS, Windows, and other operating systems. Once installed, Valet runs Nginx processes in the background when your laptop comes on.

Unlike other development environments like XAMPP and WAMP, you'll have to manually start your server each time you set out to work. Valet then uses DnsMasq to proxy all parked applications to a `.test` domain. 

So, for instance, you would access on XAMPP server `http://localhost/application` but on valet, you would do `http://application.test`, and it will point to where the application is installed. 

Working with Valet means you don't have to put all applications in an htdocs or www directory. Instead, any random directory you create will work just perfectly in Valet. 

## Helpful Valet Commands You Should Know:

* **`valet park`:** Registers all applications/sites in a directory and exposes them with the .test domain.

```
cd ~/project_directory
valet park 
```

* **`valet parked`:** Gives a tabular breakdown of all registered sites. Information like site name, SSL, URL, and path is available.

```
cd ~/project_directory
valet parked
```

* **`valet secure`:** Secures your application with an SSL certificate and makes the site accessible over HTTPS.

```
cd ~/project_directory/site
valet secure
```

* **`valet unsecure`:** Use this command to unsecure your site and revert to serving over HTTP.

```
cd ~/project_directory/site
valet unsecure 
```

* **`valet isolate`:** Isolates a particular site and makes it run on a different PHP version that's not the globally installed version. You can run `php -v` on the terminal to see the version. But if some of your applications want to downgrade or upgrade, you should use the isolate command and specify the version you need. The isolate command below, enforce the site to use PHP version 7.4:

```
cd ~/project_directory/site
valet isolate @php7.4
```

* **`valet unisolate`:** Reverts a site back to the globally installed PHP version.

```
cd ~/project_directory/site
valet unisolate
```

* **`valet restart`:** The restart command ensures all valet services are restarted. It's useful when configurations are modified, updated, and installed.

```
cd ~/project_directory/site
valet restart
```

* **`valet -v`:** This command helps check the the current Valet version. Not only that, but the command also shows a list of all available commands and descriptions of what they do in Valet.

```
~/project_directory/site
valet -v
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/Screenshot-2022-12-26-at-11.33.10.png)
_Valet available commands_

## How to Speed Up Performance in Valet

Over in the terminal, we will need to create a file `www.conf` in a directory and then add the configuration settings we need.

Get your PHP global version and copy it like this:

```
php -v
```

Navigate to the directory and replace the 7.4 with the PHP version you copied earlier.

```
cd /opt/homebrew/etc/php/7.4/php-fpm.d
```

Create a `www.conf` file like this:

```
touch www.conf

```

Open the file so you can add the valet configuration settings:

```
open -a TextEdit www.conf
```

The command opens up the `www.conf` file in your text editor and you can update the file with these settings:

```
pm.max_children = 200
pm.start_servers = 20
pm.min_spare_servers = 10
pm.max_spare_servers = 20
pm.process_idle_timeout = 10s
pm.max_requests = 500
```

Save and close the file from the text editor.

Let's go through each line we added to the `www.conf` file:

* **`pm`** is an acronym for process manager, and the setting will impact how the process manager controls every child process. The possible values available to us include static, on-demand, and dynamic.
* **pm.max_children** is a static option, indicating the maximum number of the child processes, which we have set to 200.
* **`pm.start_servers, pm.max_spare_servers`** and `pm.min_spare_servers`: These are dynamic values, and the child processes are set dynamically based on the server directives – that is, start_servers = 20, min_spare_servers = 10 and max_spare_servers = 20.
* **pm.process_idle_timeout**: the total time taken for an idle request not processed to be killed/terminated is set to a default value of 10 seconds (s). Other units can be estimated in minutes (m), hours (h) or days (d).
* **pm.max_requests**: This refers to the maximum number of requests a child process can handle at a given time before it's killed/terminated. If the request executes the maximum, it becomes idle, and the pm gets rid of it.

Finally, restart all services from the terminal using the sudo brew command. Notice again the 7.4 – that's because of my global PHP version.

```
sudo brew services restart php@7.4
```

You can now say bye-bye to the 504 error and slow Valet performance in your local environment.

## Wrapping up

In this article, you have learned about working with Laravel Valet and how to get all Valet configurations set up. You also learned how to ensure a fast development environment and get rid of persistent 504 gateway timeout errors. 

Keep learning and Happy Coding!

You can find me on [LinkedIn](https://www.linkedin.com/in/suleolanrewaju/) and [Twitter](https://twitter.com/bigdevlarry).

