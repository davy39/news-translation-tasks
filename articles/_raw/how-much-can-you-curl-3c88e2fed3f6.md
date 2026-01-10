---
title: How much can you cURL? A quick and easy intro to a useful tool.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-19T01:36:06.000Z'
originalURL: https://freecodecamp.org/news/how-much-can-you-curl-3c88e2fed3f6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tpMS_RxArawIV5OGqtTOHg.jpeg
tags:
- name: api
  slug: api
- name: command line
  slug: command-line
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Miguel Bustamante

  On a good day I can flex a 20 lb weight…twice. Probably. But that’s not the type
  of curling we’re talking about!

  Curl (or cURL), on the other hand, is a small but powerful tool for transferring
  files and data over URLs. On a smal...'
---

By Miguel Bustamante

On a good day I can flex a 20 lb weight…twice. Probably. But that’s not the type of curling we’re talking about!

Curl (or cURL), on the other hand, is a small but powerful tool for transferring files and data over URLs. On a smaller scale, it’s great for testing REST APIs. And, though most web developers might opt to use other tools such as Google’s [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en), cURL is done in the command line and can leave you feeling like a true computer hack with David Lightman-like skills (for you “War Games” fans).

CURL stands for “client” and “URL”, since it is a program run on the client side that makes HTTP requests to URL’s. Since it’s open source, you can download it [here](https://curl.haxx.se/). Or if you have [Gitbash](https://git-scm.com/downloads) already installed on your machine, it’s automatically included.

For the purposes of this quick intro, we’ll need a server that’ll allow us to make requests, and it seems [JSON Placeholder](https://jsonplaceholder.typicode.com/) fits our needs nicely. It is a fake REST API that, even though our requests won’t actually change the server’s database, will still give us the appropriate response. So go ahead and crack open that console and let’s get hacking!

### **Get**

To start, we’ll try a simple HTTP “get” request. Scroll down to the “Resources” section in JSON placeholder and let’s take a look at the types of objects we can make a request on.

![Image](https://cdn-media-1.freecodecamp.org/images/kCyy9EJv0wgDBRMWbcAqFbKHNZF8-Ux9u3z5)
_Objects to be requested_

Nice! We can call these objects by adding “/”, then the object we want in the URL. The number on the right of the row tells us how many items we’ll get back with this request. For starters, let’s request some users. Type the following line into the console:

```
curl https://jsonplaceholder.typicode.com/users
```

You should see all ten users we were promised as JSON objects. But maybe I just want the fifth user. We’ll add “/5” after the URL to get the user with the I.D. of 5.

```
curl https://jsonplaceholder.typicode.com/users/5
```

We see the JSON object for the fifth user. Great, let’s try to post a user to the server.

### **Post**

“Post”- ing is the process of submitting data to the server and having it be saved in the database. To do this with cURL let’s look at its options. Type:

```
curl --help
```

and you should get a bunch of cool options we can use in the terminal:

![Image](https://cdn-media-1.freecodecamp.org/images/mKtjAzBrGPgeLjJRjW7fExC3SgYeUK2s8JNB)
_Options for cURL_

For our purposes, it looks like the “-d” or “- -data” option would work nicely. If we look back at the homepage of the placeholder, in the “Routes” section, it tells us we could make a post request to “[https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts)”. With this information, we’ll post our own object through the console:

```
curl -d "title=Greatest Post Ever Written&body=Body of the Greatest post ever written" https://jsonplaceholder.typicode.com/posts
```

Now you’ll see the post being “created” in the db, and it has an I.D. of 101.

![Image](https://cdn-media-1.freecodecamp.org/images/-zEjFQuC3q32sqCBzwxYpLwvlpsLatdXsf7h)

### **Update**

Sometimes we need to change objects in the db. We can only change things already saved in the database, and since this is a fake REST API, our post wasn’t actually saved. So lets update a post that exists. How about the 56th one. Type:

```
curl https://jsonplaceholder.typicode.com/posts/56
```

And you’ll see:

![Image](https://cdn-media-1.freecodecamp.org/images/z1-dbP08TUfRBpWmLQgvybxekbAQiBCJ-T8S)
_Post 56_

It’s saved with some funky [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum) text that we should probably change to something intelligible. We are going to need a few other options with our command here. First, we’ll need to tell cURL that it’s a “put” request. So as we look through our “- -help” option, it seems we could use “-X” to tell cURL we want to use a “PUT” command.

Then we still want to use the “-d” option for the new data we intend to use. Let’s piece it all together. Type:

```
curl -X PUT -d "title=This is a new title" https://jsonplaceholder.typicode.com/posts/56
```

And just like that, we have changed the title of the post with the I.D. of 56 to what we wanted.

![Image](https://cdn-media-1.freecodecamp.org/images/4eOxfEfuubfhDr2FQrC3zu29M4Z8hwLFJonG)
_New title for post 56_

### **DELETE**

And now we come to the delete. Ahh, the delete. If all else fails, destroy it all! We are going to see some of the same code as we saw in the PUT command, but all we need is to give cURL a DELETE request and the URL to the post we are to delete.

```
curl -X DELETE https://jsonplaceholder.typicode.com/posts/56
```

Notice that you get nothing back in return but a newline. Maybe on some consoles you’ll see and empty hash(“{}”). This indicates that there is nothing to return because it was deleted.

### Wrapping up

We only touched on some cURL commands at a very superficial level. It is a neat tool that can be helpful when working on fully functioning API integration in your app. I would suggest looking at the [manual](https://curl.haxx.se/docs/manual.html) for further reading and playing around with the different options to see what may fit your needs.

