---
title: How to Create an AI-Powered Bot that Can Post on Twitter/X
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2025-04-23T18:27:44.353Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-ai-powered-bot
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745416845372/5eb9963d-e092-4844-99d9-01fa70032169.png
tags:
- name: automation
  slug: automation
- name: AI
  slug: ai
- name: bot
  slug: bot
- name: Twitter
  slug: twitter
- name: gemini
  slug: gemini
seo_title: null
seo_desc: 'These days, everyone wants to be a content creator. But it can be hard
  to find time to create and curate content, post on social media, build engagement,
  and grow your brand.

  And I’m not an exception to this. I wanted to create more content, and had ...'
---

These days, everyone wants to be a content creator. But it can be hard to find time to create and curate content, post on social media, build engagement, and grow your brand.

And I’m not an exception to this. I wanted to create more content, and had an idea based on something I’ve observed. I subscribe to a few technology newsletters, and I read lots of updates every day about the tech ecosystem. But I’ve noticed that many of my peers often don’t seem to be aware of this news. So, I decided to post my top three news stories (especially about AI) on my Twitter/X account every day.

I did this for a couple of weeks, but after that I couldn’t find the time to keep it going. So, I did some research into how I could automate the process, and I found a solution. In this guide, I’ll explain the process so you can use it, too.

By the end of this tutorial, you’ll have created your own AI bot that:

* Fetches data from an API or crawls a webpage
    
* Processes the data using AI
    
* Posts the results on Twitter/X
    

And the great thing: this entire process is automated.

## Table of Contents

