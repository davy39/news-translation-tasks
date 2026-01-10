---
title: How to Test and Play with Web APIs the Easy Way with Postman
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-06-30T16:34:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-test-and-play-with-web-apis-the-easy-way-with-postman
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/postman.jpg
tags:
- name: api
  slug: api
- name: Developer Tools
  slug: developer-tools
- name: programing
  slug: programing
- name: QA
  slug: qa
- name: Quality Assurance
  slug: quality-assurance
- name: REST API
  slug: rest-api
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: Software Testing
  slug: software-testing
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Testing
  slug: testing
- name: tools
  slug: tools
seo_title: null
seo_desc: "In a world where static websites and apps increasingly depend on separately\
  \ maintained APIs, it can be hard to figure out how they work by just playing around\
  \ in the browser. \nSo how can we use Postman to both test our existing APIs and\
  \ understand ho..."
---

In a world where static websites and apps increasingly depend on separately maintained APIs, it can be hard to figure out how they work by just playing around in the browser. 

So how can we use Postman to both test our existing APIs and understand how they work?

* [What is Postman?](#heading-what-is-postman)
* [What are we going to build / learn?](#heading-what-are-we-going-to-build-learn)
* [Part 0: Getting set up with Postman](#heading-part-0-getting-set-up-with-postman)
* [Part 1: An introduction to Postman](#heading-part-1-an-introduction-to-postman)
* [Part 2: Creating a new Postman request to GET info about Squirtle](#heading-part-2-creating-a-new-postman-request-to-get-info-about-squirtle)
* [Part 3: Creating a collection of requests in Postman for the PokéAPI](https://www.freecodecamp.org/news/p/a02335e1-4f9a-453d-8916-db6b8419cf99/part-3-creating-a-collection-of-requests-in-postman-for-the-pok-api)
* [Part 4: Making POST requests with Postman to translate sentences to sound like Yoda](#heading-part-4-making-post-requests-with-postman-to-translate-sentences-to-sound-like-yoda)
* [Part 5: Authenticating requests to the Lord of the Rings API with an API Key](#heading-part-5-authenticating-requests-to-the-lord-of-the-rings-api-with-an-api-key)

%[https://www.youtube.com/watch?v=KFuaybrXCdw]

## What is Postman?

[Postman](https://www.postman.com/) is a tool teams can use to reliably test APIs using easy to use configurations. It comes stocked with features you would expect when dealing with APIs, including authentication, setting headers, customizing the payload, and a bunch more that help reduce the friction of using an API.

And it’s not just for testing. The beauty is that this can be used for many aspects of working with APIs for many different members of the team. Maybe a Project Manager wants to verify that things work or might find it easier to make a change straight with the API, or a QA Engineer needs to make sure everything still works, or a developer wants to actively make changes while working on the API itself.

The best part about it – Postman provides collaboration features. The free tier includes exporting and importing collections of saved API requests as well as creating shared links. If you're part of a team, they have paid tiers that allow you to sync up your collections to make sure everyone has the most recent and up to date collection.

## What are we going to build / learn?

We’re going to walk through two different example APIs to cover the concepts of Postman.

First, we’ll walk through some simple HTTP requests with a [public API for Pokémon](https://pokeapi.co/).

We’ll then use the Yoda Translator API for one part to demonstrate how to make specific HTTP requests.

Once we understand how the basics work, we’ll use the [Lord of the Rings API](https://the-one-api.herokuapp.com/) to learn how authentication works with APIs. For this, you’ll need to register for a free account for an API key.

## Part 0: Getting set up with Postman

Before we get started, you’ll need [Postman](https://www.postman.com/downloads/) in order to follow along with this walkthrough. The good news, is Postman is available for free on Mac, Windows, and Linux, so you should be able to find a version that works for you.

Get Postman: [https://www.postman.com/downloads/](https://www.postman.com/downloads/)

Once downloaded, go through the standard installation instructions, open it up, and we should be ready to go!

## Part 1: An introduction to Postman

The first time you open up Postman you’ll immediately be shown a launchpad with a bunch of options to get started.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-launchpad.jpg)

It might seem a bit overwhelming, but let’s break down some of the key concepts that we’ll need to know.

### Requests

A request is kind of what it sounds like, it’s a specific API request. This will be a single type of request, whether it’s a GET or POST to a specific endpoint. You’ll want to create new requests for each type of endpoint which will allow you to move between them when testing.

### Collections

A collection is a group of requests. This is handy for organizing your requests into different groups. This could be as simple as two totally different APIs (ie. Twitter vs Slack) or it could be two different groups of APIs for a single API (ie. Twitter Tweets API vs Twitter Accounts API).

### Authorization

Authorization is how requests are authenticated with an API, whether by a person making a request or by a computer making that request on your behalf. This commonly comes in the form of an API key which can be a static value assigned to your account or dynamically generated with tools like [OAuth](https://oauth.net/).

### Environments

Environments will allow you to configure your endpoints to use specific variables that make it easier to use the same endpoints between different environments. For instance, you might have the same `/profile` endpoint on both your production and development environments, but they have different domains. Environments lets you manage a single request with a variable domain.

### Workspaces

We won’t go too far into workspaces in this post, but it allows you to manage and organize different sets of collections. Imagine if you want to use Postman for both work and a personal project, you might have a Work workspace as well as a Personal workspace.

For the purposes of this article, we’ll be covering Requests, Collections, and Authorization.

## Part 2: Creating a new Postman request to GET info about Squirtle

Now that we have a better understanding of the different terminology, let’s actually create a request.

At the top left of the UI you should see a but orange button that says **New**. Go ahead and click that and then select **Request**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-create-new-request.jpg)

Before we get into the request itself, it requests a few things.

This first thing requires is a name. We’re going to start off by requesting information about the Pokémon Squirtle, so let’s name this “Pokémon - Squirtle”.

It also requires a collection, so click **Create Collection** and let’s name the collection “My Favorite Pokémon”.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-configure-new-request.jpg)

Click the orange checkmark button next to the collection name then hit **Save**.

At this point we’ll have a new request, so let’s build that request.

There are two things we’ll first need to fill out for our first request:

* **Request type:** GET, POST, PUT, etc - we’ll use GET
* **Request URL:** The endpoint for your API request - for our request we’ll use [https://pokeapi.co/api/v2/pokemon/squirtle/](https://pokeapi.co/api/v2/pokemon/squirtle/)

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-squirtle-pokemon-get.jpg)

And once you make sure those are correct, you can simply hit the blue **Send** button on the right and we’ve successfully made our first request!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-squirtle-pokemon-get-success.jpg)

We immediately get a few things we can see:

* **Body:** at the bottom we should now see the response body of the API request. For our Squirtle API, we should have a JSON object with data like `abilities`, `base_experience`, and `forms`.
* **Status:** on the right, we should see the HTTP status code. “200 Ok” is a good sign and it means it was successful!
* **Time:** simply how long the request took to finish
* **Size:** the size in KB (in our example) of the response data

You can also hover over Status, Time, and Size and get a more in depth look at each option.

So we made our first request!

Once thing to notice before we move on is that our request looks like it’s in a browser tab. If we’re done with that particular request, we can close the tab and click **Save** to make sure all of our changes are there for next time!

## Part 3: Creating a collection of requests in Postman for the PokéAPI

Now that we’ve created a request, let’s create a collection of them. Technically we already had to create a new collection for Part 2, but we’ll create a new one to learn how collections themselves work.

At the top left of the UI, click the orange **New** button again and select **Collection**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-create-new-collection.jpg)

Similar to a request, it asks for a name so let’s call this “PokéAPI”. Optionally you can add a description, then click **Create** at the bottom.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-configure-new-collection.jpg)

On the left, you’ll now see your collection. You can select and expand the folder since we’ll be working with it.

Before we add a request, the PokéAPI has different types of requests, so it makes sense to organize it a little more thoroughly. So let’s click the three dots next to the PokéAPI collection and select **Add Folder**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-add-folder-to-collection.jpg)

Similar to the others, this asks for a name. Folders are kind of like collections inside of a collection, so you get similar options. Let’s name this one “Pokémon” and click the orange **Save** button like before.

Now let’s add our requests! First, click the three dots next to the Pokémon folder, similar to how we added a folder to the collection, but this time select **Add Request**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-add-request-to-collection.jpg)

Let’s name this request “Pokemon”. While it might be confusing that we have a Pokemon request inside of the Pokémon folder, Pokemon is just one of the endpoints of the Pokémon group.

Now, let’s use the same exact API that we used with our Squirtle request before:

* **Request Type:** GET
* **Request URL:** [https://pokeapi.co/api/v2/pokemon/squirtle/](https://pokeapi.co/api/v2/pokemon/squirtle/)

And similar to before, when we hit the blue **Send** button, we should see a successful request!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-successful-get-request-squirtle.jpg)

Now let’s add another request. Follow the same process as before to create a new request under the PokéAPI Pokémon folder and let’s name this request “Abilities”.

If you scroll through the response from the first Squirtle endpoint, you see a lot of other API urls. At the top, we have `abilities` and we have two different ones — “torrent” and “rain-dish”.

Choose your favorite Squirtle ability and copy the `url` value into the new Abilities request we just created, I’m going to use `rain-dish`.

We can leave the Request Type as GET, hit the blue **Send** button, and we can again see a successful response!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-successful-request-squirtle-abilities.jpg)

Here we get a lot of information about our Squirtle ability Rain Dish and some of the details come in different languages which is cool!

So now we have a new PokéAPI collection with a Pokémon folder representing the group of Pokémon API endpoints including Pokemon and abilities.

We’re going to stop Part 3 with those 2 requests, but feel free to continue on and add as many of the PokéAPI requests as you’d like!

## Part 4: Making POST requests with Postman to translate sentences to sound like Yoda

So far we’ve only made GET requests, but what if we wanted to make a POST request where we need to actually send some data?

For making a POST request, we’re going to use the Yoda Translator API from funtranslations.com. While this API only takes a single parameter, it’s still a good public endpoint we can use to understand the concept.

First, let’s create a new collection with a new request:

* **Collection:** Fun Translations
* **Request:** Yoda

This time, instead of a GET request, our request configuration will be:

* **Request Type:** POST
* **Request URL:** [https://api.funtranslations.com/translate/yoda](https://api.funtranslations.com/translate/yoda)

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-new-request-yoda-api.jpg)

Now this time, if we hit the blue **Send** button, we’ll notice we don’t get a successful 200 response, we get a 400!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-yoda-api-bad-request.jpg)

We never actually set up any data to be posted to the API and it requires that data, so let’s add it.

Right below the **Request URL**, click **Body**. Then instead of none, select **raw** as the body type. Finally, on the far right of the types, change **Text** to **JSON**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-yoda-request-body-type.jpg)

Then, in the space below it, you can add the following:

```json
{
    "text": "Hello, I am learning how to test APIs with Postman!"
}

```

And now click the blue **Send** button again and we get a successful response!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-successful-post-body-yoda-api.jpg)

We can apply this concept to pretty much any API. Postman doesn’t only permit you to post JSON, it allows you to use the other formats that we see listed in the Body Type section, meaning you have a lot of options depending on what the API you’re using requires.

## Part 5: Authenticating requests to the Lord of the Rings API with an API Key

For the rest of the walkthrough, we’re going to use the Lord of the Rings API.

First up, the Lord of the Rings API requires authentication in order to make requests using an API key. So to start, you’ll before we dive in, you’ll need to go [create a free account](https://the-one-api.herokuapp.com/sign-up).

[https://the-one-api.herokuapp.com/sign-up](https://the-one-api.herokuapp.com/sign-up)

Once you sign up and log in, the first thing you’ll see is your API key! Either copy this key down or remember where you can find it for later. If you leave the page, you can always grab it by navigating to **Welcome** and then **Account** in the navigation of the API website.

To get started, let’s first create a new collection and request:

* **Collection:** Lord of the Rings
* **Folder:** Movie
* **Request:** All Movies
* **Request Type:** GET
* **Request URL:** [https://the-one-api.herokuapp.com/v1/movie](https://the-one-api.herokuapp.com/v1/movie)

Once you’re set with the above, click **Send**, and you’ll notice immediately it gives a response that says 401 and that it’s unauthenticated.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-unauthorized-request-lord-of-the-rings-api.jpg)

Because this API requires the API key, this is exactly what we expected. So let’s click on the **Authorization** tab. We can then select a **Type** of **Bearer Token**, and on the right, we can paste in our key that we just set up with the Lord of the Rings API.

And as soon as we hit **Send**, we now see a successful response!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-authorized-successful-lord-of-the-rings-api-request.jpg)

This worked really great, but what if we have a bunch of requests that use a single key. Do we have to manage that on each request?

Instead of managing it on each individual request, we can manage it on the collection. Let’s first build another request.

Under our Lord of the Rings collection and in the Movie folder, create a new request:

* **Request:** Quote by Movie ID
* **Request Type:** GET
* **Request URL:** [https://the-one-api.herokuapp.com/v1/movie/{id}](https://the-one-api.herokuapp.com/v1/movie/%7Bid%7D)

In this request, let’s use an ID from the response of the first request, I’m going to use `5cd95395de30eff6ebccde5b` which is the ID of The Two Towers, so the request URL will look like:

```
https://the-one-api.herokuapp.com/v1/movie/5cd95395de30eff6ebccde5b
```

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-inherit-authorization-from-parent.jpg)

Now, instead of setting our token in the request Authorization, we’re going to leave the type as **Inherit auth from parent**. Click on the three dots next to the collection and select **Edit**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-edit-collection.jpg)

Here, we’re going to do the same exact thing we did with the first request but on the Collection configuration. Select the **Authorization** tab, under type select **Bearer Token**, and in the **Token** field again paste your token.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-add-authorization-api-key-token-to-collection.jpg)

Finally, click **Update** and hit the blue **Send** button again and we can see a successful request!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-authorized-request-inherit-token-from-parent.jpg)

We can now go back to our All Movies request and update the Authorization to use a Type of Inherit auth from parent and it should still continue to work!

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-successful-request-lord-of-the-rings-api.jpg)

