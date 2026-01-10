---
title: Give your workday super-powers with Google Apps Script
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-08T17:59:09.000Z'
originalURL: https://freecodecamp.org/news/automate-your-workday-with-google-app-script
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca228740569d1a4ca52e9.jpg
tags:
- name: automation
  slug: automation
- name: google apps script
  slug: google-apps-script
- name: JavaScript
  slug: javascript
- name: work life balance
  slug: work-life-balance
seo_title: null
seo_desc: 'By Peter Gleeson

  The best learn-to-code projects are often those which solve a real world problem.

  These projects can provide that extra dose of motivation so essential to finishing
  any project. They encourage you to actively explore and discover new...'
---

By Peter Gleeson

The best learn-to-code projects are often those which solve a real world problem.

These projects can provide that extra dose of motivation so essential to finishing any project. They encourage you to actively explore and discover new concepts, rather than imitate examples you've seen before.

There's also something that bit extra satisfying about solving a problem you face day-to-day.

An easy way to start is with [Google Apps Script](https://developers.google.com/apps-script/).

It is a scripting language for a range of Google applications. The language itself is in fact JavaScript.

What Google Apps Script provides are libraries and classes that allow you to work with objects such as spreadsheets, emails, calendars, slides, and more.

If you want to dive right in, the documentation is available [here](https://developers.google.com/apps-script/reference/).

Here are three examples that will show how to get started with Google Apps Script. Hopefully it will give you some ideas for your own projects!

### Launching Google Apps Script

You will need a Google account to start developing Apps Script projects. To start a new project, simply navigate to [script.google.com/home](https://script.google.com/home) and click 'New Script'.

You will be taken to an in-browser IDE that looks something like this:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-18.40.56.png)

Give your project a name by changing the title in the top left corner.

Note that every time you require Apps Script to access different Google applications, you will need to give the necessary permissions.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-17.34.16.png)

This might look a bit daunting, but if you are running your own project carefully, there will be no problem. Click "Advanced" and allow your project permission to run.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-17.34.42.png)

Let's take a look at some examples.

### Calculate your income tax

