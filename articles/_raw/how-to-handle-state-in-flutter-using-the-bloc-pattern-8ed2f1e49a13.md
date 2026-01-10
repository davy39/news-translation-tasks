---
title: How to handle state in Flutter using the BLoC pattern
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-30T21:39:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-state-in-flutter-using-the-bloc-pattern-8ed2f1e49a13
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6xT0ZOACZCdy_61tTJ3r1Q.png
tags:
- name: coding
  slug: coding
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Chuks Opia

  Last year, I picked up Flutter and I must say it has been an awesome journey so
  far. Flutter is Google’s awesome framework for crafting high-quality applications
  for Android and iOS.

  As with building almost any application, there’s alwa...'
---

By Chuks Opia

Last year, I picked up [Flutter](https://flutter.io/) and I must say it has been an awesome journey so far. Flutter is Google’s awesome framework for crafting high-quality applications for Android and iOS.

As with building almost any application, there’s always the need to handle application state. It is important that state management is handled efficiently, so as to avoid accruing technical debt, especially as your application grows and becomes more complex.

In Flutter, all UI components are widgets. As you start composing these widgets to create your awesome app, you’ll end up with a tree of deeply nested widgets. These widgets will most likely need to share application state with each other.

In this article, we’ll see how to handle state in Flutter using the BLoC pattern.

State management in Flutter can be achieved in a few different ways:

**Inherited Widget**: It allows you propagate data to its child widgets and the widgets are rebuilt whenever there is a change in the app’s state. The downside of using the InheritedWidget base class is that your state is final and this raises a problem if you want to mutate your state.

**Scoped Model**: This is an external package built on top of InheritedWidget and it offers a slightly better way to access, update and mutate state. It allows you to easily pass a data Model from a parent Widget down to its descendants. In addition, it also rebuilds all of the children that use the model when the model is updated.

This might raise a performance issue, depending on how many ScopedModelDescendants a model has, as they’re rebuilt when there’s an update.

This issue can be fixed by decomposing the ScopedModel into multiple models so you get finer-grained dependencies. Setting the `rebuildOnChange` flag to `false` also fixes this issue, but it brings with it the cognitive load of deciding what widget should be rebuilt or not.

**Redux**: Yes! As with React, there is a Redux package that helps you easily create and consume a Redux store in Flutter. Like its JavaScript counterpart, there’s usually a few lines of boilerplate code and the round trip of _actions_ and _reducers_.

#### Enter BLoC pattern

The Business Logic Component (BLoC) pattern is a pattern created by Google and announced at [Google I/O ’18](https://www.youtube.com/watch?v=RS36gBEp8OI). The BLoC pattern uses Reactive Programming to handle the flow of data within an app.

A BLoC stands as a middleman between a source of data in your app (e.g an API response) and widgets that need the data. It receives streams of events/data from the source, handles any required business logic and publishes streams of data changes to widgets that are interested in them.

A BLoC has two simple components: **_Sinks_** and **_Streams_**, both of which are provided by a **_StreamController_**. You add streams of event/data input into a _Sink_ and listen to them as streams of data output through a _Stream_.

A _StreamController_ can be accessed via the `‘dart:async’` library or as a _PublishSubject_, _ReplaySubject_ or _BehaviourSubject_ via the `[rxdart](https://pub.dartlang.org/packages/rxdart)` package.

Below is a code snippet showing a simple BLoC:

```dart
import 'dart:async';
// import 'package:rxdart/rxdart.dart'; if you want to make use of PublishSubject, ReplaySubject or BehaviourSubject.
// make sure you have rxdart: as a dependency in your pubspec.yaml file to use the above import


class CounterBloc {
  final counterController = StreamController();  // create a StreamController or
  // final counterController = PublishSubject() or any other rxdart option;
  Stream get getCount => counterController.stream; // create a getter for our Stream
  // the rxdart stream controllers returns an Observable instead of a Stream
  
  void updateCount() {
    counterController.sink.add(data); // add whatever data we want into the Sink
  }
  
  void dispose() {
    counterController.close(); // close our StreamController to avoid memory leak
  }
}

final bloc = CounterBloc(); // create an instance of the counter bloc

//======= end of CounterBloc file



//======= somewhere else in our app
import 'counter_bloc.dart'; // import the counter bloc file here

@override
void dispose() {
  bloc.dispose(); // call the dispose method to close our StreamController
  super.dispose();
}

...
@override
Widget build(BuildContext context) {
  return StreamBuilder( // Wrap our widget with a StreamBuilder
    stream: bloc.getCount, // pass our Stream getter here
    initialData: 0, // provide an initial data
    builder: (context, snapshot) => Text('${snapshot.data}'), // access the data in our Stream here
  );
}
...
```

A BLoC is a simple Dart class. In the code snippet above, we created a `CounterBloc` class and in it, a `StreamController` which we called `counterController`. We created a _getter_ for our Stream called `getCount`, an `updateCount` method that adds data into our Sink when called, and a `dispose` method to close our StreamController.

To access the data in our Stream, we created a `StreamBuilder` widget and passed our Stream to its `stream` property and accessed the data in its `builder` function.

#### Implementing BLoC

We’ll be converting the default Flutter sample app to use a BLoC. Let’s go ahead and generate a new Flutter app. In your terminal run the following command:

```
$ flutter create bloc_counter && cd bloc_counter
```

Open the app in your favourite editor and create three files in the lib folder: `counter.dart`, `counter_provider.dart` and `counter_bloc.dart`.

Our `CounterProvider` will contain an integer and a method to increment it. Add the following code to the `counter_provider.dart` file:

```dart
class CounterProvider {
  int count = 0;
  void increaseCount() => count++;
}
```

Next, we’ll implement our counter BLoC. Add the code below into your `counter_block.dart` file:

In our `CounterBloc` class, we used part of our initial sample code above. On line 7, we instantiated our `CounterProvider` class and in the `updateCount` method, we called the provider method to increment the count, and then on line 13, we passed the count to our Sink.

Replace the code in your `main.dart` file with the code below. In the code below, we simply removed most of the default counter code, which we’ll move to our `counter.dart` file. Whenever the `incrementCounter` method is called, we call the BLoC ‘s `updateCount` method which updates the count and adds it to our Sink.

Now, our BLoC is receiving and streaming data. We can access that data and display it on a screen through a **_StreamBuilder_**. We wrap whatever widget that needs the data in a StreamBuilder widget and pass the stream containing the data to it. Add the following code to the `counter.dart` file:

In the code above, we have a stateful widget. In our state class, on line 13, we call our bloc’s dispose method, so that stream controller can be closed whenever the widget is removed from the tree.

On line 19, we return a StreamBuilder widget and line 20, we pass the getter for our stream to it and also an initial data on line 21. The StreamBuilder also has a `builder` which gives us access to the data via a `snapshot`. On line 30, we access and display the data in the snapshot.

Go ahead and run the app by running the command below. Ensure you have an emulator running.

```
$ flutter run
```

With your app running, click the plus icon and watch the counter increase with every click.

![Image](https://cdn-media-1.freecodecamp.org/images/1*21qeIQKSfZy9nxiJ3bNhqA.gif)
_demo app_

Together, we’ve been able to implement the simplest form of a BLoC in Flutter. The concept remains the same regardless of your use case.

I hope you found this article useful. Please do and share so others can find this article. Hit me up on Twitter @d[evelopia_](https://twitter.com/developia_) with questions or for a chat.

