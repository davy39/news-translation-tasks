---
title: How to build a serverless report server with Azure Functions and SendGrid
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-12T17:40:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-serverless-report-server-with-azure-functions-and-sendgrid-3c063a51f963
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vQPIjM0f0bLivXDceow66w.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
seo_title: null
seo_desc: 'By Burke Holland

  It’s 2018 and I just wrote a title that contains the words “Serverless server”.
  Life has no meaning.

  Despite that utterly contradictory headline, in this article we’re going to explore
  a pretty nifty way to exploit SendGrid’s templat...'
---

By Burke Holland

It’s 2018 and I just wrote a title that contains the words “Serverless server”. Life has no meaning.

Despite that utterly contradictory headline, in this article we’re going to explore a pretty nifty way to exploit SendGrid’s template functionality using Timer Triggers in [Azure Functions](https://azure.microsoft.com/en-us/services/functions/?WT.mc_id=serverlessreport-medium-buhollan) to send out scheduled tabular reports. We are doing this because that’s what everyone wants in their inbox. A report. With numbers in it. And preferably some acronyms.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vD5Qf5yUplqO3gDw8dcDlg.png)

#### The Inventory SKU Report

First, let’s straw-man this project with a contrived application that looks sufficiently boring enough to warrant a report. I have just the thing. A site where we can adjust inventory levels. The word “inventory” is just begging for a report.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xisRfTO8WdoNqLWLL5q4ZQ.png)

This application allows you to adjust the inventory quantity (last column). Let’s say that an executive somewhere has requested that we email them a report every night that contains a list of every SKU altered in the last 24 hours. Because of course, they would ask for that. In fact, I could swear I’ve built this report in real life in a past job. Or there’s a glitch in the matrix. Either way, we’re doing this.

Here is what we’re going to be building…

![Image](https://cdn-media-1.freecodecamp.org/images/1*DjphgVS92Dtc_5r4_id9Zg.png)

Normally the way you would build this is with some sort of report server. Something like SQL Server Reporting Services or Business Objects or whatever other report servers are out there. Honestly, I don’t want to know. But if you don’t have a report server, this gets kind of tedious.

Let’s go over what you have to do to make this happen…

1. Run a job on some sort of timer (cron job)
2. Query a database
3. Iterate over records and format them for output to the screen
4. Email said report
5. Update your resume and contact recruiters

This is the kind of thing that nobody wants to do. But **I think** this project can be a lot of fun, and we can use some interesting technology to pull it off. Starting with Serverless.

#### Serverless timer functions

Serverless is a really good use case for one-off requests like this. In this case, we can use Azure Functions to create a Timer Trigger function.

To do that, I’m going to use the Azure Functions extension for VS Code. I’m going to use it for everything in fact. Why? Because I don’t know you, but I do know it’s highly likely that you are using VS Code. VS Code is great because it’s like a movie that all developer’s can universally agree is completely awesome. Sort of the opposite of “Children of Men”. That movie was terrible and you know it.

Make sure you install the Azure Functions extension.

[**Azure Functions - Visual Studio Marketplace**](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions&WT.mc_id=serverlessreport-medium-buhollan)  
[_Extension for Visual Studio Code - An Azure Functions extension for Visual Studio Code._marketplace.visualstudio.com](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions&WT.mc_id=serverlessreport-medium-buhollan)

Now create a new Function App from within VS Code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*W1QGqj0bSh4X_CJk0JQukQ.gif)

Then create a new Timer Trigger function. Timer Trigger functions are scheduled using standard Cron Expressions. You have likely not ever seen before because I had not seen one until a few months ago. And I’ve been in this industry for a LONG time. I am old, father William.

Cron expressions look kind of scary cause they have asterisks in them. In the case below, I’m saying that when minutes is 0 and seconds is 0 and hours is evenly divisible by 24, fire the function. This would be midnight.

![Image](https://cdn-media-1.freecodecamp.org/images/1*l7L3hD2vVF_imKfrwODdhg.gif)

Now we can run this locally (F5). We’ll see in the embedded terminal the schedule on which our Function will be called; the next 5 occurrences.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4w9tkPYAfylKylDNxmWwKA.png)

It feels good, man.

OK, now we need to get some data. I’m not going to drag you into the specifics of me querying SQL Server from this function because that’s not what this article is about, but here’s the code anyway.

