---
title: 'Updated: Airline websites don’t care about your privacy: a case study on Emirates.com'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-03T00:56:18.000Z'
originalURL: https://freecodecamp.org/news/how-airlines-dont-care-about-your-privacy-case-study-emirates-com-6271b3b8474b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*61m9JVlYvpvORj2IUlp-4w.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Data Science
  slug: data-science
- name: Facebook
  slug: facebook
- name: privacy
  slug: privacy
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Konark Modi

  I asked my wife if it is alright if her Date of Birth is known to a stranger. Only
  if they send me a birthday gift, she joked. What about your passport number? She
  lowered the book she was reading. I now had her attention.

  Now imagine ...'
---

By Konark Modi

I asked my wife if it is alright if her Date of Birth is known to a stranger. Only if they send me a birthday gift, she joked. What about your passport number? She lowered the book she was reading. I now had her attention.

Now imagine this, I said “You try to check-in for your flight online, and see the error message — This booking does not exist. You try again, this surely is a mistake. Nope, still the same error message. The call center person repeats the same words. This has to be a mistake! You check your email, and there it is — staring back at you — email confirmation of cancellation. But you are sure you didn’t do it.” Whodunnit?

This is not a far-fetched scenario from a Sci-fi book, [this really happened](https://media.ccc.de/v/33c3-7964-where_in_the_world_is_carmen_sandiego).

An organisation with a primary Digital Product that lacks even the basic data security practices is living in a utopian world where people leave their safe open and never expect a burglar to walk in.

In the wake of full disclosure, sometime last year while booking travel for my family, I stumbled across a few data-security practices that, as a Data Security advocate, made me extremely worried. When I voiced my concerns to Emirates team, this conversation took place -

![Image](https://cdn-media-1.freecodecamp.org/images/J98i59bZQiaHOsLcEjwt8BwljNL7iZvwi2Vt)
_Conversation with Emirates support._

For a layman, when you book your flight through Emirates, Domestic or International, there are approximately [300 data points](https://pastebin.com/cAcXx2A4) related to your booking.

The moment you click on manage preferences to select a seat or meal for your trip or to Check-in to your flight, your Booking ID and Last name is passed on to approximately 14 different third-party trackers like Crazy egg, Boxever, Coremetrics, Google, and Facebook among others.

### **Details**

After I completed the booking on Emirates, I received an e-mail confirmation titled: Booking Confirmation — Booking Number.

![Image](https://cdn-media-1.freecodecamp.org/images/8-8XXdTlMKTutKcdyriWK1-UD4YgeZlyVGJL)
_Booking confirmation email._

The body of the email contained Manage booking. I proceeded to select seats and meal by clicking on the Manage Booking button and reached the Manage Preference page. This was pretty straightforward.

![Image](https://cdn-media-1.freecodecamp.org/images/U2fdc81FxC3yRXi5ooiz2GLDMtJOS8Cks5nj)
_Manage booking link in email._

While as a user, I saw the normal behaviour of clicking a link and reaching the landing page “Manage Preferences”, in the background a redirection chain took place.

![Image](https://cdn-media-1.freecodecamp.org/images/TJgXmvJ95h6sw3noBhTlGdU5OEVB7t9ZnKAQ)
_Redirection chain before reaching the landing page._

While Manage Booking link was supposed to be exclusive to me (the user and the website), this link was also shared with numerous third party trackers implemented by Emirates on their webpages.

![Image](https://cdn-media-1.freecodecamp.org/images/UfY2o2W4fksf1pZbNRZLXMNFjBqL6oLzQ5kU)
_Manage booking page._

The cherry on the cake was the HTTP link that leads to the Manage Preferences page. The insecureness of HTTP has been [talked](https://medium.com/@pallavimodi/http-https-what-is-the-difference-3a97fe2f7fd8) about over and over again, especially when it comes to maintaining the authenticity of the content and protection against interlopers. But in short, HTTP links are a Data Privacy nightmare. So, not only was Emirates passing on user information to the self-implemented third party trackers, but also allowing network adversaries to have access to the supposedly “Private” page.

![Image](https://cdn-media-1.freecodecamp.org/images/GUDfElLiP1iynwZ8AL84GTAMC27HCh8HMZqB)
_[http://track.emirates.email/track/click/30705682/www.emirates.com?p=eMSwicCI6IntcInVcIjozM....(REDACTED)](http://track.emirates.email/track/click/30705682/www.emirates.com?p=eMSwicCI6IntcInVcIjozM....(REACTED)" rel="noopener" target="_blank" title=")_

### **What kind of information can third-parties access?**

Links mentioned in (1) and (2) are currently being sent to the third-parties.

![Image](https://cdn-media-1.freecodecamp.org/images/blQnYPaptvr2V9k8ruJXyJGRaAmdhhrrpIgp)

Following fields take home the URL, which gives access to booking details.

![Image](https://cdn-media-1.freecodecamp.org/images/S5Ah2kCOMZJznXUtFly-KRt1VltJgYrJl37d)
_Fields which take home the private url._

![Image](https://cdn-media-1.freecodecamp.org/images/CcJhlcel0E2cjrlD7WtgacQvlv4FF-4YGvbt)
_Sending url in key `dr` used by Google Analytics._

![Image](https://cdn-media-1.freecodecamp.org/images/DbuxeC1c16zWXNAguVpioFAOrfXXq0F9cdVE)

Anyone who has access to these links can not only read but also edit the information that I as a user can.

For example, they can now -

1. Change or Cancel flight
2. Change seat or meal preference
3. Add more products to the booking
4. Change or add Passport Information
5. Change or add Frequent Flyer Information, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/MJWQLCMrz6SWu2nMTuq3fm7swGiAfxl3hOO0)

![Image](https://cdn-media-1.freecodecamp.org/images/-NJQfaC6PV7DtifczwFIsA0ZDRRksu-EfopD)

![Image](https://cdn-media-1.freecodecamp.org/images/vxvDjZC9XrDCMiaWBG-WWrs4hhWzRapLS2by)
_Modify booking._

**Exhibit of editable personal information on this page:**

**a. Full Name:**

![Image](https://cdn-media-1.freecodecamp.org/images/B3TaqII7bAoKkofhVk21DY040GlpuBHQ-wQP)
_Name._

**b. Skywards number**

![Image](https://cdn-media-1.freecodecamp.org/images/Pw9KljVJmGJOZCbxPjC4R4XFYy2Id4EdJsjw)
_Skywards number_

**c. Email ID / Telephone number:**

![Image](https://cdn-media-1.freecodecamp.org/images/IXHrwJuTbuoulITQC4tADyQKdE79YKYR62DV)
_Read / Change personal information_

**d. Amount Paid, fare breakup.**

![Image](https://cdn-media-1.freecodecamp.org/images/F76wEiebLxzeqNvF1mrtmweKg9z4huZqJsby)
_Amount paid, form of payment, fare break-up._

**e. Passport details, Nationality, Date of birth, Gender**

![Image](https://cdn-media-1.freecodecamp.org/images/0zHmM1qv8K4ZqfE6fbG4MRnAfGgKrwAEK1ms)
_Passport details, DOB, Expiry, Gender, Nationality._

_Note:_ In October 2017, fields such as Passport Number, Email Id and Telephone number were shown to be masked on the User Interface but were not obfuscated in source code. The web app has been revamped since then and these fields are now obfuscated.

![Image](https://cdn-media-1.freecodecamp.org/images/8EbqAkIVUoJKvI6RnBvGSlDOG1hll183ivzO)
_Masked fields in plain text. (October 2017)_

I decided to take a peek into the mobile app and see if the past catches up with the present, and lo and behold there it was in its full glory — Passport Number, Email ID and Telephone number in plain text. What was obfuscated on the web app was easy to access on the mobile app.

![Image](https://cdn-media-1.freecodecamp.org/images/FOZAgyc668QqoBD3zh17PB6fOdh0ir4oSCD8)
_Passport details in plain text on mobile API._

**Now, what is wrong with this?**

This issue is not only limited to Emirates, a lot of airlines like Lufthansa, KLM (last checked on October 2017) suffer from the same issues.

Every website uses third party trackers for improving their product and provide better web-usage experience. Data leaks are often considered collateral-damage and sometimes not even considered at all while implementation of such trackers.

Most of these third-parties are present on a lot of other websites and use long term identifiers like cookies etc to track users across domains. Now because one of the websites, in this case Emirates, leaks private information, these companies now potentially can not only link the user’s activity across web, but also identify who the user is.

The questions that need answering by Emirates (and others) are -

1. Why was my booking information passed on to these third parties without my explicit consent.
2. Why do these third parties need to receive this information?
3. Is Emirates even aware that sensitive user information is being leaked to these third parties?
4. Who are these third parties?
5. What are they doing with user information?

### **Reporting it to Emirates**

In the wake of responsible behaviour, on discovering these serious security flaws that violate user-data privacy, I decided to flag them to Emirates through Twitter DM in October 2017. Please note that I could not find a dedicated channel for reporting security bugs on Emirates website.

The Social Media Team immediately responded to my Twitter DM with a canned response but I was not ready to give up hope. I also wrote an email to the Product Manager highlighting the security flaws. I was met with a deafening silence.

As of today (2018–03–03) lot of these issues still persists.

This is a serious violation of privacy, there is no point during the whole booking process, where I agreed upon sharing any of this personal information with any of these websites.

The [privacy policy](https://www.emirates.com/english/sitetools/privacy_policy.aspx) of Emirates itself is not very clear. It does [mention some of the of these services](https://www.emirates.com/english/sitetools/cookie-policy.aspx), but not all or the what data being shared with them.

#### **Can I not opt-out?**

Not an option. Unfortunately, I could not find a way to opt-out of this system provided by Emirates. I finally had to fall back on using privacy preserving browser extensions.

#### **Can this not be fixed by Emirates?**

As a Software Engineer who has worked for the some of the largest eCommerce companies, I understand the need to use third party services for optimising and enhancing not only the Digital Product but also how user interacts with the product.

It is not the usage of third party services that is of concern here in this case but the implementation of these services. Emirates has the control of their website and what the website shares with third party services. It is this control that needs to be exercised to limit the leakage of User information.

It is not a mammoth task, it is just a matter of commitment to preserving the basic right to privacy.

For example:

1. Private pages should have [noindex meta tags](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta).
2. Limit the presence of third-party services on private pages.
3. [Referrer-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy) on pages with sensitive data.
4. Implement CSP and SRI. Even with a huge footprint of third-party services [CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP), [SRI](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) are not enabled on Emirates.com
5. User needs to be informed when sensitive information like passport, contact details etc. is updated, edited, or deleted.
6. Domain for sending e-mails : track.emirates.email, should have a valid certificate. [https://track.emirates.email/](https://track.emirates.email/)

![Image](https://cdn-media-1.freecodecamp.org/images/n04rAIAp6Z1zBmHuWz4symTvtvVt7W-nTKOP)

If you are interested in reading more about the presence of trackers on your favourite websites, I highly recommend checking out [WhoTracksMe](https://whotracks.me/).

**_Updates:_**

**_- March 6th, 2018:_**

_Emirates responded with a standard statement._

_Excerpt: “**The depiction in Mr Modi’s article as to what data is being shared, or customer choice in ‘opting out’ is inaccurate.”**_

_Here is my response: [Privacy leaks round-trip: Emirates.com in denial](https://medium.com/@konarkmodi/privacy-leaks-round-trip-emirates-com-in-denial-7f99950bcdd)_

Happy Hacking!

- [Konark Modi](https://twitter.com/konarkmodi)

Thanks for reading and sharing ! :)

If you liked this story, feel free to ??? a few times (Up to 50 times. Seriously).

_Credits: Special thanks to [Remi](https://twitter.com/Pythux) ,[Pallavi](https://twitter.com/Pi_Modi) for reviewing the post._

