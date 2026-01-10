---
title: How to develop a great Facebook login flow with Firebase and Ionic
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-05T22:09:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-develop-a-great-facebook-login-flow-with-firebase-and-ionic-656a295c4fe9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YftIGPfmk-Sok90hvhY05Q.png
tags:
- name: authentication
  slug: authentication
- name: Facebook
  slug: facebook
- name: Firebase
  slug: firebase
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ryan Gordon

  It’s helpful to use social sign-ins with Ionic for your users who would rather not
  create and remember another username:password combination. Instead, you can allow
  users to sign in with accounts they already own. You don’t need to sto...'
---

By Ryan Gordon

It’s helpful to use social sign-ins with Ionic for your users who would rather not create and remember another username:password combination. Instead, you can allow users to sign in with accounts they already own. You don’t need to store hashed passwords to compare, you don’t have to handle sending sign up emails, and you don’t need to reset passwords. The user’s chosen provider will handle all of this for you.

**Do you want just check out the code instead of following the post? Please give the [repo](https://github.com/Ryan-Gordon/Ionic-Firestarter) a star in you find it helpful!**

Some of this post will be very similar to the other tutorials on my page. If you have ionic and Node installed and have a project setup, you can jump to the code [here](#6156) .

To follow along with this tutorial, youll need both Node.js and Ionic installed.

To install ionic and cordova, which for the moment is needed for plugins, run the following in your terminal after installing Node:

```bash
npm install -g ionic cordova
```

If you get EACCES: permission denied, you may need to run the command with sudo.

![Image](https://cdn-media-1.freecodecamp.org/images/1*O7an59vwaCcUeF8YHm9frg.png)

Create an app with ionic start <appname> <template>. For this, use a blank template as a starting point.

The code for Facebook sign-in will be put into a provider class which will be called by whichever page needs to use that sign-in method.

```bash
ionic g provider auth
```

### Setup app with Firebase and get credentials

In order for Firebase to work with the Facebook platform, we will need to perform three steps:

— Setup a new App in the Facebook developer’s portal

— Setup Facebook sign-in on Firebase

— Implement the sign-in flow

#### Facebook Developer’s Portal

The Facebook Developers Portal is an interface to all of the developer tools and APIs available. It is what we’ll use to setup the sign-in API on Facebook’s side.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8GTVmvTMHbsN8-i0_BJp0w.png)

Choose a name and a contact email for your app. The contact email may be shown to users, so make sure it’s professional.

After this, the app will be created in facebook and we can add the plugin to our application!

There will be two plugins needed. The cordova plugin designed to work with Facebook natively, and a wrapper for it.

```bash
$ ionic plugin add cordova-plugin-facebook4 --variable APP_ID="123456789" --variable APP_NAME="myApplication"
```

You’ll need to replace the values or `APP_ID` and `APP_NAME` for your real credentials. You can find both of those inside your Facebook Developer’s Dashboard.

The other plugin will allow us to work with the first one, through TypeScript.

```bash
npm install --save @ionic-native/facebook 
```

Now we have the plugin installed and wired up to the Facebook console.

There are two final steps for this: selecting which platforms we will use on the FB Developer Portal and importing in the app.module.

#### Selecting Platforms in FB portal

Our app is created, however we need to specify which apps can use our sign-in API. This is done by adding platforms with a bundle ID we specify.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3apVFW4u2k0k_2piCMPA9w.png)

To begin click Add Platform, select either Android or iOS. Both platforms will need to know the generated ID of your app when it is in deployment.

The ID value found at the top of your config.xml will be used for both the Google Play store package name and the BundleID.

> Don’t forget to also import the plugin in your `_app.module.ts_` and specify it as a provider for the project.

### Setup Facebook sign-in on Firebase

Setting up the sign-in within Firebase will be the easiest task. Once the app is created on the FB developer’s portal, it will have an APPID and an APPSECRET. These two values are needed to link Firebase to our Facebook app.

![Image](https://cdn-media-1.freecodecamp.org/images/1*58Khs2B3iNFKDVWxsGwviA.png)

Once these values are input, click enable and that’s it!

### Implement the sign-in flow

After all of the configuration, we have made it to the fun part: coding the thing and testing it!

Provided you have been following, the two Facebook Ionic plugins are now installed and the app is setup in Firebase and FB Dev Portal.

Before we can use the plugin in our code, we must import it and bring it into scope with the constructor. After this we are free to use the plugin anywhere in this provider.

```ts
import { Facebook } from '@ionic-native/facebook';

@Injectable()

export class AuthProvider {
    
constructor(private googlePlus: GooglePlus, private facebook:Facebook) {
    
}
```

The code for the login itself will seem very familiar if you’ve seen the other posts. What we are doing here is using the native Facebook plugin to do a sign-in flow. If it’s succesful, take the provided authresponse and sign into Firebase.

This function can be called anywhere in the app by importing the auth provider. The intended way to use this will be that some page (such as `home.ts`) will have AuthProvider in scope. When the user clicks a FB login button, we will delegate the login to our AuthProvider.

Now when this function is called, a native Facebook UI will pop up asking for sign-in. Or if the user is already signed in it’ll just ask for OAuth permission — and thats it! We get a token back which we can use to make a credential, and this credential is then used to sign into Firebase.

```ts
facebookLogin(): Promise<any> {
    return this.facebook.login(['email'])
      .then( response => {
        const facebookCredential = firebase.auth.FacebookAuthProvider
          .credential(response.authResponse.accessToken);
  
        firebase.auth().signInWithCredential(facebookCredential)
          .then( success => { 
            console.log("Firebase success: " + JSON.stringify(success)); 
          });
  
      }).catch((error) => { console.log(error) });
  }
```

### Conclusion

In this article, we have setup the Facebook sign-in API and worked through a cross platform solution for signing users into our Firebase with Facebook.

Same as the Google Sign-In, there was some confirguration needed (although not as much). Now the benefit is that our users can sign into any web apps we build with their existing Facebook accounts. If you followed the first article too, then the app now has Google and Facebook sign-in!

All the code for this tutorial (and all my other tutorials) can be [found here](https://github.com/Ryan-Gordon/Ionic-Firestarter). I am aiming to implement as many of the Firebase features as I can, and YES I am looking for contributors!

If you want access to the code, here again is a link to the repo :

[**Ryan-Gordon/Ionic-Firestarter**](https://github.com/Ryan-Gordon/Ionic-Firestarter)  
[_Ionic-Firestarter — Ionic Firestarter is a open source project showcasing different Firebase features implemented in…_](https://github.com/Ryan-Gordon/Ionic-Firestarter)  
[github.com](https://github.com/Ryan-Gordon/Ionic-Firestarter)

Want some similar posts on Ionic ? Here is a couple other posts I’v done:

[**How to dynamically theme your Ionic application and make your users happy**  
_Designing a sleek color scheme for your mobile application can be time consuming. Why not let the user choose their own…_](https://www.freecodecamp.org/news/how-to-dynamically-theme-your-ionic-application-and-make-your-users-happy-ffa17e15dbf7/)  


[**Alternative Sign in Methods for Firebase with Ionic**](https://medium.com/@ryangordon210/alternative-sign-in-methods-for-firebase-with-ionic-52714ee9be83)  
[_In my other posts on Firebase sign ins, a focus has been put on Social providers. The main point of this emphasis is to…_](https://medium.com/@ryangordon210/alternative-sign-in-methods-for-firebase-with-ionic-52714ee9be83)

