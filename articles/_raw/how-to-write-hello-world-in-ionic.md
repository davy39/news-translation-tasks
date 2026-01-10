---
title: How to Write "Hello, World!" in Ionic
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-18T19:34:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-hello-world-in-ionic
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c84740569d1a4ca32ac.jpg
tags:
- name: Ionic Framework
  slug: ionic
- name: toothbrush
  slug: toothbrush
seo_title: null
seo_desc: 'This guide will teach you how to write a simple Hello World program in
  Ionic.

  Step 1: installation

  Install ionic, npm ,angular and cordova if not installed. [See first introduction
  for more information.]

  sudo apt-get install nodejs

  sudo apt-get insta...'
---

This guide will teach you how to write a simple Hello World program in Ionic.

## Step 1: installation

Install ionic, npm ,angular and cordova if not installed. [See [first](https://guide.freecodecamp.org/ionic) introduction for more information.]

```shell
sudo apt-get install nodejs
sudo apt-get install npm 
sudo npm install -g ionic cordova
```

## Step 2: Create a folder named helloworld

```shell
ionic start helloworld blank
```

Note: Since this is a small project, enter No or N when prompted during program execution.

## Step 3: Change directory to helloworld [this is your ionic directory]

```shell
cd helloworld
```

## Step 4: Open the folder in your text editor . 

You will see various files and subfolders.

Don't panic – these files are generated automatically by npm for you. Just go to `src`->`page`->`home`->`home.html` .

### Basic File Format

```text
`home.html` is the html page where you can write html syntax.<br/>

`home.scss` is the css page to write css syntax.<br/>

`home.ts` is the typescript page to write typescript code.
```

## Step 6: Delete the template and add the html syntax as shown below

```html
 <ion-header>
  <ion-navbar>
    <ion-title>
      Ionic Project
    </ion-title>
   </ion-navbar>
  </ion-header>

  <ion-content padding>
   <h2>Hello World </h2>
  </ion-content>
```

## Step 7: Save the code and run

```shell
ionic serve
```

To see your code running go to the browser and and open localhost:8100 in the URL. That's it!

## More info on Ionic:

* [Ionic full course (video)](https://www.freecodecamp.org/news/ionic-full-course/)
* [Create a CRUD todo app with Ionic](https://www.freecodecamp.org/news/creating-a-crud-to-do-app-using-ionic-4/)

