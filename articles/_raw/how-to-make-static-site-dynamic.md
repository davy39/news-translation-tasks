---
title: How to Make Your Static Site Dynamic
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-23T19:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-static-site-dynamic
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/article-cover.jpg
tags:
- name: Productivity
  slug: productivity
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ondrej Polesny

  A static site seems like a good fit for a small and steady project, right? Like
  one that does not require any advanced features or interaction with users. But how
  can you leverage the performance benefits and still have your static ...'
---

By Ondrej Polesny

A static site seems like a good fit for a small and steady project, right? Like one that does not require any advanced features or interaction with users. But how can you leverage the performance benefits and still have your static site be dynamic, personalized and interactive?

Whenever I mention a "static site" to devs that haven't yet worked with static site generators, they frown upon them. The buzz word is working against me and doesn't really describe what you are getting if you decide to use a static site generator (like Gatsby or Gridsome). 

So, I explain to them how it all works, including automatic rebuilds when content or implementation changes. They always have the same comment:

> "It's nice and all, but pre-generating the site won't work for dynamic scenarios like e-commerce or personalization. Thus it's good only for small projects."

And that just isn't true. I will show you why.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/site-timeline.png)

There are two ways of making a static site dynamic:

* during site pre-rendering
* through user interactions on the site

I should explain this using a real website. Lately, I've been facing the task of creating a wedding site. I know, there are thousands of simple templates for that. But being employed in IT, people implicitly expect the site to be state of the art. So I caved. I'll show 'em.

For the implementation part I decided to use Gridsome static site generator as I prefer Vue.js to React. I'll be using a [headless CMS](http://bit.ly/38aGvfn) to store the content and two serverless functions to handle the user interaction. 

_Prefer video? Watch the_ [_Twitch series on YouTube_](http://bit.ly/2TbMo7D)_. And make sure to_ [_follow me on Twitch_](https://twitch.tv/ondrabus) _to catch all upcoming streams._

## Dynamic content during site pre-rendering

I put together all the information that I know before I build the website. I know who I want to invite. I know when the event takes place and I know who I am marrying. Just like you know what products you want to sell or what services you want to offer on your site.

With that in mind, I created a bunch of content models for my site:

* Invitee
* Accommodation
* Section
* Timeline item

And this is how they look in the actual site design:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/wedding-site-1-.png)

Because I know all the invitees, I used the content from the headless CMS to (automatically) generate a separate page for each invitee (check out the Custom URL label on the picture). As a result, at the build time, the components know the context of the invitee. Imagine the personalization possibilities – I can even return a 404 for some of my least favorite relatives.

I actually used it to display personalized salutations and only relevant timeline items.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/salutation.png)

If you were building an e-commerce site, you could implement a product page that displays a list of similar products. You would also probably link to those product-relevant services your company offers. You know all the necessary details at build time.

### Content modeling is the key for pre-build sites

I identified three content models for my site, but typically it's much more than that. A good way of approaching content modeling is to take a look at the wireframes for your future site. It's not just about how to put the data into the CMS, you need to think about:

* **How is the content going to be displayed and consumed?**  
Take products and categories for example. In most cases, you will find them being in an N:N relationship, but I am aiming at the implementation side of things here. Think about how complicated the queries for data will be. Adjusting the content models to better represent the actual site structure may help a lot with implementation.  
In my example, the timeline items are linked from invitees (1:N) which allows for simple implementation while content management is still straightforward. Like reorganizing the order of the items.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/linked-items.png)

* **How is the content related to other content items?**  
What is the relationship between products, packs of products, categories, special offers or discounts? The answers to these questions will help you choose the right tool for connecting content items like Taxonomy or Linked items.
* **How is the content going to be created?**  
Will editors understand the structure of the content you have in place? Also, in most cases, they don't get access to whole projects, but only to parts that are relevant for them. Does your structure allow for a sufficient level of permissions granularity? Are your content models restrictive enough to avoid missing content issues on the live site?

There is much more to content modeling. If you're interested, take a look at [this great series on content modeling](https://medium.com/@meandmyrobot/content-modelling-in-kentico-kontent-part-1-f820ad45d98a) written by [Michael Kinkaid](https://twitter.com/meandmyrobot).

## Dynamic components

So with the right content models, we can generate the static site. Well, pre-generated is probably a better label for it. Its content is not old and static - every content change will effectively rebuild the site again.

But what if we need to interact with visitors? At times we need to get some input from them or show them different content based on their actions. In those cases, we can use dynamic components. They are pre-initialized with values during the site build, but they can keep interacting with backend systems based on visitors' actions.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/dynamic-form.png)

On my website, I have a form which invitees can use to confirm what type of accommodation they are interested in. Their selection needs to be stored back in the same Invitee content item I created originally in the headless CMS.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/implementation.png)