```js
const { Connection, Request } = require('tedious');

const options = {
  weekday: 'long',
  year: 'numeric',
  month: 'long',
  day: 'numeric'
};

const config = {
  userName: process.env.SQL_USERNAME,
  password: process.env.SQL_PASSWORD,
  server: process.env.SQL_SERVER,
  options: {
    encrypt: true,
    database: process.env.SQL_DATABASE
  }
};

module.exports = function(context, myTimer) {
  getChangedSkus()
    .then(data => {
      if (data.length > 0) {
        sendEmail(context, data);
      } else {
        context.done();
      }
    })
    .catch(err => {
      context.log(`ERROR: ${err}`);
    });
};

/**
 * Executes a query against the database for SKU's changed in the last 24 hours
 * @returns {Promise} Promise object contains result of query
 */
function getChangedSkus() {
  return new Promise((resolve, reject) => {
    const connection = new Connection(config);
    const query = `SELECT Sku, Quantity, CONVERT(varchar, Modified, 0) as Modified
                   FROM Inventory
                   WHERE Modified >= dateadd(day, -1, getdate())`;

    connection.on('connect', err => {
      if (err) reject(err);

      let request = new Request(query, err => {
        if (err) {
          reject(err);
        }
      });

      const results = [];
      request.on('row', columns => {
        let result = {};
        columns.forEach(column => {
          result[column.metadata.colName] = column.value;
        });

        results.push(result);
      });

      request.on('doneProc', (rowCount, more) => {
        resolve(results);
      });

      connection.execSql(request);
    });
  });
}
```

I’m connecting to the database, doing a simple query and….wait a minute…did not I say I **wasn’t** going to get into specifics? You had me there for a minute, but I’m onto your game!

So this pulls in data and we get it in a JavaScript object that we can pass as JSON. If we were to `JSON.stringify` this, we will see the data set that we need to send in the report.

```js
[
  { "Sku": "1", "Quantity": 65, "Modified": "Nov  6 2018 10:14PM" },
  { "Sku": "10", "Quantity": 89, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "11", "Quantity": 39, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "12", "Quantity": 2, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "13", "Quantity": 75, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "14", "Quantity": 85, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "15", "Quantity": 58, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "16", "Quantity": 2, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "17", "Quantity": 48, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "18", "Quantity": 68, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "19", "Quantity": 67, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "2", "Quantity": 5, "Modified": "Nov  6 2018 11:18PM" },
  { "Sku": "20", "Quantity": 37, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "21", "Quantity": 54, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "22", "Quantity": 21, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "23", "Quantity": 46, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "24", "Quantity": 55, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "25", "Quantity": 21, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "26", "Quantity": 42, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "27", "Quantity": 65, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "28", "Quantity": 74, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "29", "Quantity": 33, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "3", "Quantity": 51, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "4", "Quantity": 96, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "5", "Quantity": 27, "Modified": "Nov  6 2018 11:18PM" },
  { "Sku": "6", "Quantity": 13, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "7", "Quantity": 54, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "8", "Quantity": 89, "Modified": "Nov  2 2018  8:18PM" },
  { "Sku": "9", "Quantity": 56, "Modified": "Nov  2 2018  8:18PM" }
]
```

OK! We’ve got data, now we just need to make it pretty and email it to someone we don’t like. How are we going to do that? With SendGrid!

#### SendGrid setup

SendGrid is a nifty service with a really nice dashboard. You will like it. Or you won’t. Either way, you have to use it to get through this blog post.

You can create a free account if you don’t already have one. That’s plenty for what we’re doing here today.

Once you create a report, SendGrid is going to drop you into your “dashboard”. From this dashboard, you need to create a new API Application and get the key.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4YEtLhScWTudhZZT0-O8lA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*CyjzWnmxyTsrX9qr1z5rMw.png)

Make sure you copy your API key when it gives it to you. You can’t ever get back to it and you’ll have to do this all over again. Let’s face it: it was kinda boring the first time around.

Copy that key into your Azure Functions project. Put it in the `local.settings.json` file so you can access it as a Node.js environment variable later.

```
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "DefaultEndpointsProtocol=https;AccountName=reporttimerstorage;AccountKey=OJVYCHI0GhtIm5XZdsDzGZFraJD/v/rfPwMSu4B72Kf5/O7oCrOQKNAFkQ==",
    "FUNCTIONS_WORKER_RUNTIME": "node",
    "SENDGRID_API_KEY": "SG.rlpDOy3EQNOTChnzpa1COPYg.G4MYlEYhwHk0RyvuGcY_xKEYbhQoFTtPB9A9-5ZaYQ"
  }
}
```

