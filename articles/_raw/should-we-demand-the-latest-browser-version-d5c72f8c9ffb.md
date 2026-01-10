---
title: Why we should convince our users to update their browsers — it’s a win-win.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-09T09:38:10.000Z'
originalURL: https://freecodecamp.org/news/should-we-demand-the-latest-browser-version-d5c72f8c9ffb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*g_V-TonQvcm5_8ob7sSFgw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Alex Ewerlöf

  Unless you’ve been living under a rock recently, you’re aware of Meltdown and Spectre
  — two of the most widely deployed security vulnerabilities in computer history.
  You may also know that this is not just limited to OS-level applicat...'
---

By Alex Ewerlöf

Unless you’ve been living under a rock recently, you’re aware of [Meltdown](https://en.wikipedia.org/wiki/Meltdown_(security_vulnerability)) and [Spectre](https://en.wikipedia.org/wiki/Spectre_(security_vulnerability)) — two of the most widely deployed security vulnerabilities in computer history. You may also know that this is not just limited to OS-level applications, and on the web it’s as bad as it gets:

> A website can read data stored in the browser for another website, or the browser’s memory itself. — Microsoft Vulnerability Research

![Image](https://cdn-media-1.freecodecamp.org/images/ZwbB4iJ05raoq-OmAlX9m89pCRMRPdsJ3i-A)

* **Firefox 57.0.4** ([released on 4th of January](https://www.mozilla.org/en-US/firefox/57.0.4/releasenotes/)) [fixed](https://www.mozilla.org/en-US/security/advisories/mfsa2018-01/) this.
* **Microsoft** [released and update](https://support.microsoft.com/en-us/help/4056890/windows-10-update-kb4056890) for IE and Edge on January 5th.
* **Safari** [released 11.0.2](https://support.apple.com/en-us/HT208403) on January 8th, which supposedly protects the users against these issues.
* **Chrome** users have to wait until v64 (released around 23rd of January); but [here](https://www.chromium.org/Home/chromium-security/ssca) is a list of what **you can do now** to limit the extent of the damage to your users.

Update: 2018–01–31: so far security researchers identified at least 130 malwares based on these issues: http://www.securityweek.com/malware-exploiting-spectre-meltdown-flaws-emerges

#### _Quick notes_

1. Not all those updates fix all security vulnerabilities, but they are the first action point.
2. Updating the browser is just the first step. You need to update your mobile/desktop operating system to protect yourself from a different but wider attack surface: auto updating apps. Please read more [here](https://spectreattack.com/).
3. As we understand the scope of these vulnerabilities better, more patches will come. This story is far from over.

Now the big question for us web developers is: do we keep supporting the users with older browsers that are vulnerable, or do we demand that the users have the latest browsers?

I work at the Identity team of an international company with millions of users. No amount of work I do to secure our services can prevent the user from sharing the data on our site with a malicious or infected site open in another tab.

This might be the single most important side effect of these security vulnerabilities: we may actually have a perfectly valid reason to break the web for people with older browsers.

The history of front-end development may remember this point as when we shifted from the “hippie development era” (I support all browser versions) to the “hipster development era” (I only support the latest browser versions). ?

![Image](https://cdn-media-1.freecodecamp.org/images/TOh3oFs1zrwQ2bMIvJwc5jLbejEEse3aP4TG)

This is a _huge shift_ in thinking, specially for us web developers, since we traditionally do our best to involve everyone: responsive design, progressive enhancement, and graceful degradation.

This time it’s different. In the post-Snowden era, we need to take security seriously. Supporting vulnerable browser versions is equal to promoting dangerous online life. It is our job as experts to educate the users and defend them against the bad guys. If sites don’t support the old browsers, the users **have to** upgrade.

This is a win-win situation:

* Developers get rid of legacy browser support for good
* The users get forced to make an important security decision (hopefully for the good).

If we don’t react quickly, the exploits of these issues will be deployed massively and the effect is beyond our control. The genie is out of the bottle.

![Image](https://cdn-media-1.freecodecamp.org/images/ljBa-NHW13pB8xQhsrEUMqwWtkomR2biJSlZ)

#### This is the VW-scandal of processors

In 2015, [Volkswagen was caught cheating](https://en.wikipedia.org/wiki/Volkswagen_emissions_scandal) on the emissions of their diesel engines. They cheated to make their cars more attractive to buyers. In this one, processor manufacturers “overlooked” some security concerns in their processors so they would have higher performance metrics.

I work at an international company building the _login pages_. Millions of users use our login to access the services of a wide range of companies. Naturally, my team is very concerned about security. We do our best to keep the system as secure as possible, but no amount of effort can mitigate this kind of vulnerability in browsers. For example:

* The `httpOnly` cookies are no longer inaccessible from JavaScript.
* The session cookie is super easy for other sites to steal (session spoofing).
* Chrome extensions that keep the passwords are now potentially leaking.
* The very HTML containing the `<scri`pt> tag is vulnerable, so XSS is a breeze.

Here’s an exercise: see how many of [the OWASP top 10 vulnerabilities](https://www.owasp.org/index.php/Top_10-2017_Top_10) are now **impossible to fix** in versions prior to 2018 of any major browser.

**Do we really want to serve users who don’t have a recent browser with the risk that the user’s data or our business will be compromised?** Or do we (as professionals and experts) take a stand and educate the users about the dangers and guide them to mitigate the risk?

![Image](https://cdn-media-1.freecodecamp.org/images/a4PHQNmILvijCkXy0kEqQwA4vicZukBBewto)

We need to drop support for vulnerable browsers. This will probably face a lot of resistance in a market that has traditionally been very flexible and forgiving towards the user stack (as long as they use our services, we’re good). But someone has to start the change.

### The silver lining

In every crisis there is an opportunity. I argue that it’s the coolest thing that has happened to the web development community since ES2015. We all know the pain and cost of supporting old browsers (specially the browsers which are not [evergreen](https://www.techopedia.com/definition/31094/evergreen-browser)):

* We have to bloat the code to shim features that modern browsers already have
* Debugging an older browser using its old-school debugging tools is not far from the experience of driving a car from the scrapyard after driving a modern car
* We can’t rely on browser integrity ([IE, I’m looking at you](https://www.microsoft.com/en-us/windowsforbusiness/end-of-ie-support)), so we cannot serve some sensitive information at all to certain browsers.
* We have to deal with various CSS/SVG rendering issues
* We have to test edge cases for different browsers just because we support them! There are whole [businesses](https://www.browserstack.com/) [developed](https://saucelabs.com/) around the idea of automating this tedious task with various success/effort ratios.
* The module system is now supported by all major browsers. Dropping support for vulnerable browsers has the side benefit of simplifying and modernizing our deployment channels. [**You may not need to transpile your code at all!**](https://medium.freecodecamp.org/you-might-not-need-to-transpile-your-javascript-4d5e0a438ca)

### What does it really mean?

It means you can totally rely that [async/await is available](https://caniuse.com/#feat=async-functions) on your client browser and you don’t have to transpile. It means you can assume `class` is [supported](https://caniuse.com/#feat=es6-class) and generators [are usable](https://caniuse.com/#feat=es6-generators) **TAX FREE**! It means [template literals](https://caniuse.com/#feat=template-literals), [rest params](https://caniuse.com/#feat=rest-parameters), … without transpilation, polyfill or any kind of complex toolchain! Web development is simple all of a sudden.

Hell it means [you have ES6 modules **NOW**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import) without Rollup, Webpack, Browserify…

This means a whole new era. I know it’s too early and every cell of your existence is screaming it’s a lie but nope! This is happening. If you want to support users with ancient browsers, do it at your own risk. If you care about your users security and your business’ integrity, you get all of that ?as a reward!

**One more thing: HTTP/2 is now [officially usable](https://caniuse.com/#feat=http2)!**

OK, it sounds like I’m some sort of hero now, but most of those stuff is already available in the _majority_ of the browsers. It’s just that for some weird reason, many developers and product managers assumed that [2.7% of the users](http://gs.statcounter.com/browser-version-partially-combined-market-share#monthly-201712-201801-bar) (who use IE) actually generate the majority of their business revenue and they should go to great length to support them. Sweat no more. Even if you want to, now there’s a huge reason not to!

### How?

This essay is more about WHY rather than HOW, but here are some quick thoughts:

* [Browser sniffing](https://en.wikipedia.org/wiki/Browser_sniffing) can be used to detect if the users are running a vulnerable browser. You can then refuse to serve critical data to the users with browsers that can’t keep them safe. Browser sniffing traditionally haven’t been very reliable.
* Show a notification bar to subtly warn the users; but who would read or react to that? In EU we got used to ignore the cookie notifications!
* Write a test code that actually tries the attack. If it succeeds, it shows a warning (I’m sure a NPM module will show up soon, if it hasn’t already ?).

### Conclusion

Remember how we all reacted when React.js “mixed template and code” in JSX? Sometimes we have to unlearn “best practices,” because the alternative makes more sense. I’m not talking about breaking the web! I’m asking to protect our users before all hell breaks loose. Please give it some thought.

Update 1 (2018–01–16): [Security Now #645](https://twit.tv/shows/security-now/episodes/645?autostart=false) goes into details of Spectre and Meltdown and introduces [a little handy utility (speccheck)](https://github.com/ionescu007/SpecuCheck) to test system vulnerability.

Read [You might not need to transpile your JavaScript](https://medium.freecodecamp.org/you-might-not-need-to-transpile-your-javascript-4d5e0a438ca), [When should I use TypeScript?](https://medium.freecodecamp.org/when-should-i-use-typescript-311cb5fe801b) or [Programming is the best job ever](https://medium.com/@alexewerlof/what-s-cool-about-being-a-programmer-5a1e58efeee6).

