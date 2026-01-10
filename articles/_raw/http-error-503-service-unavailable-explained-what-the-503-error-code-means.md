---
title: HTTP Error 503 Service Unavailable Explained – What the 503 Error Code Means
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-10-02T02:36:00.000Z'
originalURL: https://freecodecamp.org/news/http-error-503-service-unavailable-explained-what-the-503-error-code-means
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c986c740569d1a4ca19fd.jpg
tags:
- name: error
  slug: error
- name: servers
  slug: servers
- name: web
  slug: web
seo_title: null
seo_desc: 'Errors happen – there''s some unexpected maintenance, a bug that went unnoticed,
  or a page goes viral and the flood of connections take the server down.

  If you''ve been online for any amount of time, no doubt you''ve seen the somewhat
  vague 503 Service ...'
---

Errors happen – there's some unexpected maintenance, a bug that went unnoticed, or a page goes viral and the flood of connections take the server down.

If you've been online for any amount of time, no doubt you've seen the somewhat vague 503 Service Unavailable error.

In this article we'll go over HTTP status codes, what the 503 error means, and some possible ways to solve it – both for a site you're trying to visit and for your own site.

## An overview of HTTP status codes

Servers that host web pages listen for requests from web browsers or devices, also known as clients. The server then uses a bunch of different status codes to communicate back.

These status codes are organized into different classes, which is indicated by the first number of the status code:

* 1xx: Information – the server is still processing the request
* 2xx: Success – the request succeeded and the server responds with the page or resource
* 3xx: Redirection – the page or resource has moved and server will respond with its new location
* 4xx: Client error – there is an error in the request from the browser or device
* 5xx: Server error – there is an error with the server

The last two digits of each HTTP status code represent a more specific status for each class. For example, 301 means that a page or resource has moved permanently, while 302 means the move is temporary.

