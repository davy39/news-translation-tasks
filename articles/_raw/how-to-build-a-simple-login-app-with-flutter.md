---
title: How to Build a Simple Login App with Flutter
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-03-14T16:39:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-simple-login-app-with-flutter
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Flutter-Login-App---Banner.png
tags:
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
seo_title: null
seo_desc: 'Flutter is one of the most popular frameworks for building mobile and desktop
  applications. And many companies are using it today.

  This is in part because of its outstanding performance, having a benchmark of 60
  Frames Per Second (FPS). This helps it...'
---

Flutter is one of the most popular frameworks for building mobile and desktop applications. And many companies are using it today.

This is in part because of its outstanding performance, having a benchmark of 60 Frames Per Second (FPS). This helps it outperform other cross-platform technologies, and it performs better even when compared with native languages. 

I'm a React Native enthusiast. But after hearing all the advantages of Flutter, I decided to try it out. I would like to share my learning experience with you through this tutorial.

In this article, we'll learn how to create a Flutter app with a login layout and a few functionalities. 

## Prerequisites

In this article, I'll not cover the steps to install Flutter on your machine. I feel it's better explained on their [official documentation site](https://docs.flutter.dev/get-started/install). 

I would highly recommend that you try this [exercise](https://docs.flutter.dev/get-started/codelab) offered by the official Flutter community. It will give you a quick understanding of Flutter so you can get started. 

Don't worry if you don't understand a few concepts mentioned there. I'll be writing about them in my upcoming tutorials. I used that exercise to start my own Flutter journey, and I felt more confident after completing it on my own. 

Let's get started building our app!

I believe in the saying, "Setting a goal is half the work done". So, whenever I try to do something, I will set a goal to see where I want to be when I finish. So what's the goal for you reading this tutorial? 

## Required Tools

To build this app, you need the following items installed on your machine:

1. Visual Studio Code (One of Flutter's recommended IDEs)
2. Android Emulator / iOS Simulator / Original device
3. Flutter Installed (I would recommend following [this guide](http://docs.flutter.dev/get-started/install) to install it if you don't have it already)
4. Flutter plugin for VS Code ([Recommended Guide](https://docs.flutter.dev/get-started/editor?tab=vscode))

## How to Create the Project

Navigate to the folder where you want to create your app. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-61.png)
_Navigate to the project directory_

Open Visual Studio Code from that directory. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-62.png)
_Open Visual Studio Code_

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-63.png)
_Visual Studio Code IDE_

Open the command palette by pressing `CTRL + SHIFT + P` and type `Flutter`. Choose `Flutter: New Project` from the listed options. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-64.png)
_Use the command palette to create a Flutter project_

Select `Application` from the next list. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-65.png)
_Choose to build Flutter `Application`_

It'll ask you to Select the target folder to create the project. By default, it'll be in the same folder where you opened VS Code. Type your app name in the text input and hit `Enter`. I'm naming mine `loginapp`, but you can type any name you wish. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-66.png)
_Enter your project name_

In the next few seconds, VS Code will create a new Flutter project and you'll see a screen like the one below:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-67.png)
_Flutter project created_

By default, `main.dart` file will be opened. This is where Flutter begins to run the app. At the bottom, you will see a notification saying "Your Flutter project is ready! Press F5 to start running ...". 

## How to Spin Up the Device

To run your app, you need to have either a virtual device or an actual device running and connected to your machine. 

I'll be using an Android Emulator to run our app. You may either run a virtual device or connect your mobile phone to your machine. But remember to turn on "USB Debugging" if you're debugging via an Android phone. 

Once you're connected or spin up a virtual device, look at the bottom right of VS Code and press the device option. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-68.png)
_Devices option_

Sometimes, VS Code will select the device by default, but for the first time, you have to select it on your own. Press the "No Device" text in the above screenshot or whatever the device name is shown to you there. 

You'll be shown the list of virtual devices that are available and connected. Click on the device where you want to run your app. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-69.png)
_List of available devices to run the app_

Once you've selected your device, the bottom panel will show your selected device name similar to the below screenshot. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-70.png)
_Selected my Android emulator_

## How to Run the App

Are you ready for the Rocket Launch? 

Press `F5` to run your app. This will take some time. It'll be compiling and building your project. Once it's ready, the app will be running on your device. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-71.png)
_Running your app_

You'll see a similar kind of interface. At the bottom, you can see the notification saying "Running Gradle task 'assembleDebug...'". 

Excited for the output? Here you go:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-72.png)
_Output of the default app_

