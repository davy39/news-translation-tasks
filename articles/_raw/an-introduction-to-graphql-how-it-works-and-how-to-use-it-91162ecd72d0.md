---
title: 'An introduction to GraphQL: how it works and how to use it'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-24T17:03:26.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-graphql-how-it-works-and-how-to-use-it-91162ecd72d0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*472sv1dYbnObNwS2
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Aditya Sridhar

  GraphQL is a query language for API’s. It shows what are the different types of
  data provided by the server and then the client can pick exactly what it wants.

  Also in GraphQL you can get multiple server resources in one call rather...'
---

By Aditya Sridhar

GraphQL is a query language for API’s. It shows what are the different types of data provided by the server and then the client can pick exactly what it wants.

Also in GraphQL you can get multiple server resources in one call rather than making multiple REST API calls.

You can check out [https://graphql.org/](https://graphql.org/) for the full list of benefits.

The thing is until you see GraphQL in action, it’s hard to understand the benefits. So let’s get started with using GraphQL.

We will be using GraphQL along with NodeJS in this article.

### Pre-requisites

Install NodeJS from here: [https://nodejs.org/en/](https://nodejs.org/en/).

### How to use GraphQL with NodeJs

GraphQL can be used with multiple languages. Here we will focus on how we can use GraphQL with JavaScript using NodeJS.

Create a Folder called **graphql-with-nodejs**. Go into the project folder and run `npm init` to create the NodeJS project. The command for this is given below.

```bash
cd graphql-with-nodejs npm init
```

### Install the Dependencies

Install Express using the following command:

```bash
npm install express
```

Install GraphQL using the following command. We will be installing GraphQL and GraphQL for Express.

```bash
npm install express-graphql graphql
```

### NodeJS Code

Create a file called **server.js** inside the project and copy the following code into it:

```js
const express = require('express');
const port = 5000;
const app = express();

app.get('/hello', (req,res) => {
    res.send("hello");
   }
);

app.listen(port);
console.log(`Server Running at localhost:${port}`);
```

The above code has a single HTTP GET endpoint called **/hello**.

The end point is created using Express.

Now let us modify this code to enable GraphQL.

### Enabling GraphQL in the code

GraphQL will have a single URL endpoint called **/graphql** which will handle all requests.

Copy the following code into **server.js:**

```js
//get all the libraries needed
const express = require('express');
const graphqlHTTP = require('express-graphql');
const {GraphQLSchema} = require('graphql');

const {queryType} = require('./query.js');

//setting up the port number and express app
const port = 5000;
const app = express();

 // Define the Schema
const schema = new GraphQLSchema({ query: queryType });

//Setup the nodejs GraphQL server
app.use('/graphql', graphqlHTTP({
    schema: schema,
    graphiql: true,
}));

app.listen(port);
console.log(`GraphQL Server Running at localhost:${port}`);
```

Let us go through this code now.

**graphqlHTTP** enables us to set up a GraphQL server at **/graphql** url. It knows how to handle the request that is coming in.

This setup is done in the following lines of code:

```js
app.use('/graphql', graphqlHTTP({
    schema: schema,
    graphiql: true,
}));
```

Now let us explore the parameters inside graphqlHTTP.

### graphiql

graphiql is a Web UI with which you can test the GraphQL endpoints. We will set this to true so that it is easier to test the various GraphQL endpoints we create.

### schema

GraphQL has only one external endpoint **/graphql**. This endpoint can have multiple other endpoints doing various things. These endpoints would be specified in the schema.

The schema would do things like:

* Specify the endpoints
* Indicate the input and output fields for the endpoint
* Indicate what action should be done when an endpoint is hit and so on.

The Schema is defined as follows in the code:

```js
const schema = new GraphQLSchema({ query: queryType });
```

The schema can contain **query** as well as **mutation** types. This article will focus only on the query type.

### query

You can see in the schema that the **query** has been set to **queryType**.

We import queryType from **query.js** file using the following command:

```js
const {queryType} = require('./query.js');
```

**query.js** is a custom file which we will be creating soon.

**query** is where we specify the read-only endpoints in a schema.

Create a file called as **query.js** in the project and copy the following code into it.

```js
const { GraphQLObjectType,
    GraphQLString
} = require('graphql');


//Define the Query
const queryType = new GraphQLObjectType({
    name: 'Query',
    fields: {
        hello: {
            type: GraphQLString,

            resolve: function () {
                return "Hello World";
            }
        }
    }
});

exports.queryType = queryType;
```

### query Explained

queryType is created as a **GraphQLObjectType** and given the name **Query**.

**fields** are where we specify the various endpoints.

So here we are adding one endpoint called **hello.**

**hello** has a **type** of **GraphQLString** which means this endpoint has a return type of String. The type is **GraphQLString** instead of **String** since this a GraphQL schema. So directly using String will not work.

**resolve** function indicates the action to be done when the endpoint is called. Here the action is to return a String “Hello World”.

Finally, we export the querytype using `exports.queryType = queryType`. This is to ensure we can import it in **server.js.**

### Running the Application

Run the application using the following command:

```bash
node server.js
```

The application runs on **localhost:5000/graphql**.

You can test the application by going to localhost:5000/graphql.

This URL runs the Graphiql web UI as shown in the screen below.

![Image](https://cdn-media-1.freecodecamp.org/images/MIEYIUgUDC85-MYLKOU5kddtUiGduNKCTDSk)

The input is given in the left and the output is shown in the right.

Give the following input

```js
{
  hello
}
```

This will give the following output

```js
{
  "data": {
    "hello": "Hello World"
  }
}
```

### Congrats ?

You have created your first GraphQL endpoint.

### Adding more endpoints

We will create 2 new endpoints:

* **movie**: This endpoint will return a movie, given the movie ID
* **director**: This endpoint will return a director given the director ID. It will also return all the movies directed by this director.

### Adding Data

Usually, an application will read data from a Database. But for this tutorial, we will be hardcoding the data in the code itself for simplicity.

Create a file called **data.js** and add the following code.

```js
//Hardcode some data for movies and directors
let movies = [{
    id: 1,
    name: "Movie 1",
    year: 2018,
    directorId: 1
},
{
    id: 2,
    name: "Movie 2",
    year: 2017,
    directorId: 1
},
{
    id: 3,
    name: "Movie 3",
    year: 2016,
    directorId: 3
}
];

let directors = [{
    id: 1,
    name: "Director 1",
    age: 20
},
{
    id: 2,
    name: "Director 2",
    age: 30
},
{
    id: 3,
    name: "Director 3",
    age: 40
}
];

exports.movies = movies;
exports.directors = directors;
```

This file has the movies and directors data. We will be using the data in this file for our endpoints.

### Adding the movie endpoint to the query

The new endpoints will be added to queryType in query.js file.

The code for the movie endpoint is shown below:

```js
movie: {
            type: movieType,
            args: {
                id: { type: GraphQLInt }
            },
            resolve: function (source, args) {
                return _.find(movies, { id: args.id });
            }
        }
```

The return type of this endpoint is **movieType** which will be defined soon.

**args** parameter is used to indicate the input to the movie endpoint. The input to this endpoint is **id** which is of type **GraphQLInt.**

**resolve** function returns the movie corresponding to the id, from the movies list. **find** is a function from **lodash** library used to find an element in a list.

The complete code for **query.js** is shown below:

```js
const { GraphQLObjectType,
    GraphQLString,
    GraphQLInt
} = require('graphql');
const _ = require('lodash');

const {movieType} = require('./types.js');
let {movies} = require('./data.js');


//Define the Query
const queryType = new GraphQLObjectType({
    name: 'Query',
    fields: {
        hello: {
            type: GraphQLString,

            resolve: function () {
                return "Hello World";
            }
        },

        movie: {
            type: movieType,
            args: {
                id: { type: GraphQLInt }
            },
            resolve: function (source, args) {
                return _.find(movies, { id: args.id });
            }
        }
    }
});

exports.queryType = queryType;
```

From the above code, we can see that **movieType** is actually defined in **types.js.**

### Adding the Custom Type movieType

Create a file called **types.js**.

Add the following code into types.js

```js
const {
    GraphQLObjectType,
    GraphQLID,
    GraphQLString,
    GraphQLInt
} = require('graphql');

// Define Movie Type
movieType = new GraphQLObjectType({
    name: 'Movie',
    fields: {
        id: { type: GraphQLID },
        name: { type: GraphQLString },
        year: { type: GraphQLInt },
        directorId: { type: GraphQLID }

    }
});

exports.movieType = movieType;
```

It can be seen that **movieType** is created as a **GraphQLObjectType.**

It has 4 fields: **id, name, year and directorId**. The types for each of these fields are specified as well while adding them.

These fields come directly from the data. In this case, it will be from **movies** list.

### Adding the query and type for director endpoint

Like movie, even the director endpoint can be added.

In **query.js**, the director endpoint can be added as follows:

```js
director: {
            type: directorType,
            args: {
                id: { type: GraphQLInt }
            },
            resolve: function (source, args) {
                return _.find(directors, { id: args.id });
            }
        }
```

**directorType** can be added as follows in **types.js:**

```js
//Define Director Type
directorType = new GraphQLObjectType({
    name: 'Director',
    fields: {
        id: { type: GraphQLID },
        name: { type: GraphQLString },
        age: { type: GraphQLInt },
        movies: {
            type: new GraphQLList(movieType),
            resolve(source, args) {
                return _.filter(movies, { directorId: source.id });
            }

        }

    }
});
```

Wait a minute. The **directorType** is slightly different from **movieType**. Why is this?

Why is there a resolve function inside **directorType?** Previously we saw that resolve functions were present only in the **query…**

### The special nature of directorType

When the **director** endpoint is called we have to return the director details, as well as all the movies the director has directed.

The first 3 fields **id, name, age** in **directorType** are straightforward and come directly from the data (**directors** list).

The fourth field, **movies,** needs to contain the list of movies by this director.

For this, we are mentioning that the type of **movies** field is a **GraphQLList of movieType** (List of movies).

But how exactly will we find all the movies directed by this director?

For this, we have a **resolve** function inside the movies field. The inputs to this resolve function are **source** and **args**.

source will have the parent object details.

Lets say the fields **id =1, name = “Random” and age = 20** for a director. Then **source.id =1, source.name = “Random” and source.age = 20**

So in this example, resolve function finds out all the movies where directorId matches the Id of the required Director.

### Code

The Entire code for this application is available in this [GitHub repo](https://github.com/aditya-sridhar/graphql-with-nodejs)

### Testing the Application

Now let us test the application for different scenarios.

Run the application using `node server.js`.

Go to **localhost:5000/graphql** and try the following inputs.

### movie

Input:

```js
{
  movie(id: 1) {
    name
  }
}
```

Output:

```js
{
  "data": {
    "movie": {
      "name": "Movie 1"
    }
  }
}
```

From the above, we can see that the client can request exactly what it wants and GraphQL will ensure only those parameters are sent back. Here only **name** field is requested and only that is sent back by the server.

In `movie(id: 1)`, id is the input parameter. We are asking the server to send back the movie which has an id of 1.

Input:

```js
{
  movie(id: 3) {
    name
    id
    year
  }
}
```

Output:

```js
{
  "data": {
    "movie": {
      "name": "Movie 3",
      "id": "3",
      "year": 2016
    }
  }
}
```

In the above example **name, id and year** fields are requested. So the server sends back all of those fields.

### director

Input:

```js
{
  director(id: 1) {
    name
    id,
    age
  }
}
```

Output:

```js
{
  "data": {
    "director": {
      "name": "Director 1",
      "id": "1",
      "age": 20
    }
  }
}
```

Input:

```js
{
  director(id: 1) {
    name
    id,
    age,
    movies{
      name,
      year
    }
  }
}
```

Output:

```js
{
  "data": {
    "director": {
      "name": "Director 1",
      "id": "1",
      "age": 20,
      "movies": [
        {
          "name": "Movie 1",
          "year": 2018
        },
        {
          "name": "Movie 2",
          "year": 2017
        }
      ]
    }
  }
}
```

In the above example, we see the power of GraphQL. We indicate we want a director with id 1. Also, we indicate we want all the movies by this director. Both the director and movie fields are customizable and the client can request exactly what it wants.

Similarly, this can be extended to other fields and types. For example, we could run a query like **Find a director with id 1. For this director find all the movies. For each of the movie find the actors. For each actor get the top 5 rated movies** and so on. For this query, we need to specify the relationship between the types. Once we do that, the client can query any relationship it wants.

### Congrats ?

You now know the basic concepts of GraphQL.

You can check out the [documentation](https://graphql.github.io/learn/) to know more about GraphQL

### About the author

I love technology and follow the advancements in the field. I also like helping others with my technology knowledge.

Feel free to connect with me on my LinkedIn account [https://www.linkedin.com/in/aditya1811/](https://www.linkedin.com/in/aditya1811/)

You can also follow me on twitter [https://twitter.com/adityasridhar18](https://twitter.com/adityasridhar18)

My Website: [https://adityasridhar.com/](https://adityasridhar.com/)

Read more of my articles on my blog at [adityasridhar.com.](https://adityasridhar.com/)

