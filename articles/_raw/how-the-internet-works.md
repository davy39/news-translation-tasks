---
title: How HTTP Works and Why it's Important – Explained in Plain English
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-31T21:14:32.000Z'
originalURL: https://freecodecamp.org/news/how-the-internet-works
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c98f0740569d1a4ca1ced.jpg
tags:
- name: communication
  slug: communication
- name: http
  slug: http
- name: internet
  slug: internet
seo_title: null
seo_desc: "By Fredrik Strand Oseberg\nImagine that your house is a huge computer.\
  \ Instead of Goodison Street or 4th Avenue, your home address consists of numbers.\
  \ For example: 112.231.31.20. \nLike in a futuristic movie, your city consists largely\
  \ of high-tech ro..."
---

By Fredrik Strand Oseberg

Imagine that your house is a huge computer. Instead of Goodison Street or 4th Avenue, your home address consists of numbers. For example: 112.231.31.20. 

Like in a futuristic movie, your city consists largely of high-tech robots in the sky going from house to house, delivering their messages and carrying responses.

Got the picture?

## An overview of how the internet works

Slightly simplified, this is what happens when you type a web address into your browser:

* It finds the address of the “house” where you want to send the request
* It sends the request using the robotic postman
* It patiently waits for the response from the robotic postman

Now, all of this is abstracted away from you as the end user. You type the web address in the browser, and the web page appears before your eyes - like magic. 

Like any sufficiently advanced technology, the average user would not be able to use the internet without these abstractions.

Most of the time, you don’t need to to worry about how something works – you just need to know that it works.

But for certain subjects, diving a little bit deeper into the nuts and bolts is helpful, or just scratches that itch of curiosity.

You won’t become an expert in the technical details of the internet by reading this article – that will take a lot more time and effort – but you will gain a birds eye view and a better understanding. 

If you do find that you want to learn more, [I have a playlist on YouTube that goes more in depth.](https://www.youtube.com/playlist?list=PL_kr51suci7XVVw4SJLZ0QQBAsL2K8Opy)

## The messaging system

From the metaphor at the beginning of this article, we learned that the internet consists of messages being passed around. For the most part, these messages are sent using what is known as the HTTP protocol.

Protocol. That’s a scary word. That’s an eyes glaze over and close your browser type of word. So let’s break it down into easier terms.

> A protocol is just a fancy word for agreement.

Let’s make it clearer with an analogy. 

Say you and your best friend leave each other secret messages. When you find a piece of paper on your doorstep with the word “ballfoot”, you know that your friend wants to meet you for football tonight at 20:00. 

You know this because you agreed that the word “ballfoot” on a piece of paper delivered to your house represents an invitation to play.

Now, a problem arises when you start leaving your other friends the note “ballfoot” without telling them the secret meaning. They wouldn’t know what to do with the information. 

They would find the note on their doorstep, scratch their head for a minute, then carry on playing Fortnite in their living room. And you and your one other friend would pass the ball between you. Back and forth. Back and forth. Until the boredom becomes unbearable and you both go home.

But it doesn’t have to be that way. What if you tell your friends what the meaning of “ballfoot” is? Now every one of your friends would know and share the agreement that the note with the world “ballfoot” means to show up and play football at the local court at 20:00. 

Success.

This is – in essence – what the HTTP protocol represents. We've agreed that if we send a message in a particular way, the server will understand it, and give a response in return.

### The structure of the message

Let’s take a closer look at the HTTP agreement. It consists of requests and responses. Simply put, you ask for something and then get an answer back from something known as a server. 

Before we go on, let’s amend our metaphor from the beginning to better understand HTTP request/response cycles. 

Remember the robots going from house to house carrying messages? Now imagine that all of those robots belong to someone.

You have your own personal robot, and you can ask it to go to any address (IP address) with messages. Once your robot arrives with your message at the given address, it will enter and boldly proclaim that it has a message to deliver. Then it will speak the message.

For the sake of the metaphor, imagine that the doors to the houses (servers) are like the entrance to the mines of Moria in Lord of the Rings. Only if the words are spoken correctly will the door open and let you in.

In this case, only if your robots speak the message in a specific manner will they receive a response message to take back to you. 

This is the HTTP protocol at work. There is a predefined set of rules guiding what the request and response messages looks like.

At this point you might be wondering where these messages are coming from. You certainly don’t write them yourself when you enter the website address into your web browser. 

Well, it’s all handled for you automatically by the browser. When you write in an address, your browser takes care of composing the HTTP request message for you and sends it off to the server. The HTTP Request message looks like this:

```
GET / HTTP/1.1
Host: google.com
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) 
Version/11.0 Mobile/15A372 Safari/604.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,
image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
...etc
```

It looks scary, right?

Good thing the browser does this for us. 

Let’s take a closer look at just the first line: `GET / HTTP/1.1`. This line makes your robot go up to Google's house and say, "Can I please receive whatever you have at the root of your site?" (This means that we want to retrieve what is at www.google.com, not www.google.com/home.)

So now we have delivered our message to Google's house (the server) in the correct manner. The doors light up and swing open. 

Inside you see another robot. Behind it is a series of lockboxes marked with text like `GET / HTTP/1.1` and `GET /search HTTP/1.1`. If your request matches one of those lockboxes, the robot will unlock it and give your robot the contents, which will prompt it to return to you quickly with the response.

### The response

The response you get back will look something like this:

```text
HTTP/1.1 200 OK
Date: Mon, 27 Jul 2009 12:28:53 GMT
Server: Apache/2.2.14 (Win32)
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
Content-Length: 88
Content-Type: text/html
Connection: Closed
```

Now, you will never see this response unless you really want to inspect it in your browser's developer tools. But nevertheless, you receive it. 

What happens next depends on what kind of response you receive, and what was inside the server's lockbox.

In many cases, what you receive in return is an HTML document. HTML represents the structure of webpages and defines what the browser should display. 

If you go to www.google.com, you will receive an HTML file in return that defines how the google.com site will be displayed in your browser.

If you have some time, this 11 minute video goes deeper into HTTP requests and responses:

%[https://www.youtube.com/watch?v=8QfaJudvpmo&list=PL_kr51suci7XVVw4SJLZ0QQBAsL2K8Opy&index=3]

## Conclusion

In this article we’ve reviewed how the internet works, and how we use HTTP to communicate on the internet. 

We learned that the HTTP protocol is used to communicate between browsers and servers on the internet and consists of a generally agreed upon standard for how requests are sent and received. 

We also explored the importance of having such standards of communication and the benefits of having a generally agreed upon standard.

There are many more facets to understanding how the internet works and what kinds of responses you can receive.

If you have a moment, this 18 minute video teaching your how to build a web server will review a lot of the topics covered in this article, and go over some new ones:

%[https://www.youtube.com/watch?v=R5uwuG1wPR8&list=PL_kr51suci7XVVw4SJLZ0QQBAsL2K8Opy&index=6]

Now you should have a general understanding of how communication on the internet works. 

If you think someone else could benefit from this article, please spread the word. And if you want to know when I post more content, you can [subscribe to my YouTube channel](https://www.youtube.com/channel/UCZTeUahnA2GMoo_YpTBFo9A), or you can follow me [@foseberg on Twitter](https://twitter.com/foseberg).

