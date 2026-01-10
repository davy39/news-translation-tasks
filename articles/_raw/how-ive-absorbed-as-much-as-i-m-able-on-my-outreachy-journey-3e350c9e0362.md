---
title: How I’ve absorbed as much as I’m able on my Outreachy Journey
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-11T21:50:28.000Z'
originalURL: https://freecodecamp.org/news/how-ive-absorbed-as-much-as-i-m-able-on-my-outreachy-journey-3e350c9e0362
coverImage: https://cdn-media-1.freecodecamp.org/images/1*l2XMmdd_4upTGH10T0kKPw.jpeg
tags:
- name: Health,
  slug: health
- name: internships
  slug: internships
- name: Life lessons
  slug: life-lessons
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Toni Shortsleeve

  I can’t believe this will be the last month of my internship at LibreHealth! ?

  Just when it was starting to all come together. But I still have a few more weeks
  to finish my projects, and I’m thankful for the time to work on them....'
---

By Toni Shortsleeve

I can’t believe this will be the last month of my internship at LibreHealth! ?

Just when it was starting to all come together. But I still have a few more weeks to finish my projects, and I’m thankful for the time to work on them.

For those of you just joining me on my journey, I am an [Outreachy Intern](https://www.outreachy.org/alums/) at [LibreHealth](http://librehealth.io/) for this summer. I was accepted on April 23 this year to begin my internship on May 23, lasting until August 14. You can read more about how it started [here](https://medium.freecodecamp.org/how-i-beat-the-odds-and-became-an-outreachy-intern-9a92f47cb44e).

Since my last [article](https://medium.freecodecamp.org/special-moments-on-my-outreachy-journey-78db1ff11ef4), I have learned so much. The two documents that I’ve been working on, the [LibreHealth EHR Provider Orders](https://wiki.ehr.librehealth.io/LibreHealth_EHR_Provider_Orders) and the [LibreHealth EHR Encounters](https://wiki.ehr.librehealth.io/LibreHealth_EHR_Encounters), were approved by my mentors and are now on the LibreHealth wiki.

> **Note:** Patient and staff names or any data you may see inside my documents are completely fictional.

#### My Outreachy LibreHealth Internship so far

In the **Provider Orders** document, we covered everything from the patient’s visit to referring the patient to an outside lab, and then transcribing the order.

**Medical Transcription** was a new concept for me. When I first read the word “transcriptionist”, I imagined it being the court reporter being asked to read back notes from the previous witness. ?

It actually involves two documents being compared to each other, and then the Provider Order information is placed into the Referral Order form.

Sometimes the terms were similar, such as **Referral Date**…

![Image](https://cdn-media-1.freecodecamp.org/images/yRVfSmYbUmqknbTBGEaYrs8B-oeCPBT3n6V0)

… and **Order Date**

![Image](https://cdn-media-1.freecodecamp.org/images/o5kWM-OFXaYmibY3QJE3549m1Wpmj7YdaFF6)

Others were not quite so obvious.

For instance, the **Reason** on the **Referral Form**

![Image](https://cdn-media-1.freecodecamp.org/images/JNeSmqHoLxAWzVr-4jzKQKFWUZzHO1gKdjyp)

… is the same as the **Clinical History** from the **Procedure Order**.

![Image](https://cdn-media-1.freecodecamp.org/images/dCosJ-mMlhn29T1vcr5UdHDGRV9hfcwmECCz)

When I design web pages, I am very spoiled with my coding. With HTML and CSS, I have the freedom to design my containers, image borders, and padding to keep space as needed. However, the wiki format doesn’t allow that.

A `<`;p&g`t; or` <br/> had no affect at all. Thanks to my [inter](http://king21.neowordpress.fr/focus-on-markdown/)n-mate Adele for sharing with me th`at I` needed <br> without the front slash. A totally different concept! I kept having to remind myself to break the habit of adding that front slash.

My mentor asked me to place these comparisons next to each other instead of above and below, to make it easier to read.

This is when I learned that wiki does take some HMTL in the formatting. Imagine my delight when I found that I could format my wiki with code like this:

```
<div><blockquote>‘’’Referral Transaction’’’: ‘Referral Date’ = ‘’’Procedure Order’’’: ‘Order Date’<br><br><span>[[File:trans-refDate.jpg|500px]] [[File:trans-ordDate.jpg|500px]]</span><br><br></blockquote></div>
```

And have it look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/mn0kSixpivfSzzsiqVG99Uq73Pxyuv-uCqO3)

I think this looks much better. My mentor also agreed. ?

#### Tackling new challenges

My two areas of challenge on the **Provider Orders** were the **Flow Board** and **Fee Sheets**.

**Flow Board:** The Flow Board tracks the patient time in each segment of the visit. It updates every few seconds. It also holds on to everything that happened during the visit, including my mistakes, and automatically attempts to fix them. I was finally told how to turn that off, but by then it was too late. ?

![Image](https://cdn-media-1.freecodecamp.org/images/s5y4Cs9lOfmNbfJ1tP-skr0CKPBkJYVUye1Z)

Notice how the **Appointment Time** did not match the **Start** or **End** time. And the **Total Time** needed to be changed too. Not only that, there should only be one of each status change.

Apparently the patient Arrived three times. She went into the Exam Room twice. Well, you see what happened. That was one busy patient. ?

Also, the **Total Time** had to add up to the total section times.

This is where my development background, and my best friend the Chrome Inspector, came to my rescue. ?

![Image](https://cdn-media-1.freecodecamp.org/images/gDJT-zwC9KSta-K65eoC8Fe8YsSEY6LotwUg)

I was able to go in and change the details, then close the Inspector and take a new snapshot. Of course, every time I forgot a specific change, I had to start over. This image took a few different tries to get right:

![Image](https://cdn-media-1.freecodecamp.org/images/StI-STzGWCY-LqnEvgRtovndrzoeY2gJZOx-)

The **Fee Sheet** had similar challenges because the codes needed to be added and the codes needed to be justified.

After struggling with the actual codes, I still had to make it look good in all areas.

![Image](https://cdn-media-1.freecodecamp.org/images/uIv2WkYDI8boVHFScxtwyJyM2kwoWmHPLeVI)

And on the final image, I needed to remove the extra codes. We only need one ICD10 code for one actual visit and prescription.

![Image](https://cdn-media-1.freecodecamp.org/images/IAuCtqoHSYfliX13XzlYioMu-aH-le9gDfSp)

In the figure above,

* CPT4 99203 is the code for a new patient visit and the price is $25.
* CPT4 96372 is the code for an injection. There is no cost as it is inside the medical cost.
* HCPCS J2800 is the code for the injection medicine.

Each of the above codes were justified with ICD10 code M54.5.

As you can see, ICD10 M54.5 is the medical billing code for Low back pain.

Initially, this took a long time for me to understand, and then to bring it all together. I am very thankful to my mentor Harley Tuck for his patience.

But finally I did it, and I was able to create the **Billing Screens** and **Final Receipt**.

![Image](https://cdn-media-1.freecodecamp.org/images/-NvK2DUMv9PrWtvEbEtUTPx1GUtGN1HTkMrO)

#### The home stretch

Those were my **LibreHealth EHR** assignments. Now I am moving on to the **LibreHealth Radiology** segment and it will flow a little differently.

During my internship, I was able to take some time out to prepare to meet up with other FreeCodeCampers in New York City.

#### freeCodeCamp 2018 Top Contributor Award

I was totally surprised to receive the email from [Quincy Larson](https://twitter.com/ossia) telling me that I was chosen to be recognized for my contributions to the [freeCodeCamp](https://www.freecodecamp.org/) Medium publication. I didn’t feel like I really did anything extraordinary.

I began to hang out in the chat rooms and forums a while ago because I wanted to know an answer to a question, or to learn a new solution to a problem. Then I started answering questions that I thought I knew the answers to. Sometimes I was actually correct. ?

I like coding. It forces me to use the logical side of my mind for problem-solving, and yet my creative side can make something pretty too.

But I also love to read. I am in an Advanced Review Copies (ARC) group for a couple of fiction authors. I like their work and I can sometimes spot an error before it gets published.

I’ve been reading the weekly articles sent by Quincy Larson, as well as the Medium Digest, since I joined freeCodeCamp. I found these articles helped me a lot, especially if the article was written at the same time that I was working on a similar project or trying to understand a similar concept.

So when the call went out for volunteer editors for the freeCodeCamp Medium publication, I saw this as a great opportunity to study under some of my favorite authors. I get to read the best articles first! And I try to help fix any typos or grammar issues that occur.

We have a great editing team, and I am proud to be a part of it.

When I applied for the Documentation Internship with LibreHealth, I used everything that I had learned editing here on Medium to help me with my work.

And so, when I got that email from Quincy, I mentioned the 2018 Top Contributor Award event to my mentor. He suggested that this could be made a part of my internship. It would then be possible to receive a stipend to help pay for my trip to New York.

My Outreachy coordinator, [Sage Sharp](https://twitter.com/_sagesharp_), agreed with my mentor! I will be in New York City on the 18th of August to celebrate with a bunch of other Top Contributors.

I will also have a chance to meet one of my other LibreHealth mentors in Manhattan during the day, before the freeCodeCamp event that evening.

And, of course, I also found out that some of my favorite freeCodeCamp heroes will be at the event. I’m excited!

#### Last Words - For Now

I would like to remind women and other under represented members in the tech industry:

The next round of Outreachy Internships starts in September 2018. That is less than a month away. If you have not already done so, and are interested in applying, [Sign Up Now](https://lists.outreachy.org/cgi-bin/mailman/listinfo/announce) to receive the announcements. You’ll be notified when the process begins.

And, freeCodeCamp campers are eligible to join too! ?

Thank you for staying on this journey with me. I’ll have more when I get back from New York.

#### **Previous Articles**

* [How I beat the odds and became an Outreachy Intern](https://medium.freecodecamp.org/how-i-beat-the-odds-and-became-an-outreachy-intern-9a92f47cb44e)
* [My Outreachy internship begins today! Here’s what I’ve done and learned so far.](https://medium.freecodecamp.org/my-outreachy-internship-begins-today-heres-what-i-ve-done-and-learned-so-far-88fef9c18619)
* [The next steps on my Outreachy journey: Docker, big challenges, and small victories](https://medium.freecodecamp.org/the-next-steps-on-my-outreachy-journey-docker-big-challenges-and-small-victories-2c3a2dd2277a)
* [Every step brings something new on my Outreachy journey](https://medium.freecodecamp.org/every-step-brings-something-new-on-my-outreachy-journey-e7c0f7adf2ea)
* [Special Moments on my Outreachy Journey](https://medium.freecodecamp.org/special-moments-on-my-outreachy-journey-78db1ff11ef4)

