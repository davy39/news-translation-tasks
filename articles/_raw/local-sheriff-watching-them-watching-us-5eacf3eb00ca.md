---
title: How to protect your information with Local Sheriff
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-01T18:12:00.000Z'
originalURL: https://freecodecamp.org/news/local-sheriff-watching-them-watching-us-5eacf3eb00ca
coverImage: https://cdn-media-1.freecodecamp.org/images/1*S5zyXVDrpVR24gnN9Vs0Tg.jpeg
tags:
- name: big data
  slug: big-data
- name: JavaScript
  slug: javascript
- name: privacy
  slug: privacy
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Konark Modi

  Watching them watching us


  What is a TellTale URL ?

  A URL is the most commonly tracked piece of information. The innocent choice to
  structure a URL based on page content can make it easier to learn a users’ browsing
  history, address, h...'
---

By Konark Modi

#### Watching them watching us

![Image](https://cdn-media-1.freecodecamp.org/images/bal86HLtSK3DaHmGSDs2koKIIaTAzzAp23wY)

### **What is a TellTale URL ?**

A URL is the most commonly tracked piece of information. The innocent choice to structure a URL based on page content can make it easier to learn a users’ browsing history, address, health information or more sensitive details. They contain sensitive information or can lead to a page which contains sensitive information.

We call such URLs as TellTaleURLs.

Let’s take a look at some examples of such URLs.

### **EXAMPLE #1:**

**Website**: _donate.mozilla.org (Fixed)_

After you have finished the payment process on _donate.mozilla.org_, you are redirected to a “thank you” page. If you look carefully at the URL shown in the below screenshot, it contains some private information like _email, country, amount, payment method._

![Image](https://cdn-media-1.freecodecamp.org/images/yFTLh7ZBCOWDlqold7QyIGe9LCTe02pOzgsT)
_PII in URL on donate.mozilla.org_

Now because this page loads some resources from third-parties and the URL is not sanitised, the same information is also shared with those third-parties via referrer and as a value inside payload sent to the third-parties.

![Image](https://cdn-media-1.freecodecamp.org/images/qQpzQGwGsPEJDchKDOrU8ZKXxM7ALe4QO5DI)
_URL with PII shared when fonts being loaded from Google Apis._

In this particular case, there were 7 third-parties with whom this information was shared.

Mozilla was prompt to fix these issues, more details can be found here: [_https://bugzilla.mozilla.org/show_bug.cgi?id=1516699_](https://bugzilla.mozilla.org/show_bug.cgi?id=1516699)

### EXAMPLE #2:

**Website**: trainline.eu, _JustFly.com (Last checked: Aug’18)_

Once you finish a purchase like train tickets / flight tickets, you receive an email which has a link to manage your booking. Most of the time, when you click on the link, you are shown the booking details - without having to enter any more details like booking code, username/password.

This means that the URL itself contains some token which is unique to the user and provides access to the users’ booking.

It so happens that these URLs are also shared with third-parties, giving these third-parties [highly sensitive data](https://medium.freecodecamp.org/how-airlines-dont-care-about-your-privacy-case-study-emirates-com-6271b3b8474b) and [access to your bookings](https://cliqz.com/en/magazine/lufthansa-data-leak-what-a-single-url-can-reveal-about-you).

![Image](https://cdn-media-1.freecodecamp.org/images/B6qA9nsCDe3WcNG8MseCRhq0lnG7I2gSG08K)
_JustFly.com leaking bookingID to 10 third-party domains_

![Image](https://cdn-media-1.freecodecamp.org/images/Sgg5O7vWB-Bh4E5NuAW3wQkr0hkQiUbQN2qI)
_trainline.eu sharing booking token with 17 third-party domains._

![Image](https://cdn-media-1.freecodecamp.org/images/dKN254bU1AgMCf21rWvWc0u6ge6iscwRKT5y)
_URL with token being shared via Ref and inside the payload._

### EXAMPLE #3:

**Website**: _foodora.de, grubhub.com (Last checked: Aug’18)_

One of the pre-requisites to order food online is entering the address where you want the food to be delivered.

Some popular food delivery websites, convert the address to fine latitude-longitude values and add them to the URL.

The URL is also shared with third-parties, potentially leaking where the user lives.

![Image](https://cdn-media-1.freecodecamp.org/images/zh6XHBxE7ubGBB8l3of-fFhYuNhvQodJGRAf)
_Foodora leaking address details to 15 third-party domains._

> To be clear, it’s not just these websites that suffer from such leaks. This problem exists everywhere - it’s a default situation, not a rarity. We’ve seen it with Lufthansa, Spotify, Flixbus, Emirates, and even with medical providers.

### Risks of TellTale URLs:

* Websites are carelessly leaking sensitive information to plethora of third-parties.
* Most often without users’ consent.
* More dangerously: Most websites are not aware of these leaks while implementing third-party services.

### Are these problems hard to fix?

As a Software Engineer who has worked for some of the largest eCommerce companies, I understand the need to use third party services for optimising and enhancing not only the Digital Product but also how users interact with the product.

It is not the usage of third party services that is of concern in this case but the implementation of these services. Owners should always have the control of their website and what the website shares with third party services.

It is this control that needs to be exercised to limit the leakage of User information.

It is not a mammoth task, it is just a matter of commitment to preserving the basic right to privacy.

For example:

1. Private pages should have [noindex meta tags](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta).
2. Limit the presence of third-party services on private pages.
3. [Referrer-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy) on pages with sensitive data.
4. Implement CSP and SRI. Even with a huge footprint of third-party services [CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP), [SRI](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) are not enabled on majority of the websites.

### Introducing Local Sheriff:

Given that such information leakage is dangerous to both users and the organisations, then why is it a wide-spread problem?

One big reason that these issues exist is lack of awareness.

A good starting point for websites is to see what information is being leaked or detect presence of TellTaleURLs.

But in order to find out if the same is happening with the websites you maintain or visit, you need to learn some tools to inspect network traffic, understand first-party — third-party relationship and then make sure you have these tools open during the transaction process.

To help bridge this gap, we wanted to build a tool with the following guidelines:

* Easy to install.
* Monitors and stores all data being exchanged between websites and third-parties — Locally on the user machine.
* Helps identify the users which companies are tracking them on the internet.
* Interface to search information being leaked to third-parties.

Given the above guidelines, browser extension seemed like a reasonable choice. After you install Local-Sheriff, in the background:

1. Using the WebRequest API, it monitors interaction between first-party and third-party.
2. Classifies what URL is first-party and third-party.
3. Ships with a copy of database from [WhoTracksMe](https://whotracks.me/). To map which domain belongs to which company.

4. Provides an interface you can search for values that you think are private to you and see which websites leak it to which third-parties. Eg: name, email, address, date of birth, cookie etc.

### Revisiting EXAMPLE #1

**Website:** _donate.mozilla.org_

* The user has Local-Sheriff installed and donates to mozilla.org.

![Image](https://cdn-media-1.freecodecamp.org/images/xrealtqpe6MuxuFVU6nqyaWR3Z6FZm-J4uwv)
_PII in URL on donate.mozilla.org_

* Clicks on the icon to open search interface.

![Image](https://cdn-media-1.freecodecamp.org/images/oQTbZxMUMeO0l83pyyvQca-EWggpcB1tMn7Z)
_Local sheriff icon._

* Enters emailID used on the website donate.mozilla.org.

![Image](https://cdn-media-1.freecodecamp.org/images/XU1a1DfPQyJLtvGYM52swvVEyVD5Xj1FH91R)
_Search interface Local-Sheriff_

It can be seen that email address used at the time of donation was shared with **~7 third-party domains.**

You can try it yourselves by installing it:

* **Firefox:** [https://addons.mozilla.org/de/firefox/addon/local-sheriff/](https://addons.mozilla.org/de/firefox/addon/local-sheriff/)
* **Chrome:** [https://chrome.google.com/webstore/detail/local-sheriff/ckmkiloofgfalfdhcfdllaaacpjjejeg](https://chrome.google.com/webstore/detail/local-sheriff/ckmkiloofgfalfdhcfdllaaacpjjejeg)

**Resources:**

* **More details**: [_https://www.ghacks.net/2018/08/12/local-sheriff-reveals-if-sites-leak-personal-information-with-third-parties/_](https://www.ghacks.net/2018/08/12/local-sheriff-reveals-if-sites-leak-personal-information-with-third-parties/)
* **Source Code**: [_https://github.com/cliqz-oss/local-sheriff_](https://github.com/cliqz-oss/local-sheriff)
* **Conferences:** [_Defcon 26 Demo Labs_](https://www.defcon.org/html/defcon-26/dc-26-demolabs.html) _, [FOSDEM 2019](https://fosdem.org/2019/schedule/event/web_extensions_exposing_privacy_leaks/)_
* **Code:** [https://github.com/cliqz-oss/local-sheriff](https://github.com/cliqz-oss/local-sheriff)
* **Chrome store:** [https://chrome.google.com/webstore/detail/local-sheriff/ckmkiloofgfalfdhcfdllaaacpjjejeg](https://chrome.google.com/webstore/detail/local-sheriff/ckmkiloofgfalfdhcfdllaaacpjjejeg)

Thanks for reading and sharing ! :)

If you liked this story, feel free to ??? a few times (Up to 50 times. Seriously).

Happy Hacking !

[- Konark Modi](https://twitter.com/konarkmodi)

**_Credits:_**

* _Special thanks to [Remi](https://twitter.com/Pythux) , [Pallavi](https://twitter.com/Pi_Modi) for reviewing this post :)_
* _Title “Watching them watching us “ comes from a joint talk between Local Sheriff and [Trackula](https://trackula.org/en/) at FOSDEM 2019._

