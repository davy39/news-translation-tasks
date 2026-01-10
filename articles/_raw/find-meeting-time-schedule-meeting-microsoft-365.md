---
title: How to Find a Meeting Time and Schedule a Meeting on Microsoft 365
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-26T21:34:19.000Z'
originalURL: https://freecodecamp.org/news/find-meeting-time-schedule-meeting-microsoft-365
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Screenshot-2022-10-25-at-13.03.43.png
tags:
- name: JavaScript
  slug: javascript
- name: Microsoft
  slug: microsoft
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Waldek Mastykarz

  A common functionality that many work apps have is letting users schedule a meeting
  with others in their organization. Here''s how to do it on Microsoft 365.

  Work Apps Need Work Data

  If your organization uses Microsoft 365, it shou...'
---

By Waldek Mastykarz

A common functionality that many work apps have is letting users schedule a meeting with others in their organization. Here's how to do it on Microsoft 365.

## Work Apps Need Work Data

If your organization uses Microsoft 365, it should consider integrating it with apps that it uses for work. 

Bringing data and insights from Microsoft 365 into the context of work apps helps users stay in the flow of their work, and have access to all relevant information in one place.

Say, your organization has an app that it uses for managing projects. Along with the information about the project itself, users of the app will also need information about the people on the project to get updates or schedule meetings. 

Information about people in your organization and their work is stored on Microsoft 365 and you can bring it into the context of your app.

When you build apps for work, you can use [Microsoft Graph](https://graph.microsoft.com/) - the API for Microsoft 365, to interact with Microsoft 365 and retrieve the data that's stored there.

## Find a Meeting Time and Schedule a Meeting with Attendees on Microsoft 365

Many work scenarios require the ability to schedule a meeting with others in your organization. For organizations that use Microsoft 365, this functionality is readily available in Microsoft Outlook.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-173.png)
_Scheduling a meeting in Microsoft Outlook on the web_

But what if you don't want your users to leave your app, go to Outlook, and manually schedule the meeting with the right people?

Using Microsoft Graph you can let users **select attendees, find a suitable meeting time, and schedule a meeting directly from your app**. Let me show you how.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-176.png)
_Custom web app allowing users to find a meeting time and schedule a meeting_

A sample app built using code fragments in this article is available on [GitHub](https://github.com/waldekmastykarz/mgt-spa-findmeetingtimes). To run it, you'll need [Node.js LTS](https://nodejs.org/) and a Microsoft 365 developer tenant which you can get for free from the [Microsoft 365 developer program](https://developer.microsoft.com/microsoft-365/dev-program).

### Select meeting attendees

The first step is to let users select with whom they'd like to meet.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-179.png)
_Web app with a few people selected to find available meeting times_

The easiest way to do this is by using the [People picker](https://learn.microsoft.com/graph/toolkit/components/people-picker) component from Microsoft Graph Toolkit.

> [Microsoft Graph Toolkit](https://aka.ms/mgt-docs) is a set of web components connected to Microsoft Graph, that work in any web framework.

To add the people picker, you'd add to your app:

```html
<mgt-people-picker></mgt-people-picker>
```

People picker automatically retrieves information about people in your organization from Microsoft 365 and filters the list as you type. Each person shows up with their name and picture to help users select the right person.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/select-people-graph-mgt.gif)
_Selecting people from Microsoft 365 in a custom web app_

Combining it with the [Login component](https://learn.microsoft.com/graph/toolkit/components/login) from Microsoft Graph Toolkit, you let users sign in to your app with their Microsoft 365 account and get access to the Microsoft Graph API.

### Find meeting times

The next step is to find available meeting times for the selected attendees including the current user.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-178.png)
_Available meeting times for the selected people from Microsoft 365_

Rather than having to download calendars for all users and manually look for a suitable meeting slot, you can call the [`findMeetingTimes` Microsoft Graph API](https://learn.microsoft.com/graph/api/user-findmeetingtimes?view=graph-rest-1.0&tabs=javascript), passing as arguments the array of the attendees and the meeting duration.

```javascript
const meetingTimes = await graphClient
  .api('/me/findMeetingTimes')
  .post({
    attendees: document.querySelector('mgt-people-picker').selectedPeople.map(p => {
      return {
        emailAddress: {
          address: p.userPrincipalName,
          name: p.displayName
        },
        type: 'required'
      };
    }),
    maxCandidates: 3,
    meetingDuration: `PT${document.querySelector('#duration').value}`,
    returnSuggestionReasons: true,
    minimumAttendeePercentage: 100
  });
availableMeetingTimes = meetingTimes.meetingTimeSuggestions;
```

You can get the list of attendees from the People picker which exposes the list of people selected by the user. 

When requesting available meeting times, you can pass many additional options, such as how many suggestions you'd like to get (`maxCandidates`), how many attendees have to be able to attend the meeting at minimum (`minimumAttendeePercentage`), or between which times the meeting should take place.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/find-meeting-times-graph.gif)
_Finding available meeting times for the selected attendees and meeting duration_

### Schedule a meeting

The final step is to schedule a meeting.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-180.png)
_Scheduling a meeting on Microsoft 365 from a custom web app_

At this point, you have all the necessary information to send a meeting invite to the selected people on behalf of the current user. 

You can do this by calling the `events` Microsoft Graph API, passing in the request body all information such as subject, start- and end-time, and the list of attendees.

```javascript
const meetingTime = availableMeetingTimes[selectedMeetingTime].meetingTimeSlot;

await graphClient
  .api('/me/events')
  .post({
    subject: document.querySelector('#subject').value,
    start: meetingTime.start,
    end: meetingTime.end,
    attendees: document.querySelector('mgt-people-picker').selectedPeople.map(p => {
      return {
        emailAddress: {
          address: p.userPrincipalName,
          name: p.displayName
        },
        type: 'required'
      };
    })
  });
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/scheduling-meeting-graph.gif)
_Scheduling a meeting on Microsoft 365 from a custom web app_

## Summary

By integrating Microsoft 365 into your work apps, you help your users work more effectively. 

Using the Microsoft Graph API, you can bring data and insights from Microsoft 365 into your work apps. This provides your users with all the information they need to complete their tasks. 

Because they have all information they need at their fingertips, they don't need to switch between different apps and can stay in the flow of their work. And by using web components from the Microsoft Graph Toolkit, you can build apps connected to Microsoft 365 even quicker.

Check out the [sample app](https://github.com/waldekmastykarz/mgt-spa-findmeetingtimes), and I'm looking forward to hearing from you how about you like it and what other integration scenarios you'd be interested in.

