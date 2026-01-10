---
title: HTML List – How to Use Bullet Points, Ordered, and Unordered Lists
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2021-07-01T18:02:56.000Z'
originalURL: https://freecodecamp.org/news/html-list-how-to-use-bullet-points-ordered-and-unordered-lists
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/freeCodeCamp-Cover-1.png
tags:
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Listing items on a web page is a common task you''ll have to do as a web
  developer. You may have to list shopping cart items, the order of students based
  on their grades, dogs with the loudest bark – and so on.

  So you need to know the different ways y...'
---

Listing items on a web page is a common task you'll have to do as a web developer. You may have to list shopping cart items, the order of students based on their grades, dogs with the loudest bark – and so on.

So you need to know the different ways you can list items using HTML. While you might think it's a trivial thing to learn, it's important. And it's one of the most commonly used features of HTML in web development.

In this article, you'll learn all about HTML listing elements, their properties, styling, and how to actually use them to create neat lists. I hope you find it helpful.

# How to Make Lists in HTML

In HTML, we can list items either in an ordered or unordered fashion. 

An ordered list uses numbers or some sort of notation that indicates a series of items. 

For example, an ordered list can start with number 1, and continue through 2, 3, 4, and so on. Your ordered list can also start with the letter A and go through B, C, D, and so on.

Here is an example of an ordered list with students' names and marks.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/ordered-1.png)
_Ordered list of students_

On the other hand, we have unordered lists, like a TODO list for example. Here I am so passionate about coding that I skipped my breakfast 🤓.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/unordered-1.png)
_Unordered TODO list_

There is one more type of list called a `description list` that we will learn as well below.

Now let's get into a bit more detail and see how to create each type of list in HTML.

# How to Make an Ordered List with HTML

In HTML, we can create an ordered list using the `<ol>` tag. The `ol` in the tag stands for an **o**rdered **l**ist. Inside each of the ordered list elements `<ol>` and `<ol />`, we have to define the list items. We can define the list items using the `<li>` tag. 

Here is the complete HTML structure for an ordered list:

```html
<ol>
  <li>Eat</li>
  <li>Code</li>
  <li>Sleep</li>
</ol>
```

The output of the above ordered list is:

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image.png)

So, we have the list of elements ordered with a number starting with 1 and incremented to 2 and 3. Try this CodePen and see if you can change and play around with using `ol-li`.

%[https://codepen.io/atapas/pen/gOWpbMK]

### Types of Ordered Lists in HTML

What if you do not want to order your list by number? Instead, you want to order using the alphabet like A, B, C or a,b,c. You can do these by specifying the value of the `type` attribute of the `<ol>` tag.

You can order the list using A, B, C letters by passing `A` as the type value.

```html
<ol type="A">
  <li>Eat</li>
  <li>Code</li>
  <li>Sleep</li>
</ol>
```

The output looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-10.png)

Similarly, you can use lower case letters like `a` as the type value to list the elements with a, b, c, and so on.

```html
<ol type="a">
  <li>Eat</li>
  <li>Code</li>
  <li>Sleep</li>
</ol>
```

Here's the output:

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-2.png)

If you want to use Roman numerals, use the value `I` for an ordered list with Roman numerals:

```html
<ol type="I">
  <li>Eat</li>
  <li>Code</li>
  <li>Sleep</li>
</ol>
```

The output looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-3.png)

Check out the CodePen below to try other types:

%[https://codepen.io/atapas/pen/LYyVEbL]

## How to Use the Start Attribute in HTML Lists

The `<ol>` element has an interesting attribute called `start`. You can specify a value to the start attribute to start the ordered list from a specific number. 

Let's say you want to start the list with the number `30` instead of `1`. You can specify the number `30` as the value of the `start` attribute like this:

```html
<ol start="30">
  <li>Thirty</li>
  <li>Thirty One</li>
  <li>Thirty Two</li>
</ol>
```

The output looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-4.png)

Feel free to play around with the `start` attribute using this CodePen:

