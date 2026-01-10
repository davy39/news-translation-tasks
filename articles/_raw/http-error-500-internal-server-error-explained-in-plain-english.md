---
title: HTTP Error 500 – Internal Server Error Explained in Plain English
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-21T23:39:17.000Z'
originalURL: https://freecodecamp.org/news/http-error-500-internal-server-error-explained-in-plain-english
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a24740569d1a4ca23d2.jpg
tags:
- name: http
  slug: http
seo_title: null
seo_desc: "By Jackson Bates\nError codes in the 4xx range mean you or your browser\
  \ did something wrong. Maybe you weren't logged in, tried to access something you\
  \ didn't have permission for, or simply got lost. \nHowever, error codes in the\
  \ 5xx range means the er..."
---

By Jackson Bates

Error codes in the 4xx range mean you or your browser did something wrong. Maybe you weren't logged in, tried to access something you didn't have permission for, or simply got lost. 

However, error codes in the 5xx range means the error is out of your hands entirely (unless you are the server developer / administrator). Perhaps the second* most frustrating error code you can ever stumble across on the internet is the dreaded 500.

## What does it mean?

Simply put, the server tried to do something and failed.

According to [RFC 7231](https://tools.ietf.org/html/rfc7231#section-6.6.1):

> The 500 (Internal Server Error) status code indicates that the server encountered an unexpected condition that prevented it from fulfilling the request.

The cause of this can be anything, really! 

Let's imagine you are accessing a website using a Laravel PHP API for its back end. 

The thing throwing the 500 error could be something as simple as an errant `error_log` trying to log an array instead of a string – something completely unrelated to your request, but nonetheless an error that PHP would throw and kill the request you made to the server.

Usually something as trivial as that would get caught before deployment (hopefully), but this just goes to show that, as the user of a website or app, the error is truly out of your hands.

## How do you fix it?

As a user without access to the server, you really only have option:

### Notify the site owner that a 500 is being returned when you'd expect otherwise

If you fully expect that you should be able to access the resource in question, but you are seeing this error, it is wise to let the team behind the site know.

Try to give the developers / support team as much information about what you were attempting to do so they can quickly replicate the issue to track down the bug.

If you are feeling especially helpful, or curious, you may be able to hunt down more clues in the network tab of the developer tools for your browser. 

On Firefox you can open the network tab with the shortcut keys `ctrl + shift + E`. On Chrome, you can open the developer tools with `ctrl + shift + I` and then select the network tab. 

With this tab open, attempt your request again and look for the 500 return code in the network output. Sometimes you might see a slightly more detailed server response describing the problem you faced. You can give that information to the developers to speed up the resolution to the problem.

If you are the developer, then you need to hunt down the bug and fix it! It could be anything, so I can't tell you how to do that. But if you are new to development, I would recommend first looking in the server logs for clues if it's not already obvious what the issue is.

## Sit tight

Having reported the issue, you've done all you can reasonably do.

* are you wondering what the most frustrating error code to come across in the wild is? [418: I'm a teapot](https://en.wikipedia.org/wiki/Hyper_Text_Coffee_Pot_Control_Protocol). If you come across this as an actual error, it means the developer went to the effort of implementing this as the error response, but it's a joke and doesn't give you information. It happens.

If you promise to never return a 418 in response to a real client side error, then you are welcome to keep in touch with me on Twitter [@JacksonBates](https://twitter.com/jacksonbates).

