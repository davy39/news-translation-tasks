---
title: How I Reverse Engineered A Chrome Extension To Write My Own Flask App
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-02T17:05:34.000Z'
originalURL: https://freecodecamp.org/news/how-i-reverse-engineered-a-chrome-extension-to-write-my-own-flask-app-d77f36421106
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uOlxCoXq1faNmKA-3ie2Bg.jpeg
tags:
- name: Google Chrome
  slug: chrome
- name: chrome extension
  slug: chrome-extension
- name: JavaScript
  slug: javascript
- name: reverse engineering
  slug: reverse-engineering
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Tushar Agrawal


  Basically, if I have no intention of using a service then I won’t bother reverse-engineering
  it. — Jon Lech Johansen


  As evident from my bio, I am crazy about music and pretty much anything related
  to it. And I believe that music v...'
---

By Tushar Agrawal

> Basically, if I have no intention of using a service then I won’t bother reverse-engineering it. — _Jon Lech Johansen_

As evident from my bio, I am crazy about music and pretty much anything related to it. And I believe that music videos, if well-directed, are possibly the best way to feel the inherent soul of music. 

So, it all began with me watching the music video of a song “**Heavydirtysoul**” by **Twenty One Pilots**. The music video was so dope I didn’t even care for the lyrics. It was only after I listened to it a few times, I realized that I didn’t get much of the lyrics except the chorus part. 

This is something that is an actual problem for many ESL (English as a Second Language) speakers. You can’t enjoy a song to its fullest if you don’t get the lyrics. 

It was then that I thought of something: what if I could play the lyrics of a song alongside the music videos (much like subtitles)? It would be awesome if I could create subtitle files for my music videos and then play it on my video player!

## Initial Approach and finding Musixmatch

I then began a comprehensive search for sites or APIs that could provide me the lyrics for a song. And as expected, I found a dozen sites that provided the lyrics. Cool… isn’t it? 

Nah. Because, what I really needed was timed lyrics, much like a subtitle for a movie. I wanted the lyrics text to **sync** with the current video frame on the screen. After much searching, I was unable to find any such service.

It was only after a week someone told me to use **Musixmatch**, a chrome extension that embedded lyrics on YouTube videos. So, yeah, there was someone out there who was already doing what I had thought about. It sounded like most of the other well thought so-called new ideas I had...and I was just a step away from fetching SubRip “srt” subtitle files for my favorite music videos.

### And the hacking started…

I already had a bit of experience working with the chrome developer tools (thanks to Node.js and front end designing). So I put on my hacker glasses and fired up Chrome Dev tools. I switched to the network tab and began to look for any text file that could contain the lyrics.

