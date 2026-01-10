---
title: How to avoid the shameful look your site has on Twitter and Facebook
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-07T15:39:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-avoid-the-shaming-look-your-site-has-on-twitter-and-facebook-f2e8f4be568d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*R5gAdbWi_wTP1_zSBjBtYA.jpeg
tags:
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: SEO
  slug: seo
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Emmanuel Ohans

  If you already understand what Facebook Open Graph and Twitter Cards are, this article
  is not aimed at you. Please pass it on to someone who doesn’t understand what those
  are.

  Introduction

  According to Mashable, 52% of shared links ...'
---

By Emmanuel Ohans

If you already understand what Facebook Open Graph and Twitter Cards are, this article is **not aimed at you**. Please pass it on to someone who doesn’t understand what those are.

### Introduction

According to [Mashable](https://mashable.com/2012/08/16/twitter-day-in-the-life-infographic/#Cscw4XDZ.8qM), 52% of shared links on Twitter are articles and images, with images taking about 36% of the pie. On the average, people are sharing about [30 million unique images](https://www.quora.com/How-many-photos-are-shared-on-Twitter-per-day) per day.

![Image](https://cdn-media-1.freecodecamp.org/images/PHJm0i5jyHlBYiyDsGVXWrUHebFS93A4YDqu)
_From [Mashable](https://mashable.com/2012/08/16/twitter-day-in-the-life-infographic/#Cscw4XDZ.8qM" rel="noopener" target="_blank" title=")_

Did you gasp?

I did.

Tweets with image links get 2x the engagement rate of those without, says [Buffer](https://blog.bufferapp.com/10-new-twitter-stats-twitter-statistics-to-help-you-reach-your-followers).

Now, these stats are just for Twitter. The combined stats for other popular social media platforms will blow your mind.

Bottom line is: **humans are visual beings.**

If your site is shared on social media, and it looks like a boring sour stew, the engagement will be low. Share a link that appears nicely in people’s timeline, and you are more likely to get the kind of engagement you seek.

Not taking these into consideration when building your site? You’re definitely doing something wrong.

### What exactly is the shaming look?

Well, not all links are created equal. Consider the graphics below. They represent the appearance of two different links shared on Twitter. One is from Medium, the other from a website of mine.

![Image](https://cdn-media-1.freecodecamp.org/images/hhdzeV7Bmwg9V4uBdlksG0Sg9stiOZH9lQ-7)
_This is a shared medium article, and it definitely looks good!_

The previous graphic has a large image, title, description, and looks good generally.

![Image](https://cdn-media-1.freecodecamp.org/images/IRVjqvQg6QHvYqHv0-kNWsieGr1F1u8glvjU)
_Here’s my own website link shared and this doesn’t look as good. Sad stuff :(_

This just doesn’t look as good. So, what’s Medium doing under the hood to make their shared URLs look great?

### Going from zero to hero

Let’s take a step-by-step approach to taking a site from “shaming look” to “freaking awesome”.

For our considerations, I’ll be using one of my sites, `[TheReduxJSBooks.com](https://thereduxjsbooks.com)`, as the lab rat.

First, to preview how your link preview will be displayed on Twitter and Facebook, both companies provide debuggers where you paste in your link and have a look for yourself.

Here’s the link for the [Facebook Sharing debugger](https://developers.facebook.com/tools/debug/sharing), and [this](https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/summary-card-with-large-image) for Twitter.

Starting at “zero”, let’s see what `[TheReduxJSBooks.com](https://thereduxjsbooks.com)` looks like when shared now.

Here’s what we’ve got on facebook:

![Image](https://cdn-media-1.freecodecamp.org/images/uSAdcRyH6rIN1flXBxobnaR1lw-MvyOj3cSz)
_The poor look when shared on Facebook (FB). As simulated on the FB sharing debugger, FB managed to display the URL and the first bit of text on the website_

And this on Twitter:

![Image](https://cdn-media-1.freecodecamp.org/images/aO2xjqU6SedgDgGQsGt3-UYVTPa42htJZWbi)
_So bad — no previews are shown :( Twitter doesn’t pull out any info from the site. You gotta do the work._

Those don’t look impressive at the moment, but we will fix that shortly.

To have some control over how your links look when shared, Facebook developed the technology called **Open Graph**. It’s nearly becoming a standard across other services, and **not** just Facebook. Twitter calls theirs something different, **Twitter Cards**.

Let’s see how these work.

### Facebook Open Graph

![Image](https://cdn-media-1.freecodecamp.org/images/EOjVvxA10KOD-R84wr1wdyuTtA5qcb04PfgE)

In the simplest of terms, the Facebook Open Graph is all about including certain `meta` tags to the head of your `html`.

These metadata will be read from your site, and they affect how your link is previewed when shared.

Now, have a look at the final results we will achieve when the link is shared on Facebook.

![Image](https://cdn-media-1.freecodecamp.org/images/AaXwdtyqYFxz1tHcNYdWewf6gil3zhWmYHE7)
_The final result we’re gunning for._

What’s different now?

![Image](https://cdn-media-1.freecodecamp.org/images/Nms4XIeiT4XhIKchbTrV6UUllJFaeYj0rkXY)
_Here’s what is different._

Now, that looks beautiful. With a custom image, title, and description, you totally control how your link preview is displayed.

Now, here’s the code that yielded the preview you see above:

```html
<!-- Facebook Opengraph -->
<meta property="og:url" content="https://thereduxjsbooks.com" />
<meta property="og:type" content="website" />
<meta property="og:title" content="The ReduxJS Books" />
<meta property="og:description" content="What you ar about to view is a complete guide to mastering Redux from total novice to badass, and with every skill level catered for. Ready?"/>

<meta property="og:image" content="https://thereduxjsbooks.com/images/redux-trio-1200x630.png" />
<meta property="og:image:alt" content="3 books on ReduxJS. A sequel that takes you from beginner to pro." />
<meta property="og:image:type" content="image/png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
```

I know it feels like a lot of code, but it isn’t.

These are placed in the head of your `html` page. For example

```html
<head>
   <!-- put them here -->
</head>
```

Now, let’s go over each Open Graph `meta` tag one after the other.

Here’s the first:

```html
<meta property="og:url" content="https://thereduxjsbooks.com" />
```

What you have there is a `meta` tag with two attributes, `property` and `content`.

`property` defines the **property** of the meta tag in question. In this case, it has the value, `og:url`.

As you may have guessed, `og` is short for `Open Graph` and `url` denotes that this describes the `url` of the shared link. The`content` then holds the value for the `url`, i.e “[https://thereduxjsbooks.com](https://thereduxjsbooks.com)”.

That was easy.

Now, the same goes for the `type`, `title`, and `description` tags. You see those?

![Image](https://cdn-media-1.freecodecamp.org/images/r0kmRJ0rTKuMBPUMdo4xh7kiM3WV72b7wrfO)
_The type, title and description tags._

The next set of `meta` tags are those that describe the image preview. The first has a property, `og:image`, and the `content` is the URL to the image.

```html
<meta property="og:image" content="https://thereduxjsbooks.com/images/redux-trio-1200x630.png" />
```

An important thing to note is that, for Facebook Open Graph, you must provide the `width` and `height` of the image — preferably `1200px by 630px`

The other tags just further describe the image’s `alt` text, `type`, `width` , and `height` .

![Image](https://cdn-media-1.freecodecamp.org/images/MDwxsM9YKW6ZK53Z8H2VU5QuoOHUFWN4Sep0)
_The image’s alt text, type, width and height!_

Great! Now you know the most important bits of the Facebook Open Graph.

### Twitter Cards

![Image](https://cdn-media-1.freecodecamp.org/images/XyXsWyrWXVpwgvld2f7oGYcxtRnb0YjuHtEn)

Like Facebook, you also have total control over how your link is displayed when shared on Twitter.

If you share your link on Twitter, assuming you already have the Facebook Open Graph meta tags set, you’ll actually get some preview.

It may look something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/otJUDGfOAsJrHTAbnwGf-P5zUmNYvucHucdO)
_Some basic description is pulled from the Facebook Open Graph meta tags. Not so bad, actually._

Not bad, but not great either.

When we are done, here’s what we’ll have on Twitter:

![Image](https://cdn-media-1.freecodecamp.org/images/dAtlPj86grLCtyzPqCZPTh6CTBZCv8W3MNof)
_The better result to aim for on Twitter._

As you can see, the preview image is much larger, and the description isn’t as lengthy. Facebook takes in more characters — but not Twitter.

So, here are the basic tags you need.

```html
<!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:image" content="https://thereduxjsbooks.com/images/redux-trio-560x300.png" />
    <meta name="twitter:image:alt" content="3 books on ReduxJS. A sequel that takes you from beginner to pro." />
    <meta name="twitter:description" content="For every book you buy, we will send a free copy to a developer in India, Nigeria, and Tunisia who can't afford the cost."
    />
```

Simple!

The first `meta` tag is **super important**.

```html
<meta name="twitter:card" content="summary_large_image" />
```

Unlike Facebook Open Graph with the `property` and `content` attributes, Twitter cards use `name` and `content` attributes.

Here, the name is `twitter:card` and the content, `summary_large_image`. This describes the type of Twitter card you want. There are many different types of Twitter cards available, but `summary_large_image` gives you the large image preview you saw earlier.

Unlike Facebook, you do **not** need to describe the image’s `width` and `height`

Just having the name, `twitter:image` and `content` URL will do!

```html
<meta name="twitter:image" content="https://thereduxjsbooks.com/images/redux-trio-560x300.png" />
```

Finally, just include the image `alt` text and a shorter `description` for Twitter.

```html
<meta name="twitter:image:alt" content="3 books on ReduxJS. A sequel that takes you from beginner to pro." />
<meta name="twitter:description" content="For every book you buy, we will send a free copy to a developer in India, Nigeria, and Tunisia who can't afford the cost."
''  />
```

And that is it!

What’s even more beautiful is that setting this up means other services can equally look up this metadata and display your links beautifully!   
  
Here’s a preview for when the link is shared on Slack.

![Image](https://cdn-media-1.freecodecamp.org/images/CqxGbOlFbjJQYIVWKGblc3zE4n3oCJx6nhmX)
_The same link shared on Slack. That looks good!_

Slack’s just one of many services that honour the Facebook Open Graph and Twitter Card technology.

### Conclusion

I have skipped a lot of information to keep this article short. For more technical information, be sure to check out the official docs for both [Facebook Open Graph](https://developers.facebook.com/docs/opengraph/getting-started) and [Twitter Cards](https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/abouts-cards.html).

Now you know those beautiful link previews on Twitter and Facebook didn’t get there by magic.

Someone wrote the code, and now you know how.

Go build sites that look super awesome when shared on Twitter and Facebook!

