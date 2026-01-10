---
title: How to Work with Files in Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-11T21:16:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-files-in-node-js
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/working-with-files.png
tags:
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
seo_title: null
seo_desc: 'By Oluwatise Okuwobi

  JavaScript is a popular programming language among web developers. But when it was
  first released, only front end developers enjoyed all of the fun it had to offer,
  since you couldn''t run JavaScript outside the browser.

  But then ...'
---

By Oluwatise Okuwobi

JavaScript is a popular programming language among web developers. But when it was first released, only front end developers enjoyed all of the fun it had to offer, since you couldn't run JavaScript outside the browser.

But then in 2009, the first version of Node.js was released. Node is a JavaScript runtime that lets you run JS code outside the browser, and it gave backend developers the joy of using JavaScript as well.

Now, Node.js powers backend JavaScript development and is the 6th most used technology among programmers.

As a backend developer you'll need to understand how to effectively work with and process files in Node.js. And that's what we'll discuss here.

## Before you start writing code...

Let's talk prerequisites. Do you need an extensive amount of Node knowledge to follow this article? No. But you should understand a good amount of JavaScript to fully enjoy this guide.

Also, you have to install Node on your computer if it's not already installed. The installation process is easy – all you have to do is download [Node.js from the official site](https://nodejs.org/en/download) and follow the installation prompt and you are good to go.

## The Node.js File System

Node acts as a file server. With the Node module you can work with files on your computers and carry out various operations. When you're building a web app, you might want to upload images, a résumé, videos, or docs to the server. Well, the Node file system has the ability to do all of that and more.

Since this is a beginner-friendly guide, I'll explain what Node modules are in general first before we talk more in-depth about the file system.

### What are Node modules?

Incase you're not familiar with the term, Node modules are simply reusable JavaScript code. You can easily import modules along the line throughout your project. The purpose of modules is to ensure that you're not constantly repeating the same code throughout a project.

There are multiple types of Node modules – local modules, built-in modules, and third-party modules. In this guide we'll focus on the built-in modules.

Here's a list of Node's built-in modules:

* fs
* http
* url
* os
* path

