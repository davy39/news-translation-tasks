---
title: Why you shouldn’t forget about long tail SEO
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-16T10:06:08.000Z'
originalURL: https://freecodecamp.org/news/why-you-shouldnt-forget-about-long-tail-seo-34782120b855
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ExbW2LM_HyyFQBkfLBRgnA.jpeg
tags:
- name: Entrepreneurship
  slug: entrepreneurship
- name: General Programming
  slug: programming
- name: SEO
  slug: seo
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ben Rudolph

  A few months ago, I wrote about how I built ThingsOnReddit. It’s a site that finds
  the best Amazon products posted to Reddit and uses Amazon Affiliates to monetize
  it. I became HN famous for a few days or so, and then slowly disappeare...'
---

By Ben Rudolph

A few months ago, I [wrote about](https://medium.com/swlh/my-journey-to-unlocking-amazon-affiliates-202faf99a098) how I built [ThingsOnReddit](https://thingsonreddit.com/). It’s a site that finds the best Amazon products posted to Reddit and uses Amazon Affiliates to monetize it. I became HN famous for a few days or so, and then slowly disappeared into oblivion. That is when I realized that I would eventually run out of sites that got me that quick spike in hits, and would need to focus on building SEO for the website.

I initially ran into some roadblocks, but have slowly built a predictable and growing amount of traffic to the site. Along the way, I learned much more about how my site was being used, and focused on improving the site for that use case.

### Rethinking the SEO Strategy

In the beginning, I tried to optimize for keywords that could potentially land users to my homepage. My thought process was this: the user lands on the homepage, finds an interesting subreddit and/or product, and then buys said product on Amazon. I even created a new homepage for users to land on that was a bit more friendly, and offered an easier way to navigate to subreddits.

It was a bad strategy.

The table that changed my paradigm is below:

![Image](https://cdn-media-1.freecodecamp.org/images/WrUleKQjTcxZZFvQf39j1xZ6QqVilyrHSd24)
_Breakdown of which pages users are landing on for the last 30 days_

It’s hard to see, but the home page, which has the most page views upon landing, makes up only 11.27% of the total. Most users are landing either directly on a subreddit or a product page.

It became abundantly clear that my SEO approach should be based on the breadth of the pages on my website.

![Image](https://cdn-media-1.freecodecamp.org/images/0ykGyr-et1YWK3mY3OC86k1YrbXUInXh7ZyP)
_This graph shows how many pages Google has indexed over time_

That is when I began to realize the power of long tail SEO. **Long tail SEO means that you target niche Google keywords (usually 3+ or more words) that have low competition**. This naturally happened to my site — there are hundreds of thousands of product pages with all sorts of strange keywords resulting from the comments of Redditors about the product.

#### Sitemaps

Sitemaps tell a search engine about the structure of your website. It’s not usually needed if your site is small and well-linked together, but my site was sprawling and huge.

I created a sitemap to include the maximum number of URLs, 50,000. ThingsOnReddit has a page for every subreddit and Amazon product mentioned on Reddit, so there are _a lot_ of potential pages to index (far more than 50,000). Google takes its sweet time indexing your pages, but as it did index my pages, my SEO presence grew by over 1000%.

![Image](https://cdn-media-1.freecodecamp.org/images/hsOqon6PMdG3rI8VFvtm9QN2qNVO6xGjdwvO)
_Users coming to ThingsOnReddit via organic search_

#### Link Tags

Getting these right is essential to optimizing your SEO presence. I initially launched ThingsOnReddit without thinking about this. That was a mistake.

`**<link rel="canonical" href="**`"/>

This is critical if you have a site that does any sort of pagination. This tag tells Google that the current page is actually the same as the URL in the `href` attribute. This is often used when blogs (like Medium) repost posts from other sites, but it’s also necessary when you have URL schemas like below:

```
https://thingsonreddit.com/things/r/buildapc?page=1https://thingsonreddit.com/things/r/buildapc?page=2https://thingsonreddit.com/things/r/buildapc?page=3
```

Or even:

```
https://thingsonreddit.com/things/r/buildapc?order_by=n_references_in_subreddithttps://thingsonreddit.com/things/r/buildapc?order_by=created_utchttps://thingsonreddit.com/things/r/buildapc?order_by=score
```

The problem I came across was that Google would index the URL:

```
https://thingsonreddit.com/things/r/buildapc?page=7
```

And that URL would show up in the Google search results. Then a user would land on page 7 when I obviously wanted them to land on page 1. `rel="canonical”` will tell Google to ignore all the URL params and just index `https://thingsonreddit.com/things/r/buildapc` .

`**<link rel="next|prev" href="**`"/>

This tells Google that the next logical page (or previous if you specify `prev`) is the URL in the `href` attribute. Google [says](https://support.google.com/webmasters/answer/1663744?hl=en) they can usually figure it out on their own, but in my experience, they didn’t get it right. It takes a while for Google to make adjustments, so get it right the first time.

#### Internal Links

When building an affiliate link site, it’s tempting to build your website to get the user to Amazon (or whatever affiliate site) as quickly as possible. Initially that was what I sought to do.

![Image](https://cdn-media-1.freecodecamp.org/images/Utv-VN-z97upVMvUS8Tk40-PSr5tq6aQrLYk)

On the first implementation, users were taken straight to Amazon to get the affiliate click as quickly as possible.

The thing I eventually learned was that users that are going to buy a product will eventually click the Amazon link if they want the product. **It is far more important to have individual product pages for each product so that each one can be indexed individually and show up in search results.**

#### Analytics

Part of having a better SEO presence is building a good user experience. The better the user experience, the lower your bounce rate, and the more favorably Google will look on your site. A key part of understanding how to make a good experience is to track all the things.

It’s harder to tell how changing the user experience directly modifies your bounce rate or Google search ranking unless you do some sort of A/B testing, but analytics can point you in the right direction.

For example, I was under the impression it is _always_ good to build a mailing list. So I began aggressively showing a newsletter signup modal when a user scrolls to the bottom of the page:

![Image](https://cdn-media-1.freecodecamp.org/images/wc9okpLcdMLsNBB-eggiDbKrN7Pjo9o-k1Xy)
_My friendly newsletter signup modal_

I tried this for months, and I got **0 signups** after showing the modal **609 times**. Needless to say, this is an extremely annoying feature and it yielded no signups, so I killed it.

### The Results

After letting ThingsOnReddit run by itself for a while, I’m happy to announce some better results.

![Image](https://cdn-media-1.freecodecamp.org/images/CScgnaOlhEsM32d3UuPxVEmqID1dArRYuG3f)

The month that received the most clicks to Amazon (thus far) was November, yet it was also the month with the least revenue. Most of these clicks were generated through Social traffic when I tried to ram the site down people’s throats via various social media sites.

It turns out, **focusing on organic search is better not only for sustainable recurring users, but also users who genuinely _want_ to buy products and are more likely to convert**.

Going forward, I’m going to continue to push on improving the site’s Google search ranking, by both refining the site’s experience as well as trying to grow the number of sites linking to ThingsOnReddit.

