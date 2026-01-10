---
title: Why Using Structured Data Helps Your Website’s SEO
subtitle: ''
author: Luke Ciciliano
co_authors: []
series: null
date: '2019-08-28T18:21:57.000Z'
originalURL: https://freecodecamp.org/news/using-structured-data-helps-your-websites-seo
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/seo-and-ipad-1.jpg
tags:
- name: schema
  slug: schema
- name: SEO
  slug: seo
- name: structured data
  slug: structured-data
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Few things are as exciting for a new developer as getting their first customers.
  The idea of putting one’s new coding knowledge to work can be exhilarating.

  There’s an important thing to remember though, especially if your customer is some
  type of sm...'
---

Few things are as exciting for a new developer as getting their first customers. The idea of putting one’s new coding knowledge to work can be exhilarating.

There’s an important thing to remember though, especially if your customer is some type of small business which deals with the public (such as a restaurant, a bakery, and so on). That thing to remember is that the customer probably doesn’t care about HTML, CSS, or JavaScript. They care about whether the website performs well in search and whether customers come into their business as a result.

This means that you need to build the website with search engine optimization (SEO) in mind. One of the bigger developments recently in the area of SEO is Google’s increasing use of “structured data” in its analysis of websites. This trend made me decide to write this article on the use of structured data in your various web projects.

I’m going to divide this discussion up into four sections. The areas I’m going to delve into include:

1. What is structured data and why does Google care about it?
    
2. How to use structured data in a website.
    
3. How to test your structured data and monitor for errors after the site launches.
    
4. The need to keep your structured data up to date after the website launches.
    

This is an important discussion to have. I find that many, many, many, many……(many) people who hold themselves out as web developers don’t actually know much (if anything) about SEO.

I also find that many people who hold themselves out as assisting with SEO don’t actually know anything about web development (and often can barely code at all).

Someone who can actually code, and who understands what the search engines are looking for, can provide a great deal of value to their customers. This value, in turn, helps you to make more money as a developer. In other words, pairing an understanding of SEO with your newly learned web development skills can help you go from looking like this:

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Computer-with-help-sign.jpg align="left")

To looking like this:

