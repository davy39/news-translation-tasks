---
title: Why You Should Use rem to Set Font Size in CSS
subtitle: ''
author: Vinod Mathew Sebastian
co_authors: []
series: null
date: '2023-01-17T21:33:17.000Z'
originalURL: https://freecodecamp.org/news/why-use-rem-to-set-font-size-in-css
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/em_vs_rem.png
tags:
- name: CSS
  slug: css
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Setting font sizes is something you''ll do often as a web developer. But
  sometimes, especially for beginners, this can get a bit tricky.

  In this article, I''ll explain why I think you should always use rem over em for
  setting the font-size of an elemen...'
---

Setting font sizes is something you'll do often as a web developer. But sometimes, especially for beginners, this can get a bit tricky.

In this article, I'll explain why I think you should always use `rem` over `em` for setting the `font-size` of an element.

## What are Relative Units in CSS?

For styling a webpage, we use relative units like `em` and `rem` instead of absolute measurements like `px` (pixels).

This is because nowadays, screen sizes come in different sizes and shapes. If we use `px`, the element's size remains constant regardless of the size of the screen. So using relative units like `em` and `rem` are considered good practice. (The `:root` size is still set in `px`. We need a reference point. Don't we?)

CSS units are thus classified into two ways: absolute and relative units. Pixels (`px`), points (`pt`), and picas (`pc`) fall under absolute units. The `%`, `em`, `rem`, `vh`, and `vw` are all relative units.

## What are `em` and `rem` Units?

Talking about `em` and `rem`, in print typography `em` refers to the width of the capital letter 'M' of the current typeface.

In web design, `em` refers to the size of the current element. If the size of the current/parent element is not set, it usually defaults to the size in the browser CSS. It is usually 16px.

The `em` is not just for font-size. It is a relative unit that you can use to set the values of properties like font-size, margin, padding, width, height, and line-height of an element.

The `rem` is the root `em`. All values are relative to the topmost parent, the `html` or `:root` element. If not explicitly set for the `html` or `:root` element, it again defaults to the browser CSS: 16px.

You can use `rem` wherever you can use `em`.

## When is `rem` a Better Choice than `em`?

Now let's discuss why you should always use `rem`, instead of `em`, for setting the font-size of an element in CSS.

CSS styles cascade. That is why it is called *cascading* style sheets. If you inadvertently apply a `font-size` of `0.5em` again, the size reduces to 1/4th of the original.

Note: This happens only if you use relative units. Even if you apply an absolute unit (say `16px`) any number of times, for example, on the `font-size`, it will always remain the same. It would just be duplicate style declarations. The browser effectively ignores it.

Let me show you an example.

This is a simple webpage. Only one `h1`, `p`, and an `a` tag nested inside the `p` tag are inside it.

```typescript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome - Difference between applying em and rem</title>
</head>
<body>

<h1>The difference between em and rem in the font size of an element</h1>
<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ad beatae alias adipisci placeat fuga maiores nobis aliquam, atque porro explicabo veritatis dolorum tenetur ullam in?

<a href="#">Click me!</a>

</p>

</body>
</html>
```

For an example, the `h1`, `p`, and `a` tags are all given a `font-size` value of `0.5em` to be displayed on a smaller screen.

```typescript
@media all and (max-width:768px){

h1{
font-size:0.50em;
}
p {
font-size:0.50em;
}
a {
font-size:0.50em;
}
}
```

Now see what happens. This is the mobile view (zoomed to 300%).

![Image](https://www.freecodecamp.org/news/content/images/2023/01/mobile_view_one-1.png align="left")

The 'Click me!' inside the `a` tag is 1/4th the size of the original – and it's barely readable.

Immediately after applying `0.5em` to the `p` tag, `em` is now only `8px`.

`16px x 0.5 = 8px`

Since the `a` tag is nested inside the `p` tag, both styles cascade.

`8px x 0.5 = 4px`

The solution is to use `rem` for the `a` tag: `0.5rem`.

Please note that `h1` and `p` tags use `em` here for demonstration purposes.

```typescript
@media all and (max-width:768px){
h1{
font-size: 0.50em;
}
p { 
font-size:0.50em;
}
a {
font-size:0.50rem;
}
}
```

Since we used `rem`, the `a` tag is relative to the *root* `em` – that is, it's set to 16px by default.

`16px x 0.5 = 8px`

![Image](https://www.freecodecamp.org/news/content/images/2023/01/mobile_view_final-7.png align="left")

The *Click me!* `a` tag is styled more appropriately now.

Always remember that it is a good idea to use `rem` for setting the font size of an element as you saw here.

## Conclusion

In some places, it's better to use `em`. But when you're setting the font size of an element, `rem` is the better choice.

Happy Coding!
