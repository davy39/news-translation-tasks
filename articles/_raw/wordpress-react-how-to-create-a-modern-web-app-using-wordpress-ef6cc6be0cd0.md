---
title: How to Create a Modern Web App Using WordPress and React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-25T10:55:58.000Z'
originalURL: https://freecodecamp.org/news/wordpress-react-how-to-create-a-modern-web-app-using-wordpress-ef6cc6be0cd0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sKZ0nC0gyc5tiqlVBfu_uQ.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Development
  slug: web-development
- name: WordPress
  slug: wordpress
seo_title: null
seo_desc: 'By Bret Cameron

  Combine the power of a React front-end with the internet’s most popular CMS

  Want the advantages of a modern React SPA, but need a back-end that feels familiar?
  In this article, we’ll go through how to set-up WordPress’s REST API, incl...'
---

By Bret Cameron

#### Combine the power of a React front-end with the internet’s most popular CMS

Want the advantages of a modern React SPA, but need a back-end that feels familiar? In this article, we’ll go through how to set-up WordPress’s REST API, including custom posts types and fields, and how to fetch this data inside React.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sKZ0nC0gyc5tiqlVBfu_uQ.png)

Recently, I was working on a React app for a client when they sprung this question on me: ‘Can we use it **_with WordPress_**_?_’

Since late 2015, the answer to this question has been yes. But the steps necessary to create a working decoupled site may not seem straightforward, especially to those who aren’t familiar with both WordPress _and_ React.

On my journey to create a working application, I encountered a handful of tricky obstacles, and in this article, I’ll explain how to avoid them. I’ll also share several tips and tricks I learned along the way!

### Contents

#### [Part 1: Background Information](https://medium.com/p/ef6cc6be0cd0#842b)

