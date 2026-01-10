---
title: How to use Google Cloud Tasks in Laravel PHP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-22T11:10:14.000Z'
originalURL: https://freecodecamp.org/news/using-google-cloud-tasks-in-laravel-php-24985db107b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pGJLCV_d77eyLshIDIVCdQ.png
tags:
- name: google app engine
  slug: google-app-engine
- name: Google Cloud Platform
  slug: google-cloud-platform
- name: Laravel
  slug: laravel
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Errol Fernandes

  Deploying a Laravel application on Google App Engine is a fairly easy task thanks
  to the documentation available. But setting up asynchronous task processing (Laravel
  Eventing) on Google Cloud effectively is not that simple.

  One of...'
---

By Errol Fernandes

Deploying a Laravel application on Google App Engine is a fairly easy task thanks to the documentation available. But setting up asynchronous task processing (Laravel Eventing) on Google Cloud effectively is not that simple.

One of the ways we can do this is by using the supervisord.conf file to set up the Laravel `queue:listen` command. But this is only available for Google App Engine Flexible Environment. So if you need a solution for Google App Engine Standard Environment, then you need to use Google Cloud Tasks to process async jobs.

Google Cloud Tasks is a fully managed service that allows you to manage the execution, dispatch, and delivery of a large number of distributed tasks. Using Cloud Tasks, you can perform work asynchronously outside of a user or service-to-service request.

**Step 1:**

Create a task queue to handle the tasks. Here we use the queue.yaml file to specify the configuration of the queue to be created in Google Cloud. The target parameter contains the name of the application deployed on app engine.

![Image](https://cdn-media-1.freecodecamp.org/images/cqgEZ5IU7zeQ-NiFA60HC4AHlIbvjJyzcVn1)

**Step 2:**

Deploy the queue.yaml file in Google Cloud using the command `gcloud app deploy queue.yaml` The below image is of a Google Task queue created in Google Cloud.

![Image](https://cdn-media-1.freecodecamp.org/images/pLbVCTFBu-PMu1MOQrKXJqlczqPonw2d456T)

**Step 3:**

We need to pass the route of the API and the payload object for the task. In the below example, we will pass the required data to an `initTask()` function:

![Image](https://cdn-media-1.freecodecamp.org/images/Bu9p27rXvAA4sHalnZHVrvgSrkMaWXSH6SAQ)

**Step 4:**

Create the initTask() function:

![Image](https://cdn-media-1.freecodecamp.org/images/9oBdKkfhFjJbbCEB0nuSBr9w3yOp89N1zfIH)

We pass the userID of the current user in the payload for authentication reasons. Now that the payload is ready, we pass all the required details to the task builder function

**Step 5:**

Create the create_task() method. This method will use the Google API to build a Cloud Task and pass it to the task queue. The gAppCreds.json file is the Google Service Account created for defining the roles of the application.

![Image](https://cdn-media-1.freecodecamp.org/images/VCBtOQ8jdrE-Xp9bVZP8Ec9jkZJkjbRmVDi5)

**Step 6:**

Now we create the API routes using the RouteServiceProvider in api.php:

![Image](https://cdn-media-1.freecodecamp.org/images/3ELikvkitL6Oyv9u-jB-7IkdEck1xM-3o3xL)

**Step 7:**

Now we create a TaskController which will route the different API to the specific function. So in the below example we create an `associateApp()` function:

![Image](https://cdn-media-1.freecodecamp.org/images/N9zDssAevMKOPAljdNo6Kk9rD7xV1oHhOU6-)

In the above function, we json_decode the payload that we sent in **Step 4** and pass it to the respective event for processing. The userID that we passed in **Step 4** is used to validate the authenticity of the incoming API request.

#### Final Verdict:

Normally in Laravel, we call the event from the respective controller directly. But for using Google cloud tasks, we create a Task API which in turn calls the route that in turn calls the event to process our data. So in short we create multiple APIs for our Laravel events and jobs which are then called (**by Google Task API**) based on the route that you pass in **Step 3** and **Step 6**.

Since I am using Google Cloud Tasks, I don’t need to worry about the supervisor or managing the jobs in the queue table, as everything is taken care by the Google Task Queue. All I have to do is monitor the Task Queue if there is any failed task.

Using Google Cloud API, I can create multiple queues for different target applications I deploy on Google App Engine irrespective of whether the environment is Standard or Flexible.

