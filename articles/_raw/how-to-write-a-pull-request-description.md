---
title: How to Write a Good Pull Request Description – And Why It's Important
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-31T22:01:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-a-pull-request-description
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/wp3082255.jpg
tags:
- name: code review
  slug: code-review
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: Testing
  slug: testing
- name: version control
  slug: version-control
seo_title: null
seo_desc: "By Sajal Sharma\nWriting a good Pull Request description is one of the\
  \ most tedious jobs a developer has to do. And it can feel counter-productive at\
  \ times. \nBut developing this skill goes a long way and really helps your stakeholders\
  \ and your organiz..."
---

By Sajal Sharma

Writing a good Pull Request description is one of the most tedious jobs a developer has to do. And it can feel counter-productive at times. 

But developing this skill goes a long way and really helps your stakeholders and your organization in the long run. 

So it's always better to put in those 10 extra minutes today rather than having to break your head 6 months down the road trying to explain why you did what you did.

The following article explains the different parts of a Pull Request Description, and why you should include them.

## What is a PR description?

A pull request description describes what constitutes the Pull Request and what changes you have made to the code.

It explains what you've done, including any code changes, configuration changes, migrations included, new APIs introduced, changes made to old APIs, any new workers/crons introduced in the system, copy changes, and so on. You get the gist.

You should include this section because it gives a glimpse to different stakeholders into what the PR is doing. 

For a non-technical person, the description should explain what the impact will be on the system when these code changes are deployed to production. 

It will also help the reviewer in understanding what they will be reviewing (kind of a prologue/trailer). 

And finally it helps QA/SDET in understanding the scope of the PR as well. 

So the "what" of the PR should give a glimpse into what constitutes the changes in the PR.

## The "Why" section

This section explains why the above changes explained were done.

Sometimes a developer feels that it's okay to write "Business/Product requirement" in the description. That's fine, but doing so defeats the purpose of this section. 

If there is a better explanation as to why the changes were suggested, it's always good to attach a document reference link for that information. A good "Why" section should explain the reasoning behind any changes.

You should include this section because it gives an explanation of why you suggested your changes. It might not sound reasonable to include this section in the shorter term, but it plays a vital role as the product matures and spans years. 

Developers/Product folks comes and goes, but the code remains. And when a new developer works on a piece of code and finds a discrepancy there, they can dig deeper and get to the pull request from 2 years ago which made those changes. 

A good "why" gives them the explanation and assumptions made at that time.

**GoJek's CTO** once explained that they don't challenge their legacy code and don't question why there seems to be some absurd looking feature in the product. 

They just go back and check the documentation. 

The assumptions and circumstances might have changed, and hence the code evolves. What seems to be quite absurd today might have been relevant 2 years ago. So it's better to explain today why you are making a particular change.

## Testing Scope

This section should comprise a list of scenarios you need to keep an eye on when testing this particular PR. (This will include flows, APIs, crons, workers, and so on.)

A good testing scope gives visibility to the QA/SDET team about the scenarios and flows that they need to test.

It can also help you while you're writing this section. I have come across issues myself, which prompted me to go back to the development phase and test them again. 

A thoroughly written Testing Scope helps developers test the PR more efficiently, and gives a thorough picture of the PR to the person testing it.

## Relevant Document(s)

This section includes any relevant document that needs to be attached with the PR description.

That might include product requirement documents, architectural diagrams, database system diagrams, design patterns used, class diagrams, external library documentation, and so on.

This section helps explain any assumptions and references you made while working on this feature request. And it plays a major role in the long run. 

When someone comes back and sees why such a change was suggested, the relevant documents section will take them to the specific documentation so they can understand the issue clearly. Or it can take them to the technical implementation details of the scenario at the time of development.

## Dependent PR(s) (if any)

There are times when a particular feature spans across multiple GitHub repositories and it's important to release them in a certain order. 

For example, you might need to deploy one repo prior to another, or you might need to deploy them side by side.

Whatever the case may be, this section explains any dependent code that this PR relies upon.

You should include this section because it really helps the deployer understand the order of deployment. If another repo's code needs to go first, then the deployer will contact the person responsible for deployment of the other repo to make sure that their deployment happens first. Overall it helps smooth out the deployment process.

## Configuration Changes (if any)

This section should include all the config changes that need to be added to the secrets before the PR is deployed into production.

There will be times when the deployer will merge 10-20 PRs at a time and it becomes hard for them to keep track of all the config changes. 

Because of this, it's always better to include them in the config changes section. (Don't put the secret keys there, just include the key names and how to get the secrets.)

## Tags/Labels

These are very important in a pull request description and convey a lot of meaning when the team grows. 

Following are some tags that I use, but you can add different tags according to your needs.

* **Dev Completed -** When the development is completed from the dev's side.
* **Self Reviewed -** When the developer(s) of the Pull Request has reviewed the Pull Request from their side, and can now give it to their peers for a Peer Review.
* **Self Tested -** When the developer(s) of the Pull Request has tested the changes themself according to the description they have given in the Testing Scope section.
* **Config Changes -** This tag indicates that there are some configuration changes that need to be done before deploying the PR to production. (This includes secret keys that needs to be put into the system.)
* **Contains Migration(s) -** This indicates that the PR contains a Migration. If it is a long running migration, it should be specified beforehand.
* **Release Ready -** This indicates to the Deployer that the PR is ready for deployment and will be picked up by the deployer in the next deployment cycle.
* **Peer Reviewed -** When the Peer has reviewed the PR and the suggested changes are made by the developer(s). This is put up by the Peer who has reviewed the PR.
* **QA Tested -** This indicates that the QA/SDET has tested the PR and it is good to be deployed to production.

## Conclusion

In this article, we went through the different parts of a PR description. Most of the PRs you make will not need all these sections and tags, but you should try to include as many of them as you can. 

Writing this description might not seem productive at the time when you create a PR, but it can definitely prove helpful in the future.

A final note: The above are my views and might differ from your perspective. But I've developed this strategy over the years, and it contains the input and experience of a lot of people I have worked with in the Industry. So you can feel good knowing that it's been battle tested to a high degree.


