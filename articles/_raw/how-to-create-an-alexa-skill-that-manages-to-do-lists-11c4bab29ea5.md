---
title: How to create an Alexa skill that manages to-do lists
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-31T22:03:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-alexa-skill-that-manages-to-do-lists-11c4bab29ea5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ct9YdVEA2z92Z8CGLWz2Zg.jpeg
tags:
- name: Amazon
  slug: amazon
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Terren Peterson

  I’m recognized as an Amazon Alexa Champion and have published more than twenty custom
  skills on the platform. I continue to look for new ways to stretch this technology,
  and one recent area I’ve been exploring is using Alexa to hel...'
---

By Terren Peterson

I’m recognized as an Amazon [Alexa Champion](https://developer.amazon.com/alexa/champions/terren-peterson) and have published more than twenty custom skills on the platform. I continue to look for new ways to stretch this technology, and one recent area I’ve been exploring is using Alexa to help organize everyday tasks. One of the underused features on the platform is the ability to create custom lists. [Here](https://www.amazon.com/gp/help/customer/display.html/ref=cssoc_TW_HP_201549900?nodeId=201549900) is a brief review on how you can take advantage of this feature, and please feel free to test out the [Workout Planner Skill](https://www.amazon.com/Drawrz-com-Workout-Planner/dp/B07CLY496R/) — it’s free!

![Image](https://cdn-media-1.freecodecamp.org/images/-c8VTjSI7FO9iKgSF0uJGSgM79Z3uAin9Yqp)
_Alexa Workout Planner Skill_

### Background

Hands-free devices like an Alexa open up the possibilities of building handy digital assistants. One of the first features that was enabled with the native device was the ability to create shopping lists. Given the retail heritage of Amazon, it’s not surprising that this came early. Saying phrases like “add shampoo to my shopping list” adds it to the user’s Amazon account. It also renders the data on other applications that the user is signed in on.

### Don’t Bring Alexa to the Gym, Bring a List

After using the shopping list feature for a while, I started to think of other types of lists that I could create. The device has the ability to create custom lists, and I thought it might be helpful in organizing my workouts. Rather than bring a handwritten workout list, I could make one using my voice.

I wrote a custom Alexa Skill called Workout Planner that asked questions about what types of exercises to do. It then created a list for me to track. Here’s a screenshot of what the skill creates on my phone.

![Image](https://cdn-media-1.freecodecamp.org/images/vXvBbsfZotdq7rK2QmR4HgQVo5XnN05li9jE)

### Architecture to use the Alexa Lists

The core functionality around lists is enabled through an [Alexa API](https://api.amazonalexa.com/v2/householdlists/) that manages the entities that are rendered on the Alexa companion app.

In a typical Alexa skill architecture, the API gets invoked from the Lambda function that contains the functionality of the skill. Data passed into the API call indicates if a new list should be created, what item should be added, if an item can be crossed off the list, and so on. The companion app handles all of the user interaction with the data on the list, with no additional effort by the skill developer. The user then has the ability to manage this list through the companion app, including marking items off as complete.

![Image](https://cdn-media-1.freecodecamp.org/images/874aizqiQKmCFc2G1-LqjQRYyBW8YRvVb1TR)

The voice interface is the same as any Alexa skill. Authoring a custom skill includes setup of sample utterances, intents, and so on based on the functionality being provided to the user.

### Enabling Permissions to use the Lists

When creating an advanced skill like this, the skill will need to request additional permissions. There are multiple levels of permissions and security, which all need to be in place for the skill to fully function.

First, the skill developer will need to acknowledge to the Alexa platform that the skill will make use of the lists. You can do this within the setup of the skill in the Developer console. The screenshot below is from the Permissions tab in the console. The sliders for both list attributes must be set.

![Image](https://cdn-media-1.freecodecamp.org/images/crX24atn1zXmoeXyKHF25te6VHPTqLbPVjBO)
_Identifying additional permissions needed by this custom skill in the Alexa Developer console_

As the skill goes through certification, Amazon validates that the permissions are required for the skill to work. This helps manage access to the user’s data that will be gained by the developer.

Second, when a user enables the skill on their device, they will need to grant consent for the skill to be able to read and write their data for their account. This is enabled through the companion app, and follows an “opt-in” model to access the escalated privileges. Below is a screenshot of the sliders that need to be adjusted in the settings.

![Image](https://cdn-media-1.freecodecamp.org/images/lJTQ0BACYmViOPhC0Vlfn4BpV0LjT9vUYTOG)
_Each user will need to grant permissions to access their list data._

Finally, at runtime, a consent token is created for each session that uses the skill. This token needs to be saved by the Lambda function, then passed in the header of the API call to Alexa.

### Example API Call

As highlighted in the architecture, the household API contains the core functionality required to manage the lists. There are multiple operations available within the API, and here is the documentation from Amazon. Using Node.js, here is the code used to invoke the API using the POST operation that creates a new list called “Workout Tracker”.

```
var path = "/v2/householdlists/";     var postData = {        "name": "Workout Tracker", //item value, with a string description up to 256 characters         "state": "active" // item status (Enum: "active" only)    };            var consent_token = session.user.permissions.consentToken;
```

```
var options = {        host: api_url,        port: api_port,        path: path,        method: 'POST',        headers: {            'Authorization': 'Bearer ' + consent_token,            'Content-Type': 'application/json'        }    };
```

```
var req = https.request(options, (res) => {    console.log('statusCode:', res.statusCode);    console.log('headers:', res.headers);    var data = "";
```

```
    res.on('data', (d) => {         console.log("data received:" + d);         data += d;    });    res.on('error', (e) => {         console.log("error received");         console.error(e);    });    res.on('end', function() {         console.log("ending post request");        if (res.statusCode === 201) {             var responseMsg = eval('(' + data + ')');             console.log("new list id:" + responseMsg.listId);             callback(res.statusCode, responseMsg.listId);        } else {             callback(res.statusCode, 0);        }    });});    req.end(JSON.stringify(postData));
```

The API returns a JSON object that includes the ListIdentifier used in subsequent calls to add items to the list.

### Conclusion

This is an easy way to leverage the voice user interface of Alexa with the ubiquity of the Alexa Companion App. [Here is a link](https://github.com/terrenjpeterson/workout-planner) to the full repo of the skill, and if you have any ideas on how to improve — please let me know!

