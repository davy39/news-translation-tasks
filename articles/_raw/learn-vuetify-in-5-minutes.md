---
title: Learn Vuetify in 5 Minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-12T16:38:26.000Z'
originalURL: https://freecodecamp.org/news/learn-vuetify-in-5-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-12-at-17.19.31--2-.png
tags:
- name: Scrimba
  slug: scrimba
- name: vue
  slug: vue
- name: Vuetify
  slug: vuetify
seo_title: null
seo_desc: 'By Leanne Rybintsev

  Welcome to a whistle-stop tour of Vuetify - a popular component library for Vue.js.
  It allows you to create attractive, accessible apps with 80 elements ready to use
  from the get-go, plus it gives you the option to customize eleme...'
---

By Leanne Rybintsev

Welcome to a whistle-stop tour of Vuetify - a popular component library for Vue.js. It allows you to create attractive, accessible apps with 80 elements ready to use from the get-go, plus it gives you the option to customize elements for a bespoke design.

In the next five minutes, I'll you show you the following hot Vuetify elements:

- Typography
- Spacing
- Buttons
- Navigation
- Grid
- Card

And by the end of this article, you'll feel confident in making stunning apps with just a few lines of code.

While reading, head over to [Scrimba's 2-hour Vuetify course](https://scrimba.com/course/gvuetify?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article) to find out more and explore the code in the platform's interactive playground. Plus you can test your new skills with some interactive coding challenges. Let's get started!

## Creating a Vuetify object
To use Vuetify, we first pull in Vue and Vuetify from their CDNS. 

```html
<script src="https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js"></script>
```

This allows us to instantiate a Vue application with a Vuetify property and create a new Vuetify object:
```js
new Vue({ 
    el: '#app',
    vuetify: new Vuetify({}),
    data: {
        message: 'Using Single File Components'
    }
});
```
[Click through](https://scrimba.com/p/pP4xZu3/ckPbepSM?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article) to see this in detail. 

## Typography

[![Vuetify typography](https://dev-to-uploads.s3.amazonaws.com/i/uey76nlf4hxjttq9krzh.png)](https://scrimba.com/p/pP4xZu3/cMqPmeTG?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article)
*Click the image to go to the cast.*

Vuetify provides plenty of options for creating stunning typography, from headings of various sizes, to titles, subtitles and body text:
```vue
<h1 class="display-4">Heading 1</h1>
<h2 class="display-3">Heading 2</h2>
<h3 class="display-2">Heading 3</h3>
<h4 class="title">Title</h4>
<h5 class="subtitle-1">Subtitle</h5>
<p class="body-1">Body</p>
```

Changing text color and background color is easy with Vuetify, too. For the background color, simply add the name of the required color to the element's class. For text color, just add the color name followed by `--text`. 

This works for around 20 standard colors and can be customized using accompanying classes such as `lighten` and `darken`.
```vue
<h1 class="display-4 purple yellow--text text--darken-2">Heading 1</h1>
```

Vuetify also offers classes to change the font weight and style, as well as truncate and transform text. [Head over to the cast](https://scrimba.com/p/pP4xZu3/cMqPmeTG?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article) to find out more. 

## Spacing

Anyone who's ever used CSS knows that margins and padding can be tricky. Not with Vuetify! To add and adjust the spacing between elements, simply use classes with the following abbreviations:

`m` = margin
`p` = padding
`t` = top
`r` = right
`b` = bottom
`l` = left
`x` = right + left
`y` = top + bottom
`a` = all 

Spacing size is adjusted using the numbers 1 to 12, which correspond to four-pixel increments. For example `ml-5` denotes a left margin of 20 pixels. 

```vue
<h3 class="ml-5">Spacing</h3>
```

Centering elements is also easy with Vuetify. Simply wrap the element in a container that spans the page, then give it a right and left margin of `auto`:
```vue
<v-row>
     <h3 class="mx-auto">Spacing</h3>
</v-row>
```

That's not the end of Vuetify's handy tips and tricks for element spacing. [Click through](https://scrimba.com/p/pP4xZu3/cD7pnzSw?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article) to the cast to see more!

## Buttons

Vuetify offers dozens of options for styling buttons, including regular clickable buttons, outline buttons with ready-positioned icons, and icon-only buttons. 

Keeping reading to see some of the options available straight out the box, or [click through](https://scrimba.com/p/pP4xZu3/crmrBwtP?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article) to see how to customize buttons. 

**Large outline button:**

![Large outline button](https://dev-to-uploads.s3.amazonaws.com/i/uobelihs9l8ab86duimx.png)

```vue
<v-btn large outlined>Submit</v-btn>
```

**Button with icon:**

![Button with icon](https://dev-to-uploads.s3.amazonaws.com/i/zbs74uvuqnyfyrg529yq.png)
```vue
<v-btn tile outlined color="success">
     <v-icon left>mdi-pencil</v-icon> Edit
</v-btn>
```

**Floating action icon button:**
![Floating action button with icon](https://dev-to-uploads.s3.amazonaws.com/i/39p0zcaeyr8plveu2tjj.png)
```vue
<v-btn class="mx-2" fab dark color="indigo">
     <v-icon dark>mdi-plus</v-icon>
</v-btn>
```
## Navigation

[![Vuetify navigation bar](https://dev-to-uploads.s3.amazonaws.com/i/z4iz7cjvdttvdk31227f.png)](https://scrimba.com/p/pP4xZu3/czkwwQCw?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article)
*Click the image to go the cast.*

The two main navigation options available in Vuetify are `<v-app-bar>` and `<v-toolbar>`. 

```vue
<v-app-bar
     color="deep-purple accent-4"
     dense
     dark
>
```

Although the two elements are interchangeable to some extent, `<v-app-bar>` is designed for use as a site's main navigation and includes features such as scroll animations and a range of props and options. 

`<v-toolbar>` is a smaller, more versatile component which is designed to provide functionality to other areas of an app. For instance, it could be used for the basic edit features on a small text editor.

Both navigation elements handle list drop-downs and automatically size navigation icons and buttons. 

## Grid

Vuetify has a built-in grid system which makes sizing and positioning elements in an app simpler than ever. The grid is split into 12 columns and has five media breakpoints for handling a variety of screen sizes.

While the default width of an element is 12 columns, it's easy to adjust this by changing the column value. For example, an item with a column value of 6 takes up half the page width. Items can be positioned using the `offset` property. 
```vue
<v-col sm="6" offset-sm="3">
    <v-card
    class="pa-2"
    outlined
    tile
    >
    Column
    </v-card>
</v-col>
```

Columns in Vuetify come with pre-set spacing. [Click through](https://scrimba.com/p/pP4xZu3/cWKBnPSV?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article) to the scrim to see how this affects the element and how to customize it. 

## Card

[![Customised Vuetify card](https://dev-to-uploads.s3.amazonaws.com/i/mvxtqa1l2dfze9mu8acv.png)](https://scrimba.com/p/pP4xZu3/cdNW42t8?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article)
*Click the card to access the scrim.*

Adding cards to your app is simple with Vuetify's `<v-card>` element, which is easily customisable with its four optional nested elements: `<v-card-title>`, `<v-card-text>`, `<v-card-actions>` and `<v-list-item-content>`. 

I've played around with the card provided [in the cast](https://scrimba.com/p/pP4xZu3/cdNW42t8?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article) to make my own Coffee Card. Why not head over and see where your imagination takes you, too?

```vue
 <v-card class="mx-auto" color="brown" dark >
    <v-card-title>
    <v-icon large left> mdi-coffee</v-icon>
    <span class="title font-weight-light">Coffee Card</span>
    </v-card-title>

    <v-card-text class="headline font-weight-bold">"Coffee Rocks!"</v-card-text>

    <v-card-actions>
    <v-list-item class="grow">
        <v-list-item-content>
        <v-list-item-title>Miss C Bean</v-list-item-title>
        </v-list-item-content>

        </v-row>
    </v-list-item>
    </v-card-actions>
</v-card>
```

That's all for our hyper-speed tour of Vuetify's basic functions. To explore further, head over [to the course](https://scrimba.com/p/pP4xZu3/cdNW42t8?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article) and check out the Playground.vue file, where you can test out the code and see more of what it can do.

The course also includes a bunch of interactive challenges to put your newfound knowledge to the test and get you well on your way to becoming a Vuetify pro. When you're done there, why not check out [Scrimba's](https://scrimba.com/?utm_source=dev.to&utm_medium=referral&utm_campaign=gvuetify_5_minute_article) huge range of other topics to continue your learning journey? 

Whatever you choose to do next, happy coding :) 



