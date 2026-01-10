---
title: How to Standardize Your Development Environment with devcontainer.json
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-10-04T14:45:34.000Z'
originalURL: https://freecodecamp.org/news/standardize-development-environment-with-devcontainers
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/image--9-.png
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
seo_title: null
seo_desc: "By Hrittik Roy\nModern software development workflows are complicated,\
  \ involving many tools and dependencies. \nWhen working in a team, it's not uncommon\
  \ to use several different software programs, each with its own dependencies. This\
  \ can quickly becom..."
---

By Hrittik Roy

Modern software development workflows are complicated, involving many tools and dependencies. 

When working in a team, it's not uncommon to use several different software programs, each with its own dependencies. This can quickly become confusing, with each software requiring different configurations and management. 

One solution is to use virtual environments to isolate the dependencies. This can still require you to install and manage the installation and configuration. 

But there's another better option: packaging everything – including the database and coding language version – into one container that you can use whenever you need it. In fact, most companies deploy their logic and applications into production containers.

For development, you can use a Docker container as a fully-featured development environment. It's similar to your production environment, but with all the compilers, debuggers, build tools, SDKs, productivity tools, and others. That would be your development container or dev container.

Here `devcontainer.json` comes as the standard that streamlines and standardizes your development environment. It lets you focus on shipping changes rather than worrying about dependencies and installations. 

In this tutorial, you will learn about the devcontainer.json standard, its purpose, how to configure it, and how to adopt it for your personal or business use. It'll help you boost your productivity as an engineer.

## What's a Dev Container?

Dev containers, also known as development containers, provide a complete development environment packed within a container that can be easily accessed through your preferred IDE via Secured Shell (SSH). This setup eliminates any obstacles that impede your workflow, ranging from low performance to less bandwidth.

Your container can operate on various infrastructures, including private and public clouds, clusters, or local machines, and you can leverage the hardware that would be challenging to replicate on your own.

The isolation aspect also ensures that your dependencies do not overlap and disrupt your local environment. All container configuration is stored in a standard `.devcontainer.json` file, from Microsoft, which serves as the packaging instructions for your environment. 

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-2.png)
_Dev Container Structure. From: [containers.dev](https://containers.dev/overview)_

The file uses a structured JSON with Comments (jsonc) metadata format which you can tailor to your specific needs. For example, you can add developer tools like git, a debugger, and other configurations like various extensions.

### Where can you use it? 

The simplest setup can be to create a basic container environment with a language to experiment with different features. For instance, if you wish to test a new edition of a programming language, you can utilize the base image of that particular language and generate a new development environment with ease.

There are a few use cases for complicated setups as well. For example, one of the most difficult tasks is often creating and configuring a database to work seamlessly with your project while setting up your dev environment.

By creating a Docker compose file, you can easily configure the creation of the database and expose environment variables to create a self-contained environment. These orchestrated multi-container setups (with both the database and programming language) are installed as a parent-child relationship and can serve complex use cases.

Look at the below configuration as an example which uses Compose to connect the build space:

```json
{
"name": "Python 3 & PostgreSQL",
"dockerComposeFile": "docker-compose.yml",
"service": "app",
"workspaceFolder": "/workspaces/${localWorkspaceFolderBasename}"
}
```

In this example, your Dev Container uses a Docker Compose file and references the instructions to build a Python and PostgreSQL integrated workspace. The structure can help develop CRUD applications without trying to configure your database and system configuration to support it across every developer.

## The Problems Dev Containers Solve

Now with features like these, dev containers are gaining popularity in personal and business settings because they offer reproducibility and isolation. Let's take a look at all the advantages:

### Addressing setup configuration issues

Maintaining and managing local environments can be a lot of work. It often involves using various tools and configurations, making the process cumbersome. Having something that standardizes this process can save a lot of time.

### Standardizing build instructions of the project

Writing documentation for dependency upgrades and changes can be challenging. A better approach would be to use code to simplify the process, allowing anyone to ship without being bogged down by documentation or "it works on my machine".

### Ensuring isolation of development environments

A software developer can simultaneously work on different projects with many moving parts. What if you can isolate environments, preventing conflicts with other software on the host system and providing a clean, controlled environment for development? It’s now possible :) 

