---
title: React Native Networking – How To Perform API Requests In React Native using
  the FetchAPI
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2023-01-20T19:35:24.000Z'
originalURL: https://freecodecamp.org/news/react-native-networking-api-requests-using-fetchapi
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-pixabay-276502--1-.jpg
tags:
- name: api
  slug: api
- name: computer networking
  slug: computer-networking
- name: React Native
  slug: react-native
seo_title: null
seo_desc: 'APIs, or application program interfaces, are essential mechanisms for businesses
  in all industries. They allow for a secure exchange of data between two different
  systems, such as a web application and a database.

  Think of when you are using a mobile...'
---

APIs, or application program interfaces, are essential mechanisms for businesses in all industries. They allow for a secure exchange of data between two different systems, such as a web application and a database.

Think of when you are using a mobile app to order food from a restaurant. The restaurant's menu, pricing, and ordering information could all be stored in a database that is managed by a back-end application.

To enable the mobile app to access the data, the app must make an API request to the back-end application. The request will include information such as the restaurant's location, the menu items, and the desired order.

The back-end application will then respond with the requested information. The mobile app can then use the data to create a user-friendly interface for ordering food.

API requests can also be used to update the database with new data, providing a way for the application to save and store new information. You can also set up with in-app subscription events. For example, when a user's subscription is about to expire, an API request is sent to a notification system to alert the them.

