---
title: How I built Helpline Kerala and contributed to flood relief
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-01T15:11:04.000Z'
originalURL: https://freecodecamp.org/news/helpline-kerala-aog-my-contribution-to-flood-relief-kerala-4b2d55b42b8f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*EFby75Mad0ELMyC7N_F58g.png
tags:
- name: Flood Relief
  slug: flood-relief
- name: Apps
  slug: apps-tag
- name: Google
  slug: google
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Farha Kareem

  In August 2018, severe flooding affected the south Indian state of Kerala due to
  unusually high rainfall during monsoon season. They were the worst floods in nearly
  a century. All 14 districts were placed on red alert.

  I had always wa...'
---

By Farha Kareem

In August 2018, severe flooding affected the south Indian state of Kerala due to unusually high rainfall during monsoon season. They were the worst floods in nearly a century. All 14 districts were placed on red alert.

I had always wanted to develop an action on Google, so I went to the [website](https://developers.google.com/actions/) and checked out the [codelabs](https://developers.google.com/actions/codelabs/) created by [ActionsOnGoogle](https://twitter.com/ActionsOnGoogle). I learned about the codelabs from [Mandy Chan](https://www.freecodecamp.org/news/helpline-kerala-aog-my-contribution-to-flood-relief-kerala-4b2d55b42b8f/undefined) and the [Systers](https://www.freecodecamp.org/news/helpline-kerala-aog-my-contribution-to-flood-relief-kerala-4b2d55b42b8f/undefined) online workshop.

They conducted 2 workshops — you can listen to them [here](https://zoom.us/recording/play/S6_gDt2Dse56QZN0XzXmp3dXSSugukGodRzTwBQOCuWNwin7xBaWGEASGFO07kWA?continueMode=true) and [here](https://zoom.us/recording/play/ihyYoJja6iJBUyLLWXBlGnbpNEd_alT46d4AYfFsuhVkzCS_Qdf3d-w89uk3JaaA?continueMode=true).

Both of these online workshops were curated and taught by [Mandy Chan](https://twitter.com/MandyChanNYC).

I learned most of the basics from these resources, and they helped me build my action. I would recommend codelabs to everyone who wants to learn how to build one, too.

I happened to be living in Aluva during the time of the floods. You can read my [previous story](https://medium.com/@farhakareem/how-floods-in-kerala-affected-me-4d1b0e3a7b57) to know how the floods affected me.

I had this idea of making an action which could serve as a link to the website keralarescue.in. I discussed the idea with a couple of my friends and we thought about the different issues like language, the number of people who would be using google assistant, and their likely panicked state. These issues kept me away from going further with the plan.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ykjEJBQjY5ITI3kZrQ0rGA.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*9gft1hKAcqtNSPMdPXkJNg.jpeg)
_discussion about the action with my friends_

Later, I joined a Whats App group called _Ernakulam relief camps._ It was intended to help volunteers at various relief camps sort out excess or under-met needs at different camps in the Ernakulam district.

This group was later flooded with a lot of messages each day asking for help and sharing helpline numbers, both valid and invalid. At first, I took up the job to sort between valid and invalid messages in a Google sheet with the help of my 12-year-old cousin [Adil AbdulKhader](https://www.freecodecamp.org/news/helpline-kerala-aog-my-contribution-to-flood-relief-kerala-4b2d55b42b8f/undefined).

But all these efforts went in vain. Then I decided to circulate a google form, but nothing seemed to work.

I had told my friend [Joel Vilanilam Zachariah](https://www.freecodecamp.org/news/helpline-kerala-aog-my-contribution-to-flood-relief-kerala-4b2d55b42b8f/undefined) about my interest in developing an action. He messaged me telling me that it would be the perfect time to deploy my idea.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pONLV-vfCLCkr5NOtF8Oww.jpeg)
_Joel’s message_

I decided then to take up the project seriously. Since I knew how difficult it was to get valid helpline numbers, I decided my action would be based on that. That’s how helpline Kerala took off!

![Image](https://cdn-media-1.freecodecamp.org/images/1*5uOTYGyahCGkI6cVxkYERw.jpeg)
_Helpline Kerala_

I started collecting valid numbers of suppliers of different resources and then decided to put them up on my app. I built the app with my basic knowledge. [Adil AbdulKhader](https://www.freecodecamp.org/news/helpline-kerala-aog-my-contribution-to-flood-relief-kerala-4b2d55b42b8f/undefined) helped me with the images necessary to deploy the app. With a little guidance from my friend [Adarsh Menon](https://www.freecodecamp.org/news/helpline-kerala-aog-my-contribution-to-flood-relief-kerala-4b2d55b42b8f/undefined), we got it deployed.

My app was centered around two parts: Donations and Ask for help. So for the donation part, I asked [Mandy Chan](https://www.freecodecamp.org/news/helpline-kerala-aog-my-contribution-to-flood-relief-kerala-4b2d55b42b8f/undefined) if there was an option for developers to ask for payments for donations. She told me that it was currently not supported and that she would share the idea with the team.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hnLVQLPgbweksjnDRJdDJQ.jpeg)
_Successfully Rejected!_

I got an email with a detailed explanation of why my app got rejected:

* The privacy policy URL was incorrect.
* My app left the mic open at times unnecessarily.

This was great motivation to do better. I connected on twitter with [Wassim Chegham](https://www.freecodecamp.org/news/helpline-kerala-aog-my-contribution-to-flood-relief-kerala-4b2d55b42b8f/undefined), who is the GDE for actions on Google, and asked him for help. He told me to add him as a collaborator so he could check out my work. He soon discovered what my issue was:

* When sys.any is used, you can replace it with any word.
* Follow up intents should be avoided because it would make it more complicated for my use case.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wW99FIg3kLj98jdRLJ80DA.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*IvIMwU6LKVVdpXAVGcvMgQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*0JtMyWmx-9iavdX8lhKipQ.jpeg)
_Guidance_

He also provided me with a sample privacy policy from his app. With proper guidance I was able to develop my action, and then deploy it as well.

The next day, I got an email saying that my app was approved!

![Image](https://cdn-media-1.freecodecamp.org/images/1*bQFD1WIaTaZF8JXspYxbpA.jpeg)
_Approved!_

Here is a demo of my action — please feel free to check it out :)

Also, you can check it out on Google Assistant by asking to “_Talk to Helpline Kerala.”_ I have provided the link [here](https://assistant.google.com/services/a/uid/0000004adeb95783?hl=en)_._

This was definitely a wonderful experience!

