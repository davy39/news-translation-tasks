---
title: How you can replicate Airbnb’s location area display using geocoding in Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-22T18:28:35.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-replicate-airbnbs-location-area-display-using-geocoding-in-angular-2001794f86a9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kowBDo9y5hXO73JQUBu6AQ.png
tags:
- name: Angular
  slug: angular
- name: Google
  slug: google
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Filip Jerga

  Have you thought about integrating Google Maps into your project? Do you know how
  to geocode a location? It’s not that hard. All it takes is 20 minutes, several lines
  of code, and basic programming knowledge. So let’s see how it’s done...'
---

By Filip Jerga

Have you thought about integrating Google Maps into your project? Do you know how to geocode a location? It’s not that hard. All it takes is 20 minutes, several lines of code, and basic programming knowledge. So let’s see how it’s done.

### Let’s start with dependencies and the API key

All we need is to install [Angular Google Maps (AGM)](https://angular-maps.com/). There are a lot of packages on the internet that provide you with “out-of-the-box” Google Maps components. It is up to your preference which one you choose. **I decided on AGM because of its nicely documented API and wide range of components.**

Now is a time to setup our API key. **No API key is no fun with a map!** Google recently came up with an interesting idea. You need to provide your billing details in order to setup your project and get your API key. No worries! You need to reach a certain amount of requests in order to get charged for the service.

**We need to enable the Maps JavaScript API (25,000 free daily requests) and Geocoding API (2,500 free daily requests).** You also have an option to set your daily limit so you will not go over it.

**To get your API key, follow these steps:**

1. Go to the [Google developer console](https://console.developers.google.com/projectselector/apis/dashboard).
2. Create a new project
3. Go to the library section and enable **Maps JavaScript API** and **Geocoding API**
4. Get your credentials (API key). And then celebrate :)

![Image](https://cdn-media-1.freecodecamp.org/images/1*gGuj7I_E5hXqt42Bi1sdYA.png)
_Let’s keep this open for little while. We need our API key in Angular._

### Let’s start coding!

Warm up your machines and open your projects in the code editors of your choice, because things will get serious now.

Let’s create a map module so we have everything together. We need a service to handle all of the logic and components to display a map. Very easy — just type in the terminal: **ng g component map.** You can also check out my folder structure and map component in my [GitHub project](https://github.com/Jerga99/bwm-ng).

In the same folder as your map component folder, create **map.module.ts**. We need to import **AgmCoreModule** and give it the API key we got from Google. **Don’t forget to reference your MapModule in the main AppModule (or whatever Module where you want to display a map)!**

AGM module will provide us with all the necessary components and directives to display a Google map. It will handle the load of the Google Maps API so we need only focus on geocoding a location.

### We need a service

In order not to pollute our map component with geocoding logic, it’s always good practice to use a service. Create the map service in the same folder as your map-related logic and implement the following function:

Let’s break it down:

1. We are getting geocoder from the window object because I didn’t find abstraction in the AGM package. **Geocoder exposes functions required to geocode the location.**
2. Next we will return an Observable because why not? **Geocode is asynchronous, and the best way to work with async code in Angular is definitely observables.**
3. Call geocode with a location. After a while, when the function is resolved, our callback function is called with a result and a status.
4. Check for a status, and if it’s **OK** we are good to go. The **Geocoding was successful and we can get coordinates of our location by calling a lat and a lng function on the geometry object.**
5. If the status is not OK, just emit an error and drop a tear :(

That should be it for our service. It wasn’t that hard, right?

### Continue with rental map component

Let’s get back to our map component and fill the template with an AGM map.

Here is some code taken from the official documentation of AGM. **We are referencing the agm-map component.** This will display Google Maps on the page, **but don’t forget to set the height of agm-map**, otherwise it will not be displayed! Go to your SCSS or CSS file and write: **agm-map {height: 400px}**.

In order to display a location in the map, **we need to provide latitude and a longitude input properties to agm-circle** (the component that will display the circle area of the location on the map). The zoom property will just zoom in on the map, so the location is more visible. You can see that we are displaying the agm-circle only when we have a latitude and a longitude. Other properties to consider are the radius of the circle, color, and the opacity.

**Most important on agm-map is the mapReady eventEmitter.** This function will emit an event when the Google Maps API is loaded and a map is ready to display a location. **This is the best time for us to call our Map Service and geocode location!** So let’s not lose time — let’s create the function mapReadyHandler in our map component.ts file.

Here it is. **MapReadyHandler will call getGeoLocation, which is responsible for calling our service with the value of the location.** When the location is geolocated and emitted from the service, we will get the coordinates in the callback function subscribe.

We are almost done. **Now we just need to set a lat and a lng and call detectChanges to make sure our map will be updated with the displayed area.**

### Last piece of the puzzle

Our map component is finished. Now we just need to display it on the screen. You can choose the parent component of your choice where you want to display your map. In my case, I wanted to display the map of my rental location. See the code below:

**I am referencing my map component inside of the Rental Detail Page** and providing the location input property inside. For example it could be: New York, Main Street. **And voilà! The map with the location is displayed when we navigate to the details page of the rental.**

### Recap

To make sure everything is clear now, let’s see it in a bigger picture:

![Image](https://cdn-media-1.freecodecamp.org/images/1*nC3brY6LKHObyEzKsLFuyA.png)

I hope you now understand how this works! In case you have any questions, feel free to contact me or leave a comment.

Now you know how to integrate Google Maps inside an Angular application. This is a very simple version of it. If you are interested in something more difficult, you can check out [my GitHub project repository](https://github.com/Jerga99/bwm-ng/tree/master/src/app/common/map).

For the whole picture on the completed project, you can see my course on Udemy: [The Complete Angular, React & Node | Airbnb style application](http://bit.ly/2vs8jKM).

Happy coding!

Filip Jerga

