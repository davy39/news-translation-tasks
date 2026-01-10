---
title: How to Build a React Native App and Integrate It with Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-01T10:00:00.000Z'
originalURL: https://freecodecamp.org/news/react-native-firebase-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/react-native-firebase.png
tags:
- name: Firebase
  slug: firebase
- name: React Native
  slug: react-native
seo_title: null
seo_desc: "By Florian Marcu\nIn this tutorial, we are going to build a React Native\
  \ app that is integrated with a Firebase backend. The app will support both the\
  \ React Native CLI as well as Expo CLI. \nThis React Native Firebase tutorial will\
  \ cover the main featu..."
---

By Florian Marcu

In this tutorial, we are going to build a React Native app that is integrated with a Firebase backend. The app will support both the React Native CLI as well as Expo CLI. 

This **React Native Firebase** tutorial will cover the main features such as authentication, registration, and database (Firestore) CRUD operations.

You can also [download the full source code](https://github.com/instamobile/react-native-firebase) from Github if you want to jump straight into the code.

This tutorial will walk you through the details of the following sections:

1. **Creating a Firebase project**
2. **Creating & configuring a new React Native app**
3. **Setting up the folder structure, routes, and navigation**
4. **Implementing the UI for Login, Registration, and Home screens**
5. **Registration with Firebase Auth**
6. **Login with Firebase Auth**
7. **Persistent Login Credentials**
8. **Writing and reading data from Firebase Firestore**

Without further ado, let’s start building out the React Native Firebase project. The final mobile app will look like this:

![react native firebase](https://www.freecodecamp.org/news/content/images/2020/05/react-native-firebase-1.png)

## 1. Create a Firebase Project

Head over to [Firebase.com](https://firebase.google.com/) and create a new account. Once logged in, you’ll be able to create a new project in the [Firebase Console](https://console.firebase.google.com/u/0/).

* Create a new account on [Firebase.com](https://firebase.google.com/)
* Create a new project in [Firebase Console](https://console.firebase.google.com/)
* Enable Email & Password auth method in _Firebase Console_ -> _Authentication_ -> _Sign-in method_

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1__J2bqHTUxhs_sTxwRdbvAg.png)

* Create a new iOS app, with App ID _com.reactnativefirebase_

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_RFyy5eHgUlZIEQtaCj5ddA.png)

* (Optional) Create a new Android app with package name _com.reactnativefirebase_
* Download the configuration file generated at the next step to your computer (_GoogleService-Info.plist_ for iOS, and _google-services.json_ for Android)

Firebase allows you to build _backendless_ apps. It’s a product running on top of Google Cloud, and allows developers to build web and mobile apps without needing their own servers. 

This saves a lot of time, since you don’t need to write any backend code. It’s also highly scalable, being backed by Google infrastructure.

In Firebase, you’ll be able to store everything that’s needed for your app — users, data, files, push notification tokens, etc. All this information is made available to the mobile clients via the Firebase SDKs, which are compatible with React Native. This means that all the interactions with the backend is abstracted out and encapsulated in the SDK, so mobile developers don’t need to worry about API calls, data parsing, sockets management, and so on.

## **2. Create and Configure a New React Native App**

We’re going to make our React Native Firebase app compatible with both Expo CLI and React Native CLI. 

We’re going to use Expo for now, since it makes it easy for newcomers to preview their apps. But we won’t use any Expo specific libraries, so the _src_ code can be simply used in any React Native app, regardless of its scaffolding.

We are going to use the [Firebase Web SDK](https://firebase.google.com/docs/reference/js), which is compatible with both Expo and React Native CLI, and is supported directly by Google. 

If you want to use [react-native-firebase](https://rnfirebase.io/) instead, feel free to install and configure that (the code will still be the same). But keep in mind that we don’t recommend it for a few reasons:

* it is not directly supported by Google, so maintaining it will be much harder given it’s an extra layer that can cause bugs, and 
* it also doesn’t work with Expo, which can be a deal breaker for many developers.

The steps below are also covered in the official React Native documentation on [how to set up your dev environment](https://reactnative.dev/docs/environment-setup).

* Install Expo CLI

In your Terminal, simply run

```
npm install -g expo-cli
```

* Create a new React Native app by running

```
expo init react-native-firebase

```

For the template, choose the _Managed Workflow_ — _Blank_

* Start the app by running

```
yarn ios
// or
yarn android

```

This will also present you with a QR code which you can scan using the Camera app on iOS, or the Expo app on Android.

This is great. We now have a new React Native app, running on both iOS and Android. Let’s start connecting it to your Firebase backend.

* Add the Firebase SDK to the React Native project

```
yarn add firebase

```

* Add React Native Navigation library by running

```
yarn add @react-navigation/native && yarn add @react-navigation/stack && expo install react-native-gesture-handler react-native-reanimated react-native-screens react-native-safe-area-context @react-native-community/masked-view
```

* Add various UI components and packages to be used in the project

```
yarn add react-native-keyboard-aware-scroll-view base-64

```

Create a Firebase config file

```
mkdir src src/firebase && touch src/firebase/config.js
```

Add your firebase configuration into _src/firebase/config.js:_

<script src="https://gist.github.com/mrcflorian/f6e52d359d09b27745f27950ba601ac1.js"></script>

You can get all this information from [Firebase Console](https://console.firebase.google.com/) -> Project Settings

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_RU6D6YeIhpIprROu8lmOOw.png)

## 3. Create the Folder Structure and Set Up Routes and Navigation

* Create the folder structure by running

```
mkdir src/screens src/screens/LoginScreen src/screens/RegistrationScreen src/screens/HomeScreen
```

* Create the files structure by running

```
touch src/screens/index.js src/screens/LoginScreen/LoginScreen.js src/screens/LoginScreen/styles.js src/screens/RegistrationScreen/RegistrationScreen.js src/screens/styles.js src/screens/HomeScreen/HomeScreen.js src/screens/HomeScreen/styles.js
```

* Add this code to _src/screens/index.js_

```
export { default as LoginScreen } from './LoginScreen/LoginScreen'

export { default as HomeScreen } from './HomeScreen/HomeScreen'

export { default as RegistrationScreen } from './RegistrationScreen/RegistrationScreen'

```

Don’t worry if the project is broken! Everything will make sense in a little while.

* Set up the routes & navigators

Override _App.js_ file with the following code snippet:

<script src="https://gist.github.com/mrcflorian/411d266eaf5c081535692eaf0cf6f4b0.js"></script>

## 4. Implement the UI

Now that we have the scaffold of the app, let’s go ahead and implement the UI components of all screens. We’re not going into the details of flex layout and React Native styling, since that is outside the scope for this tutorial. We’re going to focus mostly on React Native Firebase integration. 

Simply override the files as follows:

* src/LoginScreen/LoginScreen.js

<script src="https://gist.github.com/mrcflorian/1d94b6907d3b6521d698512aa55ebeb7.js"></script>

* src/LoginScreen/styles.js

<script src="https://gist.github.com/mrcflorian/499dcf5064d03673ee9f76af2abd1e3f.js"></script>

* src/RegistrationScreen/RegistrationScreen.js

<script src="https://gist.github.com/mrcflorian/1d6924cca7ccda5e9da4f84d3208fc94.js"></script>

* src/RegistrationScreen/styles.js

<script src="https://gist.github.com/mrcflorian/499dcf5064d03673ee9f76af2abd1e3f.js"></script>

* src/HomeScreen/HomeScreen.js

<script src="https://gist.github.com/mrcflorian/bbd57208348528de759f7797936210d1.js"></script>

* src/HomeScreen/styles.js

<script src="https://gist.github.com/mrcflorian/36c027ce741269d387b261c1fa6ea6aa.js"></script>

At this point, your app should run properly and display the following screens (UI only):

![react native firebase auth](https://www.freecodecamp.org/news/content/images/2020/05/1_rwQyQ3ZCE7rgHukTAeLliw.png)

You can switch between the two screens by tapping the links buttons in the footer.

Now that we have a beautiful UI for login and sign up, let’s see how we can integrate our React Native (and Expo) app with Firebase.

## 5. React Native Firebase — Registration

Let’s start with creating a new account with Firebase Auth, since naturally login comes after. For this, we are going to add the Firebase logic for creating a new account with email & password in _RegistrationScreen.js_, by implementing the _onRegisterPress_ method as follows:

<script src="https://gist.github.com/mrcflorian/427ae7cdc5d6ece1461046b91bcb1112.js"></script>

In the account creation flow above, we do a few important things:

* We call Firebase Auth’s createUserWithEmailAndPassword API (line 13), which creates a new account that will show up in Firebase Console -> Authentication table.
* If the account registration was successful, we also store the user data in Firebase Firestore (line 24). This is necessary for storing extra user information, such as full name, profile photo URL, and so on, which cannot be stored in the Authentication table.
* If registration was successful, we navigate to the Home Screen, by passing in the user object data as well.
* If any error occurs, we simply show an alert with it. Errors can be things such as no network connection, password too short, email invalid, and so on.

Reload your app and test the registration. If you successfully created one account, check that it shows up in _Firebase Console_ -> _Authentication_:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_qy_k5wsgw4MAALmIeBxYpg.png)

## 6. React Native Firebase — Login

Now that we are able to create new accounts, let’s implement the login functionality. Firebase SDK takes care of all the authorization and authentication steps needed for a secure login.

Open _LoginScreen.js_, import firebase and complete the _onLoginPress_ method:

<script src="https://gist.github.com/mrcflorian/99d7b46ae8323f103213e331c1f1d7ff.js"></script>

Reload your app and go ahead and login with an existing account. The app should take you to the home screen if the credentials were correct, or it will alert you with an error if anything went wrong.

## 7. Persist Login Credentials

You’ll notice that if you quit the app and open it again, it will show the login screen again. For a good user experience, we’d want to land all logged in users on the Home screen. No one wants to type in their login credentials every time they want to use an app.

This is also known as persistent login. Fortunately, Firebase SDK takes care of this for us, dealing with all the security concerns. Persistent login is enabled by default in Firebase, so all we need to do is fetch the currently logged in user.

Open _App.js_ and let’s implement the persistent login feature:

<script src="https://gist.github.com/mrcflorian/b93251517dd6239848f8a66ec6160a39.js"></script>

_onAuthStateChanged_ returns the currently logged in user. We then fetch all the extra user data that we stored in Firestore, and set it on the current component’s state. This will re-render the app component, which will display the Home screen.

Notice how we call this the first time the app loads by leveraging the [useEffect](https://reactjs.org/docs/hooks-effect.html) hook.

## 8. Writing and Reading Data from Firebase Firestore

We’ve already used Firestore above, for saving extra information on our users (the full name). In this dedicated section, we’re going to see how we can write data to Firestore, and how we can query it.

We’ll also cover how to observe (listen to) changes in the Firestore collection and have those be reflected on the screen, in real-time. These can be very helpful in real-time apps, such as a [React Native Chat](https://www.instamobile.io/app-templates/video-chat-app-in-react-native/).

To simplify, we are going to save some text items into a Firestore collection named “entities”. Think of these as tasks, posts, tweets, anything you want. We’ll create a simple file that adds a new entity and we’ll also list all the entities that belong to the currently logged in user. Additionally, the list will be updated in real-time.

* Implement _HomeScreen.js_ by rewriting it to the code below

<script src="https://gist.github.com/mrcflorian/d196fd9a0a77188240ab73b66ec46f3c.js"></script>

* Style the home screen, by overriding _HomeScreen/styles.js_ to:

<script src="https://gist.github.com/mrcflorian/997aad06bec46618697c293fb2446623.js"></script>

* Reload the app and observe the new home screen. Type in some text and press the _Add_ button
* Nothing happened.
* Create an index on the entities Firestore collection

You’ll notice that the list of entities is not rendered. If you check out the logs, you’ll see an warning about “The query requires an index”, followed by a long URL:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_bfOrtReOOo9B_pDR4_Zm9w.png)

This informs us that we can’t query the entities table by _authorID_ and sort the data by _createdAt_ in descending order, unless we create an index. Creating an index is actually really easy — simply click on that URL and then click the button:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_72kARyPWnDypbCko7e4U1Q.png)

* Reload the app again

Now everything works as expected:

* The app lists all the entities in the entities collection, in descending creation order
* Adding a new entity works fine
* The list updates in real-time (try deleting an entry directly in the database, or adding a new one directly from the app)

This is how your Firestore database looks like now:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/1_zPT7lLNr6kvtdazgN50eKg.png)

This is how you read and write from Firestore in React Native. Let’s move forward to the last section.

Play around with the app, by adding new entities. This is the final project:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/react-native-firebase-2.png)

## **Conclusion**

Firebase makes it really easy to add authentication and database support to any React Native app. Firebase SDK is extremely powerful, supporting a lot of common reading and writing database patterns. 

In addition to React Native, Firebase SDK provides support for a lot of other languages, such as [Swift](https://www.iosapptemplates.com/blog/swift-programming/firebase-swift-tutorial-login-registration-ios), [Kotlin](https://www.instakotlin.com/templates/android-starter-kit-with-firebase/) or [Flutter](https://www.instaflutter.com/app-templates/flutter-login-screen/). Check out those links for similar Firebase starter kits in various languages.

We’ve showcased the most basic ones in this React Native Firebase tutorial. In the next series, we’ll cover more advanced features, such as Firebase Storage (file upload) and push notifications.

If you liked this tutorial, please give me a star on the [Github repo](https://github.com/instamobile/react-native-firebase) and share this with your community. You can check out even more [free React Native projects](https://www.instamobile.io/mobile-templates/react-native-templates-free/) on Instamobile. Cheers!