I could communicate with the CMS directly from the component on the site. However, we're talking client-side JavaScript here. Exposing the key would be a major security issue even though I don't expect any of my invitees to understand what a security key is or how it can be misused. So, the middle man between the static site and the CMS is a serverless function.

### Reactive Component on a Static Site

Let's start with the component. I used Vue.js and Gridsome as the SSG, but the dynamic component concept is the same regardless of the used framework. The headless CMS I've used here is [Kontent](http://bit.ly/38aGvfn). It has a generous free tier, but if you like open-source (to quote my operating-systems uni professor "I don't trust it unless I see its code") I heard [Strapi](http://bit.ly/2POJ9Rk) is a good choice.

#### Component Implementation

At build time, the component will receive initial data - the data we know at that specific point in time. If Michael selected one of the options last week and we are rebuilding the site today, we know his selection.

```xml
<RsvpAccommodation inviteeId="{GUID}" optionSelected="sleep_in_a_tent" howManyInvited="2" salutation="Michael" />
```

On the other hand, if he has yet to interact with the site, the selection would be empty.

```xml
<RsvpAccommodation inviteeId="{GUID}" optionSelected="" howManyInvited="2" salutation="Michael" />
```

The component looks like this:

```js
<template>
    ...
    <input type="radio" name="option" value="not_interested" id="none" v-model="option" />
    <label for="none">Děkuji, nepotřebuji</label>
    <input type="radio" name="option" value="interested_in_booking_a_room" id="hotel" v-model="option" />
    <label for="hotel">Mám zájem o ubytování v okolí</label>
    <input type="radio" name="option" value="sleep_in_a_tent" id="tent" v-model="option" /><label for="tent">Mám zájem o přespání ve vlastním stanu</label>
    ...
</template>
<script>
export default {
    props: {
        salutation: String,
        inviteeId: String,
        howManyInvited: Number,
	salutation: String,
        optionSelected: String
    },
    data: function(){
        option: this.optionSelected
    },
    ...
</script>
```

Vue.js is watching over the used data properties. When Michael changes his selection, the data change event is fired. Note that the name of the property in the watch object must match the name of the data property.

At that point we need to store his selection - we form the data and make an async request to the serverless function - all using client-side JS.

```js
...
<script>
export default {
    ...
    watch: {
        option: function(newVal, oldVal) {
            let url = `{remote base URL}/action?id=${this.inviteeId}`;
            fetch(url, {
                method: 'POST',
                body: JSON.stringify({
                    option: this.option,
                })
            })
            .then(response => {
                if (response.status !== 200) {
                    alert("Unable to save, please try again.");
                }
            });
         }
    }
}
</script>
```

### Serverless Function implementation

I used Netlify to build and deploy the serverless function. If this is your first Netlify function, feel free to take a look at my [introduction video](https://youtu.be/0krLcVQjh28?t=623) where I show how to set up the local Netlify development environment.

The headless CMS has two APIs. One for data delivery - I used that one to get all data during site build - and another one for data management. In the serverless function, I need to use both APIs so I added the project ID and management API key to .env file in the root of the Netlify functions project:

```js
KONTENT_PROJECT_ID={project ID}
KONTENT_CM_KEY={management API key}
```

And it's always nicer to use an SDK than to struggle with bare REST API calls:

```js
npm i @dotenv --save
npm i @kentico/kontent-delivery --save
npm i @kentico/kontent-management --save
```

The beginning of the function looks like this:

```js
require("dotenv").config();
const KontentDelivery = require('@kentico/kontent-delivery')
const KontentManagement = require('@kentico/kontent-management')
```

The function is available more or less publicly - it's URL is stored in the client-side JS code in plain text - so we first need to do some elementary checks. Every request to this function needs to contain an ID parameter in the querystring that holds an identifier of an existing invitee. This is the person who filled the form. If the ID is missing or is invalid, we return 404.

```js
exports.handler = async (event, context, callback) => {
  const { KONTENT_PROJECT_ID, KONTENT_CM_KEY } = process.env;
  const deliveryClient = new KontentDelivery.DeliveryClient({ projectId: KONTENT_PROJECT_ID });
  let id = event.queryStringParameters.id;
  const invitee = await deliveryClient.items()
                    .type('invitee')
                    .elementsParameter(['accommodation'])
                    .equalsFilter('system.id', id)
                    .toPromise();
  if (invitee.items == null || invitee.items.length == 0)
  {
    return {
      statusCode: 404,
      body: `Invitee not found`
    };
}
```

The deliveryClient request is limited only to a single element - `accommodation`. That is because the information from the form is not stored within the _Invitee_ model but in a linked item of type _Accommodation_.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/nested-type.png)

The content model Accommodation directly corresponds to the form on the website:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/accommodation-map.png)

