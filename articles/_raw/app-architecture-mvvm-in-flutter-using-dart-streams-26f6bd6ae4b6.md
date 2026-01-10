---
title: Use Model-View-ViewModel to make your code cleaner in Flutter with Dart Streams
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-12T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/app-architecture-mvvm-in-flutter-using-dart-streams-26f6bd6ae4b6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9spr-LhRLN2uWPcPqnvvZA.jpeg
tags:
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By QuickBird Studios

  A common problem when developing apps is that you end up with over-complicated classes.
  These classes contain view logic as well as business logic. Both are so intertwined
  that it’s impossible to test them independently. Code-rea...'
---

By QuickBird Studios

A common problem when developing apps is that you end up with over-complicated classes. These classes contain view logic as well as business logic. Both are so intertwined that it’s impossible to test them independently. Code-readability suffers, and future code changes are hard to implement.

Since there are almost no constraints on your architecture in Flutter, it’s fairly easy to run into this problem. Some developers write all their code in the Widget until they realize the mess they produced. Reusing code in other projects seems impossible, and in the end, you write most of your code twice. Model-View-ViewModel (MVVM) tries to solve that by splitting up business logic and view details.

In this article, we show you how MVVM with Flutter could look like. We’ll create a functional reactive ViewModel using Dart’s Stream API.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yXqTw6EdqmA1pewkAFvHGQ.jpeg)

### Model-View-ViewModel

Before we look at any code, we should get a basic understanding of MVVM. If you’re familiar with MVVM, you can skip this part.

The main goal behind MVVM is to move as much of the state and logic from the View into a separate entity. This name given to this entity is the ViewModel. The ViewModel also contains the business logic. It serves as the mediator between the View and the Model.

![Image](https://cdn-media-1.freecodecamp.org/images/1*A87nt_oqnajSSejzJHGY5w.png)
_MVVM: Model-View-ViewModel_

The ViewModel has basically two responsibilities:

* it reacts to user inputs (e.g. by changing the model, initiating network requests, or routing to different screens)
* it offers output data that the View can subscribe to

The View does not contain any business logic. These are the responsibilities of the view:

* it reacts to new output states of the ViewModel and renders them accordingly (e.g. by showing a String in a text field)
* it tells the ViewModel about new user inputs (e.g. button-clicks, text-changes, screen touches)

In contrast to popular MVC approaches, the Fragment / Activity / UIViewController or Widget does not contain business logic in MVVM. It is a humble view that renders the ViewModel’s output states. The ViewModel does **not know** the View (a difference from forms of MVP and MVC). It offers output states that the View observes:

![Image](https://cdn-media-1.freecodecamp.org/images/1*vO41CcfdKftvklRsFt4sWQ.png)
_Input-Output interface of a ViewModel_

### MVVM in Flutter

In Flutter, the Widget represents the View of MVVM. The business logic sits in a separate ViewModel-class. The ViewModel is totally platform-independent. It contains no dependencies to Flutter, and can be easily reused, for example in a web project.

That is one of MVVM’s biggest powers. We can create a Mobile App and a website that both share the same ViewModel. You don’t need to reinvent and write the logic twice.

#### Example: Email Subscription Widget

Let’s look at an example. We’ll implement a Newsletter signup-form with an email textfield and a submit button. The button is disabled and the user sees an error if the email is invalid:

![Image](https://cdn-media-1.freecodecamp.org/images/0*_90H8ZlAkMucYABz.gif)

#### The ugly way

Without any specific architecture, the business logic and the current state are part of the widget. It could look something like this:

The problem is that view logic, view state, and business logic are mixed up. That leads to a few problems:

1. It’s hard to unit test
2. Other Dart projects cannot reuse the business logic, since it’s intertwined with Flutter-dependent View logic
3. This style gets messy very soon and you end up with huge Widget classes

Let’s see how we can improve this…

#### Solution with MVVM

As explained above, the ViewModel has Input and Output parameters. We will add an ‘**input**’ or ‘**output**’ prefix for the sake of clarity.

All Inputs are `Sinks`. The View can use those to insert data into the ViewModel. All Outputs are `Streams`. The View can listen for changes by subscribing to the `Streams`. The interface for our ViewModel looks like this:

We are using a `StreamController` as an input `Sink`. This `StreamController`provides a stream that we can use internally to handle those input events.

### Binding a View to the ViewModel

So how do we supply inputs and handle output events? To supply input values to the ViewModel, we insert them into the ViewModel’s `Sinks`. We’ll bind a Widget to the ViewModel. In this case, we insert the TextField’s text whenever it changes.

You listen to the ViewModel Outputs by subscribing to the Output-**Streams**.

Flutter provides a really cool Widget called `StreamBuilder` that will update whenever a **Stream** provides a new value. We won’t call `setState` ever again!  
The **StreamBuilder’s** `builder` method gives you a snapshot whenever it builds. This snapshot contains information about the stream, its data, and its errors. If our stream did not emit any value, `snapshot.data` will be null. So, be careful.

QUICK TIP: Try to help the Dart compiler when working with streams. Add all the needed generic types to avoid runtime errors.

Here you can see the whole picture:

As you can see, the View’s only responsibility is rendering Outputs and supplying Inputs to the ViewModel. Our Widget is therefore super slim and easy-to-read.

### Conclusion

We started out with MVVM in the native world and wondered if it would also work with Flutter. After trying it out, we can say: MVVM is a great fit for Flutter as well.

We love how nicely the View-logic is separated from the business logic. We love how easy ViewModels can be unit-tested. And we love how Dart ViewModels can be shared with other platforms that are using Dart.

The Stream-API takes some time to get used to, but afterward it feels very smooth. For more complicated tasks we used RxDart. This adds functionality to the standard Stream-API.

If you’re just hacking a small app, then the normal “put-everything-in-one-class” approach might be more straightforward. If you plan to build a bigger app, though, MVVM might be the architecture for you.

_Originally published at [quickbirdstudios.com](https://quickbirdstudios.com/blog/mvvm-in-flutter/) on June 12, 2018._

