---
title: How to Build a Simple Deployment Pipeline with Reusable Github Actions and
  Heroku
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-31T17:25:11.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-simple-deployment-pipeline-with-reuable-github-actions-and-heroku
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/AdobeStock_131006414-1.jpeg
tags:
- name: deployment
  slug: deployment
- name: GitHub Actions
  slug: github-actions
- name: Heroku
  slug: heroku
seo_title: null
seo_desc: "By Liz Johnson\nIf you've been using GitHub for a while, you've probably\
  \ heard of or used GitHub actions. \nIf you haven't heard of Github Actions or used\
  \ them before, you can use them for automating your build, test, or deployment pipelines.\
  \ You can c..."
---

By Liz Johnson

If you've been using GitHub for a while, you've probably heard of or used GitHub actions. 

If you haven't heard of Github Actions or used them before, you can use them for automating your build, test, or deployment pipelines. You can create workflows that will be triggered upon certain actions such as opening a pull request or pushing to a branch.  

These actions are useful to create build pipelines that automate deployments. They also help maintain the integrity of branches by running tests on all pushes/pull-requests.

Here is a simple workflow that would run tests whenever you push branches or open pull-requests in Github:

```
---
name: Run tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup and Run Tests
        run:  |
          docker-compose build
          docker-compose run web rake db:setup
          docker-compose run web rspec
```

The trigger is listed after the "on" tag. This workflow is triggered on pushes to the remote. Below you will see examples where there are multiple triggers for the workflow. If you have multiple triggers you can list the triggers in brackets like an array.  

Next, you have your jobs tag. Under this tag you can list the various jobs you want to run. You may have a few different test jobs for unit tests, integration tests, and then perhaps a build job to build an image that gets pushed to a remote repository.  
  
Within the job you have various steps. The first step is usually the checkout step. GitHub actions will spin up a virtual machine runner to run your jobs in, so you will want to include all the steps you need to set up this virtual machine for your application. 

This means the first thing you'll want to do is get the code onto the virtual machine. This happens with the checkout step above. 

Then your job needs give GitHub instructions on how to run things like the tests. The workflow above is running everything through Docker. The GitHub runner can see the docker-compose file when it checks out the project. Then it can run the three Docker steps listed above to spin up a container and then run the unit tests inside that container.  
  
With this workflow if you were to open a pull-request in GitHub and the branch had failing tests, you'd get an alert telling you that your introducing breaking changes with an output like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-189.png)
_Sample GitHub Actions alert_

These workflows can sometimes become complex and very involved. In this tutorial, I will explain some simple ways to cleanup your workflows to avoid copy-pasting yaml configurations.  

I will then go on to explain how you can create a simple deployment pipeline that enforces that one job passes before the other one runs.

## Where You Might Find Duplicate Jobs

Say you have a job that runs your tests, and that job needs to be run in multiple different workflows. You want to run tests on all pull-requests. You also want to run them on merges to main in a way that blocks the production build/deploy step if the tests don’t pass.

Perhaps your first idea here is to build two workflows, one named test and the other named deploy. The test workflow would have one job: to set up and run all unit tests. In the other workflow you can copy the yaml from the test job in the test workflow and paste it as the first job in your deploy workflow. 

Your test workflow would look something like this:

```
---
name: Run tests
on: pull-request

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup and Run Tests
        run:  |
          docker-compose build
          docker-compose run web rake db:setup
          docker-compose run web rspec

```

And your deployment workflow would look something like this:

```
---
name: Deploy
on:
  push:
    branches: [main]

jobs:
  tests:
  	runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup and Run Tests
        run:  |
          docker-compose build
          docker-compose run web rake db:setup
          docker-compose run web rspec
  deploy:
    name: deploy
    runs-on: ubuntu-latest
    steps:
      - run: echo 'The triggering workflow succeeded deploying now'
      - uses: actions/checkout@v2
      - uses: akhileshns/heroku-deploy@v3.12.13 # This is the action
        with:
          usedocker: true

```

The deploy workflow allows both jobs (test and deploy) to run on merges to main, but it actually won’t block the deploy job from running if the tests fail. 

