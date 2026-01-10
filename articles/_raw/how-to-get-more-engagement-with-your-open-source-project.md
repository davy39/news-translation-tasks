---
title: How We Got 4.5K+ GitHub Stars on Our Open Source Project in 6 Months
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-26T14:54:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-more-engagement-with-your-open-source-project
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/t3.png
tags:
- name: Collaboration
  slug: collaboration
- name: community
  slug: community
- name: GitHub
  slug: github
- name: open source
  slug: open-source
seo_title: null
seo_desc: "By navaneeth pk\nWe launched our open source project in June 2021, and\
  \ since then we've gotten more than 4500 stars for our repository. \nHere are the\
  \ strategies that worked for us. This is not an article about how to just get more\
  \ stars for your repos..."
---

By navaneeth pk

We launched [our open source project](https://github.com/ToolJet/ToolJet) in June 2021, and since then we've gotten **more than 4500 stars** for our repository. 

Here are the strategies that worked for us. This is not an article about how to just get more stars for your repository. The article instead explains how to present your project well so that it is helpful for the open-source community. 

Some of these points have also helped us get contributions from more developers. We have contributions from more than 100 developers now. 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-79.png)

Fun fact: the graph above was generated using an app built with our tool. You can [try it out here](https://apps.tooljet.com/github-star-history) to generate a star history chart for your project.

Alright, let's dive into the strategies we used to raise awareness for our project.

## Write a Good Readme

The README is the first thing that a visitor to your repository sees. It should be able to convey what your project does, how to install the project, how to deploy the project (if applicable), how to contribute, and how it works. 

You can also use badges that are helpful for developers. We used [https://shields.io/](https://shields.io/) for adding badges to our Readme.   
  
Here is what our Readme looks like:

![Image](https://blog.tooljet.com/content/images/2022/01/image-1.png)

  
And here are some examples of projects with great README files:

1. [https://github.com/nestjs/nest](https://github.com/nestjs/nest) 
2. [https://github.com/typesense/typesense](https://github.com/typesense/typesense)
3. [https://github.com/airbytehq/airbyte](https://github.com/airbytehq/airbyte)
4. [https://github.com/strapi/strapi](https://github.com/strapi/strapi)

## Focus on Documentation

We get more traffic to our [documentation portal](https://docs.tooljet.com/) than our main website. A well-documented project is always loved by the community. 

Open-source projects like [Docusaurus](https://github.com/facebook/docusaurus/) make it super easy to build documentation portals that look great just out of the box. Adding links to the repository from the documentation can drive more visitors to your repository.

### What to include in documentation

#### How to install/deploy the project

If the project has a compiled software as the final product, make sure to add installation instructions. 

If the project is the codebase for a library such as an npm package or a Ruby gem, include details on how to import and use the library. 

If the project needs to be or can be deployed on platforms like Kubernetes, Docker, Heroku, and others, include separate guides for each of the options. 

#### Contributing guide

Apart from the contributing guide doc in the codebase, add one to the documentation, too. It should include guides for setting up a local environment on different platforms like Docker, Mac OS, Ubuntu, Windows, and so on. 

#### Tutorials and code examples

If this is applicable, it can be really helpful. How to guides on using using the project will show other devs how they can actually get started. It can be code examples if the project is a library. 

#### Architecture reference

It will be helpful for the contributors if the documentation has details on different components of the project. 

For example, if the project has server and client components, include a diagram on how everything works together. Here is [an example](https://docs.tooljet.com/docs/intro) from ToolJet's documentation. 

Here are some projects with great documentation:

1. [https://docs.nestjs.com/](https://docs.nestjs.com/)
2. [https://docs.n8n.io/](https://docs.n8n.io/)
3. [https://guides.rubyonrails.org/](https://guides.rubyonrails.org/)
4. [https://plotly.com/python/](https://plotly.com/python/)
5. [https://docs.mapbox.com/](https://docs.mapbox.com/)

## Drive visitors from your website to GitHub 

![Image](https://blog.tooljet.com/content/images/2022/01/image-6.png)

A lot of visitors checked out our repository after visiting our website first. Add banners, badges, and other incentives to your website so that visitors will check out your repository. 

Add a CTA to your website and blog so that the visitors will check out your repository. Write about topics relevant to your audience. For example, if your project is used for logging errors, it might be a good idea to write about how to track errors in an application. 

Publishing articles on platforms like freeCodeCamp, dev.to, Hashnode, and Hackernoon can also help you get more visibility for your blog posts. Some of these platforms allows cross-posting while some others are more suited to exclusive content. 

## Be active in developer communities

There are many discord/slack communities, forums, Reddit communities, and so on where developers usually hang out. Be active in these communities without making it look like self-promotion (which can get you banned for obvious reasons).

You can add value to the communities by participating in relevant discussions. For example, if you are building a charting library and if someone is asking a question about plotting charts using React, you can pitch in to help. 

Remember, play nice. Do not just try to link to your project if it does not add any value to the discussion. The more you build up relationships by helping people, the more you'll be able to share info about your project in a natural, helpful way.

## Trending repositories on GitHub

![Image](https://blog.tooljet.com/content/images/2022/01/image-4.png)

If you make it to the [list of trending GitHub repositories](https://github.com/trending?since=daily), it can get your repository a lot more visibility. 

When we made it to the trending list, we got more visitors to our repository and website. 

There are trending lists for specific languages too. Many Twitter bots and other tools notify developers whenever there is a new repository that has made it to the trending list. 

### How to get on GitHub's trending list

The general principle should be that repositories with the most activity ( stars, visitors, issues, contributions, and so on ) will be added to the trending list.

GitHub hasn't publicly mentioned the criteria for selecting trending repositories, so we can only assume how it works. 

## Ask for feedback from relevant communities

![Image](https://blog.tooljet.com/content/images/2022/01/image-5.png)

Communities such as [ProductHunt](https://www.producthunt.com/posts/tooljet), [Hackernews](https://news.ycombinator.com/item?id=27421408), Reddit communities, and others may find your project useful. This can bring in more visitors and stargazers to your repository. 

Target only the relevant communities. If you think the majority of the members won't find your project interesting, it is not a relevant community. Spamming can cause more harm than good. Also, it's just not nice.

## Grow a community around your project

Start a community on Discord or Slack where your users and contributors can hang out. 

Communities can be helpful when the members are stuck with something and if they want to propose something new. If there is an active community, your future posts and announcements might get more reach. 

We created the community on Slack since most of the developers have a Slack account. Don't use lesser-known platforms for building your community as it will take an additional step for the person to join the community.

## Add a public roadmap

A public roadmap helps your users and contributors understand where your project is headed. It gives an overview of the short-term vision of the project.

There are many tools available for creating public roadmaps, but in most cases GitHub projects will be more than enough for creating a simple yet effective public roadmap. 

Public roadmaps should include all major features and changes that are expected to be released in the next few months. Adding minor features and bugs as part of product roadmap can lead to a lot of noise, so avoid it as much as possible. 

If you use GitHub projects, link to the relevant issues or discussions so that the community can comment their suggestions. 

We have created one using GitHub projects that [you can check out here](https://github.com/ToolJet/ToolJet/projects/2).

## Be Active on Twitter 

Being active on posts related to your projects can create awareness, increase the number of followers on Twitter, and drive more visitors to your repository. 

Participate in discussions that are related to your project. For example, if your project is a documentation framework, you can add a lot of value to threads that compare different documentation frameworks. 

Make sure to link your repository on the project's Twitter profile. Also, add a tweet button to your GitHub repository. 

Again, make sure you add value to the discussions. No one likes a spammer.

## Respond to feedback 

Open-source communities are usually very helpful and give a lot of feedback. Respond to all this feedback, as the person has taken their valuable time to help you improve your project. 

Positive feedback helps you stay motivated, while negative feedback helps you rethink what you've done so far. 

Do not try to avoid or ignore negative feedback. Be open-minded and consider carefully what the person has shared. Work on it if it aligns with your vision, otherwise politely explain. 

## Add relevant labels for contributors

Adding labels such as "good first issue" and "up for grabs" can attract more contributors to your repository. 

There are many platforms such as [https://goodfirstissue.dev/](https://goodfirstissue.dev/) that scan for issues tagged with relevant labels to help contributors discover new repositories and issues to contribute to. 

Make sure you respond to contributors quickly. Contributors can be experienced developers as well as developers in the early stages of their careers or students. Try to help the first time contributors so they can onboard easily. 

## Wrapping Up

You landed on this article possibly because you have an interesting open-source project. I'd love to see your project. I'm available at navaneeth@tooljet.com and on [Twitter](https://twitter.com/navaneeth_pk).

Hope this article was helpful for you. We would really appreciate it if you can take a moment to [check out our project, ToolJet](https://github.com/ToolJet/ToolJet), and give us any feedback you might have.

