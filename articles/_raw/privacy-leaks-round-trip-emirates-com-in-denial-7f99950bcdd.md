---
title: 'Airline websites don’t care about your privacy follow-up: Emirates responds
  to my article with…'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-06T22:04:08.000Z'
originalURL: https://freecodecamp.org/news/privacy-leaks-round-trip-emirates-com-in-denial-7f99950bcdd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ETvXCCF1aTIj9Kial1iOhQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: privacy
  slug: privacy
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Konark Modi

  Yesterday, The Register wrote about my exposé on the privacy failings of airline
  websites.

  When I published my original article last Friday, Emirates had failed to respond
  to my request for comments. But Emirates did respond to The Reg...'
---

By Konark Modi

Yesterday, [The Register](https://www.theregister.co.uk/2018/03/05/emirates_dinged_for_slipshod_privacy_practices/) wrote about my exposé on [the privacy failings of airline websites](https://medium.freecodecamp.org/how-airlines-dont-care-about-your-privacy-case-study-emirates-com-6271b3b8474b).

When I published my original article last Friday, Emirates had failed to respond to my request for comments. But Emirates did respond to The Register, with the following statement:

![Image](https://cdn-media-1.freecodecamp.org/images/xl6tmP46uZY7rYTwUAjVKdiGO1iUe1Fi56-6)
_Comment from Emirates on theregister.co.uk_

Their statement is not only vague — it is factually incorrect. And I feel it’s my professional duty to call them out on this.

### **A breakdown of their statement, and how their logic breaks down when you really think about it**

#### Issue #1

First Emirates says, “_We can confirm that none of the security vulnerabilities highlighted will allow a breach (unauthorised access) of personal data on our website or mobile app.”_

How does Emirates define breach? Well, the [Cambridge Dictionary](https://dictionary.cambridge.org/us/dictionary/english/data-breach) defines a data breach like this:

> “An occasion when private information can be seen by people who should not be able to see it.”

In its [Privacy Policy](https://www.emirates.com/english/sitetools/privacy_policy.aspx#), Emirates highlights the importance of safeguarding Booking Reference information:

![Image](https://cdn-media-1.freecodecamp.org/images/DRUrRwOdF8KCiBlvSk0qWoJ-GbrVRaDmIFF8)
_Privacy policy highlighting risks of sharing Booking reference number._

**Update 8th March, 2018:** Another exhibit how Emirates seems to have forgotten to pay heed to their own advice _“keep your Booking Reference safe”_ and is **still** sending it to Google Analytics from mobile app, via **key:cd8** (unmasked). I have masked the fields in the picture to ensure Privacy.

![Image](https://cdn-media-1.freecodecamp.org/images/aCVUzJzm-yKZwhxuYTei-GlAfRKnfaD92Uhe)
_Sending PNR via field cd8 to Google-Analytics._

For any changes to an existing booking, a **Booking Reference number** and **Last name** is all that is required. There is no requirement to verify who initially made the booking and whether the person making the changes is authorised to do so or not.

Emirates.com and the Emirates mobile app version (6.1.0) both allow access to their Manage Booking section based **only** on these two data points. This a standard practice across airlines, and this is not the point of contention for the purposes of this article.

#### **But this is when it gets worrisome**

As of March 6th, 2018, Booking Reference number and Last Name, among many other data points, are still being sent to the third-parties implemented. Does Crazy Egg, Boxever, Coremetrics need Booking Reference Number and Last name for showing Heat Map of the page? I don’t think so.

This is the problem area — passing on user’s personal information to third parties who have absolutely no need for this information to render their services to Emirates _“for the purpose of improving the online browsing experience.”_

The importance of using HTTPS links has been established over and over again by everyone who is anyone in the field of Technology. HTTP links are not only vulnerable to Man-In-The-Middle attacks but can also suffer from injection of malicious data.

I am not sure how Emirates is confident enough to _“confirm that none of the security vulnerabilities highlighted in (Mr. Modi’s) article will allow a breach (unauthorized access) of personal data on our website or mobile app”_ when track.emirates.email still does not have any SSL. How do they plan to avoid Man-in-the-Middle attacks?

#### Issue #2

Emirates says, _“Whilst we do use a number of third party analytical tools on our sites for the purpose of improving the online browsing experience, we continually review how these are implemented.”_

I shared in the article how Passport information and contact details were earlier un-obfuscated on both website and Mobile app. While the website was fixed when I checked last in February 2018, the mobile app continues to be problematic in this area. This can happen only when there is a lack of communication between the Website and Mobile Development Team or they did not _“continually review the implementation”_ across all products.

Another question that begs to be answered is what are the parameters for reviewing the implementation of third parties. Unless the mandate is strictly to NOT leak any kind of user-information, the reviews could be of anything and would not have the slightest impact on the security and vulnerability of user information being freely passed on the third parties.

The last time this issue was highlighted to Emirates was in October 2017. In the 5 months that have passed since then these issues were not picked up by the review team. Maybe they are not as _“continuous”_ as Emirates claims them to be.

#### **Issue #3**

Emirates says, _“Customers can find out more about how we use personal data and how they can opt out by reading our privacy policy on emirates.com”_

![Image](https://cdn-media-1.freecodecamp.org/images/EyIuQm2i40qJNliIU6mixG5QD3EBvjyD1f27)
_Third-parties listed on Privacy Policy page._

![Image](https://cdn-media-1.freecodecamp.org/images/PANiBbCzm2U6CbxfznZjQwfuEteBTSYRcvrR)
_Third-parties actually present._

Upon a thorough review of [Emirates’ Privacy & Cookie Policy](https://www.emirates.com/english/sitetools/privacy_policy.aspx), these are the points to note:

1. It does not list **ALL** the implemented third-parties and the information being shared with them. Third parties like Boxever, ads-twitter.com, Coremetrics, Imigix, bing and many other that I had aggregated from their website are not even mentioned in their Privacy Policy.

2. Opt-out options available only mentions ways using about cookies, YourOnlineChoices. This means that not only the information provided in Privacy Policy is incomplete but also does not share any options to opt-out of services CrazyEgg, BoxEver, Coremetrics etc. The process is tedious and cumbersome.

3. The option to opt-out is biased based on the country of residence of the users. If you are a resident of EU you can use this link to opt-out. If you are a resident of USA this is the link to opt-out. But if you are a resident of any other region, I am sorry to break it to you that you have been short-changed.

![Image](https://cdn-media-1.freecodecamp.org/images/tDl-3ATYivfyZTuq-TXReJZ2lgtXVkefX2RI)

4. Opting-out of cookies is not going to have any impact on the data leaks highlighted in the article because the referrer is not being cleaned. Anybody with basic tech knowledge can confirm this.

### **In Short**

Even if the user somehow manages to opt-out of all the trackers using the methods listed and not listed, Emirates will still leak the Booking Reference and Last Name which is enough to access all other sensitive information because the implementation of these third-party services on Emirates.com is flawed.

Emirates needs to understand that once the information has been shared with third-parties, there is very little they can do to control how it is being used or might be used in the future, as they have themselves mentioned in their privacy policy.

**It is one thing for Emirates to think that these issues are not critical enough for them to take necessary actions to fix them. It’s an entirely different thing to say that the information shared in the article is _“not true”._**

I hope they fix these issues sooner rather than later.

Happy Hacking !

[- Konark Modi](https://twitter.com/konarkmodi)

Thanks for reading and sharing ! :)

If you liked this story, feel free to ??? a few times (Up to 50 times. Seriously).

_Credits: Special thanks to [Remi](https://twitter.com/Pythux) , [Pallavi](https://twitter.com/Pi_Modi) for reviewing this post too :)_

