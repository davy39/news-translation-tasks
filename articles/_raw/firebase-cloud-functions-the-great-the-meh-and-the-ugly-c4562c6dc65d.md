---
title: 'Firebase Cloud Functions: the great, the meh, and the ugly'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-29T18:24:33.000Z'
originalURL: https://freecodecamp.org/news/firebase-cloud-functions-the-great-the-meh-and-the-ugly-c4562c6dc65d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*P7XjBh6QtYZ5z7wJ.
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: '#firebase-cloud-functions'
  slug: firebase-cloud-functions
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Pier Bover

  When I reviewed Firebase last year, I complained that it wasn’t completely serverless.
  A Node server was still needed for common functionalities such as sending emails
  or creating thumbnails.

  Firebase Cloud Functions were announced a fe...'
---

By Pier Bover

When [I reviewed Firebase](https://medium.freecodecamp.org/firebase-the-great-the-meh-and-the-ugly-a07252fbcf15) last year, I complained that it wasn’t completely serverless. A Node server was still needed for common functionalities such as sending emails or creating thumbnails.

Firebase Cloud Functions were announced a few months later. The service is still in beta, but I’ve been using it happily for a couple of months in production.

Let’s see how it’s doing.

### What are Firebase Cloud Functions?

If you’ve never heard of cloud functions before, the concept is quite straightforward. Deploy concise logic to a server in the form of functions and some diligent elves can be magically invoked from limbo to do a task for you. All of this without caring about infrastructure and paying only for execution resources.

In many cases, this new paradigm can simplify writing, maintaining, and running backend code.

Firebase Cloud Functions in particular are like Lego blocks that you can connect to any Firebase service. For example, a function can be triggered when an image is uploaded to Firebase Storage to create a thumbnail, or maybe clean some user data when a node is deleted in the Realtime Database. Pretty much anything of interest that happens in Firebase can trigger a function.

If that isn’t enough, you can also use HTTP to trigger functions with GET, POST, etc. Check out this amazing video on how to combine Firebase Hosting with Cloud Functions to create a complete Express app:

### The Great

#### Infrastructure doesn’t get any easier than this

Infrastructure is completely abstracted from you, much like the rest of Firebase. Every time a function is triggered, a new virtual server comes to life, does its job, and returns to limbo. Google Cloud’s magic will keep triggering your functions and scale infrastructure according to workload automatically.

#### Pricing

Cloud functions in general are very cost-effective. It’s difficult to compare pricing of cloud providers, but I can say that based on my experience, Firebase Cloud Functions have been _ridiculously_ cheap. It’s hard to believe Google is making any money out of this.

#### Easy to use

As usual with Firebase and Google, the docs are great and you won’t be making mental acrobatics to _get it_. There are also [tons of samples on Github](https://github.com/firebase/functions-samples) to get you started. Deployment auth is handled by the Firebase CLI, so getting a hello world up and running is literally:

```
firebase init functionsfirebase deploy
```

I think the simplicity of using Firebase and Google Cloud in general is just awesome, specially compared to the competition.

#### Flexible

Like I wrote before, these functions can be triggered by all sorts of events. I bet you will not run out of ideas on how to integrate them with your Firebase project or even the rest of your stack.

Here are some of problems we’ve solved using Firebase Cloud Functions:

* Generate PDFs for a online invoicing service using Phantom.js, and sign these invoices with some government service
* Connect a Go service with a third party SOAP provider (ugh)
* Send emails via HTTP from anywhere in our stack

### The Meh

#### Cold starts

Scalability is great, but run time can fluctuate wildly. A simple hello world function can take 3ms to do its job, or a 100ms.

```
functions.https.onRequest((request, response) => {    response.send(“Hello from Firebase!”);});
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*7oLzO7vAtNeEChBQrYMpiA.png)

These fluctuations are caused by virtual server boot times. If the virtual server that is running your function is awake, the function will trigger instantly. But if the server has to be brought up from limbo, it will obviously need more time to start working. In the cloud functions lingo, this is referred to as warm and cold starts.

In practice, you can’t rely on consistent response times unless you are caching your data, as described in the previous video, or use hacks to keep your functions warm.

Unfortunately cold starts are an unavoidable aspect of dealing with cloud functions (from any provider). You will have to take that into account when deciding to use a cloud function to solve something.

#### No scheduler (cron)

Cloud functions are perfect for doing low traffic tasks like generating reports or doing periodic backups at 2am, but with Firebase or Google Cloud there is no easy way to trigger your functions based on a schedule.

The [Firebase team recommends](https://github.com/firebase/functions-cron) creating an App Engine project to orchestrate these triggers. The service really begs for something like the [Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler).

#### JavaScript only

Eh, I’m ok with JavaScript, but both Azure and AWS support many more languages. It’s ironic that Google doesn’t support Go in its cloud function service, but AWS does.

#### Node 6

Again, the competition is doing better. Both AWS Lambda and Azure Functions are already running on Node 8. The biggest drawback here is going back to promises without async/await or having to configure Babel on your project.

### The Ugly

#### Dev workflow

With the exception of [HTTP triggered functions](https://firebase.google.com/docs/functions/local-emulator#use_firebase_serve_for_https_functions), you can’t run your functions locally. Functions triggered by a Firebase service have to be deployed to the cloud.

This has many ugly implications:

* Little mistakes end up costing a lot of time, since new functions take a couple of minutes to start working.
* Deployed functions have no obvious versions. All logs of the same function appear to be from the same version. It’s never clear when the new functions are actually working, so your only choice is to manually trigger the functions and See-What-Happens™.
* No rollbacks

#### Environments

On top of the previous points, managing environments is… complicated.

You can add environment variables to your functions projects using the [Firebase CLI](https://firebase.google.com/docs/functions/config-env) but, like other aspects of Firebase, this is a naive approach that doesn’t scale well.

You will need credentials to access pretty much anything outside of the Firebase sandbox. For other Google Cloud services, these credentials come in the form of `.json` files. Multiply that by every environment (dev, production, staging) and you can end up with a royal mess.

I ended up up manually renaming credential files before deploying, or worse, deploying all credentials and selecting the appropriate one at runtime. Please, let me know in the comments if you’ve found a way around this.

I’d love to see an _Environment_ tab in the Firebase Console where I could easily manage these settings for the whole Firebase project. Switching between environments should be as easy as `firebase use production`.

### Conclusion

Other than some friction during dev phase, my experience with Firebase Cloud Functions has been positive. Once deployed, these things are reliable and require zero maintenance as promised. So yes, Firebase is finally completely serverless. Hurrah!

If you are already using Firebase, it’s really a no brainer. Firebase Cloud Functions are a great complement for your project, even if the service is still in beta.

On the other hand, it’s fair to say the competition has a more mature product. If you are not invested in Firebase or Google Cloud, and are considering using cloud functions in your stack, you should probably be looking into what AWS or Azure have to offer as well.

To be completely honest, I’m a bit concerned that the service is still in beta. It’s been over a year since it was announced and progress feels painfully slow. The competition seems far more committed to its cloud products, even if, according the Diane Greene, CEO for Google’s cloud businesses, Google Cloud is the [“fastest growing cloud”](https://techcrunch.com/2018/02/01/googles-diane-greene-says-billion-dollar-cloud-revenue-already-puts-them-in-elite-company/).

That is all.

**Note:** In a previous version of this article I claimed that it wasn’t possible to write tests for non HTTP functions. This is wrong, and [here are the docs](https://firebase.google.com/docs/functions/unit-testing#testing_background_non_http_functions) on how to do that.

