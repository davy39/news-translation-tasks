---
title: How to make a Cross-Platform Mobile App in Java
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-23T14:53:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-cross-platform-mobile-app-in-java-5f8eae071ff2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0Yjn597lhtYUQR98fnfNiQ.png
tags:
- name: Android
  slug: android
- name: iOS
  slug: ios
- name: Java
  slug: java
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Adrian D. Finlay

  Did you know that you can use Java to make cross platform mobile apps? Yes, pinch
  yourself, you read that right the first time! I’ll teach you the basics of how to
  use your existing Java knowledge to create performant apps on Andr...'
---

By Adrian D. Finlay

Did you know that you can use Java to make cross platform mobile apps? Yes, pinch yourself, you read that right the first time! I’ll teach you the basics of how to use your existing Java knowledge to create performant apps on Android and iOS in 12 easy steps. We will do this all using JavaFX as the GUI toolkit.

But first, some more foreground. You will need to meet the subsequent requirements to be able to build an application for **both** Android and iOS. However, if you do not desire to build an iOS application, you can feel free to develop on any x64 bit machine that supports Java SE 8. This project will be a Git repository built with gradle. But you do not need to create a Git repository.

The following are the **requirements**:

* A JDK 1.8 Compliant JVM
* Android Command Line Tools (SDK v.27)
* XCode 9.2
* Gradle 4.2
* Git Large File Storage (v.2.5.0) (Unnecessary if you do not want to create a git repository)
* Preferably at least 4G RAM

Impatient? Want to see an end result? Check out the completed project below.