* [Prerequisites](#heading-prerequisites)
    
* [How to Build the Bot](#heading-how-to-build-the-bot)
    
    * [Step 1: Generate the Twitter API Key](#heading-step-1-generate-the-twitter-api-key)
        
    * [Step 2: Generate Access Token and Secret](#heading-step-2-generate-access-token-and-secret)
        
    * [Step 3: Generate an API Key in Google Gemini](#heading-step-3-generate-an-api-key-in-google-gemini)
        
* [Node.js Project Setup](#heading-nodejs-project-setup)
    
    * [Step 1: Fetch Data from the API](#heading-step-1-fetch-data-from-the-api)
        
    * [Step 2: Upload the Data as a File to Gemini API](#heading-step-2-upload-the-data-as-a-file-to-gemini-api)
        
    * [Step 3: Prompt Gemini to Get the Latest AI News](#heading-step-3-prompt-gemini-to-get-the-latest-ai-news)
        
    * [Step 4: Post Using the Twitter/X API](#heading-step-4-post-using-the-twitterx-api)
        
    * [Step 5: Delete the File Uploaded in the Gemini API](#heading-step-5-delete-the-file-uploaded-in-the-gemini-api)
        
    * [The Result](#heading-the-result)
        
* [Conclusion](#heading-conclusion)
    

## Prerequisites

Before we begin creating a bot, you’ll need to have the following setup and tools ready to go:

* [NodeJS](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs) - A simple NodeJS app to code the bot
    

You’ll also need some API keys, secrets, and tokens. So, you’ll need to have the following accounts created:

* [Twitter Developer](https://developer.x.com/) – To generate the Twitter/X API keys, secrets, and tokens
    
* [Google AI Studio](https://aistudio.google.com/) – To generate the Gemini API key
    

## How to Build the Bot

There are a number of steps I’ll walk you through to build your bot.

We’ll start by generating an API Key and Secret so we can use the Twitter/X API. Then we’ll generate an access token and access token secret with “Read and Write” permissions that’ll be able to post in your account. After that we’ll generate an API Key in Google Gemini (we’ll be using the Gemini API to process the data).

With all that taken care of, we’ll start working on the Node.js app. The app will be able to fetch data from an API, process the data using AI, and then post that data in the form of tweets on Twitter/X.

Finally, we’ll automate the entire process and schedule it to run daily.

### Step 1: Generate the Twitter API Key

1. Navigate to [Twitter Developer Website](https://developer.x.com/).
    
2. Click on the “Developer Portal” in the top right:
    
    ![Image showing developer portal highlighted](https://cdn.hashnode.com/res/hashnode/image/upload/v1745152618491/214fe6d6-b699-40bb-8ac0-533b0c72b927.png align="center")
    
3. Signup using your account.
    
4. You’ll be asked to fill out a form asking how will you use the Twitter API, and a few basic details. It may take up to 24 hours to get approved. But, it’s approved instantly for me.
    
    ![Form asking how you'll use the Twitter API](https://cdn.hashnode.com/res/hashnode/image/upload/v1745152170917/d2c2ba21-f3f5-4bc6-bdd5-58d222e203e6.png align="center")
    
5. After login, Navigate to "Projects and Apps" and under “Overview” click on "Create App":
    
    ![Create App screen](https://cdn.hashnode.com/res/hashnode/image/upload/v1745153184830/1a731639-0df2-47e3-baf2-3633e1735a69.png align="center")
    
6. Enter a name for your app and click “Next” to proceed with creating your app. At the end, you’ll be shown your API Key and Secret. Don’t copy that now.
    
7. Click on the project you created from the left side drawer and click on the "Edit" option in “User authentication settings” section.
    
    ![Editing the user authentication settings section](https://cdn.hashnode.com/res/hashnode/image/upload/v1745153746932/002f3b38-5aaf-43ef-8d7c-0368f141524f.png align="center")
    
8. Select “Read and Write” in App Permissions section, “Web App, Automated App or Bot” in Type of App section, and enter your website URL (it can be any URL including http://localhost) in the “Callback URI” and “Website URL”. Then hit “Save”.
    
9. Go to “Keys and tokens” tab.
    
10. Click on “Regenerate” button in “API Key and Secret” section.
    
11. Copy and save the API Key and Secret somewhere securely.
    

### Step 2: Generate Access Token and Secret

1. Go to “Keys and tokens” tab.
    
2. Click on “Generate” or “Regenerate” button in “Access Token and Secret” section.
    
3. Copy and save the Access Token and Secret somewhere securely.
    
    ![Generating or regenerating keys and tokens](https://cdn.hashnode.com/res/hashnode/image/upload/v1745154373207/4309dbcc-1081-46b7-be71-5babf950eae0.png align="center")
    

### Step 3: Generate an API Key in Google Gemini

1. Navigate to [Google AI Studio](https://aistudio.google.com/).
    
2. Login to your account.
    
3. Click on “Get API Key” button at the top right.
    
4. Click on “Create API Key” button.
    
    ![Create API screen](https://cdn.hashnode.com/res/hashnode/image/upload/v1745154646809/54c4fa1a-097e-4bf6-8a5f-229c01845d28.png align="center")
    
5. Copy and save the API Key somewhere securely.
    

Alright, we are done with creating the necessary API Keys and Secrets for our project. Let’s put on our coding shoes.

## Node.js Project Setup

There are 5 major steps for this part of the project. They are:

1. Fetch data from the API
    
2. Upload the data as a file to Gemini API
    
3. Prompt Gemini with the uploaded file to get the latest AI news
    
4. Post news to Twitter/X using their API
    
5. Delete the file uploaded in Gemini API
    

These are just the snippets of code that can be assembled together to run this project.

### Step 1: Fetch Data from the API

In my case, I’ll be using `techmeme.com` to get the latest news. But this site does not offer an API. So, I’ll be downloading the HTML of this site.

%[https://gist.github.com/arunachalam-b/b204531fbfda5e805202b5f5ab5aa55d] 

In the `User-Agent` header, we pass the value that mimics a browser user agent to avoid potential blocks.

### Step 2: Upload the Data as a File to Gemini API

Now we need to store this HTML in a separate file. We cannot directly pass the HTML code in the prompt to the Gemini API, as it’ll result in an error. This is because Gemini accepts only a limited number of tokens in this API. The HTML code of any website will always result in huge number of tokens. So, we’ll create a separate file.

Upload the file to the Gemini API. Refer to the file id in the prompt to Gemini.

%[https://gist.github.com/arunachalam-b/5ebfed570c79a0f0faa8c4e42559c673] 

### Step 3: Prompt Gemini to Get the Latest AI News

Let’s write a prompt to Gemini asking it to generate top news by referring to the HTML file provided. We’ll ask it to provide a headline, short description, URL, and three relevant hashtags for each tweet. We’ll also give some example data of how it should look. We’ll ask it to generate a structured response by providing the format of the JSON that we want the output to be.

You can use whatever model you want to, but I’ll be using the `gemini-2.5-pro-exp-03-25` model for this use case. I’m using this model because we need a thinking model that thinks and picks the correct top news – not just one that predicts the next token/word. The Gemini 2.5 Pro model best qualifies for this.

%[https://gist.github.com/arunachalam-b/466449de313bcbc4241eaf3b6e1646a7] 

### Step 4: Post Using the Twitter/X API

Here’s the core of our app. We need to post all the tweets we received from Gemini. We’ll be posting the tweet as a thread. This means that the first tweet will be the root tweet and subsequent tweets will be in the comments of the prior tweet. This makes it a thread.

To do this, we’ll take the id of each tweet after it’s posted and pass it on to the next tweet as a reference. One additional thing to note here is, after each successful tweet, we’ll give a pause of 5 seconds before posting the next tweet. There are few reasons for doing it this way.

1. When any script runs, it usually runs at a much higher speed (usually in milliseconds). So, the second tweet may get posted before the first tweet was posted (maybe due to some poor internet connection). Also, I believe Twitter implements some queue system which may quickly process the second tweet before your first. So it’s always better to leave a small gap – if not 5 seconds then at least 1 second
    
2. Twitter may have implemented some rate limiting mechanism. So if there are multiple request received from a same IP within a short time frame, they may block the IP and consider your account as spam.
    
3. Since we’re using a Free tier API, we are limited to 1500 tweets per month. If you’ve paid for this API, you won’t have to worry about this (since you’ll have a higher limit and the rate limiting mechanism –refer to point #2 – might not be applicable). All of this depends on their [pricing](https://docs.x.com/x-api/introduction#access-levels), so just refer to that and make your call accordingly.
    

I’m using the free tier, and since it’s a hobby project, having a 5 seconds wait time makes sense. I have not faced any issues so far with this.

%[https://gist.github.com/arunachalam-b/b049fda9e567bc68c7fb33de0ce67cd3] 

### Step 5: Delete the File Uploaded in the Gemini API

After posting all the tweets, it’s time to clean up the system. The only thing we need to do as a clean up is delete the uploaded file. It’s always a best practice to remove an unused file that’s no longer needed. And since we’ve already posted the tweets, we no longer need that file. So, we’ll be deleting it in this step.

%[https://gist.github.com/arunachalam-b/741c5b13603187c76905f7b349661293] 

That’s it. We’re all done. You just need to copy these blocks of code into an `index.js` file and install some dependencies into the project and you should be good to go.

To make this even more simple, I have created a repo and made it public. Here’s the [Github repo URL](https://github.com/arunachalam-b/existential-crisis-alert-bot). You just need to clone the repo, install the dependencies, and run the `post` command

```plaintext
git clone https://github.com/arunachalam-b/existential-crisis-alert-bot.git
cd existential-crisis-alert-bot
npm i
```

Create a .env file and update your API keys and secrets in that file:

```plaintext
GEMINI_API_KEY=
TWITTER_API_KEY=
TWITTER_API_SECRET=
TWITTER_ACCESS_TOKEN=
TWITTER_ACCESS_TOKEN_SECRET=
```

Run the following command to post the latest AI news to your account:

```plaintext
npm run post
```

### The Result

Here’s a sample output of that command:

![Output](https://cdn.hashnode.com/res/hashnode/image/upload/v1745169397786/14e08ef8-dba5-45e0-a5d5-f3c6135c6347.png align="center")

You can modify the code/prompt to fetch data from a different API and post the top results in your Twitter account.

## Conclusion

I hope you now understand how you can automate a slightly complex process using AI and some APIs. Just note that this example is not completely automated. You still have to manually run the command everyday to post the tweets.

But you can automate that process as well. Just drop me a message if you wish to know about that. That topic itself deserves to be a separate tutorial. Also, I would request that you give a star for my project if you enjoyed this tutorial.

Meanwhile, you can follow my [Twitter/X account](https://x.com/AI_Techie_Arun) to receive the top AI news everyday. If you wish to learn more about automation, subscribe to my email newsletter ([https://5minslearn.gogosoon.com/](https://5minslearn.gogosoon.com/?ref=fcc_automated_tweet)) and follow me on social media.
