---
title: How to Automate Your Life and Everyday Tasks with Zapier
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-07-23T16:27:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-automate-your-life-and-everyday-tasks-with-zapier
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/zapier.jpg
tags:
- name: automation
  slug: automation
- name: Productivity
  slug: productivity
- name: workflow
  slug: workflow
seo_title: null
seo_desc: "Every day, we perform hundreds of small tasks. On their own, they don’t\
  \ take much time. But they can add up, especially if you consider that time for\
  \ a whole year. \nBut we’re technologists and it’s 2020. How can we use tools like\
  \ Zapier to make robot..."
---

Every day, we perform hundreds of small tasks. On their own, they don’t take much time. But they can add up, especially if you consider that time for a whole year. 

But we’re technologists and it’s 2020. How can we use tools like Zapier to make robots do these things for us?

* [What is Zapier?](#heading-what-is-zapier)
* [What can we do with Zapier Zaps?](#heading-what-can-we-do-with-zapier-zaps)
* [Zap 1: Get a text if it’s going to rain with Zapier](#heading-zap-1-get-a-text-if-its-going-to-rain-with-zapier)
* [Zap 2: Print a test every week with Google Cloud Print](#heading-zap-2-print-a-test-every-week-with-google-cloud-print)
* [Zap 3: Smashing Magazine Job Alerts with Gmail](#heading-zap-3-smashing-magazine-job-alerts-with-gmail)

%[https://www.youtube.com/watch?v=12oAIHHEJMw]

## What is Zapier?

[Zapier](https://zapier.com/) is an automation tool that connects all of the apps you love and builds powerful fully automated workflows. Whether it’s automating sending an email or making sure that new blog post gets a tweet, we can remove the manual steps of mundane tasks to focus on other things that art important.

Each time you create a new workflow, you’re creating a “Zap”. It’s essentially Zapier’s way to give a name to the workflow you create.

## What can we do with Zapier Zaps?

The brilliant part about Zapier is each app integration makes its API available via Zapier to other app integrations giving you a ton of options to connect and build powerful workflows.

Particularly, we’re going to learn how to do a few things:

* Sending a text every morning if it’s going to rain
* Set up a weekly print job to keep your ink fresh
* Receive emails for new jobs on Smashing Magazine’s job board

While each of these tasks are small, they end up saving you a lot of time. And if you’re creative, you can build upon these workflows to customize a whole lot more.

## Getting started with a Zapier account

Before we get into setting up workflows, you’ll need an account.

[Signing up for Zapier](https://zapier.com/) is free and you get 5 free Zaps to start, so we don’t have to worry about cost here.

Now let’s get into the Zaps.

## Zap 1: Get a text if it’s going to rain with Zapier

To get an idea of how this works, we’ll start with something simple. We’re going to set up a Zap that will send us a text message if the weather predicts rain.

To get started, click the big **Make a Zap** button on the top left of the page when you’re logged into your account.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-make-new-zap.jpg)
_Making a new Zap_

Here, Zapier wants to know the first app we want to connect. Since we’re going to base our Zap on the weather, search for “weather” and select **Weather by Zapier**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/weather-by-zapier.jpg)
_Selecting the Weather by Zapier integration_

It will then ask you to choose a **Trigger Event**, where you’ll select “Will It Rain Today?”, then you can click the **Continue** button.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-weather-will-it-rain.jpg)
_Choosing the Will it Rain Today? event_

When choosing Weather as an event, it requires a little bit of information to give us a personalized prediction. Particularly, it requires your Latitude and Longitude, which we can look up using [latlong.net](https://www.latlong.net/).

![Image](https://www.freecodecamp.org/news/content/images/2020/07/latitude-longitude-finder.jpg)
_Finding latitude and longitude with latlong.net_

You can then enter your **Latitude** and **Longitude** into the **Customize Forecast** screen of Zapier, select your **Units** which defaults to **Fahrenheit**, and then click the big **Continue** button.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-customize-weather-forcast.jpg)
_Configuring forecast with latitude and longitude_

At this point, you can click **Test Trigger**, which simply makes sure it’s working, and click **Continue** again.

Now we’re going to tell Zapier what to do with the information once it knows it’s going to rain.

In the "Do this..." panel, search for “sms” and select **SMS by Zapier**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/sms-by-zapier.jpg)
_Selecting SMS by Zapier_

We’re going to leave the **App** and **Event** as the defaults, so the next screen you can just click **Continue**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-sms-action-event.jpg)
_SMS App and Event_

Now, for Zapier to send you a text, it needs to verify that your phone number belongs to you or that the phone number is knowingly signing up for these texts. To do that, it sends you a one-time PIN that you’ll enter.

So click **Sign in to SMS by Zapier**, which will open a popup window.

Here, enter your phone number, and choose Sms or Call as the verification method at which point it will contact you with a PIN.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/sign-in-to-sms-by-zapier.jpg)
_Sign in to SMS by Zapier and send a PIN_

With that PIN, enter it into the field and click **Continue**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/sms-by-zapier-enter-pin.jpg)
_Entering the SMS verification PING_

At this point the window will close and move you back to the original flow. Here, click **Continue** again.

Now we get to customize the text that we receive.

In the **From Number** field, Zapier gives a bunch of phone numbers you can use. You can either select one number to always send from, which you can set up as a contact so you know it’s Zapier, or you can select **Random**, which will use a random number every time.

Then, click inside of **Message**, and it will bring up some options. I want to know everything possible if it’s going to rain, including the probability, max temperature, and summary, so we can select all or as much as we want and again click **Continue**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/sms-zapier-configure-message.jpg)
_Configuring Weather message_

Finally we get to test if our Zap worked. At this point everything should be configured, so click the **Test & Review** button and you should receive a sample text!

_Note: If you choose a single From Number, you might be limited in how frequent you can receive texts, so if you don’t get it right away, that might be why. Setting random helps prevent that issue, but the the number isn’t consistent._

And once you’re happy with the configuration, you can click **Turn On Zap**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-turn-on-zap.jpg)
_Turning on the SMS Zap_

