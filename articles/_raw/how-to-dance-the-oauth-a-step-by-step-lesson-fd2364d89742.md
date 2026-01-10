---
title: 'How to dance the OAuth: a step-by-step lesson'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-03T19:08:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-dance-the-oauth-a-step-by-step-lesson-fd2364d89742
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eTlZtD7s7bWMGaa0P4anvA.jpeg
tags:
- name: data
  slug: data
- name: oauth
  slug: oauth
- name: Security
  slug: security
- name: technology
  slug: technology
- name: user experience
  slug: user-experience
seo_title: null
seo_desc: 'By Anabella Spinelli

  Most of the times I try to learn something new and put it into practice, I quickly
  start to feel like I’m lost in a myriad of dance moves. I’m desperately trying to
  find the right way to do things, while not really understanding ...'
---

By Anabella Spinelli

Most of the times I try to learn something new and put it into practice, I quickly start to feel like I’m lost in a myriad of dance moves. I’m desperately trying to find the right way to do things, while not really understanding what’s going on or how I ended up on the wrong side of the room…

Just trying things out until something works.

Maybe it’s because of the way my learning process works, or maybe guides and tutorials are targeted at more experienced or technical people. But, after I’m done wrapping my head around the subject, I always feel like there should be an easy guide for understanding the key concepts **and** making it easier to apply them in a project.

So this time, I’ve decided to stop wishing for it and make it myself, using the last thing that I learned.

And that thing was OAuth 2.0.

### What is OAuth?

Let’s start with the basics: OAuth stands for **Open Authorization**. It’s a process through which an application or website can access private user data from another website.

This other website usually works only as a trusted **identity provider**. It gives the requesting app some basic information about you so that the app can create a profile. This way, you don’t have to fill in a boring sign-up form and deal with yet another password ?

You’ve already used this at least a gazillion times, in fact you used it every time you clicked on “Log in with Facebook / Google / GitHub / …”. Next, you were shown a consent screen that displayed which information from your (let’s say) Facebook profile you’re allowing **that-hot-new-app.com** to read (and sometimes, write). After that, since **that-hot-new-app.com** trusts the identity provided by Facebook, they can create a profile for you on their database using the data that they received.

The communication between **that-hot-new-app.com** and Facebook usually ends here. This is why your profile picture won’t change all across the Internet if you change it on Facebook. They just never go back to Facebook and ask for updated data.

### When marimba rhythms start to play…

There’s another purpose for building this kind of mechanism, one with way more potential: using the identity provider as a **service provider** (in an ongoing manner). This means communicating with it regularly to supply enhanced features for your users.

