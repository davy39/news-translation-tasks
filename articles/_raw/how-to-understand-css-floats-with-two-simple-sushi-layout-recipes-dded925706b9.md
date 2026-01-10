---
title: How to understand CSS floats with two simple sushi layout recipes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-25T14:27:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-understand-css-floats-with-two-simple-sushi-layout-recipes-dded925706b9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OyZdQ37Bw7O86Br_2gZgXA.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Anabella Spinelli

  A few weeks ago I decided I should admit to all the things I’ve never understood
  about basic CSS. I would try to do a deep and conscious dive into them and get them.
  It seemed that now, more than a couple years after learning abo...'
---

By Anabella Spinelli

A few weeks ago I decided I should admit to all the things I’ve never understood about basic CSS. I would try to do a deep and conscious dive into them and _get_ them. It seemed that now, more than a couple years after learning about CSS for the first time, I could use all the experience I’ve gathered to my advantage. This time it should be easier and clearer.

I also thought to myself: _I cannot be the only one struggling with these properties for the Nth (or first) time._ Documenting my journey into the most elusive of CSS properties would make a great bunch of articles that others could leverage.

Last month I kicked it off with an [intro to the mysterious pairings of the position property](https://medium.freecodecamp.org/an-intro-to-the-mysterious-pairings-of-css-position-flavors-92b3625176ea). Here’s my second stop in the journey:

The `float` property, in the form of cooking recipes.

#### Recipes Index

* **Sushi rows** — make elements cover a full row in an even manner
* **Clearing broth** — make content found below the floats act normally

### Sushi rows ?

We'll use floats and percentage values to distribute elements evenly in the full (container) width. Just like sushi rows in a plate.

#### Ingredients:

* 1 container or board
* Some sushi pieces you need to distribute side-by-side.
* The `%` sign
* 1 `float: left;`

#### Instructions:

Prepare your sushi pieces, that is, the elements you want to be displayed in a row. They could be makis, item cards, nigiris, icons, whatever suits your taste.

You can also add any non-positioning styling to them: colors, text-alignment, fonts, soy sauce.

Put them inside a **block** container, like a board. In its most basic form, this should be a div (but you can use any other HTML5 semantic elements such as header, footer, section, article, main). Add a descriptive class for them. I’ll be using `nigiri`.

Now, on class `nigiri` we'll apply some styles, including our `**float: left;**`. Take a moment and read through them:

What `**float: left;**`does is tell every element to stick to one side — in this case, left — and stand next to each other in a left-to-right row.

Note that we're adding `height` to the board. Normally we wouldn’t need this: the board would expand to fit whatever is in it. But floating elements, like our nigiris, are different. They don’t occupy real Document space and don’t affect other, non-floating elements. That’s why we’re using a fixed, pixel-sized height for the board.

Now, you should see all your elements on a single row. But something’s not quite right. They’re all piling up on the left and you probably have a lot of empty space on the right side of your board.

We need to space them evenly.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PTeK-2AbKxznolPfgWC6JQ.jpeg)

We can do that by setting the nigiri's width to be relative to their container (the board in this case) using a percentage value.

**Now this is the tricky part**: the % you need to set will depend on 3 things

* how many items you have
* how they’re structured inwardly (padding)
* and how much space you want between them.

Do you want them to stick to each other side by side or do they need some margin in between them? If the sushi pieces have _rice **padding**_**,** that will cause them to be bigger than their content. You’ll have to compensate that by decreasing their width. For this it’s also advisable to use % in the padding values.

I know al this can be confusing. Here’s a handmade single-press illustration that I hope can illustrate it clearly.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vEajpTwwxymHQr89D8ez1Q.jpeg)
_Each nigiri is 33.33% of the board’s full width: 2% for margin on each side, 2% for padding on each side and then 29.33% of their actual width._

But this is a recipe, not a math lesson. To make it easier for you, dear readers, here are some common combinations for shoulder-to-shoulder and margin-spaced elements, all with 1% rice padding:

You may have noticed the pattern here: we’re assuming elements come with 1% of **padding**. They need to compensate that by subtracting 2% (1% for each side) from the element’s percentage width. Same goes for our 1% **margin** breather. Now it makes more sense to not use 33.33% width for 3 elements in a row. Instead set it to 29.33% after leaving 2% the padding and 2% for the margin on each.

Sigh… that was _a lot_ of math_._ Ok so now, no matter how many pieces your sushi roll gets chopped in, you know how to present them nicely in a board.

If you want to play around with this setup, here's [a CodePen](https://codepen.io/andiemusik/pen/OwRVMK) specially made for that.

_And if you like CSS sushi, don't miss Sasha Tran's very inspiring [CSS Sushi Board](https://codepen.io/sashatran/pen/bgZVdm)._

### Clearing broth ?

The perfect soup to have with some floating sushi, while making sure your portions don’t end up swimming in it.

#### Ingredients:

* One container or board with floating sushi
* A soup or broth to follow after it.
* One `clear: broth;`

#### Instructions:

Once you have your row of floating sushi pieces ready, place your soup container below them in the html.

Our sushi is meant to gracefully float "above" the Document flow and not affect other elements. If we’re not careful they might just end up floating in soup and sushi-ramen is not something the world is ready for.

Remember that floating elements don’t have real Document height. This also means that they don’t “push” the soup down. Now look at this horrific mess:

To prevent this atrocity, we need to add our `clear: broth;`… I mean `**both**;`!

We have two options here:

We can simply put the soup in a bowl or container and give the bowl a style of `clear: both;`. This will sort of get the job done, _but_ it will result in things like `**margin-top**` not working at all on the bowl.

So if we want the sushi pieces to be completely protected from soup flooding — and not lose any features in the way — we need them to be contained in a plate with a high edge. To achieve that we’ll add an `**:after**` _pseudo-element_ to the sushi plate (that is, the container of our little floaters):

Here below there's another example for you play around with. I’ve made the plate visible using height and background color. Even though that’s **not** necessary for the soup to be well placed, it just makes it look fancier ?

Think of this as making the sushi dish have a very high southern wall in order to prevent any soup from flooding in. But… like… a _nice_ wall.

_All right, I’m super glad that you made it this far and I hope this tiny recipe book helped you get a better idea on how floats work… and how **we** can work with floats. Stay tuned for more deep-dive-into-basic-but-elusive-things like this_ ?

