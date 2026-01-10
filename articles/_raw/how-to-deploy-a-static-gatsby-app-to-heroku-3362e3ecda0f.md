---
title: How to deploy a static Gatsby app to Heroku
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-24T19:51:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-static-gatsby-app-to-heroku-3362e3ecda0f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XjHB-v-6y23f0TdUEqEZog.png
tags:
- name: deployment
  slug: deployment
- name: GatsbyJS
  slug: gatsbyjs
- name: GitHub
  slug: github
- name: Heroku
  slug: heroku
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Kristin Baumann

  This tutorials explains how to set up the deployment of a static GatsbyJS project
  with Heroku and Github. You will learn how to create a staging and production environment
  for your application so you’re ready for safe continuous de...'
---

By Kristin Baumann

This tutorials explains how to set up the deployment of a static GatsbyJS project with Heroku and Github. You will learn how to create a staging and production environment for your application so you’re ready for safe continuous deployment.

After finishing this tutorial, …

* ✈️ you will be able to **build and deploy a static Gatsby application**.
* ? you will be able to t**rigger automatic deploys** to your s**taging environment** by pushing to your git repo. (You can review the staging app and, if suitable, promote it to your p**roduction website.**)

**Requirements:**

* Your project will be based on [GatsbyJS](https://www.gatsbyjs.org/) (a static site generator). You don’t need any knowledge in coding with Gatsby or React, but you should have [Node](https://nodejs.org/en/download/) and [GatsbyJS](https://www.gatsbyjs.org/docs/) installed.
* You will need a [Github](https://github.com/) and [Heroku](https://heroku.com/) account (both available for free). Git needs to be set up on your machine.

### 1.) Create a new Gatsby project

First, you need a fresh Gatsby project.

* You can create a new project in the folder `test-project` by executing the following in our console:

```
gatsby new test-project https://github.com/gatsbyjs/gatsby-starter-hello-world
```

This creates the essential files for a static Gatsby application from a starter pack. You can start the development server locally by going into the project directory with `cd test-project` and then running `gatsby develop`. Your app is now available on `localhost:8000`.

### 2.) Set up a git repo

With the project running locally, you can now set up a git repository for your Gatsby project.

* Log into Github and create a new repo.
* Initialise a git repo in your project with:

```
git init
```

* Connect your local git repo to your remote repo with:

```
git remote add origin <remoteURL>
```

* Make your initial commit of the Gatsby project with:

```
git add .git commit -m "Initial commit"git push origin master
```

The changes in your Gatsby project are now tracked with Github, which will provide the trigger to start a deployment later on.

### 3.) Set up Heroku apps

As a next step, you can configure the continuous deployment environments on Heroku.

* Create a new pipeline called `test-project` in the Heroku app dashboard
* Within this pipeline, create a new app for the staging environment called `test-project-staging` and a new app for production called `test-project-prod`
* Connect the pipeline (not each app individually) with your previously created Github repo
* Enable automatic deployments from the master branch for the staging app (but not for the production app!)
* Set the buildpacks for both apps to:

```
"heroku/nodejs" 
```

```
"https://github.com/heroku/heroku-buildpack-static"
```

These buildpacks are scripts that run when your app is deployed and are specific for your static Gatsby project. You can configure the static buildpack in the next step.

![Image](https://cdn-media-1.freecodecamp.org/images/qNtbliSCD21VxlTI5LE69J5KajixsfdmMSth)
_Your Heroku setup including a staging and production environment_

### 4.) Prepare your Gatsby project for deployment to Heroku

* After your code is copied to Heroku and the necessary dependencies are installed, the Gatsby project needs to be build and stored in the static /public folder. Therefore add a build script in your `package.json` file:

```
{     // ...
```

```
     scripts: {         // ...
```

```
         “heroku-postbuild”: “gatsby build”
```

```
     },
```

```
     // ...}
```

* Create a file called `app.json` in the root directory of your project. This file includes general information required to run an app on Heroku. In our case we state again the usage of the two buildpacks:

```
{
```

```
    "buildpacks": [
```

```
     { "url": "heroku/nodejs" },
```

```
     { "url": "https://github.com/heroku/heroku-buildpack-static" }
```

```
    ]
```

```
}
```

* Create a file called `static.json` in the root directory of your project. The `static.json` file is used for the configuration of the static buildpack. You can view more configuration options [here](https://elements.heroku.com/buildpacks/heroku/heroku-buildpack-static). In this case we only define the folder of our built application:

```
{
```

```
    "root": "public/"
```

```
}
```

* (Optional) Heroku’s deployment will fail when you have a `package-lock.json` as well as a `yarn.lock` file in your project directory. When this is the case, decide on one. For example, delete the `package-lock.json` file in case you are using yarn.

### 5.) Test your setup

Congratulations, pretty much done! ?

You can now test your setup by committing the changes from the last step to Github:

```
git add .git commit -m "Prepared Heroku deployment of Gatsby app"git push origin master
```

This is should trigger an automatic build and deployment of your Gatsby project to the staging environment. You can then review the staging app and, if suitable, promote it to your production website.

_Thanks for reading this article! Please leave questions or feedback and follow me on [Twitter](https://twitter.com/kristin_baumann) for more JavaScript and React related posts._