You’ll now get texts in the morning if the weather is predicting rain!

## Zap 2: Print a test every week with Google Cloud Print

This one doesn’t sound exciting, but have you ever gone through a long period of time where you didn’t print something, only to end up with dried out printer heads or worse yet, a now unsalvageable printer?

We can avoid this by simply running a weekly print job that keeps our printer ink nice and fresh.

For this, we’ll use [Google Cloud Print](https://www.google.com/cloudprint/learn/). To make this work, you’ll need to already have this configured with your Google account.

Let’s create a new Zap and this time for our “When this happens…” search for and select **Schedule by Zapier**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/schedule-by-zapier.jpg)
_Selecting Schedule by Zapier_

We can then select a **Trigger Event** of **Every Week** and click **Continue**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-schedule-trigger-every-week.jpg)
_Setting Trigger Event as Every Week_

Next, you can choose the **Day Of The Week** and **Time Of Day** you’d like to print. I personally run this job weekly at 8pm on Sundays right before the start of a new week. Once configured, click **Continue**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-schedule-sunday-8pm.jpg)
_Configuring Zapier schedule_

At this point, we can click **Test** trigger, which just like before makes sure it’s working properly, and then we can click **Continue**.

Now, for our “Do this…” we want to print, so search for and select **Google Cloud Print**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-google-cloud-print.jpg)
_Selecting Google Cloud Print_

And for the action, select **Submit Print Job**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-action-event-send-print-job.jpg)
_Setting Submit Print Job as Action Event_

At this point, you’ll need to sign into Google Cloud Print. This will open a window and have you log in through Google so that Zapier can interface with the service.

Once connected, click **Continue**.

Now we can configure out print job. Here we’ll want to define what we print.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-google-cloud-print-configuration.jpg)
_Configuring Print Job in Zapier_

In the above, we’re configuring:

* **Which Printer:** the printer we want to print to connected to Google Cloud Print
* **Content:** this can be a URL to a document, HTML, or plain text. I’m using a URL which is a simple test page I made that has some color in it
* **Content Type:**  you’ll want to set this depending on what you set in Content. If you set a URL like I did, it should be URL
* **Title Of Print Job:** the name of the job so you can see it in the print logs
* **Number of Copies:** probably just want 1 so it doesn’t waste ink and paper
* **Color or Monochrome:** you’ll want to explicitly set this if you want color. The idea is to refresh all of the ink cartridges, so only printing black won’t help the color ink, so in my case, I selected color