## What else can we do with Postman?

While I covered a lot of the basics, there’s quite a lot more you can do with Postman. Here are a few of my favorites.

### Environment Variables

If you’re working as a developer on a project, it’s likely that your team uses multiple environments, such as a development and production environment. Instead of creating and maintaining completely separate requests, you can add an environment variable and instead change that variable when switching between environments!

Variables apply to many scenarios, but that’s a common use. Check out Postman’s docs to learn how.

[https://learning.postman.com/docs/postman/variables-and-environments/variables/](https://learning.postman.com/docs/postman/variables-and-environments/variables/)

### Import and Export Collections and Data

A great thing about Postman is once you have your requests all organized, you can export them for others to use. This also means that you can import collections from other team members. This makes it much easier to make sure everyone’s using the same collection.

Bonus: you can even store these files in a Git repository, as they’re just JSON.

But keep in mind - if you’re using Authorization on the collection like we went over in this guide, you’ll want to make sure you don’t include that when exporting your collection.

[https://learning.postman.com/docs/postman/collections/importing-and-exporting-data/](https://learning.postman.com/docs/postman/collections/importing-and-exporting-data/)

### Automated testing

Once you have a set of requests in a collection and even better, if you’re storing them in Github, you can begin to use those requests as part of a way to manage automated testing of your API.

While there are a few solutions for doing this, Postman includes a Collection runner built right into the app and [Newman](https://learning.postman.com/docs/postman/collection-runs/command-line-integration-with-newman/) is a command line tool that lets you run tests right from the terminal.

[https://www.postman.com/use-cases/api-testing-automation/](https://www.postman.com/use-cases/api-testing-automation/)

## What’s your favorite way to test and play with APIs?

[Share with me on Twitter!](https://twitter.com/colbyfayock)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?️ Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

