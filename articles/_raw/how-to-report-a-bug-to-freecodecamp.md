---
title: How to Report a Bug to freeCodeCamp
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-03T21:07:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-report-a-bug-to-freecodecamp
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-pixabay-144243.jpg
tags:
- name: bugs
  slug: bugs
- name: debugging
  slug: debugging
- name: freeCodeCamp.org
  slug: freecodecamp
- name: GitHub
  slug: github
- name: learn to code
  slug: learn-to-code
seo_title: null
seo_desc: 'Thank you for taking the time to report an issue with freeCodeCamp.

  If you think you’ve found a bug on freeCodeCamp, please follow these steps to resolve
  your problem:

  Reset the Code in the Editor

  Try resetting the code in the editor using the reset ...'
---

Thank you for taking the time to report an issue with freeCodeCamp.

If you think you’ve found a bug on freeCodeCamp, please follow these steps to resolve your problem:

## Reset the Code in the Editor

Try resetting the code in the editor using the reset button on the page. This will solve most of the issues if somehow you changed some code that is affecting the challenge in some way. 

Resetting clears the code to its original state as it was when the challenge was first presented to you.

## Use a Coding Keyboard or the App on Mobile

Try reading this article about [How to use freeCodeCamp on a mobile phone](https://www.freecodecamp.org/news/freecodecamp-mobile/). Or if you are using an Android device, check if the [freeCodeCamp App](https://play.google.com/store/apps/details?id=org.freecodecamp&gl=US) has the feature you are wanting to use.

## Do a Hard Refresh

If the page seems broken in any way, try to do a Hard Refresh of the page. This will update any old code that may have been cached in your browser. 

If the freeCodeCamp website was recently deployed, and the issues come from that, this will be enough to fix it.

### How to do an Hard Refresh

While on the problematic page, use the key combination below to trigger a hard refresh depending on your operating system:

* Windows: `CTRL + F5`
* Mac/Apple: `Apple + Shift + R or Command + Shift + R`
* Linux: `F5`

To learn more about this read: [http://refreshyourcache.com/en/cache/ 73](http://refreshyourcache.com/en/cache/)

## Try Clearing Your Browser's Local Storage

Removing all your locally stored challenges will solve many problems related to the browser crashing on freeCodeCamp

### In Chrome:

* On freecodecamp.org open your console
* Windows: `Ctrl` + `Shift` + `J`
* Mac OS: `Cmd` + `Opt` + `J`
* Go to resources tab (Chrome).
* There, click on the “Local Storage” link in the nav bar on the right.
* Delete all the entries on the right side, or run this command in your browser’s console to clear all entries from your localStorage: `localStorage.clear();`
* See if this solves your issue

### How to remove a single challenge from Local Storage

Maybe you don't want to lose the code from other challenges or something like that. This method will remove only the problematic challenge from your browser's Local Storage.

#### In Chrome:

* On  **freecodecamp.org**, open your developer tools.
* More tools > Developer tools (or  `Ctrl`  +  `Shift`  +  `I`  (Windows),  `Cmd`  +  `Opt`  +  `I`  (Mac))
* Navigate to the  `Resources`  tab
* Expand the  `Local Storage` item in the left pane
* Select  `http://www.freecodecamp.org`
* Find the challenge for which you wish to delete data in the right pane
* Right click the desired challenge and select `Delete`

#### In Firefox:

* On  **freecodecamp.org**, open your web console with
* `Ctrl`  +  `Shift`  +  `K`
* From there, using directly the console:
* Type  `console.log(localStorage);`  and hit  `Enter` .
* Click in  `Storage`  link.
* The  **Storage**  panel will appear at right.
* Filter the results to find the Algorithm, Front End Project or Challenge causing the problem.
* When located, mouse over it and click the  `x`  at right.
* Once removed, check if the problem was solved. Refresh or close and open the browser if necessary.

**Note:**  This can also be done with the [Storage Inspector](https://developer.mozilla.org/en-US/docs/Tools/Storage_Inspector), but seems like Firefox hangs out when there are so many values.

## Check if the issue is caused by one of your browser extensions

Try deactivating your browser extensions, or try to open the page in your browser private mode.

If in this way the issue is fixed, you will need to put in an exception for freeCodeCamp in the guilty extension, or keep it switched off while you are using the freeCodeCamp website.

## Read the Support FAQs

The [support FAQs](https://www.freecodecamp.org/news/support) offer solutions for many common issues. Try reading through that article if the steps above didn't work or were not related to your issue.

## Ask for Help on the Forum

You may have arrived here and still have your issue. Now it's time to ask for help from other humans. 

[Open a topic on the forum describing your issue](http://forum.freecodecamp.com/). Try to give as much info as possible, including your code and the challenge link, or the link to the page affected, and your operating system (if you are on a challenge, you can use the "Ask for help" button to create a precompiled post with these issues already included, to which you can add your description of the issue and eventual screenshots). 

There may be something going on with your code, or there may be a briefly occurring issue with freeCodeCamp in general.

### How to format code on the Forum

When you enter a code block into a forum post, precede it with a separate line of three backticks and follow it with a separate line of three backticks to make it easier to read.

You can also use the “preformatted text” tool in the editor (`</>`) to add backticks around text.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/Pre-formatted-text.gif)

## Create an Issue on GitHub

The forum may be able to help you, or may send you to GitHub.

Before creating a new issue on GitHub, try searching around the existing issues to see if someone has already reported something similar.

### How to search an issue on GitHub

1. Go to freeCodeCamp’s [Github Issues](https://github.com/FreeCodeCamp/FreeCodeCamp/issues) page.
2. Use the search bar to search for already filed issues that may be related to your problem.
3. If you find one, read it! You can subscribe to get updates about that specific issue by clicking on `Subscribe` in the sidebar. You can add a reaction on the posts that best describe your issue, or you can also comment on the issue if you have something to add.
4. If you cannot find any relevant issues you should create a new GitHub Issue.

### How to create a new Issue on GitHub

**IMPORTANT:**  
Before you report a new issue always get a third party confirmation from someone in the chat rooms or the forum. Remember that the issue tracker is strictly for reporting bugs or enhancements, it’s not a place to seek any help with solving the challenges.

Crafting a good issue will make it much easier for the dev team to replicate and resolve your problem. Follow these steps to do it right:

* Go to freeCodeCamp's [GitHub Issues](https://github.com/FreeCodeCamp/FreeCodeCamp/issues) page and click on  `New Issue` .
* Select the correct Issue type from the list

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-19.png)

* **Have a useful title.** Write a meaningful title that describes the issue. Some good examples are  `Logging in from the News and Field Guide pages doesn't redirect properly (using e-mail)`  and  `Typo: "for" instead of "while" loop`; bad examples include  `A bug, HELP!!!11`  and  `I found this bug in a Challenge` .
* Keep the title relatively short, as the description is for further information. One example is to shorten long Challenge names, so instead of writing  `Test case bug in 'Challenge: Check Radio Buttons and Checkboxes by Default'` , you might want to write  `Test case bug in 'Radio Buttons' Challenge` .
* In the body,  **provide a link** to the page on which you encountered this issue.
* **Describe the problem** and **provide steps** so that a developer can try to replicate the issue. Include your operating system and browser version. When referencing other issues or pull requests, simply write #issue/pr-number.
* Paste in any relevant code using proper code formatting
* **Take a screenshot** of the issue and include it in the post.
* Click `Submit New Issue` and you are done! You will be automatically subscribed to notifications for any updates or future comments.

### How to format the code on GitHub

You need to use three backticks ``` before your code block, and three backticks ``` after your code block.

You can also select your code block and use the button "Add code" in the GitHub editor.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-11.png)

In this way your code will be formatted and more legible.

Resources compiled and edited by Ilenia Magoni, freeCodeCamp author and Italian localization and community leader.

