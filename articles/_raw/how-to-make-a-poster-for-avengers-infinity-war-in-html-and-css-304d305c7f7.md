---
title: 'How to make a poster for Avengers: Infinity War in HTML and CSS'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-13T19:10:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-poster-for-avengers-infinity-war-in-html-and-css-304d305c7f7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bKfG0yasGD590ClJBKDetQ.jpeg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kunal

  In this post, we are going to make a movie poster of “Avengers: Infinity War” in
  HTML and CSS.

  Here’s what we will build:


  Looks interesting, doesn’t it?

  Here are some important concepts you will learn while making this poster:


  How to give ...'
---

By Kunal

In this post, we are going to make a movie poster of “Avengers: Infinity War” in HTML and CSS.

Here’s what we will build:

![Image](https://cdn-media-1.freecodecamp.org/images/1*bKfG0yasGD590ClJBKDetQ.jpeg)

Looks interesting, doesn’t it?

Here are some important concepts you will learn while making this poster:

* How to give a full-screen background image to your page
* Centering elements horizontally in CSS
* Centering elements vertically in CSS
* Embedding Youtube videos in HTML
* What is Margin Collapse
* How to load custom fonts from a local file
* How to load fonts from Google fonts

This is going to be fun, so let’s dive in.

### The blank slate

Let’s get on the same page first.

This is what my project folder structure looks like:

![Image](https://cdn-media-1.freecodecamp.org/images/1*SHnVL-WZQ0muKIKwoo1lWQ.jpeg)

Our stylesheet “styles.css” goes inside the CSS folder, the custom font file that we will download will go inside fonts folder, the background image that we will download will go inside the img folder, and our HTML code resides in the “infinity-war.html” file.

Here’s my HTML file for a blank page. We will build upon this blank page:

If you don’t understand the above code, then you are probably coding in HTML for the first time. I would recommend starting here: [How to Make a Burger in HTML — A Beginner Tutorial](https://medium.com/frontendshortcut/how-to-make-a-burger-in-html-a-beginner-tutorial-dca7b4b0a179).

### Full background image

First download the [image](http://hdqwalls.com/wallpapers/avengers-infinity-war-2018-4k-cq.jpg) and save it in “img” folder.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YhsGz4lXux0XEYL2NZkQJQ.jpeg)

Note: All rights of the image belongs to Marvel Studios, used here only for learning purposes.

We normally use the `<i`mg> element to include images in HTML. But for this specific purpose we will create a div, make that div cover the entire screen, and then set the background image on that div using the "background-image" CSS property.

Here’s our HTML:

and our CSS:

As you can see, we created a div and gave it a class in our HTML file. In our CSS file, we set the width and height to 100% so that it covers the entire screen. We set the background image using the “background-img” property.

Notice how we are referencing the image file: `url("../img/infinity-war-wallpaper.jpg")`. You see that `..` at the beginning of the path? See, we are referencing the image file which is in the "img" folder from our styles.css file which is in the "css" folder, right?

So we need to go one folder out and then reference the path. That `..` takes us one folder up in the folder structure.

Let’s refresh the page in the browser and see the result.

Aaand, it’s still a blank page.

Actually, we are missing one detail here.

When we set height or width in %, say 100% in our case, it’s not 100% of the screen — it’s 100% of its parent’s dimension.

What is the parent element of the div? `<bo`dy>. What is the parent element of the `body?` <html>.

So, we need to set the height of our body and HTML elements to 100%. Let’s do that and see if it works:

Now we get this output:

![Image](https://cdn-media-1.freecodecamp.org/images/1*ox5E8h7eEJyVs3moBMQy7Q.jpeg)

Okay, if you look at it carefully you will see there are two issues here:

* there is a white gap around the image — do you see that?
* the image is zoomed in, isn’t it?

Let’s tackle these issues one by one.

The body element by default has some margin to it. That’s why we see that gap around the image.

Let’s remove the margin by setting it to 0 on the body:

Refresh the browser and you will see that the white gap is gone and there is no scrollbar now.

Next, let’s solve the image scaling problem. By default, the image will be displayed in its original size. We can change this to scale the image in such a way that it will cover the screen by setting the “background-size” property to “cover”.

We also set the backgound-position to center the background image.

Both the problems are solved.

### Margin collapsing

Let’s add a heading using the `<`h1> element and give it white color using the "color" property in CSS:

and our CSS:

Output:

![Image](https://cdn-media-1.freecodecamp.org/images/1*epGPR0ycthJ6PyrYJ3bEQg.jpeg)

We messed up something. Where did that white gap come from?

Well, it turns out, the h1 element, just like the body element, also has some margin by default, and so do the h2, h3, h4, h5 and h6 elements.

But, even if the h1 element had a margin, it must be displayed with some gap _inside_ the div with our background image. So why did it display a gap _outside_ the div?

Ideally, it should have been displayed like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*XOd5CXCEZbEbMAmpZrGFSw.jpeg)

But it instead displays a gap above the “full-bg” div.

This happens because of Margin Collapsing.

When you have two block elements (the div and h1 in our case), and the parent element doesn’t have any padding or border, then the top and bottom margin of the child element will be displayed as the top and bottom margin of the parent. This is called Margin Collapsing. The margin of the child collapses with the margin of the parent.

If the parent element has a padding even of just 1px, or has a border of at least 1px, then this won’t happen. Let’s give 1px padding to our “full-bg” div and see its effect:

The margin collapsing is fixed.

But — did you notice a tiny difference?

Your browser now has a horizontal and vertical scrollbar. That means the width and height of the div have increased.

How?

### The padding and the border increase the size of the element

This is one more default behavior that you must remember. Say you create a div of 100px x 100px, and give it a padding of 10px. The div will now become 110px x 110px.

Yes, the amount of padding you give to an element is added to the dimension of the element. It’s the same with the border: if you give a 4px border to your element, its size will increase by 4px.

We ideally don’t want to increase the size of the element, but rather shrink the content inside the element to make up space for the padding and border.

We can achieve this by setting the “box-sizing” property to “border-box”. Let’s do that:

Refresh your browser. Bam, the scroll bars are gone.

### Section and header

If you saw the end result picture, you will see we still need to add a sub-header, a YouTube video, and the release date. It’s a good practice to group all these elements into a section, since these elements are related to each other. Let’s create a section using the `<secti`on> tag and put our h1 inside it:

All the elements of our poster will go inside this “poster-content” section.

You might be wondering why we didn’t use “div” here — why “section”?

Actually, before HTML5, everything used to be “div”. In fact, we can make entire websites with only “div” elements. But we don’t do that because it makes more sense to include an image with the <img> element, it makes more sense to include a paragraph wit`h t`he <p> element, and similarly, it makes more sense to group content of similar t`heme in t`he <section> element.

So, the rule of thumb is, use `<d`iv> when you want a container only for giving the content some style (like our "full-bg" div), an`d use <`;section> when you want a container to group similarly-themed content.

Next, we also know there is going to be a subheading. Luckily, HTML5 has an element to group heading elements — the `<head`er> element. Let's include that too:

We must also update the selectors in our CSS:

Now, as soon as you hit refresh, you will notice that the font of our h1 element becomes smaller.

Many browsers reduce the font size of the h1 element when placed inside a `<secti`on> `or a <`;article> element. So it's best to give the size to our h1 manually whenever it’s pl`aced insi`de &`lt;sectio`n> or <article>:

### Transparent background

Let’s give a black semi-transparent background color to our section element:

output:

![Image](https://cdn-media-1.freecodecamp.org/images/1*PsSzEft5rpXHqW8fwf1yNw.jpeg)

The code “rgba(0, 0, 0, 0.6)” means: color with 0 red, 0 green and 0 blue components, which is black, and 60% opaqueness.

Two things: we don’t want the text to stick to the borders of the semi-transparent box. Second, we want to give the section a fixed width and align it to the center.

Let’s do this:

We gave a padding of “16px” and set the “box-sizing” to “border-box” because we don’t want the container to expand by 16px to make space for padding. Rather we want the container to remain the same size and the content inside it to shrink to make space for 16px of padding.

Output:

![Image](https://cdn-media-1.freecodecamp.org/images/1*kh-fqa4y3Za8fqZYuhIDGw.jpeg)

Okay, the top and bottom gap surely don’t look like “16px” — they look like much more than that. And if you noticed, the section wasn’t touching the top edge of the browser before, but now it is. What’s happening?

It’s margin collapse at play again. The extra space above and below h1 is not the padding of the section, it’s the margin of the h1. Previously we didn’t have any padding on the section so the margin of h1 and section collapsed and was displayed outside the section. That’s why the section was not touching the top before.

Let’s reduce the margin of h1 and center it by setting “text-align: center” for our `<head`er> element:

Refresh the page and the h1 text should be centered now with relatively less space around it.

### Flex to center things

Our section is already centered horizontally, because of the “margin: auto”.

What “margin: auto” does is it sets the margins on all sides (margin-top, margin-right, margin-bottom and margin-left) to “auto”.

We know that setting margin-left and margin-right to “auto” centers the element horizontally.

But setting margin-top and margin-bottom to “auto” doesn’t automatically center an element vertically. Historically, centering things in HTML has been one of the big hair-pulling moments for web developers.

Not anymore. Now that Flexbox is widely supported by all browsers, we can use “display: flex” on an element. That element will become a “flex container” and its children will become “flex-items”.

Flex items have some great properties. For example, when the margin-top and margin-bottom of flex items are set to “auto”, it centers vertically!

Let’s give it a shot, add “display: flex” to “.full-bg”:

Output:

![Image](https://cdn-media-1.freecodecamp.org/images/1*l_d0FkGBckGqp4k6nv1z9w.jpeg)

Okay, now it’s starting to look good.

### Load a custom font from a local system

If we really want to make it look cool, we will need a custom font for our header.

Have a look at this font on “dafont.com”:

![Image](https://cdn-media-1.freecodecamp.org/images/1*_H1Wq3Uz5EKQaMUDghP7hQ.jpeg)

This looks perfect for our use, so you can download it [here](https://www.dafont.com/avengeance.font).

If you extract the zip file, you will see font files in TTF and OTF formats. We can use these, but WOFF format is the best way to go when using any custom font for CSS. Go ahead and convert any one of the TTF files to WOFF using this online [tool](https://onlinefontconverter.com/).

Then we will place the converted .woff file inside the “fonts” directory.

Let’s load our font:

Note: If you are using Firefox, you will have to allow local font files to load. Type about:config in the address bar in Firefox and hit enter. Accept the warning. Then search “strict_orogin_policy” and turn it false.

Output:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ocd8cEcW2fNHGidZYawjHg.jpeg)

Alright, now we are talking.

### Styling the “header”

Now, let’s write “Infinity War” as a sub-header as h2 and give a top and bottom border.

and our CSS:

Output:

![Image](https://cdn-media-1.freecodecamp.org/images/1*orbR-s8x_fLR6sYNgle19g.jpeg)

Okay, two problems here:

* the gap between h1 and h2,
* we don’t want the white lines (top and bottom border of h2) to span the entire section. We want it as wide as the “Avengers” text.

To reduce the gap between h1 and h2, let’s remove the margin-bottom of h1 and margin-top of h2:

The code “margin: 16px 8px 0” means set the top margin to 16px, right and left margin to 8px, and bottom margin to 0.

Now for the second problem.

The <header> element is by default a block element, so its width spans over its parent’s width. If we make it an “inline-block” element, then it won’t expand to its parent’s width, and will only occupy the width required to fit the text inside it. That’s exactly what we want.

Let’s give “display: inline-block” to the header and “text-align: center” to its parent “poster-content”:

Output:

![Image](https://cdn-media-1.freecodecamp.org/images/1*kMygYZw_BHEqZCtRRpaiBg.jpeg)

### Custom Google font

Let’s use a sci-fi font for h2. We saw how to download a font and use it in our CSS. In such a scenario, you are hosting the font yourself. Google provides many hosted fonts for free [here](https://fonts.google.com). We just link it from Google. Here is one that looks good for our use:

![Image](https://cdn-media-1.freecodecamp.org/images/1*OMR76PpUGsGzZ_ty8zPB9g.jpeg)

Here’s the [URL](https://fonts.google.com/specimen/Audiowide).

Go to the URL above and click “SELECT THIS FONT” on the right side of the screen:

![Image](https://cdn-media-1.freecodecamp.org/images/1*5LT-eATcKpb01KehR6Zxfg.jpeg)

Then click on the “Family Selected” bar displayed at the bottom:

![Image](https://cdn-media-1.freecodecamp.org/images/1*UNt8QiOtTM-OZ3Cnru18CA.jpeg)

That will give us the code to copy to use that font on our page:

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZW2S5IeEgjD6sGqjk7zC4A.jpeg)

Paste the `<li`nk> code to our HTML file:

and the font-family code to our CSS:

I also added some letter-spacing, since the letters were looking congested. I also increased the font-size to 26px.

Output:

![Image](https://cdn-media-1.freecodecamp.org/images/1*JKpvtjmxeemuwSdKx5Qoug.jpeg)

### Embed the YouTube video

The movie poster will be incomplete without a video of the trailer.

We can include the YouTube video in our HTML page using “iframe”. The “iframe” tag allows us to load another HTML page in the current page. Which page to load is decided by the “src” attribute.

Here’s how you can use <iframe> to include a video from Youtube:

```
<iframe src="https://www.youtube.com/embed/6ZfuNTqbHE8"></iframe>
```

The text “[https://www.youtube.com/embed/](https://www.youtube.com/embed/)" in “src” remains the same for all Youtube videos. Only the last random-looking string “6ZfuNTqbHE8” changes for each video. That’s the ID of the video, and you can find it in the video’s URL:

![Image](https://cdn-media-1.freecodecamp.org/images/1*UPkoofYc60Pmlh-WK6gNiA.jpeg)

Let’s include the Trailer video:

Output:

![Image](https://cdn-media-1.freecodecamp.org/images/1*FXxy6cAzUxu8L5vQLmHkiw.jpeg)

Damn. What went wrong now?

Can you guess why the video is displayed to the right of the header?

Because we set the header as “inline-block”, and as we know, an inline-block element will give place to the next element just beside it.

To solve this, let’s give some width and height to our iframe element:

The default border of the iframe was looking ugly, so I added a 2px border of “#ddd” color (almost white).

Output:

![Image](https://cdn-media-1.freecodecamp.org/images/1*vq9V7UCe2IYz5U9yv70RRQ.jpeg)

Great.

One last thing — the release date. Let’s put the release date in a paragraph at the bottom:

and style the paragraph a bit:

We increased the font size to 18px, gave it white color (#fff), set the font to “Audiowide”, and reduced the bottom margin to “8px”.

Output:

![Image](https://cdn-media-1.freecodecamp.org/images/1*bKfG0yasGD590ClJBKDetQ.jpeg)

Our Infinity War movie poster is complete.

**Want to learn Web Development with fun and engaging tutorials?**

[**Click here to get new Web Development tutorials every week.**](http://supersarkar.com)

