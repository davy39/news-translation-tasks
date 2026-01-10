---
title: How to automate Code Reviews on Github
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-24T22:22:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-automate-code-reviews-on-github-41be46250712
coverImage: https://cdn-media-1.freecodecamp.org/images/1*i_C4bry8eP6mlT3OqVo45A.jpeg
tags:
- name: '#chatbots'
  slug: chatbots
- name: code
  slug: code
- name: GitHub
  slug: github
- name: Productivity
  slug: productivity
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Mukesh Thawani

  Creating pull requests and reviewing them are two of the most common tasks in a
  developer’s daily schedule. Most projects have common guidelines which developers
  need to follow while creating and reviewing the pull requests.

  Now, it...'
---

By Mukesh Thawani

Creating pull requests and reviewing them are two of the most common tasks in a developer’s daily schedule. Most projects have common guidelines which developers need to follow while creating and reviewing the pull requests.

Now, it is hard for developers to remember every guideline while making a pull request. It is even more difficult for reviewers to ensure that every line of code is compliant to the set guidelines.

We faced the same problem with our projects and solved it by automating the major part of the manual rote work. This made the lives of our developers and reviewers a lot easier. They spent more time improving code quality and less on common chores.

In this article, I will describe exactly how we did it, what all aspects of the process we automated and the tools we used for this.

![Image](https://cdn-media-1.freecodecamp.org/images/Kxybxb-zIXEpPgFUVpgyt5xnrnPhjVk-YG14)
_200 million plus pull requests created on Github. Source: Octoverse_

### Automate styling issues

We don’t want our reviewers asking the contributors to add the corresponding Jira issue number and description whenever they make a pull request. Instead, we have deployed a bot that does all the regular checks. This helps contributors to follow project guidelines.

Yes, a bot can verify if the description is present or not by checking the body of the pull request. It can comment on a pull request if the description is missing.

![Image](https://cdn-media-1.freecodecamp.org/images/h7n4CPzzBvjkUfIT30AQ48qJ0ksUOCYrv-La)
_Applozic Bot commenting on pull requests._

We can also add a [pull request template](https://help.github.com/articles/creating-a-pull-request-template-for-your-repository/) to get some of the information related to the pull request. But this approach increases the friction required to create a pull request. When we add rules, we need to make sure that the experience of a new developer will be as frictionless as possible. At the same time, we need to maintain the code quality.

Now let’s look at the steps required in creating such a bot.

### ‘Danger’ to the rescue

> [_Danger_](http://danger.systems/) _runs during your CI process, and gives teams the chance to automate common code review chores. This provides another logical step in your build, through this Danger can help lint your rote tasks in daily code review._

> _You can use Danger to codify your team’s norms. Leaving humans to think about harder problems. She does this by leaving messages inside your PRs based on rules that you create with the Ruby scripting language. Over time, as rules are adhered to, the message is amended to reflect the current state of the code review._

> _Danger is used in all sorts of projects: ruby gems, python apps, Xcode projects, blogs, npm websites and modules._

It will give you an abstraction on top of Github’s API to get details related to a pull request and perform the necessary checks. It is created and maintained by Orta and many other awesome contributors. After installation, you need to create a file named Dangerfile which will contain all the rules. This file should be present in the root of your project.

After adding this file you are all set with the rules. Now you need to run Danger every time someone creates a pull request.

### Adding it to your CI workflow

We use Bitrise in our mobile SDK projects. It’s a Continuous Integration and Continuous Delivery service for mobile Apps. If you are using a different CI service then, you can check this [guide](https://danger.systems/guides/getting_started.html#continuous-integration) on how you can integrate Danger with that service. There is a detailed [blog post](https://blog.bitrise.io/danger-danger-uh-that-is-using-danger-with-bitrise) on integrating Danger with Bitrise. I will summarise it in five points:

* Install bundler, create a Gemfile and add the Danger gem to the Gemfile.
* Create a Dangerfile for your project.
* Create a bot user on Github and a Personal Access Token for the bot.
* Then add the generated token on Bitrise.
* Add a script step in the project’s workflow. That’s it! ?

### Rules which we can Automate

One of the ways to identify what rules we can automate is by looking at Github’s pull request API response. By comparing the API response with our pull request checklist or guideline, we can get an idea of the possibilities that are there. This is how the response looks like:

![Image](https://cdn-media-1.freecodecamp.org/images/svTngozizNzNJo2tIyJDAFWyppgAL-dLHRgW)
_Response from Github’s pull request API_

* It returns almost all the information you see on GitHub’s pull request webpage like title, description, assignee, reviewers, labels etc.
* There’s one more API to fetch a list of changed files. For each file, it will return the name of the file, the number of additions to the file, the number of deletions to the file.
* We don’t have to use this APIs as we will be using Danger which gives us an easy way to interact with this data.

![Image](https://cdn-media-1.freecodecamp.org/images/3eWH5zzgFStXBVRrFH0wGwaf7BcdDO4M3gOV)
_Response from Github’s list pull requests files API_

### List of Rules we Automated

When we were adding Danger to our repository we looked at our requirements and some of the other projects which were using Danger. Below are **some of the checks** that we have in our projects.

* **Warn if it’s a big PR**: We tend to make this mistake of pushing a lot of changes in one PR. Reviewing such PRs is a difficult task. We added a warning which shows up when the number of lines updated in a PR is more than 500.
* **Encourage pull request descriptions**: Sometimes developers think that description is not necessary or we forget to add. Even though you mentioned the issue number, a brief description always helps and gives a context to the pull request. To see if the description is empty or not we can check the body length:

![Image](https://cdn-media-1.freecodecamp.org/images/cIc1nvWw2LtsPkplGfFyTYfVHIHbo3knjsL1)

* **Check if the tests are missing**: We all know tests are important and yet we tend to skip this step. Whenever we do any modification in the source code, we should add tests if possible. So, now it warns if there are any changes in the source code and the tests folder is not modified, which means new tests are missing.
* **Update Changelog**: Added a new feature or fixed a bug — update the Changelog with the details. We made it mandatory to add a Changelog entry if the change is nontrivial. If the Changelog is not updated and pull request is not marked as trivial, then our CI fails the build. Now, we don’t have to keep track whether the Changelog was updated.
* **Encourage rebase not merge commits**: As the project grows it’s always recommended that we should avoid ‘merge’ commits so that the project has a clean history. We prefer using rebase instead of merging different branches. We can add a check for messages of this format: “Merge branch ‘master’” to avoid the merge commits.

![Image](https://cdn-media-1.freecodecamp.org/images/LHJv16-BauUBZd5Xt0QybFyE9aNkABawaXUu)

### Where to go next

For reference, you can check [ApplozicSwift’s Dangerfile](https://github.com/AppLozic/ApplozicSwift/blob/master/Dangerfile) or in some of the other popular open source projects like [React Native](https://github.com/facebook/react-native/blob/master/bots/dangerfile.js) or [CocoaPods](https://github.com/CocoaPods/CocoaPods/blob/master/Dangerfile). I discovered while writing this blog post that projects like React Native and React were also using danger. This shows us how this process of automating these checks has become part of the common pull requests workflow.

_Liked the story? Hit that clap button and follow me on [Medium](https://medium.com/@MukeshThawani). Thanks for reading! This article was originally published on [Kommunicate blog](https://www.kommunicate.io/blog/automate-code-reviews-on-github-using-a-chatbot/)._

