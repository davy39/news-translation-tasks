---
title: Common Accessibility Errors and How To Fix Them
subtitle: ''
author: Ilknur Eren
co_authors: []
series: null
date: '2022-01-05T21:15:24.000Z'
originalURL: https://freecodecamp.org/news/common-accessibility-errors-and-how-to-fix-them
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/accessibility-errors-article-image.jpeg
tags:
- name: a11y
  slug: a11y
- name: Accessibility
  slug: accessibility
seo_title: null
seo_desc: 'The Web Content Accessibility Guidelines, or WCAG, defines how to make
  websites accessible for people with disabilities.

  When we evaluate whether or not website is accessible, we look to see if software
  meets WCAG 2 standards.

  Accessibility should no...'
---

The Web Content Accessibility Guidelines, or WCAG, defines how to make websites accessible for people with disabilities.

When we evaluate whether or not website is accessible, we look to see if software meets WCAG 2 standards.

Accessibility should not be an after thought, but rather a major part of the development process. Still, sadly these days there are many websites with accessibility errors.

[WCAG's audit](https://webaim.org/projects/million/#errors) shows that many accessibility errors fall into just six areas/categories.

<table><tbody><tr><td colspan="1" rowspan="1"><p></p></td><td colspan="1" rowspan="1"><p></p></td><td colspan="1" rowspan="1"><p></p></td><td colspan="1" rowspan="1"><p>Most common types of WCAG 2 failures</p></td></tr><tr><th colspan="1" rowspan="1"><p>WCAG Failure Type</p></th><th colspan="1" rowspan="1"><p>% of home pages in February 2021</p></th><th colspan="1" rowspan="1"><p>% of home pages in February 2020</p></th><th colspan="1" rowspan="1"><p>% of home pages in February 2019</p></th></tr><tr><td colspan="1" rowspan="1"><p>Low contrast text</p></td><td colspan="1" rowspan="1"><p>86.4%</p></td><td colspan="1" rowspan="1"><p>86.3%</p></td><td colspan="1" rowspan="1"><p>85.3%</p></td></tr><tr><td colspan="1" rowspan="1"><p>Missing alternative text for images</p></td><td colspan="1" rowspan="1"><p>60.6%</p></td><td colspan="1" rowspan="1"><p>66.0%</p></td><td colspan="1" rowspan="1"><p>68.0%</p></td></tr><tr><td colspan="1" rowspan="1"><p>Missing form input labels</p></td><td colspan="1" rowspan="1"><p>54.4%</p></td><td colspan="1" rowspan="1"><p>53.8%</p></td><td colspan="1" rowspan="1"><p>52.8%</p></td></tr><tr><td colspan="1" rowspan="1"><p>Empty links</p></td><td colspan="1" rowspan="1"><p>51.3%</p></td><td colspan="1" rowspan="1"><p>59.9%</p></td><td colspan="1" rowspan="1"><p>58.1%</p></td></tr><tr><td colspan="1" rowspan="1"><p>Missing document language</p></td><td colspan="1" rowspan="1"><p>28.9%</p></td><td colspan="1" rowspan="1"><p>28.0%</p></td><td colspan="1" rowspan="1"><p>33.1%</p></td></tr><tr><td colspan="1" rowspan="1"><p>Empty buttons</p></td><td colspan="1" rowspan="1"><p>26.9%</p></td><td colspan="1" rowspan="1"><p>28.7%</p></td><td colspan="1" rowspan="1"><p>25.0%</p></td></tr></tbody></table>

> 96.7% of all errors detected fall into these six categories. Addressing just these few types of issues would significantly improve accessibility across the web. – [WebAIM](https://webaim.org/projects/million/#errors)

If we tackle these six problems, we can make sure more websites are accessible for people who use various of assistive technologies.

Let's look at each of these common accessibility problems in more detail.

## Update Low Contrast Text

%[https://codepen.io/ilkxeren/pen/qBPVRxL] 

In the code example above, we can see an example of one background/foreground color combo that meets WCAG standards and one that doesn't.

The low color contrast is the one with blue background and gray text. It's really hard to differentiate the background and foreground colors visually and the color combination does not meet WCAG standards. The foreground text blends into the background.

In the second example, the foreground is whitish color and it's easy to read the text. This color combination meets WCAG standard, and the text stands out on its own and is easy to read.

If the text color is hard to differentiate from the background it's in, we have a low contrast accessibility error. Over the last three years, by far the biggest accessibility error is low contrast text. More than 80% of websites have this accessibility error.

You can fix low contrast accessibility errors by simply auditing your website and changing the color of the text or the background. You can [run a lighthouse test](https://developers.google.com/web/tools/lighthouse) to see if color contrast is an issue on your website.

You can also check if the background/foreground color combo meets WCAG standards in the following link: [https://webaim.org/resources/contrastchecker/](https://webaim.org/resources/contrastchecker/).

## Add Missing Alternative Text for Images

In 2021, it was reported that 60.6% of all home page images were missing alternative text.

It's important to add alternative text to images because you need to describe the content of the page to those who cannot see the content. Visually impaired users will use a screen reader, which will read the content of the page back to them.

For example, if we have an image of a basket of Belgium fries, we can add an alternative tag to that image with a simple alt attribute:

`<img src="example.png" alt="basket of fries"/>`

With one attribute, `alt`, we are able to make the image accessible for screen reader users. When a screen reader user tabs over to the image, it will indicate to them that they are focused on an image and that image is a "basket of fries".

If we didn't have an alt attribute, then the screen reader user wouldn't have known that the image they were focusing on was a basket of fries.

It's also important to note that an `alt` attribute is not enough for 100% accessible images. We also need to make sure that the alt tag is descriptive and lets the user know what the image looks like.

A bad example of an alt tag would be if it's not descriptive enough. Say we have the same image of the basket of fries and we add alt tag to the image like so:

`<img src="example.png" alt="image"/>`

In the example above, we would meet accessibility standards by adding the alt tag, but the alt tag is not helpful or descriptive enough for screen reader users. When a screen reader user focuses on this image, it will say, "image, image", which doesn't let the user know what this image is at all.

It's very important to add descriptive alternative tag to images on the page.

## Add Missing Form Input Labels

About half of the websites were missing form input labels in 2021. A form label is an HTML element used in forms to describe what the the various fields in the form are for.

If you have any type of form on the page, whether it's checkbox, radio button or dropdown, you must have a `<label>` associated with this form.

A common error for missing form input is for search forms. Often search forms on a page usually have only a magnifying glass image to indicate to visual users that they can search with that form, but no label to indicate search. But if we don't add a label to this form, screen reader users will not know what the form is when they focus on it.

We can fix this accessibility error by adding a screen reader label.

HTML example:

```php
<label for="searchLabel" class="sr-only">Search</label>
<input type="text" name="search" id="searchLabel>
<input type="submit" value="Search">
```

CSS example:

```php
.sr-only{
   position:absolute;
   left:-10000px;
   top:auto;
   width:1px;
   height:1px;
   overflow:hidden;
}
```

In the example above, we added a label "Search" to the form with the help of CSS. When a user focuses on this particular form, the screen reader will read, "Search", to them. The class `sr-only` in this form will only make this element readable when on a screen reader.

## Fix Empty Links

Links are used to navigate the user to a new page or view. A link is focusable by keyboard and can be triggered by the enter key.

Similar to the missing form label error, another accessibility error is empty links. About half of the websites had empty links in 2021.

For example, if we use the Facebook logo to indicate to sighted users that the link is to go to Facebook, but we don't add any label for screen reader users, then we will get an empty link accessibility error.

If we don't add text for screen readers, then screen reader users will not know that they are focused on a Facebook logo.

A good example of adding a label to a link is below:

```php
<a href="/facebook-page">
   <i aria-hidden="true"></i>
   <span class="sr-only">Facebook</span>
</a>
```

CSS correspondent:

```php
.sr-only{
   position:absolute;
   left:-10000px;
   top:auto;
   width:1px;
   height:1px;
   overflow:hidden;
}
```

In the example above, we used a Facebook logo to indicate that this is a Facebook link. We also added "Facebook" text that will be read when users focus on it using a screen reader.

## Add Missing Document Language

For the last three years, between 28% to 33% of homepages have been missing a document language on their page. This is one of the less common accessibility problems but it is still an accessibility error we should pay attention to and fix.

We can add the language to the HTML tag like so:

```php
<html lang="en">
...
</html>
```

The example above indicates that the page is in English. We can use other codes to indicate other languages.

It's important to indicate the language of the page because screen readers use the document language to know how to pronounce the words. Document language is also good for SEO.

## Fix Empty Buttons

Buttons are used to do things on a page, for example submitting a form or show/hide things. A button is focusable and can be triggered by the space key.

Similar to empty links, we need to make sure that buttons have text for screen readers to read when on focus.

The solution for fixing empty buttons is similar to fixing empty links, which is to make sure text label is present on buttons.

If an image is used inside button, we can add an alt tag to the image. This will ensure that when a user uses a screen reader, the image alt tag is read. Here's an example of how to do this below:

```php
<button type="submit">
   <img src="/search.svg" alt="Search"/>
</button>
```

Similarly to an image, if you use an SVG inside a button, you can add a title inside the SVG. Here's an example of how to do this below:

```php
<button type="submit">
   <svg id="search" role="img" aria-describedby="search" viewBox="0 0 16 16.9">
      <title id="search">Search</title>
      <path d="M14, 2L8690, 89.1,13,6.5G87"></path>
   </svg>
</button>
```

We need to make sure that buttons are not empty and that screen readers read what the button is to the user.

## Conclusion

Accessibility should never be an afterthought, but rather a large part of the development process. Most accessibility errors come from six categories and if we fix them, we will make our websites more accessible to everyone.

Accessibility fixes should not be difficult and should only require basic HTML and CSS knowledge.

If we pay more attention to accessibility, we will open our websites to a wider audience and also make sure our code is good and meets standards. Accessibility not only helps everyone use websites but also improves the foundation of our code.