### Enabling consistency across development teams

Achieving portability across multiple teams and individuals is complicated with varied technology and configurations. A standardized development environment may ensure that all team members have a uniform configuration while decreasing inconsistencies caused by individual machine variances.

### Simplifying onboarding and training processes

Learning new things is important, but can be challenging. So what better way to learn than by practicing a new language or framework? Launching environments quickly in isolation can help keep machines clean. 

This is especially true when presenting talks or running workshops. Starting with a clean slate, everyone can follow along without getting bogged down by missing tools or mid-step confusion.

## How to Create Your First Devcontainer

Now that you know all the benefits, I'll help you create your first development container. As this is an introductory tutorial, you'll learn how to do it for a basic Go environment.

Once you have a grasp of the fundamentals, you can expand your setup to include more complex configurations that involve databases, additional developer tools, and customization. Let's get started with creating one!

### Prerequisites 

Here are the prerequisites for creating the template: 

1. Tools for running Dev Container: [Docker](https://www.docker.com/) or any other container engine
2. Tools for creating templates and connecting to Dev Container: [Visual Studio Code](https://code.visualstudio.com/)
3. Tools for managing connection and creation logic: [Visual Studio Code Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

Note: After creating the template, you can switch to your preferred IDE with different backends, as we’ll see in upcoming sections. Just think of the `.devcontainer.json` file as a source of truth for the environment and can be easily shared.

### How to build a simple dev container

You can either create the dev container from scratch or use the VSCode utility. Starting with the utility is simple. To get your dev container set up, just use the `Dev Containers: Add Dev Container Configuration Files…` option from the Command Palette `(Ctrl+Shift+P)`:

![Image](https://lh3.googleusercontent.com/KcLU2UhZfNoxHiKs9wdUBeEVrJGvOviHYrNXlWgqdSq8D1afGSzr_TCnrmwsuTgH4Zm58e_MomNp3i_4LRKnxC6ppJ4v-p2A_mvokmVnk1JSJg_f7hsuZY9cTpn-UjY2gHjdWxA696Fy-bgFnlWheOg)
_Sample Configuration for Dev Containers from VSCode Command Palette_

Now, let's move on to the next step, which is selecting the base image. You can choose any base image that you like. In this case, we're using the Go base image.

![Image](https://lh5.googleusercontent.com/sgFvvnhlbN_nt8eQpk19ZGlWxZ5Dk3TK-nAXAZAdGw314fHKKEz5RkG8WXyxCKRO5x9VHyjtuyNH_-q7Vev2Ue4bszdKm8uACtAnFPFDPZmJiM0zMYZAQazLzvJJaRN4u1A8ItAnwODEOYwaCwjONa4)
_Base Dev Container Configuration_

However, there can be a lot of versions of Go – so the next step is to choose the one you want. The latest version available is `1.21`, so I recommend using that one. But if you prefer, you can also build an image from scratch or even select from older versions.

Just scroll down and take your pick.

![Image](https://lh5.googleusercontent.com/Hkg2vqYKxnuBn6A31LrVvETkND4_S0JUsIHqStVzZaKZz-1LtVnKZEAAdtA_BfX2CvHIW6e9-P8PPQObb3B1b2C3SrYjmSWw_st8Wm2ihbuU0efRfHMLy9ynjbnaulrY0aEsNAHw1Fb21NS_lhKzEWk)
_Version of the selected base configuration file_

The next step is to import "Features", which are self-contained units of installation code that help induce specific tools or containers into your dev container configuration. These features can range from new tools to specific customizations which you can learn more about [here](https://containers.dev/features). 

But for a basic and simple Go environment, we will skip this step.

![Image](https://lh4.googleusercontent.com/YXO8ZA_kH95z7OMTkrYmLz8VMenqCdlyUFpDl2uoRfJdrtvSLFtH-QouD1gToeLrye8MDRFGzGDaQy3yhXujAiC43LKb-TvctMmxWbLqaSwde2U-XlVSdYgexohqkp5Ho_ft7UgkqkPBvvrDx6eN8Fg)
_Complimentary Features that can boost your workspace_

Click on `Ok` to generate a basic Go `.devcontainer.json` file in the `.devcontainer` directory: 

```bash
~/Code/devcontainer-new main +4 !4 ❯ tree -a
.
├── .devcontainer
│   └── devcontainer.json
```

Congrats! Now you have an environment that is isolated and can be shared with anyone. 

### How to use VSCode for dev container setup

To run this configuration, you can click on `Reopen in Container` as the simplest way as seen below:

![Image](https://lh5.googleusercontent.com/Ndj5FXh3EE09Ab_srEQH7lSQ35yDfQwLWBeJPQQMmx_JDZPVnQOZsCH-jZdTJ_ZXOfTRyc95fzhBPmPSZefUs7O3pT19xi3-FRcxlvtSBsMx5JHNN3hR6jCwPHAz_2BTr-oTzqjp9E4YvHiRAehVlUg)
_A sample Dev Container file with Go 1.21_

The extension will pull the image "_mcr.microsoft.com/devcontainers/go:1-1.21-bullseye_" and then create an SSH server in it. 

![Image](https://lh5.googleusercontent.com/NKkI-1yuc-HjQ53zmc2EfxT4zPbjSRf9r7uXSt3IVm2w7WeCLT5v9wwUJPdzIPO_0VT4tluONMOJowZeeQCa2iEZudAPJ_e2H9rchPVfFI5LkspnfT4uTAhU2LwcAangC1EXF0ff1mli5c4nYQyFMYk)
_Starting Dev Container_

After successfully building the Go version, you can confidently SSH into the environment and execute your operations. You'll see that the Go version is the same as the one you built and the connection comes from your Dev Container, which makes the connection successful: 

![Image](https://lh4.googleusercontent.com/wbxcN6fkTVxkVkn0UftnN2IsdZK79NJ32vSiLTCSlcJrX2woQjZvSjiIYl1Ynoxuil1GDPZ7SZkxYrjzEYWYCZG-Wcq6rEt7rbtB0oJujz8IZJcc5WwYYhGEZtZsXJz4gNEeJVFV8bx0MRKfzE5DP7g)
_Dev Container running locally_

### Dev Container CLI 

[Devcontainers CLI](https://github.com/devcontainers/cli) is a command line interface that helps you execute, build, and run the container from your devcontainer configuration.  

With the help of this tool, you can set up an environment without using VSCode and then connect to it manually through SSH, giving you more freedom.

Although the tool is interesting, many features have yet to be launched as listed here: 

![Image](https://lh4.googleusercontent.com/YT7slbodThp_21lmmxyzafvWP7atDEn_6lrGTotxdWsF9idTfob0nnu_517dLHizjv9tEeehkzASWF1pPrQehYPf05tSDNDZONUajVhsEGsV93vofapIhZFG9V-v3afR1Qb6Oa-Axk8ZZk6wC1CErx0)
_Feature Roadmap_

## How to Use Dev Containers to it’s Full Potential 

Once you distribute the `devcontainer.json` to your teammates, they can easily use it to launch local environments with the discussed benefits. But what if you need to help them launch the environment on the Cloud to leverage its powerful hardware?

There are a few options that can help you. The first one is [GitHub Codespaces](https://github.com/codespaces), which helps you launch on infrastructure managed by GitHub on Azure. 

But there may be a requirement for using dedicated hardware from your Kubernetes cluster, or private or public cloud. How do you do it? You can use open source client-side tools like [DevPod](https://devpod.sh/), which helps you deploy on your desired infrastructure.

![Image](https://lh5.googleusercontent.com/_nKg6h4V7em9ZORxwFUVuWpgWxAmRLSfv2lWWm6JpSoJBDXDw56bjNfBhmxWtnpb8kGAgbvkZTn4kOo4oouV2vU7ypm-m5H1H9OROlaWESPtJ4SskfXwxSz3n9rO0LA7DgU98EvKaJ0H0CZ4wooSPww)
_DevPod UI_

Currently, the tool has over [4.4k stars](https://www.freecodecamp.org/news/p/43b21e57-00ca-4850-9a0f-95ebce575227/(%E2%80%8B%E2%80%8Bhttps://github.com/loft-sh/devpod) and has been growing rapidly with more traction every day with a moto of `_Giving the power to the user. Any Infra, any IDE, and Unopinionated_`:

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-4.png)
_GitHub growth History - DevPod_

The tool is unopinionated, which means that you can use it seamlessly across various infrastructures, IDEs, and programming languages. 

For example, if you want a specific backend on a cloud provider, you can do it with providers that are already available, or you can [create your own like the 7 community providers](https://devpod.sh/docs/developing-providers/quickstart):

![Image](https://lh3.googleusercontent.com/4WvTAJUH_qOmcuGSyDQnGKf4ZDpjQ7um2SwhUAfhaFTPSK5SMwUY0TV1JuSrYXKyyUl7fQvOONHbem1puJ6ohxYn2n_1tCnrHobieQRjlkZ_FupqBobTnD8s3z0nPaVuh2CWsWHygqO27Aatas25R_c)
_DevPod Providers_

The tool also allows for a consistent development environment that can be relied on repeatedly anywhere you want and connected to any code editor/IDE ranging from JetBrains, Jupyter, or VSCode. 

## How to Launch Your Development Evironment using DevPod

This tool offers both a desktop and CLI version, so you can use whichever suits you better. When using DevPod Desktop to create an environment, the process is as follows:

Step 1: Install DevPod from the [official instructions](https://devpod.sh/docs/getting-started/install). 

Step 2: Add a provider via 'Providers' > '+ Add'. Select a provider and select 'Continue'.

![Image](https://lh4.googleusercontent.com/CfrbpPmbH6X4H3SWDLVbc0ujGBakXbGKIauhv-YJ7nNQY6ISnhpU9cJqDzVjR6ylwBvaQ88bbUQSLMKaDG1KKu1B9Ezz_1-nUiZ6fGfqDRuy4X0ju9NTK_gbZvwUgdF3GUEJBgz6pdbiKx9lXzOxfuk)
_DevPod AWS Provider_

Step 3: `Enter Workspace Source` with your `devcontainer.json` path which can be a remote or local repository or the sample:

![Image](https://lh4.googleusercontent.com/B-ovwU1mYLxJu5_ANnbP_-dHKUOgMBa4hFiHUt2QEt6suJYGKV-I5M2YJ5wX714AFYNhzib0UOsMesL1t0XJzoordevJ4En91iVpDDzNcIRcHZrsme7qWwB7BzemNzMyPzppy6I0iRGlOn-9YY8ZYgI)
_IDE and Provider Selection_

Step 4: Select your default IDE and click on `Create Workspace`:

![Image](https://lh3.googleusercontent.com/-etuLcx-G3VOHAwbNoPdcO9PWPiNu-KF3Z6NR0qq3vji5o7FCeDoJqywprmKo7yOmAlv4FV-JrRbopfXEjmK_CqyF0EmPT1zo8xZkfGmj7b0wz-chmyZgACh7Tz2qLxe1TJ2lcs6FJ1wAV0Jpih976s)
_Create Workspace_

Now, you can build and configure your application on your running instance:

![Image](https://lh3.googleusercontent.com/FWJpNnACbxTFA3BDD162oIploPPdBUQgYuaNu6dvoqAJEadvdUf5Ep5v_dMBEShFfj6lll085xLxVPpH-bte5tHLX8q2av42JDol9K_i3fnel5LuNR8GVYqHocHIsfFOMtPs1td_XvcWQJksiycanNA)
_Dev Container Running on your Local Machine_

Congratulations! You've successfully set up your first Dev Container 🎉

If you're feeling adventurous and want to explore the CLI, you can find out more about how to use it right [here](https://devpod.sh/docs/developing-in-workspaces/connect-to-a-workspace).

## Final Thoughts

Standards like dev containers help you improve your productivity and your overall development ecosystem. This reduces costs for companies as the latest hardware can be provisioned without requiring the entire team to upgrade their local machines every two years.

It also helps you effortlessly onboard new team members and maintain a consistent user experience. 

Development Container tools like DevPod can improve security and customization to cater to varying needs on any infrastructure you want while maintaining a consistent [DevEx](https://loft.sh/blog/why-every-software-team-should-have-a-developer-experience-owner-dxo/). This allows for faster building and testing using the latest hardware and replaces onboarding time with coding time.

You can join the DevPod [Slack](https://slack.loft.sh/) to learn more.  

