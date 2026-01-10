---
title: How to set up server-side rendering in React with Rails using Puppeteer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-21T06:00:04.000Z'
originalURL: https://freecodecamp.org/news/server-side-rendering-react-with-rails-using-puppeteer-cf5ec2697e88
coverImage: https://cdn-media-1.freecodecamp.org/images/0*JDwIoDI39Uzjzp5c
tags:
- name: General Programming
  slug: programming
- name: puppeteer
  slug: puppeteer
- name: Rails
  slug: rails
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sitaram Shelke

  This post is co-authored by Hricha Kabir, my colleague at Altizon Systems. She was
  working on this task primarily. I had the chance to learn along the way.


  _Photo by [Unsplash](https://unsplash.com/@rvruggiero?utm_source=medium&utm...'
---

By Sitaram Shelke

This post is co-authored by [Hricha Kabir](https://in.linkedin.com/in/hrichakabir), my colleague at [Altizon Systems](http://www.altizon.com). She was working on this task primarily. I had the chance to learn along the way.

![Image](https://cdn-media-1.freecodecamp.org/images/SFMTJgWJQqSDFXU-rUJrn4HkgCccugY1GpYh)
_Photo by [Unsplash](https://unsplash.com/@rvruggiero?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Robert V. Ruggiero</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

We work on an IoT product focusing on manufacturing industries and build analytics reports. Most of the time, report design and information vary based on the user’s role who is going to consume it.

Example: A Director level person is interested in a consolidated report of a week, whereas a Department Head is interested in the statistics of a single day and Quality Manager is keen about shift data. If we further drill down the hierarchy, then the Production Manager will be the one who wants to look into live production data.

For live data, Production manager can open the Live Dashboard and monitor it, but the user who wants to see a consolidated report won’t prefer to login into Product and check out a report. Instead, they prefer scheduled email communication which will send a report based on scheduled time and repeat it forever until unless a user stopped this scheduled job.

So our task was to write a utility which periodically sends a particular report to a user via email on a daily basis or at a defined scheduled time. For scheduling, we use [Sidekiq](https://sidekiq.org/), but our main challenge was: how to execute/calculate the report on the server side (without opening a browser) and send it over email.

In all of our products, we use **React** for the front-end and it does the heavy lifting of rendering the report on the browser. To achieve attaching the same report in the email, we would have to design an HTML template for every report. That means we would have had 2 views of each report, one written in HTML and another in ReactJS.

This has following drawbacks:

**1.** The product code base will have duplicate code which violates the DRY principle for software development.

**2.** Increases the time for designing a report which impacts product delivery.

We decided to look at other possible solutions instead of writing the same code twice. And we came across following options and explored them one by one until we succeeded in achieving our goal.

**1. Print Screen:** Print the report using print screen and send it as an attachment.

**2. FrontEnd Print Button:** In report’s UI, add a Print Button which will convert react component into HTML/PDF page.

**3. Ruby Gem:** There is a ruby gem which can render a report component on the server side within Rails, generate its HTML and send it as an email body.

**4. Server-Side Rendering with Node server:** Use serverside rendering using ReactDOMServer and [headless](https://developers.google.com/web/updates/2017/04/headless-chrome) browser protocol to render HTML and JS and generate a pdf.

Now we will go through the details of each solution.

#### **Print Screen:**

It was the simplest solution we had and it requires user input. A user needs to be present with a system who will do a screen capture as an image and attach it over the mail. But this doesn’t scale. Also what if a user wants a report at a scheduled time or sent periodically?

Example**:** Every week at 8 pm. It’s not possible for a person to do this. This also suffers from the inability to fully capture a scrollable page, so we had to drop this idea.

#### **FrontEnd Print Button:**

After doing some search, we found out there are some browser extensions available which produce a full image of an opened page. Example: Full Page Screen Capture in Chrome. After adding this extension to the browser, we would be able to capture any screen in image(png/jpg) format.

Again this solution requires no development but suffers from some of the previous scaling and scheduling issues. At the same time, we would still need a user logged in to the browser to perform this action, which defeats the purpose of email delivery.

#### **RubyGem:**

Soon we realized that our solution cannot require browser interaction. We would need to use [server-side rendering](https://alligator.io/react/server-side-rendering/). So we started exploring Ruby Gems which support server-side rendering with React. We explored the following Gems

**3.1 [rails_react_stdio](https://github.com/aaronvb/rails_react_stdio):**

It is based on [react-stdio](https://github.com/ReactTraining/react-stdio) which supports server-side rendering irrespective of server-side technology. It acts as a binary which will do the work of rendering react components. For rendering React Component on the server side we need to pass the file path of the react component and props if required. It will return a JSON response which will have the HTML code of the report. Further we can send HTML content over email.

Internally this gem uses _popen3_ for executing render command. But this means that _react-stdio_ binary needs to be present in the docker container where our rails app is running.

This is not great from a point of view of maintainability and reproducibility. Additionally having large HTML content with charts can be slow to load so we preferred pdf attachment. Yet we gave it a try.

Example**:** For rendering a report which has the component _TestComponent_ and the file path _app/assets/javascripts/components/TestComponent.jsx_

First, include the gem in Gemfile:

```rb
gem ‘rails_react_stdio’, ‘~> 0.1.0’
```

Now from the email scheduler call the gem method to render the report and get the HTML from the response. Then send this response to email.

```rb
email_body = RailsReactStdio::React.render(‘app/assets/javascripts/components/TestComponent.jsx’, {city: “Pune”})
```

We tried using the above method but had no success. Also the GitHub repo was not actively maintained, and all of its test cases were failing. So we decided to move forward without this.

**3.2 react-rails:**

The ReactJS community built this gem. It uses [ExecJS](https://github.com/rails/execjs) for executing render-action of a react component on the server side. We just need to pass one flag _‘prerender’: true_.

```js
<%= react_component(‘Dashboard’, {name: ‘Example’}, {prerender: true}) %>
```

This prerendering process does not have access to the window or document so it does not load runtime JavaScript or CSS. We also use JQuery for a few things so it wouldn’t work as well.

There is an alternative: this gem has another class for server-side rendering, _ExecJSRenderer_, which helps in availing JavaScript to a component on the server side.

_ExecJSRenderer_ Class has 2 methods: _before_render_ and _after_render,_ which gives access to the JavaScript required before and after component rendering. But it’d require a lot of changes in the existing code base for supporting server-rendering, in every controller. Apart from this, ExecJS doesn’t provide sandboxing as well as runtime error information. We were still looking for something better.

#### **Server-Side Rendering with Node server:**

Most of the ruby gems we explored internally created the node server and rendered react on the server side. So instead of using Ruby, we decided to directly use the node server and achieve this task ourselves.

**4.1 ReactDOMServer based solution:**

Here we use [ReactDOMServer](https://reactjs.org/docs/react-dom-server.html). It is the preferred solution for server-side rendering from the React team. We created a node server which calls the _renderToString()_ method with a react component. It returns the rendered content which we combine with HTML and send over email.

Example**:**

```js
server.get(‘/’, (req, res, next) => {
  /**
  * renderToString() will take our React app and turn it into a      string
  * to be inserted into our Html template function.
  */
  console.log(‘started’)
  const body = renderToString(<App />);
  const title = ‘Server side Rendering React Components’;
  var result = Html({ body, title })
}
```

The _renderToString()_ method returns a string response. We pass this response to an HTML template and send the template over mail.

When we tested this out, an email was received as expected except all the images used in the report were broken. The email was not able to resolve the image source relative path.

To get the correct images in the email, we would either need to

* Store images in S3 and use the source URL in the report: So now we would be adding S3 image URLs in the email, and the email server would directly load images from the S3 server. It would require extra cloud space for storing images, and downloading from destination requires another network call from the email inbox.

Or

* Send base64 code of image in the mail: Instead of image URL, we can send the base64 code of an image. Although It increases network payload, many mail servers such as Outlook and Gmail block base64 images.

So we would still need to do something about this.

**4.2 [Puppeteer](https://github.com/GoogleChrome/puppeteer):**

After exploring the above methods, we discovered Puppeteer Headless Chrome service. Puppeteer is a NodeJS library from the Google Chrome team, used in end to end testing. By default, it uses the Chrome/Chromium browser for the same. Essentially it simulates all the actions a user can perform in the browser. Example: Keyboard Input, Mouse events, Form submission etc.

The result of a puppeteer request can be an HTML page, Screenshot, or PDF. In case of HTML, it renders the full page on the server side along with all images, CSS, and JavaScript. Or a user can render a page on the server side and if required they can generate a screenshot or a pdf.

If we use this library with a Node server, we can schedule a task within Sidekiq which would make a request to this server, render a report, and send it over email. Puppeteer also has a rich set of APIs which support in sending customizing headers in the request which help us in authenticating a background request.

This is exactly what we needed!

**So the overall request lifecycle inside puppeteer should look like this:**

**1.** It launches the browser

**2.** Creates a page on the browser

**3.** Authenticate with the Report Application server

**4.** Opens the report URL that the user wants and returns the rendered page content

**5.** Based on the user’s requirement, stores HTML of the rendered page or takes a Screenshot or generates a PDF.

We can use either the default browser (gets downloaded when we install puppeteer) or we can give a specific browser version. If we give a specific browser version, then we will have to make sure that puppeteer APIs are compatible with the given browser.

All of the above can be achieved using the following steps.

**1. Install puppeteer:**

It downloads the default Chrome/Chromium browser. So If we want to launch the default browser and install puppeteer:

```bash
npm install puppeteer
```

**2. Serve a Request:**

Build a server which will receive a request and implement a request lifecycle and return the desired result.

The following is the code snippet we use for generating a pdf of a given page URL.

```js
const puppeteer = require(“puppeteer”);
const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.emulateMedia(“screen”);
await page.goto(‘https://www.google.com', {
      timeout: 30 * 1000, 
      waitUntil: “networkidle0”
});
await page.pdf(pdfOptions);
return page;
```

As we already mentioned in the lifecycle steps above, it first launches the browser. Then it creates and opens a page in the launched browser. Here along with the URL, we have passed _timeout_ and _waitUntil_ params which are given for the following reasons:

* _timeout_: If we want to restrict a request time then we can pass it to timeout variable
* _waitUntil_: if networkidle0 is given, then the next request will not be served until or unless the current one is completed.

In the end, rendered content will be passed to the pdf method and it will generate a pdf. We can also provide PDF formatting options like page height, page width, headers, footers, and margins.

Additionally, we have called page.emulateMedia(“screen”); which applies CSS to the page. If we don’t add emaulateMedia, our PDF doesn’t load the CSS.

Apart from what we have used, there are many different configuration options with Puppeteer APIs. Visit the [API docs](https://github.com/GoogleChrome/puppeteer/blob/v1.12.2/docs/api.md#) for more information.

If you found this helpful or if you have any suggestions, please feel free to write them it in comments.

That’s all folks.

