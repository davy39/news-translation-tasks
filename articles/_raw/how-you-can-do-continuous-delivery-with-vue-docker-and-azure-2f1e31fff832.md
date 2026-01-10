---
title: How you can do continuous delivery with Vue, Docker, and Azure
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T00:02:57.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-do-continuous-delivery-with-vue-docker-and-azure-2f1e31fff832
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6HS029y9bDY2lcUlub7ZRw.png
tags:
- name: Docker
  slug: docker
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Burke Holland

  A few weeks ago at ng-conf, I announced the launch of vscodecandothat.com — a project
  I worked on with Sarah Drasner to centralize all of my favorite VS Code tips into
  a collection of short, silent video clips. It’s like a site full ...'
---

By Burke Holland

A few weeks ago at [ng-conf](https://www.youtube.com/watch?v=Xco-TEI-HU4), I announced the launch of [vscodecandothat.com](https://vscodecandothat.com/?WT.mc_id=deployingvue-medium-buhollan) — a project I worked on with [Sarah Drasner](https://twitter.com/sarah_edo) to centralize all of my favorite VS Code tips into a collection of short, silent video clips. It’s like a site full of GIFs, except without the 600 megabyte payload and crashed browser tab.

![Image](https://cdn-media-1.freecodecamp.org/images/1*V69E9qH9mcX-h8Ao_XeBZg.png)

Sarah designed and built the site using Vue. I put together the video clips with excessive pug references.

%[https://youtu.be/drXu4L-4Q3I]

Sarah and I both work on the Azure team, so it was a good chance for us to use our own tools here at Microsoft to work with a real application. In this article, I’m going to break down how we do continuous delivery with vscodecandothat.com, and how you can do it yourself using the same tools we use.

Before we talk about the setup, I want to define exactly what I mean by “continuous delivery.”

### Continuous something-or-other

The term Continuous Delivery refers to making releases easy, fast, and streamlined. We can argue about the exact definition of the term, but just remember that I am a front-end developer so my eyes _may_ glaze over. I may snore. But go on. I swear I’m listening.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MquNEw7qIsb7l7ez_vdRMA.gif)

For our purposes, “Continuous Delivery” means that the process of building and deploying the site is completely automated. Here’s how that looks in real life:

* Developer checks code into Github master branch
* Build server pulls code from Github
* Build server runs a build (npm script)
* Build server creates a Docker container
* Build server pushes Docker container to registry
* Burke finds the source of broccoli smell in his office
* Website pulls in updated container

Got all that? Basically, we’re going to automate everything that you would normally do as a developer so that checking code into Github is all you have to worry about. And lord knows that’s [hard enough as it is](http://ohshitgit.com/).

%[https://twitter.com/TheLarkInn/status/990464006962982912?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fthelarkinn%2Fstatus%2F990464006962982912%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F923008231689003008%25252FChLxnzy9_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

OK, let’s begin at the beginning. The first thing we need to do is look at the application to see how it runs. And how it runs is “In a Docker, y’all.”

### Running Vue on Docker

vscodecandothat.com is entirely front-end driven. It’s all HTML, JavaScript, and CSS in your browser. That being the case, all we want to do is serve up the `index.html` page from the _dist_ folder. We use an nginx web server.

When you are just serving up static assets, the Dockerfile is very simple…

```
FROM nginx
WORKDIR /app
# Copy in the static build assets
COPY dist/ /app/
# Copy in the nginx config file
COPY misc/nginx.conf /etc/nginx/nginx.conf
# All files are in, start the web server
CMD ["nginx"]
```

Sarah created an nginx configuration file that we just copy in when the container gets built. Because you do not want to be in the business of configuring nginx (OMG you don’t), Sarah has posted her config file [to a gist](https://gist.github.com/sdras/2bfe545bb4df9a1a8e03b7ba73b086d5).

%[https://twitter.com/geddski/status/505082283917721600?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext%252Fhtml%26key%3Da19fcc184b9711e1b4764040d3dc5c07%26schema%3Dtwitter%26url%3Dhttps%253A%2F%2Ftwitter.com%2Fgeddski%2Fstatus%2F505082283917721600%26image%3Dhttps%253A%2F%2Fi.embed.ly%2F1%2Fimage%253Furl%253Dhttps%25253A%25252F%25252Fpbs.twimg.com%25252Fprofile_images%25252F828768956727042048%25252Fnd_Weyq4_400x400.jpg%2526key%253Da19fcc184b9711e1b4764040d3dc5c07]

I use the [Docker extension for VS Cod](https://marketplace.visualstudio.com/items?itemName=PeterJausovec.vscode-docker&WT.mc_id= vscodecandothat-medium-buhollan)e so that I can see and manage all of my images and containers. I’m not afraid of the terminal, but my brain can only remember so many flags.

![Image](https://cdn-media-1.freecodecamp.org/images/1*d6oT_mBMiy62By7DCMoRUA.png)

Now we need a registry to push the container to. We’re going to configure [Azure Container Services](https://docs.microsoft.com/en-us/azure/container-registry/?WT.mc_id=vscodecandothat-medium-buhollan) (ACR) for that.

You can create an ACR repository from the web portal, but to prove I’m not afraid of the terminal, we’ll do it with the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest&WT.mc_id=vscodecandothat-medium-buhollan).

First, we need a group for resources. I called mine “vsCodeCanDoThat”.

```
az group create — name vsCodeCanDoThat — location eastus
```

Now create the ACR repository. I called mine “hollandcr”.

```
az acr create --resource-group vsCodeCanDoThat --name hollandcr --sku Basic
```

Now we can push our image to that by tagging it with the path to the Azure Container Registry.

```
hollandcr.azurecr.io/vscodecandothat:latest
```

> [In the video](https://content.screencast.com/users/burkeholland/folders/Snagit/media/fea2bf7c-bbc1-44de-9712-df5409242a1c/2018-05-02_15-14-44.mp4) you can watch me login to the Azure Container Registry from the terminal. This is important because your push will fail if you are not logged in.

OK — now we need a site to host our container. For that we use Azure App Service.

### Creating The App Service

First create a Linux service plan. For that, you need your app name and your resource group.

So

```
az appservice plan create -n appName -g resourceGroupName --is-linux -l "South Central US" --sku S1 --number-of-workers 1
```

Becomes

```
az appservice plan create -n vsCodeCanDoThatSP -g vsCodeCanDoThat --is-linux -l "South Central US" --sku S1 --number-of-workers 1
```

Now create the web app and point it at the container that was pushed to the AKS registry. This takes 4 parameters.

* Service Plan
* Resource Group
* App Name (you haven’t defined this yet)
* Docker image that you pushed earlier

```
az webapp create -n vsCodeCanDoThatSP -g vsCodeCanDoThatRG -p vscodecandothat -i hollandcr.azurecr.io/vscodecandothat:latest
```

And that’s it. You’ll get back a URL, and you should be able to open it and see your site running.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hIRBA71rQYN48JtUx39t3A.png)

Now what we want to do is automate everything that we just did. We never ever want to have to go through any of these steps again.

The first thing we will do is to set up our site for “Continuous Deployment” from our container registry.

If you are using the App Service extension for VS Code, all of your Azure sites will show up right in the editor. You can just right-click and say “Open in Portal.”

![Image](https://cdn-media-1.freecodecamp.org/images/1*YDEY6T-QBDuVYVz3eVVbAg.png)

Select the “Docker Container” menu option…

![Image](https://cdn-media-1.freecodecamp.org/images/1*LfVbCk3RokfybznGg2fC7Q.png)

On this page you will see the container you configured from the terminal. There is an option at the bottom to turn on “Continuous Deployment.”

![Image](https://cdn-media-1.freecodecamp.org/images/1*eUT84plmPQ6qbLN3qdobSA.png)

When you toggle this on and click “save,” a webhook will get created in your Azure Container Registry for this specific container. Now, anytime the image with tag “latest” is updated, the webhook will fire and notify App Service which automatically pulls in your image.

So we’ve automated some of this already. Once we push the image, it will be deployed. There is nothing we have to do besides push it. But we don’t want to push it. We want someone else to that.

And who will do it? The robots, that’s who. Or whom? OR WHOMST. Fortunately I’m not in high school English anymore. I failed it once and that was enough.

### Setting up a build server

This is the point at which I tell you that we are going to use [Visual Studio Team Services](https://www.visualstudio.com/team-services/?WT.mc_id=deployingvue-medium-buhollan&WT.mc_id=vscodecandothat-medium-buhollan) (VSTS). Then you say, “Visual Studio? I’m not using .NET”. And I say, “I know, it’s confusing.”

We need a system specifically designed to automate builds and deployment. This is exactly what VSTS is/does. Also, it’s free for 5 users or less (in a project space) and “free” is the only word in my love language. The only word besides “beer.”

[Create a VSTS account](https://www.visualstudio.com/team-services/?WT.mc_id=vscodecandothat-medium-buhollan) if you don’t have one. Once you do, you land on the dashboard screen.

From here, you want to create a new team project.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DQSji2DhaqqWJTNPFNh2vg.png)

Give your project a name and a description that nobody will find helpful. Leave the version control at Git.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZVv_w22aLz66pa0Bgk_PPg.png)

The next screen gives you a Git URL to check your code into. But we already have Github, so just ignore that and select the “or build code from an external repository” option.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gRKs17VBTOGkndVfF6nT4Q.png)

Authorize VSTS to Github and select the repo…

![Image](https://cdn-media-1.freecodecamp.org/images/1*mGMehWVxowKVx9Gw2YAwCQ.png)

The next screen is offering to help you start with a template. In this case we are going to roll from an empty process. Because we are hard core like that.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Oj1YrEGKpNPqYdpN9sG0SQ.png)

Now we are going to start adding steps for VSTS to perform to do the build and deployment. The pull from source control is already happening, so the first thing we need to do is to run `npm install` on our code. To do that, add a task to “phase 1”. There is only 1 phase in our build / deployment.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xzQqzeSJmzD2SE-3Dtv3Bg.png)

Search for “npm” and add the npm task.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xpXq3R_ybbpEHT2qWNr4fQ.png)

By default, you get the `npm install` task, which is exactly what we want. You don’t need to add any options to this task.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ibpx3tqNj_obOO_JipQs2A.png)

Next, we’ll be running the `npm run build` command, which will build a production instance of our Vue app with all of its Webpacking magic. For that, add another npm task. This time, change the name to “npm run build.” Set the “command” to “custom” and the “command and arguments” to “run build.”

![Image](https://cdn-media-1.freecodecamp.org/images/1*Vmaq_Ap8qQKjHxyCyJZI5w.png)

Great! We’ve got the build, now we’re ready to Dockerize it. Add a new task and find the “Docker” one.

This is a big screen, so here’s the image and then we’ll walkthrough the highlights.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CEdpDsdurnim2O8rk-HLig.png)

* You are selecting the “Azure Container Registry”
* Specify your Azure subscription
* Specify your registry name (which we created earlier)
* Set the “Image Name” to $(Build.Repository.Name)
* Make sure you check the “Include Latest Tag”

Lastly, we want to push the image. Add another Docker task. This time, set the “Action” to “Push an image”. Set the “Image Name” to $(Build.Repository.Name) — just like before.

**DO NOT SELECT THE “PUSH IMAGES” ACTION**. If you do, your build will fail and you will blame god and all humanity before you figure out that you selected the wrong action. Don’t ask me how I know that.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KMy6Gh269uDeHfZdBi2BFg.png)

And that’s it for defining the Build definition. You can now click “save and queue” at the top. Make sure that you select a “Hosted Linux Preview” agent. The Docker tasks needs the Linux agent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*13JqFhuyHXeLuJQBGnwcTg.png)

Now sit back and wait for a build to kick off. If you’ve done everything right, you have now setup a completely automated build and deployment system for a Vue app that utilizes Docker and Azure. That’s the most buzzwords I’ve ever squeezed into one sentence.

### Deploy and be happy

This seems like a lot to setup, but once you have it just like you want it, all you have to do is check in code to your Github repo and all of this manual deployment ? happens automatically. Your customers will love you. Your developers will love you. Heck — even YOU might love you.

I hope you find this helpful. I’m off to update my résumé with all of these buzzwords.

