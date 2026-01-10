---
title: The Essential Launch Checklist for Web Apps and Mobile Apps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-21T03:40:25.000Z'
originalURL: https://freecodecamp.org/news/the-essential-launch-checklist-for-web-apps-and-mobile-apps-a0d52c6014b5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*e7O7A5rM79ng6b8Dc3EbEg.jpeg
tags:
- name: mobile app development
  slug: mobile-app-development
- name: SEO
  slug: seo
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ben Cheng

  This is a simple launch checklist for web and mobile apps that I’ve prepared for
  product and project managers to quickly test performance of their apps. It also
  includes a list of commonly overlooked simple mobile app tests to confirm th...'
---

By Ben Cheng

This is a simple launch checklist for web and mobile apps that I’ve prepared for product and project managers to quickly test performance of their apps. It also includes a list of commonly overlooked simple mobile app tests to confirm that the app behaves as expected.

Product managers on the client side can use the tools provided to see performance results when working with digital agencies or dev shops.

### Web Applications

For web applications, the launch check list should cover the following:

1. Performance: Pass Google Page Speed Insights Test
2. Security
3. Broken Links
4. Compatibility
5. SEO / Social
6. Nice to Haves

### Performance: Pass Google Page Speed Insights Test

![Image](https://cdn-media-1.freecodecamp.org/images/e3ZdwpSpZ51SExdgGqJKFgq72yV6jRHMm653)
_Note that Google will make [page speed a factor in mobile search ranking](https://techcrunch.com/2018/01/17/google-will-make-page-speed-a-factor-in-mobile-search-ranking-starting-in-july/" rel="noopener" target="_blank" title=") starting July 2018_

1. Plug the site into Google [PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/) to see your results
2. If the site requires login / credentials, login to the site first and check the performance with [Chrome Page Speed Insights Extension](https://chrome.google.com/webstore/detail/pagespeed-insights-with-p/lanlbpjbalfkflkhegagflkgcfklnbnh)
3. Another useful tool is [Pass GTMetrix Analysis](https://gtmetrix.com/)

**Why:** Statistics have consistently shown that a few seconds in load time makes a huge difference in retention. [53% of site visits are abandoned if a site takes more than 3 seconds to load](https://www.thinkwithgoogle.com/data-gallery/detail/mobile-site-abandonment-three-second-load/). Having a faster site helps retain visitors and increases engagement with your site. This in turn reduces your bounce rate and helps your SEO.

### Security

![Image](https://cdn-media-1.freecodecamp.org/images/TafLFoWB04CtnkMX1U3Xy7QtP0IAVnsOHmI-)
_Ensure your website / web app has at least Grade A score for SSL. Source: Qualsys_

1. Use HTTPS only. HTTP should always redirect to HTTPS.
2. [Qualys SSL Server Test](https://www.ssllabs.com/ssltest/index.html) - Aim for a score of A and above
3. Consider these free / open source scanning tools (among others): [Qualys](https://www.qualys.com/forms/freescan/), [OpenVAS](http://www.openvas.org/), [Nmap](http://nmap.org/), [OSSEC](https://ossec.github.io/), [Security Onion](http://securityonion.blogspot.com/), [OpenSSH](http://www.openssh.org/)

**Why:** It’s easy to forget if there is no checklist, because these features are usually not part of the UI and may not be caught in [exploratory tests](https://blog.oursky.com/2018/05/08/software-qa-exploratory-testing/).

### Broken Links

![Image](https://cdn-media-1.freecodecamp.org/images/LjTSSPVLill9Ok3wxQkbw7Af7m7ON0dcgpwU)
_Source: Screaming Frog_

1. Check that all pages get no broken links on [Monkeytest](https://monkeytest.it/)
2. Check that all pages get no invalid links on [Screaming Frog](https://www.screamingfrog.co.uk/)

**Why:** it’s better for UX, and broken links can hurt your SEO.

### Compatibility

1. Check compatibility with major desktop browsers and their versions (Chrome, Firefox, Safari, Opera, Internet Explorer)
2. Check mobile browsers too!
3. Also, check how Safari (iOS) and Chrome (Android) perform on various screen sizes.

In-app browsers can also behave differently. Since they are very common, you can try opening a link from Facebook, Reddit, Twitter, or even your Inbox app.

**Why:** Not all desktop browsers render the same way, and you want to ensure a consistent and high-quality user experience. In addition, responsive websites or web apps should adjust to different screen sizes (but sometimes the rendered version does not behave as expected for a specific size).

For example, check out a case we found with [YouTube’s sticky header for Internet Explorer](https://code.oursky.com/should-you-use-sticky-header/).

### SEO / Social Media

![Image](https://cdn-media-1.freecodecamp.org/images/LQAdZBeDCyantwVkP3DoMJm1HaesAEEFKNse)

1. Is it fetched correctly by Google? (Check with [Google Webmaster Tools](https://www.google.com/webmasters/))
2. Is it in the first page of Google Search Results Pages (SERPs)?
3. Does it contain correct OpenGraph tags for social sharing? Test by dropping the link into Facebook / Twitter / Pinterest to see what image, title, and description is generated
4. Does the site or app have the correct Title / Meta Description Tag?
5. Does it have a Favicon?

**Why:** Ensure your app, service, or website is discoverable by completing the technical side of SEO and social media. SEO helps potential users find you using key search terms. Social optimization formats your site content so that your users and community can easily share to refer more users.

According to [Hubspot’s 2017 statistics](https://www.hubspot.com/marketing-statistics), 61% of marketers say improving SEO and growing an organic online presence is their top priority for inbound marketing.

### Things that are nice to have

![Image](https://cdn-media-1.freecodecamp.org/images/qe5zm-k6pJhpf2wjBJJx8DRT6W2CtLvrHvp6)
_Image Source: [Paper CSS](https://github.com/cognitom/paper-css" rel="noopener" target="_blank" title=") by cognitom on GitHub_

1. Validate HTML/CSS with [https://validator.w3.org](https://validator.w3.org/)
2. Check basic Web Accessibility with [WAVE](https://wave.webaim.org/) or with tools at [https://www.w3.org/WAI/ER/tools/](https://www.w3.org/WAI/ER/tools/)
3. Are the 404 pages informative?
4. Does your site need a [print stylesheet](https://github.com/cognitom/paper-css)?
5. Make sure your JavaScript is error free when your page loads (check from Google Chrome’s Developer Tools)
6. Are the URLs reasonable/descriptive? Reasonable URLs helps visitors and search engines understand your content.
7. Does Canonical domain work? ([www.abc.com](http://www.abc.com/) vs abc.com, and so on)

### For Mobile Apps

![Image](https://cdn-media-1.freecodecamp.org/images/Wnq0bIwnGYiM8uQVSugh-ZsPX05gNAMujyWn)
_Small screens like the iPhone 4SE pose UI challenges._

This is a simple checklist for testing mobile apps. Here are some commonly overlooked problems with mobile apps:

1. Does input use the correct type of keyboard (for example, email or number inputs should use the related type of keyboards) and CTA? (for example, in a form, the keyboard CTA on bottom right in iOS should show next, and when tapped on, it should go to the next input of the form).
2. Does the app have a proper loading indicator when it is performing work that requires users to wait?
3. Test the app in [poor network conditions](https://code.oursky.com/offline-first-network-connection-error/), to check if it behaves as expected.
4. Test the app in airplane mode (if it is supposed to work offline).
5. Test the compatibility of apps in different screen dimensions (especially small screens).
6. Test if the app asks for permissions with a proper explanation.
7. Test if the app displays error messages that are easy to understand.
8. Test if the app works correctly during interruptions in Android (such as a call, or low storage).
9. Test the app with different localization / time zones.
10. Test the app with different font sizes (especially in iOS).

That’s about it. Please share if you found this post helpful!

**Oursky is an engineer-led digital agency based in Hong Kong that has worked with global brands and listed companies. If you have an app or would like to develop a digital solution for your product, [get in touch](https://oursky.com/contact)!**

_These notes are adapted from a workshop I held for project managers in an enterprise in Hong Kong and published [on our blog](https://blog.oursky.com/2018/05/21/launch-checklist-websites-web-apps/) on May 21, 2018._

