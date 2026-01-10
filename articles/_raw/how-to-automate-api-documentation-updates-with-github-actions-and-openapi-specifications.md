---
title: How to Automate API Documentation Updates with GitHub Actions and OpenAPI Specifications
subtitle: ''
author: EZINNE ANNE EMILIA
co_authors: []
series: null
date: '2025-09-09T14:28:26.753Z'
originalURL: https://freecodecamp.org/news/how-to-automate-api-documentation-updates-with-github-actions-and-openapi-specifications
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1757428080226/175085d0-cfea-41a0-aa52-a50ad8212980.png
tags:
- name: GitHub
  slug: github
- name: github-actions
  slug: github-actions-1
- name: OpenApi
  slug: openapi
- name: documentation
  slug: documentation
seo_title: null
seo_desc: Maintaining up-to-date API documentation is often one of the biggest pain
  points for developers and teams. Too often, the API spec changes but the docs lag
  behind, leaving developers with outdated or inconsistent information. This frustrates
  consumer...
---

Maintaining up-to-date API documentation is often one of the biggest pain points for developers and teams. Too often, the API spec changes but the docs lag behind, leaving developers with outdated or inconsistent information. This frustrates consumers of your API and increases support overhead.

This is where automation comes in. By combining OpenAPI specifications with GitHub Actions, you can ensure your documentation is always in sync with your API changes.

* **OpenAPI** acts as the single reference point for your API design, keeping your docs consistent, accurate, and aligned with your API.
    
* **GitHub Actions** automates the workflow, validating your spec, building docs, and publishing to GitHub Pages in seconds.
    

This tutorial walks you through a working example of how to use GitHub Actions to auto-update your docs.

## Table of Contents

