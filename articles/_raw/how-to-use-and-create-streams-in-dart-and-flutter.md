---
title: How to Use and Create Streams from Scratch in Dart and Flutter – a Beginner's
  Guide
subtitle: ''
author: Daniel Asaboro
co_authors: []
series: null
date: '2024-03-14T13:37:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-and-create-streams-in-dart-and-flutter
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/stream-controller-1.png
tags:
- name: Dart
  slug: dart
- name: Flutter
  slug: flutter
seo_title: null
seo_desc: "Programming can be a rollercoaster ride. It catapults you from feeling\
  \ like a genius to feeling utterly clueless, and back again — all in the blink of\
  \ an eye. \nWhat's even more wild is that this cycle repeats itself countless times\
  \ throughout the day..."
---

Programming can be a rollercoaster ride. It catapults you from feeling like a genius to feeling utterly clueless, and back again — all in the blink of an eye. 

What's even more wild is that this cycle repeats itself countless times throughout the day, and for the entirety of your career as a software developer.

Apart from my personal experience, a prime illustration of this phenomenon that comes to mind is the case of this Reddit User who shared their struggle a few months ago:

![A Reddit user shares their frustration with Flutter streams, streamcontrollers, and websockets and how they work.](https://cdn.hashnode.com/res/hashnode/image/upload/v1709365581794/7085351c-088b-4c10-91ac-9ba947ca3fbd.png)
_A Reddit user shares their frustration with Flutter streams, streamcontrollers, and websockets and how they work._

**Streams are** one of those concepts that can make you go from "_Wow, I'm so smart 🙈_" to "_I'm so freaking dumb 💀 I should probably be on the Farm_". A lot of developers find them difficult to grasp and understand, particularly new Dart and Flutter Developers.

While Streams might be complex, they aren't so complicated that they're impossible to learn. If you put in enough dedication and practice, you can grasp them, a skill that may become necessary sooner or later.

This is because Streams are fundamental, and so many Flutter-based Dart libraries and SDKs (like Firebase, Device Sensors, some State-Management techniques, and heck, even Dart Isolates) heavily rely on them. As a result, learning how to use streams effectively will no doubt elevate your development skills.

## What You'll Learn

When you are done reading, you should be able to:

* Understand what Streams are and what they aren't, recognize the optimal scenarios for using them in your Dart and Flutter applications, and identify situations where alternative approaches may be more suitable.
* Create custom-specific streams in Dart and leverage advanced techniques in transforming them according to your app requirements and for improved performance.
* Implement strategies to tackle common performance challenges associated with streams, ensure your applications run smoothly under diverse conditions, and many more.

## Prerequisites: What Should You Know?

Before we get started and for easy comprehension, you should have a basic understanding of the following topics and concepts:

1. **Asynchronous Code**: Familiarize yourself with the principles of asynchronous programming, how they differ from synchronous ones. Understand how asynchronous techniques contribute to performance, the key concepts like futures, async/await, callbacks, and event loops for a Single-threaded language.
2. **Dart**: Ensure you have a working knowledge of the Dart programming language, including syntax, data types, variables, functions, classes, and a basic understanding of exception handling.
3. **Flutter Framework**: While not strictly necessary, having a basic understanding of Flutter and its key components can be beneficial. Familiarize yourself with Flutter widgets, state management techniques, navigation, and widget lifecycle to better integrate streams into your Flutter applications.

## Table of Contents

While I encourage you to read each of the sections in the order they were written, still feel free to jump to any section that interests you if you grasp the section preceding it.

* [What is a Stream in Dart?](#heading-what-is-a-stream-in-dart)
* [Real-Life Applications of Streams](#heading-real-life-applications-of-streams)
* [How do Streams work](#heading-how-do-streams-work)?
* [How to Work with Streams in Dart](#heading-how-to-work-with-streams-in-dart)
* [How to Create Your Own Stream in Dart](#heading-how-to-create-your-own-stream-in-dart)
* [What about Error Handling with Streams](#heading-what-about-error-handling-in-streams)?
* [Not Everything that Changes Should be a Stream](#heading-not-everything-that-changes-has-to-be-a-stream)
* [Conclusion](#heading-just-get-started)
* [Quick Challenge](#heading-quick-challenge)

## What is a Stream in Dart?

If you are reading this article, chances are you understand Asynchronous Operations — you know how to use Futures with Async-Await. And while you may not have an idea how they work internally ([the event loop concurrency stuff](https://dart.dev/language/concurrency)), you have probably used them to fetch a JSON result from a remote API.

Streams are similar to Futures in that they both work asynchronously.

One of the key differences is that once a Future is called and starts, it can either return a value or it errors out and then stops. A Stream, on the other hand, can deliver a series of values (data and errors) continuously (more on this later).

So it's technically correct to say Futures are single-value streams or one-time response stream operations. If a method or function needs to return more than one result at different time intervals, or requires continuous updates to be handled the same way, you should probably look into streams.

## Real-Life Applications of Streams

Beyond the apparent applications like retrieving data from Firestore or managing Firebase Messages in a chat app, consider scenarios such as scanning for available Bluetooth devices or searching for WiFi hotspots.

![A screenshot showing the process of searching for wifi to illustrate a real-life application of streams.](https://cdn.hashnode.com/res/hashnode/image/upload/v1710138803116/9ae58be0-c0d8-47f8-ae76-668b7ac6c8e3.png)

In such cases, when data becomes available (a new available hotspot connection or device), an event is emitted through a stream. Then listeners subscribed to the stream receive and process these events in their way asynchronously.

It's similar to playing songs on Spotify and watching videos on platforms like YouTube and Netflix. YouTube or Spotify's music server cleverly breaks songs or videos into small, manageable chunks—a stream of bytes so you don't have to wait until the app finishes downloading. Hence, the name: Streaming.

Imagine waiting for a song to download before you can play it!?!

### Your HTTP Get request uses Streams internally

Dart just waits patiently until the stream finishes and then returns all the data at once in the form of a completed future.

```dart
//preceeding code removed for brevity

  client.getUrl(uri)
    .then((req) => req.close())
    .then((response) => response.transform(utf8.decoder).join())
    .then((value) => jsonDecode(value) as List<dynamic>)
    .then((json) => json.map((map) => Todo.fromJson(map)).toList())
    .then((retrievedTodos) {
      for (final todo in retrievedTodos) {
        print('Todo: ${todo.title}, Completed: ${todo.completed}');
      }
    })
    .catchError((e) {
      print('Error: $e');
    })
    .whenComplete(() {
      client.close();
    });

// section only for illustration
```

Here's an Async-Await version that's commented:

```dart
import 'dart:convert';
import 'dart:io';

class Todo {
  final int id;
  final String title;
  final bool completed;

  Todo({
    required this.id,
    required this.title,
    required this.completed,
  });

  factory Todo.fromJson(Map<String, dynamic> json) {
    return Todo(
      id: json['id'],
      title: json['title'],
      completed: json['completed'],
    );
  }
}

void main() async {
  final uri = Uri.parse('https://jsonplaceholder.typicode.com/todos');
  final client = HttpClient();

  try {
    final request = await client.getUrl(uri);
    final response = await request.close();

    final jsonString = await response.transform(utf8.decoder).join();
    final json = jsonDecode(jsonString) as List<dynamic>;

    final retrievedTodos = json.map((map) => Todo.fromJson(map)).toList();

    for (final todo in retrievedTodos) {
      print('Todo: ${todo.title}, Completed: ${todo.completed}');
    }
  } catch (e) {
    print('Error: $e');
  } finally {
    client.close();
  }
}

```

It should be no surprise that downloading a file leverages this technique too.

Generally, you will need streams when dealing with anything involving a form of "connection" according to Remi Rouselet, the Author of Provider and Riverpod Package.

If that's clear, let's get practical.

## How Do Streams Work?

Streams operate similarly to conveyor belts commonly seen at airports.

They act as channels that smoothly transport various items from one end to the other. Generally, you add luggage or bags onto a conveyor belt and they're carried along in its path. You can add data or events to a stream in the same way.

Where you put in items is called the source.

As the items move along the conveyor belt, workers stationed along the belt observe and interact with them. These workers represent the listeners or subscribers to the stream.

They may examine, categorize, or manipulate the items based on specific criteria.

Some workers may only be interested in specific types of items and let others pass by, while others may modify or combine items as they pass through their station. This reflects the concept of filtering, transforming, or aggregating events in the stream which we will get into later in this piece.

## How to Work with Streams in Dart

You have two choices:

* use a stream that already exists, or
* make one from scratch.

It's usually easier to use a stream that's already there instead of making a new one just to use it elsewhere in your app. So let's start with the idea of using an already-created stream of data.

But first, you should know that there are two kinds of streams:

1. A single-subscription stream
2. A broadcast stream

### A single subscription stream is the default in Dart

A single subscription only allows a single listener/subscriber during its whole lifetime. It doesn't even matter if you cancel an old subscription – you can't subscribe again. Any attempt to resubscribe will yield the `Bad State` error:

```dart
import 'dart:async';

void main() {
  // Create a StreamController
  StreamController<int> streamController = StreamController<int>();

  // Listen to the stream
  StreamSubscription<int> subscription = streamController.stream.listen(
    (int data) {
      print('Received data: $data');
    },
  );

  // Cancel the subscription
  subscription.cancel();

  // Try to listen to the stream again with the same subscription
  try {
    subscription = streamController.stream.listen(
      (int data) {
        print('Received data again: $data');
      },
    );
  } catch (e) {
    print('Error: $e'); // Handle the error
  }

  // Close the stream controller
  streamController.close();
}}
```

![The error message you get from the stream is: "Error: Bad State: Stream has already been Listened to".](https://cdn.hashnode.com/res/hashnode/image/upload/v1710052410984/6a1556d2-d90c-4878-b180-c1bcf427d667.png)

This is useful when the order in which the information arrives is critical and any misalignment will make the data unreadable or impossible to interpret such as when an HTTP GET request, reading a file, or processing messages in a chat application.

Also, a single-subscription stream is the most efficient kind of stream because it doesn't start generating events until it has a listener, and it stops sending events when the listener unsubscribes, even if there are still more events to emit.

But what if you want more than a single listener?

What if you need to share the same data stream across multiple components or widgets in your application? What if a collaborative feature involves real-time updates, and various parts of your application need to react simultaneously – what do you do?

### That's where the Broadcast Stream comes in

Unlike a single-subscription stream, a broadcast stream allows any number of listeners. What's interesting is that it fires its events when they are ready without checking if there are listeners or not.

That's quite inefficient, isn't it? So it's essential to exercise caution with broadcast streams as they lead to memory leaks if not managed properly. After all, don't they say that with great power comes great responsibility?

Broadcast streams are well-suited for situations where each event can be handled without relying on previous events and can be processed by the user as soon as it's received – for example, breaking news, sports scores, or weather alerts.

![English Premier League Livescore used to illustrate a notification stream that doesnt' rely on previous events](https://cdn.hashnode.com/res/hashnode/image/upload/v1710138971106/3b426c19-ca45-45f8-9ddd-ead192f34e0f.png)

It's worth noting that all subscribers are unsubscribed once a `done` event is fired. Then any new subscriber will simply get the done event and stop listening.

```dart
import 'dart:async';

void main() {
  // Create a StreamController
  StreamController<int> streamController = StreamController<int>();

  // Listen to the stream
  streamController.stream.listen(
    (int data) {
      print('Received data: $data');
    },
    onDone: () {
      print('Stream is done.');
    },
  );

  // Add data to the stream
  streamController.add(1);
  streamController.add(2);

  // Close the stream controller
  streamController.close();

  // Try to subscribe again after the stream is closed

  Future.delayed(Duration.zero, () {
    try {
      streamController.stream.listen(
        (int data) {
          print('New subscriber received data: $data');
        },
        onDone: () {
          print('New subscriber received the done event.');
        },
      );
    } catch (e) {
      print(e);
      print('New subscriber is no longer listening.');
    }
  });
}
```

![Result after running the code above. First 1 and 2 are printed, then the Stream is mark done. But if you try to listen to it again, it will say Stream has already been listening to](https://cdn.hashnode.com/res/hashnode/image/upload/v1710052967862/464e7a7e-ab6d-431c-8e70-09dc629a8dfd.png)

What about creating our own streams that others can subscribe to?

## How to Create Your Own Stream in Dart

Currently, there are three ways to create a new Stream in Dart:

1. Transforming existing streams
2. Using an async generator
3. Using stream controllers

### How to create streams by transforming existing streams

I didn't really think of these as a standalone method for creating streams because it requires you to rely on another stream. But going through the Dart documentation made me realize we are actually creating a new stream entity whenever we transform another stream. It's quite meta, actually...

```dart
import 'dart:async';

void main() {
  // Create a stream of integers
  final Stream<int> originalStream = Stream<int>.fromIterable([1, 2, 3, 4, 5]);

  // Transform the original stream using map()
  final Stream<int> transformedStream = originalStream.map((int value) {
    return value * 2; // Double each integer
  });

  // Listen to the transformed stream
  final StreamSubscription<int> subscription =
      transformedStream.listen((int value) {
    print('Transformed value: $value');
  });

  // Close the subscription and the streams after a delay
  Future.delayed(Duration(seconds: 1), () {
    subscription.cancel();
  });
}
```

The result:

![Result from the above code where each stream data is multipled by two giving: Transformed value: 2, 4, 6 etc](https://cdn.hashnode.com/res/hashnode/image/upload/v1709919319018/3fb5a20c-7dfc-4d11-bfc5-fda51ff4fd93.png)
_Result from the above code where each stream data is multipled by two_

This examples gets a Firebase Firestore data Stream and maps it to the UI:

```dart


//code removed for brevity

class FirestoreService {
  final CollectionReference _collectionReference =
      FirebaseFirestore.instance.collection('messages');

  Stream<List<Map<String, dynamic>>> getMessages() {
    return _collectionReference.snapshots().map((snapshot) =>
        snapshot.docs.map((doc) => doc.data() as Map<String,     		dynamic>).toList());
  }
  
  Future<void> addMessage(String message, String sender) async {
  // your code...
  }
  
  // other methods removed for brevity
}

void main() {
  final firestoreService = FirestoreService();

  // Listen to messages
  final Stream<List<Map<String, dynamic>>> messageStream =
      firestoreService.getMessages();
  messageStream.listen((messages) {
    print('Received messages: $messages');
  });

  // Add a new message
  firestoreService.addMessage('Hello Firestore!', 'Dart User');
}

// other code for brevity
```

Other common transformation methods are `take()`, `expand()`, and `where()`. If your application demands more advanced transformations (for example, converting the HTTP Get response using UTF-8 decoding) beyond these standard methods, explore the [stream transformer class](https://api.dart.dev/stable/3.3.0/dart-async/StreamTransformer-class.html) for additional capabilities.

### How to create streams using generators

Here, you make use of what is called the async generator function.

It's a function marked with `async *` instead of `async` to differentiate it from futures. This function runs asynchronously and sends back a value whenever it sees a `yield` keyword, but it won't stop executing the function code body like a `return` would.

```dart
import 'dart:async';

// Define an asynchronous generator function
Stream<int> countStream(int max) async* {
  for (int i = 1; i <= max; i++) {
    // Yield each value asynchronously
    await Future.delayed(Duration(seconds: 1));
    yield i;
  }
}

void main() {
  // Create a stream using the asynchronous generator function
  Stream<int> stream = countStream(6);

  // Subscribe to the stream
  stream.listen((value) {
    print('Received: $value');
  }, onDone: () {
    print('Stream is done');
  });
}
```

**Here's how it works:**

The stream is created when you call or invoke the function.

But it only starts running when you listen to the stream because streams are lazy-loaded. It can emit events on the stream by using `yield` or `yield*` statements until the function returns, then the stream closes.

#### How is a yield different from a return and how does it work?

In Dart, "return" is used to immediately exit a function and return a value to the caller. When a function encounters a return statement, it terminates its execution and passes control back to the caller, along with the specified return value.

Subsequent calls to the function will start execution from the beginning.

```dart
import 'dart:async';

// Function that returns a Future<int> after a delay
Future<int> fetchUserData() async {
  await Future.delayed(Duration(seconds: 2)); // Simulate a delay
  return 42; // Simulated user data
}

void main() async {
  print('Fetching user data...');

  try {
    // Initiating the asynchronous operation and waiting for the result
    int userData = await fetchUserData();
    print('User data received: $userData');
  } catch (error) {
    print('Error fetching user data: $error');
  }

  print('Continuing with other tasks...');
}
```

In contrast, when a function encounters a "yield" statement in an async generator, it suspends its execution, returns the value specified by "yield" to the caller, and preserves the state of the function. This allows the function to resume execution from where it left off when the next value is requested.

```dart
import 'dart:async';

// Asynchronous generator function
Stream<int> countStream(int max) async* {
  for (int i = 1; i <= max; i++) {
    // Simulate asynchronous delay
    await Future.delayed(Duration(seconds: 1)); 
    yield i; // Yield each value in the sequence
  }
}

void main() async {
  // Create a stream using the asynchronous generator function
  Stream<int> stream = countStream(5);

  // Subscribe to the stream using await for loop
  await for (int value in stream) {
    print('Received: $value');

    // Simulate additional processing
    await Future.delayed(Duration(milliseconds: 500));
  }

  print('Stream is done');
}
```

In the example above, the function `countStream()` is a generator function that produces a sequence of integers from 0 to 4 lazily using the "yield" keyword.

Each time the function is called, it returns the next value in the sequence without generating the entire sequence upfront. This can be useful for conserving memory and processing large datasets efficiently.

Note that, the `Stream` created by a `async*` function is always a single-subscription stream. This is because a `async*` function is intended to execute normally until it's done similar to the normal control flow of a single (asynchronous) function.

What if you want a broadcast stream — what do you do?

Hint: I've already answered that in this article.

Finally, an interesting thing that the [official documentation](https://dart.dev/articles/libraries/creating-streams#:~:text=It's%20rare%20to%20have%20an,from%20other%20asynchronous%20event%20sources.) pointed out, which I haven't really taken note of, is that:

> It's rare to have an `async*` function building a stream from nothing. It needs to get its data from somewhere, and most often that somewhere is another stream.

That makes you still dependent on other streams. What if you need to go granular and start from scratch? That's where the `StreamController` class comes in.

### How to create streams using stream controllers

Stream controllers are well suited for situations where the events of your stream come from different parts of your program, and/or can't be gotten from another stream or future.

A few examples that come to mind are managing user input events, handling data from diverse sources, or creating custom events within your application like state updates, progress notifications, or system alerts.

Stream controllers are low-level, as I understand. They don't just give you a stream, they give you ways to add events to it at any point including the [logic necessary to handle listeners and pausing](https://api.dart.dev/stable/dart-async/StreamController-class.html).

```dart
import 'dart:async';

void main() {
  // Create a stream controller to manage user input events
  StreamController<String> userInputController = StreamController<String>();

  // Listen to user input events
  userInputController.stream.listen((String userInput) {
    print('User input: $userInput');
  });

  // Simulate user input events
  userInputController.add('Hello');
  userInputController.add('World');

  // Create a custom stream controller for progress notifications
  StreamController<double> progressController = StreamController<double>();

  // Listen to progress notifications
  progressController.stream.listen((double progress) {
    print('Progress: $progress');
  });

  // Simulate progress notifications
  for (double i = 0; i <= 1; i += 0.2) {
    progressController.add(i);
  }

  // Create a custom stream controller for system alerts
  StreamController<String> systemAlertController = StreamController<String>();

  // Listen to system alerts
  systemAlertController.stream.listen((String alert) {
    print('System Alert: $alert');
  });

  // Simulate system alerts
  systemAlertController.add('System overload detected!');
  systemAlertController.add('Database connection lost!');

  // Close all stream controllers when done
  userInputController.close();
  progressController.close();
  systemAlertController.close();
}
```

It has four callback methods:

1. `onListen`
2. `onCancel`
3. `onResume`
4. `onPause`

If you want to know when the stream has been subscribed to, pass an onListenHandler to the `onListen` parameter when you create the `StreamController`.

```dart
import 'dart:async';

void main() {
  // Create a StreamController with an onListen callback
  StreamController<int> streamController = StreamController<int>(
    onListen: () {
      print('Stream has been subscribed to.');
    },
  );

  // Listen to the stream
  streamController.stream.listen((int data) {
    print('Received data: $data');
  });

  // Add data to the stream
  streamController.add(1);
  streamController.add(2);
  streamController.add(3);

  // Close the stream controller when done
  streamController.close();
}
```

The `onListen` callback is called when the stream gets its first subscriber. `onCancel`, on the other hand, is triggered when the controller loses its last subscriber.

```dart
import 'dart:async';

void main() {
  // Create a StreamController with onCancel callback
  StreamController<int> streamController = StreamController<int>(
    onCancel: () {
      print('Last subscriber canceled, stream controller is now inactive.');
    },
  );

  // Listen to the stream
  StreamSubscription<int> subscription = streamController.stream.listen((int data) {
    print('Received data: $data');
  });

  // Add data to the stream
  streamController.add(1);
  streamController.add(2);

  // Cancel the subscription
  subscription.cancel();

  // Add more data to the stream after canceling the subscription
  streamController.add(3);

  // Close the stream controller
  streamController.close();
}

//##Note: 

//When you use async* and yield*, 
//you're creating a function that can asynchronously yield values,
//potentially generating a new stream of values each time it's called.

//When you return a stream,
//you're passing around a reference to an existing stream object without
//necessarily generating new values or modifying the stream itself.
```

Remember when I said that StreamControllers are low-level?

What this generally means is that you have control over everything. However, this comes with the responsibility of implementing features that higher-level stream creation methods provide out of the box.

### One such feature is known as "honouring the pause"

When a stream subscription to an async* generator is paused, the generator function automatically pauses at a yield statement, ensuring that no new events are emitted until the subscription resumes.

But with StreamControllers, events continue to be generated and buffered during pauses. If the event-producing code fails to respect the pause, the buffer size can grow indefinitely, leading to potential memory issues.

Moreover, if the listener stops listening shortly after pausing, all the effort spent creating the buffer is wasted. Grossly inefficient, isn't it? Imagine a long-running operation.

Here's how to resolve it:

```dart
Stream<int> integerCounter(Duration interval, [int? maxCount]) {
  late StreamController<int> controller;

  void onListenHandler() {
    //code removed for brevity;
  }
  void onPauseHandler() {
    //code removed for brevity;
  }
  void onResumeHandler() {
    //code removed for brevity;
  }
  void onCancelHandler() {
    //code removed for brevity;
  }

  controller = StreamController<int>(
    onListen: onListenHandler,
    onPause: onPauseHandler,
    onResume: onResumeHandler,
    onCancel: onCancelHandler,
  );

  return controller.stream;
}
```

### Another one is something I call "Pause-Subscription Synchronization"

This term refers to the synchronization between the subscription and pause states of a StreamController. If both the subscription and pause states change simultaneously, only the `onListen` or the `onCancel` callback is triggered.

This is why it's advisable to implement all available listeners—`onListen`, `onCancel`, `onPause`, and `onResume`—to mitigate potential issues and ensure proper functionality. This way, you can effectively monitor changes in the pause state and avoid hard-to-track bugs that may arise from unexpected behaviour.

Oh, and don't ever forget to dispose of your controller:

```dart
import 'dart:async';

void main() {
  // Create a StreamController
  StreamController<int> streamController = StreamController<int>();

  // Listen to the stream
  StreamSubscription<int> subscription = streamController.stream.listen((int data) {
    print('Received data: $data');
  });

  // Add data to the stream
  streamController.add(1);
  streamController.add(2);

  // Dispose of the subscription and stream controller
  subscription.cancel();
  streamController.close(); // call the close method to dispose
}
```

## What about Error Handling in Streams?

When errors arise within a stream, the stream manages them similarly to how it handles data events—by informing listeners through error events. Generally, streams demonstrate two clear behaviours in reaction to errors:

1. The stream notifies the first error event and then halts further processing.
2. The stream notifies error event(s) but continues delivering subsequent events.

Let's take each at a time.

### Stopping after the first error

In this scenario, the stream stops after encountering the first error, but it provides insight into the initial issue and discontinues any further event transmission. This is useful when the order of importance is critical and any missing piece is enough to make the whole file unusable.

```dart
import 'dart:async';

void main() {
  // Create a StreamController
  StreamController<int> streamController = StreamController<int>();

  // Listen to the stream
  StreamSubscription<int> subscription = streamController.stream.listen(
    (int data) {
      print('Received data: $data');
    },
    onError: (error) {
      print('Error occurred: $error');
    },
    onDone: () {
      print('Stream is done.');
    },
  );

  // Add data to the stream
  streamController.add(1);
  streamController.add(2);
  streamController.addError('Error: Something went wrong'); // Simulate an error
  streamController.add(3);

  // Close the stream controller
  streamController.close();
}
```

From what you've learned, this is peculiar to async generator functions or single subscription streams. What if your case is different, say you want to continue after you encounter an error in a Stream, what do you do?

### Continuing after the first error

Unlike scenarios where streams stop after the first error, continuing after errors enables the stream to maintain its flow. This provides ongoing insights and updates to downstream consumers.

This approach is invaluable in scenarios where the stream's uninterrupted operation is paramount, such as real-time data processing or continuous monitoring systems. Streams that continue after errors offer resilience and adaptability, ensuring that critical information is not lost due to isolated incidents.

Let's look at an example:

```dart
import 'dart:async';

void main() async {
  // Create a stream controller
  StreamController<int> streamController = StreamController<int>();

  // Generate numbers asynchronously with a delay of 1 second
  int count = 0;
  Timer.periodic(Duration(seconds: 1), (Timer timer) {
    // Simulate errors for demonstration
    if (count % 3 == 0) {
      streamController.addError('Error: Failed to generate number $count');
    } else {
      streamController.add(count);
    }
    count++;
  });

  // Listen to the stream
  streamController.stream.listen(
    (int data) {
      print('Received data: $data');
    },
    onError: (error) {
      print('Error occurred: $error');
    },
  );
}

```

## Not Everything that Changes Has to Be a Stream

Streams offer great functionality by emitting events (data or error values) without concerning themselves with how they are consumed and this gives developers the flexibility to write code with low coupling and high extensibility. But they shouldn't be tied to everything that changes.

According to Randal Schwartz, [State Management is a great example](https://www.reddit.com/r/FlutterDev/comments/1586sfg/whats_a_real_world_use_case_of_a_dart_stream/) of this.

I reached out to him to be sure I understand his stance, and here's what he says:

> "The key difference, as clarified to me by Remi, is that there is a place for streams when every event must be included, vs typical state management, where only the most recent state (and notification when it changes) is relevant. If something quickly goes from 1 to 2 to 3, but you then rebuild based on 3, that's enough."

In other words, you don't care about the intermediate, only the latest ones.

State is something you have to manage through your app's entire lifecycle. If it's done poorly, your apps might suffer performance issues and lag due to excessive or large-scale rebuilds.

So minimize unnecessary updates, and rebuild only components that genuinely need rebuilding to optimise overall performance. Remember, Dart is single-threaded.

## Just Get Started

I don't expect you to grasp every detail presented here in one go even though I've dedicated countless hours spanning weeks to refine this tutorial. So don't feel pressured to.

Instead, feel free to bookmark for when you're ready to continue. If anything seems unclear, please refer to the credits and recommended resources or you can reach out to me on Twitter.

The undeniable truth is that you can consume endless tutorials and videos, but true confidence comes when you apply your knowledge to real-world problems and resolve them (I have three for you down below)

Approach this tutorial like you will use a stream to handle a large resource – break it into smaller, digestible chunks and process them at your convenience. It doesn't matter if it's irregular, just make sure to tackle it.

If any confusion arises, share it in the comments, tweet at me on Twitter (Now X), or reach out to me through the DM. I will be glad to help you resolve them and bring some clarity. Goodbye!

## Quick Challenge

1. How would you implement ChatGPT's typing style with streams?
2. Say you are assigned a new task. On button press, your app should:  
– download a compressed file,  
– extract the file into a   
– find an executable binary file, and run it,  
– return a list of directories that should be added to PATH.

		How would you resolve it with what you've learn so far in this tutorial?

3.  How can you use streams to communicate when a user is typing or not?

### Credits:

1. [Flutter Stream Basics for Beginners](https://medium.com/flutter-community/flutter-stream-basics-for-beginners-eda23e44e32f) by Dane Mackier.
2. [Streams: Asynchronous Programming with Dart](https://ptyagicodecamp.github.io/streams-asynchronous-programming-with-dart.html) by Priyanka Tyagi
3. [Difference between `await for` and `listen`](https://stackoverflow.com/questions/42611880/difference-between-await-for-and-listen-in-) answered on StackOverflow.
4. [Simple Beginners Guide to Streams | Flutter and Dart Stream Basics](https://www.youtube.com/watch?v=53jIxLiCv2E) by FilledStacks [Youtube Video]
5. [Streams: API documentation](https://api.flutter.dev/flutter/dart-async/Stream-class.html) on Flutter dot Dev

