---
title: 'The Hitchhiker’s Guide to React Router v4: the hidden value of route config'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-15T14:23:26.000Z'
originalURL: https://freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-c98c39892399
coverImage: https://cdn-media-1.freecodecamp.org/images/0*hkvZOkK2Y-HTKLCI
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Eduardo Vedes

  Welcome to the Hitchhiker’s Guide to React Router v4, Part IV!

  Now that we’ve learned about recursive routes, let’s get back to our initial boilerplate,
  to avoid mixing concerns, and learn how to create a route configuration array.

  S...'
---

By Eduardo Vedes

Welcome to the Hitchhiker’s Guide to React Router v4, Part IV!

Now that we’ve learned about recursive routes, let’s get back to our initial boilerplate, to avoid mixing concerns, and learn how to create a route configuration array.

So, just to recap a bit what we did in the beginning, let’s take a look at our initial **routes.js** file:

![Image](https://cdn-media-1.freecodecamp.org/images/uweHGbrLczGHKPDEXVe34FNAOo5OTMW32bbv)
_**routes.js (initial file)**_

Our **Routes** component is returning a **div** with a **NavBar** and a **Switch** where we’ve defined all the routes of our App.

Our first step in this Part 4 will be to define a routes array.

### Routes Array

![Image](https://cdn-media-1.freecodecamp.org/images/AfI92QlBlYm6ovQJGTLD9XjyaO0pdNKJUSuk)
_**routes config array**_

I’ve taken a look at our routes and created this array that defines each route and sub-route we had in our application.

Nice! Now what?!? ?

### Refactor the Old Hardcoded Routes

Now let’s clean our hardcoded routes and the Switch!

![Image](https://cdn-media-1.freecodecamp.org/images/eGOQoXHqYMhhKHus0C0YcGdUR6Rygv7J40XV)
_**improved Routes component**_

Yeah! Goodbye all those lines of code. What are we really doing?

Well, we’re mapping over the map array using an ES6 (fat arrow) callback to return an abstract component called **<MakeRouteWithSubRoutes />**. We are passing into it a key (just for React indexing purposes) and we are spreading the route info also into it.

#### <MakeRouteWitheSubRoutes /> Component

In the meantime, we need to create that component. I’ve decided to create it apart and import it into the **routes.js** file.

![Image](https://cdn-media-1.freecodecamp.org/images/q6WgEVi9gJUXYvyQEJklbude-zcMB5nhNDya)
_**MakeRouteWithSubRoutes Component**_

Okay, this **<MakeRouteWithSubRoutes/>** Component is picking up each route you pass into it and returning a React Router **<Route/>** Component.

As props, we have the **path** and the render method, which will invoke the **route.component** you want to render (then passing into it the spread props and the sub-routes that it needs to know).

This routes are coming from the route config array — got it? Nice! ?

#### TopicList (Sub-Routing)

This being said, let’s take a loot at the **TopicList** component because it’s the one receiving sub-routes from the route config array:

![Image](https://cdn-media-1.freecodecamp.org/images/VZQlFJucdpf7VnVtnpsPgxPxz23EoeOxc2cI)
_**TopicList Component with sub-routing**_

So, what’s happening here? Our **TopicList** now is importing the **<MakeRouteWithSubRoutes/>** component and reusing with routes it has received.

It also does a **routes.map** over the sub-routes and repeats the process done in the **routes.js** file.

Take a minute to understand it and play with it!

#### More and More Sub-Routing

As you can see, this works quite well. It’s abstracted, there’s separation of concerns. The **<MakeRoutesWithSubRoutes/>** is a quite easy to use stateless component or function which doesn’t care about the routing content. It just routes whatever you feed to it.

What if we wanted to do more sub-routing?

Easy peasy! Just keep growing or redesigning your routes configuration array!

![Image](https://cdn-media-1.freecodecamp.org/images/masX7pCVdt9vELBX-3d74HMYz1D9W4FJ5sif)
_**dynamic routes config array**_

See? The routes of the **/Topics/:topicId** could simply be an array like its parent routes. But I’ve decided to do better and invoke a function that calls an API and returns a new array of routes (just imagine it fetches the API ?).

So how can we check that in the App?

Let’s put a **console.log** inside the **TopicDetail** component and check what it is receiving:

![Image](https://cdn-media-1.freecodecamp.org/images/tnagiA612FCg0Nc6-9Cp2eFRoKoH657lRPaa)

I’m invoking **routes()** in **console.log** because now this sub-route is a function! Remember? All good! ?

![Image](https://cdn-media-1.freecodecamp.org/images/ACsSVAt8jg--jGIR993-N0njgW4nndEuTiCv)
_console.log(routes())_

Yeah Ma! We’ve done it! We’re receiving the routes dynamically and propagating those into our sub-routes and components. This is so great!

### NoMatch And Ambiguous Routes

Wait! Where’s our **NoMatch** Component?

Okay, let’s introduce it into our route config array:

![Image](https://cdn-media-1.freecodecamp.org/images/nmr0AktuM0RDiaOowU0xlylfkBuGUtxn-pT9)

Observe that **:WhereTheHeckIsThat** is a variable because it has the colon before it.

What should we expect?

Let’s see it in action:

![Image](https://cdn-media-1.freecodecamp.org/images/IoGOuriU8ZoTVqmrnwWef3nBO-Y-PRpduHxy)

Wow! As a matter of fact it’s rendering the **NoMatch** but it’s also rendering the **Home View**. Why?

Well, what’s happening is that in our initial boilerplate we had a **<Switch />** that was picking up the first **<Route />** that matches the path remember?

So now, as we do not have the switch, it can match more than one path at a time!

These are called Ambiguous Routes. Router matched the **/Home** and at the same time **/:WhereTheHeckIsThat** because it’s kind of a wildcard that accepts everything.

How to we correct that?

Simple: grab **<Switch />** back!

![Image](https://cdn-media-1.freecodecamp.org/images/kHsKnL4TduMHuJHwGmGcz-91I2wSsoCwAY-L)
_**&lt;Switch /&gt; is back to wrap our route.map!**_

![Image](https://cdn-media-1.freecodecamp.org/images/rKSsmATtmMNYywVeLz9U4RVeRUhZjp2Obtd2)
_**Home component was the only match**_

![Image](https://cdn-media-1.freecodecamp.org/images/B1QStJLEuT8-FT-i3dQk9wTybnppVKfjH3hR)
_**Unknown paths trigger NoMatch component**_

As you can see above, now the **/Home** is rendered alone, because **<Switch />** found it and returned it immediately.

If you put some unknown path in the URL, it triggers the **:/WhereTheHeckIsThat** and renders the **NoMatch** component as a default.

Great job! Everything is working as we’d expected and now we have a **powerful route array configuration** which allows us to have a lot of flexibility.

This really is the hidden value of having an abstraction and defining a route configuration array!

### Last but not least

This is the end of the Hitchhiker’s Guide To React Router v4.0!

There is still are some stuff to pay attention to, but I prefer to let you deep dive a little bit in the boilerplates we’ve built and look for what you need in the React router [website](https://reacttraining.com/react-router/web/guides/philosophy).

I had so much fun doing this Guide that I think I’m going to start writing more and more :)

It was good not only because I was able to teach you something but also because I’ve also learned a lot in this process.

#### GitHub Repo



The changes I’ve made to the application, to produce this article, can be found in my GitHub [repo](https://github.com/evedes/ReactRouter_BoilerPlate_04) for Part 4.

#### Bibliography



To make this article I’ve used the React Router documentation that you can find [here](https://reacttraining.com/react-router/core/guides/philosophy).

All the other sites I’ve used are linked along the document to add info or provide context to what I’ve tried to explain to you.

This article is part 4 of a series called “Hitchhiker’s Guide to React Router v4”

* **[Part I: Grok React Router in 20minutes](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-a957c6a5aa18/)**
* **[Part II: [match, location, history] — your best friends!](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-a957c6a5aa18/)**
* **[Part III: recursive paths, to the infinity and beyond!](https://www.freecodecamp.org/news/hitchhikers-guide-to-react-router-v4-21c99a878bf8/)**

? Thank you very much!

