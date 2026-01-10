---
title: How To Setup Your Own Disposable Email Server
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-13T09:39:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-your-own-disposable-email-server-b4cfd297afa7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*--gyEd4Bg3ZTAwGztCg8_Q.png
tags:
- name: email
  slug: email
- name: Node.js
  slug: nodejs
- name: software development
  slug: software-development
- name: Software Testing
  slug: software-testing
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Oren Geva

  Disposable email services are online services that provide temporary email addresses
  for registering or signing up on websites that require email verification.

  The purpose of these services is that you can avoid exposing your own email a...'
---

By Oren Geva

Disposable email services are online services that provide temporary email addresses for registering or signing up on websites that require email verification.

The purpose of these services is that you can avoid exposing your own email address to potential SPAM, especially if you just need the service for a short period of time.

Disposable email services are also useful in software development and testing, as many software products require email verification themselves. Using real email addresses in the context of software development or testing is cumbersome and annoying. Many teams around the world use temporary disposable email services for testing their own software products.

[AHEM - Ad Hoc Email](https://www.ahem.email) is one of these services. You can send an email to an @ahem.email address and check the [AHEM](https://www.ahem.email) mailbox to retrieve and read the email.

Many similar services such as [Mailinator](http://www.mailinator.com/), [ThrowAwayMail](https://www.throwawaymail.com/), [Temp-Mail](https://temp-mail.org) and [Yopmail](http://www.yopmail.com) are available online to name a few.

Each has their own interpretation of the theme, but one of the things that makes [AHEM](https://www.ahem.email) unique is that [AHEM’s](https://www.ahem.email) code is [freely available on GitHub](https://github.com/o4oren/Ad-Hoc-Email-Server) as open source, allowing a user to download and set up their own temporary mail server.

But why would someone want to set up their own disposable mail server? In the context of software testing, while most of the time an online disposable email service is sufficient, on some occasions you might want to host a temporary email server on site:

* Some organizations block access to disposable emails, or even just unknown websites
* Some QA labs do not offer external Internet access
* Some products require multiple or controllable email domains tested

[AHEM](https://www.ahem.email) caters to all these needs and more.

To install [AHEM](https://www.ahem.email), you’ll need a Linux or Windows machine with administrative rights and Node.js version 8.9+ as well as MongoDB installed.

Setting up Node.js, npm and MongoDB is out of the scope of this guide, but in case you’re lost, detailed information on how to set them up can be found on the [Node.js download](https://nodejs.org/en/download/) and [MongoDB download](https://www.mongodb.com/download-center/community) pages.

### Installing AHEM

The following section details the steps required to install and run [AHEM disposable mail](https://www.ahem.email) server. [AHEM](https://www.ahem.email) can run on any system supporting Node.js.  
These steps were performed and tested on an Ubuntu Linux server and may need slight modifications to be compatible with other systems.

#### **Install Angular CLI**

[AHEM](https://www.ahem.email) uses Angular for its front end delivery, so you will need to globally install angular-cli:

```
npm install -g @angular/cli
```

#### Install Concurrently

Concurrently is a JavaScript library that allows running multiple scripts concurrently. In this configuration, [AHEM](https://www.ahem.email) uses Concurrently to run both the backend node API and email server, and serve the front end directly via angular-cli:

```
npm install -g concurrently
```

#### Clone the AHEM GitHub Repository

```
git clone https://github.com/o4oren/ahem-server.git
```

#### Install Dependencies within the Created Folder

```
cd ahem-servernpm install
```

#### Update Configuration

A configuration file named properties.json is located in the root of the project. Edit it to suit your preferences.

```
vim properties.json
```

The properties.json file will look something like this:

Here is an explanation of the parameters within the properties file:

* **serverBaseUri** - the base address for your API server.
* **mongoConnectUrl** - the mongodb connect url.   
Example: “mongodb://localhost:27017/ahem”.
* **appListenPort** - the port the node app binds to.
* **smtpPort** - the SMTP server’s port. Note that by default it is set to 2525 — this is done for testing purposes, as on many systems only a system account can listen on port 25. To receive standard SMTP email, change this to 25.
* **emailDeleteInterval** - The time in seconds between age checks for purging old emails.
* **emailDeleteAge** - The max age in seconds above which emails will be deleted.
* **allowedDomains** - An array of allowed email domains. These domains will be allowed by the server as RCPT TO: entries. This also makes the server not act as an open relay. Format: [“my.domain.com”, “my.second-domain.com”].
* **customText** - A html string that will replace the default text in the landing page.
* **allowAutocomplete** - If set to false, will prevent auto completing users in the UI.

#### **Build the project**

```
npm run build:ssr
```

This may take a while…

#### Run AHEM

At this point, make sure your MongoDB server is up and running and that your properties.json file was configured correctly.

The easiest way to run AHEM, is run the project with the command:

```
node ahem.js
```

This command will start (by default) the backend server on port 3000 and the front end will run on port 4200. You can then access the [AHEM](https://www.ahem.email) web interface at [http://localhost:4200.](http://localhost:4200.)

Clap or star the [GitHub Repo](https://github.com/o4oren/Ad-Hoc-Email-Server) if you find this useful!

