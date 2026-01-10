---
title: How to Deploy Your Node.js App on Azure
subtitle: ''
author: Oluwatobi
co_authors: []
series: null
date: '2024-07-17T11:56:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-node-js-app-on-azure
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/awsP.jpg
tags:
- name: Azure
  slug: azure
- name: node
  slug: node
- name: Web Hosting
  slug: web-hosting
seo_title: null
seo_desc: "The advent of cloud computing marked a turning point in the field of technology.\
  \ It provides easier access for users across the globe to web and mobile applications\
  \ and services. \nModern-day computing services also provide a wide range of features\
  \ wh..."
---

The advent of cloud computing marked a turning point in the field of technology. It provides easier access for users across the globe to web and mobile applications and services. 

Modern-day computing services also provide a wide range of features which make web apps easier to use and more efficient. So it's important for developers to have a basic understanding of how the cloud works.

This article is a beginner's guide to deploying backend applications to the cloud. We'll use the Azure platform as our cloud infrastructure and Node.js/Express for the backend web application. Before we go on, here are a few requirements:

* Basic understanding of cloud computing (you can check out [this article](https://dev.to/oluwatobi2001/introduction-to-cloud-computing-the-models-benefits-risks-implementation-and-popular-tools-2loh) to learn more about that).
* Knowledge of JavaScript.
* VS Code.

With that, let's get started.

## Introduction to Azure

Azure is a cloud computing platform developed by Microsoft that acts as a server for deploying and hosting web applications, databases, file storage, and so on. 

Compared to other cloud computing services, it is quite beginner-friendly and has an actively growing user base. Let’s explore the Azure portal.

## How to Set Up Azure Account

Signing up on the Azure platform is the first step to hosting your application.   First, navigate to [the website](https://azure.microsoft.com/en-us/get-started/azure-portal) and complete the signup process.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-36.png)
_Azure sign in page_



After signing up, you'll have access to the management console of the Azure application where all our activities can be carried out.

Before we go on, here are some of the services we'll be getting familiar with on this platform.

* Azure Resource groups
* Azure app services
* Storage accounts
* SQL databases
* Virtual networks

![Image](https://www.freecodecamp.org/news/content/images/2024/07/serc3.PNG)
_Azure services_

Congratulations on successfully creating your Azure account.

## Deployment Options on Azure

As a cloud computing platform, Azure boasts of its wide versatility. Depending on your skill level or preference, you can deploy web applications to Azure via the following options:

* Azure CLI
* Azure Virtual machines
* Azure Functions
* Azure Kubernetes Service
* Azure Storage.
* Azure DevOps
* Azure portal service

We'll utilize the Azure portal service for this tutorial and use its VS Code integration to deploy a simple Node.js application to the Azure cloud.

## How to Set Up the Backend Application

We'll create our web application using Node.js via the command line and Visual Studio Code.

Firstly, navigate to the folder where your app will be created and initialize a Node project by executing `npm init`

Next, initialize the app by installing the `Express` framework. This can be done via `npm i express`. 

Go on and paste the sample code for this tutorial:

```
const express = require("express");
const app = express();

app.use(express.json());

app.get("/", (req, res) => {
    res.send("Hello, World");
});

app.listen(process.env.PORT || 5000, () => {
    console.log("Server is running on port " + (process.env.PORT || 5000));
});


```

The code above outputs `Hello World` whenever it is executed.

## Application Deployment

The backend code we wrote in the preceding paragraph will be deployed to Azure via the use of Azure’s VS Code extension.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/webVs.PNG)
_VS Code homepage_

Navigate to the Extensions tab, search for Azure App Services and install the extension. On successful installation, an Azure widget will appear on your taskbar where you can sign in to the Azure cloud.  


![Image](https://www.freecodecamp.org/news/content/images/2024/07/azure-app-service.PNG)
_Extensions marketplace_

  
Subsequently, we'll be creating a cloud-based web application in which our Node.js code will later be deployed.

On the Azure resources tab, clicking the `plus` icon will display a drop-down menu where various development options can be seen. We'll be clicking on the Azure app services option.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/res-1.png)
_Azure drop down menu_

  
After clicking that, a prompt will pop up asking for a unique name for the cloud application. In my case, I went with newApp777.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/newa7.PNG)
_creating a web application_

However, you can use any other name you so wish. Subsequently, you will need to select the backend language of your choice. Any version of Node.js will be compatible with our application.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/newStack.PNG)
_web stacks available_

Also, the F1 service option will be used for this tutorial. However, you can pick anyone you so desire.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/newTier.PNG)
_Various Azure tiers_

On successful completion, your application will be created on the Azure portal.

  
Now to the crux of the matter. Let's install our Node.js code on this web application. 

We'll click on the code folder which provides us with options to automatically deploy our code to an Azure web app service.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/image-35.png)
_Deployment dropdown menu_

As soon as this is done, the list of the cloud servers on your Azure account will be shown. You can then select the new app we just created.  


![Image](https://www.freecodecamp.org/news/content/images/2024/07/sear.PNG)
_app deployment_

  
Your backend code should then be deployed on the NewApp cloud server we created. On successful completion, you'll receive a success message with a link to your cloud application.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/pro.PNG)
_command prompt interface_

Congratulations, you have successfully hosted your first web application. Navigate [here](https://newapp777.azurewebsites.net/) to see the hosted application.

![Azure app](https://www.freecodecamp.org/news/content/images/2024/07/wevpage.PNG)
_The application webpage_

## Additional Information

So far, we have covered the basics of deploying an application via the use of VS code extensions on Azure portal services. As you progress in the field of cloud computing, other interesting fields can also be explored such as:

* App monitoring with Azure Monitor.
* Azure app networking essentials.
* Azure MySQL database integration.
* Node JS serverless functions deployment.

You can also interact with me on my blog and check out my other articles [here](https://linktr.ee/tobilyn77). Till next time, keep on coding!

