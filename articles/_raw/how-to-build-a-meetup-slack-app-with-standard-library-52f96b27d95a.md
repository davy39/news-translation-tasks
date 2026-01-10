---
title: How to build a Meetup Slack bot with Standard Library and Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-29T07:38:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-meetup-slack-app-with-standard-library-52f96b27d95a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bppC-vl7i0Mg0medcD-eAA.png
tags:
- name: api
  slug: api
- name: Apps
  slug: apps-tag
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Janeth Ledezma

  In this guide, you will learn how to set up a Slack application that will display
  information from Meetup’s API, which serves stored data from Meetup to other application
  software.

  Meetup is a popular website where individuals with ...'
---

By Janeth Ledezma

In this guide, you will learn how to set up a [Slack](https://slack.com) application that will display information from [Meetup’s API](https://www.meetup.com/meetup_api/), which serves stored data from Meetup to other application software.

[Meetup](https://meetup.com) is a popular website where individuals with similar interests form groups to organize events in their local cities.

Once we’ve successfully made a request to Meetup’s API, we will receive a response from Meetup, we’ll pull specific data from the JSON payload, and display that data in Slack. We will design our Slack application’s attachment so that it displays the event’s name, description, date and time, location, and more!

![Image](https://cdn-media-1.freecodecamp.org/images/-zI7vrqr8I9pF6n2OOehZufETjLb6qAt6xjB)

### How it Works:

When you submit `/nextmeetup 94709&javascript` (or any zip code and a topic of interest) in Slack’s message box, a webhook will be triggered. The webhook, built and hosted on Standard Library, will first make a request to Meetup’s API, which will return a JSON payload with results from the query.

The webhook will then create Slack messages for each event and post those to a specified channel.

No need to get overwhelmed! Let’s take it a step at a time.

### What You’ll Need:

[1x Slack Account](https://medium.com/p/52f96b27d95a/edit)

[1x Meetup Account](https://www.meetup.com/)

[1x Standard Library Account](https://stdlib.com/)

### Step 1: Set up your Slack Application

Make sure you’re [signed in to Slack](https://slack.com/signin) and visit your Slack Apps Dashboard at [https://api.slack.com/apps](https://api.slack.com/apps). You’ll see a screen that looks like the following.

![Image](https://cdn-media-1.freecodecamp.org/images/aZkh1776B3oyNpits0QtTqGstPsKZdRnQph5)

![Image](https://cdn-media-1.freecodecamp.org/images/nSYlmuf9O0E-WIChpfu5TimGz6Dk0OWmvL-r)

Click **Create New App.** You’ll be presented with a modal to enter your App Name and the Development Slack Workspace you’d like to add it to.

From here, click **Create App,** you’ll find yourself on a **Basic Information** page.

Scroll down to **Display Information.** This is where you can give your Slack app a name, description, and an image if you’d like.

Keep the **Basic Information** page open in your browser. We’ll be using it in a second to retrieve your Slack app’s credentials to connect this application to the backend logic hosted on Standard Library — the code running your application.

### Step 2: Create a Free Standard Library Account

We’ll be hosting our Slack application’s code on [Standard Library](https://stdlib.com)— the code that will be requesting and receiving specific information from Meetups API. So head on over to [Code on Standard Library](https://code.stdlib.com) and claim your free account.

![Image](https://cdn-media-1.freecodecamp.org/images/GswdEExJ9xQZYnIRWgBAjLEpI1zhjqGte5-i)

### Step 3: Copy and Modify the Slack App Code Template on Standard Library

Once you’ve logged in or signed up, you will land on “**Featured API Source.”** These are application code templates available on [Standard Library](https://www.freecodecamp.org/news/how-to-build-a-meetup-slack-app-with-standard-library-52f96b27d95a/undefined) for anyone to easily copy and modify apps. You’re going to select the Slack application code template and modify it to create your API that will power your Slack app.

Enter a unique name for your API project and hit **Okay.**

#### A Brief Explanation of the Slack App Sourcecode Template:

Let’s pause for a moment to understand what we are looking at. The left sidebar is an API project scaffold that Standard Library has set up for you to build Slack apps.

![Image](https://cdn-media-1.freecodecamp.org/images/3nIyUe9M-A4qx6nZAVuea9jcdUx21-djabIa)

The code template for Slack Apps has four directories. We will only work within the `functions` directory which comes equipped with three more folders

`actions/, commands/, and events/` as well as a single file `__main__.js.` The instructions for Slack actions, slash commands, and events for your app live inside those folders.

When you deploy your API, Standard Library will automatically generate HTTPS endpoints (URLs) for each directory. The resulting URLs will allow us to configure webhooks that listen and respond to [Slack’s actions](https://api.slack.com/actions), [slash commands](https://api.slack.com/slash-commands), and [events](https://api.slack.com/events-api).

All five folders (including the `functions` folder are set up with a `__main__.js` file (the directory’s main endpoint). These endpoints`__main__.js` dispatch the appropriate functions when they receive a message from Slack. For this tutorial, the file`__main__.js` will be dispatching the `commands` endpoint when we call our API via our Slack Bot. Now, let’s return to our bot setup!

### Step 4: Add a Command to your Standard Library API

![Image](https://cdn-media-1.freecodecamp.org/images/2YieSaBJlBzrtzxX30Jo-imlMtO0v8sr8fCH)
_Create an additional command_

`commands:` The `commands` directory is the endpoint for all Slack slash commands. Create an additional command by placing your cursor over the `commands` directory and right-clicking. Select **New File** and name your slash command file **nextmeetup.js** and click **Okay**.

![Image](https://cdn-media-1.freecodecamp.org/images/NGeSmqBZ9HUBIsGZUVSCqS1ML7nhjfdHHwLz)
_Name your command_

At this point, you will notice a “hello world” JavaScript function inside (`__main__.js`), which is automatically generated.

![Image](https://cdn-media-1.freecodecamp.org/images/X6k8eDII32yPp-EnudBel9TPujnV6TSYV7bH)

Replace the contents of `nextmeetup.js` with the following:

### A Brief Explanation of the Code:

When you submit `/nextmeetup` via your Slack app, you are making a GET request to Meetup’s API.

Every request to Meetups API has to be authenticated with an API key, so we pass our Meetup key from our `env.json` file into our request. We also send our GET request with the two parameters, zip and topic.

The Meetup API returns an array of meetup event objects, which we can view from Code on Standard Library logs by logging our response: `console.log(response.data)`. Your logs tab is located underneath the debug section.

The `response.data` is an array of events that match your query, and we want to create two attachments for each event (one for location and one for details). We have a function called `formatAttachement` that we can call on each of the events. The results get put in an array called `attachments` that gets sent to Slack.

Once you’ve copied and pasted the code into your file `nextmeetup.js`, save the changes and navigate to the `env.json` file on the left bar menu.

### **Step 5: Fill your env.json File with App Credentials and Keys**

Inside the `env.json` you will notice environment variables for your API. You can set different values for local, dev, and release (production) environments. This file will hold all of your unique access keys to your Standard Library account, Meetup account and Slack app credentials.

We’ll only be making modifications to the `"dev"`environment variables — **make sure you’re modifying the right set**! Note that `"dev”`values are for your development environment and `"release"`values should only be populated when you’re ready to release your app. `“local”` variables can be left blank when deploying from Code on Standard Library, but they should be filled out when working with the [command line tools](https://github.com/stdlib/lib).

![Image](https://cdn-media-1.freecodecamp.org/images/kmKEINtXpdkj3DnRkNN2kgH0xLdt2l8zpvzt)

Let’s start off by filling in the `“STDLIB_TOKEN”` variable. Place your cursor in between the quotation marks (see screen) and either right-click and select **Insert Library Token…** or use the shortcut ⌘ + K.

![Image](https://cdn-media-1.freecodecamp.org/images/BieAtoX31d6JZGVsw2zsOU8m24aKJO-dJjv9)
_Select your library token_

Select **Library Token** to fill in `"dev"` environment.

Now go back to the **Basic Information** page of your Slack App and scroll down to **App Credentials**:

![Image](https://cdn-media-1.freecodecamp.org/images/XHdgD085GHzg7Te1kCHhJ7dumjiBFJDVqK5H)

Copy your **Client ID, Client Secret**, and **Verification Token**. Paste them into their respective fields in`“dev”` section of the `env.json` file.

Add the name you gave your Slack app for the`SLACK_APP_NAME`.

Ex: `SLACK_APP_NAME:Meetup-bot`

The `“SLACK_REDIRECT”` value will be an https endpoint generated by Standard Library once you deploy your API. Even though we haven’t yet deployed, go ahead an fill it in now using this structure. `https://<username>.api.stdlib.com/<apiname&g`t;@dev/auth/ — with your standard library username and your API name. Once we deploy the code you can return to confirm that you filled this value properly.

My `SLACK_REDIRECT` looks like this: `[https://Janethl.api.stdlib.com/slack-meetup-bot@dev/auth/](https://Janethl.lib.id/slack-meetup-bot@dev/auth/)` — make sure you add authentication path with a slash at the end.

Your Slack app’s capabilities and permissions will already be set up with the following [_scopes_](https://api.slack.com/docs/oauth-scopes)_:_

“SLACK_OAUTH_SCOPE”:`bot,commands,chat:write:bot,chat:write:user,files:write:user,channels:history`

![Image](https://cdn-media-1.freecodecamp.org/images/xzltxI-lwFhcCpdQB-lXlBjlknAel681aiSL)

The last variable that you will need to add is your Meetup API key. Meetup requires that every request is authenticated with an API key.

### Step 6: Retrieve your Meetup API Key

Login or create an account at Meetup.com. Head on over to [https://secure.meetup.com/meetup_api/key/](https://secure.meetup.com/meetup_api/key/) to retrieve your unique API key. Click the lock to reveal your API key and copy it.

![Image](https://cdn-media-1.freecodecamp.org/images/JHccHqG9xWelNZYBO-5l8C0P0H6jsL-GOQUC)

Return to your `env.json`file on [Code on Standard Library](https://code.stdlib.com). Add your Meetup key as a `"key"` value, exactly as I have done in the image:

![Image](https://cdn-media-1.freecodecamp.org/images/YXWKWY60H81suM-HQD4HHbxcRBs9Nfzt7y2J)

Make sure to save the changes with **‘⌘ + s’** (or hit **Save** in the bottom right).

On the sidebar menu pen the `__main__.js` file located below the events directory. Deploy the code of your Slack app to Standard Library by clicking “**Run**”.

![Image](https://cdn-media-1.freecodecamp.org/images/5MKFKtAxFpYx5zw7n4MgLd2l4bQHRRko2avG)

* _Shortly after deploying your code, Standard Library generates an HTTPS API endpoint URL where your code lives. This address consists of your <username>.api.stdlib.com followed by the name you gave your API @ the environ[ment: https://janethl.api.stdlib.com/slack-meetup-bo](https://janethl.lib.id/slack-meetup-bot@dev/commands/nextmeetup/)_t@dev/

We now have the URL that will allow us to send and receive messages from our Slack app to Meetup’s API. Now we need to set our URL as webhook in Slack, so let’s head back to the Slack app dashboard

### Step 7: Create a New Slash Command and Set a Webhook

We now need to set our Slack app to respond to a slash command (`/` ). For this, we need to set up a webhook on Slacks API page.

#### What is a Webhook?

Perhaps we can understand what a webhook is by comparing it to an API. APIs are request based — meaning that they operate when a request is made from a third party application. A webhook is event-based — the code will run when a specific event triggers it.

To set a webhook, a service provider must allow its consumers to register a URL where the provider can send information when an event happens. In this example, Slack enables us to register our URL address, and once registered a slash command can trigger our webhook, which will execute the code in our URL.

Now that we understand this, let’s head on over to Slack’s API page to set our webhook. Find and Select **Slash Commands** on the sidebar menu.

![Image](https://cdn-media-1.freecodecamp.org/images/9RPI3R3aSmR2x1IgCzsvzhh0RLjxFvBUFtTJ)

After clicking **Create New Command**, you’ll be asked to enter your command details, for this example use:

![Image](https://cdn-media-1.freecodecamp.org/images/RdkBTkWNoJkHfycs56tu2UoyVV8KXJhregfn)

Command: `/nextmeetup`

RequestURL: `https://<username>.api.stdlib.com/<apiname>@dev/`commands/:bg

Short Description: `retrieves Meetup events`

Usage Hint:`[<zip>&&l`t;topic>]

Hit “**Save**” once complete.

### Step 8: Enable OAuth & Permissions

![Image](https://cdn-media-1.freecodecamp.org/images/jEi9O8ZCrOwelWziR8q3mkNpPmLgQ8cTTaOB)

Return to your [Slack App](https://api.slack.com/apps), On the sidebar menu, click **OAuth & Permissions**.

Once there, you’ll want to enter in a **Redirect URL** as follows: `https://<username>.api.stdlib.com/ <apiname&g`t;@dev/auth/

click “Add” and “Save URLS.”

_This Redirect URL should match the URL that we set on the `env.json` file on Code on Standard Library._

### Step 9: Add a Bot to Your Slack App

Return to your Slack App page, and click **Bot Users** on the left sidebar**.** Click **Add Bot User**. Keep the default settings.

![Image](https://cdn-media-1.freecodecamp.org/images/1nZYRzggEMPwybY5oqVPgmVrFb1Bt-7dwedm)
_Add a Bot User_

**The final step** is to authorize the app. In your browser, type: `https://<username>.api.stdlib.com/<apin`ame>@dev/

![Image](https://cdn-media-1.freecodecamp.org/images/rNNe9b8cppAyfWgiNYwNYdf7ta6HoPZEyDlR)

![Image](https://cdn-media-1.freecodecamp.org/images/derVrVuzpBIm8FxXk9MVJFDPMIjzJ9P3lXtC)

Click the **Add to Slack** button. You will be taken to another authorization screen.

Click **Authorize**. You should see a success message!

![Image](https://cdn-media-1.freecodecamp.org/images/h-QGo9rXpweIsERoYC23FICtUVmjdZDk528D)

### Step 10: Test Your Slack Meetup Application

![Image](https://cdn-media-1.freecodecamp.org/images/J3VxdRA0Vr0wFCUAy3e82nFvEEp4pMt3o6PB)

You’re all done. Try it out! Your Slack App is now available for use in the Slack workspace you authorized it for. Your Slack app should respond to a `/nextmeetup<94709>&<ja`vascript> as I show in the screenshot above.

### That is it & Thank You!

I hope you found this tutorial helpful. I would love for you to **comment here**, **e-mail me at Janeth [at] stdlib [dot] com**, or follow [Standard Library](http://www.stdlib.com?utm_source=content&utm_medium=blog&utm_campaign=scrape_service) on Twitter, [@StdLibHQ](https://twitter.com/StdLibHQ) .

_Janeth Ledezma is a Developer Advocate for Standard Library and Cal grad — go bears! When she isn’t learning the Arabic language, or working out, you can find her exploring NorCal on her CBR500R._ ??? Fol_low her journey with Standard Library through Twitter @ms[s_ledezma.](https://twitter.com/mss_ledezma)_

