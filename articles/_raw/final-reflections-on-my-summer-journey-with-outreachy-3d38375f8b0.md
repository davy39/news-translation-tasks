---
title: Final Reflections on my Summer Journey with Outreachy
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-24T22:49:12.000Z'
originalURL: https://freecodecamp.org/news/final-reflections-on-my-summer-journey-with-outreachy-3d38375f8b0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Mw4SmCZV23tSDsDsV8xuXg.jpeg
tags:
- name: coding
  slug: coding
- name: healthcare
  slug: healthcare
- name: Life lessons
  slug: life-lessons
- name: outreachy
  slug: outreachy
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Toni Shortsleeve

  Working as an Outreachy intern with LibreHealth this summer has been a great experience!
  Needless to say, I had mixed emotions when it was time to hand in my final project.
  I am proud of what I’ve contributed, thankful to have wor...'
---

By Toni Shortsleeve

Working as an [Outreachy](https://www.outreachy.org/) intern with [LibreHealth](https://librehealth.io/) this summer has been a great experience! Needless to say, I had mixed emotions when it was time to hand in my final project. I am proud of what I’ve contributed, thankful to have worked with great mentors and a fabulous intern-mate, and saddened that it ended.

For those needing to catch up, you can read about the [beginning](https://medium.freecodecamp.org/how-i-beat-the-odds-and-became-an-outreachy-intern-9a92f47cb44e) of my experience. The rest of my journey links will be at the end of this article. For those of you who have been with me throughout this summer, I’ll just jump right in.

### Projects

As a Documentation Intern, I provided some of the documentation on the LibreHealth Electronic Health Records system in English. [Adele](https://medium.freecodecamp.org/@nguimatiobest) was my intern-mate. She translated all of the documentation into French. You can follow her journey [here](http://king21.neowordpress.fr/my-internship-is-coming-to-an-end/).

From May 23 to August 31, I contributed four documents to the LibreHealth wiki.

#### User Guide

My first document was the [LibreHealth EHR User Guide](https://wiki.ehr.librehealth.io/LibreHealth_EHR_User_Guide). This was an overview of the basic appearance and features of the LibreHealth EHR system. We walked through the different screens and focused on the different functionalities of the system. The goal was to help the user run the electronic health record system smoothly and efficiently. We explored the Login, User Preferences, and Menu Navigation sections.

![Image](https://cdn-media-1.freecodecamp.org/images/oKxVj35LEJL651obqtONNBxpz67nzf6JgiTp)
_user-login-1_

I followed a video by my EHR mentor Harley Tuck called [LibreHealth EHR Introduction To Libre](https://www.youtube.com/watch?v=Fh0_NUVUn7k&t=62s). Even though it was only a few months old, things had changed. I used the website demo to capture the flow and images not covered in the video. I like the way Harley speaks — clear, articulate and precise. I tried to keep the tone of the User Guides conversational, as he did.

A doctor, also referred to as a provider, was already listed in the demo. I created a new facility — also referred to as a practice — to show the various methods of calendars and user preferences.

![Image](https://cdn-media-1.freecodecamp.org/images/B5kDyiFrn1qdc-G5lkkJ11LjVU-cZIuSJArI)
_nav-cal-two-day.jpeg_

#### Provider Orders

The second document was the [LibreHealth EHR Provider Orders](https://wiki.ehr.librehealth.io/LibreHealth_EHR_Provider_Orders) guide. I created a patient who was in need of a referral for an x-ray. Then I created the lab that would perform the x-ray so that we could send the orders.

I used the same doctor and facility that I had used for the previous User Guide. I also created three users. They were the Front Desk Receptionist, the LPN, and the Transcriber.

![Image](https://cdn-media-1.freecodecamp.org/images/BaPJ8TafBpasJLSkDtxYOoyxMChhOqpFJbIB)

#### Encounters or Visits

The third document was the [LibreHealth EHR Encounters](https://wiki.ehr.librehealth.io/LibreHealth_EHR_Encounters) guide. It was similar to the Provider Orders. However, instead of sending the patient to another provider, we administered medication on-site.

![Image](https://cdn-media-1.freecodecamp.org/images/2xdc3Vp3NimMwy2Lt6fymIJfkeiSgzfuWpGh)
_encounter-soap-med.jpeg_

This is where I learned a lot about healthcare codes. Understanding how the services, procedure and justification — for insurance billing — worked together to create the fees to be paid.

![Image](https://cdn-media-1.freecodecamp.org/images/4urStQjQ0u9LAooMVzozXyYcW4WmLznWD5SD)

Notice the two CTP4 codes:  
99203 is the initial patient visit at $25.  
96372 is the injection at no cost. The fee for the injection was covered in the medication — HCPCS code.

HCPCS J28000 is the medication in solution form at $27.

They all came together with the ICD10 Diagnosis code of M54.5 as low back pain.

#### Fee Sheets

The final document was [HOW TO: Create Fee Sheet List Categories](https://wiki.ehr.librehealth.io/HOW_TO:_Create_Fee_Sheet_List_Categories). This How To guide showed how the administrator would add a medication and the proper code to a Fee Sheet List. The information on the Fee Sheet List will be used for the billing of the visit on the Fee Sheet.

![Image](https://cdn-media-1.freecodecamp.org/images/4W1Ph3qzQsyIq3Mzb93kHHPH0SeTB7MY7YIX)

### Lessons Learned

#### Wiki

Wiki is wide open for contributors. This means that we had to be very careful on how we named our files and images. Otherwise you may end up using someone else’s images.

I solved this issue by prefixing the image by the document or section nick-name and then the actual image name. For instance: `orders-vapgar.jpg`.

![Image](https://cdn-media-1.freecodecamp.org/images/Foe2ug4u0mLkAVecnJaZZgxeWBxzGMm7SRKN)
_orders-vapgar.jpg_

Wiki markdown is not the same as the GitHub ReadME.md files. And it is not HTML. I had to make a code attitude adjustment, because I couldn’t quite style the way I normally would.

The `<`;p> tag didn’t work for me at all. So I tr`ied a` <br/> tag. No, that didn’t work either. H`owev`er, the <br> tag did work.

I couldn’t break columns up — as you would on a grid. However, `<d`i`v>,`<s`pan> and` <blockquote> solved my problem.

I could not use the `<img src=“section-image.jpg”` /> tag. Images are referred to as files. So instead, I had to `call [[Files:section-image`.jpg]].

My code to create a two row, two column image section looked like this:

`<div>`  
`<blockquote>`  
`‘’’Referral Transaction’’’: ‘Referral Date’ = ‘’’Procedure Order’’’: ‘Order Date’`  
`<br><br>`  
`<span>`  
`[[File:trans-refDate.jpg|500px]] [[File:trans-ordDate.jpg|500px]]</sp`an>  
<br><br>  
</blockquote>  
</div>

![Image](https://cdn-media-1.freecodecamp.org/images/-DEKVfggg2VUUFFjwBlc2IcjVYaZG2f2o9Ta)
_It worked!_

It was different for me, and took some time to adjust.

#### Healthcare

SOAP Notes is not about soap to wash with. It is the doctor and nurse notes that reflect the patient statements, and the doctor’s objective observations, assessment of the situation, and the plan of treatment for the patient.

![Image](https://cdn-media-1.freecodecamp.org/images/VUCQxSEpi1gaLb49gn-8oJVksdq3knLoAKnH)

Also, if it’s not on the SOAP Note Plan, Don’t Do It….

Work flow is very specific. Many of the staff members have restricted access to various areas of the patient information.

![Image](https://cdn-media-1.freecodecamp.org/images/I6f774Vry4gNZFGKCjeYtun89EeMtNELqncZ)
_order-access.jpg_

Billing, Medication, Fees and Justification codes are very stringent. I double-checked a lot with my mentor to make sure that my work was correct.

#### Documentation Styles

My first three documents carried a conversational tone. However, the last document was a Step-By-Step instructional style.

It wasn’t easy for me to place arrows and numbers in this one. Although it was the smallest document, it took more of my focus to get it how my mentor wanted it.

![Image](https://cdn-media-1.freecodecamp.org/images/HPO2TSowp3t4y5XxfSSEJDaWH3ws82FjazmN)

### Achievements

This summer was filled with many blessings and feelings of positive achievement for me.

I learned a lot about the health care practices, codes and work flows. I also learned a lot about technical and user documentation.

And I learned more than one way to create markdown documents.

#### Outreachy

This summer would not have gone this direction if I had not first been accepted to the Outreachy internship. It meant a lot to me that out of 45 candidates, I was considered to be someone who could help with their LibreHealth project.

That they were willing to pay me while I learned was even more awesome.

Then, they provided a travel stipend for the [New York Minute](https://medium.freecodecamp.org/how-i-escaped-to-nyc-and-celebrated-with-freecodecamp-on-my-outreachy-journey-22946d5af21e) of my Journey.

I recommend that every female tech student apply for the Outreachy Internship when the rounds open up.

#### freeCodeCamp

One of my duties as an Outreachy intern was to write every two weeks about my experiences. I really don’t consider myself a writer, so this seemed like it would be a daunting task.

As a freeCodeCamp camper, and an editor for freeCodeCamp on Medium, I had the perfect publishing platform. Fortunately, our founder [Quincy Larson](https://twitter.com/ossia) agreed.

Our executive editor, [Abigail Rennemeyer](https://twitter.com/abbeyrenn), has been the first to see my drafts — after my husband, [Alex Shortsleeve](https://twitter.com/alxsleeve). She has led me to write more and stop making 1-minute articles.

And, we have an awesome editing team who makes my final work look good. But the images are all on me…

#### Top Contributor Award

I was one of two hundred Campers who were awarded the Top Contributor badge from [freeCodeCamp](https://www.freecodecamp.org/konikodes). It was a great honor, but I wasn’t sure I could afford to travel to the other side of the mainland.

That’s when my LibreHealth mentor had me contact my Outreachy organizer. I was approved for the travel stipend! I arrived late Friday night and left early Sunday morning. But my Saturday was awesome!

I was able to meet some of my heroes and authors, a couple of my favorite moderators and the great people running study groups from all over the world. It was incredible. You can see the live stream [here](https://www.youtube.com/watch?v=u_4ZhwZmtes).

Honestly, I feel like I didn’t do much to deserve this. I just enjoyed editing some of my favorite authors’ articles, and answering the questions I thought I knew the answers to on the Forum. But I’m glad they didn’t realize I was just being nosy…

### Regrets and Hopes

I had hopes of learning more about the LibreHealth Radiology Information System. I began to work on two different documents, the User Guide and the Tech guide.

I wasn’t able to complete it due to technical difficulties. I am hoping that the next intern will be able to create it properly.

### Advice for future interns

As of September 19, applications for the Outreachy December 2018 to March 2019 internships are now open. You can apply [here](https://www.outreachy.org/apply/).

Find something that interests you. Something you can enjoy learning and that you can contribute to.

Follow the Outreachy guidelines. Your project will also have guidelines in place for you. You can make them both happen. When in doubt — such as deadline dates — ask your Outreachy Organizer.

Be patient. Not everyone is in your time zone. And everyone has a different schedule. So place your question out there, but realize that it may take a couple of days to get an answer.

Remember the holidays. In America, we have a lot of national holidays. And every state has it’s own days of celebration set aside. Family usually comes first for this. If you have a holiday coming up — where work, services and banks are shut down — let your team know ahead of time.

Be transparent. You will be working within an open source environment. Don’t Direct Message your mentor unless it is a question about your personal workload. The rest of the team and mentors need to see what everyone is doing.

Be friendly and play nice. Yes, this is a competition. But keep it a friendly competition.

### Appreciation

Special thanks to my mentors, Harley Tuck and Robby O’Connor. You both kept me on path, encouraged me to stretch myself, and applauded when I got it right.

And my thanks to you, my readers. Your feedback has been priceless. And the fact that you have stayed with me on my journey has really helped make my Summer a special season.

#### What now?

The Autumn season begins with the ending of a special editing project, and the beginning of working with a fellow camper on an interesting new library.

I will also return to my [freeCodeCamp](https://learn.freecodecamp.org/) curriculum and see if I can make real progress on my React-Redux challenges. And hopefully make something special to share with the world.

#### Previous Articles

* [How I beat the odds and became an Outreachy Intern](https://medium.freecodecamp.org/how-i-beat-the-odds-and-became-an-outreachy-intern-9a92f47cb44e)
* [My Outreachy internship begins today! Here’s what I’ve done and learned so far.](https://medium.freecodecamp.org/my-outreachy-internship-begins-today-heres-what-i-ve-done-and-learned-so-far-88fef9c18619)
* [The next steps on my Outreachy journey: Docker, big challenges, and small victories](https://medium.freecodecamp.org/the-next-steps-on-my-outreachy-journey-docker-big-challenges-and-small-victories-2c3a2dd2277a)
* [Every step brings something new on my Outreachy journey](https://medium.freecodecamp.org/every-step-brings-something-new-on-my-outreachy-journey-e7c0f7adf2ea)
* [Special Moments on my Outreachy Journey](https://medium.freecodecamp.org/special-moments-on-my-outreachy-journey-78db1ff11ef4)
* [How I’ve absorbed as much as I’m able on my Outreachy Journey](https://medium.freecodecamp.org/how-ive-absorbed-as-much-as-i-m-able-on-my-outreachy-journey-3e350c9e0362)
* [I made it to NYC and celebrated with freeCodeCamp on my Outreachy journey](https://medium.freecodecamp.org/how-i-escaped-to-nyc-and-celebrated-with-freecodecamp-on-my-outreachy-journey-22946d5af21e)
* [Sharing the Aloha Spirit with the Cloud](https://medium.freecodecamp.org/sharing-the-aloha-spirit-with-the-cloud-1c62e1a93cfb)

You can catch me on [GitHub](https://github.com/KoniKodes) or join me on [Twitter](https://twitter.com/konikodes). You can also visit my [website](https://www.konikodes.com).

