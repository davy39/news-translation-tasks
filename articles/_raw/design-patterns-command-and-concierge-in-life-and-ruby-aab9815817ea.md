---
title: 'Design Patterns: Command and Concierge in Life and Ruby'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-13T16:45:26.000Z'
originalURL: https://freecodecamp.org/news/design-patterns-command-and-concierge-in-life-and-ruby-aab9815817ea
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oHisJCqpKvA2G-t2st7PZw.png
tags:
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Sihui Huang

  The Command Pattern’s definition is a stressful one to look at. The formal definition
  is that it:


  encapsulates a request as an object

  thereby letting you parameterize other objects with different requests, queue or
  log requests, and s...'
---

By Sihui Huang

The Command Pattern’s definition is a stressful one to look at. The formal definition is that it:

* encapsulates a request as an object
* thereby letting you parameterize other objects with different requests, queue or log requests, and support undoable operations.

Let’s forget about it for a second and take a trip to Hawaii.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gaUs2oV-Mv6K5yTfY9GTfA.png)

And live in a luxury hotel.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SEPz2ulxuXpSC62G958ZQw.png)

We spent the day on the beach, scuba dived, and did some sightseeing. It’s time to get back to the hotel to chill, eat, and plan for the next day.

After getting back to the hotel, we want to:

1. Get room service for dinner
2. Get laundry service because we didn’t bring extra clothes
3. Get a travel guide for Kauai, the island we are going to tomorrow

We check out the hotel’s service menu and find three service items matching our needs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-zYwuRdFHA3oTs-076CAoQ.png)

We then call the front desk to place these three requests. A concierge picks up our call, writes down our list of requests, and acts on each service request as instructed by the service menu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7PbUyLZWcULve0IB2gnjkw.png)

Then each staff member executes according to each specific request:

1. The chef in the kitchen starts cooking
2. The cleaning department send a staff to our room to pick up our clothes
3. The staff in the lobby grabs a travel guide and delivers it to our room

Let’s recap what just happened.

a. We selected the services we wanted from the menu and submitted them to a concierge.

b. The concierge wrote these service requests down as a list.

c. After we hung up, instructed by the service menu, the concierge sent our requests to corresponding departments.

d. Each department executed on the given request.

### Let’s see the actions in Ruby.

1. We submitted these three requests to the concierge:

2. These requests went into a list the concierge keeps track of:

Let’s see that in action (console):

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gef7_F3B3AlSNPR8n-ESLw.png)

As we can see, after `we` submitted three requests, these requests were in a `request_list` taking care by `concierge`.

3. Instructed by the service menu, the concierge sent our requests to corresponding departments.

The code above should work fine.

Except for one thing….

It [smells](https://en.wikipedia.org/wiki/Code_smell) bad.

Specifically, the part where we have the switch cases:

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZURBU8cccrssu44O_cq64g.png)

Why does this part smell bad?

1. If the hotel offers twenty services, instead of three, the method will be really long.
2. We want to offer new services or remove an existing service. However, each time we have to open the `Concierge` class and redefine the `act_on_requests`method.

T**he method knows too much and requires frequent changes**. **Having these two combinations together is almost always a bad thing.**

Why?

A method that requires frequent changes is a method you need to update often. Each time you update a piece of code is an opportunity to introduce new bugs to the system.

When the method also knows a ton — and it’s long — the chances of messing it up when updating increases significantly. That’s the reasoning behind [a design principle we talked about earlier](http://www.sihui.io/design-pattern-factory/) — **encapsulate what varies.**

### Time to Refactor!

There must be a better way than this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZOZwUbQ4qOP118ZuichbMw.png)

Take a closer look and think about it.

Let’s rephrase what the code is doing in English. We loop through the requests on the request list. For each request, according to its service type, we give the corresponding department related data and execute the request. Essentially, we loop through the requests and execute each of them accordingly.

But what if each request actually knew how to execute itself?

Then the method can be as simple as:

![Image](https://cdn-media-1.freecodecamp.org/images/1*qjmwlq83eoCo144JeexHzQ.png)

Instead of letting the `act_on_requests` method decide how each request should be handled, we distribute that responsibility and knowledge back to each request and let it decide how to itself should be handled.

With that being said, our requests could look like this:

And the updated `Concierge` will look like:

With the updated codes, here is how we, customers of the hotel, send requests to the concierge.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xNsFb62V7sOPCR5bvZJR5g.png)

It is pretty easy to create another service.

For example, the hotel also allows us to reserve SPA:

The service not only supports `execute` (making a spa reservation) but also `undo` (canceling the reservation).

Let’s say the hotel also provides another way to request services without having to call the concierge — a service requesting panel:

![Image](https://cdn-media-1.freecodecamp.org/images/1*khdqlv3l_ETG3JW92J9nPw.png)

We can just press the button and the service with a default setting will be delivered to our room.

Here is the code for the `ServicePanel`:

And here is how we can create a service panel:

![Image](https://cdn-media-1.freecodecamp.org/images/1*t3qn7WWidvn44W51A5sNlw.png)

### ??We are now using the Command Pattern!??

Let’s revisit the definition of the Command Pattern. It:

* encapsulates a request as an object
* thereby letting you parameterize other objects with different requests, queue or log requests, and support undoable operations.

> 1. “encapsulates a request as an object”

Each of the services classes we created, `RoomService`, `LaundryService`, `TripPlanningService`, and `SpaReservationService`, is an example of encapsulating a request as an object.

Recap:

![Image](https://cdn-media-1.freecodecamp.org/images/1*KN9SLCFu_m0cjse4CcnuGQ.png)

> 2. “thereby letting you parameterize other objects with different requests,”

The `ServicePanel` is an example of parameterizing an object with different requests.

Recap:

![Image](https://cdn-media-1.freecodecamp.org/images/1*56FeG3eKTst6X73DgFFj0A.png)

> 3. “queue or log requests,”

Our requests were queued while the concierge was taking them over the phone.

Recap:

![Image](https://cdn-media-1.freecodecamp.org/images/1*wCjFrqn2HZiShOzRr70giQ.png)

> 4. and support undoable operations.

`SpaReservationService` supports `undo`.

Recap:

![Image](https://cdn-media-1.freecodecamp.org/images/1*8bQzLGARIgIMCze913npDA.png)

Thanks for reading!

Don’t forget to subscribe. :D

This was originally published on my blog, [Design patterns in life and Ruby](http://www.sihui.io/design-patterns/).

