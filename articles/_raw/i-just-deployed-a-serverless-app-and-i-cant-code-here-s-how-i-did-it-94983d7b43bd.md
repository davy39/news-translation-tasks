---
title: I just deployed a serverless app — and I can’t code. Here’s how I did it.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-06T14:35:18.000Z'
originalURL: https://freecodecamp.org/news/i-just-deployed-a-serverless-app-and-i-cant-code-here-s-how-i-did-it-94983d7b43bd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Zq-SUy3UzV6e09uBD_c8PQ.jpeg
tags:
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: writing
  slug: writing
seo_title: null
seo_desc: 'By Andrea Passwater

  Hey there developer friends! I somehow just managed to deploy a real, working application.
  But heads up — I am not one of you.

  I am a writer who honest-to-god composes tweets and blog posts for a living.

  My command line experience...'
---

By Andrea Passwater

Hey there developer friends! I somehow just managed to deploy a real, working application. But heads up — I am not one of you.

I am a writer who honest-to-god composes tweets and blog posts for a living.

My command line experience is limited to a Codecademy course I took back before the iPhone 5 was released. I know how to type `ls` to see the contents of a folder without visual styling. Tl;dr I’m a hacker badass.

All the same, friends, I wrote an app. And it’s hosted. And you can go visit it yourself, from your own personal computer.

