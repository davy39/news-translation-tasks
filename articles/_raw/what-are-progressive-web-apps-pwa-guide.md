---
title: What are Progressive Web Apps? PWA Guide for Beginners
subtitle: ''
author: Ophy Boamah
co_authors: []
series: null
date: '2024-01-18T15:56:46.000Z'
originalURL: https://freecodecamp.org/news/what-are-progressive-web-apps-pwa-guide
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/Essentials.png
tags:
- name: progressive web app
  slug: progressive-web-app
- name: PWA
  slug: pwa
seo_title: null
seo_desc: "Progressive Web Apps (PWAs) are simply installable web applications – websites\
  \ that you can install on your device, much like you would install an app from an\
  \ app store. \nThey bring together the best parts of using a website (easy to access,\
  \ no need ..."
---

Progressive Web Apps (PWAs) are simply installable web applications – websites that you can install on your device, much like you would install an app from an app store. 

They bring together the best parts of using a website (easy to access, no need to install anything) with the great features of mobile apps (fast, can work offline), offering a high-quality user experience. 

The core of a PWA's usefulness lies in the offline-first approach, where applications are designed to function seamlessly without a constant internet connection. This means you can still use these apps even when your internet is slow or not available, and makes PWAs very user-friendly and accessible, even where an internet connection is not always reliable.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/pwaa.png)
_Graphic showing a native app vs a web application vs a PWA_

## 5 Reasons to Use a PWA Instead of a Native app

Progressive Web Apps (PWAs) are reshaping the landscape of digital interaction. They offer a hybrid experience that combines the best features of web and mobile apps. 

Let's delve deeper into why PWAs are often a superior choice compared to native apps:

### 1. Speed and Ease of Installation

PWAs eliminate the lengthy download and installation process typical of native apps. You can access a PWA as swiftly as you'd load a web page, making it as straightforward as bookmarking your favorite site – no waiting for downloads or navigating through app stores. 

Consider Twitter Lite, a PWA version of the popular social media platform, which offers the full Twitter experience without the need to wait for a separate app download. 

### 2. Minimal Storage Requirements

One of the most significant advantages of PWAs is their minimal storage requirements. Since they primarily store data online, much like cloud services, they occupy significantly less space on a user’s device. 

This feature is particularly beneficial for users with limited device storage or expensive data plans. For example, Pinterest’s PWA takes up less space than its native counterpart but still provides a rich, engaging user experience. 

### 3. Reliable Offline Performance

A PWA's ability to function offline is like having a good book downloaded to your e-reader, ready to enjoy even when you're out of range of a good signal. 

PWAs can function effectively even in areas with poor or no internet connectivity, using cached data from previous online activities. This ensures that users have uninterrupted access to essential features. 

A notable example is the Starbucks PWA, which allows customers to browse the menu and customize orders, regardless of their internet connection for a consistent user experience.

### 4. Cost-Effective Development and Cross-Device Compatibility

Developing a PWA can be more cost-effective than building native apps for various platforms. This unified approach not only saves significant development time and resources but also simplifies maintenance and updates. 

Businesses like Uber have leveraged PWAs to provide a seamless user experience across all devices without the need for multiple native apps. 

### 5. Automatic Updates and Push Notifications

PWAs update themselves seamlessly, much like a web page loading the latest content each time it’s visited. Users always have access to the most current version of the app without going through the process of manual updates. This feature ensures that users are not hindered by outdated versions, a common issue with native apps. 

For instance, Google Maps’ PWA automatically incorporates the latest features and improvements without user intervention. In addition to staying current, PWAs can engage users with push notifications, just like native apps, keeping them informed and involved without the need for a visit to the app store. 

![Image](https://www.freecodecamp.org/news/content/images/2024/01/pwass.png)
_Infographic of a Progressive Web App (PWA) showcasing its features: adaptability across devices, security, offline functionality, fast performance, updates, and push notifications._

## PWA Core Concepts

To fully grasp the potential and functionality of Progressive Web Apps, it's essential to understand their foundational components. These core concepts not only define the structure and behavior of PWAs but also distinguish them from traditional web applications.

### Service Workers: The Backbone of PWAs

Service workers are scripts that run in the background, separate from your web page. They act as a proxy between the web application and the network. 

Think of service workers as behind-the-scenes helpers for your web app. Their main job is to manage how your app talks to the internet. 

They can save important parts of your app on the user's device, which means your app can work even when there's no internet. They're also in charge of quietly updating app content and can send notifications, just like a native app on your phone.

### The App Manifest: Your PWA's Identity

The web app manifest is a JSON file which is essential because it tells the user's device how your app should look and behave. 

It's like your app's ID card – it includes the app's name, the icons it uses, the first page it should open, and how it should display (like in full screen). This file makes your web app feel more like a regular app, allowing users to 'install' it on their home screen.

### Caching: The Key to Offline Functionality

Effective caching is vital for a robust offline experience. Caching is like your app's memory. It stores important parts of your app so they can be quickly loaded later, even if there's no internet. It's crucial for making your app work offline. 

There are different ways to handle caching, such as cache-first (where the app checks the cache before the internet), network-first (the opposite), and stale-while-revalidate (a mix of both). The choice depends on what your app does and what kind of information it handles, affecting how your app stores and retrieves its data.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/pwa-components.png)
_Icons representing key components of a PWA: Service worker, Manifest and HTTPS_