Don't make any changes to the code now. Your changes will not be tracked as Git is not initialized for this repo. 

This is one part that I like about React Native. Whenever you create a React Native app, it'll make an initial commit. You can just go forward and make your changes and you'll be able to see all your changes being tracked. 

This is not available in Flutter as of now (Mar 2023), but I hope the Flutter team may add this in the future. 

Let's make the commit on our own. 

Navigate to the project location in the Terminal:

```bash
cd <project_location>
```

Initialize Git by running `git init` command. 

As it's our first commit, we'll do `git add .` to add all the changes to our commit. 

Let's make the initial commit:

```
git commit -m "Initial commit"
```

Here's the screenshot of the above process:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-73.png)
_Commit the changes to git_

Let's verify if our changes are committed by running the `git status` command:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-74.png)
_Verifying after commit_

Looks Good. Our changes are committed. Let's proceed. 

## How to Remove Comments

I don't like comments in my code. I love writing readable code. Let's remove all the comments in the `main.dart` file. Don't touch the other files. 

All the Flutter files will reside under the `lib/` directory and they'll have the `.dart` file extension. For this entire tutorial, we'll be working only on the `main.dart` file. 

You can read the comments and get some insights from them. They'll give you a clear understanding about how the default app works which can be really helpful for beginners. 

But, it does not make any sense if you're building the app for 2nd or 3rd time. There is no point in reading the same comments again and again as you will have gained context on your 1st read. 

You can ignore this step if you want to keep the comments as they are. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Full-code.png)
_App Code_

My code has become super simple now. I've made a commit here (after removing the comments). If you have come this far, after committing just ensure your app is running fine and there have been no changes on the UI. 

## How to Change the Name

Let's change the name of the title bar and the internal class names. On the `MyApp` class, inside the `build` method, change the title in the home field from "Flutter Demo Home Page" to "Login App".  

```dart
class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Login App'),
    );
  }
}
```

Let's change our class name from "MyHomePage" to "Login". Place the cursor on the "MyHomePage" text and press `F2`. `F2` is the shortcut key to rename and refactor in VS Code. This means, it renames at the current place and replaces all its usages. Here's the screenshot of how it looks when you press `F2` (on refactoring). 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-76.png)
_Rename class name from `MyHomePage` to `Login`_

Let's commit our changes. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-77.png)
_Commit the changes to the names_

You should be able to see the title "Login App" in your app. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-78.png)
_The title bar of the app changed to "Login App"_

## How to Build the App

Now let's build our app. Copy the below code and replace it with the `_LoginState` class in the `main.dart` file. 

<script src="https://gist.github.com/arungogosoon/48c951d288dde4ac6b472c501655b9ad.js"></script>

Immediately after you paste and save the file, your UI will change like magic. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-79.png)
_UI Changed to ask for Login credentials_

Let's dismantle the code you copied into parts and try to understand each block. 

```dart
  final _formKey = GlobalKey<FormState>();
  TextEditingController emailController = TextEditingController();
  TextEditingController passwordController = TextEditingController();
```

The first line indicates that you're creating a key for a form. In our context, it is the login form. You're creating it to identify the form uniquely. It is set to final, so that it won't change. 

The next 2 lines are definitions of controllers. A controller in our context is used to read the values from the input. Using a controller, you'll be able to control its associated component. 

