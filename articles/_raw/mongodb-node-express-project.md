---
title: Learn Node + MongoDB by Creating a URL Shortener Project
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-18T21:47:03.000Z'
originalURL: https://freecodecamp.org/news/mongodb-node-express-project
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/urlshortener.jpg
tags:
- name: MongoDB
  slug: mongodb
- name: node
  slug: node
- name: projects
  slug: projects
seo_title: null
seo_desc: 'By Mehul Mohan

  If you want to learn about something, what better way than by building a project
  around the thing you want to learn?

  In this blog post, we''ll learn about MongoDB, Mongoose, Node, and other tech by
  building a simple URL shortener applic...'
---

By Mehul Mohan

If you want to learn about something, what better way than by building a project around the thing you want to learn?

In this blog post, we'll learn about MongoDB, Mongoose, Node, and other tech by building a simple URL shortener application. 

URL shorteners are everywhere, from links you share on twitter to popular services like bit.ly. But have you ever wondered how you could create a quick URL shortener for yourself?

So we'll go through the hands-on practice of building a URL shortener with MongoDB as our backend solution. This project will give you confidence in your knowledge and solidify each concept you learn. Let's get started.

## Introduction to the project

We will be using this free [URL shortener classroom](https://codedamn.com/practice/url-shortener-node) from codedamn to get hands-on practice and evaluate our progress as we proceed.

We will be using the following technologies:

* Mongoose as the ORM
* MongoDB as the backend database
* Node.js as the backend
* A simple embedded JS file as the frontend

We will complete this project in 7 steps, which take you through from the beginning to completion. Let's start the labs now.

## Part 1: Setting up the Express server

First let's set up our Node server. We'll use Express as the framework for this part as it is easy to work with. Here's the [link to this part](https://codedamn.com/practice/url-shortener-node/36280bc2-36b5-4f4e-8976-ed4687dc7cbd).

We can see this is a reasonably easy exercise. The only two challenges we have to overcome are the following:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/i1.png)

The solution could look like this:

```js
// Initialize express server on PORT 1337
const express = require('express')
const app = express()

app.get('/', (req, res) => {
	res.send('Hello World! - from codedamn')
})

app.get('/short', (req, res) => {
	res.send('Hello from short')
})

app.listen(process.env.PUBLIC_PORT, () => {
	console.log('Server started')
})
```

Simple and easy. We create another GET route using `app.get`, and it should get the job done.

## Part 2: Setting up our view engine

Now that we're familiar with Express installation, let's take a look at the `.ejs` template we have. Here's the [link to this part](https://codedamn.com/practice/url-shortener-node/0eb7b0b0-473e-4a83-9589-8ea13467972f).

The EJS engine allows you to pass variables down with the Node.js code to your HTML and iterate or display them before you send an actual response to the server. 

Take a quick look at the `views/index.ejs` file. It'll look similar to how a regular HTML file looks, except that you can use variables. 

Here's our current `index.js` file:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/i2.png)

Now, you can see that in the `index.js` file we have the line `app.set('view engine', 'ejs')` . It tells Express to use `ejs` as its default templating engine.

Finally, see that we are using res.render and only passing the file's name, not the full path. This is because Express will automatically look inside the views folder for available `.ejs` templates. 

We pass variables as the second argument, which we can then access in the EJS file. We'll use this file later, but for now let's go through a quick challenge.

To complete this challenge, we just need to change the name from `Mehul` to anything else. 

To pass this challenge, view the `index.ejs` file first and then update your name to anything else you like. Here's a good solution:

```js
const express = require('express')
const app = express()

app.set('view engine', 'ejs')

app.get('/', (req, res) => {
	res.render('index', { myVariable: 'My name is John!' })
})

app.listen(process.env.PUBLIC_PORT, () => {
	console.log('Server started')
})
```

## Part 3: Setting up MongoDB

