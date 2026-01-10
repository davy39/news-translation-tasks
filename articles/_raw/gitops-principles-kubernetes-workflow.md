---
title: What is GitOps? Principles, Best Practices, and Kubernetes Workflow
subtitle: ''
author: ania kubow
co_authors: []
series: null
date: '2021-11-23T22:50:29.000Z'
originalURL: https://freecodecamp.org/news/gitops-principles-kubernetes-workflow
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/gitops.jpeg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Cloud Services
  slug: cloud-services
- name: Kubernetes
  slug: kubernetes
seo_title: null
seo_desc: "In this talk, CTO Cornelia Davis will teach you what GitOps is and what\
  \ its four main principles are. \nWhat is GitOps?\nThe first thing you need to know\
  \ is that GitOps is a set of modern best practises for deploying and managing cloud\
  \ native infrastru..."
---

In this talk, CTO Cornelia Davis will teach you what GitOps is and what its four main principles are. 

## What is GitOps?

The first thing you need to know is that GitOps is a set of modern best practises for deploying and managing cloud native infrastructure and applications. 

And it can an be a hard thing to get your head around if you have never worked with cluster management or application delivery before. But thankfully Cornelia does a great job explaining it in this 30 minute presentation.

Give it a watch, and then you can find the recap below.

%[https://www.youtube.com/watch?v=wdoLEA7U8_M]

So now that we have covered the basics of what GitOps are, here is a recap of its 4 main principles. Hopefully you can use them to start managing your own cluster with GitOps workflows.

## Principles of GitOps

### Describe Declaratively

By 'Declarative', all we mean is that we are writing our configuration as a set of facts directly in our source code on Git. This is now our single 'source of truth'. 

For example I can declare my environments, such as a 'test environment', or a 'staging environment' or 'production' and so on, along with the application version that resides in that environment.

### Make Sure State is Versioned

With our declarations now stored in a version controlled system and acting as our 'source of truth', we now have a single place from where everything is derived. We can spin up previous versions of the app easily, or perform rollbacks if we need.

### Automate Change Approvals

We also need to allow any changes to our declared states to be automatically applied to our system. This is worth mentioning, because as we are now working in segregated environments, we no longer need cluster credentials to make changes in our system.

### Alert on Differences

So now that we have the state of our system declared and versioned, we can use agents to check if everything is working as it should. This is considered a 'Feedback and Control Loop'. If something 'looks' different and not right, we will get alerted on this.

For a more in-depth look into these 4 principles, you can watch the Talk by Cornelia Davis above.

This article was written by Ania Kubow in support of the conference talk made by Cornelia Davis.

<figure class="kg-card kg-bookmark-card"><a class="kg-bookmark-container" href="https://www.youtube.com/channel/UC5DNytAJ6_FISueUfzZCVsw"><div class="kg-bookmark-content"><div class="kg-bookmark-title">Code with Ania Kubów</div><div class="kg-bookmark-description">Hello everyone. This channel is run by Ania Kubow. In this channel, I will be teaching you JavaScript,React, HTML, CSS, React-native, Node.js and so much more! A little bit about me:My background is in the financial markets, where I worked as a derivates broker our of University. After starting m…</div><div class="kg-bookmark-metadata"><img class="kg-bookmark-icon" src="https://www.youtube.com/s/desktop/6b151e52/img/favicon_144.png"><span class="kg-bookmark-publisher">YouTube</span></div></div><div class="kg-bookmark-thumbnail"><img src="https://yt3.ggpht.com/ytc/AAUvwnjSRt8sIbeM7P--pHoUDh67sDhaNTCMF_XiNOCvUw=s900-c-k-c0x00ffffff-no-rj"></div></a></figure>


