---
title: My Outreachy internship begins today! Here’s what I’ve done and learned so
  far.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T01:24:58.000Z'
originalURL: https://freecodecamp.org/news/my-outreachy-internship-begins-today-heres-what-i-ve-done-and-learned-so-far-88fef9c18619
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VLRQmKC6ipGiZS3il-wQWw.jpeg
tags:
- name: healthcare
  slug: healthcare
- name: internships
  slug: internships
- name: learning
  slug: learning
- name: Life lessons
  slug: life-lessons
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Toni Shortsleeve

  Today marks the first day of my official full-time Outreachy Internship with LibreHealth.
  If you missed my first story about how I got this wonderful internship, check it
  out here. It’s been quite a journey!

  I’m thankful for the b...'
---

By Toni Shortsleeve

Today marks the first day of my official full-time Outreachy Internship with LibreHealth. If you missed my first story about how I got this wonderful internship, check it out [here](https://medium.freecodecamp.org/how-i-beat-the-odds-and-became-an-outreachy-intern-9a92f47cb44e). It’s been quite a journey!

I’m thankful for the break between being accepted and actually getting started. It has allowed me to wrap up some of my previous projects, and I spent part of my time preparing for today. In this article, I’ll give a brief overview of what I’ve done — and learned — so far.

### Getting started

I’ve been doing research on the clinical practice workflow and procedures through the [LibreHealth](https://www.youtube.com/channel/UC4bKSiSB7196D5W3xGGKxqQ/featured) YouTube videos. Since there are two videos that had not been transcribed yet — and they were the subjects I needed a stronger understanding of — that’s where I began.

I worked with the LibreHealth Electronic Health Record (EHR) system. I created a patient who was in need of a referral for an x-ray. Then I created the lab that would perform the x-ray.

I also created three users. They were the Front Desk Receptionist, the LPN, and the Transcriber. I didn’t even know there was a transcriber in the medical field, but now it makes a little more sense.

### Who can do what

The Front Desk receptionist, Tina, is only allowed to see specific patient demographics. She welcomes the patient and assigns available exam rooms. In this setting, Tina will escort the patient to the Nurse’s Station.

At the Nurse’s Station, Dana is the LPN who will take the vitals of the patient. This requires a specific form that must be filled in properly. This is an intimidating form. It was asking for both imperial and metric measurements. So it was a pleasant surprise to find that the system automatically calculated the metrics for me.

Once Dana completes the process of entering the patient’s vital information, she escorts the patient to the exam room.

The doctor was already in the system as a provider, so I did not need to create a profile for her.

### Notes and codes

But the doctor did need to make a Subjective, Objective, Assessment Plan (SOAP) note. This was complex. It needed to say what the patient said, what the doctor saw, what the doctor suggests the issue may be, and then how the patient should be treated for it.

At first, I thought that “Objective” would make more sense if it were labeled “Observation.” But then I realized it might mean that that the doctor should be an objective observer.

According to my mentor, my first try was close — but I had a couple of things backwards. Once I was heading in the right direction, my updated SOAP made sense, too. One mistake I made: I signed it too soon. Then I had to start over, because e-signing a SOAP will lock it and I wasn’t ready for that yet.

Then the doctor needed to create a Procedure Order — this is also known as a Provider Order. This order form tells the staff what needs to be done for the patient, such as sending samples to a lab or referring to a specialist. It also requires a diagnosis code.

The [International Classification of Diseases](https://searchhealthit.techtarget.com/definition/ICD-10) (ICD) 10th revision is the most current clinical cataloging system. I went back to Google and found the ICD10 code for an x-ray of a sprained wrist. There a lot of sub-codes! What part of the hand? Is this the initial x-ray or a sequential view?

I checked with my mentor again, and I got the code right! This was a lot more difficult than finding a simple JavaScript error or resolving why my code wasn’t rendering on the screen. Learning something new every day!

### Sending it on

Marc is the Clinician who is tasked with transcribing the Procedure Order and sending it to the lab.

His job is interesting. He creates a Referral Form based on the information from the Procedure Order.

[Current Procedural Terminology](https://searchhealthit.techtarget.com/definition/Current-Procedural-Terminology-CPT) (CPT) 4th Edition is the most current medical code set that is used to report medical, surgical, and diagnostic procedures and services for medical billing purposes.

Marc added CPT4 codes based on the ICD10 code.

And this is where I was stuck for a while. Once again my mentor came to the rescue so I could continue forward.

Once Marc submitted and e-signed the Referral Form, the patient was able to pay and check out — and hopefully schedule that x-ray.

### My documentation

My document was submitted for review on May 22, the day before my new Outreachy Internship officially began. I have been given a lot of areas that need to be revised.

I have my work cut out for me. I will revise the current document, and transcribe the other video based on the feedback from this document.

I am hopeful that within a few short weeks I will be able to track the Radiology work-flow. It’s part of the LibreHealth system, but it’s a totally different style and workflow from anything I’ve worked with before.

### More to come

I am so glad I had the time to accomplish as much as I did in preparation for this internship. Although I didn’t immediately get everything right, I am learning a lot and looking forward to learning more.

Thank you for being with me on my Outreachy journey.

