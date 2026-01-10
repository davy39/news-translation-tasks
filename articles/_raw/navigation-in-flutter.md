---
title: Navigation in Flutter – How to Add Stack, Tab, and Drawer Navigators to Your
  Apps
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-04-21T18:10:23.000Z'
originalURL: https://freecodecamp.org/news/navigation-in-flutter
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Types-of-Navigations-in-Flutter---Banner.png
tags:
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
seo_title: null
seo_desc: "Almost any app that you design or develop will use some type of navigation.\
  \ \nThere are three types of navigation that are common to all apps – stack, tab,\
  \ and drawer navigation.\nFlutter supports all three types, and implementing them\
  \ is similar to ho..."
---

Almost any app that you design or develop will use some type of navigation. 

There are three types of navigation that are common to all apps – stack, tab, and drawer navigation.

Flutter supports all three types, and implementing them is similar to how you do it in other apps. But I found it super smooth to build navigation into my Flutter app.

In this article, we'll build a Flutter app that uses all three types of navigation in a single app so you can learn how they work.

## Types of Navigation

As I mentioned above, there are three main types of navigation that you might use in your apps. Again, they are:

1. Stack Navigation
2. Tab Navigation
3. Drawer Navigation

Let's understand how each one works.

### Stack Navigation

Picture a deck of cards, where you can add or remove cards from the top of the stack. Stack Navigation in Flutter works in a similar fashion. It helps you navigate between pages or screens by stacking new pages on top of existing ones. 

When you move to a new screen, the current screen is pushed onto the navigation stack, and when you return, the top screen is popped off the stack. 

This navigation type is commonly used for hierarchical and linear flows within an app. 

### Tab Navigation

Tabs are a staple of mobile app navigation, allowing users to quickly switch between different sections or views without losing their current context. 

Flutter makes it easy to implement tabbed navigation with its built-in widgets, such as TabBar and TabBarView. By using these widgets, you can create a beautiful and functional tab navigation experience, perfect for organizing content into logical sections. 

You also have the freedom to customize the appearance of your tabs, making it simple to create a unique look and feel for your app. 

### Drawer Navigation

The Drawer Navigation pattern, also known as the "hamburger menu" or "side menu," is a popular navigation style in mobile apps. It consists of a hidden panel that slides out from the side of the screen, revealing a menu with various navigation options. 

This space-saving technique keeps your app's main content visible while providing easy access to additional features or sections. 

Let's start building the app and see how to implement each of these navigation features.

## How to Create the Project

Instead of creating a new project every time from scratch, I've created a boilerplate app and uploaded in [GitHub](https://github.com/5minslearn/Flutter-Boilerplate). You can pull the code and run. I hope that makes creating this project a bit simpler. 

Navigate to the folder where you want to create your project in the terminal and run the following command. 

```bash
git clone https://github.com/5minslearn/Flutter-Boilerplate.git
```

Navigate to the `Flutter-Boilerplate` folder and run the `flutter pub get` command to install the dependencies. 

```bash
cd Flutter-Boilerplate/
flutter pub get
```

That's it. We've got our dependencies installed. 

Open the project in Visual Studio Code by running the `code ./` command in the terminal. 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-147.png)
_Clone repo and install dependencies_

Start your emulator/connect your device and press `F5` in VS Code to run your app. 

At the moment, the app will just contain an empty screen as shown in the below screenshot. 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-148.png)
_Flutter app with empty screen_

Let's build all 3 types of navigation into our app. 

But before that, let's see what our final app will look like:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-155.png)
_Look of our final app_

We'll have both drawer and tab navigators at the top. Pressing on the button in the first tab will take us to the next page via the stack navigator. 

## How to Build the Tab Navigation

