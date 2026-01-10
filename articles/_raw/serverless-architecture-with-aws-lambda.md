---
title: 'The Serverless Architecture Handbook: How to Publish a Node Js Docker Image
  to AWS ECR and Deploy the Container to AWS Lambda'
subtitle: ''
author: Prince Onukwili
co_authors: []
series: null
date: '2025-04-17T02:19:13.327Z'
originalURL: https://freecodecamp.org/news/serverless-architecture-with-aws-lambda
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744843935296/c359998f-1657-482f-adf4-5ab023cb1c02.png
tags:
- name: AWS
  slug: aws
- name: aws lambda
  slug: aws-lambda
- name: Docker
  slug: docker
- name: Node.js
  slug: nodejs
- name: serverless
  slug: serverless
- name: ecr
  slug: ecr
seo_title: null
seo_desc: 'Imagine you’re tasked with building a web application that can handle incoming
  traffic surges as your users grow without accumulating too much cost. Sounds like
  a dream, right?

  But here’s the thing: traditionally, to do this, you would have to manage...'
---

Imagine you’re tasked with building a web application that can handle incoming traffic surges as your users grow without accumulating too much cost. Sounds like a dream, right?

But here’s the thing: traditionally, to do this, you would have to manage lots of infrastructure – resources on which your application will be deployed – which can be a real headache. You’d have servers (VM instances or physical computers) to configure, databases to scale, load balancers to monitor...it’s a whole lot 😩

This is where Serverless architecture comes to the rescue. With the Serverless model, you can deploy your applications to handle thousands of users without you having to worry about incurring too much cost, managing infrastructure, servers, networking, and so on.

In this article, you’ll learn about Serverless Architecture: what it’s all about, and how to deploy your very own application using AWS Lambda. We’ll walk through the entire process step-by-step:

* How to clone your application repository using Git.
    
* How to build an image of your application using Docker.
    
* How to install the AWS CLI on your local machine and create AWS IAM users with the right permissions to push your Docker image to AWS Elastic Container Registry (ECR).
    

Once the image is up and running on ECR, we’ll then connect it to AWS Lambda and deploy the container to Lambda for a fully serverless experience. 💡✨

Ready to go serverless? Let’s get started! 🚀

## Table of Contents

