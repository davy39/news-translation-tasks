---
title: Here’s what I wish I knew before I started using Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-19T21:45:18.000Z'
originalURL: https://freecodecamp.org/news/heres-what-i-wish-i-knew-before-i-started-using-firebase-9110d393e193
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fXiKiz-wuXiCUboQDAG5Cw.png
tags:
- name: database
  slug: database
- name: Firebase
  slug: firebase
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Nikhil Sridhar

  A list of advantages and drawbacks you should consider before choosing Cloud Firestore
  as your database


  Over the last few years, Firebase has grown as an increasingly popular backend solution.
  Especially after the release of Cloud ...'
---

By Nikhil Sridhar

#### A list of advantages and drawbacks you should consider before choosing Cloud Firestore as your database

![Image](https://cdn-media-1.freecodecamp.org/images/dfT6Nj8mXMG8y0qJgCA1F5r3GeGqwHoMLppn)

Over the last few years, Firebase has grown as an increasingly popular backend solution. Especially after the release of Cloud Firestore. Firestore is a flexible cloud database with expressive queries and real-time updates. After developing my first application with Cloud Firestore, I organized a list of advantages and drawbacks. This list will help you choose if Firestore is the database for you.

Before I begin, it is imperative that you understand Cloud Firestore’s data model. Firestore stores data in documents, organized into collections. _Each_ **_document_** _contains a set of key-value pairs_. Cloud Firestore is optimized for storing large collections of small documents. _All documents must be stored in_ **_collections_**. Documents can contain sub-collections and nested objects. B_oth of which can include primitive fields like strings or complex objects like lists_.

Now that you understand the basics, here is a list of items in Cloud Firestore which can make or break your application.

### Advantage #1: Transactions and Batched Writes

Error handling can be one of the most tedious tasks when it comes to reading from and writing to a database. In some situations, if an error occurs while reading from or writing to one location in the database, you might want to cancel the entire operation. This is where batched writes and transactions come in.

**Batched writes are a set of write operations performed atomically. In a set of atomic operations, either all the operations succeed, or none of them.** If your application succeeds in writing data to one document but fails in writing data to another document, none of the writes are performed. An error is thrown.

**Transactions work similarly. They are more powerful, for they allow you to both read and write to documents in an atomic fashion.**

Batched writes and transactions can be best explained through an example. The easiest being adding friends on a social media platform. When User A adds User B as a friend, you want to write data to both User A’s document and User B’s document to signify that they are friends. However, if either the write to User A’s document or User B’s document fails, you want to undo any changes and throw an error. Batched writes and transactions simplify this process with only a few lines of code.

### Advantage #2: Invites

![Image](https://cdn-media-1.freecodecamp.org/images/KKJeFis8M7Z0fjdCH1PK0P0Yg49jKs9V8oa3)

Firebase Invites is perhaps the **most powerful on-boarding technique**_,_ especially if your app runs on multiple platforms (iOS, Android, etc.). It allows you to **prompt the current user if he would like to invite his friends to your app.** However, what’s more is that Firebase actually allows you to create a temporary user for the invited user to provide the current user with the best customer experience.

For instance, let us say that you are building an app similar to Venmo. This app allows users to track expenses and eventually settle up. User A wants to pay User B, who currently does not have an account. Using Firebase Invites, you could allow User A to invite User B. Then set up a temporary account for User A to track expenses with until User B accepts the invitation and creates his own account. Invites provide app referrals through both **email and SMS.** It is a great way to acquire new users and keep current users happier than ever before.

### Advantage #3: Dynamic Links

Firebase Dynamic Links allows for the best possible user-onboarding experience. **These links work cross-platform. They allow you to provide a custom experience within an application once a user opens a certain link**_._ Dynamic Links is best utilized when integrated with Firebase Invites.

Let us take the example in the previous advantage. User B, who has been invited to your app by User A, now decides he wants to create an account to view any debts he owes to User A. When User B receives the invite via email and clicks on the dynamic link, he will be directed to the AppStore where he will download your app. Then, when he opens the app and begins to register, his email will already be filled in thanks to the **information passed by the dynamic link**.

### Drawback #1: Querying by Sub-collection

One of the biggest disappointments in Cloud Firestore is the **inability to query documents by their sub-collections**. For example, let us say you have the following data structure:

**collection** of users -> us**er docum**ent **-> coll**ection of friends ->**; friend** doc**umen**t -> data regarding that friend (name, email, etc.)

In this structure, it would be impossible to fetch all users who have a friend with a specific name and email. Firebase does eventually plan to offer a solution. For the time being, it seems like the **only solution is to replace sub-collections with arrays** in which documents can be queried by.

Although this fix might seem sufficient, it isn’t. As your application grows, so can the arrays, **significantly affecting the read and write document performance**.

### Drawback #2: Querying by Location

![Image](https://cdn-media-1.freecodecamp.org/images/yPBPQPtjssORw63qBsL2qKBZjII3XSXTmMe8)

Depending on your application’s functionality, this could be the biggest flaw of all. Although Cloud Firestore does provide a location data type, **it does not allow you to query all documents within a radius of a given location**.

Let us consider that you are building an app identical to Uber. When a user logs into the app, you want to fetch all cars within a certain radius of the current user’s location to alert the user if there are any drivers nearby. This task is impossible without the help of third party libraries.

Luckily, if you are using the real-time database, Firebase now recommends you use the [GeoFire](https://github.com/googlearchive/geofire) library to query documents by location. However, if you plan to use Cloud Firestore, there is no recommended solution.

Although there are a few libraries which have attempted to solve this problem like [GeoFirestore](https://github.com/imperiumlabs/GeoFirestore), Firebase has yet to verify them as a reliable source.

### Drawback #3: Full-text Search

This problem is sure to affect anybody who uses Cloud Firestore, for **it does not allow you to query documents by “incomplete text”**. This problem can be best illustrated through an example.

Let us say your application allows users to friend each other. One user types in “Al” in an attempt to search for his friend “Alex”. **You want to fetch all users in the database whose name contains the text “Al” to help the user narrow down his search. This task is not possible** through Cloud Firestore alone. **Algolia, a third party service, is required to implement full-text search**. All documents must be uploaded to Algolia as records. These records can then be queried by incomplete text.

For more tips, please stay tuned and follow me. If you enjoyed this article, feel free to hold down that clap button.

