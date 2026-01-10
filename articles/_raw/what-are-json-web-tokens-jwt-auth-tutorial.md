---
title: What are JSON Web Tokens? JWT Auth Tutorial
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-11-12T20:51:31.000Z'
originalURL: https://freecodecamp.org/news/what-are-json-web-tokens-jwt-auth-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/jwt.png
tags:
- name: JSON Web Tokens
  slug: json-web-tokens
- name: youtube
  slug: youtube
seo_title: null
seo_desc: 'Most web apps use security measures to make sure user data stays private.
  Authentication is a key part of security and JSON Web Tokens (JWT) are a great way
  to implement authentication.

  So what are JSON Web Tokens?

  JWT is a standard that defines a co...'
---

Most web apps use security measures to make sure user data stays private. Authentication is a key part of security and JSON Web Tokens (JWT) are a great way to implement authentication.

## So what are JSON Web Tokens?

JWT is a standard that defines a compact and self-contained way to securely transmit information between a client and a server as a JSON object. The compact size makes the tokens easy to transfer through an URL, POST parameter, or inside an HTTP header. Also, since they are self-contained they include all the necessary information about a user so the database does not need to be queried more than once.

The information in a JWT can be trusted because it is digitally signed using a secret or public/private key pair.

## Authentication

JWT are mainly used for authentication. After a user logs in to an application, the application will create a JWT and send it back to the user. Subsequent requests by the user will include the JWT. The token tells the server what routes, services, and resources the user is allowed to access. JWT can be easily used across multiple domains so they are often used for Single Sign On.

## Using JSON Web Tokens

Thomas Weibenfalk made an excellent video tutorial that explains JSON Web Tokens and demonstrates how to use them for authentication. The tutorial teaches JWT Auth as simply as possible, without using a lot of extra libraries.

Watch the tutorial below or on [the freeCodeCamp.org YouTube channel](https://www.youtube.com/watch?v=x5gLL8-M9Fo) (2 hour watch).

%[https://www.youtube.com/watch?v=x5gLL8-M9Fo]