Now we are going to create a template in SendGrid. That’s what we will use to design our report. SendGrid has something called “Transactional Templates”. I have no idea why they are called that, but we are going to be needing one.

![Image](https://cdn-media-1.freecodecamp.org/images/1*s53lLNCrkJBZatWFVff0pA.png)

Once you create a new one, you have to create a new “version”. I had a hilariously hard time figuring this out. But then again, my brain is tad on the smallish side of little.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SteEZljYYaKdqArZ4PzWlQ.png)

Choose to design your template with the Code Editor. You don’t need no freakin’ Designer Editor!

![Image](https://cdn-media-1.freecodecamp.org/images/1*wyh-9yjmGsJYGg5gu3Vkvw.png)

SendGrid support handlebars, which is a template syntax that’s so easy, even I can do it. In the Code Editor, you can paste the JSON data into the “Test Data” tab…

![Image](https://cdn-media-1.freecodecamp.org/images/1*KOj15MbsQnxKsdLsDYkoPQ.png)

Now iterate over the data using its key name from the JSON…

![Image](https://cdn-media-1.freecodecamp.org/images/1*oAx66f58qZbtieLt0wghFA.png)

It’s BEAUTIFUL! I’m crying. Ship it.

ALRIGHT. Fine. We’ll make it a little nicer on the old eyeballs. Here is a style that I shamelessly ripped off of the gorgeous [Bulma CSS framework](https://bulma.io/).

```html
<style>
  table {
    border-collapse: collapse;
    border-spacing: 0;
    background-color: white;
    color: #363636;
  }
  .table td,
  .table th {
    border: 1px solid #dbdbdb;
    border-width: 0 0 1px;
    padding: 0.5em 0.75em;
    vertical-align: top;
  }
  .table th {
    color: #363636;
    text-align: left;
  }
  .table thead td,
  .table thead th {
    border-width: 0 0 2px;
    color: #363636;
  }
  .table tbody tr:last-child td,
  .table tbody tr:last-child th {
    border-bottom-width: 0;
  }
  .table.is-bordered td,
  .table.is-bordered th {
    border-width: 1px;
  }
  .table.is-bordered tr:last-child td,
  .table.is-bordered tr:last-child th {
    border-bottom-width: 1px;
  }
  .table.is-fullwidth {
    width: 100%;
  }
  .container {
    margin: 0 auto;
    position: relative;
    max-width: 960px;
    padding-top: 20px;
    font-family: helvetica, sans-serif;
  }
</style>

<div class="container">
  <h1>Modified SKUs</h1>
  <p>The following SKU's were modified in the last 24 hours</p>

  <table class="table is-fullwidth">
    <thead>
      <tr>
        <th>Sku</th>
        <th>Quantity</th>
        <th>Last Modified</th>
      </tr>
    </thead>
    <tbody>
      {{#each Skus}}
      <tr>
        <td>{{Sku}}</td>
        <td>{{Quantity}}</td>
        <td>{{Modified}}</td>
      </tr>
      {{/each}}
    </tbody>
  </table>
</div>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*TML-eMV1jv6d5NQppwtV5g.png)

It’s ok at this point for you to be audibly impressed.

Now you might have noticed that the Subject of the email is missing. How do we fill that in? Well, after another embarrassing period of failure followed by introspection, I figured out that it’s behind the “Settings” icon on the left. You just have to pass a value in your JSON for “Subject”.

![Image](https://cdn-media-1.freecodecamp.org/images/1*siB4hsbwPrTkydVpVT66Fg.png)

Now we need to get the template ID and add it to our Azure Functions project. Save this template and select the ID from the main template screen.

![Image](https://cdn-media-1.freecodecamp.org/images/1*S6zR6HQbhBWc1pgwpA9gnw.png)

Drop it in the trusty `local.settings.json` file right underneath your SendGrid API key.

```
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "DefaultEndpointsProtocol=https;AccountName=reporttimerstorage;AccountKey=OJVYCHI0GhtIm5XZdsDzGZFraJD/v/rfPwMSu4B72Kf5/O7oCrOQKNAFkQ==",
    "FUNCTIONS_WORKER_RUNTIME": "node",
    "SENDGRID_API_KEY": "SG.rlpDOy3EQNOTChnzpa1COPYg.G4MYlEYhwHk0RyvuGcY_xKEYbhQoFTtPB9A9-5ZaYQ"
    "SENDGRID_TEMPLATE_ID": "d-3e33c1453cf7457fb06e6d30519bd422"
  }
}
```

Now we are ready to pass our data from our Azure Function to SendGrid and send out this incredible work of business art.

![Image](https://cdn-media-1.freecodecamp.org/images/0*3RlCKtdQS1oXYBc0.jpg)

#### SendGrid bindings for Azure Functions

Azure Functions provides a binding for SendGrid. If you create a function through the Azure Portal, it will create this binding for you when you select the “SendGrid” template. If you are doing it locally like I am, you have to add it yourself.

First you need to open the `function.json` file for the `CreateReport` function and add in the SendGrid binding.

```
{
   "type": "sendGrid",
   "name": "message",
   "apiKey": "SENDGRID_API_KEY",
   "to": "youremail@company.com",
   "from": "hahabusiness@businesstime.com",
   "direction": "out"
}
```

The SendGrid binding comes as an extension for Azure Functions. Run the following command in the terminal to install it.

```
Microsoft.Azure.WebJobs.Extensions.SendGrid -Version 3.0.0
```

When you run this command, VS Code will ask you to restore some dependencies. You can click restore. Nothing bad will happen…OR WILL IT?!

One other thing you need to do is tweak your `extensions.csproj` file to reference the latest SendGrid library. This is required to use dynamic templates.

```
<PackageReference Include="Sendgrid" Version="9.10.0" />
```

When you add that, VS Code will prompt you to restore again and yes, you definitely need to do it this time. VS Code needs to build these binaries and the restore does that.

OK! Now we’re ready to send an email via our SendGrid template. Here is the code to do it. It’s depressingly simple. I know after all this you were hoping for enough code to choke a cat (what? you’ve never heard that metaphor before?), but this is all it takes.

```js
function sendEmail(context, data) {
  context.done(null, {
    message: {
      /* you can override the to/from settings from function.json here if you would like
        to: 'someone@someplace.com',
        from: 'someone@anotherplace.com'
        */
      personalizations: [
        {
          dynamic_template_data: {
            Subject: `Tailwind SKU Report For ${new Date().toLocaleDateString(
              'en-US',
              options
            )}`,
            Skus: data
          }
        }
      ],
      template_id: process.env.SENDGRID_TEMPLATE_ID
    }
  });
}
```

The items of note are me passing in a Subject as part of the JSON. As well as the fact that you can override to/from addresses specified in the `function.json` file here.

Now you can run your function and wait 24 hours to test it!

No but seriously — how do you manually test a Timer Trigger without constantly modifying the damn Cron Job?

I’ll show you how I do it and then you can figure out a better way.

#### Testing timer triggers with http triggers

I create an Http Trigger in the same project and call it “RunCreateReport”. In that function, I just import and call the timer function.

```js
const index = require('../CreateReport/index');

module.exports = function(context, req) {
  // This is a tester function that manually executes the CreateReport timer function
  index(context);
};
```

The only drawback to this is that you have to repeat your SendGrid binding settings from `function.json` in the “CreateReport” over in the “RunCreateReport” `function.json`. But other than that, this works just fine. Now you can run this thing, fire up a browser and hit the URL which will call the timer function immediately. You can test without having to touch that icky old Cron expression.

#### HAHA business

Now go check your email and bask in the glory of the report. Note that you don’t have to own an email address to send from SendGrid. You can literally send from any address. Seriously. Go ahead and try. JUST THINK OF WHAT YOU CAN DO WITH THIS POWER.

Here’s what my inbox looks like. Heads up, it does go to junk. Probably because I don’t own the sender email address.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BOXOst-_FtJ-RHaHO11jyA.png)

WHAT? There’s a “Business Resilience Conference”? OMG so much business. I bet those people get a LOT of reports.

You can get this project from Github.

[**burkeholland/serverless-sendgrid-report**](https://github.com/burkeholland/serverless-sendgrid-report)  
[_Contribute to burkeholland/serverless-sendgrid-report development by creating an account on GitHub._github.com](https://github.com/burkeholland/serverless-sendgrid-report)

Here are a few other Azure Functions resources to keep you busy.

* [Deploy to Azure using Azure Functions](https://code.visualstudio.com/tutorials/functions-extension/getting-started?WT.mc_id=serverlessreport-medium-buhollan)
* [Azure Functions JavaScript developer guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-node?WT.mc_id=serverlessreport-medium-buhollan)
* [Migrating a Mongo DB API to Azure Functions](https://www.youtube.com/watch?v=89WXgaY-NqY)

