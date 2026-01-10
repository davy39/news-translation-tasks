---
title: How to Keep Your Package Dependencies Up to Date on Azure DevOps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-18T20:15:51.000Z'
originalURL: https://freecodecamp.org/news/keep-package-dependencies-up-to-date-on-azure-devops
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/photo-1587620962725-abab7fe55159-1.png
tags:
- name: Azure
  slug: azure
- name: dependency management
  slug: dependency-management
- name: Devops
  slug: devops
seo_title: null
seo_desc: 'By Apoorv Tyagi

  As a developer, how often have you seen a repository with packages that are out
  of date?

  New package updates generally include new features, performance improvements, and
  security fixes. But keeping track of all outdated dependencies ...'
---

By Apoorv Tyagi

As a developer, how often have you seen a repository with packages that are out of date?

New package updates generally include new features, performance improvements, and security fixes. But keeping track of all outdated dependencies in your project can be really boring and a time consuming task, especially if you have lots of them.

So to do this sort of housekeeping, I tried out [Dependabot](https://github.blog/2020-06-01-keep-all-your-packages-up-to-date-with-dependabot/).

## How Dependabot Works

Dependabot goes through the dependency files of your project. For instance, it searches your `package.json` or `pom.xml` files and inspects for any outdated or insecure dependencies. If it finds any, it opens individual pull requests to update each one of them.

This tool is natively integrated with GitHub. But recently, I had to solve this problem of updating dependencies for a project running in Azure DevOps. So I decided to find a workaround to integrate Dependabot with Azure Pipelines. In this blog post, I will share my solution.

If you go to [Azure DevOps Extension Marketplace](https://marketplace.visualstudio.com/azuredevops) and search for "Dependabot", you will find an [extension](https://marketplace.visualstudio.com/items?itemName=tingle-software.dependabot) by Tingle Software. Using this extension we can easily integrate Dependabot with our repos in Azure DevOps.

You can check if you have this extension in your "Organization Settings" in Azure DevOps. If not, make sure you have it installed before proceeding.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/1-2.png)
_Installed Extensions - Azure DevOps_

## How to Create the Azure Pipeline

Let's now create start with creating a new `YAML` file for your azure pipeline:

```
trigger: none

stages:
  - stage: CheckDependencies
    displayName: 'Check Dependencies'
    jobs:
      - job: Dependabot
        displayName: 'Run Dependabot'
        pool:
          vmImage: 'ubuntu-latest'
        steps:
          - task: dependabot@1
            displayName: 'Run Dependabot'
            inputs:
              packageManager: 'npm'
              targetBranch: 'develop'
              openPullRequestsLimit: 10
 ```

In the task parameters, I have specified three params:

1. **packageManager**: It specifies the type of packages to check for dependency upgrades. Examples: `nuget`, `maven`, `gradle`, `npm`, and so on.
2. **targetBranch**: It is an optional parameter that defines the branch to be targeted when creating pull requests. When not specified, Dependabot will pick the `default` branch of the repository. 
3. **openPullRequestsLimit**: This is again an optional parameter that specifies the maximum number of open pull requests to have at any one time. By default, it opens 5 pull requests at a time.

You can go through all the [Task Parameters](https://github.com/tinglesoftware/dependabot-azure-devops/blob/main/src/extension/README.md#task-parameters) that the extension supports to tweak your implementation. Now just simply configure this YAML file with a new azure pipeline and then you're ready to run it.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/3-2.png)
_Pipeline Configuration - Azure DevOps_

The next step is to give your repository's `Project Collection Build Service` access so that Dependabot can create the pull request to your project's repositories.

For that, go to your project settings. Here, you click on the repositories and search for the repo where you have integrated the pipeline.

After you have selected that, click on the security tab and search for **project collection build service**. You have to allow the following access to it:

* Contribute
* Contribute to pull request
* Create Branch
* Create Tag
* Force Push

![Image](https://www.freecodecamp.org/news/content/images/2022/01/2-1.png)
_Access to raise PR in Repo_

With this, you're completely ready to run the pipeline. Once you do it, you'll start receiving pull requests in your repository with the updated packages.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/5-3.png)
_PR raised by Dependabot_

## How to Schedule the Pipeline

Up to this point, you've had to manually trigger the pipeline to run. To make it run automatically, you can configure schedules for your pipelines. This will trigger your pipeline to start based on a schedule.

Use the following syntax and add it to the very top of your `YAML` file:

```
schedules:
- cron: string
  displayName: string
  branches:
    include: [ string ]
  always: boolean
  ```

The branche_s’_ `include` parameter specifies which branches the schedule applies to.

The `always` parameter specifies whether to "always" run the pipeline or only if there have been any source code changes since the last successful scheduled run. The default is false. 

For this case, you set its value to **true** as Dependabot updates are independent of any code changes.

The time zone for cron schedules is UTC and cron syntax is as follows:

```
mm HH DD MM DW
 \  \  \  \  \__ Days of week
  \  \  \  \____ Months
   \  \  \______ Days
    \  \________ Hours
     \__________ Minutes
```     

So if you want to run your pipeline every week on Sunday at 12pm UTC, you would need to write - `cron: "0 12 * * 0"` (update the cron to suit your needs).

This is how your final `YAML` should look like after adding a schedule:

```
schedules:
  - cron: "0 12 * * 0"
    displayName: Weekly Dependency Updates
    branches:
      include:
      - develop
    always: true
    
trigger: none

stages:
  - stage: CheckDependencies
    displayName: 'Check Dependencies'
    jobs:
      - job: Dependabot
        displayName: 'Run Dependabot'
        pool:
          vmImage: 'ubuntu-latest'
        steps:
          - task: dependabot@1
            displayName: 'Run Dependabot'
            inputs:
              packageManager: 'npm'
              targetBranch: 'develop'
              openPullRequestsLimit: 10
 ```

This pipeline does the following for you:

It runs on a weekly basis (Sunday 12pm UTC in this case) and looks for any outdated or insecure dependency. If it finds any, it opens pull requests to update each one of them individually.

Hopefully, this will help you to keep your project dependencies up to date in Azure DevOps!

## Wrapping Up

With this, we come to the end of the article. My DMs are always open if you want to discuss further on any tech topic or if you've got any questions, suggestions, or feedback in general:

* [Twitter](https://twitter.com/apoorv__tyagi)
* [LinkedIn](https://www.linkedin.com/in/apoorvtyagi/)
* [GitHub](https://github.com/apoorvtyagi)
* [Blog](https://apoorvtyagi.tech/)

Happy learning! 💻 😄

