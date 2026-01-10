---
title: How to Indent HTML Code – And Why it's Important
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-06-01T15:40:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-indent-in-html-and-why-it-is-important
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/irvan-smith-ymn_TY_MBn8-unsplash.jpg
tags:
- name: freeCodeCamp Curriculum Guide
  slug: freecodecamp-curriculum-guide
- name: best practices
  slug: best-practices
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'When you are building out HTML files, it''s really important to indent
  your code. But how do you do that in HTML and why is it important?

  In this article, I will show you how to properly indent your HTML files and explain
  why it is important to proper...'
---

When you are building out HTML files, it's really important to indent your code. But how do you do that in HTML and why is it important?

In this article, I will show you how to properly indent your HTML files and explain why it is important to properly format your code. 

## How to Indent Your Code in HTML

Whenever you have HTML elements nested inside other HTML elements, it's best to use indentation. Nested elements  are known as children of their parent element.

In this example, I have a `p` element nested inside a `div` element.  To indent the `p` element, I will move it two spaces to the right.

```html
<div>
  <p>This is what indentation looks like for HTML</p>
</div>
```

This is considered best practice and will make your code more readable by other developers.  Now we can see that the `p` element is nested inside its parent element which is the `div`. 

In this next example, I have an `h2` and `p` element nested inside a `main` element **without** indentation.

```html
<main>
<h2>Let's learn about indentation</h2>
<p>There is no indentation here</p>
</main>
```

But if I edit the code by moving the `h2` and `p` elements two spaces to the right, now we have proper indentation.

```html
<main>
  <h2>Let's learn about indentation</h2>
  <p>This is indentation</p>
</main>
```

The `h2` and `p` elements are children of the `main` element.

## Commonly Used Examples of Indentation in HTML

### Unordered lists

The `li` elements are indented two spaces to the right and nested inside the `ul` element. The `ul` element is the parent of the `li` elements.

```html
<ul>
  <li>Cake</li>
  <li>Pizza</li>
  <li>Salad</li>
  <li>Apple</li>
</ul>
```

### Ordered lists

The `li` elements are indented two spaces to the right and nested inside the `ol` element. The `ol` element is the parent of the `li` elements.

```html
<ol>
  <li>Drive 1.2 miles and turn left on Cherry lane</li>
  <li>Drive 4.5 miles and turn right on Sycamore Rd.</li>
  <li>Drive 400 feet and stop at the light</li>
  <li>Turn left at the light</li>
  <li>Arrive at the destination on your right</li>
</ol>
```

## Why is Indentation Important?

When you are writing code, it is important to write code that is readable by other developers. A large part of readability is properly indenting your HTML. 

