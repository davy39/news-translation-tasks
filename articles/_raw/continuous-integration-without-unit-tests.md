---
title: How to Set Up Continuous Integration Without Unit Tests
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-03T09:51:00.000Z'
originalURL: https://freecodecamp.org/news/continuous-integration-without-unit-tests
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/continuous-integration-without-unit-tests.jpg
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: Productivity
  slug: productivity
seo_title: null
seo_desc: 'By Jean-Paul Delimat

  Do you think continuous integration is not for you because you have no automated
  tests? Or no unit tests at all? Not true. Tests are important. But there are many
  more aspects to continuous integration than just testing. Let''s se...'
---

By Jean-Paul Delimat

Do you think continuous integration is not for you because you have no automated tests? Or no unit tests at all? Not true. Tests are important. But there are many more aspects to continuous integration than just testing. Let's see what they are.

## **1. Building the codebase**

This is the most critical issue continuous integration should solve. The main branch of your codebase should always build/compile. It seems silly to even mention it.  

Take a team of 12. Say 1 faulty commit gets into the main branch. Everybody pulls. Here starts the process of finding out what's wrong and coordinating who should or will fix it. The confusion puts your whole team out of focus for around 30 minutes. Plus it causes frustration.

Let's say this happens once a week (everybody makes mistakes eventually). 30 minutes x 12 people is 8 lost hours per week.

If you are OK with that you might as well:

* set up a CI process preventing faulty builds from getting into the main branch
* give away a day off to one developer every week

Same outcome, happier team :)

Setting up a CI process that ensures your codebase compiles is less than half a day's work. It's worth the effort.

## **2. Static code analysis**

This comes for free in almost every language and is a one liner to run against a predefined set of rules:

