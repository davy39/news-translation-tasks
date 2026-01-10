---
title: How to Build a Native Communication Bridge in Flutter with WebView and JavaScript
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2020-12-01T16:27:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-native-communication-bridge-in-flutter-with-webview-and-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/0_vBF65VQHbXyUUeHN.jpg
tags:
- name: Flutter
  slug: flutter
- name: mobile
  slug: mobile
- name: mobile app development
  slug: mobile-app-development
seo_title: null
seo_desc: 'As a follow up to my article explaining how to create communication bridges
  in Android and iOS, I thought it might be a good idea to do the same for Flutter.

  While it may seem like this is a straightforward affair, you’ll soon realize it
  takes a bit ...'
---

As a follow up to my [article](https://www.freecodecamp.org/news/how-to-build-cross-origin-communication-bridges-in-ios-and-andriod-7baef82b3f02/) explaining how to create communication bridges in Android and iOS, I thought it might be a good idea to do the same for Flutter.

While it may seem like this is a straightforward affair, you’ll soon realize it takes a bit of work to get this functionality working.

First and foremost, it is important to realize that (at the time of writing this article) Flutter does **not** have built in support for embedded WebViews.

Unlike a native application in either Kotlin or Swift where you can just instantiate a WebView component, you cannot add a WebView component to your Flutter application out of the box.

In this article, we'll go over how to configure WebView in Flutter applications, and how to communicate between Flutter and Webview.

## How to configure WebView in a Flutter application

After creating a new Flutter project, we need to use the [webview_flutter package](https://pub.dev/packages/webview_flutter) to be able to use a WebView. We will add the dependency to our `pubspec.yaml` file:

```yaml
dependencies:  
       flutter:    
           sdk: flutter
       webview_flutter: ^1.0.7
```

Then, we need to run `pub get` in the terminal:

```bash
flutter pub get
```

Next, we import the package in our `main.dart` file:

```dart
import 'package:webview_flutter/webview_flutter.dart';
```

If you haven’t cleaned up the code from the starter project yet, now is a good time to do so. 

After you remove all the comments, the floating action button and everything related to it, you will be left with this (I added a text widget just for show):

```dart
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Communication Bridge',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: MyHomePage(title: 'Native - JS Communication Bridge'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  WebViewController _controller;

  @override
  Widget build(BuildContext context) {
    return Text(
      "Flutter JS-Native Communication Bridge"
    );
  }
}
```

Which will give you this result:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/1_txc-SxRUBZFMR4mdJq-tCA.png)

### Creating a local HTML asset

Since we will be using a local HTML file with embedded JavaScript code inside of it, we need to create it in our project. 

All local assets in a Flutter application need to be in an `assets` directory. 

Create an `assets` directory in your main project hierarchy by right clicking in the left side panel and choosing New → Directory:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/1_xlBwiAWJUdKiZWDsAdx7SQ.png)
_The file hierarchy after creating the asses directory_

Then, go on ahead and create `index.html` inside the assets directory and add the following code:

```html
<html>

    <head>
        <title>My Local HTML File</title>
    </head>

    <body>
        <h1 id="title">Hello World!</h1>
        <script type="text/javascript">
            function fromFlutter(newTitle) {
                document.getElementById("title").innerHTML = newTitle;
                sendBack();
             }

             function sendBack() {
                messageHandler.postMessage("Hello from JS");
             }
        </script>
    </body>
</html>
```

You will notice that we have written two methods in the JavaScript section of our html:

1. `fromFlutter` is the method we will call from Flutter with a string representing the new title for the page
2. `sendBack` is the method we will call to communicate back to Flutter. In it we are sending a string message.

We will get into the contents of sendBack in a minute, but before that, we have to set up our WebView in our application.

✋ Don’t forget to add `index.html` to your `pubspec.yaml` under an `assets` section (use the correct indentation):

```yaml
dependencies:
  flutter:
    sdk: flutter
  webview_flutter: ^1.0.7
  cupertino_icons: ^1.0.0

dev_dependencies:
  flutter_test:
    sdk: flutter
    
flutter:
  uses-material-design: true
  
  assets:
    - assets/index.html
```

### Set up the WebView

Since we already imported the package into our `main.dart` file, we need to replace the Text widget with a WebView widget:

```dart
class _MyHomePageState extends State<MyHomePage> {

  WebViewController _controller;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Webview')),
      body: WebView(
        initialUrl: 'about:blank',
        onWebViewCreated: (WebViewController webviewController) {
          _controller = webviewController;
          _loadHtmlFromAssets();
        },
      ),
    );
  }

  _loadHtmlFromAssets() async {
    String file = await rootBundle.loadString('assets/index.html');
    _controller.loadUrl(Uri.dataFromString(
        file,
        mimeType: 'text/html',
        encoding: Encoding.getByName('utf-8')).toString());
  }

}
```