In this example, I have copied all of the code from the [Learn HTML by Building a Cat Photo App](https://www.freecodecamp.org/learn/2022/responsive-web-design/#learn-html-by-building-a-cat-photo-app) project and removed all of the indentation to show you what poor code formatting looks like. 

```html
<html lang="en">
<head>
<title>CatPhotoApp</title>
</head>
<body>
<h1>CatPhotoApp</h1>
<main>
<section>
<h2>Cat Photos</h2>
<!-- TODO: Add link to cat photos -->
<p>
Click here to view more
<a target="_blank" href="https://freecatphotoapp.com">cat photos</a>.
</p>
<a href="https://freecatphotoapp.com"
><img
src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg"
alt="A cute orange cat lying on its back."
/></a>
</section>
<section>
<h2>Cat Lists</h2>
<h3>Things cats love:</h3>
<ul>
<li>cat nip</li>
<li>laser pointers</li>
<li>lasagna</li>
</ul>
<figure>
<img
src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/lasagna.jpg"
alt="A slice of lasagna on a plate."
/>
<figcaption>Cats <em>love</em> lasagna.</figcaption>
</figure>
<h3>Top 3 things cats hate:</h3>
<ol>
<li>flea treatment</li>
<li>thunder</li>
<li>other cats</li>
</ol>
<figure>
<img
src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg"
alt="Five cats looking around a field."
/>
<figcaption>Cats <strong>hate</strong> other cats.</figcaption>
</figure>
</section>
<section>
<h2>Cat Form</h2>
<form action="https://freecatphotoapp.com/submit-cat-photo">
<fieldset>
<legend>Is your cat an indoor or outdoor cat?</legend>
<label
><input
id="indoor"
type="radio"
name="indoor-outdoor"
value="indoor"
checked
/>
Indoor</label
>
<label
><input
id="outdoor"
type="radio"
name="indoor-outdoor"
value="outdoor"
/>
Outdoor</label
>
</fieldset>
<fieldset>
<legend>What's your cat's personality?</legend>
<input
id="loving"
type="checkbox"
name="personality"
value="loving"
checked
/>
<label for="loving">Loving</label>
<input id="lazy" type="checkbox" name="personality" value="lazy" />
<label for="lazy">Lazy</label>
<input
id="energetic"
type="checkbox"
name="personality"
value="energetic"
/>
<label for="energetic">Energetic</label>
</fieldset>
<input
type="text"
name="catphotourl"
placeholder="cat photo URL"
required
/>
<button type="submit">Submit</button>
</form>
</section>
</main>
<footer>
<p>
No Copyright -
<a href="https://www.freecodecamp.org">freeCodeCamp.org</a>
</p>
</footer>
</body>
</html>

```

This is not good HTML practice at all because it is really difficult to read and understand what the code is doing. If you tried to submit something like this in a professional developer setting, your team would not be happy with you at all.

Now I am going to take that exact same code and properly indent it to show you the difference. 

```html
<html lang="en">
  <head>
    <title>CatPhotoApp</title>
  </head>
  <body>
    <h1>CatPhotoApp</h1>
    <main>
      <section>
        <h2>Cat Photos</h2>
        <!-- TODO: Add link to cat photos -->
        <p>
          Click here to view more
          <a target="_blank" href="https://freecatphotoapp.com">cat photos</a>.
        </p>
        <a href="https://freecatphotoapp.com"
          ><img
            src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg"
            alt="A cute orange cat lying on its back."
        /></a>
      </section>
      <section>
        <h2>Cat Lists</h2>
        <h3>Things cats love:</h3>
        <ul>
          <li>cat nip</li>
          <li>laser pointers</li>
          <li>lasagna</li>
        </ul>
        <figure>
          <img
            src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/lasagna.jpg"
            alt="A slice of lasagna on a plate."
          />
          <figcaption>Cats <em>love</em> lasagna.</figcaption>
        </figure>
        <h3>Top 3 things cats hate:</h3>
        <ol>
          <li>flea treatment</li>
          <li>thunder</li>
          <li>other cats</li>
        </ol>
        <figure>
          <img
            src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg"
            alt="Five cats looking around a field."
          />
          <figcaption>Cats <strong>hate</strong> other cats.</figcaption>
        </figure>
      </section>
      <section>
        <h2>Cat Form</h2>
        <form action="https://freecatphotoapp.com/submit-cat-photo">
          <fieldset>
            <legend>Is your cat an indoor or outdoor cat?</legend>
            <label
              ><input
                id="indoor"
                type="radio"
                name="indoor-outdoor"
                value="indoor"
                checked
              />
              Indoor</label
            >
            <label
              ><input
                id="outdoor"
                type="radio"
                name="indoor-outdoor"
                value="outdoor"
              />
              Outdoor</label
            >
          </fieldset>
          <fieldset>
            <legend>What's your cat's personality?</legend>
            <input
              id="loving"
              type="checkbox"
              name="personality"
              value="loving"
              checked
            />
            <label for="loving">Loving</label>
            <input id="lazy" type="checkbox" name="personality" value="lazy" />
            <label for="lazy">Lazy</label>
            <input
              id="energetic"
              type="checkbox"
              name="personality"
              value="energetic"
            />
            <label for="energetic">Energetic</label>
          </fieldset>
          <input
            type="text"
            name="catphotourl"
            placeholder="cat photo URL"
            required
          />
          <button type="submit">Submit</button>
        </form>
      </section>
    </main>
    <footer>
      <p>
        No Copyright -
        <a href="https://www.freecodecamp.org">freeCodeCamp.org</a>
      </p>
    </footer>
  </body>
</html>

```

This is much easier to read and now we can see all of the nested child elements inside their parent elements and understand what the code is doing.

## Conclusion

When writing HTML it is important to properly format your code using good indentation. You can indent elements by moving them two spaces to the right. 

```html
<main>
  <h2>Let's learn about indentation</h2>
  <p>This is indentation</p>
</main>
```

This will make your code more readable by other developers and shows the relationship between the child and parent HTML elements. 

I hope you enjoyed this article and best of luck on your developer journey. 

