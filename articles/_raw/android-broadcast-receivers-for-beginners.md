---
title: Android Broadcast Receivers for Beginners
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2019-06-13T21:59:00.000Z'
originalURL: https://freecodecamp.org/news/android-broadcast-receivers-for-beginners
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca208740569d1a4ca521a.jpg
tags:
- name: android app development
  slug: android-app-development
- name: Java
  slug: java
- name: mobile app development
  slug: mobile-app-development
seo_title: null
seo_desc: 'Let’s say you have an application that depends on a steady internet connection.
  You want your application to get notified when the internet connection changes.
  How do you do that?

  A possible solution would be a service which always checks the interne...'
---

Let’s say you have an application that depends on a steady internet connection. You want your application to get notified when the internet connection changes. How do you do that?

A possible solution would be a service which always checks the internet connection. This implementation is bad for various reasons so we won’t even consider it. The solution to this problem is a Broadcast Receiver and it will listen in on changes you tell it to. 

A broadcast receiver will always get notified of a broadcast, regardless of the status of your application. It doesn’t matter if your application is currently running, in the background or not running at all.

## Background

Broadcast receivers are components in your Android application that listen in on broadcast messages(or events) from different outlets:

* From other applications
* From the system itself
* From your application

Meaning, that they are invoked when a certain action has occurred that they have been programmed to listen to (I.E., a broadcast).

A broadcast is simply a message wrapped inside of an Intent object. A broadcast can either be implicit or explicit.

