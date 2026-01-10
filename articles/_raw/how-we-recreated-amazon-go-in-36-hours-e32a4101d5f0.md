---
title: How we recreated Amazon Go in 36 hours
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T20:57:41.000Z'
originalURL: https://freecodecamp.org/news/how-we-recreated-amazon-go-in-36-hours-e32a4101d5f0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*FR4dUJjxG1v5cV66.
tags:
- name: Android
  slug: android
- name: Future
  slug: future
- name: iot
  slug: iot
- name: software
  slug: software
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Subhan Nadeem

  My colleagues and I wanted to create something that would make people go “wow” at
  our latest hackathon.

  Because imitation is the sincerest form of flattery and IoT is incredibly fun to
  work with, we decided to create our own version ...'
---

By Subhan Nadeem

My colleagues and I wanted to create something that would make people go “wow” at our latest hackathon.

Because imitation is the sincerest form of flattery and IoT is incredibly fun to work with, we decided to create our own version of Amazon Go.

Before I explain what it took to make this, here’s the 3 minute demo of what we built!

There were four of us. [Ruslan](https://www.freecodecamp.org/news/how-we-recreated-amazon-go-in-36-hours-e32a4101d5f0/undefined), a great full-stack developer who had experience working with Python. John, an amazing iOS developer. Soheil, another great full-stack developer who had experience with Raspberry Pi. And finally, there was me, on the tail end of an Android developer internship.

I quickly realized that there were a lot of moving parts to this project. Amazon Go works on the basis of real-time proximity sensors in conjunction with a real-time database of customers and their carts.

We also wanted to take things a step further and make the entry/exit experience seamless. We wanted to let people enter and exit the store without needing to tap their phones.

In order to engage users as a consumer-facing product, our app would need a well-crafted user interface, like the real Amazon Go.

On the day before the hackathon, I put together a pseudo-design doc outlining what we needed to do within the 36 hour deadline. I incorporated the strengths of our team and the equipment at hand. The full hastily assembled design doc can be seen below.

There were six main components to EZShop, our version of Amazon Go.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eTzUuujmvx3U3foEb_lNog.png)
_A quick diagram I whipped up visualizing the components of this project_

### The Kairos Facial Recognition API

