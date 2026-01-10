---
title: How to Set Up GitHub User Authentication using Firebase and React (with Hooks)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-06T18:18:52.000Z'
originalURL: https://freecodecamp.org/news/github-user-authentication-using-firebase-and-reactjs-with-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Modern-Music-Electronic-Channel-Youtube-Thumbnail-3.png
tags:
- name: authentication
  slug: authentication
- name: Firebase
  slug: firebase
- name: GitHub
  slug: github
- name: React
  slug: react
seo_title: null
seo_desc: 'By Rishi Purwar

  In this tutorial, I will walk you through the process of creating a GitHub User
  Authentication System using Firebase and React (with hooks).

  If you have ever tried building an authentication system before, you might agree
  that it can ...'
---

By Rishi Purwar

In this tutorial, I will walk you through the process of creating a GitHub User Authentication System using Firebase and React (with hooks).

If you have ever tried building an authentication system before, you might agree that it can be painful. This is where Firebase steps in. Firebase provides user authentication out of the box, so you don't need to write complex authentication code from scratch – which saves a lot of time.

In this article, we will build a simple Profile Card Component that'll show an authenticated user GitHub profile data such as profile picture, display name, and username. 

We'll also see how we can use `ContextAPI` and the `useReducer` hook to manage the state of the authenticated user like a pro.

🚀 Let's get started!

Note that you'll need a basic understanding of React to follow this tutorial.

