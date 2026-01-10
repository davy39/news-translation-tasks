---
title: GDPR terminology in plain English
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-23T07:57:35.000Z'
originalURL: https://freecodecamp.org/news/gdpr-terminology-in-plain-english-6087535e6adf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6hCZUnZq19I_UvHv4sIp9w.jpeg
tags:
- name: data
  slug: data
- name: '#gdpr'
  slug: gdpr
- name: privacy
  slug: privacy
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Alex Ewerlöf

  My team builds the technologies for some of the highest traffic newsrooms in Sweden
  and Norway. Part of the revenue comes from selling ads. Ads sell best when personalised,
  and for personalization you need data. Internet’s default bus...'
---

By Alex Ewerlöf

My team builds the technologies for some of the highest traffic newsrooms in Sweden and Norway. Part of the revenue comes from selling ads. Ads sell best when personalised, and for personalization you need data. Internet’s default business model is based on ads. GDPR has big implications for online businesses like newsrooms.

But here’s the interesting part — the General Data Protection Regulation (GDPR) puts restrictions on what data can be gathered, how it can be used, and for how long it can be stored.

This post is about demystifying the core GDPR terms so everyone can understand this interesting topic. If you are European or have European users, you need to understand GDPR.

> TL;DR; this is a huge shift in how personal data is gathered from “by default” to “opt-in”. Plus some other perks.

Here is a video that sums it up at a basic level:

Before we start, a quick disclaimer: I don’t represent my current/previous employers on my personal blog. The information provided here is purely based on my own research, and doesn’t necessarily reflect my company’s policies, strategy or implementation of GDPR.

### A bit of background

GDPR came into effect on May 25. Despite making developers’ and marketers’ lives harder, it’s actually a very sweet deal for the end users. GDPR prevents the companies from gathering information they don’t need to (strictly speaking).

