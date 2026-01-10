---
title: 10 Awesome JavaScript Libraries You Should Try Out
subtitle: ''
author: Ashutosh K Singh
co_authors: []
series: null
date: '2021-01-03T17:32:00.000Z'
originalURL: https://freecodecamp.org/news/10-javascript-libraries-you-should-try
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9999740569d1a4ca20a6.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Libraries
  slug: libraries
- name: Productivity
  slug: productivity
seo_title: null
seo_desc: 'JavaScript is one of the most popular languages on the web. Even though
  it was initially developed just for web pages, it has seen exponential growth in
  the past two decades.

  Now, JavaScript is capable of doing almost anything and works on several pl...'
---

JavaScript is one of the most popular languages on the web. Even though it was initially developed just for web pages, it has seen exponential growth in the past two decades.

Now, JavaScript is capable of doing almost anything and works on several platforms and devices including IoT. And with the recent SpaceX Dragon launch, JavaScript is even in space.

One of the reasons for its popularity is the availability of a large number of frameworks and libraries. They make development much easier compared to traditional Vanilla JS development.

There are libraries for almost anything and more are coming out almost every day. But with so many libraries to choose from it becomes difficult to keep a track of each one and how it might be tailored specifically to your needs.

In this article, we will discuss 10 of the most popular JS libraries which you can use to build your next project.

# [Leaflet](https://leafletjs.com/)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-17.png align="left")

*Leaflet*

I think Leaflet is the best open source library for adding mobile-friendly interactive maps to your application.

Its small size (39kB) makes it a great alternative to consider over other map libraries. With cross-platform efficiency and a well-documented API, it has everything you need to make you fall in love.

Here is some sample code that creates a Leaflet map:

```javascript
var map = new L.Map("map", {
    center: new L.LatLng(40.7401, -73.9891),
    zoom: 12,
    layers: new L.TileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png")
});
```

In Leaflet, we need to provide a tile layer since there isn't one by default. But that also means that can choose from a wide range of layers both free and premium. You can explore various free tile layers [here](https://leaflet-extras.github.io/leaflet-providers/preview/).

