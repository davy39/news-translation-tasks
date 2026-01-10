---
title: How to handle navigation in your Flutter apps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-14T17:59:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-navigation-in-your-flutter-apps-ceaf2f411dcd
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca450740569d1a4ca61a9.jpg
tags:
- name: Dart
  slug: dart
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sameeha Rahman

  Flutter is a Google product used to build hybrid mobile apps with Dart as the coding
  language.

  An app page in Flutter is a Widget, a description of the UI portrayed. To make a
  legitimate app, you need many of these pages, displaying...'
---

By Sameeha Rahman

Flutter is a Google product used to build hybrid mobile apps with Dart as the coding language.

An app page in Flutter is a Widget, a description of the UI portrayed. To make a legitimate app, you need many of these pages, displaying a multitude of features. It’s all well and fine after you create a new page. But, how do you move between them?

Quite simple: you use the [Navigator](https://docs.flutter.io/flutter/widgets/Navigator-class.html) Class, inbuilt in the Flutter SDK.

### Navigator

Navigator is yet another Widget that manages the pages of an app in a stack-like format. The full-screen pages are called routes when used in the Navigator. The Navigator works like a normal stack implementation. It comes with two well-known methods, `push` and `pop`.

1. Push: The push method is used to add another route onto the top of the current stack. The new page is displayed over the previous one.
2. Pop: As the Navigator works like a stack, it uses the LIFO (Last-In, First-Out) principle. The pop method removes the topmost route from the stack. This displays the previous page to the user.

In this post, I will display:

1. Two ways of navigation and
2. Passing data to the next page.

### Normal Navigation.

There are two ways to do this:

#### Creating a new page within the `push` method

In this method, a new route is created using the `MaterialPageRoute` class. A new page (Widget) is created within it. These two creation statements come enclosed in the `push` method and add this page to the top of the stack.

To display a simple example, I’m using code from a previous repo and [blog post](https://medium.freecodecamp.org/https-medium-com-rahman-sameeha-whats-flutter-an-intro-to-dart-6fc42ba7c4a3). I edited it to include a button on the `CustomCard` component. This button uses the `push` method, while the new route and page are created within it.

```dart
Widget build(BuildContext context) {  
	return Card(    
    	child: Column(      
        	children: <Widget>[        
            	Text('Card $index'),        
                FlatButton(          
                	child: Text("Press Me"),          
                    onPressed: () {            
                    	Navigator.push(context, MaterialPageRoute<void>(
                        	builder: (BuildContext context) {                
                            	return Scaffold(                  
                                	appBar: AppBar(title: Text('My Page')),
                                    body: Center(                    
                                    	child: FlatButton(
                                        	child: Text('POP'),
                                           	onPressed: () {
                                            	Navigator.pop(context);
                                            },                    
                                        ),                  
                                    ),                
                                );              
                            },            
                        ));          
                    }),    
            ],  
        ));
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/ALt9-AfRlKL7NIYPAsCu1LJvMEuoaS4Xqy1H)

#### Add routes to the apps’ entry point

In retrospect, apps have many pages, and more often than not, with complex coding. It wouldn’t be easy to keep creating a new page to push into. This is especially true if the page is accessed from many different areas. You might lose track of the code for each of the same route.

So, in the second method, the page is created once but added as a route in the entry point of the app, `main.dart`. These routes are named like file paths since the root page of the app is the path `/`.

You first build a new app page, like so:

```dart
class SecondPage extends StatelessWidget {
	@override
	Widget build(BuildContext context) {
		return Scaffold(
			appBar: AppBar(
				title: Text('Second Page'),
			),
			body: Center(
				child: RaisedButton(
					child: Text('Back To HomeScreen'),
					color: Theme.of(context).primaryColor,
					textColor: Colors.white,
					onPressed: () => Navigator.pop(context)),
			),
		);
	}
}
```

Then, import the new page in the `main.dart` file and add it to the list of routes inside the MaterialApp constructor.

```dart
class MyApp extends StatelessWidget {
// This widget is the root of your application.
	@override
	Widget build(BuildContext context) {
		return MaterialApp(
			title: 'Flutter Demo',
			theme: ThemeData(
				primarySwatch: Colors.green,
			),
			home: MyHomePage(title: 'Flutter Demo Home Page'),
			routes: <String, WidgetBuilder>{
				'/a': (BuildContext context) => SecondPage(),
			});
	}
}
```

We then edit the onPressed method of the `FlatButton` in the `CustomCard` to this:

```
Navigator.pushNamed(context, '/a');
```

![Image](https://cdn-media-1.freecodecamp.org/images/VBQNP-t93AVi2wmCoiyYawJk326olmYxNByE)

In the above example, the user is redirected to the `SecondPage` class created as it is the corresponding page to the path `/a.`

### Passing Data between pages

Now for the last part of the demo, passing data to the next page. Doing so in an easy way requires a mix of both the above-mentioned navigation methods.

Both `pushNamed` and creating a new route inside the push method can be used to pass data to the new page. For the latter, a new page need not be made. The builder parameter of the `MaterialPageRoute` will now call the constructor of the `SecondPage` class.

Update the `SecondPage` class to accept the data being passed to it, like so:

```dart
class SecondPage extends StatelessWidget {
	SecondPage({@required this.title});
	final title;
    
	@override
	Widget build(BuildContext context) {
		return Scaffold(
			appBar: AppBar(
				title: Text('Card No. $title'),
			),
			body: Center(...),
		);
	}
}
```

The `FlatButtons`’ onPressed method is now edited to:

```dart
Navigator.push(context,
	MaterialPageRoute(
		builder: (context) => SecondPage(title: index)
	)
);
```

Or this:

```dart
Navigator.pushNamed( context, '/a',
	arguments: <String, String>{
		'title': index + "",
	},
);
```

The index of the card is now passed on to the `SecondPage` class, and is displayed in the `AppBar`.

![Image](https://cdn-media-1.freecodecamp.org/images/OuRrgD0YV1Ukxgjv7-MZL7pB2sFxfKHaKNxb)

Thanks for reading! You can find the repo, [here](https://github.com/samsam-026/flutter-example).

Find the commit for the following changes, [here](https://github.com/samsam-026/flutter-example/commit/166122bf68f3a17ed516f91cb9d9341571c3da50).

