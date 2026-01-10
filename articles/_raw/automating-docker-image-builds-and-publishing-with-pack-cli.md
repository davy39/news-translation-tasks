---
title: How to Automate Docker Image Building and Publishing with Pack CLI and GitHub
  Actions
subtitle: ''
author: Destiny Erhabor
co_authors: []
series: null
date: '2023-07-12T21:55:00.000Z'
originalURL: https://freecodecamp.org/news/automating-docker-image-builds-and-publishing-with-pack-cli
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/pexels-jiyoung-kim-4513940.jpg
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: GitHub Actions
  slug: github-actions
seo_title: null
seo_desc: Building and publishing Docker images is a crucial aspect of modern software
  development. The traditional approach often involves writing complex Dockerfiles
  and managing dependencies. But in this tutorial post, I'll show you a simpler way
  that uses ...
---

Building and publishing Docker images is a crucial aspect of modern software development. The traditional approach often involves writing complex Dockerfiles and managing dependencies. But in this tutorial post, I'll show you a simpler way that uses the Pack CLI.

PackCLI leverages Cloud Native Buildpacks to transform your application source code into images that can run on any cloud. They are typically responsible for a language component, toolchain, or app component, such as Python, pip, or a web server. You can learn more from their [website.](https://buildpacks.io/)

In this article we will walk through a step-by-step GitHub workflow to build a Docker image for a personal portfolio application and publish it to Docker Hub using this power tool.

## Table Of Contents

* [Prerequisites](#heading-prerequisites)
* [How to Create the Workflow](#heading-how-to-create-the-workflow)
* [Workflow Breakdown](#heading-workflow-breakdown)
* [Full Workflow](#heading-full-workflow)
* [Conclusion](#heading-conclusion)

## Prerequisites

Before diving into the workflow, make sure you have the following prerequisites:

* **Docker**: Although optional for local builds, having Docker installed is recommended.
* **Pack CLI**: This tool is essential for local builds and can be installed from the official documentation.
* **Docker Hub Account**: You'll need an authenticated Docker Hub account to publish the images.
* **GitHub Account**: The workflow will be triggered by actions on GitHub.

**Before you begin**: To follow along with the example GitHub workflow, make sure you have cloned the [personal_website](https://github.com/Caesarsage/personal_website.git) repository. You can also use any other project you want to build the image and publish it to Docker Hub.

Now let's get started with our workflow:

## How to Create the Workflow

To simplify the process of building and publishing Docker images, we will utilize Pack CLI and a powerful workflow on GitHub. 

This workflow eliminates the need for writing complex Dockerfiles and streamlines the image building process. 

## Workflow breakdown

Here's a breakdown of the workflow:

### Trigger the workflow:

```yaml
on:
  push:
    branches:
      - main
  pull_request_target:
    branches:
      - main
```

The workflow is triggered whenever there is a push to the main branch or a pull request to the main branch. You can customize the trigger conditions based on your specific requirements.

### Define environment variables:

```yaml
env:
  BUILDER: "heroku/builder:22"
  IMG_NAME: 'personal-portfolio'
  USERNAME: "caesarsage"
```

This section defines the environment variables that will be used throughout the workflow. 

The `BUILDER` variable specifies the Docker image that will be used to build the application. The `IMG_NAME` variable specifies the name of the Docker image that will be built and published. The `USERNAME` variable specifies your Docker Hub username.

### Check out the repository:

```yaml
jobs:
  version:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
```

This section defines a job called "version" that runs on an Ubuntu environment. The `actions/checkout@v2` action is used to check out the code from the GitHub repository. This step allows us to access the application source code for building the Docker image.

### Set the app name:

```yaml
dockerhub_remote_build:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v2
        
    - name: Set App Name
      run: 'echo "IMG_NAME=$(echo ${USERNAME})/$(echo ${IMG_NAME})" >> $GITHUB_ENV'
```

This section sets the `IMG_NAME` environment variable, which includes the Docker Hub username and the desired image name. 

The `dockerhub_remote_build` job runs on an Ubuntu environment and uses the `actions/checkout@v2` action to check out the code. The `run` step sets the `IMG_NAME` variable using the provided Docker Hub username and image name.

### Log in to Docker Hub:

```yaml
- name: login
  uses: docker/login-action@v1
  with:
    username: ${{ env.USERNAME }}
    password: ${{ secrets.DOCKER_PASSWORD }}
```

This step logs in to Docker Hub using the provided Docker Hub username and password. 

The `docker/login-action@v1` action is used to authenticate the workflow with Docker Hub. The Docker Hub username is taken from the `env.USERNAME` variable, and the password is stored securely in the repository secrets.

### Build the Docker Image with Pack CLI:

```yaml
- name: Pack Remote Build
  uses: dfreilich/pack-action@v2.1.1
  with:
    args: 'build ${{ env.IMG_NAME }} --builder ${{ env.BUILDER }} --publish'
```

Here comes the main part of the workflow. This step utilizes the `dfreilich/pack-action@v2.1.1` action, which is a GitHub Action for running Pack CLI commands. 

The `args` parameter specifies the Pack CLI command to build the Docker image. The `env.IMG_NAME` variable is used to specify the image name, and the `env.BUILDER` variable defines the builder image to use. The `--publish` flag instructs Pack CLI to publish the built image to Docker Hub.

### Test the app:

```yaml
- name: Test App
  run: |
    docker run -d -p 8080:8080 --name personal-portfolio ${{ env.IMG_NAME }}
    sleep 30s
    curl --request GET --url http://localhost:8080
```

This step runs the Docker image that was built and published in the previous step. 

It starts the container in detached mode (`-d` flag) and maps port 8080 of the host to port 8080 of the container. Then, it waits for 30 seconds (`sleep 30s`) to allow the application to start. Finally, it performs a simple HTTP GET request to the application using `curl` to test if it is working as expected.

### Rebase the Docker image:

```yaml
- name: Pack Rebase
  uses: dfreilich/pack-action@v2.1.1
  with:
    args: 'rebase ${{ env.IMG_NAME }}'
```

To ensure that the Docker image is reproducible and upgradable, this step uses the Pack CLI `rebase` command to rebase the image. 

This process helps incorporate any changes or updates that might have occurred in the base image or dependencies, making the image more maintainable in the long run.

### Inspect the Docker image:

```yaml
- name: Inspect Image
  uses: dfreilich/pack-action@v2.1.1
  with:
    args: 'inspect-image ${{ env.IMG_NAME }}'
```

This step uses the Pack CLI `inspect-image` command to gather detailed information about the Docker image. It provides insights into the image layers, metadata, and other relevant details. 

This inspection can be helpful for troubleshooting, optimizing image size, and ensuring the image is built correctly.

### Clean Up

```yaml
- name: Clean Up
  run: |
    docker container stop 'personal-portfolio'
```

To ensure proper resource management, this step stops the Docker container that was started in the previous testing phase. It stops the container named 'personal-portfolio' using the `docker container stop` command.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/docker-hub.png)

## Full Workflow

To see the complete workflow with all the defined steps, including their configurations, you can refer to the [main-pack-cli.yaml.yml](https://chat.openai.com/c/.github/workflows/main-pack-cli.yaml.yml) file in the repository.

## Conclusion

With Pack CLI and Cloud Native Buildpacks, building and publishing Docker images becomes simpler and more efficient. By eliminating the need to write Dockerfiles, the process is streamlined, reducing complexity and potential errors. 

In this tutorial, we have explored a step-by-step workflow that demonstrates the power of Pack CLI in simplifying Docker image management. By following this workflow, you can easily adapt the process to your own projects, accelerating your Docker image building and publishing process.

I hope this explanation helps you understand the code and the workflow in more detail. 

