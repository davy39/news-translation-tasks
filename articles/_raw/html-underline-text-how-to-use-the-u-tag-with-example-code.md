---
title: HTML Underline Text – How to Use the <u> Tag with Example Code
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-07-20T22:48:13.000Z'
originalURL: https://freecodecamp.org/news/html-underline-text-how-to-use-the-u-tag-with-example-code
coverImage: https://cdn-media-2.freecodecamp.org/w1280/605301d528094f59be257c67.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: HTML5
  slug: html5
seo_title: null
seo_desc: "In this article, we are going to learn about the <u> tag and when it is\
  \ appropriate to use it in HTML 5. \nIn older versions of HTML, you'd use this tag\
  \ as a way to underline text. We are going to learn about the new HTML 5 definition\
  \ and ways to unde..."
---

In this article, we are going to learn about the `<u>` tag and when it is appropriate to use it in HTML 5. 

In older versions of HTML, you'd use this tag as a way to underline text. We are going to learn about the new HTML 5 definition and ways to underline text using CSS. 

## What is the <u> tag?

The `<u>` tag stands for Unarticulated Annotation element. This element is a length of inline text that stylistically looks different from its surrounding text but has non-textual annotation. 

The default style for this element is a single underline. 

Let's take a look at some examples of when to use the `<u>` tag.

### How to use the <u> tag for misspelled words

A common use for this tag is to point out misspelled words. 

```html
<p>I was sitting in <u>orcestra</u> practice and the conductor was mad because we <u>didt</u> practice our parts.</p>
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-20-at-2.45.43-PM.png)

You can also use the `<u>` tag if you want to label Chinese text as a proper name mark. According to Wikipedia, 

> a **proper name mark** ([Simplified Chinese](https://en.wikipedia.org/wiki/Simplified_Chinese): 专名号, zhuānmínghào; [Traditional Chinese](https://en.wikipedia.org/wiki/Traditional_Chinese): 專名號) is an [underline](https://en.wikipedia.org/wiki/Underline) used to mark [proper names](https://en.wikipedia.org/wiki/Proper_name), such as the names of [people](https://en.wikipedia.org/wiki/Chinese_name), [places](https://en.wikipedia.org/wiki/Place_name), [dynasties](https://en.wikipedia.org/wiki/Chinese_dynasties), organizations.

```html
<p> This is an example of a proper name mark:<u>书名号</u></p>
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-20-at-1.28.22-AM.png)

## How to use CSS to change the style of the <u> tag

If you want to point out misspelled text, you can style the `<u>` tag with a red wavy line underneath it. 

```html
<p>This sentence has so <u class="spelling">mannny</u> spelling <u class="spelling">errrrors</u>.</p>
```

```css
body {
  font-family: Verdana, sans-serif;
}
u.spelling {
  text-decoration: red wavy underline;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-20-at-1.36.15-AM.png)

## Avoid using the <u> tag for styling purposes

In earlier versions of HTML, it was appropriate to use the `<u>` tag strictly for styling text with an underline. But in HTML 5, the `<u>` tag holds semantic meaning and you should use CSS to style your text with an underline. 

```html
<span class="underline">This text was styled with CSS.</span>
```

```css
.underline {
  text-decoration: underline;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-20-at-1.50.19-AM.png)

## Do not use the <u> tag for titles of books

If you are referring to a book title, you should use the `<cite>` tag. The default styling is in italics but you can override those styles using CSS.  

```html
<p>I enjoyed reading <cite>The Great Gatsby</cite> in high school.</p>
```

```css
cite {
  font-style: normal;
  text-decoration: underline;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-20-at-2.11.30-AM.png)

## Conclusion

The `<u>` tag is a semantic element that should only be used in very specific cases. If you want to point out spelling errors within the text, then you can use the `<u>` tag.  

A less common example would be to use the tag in Chinese proper name marks. 

You should never use the `<u>` tag for styling purposes. Instead you should use `text-decoration:underline;` in your CSS. 

Whenever you are working on a project, it is important to learn the correct usage for HTML 5 elements so you can use them in the proper way. 


