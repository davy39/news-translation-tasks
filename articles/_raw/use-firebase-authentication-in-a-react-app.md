---
title: How to Use Firebase Authentication in a React App
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2022-10-31T14:54:20.000Z'
originalURL: https://freecodecamp.org/news/use-firebase-authentication-in-a-react-app
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/ferenc-almasi-tvHtIGbbjMo-unsplash.jpg
tags:
- name: authentication
  slug: authentication
- name: Firebase
  slug: firebase
- name: React
  slug: react
seo_title: null
seo_desc: "Almost every web application requires some form of authentication. This\
  \ prevents unauthorized users from having access to the app's inner workings. \n\
  In this tutorial, you will learn how to authenticate your React app with the Firebase\
  \ SDK.\nHow to Aut..."
---

Almost every web application requires some form of authentication. This prevents unauthorized users from having access to the app's inner workings. 

In this tutorial, you will learn how to authenticate your React app with the Firebase SDK.

## How to Authenticate with Firebase

Authenticating with Firebase makes things easy for both end users and developers. Firebase Authentication provides backend services, easy-to-use SDKs, and ready-made UI libraries. This allows you to focus on your users, not complex infrastructure to support them. 

Firebase supports a lot of ways for users to get authenticated. They include authentication through email addresses, third-party providers such as Twitter, Facebook, Github, Google, Microsoft, and much more.

## How to Set Up Firebase Authentication

Before you set up and initialize the Firebase SDK for your React app, you'll need to sign up for Firebase using your Google account. 

If you have a Firebase account already, sign in and follow the prompts to create a new project. Pick a suitable name for your project and click **Continue.**

For this tutorial, we will name our project **Focus-app.** Your next screen will be a prompt to enable Google Analytics. We won’t be needing it. You can choose to turn it off.

Congratulations, you have successfully set up your Firebase Console. Your next screen will be the Firebase console dashboard which will look like this:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot--197-.png)

There are a lot of ways to authenticate users using Firebase. For this tutorial, we will authenticate our users with their email addresses and passwords. 

To start using the Firebase SDK Authentication, select the Authentication SDK among the **Build** categories. 

Next, we will set up our sign-in method. Click on **Set up sign-in method** and select **Email/Password** from the list of sign-in providers.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Screenshot--209--3.png)

Enable the **Email/Password** option to let users sign up using their email address and password and click on **Save**.

## How to Set Up Your React App with React Router

Authentication is a feature that most apps need. We will set up our React app by using the following command:

```js
$ npx create-react-app focus-app
```

Before we start our app, we should set up our react-router-dom. You can install your **react-router-dom** by running the following command:

```js
$ npm i -D react-router-dom
```

