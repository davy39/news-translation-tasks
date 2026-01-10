---
title: How to set up the debugger for Chrome extension in Visual Studio Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-30T21:38:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-the-debugger-for-chrome-extension-in-visual-studio-code-c0b3e5937c01
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XuUPNSTBAcqzuKXOABL-_w.png
tags:
- name: debugging
  slug: debugging
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Victor A. Requena

  Debugging your web applications with Visual Studio Code makes you more efficient.
  It helps you save a lot of time and keeps your code cleaner. This is because you
  don’t have to write a bunch of console.logs and you can go through...'
---

By Victor A. Requena

Debugging your web applications with Visual Studio Code makes you more efficient. It helps you save a lot of time and keeps your code cleaner. This is because you don’t have to write a bunch of `console.log`s and you can go through your code execution line by line. But if you’re here, you probably know the benefits of debugging web applications. So let’s begin…

### Getting set up

The first thing you need to do is install the [Debugger for Chrome extension](https://marketplace.visualstudio.com/items?itemName=msjsdiag.debugger-for-chrome). After you’ve installed it, you’re almost ready to go. The next thing you need to do is create a launch file for the Visual Studio Code Debugger. This file contains the debugger’s different configurations for your project.

You can create the launch file by going to the debug section in the Activity Bar and clicking the gear icon.

![Image](https://cdn-media-1.freecodecamp.org/images/AUFWFZ8FQncLNTOIsD2at38qFq0GQOWErXm0)
_This gear icon._

A list of options will prompt you to select the “Chrome” one.

![Image](https://cdn-media-1.freecodecamp.org/images/gV9J3xLjSklXcHaK4QdXWXzkkf1t84eh5OFO)
_Like this._

After you’ve done this, you’re going to have a `.vscode` directory with a `launch.json` file.

### Configurations

There are two kinds of Chrome debugging configurations: `launch` and `attach`. You can set this in the `request` option inside every configuration object.

#### Launch

The launch configuration _launches_ a Chrome instance running a specified file or URL. If you specify a URL, you have to set `webRoot` to the directory that files are served from. This can be either an absolute path or a path using the `${workspaceFolder}` resolver. This is the folder opened in your Visual Studio Code workspace.

_Note: Be careful while setting `webRoot`, this is used to resolve URLs to a file on your computer._

You can see an example of two `launch` configurations: One launching against a local server and the other launching against a local file.

If you have a Chrome instance running, the one launched by the debugger will use a temporary session. This means that you won’t have your extensions or opened tabs. If you want to launch a Chrome instance with your user and extensions, you have to close every running instance first.

_Note: When you stop the debugger, this will close the Chrome window._

#### Attach

I personally prefer using this one… This configuration attaches the debugger to a running instance of Chrome. But in order for this option to work, you need to launch Chrome with remote debugging enabled. Launching a Chrome instance with remote debugging varies depending on your OS.

#### Windows

There are two ways to launch Chrome with remote debugging in Windows. The simplest one is to right-click on the Google Chrome shortcut. Select the properties option and append the following command in the _target_ field.

```
--remote-debugging-port=9222
```

_Note: This will launch Chrome with remote debugging enabled every time you click on the shortcut._

The other way is to open the command prompt and execute this command replacing the `<chrome_pa`th> with the actual location of your Chrome installation.

```
<chrome_path>\chrome.exe --remote-debugging-port=9222
```

#### macOS

Open the terminal and execute the following command:

```
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
```

#### Linux

Launch your terminal and run this command:

```
google-chrome --remote-debugging-port=9222
```

What this does — no matter what OS — is open Chrome with a flag, in this case: `--remote-debugging-port`, and sets it to `9222`. You can read more about this [here](https://www.chromium.org/developers/how-tos/run-chromium-with-flags).

_Note: If you have other Chrome instances running with no remote debugging, make sure to close them before launching a new one._

Here’s a sample `attach` configuration.

_Note: If you do not set the `"url"` option, a list will be prompted with your open tabs._

This extension have a lot of very useful options that you can use to adapt the configurations to your project. You can read the documentation of some of them [here](https://github.com/Microsoft/vscode-chrome-debug#other-optional-launch-config-fields).

#### Summary

Congratulations! You’ve learned how to install and set up the debugger for Chrome in Visual Studio Code. You also learned how to launch Google Chrome with remote debugging enabled. Now it’s time for you to explore and expand your new knowledge… I highly recommend you to take a look at the extension’s [repository](https://github.com/Microsoft/vscode-chrome-debug).

I hope you enjoyed this post. You can find me on Twitter [@_svictoreq](https://twitter.com/_svictoreq). ?

