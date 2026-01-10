---
title: How to Build Full Stack Apps with a Simple Starter Kit Called Reno Expo
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-17T23:10:42.000Z'
originalURL: https://freecodecamp.org/news/reno-expo-full-stack-starter
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a34740569d1a4ca2431.jpg
tags:
- name: Apps
  slug: apps-tag
- name: Express
  slug: express
- name: full stack
  slug: full-stack
- name: node
  slug: node
- name: React
  slug: react
seo_title: null
seo_desc: 'By Jackson Bates

  Building any new project from scratch can be intimidating. There''s a lot to decide
  before you can even start coding to test out your idea.

  How are you building the front end? Plain CSS, or a framework? Vanilla HTML and
  JS, or a frame...'
---

By Jackson Bates

Building any new project from scratch can be intimidating. There's a lot to decide before you can even start coding to test out your idea.

How are you building the front end? Plain CSS, or a framework? Vanilla HTML and JS, or a framework or library such as Vue, React, Angular, or Svelte?

What back end language will you use? JavaScript, Ruby, PHP, Python or something else? Maybe 'serverless'?

What about the database? Relational? MySQL, Postgresql? NoSQL? Mongo? Maybe something 'easy' like Firebase instead?

How will you handle authentication? Maybe a Passport integration that just bundles in a Facebook, Google, Github and LinkedIn login screen?

Whenever I have a cool idea for a little app I want to build myself, I'm always exhausted by the range of options and decisions to be made.

So I took some time to think about my ideal stack, including authentication and deployment considerations, and bundled it all up into one reasonably easy to setup package: Reno Expo.

# What is Reno Expo?

Reno Expo stands for React, NodeJS, Express, and Postgresql. It also uses Sequelize as the ORM for the database.

At its core it is a very simple Express app that has a Create React App bundled for the front end. It is designed to be deployed to Heroku and has a very simple interface for registering new users and logging in, using JWT for authentication.

Apart from that, it is a completely blank slate. I've intentionally left it pretty empty in terms of CSS styling, so I can plug in any style libraries I want or write my own CSS as required.

Aside from the completely raw version of Reno Expo, I've also made a freeCodeCamp project, the Personal Library, using this stack. It serves as an example of how to integrate a CSS framework, Ant Design in this instance, and also provides some examples of extending the database with Sequelize migrations.

## Where can I get it?

The code for the two apps can be found here:

* [Reno Expo Starter Kit](https://github.com/JacksonBates/reno-expo)
* [Personal Library, built with Reno Expo](https://github.com/JacksonBates/reno-expo-books)

Each has a detailed README.md file, but I'll also explain how to get started with both, and explain how the latter app builds upon the starter kit in this article.

## What do the apps look like?

Examples for both apps can be found here:

* [Reno Expo, example hosted on Heroku](http://renoexpo.herokuapp.com/)
* [Personal Library, hosted on Heroku](https://reno-expo-books.herokuapp.com/)

The starter kit is hideous, frankly. As I stated earlier, it has minimal styling - and I wasn't kidding. The Personal Library shows how one might integrate a CSS framework to get some easy styling wins with minimal effort.

## Getting Started with Reno Expo

To work with Reno Expo you will need the following installed on your local computer: [git](https://git-scm.com/), [Node](https://nodejs.org/en/download/), npm (bundled with your Node download), and [Postgresql](https://www.postgresql.org/).

Use the latest versions of each if you are starting from scratch, but if you already have other versions of these on you system they may well work just fine. 

For the record, I've been developing with these versions: Node 8.16, npm 6.14 and Postgres 10, and my Heroku deployments have been the latest stable versions of all these. 

If you run into problems using different versions, either using these versions or try looking for differences in the appropriate change logs to help you get unstuck.

Your Postgres installation will also require a valid user with database creation privileges. Setting this up is outside the scope of this article, but you can find the relevant guides for your environment with an online search for "getting started with postgres windows/mac/ubuntu" etc.

### Installing the Starter Kit

To initialise the starter kit, we will use two terminals. Later, I'll share a trick for spinning up your development environment from a single terminal, but for now we'll keep the front end and back end separated.

In terminal one, from the directory in which you wish to create your new app:

`git clone git@github.com:JacksonBates/reno-expo.git`

Then navigate to that new folder: `cd reno-expo`

Make a copy of the .env file: `cp .env.example .env`

You will need to adjust the development variables in the new .env file:

```sh
DEVELOPMENT_DATABASE=database_development
DEVELOPMENT_DATABASE_USERNAME=sequelize
DEVELOPMENT_DATABASE_PASSWORD=password
```

The development database can be whatever you like, but the username and password will have to match whatever you have configured for your local Postgres installation.

Now install the npm packages for the back end: `npm i`

Next we will create the database using Sequelize. Note, if your Postgres installation isn't set up properly, this is the first bit that will fall over...

`npx sequelize-cli db:create`

This will create the database with the name you set in your .env file.

Now we can create the table for our users:

`npx sequelize-cli db:migrate`

If this works, you should see some terminal output such as:

```sh
== 20200606113054-create-user: migrating =======
== 20200606113054-create-user: migrated (0.074s)
```

If all this has worked, you can now start the back end server with `npm start`.

Setting up the front end should be more simple. In your second terminal navigate to the client folder: `reno-expo/client`

Install the node modules: `npm i`

Now run the React app with `npm start`.

### Single terminal Launch

If everything initialises properly, in future you can easily spin up both the React app and Express server with one command from a single terminal:

`npm run dev`

### Check that it works

In your browser of choice, visit localhost:3000 and you should see a very basic 'Home' page and some links to an Admin and Login page.

Admin should be locked until you log in.

Login will require you to create a user account first. Click 'I don't have an account' and make one via the registration form. You can now log in and test your access to the Admin page.

If all is working, you can begin to develop your app!

## Building something more substantial with Reno Expo

To create the Personal Library there were 3 main things to do: 

1. install and implement the Ant Design CSS framework
2. create the new front end routes / views
3. extend the api with new database models and controllers

After installing Ant Design with `npm i antd` I added the following line to the existing App.css file in the `client/styles` folder: `@import"~antd/dist/antd.css";`

This ensures the Ant Design styling will be available throughout the app.

The repo for the Personal Library contains all the amendments, but here are some examples of patterns you could use. Of course, you could roll your own CSS, or use other frameworks such as Material-UI, Bootstrap or others, what follows is just illustrative.

### Implementing a layout

```js
import React from "react";
import { Layout, Menu } from "antd";
import { Link } from "react-router-dom";
import { useAuth } from "../../context/auth";

const { Content, Sider, Footer } = Layout;

export default function AppLayout(props) {
  const { setAuthTokens } = useAuth();

  const logout = (e) => {
    e.preventDefault();
    setAuthTokens();
    localStorage.removeItem("tokens");
  };

  return (
    <Layout>
      <Sider breakpoint="md" collapsedWidth="0">
        <Menu theme="dark" mode="inline">
          <Menu.Item key="1">
            <Link to={"/"}>
              <span className="nav-text">Home</span>
            </Link>
          </Menu.Item>
          <Menu.Item key="2">
            <Link to={"/personal"}>
              <span className="nav-text">Personal Library</span>
            </Link>
          </Menu.Item>
          <Menu.Item key="3">
            <Link to={"/public"}>
              <span className="nav-text">Public Library</span>
            </Link>
          </Menu.Item>
          <Menu.Item key="4">
            <Link to={"/login"} onClick={logout}>
              <span className="nav-text">Log out</span>
            </Link>
          </Menu.Item>
        </Menu>
      </Sider>
      <Layout style={{ minHeight: "100vh" }}>
        <Content style={{ margin: "24px 16px 0" }}>
          <div style={{ padding: 24, background: "#fff", minHeight: "80vh" }}>
            {props.children}
          </div>
        </Content>
        <Footer>Reno Expo Books</Footer>
      </Layout>
    </Layout>
  );
}

```

Apart from a small function handling the auth token, the rest of this uses the components supplied by Ant Design for creating an app with a persistent side bar for navigation, and dynamically rendered content depending on the active component.

Where does the active component get loaded?

```js
import React from "react";
import { Route } from "react-router-dom";
import { AppLayout } from "../layouts";

export default function PublicRoute({ children, ...rest }) {
  return (
    <Route {...rest}>
      <AppLayout>{children}</AppLayout>
    </Route>
  );
}
```

Above we have an example of the PublicRoute component. There are some other route components I use, but understanding them should be straightforward enough based on this one.

Our PublicRoute is a React-Router `<Route>` wrapping the layout from above. 

App.js shows examples of these Public Routes being used, for example:

```js
<PublicRoute exact path="/">
  <Home />
</PublicRoute>
      
```

So in the first two files we can see a reference to `children`.

`children` is a built in prop in React that references the child components that are nested in parent components.

In the above examples we see the `<Home>` component as a child of the `PublicRoute`. In the PublicRoute.js file we see the reference to children, both in the props and being passed directly to the `<AppLayout>` component. And finally in the AppLayout.js the `<Content>` component also contains the children. In all these cases, children refers to that `<Home>` component passed from App.js.

In practice, this means any of the components passed from App.js on public or private routes will be rendered into the content area on our Layout, leaving the navigation sidebar untouched.

Other files in the client folder should give ample examples of how things like the Login form can be replaced with the Ant Design framework after some small modifications.

### Making changes to the back end

The other main thing to develop when working with Reno Expo is the api itself - after all, it's useful being able to register a user and have them log in, but most apps require more than that to be really useful.

For the purposes of my version of the Personal Library we needed to implement a number of new api endpoints, and create some new database tables to store book and comment data.

It's worth highlighting here that in these examples I'm working backwards. Normally I'd create the database migrations and models first, then build the controller methods and api routes afterwards. I present them 'backwards' here so we can follow the logic from our goal back through how it was implemented piece by piece.

The file `reno-expo-books/app/router/router.js` contains all the routes for the project, but I'll share two examples here for illustration.

```js
// Public route
app.get("/api/books", booksController.getBooks);


// Private route
app.get(
    "/api/user/books",
    [authJwt.verifyToken],
    booksController.getUserBooks
  );
  
```

Adding public routes is simple enough, we just need to define the http method, the api endpoint and the controller method that will handle the request, e.g. a GET request, to `api/books` handled by the booksController `getBooks` method.

The JWT auth that we already have available from the Reno Expo starter makes the private routes pretty simple too. All we need to do is include the middleware for verifying the token, `[authJwt.verifyToken]` in the example above.

The controllers for these endpoints, i.e. the code that processes the requests, are also reasonably straightforward, although using Sequelize for the first time can have a bit of a learning curve.

Here's an example of the public 'getBooks' method referenced above:

```js
const db = require("../../models/index");
const Sequelize = require("sequelize");
const Book = db.Book;
const BookComment = db.BookComment;

// Public routes

exports.getBooks = (req, res) => {
  Book.findAll({
    where: { userId: null },
    attributes: {
      include: [
        [
          Sequelize.fn("COUNT", Sequelize.col("BookComments.id")),
          "commentcount",
        ],
      ],
      exclude: ["createdAt", "updatedAt"],
    },
    include: {
      model: BookComment,
      attributes: [],
    },
    group: ["Book.id"],
  })
    .then((data) => res.status(200).json(data))
    .catch((error) => res.send(error));
};

```

The imports at the top of the file provide the database models and the Sequelize library.

The `getBooks` method looks complicated, but it is made up of a few relatively simple parts.

Firstly we call the `Book` model. The model is an ORM representation of the books table - we'll look at how we create that table soon.

Sequelize, like most ORMs, provides not only a schema or description of the table, but also methods that can be called upon the model. In this case we call `Book.findAll({...})`, which will return all the books it can find that match particular parameters we pass to it.

In this particular instance I wanted to receive something like this:

```json
[
  {
    "id": 1,
    "title": "The Hobbit",
    "commentcount": 3
  },
  {
    "id": 2,
    "title": "The Lord of the Rings",
    "commentcount": 2
  }
]
```

In the findAll method, first we pass the `where` parameters. If you are familiar with SQL, it should be pretty clear what this does. In the example above we want all books where the userId is null. This is because we only want to return the public books from this controller, so only those with no user attached to them.

Next, the `attributes` describes the shape of the response, or the data we expect back. The exclude section is easier to understand, so I'll explain it first. The books table has columns for the created_at and updated_at timestamps for each record. Since we don't want these in our json response, we can omit them explicitly in the exclude section.

Our include portion of the attributes is more complicated. In raw SQL we would count the number of associated comments like this:

```sql
SELECT "Books"."id", "Books"."title", COUNT("BookComments"."id") AS "commentcount"
FROM "Books"
JOIN "BookComments" ON "BookComments"."bookId" = "Books"."id"
GROUP BY "Books"."id";
```

The SQL COUNT function counts all the records in the BookComments.id column, and the GROUP BY function limits the counted comments to each book, by ID.

It's worth pointing out that commentcount is not a column on the books table, rather it is a calculated column derived from the thing we ask the database to count for us.

Sequelize gives us access to the count function via its library.

The relevant function is included in the attributes above like this:

```js
[Sequelize.fn("COUNT", Sequelize.col("BookComments.id")),"commentcount"]

```

I.e. "Call the Sequelize function 'COUNT', count the columns for BookComments.id, and name the generated column 'commentcount'

This provides our count function just like in the SQL version. All that's left is to include the `group: ['Book.id']` as an extra parameter of the findAll method on the Book model.

The other part you may have noticed in the findAll method parameters is this:

```js
include: {
  model: BookComment,
  attributes: [],
},
```

That's right, _another_ include. Notice that this one is not nested in the attributes, but is its peer. This include acts much the same way as the JOIN statement in the SQL above. It means we want to include the BookComment model, but we don't need to add any attributes since we don't want to reference any of the columns it has directly - we just use it in the count function.

### Making changes to the database

The final thing we need to understand to be productive with Sequelize is the migrations for making changes to the database.

Migrations can be thought of as source control for your database.

While you can amend a database directly by creating new tables, adding columns, introducing constraints, changing data types or whatever else, using migrations allows you to make experimental changes with the ability to roll them back easily, and be able to share your development on a database with other people that do not have to struggle with keeping their local databases, and prod, in sync.

Migrations are essentially code that tell your database how to change, and how to undo the change that was introduced, should that be necessary.

Here is the migration for creating the books table:

```js
'use strict';
module.exports = {
  up: (queryInterface, Sequelize) => {
    return queryInterface.createTable('Books', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER
      },
      title: {
        type: Sequelize.STRING
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE
      }
    });
  },
  down: (queryInterface, Sequelize) => {
    return queryInterface.dropTable('Books');
  }
};
```

This migration is a module that exports two functions: `up` and `down`

The `up` function makes the changes, while the `down` function undoes any of the changes that were introduced.

So here we see that up creates a table called 'Books' with the columns id, title, created_at and updated_at. Each column has some associated qualities as well, such as data type, and whether it can contain a null value, for example.

The down function simply drops the table.

I won't share all of the next migration, i.e. the one for creating the Book Comment table, but I will show a snippet from it's up function that defines the bookId column:

```js
bookId: {
  type: Sequelize.INTEGER,
  onDelete: "CASCADE",
  references: {
    model: { tableName: "Books" },
    key: "id",
  },
  allowNull: false,
},
 
```

The interesting things to note here are the `onDelete` property, which is set to "CASCADE" and the `references` property which links the books table via the id column. This sets up the relationship between a book and its comments. The onDelete property tells the database what to do if a book is deleted: that deletion action should cascade to all associated comments. That is, if I delete 'The Hobbit' all the comments relating to 'The Hobbit' get deleted too.

The last thing to be aware of is that these migrations are also supported by models. The BookComment model looks like this:

```js
"use strict";
module.exports = (sequelize, DataTypes) => {
  const BookComment = sequelize.define(
    "BookComment",
    {
      comment: DataTypes.TEXT,
      bookId: {
        type: DataTypes.INTEGER,
        references: {
          model: "Books",
          key: "id",
        },
      },
    },
    {}
  );
  BookComment.associate = function (models) {
    // associations can be defined here
    BookComment.belongsTo(models.Book, {
      foreignKey: "bookId",
    });
  };
  return BookComment;
};

```

You will notice some similarities between this and the migration. It has two parts, the Model definition and the model associations. These help reinforce the relationship between the various tables as necessary.

To create tables from scratch, you can use a command like this:

`npx sequelize-cli model:generate --name Post --attributes post:text`

This will automatically generate a model skeleton and a migration skeleton for a `posts` table with the column 'post'. You can then fill in the migration and model with whatever other column details or associations are relevant.

If you just want to amend an existing table, for example, to change a data type, or add a column, you can use a command to only generate a migration:

`npx sequelize-cli migration:generate --name add-userId-to-posts`

You can then make the changes to the existing model and new migration file as necessary.

### Applying database changes

Simply writing the code to update the database is not enough, you also need to run the migrations for each database your code works on - i.e. your local dev machine, maybe your staging server if you have one, and also your production server.

The command for running these is:

`npx sequelize-cli db:migrate`

You can roll back migrations as well: 

`npx sequelize-cli db:migrate:undo`

##  Happy coding!

That's it! As I mentioned above, I personally deploy everything I make with these to Heroku, and there are detailed instructions for the particulars of deploying them to Heroku in the README.md of Reno Expo. This also includes the commands for running migrations on Heroku's server.

There is a lot to take in here. But if you fundamentally understand Express and React, and are willing to dig in to the Sequelize docs when needed, you can build pretty much anything you can imagine that benefits from a relational database using this starter kit.

It's not quite as fully featured as a proper MVC framework like Rails, Laravel, Sails, or Nest, but I happen to like that there is less cruft and less `magic` hidden in the internals of this. It is, after all, just a Create React App bundled with a light server and an ORM package. The rest is up to you.

---

If you made it to the end of this article, and especially if you build anything with Reno Expo, I would love to hear from you. You can contact me on Twitter: [@JacksonBates](https://twitter.com/JacksonBates)

