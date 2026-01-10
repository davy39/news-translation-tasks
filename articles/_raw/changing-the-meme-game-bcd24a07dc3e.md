---
title: 'The new Meme order: changing the game with simple browser caching'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-13T19:49:43.000Z'
originalURL: https://freecodecamp.org/news/changing-the-meme-game-bcd24a07dc3e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sa36HnySp33Inkm62q-Scw.png
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: memes
  slug: memes
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Philipp

  Even in 2018, not all humans have access to 3G internet and are trapped inside a
  memeingless world. It’s time to stop this madness.

  In case you are not familiar with the meme concept, a meme is typically an image
  associated with a specific...'
---

By Philipp

Even in 2018, not all humans have access to 3G internet and are trapped inside a memeingless world. It’s time to stop this madness.

In case you are not familiar with the **meme** concept, a meme is typically an image associated with a specific context or idea.

Adding different text to those images — memes — is mostly used as a way to ridicule human behaviour, or to describe situations. Memes are spread widely online, especially through social media and image platforms.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Nw3DnbmpuEBnbtP-gdqyfg.png)
_Your typical next door Meme_

### There is a problem

Each of these memes has been used millions of times to make millions of jokes. Right now, all search engines, social media, and image platforms load each of these images separately. This causes **megabytes** of traffic, and requires data capacity on your phone.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Bt-YmOk2Aa2F4Hbj1FaQIw.png)
_Search results for “Bad Luck Brian”_

### My idea

I came up with the idea to save the most used meme images once, and append the rest of the text later dynamically.

This works great for memes, since the images stay the same and only the text changes.

The huge advantage is the reduced data transfer. Ten to fifteen “normal” images can easily transfer 1MB of data. I can load 1000 memes and more with the same 1MB of data transfer, because palin text is much lighter than images.

So, for example, the second meme from this Medium article is saved as an image and is over **80kB** but could be also be saved as

1. **Image :** ”success_kid.jpg”

2. **Top Text :** ”Heavy night of drinking”

3. **Bottom Text:** ”Woke up with keys, wallet and phone”

This would require just **0.1kB** as long the “success_kid.jpg” image was cached once before. If the image is not in the browser cache, it would be downloaded once. It could then be repeatedly used forever without any further data transfer.

The user benefits from a huge decrease in loading time and data usage. With this system, it does not matter if your mobile provider throttled your bandwidth — you can still meme around like crazy. The system also saves storage space on your phone.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZMaYMU0jYu1hLypBslw_pA.png)
_Each “Type XHR” = 15 Memes, Document = Code for layout and functionality_

To load **100** memes, only **15kB** were transferred in total since the images are already “cached” (“Transferred” **0B**) and 15 posts require less than **1.5kB** of data. The website itself is less than **10kB**. I achieved this by:

1. **Not using** any plug-ins/libraries and writing native code.

2. **Not using** images to create the layout and high quality images in general.

3. Keeping everything **plain simple**.

Since the memes are so lightweight, it made sense to keep the layout and functionality lean as well so the website is compact and fast.

