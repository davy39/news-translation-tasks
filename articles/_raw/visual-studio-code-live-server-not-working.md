---
title: Visual Studio Code Live Server Not Working
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-14T09:28:00.000Z'
originalURL: https://freecodecamp.org/news/visual-studio-code-live-server-not-working
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9941740569d1a4ca1eab.jpg
tags:
- name: Browsers
  slug: browsers
- name: Google Chrome
  slug: chrome
- name: Visual Studio Code
  slug: visual-studio-code
- name: Visual Studio Code
  slug: vscode
seo_title: null
seo_desc: "VSCode has a lot of great extensions, and Live Server is one of the best.\
  \ \nWith just a couple of clicks, Live Server lets you see your page live in an\
  \ actual browser. Better yet, it features live reloading, so if you update your\
  \ code, the changes are..."
---

VSCode has a lot of great extensions, and [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) is one of the best. 

With just a couple of clicks, Live Server lets you see your page live in an actual browser. Better yet, it features live reloading, so if you update your code, the changes are also reflected in the browser.

All you have to do is right click in the HTML file you want to view, right click, then select "Open with Live Server":

![Image](https://www.freecodecamp.org/news/content/images/2020/09/live-server-ex.gif)
_Live Server in action_

But what if Live Server doesn't open your browser and show your page like you expect? If this is happening to you, here are a few things you can try.

## Restart VSCode

Sometimes the best you can do is start VSCode from scratch.

First, save all of your work. Then close VSCode, which will also stop all of the extensions you've installed.

Then, reopen VSCode and try again – go to the HTML file you want to view, right click, and select "Open with Live Server".

## Set the browser for Live Server

It's possible that the extension is working, but your system doesn't have a default browser.

Even if you did set the default browser for your system, it wouldn't hurt to let Live Server know which browser you'd like to use explicitly.

First, open the Command Pallete with F1, then type in `Preferences: Open Settings (JSON)` and select that option.

This will open your VSCode `settings.json` file.

Scroll all the way to the bottom of the file, add a comma after the last setting, then paste in `"liveServer.settings.CustomBrowser": "chrome"`:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/settings-json.gif)

Note that you can also use `"firefox"`, `"safari"`, or any other browser as the value for the `"liveServer.settings.CustomBrowser"` setting.

Finally, save the `settings.json` file and try to run Live Server again.

## Set the default browser for your operating system

Even after telling Live Server which browser you want to use, it's possible that it's still not opening your page in that browser correctly.

The next thing to try is to set the default browser for your operating system itself.

The exact method for doing this can vary based on your operating system, so it's best to search for how to do this if you aren't sure.

Here's what the settings page looks like in Windows:

![Image](https://www.freecodecamp.org/news/content/images/2020/09/image-56.png)
_Credit: [Advitya-sharma](https://forum.freecodecamp.org/u/Advitya-sharma)_

## Go to the live page yourself

If for some reason Live Server still isn't opening the page in your browser automatically, no worries. You can always open the browser of your choice and view the page directly.

Just open your preferred browser and go to `http://127.0.0.1:5500/<your_file_name>`.

For example, if your file is called `index.html`, just go to `http://127.0.0.1:5500/index.html`.

As long as Live Server is running, you should see your page.

## In closing

Those are a few common fixes you can try if Live Server isn't working the way you expect.

Stay safe, and happy (live) coding.

