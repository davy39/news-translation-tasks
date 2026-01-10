---
title: How to build cross-origin communication bridges in iOS and Android
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2018-08-01T18:15:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-cross-origin-communication-bridges-in-ios-and-andriod-7baef82b3f02
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aVKPXp6zfjMErb99NPZfKw.jpeg
tags:
- name: Android
  slug: android
- name: iOS
  slug: ios
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'I was working on a certain project at work, in which I needed to connect
  several varying components via messages. Each had its own logic and code language.
  This made me want to understand all the ways different platforms enable communication.

  This ar...'
---

I was working on a certain project at work, in which I needed to connect several varying components via messages. Each had its own logic and code language. This made me want to understand all the ways different platforms enable communication.

This article’s aim is to explain these cross-origin communication bridges and present simple, yet informative, examples to achieve them.

There will also be plenty of bridge puns ?

YOU WERE WARNED.

If you just want to get your hands dirty with the code, there are links to the GitHub repositories at the bottom of this article.

Typically, the JavaScript you write will run inside a browser. On **iOS**, it can either be a UIWebView or a WKWebView. On **Android**, a WebView.

Since iOS can be the more exasperating of the platforms, I’ll describe the communication bridge there first.

### London Bridge is Falling Down (iOS)

From iOS 8 onwards, Apple recommends using WKWebView instead of UIWebView, so the following will only address the bridge on a **WKWebView**.

For a UIWebView reference, please go [here](https://stackoverflow.com/questions/5671742/send-a-notification-from-javascript-in-uiwebview-to-objectivec).

To send messages from the WKWebView to JavaScript, you use the method below:

```android

- (void)evaluateJavaScript:(NSString *)javaScriptString 
         completionHandler:(void (^)(id, NSError *error))completionHandler;
```

To receive messages from JavaScript inside your WKWebView, you must do the following:

1. Create an instance of [WKWebViewConfiguration](https://developer.apple.com/documentation/webkit/wkwebview/1414979-configuration?language=objc)
2. Create an instance of [WKUserContentController](https://developer.apple.com/documentation/webkit/wkusercontentcontroller?language=objc)
3. Add a script message handler to your configuration (this part bridges the gap). This action also registers your message handler on the window object under the following path: **window.webkit.messageHandlers.MSG_HANDLER_NAME**
4. Make the class implement the message handler protocol by adding <WKScriptMessageHandler> at the top of the file
5. Implement [userContentController:didReceiveScriptMessage](https://developer.apple.com/documentation/webkit/wkscriptmessagehandler/1396222-usercontentcontroller?preferredLanguage=occ) (this method handles receiving the messages from JavaScript)

### Building Bridges

Let’s say we have the following HTML page set up:

```html
<html>
  
  <head>
    <title>Javascript-iOS Communication</title>
  </head>
  
  <body>
    
    <script>
      window.webkit.messageHandlers.myOwnJSHandler.postMessage("Hello World!");
    </script>
  </body>
  
  
</html>
```

And in our native code we implement the steps described above:

```android
#import <UIKit/UIKit.h>
#import <WebKit/WebKit.h>

// 4
@interface ViewController : UIViewController <WKScriptMessageHandler>

@property(nonatomic, strong) WKWebView *webview;


```

And violà! Now you have full JavaScript - iOS Communication!

![Image](https://cdn-media-1.freecodecamp.org/images/1*EosjstTDed_5cYeD7Fa-mQ.jpeg)
_Photo by [Unsplash](https://unsplash.com/photos/OHMg0Hgetn4?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Todd Diemer</a> on <a href="https://unsplash.com/search/photos/bridge?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Crossing The Bridge (Android)

Things are much simpler and more friendly here. In order to set up our communication bridge, there are only a few steps:

1. Create an instance of a [WebView](https://developer.android.com/reference/android/webkit/WebView) object
2. Enable JavaScript inside this WebView (**setJavaScriptEnabled**)
3. Set your own JavaScript Interface (which will hold methods that are visible to your JavaScript)
4. Any method that you want exposed to your JavaScript must have the **@JavascriptInterface** annotation before its declaration

Like before, let’s assume we have created this HTML file:

And we have created the following simple Android Application:

And there you go!

You can now consider yourself a Native Communication Ninja!

Here are the links to the repositories:

<a href="https://github.com/TomerPacific/MediumArticles/tree/master/AndroidtoJSNativeCommunicator">AndroidtoJS Repository</a>

<a href="https://github.com/TomerPacific/MediumArticles/tree/master/iOStoJSNativeCommunicator">iOStoJS Repository</a>

### ⚠️ Important Note Regarding iOS ⚠️

When you get to the point that you want to destroy your WKWebView, it is **imperative** that you remove your script message handler. If you do not do so, the script message handler will still hold a reference to your WKWebView and memory leaks will ensue upon creating new WKWebViews.

