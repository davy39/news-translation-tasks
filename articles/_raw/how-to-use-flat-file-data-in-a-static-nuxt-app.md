---
title: How to Use Flat-File Data in a Static Nuxt App
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-19T18:33:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-flat-file-data-in-a-static-nuxt-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/flat_file_db.jpg
tags:
- name: database
  slug: database
- name: JavaScript
  slug: javascript
- name: Nuxt.js
  slug: nuxtjs
seo_title: null
seo_desc: 'By Anthony Gore

  Making your Nuxt web app static can potentially save you the time and money of setting
  up a server-rendered app. It may also offer superior performance.

  But what if your app needs dynamic data? The most popular solution is to set up
  a...'
---

By Anthony Gore

Making your Nuxt web app static can potentially save you the time and money of setting up a server-rendered app. It may also offer superior performance.

But what if your app needs dynamic data? The most popular solution is to set up an API alongside your static app that can deliver dynamic data via AJAX.

In this article, I'll show you another possible architecture - using a flat-file database. This architecture might save you the hassle of setting up an API and offers superior performance.

## What is a flat-file database?

A "flat-file database" is a database architecture where data is stored in a simple text file rather than in database software like MySQL or MongoDB.

In a Nuxt app, this file can be a JSON file that sits in your static files directory and is deployed alongside the markup files.

At runtime, the JSON file is loaded by the Nuxt app. Once the data is parsed as JavaScript data it can be used to power the app.

## Why use a flat-file database?

Flat-file databases are advantageous because of their simplicity and low overhead. But they are also insecure and don't offer the performance benefits of conventional database software, which is why they're rarely used.

In the context of Nuxt apps, though, they have another great advantage – they can be stored and accessed from static hosting.

Using a flat-file database may also have a performance advantage over an API service which will have a small latency overhead incurred when requests are processed by the server.

However, flat-file DBs won't always be appropriate to use, as they offer no security and are read-only while in production. This means you'll need to rebuild the site any time you want to write new data.

