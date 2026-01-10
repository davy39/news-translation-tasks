---
title: How to manage different environments and configurations for iOS projects
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-18T10:51:44.000Z'
originalURL: https://freecodecamp.org/news/managing-different-environments-and-configurations-for-ios-projects-7970327dd9c9
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9cb264740569d1a4cac1c3.jpg
tags:
- name: Apple
  slug: apple
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Boudhayan Biswas

  As iOS developers, we are already aware of managing different environments like
  Development, QA, Beta, and Production. For these different environments, there are
  different server URLs, app icons, and configurations.

  So before cre...'
---

By Boudhayan Biswas

As iOS developers, we are already aware of managing different environments like Development, QA, Beta, and Production. For these different environments, there are different server URLs, app icons, and configurations.

So before creating a new build pointing to an environment, we need to keep in mind that we also have to change the server URL. We could do this by changing some hardcoded flag value in the constant file or using macros, but it makes everything more complicated.

But if we think for a little while, we can come up with an idea. And by applying this idea, we can easily handle any scenario. So the idea is, if we create different schemas and configurations, then it allows us to change the application server URLs, App icon, Plist file, and configuration.

In this tutorial, I will show you how to manage different environments using schemas and configuration.

These are the steps:

#### **Project Setup:**

Open XCode and create a new single view application with a proper name.

#### **Add Schema and Configurations:**

Before adding a schema, we need to know that every XCode schema comes with two different build configurations: **Debug** and **Release.** Then if we want, we can make changes specific to a particular build configuration.

Now to add our build configurations, select the project in the **Project Navigator** pane on the left. Then select **Info** from the two options (**Info** and **Build Settings)**. In the **Configurations**, we have to add our own configuration for the five environments (Development, Production, QA, Beta, and UAT) there.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5IHSpl7Pm7qdzjJ0VXpO9w.png)
_Add a new configuration for an Environment (Debug and Release)_

First of all, double click on **Debug** and rename it as **Debug (Development).** Similarly, double click on **Release** and rename it as **Release (Development).** Now click +, and select **Duplicate** **Debug (Development)** and **Duplicate Release (Development),** then change the duplicate environment name with the others available names.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ytKEoM7Fp-pi6eXdVde8XA.png)
_After adding all the configurations for different environments_

For the **schema creation**, go to manage schema in top left corner of XCode. There you can see that one schema is already available. Rename it as **Development —** or you can delete the existing and add a new one with the name **Development**. Then add the rest of the four schemas for the other environments.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JVJ5eY0P-wkS2ViI5rj4-w.png)
_Add a new schema for an Environment_

Oops, don’t forget to check the shared box there. After adding all the schemas, the manage schema screen should look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*v_rGZmAYjZe_p4R6usHwTg.png)
_All the schemas are added_

#### Add Configuration Settings File:

Right click on Project, select new file, then add Configuration Settings File and give it the same name as the environment.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EWfTg9WN09lbX8v-KcHDQw.png)
_Configuration Settings File_

After adding all the config files, your Project Navigator left pane should look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*53B3UEp-ZMzRvQdj1EEL-w.png)
_Configuration Files added_

Now the most important part starts: add your **server URL** and other customized key value in the corresponding configuration file.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xECXRXHZGrqvL9ijPLgGiQ.png)
_Server URL added in Configuration File_

#### Add Plist Files:

Rename the info.plist file as development.plist. Copy and paste the same plist file for the different environments inside the project, and rename each of the plist file with the environment’s name. You can set some environment-specific keys and values in the plist files. After that, add the keys from the configuration file to the plist files like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*hMBtu6KdmmIgybiF53dSOw.png)
_Add keys in Plist File_

Now we have to set the appropriate plist path for each build configuration. From Targets, just select a plist file, and rename it with the same name for the **Debug** and **Release** configuration.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eFuPiN80FOC4Y3Ea4G2N1Q.png)
_Add Plist Path for build configuration_

![Image](https://cdn-media-1.freecodecamp.org/images/1*9H2q_Lgql8R7BKyW1sqDww.png)
_Renamed Plist Files_

#### Linking Build Configuration with the Configuration File:

Select all the build configurations (Debug and Release) in **Projects Info** one by one. Then set the appropriate configuration file, which you have added to the project.

![Image](https://cdn-media-1.freecodecamp.org/images/1*W8_auNFU_NRDcsA21Msa0w.png)
_Set Configuration File to Build Configuration_

After adding all the configuration files, your Build settings should look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*sNPBwjaXWmYZSAe_3CdFpw.png)
_Configuration File and Build Configuration_

So we have now successfully linked all the configuration files to the respective build configurations.

#### Linking Schema with the Build Configuration:

Now the last step is linking the schema with the build configuration. To do this, select any schema, go to edit schema, and set the appropriate build configuration there.

![Image](https://cdn-media-1.freecodecamp.org/images/1*o-OY3Yzv7GzmlSs09o2uyA.png)
_Linking Schema and Build Configuration_

#### Ready to Run the Project:

Now all the set up is done. The only thing you have to do select the schema and run — the environment will be automatically selected for you. So for fetching the server URL and other values, I have created an Environment.swift file. Check it out:

To fetch the server URL or other settings in ViewController.Swift or any other file, you have to write only one line of code:

You can also manage different app icons for different environments from build settings. Then, you will only have to look for a second to see which environment build is installed on your device.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GyDczhyCu8IGrR1jlS0Miw.png)

The complete project is available on [GitHub](https://github.com/boudhayan/DemoEnvTest). You can download it if you have any questions.

Don’t spend extra time changing the server URL or some other configuration every time you build your project. This is the easiest way to manage different environments, app icons, and configurations.

If you like this, please don’t forget to give a clap. It will inspire me more. For any suggestions, please feel free to write an email to _mail2boudhayan@gmail.com._