Let's dismantle the `build` method. You use the `build` method in Flutter to build the UI. It contains the design code. The content returned from this method will be rendered on the UI. 

```dart
@override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Form(
        key: _formKey,
```

The Scaffold is a widget in Flutter used to implement the basic material design visual layout structure. Assume the widget is a simple UI component. 

We're setting the title passed as a parameter to this class. We can access the parameters using the widget object. So, it goes like `widget.{key_name}`. 

If you want to access the title property, then it'll be `widget.title`. This is similar to passing `props` in React. 

```
body: Form(
  key: _formKey,
  child: Padding(
    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 16),
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
```

The next section is `body`. As we're building a simple login app, we need a form to be filled out by the user to authenticate. We're setting the unique key which we created above to this form. The `Form` accepts a child. It can accept only one component. 

We are creating a layout with horizontal padding of 8px and vertical padding of 16px. This `Padding` widget also accepts only one child. 

`Column` is a widget in Flutter that is used to display its children in a vertical array. We set `crossAxisAlignment` to horizontally center the contents of the `Column` widget. 

As we saw, the `Column` widget displays its children in a vertical array. We can pass multiple widgets in its `children` property. 

```dart
Padding(
  padding:
      const EdgeInsets.symmetric(horizontal: 8, vertical: 16),
      child: TextFormField(
        controller: emailController,
        decoration: const InputDecoration(
          border: OutlineInputBorder(), labelText: "Email"),
        validator: (value) {
          if (value == null || value.isEmpty) {
            return 'Please enter your email';
          }
          return null;
        },
     ),
  ),
```

The first item we want to display in the UI is an input box to get the email address of a user. So, we used the `TextFormField` widget and set the controller to `emailController`. 

In order to get the floating text, we need to use the decoration option which asks for the type of `border` and the `labelText` of the input. 

We can add any default validation to be applied when this form is submitted in the `validator` field. We're validating if it's either a `null` or empty value and we return an error if any of them match. If it has some value, then we're not throwing any errors and returning `null`. 

```
Padding(
  padding:
  const EdgeInsets.symmetric(horizontal: 8, vertical: 16),
    child: TextFormField(
      controller: passwordController,
      obscureText: true,
      decoration: const InputDecoration(
        border: OutlineInputBorder(), labelText: "Password"),
      validator: (value) {
        if (value == null || value.isEmpty) {
          return 'Please enter your password';
        }
        return null;
      },
   ),
),
```

The second item is the input box to get the `Password` from the user. This is similar to the `email` field except for one thing: we should hide the password in the input field and display a dot for each typed character. 

To do that, we have to pass an `obscureText` property to the `TextFormField` widget and set it to `true`. The decoration, validation, and other items remain the same as that of `Email`. 

```dart
Padding(
  padding:
    const EdgeInsets.symmetric(horizontal: 8, vertical: 16.0),
      child: Center(
        child: ElevatedButton(
          onPressed: () {
            if (_formKey.currentState!.validate()) {
              // Navigate the user to the Home page
            } else {
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(content: Text('Please fill input')),
              );
            }
          },
        child: const Text('Submit'),
      ),
    ),
),
```

This is the final piece of our form, which is a submit button. We're using a `ElevatedButton` widget and passing the button text in the `child` property of the button. We define the action that should be followed when pressing this button in the `onPressed` property. 

In our case, we're validating the input fields (remember the `validator` property we defined for the `email` and the `password` input box). If the validation passes, we should navigate the user to the next screen (which we'll be adding later). If not, we show a message asking the user to fill in the inputs ("Please fill input"). 

It's time to verify if our code is working properly. Check your app. Try to submit without entering any input and you should notice the Snackbar at the bottom with the text "Please fill input". Fill in the input boxes with some random values and try to submit and you should not be seeing the error now. 

If you're facing any errors in viewing the UI, most of the time (almost 90%) it'll be with brackets. We'll be using a lot of brackets in Flutter which is often confusing for beginners. Make sure you have the proper opening and closing brackets. The Flutter app may terminate in the middle in case of any errors. In these cases, after applying the fix, press `F5` to restart the app. 

