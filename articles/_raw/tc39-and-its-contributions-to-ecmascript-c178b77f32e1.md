---
title: TC39 and its contributions to ECMAScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-19T16:47:50.000Z'
originalURL: https://freecodecamp.org/news/tc39-and-its-contributions-to-ecmascript-c178b77f32e1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ReeHV0eEsfmMskVUk1vVog.png
tags:
- name: education
  slug: education
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Parth Shandilya

  Many people get confused about what is JavaScript and what is ECMAScript. Sometimes
  it’s hard to tell how they are connected with each other and what role ECMA International
  and TC39 play in the standardization of JavaScript.


  Sour...'
---

By Parth Shandilya

Many people get confused about what is JavaScript and what is ECMAScript. Sometimes it’s hard to tell how they are connected with each other and what role ECMA International and TC39 play in the standardization of JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/5OdmbTTjQnXDYHJuByZ6cF7vhao0VuyHew3D)
_Source : Warosu.org_

In this blog post, I am going to discuss TC39 and its contributions to ECMAScript.

Let’s start with all the basic terminologies used when talking about JavaScript and ECMAScript.

![Image](https://cdn-media-1.freecodecamp.org/images/nIUSJ6sNCOSO8Xpk5Y4X-xK-7OEKUbgjrK25)
_Source : [GitHub](https://github.com/exercism/meta/issues/39" rel="noopener" target="_blank" title=")_

### What is ECMAScript?

ECMAScript is a standard script language, developed with the cooperation of Netscape and Microsoft and mainly derived from Netscape’s JavaScript. JavaScript is a widely-used scripting language that is used in Web pages to affect how they look or behave for the user.

ECMA-262 is a standard published by ECMA International. It contains the specification for a general purpose scripting language which is known as ECMAScript.

![Image](https://cdn-media-1.freecodecamp.org/images/RHLIOHZTT3aSteRpwf9vrr8yWRSMAiSx1FUP)
_Source : [my.wikipedia.org](https://my.wikipedia.org/wiki/File:Javascript-736400_960_720.png" rel="noopener" target="_blank" title=")_

#### A bit more about JavaScript

[JavaScript](https://developer.mozilla.org/en-US/docs/Glossary/JavaScript) is a scripting language that enables you to create dynamically updating content, to control multimedia, to animate images, and to do pretty much everything else. (Okay, not everything, but it is amazing what you can achieve with a few lines of JavaScript code.)

#### What is ECMA?

ECMA is a standards organization for information and communication systems. ECMA aims to develop [standards](https://en.wikipedia.org/wiki/Standardization) and technical reports to facilitate and standardize the use of information communication technology and consumer electronics. It encourages the correct use of standards by influencing the environment in which they are applied, and it publishes these standards and reports in electronic and printed form.

And now, let’s introduce the hard working people behind ECMAScript: TC39.

![Image](https://cdn-media-1.freecodecamp.org/images/4jpm8A3xphEWYvTGYYQ1jAzl9xInt382JMnC)
_Source : [GitHub](https://github.com/tc39" rel="noopener" target="_blank" title=")_

### What is TC 39?

TC39 means Technical Committee number 39. It is part of ECMA, the institution which standardizes the JavaScript language under the “ECMAScript” specification. It works on the standardization of the general purpose, cross platform, vendor-neutral programming language that is ECMAScript. This includes the language syntax, semantics, libraries, and complementary technologies that support the language.

#### **TC 39 works on**:

* Maintaining and updating the standard for the ECMAScript programming language.
* Identifying, developing and maintaining standards for libraries that extend the capabilities of ECMAScript.
* Developing test suites that may be used to verify correct implementation of these standards.
* Contributing with selected standards to the [ISO/IEC JTC 1](https://www.iso.org/isoiec-jtc-1.html) committee.
* Evaluating and considering proposals for complementary or additional technologies.

Since ES6 came out, TC 39 streamlined the proposal previsioning process to meet modern expectations. The new process uses a superset of HTML to format the proposals. They use GitHub pull requests, which helped boost participation from the community. The number of proposals being made also increased.

The specification is now more of a [living standard](https://tc39.github.io/ecma262), meaning that proposals see adoption faster, and we don’t spend years waiting for a new edition of the specification to come out.

#### A more general view

By reading the [ECMAScript specification](https://www.ecma-international.org/publications/files/ECMA-ST/Ecma-262.pdf), you learn how to create a scripting language. By reading the [JavaScript documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript), you learn how to use that scripting language.

![Image](https://cdn-media-1.freecodecamp.org/images/1LfArE3VVriv6feIsd2jBvhODIUDX0sUMCbv)
_Source : [tc39/ecma262](https://tc39.github.io/ecma262/" rel="noopener" target="_blank" title=")_

### Proposal Processing

![Image](https://cdn-media-1.freecodecamp.org/images/o4rwMZpJd-UqToWMWZQ8K4cw3F-Vuh64SgkB)
_Source : pyrus.com_

#### Stage 0: Strawman

Any discussion, idea, change, or addition which has not yet been submitted as a formal proposal is considered to be a “strawman” proposal at this stage. Only members of TC39 can create these proposals, and there’s over a dozen active strawman proposals today.

#### Stage 1: Proposal

At this stage, a proposal is formalized and expected to address cross-cutting concerns, interactions with other proposals, and implementation concerns. Proposals in this stage identify a discrete problem and offer a concrete solution to that problem.

At this stage, proposal often includes a high level API description, usage examples, and a discussion of internal semantics and algorithms. These proposals are likely to change significantly as they make their way through the process.

#### Stage 2: Draft

Proposals in this stage should offer an initial draft of the specification.

At this point, it’s reasonable for implementers to begin experimenting with actual implementations in runtime. The implementation could come in many forms: a polyfill, user code that mangles the runtime into adhering to the proposal, an engine implementation (which natively provides support for the proposal), or it could be support by a build-time compiler like Babel.

#### Stage 3: Candidate

Proposals in this stage are candidate recommendations. At this advanced stage, the specification editor and designated reviewers must have signed off on the final specification. A Stage 3 proposal is unlikely to change beyond fixes to issues identified in the wild.

Implementers should have expressed interest in the proposal as well — a proposal without support from implementers is dead in the water. In practice, proposals move to this level with at least one browser implementation, a high-fidelity polyfill, or when supported by a build-time transpiler like Babel.

![Image](https://cdn-media-1.freecodecamp.org/images/8DfDJXfxWqiPPPUAaeRoEUMJMO0uhburUUxm)
_Source : [Expert Elevation](https://expertelevation.com/how-may-project-not-finished" rel="noopener" target="_blank" title=")_

#### Stage 4: Finished

Finally, proposals get to this stage when there are at least two independent implementations that pass acceptance tests.

#### What’s Next?

Proposals that make their way through to stage 4 will be included in the next revision of ECMAScript. When the spec goes through its yearly ratification as a standard, the proposal is ratified as part of it.

![Image](https://cdn-media-1.freecodecamp.org/images/-t5pyaZSwzxFcc0iOG9MMQXvzhd4wC1wc2Jj)
_Source : [get-it-done.co.za](http://get-it-done.co.za/" rel="noopener" target="_blank" title=")_

This is how ideas for evolving the ECMAScript language are accepted and added to next revision of ECMAScript. And we are all thankful for the work done by TC39, which is invaluable.

With that, we have reached the end of our discussion on TC39 and its contributions to ECMAScript.

Thanks for reading.

Sources: [TC 39 Process](https://tc39.github.io/process-document/), [ECMA International](https://www.ecma-international.org/memento/TC39.htm)

![Image](https://cdn-media-1.freecodecamp.org/images/zrBZCsgUIErlYw8aLqUKntaZxKP5gI6HyCWo)
_Did you like the read? Medium doesn’t offer partner program in my country―so I ask people to buy me coffee instead._

