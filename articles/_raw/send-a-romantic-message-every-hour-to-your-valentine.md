---
title: How to Declare Your Love Like a Programmer ❤️
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-14T11:19:17.000Z'
originalURL: https://freecodecamp.org/news/send-a-romantic-message-every-hour-to-your-valentine
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/declare-your-love-as-a-programmer.png
tags:
- name: Node.js
  slug: nodejs
seo_title: null
seo_desc: 'By Florin Pop

  Today is Valentines Day! ?

  How nice would it be if you sent a Romantic Message every hour to your loved one?
  But even better...

  How awesome would it be to do it automatically using a Node.js script? We are after
  all... programmers, righ...'
---

By Florin Pop

Today is Valentines Day! ?

How nice would it be if you sent a Romantic Message every hour to your loved one? But even better...

How awesome would it be to do it automatically using a Node.js script? We are after all... programmers, right? ?

In this short tutorial I'm going to show you how to do it.

P.S. For the lazy ones out there, here is a Video Tutorial:

%[https://youtu.be/HxqMPlyZC3w]

## Create a CRON job

First, we need to create a CRON job which will run a function every hour.

For that, let's install the `node-cron` package into our NodeJS app:

`npm install node-cron`

Next, we're going to schedule a function to run every hour:

```js
const cron = require('node-cron');

cron.schedule('0 * * * *', () => {
	sendMessage();
});
```

Perfect. We don't have the `sendMessage()` function yet, but we'll create it later.

Also, in case you don't know how the CRON string works, here is an [awesome website](https://crontab.guru/#*_*_*_*_*) where you can test it out.

Basically `'0 * * * *'` means: `Run every hour at 0 minutes`, so it will run at: `00:00, 01:00, 02:00`, etc... You get the point!

## Connect to Twilio

We need a Twilio acount, so head over to [Twilio.com](www.twilio.com/referral/79CRPu) and create one. You need to verify your email address and also verify the number you want to send the message to. (I had to "steal" my wife's phone in order to verify the number ?)

In there they'll ask you a couple of questions like: "What programming language are you using?" You can pick Node.js and then you'll end up on the `/console` page.

Here you'll get the `ACCOUNT SID` and `AUTH TOKEN`. We need these to call the Twilio API so we are going to store them inside a `config.js` file.

**Warning:** Do not share the **AUTH TOKEN**. This is a secret key so we're going to store them inside this "secret" config.js file.

Great.

The next thing will be to create a Trial Number (you can find the button on the `/console` page). This number will be used to send the messages FROM.

Now that we have everything in place, let's go back to our code!

We need to install the Twilio package: `npm install twilio` and we need to use the data we stored inside the `./config.js` file.

Along with the `ACCOUNT_SID` and `AUTH_TOKEN` we can also store the `PHONE_NR` of our loved one as we are going to use this to tell Twilio where to send the message TO.

Let's do that and also let's create the `sendMessage()` function, which will... send a message ?.

```js
const config = require('./config');
const accountSid = config.ACCOUNT_SID;
const authToken = config.AUTH_TOKEN;
const client = require('twilio')(accountSid, authToken);

function sendMessage() {
	client.messages
		.create({
			body: 'Your Message here',
			from: '+19166191713',
			to: config.PHONE_NR
		})
		.then(message => {
			console.log(message);
		});
}
```

You can see that the `client.messages.create()` function required three things:

1. The body/the message
2. The FROM number (this is the trial number created above)
3. The TO number (this is the number we want to send the message to)

## Get the messages

We need a list of 24 romantic messages, so for that let's create a `messages.js` file and put all the messages in there inside an array.

```js
module.exports = [
	`If I could give you one thing in life, I'd give you the ability to see yourself through my eyes, only then would you realize how special you are to me.`,
	`If you were a movie, I'd watch you over and over again.`,
	`In a sea of people, my eyes always search for you.`
];
```

I only added 3 messages above, but you can fill the array up until you get to 24 messages.

## Combine everything

Now that we have all the 3 components:

- the CRON job
- the Twilio sendMessage() call
- the messages

We can combine them into the final code:

```js
const cron = require('node-cron');

const config = require('./config');
const accountSid = config.ACCOUNT_SID;
const authToken = config.AUTH_TOKEN;
const client = require('twilio')(accountSid, authToken);

const messages = require('./messages');

const currentMessage = 0;

function sendMessage() {
	client.messages
		.create({
			body: messages[currentMessage],
			from: '+19166191713',
			to: config.PHONE_NR
		})
		.then(message => {
			currentMessage++;
			console.log(message);
		});
}

cron.schedule('0 * * * *', () => {
	console.log('Message sent!');
	sendMessage();
});
```

You can see that I added a `currentMessage` counter which will be incremented every time we send a message, this way we're going to loop over the entire array of messages.

That's it! ?

Now you can run the script and it'll send a romantic message, every hour, to your loved one!

Happy Valentine's! ?

_Originally posted on [www.florin-pop.com](https://www.florin-pop.com/blog/declare-your-love-as-a-programmer/)_