We wrapped our WebView with a Scaffold widget (we'll go over this more later in the article), but let’s focus on the different fields of the WebView widget seen above:

* `initialUrl` is where we can define which URL the WebView points to. Here we decided to point it to nothing since we are going to load our local HTML file
* `onWebViewCreated` is a callback we get from the package once the WebView is created. Since we want to save the controller instance that we get from this callback, we have created a private member to store it to, `_controller`

You will also notice that we created a method called `_loadHtmlFromAssets`, which as is implied by its name, will load our local HTML file into the WebView.

Inside this method, we use our private WebViewController instance, `_controller`, and it’s exposed method `loadUrl` to load our local HTML file. Due to the logic in this method, its execution is asynchronous.

If we run our application, we will get the following:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/1_hE6jeEprGAW3YkVt0AiYrA.png)

## How to communicate from Flutter to WebView

Now let’s add some functionality to call the `fromFlutter` method we defined in our local HTML file. 

To do that, we will be adding a Floating Action Button (or FAB) to our layout and connecting its `onPressed` method to call the `fromFlutter` method.

This is also the reason behind the usage of the Scaffold widget – so we can easily add a FAB:

```dart
@override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Webview')),
      body: WebView(
        initialUrl: 'about:blank',
        javascriptMode: JavascriptMode.unrestricted,
        onWebViewCreated: (WebViewController webviewController) {
          _controller = webviewController;
          _loadHtmlFromAssets();
        },
      ),
      floatingActionButton: FloatingActionButton(
        child: const Icon(Icons.arrow_upward),
        onPressed: () {
          _controller.evaluateJavascript('fromFlutter("From Flutter")');
        },
      ),
    );
  }
```

In order to make calls from Flutter to our loaded HTML we are using the `evaluateJavascript` method. To be able to use it, we must add another property to our WebView called `javascriptMode`. 

In the code above, we are setting it to unrestricted. If we don’t set it, we will not be able to communicate between Flutter and the WebView:

![Image](https://www.freecodecamp.org/news/content/images/2020/11/1_odgcLrPQUlhGHdbaF4rO4A.gif)

## How to communicate back from WebView to Flutter

Remember how I said we will talk about the contents of our `sendBack` method? Let's do that now:

```javascript
function sendBack() {
  messageHandler.postMessage("Hello from JS");
}
```

In the `sendBack` method, we are using an object called `messageHandler`, and it’s attached method called `postMessage`. 

Just like creating a communication bridge in a native application, once you set one up, you are adding an object to the global `Window` object in the JavaScript layer to be used for communication.

You can name this object to whatever you like as long as you reference it when you make calls from JavaScript to your native application.

How is this object added to the JavaScript layer in our application, you might ask? By adding the `JavascriptChannels` attribute to our WebView widget:

```dart
class _MyHomePageState extends State<MyHomePage> {

  WebViewController _controller;
  final GlobalKey<ScaffoldState> _scaffoldKey = new GlobalKey<ScaffoldState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: _scaffoldKey,
      appBar: AppBar(title: Text('Webview')),
      body: WebView(
        initialUrl: 'about:blank',
        javascriptMode: JavascriptMode.unrestricted,
        javascriptChannels: Set.from([
          JavascriptChannel(
              name: 'messageHandler',
              onMessageReceived: (JavascriptMessage message) {
               _scaffoldKey.currentState.showSnackBar(
                  SnackBar(
                      content: Text(message)
                  )
                 );
              })
        ]),
        onWebViewCreated: (WebViewController webviewController) {
          _controller = webviewController;
          _loadHtmlFromAssets();
        },
      ),
      floatingActionButton: FloatingActionButton(
        child: const Icon(Icons.arrow_upward),
        onPressed: () {
          _controller.evaluateJavascript('fromFlutter("From Flutter")');
        },
      ),
    );

  }
```

We have defined a `JavascriptChannel` with a name and an `onMessageReceived` handler. The name we have given this channel, `messageHandler`, is the name we are using to communicate from the local HTML file we loaded to our native layer.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/1_AGpwDR2o8Fh7Re_Cwtg7fA.gif)
_Great success_

For the keen eyed, you probably noticed that a new private variable has been added, `_scaffoldKey`. This is because we needed to add a key to our Scaffold widget so we can display the snackbar.

You can get the source code for the application described in this article below:

%[https://github.com/TomerPacific/MediumArticles/tree/master/flutter_communication_bridge]

Two final points to be aware of:

1. [The alert method is broken in the webview_flutter package](https://github.com/flutter/flutter/issues/30358)
2. To use the package in iOS, you must add the following key to your `info.plist` file: `<key>io.flutter.embedded_views_preview</key><string>yes</string>`

Here are some other sources you may find helpful if you want to learn more about Flutter and WebViews:

* [The Power of WebViews In Flutter](https://medium.com/flutter/the-power-of-webviews-in-flutter-a56234b57df2)
* [WebView_Flutter Package](https://pub.dev/packages/webview_flutter)

