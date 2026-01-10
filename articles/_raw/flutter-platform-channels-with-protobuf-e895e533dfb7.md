---
title: How to set up Flutter platform channels with Protobuf
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-31T10:18:45.000Z'
originalURL: https://freecodecamp.org/news/flutter-platform-channels-with-protobuf-e895e533dfb7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qoKGLp8R3kVLlJ6bKlNkBw.jpeg
tags:
- name: android app development
  slug: android-app-development
- name: Dart
  slug: dart
- name: Flutter
  slug: flutter
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By TruongSinh Tran-Nguyen

  This post is intermediate-advanced level. It is aimed for the audience who is going
  to write custom platform-specific code as a Flutter plugin.

  TLDR: When writing platform-specific code as Flutter plugins, you should use Pro...'
---

By TruongSinh Tran-Nguyen

This post is intermediate-advanced level. It is aimed for the audience who is going to [write custom platform-specific code as a Flutter plugin](https://flutter.dev/docs/development/platform-integration/platform-channels).

TLDR: When writing platform-specific code as Flutter plugins, you should use ProtoBuf for type-safety, high performance, and a superb development experience. The example code and all 5 steps are available on my [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf).

![Image](https://cdn-media-1.freecodecamp.org/images/1*qoKGLp8R3kVLlJ6bKlNkBw.jpeg)

### The Problem

When writing platform-specific code as Flutter plugins, one of the key things is data transfer between the Dart side and the platform side. Under the hood, it’s just a bunch of binary 0s and 1s. Though all the code we’re dealing with (Dart, Java/Kotlin, ObjC/Swift) is typed, so Flutter makes it easier to have some typing:

However, looking at the table above, you will notice several things:

* FlutterStandardTypedData family is troublesome. (Believe me, been there done that ?)
* Any more complicated structure than those more or less “primitive” types will need to use `List<dynam`ic>`; and Map<String,` dynamic>`;, in w`hich dynamic should be a red flag.

Let’s look at my common error casting `List` (and the same happens with `Map`):

and how verbose it is to do correctly:

This is just a top level `List`/`Map`, imagine you have to go deep into the data structure that you have to pass back and forth between Dart and platform-specific:

So, to sum up:

* `FlutterStandardTypedData` is frustrating.
* Casting data is a nightmare.
* When dealing with `List`/`Map` , we lose type-safety (especially with typos in `Map`’s key, or refactoring code/structure).
* `List<dynam`ic>`; and Map<String,` dynamic> are not particularly good in terms of performance.

### The solution

[Protocol Buffers](https://developers.google.com/protocol-buffers/), aka Protobuf, is a language-neutral, platform-neutral, extensible mechanism for serializing structured data, which happens to support:

* [Dart](https://developers.google.com/protocol-buffers/docs/darttutorial) (maintained by Google)
* [Java](https://developers.google.com/protocol-buffers/docs/javatutorial) (maintained by Google)
* [Kotlin via Java bindings](https://github.com/protocolbuffers/protobuf/issues/3742) (Non-JVM Kotlin is not yet supported, but it’s not our problem)
* [ObjC](https://github.com/protocolbuffers/protobuf/tree/master/objectivec) (maintained by Google)
* [Swift](https://github.com/apple/swift-protobuf) (maintained by Apple)

So, let’s deep dive!

#### Prepare the project

I will create the plugin project with Kotlin and Swift (because I love them), it is the same for Java and ObjC anyway.

```
flutter create -t plugin -i swift -a kotlin plugin_with_protobuf
```

Then you should see

```
All done!
```

```
[✓] Flutter is fully installed. (Channel master, v1.4.2, on Mac OS X 10.14.3 18D109, locale en-US)
```

```
[✓] Android toolchain - develop for Android devices is fully installed. (Android SDK version 28.0.3)
```

```
[✓] iOS toolchain - develop for iOS devices is fully installed. (Xcode 10.2)
```

```
[✓] Android Studio is fully installed. (version 3.3)
```

```
[✓] VS Code is fully installed. (version 1.32.3)
```

```
[!] Connected device is not available.
```

```
Run "flutter doctor" for information about installing additional components.
```

```
In order to run your application, type:
```

```
$ cd plugin_with_protobuf/example
```

```
$ flutter run
```

```
Your application code is in plugin_with_protobuf/example/lib/main.dart.
```

```
Your plugin code is in plugin_with_protobuf/lib/plugin_with_protobuf.dart.
```

```
Host platform code is in the "android" and "ios" directories under plugin_with_protobuf.
```

```
To edit platform code in an IDE see https://flutter.io/developing-packages/#edit-plugin-package.
```

Now run the project to make sure everything’s right. I assume you already have a device connected or simulator/emulator running

```
cd plugin_with_protobuf/exampleflutter run
```

Or easier, use your preferred IDE, either VS Code or Android Studio / IntelliJ. Anyway, you should have this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*jvE26cm-S4EfzpQWpf4a_A.png)

The current code at this step is available on [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf/tree/step/0).

#### Prepare environments

* Install Protobuf compiler: `brew install protobuf` on Mac, or see the detailed instruction in [README](https://github.com/protocolbuffers/protobuf#protocol-compiler-installation).
* Install Swift-plugin for Protobuf compiler: `brew install swift-protobuf` on Mac, or see the detailed instruction in [README](https://github.com/apple/swift-protobuf#building-and-installing-the-code-generator-plugin).
* Install Dart-plugin for Protobuf compiler: `pub global activate protoc_plugin`
* Install Protobuf extension for IDEs

![Image](https://cdn-media-1.freecodecamp.org/images/1*RIpKgYZTMuvZ9J5mUaQq-A.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*LkpfLs-ny3WZ6Wv9qSMt2g.png)

#### Create proto

Now let’s use an IDE. I’m using both VS Code or Android Studio, but for this one, I will use Android Studio. Open the project `plugin_with_protobuf` (not `plugin_with_protobuf/example`) with Android Studio. Then create a new directory called `protos` , and create a new file `person.proto`

![Image](https://cdn-media-1.freecodecamp.org/images/1*e0FUBz3vtCLjRchHDvguYg.png)

The current code at this step is available on [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf/tree/step/1).

#### Generate proto in Dart

You can see from the first 2 lines in `person.proto`, run the first commands to generate Dart code (you might want to create `gen` directories beforehand).

```
protoc --dart_out=./lib/gen ./protos/person.proto
```

In `pubspec.yaml` , add a dependency for Protobuf runtime as well:

The current code at this step is available on [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf/tree/step/2).

#### Generate proto in Swift

Similar to step 2:

```
protoc --swift_out=./ios/Classes ./protos/person.proto
```

In `ios/plugin_with_protobuf.podspec` , add a dependency for Protobuf runtime as well, note that SwiftProtobuf 1.4 requires minimum iOS 9.0.

The current code at this step is available on [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf/tree/step/3).

#### Send data from Swift and receive in Dart

Open XCode from Android Studio:

![Image](https://cdn-media-1.freecodecamp.org/images/1*aYbh5McitgTRqM7sdagCdg.png)

Create mock data (mock data creation is abbreviated, you can see full diffs on [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf/tree/step/4)), serialize and send it to Dart.

Back to Android Studio, receive and deserialize data:

Some other UI changes are abbreviated, you can see full diffs on [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf/tree/step/4). Now it seems to be working.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TPtVuNPxCHYJdGEin090hA.png)

The current code at this step is available on [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf/tree/step/4).

#### Generate proto and send data from Kotlin

Unlike steps 2 and 3, protos in Java/Kotlin can be automatically generated from Gradle. We just need to use `protobuf-gradle-plugin`.

Similar to step 4, create mock data (mock data creation is abbreviated, you can see full diffs on [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf/tree/step/5)), serialize and send it to Dart.

And because we can already receive data from Dart and display, it “just works.”

![Image](https://cdn-media-1.freecodecamp.org/images/1*IYCf6njmxpJ_1qJjdwJFTw.png)

The current code at this step is available on [GitHub](https://github.com/truongsinh/flutter-plugin-protobuf/tree/step/5).

### Conclusion

Communication between Dart and platform-specific code, especially when it involves complicated data structures, should use a type-safe and high-performance serialization tool, such as ProtoBuf (for example, [BuiltValue](https://github.com/google/built_value.dart) is more or less type-safe but not as high-performant). It is fortunate that ProtoBuf supports all 5 languages and build tools require for Flutter, and is easy to integrate.

Final note: what kind of unit test / integration test do you think we should have for this example? ?

