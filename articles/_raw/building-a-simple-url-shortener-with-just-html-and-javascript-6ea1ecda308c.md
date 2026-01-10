---
title: How to build a simple URL shortener with just HTML and JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-11T06:15:10.000Z'
originalURL: https://freecodecamp.org/news/building-a-simple-url-shortener-with-just-html-and-javascript-6ea1ecda308c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*8L64PM8OQXszS_rH.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Palash Bauri

  You might have used a URL shortener before, such as bit.ly, goo.gl. They are useful
  for shortening long URLs so that you can easily share them with your friends, family
  or co-workers.

  You might be wondering how these things work. To u...'
---

By Palash Bauri

You might have used a URL shortener before, such as [bit.ly](https://bit.ly), [goo.gl](https://goo.gl). They are useful for shortening long URLs so that you can easily share them with your friends, family or co-workers.

You might be wondering how these things work. To understand how, we need to take a closer look at an URL shortener — so we’ll be building a simple one! With that task, we’ll be learning some new things as well as understanding how a URL shortener works.

Today, we’ll be building a simple URL shortener which does not need a database system to host it. Instead, we’ll use [jsonstore.io](https://jsonstore.io). I’ll be assuming that you already know some basic HTML & JavaScript.

So without further ado, let’s start building. . .

### Start with the HTML

We’ll need only a text input box, a button, and a script tag to create our URL shortener.

First create an HTML file called `index.html`, as there is only a need for those two elements (a text input box and a button).

So let’s start adding our three main elements:

```
<html> <body> <input type=”url” id=”urlinput”> <button onclick=”shorturl()”>Short The URL</button> <script src=”main.js”></script> </body></html>
```

As I showed you in the above code, I’ve created a simple HTML file. Inside the body tags, there are only three elements: an `input`, a `button` and a `script`.

The first element is `input` where we will type/paste our long URL. I gave it an id name `urlinput` so it would be easy to access in the JavaScript.

The next element is a `button`. When we click this button, our long URL will be shortened as it has an `onclick` function which will be executed when we click the button. And inside the `shorturl()` function there will be commands necessary to shorten the URL.

At the end we have a `script` called `main.js` where all our main JavaScript code will be. The above-mentioned `shorturl()` function will be also there.

So, for now, our HTML part is complete. Let’s start writing some JavaScript

### Start writing some JavaScript

As we showed above, we’ll need some JavaScript to create our URL shortener.

**Step 0:** as I mentioned, we’ll be using **jsonstore.io** to store information about our long URL. We will need a **jsonstore.io** **endpoint** URL to store data, so you can visit [jsonstore.io](https://jsonstore.io) where you’ll see something like below:

![Image](https://cdn-media-1.freecodecamp.org/images/Z7nKP7sEB4Lu2PGz64A9-WkBvLlitPw3z64e)

Under the text _This Is Your Endpoint_, you can see a text box with a long URL such as this:

`[https://www.jsonstore.io/8ba4fd855086288421f770482e372ccb5a05d906269a34da5884f39eed0418a1](https://www.jsonstore.io/8ba4fd855086288421f770482e372ccb5a05d906269a34da5884f39eed0418a1)`

Click the purple _COPY_ button.

So now, let’s start writing some JavaScript . . .

Create a JavaScript file called `main.js` and start following the below steps.

First, we must keep the copied link as a variable:

```
var endpoint = "https://www.jsonstore.io/8ba4fd855086288421f770482e372ccb5a05d906269a34da5884f39eed0418a1";
```

Then we need to generate some random string so that we can create a link between the short URL and the long URL.

> _Assume that we have a random URL `abcd`, our simple URL shortener is hosted on [https://shortner.com](https://shortner.com) and we have shortened the URL [https://google.com](https://google.com) with that random URL. So whenever we go to [https://shortner.com/#abcd](https://shortner.com/#abcd) we will be redirected to [https://google.com](https://google.com)_

So, now well create a function called `getrandom()`:

```
function getrandom(){    var random_string = Math.random().toString(32).substring(2, 5) + Math.random().toString(32).substring(2, 5);    return random_string()}
```

Don’t worry, I’ll help you understand the above code.

First, we initiated a function called `getrandom`. Then we initialized a variable called `random_string` and gave it a value.

`Math` is a built-in Javascript object which allows us to perform mathematical tasks on numbers. First we called the `random` function from `Math` , `Math.random()` returns a random number between 0 (inclusive), and 1 (exclusive).

> _You Can Learn More About `Math` object from [here](https://www.w3schools.com/js/js_math.asp)._

Then we transform the returned number to a string using `toString()` and we give it an argument of 32 so that we get a proper string not a binary, hexadecimal or octal.

Then we use `substring(2,5)` as well to slice the string and maintain the size of the string. Then again we follow the same procedure to get another chunk of a random string, and finally we add both chunks of the string using `+`.

And don’t forget to add a `return` statement returning our random string.

> _Remember, this is not the only way to generate random strings. You can also use the method mentioned below to achieve the goal:_

```
function getrandom() {    var text = “”;    var possible = “ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789”;   
```

```
    for (var i = 0; i < 5; i++)        text += possible.charAt(Math.floor(Math.random() * possible.length));    return text;}
```

Now return to `index.html` and add JQuery because it will be easier to achieve our goals if we use JQuery. Add it at the end of the body tag but before the `main.js` script tag.

Now again return to `main.js`.

Let’s create a function called `geturl` which will take the value from the input box, verify it, and return the value:

```
function geturl(){     var url = document.getElementById(“urlinput”).value;     var protocol_ok = url.startsWith(“http://”) || url.startsWith(“https://”) || url.startsWith(“ftp://”);     if(!protocol_ok){         newurl = “http://”+url;         return newurl;     }else{         return url;     }
```

In the `geturl` function, we first store the value of the input box in the `url` variable. Then we check if the URL protocols are OK or not. If the protocol doesn’t start with `http://` , `https://` or `ftp://` we add `http://` at the beginning of the URL then return the URL.

> Actually this isn’t a safe method. You should be using a regex to validate your URLs! But I want to keep this article easy to understand.

Now we will need another function to change the hash in the location bar, so let’s create it:

```
function genhash(){    if (window.location.hash == “”){        window.location.hash = getrandom();    }}
```

At first, we check if the hash location is empty. If it’s empty, we than add a random hash to the location bar.

> _Example: if our URL is [https://example.com/#abcd](https://example.com/#abcd) then the value of `window.location.hash` will be `#abcd`._

Next, we’ll work on our main function `shorturl()` , so let’s go…

```
function shorturl(){    var longurl = geturl();    genhash();    send_request(longurl);}
```

First we store the long URL in the `longurl` variable. Then we add a random hash to the location bar so that we can use the URL as the short URL. Next we call the `send_request()` with an argument `longurl`. In this function we send a JSON request to **jsonstore** to store the long URL with a link to short URL. So now let’s create the `send_request()` function.

```
function send_request(url) {    this.url = url;    $.ajax({        ‘url’: endpoint + “/” + window.location.hash.substr(1),        ‘type’: ‘POST’,        ‘data’: JSON.stringify(this.url),        ‘dataType’: ‘json’,        ‘contentType’: ‘application/json; charset=utf-8’    })}
```

Here we use JQuery to send the JSON request to **endpoint+”/” + our random string hash from the location bar.** As an example:

`[https://www.jsonstore.io/8ba4fd855086288421f770482e372ccb5a05d906269a34da5884f39eed0418a1/abcd](https://www.jsonstore.io/8ba4fd855086288421f770482e372ccb5a05d906269a34da5884f39eed0418a1/abcd)`

So whenever we send a get request to the above-mentioned URL, we’ll get the long URL as `data`.

**Important**: add the `send_request()` function before the `shorturl()` function, otherwise it will not work.

> _To know more about JQuery’s Ajax function, go [HERE](https://www.w3schools.com/jquery/ajax_ajax.asp). To know more about JSON, go [HERE](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)._

Now we will use the code to GET the long URL linked to the short URL entered in the address bar:

```
var hashh = window.location.hash.substr(1)
```

```
if (window.location.hash != "") {    $.getJSON(endpoint + "/" + hashh, function (data) {        data = data["result"];
```

```
if (data != null) {            window.location.href = data;        }
```

```
});
```

Then the above-mentioned code will be executed whenever we put the short URL in the address bar (eg. [https://shorturl.com/#abcd](https://shorturl.com/#abcd) ).

First, we store the hash value from the URL in the `hashh` variable.

> _Example: if our short URL is [https://shorted.com/#abcd](https://shorted.com/#abcd) , the value of the hash will be **#abcd.**_

Then we check if the hash location is empty or not. If it’s not empty we send a get request to the address, `endpoint` + `hashh`.

> _Example :_`[https://www.jsonstore.io/8ba4fd855086288421f770482e372ccb5a05d906269a34da5884f39eed0418a1/abcd](https://www.jsonstore.io/8ba4fd855086288421f770482e372ccb5a05d906269a34da5884f39eed0418a1/abcd)`

And as usual, if everything is okay we will get the long URL from the data which is JSON array data, and from that we extract the result with `data["result"]`.

> _The value of data will be similar to this `{"result":longurl,"ok":true}` , where the long URL is the URL you shortened._

Our URL shortener is almost complete! Copy-paste a long URL in the input box then click the **Shorten The URL** button! Copy the link from the address bar — it’s your short URL!

![Image](https://cdn-media-1.freecodecamp.org/images/KdWpDkClj9ekuuHM47166AbVxkxAT0GlFXvN)

### Some Useful Tricks

* We can add a function to automatically copy the short URL when a user clicks the **Shorten The URL** button using libraries like [SimpleCopy](https://github.com/kyle-rb/simplecopy), or [ClipboardJS](https://clipboardjs.com/) — they’ll copy the short URL which is currently in the location bar.
* If using SimpleCopy, we can add `simplecopy(window.location.href);` at the end of the `shorturl()` function to copy the short URL whenever it shortens a URL.
* This simple URL shortener relies on third-party libs such as **jsonstore** so it would not be a good idea to shorten some confidential long URL with it.
* You can host the whole project in Github/Gitlab pages and set up a simple CNAME. That’s it — your brand new personal URL shortener is ready! You can use any static site hosting service to host your URL shortener.
* You can find the full source code of the project on [GITHUB](https://github.com/bauripalash/simpleurlshortener)

That’s it for today! This is my first technical guide, so I apologize for any mistakes.

If you find any problems or mistakes, let me know in the comments below ?.

Or ping ee on [Facebook](http://fb.me/bauripalash) or [Twitter!](https://twitter.com/bauripalash)

Peace!

