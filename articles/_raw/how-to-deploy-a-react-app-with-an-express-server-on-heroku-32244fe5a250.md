---
title: How to deploy a React app with an Express server on Heroku
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-18T21:35:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-react-app-with-an-express-server-on-heroku-32244fe5a250
coverImage: https://cdn-media-1.freecodecamp.org/images/1*j8DELPVuI_w8045sxmHQsA.png
tags:
- name: Express.js
  slug: expressjs
- name: Heroku
  slug: heroku
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ashish Nandan Singh

  Hello, world! Recently I had to deploy a website to Heroku for one of the pieces
  of freelance work I was doing. I think this process may be somewhat difficult, and
  a detailed tutorial or article on how to do this should help. S...'
---

By Ashish Nandan Singh

Hello, world! Recently I had to deploy a website to Heroku for one of the pieces of freelance work I was doing. I think this process may be somewhat difficult, and a detailed tutorial or article on how to do this should help. So this one is going to be very simple and hopefully very short.

We will start by creating an Express app, which will act as our server. Once the server is done, we will create a simple create-react-app application, connect the server with the frontend and, finally, deploy the whole thing to a hosting platform such as Heroku.

Before we go any further, I want you to understand that in the world of web development almost everything is up to one’s preference. Some of you may disagree on certain things, you may continue the way you want to do things, and that’s totally fine. Up to the point when we’re breaking the application I consider everything to be fine.

Let’s get started.

### Create a Node/Express app

Start by creating a folder for the overall project. This folder will contain the client side application — our React app in this case. Navigate to the directory in your terminal and type the commands below.

```
$ touch server.js$ npm init
```

The last command from the above snippet will take you through some of the steps and will initialise your project with a `package.json` file. If you are totally new to this, you can consider this file to be a ledger where you keep the record of all the dependencies you’ll be using across the build process of your application.

Moving on, now that we have the `package.json` file ready, we can start by adding our dependency for the project.

Adding Express:

```
$ npm i -g express --save
```

This will add Express as a dependency to your package.json. Now that we have this, all we need is one more dependency and that is for hot reloading of the app whenever we make some change to the code:

```
$ npm i -g nodemon --save --dev
```

