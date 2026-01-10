---
title: Lessons learned from deploying my first full-stack web application
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-25T09:38:32.000Z'
originalURL: https://freecodecamp.org/news/lessons-learned-from-deploying-my-first-full-stack-web-application-34f94ec0a286
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/edu-lauton-TyQ-0lPp6e4-unsplash.jpg
tags:
- name: learning
  slug: learning
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Will Abramson

  I recently achieved one of my long-term goals: deploying my first full-stack web
  application.

  In this post, I’ll be sharing the lessons I learned from a beginner’s perspective,
  along with some useful tutorials I followed, key roadblo...'
---

By Will Abramson

I recently achieved one of my long-term goals: deploying my first full-stack web application.

In this post, I’ll be sharing the lessons I learned from a beginner’s perspective, along with some useful tutorials I followed, key roadblocks that I had to overcome, and mistakes that I made along the way. I want to help other developers understand what’s involved in deploying a web application.

After spending over six weeks googling, trying, failing, and trying again, I finally managed to deploy my web application. It was comprised of a Node.js backend along with a React frontend to an Amazon Web Services (AWS) EC2 virtual machine.

It was quite a challenge but it was truly satisfying, as in the end the application was successfully deployed and is now accessible via a public domain name.

![Image](https://cdn-media-1.freecodecamp.org/images/7lX00uJHwR2qavL7Wm7oV-W-6LcApDtK1aP3)
_Victory Jump! - After deploying your Web Application_

The biggest difficulty for me was finding the information. I didn’t understand what was involved in deployment. So I struggled to find effective answers on the web. I failed to find a single guide for the whole process.

Hopefully, I can simplify the deployment learning curve for the next person by bringing all the information I learned into one place.

So here it goes…

### What does it mean to deploy an application?

A web application is split into two parts.

* **Client side code:** This is your frontend UI code. These are static files that don’t change throughout your application’s life. Static files need to exist **somewhere** so that your users can download and run them in their browser on the client side. I will go into more detail about where that somewhere might be later.
* **Server side code:** This deals with all the logic of your application. It should be run on a server (machine), commonly a virtual one like an EC2 instance, much like you run it when developing locally.

To run your local code, the server must have a copy of it. I just cloned my Github repo onto the server from the command line interface of the server.

You also need to setup your server. This includes:

* setting up the machine to be able to access the internet and run your code
* exposing the correct [ports](https://www.lifewire.com/port-numbers-on-computer-networks-817939)
* listening for HTTP requests (Internet requests)
* pointing a custom domain name to the server your application is running from

You’ll know it’s working when you can access your application using your custom domain name from any machine on the Internet and all the functionality of your application is working as expected.

So, that’s an overview. But, how do we actually do it?

### Getting started

You should split up your application and break down the problem. You are deploying two different things: client-side static files and server-side code.

My first mistake was to think of my application as a whole, rather than two separate applications that talk to each other.

This added to the complexity and made googling for answers useless. It left me feeling overwhelmed.

I broke down the problem into these steps. Although each problem can always be broken down further.

* Setting up your VM and deploying your Backend
* Deploying your Frontend
* Getting the Two Applications Communicating
* Pointing your Domain Name

In the figure below, I’ve attempted to put the complete process in a diagram.

![Image](https://cdn-media-1.freecodecamp.org/images/eBec3M2S8ovEMvyboray1w2JoZn1kp3uueXY)
_The deployment process. Created using[ draw.io](https://www.draw.io/" rel="noopener" target="_blank" title=") - an awesome free diagram tool._

### Setting up your VM and deploying your Backend

In my case, this was an Express.js server deployed on an amazon EC2 virtual machine. I would’ve explained how to do it, but the tutorial “[Creating and Managing a Node.js Server on AWS - Part 1](https://hackernoon.com/tutorial-creating-and-managing-a-node-js-server-on-aws-part-1-d67367ac5171)” does a far better job.

It’s the best tutorial I have come across in this space and covers:

* Starting an AWS virtual machine
* Getting up correct security groups for ports
* Pulling code from GitHub onto the virtual machine
* Running your server
* Using Nginx, a HTTP server, to forward requests from port 80
* Using PM2 to persist the process running your server

It was a life saver, and without it I would still probably be stuck. So thank you, [Robert Tod](https://www.freecodecamp.org/news/lessons-learned-from-deploying-my-first-full-stack-web-application-34f94ec0a286/undefined).

You can easily test that your server is running using [Postman](https://www.getpostman.com/) to send a request to one of your Backend endpoints.

### Deploying your Frontend

So now that you have a server with your backend running (I hope), you need to get your Frontend working. This is really easy when you understand the process.

Unfortunately, I didn’t for a long time. For example, at the beginning I tried to run my Frontend using npm start.

Npm start creates a local development server, serving the files so that they are only accessible using `localhost` which is not what we want.

To deploy the Frontend code, you have to store all the files on your virtual machine in a location your web server knows about. The web server lets a client download the code and run it in their browser.

[Apache](https://httpd.apache.org/) and [Nginx](https://www.nginx.com/) are examples of web servers.

A web server listens to certain ports, port 80 or more commonly port 443 (secure), and either serves static files (your Frontend code) or passes the request to a different port. For example, we saw a request to the Backend in the Node.js tutorial above.

As Frontend code is just a collection of files stored on a web server, we want to make these files as small and optimized as possible. This ensures that the client can download and run them as fast as possible.

Faster page loads equal happy users.

All your Frontend JavaScript files can be bundled into a single JavaScript file. This is usually done by running npm run build, assuming you have this script defined in your package.json.

You can read more about bundling code [here](https://medium.com/@andrejsabrickis/modern-approach-of-javascript-bundling-with-webpack-3b7b3e5f4e7).

Basically, bundling your application removes anything that isn’t essential. This includes shortening names and placing all JavaScript code in one file. It will also compile your code into the correct JavaScript version. This is so all web browsers can understand and run it (for example, converting TypeScript to JavaScript).

When your code is bundled, you just have to copy the files into your web server. Then configure your web server to serve files stored at that location.

Here is a good [article](https://medium.com/@jgefroh/a-guide-to-using-nginx-for-static-websites-d96a9d034940) on deploying static files to an Nginx web server.  
Hopefully, if all is going well (which it never does), your Frontend code is now working.

Visit the public DNS for the virtual machine to verify that the static information from the site loads.

### Getting the Two Applications Communicating

So I had both my applications running individually, but something wasn’t right. I couldn’t get rid of a network request error.

This was the most frustrating point for me. I was so close, but I ran into some setbacks that ended up taking weeks to solve.

Cross-Origin Resource Sharing (CORS) is a mechanism that allows communication between different IP addresses or ports. You want your Backend to be allowed to send data back to your Frontend.

To enable this, your Frontend must include the correct headers when requesting resources. This can be done in two ways:

* The headers can be added in Nginx although it takes some figuring out. You can start [here](http://oskarhane.com/avoid-cors-with-nginx-proxy_pass/).
* You can [use the cors npm module](https://www.npmjs.com/package/cors) to include the headers.

A great way to test this if it is working is by looking within the network tab of your browser’s developer tools. This shows all the requests your application is making. If you select a request you can see where the request went to and what headers it included.

![Image](https://cdn-media-1.freecodecamp.org/images/y1rlso3aqjosHHJaBZpKCwdOugXiYNOLLHQW)

Once you have the right request headers being sent with your request, you have to make sure the requests are going to the correct place. This should be the address and port of your EC2 Backend server and **not** the address and port of your **local** Backend server like mine was.

Your Frontend communicates with your Backend using HTTP requests. Somewhere in your Frontend, code you will tell it where your Backend is located.

```js
const networkInterface = createNetworkInterface({
 uri: ‘http://0.0.0.0:5000/graphql',
});
```

Mine looked like this, which clearly was not going to be correct for my production server.

Annoyingly this made my application seem like it worked when I first navigated to it on my local machine, as my local server was running and able to return the required information.

To fix this, you can simply change the URI defined, but that means having to change it back every time you do further development, which is **not** the best approach (I know because I did it).

A more sophisticated solution is to include both URIs and use environment variables to select the appropriate one.

```js
const networkInterface = createNetworkInterface({   
   uri: process.env.NODE_ENV === 'production' ?      
                     'http://thecommunitymind.com/graphql' : 
                     'http://0.0.0.0:5000/graphql',
});
```

Simple but effective. Just make sure you set your NODE_ENV to production when using it for your production server.

We’re almost there. In fact, your deployment might work now.

But I had one last problem to overcome.

Even though my CORS setup was correct, the required headers were not being included consistently and were only getting added sometimes. For some POST requests, the CORS headers were not always present. Very odd!

This error lead me on a frustrating goose chase trying to fix my CORS setup in Nginx, when actually it had nothing to do with CORS.

Actually, I didn’t even need to do anything with CORS in Nginx, because I was using the CORS npm module.

The error was due to two other issues:

* My database was included as an sqlite file in the Backend and
* My process manager, [PM2](http://pm2.keymetrics.io/), was watching for file changes

So writing to the database file on a POST request caused PM2 to restart the server. This was leading to the correct headers not getting picked up which resulted in misleading errors.

A great tip and one I wish I had known earlier is to check your server logs on your EC2 instance. Whether you’re using PM2 or something else there will always be a way to check your logs. Just Google it!

These logs provided the key to solve my issue.

I simply had to turn off the watch ability of PM2. Bingo. And finally, it worked.

### Pointing your Domain Name

This is the icing on the cake. You want a nice clean URL for your newly deployed application.

I bought my domain name through Amazon and used Route 53 to point it to the correct EC2 instance. This was a surprisingly painless experience.

Amazon’s [tutorial](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-ec2-instance.html) was quite sufficient.

![Image](https://cdn-media-1.freecodecamp.org/images/gi7iwvOLcVgcWyejOR2SDpnnV3hImGJPBpG5)
_Great diagram - Source: [WPBeginner](http://www.wpbeginner.com/beginners-guide/beginners-guide-what-is-a-domain-name-and-how-do-domains-work/" rel="noopener" target="_blank" title=")_

### Summary

I hope this post has helped you understand the web application deployment process and ultimately get your amazing project online — whatever that may be.

At least you should have a better idea of what to Google for!

Good Luck.

