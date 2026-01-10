---
title: How to build a Meetupbot for Slack using Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-13T19:49:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-meetupbot-for-slack-using-node-js-618725aa4c6e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YQTE7lkH8LNnkguLdzaDkA.png
tags:
- name: api
  slug: api
- name: bots
  slug: bots
- name: Meetup
  slug: meetup
- name: slack
  slug: slack
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By premprakashsingh


  What is Slack?

  If you are new to Slack, it’s a great platform for team collaboration and instant
  messaging used in and out of organizations to help team communication and collaboration.

  I first used Slack for a study group. You c...'
---

By premprakashsingh

![Image](https://cdn-media-1.freecodecamp.org/images/1*qj03MmP47z5lduohrVC5aA.png)

### What is Slack?

If you are new to [Slack](https://slack.com/), it’s a great platform for team collaboration and instant messaging used in and out of organizations to help team communication and collaboration.

I first used Slack for a study group. You can create different channels to separate messages and discussions. You can create private channels as well to keep messages private in a team.

The best functionality is that it also allows integrations on it’s platform. And this is what makes it different than other messaging and collaboration platforms.

You can integrate Google Calendar, Twitter, Trello, and more. It also let’s you create custom applications like bots.

### Project

In this post, I will walk you through building a [MeetupBot](https://meetupbotteam.github.io/meetupbot-landing-page/) for Slack using Node.js. It will give you list of meetups going on near your location based on your interest.

Feeling excited?

![Image](https://cdn-media-1.freecodecamp.org/images/1*l2W7LDBTPVvEAArgB4Sg2w.gif)

It will use Slack’s slash commands. You can type **/meetupbot** from within Slack to call the [MeetupBot](https://meetupbotteam.github.io/meetupbot-landing-page/) and it will greet you along with the list of commands.

I built this project as part of [Chingu](https://medium.com/chingu) cohort with my 2 team members [Zameer](https://github.com/zamhaq) and [Linus](https://github.com/nusli)

![Image](https://cdn-media-1.freecodecamp.org/images/1*VTIZoHI-bb-CuXb85G6DHg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*2ROpGK4lel2ZHV5rG8PI0A.png)

You will need basic knowledge of Node.js and how APIs work. Let’s get started.

### Steps for building MeetupBot for Slack

#### Step 1 — Project Setup

my repo URL : [slack-meetup-bot](https://github.com/PREMPRAKASHSINGH/slack-meetup-bot)  
Glitch : [glitch.com](https://glitch.com/)  
Meetup_api : [meetup.com/meetup_api](https://www.meetup.com/meetup_api/)

* First fork my repository [here](https://github.com/PREMPRAKASHSINGH/slack-meetup-bot).
* Then go to [glitch.com](https://glitch.com/) and create a project and edit the project name to a shorter name.
* Click on the **Project Name** &g**t; Advanced Opti**ons. Then cli**ck Import from Git**Hub. You first need to grant access of the GitHub repo to import your repositories into Glitch.
* Go to [Meetup Api here](https://www.meetup.com/meetup_api/) and click on **API Key** tab and save that as you will pass it with every request to Meetup API.
* In your Glitch project open `**.env**` file and set a variable **SECRET** as Your Meetup API Key as `SECRET=<MeetupApiK`ey>
* Click on **Show Live** in Glitch and you will get your Glitch project URL.

#### Step 2 — Create a Slack App

* Go to [Slack apps](https://api.slack.com/) and then click on **Your Apps** &g**t; Create New** App.   
It will show you following screen:

![Image](https://cdn-media-1.freecodecamp.org/images/1*EOvPe85KeYY8q_refsTtyQ.png)

Enter the App Name and select **Development Slack Workspace** and click on **Create App**. Now we need to do 3 things to see it working in our Slack workspace.

On the next screen you will see your App Configuration page with following things:

1. Activate incoming webhooks.
2. Create Slash commands.
3. Install your app to your workspace.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EusJC6rdy4lN82UtELAbMw.png)

* Now click on **Incoming Webhooks** and activate it.   
Incoming Webhooks allows you to post messages into Slack.
* Next thing click on **Slash Command**” and create one as **/meetupbot**. Command as `/meetupbot`, **Request URL** as `**<glitch-project-url>/mee**`tupbot, and **add a Short Descr**iption **and a Usag**e Hint.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eWKdYfwrTuq-TrbrVBn6ng.png)

* By activating Incoming Webhooks and creating Slash Commands you should have already got a green tick on Permissions.
* Now click on **Install your app to your workspace** and that will take you to next screen to confirm and authorize before installing. And now you are good to go.

#### Step 3 — Test it in your channel

Open your Slack team channel and type **/meetupbot** and you should be able to see your commands popping up. Click **Enter** and you will see a greeting message from MeetupBot and a list of commands that you can use.

Since you have created only one slash command go to your App page and create 1 more commands as **/meetupbot-show** with **Request URL** as `<glitch-project-url>/meetupbo`t-show (Follow step 2 — create Slack Command).

Now try this command, type `**/meetupbot-show San Francisco and JavaScript**` then hit Enter and you will see list of JavaScript meetups in San Francisco with details like Name of Event and Meetup Group, Date of Meetup, Status, Venue and Rsvp Count. Click on Event and it will take you to their Meetup Event page.

So that’s it, Congratulations you have successfully created a MeetupBot for Slack using Node.js.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6MYbG_q1sUHux_vYTIBW-w.gif)

### Lets understand the code.

We are using the Google Geocode API to get Latitude and Longitude from location/address parameter that is passed in the command. This latitude and longitude along with interest parameter is then passed to the Meetup API to get a list of meetups.

Also we are using Express.js and JavaScript Promises, npm packages Moment.js for parsing dates and Request to make API calls.

What happens when you call `**/meetupbot**` ? It makes a Post request to `glitch-project-url/meetupbot`.

The request body contains `user_name`, `text` and other info. The reply object is the JSON response format for the Slack API.

What happens when you call `**/meetupbot-show**` ? It makes a Post request to `glitch-project-url/meetupbot`. The request body contains the `user_name`, `text` (such as location and interest separated by “&”) and other info.

We first make sure the location and interest parameters sent with the command are not blank.

Then we pass location to `getGeocode` method which is a JavaScript Promise that make calls to Google Geocode API and returns Latitude and Longitude, which is then passed to `getMeetupEvents` Promise to get list of meetup by making a call to Meetup API.

The Meetup API returns an array of meetup event objects and we iterate through this array to make an array of event objects in Slack response format and keep pushing it in the `attachment` array which we created in the start.

And that reply with event attachments is then returned as response and is shown in your Slack.

This response will only be visible to you (the user who calls the bot ) and won’t disturb other members of channel.

In the above code we have 2 Promises as follows:

* `getGeoCode()` — This take location as parameter and makes an API call to Google Geocode API with location as query string and returns `latlong`.
* `getMeetupEvents()` — This takes location and interest as parameters and makes API call to Meetup API containing the API Key, Latitude, Longitude, text or interest and radius as query string parameters.

The above code uses JavaScript Promise which is basically used to handle asynchronous operations. It allows you to write asynchronous code that is similar in style to synchronous code.

Also helps in avoiding nested callbacks by using chainable `then`. If you have nested callbacks in code then it looks like pyramid structure also known as “callback hell”.

### Official MeetupBot

The official MeetupBot has one more command as **/meetupbot-find** to get list of meetup group in your location/area and also has Oauth code so that you can install it by clicking add to slack button.

You can find it here [MeetupBot landing page](https://meetupbotteam.github.io/meetupbot-landing-page/) and [MeetupBot github repo](https://github.com/MeetupBotTeam/slack-meetup-bot). Start using it now.

Did you find this article useful? Write your comments below.

If you found this article helpful, do share with your friends and give this couple of claps.

— Thank you :)

Originally posted [here](http://howtocoder.com/blog/how-to-build-meetupbot-for-slack-using-nodejs).

