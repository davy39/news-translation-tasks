---
title: Creating serverless Slack commands in minutes with Go & Up
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-11T00:39:48.000Z'
originalURL: https://freecodecamp.org/news/creating-serverless-slack-commands-in-minutes-with-up-f04ce0cfd52c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uFEp4Ubz5TOzlfo0-FE5Qw.png
tags:
- name: golang
  slug: golang
- name: Productivity
  slug: productivity
- name: serverless
  slug: serverless
- name: slack
  slug: slack
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By TJ Holowaychuk

  This post walks through the creation of a serverless Slack command written in Golang,
  and deployed to AWS Lambda in seconds with Up.

  You’ll be creating a /time <url> command used to check how long a website takes
  to respond. Up uses...'
---

By TJ Holowaychuk

This post walks through the creation of a serverless Slack command written in Golang, and deployed to AWS Lambda in seconds with [Up](https://github.com/apex/up).

You’ll be creating a `/time <url>` command used to check how long a website takes to respond. Up uses your own AWS account. You can host a large number of custom apps for free while still utilizing the AWS free tier (1 million requests/m).

Check out the [installation instructions](https://up.docs.apex.sh/) as well if you’re new to Up.

### Registering the Slack command

The first step is to create a Slack app, allowing you to register commands, among other things.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dE4mvNpvma_IM0UHxlC4qQ.png)

Once created, click “Slash commands” in the menu on the left, and register the `/time` command. You’ll need to keep this page open for a minute since we need a **Request URL** so Slack knows where to send requests.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9Ot1sxpiFdpxDYe4xZMOGg.png)

#### Creating the Slack command

In your project’s directory create a file named `up.json`. Make sure to replace `PROFILE` with your AWS profile name ([read more](https://apex.github.io/up/#aws_credentials)).

```
{  "name": "slack-cmd-test",  "profile": "PROFILE"}
```

Now we need a little HTTP server to process the Slack command POST request. Create a `main.go` file with the following net/http server.

Deploy it with `up` .

> **NOTE** : The first deploy may take roughly 60s to set up resources.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QuKc-ue1qJuwg9xt-NOlqQ.png)

Now you need to grab the URL and paste it into the Slack command page so Slack knows where to send requests. Copy the command’s URL to the clipboard using:

```
$ up url -cCopied to the clipboard!
```

Paste it in the **Request URL** field, then you’re good to give it a test run:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ht5Cs6Wcfqezwk0ChfC84g.png)

With any luck, you’ll see a Hello World response!

![Image](https://cdn-media-1.freecodecamp.org/images/1*fFywF9gQ3XNKRe-QYxRHLw.png)

#### Performing the request

Slack sends a POST request with form inputs, otherwise known as `application/x-www-form-urlencoded` (a tragically named mime type, turned standard-ish).

To access the form values, parse the form with the ParseForm() method. In this case all we need is the “text” field from r.Form, the parsed form.

Now that the request is portion is complete, import the `time` package and wrap the request with `time.Now()` and `time.Since()` to record the request duration.

Deploy again with `up` and immediately after the deploy you’re ready to test out the real version:

![Image](https://cdn-media-1.freecodecamp.org/images/1*WTFhC_dOxL3iqNTsQf6x3w.png)

Two files and a few commands later, you’re done! Repeat for as many Slack commands as you need.

### Testing locally

One of Up’s strengths is deploying traditional “vanilla” HTTP servers. This means there is nothing new to learn when testing on your machine, develop the app as you always would.

Here’s an example of this application tested via `curl` :

```
$ PORT=3000 go run main.go$ curl -d 'text=https://apex.sh' http://localhost:3000/
```

```
https://apex.sh took 19.33542m
```

Hope that was helpful! Check out the [documentation](https://apex.github.io/up/) for more help, and follow on [Twitter](https://twitter.com/tjholowaychuk) for updates and various software rants.

