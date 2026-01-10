---
title: How to Develop Particle IoT Apps Using NativeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T17:42:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-develop-particle-iot-apps-using-nativescript
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/NativeScript---Particle.png
tags:
- name: iot
  slug: iot
- name: mobile
  slug: mobile
- name: NativeScript
  slug: nativescript
- name: particle
  slug: particle
seo_title: null
seo_desc: 'By Jared Wolff

  If you''re developing any type of IoT product, inevitably you''ll need some type
  of mobile app. While there are easy ways, they''re not for production use.

  In this tutorial, we''ll talk about the basics of Particle app development. You''ll
  ...'
---

By Jared Wolff

If you're developing any type of IoT product, inevitably you'll need some type of mobile app. While [there are easy ways](https://www.jaredwolff.com/create-a-cross-platform-app-using-blynk/), they're not for production use.

In this tutorial, we'll talk about the basics of Particle app development. You'll learn about some of the many app frameworks you can take advantage of. Plus there's libraries, tricks, and tools along the way to make your life a lot easier.

## App Frameworks

Sometimes it's dang near irritating to program multiple applications natively. You see, Swift (or Objective C ?) and Java aren't terrible at first glance (well, maybe except for Obj-C ?). But when you're resource constrained, you have to figure out a new game plan. That's where App Frameworks come in.

These frameworks allow an app developer to write, build and test cross platform apps. In some cases, the frameworks convert your app into native code. That means that they run as fast and as well as one written in Swift or Java.

I did the research and as of January 2020, here are some of the most supported frameworks:

* [Framework7](https://github.com/framework7io/framework7)
* [Flutter](https://flutter.dev/)
* [NativeScript](https://www.nativescript.org/)
* [ReactNative](https://github.com/facebook/react-native)
* [Ionic](https://github.com/ionic-team/ionic)
* [Cordova](https://cordova.apache.org/) / [PhoneGap](https://phonegap.com/)
* [Meteor](https://github.com/meteor/meteor)
* [Xamarin](https://dotnet.microsoft.com/apps/xamarin)

The list goes on for days.

I've used a few of these frameworks in the past. I've built a Meteor app which (surprisingly) worked. In the end I had to pick one though. What did I go with?

**NativeScript.**

For the most part, NativeScript's documentation and on-boarding experience is fantastic. Not only can you preview your app inside an emulator but you can load it directly to your phone too!

![images/Apple_iPhone_6s_Gold_-__status-b1ad9325-8e81-4ee0-b72a-687b62adec29.png](https://www.jaredwolff.com/how-to-develop-particle-iot-apps-using-nativescript/images/Apple_iPhone_6s_Gold_-__status-b1ad9325-8e81-4ee0-b72a-687b62adec29.png)

One of the cool things about NativeScript is that it supports TypeScript. TypeScript is a superset of JavaScript with some extra wiz-bang features. 

Unlike other languages, JavaScript technically has no types. If you've done any Particle development you likely know what a type is. We're talking about `int`, `String`, `float` and more. i.e. they're directives to to make sure your JavaScript code stays consistent.

NativeScript is also compatible with most major JavaScript web frameworks. This includes [Vue.Js](https://vuejs.org/) and [Angular](https://angular.io/).

I've only noticed one major drawback thus far: the mobile preview mode (`tns preview` command) does not pay well with native libraries. If you have some native platform specific libraries, you'll have to use the emulator or a device (if you have one).

If you're gung-ho and you _want_ to build multiple apps in their respective languages, the more power to you. There is an advantage over the above frameworks: tried and true Particle SDKs.

## Available Libraries & SDKs

Particle has gone out of their way to make app development a little easier. This is thanks to the massive development work that has gone into their own SDKs. Yup, gone are the days you have to write manual HTTP request handlers.

Here's a link to both the iOS and Android SDKs:

* [iOS](https://docs.particle.io/reference/SDKs/ios/)
* [Android](https://docs.particle.io/reference/SDKs/android/)

Though we won't be covering them here, they reflect all the potential calls that you can make using the [Cloud API.](https://docs.particle.io/reference/device-cloud/api/)

Speaking of Cloud API, Particle has also developed a [Node.js](https://docs.particle.io/reference/device-cloud/api/) library as well. As you can imagine, you can use this for your server side code or JavaScript based app frameworks. Sadly, it doesn't work with NativeScript. Frameworks that use a [WebView](https://www.tutorialspoint.com/android/android_webview_layout.htm) should be more compatible.

In the case of this tutorial, we'll be mostly focusing on the Cloud API. This way you have a good understanding of the overall system. It may seem intimidating but if you do it right, you'll get the hang of it real fast.

## Making API Calls

In NativeScript you can't use libraries like `[request](https://github.com/request/request)`. (Which happens to be the library Particle's very own [DMC](https://github.com/dmiddlecamp) used in the [CLI](https://github.com/particle-iot/particle-cli) — DMC if you're reading this, Hi!) You'll have to use the provided [HTTP](https://docs.nativescript.org/ns-framework-modules/http) module. 

If you scroll all the way to the [bottom of that page](https://docs.nativescript.org/ns-framework-modules/http#http-post), you'll see a fully fledged `POST` example. I'll reproduce it here but with some Particle specific changes:

```typescript
// Create form post data
var data = new FormData();
data.append("name", "update");
data.append("data", "It's hammer time!");
data.append("private", "true");
data.append("access_token", _token);

// Configure the httpModule
return httpModule
    .request({
        url: `https://api.particle.io/v1/devices/events`,
        method: "POST",
        content: data
    })
    .then(
        response => {
            const result = response.content.toJSON();
            console.log(result);
        },
        e => {
            if (e) console.log(e);
        }
    );

```

The above is an example of what's equivalent to `Particle.publish` in DeviceOS. Let's break down the parts.

First of all, one of the main gotchas of Particle's Web API is the data format. I first expected that they use JSON but I was sorely wrong. After actually _reading_ the documentation I realized that most POST requests were actually `application/x-www-form-urlencoded`. That means when you submit data, it's the equivalent to hitting the submit button on an HTML form.

Fortunately, there is an easy way to assemble form data in Node/JavaScript. We can use the `FormData()` object. Take a look at the above. There should be some familiar parameter names in the `data.append` calls.

`"name"` refers to the name of the event you're publishing to.

`"data"` refers to the string formatted data that you're publishing.

`"private"` dictates whether or not you want to broadcast this data to the whole Particle world, or just your little corner of it.

`"access_token"` is a token that you can generate in order to make these API calls. Without a token though, you're dead in the water.

### Getting a Token

Where do we get this elusive `access_token`?

At first I had no idea.

I created an OAuth user and secret in the console. That lead to a dead end. Fiddled around with different API calls and settings. Nothing. Then it hit me like a ton of bricks. There's an `access_token` attached to the curl request on every device page!

Open up any device, click the little console button near _Events._ A popup with instructions an a URL will pop up. Copy the text after `access_token=`. That is your `access_token`! See below:

![images/Screen_Shot_2020-01-25_at_8.55.21_AM.png](https://www.jaredwolff.com/how-to-develop-particle-iot-apps-using-nativescript/images/Screen_Shot_2020-01-25_at_8.55.21_AM.png)

You can use this token to make calls to the Particle API. This can be to subscribe, publish, write to a function, read variables and more.

### Through the command line

That's nice and everything but how the heck can you _programmatically_ generate one? One way is with the command line.

`particle token create` is the name of the command you need to know about. When you run it, you'll be prompted to login. (Also enter your Authenticator code if you use one.) Then the command line will spit out a shiny new `access_token` you can use with the API!

### Through the API itself

If you couldn't guess, `particle token create` is a [frontend to a raw API call](https://github.com/particle-iot/particle-cli/blob/20d02afc7b72ade0e79d4f4ec724ec6cce9fff1b/src/lib/api-client.js#L192). You can make these API calls directly too. Here's what it looks like in NativeScript.

```typescript
// Create form post data
var data = new FormData();
data.append("username", "jaredwolff");
data.append("password", "this is not my password");
data.append("grant_type", "password");
data.append("client_name", "user");
data.append("client_secret", "client_secret_here");

// Configure the httpModule
return httpModule
    .request({
        url: `https://api.particle.io/v1/oauth/token`,
        method: "POST",
        content: data
    })
    .then(
        response => {
            const result = response.content.toJSON();
            console.log(result);
        },
        e => {
            if (e) console.log(e);
        }
    );

```

This call _may_ get more complicated. Mostly in the case if you have two factor authorization setup. It's well worth it when you figure it all out. After all, no one wants to manually create auth tokens if they don't have to!

Now you're ready to write and read from your devices. There's one thing though that may trip you up. Subscribing to events can be troublesome with a regular HTTP client. So much so that if you try to do it with NativeScript's HTTP client, it will lock up and never return. Luckily there is a way to handle these special HTTP calls.

## Server Sent What?

Server Sent Events (SSE for short) is an HTTP/S subscription functionality. It allows you to connect to a SSE end point and continuously listen for updates. It's a similar web technology to what companies use for push notifications. It does require some extra functionality under the hood though...

### SSE Library

After much head scratching and searching I stumbled upon `nativescript-sse`. It looked simple enough that I could start using immediately. More problems arose when I tried to use it though.

First, it turns out you can't use the library in `tns preview` mode. The alternative is to use `tns run ios --emulator` or use `tns run ios` with your iPhone connected to your computer. The non-emulator command will automatically deliver your prototype app.

**Side note:** I had already set up my phone in Xcode. You may have to do this yourself before `tns run ios` is able to find and deploy to your phone.

Secondly, once I got the library working, I noticed I would get some very nasty errors. The errors seemed to happen whenever a new message from Particle came along. 

Turns out the underlying Swift library for iOS [had fixed this last year.](https://github.com/inaka/EventSource/issues/89) So I took it upon myself to figure out how to upgrade the NativeScript plugin. I'll save you the time to say that it can be a pain and there is a learning curve!

Fortunately after some hacking I got something working. More instructions on how to compile the plugin are in the [README](https://github.com/jaredwolff/nativescript-sse). Alternatively, you can download a pre-built one on the [Release page of the repository.](https://github.com/jaredwolff/nativescript-sse/releases/tag/v4.0.3)

Download the `.tgz` file to wherever you like. Then, you can add it using `tns plugin add`. The full command looks like this:

```
tns plugin add path/to/plugin/file.tgz

```

You can check to make sure the library is installed by running `tns plugin list`

```
**jaredwolff$ tns plugin list
Dependencies:
┌─────────────────────┬──────────────────────────────────────────────────────────────────────────────────┐
│ Plugin              │ Version                                                                          │
│ @nativescript/theme │ ~2.2.1                                                                           │
│ nativescript-sse    │ file:../../Downloads/nativescript-sse/publish/package/nativescript-sse-4.0.3.tgz │
│ tns-core-modules    │ ~6.3.0                                                                           │
└─────────────────────┴──────────────────────────────────────────────────────────────────────────────────┘
Dev Dependencies:
┌──────────────────────────┬─────────┐
│ Plugin                   │ Version │
│ nativescript-dev-webpack │ ~1.4.0  │
│ typescript               │ ~3.5.3  │
└──────────────────────────┴─────────┘
NOTE:
If you want to check the dependencies of installed plugin use npm view <pluginName> grep dependencies
If you want to check the dev dependencies of installed plugin use npm view <pluginName> grep devDependencies**

```

Once installed, invoking the library takes a few steps. Here's an example:

```typescript
import { SSE } from "nativescript-sse";

sse = new SSE(
            "https://api.particle.io/v1/events/blob?access_token=<your access token>",
            {}

// Add event listener
sse.addEventListener("blob");

// Add callback
sse.events.on("onMessage", data=>{
	// TODO: do stuff with your event data here!
	console.log(data);
});

// Connect if not already
sse.connect();

```

First you need to import and create an instance of the library. When you create the instance, you will have to enter the URL that you want to use. 

In this case we'll be doing the equivalent of `Particle.subscribe()`. It should look something similar to the above: `https://api.particle.io/v1/events/<your event name>?access_token=<your access token>`. 

Replace `<your event name>` and `<your access token>` with the name of your event and your freshly created token!

Then you set up the library to listen for the event you care about. In this case `blob` is the event I most care about.

Then make sure you configure a callback! That way you can get access to the data when `blob` does come along. I've made a `TODO` note where you can access said data.

Finally, you can connect using the `.connect()` method. If you don't connect, SSE will not open a session and you'll get no data from Particle.

Placement of the code is up to you but from the examples it looks like within the `constructor()` of your model is a good place.([https://github.com/jaredwolff/nativescript-sse/blob/master/demo/app/main-view-model.ts](https://github.com/jaredwolff/nativescript-sse/blob/master/demo/app/main-view-model.ts))

### Other Examples

If you're curious how to use SSE in other places I have another great example: Particle's CLI.

Particle uses the `[request](https://github.com/request/request)` library to handle SSE events in the app. Whenever you call `particle subscribe blob` it invokes a `getStreamEvent` further inside the code.  You can [check it out here.](https://github.com/particle-iot/particle-cli/blob/master/src/lib/api-client.js#L862) The `request` library has more information on streaming [here](https://github.com/request/request#streaming).

## More resources

This is but the tip of the iceberg when it comes to connecting with Particle's API. Particle has some great documentation (as always) you can check out. Here are some important links:

* [API documentation](https://docs.particle.io/reference/device-cloud/api/)
* [Javascript SDK](https://docs.particle.io/reference/SDKs/javascript/)
* [iOS SDK](https://docs.particle.io/reference/SDKs/ios/)
* [Android SDK](https://docs.particle.io/reference/SDKs/android/)

## Conclusion

In this post we've talked about app frameworks, NativeScript, NativeScript plugins and Server Sent Events. Plus all the Particle related things so you can connect your NativeScript app to Particle's API. 

I hope you've found this quick tutorial useful. If you have any questions feel free to leave a comment or [send me a message](https://www.jaredwolff.com/contact/). Also be sure to check out my [newly released guide](https://www.jaredwolff.com/the-ultimate-guide-to-particle-mesh/). It has content just like this all about Particle's ecosystem.

Until next time!

**This post was originally from** [**https://www.jaredwolff.com/how-to-develop-particle-iot-apps-using-nativescript/**](https://www.jaredwolff.com/how-to-develop-particle-iot-apps-using-nativescript/)