* [What is a Headless CMS?](https://medium.com/p/ef6cc6be0cd0#b8b4)
* [What Should I Know to Follow Along?](http://What Should I Know to Follow Along?)
* [Key Acronyms](http://Key Acronyms)
* [Where Can I See WordPress’s JSON Data?](https://medium.com/p/ef6cc6be0cd0#1012)

#### [Part 2: WordPress](https://medium.com/p/ef6cc6be0cd0#371b)

* [Adding a Custom Post Type](https://medium.com/p/ef6cc6be0cd0#c03e)
* [Changing Title Placeholder Text](https://medium.com/p/ef6cc6be0cd0#9a1a)
* [Adding a Custom Field to Your Custom Post Type](https://medium.com/p/ef6cc6be0cd0#40c2)
* [Making Custom Fields Available as JSON](https://medium.com/p/ef6cc6be0cd0#43a6)
* [Restricting Visible JSON Data](https://medium.com/p/ef6cc6be0cd0#6093)

#### [Part 3: React](https://medium.com/p/ef6cc6be0cd0#a1f9)

* [Promises in JavaScript](https://medium.com/p/ef6cc6be0cd0#39f1)
* [The Fetch Method](https://medium.com/p/ef6cc6be0cd0#092c)
* [Handling Promises](https://medium.com/p/ef6cc6be0cd0#02fd)

#### [A Working Example in React](https://medium.com/p/ef6cc6be0cd0#8a3b)

#### [Conclusion](https://medium.com/p/ef6cc6be0cd0#2968)

### Part 1: Background Information

![Image](https://cdn-media-1.freecodecamp.org/images/1*V5SV3AAoVrt9qjiWsTabbg.png)

#### What is a Headless CMS?

In the past, using a CMS like WordPress meant you had to build your frontend using PHP.

Now, with a headless CMS, you can build your front end with whatever technologies you like; this is because of the separation of the front-end and the back-end via an API. If you want to create a SPA (single-page application) using React, Angular or Vue, and control the content using a CMS like WordPress, you can!

#### What Should I Know to Follow Along?

You’ll get the most out of this article if you have:

* some knowledge of how a CMS like WordPress works, a bit of PHP, and an idea about how to set up a basic WordPress project on your computer;
* an understanding of JavaScript, including ES6+ language features and React class syntax.

#### Key Acronyms

Programming is full of jargon, but it does make it a lot quicker to discuss some of the concepts in this article. Here’s a quick recap of the terms we’ll be using:

* **CMS — content management system.** Think WordPress, Drupal, Joomla, Magneto.
* **SPA — single-page application.** Rather than re-loading each page in its entirety, a SPA application loads content dynamically. The fundamental code (HTML, CSS and JavaScript) of the website is loaded just once. Think React, Vue, Angular.
* **API — application programming interface.** In simple terms, a series of definitions, that a service provides to allow you to take and use its data. [Google Maps has one](https://developers.google.com/maps/documentation/javascript/tutorial). [Medium has one](https://github.com/Medium/medium-api-docs). And now, [every WordPress site comes with an API in-built](https://developer.wordpress.org/rest-api/).
* **REST — representational state transfer.** A style of web architecture based around HTTP’s request methods: `GET` , `PUT` , `POST` and `DELETE` . WordPress’s in-built API is a REST or “RESTful” API.
* **HTTP — hypertext transfer protocol.** The set of rules used to transfer data over the web. It’s specified at the beginning of URLs as `http` or `https` (the secure version).
* **JSON — JavaScript object notation.** Though derived from JavaScript, this is a language-independent format for the storage and transfer of data.

In this article, we’re using WordPress as our CMS. That means programming our back-end in PHP and using WordPress’s REST API to deliver JSON data to our frontend.

#### Where Can I See WordPress’s JSON Data?

Before getting to the good stuff, a quick note about _where_ you can find the JSON data on your WordPress site. Nowadays, every WordPress website has JSON data available (unless the site owner has disabled or restricted access to it). You take a look at the main JSON of a WordPress site by appending `/wp-json` to the root domain name.

So, for example, you can take a look at the JSON for WordPress.org by visiting [https://wordpress.org/wp-json](https://wordpress.org/wp-json). Or, if you’re running a WordPress site locally, you can see its JSON by following `localhost/yoursitename/wp-json`.

To access the data for your posts, type `localhost/yoursitename/wp-json/wp/v2/posts` . For a custom post format, swap in the new format (e.g. `movies`) instead of `posts`. What now looks like an unreadable block of text is exactly what will allow us to use WordPress as a headless CMS!

### Part 2: WordPress

![Image](https://cdn-media-1.freecodecamp.org/images/1*jUVbqOjhcy-68oCBkIlm2Q.png)

To set-up your REST API, most of what you’ll need to do will happen in your `functions.php` file. I’ll assume you know how to set up a WordPress project and access it using `localhost` , but if you’d like some help with that, I recommend [this article](https://www.taniarascia.com/developing-a-wordpress-theme-from-scratch/#installing-wordpress) (it’s what I used to get started programming with WordPress).

For most projects, you’ll want to use a custom post type, so let’s begin by setting one up.

#### Adding a Custom Post Type

Let’s say our site is about films, and we want a post type called ‘movies’. First, we want to make sure our ‘movies’ post type loads as soon as possible, so we’ll attach it to the `init` hook, using `add_action` :

```
add_action( 'init', 'movies_post_type' );
```

I’m using `movies_post_type()` , but you can call your function whatever you want.

Next, we want to register ‘movies’ as a post type, using the `register_post_type()` function.

The next chunk of code may look overwhelming, but it’s relatively simple: our function takes a lot of in-built arguments to control the functionality of your new post type, and most of them are self-explanatory. We’ll store these arguments in our `$args` array.

One of our arguments, `labels` , can take many different arguments of its own, so we split that off into a separate array, `$labels` , giving us:

Two of the most important arguments are `'supports'` and `'taxomonies'` , because these control which of the native post fields will be accessible in our new post type.

In the above code, we’ve opted for just three `'supports'`:

* `'title'`— the title of each post.
* `'editor'`— the primary text editor, which we’ll use for our description.
* `'thumbnail'`— the post’s featured image.

To see the full list of what’s available, click [here for supports](https://codex.wordpress.org/Function_Reference/post_type_supports), and [here for taxonomies](https://codex.wordpress.org/Custom_Taxonomies#Default_Taxonomies).

Generate WordPress also has [a handy tool to help you code custom post types](https://generatewp.com/post-type/), which can make the process a lot quicker.

#### Changing Title Placeholder Text

If the title placeholder text “enter title here” could be a little misleading for your custom post type, you can edit this in a separate function:

#### Adding a Custom Field to Your Custom Post Type

What if you want a field that doesn’t come pre-defined by WordPress? For example, let’s say we want a special field called “Genre”. In that case, you’ll need to use `add_meta_boxes()` .

For, we need to attach a new function to WordPress’s `add_meta_boxes` hook:

```
add_action( 'add_meta_boxes', 'genre_meta_box' );
```

Inside our new function, we need to call WordPress’s `add_meta_box()` function, like so:

```
function genre_meta_box() {  add_meta_box(    'global-notice',    __( 'Genre', 'sitepoint' ),    'genre_meta_box_callback',    'movies',    'side',    'low'  );}
```

You can read more about this function’s arguments [here](https://developer.wordpress.org/reference/functions/add_meta_box/). For our purposes, the most critical part is the callback function, which we’ve named `genre_meta_box_callback` . This defines the actual contents on the meta box. We only need a simple text input, so we can use:

```
function genre_meta_box_callback() {  global $post;  $custom = get_post_custom($post->ID);  $genre = $custom["genre"][0];  ?>  <input style="width:100%" name="genre" value="<?php   echo $genre; ?>" />  <?php};
```

Finally, our custom field won’t save its value unless we tell it to. For this purpose, we can define a new function `save_genre()` and attach it to WordPress’s `save_post` hook:

```
function save_genre(){  global $post;  update_post_meta($post->ID, "printer_category",   $_POST["printer_category"]);};
```

```
add_action( 'save_post', 'save_genre' );
```

Together, the code used to create the custom field should look something like this:

#### Making Custom Fields Available as JSON

Our custom posts are automatically available as JSON. For our “movies” post type, our JSON data can be found at `localhost/yoursitename/wp-json/wp/v2/movies` .

However our custom fields are not automatically part of this, and so we need to add a function to make sure they are also accessible via the REST API.

First, we’ll need to attach a new function to the `rest_api_init` hook:

```
add_action( 'rest_api_init', 'register_genre_as_rest_field' );
```

Then, we can use the in-built `register_rest_field()` function, like so:

```
function register_genre_as_rest_field() {  register_rest_field(    'movies',    'genre',    array(      'get_callback' => 'get_genre_meta_field',      'update_callback' => null,      'schema' => null,    )  );};
```

This function takes an array with `get` and `update` callback. For a more straightforward use-case like this, we should only need to specify a `'get_callback'` :

```
function get_genre_meta_field( $object, $field_name, $value ) {  return get_post_meta($object['id'])[$field_name][0];};
```

As a whole, here is the code necessary to register a custom field.

#### Making Featured Image URLs Available as JSON

Out-of-the-box, WordPress’s REST API doesn’t include URL for your featured images. To make it easier to access this, you can use the following code:

The WordPress filter `rest_prepare_posts` is dynamic, so we can swap in our custom post type in place of “posts”, such as `rest_prepare_movies` .

#### Restricting Visible JSON Data

We almost ready to start pulling in data to our React app, but there’s one more quick optimisation we can make, by limiting the data that is made available.

Some data comes as standard which you may never need in your frontend and — if that’s the case — we can remove it using a filter, like this one. You can find the names of the data types by looking at your `/wp-json/wp/v2/movies` part of your website.

With that done, once you’ve added a few movies using the WordPress backend, and we have everything we need to start bringing the data into React!

### Part 3: React

![Image](https://cdn-media-1.freecodecamp.org/images/1*qKj1pMwgVFGtOID_wD1N-g.png)

To fetch external data in JavaScript, you need to use promises. This will likely have implications for the way you want to structure your React components, and in my case (converting an existing React project), I had to re-write a fair amount of code.

#### Promises in JavaScript

Promises in JavaScript are used to handle asynchronous actions — things that happen outside the usual step-by-step or “synchronous” order of execution (after hoisting).

The good news is that asynchronous JavaScript is a lot easier than it used to be. Before ES6, we were dependent on callback functions. If multiple callbacks were necessary (and they often were), nesting would lead to code that was very difficult to read, scale and debug — a phenomenon sometimes known as callback hell, or the pyramid of doom!

Promises were introduced in ES6 (or ES2015) to solve that problem, and ES8 (or ES2018) saw the introduction of `async ... await` , two keywords which further simplify asynchronous functionality. But for our purposes, the most critical promise-based method is `fetch()` .

#### The Fetch Method

This method has been available since Chrome 40, and it is an easier-to-use alternative to `XMLHttpRequest()` .

`fetch()` returns a promise and so it is “then-able”, meaning that you can use the `then()` method to process the outcome.

You can add fetch to a method inside your React class component, like so:

```
fetchPostData() {  fetch(`http://localhost/yoursitename/wp-json/wp/v2/movies?per_page=100`)  .then(response => response.json())  .then(myJSON => {  // Logic goes here});}
```

In the code above, two things are important:

* First, we are calling a URL with the filter `?per_page=100` appended onto the end. By default, WordPress only shows 10 items per page, and I often find myself wanting to increase that limit.
* Second, before processing our data, we are using the `.json()` method. This method is used primarily in relation to `fetch()`, and it returns the data as a promise and parses the body text as JSON.

In most cases, we’ll want to run this function as soon as our React component has mounted, and we can specify this using the `componentDidMount()` method:

```
componentDidMount() {  this.fetchPostData();}
```

#### Handling Promises

Once you have returned a promise, you have to be careful about handling it in the correct context.

When I first tried to use promises, I spent a while trying to pass that data to variables outside of the scope of the promise. Here are a few rules of thumb:

* In React, the best way to use promises is via the state. You can use `this.setState()` to pass promise data into your component’s state.
* It is best to process, sort and re-arrange your data within a series of `then()` methods following the initial `fetch()` . Once any processing is complete, it is best practice to add the data to state within your final `then()` method.
* If you want to call any additional functions to process your promise (including within `render()`) it’s good practice to prevent the function from running until the promise has resolved.
* So, for example, if you’re passing your promise to `this.state.data` , you can include a conditional within the body of any functions that depend on it, like below. This can prevent annoying unwanted behaviour!

```
myPromiseMethod() {  if (this.state.data) {    // process promise here   } else {    // what to do before the fetch is successful  }}
```

### A Working Example in React

Let’s say we want to pull in the `name`, `description`, `featured_image` and `genre` of the custom WordPress post type we defined in part 1.

In the following example, we’ll fetch those four elements for each movie and render them.

As so often with React tutorials, the following block of code may look intimidating, but I hope it will seem much simpler when we break it down.

#### constructor(props)

In this method, we call `super(props)`, define our initial state (an empty `data` object) and bind three new methods:

* `fetchPostData()`
* `renderMovies()`
* `populatePageAfterFetch()`

#### componentDidMount()

We want to fetch our data as soon as the component has mounted, so we’ll call `fetchPostData()` in here.

#### fetchPostData()

We fetch the JSON from our URL, passing `.json()` in the first `.then()` method.

In the second `.then()` method, we extract the four values we want for every movie entry we’ve fetched and then add them to our `newState` object.

We then use `this.setState(newState)` to add this information to `this.state.data` .

#### renderMovies()

The conditional `if (this.state.data)` means that the function will only run once data has been fetched.

In here, we take an array of all our fetched movies from `this.state.data` and pass it to the function `populatePageAfterFetch()` .

#### populatePageAfterFetch()

In this function, we prepare the data for each movie to be rendered. This should look straightforward to anyone who’s used JSX, with one potential stumbling block.

The value of `movie.description` is not plain text, but HTML markup. To display this, we can use `dangerouslySetInnerHTML={{__html: movie.description}}` .

**Note:** _The reason this is potentially “dangerous” is that, if your data were hijacked to contain malicious XSS scripts, these would be parsed too. As we’re using our own server/CMS in this article, we shouldn’t need to worry. But if you do want to sanitise your HTML, take a look at [DOMPurify](https://github.com/cure53/DOMPurify)._

#### render()

Finally, we control where our rendered data will appear by calling the `renderMovies()` method within our chosen `<d`iv> tags. We’ve now successfully fetched data from our WordPress site and displayed it!

### Conclusion

Overall, I hope this article makes the process of connecting a React front-end to a WordPress back-end as painless as possible.

Like so much in programming, what can look intimidating to begin with quickly becomes second nature with practice!

I’d be very interested to hear about your own experiences using WordPress as a headless CMS, and I’m happy to answer any questions in the comments.

