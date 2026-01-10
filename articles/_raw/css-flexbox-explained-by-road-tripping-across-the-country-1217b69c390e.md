---
title: CSS Flexbox Explained by Road Tripping Across the Country
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-22T05:34:28.000Z'
originalURL: https://freecodecamp.org/news/css-flexbox-explained-by-road-tripping-across-the-country-1217b69c390e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kwaAOW_ja_raNVgV3VgZ2g.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Kevin Kononenko

  If you have ever been on a long roadtrip, then you can understand CSS Flexbox!

  The popular Flexbox model attempts to replace the giant pain known as CSS “floats”.
  Unfortunately, it also introduces yet another entirely new system in...'
---

By Kevin Kononenko

#### If you have ever been on a long roadtrip, then you can understand CSS Flexbox!

The popular Flexbox model attempts to replace the giant pain known as CSS “[floats](https://medium.freecodecamp.com/css-floats-explained-by-riding-an-escalator-57fa55232333)”. Unfortunately, it also introduces yet another entirely new system into CSS. And you thought there were enough already!

Actually, the grid-oriented nature of Flexbox makes much more sense than constantly juggling your “float” and “block/inline-block” values.

There are already a couple good resources out there, like [Flexbox Tower Defense](http://www.flexboxdefense.com/) and this [more technical guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/).

In this article, I’ll take the route of explaining the Flexbox system through one of my favorite types of vacations… the road trip!

That’s right — we’re going to use the entire United States in this analogy.

The US actually has a grid-oriented interstate highway system that spans East-West and North-South.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dvFENsh3hvfWUw4Y6ahXfA.png)

While this map is geographically accurate, it’s pretty hard to understand. So let’s try that again.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Qqg_4ini5SyEszW8kQByqA.jpeg)
_[https://betterexplained.com/articles/highway-math/](https://betterexplained.com/articles/highway-math/" rel="noopener" target="_blank" title=")_

In this scenario, **you must primarily travel along a one-directional path**.

For example, you might take the route from Seattle to Boston which only includes west to east. Or, you might take the route from Seattle to San Diego, which only covers north to south.

Since the default position is top left, we’ll start from Seattle. You’ll get a chance to add side trips to your road trip towards the end! This is important because it imitates the flow of <div>s within their container.

Let’s hit the road!

### flex-direction: The direction of your trip

Flex-direction determines the direction of elements within a container <div> with “display:flex;”. The default value is “row”, which means from left to right. No surprises there.

Let’s say you’re starting in Seattle, and taking a trip to Boston. That trip might look like this in HTML:

This assumes that you’re making stops at Yellowstone, Mount Rushmore and Chicago. Here is a timeline view, assuming you stop for 2 days at each location.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MHr0lF_nWdUim0T1duN81A.png)

And what if you are using “flex-direction:column;”? That means that your <div>s will align from top to bottom. Now, you’re going from Seattle to San Diego. Stops along the way might be Portland, San Francisco and Los Angeles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9k1NlSDqmYG46zb_nc49oQ.png)

### justify-content: How you space your stops along the trip

Alright, let’s return to the Seattle to Boston trip. With Flexbox, we can decide how our child <div>s spread out along the width of the container. So, if you are on a road trip, you may not necessarily evenly space out your stops. You might stop more frequently at the beginning, or at the end.

The default value for justify-content is “_flex-start_”, which means your <div>s spread from the left-most side. This is similar to choosing to do all of your stops on the roadtrip at the beginning. This would include places like Glacier National Park, Yellowstone and Mount Rushmore.

On a map:

