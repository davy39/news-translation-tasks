---
title: How to quickly set up a build process for a static site
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-11T17:23:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-quickly-set-up-a-build-process-for-a-static-site-1a6e7923e105
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lWOnHgWDaYgoBFh9dErY-A@2x.png
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ondřej Polesný

  You have a static site all implemented and ready for the world to see, but where
  should you host it? How do you select the right platform and plan for a set of static
  files? How can you ensure that the website will automatically reg...'
---

By Ondřej Polesný

You have a static site all implemented and ready for the world to see, but where should you host it? How do you select the right platform and plan for a set of static files? How can you ensure that the website will automatically regenerate whenever you change its content?

In this article, I will show you how to generate a static site, set up an automatic build process that is triggered by content changes and deploy the site to a public facing server.

### Introduction

In previous articles, I explained how to [build a dynamic JavaScript website with content from a headless CMS](http://bit.ly/2CyDnhX) [Kentico Cloud](http://bit.ly/2QzUALM). Then I showed you [how to convert it into a static site](http://bit.ly/2PN46Jy) to help performance, security, and SEO. So now it’s time to get that site generated and push it online for the whole world to see.

### Generating a static site

Every static site generator lets you build the site locally without generating all files after every single file change. If you followed my articles, you have a site on Vue.js that is converted to use Nuxt.js as a framework but still requires a development server to handle website requests. To generate the static files, run the following command:

```
npx nuxt generate
```

Open the `dist` folder in the root of your project to find the generated files and check out `index.html` to make sure your website generates correctly. I have a habit of also checking the child pages where I know there is some content from a headless CMS, like a Blog page. If you see the content in HTML form, you are a winner!

### Where should I host a static site?

That is probably the next question you ask after generating all the files. If you are rebuilding a site and your old website is still online, you are probably thinking of using the same provider for the static site. That’s perfectly fine. However, if your old site was built on top of a traditional CMS or another programming language, you may need to think twice.

Your current hosting space is scaled to fit the requirements of another system or designed to support a specific setup, like PHP and MySQL or .NET and PostgreSQL. So if that is the case, you probably used the amount of traffic, sessions, and other values to calculate which amount of computing power you will need (or like me in the past, just hoped it would be OK).

With static sites comes relief: no more complicated formulas, approximations, and professional guesswork. Hosting a bunch of static files is something every web server can do easily. The most important aspect is that the server no longer needs to go through the sophisticated pipeline of request handling for each hit. It just serves static files instead. And that’s easy and fast.

Hosting static sites is therefore much cheaper. There are dozens of services that allow you to host your websites for free or at least have free starter plans. They include:

* [GitHub pages](http://bit.ly/2AAQrR5)
* [Netlify](http://bit.ly/2TEmPJK)
* [Heroku](http://bit.ly/2VHD0If)
* and other global and local providers. You can, of course, use global website hosting services like Azure or AWS too.

I decided to choose GitHub pages as all of my repositories are already hosted on GitHub. It is also completely free and supports custom 2nd level domains.

### How do I build and deploy a static site?

But it’s not just about hosting. Having the pages online is essential, but it is just as important to think about the whole process of deployment. That is — how are the static pages going to be generated and transported to the server. For the first build, you can generate pages in your local environment using `npx nuxt generate` and copy-paste the static files to your hosting space via FTP. But are you going to repeat that process every time there is a content change?

![Image](https://cdn-media-1.freecodecamp.org/images/TOkelGF8EBjynGKQy8H62YPjMh98lIWIuNgS)

The process of deploying a static site has three parts:

1. Trigger
2. Build
3. Deployment

### Trigger

A new build needs to happen when either a content or implementation change occurs. That means whenever a content editor publishes new content in a [headless CMS](http://bit.ly/2QzUALM), or you change the source code, the website needs to rebuild. But how do we achieve that?

![Image](https://cdn-media-1.freecodecamp.org/images/0UAVMwIbWrAJT-SMlTDL1nDbM7lzGLl3WWA4)

#### Content change trigger

Every mature headless CMS features [webhooks](http://bit.ly/2QzOdeS). They represent service-to-service notification about a certain type of action. So when an editor publishes a content item, the headless CMS initiates a webhook notification that is sent to a defined URL. In this case to a build server that will act upon the notification and rebuild the site.

But how does the build server know what to do? Well, it has no idea what kind of content storage you use and would probably not understand the generic webhook notification. For that reason I added a simple Azure function in the middle that does two things — first, it checks that the notification’s origin is Kentico Cloud:

```
...
```

```
if (!isValidSignature(req, process.env['KC_WEBHOOK_SECRET'])) { context.log('Signature was invalid'); return;}
```

```
...
```

```
const isValidSignature = (req, secret) => { const givenSignature = req.headers['x-kc-signature']; const computedSignature = crypto.createHmac('sha256', secret) .update(req.rawBody) .digest();
```

```
 return crypto.timingSafeEqual(Buffer.from(givenSignature, 'base64'), computedSignature);}
```

_(see the complete [file on GitHub](https://github.com/Kentico/kentico.github.io/blob/source/src/azureFunctions/fireSiteRegeneration/index.js))_

and then triggers the build using the API of the build server:

```
request.post({ url: "https://api.travis-ci.org/repo/Kentico%2Fkentico.github.io/requests", headers: { "Content-Type": "application/json", "Accept": "application/json", "Travis-API-Version": "3", "Authorization": `token ${process.env['TRAVIS_TOKEN']}` },
```

```
...
```

_(see the complete [file on GitHub](https://github.com/Kentico/kentico.github.io/blob/source/src/azureFunctions/fireSiteRegeneration/index.js))_

I know I know, Azure asks you for your credit card before you can create functions. But you can use [Webtask.io](http://bit.ly/2yCjNgl), which is completely free. I explained how to create a simple function there in [one of my previous articles](http://bit.ly/2P0gidP).

![Image](https://cdn-media-1.freecodecamp.org/images/bLPPwLQ6jTgOOAw8WhYfcUEvTxLn5rlloQUb)

### Code change trigger

With code, the process gets even easier. The build servers often offer direct integration with GitHub, so it is just a matter of authorizing the build server with GitHub. When you push your code change into a remote repository, the build server receives the information automatically, and based on its configuration triggers a new build.

### Build

I know, the words “build server” sounds so complicated and expensive. But when you think about it, the only thing a build server needs to do for you is to generate pages and deploy them. Exactly what you did manually with one `npx` command and copy-paste operation. And that was not that hard, was it?

So how can you decide which build server to use? First, you need to choose whether you want to run the build locally on your server or remotely on a third-party service. I don’t have a local server I could use for this purpose, so I decided to use third-party services. These services include:

* [AppVeyor](http://bit.ly/2spdv0M)
* [Travis CI](http://bit.ly/2RKgW0q)

Both of these services are free for open-source projects.

“What? Is my website open-source? This guy is crazy!”

Am I? :-) I already mentioned the benefits of open-sourcing your website implementation in my [previous article about security](http://bit.ly/2QVSm9a). In most cases, websites are very similar in functionality, so there is probably no special know-how in your implementation. It’s the content that holds the value.

But let’s get back to the build server. I chose Travis CI as it was recommended to me by a colleague. We use it for many GitHub projects in our company. So how long does it take to set it up?

Initially, I was expecting a complicated UI to configure all aspects of a build within Travis (remember VSTS online?), so finding out it all sits in a single file was a relief. So the first thing you need to do is create a file #.travis.yml# in the root of your project. This file defines what is happening during a build.

```
dist: trusty language: node_js node_js: — "stable" before_script: — npm install script: — npm run build deploy: ...
```

```
packages.json:"scripts": { ... "build": "npx nuxt generate && cpx CNAME dist", ...}
```

You see it is straightforward to understand. First I instruct NPM to install all required packages as a prerequisite to running a build. Then all static files are generated into a `dist` folder — this is the default when using Nuxt. I also included a preview of a `packages.json` file, which defines build script. Note that I am also copying `CNAME` file to `dist` directory — this tells GitHub Pages I am using custom domain rather than github.io.

### Deployment

Finally the last part of the whole process. We have files generated, and now we need to transfer them to our hosting space, just like we did before using FTP. This is yet another thing a build server can do for you.

As I mentioned before I have chosen GitHub Pages as my host and Travis CI as a build server. Travis provides [many options](http://bit.ly/2RshbOb) for automated deployments including GitHub Pages, so the configuration was a piece of cake. Take a look at the deployment configuration:

```
deploy: local-dir: dist target-branch: master provider: pages skip-cleanup: true github-token: $GITHUB_TOKEN keep-history: true verbose: true on: branch: source
```

`Local-dir` defines where my generated static pages are, `target-branch` marks a branch in the GitHub repository to deploy to, and `pages` is the name of the Travis provider for GitHub Pages. To deploy successfully you also need to generate and provide a `github-token`. You see there is just a variable in the build configuration as the file sits in public repository. The token’s value is stored in repository settings in Travis UI.

### The finale of the series

And that’s it. That’s all you need to trigger, build, and deploy a static site automatically. Without any previous experience with build and deployment processes, this should not take you longer than a few hours. You see, static sites can be very dynamic in terms of content, the actual static file generating is handled automatically without a single human effort.

During this series of articles, I explained how to build a website using Content-as-a-Service (CaaS) to store your content, how to ensure your website is secure by not using any database, and how to ensure such a website still contains dynamic functionality like form submissions.

Good luck with your new static websites and have a [#staticNewYear](http://bit.ly/2QLE7Tj)!

#### Other articles in the series:

1. [How to start creating an impressive website for the first time](http://bit.ly/2Duglu1)
2. [How to decide on the best technology for your website?](http://bit.ly/2N0kXY4)
3. [How to power up your website with Vue.js and minimal effort](http://bit.ly/2zLRE8a)
4. [How to Mix Headless CMS with a Vue.js Website and Pay Zero](http://bit.ly/2CyDnhX)
5. [How to Make Form Submissions Secure on an API Website](http://bit.ly/2P0gidP)
6. [Building a super-fast and secure website with a CMS is no big deal. Or is it?](http://bit.ly/2QVSm9a)
7. [How to generate a static website with Vue.js in no time](http://bit.ly/2PN46Jy)
8. **How to quickly set up a build process for a static site**