![Image](https://www.freecodecamp.org/news/content/images/2019/08/computer-and-money.jpg align="left")

So let’s get to it and discuss why structured data is important to a website’s SEO.

### What is structured data and why does Google care about it?

Structured data is form of markup you can apply to your website’s content. This markup allows you to provide information to search engines about your web pages and the information they contain.

This markup is important because search engines, while getting better at understanding natural language, can struggle with understanding the wording or other content contained within a web page.

For example, if someone is searching for “professional to help with investing,” search engines may struggle to distinguish between sites which belong to investment managers and sites which discuss how to pick an investment manager in general (this is a very generalized example).

By using structured data, you can help Google know that your website actually belongs to an investment manager.

Another purpose of structured data is that it helps search engines identify who is who on the web. Suppose, for example, you're doing a website for a political candidate. The candidate, in addition to an official campaign website, has an official Facebook page for the campaign.

For obvious reasons, there may be people who start false Facebook pages about the candidate. By including certain structured data in the website, you can create a relational link between the official Facebook page and the campaign’s website. This helps the search engines to know which Facebook page is legit and which one is bogus.

Google has been working to identify who is who on the web for roughly a decade. This started with their now defunct social network, Google+ (you know…..that social network that you may have tried but none of your friends were on).

Back in the early part of this decade, if a website included a link to a Google+ profile, and the link included the “rel=author” attribute, the link informed Google that the website belonged to the holder of the Google+ profile. This was something Google intended to ratchet up in search, as one of their executives explained in this 2013 video:

%[https://www.youtube.com/watch?v=3QlY8ba0jYI] 

Google abandoned this approach, mainly due to the struggles of Google+, in August of 2014. Since that time, Google has been increasing its emphasis on structured data as a way of annotating information in search results and identifying who is who on the web.

So, in short, structured data is something you should be including to add value to any website you build for your clients.

### How to use structured data in a website

Structured data can be used in a number of ways. In addition to using it to help identify the individual or entity operating the site, you can use it to help Google better understand a page’s content.

If, for example, you’ve built a website for a bakery, then there are types of markup you can use to highlight the business’ good reviews, to highlight upcoming events, and so on. This markup can lead to highlights in search results which, in turn, will make your customer (the bakery owner) happy.

Let’s look at a few examples of what this looks like in real life, using a [real estate agent website](https://www.dayton-real-estate-agent.com/) which I recently built (I'm including the link in case you want to take a look at the code).

The realtor I built the website for focuses her business on dealing with investors. The website includes structured data which informs Google that the site belongs to an actual real estate agent. When I perform a Google search for “Dayton realtor for investors,” the top three organic results I receive are as shown in this photo:

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Investor-search.png align="left")

The first result is the website I built. The latter two are websites which do not belong to actual real estate agents, even though that is what I was clearly looking for with my search term. In fact, only one other realtor website even appears on the first page of the search results. Now, I’m not saying that this is entirely due to the structured data, but it certainly helps.

The markup used for structured data is generated/governed by [Schema.org](https://schema.org/). When you’re marking up a site, an individual page, an event, or a product, it’s important to use as much markup as is *reasonably* possible in order to provide the search engines with relevant information.

Schema.org's website often provides examples of what your markup should look like. The start of the markup that I used for the realtor site involved informing Google that the site belonged to a real estate agent by placing the following inside of a

:

```html
<itemscope itemtype=http://schema.org/RealEstateAgent>
```

This tells the search engines that I am relying on schema’s markup to identify and describe the site and that the site belongs to a real estate agent, as defined by schema [here](https://schema.org/RealEstateAgent).

I was also able to use structured data to tell Google that this realtor has good online reviews and that they work on commission. This, in turn, is now showing up in search results.

For example, the page at the following link is on the first page of search when I look for [Dayton apartments for sale](https://www.dayton-real-estate-agent.com/apartments-multi-family-homes-for-sale/). (Again, I'm including this link in case you want to look at the site's source code).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/multifamily-1.png align="left")

Notice that the search results include the fact that this is a five-star rated realtor and that the professional works on commission? In other words, the use of structured data helps the site to stand out more in the search results. This information was added to the site with the following markup:

```html
<div itemprop="aggregateRating" itemscope itemtype="http://schema.org/AggregateRating">
Rated <span itemprop="ratingValue">Actual Rating of Realtor</span> out of <span itemprop="bestRating">Highest Possible Rating of Realtor</span> by <span itemprop="ratingCount">Number of Total Reviews</span> clients at <a href="URL of Website Where Reviews Are Located" target="_blank" rel="noopener">Name of Website Where Reviews Are Located</a>
Fee Structure: <span itemprop="priceRange">Commission</span>
</div>
```

Figuring out what structured data to use in a site, or on a particular page, can be difficult. Fortunately, Google gives a few tools that help with this. Let’s look at those tools in the following section of this article.

### Testing your structured data and monitoring it after your site launches

The first step in adding structured data to your content is to figure out the category it falls into. You can do this by researching the Schema.org website, looking at the data from other websites, or a combination of both. Once you find the category you fall into, the rest is pretty easy. Let’s stick with the real estate agent example from above.

The first step is to add the realtor markup, from Schema, the site. Then enter your url into [Google’s structured data testing tool](https://search.google.com/structured-data/testing-tool). The tool will tell you what structured data has been found on your site, what errors you may have, and what structured data is “suggested” for the category you’ve selected. Once you start using this tool, you’ll find that making sure you have the right information in the website becomes fairly simple and straightforward.

Also, I heavily rely on the examples which Schema provides for various categories and data types. Using Google’s testing tool can help you to make sure that you have the correct data in your site from the get go.

Another important tool, in monitoring for errors, is [Google Search Console](https://search.google.com/search-console/about). This is another developer tool, from Google, that will let you know when structured data errors appear on your website after launch. This is an incredibly useful tool and if you’re supporting your client’s website on an ongoing basis, after launch, then you need to be using it to monitor things.

### The need to keep your structured data up to date after a website launches

It is important to understand that you may need to go back and edit a site’s older structured data after a site launches. This is because, like many other things, the standards for structured data change over time. As an example, I build and maintain websites for law firms as part of my primary business. Under the prior structured data standards, these websites were marked up with the following:

In later revisions to the structured data standards, however, the “Attorney” classification was deprecated and changed to “LegalService” – as such, I had to change the markup on each website I manage. I tell you this because it’s important to realize that these standards change somewhat often. It’s important that you keep up with the changes.

### Conclusion

Web results are becoming increasingly rich in that they provide more information than just a link to a website. It’s important for your clients that you markup your pages accordingly. Doing so is important to your SEO efforts and to providing value to your customers. This is why it’s important to include structured data in your projects.

### About Me

I am a web developer who primarily provides various types of services to law firms. I am also a co-founder of [Modern Website Design](https://www.modern-website.design/). I enjoy writing on issues which help freelance developers and small businesses to grow their revenue.
