---
title: How to generate an HTML table and a PDF with Node & Google Puppeteer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-15T21:53:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-generate-an-html-table-and-a-pdf-with-node-google-puppeteer-32f94d9e39f6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vmoUk8zB0XXR2l203rw7fQ.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Adeel Imran


  _Photo by [Unsplash](https://unsplash.com/@lobosnico?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit">Nicolas
  Lobos / <a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utmcampaign=api-credit)

  Understandi...'
---

By Adeel Imran

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-244.png)
_Photo by [Unsplash](https://unsplash.com/@lobosnico?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Nicolas Lobos</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Understanding NodeJS internally can be a little bit daunting (I know it was for me once). Node is a very powerful language and it can do a lot of things.

Today I wanted to uncover the power of Node’s built-in utility tool called [fs](https://nodejs.org/api/fs.html) ([file system](https://nodejs.org/api/fs.html))

As per the [fs](https://nodejs.org/api/fs.html) docs:

> The `fs` module provides an API for interacting with the file system in a manner closely modeled around standard POSIX functions.

Which is just a fancy way of saying that [file system](https://nodejs.org/api/fs.html) is a way in Node to interact with files for both read and write operations.

Now [file system](https://nodejs.org/api/fs.html) is a humongous utility in NodeJS that has a lot of fancy features. In this article, however I will only discuss 3:

* Getting file information: **_fs.statSync_**
* Deleting a file: **_fs.unlinkSync_**
* Writing data to a file: **_fs.writeFileSync_**

Another thing we will cover in this article is [Google Puppeteer](https://developers.google.com/web/tools/puppeteer/) which is this really cool, slick tool created by some awesome folks at Google.

So what is puppeteer? Well as per the docs, they say:

> Puppeteer is a Node library which provides a high-level API to control [headless](https://developers.google.com/web/updates/2017/04/headless-chrome) Chrome or Chromium over the [DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/). It can also be configured to use full (non-headless) Chrome or Chromium.

So it’s basically a tool that lets you do all the cool browser related things on server. Like getting a website’s screenshots, crawling websites, and generating pre-render content for single page applications. You can even do form submissions via your NodeJS server.

Again puppeteer is a huge tool, so we will cover just a small but a very cool feature of puppeteer. We’ll look at how to generate a nice PDF file based on our generated HTML table file. In the process we’ll learn about puppeteer.launch() and understand a bit about page() & pdf().

#### So to again give a brief overview, things we will cover:

* Generating stub data (for invoices) using an online tool.
* Creating an HTML table with a little bit of styling with generated data in it, using an automated node script.
* Learning about checking if a file exists or not using fs.statSync
* Learning about deleting a file by using fs.unlinkSync
* Learning about writing a file using fs.writeFileSync
* Creating a PDF file of that HTML file generated using Google puppeteer
* Making them into npm scripts, to be used later ? ?

> Also before we begin here is the entire [source code of the tutorial](https://github.com/adeelibr/understaning-node-fs-and-puppeteer), for everyone to follow along. You don’t have to write anything, but you should write code along with this tutorial. That will prove more useful & you’ll understand more. [**_SOURCE CODE OF TUTORIAL_**](https://github.com/adeelibr/understaning-node-fs-and-puppeteer)

Before we begin, please ensure that you have at least the following installed on your machine

* Node version 8.11.2
* Node Package Manager (NPM) version 6.9.0

You don’t need to, but you can also watch an introductory video (my first ever made) that talks about the basics in reading, writing, and deleting a file in NodeJS. This will help you understand this tutorial. (Please do give me feedback). ?

%[https://youtu.be/7tc_lYelc-U]

### Let’s get started

#### **Step 1:**

In your terminal type in the following:

```
npm init -y
```

This will initialize an empty project for you.

#### Step 2:

Second, in the same folder, create a new file called `data.json` and have some mocked data in it. You can use the following JSON sample.

You can get the mocked JSON stub data from [**here**](https://gist.github.com/adeelibr/69d2ca9d40642aaf99721796da0aaa64)**.** For generating this data I have used an awesome tool called [https://mockaroo.com/](https://mockaroo.com/) It is an online data generator tool.

The JSON data I am going with has a structure like this:

```js
[
  {},
  {},
  {
   "invoiceId": 1,
   "createdDate": "3/27/2018",
   "dueDate": "5/24/2019",
   "address": "28058 Hazelcrest Center",
   "companyName": "Eayo",
   "invoiceName": "Carbonated Water - Peach",
   "price": 376
  },
  {
   "invoiceId": 2,
   "createdDate": "6/14/2018",
   "dueDate": "11/14/2018",
   "address": "6205 Shopko Court",
   "companyName": "Ozu",
   "invoiceName": "Pasta - Fusili Tri - Coloured",
   "price": 285
  },
  {},
  {}
]
```

> You can download the complete JSON array for this tutorial from [**here**](https://gist.github.com/adeelibr/69d2ca9d40642aaf99721796da0aaa64)**.**

#### Step 3:

Next create a new file called `buildPaths.js`

```js
const path = require('path');
const buildPaths = {
   buildPathHtml: path.resolve('./build.html'),
   buildPathPdf: path.resolve('./build.pdf')
};
module.exports = buildPaths;
```

So `path.resolve` will take in a relative path and return us the absolute path of that particular directory.

So `path.resolve('./build.html');` will for example return something like this:

```
$ C:\\Users\\Adeel\\Desktop\\articles\\tutorial\\build.html
```

#### **Step 4:**

In the same folder create a file called `createTable.js` and add the following code:

```js
const fs = require('fs');
// JSON data
const data = require('./data.json');
// Build paths
const { buildPathHtml } = require('./buildPaths');

/**
 * Take an object which has the following model
 * @param {Object} item 
 * @model
 * {
 *   "invoiceId": `Number`,
 *   "createdDate": `String`,
 *   "dueDate": `String`,
 *   "address": `String`,
 *   "companyName": `String`,
 *   "invoiceName": `String`,
 *   "price": `Number`,
 * }
 * 
 * @returns {String}
 */
const createRow = (item) => `
  <tr>
    <td>${item.invoiceId}</td>
    <td>${item.invoiceName}</td>
    <td>${item.price}</td>
    <td>${item.createdDate}</td>
    <td>${item.dueDate}</td>
    <td>${item.address}</td>
    <td>${item.companyName}</td>
  </tr>
`;

/**
 * @description Generates an `html` table with all the table rows
 * @param {String} rows
 * @returns {String}
 */
const createTable = (rows) => `
  <table>
    <tr>
        <th>Invoice Id</td>
        <th>Invoice Name</td>
        <th>Price</td>
        <th>Invoice Created</td>
        <th>Due Date</td>
        <th>Vendor Address</td>
        <th>Vendor Name</td>
    </tr>
    ${rows}
  </table>
`;

/**
 * @description Generate an `html` page with a populated table
 * @param {String} table
 * @returns {String}
 */
const createHtml = (table) => `
  <html>
    <head>
      <style>
        table {
          width: 100%;
        }
        tr {
          text-align: left;
          border: 1px solid black;
        }
        th, td {
          padding: 15px;
        }
        tr:nth-child(odd) {
          background: #CCC
        }
        tr:nth-child(even) {
          background: #FFF
        }
        .no-content {
          background-color: red;
        }
      </style>
    </head>
    <body>
      ${table}
    </body>
  </html>
`;

/**
 * @description this method takes in a path as a string & returns true/false
 * as to if the specified file path exists in the system or not.
 * @param {String} filePath 
 * @returns {Boolean}
 */
const doesFileExist = (filePath) => {
	try {
		fs.statSync(filePath); // get information of the specified file path.
		return true;
	} catch (error) {
		return false;
	}
};

try {
	/* Check if the file for `html` build exists in system or not */
	if (doesFileExist(buildPathHtml)) {
		console.log('Deleting old build file');
		/* If the file exists delete the file from system */
		fs.unlinkSync(buildPathHtml);
	}
	/* generate rows */
	const rows = data.map(createRow).join('');
	/* generate table */
	const table = createTable(rows);
	/* generate html */
	const html = createHtml(table);
	/* write the generated html to file */
	fs.writeFileSync(buildPathHtml, html);
	console.log('Succesfully created an HTML table');
} catch (error) {
	console.log('Error generating table', error);
}
```

I know that is a lot of code, but let’s divide it into chunks and start understanding it piece by piece.

Go to **_line 106_** _([github gist](https://gist.github.com/adeelibr/70936277d38f3c77d3910e417581e98a#file-createtable-js))_

In our `try/catch` block we first check if the build file for HTML exists in the system or not. This is the path of the file where our NodeJS script will generate our HTML.

`if (doesFileExist(buildPathHtml){}` calls doesFileExist() method which simply returns true/false. For this we use

```
fs.statSync(filePath);
```

This method actually returns information about the file like the size of the file, when the file was created, and so on. However if we provide it an invalid file path, this method returns as a null error. Which we use here to our benefit and wrap the `fs.statSync()` method in a `try/catch`. If Node is successfully able to read the file in our try block, we return `true` — otherwise it throws an error which we get in our catch block and returns `false`.

If the file exists in the system we end up deleting the file using

```
fs.unlinkSync(filePath); // takes in a file path & deletes it
```

After deleting the file, we need to generate rows to put in the table.

#### Step 5:

So first we import `data.json` which we do at **_line 3_** & then on **_line 115_** we iterate each item using map(). You can read more about [Array.prototype.map() here.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

The map method takes a method `createRow` which takes in an object through each iteration and returns a string which has content like this:

```html
"<tr>
  <td>invoice id</td>
  <td>invoice name</td>
  <td>invoice price</td>
  <td>invoice created date</td>
  <td>invoice due date</td>
  <td>invoice address</td>
  <td>invoice sender company name</td>
</tr>"
```

> `const row = data.map(createdRow).join('');`

The `join('')` part is important here, because I want to concatenate all of my array into a string.

An almost similar principle is used for generating a table on **_line 117_** & then the html table on **_line 119._**

#### **Step 6:**

The important part is where we write to our file on **_line 121_**:

```
fs.writeFileSync(buildPathHtml, html); 
```

It takes in 2 parameters: one is the build path (string) and the html content (string) and generates a file (if not created; and if it is created, it overwrites the already existing file).

> One thing to note here we might not need Step 4, where we check if the file exists & if it does then delete it. This is because writeFileSync does that for us. I just added that in the code for learning purposes.

#### Step 7:

In your terminal, go in the folder path where you have the `createTable.js` and type

```
$ npm run ./createTable.js
```

As soon as you run this script, it will create a new file in the same folder called `build.html` You can open that file in your browser and it will look something like this.

![Image](https://cdn-media-1.freecodecamp.org/images/lnYaAbNKig8Zhhuqh1QQDnMGFcQ1KNcHAA2I)
_Generated HTML table._

> Cool right? So far so good. _?_

Also you can add an `npm script` in your package.json like this:

```js
"scripts": {
  "build:table": "node ./createTable.js"
},
```

This way instead of writing `npm run ./createTable.js`, you can just type in `npm run build:table`.

Next up: generating a PDF from the generated `HTML` file.

#### Step 8:

First things first we need to install a fancy tool, so go in your terminal in your application folder and type in

```
npm install puppeteer
```

#### **Step 9:**

In the same folder where you have files `createTable.js` , `buildPaths.js` & `data.json`, create a new file called `createPdf.js` and add content to it like below:

```js

const fs = require('fs');
const puppeteer = require('puppeteer');
// Build paths
const { buildPathHtml, buildPathPdf } = require('./buildPaths');

const printPdf = async () => {
	console.log('Starting: Generating PDF Process, Kindly wait ..');
	/** Launch a headleass browser */
	const browser = await puppeteer.launch();
	/* 1- Ccreate a newPage() object. It is created in default browser context. */
	const page = await browser.newPage();
	/* 2- Will open our generated `.html` file in the new Page instance. */
	await page.goto(buildPathHtml, { waitUntil: 'networkidle0' });
	/* 3- Take a snapshot of the PDF */
	const pdf = await page.pdf({
		format: 'A4',
		margin: {
			top: '20px',
			right: '20px',
			bottom: '20px',
			left: '20px'
		}
	});
	/* 4- Cleanup: close browser. */
	await browser.close();
	console.log('Ending: Generating PDF Process');
	return pdf;
};

const init = async () => {
	try {
		const pdf = await printPdf();
		fs.writeFileSync(buildPathPdf, pdf);
		console.log('Succesfully created an PDF table');
	} catch (error) {
		console.log('Error generating PDF', error);
	}
};

init();
```

As we did with `createTable.js` script, let’s break this down into chunks and start understanding this script step by step.

Let’s start with **[line 40:](https://gist.github.com/adeelibr/57081ec24b634b4d161e405ae3bf6d78#file-createpdf-js-L40)** here we call a method **_init()_** which calls the method on **[line 30](https://gist.github.com/adeelibr/57081ec24b634b4d161e405ae3bf6d78#file-createpdf-js-L30).** One thing to focus on is that our init() method is an async method. Read more on this [async function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function).

First in the init() method we call **_printPdf()_** method which is again an async method, so we have to wait for its response. The printPdf() method returns us a PDF instance which we then write to a file on **[line 33](https://gist.github.com/adeelibr/57081ec24b634b4d161e405ae3bf6d78#file-createpdf-js-L33).**

So what does the `printPdf()` method do? Let’s dig deep in it.

```js
const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.goto(buildPathHtml, { waitUntil: 'networkidle0' });
const pdf = await page.pdf({
  format: 'A4',
  margin: {
   top: '20px', right: '20px', bottom: '20px', left: '20px'}
});
await browser.close();
return pdf;
```

We first launch a headless browser instance using puppeteer by doing the following:

```
await puppeteer.launch(); // this returns us headless browser
```

which we then use to open a web page:

```
await browser.newPage(); // open a blank page in headless browser
```

Once we have a blank page open we can navigate to a page. Since our web page is locally in our system, we simply

```
page.goto(buildPathHtml, { waitUntil: 'networkidle0' });
```

Here `waitUntil: 'networkidle0;` is important, because it tells puppeteer to wait for 500/ms until there are no more network connections.

> **_Note:_** This is why we used path.resolve() to get absolute paths, because in order to open the web page with puppeteer, we need an absolute path.

After we have a web page opened in the headless browser on the server, we save that page as a pdf:

```
await page.pdf({ });
```

As soon as we have a pdf version of the web page, we need to close the browser instance opened by puppeteer to save resources by doing this:

```
await browser.close();
```

& then we return the `pdf` saved, which we then write to the file.

#### Step 10:

In your terminal type

```
$ npm ./createPdf.js
```

Note: Before running the above script, ensure that you the `build.html` file generated by `createTable.js` script. This ensures we always have the `build.html` prior to running the `createPdf.js` script. In your `package,json` do the following.

```
"scripts": {
  "build:table": "node ./createTable.js",
  "prebuild:pdf": "npm run build:table",
  "build:pdf": "node ./createPdf.js"
},
```

Now if you run `**$** npm run build:pdf` it will execute the `createTable.js` script first and then `createPdf.js` script. You can read more on [NPM scripts](https://docs.npmjs.com/misc/scripts) on their official [docs](https://docs.npmjs.com/misc/scripts).

When you run

```
$ npm run build:pdf
```

It will run and create a `build.pdf` which will look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/UOMwXytU2JyC8VlsgaM-wXF-9D9icvPpLlnC)
_Generated .pdf file on running **createPdf.js** script_

And that is it, we are done.

You have learned the following:

* How to check if a file exists / tet file information (in Node)
* How to delete a file in Node
* How to write to a file
* How to use Google Puppeteer to generate a PDF file

Happy learning, I would love to hear your thoughts on this article. You can reach me on [**_twitter_**](https://twitter.com/adeelibr) as well.

