---
title: How to Build a ChatGPT Plugin – Case Study using PodcastAPI.com and Serverless
  Cloudflare Pages
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-22T23:01:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-chatgpt-plugin-case-study
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/56ae8d3bf6a04a8b85c96c695f29643f.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: chatgpt
  slug: chatgpt
- name: plugins
  slug: plugins
seo_title: null
seo_desc: "By Wenbin Fang\nChatGPT is a highly intelligent auto-completion tool. It\
  \ takes instructions or questions in natural language and provides good enough text-based\
  \ outputs. \nBut there’s a catch — ChatGPT’s knowledge only goes up until September\
  \ 2021. So,..."
---

By Wenbin Fang

[ChatGPT](https://chat.openai.com/) is a highly intelligent auto-completion tool. It takes instructions or questions in natural language and provides good enough text-based outputs. 

But there’s a catch — ChatGPT’s knowledge only goes up until September 2021. So, as of writing this blog post (June 2023), the model itself is not aware of any events or data after September 2021.

![Image](https://production.listennotes.com/web/image/5d9ab8edda604b2398d113fd45044b1d.png)

Here is where [ChatGPT plugins](https://openai.com/blog/chatgpt-plugins) come to the rescue. These plugins allow ChatGPT to interact with external APIs to gain access to up-to-date information. They can also help ChatGPT perform certain actions like triggering a Zapier task or sending an email.

From the perspective of an API provider (like [Listen Notes](https://www.listennotes.com/) providing [PodcastAPI.com](https://www.podcastapi.com/)), creating a ChatGPT plugin is similar to providing a user-friendly, AI-powered interface for your API. For enthusiastic users of ChatGPT, building custom plugins can extend its use cases significantly.

In this tutorial, we’ll leverage a real-world example of the [Listen Notes ChatGPT plugin](https://ai.listennotes.com/) (already available on the Plugin store) as a case study to illuminate the process of creating a ChatGPT plugin. 

The process is simpler than you might assume. By the end of this article, you should have the necessary understanding to employ any APIs and craft your very own ChatGPT plugin.

Feel free to try out the [Listen Notes ChatGPT Plugin](https://ai.listennotes.com/) and explore the source code [on GitHub](https://github.com/ListenNotes/listennotes-chatgpt-plugin).

## **How Do ChatGPT Plugins Work?**

For an end user, the process of using a ChatGPT plugin is quite straightforward. You just need to activate the plugin on the ChatGPT user interface, and then type in the prompts.

![Image](https://production.listennotes.com/web/image/f8dcb56eeedb4b7bb810ddfc64a97028.png)
_Example of a ChatGPT plugin at work_

For developers, the process requires some more work. You'll need to provide a hosted **ai-plugin.json** file using your own domain name. This file includes metadata about the plugin and an OpenAPI specification detailing the available API endpoints that ChatGPT can interact with. 

Essentially, a ChatGPT plugin is a smart API caller. The user employs natural language to call these external APIs instead of writing code. All the API endpoints, as well as the **ai-plugin.json** and **openapi.json**, should be hosted under the same domain name.

## **Case study: How to Build a Podcast Discovery ChatGPT Plugin using PodcastAPI.com and Cloudflare Pages**

### **Requirements**

Our plugin should be able to search for podcasts or episodes based on keywords, languages, countries, and audio length, among other factors.

We'll use PodcastAPI.com and Cloudflare Pages to build this ChatGPT plugin.

[PodcastAPI.com](https://www.podcastapi.com/) is a widely used Podcast API globally, and it powers [thousands of podcast apps/websites](https://www.listennotes.com/api/apps/). It’s a typical RESTful API. 

For example, to find podcasts related to “startup” in English, you send an API request like **GET /search?q=startup&type=podcast&language=English**. You can easily try out all of Podcast API endpoints with the mock server and see how the response JSON data look like [on the API docs page](https://www.listennotes.com/api/docs/?test=1).

[Cloudflare Pages](https://pages.cloudflare.com/) is a serverless platform with a generous free quota. It allows you to build a dynamic web app in JavaScript and send requests to external APIs securely without exposing API credentials. And since it’s serverless, you don’t need to worry about server provisioning, scalability, or operational issues. 

We’ve gained some experience using Cloudflare Pages from building [microfeed](https://www.microfeed.org/) — a lightweight serverless WordPress alternative, which you can use to host podcasts and media files for free.

### **How does the plugin work exactly?**

You can find the source code for the Listen Notes ChatGPT plugin on GitHub: [github.com/ListenNotes/listennotes-chatgpt-plugin](http://github.com/ListenNotes/listennotes-chatgpt-plugin).

The plugin, built with JavaScript, is deployed as a web app on the serverless platform Cloudflare Pages. This deployment serves three vital resources under the custom domain name ai.listennotes.com:

1. The **ai-plugin.json** file: This can always be found at [https://ai.listennotes.com/.well-known/ai-plugin.json](https://ai.listennotes.com/.well-known/ai-plugin.json). The path for this file is static and should not be changed. [Here](https://github.com/ListenNotes/listennotes-chatgpt-plugin/blob/main/functions/.well-known/ai-plugin.json/index.js) is the source code for your reference.
2. The **openapi.json** file: This location is determined by the **ai-plugin.json file**. In our case, it’s hosted at [https://ai.listennotes.com/chatgpt-plugin/openapi.json](https://ai.listennotes.com/chatgpt-plugin/openapi.json). You can check out the source code [here](https://github.com/ListenNotes/listennotes-chatgpt-plugin/blob/main/functions/chatgpt-plugin/openapi.json/index.js).
3. Proxy API endpoints: For example, https://ai.listennotes.com/api/v2/search_episodes. These are essentially thin wrappers of the actual PodcastAPI.com endpoints. The source code for these endpoints can be found [here](https://github.com/ListenNotes/listennotes-chatgpt-plugin/tree/main/functions/api/v2).

So, how do these pieces work together? Let’s delve deeper:

Firstly, ChatGPT identifies the **ai-plugin.json** file from its fixed path **/.well-known/ai-plugin.json**. This file contains essential metadata about the plugin and informs ChatGPT about the location of the **openapi.json** file. Here's what that looks like:

![Image](https://production.listennotes.com/web/image/439e931c7a7e460f834d3b2cdda20c19.png)

Secondly, ChatGPT uses the **openapi.json** file to understand the available API endpoints and their parameters. This file essentially helps ChatGPT understand how to interact with the API.

![Image](https://production.listennotes.com/web/image/89307fbe9bb541cfab24f4a879f69856.png)

Finally, using the description and other metadata specified in the **openapi.json** file, ChatGPT can translate natural language prompts into specific API requests. 

For example, a user's prompt like "search startup podcasts in English" is translated by ChatGPT into a GET request to **GET /search_podcasts?q=startup&language=English**.

### Securing the Keys to the Kingdom

When working with external APIs, like PodcastAPI.com in our case, an important concern is maintaining the confidentiality of API keys. You can do this through layers of indirection — “All problems in computer science can be solved by another level of indirection.” :)

Firstly, the real API key (**LISTEN_API_KEY** in our case) is provided as an environment variable on Cloudflare Pages. This ensures that the API key is never exposed in the source code.

Next, we utilize a secret (**CHATGPT_SECRET** in our case) for ChatGPT to call our proxy API endpoints. When submitting the plugin to ChatGPT, you will be prompted to provide this secret.

After providing the secret, ChatGPT will issue a verification token (**CHATGPT_VERIFICATION_TOKEN** in our case), which is placed in the ai-plugin.json file. It’s perfectly fine for this verification token to be public.

In our case, the **LISTEN_API_KEY**, **CHATGPT_SECRET**, and **CHATGPT_VERIFICATION_TOKEN** are all stored as encrypted environment variables on Cloudflare Pages, effectively kept out of the public eye:

![Image](https://production.listennotes.com/web/image/5c9e02cdc2984f2993e033c1acda7b9c.png)

### How to Navigate the Review Process

Before your plugin is listed in the ChatGPT Plugin store, you can test it via your custom domain (in our case, ai.listennotes.com).

When you’re ready to submit your plugin for review, you’ll do so via an Intercom ticket. You’ll need to answer several questions and provide some example prompts. From our experience, it took around 2 days for a ChatGPT team member to review our ticket.

Initially, our submission was rejected because our description did not end with punctuation. We promptly added a period to our ai-plugin.json’s description, resubmitted, and were approved within 2 hours. So, from submission to approval, it was roughly a 2-day process.

## **How to Adapt the Process for Other APIs**

If you wish to adapt [the listennotes-chatgpt-plugin repository](https://github.com/ListenNotes/listennotes-chatgpt-plugin) to work with other APIs, there are three main areas you’ll need to modify:

1. Update **ai-plugin.json** ([source code](https://github.com/ListenNotes/listennotes-chatgpt-plugin/blob/main/functions/.well-known/ai-plugin.json/index.js)): You’ll find more details on this at [openai.com](https://platform.openai.com/docs/plugins/getting-started/plugin-manifest).
2. Update **openapi.json** ([source code](https://github.com/ListenNotes/listennotes-chatgpt-plugin/blob/main/functions/chatgpt-plugin/openapi.json/index.js)): This is crucial as ChatGPT relies on this OpenAPI spec to identify available proxy endpoints. For more insights, check out [openai.com](https://platform.openai.com/docs/plugins/getting-started/openapi-definition).
3. Update proxy API endpoints ([source code](https://github.com/ListenNotes/listennotes-chatgpt-plugin/tree/main/functions/api/v2))to align with other APIs: The proxy endpoints that run on Cloudflare Pages need to be updated to send API requests to your chosen APIs. You may want to familiarize yourself with [how Cloudflare Pages functions work](https://developers.cloudflare.com/pages/platform/functions/get-started/).

After making these updates, you can [deploy to Cloudflare Pages](https://github.com/ListenNotes/listennotes-chatgpt-plugin#deploying-to-production) and then [submit your plugin to ChatGPT for review](https://platform.openai.com/docs/plugins/review).

## Wrapping Up

While this overview aims to provide useful information, keep in mind that the ChatGPT plugin is still in beta and subject to change. 

We hope to keep this post updated as changes arise. The world of AI is fast-paced, but with a solid understanding of these principles, you’ll be well-equipped to navigate it.

You can find this article and many others on [listennotes.com](https://www.listennotes.com/blog/how-to-build-a-chatgpt-plugin-a-case-study-using-78/).

