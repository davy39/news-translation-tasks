---
title: How to Deploy a MERN Application to Heroku Using MongoDB Atlas
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-21T14:27:17.000Z'
originalURL: https://freecodecamp.org/news/deploying-a-mern-application-using-mongodb-atlas-to-heroku
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/1_qgxaya.png
tags:
- name: Express
  slug: express
- name: JavaScript
  slug: javascript
- name: MongoDB
  slug: mongodb
- name: Node.js
  slug: nodejs
- name: prototype
  slug: prototype
- name: React
  slug: react
seo_title: null
seo_desc: 'By Dillion Megida

  Introduction to MERN

  In this article, we''ll be building and deploying an application built with the
  MERN stack to Heroku.

  MERN, which stands for MongoDB, Express, React, and Node.js, is a popular tech stack
  used in building web appl...'
---

By Dillion Megida

## Introduction to MERN

In this article, we'll be building and deploying an application built with the MERN stack to Heroku.

MERN, which stands for MongoDB, Express, React, and Node.js, is a popular tech stack used in building web applications. It involves frontend work (with React), backend work (with Express and NodeJS) and a database (with MongoDB).

[Heroku](https://www.heroku.com/), on the other hand, is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

For the database, we'll be using MongoDB Atlas, which is a global cloud database service for modern applications. This is more secure than the MongoDB installed locally on our server and it also gives us room for more resources on our servers.

For the frontend we'll build a simple React app which makes POST requests to an API to add a user, and can also make GET requests to get all users.

_You can skip to any step with the table of contents listed below._

## Table of contents

* [Introduction to MERN](#heading-introduction-to-mern)
* [Let's Start Building](#heading-lets-start-building)
* [Building the React App](#heading-building-the-react-app)
* [Creating the Backend](#heading-creating-the-backend)
* [Connect the MongoDB Atlas Database](#heading-connect-the-mongodb-atlas-database)
* [Calling APIs on the Frontend](#heading-calling-apis-on-the-frontend)
* [Deploying to Heroku](#heading-deploying-to-heroku)
* [Create a Heroku app](#heading-create-a-heroku-app)
* [Configure package.json](#heading-configure-packagejson)
* [Wrap up](#heading-wrap-up)

## Let's Start Building

### Building the React App

**Note:** Before we begin with our project, `node` must be installed on your computer. `node` also provides us with `npm`, which is used for installing packages.

#### Install `create-react-app`

`create-react-app` is used to create a starter React app.

If you do not have `create-react-app` installed, type the following in the command line:

```shell
npm i create-react-app -g

```

The `-g` flag installs the package globally.

#### Create the project directory

```shell
create-react-app my-project
cd my-project

```

The above creates a directory 'my-project', and installs dependencies which will be used in the React starter app. After it's finished installing, the second command changes to the project directory.

#### Start the app and make necessary edits

```shell
npm start

```

The command above starts the React application, which gives you a URL where you preview the project. You can then make necessary edits like changing images or text.

#### Install axios

```shell
npm i axios --save

```

`axios` is a JavaScript library used to make HTTP requests easier. It'll be used to send requests from the frontend (React) to the APIs provided by the backend.

### Creating the Backend

The backend manages the APIs, handles requests, and also connects to the database.

#### Install the backend packages

```shell
npm i express cors mongoose body-parser --save

```

1. `express`: "Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web applications" - Express [Documentation](http://expressjs.com/)
2. `cors`: "CORS is a node.js package for providing a Connect/Express middleware that can be used to enable CORS with various options" - [cors Documentation](https://www.npmjs.com/package/cors)
3. `mongoose`: "Mongoose is a MongoDB object modeling tool designed to work in an asynchronous environment. Mongoose supports both promises and callbacks" - [Mongoose Documentation](https://www.npmjs.com/package/mongoose)
4. `body-parser`: "Node.js body parsing middleware." - [body-parser Documentation](https://www.npmjs.com/package/mongoose)

#### Create the backend folder

```shell
mkdir backend
cd backend

```

#### Configure the backend

##### Create an entry point `server.js`

First, create a `server.js` file, which will be the entry point to the backend.

```shell
touch server.js

```

In `server.js`, type the following:

```js
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const path = require('path')
const app = express();
require('./database');
-----
app.use(bodyParser.json());
app.use(cors());
-----
// API
const users = require('/api/users');
app.use('/api/users', users);
-----
app.use(express.static(path.join(__dirname, '../build')))
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, '../build'))
})
-----
const port = process.env.PORT || 5000;
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});

```

`express.static` delivers static files which are the ones built when `npm run build` is run on a React project. Remember, the built file is in the build folder.

From our configuration, any request sent to `/api/users` will be sent to `users` API which we're about to configure.

##### Configure the `users` API

```shell
mkdir api
touch api/users.js

```

In `api/users.js`, add the following:

```js
const express = require('express');
const router = express.Router()
-----
const User = require('../models/User');
-----
router.get('/', (req, res) => {
    User.find()
        .then(users => res.json(users))
        .catch(err => console.log(err))
})
-----
router.post('/', (req, res) => {
    const { name, email } = req.body;
    const newUser = new User({
        name: name, email: email
    })
    newUser.save()
        .then(() => res.json({
            message: "Created account successfully"
        }))
        .catch(err => res.status(400).json({
            "error": err,
            "message": "Error creating account"
        }))
})
module.exports = router 

```

In the code above, we create a GET and POST request handler which fetches all users and posts users. Fetching and adding a user to the database is aided by the `User` model we'll create.

##### Create `User` model

```shell
mkdir models
touch models/user.js

```

In `models/user.js`, add the following:

```js
const mongoose = require('mongoose');
const Schema = mongoose.Schema;
-----
const userSchema = new Schema({
    name: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true
    }
})
module.exports = mongoose.model("User", userSchema, "users")

```

In the code above, a schema is created for the user which contains the fields of the user. At the end of the file, the model ("User") is exported with the schema and the collection ("users").

##### Connect the MongoDB Atlas Database

According to [the docs](https://www.mongodb.com/cloud/atlas), "MongoDB Atlas is the global cloud database service for modern applications."

First we need to register on Mongo cloud. Go through [this documentation](https://docs.atlas.mongodb.com/getting-started/) to create an Atlas account and create your cluster.

One thing worth noting is **whitelisting your connection IP address**. If you ignore this step, you won't have access to the cluster, so pay attention to that step.

The cluster is a small server which will manage our collections (similar to tables in SQL databases). To connect your backend to the cluster, create a file `database.js`, which as you can see is required in `server.js`. Then enter the following:

```js
const mongoose = require('mongoose');
const connection = "mongodb+srv://username:<password>@<cluster>/<database>?retryWrites=true&w=majority";
mongoose.connect(connection,{ useNewUrlParser: true, useUnifiedTopology: true, useFindAndModify: false})
    .then(() => console.log("Database Connected Successfully"))
    .catch(err => console.log(err));

```

In the `connection` variable, enter your `username` (for MongoDB cloud), your `password` (cluster password), your `cluster` (address for your cluster) and the `database` (name of your database). All these can be easily discovered if you followed the documentation.

## Calling APIs on the Frontend

All APIs will be available on `localhost:5000` locally, just as we set up in `server.js`. When deployed to Heroku, the server will use the port provided by the server (`process.env.PORT`).

To make things easier, React allows us to specify a proxy which requests will be sent to.

Open `package.json` and just before the last curly brace, add the following:

```json
"proxy": "http://localhost:5000"

```

This way we can directly send requests to `api/users`. And when our site is deployed and built, the default port of our application will be used with the same API.

Open `App.js` for React and add the following:

```js
import React, {useState, useEffect} from 'react'
import axios from 'axios';
-----
const App = function () {
	const [users, setUsers] = useState(null);

	const [username, setUsername] = useState("");
	const [email, setEmail] = useState("");
	useEffect(() => {
		axios
			.get("/api/users")
			.then((users) => setUsers(users))
			.catch((err) => console.log(err));
	}, []);

	function submitForm() {
		if (username === "") {
			alert("Please fill the username field");
			return;
		}
		if (email === "") {
			alert("Please fill the email field");
			return;
		}
		axios
			.post("/api/users", {
				username: username,
				email: email,
			})
			.then(function () {
				alert("Account created successfully");
				window.location.reload();
			})
			.catch(function () {
				alert("Could not creat account. Please try again");
			});
	}
	return (
		<>
			<h1>My Project</h1>
			{users === null ? (
				<p>Loading...</p>
			) : users.length === 0 ? (
				<p>No user available</p>
			) : (
				<>
					<h2>Available Users</h2>
					<ol>
						{users.map((user, index) => (
							<li key={index}>
								Name: {user.name} - Email: {user.email}
							</li>
						))}
					</ol>
				</>
			)}

			<form onSubmit={submitForm}>
				<input
					onChange={(e) => setUsername(e.target.value)}
					type="text"
					placeholder="Enter your username"
				/>
				<input
					onChange={(e) => setEmail(e.target.value)}
					type="text"
					placeholder="Enter your email address"
				/>
				<input type="submit" />
			</form>
		</>
	);
};
export default App

```

The `useState` and `useEffect` hooks are used to handle state and `sideEffects`. What is basically happening is that the first state of users is `null` and 'Loading...' is showed in the browser. 

In `useEffect`, `[]` is used to specify that at the `componentDidMount` stage (when the component is mounted), make an Axios request to the API which is running on `localhost:5000`. If it gets the result and there is no user, 'No user available' is displayed. Otherwise a numbered list of the users is displayed.

If you want to learn more about `useState` and `useEffect`, check out this article - [What the heck is React Hooks?](https://blog.soshace.com/what-the-heck-is-react-hooks/)

With the form available, a POST request can be made to post a new user. The state of the inputs are controlled and sent to the API at `localhost:5000` on submission. Afterwards, the page is refreshed and the new user is displayed.

## Deploying to Heroku

To deploy your application to Heroku, you must have a Heroku account. 

Go to [their page](https://www.heroku.com/) to create an account. Then go through [their documention](https://devcenter.heroku.com/articles/creating-apps) on how to create a Heroku app. Also check out [the documentation](https://devcenter.heroku.com/articles/heroku-cli) on Heroku CLI.

### Create a Heroku App

First, login to Heroku:

```shell
heroku login

```

This will redirect you to a URL in the browser where you can log in. Once you're finished you can continue in the terminal.

In the same React project directory, run the following:

```shell
heroku create

```

This will create a Heroku application and also give you the URL to access the application.

### Configure package.json

Heroku uses your package.json file to know which scripts to run and which dependencies to install for your project to run successfully.

In your `package.json` file, add the following:

```json
{
    ...
    "scripts": {
        ...
        "start": "node backend/server.js",
        "heroku-postbuild": "NPM_CONFIG_PRODUCTION=false npm install npm && run build"
    },
    ...
    "engines": {
        "node": "10.16.0"
    }
}

```

Heroku runs a post build, which as you can see installs your dependencies and runs a build of your React project. Then it starts your project with the `start` script which basically starts your server. After that, your project should work fine.

`engines` specifies the versions of engines like `node` and `npm` to install.

#### Push to Heroku

```shell
git push heroku master

```

This pushes your code to Heroku. Remember to include unnecessary files in `.gitignore`.

After few seconds your site will be ready. If there are any errors, you can check your terminal or go to your dashboard in the browser to view the build logs.

Now you can preview your site at the URL Heroku sent when you ran `heroku create`.

That's all there is to it. Glad you read this far.

## Wrap Up

Of course there is more to MERN stack applications.

This article did not go as deep as authentications, login, sessions, and all that. It just covered how to deploy MERN stack applications to Heroku and work with MongoDB Atlas.

You can find other articles like this on my blog - [dillionmegida.com](https://dillionmegida.com)

Thanks for reading.

