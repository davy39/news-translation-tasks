---
title: How to build a photo feed using .NET and Pusher
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-03T15:41:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-photo-feed-using-net-and-pusher-5c2dae1ee889
coverImage: https://cdn-media-1.freecodecamp.org/images/0*w8Gy4MNNr3vwqdWh.gif
tags:
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ogundipe Samuel

  Today, we will make a real-time photo feed using .NET and Pusher.


  We will build a mini system that allows people to upload their images/photographs
  for everyone to view in real-time. It’s like a mini-Instagram without the comment,...'
---

By Ogundipe Samuel

Today, we will make a real-time photo feed using .NET and Pusher.

![Image](https://cdn-media-1.freecodecamp.org/images/0*w8Gy4MNNr3vwqdWh.gif)

We will build a mini system that allows people to upload their images/photographs for everyone to view in real-time. It’s like a mini-Instagram without the comment, like, and views aspect.

Sounds cool? Let’s ride on.

To follow this tutorial, please ensure that you are familiar with the basics of:

### Setting up a Pusher account and app

Pusher is a hosted service that makes it super-easy to add real-time data and functionality to web and mobile applications.

Pusher sits as a real-time layer between your servers and your clients. Pusher maintains persistent connections to the clients (over Websockets if possible and falling back to HTTP-based connectivity) so that as soon as your servers have new data they want to push to the clients they can do so via Pusher.

We will register a new app on the dashboard. The only compulsory options are the app name and cluster. A cluster represents the physical location of the Pusher server that will handle your app’s requests. Also, select `jQuery` as the front-end technology and `ASP.NET` as the back-end tech for this tutorial. For other projects, you can choose as per your requirements.

Next, copy out your App ID, Key, and Secret from the `App Keys` section, as we will need them later on.

### Setting up the Asp.Net project in Visual Studio

The next thing we need to do is create a new Asp.Net MVC application.  
To do so, let’s:

* Open Visual Studio and select new project from the sidebar
* Under templates, select `Visual C#`
* Next, select web
* In the middle section, select `ASP.N``ET MVC Web Applicat``ion`

For this tutorial, I named the project: `Real-time-photo-feed`.

Now we are almost ready. The next step will be to install the official `Pusher` library for .Net using the `NuGet Package`.

To do this, we go to tools, via the menu on the top bar, click on `NuGet Package Manager`. On the drop-down, we select `Package Manager Console`.

We will see the `Package Manager Console` at the bottom of our Visual Studio. Next, let’s install the package by running:

Alternatively, we can also install the `Pusher` library using the `NuGet Package Manager UI`. To do this, in the `Solution Explorer`, right-click either `References` or a project and select `Manage NuGet Packages`. The Browse tab displays available packages by popularity. Search for the `Pusher` package by typing in `PusherServer` into the search box on the top right. Select the Pusher package to display the package information on the right and to enable the `Install` button.

### Crafting our application

Now that our environment is set up and ready, let’s dive into writing code.

By default, Visual Studio creates three controllers for us. However, we will use the `HomeController` for the application logic. The first thing we want to do is to define a model that stores the list of images we have in the database.

Under the `models` folder, let’s create a file named `PhotoFeed.cs` and add the following content:

In the above block of code, we have declared a model called `PhotoFeed` with three main properties:

* Id: This is the primary key of the model table
* Comment: The description of the image
* Imagepath: The path to the stored image

Now we have defined our model, let’s reference it in our default database context called `ApplicationDbContext`. To do this, let’s open `models\IdentityModels.cs` file, then locate the class called `ApplicationDbContext` and add the following after the create function:

In the code block above, the `DBSet` class represents an entity set used for reading, updating, and deleting operations. The entity which we will use to do CRUD operations is the `PhotoFeed` model we created earlier, and we have given it the name `FeedModel`.

### Connecting our database

Although our model is set up, we still need to attach a database to our application. To do so, select the Server Explorer on the left-hand side of our Visual Studio, right click on Data Connections, and add a database.

There are various databases that are lightweight and can fit into the application we are building, such as:

* Microsoft access database
* Sqlite Database
* MSSQL Server
* Firebird
* VistaDb

For this tutorial, I used the MSSQL Server.

### Creating our index route

Now both our model and database is set to work. Let’s go ahead and create our index route. Open the `HomeController` and replace it with the following code:

In the code block above, we have defined our Index function for both `GET` and `POST` requests.

Before looking at our `GET` and `POST` controller functions, we notice that there is an import of our db context into our class with the line that says:

This makes it possible to access our database model which we have defined using the `DbSet` class in our `ApplicationDbContext` class.

In the `GET` function, we have returned the view with which we will handle the addition and real-time updating of our feed.

Notice that in the `GET` function, we pass a variable into the view function called `me`. This variable is a **queryable** version of our `BlogFeed` model. This will be passed to the view, which is later looped and rendered.

Observe that the `POST` method is set to be asynchronous. This is because the Pusher .NET library uses the await operator to wait for the asynchronous response from the data sent to Pusher.

In this function, we first add our new movie to the database, then we trigger an event. Once the event has been emitted, we then return an ok string.

However, please note that the code above would not handle any error if the image was saved in DB but not posted using Pusher. We might need to use a try and catch statement to handle failures posting to Pusher.

### Creating our view files

Let’s open up our `Views\Home\Index.cshtml` and replace the content with the following:

In the above block of code, we have created our form which **comprises** three main elements, which are:

* Text input for the comment of the image.
* File input for selecting the image we want to feed.
* Button to save the new entry into the database.

Also, note we have included some required libraries such as:

* Bootstrap CSS
* jQuery JavaScript library
* Pusher JavaScript library

### Pusher Bindings And jQuery Snippet

Below is our example jQuery snippet used to handle the file upload and Pusher’s real-time updates.

In the code block above, we notice we have done two major activities, which are:

### Uploading Image Code

To process the upload of images from the client side to the server, the following steps were followed:

* We attached an event listener to our file input button that stores our image into a variable called `files`.
* We defined a function called `feed_it` which creates a new `FormData`, then appends our image and description to the form data. This function then makes an `AJAX POST` request to our `index` route.

### Subscribing for Feed Additions on Server from other clients

After the image has been sent to the server, a request is sent to Pusher to return an event with the new data we have broadcasted. To listen for this real-time events, we have:

* Initialized a Pusher object while passing our app key and cluster.
* Subscribed to our channel called `a_channel`.
* Declared a binding to our event called `an_event`. In the callback function of this binding, we have `pre-pended` the new data to our list of feeds.

That’s it! Now, once a photo gets uploaded, it also gets broadcast and we can listen using our channel to update the feed in real-time.

Below is an image of what we have built:

![Image](https://cdn-media-1.freecodecamp.org/images/0*w8Gy4MNNr3vwqdWh.gif)

### Conclusion

In this article, we have covered how to create a real-time photo feed using .NET and Pusher as well as handling file uploads in .NET.

The code base to this tutorial is available in a [public GitHub](https://github.com/samuelayo/ASP.NET-PHOTO-FEED) [repository](https://github.com/samuelayo/ASP.NET-PHOTO-FEED). You can download it for educational purposes.

Have a better way we could have built our application, reservations or comments? Let us know in the comments.

This post was originally published on Pusher’s blog [here](https://blog.pusher.com/build-a-photo-feed-using-net-and-pusher/).

This version has been edited for clarity and may appear different from the original post.

