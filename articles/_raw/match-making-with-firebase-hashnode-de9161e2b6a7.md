---
title: How to use Firebase for building multiplayer Android games
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-10T22:16:35.000Z'
originalURL: https://freecodecamp.org/news/match-making-with-firebase-hashnode-de9161e2b6a7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cUxtuiNpwNevTBxw3oAY4g.png
tags:
- name: android app development
  slug: android-app-development
- name: Firebase
  slug: firebase
- name: gaming
  slug: gaming
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Shukant Pal

  Have you just built your board game for Android? Want to get it online? You are
  in the right place — let’s build it together!


  We are going to implement match-making with the Firebase Realtime Database in this
  article. For that, you ne...'
---

By Shukant Pal

Have you just built your board game for Android? Want to get it online? You are in the right place — let’s build it together!

![Image](https://cdn-media-1.freecodecamp.org/images/1*cUxtuiNpwNevTBxw3oAY4g.png)

We are going to implement match-making with the Firebase Realtime Database in this article. For that, you need Firebase setup in your Android project — see how to do that [here](https://firebase.google.com/docs/database/android/start).

### Prerequisites

* **Firebase users** — here, we are assuming you were able to login your user into Firebase using any method. This is necessary to identify whom to communicate with after the match-making is finished.
* **Gradle Dependencies** — Add these to the `dependencies` block in your app module's grade file.

```
implementation 'com.google.firebase:firebase-core:16.0.6' implementation 'com.google.firebase:firebase-auth:16.1.0' implementation 'com.google.firebase:firebase-database:16.0.6'
```

* You aren’t done after implementing match-making. That’s because you’ve only found two players that will play — but haven’t implemented how their moves will propagate over the network.

### Our model

We will use a node in the Firebase database called the game room which will store all the active challenges that users have pushed. Each user will search for existing challenges within the game room and will accept the first one found. Otherwise, the user will upload their own challenge and wait until someone accepts the challenge.

You will be able to add more features in your match-making implementation like matching based on similar performance ratings, friends, regional-bias, etc.

### How the heck are we gonna implement that?

I’ve divided our problem into three objects:

* **Matcher**: Finds any existing matches in the game room.
* **SelfChallengeManager**: Manages the challenge a user uploads if Matcher fails to find any one.
* **SelfChallengeCanceller**: Cancels the match-making process if this user doesn’t wanna play anymore.

In addition, we will require a “Challenge” object that has two properties — communication node reference and the challenger’s user ID (get why we need to login to Firebase now?). This object will be uploaded into the game-room by `SelfChallengeManager`.

### Writing our components first

Before writing our three components, we need to understand what a Firebase [transaction](https://firebase.google.com/docs/database/android/read-and-write#save_data_as_transactions) is. We don’t want two users accepting the same challenge at the same time — which would corrupt our database and make our precious users angry. Transactions come to the rescue by preventing concurrent operations on a node in the database (which will be the game room).

How does that relate to our components? — Our components will be modeled as transactions as inner classes in our ‘FirebasePlayerMatchMaker’ class.

[https://gist.github.com/SukantPal/2c1f5daedfaee784bfeb622d4e26736e](https://gist.github.com/SukantPal/2c1f5daedfaee784bfeb622d4e26736e)

We use two callback interfaces — `OnMatchMadeCallback` and internally `OnFailCallback`. The factory method takes a `OnMatchMadeCallback` which is called whenever a match is made. The `OnFailCallback` is invoked whenever **MatchMaker** fails to find a match.

Here, `findMatch` runs on a separate thread and creates an `OnFailCallback` if `Matcher` doesn't find a match. In that case, we have to create a `SelfChallengeManager` and run it as a transaction.

1. **Matcher**

Here, the `doTransaction()` method iterates over all the children of the game room node and searches for a `Challenge` that is compatible for our user. By default, `isChallengeCompat` returns `true`, but you can change that by adding additional constraints like ratings. The first compatible challenge is then stored and the challenge node is deleted (by setting the value to `null`) in the database. Note that by deleting the node, the other player will be notified of the acceptance.

2. **SelfChallengeManager**

Here, the `doTransaction` method adds a child node to the `GAME_RECORD` node in our database. This is where the game moves will be communicated after the match-making. It then uploads a `Challenge` to the game room and adds itself as a `ValueEventListener`. Whenever another user accepts the request, they will delete this node and this user will get notified as we are listening.

3. **SelfChallengeCanceller**

Our code just deletes the node created in by `SelfChallengeManager` by iterating over all the game room and finding our challenge. BUT IT’S INCOMPLETE!! You (optionally) should add a feature where the this user automatically resigns from the game if the match was accepted already.

In the `OnMatchMadeCallback` you provide to `FirebasePlayerMatchMaker.newInstance`, you must initialize the game communication to be done in the node (by path) `mGamePath`.

Yo, you’ve done it. Thanks for reading!

_Originally published at [hashnode.com](https://hashnode.com/post/match-making-with-firebase-cjrzgoi6k0010ads2xqojc7a1)._

