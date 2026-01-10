---
title: How to Containerize and Deploy Your Node.js Applications
subtitle: Let’s learn how to containerize your app with Docker and deploy it to production
  in just a few steps.
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-10-09T23:10:37.662Z'
originalURL: https://freecodecamp.org/news/how-to-containerize-and-deploy-your-nodejs-applications
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1760051426715/fd0f14cf-95dc-4191-b0fc-e5c916520097.png
tags:
- name: containers
  slug: containers
- name: Node.js
  slug: nodejs
- name: Docker
  slug: docker
seo_title: null
seo_desc: 'When you build a Node.js application, running it locally is simple. You
  type npm start, and it works.

  But when you need to run it on the cloud, things get complicated. You need to think
  about servers, environments, dependencies, and deployment pipeli...'
---

When you build a Node.js application, running it locally is simple. You type `npm start`, and it works.

But when you need to run it on the cloud, things get complicated. You need to think about servers, environments, dependencies, and deployment pipelines. That’s where containerization comes in.

Containers make your application portable and predictable. You can run the same code with the same setup anywhere, from your laptop to the cloud.

In this guide, we will walk through how to containerize a simple Node.js API and deploy it to the cloud. By the end, you will know how to set up Docker for your app, push it to a registry, and see your application running on the cloud.

## **Table of Contents**

