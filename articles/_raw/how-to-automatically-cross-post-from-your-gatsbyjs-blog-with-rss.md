---
title: How to Automatically Cross-post from Your GatsbyJS Blog with RSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-11T18:45:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-automatically-cross-post-from-your-gatsbyjs-blog-with-rss
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/gatsby-rss.jpg
tags:
- name: blog
  slug: blog
- name: canonical url
  slug: canonical-url
- name: Gatsby
  slug: gatsby
- name: GatsbyJS
  slug: gatsbyjs
- name: rss feed
  slug: rss-feed
- name: SEO
  slug: seo
seo_title: null
seo_desc: 'By Dane Stevens

  With the recent exodus from Medium many developers are now creating their own GatsbyJS
  Blogs and then cross-posting to Medium or publications like freecodecamp.org and
  dev.to.

  Cross-posting is time consuming, but necessary to drive tr...'
---

By Dane Stevens

With the recent exodus from [Medium](https://medium.com) many developers are now creating their own GatsbyJS Blogs and then cross-posting to [Medium](https://medium.com) or publications like [freecodecamp.org](https://www.freecodecamp.org/news/) and [dev.to](https://dev.to).

Cross-posting is time consuming, but necessary to drive traffic to your personal site. Let's look at how we can automate this by adding an RSS feed to your personal GatsbyJS blog.

## Add Canonical URL's to Your Blog

What is a canonical url?

![Canonical URL for Tueri.io](https://cdn.tueri.io/274877907146/carbon.png)

A canonical url tells search engines which page is the primary or authorative page when duplicate content is found (ie. cross-posting).

Let's install [gatsby-plugin-canonical-urls](https://www.gatsbyjs.org/packages/gatsby-plugin-canonical-urls/)

**Quick tip:** `npm i` is an alias for `npm install --save`

```
npm i gatsby-plugin-canonical-urls

```

**Note:** If you are using `gatsby-plugin-react-helmet` install this plugin instead: [gatsby-plugin-react-helmet-canonical-urls](https://www.gatsbyjs.org/packages/gatsby-plugin-react-helmet-canonical-urls/)*

```
npm i gatsby-plugin-react-helmet-canonical-urls

```

Add plugin configuration to `/gatsby-config.js`

```javascript
// In your gatsby-config.js
plugins: [
  {
    resolve: `gatsby-plugin-canonical-urls`,
    // or
    // resolve: `gatsby-plugin-react-helmet-canonical-urls`
    options: {
      // Change `siteUrl` to your domain 
      siteUrl: `https://tueri.io`
      
      // Query string parameters are inclued by default.
      // Set `stripQueryString: true` if you don't want `/blog` 
      // and `/blog?tag=foobar` to be indexed separately
      stripQueryString: true
    }
  }
]

```

With this configuration, the plugin will add a `<link rel="canonical" ... />` to the head of every page e.g.

```html
<link rel="canonical" href="https://tueri.io/2019-04-04-how-to-securely-deploy-to-kubernetes-from-bitbucket-pipelines/" />

```

## Install an RSS Feed Generator

We'll use [gatsby-plugin-feed](https://www.gatsbyjs.org/packages/gatsby-plugin-feed/) to generate an rss feed from our blog posts.

```
npm i gatsby-plugin-feed

```

Add plugin configuration to `/gatsby-config.js`

```javascript
// In your gatsby-config.js
plugins: [
  {
    resolve: `gatsby-plugin-feed`,
    options: {
      query: `
        {
          site {
            siteMetadata {
              title
              description
              siteUrl
              site_url: siteUrl
            }
          }
        }
      `,
      feeds: [
        {
          serialize: ({ query: { site, allMarkdownRemark } }) => {
            return allMarkdownRemark.edges.map(edge => {
              return Object.assign({}, edge.node.frontmatter, {
                description: edge.node.excerpt,
                date: edge.node.frontmatter.date,
                url: site.siteMetadata.siteUrl + edge.node.fields.slug,
                guid: site.siteMetadata.siteUrl + edge.node.fields.slug,
                custom_elements: [{ "content:encoded": edge.node.html }],
              })
            })
          },
          query: `
            {
              allMarkdownRemark(
                sort: { order: DESC, fields: [frontmatter___date] },
              ) {
                edges {
                  node {
                    excerpt
                    html
                    fields { slug }
                    frontmatter {
                      title
                      date
                    }
                  }
                }
              }
            }
          `,
          output: "/rss.xml",
          title: "Your Site's RSS Feed",
          // optional configuration to insert feed reference in pages:
          // if `string` is used, it will be used to create RegExp and then test if pathname
          // of current page satisfied this regular expression;
          // if not provided or `undefined`, all pages will have feed reference inserted
          match: "^/blog/",
        },
      ],
    }
  }
]

```

**NOTE:** This plugin will only generates the `xml` file(s) when run in `production` mode! To test your feed, run: `gatsby build && gatsby serve`

Here's what our feed looks like: [Tueri.io's RSS Feed](https://tueri.io/rss.xml)

For more information on configuring your feed check out the [plugin docs](https://www.gatsbyjs.org/packages/gatsby-plugin-feed/).

## Connect [dev.to](https://dev.to) to Your RSS Feed

1. Log in to your [dev.to](https://dev.to) account
2. Go to: Settings > Publishing from RSS or [https://dev.to/settings/publishing-from-rss](https://dev.to/settings/publishing-from-rss)
3. Add your "RSS Feed URL" e.g. [https://tueri.io/rss.xml](https://tueri.io/rss.xml)
4. Check "Mark the RSS source as canonical URL by default
5. Click "Update"

![Screenshot of dev.to RSS settings](https://cdn.tueri.io/274877907149/screencapture-dev-to-settings-publishing-from-rss-2019-06-06-06_48_32.png)

## Connect [Medium](https://medium.com) to Your RSS Feed

The connection for [Medium](https://medium.com) is not quite as straight-forward, but simple enough using [Zapier](https://zapier.com).

Head on over to [Zapier](https://zapier.com) and create a free account.

### "Make a Zap"

1. Choose "RSS" as your "Trigger App"
2. Select "New Item in Feed"
3. Paste in your "Feed URL"
4. Select a sample from your feed.
5. Choose "Medium" as your "Action App"
6. Select "Create Story"
7. Authorize your Medium account
8. Select your fields: make sure you select your Canonical URL
9. Send a test to Medium
10. Finish and turn on your Zap

![Screenshot of connecting RSS to Medium with Zapier](https://cdn.tueri.io/274877907150/screencapture-zapier-app-editor-59814153-nodes-59814313-fields-2019-06-06-06_53_55.png)

## Conclusion

Make sure Google gives you credit for your content by using Canonical URL's.

I hope you found this helpful and that it saves you lots of time cross-posting your content!

---

_Originally published at [Tueri.io](https://tueri.io/blog/2019-06-06-how-to-automatically-cross-post-from-your-gatsbyjs-blog-with-rss/?utm_source=Freecodecamp&utm_medium=Post&utm_campaign=)_