[**afinlay5/OnyxFx**](https://github.com/afinlay5/OnyxFx)  
[_Gradle source code repository for OnyxFx, a cross-platform (Android/iOS/Linux/macOS/Windows) JavaFX app rendering…_github.com](https://github.com/afinlay5/OnyxFx)

My development environment will be Fedora Linux 28 and macOS High Sierra. Now that we’ve got that out of the way, let’s dig in.

### 1) Create a folder to house the project

I hosted my project, OnyxFx, as follows: “**/home/adriandavid/Projects/OnyxFx”.** You are, of course, free to host the project wherever you please.

![Image](https://cdn-media-1.freecodecamp.org/images/1*14wz3bVNKav6LNbTAYjEhA.png)

### 2) Initialize gradle, Git, set JAVA_HOME

Open a terminal in the root of the project directory. If gradle is properly configured, you should see something like this after executing the following command:

```
gradle -v
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*kuAXbVwYzNd3XRsGHjRy-w.png)

You need to make sure that gradle lists your Java Development Kit (JDK) 8 installation adjacent to the section labeled “JVM”.

While there are many ways to do this, the most straightforward way is to ensure that your JAVA_HOME environmental variable is properly set.

Depending on your environment, there are many ways to do this. One way to do this in most *nix environments is to set the variable in **/home/<user>/.b**ash**rc or /etc/pro**file. See the manual for your operating system to ensure that your JAVA_HOME environmental variable is set correctly.

You can include the following lines at the end of either .bashrc or profile to ensure that JAVA_HOME is set correctly.

```
JAVA_HOME=/home/adriandavid/java/oracle_jdk1.8.0_181/export JAVA_HOME
```

**Note:** You may install Oracle’s JDK 8 [here](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html).

Then, make sure that the shell reflects the above changes by running one of the following commands:

```
source ~/.bashrcsource /etc/profile
```

Enter the following command to verify that the variable is correctly set:

```
echo $JAVA_HOME
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*kJZ9I_IqrhACbckpzh6ueA.png)

If you are still experiencing difficulty or you are using Microsoft Windows, see [here](https://docs.oracle.com/cd/E19182-01/820-7851/inst_cli_jdk_javahome_t/).

First, run `git init` in the project’s root directory to initialize the Git repository. **Note: should you not desire to host a git repository, you may skip this step.**

Second, run `gradle init` in the project’s root directory to initialize the gradle repository. This step is required.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ab57WniSkAlmhElis7Aw3Q.png)

**Note:** You will notice that my example appears slightly different. This is because I already have gradle and Git initialized on my local environment.

### 3) Get groovy! Edit gradle.build and

Hopefully _Earth, Wind, & Fire_ can help you get groovy! Power up your favorite text editor, and edit your build.gradle located in your project’s root directory and replace the contents with the contents of the following GitHub gist.

These build.gradle settings configure our gradle project to use the **javafxmobile** plugin, which is the work horse of our project. You can learn more about the plugin [here](https://github.com/javafxports/javafxmobile-plugin) and [here](https://bitbucket.org/javafxports/javafxmobile-plugin). Among many things, the javafxmobile plugin automates the process of downloading (from Maven Central or jcenter) and adding the iOS and Android SDKs to your application’s classpath.

If you are familiar with gradle, maven, or ant, great — you probably have an idea of what’s going on. If you are not familiar with gradle, **don’t worry about it**. All you need to understand is that gradle is a build tool used to automate many tasks involved in building apps such as: grabbing dependencies, project organization, and so on.

Notice that we are targeting Android 7.1 Nougat (API version 25) and iOS 11 (we will see where this is done shortly). You may adjust these values as you see fit. Note, however, that in the case of Android, you must ensure that the API version matches the version of the SDK that you have download (more on this later).

Lastly, I will not demonstrate the production of signed executables in this tutorial. For this reason, _iOSSkipSigning_ is set to true and we do not make use of the _releaseAndroid_ gradle task. You can, however, provide the appropriate accommodations to produce signed apps.

### 4) Make a new file called gradle.properties and configure it

Create a new file in the project’s root directory called `gradle.properties` and add the following content to the file.

```
robovm.device.name=iPhone-7robovm.sdk.version=11.0org.gradle.jvmargs=-Xms4g -Xmx8g
```

These settings tell the javafxports plugin to use an iPhone-7 as the on-board emulator, to target iOS 11, and to pass the Xms and Xmx flags to the JVM, which specifies both the initial memory pool to 4GB and the maximum heap memory pool to 8GB. This will be necessary for the compilation of the openJDK and the development of the iOS build.

### 5) Install Homebrew (iOS only)

If you do not have a Mac and are not intending to produce an iOS build, feel free to skip this step.

Open the terminal in macOS and paste the following command.

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### 6) Install the USB Multiplexing Socket (iOS only)

Only move on to this step if Homebrew has successfully installed. If you do not have a Mac and are not intending to produce an iOS build, feel free to skip this step.

Open the terminal in macOS and paste the following command.

```
brew install usbmuxd
```

### 7) Grab the Android Command Line Tools

Grab Android Command Line Tools for your platform [here](https://developer.android.com/studio/#downloads). After the download has finished, unzip the folder and paste the contents in the directory of your choice. For me, this was `/home/<user>/A`ndroid.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cZFJp50kxOy9kORJ9VQX4Q.png)

### 8) Set Android_HOME, Grab necessary Android packages

As with Java, gradle needs to know where to look to find the Android Command Line Tools. There are a few ways to do this. However, in the spirit of simplicity and consistency, we will set the ANDROID_HOME environmental variable in this tutorial. Add the following variable in the same way that we did it for JAVA_HOME. For example:

```
ANDROID_HOME=/home/adriandavid/Android/ export ANDROID_HOME
```

Remember to reload the shell by adding `source <fi`le> as we did for JAVA_HOME.

Now, grab the tools necessary to build the Android build. Execute the following command:

```
# *.nix./sdkmanager "platform-tools" "build-tools;25.0.3" "platforms;android-25" "extras;android;m2repository" "extras;google;m2repository"
```

```
or
```

```
#Windowssdkmanager "platform-tools" "build-tools;25.0.3" "platforms;android-25" "extras;android;m2repository" "extras;google;m2repository"
```

Take careful notice that the SDK and API version we have specified in gradle.build correspond to the version we have specified in this command. Namely, “25”. Should this be misaligned, the build will not succeed.

### 9) Create the application’s directory structure

To automate the process of creating these directories, execute the following shell script.

Bourne-Again Shell / Korn Shell:

Windows Shell (cmd):

Save the file as mkpdir.bat or mkpdir.sh and execute the file from the project’s root directory as **root** (or **Administrator**).

```
# *.nixchmod +x mkdir.sh-sh ./mkpdir.sh
```

```
# Windowsmkpdir
```

Notice that we created directories for embedded and desktop. We will produce a desktop build, because it takes no additional work to do so. However, we will not produce any builds for embedded devices.

### 10) Create your JavaFX Application!

Navigate to /src/<platform>/java and begin developing your JavaFx application! Application resources are stored in /src/<platform>/resources.

You can start with a simple _Hello World_ application or look at the source code that I have put together [here](https://github.com/afinlay5/OnyxFx). OnyxFx is an application I made, following these instructions, that makes REST calls over HTTP to the OnyxFxAPI. The API, in turn, is a web scraper that will return the statistical data (points per game, rebounds per game, assists per game) for the NBA® player and season the client specifies. It returns the data as JSON, which is then parsed and displayed to the screen of the mobile app. Feel free to edit it!

Keep in mind that although you can share source code, you should include custom edits in each copy of the source, should you want to make device specific changes.

Also note that the underlying compiler (MobiDevelop’s fork of RoboVM) does not fully support all Java 8 APIs. If you look very closely at my source code, you will notice that in the iOS version of the source code, I have removed unsupported API such as **java.util.function.BiConsumer** and **java.util.Map.replace()**.

### 11) Create a RAM disk for iOS builds (iOS only)

The compilation process for iOS is very resource-heavy, as the plugin will compile the entire openJDK and other libraries twice to create a fat JAR that it will use to build your application. Therefore, you should preemptively create a RAM disk to accommodate for the memory requirements.

This step, however, is subject to your judgement of your machine’s capabilities. For context, the macOS machine that I used to compile my iOS app has 4GB of DDR2 RAM. I decided to make an 8GB RAM disk. To do so, execute the following command in the terminal.

```
SIZE=8192 ; diskutil erasevolume HFS+ ‘RoboVM RAM Disk’ `hdiutil attach -nomount ram://$((SIZE * 8192))`
```

### 12) Build and Run your application!

To build your application, execute the gradle wrapper in the root directory from the terminal as follows.

```
./gradlew clean build
```

This will produce a desktop application packaged as a JAR with scripts to run the application provided in `/build/distributions/<AppName.t`ar>`; and /build/distributions/<App`Name.zip>. Should you unzip the directories, you will notice the following structure:

![Image](https://cdn-media-1.freecodecamp.org/images/1*oF-cta8Trg15kQLld7oitA.png)

Notice that in /bin there are scripts to execute the application. These scripts rely on preserving the current folder structure. Also notice that is not necessary for you to have **tree** installed. It is used here simply for illustrative purposes.

There is, additionally, a standalone JAR that you can use to execute the application on any desktop environment supporting JavaFX 8. To run the application, execute one of the following:

```
# Navigate to /build/distributions/<ProjectName>/
```

```
#On *.nixcd bin./<ProjectName>
```

```
#On Windowscd bin<ProjectName>
```

```
#Platform agnosticjava -jar OnyxFxMobile.jar (or double click, if jvm is configured to run .jar files)
```

```
Note: If the executable providing "java" is not the same vendor and/or version of the Java 8 JDK with which you built this application, the jar may not run. JavaFX 8 builds between the openJDK & Oracle JDK are incompatible.
```

```
Otherwise: /location/to/java8/bin/java -jar <ProjectName>
```

#### View this project’s gradle tasks

You can view this project’s gradle tasks by running the following in the project’s root directory.

```
./gradlew tasks
```

#### To Compile, Run on Desktop

The following command will run your project in the host environment.

```
./gradlew jar./gradlew run
```

You will find a standalone jar in `build/libs/<AppName&g`t;.jar .

#### To Compile, Run on Android

```
./android #Generates a debug Android apk containing the JavaFX application.
```

```
./androidInstall #Launch the application on a connected android device.
```

```
./androidRelease #Generates a release Android apk containing the JavaFX application.
```

```
Note: You will need to configure a valid signingConfig when releasing an APK (javafxports).
```

You will find two APKs in `build/javafxports/android`.  
The first will be named `<AppName&g`t;.apk.  
The second will be `named <AppName>-u`naligned.apk.

#### To Compile, Run on iOS

```
./createIpa - Generates an iOS ipa containing the JavaFX app.
```

```
./launchIOSDevice - Launches app on a connected ios device.
```

```
./launchIPadSimulator - Launches app on an iPad simulator.
```

```
./launchIPhoneSimulator - Launches app on an iPhone simulator.
```

You will find three executables in `build/javafxports/ios`.  
The first will be named `<AppName&g`t;.ipa.  
The second will be `named <AppN`ame>.dSYM.  
The third wi`ll be named &`lt;AppName>.app.

### Some screenshots of my sample app

#### On Desktop

![Image](https://cdn-media-1.freecodecamp.org/images/1*0Yjn597lhtYUQR98fnfNiQ.png)

#### On Android

![Image](https://cdn-media-1.freecodecamp.org/images/1*YYNxKLhPNfKZe3Z3Ig9jFQ.png)

#### On iPhone

![Image](https://cdn-media-1.freecodecamp.org/images/1*rsyQ8wQJI-AeWeK56Z45Og.png)

#### On iPad

![Image](https://cdn-media-1.freecodecamp.org/images/1*rAVDpDXcdQkNzDDol5p3hQ.png)

#### Splash Screen

![Image](https://cdn-media-1.freecodecamp.org/images/1*_HKrh4pQXXwupdd70yomgg.png)

### My Closing Thoughts

_javafxports_ is a promising project that aims to bring JavaFX and the Java SE platform onto mobile and other devices. In a way, the tool parallels Xamarin in its efforts. However, the project has a lot of work left to be done.

For a start, the plugin currently does not fully support Java 8. On Android, it uses retrolambda to handle Java 8 Lambda Expressions & Method References. It technically is up to Java 6. Additional dependencies make it such that you can use Java 8. However, the process is straightforward, the builds work as expected, and the compilation time is not too long.

On iOS, however, the builds are extremely memory-intensive and the compilation process takes a very long time. The following is a snippet of the log for ./gradlew createIpa task.

```
:createIpa (Thread[Task worker for ‘:’,5,main]) completed. Took 1 hrs 46 mins 40.198 secs.
```

In total, the process consumed about over 6GB of RAM on my machine. This is hardly ideal. However, the future is promising. A company called Gluon has developed a high performance, fully modular custom JVM fully supporting Java 9, that you can read more about [here](https://gluonhq.com/products/mobile/vm/).

_This article is originally published on the blog section of my homepage, [here](http://www.adriandavid.me/blog/24/how-to-make-a-cross-platform-mobile-app-with-java.xhtml)._

### Resources to explore:

* JavaFxMobile Plugin Git Repo: [https://github.com/javafxports/javafxmobile-plugin](https://github.com/javafxports/javafxmobile-plugin)
* JavaFxPorts Documentation: [http://docs.gluonhq.com/javafxports/#_how_it_works](http://docs.gluonhq.com/javafxports/#_how_it_works)
* JavaFxPorts Homepage: [http://javafxports.org/](http://javafxports.org/)
* Gluon Documentation: [https://gluonhq.com/developers/documentation/](https://gluonhq.com/developers/documentation/)
* Google Groups Page for JavaFxPorts: [https://groups.google.com/forum/#!forum/javafxports](https://groups.google.com/forum/#!forum/javafxports)
* StackOverflow Page for JavaFxPorts: [https://stackoverflow.com/questions/tagged/javafxports](https://stackoverflow.com/questions/tagged/javafxports)
* Gluon Mobile Pricing/License Options: [https://gluonhq.com/products/mobile/buy/](https://gluonhq.com/products/mobile/buy/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*SWVp-cGi_ipjWWw3SU5ITQ.jpeg)
_Source: [Looney Tunes Ending](https://www.youtube.com/watch?v=0FHEeG_uq5Y" rel="noopener" target="_blank" title=")_