1. [What is Serverless Architecture?](#heading-what-is-serverless-architecture)
    
2. [Differences Between Serverless and Other Deployment Models ⚡](#heading-differences-between-serverless-and-other-deployment-models)
    
3. [🧠 Prerequisites — What You Should Know Before Following Along!](#heading-prerequisites-what-you-should-know-before-following-along)
    
4. [How to Set Up the Application Using Git 🐙](#heading-how-to-set-up-the-application-using-git)
    
5. [Understanding the Codebase 🔎](#heading-understanding-the-codebase)
    
6. [How to Create a Docker Image of the Application 🐋](#heading-how-to-create-a-docker-image-of-the-application)
    
7. [How to Create a Container Registry on AWS Elastic Container Registry (ECR) 📁](#heading-how-to-create-a-container-registry-on-aws-elastic-container-registry-ecr)
    
8. [IAM with AWS: How to Create a User on AWS IAM to Allow Access to Your AWS ECR 👤🔐](#heading-iam-with-aws-how-to-create-a-user-on-aws-iam-to-allow-access-to-your-aws-ecr)
    
9. [How to Upload Your Docker Image to the AWS ECR repository ⬆️](#heading-how-to-upload-your-docker-image-to-the-aws-ecr-repository)
    
10. [How to Deploy the Application Container to AWS Lambda from the Image on AWS ECR 🚀](#heading-how-to-deploy-the-application-container-to-aws-lambda-from-the-image-on-aws-ecr)
    
11. [Advantages of Adopting the Serverless Model in Businesses 💼](#heading-advantages-of-adopting-the-serverless-model-in-businesses)
    
12. [Disadvantages of the Serverless Model 🚫](#heading-disadvantages-of-the-serverless-model)
    
13. [When to Adopt the Serverless Model 🤔](#heading-when-to-adopt-the-serverless-model)
    
14. [Conclusion 📝](#heading-conclusion)
    
15. [About the Author 👨‍💻](#heading-about-the-author)
    

## What is Serverless Architecture?

Before we dive deeper, let’s break down what we mean by Servers. In the tech world, servers are powerful computers that store, process, and manage data. Think of them as the behind-the-scenes workhorses that:

* **Store your data:** Like a central filing cabinet for your digital documents.
    
* **Run your applications:** They execute the code that keeps your app or website running.
    
* **Handle requests:** Servers respond to user requests – like loading a webpage or processing a login.
    

Alright, now let’s talk about Serverless Architecture – but first, let’s clear up a common misconception. When most people hear the word "Serverless", they immediately think, "Wait… no servers? How does that even work?!" 😅

Here’s the truth: Serverless doesn’t mean there are no servers involved (surprise, surprise! 😉). Instead, it means you, as a developer, don’t have to worry about managing the servers that your application runs on. The server-side infrastructure is fully handled by the cloud provider – in this case, AWS Lambda. You just focus on writing code and deploying it, and AWS takes care of the rest.

### So, What’s the Big Deal with Serverless?

In a traditional setup, when you deploy your application, you’re responsible for things like:

* **Provisioning servers** (how many servers do you need? What size?)
    
* **Scaling resources** (how do you handle traffic spikes without overpaying?)
    
* **Monitoring** and keeping everything running smoothly.
    

Sounds like a lot, right? 🤯 Well, Serverless Architecture simplifies all of that by letting you focus purely on your application code. With Lambda, you can run code in response to events (like an HTTP request, a file upload, or a database change) without worrying about the infrastructure behind it. AWS automatically scales the compute resources as needed, charging you only for the time your code is actually running. ⏱️💸

Imagine you’re at a restaurant. Instead of running the kitchen yourself (like managing your own servers), you just place an order (your code) and the chef (AWS Lambda) makes it for you, on-demand, based on what you need. 🍽️🍴

## Differences Between Serverless and Other Deployment Models ⚡

Now that you understand how Serverless works, let’s take a little detour and explore the other models used to deploy applications. After all, Serverless isn’t the only kid on the block, and this will give you some important perspective when choosing the right model for your use case. 👀

When you build an app, you need somewhere to host it – a home for your code to live and run. Over the years, the tech world has come up with different ways to handle this, and each one gives you a different level of control (and responsibility) over your servers.

Let’s break it down.

### 🏠 Infrastructure as a Service (IaaS)

With IaaS, cloud providers like AWS, Google Cloud, or Microsoft Azure give you the building blocks – virtual servers (also called instances), storage, and networking tools – but it’s still your job to set everything up.

It’s like renting an empty apartment. You get the walls, the doors, and the roof, but you still have to bring your own furniture, set up your Wi-Fi, and clean the place regularly. 🏡🧹

When you choose IaaS, you’re responsible for:

* Configuring the servers (choosing the size, the operating system, and installing software).
    
* Handling updates, patches, and security.
    
* Scaling up or down when traffic changes.
    

**Example:** Amazon EC2 (Elastic Compute Cloud) is a classic IaaS service. You rent a virtual machine, set it up yourself, and manage it like a digital landlord.

### 🎯 Platform as a Service (PaaS)

Next up, we’ve got PaaS – a more polished setup.

In this model, the cloud provider takes care of the infrastructure and the underlying operating system, so you don’t have to. You just upload your code, configure a few settings, and the platform runs your app.

It’s like moving into a fully furnished apartment — the kitchen works, the lights are on, and the Wi-Fi is already connected. You just show up with your bags and get to work! 🧳✨

**Example:** AWS Elastic Beanstalk, Heroku, or Google App Engine.

### 🌩️ Serverless: The Special PaaS

Now here’s where things get interesting: Serverless actually falls under the PaaS umbrella, but it deserves its own spotlight. Why? Because it takes the convenience of PaaS and pushes it to the next level.

In a traditional PaaS model (like AWS Fargate or Heroku), your application is running 24/7, whether you have visitors using it or not. You pay for the reserved space and compute power all month long, just like renting an apartment. Even if you didn’t sleep there the entire month, the bill still comes at the end. 💸🏡

But with Serverless, the rules change. You only pay when your code is actually being used.

#### How Applications Run in the Serverless Model ⚙️

In a Serverless model, your application isn’t just sitting there running all day. It “wakes up” only when it’s needed. But what exactly causes it to wake up? That’s where triggers come in.

Triggers are events that tell your Serverless application, “Hey, it’s time to do something!” These events could be all sorts of things, like:

* A user visiting your website and clicking a button.
    
* Someone uploading a file to your cloud storage (like an image or document).
    
* A new row being added to a database.
    
* An automated schedule (like a reminder that runs every day at 8 AM).
    

When one of these events happens, your application instantly comes to life, runs the exact task you programmed, and then goes back to “sleep” until the next trigger. This is how Serverless keeps your cloud costs low and your resources efficient – no constant running in the background, only action when there’s actually something to do!.⚡😎

For example, if a user sends a request that triggers your application to run for just 10 seconds and uses 20MB of memory, that’s all you pay for — the exact time and resources consumed.

No users? No requests? No payment. Now that’s a smart way to save money. 🧠💰

### 💡 Quick Comparison: PaaS vs Serverless

| **Feature** | **Traditional PaaS (example: AWS Fargate)** | **Serverless PaaS (example: AWS Lambda)** |
| --- | --- | --- |
| Server Configuration | You select compute size & limits. | No need — AWS handles it all. |
| Scaling | You configure scaling policies. | Automatic, event-driven scaling (based on incoming traffic). The higher the traffic, the more compute power is added to your application, and vice versa. 😃 |
| Billing | Charged for running instances 24/7, even when idle. | Charged only when your code runs. ⏱️💸 |
| Deployment | Deploy full applications. | Deploy small chunks of code (functions). You can also deploy microservices and full-scale web applications |

---

## 🧠 Prerequisites — What You Should Know Before Following Along

Before we dive in, here’s the best part: I wrote this article to be super beginner-friendly and detailed, so even if you have little to no programming background, you’ll still be able to follow along.

Whether you’re a developer, a tech-curious startup, or a business leader trying to understand modern cloud solutions, this guide was written for you.

That said, having some light knowledge in these areas will make the ride even smoother:

* 🧑‍💻 Basic Programming Concepts – like how Node.js apps run and what a server does.
    
* 💡 Familiarity with Common Tech Terms – words like “deploy,” “application,” “CPU,” and “software” will pop up, but don’t worry: I’ve done my best to break these down into simple, relatable explanations.
    

No prior cloud experience? No problem! This guide holds your hand all the way from setup to deployment – all in plain language, no jargon.

So buckle up, and let’s proceed with deploying your very own application to AWS Lambda. 😁

## How to Set Up the Application Using Git 🐙

Before we jump into writing code or deploying anything, the very first step is to grab the application we’ll be working with — and for that, we’ll be using Git.

But wait... what’s Git? — It’s a Version Control System (VCS) that helps developers track changes to their code, collaborate with teammates without stepping on each other’s toes, and safely store their work in a central place — like GitHub.

### Clone the Application Repository 🧑‍💻

I’ve already created a simple project for us to use in this tutorial — it’s sitting pretty on GitHub, waiting for you.

To clone the project onto your local machine, open up your terminal and run:

```bash
git clone https://github.com/onukwilip/lambda-tutorial.git
```

This command will download all the code from the `lambda-tutorial` repository into a folder on your computer. 📁

Once the cloning is done, navigate into the project directory like this:

```bash
cd lambda-tutorial
```

Boom — just like that, your local machine is now set up with the same code that’s stored in the GitHub repo. 🏡

## Understanding the Codebase 🔎

### Open the Codebase in Your Favorite IDE 🧑‍💻

For this tutorial, we’ll be using Visual Studio Code (VS Code), but feel free to use any editor you’re comfortable with.

Once you open the `lambda-tutorial` project folder, you’ll notice it’s a simple Node.js web server. Nothing too fancy — just a server that can handle requests and respond with some data.

Now, it’s important to understand what’s going on inside our codebase, especially if you’re coming from deploying on platforms like Render, Vercel, or Google Cloud Run.

### **Deploying to Lambda vs Other Serverless Platforms ⚡**

When you deploy to platforms like Vercel, Render, or Google Cloud Run, you usually package your web server just the way you wrote it – whether it’s a Node.js Express server or a Next.js app – and the platform handles it pretty much as-is.

Those platforms run your server like a mini container (or microservice) that’s always ready to handle incoming traffic, just like a waiter standing by at your table, waiting for your order.

But AWS Lambda works a little differently.

Lambda expects your code to be organized around functions – not full web servers. Think of Lambda as a chef that only shows up the moment an order is placed, cooks the food, and disappears once the job is done. 👨‍🍳🍽️

So if you’ve got a full-blown Node.js Express server, you’ll need to do a tiny bit of “translation” to fit Lambda’s expectations – and that’s where the lambda.js file comes in.

#### The `lambda.js` File — Your Lambda Translator 🔀

Here’s what the file looks like:

```javascript
const serverless = require("serverless-http");
const app = require("./app");

const handler = serverless(app);
module.exports.handler = handler;
```

Let’s break it down:

* `const serverless = require("serverless-http");`: This imports a handy little library called serverless-http. (The `serverless-http` library is important for our platform to run properly on AWS Lambda.) It acts like a translator: it takes your regular Express app and wraps it so that AWS Lambda can understand it.
    
* `const handler = serverless(app);`: Here’s the magic. This wraps your Express app into a Lambda-compatible function.
    
* `module.exports.handler = handler;`: This exports your wrapped function so AWS Lambda can call it when the application is triggered.
    

So, instead of starting your server like this:

```javascript
app.listen(5000, () => {
  console.log("Server running on port 5000");
});
```

You’re handing your app over to Lambda and letting it handle incoming requests, scale, and run the app only when it’s needed.

#### The `app.js` File — Your Classic Express App 💻

Your `app.js` is where the main application logic lives. Here is usually where you:

* Set up Express.
    
* Define routes (like `/api`, `/users`, `/hello`).
    
* Apply middleware (like JSON parsing, logging, CORS, and so on).
    
* Handle HTTP requests and send back responses.
    

In a normal deployment (Render, Google Cloud Run, DigitalOcean, or your own server), you’d start the server using `app.listen(PORT)` at the bottom of this file.

But since we’re deploying to Lambda, you don’t directly start the server here. Instead, you export the `app` like this:

```javascript
module.exports = app;
```

This way, your application stays “server-agnostic” – it’s not hardcoded to run on a traditional server. Lambda (via the `lambda.js` file) takes care of starting and stopping your app whenever it’s triggered by an event (like an HTTP request). Smart, right? 💡

Why this setup? 🤔

This little separation gives you flexibility:

* You can write your Node.js app like you always would (using `Express`) inside `app.js`.
    
* And you only tweak the entry point (via `lambda.js`) to fit AWS Lambda’s expectations.
    

## How to Create a Docker Image of the Application 🐋

Now that we’ve had a good look at the code, let’s package it up the smart way — using Docker.

### What is Docker? 🐳

Now, you might be wondering, *"Why are we using Docker?"*

Docker is a software for creating images of your applications and running those images as containers. Just like real-world shipping containers hold goods securely, Docker containers hold your app, bundled with everything it needs to run: its code, libraries, dependencies, and settings. Everything is all wrapped up neatly, so your app runs the same way everywhere, whether on your laptop, AWS Lambda, or even your friend’s machine.

### Let’s Take a Look at the Dockerfile 🔍

Inside your project folder, you’ll find a file named `Dockerfile`. This is basically the recipe that Docker uses to build your app’s container image.

Here’s what it looks like:

```dockerfile
FROM node:18-slim AS builder

WORKDIR /app

COPY package.json .

RUN npm i -f

COPY . .

USER root

FROM amazon/aws-lambda-nodejs

ENV PORT=5000

COPY --from=builder /app/ ${LAMBDA_TASK_ROOT}
COPY --from=builder /app/node_modules ${LAMBDA_TASK_ROOT}/node_modules
COPY --from=builder /app/package.json ${LAMBDA_TASK_ROOT}
COPY --from=builder /app/package-lock.json ${LAMBDA_TASK_ROOT}

EXPOSE 5000

CMD [ "lambda.handler" ]
```

Let’s break down the important steps— in plain English: 😎

* `FROM node:18-slim AS builder`: We start by using a lightweight version of Node.js called `node:18-slim` and give it a tag named `builder` (think of it as Stage 1). This gives us the tools we need to build a Node.js app, but without extra stuff that makes the image heavy. The tag `builder` enables us to re-use the content of this build in the next stage
    
* `WORKDIR /app`: We set the working directory inside the container to `/app`. Think of this as telling Docker: *"Hey, this is the folder where I’ll be working from!"*
    
* `COPY package.json .`: This copies the `package.json` file (which lists your app’s dependencies) into the `/app` folder inside the container.
    
* `RUN npm i -f`: This installs all the Node.js dependencies (the packages your app needs to work).  
    The `-f` flag forces npm to resolve conflicts if any pop up.
    
* `COPY . .`: This copies the rest of your project files from your computer into the container.
    
* `USER root`: This sets the user to root (administrator level) inside the container. Useful when extra permissions are needed for certain tasks.
    
* `FROM amazon/aws-lambda-nodejs`: Now here’s the switch: we swap to the official AWS Lambda base image for Node.js! That is, Stage 2. This image is designed to work smoothly when deploying containers to Lambda.
    
* `ENV PORT=5000`: We set an environment variable for the server port. Our app will listen on port 5000.
    
* `COPY --from=builder /app/ ${LAMBDA_TASK_ROOT}`: This grabs all the files from the builder stage and copies them into Lambda’s special working directory (`${LAMBDA_TASK_ROOT}`).
    
* `COPY --from=builder /app/node_modules ${LAMBDA_TASK_ROOT}/node_modules`: Same thing, but this one specifically copies the node\_modules folder (all your installed dependencies) into Lambda’s working directory.
    
* `COPY --from=builder /app/package.json ${LAMBDA_TASK_ROOT}`: Copies the `package.json` file into Lambda’s working directory.
    
* `COPY --from=builder /app/package-lock.json ${LAMBDA_TASK_ROOT}`: Copies the lock file for your dependencies – so Lambda knows exactly which versions of libraries to use.
    
* `EXPOSE 5000`: This tells Docker, *“Hey, my app is going to listen for requests on port 5000!"* (Though Lambda doesn’t use this directly, it’s useful for local testing.)
    
* `CMD [ "lambda.handler" ]`: This tells AWS Lambda which function to run when the container starts.  
    In this case, it’s looking for a `handler` function inside your app – that’s the entry point!
    

### How to Create Our Own Docker Image

Before we proceed, you need to have Docker running on your machine. If you haven’t installed Docker yet, check out the official installation guide here: [Docker Installation Tutorial](https://docs.docker.com/engine/install/). It’s a great resource to get Docker up and running.

#### Ensure Docker is Running

Make sure Docker Desktop is installed and running. You can usually tell by the Docker icon in your system tray. If it’s not running, start it up before proceeding.

#### Build the Docker Image

Now, it’s time to create a Docker image of our application. In your terminal, navigate to the root directory of your project (where your Dockerfile is located). Then run the following command:

```bash
docker build -t demo-lambda-project:latest .
```

* The `docker build` command tells Docker to create an image.
    
* The `-t demo-lambda-project:latest` flag assigns a tag (or name) to your image (we’ll change this later to the image naming convention supported by AWS Elastic Container Registry – ECR).
    
    * Here, `demo-lambda-project` is the name, and `latest` is the tag indicating the most recent build.
        
* The `.` at the end tells Docker to look for the Dockerfile in the current directory.
    

#### What This Does

Docker will now follow the instructions in your Dockerfile step-by-step. It starts by building your Node.js app (using the lightweight Node 18 image), installs the dependencies, and then copies everything over to an AWS Lambda-ready image. Once done, you have a neat image tagged as `demo-lambda-project:latest` that’s ready for deployment.

## How to Create a Container Registry on AWS Elastic Container Registry (ECR) 📁

Okay, let’s dive into creating an image registry on AWS Elastic Container Registry (ECR). Follow these steps closely to set up your repository named lambda-practice:

### Step 1: Sign In and Navigate to AWS ECR

Log in to your AWS Management Console: [https://console.aws.amazon.com/console/home](https://console.aws.amazon.com/console/home).

In the search bar at the top, type "ECR". You should see Amazon ECR pop up in the dropdown results. Click on it to navigate to the Elastic Container Registry section.

### Step 2: Start Creating Your Repository

Once you’re in the ECR section, look for a button that says "Create repository". Click this button to start setting up your new container registry.

![Create new AWS ECR repository](https://cdn.hashnode.com/res/hashnode/image/upload/v1744649904087/615bbd21-c6ed-4243-9a18-10042eec9634.png align="center")

### Step 3: Configuring the Repository Details

You’ll need to add some info like:

* **Repository name:** In the form that appears, enter `lambda-practice` as the repository name. This name will be used to reference your repository later when uploading your Docker image.
    
* **Tag mutability:** You’ll also see an option for Tag Mutability. For this tutorial, set it to Mutable. This means that if you need to update or change a tag on your image later, you can do so. (Keep in mind that in some scenarios, you might want immutable tags for images used in production environments – but mutable tags are great for testing and development, especially since we want to use the tag `latest` for our images.)
    

When you’re happy with the settings, click the "Create repository" button at the bottom of the form.

![Configure AWS ECR repository](https://cdn.hashnode.com/res/hashnode/image/upload/v1744650070919/3010590f-f2e3-4d52-9631-8c5d4e1a5239.png align="center")

### Repository Created – Now Let's Take a Look

After creating the repository, AWS will redirect you to the page listing your repositories.

Find the repository named `lambda-practice` in the list. This is your newly created container registry where you can push Docker images.

Copy the `lambda-practice` repository URI, which we’ll need later when we push our image from our local machine. The URI should be in a format similar to this - `<aws_account_id>.dkr.ecr.<region>.amazonaws.com/lambda-practice`

![Completed creation of AWS ECR repository](https://cdn.hashnode.com/res/hashnode/image/upload/v1744650192129/67d724c7-15da-4ff1-8e38-638c3a8d1aa4.png align="center")

And that’s it! You’ve now successfully created a container registry on AWS ECR and have your repository (`lambda-practice`) ready to receive your Docker image. 🚀

## IAM with AWS: How to Create a User on AWS IAM to Allow Access to Your AWS ECR 👤🔐

Now that we’ve successfully created our AWS ECR container registry (the home for our Docker image), it's time to make sure our local machine has the necessary permissions to interact with that registry. Without proper authorization, we won’t be able to upload our image.

To do that, we’ll create an IAM user with the appropriate permissions.

### Step 1: Access the IAM Console

Start by logging in to your AWS Management Console: [https://console.aws.amazon.com/console/home](https://console.aws.amazon.com/console/home).

In the search bar at the top, type "IAM" and select the IAM service from the dropdown. This brings you to the IAM dashboard where you can manage users, roles, policies, and more.

### Step 2: Navigate to the Users Section

On the left sidebar of the IAM dashboard, click on "Users". Here you'll see a list of existing users, and this is where you'll add a new one.

![Create AWS IAM User](https://cdn.hashnode.com/res/hashnode/image/upload/v1744651384601/085a25ca-82eb-447b-8106-46df32264a85.png align="center")

### Step 3: Create a New User

Click the "Add users" button at the top. In the "Set user details" step, enter the username as `lambda-practice`.

### Step 4: Attach Permissions Directly

In the "Set permissions" step, choose "Attach policies directly". In the search box, type `AmazonEC2ContainerRegistryPowerUser`. Select the `AmazonEC2ContainerRegistryPowerUser` policy by ticking its checkbox. This policy grants the necessary permissions to work with AWS ECR, such as pushing and pulling Docker images.

Click Next, and verify that the username is `lambda-practice` and that the AmazonEC2ContainerRegistryPowerUser policy is attached. If everything looks good, click "Create user".

![Add policy to AWS IAM User](https://cdn.hashnode.com/res/hashnode/image/upload/v1744651476901/c6d91c8c-9757-4cc6-a00f-c23d3a72de59.png align="center")

### Step 5: Generate Access Keys for the User

Once the user is created, you’ll be redirected to the page listing all IAM users. Locate and click on the user `lambda-practice`. This action will take you to the user’s summary page.

* Navigate to the "Security credentials" tab.
    
* Under "Access keys", click the "Create access key" button.
    
* A page will appear for configuring the new access key.
    

![Create Access key for AWS IAM User](https://cdn.hashnode.com/res/hashnode/image/upload/v1744652284582/f6a586e9-d09e-467f-ad12-81ccf538bc34.png align="center")

In the "Access key best practices & alternatives" step, select "Command Line Interface (CLI)".

**Why should you select this option?** Choosing CLI ensures that the generated access key is optimized for use with the AWS CLI and other command-line tools (like Docker commands that push images to ECR), which is exactly what we need for our workflow.

Leave the other configurations as their default settings, and then click "Create access key".

Once the key is created, you’ll see the new Access key ID and Secret access key. Make sure to copy and store these credentials securely. They are essential for authorizing your local machine to access AWS ECR and perform operations with the permissions assigned to the `lambda-practice` user.

![Completed creation of Access key for AWS IAM User](https://cdn.hashnode.com/res/hashnode/image/upload/v1744652339772/c3d94e2a-f823-4d73-9a46-ab4d829289e9.png align="center")

### **How to Authorize Your Local PC to Publish Images to the AWS ECR Repository**

Now that we have our IAM user set up and the access keys in hand, it’s time to authenticate our local PC so we can securely push our Docker images to AWS ECR using the AWS CLI. Follow these steps:

#### Step 1: Install the AWS CLI

If you haven’t installed the AWS CLI on your machine yet, download and install it using the official guide here: [Install the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

This tool allows you to interact with your AWS account right from the command line, which is essential for pushing images to ECR.

#### Step 2: Configure Your AWS CLI Credentials

Once installed, you need to configure your AWS CLI to use the credentials associated with the `lambda-practice` user. Open your terminal and run the following command to set up a new profile named `lambda`:

```bash
aws configure --profile lambda
```

You’ll be prompted to enter the following details:

* **AWS Access Key ID:** Paste the access key ID that you generated for the `lambda-practice` user.
    
* **AWS Secret Access Key:** Paste the corresponding secret access key.
    
* **Default region name:** Enter your preferred AWS region (for example, `us-east-1` or your relevant region).
    
* **Default output format:** You can leave this as `json` or choose your preferred format.
    

This command configures a new CLI profile called `lambda` with the credentials of our IAM user.

![Authenticate and authorize AWS CLI with AWS IAM User Access key](https://cdn.hashnode.com/res/hashnode/image/upload/v1744652931837/650c93af-25f0-4d7b-a202-50d825a6b77a.png align="center")

#### Step 3: Verify the Configuration

To ensure everything is set up correctly, run:

```bash
aws sts get-caller-identity --profile lambda
```

This command will return details about the IAM user configured for the `lambda` profile, confirming that your local PC is now authenticated correctly.

Now you’re all set! Your AWS CLI is configured with the `lambda` profile, meaning your local machine has the right credentials to interact with your AWS ECR repository and push Docker images using the permissions assigned to your `lambda-practice` IAM user.

## How to Upload Your Docker Image to the AWS ECR repository ⬆️

Uploading your Docker image to AWS ECR is the moment when your hard work gets sent off to your repository so AWS Lambda can later grab and run your container. Now that your PC is authorized to talk to ECR, let’s take a look at how to upload the image.

### Step 1: Log in to ECR with Docker

Before you can push your image, you need to authenticate Docker to your AWS ECR account. You do this by running a command that gets an authentication token from AWS and pipes it to Docker. For example:

```bash
aws ecr get-login-password --region <YOUR_REGION> --profile lambda | docker login --username AWS --password-stdin <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.<YOUR_REGION>.amazonaws.com
```

Let’s break it down:

* `aws ecr get-login-password --region <YOUR_REGION> --profile lambda`: This part uses the AWS CLI to get a temporary login password for ECR. Be sure to replace `<YOUR_REGION>` with the region in which your ECR repository was created (for example, `us-east-1`).
    
* `| docker login --username AWS --password-stdin <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.<YOUR_REGION>.`[`amazonaws.com`](http://amazonaws.com): The pipe (`|`) takes the password from the AWS CLI command and passes it as input to `docker login`. The login command then logs Docker into ECR using the provided username (`AWS`) and the password. Replace `<YOUR_AWS_ACCOUNT_ID>` with your actual AWS account ID.
    

### Step 2: Environment Considerations

This command works on shell environments like Powershell, zsh, and bash.

**Windows Users (CMD)**:  
If you’re using the classic Windows Command Prompt (CMD), the piping syntax might not work the same way. In that case, you might consider using Windows PowerShell or Git Bash. Alternatively, you can run the command in an environment like Windows Subsystem for Linux (WSL).

#### Why Use the Correct Region?

It is crucial to use the exact region where your ECR repository was created. The region is a part of your repository URI. If you use the wrong region, the login will fail because it won’t find the correct repository endpoint.

#### How to Check the Region:

Log in to your AWS Console, navigate to the ECR section, and select your repository. The URI will look similar to this: `<YOUR_AWS_ACCOUNT_ID>.dkr.ecr.<YOUR_REGION>.amazonaws.com/lambda-practice`. Here, `<YOUR_REGION>` is the region you must use in your login command.

### Step 3: Build Your Docker Image with the Correct Tag

Before pushing the image to ECR, you need to build it on your local machine and tag it with your repository’s name. In your terminal, navigate to your project’s root folder (where your Dockerfile is located), then run (replace `<YOUR_AWS_ACCOUNT_ID>` and `<YOUR_REGION>` placeholders with your AWS Account ID and AWS ECR repository region):

```bash
docker build -t <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.<YOUR_REGION>.amazonaws.com/lambda-practice:latest
```

### Step 4: Push Your Docker Image to AWS ECR

Once your image is built and tagged, it’s time to push it to your remote ECR repository. Run the following command:

```bash
docker push <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.<YOUR_REGION>.amazonaws.com/lambda-practice:latest
```

This command tells Docker to upload (or “push”) your image to the repository you created earlier.

* Make sure the repository URI and tag match what you used in the build command.
    
* Remember, if you use a different region than the one in your repository URI, the push will fail because AWS won’t recognize the repository endpoint.
    

## How to Deploy the Application Container to AWS Lambda from the Image on AWS ECR 🚀

You can deploy your function on AWS Lambda in several ways, each catering to different use cases. Here’s a quick rundown:

1. **ZIP file upload:** Simply compress your code and dependencies into a ZIP file, then upload it directly via the AWS Lambda console. This traditional method is great for small codebases that don’t require custom runtimes.
    
2. **Direct editing in the console:** Write or edit your function code directly in the AWS Lambda code editor. Handy for quick tweaks, but not ideal for larger projects.
    
3. **Container image:** Package your application as a Docker container image and deploy it. This approach is particularly useful if you have complex dependencies, need a custom runtime, or want consistent environments across development and production.
    

In this tutorial, we’re taking the container image route because it offers flexibility, consistency, and scalability – all while letting us reuse our existing Docker configuration. Let’s walk through the steps for deploying your containerized application to AWS Lambda:

### Step 1: Access the AWS Lambda Console

Log into your AWS Management Console. In the search bar at the top, type "Lambda" and select the AWS Lambda service from the dropdown results.

### Step 2: Create a New Lambda Function

Once on the Lambda page, click the "Create function" button. You’ll see multiple function creation options. For our purposes, select the "Container image" option. This choice tells AWS that you’ll be deploying a containerized application instead of uploading a ZIP file.

### Step 3: Name Your Function

In the function setup screen, enter `lambda-practice` as the name of your new Lambda function. This name identifies your function in AWS.

### Step 4: Configure the Container Image

Under the “Container image” settings, click the "Browse images" button. A new window should appear, listing your available images from AWS Elastic Container Registry (ECR).

Select the repository you previously created (for instance, the one named `lambda-practice`), and pick the image tagged as `latest`.

![Create AWS Lambda function](https://cdn.hashnode.com/res/hashnode/image/upload/v1744655907615/df0e3576-5fe6-43a7-8da5-d2964b36a2af.png align="center")

![Connect AWS ECR image to AWS lambda Function](https://cdn.hashnode.com/res/hashnode/image/upload/v1744655978526/fafd6b35-579a-4439-b15e-dd5e3dba2acf.png align="center")

![Select Image from AWS ECR repository](https://cdn.hashnode.com/res/hashnode/image/upload/v1744656031049/3de3bcc1-2034-4518-acb6-84adb6136752.png align="center")

### Step 5: Finalize and Create

Now you’ll want to review the basic settings. In this step, you might also configure additional options such as memory allocation, timeout limits, and environment variables, depending on your application needs.

Once everything is set, click "Create function" to finalize the deployment.

### How to Enable Access to Your Lambda Function

Awesome – hurray, you’ve successfully deployed your image from AWS ECR to AWS Lambda! Now the next step is to make sure your function is up and running and can be triggered properly. But you might be wondering, “How do I actually access my Lambda function to see if it’s working?” Let's break it down:

#### Understanding Lambda Function Triggers

There are several ways to invoke a Lambda function, and AWS supports multiple trigger options. Here are a few:

* **Event Source Mapping:** Automatically triggers your function in response to changes in services like DynamoDB, Kinesis, or S3.
    
* **Scheduled Events:** Set up cron-like scheduled invocations via Amazon CloudWatch Events.
    
* **API Gateway:** Create RESTful APIs that call your function.
    
* **AWS SDK/CLI:** Directly invoke the function using the AWS SDK or CLI commands.
    
* **Function URLs:** A simple way to expose your function over HTTPS, giving you a public URL that users or applications can call directly.
    

In this tutorial, we’re going to use a Function URL to trigger our Lambda function via an HTTP event. This method allows you to invoke your function from the public internet and is perfect for testing or building public-facing APIs.

### How to Create a Function URL for Your Lambda Function

Now that you're on your Lambda function's details page, here’s how to create a Function URL step-by-step:

First, on your Lambda function’s page, click the "Configuration" tab at the top. Within the Configuration section, find and select the "Function URL" sub-tab. This is where you manage the public URL for your function.

Click on the "Create Function URL" button. This will open a new configuration screen for setting up your Function URL.

![Create Function URL for AWS Lambda Function](https://cdn.hashnode.com/res/hashnode/image/upload/v1744656877335/835422c5-8c88-418a-b1f2-3650360069c3.png align="center")

* **Authentication type:** Set the Auth type to NONE. This setting allows public, unauthenticated access to your function from the internet, which means anyone with the URL can invoke it. (This is great for testing or building public services, but be cautious with security in production environments!)
    
* **Additional settings:** Under the Additional Settings section, enable Configure cross-origin resource sharing (CORS). This is useful if you plan to call your function from client-side applications hosted on different domains. Think of it as opening a window for your app to communicate with other web pages or services.
    

After configuring your settings, click the appropriate button to create or save the Function URL.

![Configure AWS Function URL for AWS Lambda Function](https://cdn.hashnode.com/res/hashnode/image/upload/v1744656860868/cd98ce34-7fdf-4cb6-be85-a25d3718e2e6.png align="center")

#### Verify Your Function URL

Once configured, you’ll see the Function URL displayed on the same page. You can now copy this URL.

Paste the URL into a browser or use tools like `curl` or Postman to send an HTTP request, triggering your Lambda function and verifying that it works as expected.

You should get a response just like this on your browser:

![Deployed application on AWS Lambda](https://cdn.hashnode.com/res/hashnode/image/upload/v1744656939019/fcda2621-8057-438b-8d5a-8ac8936b6322.png align="center")

And that’s it! You’ve successfully set up a public HTTP endpoint that triggers your AWS Lambda function. Whether you're testing your deployment or building a public-facing API, the Function URL makes it easy for anyone to interact with your function.

### **Congrats — You did it!**

You've just walked through the entire journey of deploying a Node.js web server, containerized with Docker, all the way to AWS Lambda using AWS ECR as your image repository. 🚀

From writing and containerizing your Node.js application, creating an AWS ECR repository, setting up IAM users and access keys, pushing your Docker image to ECR, to deploying it on Lambda – you’ve covered it all like a pro. 💪

Not only that, but you also configured a public-facing Function URL so your serverless app can now handle requests from anywhere in the world 🌍.

You’ve just combined modern cloud-native workflows with serverless deployment – giving you flexibility, scalability, and lightning-fast response times without the headache of managing servers 😁.

👏 Give yourself a pat on the back. You’ve officially containerized and deployed your Node.js web server to AWS Lambda!

## Advantages of Adopting the Serverless Model in Businesses 💼

When it comes to deploying applications in the cloud, the serverless model has truly flipped the old playbook and has helped businesses save on Cloud costs! Let’s break it down in simple, real-world terms.

### **Cost-Efficiency 💰**

For most businesses – especially startups – serverless offers a major financial advantage. Here’s why:

In traditional models like IaaS (Infrastructure as a Service) and PaaS (Platform as a Service), such as using AWS EC2 or AWS Elastic Beanstalk, you provision resources upfront.

For example: You spin up a server with 4 GB RAM and 4 vCPUs, and AWS charges you $100/month (this covers 730 hours – the whole month). Even if your app barely does anything – say it only serves real requests for 120 hours, and uses just 1 GB of memory – you still pay the full $100, because the resources were reserved and waiting for traffic 24/7.

But with Serverless:

* You don’t pre-allocate or reserve compute power.
    
* Your application only runs when someone actually needs it (for example, when a user makes an HTTP request).
    
* You only pay for the actual execution time and the resources used.
    

For instance, if your function only runs for 50 hours in a month and uses 1.5 GB RAM, you might pay something like $30, compared to the flat $100 you'd have paid on EC2 or Elastic Beanstalk.

### **Scalability Without Stress 📈**

Serverless platforms like AWS Lambda automatically handle:

* Scaling up during high demand.
    
* Scaling down to zero when idle.
    

This means your team won’t need to predict or provision for resources during traffic surges. Whether 1 or 1 million users visit your app, the cloud provider handles the rest.

### **Simplified Operations ⚙️**

For your software team:

* No more babysitting servers, patching security updates, or worrying about load balancers.
    
* You focus purely on writing the business logic and shipping code.
    
* The cloud provider handles the infrastructure behind the scenes.
    

This frees up your team’s time, cuts maintenance tasks, and speeds up development times.

### **Better Return on Investment (ROI) 📊**

Because you only pay for what you use, the cost-to-value ratio improves significantly. Startups and businesses can:

* Launch faster.
    
* Experiment without financial risk.
    
* Scale without surprise bills.
    
* Avoid overpaying for idle resources.
    

## Disadvantages of the Serverless Model 🚫

As exciting and cost-friendly as the serverless model seems, the golden rule in tech still applies:  
every solution comes with trade-offs.

Let’s walk through a few important downsides you should consider:

### **No Built-in Support for Background Jobs ⏰**

Unlike traditional servers where you can run background processes – like sending out newsletters at midnight or cleaning up databases at scheduled times – serverless platforms such as AWS Lambda don’t natively support background tasks or recurring jobs.

For example, let’s say you wanted your app to automatically generate reports every day at 3 AM. In a typical server setup, you’d just write a cron job and call it a day.

But with Lambda or serverless, you can’t do this directly inside your deployed function. Instead, you need external tools like:

* AWS EventBridge (for scheduling and triggering Lambda functions)
    
* Or other cloud-native schedulers.
    

This adds a bit of extra setup, management, and sometimes extra cost.

### **Unpredictable Cloud Costs 💸**

One of the biggest selling points of serverless is “pay-as-you-use” – but this can also become a financial blind spot, because:

* Costs depend on traffic volume and resource usage.
    
* If your app suddenly goes viral or experiences a traffic spike, your cloud bill could skyrocket without warning.
    

For example, an app that runs stable at $30/month for low traffic could unexpectedly hit $1000+ if a marketing campaign or external event drives huge numbers of users to your service. While this means your app is succeeding, your budget might take a hit.

In contrast, with traditional models like AWS EC2 or Elastic Beanstalk, your costs are usually predictable – even if your server sits idle all month.

## When to Adopt the Serverless Model 🤔

So, is Serverless always the right choice? Not necessarily!

If you expect:

* **Steady, predictable workloads,** EC2 or Elastic Beanstalk might offer more cost certainty.
    
* **Long-running background tasks**, serverless isn’t ideal without extra services.
    
* **Real-time control over resource limits**, traditional servers give you more flexibility.
    

But if your app has burst traffic (users come and go), event-driven logic (like APIs or webhooks), or you want minimal ops overhead, then Serverless can save time, effort, and money.

### **When Serverless is the Perfect Fit: A Startup Building an Event-Driven API**

Imagine you’re running a small tech startup that just launched an app for booking fitness classes. Your team is small, budgets are tight, and traffic is unpredictable – some days you have 50 users, some days 5,000.

In this case:

* Your backend mostly handles HTTP requests: new sign-ups, class bookings, cancellations, and payments.
    
* Traffic spikes during lunch breaks and weekends, but is quiet at night.
    
* You don’t want to hire a full-time DevOps engineer just to manage servers.
    

👉 **Why Serverless is perfect in this case:**

* You only pay when people use your app.
    
* No need to manage or provision servers.
    
* AWS Lambda auto-scales based on demand.
    
* Fast to deploy, easy to connect to other AWS services (like DynamoDB for your database, S3 for images, and SES for emails).
    

By using Serverless in this case, you can save money, scale automatically, and stay laser-focused on features – not infrastructure.

### **When Serverless is Not a Good Fit: A Video Streaming Platform**

Now imagine you’re building the next YouTube-like service for a niche audience – say, education-based content for universities.

In this case:

* Your platform requires continuous background processing: encoding videos, generating thumbnails, and pushing them to CDN.
    
* Users stream content 24/7, meaning your app is always under load.
    
* Background jobs like recommendation engine updates or nightly reports need to run frequently.
    

👉 **Why Serverless might be a bad idea:**

* Functions like AWS Lambda have a timeout limit (for example 15 minutes max per execution).
    
* Continuous processing or streaming doesn’t fit the on-demand, short-lived nature of serverless.
    
* Costs could skyrocket since the app runs almost all the time, making it more expensive than a dedicated EC2 or Kubernetes cluster.
    

**Better alternative:**  
For this kind of use case, a traditional server-based setup – like EC2 or container orchestration via ECS or Kubernetes – would offer more control, predictable pricing, and support for long-running processes

✅ **Bottom line:**  
Serverless is fantastic for modern apps, but like any tool, it’s best used when its strengths match your project’s needs.

## Conclusion 📝

Congratulations on making it to the end of this tutorial! 🚀

In this article, we explored the power of serverless computing by walking step-by-step through the process of deploying a Node.js web server using Docker and AWS Lambda.

From building your container image, pushing it to AWS ECR, and finally deploying it on Lambda – you’ve now seen how easy it is to get an app running without the hassle of provisioning servers.

We also discussed the advantages of adopting the Serverless model in deploying your applications, it’s disadvantages, and real-world use cases in which you should adopt the serverless approach.

## **About the Author 👨‍💻**

Hi, I’m Prince! I’m a DevOps engineer and Cloud architect passionate about building, deploying, and managing scalable applications and sharing knowledge with the tech community.

If you enjoyed this article, you can learn more about me by exploring more of my blogs and projects on my [LinkedIn profile](https://www.linkedin.com/in/prince-onukwili-a82143233/). You can find my [LinkedIn articles here](https://www.linkedin.com/in/prince-onukwili-a82143233/details/publications/). You can also [visit my website](https://prince-onuk.vercel.app/achievements#articles) to read more of my articles as well. Let’s connect and grow together! 😊
