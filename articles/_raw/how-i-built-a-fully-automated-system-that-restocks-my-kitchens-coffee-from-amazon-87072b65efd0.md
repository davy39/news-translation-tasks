---
title: How I built a fully-automated system that restocks my kitchen’s coffee from
  Amazon
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-28T23:59:46.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-fully-automated-system-that-restocks-my-kitchens-coffee-from-amazon-87072b65efd0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0CIKiBzkfud1zF3g9btnQQ.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: Raspberry Pi
  slug: raspberry-pi
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Terren Peterson

  I’ve perfected a method over the years for preparing for a grocery store run. I
  carefully open up the fridge and scan through it several times, letting out most
  of the cold air.


  I then do a similar exercise with a few other cabine...'
---

By Terren Peterson

I’ve perfected a method over the years for preparing for a grocery store run. I carefully open up the fridge and scan through it several times, letting out most of the cold air.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BhwVxeex2ZzHlnyFkQOhNw.jpeg)

I then do a similar exercise with a few other cabinets in the kitchen. Then I scribble down all the items I need on a piece of paper.

Even though I’ve tried different mobile apps in an effort get more organized, I have yet to improve upon this simple paper method.

Given that I love technology, I’m convinced there’s a better way to stock my shelves, but haven’t seen the right solution yet. I do like the convenience around online shopping from Amazon, but there’s still a lag in the fulfillment that requires more planning than I’m capable of.

That’s when I got to thinking: perhaps the solution lies in better monitoring of inventory. And so I’ve set out in this direction.

Since my household drinks a lot of coffee, and there’s a great selection available online, I decided to start there.

As part of a [Hackster](https://www.freecodecamp.org/news/how-i-built-a-fully-automated-system-that-restocks-my-kitchens-coffee-from-amazon-87072b65efd0/undefined) competition, I got really motivated to take this from a concept to code, and fully automate the fulfillment of my coffee bean supply straight to my home. A detailed writeup of my entire solution can be found [here](https://www.hackster.io/terren/javawatch-your-coffee-bean-guardian-807ef7), with a summary below.

### Amazon Dash Replenishment Service

One of the many new technology products that Amazon has released is called Dash. Here’s a picture of a programmable one called a Dash Button, and they also sell ones that are already set to order products from their website, like soap detergent, batteries, chips, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6-jdNVlWrhEY7PzANef-Cw.png)

The same technology that goes into these buttons can be built into hardware natively. This enables replacing a button with other stimuli that can request a product to be ordered. So after some great brainstorming, here’s the pitch that I came up with.

### How to make it all work

So after coming up with a catchy name, and creative concept, I sketched out an architecture on how this was going to work. In between the Raspberry Pi based hardware device and the Dash Replenishment API’s, I added the [Amazon Rekognition Service](https://aws.amazon.com/rekognition/) that was launched a few months ago. Here’s how all of the pieces fit together.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FiHh8kf3et_s0kpOKfEcgQ.png)

### Leveraging Artificial Intelligence in the Kitchen

The key to the keeping the coffee beans supplied relied on leveraging the image recognition abilities from AWS. I’ve seen some great use cases for this technology for facial recognition, but perhaps I am the first one to be taking photos of coffee beans.

The service was straight forward to get working. The Raspberry Pi Camera captures and uploads photos on preset intervals to the object based storage service by AWS called S3. Each photo object gets a unique address, and a call to the Rekognition API is made passing this address so that the AI can be applied. As an example, here’s an actual picture taken by the device of a full jar of beans.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HGR6Ouwr6SsxCO4_5-jnCQ.jpeg)

What comes back in the response is an array of “labels” — think of these as predictions on what is in the field of view for the image.

```
{    “Labels”: [        { “Confidence”: 84.64501190185547, “Name”: “Bottle”,        { “Confidence”: 84.64501190185547, “Name”: “Jug”,        { “Confidence”: 84.64501190185547, “Name”: “Water Bottle”,        { “Confidence”: 80.86704254150390, “Name”: “Jar”,        { “Confidence”: 73.33070373535156, “Name”: “Bean”,        { “Confidence”: 73.33070373535156, “Name”: “Produce”,        { “Confidence”: 73.33070373535156, “Name”: “Vegetable”    ],    “OrientationCorrection”: “ROTATE_0”}
```

I was in luck that the AI does register a “Bean” label, and in this photo predicted at 73% certainty that it was in the image. It also came back with many other assertions that were correct (yes it is also a bottle, and might be produce?) but aren’t relevant to what I am looking for.

So what happens when the coffee bean supply goes nearly empty? Here’s what the image that the Raspberry Pi captured from my kitchen when that occurred.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y39h4fIrhvZvEXHduRhEVA.jpeg)

And here are the labels that the AI came back with as a response.

```
{    “Labels”: [        { “Confidence”: 94.05787658691406, “Name”: “Bottle”,        { “Confidence”: 94.05787658691406, “Name”: “Jug”,        { “Confidence”: 94.05787658691406, “Name”: “Water Bottle”,        { “Confidence”: 80.77616882324219, “Name”: “Jar”,        { “Confidence”: 63.5648078918457, “Name”: “Alcohol”,        { “Confidence”: 63.5648078918457, “Name”: “Beer”,        { “Confidence”: 63.5648078918457, “Name”: “Beer Bottle”,        { “Confidence”: 63.5648078918457, “Name”: “Beverage”,        { “Confidence”: 63.5648078918457, “Name”: “Drink”    ],    “OrientationCorrection”: “ROTATE_0”}
```

It worked! The beans had disappeared from the field of vision, and no longer came back in the array. Parsing through the array gave me enough detail that I could then make an ordering decision to fill the jar back up.

### Which Coffee Should Amazon Send?

Determining which coffee Amazon should fulfill on was a separate task, and required setting up a simple website that allows registration of a device with Amazon. Below is a quick video that shows some screenshots of what the [site](http://javawatcher.com/) looks like, and how it plugs into the Amazon product catalog.

### Could it work for other Items?

Now once I got things working, I tested it out on a few other things laying around to see how good the AI was around the kitchen.

Ketchup (huge success — 98.6% recognition).

Sriracha (miss — 73.1% guess that it was a beverage).

Strawberries (another success — 85.4% recognition).

Blueberries (partial miss — closest was recognition of “Food” at 61.7%).

Eggs — top view of carton (total miss — 51.6% guess that it was a car bumper).

So there still is room to train the models, but a good start and seems reasonable that it isn’t specific to coffee beans.

### What’s Next?

After working with it for a while, I determined that I may have overcomplicated the solution. While I absolutely love building with Raspberry Pi’s, the next step in user experience is to build this as an App on smartphones, leveraging the camera capabilities already available in consumers pockets.

Making the solution totally portable would be a huge win and removes the cost for building and any hardware components. Most of the work in the solution is already powered in the Cloud, so it’s just a matter of how to get photos out to it. The Rekognition service is only a few months old, and if improving its models would encourage Amazon.com retail purchases, I’d bet it would get good fast!

