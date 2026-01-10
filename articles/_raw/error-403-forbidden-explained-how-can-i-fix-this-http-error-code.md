---
title: Error 403 Forbidden Explained - How Can I Fix This HTTP Error Code?
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2019-11-03T19:02:00.000Z'
originalURL: https://freecodecamp.org/news/error-403-forbidden-explained-how-can-i-fix-this-http-error-code
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/403-error.png
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: http
  slug: http
seo_title: null
seo_desc: "So you have encountered a 403 Forbidden error and you are wondering what\
  \ it means. \nThis error is an HTTP status code which means that you are forbidden\
  \ from accessing the page or resource that you are trying to reach. Unless you are\
  \ the person who c..."
---

So you have encountered a **403 Forbidden** error and you are wondering what it means. 

This error is an HTTP status code which means that you are forbidden from accessing the page or resource that you are trying to reach. Unless you are the person who created the website, there is often nothing you can do. However, there are a few things that might help.

It is possible the creator of the website set up the permissions correctly and is intentionally forbidding you from accessing the page. But this error could also indicate that the website was set up incorrectly.

Here are some things you can try to fix the 403 Forbidden error.

### ? Verify and refresh

First verify that the URL is correct and refresh the page. This is the first thing you should do when you encounter any error on a website. 

Most web servers are set up to return a 403 Forbidden error if someone tries to access a directory on the server instead of a file (like an HTML file). So you may have typed in the URL incorrectly and are trying to access a directory.

### ? Clear browser cache

A cached version of the page could be causing the issue. Here are shortcut keys that will clear the browser cache on most browsers:

* Windows: `CTRL + F5`
* Mac/Apple: `Apple + Shift + R or Command + Shift + R`

### ⌨️ Log in

It is possible that the page you are trying to access requires you to log in. If so, make sure to log in to get additional access.

### ? Clear cookies 

Clearing your browser's cookies can sometimes help. This is especially true if the site usually requires a log in, and if logging out and in does not solve the problem.

### ? Contact the website

It is possible the website has been set up incorrectly and the creator of the website is not aware. Other people could be getting this same error. Try to find the contact information for the website and let them know about the problem. It could be a simple fix on their end.

### ?️ Come back later

Often 403 Forbidden errors are caused by an issue with the website. It is possible that the website developers are currently working on a fix. If you just try again at a later time, the problem could be fixed.

## For web developers only

If you are the creator of the page that is giving a 403 Forbidden error, then it is your job to fix the error on the server. The two most common reasons for the error are no index page and incorrect permissions.

Make sure the you have a file called index.htm or index.php in the location that is showing the error. For instance, if the URL `https://www.freecodecamp.org/forbidden` is showing the error, make sure that the directory named `forbidden` on your server has an index.htm or index.php file located in it. 

The next thing to look into is the permissions on the files that are creating the error. Here is how the permissions should usually look:

* Folders: 755
* Static Content: 644
* Dynamic Content: 700

