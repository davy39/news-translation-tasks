---
title: 'Going serverless with React and AWS Amplify: Development Environment Set up'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-22T16:31:05.000Z'
originalURL: https://freecodecamp.org/news/going-serverless-with-react-and-aws-amplify-development-environment-set-up-9b15c3363bd
coverImage: https://cdn-media-1.freecodecamp.org/images/0*B6_zkUG4Or9zIWwU
tags:
- name: AWS
  slug: aws
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Peter Mbanugo

  Serverless computing provides us with benefits such as reduced operation costs and
  development time. It allows us focus on our code to provide business value to the
  users without worrying about building and maintaining servers.

  AWS i...'
---

By Peter Mbanugo

Serverless computing provides us with benefits such as reduced operation costs and development time. It allows us focus on our code to provide business value to the users without worrying about building and maintaining servers.

AWS is one of the many providers of serverless computing services. In this post, I’ll walk you through setting up your development environment to build on AWS. This will be a primer for future posts in this series.

According to [Wikipedia](https://en.wikipedia.org/wiki/Serverless_computing), serverless computing is a cloud-computing execution model in which the cloud provider acts as the server, dynamically managing the allocation of machine resources. What this typically means is that you can single handedly build production-ready apps by focusing on coding the business logic, and leave off the task of provisioning servers, scaling or upgrading servers, and other functionalities to cloud providers or third-party service providers. You can utilise this to build nearly any type of application or backend service, and everything required to run and scale your application with high availability is handled for you.

This model of running applications provides us benefits such as reduced operational costs, reduced development time, and many more. If you’d like to read more about what serverless is and its benefits, checkout [this article on serverless architecture](https://martinfowler.com/articles/serverless.html).

### What am I going to learn reading this?

This post (and more to come in the near future) is intended to teach you how to build React applications utilising the serverless architecture and various [AWS](https://aws.amazon.com/) services. We will cover areas such as authentication, creating and consuming REST APIs, analytics, and hosting, all while utilising services from a single cloud provider. We will be working with [AWS Amplify](https://aws-amplify.github.io/), which provides CLI tools and UI component to make it easy to build serverless applications on AWS.

In this post, I’ll walk you through setting up your development environment to build on AWS.

### Getting started with AWS Amplify

[AWS Amplify](https://aws-amplify.github.io/) is a library that provides you with tools to build serverless applications. With it, integrating various AWS services with your app can be done in few lines of code. You also get UI components to accelerate development.

To use any AWS services or the Amplify library, you’ll need an AWS account. If you don’t have one, you can [sign up](https://portal.aws.amazon.com/billing/signup?redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation) now. Signing up gives you immediate access to the AWS free tier and there are no upfront charges.

### Install and configure the Amplify CLI

The Amplify CLI is a tool that allows you create and configure AWS services for your application. Its purpose is to simplify mobile and web application development for you. The CLI uses [AWS CloudFormation](https://aws.amazon.com/cloudformation/) and nested stacks, which allows you to add or modify configurations locally before you push them for execution in the cloud.

You need Node.js (version 8.11 or greater) and npm (version 5 or greater) installed to use the CLI. If you don’t have them installed, visit the [Node.js download page](https://nodejs.org/en/download/). Installing node will also give you npm, but if you have just node installed, you can also [download npm](https://www.npmjs.com/get-npm) separately.

Install the CLI by running `npm install -g @aws-amplify/cli` in the command line. Do not use yarn to install the CLI as it has known issues. Once the Amplify CLI is installed, you will have to configure it to specify the necessary AWS credentials and region. Follow the instruction below to configure the CLI.

1. Open the command line and run the command `amplify configure`. This will open the AWS Console in your browser, and if you're not signed in, you'll need to sign in to your account.
2. When you’ve signed in, go back to the command line and press Enter.
3. You’ll be prompted to select an AWS region. Select one and press Enter.
4. Then you get the option to specify the username of a new AWS IAM (Identity and Access Management) user to use with the CLI. Enter a user name and press Enter. When you press enter, it opens your browser and takes you to the IAM dashboard in the AWS Console.
5. On the IAM dashboard you’re asked to create a new user. The username field is pre-populated with the username you entered in the console, and the `Programmatic Access` access type selected. Click `Next: Permissions` button to go to the next page.
6. Leave the default selected `Administrator Access` policy and click `Next: Review` button.
7. Click `Create User` button to create the user. When the user is created, you'll be given an **Access Key ID** and a **Secret Access Key**. Keep those information because you'll need it to set up the CLI.
8. Go back to the command line and press Enter.
9. It’ll prompt you for the **Access Key ID**. Copy and paste the value then press Enter.
10. Another prompt shows asking for the **Secret Access Key**. Copy and paste the value then press Enter.
11. Now you’ll be asked if you want to create or update the AWS profile in your local machine. We’ll be using default for this profile. Press Enter to select the default and create your AWS profile.

![Image](https://cdn-media-1.freecodecamp.org/images/WQsdAH5XMIvZzw5gD2DfjVbP2EOQhtISKCe3)

### Create the React app

Now that the Amplify CLI has been configured, we can begin creating the React app. We will bootstrap the React app with [Create React App](https://github.com/facebookincubator/create-react-app). This allows us focus on writing code and not worry about setting up Babel and Webpack because they’ll preconfigured for us. To create the React project, run the following command:

```
$ npx create-react-app serverless-react
```

This creates a folder `serverless-react` with necessary files for a react app. Next thing to do is to initialise an Amplify project. To do this, follow the instructions below

1. Switch directory to the project by running `cd serverless-react` in the command line
2. Run the command `amplify init`. This will prompt you to answer some questions.
3. Select your code editor and press Enter.
4. The next set of prompts presents you with questions to determine the type of app you’re building. Select JavaScript, then React, and then press Enter for the remaining prompts to use the default values.

![Image](https://cdn-media-1.freecodecamp.org/images/-No7PaAGFPBfb4jGZDHL5zkU5aYRKs7FwmEn)

The `amplify init` command sets up deployment resources in the cloud with CloudFormation stacks, and prepares the project for Amplify. It pulls configuration details of the resources into the project directory. This configuration information will be used to add AWS services to the project and update service configuration. At the root of the project directory, you'll find a `.amplifyrc` file and a **amplify** folder. They contain CloudFormation configuration information for resources we'll be using.

The final bit we need to set up the project is to add the Amplify library to our project. The library provides us with modules and UI component that makes it easy to integrate AWS services in few lines of code. Run the following command to install it from npm.

```
$ npm install -S aws-amplify && npm install -S aws-amplify-react
```

### That’s A Wrap

Serverless computing provides us with benefits such as reduced operation costs and development time. It allows us focus on our code to provide business value to the users without worrying about building and maintaining servers.

AWS is one of the many providers of serverless computing services. It takes a couple of steps to configure and integrate these services, and AWS Amplify was built to make it easier to build serverless applications on AWS. It provides tools to create and configure services with a few commands, and library components to easily interact with those services from our code.

This is the first post in a series to introduce you to building serverless applications with AWS Amplify. We set up the Amplify CLI and created an Amplify project.

