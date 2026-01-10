---
title: The Ultimate Guide to End to End Tests with Selenium and Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-16T22:46:40.000Z'
originalURL: https://freecodecamp.org/news/end-to-end-tests-with-selenium-and-docker-the-ultimate-guide
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/end-to-end-testing-selenium-docker.jpg
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: Docker
  slug: docker
- name: Docker compose
  slug: docker-compose
- name: selenium
  slug: selenium
- name: Software Testing
  slug: software-testing
seo_title: null
seo_desc: 'By Jean-Paul Delimat

  Automated end to end testing is the most effective way to test your app. It also
  requires the least effort to get the benefit of tests if you currently have no tests
  at all. And you don’t need a ton of infrastructure or cloud ser...'
---

By Jean-Paul Delimat

Automated end to end testing is the most effective way to test your app. It also requires the least effort to get the benefit of tests if you currently have no tests at all. And you don’t need a ton of infrastructure or cloud servers to get there. In this guide we’ll see how we can easily overcome the two main hurdles of end to end testing.

The first hurdle is Selenium. The API you use to write tests is ugly and non-intuitive. But it is not that difficult to use, and with a few convenient functions it can become a breeze to write Selenium tests. The effort is well-rewarded because you can automatically test your end users' flows end to end.

The second hurdle is putting components together in an isolated environment. We want the frontend, the backend, the database and everything else your app uses. We will use Docker compose to put things together and automate the tests. It is easy even if you have your components in different Git repositories.

## Writing end to end tests in Selenium

Even if you are an API only business, you have a frontend, and an admin or back office frontend. So end to end tests ultimately talk to a frontend application. 

The industry standard tool is Selenium. Selenium provides an API to talk to the web browser and interact with the DOM. You can check what elements are displayed, fill inputs and click around. Anything a real user would do with your application, you can automate.

