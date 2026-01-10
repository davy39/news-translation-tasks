---
title: How to create a Facebook messenger bot for your page
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-08T17:12:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-facebook-messenger-bot-for-your-page-3be12ca18de5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Q5N9wNLQUAl3tnqHbmHWwQ.png
tags:
- name: AI
  slug: ai
- name: '#chatbots'
  slug: chatbots
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Paul Pinard

  When it comes to sharing your chatbot, Facebook Messenger is a must. We created
  a very easy step-by-step integration process for our platform users. Let’s dive
  in!

  In fact, we realized many companies immediately put their bots on Faceb...'
---

By Paul Pinard

When it comes to sharing your chatbot, Facebook Messenger is a must. We created a very easy step-by-step integration process for our platform users. Let’s dive in!

In fact, we realized many companies immediately put their bots on Facebook once in production, as it’s clearly the most user-friendly and easiest way for a customer to contact a company.

A Facebook chatbot has a lot of advantages:

* 24/7 availability
* 100% answers
* Instant answers (think about your _Answer rate_!)
* Tedious tasks are automated

On the SAP Conversational AI platform, we created a step-by-step integration process for our users, so that it only takes a few minutes to reveal your chatbot to your Facebook followers. Let’s dive in!

### Step 1: Get your chatbot ready

First of all, you’ll need a chatbot (seems legit, right?!). Note that once your chatbot is online on Facebook, you’ll be able to modify it, and any changes you make to it will appear in your Messenger chat.

For the purpose of this tutorial, we won’t go into how to create a chatbot. Instead, I warmly invite you to [create your account](https://cai.tools.sap/signup) (it’s completely free!) and [read our tutorial](https://medium.freecodecamp.org/how-to-build-your-first-chatbot-with-the-sap-conversational-ai-9a1a2bd44e3c).

Once your “joke-telling chatbot” (or whatever you’ve built) is ready, return here!

### Step 2: Get your Facebook page ready

Your chatbot will only be available for integration on a **Facebook page** (not on your personal profile). This means you have to create a Facebook page or have in mind the one you’ll use. Let’s assume your company, business, or group already has a page. (If that’s not the case, hit [this link](https://www.facebook.com/bookmarks/pages) and create one.)

As I said in the introduction, having a chatbot on a Facebook page will automate private messaging once it’s connected to your page. Thus, if you decide to remove the chatbot, you’ll immediately revert to traditional person-to-person conversations (which means nothing will happen when users enter a message until you manually answer them).

### Step 3: Create a Messenger Facebook app

Creating an app will help make the **connection between SAP Conversational AI and your Facebook page**. Without this app, you won’t be able to publish your chatbot on your Facebook page.

Click on this link, choose _My Apps_ in the top menu and then _Add New App_.

![Image](https://cdn-media-1.freecodecamp.org/images/PeVCMeylF1uf-IiqZrC2XUDMF1LWji-Id-BA)

Once your app is created, you’ll have to add a Messenger “product”.

There are tons of jobs a Facebook app can be dedicated to, but we specifically want a private messaging application. Go to your app’s dashboard and click _Set Up_ in the _Messenger_ box.

![Image](https://cdn-media-1.freecodecamp.org/images/alQcAGzqHcXP0aGvcCNyzBN1JFMgdNCkafai)

In the left-hand menu, you’ll then see _Messenger_ under _PRODUCTS_.

### Step 4: Get your page token and app secret

Now that we’ve created a Messenger app, we need to link it to your Facebook page (by default, a Facebook app is an independent entity). With this connection, you’ll be given a token, which is basically a unique code that says “OK, this is the code of the Messenger app of the page X”.

In the left-hand menu, click _Settings_ just below the product _Messenger_.

![Image](https://cdn-media-1.freecodecamp.org/images/YAYFtBF9SLnId6tm51ImbksdfubG0hlbX0xK)

Choose the page you want your chatbot to appear on.

For security reasons, you’ll probably need to allow the app to interact with your Facebook page. Click the blue _Edit Permissions_ button, select your page, and check the different boxes.

Once the permissions are given, a token will be generated.

![Image](https://cdn-media-1.freecodecamp.org/images/LOSgIcffDSDDT2S7aEKA1POo6-X0DRc4MuqL)

Go back to the _Connect_ tab in your SAP Conversational AI chatbot, choose _Messenger_, and paste your token in the _Page token_ field in step 4.

**Yay, we’re halfway through!** Let’s now get our “app secret”, which is like a password for your app.

In the left-hand menu, go to _Settings_ &_gt; Ba_sic.

![Image](https://cdn-media-1.freecodecamp.org/images/ihFc65y1uMs6SXh5ArP9CNJDc55XrT82opCN)

For privacy, the app secret is hidden. Click _Show_ and copy and paste it to the _App secret_ field on your chatbot’s _Connect_ tab (similar to what you just did with the page token).

Click _Update channel_ under the SAP Conversational AI form.

### Step 5: Connect SAP Conversational AI to your app

It’s time to connect our platform to Messenger!

On the _Products_ &g_t; Messen_ger _> Se_ttings page, go t_o the We_bhooks section and _click Subscribe To_ Events.

![Image](https://cdn-media-1.freecodecamp.org/images/BNzlSqmuJyI4uUsnB4xDeURV5AWJF958r9JR)

In the pop-up window, enter the values for _Callback URL_ and _Verify token_ that you’ll find in step 4 of your chatbot’s _Connect_ tab.

![Image](https://cdn-media-1.freecodecamp.org/images/ApENnguDSN3hUUxXMn3EfjToXZwRnDowRPdT)

Also select the checkboxes shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/BNecL0jhzxHxfxJJ9k7fKSYnYR0duMCpgjcs)

Once your page has reloaded, select your page in the list so that it can access your webhook.

### Step 6: Test and publish the Messenger Chatbot

Now **you can test your bot as an administrator** (you can also grant some test roles using _Roles_ &g_t; Test Us_ersin the left-hand menu). Your bot won’t be publicly accessible until you change the status, **so take your t**ime to test it and make sure everything is just fine before releasing it to the world!

![Image](https://cdn-media-1.freecodecamp.org/images/wadmMwha2ugHb63V7qmaoW75BK-8F4O8Ou4H)

Once you’re happy with your bot, if you change the toggle to _ON_ (in the top right corner), you’ll be redirected to the settings and prompted to provide some extra information before your bot is published. (Tip: You can also access the settings under _Settings_ &g_t; Ba_sic in the left-hand menu.)

![Image](https://cdn-media-1.freecodecamp.org/images/2Kb-lvORz10FyneB-VlZM-wXL155lwmc1t5W)

Very last step: Facebook will want to verify and test your Messenger chatbot. Here’s what they say about this step in their documentation:

> _“_When you are ready to release your bot to the public, you must submit it to our team for review and approval. This review process allows us to ensure your Messenger bot abides by our policies and functions as expected before it is made available to everyone on Messenger._” — Facebook Documentation_

In the left-hand menu, go to _Products_ &g_t; Messen_ger _> Se_ttings and _click Add to Subm_ission i_n the pages_mes_saging block.

![Image](https://cdn-media-1.freecodecamp.org/images/0XcELdwF90OFhNryXq4PyKU-YHZmaZ5p2kz0)

It won’t take long for the Facebook review team to look at your bot and give you the green light to publish it!

**And that’s all there is to it!**

Hope you enjoyed this tutorial. And remember you’re very welcome to contact us if you need help, through the comment section below or via [Stack Overflow](https://stackoverflow.com/questions/tagged/sap-conversational-ai).

Happy bot building ?