* [Prerequisites](#heading-prerequisites)
    
* [What is Containerization?](#heading-what-is-containerization)
    
* [Setting Up a Node.js App](#heading-setting-up-a-nodejs-app)
    
* [Writing the Dockerfile](#heading-writing-the-dockerfile)
    
* [Building and Testing the Container](#heading-building-and-testing-the-container)
    
* [Preparing for Deployment](#heading-preparing-for-deployment)
    
* [Deploying to the Cloud](#heading-deploying-to-the-cloud)
    
* [Scaling Your App](#heading-scaling-your-app)
    
* [Updating Your App](#heading-updating-your-app)
    
* [Benefits of sing Containers](#heading-benefits-of-sing-containers)
    
* [Conclusion](#heading-conclusion)
    

## Prerequisites

Before we dive into containerizing and deploying your Node.js application, make sure you have the following set up on your system. These basics will help you follow along without running into errors.

**Node.js and npm**  
You should have [Node.js](https://nodejs.org/en) (v18 or higher) and npm installed on your local machine. This ensures you can run your app locally before containerizing it.  
To check your versions, run:

```python
node -v
npm -v
```

**Docker installed and running**  
[Docker](https://www.docker.com/) is the core tool we’ll use to containerize the app. Install Docker Desktop or Docker Engine depending on your system. Once installed, confirm that it’s running and working by typing:

```python
docker --version
```

**Docker Hub account (or any container registry)**  
You’ll need a Docker Hub account to push your container image to the cloud. This allows your deployment platform to pull and run the image. You can create one for free at [hub.docker.com](http://hub.docker.com)[.](https://hub.docker.com/)

Once you have these prerequisites ready, you’ll be set to build your first containerized Node.js app and deploy it to the cloud.

## **What is Containerization?**

Containerization is a way to package an application along with everything it needs to run. That includes the code, libraries, system tools, and settings. The package is called a container image.

When you run that image, you get a container that behaves exactly the same on any system that supports [Docker](https://www.freecodecamp.org/news/the-docker-handbook/).

Without containers, deployment can be messy. Your app might work on your machine but fail in production due to missing libraries or version mismatches.

Containers solve this by locking in the environment. Think of them as lightweight virtual machines that only contain what your app needs.

## **Setting Up a Node.js App**

Let’s start by building a simple Node.js API. We will keep it minimal so we can focus on the containerization and deployment steps.

Create a new folder and add a file called `server.js`:

```plaintext
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.json({ message: 'Hello from Container!' });
});
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

Next, create a `package.json` file with the following content:

```plaintext
{
  "name": "container-node-app",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^5.1.0"
  }
}
```

Run `npm install` to install the Express dependency. You now have a simple Node.js API that runs locally. You can test it with `npm start` and open `http://localhost:3000` in your browser.

## **Writing the Dockerfile**

To run this app in a container, we need to write a `Dockerfile`. This file defines how to build the container image. Create a new file called `Dockerfile` and add this:

```plaintext
FROM node:24

WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

Let’s break this down. We start with the official Node.js 24 image. We set a working directory inside the container. We copy the package files and install dependencies.

Then we copy the rest of the code. We expose port 3000 so that the app can accept traffic. Finally, we run `npm start` as the default command.

## **Building and Testing the Container**

Now that we have the `Dockerfile`, we can build the image. Run the following command:

```plaintext
docker build -t container-node-app .
```

This builds an image named `container-node-app`. To test it locally, run:

```plaintext
docker run -p 3000:3000 container-node-app
```

Open `http://localhost:3000` in your browser, and you should see the JSON message `{"message":"Hello from Container!"}`. At this point, we know our app works in a container.

## **Preparing for Deployment**

To deploy on any cloud platform, you need to push your image to a container registry. A registry is a place where container images are stored and shared. Your cloud provider can pull images from [Docker Hub](https://hub.docker.com/) or other registries.

Tag your image with a registry path. For Docker Hub, it looks like this:

```plaintext
docker tag container-node-app your-dockerhub-username/container-node-app:latest
```

Then log in and push it:

```plaintext
docker login
docker push your-dockerhub-username/container-node-app:latest
```

Your image should now be available in the cloud registry and ready for deployment.

Here’s mine:

![Docker Registry](https://cdn.hashnode.com/res/hashnode/image/upload/v1759747825354/e217d7f1-6131-41a2-a8b1-76e8ad84399a.webp align="center")

## **Deploying to the Cloud**

In this tutorial, I’ll be using Sevalla since it offers a free tier, so there are no costs involved to deploy this container to the cloud. You can use other providers like [AWS](https://aws.amazon.com/) or [Heroku](https://www.heroku.com/), but just note that you will incur costs for creating resources.

[Sevalla](https://sevalla.com/) is a modern, usage-based Platform-as-a-service provider. It offers application hosting, database, object storage, and static site hosting for your projects.

Once you have your account set up, you can create a new application and tell it which container image to use. Sevalla will pull the image from the registry, create a container, and handle the networking, scaling, and updates for you.

To get started, [login](https://app.sevalla.com/login) to Sevalla. In the dashboard, choose to create a new application. Give it a name like `node-api`. Provide the registry path of your image.

![Create application](https://cdn.hashnode.com/res/hashnode/image/upload/v1759747861994/4ad344d6-d8a5-4593-a85e-eb679bc600f5.webp align="center")

Choose a location and use the “Hobby” plan. Sevalla comes with a $50 free credit, so you wont be charged for deploying this image.

![Application Resources](https://cdn.hashnode.com/res/hashnode/image/upload/v1759747920267/cf23401d-131e-4c51-a248-411d8624542c.webp align="center")

Click “Create and Deploy”. Sevalla will handle the rest. You can watch it configure the application and run the deployment.

![Sevalla Deployment](https://cdn.hashnode.com/res/hashnode/image/upload/v1759747953591/79db7997-88a3-48f7-ae09-65703ec2abab.webp align="center")

Once the deployment is complete, click on “Visit app” to get your app’s live URL. You can see the response from the API.

![Sevalla deployment success](https://cdn.hashnode.com/res/hashnode/image/upload/v1759747987239/b3a1de3a-3f3a-48d6-86e1-27137f6b41fd.webp align="center")

## **Scaling Your App**

One of the main benefits of Sevalla is easy scaling. If you start getting more traffic, you can increase the number of containers running your app with just a few clicks. Sevalla will load balance traffic between them. This means your app can handle more requests without downtime.

Scaling with containers is efficient because each container runs the exact same code. There is no need to configure extra servers manually. Sevalla takes care of orchestration, so your focus stays on writing code instead of managing infrastructure.

## **Updating Your App**

When you make changes to your Node.js app, updating is straightforward. You rebuild the Docker image, push it to the registry, and tell Sevalla to redeploy.

Since containers are immutable, every new build creates a fresh environment. This ensures your updates are clean, consistent, and free of old dependencies.

For example, if you change the message in `server.js` and want to deploy it, you would run:

```plaintext
docker build -t your-dockerhub-username/container-node-app:latest .
docker push your-dockerhub-username/container-node-app:latest
```

Then trigger a redeploy in the Sevalla dashboard. Within minutes, your users will see the updated response.

## **Benefits of sing Containers**

[Containers](https://techcrunch.com/2016/10/16/wtf-is-a-container/) bring many advantages when deploying Node.js applications. They make your app portable because the container holds both the code and its dependencies, ensuring it runs the same way everywhere.

They improve consistency, since every build creates an isolated environment without leftover files or mismatched versions. Scaling becomes simple because you can spin up more containers as traffic grows, and each one behaves identically. Updates are cleaner too, as you replace old containers with fresh ones built from the latest code.

For developers, this means fewer surprises and less time fixing environment issues. Containers provide a reliable foundation, so you can focus on building features rather than troubleshooting deployments.

## **Conclusion**

Containerization is one of the most important shifts in modern software development. By learning how to put your Node.js app into a Docker container, you unlock the ability to run it anywhere.

In this guide, we built a small Node.js API, created a Dockerfile, tested the container locally, pushed it to a registry, and deployed it to the cloud. The steps you followed here apply to much larger and more complex applications as well. Once you get the basics, you can scale up your workflows to production-level projects.

Hope you enjoyed this article. Connect with me [on Linkedin](https://www.linkedin.com/in/manishmshiva/?originalSubdomain=in) or [visit my website](https://manishshivanandhan.com/).