The fs is the file system module in Node. It's all making sense now, right? There's a whole library of node modules. If you want to know more about them, you should read more on [Node modules and how you can use them.](https://www.freecodecamp.org/news/what-are-node-modules/) Let's keep going!

## How to Work with the Node `fs` Module

The `fs` module allows you to carry out several operations that involve files and folders. With the `fs` module you can:

* read files
* create files
* update files
* delete files
* rename files

To get started with this world of file handling, first we'll create a folder. Then we'll create a JavaScript file for now. Open the JS file with VS Code or any text editor you are happy with, and let's write some code.

### How to Read Files

To read the files directly from your computer, you'll have to use the use the `fs.readFile()` method. For this to work you'll need to create the file you want to read. Let's assume that it's a txt file with the content `hello world`. Let's call it dummyText.txt.

Now there are multiple ways you can read a file with Node – either using the `http` module, which will read your file on the localhost, or using promises. I'm going to show you both, and which one is preferable.

Let's start with using the `http` module. Open your JS file, let's call it `readfile.js`, and add the following code:

```
const http = require('http'); 
const fs = require('fs');

http.createServer(function (req, res) { 
   fs.readFile('dummyText.txt', function(err, data) { 
      res.writeHead(200, {'Content-type': 'text/html'}); 
      res.write(data);           
      return res.end(); 
    }); 
 }).listen(8080);
```

Save the code, and then open `cmd` in the file directory and run Node readfile.js:

‌ `C:\Users\nodefilesystem>node readfile.js`

Visit https://localhost:8080 to see your results. You should see the content of the dummy text on your browser.

Now let's recreate this with promises. The promise way is a more modern programming style, as we'll incorporate the new _async_ and _await_ syntax_._ Let's read our file using promises.            

```
// import promises 
const { readFile } = require('fs/promises'); 

async function readThisFile('./dummytext.txt') { 
  try { 
    const data = await readFile('/dummytext.txt');
    console.log(data.toString()); 
  } catch (error) { 
    console.error(`Got an error trying to read the file: {error.message}`); 
  } 
 }
```

Let's explain the code. So we imported the Node promises module using the file system. We used `fs/Promises` to processes our files with promises.

We used the `readFile` method to process our file that we want to read. Using promises we can read our files in an asynchronous manner. Inside the `readFile` method we have the path to our `dummytext` that we want to read, then return the content of the file.

We also used a try-catch error handling method to ensure that we can properly control what the error message reads. So, if there's something wrong with the code before the catch line, It'll output "Got an error trying to read the file", instead of an untidy error message.

Error-handling will also prevent the program from stopping when it spots an error. With our code, the program can still resume even if it's interrupted.

If you want to read more on this, here's a great resource from freeCodeCamp about [error-handling in JavaScript.](https://www.freecodecamp.org/news/error-handling-and-try-catch-throw/)

### How to Create Files

Now that we're familiar with the promises method of working with the file system, we're going to be using that throughout the rest of the guide. Now that we know how to read the contents off an existing file, how about we learn how to create them?

To create a file we can use one of three methods: `appendFile()`, `open()`, and `writeFile()`.

Let's open our text editor and start with `appendFile()`:

```
const { appendFile} = require('fs/promises'); 

async function appendToFile('anotherDummyText.txt', 'i love node') { 

  try { 
    await appendFile(fileName, data, { flag: 'w' });                   console.log(`Appended data to ${fileName}`); 
  } catch (error) { 
    console.error(`Got an error trying to append the file: {error.message}`); 
  } 
 }
```

Let's explain the code a little bit more. We already called the module, and now we are using the `appendFile` method to write to the file we created earlier. If the program doesn't see any file with the name we stated in the `appendToFile` function, it'll create it.

Also we used the try-catch error handling method to make sure to control the errors.

Next, we'll work with `WriteFile`. It's pretty much the same code, but with a few adjustments:

```
const { writeFile } = require('fs/promises'); 

async function writeToFile('dummyText.txt', 'using write method') { 
   try { 
     await writeFile(fileName, data); 
     console.log(`Wrote data to ${fileName}`); 
   } catch (error) { 
     console.error(`Got an error trying to write the file: ${error.message}`); 
   } 
 }
```

Now we are using the `writeFile` method which creates the file directly and adds the data to it. Also take note of the `await` keyword, which we need to run a successful JavaScript promise.

### How to Rename Files

Another major part of working with files is renaming an already existing file. Let's take a look at how that works:

```
const { rename } = require('fs/promises'); 

async function renameFile('dummytext.txt', 'changedDummyText.txt') { 
   try { 
     await rename(from, to); 
     console.log(`Renamed ${from} to ${to}`); 
   } catch (error) { 
     console.error(`Got an error trying to rename the file: ${error.message}`); 
   } 
 }
```

As you can see, our `async` function took in two parameters this time, the first one will old the current name of the document we are about to change, and the second one will old the new name we are working with. 

We've also changed our `dummyText.txt` to `changedDummyText.txt`.

### How to Delete Files

To delete a file we'll have to call the `unlink` method. This time, instead of having two parameters, we'll have only one: the name, or the path of the file you want to delete.

We'll also still use our try-catch error handling method to control our errors, and log the name of the file that has been deleted on the console.

```
const { unlink } = require('fs/promises'); 

async function deleteFile('./dummytext.txt') { 

   try { 
     await unlink(filePath); 
     console.log(`Deleted ${filePath}`); 
   } catch (error) { 
     console.error(`Got an error trying to delete the file: ${error.message}`); 
   } 
 }
```

### How to Update Files

Yes, I did mention that we will learn how to update files too – but if you've been paying close attention, you'll see that we already did.

We talked about `appendFile()`, which basically changes key information, and allows you to write new contents of the file. We also talked about `writeFile()`, which updates the contents of a file as well.

## Conclusion

Here we are, the end of this guide. Let's recap what we've learned in this tutorial.

First, we talked about the what Node.js is, and how important the file system is. We also learned what Node modules are. All of this is vital to you understanding the rest of the tutorial.

Keep in mind there are more operations that you can perform with the file system in Node. This tutorial just covered the basics, and the primary functions. Read up a bit on it and you'll discover a lot more.

If you loved this article, [let's talk on Twitter](https://www.twitter.com/tiseysoft). I'd love to connect with each and every one of you.