A nice example of this is [**Relive**](https://www.relive.cc/), a service that connects with different sports tracking apps to create Earth view videos of your run or ride. Every time you finish an activity, Relive prompts you offering to create a video from it. If you say yes, they’ll process it, and notify you when it’s ready for social media bragging… I mean sharing ?

There’s really no technical difference between these two usages. That’s why **you should be cautious** about where you log in with your social media or Google/Gmail account.

It might sound scary, but there's really nothing to fear. Just bear in mind that you’re authorizing **that-hot-new-app.com** to access that information about you that’s detailed in the consent screen, potentially on a recurrent basis. Be aware of the permissions you grant, and make sure you know how to disable them whenever you don’t feel trusting anymore.

For instance, if you are using your Google account for accessing **that-hot-new-app.com** but don’t want to allow that anymore, just go to your [Google account settings](https://myaccount.google.com/security#connectedapps) and disable their access.

All the main identity providers offer control over this.

### All right, but how do you dance the OAuth?

Before you land on **that-hot-new-app.com** and even click on “Log in with `YourFavoriteIdentityProvider`_”_, someone — probably a developer — has to create an application on the provider’s site.

This is a way of registering **that-hot-new-app.com** so that, later, the provider knows who’s asking for private data.

In this step, the developer will set up some information about the application, like the app's name or website and — most importantly — **a redirect URI**. The provider (like Google or Facebook) will use this to contact the requesting app and tell them that the user said _yes_ ?

![Image](https://cdn-media-1.freecodecamp.org/images/-ZNoydoRCuDXAntqiAdKG9MVmuTjLk7qpOtW)
_I promise you won't have to write it by hand, we pride ourselves on our paperlessness._

Once the app is registered, the provider will give **that-hot-new-app.com** a **clientId** and a **clientSecret** which will be used in the communications between them. They work sort of like a username and password for the application.

![Image](https://cdn-media-1.freecodecamp.org/images/Nc8EUZy8o8w-5QddAogfWj2SifjW9Qh5OZWh)
_You'll get the clientID and clientSecret right after you click on Save application_

It's very important that you keep your clientSecret in a secure location and don't share it with strangers. If someone gets access to it, they could request private user data from the provider on your behalf, and then use it for evil!

We don't want that.

#### Hands on waists or shoulders

Apart from setting up all those things, the developer has to find out what kind of data the provider gives access to, and how it’s segmented.

These “segments” are known as **scopes** and they define access rights, usually separated in read/write categories. So, for example, **that-hot-new-app.com** can request for “**profile:read**” and “**contacts:read**” scopes. This means they can read whatever the provider assigns to the “profile” and “contacts” segments. Other things won’t be accessible, for example your posts or what content you like.

Well, just to make things simple for now on, let’s say that **that-hot-new-app.com** is a website that integrates with [**Typeform**](https://www.typeform.com/), a service for creating beautiful and smart forms and also the company I work for. You definitely want in on the hottest thing right now, and quick, so on their website you click on “Log in with Typeform” to get right into the action. What’s next?

Here’s a home-made, organic, and cholesterol-free diagram to use as a map for the whole thing. It may look a bit complicated but don’t worry, we’ll examine each step up next.

![Image](https://cdn-media-1.freecodecamp.org/images/EieGAKMEfd4kumthtdBGcXE7rUq4xsvo8i15)
_Colorful notes bring joy to my heart_

### Authorize: the first step in the OAuth dance

So, you take the initiative and click on “Connect with Typeform”. Here, that-hot-new-app.com (_THNA_ from now on, ’cause I’m getting tired of writing dash-separated words) will send you to Typeform’s authorize endpoint (`/oauth/authorize`) and provide:

* their clientId (remember, that’s **THNA**’s username)
* their desired scopes (or access rights)
* and their redirect URI again (Typeform already knows it from when we set up the whole thing, but we send it again as an extra layer of security)

That URL will look something like this:

```
https://api.typeform.com/oauth/authorize?client_id=yourClientId&scope=accounts:read+forms:read+results:read
```

Typeform will use this information to generate a consent screen where you can review what sort of things you’re authorizing **THNA** to see and do.

![Image](https://cdn-media-1.freecodecamp.org/images/istIyX0juNBgdwBXW2-y-sAzMhnOgkF1sY0R)

Once you have **thoroughly read what you’re consenting** to and happily click on “Allow”, Typeform will send you to the redirect URI with a temporary, like so:

```
https://that-hot-new-app.com/auth/redirect?code=xxxXXXxxxXXXxxx
```

### Token: it takes 2 to tangOAuth ?

All this back and forth feels like someone’s taking you for a tango spin, right?

The second step of the OAuth dance is when **THNA** receives that code, and exchanges it for an **OAuth Token**.

So **THNA** takes that code and sends it back again to Typeform, along with the redirect URI (yes, again!), and the client secret (that’s the app’s password!).

As reward for a dance well danced, **THNA** will get a shiny OAuth Token ✨ which it can use to interact with Typeform on behalf of the user, that is… you!

#### Stay with me, sway with me

From now on, in every request _THNA_ makes to Typeform on your behalf, they’ll have to include an **Authorization** header with that access token. With it, Typeform (or any other provider) can identify:

* who’s asking for the data (in this case, **THNA**_)_
* who’s the data about (you!)
* and also make sure they have the correct **authorization** to access that data (only what you consented to).

### Ready for the dance floor ?

So now that you know all the steps and spins of the OAuth dancing technique you should be ready to create your own choreographies, I mean, integrations, and make the Internet an even greater place.

Drawings by yours truly, cover photo by [Gez Xavier Mansfield](https://unsplash.com/photos/I_mkJxsx8kA?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText).