Read the [Docs](https://leafletjs.com/reference-1.6.0.html) or follow the [Tutorials](https://leafletjs.com/examples.html) to learn more.

# [fullPage.js](https://alvarotrigo.com/fullPage/)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ezgif.com-video-to-gif-1--1.gif align="left")

This open-source library helps you create full-screen scrolling websites as you can see in the above GIF. It's easy to use and has many options to customize, so it's no surprise it is used by thousands of developers and has over 30k stars on GitHub.

Here is a Codepen demo that you can play with:

%[https://codepen.io/lelouchb/pen/WNrLvLG] 

You can even use it with popular frameworks such as:

* [react-fullpage](https://alvarotrigo.com/react-fullpage/)
    
* [vue-fullpage](https://alvarotrigo.com/vue-fullpage/)
    
* [angular-fullpage](https://alvarotrigo.com/angular-fullpage/)
    

I came across this library about a year ago and since then it has become one of my favorites. This is one of the few libraries that you can use in almost every project. If you haven't already started using it then just try it, you will not be disappointed.

# [anime.js](https://animejs.com/)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/anime.gif align="left")

*anime.js*

One of the best animation libraries out there, Anime.js is flexible and simple to use. It is the perfect tool to help you add some really cool animation to your project.

Anime.js works well with CSS properties, SVG, DOM attributes, and JavaScript Objects and can be easily integrated into your applications.

As a developer it's important to have a good portfolio. The first impression people have of your portfolio helps decide whether they will hire you or not. And what better tool than this library to bring life to your portfolio. It will not only enhance your website but will help showcase actual skills.

Check out this Codepen to learn more:

%[https://codepen.io/lelouchb/pen/XWXoboE] 

You can also take a look at all the other cool projects on [Codepen](https://codepen.io/collection/XLebem) or [Read the Docs here](https://animejs.com/documentation/).

# [Screenfull.js](https://github.com/sindresorhus/screenfull.js)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-29.png align="left")

*screenfull.js*

I came across this library while searching for a way to implement a full-screen feature in my project.

If you also want to have a full-screen feature, I would recommend using this library instead of [Fullscreen API](https://developer.mozilla.org/en/DOM/Using_full-screen_mode) because of its cross-browser efficiency (although it is built on top of that).

It is so small that you won't even notice it – just about 0.7kB gzipped.

Try the [Demo](https://sindresorhus.com/screenfull.js) or read the [Docs](https://github.com/sindresorhus/screenfull.js) to learn more.

# [Moment.js](https://momentjs.com/)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-18.png align="left")

*Moment.js*

Working with date and time can be a huge pain, especially with API calls, different Time Zones, local languages, and so on. Moment.js can help you solve all those issues whether it is manipulating, validating, parsing, or formatting dates or time.

There are so many cool methods that are really useful for your projects. For example, I used the `.fromNow()` method in one of my blog projects to show the time the article was published.

```javascript
const moment = require('moment'); 

relativeTimeOfPost = moment([2019, 07, 13]).fromNow(); 
// a year ago
```

Although I don't use it very often, I am a fan of its support for internationalization. For example, we can customize the above result using the `.locale()` method.

```javascript
// French
moment.locale('fr');
relativeTimeOfPostInFrench = moment([2019, 07, 13]).fromNow(); 
//il y a un an

// Spanish
moment.locale('es');
relativeTimeOfPostInSpanish = moment([2019, 07, 13]).fromNow(); 
//hace un año
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ezgif.com-video-to-gif.gif align="left")

*Moment.js Homepage*

Read the [Docs here](https://momentjs.com/).

**Update September 2020:** Moment.js has entered maintenance mode. Read more about it [here](https://momentjs.com/docs/#/-project-status/). You may want to explore alternatives such as [Day.js](https://day.js.org/) or [date-fns](https://date-fns.org/).

# [Hammer.js](http://hammerjs.github.io/)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ezgif.com-video-to-gif-2.gif align="left")

Hammer.js is a lightweight JavaScript library that lets you add multi-touch gestures to your Web Apps.

I would recommend this library to add some fun to your components. Here is an example to play with. Just run the pen and tap or click on the grey div.

%[https://codepen.io/lelouchb/pen/abdPOPj] 

It can recognize gestures made by touch, mouse and pointerEvents. For jQuery users I would recommend using the [jQuery plugin](http://hammerjs.github.io/jquery-plugin/).

```javascript
$(element).hammer(options).bind("pan", myPanHandler);
```

Read the [Docs here](http://hammerjs.github.io/getting-started/).

# [Masonry](https://masonry.desandro.com/)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-20.png align="left")

*Masonry*

Masonry is a JavaScript grid layout library. It is super awesome and I use it for many of my projects. It can take your simple grid elements and place them based on the available vertical space, sort of like how contractors fit stones or blocks into a wall.

You can use this library to show your projects in a different light. Use it with cards, images, modals, and so on.

Here is a simple example to show you the magic in action. Well, not magic exactly, but how the layout changes when you **zoom in** on the web page.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ezgif.com-crop.gif align="left")

And here is the code for the above:

```javascript
var elem = document.querySelector('.grid');
var msnry = new Masonry( elem, {
  itemSelector: '.grid-item',
  columnWidth: 400
});

var msnry = new Masonry( '.grid');
```

Here is a cool demo on Codepen:

%[https://codepen.io/lelouchb/pen/qBbLdLQ] 

Check out these Projects

* [https://halcyon-theme.tumblr.com/](https://halcyon-theme.tumblr.com/)
    
* [https://tympanus.net/Development/GridLoadingEffects/index.html](https://tympanus.net/Development/GridLoadingEffects/index.html)
    
* [https://www.erikjo.com/work](https://www.erikjo.com/work)
    

# [D3.js](https://d3js.org/)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-30.png align="left")

If you are a data-obsessed developer then this library is for you. I have yet to find a library that manipulates data as efficiently and beautifully as D3. With over 92k stars on GitHub, D3 is the favorite data visualization library of many developers.

I recently used D3 to visualize COVID-19 data with React and the [Johns Hopkins CSSE Data Repository on GitHub](https://github.com/CSSEGISandData/COVID-19). It I was a really interesting project, and if you are thinking of doing something similar, I would suggest giving D3.js a try.

Read more about it [here](https://github.com/d3/d3/wiki).

# [slick](https://kenwheeler.github.io/slick/)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-23.png align="left")

*slick*

Slick is fully responsive, swipe-enabled, infinite looping, and more. As mentioned on the homepage it truly is the last carousel you'll ever need.

I have been using this library for quite a while, and it has saved me so much time. With just a few lines of code, you can add so many features to your carousel.

```js
$('.autoplay').slick({
  slidesToShow: 3,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 2000,
});
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/ezgif.com-video-to-gif-2-.gif align="left")

*Autoplay*

Check out the demos [here](https://kenwheeler.github.io/slick/).

# [Popper.js](https://popper.js.org/)

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-25.png align="left")

*Popper.js*

Popper.js is a lightweight ~3 kB JavaScript library with zero dependencies that provides a reliable and extensible positioning engine you can use to ensure all your popper elements are positioned in the right place.

It may not seem important to spend time configuring popper elements, but these little things are what make you stand out as a developer. And with such small size it doesn't take up much space.

Read the [Docs here](https://popper.js.org/docs/v2/).

# Conclusion

As a developer, having and using the right JavaScript libraries is important. It will make you more productive and will make development much easier and faster. In the end, it is up to you which library to prefer based on your needs.

These are 10 JavaScript libraries that you can try and start using in your projects today. What other cool JavaScript libraries you use? Would you like another article like this? [Tweet](https://twitter.com/noharashutosh) and let me know.
