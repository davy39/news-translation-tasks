---
title: Google Sheets – How to Automatically Post Events to Google Calendar with Apps
  Script
subtitle: ''
author: Eamonn Cottrell
co_authors: []
series: null
date: '2023-05-24T21:44:39.000Z'
originalURL: https://freecodecamp.org/news/google-sheets-automatically-post-events-to-google-calendar-with-apps-script
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Sheets-to-Calendar3.jpg
tags:
- name: google apps script
  slug: google-apps-script
- name: google sheets
  slug: google-sheets
seo_title: null
seo_desc: 'In this article we''ll link two Google services -> Google Sheets and Google
  Calendar.

  By using a very short custom function in Google Apps Script, we can add a list of
  events from a Google Sheet to a Google Calendar. 🤯

  And we''ll even have it email ou...'
---

In this article we'll link two Google services -> Google Sheets and Google Calendar.

By using a very short custom function in Google Apps Script, we can add a list of events from a Google Sheet to a Google Calendar. 🤯

And we'll even have it email our guests as well. 🔥

Here's the video walkthrough to accompany the article:

%[https://youtu.be/FxxPq2wXcK4]

## Google Sheets Setup

Our sheet is quite straightforward. We have event names, dates, start times, end times and guest emails. 

The only curious thing is the formatting of our dates and times - I'll cover this as we go on, but you can see that columns B and C are repeating information from columns D, E and F...

![Screenshot of Google Sheet event information](https://www.freecodecamp.org/news/content/images/2024/03/1684886378577.png)

Google Calendar needs to receive the start and end times in the form of a full date/time object. But in the Google Sheet, there's not an easy way to create a dropdown data validation for users to select a date/time object.

In column D, I've put data validation to select a valid date.

![Screenshot of data validation for a valid date](https://www.freecodecamp.org/news/content/images/2024/03/1684886609169.png)

And in columns E and F, I've created a dropdown list of valid times.

![Screenshot of data validation for a valid time](https://www.freecodecamp.org/news/content/images/2024/03/1684886767503.png)

Columns B and C combine these together into a format that's useable to send to Google Calendar by using the =TEXT() function to concatenate the date and times together.

![Screenshot of google sheets text concatenation](https://www.freecodecamp.org/news/content/images/2024/03/1684886775902.png)

I promise it'll make more sense in a second! 😃

## Calendar Setup

Let's make a new calendar in Google Calendar.

![Screenshot of new calendar options](https://www.freecodecamp.org/news/content/images/2024/03/1684887186669.png)

Underneath your calendars on the left sidebar of Google Calendar, click the plus icon to add a new one.

Give it a name and a description if you want, and then we're ready to roll.

![Screenshot of creating a new calendar](https://www.freecodecamp.org/news/content/images/2024/03/1684887287557.png)

Scroll down a bit in the calendar's settings to the Integrate Calendar section. Copy the calendar ID. This is how we'll get Apps Script talking to Calendar!

![Screenshot of calendar ID](https://www.freecodecamp.org/news/content/images/2024/03/1684887643027.png)

## Apps Script + CalendarApp

Apps Script is awesome. 👏

The [Class CalendarApp](https://developers.google.com/apps-script/reference/calendar/calendar-app) allows a script to access a user's Google Calendar and make changes to it.

Here is the full script, and we'll walk through what's going on below.

```javascript
// Creates an events variable which is an array of arrays
function createCalendarEvent() {
	let events = SpreadsheetApp.getActiveSpreadsheet().getRangeByName("events").getValues();

	// Creates an event for each item in events array
    
	events.forEach(function(e){
    	CalendarApp.getCalendarById("f7574e7b4d1ad00c9ecd7f1eba5bed329e8600e317cd387a400748d67f301d06@group.calendar.google.com").createEvent(
      	e[0],
      	new Date(e[1]),
      	new Date(e[2]),
      	{guests: e[6],sendInvites: true}
    );
  })
}
```

I've named the range `A3:B8` as "events". Then in Apps Script, we create a variable named events that grabs all the values in that whole range. We used a small range, but you could make this as many rows long as need be.

```javascript
let events = SpreadsheetApp.getActiveSpreadsheet().getRangeByName("events").getValues();
```

Then, we loop through each item and add the events to our calendar.

The first part is where we use that calendar ID string we grabbed from Google Calendar for the `getCalendarById` method.

Then we use the `createEvent` method to pull data from each row in our Google Sheet and make new events.

Here's the `createEvent` description from the [developers page](https://developers.google.com/apps-script/reference/calendar/calendar-app#createeventtitle,-starttime,-endtime,-options):

![Screenshot of createEvent method](https://www.freecodecamp.org/news/content/images/2024/03/1684888482755.png)

You can think of each row of data in the Google Sheet as an array of values. In the zero position is the event name, in the one position is the event date and start time, and so on.

![Screenshot of array of arrays illustrated](https://www.freecodecamp.org/news/content/images/2024/03/1684938707460.jpeg)

By using `e[0]` we can access the element that is in the zero position for every time we loop through the forEach loop...effectively looping through each row of data.

And this is where the funky stuff we did with the start and end times comes into play.

Because the values in columns B and C are strings since we concatenated them together, we need to turn them back into complete date objects now.

That's why we're passing `new Date(e[1])` and `new Date (e[2])` into our createEvent function.

It's a bit of a cumbersome way to allow ourselves to use those dropdown selections in Google Sheets rather than painfully typing in a full date/time object.

User experience > code. 👍

And lastly, we add an optional parameter to send invites to guests.

## Send with Button

That's all there is to the Apps Script. 🎉

As an added feature, we've attached a script to the rounded rectangle drawing to make it function like a button. Any time this is pressed, the events in the Google Sheet will populate the Google Calendar.

![Screenshot of assigning a script to a drawing in Google Sheets](https://www.freecodecamp.org/news/content/images/2024/03/1684938905901.png)

I hope this has been useful for you!

Please come check out and subscribe to my [YouTube channel](https://www.youtube.com/@eamonncottrell?sub_confirmation=1) where I'm making weekly videos on coding and spreadsheets.

If you'd like my newsletter in your inbox, [check it out here](https://got-sheet.beehiiv.com/subscribe).

