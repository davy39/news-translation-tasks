---
title: How to use Streams, BLoCs, and SQLite in Flutter
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-17T19:58:12.000Z'
originalURL: https://freecodecamp.org/news/using-streams-blocs-and-sqlite-in-flutter-2e59e1f7cdce
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ihvDZXwv6oGz760kKUgYTQ.png
tags:
- name: Apps
  slug: apps-tag
- name: Flutter
  slug: flutter
- name: General Programming
  slug: programming
- name: SQLite
  slug: sqlite
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Eric Grandt

  Recently, I’ve been working with streams and BLoCs in Flutter to retrieve and display
  data from an SQLite database. Admittedly, it took me a very long time to make sense
  of them. With that said, I’d like to go over all this in hopes yo...'
---

By Eric Grandt

Recently, I’ve been working with streams and BLoCs in Flutter to retrieve and display data from an SQLite database. Admittedly, it took me a very long time to make sense of them. With that said, I’d like to go over all this in hopes you’ll walk away feeling confident in using them within your own apps. I’ll be going into as much depth as I possibly can and explaining everything as simply as possible.

In this post, we’ll be making a simple app from start to finish that makes use of streams, BLoCs, and an SQLite database. This app will allow us to create, modify, and delete notes. If you haven’t done so yet, create a new barebones Flutter app using `flutter create APPNAME`. It'll be a lot easier to understand all this if you start fresh. Then, later on, implement what you learned into your existing apps.

The first order of business is creating a class to handle the creation of our tables and to query the database. To do this properly, we need to add `sqflite` and `path_provider` as dependencies in our `pubspec.yaml` file.

<script src="https://gist.github.com/Erigitic/b7f663db0901d93295c3c4c7a0f50495.js"></script>

In case it doesn’t run automatically, run `flutter packages get` to retrieve the packages. Once it finishes, create a `data` folder and a `database.dart` file within it. This class will create a singleton so we can access the database from other files, open the database, and run queries on that database. I've included comments to explain some of the code.

<script src="https://gist.github.com/Erigitic/f6835ec9f36832eb7440a6ab1a4443a7.js"></script>

Create another folder, `models`, and add one file to it: `note_model.dart`. Here's a great tool to easily make models: [https://app.quicktype.io/#l=dart](https://app.quicktype.io/#l=dart).

**NOTE:** Keep in mind that models do NOT have to copy the columns in the table. For example, if you have a user id stored in a table as a foreign key, the model probably shouldn’t contain that user id. Instead, the model should use that user id in order to retrieve an actual `User` object.

<script src="https://gist.github.com/Erigitic/5a70f4a10130fba98155fd93f03c108c.js"></script>

With our note model created, we can add the final functions to our database file that’ll handle all note related queries.

<script src="https://gist.github.com/Erigitic/88a40ab6402dc9ac274b45a1f233505e.js"></script>

Let’s get started with streams and BLoCs now. If this is your first time working with these, it can be quite daunting. I promise you though that streams and BLoCs are exceptionally simple once you get past the learning phase.

The first thing we need is a `blocs` folder within the `data` folder. This folder will contain all our BLoCs, as the name suggests. Let's create the files for each BLoC: `bloc_provider.dart`, `notes_bloc.dart`, and `view_note_bloc.dart`. One BLoC per page and one to provide the BLoCs to those pages.

The `bloc_provider` is in charge of easily providing our pages with the necessary BLoC and then disposing of it when necessary. Every time we want to use a BLoC, we'll be using the `bloc_provider`.

<script src="https://gist.github.com/Erigitic/f21abb7afa652d75a67a64a087072eb6.js"></script>

Whenever we need a BLoC on one of our pages, we’ll utilize the `BlocProvider` like this:

<script src="https://gist.github.com/Erigitic/f72c35d2cbc3291a904e75dddcda6ae3.js"></script>

Let’s create our notes BLoC which will handle retrieving all our notes and adding new notes to the database. Since our BLoCs are page specific, this BLoC will only be used on the notes page. I’ve commented the code to explain what’s going on.

<script src="https://gist.github.com/Erigitic/edb7fe1650f1f9a248d81a0bb12696da.js"></script>

With the notes BLoC created, we have everything we need to create our notes page. This page will display all our notes, and allow us to add new ones. We’ll put the code for our notes page into `main.dart`. Once again, I've commented on all the necessary pieces of code to explain what's going on.

<script src="https://gist.github.com/Erigitic/b278a95269fa712f06c83927a8a480f1.js"></script>

Now we need a way to view, edit, save, and delete the notes. This is where the view note BLoC and the view note page come into play. We’ll start with `view_note_bloc.dart`.

<script src="https://gist.github.com/Erigitic/5b7c50bbe9eeae3d2c7dfaa898eda203.js"></script>

Now we can build the actual page to allow us to interact with our notes. The code for this page is going in `view_note.dart`.

<script src="https://gist.github.com/Erigitic/a9af0325bab99057f71c313fd9b3b5d4.js"></script>

![Image](https://cdn-media-1.freecodecamp.org/images/VM6e-BtScNO6RMweffYoZGr8kiqmcnstM2DE)
_Final app using streams, BLoCs, and SQLite_

That’s all it takes to work with streams, BLoCs, and SQLite. Using them, we’ve created a super simple app that allows us to create, view, edit, and delete notes. I hope this walkthrough has made you more confident in working with streams. You’ll now be able to implement them into your own apps with ease. If you have any questions, please leave a comment as I’d love to answer them. Thanks for reading.

View the full code here: [https://github.com/Erigitic/flutter-streams](https://github.com/Erigitic/flutter-streams)

