---
title: Cordova iOS Application Development Explained from Setup to Deployment
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-01T20:01:00.000Z'
originalURL: https://freecodecamp.org/news/cordova-ios-application-development-setup-to-deployment
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e58740569d1a4ca3c99.jpg
tags:
- name: app development
  slug: app-development
- name: iOS
  slug: ios
seo_title: null
seo_desc: 'Hybrid Application development for Android is a breeze, be it for development
  or production configuration. But I personally find Cordova iOS setup, development,
  and deployment a bit complicated.

  Most of the Hybrid Application Developers who are in th...'
---

![iphone_1737513_1920](https://image.ibb.co/iKCSuQ/Xz_J197k8_QI32.jpg)

Hybrid Application development for Android is a breeze, be it for development or production configuration. But I personally find Cordova iOS setup, development, and deployment a bit complicated.

Most of the Hybrid Application Developers who are in the learning stages are not able to explore hybrid iOS app development process simply because they don't own a mac. And developing iOS apps requires the iOS SDK and XCode (unlike the Android SDK which runs on any Desktop OS). 

Therefore the aim of this guide is to show the basic workflow of hybrid iOS app development on a Mac. This way developers can see how it's done even if they can't develop the apps.

## **Creating a cordova project**

Begin by opening the terminal and creating a new cordova project (use sudo only if you have permission issues, ie. EACCESS errors):

```text
sudo cordova create iosdemo
cd iosdemo
sudo cordova platform add ios
```

At the time of writing this guide the cordova iOS platform version is 4.3.1.

We wont modify any source code of the app – rather, we'll simply continue with the default sample code that is added by cordova automatically when we run the create command. However it is assumed we will add plugins modify code in the `www` folder during normal development flow.

The next step is to run the cordova build command. This will convert our app code to an .xcodeproj file which we will use next.

```text
sudo cordova build ios
```

The generated Xcode Project file will be here:

```text
[Your App Folder]/platforms/ios/[Your App Name].xcodeproj
```

Now in the case of Android the code signing is done using the Keystore file which is in .jks format. However in iOS it is required that you have a Apple developer account for distributing iOS apps. This is so that we can generate the _Certificates_ and _Provisioning Profiles_ required for distributing the app.

For pricing and other info about a Developer account refer to [this page](https://developer.apple.com/support/purchase-activation/).

## **Creating Development Certificates**

Once you have the account ready we can proceed further and login to your [Apple developer account](https://developer.apple.com/account/).

The dashboard screen should look something like this:

![Project opening in Xcode](https://image.ibb.co/j0d8zQ/Clipboard_image_2017_09_18_11_35_58.png)

Click on `Certificates, Identifiers & Profiles`. This should take you to the following screen, which by default displays Certificates issued from your account:

![Certificates, Identifiers & Profiles](https://image.ibb.co/fk8mm5/1.png)

iOS Certficates are of mainly two types: Development or Distribution. Click on the Plus (+) button in the top right corner of the list which will open the following page:

![Add iOS Certificate](https://image.ibb.co/dksXtk/2.png)

First let's create a development profile. Select _iOS App Development_ and click continue.

This should bring you to the following screen, where you are asked to create and upload a Certificate Signing Request or CSR file.

![Upload CSR file](https://image.ibb.co/iwBE65/3.png)

Follow the on-screen instructions to generate it, and continue. Once the certificate is ready, download it to your Mac, and double click it. This will add it to Keychain Access in the Mac.

![Download development certificate](https://image.ibb.co/dJg6m5/4.png)

## **Creating Distribution Certificates**

Creating distribution certificates is similar to the process for creating development certificates. However here we select `App Store and Ad Hoc` from `Production` section in the `Add iOS Certifcate Page`:

![Add iOS Certificate](https://image.ibb.co/bEKFeQ/5.png)

## **Creating the App ID**

Select `App IDs` from `Identifiers` section. This will open the list of existing app IDs. Next click on the Plus button on the top right (+). This will open the _Register iOS App IDs_ page.

![Register iOS App IDs](https://image.ibb.co/iXTuOk/6.png)

Select Explicit App ID. The App Description can be any related name – this is what will be displayed in the app id list against the particular app id.

An app id is a string in the format _AB11A1ABCD.com.mycompany.myapp_ where _AB11A1ABCD_ is the app id prefix which is by default the team ID and _com.mycompany.myapp_ is the bundle ID which is unique to each app. 

Its recommended that the bundle id must be in a reverse-domain name style string. For example, the company MYCOMPANY may have two apps (App1 and App2). So the HTTP URL for each app is usually app1.mycompany.com and app2.mycompany.com. Hence the bundle IDs for each app will be com.mycompany.app1 and com.mycompany.app2

Next select any services from the checklist that you need to use in your app, such as Push Notifications, Wallet etc. Next click on continue and confirm the details and finally register the app id.

## **Adding devices to your developer account**

Select `All` from the `Devices` section. This will open the list of already added devices to your Apple developer account. Only these devices are allowed to run the app during development. 

To add a new device, click on the Plus button in the top right (+). The following screen will be displayed:

![add device screen](https://image.ibb.co/gTmW3k/8.png)

Here the name can be any easily understandable name, for example iPhone 5s ABC Pvt Ltd. The device UDID is the unique ID associated with each Apple device.

To find the UDID of a device follow these steps:

1. Connect the device to your Mac.
2. Open the System Information app located in the /Applications/Utilities folder.
3. Select USB under Hardware in the left column. 
4. On the right, select the connected device under USB Device Tree. The device ID, or “Serial Number”, appears below.

Once you have entered the device UDID and name click continue, then confirm the details and register.

## **Creating a Development Provisioning Profile**

To create a development Provisioning Profile click on Provisioning Profiles -> All. This should show all the profiles, development as well as distribution. Next click on the Plus button on the top right (+) This should show the following page:

![Creating a development provisioning profile](https://image.ibb.co/dk3KOk/7.png)

Here select `iOS App Development` and click continue. In the dropdown that is displayed select the App ID we created previously and continue.

Next A checklist of certificates is displayed from which we can select one or multiple. These are development certificates and not distribution ones. The generated provisioning profile will be linked to these certificates.

When you click Continue, a checklist of devices is displayed. Select one, multiple, or all. Only selected devices will be allowed to run the app using this provisioning profile.

Next, after clicking continue, enter the name for the provisioning profile, and download the generated .mobileprovision file.

**Notes**: it's the same process to create your Adhoc Distribution Provisioning Profile. It's also very similar to create your AppStore Distribution Provisioning Profile, except for that one we don't select devices, as the app will be available publicly through the AppStore.

Now that we have all that we need we can continue generating the actual ipa using Xcode.

_Cordova build command converts our app code to an xcode project. Using Xcode we create an .ipa file which is the actual app to be installed._

Before moving forward double tap on both Certificates to add them to your keychain.

## **Continuing in Xcode**

Next, double tap the .xcodeproj file which should open it in Xcode. (Please use the latest version of Xcode – I have used Xcode 8.3.2.)

![Project opening in Xcode](https://image.ibb.co/mPdGKQ/Screen_Shot_2017_09_18_at_11_06_55_AM.png)

The Xcode screen should look something like the above.

Click on the App Name on the top left corner fo the window. This will open the detailed view on the right side.

![Project settings](https://image.ibb.co/fqb3ZQ/Screen_Shot_2017_09_18_at_5_07_53_PM.png)

Then click on Targets-> App Name:

![targets](https://image.ibb.co/i0znTk/Screen_Shot_2017_09_18_at_5_11_28_PM.png)

This will display the following details tab:

![target details](https://image.ibb.co/ksBj8k/Screen_Shot_2017_09_18_at_5_15_29_PM.png)

Click on general, which should display this:

![general details](https://image.ibb.co/k8KFEQ/Screen_Shot_2017_09_18_at_5_18_29_PM.png)

Uncheck the Automatically Manage Signing Checkbox.

This should display the following error, stating AppNAme requires a provisioning profile:

![profile error](https://image.ibb.co/mDq5EQ/Screen_Shot_2017_09_18_at_5_20_35_PM.png)

Next, under Signing (Debug), click the Provisioning Profile Dropdown and select the _import profile_ option. In the file selection dialog that pops up, navigate to the path where the development provisioning profile is downloaded, and select it. It will have an extension of _.mobileprovision._

After you select that, the error should be gone, and it should show Team as the Team Name in your Apple developer account and Signing Certificate Name.

Do the same thing for the Signing (Release) section – but in the file selection dialog select the Ad Hoc distribution Profile.

Now that the Code signing steps are done we either

* run the app directly on device
* run the app on a simulator
* generate an ipa file for distribution
* upload app to appstore

## **Running the app directly on device**

To run the app on a device connect the device to the Mac via USB. Then in the top left corner in the list of devices select the connected device, and click the run or play button (black triangular button):

![run device](https://image.ibb.co/k4xo15/Screen_Shot_2017_09_18_at_5_34_14_PM.png)

![run device](https://image.ibb.co/hjzhuQ/Screen_Shot_2017_09_18_at_5_36_55_PM.png)

The build status will be displayed in the status bar on the top of the window. If all goes fine, the app should be installed on the device, and it should automatically load in a while.

**Note**: the steps are the same for running the app on a simulator. But instead of an actual device we use the available iPhone and iPad simulators from the device list.

## **Generate an ipa file for distribution**

This approach can be done in case you need to distribute the app to the testing team, etc. However the device used by them must have a UDID present in the provisioning profile.

From the Xcode menu select `Product` -> `Clean`, then `Product` -> `Archive`. The Archives organizer appears and displays the new archive.

![ios archive organizer](https://image.ibb.co/iunfMG/6_ios_archive_organizer_2x.png)

In the righthand side panel select the Export option and a list of options will appear.

To distribute your app to users with designated devices, select “Save for Ad Hoc Deployment.” The app will be code signed with the distribution certificate.

To distribute your app for internal testing, select “Save for Development Deployment.” The app will be code signed with your development certificate.

![ios archive organizer export as ad hoc](https://image.ibb.co/jQJLMG/6_ios_createappstorepackage_1_2x.png)

In the dialog that appears, choose a team from the pop-up menu and click Choose.

![ios export select team](https://image.ibb.co/gH2VMG/6_ios_export_choose_team_2x.png)

Next the device selection dialog pops up. Select either _All devices_ or _specific devices_ and click next.

Next the review dialog is displayed. Here it will show the signing certificate and provisioning profile used for generating the build. Review and click next. Finally the file save as a popup is displayed to select the location in the file system to store the exported app file.

The app is exported as .ipa` file .

To run this file on device simply double tap it which will open it in iTunes.

Then connect your device (this should show a small device icon on the top left corner of the iTunes window). Tapping on it will show the device summary such as apps, music etc on the device. Select the apps tab, and in the left pane select the app to be installed and click install. Wait for the process to complete and click apply. This should install the ipa file on your device.

To debug the app:

1. open Safari
2. open the app on the device
3. in the Safari menu bar select `Develop --> Your Device Name --> Your App`.

## **Thats all folks!**

