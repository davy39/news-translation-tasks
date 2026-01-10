---
title: How to Add a Splash Screen to Your Flutter App
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-26T16:30:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-a-splash-screen-in-flutter-app
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/photo-1603539240352-8f2cce3257c4.jpeg
tags:
- name: Flutter
  slug: flutter
- name: user experience
  slug: user-experience
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By Krissanawat

  In this article, we''re going to learn how to integrate a splash screen in a Flutter
  app. But first, why is having a splash screen in your app essential?

  What is a Splash Screen?

  A splash screen is an initial screen that gets displayed ...'
---

By Krissanawat

In this article, we're going to learn how to integrate a splash screen in a Flutter app. But first, why is having a splash screen in your app essential?

## What is a Splash Screen?

A splash screen is an initial screen that gets displayed right when the user launches the app, before the main page loads. It may not look like much because it's only shown for a short time. But splash screens can really pack a punch as they're the first impression of the app. 

You may think that most users ignore them. But splash screens do have an impact, even subconsciously. They set the tone for the overall app theme and the user experience. 

Think of a splash screen as a welcome screen for your app. They also help let your users know when there's a loading delay due to a network issue or other error. Because of all this, we as developers should know how to add a proper splash screen to our mobile applications.

## Splash Screen Overview

Since splash screens are a valuable initial element in any app, you need to learn how to integrate them properly. So in this tutorial, we are going to learn how to do so in the Flutter ecosystem. 

The exact steps are pretty simple because we'll use a package to help us integrate the screen called [_splashscreen_](https://pub.dev/packages/splashscreen). This package allows us to set the splash screen as well as time the splash screen appears with just a few lines of code. And we don't have to touch any native codes. 

So let's get started and learn how to add a simple splash screen containing text, an image, and a loading indicator. 

## Create a New Flutter Project

First, we need to create a new Flutter project. For that, make sure that you have the Flutter SDK and other Flutter app development related components installed. 

If everything is properly set up, then to create a project you can simply run the following command in whatever local directory you want:

```
flutter create splashSceenExample
```

After the project has been set up, navigate inside the project directory and execute the following command in the terminal to run the project in either an available emulator or an actual device:

```flutter run```

After it's successfully built, you will get the following result on the emulator screen:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-74.png)

### How to Install the splashscreen Package

Now that we have our flutter project up and running, we can install the required dependencies. Now, you could add a splash screen by tampering with the native code in the Android and iOS folders – but if you're not a native Android or iOS developer, this isn't something you'll need to know how to do. 

Fortunately, we have the _[splashscreen](https://pub.dev/packages/splashscreen)_ package that makes it easy to add a splash screen in your Flutter app. The package offers widgets and various customization parameters to put up a simple introductory splash screen in your app. 

In order to use it, you need to add it to your dependencies first. To do that, just copy the piece of code in the code snippet below and paste it into your **pubspec.yaml** file:

```splashscreen: ^1.3.5```

The package provides a `SplashScreen` widget that lets you display a splash screen before navigating to your app’s primary screen.

## How to Add a Splash Screen to Your App

Now, we are going to use the `SplashScreen` widget provided by the _splashscreen_ package. The idea is to apply the `SplashScreen` widget to the `home` parameter of your `MaterialApp` widget. You can see the overall coding implementation in the code snippet below:

```
class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: SplashScreen(
        seconds: 8,
        navigateAfterSeconds:MyHomePage(title: 'Flutter Demo Home Page'),
        title: new Text(
          'SplashScreen Example',
          style: new TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 20.0,
              color: Colors.white),
        ),
        backgroundColor: Colors.lightBlue[200],
      )
    );
  }
}
```

In this code, we have introduced the SplashScreen widget in the home parameter of the MaterialApp. There are several parameters we have configured inside the `SplashScreen` widget. Let's look at each one more closely.

* `seconds`: The `seconds` option allows you to enter the time in seconds that you want the splash screen to be displayed. 
* `navigateAfterSeconds`: This option allows you to define the Widget or Screen (preferably the Home Screen of the app) which is shown after the splash screen ends. 
* `title` : This option let you add text to your splash screen. Here, we have used `Text` widget with some styles to do that. 
* `backgroundColor` : This allows you to specify the overall background color of the splash screen.

Alright, that was a simple configuration of a splash screen with text. This is what it'll look like:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/splashGIF1--1-.gif)

Here, you can see that the splash screen appears for few seconds before the default Home page loads. The loader is also shown by default. 

But, we can control the visibility of the loader by applying the `useLoader` parameter in the `SplashScreen` widget, which can be either true or false.

### How to Add a Custom Loader to Your Splash Screen

We already have the loader in place by default. But, we can control its color and styling by using the `loaderColor` options as shown in the code snippet below:

```
home: SplashScreen(
        seconds: 8,
        navigateAfterSeconds:MyHomePage(title: 'Flutter Demo Home Page'),
        title: new Text(
          'SplashScreen Example',
          style: new TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 20.0,
              color: Colors.white),
        ),
        backgroundColor: Colors.blue,
        styleTextUnderTheLoader: new TextStyle(),
        loaderColor: Colors.white
      )
```

Now you'll get the result as shown in the demo below:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/splashGIF2--1-.gif)

Here, you can see that we've changed the color of the loader to white.

### How to Add an Image or Logo to a Splash Screen

Now to make the splash screen look better, we can add an image or diagram – perhaps a logo or something similar. 

The `SplashScreen` widget gives you two additional parameters to set the logo correctly in the splash screen. The `image` option lets you add an image from your assets or network, and the `photoSize` option allows you to specify the dimensions of the image. 

It's better to add images from your assets because loading network images depends on connectivity and sometimes the image may not show up due to a slow internet connection. 

So we'll need to get the image to our **./assets** directory and then register the path to it in our **pubspec.yaml** file. Then, we can use the `image` and `photoSize` options as shown in the code snippet below:

```
home: SplashScreen(
        seconds: 5,
        navigateAfterSeconds:MyHomePage(title: 'Flutter Demo Home Page'),
        title: new Text(
          'SplashScreen Example',
          style: new TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 20.0,
              color: Colors.white),
        ),
        image: new Image.asset('assets/flut.png'),
        photoSize: 100.0,        
        backgroundColor: Colors.blue,
        styleTextUnderTheLoader: new TextStyle(),
        loaderColor: Colors.white
      )
 ```

This will be the result:

![Image](https://www.freecodecamp.org/news/content/images/2021/08/splashGIF3--1-.gif)

As you can see, we have the image placed at the top of our text. There are other options available as well which you can explore via the documentation of the splash screen package itself. 

And there you have it! Keep in mind that this works on both Android and iOS and does not need separate implementations.

## Conclusion

Adding a splash screen to your app doesn't have to be hard, thanks to the _splashscreen_ plugin. The main aim of this tutorial was to show you how to integrate a splash screen into your Flutter app without having to touch the native code. 

Here, you learned how to create a splash screen and include text, a loading indicator, and an image. Now, the challenge is to use the remaining parameters provided by the `SplashScreen` widget. 

Remember that a nice splash screen also helps alleviate any anxiety a user might have while launching your app. So, it does provide mental health benefits as well. 

Just keep in mind that the `splashcreen` plugin's functionality is a bit limited. If you want to create a custom splash screen with full control over what you can add to it, then you will have to go into the native code. Still, for simple splash screens, this plugin does the job. 

Lastly, you can get inspiration for your [Flutter App](http://instaflutter.com/) from others that are already out there.