%[https://codepen.io/atapas/pen/VwbLYzQ]

Incidentally, I have shared the same tips on Twitter recently. You may find some interesting discussion there as well:

%[https://twitter.com/tapasadhikary/status/1410508936344588289]

# How to Make an Unordered List in HTML

Let's move over to unordered lists now. We use the `<ul>` tag to create an unordered list. As usual, we need to use the `<li>` tags within `<ul>` and `<ul/>` to create the list items. 

The list items (`li`) inside the unordered list (`ul`) come with the default style of bullet points – so each of the list items is preceded by a black dot.

Let's create a list of my favorite online resources to learn about web programming:

```html
My Favorite Web Development Learning Sites
<div>
  <ul>
    <li>freeCodeCamp</li>
    <li>CSS-Tricks</li>
    <li>Traversy Media</li>
  </ul>
</div>
```

The output looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-5.png)

You can see the bullet points for each of the list items above, but you can customize them. We'll learn that too. 

But before that, feel free to use this CodePen to change and run the code.

%[https://codepen.io/atapas/pen/zYwxgJw]

## How to Use Bullet Points with Links in HTML Lists

We can use the links (anchor tag `<a>`) in the list items (`<li>` tag) to link each of the items to any internal or external web pages. 

Here is an example that shows you how to link each of the web programming resources to their respective websites: 

```html
My Favorite Web Development Learning Sites
<div>
  <ul>
    <li>
      <a href="https://www.freecodecamp.org/" target="_blank">freeCodeCamp</a>
    </li>
    <li>
      <a href="https://css-tricks.com/" target="_blank">CSS-Tricks</a>
    </li>
    <li>
      <a href="https://www.traversymedia.com/" target="_blank">Traversy Media</a>
    </li>
  </ul>
</div>
```

The output looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-6.png)

You can use the CodePen below to try out the same. Feel free to modify it as you wish:

%[https://codepen.io/atapas/pen/yLbNBmj]

## Types of Unordered Lists in HTML

As we discussed briefly, we can customize the bullet point style of an unordered list, which we will see in action now. We can do this using the CSS style property called `list-style`.

There are four main values of the `list-style` property that help us with this customization:

| list-style      | Effect  |
| -------------   | -----:|
| none            | There will not be any bullets appearing in front of the list item |
| circle          | A circular (hollow) bullet appears in front of the list item   |
| disc            | This is the default filled circular bullet     |
| square          | A filled square bullet appears in front of the list item |

%[https://codepen.io/atapas/pen/vYmOYyK]

You can use the CodePen above to try out different `list-style` options.

# Did You Know – There is a Description List, Too?

There is one more type of HTML list, but it's not used as often. It is called `Description List`. 

We can define a description list using the `<dl>` tag element. Inside the `<dl>..</dl>` we need to define a description term using the `<dt>` tag. The term is usually some small text about something. Then, we can define the description descriptor to describe the term further using the `<dd>` tag.

Too much to digest? Let's see how it works with a code example. 

Let's assume that we want to describe some information about coding, gossiping, and sleeping on our webpage. We can first define a `<dl>` tag. Now we define three pairs of `<dt>` and `<dd>` tags to describe coding, gossiping, and sleeping respectively. 

```html
<dl>
  <dt>Coding</dt>
  <dd>An activity to keep you happy, even in sleep.</dd>
  <dt>Gossiping</dt>
  <dd>Can't live without it.</dd>
  <dt>Sleeping</dt>
  <dd>My all time favorite.</dd>
</dl>
```

The output looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-7.png)

Try out this CodePen to experiment further with description lists:

%[https://codepen.io/atapas/pen/xxdGbzL]

You must be wondering, why don't we use this type of list much? Well, you can create this structure using the unordered list (ul), list items (li), and the CSS styles. 

But if you consider the HTML semantics, you should give a place to description lists in your code when you have a good use-case for it.

# How to Create a Page Header with HTML List Elements

We're almost at the end of this tutorial. But I feel like it's incomplete without at least one use-case example of the HTML lists and tags. My favorite one is listing the items in the header of a web page.

Let's create a very basic header with a sample logo and three links: `Home`, `Products`, and `About Us`. We will first create the HTML structure like this:

```html
<nav>
  <span class="logo">Logo</span>
  
  <ul>
    <li><a href="#/home">Home</a></li>
    <li><a href="#/products">Products</a></li>
    <li><a href="#/about">About Us</a></li>
  </ul>  
</nav>
```

Here we have taken an unordered list with three list items to define Home, Products, and About Us links. You'll also notice a span element with the text Logo which indicates it is a logo. We can use a suitable image there, based on our needs later. 

So far, the header should look like this:

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-8.png)

Well, this is not what we want. So next we will write a few CSS rules and properties to make it look like a page header (at least close to it).

```css
nav{
  background-color: #273032;
  color: #FFF;
  padding: 10px;
  display: flex;
}

.logo {
  background-color: blue
}

ul {
  margin: 0px;
}

li {
  list-style: none;
  display: inline;
  margin-right: 0.2rem;
}

a {
  color: pink;
}
```

Now it is much better and looks closer to a realistic page header.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-9.png)

Again, you can use this CodePen to change and try out things with the header.

%[https://codepen.io/atapas/pen/OJmVPGe]

# Before We End...

That's all for now. I hope you've found this article insightful, and that it helps you understand HTML lists more clearly. You can find all the examples together in this [CodePen Collection](https://codepen.io/collection/jbOYRo?sort_by=item_created_at&grid_type=list).

Let's connect. You will find me active on [Twitter (@tapasadhikary)](https://twitter.com/tapasadhikary). Feel free to give a follow. I've also started sharing knowledge using my [YouTube channel](https://youtube.com/c/TapasAdhikary?sub_confirmation=1), so you can check it out, too.

You may also like these articles:

* [10 DevTools tricks to help you with CSS and UX design](https://blog.greenroots.info/10-devtools-tricks-to-help-you-with-css-and-ux-design-ckpp7mtnu04u6whs143e7huwx)
* [10 trivial yet powerful HTML facts you must know](https://blog.greenroots.info/10-trivial-yet-powerful-html-facts-you-must-know-ckmx0d7q30346c1s125iydcsa)
* [10 useful HTML5 features, you may not be using](https://blog.greenroots.info/10-useful-html5-features-you-may-not-be-using-ckdua7ql300l1m3s1ez7teshc)




