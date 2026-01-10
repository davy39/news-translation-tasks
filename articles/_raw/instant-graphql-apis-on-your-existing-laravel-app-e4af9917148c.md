---
title: How to get instant GraphQL APIs on your existing Laravel app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-27T16:16:05.000Z'
originalURL: https://freecodecamp.org/news/instant-graphql-apis-on-your-existing-laravel-app-e4af9917148c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q3KiCaC7_bynx8CfVlTXNw.jpeg
tags:
- name: api
  slug: api
- name: GraphQL
  slug: graphql
- name: Laravel
  slug: laravel
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Karthikeya Viswanath

  TL;DR


  Setup GraphQL engine — Install Hasura GraphQL engine and expose tables over a GraphQL
  API

  Authentication and Securing your GraphQL Server

  Migrations


  In this post, we’ll use the Hasura GraphQL Engine to get instant Grap...'
---

By Karthikeya Viswanath

#### TL;DR

* [**Setup GraphQL engine**](#8668) — Install Hasura GraphQL engine and expose tables over a GraphQL API
* [**Authentication and Securing your GraphQL Server**](#9050)
* [**Migrations**](#6d18)

In this post, we’ll use the [Hasura GraphQL Engine](https://hasura.io) to get instant GraphQL APIs on my existing Laravel app running locally.

For the purpose of this project, we’ll be using a sample Laravel ToDo app built using Laravel 5.1, and modifying the code to integrate HGE. (Please note though, that Laravel 5.1 has already reached End of Life in June 2018, and you should migrate to a newer version if you’re still using this.)

You can find the initial sample app [here](https://github.com/milon/laravel-todo), the final repository [here](https://github.com/hasura/laravel-todo-hge), and a live app for you to test out [here](http://laravel-todo-hge.herokuapp.com/).

This is what the our planned architecture will look like:

![Image](https://cdn-media-1.freecodecamp.org/images/1*hEit6SqjtIbh0gdYFE0cGw.png)
_Architecture before and after integration with HGE_

### Setup GraphQL Engine

[Hasura GraphQL engine](https://hasura.io/) (HGE) gives you an instant realtime GraphQL API on top of your existing Postgres. HGE works out of the box with your existing:

* [**Postgres database**](#f087) **—** Connects with your existing database and provides a GraphQL API to your database.
* [**Authentication system**](#9050) **—** Connects with your existing authentication system to secure GraphQL API.
* [**Migration system**](#50e3) **—** Hasura GraphQL Engine doesn’t interfere with the existing Laravel migration system. Schemas can be managed separately in Laravel as long as it doesn’t alter the schema tracked by the GraphQL Engine. More info on how Hasura GraphQL engine manages your schema state [here](https://docs.hasura.io/1.0/graphql/manual/engine-internals/index.html).

Also it comes with a nifty console, with GraphiQL integrated, which is useful while debugging GraphQL APIs.

### Installation

Hasura GraphQL engine can be installed on Heroku using the button below

![Image](https://cdn-media-1.freecodecamp.org/images/1*dcgu-klnpwTWilYiGMdM6Q.jpeg)
_Click this button to deploy the GraphQL engine to Heroku_

or on any machine which can run Docker. Checkout the [getting-started](https://docs.hasura.io/1.0/graphql/manual/getting-started/index.html) section for more info.

For the sake of this tutorial, we’ve set up a HGE instance for our Laravel app [here](https://hge-laravel-todo.herokuapp.com/console) (use the access-key `helloworld` , we’ll explain how it works below).

#### [Installation using Docker](https://docs.hasura.io/1.0/graphql/manual/deployment/docker/index.html)

Before installing the Hasura GraphQL Engine, you’ll need a postgres connection string. You can get this from your `config/database.php` file, or your `.env` file, wherever your storage credentials are kept.

Putting the details together:

```
postgres://username:SECUREPASSWORD@host:port/database_name
```

Follow the instructions [here](https://docs.hasura.io/1.0/graphql/manual/deployment/docker/index.html).

Once Hasura GraphQL engine starts, visiting [http://localhost:8080](http://localhost:8080) opens the Hasura Console. The console provides a GraphiQL instance to easily test all your GraphQL queries, mutations, and so on.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dJlxjx1PHK5flNXiKVy5sg.jpeg)
_Hasura GraphQL Engine Console_

Now go to the Data tab, and track all the tables to create instant GraphQL APIs!

### Authentication

By default, HGE is installed in development mode. All the tables/views which are tracked by HGE can be viewed/updated without any checks. This is is not recommended for a production environment. Hasura lets you define granular access controls for every field in your GraphQL schema, that’s every table or view in your Postgres schema. These access control rules can use dynamic variables that come in with every request. Check out the [docs](https://docs.hasura.io/1.0/graphql/manual/auth/index.html) for more information.

HGE can be secured from direct access by configuring a webhook URL which will be called to validate every request unless the request contains a valid `access-key`.

Let’s first make a simple request for users:

And running it in GraphiQL:

![Image](https://cdn-media-1.freecodecamp.org/images/1*VVG55IL6bFoDlYnCDvk9vg.png)

Note that `x-hasura-user-id` is set to “2” and `x-hasura-role` is set to “user”. These are the `auth` headers which will need to be set by the `auth-hook` in the [production mode](https://docs.hasura.io/1.0/graphql/manual/deployment/docker/securing-graphql-endpoint.html). (GraphQL engine started with `access-key` and `auth-hook`).

#### Secure GraphQL API

![Image](https://cdn-media-1.freecodecamp.org/images/1*nJKLzkgQXGd7a7ILDBAEfQ.png)
_Webhook architecture_

The first step is to [secure HGE](https://docs.hasura.io/1.0/graphql/manual/deployment/securing-graphql-endpoint.html) with an`access-key` and configure `auth-hook` with the a webhook, which in this case will be served by the Laravel app. This webhook will be invoked by the GraphQL engine, with the headers attached to the request. The webhook will return appropriate `x-hasura-role` and `x-hasura-user-id` , which it can obtain from authenticating the user with the `Authorization` header that’s passed on from the request.

Here, the auth-hook host will be your IP address on the docker bridge network if you’re using docker, or your webhook URL otherwise. You can ignore the `postgres` section if you’re using an external Postgres database.

To set up the `access-key` / `auth-hook` flags on your Heroku instance of HGE, [follow these instructions](https://docs.hasura.io/1.0/graphql/manual/deployment/heroku/securing-graphql-endpoint.html). We’ll assume that the webhook is at `/hge-webhook` for now, we will be setting it up on Laravel later.

Let’s try to make the query again and see what the response is.

![Image](https://cdn-media-1.freecodecamp.org/images/1*afYqLtDIyrJyR7RU7iG6_w.jpeg)

This is because we haven’t configured the webhook yet, or even set the correct `Authorization` headers.

### Setting up the Laravel webhook

Let’s set up our sample app on Heroku, so that we can easily deploy it and test out our changes.

For the purposes of this tutorial, we’ve deployed a sample app with the webhook [here](http://laravel-todo-hge.herokuapp.com). The corresponding HGE instance can be accessed [here](https://hge-laravel-todo.herokuapp.com/console). (Access key: `helloworld` )

You can register on this sample app, and add/remove todos on the app.

Let’s add a webhook now to authenticate requests sent to our HGE instance. We’ll do this using a middleware, so let’s generate a middleware class first.

`php artisan make:middleware webhookMiddleware`

Let’s first add the route to our `app/Http/routes.php` file:

Now we’ll register our middleware by adding it to the `app/Http/Kernel.php` file under `routeMiddleware`:

Now let’s set up the actual webhook at `app/Http/Middleware/webhookMiddleware.php` :

This page simply uses the `Authorization` bearer token to start a session, and then uses Laravel’s Auth to check and get the user id. You can modify this to add your custom session/token logic, and verify authentication.

If authenticated, we return the `x-hasura-role` and `x-hasura-user-id` variables as JSON. This will authenticate the request to HGE.

Now, we need an easy way to get the session token of a logged in user, so let’s add this to our `resources/views/users/profile.blade.php` :

Now, login in and head to the User Profile to see your new session token:

![Image](https://cdn-media-1.freecodecamp.org/images/1*KvPgJCAvDSq3btHtZ-xw7A.png)

Let’s commit and deploy this to Heroku:

`git commit -am "Add HGE webhook"`

`git push heroku master`

Once it’s pushed, let’s head over to the HGE Console to test our new webhook!

![Image](https://cdn-media-1.freecodecamp.org/images/1*2hIa4anl3efGIqbJv2dgLw.png)
_Authorization using Bearer token_

The webhook returns the corresponding `x-hasura-user-id` and `x-hasura-role`, and GraphQL engine responds with appropriate results as configured in the access rules.

### Migration System

HGE comes with a powerful Rails-inspired migration system, and changes made in the HGE console automatically generate schema files in your folder when run as `hasura console` (you can install the [Hasura CLI](https://docs.hasura.io/1.0/graphql/manual/hasura-cli/install-hasura-cli.html) for this).

For the purposes of this blog, though, we’ll let Laravel handle our migrations, and just export the HGE metadata so that it can track the schema and permissions separately.

You can check out the [HGE docs](https://docs.hasura.io/1.0/graphql/manual/migrations/database-with-migrations.html) for more detailed instructions.

Once you have everything set up as described in the above link, you can just add the folder created to your version control repository for the Laravel code.

To export metadata, run the following command in the folder created by the `hasura init` command in the migration instructions:

`hasura metadata export`

Since we’re letting Laravel handle the migrations, avoid making schema changes through the Hasura console, so that the Laravel migrations remain your source of truth on the schema.

That’s it! We now have a secure HGE endpoint working neatly with Laravel’s internal auth. Go forth and write code!

[**_Hasura_**](https://goo.gl/fR68ep) _gives you instant realtime GraphQL APIs over any Postgres database without having to write any backend code._

