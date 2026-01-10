---
title: How to build a Live Comment feature using JavaScript and Pusher
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-02T17:07:20.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-live-comment-feature-using-javascript-and-pusher-747d51e21430
coverImage: https://cdn-media-1.freecodecamp.org/images/0*AFHx4TZQ480CmwUU.png
tags:
- name: Apps
  slug: apps-tag
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Rahat Khanna

  These days “Social” has become the buzzword and we all want our apps to be the center
  of these amazing social conversations. Comments on a post, video, update or any
  feature of your new app is a great way to add fun and enriching soci...'
---

By Rahat Khanna

These days “Social” has become the buzzword and we all want our apps to be the center of these amazing social conversations. Comments on a post, video, update or any feature of your new app is a great way to add fun and enriching social conversations to your App.

If these conversations can be realtime, then it’s even better. So in this article we will be discussing how we can create a realtime comment feature for our web apps using [Pusher](https://pusher.com/) with Vanilla JavaScript on the front-end and [Node.js](https://nodejs.org/en/) on the back-end.

We will call this realtime comment system **Flash Comments**, which can be re-used for multiple posts/features in your app and can generate amazing conversations in real time. Only basic HTML, CSS and JavaScript knowledge is required to follow through this blog post.

Our app will look something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/0*pDZl2GiJiqbr2pBK.gif)

### Sections

* Brief Introduction to Pusher
* Signing Up with Pusher
* Node.js and Express App for exposing a Comment Creation API and triggering a Pusher Event
* Front End using Vanilla JavaScript subscribing to Channel

** Skip the first two sections, if you have already signed up with Pusher.

### Brief Introduction to Pusher

Pusher is an amazing platform which abstracts the complexities of implementing a realtime system on our own using WebSockets or Long Polling. We can instantly add realtime features to our existing web applications using Pusher as it supports wide variety of software development kits (SDKs).

Integration kits are available for variety of front-end libraries like Backbone, React, Angular, and jQuery — and also back-end platforms/languages like .NET, Java, Python, Ruby, PHP, and GO.

### Signing up with Pusher

