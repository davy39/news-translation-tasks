---
title: Reducing CSS bundle size 70% by cutting the class names and using scope isolation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-12T22:50:35.000Z'
originalURL: https://freecodecamp.org/news/reducing-css-bundle-size-70-by-cutting-the-class-names-and-using-scope-isolation-625440de600b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mGuDYFM56iyLi1MgZPC8bw.png
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: SEO
  slug: seo
- name: Web Development
  slug: web-development
- name: webpack
  slug: webpack
seo_title: null
seo_desc: 'By Gajus Kuizinas

  Just like Google does it

  At the beginning of this year I have quit consulting and set out to build GO2CINEMA
  — Fast, simple and secure way to book cinema tickets in the UK. I have done a splendid
  job making it fast, simple and secur...'
---

By Gajus Kuizinas

#### Just like Google does it

At the beginning of this year I have quit consulting and set out to build [GO2CINEMA](https://go2cinema.com/) — Fast, simple and secure way to book cinema tickets in the UK. I have done a splendid job making it _fast, simple and secure_. Somewhere along the way, I’ve gotten obsessed with the critical rendering path optimization ⚡️.

I have solved pre-rendering of the HTML using [ūsus](https://github.com/gajus/usus). ūsus renders HTML of single page applications (SPA) and [inlines the CSS used to render the page](https://medium.com/@gajus/pre-rendering-spa-for-seo-and-improved-perceived-page-loading-speed-47075aa16d24). However, I did not like inlining 70 KB into every HTML document, esp. most of it being the CSS class names.

#### Just like Google does it

Have you ever peeked into the source code of [https://www.google.com/](https://www.google.com/)? The first thing you will notice is that the CSS class names are no more than a couple of characters long.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mGuDYFM56iyLi1MgZPC8bw.png)
_google.com HTML_

But how?

#### Shortcomings of the CSS minifiers

There is one thing a minifier cannot do – change the selector names. This is because a CSS minifier does not control the HTML output. Meanwhile, CSS names can get long.

If you are using CSS modules, your CSS modules are likely going to include stylesheet file name, local identifier name and a random hash. The class name template is described using [css-loader `localIdentName`](https://github.com/webpack-contrib/css-loader) configuration, e.g. `[name]___[local]___[hash:base64:5]`. Therefore, a generated class name will look something like this `.MovieView___movie-title___yvKVV` ; if you like descriptive names, it can get a lot longer, e.g `.MovieView___movie-description-with-summary-paragraph___yvKVV` .

#### Renaming CSS class names at the compilation time

However, if you are using [webpack](https://webpack.js.org/) and [babel-plugin-react-css-modules](https://github.com/gajus/babel-plugin-react-css-modules), you are in luck ? – you can rename class names at the compilation time using c[ss-loader g`etLocalIdent`](https://github.com/webpack-contrib/css-loader) configuration and the equivalent babel-plugin-react-css-modules g`[enerateScopedName](https://github.com/gajus/babel-plugin-react-css-modules#configuration)` configuration.

The cool thing about `generateScopedName` is that the same instance of the function can be used for Babel and webpack build process:

#### Making the names short

Thanks to `babel-plugin-react-css-modules` and `css-loader` sharing the same logic to generate the CSS class names, we can change the class names to whatever we like, even a random hash. However, instead of a random hash, I wanted the shortest possible class names.

To generate the shortest class names, I have created class name index and used the `[incstr](https://github.com/grabantot/incstr)` module to generate incremental IDs for every entry in the index.

This guarantees short and unique class names. Now, instead of `.MovieView___movie-title___yvKVV` and `.MovieView___movie-description-with-summary-paragraph___yvKVV` our class names have become `.a_a`, `.b_a`, etc.

This has reduced [GO2CINEMA](https://go2cinema.com/) CSS bundle size from 140 KB to 53KB.

#### Using Scope isolation to further reduce the bundle size

There is a good reason I have added `_` into the CSS class name separating the component name and the local identifier name – the distinction is useful for minification.

[csso](https://github.com/css/csso) (CSS minifier) has [scopes](https://github.com/css/csso#scopes) configuration. Scopes define lists of class names that are exclusively used on some markup, i.e. selectors from different scopes don’t match the same element. This information allows the optimizer to move rules more aggressive.

To leverage this, use [csso-webpack-plugin](https://github.com/zoobestik/csso-webpack-plugin) to post-process the CSS bundle:

This has reduced [GO2CINEMA](https://go2cinema.com/) CSS bundle size from 53 KB to 47 KB.

#### Is it worth it?

The first argument against such minification is that the compression algorithms will do it for you. GO2CINEMA CSS bundle compressed using the [Brotli](https://en.wikipedia.org/wiki/Brotli) algorithm saves a mere 1 KB compared to the original bundle with the long class names.

On the other hand, setting up this minification is a one-time investment and it reduces the size of the document that needs to be parsed. It has other benefits, such as deterring scapers that rely on the CSS class names to navigate or accidentally matching CSS selectors of the ad-blocker [blacklists](https://gist.github.com/spyesx/42fe84c0ef757d1c38a4).

Meanwhile, you can see a demo of this minification being used on the GO2CINEMA movie and venue pages, e.g.

* [https://go2cinema.com/movies/wonder-woman-2017-1305237](https://go2cinema.com/movies/wonder-woman-2017-1305237)
* [https://go2cinema.com/venues/odeon-oxford-magdalen-st-1001053](https://go2cinema.com/venues/odeon-oxford-magdalen-st-1001053)

#### Can you help me with GO2CINEMA?

[GO2CINEMA](https://go2cinema.com/) is my baby. I love working working on it ?. However, it is my first startup this decade and there are a lot of things I need help with.

If you can give feedback, an SEO advice, a business advice, know an angel investor, know someone who can write an article about [GO2CINEMA](https://go2cinema.com/), make a tweet, invite me to a conference, a radio talk show, etc. or just want to express your support/ curiosity and say “Hi!”, email me at gajus@gajus.com or DM via Twitter, [https://twitter.com/kuizinas](https://twitter.com/kuizinas).

### You like to read, I love to write

You can support my [open-source work](https://github.com/gajus) and me writing technical articles through [Buy Me A Coffee](https://www.buymeacoffee.com/gajus) and [Patreon](https://www.patreon.com/gajus). You’ll have my eternal gratitude ?

