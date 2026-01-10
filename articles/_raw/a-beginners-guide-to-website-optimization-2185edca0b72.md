---
title: A beginner’s guide to website optimization
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-08T09:48:26.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-website-optimization-2185edca0b72
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xNt4aprSuOo2bdYg9F-6gw.jpeg
tags:
- name: Productivity
  slug: productivity
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Mario Hoyos

  I am a beginner, and I was able to achieve 99/100 in Google’s optimization ranking.
  If I can do it, you can too.

  If you’re like me, you like proof. So here are Google’s PageSpeed Insights results
  for hasslefreebeats, a website that I m...'
---

By Mario Hoyos

I am a beginner, and I was able to achieve 99/100 in Google’s optimization ranking. If I can do it, you can too.

If you’re like me, you like proof. So here are [Google’s PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/) results for [hasslefreebeats](https://www.hasslefreebeats.com), a website that I maintain and recently spent some time optimizing:

![Image](https://cdn-media-1.freecodecamp.org/images/zezZUe60TuNoOV7BQOmSolQoXAmdjqYXyr8Q)
_A screenshot of my PageSpeed Insights score._

I am pretty proud of these results, but I want to stress that I didn’t have a clue about how to optimize a website just a couple of weeks ago. What I have to share with you today is simply the result of a whole lot of googling and troubleshooting, pains I wish to spare you.

This article is broken up into subsections for each optimization, in case you want to jump around.

I am by no means an expert, but I’m confident that if you implement the techniques below, you will see results!

### Images

![Image](https://cdn-media-1.freecodecamp.org/images/OVVkYdYxj4rUdLyXLdX0fYA6tOCXO226f5cB)
_Image courtesy of Pexels (and surely optimized by Medium)._

As a beginner web-developer, images were not something I ever paid much mind to. I knew that adding high-quality images to my website would make it look more professional, but I never stopped to consider the effects they would have on my page’s load time.

The main thing I did to optimize my images was compress them.

Looking back, this should have been fairly intuitive from the get-go, but it wasn’t for me, so maybe it isn’t for you either.

The service that I used to compress my images was [Optimizilla](http://optimizilla.com/), an easy-to-use website where you upload your images, select the level of compression you want, and then download the compressed image. I saw size decreases upwards of 70% for some of my resources, which goes a LONG way towards faster load times.

Optimizilla is hardly the only choice for your image compression needs. Some standalone, open-source software you can use is [ImageOptim](https://imageoptim.com/mac) for Mac or [FileOptimizer](https://sourceforge.net/projects/nikkhokkho/files/FileOptimizer/) for Windows. If you prefer to compress using build tools, there are [Gulp](https://www.npmjs.com/package/gulp-imagemin) and [WebPack](https://github.com/Klathmon/imagemin-webpack-plugin) plugins that should do the trick. It doesn’t matter so much how you do, so long as you do. The performance gains are well worth the minimal effort.

Depending on your use case, it may also be worth looking at your files’ format. Generally speaking, jpg is going to be smaller than png. The main difference in whether I use one or the other is whether I need transparency behind the image: If I need transparency, I use png, otherwise I use jpg. You can dive deeper into the pros and cons of both [here.](https://www.digitaltrends.com/photography/jpeg-vs-png-photo-format/)

Also, Google has come out with a webp format that is pretty sweet, but since it’s not supported on all browsers yet, I’m hesitant to use it. Keep an eye out for further support in the future!

I didn’t do more than compress my images to get the results I showed you above, but if you want to optimize further [here is a great article.](https://www.frontamentals.com/practical-guide-to-images)

### Video

![Image](https://cdn-media-1.freecodecamp.org/images/pyCjB8NJV7cWOJ3rtxEKW0YsrrmW0icWFHvf)
_Photo by Terje Sollie from Pexels._

I haven’t used video in any of my current projects, so I will only touch on this briefly as I do not feel I am the best resource for this, specifically.

This is one of those situations where I would likely let the pros do the heavy lifting. [Vimeo](http://Mock interview outline    background of company        What we do            — Match                                                                      What we're looking for            Entry level dev who can jump in and go to work            Quick learner            excited to build clean code    tell me about yourself        education        experience        tech stack familiarity            Go over each main piece of tech and ask about comfort and             familiarity with each piece        How do you stay up to date on new technologies?        What new technologies are you currently learning?        1. Tell me about the most recent project you worked on. What                 were your responsibilities?        2. What is semantic html?        3. What is the box model in css?            What CSS frameworks/libraries have you used?        4. What is the keyword 'this' used for?        5. What is a callback?        6. How do promises work in JavaScript?        7. What is a closure?        8. What is the prototype on objects?        9. What is rest?        1. Describe the react lifecycle        2. What is redux and why would we use it?     Whiteboarding Problem        Write a function that takes in a multi-dimensional array, finds the average of each array in the collection, and returns the sum of the averages.        What are your salary requirements?        What questions do you have for me?   At end of interviews, talk about JavaScript Fundamentals and using flash cards or something to remember and train on the concepts. Have enough know to give high level definition of concept, then enough in your pocket to give more including examples  Do you know what it is What's an example) offers an excellent platform for hosting videos where they will degrade video quality for slower connections and compress your videos to optimize performance.

You could also host your videos on Youtube and then use this [youtube-dl](https://rg3.github.io/youtube-dl/) tool to download them from Youtube while configuring the videos to your website’s needs.

For other possible solutions, check out [Brightcove](https://www.brightcove.com/en/), [Sprout](https://sproutvideo.com/) or [Wistia](https://wistia.com/).

### Gzip

![Image](https://cdn-media-1.freecodecamp.org/images/IRfWI4Cv-mN4go0roOEw2pPR3VlCvCFmkONT)
_Get it? Zip? Image courtesy of Pexels._

I had no idea what gzipping was when I initially deployed my website.

Long story short, gzip is a file compression format that most browsers understand and that can run behind the scenes without requiring the user to even know it’s happening.

Depending on where you are hosting your application, gzipping may be as simple as flipping a configuration switch to specify that you want your server to gzip files when sending them out. In my case, my website is hosted on Heroku, which does not provide this option.

As it turns out, there are packages to add compression explicitly in your server code, which allows you to reap the benefits of gzipping in exchange for only a few lines of code. Using [this](https://github.com/expressjs/compression) compression middleware, [I was able to decrease the size of my Javascript and CSS bundles by 75%.](https://codeburst.io/how-i-decreased-the-size-of-my-heroku-app-by-75-1a4cf329b0ab)

It is worthwhile to check if your hosting service provides a gzip option. If it does not, look into how to add gzipping to your server-side code.

### Minifying

![Image](https://cdn-media-1.freecodecamp.org/images/HEgC7zdae1AigTekOi6h4gLJvL5jsikRl4mH)
_Minified pineapple courtesy of Pexels._

Minification is the process of removing unnecessary characters from code without affecting its functionality (whitespace, new-line characters, and so on). This allows you to decrease the size of the file you are transporting across the internet. It’s also useful for obfuscating your code, which makes it harder for sneaky hackers to detect security weak-points.

These days, minifying is usually done as part of the build process with Webpack or Gulp or some alternative. These build tools can have a bit of a learning curve, however, so if you are looking for easier alternatives, Google recommends [HTML-Minifier for HTML](https://github.com/kangax/html-minifier), [CSSNano for CSS](https://github.com/ben-eb/cssnano), and [UglifyJS for Javascript](https://github.com/mishoo/UglifyJS2).

### Browser-Caching

![Image](https://cdn-media-1.freecodecamp.org/images/zdsoMOxhnEdxS8Dqk66AcOM50hLjIyZdUYiv)
_Not quite how the browser stores data, but it’s as close as I could get. Courtesy of Pexels._

Storing static files in the browser’s cache is a very efficient way to increase the speed of your website, especially on return visits from the same client. I was not aware, until Google told me, that some of my resources were not being cached appropriately because of missing headers on the HTTP response I was sending from my server.

As soon as my home page is loaded, a request is made to my server to get data about a bunch of songs which are then rendered in a music player. I don’t update the songs on this website very often, so I do not mind if a user comes to my website and sees the same songs from the last time they visited, if it will make my page load a bit faster for them.

In order to get a performance boost, I added the following code to my server’s response object (Express/Node server):

```
res.append("Cache-Control", "max-age=604800000");
```

```
res.status(200).json(response);
```

All I am doing here is appending a cache-control header to my response, which says that after one week (in milliseconds), the resources should be re-downloaded. If you update these files more often, a shorter max-age might be a good idea.

### **Content Distribution Network**

![Image](https://cdn-media-1.freecodecamp.org/images/uDwV3cw6CCHGF9gi2ifn6F5fAtjNxIeCCPOm)
_Real-life image of a CDN, courtesy of Pexels._

A content distribution network, or CDN, is a network that allows users from all over the world to be geographically closer to your content. If a user has to load a large image from Japan, but your server is in the United States, this will take longer than if you had a server in Tokyo.

A CDN allows you to take advantage of a bunch of proxy servers located all over the world, allowing your content to be loaded more quickly regardless of where your end-user is located.

I want to note that I was able to achieve the results you saw above **before** implementing a CDN — I simply wanted to mention them as no article about website optimization would be complete without mentioning them. Having one of these bad boys on your website is imperative if you are planning to have a worldwide audience.

Some popular CDNs include [CloudFront](https://aws.amazon.com/cloudfront/) and [CloudFlare](https://www.cloudflare.com/lp/ddos-a/?_bt=157293179478&_bk=cloudflare&_bm=e&_bn=g&gclid=CjwKCAiA_c7UBRAjEiwApCZi8Ri3kAEt3UraYPUFUQOMTG0Xz7WGCNRUri0UNtCOUAdUMJI8osxuDRoCTx8QAvD_BwE).

### Miscellaneous

Here’s a couple more tips to squeeze out even more juice:

* Optimize your website to load “above-the-fold” content first to increase the perceived performance of your site. One common way to do this is by [lazy-loading](https://en.wikipedia.org/wiki/Lazy_loading) images that don’t show up on the landing page.
* Unless your application depends on Javascript to render HTML, such as a website built with Angular or React, then it is likely safe to load your script tags at the bottom of the body section of your HTML file. This could affect your [time-to-interactive](https://developers.google.com/web/tools/lighthouse/audits/time-to-interactive), however, so it is NOT a technique I would recommend for every situation.

### In Conclusion

This is just the tip of the iceberg when it comes to optimizing your website. Depending on the amount of traffic you are receiving and the service you are providing, you could have performance bottlenecks in many different areas. Maybe you need more servers, maybe you need a server with more RAM, maybe your triple-nested for-loop could use some refactoring — who knows?

There is no one-size-fits-all when it comes to speeding up your site, and you’ll ultimately have to make the best decisions for your situation based on measurements. Don’t waste your time optimizing something that does not need optimizing. Analyze the performance of your site to find bottlenecks, then attack those specifically.

I hope that you found something useful in this article! As I mentioned, I still have a lot to learn in this domain. If you have any additional tips or recommendations, please leave them in the comments below!

If you liked this article please give it some claps and check out:

* [Tools I wish I had known about when I started coding](https://medium.freecodecamp.org/tools-i-wish-i-had-known-about-when-i-started-coding-57849efd9248)
* [Tools I wish I had known about when I started coding: Revisited](https://medium.freecodecamp.org/tools-i-wish-i-had-known-about-when-i-started-coding-revisited-ffb715ffd23f)

Also, give me a follow on [Twitter](https://twitter.com/marioahoyos).

