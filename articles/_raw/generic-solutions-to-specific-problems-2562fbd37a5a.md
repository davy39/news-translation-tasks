---
title: 'Generic solutions to specific problems: when to write some code and when to
  just do it'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-19T03:58:37.000Z'
originalURL: https://freecodecamp.org/news/generic-solutions-to-specific-problems-2562fbd37a5a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0BIInBkbvWUbf2j1krD2Iw.jpeg
tags:
- name: Design
  slug: design
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Rina Artstain

  There is a traditional story that tells of a rabbi who comes upon a guy sitting
  next to a fork in the road. The rabbi asks the guy which way is best to get to the
  city, and the guy answers: That one is a short road which is long, and...'
---

By Rina Artstain

There is a traditional story that tells of a rabbi who comes upon a guy sitting next to a fork in the road. The rabbi asks the guy which way is best to get to the city, and the guy answers: That one is a short road which is long, and the other is a long road which is short. The rabbi chooses the short road, but soon arrives at a field full of thorns which he can’t get through, and must turn back and take the other road, which actually leads him to the city.

The moral of the story, other than wondering if this guy was the first troll in history, is that sometimes trying to take a short cut will end up being longer than just doing it the long way.

### Coding the Long Way (which is Short)

If you’re specifically writing an API or a library for internal or external use, you know that it should be as generic as possible. You want it to be clear, concise and easy to use, while still giving your users a lot of flexibility. There are trade-offs between those goals, but you’ll figure them out.

But what happens when you’re given a specific task to complete, and you can either just do it, or write some infrastructure which will make just doing it easier in the future?

Should you get the task done as quickly as possible or spend the time to build some infrastructure which will make future tasks easier to complete?

Should you choose the short road which might turn out to be long, or the long road which will actually help you hit your target sooner?

### An example (based on a true story)

(Some of the details have been changed or omitted for simplicity, and, well, better story telling. Reality is much too messy.)

One day, my boss comes up to me and asks me to quickly get some data from the DB and send it to him as an excel sheet. It wasn’t too complicated, so I did it right away.

The next day he asks for the same data again, with different dates. He thinks for a bit and says, well — maybe you should just put this report up on the web. I’d like to be able to access this data any time and choose the dates myself.

No problem! Here you go, some front-end, some back-end, deploy. Wait. Wait. Wait. Deployment done, and the report is online.

A couple of days go by, and I’m asked for another quick report, and “do it with that nice interface and date filters you gave us last time”. OK, sure. No problem. Front-end, back-end, deploy, wait, online.

Next time I got a similar request I said: “Look, it will take me half a day to write this report, but if you give me two days, I can build some infrastructure which will allow me to define a query in the DB, add some configuration, and your report will be live without having to wait for deployment”. My request was approved.

#### **Here’s what I did with my two days:**

I defined a convention for a “report” stored procedure, which expected to get the following parameters:

* From Date
* To Date
* Start At Index (for paging)

Each procedure returned a result set for the query, and the Total Result Count (for paging).

In addition, I added a Reports table which held:

* Stored Procedure Name (to execute)
* Title (of the report)
* Description (to be displayed on the report page)

I also added an endpoint on the server, UI, and some logic to:

* Check the DB for reports and add them to the site navigation.
* When a report was accessed, execute the matching stored procedure and return the result to the UI.
* Display two date pickers for selecting From Date and End Date and executing the query.
* A generic table to display the results formatted according to the data type of each column. (I already had a generic UI component for paging, yay me!)

When I was done, I could add a stored procedure and an entry in the DB and the report would automagically appear on our site.

### The Only Constant is Change

Everyone was happy and super excited about my time saving report feature, but… What about sorting? And could we have the first column link to the customer’s profile? And could we maybe add filtering by the sales rep responsible for that customer?

Yeah! Sure. That makes a lot of sense. So I added:

* Optional Sort By and Sort Direction parameters to the Stored Procedures.
* A flag for specifying if the first column should link to the customer’s profile.
* Another flag for specifying if the query included filtering by sales rep.
* And a few UI/logic changes to support displaying/executing these new requirements.

Happy happy, joy joy. But… How about grouping the results? And when you click the row could you have an email sent to a group of predefined users? And when a sales rep enters the report, could you have the report displayed in their favorite color? (OK, I made that last one up)

#### Hold your Horses

At this point, I had to stop and think which features should be implemented as part of my generic solution, and which should be developed as a stand-alone solution.

It was obvious to me that specific custom actions which don’t depend on the actual data returned from the query (like sending an email to certain predefined users) was out of the question.

I also thought that uncommon actions which depend on the data returned by the query shouldn’t be added to the generic report infrastructure. So, filter by sales rep — sure, why not. Link to customer — OK, common scenario. But other actions which are very specific to a single report — nope.

The grouping requirement posed more of a challenge: Grouping is a common and extremely useful scenario. Should I add it to my infrastructure or not?

Well, what would grouping the results require?

* Adding a Group By flag to the report’s DB entry, to let the logic know to expect two distinct result sets — group header and group details.
* The logic would also have to know how to match the group to the details, and it would have to be done by convention. Extremely risky business.
* Figuring out how to generically sort results with a group header. I can’t even.
* And probably some other issues I haven’t thought of.

### The Code Not Written

I didn’t add grouping.

In retrospect, putting about a week of effort total into this reports feature saved me hundreds of hours developing reports later on. I also managed to avoid the pitfall of trying to be too generic and supporting too much extraneous **stuff,** which would have hurt the system’s stability in the long run.

But really, I shouldn’t have written a single line of code. I should have looked into a reporting tool.

However, there are other generic helper systems which I wrote which were a good investment and **should** have been written. For example, a library of helpers which create HTML elements with predictable ids and classes tailored to our data models and UI requirements.

### Now What?

So how should you decide whether to write some infrastructure or just do it? Here’s how I decide:

* Is it a rote task? If it’s boring and recurring, if you find yourself copy-pasting a whole lot of code often — check if you can generalize what you’re doing and build some code to do it for you.
* How long will building the infrastructure take? If you can build the infrastructure in 5 minutes and each task would have taken you 5 days, it’s an easy answer. If building the infrastructure would take a year and each task would take 5 minutes — don’t build it. But it’s usually not that clear cut. Try to estimate as best you can, try to keep it simple, and be prepared to cut your losses if it takes too long.
* Do not add specific implementations to your generic solution. If it doesn’t fit, don’t try to force it. You’ll end up ruining your infrastructure and getting a mediocre result for the task you were actually trying to complete.
* But first, **please** check if there is ready made solution to your problem.

Like what you read? Share the love by clapping. Have a question or comment? Let me know in the comments section.

