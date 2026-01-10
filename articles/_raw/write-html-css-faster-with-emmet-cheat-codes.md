---
title: How to Write HTML/CSS Faster with Emmet Cheat-Codes
subtitle: ''
author: Jesse Hall
co_authors: []
series: null
date: '2020-09-22T17:16:17.000Z'
originalURL: https://freecodecamp.org/news/write-html-css-faster-with-emmet-cheat-codes
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/fCC_-Emmet.png
tags:
- name: efficiency
  slug: efficiency
- name: Productivity
  slug: productivity
- name: 'self-improvement '
  slug: self-improvement
- name: Visual Studio Code
  slug: vscode
seo_title: null
seo_desc: 'Emmet is one of my favorite built-in features of VS Code. It is also available
  as an extension in other code editors.

  Think of Emmet as shorthand. With it, you can easily write a lot of code quickly.
  It dramatically speeds up your HTML & CSS workflow...'
---

Emmet is one of my favorite built-in features of VS Code. It is also available as an extension in other code editors.

Think of Emmet as shorthand. With it, you can easily write a lot of code quickly. It dramatically speeds up your HTML & CSS workflow.

Understanding how to use Emmet is literally a superpower. Some have even called it a coding cheat-code. ?

And it's just one of many amazing built-in features of VS Code.