* Javascript: [eslint](https://eslint.org/), [tslint](https://palantir.github.io/tslint/)
* Java: [sonarlint](https://www.sonarlint.org/)
* Python: [pylint](https://www.pylint.org/)
* Go: [golint](https://github.com/golang/lint)

Setting up the static code analysis (or linting) takes 1 hour or so. So what are the benefits? You have well-formatted and "by the book" code in your main branch. That's a clear quality increase for your code base.

If that is the least of your problems because your team is always rushing to meet deadlines, think of it this way. Your code review process will be faster. Anything that is in the area of code structure, best practices etc. is already checked by your CI process. No need to review or discuss it. Your developers can focus on the business content of code reviews.

Great bonus: developers learn the code conventions automatically. The static analysis tool provides shows you the violated rule and explains why it is wrong to do that thing.

A hurdle with conventions is that developers are dogmatic about, for example, tabs versus spaces or those sorts of things. At the end of the day good conventions are those that are followed by all. Pick a set of standard conventions and roll with them.

## **3. Culture change**

Continuous Integration is not a technical problem. It's a team process. You want to work in small increments and integrate code to the main branch often. See [How to get started with CI](https://fire.ci/blog/how-to-get-started-with-continuous-integration/) for a larger discussion on what the culture goal actually is.

After the team masters the first critical elements, another shift should happen. People will realize that working in smaller increments is more efficient. Automated checks for basic mistakes will boost your confidence so you can merge code faster. 

As a result, a branch's life span will decrease. Code review will be faster. Everybody will work with almost the latest code. It will prevent drifts and merge conflicts due to people working apart. See [Why you should not use feature branches](https://fire.ci/blog/why-you-should-not-use-feature-branches/) for a full list of benefits.

At the end of the day CI helps our pride and ego. Everybody should be happy to have a tool to catch their mistakes before they reach the world. 

## **How do you get started?**

  
Here is a very simple and actionable process to get started. It works regardless of your git provider: GitHub, Bitbucket, Gitlab, Azure DevOps, and all the others.

### **1. Enable a Pull Request (PR) process**

Lock your main branch from direct pushes. Everything should come through PRs. Here are links on how to do this for [Github](https://help.github.com/en/github/administering-a-repository/enabling-branch-restrictions), [Bitbucket](https://confluence.atlassian.com/bitbucketserver/using-branch-permissions-776639807.html#Usingbranchpermissions-Addbranchpermissionsforasinglerepository), [GitLab](https://docs.gitlab.com/ee/user/project/protected_branches.html), and [Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/repos/git/branch-policies?view=azure-devops).

### **2. Pick a CI platform**

Every git provider allows you to define build pipelines for your PRs. The builds will run when the PR is created and for each new push to the branch the PR carries. A pre condition to complete your PR (= merge your branch) will be a successful build.

The big CI players are CircleCI, Codeship, and Travis CI. I of course recommend [Fire CI](https://fire.ci/) since its the platform I've built. But I don't claim it is better than the rest for each and every use case.

Just pick one and get started.

### **3. Define a 2 liner build**

The most basic build we want to achieve is build + static code analysis. Getting there is 2 or 3 commands in a shell.

All CI platforms go for "configuration as code". You define your build in a *.yml file at the root of your repository and the platform picks it up.

With Fire CI, for example, you would need to add a .fire.yml file at the root of your repo that would look like this:

```yaml
pipeline:   
  dockerfile: Dockerfile
```

Then you add a file named "Dockerfile" to build your app. Here are a few examples of simple Dockerfiles.

Any yarn/npm based tech like React/Angular/Vue/Node:

```docker
FROM python:3 
WORKDIR /app  
COPY . . 
RUN yarn
RUN yarn lint 
RUN yarn build
```

Python:

```docker
FROM python:3
WORKDIR /app 
COPY . .
RUN pip install all_your_dependencies
RUN pylint all_your_python_files.py
```

Go:

```docker
FROM golang:latest
WORKDIR /app
COPY . .
RUN go build -o main .
```

I could go on with many more. These examples are simplistic and could be improved with a few more commands. But you get the point: it's easy.

### **Optional: Enable code reviews**

Now that every code contribution comes through a PR, code reviews are easy to do. Every git provider has an awesome UI to present the differences and allow you to comment on code.

If you are new to the process do not define a mandatory set of reviewers as it will slow your team down. Do start a best effort process to review each others' code. And build on that.

## **What then?**

As with everything, think big but start small. Having a CI process in place opens a world of opportunities.

### **Testing**

Once you have the basic process in place, it becomes a breeze to add your first automated test. And then some others. Low yet continuous effort can bring you awesome test coverage before you know it.

I recommend that you remain lean and not invest effort into writing tests. Check what breaks often or requires a lot of effort to test manually. Automate that.   
Always keep productivity in mind. Having a ton of tests just because is worth nothing.

### **Other perks**

There are many tools out there that you can integrate to your CI process. They are not key but the effort versus benefits could be worthwhile.

A few examples are below. Links are for the GitHub marketplace but other git providers integrate as easily.

* Automatic update of dependencies: [Depfu](https://github.com/marketplace/depfu) suggests dependencies to you to update automatically. This way you remain up to date doing small increments. This is always better than a once a year "let's bump everything" strategy.
* Open source security: [Snyk](https://github.com/marketplace/snyk) warns you about security threats in open source libraries.
* Images optimisation: [ImgBot](https://github.com/marketplace/snyk) detects large images in your repository and submits a PR with size optimized version. Relevant for front end projects, but still nice.

There are many more out there. Browse the marketplace for things that could solve a problem for you.

Careful though! Resist the urge to use everything that comes to mind. Pick the ones that really provide a productivity boost. Free metrics or tools that you don't consider carefully are harmful as people are not sure what to do with them.

## **Conclusion**

You do not need fancy tests suites to get started with Continuous Integration. 

Literally 2 hours of effort can get you rolling. And it'll enable a virtuous circle for your team's productivity.

The bigger your team and your projects, the greater the benefits. In 2020 there is no good reason to not have a CI process.

Feel free to [contact me](https://twitter.com/jpdelimat) if you need help setting up a CI process for your team. I'll be happy to help if I can.

Thanks for reading and good luck!  
  
_Originally published on The Fire CI Blog._

  
  
  
  