A type of data that is a good candidate for flat-file storage and retrieval is meta data. For example, on the [Vue.js Developers blog](https://vuejsdevelopers.com/), which I built with Nuxt, I use a flat-file database to store meta data about published posts.

This allows me to easily access that data across the site, for example on the home page where the latest blog articles are displayed, and on the topics page which indexes posts based on topic tags applied (both shown below).

![Vue.js Developers Blog](https://s3.us-east-2.amazonaws.com/downloads.vuejsdevelopers.com/flat_file_db_image_1.png)

## Implementing the flat-file database architecture in Nuxt

Now let's see how to implement the flat-file database architecture in your own Nuxt site.

Say we want to create a blog home page which show the latest published article like that on the Vue.js Developers blog.

We'll begin by seeing how flat-file-sourced data gets used in the page, and then work backwards until we can see how the whole architecture works.

### Using flat-file data in a page

In our home page component, _pages/index.vue_, we'll import `getArticleSummaries` from a soon-to-be-created JavaScript module `flatFileDb`.

This method will return a Promise containing the article summary data ready for use on the page.

You can, of course, use this data at build time via `asyncData`, and at run time via the `created` hook.

_pages/index.vue_:

```js
const { getArticleSummaries } from "@/assets/js/flatFileDb";

export default {
    data: () => ({
        articleSummaries: []
    }),
    async asyncData () {
        const articleSummaries = await getArticleSummaries();
        return { articleSummaries }
    },
    async created () {
        this.articleSummaries = await getArticleSummaries();
    }
}

```

Note that the data structure we'll get from `getArticleSummaries` will be an array of objects like this:

```js
[
    {
        title: "...",
        description: "...",
        published: "...",
        ...
    },
    ...
]

```

Note: If you have multiple entities (for example, in addition to articles you also store information about videos), each will have its own flat file and its own retrieval method in the app, like `getVideoSummaries`.

### Flat-file database module

We saw above that a `getArticleSummary` method was imported from the `flatFileDb` module. Let's see how we can implement that.

Our flat-file database will be included in our static files and should be a JSON file since these are simple to parse as valid JavaScript data.

We'll include this JSON file by using a dynamic import. This feature is designed for importing JavaScript modules, but it works with JSON files out-of-the-box with Webpack. Conveniently, you get the JSON file already parsed as JavaScript.

It's important to call the dynamic import in a `try/catch` block to prevent the app crashing if the file is missing or the JSON parsing fails.

Before we return the data to the consuming component we need to "decode" it with another custom method `decodeArticleSummaries`. I'll explain that in a moment.

Finally, note that a JSON file doesn't have a default export, so you'll need to access the `default` property of the db module to access the data.

_assets/js/flatFileDb.js_:

```js
import { decodeArticleSummaries } from "dbDecoders";

const getArticleSummaries = async () => {
    try {
    const db = await import(`@/static/article-summaries.json`);
    return decodeArticleSummaries(db.default);
  } catch (err) {
    console.log(err);
    return [];
  }
};

export { getArticleSummaries };

```

### Decoding the database

Above, I said the data provided to the component would look like this:

```
{
    title: "...",
    description: "...",
    published: "...",
    // etc
}

```

However, it shouldn't be stored in the database like this because the property names are wastefully long.

In order to keep the flat file as lean as possible we should "encode" each key when the database is created. Then we should decode them before they're consumed by components so they have their full names available to the developer.

So, let's say we make "title" => "t", "description" => "d", and "published" => "p". In a large database, this transformation could reduce the file size by many bytes.

_assets/js/dbDecode.js_:

```js
const decodeArticleSummaries = db => {
    return db.map(article => ({
        title: article.t,
        description: article.d,
        published: article.p
        // etc
    }));
}

```

## Generating the flat-file database

So now we've seen how the flat-file database is consumed at run time. How is it created?

You could create a flat-file database manually by hand, but usually you'll want to generate it at build time with a Node.js script.

In our example, we'll want to make a script that extracts the meta data of each article and stores it as _static/article-summaries.json_. Let's assume the articles are stored as markdown and are in an "articles" directory in the project root.

The details of the script will be specific to your implementation, so I'll just give you pseudo code to communicate the basic idea.

_scripts/generateDb.js_:

```js
const fs = require("fs");
const frontmatterExtractor = require("./frontmatterExtractor");
const encodeArticleSummaries = require("./encodeArticleSummaries");

module.exports = async () => {
    // Load article files
    const articles = await fs.readdir("/articles", (err, filePaths) => {
        // Create the database by reading each file
        const db = filePaths.map(async path => {
            const file = await fs.readFile(path);
            // Extract the meta data
            return frontmatterExtractor(file);
        });
        // Encode the data
        const encoded = encodeArticleSummaries(db);
        // Write the database object to a JSON file
        await fs.writeFile(
            "/static/article-summaries.json", 
            JSON.stringify(encoded)
        );
    });
}

```

## Running the DB generator script before the site build

Now that we've got a database generator script, let's trigger it to run just before the build (or generate) processes which will want to consume it.

To do this, we'll squeeze it into the NPM commands in _package.json_. Note that by using the `&&` operator we can ensure the Nuxt process doesn't begin until the generator script completes.

_package.json_:

```json
{
    ...
    "scripts": {
        ...
        "build": "node scripts/generateDb && nuxt build",
        "generate": "node scripts/generateDb && nuxt generate",
        ...
    }
    ...
}

```

In development, however, I find it easier to manually generate the database on the command line whenever I need to update it:

```
$ node scripts/generateDb

```

## Further reading

That's the basic architecture explained. Here are a few other articles learn more:

* [Going JAMstack with Netlify and Nuxt](https://blog.lichter.io/posts/jamstack-nuxt-netlify/)
* [Multiple Ways of API Integration in your JAMStack](https://www.raymondcamden.com/2019/07/25/multiple-ways-of-api-integration-in-your-jamstack)
* [Including Markdown Content in a Vue or Nuxt SPA](https://vuejsdevelopers.com/2018/12/31/vue-nuxt-spa-markdown/)

