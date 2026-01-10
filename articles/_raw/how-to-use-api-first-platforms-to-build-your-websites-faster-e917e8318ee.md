---
title: How to use API-first platforms to build your websites faster
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T07:45:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-api-first-platforms-to-build-your-websites-faster-e917e8318ee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6T2sSRtPdHIgyrUCeOnVoA.jpeg
tags:
- name: api
  slug: api
- name: Developer Tools
  slug: developer-tools
- name: software architecture
  slug: software-architecture
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Mike Sedzielewski

  Tools like Jekyll, Hugo, or Hexo have popularized static websites in recent years.
  The so-called JAMstack allows you to deliver highly dynamic content with no back-end
  layer at all. Additionally, developer-first APIs enabled fron...'
---

By Mike Sedzielewski

Tools like [Jekyll](https://jekyllrb.com/), [Hugo](https://gohugo.io/), or [Hexo](https://hexo.io/) have popularized static websites in recent years. The so-called [JAMstack](https://jamstack.org/) allows you to deliver highly dynamic content with no back-end layer at all. Additionally, developer-first APIs enabled front-end developers to build even more complex functionality. This they can do without leaving the browser sandbox. Let’s see how you can leverage modern API-first platforms to ship a solid prototype of a business application. The approach presented in this article might become a useful asset in your solution architect’s toolbox.

The tutorial consists of 2 parts:

* The first will show you how to design the application to get a so-called happy path. We’ll build a semi-automated prototype you can use to get user feedback on a demo session
* The second explains how to step up the business processes automation so that the app can handle early traffic in production

### What’s an API-first platform?

As Ed Shelley from [ChartMogul](https://chartmogul.com/) describes it, there are a few rather hard-to-miss features of such a service:

* _There is NO user interface (GUI). Or in some cases, there is a GUI but it’s secondary to the core product._
* _Interaction with the service is through a web-based API. This is a programmatic way of connecting services and transferring data across the web in a machine-readable way._
* _The value of the service is usually in the data that’s delivered (through the API)._
* _Pricing is often usage-based, meaning that the cost is based on the number of requests made to the API._

Basically, what they offer is a set of building blocks, usually in the SaaS model. These you can use to construct a specific functionality with less code. One of the first and probably most notable representatives of this is [Stripe.](https://stripe.com)Stripe helps process payments. However, you might’ve heard about other big fish recently who’ve emerged from the market, like [Twilio](https://www.twilio.com/) or [Algolia](https://www.algolia.com/).

### Why use an API-first platform?

Let’s start with a small disclaimer. This tutorial describes how to develop applications with **no server-side at all.** However, we believe that is not a pragmatic approach to software architecture.

Rather, we want to highlight some parts of your back-end machinery that you don’t need to implement from scratch. This is especially true **when the business requirements for a particular feature aren’t set in stone** and your aim is to actually figure them out. In other words, to find out if the functionality gets a positive response from users and eventually has a place in your product.

At the same time, you don’t want to lock-in your product with a vendor providing an out-of-the-box solution. This is because you know it will lead to a “workaround hell” sooner or later. And, as you’ve learned, it’s hard to come back from there.

To give you an example, imagine that your company wants to build a blog. Moreover, they’ve already stated they want to extend it and monetize it down the road. There are 2 implicit requirements you need to take into consideration before coming up with a tech stack in such a scenario:

* You want to ship the blog functionality quickly — business can’t wait for ages for a simple blog.
* You don’t want to end up juggling Wordpress plugins.

The type of tools we want to present might be the answer. They give you some functional building blocks and your only task is to adapt them to your business.

You get happy because you have full control over your code base. Additionally, the management is happy too because they get value from day 1. Plus, they don’t have to pay up-front!

So, let us now show you how these tools can save weeks of engineering time while still keeping your code base open for changes.

**Note:** The tools we’re going to use work in server-side mode too. They actually offer more functionality when connected using secure API keys. So, we think it’s more pragmatic to have it integrated on the server-side. Nonetheless, as an experiment, we will use the client-side functionality only. Additionally, we will use some [Zapier](https://zapier.com/) glue to automate different business processes quickly.

### nostalgia.io

We’re going to build a marketplace for the legacy web technologies consultants — nostalgia.io. If by any chance you seek help with an old system based on Struts or Google Web Toolkit, this is the place to go. In the first part of this tutorial, we’ll learn how to leverage several API-first platforms to ship the following functionality:

* Browsing through legacy technologies
* Full-text searching and filtering of experts
* Booking meetings with experts
* Discounting with coupons

The tech stack will comprise of:

* [Contentful](https://www.contentful.com/) — as a database for technologies and experts
* [Algolia](https://www.algolia.com/) — for the full text search
* [Timekit](https://www.timekit.io/) — for availability checking and booking
* [Typeform](https://www.typeform.com/) — for forms
* [Voucherify](https://www.voucherify.io/) — for coupon management (disclaimer: this is our product)

**Note:** We won’t cover authentication and payment processing itself. You can try implementing them yourself as homework (hint: [auth0](https://auth0.com/) and [Stripe](https://stripe.com) might be helpful).

Let’s jump into the code.

**Note 1:** for brevity, we won’t be describing a detailed step-by-step guide. You should look up the missing parts in the specs — fortunately, API-first providers tend to have developer-friendly docs, comprehensive API reference, and dozens of useful guides.

**Note 2:** there are a plenty of ways you can host your static website. We’ll use [glitch](https://glitch.com) development platform so that you can easily [remix](https://glitch.com/about/) it and play with it yourself.

**Note 3:** we don’t care about the look and feel of the application not to obscure the integration part, plus it somehow fits the business theme, doesn’t it? :)

### Data Model — Contentful

Usually, the application’s design starts with a data relationship model. This should be the first concern for us too. But let’s skip the database providers discussion for a moment and jump straight into models. How so?

Meet [Contentful](https://www.contentful.com/) — a headless CMS. Using a stark simplification, you can think of it as a Wordpress without front-end.

It enables:

* **developers** to deliver the content adjusted to the medium, be it website, mobile app or VR device — this is done through RESTful API
* **marketers** to create, manage, and publish content without having to deal with the formatting — with the support of the content modelling dashboard and rich-text editor

We’ll use Contentful to create 2 basic entities — Technology and Expert. An Expert knows one or many Technologies. Let’s see how easy it is to create such entities, add some real objects, and display them on a static page.

### Technology Browser

With Contentful’s model manager, designing an entity is as easy as drag’n’dropping new fields into the data content model manager. There are 8 different types. These include the default, like a string or number. There as also some specific types, like Location or Media, which come with useful properties.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lKRyvvSWtYX8R1VkRpdvsQ.png)

Create a free account. Then follow the on-boarding guide to create a space.

Finally, create your first model, similar to what you can see in the screenshot below:

![Image](https://cdn-media-1.freecodecamp.org/images/1*oeOvlrFC7In9Eqtrq_ydaQ.png)

Now that you have the Technology model, go to the Content tab to create a couple of instances. As you can see, Contentful provides an intuitive editor for data entry. It takes care of data validation, localization, publishing status, version control, and much more. It’s first and foremost a developer-first platform. Yet these features satisfy marketers and content managers too.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZnSZwdmKWRIB4miEM36Vlw.png)

Enough clicking, let’s get to coding. The first task is to display the technologies we’ve just created. To do so, we’ll use Contentful JavaScript [SDK](https://github.com/contentful/contentful.js).

It makes fetching technologies easy and comes down to 3 steps:

* Create a new [glitch](https://glitch.com) website project, load the `contentful.js` script, and initialize it with the credentials you can find in the API section.

**Note:** there are 2 types of keys available in Contentful. One is for content management and one is for content delivery.   
The first type can be used to create, update, or delete new models or their instances programmatically.  
The second gives you a way to deliver your content to your website or app.  
This distinction has been made for security reasons. You don’t want to publish your content management keys on your website, do you? The same applies to the other API-first platforms we’re using in this tutorial.

* Call [getEntries](https://contentful.github.io/contentful.js/contentful/5.0.5/ContentfulClientAPI.html#.getEntries) method. This loads the content according to your query parameters. In our case, we want to load only the “Technology” entities. Build some front-end on top of the data . What you get from Contentful is pure JSON ([example](https://gist.github.com/sedzia/56d83d61c35720ecdbe7302c53154888)). Now you can display it to your users as you want. That’s one of the biggest pros when you want or have to adapt your content to multiple devices.

Take a look at this gist:

```js
const client = contentful.createClient({
    space: SPACE_ID,
    accessToken: ACCESS_TOKEN
  })
    
  const techCards = document.querySelector('#cards');

  function fetchTechnologies () {
    return client.getEntries({
        content_type: "technology"
      })
    .then((response) => response.items)
    .catch((error) => {
      console.log(`\nError occurred while fetching Entries for Technology:`)
      console.error(error)
    })
  }

  fetchTechnologies().then((technologies) => {
    techCards.innerHTML += technologies.map(technology => 
      `<div class="col-md-4">
        <div class="card">
          <a href="${technology.fields.link}"><img src="${technology.fields.logo.fields.file.url}"/></a>
          <h2><a href="/experts.html?t=${technology.fields.name}">${technology.fields.name}</a></h2>
          <p>${technology.fields.description}</p>
        </div>
      </div>`).join('')
  })
```

Short and sweet, isn’t it? You can see the overall effect [here](https://glitch.com/edit/#!/meteor-rooster?path=index.html).

### Adding Experts and the Search

So, now we want to display the list of experts when somebody chooses a particular tech. That should be similar to what we’ve just done with Technology a second ago. But let’s make it a bit more advanced. What if we want to make experts searchable? Think of full-text search in their profiles and also a price filter.

Certainly, you can build it on top of Contentful. For example, add another entity, configure search mechanics and UI with `getEntries`, but there’s a faster way. And by saying faster I mean in both implementation time and the speed of loading search results.

We’ll use another API provider — [Algolia](https://www.algolia.com/). Their platform makes it easy to build and maintain super-fast full-text search. They take care of typo-tolerance, synonyms, geosearch and other little issues. These issues you would most likely bump into when your search feature goes to production.

How does it work? You just use a RESTful API to feed their engine with the data. Then, you configure what attributes should be searchable and how the results should be ranked. Finally, using their JavaScript SDK, you can deliver the instant search experience to any website. Let’s make our experts searchable now!

We’ll start off by creating a data model in Contentful and creating a relationship with Technology entity. Then, we’ll build an Algolia index and add our entities (JSON format) to it.

Add another content model with the fields you can see below:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Qq8QlKi9kx1j6T6cmasC9g.png)

Notice that we’ve made a one-to-many relationships using the Reference field type. We just want to reflect that any expert might know more than one tech. Once ready, add some experts and assign them to their technologies manually. Use multiple technologies for one of the experts.

You should end up having a similar list:

![Image](https://cdn-media-1.freecodecamp.org/images/1*OsClINqbZQt9BKiMFw9UkA.png)

And the JSON structure looks like:

```json

{
   "sys":{
      "space":{
         "sys":{
            "type":"Link",
            "linkType":"Space",
            "id":"n763nxcwuf4y"
         }
      },
      "id":"1mn1mwlwAcQWqgQamsIEmW",
      "type":"Entry",
      "createdAt":"2017-12-05T11:29:35.202Z",
      "updatedAt":"2017-12-13T10:04:52.381Z",
      "revision":7,
      "contentType":{
         "sys":{
            "type":"Link",
            "linkType":"ContentType",
            "id":"expert"
         }
      },
      "locale":"en-US"
   },
   "fields":{
      "name":"Javier Hernandez",
      "technologies":[
         {
            "sys":{
               "type":"Link",
               "linkType":"Entry",
               "id":"5oKmKwfdjGO2cCaCkwamKW"
            }
         },
         {
            "sys":{
               "type":"Link",
               "linkType":"Entry",
               "id":"7Dtej0GnXqw6cSIMmA6Cko"
            }
         }
      ],
      "image":{
         "sys":{
            "type":"Link",
            "linkType":"Asset",
            "id":"4RZoQOCwvCMEWMMCuqA0ey"
         }
      },
      "description":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sed faucibus turpis in eu mi bibendum. Mauris in aliquam sem fringilla ut. Tincidunt nunc pulvinar sapien et ligula. ",
      "projects":53,
      "price":40,
      "city":{
         "lon":2.2247314453125,
         "lat":41.36933709640475
      }
   }
}
```

Let’s upload our experts to Algolia. Sign up for a free account, go to the Indices section and run `NEW INDEX.`

Now we need to transfer our entities from Contentful to Algolia. We could’ve used a dedicated [migrator](https://github.com/drublic/contentful-to-algolia). This is a fantastic tool that automatically loads your content. It then removes, in this case redundant, the Contentful system information (see the gist above) from effective JSONs. It can also resolve relationships. For example instead of IDs, you’ll send the actual names when it comes to the “technologies” field. Finally it syncs with the Algolia index.

But we’ll deliberately do it manually. We need a small improvement in the way we build our index. Therefore, syncing one-to-one with the migrator isn’t an option in our case.

When we use search input in a technology site, naturally we want to include only the experts of chosen technology in the search results. As you can see in the Expert JSON example, technologies are represented as an array of objects. The problem is that you can’t build a facet which filters the data based on a nested array of objects with Algolia.

What they suggest is to split the expert object into as many sub-objects as the number of technologies. So, in the case of Javier Hernandez, who knows 2 frameworks, we should add 2 objects:

```json
{
  name: "Javier Hernandez", 
  technologies: { 
    name: “Google Web Toolkit”
    … // other properties
  }
  … // other properties
} 
{
  name: "Javier Hernandez" 
  technologies: { 
    name: “Apache Struts 1”
    … // other properties
  }
  … // other properties
}
```

As an exercise, you can create a script that splits experts and adds them to the index through the Algolia API. You’ll need Algolia server-side authentication keys. Here’s a snippet which handles the split logic. Notice that the script also purges Contentful’s system info.

This makes the objects lighter will make the search faster:

```js
client.getEntries({ content_type: "expert" })
  .then((response) => {

    const denormalized = [].concat(...response.items.map(item => {
      let arr = []
      
      item.fields.contentfulID = item.sys.id
      delete item.sys

      item.fields.technologies.forEach(tech => {
        const i = JSON.parse(JSON.stringify(item))
        i.fields.technologies = tech.fields
        i.fields.image = item.fields.image.fields
        arr.push(i.fields)
      })
      return arr
    }))
    console.log(JSON.stringify(denormalized))
  })
  .catch((error) => {
    console.log(`\nError occurred while fetching Entries for Expert:`)
    console.error(error)
  })
```

As we have 6 experts and 2 of them know 2 technologies, we should end up with 8 objects in the index. As an alternative to the API insert method, you can upload them with the dashboard. Once uploaded, you can try to use the search in the Dashboard to see how fast Algolia filters the data.

![Image](https://cdn-media-1.freecodecamp.org/images/1*B2JuHiQdwdCpUDZYxRStXA.png)

Now, we’re almost ready to connect our search to Algolia. Almost — because we need to create a facet which will allow us to filter results by technology and price. Go to DISPLAY and select `technology.name` and `price` in “Attributes for faceting”, then Save.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9rKcjASE_hiv3RSYX15Y4w.png)

Finally, we can connect our search to our index so that it retrieves and displays the results. Algolia comes with an advanced JavaScript library which makes it easy as pie.

Take a look at this code:

```js
const isConfig = {
    appId: 'N675AF3ESI',
    apiKey: '14b65c352deb9a505131d3d00cba2f6c',
    indexName: 'experts',
    urlSync: false
  }
  
isConfig.searchParameters = {
  filters: `technologies.name:"${selectedTechnology}"`
}

const search = instantsearch(isConfig)

search.addWidget(
  instantsearch.widgets.searchBox({
    container: '#search-input'
  })
)

search.addWidget(
  instantsearch.widgets.hits({
    container: '#hits',
    hitsPerPage: 10,
    templates: {
      item: document.getElementById('hit-template').innerHTML,
      empty: "We didn't find any results for the search <em>\"{{query}}\"</em>"
    },
    cssClasses: {
      root: 'row',
      item: 'col-md-4'
    }
  })
)

search.addWidget(
  instantsearch.widgets.rangeSlider({
    container: '#price-refinement',
    attributeName: 'price',
    tooltips: {
      format: function(rawValue) {
        return '$' + Math.round(rawValue).toLocaleString();
      }
    }
  })
)

search.start()
```

Notice how we configure the search to use the technology filter in lines 8–10. See how easy it is to adjust the result page to a respective container — line 28 (though it’s hard to find in the docs).

Overall, with about 2-dozen lines and you get this:

<iframe src="https://giphy.com/embed/3o751QR0q4ELZfyICs" width="480" height="276" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

So far, we’ve built a simple expert browser supporting full-text search and price sliders. Adding new experts is troublesome at this stage because you have to first manually create them in Contentful and then sync it with Algolia. We’ll automate this in the second part.

The good news is that you can already use this prototype to get some early feedback for the technology browsing and experts filtering. The next step is to create the expert profile page and enable booking.

The search demo code can be found in [experts.html](https://glitch.com/edit/#!/nostalgia?path=experts.html).

### Bookings

As you might’ve guessed, we won’t be implementing calendar functionality from scratch either. We’ll use [Timekit](https://www.timekit.io/). They offer the API + dashboard to manage calendars and bookings for people and resources. Think of it as a Google/Outlook calendar engine exposed with REST API.

The process of making experts bookable with Timekit is as follows:

* Create a Resource entity and an assigned Calendar entity
* Store the resource and calendar IDs in a corresponding expert entity in Contentful
* Use Timekit JS SDK to display the calendar on an expert’s profile page

And that’s it, you’ve just got bookings up-and-running! Don’t believe me? Read on:

* Create an account and start a [free trial](https://www.timekit.io/) (there’s no free version).
* Create a Project in which you’ll define the basic calendar mechanics . For instance, event duration, minimum notice, and reminders.
* Define if the booking requests should be accepted automatically or must be confirmed manually.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Bb_JKj1_bMeayT7BjAb-3A.png)

For each expert, create a resource and within this resource, create a calendar. Notice that one resource might have more than one calendar.

This is a nice feature to keep in mind when we plan some upgrades in Nostalgia’s business model.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kXLZEwb6pa_ZTJYjKGaMsw.png)

Now, we have to store the resource’s email, newly created calendar ID, and the client-side API key in the corresponding expert entity in Contentful.

You can edit the expert content model and add a JSON field named `timekit`. Then, modify the expert entities to add `timekit` details.

The last step is to display the actual calendar in the expert’s profile page. You already know the process. Include an SDK script and configure it properly to render the widget.

But this time we need to load 2 libraries:

* Contentful — to load customers details, including Timekit credentials
* Timekit — to place the calendar assigned to a given expert

![Image](https://cdn-media-1.freecodecamp.org/images/0*t-RhbQuc-QEVo1sr.)

Here’s the code:

```js
const widget = new TimekitBooking()
  
const client = contentful.createClient({
  space: SPACE_ID,
  accessToken: ACCESS_TOKEN
})

client.getEntries({'sys.id': expertId}).then((response) => {
  const e = response.items[0].fields

  expertWidget.innerHTML=
  `
  <div class="row card hit">
    <div class="col-md-4">
        <div class="hit-image">
          <img style="height: 5em" src="${e.image.fields.file.url}" alt="${e.name}">
          <h2 class="hit-name">${e.name}</h2>
          <h2 class="hit-price">$<span id="priceTag">${e.price}</span></h2>
        </div>
    </div>
    <div class="col-md-8 start-xs">
        <div class="hit-content">
          <h4 class="hit-price">projects: ${e.projects} </h4>
          <p class="hit-description">${e.description}</p>
        </div>
    </div>
  </div>
  `

  const timekitConf = e.timekit

  widget.init({
      targetEl: '#bookingjs',
      app:      'nostalgia-4592',
      apiToken: timekitConf.apiToken,
      email:    timekitConf.email,
      calendar: timekitConf.calendar,
      name:     'Jane Doe',
      timekitFindTime: {
        length: '3 hours',
        start: 'tomorrow',
        filters: {
          and: [
            { specific_time: { start: '8', end: '17' }}
          ]
        }
      },
      fullCalendar: {
        defaultView: 'month'
      }
    })    

})
.catch((error) => {
  console.log(`\nError occurred while fetching Entries for Expert:`)
  console.error(error)
})
```

Notice how we can adjust the booking details such as time slots (line 39). Timekit offers even more customization capabilities, so make sure to read the [booking.js](https://github.com/timekit-io/booking-js) spec.

The effect just blows us away. Twenty lines of code and we have our booking widget in place. Timekit oversees the whole process for you. It helps with resolving conflicts and sends email confirmations to experts and customers.

The most important thing is that this approach is highly flexible. It’s all in code. Every single piece of this mechanism can be adjusted through the API.

For example, let’s suppose we want to review a booking request before accepting. It just so happens that Timekit makes it possible with a single flag. Such options are the real power of API-first solutions. Make sure you read the tutorials and docs to learn all the features.

### Coupons

Nostalgia isn’t a well-known business yet. We need to find some way to attract early adopters. One of the oldest and most successful methods is discounts. A discount might be applied either after redeeming a coupon or because of the volume of products in the cart. To implement both cases, you might want to use [Voucherify](https://www.voucherify.io/).

Why Voucherify? There are a few basic things you should get right when you want to handle coupons properly to save yourself tons of engineering time:

* Uniqueness of coupon codes — To reduce fraud and get precise tracking of your promotional campaigns
* Extensible coupon validation mechanism — This is a generic approach which enables adding/removing/expiring multiple coupon codes
* Easy monitoring of redemption — This will answer marketing and customer service department questions off the bat

You can take care of these 3 things yourself. However, you can get the same result with a couple of lines using Voucherify API endpoints. By doing so, you can immediately forget about coupon misuse, maintaining the “if” ladder validating whether the code is active and valid. You can also forgo providing marketing teams with coupon campaigns results. Nor will you be drilling down the logs to understand why a customer’s redemption failed.

Let’s create a bulk 1000 coupons. These we’ll send to our early adopters. Finally let’s give the customers the possibility to actually use them in our website to enjoy discounted prices.

Sign up for a Voucherify account and go to the [campaign manager](http://support.voucherify.io/article/17-how-do-i-create-my-first-campaign) to create the first batch of coupon codes. Let’s say each coupon carries 25% off.

In the manager, you can specify the discount details and other business limits. For example, specify the expiration date, max total amount, or a specific customer segment eligible for the discount.

![Image](https://cdn-media-1.freecodecamp.org/images/1*REoy3OlagtuWrQcV81MXZA.png)

When the manager is done, you can start distributing coupons through various channels. Voucherify offers email, sms, push notification, intercom or braze out of the box. But there’s a lot of other ways available thanks to REST API and webhooks.

Before you send them out, you should give customers an option to redeem them. This can be achieved by using the [redemption](https://docs.voucherify.io/reference#redeem-voucher) endpoint from the API. Yet, you can also use the pre-built widget from [voucherify.js](https://github.com/rspective/voucherify.js).

![Image](https://cdn-media-1.freecodecamp.org/images/1*b_RjBXbyhxI1QmQN600A0w.gif)

Voucherify allows you to either validate or redeem the coupon.

The validation checks if:

* the coupon comes from your Voucherify account
* is not expired or disabled
* it matches all business rules

The redemption does the validation first and **subsequently** **marks the coupon as used**. In this part, we’ll wire in validation only to show customers a discounted price. In the second article, we’ll send a redemption request when the booking is confirmed.

Include `voucherify.js` snippet and optionally the corresponding CSS file for a better look and feel. Then, put in the following code:

```js
Voucherify.initialize(
    "4dde7477-d8d1-4057-8f91-8a9e7137acee",
    "404c6c0b-4445-4f14-84b1-f4a58f1da2f6"
)

Voucherify.render("#voucher-widget", {
    textPlaceholder: "Your coupon...",
    onValidated: function(response) {
      if (response) {
        const priceTag = document.querySelector('#priceTag') 
        priceTag.innerHTML = Voucherify.utils.calculatePrice(parseInt(priceTag.innerHTML), response)
      }
    }
})
```

The library will render a coupon widget which automatically validates the code against the Voucherify API.

You can test it out with the codes we’ve pre-generated with the campaign manager:   
* 25% off: _nstlg-CCAMIDFf, nstlg-wZK4CoLs, nstlg-V8eV9A3p_  
* $5 off: _uub-nstlg, afl-nstlg, yeq-nstlg_  
_*_ expired code_: VuFF2Wyy_

Notice that you can easily customize codes patterns, prefixes and post-fixes can be useful for tracking and reporting.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9LQC64sGNxoYoH7f7LUFJA.png)

Now, paste any coupon code into the widget and see the corresponding discount applied:

![Image](https://cdn-media-1.freecodecamp.org/images/1*J0-_vtjHA8vJy8bGgpLlDQ.png)

n the 2nd article, we’ll show you how to monitor the successful and failed coupon redemptions to see if your promo campaign is on track.

Voucherify offers much more than that. Check out the [docs](https://docs.voucherify.io) and [examples](http://docs.voucherify.io/docs/examples) to find out how to build advanced promotions and referral programs in days instead of months.

You can find the booking page code here ([scheduler.html](https://glitch.com/edit/#!/nostalgia?path=scheduler.html)).

### Recap

We planned to build a proof of concept for a new business application — Nostalgia.io. A prototype we can use to pick early users’ brains. Something we can deliver in a decent timeframe yet not a total throwaway.

Hopefully, we’ve convinced you that with developer-first tools like **Contentful**, **Algolia**, **Timekit**, or **Voucherify** you can achieve it. Even more importantly, you can do it without setting up any back-end layer at all.

It still requires some manual work to keep data in sync among tools. Yet, the flexibility and speed of iteration of these API-first tools at your fingertips definitely makes up for it.

Certainly, these tools aren’t all light and bright. For example, we bumped into these several issues when going through this article:

* Contentful `getEntry()`method doesn’t resolve links. We had to use `getEntries()` instead to get a single expert entity with profile image URL
* It took us more than a little while to understand how we can display results using column layout (the default is rows)
* Timekit doesn’t allow for fetching the calendar instance config using an external id. That’s why we need to store calendar tokens in expert entity in Contentful
* The Voucherify widget doesn’t enable you to try another valid code without refreshing the website

I’m sure there are many more of them. But you can work these little issues around in far less time than you’d spend to build these features from scratch. On top of that, you avoid the serious and time-consuming architectural mistakes the teams at these platforms have made before you.

The source code of the project can be found [here](https://glitch.com/edit/#!/nostalgia?path=index.html:1:0). And the demo is live [here](https://nostalgia.glitch.me/)!

### Hardening and scaling

As you can see, some processes are still manual and thus tedious:

* Adding new experts
* Making experts searchable
* Creating calendars for experts

In the next part, we’ll glue these services using [Zapier](https://zapier.com/). Zapier is a platform which facilitates connecting API-first platforms. This way, we’ll reduce the manual work necessary to run the aforementioned business flows. For example, experts will be able to sign up themselves. Additionally, the platform will create all the necessary entities programmatically.

Lastly, we will push the prototype to production. It will still be an early stage application but it’ll be more robust and ready to serve real customers. Stay tuned!

**Update**: you can find the second part is [here](https://www.freecodecamp.org/news/how-to-use-api-first-platforms-to-build-your-websites-faster-part-2-68085d7cdf36/).

