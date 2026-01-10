---
title: How to Make a Google Form Survey – Google Forms Tutorial
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-04-19T18:13:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-google-form-survey-google-forms-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/04/google-form-survey-image.png
tags:
- name: forms
  slug: forms
- name: Google
  slug: google
- name: how-to
  slug: how-to
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'Google Forms is a helpful tool that lets you create surveys with a great
  variety of customization options. In this guide we will see the most common ways
  to make and customize your own Google Form.

  Start from a template

  When you''re ready to create a ...'
---

Google Forms is a helpful tool that lets you create surveys with a great variety of customization options. In this guide we will see the most common ways to make and customize your own Google Form.

## Start from a template

When you're ready to create a new survey, you have the option to start from a blank document or start from one of the many templates already available.

These templates are divided into three categories: Personal, Work, and Education. There are ready to use and save you from having to design the form yourself – for example, for a Customer Feedback form or a Party invite.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-36.png)
_In the image you can see examples of the templates available when creating from a model._

## General Google Form features

In the upper right corner of the page there are the buttons to reach the settings and customization options.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-58.png)
_From left to right the buttons are Customize Theme, Preview, Settings, Send, More, Google Account_

### Settings

The Settings allow you to customize various features, such as 

* whether the email addresses of the respondents are collected
* if respondents can return later to change their answers
* if they can submit multiple times or only once (in this case the respondent must be logged in with their account)
* if it shows a progress bar, and
* if the questions are shuffled randomly.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-57.png)
_General tab in the Settings with options: Collect email addresses, Limit to 1 response, Edit after submit, See summary charts and text responses._

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-59.png)
_Presentation tab in Settings with options: Show progress bar, Shuffle question order, Show link to submit another response._

### Customize Theme

You can also customize your template's Theme with various options, like changing the main color, the background color, and the font used in the form. 

You can also add a header image, upload one, or choose between the many available options.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-60.png)
_Theme Option menu, with options of changing header image, theme color, background color, font style._

## Google Form Questions and Question Types

You can add a new question using the first button in the floating menu to the right. Each question can be customized with a title and a description (through the three dot menu of the question), and also with an image or a video. 

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-72.png)
_The floating menu, with the Create Question button marked_

You can also set up each question as you require, making certain responses required. This way, it's impossible to submit the form without filling in that answer. For certain question types it is also possible to customize a response validation.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-62.png)
_Three dots menu on questions, with Description and Response validation menu items._

There are various possible types of questions, which I'll described individually below.

### Short answer form questions

Short answer questions allow for a single line answer. From the three dots menu, this answer can be validated:

* as a number, and also with various possible constraints for which numbers are allowed,
* as text, constraining whether it contains or doesn't contains something, 
* as a URL or email address,
* using length, with a minimum or maximum length constraint,
* using regular expressions, which allows you to make personalized pattern validations (this [Google Support page on Regular Expressions Syntax](https://support.google.com/a/answer/1371415?hl=en) can be useful),

You can set a custom error message to show when the answer fails the validation.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-63.png)
_The response is being validated to be a whole number, and a custom error message of "Please use a whole number" will be shown in case the response fails validation._

### Paragraph form questions

A paragraph question allows for a multi-line text answer. It can be validated with a minimum or a maximum length or a regular expression, and you can set a custom message to show if the validation fails.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-71.png)
_Paragraph form question creation, the response is being validated by length, a minimum character count of 160 characters is required. If the validation fails the message "Please write more than a tweet" is displayed._

### Multiple Choice, Checkboxes, and Dropdown form questions

These three types of questions let the respondent choose between multiple prewritten options. Where multiple choice or dropdown allow for a single answer, checkboxes allow respondents to select multiple options. 

The difference between multiple choice and dropdown is that in dropdown all the options are hidden inside the menu until it is selected. In multiple choice, all options are always visible. 

Both checkboxes and multiple choice allow for an "other" option where the respondent can fill in what they want. In all of these types of questions, the option order can be shuffled.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-39.png)
_Screenshot of the process of creating a multiple choice question._

### File upload form questions

These questions allow a user to upload a file to the form owner's Google Drive. Adding this question makes it mandatory for respondents to be signed in with their Google Account.

For this type of question you will need to confirm you agree to give others the access to your Google Drive.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-64.png)
_The message that appear when creating a File upload question._

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-65.png)
_FIle upload question settings._

You can set limits on what files can be uploaded, and on their size, and if multiple files can be uploaded at once. 

* **Allow only specific file types**: switching this on will let you choose which file types will be accepted.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-66.png)