This simple example will show you how to extend [Google Sheets](https://www.google.com/sheets/about/) by adding your own custom formulae. In this example, the formula will be used to calculate UK income tax.

In the UK, [different income tax rates](https://www.gov.uk/income-tax-rates) are applied to different earnings categories. Therefore, the amount of income tax owed varies depending on the income.

First, create a new [Google Sheet](https://docs.google.com/spreadsheets/u/0/). Then, from the menu ribbon, select Tools > Script editor. You will be taken to the Apps Script IDE.

The code block below uses a [switch statement](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/basic-javascript/selecting-from-many-options-with-switch-statements/) to calculate the right amount of tax for a numerical argument `income`. If you are familiar with JavaScript, you will recognise the syntax.

```javascript
function TAX(income) {
  
  switch (true) {
      
    case income <= 12500:
      var tax = 0;
      break;
    case income <= 50000:
      var tax = 0.2 * (income - 12500);
      break;
    case income <= 150000:
      var tax = 7500 + (0.4 * (income - 50000));
      break;
    case income > 150000:
      var tax = 47500 + (0.45 * (income - 150000));
      break;
    default:
      var tax = "ERROR";
  }
  
  return tax;
  
}
```

Save your project if you haven't already.

Now, back in the sheet, enter your chosen salary in e.g., cell A1. You can now call the new formula with  `=TAX(A1)`.

You could write a similar function to calculate [UK National Insurance contributions](https://www.which.co.uk/money/tax/national-insurance/national-insurance-rates-ajg9u9p48f2f#headline_3).

What other Sheets functions could you write?

### Remember to check your emails

It can be difficult to make time to respond to important emails. This example will bring together [Gmail](https://www.google.com/gmail/) and [Google Calendar](https://calendar.google.com/calendar/r) in one short application.

The idea is simple. You provide a list of important email contacts and/or keywords. The application checks your inbox every six hours. If it finds any new emails from these contacts (with any of the keywords in the subject line), it creates a calendar event reminding you to reply later in the day.

You can create a new project from [script.google.com/home](https://script.google.com/home).

Check out the code below:

```javascript
function reminder() {
  /* create list of senders and subject keywords */
  senders = ["freecodecamp", "codecademy", "meetup"];
  subjects = ["javascript", "python", "data science"];

  /* build the search query */
  var searchString = "is:unread newer_than:1d from: { " +
    senders.join(" ") + "} subject: { " + 
    subjects.join(" ") + " }"

  /* retrieve any matching messages */
  threads = GmailApp.search(searchString);

  /* if there are any results, create a calendar event */
  if (threads.length > 0) {
    var event = CalendarApp.getDefaultCalendar();
    event.createEventFromDescription('Review emails 6pm today');
  }

}

```

To run this function at regular intervals, you can set up a trigger. From the menu ribbon, choose Edit > Current project's triggers.

This will take you to a new tab where you can add a new trigger for the current project. Click 'Add new trigger' and choose the settings you wish to use.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-16.30.47.png)

Now, your script will run every 6 hours, and create a calendar event if you have any emails you need to review.

A useful extension might be to create a spreadsheet or Google Form that lets you add contacts and keywords easily.

How else could you integrate your inbox and your calendar?

### Slides update

Keeping presentations and slide decks up-to-date can be a tedious task. Luckily, you can use Google Apps Script to automate the process.

For this example, we'll use a fictional mobile app. The aim is to produce a slide deck with up-to-date metrics such as app downloads, active users, and revenue.

The trick will be to replace a number of `<tags>` in the deck with data contained in a Google Sheet.

In Slides, create a new presentation. Give it a name such as "App update template".

Create a new slide. Give it a title such as "Key metrics".

In a text box, add some content such as below:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-18.55.18.png)

Notice the tags included in each line. These will be replaced by up-to-date figures each time the script is run.

Next, create a new Sheet and add some data to use in the slide deck. In one column, refer to the tags in the slide deck. In the other, add the latest data.

In a real-life example, this would be calculated from raw data elsewhere in the spreadsheet. The raw data could come from Google Analytics, or be exported from a data warehouse, or from some other source.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-18.53.00.png)

Back in Slides, select Tools > Script Editor from the menu ribbon. This will open a new Apps Script project. 

Now you can start writing some code. The function takes two file ids as arguments - one for the Slides template, one for the Sheet. The file id is the string of letters and numbers you can find in the file's URL.

```javascript
function updateSlides(templateId, sheetId) {
  
  /* Make a latest copy of the slide deck template */
  var template = DriveApp.getFileById(templateId);
  var today = Date();
  var copyName = "App update " + today;
  var templateCopy = template.makeCopy(copyName);
  
  /* Open spreadsheet and slides by their id*/
  var sheet = SpreadsheetApp.openById(sheetId);
  var slides = SlidesApp.openById(templateCopy.getId());
  
  /* Get the data from the sheet */
  var data = sheet.getRange("A1:B5").getValues();
  
  /* replace all the tags in the deck with their latest values */
  for(var i=0; i <data.length; i++){
    var tag = "<"+data[i][0]+">";
    var value = data[i][1].toString();
    
    slides.replaceAllText(tag, value);
    
  }
}


```

If you run this script, a new presentation will be created with the latest data in place of each of the tags.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-18.56.23.png)

You could schedule this script to run at regular intervals, such as at the end of each month. If you wanted to develop the idea even further, you could use Apps Script to automatically email the new deck to a list of contacts.

### Over to you

Google Apps Script is a great way to start writing real JavaScript in a way which is immediately practical. Hopefully you found these three examples helpful. 

Perhaps this introduction has given you ideas for projects you could develop?

Remember, coding is a powerful tool - don't do anything with Apps Script you wouldn't do manually. Best not to erase your entire inbox or overwrite an important file with memes.

Thanks for reading!

