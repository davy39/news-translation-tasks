---
title: How to Use Google Sheets – A Beginner's Guide
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-07-25T17:53:57.000Z'
originalURL: https://freecodecamp.org/news/google-sheets-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/maxresdefault.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: google sheets
  slug: google-sheets
- name: spreadsheets
  slug: spreadsheets
seo_title: null
seo_desc: 'Google Sheets is an online spreadsheet app with real-time collaboration
  features. It''s like Microsoft Excel for regular people. 🙌


  gif of guy saying aren''t ordinary people adorable

  And, these days, it''s actually giving Excel a run for its money. It''...'
---

Google Sheets is an online spreadsheet app with real-time collaboration features. It's like Microsoft Excel for regular people. 🙌

![Image](https://www.freecodecamp.org/news/content/images/2023/07/ordinary.gif)
_gif of guy saying aren't ordinary people adorable_

And, these days, it's actually giving Excel a run for its money. It's picked up a lot of features and processing power over the years that used to be exclusive to Excel.

But we're here to talk about the basics today.

🧾I'm going to cover:

1. How to create new Google Sheets
2. Intro to Templates
3. Menu and toolbar overview
4. Basic data entry and calculations
5. Basic formatting
6. How to create a table
7. How to sort and filter data
8. Intro to formulas and functions

## Video Walkthrough

I've made a video walkthrough of the things we'll be covering in this article. You can check it out below:

%[https://youtu.be/_bvRa7T-59U]

## How to Create a New Sheet

Spreadsheets can be intimidating even in their most basic form. 

Don't be scared, though.👇 

To use Google Sheets, you need a free Google account. (If you're using Gmail, you already have this.) Go [here](https://www.google.com/sheets/about/) to sign up if you don't have one yet.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-141.png)
_pic of the Google Sheets homepage_

Go ahead and go to [sheets.new](https://sheets.new) to create a brand new Google Sheet. It will also prompt you to sign up if you don't have an account yet. 

 💥This is what you'll see:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-138.png)
_pic of a blank spreadsheet_

😓Some of you may already have begun perspiring because a spreadsheet looks like an unapproachable blank slate reserved for data analysts, financial gurus, and overly ambitious content creators. 

![Image](https://www.freecodecamp.org/news/content/images/2023/07/sweat.gif)
_gif of man stressing out_

💪Fear not. 

A spreadsheet, and particularly a Google Sheet, is ripe with possibilities for the average person.

You can use them to enhance productivity after learning only a few basic things. 

📊A spreadsheet is a **big grid** made up of **columns labeled with letters** and **rows labeled with numbers**. Each of the rectangles of the grid are called a **cell**, and the active cell is the one with the blue outline. 

If you start typing, whatever you type will appear in the active cell.

The cells can contain numbers, words, formulas, dates, pretty much anything...

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-140.png)
_pic of spreadsheet cell_

## Google Sheets Templates

Google has supplied us with a respectable amount of templates to get started with. 

I will not be covering these in any detail because it's important to get the basics down first. I just want you to be aware of them if you need a starting point **after** you've gotten comfortable with Sheets. 

You can look through the template gallery [here](https://docs.google.com/spreadsheets/u/0/?ftv=1).

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-142.png)
_pic of Google Sheets templates_

## Menu and Toolbar Overview

![Image](https://www.freecodecamp.org/news/content/images/2023/07/menus.png)
_pic of Google Sheets menu and toolbar_

You will likely be familiar with the menu and toolbar setup. As with most modern applications, they are at the top of the page. The menu has many familiar options like File, Edit, View, Insert, and so on. And the toolbar below it consists of mostly icons related to formatting and text options.

The **File** menu has options to share, download, copy, import, rename and other such things related to the whole spreadsheet.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-144.png)
_pic of file menu_

**Edit** and **View** have familiar options regarding copy/paste and choosing different levels of visibility for your spreadsheet.

**Insert** gives us a host of options of things to import into our sheet like charts, pivot tables, checkboxes, emojis, dropdown lists, and many more.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-145.png)
_pic of insert menu_

**🎨Format** contains many options for formatting our sheet. We can add color, borders, tables styles, and more from here.

The **Data** menu has a lot of spreadsheet specific functions. It contains shortcuts to sort and filter data, to protect different ranges of cells, to group ranges together by naming them, data validation, and advanced items like connecting data sources.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-146.png)
_pic of the Data menu in Google Sheets_

Tools and Extensions will be lesser used menus, at least in the beginning. But some really exciting stuff is possible by leveraging the power of **Google Apps Script** through the Extensions menu. This lets us write programs in a language similar to JavaScript all while in a spreadsheet.

But, that's for later – or check out some of my other [videos](https://www.youtube.com/@eamonncottrell) and [articles](https://www.freecodecamp.org/news/author/eamonn) to get a taste of Apps Script.

## Basic Data Entry and Calculations

What is data? According to my Google search, data are "facts and statistics collected together for reference or analysis."

Spreadsheets thrive on data. Yes, think numbers, dates, percentages...things that are easily calculable.

In Google Sheets, we can enter in some data. Say, a list of names, dollar amounts, and dates. 

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-150.png)
_pic of some data_

Now, we have a simple list of data. Because it's small, we can scan it and analyze it ourselves pretty easily. 