We want to store the data we got from the client-side JS as a new record. Updating the existing content item is also a possibility, but we would lose all history should the invitees change their selection in the future.

First, we note the ID of the existing _Accommodation_ content item and initialize the Content Management client.

```js
let accommodationId = invitee.items[0].accommodation.value[0].system.id;
const client = new KontentManagement.ManagementClient({ projectId: KONTENT_PROJECT_ID, apiKey: KONTENT_CM_KEY });
```

Then, we need to create a new language variant of the _Accommodation_ content item. Even if there is just one language in the project, content is stored in a separate bucket labeled with that language codename. This ensures a smooth transition should you decide to add additional languages in the future.

```js
await client.createNewVersionOfLanguageVariant()
      .byItemId(accommodationId)
      .byLanguageCodename('default')
      .toPromise();
```

This code does the same thing as if you click on "Create a new version" in the UI.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/create-new-version.png)

Next, we need to fill the variant with data. The data are coming as JSON in the request body.

```js
let accommodation = JSON.parse(event.body);
await client.upsertLanguageVariant()
    .byItemId(accommodationId)
    .byLanguageCodename('default')
    .withElements([{
        element: { codename: 'option' },
        value: [{ codename: accommodation.option }]
     }])
    .toPromise();
```

The last step is to publish the new variant:

```js
await client.publishOrScheduleLanguageVariant()
    .byItemId(accommodationId)
    .byLanguageCodename('default')
    .withData()
    .toPromise();
return { statusCode: 200, body: `OK` }
```

#### CORS issues with Netlify

Even if you're running the functions and static site locally, you will stumble upon a CORS issue as both implementations are being served from different ports. On all responses from the serverless function, you need to return the "Access-Control-Allow-Origin" header. 

Netlify has a simple way of handling this globally through the `netlify.toml` configuration file in the root of the functions project:

```js
[build]
  Functions = "lambda"
[[headers]]
  for = "/*"
  [headers.values]
    Access-Control-Allow-Origin = "*"
```

#### Old data after page refresh

Now the component reacts to the actions of the visitors. However, the initial state (which will also be displayed if the visitor refreshes the page) still comes from the static site build. If a visitor changes his or her selection, the change is saved in the CMS, but the site is not rebuilt. 

It would not be efficient to rebuild the whole site after every user interaction. Even if we did that, it would take a couple of seconds to minutes until the build and deployment are finished.

Instead, we do an async request when the component is first rendered:

```js
<script>
...
    mounted: function () {
        let url = `${baseUrl}/delivery?id=${this.inviteeId}`;
        let response = fetch(`{remote base URL}/delivery?id=${this.inviteeId}`, { method: 'GET', mode: 'cors' })
            .then(response => response.json())
            .then(accommodationObj => {
                this.option = accommodationObj.option;
            });
    },
...
</script>
```

The component will be pre-initialized with data during the site pre-build. But once the component is created, it will get fresh data from the CMS using another serverless function. That function is very similar to the previous one:

```js
exports.handler = async (event, context, callback) => {
  const { KONTENT_PROJECT_ID } = process.env;
  let id = event.queryStringParameters.id;
  const deliveryClient = new KontentDelivery.DeliveryClient({ projectId: KONTENT_PROJECT_ID });
  const invitee = await deliveryClient.items()
                    .queryConfig({ waitForLoadingNewContent: true })
                    .type('invitee')
                    .elementsParameter(['accommodation', 'option'])
                    .equalsFilter('system.id', id)
                    .toPromise();
  if (invitee.items == null || invitee.items[0] == null)
  {
    return {
      statusCode: 404,
      body: `Invitee not found`
    };
  }
  return {
	statusCode: 200,
	body: JSON.stringify({
		option: invitee.items[0].accommodation.value[0].codename
	})
  };
};
```

In this case, we need to add additional configuration to the data query - `waitForLoadingNewContent`. The content coming from headless CMS is cached and delivered via CDN so we may be getting outdated content if it was changed in the last few minutes. The configuration option ensures the response will always contain fresh data.

So, the overall process of a dynamic component on a static site looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/dynamic.png)

## It's Fast and Interactive

You see, the great benefit static sites bring is that all information available at build time can be served as static files, which is fast and easily scalable using a CDN. 

But they can also provide dynamic functionality that can be delivered via serverless functions - also cheap and easily scalable. 

If you take my website as an example - instead of having to deploy the whole application to the cloud, I only needed to host a bunch of small static files and two tiny serverless functions. And I'm also able to scale these functions independently.

Static sites may not be the ultimate choice for web development, but for many projects bring clarity, performance and security benefits as well as reduced maintenance costs. What is your experience? [Let me know.](http://bit.ly/38kyjt6)

Make sure to also check out my [Twitch streams](http://bit.ly/3akWp8l) and [YouTube channel](http://bit.ly/2TbMo7D) about Web Development.

