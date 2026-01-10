---
title: Lume SSG Handbook – How to Create a Static Blog with Lume
subtitle: ''
author: Rajdeep Singh
co_authors: []
series: null
date: '2022-11-18T17:06:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-static-blog-with-lume
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/Create-a-Static-Blog-with-Lume.png
tags:
- name: Deno
  slug: deno
- name: Static Site Generators
  slug: static-site-generators
seo_title: null
seo_desc: "Lume is a new static site generator based on Deno. Deno is a JavaScript-based\
  \ run-time environment that supports TypeScript. \nLume is not built around any\
  \ specific language. It supports Markdown, Nunjucks, TypeScript, and JavaScript\
  \ by default. Lume ..."
---

Lume is a new static site generator based on Deno. Deno is a JavaScript-based run-time environment that supports TypeScript. 

Lume is not built around any specific language. It supports Markdown, Nunjucks, TypeScript, and JavaScript by default. Lume also supports plugins. Some plugins come preinstalled by default. This is why Lume itself is template-language agnostic.

Before learning more about Lume, let's discuss Deno and consider some important Deno features.

## What is Deno?

Deno is an alternative to Node.js built by [Ryan Dahl](https://en.wikipedia.org/wiki/Ryan_Dahl) (who also developed Node). Deno is based on the Rust programming language, and the second main component in Deno is the JavaScript V8 engine for WebAssembly.

Deno has many cool features – it's fast, secure by default, is compatible with web assembly and has TypeScript support, has in-built development tools, and more. Deno also supports Node.js APIs so you can use all npm packaged with Deno.

In Deno, you do not need to create a configuration file to run a simple program. You simply deploy your website instantly with a second on-edge network. But my final favorite feature is the new `node_modules` folder in the workspace. Deno caches all the packages locally and uses them, which is very fast compared to Node.

You can check out the [demo blog website here,](https://minimalist-blog.deno.dev/) and all the [code is available on GitHub here](https://github.com/officialrajdeepsingh/Minimalist-blog).

Now let's dive into the tutorial.

## Table of Contents

1. [Lume + Markdown](#heading-lume-markdown)
2. [Why is Lume special?](#heading-why-is-lume-special)
3. [How does Lume compare to other static site generators?](#heading-how-does-lume-compare-to-other-static-site-generators)
4. [How to start a new project with Lume](#heading-how-to-start-a-new-project-with-lume)
5. [Lume folder structure](#heading-lume-folder-structure)
6. [Additional folders](#additional-folders)
7. [How to create global data](#heading-how-to-create-global-data)
8. [How to create a dynamic page](#heading-how-to-create-a-dynamic-page)
9. [How to create a Home and Pagination page](#heading-how-to-create-a-home-and-pagination-page)
10. [How to build an articles page](#heading-how-to-build-an-articles-page)
11. [How to generate a category page](#heading-how-to-generate-a-category-page)
12. [How to generate a tag page](#heading-how-to-generate-a-tag-page)
13. [How to enable search functionality](#heading-how-to-enable-search-functionality)
14. [How to install page find](#heading-how-to-install-page-find)
15. [Lume SEO](#heading-lume-seo)
16. [Lume Sitemap](#heading-lume-sitemap)
17. [Lume plugins](#heading-lume-plugins)
18. [How to enable comments](#heading-how-to-enable-comments)
19. [How to use Netlify CMS with Lume](#heading-how-to-use-netlify-cms-with-lume)
20. [How to deploly your blog with Deno Deploy](#heading-how-to-deploy-your-blog-with-deno-deploy)
21. [Github pages](#github-pages)
22. [Conclusion](#heading-conclusion)

## Lume + Markdown

Lume is a new static site generator based on Deno created and maintained by [Óscar Otero](https://github.com/oscarotero). Lume uses **markdown-it** as the default markdown. You can use the [remark plugin](https://lume.land/plugins/remark/) to change the default markdown.  

Markdown is a language that helps to write documents, readme files, and blogs on the internet. [John Gruber](https://en.wikipedia.org/wiki/John_Gruber) created markdown in 2004.

**Markdown-it** is similar to [GitHub-flavored Markdown](https://github.github.com/gfm/) (GFM) markdown. GFM and [markdown-it](https://github.com/markdown-it/markdown-it) both follow the exact [markdown specifications](https://commonmark.org/). 

If you've worked with GitHub and written README files, that means you are likely familiar with GFM markdown. If you don't like the default (markdown-it) markdown, you can change the markdown with the remark plugin.

There are tons of static site generators. So why is Lume special? What does it provide compared to other static site generators? Let's find out.

## Why is Lume special?

As you know, Lume is built on Deno, and Deno is a Node.js alternative—that is why Lume provides lots of features out of the box. 

Lume works similarly to a GitHub readme file. If you're familiar with writing one of those (and using markdown), you do not need to learn anything else to write articles and documentation with Lume.

Here are some benefits of Lume:

1. Lume supports multiple template engines like Markdown, [Nunjucks](https://lume.land/plugins/nunjucks/), [Eta](https://lume.land/plugins/eta/), [JSX](https://lume.land/plugins/jsx/), [Liquid](https://lume.land/plugins/liquid/), or [Pug](https://lume.land/plugins/pug/).
2. It supports multiple authors
3. It has code syntax highlighting
4. There's great SEO support
5. Lume supports multiple languages
6. It has Windi CSS support
7. There's pagination and component support
8. It supports minifying JavaScript, HTML, CSS, and SASS
9. It has relations support
10. There is the built-in search functionality
11. It supports Netlify CMS
12. It supports images and SVGs
13. There's Remark.js plugin support
14. You can deploy with Netlify, Vercel, GitLab Pages, and the GitHub page.

## How Does Lume Compare to Other Static Site Generators?

Lume is a new static site generator compared to others, but it comes with many configuration options, and you can do anything with it. You don't even need to use any third-party plugins. 

With Lume processors and preprocessors, you can easily manipulate the HTML code with the JavaScript DOM API. Other static site generators support a few template engines, but Lume supports many template engines like JavaScript, JSX, Nunjucks, Eta, JSX, Liquid, and Pug.

Note that Lume can seem tough to get started with for beginners. But if you're following my article, just make sure to [open the code](https://github.com/officialrajdeepsingh/Minimalist-blog) which will make things much clearer for you.

## How to Start a New Project with Lume

You can set up a new project with the Lume CLI with this command:

```bash
deno run -Ar https://deno.land/x/lume/init.ts
```

![Lume installation demo](https://www.freecodecamp.org/news/content/images/2022/11/lume-installation-low.gif)
_Lume installation demo_

#### Follow these steps:

1. First, create an empty  `mkdir lume-deno` folder project.
2. Then run the lume `init.ts` command.
3. Select an available plugin from the list.

And you should be up and running.

## Lume Folder Structure

After the installation finished, we saw three files:

1. `_config file` is used to configure Lume.
2. `deno.json` is a defined script or task for Deno.
3. `import_map.json` is to help you import a Deno package for the internet.

![lume default folder structure ](https://www.freecodecamp.org/news/content/images/2022/11/folder-struture-1.png)
_lume default folder structure_

### How to run the Lume server

To run a local development server, you'll use the `deno task lume --serve` command. To build a website, run the `deno task build` command.

If you face a 404 - not found error, you can create a `index.njk` file within the root folder.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/lume404-1.png)

In the `index.njk` file, paste the following code.

```nunjucks
---
title: "hello"
---
hello world
```

And you'll see the following output:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/hello-world-lume-2.png)
_Lume hello-world_

### Additional folders:

1. `posts` folder is not a compulsory folder. It contains all your posts' markdown files.
2. `pages` folder is not a compulsory folder. It has all your pages' markdown files.
3. `author` folder is not a compulsory folder. It has all your author markdown files.
4. `_components` folder is a **compulsory** folder. It has all your components.
5. `_includes`  folder is a **compulsory** folder. It contains your layout and templates for your site.
6. `images` folder is not a compulsory folder. It contains all your images.

The posts, pages, authors, and images folders are optional. You can rename these folders according to your wishes. The `_components` and `_includes` folders are mandatory and you don't rename them.

The difference between components, layout, and template are as follows:

* The components are reusable code
* The layout and template are not reusable like components.

## How to Create Global Data

In Lume, you can create a data variable, which has access to the entire website by all template engines.

```javascript
// Set a variable
site.data("post_per_page", 10);

// Set a function
site.data("randomNumber", function () {
  return Math.random();
});
```

#### How to create posts, pages, and author markdown files

You create posts, pages, and author folders in the root folder. Then, inside every folder, you write markdown files.

You can access all posts, pages, and authors by file name on the browser:

1. `localhost:3000/posts/your-title.html`
2. `localhost:3000/pages/your-pages.html`
3. `localhost:3000/author/your-author.html`

Suppose you need a demo post, pages, and author markdown for a project or template. Then, you can use [demo-markdown posts](https://github.com/officialrajdeepsingh/Demo-markdown-posts) for your project. It is free and open source, and you can create your own template.

### How to create a dynamic page

In Lume, `.tmpl.js` and `.tmpl.ts` extensions use JS and TS as [template engines](https://lume.land/plugins/modules/). You can use them with regular pages or dynamic pages to create categories, tags, pagination, and so on for your website.

### How to create a home and pagination page

The home page is based on pagination, and pagination is based on posts. Lume dynamically generates the pagination. 

In Lume, I chose nunjucks and JavaScript to create my demo website. Nunjucks is the default template engine. You can easily change the default Nunjucks engine with another template engine with copy-paste code.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Home-page-1.png)
_home page_

Lume provides a JavaScript template function that helps create dynamic web pages. If you create a home page for the site, you need to create an `index.tmpl.js` file in your root or src folder. Lume also supports an src folder to organize your project. In my demo project, I'm not using the `src` folder.

The  `*.tmpl.js` is an extension of a [JavaScript template](https://lume.land/plugins/modules/#creating-pages) that helps create dynamic pages for websites. It comes pre-installed in Lume with the [modules plugin](https://lume.land/plugins/modules/).

For example, the following code creates pagination for your website. But the layout comes from the `_includes` folder.

```javascript
// index.tmpl.js

// title for SEO
export const title = "Minimalist blog"
// description for SEO
export const description = "Minimalist blog theme is liteweight and work with lume."

export default function* ({ search, paginate }) {

//  Get all posts of type article.
  const posts = search.pages("type=article", "date=desc");

  // Configation for pagination
  const options = {
    // Page 1 is the homepage, set "/" as url
    url: (n) => n === 1 ? "/" : `/page/${n}/`,
    // par page posts
    size: 7,
  };

  // Yield the pages, but the index needs a different layout
  for (const page of paginate(posts, options)) {

    //  if home page, use diffrent layout "/"
    if (page.pagination.page === 1) {
      page.menu = {visible: true, order: 1, title:"Home" }
      page.title = "Home page"

      //  comes from _includes folder

      page.layout = "layouts/home.njk";
    } else {
      // Render diffrent layout if it is not home page page "/page/2","/page/3",etc
      page.title = "Pagination page"

      page.layout = "layouts/home.njk";
    }
    
    yield page;
  }

}
```

‌Lume has a [search plugin](https://lume.land/plugins/search/) that helps you search pages. In my demo blog, I search all pages base on the type. 

In my all posts folder, all posts are defined in `type=article`, the author is described in `type=author`, and pages are defined in `type=page` . The search plugin is pre-installed with Lume.

On `index.tmpl.js` file, you can get all pages that have the type "article" (`type=article` ) using the following code:  `const posts = search.pages("type=article", "date=desc");`. The `search.pages("type=article", "date=desc")` function only returns those that have `type=article` .

The  `layouts/base.njk` layout file contains an HTML base and includes a header and footer for the website.

```nuckjunks
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <meta name="description" content="{{ description or site.description }}">
   </head>
  <body>

    {% include "layouts/header.njk" %}

    <main class="{{ bodyClass }}">
      {{ content | safe }}
    </main>

    {% include "layouts/footer.njk" %}

  </body>
</html>
```

Inside the `{{ content | safe }}`, Lume renders other HTML, like cards, articles, home templates, Tag and category pages, and so on.

```javascript
// rest code ...
  for (const page of paginate(posts, options)) {
  }
// rest code ...
```

I used the for loop on the `index.tmp.js` file that helps get all the posts and send them to the `layouts/home.njk` file and the `layouts/home.njk` file. You get all posts from the result, and then pass them to the `card.njk` template.

```nunjucks
---
layout: layouts/base.njk
---

{% for post in results %}
    {% include "templates/card.njk" %}
{% else %}
    <h2> Posts is empty </h2>
{% endfor %}

{% include "templates/pagnation.njk" %}
```

‌The `templates/card.njk`  file runs for all blogs and generates HTML for each blog. Your card looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/11/card.njk-1.png)
_card.njk_

In `card.js` template, you can access it using `{{}}` curly brackets. Get the title using `{{post.data.title}}` and `{{post.data.description}}`.

In my demo blog, I'm getting only the first category to show inside the card. So I use a defined filter  `_config.ts` and use it with `|` symbols. Inside `card.njk` we get a zero index or first value in from categories with the following code: `{{ post.data.category | category }}`.

To get the author on `card.njk` I define the [relationship](https://lume.land/plugins/relations/) between the article and the author type, which you can learn about from the docs.

```nuckjunks
<div class="container px-6 py-10 mx-auto">

    <div class="mt-8 lg:-mx-6 lg:flex lg:items-center">

        <img class="object-cover border-none w-full lg:mx-6 lg:w-1/2 rounded-xl h-72 lg:h-96" src="{{ post.data.image }}" alt="{{ post.data.title }}">

        <div class="mt-6 lg:w-1/2 lg:mt-0 lg:mx-6 ">

            <a class="text-sm text-blue-500 uppercase" href="/category/{{ post.data.category | category }}" >
                {{ post.data.category | category }}
            </a>

            <a href="{{ post.data.url }}" class="block mt-4 text-2xl font-semibold text-gray-800 hover:text-gray-500 dark:text-white md:text-3xl">{{ post.data.title }}</a>

            <p class="mt-3 text-sm text-gray-500 dark:text-gray-300 md:text-sm">
                {{ post.data.description }}
            </p>

            <a href="{{  post.data.url }}" class="inline-block p-2 bg-blue-700 mt-4 text-white hover:bg-blue-500">Read more</a>


            <div class="flex items-center mt-6">

                {% if post.data.author.length <= 2 %}

                    {% for author in post.data.author %}

                        <img class="border-none object-cover object-center w-10 h-10 rounded-full" src="{{ author.image}}" alt="{{ author.author_name}}">

                        <div class="mx-4">
                            <a href="{{author.url}}" class="text-sm text-gray-700 dark:text-gray-200">
                                {{ author.author_name}}</a>
                            <p class="text-sm text-gray-500 dark:text-gray-400">
                                {{author.job}}
                            </p>
                        </div>
                    {% endfor %}
                {% else %}

                    <img class="border-none object-cover object-center w-10 h-10 rounded-full" src="{{ post.data.author.image}}" alt="{{ post.data.author.name}}">

                    <div class="mx-4">
                        <a href="{{ post.data.author.url}}" class="text-sm text-gray-700 dark:text-gray-200">
                            {{ post.data.author.author_name}}</a>
                        <p class="text-sm text-gray-500 dark:text-gray-400">
                            {{post.data.author.job}}
                        </p>
                    </div>
                {% endif %}

            </div>
        </div>
    </div>
</div>
```

The `{{ title }}` and `{{description}}` both show the markdown file title and description. To show the category, I used a filter to show a single category on the article page and define the filter on `_config.ts` file. I also show single and multiple authors with For loop. Every card has its own `post.data.url` property, after the user clicks on the read more button user ago respected the article read page. To show the image, I used `{{ post.data.image }}` property. I also show single and multiple authors with For loop on `card.njk` file.

## How to Build an Articles Page

I know the page containing the article content is one of the most important for a blog. It's where readers should spend most of their time rather than the website's home page.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/random-blog-title-lume-1.png)

```markdown
---
category:
  - Blog
date: 2022-03-20T13:09:24Z
description: Dolor excepteur ad ad fugiat Lorem consectetur velit excepteur duis qui.
image: /images/dice.jpg
tags:
  - npm
  - npm cli
  - npm install command
title: Random blog Title for markdown.
draft: false
author_id: 1
type: article
layout: templates/article.njk
---

Laboris consequat elit ad excepteur. Ipsum duis amet dolore voluptate dolore consequat ullamco incididunt ullamco. Dolore laborum cupidatat dolor ipsum reprehenderit excepteur cupidatat dolore.

## First
Cupidatat non amet irure esse quis aute qui enim. Est qui ullamco proident consequat aute reprehenderit eiusmod nisi. Laboris ullamco fugiat sint occaecat.

## Second 
Irure fugiat officia non esse esse irure eu sint commodo quis amet. Dolor culpa non amet elit adipisicing exercitation ex anim velit ipsum.

## conclusion
Culpa irure eiusmod labore ut proident sit enim laborum nulla voluptate eu. Id tempor velit cillum pariatur est laboris ipsum ad. Sint nostrud nostrud laboris Lorem consequat tempor voluptate dolore velit. Commodo elit nulla commodo pariatur. Deserunt ipsum fugiat id ipsum pariatur cupidatat magna ex. Fugiat aliquip nisi laboris aliquip velit velit id quis eu reprehenderit excepteur fugiat.

```

I created an article in the posts folder under `type=article` . The `author_id` defines the relation between the author and the article.

I used `templates/article.njk` as the layout for my articles page. You can design yours as per your requirements. You can design the article title, description, author card, and tags as well. 

```nuckjunks
---
layout: layouts/base.njk
---
<article class="container mx-auto p-2">
  <div class="flex flex-col">

    <h1 class="text-2xl text-black mt-3">{{ title }}</h1>
    <p class="text-xl mt-1 text-gray-600">{{ description }}</p>

    {% if author %}
      <div class="flex flex-row mt-4">
        
        
        {% if author.length <= 2 %}

          {% for author in author %}

            <img class="border-none object-cover object-center w-10 h-10 rounded-full" src="{{ author.image}}" alt="{{ author.author_name}}">

            <div class="mx-4">
              <a href="{{author.url}}" class="text-sm text-gray-700 dark:text-gray-200">
                {{ author.author_name}}</a>
              <p class="text-sm text-gray-500 dark:text-gray-400">
                {{author.job}}
              </p>
            </div>
          {% endfor %}

        {% else %}
        
          <img class="border-none object-cover object-center w-10 h-10 rounded-full" src="{{ author.image}}" alt="{{ author.name}}">

          <div class="mx-4">
            <a href="{{ author.url}}" class="text-sm text-gray-700 dark:text-gray-200">
              {{ author.author_name}}</a>
            <p class="text-sm text-gray-500 dark:text-gray-400">
              {{ author.job}}
            </p>
          </div>
        {% endif %}

      </div>

    {% endif %}

      <nav class="flex flex-row my-5">
        {% for tag in tags %}
          <a href="/tag/{{ tag.trim().toLowerCase().split(' ').join("-") }}/" class=" bg-blue-500 text-black p-2  mx-1">{{ tag }}</a>
        {% endfor %}
      </nav>

    <time class="mt-2" datetime="{{ date | date('DATETIME') }}">
      {{ date | date('HUMAN_DATE') }}
    </time>


  </div>

  <div class="mt-4">
    {{ content | safe }}
  </div>
</article>

{%- set previousPost = search.previousPage(url, "type=article") %}

{% if previousPost %}
  <ul class="flex flex-row w-full mt-10 justify-between p-4">
    {%- if previousPost %}
      <li class="w-6/12 text-left">
      ← Previous: <a href="{{ previousPost.data.url }}" rel="prev">{{ previousPost.data.title }}</a>
      </li>
    {% endif %}

    {%- set nextPost = search.nextPage(url, "type=article") %}
    {%- if nextPost %}
      <li class="w-6/12 text-right">
        <strong>Next: <a href="{{ nextPost.data.url }}" rel="next">{{ nextPost.data.title }}</a> →</strong>
      </li>
    {% endif %}
  </ul>
{% endif %}

<div class="container p-2 mx-auto mt-6"> 

{# ==== #}
{#  Addding the utteranc Commenting script #}
{# ==== #}

<h1 class="text-center text-2xl my-3"> Comment </h1> 

<script src="https://utteranc.es/client.js"
        repo="officialrajdeepsingh/Minimalist-blog"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
</div>
```

The `layouts/base.njk` file is the base file for our blog (which I've already explained). The `{{ title }}` and `{{description}}` both show the markdown file title and description. 

To show tags on the article page, I used a for loop. I also showed single and multiple authors with the for loop. 

To convert the date into a human-readable format, I used Lume date plugin and wrapped it with a date filter that looks like this: `{{ date | date('HUMAN_DATE') }}`. To show all markdown paragraphs, I used `{{ content | safe }}` . 

For pagination, I used the Lume pagination plugin, and with the `search.previousPage(url, "type=article")` function, I showed the next and previous posts on the article page. For comments, I used [utteranc.es](#heading-how-to-enable-comments).

## How to Generate a Category Page

In Lume, you create a dynamic category based on article type. Lume also provides inbuilt functionality called a JavaScript template engine that helps you create a  dynamic page. It is similar to creating pagination functionality.

In Lume, there's a special file called `.tmpl.js` that helps you create a dynamic category.

```nunjucks
export const layout = "layouts/category.njk";

export default function* (props) {


  const { search }= props

  for (const category of search.values("category") ) {

    yield {
      url: `/category/${category}/`,
      title: `Categoryed ${category}`,
      type:"category",
      category,
    };
    
  }

}

```

In lume `search.values()` have a function that helps you find a category using markdown meta tags and sends data into the `layout/category.njk` file. It will generate all categories with the following URLs like  `/category/android/` , `/category/android-phone/` , `/category/human/` and so on.

## How to Generate a Tag Page

Generating a dynamic tags page is similar to a category. Lume provides a special `search.tags()` function to generate tags:

```nunjucks
export const layout = "layouts/tag.njk";

export default function* ({ search }) {

  for (const tag of search.tags()) {
    yield {
      url: `/tag/${tag}/`,
      title: `Tagged ${tag}`,
      type: "tag",
      tag,
    };
  }
}
```

The following code generates all tags with the following URLs like `/tag/android/`, `/tag/android-phone/`, `/tag/human/` and so on.

## How to Enable Search Functionality

Lume has many in-built plugins which provide an excellent development experience. You can solve lots of problems with Lume plugins, and they allow you to add and remove features easily.

Lume provides inbuilt search functionality for the site. You enable it with the lume page find plugin.

![Add a search bar in lume](https://www.freecodecamp.org/news/content/images/2022/11/lume-serachbar-1.png)
_Add a search bar in lume_

### How to Install Page Find

The Lume page finds plugin provides you with a search bar. Simply copy the following code and paste it into the `_config.ts` file and restart your server.

```javascript
import pagefind from "lume/plugins/pagefind.ts";
```

#### How to configure the page find plugin

You configure the plugin in the `_config.ts` fil. You can also change the default config.

```
// rest of code ...
import lume from "lume/mod.ts";
import pagefind from "lume/plugins/pagefind.ts";

const site = lume();

// config the pagefind plugin with default config
site.use(pagefind());

 // or 

// change the default config in pagefind plugin
site.use(pagefind({
  ui: {
    containerId: "search",
    showImages: false,
    showEmptyFilters: true,
    resetStyles: true,
  },
}));

export default site;
```

## Lume SEO

Lume has a plugin to help with SEO called metas. With the plugin, you can easily add various SEO-friendly configurations.

### How to install metas

You install all plugins within the `config.ts` file. Copy the following code and paste it into the `config.ts` file, then restart the server.

```javascript
import metas from "lume/plugins/metas.ts";
```

#### How to configure metas

You can configure metas in various ways in the  `_config.ts` file. See the comments below:

```
import lume from "lume/mod.ts";

// install metas plugin for SEO
import metas from "lume/plugins/metas.ts";

const site = lume();

// config the metas plugin with default config
site.use(metas());

or

// add custom config 
site.use(metas({
  defaultPageData: {
    title: "title", // Use the `title` value as fallback.
  },
}));


export default site;
```

### How to Use the Metas SEO Plugin in Lume

To use the SEO metas plugin, you'll need to create a `_data.yml` file in the root of the project folder and paste the following code into it:

```
metas:
  site: Minimalist blog
  twitter: "@Official_R_deep"
  icon: /images/icon.png
  lang: en
  generator: true

mergedKeys:
  metas: object
```

The following code helps you create all the various SEO tags for your website, and you can easily extend it with the [metas plugin](https://lume.land/plugins/metas/) in Lume.

### Lume Sitemap

Lume has a plugin called [sitemap](https://lume.land/plugins/sitemap/). This plugin helps you create sitemaps for your blog. With Lume 13 you do not need to create a sitemap manually. 

#### How to install the sitemap plugin

You install all plugins within the `config.ts` file. Copy the following code and paste it into the `config.ts` file, then restart the server.

```javascript
import sitemap from "lume/plugins/sitemap.ts";

```

#### How to configure the sitemap plugin

You can configure the sitemap plugin in various ways in the `_config.ts` file. See the comments below:

```javascript
import lume from "lume/mod.ts";
import sitemap from "lume/plugins/sitemap.ts";

const site = lume();

site.use(sitemap());

// or

// add custom config 
site.use(sitemap({
  filename: "my-sitemap.xml", // to change the sitemap filename
  query: "indexable=true", // Select only pages with the indexable attribute as true
  sort: "date=desc", // To sort by data in ascendent order
}));

export default site;
```

### How to use the sitemap plugin in Lume

You do not need any special file to use the site map plugin. Simply add the plugin after calling the plugin in `config.ts` and it'll start working on your site. This creates the `sitemap.xml` file and you can change the file name with a custom configuration in `_config.ts` file.

### How to access the sitemap on the website

You can access the sitemap with the filename, for example by default in the localhost `[http://localhost:3000/sitemap.xml](http://localhost:3000/sitemap.xml)` and production `[http://my-domain-name/sitemap.xml](http://localhost:3000/sitemap.xml)` . 

## Lume Plugins

Lume comes with [inbuilt plugins](https://lume.land/plugins/?status=all), but you can easily add or remove features according to your requirements. You do not need all the stuff on your site – you can configure everything as you wish. 

You can add more template engines, minify HTML, CSS, and JavaScript with plugins, enable code highlighting, date manipulation, image manipulation, SVG support, and more. 

You can also easily create your own plugins with lume. [Lume also provides excellent documentation](https://lume.land/docs/advanced/plugins/) where you can learn more.

## How to Enable Comments

To add comments on your Lume site, I think [utteranc.es](https://utteranc.es/) is the best choice for all static site generators. utteranc.es is an open-source commenting system based on GitHub. It looks like this:

![Enable comment in lume](https://www.freecodecamp.org/news/content/images/2022/11/enable-coments-on-minimalist-blog.deno-1.png)
_Enable comment_

If you want to enable comments on the site, the first step is to install an [utterances application](https://github.com/apps/utterances) on GitHub. Then, copy and paste the following code into the article read file or where you show comments on the site. 

```javascript
<script src="https://utteranc.es/client.js"
        repo="officialrajdeepsingh/Minimalist-blog"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
```

Next, you'll need to change the utterance comment script. The first change in the repo `repo="your-github-repo"` name is compulsory. The others are not. You can adjust according to your requirements – for example, changing the theme, issue term, and so on. 

To read more about utterance, here's a [great article written by Josh Collinsworth](https://joshcollinsworth.com/blog/add-blog-comments-static-site).

The best approach is to add utterance comments in lume and then read the [GitHub discussion](https://github.com/lumeland/lume/discussions/312).

## How to Use Netlify CMS with Lume

Netlify CMS is an open-source content management system. You can easily integrate Netlify with Lume using the [netllify_cms](https://lume.land/plugins/netlify_cms/) plugin. It is provided by Lume, and you just need to install it and copy/paste the code.

### How to Install the Netlify Plugin

Import the Netlify plugin in your `_config.ts` file to use it like this:

```javascript
import lume from "lume/mod.ts";
import netlifyCMS from "lume/plugins/netlify_cms.ts";

const site = lume();

site.use(netlifyCMS());

export default site;
```

To configure it, you'll need to create a `/_data/netlify_cms.yml` file in the root level and then paste the following code after restarting your server:

```yml
backend:
  name: git-gateway
  branch: master

media_folder: statics

collections:
  - label: Posts
    name: posts
    description: List of posts
    folder: posts
    extension: md
    create: true
    fields:
      - label: Title
        name: title
        widget: string
      - label: Content
        name: body
        widget: markdown
```

Netlify will ask you for permissions for the CMS proxy. Type `npx netlify-cms-proxy-server`  in a terminal, press enter or `type y`, and your Netlify CMS will start running locally on [http://localhost:3000/admin](http://localhost:3000/admin) URL. Now your Lume blog is ready for deployment on Netlify. 

## How to Deploy Your Blog with Deno Deploy

You can deploy Lume on various platforms such as Deno Deploy, GitHub Pages, Gitlab Pages, Netlify, Vercel, Fleek, AWS Amplify, and Cloudflare Pages. Lume also provides [excellent documentation on deployment](https://lume.land/docs/advanced/deployment/). 

In this article, I'm deploying my Lume blog with Deno Deploy (and we'll also see how to do it with GitHub pages). Deno Deploy is an official platform built by the Deno team to deploy Deno-based applications.

Before deploying your Lume blog on Deno Deploy, make sure you create a `server.ts` file in the root level.

```javascript

import Server from "lume/core/server.ts";

const server = new Server({
  port: 8000,
  root: `${Deno.cwd()}/_site`,
});

server.start();

console.log("Listening on http://localhost:8000");

```

#### Deployment Steps:

1. Create an account on Deno Deploy.
2. Push your local code to GitHub and then select the `server.ts` file. Deno Deploy automatically creates a site based on the `server.ts` the file.
3. Make sure to first create a custom `server.ts` file. Then move to the next step.
4. The easiest way to deploy your site is with GitHub Actions. Create a new `.github/workflows/deno.yml` file in your project root level and paste the following code into it:

```yml
name: Deploy
on: [push]

jobs:
  deploy:
    name: Deploy
    runs-on: ubuntu-latest
    permissions:
      id-token: write # Needed for auth with Deno Deploy
      contents: read # Needed to clone the repository

    steps:
      - name: Clone repository
        uses: actions/checkout@v3

      # TODO: add a build step here

      - name: Upload to Deno Deploy
        uses: denoland/deployctl@v1
        with:
          project: "minimalist-blog"
          entrypoint: "./serve.ts" 

```

## How to Deploy Your Blog with Github Pages

GitHub Pages are free static sites you can use to host pages. You can also deploy your Lume blog it. The process of deployment is pretty easy. 

To deploy Lume on GitHub pages you need to have GitHub Actions set up. 

#### Deployment Steps

1. It's best if you have a GitHub repository so you can convert your local website to GitHub Pages.
2. Create a new repo and push all your local code into it.
3. Create a new `.github/workflows/deno.yml` in your project root level, then paste the following code into it and push it into the GitHub repo. The GitHub action runs based on the `github.yml` action and it generates a GitHub page. 

```yml
name: Publish on GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Clone repository
        uses: actions/checkout@v3

      - name: Setup Deno environment
        uses: denoland/setup-deno@v1
        with:
          deno-version: v1.x

      - name: Build site
        run: deno task build

      - name: Deploy
        uses: crazy-max/ghaction-github-pages@v3
        with:
          build_dir: _site
        env:
          GITHUB_TOKEN: ${{ secrets.MY_GITHUB_TOKEN_PAGE }}
```

You need a GitHub token to deploy your Lume website to GitHub pages. This is a required part of the setup. I found [a great article written by Davide](https://dev.to/github/the-githubtoken-in-github-actions-how-it-works-change-permissions-customizations-3cgp) that can help you learn more about GitHub Actions and how to create one.

GitHub Actions takes two or three minutes to finish hosting your website on GitHub Pages. 

Check out the [GitHub repository](https://github.com/officialrajdeepsingh/minimalist-blog-github-page) to learn how to configure the GitHub workflow for GitHub pages. You can also see a live demo [website on the GitHub page](https://officialrajdeepsingh.github.io/minimalist-blog-github-page/).

A quick note: if you deploy your Lume site on GitHub pages and your image does not show on the website, there are two possible reasons for this:

1. If all image names aren't in lowercase, you might get an error. To resolve the error, convert your image names into lowercase with this command: `your.github.com/your-reponame/images/my-image.png`
2. If you're using the `base_path` and `relative_urls` Lume plugins in your project and `relative_urls` is redundant, and then you'll need to remove the `relative_urls` plugin in your project. Your image should now work fine.

## Conclusion

Lume is an easy-to-learn and feature-rich static site generator. You can do anything you imagine with it. Lume gives you a lot of freedom with the code.

The Lume community is not as big as those of Hugo, 11ty, Jekyll, and other tools. But, the Lume maintainers actively reply to everybody who comments in the GitHub discussion. Without a strong community, this tool should be able to create a strong impact.

One challenge with Lume is that it's tough to get started for beginners and is more suited to intermediate and advanced developers. If you're jumping right into using Lume as a beginner, you might struggle with a lack of background knowledge about how static site generators work. 

Because of this, it's helpful to have a **little bit of knowledge** about Nuckjunks, JSX, and other template engines that work based on markdown. Once you gain this experience, then you'll easily be able to use Lume to design your markdown-based blog. 

I recommend using the [lume MDX plugin](https://lume.land/plugins/mdx/) for markdown. You can use JSX-based components inside the markdown file, and you can create beautiful code blocks, tip blocks, and so on.

I highly encourage all developers to try Lume out. If you have problems with Lume, you can reach out to its creator on the [GitHub discussion](https://github.com/lumeland/lume/discussions) and the [Discord server](https://discord.com/invite/YbTmpACHWB). 

If your course is about Computer science, Bioinformatics, and Biotechnology. You can join my free [newsletter](https://www.getrevue.co/profile/officialrajdeepsingh). 

