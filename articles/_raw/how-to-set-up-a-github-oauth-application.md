---
title: How to Set Up a GitHub OAuth Application
subtitle: ''
author: Naomi Carrigan
co_authors: []
series: null
date: '2022-10-27T21:31:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-github-oauth-application
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-george-becker-333837--1-.jpg
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: GitHub
  slug: github
- name: oauth
  slug: oauth
seo_title: null
seo_desc: "GitHub is an incredibly useful OAuth provider, especially if you are building\
  \ an application targeted toward developers. \nIn this article, we will give you\
  \ a quick rundown of how to set up a GitHub OAuth application.\nCreate Your Application\n\
  Begin by ..."
---

GitHub is an incredibly useful OAuth provider, especially if you are building an application targeted toward developers. 

In this article, we will give you a quick rundown of how to set up a GitHub OAuth application.

## Create Your Application

Begin by navigating to your GitHub settings (make sure you are logged in!). Scroll down to the bottom of the sidebar and click "Developer Settings".

This will take you to the application page:

![GitHub OAuth Apps view, showing a hacktoberfest and mattermost application that have been previously authorised.](https://www.freecodecamp.org/news/content/images/2022/10/image-230.png)
_You may see some applications you've previously authorised._

Click the "New OAuth App" button to create a new application.

![The new OAuth application page, showing form fields for Application name, homepage URL, application description, and authorisation callback URL.](https://www.freecodecamp.org/news/content/images/2022/10/image-232.png)

Fill in the form and click "Register application". This will create your application and take you to the settings page.

![The Application settings page, which shows the same form fields as the previous form, with additional options to transfer ownership, revoke user tokens, generate client secrets, and upload a logo.](https://www.freecodecamp.org/news/content/images/2022/10/image-233.png)

For OAuth applications, you will need the Client ID. You will also need to generate a client secret. Click the "Generate a new client secret" to do so.

![The new client secret (obfuscated for security in this image)](https://www.freecodecamp.org/news/content/images/2022/10/image-234.png)

Make sure to save this secret in a secure location as you will not be able to view it again.

## Using Your New Application

Now that you have a client ID and secret, you can use your OAuth application in your project. 

If you want to learn how to do so, [freeCodeCamp's curriculum can teach you](https://www.freecodecamp.org/learn/quality-assurance/#advanced-node-and-express). 

Happy coding!

