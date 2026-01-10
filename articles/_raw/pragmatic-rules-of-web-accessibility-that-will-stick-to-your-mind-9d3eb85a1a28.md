---
title: Pragmatic rules of web accessibility that will stick to your mind
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-17T16:00:50.000Z'
originalURL: https://freecodecamp.org/news/pragmatic-rules-of-web-accessibility-that-will-stick-to-your-mind-9d3eb85a1a28
coverImage: https://cdn-media-1.freecodecamp.org/images/1*n8wSWsgY5iNzLCqNOIdRIQ.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: Inclusion
  slug: inclusion
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Tiago Romero Garcia

  I first started to work with web accessibility back in 2015, at an American retail
  giant. It had just gotten a hefty lawsuit, as its website failed to comply with
  the Americans with Disabilities Act (ADA). After that happened, ...'
---

By Tiago Romero Garcia

I first started to work with web accessibility back in 2015, at an American retail giant. It had just gotten a hefty lawsuit, as its website failed to comply with the Americans with Disabilities Act (ADA). After that happened, my team and I worked extensively on the ADA compliance, when I was introduced to many web accessibility principles.

However, over the next years, I found myself constantly violating such principles, even though I was regularly working with them. Somehow, I would never remember them properly while I was coding. I wouldn't admit it, but I definitely had not fully internalized these principles.

Eventually, I decided that the time had come to invest my time into boiling things down into simple, pragmatic rules which are easy to remember. I finally did just that, and they have been working quite well for me ever since.

