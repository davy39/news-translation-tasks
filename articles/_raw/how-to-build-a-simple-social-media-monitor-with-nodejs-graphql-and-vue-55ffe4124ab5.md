---
title: How to build a simple social media monitor with NodeJS, GraphQL, and Vue
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-31T19:55:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-simple-social-media-monitor-with-nodejs-graphql-and-vue-55ffe4124ab5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*apsmd1svbRnvOh_Evak5nA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Paschal

  Introduction

  We’ll build a simple monitor that will track the number of people that followed
  us on specific dates, using Medium as the use case. This is just a bare prototype
  and can be done for any other social media or networking platfor...'
---

By Paschal

#### Introduction

We’ll build a simple monitor that will track the number of people that followed us on specific dates, using Medium as the use case. This is just a bare prototype and can be done for any other social media or networking platform.

In the end, we should have something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*IWAiDTjoSP9FrikYuvcvvA.png)

To achieve this, we will use the [node-imap](https://github.com/mscdex/node-imap) package. The two major protocols for handling emails are IMAP (Internet Messaged Access Protocol) and POP (Post office protocol). IMAP is preferred, because it always syncs with the mail server, hence the changes made on the mail client will appear immediately on the webmail inbox.

#### Prerequisites

* NodeJS
* VueJS
* A Gmail account

#### Setup the back-end with node-imap and apollo

Firstly, install the necessary packages.

```
npm i --save node-imap apollo-server mailparser
```

Now you can define the types and resolver and then run the apollo server.

A ‘**User**’ type that has the email and password string types as its schema has been defined, and a mutation called **‘imapMutation’** which receives the email and password from the user and then returns a response with the User type.

The resolver handles the mutation, and then you can work with the arguments sent from the client.

Now you can run the server.

You can then import the **node-imap** and **mailparser** modules. The **mailparser** module will be used to receive the mail responses as JSON.

```
const Imap = require('imap')const simpleParser = require('mailparser').simpleParser
```

You are going to create a ‘**connectImap’** function that will handle our IMAP functionality. From the [node-imap](https://github.com/mscdex/node-imap) documentation, you can get the skeleton of how the module works, and then copy and paste it into the code. It basically works with callbacks and emitters, so we’ll wrap it in a promise.

You should have something like this.

When the ‘**ready**’ event is called, we connect to our mail, and then we can search for messages. So, we’ll search for emails from the medium account that handles followers (**_noreply@medium.com_**).

Our ‘**_ready_**’ event should look like this.

We search for emails where each subject contains a ‘**_started following you_**’ substring. Then, we split the arrays with either a comma or the conjunction ‘and’ to get the number of followers, and then handle cases like ‘**_Peter and 3 others started following you_**’. After splitting the string above, we will have an output:

```
[  'Peter',  '3 others started following you']
```

The length of this array is **2**, so we have two followers. If the subject contains ‘**_others_**’, we take the digit behind it and add to the length of the array, which is **5** and then we subtract **1** to get rid of the ‘**_3 others started following you_**’ string. This leaves us with **4**.

Then, we resolve the promise when the ‘**_end_**’ event is fired (_imap.once(‘end’)_).

Since we will have to send the array to our apollo client, we will need to define the type of the ‘**_graphPoints_**’ array.

Our type definitions should look like this:

We added the **data** key to the ‘**_User_**’ type, which will hold the ‘**_graphPoints_**’ value, and its type is an array of objects with the ‘**_Graph_**’ type.

Finally, we handle the resolver, which will get the email and the password of the user and then return the **email** and the data (**_graphPoints_**).

If we log the **user** object, our structure should be something like this:

```
email: String,data: [ { numberOfFollowers: 1, date: 2017-07-05T07:53:18.000Z },        { numberOfFollowers: 1, date: 2017-07-07T19:34:57.000Z }      ]
```

#### Setup the front-end with v-charts and apollo client

Now, we want to get the data sent from the server and plot the chart with the [v-charts](https://www.npmjs.com/package/v-charts) module.

But first, we install our dependencies.

```
npm install --save vue-chartjs vue-apollo apollo-client apollo-link-http apollo-cache-persist apollo-cache-inmemory graphql graphql-tag moment
```

I know what you’re thinking — that’s a lot of dependencies. If you have troubles setting up a Vue project, you can find out how to do that [here](https://cli.vuejs.org/guide/creating-a-project.html#vue-create). We should also include [vuetify](https://vuetifyjs.com/en/getting-started/quick-start) and the [vue-router](https://router.vuejs.org/installation.html#direct-download-cdn) if we want to style the project and create additional routes.

In our ‘**_src_**’ folder, we can create a ‘**_config_**’ folder. The structure should look like this:

```
|src  |config     -graphql.js     -index.js     -LineChart.js  |pages      -login.vue  |router      -index.js  App.vue  main.js
```

We will have to set up our graphql client in the **_src/config/index.js_** file.

Make sure the **_uri_** is on the same port as your apollo server, by default the apollo server runs on port **4000**. Our apollo client is then set up with the _httpLink_ and the _cache_.

The **_src/config/graphql.js_** file should look like this:

This query will submit the **email** and the **password** of the user to the imapMutation and then get the **email** and the **data**(graphPoints) from the apollo server.

Then, we create our chart component in the **_src/config/LineChart.js_** file. We can use charts ranging from bar charts to histograms. A line chart was used in this example.

We can import the ‘**_vue-apollo_**’ package in our main.js file and include the **apolloProvider** when initializing the app.

Finally, we will set up the **src/pages/login.vue** file, which we should have configured as the component for the default home route ‘/’ in the **src/router/index.js** file.

So we created a basic form that accepts the email and password of the user and then send this data to the server through the **_signup()_** method. The **_plotGraph()_** method loops through the response(graphPoints) and pushes the dates to the labels array and the number of followers to the data array.

After styling using the ‘**_options_**’ object, we should have something like the screenshot shown during the introduction to this project.

#### Conclusion

You can still do more with your personal project, but the aim of this was to show how to work with the node-imap package, and how apollo works as a server and as a client. If you had any problems with this project, you can leave a comment or send a message on [Twitter](https://twitter.com/_Obbap).

You can try the live version of [this](https://medium-followers.netlify.com/), or you could check out the repositories for the [client](https://github.com/obbap1/MonitorFollowers_frontend) and [server](https://github.com/obbap1/MonitorFollowers_backend) applications on GitHub.

If you want to learn new technologies and frameworks, you can do so [here](https://www.microverse.org/) and if you learned anything at all, please do well to clap below.

_I will like to thank [Wes Wagner](https://www.freecodecamp.org/news/how-to-build-a-simple-social-media-monitor-with-nodejs-graphql-and-vue-55ffe4124ab5/undefined) for his feedback in making this article._

Thanks!

![Image](https://cdn-media-1.freecodecamp.org/images/1*SRAIx1jmXTBHByfDCOtZig.png)

