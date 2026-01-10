---
title: How to Hide Your API Keys in an Android Application
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2023-01-16T21:03:19.000Z'
originalURL: https://freecodecamp.org/news/hide-your-api-keys-in-android
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/oleg-didenko-lMNo9SwBN_o-unsplash.jpg
tags:
- name: Android
  slug: android
seo_title: null
seo_desc: 'Let''s say that you are using a version control system and your project
  uses services that require API keys. Everything is all good when they''re on your
  local machine, but you don’t want to share these API keys with the world.

  So how can you still pre...'
---

Let's say that you are using a version control system and your project uses services that require API keys. Everything is all good when they're on your local machine, but you don’t want to share these API keys with the world.

So how can you still preserve your API keys within your application, but also hide them when you upload your code to your repository?

You probably want to be able to still use your API keys in a normal fashion inside your applications, but also not expose them.

## What Are Secrets?

That’s where **secrets** come in. Similar to those that you keep only to yourself, but in a developer kind of way.

Secrets can represent crucial information that is required by your application to operate, but should not be visible to anyone working outside the project. 

These can be API keys or authorization tokens, but in essence a secret is any piece of authorization information that should only be used by you and you alone. It's similar to how you don’t want to share your password to a website with anyone else.

🚨 Disclaimer: Be aware that the solution provided in this article works for not exposing your secrets from your version control system. But since they are part of your application, they can still be discovered by decompiling your APK.

## How to Keep Your Secrets Safe

In your project, you should have a **local.properties** file under the root directory of your project

To make sure it is ignored by your version control system, open the .gitignore file and see that it is found there:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/1_Br5FcOmNI-SVp7QxWM3FYA.jpeg)

You will need to import to your project the [Secrets Gradle plugin](https://github.com/google/secrets-gradle-plugin).

To do this, go to your project’s root build.gradle file and paste in the following line:

```kotlin
buildscript {
    dependencies {
        id 'com.google.android.libraries.mapsplatform.secrets-gradle-plugin' version '2.0.1' apply false
    }
}
```

Next, go to your app’s build.gradle file and paste in the following line:

```kotlin
plugins {
    ...
    id 'com.google.android.libraries.mapsplatform.secrets-gradle-plugin'
}
```

Add your API key inside the local.properties file:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/1__T-HkbD9isK3IuCLdE1v5w.jpeg)

You can use your secret inside your **AndroidManifest.xml** file by adding a meta-data tag inside your application tag:

```xml
<application
        android:allowBackup="true" 
        .....
                                     >
    <activity>
      ....
    </activity>
      <meta-data
            android:name="YOUR_API_KEY_NAME"     /// Choose any value here
            android:value="${API_KEY_NAME}"/>    /// Write the name you gave inside your local.properties file
</application>
```

To access your API key, you can use the PackageManager to get the meta data:

```kotlin
val applicationInfo: ApplicationInfo = application.packageManager
                .getApplicationInfo(application.packageName, PackageManager.GET_META_DATA)
val apiKey = applicationInfo.metaData["YOUR_API_KEY_NAME"]
```

Alternatively, you can also use the BuildConfig object to get it:

```kotlin
BuildConfig.YOUR_API_KEY_NAME
```

That’s it. Now you can rest easy knowing that your secrets won’t be exposed by your version control system.

Enjoy keeping your secrets. ㊙️

I used this on one of my recent projects, and you can see the source code (sans the secrets) [here](https://github.com/TomerPacific/movies-presenter).

And if you want to check out other articles that I have written, you can go [here](https://github.com/TomerPacific/MediumArticles).

