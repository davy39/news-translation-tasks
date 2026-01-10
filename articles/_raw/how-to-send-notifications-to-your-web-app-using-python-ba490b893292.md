---
title: How to send notifications to your Web App using Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-08T21:54:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-send-notifications-to-your-web-app-using-python-ba490b893292
coverImage: https://cdn-media-1.freecodecamp.org/images/1*htDJgQOlkHDn7eF9WITh8Q.jpeg
tags:
- name: General Programming
  slug: programming
- name: progressive web app
  slug: progressive-web-app
- name: Python
  slug: python
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Lucas Hild

  Native apps have become hugely popular recently, mostly because of features such
  as working offline, transitions, easy distributability and of course push notifications.
  But unfortunately, you need a good knowledge of languages like Jav...'
---

By Lucas Hild

Native apps have become hugely popular recently, mostly because of features such as working offline, transitions, easy distributability and of course push notifications. But unfortunately, you need a good knowledge of languages like Java or Swift to create a valuable native app.

### Progressive Web Apps

Progressive Web Apps (PWAs) are JavaScript applications that run in the browser. They make the effort to bring some of the native app features to the web. PWAs are easy to develop if you have a fundamental knowledge of HTML, CSS, and in particular JavaScript. Moreover, if your service is already accessible for desktop devices on a website, it is easier to add the functionalities of a Web App, instead of developing a native mobile app.

### Notifications

Notifications keep users informed about new messages, tell them about a new blog post, and so on.

Many native apps send push notifications to the user. But this is also possible using PWAs and the Notifications API.

