---
title: How to Build a RESTful API with Authentication in 5 minutes — all from your
  command line (Part 1)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-27T10:24:38.000Z'
originalURL: https://freecodecamp.org/news/build-restful-api-with-authentication-under-5-minutes-using-loopback-by-expressjs-no-programming-31231b8472ca
coverImage: https://cdn-media-1.freecodecamp.org/images/1*r9V8K9siyS45bR95DLPQSA.gif
tags:
- name: api
  slug: api
- name: authentication
  slug: authentication
- name: Loopback
  slug: loopback
- name: Node.js
  slug: nodejs
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Niharika Singh

  If the title of this article excites you, then my friend, you’re about to achieve
  level 100 of satisfaction by the end. I’ll quickly go through the course of this
  article:


  What we are about to create: RESTful API which handles logs...'
---

By Niharika Singh

If the title of this article excites you, then my friend, you’re about to achieve **level 100** of satisfaction by the end. I’ll quickly go through the course of this article:

1. **What we are about to create:** RESTful API which handles logs of food items on a restaurant menu. The database used in the back-end will be MongoDB. (You can literally use any fricking database on this planet. There’s an exhaustive list of database connectors/non-database connectors supported by [LoopBack](https://loopback.io/) below.)
2. **What is LoopBack:** In extremely simple terms, it is highly extensible, open source Node.js framework used to create dynamic, end-to-end REST APIs very rapidly. APIs generated via LoopBack are Swagger APIs (world’s most popular API framework, and you’ll see why very soon). The front-end could be made in whichever framework you’re in love with; Angular or React.
3. **Creating application via CLI:** This is the WOW part which removes all the programming involved. LoopBack CLI is so beautiful that all the hours of development work are reduced down to seconds. Here, we’d be setting up our database using CLI.
4. **Creating data models via CLI:** Again, no programming. All via the beautiful CLI.
5. **Setting up Authentication via CLI:** If you have experience creating APIs, you know how tough it is to restrict parts of API using authentication. Setting up token-based authentication using Express+Node.js on the server side is a pain. All of that pain will be taken away by tasting the elixir of LoopBack! It is heaven’s own drink.

![Image](https://cdn-media-1.freecodecamp.org/images/iGHE28Ucn5MVvYyBssY3frS7FDU1HIUwo8AX)

#### Step by Step Guide:

**Pre-requisites:** Make sure you’ve got [Node.js](https://nodejs.org/en/), [Robomongo](https://robomongo.org/) installed and MongoDB server running.

#### **STEP 1: Install LoopBack CLI via NPM**

Open the terminal and write the following command to install LoopBack CLI so that ‘lb’ command can be accessed. Only through ‘lb’ command can we generate applications, models, data sources etc. For further reading: [https://loopback.io/doc/en/lb2/Command-line-tools.html#using-yeoman](https://loopback.io/doc/en/lb2/Command-line-tools.html#using-yeoman)

```
$ npm install -g loopback-cli
```

Make sure you install this globally, or else ‘lb’ command might not work for you.

#### **STEP 2: Creating Application**

Make a directory where you wish to store your project. I’ll name it ‘restaurant-menu’. Make sure you’ve opened this directory in your terminal so that all the files generated via LoopBack are stored in that folder.

Then enter the following command:

```
$ lb
```

A lot of questions will be asked, like those displayed in the image below.

![Image](https://cdn-media-1.freecodecamp.org/images/R0sLAcXrQXqn-zeUSfj9thykmF9YwRcYKCNa)
_This is what it should look like._

(To navigate among options, use arrow keys on your keyboard)

### **THE API IS CREATED!**

![Image](https://cdn-media-1.freecodecamp.org/images/rBQvFJ35WfSz3QdckTEmIqPc6KUZDzftWIBd)

I’m not kidding. Don’t believe me? Run the application using the following command:

```
$ node .
```

![Image](https://cdn-media-1.freecodecamp.org/images/rAYYNopW-YM9SyR51w47dU6VI2lEsF1Rto1U)

If you point to localhost:3000, you’ll see something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/yiv9xKmwl7OkCTdHmolz7o232lczz6KNBB6o)
_This will only tell you when the API was started and since how many seconds it has been up._

However, if you go to localhost:3000/explorer, you’ll see the gorgeous SwaggerAPI.

![Image](https://cdn-media-1.freecodecamp.org/images/nGKuHXxfQh-B85Ny9MIXh8GiXpyW7nSn6yCN)

LoopBack has set up all the routes for you:

GET users, POST users, PUT users, DELETE users, Login, Log out, Change Password. Literally everything! It would otherwise take hours of work to code this out.

Open this folder in any text editor. I’d be using Atom.

#### **STEP 3: Connecting MongoDB**

If you open `**datasources.json**` in the Server folder, you should see something like:

```json
{
  "db": {
    "name": "db",
    "connector": "memory"
  }
}

```

This means that presently, the data source being used is the memory of our computer. We’ve got to change this to Mongo. So let’s install mongo connector:

```
$ npm install --save loopback-connector-mongodb
```

Alongside, I hope mongod is running. This is how you’d know it is running:

```
2018-01-27T15:01:13.278+0530 I NETWORK  [thread1] waiting for connections on port 27017
```

Now, let’s connect the connector!

```
$ lb datasource mongoDS --connector mongoDB
```

This will ask a lot of questions as follows:

![Image](https://cdn-media-1.freecodecamp.org/images/-satN8CMcb23tpBD1cmouXNwjbr4gLG9ArWj)

Now modify `**datasources.json**` because we don’t wish to use memory. We wish to use Mongo.

```json
{
  "db": {
    "host": "localhost",
    "port": 27017,
    "url": "",
    "database": "food",
    "password": "",
    "name": "mongoDS",
    "user": "",
    "connector": "mongodb"
  }
}

```

So our database named: `**food**` is created.

#### **STEP 4: Creating Data Models**

Run following command to create data models:

```
$ lb model
```

![Image](https://cdn-media-1.freecodecamp.org/images/rhCkwWcP7f1SiI5ezMAvtdHhXU6eUllSB9pZ)

You may add however many properties to a particular model. To stop entering more properties, just hit Enter to get out of the CLI.

Check out `**dishes.json**` in the Common/Models folder.

```json
{
  "name": "dishes",
  "base": "PersistedModel",
  "idInjection": true,
  "options": { "validateUpsert": true },
  "properties": {
    "name": { "type": "string", "required": true },
    "price": { "type": "number", "required": true }
  },
  "validations": [],
  "relations": {},
  "acls": [],
  "methods": {}
}

```

You may edit the properties from this json file as well. It is not necessary to use CLI.

Now let’s rerun the server using the following command and head over to localhost:3000/explorer

```
$ node .
```

Now you’ll see 2 models: `**dishes**`, and `**user**`

![Image](https://cdn-media-1.freecodecamp.org/images/yiCcXdhwh6KmkvQ65H6KHvjskh9pbc9JbXbr)

Now let’s POST some `dish`.

![Image](https://cdn-media-1.freecodecamp.org/images/bncjurriEZN0SKiIdb7POrdOAocWlFjNAQHR)

Now let’s GET the same `dish`.

![Image](https://cdn-media-1.freecodecamp.org/images/38k0M-rkWNr5-x1UDVtS0L7w9IDFWd0ucxlv)

You may play around with other HTTP requests too!

These APIs can be accessed outside the explorer as well:

[http://localhost:3000/api/dishes](http://localhost:3000/api/dishes)

![Image](https://cdn-media-1.freecodecamp.org/images/w-Hiil7wjDNHghvGoW488BgOsHwBzgVEDs2T)

#### **STEP 5: AUTHENTICATION: Cherry on the cake!**

To set up authentication, run the following command:

```
$ lb acl
```

![Image](https://cdn-media-1.freecodecamp.org/images/bd94tNvvyNQzynur9S9CKyC-lSKoU8IKR2ye)

Now, let’s try to GET the `**dishes**`. Before that, please rerun the server.

![Image](https://cdn-media-1.freecodecamp.org/images/BeN7OxZjcmu7EcRwPvf0PRab8HRavKLx3ya9)
_So it doesn’t GET any dishes. As expected. Because we are not logged in. It alerts us by saying Authentication required._

Let’s get authenticated! For that, we need to get registered first. So we POST in `**users**`.

![Image](https://cdn-media-1.freecodecamp.org/images/IhYOhlb41zpLxsKOtVzX37Ji7dVriLKDv2Ln)

Now, let’s log in.

![Image](https://cdn-media-1.freecodecamp.org/images/hxCQm4xGEBEvevqPZtL6sgVN1mXoRV5tpj2u)

Now, copy the ID in the response body and paste it in the Access Token field on top of the page.

![Image](https://cdn-media-1.freecodecamp.org/images/NY830CQpK2jD-BMJ0gvbDAadX1KOGyC8fh-r)

Now we are authenticated. YAY.

Now, let’s GET the `**dishes**` again.

![Image](https://cdn-media-1.freecodecamp.org/images/DhkE4UiURk9UHLXBvwWBLlM2PoWjeZuWc5dM)

HOORAY!

Congratulations if you’ve successfully reached this step. So proud of you.

Next steps would be to create a front end around this API which would be done later.

![Image](https://cdn-media-1.freecodecamp.org/images/cJRJuth-oFUh34e3LYZXnP2dl75mFx3jHuPf)

#### The frontend tutorial of this article can be found [here](https://medium.freecodecamp.org/how-to-build-a-restful-api-with-authentication-in-5-minutes-all-from-your-command-line-part-2-dcf29d5de0bb). In that tutorial, I have used ReactJS to weave a frontend around this API.

Bye folks!   
Happy coding.

