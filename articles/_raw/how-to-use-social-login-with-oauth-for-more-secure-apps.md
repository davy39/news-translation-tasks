---
title: How to Use Social Login with OAuth to Make Your Apps More Secure
subtitle: ''
author: Rohit Jacob Mathew
co_authors: []
series: null
date: '2021-10-29T14:50:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-social-login-with-oauth-for-more-secure-apps
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/MzBKTcnJA.jpeg
tags:
- name: Application Security
  slug: application-security
- name: oauth
  slug: oauth
- name: Security
  slug: security
seo_title: null
seo_desc: 'Many developers have written a demo login application at some point in
  time. We all start with the simple user defined ID and password. We then try to
  implement something like a social login with, say, Google or Twitter.

  There is, of course, a more c...'
---

Many developers have written a demo login application at some point in time. We all start with the simple user defined ID and password. We then try to implement something like a social login with, say, Google or Twitter.

There is, of course, a more complex process involved in setting up social login, but for a user it's as simple as clicking a button to log in. 

The ease of not having to remember an ID/password and just being able to signup/login through the click of a button is extremely beneficial to the user.

## What if I Told You This Was Way More Secure? 😉

Social logins really help us achieve a few things:

* Support for multiple devices
* Single Sign On
* Simple to implement
* The ability to share data for users without having to release personal information
* Ability revoke an active session i.e not allow a third party access to the login and data
* There are no long-lasting credentials being exchanged

## So What Technology Drives Social Login? 🤔

The underlying protocol used is something called [OAuth](https://oauth.net/). It is defined as:

> An open protocol to allow secure authorization in a simple and standard method from web, mobile, and desktop applications.

Now with a basic understanding of social login and the above definition you probably have some idea of how this works – but let me use a simple example to explain how to use OAuth.

I remember my friend [Sumedh](https://twitter.com/lunatic_monk) describing it as an interaction between a Mother, Father, and their Son. Imagine that the mother wants some groceries from the market and she wants the son to buy them for her.

Before I go into the conversation let me set some context.

> **Mother:** The user of the application

> **Son:** Third party client or in technical terms the OAuth Client

> **Father:** The Social Account or in technical terms the OAuth Provider

The conversation could possibly go like this:

> **Mother:** Hey son, go to the market and bring me some coffee powder. Take the required money from your father.

> **Son:** Okay.

> _Son (OAuth client) goes to father (OAuth provider)_

> **Son:** Hey dad, mom told me to take money from you since she wants some things from the market.

> _Father (OAuth provider) asks mother (User) about the permission to give money to their son (OAuth client)_

> **Father:** Hey, shall I give him the money and how much?

> _Authorization of your application takes place here._

> **Mother:** Yes, please give it to him.

> _Permission grant by mother (User)_

> _Son (OAuth client) gets the required things from the market and returns them to mother (User). Here returning things to mother (User) can be thought of redirecting the user (or logging them) into the third party site._

For a more technical understanding of how this works in code, [Richard Schneeman](https://twitter.com/schneems) has this amazing video below:

%[https://youtu.be/tFYrq3d54Dc]

## Now Lets Put All of This in Context

Let's take as an example [the DEV Community](https://dev.to/). If you wanted to create an account on the DEV Community using Twitter, what would happen?

Basically, if the "Sign up with Twitter" button exists, then the initial setup between the OAuth Client (Dev.to) and the OAuth Provider (Twitter) is already done.

The Client triggers a permission granting page for the OAuth Provider based on the credentials it receives from the initial setup. This looks something like below:

![Permission Grant Page](https://cdn.hashnode.com/res/hashnode/image/upload/v1622980489496/IrLawupb6.png)

Once you login and grant permission, the OAuth Provider redirects you back to the client and the client gets a token to access your information from the OAuth Provider. This access token enables the client to get specific data from the provider

Based on that data the client then creates an account and logs you in

### What Happens on Successive Login?

Thats a good question. Now OAuth has multiple grant types, and based on that we have different ways to get an access token from the OAuth Provider. 

For all subsequent logins, the OAuth Client will hit the provider and generate a new access token to get access to the data and do the login.

Thus this enables us to achieve Single Sign On, the ability to share data for users without having to release personal information, the ability to revoke access, and the ability to not have long lasting credentials exchanged.

This all leads to a more secure experience.

## Conclusion

I hope this short blog post helps you understand why social logins are more secure than the traditional username/password option. I will be writing about the different OAuth Grant types in the future and will be providing code examples as well.

Thanks for reading! I really hope that you find this article useful. I'm always interested to know your thoughts and happy to answer any questions you might have in your mind. If you think this post was useful, please share it to help promote this piece to others.

Thanks for reading! :)

P.S Do feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/rohitjmathew) or [Twitter](https://twitter.com/iamrohitjmathew)

