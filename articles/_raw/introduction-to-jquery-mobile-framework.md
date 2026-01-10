---
title: A Simple Introduction to the jQuery Mobile Framework
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-02T16:49:43.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-jquery-mobile-framework
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99e8740569d1a4ca225a.jpg
tags:
- name: jQuery
  slug: jquery
- name: mobile app development
  slug: mobile-app-development
seo_title: null
seo_desc: "By Alfrick Opidi\nWhen the world discovered the web, things were unexciting\
  \ and lifeless. For example, building a simple image mouseover application required\
  \ several lines of code, and couldn't work on some platforms. \nBut things got better\
  \ when jQuer..."
---

By Alfrick Opidi

When the world discovered the web, things were unexciting and lifeless. For example, building a simple image mouseover application required several lines of code, and couldn't work on some platforms. 

But things got better when jQuery was introduced, since it allowed developers to create stunning JavaScript applications that could run comfortably in various places.

After that, the jQuery team took things a notch higher by developing jQuery UI, which made it possible for developers to create nice-looking web applications on the existing jQuery core. 

Better still, in 2010 jQuery Mobile was introduced which has made development much better and more efficient.

Built with a bias to mobile phones, [jQuery Mobile](http://jquerymobile.com/) is an effective, unified framework that offers UI components, data transitions, and other exciting features. 

jQuery Mobile leverages the functionalities of HTML5, CSS3, jQuery, as well as jQuery UI into a single framework that allows developers to achieve consistency across different platforms and devices.

## Basic Features of jQuery Mobile

### 1. Great simplicity and usability

The jQuery Mobile framework is uncomplicated and flexible. Since the framework's configuration interface is mark-up driven, developers can easily build their complete basic application interfaces in HTML, with minimal or no JavaScript code. 

Complex tasks requiring several lines of JavaScript code, such as Ajax calls and DOM manipulation, can easily be realized with few [lines of code](https://www.freecodecamp.org/news/long-code-vs-short-code/) in mobile jQuery.

For example, if we want a user to click and hide some text after a page has been created in the DOM, but before enhancement is complete, we can simply use the **pagecreate** event handler. This is something that would require several lines code to accomplish without jQuery Mobile. 

```javascript
$(document).on("pagecreate","#mypagetest",function(){
  $("span").on("click",function(){
    $(this).hide();
  });                       
});
```

In the above code, the **#mypagetest** parameter refers to the id of the page that specifies the page event. Also, the **on()** method is used to attach the event handlers.

Furthermore, its simplicity allows developers to break their applications into multiple pages. With the framework, developers can "write less, and do more."

### 2. Progressive enhancement and graceful degradation

[Progressive enhancement](https://www.gov.uk/service-manual/technology/using-progressive-enhancement) and graceful degradation are key features that propel the agility of jQuery Mobile. They enable it to support both high-end and less capable devices (for example, those lacking JavaScript support).

The framework allows developers to build applications that can be accessed by the widest number of browsers and devices, whether it is Internet Explorer 6 or the newest Android or iPhone.

Mobile jQuery also gives developers the ability to render basic content (as built) on basic devices. And the more sophisticated platforms and browsers will be increasingly enriched using additional, externally linked JavaScript and CSS.

### 3. Support for user-friendly inputs

During jQuery mobile development, developers can include an uncomplicated [API](https://blog.api.rakuten.net/what-is-an-api/) to support touch, mouse, and cursor focus-based user input functionalities. Several types of easily styled and touch-friendly form elements are also included in the framework.

Examples include checkbox and radio sets, slider, search filtering, and menu selection elements. Also, every one of the form elements includes an alternate 'mini' version, which can be easily incorporated into mobile web pages.

For example, here's how to create a checkbox button using jQuery Mobile. Notice that the **data-mini="true"** attribute is added to create a mini version of the button. 

```html
<form>
    <input type="checkbox" name="checkbox-mini-0" id="my-checkbox" data-mini="true">
    <label for="checkbox-mini-0">Click here to agree</label>
</form>
```

Beyond all this, to ensure the user experience is optimized on mobile devices, the framework has a rich Ajax-driven navigation system that allows animated page transitions to take place seamlessly.

With jQuery Mobile transition events, you can animate the transition from the current active page to the new page. 

For example, you can use the **pagebeforeshow** event (triggered on the "to" page) and the **pagebeforehide** event (triggered on the "from" page) when transitioning from one page to the next. Both events are triggered before the transition animation begins.

Let's see how they can be applied: 

```javascript
$(document).on("pagebeforeshow","#myfirstpage",function(){ 
    
    // When entering myfirstpage
    
  alert("myfirstpage is about to appear");
    
});

$(document).on("pagebeforehide","#myfirstpage",function(){ 
    
    // When leaving myfirstpage
    
  alert("myfirstpage is about to disappear");
});
```

### 4. Accessibility

Besides its cross-platform capabilities, jQuery for mobile was created with a strong consideration for accessibility. 

The framework comes with support for Accessible Rich Internet Applications (WAI-ARIA) to assist disabled persons using screen readers and other assistive technologies easily access web pages.

### 5. Lightweight size

Mobile jQuery's lightweight size (about 40KB when minified) adds to its swiftness. Additionally, the fact that it employs minimal image dependencies also vastly accelerates its capabilities.

### 6. Theming and UI widgets

jQuery Mobile has an in-built theme system that enables developers to determine their own application styling. With the jQuery Mobile Themeroller, developers can effectively customize their applications to fit their color, tastes, and preferences.

The framework also comes with various innovative, cross-platform widgets that enable developers to create applications that are better customized. 

Some of the available widgets are persistent toolbars, buttons, dialogs, and the commonly used popup widget.

### 7. Responsiveness

The framework's full responsiveness enables the same underlying codebases to fit comfortably in different types of screens, from mobile devices to desktop-sized screens.

## Basic Page Structure of jQuery Mobile

jQuery Mobile's structure has all the UI components and attributes required for creating user-friendly and feature-rich mobile web applications and websites of all kinds—whether basic or advanced.

You can use jQuery mobile to build web pages, various types of list views, toolbars, a wide range of form elements and buttons, dialogs, as well as other functionalities.

Importantly, since jQuery Mobile is created on top of jQuery core, it lets developers leverage jQuery UI code and access key facilities. These include robust animation and image effects for web pages, DOM manipulation, event handling, and Ajax for server communication.

Let's get a feel for how jQuery mobile development code looks.

For example, in this time of the COVID-19 pandemic when most people are working from home or from [co-working spaces](https://novelcoworking.com/locations/ohio/cincinnati/hooper-building/), let's create a simple web page that demonstrates some team management mistakes that people make.

Here is the code:

```html
<!DOCTYPE html>
<html>

<head>
  <title>jQuery Mobile Example</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css" />
  <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
  <script src="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
</head>

<body>
  <div data-role="page" date-theme="c">
    <div data-role="header">
      <h1>fCC jQuery Mobile Sample</h1>
    </div>
    <div data-role="content">
      <p>COVID-19 Work-From-Home Team Management Mistakes To Avoid</p>
    </div>
    <p>
    <ul data-role="listview" data-inset="true" data-filter="true"></ul>
    </p>
    <p>
    <ul>
      <li><a href="#">Using Unnecessary Tools</a></li>
      <li><a href="#">Foregoing Team Evaluations</a></li>
      <li><a href="#">Micromanaging</a></li>
      <li><a href="#">Hiring Too Quickly</a></li>
      <li><a href="#">Not Having Contingencies</a></li>
    </ul>
    </p>
    <div data-role="footer">
      <h4>alfrickopidi.com, 2020 - Copyright</h4>
    </div>
  </div>
</body>

</html>
```

Here is the output when the above mobile jQuery lines of code are opened on a browser:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/image1.png)

Notably, when the browser is decreased or increased, the size of the items in the list also adjusts appropriately. Therefore, the web page can be easily accessed in various devices with different screen resolutions without worrying about lack of consistency. The size of the items will change accordingly to suit the type of device.

As you can see in the above code sample, the document is a simple HTML5 that includes the following three things:

* Files from the jQuery Mobile CSS (jquery.mobile-1.4.5.min.css)
* Files from the jQuery repository (jquery-1.11.1.min.js)
* Files from the jQuery Mobile repository (jquery.mobile-1.4.5.min.js)

These files are directly linked to the jQuery CDN. Another alternative is to head over to the [download page](http://jquerymobile.com/download/) to get these files and host them on a private server.

Importantly, including the "viewport" metatag during jQuery mobile development instructs devices that the page width and the device screen width are equivalent (width=device-width).

The tag also instructs the browser to zoom in to 100 per cent (scale=1). If the scale is changed to 2, for instance, the browser will zoom the web page by 50 per cent.

A closer examination of the code reveals some strange "_data-"_attributes scattered throughout it. This is an improved feature of HTML5 that enables developers to pass organized data across an application – for example, the _data-role="header"_ attribute defines the head section of the web page.

The above example just scratches the surface of the things developers can achieve using jQuery Mobile. The framework's [documentation](https://demos.jquerymobile.com/1.4.5/) is easy to follow and describes its many features, including linking pages, incorporating animated page transitions, and designing buttons.

## Conclusion

jQuery for mobile is a resource-rich framework built with jQuery, HTML5, and CSS capabilities to handle certain cross-platform, cross-device and cross-browser compatibility issues effectively.

The framework offers great opportunities for creating mobile and web applications that are powerful, fully responsive, and future-ready.

Will you give it a try?