The rest of the fields are optional, feel free to customize to your liking.

With our configuration set, click **Continue**, and similar to before, we can click **Test** to see our print job in action and if we’re happy, we can click **Turn on Zap**!

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-print-test.jpg)
_Test print from Zapier print job_

_If you want to use the same document, you can find it here: [https://fay.io/printer-test.pdf](https://fay.io/printer-test.pdf)_

## Zap 3: Smashing Magazine Job Alerts with Gmail

If we’re looking for a job, it can be a pain to have to visit every job board every day (or every hour, am I right?). But we can automate this process when the job board supports it.

Luckily, job boards like Smashing Magazine and a whole lot of others provide RSS feeds which we can hook right in to Zapier to automate getting an email whenever a new job is posted.

To get started, let’s create a new Zap, and this time, search for RSS and select **RSS by Zapier**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rss-by-zapier.jpg)
_Selecting RSS by Zapier_

For our **Trigger Event**, select **New Item in Feed**, then click **Continue**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-rss-new-feed-item.jpg)
_Setting New Item in Feed as Trigger Event_

At this point, we want to enter a feed URL. This will be the URL to the XML RSS feed that websites make available. For Smashing Magazine, you can find it here:

[https://www.smashingmagazine.com/jobs/feed](https://www.smashingmagazine.com/jobs/feed)

So enter that URL above into **Feed URL** (you can leave **Username** and **Password** blank), and keep **Different GUID** selected for **What Triggers A New Feed Item**. Then click **Continue**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-rss-feed-configuration.jpg)
_Setting RSS Feed URL_

Same as usual, now you can test the trigger to make sure it works. If the RSS feed is valid, this will be smooth, otherwise you might see an error. The above URL should be valid!

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-rss-found-feed-item-test.jpg)
_Testing the RSS feed_

Next, we need to choose what we want to do with the new item. Since we want it emailed, we can choose our email service, which in my case is Gmail.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-gmail.jpg)
_Selecting Gmail in Zapier_

For our action, we want to **Send Email**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-gmail-send-email-trigger.jpg)
_Setting Action Event as Send Email_

Next, you want to sign in to your account, similar to what we did with Google Cloud Print. This should be your Google account that you use Gmail with.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-sign-in-to-gmail.jpg)
_Sign in to Gmail_

Now when we customize our email, we want to include the following:

* **To:** wherever you want these sent to, probably the same account you signed into Gmail with
* **From:** select your Gmail account
* **From Name:** can be anything you’ll recognize, like I’ll use Colbybot
* **Subject:** can be whatever you’d like, but a helpful idea could be “New Job Alert:" followed by selecting the title from the dropdown selection
* **Body Type:** you can leave as Plain
* **Body:** I would recommend including all tokens you’ll find helpful including the Title, Description, and Link

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-gmail-email-configuration.jpg)
_Configuring job notification email_

Once you’re done configuring, you can hit continue. Then, similar to before, click **Test & Review**, and you should receive your test email.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-gmail-test-email.jpg)
_Test job alert email_

Finally if you’re happy with the configuration, turn on the Zap, and enjoy your job search!

## What else can you do?

### More Ideas

Here’s more ideas to get you moving in the right direction:

* **Post Tweets to Slack:** every time an account tweets or someone from a list of accounts tweets, post that tweet to Slack
* **File Github Bugs to Jira:** whenever someone tags a Github Issue with a label of “bug”, create a new ticket in Jira with that Issue details
* **Post RSS Items to Twitter:** do you write your own content? Set up an RSS feed to automatically post a tweet with your new blog post

### Not Google Assistant

The only thing that it’s missing for me right now is Google Assistant, otherwise I would have included some Zap ideas for that. [IFTTT](http://ifttt.com/) supports Google Assistant for simpler flows, but Zapier can get more powerful.

### Webhooks

Zapier supports web hooks — meaning you can really do whatever you want. Though this [is a premium feature](https://zapier.com/apps/webhook/integrations), you can set up some custom workflows based off of new data Zapier sees or accept requests that you post to trigger other automations.

## What's your favorite Zap?

Love hearing new creative ways to use Zapier. [Share with me on Twitter!](https://twitter.com/colbyfayock)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?️ Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

