---
title: How to Sync VS Code Settings Between Multiple Devices and Environments
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-06-16T14:45:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-sync-vs-code-settings-between-multiple-devices-and-environments
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync.jpg
tags:
- name: code
  slug: code
- name: coding
  slug: coding
- name: Developer Tools
  slug: developer-tools
- name: editor
  slug: editor
- name: Productivity
  slug: productivity
- name: programing
  slug: programing
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: tools
  slug: tools
- name: Visual Studio Code
  slug: vscode
seo_title: null
seo_desc: 'All developers like their text editor a certain way, but it can be tough
  to make sure all of your environments have the same configuration. How can we make
  sure our VS Code configuration is the same wherever we use it?


  What is VS Code?

  What will we ...'
---

All developers like their text editor a certain way, but it can be tough to make sure all of your environments have the same configuration. How can we make sure our VS Code configuration is the same wherever we use it?

* [What is VS Code?](#heading-what-is-vs-code)
* [What will we use?](#heading-what-will-we-use)
* [How does it work?](#heading-how-does-it-work)
* [Step 1: Install Settings Sync](#heading-step-1-install-settings-sync)
* [Step 2: Authorize access to Github](#heading-step-2-authorize-access-to-github)
* [Step 3: Upload your current settings](#heading-step-3-upload-your-current-settings)
* [Step 4: Syncing your configuration to another environment](#heading-step-4-syncing-your-configuration-to-another-environment)
* [Step 5: Updating your configuration](#heading-step-5-updating-your-configuration)

%[https://www.youtube.com/watch?v=TR2va67cVkQ]

## What is VS Code?

[Visual Studio Code](https://code.visualstudio.com/), or VS Code, is an all-inclusive code editor that takes all of the features you want out of working with code and puts them in one editor to make you ultra productive.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/visual-studio-code-editor.jpg)
_VS Code editor_

It’s been the “cool kid on the block” for a little while now and has been increasingly growing in popularity at least in the JavaScript community. Microsoft has put a lot of effort into making it something people want to use (and they’re doing a great job at that).

## What will we use?

We’re going to use a VS Code extension called [Settings Sync](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) that makes use of Github’s [Gist](https://gist.github.com/) feature to store a private JSON configuration file in the cloud.

## How does it work?

The extension uses Github’s OAuth to log in to your Github account. Once approved, VS Code obtains an access token and reaches out to both store and download your settings file to a private Github Gist.

Once it’s set up, you can then configure the extension on any other instance of VS Code and immediately download your configuration to sync up your editor.

## Step 0: VS Code

We’ll assume for this walkthrough you have VS Code already installed. While you don’t need to have any special configuration, having something different than the default (like a [color theme](https://code.visualstudio.com/docs/getstarted/themes)) will help you see it work.

Let’s get started!

## Step 1: Install Settings Sync

The first thing we need to do is install the extension. You can do this [a few ways](https://code.visualstudio.com/docs/editor/extension-gallery) — you can visit [the webpage](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync) and hit **Install** which will open up VS Code or you can search for the extension in the Extensions panel.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-1.jpg)
_VS Code Settings Sync extension_

Once installed, it will open up a new tab with the Settings Sync dashboard.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-dashboard.jpg)
_Settings Sync dashboard after installation_

## Step 2: Authorize access to Github

To get started with Github, click the **Login with Github** button in the Settings Sync dashboard.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-login-with-github.jpg)
_Log in to Settings Sync with Github_

This will open up Github in your default web browser and ask you to log in. While you can use any Github account you want, it would probably make most sense to use your personal account.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-login-success.jpg)
_Successful Github login to Settings Sync_

Once you’re logged in, you should now see **Success!** in your browser.

## Step 3: Upload your current settings

Now that you’re connected to Github, you’re ready to upload your settings.

Open up your [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette) with CMD+Shift+P (on Mac) or navigate to View and Command Palette. Type “Sync Upload” which will filter the commands and hit enter once the **Sync: Update/Upload Settings** option is selected.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-upload-update-command.jpg)
_Update/Upload Settings command in Settings Sync_

When doing this, you might be prompted with screen that asks if you want to force upload — press **Yes**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-force-upload.jpg)
_Force upload new settings in Settings Sync_

At this point, Settings Sync will create a new Gist in your Github account with your configuration settings. Once it’s done you should see a success message.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-successful-upload.jpg)
_Successful settings upload in Settings Sync_

You should now be able to visit [gist.github.com](https://gist.github.com/) and find a new private `cloudSettings` Gist that includes all of your VS Code settings!

## Step 4: Syncing your configuration to another environment

To sync your VS Code configuration to another computer or VS Code environment, you want to first follow steps 1 and 2 above — installing the extension and logging in to Github.

The difference is this time, you’ll want to configure VS Code to download your settings instead of upload them.

To get started, first open back up your Sync Settings dashboard. If this is a new installation like we’re assuming here, you can open up the Command Palette and type “sync download” and hit enter which will open up that dashboard. Here, click **Edit Configuration** this time.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-edit-configuration.jpg)
_Edit Settings Sync configuration_

On this screen, you should see your **Github Access Token**, but you should also see an empty field for Gist ID. Here, we want to first grab the ID from our cloudSettings Gist URL:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-github-gist.jpg)
_VS Code cloudSettings Gist ID_

And then paste that value inside of our **Gist ID** input in VS Code.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-gist-id-configuration-1.jpg)
_Adding Gist ID to Settings Sync configuration_

Once it’s there, you can open the Command Palette again, type “sync download”, and hit enter, and Sync Settings will fetch your VS Code configuration from the Gist and update your local settings with that configuration!

## Step 5: Updating your configuration

From here on, any time you want to make a new change to your stored configuration, you’ll want to use both the Update/Upload and Download features like we used above.

To update a new tweak to your configuration, type “sync update”  and hit enter:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-update-settings.jpg)
_Update command for Settings Sync_

And to download your configuration to sync up another editor, type “sync download” and hit enter:

![Image](https://www.freecodecamp.org/news/content/images/2020/06/vs-code-settings-sync-download-command.jpg)
_Download settings command for Settings Sync_

These commands will both update your cloudSettings Gist and download from it to sync up your VS Code instances

## What’s your favorite VS Code trick?

[Share it with me on Twitter!](https://twitter.com/colbyfayock)

## Join the conversation

%[https://twitter.com/colbyfayock/status/1272906851005366274]

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?️ Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

