---
title: How to deploy your app to the web using Express.js and Heroku
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-02T11:55:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-your-site-using-express-and-heroku
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c56740569d1a4ca317c.jpg
tags:
- name: deployment
  slug: deployment
- name: Express
  slug: express
- name: Express JS
  slug: express-js
- name: full stack
  slug: full-stack
- name: Git
  slug: git
- name: Heroku
  slug: heroku
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: node
  slug: node
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
- name: Tutorial
  slug: tutorial
- name: Web Applications
  slug: web-applications
seo_title: null
seo_desc: 'By Peter Gleeson

  If you are new to the world of web development, you will spend a lot of time learning
  how to build static sites with HTML, CSS and JavaScript.

  You might then start learning how to use popular frameworks such as React, VueJS
  or Angula...'
---

By Peter Gleeson

If you are new to the world of web development, you will spend a lot of time learning how to build static sites with HTML, CSS and JavaScript.

You might then start learning how to use popular frameworks such as [React](https://reactjs.org/), [VueJS](https://vuejs.org/) or [Angular](https://angular.io/).

But after trying out a few new ideas and running some sites locally, you might wonder how to actually deploy your site or app. And as it turns out, it can sometimes be difficult to know where to start.

Personally, I find running an Express server hosted on Heroku one of the simplest ways to get going. This article will show you how to do this.

[Heroku](https://www.heroku.com/) is a cloud platform which supports a number of different programming languages and frameworks.

This is not a sponsored post - there are of course many other solutions available, such as:

* [Digital Ocean](https://www.digitalocean.com/)
* [Amazon Web Services](https://aws.amazon.com/)
* [Azure](https://azure.microsoft.com/en-gb/)
* [Google Cloud Platform](https://cloud.google.com/)
* [Netlify](https://www.netlify.com/)
* [ZEIT Now](https://zeit.co/)

Check them all out and see which suits your needs best.

Personally, I found Heroku the quickest and easiest to start using "out of the box". The free tier is somewhat limited in terms of resources. However, I can confidently recommend it for testing purposes.

This example will host a simple site using an Express server. Here are the high-level steps:

1. Setting up with Heroku, Git, npm
2. Create an Express.js server
3. Create static files
4. Deploy to Heroku

It should take about 25 minutes in total (or longer if you want to spend more time on the static files).

This article assumes you already know:

* Some HTML, CSS and JavaScript basics
* Basic command line usage
* Beginner-level Git for version control

You can find all the code in [this repository](https://github.com/pg0408/lorem-ipsum-demo).

### Setting up

The first step in any project is to set up all the tools you know you'll need.

You'll need to have:

* Node and npm installed on your local machine (read how to do this [here](https://nodejs.org/en/download/))
* Git installed (read [this guide](https://www.atlassian.com/git/tutorials/install-git))
* The Heroku CLI installed ([here's how to do it](https://devcenter.heroku.com/articles/heroku-cli#download-and-install))

**1. Create a new directory and initialise a Git repository**

From the command line, create a new project directory and move into it.

```
$ mkdir lorem-ipsum-demo
$ cd lorem-ipsum-demo
```

Now you are in the project folder, initialise a new Git repository.

⚠️This step is important because [Heroku relies on Git](https://devcenter.heroku.com/articles/how-heroku-works#deploying-applications) for deploying code from your local machine to its cloud servers ⚠️

```
$ git init
```

As a final step, you can create a README.md file to edit at a later stage.

```
$ echo "Edit me later" > README.md
```

**2. Login to the Heroku CLI and create a new project**

You can login to Heroku using the Heroku CLI (command line interface). You will need to have a free Heroku account to do this.

There are two options here. The default is for Heroku to let you login through the web browser. Adding the `-i` flag lets you login through the command line.

```
$ heroku login -i
```

Now, you can create a new Heroku project. I called mine `lorem-ipsum-demo`.

```
$ heroku create lorem-ipsum-demo
```

Naming your project:

* Heroku will generate a random name for your project if you don't specify one in the command.
* The name will form part of the URL you can use to access your project, so choose one you like. 
* This also means that you need to choose a unique project name that no one else has used.
* It is possible to rename your project later (so don't worry too much about getting the perfect name right now).

**3. Initialise a new npm project and install Express.js**

Next, you can initialise a new npm project by creating a package.json file. Use the command below to do this.

⚠️This step is crucial. Heroku relies on you providing a package.json file to know this is a Node.js project when it builds your app ⚠️

```
$ npm init -y
```

Next, [install Express](https://expressjs.com/en/starter/installing.html). Express is a widely used server framework for NodeJS.

```
$ npm install express --save
```

Finally, you are ready to start coding!

### Writing a simple Express server

The next step is to create a file called `app.js`, which runs an Express server locally.

```
$ touch app.js
```

This file will be the entry point for the app when it is ready. That means, the one command needed to launch the app will be:

```
$ node app.js
```

But first, you need to write some code in the file.

**4. Edit the contents of app.js**

Open `app.js` in your favourite editor. Write the code shown below and click save.

```javascript
// create an express app
const express = require("express")
const app = express()

// use the express-static middleware
app.use(express.static("public"))

// define the first route
app.get("/", function (req, res) {
  res.send("<h1>Hello World!</h1>")
})

// start the server listening for requests
app.listen(process.env.PORT || 3000, 
	() => console.log("Server is running..."));
```

The comments should help indicate what is happening. But let's quickly break the code down to understand it further:

* The first two lines simply require the Express module and create an instance of an Express app.
* The next line requires the use of the `express.static` middleware. This lets you serve static files (such as HTML, CSS and JavaScript) from the directory you specify. In this case, the files will be served from a folder called `public`.
* The next line uses `app.get()` to define a URL route. Any URL requests to the root URL will be responded to with a simple HTML message.
* The final part starts the server. It either looks to see which port Heroku will use, or defaults to 3000 if you are running locally.

⚠️The use of `process.env.PORT || 3000` in the last line is important for deploying your app successfully ⚠️

If you save `app.js` and start the server with:

```
$ node app.js
```

You can visit [localhost:3000](http://localhost:3000/) in your browser and see for yourself the server is running.

### Create your static files 

The next step is to create your static files. These are the HTML, CSS and JavaScript files you will serve up whenever a user visits your project.

Remember in `app.js` you told the `express.static` middleware to serve static files from the `public` directory.

The first step is of course to create such a directory and the files it will contain.

```
$ mkdir public
$ cd public
$ touch index.html styles.css script.js
```

**5. Edit the HTML file**

Open `index.html` in your preferred text editor. This will be the basic structure of the page you will serve to your visitors.

The example below creates a simple landing page for a [Lorem Ipsum](https://en.wikipedia.org/wiki/Lorem_ipsum) generator, but you can be as creative as you like here.

```html
<!DOCTYPE html>
<head>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
	<link href="https://fonts.googleapis.com/css?family=Alegreya|Source+Sans+Pro&display=swap" rel="stylesheet">
	<link rel="stylesheet" type="text/css" href="styles.css">
</head>
<html>
<body>
<h1>Lorem Ipsum generator</h1>
  <p>How many paragraphs do you want to generate?</p>
  <input type="number" id="quantity" min="1" max="20" value="1">
  <button id="generate">Generate</button>
  <button id="copy">Copy!</button>
<div id="lorem">
</div>
<script type="text/javascript" src="script.js"></script>
</body>
</html>
```

**6. Edit the CSS file**

Next up is editing the CSS file `styles.css`. Make sure this is linked in your HTML file.

The CSS below is for the Lorem Ipsum example. But again, feel free to be as creative as you want.

```css
h1 {
	font-family: 'Alegreya' ;
}

body {
	font-family: 'Source Sans Pro' ;
	width: 50%;
	margin-left: 25%;
	text-align: justify;
	line-height: 1.7;
	font-size: 18px;
}

input {
	font-size: 18px;
	text-align: center;
}

button {
	font-size: 18px;
	color: #fff;
}

#generate {
	background-color: #09f;
}

#copy {
	background-color: #0c6;
}
```

**7. Edit the JavaScript file**

Finally, you might want to edit the JavaScript file `script.js`. This will let you make your page more interactive.

The code below defines two basic functions for the Lorem Ipsum generator. Yes, I used [JQuery](https://jquery.com/) - it's quick and easy to work with.

```javascript
$("#generate").click(function(){
	var lorem = $("#lorem");
	lorem.html("");
	var quantity = $("#quantity")[0].valueAsNumber;
	var data = ["Lorem ipsum", "quia dolor sit", "amet", "consectetur"];
	for(var i = 0; i < quantity; i++){
		lorem.append("<p>"+data[i]+"</p>");
	}
})

$("#copy").click(function() {
	var range = document.createRange();
	range.selectNode($("#lorem")[0]);
	window.getSelection().removeAllRanges();
	window.getSelection().addRange(range);
	document.execCommand("copy");
	window.getSelection().removeAllRanges();
	}
)
```

Note that here, the `data` list is truncated to make it easier to show. In the actual app, it is a much longer list of full paragraphs. You can see the entire file in the repo, or look [here for the original source](http://www.thelatinlibrary.com/cicero/fin1.shtml).

### Deploying your app

After writing your static code and checking it all works as expected, you can get ready to deploy to Heroku.

However, there are a couple more things to do.

**8. Create a Procfile**

Heroku will need a Procfile to know how to run your app.

A Procfile is a "process file" which tells Heroku which command to run in order to manage a given process. In this case, the command will tell Heroku how to start your server listening on the web.

Use the command below to create the file.

⚠️This is an important step, because without a Procfile, Heroku cannot put your server online. ⚠️

```
$ echo "web: node app.js" > Procfile
```

Notice that the Procfile has no file extension (e.g., ".txt", ".json"). 

Also, see how the command `node app.js` is the same one used locally to run your server.

**9. Add and commit files to Git**

Remember you initiated a Git repository when setting up. Perhaps you have been adding and committing files as you have gone.

Before you deploy to Heroku, make sure to add all the relevant files and commit them.

```
$ git add .
$ git commit -m "ready to deploy"
```

The final step is to push to your Heroku master branch.

```
$ git push heroku master
```

You should see the command line print out a load of information as Heroku builds and deploys your app.

The line to look for is: `Verifying deploy... done.`

This shows that your build was successful.

Now you can open the browser and visit your-project-name.herokuapp.com. Your app will be hosted on the web for all to visit!

### Quick recap

Below are the steps to follow to deploy a simple Express app to Heroku:

1. Create a new directory and initialise a Git repository
2. Login to the Heroku CLI and create a new project
3. Initialise a new npm project and install Express.js
4. Edit the contents of app.js
5. Edit the static HTML, CSS and JavaScript files
6. Create a Procfile
7. Add and commit to Git, then push to your Heroku master branch

### Things to check if your app is not working

Sometimes, despite best intentions, tutorials on the Internet don't work exactly as you expected.

The steps below should help debug some common errors you might encounter:

* Did you initialise a Git repo in your project folder? Check if you ran `git init` earlier. Heroku relies on Git to deploy code from your local machine.
* Did you create a package.json file? Check if you ran `npm init -y` earlier. Heroku requires a package.json file to recognise this is a Node.js project.
* Is the server running? Make sure your Procfile uses the correct file name to start the server. Check you have `web: node app.js` and not `web: node index.js`.
* Does Heroku know which port to listen on? Check you used `app.listen(process.env.PORT || 3000)` in your app.js file.
* Do your static files have any errors in them? Check them by running locally and seeing if there are any bugs.

Thanks for reading - if you made it this far, you might want to [checkout the finished version](http://lorem-ipsum-demo.herokuapp.com/) of the demo project.