Let's begin with building the tab navigator. Let's assume the tab will be on the home page (ideally that's where it would be). 

Create a new file named `tab.dart` in the `lib/` directory. Add the following code:

```dart
import 'package:flutter/material.dart';
import './tabs/tab1.dart';
import './tabs/tab2.dart';
import './tabs/tab3.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Scaffold(
          appBar: AppBar(
            title: const Text("Home"),
            bottom: const TabBar(
              tabs: [
                Tab(icon: Icon(Icons.phone_android)),
                Tab(icon: Icon(Icons.tablet_android)),
                Tab(icon: Icon(Icons.laptop_windows)),
              ],
            ),
          ),
          body: const TabBarView(
            children: <Widget>[
              Tab1(),
              Tab2(),
              Tab3(),
            ],
          )),
    );
  }
}
```

In the above code, we're creating a class named `HomePage`. In the build method, we return the `DefaultTabController` widget, which is basically a tab view. We define that we need 3 tabs in the `length` property. 

At the bottom of the `appBar` property we have defined icons for each tab (Phone, Tablet, and Computer icons). Below that we define the `body` property with a `TabBarView` rendering all the tabs inside it. 

Immediately when you paste in the above code, you'll notice lot of errors being highlighted in your VS Code editor.

 This is because, if you look at the top four lines, the first line is the import of Flutter's Material UI package and the other three are imports from the user defined files. But we haven't created them yet. So, your code editor will throw an error in those lines and at the last three lines where we call `Tab1()`, `Tab2()`, and `Tab3()` (because, these classes are imported from those files). Let's resolve this issue now. 

Create a new folder named `tabs` inside the `lib/` directory and create three files named `tab1.dart`, `tab2.dart`, and `tab3.dart`. 

Copy the below content into the `tab1.dart` file:

```dart
import 'package:flutter/material.dart';

class Tab1 extends StatelessWidget {
  const Tab1({super.key});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: double.infinity,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          const Text("Mobiles"),
          Padding(
            padding: const EdgeInsets.only(top: 16.0),
            child: ElevatedButton(
              onPressed: () {
                Navigator.of(context).pushNamed("/secret");
              },
              child: const Text('Disclose Secret'),
            ),
          ),
        ],
      ),
    );
  }
}
```

Copy the below content into the `tab2.dart` file:

```dart
import 'package:flutter/material.dart';

class Tab2 extends StatelessWidget {
  const Tab2({super.key});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: double.infinity,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: const <Widget>[
          Text("Tablets"),
        ],
      ),
    );
  }
}
```

Copy the below code into the `tab3.dart` file:

```
import 'package:flutter/material.dart';

class Tab3 extends StatelessWidget {
  const Tab3({super.key});

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: double.infinity,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: const <Widget>[
          Text("Laptops"),
        ],
      ),
    );
  }
}
```

If you look at the code for all three files, you'll notice everything is the same except that the first tab file (`tab1.dart`) has an additional button called "Disclose Secret". Pressing that will navigate the user to the `/secret` route. It won't throw any error as this route has not been defined yet. The other two files (`tab2.dart` and `tab3.dart`) will show only the text. 

All the errors you saw in the `tab.dart` file will be resolved now. But if you run your app, you will not notice any changes in the output. This is because we have just created the tab layout and we haven't mapped it to our `main.dart` file. 

Add the following line at the top of the `main.dart` file:

```dart
import './tab.dart';
```

Replace `home: const MyHomePage(title: 'Home')` with `home: const HomePage()`, in the `build` method of the `MyApp` class. 

Save the file and run your app. You should be able to see the tab layout on your screen now. 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-157.png)
_Tab Layout in Flutter App_

Don't press the "Disclose Secret" button. If you press it, it will throw an error. Because, as I mentioned earlier, we set up a route navigation in the `onPress` property of this button, but the route is not yet defined. 

"Let's click that and see what happens"...

Hopefully, this thought will have entered your mind by now. It's not a mistake, it's human nature. We're curious to explore the things even if they're not recommended to do. 

By the way, if you do that you'll see the following error (Exception in programming terminology):

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-156.png)
_Flutter Router Exception_

In a nutshell, this error screenshot describes that the provided route does not exist. 

## How to Build the Drawer Navigation

Our next target is to add the drawer navigation. But before that, we have to create two files:

1. `drawer.dart`: to show the Navigation Drawer
2. `about.dart`: an option will be provided on the Drawer Navigator to navigate here

Create the `drawer.dart` file inside the `lib/` directory and not inside the `tab/` directory. The `tab/` directory is only for tabs and we don't need to touch that further as we're done with the tabs. Copy the below code into the `drawer.dart` file:

```dart
import 'package:flutter/material.dart';

class MyDrawer extends StatelessWidget {
  const MyDrawer({super.key});

  navigateTo(String route, BuildContext context) {
    Navigator.of(context).pushReplacementNamed(route);
  }

  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: ListView(
        padding: const EdgeInsets.all(16.0),
        children: <Widget>[
          ListTile(
            leading: const Icon(Icons.home),
            title: const Text('Home'),
            onTap: () {
              navigateTo("/home", context);
            },
          ),
          ListTile(
            leading: const Icon(Icons.info),
            title: const Text('About'),
            onTap: () {
              navigateTo("/about", context);
            },
          ),
        ],
      ),
    );
  }
}
```

