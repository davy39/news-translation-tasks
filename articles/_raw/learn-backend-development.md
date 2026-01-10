---
title: The Best Way to Learn Backend Web Development
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-12T14:38:22.000Z'
originalURL: https://freecodecamp.org/news/learn-backend-development
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9bab740569d1a4ca2d39.jpg
tags:
- name: Backend Development
  slug: backend-development
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Mehul Mohan

  My previous article described how you can get into frontend development. It also
  discussed how the front end can be a place filled with landmines – step in the wrong
  place and you''ll be overwhelmed by the many frameworks of the JavaScr...'
---

By Mehul Mohan

My previous article described [how you can get into frontend development](https://www.freecodecamp.org/news/learn-frontend-web-development/). It also discussed how the front end can be a place filled with landmines – step in the wrong place and you'll be overwhelmed by the many frameworks of the JavaScript ecosystem. 

In this blog article, let's see how you can get into back end development. Along the way, I'll answer some of the most common questions people ask me about it.

## What is Backend Development?

Front end development involves what a user sees on the screen when they open a specific URL owned by you. Even in a completely static environment (with only HTML/CSS), when someone opens a website, some server on the planet needs to respond to you with those HTML and CSS files. 

That server is just a computer, just like the one you use yourself to browse the internet. But it has been tuned for performance, and doesn't have unnecessary components like a mouse or keyboard attached. And it sits with tons of other computers probably in a data warehouse. 

Programming those computers in some special way is called **back end development**.

You may think that backend development is called what it is because it runs behind the user's back. A visitor to your website never really "accesses" the back end completely. They just communicate with your server, either directly through ports for very limited access (like transferring HTML/CSS files) or not even that – buried deep under CDNs or firewalls (like Cloudflare).

Now that we have a raw understanding of what back end development means, let's get into some **real** questions.

## Is front end programming knowledge required for the back end?

**TLDR;** No.

Back end development, as mentioned above, involves the programming of a computer sitting probably on the other side of the planet responsible for responding to what your users say from their own computers. 

If you're a full-time backend developer, you do not really need to care about what goes on inside those HTML, CSS and JavaScript files you send to the user's browser. Instead, you've to focus more on the performance of the server, the server code, and throughput.

## What goes into back end development?

Well, going by the books, you may say that a person who codes an application that can respond to HTTP requests is a back end developer. 

But in reality, sometimes back end developers are able to do much more than just writing server scripts. They have the knowledge to set up reverse proxy servers (NGiNX/HAProxy), enable compression and other ways to speed up the site, and set up a production docker environment.

To qualify as a back end developer, I'd say the bare minimum skills you need are:

1. Good knowledge about a programming language in which you can write HTTP servers. Examples: C#, Java, Node, PHP, Python, etc. (there are many!)
2. Manage to host using cPanel (traditional) or using bash terminal (cloud hosting/traditional)
3. Working with Version Control Systems (VCS) like git for managing and deploying builds

Just like every game comes with minimum and recommended specifications, for back end developers, my recommend specifications would be (inclusive of the minimum skills):

1. NGiNX for static file assets and server management
2. Database Management skills (SQL/NoSQL)
3. Security of backend (Writing safe and robust code, running applications in docker containers with limited privileges, protection against DoS attacks)
4. Autoscaling/Load balancing

Alright, too much talking about what goes into back end development. But how do you become one?

## Start with minimum requirements

Like I said, for the back end, just like games, we have a set of minimum requirements and recommended requirements. The minimum requirements consists of 3 things:

### Learn a backend programming language

When people learn by themselves, they usually do not have a team or anyone who can do front end development. They're all on their own. So you'll often have to create webpages and servers all by yourself, at least in the beginning. 

Although there are a lot of choices for back end programming languages, and I cannot think of any popular system language which doesn't support HTTP servers out of the box. The advantage of choosing Node is that your front end JavaScript skills are transferrable to the back end.

Nonetheless, you can choose from a variety of languages like Java, C++, C#, Python, PHP, etc.

How do you pick one, you might ask. The answer is the same as it was in the front end development article: you have gotta try everything initially and see which one clicks the best with you. 

Node is easy as you might have already done JS programming for the front end. But if you're a Python or Java developer, you might find those easy to pick up. It depends on your profession and taste completely.

### Learn about managing hosting

Gone are the days when you'll have to manually purchase servers and set them up in your home, connect to your ISP, do all that stuff yourself. This is the era of cloud computing. Now, when hosting your website, you have mainly 2 options:

1. Going for managed hosting servers like HostGator or GoDaddy.
2. Going for cloud hosting providers like GCP, AWS, or DigitalOcean.

What is the difference between the two? In both cases, the servers are owned and operated by the respective companies. But the major difference is that managed hosting is more GUI friendly, has a rich set of tools for seeing the filesystem, monitoring usage, managing your official domain emails, uploading/downloading files from your server, and so on. It's basically a setup for people with less technical skills. 

For that reason, I do not recommend managed sites like HostGator or GoDaddy for seasoned developers. Still, it might be a good platform to make mistakes and learn on, primarily because you usually have prepaid plans for them. You'll also have a nice UI for managing things, which doesn't allow you to accidentally shoot up your bills.

But when you start picking up speed, I recommend that you switch to a cloud provider. This takes away all the nice tools from cPanel that you used to manage files and folders on servers. But at the same time, it will challenge you to level up your skills a lot. 

Today, a lot of cloud providers offer a decent free trial, too, so that you can actually try out their platform before going full in. I host my website for developers - codedamn - on DigitalOcean and find it to be at a sweet balance of site complexity and features. 

You can use [this link to signup](https://m.do.co/c/2c4c3ec5405a) on DigitalOcean and get **free $100 credits**. DigitalOcean instances are as cheap as $5 a month, so you have a runway of about 20 months on that instance, great deal, huh?

Anyway, you can choose any cloud provider. Then it's important to learn to manage the server using just the command line by ssh'ing into it.

### Learn about Version Control Systems

There are other solutions apart from Git for VCS. But Git is the most used and simplest to understand. 

As an individual, you might not appreciate it right away. But you'll understand why it is so important the moment you start working either in a team on multiple features simultaneously in your project. 

Git allows you to manage your workflow using commits and branches. Commits are like **checkpoints** in your codebase - the ones you can always revert to if you screw up. 

Branches are like **alternate realities** of your project, where something completely different could happen. These alternate realities can be created from any point in time and can be merged back again at any time. 

If those realities can be merged together with compatibility, then it's fine. But if there's a conflict (like if you're alive in one reality and dead in other), then you have to manually make a choice. Other changes can be merged automatically.

Git is super interesting, and once you get hang of it, you'll want to use it in every project. You get to keep a history of your work in an efficient manner (it compresses and stores only the difference between commits). 

It also allows you to create online git repositories on sites like GitHub, which acts as a central source of truth for your website. Sites like GitHub can be configured with special webhooks that can actually update your website whenever you add a new checkpoint (a new commit) without you ever needing to manually go to the server and update it yourself.

## Go for recommended skills

I'm a big believer in learning by doing. And the best way to do something comes out of necessity or interest. Once you consider yourself good enough with the minimum requirements, it's time to acquire the recommended skills. This includes all the tools like Docker and NGiNX mentioned above. 

**DevOps** is also something which fits in super nicely with back end developers. You could try and explore **TravisCI** or **CircleCI** for automated build deployments. Continuous Integration and Deployment (CI/CD) is a topic that could take another whole blog post, so I'll not get into that. In fact, once it is set up correctly, it'll save you a ridiculous amount of developer time!

Then comes databases, which I placed in recommended skills. But you're gonna need databases for pretty much any application which involves some sort of data persistence generated by the user. 

Databases are usually easy to begin working with, but harder to maintain and tweak properly. The best way to start working on a back end tech stack is to have everything together on a single server - the code of your application, the reverse proxy servers, the database, etc. Then as you become more proficient in each thing, you can decouple it from the existing business logic. 

By doing this, you're enabling an architecture that can be highly scaled. A database-operation intensive application could have an optimized solution for databases. And a heavy traffic bound site should have a good CDN mechanism to offload static assets, and so on.

## Conclusion

There's so much to learn, but it's all achievable if you don't give up. Let me know what you think about this post through my [**twitter**](https://twitter.com/mehulmpt) and [**Instagram**](https://instagram.com/mehulmpt) handles. It'll mean a lot to me if we connect over there! 

Also, if you're interested, checkout [**codedamn**](https://codedamn.com) - a developer-focused platform for learning technologies like backend development! I even posted a [YT video on spinning up your own simple website server in 2 minutes](https://www.youtube.com/watch?v=IOTL7RqUZEU)! Check that out and let me know what you think!

Peace!

