---
title: Three Things to Consider Before Deploying Your First Full Stack App
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-17T21:12:22.000Z'
originalURL: https://freecodecamp.org/news/3-things-to-consider-before-deploying-your-first-full-stack-app
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c1d740569d1a4ca3007.jpg
tags:
- name: api
  slug: api
- name: AWS
  slug: aws
- name: Azure
  slug: azure
- name: containers
  slug: containers
- name: deployment
  slug: deployment
- name: Docker
  slug: docker
- name: Express
  slug: express
- name: full stack
  slug: full-stack
- name: Heroku
  slug: heroku
- name: Kubernetes
  slug: kubernetes
- name: mongoose
  slug: mongoose
- name: node
  slug: node
- name: REST
  slug: rest
- name: vue
  slug: vue
seo_title: null
seo_desc: 'By M. S. Farzan

  Building a full stack app is no small endeavor, and deploying it comes with its
  own host of things to consider.

  I''m a tabletop game developer, and recently deployed a simple roleplaying game
  tracker that uses the M-E-V-N stack (you ca...'
---

By M. S. Farzan

Building a full stack app is no small endeavor, and deploying it comes with its own host of things to consider.

I'm a [tabletop game](https://www.nightpathpub.com/entromancy) developer, and recently deployed a simple [roleplaying game tracker](https://mevn-rpg-app.herokuapp.com/) that uses the [M](https://www.mongodb.com/)-[E](https://expressjs.com/)-[V](https://vuejs.org/)-[N](https://nodejs.org/en/) stack (you can follow my tutorial to create your own app [here](https://www.freecodecamp.org/news/build-a-full-stack-mevn-app/)).  

In deploying the app, I came across three key takeaways that may be useful as you begin considering the best way to bring your projects from development to production. 

You can check out the code to my app on [GitHub](https://github.com/sominator/mevn-rpg-app), and I should mention that it includes Chad Carteret's [very cool CSS statblock](https://codepen.io/retractedhack/pen/gPLpWe) in prettifying what's otherwise very basic HTML.

If you're thinking of following the same path to deployment as I have here, be sure to check out the official documentation on [Heroku](https://devcenter.heroku.com/articles/deploying-nodejs), the [Vue CLI](https://cli.vuejs.org/guide/deployment.html), and [this tutorial](https://medium.com/netscape/deploying-a-vue-js-2-x-app-to-heroku-in-5-steps-tutorial-a69845ace489) by Nick Manning.

You'll also want to take a look at Will Abramson's [article on a similar topic](https://www.freecodecamp.org/news/lessons-learned-from-deploying-my-first-full-stack-web-application-34f94ec0a286/).

On to deployment!

## Your front end and back end can be deployed together or separately, depending on your app's complexity.

One snag that seems to appear immediately when considering production is the structural question of how to deploy the front and back ends of your app.

Should the client (or static files) live in the same place as the server and database? Or should they be separate, with the front end making HTTP requests from elsewhere to the back end using [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)?

The answer is yes! Or no. Maybe??

For better or worse, there's no one-size-fits-all solution to this question, as it will likely depend on your app's architecture and complexity. In the roleplaying game tracker that I linked to above, I have the whole stack running on a single Heroku [dyno](https://www.heroku.com/dynos), with the following folder structure:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Folder-Structure.PNG)

All of the front and back end files live in the same place, with the Vue client built for production in a folder located at /client/dist.

In server.js, along with a bunch of database and routing code, there's a little line that says:

```javascript
server.use(serveStatic(__dirname + "/client/dist"));
```

In Express, this tells the app to serve my static client files from a particular folder, and enables me to run the front and back ends all within the same environment. If you're deploying a similarly simple app, this type of solution might work for you as well.  

Conversely, and depending on your project's complexity, you may have to separate the front and back ends and treat them as separate applications, which is no big deal. In the app above, my client is making calls to static API endpoints that are handled by the server, like this:

```javascript
getQuests: function () {
    axios
        .get('https://mevn-rpg-app.herokuapp.com/quests')
        .then(response => (this.questData = response.data))                   
 }
```

Technically, my client could be making those requests from anywhere - even a static GitHub Pages site. This type of solution can help separate your app into two distinct entities to tackle, which is sometimes better than trying to cram the whole project into one location.

One note: if you're going to be making cross-origin HTTP requests - that is, requests from a client that lives on a separate domain from the API or server - you'll need to become familiar with [CORS](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing).  You can read more about it in [this article](https://www.freecodecamp.org/news/i-built-a-web-api-with-express-flask-aspnet/).  

## Your code will need to change to support a production environment.

When you're knee deep in the development process, it can be easy to lose track of how much of your code depends on local files or other data.

Consider the following in a locally-running server.js:

```javascript
server.listen(3000, () => console.log("Server started!"));
```

On a local machine, the code just asks the server to listen on port 3000 and log to the console that we're ready for liftoff.

In a production environment, the server has no concept of where the "localhost" should be, or to whose port 3000 it should be listening. With this example, you'd have to change your code to something like:

```javascript
const port = process.env.PORT || 3000;

server.listen(port, () => console.log("Server started!"));
```

The above instructs the server to instead listen at port 3000 of the _process_ that's currently running, wherever that might be (check out [this article](https://codeburst.io/process-env-what-it-is-and-why-when-how-to-use-it-effectively-505d0b2831e7) for further reading on this topic).

Similarly, in my app, I have several modules that need to be imported by one another to function:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Folder-Structure-Expanded.PNG)

In /routes/Quests.js, for example, I have a router that tells the server what to do when receiving API requests to interact with quest-related items in the database. The router needs to import a [Mongoose schema](https://mongoosejs.com/docs/guide.html) from /models/quest.js to function properly. If the application were running locally, we could just say:

```javascript
const Quest = require('../models/quest');
```

Pretty simple! Yet, unfortunately, our server won't know where to find the root directory of our project once deployed. In Express, we'd change our code to something like:

```javascript
const path = require('path');
const Quest = require(path.join(__dirname, '../models/quest'));
```

Your particular case might be different, depending on your language and framework(s), but you'll need to get specific about what your code looks like in a production environment rather than in your local development environment.

Additionally, you're probably already familiar with whatever bundler you're using for your front end (e.g., [webpack](https://webpack.js.org/)), and will want to build your client for production to optimize it for deployment.

## You have a multitude of deployment platforms from which to choose.

If you've deployed a front end website or some other type of static app, you might be familiar with just pushing your files to some remote repository and calling it a day.

Deploying a full stack app (or even just a back end) is eminently more complex. You'll need a dedicated server, or something that emulates one, to respond to the HTTP requests that it will be receiving and work with an online database.

There are a number of services that will do this very thing for you, and the spectrum ranges based on price, scalability, complexity, and other factors.

There's a bunch of articles out there that compare [PaaS](https://en.wikipedia.org/wiki/Platform_as_a_service) options for deployment, but here are some thoughts as you consider platforms for your first project:

<ul>
    <li><strong>Heroku</strong>: If you have a small project like mine or just want to learn about deployment, a good first step could be <a href="https://www.heroku.com/">Heroku</a>.</li>
    <li><strong>AWS, Docker, and Kubernetes</strong>: If you're seeking a career in full stack web development or DevOps, now's a good time to familiarize yourself with <a href="https://aws.amazon.com/">Amazon Web Services</a> and/or container platforms like <a href="https://www.docker.com/">Docker</a> and <a href="https://kubernetes.io/">Kubernetes</a>.</li>
    <li><strong>Azure</strong>: If you're a C# or .NET developer, <a href="https://azure.microsoft.com/en-us/">Azure</a> appears to be a seamless way to deploy your apps without having to leave the safety of the Microsoft ecosystem.</li>
</ul>

There are, of course, several other options out there, and your particular use-case scenario might depend on pricing or the specific feature sets that are on offer.

Additionally, you'll want to consider any addons that will be necessary to replicate your app's functionality in a production environment. My roleplaying game tracker, for example, uses MongoDB, but the production version certainly can't use the little database on my local machine! Instead, I've used the [mLab](https://elements.heroku.com/addons/mongolab) Heroku addon to get the live site up and running with the same functionality as in my development environment.

Your app's success, as well as your own progress as a full stack web developer, depend on your ability to consider deployment options and create a successful pipeline for production. With a little research, I'm certain that you can find the best solution that fits all of your app's needs.

Happy coding!

If you enjoyed this article, please consider [checking out my games and books](https://www.nightpathpub.com/), [subscribing to my YouTube channel](https://www.youtube.com/msfarzan?sub_confirmation=1), or [joining the _Entromancy_ Discord](https://discord.gg/RF6k3nB).

M. S. Farzan, Ph.D. has written and worked for high-profile video game companies and editorial websites such as Electronic Arts, Perfect World Entertainment, Modus Games, and MMORPG.com, and has served as the Community Manager for games like _Dungeons & Dragons Neverwinter_ and _Mass Effect: Andromeda_. He is the Creative Director and Lead Game Designer of _[Entromancy: A Cyberpunk Fantasy RPG](https://www.nightpathpub.com/rpg)_ and author of _[The Nightpath Trilogy](http://nightpathpub.com/books)_. Find M. S. Farzan on Twitter [@sominator](https://twitter.com/sominator).

