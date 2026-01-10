---
title: How to Set Width Ranges for Your CSS Media Queries
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-06T16:32:00.000Z'
originalURL: https://freecodecamp.org/news/media-queries-width-ranges
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/amirali-mirhashemian-jh5XyK4Rr3Y-unsplash-1.jpg
tags:
- name: CSS
  slug: css
- name: responsive design
  slug: responsive-design
seo_title: null
seo_desc: 'By Caleb Olojo

  A media query is a feature of CSS. It lets you create and implement layouts that
  adapt to the properties of the device you''re using. Some of these properties include
  the height and width of a page.

  In this short guide, you''ll see how y...'
---

By Caleb Olojo

A media query is a feature of CSS. It lets you create and implement layouts that adapt to the properties of the device you're using. Some of these properties include the height and width of a page.

In this short guide, you'll see how you can set multiple width properties in a media query rule. For now let's take a look at the fundamentals first.

## How Media Queries Work in CSS

Now that you have a basic idea what a media query is, let's take a look at how this particular feature of CSS actually works.

A basic media query looks like this:

```css
@media only screen and (max-width: 576px) {
    // do something
}

@media only screen and (min-width: 576px) {
    // do something again
}
```

This means that the styles that would be written inside the media rules above will only work or be effective at the width properties specified above.

Literally, you're saying that at this particular width (that is, the `max-width` property of `576px`), CSS please apply the styles that I will be writing here to this width alone, from an initial width of `0px`.

## max-width and min-width properties

There are two things you need to keep in mind when you're creating media queries for different screen sizes: the `max-width` and `min-width` properties.

When a `max-width` property is passed into a media query, CSS interprets it as a width starting from zero – that is if no minimum width property has been set yet. We'd get to that soon.

Once the `max-width` property gets a value assigned to it, all the styles within that particular media query will be applied to any device whose screen size spans from `0px` to the specified maximum width.	  
  
The `min-width` property, on the other hand, takes the initial value that you have assigned to it and applies the styles within the media rule until the next `max-width` is provided. Say for example:

```css
@media only screen and (min-width: 576px) {
    // apply the styles here from this minimum width of 
    // 576px (medium screen sized devices)
}
```

The styles that would be written in the media query above would only be applicable to devices that fall within the minimum width specified and above.

## How to Set the width-range for a Media Query

The method we just discussed of creating media queries by applying just one `width` property solves just one problem. 

By setting a "width-range", you have a certain amount of flexibility when creating layouts that gives you responsiveness across all device widths.

Setting a particular "width-range" isn't any different from the way media queries are created. The only difference is the addition of more media feature expressions (that is, the screen width sizes).

Take a look: 

```css
@media only screen and (min-width: 360px) and (max-width: 768px) {
	// do something in this width range.
}
```

The media query above will only work for the feature expression (the screen size of the mobile device that you're writing a style for) provided above.  
  
It takes the first width expression provided as the initial value and the second as the final value. 

Remember how we saw the difference between the `max-width` and `min-width` property above? We're simply telling the browser to apply the CSS styles that we'll write inside this rule to mobile devices with screen sizes from `360px` to `768px`. 

In basic terms, we're building layouts that will be responsive from small device widths to medium widths, like tablets or mobile devices. 

You can take a look at some media breakpoints that are available in [Bootstrap's documentation](https://getbootstrap.com/docs/5.0/layout/breakpoints/). Try playing with them by setting the screen size ranges that you prefer.

## Try Media Queries Out with Flexbox

You've seen how to create a basic media query that takes in multiple screen size expressions. And you've seen the difference between the `max-width` and `min-width` properties and how to apply them.

In this section, we'll be looking at how to create a simple layout whose appearance changes at different media breakpoints (screen sizes). We'll start by creating the markup that would hold the layout.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Media query example</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div class="container">
      <div class="boxes box1">
        <h1>First Box</h1>
        <p>
		Information in the first box
        </p>
      </div>
      <div class="boxes box2">
        <h1>Second Box</h1>
        <p>
          Information in the second box
        </p>
      </div>
  </body>
</html>

```

The snippet above will display two boxes with their respective information when the styles are applied. You can view the full code example [here](https://gist.github.com/Caleb335/ed730da8fb43af4d29b0a1368f5e112b), if you want to.

```css
.container {
  display: flex;
  flex-wrap: wrap;
  width: 980px;
  margin: 0 auto;
  margin-top: 40px;
}

@media only screen and (min-width: 320px) and (max-width: 576px) {
  .container {
    width: 100%;
    padding-left: 23px;
    flex-direction: column-reverse;
  }
  .boxes {
    width: 100%;
  }
}
```

Taking a look at the CSS file, you'll notice that the media query has a minimum width of `320px` and a maximum width of `576px`. This just means that all the styles that will go into this rule will only be applicable to devices with extra-small and small widths.

The layout of the boxes also changes in this particular width range. That's due to the `.container` selector having its `flex-direction` property changed from `row` to `column-reverse`.

You can decide to experiment with the other values that can be assigned to the `flex-direction` property. Check them out [here](https://www.w3schools.com/cssref/css3_pr_flex-direction.asp).   

## Conclusion

Without setting a width range, the CSS styles of the snippet [above](#max-width-and-min-width) will be applied to all devices with a minimum screen size of `576px` and above.

When you set a width range, you get better control as a developer. You'll be able to specify which styles should be applied to a device with a particular screen size which gives your app better responsiveness.

Thank you for reading this article. Kindly share it if it has helped you grasp why you should set width ranges when creating media queries.

