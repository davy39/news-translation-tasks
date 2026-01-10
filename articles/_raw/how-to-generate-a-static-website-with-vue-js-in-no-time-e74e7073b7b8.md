---
title: How to generate a static website with Vue.js in no time
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-18T17:33:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-generate-a-static-website-with-vue-js-in-no-time-e74e7073b7b8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LLjrzVGPTIotAeil7DiXyA@2x.png
tags:
- name: JavaScript
  slug: javascript
- name: Nuxt.js
  slug: nuxtjs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
seo_title: null
seo_desc: 'By Ondřej Polesný

  You have decided to build a static site, but where do you start? How do you select
  the right tool for the job without previous experience? How can you ensure that
  you succeed the first time, while avoiding tools that won’t help you ...'
---

By Ondřej Polesný

You have decided to build a static site, but where do you start? How do you select the right tool for the job without previous experience? How can you ensure that you succeed the first time, while avoiding tools that won’t help you in the end?

In this article, you will learn how to adjust a Vue.js website to be automatically generated as a static site.

### Introduction

I summarized the key differences between an API based website and static sites in my [previous article](http://bit.ly/2QVSm9a). As a quick reminder, static sites are:

* Blazing fast
* Secure (as they are just a set of static pages)
* Regenerated every time editors update the content
* Compatible with additional dynamic functionality

#### What is a Static Site Generator?

A static site generator is a tool that generates a static website from a website’s implementation and content.

Content can come from a headless content management system, through a REST API. The website implementation uses one of the JavaScript frameworks like Vue.js or React. The output of a static site generator is a set of static files that form the website.

![Image](https://cdn-media-1.freecodecamp.org/images/0VwMHb8tn3Cn8aNcazzqntftAKyRki4svRCc)

#### Static Site Implementation

I chose Vue.js as the JavaScript framework to use. Therefore I will be working with [Nuxt.js](http://bit.ly/2Aiaggm), which is a static site generator for Vue.js.

If you are using a different framework, look for a static site generator built on top of that framework (for example [Gatsby](http://bit.ly/2ypBwZ7) for [React.js](http://bit.ly/2PGeCTL)).

Essentially, Nuxt is a combination of multiple tools that together enable you to create static sites. The tools include:

* Vue2 — Core Vue.js library.
* Vue Router — Handles URL routing for pages within the website.
* Vuex — Memory store for data that are shared by components.
* Vue Server Renderer — Enables server side rendering of pages before the actual static files generation
* Vue-Meta — Manages page metadata info

Nuxt also defines how the website needs to be built in order to generate static files.

#### Installation

In order to start building websites with Nuxt, you need to install it. See detailed installation instructions on the [Nuxt.js webpage](http://bit.ly/2R0LTJH). In a nutshell, you need `npx` (shipped with NPM by default) installed and run:

```
npx create-nuxt-app <website-name>
```

You can just use default selections, unless you have preferences otherwise.

#### Components

In [one of my previous articles](http://bit.ly/2zLRE8a) I explained how to create a template layout and components. All of them were defined within single file `components.js`. That needs to be changed with Nuxt. All components need to be extracted from `components.js` file into separate files under folder `components`. Take a look at my `blog-list` component and its previous implementation:

```
Vue.component('blog-list', { props: ['limit'], data: function(){  return {   articles: null  } },
```

```
 created: function(){  var query = deliveryClient   .items()   .type('blog_post')   .elementsParameter(['link', 'title', 'image_url', 'image', 'teaser'])   .orderParameter('elements.published', SortOrder.desc);   if (this.limit){   query = query.limitParameter(this.limit);  }  query   .getPromise()   .then(response =>    this.$data.articles = response.items.map(item => ({     url: item.link.value,     header: item.title.value,     image: item.image_url.value != '' ? item.image_url.value : item.image.assets[0].url,     teaser: item.teaser.value    }))   ); },
```

```
 template: `  <section class="features">   <article v-for="article in articles">    ...   </article>  </section> ` });
```

To separate it, you also need to change the component’s syntax to match the following template:

```
<template> HTML of the component</template><script> export default {  Vue.js code }</script>
```

Therefore my adjusted `Blog-list` component looks like this:

```
<template> <section class="features">  <article v-for="article in blogPosts">   ...  </article> </section></template><script> export default {  props: ['limit'],  computed: {   blogPosts: function(){    return this.$store.state.blogPosts && this.limit && this.$store.state.blogPosts.length > this.limit ? this.$store.state.blogPosts.slice(0, this.limit) : this.$store.state.blogPosts;   }  } }</script>
```

You see the template stayed the same. What changed is the implementation that is now within `export default` section. Also, there used to be a function gathering data from headless CMS Kentico Cloud.

That content is now stored within Vuex store. I will explain this part later. Convert all of your components this way, to contain template within `<templa`te> tags and implementation w`ithin &l`t;script> tags. You should end up with a similar file structure as I have:

![Image](https://cdn-media-1.freecodecamp.org/images/cZ4HD2jJIJ0bTeTi5ZGwFYRTMYr2p6L0HQzL)

Note that I have two new components here — Menu and Header. As my aim was to also improve performance, I decided to remove jQuery from my website. jQuery is quite a large and heavy library that was used only for small UI effects. I was able to recreate them using just Vue.js. Therefore, I converted the static HTML representing header to component. I also added the UI related functionality into `mounted` function of this component.

```
mounted: function(){ window.addEventListener(‘scroll’, this.scroll); …},methods: { scroll: function(){  … }}
```

### Handling Vue.js Events with Nuxt

I used to leverage Vue events in my website. The main reason was reCaptcha control used for form validation. When it was initialized, it would broadcast the event so that form component can unlock the submit button of the contact form.

With Nuxt, I no longer use `app.js` or `components.js` files. Therefore I created a new `recaptcha.js` file that contains a simple function emitting the event when reCaptcha gets ready. Note that instead of creating new Vue.js instance just for events (`let bus = new Vue();` in my old code), it is possible to simply use `this.$nuxt` the same way.

```
var recaptchaLoaded = function(){ this.$nuxt.$emit('recaptchaLoaded');}
```

### Layout and Pages

The main frame of the page was `index.html`, and each page defined its own layout in constants that were handed over to Vue router.

With Nuxt, the main frame including `<ht`ml> `tag`, meta tags and other essentials of any HTML page are handled by Nuxt. The actual website implementation is handling only content w`ithin` <body> tags. Move the layout that is common for all your `pages into layouts`/default.vue and respect the same template as with components. My layout looks like this:

```
<template> <div>  <Menu></Menu>  <div id="page-wrapper">   <Header></Header>   <nuxt/>   <section id="footer">    <div class="inner">     …     <ContactForm></ContactForm>     …    </div>   </section>  </div> </div></template><script> import ContactForm from ‘~/components/Contact-form.vue’ import Menu from ‘~/components/Menu.vue’ import Header from ‘~/components/Header.vue’  export default {  components: {   ContactForm,   Menu,   Header  } } </script>
```

The layout is basically the HTML markup of my old `index.html`. However, note the `<scri`pt> section. All of the components I want to use within this layout template need to be imported from their location and specified in exported object.

![Image](https://cdn-media-1.freecodecamp.org/images/FwQ-P1izN6Qai74S7TrMPcJGJ2SOL-7K93X-)

Page components were previously defined in `app.js` as constants. Take a look at my old Home page for example:

```
const Home = { template: `  <div>   <banner></banner>   <section id="wrapper">    <about-overview></about-overview>    ...    <blog-list limit="4"></blog-list>    <ul class="actions">     <li><a href="/blog" class="button">See all</a></li>    </ul>    ...   </section>  </div> `}
```

All these pages need to be defined in separate files within `pages` folder. Main page is always called `index.vue`. This is how my new `pages/index.vue` (my Homepage) looks like:

```
<template> <div>  <Banner></Banner>  <section id="wrapper">   <AboutOverview></AboutOverview>   ...   <BlogList limit="4"></BlogList>   <ul class="actions">    <li><a href="/blog" class="button">See all</a></li>   </ul>   ...  </section> </div></template><script> import Banner from ‘~/components/Banner.vue’ import AboutOverview from ‘~/components/About-overview.vue’ import BlogList from ‘~/components/Blog-list.vue’  export default {  components: {   Banner,   AboutOverview,   BlogList  }, }</script>
```

### Where to Store Assets

On every website there are assets like CSS stylesheets, images, logos, and JavaScripts. With Nuxt, all these static files need to be stored under folder static. So the folder structure currently looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/pez1-XpfChKIX8aOVP0vP-2BH2cz28MCsFlM)

When you reference any resources from CSS stylesheets like fonts or images, you need to use static folder as a root:

```
background-image: url("~/assets/images/bg.jpg");
```

### Getting Content

With all the components and pages in place, we finally get to it: getting content into components.

Getting content using Nuxt is a bit different than it used to be. The important aspect of this process when using a static site generator is that the content needs to be gathered before all the pages are generated. Otherwise you will end up with a static website, but requests for content would still be dynamic, hitting the headless CMS from each visitor’s browser and you would lose the main benefit.

Nuxt contains two special methods that handle asynchronous data fetching at the right time, that is before the pages are generated. These methods are `asyncData` and `fetch`. They are available only to page components (that is files within `pages` folder) and their purpose is the same, but `asyncData` will automatically store received data within the component dataset.

This can be beneficial if you have many components on a single page using the same set of data. In my case, I even have multiple pages with many components that need to share the same data. Therefore I would either need to request the same data on each page or use a shared space that all pages and components could access.

I chose the latter. Nuxt makes it very easy for us. It automatically includes Vuex store that enables our components and pages access any data that are within the store. To start using the store all you need to do is create an `index.js` file within the `store` folder.

```
import Vuex from 'vuex'
```

```
const createStore = () => { return new Vuex.Store({  state: () => ({}),  mutations: {},  actions: {}, })}export default createStore
```

You see the instance has a few properties:

* **State**  
State is similar to data in components. It contains definition of data fields that are used to store data.
* **Mutations**  
Mutation are special functions that are permitted to change data in State (mutate the state).
* **Actions**  
Actions are simple methods that enable you to, for example, implement content gathering logic.

Let’s get back to the `Blog-list` component. This component needs an array of blog posts in order to render its markup. Therefore blog posts need to be stored within Vuex store:

```
…const createStore = () => { return new Vuex.Store({  state: () => ({   blogPosts: null  }),  mutations: {   setBlogPosts(state, blogPosts){    state.blogPosts = blogPosts;   }  },  actions: {   getBlogPosts (context) {    logic to get content from Kentico Cloud   }  }, })}
```

After adjusting Vuex store this way, the `Blog-list` component can use its data:

```
<article v-for="article in $store.state.blogPosts"> …</article>
```

I already shared the whole implementation of this component above. If you noticed, it uses `computed` function as a middle layer between component markup and Vuex store. That middle layer ensures the component displays only a specific amount of articles as configured in the `limit` field.

### Querying the Headless CMS

Maybe you remember the `deliveryClient` was used to get data from [Kentico Cloud](http://bit.ly/2QzUALM) into the components.

_Disclaimer: I work for Kentico, a CMS vendor that provides both traditional (coupled) CMS and a new cloud-first headless CMS — Kentico Cloud._

The very same logic can be used here in the Vuex store actions with a little tweak. Kentico Cloud has a [module for Nuxt.js](http://bit.ly/2Qiovur), install it using following command:

```
npm i kenticocloud-nuxt-module — savenpm i rxjs — save
```

With this module you can keep using `deliveryClient` like before, just with a `$` prefix. So in my case the logic to get blog posts looks like this:

```
…getBlogPosts (context) { return this.$deliveryClient  .items()  ...  .orderParameter('elements.published', SortOrder.desc)  .getPromise()  .then(response => {   context.commit('setBlogPosts', response.items.map(item => ({    url: item.link.value,    header: item.title.value,    image: item.image_url.value != '' ? item.image_url.value : item.image.assets[0].url,    teaser: item.teaser.value   })))  }); },…
```

If you want to use ordering using the `orderParameter`, you may need to include another import in the `store/index.js` file:

```
import { SortOrder } from 'kentico-cloud-delivery'
```

Now when the content gathering logic is implemented, it’s time to use the special asynchronous function fetch that I mentioned before. See my implementation in the `index.vue` page:

```
async fetch ({store, params}) { await store.dispatch('getBlogPosts')}
```

The call to `store.dispatch` automatically invokes `getBlogPosts` action. Within the `getBlogPosts` implementation note the call for `context.commit`. `context` refers to Vuex store and `commit` will hand over blog posts data to `setBlogPosts` mutation. Updating the data set with blog posts changes the state of the store (mutates it). And we are almost finished!

#### Other content storage options

I used [Kentico Cloud](http://bit.ly/2QzUALM) headless CMS and its API here, as I am using it throughout all articles in this series. If you want to also check out other options, you can find an independent list of headless CMSs and their features at [headlesscms.org](http://bit.ly/2S8gxSi).

If you don’t want to use a headless CMS and its API, you may decide to store your content in some other way — usually as a set of markdown files directly stored within your project or Git repository. You can find a nice example of this approach in [nuxt-markdown-example GitHub repository](http://bit.ly/2R5PQAo).

### Nuxt Configuration

The whole application needs to be properly configured using `Nuxt.config.js` file. This file contains information about used modules, their configuration and site essentials like title or SEO tags. The configuration of my website looks like this:

```
export default { head: {  title: 'Ondrej Polesny',  meta: [   { charset: 'utf-8' },   ...   { hid: 'description', name: 'description', content: 'Ondrej Polesny — Developer Evangelist + dog lover + freelance bus driver' }  ],  script: [   { src: 'https://www.google.com/recaptcha/api.js?onload=recaptchaLoaded', type: "text/javascript" },   { src: 'assets/js/recaptcha.js', type: "text/javascript" }  ], }, modules: [  'kenticocloud-nuxt-module' ], kenticocloud: {  projectId: '*KenticoCloud projectId*',  enableAdvancedLogging: false,  previewApiKey: '' }, css: [  {src: 'static/assets/css/main.css'}, ], build: {  extractCSS: {   allChunks: true  } }}
```

The head section describes website essentials like `title` and `meta` tags you want to include in header.

Note the `modules` and `kenticocloud` configuration. The first one lists all modules your application depends on and the second one is specific module configuration. This is the place where you need to put your project API key.

To see all the options for meta tags, please refer to [https://github.com/declandewet/vue-meta](http://  https://github.com/declandewet/vue-meta)

### Running and Generating

Static sites need to be generated before anyone can access them or upload them to an FTP server. However, it would be very time consuming to regenerate the site every single time a change has been made during the development phase. Therefore, you can run the application locally using:

```
npm run dev
```

This will create a development server for you and enable you to access your website on http://localhost:8000 (or similar). While you keep your console running this command, every change you make in your scripts will have immediate effect on the website.

To generate a true static site, execute following command:

```
npx nuxt generate
```

The output, that is your static site, will be in `dist` folder. Feel free to open any page in your favorite text editor and see if the source code contains content from the headless CMS. If it does, it was successfully fetched.

### Conclusion

Having a generated static site will greatly improve the website’s performance. Compared to traditional sites, the webserver does not need to perform any CPU heavy operations. It only serves static files.

Compared to API based websites, the clients receive requested data instantly with the very first response. That’s what makes them all that fast — they do not need to wait for external content to be delivered via additional asynchronous requests. The content is already there in the first response from the server. That dramatically improves user experience.

Converting the site from Vue.js implementation to Nuxt definitions is very straightforward and does not require deep knowledge of all used components and packages.

Have you successfully created your first static site? Have you experienced any struggles? Please leave a comment.

In the next article I will focus on automated regeneration of static sites and where to host them, so stay tuned.

#### Other articles in the series:

1. [How to start creating an impressive website for the first time](http://bit.ly/2Duglu1)
2. [How to decide on the best technology for your website?](http://bit.ly/2N0kXY4)
3. [How to power up your website with Vue.js and minimal effort](http://bit.ly/2zLRE8a)
4. [How to Mix Headless CMS with a Vue.js Website and Pay Zero](http://bit.ly/2CyDnhX)
5. [How to Make Form Submissions Secure on an API Website](http://bit.ly/2P0gidP)
6. [Building a super-fast and secure website with a CMS is no big deal. Or is it?](http://bit.ly/2QVSm9a)
7. **How to generate a static website with Vue.js in no time**
8. [How to quickly set up a build process for a static site](http://bit.ly/2Dv2UGS)

