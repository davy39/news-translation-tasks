---
title: Why you should write merge requests like you’re posting to Instagram
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2019-05-02T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-write-merge-requests-like-youre-posting-to-instagram-765e32a3ec9c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BW0h4oGKEJaPmSbE2z-o1w.jpeg
tags:
- name: coding
  slug: coding
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: Merge requests (or pull requests) are a huge part of a team’s development
  process. It’s the main gatekeeper preventing developers from throwing whatever they
  want into the default branch. It’s also a reference to the history and understanding
  of the ...
---

Merge requests (or pull requests) are a huge part of a team’s development process. It’s the main gatekeeper preventing developers from throwing whatever they want into the default branch. It’s also a reference to the history and understanding of the changes someone is making to an application. It gives code reviewers and testers more confidence in really knowing what’s going on.

![Image](https://cdn-media-1.freecodecamp.org/images/YgdjhAHTChoj8uhrbINlzctXz1SyGeCWEHBY)
_Gandalf: you shall not merge this code!_

So what does it have to do with Instagram? Bear with me here, it has merit.

### The foundations of an Instagram post

This can apply to any social media platform, but we’re going to stick with Instagram here. Let’s start with an example of a post from NASA. The post can be broken down into a few vital components: an image, description, and hashtags.

![Image](https://cdn-media-1.freecodecamp.org/images/22w7-FHEtT7b8VUmP6o0k0S4uDQ7-pHsBcUf)
_[https://www.instagram.com/p/BwH0GRAjL5i/](https://www.instagram.com/p/BwH0GRAjL5i/" rel="noopener" target="_blank" title=")_

### What does this have to do with code?

I’m getting there! Looking at each part, we can start to relate these back to our merge request. Starting with the 3 basics:

* Image => Code
* Description => What is your feature?
* Hashtags => What parts of your application does this impact?

#### Code

Just as much as the image or video is the most important aspect of a post, so is your code. It’s the primary content that’s driving the conversation and interest. While it’s strong on its own, without context it can create its own set of issues.

#### Description

In NASA’s post above, without seeing the description, this could very well be a blurry illustration of the Death Star. Instead, thanks to the description, we find out it’s Jupiter. The infrared imaging allows us to get a better look at its atmosphere.

![Image](https://cdn-media-1.freecodecamp.org/images/2jgyZaOM9IPXhInSF6AoSEMBTofSb0CydA7L)
_That’s no moon! Right, it’s Jupiter._

Not knowing what the code you’re looking at does or what it impacts can lead to confusion and a lack of understanding for those not already familiar with your application. Even for veterans, only being able to see a small segment of a diff when compared to a giant codebase completely changes what you’re looking at.

#### Areas of Impact

Just as hashtags allow people to tag content to show the topics it’s related to, providing an area of impact helps give your reviewer an idea of where they should be paying attention. If the reviewer or tester only knows of one location a changed component is used (when it’s used more broadly throughout the application), they’re potentially missing important use cases that may have breaking changes outside of that instance.

### Learning from History

I’m sure Jupiter will stick around for the next 2 years. Looking back at our code within that amount of time can feel like a completely different landscape. Bits of code that were worked on by developers long gone may not be completely understood. It could be crucial to the integrity of an application.

![Image](https://cdn-media-1.freecodecamp.org/images/TK-wVHMdMdlwkREfBQumX1K6H3f7CG-Rocs1)
_[https://www.instagram.com/p/BveREmPD9Vb/](https://www.instagram.com/p/BveREmPD9Vb/" rel="noopener" target="_blank" title=")_

Each of these merge request components plays a key role in preventing lost knowledge and context of changes to an application. Why was the business logic set up to handle a particular situation this way? Finding the commit and relating it back to the merge request could very well prevent a situation where your application is losing money due to a bug that you wouldn’t have thought of without that context.

### Bonus: Comments

Feedback is crucial to Instagrammers and developers alike. Being able to learn from others and gain a different perspective is key to not just growing as an individual, but being able to pull the best pieces and wisdom from all parts of your team. Taking and understanding this feedback is crucial to strengthening your application.

### How does the [E84 Team](https://www.freecodecamp.org/news/why-you-should-write-merge-requests-like-youre-posting-to-instagram-765e32a3ec9c/undefined) write Merge Requests?

On larger projects, we take some extra effort to help guide our team into writing quality merge requests. Particularly, we use merge request templates to get the job done.

We’ve tried to break it down into 2 primary topics, an overview of the work and how to test.

```
## Overview

### What is the feature?
(Describe what the feature is)

### What is the solution?
(Describe at a high level how the feature was implemented)

### What areas of the site does it impact?
(Describe what parts of the site are impacted and*if*code touched other areas)

## Testing

### What's required testing?
(Describe the prerequisites for the steps to test)

### What are the steps to reproduce?
(Describe and list the steps to reproduce - distinguish if instructions are for a developer or QA tester)

## Other Notes
(Add any additional information that would be useful to the developer or QA tester)
```

Also available here: [https://gist.github.com/colbyfayock/086038bc5e38fd7edf4e73e1602de71c](https://gist.github.com/colbyfayock/086038bc5e38fd7edf4e73e1602de71c)

Since adding this template, we’ve been able to see a clear upward trend in the quality of our merge requests. Subsequently, better historical references to code changes.

### How do I add templates?

We’re a Gitlab-flavored house for our internal projects. Most Git software should be able to provide the option to add a merge request template. To help get started:

* Gitlab: [https://docs.gitlab.com/ee/user/project/description_templates.html#creating-merge-request-templates](https://docs.gitlab.com/ee/user/project/description_templates.html#creating-merge-request-templates)
* Github: [https://help.github.com/en/articles/creating-a-pull-request-template-for-your-repository](https://help.github.com/en/articles/creating-a-pull-request-template-for-your-repository)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?️ Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

_Originally published at [https://www.element84.com/blog/write-merge-requests-like-youre-posting-to-instagram](https://www.element84.com/blog/write-merge-requests-like-youre-posting-to-instagram)._