Check out this page for a list of common HTTP status codes and their meaning: [https://en.wikipedia.org/wiki/List_of_HTTP_status_codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

Most status codes go by totally unnoticed, which is fine because it means everything is working. It's only when you get to the 4xx-5xx range that you might notice a status code because you'll see a page like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/E20Ry-1.png)
_A typical 503 error page – Source: [Stack Overflow](https://stackoverflow.com/questions/27944151/asp-net-website-shows-503-service-unavailable-after-successful-publishing)_

Now that you have a basic understanding of HTTP status codes, let's dig a bit deeper into the 503 Service Unavailable error.

## What does the 503 error code mean?

As mentioned above, 5xx status codes mean there's a problem with the server itself.

A 503 Service Unavailable error means that the page or resource is unavailable. There are many reasons why a server might return a 503 error, but some common reasons are maintenance, a bug in the server's code, or a sudden spike in traffic that causes the server to become overwhelmed.

The message that's sent with the 503 error can vary depending on server it's coming from, but here are some of the common ones you'll see:

> - 503 Service Unavailable  
> - 503 Service Temporarily Unavailable  
> - HTTP Server Error 503  
> - HTTP Error 503  
> - Error 503 Service Unavailable  
> - The server is temporarily unable to service your request due to maintenance downtime or capacity problems. Please try again later.  
>   
> [Source](https://kinsta.com/blog/http-error-503/)

Whatever the reason for the 503 error, it's usually temporary – the server will restart, traffic will die down, and the issue will resolve itself.

## How to solve the 503 Status Unavailable error

When trying to solve a 503 error, there are two general camps.

The first is where you're an end user, and you're trying to visit a site that you don't own. In the second, you own the site, and it's throwing 503 errors to people who are trying to visit.

The method to solve 503 errors is different depending on which group you fall into. Let's take a look at some things you can do as an end user if you see a 503 error.

### How to solve a 503 Status Unavailable error as an end user

Since 5xx status codes mean that the error is on the server-side, there isn't a lot you can do directly.

Even though 503 errors are usually temporary, there are some things you can do while you wait.

**#1: Refresh the page**

Sometimes the error is so temporary that a simple refresh is all it takes. With the page open, just press Ctrl - R on Windows and Linux, or Cmd - R on macOS to refresh the page.

**#2: See if the page is down for other people**

The next thing you can do is use a service like [Is It Down Right Now?](https://www.isitdownrightnow.com/) or [Down For Everyone Or Just Me](https://downforeveryoneorjustme.com/) to see if other people are getting the same error.

Just go to either of those sites and enter in the URL for the page you're trying to visit.

The service will ping the URL you entered to see if it gets a response. Then it'll show you some cool stats and graphs about the page:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-44.png)
_Checking [freeCodeCamp](https://www.freecodecamp.org/) on Is It Down Right Now?_

If you scroll down a bit you'll see some comments from other people. Often people will give their general location and other data, so this can be a good way to determine if the error is just affecting certain regions or specific devices.

**#3: Restart your router**

Sometimes the issue has to do with a DNS server failure.

DNS stands for Domain Name System, and they basically act as translators between IP addresses and human readable URLs.

For example, you can visit Google by entering its long IP address directly (172.217.25.206), or you can just enter in the URL, www.google.com.

It's a DNS, often hosted on a server, that handles all that behind the scenes.

All of that is to say, many routers cache responses from DNS servers (www.google.com <==> 172.217.25.206). But sometimes this cache can get corrupted and cause errors.

An easy way to reset or "flush" the cache is to restart your router. Just unplug your router for about 5 seconds, then plug it back in again.

It should restart after a minute and all of your devices should reconnect automatically. Once they do, try visiting the site again.

### How to solve a 503 Status Unavailable error as the site's owner

If you are the owner/developer of the site that's returning 503 errors, there's a bit more you can do to diagnose and resolve the issue.

Here are some general tips to get you started:

**#1: Restart the server**

Development is tough – even a simple static page can have so many moving parts that it can be difficult to pin down what's causing the 503 error.

Sometimes the best thing to do is to restart the server and see if that fixes the issue.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/1rs7t0-1.jpg)
_Source: [imgflip](https://imgflip.com/i/1rs7t0)_

The exact method of restarting your server can vary, but usually you can access it from your provider's dashboard or by SSH'ing into the server and running a restart command.

The server should restart after a couple of minutes. If you've configured everything to run automatically on boot, you can visit your site and see if it's working.

**#2: Check the server logs**

The next thing to do is check the logs.

The location of the server logs can vary depending on what service you're running, but they're often found in `/var/log/...`.

Take a look around that directory and see if you can find anything. If not, check the manual for your programs by running `man program_name`.

**#3: Check if there's ongoing automated** maintenance

Some service providers offer automated package updates and maintenance. Normally this is a good thing – they usually occur during downtime, and help make sure everything is up-to-date.

Occasionally 503 errors are due to these scheduled maintenance sessions. 

For example, some hosting providers that specialize in WordPress hosting automatically update WP whenever there's a new release. WordPress automatically returns a 503 Service Unavailable error whenever it's being updated.

Check with your service providers to see if the 503 error is being caused by scheduled maintenance.

**#4: Check your server's firewall settings**

Sometimes 503 Service Unavailable errors are cause by a misconfigured firewall where connections can get through, but fail to get back out to the client.

Your firewall might also need special settings for a CDN, where multiple connections from a small handful of IP addresses might be misinterpreted as a DDoS attack.

The exact method of adjusting your firewall's settings depends on a lot of factors. Take a look at your pipeline and your service provider's dashboards to see where you can configure the firewall.

**#5: Check the code**

Bugs, like errors, happen. Try as you might, it's impossible to catch them all. Occasionally one might slip through and cause a 503 error.

If you've tried everything else and your site is still showing a 503 Service Unavailable error, the cause might be somewhere in the code.

Check any server-side code, and pay special attention to anything having to do with regular expressions – [a small regex bug](https://www.freecodecamp.org/news/freecodecamp-servers-update-october-2019/) is what caused a huge spike in CPU usage, rolling outages, and about three days of panic for us at freeCodeCamp.

Hopefully you'll be able to track down the culprit, deploy a fix, and everything will be back to normal.

## In summary

That should be everything you need to know about 503 Service Unavailable errors. While there's usually not much you can do when you see a 503 error, hopefully some of these steps will help the next time you encounter one.

Stay safe, and happy refreshing-until-it-works :)

