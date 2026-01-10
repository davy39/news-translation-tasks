---
title: How to Develop Kubernetes Applications with Joy
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-20T08:55:00.000Z'
originalURL: https://freecodecamp.org/news/developing-kubernetes-applications-with-joy
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/ships-wheel.jpg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Continuous Integration
  slug: continuous-integration
- name: 'Integrated Development Environment  '
  slug: integrated-development-environment
- name: Kubernetes
  slug: kubernetes
- name: Visual Studio Code
  slug: vscode
seo_title: null
seo_desc: "By Sven Efftinge\nLet’s face it: Developing distributed applications is\
  \ painful.\nMicroservice architectures might be great for decoupling and scalability\
  \ but they are intimidatingly complex when it comes to development. \nLocal Kubernetes\
  \ clusters (Min..."
---

By Sven Efftinge

**Let’s face it: Developing distributed applications is painful.**

Microservice architectures might be great for decoupling and scalability but they are intimidatingly complex when it comes to development. 

Local Kubernetes clusters (Minikube), long build times (Docker), and awkward or even nonexistent solutions to debugging is how we started. Two years in, we have automated everything: nothing runs on my local machine anymore and I can start coding and debugging individual components on any branch in just 15 seconds. ?

I now enjoy working on our project so much and believe this is one of the most streamlined setups out there. In the following I want to share that experience.

## Starting with a Preview Environment

To get started on a bugfix or feature, I just need to create a new branch on GitHub. This will immediately trigger our CI servers (we use Jenkins) which then deploys a preview application to a GKE cluster. The application lives in a namespace corresponding to the branch name and, using the preview URL, I can access and use the application.

Since I only branched off and didn't push any changes, the build artifacts are cached and the deployment takes only a few seconds. But even once I push changes, the build will run quickly as it only rebuilds what is really necessary.

## Starting to Code

Next up I spin up a development environment to work on my task. We use [Gitpod](https://www.gitpod.io), which similarly to a CI server prebuilds dev environments for any branch. A click on a button from any of our project’s GitHub pages starts a fresh dev environment for exactly that branch and opens it in my browser.

The dev environment is up after ~15secs and awaits me with a fresh clone of our repo and the correct branch checked out. Furthermore, the project is fully built and even all dependencies are downloaded already. The terminal welcomes me with the following message:

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot-2019-11-19-at-13.19.06.png)

The IDE is preconfigured with all the VS Code extensions we need, in our case Kubernetes, Docker, MySQL, Go and TypeScript. It is also already connected to the Kubernetes cluster running the preview environment as well as the corresponding database. So I can, for example, type '_kubectl get all'_ in my terminal and see all the deployed kube objects.

The connection is based on a secret token that every developer has to put into their user account once and which is injected when starting a dev environment.

Although these ephemeral dev environments run in my browser, they provide all the state-of-the-art tools, allowing me to code, compile, run and debug code as well as interact with the database and the cluster.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot-2019-11-19-at-13.23.33-1.png)

Of course, I can now push any of my code changes to GitHub and wait for the CI to update my preview environment accordingly. Since the build is caching heavily, small changes are deployed in a minute or so. Most of the time, however, a minute is way too long. We need an instant, hot-reloading experience that allows to debug any service in the context of the full application. Enter _Telepresence_.

## Debugging with Telepresence

I want to be able to debug any individual service in the context of the full application. Instead of waiting for redeploys, our components have proper launch configs to debug them using [Telepresence](https://telepresence.io).

![Image](https://www.freecodecamp.org/news/content/images/2019/11/bird-on-bricks.svg)

Telepresence replaces a Kubernetes deployment with a proxy that forwards all communication to a locally running process. So in short I can start a local debug session and have it working in the context of my preview environment.

This works fantastically and is the best way I’ve seen so far for debugging Kubernetes services. It allows me to reuse all the existing debugging tools available.

## Pushing and Review

Once I’m happy with my changes, I push to my branch and create a Pull Request. I can do that from within Gitpod which is quite convenient.

Jenkins will now update the preview environment and Gitpod prebuilds a new dev environment. So when a colleague wants to start reviewing my changes, they can try them out immediately and quickly launch a dev environment for deeper inspection. From within Gitpod they can add comments to the code and even approve (or reject) the PR.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/Screenshot-2019-11-19-at-11.54.50.png)
_Our Toolchain_

## Conclusion

Achieving fast turnarounds and automated setups for distributed applications is hard but an absolute necessity for getting into a productive flow. Any friction in this will have a bad effect on the productivity of your team.

A fast build with preview environments and the slick Telepresence-based debugging experience have been an enjoyable productivity boost for us. If Gitpod didn’t exist we’d have to build it ;).

Do you have questions? [Reach out](https://www.typefox.io/contact/), we are happy to help.

---

> Note: Some of the features in Telepresence require system calls that are currently only allowed in Gitpod self-hosted.


