---
title: How to Host Static Sites on Azure Static Web Apps for Free
subtitle: ''
author: Shrijal Acharya
co_authors: []
series: null
date: '2024-06-18T10:59:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-host-static-sites-on-azure-static-web-apps
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/host_static_sites_swa_azure.png
tags:
- name: Azure
  slug: azure
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: "In this article, I will show you how you can host your React/Next.js app\
  \ or any static web app on Azure Static Web Apps. \nI will be showing you both ways\
  \ of doing it – through the GUI and with the CLI.\nI assume you already have built\
  \ a project and op..."
---

In this article, I will show you how you can host your React/Next.js app or any static web app on Azure Static Web Apps. 

I will be showing you both ways of doing it – through the GUI and with the CLI.

I assume you already have built a project and optionally pushed it to GitHub or any other alternative, like GitLab or Bitbucket.

It's time to go live with your project and showcase it to the world. 💪 

Whether it is your first time working with Azure or you are already a champ, feel free to follow along. 

## What is CI/CD?



Before we dive into Azure Static Web App, let me give you a brief overview of what CI/CD is.

Imagine you're building your cool new web app. Now, to make sure it's always up-to-date and running, you need something called Continuous Integration/Continuous Deployment (CI/CD). 

Here's how it works:

* **Continuous Integration (CI)** is the process of automatically building and testing your code whenever you make changes and ensuring it is working as you expect.
* **Continuous Deployment (CD)** is the process of automatically deploying your tested code to production.

You might have already came across CI/CD if you've ever hosted your project on Vercel, Netlify, or any other site hosting platform, and noticed that once you push your local changes to your remote repository, those changes are reflected on the original hosted site in just a few minutes. Magic, huh? This is all possible with the help of CI/CD.

In short, CI/CD ensures that your project is tested and deployed whenever you push new commits to the repository hosting your project.

## How to Push your Project to GitHub

In this step, I will use GitHub as an example. If your project is already pushed to GitHub, feel free to skip this step. Otherwise, follow the steps shown below.

### Log in to GitHub CLI

Did you know you can create a GitHub repository right from your command line?

Let's get started. Firstly, make sure you have GitHub CLI installed. For installation instructions, follow the steps shown [here](https://github.com/cli/cli/blob/trunk/docs/install_linux.md).

To authenticate your GitHub CLI to your account, run the below command:

```bash
gh auth login
```

Follow the steps displayed in your terminal to authenticate with GitHub. Once done, you can proceed to the next step.

### Create a repository

Once you're logged in, you can run the below command to start an interactive repository creation mode:

```bash
gh repo create
```

Or, directly specify flags to it like so:

```bash
gh repo create <repository_name> --public --license mit --description <repository_description>
```

Running, this command will create a repository with all the specified options in your GitHub account.

### Push your changes

Now, that you have already authenticated yourself and have created a repository in your GitHub account, it's time to push your local changes to the remote repository.

Run the following commands to push your local changes to the remote:

```bash
git branch -M main
git remote add origin https://github.com/<username>/<repository_name>.git
git push -u origin main
```

Note that if you have SSH authentication set up, you need to make sure you change the origin URL to follow SSH protocol.

That concludes the initial preparation. Now, let's proceed with creating the Azure Static Web App. 🚀

## Host your project with Azure SWA CLI

In this section, you'll learn how to host your static project, whether it built with Next.js, React, or any other static site, using Azure SWA CLI.

First, you need to install the `@azure/static-web-apps-cli` package as a dev dependency. 

If using `pnpm` as a package manager, run the below command. The command might vary based on different package managers.

```bash
pnpm install -g @azure/static-web-apps-cli
```

Now, build your project with the appropriate build command:

```bash
pnpm run build
```

It's time to deploy the application with the build folder. Run the below command to deploy it to Azure SWA:

```bash
swa deploy <build_location> --env production
```

If your application uses an API, then you need to pass the `api` folder location as a flag to the above command. So, your final command would be:

```bash
swa deploy <build_location> --api-location <api_folder_location> --env production
```

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Untitled-design-5-.png)
_Deploying the project with Azure Static Web App CLI._

That is it. Your site is deployed to Azure Static Web App through CLI. 🎉 You can view it in the shown URL. 

There are further configuration which can be specified. For additional configuration, follow this [link](https://learn.microsoft.com/en-us/azure/static-web-apps/static-web-apps-cli-configuration).

## How to Host your project with Azure Portal GUI

In this section, we will create another brand new Azure SWA through the Azure portal.

Head over to the Azure portal at [https://portal.azure.com](https://portal.azure.com) and search for the Azure Static Web App.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-from-2024-06-15-16-24-56.png)
_Azure portal search results for Static Web App._

 Hit "Create" and you should be asked with a bunch of extra configurations.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Untitled-design-1-.png)
_Creating a new Azure Static Web App._

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-15-at-16-39-09-Microsoft-Azure.png)
_Setting up the configurations for the Azure Static Web App._

For the Resource Group, create one and name it whatever you want. Also, give your web application a name.

If your project is hosted on GitHub, choose GitHub as the option and choose the repository from the dropdown menu. For the branch, select 'main' if you created the project from scratch with default settings.

If you are using any other alternatives, then select the one which satisfies your criteria.

Leave everything else as default and click on "Review + create" and wait till it is done hosting your project to Azure SWA.

In the Overview section of the app, you should see URL for your built project. Here is the overview of mine:

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Untitled-design-2-.png)
_Azure Static Web App dashboard overview._

Visit the URL and you should have your site ready. 🥳

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-84.png)
_Deployed project hero section._

## Wrapping Up

By now, you should have a general idea of how to host any static web app in Azure Static Web Apps.

While we could cover additional topics like adding a custom domain to our site, this may not apply to most of you, so I'm not including the steps in this article. To learn more, visit this [link](https://learn.microsoft.com/en-us/azure/static-web-apps/custom-domain-external).

So, that is it for this article. Thank you so much for reading! See you next time. 🫡

Now that you've had a sneak peek at my portfolio in the image above, why not get in touch? 😉 Feel free to connect with me here:

* **GitHub**: [https://github.com/shricodev](https://github.com/shricodev)
* **LinkedIn**: [https://linkedin.com/in/iamshrijal](https://linkedin.com/in/iamshrijal)
* **Twitter**: [https://twitter.com/shricodev](https://twitter.com/shricodev)

