---
title: 'The Beauty of Heroku Connect: Simplifying Database Synchronization'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-12T21:25:37.000Z'
originalURL: https://freecodecamp.org/news/the-beauty-of-heroku-connect-simplifying-database-synchronization-e57451d3b376
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EPgspRCbfWjtUtUXoGnVHg.png
tags:
- name: Heroku
  slug: heroku
- name: General Programming
  slug: programming
- name: Ruby on Rails
  slug: ruby-on-rails
- name: Salesforce
  slug: salesforce
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Wilson Wang

  I’m currently a developer for Blueprint, an organization at UC Berkeley. We develop
  software pro bono for non-profits and advance technology for social good. This past
  year, my team worked on building a solution for The Dream Project. ...'
---

By Wilson Wang

I’m currently a developer for [Blueprint](https://calblueprint.org/), an organization at UC Berkeley. We develop software pro bono for non-profits and advance technology for social good. This past year, my team worked on building a solution for [The Dream Project.](http://www.dominicandream.org/) The goal is to provide a better education for children in the Dominican Republic.

I am writing this post in hopes of sharing my experience of doing Salesforce integration using Heroku Connect for a Ruby on Rails/React Native app.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EPgspRCbfWjtUtUXoGnVHg.png)

#### What is [Heroku Connect](https://www.heroku.com/connect)?

> “Heroku Connect makes it easy for you to build Heroku apps that share data with your Salesforce deployment. Using bi-directional synchronization between Salesforce and Heroku Postgres, Heroku Connect unifies the data in your Postgres database with the contacts, accounts and other custom objects in the Salesforce database.”

Another way to put it…

