---
title: 'A simple How-To on Webhooks: the intimidation stops now'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-22T15:27:09.000Z'
originalURL: https://freecodecamp.org/news/a-simple-how-to-on-webhooks-the-intimidation-stops-now-9671e8c94c76
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QNB36W_y-FapMFqIPm7ldw.png
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Jared Wolff

  Webhook.

  It sounds like what happens when you cross a spider and a pirate. In the world of
  the internet though, webhooks are something completely different. Webhooks help
  connect services together.

  Let me explain.

  Say we have two hypot...'
---

By Jared Wolff

Webhook.

It sounds like what happens when you cross a spider and a pirate. In the world of the internet though, webhooks are something completely different. Webhooks help connect services together.

Let me explain.

Say we have two hypothetical services. One is a service that generates data, and the other that gathers and organizes that data.

The developers of the first service thought, “Man, our platform is only so useful. Let’s give the users the ability to forward real-time data to other services.”

The developers of the second service thought. “Gee willikers, it would be great if our users could import data easier.” So, they added webhooks to receive data in real time from a service like the first service.

Now as a user, you happen to use both services. You now have the power in your hands to connect them together.

The best way to explain it is with a real-world example.

![Image](https://cdn-media-1.freecodecamp.org/images/neTkch0k1ePK9-yoALIKhtl1iPY4UXv1Ifjp)
_Are you ready?_

### Real World Example

On a [recent project](https://www.jaredwolff.com/homemade-indoor-air-quality-sensor/), I connected an IoT sensor to a Google Docs Sheet. It took me only about 10 minutes. I’m going to show you the same right now.

#### Let’s first start by setting up the Google Sheet.

* Create a new sheet

![Image](https://cdn-media-1.freecodecamp.org/images/Zvel9b1dtdfuIcP3xQAREREdqnbbxQtBxHLL)
_Create a new sheet._

* Once you’re there, go to **Tools** and click **Script editor**

![Image](https://cdn-media-1.freecodecamp.org/images/3hAZkBZ7FcMHNSyAkqjPKCV1OFW6wnN5HOyS)
_Create a new script based on the sheet._

* It should open up a new window which looks something like this:

![Image](https://cdn-media-1.freecodecamp.org/images/eA7rAwDdGcK3uM6pIdhCXM935Cr9c4cSaXR3)
_New script screen._

* Copy and paste this code. I’ll explain it after we do that.

```
//this is a function that fires when the webapp receives a POST requestfunction doPost(e) {    //Return if null  if( e == undefined ) {    console.log("no data");    return HtmlService.createHtmlOutput("need data");   }    //Parse the JSON data  var event = JSON.parse(e.postData.contents);  var data = event.data;
```

```
//Get the last row without data  var sheet = SpreadsheetApp.getActiveSheet();  var lastRow = Math.max(sheet.getLastRow(),1);  sheet.insertRowAfter(lastRow);    //Get current timestamp  var timestamp = new Date();    //Insert the data into the sheet  sheet.getRange(lastRow + 1, 1).setValue(event.published_at);  sheet.getRange(lastRow + 1, 2).setValue(data.temperature);  sheet.getRange(lastRow + 1, 3).setValue(data.humidity);  sheet.getRange(lastRow + 1, 4).setValue(data.pm10);  sheet.getRange(lastRow + 1, 5).setValue(data.pm25);  sheet.getRange(lastRow + 1, 6).setValue(data.tvoc);  sheet.getRange(lastRow + 1, 7).setValue(data.c02);    SpreadsheetApp.flush();  return HtmlService.createHtmlOutput("post request received");}
```

Now, let’s understand everything.

```
function doPost(e) {
```

Is the function that gets called on a POST event. Consider this script as a web server. We’re sending it data at a specific address (that we’ll have in a hot minute)

**e** is the object of the HTTP call. It will have the data that we’re sending it. So it’s a good idea to check if it’s **NULL.** If it is, then there’s no need to run the script.

If we do have valid data, let’s change it from a string into useable JSON. You can use everyone’s favorite function`JSON.parse` to do so.

```
var event = JSON.parse(e.postData.contents);
```

Remember, the structure of the data will determine how you process it! You may have to run `JSON.parse` several times depending on how nested your data is and what format it’s in.

After you have your data, it’s time to put it in the right place!

```
//Get the last row without datavar sheet = SpreadsheetApp.getActiveSheet();var lastRow = Math.max(sheet.getLastRow(),1);sheet.insertRowAfter(lastRow);
```

These three calls will get you to the first available row starting at row 1 (leaving row 0 for the column labels).

Then, finally, we put the data in the row it belongs:

```
sheet.getRange(lastRow + 1, 1).setValue(event.published_at);
```

Where the first parameter of `sheet.getRange` is the row and the second is the column. You can use the `setValue` function to set what you want in that particular cell.

By the way, the inspiration for this code came from [this post](https://blog.runscope.com/posts/tutorial-capturing-webhooks-with-google-sheets).

Cool. So we have a script. How do we call it?

![Image](https://cdn-media-1.freecodecamp.org/images/xmlYv8J8o8Seprjfok6kRtE9mEeZS3GdYpmX)
_Why can’t I do annything riiiiiighhhhttt._

* Hit that **Publish** button

![Image](https://cdn-media-1.freecodecamp.org/images/f7hbT1FSsO7xFFFSOdw2sTPXuCGI7YFUnELw)
_Click the “Publish” button._

* Click `Deploy as a web app`

![Image](https://cdn-media-1.freecodecamp.org/images/gvRCAP7JBc3Ov8AlE1Uv3ndchKK5LjcDr85S)
_Click that “Deploy as web app” link!_

* Change the settings to match the screenshot below. Then click `Deploy`

![Image](https://cdn-media-1.freecodecamp.org/images/LTXLSZqj14WMm0V9rpyV62csz6YQ2m2qaleT)
_Anyone can have access for simplicity. For other use cases, logins are recommended._

* You may get a screen asking you to update your permissions. Click `Review Permissions`

![Image](https://cdn-media-1.freecodecamp.org/images/GjeBOC97Gcp579KijLCau3MSdzF0XvVDpIRW)
_You’ll need to authorize the app to use your account to modify the Google Sheet._

* Click the `Advanced` and then click `Go to <Your File Na`me> in the bottom left.

![Image](https://cdn-media-1.freecodecamp.org/images/dXKx4QtvjijriJz8sLhBJcJBxXHZocHwJ1Rh)
_Security warning. No worries._

* Finally, click `Allow`

![Image](https://cdn-media-1.freecodecamp.org/images/XjQpS2dsfjH34y9PgLRBIryQvf57HkZJR-xS)
_This is a security mechanism for Google. Since it’s your app, it's ok!_

* In the last screen, copy your Webhook URL!

![Image](https://cdn-media-1.freecodecamp.org/images/OZBuLa8p0qkal7hy3DX5KhfL-5gMiQXOH0jD)
_This URL does not change, even when you release a “new version.”_

### Test it

Now we can test if everything works by using Postman. If you haven’t played with Postman yet, it’s a great graphical user interface for `curl`.

* [Install Postman.](https://www.getpostman.com/downloads/) You may need an account to go further.
* Once inside, create a new request. Name it so you know it belongs to this Google Docs webhook

![Image](https://cdn-media-1.freecodecamp.org/images/SMjDT0WyXxmyAB9AE3XlAptskaJF4RQkX6aG)
_Two very important steps. If either of these is wrong, you won’t be getting any entries._

* Click `body` and enter the following test code:

```
{    "event": "gdxg",    "data": {        "temperature": 21    },    "coreid": "zczxvz",    "published_at": "zcvzxcvx"}
```

* Finally, click that blue `Send` button.

![Image](https://cdn-media-1.freecodecamp.org/images/KDjc6l3qfgCOXFx1EnawJgCa3sYVAklQSaNJ)
_This is bogus data for testing only._

* Go back to your excel sheet and see the magic!

![Image](https://cdn-media-1.freecodecamp.org/images/vSeMTe75LnIFgtwa8bsQ6gA6hS9IyD-hlwjs)
_Note that the headings are added so we know what the data is!_

Now we’re cooking with gas!

![Image](https://cdn-media-1.freecodecamp.org/images/gmvzAcpsHrsdiNdvQ0zZoxukiVAlvBqAHY1z)
_Mr. Scary Gas Bunny Man_

### Conclusion

I hope you’ve gotten the above example to work. Luckily for you, there’s a lot less to worry about once you get this part up and running!

To recap, we’ve talked about webhooks and why they’re used. You should be feeling confident at this point to go and set up some of your own. If you’re still feeling intimidated, I recommend using services like Zapier or IFTTT. (They’re shiny front ends for APIS and Webhooks already available.)

Last but not least [check out the full post](https://www.jaredwolff.com/homemade-indoor-air-quality-sensor/) where I integrate hardware and web in one awesome project.

Happy webhooking!