![Image](https://cdn-media-1.freecodecamp.org/images/H0tzewZI3D7d-DcwdysrJx3CpPTE2IcvEUeE)
_Photo by [Unsplash](https://unsplash.com/@jamie452?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Jamie Street</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### OneSignal

In this tutorial, we will be using [OneSingal](https://onesignal.com) to send notifications to our web app. OneSignal is a powerful tool that provides a simple interface to push notifications. They also provide a Rest API, which we will be using to send notifications.

### Setup OneSignal

To send push notifications, you need to setup OneSignal first. Therefor you need an account on OneSignal. Head over to [their website](https://onesignal.com) and press “Log in” in the upper right corner.

Next you will have to create an app. Give it a name and choose “Setup platform”. Here you select “All Browsers”. After that, you choose “custom code” as the integration. Then you have to provide some information about your website.

In the settings area of your app, there is a tab called “Keys & IDs”. Copy both keys for later.

![Image](https://cdn-media-1.freecodecamp.org/images/CZolsxSB91fV86I3nzpJL2qHSLEOfSyR0eWz)

**Important: Do not share you REST API Key. Keep it private!**

That’s it for setting up OneSignal. That was easy!

### Setup our website

In the next part, we will be adding the notification functionality to our website. The website will have to wait for notifications sent by OneSignal and display them to the user.

To let the browser know that you are creating a Progressive Web App, we will add a file called **manifest.json** to the root of our project.

```
{  "name": "My Application",  "short_name": "Application",  "start_url": ".",  "display": "standalone",  "background_color" : "#fff" ,  "description": "We send notifications to you",  "gcm_sender_id": "482941778795",  "gcm_sender_id_comment": "Do not change the GCM Sender ID"}
```

The first six key-value-pairs describe the appearance of the application. The **gcm_send_id** is important for sending notifications. If you want to know more about **manifest.json**, you can have a look in the [Mozilla Documentation](https://developer.mozilla.org/de/docs/Web/Manifest).

Your browser doesn’t automatically look for the manifest. You have to put the path to it in every HTML document in the _&_lt;h_e_ad> tag.

```
<head>    ...    <link rel="manifest" href="manifest.json">    ...</head>
```

Additionally, we need some JavaScript code to connect our website to OneSignal.

You can put the code for that in a script tag in the _&_lt;h_e_ad> part. Don’t forget to re**place my-**app-id with your own OneSignal app id.

```
<head>    <script src="https://cdn.onesignal.com/sdks/OneSignalSDK.js" async=""></script>        <script>        var OneSignal = window.OneSignal || [];        OneSignal.push(function () {            OneSignal.init({                appId: "my-app-id",                autoRegister: false,                notifyButton: {                    enable: true,                },            });        });    <script></head>
```

![Image](https://cdn-media-1.freecodecamp.org/images/rXjHpdqOUr9ahuanYkm9FlHip7ftX12pFV-n)
_Prompt the user to subscribe to your notifications_

When you want to prompt the user to subscribe to your notifications, you execute this piece of code.

```
OneSignal.push(function () {    OneSignal.showHttpPrompt();});
```

Moreover, you need a service worker, which listens in the background for notifications. Therefore, you need two files in the root directory of your project.

**OneSignalSDKUpdaterWorker.js**

```
importScripts('https://cdn.onesignal.com/sdks/OneSignalSDKWorker.js');
```

**OneSignalSDKWorker.js**

```
importScripts('https://cdn.onesignal.com/sdks/OneSignalSDKWorker.js');
```

### Access the API using Python

OneSignal has an easy-to-use Rest API. The endpoints are documented in the [OneSignal Developer Documentation](https://documentation.onesignal.com/docs).

![Image](https://cdn-media-1.freecodecamp.org/images/JonbuaZJXt9N2C-HIZzS-JR6gp1trvGEZ741)
_Photo by [Unsplash](https://unsplash.com/@maxcodes?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Max Nelson</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

To access it, we need to send HTTP requests. Therefore, we will use a library called [**requests**](http://docs.python-requests.org/en/master/). To install it, you can use pip, the package manager of Python.

```
pip install requests
```

This is the API endpoint we need to send a notification: [https://onesignal.com/api/v1/notifications](https://onesignal.com/api/v1/notifications).

The HTTP protocol has several methods. In this case, we want to make a POST request. To do so, we need to import requests and execute a function.

```
import requests
```

```
requests.post("https://onesignal.com/api/v1/notifications")
```

OneSignal wants to verify that only you can send notifications to your website. So you have to add an HTTP header with your Rest API Key from OneSignal.

```
requests.post(    "https://onesignal.com/api/v1/notifications",    headers={"Authorization": "Basic my-rest-api-key"})
```

Remember to replace **my-rest-api-key** with your Rest API Key.

Moreover, you need some basic information about your notification.

```
data = {    "app_id": "my-app-id",    "included_segments": ["All"],    "contents": {"en": "Hello"}}
```

```
requests.post(    "https://onesignal.com/api/v1/notifications",    headers={"Authorization": "Basic my-rest-api-key"},    json=data)
```

Replace **my-app-id** with your own app id. Next you choose who will receive your notifications. Example values are `"All", "Active Users", "Inactive Users”`. But you can also create your own segments. And for the last one, you add some content of the message in English. If you need another language, you can add it here too.

**That’s it! If you subscribed to the notifications, you should get a push notification.**

![Image](https://cdn-media-1.freecodecamp.org/images/Z6q3cFDErQJTIstdDh8lc93gBpRgtvLxJmTs)

### Send notifications using an API Wrapper

Because my code became kind of messy with many different notifications, I [created an API wrapper for OneSignal](https://github.com/Lanseuo/onesignal-notifications).

#### API Wrapper

But what is an API wrapper? An API wrapper makes it easier for you to access an API. You can say that it is an API for an API. You call the API wrapper instead of the API directly.

You can install the wrapper called **OneSignal-Notifications** from pip.

```
pip install onesignal-notifications
```

Now you can import it and setup your client.

```
from onesignal import OneSignal, SegmentNotificationclient = OneSignal("MY_APP_ID", "MY_REST_API_KEY")
```

To send a Notification, you have to initialize the class **SegmentNotification** and use the method **send**.

```
notification_to_all_users = SegmentNotification(    {        "en": "Hello from OneSignal-Notifications"    },    included_segments=SegmentNotification.ALL)client.send(notification_to_all_users)
```

Maybe this looks kind of unnecessary to you, because it takes even more lines of code. But if you have several notifications, it makes the process much easier and your code more beautiful.

For example if you want to send a notification, which is based on some conditions, the API wrapper has a custom class for that.

```
from onesignal import OneSignal, FilterNotification, Filterclient = OneSignal("MY_APP_ID", "MY_REST_API_KEY")
```

```
filter_notification = FilterNotification(    {        "en": "Hello from OneSignal-Notifications"    },    filters=[        Filter.Tag("my_key", "<", "5"),        "AND",        Filter.AppVersion(">", "5"),        "OR",        Filter.LastSession(">", "1"),    ])
```

There are many custom parameters you can provide to adapt your notification. For example, you can add buttons to the notification. All list of all parameters can be found [here](https://lanseuo.github.io/onesignal-notifications/guide/send-notification.html#common-parameters).

```
from onesignal import OneSignal, FilterNotification, Filterclient = OneSignal("MY_APP_ID", "MY_REST_API_KEY")
```

```
filter_notification = SegmentNotification(    {        "en": "Hello from OneSignal-Notifications"    },    web_buttons=[        {          "id": "like-button",          "text": "Like",          "icon": "http://i.imgur.com/N8SN8ZS.png",          "url": "https://github.com/Lanseuo/onesignal-notifications"}    ],    included_segments=SegmentNotification.ALL)
```

If you want to find out more about **OneSignal-Notifications**, you can have a look in the [GitHub Repository](https://github.com/Lanseuo/onesignal-notifications) or in the [docs](https://lanseuo.github.io/onesignal-notifications).