People around the world have problems loading webpages because it takes too much time to open them. The [average webpage is about 2.300kB](https://www.wired.com/2016/04/average-webpage-now-size-original-doom/), and imageboards or video platforms are often unreachable because the content is to big to download with a weak or throttled connection.

I hope that this cache system will help by providing an alternative which requires less data usage. It’s time to make the internet and people’s lives more memeingfull by making this piece of internet culture accessible to everybody at anytime.

The rest of the article is about the technical implementation and a bit about myself. If you simply want to take a look at the project go to **CacheMe.me** (Make sure to check out tools like the offline Memeviewer and many more by opening the Menu(☰) → Gadgets).

### Technical part

To demonstrate the idea, I created a little example. I used ten typical memes and, after that, endless memes with random generated numbers (ain’t nobody got time to generate infinity real examples).

**To turn this example into a real meme machine**, query a database and append the returned content. If you want to see full examples check out my [GitHub](https://github.com/Cachememe/Cachememes). The front end (HTML, CSS, JS, Kotlin and Swift) is going to be open source, anyway.

#### Front end

This article will **focus** on the web implementation of the concept. There is an app for Android but I will not go into any details in this article. If you want me to write about it, leave a comment.

**Html/CSS:** The `<d`iv> I use as a meme container needs to have the CSS pro`perty position:rel`ative; so the text will be on the image`, and text-align:`center to align the text in the center (who would have guessed).

```
/* CSS class for the top and bottom meme text */.text1, .text2 {   left: 0;   font-family: Impact,sans-serif /*sans-serif as fallback*/;   width: 100%;   color: white;   position: absolute;   z-index: 99;   pointer-events: none;   text-align: center;   -webkit-text-stroke: 1px #000 }
```

The text gets a `font-family: Impact; color: white; -webkit-text-stroke: 1px #000` to achieve the typical meme styled text. The`position:absolute` attribute, in combination with the meme container `position:relative`, is used to get the text on top of the image. By adding attributes like`z-index:99` and `pointer-events:none` I made the meme feel more like a usual image.

```
<!-- The Meme structure in its natural shape --><h2>title</h2><div style=”position: relative;text-align: center;”>  <span class=”text1">first text</span>  <img src=”image_url">  <span class=”text2">second text</span></div>
```

**JavaScript:** To get more/endless content, I call a function in this case with Ajax/XHR (so the site won’t reload). This sends a request to the server for more content. If the response is in HTML format, I append it directly like so:

```
function get_memes() {   var xhr = new XMLHttpRequest();   xhr.open('GET', "url");   xhr.onload = function () {     if (xhr.status === 200) {// if the response is already HTMLdocument.getElementsByTagName("body").[0].insertAdjacentHTML("beforeend", xhr.responseText)}   };xhr.send();};
```

If the `resposeText` is JSON formatted, I parse the response text first, then create HTML from the content within a `for-loop` like so:

```
...var meme collection = JSON.parse(xhr.responseText)for (var i = 0; i <= meme_collection.length; i++) {  var o = '<h2>title</h2><div style="position: relative;"><span class="text1">'+meme_collection[i]["text1"]+'</span><img src="'+meme_collection[i]["image"]+'"><span class="text2">'+meme_collection[i]["text2"]+'</span></div>'
```

```
  document.getElementsByTagName("body").[0].insertAdjacentHTML("beforeend", o)}
```

The best part: I don’t even have to write a function to cache the images, every web-browser does this by default. You can simply reuse the same image link and the ?magic is already happening.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pAmE_dqKdzDrjO6_deW2vg.png)

#### Backend

The effect of data savings is a result of the way the front end (HTML/XML) is structured — so the backend isn’t really relevant for the data saving effect. Basically, a server that returns HTML or JSON formatted data (top text, bottom text, image name) is all that is required.

For my project, I chose [**Django**](https://www.djangoproject.com) (a Python web framework). I also integrated some [**Golang**](https://golang.org). Django/Python takes care of the platform in general (Users, Content and HTML) while Golang jumps in to handle API requests and to serve JSON to the client. Both programming languages work with the same **PostgreSQL** database**.**

### $whoami

My name is Philipp, and last year I started to learn coding next to my studies. I always wanted to learn how to code, but was scared of code since I imagined it to be very abstract and complex. I was partly right. There is web, mobile, and desktop application development and each of them requires a different skill set. There are a ton of different languages, frameworks, and libraries out there, and everybody is recommending to learn something different.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZQ-nJEzv6ONWBlfNHFpMZw.png)
_Major topics in programming and how they are connected. From [StackOverflow Survey](https://insights.stackoverflow.com/survey/2018/#technology-how-technologies-are-connected" rel="noopener" target="_blank" title=")_

Luckily I came across [freeCodeCamp](https://www.freecodecamp.org), which was an awesome starting point to learn and get into coding. I could decide on my own when and where to learn and, most importantly, the clear course path kept me on track what to learn next. It always helped to see that other people had similar problems and I wasn’t the only one who struggled to solve “easy” algorithms.

The freeCodeCamp community was supportive enough to carry me through these first weeks/months of frustration, and guided me a way to start projects on my own. After finishing my front end certificate, I started to get into Python and after 6 months I was able to get a Full Stack Junior Position (part-time since I have to finish my studies) in a young company.

Thanks to the entire programming community. Without freeCodeCamp, StackOverflow, and GitHub, I wouldn’t have come so far. Also thanks to all my fellow memeing humans, your memes were there when no one else was.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HqjMpHNELDuu8UzEreH7kQ.png)
_**The new Meme order**_

To enjoy some cached Memes, and join the revolution, go to [CacheMe.me](https://www.cacheme.me) or download the [Android App](https://play.google.com/store/apps/details?id=com.herokuapp.meme_maschine.low_data)!

