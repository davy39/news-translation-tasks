---
title: How to setup CI on GitLab using Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-12T19:11:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-ci-on-gitlab-using-docker-66e1e04dcdc2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*b7KBZqZQ_VZ3kFu6lQQaYQ.png
tags:
- name: coding
  slug: coding
- name: Continuous Integration
  slug: continuous-integration
- name: Docker
  slug: docker
- name: GitLab
  slug: gitlab
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ying Kit Yuen

  An example using Docker to test and build your pipeline


  In the past you may have tried different tools to manage the deployment of your
  applications effectively. In this tutorial, I’ll be showing you a quick and easy
  way to set up c...'
---

By Ying Kit Yuen

An example using Docker to test and build your pipeline

![Image](https://cdn-media-1.freecodecamp.org/images/1*b7KBZqZQ_VZ3kFu6lQQaYQ.png)

In the past you may have tried different tools to manage the deployment of your applications effectively. In this tutorial, I’ll be showing you a quick and easy way to set up continuous integration for your environment using GitLab and Docker. So lets get started.

Here is what we’ll be setting up:

* Version control
* Issue Tracker
* Documentation
* Continuous Integration
* Continuous Delivery
* Repository (artifacts/docker images)

Tools like [Jenkins](https://jenkins.io/) are good for continuous integration and delivery. [Mantis](https://www.mantisbt.org/) helps with issue tracking. But to improve the efficiency and quality of our project, we need to bring all these tools together. For example, we may want a git commit hook up with existing issues, or trigger an automated test after pushing commits to the master branch.

Usually, most tools already provide out of the box integration with other common services but it is still difficult to configure them at times. Moreover, the workflow would be broken if any one of the services in the chain go down. So it would be great if there were a single platform which could fulfil all these requires and that is why we’ve chosen [GitLab](https://gitlab.com).

### GitLab CI

[GitLab.com](https://gitlab.com) is a SAAS based service where you can host your Git repository, track issues and write the wiki in markdown. [GitLab CI](https://about.gitlab.com/features/gitlab-ci-cd/) also allows you to setup continuous integration utilizing any Docker image available on [Docker Hub](https://hub.docker.com/). Let’s take a look at the following example.

#### The GitLab CI YML

GitLab CI uses a YAML file `.gitlab-ci.yml` to define the project configuration, which includes a definition of all the stages that need to be run after a CI/CD pipeline is triggered in response to a git push/merge. In this example, we have a simple Node.js project and we would like to make sure the code is good by linting and running a unit test. To play along, fork this [repository](https://gitlab.com/ykyuen/gitlab-ci-demo) and check it out.

In the above YAML configuration file we defined 3 stages. Each stage is just a gulp task defined in `gulpfile.js`. Anyone could run the task locally as long as the have Node.js installed. But in [GitLab CI](https://about.gitlab.com/features/gitlab-ci-cd/), we only need to mention which Docker image is needed. In our case, that is node:6.11.2. Furthermore, this image attribute could be defined within the stage definition so that you could use different tool for each stage.

#### The stage definition

Let’s take a deeper look in the stage definition.

The attributes of `before_script` and `script` can have multiple values (array in .yml). And if the script execution fails, the stage will be classified as failed.

#### Trigger the pipeline

Just make some changes on the master branch and you can find the pipeline running on the `CI / CD -> Pipel`ine page.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Rtj97p-NEzbJjOe2Lh3-8A.jpeg)
_The pipeline history_

#### View the stage in detail

Click on a specific pipeline and you can read the console output of each stage. This is useful when the stage/job fails.

![Image](https://cdn-media-1.freecodecamp.org/images/1*t_0-lH0Hi05sEBeK8XzDIg.jpeg)
_The stage output_

### The benefits of using GitLab CI with Docker

Different projects may require different dependencies such as Node.js, Ant, Maven. In the past when using a tool such as [Jenkins](https://jenkins.io/), I’d have to make sure that all of these are installed on the server. By using [Docker](https://www.docker.com/), the developer can reference dependencies available on [Docker Hub](https://hub.docker.com/) without asking the server admin to setup such dependencies on the server each time. Actually Jenkins also has a pipeline plugin and it could work with Docker to serve exactly the same purpose. But extra effort on integrating Jenkins with version control is needed and as I mentioned before.

Although i prefer using [GitLab CI](https://about.gitlab.com/features/gitlab-ci-cd/), it doesn’t mean it could completely replace [Jenkins](https://jenkins.io/). [Jenkins](https://jenkins.io/) offers a configurable user interface which is convenient for non-developers such as QA to execute certain tasks like deployments and integration tests.

### Pick a suitable tool - It doesn’t have to be perfect

The key is not about choosing the perfect tool. Instead it is more about the people who use it. So before searching for a new tool, try to identify the problem which you would like to solve first.

— Originally posted on [Boatswain Blog](https://blog.boatswain.io/post/a-simple-gitlab-ci-example/).

