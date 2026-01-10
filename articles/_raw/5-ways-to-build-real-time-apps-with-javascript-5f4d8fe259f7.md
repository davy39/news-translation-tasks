---
title: 5 ways to build real-time apps with JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-14T15:24:05.000Z'
originalURL: https://freecodecamp.org/news/5-ways-to-build-real-time-apps-with-javascript-5f4d8fe259f7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9ldkwChSUEeQGlbVzcJSVg.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Burke Holland

  There was a point in time where we didn’t expect too much from web pages. Which
  reminds me, the Space Jam movie website is still on the internet in its original
  form. And it uses a frameset. Not iFrames. FRAMES.

  Space Jam_SPACE JAM, ...'
---

By Burke Holland

There was a point in time where we didn’t expect too much from web pages. Which reminds me, the Space Jam movie website is still on the internet in its original form. And it uses a [frameset](https://caniuse.com/#search=frameset). Not iFrames. **FRAMES**.

[**Space Jam**](https://www.warnerbros.com/archive/spacejam/movie/jam.htm)  
[_SPACE JAM, characters, names, and all related indicia are trademarks of Warner Bros. © 1996_www.warnerbros.com](https://www.warnerbros.com/archive/spacejam/movie/jam.htm)

Warner Bros has some gently used copies of Dreamweaver MX.

That was 1996. This is 2019. Times have changed and users expect a lot more out of websites. They don’t just expect them to look good, they expect them to be full on apps, and that includes being real-time.

#### Real-time Applications

Real-time apps are those that react to changes anywhere in a connected application’s system— not just those made by the current user.

The canonical example of real-time is a messaging application. Like when you send a group of friends a text message about getting together for wings on Friday. Then update everyone minute by minute on your progress getting from work to the bar. Thanks, Trevor. Now we’re all trapped in a notification hell that we didn’t sign up for. I JUST WANTED SOME WINGS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*A0RYVB-7SF0sqpvQdVLWXg.png)
_What’s that, Trevor? You’re only 10 minutes away now? REJOICE. Looking forward to single digits._

When it comes to the web, there are several different patterns, technologies, libraries and services that you can use to get the real-time functionality that is usually reserved for native applications. I recently sat down with Anthony Chu who gave me 5 ways that you can build real-time apps in JavaScript.

[**Anthony Chu #MSIgniteTheTour (@nthonyChu) | Twitter**](https://twitter.com/nthonychu)  
[_The latest Tweets from Anthony Chu #MSIgniteTheTour (@nthonyChu). Cloud Advocate @Microsoft. Azure, ASP .NET, Node.js…_twitter.com](https://twitter.com/nthonychu)

#### 1. Long-Polling

This is when the application requests updates from the server on a schedule. The app is “polling” the server.

This is the net equivalent of kids asking “are we there yet?” every five minutes. Does it look like we’re there yet, kid? Ask me one more time and I swear to you that I will throw this copy of the “The Bee Movie” in a ditch and you can stare out the window at grass like we did when I was a kid.

Long-polling can be implemented manually with any JavaScript HTTP library, such as jQuery or Axios. I have never actually implemented this myself. When doing some research for this article, I discovered that the best way to do this is to use a recursive function with `setTimeout`. This is because using `setInterval` does not account for requests that fail or timeout. You could end up with a bunch of ajax calls that are all processed out of order.

Here is an example from the very nice article over on [Tech Octave](https://techoctave.com/c7/posts/60-simple-long-polling-example-with-javascript-and-jquery).

```
(function poll(){
   setTimeout(function(){
      $.ajax({ url: "server", success: function(data){
        //Update your dashboard gauge
        salesGauge.setValue(data.value);
        //Setup the next poll recursively
        poll();
      }, dataType: "json"});
  }, 30000);
})();
```

There are also libraries like pollymer (not to be confused with Polymer) that are specifically for long-polling. Get it? “poll”ymer? Cause it polls? Is this thing on?

[**fanout/pollymer**](https://github.com/fanout/pollymer)  
[_General-purpose AJAX/long-polling library. Contribute to fanout/pollymer development by creating an account on GitHub._github.com](https://github.com/fanout/pollymer)

Long-polling is good because it works in every browser; even the super old ones. It’s bad because it’s super inefficient and not exactly “real-time”. It also has some weird edge cases (like request failures) that you have to program around as we’ve already seen with `setInterval`.

A better alternative to long-polling is Server-Sent Events or SSE.

#### 2. Server-Sent Events

Server-Sent Events (SSE) is similar to long-polling in so much as the client asks the server for information. The big difference is that with SSE, the server just holds the connection open. When an event occurs and there is information to send to the client, the server sends an event to the client.

[**Server-sent events**](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)  
[_Traditionally, a web page has to send a request to the server to receive new data; that is, the page requests data from…_developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)

Back to our “road trip from hell” analogy, this would be like if the kid says “Are we there yet?”, and then waited patiently for your response. Four sublime hours of silence later you arrive at the destination, turn around, and say “yes”. That’s the most unrealistic scenario I have ever come up with in my life.

SSE is part of the browser `EventSource` API. Note that according to [caniuse.com](https://caniuse.com/#search=EventSource), neither IE 11 nor Edge support SSE. That makes it kind of a tough technology to pick, however interesting it is.

The good news is that pretty much every browser supports Web Sockets.

#### 3. Web Sockets

Web Sockets is a technology that facilitates a true two-way communication channel between a client and a server. Unlike Server-Sent Events, which is only communication from server to a client, Web Sockets can be used to communicate in both directions.

Web Sockets are, uh, kinda verbose. They aren’t really the kind of API’s you wanna build apps with. Kind of like you _could_ make an HTTP request with the [XHR object](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest), but OMG NO. I Googled “PHP Web Socket Sample” and found this doozy from the PHP docs. I zoomed all the way out in Chrome and barely got everything in a single screenshot.

![Image](https://cdn-media-1.freecodecamp.org/images/1*b8NjhSqlK84BiLsFDlfRkA.png)

And that’s ONLY the server portion. You still gotta wire up the browser.

So….that’s a **no** for me.

Fortunately, there are plenty of libraries that abstract Web Sockets even further so you don’t have to write any of this. One of those libraries is called “SignalR”.

#### 4. SignalR

SignalR is a library that implements Web Sockets both in JavaScript AND .NET. On the server, you create what is known as a “hub” in SignalR. This hub sends and receives messages from clients.

Clients then connect to the hub (using the SignalR JavaScript library) and respond to events from the hub, or send their own events into the hub.

SignalR also falls back to long-polling whenever Web Sockets is unavailable. Although that’s not super likely unless you’re using IE 9 or lower.

Here is an example of setting up SignalR on the server…

```
using System;
using System.Web;
using Microsoft.AspNet.SignalR;
namespace SignalRChat
{
    public class ChatHub : Hub
    {
        public void Send(string name, string message)
        {
            // Call the broadcastMessage method to update clients.
            Clients.All.broadcastMessage(name, message);
        }
    }
}
```

OK, ok. I know this is not an apples to apples comparison with the PHP example from above, but I’m trying to make a point here. Just go with it. Do it for me. I’m having a rough morning.

So SignalR makes it more fun to program Web Sockets, but you know what’s even more fun than programming them? Not programming them.

#### 5. Azure SignalR

Often, when we want to set up real-time applications, building out a Web Socket server isn’t exactly a value-added activity. We do it, but only because we have to to get the real-time. We’d prefer that it “just worked”.

Azure SignalR is exactly that. It is a SignalR Hub that you can consume on demand as a service. That means that you only have to send and respond to events — which is what you’re after in the first place.

[**What is Azure SignalR**](https://docs.microsoft.com/en-us/azure/azure-signalr/signalr-overview?WT.mc_id=medium-blog-buhollan)  
[_An overview of the Azure SignalR service._docs.microsoft.com](https://docs.microsoft.com/en-us/azure/azure-signalr/signalr-overview?WT.mc_id=medium-blog-buhollan)

You create the SignalR Hub in Azure as an Azure Service, and then you just connect to it from the client and send/receive messages.

#### And now you know….

Check out the interview below with Anthony. We shot this one in Vegas while we were both at a conference and had a good time with a wig that I bought at Party City. Best 8$ I ever spent.

%[https://youtu.be/3qucTcr3pGA?list=PLlrxD0HtieHgugDxYBujMFnvSveH4fgWN]


