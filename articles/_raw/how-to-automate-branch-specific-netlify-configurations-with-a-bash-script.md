---
title: 'How to Automate Branch-Specific Netlify Configurations with a Bash Script:
  A Step-by-Step Guide'
subtitle: ''
author: Francis Ihejirika
co_authors: []
series: null
date: '2024-12-16T17:51:07.621Z'
originalURL: https://freecodecamp.org/news/how-to-automate-branch-specific-netlify-configurations-with-a-bash-script
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1733871988108/cde4ea9b-705c-40e0-9730-09dbeebdfbae.png
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: Netlify
  slug: netlify
- name: Web Development
  slug: web-development
- name: automation
  slug: automation
- name: Bash
  slug: bash
seo_title: null
seo_desc: 'When you’re working on a project with multiple environments – like staging
  and production – for your backend APIs and frontend deployments, you’ll want to
  make sure you have the correct configuration and commands for each branch in your
  repository.

  T...'
---

When you’re working on a project with multiple environments – like staging and production – for your backend APIs and frontend deployments, you’ll want to make sure you have the correct configuration and commands for each branch in your repository.

This can be daunting in situations where multiple developers are actively working on a codebase, making changes to different branches, or managing multiple branch-specific configurations.

Like with every pull request or change pushed to a branch, you’ll need to review every line of code that’s been changed, added, or removed before deciding what gets merged or not. Configuration files in codebases are not exempt from this, making them prone to errors, as a simple change can affect your entire Continuous Integration setup.

When changes get made to the staging or production branch and a build is triggered, you’ll want to ensure that the correct resources attached to a branch are maintained. In some cases, you may need to define different redirect rules for each respective client, custom build commands, or other settings for each branch.

In this article, I’ll walk through how to manage branch-specific configurations including redirects for multiple branches automatically, using a simple bash script. I’ll also show you how to safely merge context-specific rules for your staging and production branches on Netlify.

## What we’ll cover:

