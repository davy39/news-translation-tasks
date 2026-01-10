---
title: How to Use Node Environment Variables with a DotEnv File for Node.js and npm
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-25T00:48:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-node-environment-variables-with-a-dotenv-file-for-node-js-and-npm
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/node-env-variables.jpg
tags:
- name: node
  slug: node
- name: node js
  slug: node-js
- name: npm
  slug: npm
seo_title: null
seo_desc: "By Veronica Stork\nEnvironment variables are variables that are set outside\
  \ of a program, often through a cloud provider or operating system. \nIn Node, environment\
  \ variables are a great way to securely and conveniently configure things that don't\
  \ chan..."
---

By Veronica Stork

Environment variables are variables that are set outside of a program, often through a cloud provider or operating system. 

In Node, environment variables are a great way to securely and conveniently configure things that don't change often, like URLs, authentication keys, and passwords.

## How to Create Environment Variables

Environment variables are supported out of the box with Node and are accessible via the `env` object (which is a property of the `process` global object.) 

To see this in action, you can create your own environment variable right in the Node REPL by appending a variable to the `process.env` object directly. 

For example, to create an environment variable to store the [combination on my luggage](https://www.youtube.com/watch?v=a6iW-8xPw3k) I could assign the variable like this: `process.env.LUGGAGE_COMBO=“12345”`.

(A quick aside: environment variables are, by convention, generally written in all caps.)

While this is a neat experiment, you would not use the Node REPL like this in an app. To create environment variables in your Node app, you will probably want to use a package like DotEnv. 

## How to Use DotEnv

[DotEnv](https://www.npmjs.com/package/dotenv) is a lightweight npm package that automatically loads environment variables from a `.env` file into the `process.env` object.

To use DotEnv, first install it using the command: `npm i dotenv`. Then in your app, require and configure the package like this: `require('dotenv').config()`. 

Note that some packages such as Create React App already include DotEnv, and cloud providers may have different means of setting environment variables all together. So make sure you check the documentation for any packages or providers you are using before you follow any advice in this article. 

## How to Create a .env File

Once you have DotEnv installed and configured, make a file called `.env` at the top level of your file structure. This is where you will create all of your environment variables, written in thr `NAME=value` format. For example, you could set a port variable to 3000 like this: `PORT=3000`. 

You can declare multiple variables in the `.env` file. For example, you could set database-related environment variables like this:

```
DB_HOST=localhost
DB_USER=admin
DB_PASSWORD=password
```

There is no need to wrap strings in quotation marks. DotEnv does this automatically for you.

Once you’ve created this file, remember that you should not push it to GitHub as it can contain sensitive data like authentication keys and passwords. Add the file to .gitignore to avoid pushing it to a public repo accidentally.

## How to Access the Environment Variables

Accessing your variables is super easy! They are attached to the `process.env` object, so you can access them using the pattern `process.env.KEY`.  

If you ever need to change the value of any of your environment variables, you just need to alter the `.env` file.

## Wrapping Up

Environment variables will make your code more maintainable and more secure. They are easy to set up with Dotenv, and straightforward to use in Node. 

Now that you know how it's done, you can create your own environment variables for your Node application. Enjoy!

  

