---
title: The React + GraphQL 2020 Crash Course
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2020-06-30T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/the-react-graphql-2020-crash-course
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/React---GraphQL-2020-Crash-Course-Cover--Large--1.png
tags:
- name: '2020'
  slug: '2020'
- name: Apollo GraphQL
  slug: apollo
- name: apollo client
  slug: apollo-client
- name: beginner
  slug: beginner
- name: GraphQL
  slug: graphql
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: null
seo_desc: "Have you heard a lot about using React with GraphQL but don't know how\
  \ to combine them to build amazing apps? In this crash course, you'll learn how\
  \ to do just that by building a complete social blogging app. \nWithin an afternoon,\
  \ you will gain the c..."
---

Have you heard a lot about using React with GraphQL but don't know how to combine them to build amazing apps? In this crash course, you'll learn how to do just that by building a complete social blogging app. 

Within an afternoon, you will gain the core skills to build your own React and GraphQL projects.

## Why you should learn React with GraphQL ?

React is the go-to library for building amazing app experiences with JavaScript. GraphQL, on the other hand, is a tool that gives us a better, more straightforward means of getting and changing our data.

That data could be from a standard database (as we'll be using in our app) or as React frameworks like Gatsby have made possible, even from static files such as markdown files. Regardless of how it's stored, GraphQL makes working with data in our apps better.

We'll see how to leverage the powers of React and GraphQL by creating a social blogging app from start to finish, where you can create, read, edit and delete posts.

[![Click to access the course](https://dev-to-uploads.s3.amazonaws.com/i/o51wpa2tgx9k85p8rse8.gif)](https://bit.ly/2020-react-graphql)

You can [click here](https://courses.reedbarger.com/p/2020-react-graphql) to access the course.

## What tools we'll be using ?️

The crash course is meant for developers who are somewhat familiar with React (including the core React Hooks, such as `useState` and `useEffect`), but aren't familiar with GraphQL yet.

Basic React knowledge is assumed, but GraphQL knowledge is not required. We'll cover all the core GraphQL concepts you need along the way.

Throughout the course, we'll utilize the following technologies to create our app:

* **React** (to build our user interface)
* **GraphQL** (to get and change data in a declarative way)
* **Apollo Client** (to allow us to use React and GraphQL together)
* **Hasura** (to create and manage our GraphQL API + database)

To top it off, we'll be using the online IDE CodeSandbox. This will allow us to code our entire application within the browser in realtime, without the need to create any files, folders, or install dependencies on our own.

## Creating a GraphQL API from scratch

To get started working with GraphQL, we'll see how to make an entire GraphQL API from scratch that will communicate with our database. 

Fortunately, using the (free) service **Hasura**, this process is very simple and straightforward. Within seconds, we'll see how to create and deploy a complete GraphQL API to the web, which is connected to a Postgres database that will take care of storing our app data.

[![Click to access the course](https://dev-to-uploads.s3.amazonaws.com/i/ss4wp2tt4ernoe5ukea8.png)](https://learn.codeartistry.io/courses/2020-react-graphql/lectures/19445637)*Click to watch this lecture*

## Getting familiar with GraphQL

In the second lecture, we'll cover how to write in the GraphQL language using our API's built-in console called **GraphiQL**. 

First, we will create a table in our database for all of our posts data. After which, Hasura will automatically create the **queries** and **mutations** we need, which are the names of GraphQL operations that allow us to get and change data in our database. 

Throughout this lesson, we'll get very familiar performing queries and mutations in GraphiQL, which will enable us to get entire sets of posts and individual posts, as well as to create, update, and delete our individual post data. 

[![Click to access the course](https://dev-to-uploads.s3.amazonaws.com/i/bo5twcv0hhal7xtj1ksw.png)](https://learn.codeartistry.io/courses/2020-react-graphql/lectures/19445640)*Click to watch this lecture*

## Connecting React with our GraphQL API using Apollo Client

Now that we're comfortable with using GraphQL and understand its core features, we'll see how to connect it with our React client. 

The way that we connect our React app with the GraphQL API we created is through a library called **Apollo**. We'll see how to set up the Apollo client, by providing the GraphQL endpoint, which points to our API, like so:

```javascript
import ApolloClient from "apollo-boost";

const client = new ApolloClient({
  uri: "https://react-graphql.herokuapp.com/v1/graphql"
});
```

With our newly created client, we have the ability to execute any GraphQL operation through React. To do this, however, we need to pass our client to our entire to all of our React components. We do that with the help of the Apollo provider, as you see below:

[![Click to access the course](https://dev-to-uploads.s3.amazonaws.com/i/iplsbo37x2oujohn7ulc.png)](https://learn.codeartistry.io/courses/2020-react-graphql/lectures/19445642)*Click to watch this lecture*

### Getting posts with useQuery

After setting up our client, we'll see how to execute different GraphQL operations with them, using some special React hooks that come with the package `@apollo/react-hooks`.

The hook that allows us to query for data with GraphQL is called `useQuery`. With it, we'll first see how to get and display all of our post data in our homepage.

Additionally, we'll learn how to write our GraphQL queries directly in our JavaScript files with the help of a special function called `gql`.

```jsx
import React from "react";
import { useQuery } from "@apollo/react-hooks";
import { gql } from "apollo-boost";

export const GET_POSTS = gql`
  query getPosts {
    posts {
      id
      title
      body
      createdAt
    }
  }
`;

function App() {
  const { data, loading } = useQuery(GET_POSTS);

  if (loading) return <div>Loading...</div>;
  if (data.posts.length === 0) return <Empty />;

  return (
    <>
      <header className={classes.header}>
        <h2 className={classes.h2}>All Posts</h2>
        <Link to="/new" className={classes.newPost}>
          New Post
        </Link>
      </header>
      {data.posts.map(post => (
        <Post key={post.id} post={post} />
      ))}
    </>
  );
}
```

## Creating and editing new posts with useMutation

After that, we'll see how to create new posts with the `useMutation` hook. In order to do this, we'll take a look at how to work with GraphQL variables to pass our mutation dynamic values that will change with each execution. 

Following that we'll take a look at how to edit our posts. To do so, we'll need to fetch an individual post and display it within our form, so that our user can make changes to the data. Then we'll need to execute a mutation that will perform the update, based on the posts id. 

[![Click to access the course](https://dev-to-uploads.s3.amazonaws.com/i/n9swv8j0qr962spqxhkx.png)](https://learn.codeartistry.io/courses/2020-react-graphql/lectures/19445643)*Click to watch this lecture*

## Handle loading and errors

In the following lecture, we'll cover some essential patterns for handling the process of loading our data. 

It's important to do so when we execute a mutation, to make sure we don't submit our forms multiple times as our mutation is being executed. We'll also take a look at how to handle errors in the event that our mutation is not executed correctly. 

[![Click to access the course](https://dev-to-uploads.s3.amazonaws.com/i/548ekws3psm3cbfpqy8e.png)](https://learn.codeartistry.io/courses/2020-react-graphql/lectures/19445638)*Click to watch this lecture*

## Deleting posts

Finally, we'll cover how to delete posts from our app. First, we'll confirm that the user wants to actually delete the post that they've made, then perform the mutation. 

Additionally, we'll take a look at how to update our UI in response to mutations with  the helpful `refetch` function that Apollo gives us. It will enable us to re-execute a query on demand. In this case, we'll do it after the delete mutation has been successfully performed.

[![Click to access the course](https://dev-to-uploads.s3.amazonaws.com/i/ojjd4jjxuh0h7p1048ck.png)](https://learn.codeartistry.io/courses/2020-react-graphql/lectures/19445639)*Click to watch this lecture*

## Become a Professional React Developer

React is hard. You shouldn't have to figure it out yourself.

I've put everything I know about React into a single course, to help you reach your goals in record time:

[**Introducing: The React Bootcamp**](https://www.thereactbootcamp.com)

**It’s the one course I wish I had when I started learning React.**

Click below to try the React Bootcamp for yourself:

[![Click to join the React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Click to get started*