To set up your React app to use **react-router-dom**, you can read their [docs](https://reactrouter.com/en/6.4.2/start/tutorial). After setting up your routes, your app.js file should have the following code:

```js
import React, {useState, useEffect} from 'react';
import Home from './page/Home';
import Signup from './page/Signup';
import Login from './page/Login';
import { BrowserRouter as Router} from 'react-router-dom';
import {Routes, Route} from 'react-router-dom';
 
function App() {
 
  return (
    <Router>
      <div>
        <section>                              
            <Routes>                                                                        <Route path="/" element={<Home/>}/>
               <Route path="/signup" element={<Signup/>}/>
               <Route path="/login" element={<Login/>}/>
            </Routes>                    
        </section>
      </div>
    </Router>
  );
}
 
export default App;
```

We set up our React app to have three routes: **Home**, **Login**, and the **Signup** page.

## How to Set Up and Configure Firebase SDK

You have two options to set up your Firebase SDK. We will be installing and setting up Firebase using the **npm** option. 

Before installing the Firebase SDK, you should have [npm](https://nodejs.org/en/download/) installed on your machine. You can install the latest Firebase SDK by running the following command:

```js
$ npm install firebase
```

To initialize Firebase, create a **firebase.js** file in your **src** directory. Get your Firebase configuration in the project settings part of your dashboard and copy your Firebase configuration into your **firebase.js** file. Your **firebase.js** file should have the following code:

```js
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
// Your web app's Firebase configuration

const firebaseConfig = {
  apiKey: "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  authDomain: "XXXXXXXXXXXXXXXXXXXXXXXX",
  projectId: "XXXXXXXXX",
  storageBucket: "XXXXXXXXXXXXXXXXXX",
  messagingSenderId: "XXXXXXXXXXXX",
  appId: "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

```

Congratulations, you have successfully initialized Firebase. 

To start using the Firebase SDK, you will have to import the products you'd like to use. After importing the Firebase SDK for authentication, your **firebase.js** file should have the following code:

```js
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries
// Your web app's Firebase configuration

const firebaseConfig = {
  apiKey: "AIzaSyAAx_knJ_qqxPkJQ_xoIZnxt_c6gb6Wdys",
  authDomain: "todoapp-eeeb7.firebaseapp.com",
  projectId: "todoapp-eeeb7",
  storageBucket: "todoapp-eeeb7.appspot.com",
  messagingSenderId: "1072574112522",
  appId: "1:1072574112522:web:65fc4e184aed9894dc90f3"
};
 
// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Initialize Firebase Authentication and get a reference to the service
export const auth = getAuth(app);
export default app;
```

## How to Authenticate Your React App

Firebase has a number of built-in products, one of which is authentication. According to its [docs](https://firebase.google.com/docs/auth), 

> to authenticate users to your app, Firebase Authentication provides cool features like backend services, easy-to-use SDKs, and ready-made UI libraries. 

Firebase Authentication allows users to sign in to your app using different sign-in methods. In this tutorial, we will learn how to authenticate users using email and passwords to sign in to your app. We won’t be using any styling for this article.

To create a user, you should create a form that takes inputs and create new users using the **createUserWithEmailAndPassword** method from Firebase. 

The form should take the new user's email address and password as input and pass them into the **createUserWithEmailAndPassword** method. If a user is successfully created, you will be routed to the login screen. 

Here is the complete code to create a user:

```js
import React, {useState} from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import {  createUserWithEmailAndPassword  } from 'firebase/auth';
import { auth } from '../firebase';
 
const Signup = () => {
    const navigate = useNavigate();
 
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('');
 
    const onSubmit = async (e) => {
      e.preventDefault()
     
      await createUserWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            // Signed in
            const user = userCredential.user;
            console.log(user);
            navigate("/login")
            // ...
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            console.log(errorCode, errorMessage);
            // ..
        });
 
   
    }
 
  return (
    <main >        
        <section>
            <div>
                <div>                  
                    <h1> FocusApp </h1>                                                                            
                    <form>                                                                                            
                        <div>
                            <label htmlFor="email-address">
                                Email address
                            </label>
                            <input
                                type="email"
                                label="Email address"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}  
                                required                                    
                                placeholder="Email address"                                
                            />
                        </div>

                        <div>
                            <label htmlFor="password">
                                Password
                            </label>
                            <input
                                type="password"
                                label="Create password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)} 
                                required                                 
                                placeholder="Password"              
                            />
                        </div>                                             
                        
                        <button
                            type="submit" 
                            onClick={onSubmit}                        
                        >  
                            Sign up                                
                        </button>
                                                                     
                    </form>
                   
                    <p>
                        Already have an account?{' '}
                        <NavLink to="/login" >
                            Sign in
                        </NavLink>
                    </p>                   
                </div>
            </div>
        </section>
    </main>
  )
}
 
export default Signup

```

Firebase allows existing users to sign in using the **email** and **password** that they initially used for signup. 

To allow existing users to sign in, you should create a form that collects both their email and password. The form has a submit button that calls the **signInWithEmailAndPassword** method whenever it is clicked. 

You can sign in using the following code:

```js
import React, {useState} from 'react';
import {  signInWithEmailAndPassword   } from 'firebase/auth';
import { auth } from '../firebase';
import { NavLink, useNavigate } from 'react-router-dom'
 
const Login = () => {
    const navigate = useNavigate();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
       
    const onLogin = (e) => {
        e.preventDefault();
        signInWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            // Signed in
            const user = userCredential.user;
            navigate("/home")
            console.log(user);
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            console.log(errorCode, errorMessage)
        });
       
    }
 
    return(
        <>
            <main >        
                <section>
                    <div>                                            
                        <p> FocusApp </p>                       
                                                       
                        <form>                                              
                            <div>
                                <label htmlFor="email-address">
                                    Email address
                                </label>
                                <input
                                    id="email-address"
                                    name="email"
                                    type="email"                                    
                                    required                                                                                
                                    placeholder="Email address"
                                    onChange={(e)=>setEmail(e.target.value)}
                                />
                            </div>

                            <div>
                                <label htmlFor="password">
                                    Password
                                </label>
                                <input
                                    id="password"
                                    name="password"
                                    type="password"                                    
                                    required                                                                                
                                    placeholder="Password"
                                    onChange={(e)=>setPassword(e.target.value)}
                                />
                            </div>
                                                
                            <div>
                                <button                                    
                                    onClick={onLogin}                                        
                                >      
                                    Login                                                                  
                                </button>
                            </div>                               
                        </form>
                       
                        <p className="text-sm text-white text-center">
                            No account yet? {' '}
                            <NavLink to="/signup">
                                Sign up
                            </NavLink>
                        </p>
                                                   
                    </div>
                </section>
            </main>
        </>
    )
}
 
export default Login
```

Firebase Authentication provides other sign-in methods, including using GitHub, Microsoft, Apple, or a federated identity provider, such as [Google Sign-In](https://firebase.google.com/docs/auth/web/google-signin) or [Facebook Login](https://firebase.google.com/docs/auth/web/facebook-login). 

After a successful sign-in, a user’s information can be accessed and can be used to add more features to your app, including protecting your routes.

To get a currently signed-up user, we set an observer on the Auth object. We can get a currently signed user using the following code in the **Home** component:

```js
import React, { useState, useEffect } from 'react';
import { onAuthStateChanged } from "firebase/auth";
import { auth } from '../firebase';
 
const Home = () => {
 
    useEffect(()=>{
        onAuthStateChanged(auth, (user) => {
            if (user) {
              // User is signed in, see docs for a list of available properties
              // https://firebase.google.com/docs/reference/js/firebase.User
              const uid = user.uid;
              // ...
              console.log("uid", uid)
            } else {
              // User is signed out
              // ...
              console.log("user is logged out")
            }
          });
         
    }, [])
 
  return (
    <section>        
      …
    </section>
  )
}
 
export default Home
 

```

To complete our Firebase authentication, after creating a user and signing in, there should be a way to sign out users. 

To sign out a user, the **signOut** method is called from Firebase. After signing in to the **Home** route, there will be a button to sign out whenever the **Logout** button is clicked. The button should have an **onClick** event that calls the **signOut** method from Firebase auth. A success message will be displayed on the console if the sign out is successful. 

Here is the complete code to sign out a user:

```js
import React from 'react';
import {  signOut } from "firebase/auth";
import {auth} from '../../firebase';
import { useNavigate } from 'react-router-dom';
 
const Home = () => {
    const navigate = useNavigate();
 
    const handleLogout = () => {               
        signOut(auth).then(() => {
        // Sign-out successful.
            navigate("/");
            console.log("Signed out successfully")
        }).catch((error) => {
        // An error happened.
        });
    }
   
    return(
        <>
            <nav>
                <p>
                    Welcome Home
                </p>
 
                <div>
        			<button onClick={handleLogout}>
                        Logout
                    </button>
        		</div>
            </nav>
        </>
    )
}
 
export default Home;

```

## Conclusion

Firebase authentication allows you to create the identity of a user. It authenticates users seamlessly. 

Through this article, I hope you have got enough knowledge to build applications that authenticate users. You can check the [documentation](https://firebase.google.com/docs/auth) to learn more.

Here is a [link](https://github.com/IsraelChidera/focus-app) to the GitHub repository that uses Firebase authentication. It also uses **TailwindCSS** for styling and **React Router** for routing.

Happy Coding!

  