## Navigate on Login

Let's navigate the user to the Home page on successful login and show the email address they entered on the Login page. Something similar to the below screenshot:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-87.png)
_Home page_

Go to the last line of the `main.dart` file and copy and paste the below content:

<script src="https://gist.github.com/arungogosoon/4677275a5265981967362825da714f32.js"></script>

In this code, we are creating a new class called "HomePage" and extending it from "StatelessWidget". We receive an email from the previous page. 

```dart
@override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text('Home Page'),
        ),
        body: Column(
          children: [
            Text(email),
            Center(
              child: ElevatedButton(
                onPressed: () {
                  Navigator.pop(context);
                },
                child: const Text("Go back!"),
              ),
            ),
          ],
        ));
```

On the `build` method, we define the title of the page to be "Home Page" and its body contains a `Text` and `ElevatedButton` widget. The `Text` widget will display the email address passed from the previous screen. The `ElevatedButton` widget will navigate the user to the previous screen whenever it's pressed. We use `Navigator.pop(context);` to navigate to the previous screen. 

Let's understand how to navigate from the `Login` page to the `Home` page. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-89.png)
_Code to navigate to the next page_

Remove the comment we made on `validation` condition ("Navigate the user to the Home page") as shown in above screenshot and replace it with the below content. 

```dart
if (emailController.text == "arun@gogosoon.com" && passwordController.text == "qazxswedcvfr") {
  Navigator.push(
    context,
    MaterialPageRoute(
      builder: (context) => HomePage(
        email: emailController.text,
    )),
  );
} else {
  ScaffoldMessenger.of(context).showSnackBar(
    const SnackBar(
      content: Text('Invalid Credentials')),
    );
}
```

Here's the final code for the Submit button. 

```
Padding(
  padding:
    const EdgeInsets.symmetric(horizontal: 8, vertical: 16.0),
      child: Center(
        child: ElevatedButton(
          onPressed: () {
            if (_formKey.currentState!.validate()) {
              if (emailController.text == "arun@gogosoon.com" &&
                            passwordController.text == "qazxswedcvfr") {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => HomePage(
                      email: emailController.text,
                    )),
                );
              } else {
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(
                    content: Text('Invalid Credentials')),
                  );
              }
            } else {
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(content: Text('Please fill input')),
              );
            }
          },
        child: const Text('Submit'),
      ),
    ),
),
```

Let's try to understand this code. 

In addition to form validation, we are adding another layer of validation which checks if the user has typed the email address as "arun@gogosoon.com", (which is my email address, you can replace it with whatever you want) and the password as "qazxswedcvfr". We navigate the user to the Home page if the entered credentials match, and show "Invalid Credentials" in the Snackbar otherwise. 

That's it. We have covered a very basic login validation. Try to run the app and check if your app works as expected. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-91.png)
_Login Page_

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-92.png)
_Home Page_

## Conclusion

In this article, you have learned to build a basic version of a login app using Flutter. Hope you're clear on the flow of building the Flutter app. 

If you're curious to learn Flutter further, try out the exercise I'm adding below. Searching, applying the code, and getting the result by yourself will make you more confident in Flutter app development. 

1. Try to add an eye icon at the end of the "Password" input field. Clicking on it should toggle showing the password in plain text and hidden text
2. Clear the Email and Password input fields before navigating to the Home page
3. Add additional regex validation for email input
4. Add validation to the password field if the user has entered at least one number, letter, and a symbol
5. Add a "Signup" button below the "Submit" button which should navigate the user to a new "Signup" page

To learn more about Flutter, subscribe to my email newsletter on my [site](https://5minslearn.gogosoon.com/?ref=fcc_flutter_login_app) ([https://5minslearn.gogosoon.com](https://5minslearn.gogosoon.com/?ref=fcc_flutter_login_app)) and follow me on social media. 


