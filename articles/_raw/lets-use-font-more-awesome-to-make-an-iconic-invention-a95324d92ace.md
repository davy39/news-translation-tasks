---
title: Font (More) Awesome — an iconic invention
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-08T07:31:19.000Z'
originalURL: https://freecodecamp.org/news/lets-use-font-more-awesome-to-make-an-iconic-invention-a95324d92ace
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cPpBR06SrC96_qi9Bw5Pmw.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: technology
  slug: technology
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Pubudu Dodangoda

  Whether you are building a website, a mobile app, or even a standalone app, there
  are few things you can never escape. The proper use of graphics and icons is one
  such basic need. Fancy icons are just as important as alignments an...'
---

By Pubudu Dodangoda

Whether you are building a website, a mobile app, or even a standalone app, there are few things you can never escape. The proper use of graphics and icons is one such basic need. Fancy icons are just as important as alignments and color combinations. That is because a single icon can express what a hundred words can say!

While there are numerous ways to add icons to a website, the most popular way is to use Font Awesome. Once you perform the required configurations, adding an icon is as simple as this:

```
<i class="fa fa-bell"></i>
```

Yet, there are situations where the icon set provided by Font Awesome is insufficient. For example, I recently wanted to use the logos of Facebook, Twitter, and Airbnb on a website. And it took me by surprise — the Airbnb icon was not included in Font Awesome. In fact, the community had requested the Airbnb icon about **3 years back**. Yet the icon is still not in the official icon set.

Also, if you want a custom icon which is not very popular, the least complex way to add it is using an `img` tag. This is too much work compared to using Font Awesome. On the other hand, the Font Awesome guys can’t cater to all icon requests, practically speaking.

So I searched for an easy way to get the icons I needed, without depending on a third party. Luckily, I found a tool called [Calligraphr](https://www.calligraphr.com/). I’ll now explain how I used this tool, some CSS knowledge, and few other simple tricks to be able to do the following in my code:

```
<i class="fa fa-troll"/><i class="fa fa-like-a-boss"/><i class="fa fa-lol"/>
```

![Image](https://cdn-media-1.freecodecamp.org/images/06GY02wLrvOJ37HhebA2R9Jb7c5ceMs-avez)

Pretty cool right? Then **let’s build Font More Awesome!**

### Creating a Font

The first milestone on our journey is to create the Font More Awesome font using the [instructions on their website](https://www.calligraphr.com/en/webapp/app_home/?/). The first step is to download the template. Here is an example:

![Image](https://cdn-media-1.freecodecamp.org/images/xvjYDSmV1iYpfqMQtNBhcrOlAaYQUR6hOb3X)
_Calligraphr Template_

Now what we have to do is fill in these boxes with our desired icons. You can either print and draw the icons by hand, or use a tool like Adobe Photoshop or GIMP to use images downloaded from the internet.

After filling the template, it will look as follows:

![Image](https://cdn-media-1.freecodecamp.org/images/T9jAuPS950YFzb61zATJA0iucZjDz1b4pMKU)

The next thing you have to do is quite simple. Just upload the filled template to the calligraphr website, and click on the “build font” button — and BOOM! Your custom font will be downloaded. Let’s name it `FontMoreAwesome.otf`

If you are wondering what magic just happened, it’s called image [vectorization](https://en.wikipedia.org/wiki/Image_tracing) or Image Tracing. Because of the underlying tracing algorithm, you might notice slight differences between the image used and the actual icon created. But, once the images are converted to a vector, they can scale up and down, without losing quality.

### Integrating with Font Awesome

Of course you can treat the new font file as a separate icon set. But wouldn’t it be cool if we could extend the Font Awesome font itself? Let’s do it!

One thing that you should understand here is that we are going to inherit the CSS rules defined by the Font Awesome CSS file. For example, it will contain an entry as follows:

```
.fa {  display: inline-block;  font: normal normal normal 14px/1 FontAwesome;  font-size: inherit;  text-rendering: auto;  -webkit-font-smoothing: antialiased;  -moz-osx-font-smoothing: grayscale;}
```

That means that when we define an icon element as follows, it will inherit styles such as `display`, `font-size`, and `text-rendering` from the above.

```
<i class="fa fa-troll"/>
```

Now let’s define our custom CSS file. Let’s name the file `font-more-awesome.css`

The first entry of this file should be the font-face declaration. This can be done as follows. No big deal. Just some basic CSS.

```
@font-face {    font-family: 'FontMoreAwesome';    src: url('../fonts/FontMoreAwesome.otf');    font-weight: normal;    font-style: normal;}
```

Then we can easily define the custom icons we want like this:

```
.fa-troll:before {    font-family: FontMoreAwesome;    content: "A";}.fa-lol:before {    font-family: FontMoreAwesome;    content: "B";}.fa-like-a-boss:before {    font-family: FontMoreAwesome;    content: "C";}
```

Note here that we are defining the icons as pseudo-elements using the `before` selector. That way, we can inject the content we want into the element which uses these classes.

In the FontMoreAwesome font we created, “A,” “B,” and “C” are represented by the icons for Troll, Lol, and Like-a-boss respectively. This is not the best way to do it, though.

Font Awesome uses Unicode Private Use Area (PUA) to ensure screen readers do not read off random characters that represent icons.

But for our example, we’ll stick with the English alphabet letters to keep the story simple.

Another thing to note in the above example is that we override the font-family defined by Font Awesome while injecting custom content.

### Let’s Use Font More Awesome

The final step is to load this CSS file into the index.html file, which is pretty easy.

```
<link href="css/font-more-awesome.css" rel="stylesheet">
```

Now you can use these icons as any other `fa` icon. For example, the following icon will be large and will spin.

```
<i class="fa fa-troll fa-spin fa-lg"/>
```

### Did you enjoy this story? Then there’s one little thing you could do…

![Image](https://cdn-media-1.freecodecamp.org/images/bD2IJyIxD9odMO7kgFmvcbVVQPDaCUceF69M)

