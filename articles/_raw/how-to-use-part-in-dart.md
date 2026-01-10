---
title: How to Use part in Dart – Splitting Files for Scoped Access
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-03T16:17:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-part-in-dart
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/parts-in-dart-1.png
tags:
- name: Dart
  slug: dart
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
seo_title: null
seo_desc: 'By Rutvik Tak

  When you''re coding in Dart, you may come across these  following situations:


  A class/method is associated with a particular file of your codebase and you want
  to keep it private only to that one file.

  You want to break your one big fil...'
---

By Rutvik Tak

When you're coding in Dart, you may come across these  following situations:

1. A class/method is associated with a particular file of your codebase and you want to keep it private only to that one file.
2. You want to break your one big file in different parts but avoid accidentally using any private members of that file in other sections of your codebase.

Now to solve the first problem, you might say that it’s quite simple, right? You just make the `class/method` private in that file, so it’s accessible only within it. Like this:

```dart
// Private class which is accessible only in the file it's declared.

class _MyPrivateClassOne {	

}
```

Yes, that’s one way of doing it. But, it may not be the most suitable way in some cases.

If you keep on doing this, you’ll end up with the second problem we mentioned. You’ll soon have one very large file with multiple members inside it. And it will very quickly become a pain to manage and navigate different parts of that file.

## **How to use `part` in Dart**

That’s where `part`  comes in. It is an interesting feature of the **Dart** language that makes it easy to split a file into different parts to better manage and navigate file as it gets big.

We'll take a look at the following example:

```
// main_file.dart

part "private_class2.dart" 

void main() { 

final privateClassOne = _PrivateClassOne();
final privateClassTwo = _PrivateClassTwo();

}

// private_class1.dart

part of "main_file.dart"

class _PrivateClassOne{

}

// private_class2.dart

part of "main_file.dart"

class _PrivateClassTwo{

}
```

Let's break down the above example and understand what we are doing here:

```dart
// #1 Declaring private parts

part "private_class1.dart"

part "private_class2.dart" 

void main() { 

final privateClassOne = _PrivateClassOne();
final privateClassTwo = _PrivateClassTwo();

}

```

In the first step, we declared the files into which we want to split our main file.

Secondly, in the respective files `private_class1.dart` and `private_class2.dart`, we need to add the following line at the top of those files to associate them with the main file:

```dart
// #2 Associating the file with the main file for access.

part of "main_file.dart"

class _PrivateClassOne{

}
```

This way, you’re able to split ur one big file into multiple parts for better management and readability.

## **Other examples of using `part`**

One popular package that makes use of `part` is **[Freezed](https://pub.dev/packages/freezed)**. It’s a package for code generation for `data-classes/unions/pattern-matching/cloning`. You can, for example, use it to create helper methods on your model like `fromJson/toJson` which allows you to take in some JSON data and convert it to your model or vice-versa.

To learn more about **Freezed**, you can check it out on [pub.dev](https://pub.dev/packages/freezed).

Whenever you generate a **Freezed** model – for example, `Screenshot` and is in a file `screenshot.dart` – you’ll notice that it generates two other files, `screenshot.freezed.dart` and `screenshot.g.dart`. This includes the helper methods like `fromJson/toJson/copyWith` in them.

You’ll notice that, at the start of your actual **Freezed** model file, you need to add these two lines:

```dart
// #1 Declaring separate private files

part 'screenshot.freezed.dart';

part 'screenshot.g.dart';
```

As we discussed in our above example, here you're mentioning the parts of your main file `screenshot.dart` model.

And these two generated files have the following line added to them at the start:

```dart
// #2 Associating the respected private files with the main file

part of 'screenshot.dart';
```

Here, **Freezed** is generating these other helper methods that your model utilizes. But it splits them in these different files to keep parts of the generated code away from you which you don’t need to worry about.

## **Use Cases for part**

Currently I’m working on my side project, [AppShots](https://appshots.co/) where I needed to use `part` to solve an actual problem.

I’ve two database layers, `PrimaryDatabaseLayer` and `_SecondaryDatabaseLayer` in my flutter app. The `_SecondaryDatabaseLayer`  would talk to the local database directly for adding/updating/deleting items.   
  
Lets see how the `PrimaryDatabaseLayer`  looks like,

```dart
// primary_database_layer.dart

part "secondary_database_layer.dart"

class PrimaryDatabaseLayer {

	Future<Screenshot1> addScreenshot(....){
	  // convert the model from Screenshot1 to Screenshot2 and call 	  // addScreenshot method from _SecondaryDatabase with Screenshot2
		....
        .......
	}

	Future<Screenshot1> updateScreenshot(....){
		// update screenshot to local db
		....
        .......
	}

	Future<Screenshot1> deleteScreenshot(....){
		// delete screenshot from local db
		....
        .......
	}

}
```

Then I had the second layer as follows:

```dart
// secondary_database_layer.dart

part of "primary_database_layer.dart"

class _SecondaryDatabaseLayer {

	Future<Screenshot2> addScreenshot(....){
		// add screenshot to local db
		....
        .......
	}

	Future<Screenshot2> updateScreenshot(....){
		// update screenshot to local db
		....
        .......
	}

	Future<Screenshot2> deleteScreenshot(....){
		// delete screenshot from local db
		....
        .......
	}

}
```

The main reason to have two db layers here was, I had two different models, `Screenshot1` and `Screenshot2`. The `Screenshot2` is the model that's suitable for interacting with the actual local db and `Screenshot1` is the model I used in the **apps business logic and the ui views**.

Now, as you can see the `PrimaryDatabaseLayer` is just a wrapper around the `_SecondaryDatabaseLayer` for convenient conversion of data models.

Adding the `_SecondaryDatabaseLayer` in the same file as `PrimaryDatabaseLayer` makes it difficult to mange and navigate as the layers grow in terms of their functionality. So, I used `part` here to make the `_SecondaryDatabaseLayer` a part of the `PrimaryDatabaseLayer` .

## **Conclusion**

In this tutorial, we discussed how to use `part` in **Dart** to improve your codebase. And you learned about a few examples where using `part` is beneficial and makes your life a little bit easier managing your code.

☺️ I hope you enjoyed this article. I'm planning to release more content where I'll be sharing my experiences/challenges building personal/work projects in Dart and Flutter to help you become a better developer.💪

If you liked this article and have any questions or would like to get in touch, you can connect with me on Twitter [**@TakRutvik**](https://twitter.com/TakRutvik) where I'm active and share all of my learnings and interesting projects I'm working on. ✨

Have a great day!☺️  
Keep Fluttering 💙

