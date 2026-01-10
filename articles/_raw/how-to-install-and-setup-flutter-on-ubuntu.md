---
title: How to Install and Set Up Flutter on Ubuntu 16.04+
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-12T15:43:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-and-setup-flutter-on-ubuntu
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/Flutter-logo.png
tags:
- name: Flutter
  slug: flutter
- name: Ubuntu
  slug: ubuntu
seo_title: null
seo_desc: "By Otavio Ehrenberger\nFlutter is a Dart-based toolkit that helps you build\
  \ the front end of your apps. It really shines in cross-platform mobile app development\
  \ and aims to be a viable option for web and desktop as well. \nIn its mobile app\
  \ flavor, Fl..."
---

By Otavio Ehrenberger

Flutter is a Dart-based toolkit that helps you build the front end of your apps. It really shines in cross-platform mobile app development and aims to be a viable option for web and desktop as well. 

In its mobile app flavor, Flutter provides many UI abstractions to build interfaces. You can implement logic in Dart, or directly with Kotlin or Swift if you need more specific interactions with your OS of choice. 

While cross-platform app development is nothing new, earlier strategies such as PhoneGap and Ionic used the available WebView implementation instead of interfacing directly with the system. This is not only very limiting but also has a lot of performance costs. 

The gold standard for _native_ cross-platform app development is yet to be established. But Flutter both offers a a lot on its own and elegantly steps out of the way when you need to interact directly with the OS using whatever official language you need to use. 

This makes Flutter a game changer even before it has fulfilled its potential of sharing the same codebase with the web and desktop versions of an app.

In this tutorial we'll get to setup an Ubuntu 16.04+ machine for Android app development with Flutter. You can also edit Swift code directly from Android Studio, but unfortunately you won't have official support to test the app in iOS devices or emulators due to Apple's policies. 

For this we'll need to install and configure Java as an Android Studio dependency, setup Android Studio to use hardware-acceleration and run Flutter apps and, of course, install and configure Flutter itself. So, let's get started.

## How to Install and Configure Flutter

First things first: let's install Flutter through the snap store. If you are using Ubuntu 16.04 onwards, you likely already have the `snap` command installed. 

