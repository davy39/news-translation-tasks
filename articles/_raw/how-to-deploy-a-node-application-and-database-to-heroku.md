---
title: How to deploy a Node Application and Database to Heroku
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2019-09-28T05:02:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-node-application-and-database-to-heroku
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/banner.png
tags:
- name: 100DaysOfCode
  slug: 100daysofcode
- name: deployment
  slug: deployment
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: Heroku
  slug: heroku
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: terminal
  slug: terminal
seo_title: null
seo_desc: Heroku is a cloud-based, fully-managed platform as a service (PaaS) for
  building, running, and managing apps. The platform is flexible and designed with
  DX support for you and your team’s preferred development style and to help you stay
  focused and p...
---

Heroku is a cloud-based, fully-managed platform as a service (PaaS) for building, running, and managing apps. The platform is flexible and designed with DX support for you and your team’s preferred development style and to help you stay focused and productive.

Developers, teams, and businesses of all sizes use Heroku to deploy, manage, and scale apps. Whether you're building a simple prototype or a business-critical product, Heroku's fully-managed platform gives you the simplest path to delivering apps quickly.

With features like Heroku Runtime, Heroku Postgres (SQL), Heroku Redis, Add-ons, Data Clips, App metrics, Smart containers, Enterprise-grade support, GitHub Integration and lots more, Heroku gives developers the freedom to focus on their core product without the distraction of maintaining servers, hardware, or infrastructure.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku.png align="left")

---

One of Heroku's core feature is deploying, managing, and scaling apps with your favorite languages \[Node, Ruby, Python, Java, PHP, Go, and more\].  
In this article, I'll show you how to take an existing Node.js app and deploy it to Heroku – everything from creating your Heroku account to adding a database to your deployed application.

## Prerequisites

In my previous article, I wrote about "[Building a SlackBot with Node.js and SlackBots.js](https://bolajiayodeji.com/building-a-slackbot-with-nodejs-and-slackbotsjs-cjz8gh7zg000exfs1tq2z5zzu)" and I promised to write a follow-up article to show how to host the SlackBot on either Heroku, Zeit or Netlify and publish it to the Slack Apps store. Well, this is the follow-up article but without the "Publishing to Slack Apps" part. We'll cover that in another article.

I assume you have/ know the following already:

* Read my [previous article](https://bolajiayodeji.hashnode.dev/building-a-slackbot-with-nodejs-and-slackbotsjs-cjz8gh7zg000exfs1tq2z5zzu)
    
* Built the [inspireNuggets SlackBot](https://github.com/BolajiAyodeji/inspireNuggetsSlackBot)
    
* Git, Node, and npm installed
    
* A free [Heroku account](https://signup.heroku.com/)
    
* [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed
    

## Bonus

If you don't have npm, Node, and Heroku CLI installed or a Heroku account already, here's a quick bonus \[ Yes, you're welcome :) \].

### Installing npm and Node

* [Node.js](https://nodejs.org) is a JavaScript runtime built on [Chrome's V8 JavaScript engine](https://v8.dev/).
    
* [npm](https://www.npmjs.com/) is the package manager for Node.js. An open-source project created to help JavaScript developers easily share packaged modules of code.
    

You can simply download Node.js [here](https://nodejs.org/en/). Don't worry, npm comes with Node.js, so doing this installs both ✨

### Creating a free Heroku account

Kindly head [here](https://signup.heroku.com/) and fill the Signup form. It's pretty simple.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-signup.png align="left")

### Installing Heroku CLI

The Heroku Command Line Interface (CLI) makes it easy to create and manage your Heroku apps directly from the terminal. It’s an essential part of using Heroku. \[ Well, you can decide to use the GitHub integration feature and Heroku Dashboard but yes you should learn how to use the CLI \]  
Heroku CLI requires Git, the popular version control system. If you don’t already have Git installed, I wrote [this article](https://www.bolajiayodeji.com/setting-up-git-first-time/) to help you.

#### Heroku CLI for Mac OS

```python
brew tap heroku/brew && brew install heroku
```

or [download the installer](https://devcenter.heroku.com/articles/heroku-cli).

#### Heroku CLI for Ubuntu

```python
sudo snap install --classic heroku
```

#### Heroku CLI for Windows

Download the installer for [64-Bit](https://cli-assets.heroku.com/heroku-x64.exe) or [32-Bit](https://cli-assets.heroku.com/heroku-x86.exe).

#### Other installation methods

Please read [this](https://devcenter.heroku.com/articles/heroku-cli#other-installation-methods).

#### Getting started with Heroku CLI

* Verify your installation
    

```python
heroku --version
```

heroku/7.30.1 linux-x64 node-v11.14.0

* Login to your Heroku account
    

There are two ways to do this:

* **Web based auth**
    

```python
heroku login
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-web-auth.png align="left")

Follow the instructions and login via your web browser then return to your terminal.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-web-auth2.png align="left")

* **CLI auth**
    

This is a safer option as it saves your email address and an API token to `~/.netrc` for future use.

```python
heroku login -i
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-cli-auth-1.png align="left")

---

### Deploying your Node.js App

I presume you've built the SlackBot already. If you haven't, please clone the [finished project](https://github.com/BolajiAyodeji/inspireNuggetsSlackBot).

The project is a simple Slackbot that displays random inspiring techie quotes and jokes for developers/designers.

```bash
git clone https://github.com/BolajiAyodeji/inspireNuggetsSlackBot.git && cd inspireNuggetsSlackBot
```

Now let's deploy our app to Heroku ??. I'll show you two ways to do this:

#### Deploy via the Heroku Git

This is done via the Heroku CLI.

##### **☑️ Checklist**

* Specify the version of Node.js that will be used to run your application on Heroku in your `package.json` file.
    

```python
"engines": {
    "node": "10.16.0"
  },
```

* Specify your start script.  
    Simply create a `Procfile` (without any file extension) and add
    

```python
web: node index.js
```

Heroku first looks for this Procfile. If none is found, Heroku will attempt to start a default web process via the start script in your `package.json`.

* Start your app locally using the heroku local command to be sure everything works fine
    

```python
heroku local web
```

Your app should now be running on [http://localhost:5000](http://localhost:5000).

* Don't forget to `.gitignore`
    

```python
/node_modules
.DS_Store
/*.env
```

##### **? Let's Deploy**

How this works is, you have the project working on local already and you've pushed to GitHub already.

* Run `heroku create`
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-create.png align="left")

Basically, this command creates a new Heroku app for you with some randomly generated domain and adds Heroku to your local Git repository.

* Now run `git push heroku master`
    

This is the magic command, it pushes your app to Heroku, installs it there, and launches it on your allocated domain.

In the example above, it's [https://lit-cove-58897.herokuapp.com/](https://lit-cove-58897.herokuapp.com/)

You can always make changes to your app settings and domains in your [Heroku Dashboard](https://dashboard.heroku.com/)

* Now visit your app in your browser
    

```python
heroku open
```

* You can also view information about your running app using one of the logging commands. This is very useful in debugging errors.
    

```python
heroku logs --tail
```

#### Deploy via GitHub integration

You can configure GitHub integration in the Deploy tab of apps in the [Heroku Dashboard](https://dashboard.heroku.com).

##### **☑️ Checklist**

* All previous checklists apply here – ensure you have the app deployed to GitHub already
    

##### **? Let's Deploy**

How this method works is that you push your entire project to GitHub and integrate it to Heroku. Every time you push, it deploys from GitHub to Heroku. Pretty cool right?

* Login to your Heroku Dashboard and create a new app
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/create-app.png align="left")

* Select your app name and region
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/new-app.png align="left")

Now your app has successfully been created

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-dash.png align="left")

* Click the deploy tab and scroll to the **Deployment method** section
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-deploy.png align="left")

* Click the **Connect to GitHub** button
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-github.png align="left")

* Now you have the **Connect to GitHub section**, search for the repository and deploy.
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-search.png align="left")

* Now your app was deployed successfully
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-200.png align="left")

#### Automatic deploys

Now your app is deployed but you'll have to keep deploying manually. You need to enable automatic deploys for a GitHub branch, so Heroku builds and deploys all pushes to that branch.

* Scroll to the **Automatic Deploys** section
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-auto.png align="left")

Select the branch you want to deploy. Ideally, this should be the `master` branch but change this according to your preference.

Now every push to `master` (or the branch you chose) will deploy a new version of this app.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-auto-200.png align="left")

#### Node.js Buildpack

In Heroku, Buildpacks are scripts that are run when your app is deployed. They are used to install dependencies for your app and configure your environment.

After deploying your app, ensure you add a Node.js buildpack to your project.

* Go to **Settings** and scroll to the **Buildpack section**
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-buildpack.png align="left")

* Click the **Add Buildpack** button and select Node.js in the Popup modal.
    

![Image](https://www.freecodecamp.org/news/content/images/2019/10/heroku-add-build.png align="left")

* Now the new buildpack configuration will be used when this app is next deployed. Make some changes to your app and push to GitHub – it will automatically deploy.
    

### Adding a Database to your deployed App'

The Heroku add-on marketplace has a large number of data stores, from Redis and MongoDB providers, to Postgres and MySQL.

Heroku provides three managed data services to all customers in the form of Add-ons:

* [Heroku Postgres](https://elements.heroku.com/addons/heroku-postgresql)
    
* [Heroku Redis](https://elements.heroku.com/addons/heroku-redis)
    
* [Apache Kafka on Heroku](https://elements.heroku.com/addons/cloudkarafka)
    

Writing about this three will make this article too long. It's pretty simple and I'll add some links to the Heroku Docs.

* [Heroku Postgresql Docs](https://devcenter.heroku.com/categories/postgres-basics)
    
* [Heroku Redis Docs](https://devcenter.heroku.com/articles/heroku-redis)
    
* [Apache Kafka on Heroku Docs](https://devcenter.heroku.com/articles/kafka-on-heroku)
    

---

## Conclusion

Every Heroku account is allocated a pool of free dyno hours. Heroku (free) dynos are great for hosting apps and personal projects. The downside, however, is that your app will fall asleep if it doesn't receive any web traffic within 30-minutes :(.

You can use external tools to ping your server periodically so it never falls asleep.

Here are some to consider:

* [Pingmydyno](https://www.npmjs.com/package/pingmydyno)
    
* [Heroku self ping](https://www.npmjs.com/package/heroku-self-ping)
    
* [Wakemydyno](http://wakemydyno.com/)
    
* [Kaffeine](https://kaffeine.herokuapp.com/)
    

---

> Heroku is meticulously designed to help developers be as productive as possible. The platform removes frustrating obstacles and mundane tasks, so you can stay free of distraction in your development flow. Wherever you are on the learning path, Heroku helps you love app development even more. - Heroku

The Heroku experience provides services, tools, workflows, and polyglot support—all designed to enhance developer productivity. There is more to using Heroku and I hope you explore more and build amazing stuff with Heroku.

If you're a student, Kindly register for the [GitHub Student Developer Pack](https://education.github.com/pack) to get One free [Hobby Dyno](https://www.heroku.com/pricing) for up to two years.

The pack give students free access to the best developer tools in one place so you can learn by doing.
