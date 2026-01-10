---
title: 'How to start using Curl and why: a hands-on introduction'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-07T22:33:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-start-using-curl-and-why-a-hands-on-introduction-ea1c913caaaa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ikPF01FOkQQaDAH2IfA3LA.jpeg
tags:
- name: api
  slug: api
- name: Linux
  slug: linux
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Luciano Strika

  Whether it’s testing the output of an API before deploying it to production, or
  simply fetching a response from a website (for instance, to check it’s not down),
  Curl is practically omnipresent.

  As a Data Scientist I’ve had to use i...'
---

By Luciano Strika

Whether it’s testing the output of an API before deploying it to production, or simply fetching a response from a website (for instance, to check it’s not down), Curl is practically omnipresent.

As a Data Scientist I’ve had to use it from time to time. However, more often than not I ended up just replacing parameters from a copied and pasted curl command that went around my team’s Slack channel.

I decided I needed to understand this powerful tool better if I wanted to use it to its full potential, and now I’m here to share some of the most interesting things I found in this curl tutorial.

If you have any tips or tricks you’d like to add, please do so in the comments, as my understanding of this tool is still in its early stages.

### Curl: What is it good for?

Curl is a command-line tool that allows us to do HTTP requests from shell. It also covers many other protocols, like FTP, though they go beyond the scope of this tutorial.

Its name [stands for “Client URL”](https://en.wikipedia.org/wiki/CURL), and it was developed by Swedish developer Daniel Stenberg. It is an open source project, and its code can be found [here](https://github.com/curl/curl), in case you feel like contributing.

You can invoke it from your favorite terminal, and it usually comes pre-installed in Linux-based OS’s. Otherwise, it can normally be downloaded through _apt-get_ on Linux, and _brew_ on Mac.

### Calling a GET method

In its most basic form, a curl command will look like this:

```
curl http://www.dataden.tech
```

The default behavior for curl is to invoke an HTTP GET method on the given URL. This way, the program’s output for that command will be the whole HTTP response’s body (in this case, HTML) the site returns on a GET, which will be written as given on _stdout_.

If you wish to read through a response without leaving the shell, I’d recommend at least piping it into a _less_ command, to be able to easily scroll through the output.

Many times we’ll wish to direct the response’s contents into a file. This is done with the _-o_ argument, like this:

```
curl -o output.html www.dataden.tech
```

which is equivalent to:

```
curl www.dataden.tech > output.html
```

Optionally, you can specify the URL of the site you wish to call curl on with a _-s_ argument, like this:

```
curl -s http://www.dataden.tech
```

allowing you to change the order of your arguments.

You can also use _–next_ to specify more than one URL, though the official doc advises to instead call curl on each URL in a different command.

### Doing a POST to a URL

Sometimes you’ll want to test whether an API is working correctly, and usually that will require sending arguments to it.

We’ll usually do this through the POST method, passing some JSON with all the required parameters. There are many ways to do this with curl.

You can pass your arguments’ values like this:

```
curl --data "name=John&surname=Doe" http://www.dataden.tech
```

Or like a regular JSON:

```
curl --data '{"name":"John","surname":"Doe"}' \http://www.dataden.tech
```

Using _–data_ is equivalent to using _-d,_ and both will make the method change to POST automatically. However, we can also use the _-X_ flag (_–request_) to specify which method we want to invoke:

```
curl -X "POST" \-d "name=John&surname=Doe" http://www.example.com
```

### Fetching the site’s headers

Sometimes we just need to quickly see if the site’s still up, without really wanting to load the whole, potentially heavy, response. Other times, the headers store important configurations.

Those two use cases are also addressed by curl. We can use the _–include_ (_-i_) parameter to include the headers, and _–head_ (_-I_ -that’s capital ‘i’-) to include only the headers (calling the HEAD method).

### Setting your user-agent value

Now that I’ve covered the basics, let me walk you through some of the coolest things I’ve found we can do with curl.

The _user-agent_ argument lets you specify which device and browser versions you are using, in case that makes the site render differently.   
With this, you could see the mobile version of a site from your laptop, or vice versa.

From a security standpoint, this probably raises some issues. I didn’t know how easy it is to pretend to be using a different device (without even using a virtual machine) until now, and working in Fraud Prevention I can see why this could be a problem.

With that said, as long as you are using this for good, this is an awesome way of seeing what a website looks like from a tablet, a mobile device or a laptop, to name a few.

Here’s an example, straight from the official documentation (though lists of user-agents are readily available online).

```
curl --user-agent "Mozilla/4.73 [en] (X11; U; Linux 2.2.15 i686)" www.example.com
```

### Timing a connection with Curl

Another reason I started learning more about curl was that I wanted to see how long exactly it took for my website to respond.

Though the basic documentation doesn’t cover it, a bit of googling uncovered this command, which I’ve found very useful:

```
curl -w "%{time_total}\n" -o /dev/null -s www.example.com
```

This will simply output the total time it took to fetch the response from the given domain.

More generally, the _-w (–write-out)_ argument takes a special formatting string, and fills in reserved keywords with different properties of the response, in a formatted way. All keywords, and their respective values, are available in the [command’s man page](https://curl.haxx.se/docs/manpage.html).

### Further reading

Here are a few links you may find interesting, in case you wish to learn more about this broad subject:

* [List of User-Agents](https://developers.whatismybrowser.com/useragents/explore/) A compilation of user-agent arguments for different devices and browsers.
* Curl’s [official documentation](https://curl.haxx.se/docs/httpscripting.html).
* Curl’s [manpage](https://curl.haxx.se/docs/manpage.html).

### To conclude

I hope you’ve found this introduction useful, and you leave this tutorial knowing at least the basics of this convenient command.

As I said before, I’m still learning as well, and will appreciate any other interesting bits of knowledge about the program’s use. The same goes for any feedback on what I’ve written so far.

If I’ve made any mistakes, or there’s any part you think I could have worded more clearly, please let me know.

I hope I’ll see you again soon, happy coding!

_Follow me on [Medium](http://www.medium.com/@strikingloo) and [Twitter](http://www.twitter.com/strikingloo) to keep up to date with my tutorials, tips and articles. Consider sharing this article with a web developer friend if you liked it (or as a passive aggressive way of telling them to learn curl)._

_Originally published at [www.dataden.tech](http://www.dataden.tech/programming/how-start-using-curl/) on October 7, 2018._