![Image](https://cdn-media-1.freecodecamp.org/images/1*hsukM2jd3rHpnMZe77R0SQ.png)

Okay, this is admittedly a little unrealistic. You probably would not want to drive 20 hours from South Dakota straight to Boston. The same could be said of “_flex-end_”, when all of the <div>s hug the right side of the container. This would include stops at places like the wonderful city of Cleveland, Niagara Falls and the MLB Hall of Fame.

On map:

![Image](https://cdn-media-1.freecodecamp.org/images/1*UqTFioPsD_oGuGSR04u22w.png)

Another example is “_center_”, where the <div>s align themselves to the middle of the container <div>. That would mean visits to Mount Rushmore, the Mall of America in Minnesota and Chicago.

### align-items: Which highway do you want to take across the country?

Alright, so far we have mainly been discussing the northern route across the country. In HTML terms, that means we are just going along the top of the <div>. But, one magical property of Flexbox is that we can easily move to the middle or bottom of the <div> without any CSS trickery.

The align-items property defaults to “flex-start”, but if we change that to “_center_”, our <div>s will vertically align to the center of the container. This is kind of like starting your road trip in San Francisco, heading over to Las Vegas, then Denver, then St. Louis and ending in Washington D.C.

Here’s the map:

![Image](https://cdn-media-1.freecodecamp.org/images/1*v8ihdtN84aFfEu5rMlCrXw.png)

And, in HTML:

If you wanted to set your align-items value to “_flex-end_”, your <div>s would align to the bottom of the container. You would be taking the southern route across the United States, and stopping in places like Sedona, Austin and New Orleans before ending in Jacksonville.

### align-self: Have one stop on a different highway route

You can apply “align-self” to individual child <div>s in order to have them move vertically within the container, regardless of the align-items property. So if you are taking the trip from Seattle to Boston, you can make a stop in Las Vegas, which is in the middle of the country. Then you can continue on to Mount Rushmore or wherever else on the normal horizontal flow.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MktBw1O06Ka2hyx94qaC3g.png)

### order: Make your stops in a specific order

So far, every stop has corresponded with the order of the elements in the HTML. In other words, if the Mount Rushmore stop is specified third in the HTML, that means it will be the third stop on the road trip.

The “order” property is a numerical value that allows us to change the order of the HTML elements. Without Flexbox, we would need to use a confusing series of floats, or just change the HTML.

With “order”, we can turn around on our road trip and visit a place that is not on the way to the end point. Would you do this in real life? Only if you enjoy an extra 15 hours in the car!

Let’s say we’re taking the northern trip, Seattle to Boston. Here’s that HTML again.

But, after starting in Seattle, we want to first go to South Dakota for the world’s largest square dance festival. We would use the “order” property to make sure the Mount Rushmore visit comes right after Seattle.

Order defaults to 0, so we might want to give seattleVisit a value of -2, and mountRushmoreVisit a value of -1 to make sure it comes 2nd. Then the rest of the elements will follow in a normal flow.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qXT61u8PvoKDzOQhQVvH2A.png)

Notice — this is now strictly a timeline view, not using the geographic order as the other maps were using.

### Conclusion

Time for a little quiz! Here are some sample destinations, in HTML.

But, if the following is your planned route… what would the CSS need to look like?

* Start in San Francisco
* 2nd stop: Las Vegas
* 3rd Stop: Mount Rushmore
* 4th Stop: Backtrack to Denver
* End by driving all the way to Washington D.C

The answer:

Here’s the reasoning behind this:

* 4 out of 5 items are along our central route, so we “align-items” to _center._
* The three stops are generally in the middle of the United States from a West-East perspective, so we “justify-content_”_ to _center_ as well.
* Mount Rushmore is on the northern route, so we use _align-self_ on that one <div>.
* The _order_ CSS property is why we must backtrack to Denver, and why our actual trip does not follow the order of the children <div>s in the HTML. Order allows us to change the sequence of <div>s. In this case, we move Denver to the second to last stop, so we must _give_ it an order greater than 0, but less than the order of the final <div> so that we still end in D.C.

If you enjoyed this post, you may also enjoy my [other explanations](https://www.rtfmanual.io/guides/) of challenging CSS and JavaScript topics, such as positioning, Model-View-Controller, and callbacks.

And if you think this might help other people in the same position as you, give it a “heart”!