* [How to Create a New React Project](#heading-how-to-create-a-new-react-project)
* [🧹 Pre-Project Housekeeping](#heading-pre-project-housekeeping)
* [How to Set Up Firebase](#heading-how-to-set-up-firebase)
* [How to Set Up Firebase Auth](#heading-how-to-set-up-firebase-auth)
* [How to Create a GitHub Log in a Hook](#heading-how-to-create-a-github-log-in-a-hook)
* [How to Build the Login Functionality](#heading-how-to-build-the-login-functionality)
* [How to Build the Log Out Functionality](#heading-how-to-build-the-log-out-functionality)
* [How to Create an Authentication Context](#heading-how-to-create-an-authentication-context)
* [How to Create a Context Provider](#heading-how-to-create-a-context-provider)
* [How to Create a Reducer Function](#heading-how-to-create-a-reducer-function)
* [How to Wire Up Context and Reducer](#heading-how-to-wire-up-context-and-reducer)
* [How to Update the Auth Context Value](https://www.freecodecamp.org/news/p/95ce6097-8ce9-427b-afeb-a8731e785c4b/how-to-update-the-auth-context-value)
* [How to Persist Auth State](#heading-how-to-persist-auth-state)
* [How to Add a Profile Card Component](#heading-how-to-add-a-profile-card-component)
* [How to Save a User to Firebase](#heading-how-to-save-a-user-to-firebase)
* [🙏 Thank you for reading this tutorial](#heading-thank-you-for-reading-this-tutorial)

## How to Create a New React Project

The first step to getting started is to use the [create-react-app](https://reactjs.org/docs/create-a-new-react-app.html) tool to generate a new React project. If you don't already have it installed, first open your terminal and run this command to install it globally:

```
npm install -g create-react-app

```

Once it's installed, you can run the following command to generate a new React project:

```
npx create-react-app react-firebase-github-auth

```

Once you execute this command, create-react-app will take a few minutes to download and install all of the required dependencies. This might seem like a long time, but it's normal! You can go make yourself some tea while that happens.

When the process is complete, cd into the directory using the `cd react-firebase-github-auth` command. Now that we're in our project directory, let's run `code .` to open the project folder into your code editor (I'm using VS Code). 

Now open your terminal by pressing `ctrl + `` and run `npm start` to start the development server. This will open up a new browser tab with our app running inside it. Your browser will display something like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/BqGj8FM.png)

## 🧹 Pre-Project Housekeeping

Now that you've created a new project, we're going to do some pre-project housekeeping.

The `create-react-app` command we ran earlier has created a lot of files that we won't need in our project. We're going to delete some of the files to keep things tidy.

The first thing to do is replace the whole code of the `App.js` file with this:

```
const App = () => {

  return (
    <div className="App">
      <button className="btn">
        Login With Github
      </button>
      <button className="btn">
        Log Out
      </button>
    </div>
  );
};

export default App;



```

Now that you've replaced the whole code of your **App.js** file, let's add some CSS for your **App** component. Open your `index.css` and replace the content with the following styles. We won't be focusing on styling much, so here are the styles for you to use:

```
@import url("https://fonts.googleapis.com/css2?family=Overpass:wght@400;700&display=swap");

* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

.App {
  font-family: "Overpass", sans-serif;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: hsl(216, 12%, 8%);
}

.btn {
  border: none;
  background-color: hsl(25, 97%, 53%);
  cursor: pointer;
  border-radius: 6px;
  color: white;
  font-weight: bold;
  padding: 12px 14px;
  font-size: 18px;
  margin-top: 8px;
}

.btn:hover {
  background-color: hsla(25, 97%, 53%, 0.668);
  transition: all 100ms linear;
}

.github-logo {
  width: 18px;
  margin-right: 6px;
  vertical-align: middle;
}

```

Let's go ahead and delete some unnecessary files as well. Open up your terminal and run the following command. Make sure you're in the root directory of your project folder:

```
cd src

rm -- App.test.js App.css logo.svg serviceWorker.js setupTests.js

cd ..

```

Note: If you stopped your server to do the terminal tasks mentioned above, you'll have to start it again using npm start.

## How to Set Up Firebase

Before diving into React and coding some good stuff, we need to set up our own Firebase project through the Firebase Console. 

To get started, navigate your browser to [Firebase Console](https://console.firebase.google.com/). Make sure you are logged into your Google account.

Now, click on Add project, and you should see the following screen:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/1CquSV9Qf.png)

You can name your project anything you want. But for this example, we will call it "react-firebase-github-auth". Once that is done, click on the **Continue** button. You should see something like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/SfFPlAwOu.png)

Now, you'll see a toggle button to enable Google Analytics for this project. But we won't need it, so simply click on that toggle button to disable it. You can enable it later on if you want.

Once you've created your Firebase project, click on the **Continue** button to go to your project dashboard, which looks something like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/dM0vleyHO--1-.png)

Now that we've set up a Firebase project let's go ahead and register our React app to start using Firebase. 

So, to do that, click on the code icon(</>) that I pointed out in the above screenshot. Now, give it a name. For this tutorial, I'll call it "react-firebase-github-auth" and click on the **Register app** to register our app. You should see the following config code:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/sY07iiBu6--1--2.png)

Copy the whole config code by clicking on the copy to clipboard button and click on the `Continue to console` button. Then we need to create a file in our project to store it. 

Let's head over to our React app, create a new folder inside `src`, and call it `firebase`. Inside this Firebase folder, create a new file and name it `config.js` and paste your config code into this file. 

If you want, you can remove the comments from your config.js file. You also don't need to create an app variable. Instead, you can call `initializeApp()` without saving it to a variable. Now, your code should look similar to this:

```
import { initializeApp } from "firebase/app";

const firebaseConfig = {
  apiKey: "AIzaSyA2jZRiXP36UXbBS2xuV1UE4Yr3dYwhX24",
  authDomain: "react-firebase-github-au-eb675.firebaseapp.com",
  projectId: "react-firebase-github-au-eb675",
  storageBucket: "react-firebase-github-au-eb675.appspot.com",
  messagingSenderId: "605356741694",
  appId: "1:605356741694:web:5efdfac0ea6046e25c2d6f",
};

// Initialize Firebase
initializeApp(firebaseConfig);

```

Now, let's install Firebase using npm to our project. So to do this, open your terminal and run this command:

```
npm install firebase

```

This workflow uses npm and requires module bundlers or JavaScript framework tooling. This is because the v9 SDK is optimized to work with module bundlers to eliminate unused code (tree-shaking) and decrease app size.

## How to Set Up Firebase Auth

After creating a Firebase project in your Firebase Console, you need to enable the GitHub provider. To do this, follow these steps:

* Go to your Firebase Project dashboard and click on the **Authentication** tab on the sidebar.
* Now, click on the **Get started** button, then click on the **Sign-In Method** tab, and then select the **GitHub Sign-in** provider.
* After that, click on the toggle button to enable the Github Auth.

Now, you need to add the `Client ID` and `Client Secret` from the GitHub developer console.

To get your `Client ID` and `Client Secret`, first [register your app](https://github.com/settings/applications/new) as a developer application on GitHub, and you'll see an application form which looks like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/P0SjzJSFc--1--3.png)

Fill out this form and ensure your **Firebase OAuth redirect URI** (for example, my-app-12345.firebaseapp.com/__/auth/handler) is set as your **Authorization callback URL**. You can find your **Firebase OAuth redirect URI** here:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/GltEGGRMI.png)

Now click on **Register application**. You'll see your `Client ID`, but you need to generate your `Client secrets` by clicking on the **Generate a new client secret** button. Now copy your `Client ID` and `Client secrets` from the GitHub application page and paste them in your Firebase GitHub Sign-in providers form.

Click **Save**.

Now that we've enabled GitHub Auth on our Firebase project, it's time to initialize it on the frontend. 

First, open your `config.js` file and import `getAuth` from the `firebase/auth` just below the `initializeApp` import statement. 

Then we're going to create a variable called `auth` and set it equal to the `getAuth()`. And finally, export this `auth` variable from here. 

Your code should look like this:

```
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyAaHLAnc5DXxHHFtcjIO7dQVe9i9OKsFqg",
  authDomain: "fir-github-auth-b5110.firebaseapp.com",
  projectId: "fir-github-auth-b5110",
  storageBucket: "fir-github-auth-b5110.appspot.com",
  messagingSenderId: "857975576429",
  appId: "1:857975576429:web:0a1d4e6a5a3b08febcac64",
};

// Initialize Firebase
initializeApp(firebaseConfig);

// Initialize Firebase Auth
const auth = getAuth();

export { auth };

```

Now that we've got all of this setup, we can use the Firebase Authentication services like **Log In** and **Log Out** in any component we need to!

## How to Create a GitHub Log in a Hook

So far, we have added a Firebase to our project. Now, let's use it.

First, let's create a custom hook to sign up users using their GitHub accounts. So to do that, first, make a folder inside the `src` folder called `hooks`. Inside this, create a new file and name it `useLogin.js`. In this file add the following code:

```
import { GithubAuthProvider, signInWithPopup } from "firebase/auth";
import { auth } from "../firebase/config";
import { useState } from "react";

export const useLogin = () => {
  const [error, setError] = useState(false);
  const [isPending, setIsPending] = useState(false);
  const provider = new GithubAuthProvider();

  const login = async () => {
    setError(null);
    setIsPending(true);

    try {
      const res = await signInWithPopup(auth, provider);
      if (!res) {
        throw new Error("Could not complete signup");
      }

      const user = res.user;
      console.log(user);
      setIsPending(false)
    } catch (error) {
      console.log(error);
      setError(error.message);
      setIsPending(false);
    }
  };

  return { login, error, isPending };
};

```

I'm going to walk through the above code. Don't worry—it's not scary! You'll understand it all in a jiffy.

The first two lines are pretty simple—they just import some bits from Firebase and auth from our config.js file that we'll need later on. In the third line, we're importing the `useState` hook from the React module.

The fifth line is where things get interesting! We've created a function called `useLogin` and exported it immediately on the same line. Inside that function, we're creating two states using the useState hook: `error` and `isPending`. 

We'll use the error state for showing errors, and isPending state for showing the pending state. 

For example, let's say a user clicks on the signup button, and we set isPending to `true`. When a signup request is complete, we can set it back to false using setisPending(false). We can use this `isPending` state to add a loader to show a pending state in our component.

And after that we created an instance of the GitHub provider object:

```
const provider = new GithubAuthProvider();

```

Then we're creating a login function, and inside that we've added this piece of code:

```
setError(null);
setIsPending(true);

```

When the above code runs, it will automatically set the state of the error to null and the state of `isPending` to true. This means that when you login, you'll see no errors, but you'll have pending states on your page.

And just below that, we've added a `try-catch` block, In the try block, we're trying to sign up the user using the `signInWithPopup` function. But we have two ways to prompt users to sign in with their GitHub accounts: either by **opening a pop-up window** or by **redirecting to the sign-in page**.

In this blog, we're using `signInWithPopup` that takes two arguments. The first is the `auth` and the second is the `provider`.

And in the `catch` block, we're catching the error if it occurs in the try block. If it occurs, then we'll set it using `setError(error.message)`. We'll also set `isPending` equal to `false` because we've finished doing what we've been trying to do and now have a response – either a logged-in user or an error.

Finally, we're exporting the **login** function, **error**, and **isPending** so that we can use them in other components.

## How to Build the Login Functionality

Now that we've created a `useLogin` hook, let's use it to login the users using their GitHub accounts.

Let's start by importing the `useLogin` hook from `./hooks/useLogin` in our **App.js** file that we exported from the `useLogin.js`. Then we'll call this hook at the start of the App component and destructure two things: `login` function and `isPending` state:

```
import { useLogin } from "./hooks/useLogin";
....
const App = () => {
  const { login, isPending } = useLogin();

  return (
    <div className="App">
....

```

Now, let's add an `onClick` event handler to our `Login With Github` button in order to call the `login` function when the user clicks on the button. We'll also show a button text conditionally – if `isPending` is true then show `Loading...` else show `Login With Github`. 

Your button code should look like this:

```
<div className="App">
    <button className="btn" onClick={login}>
        {isPending ? "Loading..." : "Login With Github"}
    </button>
</div>

```

Now, let's test our log-in button. Click on the `Login With Github` button, and it should open up a new window then you need to authorize your React app.Then you'll see a user object gets printed on your console that looks something similar to this:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/2A4p7e3T3-2.png)

Now open your Firebase project dashboard and click on the Authentication tab. You'll see a logged-in user that looks something like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Gda8EuxXf.png)

## How to Build the Log Out Functionality

Now that we can log in the users, what do we do next? Well, it's time to work on the functionality to log out the user. It is actually relatively easier than logging them in. 

So, first, let's create a `useLogout` custom hook to log out the user. To do that, create a file and name it `useLogout.js` inside the `hooks` folder. In this file, add the following code:

```
import { signOut } from "firebase/auth";
import { auth } from "../firebase/config";

export const useLogout = () => {

  const logout = async () => {
    try {
      await signOut(auth);
      console.log("user logged out")
    } catch (error) {
      console.log(error.message);
    }
  };

  return { logout };
};


```

I'm going to walk through the above code. You'll understand it all in a jiffy.

The first two lines are pretty simple—we just import the `signOut` function from Firebase and `auth` from our config.js file that we'll need later on.

The fourth line is where things get interesting! We've created a function called `useLogout` and exported it immediately on the same line.

Then we're creating an async `logout` function and exporting it on the same line. Inside that, we've added a `try-catch` block. In the try block, we're logging users out using the `signOut` method that's provided by `firebase/auth`. And in the catch block, we're catching the error if it occurs in the try block.

Now, let's import this `useLogout` hook into the App.js component like this:

```
import { useLogout } from "./hooks/useLogout";

```

And just below the line where we call the `useLogin()` hook, call the `useLogout` hook as well:

```
const { logout } = useLogout();

```

Now, let's add an `onClick` event handler to the `Log Out` button in order to call the `useLogout` function when the user clicks on the button. Your button code should look like this:

```
<button className="btn" onClick={logout}>
    Log Out
</button>

```

Now, time to test our log-out functionality. Click on the `Log Out` button if you're already logged in. If you're not logged in, log in first and then click on the Log Out button. Now, you should see a **" user logged out"** printed in your console:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/n3gT5cWkg.png)

## How to Create an Authentication Context

Now that we're able to sign up and log out the user, we want to store the user object in some kind of global state when the user is logged in. This will let us access the user data to our components without doing prop drilling.

If you don't know about Context, let me explain it to you briefly:

[Context API](https://reactjs.org/docs/context.html) is a way of sharing data between React components without using props. This means that you can pass data directly to the components that need them instead of through intermediate components. It does this by providing a sort of global store for data.

Now, we're going to create a context for our React app. The first thing we'll do is create a folder for our context inside the `src` folder and we'll call it `contexts`. This folder will be where we put all our application's contexts (if we have more than one context, then we'll put all of them in this folder. But for this small React app, we're only going to create one context for auth). 

Now, let's create a file for our context under the contexts folder and name it `AuthContext.js`. Our new AuthContext.js file is currently empty! Open it up and give it its first two lines:

```
import { createContext } from "react";

export const AuthContext = createContext();

```

This `createContext` function which React provides us basically creates a context object.We'll use this object to consume the context in our components. I'll show you how to consume context in a later section.

## How to Create a Context Provider

The AuthContext that we have created above gives us access to the `AuthContext.Provider` component that we use to provide context to all the child elements. 

To set the value of the context, we need to use the `value` prop available on the `<AuthContext.Provider value={/* some value */}>`.

Copy the following snippet, then paste it into `AuthContext.js` beneath your `createContext()` function.

```
const AuthContextProvider = ({ children }) => {

  return (
    <AuthContext.Provider value={/* some value */}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContextProvider;

```

## How to Create a Reducer Function

First, let's talk about what reducers are. A reducer function is a JavaScript function that takes two parameters: **state** and **action**. The state parameter is the current state of the application, while the action parameter is an object describing the action being performed by the user.

To create a reducer function, let's first create a folder inside `src` folder and name it `reducers`. Inside this reducers folder, create a file and call it `authReducer.js`.

Our new `authReducer.js` file is currently empty! Copy the following snippet, then paste it into authReducer.js.

```
export const authReducer = (state, action) => {
  switch (action.type) {
    case "LOGIN":
      return { ...state, user: action.payload };
    case "LOGOUT":
      return { ...state, user: null };
    case "AUTH_IS_READY":
      return { ...state, user: action.payload, authIsReady: true };
    default:
      return state;
  }
};


```

Let me walk through the above code:

The above code is basically a function that takes two parameters: **state** and **action**. Inside this function, we added a switch case to determine the action type and run the corresponding case according to the action type. 

For example, if you click on a login button on your webpage and it dispatches a "LOGIN" action, then this would be handled by one of these case statements. If there is no match for one of these cases, then it will return the state unchanged. This means that if no actions are dispatched, then nothing happens!

You might be wondering what this action means. An action is an object that describes how to update the state. The actions are performed by a user on some user interaction, such as clicking on a button or pressing an arrow key. 

This action object typically has two keys:

1. **type:** The type of action being performed. This is simply a string, and it's important to use a descriptive string. For example, you might use **"LOGIN"** or **"LOGOUT"**, depending on what you're doing.
2. **payload:** The payload for the action is whatever data you need to pass along with the type of action being performed. If you're signing a user up, then this could be the user data.

If you're wondering where I'm going with this, don't worry—it'll make sense soon!

## How to Wire Up Context and Reducer

Let's wire up our **authReducer** with our **AuthContext**. So to do that, first import the reducer function from `authReducer.js` into the `AuthContext.js` file.

```
import { authReducer } from "../reducers/authReducer";

```

Now, we're going to use a `useReducer` hook. The `useReducer(reducer, initialState)` takes two arguments: a **reducer** and an **initial state**. 

In this case, we're just passing in our `authReducer` function and an initial state object which has two properties: **user** and **authIsReady**:

```
{
    user: null,
    authIsReady: false,
}

```

So, let's import the `useReducer` hook into this file from the React. Update your very first line so that it reads like this:

```
import { createContext, useReducer } from "react";

```

This useReducer hook returns us an array of two items that have both our current `state` as well as the `dispatch` method. (If you're familiar with Redux, you already know how this dispatch method works.).

Now, let's add the below code just above the return keyword of the `AuthContextProvider` component:

```
  const [state, dispatch] = useReducer(authReducer, {
    user: null,
    authIsReady: false,
  });

```

Now that we've destructured the `state` and `dispatch` values from the array using [array destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment#examples), let's update the `value` prop of `AuthContext.Provider` so that it includes all of these values:

```
<AuthContext.Provider value={{ ...state, dispatch }}>

```

Let's also add a `console.log(state)` just above the return statement, so we can see the state of the user when it gets changed.

Now that we've created a context, let's import the `AuthContextProvider` component into the `index.js` file to use it:

```
import AuthContextProvider from "./contexts/AuthContext";

```

And now wrap your `App` component with the `AuthContextProvider` component to provide a context to your whole app. To do that, wrap your App component like this:

```
<AuthContextProvider>
    <App />
</AuthContextProvider>

```

Now, let's go back to our App component and see how we can use the AuthContext object in order to get the user details. First, let's import the `AuthContext` object from the `AuthContext.js` into the `App.js` file:

```
import { AuthContext } from "./contexts/AuthContext";

```

And we also need to import the `useContext` hook into this file, so that we can consume the AuthContext object:

```
import { useContext } from "react";

```

A `useContext` hook accepts a context object (the value returned from `createContext()`) and returns the current context value for that context. 

The current context value is determined by the value prop of the `<AuthContext.Provider value={{ ...state, dispatch }}>`.

Now let's call this `useContext` with our `AuthContext` object. Add this piece of code just above the return statement of the App component

```
const { user } = useContext(AuthContext);
console.log(user);

```

Now, let's refresh the page. You should see `null` get printed from your `App.js` file. If you try to log in using your GitHub account, it still print `null`. 

If you're wondering why you only see `null` even if you are logged in, it's because, on Login or Logout, we're not updating our context value – it's always showing an initial value that we passed.

To fix this, we need to update our context value using the `dispatch` method whenever we Log in or Log out.

## How to Update the Auth Context Value

Now that we've set up the Auth Context and Auth Reducer, now let's use them to update the state.

First of all, let's import the `AuthContext` object from the `AuthContext.js` into the `useLogin.js` file:

```
import { AuthContext } from "../contexts/AuthContext";

```

And now import the `useContext` hook into this file, so that we can consume the AuthContext object — update your `useState` import line so that it reads like this:

```
import { useContext, useState } from "react";

```

Now let's call this useContext with our AuthContext object. Add this piece of code below the `GithubAuthProvider()` inside the `useLogin` function:

```
const { dispatch } = useContext(AuthContext);

```

Now, let's dispatch the `LOGIN` action to update the state. So, to do that, simply call the `dispatch` function with the action object just below the `user` variable inside the try block. Your try block code should look like this:

```
try {
      const res = await signInWithPopup(auth, provider);
      if (!res) {
        throw new Error("Could not complete signup");
      }

      const user = res.user;
      dispatch({ type: "LOGIN", payload: user });

      console.log(user);
      setIsPending(false);
    }

```

Save your file and try to login again, and you should see a user object get printed on the console from the App.js file when you log in.

Now, let's do the same thing with the logout functionality to update the state again when the user logs out.

So, to do that, open your `useLogout.js` file and import the `AuthContext` object from the `AuthContext.js`:

```
import { AuthContext } from "../contexts/AuthContext";

```

And now import the `useContext` hook into this file:

```
import { useContext } from "react";

```

Now let's call this useContext with our AuthContext object. Add this piece of code above the `logout` function inside the `useLogout` function:

```
const { dispatch } = useContext(AuthContext);

```

Now, let's dispatch the `LOGOUT` action. So, to do that, simply call the `dispatch` function with the action object just below the `await signOut(auth)` inside the try block. Your try block code should look like this:

```
try {
      await signOut(auth);
      dispatch({ type: "LOGOUT" });
      console.log("user logged out");
    }

```

Save your file and try to log out. You should see `null` and `user logged out` get printed on the console when you log out.

We have now successfully implemented the logic behind authenticating users using Firebase and ReactJS.

But there is still one issue left: when you try to refresh the page, you will see `null` printed on the console. This means that you're automatically logged out when you do a refresh! 

We don't want to log out our users on refresh. We can fix this problem by persisting the auth state using [onAuthStateChanged](https://firebase.google.com/docs/auth/web/start#set_an_authentication_state_observer_and_get_user_data) method that's provided by the `firebase/auth`.

## How to Persist Auth State

Now, open your `AuthContext.js` file and import `onAuthStateChanged` like this:

```
import { onAuthStateChanged } from "firebase/auth";

```

Now, let's import the `useEffect` hook into this file from the React. Update your very first line so that it reads like this:

```
import { createContext, useEffect, useReducer } from "react";

```

Now, import `auth` from `config.js` file:

```
import { auth } from "../firebase/config";

```

And then just above the return statement, add this piece of code:

```
  useEffect(() => {
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      dispatch({ type: "AUTH_IS_READY", payload: user });
    });
    return unsubscribe;
  }, []);

```

Let me quickly walk you through the above code, you'll understand everything in a moment.

In the first line, we use a hook called `useEffect()`, which takes in a function and empty dependencies array as arguments.

Then, we define an `onAuthStateChanged` method which takes two arguments: first, it takes the `auth` that we exported from the `config.js` file. Second, it takes a callback function that gets invoked **immediately** after registering the `onAuthStateChanged` observer with the current authentication state and whenever the authentication state changes.

And inside this callback function, we pass whatever data we receive from the user object and set our dispatch method to dispatch an action with type `AUTH_IS_READY` and payload as our user object to update the value of the context.

Finally, the onAuthStateChanged() function returns the [unsubscribe function](https://firebase.google.com/docs/reference/js/v8/firebase.auth.Auth#onauthstatechanged) to unregister the `onAuthStateChanged` observer. We save this function in a variable and name it `unsubscribe`. At the end, we return this `unsubscribe` function for cleanup to avoid memory leaks.

Now, if you do a refresh after logging in, you'll see a user object gets printed on the console.

So, that's all for the authentication logic. In the next section, we'll add a ProfileCard component to show logged-in user data.

## How to Add a Profile Card Component

Let's create a Profile Card component where we'll show logged-in data. To do that, first create a `components` folder inside the `src` folder. Inside this folder create a file and name it `ProfileCard.js` and add this piece of code:

```
import React from "react";
import { useLogout } from "../hooks/useLogout";

const ProfileCard = ({ user }) => {
  const { logout } = useLogout();
  return (
    <>
      <div className="profile-card">
        <img className="profile-img" src={user.photoURL} alt="" />
        <p>
          Name: <span>{user.displayName}</span>
        </p>
        <p>
          Username: <span>{user.reloadUserInfo.screenName}</span>
        </p>
        <p>
          Email: <span>{user.email}</span>
        </p>
        <p>
          User ID: <span>{user.uid}</span>
        </p>
      </div>
      <button className="btn" onClick={logout}>
        Log Out
      </button>
    </>
  );
};

export default ProfileCard;

```

As you can see, this component takes in a user prop from its parent component (that's `App`). Then we destructured this user prop using object destructuring.

Now, let's add some CSS for this ProfileCard component. Just copy and paste the following CSS into your index.css file:

```
.profile-card {
  text-align: center;
  background-color: hsl(213, 19%, 18%);
  border-radius: 8px;
  padding: 16px;
  box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
  margin-bottom: 4px;
}

.profile-img {
  border-radius: 50%;
  width: 112px;
  border: 4px solid hsl(25, 97%, 53%);
  margin-bottom: 8px;
}

p {
  color: hsl(216, 12%, 54%);
  font-size: 24px;
  font-weight: 700;
}

span {
  color: white;
  font-size: 18px;
  font-weight: 400;
}

```

Now, let's import this `ProfileCard` component into the `App.js` file:

```
import ProfileCard from "./components/ProfileCard";

```

Now, simply replace the content of the return statement with this piece of code:

```
return (
    <div className="App">
      {user ? (
        <ProfileCard user={user} />
      ) : (
        <button className="btn login-btn" onClick={login}>
          Login With GitHub
        </button>
      )}
    </div>
  );

```

As you can see, we're using a property called `user` to determine whether a user is logged in or not. 

If a user is logged in, then the `ProfileCard` component will be displayed. If a user is not logged in, then the `Login With GitHub` button element will be displayed.

Now, your app should look like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/06/31YHvHfM2.png)

But there is one problem: if you do a refresh it first shows a `Login With GitHub` button and then it shows a profile component. This is happening because Firebase takes some time to check whether a user is logged in or not.

This can be a bad user experience—especially if your app has private routes that users can only access when they are logged in. 

Let's say you have a website where users can access a private route only when they are logged in – and if they are not logged in then they will get redirected to the home page when they try to access the private route.

Let's say a user is logged in and is on the private route, and for some reason they do a refresh. What do you think will happen?

They will get redirected to the homepage because Firebase will take some time to verify whether they are logged in or not. This can be frustrating for the users of your website!

You may be wondering how we can fix this problem? 🤔

The solution to this problem is simple—if you remember, we added one property called `authIsReady` along with the `user` property to our initial state. We're going to use that property to solve this issue.

Open your `App.js` file and update your `useContext(AuthContext)` line so that it reads like this:

```
const { user, authIsReady } = useContext(AuthContext);

```

And now let's add one check right after the return keyword:

```
  return authIsReady ? (
    <div className="App">
      {user ? (
        <ProfileCard user={user} />
      ) : (
        <button className="btn login-btn" onClick={login}>
          Login With Github
        </button>
      )}
    </div>
  ) : (
    <h1>Making your auth ready, please wait for a moment</h1>
  );

```

Here we're simply checking if `authIsReady` is `true`, then showing an `App` component. If it's not, then we're showing a `Loader` component (in our case, we're simply showing some ugly-looking text, but you can add a beautiful loader instead).

Note: `authIsReady` doesn't mean we're logged in. It simply means that now that we have the user value it can be a null or a user object.

So, now you've created a great sign-up flow!

But we're not done yet. It's time to store some user data on Firebase when they first sign up.

This is something that I personally think is a really good idea. Let's say you're building a Job Posting website where you want to list out all the candidates that are registered on your website. How will you be able to do that if you don't store individual users' data?

Now let's add some logic to store user data in the next section.👇

## How to Save a User to Firebase

First, let's create our database. To start, go to your **Firebase Project dashboard** and click on the **Firebase Database** tab on the sidebar. 

Now, click on the **Create database** button to create a database. You'll be prompted to select a starting mode for your Cloud Firestore Security Rules. For now, select the test mode but you can change it later. Then click on the **Next** button.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/EFGHwYJ-R.png)

Next, select your Cloud Firestore location and click on the **Enable** button.  
Now that we have our database set up, we're ready to write some code! Let's jump right in.

First, open your `config.js` file and import the `getFirestore` module from Firebase:

```
import { getFirestore } from "firebase/firestore";

```

Then we're going to create a variable called `db` and set it equal to the `getFirestore()`. Finally, export `db` along with `auth` like this:

```
// Initialize Firebase Firestore
const db = getFirestore();
export { auth, db };

```

Now, let's create a file and name it `createUserDocument.js` inside the `firebase` folder. Then add this piece of code:

```
import { collection, doc, getDocs, query, serverTimestamp, setDoc, where } from "firebase/firestore";

import { db } from "./config";

export const createUserDocument = async (user) => {
  const q = query(collection(db, "users"), where("uid", "==", user.uid));
  const { docs } = await getDocs(q);

  if (docs.length === 0) {
    const { uid, displayName, email, photoURL, reloadUserInfo } = user;

    const docRef = doc(db, `users/${uid}`);
    await setDoc(docRef, {
      displayName,
      email,
      photoURL,
      username: reloadUserInfo.screenName,
      createdAt: serverTimestamp(),
    });
  }
};

```

I'm going to walk you through the above code. Don't worry—it's not scary! You'll understand it all in a jiffy.

First, we created an async function called `createUserDocument`. This function will be used to create new user documents in our database.

Next, we used the `query` method on the `db` to query the `users` collection with a `where` clause to find all documents with a `uid` equal to the provided user's uid.

Then we pass this query `q` to the `getDocs(q)` method. This method returns an array of `docs`.

And after that we added an if statement to check whether the docs array is empty or not. If it's empty, then we'll create a new docRef using the `doc` method that takes two arguments: `db` and the `document id`. This method returns a reference to that document.

Finally, we'll call the `setDoc` method that again takes two arguments: `docRef` and the user data that we want to save to the database.

Now, open your `useLogin.js` file and import the `createUserDocument` function:

```
import { createUserDocument } from "../firebase/createUserDocument";

```

And just above the dispatch statement, call the `createUserDocument` function like this:

```
const user = res.user;
await createUserDocument(user);
dispatch({ type: "LOGIN", payload: user });

```

Now, try to login again and it should save the new user to the Firestore.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/6KFqHkwMa.png)

🎉That's it! You have successfully implemented a great auth flow and now your app is ready to store user data when users sign up for the first time.

Now go and make your app amazing, and don't forget to let me know how it goes!

## 🙏 Thank you for reading this tutorial

Thank you for taking the time to read this guide!

I hope you enjoyed this tutorial and found it useful. If you have any questions or comments, please get in touch via [Twitter](https://twitter.com/thefierycoder) or [LinkedIn](https://www.linkedin.com/in/thefierycoder/)!

If you enjoyed this post, I would greatly appreciate it if you shared it on your favourite social media platform.

Please take a look around my [YouTube channel](https://www.youtube.com/c/TheFieryCoder) and subscribe if you like it.

Cheers, and see you in the next one! 🙏

Thank you for reading.

