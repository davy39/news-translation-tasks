---
title: <img> HTML – Image Tag Tutorial
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-11T15:28:58.000Z'
originalURL: https://freecodecamp.org/news/img-html-image-tag-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/imgTag.png
tags:
- name: HTML
  slug: html
- name: image
  slug: image
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'In HTML, you use the <img> tag to add images to websites. It is an inline
  and empty element, which means that it doesn''t start on a new line and doesn''t
  take a closing tag (unlike the paragraph (<p>) tag, for instance).

  The <img> tag takes several at...'
---

In HTML, you use the `<img>` tag to add images to websites. It is an inline and empty element, which means that it doesn't start on a new line and doesn't take a closing tag (unlike the paragraph (`<p>`) tag, for instance).

The `<img>` tag takes several attributes, of which `src`, `height`, `width`, and `alt` are the most important. 

Knowing the ins and outs along with some best practices of the `<img>` tag is crucial because images can negatively affect your site's load time and SEO. 

So in this tutorial, we will take a look at how to add images to websites using the `<img>` tag, how to use its attributes, some best practices, and modern approaches to using `<img>`.

## Basic HTML `<img>` Tag Syntax

Here's the basic syntax for adding an `<img>` tag to your HTML:

```html
<img 
    src="assets/images/ring-tailed-lemurs.webp" 
    alt="A Group of Ring-tailed Lemurs" 
/>
```

Now let's talk about its attributes and how they work.

## HTML `<img>` Tag Attributes

### The `src` Attribute

The `src` attribute signifies the image source. Without it, the tag itself wouldn't be functional in the real world. 

It indicates to the browser where to find the image. So it takes a relative path if the image is hosted locally, or an absolute URL if the image is hosted online. 

### The `alt` Attribute

The alt attribute specifies an alternative text for the image. This could be the text that shows during a network failure, for example. Or it could display something when the image source is wrongly specified, so users know what the image is about.  

In the code snippet below, the image source is wrongly specified, showing you the role that the `alt` attribute plays:

```html
<img
     src="assets/images/ring-tailed-lemur.webp"
     alt="A Group of Ring-tailed Lemurs"
/>
```

This is the CSS that centers the image horizontally and vertically:

```css
body {
   display: flex;
   align-items: center;
   justify-content: center;
   flex-direction: column;
   height: 100vh;
  }
```