Despite starting with the word ‘General’, GDPR is actually an European Union (EU) law that [applies to](https://www.lexology.com/library/detail.aspx?g=70046340-607b-4620-a680-6b6a0cefaf47):

1. Companies that are based in the EU
2. Companies that gather personal data from European citizens.

Maybe that ‘General’ is good, because a huge part of the internet is European!

![Image](https://cdn-media-1.freecodecamp.org/images/1*jS0wmtrioU6pGFsVO6sS7g.gif)
_Global internet usage during 24 hours ([wikipedia](https://en.wikipedia.org/wiki/Global_Internet_usage" rel="noopener" target="_blank" title="))_

The word ‘Regulation’ in GDPR means that it must be applied in its entirety across the EU.

In the long run, this leads to **privacy by design**. This is a principle that calls for the inclusion of data protection from the start of designing the systems, rather than as an afterthought.

### Common terminology

Here’s a list of the most common GDPR terms:

* A **Data Subject** is a person (such as you and me) whose personal data is processed by a data controller (such as a company or service we use).
* A **Data Controller** is an organisation that collects data from EU residents. It determines the purposes, conditions and means of processing the personal data.
* The entity that does the actual data processing is called a **Data Processor** — an example might be a cloud service provider.
* **Processing** involves any operation performed on personal data, whether or not by automated means. This includes collection, use, recording, feeding it to machine learning algorithms (read [how ML is affected by GDPR](https://www.oreilly.com/ideas/how-will-the-gdpr-impact-machine-learning)), and so on.

### GDPR for the users

Your **personal data** is any information that can be used to directly or indirectly identify you_._ For example: your name, home address, photo, email address, bank details, posts on social networking websites, medical information, or a computer or mobile IP address.

This data is usually used for **profiling**, in which automated processes evaluate, analyse, or predict your behaviour. As an example, knowing your age means you’ll be exposed to ads that are targeted to your age group. This is also true about data that you’re not explicitly giving to a company, like your IP address, which will be used to guess your location.

Now that GDPR is in effect, companies have limitations on what personal data they can gather and how long they can store it. They should justify why they need it.

#### When the companies NEED user consent

The data controller (company) cannot just go and gather user data. They have to first ask for your permission or consent.

The consent must be explicit for data collected and for the purposes the data is used. The consent is freely given (if you say ‘no’, the company should still serve you as well as possible without your data). The consent should not be regarded as freely given if the data subject has no genuine or free choice or is unable to refuse or withdraw consent without detriment. The consent should be specific and explicit about what data is gathered and how it is processed. The user have the right **to withdraw his or her consent at any time** but more importantly **it shall be as easy to withdraw as to give consent.**

Companies can no longer force you to tick a checkbox that says “I accept all terms and conditions and privacy policies”. That is why you were getting those emails from many websites informing you about their policies before the May 25th deadline.

The area of GDPR consent has a number of implications for businesses who record calls as a matter of practice. The typical “calls are recorded for training and security purposes” warnings will no longer be sufficient to gain assumed consent to record calls.

#### When the companies DON’T need user consent

There must be a reasonable legal basis for gathering an exact piece of data. According to the [GDPR’s site](https://www.gdpreu.org/the-regulation/key-concepts/legitimate-interest/), these can be when:

* Processing is necessary for the fulfillment of a contract to which the data subject is party or to take steps at the request of the data subject prior to entering into a contract.
* Processing is necessary for compliance with a legal obligation to which the controller is subject.
* Processing is necessary to protect the vital interests of the data subject or of another natural person.
* Processing is necessary for the performance of a task carried out in the public interest or in the exercise of official authority vested in the controller.
* Processing is necessary for the purposes of the legitimate interests pursued by the controller or by a third party unless such interests are overridden by the interests or [fundamental rights](https://en.wikipedia.org/wiki/Charter_of_Fundamental_Rights_of_the_European_Union) and freedoms of the data subject, which require protection of personal data, in particular if the data subject is a child.

The most important benefit of GDPR is that it [gives controls](https://gdpr-info.eu/chapter-3/) to the users to:

1. Erase their data whenever they like (also known as the [Right to be Forgotten](https://en.wikipedia.org/wiki/Right_to_be_forgotten)). **Data Erasure** requests don’t stop at the data controller. If third party data processors are involved, they too have to stop processing the data and erase it. I’m guessing there’ll be a de facto standard API for that, but so far it’s more ad-hoc and depends on how services talk to each other. I’m sure in the future there’ll be services where you give them your personal info and they’ll check thousands of online services to give you an aggregated report of which sites have your information. The companies should provide a way to query if they have data for a particular user (without requiring registration)_._ Trivia: this is essentially in contradiction with how Blockchain works! Read more about [the implications of GDPR for Blockchain here](https://medium.com/@alexewerlof/gdpr-for-blockchain-f73744b9be34).
2. Own their data! The data subjects (users) can download and see their data and how it is processed. Furthermore, the data controller has to inform the data subject on details about the processing, such as the purposes of the processing, with whom the data is shared, and how it acquired the data. This is called **right of access** or **subject access right**. Personal data [cannot be transferred to countries outside the European Union](http://ec.europa.eu/justice/data-protection/international-transfers/index_en.htm) unless they guarantee the same level of data protection.
3. Move their data to competitors. This is good for competition and eventually the users win. The data must be provided by the controller in a structured and commonly used standard electronic format. No more lock-in! This is known as **data Portability**. This will probably open up a whole new business segment for converting data formats from one controller to another controller.
4. Update/correct their data. The data subjects have the right to ask the data controllers to immediately correct (public or private) data that is invalid.

I personally find the **data breach** announcement amazing.

The data controller is under a legal obligation to notify the relevant supervisory authority of any data breach without undue delay, unless the breach is likely to result in a risk to the rights and freedoms of the individuals affected.

Individuals have to be notified if an adverse impact is determined. There is a maximum of 72 hours after becoming aware of the data breach to make the report. In addition, the data processor will have to notify the data controller without undue delay after becoming aware of a personal data breach.

Do you remember [when Yahoo kept its breach secret for two years](https://www.washingtonpost.com/news/the-switch/wp/2016/11/10/yahoo-discovered-hack-leading-to-major-data-breach-two-years-before-it-was-disclosed/?noredirect=on&utm_term=.4782fea5e3e5)? Well, not anymore!

### GDPR for the governments

Since GDPR is quite a big thing, governments are involved to protect their citizens and enforce the regulations. There are two terms to understand:

* National **Data Protection Authorities** ([DPA](https://www.whitecase.com/publications/article/chapter-14-data-protection-authorities-unlocking-eu-general-data-protection)) are appointed by each EU country to implement and enforce data protection law, and to offer guidance. **Supervisory Authority** (SA) [is another name](https://www.i-scoop.eu/supervisory-authorities-consistency-and-data-protection-authorities-dpas/#What_is_a_Data_Protection_Authority_or_DPA_in_the_scope_of_the_GDPR) for DPO. As set out in Chapter 16, DPAs have significant enforcement powers, including the ability to issue substantial fines. They are also the place to go to in case of a violation of data protection legislation (in the scope of the GDPR for EU citizens) and for advice and specific questions and/or assistance from the perspective of organisations.
* A **Data Protection Officer** ([DPO](https://www.whitecase.com/publications/article/chapter-12-impact-assessments-dpos-and-codes-conduct-unlocking-eu-general-data)) is a an employee of the data controller (company) who is formally tasked with ensuring that an organisation is aware of, and complies with, its data protection responsibilities. More about this in the next section.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q6HO-CQ7tHOUAd0s9tG6xA.png)
_DPA &amp; DPO_

Each EU member has a main establishment where key decisions about data processing are made.

### GDPR for the companies

The upper fine limit for contravening GDPR is pretty expensive: up to €20 million, or up to 4% of the annual worldwide turnover of the preceding financial year… whichever is _higher_!

Companies that gather data have a responsibility and the liability to implement and demonstrate that they comply with GDPR. This is called **compliance**.

The companies are supposed to keep a log of who accessed what information for when the authorities ask for an audit. Records of processing activities must be maintained, that include purposes of the processing, categories involved and envisaged time limits.

The records must be made available to the supervisory authority on request. The interesting part is that even if the actual processing happens by another company (a data processor on behalf of the data controller), it is still the company that gathers the data that bears the main responsibility.

This whole new range of requirements is complicated enough to create a new job title: data protection officer (DPO)! This is an enterprise security leadership role responsible for overseeing data protection strategy and implementation to ensure compliance.

They also:

* Educate the company and employees on important compliance requirements
* Are the point of contact between the company and supervisory authorities
* Monitor and provide advice on data protection efforts across the company
* Keep tabs on all data processing activities at the company, including the purpose of all processing activities, which must be made public on request
* Answer inquiries from users regarding how their data is being used, data erasure right and queries regarding what measures the company has put in place to protect their personal information
* Identify and reduce the privacy risks of entities by analysing the personal data that are processed and the policies in place to protect the data, which is called **Data Privacy Impact Assessment**. The GDPR [mandates a DPIA](https://www.itgovernance.co.uk/privacy-impact-assessment-pia) be conducted where data processing is likely to result in a high risk to the rights and freedoms of natural persons.

The DPO must have a support team and will also be responsible for continuing professional development to be independent of the organization that employs them, effectively as a “mini-regulator.”

If a business has multiple establishments in the EU, it will have a single supervisory authority as its lead authority, based on where the main data processing activities take place.

### GDPR for the developers

Since GDPR enforces **privacy by design**, it affects software architecture and its implementation. For example, we can no more keep logs of sensitive information (as mentioned before, IP addresses are considered personal information). This makes tracing bugs a bit harder.

Privacy settings must therefore be set at a high level by default. So we have to make sure checkboxes that expose personal data are not ticked by default.

If the Cloud is used for data storage, only the data owner, not the cloud service, should hold the decryption keys.

We cannot store data for longer than necessary. Database columns should have a **data retention deadline** which specifies when the data should be deleted.

Personally identifiable information should be **pseudonymised** in a way that it can no longer be linked (or ‘attributed’) to a single data subject without the use of additional data.

Read more about [the pseudonymization in techniques in my newer post](https://medium.com/@alexewerlof/gdpr-pseudonymization-techniques-62f7b3b46a56).

### Exceptions to GDPR

What good is a law if it is not meant to be broken? Don’t get too excited about your rights because the following cases are not covered by the regulation:

* Lawful interception, national security, the army, the police, justice
* Statistical and scientific analysis for research
* Deceased persons are subject to national legislation
* There is a dedicated law on employer-employee relationships. The GDPR was developed with a focus on social networks and cloud providers, but did not consider enough requirements for handling employee data.
* Processing of personal data by a natural person in the course of a purely personal or household activity

### Acknowledgement

Thanks to my colleague [Ioana Norgen](https://www.linkedin.com/in/ioanadodu/) for proof-reading this post before publishing. Any possible errors are still mine.

### Sources

* A [glossary](https://www.eugdpr.org/glossary-of-terms.html) of GDPR terms
* [Pseudoanonymization techniques](https://gdpr.report/news/2017/11/07/data-masking-anonymisation-pseudonymisation/)
* [Wikipedia](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation)
* [Data Protection Officer](https://digitalguardian.com/blog/what-data-protection-officer-dpo-learn-about-new-role-required-gdpr-compliance)

### Interesting reading

* [ePrivacy](https://en.wikipedia.org/wiki/EPrivacy_Regulation_(European_Union)), a set of related regulations that are also enforced at the same time as GDPR. It targets any business that provides any form of online communication service, uses online tracking technologies, or engages in electronic direct marketing (eg. telecom operators and online communication services like Skype and WhatsApp). Its most important aspect is protection against spam SMS/email and marketing calls.
* An [excellent guide to GDPR for developers](https://techblog.bozho.net/gdpr-practical-guide-developers/) and some [nice slides](https://techblog.bozho.net/gdpr-developers-presentation/)
* Belitsoft has made [a great checklist for businesses about GDPR](https://belitsoft.com/gdpr-compliance-checklist) although not all items in the checklist are a requirement by GDPR and some like 2 factor authentication are more of a best practice.
* [How GDPR affects cookies used for tracking](https://techblog.bozho.net/tracking-cookies-gdpr/)
* The data protection reform package also includes [a separate Data Protection Directive](http://eur-lex.europa.eu/eli/dir/2016/680/oj/eng) for the police and criminal justice sector that provides rules on personal data exchanges at national, European, and international levels.
* [Facebook and Google hit with $8.8 billion in lawsuits on day one of GDPR](https://www.theverge.com/2018/5/25/17393766/facebook-google-gdpr-lawsuit-max-schrems-europe)
* [Privacy by design](https://en.wikipedia.org/wiki/Privacy_by_design)

> The bottom line is: GDPR is an obvious right. Europe pioneered its establishment but this should be a global right. Talk about it with your friends, colleagues and law makers if you want to enjoy the same protection and choice as Europeans.

If you liked this, you may enjoy: [programming is the best job ever](https://medium.com/@alexewerlof/what-s-cool-about-being-a-programmer-5a1e58efeee6) and [how do I keep up with technology](https://medium.com/@alexewerlof/how-i-learn-new-tech-cb79db19c818).

