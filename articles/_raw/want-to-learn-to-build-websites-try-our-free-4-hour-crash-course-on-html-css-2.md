---
title: Want to learn to build websites? Try our free HTML & CSS crash course
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-10T10:02:09.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-to-build-websites-try-our-free-4-hour-crash-course-on-html-css-2
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/Want_to_learn_to_build_websites__Try_our_free_HTML__-CSS_crash_course.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Per Harald Borgen

  I''m excited to share this four hour course on HTML and CSS with you (<– link to
  course).

  If you''re curious about web development, but don''t know where to start, this is
  the perfect course for you!

  There are absolutely no prerequi...'
---

By Per Harald Borgen

I'm excited to share this four hour [course on HTML and CSS with you](https://scrimba.com/g/ghtmlcss?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=ghtmlcss_launch_article) (<– link to course).

If you're curious about web development, but don't know where to start, this is the perfect course for you!

There are absolutely no prerequisites for it, and you don't even need to install a code editor! Scrimba will cover you there.

The instructor of the course is the brilliant [Kevin Powell.](https://www.kevinpowell.co/) He's a big CSS fan, a very popular YouTube instructor, and he also teaches HTML and CSS in classrooms. In other words, you're in good hands.

During the course, you're going to learn the basics of HTML and CSS and start building your very first web pages. All the lessons are going to be hands-on and start writing actual code straight away. 

Once you've completed this course, and are ready for more challenges, you can check out Kevin's [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=ghtmlcss_launch_article) as well. It's a massive 15-hour course that teaches you advanced CSS and how to build responsive websites on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ghtmlcss_launch_article)_

But for now, let's have a closer look at the lessons in the intro course.

# 1. Introduction

![Image](https://thepracticaldev.s3.amazonaws.com/i/fjx5n9tuqopauujrhdo6.png)

In the first lesson, Kevin gives a little introduction to what you can expect for the course, and some tips for learning as much as you can from it.

# 2. What are HTML and CSS?

![Image](https://thepracticaldev.s3.amazonaws.com/i/4mw48ltdwgaduyydecld.png)

In the second cast, Kevin introduces us to HTML and CSS, what these acronyms stand for and how both HTML and CSS are closely intertwined.

# 3. Basic Terminology and Syntax

Kevin uses a book as an example of how HTML markup works and introduces such concepts as `elements` and `tags`, and how to use them.

# 4. Let's write some HTML!

In this screencast, Kevin introduces `<!DOCTYPE html>` to let browser know that the content is HTML and we write our first HTML webpage and learn some fundamental elements along the way!

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My first website</title>
  </head>

  <body>
    <h1>My very first webpage</h1>
    <h2>Websites are built with HTML</h2>
    <p>HTML is a markup language that tells the browser what everything is</p>
    <h2>They also use CSS</h2>
    <p>I can't wait to start learning CSS!</p>
  </body>
</html>

```

# 5. `strong` and `emphasis`

We can use `<em>` to add _emphasis_ to our text and `<strong>` to add **importance**.

# 6. File naming and organization

In this part, Kevin teaches us some good practices around file naming and gives good advice on how to organise our files.

# 7. Anchors and Attributes

We can use anchor `<a>` element to link to a different location on the same page or to another page. To tell `<a>` where to link, we use `attributes`, and for anchors, it's `href`.

```html
<a href="https://scrimba.com">Link to Scrimba</a>

```

# 8. Intro to CSS

Kevin introduces us to CSS syntax and the notion of properties and values in CSS. How using `property: value` syntax we can style our webpages and introduces _inline_ styling to make individual elements look good on the page.

# 9. CSS Basics

In this video, we're going to learn about font size, colours, background colours and text alignment. Kevin will introduce us to four different ways of specifying colours in CSS, using keywords, `hex`, `rgb` and `hsl` values.

# 10. Practice time!

Ok, time for some individual practice. Kevin sets us a task to create a page about ourselves and sets us some HTML/CSS challenges along the way.

```html
<!--
HTML
  - h1 (the title of the page)
  - An introductory paragraph
  - Two h2s, each followed by a few paragraphs
  - Inside the paragraphs, use strong and emphasis tags
  - If you are feeling adventurous add a second page and link to it

CSS
  - Change the color of the h1
  - Change the text alignment of the h1
  - Change the color of the h2s
  - Change the font-size of the paragraphs
  - If you added a link, change the color of it
 -->

```

# 11. Recap up until this point

In this cast, we quickly go over everything we've learned about HTML and CSS up until this point. Repetition is the mother of learning!

# 12. Lists

Now, Kevin shows us how to create lists in HTML using `<ol>` for ordered lists and `<ul>` for unordered lists.

```html
<ol>
  <li>List item one</li>
  <li>a second list item</li>
</ol>

<ul>
  <li>bullet point</li>
  <li>another bullet</li>
</ul>

```

![ol and ul tags rendered to show the difference between the two](https://thepracticaldev.s3.amazonaws.com/i/corow6lf3d1ghgvz2jyv.png)
_[Click here to go to the cast](https://scrimba.com/p/pvwJdCn/cnZ3dnAJ?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ghtmlcss_launch_article)_

# 13. Images

![Image](https://thepracticaldev.s3.amazonaws.com/i/44kc9bv0c71dsgjw66xc.png)

Images are self-closing and both `<img>` are valid `<img />`. Kevin also explains how to use `src` and `alt` attributes and how `alt` helps improve accessibility.

```html
<img
  src="images/dog-in-blanket.jpg"
  alt="a dog wrapped in a blanket sitting on the road"
/>

```

# 14. Practice time!

Alright, time for our second practice screencast. Kevin sets us a challenge to convert some markdown files to HTML/CSS webpage. No worries if you're not sure what `markdown` is because in this practice session Kevin will walk us through the completion of the task.

# 15. Internal CSS

In this chapter, Kevin introduces internal CSS, an alternative to writing inline CSS.

Internal CSS is written in the same file as HTML, but within a separate `<style>` tag

```html
<!DOCTYPE html>
<html>
  <head>
    <title>All about Earth and Mars</title>
    <style>
      h1 {
        font-size: 60px;
      }

      p {
        font-size: 24px;
        color: steelblue;
      }
    </style>
  </head>
  <body>
    <h1>Earth and Mars</h1>
    <p>Earth and Mars are two planets within our solar system.</p>
  </body>
</html>

```

![Rendered code above with styles applied](https://thepracticaldev.s3.amazonaws.com/i/85yb8c9wg9zqnxx3psvb.png)
_[Click here to go to the cast](https://scrimba.com/p/pvwJdCn/cbWKNeuE?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ghtmlcss_launch_article)_

# 16. External CSS

External CSS is another approach to managing CSS. This time Kevin shows us how we can extract CSS into a separate file and how to link CSS stylesheets to our HTML files with a `<link>` tag

```html
<link href="css/style.css" rel="stylesheet" />

```

# 17. Classes and IDs

In this screencast, Kevin focuses on three types of selectors in CSS and when you might want to use which.

```css
/* Element selector  */
a {
  color: darksalmon;
}

/* Class selector  */
.intro {
  font-size: 24px;
}

/* ID selector  */
#earth-title {
  color: lightgreen;
}

```

# 18. Comments in HTML and CSS

We can add comments in HTML:

```html
<html>
  <head>
    <title>Comments!</title>
    <link rel="stylesheet" href="css/style.css" />
  </head>
  <body>
    <h1>Comments!</h1>
    <!-- My comment goes here -->
  </body>
</html>

```

And in CSS:

```css
/* TODO: change the color of the text to white */

body {
  background: #333;
  color: white;
}

/* Some more comments */

h1 {
  color: red;
}

```

# 19. The only tags you need to know (for now)

In this part of the course, Kevin reminds us that we don't need to know everything at this point and at this stage we really need to know only the following tags:

```txt
h1 -> h6
p
strong and em
a
ul, ol, li
img

```

And it would be good if we can tell the difference between the following tags:

```txt
header
main
section
footer
nav
div

```

# 20. Intro to the box model

It's now time to discover the _box model_.  
Most elements are block elements, which means they are 100% width of their parent and have a height of 0.

This is a brilliant cast, where Kevin not just simply and succinctly explains how the box model works, but also saves us from the common pitfalls that even experienced developers fall into from time to time.

# 21. Margin and Padding

Up next are margins and paddings.  
Margins are used to control the position of an element **relative to those around it**, while padding is used to control the positioning of content **inside** our element.  
Kevin does a great job explaining many different ways padding and margins can be set in CSS.

```css
/*  */
padding-top: 20px;
padding-right: 30px;
padding-bottom: 40px;
padding-left: 50px;

/* Shorthand version would be */
padding: 20px 30px 40px 50px;

margin-top: 500px;
margin-left: 100px;
margin-right: 100px;
margin-bottom: 10px;

/* Shorthand version would be */
margin: 500px 100px 10px;

```

# 22. Borders

The last piece in the box model - borders. Borders are added around your elements. And they can be set in a similar way to margins and padding.

```css
border-color: yellow;
border-width: 20px;
border-style: solid;

/* Shorthand version would be */
border: solid yellow 20px;

```

# 23. Box model wrap up

In this chapter, Kevin helps us review CSS box model and provides a nice visualisation for future reference.

![Visualisation of the CSS box model](https://thepracticaldev.s3.amazonaws.com/i/j3j3hgaarut1pxh7npdk.png)
_[Click here to go to the cast](https://scrimba.com/p/pvwJdCn/cWQVDPCJ?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ghtmlcss_launch_article)_

# 24. A basic layout

We are now ready to create a very basic layout.

![Example of page layout](https://thepracticaldev.s3.amazonaws.com/i/od8w5yem96ap94ngjg30.png)
_[Click here to go to the cast](https://scrimba.com/p/pvwJdCn/cbWmpeC9?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ghtmlcss_launch_article)_

Kevin will guide us through creating a page about dinosaurs, where we will be able to put everything we've learned so far to practice.

# 25. A basic layout - centring an element on the page

In this chapter, Kevin shows us how to centre the main element. It's not too difficult, but there are a few tricky bits to it.

![Example of page layout with centred main element](https://thepracticaldev.s3.amazonaws.com/i/p93ejs4zuebprkgw3lil.png)
_[Click here to go to the cast](https://scrimba.com/p/pvwJdCn/ckdDNKAV?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ghtmlcss_launch_article)_

# 26. Creating columns with flexbox

We are doing pretty well, so far.

Over these last cast, Kevin introduces a mini-capstone project to create this HTML layout from scratch.

![Capstone project layout, the task](https://lh5.googleusercontent.com/oVRWavp2Y-omJxn6A1JfXqOLnYL3sdO7DejsRCY5o2xF0vhoDkA0g5RWuvebxhJXNkCfKvVcrfRfGWh-Mr04Duirxe2hDy4nwGZpSdey6iDtzCcW7E5z-4t15QifHq5b0U81)
_[Click here to go to the cast](https://scrimba.com/p/pvwJdCn/cZnGZDc8?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ghtmlcss_launch_article)_

Oftentimes, a lot of designs use columns in the footer. In this cast, Kevin shows us how to use `display: flex` to create this neat layout.

![Zoomed in footer, implemented using flexbox columns](https://thepracticaldev.s3.amazonaws.com/i/pqpjcl7dzrx5ifvl51xp.png)
_[Click here to go to the cast](https://scrimba.com/p/pvwJdCn/cZnGZDc8?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ghtmlcss_launch_article)_

# 27. Creating the layout from scratch - the HTML

In this screencast, Kevin slices the design into manageable pieces and walks us through the HTML implementation.

![Capstone layout with highlighted boxes around sections of the layout](https://thepracticaldev.s3.amazonaws.com/i/ywet3byo1ipn6y831lg9.png)
_[Click here to go to the cast](https://scrimba.com/p/pvwJdCn/cdPK6BCv?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ghtmlcss_launch_article)_

In this screencast, we are creating the HTML markup.  


![The layout is written in just HTML](https://thepracticaldev.s3.amazonaws.com/i/yhsyvzem21iuoeqdja7g.png)
_[Click here to go to the cast](https://scrimba.com/p/pvwJdCn/cdPK6BCv?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ghtmlcss_launch_article)_

# 28. Creating the Layout - The CSS

And in the final part of this course, we're writing CSS to create the final layout.

![Capstone project layout, finished](https://lh5.googleusercontent.com/oVRWavp2Y-omJxn6A1JfXqOLnYL3sdO7DejsRCY5o2xF0vhoDkA0g5RWuvebxhJXNkCfKvVcrfRfGWh-Mr04Duirxe2hDy4nwGZpSdey6iDtzCcW7E5z-4t15QifHq5b0U81)
_[Click here to go to the cast](https://scrimba.com/p/pvwJdCn/cqR8k6cN?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ghtmlcss_launch_article)_

# 29. What's next?

![You rock! poster](https://thepracticaldev.s3.amazonaws.com/i/zmrq0v0ipp319fdzxcqo.png)

If you reach all the way to this cast, then give your self a pat on the back. Congratulations on finishing the course! We've covered a LOT, and you have every reason to be proud of yourself.

Where can you go from here? Kevin's first recommendation is to install a text editor. Any of them at this stage would be good and you can always change later. VS Code is very popular and for a good reason.

You should also keep an eye on Kevin's upcoming advanced course on how to build responsive websites, so be sure to [sign up for Kevin's newsletter](https://www.kevinpowell.co/newsletter/).

Happy coding :)

---

Thanks for reading! My name is Per Borgen, I'm the co-founder of [Scrimba](https://scrimba.com/?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=ghtmlcss_launch_article) – the easiest way to learn to code. You should check out our [responsive web design bootcamp](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=ghtmlcss_launch_article) if want to learn to build modern website on a professional level.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Click here to get to the advanced bootcamp.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=ghtmlcss_launch_article)_