Because, as I have discovered, [AWS Lambda](https://aws.amazon.com/lambda/) and the [Serverless Framework](http://serverless.com/framework) make it **really** not that hard to deploy an application.

Here’s how you, too, can write and deploy a serverless app with basically zero coding experience.

### Ok but like…why did you do this?

So glad you asked! Because, look — automation is power.

Just like you, I have things — too many things — to do, and not enough resources to get them done.

I want to write slack bots that remind people when their blog drafts are due. I want to create drip campaigns based on user behavior without blowing my budget on fifteen marketing tools. I want to automerge blog posts according to a pre-set schedule.

Custom apps give me that. I could create a **team of robot minions**.

### Making the app

This whole project took me maybe an hour.

Here is what we’re going to do:

* Install the Serverless Framework
* Create an AWS account
* Set up AWS permissions (IAM roles) for my serverless user
* Find some freely-available code on npm that does close enough to what I want
* Steal it
* Tweak it
* Deploy it up to Lambda using the Serverless Framework

The cool thing about Lambda is, I don’t have to manage it or provision it or scale it **or anything**. I throw my code up there, and it runs when it needs to. I can deploy this and basically forget about it.

The cool thing about the Serverless Framework is, AWS is hard to figure out. The Framework takes care of all the details behind the scenes, and frankly makes it pretty impossible to mess up.

Case in point: me. I didn’t mess it up.

This thing is bullet proof.

### Install the Serverless Framework

If you don’t already have Homebrew (I didn’t), you’ll need to install that first. [Homebrew](https://brew.sh/) makes it easy to install all kinds of developer stuff on your machine.

Open your terminal, and paste the snippet from the Homebrew homepage:

```
/usr/bin/ruby -e “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Wait an eternity (aka 5 minutes) for it to finish, and then install Node; the Framework requires this to run:

`brew install node`

Then paste the snippet from the Serverless.com homepage:

`npm install serverless -g`

Congratulations! You’ve made it this far using only copy/paste.

### Create an AWS account

Go to [aws.amazon.com](https://aws.amazon.com/) and click one of the fifteen helpful buttons that let you create a new account. I chose the one in the top right corner:

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

They will make you answer a lot of questions. Sorry about that. This will all be over soon.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

When they ask for you credit card, you’ll have to give them one. They don’t charge you for anything up front, but they keep it on file just in case they ever have to.

![Image](https://cdn-media-1.freecodecamp.org/images/7VTKpigfo8aAw9ZJx07wazSRe4qGdqhicMtK)

Ok I lied about the “over soon” part. Now they’ll want to verify your identity by having a robot call you on the phone (lol). Just appease them, we’re seriously almost done this time.

When your phone rings, enter the 4-digit PIN on your screen. I looked at the timer on my phone; it was a 20 second call.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Finally, choose your support plan! Which is to say, do not choose a support plan. Unless you are a real company, I guess, in which case spend those investor dollars however you want.

Here I am not being a real company and choosing the “Basic” option because it’s free:

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Now go ahead and click “Launch the console” and log in again.

All said and done, this stage takes 5–10 minutes, depending on whether or not you (humble brag) have your credit card number memorized because you are a prolific online shopper.

### Configure an IAM user

The Serverless Framework needs this in order to do all the complicated Lambda setup stuff on your behalf.

Sounds like a great trade to me! Let’s do it.

It’s worth noting that I used [this incredibly helpful walkthrough](https://serverless.com/blog/anatomy-of-a-serverless-app/) to guide me throughout the entire setup process. You might like it too.

Now that you’ve launched your AWS console, type “iam” into that handy search box:

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Why yes, we would like to manage “User Access” and “Encryption Keys.” Click dat.

Once you’re inside IAM, go to “Users” in the lefthand menu:

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

And then “Add user” up top:

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Now we need to configure this new user.

You can either [watch this 75 second video](https://www.youtube.com/watch?v=yaLMc7WMmHQ&index=1&list=PLIIjEI2fYC-A5wxo521u6OqAwbsFFQFbW) and do exactly what they do, **or** if you’re a nerd for abstractions, you can scroll through these screenshots of **me** doing exactly what they do and copy those instead.

Create any user name you want and check the box beside “Programmatic access”:

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Click “Attach existing policies directly” and then check the box beside “AdministratorAccess”:

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

It’s worth noting that, according to [this Serverless.com blog post on IAM](https://serverless.com/blog/abcs-of-iam-permissions/), taking the “AdministratorAccess” route is the “Fast but risky YOLO method.” I’m going to do it anyway because I’m not a developer and therefore do not understand the havoc I may wreak.

Please don’t hack me.

If you want to be extra diligent about it, follow their guidelines on the [slow but safe approach](https://serverless.com/blog/abcs-of-iam-permissions/#managing-permissions-for-the-serverless-framework-user).

Go ahead and click “Next” and then “Create user.”

You will land on a screen like this. **Don’t close this window yet, we’re about to need it**:

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

#### Install AWS CLI

This will let us (1) do stuff with AWS without poking through their intimidating interface with too many icons; (2) mindlessly copy/paste stuff into the terminal that experts on the internet say will do what we want.

To start off this copy/paste party, put `brew install awscli` in your terminal to make Homebrew install the AWS CLI for you.

After that’s done, type `aws configure`.

Now you’ll need that IAM user window, which you definitely haven’t closed! Copy the “Access key ID” and “Secret access key” from that window and paste them into the terminal as prompted.

I’m leaving the other stuff blank because (as we’ve already covered) YOLO:

```
AWS Access Key ID [None]: PLZ-PUT-UR-ACCESS-KEY-HEREAWS Secret Access Key [None]: PLZ-PUT-UR-SECRET-ACCESS-KEY-HEREDefault region name [None]: Default output format [None]:
```

### Surfing NPM for pre-written code

Since I’m a hipster with an ironic sense of humor, I decided to make my first serverless app a Serverless Ipsum generator.

It’s like Lorem Ipsum, but with randomized “serverless movement” buzzwords. Get it. It’s a serverless Serverless app. ?

I went over to [npmjs.com](https://www.npmjs.com/), which is a magical website where people with hearts much bigger than mine post their NodeJS code so other people can use it. …for free. I still can’t believe this actually exists.

I typed “lorem ipsum” into the search box and evaluated my options.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

I clicked the one that was simply called “lorem-ipsum,” because as a professional writer I have an affinity for word choice minimalism. (Thanks [knicklabs](https://www.npmjs.com/~knicklabs)!)

Let’s snag it.

But first we need to create a place to put it. A new serverless project, if you will.

#### Using the Serverless Framework to create a new project

Remember at the top of this post, when we did `npm install serverless -g`? That installed the Serverless Framework, which we’re now going to use!

First, let’s make a folder to keep all of our numerous future serverless projects in. I’m going to call my folder “Code” because it rhymes with Node and I’m a poet.

Here’s where my badass Codecademy hacker skills become relevant. In your terminal, type `ls` to see all your folder names. (I don’t actually think there’s a reason you **need** do this, but there’s no reason not to do it either, so might as well get warmed up.)

You should be looking at a list of all the folders on your desktop right now, in a clean monospaced font. Magical.

Now type `mkdir Code` — aka, “make a directory (folder) called ‘Code.’’’ Then `cd Code` to navigate there.

Inside this brand new “Code” folder, I am going to create my very first serverless app ever. Watch me go:

`serverless create --template aws-nodejs --path serverless-ipsum`

The`--template aws-nodejs` part tells Serverless that we are using AWS and NodeJS. They’ll use that info to do magical setup/configuration tricks on our behalf.

The `--path serverless-ipsum` part tells Serverless that our new project is called “serverless-ipsum.” So you should replace serverless-ipsum with whatever you want your project name to be.

When you press `enter`, Serverless will create a new folder called “serverless-ipsum.” All of your application stuff will live there.

We just made the beginnings of an app. Now let’s give it some code to run.

#### Installing that lorem ipsum package from NPM

Navigate to that serverless-ipsum directory we just created by typing `cd serverless-ipsum` in your terminal.

Then type `npm install lorem-ipsum` to install the lorem ipsum package from NPM.

Now our app folder has code in it! It’s basically an app already! Sort of.

#### Tweaking that NPM code

We do have to make some tweaks to that code, so go on and open up your favorite code editor. I used [Atom](https://atom.io/) because I do not have a favorite code editor but I do have a favorite unit of matter.

Anyway this is what your `handler.js` file should look like right now:

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Open it up and replace the stuff up top with this:

```
'use strict';
```

```
const ipsum = require("lorem-ipsum")
```

```
module.exports.hello = (event, context, callback) => {  const response = {    statusCode: 200,    body: ipsum(),  };
```

```
callback(null, response);};
```

Such that your `handler.js` file now looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/jc2AY8UcAB3waJg0X-lbBk-clwiFRHP0BIPg)

What we did here was tell our little function handler to run that `lorem-ipsum` package we downloaded and print the output for us.

We first required the package up top with `const ipsum = require("lorem-ipsum")`, and then told the `body` to print out that generated ipsum with `body: ipsum()`. Everything else stayed the same.

#### Testing it out locally in the terminal

Guys. We have created a serverless project in the Framework. We have downloaded some pre-written code that generates lorem ipsum.

We can tell Serverless to run this. Right now. In our terminals.

Moment of truth. Type: `serverless invoke local --function hello`

Wait for it…

```
{“statusCode”: 200,“body”: “Amet cillum est dolor eiusmod elit eiusmod nulla eu do.”}
```

Oh my god.

### Tweaking that pre-built lorem ipsum generator

Latin is great, but serverless gibberish is better. We are, after all, making a **Serverless** Ipsum generator.

Go back to Atom, where your “serverless-ipsum” project is probably still open. It contains several files, and we’re going to make it contain one more.

Hit `cmd/ctrl + n` to create a new file, and name it `dictionary.js`. Create an [array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) and fill it with industry buzzwords like “Lambda” and “serverdeath”:

![Image](https://cdn-media-1.freecodecamp.org/images/wU4Xhy41DtdJw3m9yV2KAHra3RyG0wWRGoAA)

For those of you who are exclusively on the copy/paste train, here you go:

```
module.exports = ['auto-scaling','zero-maintenance','pay-per-execution','serverdeath','function','event','handler','cloud','NoOps','Lambda','microservices','monitoring',]
```

Then save the file with `cmd/ctrl + s`.

We also have to go back into our `handler.js` file, and tell it to use the dictionary file we just made.

So click in to `handler.js`, and stick this up top:

```
const dictionary = require("./dictionary")
```

Now go into the `body` of your function again, and tell it to pull all its words from the dictionary you just made, i.e.:

```
module.exports.hello = (event, context, callback) => {  const response = {    statusCode: 200,    body: ipsum({      words: dictionary,    }),  };
```

Your `handler.js` file should now look like this:

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Let’s try it out locally again, and see if the output is Serverless Ipsum instead of Lorem Ipsum. Go back to the terminal and re-type that `--function` command from before:

`serverless invoke local --function hello`

Wait for it…

```
{“statusCode”: 200,“body”: “Multi-cloud openWhisk google cloud functions lambda source services signature function monitoring zero-maintenance monitoring multi-cloud azure.”}
```

This is literally the most beautiful thing I’ve ever seen.

### Let’s put this thing on the internet

Yeah yeah, ok, so it works on your personal laptop. But real devs got their stuff available on **Chrome**.

That takes one more tiny step.

#### Tweaking that serverless.yml

The serverless YAML (`serverless.yml`) is the configuration file Serverless uses to manage the functions (aka, bits of code) you deploy to Lambda. We need to tell it to make a little website for us.

This is what our `serverless-ipsum` YAML file currently looks like (all comments collapsed for concision):

![Image](https://cdn-media-1.freecodecamp.org/images/MtSdYP0449FYoFNF3rBocTw97JBEzSlJtosH)

We’re going to change a couple things in the `functions` portion.

That “hello” stuff is by default. We’re going to replace it with “ipsum,” because I rather reasonably decided that I wanted to run Serverless Ipsum with the command `ipsum`. (**Note:** This means that from now on, you’ll run `--function ipsum` instead of `--function hello`.)

Then we’re going to tell the function handler that, when we run `ipsum`, what we actually want it to do is post Serverless Ipsum to a public URL via HTTP request.

Blah blah blah just go to line 57 in your editor and replace all that stuff with this:

```
functions:  ipsum:    handler: handler.ipsum    events:      - http:          method: get          path: /
```

And now your `serverless.yml` should look like this!

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Go back to your `handler.js` file and change `module.exports.hello` to say `module.exports.ipsum`. This is because we changed our function name from “hello” to “ipsum.”

So now your `handler.js` file looks like this:

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

#### Deploy deploy deploy!

It’s time. We are ready to launch this thing for real.

Get yourself in that terminal.

Type `serverless deploy`.

Hold your breath.

And —

(!!!)

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

BOOM.

Take that url beside `GET`: [https://791qej6263.execute-api.us-east-1.amazonaws.com/dev/](https://791qej6263.execute-api.us-east-1.amazonaws.com/dev/?paragraphs=6)

Copy/paste it into your browser, and behold:

![Image](https://cdn-media-1.freecodecamp.org/images/kDNZvno6vKXA5fvrbIoZ-kbQ1KRXkmNIxIU1)

Our app. Is alive. **On the internet!**

### Things I still have to do

Ok so, let’s be real. The UI is not pretty. I plan to actually get a domain for this and give it some sort of simple frontend so it looks at least plausibly professional.

Another day, friends. Another day.

### In sum

I am a writer. I can’t code. But I made a serverless application and I put it on the internet for all to see.

Serverless: **literally anyone can do it**_._

AWS: **not that scary** after all_._

Hope you all use this to make something cool.