Recently, I launched a comprehensive and detailed course called [**Become A VS Code SuperHero**](https://courses.codestackr.com/vs-code-superhero?coupon=LAUNCH).\*\*\*\* It covers all aspects of VS Code in great depth.

This article is based on one of the 11 sections of the course: **Writing & Formatting Code**.

## HTML

With Emmet you can quickly create an HTML boilerplate in the blink of an eye. In an HTML file, simply type `!` and you’ll see that Emmet has popped up as a suggestion. Now hit `Enter`. There you have it, a basic, blank HTML web page ready to go.

If you’ve never seen HTML before and have no clue what all of this is, don’t worry. I’m just demonstrating the capabilities of VS Code and Emmet. You don’t have to know what any of this means right now.

### Basic Tags

To create basic HTML tags, just type the tag's name and hit `Enter`. Notice how Emmet puts your cursor inside the tag. You are now set up to continue typing inside the tag.

* Try typing: `div` then `Enter`, or `h1 Enter`, or `p Enter`.
    
* These work as well: `bq` for a `<blockquote>`, `hdr` for a `<header>`, `ftr` for a `<footer>`, `btn` for a `<button>`, and `sect` for a section.
    

### Classes

If you are familiar with CSS, Emmet uses the same way to refer to classes using a `.`. To define a class along with the tag simply add it like this:

* `div.wrapper` —&gt; `<div class="wrapper"></div>`
    
* `h1.header.center` —&gt; `<h1 class="header center"></h1>`
    

### ID’s

Id's work very much the same:

* `div#hero` —&gt; `<div id="hero"></div>`
    

### Combining

You can string these together:

* `div#hero.wrapper` —&gt; `<div id="hero" class="wrapper"></div>`
    

### Attributes

We can also specify attributes for tags:

* `img[src="cat.jpg"][alt="Cute cat pic"]` —&gt; `<img src="cat.jpg" alt="Cute cat pic" />`
    

### Content

To include content within the tag, we simply wrap the content in curly braces, `{ }`.

* `p{This is a paragraph}` —&gt; `<p>This is a paragraph</p>`
    

### Siblings & Children

It just keeps getting better. We can also specify siblings and children using the `+` and `>` characters.

* `section+section` —&gt; `<section></section><section></section>`
    
* `ul>li` —&gt; `<ul><li></li></ul>`
    

### Climbing Up

You have to try to picture what you are building in your head as you type the Emmet shorthand. In this example we'll "climb up" the tree by using `^`.

`div+div>p>span+em^bq`

Result:

```html
<div></div>
<div>
    <p><span></span><em></em></p>
    <blockquote></blockquote>
</div>
```

Here, we wanted the blockquote to be on the same level as the paragraph. Because of that, we needed to "climb up". Otherwise, it would be inside of the paragraph.

### Grouping

If your structure is very complex, you may want to group tags instead of traversing by climbing.

In this example, we'll create a header and footer without climbing using parenthesis `( )`.

`div>(header>ul>li>a)+footer>p`

Result:

```html
<div>
    <header>
        <ul>
            <li><a href=""></a></li>
        </ul>
    </header>
    <footer>
        <p></p>
    </footer>
</div>
```

### Multiplication and $

We can generate multiple tags by multiplying (`*`) and number items in sequence using a dollar sign (`$`).

* `ul>li*5` —&gt; `<ul><li></li><li></li><li></li><li></li><li></li></ul>`
    
* `ul>li{Item $}*3` —&gt; `<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>`
    

You can even customize the numbering sequence by padding with zeros, starting with a specific number, and even reverse direction.

Pad with zeros: `ul>li.item$$$*5`

Result:

```html
<ul>
    <li class="item001"></li>
    <li class="item002"></li>
    <li class="item003"></li>
    <li class="item004"></li>
    <li class="item005"></li>
</ul>
```

Start with a specific number: `ul>li.item$@3*5`

Result:

```html
<ul>
    <li class="item3"></li>
    <li class="item4"></li>
    <li class="item5"></li>
    <li class="item6"></li>
    <li class="item7"></li>
</ul>
```

Reverse direction: `ul>li.item$@-*5`

Result:

```html
<ul>
    <li class="item5"></li>
    <li class="item4"></li>
    <li class="item3"></li>
    <li class="item2"></li>
    <li class="item1"></li>
</ul>
```

Reverse direction from a specific number: `ul>li.item$@-3*5`

Result:

```html
<ul>
    <li class="item7"></li>
    <li class="item6"></li>
    <li class="item5"></li>
    <li class="item4"></li>
    <li class="item3"></li>
</ul>
```

### Implicit Tag Names

There are certain tags that do not need to be typed and can be implied.

* A class defined initially with no tag will be implied as a `<div>`.  
    `.wrapper` —&gt; `<div class="wrapper"></div>`
    
* A class defined within an emphasis tag will be implied as a `<span>`.  
    `em>.emphasis` —&gt; `<em><span class="emphasis"></span></em>`
    
* A class defined within a list will be implied as a list item.  
    `ul>.item` —&gt; `<ul><li class="item"></li></ul>`
    
* A class defined within a table will be implied as a `<tr>` and within a row would be a `<td>`.  
    `table>.row>.col` —&gt; `<table><tr class="row"><td class="col"></td></tr></table>`
    

### Wrap with Tags

There will be times when you have existing code that you want to wrap with a tag. We can do with easily with Emmet.

Just highlight the code that you want to wrap and open the command pallet (`F1`). Then search for `Emmet: Wrap with Abbreviation`. You'll then be presented with a dialog box where you can type in the element.

`test` —&gt; `<div>test</div>`

You can also use standard Emmet syntax in this dialog. Try wrapping some text with `span.wrapper`.

By default, this functionality is not assigned to a keyboard shortcut. So if you find yourself using it often, you may want to add a custom shortcut for it.

### Lorem Ipsum

"Lorem Ipsum" is dummy text used by developers to represent data on a page. Just type `lorem` and hit `Enter`. Emmet will generate 30 words of fake text that you can use as a filler in your project.

The amount of words generated can be defined as well.

* `lorem10` will give you 10 words of random text.
    

### Putting It All Together

Let's use several things that we've learned so far. Give this a try:

`ul.my-list>lorem10.item-$*5`

Result:

```html
<ul class="my-list">
  <li class="item-1">Lorem ipsum dolor sit amet.</li>
  <li class="item-2">Numquam repudiandae fuga porro consequatur?</li>
  <li class="item-3">Culpa, est. Tenetur, deleniti nihil?</li>
  <li class="item-4">Numquam architecto corrupti quam repudiandae.</li>
</ul>
```

## CSS

In CSS, Emmet has an abbreviation for every property. I'm not going to list all of them, but I will point out my most used ones. To see the full list, refer to the Emmet [cheat-sheet](https://docs.emmet.io/cheat-sheet/).

### Position

* `pos` —&gt; `position:relative;` (defaults to relative)
    
* `pos:s` —&gt; `position:static;`
    
* `pos:a` —&gt; `position:absolute;`
    
* `pos:r` —&gt; `position:relative;`
    
* `pos:f` —&gt; `position:fixed;`
    

### Display

* `d` —&gt; `display:block;` (defaults to block)
    
* `d:n` —&gt; `display:none;`
    
* `d:b` —&gt; `display:block;`
    
* `d:f` —&gt; `display:flex;`
    
* `d:if` —&gt; `display:inline-flex;`
    
* `d:i` —&gt; `display:inline;`
    
* `d:ib` —&gt; `display:inline-block;`
    

### Cursor

* `cur` —&gt; `cursor:pointer;`
    

### Color

* `c` —&gt; `color:#000;`
    
* `c:r` —&gt; `color:rgb(0, 0, 0);`
    
* `c:ra` —&gt; `color:rgba(0, 0, 0, .5);`
    
* `op` —&gt; `opacity: ;`
    

### Margin & Padding

* `m` —&gt; `margin: ;`
    
* `m:a` —&gt; `margin:auto;`
    
* `mt` —&gt; `margin-top: ;`
    
* `mr` —&gt; `margin-right: ;`
    
* `mb` —&gt; `margin-bottom: ;`
    
* `ml` —&gt; `margin-left: ;`
    
* `p` —&gt; `padding: ;`
    
* `pt` —&gt; `padding-top: ;`
    
* `pr` —&gt; `padding-right: ;`
    
* `pb` —&gt; `padding-bottom: ;`
    
* `pl` —&gt; `padding-left: ;`
    

### Box Sizing

* `bxz` —&gt; `box-sizing:border-box;`
    

### Width

* `w` —&gt; `width: ;`
    
* `h` —&gt; `height: ;`
    
* `maw` —&gt; `max-width: ;`
    
* `mah` —&gt; `max-height: ;`
    
* `miw` —&gt; `min-width: ;`
    
* `mih` —&gt; `min-height: ;`
    

### Border

* `bd` —&gt; `border: ;`
    
* `bd+` —&gt; `border:1px solid #000;`
    
* `bd:n` —&gt; `border:none;`
    

### Emmet Is Awesome!

With Emmet, you can create a really complex HTML structure with one line. It’s really awesome. And, it also works with CSS.

You can see how Emmet can drastically increase your efficiency and speed when writing HTML and CSS.

If you want to further increase your efficiency and speed while using VS Code, check out my course [**Become A VS Code SuperHero**](https://courses.codestackr.com/vs-code-superhero?coupon=LAUNCH)**.**

The course dives much deeper into these concepts and helps you to become a fast, efficient superhero developer :)

![Jesse Hall (codeSTACKr)](https://www.freecodecamp.org/news/content/images/2020/06/footer-banner-1.png align="left")

I'm Jesse from Texas. Check out my other content and let me know how I can help you on your journey to becoming a web developer.

* [Subscribe To My YouTube](https://youtube.com/codeSTACKr)
    
* Say Hello! [Instagram](https://instagram.com/codeSTACKr) | [Twitter](https://twitter.com/codeSTACKr)
    
* [Sign Up For My Newsletter](https://codestackr.com/)
