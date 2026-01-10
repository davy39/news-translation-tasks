---
title: How Uber was made
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-31T23:30:59.000Z'
originalURL: https://freecodecamp.org/news/how-uber-was-made-da3c631066d0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*N8jLWFdC1v1ZBLdOHQlO3A.png
tags:
- name: mobile
  slug: mobile
- name: mobile app development
  slug: mobile-app-development
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: uber
  slug: uber
seo_title: null
seo_desc: 'By Dmytro Brovkin

  Uber has transformed the world. Indeed, its inconceivable to think of a world without
  the convenience of the innovative ride sharing service. Tracing its origins in a
  market which is constantly being deregulated, Uber has emerged tr...'
---

By Dmytro Brovkin

Uber has transformed the world. Indeed, its inconceivable to think of a world without the convenience of the innovative ride sharing service. Tracing its origins in a market which is constantly being deregulated, Uber has emerged triumphant. Operating in over 58 countries and valued roughly at US$ 66 billion, Uber has rapidly expanded to established branches in over 581 cities in over 82 countries with the United States, Brazil, China, Mexico and India being Uber’s most active countries.

If that wasn’t impressive enough, in 2016 the company completed a total of [2 billion rides](http://www.reuters.com/article/us-uber-rides-idUSKCN0ZY1T8) in one week. When you consider the fact that the first billion rides took Uber 6 years, and the second billion was garnered in a mere 6 months, it’s not surprising to see Uber emerge as a global business leader. This worldwide phenomenon is built on a simple idea, seductive in its premise - the ability to hail a car with nothing but your smartphone.

It took the problem of hailing a taxi and gave everyone an equitable solution while further capitalizing on the emerging market. And smart people are asking the right question: _How do I build an app like Uber for my business needs?_

### Humble Beginnings

It all started in 2008, with the founders of Uber discussing the future of tech at a conference. By 2010, Uber officially launched in San Francisco. In 6 months, they had 6,000 users and provided roughly 20,000 rides. What was the key to their success? For one, Uber’s founders focused on attracting both drivers and riders _simultaneously_. San Francisco was the heart of the tech community in the US and was thus the perfect sounding board for this form of technological innovation to thrive.

In the beginning, Uber spread their App through word of mouth, hosting and sponsoring tech events, and giving participants of their events free rides with their app. This form of go-to-marketing persists today - giving 50% discounts to new riders for their first Uber ride. This initial discount incentivized users to become long term riders, and the rest was history. As more and more people took to social media to tell the world about this innovative new App - the sheer brilliance of their marketing strategy paid off.

### Product Technology Cohesion: How Uber Works

What makes Uber, Uber? For one, it’s the ubiquitous appeal, or the way in which they streamlined their product, software and technology. It was, at the start, fresh, innovative, and had never been seen before. So if one were to replicate the model, they’d need to look at Uber’s branding strategy.

To use Uber, you have to download the app, which launched first on iPhone, then extended to Android and Blackberry.

![Image](https://cdn-media-1.freecodecamp.org/images/yDIB85tHWIguxTk-5yISquZxfjDP8L4mzUUc)

Uber’s co-founders, Garret Camp and Travis Kalanick, relied heavily on 6 key technologies based on iOS and Android geolocation. What really sold it though, was its clear core value - the ability to map and track all available taxis in your given area. All other interactions are based on this core value - and its what sets Uber (and will set _your_ app) apart from the crowd. To build an App like Uber, you’ll need to have:

**1. Registering/Log-in features:** Uber allows you to register with your first name, last name, phone number and preferred language. Once you’ve signed up, they’ll send you an SMS to verify your number, which will then allow you to set your payment preferences. Trip fares are charged after every ride through this cashless system.

**2. Booking features:** This allows drivers the option to accept or deny incoming ride requests and get information on the current location and destination of the customer.

**3. The ability to Identify a Device’s location:** Uber, via [CoreLocation framework](https://developer.apple.com/library/ios/documentation/CoreLocation/Reference/CoreLocation_Framework/_index.html) (for iOS platforms) obtains the geographic location and orientation of a device to schedule location and delivery. Understanding iOS and Android geolocation features is crucial for this step, because that’s what your App is running on.

**4. Point to Point Directions:** The Uber App provides directions to both the driver and the user. Developers of the Uber App use [MapKit](https://developer.apple.com/library/ios/documentation/MapKit/Reference/MapKit_Framework_Reference/_index.html) for iOS and [Google Maps Android API](https://developers.google.com/maps/documentation/android/?hl=uk) for Android to calculate the route and make directions available. They further implemented Google Maps for iPhone and Android, but cleverly adapted technology from other mapping companies to solve any logistical issues that might come up.

**5. Push Notifications and SMS:** You get up to 3 notifications instantly from Uber when you book a ride.

* A notification telling you when the driver accepts your request
* One when the driver is close to your location
* One in the off chance your ride has been cancelled

You further get the full update on your driver’s status, down to the vehicle make and license number, and an ETA on the taxi’s time of arrival.

**6. Price Calculator:** Uber offers a cashless payment system, paying drivers automatically after every ride, processed through the user’s credit card. Uber takes 25% of the driver’s fare, making for easy profit. They paired with Braintree, a world leader in the mobile payment industry, but other good options avaible are Stripe, or Paypal, via [Card.io](https://www.card.io/).

![Image](https://cdn-media-1.freecodecamp.org/images/jSK4uzHjvAgF9B-HZppjCqhtzposxcaTs4ck)

Here are few more much sought after features for the user’s side of the App:

* **The ability to see the driver’s profile and status:** Your customers will feel safer being able to see your driver’s verification, and it’s makes good security sense to ensure you know who’s using your App for profit.
* **The ability to receive alerts:** Receive immediate notifications about the status of your ride and any cancellations.
* **The ability to see the route from Their Phones (An In built Navigation system):** This is intrinsically linked to your geolocation features, you want to be able to direct your taxis to the quickest, most available routes.
* **Price calculation:** Calculating a price on demand and implementing a cashless payment system.
* **A “spilt fare” option:** Uber introduced this option wit great success. It allows friends to spilt the price of the ride.
* **Requesting previous drivers:** It’s a little like having your favourite taxi man on speed dial, and is a good way of ensuring repeat customers.
* **Waitlist instead of surge pricing:** Avoid the media hassle of employing surge pricing by employing a wait list feature, so your users can be added to a waiting list rather than be charged more than they should, and to keep them from refreshing the App during peak hours, reducing the resources required by your backend infrastructure.

Another key to Uber’s success, that should be noted by potential developers of similar Apps, is the way in which Uber operates. They tap into more than one market which equates to more riders, more drivers, and more business for the company. Uber has mastered the art of localization - the ability to beat out pre-existing markets and competitors, which further retains their customer base by improving their own business strategy.

They’ve taken local context and circumstances into consideration. For example, they partnered with Paypal in November 2013 to provide as many people in Germany don’t use credit cards, and switched to services based on SMS messages in Asia as there are more people but fewer smart phones per capita. This helps them cater to various markets and and optimize profits.

The Uber marketing strategy isn’t static - it’s _dynamic._ Expansion was necessary, and the business model reaps profits from saturating the taxi market with their customers and drivers, driving their exponential growth. What aspiring App developers can take from this is that you need to design your App for _flexibility._

![Image](https://cdn-media-1.freecodecamp.org/images/xjyzI3-4GQNC6sGtfj5nFecOrXfmeIJPAKNK)

Design your App in a way that’s going to let it take a hit and roll with punches. Having a system in place that allows you to build and integrate changes effectively within the App and allows team members to communicate effectively is of paramount importance.

What made Uber so successful was its ability to reshape how we think about technology and its operation. Indeed it made the market a better, more efficient place through the innovative on-demand service.

### What Technology is Uber Built on?

The tech side of the App is written largely in JavaScript which is also used to calculate supply and predict demand. With the real time dispatch systems being built on Node.js and Redis. Java, as well as Objective-C is used for the iPhone and Android apps. [Twilio](http://www.twilio.com/customers/stories/hulu) is the force behind Uber’s text messages, and push notifications are implemented through [Apple Push Notifications Service](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Chapters/ApplePushService.html) on the iOS platform and [Google Cloud Messaging](http://developer.android.com/google/gcm/index.html) (GCM) for the Android App.

### How much does Uber make?

Actually, it’s a lot less than you think. The $66 billion valuation, after the 25% commission (which rounds out to about $0.19 per ride) mostly goes towards credit card processing, interest, tax, compensation for employees, customer support, marketing, and various anti-fraud efforts.

### How much does it take to build Uber?

Uber’s not just one App, it’s two - one for the rider and one for the driver. The cost of developing an App like Uber is dependent on a number of factors

* the cost of building an MVP
* product development and acquisition
* getting the economics of marketing sorted
* the constant cost of building on and improving your App’s analytic capabilities

When you make an App like Uber, you’ll invest a fair bit into design services, backend and web development, project management, not to mention Android and iOS native app development. The total man hours round out to around 5000 hours for similar on demand taxi Apps, which puts the cost of developing such an App to around $50,000 (assuming that your team works for $50 dollars an hour). However, since hourly rates roughly range from $20 to $150, median costs could be higher or lower.

### Conclusion

To wrap up, Ubers success was due to several factors, including a clear business model and interaction based features, and not the other way around combined with a marketing strategy focusing on attracting users.

The question on everyone’s mind of course is how can you reduce the overall risk of failure by making sure that your idea and product are viable when you’re developing an App?

One way is to use a Mobile App development partner (such as [Octodev](https://octodev.net/)) that has worked on many such Apps and understands the processes involved. An advance of using such a partner is they’ve worked on many such App development projects and have the practical experience in product development to avoid the pitfalls and make the most of your vision.

![Image](https://cdn-media-1.freecodecamp.org/images/xBVVhGnGnGEq75DCyMztISQhiCRXGmkrh1nF)
_Octodev App Development Process_

Another important part of ensuring that your App development project is swiftly and smoothly executed is having a clear road map and regular communication during the project. There are many approaches to achieve this and we, at Octodev, use a consultative approach to App development. We draw from our successful App implementations. [Get in touch](https://octodev.net/contact-us/) with us now if you want an accurate cost for your own Uber like App idea.

This article was originally published on the [Octodev Blog](https://octodev.net/how-uber-was-made/).

