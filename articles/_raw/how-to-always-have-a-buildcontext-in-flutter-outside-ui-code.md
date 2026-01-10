---
title: How to Always Have A BuildContext in Flutter Outside of UI Code
subtitle: ''
author: Obum
co_authors: []
series: null
date: '2024-03-19T14:42:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-always-have-a-buildcontext-in-flutter-outside-ui-code
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/Untitled-design.png
tags:
- name: Flutter
  slug: flutter
seo_title: null
seo_desc: "The BuildContext provides important app-wide configuration information\
  \ to all widgets in the widget tree. It is always naturally available in build methods\
  \ and within State classes. \nIn this article, we will explore how we can obtain\
  \ a valid BuildCon..."
---

The BuildContext provides important app-wide configuration information to all widgets in the widget tree. It is always naturally available in build methods and within State classes. 

In this article, we will explore how we can obtain a valid BuildContext outside the scope of its natural availability.

## Table Of Contents

* [Introduction](#heading-introduction)
* [The essence of the BuildContext in Flutter](#heading-the-essence-of-the-buildcontext-in-flutter)
* [The need for a BuildContext outside UI code](#heading-the-need-for-a-buildcontext-outside-ui-code)
* [Having a globally available navigatorKey](#heading-having-a-globally-available-navigatorkey)
* [A note on Navigator 2.0](#heading-a-note-on-navigator-20)
* [Using navigatorKey's NavigationState to show toasts](#heading-using-navigatorkeys-navigationstate-to-show-toasts)
* [Summary](#heading-summary)

## Introduction

Flutter is a UI toolkit for building desktop, mobile, and web apps. Flutter is a framework that allows you to build apps in the Dart programming language.

In Flutter, you build UIs by composing widgets. A widget is any logical piece of what is renderable on the screen like Icon, Image, Text, and so on.

Composing widgets involves setting them as a child or as children of other parent widgets. In other words, you are building a widget tree.  All the widgets in your UI tree have access to the BuildContext.

## The Essence of the BuildContext in Flutter

The BuildContext provides important app-wide configuration information to all widgets in the widget tree.

The BuildContext is to Flutter widgets what water is to our body. Just as water circulates round our system with nutrients and oxygen, so does the BuildContext provide runtime-specific values to every widget in our apps.

In Flutter, you commonly create a widget by extending the StatelessWidget or StatefulWidget (and its State) classes. 

In both cases, you have to override the build method. In the build method, you must return another widget. By this way, you keep building the widget tree.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/widget_tree.png)
_Image Source: https://groups.google.com/g/flutter-dev/c/jfPgd5FS6EM_

All build methods take only one argument: the BuildContext. You need the BuildContext in Flutter to render the UI. It is indispensable. The Flutter framework itself provides the BuildContext to each widget's build method.

The BuildContext gives you access to getters and methods like:

* [`findAncestorStateOfType`](https://api.flutter.dev/flutter/widgets/BuildContext/findAncestorStateOfType.html): a _typed_ method that returns the `State` object of the specified `StatefulWidget`.
* [`getInheritedWidgetOfExactType`](https://api.flutter.dev/flutter/widgets/BuildContext/dependOnInheritedWidgetOfExactType.html): a _typed_ method that returns a requested widget type that is found upper in the widget tree.
* [`mounted`](https://api.flutter.dev/flutter/widgets/BuildContext/mounted.html): a `bool` which tells whether the widget _in context_ is in view.

There are other useful getters and methods available on the BuildContext. Outside them, the BuildContext is also important because through it, we can obtain the app's active instance of specific classes. For example: MediaQuery, Navigator, Theme, and so on.

A common pattern is to call the static `.of` method on the class of interest and provide our BuildContext (or just "context") to this `.of` method.

```dart
final isLandscape = MediaQuery.of(context).orientation == Orientation.landscape;
final hasConfirmed = Navigator.of(context).pop(false);
final lightTheme = Theme.of(context).copyWith(brightness: Brightness.light);

```

The `.of` is the most common pattern. However, there are other more direct, specific, and rare use cases of such static getters that rely on the context.

```dart
final isDarkTheme = Theme.brightnessOf(context) == Brightness.dark;

```

You can also create static getters of instances of your classes that rely on the BuildContext. [You can learn more about how to do that (through InheritedWidget) here](https://api.flutter.dev/flutter/widgets/InheritedWidget-class.html).

As we see, the following are why we need the BuildContext:

* To build widgets,
* To access resources,
* To obtain instances of classes,
* and so on.

## The need for a BuildContext outside UI code

The BuildContext is naturally available inside all build methods and inside the `State` class of `StatefulWidgets`. Most method calls with context inside these scopes will work as intended.

In minor occasions, you will need to access the BuildContext from where it is not naturally available. You will want to obtain runtime instances outside of UI code (outside build methods and `State` classes).

This is usually difficult as we can't instantiate a BuildContext of our own. We only have access to one once our app has started running.

Popular reasons of accessing the BuildContext this way is either when performing navigation, when showing alerts and modals in non-UI code, or when triggering UI updates from changes in the app's state architecture.

Also, when a user opens a notification, we want to navigate the user to the target screen if the app is already open. We need the BuildContext to do this.

## Having a globally available navigatorKey

A solution to always having a BuildContext in Flutter is by providing one yourself at the start of the application.

The top-most widget of Flutter apps is usually either [`CupertinoApp`](https://api.flutter.dev/flutter/cupertino/CupertinoApp-class.html), [`MaterialApp`](https://api.flutter.dev/flutter/material/MaterialApp-class.html), or [`WidgetsApp`](https://api.flutter.dev/flutter/widgets/WidgetsApp-class.html). In other words, they are the entry-point of our application.

These "app" widgets take an optional `navigatorKey` parameter. It has the type of `GlobalKey<NavigatorState>`. This NavigatorState-specific GlobalKey has a BuildContext attached to it once the app is running. 

When you create a navigatorKey and give it to the top-most "app" widget, your Flutter app will keep the BuildContext it is using in your navigatorKey. That way, you can have access to the BuildContext wherever you have access to the navigatorKey.

Create and expose the navigatorKey as a _static final_ variable from a global utility class. Provide it to the top-most "app" widget. Then obtain the context from this globally-available class wherever you need it.

```dart
/* In services/navigation_service.dart */
class NavigationService {
  static final navigatorKey = GlobalKey<NavigatorState>();

  // ... other methods and getters
}

/* In main.dart */
import 'package:flutter/material.dart';

import 'services/navigation_service.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      navigatorKey: NavigationService.navigatorKey, // line of interest
      home: const Scaffold(body: Center(child: Text('BuildContext'))),
    );
  }
}

/* In services/modal_service.dart */
import 'package:flutter/material.dart';

import 'services/navigation_service.dart';

Future<T?> showModal<T>(Widget modal) async {
  return await showModalBottomSheet<T>(
    context: NavigationService.navigatorKey.currentContext!,
    backgroundColor: Colors.transparent,
    isScrollControlled: true,
    builder: (_) => modal,
  );
}

```

In the example above, you can see how we can call [`showModalBottomSheet`](https://api.flutter.dev/flutter/material/showModalBottomSheet.html) from a non-widget file by using the context from the navigatorKey. This will only work if this key has been attached to the top-most "app" widget as shown in the code snippet.

This way of accessing the BuildContext has always been around. [We can see it in use in the Stacked Architecture](https://github.com/Stacked-Org/stacked/blob/53ef130d36db1d8d6756375cb8e9495f82c1d771/example/navigator_example/lib/main.dart#L20).

You could keep the navigatorKey in an entirely different class from some NavigationService. It could also be a standalone global variable in your Flutter project. Furthermore, you could make it available through the state management architecture you are using.

The manner in which you make the navigatorKey globally available is up to you. What is necessary is that you provide one to Flutter when you need the BuildContext outside UI code.

## A note on Navigator 2.0

There is a special configuration that is worthy of mention at this point. 

The top-most "app" widgets (CupertinoApp, MaterialApp, and WidgetsApp) all have a `.router` constructor. This constructor is different from the direct equivalent because it creates an app that uses a [`Router` instead of a `Navigator`](https://docs.flutter.dev/ui/navigation).

Specifically, the `.router` apps allow us to perform declarative navigation (`router.go`) instead of only imperative navigation (`navigator.push` and `navigator.pop`). 

Declarative navigation works well with deep linking (when mobile apps open URLs) and with the browser history (a plus to Flutter web).

These `.router` constructors don't take a navigatorKey argument. However, they can accept various router-specific classes as arguments. In these classes, you can provide a navigatorKey in one way or the other.

For example, [`go_router`](https://pub.dev/packages/go_router) is a well-known package for Navigator 2.0 in Flutter. It abstracts out the complexities of those router-specific classes. 

Now, the [`GoRouter`](https://pub.dev/documentation/go_router/latest/go_router/GoRouter-class.html) constructor, as you will expect, accepts a navigatorKey argument. This way, if you are using it, you can still have access to the BuildContext in any non-UI code in your Flutter project.

## Using navigatorKey's NavigationState to show toasts

An added advantage of having an attached navigatorKey is when we want to toast information to the user. 

We can do this by adding an [`OverlayEntry`](https://api.flutter.dev/flutter/widgets/OverlayEntry-class.html) (with a toast widget) into the `overlay` of `NavigatorState` that is attached to our navigatorKey.

With the help of a `Timer`, the toast gets dismissed after a few seconds:

```dart
/* In services/toast_service.dart */
import 'dart:async';

import 'navigation_service.dart';

Widget _toast(String text) => Container(
    padding: const EdgeInsets.fromLTRB(16, 12, 16, 12),
    decoration: BoxDecoration(
      borderRadius: BorderRadius.circular(6),
      color: Colors.teal,
    ),
    child: Text(text),
  );

class ToastService {
  static OverlayEntry? _entry;
  static Timer? _timer;

  static show(String text) {
    _dismiss();
    _entry = OverlayEntry(builder: (context) => _Toast(text));
    NavigationService.navigatorKey.currentState!.overlay!.insert(_entry!);
    _timer = Timer(const Duration(seconds: 5), _dismiss);
  }

  static _dismiss() {
    try {
      _timer?.cancel();
      _timer = null;
      _entry?.remove();
      _entry = null;
    } catch () {
    }
  }
}

/* In services/auth_service.dart */
import 'toast_service.dart';

class AuthService {
  static void login({required String email, required String password}) async {
    // ... calling the API

    // toast after a successful login
    ToastService.show('Welcome Back!');
  }
}

```

## Summary

"context" is something you will always use in Flutter. 

When you need it outside the build method (or State classes), create a navigatorKey and attach it to the top-most "app" widget. 

You can then access the same context that your UI code uses from this key from anywhere within the Flutter project.

Cheers!