* [Prerequisites](#heading-prerequisites)
    
* [How to set up your repository](#heading-how-to-set-up-your-repository)
    
* [How to Create the OpenAPI Specification](#heading-how-to-create-the-openapi-specification)
    
* [How to Test the API Spec Locally](#heading-how-to-test-the-api-spec-locally)
    
    * [Install tools](#heading-install-tools)
        
    * [Create a landing page](#heading-create-a-landing-page)
        
    * [Validate Your Spec](#heading-validate-your-spec)
        
    * [Preview in the Browser](#heading-preview-in-the-browser)
        
* [How to Push Local Changes to GitHub](#heading-how-to-push-local-changes-to-github)
    
* [How to Set Up Your GitHub Actions Workflow](#heading-how-to-set-up-your-github-actions-workflow)
    
* [How to Set Up GitHub Pages](#heading-how-to-set-up-github-pages)
    
    * [What is GitHub Pages?](#heading-what-is-github-pages)
        
    * [Setting Up GitHub Pages](#heading-setting-up-github-pages)
        
* [How to Handle Multiple Versions](#heading-how-to-handle-multiple-versions)
    
    * [About the Versions](#heading-about-the-versions)
        
        * [Version 1 (v1)](#heading-version-1-v1)
            
        * [Version 2 (v2)](#heading-version-2-v2)
            
        * [Version 3 (v3)](#heading-version-3-v3)
            
    * [How to Set Up the Versions Locally](#heading-how-to-set-up-the-versions-locally)
        
    * [How to Validate the API Specs](#heading-how-to-validate-the-api-specs)
        
    * [How to Update the GitHub Actions Workflow](#heading-how-to-update-the-github-actions-workflow)
        
* [Summary](#heading-summary)
    

## Prerequisites

* [Node.js and npm installed.](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
    
* [A GitHub account with basic Git knowledge.](https://www.freecodecamp.org/news/gitting-things-done-book/)
    
* [Visual Studio Code Editor](https://code.visualstudio.com/download).
    
* [Basic knowledge of documentation and OpenAPI](https://idratherbewriting.com/learnapidoc/).
    

## How to Set Up Your Repository

If you don’t already have one, create a GitHub repository. For this tutorial, I’ll use `api-docs` as the repo name.

Then open VSCode and create a folder with the same name.

## How to Create the OpenAPI Specification

Inside the folder you just created, create a folder called `spec` and add a file named `greetings.yaml` with the following content:

```yaml
openapi: 3.0.3
info:
  title: Greetings API
  version: 1.0.0
  description: This is a greetings API demonstrating a simple greeting endpoint with query parameters and multilingual support.
  license:
    name: MIT
    url: https://opensource.org/licenses/MIT
servers:
  - url: https://api.yourdomain.com/v1
    description: Production server(v1)
  - url: https://staging.yourdomain.com/v1
    description: Staging server(v1)
security:
  - api_key: []
paths:
  /hello:
    get:
      summary: Returns a greeting
      operationId: getGreeting
      parameters:
        - name: name
          in: query
          required: false
          description: Name of the person to greet
          schema:
            type: string
            example: Ezinne
        - name: lang
          in: query
          required: false
          description: Language of the greeting (default is English)
          schema:
            type: string
            enum: [en, fr, es, ig]
            example: en
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
              examples:
                english:
                  value: { message: "Hello, Ezinne!" }
                french:
                  value: { message: "Bonjour, Ezinne!" }
                spanish:
                  value: { message: "¡Hola, Ezinne!" }
                igbo:
                  value: { message: "Ndeewo, Ezinne!" }
components:
  securitySchemes:
    api_key:
      type: apiKey
      name: Authorization
      in: header
```

This is a simple spec with multilingual greetings. As your API grows (say more languages or versions), keeping docs in sync manually might get tedious. That’s why automation helps.

## How to Test the API Spec Locally

### Install tools:

Before setting GitHub Actions, you can test the API Spec locally on your machine by setting up [Redocly](https://github.com/Redocly) (used to be called Redoc) and testing it in an HTML environment.

Redocly is a lightweight, customizable tool to render OpenAPI specs as an interactive HTML documentation. It’s ideal for static site deployment which makes it ideal for this scenario.

* Install Redoc globally with `npm install -g @redocly/cli`
    
* Install http-server globally with `npm install -g http-server`
    

The http-server is a local server you can use to test the doc on your machine before you push to GitHub and deploy to GitHub Pages.

### Create a landing page:

In your project, make a `docs` folder and add `index.html`:

```xml
<!DOCTYPE html>
<html>
  <head>
    <title>API Documentation</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <body>
    <redoc spec-url="../spec/greetings.yaml"></redoc>
    <script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"></script>
  </body>
</html>
```

### Validate Your Spec:

`redocly lint spec/greetings.yaml`

You should see this if there are no errors or warnings:

```powershell
Woohoo! Your API description is valid. 🎉
```

**Note:** Validating your API Spec before testing is important as it’ll flag any possible errors. This is because Redocly will fail to run the preview if there are any errors in your spec. 

### Preview in the browser:

Run `http-server`, and you should see this in the terminal:

```powershell
Starting up http-server, serving ./
Available on:
  http://127.0.0.1:8080
  http://192.168.x.x:8080
Hit CTRL-C to stop the server
```

Open [`http://127.0.0.1:8080/`](http://localhost:8080/docs/index.html) and navigate to `/docs` to see your docs.

![A preview of the API Specification in a Html page](https://cdn.hashnode.com/res/hashnode/image/upload/v1756983802999/944b8603-7b2e-477a-8156-fdaa60f7e0af.png align="center")

## How to Push Local Changes to GitHub

After making local changes, you need to set up the API documentation so it can update automatically whenever you make changes.

Run these commands if you are pushing to the repository for the first time:

```powershell
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

## How to Set Up Your GitHub Actions Workflow

You can set up your GitHub workflow by creating a few folders.

First, create `.github/workflows/` in the `api-docs` folder. Then, inside the `workflows` folder, create a `docs.yml`. This is the workflow file that will serve as a trigger to run validation, generate the HTML with Redocly, and deploy to GitHub Pages at the same time.

```yaml
name: Build API Documentation and Deploy to GitHub Pages

on:
  push:
    branches:
      - main
    paths:
      - 'spec/greetings.yaml'

jobs:
  build-spec:
    runs-on: ubuntu-latest
    permissions:
      contents: write # needed for gh-pages deployment

    steps:
      # 1. Checkout repository
      - name: Checkout code
        uses: actions/checkout@v4

      # 2. Set up Node.js
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      # 3. Install Redocly CLI
      - name: Install Redocly CLI
        run: npm install -g @redocly/cli

      # 4. Validate OpenAPI spec
      - name: Validate OpenAPI Spec
        run: redocly lint spec/greetings.yaml

      # 5. Build output directory
      - name: Create build directory
        run: mkdir -p public

      # 6. Copy spec
      - name: Copy spec
        run: mkdir -p public/spec && cp spec/greetings.yaml public/spec/

      # 7. Copy landing page
      - name: Copy landing page
        run: cp docs/index.html public/index.html

      # 8. Deploy to GitHub Pages
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
```

Here’s what’s going on in this code:

* Runs when changes are pushed to `main` that affect `spec/greetings.yaml`.
    
* Checks out the repo code.
    
* Sets up Node.js and installs Redocly.
    
* Validates your OpenAPI spec (so broken specs won’t deploy).
    
* Copies the spec and index page into a `public/` folder.
    
* Deploys `public/` to the `gh-pages` branch with GitHub Pages.
    

Since we’re done with local testing, update the file path in the `index.html`:

```xml
<!DOCTYPE html>
<html>
  <head>
    <title>API Documentation</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <body>
    <redoc spec-url="./spec/greetings.yaml"></redoc> <!--update the filepath to match your gh config-->
    <script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"></script>
  </body>
</html>
```

This is so the `public` directory in the workflow will be able to access it correctly.

This workflow will only run when it detects changes in the API Spec (`greetings.yml`). To see the workflow in action, make a minor edit in the `greetings.yaml`.

Push the changes to your GitHub repository:

```powershell
git add .
git commit -m 'add changes'
git push
```

## How to Set Up GitHub Pages

### What is GitHub Pages?

[GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) is a hosting platform owned by GitHub where you can host websites directly from your GitHub account. This means you can publish static sites on the internet using a GitHub domain and anyone with the website link can access it.

There are other hosting platforms you can use to deploy static websites such as [Netlify](https://www.netlify.com/) and [Vercel](https://vercel.com/). But using GitHub Pages for this documentation is easier to set up as it’s on the same platform.

### Setting up GitHub Pages

Set up GitHub Pages by clicking on the Settings tab in your repository.

![A preview of the settings tab in the `api-docs` repository](https://cdn.hashnode.com/res/hashnode/image/upload/v1756985360548/fa3518a7-0b44-4c7b-ae7f-d0e0b17a84c6.png align="center")

Under Source, choose:

* Deploy from branch: `gh-pages`
    
* Folder: `/ (root)`
    

![A step-by-step preview of the gh-pages and root setup](https://cdn.hashnode.com/res/hashnode/image/upload/v1756985446692/a4774bcc-1a42-49f8-a9fd-8ca9339808ef.png align="center")

Then save and wait for the workflow to finish.

Your docs will be live at: `https://<username>.github.io/api-docs`.

## How to Handle Multiple Versions

What if you had multiple API versions to update? Let’s assume the simple greetings API in this tutorial had more features added to it across different versions. In this case, you can manage the APIs for the different versions in a single page and also build and deploy it automatically. 

### About the Versions

#### Version 1 (v1)

This is the starting point which is `greetings.yaml`. The API only has a single `/hello` endpoint that returns a greeting in four languages (English, French, Spanish, or Igbo).

#### Version 2 (v2)

In version 2, the API adds create and read features. You can:

* Use `POST /hello` to create and save a greeting.
    
* Retrieve greetings by their unique ID with `GET /hello/{id}`.
    

#### Version 3 (v3)

Version 3 builds on top of v2 by adding an update functionality. Along with creating and retrieving greetings, you can now update an existing greeting using `PUT /hello/{id}`.

### How to Set Up the Versions Locally

First, create a `v1` folder and move the `greetings.yaml` file to it. Since we are going to be using versions, you can delete the existing `spec` folder.

Then, create a `v2` folder and create a `greetings-v2.yaml` file. [Get the greetings API for version 2 here](https://ezinneanne.github.io/api-doc/v2/greetings-v2.yaml).

Next, create a `v3` folder and add `greetings-v3.yaml` file. [Get the greetings API for version 3 here](https://ezinneanne.github.io/api-doc/v3/greetings-v3.yaml).

To follow the same pattern with others, rename the version 1 file to `greetings-v1.yaml`. Then update your `index.html` to accommodate the other two versions.

```xml
<!DOCTYPE html>
<html>
  <head>
    <title>API Documentation</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 0;
      }
      header {
        background: #2c3e50;
        color: white;
        padding: 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
      }
      select {
        padding: 0.4rem;
        font-size: 1rem;
      }
    </style>
  </head>
  <body>
    <header>
      <h2>API Documentation</h2>
      <div>
        <label for="version">Version: </label>
        <select id="version" onchange="loadSpec()">
          <option value="./v1/greetings-v1.yaml">v1</option>
          <option value="./v2/greetings-v2.yaml">v2</option>
          <option value="./v3/greetings-v3.yaml">v3</option>
        </select>
      </div>
    </header>

    <!-- ReDoc container -->
    <div id="redoc-container"></div>

    <!-- ReDoc script -->
    <script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"></script>
    <script>
      function loadSpec() {
        const version = document.getElementById("version").value;
        Redoc.init(version, {}, document.getElementById("redoc-container"));
      }
      // Load default (v1) on first load
      window.onload = loadSpec;
    </script>
  </body>
</html>
```

### How to Validate the API Specs

Earlier in this article, I mentioned testing your specification locally. Now that you have two more versions of the greetings API, run the test to highlight and fix any existing errors.

* For the version V2: `redocly lint v2/greetings-v2.yaml`
    
* For the version V3: `redocly lint v3/greetings-v3.yaml`
    

### How to Update the GitHub Actions Workflow

Now that you have three API Spec versions, you need to update your workflow so it will monitor the three spec files and the HTML document for changes, and then push and deploy them to GitHub Pages as well.

Add this to your `.github/workflows/docs.yml`:

```yaml
# Name of the workflow
name: Build and Deploy API Documentation

on:
  push:
    branches: [ main ]
    paths:
      - 'docs/index.html'
      - 'v1/greetings-v1.yaml'
      - 'v2/greetings-v2.yaml'
      - 'v3/greetings-v3.yaml'

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    permissions:
      contents: write

    steps:
      # 1. Checkout the repository
      - name: Checkout repository
        uses: actions/checkout@v4

      # 2. Create build directory
      - name: Create build directory
        run: mkdir -p public

      # 3. Copy YAML specs into public folder
      - name: Copy v1 spec
        run: mkdir -p public/v1 && cp v1/greetings-v1.yaml public/v1/

      - name: Copy v2 spec
        run: mkdir -p public/v2 && cp v2/greetings-v2.yaml public/v2/

      - name: Copy v3 spec
        run: mkdir -p public/v3 && cp v3/greetings-v3.yaml public/v3/

      # 4. Copy landing page into public
      - name: Copy landing page
        run: cp docs/index.html public/index.html

      # 5. Deploy to GitHub Pages
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
```

And finally, push the changes and reload the site. This should showcase the updated documentation.

![A preview of the API documentation in a hosted GitHub Pages environment](https://cdn.hashnode.com/res/hashnode/image/upload/v1756986868235/9de187f1-12c4-46ca-a73b-daafa353ed1f.png align="center")

## Summary

In this tutorial, you have learned how to auto-update your API docs. We started with a single OpenAPI spec and a basic HTML page rendered by Redocly, and tested it locally. We then set up GitHub Actions to automatically validate the spec, copy the files, and deploy the docs to GitHub Pages. Finally, we extended the setup to handle multiple API versions in one place.

With this workflow, your documentation stays accurate, up-to-date, and hassle-free so every change you make to your API spec goes live when you push the changes.
