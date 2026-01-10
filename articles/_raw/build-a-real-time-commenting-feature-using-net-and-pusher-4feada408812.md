---
title: Build a real-time commenting feature using .NET and Pusher
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-03T15:07:25.000Z'
originalURL: https://freecodecamp.org/news/build-a-real-time-commenting-feature-using-net-and-pusher-4feada408812
coverImage: https://cdn-media-1.freecodecamp.org/images/0*dk8lZiI7UJOq2eLs.gif
tags:
- name: education
  slug: education
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ogundipe Samuel

  Today, we will build a mini-blog engine with live commentary features using .NET
  and Pusher.


  Reloading pages to view new comments can bore and is also strenuous, given you don’t
  even know if the reply to your comment has come in y...'
---

By Ogundipe Samuel

Today, we will build a mini-blog engine with live commentary features using .NET and Pusher.

![Image](https://cdn-media-1.freecodecamp.org/images/0*dk8lZiI7UJOq2eLs.gif)

Reloading pages to view new comments can bore and is also strenuous, given you don’t even know if the reply to your comment has come in yet or not. You keep reloading and keep wasting your data. To cut a long story short, users may abandon sites where they have to reload pages to see a new comment.

To follow through with this tutorial, we will use MSSQL as our database engine. Please ensure that it is up and running.

To follow this tutorial, please ensure that you are familiar with the basics of:

### Setting up a Pusher account and app

[Pusher](https://pusher.com/) is a hosted service that makes it super-easy to add realtime data and functionality to web and mobile applications.

Pusher acts as a real-time layer between your servers and clients. Pusher maintains persistent connections to the clients (over Web-socket if possible and falling back to HTTP-based connectivity) so that as soon as your servers have new data they want to push to the clients they can do so, via Pusher.

If you do not already have one, head over to Pusher and create a free account.

We will register a new app on the dashboard. The only compulsory options are the app name and cluster. A cluster represents the physical location of the Pusher server that will handle your app’s requests. Also, copy out your App ID, Key, and Secret from the App Keys section, as we will need them later on.

### Setting up the Asp.Net project in Visual Studio

The next thing we need to do is create a new `Asp.Net MVC application`.

To do so, let’s:

* Open `Visual Studio` and select `New Project` from the sidebar
* Under templates, select `Visual C#`
* Next, select `Web`
* In the middle section, select `ASP.NET Web Application`
* For this tutorial, I named the project: `Real-Time-Commenting`
* Now we are almost ready. The next step will be to install the official `Pusher` library for `ASP.NET` using the `NuGet Package`

To do this, we go to tools on the top bar, click on `NuGet Package Manager`, on the drop-down we select `Package Manager Console`.

We will see the `Package Manager Console` at the bottom of our Visual Studio. Next, let’s install the package by running:

### Crafting our application

Now that our environment is set up and ready, let’s dive into writing code.

By default, Visual Studio creates three controllers for us. But, we will use the HomeController for the application logic.

The first thing we want to do is to define a model that stores the list of articles we have in the database. Let’s call this model `BlogPost`. So, let’s create a file called `BlogPost.cs` in our models folder, and add:

In this code block, we have defined the model that holds our blog posts. The properties which we have defined here include:

* The id of the post, called `BlogPostID` (usually the primary key).
* The title of our post, called `Title` (defined as a string)
* The body of the post which we will be creating (defined as a string)

Next, let us create the model called `Comment`, which we had referenced earlier on. Let’s create a file called `Comment.cs` in our models folder and add:

Looking at the code above, we notice that we have declared the following properties:

* The ID of our comment called `CommentID` (Usually the primary key)
* The name of the person commenting
* The body of the comment
* The ID of the post we are commenting on

Now that we have defined our model, let’s reference it in our default database context called `ApplicationDbContext`.

To do this, let’s open `models\IdentityModels.cs` file. Locate the class called `ApplicationDbContext` and add the following after the create function:

In the code block above, the `DbSet` class represents an entity set used for read, update, and delete operations.

Here, we have defined two entities, our `BlogPost` and `Comment` models. We will now have access to them from an instance of the `ApplicationDbContext` .

### Connecting to our database

Although our model is set up, we still need to attach a database to our application. To do so, select the Server Explorer on the left-hand side of our Visual Studio, right click on Data Connections and add a database.  
 There are various databases that are lightweight and can fit into the application we are building, such as:

* Microsoft access database
* Sqlite Database
* MSSQL Server

For this tutorial, I used the MSSQL Server.

### Creating our controller

Now both our model and database are setup, let’s go ahead creating our index route. Open the `HomeController` and replace it with:

In the code block above, we have defined six different functions :

* The `Index` function, which shows a quick list of all our blog posts
* The `Create` function, which handles the addition of new BlogPosts for both `GET` and `POST` requests
* The `Details` function, which returns the full view of our post
* The `Comments` function, which returns a JSON data of all the comments for a particular post
* The `Comment` function, which handles the addition of a new comment and emitting the data to Pusher.

Before looking at our controller functions, we notice that there is an import of our DB context into our class with the line that says:

This makes it possible to access the database model which we have defined in our `ApplicationDbContext` class.

In the `Index` function we return our View, passing in a list of all the posts we have in our database, which will be looped.

Next, In the `Create` function that handles our `GET` request, we simply return the view for creating a new post.

We move to the `Create` function that handles our `POST` request, which receives an argument called `post` of type `BlogPost` . In this function we add a new `post` into the database, after which we return a redirect to our `Index` function.

In our `Details` function, we return an instance of a particular `post` to our view which will be displayed. This view will also display the form which allows us to add comments.

In our `Comments` function, we return all the `comments` that belong to a particular `post`, the ID of which was supplied as JSON. This method will be called via an AJAX POST.

Finally, our `Comment` function handles adding the comments to the database, and sending the data to Pusher. We notice here that this function is an `async` method. This is because the Pusher library sends the data asynchronously, and we have to await its response.

Also, we need to replace `XXX_APP_CLUSTER`, `XXX_APP_ID`, `XXX_APP_KEY` and `XXX_APP_SECRET` with our app cluster, ID, key and secret which we got from Pusher earlier on.

### Creating our view files

To complete our application we will need 3 different view files, which we will discuss below.

#### **The index view**

Let us replace the default content in the `Index.cshtml` file at `Views\Home\Index.cshtml` with:

Looking at the HTML structure above, we notice we have defined a table which lists all our posts and links them to the details page.

#### **The Create View**

Here, we need to create a new file called `Create.cshtml` in the `View\Home` folder and paste the following into it:

In the HTML structure above we have three main inputs:

* A text input element, which holds the title of the post
* A text input element, which holds the content of the post
* A button element, which is used to submit the new entry

**The Details View and Vue Bindings**

This is the final View file we will be needing. This file also handles binding to Pusher events and updating the comments in realtime using Pusher and Vue.  
 Let us create a new file called `Details.cshtml` in our `Views\Home` folder and add the following content into it:

[https://gist.github.com/755c0e5e8cbf53dbb9560deafdd50a21](https://gist.github.com/755c0e5e8cbf53dbb9560deafdd50a21)

In the above block of code, we have displayed the title and content of the current post, and **the number of comments** it has.

We have also created our comment form which comprises three main elements, which are:

* Text input for the name of the person making the comment
* Textarea for the body of the comment
* Button to save the new comment into the database

Notice that we have used Vue’s `v-for` directive to iterate and display the comments which are available.

Also, note we have included some required libraries such as:

* axios JavaScript library
* Vue js JavaScript library
* Pusher JavaScript library

#### **Pusher Bindings and Vue snippet**

Below is our example Vue snippet used to handle the comment submission and Pusher’s realtime updates.

In the code block above, we have done two major activities, which are:

#### **Uploading Comment Code**

To process new comments from the client side to the server, the following steps were followed:

* We attached a Vue event listener `@click` to our submit button which fires a method called `submit_comment`
* We defined a function called `submit_comment` which uses `axios` to make a POST request to our `comment` function

#### **Subscribing for Feed Additions on Server from other clients**

After the comment has been sent to the server, a request is sent to Pusher to return an event with the new data we have broadcasted. To listen for these realtime events, we have:

* Initialized a Pusher object while passing our app key and cluster
* Subscribed to our channel called `asp_channel`
* In the listen method in our Vue code, we declared a binding to our event called `asp_event`. In the callback function of this binding, we push the new data to our list of comments

That’s it! Now, once a new comment is made, it also gets broadcast and we can listen using our channel to update the comments in realtime.

![Image](https://cdn-media-1.freecodecamp.org/images/0*d-b_bCTehgAMknrK.gif)

### Conclusion

In this article, we have covered how to create a live comments feature using .NET and Pusher, and creating a mini blog engine in .NET.

The codebase to this tutorial is available in a [public Github repository](https://github.com/samuelayo/Net_real_time_commenting_pusher). You can download it for educational purposes.  
Have any reservations or comments, let us know your feedback in the comments.

This post was originally published by the author on Pusher’s blog [here](https://blog.pusher.com/build-a-realtime-commenting-feature-using-net-and-pusher/)