The [Kairos facial recognition API](https://www.kairos.com/) was a fundamental component for us. It abstracted the ability to identify and store unique faces. It had two APIs that we used: `/enroll` and `/verify`.

`/enroll` is described as:

> Takes a photo, finds the faces within it, and stores the faces into a gallery you create.

We enrolled all new customers into a single “EZShop” gallery. A unique `face_id` attribute would be returned and stored with the customer’s registered name in our real-time database.

When we wanted to verify a potential customer’s image, we would POST it to the `/verify` endpoint. This would return the `face_id` with the highest probability of a match.

In a real-world implementation, it probably would have been a better idea to use a natively implemented facial recognition pipeline with TensorFlow instead of a network API. But given our time constraints, the API served us very well.

### **The Realtime Firebase Database**

The Firebase database was another fundamental piece to our puzzle. Every other component interacted with it in real time. Firebase allows customized change listeners to be created upon any data within the database. That feature, coupled with the easy set-up process, made it a no brainer to use.

The schema was incredibly simple. The database stored an array of items and an array of users. The following is an example JSON skeleton of our database:

```
{  "items": [    {      "item_id": 1,      "item_name": "Soylent",      "item_stock": 1,      "price": 10    }  ],  "users": [    {      "face_id": 1,      "name": "Subhan Nadeem",      "in_store": false,      "cart": [        1      ]    }  ]}
```

New users would be added to the array of users in our database after registering with the Kairos API. Upon entry or exit, the customer’s boolean `in_store` attribute would be updated, which would be reflected in the manager and personal app UIs.

Customers picking up an item would result in an updated item stock. Upon recognizing which customer picked up what item, the item’s ID would be added to the customer’s `cart` array.

I had planned for a cloud-hosted Node/Flask server that would route all activity from one device to another, but the team decided that it was much more efficient (although more hacky) for everybody to work directly upon the Firebase database.

### The Manager and Personal Customer Apps

John, being the iOS wizard that he is, finished these applications in the first 12 hours of the hackathon! He really excelled at designing user-friendly and accessible apps.

#### **The Manager App**

![Image](https://cdn-media-1.freecodecamp.org/images/1*-mxfk-c6IMhkviUW-91isw.png)

This iPad application registered new customers into our Kairos API and Firebase database. It also displayed all customers in the store and the inventory of store items. The ability to interact directly with the Firebase database and observe changes made to it (e.g. when a customer’s `in_store` attribute changes from `true` to `false`) made this a relatively painless process. The app was a great customer-facing addition to our demo.

#### The Personal Shopping App

![Image](https://cdn-media-1.freecodecamp.org/images/1*3kMsmAdlwvkbb7zfvppvsA.png)

Once the customer was registered, we would hand a phone with this app installed to the customer. They would log in with their face (Kairos would recognize and authenticate). Any updates to their cart would be shown on the phone instantly. Upon exiting the store, the customer would also receive a push notification on this phone stating the total amount they spent.

### The Item Rack, Sensors, and Camera

Soheil and Ruslan worked tirelessly for hours to perfect the design of the item shelf apparatus and the underlying Pi Python scripts.

![Image](https://cdn-media-1.freecodecamp.org/images/1*x8ClNraW0zWDkr4lMWcpIw.png)
_The item rack apparatus. Three items positioned in rows, a tower for the security camera, and ultrasonic sensors positioned at the rear_

There were three items positioned in rows. At the end of two rows, an ultrasonic proximity sensor was attached. We only had two ultrasonic sensors, so the third row had a light sensor under the items, which did not work as seamlessly. The ultrasonic sensors were connected to the Raspberry Pi that processed the readings of the distance from the next closest object via simple Python scripts (either the closest item or the end of the rack). The light sensor detected a “dark” or “light” state (dark if the item was on top of it, light otherwise).

When an item was lifted, the sensor’s reading would change and trigger an update to the item’s stock in the database. The camera (Android phone) positioned at the top of the tower would detect this change and attempt to recognize the customer picking up the item. The item would then instantly be added to that customer’s cart.

### Entrance and Exit Cameras

I opted to use Android phones as our facial recognition cameras, due to my relative expertise with Android and the easy coupling phones provide when taking images and processing them.

The phones were rigged on both sides of a camera tripod, one side at the store’s entrance, and the other at the store exit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*k-WY9QPGAuQocOBCjHhrWw.png)
_A camera tripod, two phones, and lots of tape_

Google has an incredibly useful [Face API](https://developers.google.com/vision/) that implements a native pipeline for detecting human faces and other related useful attributes. I used this API to handle the heavy lifting for facial recognition.

In particular, the API provided an approximate distance of a detected face from the camera. Once a customer’s face was within a close distance, I would take a snapshot of the customer, verify it against the Kairos API to ensure the customer existed in our database, and then update the Firebase database with the customer’s in-store status.

I also added a personalized text-to-speech greeting upon recognizing the customer. That really ended up wowing everybody who used it.

The result of this implementation can be seen [here](https://www.youtube.com/watch?v=XgtPey1TSIE):

Once the customer left the store, the exit-detection state of the Android application was responsible for retrieving the items the customer picked up from the database, calculating the total amount the customer spent, and then sending a push notification to the customer’s personal app via Firebase Cloud Messaging.

Of the 36 hours, we slept for about 6. We spent our entire time confined to a classroom in the middle of downtown Toronto. There were countless frustrating bugs and implementation roadblocks we had to overcome. There were some bugs in our demo that you probably noticed, such as the cameras failing to recognize several people in the same shot.

We would have also liked to implement additional features, such as detecting customers putting items back on the rack and adding a wider variety of items.

Our project ended up winning first place at the hackathon. We set up an interactive booth for an hour (the Chipotle box castle that can be seen in the title picture) and had over a hundred people walk through our shop. People would sign up with a picture, log into the shopping app, walk into the store, pick up an item, walk out, and get notified of their bill instantly. No cashiers, no lines, no receipts, and a very enjoyable user experience.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_J9ngCwl2XZLdLgHZeVJuA.jpeg)
_Walking a customer through our shop_

I was proud of the way our team played to each individual’s strengths and created a well put-together full-stack IoT project in the span of a few hours. It was an incredibly rewarding feeling for everybody, and it’s something I hope to replicate in my career in the future.

I hope this gave you some insight into what goes on behind the scenes of a large, rapidly prototyped, and hacky hackathon project such as EZShop.

**Follow me on [Twitter](https://twitter.com/SubhanNadeem19) and [Medium](https://medium.com/@subhan_nadeem) if you’re interested in more in-depth and informative write-ups like this one! I’m always opening to connecting with and learning from other software developers.**

**The project is open-source and can be found on Github [here](https://github.com/subhan-nadeem/EZShop). Be warned, hackathon code isn’t pretty!**

