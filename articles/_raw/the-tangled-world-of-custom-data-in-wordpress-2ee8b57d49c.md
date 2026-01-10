---
title: The Tangled World of Custom Data in WordPress
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-02T01:07:07.000Z'
originalURL: https://freecodecamp.org/news/the-tangled-world-of-custom-data-in-wordpress-2ee8b57d49c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZdgftYvXborZxb4LL_WW8g.jpeg
tags:
- name: PHP
  slug: php
- name: Quality Software
  slug: quality-software
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: WordPress
  slug: wordpress
seo_title: null
seo_desc: 'By Kamil Grzegorczyk

  Reducing Risk and Managing Your Custom Fields


  source https://pixabay.com

  Have you ever wondered how to properly name keys of WordPress custom fields? Does
  it make any difference? Should you care? What are the potential risks?

  Re...'
---

By Kamil Grzegorczyk

#### Reducing Risk and Managing Your Custom Fields

![Image](https://cdn-media-1.freecodecamp.org/images/T7IWEtq6emQ8ewTaeh51rey6BLxOwcWWD9E8)
_source https://pixabay.com_

Have you ever wondered how to properly name keys of [WordPress](https://wordpress.org) custom fields? Does it make any difference? Should you care? What are the potential risks?

Recently I wrote a tutorial about filtering WordPress admin views. In the code, I named custom fields key like `kg_order_items`. You could ask why? Why not name it just `items`? Well… read below!

If you try to google for naming custom fields there is not so much information about it. Even the [Codex entry](https://codex.wordpress.org/Custom_Fields) tells nothing about naming the field keys in a proper way. I found only [one resource at ACF forums](https://support.advancedcustomfields.com/forums/topic/best-practice-for-name-the-fields/) that contains proper information.

If there is no problem, what is the fuss about? You could ask.

![Image](https://cdn-media-1.freecodecamp.org/images/FPg2xCt4KCRLjf4JzMlakYO1-fuN8qhrY63B)
_Found on [http://dilbert.com](http://dilbert.com" rel="noopener" target="_blank" title=")_

The days when WordPress was a simple CMS supporting small blog websites with only posts and pages are gone. Today even the smallest website uses a plethora of plugins and complex themes. And all of them bring new custom fields into the game.

The situation gets even worse if you use any of the fancy “premium” themes. Unfortunately, many of these are not well written and combine 1001 functions in one. Final result? Slow, not performant, and tangled site which looks nice only on demo content and stock images. And they **add a lot** of custom fields too.

### Danger!

![Image](https://cdn-media-1.freecodecamp.org/images/m8se5ytEdXwvEddSjmVS3dVkmvy4XZ2x0TCr)
_Source unknown_

WordPress `wp_postmeta` table is very simple. It is a key-value pair attached to particular post_id. It means that all **custom fields keys share a common namespace**. That is especially true for the particular ID of the post.

**First example**  
a) Imagine that your post has a “learn more” link. After you click the link it redirects you to a particular URL. The address is provided in a custom field. Let’s name the field key as `redirect_to`.

b) Now imagine that you install a plugin called for example “Redirect me, Honey”. The plugin is very, very simple. When the user enters the page it immediately redirects the user based on custom field setting attached to a post. Oh… and its field key is named `redirect_to` as well.

Result? After you activate the plugin, all of your posts with “learn more” button are redirecting users out of your website. And the reason why is not obvious at the first sight. It may even be unnoticed for quite a while.

This scenario is, of course, made up but the dangers are real. With thousands of plugins and thousands of themes available it’s just a matter of time to encounter such name collision.

**Second example**  
WordPress can store multiple values for the same key name and post ID. (Unless you provide special parameter called `$unique`).

It means that if you save your data 5 times under the key `location` you will receive an array consisting of 5 elements when calling `get_post_meta().`

Let’s assume that you have a post about the cities you have visited. You have been to 5 cities and those locations are shown on the embedded map in the post. Simple, right?

Attention! Not useful code ahead. ;) !

```
//NYadd_post_meta($post_id, 'location', '40.7127753, 73.989308'); 
```

```
//LAadd_post_meta($post_id, 'location', '34.0522342, -118.2436849');
```

```
//Parisadd_post_meta($post_id, 'location', '48.856614, 2.3522219000000177'); 
```

```
//Viennaadd_post_meta($post_id, 'location', '48.2081743, 16.37381890000006'); 
```

```
//Romeadd_post_meta($post_id, 'location', '41.90278349999999, 12.496365500000024');
```

```
//Lets check what we have herevar_dump(get_post_meta($post_id, 'location');
```

```
array (size=5)0 => string '40.7127753, 73.989308' (length=21)1 => string '34.0522342, -118.2436849' (length=24)2 => string '48.856614, 2.3522219000000177' (length=29)3 => string '48.2081743,16.37381890000006' (length=28)4 => string '41.90278349999999,12.496365500000024' (length=36)
```

What if after a while you use a new theme or plugin. It has a feature which can set the position of a post on a front page. You can pick between slider, sidebar or featured posts etc. This scenario may end up like this:

```
array (size=6) 0 => string ‘40.7127753, 73.989308’ (length=21) 1 => string ‘34.0522342, -118.2436849’ (length=24) 2 => string ‘48.856614, 2.3522219000000177’ (length=29) 3 => string ‘48.2081743,16.37381890000006’ (length=28) 4 => string ‘41.90278349999999,12.496365500000024’ (length=36) 5 => string ‘left_sidebar’ (length=12) // Yeah, right…
```

Or even worse:

```
array (size=5)  0 => string 'left_sidebar' (length=12)  1 => string 'left_sidebar' (length=12)  2 => string 'left_sidebar' (length=12)  3 => string 'left_sidebar' (length=12)  4 => string 'left_sidebar' (length=12)
```

Your pretty little map **is broken now!** And you lost all of your entered data. Not funny right?

![Image](https://cdn-media-1.freecodecamp.org/images/UVx09NmJbiPAIBJ1GJ7CgaDLvClyDxRghgYS)
_B-b-b-b-roken?? ;( source https://pixabay.com_

### Solution

You can never protect your custom fields data from being overwritten or deleted. This is how WordPress works and why it is so flexible. **You can reduce that risk though**.

**How?**  
By avoiding common names and namespacing **all** your custom fields keys.

My proposed convention is:

* **cpt-name_field-name**   
like `books_author` instead of `author`, `order_items` instead of `items`(solution for most lazy ones :) ).
* **purpose_field-name**  
like `front_page_location` instead of location, `visited_cities_locations`instead of `location`.
* **prefix_(cpt-name/purpose)_field-name**   
like `kg_books_author`, `kg_visited_cities_locations` (for the most strict ones).

That is not all. Additionally, you should always take care of optional parameters of built-in WordPress functions:

* [add_post_meta()](https://codex.wordpress.org/Function_Reference/add_post_meta) has `$unique` to not add the custom field if it already exists.
* [get_post_meta()](https://developer.wordpress.org/reference/functions/get_post_meta/) uses `$single` to retrieve only one record (if you expect only one record).
* [update_post_meta()](https://codex.wordpress.org/Function_Reference/update_post_meta) and [delete_post_meta()](https://codex.wordpress.org/Function_Reference/delete_post_meta) leverage `$previous_value` to ensure that you update/delete the key you want.

Those parameters are helping in writing better, cleaner and more predictable code.

And that is not all. Use well tested, well written and extendable plugins like [Pods Framework](https://pods.io/) or [Advanced Custom Fields](https://www.advancedcustomfields.com/). These will help manage your custom fields. They are great when it comes to managing the tangled world of your custom data.

### Summary

In the ideal world, we should always be aware of what you are adding to the system. We should know what your plugins, themes, and custom functions are doing. That is unfortunately not always possible.

Therefore we should pay attention to the code we produce and tighten up all those loose ends.

That is all folks! I hope you liked it and have a great day!

This post was originally published on [my private blog](https://kamilgrzegorczyk.com/2017/10/12/best-practices-naming-convention-for-wordpress-custom-fields/) where I write about WordPress and development in general.

