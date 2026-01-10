---
title: How to Code Dark Mode for Google Sheets with Apps Script and JavaScript
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-09-20T22:23:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-code-dark-mode-for-google-sheets
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/code-your-own-dark-mode.png
tags:
- name: dark mode
  slug: dark-mode
- name: google apps script
  slug: google-apps-script
- name: google sheets
  slug: google-sheets
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: "Google Sheets is a great tool for working and collaborating on spreadsheets,\
  \ but it doesn't have native support for dark mode. \nIn this article, we'll create\
  \ our own dark mode. One way to do that would be by selecting all the cells and\
  \ manually chang..."
---

Google Sheets is a great tool for working and collaborating on spreadsheets, but it doesn't have native support for dark mode. 

In this article, we'll create our own dark mode. One way to do that would be by selecting all the cells and manually changing their background color and font color. This will get the job done, but we can automate the process and add more style options to choose from.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/automate-2.gif)
_gif of cartoon character grabbing a computer_

Here’s what we’ll build: a style selector that has four different styles triggered by either a new dropdown menu or by clicking a custom button icon.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/1-12.png)
_screenshot of Google Sheets with different background modes_

And here's the video walkthrough if you'd like to follow along with that instead: 

%[https://youtu.be/TxSGuXPav70]

## How to Create Dark Mode in Apps Script

We’ll create four functions, one for each style mode. Each of our functions will do the following:

1. Set background color
2. Set font color
3. Set font family
4. Set border color and style

Let’s walk through how to create a `darkMode` function in [Apps Script](https://script.google.com/home/start). We'll define each function with the `function` keyword, followed by whatever we’ll name it.

Because the functions take no arguments (they just run without needing more info from us). That is, we have open and closed parentheses with nothing inside them followed by an open curly brace.

All of our code for the function goes between the `darkMode` function's curly braces:

```javascript
function darkMode() {
  SpreadsheetApp.getActive().getRange('A1:Z')
    .setBackground("#333333")
    .setFontColor("white")
    .setFontFamily("Google Sans")
    .setBorder(false,false,false,false,true,
     true,"#444444",SpreadsheetApp.BorderStyle.SOLID)
}
```

To select all the cells, we used the built-in methods from the `SpreadsheetApp` class: `getActive()` and `getRange()`. These select the active sheet as well as a given range.

In our case, we’ll plug in `A1:Z` as the range, but you can extend this further if you’d like. For instance,  `A1:AZ`, would add columns `AA:AZ` and then apply our styling to them.

The four lines that follow are simply dot notation extensions telling what styles to apply. You can write this on one line if you’d like, but it’s good practice to have line breaks to make the code easy to read.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/clever.gif)
_gif of man saying, that’s clever_

## How to Set Colors and Fonts

You'd notice that we used both `setBackground(#333333)` and `setFontColor("white")` in the code. This is because we can use CSS notation colors in either hex format or by using the color’s name.

Using `setFontFamily("Google Sans")`, we gave it the font family name within quotations. Being a Google product, you can use any of the [Google Fonts](https://fonts.google.com/) as well as Google’s own Google Sans font as I found out making this project.

## How to set the Border

The `setBorder(false,false,false,false,true, true,"#444444",SpreadsheetApp.BorderStyle.SOLID)` function let’s you enter `true` or `false` values for the top, left, bottom, right, vertical, or horizontal borders, in that order, followed by the color and style.

To set the style, we had to invoke a built in [Enum Attribute](https://developers.google.com/apps-script/reference/document/attribute) — `BorderStyle` — to change the style of the border.

## How to Create the Style Menu

To be able to select any of the styles we’re making from the actual spreadsheet, we need a menu.

To add the menu, we'll create a new function called  `onOpen()` that runs as soon as the spreadsheet opens and then the built-in methods from the `getUi()` to build our custom menu.

We can create the menu with `.createMenu()` and then add each of our functions to the menu with the `addItem()` function.

Here's the code:

```javascript
function onOpen(){
  SpreadsheetApp.getUi()
    .createMenu('Style')
    .addItem("Dark","darkMode")
    .addItem("Papyrus","papyrusMode")
    .addItem("Light","lightMode")
    .addItem("Synth","synthMode")
    .addToUi();
}
```

Google Apps Script automatically integrates with Google Workspace apps (like Google Sheets) so the functions we've added in the code will make the functionalities accessible in your Google Sheets.

## How to Add Icon Buttons

As a bonus, I added four icon images to the sheet, and by selecting `Assign script` we can have these icons act as buttons to trigger any of the four styles we’ve built:

![Image](https://www.freecodecamp.org/news/content/images/2023/09/2.png)
_screenshot of icons in spreadsheet_

When you type the function name into the Assign script dialog box, make sure you do not to use parentheses. You should only enter the name of the function itself:

![Image](https://www.freecodecamp.org/news/content/images/2023/09/3.png)
_screenshot of assigning script to image_

And bingo! We’ve got ourselves a style picker. You can add or edit these to create any number of combinations that you can easily toggle on and off in your own Google Sheet!

![Image](https://www.freecodecamp.org/news/content/images/2023/09/4.png)
_screenshot of Synth Mode Style_

## Conclusion

This article shows how you can create can code dark, and other background modes for your Google Sheets using Apps Script and JavaScript.

I hope this has been useful for you!

## More Resources😄

▶ Find all my video tutorials and walkthroughs on YouTube: [https://www.youtube.com/@eamonncottrell?sub_confirmation=1](https://www.youtube.com/@eamonncottrell?sub_confirmation=1)

▶ Connect with me on LinkedIn where I share daily tips: [https://www.linkedin.com/in/eamonncottrell/](https://www.linkedin.com/in/eamonncottrell/)

