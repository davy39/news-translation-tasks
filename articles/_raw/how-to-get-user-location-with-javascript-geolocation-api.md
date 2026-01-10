---
title: JavaScript Geolocation API Tutorial – How to Get a User's Location in JS
subtitle: ''
author: Israel Oyetunji
co_authors: []
series: null
date: '2022-09-07T18:29:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-user-location-with-javascript-geolocation-api
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/Blog-article-cover-images--4---1-.png
tags:
- name: api
  slug: api
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'Some applications require you to know your user''s location, like food
  delivery or eCommerce apps. So you''ll need an efficient way to get this info.

  The Geolocation API, which we will look at today, is a simple solution. You can
  use it to determine yo...'
---

Some applications require you to know your user's location, like food delivery or eCommerce apps. So you'll need an efficient way to get this info.

The Geolocation API, which we will look at today, is a simple solution. You can use it to determine your users' location, local currency, language, and other useful information. You can then use this to provide them with the most relevant content based on their location.

In this article, we'll go over what the Geolocation API is, why it's useful, and how to use it in your apps.

## What Is the Geolocation API?

The JavaScript Geolocation API provides access to geographical location data associated with a user's device. This can be determined using GPS, WIFI, IP Geolocation and so on.

To protect the user's privacy, it requests permission to locate the device. If the user grants permission, you will gain access to location data such as latitude, longitude, altitude, and speed. You'll also get the accuracy of the acquired location data and the approximate time when the position was acquired.

Here are a few uses for geolocation:

* Show user's position on a map
    
* Get up-to-date local information
    
* Show local Points-of-interest (POI) near the user
    
* Enable Turn-by-turn navigation (GPS)
    
* Track a fleet or delivery vehicle
    
* Tag photographs with a location
    

## How to Use the Geolocation API

You can access the Geolocation API by calling the `navigator.geolocation` object. It grants the app access to the device's location.

This object provides the methods listed below for working with the device's position:

1. getCurrentPosition: Returns the current location of the device.
    
2. watchPosition: A handler function that is automatically invoked when the device's location changes.
    

There are three possible arguments with these methods:

* A success callback (required)
    
* An error callback (optional)
    
* An options object (optional)
    

### How to Get User Location with `getCurrentPosition()`

You can use the `getCurrentPosition` method to get the user's current location. It sends an asynchronous request to the browser, asking for consent to share their location.

Here is the syntax for getting a user's location:

```js
const successCallback = (position) => {
  console.log(position);
};

const errorCallback = (error) => {
  console.log(error);
};

navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
```

When you run this, you'll get a popup in the browser requesting permission:

![Image](https://www.freecodecamp.org/news/content/images/2022/09/popup.PNG align="left")

Click **Allow**, and open up the developer console. You'll see that the successful call returns two things:

1. `GeolocationPosition.coords` object: represents the position, altitude and the accuracy at which the device calculates these properties.
    
2. `timestamp`: represents the time at which the location was gotten.
    

You should see something like this in your console:

```plaintext
GeolocationPosition {coords: GeolocationCoordinates, timestamp: 1662499816712}
    coords: GeolocationCoordinates
        accuracy: 7173.528443511279
        altitude: null
        altitudeAccuracy: null
        heading: null
        latitude: 6.5568768
        longitude: 3.3488896
        speed: null
        [[Prototype]]: GeolocationCoordinates
timestamp: 1662499816712
```

With this simple request, we've successfully gotten the location. But that's not all. We can also track the user by watching their location.

### How to Track User Location with `watchPosition()`

The `watchPosition()` method allows the app to continually track the user, and get updated as their position changes. It does this by installing a handler function that will be called automatically whenever the user's device position changes.

Here is the syntax below, where `id` is basically used to manage or reference the method:

```js
const id = navigator.geolocation.watchPosition(successCallback, errorCallback);
```

### How to Stop Tracking Position with `clearWatch()`

We use the `clearWatch()` method to cancel the handler functions that were previously installed using the `watchPosition`.

```js
navigator.geolocation.clearWatch(id);
```

### How to Use the `options` Object

Although the [`options`](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/getCurrentPosition#parameters) object is optional, it provides parameters that can help you get more accurate results, for example:

```js
const options = {
  enableHighAccuracy: true,
  timeout: 10000,
};

navigator.geolocation.getCurrentPosition(
  successCallback,
  errorCallback,
  options
);
```

In the code above, we specified in out options object that:

* The response should provide a more accurate position, by setting enableHighAccuracy to true.
    
* The maximum length of time (in milliseconds) the device is allowed to take in order to return a position. In this case, 10 seconds.
    

## Wrapping Up

In this article, we learned about the JavaScript Geolocation API, how to use it to get a user's location and also track the user using the watchPosition() method.

You can go further to explore this API by building a Weather app, Search App or Map app. Thanks for reading!