In this file, we define the class named `MyDrawer`. In the `build` method we render the `Drawer` widget with `Home` and `About` options in the list. Clicking on those options will navigate us to the appropriate routes. 

Create an `about.dart` file in the same directory and copy the below code: 

```dart
import './drawer.dart';
import 'package:flutter/material.dart';

class About extends StatelessWidget {
  const About({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      drawer: const MyDrawer(),
      appBar: AppBar(title: const Text("About")),
      body: const Center(child: Text("About")),
    );
  }
}
```

In this file, we create a class named `About` which returns a `Scaffold` widget containing the drawer which we defined right before this file. The `appBar` and the `body` will show the text "About". 

Again, you'll not be able to see these changes immediately in the app. This is because we haven't linked it into the `main.dart` file. 

Before we link them, we have one item in our backlog. Let's finish it and come back to linking them all together. 

Create a file named `secret.dart` in the `lib/` directory and copy the below code:

```dart
import 'package:flutter/material.dart';

class SecretPage extends StatelessWidget {
  const SecretPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          // backgroundColor: Colors.red,
          title: const Text("Secret"),
        ),
        body: SizedBox(
          width: double.infinity,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: const <Widget>[
              Text("Nothing to show"),
            ],
          ),
        ));
  }
}
```

In this file, we have created a class named `SecretPage` and returned just a `Text` in the `body`. Nothing fancy here. It's a super simple Flutter widget. 

Our backlog item is also done. This is what you've been waiting for: we're going to define our routes now. 

Open the `main.dart` file and add the following imports at the top of the file: 

```dart
import './about.dart';
import './secret.dart';
```

Replace the `build` method of the `MyApp` class with the below code:

```dart
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      routes: <String, WidgetBuilder>{
        "/about": (BuildContext context) => const About(),
        "/home": (BuildContext context) => const HomePage(),
        "/secret": (BuildContext context) => const SecretPage(),
      },
      initialRoute: "/home",
      title: 'Flutter Navigation',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const HomePage(),
    );
  }
```

In the above code, you can see we're defining the MaterialApp to contain routes. They're defined as key-value pairs, mapping a route with a Widget. We have defined three routes:

* `/about` – the route for the drawer navigator
* `/home` – the route for the tab navigator
* `/secret` – the route for the stack navigator

We have set the initial route to be `/home`, which has the tab navigator. 

Run the app and you should be able to see the following output on your device:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-158.png)
_Merged Tab and Drawer View_

On pressing the "Disclose Secret" button you'll be taken to the Secret page which we created (ideally it does not have a secret). You should also be able to scroll through the tabs smoothly. 

By now, I hope you will have noticed an error here. If not, here's what it is: the back button is shown on the first screen of our app. 

"Why would we need to show the back button on the first screen?"

That's an error and we have to resolve it. Press the back button and let's see what happens. Hopefully, you see what I saw. The back button was hidden and we see just the "Home" title in the `appBar` (similar to the below screenshot):

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-160.png)
_Back button issue_

But there's an another issue on the same screen. Hopefully you saw that too. If not, don't worry, I'll reveal it right here. 

"Can you access the drawer navigator by any means?"

No. Right? 

But fortunately, the fix for the above two issues is the same. If we fix the second issue, the first issue will automatically be fixed. 

That's great. But how do we fix the second issue? 

You have to show the drawer navigator button (Hamburger icon) on the top left. This will eventually hide the back button. 

Open the `tab.dart` file and import the drawer file at the top of this file. 

```dart
import './drawer.dart';
```

Add the following line inside the `Scaffold` widget of the `build` method:

```dart
drawer: const MyDrawer(),
```

And that's it!

Here's the output you can see when you run your app:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-163.png)
_App look after the issues are fixed_

## Conclusion

In this article, you've learned how to implement navigation in a Flutter app. We've included all three types of navigation in a single app in this tutorial for educational purposes. Ideally, you wouldn't do this with any real app you're building. Most apps will be built on either one or two types of navigation. 

This [repo](https://github.com/5minslearn/Flutter-Navigation-Types) has my code. You can use it for your reference. 

To learn more about Flutter, subscribe to my email newsletter on my [site](https://5minslearn.gogosoon.com/?ref=fcc_flutter_navigation) ([https://5minslearn.gogosoon.com](https://5minslearn.gogosoon.com/?ref=fcc_flutter_navigation)) and follow me on social media. 


