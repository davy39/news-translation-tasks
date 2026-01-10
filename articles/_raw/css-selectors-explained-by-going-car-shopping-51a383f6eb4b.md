---
title: CSS Selectors Explained By Going Car Shopping
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-21T06:07:05.000Z'
originalURL: https://freecodecamp.org/news/css-selectors-explained-by-going-car-shopping-51a383f6eb4b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EQ87S6jXZiyDzCVQMJ6mPw.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kevin Kononenko

  If you have ever seen a car dealership, then you can understand CSS selectors.

  When you step onto the lot of a car dealership, you’re instantly surrounded by different
  cars, colors, and years.

  And of course there’s that aggressive ...'
---

By Kevin Kononenko

#### If you have ever seen a car dealership, then you can understand CSS selectors.

When you step onto the lot of a car dealership, you’re instantly surrounded by different cars, colors, and years.

And of course there’s that aggressive salesperson. But let’s leave them out this simulation.

Cars — and car features — can be categorized using the same system as CSS selectors. So if you can understand the different ways to segment cars in a dealership lot, he market, then you can understand CSS selectors.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lwrVtbNNgHdeYnat-UtaKg.png)

Let’s start off by imaging a car dealership, using HTML:

Now we’re going to cover four different ways of styling your HTML elements:

1. By the type of element i.e. <div>
2. By class, i.e. ‘blue’
3. By id, i.e. ‘123xyz’
4. By relationship to other elements

#### By Type of Element

In our HTML above, every <div> is really a car of some sort. It could be a sedan, truck, or a convertible. But those are just variations of cars.

If we wanted to add styling to every car, we would have to think about the things that every car on this lot has in common.

Here’s some example CSS:

All right, I’m making this basic to start, OK? And yes, I made up some CSS properties to make this work.

Anyway, it would be fair to say that every car in this lot is made of steel, has 4 wheels, and has a maximum height of 9 feet. So every time we add a <div> to our HTML, it will have these properties by default.

In fact, we can take this car concept even further. We can break up the interior of the car into HTML as well:

What are some properties that the seats and windows might have? They must be shared by all windows and seats! We’ll do a deep dive on this later in this article.

#### Using Class

Check out our first HTML snippet, which covers all of the cars on the lot. You can see that each car <div> has a series of classes. These classes are used to assign common properties to all class members.

Let’s say we’re assigning the class ‘2005’ to different sedans, trucks, and convertibles. Well, what’s one trait that many cars had in common in 2005? CD players! So let’s do that in pseudo-CSS.

What if we have the class “crewCab”? Trucks with crew cabs have 2 rows of seats, with 5 seats total. So, we might want to assign this class specifically to trucks. We can combine classes by stringing them together.

Classes are a more specific way to reference HTML elements. So, let’s say that all vehicles are made of steel, by default. But you want some vehicles to be made of aluminum. You can create an “aluminum” class that will override the material property of all members of the class.

#### Using ID

HTML elements can have an ID. This is the most specific way to reference a single element, and it overrides all other styles. This unique identifier is kind of like the element’s license plate.

![Image](https://cdn-media-1.freecodecamp.org/images/1*U76THFEJoQcBTmFzX7MYUA.png)

So let’s say you have one car and it has the license plate “123 XYZ”. This car has a unique purple color, because for some reason the owner demanded it. Here is that one element in CSS.

Elements have a 1-to-1 relationship with IDs. Just like with cars and license plates, no two cars can have the same license plate. This is also the most powerful way to identify an element, so you can create unique exceptions to all other rules that an element should be obeying.

#### Relationships Between Elements

Let’s say you want to make sure that cars with the “leatherSeats” class have seats made out of leather. Check out the second HTML snippet from the “Type of Element” section.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jcGxiBfdyRy1t7mr4mlrOg.png)

You could have also given each <div> with class “seat” the class “leather” as well. But here’s the thing: that wouldn’t allow you to select just the cars with leather seats as a whole. You would only be able to select the seats themselves.

So, we want to give the entire car a “leatherSeats” class to make sure we can select the whole <div> and its children.

The CSS above will select all elements with class “seat” within a “leatherSeats” container.

Now let’s say you want to make sure that the front passenger seat has seat warmers. You can use the “~” selector, which is known as the sibling selector. It allows you to assign styles to elements relative to their neighbors.

So you can say:

Here’s one last example. Let’s say one particular make and model had a bizarre, random feature. For example, a 2008 Chevy truck might have had DVD players in the back seats.

Here’s how you would turn that into CSS:

1. You need to start with multiple classes, since this is a highly specific type of car. This might be “div.truck.chevy.year2008”.
2. Then, think about how you will be able to select the back seats, specifically. You could give the row an extra class, like “.backRow”. Or, you could use the [:last-child selector](http://www.w3schools.com/cssref/css_selectors.asp).
3. Finally, you need to select the seats themselves.

Answer:

If you enjoyed this post, you may also enjoy my [other explanations](https://www.rtfmanual.io/guides/) of challenging CSS and JavaScript topics, such as positioning, Model-View-Controller, and callbacks.

And if you think this might help other people in the same position as you, give it a “heart”!