Heroku Connect assists with replacing your app’s Postgres database with a Salesforce database. Of course, since Rails apps connect natively to Postgres, you cannot do immediate calls and pushes to Salesforce without some API like the [Restforce gem](https://github.com/restforce/restforce).

In reality, the Postgres database that our Rails app will interact with serves as a disguise for Salesforce. It is a working middleman. All data must go through it before reaching Salesforce, and vice versa. Heroku Connect is the bridge that combines the capabilities of Force.com and Heroku without the need for a gem.

You might ask… why even bother learning Salesforce integration?

Well, Salesforce integration streamlines the process of storing and retrieving data. Especially customer data for businesses.

You can provide your customers with modernized computer systems for an improved user experience and workflow. You’ll be accelerating app development. It also creates better tools for informing management and sales on business performance.

This helps businesses achieve efficient levels of operation for business-to-consumer apps. It does this through instantaneous and accurate updates.

#### A Sample Project for Inspiration

To give some background for the code snippets below in the tutorial, I will explain beforehand the project I was working on. This project got me introduced to Heroku Connect.

Previously, Dream recorded student information in a Salesforce database. This was not ideal for teachers to use. To make their lives easier, we created a user-friendly app. The app handled course creation, student enrollment, and attendance taking.

Due to the poor internet connection at Dream campuses, we turned to Heroku Connect for constant synchronization of updates. It synchronized updates on the Heroku Postgres database side and Salesforce database side.

All the code described in this demo is available in our [project repo](https://github.com/calblueprint/dream-rails). You can also check out the React side of the application [here](https://github.com/calblueprint/dream-mobile).

### Alright, let’s start the demo…

#### Overview

I’m going to tackle this demo in the following order:

1. Description of Tech
2. Setup (Heroku Postgres and Heroku Connect)
3. Heroku Connect Mappings + Notes
4. Changes to your local Rails app

#### Description of Tech

* Force.com ([Salesforce Developer Account](https://developer.salesforce.com/))
* [Heroku Connect](https://www.heroku.com/connect)
* Rails app (my Rails version was 5.1.4)

#### Setting up: Deploying your app to Rails

After setting up your Rails app, you want to deploy your app on Heroku. Here is a quick run-through on deploying your app:

1. Login to your Heroku account, and you will be redirected to the dashboard on the top right. You will see a “New” button on a top right to create a new project. Type in your custom app name and create your app.
2. You will be redirected to the deploy page of your new app. Scroll down to the bottom to the section “Deploy using Heroku Git.” Follow the instructions on the page. (Note: after you add the Heroku Git remote you can alway update your Heroku app. You update by adding and commiting your changes and finally doing a git push **heroku** master.)

Most likely, if this is your first time, you will face an error: “Heroku deployment failed because of sqlite3 gem error.” This is because Heroku uses Postgres instead of sqlite3. To fix this, check out this [Stack Overflow post](https://stackoverflow.com/questions/13083399/heroku-deployment-failed-because-of-sqlite3-gem-error.).

#### Heroku Postgres

With your app deployed, your overview page should have the add-on Heroku Postgres. This is your usual database for deployed Heroku apps.

![Image](https://cdn-media-1.freecodecamp.org/images/0*R9kFu8MDX4RC17HJ)
_Add-ons like Heroku Postgres or Heroku Connect appear in the Overview tab or Resources tab._

Click on this add-on to check the URL database info in the settings tab. Be sure to add your Postgres database URL to your Rails app.

![Image](https://cdn-media-1.freecodecamp.org/images/0*NOr58iU9H0g4xG_5)

To add the database URL, you can either create an environment variable using the [Figaro](https://github.com/laserlemon/figaro) gem:

or just include a URL variable in your database.yml file:

#### Heroku Connect

Next, click on configure add-ons or the resources tab, and search for Heroku Connect. Click provision to add the add-on.

![Image](https://cdn-media-1.freecodecamp.org/images/0*g85k6DdH9HyNB1vJ)

You will then be redirected to the screen below. Note that the schema name is “salesforce” for now (feel free to change it as well), and you’re good to continue.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WUvsdQ_IgEgV41S7Y9_hew.png)

Click setup connection. Enter your Salesforce user info to establish the connection with the appropriate details.

You’re now done with the setup! Now we can move on to mappings.

#### Mappings

I recorded a short video of creating a mapping for a Teacher object:

The video is a walkthrough for establishing mappings. There are a couple things I want to explain further that I personally got confused with. After reading these clarifications, I would recommend rewatching the video for a better understanding.

#### 1. ‘__c’

You may be asking why there are so many ‘__c’s that are appended at the end of my teacher object and teacher fields. Well, Salesforce actually appends this to each custom class/field.

So, tying back to my Rails project, the table name is now _Teacher__c_ instead of Teacher and the columns/fields have changed from names like First_name, Last_name to _First_name__c_, _Last_name__c_. Some default fields like _sfid_ or _createddate_ are not custom, so they don’t require appending ‘__c’.

#### 2. Custom Fields

So, how do you create custom fields? Well, there’s actually a small arrow on the right side of your screen for you to edit objects and fields.

![Image](https://cdn-media-1.freecodecamp.org/images/0*BZ1PIjziwnyF2V3A)
_Click on view object/fields to modify them respectively._

After each modification, remember to check if you also need to modify your Heroku Connect mappings.

#### 3. Two Way Syncing

![Image](https://cdn-media-1.freecodecamp.org/images/0*-CCzjvqWA4i5Aggx)

I wanted to point out two very cool features about Heroku Connect’s Two-Way Syncing. The first is poll frequency, which regulates how often you want your Postgres database to update with Salesforce updates. Checking the Accelerate Polling box makes most operations pretty much instantaneous.

The second is the section on pushing data from your Postgres database to sync with the Salesforce database. You must check the box in order to have this feature work at all. However, right afterward, you will most likely see a warning pop up:

![Image](https://cdn-media-1.freecodecamp.org/images/0*AxFt3ybUi7xmipGk)
_“Warning: Read-write mappings require a unique identifier to be specified.”_

This is a layer of protection to ensure that you don’t accidentally create duplicate objects. It’s great if you have a unique identifier (in the video, each teacher has a unique email, so I made that my identifier). Otherwise, you can skip it and still have a functional Heroku Connect mapping. However, you may want to program your app to double check for existing records before creating an object.

#### Changes to your local Rails app

Now that you have your Heroku Connect all nice and set up, it’s time for a quick local adjustment before you can interact with your Salesforce data.

![Image](https://cdn-media-1.freecodecamp.org/images/0*qqvmsH_-kzF_NeCh)

In overview, you will see the name of your schema, in this case “salesforce”. If you had picked a different name during the provisioning phase, that name would show up here instead.

Because my Rails app’s table name is still Teacher, I need to change it to _Teacher__c_ to correctly reference the Salesforce data. I must change the table name to the format _schema_name_._object_name_ or _salesforce.teacher__c_ to reflect the changes.

The other notable change applies if your model has validated statements, like my Teacher model. Following the validates keyword, we still have the old field names like first_name without ‘__c’ and last_name without ‘__c’. We need to change those names by either appending the ‘__c’ to the old field names or by creating separate methods:

Afterwards, create some objects in Salesforce and open up your Rails console to retrieve this info. (In the video, I called Teacher.all to display all Salesforce Teacher objects in my Rails console.) The information should also be reflected in the Heroku Connect explorer.

### Reflection

I spent a good half of my semester trying to figure out Salesforce integration. I did lots of research, experimented with different solutions, and plenty of support. In the end, it was a very enlightening experience to work with the cool features of Salesforce/Heroku/Rails. I also learned how much I’ve grown as a developer and reflect on my strengths and weaknesses.

Usually people implement the first solutions they find. They do this without understanding why it is good or bad. I researched and planned out three separate solutions before discovering Heroku Connect. Through this, I realized how important it was to weigh the pros and cons of different solutions before settling, even if more time is spent researching instead of implementing.

By using this knowledge, my team and I built an app to help teachers provide quality education for students in the Dominican Republic schools that have a poor connection to the Internet. We learned to persevere when times were hard because we knew that despite every long work session, every bug fix, every line of code, we had a mission, and every step of the way was another step towards improving the world.

This experience helped me to really prioritize the goal and the importance of doing quality work instead of immediately using the fastest way to go. Every solution is worth researching its pros and cons. It’s all about resilience and tenacity.

So to all developers out there, no matter what situation you’re in, don’t give up. Don’t be afraid of trying new solutions and failing. Stay positive and Happy Deving!

_Wilson Wang is a junior at UC Berkeley studying computer science and data science. He is interested in developing software for improving business-customer relationships. Besides technology, Wilson is passionate about martial arts, architectural design, and landscape photography._

![Image](https://cdn-media-1.freecodecamp.org/images/1*gcqfNtbXJmAFRUZiwkBHbw.jpeg)

#### Thanks for reading! To learn more about Blueprint, follow us on [Facebook](http://facebook.com/CalBlueprint) and [Instagram](https://www.instagram.com/calblueprint/), and visit our [website](https://calblueprint.org/)!