## Overview of Building a PWA

Building a Progressive Web App (PWA) might sound complex, but it's quite manageable when you break it down into steps. In this article, I'll give you an overview of the process – and in my next tutorial, I'll go into the process in more detail.

### 1. Start with a Basic Webpage:

Create a simple website using HTML for structure, CSS for style, and JavaScript for functionality.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Ophy's To-Do List PWA</title>
</head>
<body>
    <h1>Ophy's To-Do List</h1>
    <input type="text" id="todo-input" placeholder="Add a new task...">
    <button onclick="addTask()">Add</button>
    <ul id="todo-list">
        <!-- Tasks will go here -->
    </ul>

    <script src="app.js"></script>
</body>
</html>

```

```css
body {
    font-family: 'Arial', sans-serif;
}

#todo-list {
    list-style-type: none;
}

#todo-list li {
    padding: 5px;
    margin: 5px;
    background-color: #f2f2f2;
    border-radius: 3px;
}

```

```javascript
function addTask() {
    var input = document.getElementById('todo-input');
    var newTask = input.value;
    if (newTask) {
        var listItem = document.createElement('li');
        listItem.textContent = newTask;
        document.getElementById('todo-list').appendChild(listItem);
        input.value = ''; // Clear the input
    }
}
```

### 2. Create a Manifest File:

In the manifest file, write down your app's name, the icons it uses, and the first page it should open. This makes your website act more like an app you can install.

```json
{
    "name": "Ophy's To-Do List",
    "short_name": "OphyToDo",
    "icons": [
        {
            "src": "favicon.ico",
            "sizes": "64x64 32x32 24x24 16x16",
            "type": "image/x-icon"
        }
    ],
    "start_url": "/",
    "display": "standalone",
    "theme_color": "#000000",
    "background_color": "#ffffff"
}

```

### 3. Set Up a Service Worker:

In your main JavaScript file, add a service worker. This is a special script that works separately from your website.

The service worker's job is to handle how your app stores and retrieves data, especially for offline use.

```javascript
self.addEventListener('install', function(event) {
    // Perform install steps
    var CACHE_NAME = 'ophy-todo-cache-v1';
    var urlsToCache = [
        '/',
        '/styles.css',
        '/app.js'
    ];

    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function(cache) {
                console.log('Opened cache');
                return cache.addAll(urlsToCache);
            })
    );
});

```

Following these steps will help you build a simple PWA that users can install and use, even when they're offline.

## Real World Use Cases for PWAs

These real-world examples demonstrate the practical benefits and impact of offline-first strategies:

1. **Starbucks**: Starbucks has a PWA that lets customers look at the menu and order drinks and food even when they're offline. This not only makes the experience better for customers but also helps increase sales and customer interaction with the brand, as they can order anytime, anywhere.
2. **Khan academy**: Khan Academy, a well-known educational site, has a PWA allowing students to download and access lessons and courses without an internet connection. This feature is particularly helpful for those in areas with unreliable internet, ensuring uninterrupted learning. Just like the Starbucks PWA, Khan Academy's use of this technology improves the user experience, making education more accessible and flexible.
3. **Trivago**: Trivago, a popular hotel search engine, developed a PWA to enhance user experience, especially for travelers with unstable internet connections. The PWA allows users to browse hotel deals and information offline, making trip planning more flexible and accessible. This has led to increased user engagement and higher conversion rates, as travelers can continue interacting with the app even in areas with poor connectivity.
4. **Forbes**: Forbes, a leading global media company, launched a PWA to improve the mobile experience for its readers. The PWA significantly reduced loading times and allowed offline reading of articles. This innovation not only enhanced user engagement but also resulted in a noticeable increase in readership and time spent on the site. The Forbes PWA demonstrates how media outlets can leverage offline-first strategies to reach and retain a wider audience, regardless of their internet connectivity.

## Conclusion

PWAs are changing the game in web development, bringing features we usually see in native apps to the web. 

They offer a blend of the accessibility of web applications with the engaging user experience of native apps. They represent a forward-thinking solution for businesses and developers looking to maximize reach and functionality while minimizing costs and complexity. 

PWAs aren't just a passing trend – they're the next big thing in how we make and use web apps. By focusing on working offline, PWAs provide a more reliable and user-friendly experience. 

Whether you're just curious or ready to start building, the following resources remain great places to begin exploring the possibilities of offline-first web applications.

* [Google's PWA Checklist](https://developers.google.com/web/progressive-web-apps/checklist)
* [MDN Web Docs on Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)
* [Web.dev for PWA tutorials](https://web.dev/progressive-web-apps/)