If you are not, you can follow the instructions available for your distro at the "Install Snap Store on your Linux distribution" section on [this](https://snapcraft.io/snap-store) page.

![Some of the linux distros snap store is available for.](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5wgxz7mtwcps32vuq3fp.png)

With the `snap` command available, install Flutter like this:

```bash
sudo snap install flutter --classic

```

After Flutter has finished installing, run a basic checkup which will also do some automatic configuring:

```bash
flutter doctor -v

```

![flutter doctor output](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/12plekbnhxgfqz6u4efn.png)

Flutter has been installed, nice!

## How to Install and Configure Java

First of all, we need to get the (community-backed) Open Java Development Kit before being able to use Android Studio. 

To get the latest stable version of Java 8, open your terminal and run: 

```bash
sudo apt-get update && sudo apt-get install openjdk-8-jdk

```

Other versions can sometimes show some unpredictable problems while working alongside Flutter as of May 2021, so I recommend installing OpenJDK 8. Don't worry, OpenJDK 8 is set to receive support at least until 2024.

After a successful installation, it is time to set the `$JAVA_HOME` environment variable. It's used by default by many applications which interact with your local Java installation, Android Studio among them. 

Get a list of the currently installed JDKs in your system with this command:

```bash
sudo update-alternatives --config java

```

Choose from the list of locally installed versions (remember that Java 8 is the easiest to use with Flutter) and set the one which you would like to be the system's default. 

Set `$JAVA_HOME` to its path, **without including the `/bin` portion onwards of the path** (in my case, for instance, the correct path was `/usr/lib/jvm/java-8-openjdk-amd64`):

```bash
#JAVA_HOME=<your_java_installation_path>, same as below if you followed instructions
JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64" # my local path after installing openjdk-8
echo "JAVA_HOME=\"$JAVA_HOME\"" >> ~/.bashrc # sets JAVA_HOME env var for current user
echo 'export PATH=$PATH:$JAVA_HOME/bin' >> .zshrc # adds java's binaries to your path
source ~/.bashrc && echo $JAVA_HOME # verifies that the variable was perenially set

```

## How to Install and Configure Android Studio to Run with Flutter

You can download Android Studio [here](https://developer.android.com/studio).

After your download finishes, extract the Android Studio package into the `/usr/local/` directory:

```bash
sudo tar -C /usr/local -zxvf ~/Downloads/<android_studio_package>.tar.gz

```

After it's successfully extracted, run Android Studio's installation script:

```bash
bash /usr/local/android-studio/bin/studio.sh

```

This should pop up the install wizard. Follow the wizard's instructions for the standard installation and you should eventually arrive at the starter screen. 

Select Configurations at the lower right corner and click on "Plugins":

![Android Studio starter screen](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9xaxzsat1b2kcksqkypy.png)

Install the "Flutter" official plugin, published by **flutter.dev**:

![Flutter Plugin](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o6t1w69ero8xe234idnl.png)

You will be prompted to install the Dart plugin (Flutter's base programming language) before you proceed. Click 'Ok' and restart the Android Studio IDE. 

The option to start a Flutter project should be visible now. Click on it, then select 'Flutter Application' and click on 'Next'.

You should be greeted by the project configuration screen. Configure your project's name, location, and description as you wish, and point the field "Flutter SDK" to `/home/<your_user_name>/snap/flutter/common/flutter`:

![Flutter Project Config](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/w4j43px47sc5o9t04jtl.png)

In case the above path is not available, open a terminal and run:

```bash
flutter doctor -v

```

You should then be greeted with the starter project screen:

![Flutter Project Starter](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ve413tpxbsn674bqlowx.png)

Almost done. Now you need to accept the Android licenses and double check your Flutter installation's ownership in order to avoid future surprise build errors due to resources denied for Android Studio. 

Open up your terminal and run:

```bash
flutter doctor --android-licenses # accept Google's licenses, necessary to build the app
sudo chown -R $USER:$USER /home/$USER/snap/flutter # confirm you are the owner of local flutter

```

Now Android Studio is finally setup to run Flutter projects. Nice!

You should also enable the Desktop Entry for Android Studio. In your project screen, click on "Tools" then "Create Desktop Entry":

![AS Desktop Entry](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qmw2u417r7v8x6ry2n7t.png)

The Android Studio shortcut should be available from the "Activities" menu now.

## How to Enable Hardware Virtualization for the Android Emulator

In order to run the emulator, we must first set up your CPU's hardware virtualization capabilities.

Run `kvm-ok` in your terminal and your output should indicate whether you can use KVM acceleration or not. If you have an AMD or Intel CPU, most likely it can.

The Kernel Virtual Machine, in a nutshell, is a bridge between the kernel with virtual devices which allows a virtual device to emulate its own hardware directly from the host computer's hardware. You can take a look [here](https://www.linux-kvm.org/page/FAQ#Preparing_to_use_KVM) for more detailed information.

Provided you are indeed able to use KVM acceleration, it is time to setup KVM and authorize the current user for it:

```bash
sudo apt update # update repositories
sudo apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils # base packages
sudo addgroup kvm && sudo addgroup libvirtd # create user authorization groups
sudo adduser $USER kvm && sudo adduser $USER libvirtd # add current user to auth groups
sudo virsh -c qemu:///system list # checks if virtualization is ok
# if everything went fine, your output will be something like:
#
#  Id    Name                           State
#----------------------------------------------------


```

And restart your user session. In the computer, not only the terminal. Log off the system and then login or reboot the PC, I'll be waiting.

## How to Use the Android Emulator to Test Apps

Now, open an Android Studio project and click on the 'AVD Manager' (Android Virtual Device) option located in the window's upper right corner:

![AVD Manager](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/a3hnfp08d78fu8s81qad.png)

Click on the "Create Virtual Device" button and a window with a list of devices should pop up with the 'Phone' category preselected. I recommend that you pick a device with Play Store enabled just in case you might want to use it later inside your emulated device. Mine was the Nexus 5.

Click on the 'Next' button and a list of system images (Android OS Versions) should appear:

![System Images](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lsncydy90yb8wh6yiq1p.png)

First, download your target image (by simply clicking on 'Download' right beside the Release Name), select a locally downloaded image, and click on 'Next'. It should only be highlighted after the image was successfully downloaded.

A window will then show up, offering you to customize your virtual device's properties such as screen orientation on startup, RAM usage, and so on. Tweak the device to your liking if you want, otherwise you can safely click on 'Finish'.

If everything goes well, you should now see your device listed at the Android Virtual Device Manager window:

![AVD Manager List](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qsyjl24niolby6uh2np7.png)

Go back to your Android Studio project view. At the same line where the 'AVD Manager' button is located, there is a dropdown list of available devices just to the left of 'main.dart'. Select the emulator you have just set up and click the green 'play' button just to the right of 'main.dart'. 

In case the emulator is not listed there yet, open the AVD Manager window again and click the green 'play' button under the 'actions' label listed for your virtual device. This will load and open the emulator before running your Flutter code.

![Android Virtual Device](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/hli5nfnywjr2i5mcf289.png)

Notice that 'debug' ribbon in the upper right corner? In case you wanna get rid of it, add `debugShowCheckedModeBanner: false` as a field of `MaterialApp`.

## How to Use a Physical Android Device to Test Apps

You'll need to have a local installation of the Android Debug Bridge in order to enable your computer to trade information (such as APK builds) with any connected Android devices, virtual or otherwise.

The ADB consists of a client (the interface from which you run commands, which will be the ADB binary installed in your computer for all purposes of this tutorial), a daemon (which executes in the Android device the commands initially sent from the client) and a server (which runs locally in the PC, which has a default listening location at tcp://localhost:5037, and intermediates the communication between the client and the daemon).

Very conveniently, Android Studio currently ships with an ADB, so if you followed the instructions above to install Android Studio, you already have one at your computer. 

It is possible to install ADB from the Ubuntu repositories alongside the one in Android Studio, but this invites headaches if your computer eventually confuses the locally installed versions. So instead let's setup our Linux user to access Android Studio's ADB and then run ADB:

```bash
echo 'export PATH=$PATH:$HOME"/Android/Sdk/platform-tools"' >> .bashrc # adds adb to path
adb start-server # launches adb server
adb devices # lists connected devices

```

After running `adb devices`, you most likely got an error. This error has registered the `$LOGNAME` variable which contains the current user name. You will use it to insert your user into the `plugdev` group, in case you are not there already. 

You also most likely do not have a set of `udev` rules for Android devices. UDEV rule files specify Ubuntu interactions with plugged in devices, and Ubuntu will refuse to perform certain interactions with your Android device unless it is previously authorized in an UDEV rules file. 

So, let's correct those errors:

```bash
# add user to plugdev group
sudo usermod -aG plugdev $LOGNAME
# downloads a very thorough UDEV rules file into the appropriate directory
sudo wget -O /etc/udev/rules.d/51-android.rules https://raw.githubusercontent.com/NicolasBernaerts/ubuntu-scripts/master/android/51-android.rules
# gives reading permission to the UDEV android file
sudo chmod a+r /etc/udev/rules.d/51-android.rules

```

Reboot your current Linux user session to apply these changes, then open a terminal and run `adb devices` again. 

In case you still have a UDEV-related error, your device's manufacturer ID probably is not listed in `/etc/udev/rules.d/51-android.rules`. In this case, search the internet for your device's manufacturer UDEV id and manually add it to the rule list in the same format as the others. 

Notice how the only field with a unique value amongst the rows is `ATTR{idVendor}`. If you do not receive any error, you'll notice that your device is listed as 'unauthorized'. Let's unlock the device for USB debugging.

## How to Unlock Developer Mode and USB Debugging

In your Android device, open up 'Settings', then 'About Phone'. Tap your 'Build number' 5-6 times until a toast telling that 'You are now a developer!' pops up.

![You Are Now a Developer](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/skib1pnotczz49wo5s4k.png)

Back to 'Settings', open System', you should see that 'Developer Options' were unlocked.

![Developer Options](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/lovbrm5eg1yg8twi3dft.png)

Tap this new entry and check 'USB debugging' just under the 'Debug' section.

![USB Debugging](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0vp2kw9urr2dalqfvorb.png)

Plug your Android device in your PC via USB, then run `adb devices` on your terminal. The output should list your device and also point that it is unlocked for debugging. 

Now, go back to Android Studio, click on the device dropdown list (the one in which you selected your Virtual Device before) and your physical device should now be listed. Select it. 

Finally, click on the 'run' button and you should see the app in your device, ready to be interacted with.

Congratulations! You are now a Flutter developer. Good luck in your development journey!

_Cover image from flutter.dev._

