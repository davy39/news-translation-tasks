---
title: A quick guide to deploying your Python webapp on Google App Engine
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-16T00:12:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-your-first-python-webapp-on-google-app-engine-2d487b52796a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BD_VuHYR7AmZpNo0Jsz6MA.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Google
  slug: google
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Karan Asher

  The growth in the number of web-based applications and frameworks in the recent
  times is astounding. As companies such as Google, Amazon, and Microsoft provide
  more and more easy-to-use tools to build and deploy applications, it makes ...'
---

By Karan Asher

The growth in the number of web-based applications and frameworks in the recent times is astounding. As companies such as Google, Amazon, and Microsoft provide more and more easy-to-use tools to build and deploy applications, it makes more sense to use the services and tools provided by them instead of building things in-house and hosting it on-premise.

Google App Engine is a great way to get started with learning web development. It provides a bunch of useful features such as sharding, automatic database replication, automatic scaling, memcache, and so on.

However, the process to sign-up and deploy your first test hello world app is not very intuitive.

In this, post, you will learn a very straightforward and easy to understand method to **deploy your first Python webapp on Google App Engine. So let’s get started.**

### Step 1. Download the basic housekeeping stuff

No matter what platform you build products on, there is always some housekeeping stuff you need to put in place before you can hit the ground running. And deploying apps within the Google App Engine is no exception.