1. We can see that it's ordered by date
2. We can see that Paul either has or owes the most
3. We can see that Sara either has or owes the least

But imagine this is a list of thousands of records (each row of an amount, a name, and a date can be referred to as one record).

Suddenly it gets a lot harder to analyze or make sense of the data. 

Then add a dozen or a hundred more columns of data for each record. It becomes virtually impossible for a human to draw anything meaningful from the data without the help of a spreadsheet or computer program.

Next, we'll see how some organization and simple spreadsheet operations can help us draw insights from our data.👇

![Image](https://www.freecodecamp.org/news/content/images/2023/07/easy.gif)
_gif of woman saying this is so easy_

## Basic Formatting

Highlight the table. You can do this by clicking and dragging across the whole range of cells. Now, you should have an active **range** instead of an active **cell**:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-151.png)
_pic of Google Sheets table_

Take a moment and click through some of the formatting options on the toolbar. I've changed the text, the font size, and then made bold the first header row. 

I've also highlighted only the dollar amounts, and changed their format to **currency** instead of just a number.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/menus-1.png)
_pic of Google Sheets formatting_

Already, the information is a little more readable. In the next steps we will go further.👇

![Image](https://www.freecodecamp.org/news/content/images/2023/07/rabbit-hole.gif)
_gif of Alice falling down rabbit hole_

## How to Create a Table in Sheets

Alas, we don't (yet) have a swift shortcut like Excel does to make a table. But if we highlight our data again, and select **Format -> Alternating Colors** from the toolbar, we can create table formatting for enhanced readability.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-153.png)
_pic of Alternating Colors table style in Google Sheets_

Now, we have banded rows of alternating colors. This becomes very useful in large data sets, but is equally pleasing in our small example. Once satisfied with your color selections, click done.

Now, if we add rows of data to the bottom of our table, Google Sheets is smart enough to know that we probably want to extend the table downward. It will extend the alternating color formatting as we add two more lines:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-154.png)
_pic of extended Google Sheets table_

## How to Sort Data with a Filter in Sheets

Tables are useful because, with some small steps, we can sort and filter data in ways that make it easier to draw conclusions or extract meaning from our data.

Click anywhere in the range of data, and select **Data -> Create a filter** from the Menu bar.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-155.png)
_pic of creating a filter in Google Sheets_

Again, Google Sheets knows to create a filter for the entire data set, and you can see two things visually represented: 

1. The rows and columns of the data set are now given a highlight color to show that a filter has been applied.
2. To the right of each header label, there are three horizontal lines that look like an upside-down pyramid. These are the filters.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-156.png)
_pic of filter on a Google Sheets table_

From here, we can both sort and/or filter our data. If we sort, for instance, Z -> A, we can display each row from highest to lowest dollar amount.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-157.png)
_sorted table_

If we click the data column's pyramid, we can see that for filtering options, we can either filter by condition or by value.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-158.png)
_pic of filtering options in Google Sheets_

Filtering by **values** lets us toggle on or off certain dates. Filtering by **condition** allows for all sorts of options. We can choose dates that are before or after certain dates. 

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-159.png)
_pic of filter options in Google Sheets_

Or we can select "Is between" and then write in a period of dates we want to filter for.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-161.png)
_pic of filter options in Google Sheets_

This becomes immensely helpful to narrow down a field of results for analysis. Now we can focus on only the subset of filtered results.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-162.png)

## Intro to Formulas and Functions

The final piece we'll touch on is the ability to **write formulas** and **use functions**.

### Formulas in Google Sheets

Formulas are instructions we manually type into a cell to manipulate data. If we wanted to add the values in cells A16 and A17, we could write a formula that did this like so: `=A16+A17`.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-163.png)
_pic of a formula in Google Sheets_

We can do basic math very easily like this, but there's an even better way to do this by using functions.

### Functions in Google Sheets

Functions are built-in formulas that we use by typing their name. Again, we start out by typing the equals sign, but then we type the name of the function, in this case SUM: `=SUM(A16:A17)`.

When we begin typing a function, a tooltip will pop up giving us options for the different functions available. You can hit the TAB key to select a function, click one from the list, or complete the spelling of the function and type an open parentheses to select a function.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-165.png)
_pic of available functions in Google Sheets_

Once selected, the tooltip will display helper text about that function in case we need an explanation of what it does and/or the variables it needs:

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-164.png)
_pic of the SUM function in Google Sheets_

These are straightforward examples of adding numbers, but there are over 400 built-in functions that range greatly in complexity. 

## What's Next?

As you've probably figured out, this barely scratches the surface of Google Sheets. Once you're comfortable with the basics, it's time to dive deeper and use Sheets to solve some problems of your own.

Check out the templates I've linked above for inspiration, spin up a personal finance tracker, make a workout calendar, track stock prices, build a cost of goods sheet for a small business, build an amortization sheet to see if you can afford a house, track your time with a project management sheet...the possibilities are vast.

🔗Check out my [YouTube channel](https://www.youtube.com/@eamonncottrell) and [newsletter](https://got-sheet.beehiiv.com/subscribe) for more Sheets content and projects.

🔗Connect with me on [LinkedIn](https://www.linkedin.com/in/eamonncottrell/).

Hope you have a great one!

![Image](https://www.freecodecamp.org/news/content/images/2023/07/bye-gosling.gif)
_gif of Gosling waving bye_


