---
title: How to use Netlify Functions in Elm
subtitle: ''
author: Cedd Burge
co_authors: []
series: null
date: '2019-08-28T07:37:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-netlify-functions-in-elm
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/netlify-functions-elm.jpg
tags:
- name: create-elm-app
  slug: create-elm-app
- name: netlify-functions
  slug: netlify-functions
- name: aws lambda
  slug: aws-lambda
- name: ELM
  slug: elm
- name: Netlify
  slug: netlify
- name: serverless
  slug: serverless
seo_title: null
seo_desc: 'This worked example creates a simple Netlify Function and integrates it
  with an Elm application.

  Netlify functions provide a very convenient way of working with AWS Lambdas, and
  they have an impressive array of example use cases, such as sending emai...'
---

This worked example creates a simple [Netlify Function](https://functions.netlify.com/) and integrates it with an Elm application.

Netlify functions provide a very convenient way of working with AWS Lambdas, and they have an [impressive array of example use cases](https://functions.netlify.com/examples), such as sending emails, processing payments and logging.

This example reads secrets from environment variables (to avoid them being exposed in the browser), but it is mostly generic, and can be adapted for other use cases easily.

## Step 1 - Prerequisites

* Create a repository for the code, probably on GitHub
* `npm i -g elm`
* `npm install -g netlify-cli`
* `npm i -g create-elm-app`

## Step 2 - Create vanilla Elm app

* `create-elm-app elm-app-with-netlify-function`
* `cd elm-app-with-netlify-function`
* `elm-app start`

This should start a development server and load the app in your browser.

You can look at [this commit in the companion repository](https://github.com/ceddlyburge/netlify-functions-with-elm/commit/d976b2391f98f07113d1e41a64b0359caddf3452) to check that everything is ok.

## Step 2 - Deploy on Netlify

* `npm init` (and fill in sensible values)
* `npm i create-elm-app --save-dev` (this adds create-elm-app to package.json, which is used by netlify)
* Push the code to GitHub

You can see the results of this at [this commit in the companion repository](https://github.com/ceddlyburge/netlify-functions-with-elm/commit/aa52ccfabacae69591a920f0675eedf620ae8b03)

* Log in / Sign up / register with [Netlify](https://www.netlify.com/)
* Create a [new site](https://app.netlify.com/start) on Netlify
* Choose your repository
* Set the "Build command" to `elm-app build`
* Set the "Public directory" to `build`
* Click on "Deploy Site"

Netlify will now deploy the site, installing the dependencies specified in package.json, then running `elm-app build` and then serving the dist directory.

From now on, Netlify will attempt to deploy the latest code every time you push to GitHub.

## Step 3 - Link Netlify Dev

* `netlify login`
* `netlify link` and choose the “Use current git remote url” option
* Add “./netlify” to .gitignore
* Add a netlify.toml file (from [this commit in the companion repository](https://github.com/ceddlyburge/netlify-functions-with-elm/commit/6514012000ea82fb6625fa3686adafa321723d28))
* `netlify dev`

This should start a local development server and load the app in your browser, in a similar way to step 1.

## Step 4 - Add a netlify function

Run `netlify functions:create` to create a new netlify function. Choose the “js-token-hider” template, and name it "call-api".

This will create a javascript file for the function, and a package.json for its dependencies in “functions/call-api”.

Replace functions/call-api/call-api.js with this one in [the companion repository](https://github.com/ceddlyburge/netlify-functions-with-elm/commit/79381b9c1a7731b01f0c81b58a772d9576f76732)

Now if you run `netlify dev`,  the function will be served as well as the app, albeit on different  ports. You can view the function in the browser to check that it is  working (probably at [http://localhost:34567/call-api](http://localhost:34567/call-api) or [http://localhost:34567/.netlify/functions/call-api](http://localhost:34567/.netlify/functions/call-api))

## Step 5 - Call the netlify function from Elm

Install depdencies

* `elm install elm/json`
* `elm install elm/http`
* `elm install krisajenkins/remotedata`

Update Main.elm to call the function and display the results (from [the companion repository](https://github.com/ceddlyburge/netlify-functions-with-elm/commit/4dc9e8e4b60d061b5d5ef0fb2ce6ab856741236f)).

Instruct create-elm-app to proxy api calls to the function, by adding elmapp.config.js, as shown in [the companion repository](https://github.com/ceddlyburge/netlify-functions-with-elm/commit/90a63178e38f2919770e37fcc94e7ee0bec343ab).

At  this point, thee application runs, and successfully calls the api, but  there are no secrets / environment variables yet, so the UI shows an error.

## Step 6 - Add the secrets

Go  to the “Site Settings” - “Build & Deploy” - “Continuous Deployment”  - “Environment Variables” section on the Netlify website for your application.

Add environment variables for API_TOKEN and API_URL

Now when you run ‘netlify dev’ the app should now load in the browser and call the locally hosted netlify function, which will return the API_TOKEN and API_URL environment variables that you set on Netlify.

The  same should be true on the live deployment on Netlify. You may need to  “Trigger Deploy” manually on Netlify, so that it uses the new environment variables.

You can see the deployment of the companion repository at [https://netlify-functions-with-elm.netlify.com](https://netlify-functions-with-elm.netlify.com)

## Conclusion

Netlify  / serverless functions are extremely useful for creating / connecting to the backend services that your front end needs. They are also very east to set up, as this artcile (hopefully!) shows.

Create-elm-app is a great tool for developing Elm applications, and its simple proxy feature works well when developing Netlify functions.

Netlify Dev is great for replicating the production Netlify setup when developing locally (in this case by automatically providing the environment variables).

