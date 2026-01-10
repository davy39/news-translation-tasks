---
title: How to set up continuous integration and deployment for your React app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-16T01:27:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-continuous-integration-and-deployment-for-your-react-app-d09ae4525250
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PJiNN3izrhZXN6TNm0koMg.png
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Zac Kwan

  Setting up a React development environment can be confusing and daunting to newcomers.
  You might have heard developers talking about how different packages like babel,
  Webpack and so on, are needed as well (but this is debatable).

  With Re...'
---

By Zac Kwan

Setting up a **React** development environment can be confusing and daunting to newcomers. You might have heard developers talking about how different packages like **babel**, **Webpack** and so on, are needed as well (but this is debatable).

With React getting more popular, there are a few boilerplate projects that aim to help developers create a suitable React development environment. [**create-react-app**](https://github.com/facebookincubator/create-react-app) is one of the most popular starter templates.

It aims to allow developers to create a react app with **zero build configuration**.

Developers no longer have to worry about how `webpack` should be setup, what should be configured with `babel` to use `es6`, or which `linter` and `test` package to use. Everything will just work out of the box. **Yes, it is so easy!**

For developers who need to manage the underlying configuration, it has a `npm run eject` that allows them to mess with the configuration and do what they couldn’t do previously. The only thing to note is that once `eject` is run, it cannot be reversed.

### Development Stack for React

I wrote the following guide to help developers build a **Continuous Integration and Continuous Deployment stack for their React app**. We will be using [**CircleCI**](https://circleci.com), [**CodeClimate**](https://codeclimate.com)**,** and [**Heroku**](https://heroku.com). If you do not have an account at any of the services above, head over to sign up — they’re FREE!

At the end, we will have a React app in a [Github Repo](https://github.com/Zaccc123/awesome-cicd-react) that will automatically deploy any changes on `_master_` branch to [**Heroku**](https://heroku.com) after all tests pass. [Here](https://awesome-cicd-react.herokuapp.com) is a sample of the deployed **React** website.

#### **Let’s Start!**

The first step is to follow the [**create-react-app**](https://github.com/facebookincubator/create-react-app) guide to create a new React app. Do this:

```
$ npm install -g create-react-app$ create-react-app my-react-app$ cd my-react-app/$ npm start
```

Then the browser should automatically open a page at [http://localhost:3000/](http://localhost:3000/](http://localhost:3000/).). If you see a **Welcome to React** page running, everything is good.

#### **CircleCI Setup**

Next, we need to add a little configuration to setup [**CircleCI**](https://circleci.com) for our project. Create a `.circleci` folder and a `config.yml` in that directory and add the following:

```
version: 2jobs:  build:    docker:      - image: circleci/node:8    steps:      - checkout      - restore_cache: # special step to restore the dependency cache          key: dependency-cache-{{ checksum "package.json" }}      - run:          name: Setup Dependencies          command: npm install      - run:          name: Setup Code Climate test-reporter          command: |            curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 > ./cc-test-reporter            chmod +x ./cc-test-reporter      - save_cache: # special step to save the dependency cache          key: dependency-cache-{{ checksum "package.json" }}          paths:            - ./node_modules      - run: # run tests          name: Run Test and Coverage          command: |            ./cc-test-reporter before-build            npm test -- --coverage            ./cc-test-reporter after-build --exit-code $?
```

This setup is for [CircleCI 2.0](https://circleci.com/docs/2.0/). They are sunsetting [Circle 1.0](https://circleci.com/docs/1.0/) on August 31, 2018.

The `build` step sets up a `node:8` with a Docker image. It requires `v6` or higher to work.

In `steps`, we first check out the project, restore from the cache if any, then install dependencies. We also install `cc-test-reporter`, a tool provided by CodeClimate to send a coverage report.

We then run the `test` between the `before-build` and `after-build` commands according to [CodeClimate docs.](https://docs.codeclimate.com/docs/configuring-test-coverage) This notifies CodeClimate of the pending report and when completed, it either sends the report or a failure status.

#### **Setup Git**

Create a repo in [**Github**](https://github.com) and do the following:

```
$ git init$ git remote add origin git@github.com:username/new-repo-here$ git add .$ git commit -m “first commit”$ git push -u origin master
```

This will push the project that we’ve created into GitHub.

#### **Build and Test the Project**

Head over to [**CircleCI**](https://circleci.com), sign in, and build the newly created project. At the end of the build, you should see a failure on the `Run Test and Coverage`.

![Image](https://cdn-media-1.freecodecamp.org/images/xfFDemobQXl0bQqLcFTPlYH2nbZrCbSOSTey)

### **Setup CodeClimate**

The above failure is because we are not authorized to post a report to CodeClimate yet. So, now, head over to [**CodeClimate**](https://codeclimate.com), sign in and build the created GitHub project. We should get this at the end of the analysis:

![Image](https://cdn-media-1.freecodecamp.org/images/KbRpYcTUdK-5JfYQkC4PtenUIGlAEUKfRckI)
_codeclimate analyse_

In order to fix the CircleCI issue and use `Test Coverage` feedback, we will need the `Test Reporter ID`. This can be retrieved at the `Settings > Test Cover`age tab. Copy t`he Test Reporter` ID without sharing it with anyone.

In [**CircleCI**](https://circleci.com), navigate to `Project > Settings > Environment va`riable an`d add CC_TEST_REPOR`TER_ID with the c`opied Test Repor`ter ID.

![Image](https://cdn-media-1.freecodecamp.org/images/hwSIlgr-NHjjVUsevYMsgvQ2EKWolGDHi5td)

### **Heroku Deployment Setup**

In order to deploy React on [**Heroku**](https://heroku.com) , we will use a [buildpack](https://github.com/mars/create-react-app-buildpack). Do the following:

```
$ heroku create REPLACE_APP_NAME_HERE — buildpack https://github.com/mars/create-react-app-buildpack.git$ git push heroku master$ heroku open
```

We pushed the latest `master` branch to `heroku` with `git push heroku master`. A webpage will be open at the end showing the **Welcome to React** page.

Next, we will have to navigate to the newly create app in [**Heroku Dashboard**](https://dashboard.heroku.com/apps) to setup automated deployment. Do the following on the dashboard:

* Go to **Deploy** tab and **Connect** to the correct GitHub repo.
* **Enable** Automatic deployment and **check** `Wait for CI to pass before deploy`.

![Image](https://cdn-media-1.freecodecamp.org/images/FVc8xtFqrBOMAIGYlRpSJJ1PBnlfCitMxkHr)
_enable automatic deployment_

### **We are done!**

With a few steps, we have a fully automated continuous integration and deployment suite ready. Now with every commit that is pushed to [**GitHub**](https://github.com), it will send a trigger to [**CircleCI**](https://circleci.com) and [**CodeClimate**](https://codeclimate.com). Once the test has passed, if it was on the master branch, it will also be automatically deployed to [**Heroku**](https://heroku.com)**.**

View the sample repo [**here**](https://github.com/Zaccc123/awesome-cicd-react) and the deployed website [**here**](https://awesome-cicd-react.herokuapp.com)!

### Conclusion

This is an update of my previous [post](https://medium.com/@Zaccc123/https-medium-com-zaccc123-continuous-integration-and-deployment-setup-for-react-app-7b5f4bd76cdd) almost a year ago. The use of CircleCI has been updated to `2.0` , and we also use the updated `cc-test-reporter` by `CodeClimate`. If you are interested in the migration, you can look at the [pull request](https://github.com/Zaccc123/awesome-cicd-react/pull/3).

### Thanks for reading! If you like it, please hit ???

I enjoy reading and writing about tech and products especially related to boosting the productivity of developers. You can say hello to me on my [Twitter](https://twitter.com/Zaccc123) or my [blog](https://zackwan.app).

