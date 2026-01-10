---
title: Hack G Suite using Apps Scripts — in under an hour.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-21T05:42:15.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-hack-using-apps-scripts-in-under-an-hour-8442a1495dce
coverImage: https://cdn-media-1.freecodecamp.org/images/0*nVQ-TOygSLHF9ucy
tags:
- name: Google
  slug: google
- name: google apps script
  slug: google-apps-script
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Supriya Shashivasan

  Have you heard of Google Apps Script? I was introduced to it for the first time
  at a Google Developer Group meetup held in Bangalore.

  Apps Script helps you use Google’s G Suite products, by running a script similar
  to JavaScrip...'
---

By Supriya Shashivasan

Have you heard of [Google Apps Script](https://developers.google.com/apps-script/)? I was introduced to it for the first time at a [Google Developer Group](https://www.meetup.com/GDGBangalore/) meetup held in Bangalore.

Apps Script helps you use Google’s G Suite products, by running a script similar to JavaScript. With just a few lines of code, users can get things done at a click of a button, which would otherwise take much more time.

Google Apps Scripts is very easy to pickup, and helps you to build complex systems by making use of G Suite. Users can publish web apps, and build custom functions for Google Slides, Sheets and Forms.

In this article, I will walk you through building a small app that uses Google Sheets, Google Slides, and Google Translate.

I built this app for travellers. When we visit foreign countries, communication becomes a problem due to language barriers. People often take flash cards with them to help communicate with locals.

![Image](https://cdn-media-1.freecodecamp.org/images/NNMmCE6qcHtQ1kn3fi6AGLQI-UK81XER9XUe)
_Photo by [Unsplash](https://unsplash.com/@sonereker?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Soner Eker</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

We are going to build exactly this. Questions and phrases are put up in Google Sheets. Then, a script translates the lines and writes them on to Google Slides. There!! Translated flash cards are ready to use.

Now, _READY.SET.CODE_

![Image](https://cdn-media-1.freecodecamp.org/images/wnoNxBiBIyjAcxeQAoR85BqnqU3TAdZH4egu)

### Storing data

Data here are sentences/words you want to translate. They are stored in the rows of the Google sheet.

So the structure of the spreadsheet will be:

* Each row will be filled with sentences that you want translated.
* The second column will hold the value to tell us the language the sentences must be translated to. The value here is the [Google translate language code](https://ctrlq.org/code/19899-google-translate-languages). If I want the sentences translated in Spanish, the code will be “es”.

![Image](https://cdn-media-1.freecodecamp.org/images/-CaL-t-tLtaweljpuILtIsX4xcV04CkZijiO)
_Filled Google Sheet_

### Accessing script editor

The script to complete the desired task is written in the Script Editor. To access this, go to **Tools > Script Edito**r. Another way to access the Script Editor is to visit t[he App Scripts dashbo](https://script.google.com/home)ard and create a new Apps script. All the scripts users write can be managed by this dashboard.

The script editor contains an empty file called **Code.gs**. We will write the code here in just one script.

### Main function

We write a main function `sheetToSlide()` in which the active sheet and slide are initialized. Another function `translate()` is called in the main function. It is here that the actual logic takes place.

```
function sheetToSlide() {  var sheet =   SpreadsheetApp.getActiveSheet();  var slide = SlidesApp.create('TranslateApp');  var data = sheet.getDataRange().getValues();  var lan= data[0][1];  Logger.log(lan);  for (var i=0; i<data.length; i++){     translate(i,data[i][0],lan,slide);  }}
```

In the variable `data`, the contents of the spreadsheet are stored as a multi-dimensional array. These values can be accessed by `data[Row][Column]`.

They are passed on to the `translate` function for further processing, along with the `slide` variable and `language` in which translation is required.

`Logger` is a class used to write text to the logging console. This helps a lot in the process of developing a code. The output of the code can be printed on to the debugging logs. To have a look at the logs go to **View > L**ogs in the script editor window.

### Translate function

In this function, new slides are added to the presentation that contain both the original and the translated sentences. Each sentence is inserted in a new slide in a text box.

```
function translate(num,data,language,slide){  var translate_lang = LanguageApp.translate(data, 'en', language);  var card= slide.insertSlide(num);  var shapeEnglish = card.insertShape(SlidesApp.ShapeType.TEXT_BOX, 150,100,300,60);  var textEnglish = shapeEnglish.getText();    textEnglish.setText(data);  textEnglish.getTextStyle().setBold(true);  card.insertLine(SlidesApp.LineCategory.STRAIGHT, 200,175,300,175)      var shapeTranslated = card.insertShape(SlidesApp.ShapeType.TEXT_BOX, 150,200,300,60);  var textTranslated = shapeTranslated.getText();  textTranslated.setText(translate_lang);  textTranslated.getTextStyle().setBold(true);  }
```

The sentence obtained is first translated using Google Translate which is a part of G Suite.

A new slide is inserted to hold the sentences. In the slide a text box is placed at a particular position. You can alter it by going through the docs [here](https://developers.google.com/apps-script/reference/slides/).

The text that must be displayed in the text box is done using the `getText()` and `setText()` methods. These are all properties of the Google Slides that you can manipulate and customize according to your wishes.

The design here is made very simple. A horizontal line is placed in the middle using `insertLine()` method to split the original and translated text. The properties and variables of all these methods used are given in detail in the docs provided by Google.

![Image](https://cdn-media-1.freecodecamp.org/images/bw5GvkzBf8xM-B66nc1XsQBoSYKyoT5AcSMM)

To run a the script, click on the run button beside the time icon. The script will prompt up a window which will ask for permission to access the Sheets and Slides, simply allow it. Next, go to your drive and a new presentation will be ready which will have translated sentences in the cards.

That’s how helpful and easy Apps Script is. You can also fill up a Firebase Realtime database by just using Google Sheets. By just writing simple scripts in few lines, you can automate a lot of things and also build web apps that can be hosted.

App Scripts is really powerful and aims highly at letting users make their services automated. Next time you want to send an email to a bunch of people, try using App Scripts. Once you get the hang of it, you can build wondrous things, like Sheets to website, your own blog, Sheets to Slides and many more.

Hope this helped. Cheers!!

You can feel free to reach out to me!

**Twitter**: [https://twitter.com/@s_omeal](https://twitter.com/@s_omeal)

**Paybackhub** : paybackhub.com and **Certhive**: certhive.com

