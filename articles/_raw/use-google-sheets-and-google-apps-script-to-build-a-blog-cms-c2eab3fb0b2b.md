---
title: How to use Google Sheets and Google Apps Script to build your own blog CMS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-03T01:48:32.000Z'
originalURL: https://freecodecamp.org/news/use-google-sheets-and-google-apps-script-to-build-a-blog-cms-c2eab3fb0b2b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8ee675JOtyd-tjE6cfk0Tg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Daniel Ireson

  I recently stumbled across Google Apps Scripts, a platform that allows users to
  extend Google’s G Suite of online products through a scripting language derived
  from JavaScript. It’s analogous to VBA, which is built into most of Micro...'
---

By Daniel Ireson

I recently stumbled across [Google Apps Scripts](https://developers.google.com/apps-script/), a platform that allows users to extend Google’s G Suite of online products through a scripting language derived from JavaScript. It’s analogous to [VBA](https://msdn.microsoft.com/en-us/vba/office-shared-vba/articles/getting-started-with-vba-in-office), which is built into most of Microsoft Office products.

Google Apps Scripts is incredibly powerful and enables complex systems to be built on top of Google services. It can be a great choice when you need to quickly prototype an idea or design a solution that’s customizable by non-technical users. A great way to make an accessible solution is to build on top of products that users are already familiar with.

In this article, I will walk through a simple yet novel example of building a “Content Management System” (CMS) for an online blog using Google Sheets, Google Forms, and Google Apps Script.

The blog will be designed as a single page application with pagination and the ability to filter by post category. Blog posts will be stored in a Google Sheets spreadsheet. New posts will be added through Google Forms since it provides a user-friendly interface. Google Apps Script will be used to build an API to make the spreadsheet content available in an easy-to-use format.

![Image](https://cdn-media-1.freecodecamp.org/images/07oxc4724ms4QIehmCYTvmw9-w3Y24UiSLU8)
_[https://danielireson.github.io/google-sheets-blog-cms](https://danielireson.github.io/google-sheets-blog-cms/" rel="noopener" target="_blank" title=")_

#### Disclaimer

I’m not using this in production, and I have no idea if it will scale. Think of it as a proof of concept to show what’s possible. You should do your own research if you want to use it in a production environment. I suspect that traffic will get throttled if you get near the upper limits of the service quotas. There’s a hard limit of [20,000 URL fetches](https://developers.google.com/apps-script/guides/services/quotas) per day on scripts for free Google accounts, and there may also be other limits in place.

### Storing the data

Google Sheets will be used as a flat-file database to store the blog posts. A flat-file database stores data in plain-text in a single table. In contrast, a relational database captures relationships across tables and enforces the structure of those relationships to minimize duplication and maximize data integrity.

Although more limited, a flat-file structure is easy to get started and is suitable for our use case of a small blog.

#### Spreadsheet structure

Each row will represent a new blog post, and columns will be used to capture individual blog post fields. In a flat-file structure, there’s no concept of primary and foreign keys like in the relational model. Information that is captured in columns, such as category and author, will be duplicated across blog posts when common.

#### Getting started

Create a new Google Sheets spreadsheet and connect this to Google Forms by going to **Tools > Create a fo**rm in the menu bar. After selecting this option, you’ll be presented with an editor to define the form questions. These get mapped to spreadsheet columns.

For my demo, I added four questions for **Title**, **Category**, **Author,** and **Content**.

Each field had a text type apart from **Category**, which was a radio type with four hypothetical categories: general, marketing, financial, technology.

![Image](https://cdn-media-1.freecodecamp.org/images/a9K2JlG8UCudNKRgAUmyhtKtc3ASZ2vTVju7)
_[https://docs.google.com/forms/d/1QKthdGK9pznyojcZ4esrU1moky8_Wih4aqa7_uIQ0sw](https://docs.google.com/forms/d/1QKthdGK9pznyojcZ4esrU1moky8_Wih4aqa7_uIQ0sw/closedform" rel="noopener" target="_blank" title=")_

When a form submission is made, a row is appended to the Google Sheets spreadsheet. A **Timestamp** field is automatically added for each row, which we’ll use to calculate the post date.

To allow for draft posts, I also added a boolean **Published?** field as the first column. The API should only return posts with a value of **true**. This allows posts to be reviewed and edited before they are published.

![Image](https://cdn-media-1.freecodecamp.org/images/z3uEkxyDVTu9Co94vNxUODDqCdSCijV78rHv)
_[https://docs.google.com/spreadsheets/d/1xy6Hz8yagIW7zwdGGC0XICObIoZ_YYhRhnQ1T8GrQnE/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1xy6Hz8yagIW7zwdGGC0XICObIoZ_YYhRhnQ1T8GrQnE/edit?usp=sharing" rel="noopener" target="_blank" title=")_

### Building the API

Google Apps Script is built on top of the ECMAScript 5 (ES5) JavaScript standard. When building the API, we can’t use ES6 features like scoped variables, arrow functions, or default parameters. If you’re unsure of what’s available in ES5, I’d recommend consulting the [MDN docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript) compatibility tables.

Despite the lack of ES6, Google Apps Scripts can still be used to build reasonably complex applications on top of G Suite products.

#### Getting started

You can access the Google Apps Script online editor by going to **Tools > Script Edit**or in the menu bar from the Google Sheets spreadsheet. A script editor will open with an empty file nam**ed Code**.gs. Since this is a simple application, we’ll put our logic in this one script, but you can also easily break up your application into separate scripts.

#### Returning a response

We can make use of `doGet` and `doPost` callback functions to respond to HTTP requests. These are just ordinary functions that Google Apps Script looks to invoke when a GET or POST request is respectively made to the API.

To generate a response, we’ll use the [ContentService](https://developers.google.com/apps-script/guides/content). A JavaScript object can be passed to `JSON.stringify` and then to `createTextOutput` on this service to build a JSON response. If the mime type is set to `ContentService.MimeType.JSON` this will appropriately set the content type to `application/json`.

Generating a JSON response is as easy as the following:

```
function doGet(e) {  var output = JSON.stringify({    status: 'success',    message: 'It worked',  });    return ContentService.createTextOutput(output)    .setMimeType(ContentService.MimeType.JSON);}
```

#### Parsing requests

The `doGet` callback is always invoked with an event generated from the request. From this event, we can access the query string parameters, which we’ll use to support various API options. Simple stateless authentication will be implemented through a `key` parameter. This will simply check that the `key` parameter value matches a hardcoded key value. Requests that don’t match will be shown an unauthorized response.

A `category` parameter will be used so that users can request posts from a single category. This saves them from having to filter by category on the front-end. Pagination will also be implemented through a `page` parameter.

These options should be appended to the URL when making the API request.

```
GET https://apiurl?key=abcdef&category=general&page=1
```

This request would generate the following event:

```
{  "queryString": "key=abcdef&category=general&page=1",  "parameter": {},  "contextPath": "",  "parameters": {    "key": [      "abcdef"    ],    "category": [      "general"    ],    "page": [      "1"    ]  },  "contentLength": -1}
```

Let’s first authenticate the event. We’ll do this by checking that `key` has been provided and that it matches the defined API key.

```
var API_KEY = 'abcdef';
```

```
function doGet(e) {  if (!isAuthorized(e)) {    return buildErrorResponse('not authorized');  }      return buildSuccessResponse('authorized');}
```

```
function isAuthorized(e) {  return 'key' in e.parameters && e.parameters.key[0] === API_KEY;}
```

```
function buildSuccessResponse(message) {  var output = JSON.stringify({    status: 'success',    message: message  });    return ContentService.createTextOutput(output)   .setMimeType(ContentService.MimeType.JSON);}
```

```
function buildErrorResponse(message) {  var output = JSON.stringify({    status: 'error',    message: message  });    return ContentService.createTextOutput(output)   .setMimeType(ContentService.MimeType.JSON);}
```

The API key is defined as `abcdef` at the top of the file. The `isAuthorized`function returns a boolean value for authentication. If this returns false a `not authorized` message is returned through the `buildErrorResponse` helper. If `isAuthorized` returns true, the function is allowed to continue until a successful response is returned through `buildSuccessResponse`.

A drawback I’ve found when building applications on Google Apps Script is that you don’t have the capability to set status codes for responses. These can be used to indicate whether the response was successful and if not, why.

For example, a [401 Unauthenticated](https://httpstatuses.com/401) status code implies that the user credentials didn’t match and that they should try again using different credentials. Responses always have a [200 OK](https://httpstatuses.com/200) status code when using `doGet`, even for handled unsuccessful responses. I get around this by adding a `status` value to all the API responses. For this simple example, the status can either be `success` or `error`, but it’s easy to see how this pattern could be extended for other more granular statuses if required.

Let’s create two functions to parse the `category` and `page` parameters. If a valid numerical `page` isn’t supplied, its default value should be `1`. Likewise if a category isn’t provided, the default value should be set to `null`, in which case posts from all categories should be returned.

```
function getPageParam(e) {  if ('page' in e.parameters) {    var page = parseInt(e.parameters['page'][0]);    if (!isNaN(page) && page > 0) {      return page;    }  }    return 1}
```

```
function getCategoryParam(e) {  if ('category' in e.parameters) {    return e.parameters['category'][0];  }    return null}
```

#### Reading from the spreadsheet

Google Apps Script makes various global objects available that can be used to interact with G Suite products. We’ll use the [SpreadsheetService](https://developers.google.com/apps-script/reference/spreadsheet/) to load our spreadsheet by ID and read the blog posts. The easiest way to look up a spreadsheet ID is by checking the Google Sheets URL for it.

```
https://docs.google.com/spreadsheets/d/{id}/edit
```

After loading the spreadsheet through the `openById` method on the global `SpreadsheetService`, we need to get the active data range from the first worksheet. To return the most recent posts first, we should sort on the **Timestamp** column, which is the second column.

```
var SPREADSHEET_ID = '12345';var spreadsheet = SpreadsheetApp.openById(SPREADSHEET_ID);var worksheet = spreadsheet.getSheets()[0];var rows = worksheet.getDataRange() .sort({column: 2, ascending: false}) .getValues();
```

The `rows` array from `getDataRange` contains both the columns headings as the first array item and the blog post rows as subsequent array items. Headings can be mapped to blog posts so that the API can return full blog post objects rather than just the column values.

```
var headings = rows[0].map(String.toLowerCase);var posts = rows.slice(1);var postsWithHeadings = addHeadings(posts, headings);
```

```
function addHeadings(posts, headings) {  return posts.map(function(postAsArray) {    var postAsObj = {};        headings.forEach(function(heading, i) {      postAsObj[heading] = postAsArray[i];    });        return postAsObj;  });}
```

#### Filtering irrelevant posts

Blog posts should only be returned if their category matches the one requested, and posts from all categories should be returned if one wasn’t requested. Blog posts should also further only be returned if they have a `**Published**` value of **true**.

Let’s create a function to remove draft posts by an [array filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter):

```
var postsPublic = removeDrafts(postsWithHeadings);
```

```
function removeDrafts(posts, category) {  return posts.filter(function(post) {    return post['published'] === true;  });}
```

And another function to `filter` on the post category:

```
var category = getCategoryParam(e);var postsFiltered = filter(postsPublic, category);
```

```
function filter(posts, category) {  return posts.filter(function(post) {    if (category !== null) {      var c1 = post['category'].toLowerCase()      var c2 = category.toLowerCase()      return c1 === c2;    } else {      return true;    }  });}
```

#### Paginating responses

For performance reasons, we should limit the maximum number of posts returned by a single API response. The client should be able request the next page of posts by increasing the `page` query parameter.

Let’s implement this through a pagination function that returns an object containing the filtered blog posts under `posts` and pagination links under `pages`. If there are more or previous results, `pages` contains the appropriate page number under `next` and `previous` respectively.

```
var RESULTS_PER_PAGE = 5;var page = getPageParam(e)var paginated = paginate(postsFiltered, page);
```

```
function paginate(posts, page) {  var postsCopy = posts.slice();  var postsChunked = [];  var postsPaginated = {    posts: [],    pages: {      previous: null,      next: null    }  };    while (postsCopy.length > 0) {    postsChunked.push(postsCopy.splice(0, RESULTS_PER_PAGE));  }    if (page - 1 in postsChunked) {    postsPaginated.posts = postsChunked[page - 1];  } else {    postsPaginated.posts = [];  }
```

```
  if (page > 1 && page <= postsChunked.length) {    postsPaginated.pages.previous = page - 1;  }    if (page >= 1 && page < postsChunked.length) {    postsPaginated.pages.next = page + 1;  }    return postsPaginated;}
```

Our `buildSuccessResponse` helper from earlier can be updated to handle `posts` and `pages`. The API should then ready for deployment.

```
function buildSuccessResponse(posts, pages) {  var output = JSON.stringify({    status: 'success',    data: posts,    pages: pages  });    return ContentService.createTextOutput(output)    .setMimeType(ContentService.MimeType.JSON);}
```

#### Deploying the API

With the script finalized, the API can be made publicly available by going to **Publish > Deploy as weba**pp from the script editor menu bar. Ensure the app is being executed **as** me and th**at anyone, even anonym**ous has access.

Deploying will return a URL that will look like the one below:

```
https://script.google.com/macros/s/{id}/exec
```

Append the API key to the URL and then enter it into your web browser to check that the API is working correctly. Hopefully you should see a JSON response with three top level keys: `status`, `posts`, `pages`.

```
https://script.google.com/macros/s/{id}/exec?key=abcdef
```

### Summary

If you followed along you should now have a functional CMS built on Google Sheets, Google Forms, and Google Apps Script. It’s not advanced, but it was easy to get started and delivers the core requirements of a CMS. Connecting it to a front-end was outside the scope of this article, but if you want to see how that is done, you should check out the demo I put together [on GitHub](https://github.com/danielireson/google-sheets-blog-cms).

Next time you’re about to reach for the technology flavor of the day, I challenge you to take a few moments to think about whether there’s an easier solution that can be built using existing software. That solution might not be fully featured, but it will often get you [80% of the way there for 20% of the effort](https://en.wikipedia.org/wiki/Pareto_principle), which in many cases will be good enough. I hope this blog post demonstrated that and that you learned a thing or two about Google Apps Script along the way.

#### [View the demo](https://danielireson.github.io/google-sheets-blog-cms)

#### [View the project on GitHub](https://github.com/danielireson/google-sheets-blog-cms)

![Image](https://cdn-media-1.freecodecamp.org/images/mja7cLraj-m84aPQRLYXru7c3tIBYr38l9XS)

