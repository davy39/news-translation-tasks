---
title: How to Convert a React App to React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-04T20:36:00.000Z'
originalURL: https://freecodecamp.org/news/converting-a-react-app-to-react-native
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb77f740569d1a4cae4f4.jpg
tags:
- name: mobile app development
  slug: mobile-app-development
- name: React
  slug: react
- name: React Native
  slug: react-native
seo_title: null
seo_desc: 'By Gwendolyn Faraday

  I have been working on a lot of mobile projects lately — including Cordova, PhoneGap,
  React Native, some Ionic and Swift — but I have to say, React Native is by far the
  best experience in mobile development I have had so far. It ...'
---

By Gwendolyn Faraday

I have been working on a lot of mobile projects lately — including Cordova, PhoneGap, React Native, some Ionic and Swift — but I have to say, React Native is by far the best experience in mobile development I have had so far. It has great, web-like developer tools, lets me use NPM packages plus a lot of great react-native ones, and also produces faster, smoother apps than Cordova or Ionic. It shares the same workflow as a React application for the web which is pretty easy to reason about and find where things are quickly.

Now I am building an app to gamify recycling in Indiana. I have a web app completed in alpha, however, the app required the use of geolocation, augmented reality, and some other features, so I am building a mobile app to complement the one for the web. Since the web app is in React, I figured it would be easier to build the Native version in iOS and Android at the same time using React Native.

Here are some mockups to give you an idea.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wueFtT0VpHQ3uxJm5sqWQg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*dSFJs29dTU8RiLBcpwUhAg.png)
_(I changed the menu from the right side to the left side after this)_

### Setting Up the React Native App

Where React Native outdoes React is on it’s simple set up for apps. One command creates a folder with all your Xcode and Android set up as well as a starter app ready for the emulator.

[Link to simple set up instructions](https://facebook.github.io/react-native/docs/getting-started.html).

After getting it to run in the simulator, I create a ‘src’ directory to put all my code in. Then I turn on live reload (command + D opens the dev menu on iOS and control + D on Android) and begin developing!

![Image](https://cdn-media-1.freecodecamp.org/images/1*uakeeXPDb09NCgpr3uK3yQ.png)

A quick note about React-style applications: If you are new to this, it can feel a little strange to return your view from your `.js` files.

React, in its simplest form is a way to write modular, reusable code. Each component is broken down into sub components wherever it makes sense. Each component is encapsulated as a function or class in its own file, meaning you only import what you need. The function then return its view — the content to display on the screen from the component.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZF5Pc5eg9KYQP-Cpo6IkyQ.png)

### Menu and Navigation

I have a menu on the web, but I need to change the location for mobile. I wanted the user to be able to swipe or click to open the menu. There are a surprising number of React Native libraries out there to cover most mobile needs.

[react-native-side-menu](https://github.com/react-native-community/react-native-side-menu) is a great little library that was pretty easy to set up. I tested out the swiping to make sure it was smooth and then added links to the side menu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CrUTBi4wdMstsOh5kZ005Q.png)

RN doesn’t come with a built in navigation solution, so I added [react-native-router-flux](https://github.com/aksonov/react-native-router-flux). It works great, even if you are not using a traditional flux (flux was similar in concept to Redux) state management system and it’s easy to set up.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rIFVcz6EFmanByClF4Ix7Q.png)
_router.js_

A `Scene` is a ‘view’ or a ‘page’ in the application (you can see how the navigation works together in the short video clip at the end). The `title`attribute shows up in the header at the top, the `key` is used for navigating to the specific page, and the `component` is the actual Javascript file that contains the React Native component to display on that page. So, I created a component for each page with placeholder content:

![Image](https://cdn-media-1.freecodecamp.org/images/1*gTBtDUUcGA9s9cAXuQNWzQ.png)

Now, there is a menu and basic dummy pages and the user has the ability to navigate around the app. That was pretty quick and easy —I just installed a few modules and wrote a minimal amount of code.

### List Views

Most of the components I made I was able to copy from my web app and just update the UI.

For this app, I have an ever-growing array of various characters that I wanted to display in a scrollable list on mobile. React Native offers ScrollView and ListView as build in solutions for handling infinite scroll.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DdyYRy8j07M53H_DM-se3w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Mi5OiCEeLYFAb4r3Hc8gqA.png)

Each one of the animals above can be clicked on and viewed on an individual page:

![Image](https://cdn-media-1.freecodecamp.org/images/1*P7ROW-uP6fqCH4DSvkkWmw.png)

I set the ‘Amici Info’ page as a scene in the router and populate it with the information of the creature that was clicked on.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xi5wNcI6RBCc7zICrAE8hg.png)

### Reusable Components

I can also make wrappers around components with styles and basic functionality of common mobile solutions. eg cards, I can update the colors and padding slightly for each project.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2DvVIaSBmtTHtC-Q2N4Ezg.png)

### Porting Over Redux

Fortunately, most of my redux and API calls are the same. The app doesn’t need quite as much data as the website, so I could remove a few functions.

The only thing I am doing so far is fetching the character objects from DynamoDB (AWS).

![Image](https://cdn-media-1.freecodecamp.org/images/1*njqrI7O6EUIB1KfstjuDKw.png)

This is the reducer to match this action:

![Image](https://cdn-media-1.freecodecamp.org/images/1*SztYfpquPHgEVr5C4ntIQg.png)

That’s basically the state of Redux so far. I still have a lot more work to do on the Redux part but this is a good start. **Next up:** I need to set up a map component and display the locations for users to see.

### Debugging and Dev Tools

One of the best features of React Native is the dev tooling. `Command + D` gives me a dev menu:

![Image](https://cdn-media-1.freecodecamp.org/images/1*vlbSKws1cVciibhiK2zXyw.png)

It’s one click to open up Chrome Developer Tools or use an inspector similar to the `inspect element` option when right-clicking in a browser.

### Wrapping Up

For an MVP, I think it’s coming along well so far.

%[https://youtu.be/44hq-XaqR14]

I really enjoy working in React Native and I will continue to use it whenever possible until something better comes along.

_If I’m missing any information in this article or you have any questions, let me know_ :)

