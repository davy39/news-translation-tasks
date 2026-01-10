---
title: The reality of being a junior software engineer at a small startup
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-13T18:20:14.000Z'
originalURL: https://freecodecamp.org/news/the-reality-of-being-a-junior-software-engineer-at-a-small-startup-3d50004fb721
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YyObHUMrZFLQGNfjfqra6g.jpeg
tags:
- name: 'Junior developer '
  slug: junior-developer
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Tan Le Tian

  Real world software development is indeed quite different from what they teach in
  school.


  _Photo by [Unsplash](https://unsplash.com/photos/dWYU3i-mqEo?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" ...'
---

By Tan Le Tian

Real world software development is indeed quite different from what they teach in school.

![Image](https://cdn-media-1.freecodecamp.org/images/5Pf1VuQzoC30B3ErkHFIQF4c43Vx3XrdEJLB)
_Photo by [Unsplash](https://unsplash.com/photos/dWYU3i-mqEo?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Annie Spratt</a> on <a href="https://unsplash.com/collections/2274666/agency-life?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Here is what I have learned after working at a startup that builds a web application tailored to customers’ specific requirements.

### 1. Being a full stack engineer is not an option but a necessity

As a small startup company with only 7 people, there are simply not enough resources to hire people specializing only in the frontend, backend, database or design. This is probably very different from how those big companies work.

We usually have several projects from different clients going on concurrently. Everyone needs to complete different projects independently. Thus, it is necessary for everyone to know all aspects of web development to implement features and fix bugs.

For example, we had to fully implement a feature that allows the user to add and edit records in a system. We need to use HTML, CSS, and JavaScript to build out forms on the frontend. While on the backend, PHP and MySQL languages are required to perform read and write database operations.

![Image](https://cdn-media-1.freecodecamp.org/images/tm4JD-E9zpsLW2hsXy3NLEwl0-3TVYwV2zWe)
_Image by [Pixabay](https://pixabay.com/users/stevepb-282134/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1015125" rel="noopener" target="_blank" title="">Steve Buissinne</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1015125" rel="noopener" target="_blank" title=")_

### 2. Shipping product which closely meets customers’ budget and requirements

The client sometimes needs software urgently to solve some problem. They set tight deadlines and offer a limited budget.

There is always a trade-off in development time, price and quality of a software product. It is really difficult to deliver a high quality yet cheap product under a tight deadline.

Thus we have to prioritize on developing the core requirements of the software first. A high-quality product takes time to build. To deliver the product on time and within the budget, sometimes we are forced to trade off on the aspects of aesthetics and user experience.

But to be fair, the customer did clearly mention to us that what he wants is just a web application that can work. He emphasized many times that he does not care about the aesthetics of the user interface, so long as we charge him the cheapest price possible.

It might sound like the customer wants a subpar product. But I would rather say he just wants a “Minimum Viable Product” or “Proof of Concept”. It is far from perfect, but good enough to be used to automate some manual work in his company.

Moreover, software development is an iterative process. If the software has been proven to be useful in real-world usage, the client probably would not hesitate to pay more for us to improve on it.

![Image](https://cdn-media-1.freecodecamp.org/images/w1EG179uTks2OzfCAjhRP7qkKTNWLB3dR-5n)
_Image by [Pexels](https://www.pexels.com/@olly?utm_content=attributionCopyText&amp;utm_medium=referral&amp;utm_source=pexels" rel="noopener" target="_blank" title="">bruce mars</a> from <a href="https://www.pexels.com/photo/man-repairing-chair-2105434/?utm_content=attributionCopyText&amp;utm_medium=referral&amp;utm_source=pexels" rel="noopener" target="_blank" title=")_

### 3. Hacky code and workarounds are sometimes unavoidable

Nobody likes to write ugly code which works but is not maintainable and scalable. Nobody likes to accumulate technical debt and pay the price for it later.

Personally, I have always tried to write readable and clean code. But sometimes there is simply no choice.

When integrating some third-party API, sometimes it will throw some unexpected results. Usually, their documentation will never clearly explain why.

When using some external open source libraries, it is inevitable that there are some minor bugs in it here and there. In my experience, the incompatibility between different versions of libraries is often the number one culprit for unexpected bugs.

All of this may cause the application to crash, and your clients are going to be extremely unhappy about it. Although the bugs are in someone else’s code, they will think it is all your fault, and will definitely hold you accountable for it.

In this case, the only way to resolve these bugs in the third party code is by implementing some clever workaround in your code. The patch might be ugly, but it works and enables the product to be shipped quickly.

![Image](https://cdn-media-1.freecodecamp.org/images/S6Rvo2wDBEu5zJMPe-iO6zgswrgqD-OnTl71)
_Image by [Pixabay](https://pixabay.com/users/jarmoluk-143740/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=436498" rel="noopener" target="_blank" title="">Michal Jarmoluk</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=436498" rel="noopener" target="_blank" title=")_

### 4. There is nothing wrong with using old school technology (like PHP, jQuery)

In more recent years, a lot of newer and cooler technology has emerged. We have React.js, Vue.js, express.js, Golang, Scala and etc.

A lot of people start to look down on older technology like PHP, jQuery, and Java because they are so “boring” and ubiquitous.

As a developer, it is always exciting to learn new technologies and build stuff with them. But from a business point of view, there is often no strong reason to use the latest and greatest technology.

In my workplace, the senior engineer has more than 10 years of experience in developing PHP applications. Thus, we have access to a deep PHP codebase on common features like sending emails, sending notifications to a mobile app, and uploading images to AWS S3.

This means to implement a new feature in a project, we can copy-paste some code from older projects and do some necessary modifications. It enables us to develop web applications quickly.

Although PHP has its own flaws as a language, it is good enough as a tool to build out the product that meets our customers’ requirements.

Also, there is a lot of hot debate out there on whether the good old jQuery should be abandoned in favor of pure vanilla JavaScript.

Some people dislike using jQuery because it requires loading a 30kb library (minified and gzipped) when loading the webpage. They advocate the use of vanilla JavaScript as it can make web applications that are more lightweight and load faster.

But considering the popularity of jQuery, most of the developers around me are much more familiar with jQuery. They can get things done quickly with it. Using a 30kb library sounds like a relatively small price to pay for higher development velocity.

Also, why not use the newer and cooler frameworks like React.js or Angular.js?

In my case, most of the projects I have done are related to inventory management systems used internally by the clients’ company. The good old jQuery seems sufficient to implement all the features as per required by the clients.

Well, using JavaScript frameworks to build a Single Page Application may provide a better user experience. But it feels a bit like overkill for smaller web application used internally by a few company admins.

That said, we are not against the usage of new technology. We will not hesitate to use the modern JavaScript frameworks if our client demanded a dynamic web application with complex frontend features.

### Conclusion

Being a software engineer is really so much more than writing some code. Ultimately, the real challenge lies in understanding the problem faced by the customer. Then develop a solution within the budget and deadline.

#### Thank you so much for reading! ? Feel free to f[ollow me on Twitter](https://twitter.com/getsudocode) for more stories like this. ?

_Originally published at [https://getsudocode.com](https://getsudocode.com/the-reality-of-being-a-junior-software-engineer-at-a-small-startup/) on April 14, 2019._