And it looks like this: 
![alt-text-1](https://www.freecodecamp.org/news/content/images/2021/08/alt-text-1.png)

The alt attribute is very important for 2 other reasons:

- SEO: it indicates to web crawlers what the image is about
- Accessibility: it helps screen readers know what the image is about so they can report that to visually impaired people. In addition, it lets users with low bandwidth know what the image is about.

### The `width` and `height` Attributes

You can use these attributes to specify a certain width and height for your images. With these attributes, you can resize the image down or up. 

Ideally, though, you shouldn't resize an image with these attributes. We'll touch on this more under best practices.

## HTML `<img>` Tag Best Practices

### Do not resize an image with the width and height attributes.

This is a bad practice because it can make the image appear distorted and can affect the quality. 

Instead, you can optimize the image to your desired dimensions with photo editing software such as Photoshop. 

In the code snippet below, I specify a width and height for the image – a bad practice:

```html
<img
      src="assets/images/ring-tailed-lemurs.webp"
      height="440px"
      width="440px"
      alt="A Group of Ring-tailed Lemurs"
/>
```

The image looks like this:
![wrong-width-height-usage-1](https://www.freecodecamp.org/news/content/images/2021/08/wrong-width-height-usage-1.png)

Without using the width and height attributes, the image looks like this:
![no-width-height-1](https://www.freecodecamp.org/news/content/images/2021/08/no-width-height-1.png)

Looks better? Yes!

### Name Your Images Appropriately

Naming images appropriately can help search engines understand what the image is about. For example, name an image `ring-tailed-lemurs.webp` instead of `photo-1580855733764-084b90737008.webp`. The latter is not enough for search engine optimization (SEO).

### Reduce Image File Size

The image's file size is crucial when it comes to page speed. A smaller image size (that preserves the image's quality) reduces load time while larger images take forever to load. 

There are several tools and various software that can help you do this. Some examples are imageOptim, jStrip, and PNGGauntet. And if you're concerned about SEO, you'll want to look into these – as page speed is an important ranking factor.

### Host Images with a CDN

Imagine if a website is hosted in the United States but a user in Africa wants to accessed it. Assets such as images and icons would have to travel from The States to Africa, which in turn slows download time.

Using a CDN (Content Delivery Network) will allow the website's images to be cached across several locations around the world. The CDN can then serve them from locations closest to the user, improving load time and providing a better user experience. 

Cloudflare is a popular CDN that a lot of developers use to host their images.

### Use Descriptive Alternative Text

Using descriptive alternative text helps search engines understand what the image is about. But it doesn't end there – the alt text must also be relevant to the image. 

For example, use this:

```html
<img
   src="assets/images/ring-tailed-lemurs.webp"
   alt="A Group of Ring-tailed Lemurs"
/>
```

Insead of this:

```html
<img src="assets/images/ring-tailed-lemurs.webp" alt="Lemurs" />
```

### Use the `title` Attribute to Show Tooltips

Just like the `alt` attribute, you can use the `title` attribute to show additional information about the image. Browsers display this as a tooltip when the user hovers over the image.

```html
<img
    src="assets/images/ring-tailed-lemurs.webp"
    alt="A Group of Ring-tailed Lemurs"
    title="Ring-tailed lemurs are led by females"
/>
```

![tooltip-1](https://www.freecodecamp.org/news/content/images/2021/08/tooltip-1.png)

## `<img>` Tag Modern Approaches

There are various ways you can use the `<img>` tag that are a bit more up to date and modern. Let's look at some of them now.

### Lazy Load Images

Lazy loading is a newish "load what is needed" concept. With lazy loading, the image is loaded only when the user scrolls to its viewport. 

This is in contrast to eager loading, which loads every image immediately after the page is rendered by the browser. 

To apply lazy loading, add the loading attribute to the `<img>` tag and set the value to “lazy”.

```html
<img
      src="assets/images/ring-tailed-lemurs.webp"
      alt="A Group of Ring-tailed Lemurs"
      title="Ring-tailed lemurs are led by females"
      loading="lazy"
/>
```

Images are often quite high quality and large these days, but this can negatively impact user experience and SEO – hence the introduction of lazy loading. 

### Use the `<figure>` and `<figcaption>` Tags

Often, you might need to specify to the user the caption of an image. A lot of developers do this by placing a `<p>` tag right after the `<img>`. 

This might not be wrong, but it defies best practices and does not associate the caption with the image, so search engines won’t understand what it is. 

```html
<img
      src="assets/images/ring-tailed-lemurs.webp"
      alt="A Group of Ring-tailed Lemurs"
      title="Ring-tailed lemurs are led by females"
      loading="lazy"
/>
<p>Ring-tailed lemurs are social animals</p>
```

![wrong-captioning-1](https://www.freecodecamp.org/news/content/images/2021/08/wrong-captioning-1.png)

Its is clear that there is no association between the image and the caption in the above example.

HTML5 introduced the `<figure>` and `<figcaption>` elements to help with this. You wrap the `<img>` tag inside a `<figure>` element, and you specify a caption within the `<figcaption>` element. 

This helps search engines associate the caption with the image, leading to better performance and SEO. 

The snippets of code below and the screenshots show you an image with and without the `<figure>` and `<figcaption>` elements:

```html 
<figure>
   <img
     src="assets/images/ring-tailed-lemurs.webp"
     alt="A Group of Ring-tailed Lemurs"
     title="Ring-tailed lemurs are led by females"
     loading="lazy"
   />
<figcaption>Ring-tailed lemures are social animals</figcaption>
</figure>
```

![right-captioning](https://www.freecodecamp.org/news/content/images/2021/08/right-captioning.png)

You can see now that the image and the caption are beautifully associated.

### Use the .webP Image Format

.webP is an image format created by Google. According to the creator, it's an image format lower in size than its counterparts - JPG, JPEG, PNG, but with the same quality. 

This format has been getting more and more widely accepted and is considered the nextgen image format for the web.

## Conclusion

I hope this article helps you understand how the `<img>` tag works in HTML so you can use it properly in your projects. If you do so, it'll help improve your user experience and SEO.

Thanks a lot for reading, and keep coding.   