In this tutorial, you’ll learn how to make GET, POST, PUT and DELETE requests to APIs in a React Native app using the FetchAPI. You can access the full code from this tutorial [here](https://snack.expo.dev/@ubahthebuilder/b61a85).

## Prerequisites

To follow this tutorial, you’ll need just two things:

* A basic understanding of React Native
    
* [Expo Snack](https://snack.expo.dev/)
    

Expo Snack is an online development environment for React Native which essentially lets you run React Native apps on your web browser. This removes the hassle of setting up your local React Native environment from scratch.

## Setting up the app

Go to [Expo Snack](https://snack.expo.dev/) to initialize a new React Native project, then go to the App.js file and clear the file’s content.

Start by importing React, useState, and useEffect hooks from React as well as the Text, View, and StyleSheet components from React Native.

```js
import React,{useState, useEffect} from 'react';
import { Text, View, StyleSheet } from 'react-native';
```

Next, define an App component function. Inside the function body, we set the data state to an empty array, the loading state to true, then we return a simple “Hello World” text for now.

```js
export default function App() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  return (
    <View>
      <Text>Hello World</Text>
    </View>
  );
}
```

Later on, when we retrieve data from JSONPlaceholder API (see next section), we’ll populate out the data state with it and render the data from the App component as text.

## The API we’ll be working with

The API we’ll be fetching our data from is [JSONPlaceholder.](https://jsonplaceholder.typicode.com/) This is a free fake API for testing and prototyping purposes.

The API comes with 6 common resources which you can read, edit, update or delete by making API requests.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/https___jsonplaceholder.typicode.com_posts-1.png align="left")

*Array of 100 post objects*

So here each post is an object with four properties: userId, id, title and body. There are 100 objects in the array.

You can:

* create a new post by making a POST request to this API (that is, add a new object)
    
* read a specific post by making a GET request to this API (that is, read an object)
    
* update an existing post by making a PUT request to this API (that is, modify an object)
    
* delete an existing post by making a DELETE request to this API (that is, remove an object)
    

Let’s start with making GET requests in our React Native app.

## How to Make a GET Request in React Native

An API GET request is a type of API request used to retrieve data from a server. The request is sent via a HTTP GET method and data is returned in the form of a JSON or XML object.

Let’s make a GET request in our React Native app. First, store the URL you want to make the request to inside a variable (paste this code under state variable declaration):

```js
const url = "https://jsonplaceholder.typicode.com/posts"
```

Next, use the fetch method to execute the API request to the URL. Wrap the fetch inside of useEffect (this hook allows us to perform side effects in our code, for example API calls):

```js
useEffect(() => {
  fetch(url)
    .then((resp) => resp.json())
    .then((json) => setData(json))
    .catch((error) => console.error(error))
    .finally(() => setLoading(false));
}, []);
```

So what’s happening here inside `useEffect`? First we make a GET call to the URL. Once the data is returned, we parse it to JSON with `resp.json()`, and in the next `then` block we call `setData` to update the state with the post.

In the event of any error, the `catch` method will run (which logs the error to the console). Finally, we set the loading state to `false`.

Finally, we render the post gotten from the API:

```js
<View style={styles.container}>
  {loading ? (
    <Text>Loading...</Text>
  ) : (
    data.map((post) => {
      return (
        <View>
          <Text style={styles.title}>{post.title}</Text>
          <Text>{post.body}</Text>
        </View>
      );
    })
  )}
</View>;
```

So if the API request is still in progress, we show the “Loading” text on our app. Once the data is retrieved, we loop through the array and render the title and text of each post.

To style it up a bit, paste the following stylesheet underneath App:

```js
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    backgroundColor: "#ecf0f1",
    padding: 8,
  },
  title: {
    fontSize: 30,
    fontWeight: "bold",
  },
});
```

Here’s the result when the posts are returned from the API.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/vigorous-carrot---Snack.png align="left")

*Final look*

As you can see, we successfully fetched the list of posts from the API and rendered each of them in our React Native app.

Now if you want to retrieve a specific resource (like a specific post) as opposed to a collection of resources like a list of posts, all you need to do is add the resource ID to the URL like so:

```js
const url = "https://jsonplaceholder.typicode.com/posts/1"
```

If we make a GET request to the above API endpoint, the server will only gives us back the post with an ID of 1.

Let’s move on to other types of requests.

## How to Make a POST Request in React Native

An API POST request is a type of API request that is used to create or update a resource on a web server.

It sends data to the server in the form of a request body which usually contains information such as the title, description, and other relevant details. If the data is accepted, the server responds with a success code and the resource is created or updated.

When making a POST request with the FetchAPI, you must specify the method as ‘POST’. Here’s an example of a POST to the fake server from our React Native app:

```js
fetch("https://jsonplaceholder.typicode.com/posts", {
  method: "POST",
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    userId: 55,
    id: 101,
    title: "Post title",
    body: "Post body",
  }),
})
  .then((response) => response.json())
  .then((responseData) => {
    console.log(JSON.stringify(responseData));
  })
  .done();
```

The value of the body property must always be a JSON object with JSON string values (hence the `JSON.stringify` call).

Once the server is done processing the request, it sends back a response to tell you if the resource was created on the server or not (and why it failed).

## How to Make a PUT Request in React Native

If a POST request is used to create a new resource on a server, a PUT request is used to update a specific resource on that server.

In a PUT request, you need to specify the ID of the resource you want to update on the server as well as the new values. Here’s an example which updates the title and body of post one on the server:

```js
fetch("https://jsonplaceholder.typicode.com/posts/1", {
  method: "PUT",
  body: JSON.stringify({
    userId: 55,
    id: 101,
    title: "New Post title",
    body: "New Post body",
  }),
})
  .then((response) => response.json())
  .then((responseData) => {
    console.log(JSON.stringify(responseData));
  })
  .done();
```

Similar to a POST request, the server sends back a response to tell you if the resource was updated on the server or not (and why it failed).

## How to Make a DELETE Request in React Native

As you might have guessed, a DELETE request is used to delete a specific resource from a server.

In a DELETE request, you only specify the ID of resource you want to delete on the server:

```js
fetch("https://jsonplaceholder.typicode.com/posts/1", {
  method: "DELETE",
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
})
  .then((response) => response.json())
  .then((responseData) => {
    console.log(JSON.stringify(responseData));
  })
  .done();
```

Once the server is done with processing the request, it sends back a response to tell you if the resource was deleted on the server or not (and why it failed).

## How to Integrate Other Third-Party APIs to React Native

Third-party APIs are created and maintained by organizations other than the main developer of the application. They are used to provide access to certain external data sources so that developers can incorporate them into their applications.

With the widespread use of React Native for developing mobile applications, third-party APIs can be easily integrated to create powerful and feature-rich applications.

One of the main benefits of using third-party APIs is that they are often updated frequently, which means that the developers can quickly access the latest features and data sources. This can be especially useful when developing mobile applications, as they often require access to the latest features and data sources.

Additionally, you can also use third-party APIs to add features that are hard or impossible to create in-house as it requires substantial human, financial, and time resources.

For example, there are complex APIs for [Facebook login](https://developers.facebook.com/docs/facebook-login/web/), [payment processing](https://stripe.com/docs/api), [weather report](https://openweathermap.org/api), [integrating in-app purchases infrastructure](https://adapty.io/blog/react-native-in-app-purchases-implementation-tutorial), and so on.

## Conclusion

This tutorial walked you through the steps of making API requests in React Native using the built-in Fetch library.

I hope you enjoyed this as much as I did writing it. Have a great week.
