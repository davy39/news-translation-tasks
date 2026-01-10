---
title: How to Add Search to a React App with Fuse.js
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-05-26T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-search-to-a-react-app-with-fuse-js
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/fusejs-1.jpg
tags:
- name: fuse.js
  slug: fuse-js
- name: front end
  slug: front-end
- name: Front-end Development
  slug: front-end-development
- name: frontend
  slug: frontend
- name: JavaScript
  slug: javascript
- name: js
  slug: js
- name: json
  slug: json
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: React
  slug: reactjs
- name: search
  slug: search
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: Search is a powerful way help people visiting your site find the content
  that's most important to them. But often it's really challenging to figure out the
  rules and logic to make that happen. In this article, we'll see how can we can use
  fuse.js to ...
---

Search is a powerful way help people visiting your site find the content that's most important to them. But often it's really challenging to figure out the rules and logic to make that happen. In this article, we'll see how can we can use fuse.js to add search to our apps.

* [What is fuse.js?](#heading-what-is-fusejs)
* [Why is search important?](#heading-why-is-search-important)
* [What are we going to build?](#heading-what-are-we-going-to-build)
* [Step 0: Bootstrapping our app](#heading-step-0-bootstrapping-our-app)
* [Step 1: Installing Fuse.js](#heading-step-1-installing-fusejs)
* [Step 2: Creating a new Fuse search instance](#heading-step-2-creating-a-new-fuse-search-instance)
* [Step 3: Setting up dynamic search based on user input](#heading-step-3-setting-up-dynamic-search-based-on-user-input)

%[https://www.youtube.com/watch?v=GZl-yEz4_qw]

## What is fuse.js?

[Fuse.js](https://fusejs.io/) is a JavaScript library that provides fuzzy search capabilities for applications and websites. It's nice and easy to use out of the box, but also includes configuration options that allow you to tweak and create powerful solutions.

## Why is search important?

Whether you're a content creator or are trying to sell a product with your website, it's important to help your visitors actually find what they're looking for. 

If you're building an ecommerce website, you want someone to be able to easily find your Bender vinyl figures rather than having to dig through the entire catalog first.

## What are we going to build?

We're going to start off with a basic Create React App example. It's going to include some character info as structured data for one of my favorite shows Futurama that's simply dumped out into an HTML list.

With that list, we're going to use fuse.js to provide client-side search capabilities, allowing us to demonstrate searching for the character we're looking for by their name and other details.

## Step 0: Bootstrapping our app

To get started, we're going to need content to work with. I got started by building a list of characters from Futurama as structured json data that I put in a list with a fresh Create React App.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/futurama-character-search-demo.jpg)
_Futurama character search demo_

You'll also notice I've already added an input for our search. It's not yet functional but we'll use that to get started.

If you'd like to start off at the same place, I created a branch with my demo repo that you can clone locally to walk through the project with me!

```shell
git clone --single-branch --branch start git@github.com:colbyfayock/my-futurama-characters.git

```

[Git branch "start"](https://github.com/colbyfayock/my-futurama-characters/tree/start)

Or [follow along with the commit](https://github.com/colbyfayock/my-futurama-characters/commit/20d4e42aaf69e214b63e684e012cd2f8c95d427b).

## Step 1: Installing Fuse.js

First thing we'll want to do is actually add Fuse.js to our app. In your project, run:

```shell
yarn add fuse.js
# or
npm install --save fuse.js

```

This will save the dependency to our project so that we'll be able to use it in our project.

Next we'll want to import the dependency to our app so that we can start building with it. At the top of your file, in our case `src/App.js` if you're following along with me in a new Create React App project, add:

```js
import Fuse from 'fuse.js';

```

If you want to test that it's working, you can `console.log(Fuse)` and see our `Fuse` class we'll use to create our search capabilities.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/fusejs-class.jpg)
_Imported fuse.js class_

And with that, we're ready to get started!

[Follow along with the commit](https://github.com/colbyfayock/my-futurama-characters/commit/54720daffa6ff415997c319b12f8f44d7ec8b748)

## Step 2: Creating a new Fuse search instance

To use Fuse.js, we'll want to first create a new instance of it.

At the top of your component, add:

```js
const fuse = new Fuse(characters, {
  keys: [
    'name',
    'company',
    'species'
  ]
});

```

With this does:

* Creates a new instance of Fuse
* Passes in our `characters` array of objects
* Specifies the 3 keys in our data that we want to search on

Next, to perform the search, we can add:

```js
const results = fuse.search('bender');

```

And if we console log out the results, we can see:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/basic-fusejs-search-results.jpg)
_Basic fuse.js search results_

You'll notice that we have more results than our friend Bender though. Fuse.js provides a "fuzzy search" meaning it tries to help you in case you're not sure what you're looking for or if you're misspelling your query.

To get an idea of how this works, let's add the `includeScore` option to our search:

```js
const fuse = new Fuse(characters, {
  keys: [
    'name',
    'company',
    'species'
  ],
  includeScore: true
});

```

Now we can see the `score` attribute in our results object.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/fusejs-search-results-with-score.jpg)
_Fuse.js search results with score_

You'll notice that our first result has a really low score. With fuse.js, a lower score means it's closer to an exact match.

A score of 0 indicates a perfect match, while a score of 1 indicates a complete mismatch.

It's saying that is incredibly likely that the first result is what we're looking for, but it's not confident in the others.

So with our results, we want to actually connect that to our UI. If you notice our array output is different than what we are mapping through for the HTML list, so let's create a new variable that we can change it to:

```js
const results = fuse.search('bender');
const characterResults = results.map(character => character.item);

```

What this is doing is creating a new array using the [map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) method that will only include the `item` property from each array object.

Then if we replace our `characters` map inside of our list with `characterResults.map`:

```jsx
<ul className="characters">
  {characterResults.map(character => {
    const { name, company, species, thumb } = character;

```

We can now see that our page only shows the results for "bender"!

![Image](https://www.freecodecamp.org/news/content/images/2020/05/futurama-character-search-filtered-results.jpg)
_Demo with filtered results_

[Follow along with the commit!](https://github.com/colbyfayock/my-futurama-characters/commit/adbf30a872fa134cfca4e142ba479877b9665e9a)

## Step 3: Setting up dynamic search based on user input

Now that we have a hard-coded search working, we want someone to actually be able to use the search input to search!

To achieve this, we're going to use the `useState` hook and listen for changes to the `input` field, which will dynamically create a search for our data.

First, import the `useState` hook from React:

```js
import React, { useState } from 'react';

```

Next, let's use that hook to create a state instance:

```js
const [query, updateQuery] = useState('');

```

Here, we're creating a new state of `query` that we can update with `updateQuery` that defaults to an empty string (`''`).

With that, let's tell our search input to use that `query` value as it's value:

```jsx
<input type="text" value={query} />

```

At this point, nothing should be different, as we are using a blank query.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/futurama-character-search-filtered-results.jpg)
_Demo with filtered results - nothing changed_

Now let's add an event handler to our input that we can use to update our state:

```jsx
<input type="text" value={query} onChange={onSearch} />

```

And we'll want to create that function so we can use it:

```js
function onSearch({ currentTarget }) {
  updateQuery(currentTarget.value);
}

```

This will update our `query` with the input's value any time it changes.

Now that our `query`  will have what we want to search for, we can update our search instance:

```js
const results = fuse.search(query);

```

And now if you reload the page, it's blank! ?

![Image](https://www.freecodecamp.org/news/content/images/2020/05/futurama-character-search-no-results.jpg)
_Demo with no results_

That's because by default, Fuse sees our empty query and doesn't match it to anything. If we now search for something like `slurms`, we can see our search dynamically update with results!

![Image](https://www.freecodecamp.org/news/content/images/2020/05/futurama-character-search-results.jpg)
_Demo with results for "slurms"_

If we wanted to fix this though so that all of our results show when there's no query, we can do so with an `if` statement or in my example, a ternary, that will show all of the characters if there is no query:

```js
const characterResults = query ? results.map(character => character.item) : characters;

```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/futurama-character-search-demo.jpg)
_Demo with all results_

And with that, we have our basic search!

![Image](https://www.freecodecamp.org/news/content/images/2020/05/futurama-character-search-results-query.jpg)
_Demo with filtered results for "zoidberg"_

[Follow along with the commit!](https://github.com/colbyfayock/my-futurama-characters/commit/1b8918fc56f31517686a6c73f1969787728736ac)

## What can I do next?

### Tuning your search

Fuse.js comes with a lot of options that you can use to tune your search to however you'd like. Want to only show confident results? Use the `threshold` option! Want case sensitive queries? Use the `isCaseSensitive` option!

[https://fusejs.io/api/options.html](https://fusejs.io/api/options.html)

### Setting the default query with URL parameters

Sometimes you want someone to be able to link to a particular set of results. To do this, we might want to be able to add a new URL parameter like `?q=bender`.

To make this work, you can grab that URL parameter with javascript and use that value to set our `query` state.

## Join the conversation!

%[https://twitter.com/colbyfayock/status/1265298322891378688]

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?️ Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

