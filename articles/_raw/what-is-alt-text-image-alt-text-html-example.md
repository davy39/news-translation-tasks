---
title: What is Alt Text? Image Alt Text HTML Example
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-09-16T20:39:17.000Z'
originalURL: https://freecodecamp.org/news/what-is-alt-text-image-alt-text-html-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/cover-template--1-.jpg
tags:
- name: Accessibility
  slug: accessibility
- name: HTML
  slug: html
- name: image
  slug: image
seo_title: null
seo_desc: 'Images play a significant role on our web pages. They help explain concepts
  better, make our web pages visually attractive, and lots more.

  In HTML, you use the <img> tag to embed an image into your web page.

  This <img> tag has two required attributes...'
---

Images play a significant role on our web pages. They help explain concepts better, make our web pages visually attractive, and lots more.

In HTML, you use the `<img>` tag to embed an image into your web page.

This `<img>` tag has two required attributes: `src` to specify the path to the image, and `alt` to specify an alternate text for the image. The `alt` attribute is there in case, for some reason (maybe wrong image path), the image doesn't get displayed.

```html
<img src="/my-image.jpg" alt="This is the alt text for my image">
```

Although the `alt` attribute is required in the `<img>` tag, many people decide to leave it empty or type some text that doesn't not correlate with the image to make sure it has text.

Most developers pay little or no attention to the alt text because they don't know its usefulness, and most tutorials fail to highlight its importance.

In this article, you will understand what alt text means, what it does, and how useful it is when embedding an image in your webpage. We will also highlight a few points to consider when writing alt text for your images.

## What is Alt Text?

Alternative or alt text is also referred to as an alt attribute. It is concise, descriptive text that accurately describes an image.

By default, this text is not shown when you view a web page in the browser. Still, in a situation where you cannot view an image for some reason, the alt text becomes visible. This text should be informative and descriptive enough to give the reader or user a sense of what the image is about and what message it conveys.

For example, if you have an image like this:

![Image by Erik-Jan Leusink on Unplash](https://paper-attachments.dropbox.com/s_95E44C54B681F0DAF38695280E5CE127D3338A54647F8EF9DBA670394BC64304_1663348516195_cat.avif align="left")

Rather than giving it a random alt text like "cat" or "Sleeping cat", you can be more descriptive and specific by adding alt text like "A Cat sleeping on a blanket" or "A Cat dozing on on a blanket".

```html
<img src="/imgs/cat-sleeping.jpg" alt="A Cat sleeping on a blanket">
```

## Why is Image Alt Text Important?

The alt attribute is required for the `<img>` tag, which is one reason you should add it to your images.

But there are several other reasons why you should not only consider adding alt text but rather descriptive and informative alt text to your images:

1. When you have connectivity issues or your image's path is incorrectly declared, your image may not be loaded to your webpage. In this case, the alt text value is shown in the place of the image.
    
2. The alt text provides the descriptive meaning of an image that search engines can use to improve your web page's SEO. It gives search engines better information to rank your web page with, meaning having proper alt text will help your web page rank higher.
    
3. Visually impaired users who use screen readers can hear a description of the image. This shows how useful it is to enhance accessibility for people who can't see the screen.
    
4. When you want to link your image to another page or document, the alt text is used as the anchor text when the image fails to load.
    

## Tips for Writing Good Alt Text

A famous saying is that "anything worth doing is worth doing well". The same basically applies to writing your alt text – it is better not to write alt text than to write bad or meaningless alt text.

Here are a few tips to bear in mind when writing your alt text:

### Accurately describe the image

The main aim of writing alt text is that it is able to stand as an alternative for an image (like when the images fail to display or for screen readers).

For alt text to serve its purpose, it must adequately and accurately describe the image.

One helpful tip is to think of a way to describe an image to a user who cannot see the image or as if you were describing it to someone over the phone. Then write the alt text that way.

### Keep it short

At this point, you might begin to think that these alt texts would end up being in the form of a paragraph – but they should't be. In most cases, we should always look for the best way to explain and describe our images in a few words.

Always remember that screen readers may cut off alt text at around 125 characters, so it's best to stick within that limit. Still, you should also always avoid using a single word as alt text.

For example, in the image below, we can see a man standing on an elevated rock looking at the sky with his hands stretched out:

![image by Joshua Earle on unsplash](https://images.unsplash.com/photo-1454942901704-3c44c11b2ad1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80 align="left")

A poor alt text would be "Man standing" or "Man looking at sky". Better alt text would involve adding more descriptive information like "Man standing on top of rock mountain during golden hour" or "Man standing on top of a rock mountain and looking at the sky", and so on.

**Note:** There are always many ways to describe an image, but always think of a better way to describe your images to someone who cannot see the image, making your text short but precise.

### Use keywords but avoid keyword stuffing

When describing an image, the keyword should not be your top priority. Instead, you should focus on truthfully describing your image.

Although having your keywords in your alt text will help your web page rank higher on search engines, it is essential to know that search engines can't recognize unhelpful or bad alt text. And if you have excessive keywords in your alt text (keyword stuffing) it can make your web page rank low.

This means you should only to use important images that enhance the essence of your web page and only use the most important keywords to describe them.

### Don't repeat yourself

Avoid repetition by all means. Why would you use your web page title or heading as alt text? It's better to leave it empty than repeat captions or web content.

The best advice is, when you cannot describe an image well, it's best to leave the alt text empty than add any random text or use image captions as alt text which is repetition.

#### Image Captions vs. Alt Text

It's easy to confuse image captions and alt text or repeat the content in your alt text as an image caption.

Captions describe images to help users relate to surrounding text, whereas alternative text explains the information in an image or describes an image for screen reader users.

Captions do not have to exactly match what the image shows but rather they explain how the image relates to the text or content in which it is placed.

### Don't include the words' image' or 'picture'

The alt attribute is used in an image tag, which means search engines will know that this is an image, so there is no need to use the word image or picture when writing alt texts.

However, it's good to help people understand the context or what type of image or picture it is. For example, you could say headshot, illustration, screenshot, chart, and lots more.

## Wrapping Up

In this article, you have learned what alt text means and why it's essential. You've also seen some important tips on how to use it when embedding images on your web page.

Finally, it is essential to note that you should always add alt text to your images, including your logo, images used as buttons, and many others – and it's crucial to know why uou're doing this.

But note that decorative images, whose primary purpose is to decorate your web pages rather than pass information, do not require alt text.

Thanks for reading, and ensure you have fun coding!
