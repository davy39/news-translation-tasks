---
title: CSS Comments – How to Comment out CSS
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-06-02T14:49:40.000Z'
originalURL: https://freecodecamp.org/news/css-comments-how-to-comment-out-css
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/CSSComment.png
tags:
- name: best practices
  slug: best-practices
- name: CSS
  slug: css
seo_title: null
seo_desc: 'Commenting is an integral part of any programming language, and CSS is
  no exception.

  If you have a very large project or you work in a team, then you''ll need to help
  others understand your CSS stylesheet better by adding comments to it.

  Since stylesh...'
---

Commenting is an integral part of any programming language, and CSS is no exception.

If you have a very large project or you work in a team, then you'll need to help others understand your CSS stylesheet better by adding comments to it.

Since stylesheets can get complicated and verbose over time, adding comments to your CSS code is a helpful convention you should follow.

This article will show you how to add both inline and multiline comments in CSS.

## How to Comment Out CSS

A forward slash (`/`) and asterisk (`*`) are all you need to comment out a line or lines of CSS. But how do you do it?

To add both inline and multiline comments in CSS, you start with a forward slash and asterisk (`/*`), and you end the comment it with an asterisk and forward slash (`*/`).

This is what an inline comment looks like in CSS:
```css
/* This is an inline comment in CSS */
```

This is what a multi-line comment looks like:
```css
/* 
This 
is
a 
multi-line
comment
in 
CSS
*/
```

You can comment out a line or lines of CSS you don’t want to run:
```css
/* .email-sub {
  padding: 0.2rem;
  border: 1px solid var(--primary-color);
  border-radius: 4px;
}

.email-sub:focus {
  border: 1px solid var(--secondary-color);
  outline: none;
} */
```

You can specify the start and the end of the styles for a section of the your web page with comments:
```css
/* Hero section starts */
.hero {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.9rem;
  max-width: 1100px;
  margin: 2rem auto -6rem;
}
/* Hero section ends */
```
You can also use comments to add notes to your CSS:
```css
/* 
Don't override this style if you don't know what you are doing. Otherwise, CSS might give you a kick in the butt
*/
```

## Conclusion

In the long run, adding comments to your CSS can help you remember what you were doing when you wrote the code.

In addition, when you add comments the right way, it makes it easier to begin working on a project if it’s been a long time since you looked at the code.

To see how you can organize your CSS with comments, you should read [this article](https://www.freecodecamp.org/news/comments-in-css/).