Selenium uses something called the WebDriver API. It is not very handy to use at first glance. But the learning curve is not steep. Creating a few convenience functions will get you productive in no time. I won’t go into the details of the WebDriver API here. You can have a look at [this excellent article](https://marmelab.com/blog/2016/04/19/e2e-testing-with-node-and-es6.html) to dig deeper.

There are also libraries to make your life easier. [Nightwatch](https://nightwatchjs.org/) is the most popular.

If you have an Angular application, [Protractor](https://www.protractortest.org/) is your best friend. It integrates with the Angular event loop and allows you to use selectors based on your model. That is gold.

Writing a test for your most critical user feature or your app should take only a few hours, so go ahead. It will run automatically ever after. Let's see how.

## Running your tests in Docker

We need to run our tests in an isolated environment so the outcome is predictable. And so we can enable [Continuous Integration](https://fire.ci/blog/how-to-get-started-with-continuous-integration/) easily. We'll use Docker compose.

Selenium provides Docker images out of the box to test with one or several browsers. The images spawn a Selenium server and a browser underneath. It can work with different browsers.

Let’s start with one browser for now: headless-chrome. You can see the _docker-compose.yml_ file below (the commands are from an Angular example).

Note: If you've never used Docker you can easily install it on your computer. Docker has the troublesome tendency of forcing you to sign up for an account just to download the thing. But you actually don't have to. Go to the release notes ([link for Windows](https://docs.docker.com/docker-for-windows/release-notes/) and [link for Mac](https://docs.docker.com/docker-for-mac/release-notes/)) and download not the latest version but the one right before. This is a direct download link.

```
version: '3.1'

services:
 app-serve:
   build: .
   image: myapp
   command: npm run serve:production
   expose:
    - 4200

 app-e2e-tests:
   image: myapp
   command: dockerize -wait tcp://app-serve:4200 
             -wait tcp://selenium-chrome-standalone:4444 
             -timeout 10s -wait-retry-interval 1s bash -c "npm run e2e"
   depends_on:
     - app-serve
     - selenium-chrome-standalone

 selenium-chrome-standalone:
   image: selenium/standalone-chrome
   expose:
    - 44444
```

The file above tells Docker to spin up an environment with 3 containers:

* Our app to test: the container uses the myapp image which we’ll build right below
* A container running the tests: the container uses the same myapp image. It uses [dockerize](https://github.com/jwilder/dockerize) to wait for the servers to be up before running the tests
* The Selenium server: the container uses the official Selenium image. Nothing to do here. We could run the tests from the same container as the app. Splitting it makes things clearer. It also allows you to separate outputs from the 2 containers in the result logs.

The containers will live inside a private virtual network and see each other as http://the-container-name (more [here](https://docs.docker.com/compose/networking/) on networking in Docker).

We need a _Dockerfile_ to build the _myapp_ image used for the containers. It should turn your frontend code into a bundle as close to production as possible. Running unit tests and linting is a good idea at that stage. After all, there's no need to run end to end tests if the basics do not work.

In the _Dockerfile_ below we use a node image as base, install dockerize, and bundle the application. It is important to build for production. You don’t want to test a development build that is pre-optimizations. Many things can go wrong there.

```
FROM node:12.13.0 AS base

ENV DOCKERIZE_VERSION v0.6.0

RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
   && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
   && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN mkdir -p ~/app
WORKDIR ~/app

COPY package.json .
COPY package-lock.json .

FROM base AS dependencies

RUN npm install

FROM dependencies AS runtime

COPY . .
RUN npm run lint
RUN npm run test:ci
RUN npm run build --production
```

Now that we have all the pieces together let's run the tests using this command:

```
docker-compose up --build --abort-on-container-exit
```

It is long-ish, so script it in your project somehow. It will build the myapp image based on the provided _Dockerfile_ and then start all the containers. Dockerize makes sure your app and Selenium are up before executing the tests.

The _--abort-on-container-exit_ option will kill the environment when one container exists. Since only our testing container is meant to exit (the others are servers), that is what we want. 

The docker-compose command will have the same exit code as the exiting container. It means you can easily detect from the command line if the tests succeeded or not.

You are now ready to run end to end tests locally and on any server supporting Docker. That's pretty good!

The tests run with only one browser for now, though. Let’s add more.

## Testing on different browsers

The standalone Selenium image spins up a Selenium server with the browser you want. To run the tests on different browsers you need to update your tests' configuration and use the selenium/hub Docker image.

The image creates a hub between your application and the standalone Selenium images. Replace the selenium container section in your docker-compose.yml as follows:

```
  selenium-hub:
    image: selenium/hub
    container_name: selenium-hub
    expose:
      - 4444
  chrome:
    image: selenium/node-chrome
    volumes:
      - /dev/shm:/dev/shm
    depends_on:
      - selenium-hub
    environment:
      - HUB_HOST=selenium-hub
      - HUB_PORT=4444
  firefox:
    image: selenium/node-firefox
    volumes:
      - /dev/shm:/dev/shm
    depends_on:
      - selenium-hub
    environment:
      - HUB_HOST=selenium-hub
      - HUB_PORT=4444
```

We now have 3 containers: Chrome, Firefox and the Selenium hub.

All the Docker images provided by Selenium are [in this repository](https://github.com/SeleniumHQ/docker-selenium).

Careful! There is a tricky timing effect to consider. We use dockerize to have our test container wait for the Selenium hub to be up. That is not enough because we need to wait for the standalone images to be ready – in fact to register themselves to the hub.

We can do this by waiting for the standalone images to expose a port, but that is not a guarantee. It is easier to wait a few seconds before starting the tests. Update your test script to wait 5 seconds before the tests start (you can add a sleep command after the dockerize call).

Now you can be sure that your tests won’t start until all the browsers are ready. Waiting is not ideal but a few seconds are worth it. There is nothing more annoying than failing tests because of unstable automations.

Good. We have now covered the front end part. Let’s add the back end.

## Add the back end as containers or git modules

The above might seem overkill to test only the front end part of your app. But we're aiming for much more. We want to test the whole system.

Let’s add a database and a back end to our Docker compose environment.

If you are a front end developer you might think "we are the front end team – we don’t care about testing the back end." Are you sure?

> The front end is always the last part to integrate all the other pieces. That means crunch time. Crunch time that would no longer exist if you were able to test the front end with the back end continuously and catch errors sooner.

The technique I describe here is very easy to apply even if your back end is in a different repository.

This is what the _docker-compose.yml_ looks like:

```
version: '3.1'

services:
 db:
   image: postgres
   environment:
     POSTGRES_USER: john
     POSTGRES_PASSWORD: mysecretpassword
   expose:
     - 5432
 backend:
   context: ./backend
   dockerfile: ./backend/Dockerfile
   image:mybackend
   command: dockerize
       -wait tcp://db:5432 -timeout 10s
       bash -c "./seed_db.sh && ./start_server.sh"
   environment:
     APP_DB_HOST: db
     APP_DB_USER: john
     APP_DB_PASSWORD: mysecretpassword
   expose:
     - 8000
   depends_on:
     - db
 app-serve:
   build: .
   image: myapp
   command: npm run serve:sw
   expose:
    - 4200
 app-e2e-tests:
   image: myapp
   command: dockerize -wait tcp://app-serve:4200 
        -wait tcp://backend:8000 
        -wait tcp://selenium-chrome-standalone:4444 -timeout 10s 
        -wait-retry-interval 1s bash -c "npm run e2e:docker"
   depends_on:
     - app-serve
     - selenium-chrome-standalone
 selenium-chrome-standalone:
   image: selenium/standalone-chrome
   expose:
    - 44444
```

In this example we added a postgres database and a container for the back end to run. Dockerize synchronizes the containers' commands.

If your system has more than one back end component, add as many containers as you need. You need to wire the container dependencies properly. This means proper hostnames as environment variables on your components. And order of startup if some components depend on others.

The Selenium tests you have written should not need any modifications. You might need to put test data in the database. To keep this step in the testing area we added the seeding script before the backend startup script. This way we are sure that things happen in the proper order:

* The DB starts and is ready to accept connections
* A script seeds the DB data
* The back end and the front end start – so the tests can start

### Monorepository

If you look at the back end container you can see there is a catch. It uses an image called _mybackend_ built from a file located at _backend/Dockerfile_. This implies that your back end is in the same git repository in a folder called _backend_. The name is just an example of course.

If your back end and front end are in the same repository you are good. Define the Dockerfile to build your back end and adjust the startup command to what you need.

That’s all good but usually the back end is not in the same repository. Or you can have many back end components in different repositories. What do you do then?

### Multiple repositories

The super clean solution is to have a CI process on each back end component repository. 

If you don’t have any you can check out the [API end to end testing with Docker](https://fire.ci/blog/api-end-to-end-testing-with-docker/) guide to get started. It uses the same techniques as this article so you have a consistent setup across your whole project.

The CI process for each component runs automated tests. Upon success it pushes a docker image with the component to a private Docker registry. The back end container in our _docker-compose.yml_ file above would use this image.

This solution requires a private Docker registry to store your images. You can use [Docker Hub](https://hub.docker.com/) but then it becomes public. If you don't have one already and don’t plan to do so, it is not worth the effort.

The other solution is to use the submodules feature in git. Your back end repository becomes a virtual child of your front end repository. You just need to add the file _.gitmodules_ like this to your front end repository:

```
[submodule "backend"]
  path = backend
  url = git@your:backend/repository.git
  branch = develop
```

Run the command _git submodule update --remote_ which will pull the specified branch of the back end repository into a folder called "backend". Add as many submodules as you need if you have more than one back end component.

That’s it. Have your CI run the submodule command and from a file system perspective it's as if you're in a monorepository. 

If you don’t want the back end code locally while developing the front end just don’t run the command. You’ll have an empty back end folder.

### Versioning and back end/front end incompatibilities

The 2 techniques above test the front end with the latest “CI tests passed” version of your back end. That may lead to broken builds if your components are not compatible at times.

If they are compatible more often than not, stick to the “always test with the latest versions” approach. You’ll fix the occasional incompatibilities on the fly.

That won’t work, though, if incompatibilities are business as usual. In this case you need to manually control version updates. That is very easy to do.

You can lock the version of a component in the _docker-compose.yml_ file or in the _.gitmodules_ file. When pushing to the Docker registry you would tag the component image with the commit number of the corresponding code. The relevant docker-compose.yml file section becomes:

```
backend:
  image: backendapp:34028fc
```

Similarly the _.gitmodules_ file would not target a branch head but a given commit:

```
[submodule "backend"]
  path = backend
  url = git@your:backend/repository.git
  branch = 34028fc
```

Bonus: version updates are versioned with your code. You can track which version was used for each build. This is useful when fixing failed builds or trying to reproduce old bugs.

We could push the approach to the next level. You could have a dedicated repository that would wire all your components as git modules. Bumping the versions could be a form of delivery and handover to the test/QA team.  

In theory it is best to keep the latest versions of components working together more often than not. And drop the need for manual versioning. If that is not the case that is OK. Ignore the purists who will tell you that you are not following best practices and so on.

> If you are just starting don't aim for the stars at first. Pick what works best for you to enjoy the benefits of automated testing right now. Then keep improving your process along the way.

## Bonus on writing maintainable Selenium tests

Back to Selenium and three important bits of advice to help you write good UI tests.

First, avoid CSS selectors if you can. Selenium works on the DOM and can identify elements by IDs or CSS or XPath. Use IDs as much as possible even if you have to add them to your app code for only this purpose. CSS and XPath selectors are shaky. As soon as your application structure changes, they will be broken.

Second, use the Page Objects approach. It is about encapsulating your application so selectors are not directly used in tests. If your page HTML/CSS changes, your tests will have to be rewritten to use new selectors. Page Objects abstract selectors and turn them into user actions. Here is a great article on [how to use Page Objects properly](https://johnfergusonsmart.com/page-objects-that-suck-less-tips-for-writing-more-maintainable-page-objects/).

Third, don’t build long user journeys in your tests. If your tests fail at the 50th action it’s going to be difficult to reproduce and fix. Create test suites that play part of the scenarios starting from the login page. This way you are always a few clicks away from the bug your tests will catch.

Also don’t risk writing tests that rely on state from previous actions. Test suite coupling is something you want to avoid. 

Let's take a practical example. Say you are testing a SaaS application for schools. The use cases could be:

* Create a class
* Register kids' and parents' data
* Setup the weekly plan for the class
* Check absences
* Input grades

Along the way you will have the login process and some navigation checks.

You could write a test that goes through the whole chain as described above. And this would be convenient because to declare kids you need a class to exist. To check absences you need a weekly plan in place. And you need kids to input grades. It’s a quick win to build one test suite that does all these things at first.

If you have nothing at the moment and want to achieve good test coverage quickly: go for it! Done is better than perfect if it allows you to catch errors in your application now.

The cleaner solution would be to use a baseline scenario to start smaller test suites. In the example above the baseline scenario should be to create a class and register kids' data.

Create a test suite that does exactly that: create a class and registered kids' and parents' data. Always run it first. If this stops working then you don’t need to move further on. This version of the code will never reach end users anyway.

Then create a function that encapsulates the baseline scenario. It will be duplicate code to some extent with the previous test suite. But it will allow you to have a one line function to use as a setup hook for all the other test suites. This is the best of both worlds: test scenarios starting from a fresh state in the application with minimal effort.

## Conclusion

I hope this article gave you some good insight into how you can quickly set up end to end tests for a complex system. Multiple components in multiple repositories should not be a barrier. Docker compose makes it easy to put things together.

End to end tests are the best way to avoid crunch time. In complex systems, late delivery of some components puts a burden on other teams. Integrations are done in a rush. Code quality drops. That's a vicious circle. Testing often and catching cross component errors early is the solution.

Selenium tests can be done quick and dirty to get going fast. That is perfectly OK. Automate things. Then improve. Remember:

> Done is better than perfect any day of the year.

Thanks for reading! 

_If you want more of my articles like this, you can find them on [The Fire CI Blog](https://fire.ci/blog)._  