You can create a free account in Pusher [here](http://pusher.com/signup). After you signup and login for the first time, you will be asked to create a new app as seen in the picture below. You will have to fill in some information about your project and also the front-end library or back-end language you will be building your app with. You also have an option to select the cluster of Pusher based on your users location distribution, I have chosen `ap2 (Mumbai, India)` as I may be building an app for the India region.

![Image](https://cdn-media-1.freecodecamp.org/images/0*AFHx4TZQ480CmwUU.png)

For this particular article, we will be selecting JavaScript for the front-end and Node.js for the back-end as seen in the picture above.

This will just show you a set of starter sample codes for these selections, but you can use any integration kit later on with this app.

![Image](https://cdn-media-1.freecodecamp.org/images/0*_dzai36l6cdqlv90.png)

### Node.js App

You can create a new folder named `**flash-comments**` and run the following command at the root of the folder:

It will ask you bunch of information regarding the app and it will create a new `**package.json**` file inside your folder.

We will be using the fairly simple and popular Express framework in Node.js. Now, we will install the important packages that will be used in our minimal Express app.

After installing all required `npm` modules, now we will create an entry point file for our Node.js app as `server.js` inside the root folder. Add the following basic code for a basic HTTP Server to be run using port `9000`.

Pusher has an open source NPM module for the Node.js integrations which we will be using. It provides a set of utility methods to integrate with Pusher APIs using a unique `**appId**`, `**key**` and a `**secret**`. We will first install the `pusher` `npm` module using the following command:

Now, we can use require to get the Pusher module and to create a new instance passing an options object with important keys to initialize our integration. For this article, I have put random keys. You will have to obtain it for your app from the Pusher dashboard.

You will have to replace the `appId`, `key` and a `secret` with values specific to your own app. After this, we will write code for a new API which will be used to create a new comment. This API will expose the route `/comment` with HTTP `POST` method and will expect an object for comment with the properties `name`, `email` and `comment`. Add the following code to your `server.js` file before the `app.listen` part.

In the above code, we have extracted the data from `req.body` into a `newComment` object and then used it to call the `trigger` method on the `Pusher` instance.

### Important Pusher Concepts

#### Channel

In Pusher, we have a conceptual grouping called “channels” and it provides the basic way to filter data in Pusher. A channel can represent many entities in a real world application. For example: In our comments app, a channel can be comments for a specific Article, video, blog post, photo, or live streaming of an event.

We would create a new unique channel id for each of these entities to uniquely identify or group data like comments associated with any one of these. Two unique live streaming videos should also have separate channels so that we can show the respective live comments stream on their respective pages.

So we will create a new unique channel for each entity with their unique id. For example a YouTube video comments channel can be named `comments-youtube-234`.

There are three types of channel

* **Public Channel** — can be subscribed by anyone who knows the name of the channel.
* **Private Channel** — channel which can be subscribed by authorized users only. If the channel name has a `private-` prefix, it will be regarded as a private channel.
* **Presence Channel** — this is a special channel type similar to private as only authorized users can subscribe, where the subscribers list is also maintained and notified to other users also. Channel name should have a prefix `presence-`

We will use a public channel in our blog post which we are naming as **flash-comments** but you should ideally use a private channel for commenting systems with unique name for each entity you want to enable commenting feature.

### Event

Now, the real data in pusher is transmitted through events which is the primary way of packaging messages. An event can be triggered by a back-end or even client in special cases for any particular channel. A channel is required to ensure that your message reaches the intended recipient.

We give a unique name to each event so that we can setup handlers for receiving and processing these event messages at each of our client end who has subscribed to any channel.

### Pusher Trigger Method

Now we will understand our server side code for sending an event to the pusher channel `**flash-comments**`.

We are using the `.trigger(channel-name,event-name, payload)`to send an event from the server whenever the `POST` API is called for creating a new comment. For the simplicity of this article, we will not use any database to save and persist the comments but in a production system. You would be required to store a comment corresponding to a unique entity id like a YouTube Video ID or a Blog Post ID.

Now, we can run our server using `node server` command. Our web service will be accessible on the URL `http://localhost:9000/comment`.We can write a `POST` request using any chrome extension like [Postman](https://www.getpostman.com/) or even [**curl**](https://curl.haxx.se/) to test if it returns `{ "created":"true" }` .

The curl command to test your `POST` API will be as follows:

### Front-End using Vanilla JavaScript

Now, we will be writing the most crucial part, the front-end code using Vanilla JavaScript. In the front-end code we will be developing a comments box section which would have following two features:

* **Display** all the Live Comments added to the channel with a smooth animation
* **Add** new comment to the live comments by hitting the `POST` API we have just created

### Step 1: Create a folder named public and create an index.html file

We have already written code in our `server.js` to serve static content from `public` folder, so we will write all our front-end code in this folder.

Please create a new folder `public` and also create an empty `index.html` file for now.

### Step 2: Add Boilerplate Code to our index.html

We will be adding some basic boilerplate code to set up the base structure for our web app like `Header`, and `Sections` where content like video or blog post can be put and also the section which will contain our `**Flash Comments**` box.

### Step 3: Create style.css file

Now we will also create a `style.css` file to contain the important CSS code for styling our web app and the `**flash comments**` component. We will add basic styles to render our skeleton.

### Step 4: Add the pusher.js Library and create app.js

Now we will add the pusher.js Library available on its CDN to use it to integrate with the Pusher system using plain JavaScript code. Please add the following script tag at the end of the body before its closing tag:

Also, create a new `app.js` file where we will be writing all our code and also import the same in our `index.html` file after the script tag to import `pusher.js` file.

In our file `app.js` now, we will write code to initialize the Pusher instance using the unique client API key we have got from the Pusher dashboard. We will also pass an object specifying the cluster and setting the flag encrypted to true so that all messaging and communication is encrypted. We will also use the `pusher.subscribe('channel-name')` to listen to all events for a specific channel.

We will create a JavaScript IIFE (Immediately Invoking Functions) to create a private scope so that we do not pollute the global scope. Please add the following code to `app.js` file:

### Step 5: Creating Form for adding new comment

Now, we will create the form controls for letting the user input their name, email and comment text for creating a new comment using our Node.js API and Pusher. We will add the following HTML code inside the existing form tag to create the form:

In the form code above, we have used HTML5 validations like r`equired` and `type=email` which would not allow user to keep these fields blank or submit an invalid email. These validations will automatically work in most browsers which support HTML5 form validations.

Also, we will be adding the following CSS to style the form:

After building the visual form, now we need to attach an event handler to the `Submit` event of the form. We will do that using the following code in the `app.js` file, probably at the top after the `var` declarations:

Now, we will write the code for implementation of the handler `addNewComment` with the following code:

We are using native XHR request to make an AJAX request to the Node API. You can use either jQuery AJAX or any framework-specific `ajax` method in your app. Now if we run our application, then fill the form and submit it, we will see a `Success: { created: true }`message in our browser developer tools console.

Also, we can see the Pusher Dashboard to see the stats about Event Messages sent for any channel.

![Image](https://cdn-media-1.freecodecamp.org/images/0*nxysjGfuHjjcCK1k.png)

### Step 6: Display List of Comments Received for this Channel

Now, we will bind to the `new_comment` event on this channel `flash-comments` so that we can receive any message about new comment creation done from any client in realtime, and we can display all those comments.

We will first add a template for a new comment in our `index.html` file inside the div tag with `id="comments-list"`.

Now, we will write the JavaScript code to bind to the new_comment event on the pusher channel instance we have subscribed. Whenever the `new_comment` event will be fired, we will take the template innerHTML content and replace the placeholders `{{name}}, {{email}} & {{comment}}`with the data passed along with the event and append them to the `comments-list` div element.

Using the above code, a new div tag representing the new comment will automatically be created and appended to the `comments-list` container.

We will now add the following CSS to nicely display the list of comments and also animate whenever a new comment appears on the list:

Now, you can run the app we have built, either in two different browsers or one in normal browser and the other in incognito window, and add multiple comments. We can see that the live comments will be added in realtime with a smooth animation.

![Image](https://cdn-media-1.freecodecamp.org/images/0*EU6UJeB7p1ZyImwq.gif)

The complete code for this tutorial is available on [GitHub](https://github.com/mappmechanic/flash-comments).

### Conclusion

We have built a nice web app with live comment feature using Pusher, Node.js and Vanilla JavaScript. We can use this component with any of our applications and enable live comments for variety of social entities like Videos, Blog Post, Polls, Articles and live streams.

We have used the Node.js server to create a REST API to get a new comment and then trigger a Pusher event on a specific channel. For any real world application, we can take a unique id for each entity and use a unique channel name for any entity. In a production scenario we can also store the comments in a persistent storage and then later retrieve them.

We have also created a Front-End app, which will connect to the Pusher API using the pusher.js library. We have created a form to hit the Node API which will trigger the `new_comment` event. Comments are displayed in realtime with an animation using the bind method on the channel instance.

This article was originally published on [Pusher’s blog](https://blog.pusher.com/build-live-comments-feature-using-javascript/).