* An **_implicit broadcast_** is one that does not target your application specifically so it is not exclusive to your application. To register for one, you need to use an [IntentFilter](https://developer.android.com/reference/android/content/IntentFilter) and declare it in your manifest. You need to do all of this because the Android operating system goes over all the declared intent filters in your manifest and sees if there is a match. Because of this behavior, implicit broadcasts do not have a target attribute. An example for an implicit broadcast would be an action of an incoming SMS message.
* An **_explicit broadcast_** is one that is targeted specifically for your application on a component that is known in advance. This happens due to the target attribute that contains the application’s package name or a component class name.

There are two ways to declare a receiver:

1. By declaring one in your AndroidManifest.xml file with the <receiver> tag (also called static)

```xml
<receiver android:name=".YourBrodcastReceiverClass"  android:exported="true">
    <intent-filter>
        <!-- The actions you wish to listen to, below is an example -->
        <action android:name="android.intent.action.BOOT_COMPLETED"/>
    </intent-filter>
</receiver>
```

You will notice that the broadcast receiver declared above has a property of **_exported=”true”_**. This attribute tells the receiver that it can receive broadcasts from outside the scope of the application.

2. Or dynamically by registering an instance with registerReceiver (what is known as context registered)

## How to Implement a Broadcast Receiver in Android

To create your own broadcast receiver, you must first extend the BroadcastReceiver parent class and override the mandatory method, onReceive:

```java
 public void onReceive(Context context, Intent intent) {
    //Implement your logic here
 }
```

Putting it all together yields:

```java
public class MyBroadcastReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        StringBuilder sb = new StringBuilder();
        sb.append("Action: " + intent.getAction() + "\n");
        sb.append("URI: " + intent.toUri(Intent.URI_INTENT_SCHEME).toString() + "\n");
        String log = sb.toString();
        Toast.makeText(context, log, Toast.LENGTH_LONG).show();

    }
}
```

⚠️ The onReceive method runs on the main thread, and because of this, its execution should be brief.

If a long process is executed, the system may kill the process after the method returns. To circumvent this, consider using [goAsync](https://developer.android.com/reference/android/content/BroadcastReceiver.html#goAsync()) or scheduling a job. You can read more about scheduling a job at the bottom of this article.

## Dynamic Registration Example

To register a receiver with a context, you first need to instantiate an instance of your broadcast receiver:

```java
BroadcastReceiver myBroadcastReceiver = new MyBroadcastReceiver();

```

Then, you can register it depending on the specific context you wish:

```java
IntentFilter filter = new IntentFilter(ConnectivityManager.CONNECTIVITY_ACTION);
filter.addAction(Intent.ACTION_AIRPLANE_MODE_CHANGED);
this.registerReceiver(myBroadcastReceiver, filter);

```

Don’t forget to unregister your broadcast receiver when you no longer need it:

```java
@Override
protected void onStop() {
  super.onStop();
  unregisterReceiver(myBroadcastReceiver);
}
```

## How to Broadcasting An Event in Android

The point behind broadcasting messages from your application is to allow your application to respond to events as they happen inside of it. 

Think of a scenario where in one part of the code, the user performs a certain action and because of it, you want to execute some other logic you have in a different place.

There are three ways to send broadcasts:

1. The [**_sendOrderedBroadcast_**](https://developer.android.com/reference/android/content/Context.html#sendOrderedBroadcast(android.content.Intent,%20java.lang.String)) method, makes sure to send broadcasts to only one receiver at a time. Each broadcast can in turn, pass along data to the one following it, or to stop the propagation of the broadcast to the receivers that follow
2. The [**_sendBroadcast_**](https://developer.android.com/reference/android/content/Context.html#sendBroadcast(android.content.Intent)) is similar to the method mentioned above, with one difference. All broadcast receivers receive the message and do not depend on one another
3. The **_LocalBroadcastManager.sendBroadcast_** method only sends broadcasts to receivers defined inside your application and does not exceed the scope of your application.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/giphy.gif)

## Gotchas And Things To Pay Attention To

* Do not send sensitive data through an implicit broadcast, because any application listening in for it, will receive it. You can prevent this by either specifying a package or attaching a permission to the broadcast
* Don’t start activities from a broadcast received as the user experience is lacking. Choose to display a notification instead.

The following bullet points refer to changes in broadcast receivers relevant for each Android OS version (starting from 7.0). For each version, certain limitations have taken places and behavior has changed as well. Keep these limitations in mind when thinking about using a broadcast receiver.

* **_7.0 and Up (API level 24)_** - Two system broadcasts have been disabled, [Action_New_Picture](https://developer.android.com/reference/android/hardware/Camera.html#ACTION_NEW_PICTURE) and [Action_New_Video](https://developer.android.com/reference/android/hardware/Camera.html#ACTION_NEW_VIDEO) (but they were brought back in Android O for registered receivers)
* **_8.0 and Up (API level 26)_** - Most implicit broadcasts need to be registered to dynamically and not statically (in your manifest). You can find the broadcasts that were whitelisted in this [link](https://developer.android.com/guide/components/broadcast-exceptions).
* **_9.0 and Up (API level 28)_** - Less information received on Wi-Fi system broadcast and [Network_State_Changed_Action](https://developer.android.com/reference/android/net/wifi/WifiManager.html#NETWORK_STATE_CHANGED_ACTION).

The changes in Android O are the ones you need to be the most aware of. The reason these changes were made was because it lead to performance issues, battery depletion and hurt user experience. This happened because many applications (even those not currently running) were listening in on a system wide change and when that change happened, chaos ensued. Imagine that every application registered to the action, came to life to check if it needed to do something because of the broadcast. Take into account something like the Wi-Fi state, which changes frequently, and you will begin to understand why these changes took place.

## Alternatives to Broadcast Receivers

To make it easier to navigate all these restrictions, below is a breakdown of other components you can use in the absence of a broadcast receiver. Each one has a different responsibility and use case, so try to map out which one caters to your needs.

* **_LocalBroadcastManager_** - As I mentioned above, this is valid only for broadcasts within your application
* **_Scheduling A Job_** - A job can be run depending on a signal or trigger received, so you may find that the broadcast you were listening on can be replaced by a job. Furthermore, the [JobScheduler](https://developer.android.com/reference/android/app/job/JobScheduler.html), will guarantee your job will finish, but it will take into account various system factors(time and conditions)to determine when it should run. When creating a job, you will override a method called **_onStartJob_**. This method runs on the main thread, so make sure that it finishes its work in a limited amount of time. If you need to perform complex logic, consider starting a background task. Furthermore, the return value for this method is a boolean, where true denotes that certain actions are still being performed, and false means the job is done

If you want to experience first hand the joy and wonder that are broadcast receivers, you can follow these links to repositories that I have set up:

1. [Custom Broadcast](https://github.com/TomerPacific/MediumArticles/tree/master/BroadcastReceivers/CustomBroadcast) (with manifest declaration)
2. [Registering Broadcast](https://github.com/TomerPacific/MediumArticles/tree/master/BroadcastReceivers/RegisteringBroadcast) (without declaring one in the manifest)
3. [LocalBroadcastManager](https://github.com/TomerPacific/MediumArticles/tree/master/BroadcastReceivers/LocalBroadcastManager)

Broadcast over.