* [Project Structure and Scenario](#heading-project-structure-and-scenario)
    
* [What are Redirects/Rewrites?](#heading-what-are-redirectsrewrites)
    
* [How Netlify Processes Redirects](#heading-how-netlify-processes-redirects)
    
    * [Using the \_redirects file syntax](#heading-using-the-redirects-file-syntax)
        
    * [Using the netlify.toml configuration file syntax](#heading-using-the-netlifytoml-configuration-file-syntax)
        
* [The Problem: Managing Multiple netlify.toml Files for Different Branches](#heading-the-problem-managing-multiple-netlifytoml-files-for-different-branches)
    
* [How to Write the Script to Automatically Create Our Configuration File(s)](#heading-how-to-write-the-script-to-automatically-create-our-configuration-files)
    
    * [Sample Netlify.toml file](#heading-sample-netlifytoml-file)
        
    * [Step 1: Create the script folder and add the script file](#heading-step-1-create-the-script-folder-and-add-the-script-file)
        
    * [Step 2: Modify package.json to include the script command](#heading-step-2-modify-packagejson-to-include-the-script-command)
        
* [How to Deploy Our Client to Netlify](#heading-how-to-deploy-our-client-to-netlify)
    
    * [First deployment of your project to Netlify](#heading-first-deployment-of-your-project-to-netlify)
        
    * [Subsequent Deployments / How to Set Up Branch Deployments](#heading-subsequent-deployments-how-to-set-up-branch-deployments)
        
        * [Step 1: Set Up Environment Variables in Netlify for each branch context — production, staging, and so on](#heading-step-1-set-up-environment-variables-in-netlify-for-each-branch-context-production-staging-and-so-on)
            
        * [Step 2: Trigger a new deploy](#heading-step-2-trigger-a-new-deploy)
            
* [Inspect Your Deployments](#heading-inspect-your-deployments)
    
* [Conclusion](#heading-conclusion)
    

## Project Structure and Scenario

Consider a situation where you have two separate servers deployed for a project: one to serve requests to a staging environment (deployed to Render), and another to the production environment (deployed to Google Cloud Run).

You also have two separate client deployments on Netlify, each with their respective API\_BASE\_URLs, that are served by their respective servers as illustrated below:

![Illustration showing branches of a project repository - development, staging and production - each with its own server and client](https://cdn-images-1.medium.com/max/1200/1*Zat3jiq5BCucEzDHKp8yuA.png align="left")

The image below is a `sample-project` repository, with `api` and `client` folders/directories within it. This is an overview of the structure in each of the branches outlined above. Each directory contains its own `package.json` file, is treated as an independent component, and can be deployed to two separate services.

![A project structure for a sample project, including directories and files for both backend and frontend. ](https://cdn-images-1.medium.com/max/800/1*Vkh8EyIA5qamhoJOz2ksSg.png align="left")

In your frontend deployment for each of the clients, all your requests made to endpoints that begin with `/api/v1/` are routed to the server. Other routes remain within the frontend to direct you to pages within the client. So you’re required to write the correct rules to guide your client on how to process these requests. These are called redirect rules or rewrites.

## What are Redirects/Rewrites?

Redirects, or rewrites, are rules you can create to have certain URLs automatically go to a new location anywhere on the internet (source: [WPengine](https://wpengine.com/)). These are also generally known as **URL forwarding** and you can use them anywhere – in entire websites, sections of a website, or an entire web application.

In web applications, redirects are often utilized to determine how to process requests. Web hosting platforms such as Netlify and Vercel use them as well, giving developers the option to determine how their web applications process requests.

## How Netlify Processes Redirects

Netlify has two possible ways to specify redirect rules. You can do it using the `_redirects` file syntax or using the `netlify.toml` configuration file syntax. They achieve the same goal, but the `netlify.toml` syntax gives you more options and capabilities.

### Using the `_redirects` file syntax

If you opt to use the redirect syntax, you should simply create a `_redirects` file in the public folder of your client app, and specify the redirect rules within it. That’s as easy as it gets. Below is an example of a redirect rule within the file:

![Sample Netlify _redirects file showing usage syntax and redirect rules](https://cdn.hashnode.com/res/hashnode/image/upload/v1733944577546/2f21a9b9-6843-4900-a6fe-5573a087b3d9.png align="center")

The above rule can be interpreted as:

1. Send all my requests that match `/api/v1` to the API URL specified, and return a 200 success status code. The asterisks (\*) after `/api/v1/` as seen in `/api/v1/*` instruct it to append any other extension of the original URL to the stated API URL. For example, if you have a `/api/v1/users` route in your frontend, that request will be redirected to `https://your-api-base-url.com/api/v1/users`. The `:splat` seen in the API URL is simply a placeholder.
    
2. Serve all other default routes through the index.html folder. This is required to ensure that you don’t encounter broken pages when you navigate to other pages and attempt to visit the previous page using the “back” button.
    

### Using the `netlify.toml` configuration file syntax

The `netlify.toml` configuration file gives you a lot more flexibility when specifying redirect rules, including but not limited to matching the original request route, the required destination, the preferred status code response, header rules, signatures, country restrictions, roles and more.

This is a sample `netlify.toml` file sourced from [Netlify’s documentation](https://docs.netlify.com/routing/redirects/#syntax-for-the-netlify-configuration-file):

![Sample netlify.toml file showing configuration](https://cdn.hashnode.com/res/hashnode/image/upload/v1733947216566/f64670b4-9d28-4c50-a753-1deb27dfc646.png align="center")

**Quick Note:** using the redirects file for redirecting certain requests to our API is perfectly fine. But it can be considered a security risk adding our API URL in plain text in the *redirects* file if the API\_BASE\_URL is supposed to be private. This is because any file in the public folder is what it sounds like – public – and anyone can access it.

If the direct locations you desire to have in your app are public URLs, then feel free to utilize the `_redirects` file syntax. But if you prefer to have a private URL(s), utilizing a `netlify.toml` configuration file in combination with the environment variables is generally a better idea.

## The Problem: Managing Multiple `netlify.toml` Files for Different Branches

When you use the `netlify.toml` file to define your build commands and environment-specific settings, and you make changes that are pushed to your repository and open pull requests, you have to manually ignore or edit each `netlify.toml`in each branch. This eventually becomes very stressful and susceptible to errors.

In addition to this, we want to avoid having our API URLs hardcoded in either our `_redirects` or `netlify.toml`file within our project codebase for security reasons. We will use environment variables as provided within our Netlify UI for production and staging contexts.

To avoid the above problems, we will use a small script in our codebase to dynamically generate the correct `netlify.toml` files for each branch. This approach eliminates conflicts and removes the need for manual intervention when switching between branches or handling pull requests.

## How to Write the Script to Automatically Create Our Configuration File(s)

### Sample `Netlify.toml` file

Below is a screenshot of a sample `netlify.toml` file we are trying to achieve for each build. You can see that all our requests that match `api/v1/` in our codebase will be routed to our API.

You could have your API endpoint requests structured differently, for example `/api/your-endpoint` – just make sure to adjust the script accordingly. In this sample project, we use `api/v1/your-endpoint` as our structure.

![Netlify configuration file showing build commands and redirect rules](https://cdn-images-1.medium.com/max/800/1*oj_oJDA7lnC9we2zuQHm4w.png align="left")

### Step 1: Create the script folder and add the script file

In the `client` directory, create a `scripts/` directory and a [`configure-netlify.sh`](http://configure-netlify.sh) script file. You are required to do this for each branch in your repo. The content remains the same.

Open the [`configure-netlify.sh`](http://configure-netlify.sh) script file and paste the following content within it:

```bash
#!/bin/bash

# Ensure API_BASE_URL is set
if [ -z "$API_BASE_URL" ]; then
  echo "Error: API_BASE_URL environment variable is not set."
  exit 1  # Exit the script to stop the deployment
fi

echo "Using API endpoint: $API_BASE_URL"

# Define the desired Netlify configuration
NETLIFY_CONFIG="
[build]
  command = \"npm install && npm run build\"
  base = \"client\"
  publish = \"dist\"

[[redirects]]
  from = \"/api/v1/*\"
  to = \"$API_BASE_URL/:splat\"
  status = 200
  force = true

[[redirects]]
  from = \"/*\"
  to = \"/index.html\"
  status = 200
"

# Create or update the netlify.toml file
if [ ! -f "netlify.toml" ]; then
  echo "Creating netlify.toml file..."
else
  echo "Updating existing netlify.toml file..."
fi

echo "$NETLIFY_CONFIG" > netlify.toml

# Confirm successful configuration
echo "netlify.toml file has been configured successfully!"
```

The script does the following:

1. It checks the environment variables to ensure that the `API_BASE_URL` is set. If this isn’t set, it exits the build and causes it to fail. We did this to ensure that you don’t mistakenly create a successful deployment but with invalid URLs in production.
    
2. It then creates the content of the `netlify.toml` file as shown in the sample above. If your API endpoints use a different structure from `api/v1/your-endpoint`, you can adjust the script to fit your desired structure.
    
3. It checks if there already exists a `netlify.toml` file. If it doesn’t exist, it creates one and writes the content into it. If it exists, it updates it with the correct content during the build, using the `API_BASE_URL` set in the environment variables.
    

### Step 2: Modify `package.json` to include the script command

To integrate this script with your build process, we will add a script command to the `package.json` file to call this script before running the actual build.

Add the `configure-netlify` command as follows: `"configure-netlify": "bash scripts/`[`configure-netlify.sh"`](http://configure-netlify.sh) within the scripts in your `package.json` file.

Update your build command to run the script before running the actual build: `"build": "npm run configure-netlify && vite build"`.

![Image showing updated package.json file with custom configure-netlify command and updated build command](https://cdn-images-1.medium.com/max/800/1*Sds0AS4Poe80pc9D9YkBvQ.png align="left")

Don’t forget to save these changes and push them to your remote repository.

## How to Deploy Our Client To Netlify

When deploying our client to Netlify, we are given three options:

1. importing an existing project (that is, a project that exists on a git repository service such as GitHub and GitLab),
    
2. importing from a template, or
    
3. manually deploying a static site using the Netlify drop (drag and drop) interface.
    

For the configuration in our repository to work as expected during our build process, you’ll need to use the option that requires importing from an existing project such as GitHub. Using the drag-and-drop interface won’t work. If you must use this, then opt for the `_redirects` file syntax option to define your redirects.

### First deployment of your project to Netlify

When deploying your project for the first time, you are given the option of deploying only one branch initially. You can only add and specify other options, such as other branches, in subsequent deployments.

To deploy your project, take the following steps:

1. Sign in to Netlify &gt; [netlify.com](http://netlify.com)
    
2. Click "Add new site" &gt; "Import an existing project" &gt; "Deploy with GitHub"
    
3. Click "Configure Netlify on GitHub" &gt; Search for your repository &gt; Select it
    
4. Enter a unique site name for your project
    
5. Configure deploy settings. Here you are required to select the preferred branch to deploy. For the initial deployment, we will deploy the `main` branch which we use as the production branch.
    
    * Branch: main/master
        
    * Build command: `npm run build`
        
    * Publish directory: `dist` (Select the directory where your static file lives. In this sample project, it’s exported into the `dist` directory. Some tools export into `build`)
        
6. Enter the environment variables for your project. Don’t forget to enter your `API_BASE_URL` from your server. This is an essential requirement according to the bash script.
    
7. Click "Deploy site"
    

![Netlify deployment screen showing optional project build settings](https://cdn.hashnode.com/res/hashnode/image/upload/v1733951997499/f329f2e6-b977-4b1f-a6ea-6b20610dc0d2.png align="center")

Your project should deploy correctly, and you’ll be able to see the `netlify.toml` configuration generated by the script by inspecting the deployment details at the bottom of the successful deployment page.

You can download this file to your local machine to see the configuration generated. It should match the sample `netlify.toml` file above. You can also test that it works using your generated site link.

![Netlify screen showing deploy log and static files after successful deployment](https://cdn.hashnode.com/res/hashnode/image/upload/v1733952720930/97ccee2f-e93b-4205-94fa-a8ab32dd37c2.png align="center")

## Subsequent Deployments / How to Set Up Branch Deployments

### Step 1: Set Up Environment Variables in Netlify for each branch context  — production, staging, and so on

When your project has been deployed successfully, you can set up deployments for your staging branch. To edit the configurations, you’ll need to:

1. Navigate to the list of your sites
    
2. Select your successfully deployed site
    
3. Click on “site configuration” on the left menu
    
4. Select “environment variables” &gt; click the “Add a variable” button.
    

![Netlify site configuration page of successfully deployed site, showing environment variables](https://cdn.hashnode.com/res/hashnode/image/upload/v1733953093253/26948920-70a7-47bc-8f53-4cb19a9d8543.png align="center")

You will be given the option of adding variables individually or importing an entire `.env` file. You can choose either option. In the image below, I’ve selected “Import from a `.env` file”.

![Environment variables screen showing options available to add a variable - using a single variable entry or multi entry from a .env file](https://cdn.hashnode.com/res/hashnode/image/upload/v1734124727631/1bb20e6b-1232-4a79-bc18-2df2440cb641.png align="center")

Seeing that our production site, deployed from the `main` branch (with the production environmental variables), has already been deployed, you’ll need to:

1. Uncheck the production branch (to prevent replacing the initially deployed main branch. Be careful not to mix up your environment variables for different branches)
    
2. Select “branch deploys”
    
3. Copy and paste the content of your .env file in the input section
    
4. Don’t forget to add the `API_BASE_URL` environment variable for your staging environment
    

Note that in selecting branch deploys, the environment variables imported here will affect all branch deploys, apart from the production branch. You can further customize your contexts by selecting a custom branch, but that’s an entirely different approach which may require you to further customize your `netlify.toml` configuration file or the bash script.

![Environment variables screen with available contexts for deployment](https://cdn.hashnode.com/res/hashnode/image/upload/v1733953419262/2f62d3d6-2549-4a35-aa0b-7a02225bd630.png align="center")

If you decide to import each environment variable individually, you are given a similar option as seen below. Ensure that you select the correct context for each branch.

DON’T USE THE SAME VALUES FOR ALL CONTEXTS. As seen in the image below, selecting “*different value for each deploy context*” will allow you to define the values for each one. In this case, we define the values for branch deploys. Your initially used production variable should already exist.

![Environment variable insertion screen for single variable, showing value options for different contexts](https://cdn-images-1.medium.com/max/800/1*699HAdcahAzATFCDYlbqpw.png align="left")

When all the variables have been imported, you can inspect them to confirm that they have been correctly imported by selecting the dropdown on the right beside each variable and inspecting their values.

![Environmental variables set for deployed web application](https://cdn.hashnode.com/res/hashnode/image/upload/v1733954618431/66e90f42-4e3d-4c5b-95ec-a6ae03207498.png align="center")

### Step 2: Trigger a new deploy

When all your environment variables have been imported for the different contexts – production and staging in this case – navigate to “deploys” on the left panel of your screen. Then hit the “Trigger deploy” button, clear the cache, and initiate a new deployment.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1733954838853/79685cf6-54a5-4495-8777-914fcc46950f.png align="center")

## Inspect Your Deployments

You can confirm that your script works as expected by selecting any of the deployments and selecting the building dropdown in the “Deploy log”. You will see the command run, as well as your output and API URL for that deployment, as defined by your context.

![Deploy log for successfully deployed web application, showing values logged by automation script during build](https://cdn.hashnode.com/res/hashnode/image/upload/v1733955355311/8268c1f3-c9cb-4b98-8094-59b7dd2d5b13.png align="center")

## Conclusion

By following the steps in this guide, and using your script and updated commands in each branch in your repo, when you push changes then Netlify will automatically generate or update the `netlify.toml`file in each branch. This ensures that the correct configurations and environment variables for each environment are used at build time.

Your script remains the same across all the branches. This lets you focus on other code changes while your script handles the correct configuration for you safely and easily.

Push changes to any branch to see this in action.

Feel free to connect with me on [Twitter](https://x.com/@francisihej) (@francisihej) or [LinkedIn](https://linkedin.com/in/francis-ihejirika)!