1. Download [Python 2.7](https://www.python.org/download/releases/2.7/)  
As of when this article was written, the Google App Engine [standard environment supports Python only upto version 2.7](https://cloud.google.com/appengine/docs/standard/python/). However, it is only a matter of time before support for Python 3.x is added. You can check the App Engine docs for the latest info.
2. Download [Google Cloud SDK](https://cloud.google.com/appengine/docs/standard/python/download)  
This will allow you to fork apps onto your local machine, make changes (edit and develop the app), and deploy your app back to the cloud.
3. Set the Python path in the Google App Engine launcher  
After downloading the SDK, launch the App Engine launcher, go to Edit -> Preferences and make sure you set the path for where you installed Python in step 1 above.

![Image](https://cdn-media-1.freecodecamp.org/images/ykQfsEj0zmdjjRFnxiLSFqOOjGF1lWdJYkGK)
_Set the Python path in Google App Engine launcher_

That’s all you need. Your local machine should now be ready to build webapps.

### Step 2. App Engine sign-up

This is often the most confusing part of the entire setup. Things you should know when you sign-up:

1. Currently, App Engine offers a free trial for one year.
2. The trial includes $300 of credit that can be used during the one year trial period.
3. You will need to add a credit card to sign-up (for verification purposes).
4. You will not be charged during the sign-up process.
5. You will not be charged during the trial period as long as you do not cross the credit limit offered.

Here are the steps you need to follow to sign-up:

1. Go to the [Google Cloud](https://cloud.google.com/) landing page
2. Follow the sign-up process and go to your App Engine dashboard

Most of the hard work is complete after a successful sign-up.

### Step 3. Create a new project

The next step is to create a new Python project that you can work on. Follow the screenshots below to create a new project.

Launch the new project wizard.

![Image](https://cdn-media-1.freecodecamp.org/images/gHQqw94gnz6i7FPB93bNNPMXoTCIHps5pKEN)
_Image courtesy. [https://console.cloud.google.com/home](https://console.cloud.google.com/home" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/QcsRz0RUf6xmkrBwttFSLeqGLj5rRHqUePXF)
_Image courtesy [https://console.cloud.google.com/home](https://console.cloud.google.com/home" rel="noopener" target="_blank" title=")_

Give your app a name and make a note of your project ID.

![Image](https://cdn-media-1.freecodecamp.org/images/Vxf5RJu080-wPyclcCkQYqHiXeS5uJwZIkbp)
_Image courtesy. [https://console.cloud.google.com/home](https://console.cloud.google.com/home" rel="noopener" target="_blank" title=")_

Hit the create button and Google should take a few minutes to set up all that is necessary for your newly created app.

### Step 4. Fork the app to develop it locally

The next step in the process is to fork the app on your local machine. This will allow you to make changes to the app locally and deploy it whenever you wish to.

Go to Google App Engine launcher and create a new application.

![Image](https://cdn-media-1.freecodecamp.org/images/OYQUQ619PxSHi9DMmgMitKSChUuUF6JdTsYR)

Enter the project ID of your newly created app. Also, provide the folder (local destination) where you wish to store the app locally. Make sure you select the Python 2.7 as your runtime engine.

![Image](https://cdn-media-1.freecodecamp.org/images/8zCrS5i2DBzmxWur4iVctxlktlpYLbfka7aa)

Hit the create button, and you should see your app listed on the window that follows. You should also check that you now see some files in your local storage (the directory you chose in the screenshot above) after this step.

### Step 5. Run the app locally

Before you go ahead and make some changes to the app, it is important to check whether or not you have executed all the above steps correctly. This can be done by simply running the app locally.

Select the app and hit the run button on the window.

![Image](https://cdn-media-1.freecodecamp.org/images/s6uLNJX1RSlALzBAIyodKAZ6ijTwJ9O40Mom)

Wait for a few seconds until you can hit the **Browse** button. Once the **Browse** button becomes clickable, click it. This should take you to the browser, and you should see the hello world text appear in your browser window. Alternatively, you can manually go to the browser and use the port specified to access the app.

![Image](https://cdn-media-1.freecodecamp.org/images/8P4dKa9dS8DMRug1p-jxwNaAyITijRwWGn2x)

As long as you see the above screen, you are all set.

### Step 6. Understand the app structure

It is finally time to look at the lines of code which are running this webapp. Open your app folder in the text editor of your choice. I recommend [Sublime text](https://www.sublimetext.com/) or [VS Code](https://code.visualstudio.com). However, feel free to choose the one you prefer.

Here is a description of the various files.

**app.yaml**

This file is a basic markup file that stores information (some metadata) about the app. It is important to note the following crucial parts of the file.

1. **application**  
This is the project ID which you should never change. This is the unique identifier for the app
2. **url -> scr**ipt  
This is the homepage for the app. In other words, this file will be rendered in your browser when you launch the app
3. **libraries**  
This is where you can include external libraries to use within the webapp

![Image](https://cdn-media-1.freecodecamp.org/images/3Yw98n-vBszn0AtjOTQZKHwyXQdAHFhLzasM)
_app.yaml file in the webapp folder_

**main.py**

This is the homepage of the app (as discussed above). Note that the hello world text in the browser window (step 5) is due to the code you see highlighted below.

![Image](https://cdn-media-1.freecodecamp.org/images/FmhahIpA3gof3ZFwQf0JnA5px4KaqHqEDR6n)
_main.py file in the webapp folder_

### Step 7. Make your changes and deploy the new app

No hello world app is ever complete without the developer changing the hello world text to something else just to make sure that everything happening behind the scenes is working as it should.

Go ahead and change the text in the above screenshot to something else.

![Image](https://cdn-media-1.freecodecamp.org/images/QitcnUiNGjFfYJeANmoPZZydYdMLYGc2D-do)
_main.py file in the webapp folder_

Save the changes, go to the browser and refresh the page. You should see the page with the text “MEOW” displayed.

![Image](https://cdn-media-1.freecodecamp.org/images/w7D7QiVHfJW0JCL3Dl3Ua8S7hNuApqU2psAt)

Finally, it is time to deploy your changes to the cloud to make them globally accessible via a URL. Go to the App Engine launcher, select the app, and hit the **Deploy** button.

![Image](https://cdn-media-1.freecodecamp.org/images/breGh1hefgwsD5w7zR7yVtiujWPENETaPs9Z)

This will ensure your app gets deployed onto Google Cloud. To check whether or not everything worked just fine, go to the URL below:

**https://<yourProjectID>.appspo**t.com/

You should see the exact same window as above, expect now, it is a URL that is globally accessible.

![Image](https://cdn-media-1.freecodecamp.org/images/9wrAp6-bGh7bdzEjdaO2Gb1u38lA1wjhMQBd)

### Step 8. Misc

Congratulations, you’ve finally gotten your first Python webapp deployed on the Google App Engine. Here are some other points which you may find useful.

1. [Jinja 2](http://jinja.pocoo.org/docs/2.10/) is an amazing front end templating library for Python that can do some cool stuff, such as passing objects form Python to HTML, using for loops, if conditions, and so on directly out of the box
2. [Here’s](https://classroom.udacity.com/courses/cs253) a very useful Udacity course on web development that I have personally found quite resourceful
3. Viewing the logs while running your webapp can be handy to debug and also discover some bugs on the fly

![Image](https://cdn-media-1.freecodecamp.org/images/saG-0CilWV6HYRdE9e7GhMEhVjk2k6yE7PFp)
_Log console of the webapp_

_#UntilNextTime_.