This article has 2 sections: [What is web accessibility?](#138c) and [3 pragmatic rules of web accessibility](#13e5). In the first section, I give a refresher on web accessibility and share my experience with it. But if you would rather cut to the chase, then just go straight to the second session: [3 pragmatic rules of web accessibility](#13e5).

### What is web accessibility?

As I mentioned, back in 2015 my company got sued for not complying with the ADA.

The [ADA](https://www.ada.gov) is a civil rights law that

> _“prohibits discrimination against individuals with disabilities in all areas of public life, including jobs, schools, transportation, and all public and private places that are open to the general public”_.

This way, the ADA requires that **businesses, state and local governments, and nonprofit services providers** make accommodations for the disabled public to access the same services as able-bodied patrons. Similarly, **federal government agencies** are required to comply with a federal law called [Section 508](https://www.section508.gov).

In the context of the web, any public website in the USA failing to comply with the ADA or Section 508 is in reality excluding several groups of users with varying degrees of impairments.

On the other hand, the inclusive practice of making a website's content available to everyone and its functionality able to be operated by anyone is understood as [web accessibility](http://en.wikipedia.org/wiki/Web_accessibility), or just [a11y](https://a11yproject.com/posts/a11y-and-other-numeronyms/).

#### Who can be supported by a11y?

According to the [World Report on Disability](http://www.who.int/disabilities/world_report/2011/report/en/), published in 2011 by the [World Health Organization](http://www.who.int) (WHO), it is estimated that 15% of the global population lives with some form of disability. Of these, 2 to 4% experience significant difficulties in functioning.

An excellent article by the great [Addy Osmani](https://www.freecodecamp.org/news/pragmatic-rules-of-web-accessibility-that-will-stick-to-your-mind-9d3eb85a1a28/undefined), [Accessible UI Components For The Web](https://medium.com/@addyosmani/accessible-ui-components-for-the-web-39e727101a67), spells out the four major areas of disabilities to be considered in the context of a11y:

**1. Visual issues:** can range from an inability to distinguish colors to no vision at all.

**2. Hearing issues:** means a user may have issues hearing sound emitted from a page.

**3. Mobility issues:** can include the inability to operate a mouse, a keyboard, or touch-screen.

**4. Cognitive issues:** means a user may require assistive technologies to help them with reading text, so it’s important to ensure text alternatives exist.

Keep in mind these are very broad ranges of impairments. This means that one doesn't need to have a severe impairment to need a11y support.

In order to learn more, I recommend taking the [Web Accessibility](https://www.udacity.com/course/web-accessibility--ud891) free course on Udacity, by Google. Here is a video from the course that covers these areas of disability:

#### Alright, so how can we provide a11y support?

By the time we got the lawsuit in 2015, there had been an audit which found several a11y issues. Our team went through a day-long accessibility training session, where we learned about the [Web Content Accessibility Guidelines](https://www.w3.org/TR/WCAG21/) (WCAG, currently at version 2.1), which are generally accepted as the standard for a11y compliance.

The WCAG are maintained by the [Web Accessibility Initiative](https://www.w3.org/WAI/) (WAI) of the [World Wide Web Consortium](https://www.w3.org) (W3C). The same group authored the [Accessible Rich Internet Applications](https://www.w3.org/TR/wai-aria-1.1/) (WAI-ARIA or simply ARIA, currently at version 1.1), which is a specification on how to increase the a11y of web pages through additions to HTML as roles and ARIA attributes.

These guidelines are categorized into three levels of compliance:

* A (must support)
* AA (should support) and
* AAA (may support).

Many of the accessibility laws around the world are based on WCAG levels. For instance, in January 2017, Section 508 adopted conformance with level AA of WCAG 2.0.

A great summary of the guidelines can be found at [WebAIM’s WCGA 2 checklist](https://webaim.org/standards/wcag/checklist), where each criteria indicates its corresponding compliance level.

#### How hard is it to learn WCAG and WAI-ARIA?

I would like to take a moment to share my experience of learning a11y.

While our training was quite comprehensive, and given by extremely knowledgeable people, we simply sat there for hours while we reviewed the entire WCAG specification, item by item. Their slide deck was humongous, and we moved swiftly through the slides. I will be honest: It was cumbersome, since the WCAG is definitely not small.

Long story short, we were able to write down many action items, and we immediately started working on these fixes. However, this soon became something repetitive, mechanical, a response to stimuli. Stories in, code out. We were drowning in the sea of a11y.

Everybody knew how well-versed we became in a11y, so nobody would contest our work. The a11y stories stopped to come in, and we got different priorities. The expectation was that we would carry over what we had learned, which actually happened for quite a while.

As time passed, some people left, some people joined, and the new management came in. The market moves fast. We changed our focus and our team spirit. Needless to say, we became so involved with the new things that our a11y compliance slipped far into the background.

It was so bad, that six months later we had another audit, only to discover we were still sitting in a big pile of a11y violations! We soon realized that while we fixed the original audited issues, **most of the new code we wrote was just as bad on a11y**. Not only that, we never adopted a11y as part of our development checklist, and the newcomers were never trained on the subject.

**Conclusion**: We simply allowed it to happen — a11y was being neglected, and the key ideas were not ingrained in us.

In other words, we were creating **exclusions**, which is what happens when we solve problems using our own biases, according to [Microsoft Inclusive Design](https://www.microsoft.com/design/inclusive/).

#### Experiencing an exclusion

![Image](https://cdn-media-1.freecodecamp.org/images/1*PrdvH8QWWSO4296p_3eREg.jpeg)
_“Exclusion is never the way forward on our shared paths to freedom and justice.” — Desmond Tutu_

Sometimes you need to experience things yourself in order to better understand them. That's what happily happened to me.

I donate my platelets regularly, since my blood type is A+, so I can help more people this way. Once, my vein got perforated incorrectly and I got a big and painful bruise on my left arm.

Typically, regular blood donations last 10 minutes or so, but platelet donations last around 90 minutes. It took us about 20 minutes to notice that I had a blown vein, since my arm was covered with blankets (because blood returns make you feel cold).

By that time, the damage was done, and we had to interrupt the donation. My arm got quite bloated and very sensitive for a few days. So much that I didn't feel like using my left arm at all to work.

Now, I was trying to do everything with my right hand. All of a sudden, I noticed it wasn’t efficient to keep alternating between keyboard and mouse, and I would rather do the whole task at hand using just the keyboard or the mouse.

Soon, I found myself preferring to use exclusively the keyboard for everything, and then I noticed how many sites are simply not there on keyboard support. Then it came to me: I was experiencing an exclusion, even though it was just a **temporary** one.

And then, exactly at that moment, I remembered the past me working with a11y and letting these exclusions pass. Oh, man!

#### Levels of exclusions

According to [Microsoft's Inclusive 101 Toolkit](https://www.microsoft.com/design/inclusive/), there are three levels of exclusions:

1. **Permanent:** experienced by those who have a disability such as loss of limb, sight, hearing, or speech.
2. **Temporary:** experienced by those who have a short-term injury or are going through certain events for a short time, such as looking into a bright light, wearing a cast, or ordering dinner in a foreign country.
3. **Situational:** experienced by those whose abilities can dramatically change in specific environments, such as being unable to hear well in a loud crowd, being visually impaired in a car, or new parents doing tasks one-handed.

It was extremely mind opening for me to have a temporary exclusion, since I had never been faced before with such a challenge at work.

Nevertheless, I am tremendously privileged since mine was just for a couple of days, while millions of people around the world experience permanent exclusions for their entire lives.

#### Coding for change

Finally, it came to me: Implementing a11y means contributing to a **more inclusive world**! Here are a few things we can do as engineers:

* Learning how to write code that supports a11y.
* Adding a11y compliance as part of your development checklist (just like you would work on unit testing and documentation).
* Talking about a11y with your team, to increase the awareness.
* Assessing if your team is producing accessible code, and logging a11y issues as defects to be taken up by the team.
* Questioning business requirements which are not covering a11y and demanding accessible alternatives.
* Sharing your experience, and showing your peers how to adopt a11y in a practical way, which is the very reason why I am writing this article. :)

### 3 pragmatic rules of web accessibility

So here am I with my mission to distill a11y into 3 practical rules that will stick to your mind. From these rules, you should be able to derive the rest of the knowledge and find guidance on implementing a11y in your project.

**Disclaimer:** These rules don't replace the need to learn a11y. They are also not comprehensive. They simply will provide you a basic yet effective foundation, so you can follow the rest of path on your own.

Again, in order to learn a11y I wholeheartedly recommend taking the [Web Accessibility](https://www.udacity.com/course/web-accessibility--ud891) free course on Udacity, by Google:

[**Web Accessibility | Udacity**](https://www.udacity.com/course/web-accessibility--ud891)  
[_Get hands-on experience making web applications accessible. You'll understand when and why users need accessibility…_www.udacity.com](https://www.udacity.com/course/web-accessibility--ud891)

Now to the 3 pragmatic rules of web accessibility. I hope you can take them with you and apply them every day at work:

#### 1) Insist on semantic HTML elements, or DIY

![Image](https://cdn-media-1.freecodecamp.org/images/1*YNNi0BjugGN3ouENt2g-Dw.jpeg)
_"The Semantic Web isn’t inherently complex. The Semantic Web language, at its heart, is very, very simple. It’s just about the relationships between things." — Tim Berners-Lee_

This one is for me the **golden rule of accessibility**, hands down.

**Semantic** elements are these which convey a certain meaning along with the content they represent, like `<butt`on`>, &`lt`;in`pu`t>`;, &l`t;a`>, <h1> and <p>. They provide some context to the user agent (browser, device or assistive technology like a screen reader), so it will know how to interact with and what to expect of these elements.

They are different than **neutral** elements, such as `<d`iv>`; and` <s**pan>, or pr**esentational el`ements l`ike &`lt;ce`nter> and <big>, which do not provide such context to the user agent.

Semantic elements are already accessible (and SEO-friendly) for the most part. This means they already cover many a11y aspects out of the box, like:

* handling of **focus** properly through the tab key.
* responding to **keyboard events** (as Enter, Esc, space, arrow keys).
* representing **semantic** information (Name, Role, State and Value) so assistive technology will be able to understand it.
* conforming to **color contrast** requirements with default styling.

However, when not using a semantic element, **you are supposed to manually code all of these things in order to make it accessible**.

Which means you would need to do things like:

* add `tabindex="0"` so the component will be part of the natural tab order, and use `focus()`, `display: none` or `aria-hidden` to avoid focus traps. Learn about tabindex on [Using tabindex](https://developers.google.com/web/fundamentals/accessibility/focus/using-tabindex).
* attach listeners for expected **keyboard events**. Check the expectations for your component on [WAI-ARIA Design Patterns and Widgets](https://www.w3.org/TR/wai-aria-practices-1.1/#aria_ex).
* use a **role** to provide some semantics and SEO value. Learn all the possible roles on [WAI-ARIA Categorization of Roles](https://www.w3.org/TR/wai-aria-1.1/#roles_categorization).
* provide **ARIA attributes** to describe the state and value. Find out which ARIA attributes apply each role on [WAI-ARIA Definition of Roles](https://www.w3.org/TR/wai-aria-1.1/#role_definitions).
* watch out for the **color contrast** and the **focus indicator**, especially if using `outline: 0` (which is not recommended).

Still on semantic elements, here are a few more things to keep in mind:

* use [sectioning tags](https://www.w3.org/TR/wai-aria-practices/examples/landmarks/HTML5.html) to structure your page into sections, otherwise you need to provide landmark roles.
* use [heading tags](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/Heading_Elements) to organize your text content, so you can express the relationship between sections and their order of importance. For the record: There must be only one `<`h1> on each page.
* use `<label for="..`."> with form fiel`ds as &`lt`;input&g`t;, &`lt;select&`gt; and <textarea>.
* use the right tool for the job, for instance if it’s a link, use `<a href=`""> and `never <span oncli`ck="...">, and if it’s a `button,` use <but`ton> and never <a hr`ef="#" onclick="...">.

Well, semantic elements seem way more convenient, don’t you think?

#### 2) Provide alternatives for images, color, sound and movement

![Image](https://cdn-media-1.freecodecamp.org/images/1*MhrobCU9QTezLtLUFPGHpQ.jpeg)
_"Painting is just another way of keeping a diary." — Pablo Picasso_

Assistive technology deals best with text. When using anything else, always provide a text alternative, for instance:

* For images, provide a **text alternative**. You can use `alt="description"` for **informative images** (those which have a meaning, like a picture or a standalone icon) and `alt=""` for **decorative images** (those which don’t have a meaning, like an icon inside a button and right next to its text). This is especially important on image links.
* Still on images, when relying on them for user interaction, provide an **audio alternative**, or explore how to stop relying on them. You can check [Google reCaptcha](https://www.google.com/recaptcha/intro/v3beta.html), for instance.
* For colors, when indicating a validation state, a designated area or simply distinguishing elements, add a **secondary indicator** such as informative text, an icon or even a tooltip.
* Still on colors, find out the **contrast ratio** of your text and check if it meets the standard you are following. For instance, the level AA of the WCAG requires a minimum of 4.5:1 for regular text and 3:1 for large text.
* For audio tracks and video, provide **text captions** or a **transcript** when they are available. For action sounds, provide a **visual alternative**.
* For user movement, any time we expect the user to perform specific gesture movements, make them **optional** or provide **interaction alternatives** through the keyboard.
* For automatic movement, avoid flashes, blinking, moving content, and new windows. When it’s unavoidable, add **controls** to adjust the time, pause or hide this content. Also, use [aria-live](https://www.w3.org/TR/wai-aria-1.1/#aria-live) so the screen reader can notify the user whenever an interruption happen.

#### 3) Make it a habit to use a11y tools into your work routine

![Image](https://cdn-media-1.freecodecamp.org/images/1*Tfk2GQ_VqsCsAKHbVnGEYA.jpeg)
_"We shape our tools and then our tools shape us." — Marshall McLuhan_

This is perhaps the most efficient rule, so when you let something pass from the two rules above, this one should catch it.

I am listing here several a11y tools. Give them a try, run them on your website, see what you learn from them and try to stick around with them.

There are basically 3 types of tools I recommend that you adopt:

**a) For your development checklist**

* [aXe chrome plugin](https://chrome.google.com/webstore/detail/lhdoppojpmngadmnindnejefpokejbdd): An easy-to-use a11y checker which finds issues and provides suggested fixes.
* [Wave](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh?hl=en-US): An a11y evaluation tool which provides visual feedback about the accessibility of your web content by injecting icons and indicators into your page.
* [DevTools (Accessibility pane, Contrast ratio and Audits)](https://developers.google.com/web/updates/2018/01/devtools#a11y): These 3 DevTools features allow to navigate the accessibility tree and see a11y properties for each element, to verify the color contrast ratio for text elements, and to perform full-page audits on accessibility (and other metrics).
* [NoCoffee chrome plugin](https://chrome.google.com/webstore/detail/nocoffee/jjeeggmbnhckmgdhmgdckeigabjfbddl): Simulates the problems faced by people with slight to extreme vision problems.
* [High Contrast chrome plugin](https://chrome.google.com/webstore/detail/high-contrast/djcfdncoelnlbldjfhinnjlhdjlikmph): Lets you browse the web with your choice of several high-contrast color filters designed to make it easier to read text, so you can check how your website fares for users that need high-contrast support.

**b) For manually testing with real screen readers**

* Mac [VoiceOver](https://www.apple.com/voiceover/info/guide/_1124.html) (included in macOS).
* Windows [NVDA](https://www.nvaccess.org/download/) (free) and [JAWS](http://www.freedomscientific.com/Products/Blindness/JAWS?gclid=CjwKCAiA8vPUBRAyEiwA8F1oDDzHAjW9-GfooiNT3sCDcTg_7LNXvHz4XL7osONDyf3Y4k9KRbcuihoCKGMQAvD_BwE) (paid).

**c) For automated auditing**

* [Google Lighthouse](https://www.npmjs.com/package/lighthouse): Automated auditor, similar to DevTools Audits.
* [aXe](https://www.npmjs.com/package/axe-core): Automated checker for the same a11y rules found on aXe chrome plugin.
* [Pa11y Dashboard](https://github.com/pa11y/pa11y-dashboard): A web interface which helps you monitor the accessibility of your websites.

#### Learn more

* [508, ADA, WCAG: What’s the difference?](https://www.logicsolutions.com/508-ada-wcag-accessibility-difference/)
* [WHO's World Report on Disability](http://www.who.int/disabilities/world_report/2011/report/en/)
* [Accessible UI Components For The Web](https://medium.com/@addyosmani/accessible-ui-components-for-the-web-39e727101a67)
* [Microsoft Inclusive Design](https://www.microsoft.com/design/inclusive/)
* [Web Accessibility free course on Udacity, by Google](https://www.udacity.com/course/web-accessibility--ud891)
* [WebAIM’s WCGA 2 checklist](https://webaim.org/standards/wcag/checklist)
* [Using tabindex](https://developers.google.com/web/fundamentals/accessibility/focus/using-tabindex)
* [WAI-ARIA Design Patterns and Widgets](https://www.w3.org/TR/wai-aria-practices-1.1/#aria_ex)
* [WAI-ARIA Categorization of Roles](https://www.w3.org/TR/wai-aria-1.1/#roles_categorization)
* [HTML5 Sectioning Elements](https://www.w3.org/TR/wai-aria-practices/examples/landmarks/HTML5.html)

