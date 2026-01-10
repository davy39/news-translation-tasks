---
title: How to Create Custom Named Functions in Google Sheets
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-03-13T17:56:24.000Z'
originalURL: https://freecodecamp.org/news/google-sheets-how-to-create-custom-named-functions
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/fCC-thumbp.jpg
tags:
- name: google sheets
  slug: google-sheets
- name: spreadsheets
  slug: spreadsheets
seo_title: null
seo_desc: "There are 513 built-in functions in Google Sheets at the time of this writing.\
  \ But what if you needed a custom function that wasn't included? \nIn this tutorial,\
  \ I'll show you how to create and use your own custom function in Google Sheets.\n\
  Why would ..."
---

There are 513 built-in functions in Google Sheets at the time of this writing. But what if you needed a custom function that wasn't included? 

In this tutorial, I'll show you how to create and use your own custom function in Google Sheets.

Why would you need a custom function? There could be many reasons. It could minimize typing if you have a lot of instances where you need a few things calculated. It can tidy up an otherwise messy arrangement of manually typed formulas. You may just want to flex your spreadsheet muscles.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/custom.gif)
_gif of woman saying "this is custom"_

I'll walk through a simple example below where we find the percent change between two numbers. I've written extensively about 5 ways to do this particular exercise in another post [here](https://www.freecodecamp.org/news/how-to-calculate-percentage-differences-between-two-numbers-in-excel-cell-percentage-change-tutorial/).

## Percent Change Example

First, here's a video walkthrough of creating custom named functions if you'd like to see a live demonstration.

[Here's the demo spreadsheet](https://docs.google.com/spreadsheets/d/1pubmIp-4VmcHpQJXibxU1Astl6lgH2qZEN3Ry1S7i6Q/edit#gid=337119202). 

%[https://youtu.be/UmzAdZnVRy0]

To find the percent change between two numbers, we need to make a simple calculation by dividing the difference between them by the first number. 

If we have the following table of sales data in columns E, F and G, we can find the percent change between the years 1 and 2 by manually writing the formula `(F7-E7)/E7`. And in the same way for years 2 to 3 by writing `(G7-F7)/F7`.

<table><tbody><tr><td>year 1 </td><td>year 2</td><td>                  year 3</td></tr><tr><td>$180,000.00</td><td>$200,088.00</td><td>$340,000.00</td></tr><tr><td>$180,000.00</td><td>$200,088.00</td><td>$340,000.00</td></tr></tbody></table>

This is fine and good. But, Google Sheets allows for custom functions that we can define once and then use without having to manually type as much. For this example, it's quite simple, but for more complex formulas, it can save a lot of time and mistakes.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/image-97.png)
_Google Sheets Screenshot_

## How to Create a Custom Named Function

To access named functions, click `Data, Named functions` from the toolbar.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-10-at-7.51.03-PM.png)
_screenshot of data menu and named functions option_

Select `Add new function` from the bottom:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-10-at-7.52.24-PM.png)
_Screenshot of adding a new function_

And from here we can fill in the details of our new function starting with the name and the description:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-10-at-7.53.03-PM-1.png)
_Screenshot of name of named function_

Next we have optional argument placeholders. For our function, we need two of these: one for each year.

Then we fill in the actual formula definition. This is where we describe what we need the formula to do. We use the argument placeholders like variables instead of the specific cell references:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-10-at-7.53.14-PM.png)
_screenshot of arguments and formula definition_

And in the final menu we can add additional details describing and giving examples of our arguments. This can be as detailed or sparse as need be. In our case, I filled in only the bare minimum:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-10-at-7.53.34-PM.png)
_Screenshot of argument details in custom named function_

Check it out! Now we have a working custom named function to find the percent change between two numbers. Instead of having to enter the whole formula, now we just enter the cells for `year1` and `year2`:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-10-at-8.16.52-PM.png)
_Screenshot of custom named function_

## Summary

The built in functions in Google Sheets can take you far, but if you ever have the need to define a unique function of your own, now you can. 

I hope this has been helpful for you!

Please check out my [YouTube channel here](https://www.youtube.com/@eamonncottrell?sub_confirmation=1) & [LinkedIn page here](https://www.linkedin.com/in/eamonncottrell/).

Have a great one!