But we can make this better in two ways: the first is by using reusable GitHub actions so that we can eliminate the copy pasting of the job yaml. Second, is using the GitHub job “needs” keyword so that we can make our deploy job depend on our test job succeeding.

I built this out [here](https://github.com/lizzypy/base-app-liz) and will be going through that example. 

## How to Create Reusable Github Actions

Github has [a blog post about reusable actions](https://github.blog/2022-02-10-using-reusable-workflows-github-actions/) that I recommend. It goes a bit further than I will go here. But the important information for us is the explanation of what a reusable action is.  A reusable action is one where you create a job in one place and then call it a separate workflow.

If I wanted my test workflow to be re-useable, I'd need to add a trigger labeled "workflow_call".  I also want my workflow triggered on push and pull-requests. So my triggers would look something like this:

```
---
name: Run CI Process for the app
on: [workflow_call, push, pull_request, workflow_dispatch]
```

And the full workflow would look like this:

```
---
name: Run tests
on: [workflow_call, push, pull_request, workflow_dispatch]


jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Setup and Run Tests
        run:  |
          docker-compose build
          docker-compose run web rake db:setup
          docker-compose run web rspec
```

To reuse the test workflow in a deploy workflow (where I want to run tests and deploy my application) I could do something like the following:

```
jobs:
    test:
        uses:./.github/workflows/test.yml
```

This would allow the test job to be run in a separate workflow without having to copy the yaml associated with the test job from one workflow to another.

## Dependent Jobs

That’s cool, but we don’t just want our test job to be reused in our deploy workflow. If the test job happens to fail in the deploy workflow, we actually want that to _block_ deployment.

Now, we can look at the “needs” keyword which is documented [here](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions). Using “needs” we can require that the deploy job won’t even run unless the test job is successful.

Before I jump into using the "needs" tag, let me briefly explain what the deployment job is doing. 

I have deployed the example app using Heroku. Instead of using the Heroku Git remote, I open pull-requests against a main branch. On merges to main I use this [open source Github action](https://github.com/AkhileshNS/heroku-deploy) to deploy the main branch to Heroku.  

My deploy job will look something like this:

```
deploy:
    name: deploy
    runs-on: ubuntu-latest
    steps:
      - run: echo 'The triggering workflow succeeded deploying now'
      - uses: actions/checkout@v2
      - uses: akhileshns/heroku-deploy@v3.12.13 # This is the action
        with: 
            usedocker: true
```

The "usedocker" tag above specifies that I want to deploy this application to Heroku by building a pushing a docker image to the Heroku Container Registry. If you look through the source code for the Heroku deploy action that is referenced above, you’ll see that when I set "usedocker" to "true" it will run this command:

`heroku container:push`

That can be seen [here](https://github.com/AkhileshNS/heroku-deploy/blob/master/index.js#L76).

If we want this job to require the a successful test run before we run the deploy job, we can add a test job to our workflow that references our reusable test job that we created:

```
---
name: Deploy
on:
  push:
    branches: [main]

jobs:
  tests:
    uses: ./.github/workflows/test.yml 
```

Now we can add the `needs` tag to our deployment action and our full workflow yaml will look something like this:

```
---
name: Deploy
on:
  push:
    branches: [main]

jobs:
  tests:
    uses: ./.github/workflows/test.yml
  deploy:
    name: deploy
    needs: [ tests ]
    runs-on: ubuntu-latest
    steps:
      - run: echo 'The triggering workflow succeeded deploying now'
      - uses: actions/checkout@v2
      - uses: akhileshns/heroku-deploy@v3.12.13 # This is the action
        with:
          usedocker: true
```

And that's it! Now when we merge branches to main, GitHub gives us a visual of our dependent jobs that looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-159.png)

  
If we had a more complex workflow we could see exactly which job it is failing on. 

## Wrapping Up

With these steps, we can clean up our workflow yamls to reference existing jobs/workflows when possible. We can also build a simple pipeline of dependent actions where one steps depends on the success of a previous step.  

These are the beginnings of CI/CD pipeline that can allow for frequent deploys. In turn it will allow us to get new features and fixes to users faster.  