* **Maximum number of files**: this dropwdown menu lets you choose between 1, 5 and 10 files to be uploaded at once.
* **Maximum file size**: you can choose between a maximum file size of 1 MB, 10 MB, 100 MB, 1 GB, 10 GB.
* **The form can accept up to 1 GB of files. Change**: pressing on "Change" will bring up a section of the Settings where you can change how much memory can be occupied by the files uploaded from this form. You can choose between 1 GB, 10 GB, 100 GB, 1 TB. Once the size limit has been reached, the form will stop accepting answers.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-67.png)
_In the General tab of the Settings you can set the maximum size of files collected. This section appear only if this kind of question is present in the form._

### Linear Scale form questions

This type of question creates a scale starting from 1 or 0, with a maximum number of 10. The respondents will select a point on the scale that they feel best reflects what they think.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-40.png)
_Screenshot of the process of creating a linear scale question._

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-41.png)
_This is how a linear scale question appears to the respondents._

### Multiple Choice grid and Checkboxes grid questions

These questions create a grid where each row is a multiple choice or checkboxe question. You can set it to require a response for each row, and/or to limit the respondent to one response per column (do not set both if you have more rows than columns). You an also set the order of the rows to shuffle.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-43.png)
_Building a multiple choice grid question._

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-44.png)
_How a multiple choice grid appears to the respondents._

### Date and Time form questions

The Date type question will let respondents insert a date. There are the options to include or not include the year, or to include or not include the time. The Time type question will let respondents insert a time or a duration.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-68.png)
_Creating a Date question._

## How to Divide the Form into Sections

Sections can be used to divide the Form in pages, and each section is shown separately to the respondent. 

You can create a new section from the last button in the floating menu to the right of the page. From the three dots menu near the title of the section, you can duplicate the current section, move it to another position in the document, or delete it. And you can customize each section with a description.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-73.png)
_The floating menu with the New section button marked._

### How to navigate between sections

You can make it so that, at the end of a section, the respondents will be redirected to a section that is not the next one in order. 

You can set this by the drop down menu at the end of a section.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-74.png)
_Menu at the end of a section from which you can choose which is the next section._

Or you can use the setting that gives to a multiple choice or dropdown question the power to determine to which section to go based on the selected answer. If a respondent selects an answer that has redirecting power, that wins over the end of section option. 

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-75.png)
_Three dots menu of a question, you can give redirecring powers to the answers from "Go to section based on answer"_

If multiple questions have redirecting powers, the last one is the one that determines what redirecting happens (if question 2 dictated redirection to Section C and question 4 to Section D, then the last question determines that the next section visited is Section D). 

## How to Show Answers in a Google Form

The answers are collected in a second tab on the same page in which the form is created. There are the options to see the answers in a Summary, by question in the Question tab, or by respondent in the Individual tab.

Using the Google Sheet button, you can have the answers automatically updated in a sheet. From the three dots menu, more answer options are available, like downloading them in a `*.csv` file, activating an email notification each time the form is submitted, or printing the answers.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-38.png)
_The top of the Responses tab_

The image below shows the summary of a multiple choice question. The answers given with the "other" option also appear in the legend on the side. The same answer spelled differently will create different entries, so it will need a manual tally.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-42.png)
_Summary of a multiple choice question, a cake diagram where each slice represents the percentage of respondents choosing that option._

## Other Google Form Features

### Quizzes

You can switch on Quiz mode at any time from the settings. This will give access to more options for each type of question, like auto-grading, providing a score for each question, and feedback to show with the results.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-45.png)
_Screenshot of the settings showing the toggle to activate quiz options._

When you set the form as a graded quiz using the "answer key" in the bottom left corner of the question block, you can add the score and the correct answer for the question. You can also set a feedback to show to the respondent with their test results.

### More complexity

The options for using Google Apps Script (three dots --> Script editor) or Add-Ons (three dots --> Add-ons) allow you to customize your forms even more. 

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-70.png)
_Three dots menu in the upper right corner, the Script editor and Add-ons item menu are near the bottom._

For example you can populate multiple choice, list, checkbox, and grid options from columns in any Google Sheet, or you can shut off the form after a certain number of submission. You can even (useful with the Quiz mode) add a timer to the form, or webcam face identification as an anti-cheating measure.

## Conclusion

Google Forms offers a lot of customization options on its own. You can create complex data collection surveys or complex graded quizzes. And with the added complexity of Scripts and Add ons, there's almost nothing that's out of reach.