Now that we have a bit of frontend and backend understanding, let's go ahead and setup MongoDB. Here's the [link to this part](https://codedamn.com/practice/url-shortener-node/523eaae7-27ff-47fe-bfdc-67a65dfd5711).

We'll use Mongoose for connecting to MongoDB. Mongoose is an ORM for MongoDB. 

Simply speaking, MongoDB is a very _loose_ database, and it allows all sorts of operations on anything. 

While it is good for unstructured data, most of the time we are actually aware of what the data will be (like user records or payment records). Thus, we can define a _schema_ for MongoDB using Mongoose. This makes a lot of functions easy for us.

For example, once we have a schema, we can be assured that data validation and any necessary checks will be handled by Mongoose automatically. Mongoose also gives us a bunch of helper functions to make our lives easier. Let’s now set it up.

To complete this part, we have to take care of the following points:

* Mongoose NPM package has already been installed for you. You can directly `require` it.
* Connect to the `mongodb://localhost:27017/codedamn` URL using the `mongoose.connect` method.

Here's our current index.js file:

```js
const express = require('express')
const app = express()
const mongoose = require('mongoose')

app.set('view engine', 'ejs')

app.get('/', (req, res) => {
	res.render('index')
})

app.post('/short', (req, res) => {
	const db = mongoose.connection.db
	// insert the record in 'test' collection

	res.json({ ok: 1 })
})

// Setup your mongodb connection here
// mongoose.connect(...)

// Wait for mongodb connection before server starts
app.listen(process.env.PUBLIC_PORT, () => {
	console.log('Server started')
})

```

Let's fill in the appropriate placeholders with the relevant code:

```js
const express = require('express')
const app = express()
const mongoose = require('mongoose')

app.set('view engine', 'ejs')

app.get('/', (req, res) => {
	res.render('index')
})

app.post('/short', (req, res) => {
	const db = mongoose.connection.db
	// insert the record in 'test' collection
	db.collection('test').insertOne({ testCompleted: 1 })

	res.json({ ok: 1 })
})

// Setup your mongodb connection here
mongoose.connect('mongodb://localhost/codedamn', {
	useNewUrlParser: true,
	useUnifiedTopology: true
})
mongoose.connection.on('open', () => {
	// Wait for mongodb connection before server starts
	app.listen(process.env.PUBLIC_PORT, () => {
		console.log('Server started')
	})
})
```

Notice how we start our HTTP server only when our connection with MongoDB is open. This is fine because we don't want users to hit our routes before our database is ready.

We finally use the `db.collection` method here to insert a simple record, but we'll have a better way soon to interact with the database using Mongoose models.

## Part 4: Setting up a Mongoose schema

Now that we have had our hands-on experience with the MongoDB implementation in the last section, let’s draw out the schema for our URL shortener. Here's the [link for this part](https://codedamn.com/practice/url-shortener-node/a64e6946-a6ea-4ba7-8357-fe000c61658c).

A Mongoose schema allows us to interact with the Mongo collections in an abstract way. Mongoose's rich documents also expose helper functions like `.save` which are enough to perform a full DB query to update changes in your document.

Here's how our schema for the URL shortener will look:

```js
const mongoose = require('mongoose')
const shortId = require('shortid')

const shortUrlSchema = new mongoose.Schema({
  full: {
    type: String,
    required: true
  },
  short: {
    type: String,
    required: true,
    default: shortId.generate
  },
  clicks: {
    type: Number,
    required: true,
    default: 0
  }
})

module.exports = mongoose.model('ShortUrl', shortUrlSchema)
```

We'll store this file in the `models/url.js` file. Once we have the schema, we can pass this part of the exercise. We have to do the following two things:

1. Create this model in the `models/url.js` file. (We did that.)
2. A POST request to `/short` should add something to the database to this model.

In order to do that, we can generate a new record using the following code:

```js
app.post('/short', async (req, res) => {
	// insert the record using the model
	const record = new ShortURL({
		full: 'test'
	})
	await record.save()
	res.json({ ok: 1 })
})
```

You'll see that we can omit the `clicks` and `short` field because they already have a default value in the schema. This means Mongoose will populate them automatically when the query runs.

Our final `index.js` file to pass this challenge should look like this:

```
const express = require('express')
const app = express()
const mongoose = require('mongoose')
// import the model here
const ShortURL = require('./models/url')

app.set('view engine', 'ejs')

app.get('/', (req, res) => {
	res.render('index', { myVariable: 'My name is John!' })
})

app.post('/short', async (req, res) => {
	// insert the record using the model
	const record = new ShortURL({
		full: 'test'
	})
	await record.save()
	res.json({ ok: 1 })
})

// Setup your mongodb connection here
mongoose.connect('mongodb://localhost/codedamn')

mongoose.connection.on('open', () => {
	// Wait for mongodb connection before server starts
	app.listen(process.env.PUBLIC_PORT, () => {
		console.log('Server started')
	})
})
```

## Part 5: Linking the frontend, backend, + MongoDB

Now that we have a handle on the backend part, let’s get back to the frontend and setup our webpage. There we can use the **Shrink** button to actually add some records to the database. Here's the link to [this part](https://codedamn.com/practice/url-shortener-node/bfd9d2d7-e925-4ade-9d4b-f9e23124cc07).

If you look inside the `views/index.ejs` file, you’ll see that we have already passed the form data on the backend `/short` route. But right now we are not grabbing it.

* You can see that there’s a new line called `app.use(express.urlencoded({ extended: false }))` on line 8, which allows us to read the response of the user from the form.
* In the `index.ejs` file, you can see that we set `name=”fullURL”` which is how we can receive the URL on the backend.

Here's our `index.ejs` file:

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<meta http-equiv="X-UA-Compatible" content="ie=edge" />
		<link
			rel="stylesheet"
			href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
		/>
		<title>codedamn URL Shortner Project</title>
	</head>
	<body>
		<div class="container">
			<h1>URL Shrinker</h1>
			<form action="/short" method="POST" class="my-4 form-inline">
				<label for="fullUrl" class="sr-only">URL</label>
				<input
					required
					placeholder="URL"
					type="url"
					name="fullUrl"
					id="fullUrl"
					class="form-control col mr-2"
				/>
				<button class="btn btn-success" type="submit">Shrink This!</button>
			</form>

			<table class="table table-striped table-responsive">
				<thead>
					<tr>
						<th>Full URL</th>
						<th>Short URL</th>
						<th>Clicks</th>
					</tr>
				</thead>
				<tbody>
					<% shortUrls.forEach(shortUrl => { %>
					<tr>
						<td><a href="<%= shortUrl.full %>"><%= shortUrl.full %></a></td>
						<td><a href="<%= shortUrl.short %>"><%= shortUrl.short %></a></td>
						<td><%= shortUrl.clicks %></td>
					</tr>
					<% }) %>
				</tbody>
			</table>
		</div>
	</body>
</html>

```

This is a simple challenge, because we just have to put this code in to complete it:

```js
app.use(express.urlencoded({ extended: false }))

app.post('/short', async (req, res) => {
	// Grab the fullUrl parameter from the req.body
	const fullUrl = req.body.fullUrl
	console.log('URL requested: ', fullUrl)

	// insert and wait for the record to be inserted using the model
	const record = new ShortURL({
		full: fullUrl
	})

	await record.save()

	res.redirect('/')
})
```

First of all, we grab the sent URL by HTML using the `req.body.fullUrl`. To enable this, we also have `app.use(express.urlencoded({ extended: false }))` which allows us to get the form data.

Then we create and save our record just like we did the last time. Finally, we redirect the user back to the homepage so that the user can see the new links.

**Tip:** You can make this application more interesting by performing an Ajax request to the backend API instead of typical form submission. But we'll leave it here as it focuses more on MongoDB + Node setup instead of JavaScript.

## Part 6: Displaying short URLs on the frontend

Now that we’re storing shortened URLs in MongoDB, let’s go ahead and show them on the frontend as well. 

Remember our variables passed down to the `ejs` template from before? Now we’ll be using them.

The template loop for `ejs` has been done for you in the `index.ejs` file (you can see that loop above). However, we have to write the Mongoose query to extract the data in this section.

If we see the template, we'll see that in `index.js` we have the following code:

```js
app.get('/', (req, res) => {
	const allData = [] // write a mongoose query to get all URLs from here
	res.render('index', { shortUrls: allData })
})

```

We already have a model defined with us to query data from Mongoose. Let's use it to get everything we need.

Here's our solution file:

```js
const express = require('express')
const app = express()
const mongoose = require('mongoose')
// import the model here
const ShortURL = require('./models/url')

app.set('view engine', 'ejs')
app.use(express.urlencoded({ extended: false }))

app.get('/', async (req, res) => {
	const allData = await ShortURL.find()
	res.render('index', { shortUrls: allData })
})

app.post('/short', async (req, res) => {
	// Grab the fullUrl parameter from the req.body
	const fullUrl = req.body.fullUrl
	console.log('URL requested: ', fullUrl)

	// insert and wait for the record to be inserted using the model
	const record = new ShortURL({
		full: fullUrl
	})

	await record.save()

	res.redirect('/')
})

// Setup your mongodb connection here
mongoose.connect('mongodb://localhost/codedamn', {
	useNewUrlParser: true,
	useUnifiedTopology: true
})

mongoose.connection.on('open', async () => {
	// Wait for mongodb connection before server starts

	// Just 2 URLs for testing purpose
	await ShortURL.create({ full: 'http://google.com' })
	await ShortURL.create({ full: 'http://codedamn.com' })

	app.listen(process.env.PUBLIC_PORT, () => {
		console.log('Server started')
	})
})
```

You can see that it was as easy as doing `await ShortURL.find()` in the `allData` variable. The next part is where things get a bit tricky.

## Part 7: Making the redirection work

We’re almost done! We have the full URL and short URL stored in the database now, and we show them on the frontend too. 

But you’ll notice that the redirection does not work right now and we get an Express error.

Let’s fix that. You can see in the `index.js` file there’s a new dynamic route added at the end which handles these redirects:

```
app.get('/:shortid', async (req, res) => {
	// grab the :shortid param
	const shortid = ''

	// perform the mongoose call to find the long URL

	// if null, set status to 404 (res.sendStatus(404))

	// if not null, increment the click count in database

	// redirect the user to original link
})
```

Our challenges for this part looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/i3.png)

Alright. First things first, we have to extract out the full URL when we visit a short URL. Here's how we'll do that:

```js
app.get('/:shortid', async (req, res) => {
	// grab the :shortid param
	const shortid = req.params.shortid

	// perform the mongoose call to find the long URL
	const rec = await ShortURL.findOne({ short: shortid })

	// ...
})

```

Now, if we see that our result is null, we'll send a 404 status:

```js
app.get('/:shortid', async (req, res) => {
	// grab the :shortid param
	const shortid = req.params.shortid

	// perform the mongoose call to find the long URL
	const rec = await ShortURL.findOne({ short: shortid })

	// if null, set status to 404 (res.sendStatus(404))
	if (!rec) return res.sendStatus(404)

	res.sendStatus(200)	
})
```

This passes our first challenge. Next, if we in fact have a link, let's redirect the user and increment the click count too in the database.

```js
app.get('/:shortid', async (req, res) => {
	// grab the :shortid param
	const shortid = req.params.shortid

	// perform the mongoose call to find the long URL
	const rec = await ShortURL.findOne({ short: shortid })

	// if null, set status to 404 (res.sendStatus(404))
	if (!rec) return res.sendStatus(404)

	// if not null, increment the click count in database
	rec.clicks++
	await rec.save()

	// redirect the user to original link
	res.redirect(rec.full)
})
```

This way, we can increment and store the result in the database again. And that should pass all of our challenges.

## Conclusion

Congratulations! You just built a full working URL shortener by yourself using Express + Node + MongoDB. Give yourself a pat on back! 

The final source code is [available on GitHub](https://github.com/codedamn-classrooms/node-mongodb-url-shortner/tree/lab7-sol).

If you have any feedback on this article or codedamn classrooms, feel free to reach out to me on [Twitter](https://twitter.com/mehulmpt). Let's discuss :)