![Image](https://cdn-media-1.freecodecamp.org/images/1*O89WdLDnoVHaOvXK5T-A5w.jpeg)
_Snapshot of developer tools with YouTtube video playing_

But I was analyzing requests on a page that was playing YouTube videos, so I had a plenty of requests. And since the extension was fetching lyrics, the request must have something to do with the Musixmatch domain. 

So I filtered using the keyword ‘musix’ and looked patiently for my file and I finally found it. Lyrics along with the time stamp. I noted the URL of that request and frankly, it all seemed like gibberish to me. Anyways, I copied the URL string as such and then pasted it into the URL bar, and voilà, I got the lyrics. 

So, the only thing left was to find out how the URL is being framed and what were the parameters..

![Image](https://cdn-media-1.freecodecamp.org/images/1*JlKw3JsfgOuUkgG3SS0rRw.jpeg)
_Request URL_

### Parameters and what?

After all the analyzing and filtering, I finally ended up with this. A long URL with a bunch of unknown parameters.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1kfqTsYqS8MjhQY5Dyqq0A.jpeg)
_Parameters for the URL_

I needed to dig deeper to actually understand the importance of each parameter. At a glance, it was clear that the only parameters that actually mattered were `res` and `v`. Others were just for house-keeping stuff. Then I began to explore the options and ended up wasting an hour just to find that the parameter `v` is nothing but the YouTube Video Id.

For example, the Video Id or `v` for a YouTube video with a URL https://www.youtube.com/watch?v=ZQeq_T_2VE8 is `ZQeq_T_2VE8`. Now that I had unveiled the mystery of `v`, I thought it would take me hardly another hour to find about `res`, but boy was I wrong.

### The curious case of the parameter ‘res’

An hour of deep analysis and research gave me nothing. A little later, I realized that the URL worked even when I changed few alphabets. I kept up digging and by the end of the 3 hours, I figured out that the alphabets in the string didn’t mean anything. They were just put randomly.

```
A typical value of res : 90rt120b114xz70xv82w85vv90a94hn90vb102av86
```

So I was done with the alphabets but the numeric values were still alien to me. The next thing I could think of was applying a bit of reverse-engineering to analyze the numbers. 

I began with removing all the alphabets as they didn’t mean anything and the first thing I noticed that the number of those values were fixed, the number being 11. I tried it with many other videos, but the number remained constant. 

Suddenly, it struck me, Video Id, the `v`, we discussed earlier also had 11 characters. However, each character in `v` could be an alphabet or a digit or even a ‘-’ or ‘_’, unlike `res` which had only numbers. 

So, I tried the most obvious mapping that can map a character to its numeric value, ASCII, and voilà that was it. The characters were ASCII encoded and alphabets were randomly put in between the numbers to make the whole string look more random, I guess.

At this point, I was delighted. After all, I had learned about all the parameters and was only a step away from writing my own handy script to download the lyrics file in “srt” format. Just to be sure, I checked with different videos and there seemed to be no issue whatsoever. I also shared the URL with one of my friends (yeah, a music lover).

I got a quick reply and it said “What is it? There’s nothing”. I crosschecked the URL and it was working fine on my browser.

### Who was the culprit ? :P

> I don’t get sent anything strange like underwear. I get sent cookies. :P — Jennifer Aniston

![Image](https://cdn-media-1.freecodecamp.org/images/1*zfKtWngPstlY9a7Iw64p3g.jpeg)
_Cookie field in the Request Headers_

I fired up the developer tools again and then copied the link for a new song. It again worked and then I switched to an incognito tab and pasted that same URL. It didn’t work. 

My experience of CTF (Capture The Flag) contests immediately told me that it had something to do with the cookies. That’s the most likely case if a URL is working in a browser window and not the other. 

I switched to the developer console and saw that the cookie was indeed being sent by the browser. To be sure, I analyzed the request many times and it finally occurred to me that the cookie being sent was the same the Musixmatch server is sending in the response. Also, each cookie is valid for only a certain time period. 

So, I wrote a Python script using urllib that first gets the cookie from a normal HTTP response since the cookie works across the domain. Then the cookie along with other parameters was framed as an HTTP request and we got the lyrics... Finally!!

### Preparing the parameters for a successful request

Here is the Python code for all the steps discussed above. The code first generates the parameters followed by a request to get the cookies. URL is then prepared using the parameters. Next, the cookie is defined in the header request along with other header fields like ‘Host’ and ‘User-agent’ to give it more of an authentic request look.

### Parsing the raw timed lyrics into srt format

Now, the next major thing or the only task left was to convert the raw timed lyrics data into a proper srt (SubRip Text) format. Here is what the MusixMatch lyrics format looked like.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FcdBLOPuQQddd7uM6vYTrQ.jpeg)
_HTTP Response for the lyrics_

Below is a proper format for a srt file.These files contain formatted lines of plain text in groups separated by a blank line. Subtitles are numbered sequentially, starting at 1 as depicted in the figure below.

```
100:00:00,350 --> 00:00:03,45071 buildings explodedor caught fire.
```

```
200:00:03,490 --> 00:00:05,020Elliot, tell me what it isthat you think he did.
```

```
300:00:05,060 --> 00:00:06,930Sorry.I don't know if I can say.
```

This sounded like a whole lot of work was required as the data was yet to be properly formatted. But, if you have the required data and a knowledge of Python, all it takes is a simple script to handle the data and that’s exactly what I did. The HTML tags annoyed me a bit during HTML parsing but guess what, there is an awesome library just for HTML parsing which made the whole process very easy. No points for guessing the library’s name, HTMLParser :-).

## Final words

So, I put together this script along with some modifications and with a simple front end on a flask server, I had my own lyrics fetching interface, possibly the only one of its kind in the whole world !!

By the way, if you are into music, have a look at Musixmatch. It is really awesome. This exercise was just for educational purposes and wasn’t used in any way to violate Musixmatch’s copyright.