This will add nodemon to the app. If you would like to read more about nodemon, you can check [this](https://nodemon.io/) link for more information.

Now that we have these added, we are all set to create our most basic server in Express. Let’s see how that’s done.

```
const express = require('express');const app = express();const port = process.env.PORT || 5000;
```

```
//Route setupapp.get('/', (req, res) => {    res.send('root route');
```

```
})
```

```
//Start serverapp.listen(port, (req, res) => {
```

```
console.log(`server listening on port: ${port}`)
```

```
 });
```

That’s it. Just navigate to the terminal, make sure you are in the root directory of the project, and type:

```
$ nodemon <name-of-the-file> (index.js/server.js)
```

In our case since we named it `server.js` it would be `nodemon server.js` _._ This will start the server on port 5000 of your computer locally. If you go visit the browser and open [https://localhost:5000/](https://localhost:5000/) you will see the text “root route”, which means the server has started. In case you face any issues, feel free to add them in the comments below.

Now that the server is set up and is working, let’s proceed towards getting the React app setup.

### React app

```
$ npm i -g create-react-app$ create-react-app <name-of-the-app>
```

For the purpose of this tutorial we will name the app “client,” so our command will look like this `create-react-app client`_._

Once this is done, the setup will take some time and will create a nice little folder inside your main application with the name “client”.

We will not make any major changes in the overall React application for now — that is outside the scope of this tutorial.

Now the challenge is that we need to call and connect with our server running on the localhost. To do that we need to make an API call.

#### Adding a proxy

React gives us the ability to do so by adding a proxy value to our `package.json` file. Navigate to the `package.json` file in your directory and add the piece of code below.

```
"proxy": "http://localhost:5000",
```

In our case, the server is running at port 5000, hence the 5000 in the proxy value. The value may vary if you are using a different port altogether.

Now we need to call the Express-defined endpoints, or API endpoints, from our React components. What that really means is that now we can simply call “api/users/all” from our client side, which will then proxy our request and it will look like this “https://localhost:5000/api/users/all". This saves us from making a cross origin request, which most of the modern browsers do not allow for security reasons.

Next we will make some changes to the `src/app.js` file.

```
import React, { Component } from 'react';import './App.css';import Navbar from './Components/Layout/Navbar';import { BrowserRouter as Router, Route } from 'react-router-dom';import Footer from './Components/Layout/Footer';import Home from './Components/Layout/Home';import Social from './Components/social/Social';
```

```
class App extends Component {  constructor(props) {    super(props);    this.state = {}    this.connecToServer = this.connecToServer.bind(this);  }
```

```
  connecToServer() {    fetch('/');  }
```

```
  componentDidMount() {    this.connecToServer();  }
```

```
  render() {    return (      <Router>      <div className="container">         <Navbar />         <Route exact path="/" component={Home} />         <Route exact path="/social" component={Social} />         <Footer />      </div>      </Router>    );  }}
```

```
export default App;
```

What we did was to create a constructor, and bind the value of this in our function which will make the fetch API call. Then we call the function as soon as the component is mounted. Next we have the render function which has the overall markup for the app. So that was the last change we will do in React or our frontend application.

Your `package.json` file should look like the code snippet below.

```
{  "name": "project-name",  "version": "0.1.0",  "private": true,  "dependencies": {    "react": "^16.6.3",    "react-dom": "^16.6.3",    "react-scripts": "2.1.1",    "react-router-dom": "^4.3.1"  },
```

```
  "scripts": {    "start": "react-scripts start",    "build": "react-scripts build",    "test": "react-scripts test",    "eject": "react-scripts eject"  },
```

```
  "eslintConfig": {    "extends": "react-app"  },
```

```
  "proxy": "http://localhost:5000",
```

```
  "browserslist": [    ">0.2%",    "not dead",    "not ie <= 11",    "not op_mini all"  ]}
```

Now let’s pause for a minute and think about what we need to do next…. any thoughts?

Some of you are right by thinking we need to make sure our React files are being served by our Express server. Let’s make some modifications to the `server.js` file to make sure that the React files get served by the Express server.

#### Server file change

```
const express = require('express');const app = express();const path = require('path');const port = process.env.PORT || 5000;
```

```
//Static file declarationapp.use(express.static(path.join(__dirname, 'client/build')));
```

```
//production modeif(process.env.NODE_ENV === 'production') {  app.use(express.static(path.join(__dirname, 'client/build')));  //  app.get('*', (req, res) => {    res.sendfile(path.join(__dirname = 'client/build/index.html'));  })}
```

```
//build modeapp.get('*', (req, res) => {  res.sendFile(path.join(__dirname+'/client/public/index.html'));})
```

```
//start serverapp.listen(port, (req, res) => {  console.log( `server listening on port: ${port}`);})
```

In the above code snippet, first you need to use the inbuilt path module in node and declare the static folder you would like to use in this Express server.

Then you check if the process **is production**, which it will be once the app is deployed to Heroku. Under this condition you would like to serve the `index.html` file from the build folder **and not** the public folder.

If it’s **not the production mode,** and you are testing some feature and your server is running on the localhost, you would like the `index.html` from the public folder to be served.

Now we need to make sure that first we start our Express server and then go about starting our React server. Now there are a lot of ways to do this, and for the simplicity of this tutorial we will be using a module called `concurrently` to run both the servers with one command.

Make sure you are in the root directory, and then run the command below from your terminal.

```
npm i concurrently --save
```

After doing this, let’s make some changes to the scripts we have in our Express server `package.json` files.

```
"scripts": {    "client-install": "npm install --prefix client",    "start": "node index.js",    "server": "nodemon index.js",    "client": "npm start --prefix client",    "dev": "concurrently \"npm run server\" \"npm run client\"",
```

```
}
```

* `npm run client-install` will install all the dependencies for the React application
* `npm start` will start the server and not reload after detecting any change
* `npm run server` will start the server, listen for any changes in the code, and hot reload the page on browser to reflect the change.
* `npm run client` will run the React application without starting the server
* `npm run dev` will concurrently run the server and then run the client on your browser

### Heroku setup

Make sure you have an account on Heroku. If you don’t, you can make one using your GitHub credentials very quickly.

Next we will install the Heroku CLI , which will help us deploy the application right from our terminal. [Click here](https://devcenter.heroku.com/articles/heroku-cli) to get install instructions on both macOS and Windows.

```
$ heroku login
```

Enter the login credentials for Herkou and then:

```
$ heroku create
```

This will create an application for you. If you visit the Heroku dashboard now, it will have the application there.

Now we need to make sure we have a build folder in our project before we push the project to the Heroku repository. Add the script below into your `package.json` file.

```
"scripts": {    "client-install": "npm install --prefix client",
```

```
    "start": "node server.js",
```

```
    "server": "nodemon server.js",
```

```
    "client": "npm start --prefix client",
```

```
    "dev": "concurrently \"npm run server\" \"npm run client\"",
```

```
    "heroku-postbuild":      "NPM_CONFIG_PRODUCTION=false npm install --prefix client        && npm run build --prefix client"  },
```

After doing this, save the file and push the entire project repository to your Heroku application branch.

```
//add remote
```

```
$ heroku git:remote -a application-name
```

```
$ git add .
```

```
$ git commit -am 'prepare to deploy'
```

```
$ git push heroku master
```

And that should be it.

Once this is all done, you will get a URL for your live hosted project. Share and showcase what you can build using these technologies.

If you have any questions or comments feel free to add your comment or connect directly.

Github: [https://github.com/ashishcodes4](https://github.com/ashishcodes4)

Twitter: [https://twitter.com/ashishnandansin](https://twitter.com/ashishnandansin)

LinkedIn: [https://www.linkedin.com/in/ashish-nandan-singh-490987130/](https://www.linkedin.com/in/ashish-nandan-singh-490987130/)

