---
title: Amazon has made it easier to add sounds to custom Alexa Skills
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-27T08:06:57.000Z'
originalURL: https://freecodecamp.org/news/amazon-has-made-it-easier-to-add-sounds-to-custom-alexa-skills-513b865d7528
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iXOMQlmW4OqiYidOPVfatw.jpeg
tags:
- name: AWS
  slug: aws
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Terren Peterson

  I’m recognized as an Amazon Alexa Champion and have published more than twenty custom
  skills on the platform. I continue to look for new ways to stretch this technology,
  and one of the best ways I’ve found to improve the user exper...'
---

By Terren Peterson

I’m recognized as an Amazon [Alexa Champion](https://developer.amazon.com/alexa/champions/terren-peterson) and have published more than twenty custom skills on the platform. I continue to look for new ways to stretch this technology, and one of the best ways I’ve found to improve the user experience is by adding sounds. Given [the recent improvement](https://developer.amazon.com/docs/custom-skills/ask-soundlibrary.html) to the Amazon Alexa platform, this has just gotten even easier. Here is a brief review on how you can take advantage of this new feature.

### How Amazon Alexa works

The Alexa platform has the ability to enable custom skills made by third-party developers. There are now more than 30k of them available, and the millions of Alexa users can enable them on their devices. These range from ordering a pizza from a popular chain to playing sounds to aid sleeping.

The architecture for these custom skills has two components. The first is the voice component that leverages the machine learning models of the Alexa platform. This is what translates the spoken word requests into a set of instructions.

The other component is the if/then/else logic that decides what answer should come back to the user. This is hosted on an AWS Lambda function.

![Image](https://cdn-media-1.freecodecamp.org/images/uktbt4NNJPyLIOzMTI0SWzAgriH5OMiOVhAc)

To enhance skills, additional AWS services can be used, as well as third-party tools. This includes recording custom MP3 sounds and graphics that can be leveraged by the Lambda function.

![Image](https://cdn-media-1.freecodecamp.org/images/5Iwg4WP1zl0gepFBIRJU70TyWHQeHhksGibI)

To add sounds, MP3 files are uploaded into an S3 bucket, and the appropriate access policy is applied so that it can be read by an Alexa device.

### Challenges with adding custom sounds

One of the barriers to entry for including sounds into custom skills has been the ability to record high-quality sounds. These sounds need to match the exact standards for the platform, including bit rate and sample rates. This can be done through sound editing expertise using software like Audacity, but adds time to developing the skill.

Recording high-quality sounds can also be a challenge. There are apps for mobile devices that enable recording, but access to a wide variety of sounds is difficult. For example, recording the roar of an airplane, or the sound that an elephant makes.

Alternatively, an Alexa developer can search for sounds that have been recorded by others. There are some repositories on the internet that have these, but most cost money to license and require resampling with software like Audacity to get the right sound attributes.

### Free MP3 content

Amazon has now published a catalog of hundreds of sounds already recorded under the exact standards required by the platform. Just like in the architecture diagram above, they are published into an S3 bucket on AWS and can be used by any custom skill.

The complete list is provided on the [developer page](https://developer.amazon.com/docs/custom-skills/ask-soundlibrary.html), and here are the main categories.

![Image](https://cdn-media-1.freecodecamp.org/images/3fgPZrn6W9hhJIGCrXOYgH6bTs2pYm82ZH8e)

The range is expansive. Motorcycle engines, fireworks noises, and the roar of a bear are all at your fingertips. There are no royalties required for using these, and the cost for downloading the sound clips is not charged to your AWS account.

### How to use sound in a basic skill

If you’re just getting started with Amazon Alexa, start with the basic templates from the [Alexa GitHub page](https://github.com/alexa). This includes building a trivia skill, fact skill, or simple guessing games. For example, I recently published a fun kids skill called Easter Egg Hunt. [Here is the complete repo](https://github.com/terrenjpeterson/eastereggskill) on GitHub, including both the Lambda function as well as the intent model.

With any of the message responses, you can add the SSML syntax to include the link to the MP3 file in the S3 bucket. Here is an example from the Welcome Handler for the Easter Egg skill.

```js
// This is the initial welcome message
var welcomeMessage = "<audio src=’https://s3.amazonaws.com/ask-soundlibrary/musical/amzn_sfx_trumpet_bugle_03.mp3'/>Welcome to the Easter Bunny Egg Hiding Game. I will ask you multiple questions that you should answer yes or no. Based on your choices, I will make a recommendation on where to hide an egg. Are you ready to begin?";

this.emit(':ask', welcomeMessage, repeatWelcomeMessage);
```

When the user first invokes this custom skill, the Alexa device plays the sound clip for the trumpet bugle, then reads the syntax with the standard voice.

### Ready to get started?

Go ahead and sign-up for a [free developer account](https://developer.amazon.com) on Amazon, and start building your first skill today! The Amazon developer blog has some great resources to leverage on this topic, including this [recent post](https://developer.amazon.com/blogs/alexa/post/c202ca98-ed68-440b-adb3-73ae9d8f36da/how-to-enhance-your-alexa-skill-with-audio-clips-from-the-ask-sound-library) giving ideas on how to use this new content.

