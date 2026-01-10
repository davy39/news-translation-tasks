---
title: Can you find the bug? JavaScript security vulnerabilities course
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2023-05-16T17:43:07.000Z'
originalURL: https://freecodecamp.org/news/can-you-find-the-bug-javascript-security-vulnerabilities-course
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/semgrep2.png
tags:
- name: JavaScript
  slug: javascript
- name: youtube
  slug: youtube
seo_title: null
seo_desc: 'In a world where cybersecurity threats are more prevalent than ever, understanding
  how to safeguard your web applications is of paramount importance.

  We just published a course on the freeCodeCamp.org YouTube channel that will help
  you learn common J...'
---

In a world where cybersecurity threats are more prevalent than ever, understanding how to safeguard your web applications is of paramount importance.

We just published a course on the freeCodeCamp.org YouTube channel that will help you learn common JavaScript security vulnerabilities and how to prevent them.

Brandon teaches this course. He is an engineer at Semgrep and teaches at Carnegie Mellon University. Semgrep provided a grant that made this course possible.

This course centers around 10 examples, each illustrating a different type of vulnerability in web applications. The examples encompass a variety of languages and technologies, including JavaScript, MongoDB, and Docker, ensuring a broad understanding of potential security issues across different programming contexts.

To make it interesting and fun, the video is presented in a quiz format. You will see a small code snippet and be asked to find the vulnerabilities. Then you will learn about the vulnerabilities and how to fix them.

The course begins with an exploration of Cross-Site Scripting (XSS), a common vulnerability in JavaScript applications. It further delves into NoSQL injection attacks, a security risk associated with MongoDB databases. You will be taught how to prevent such attacks by ensuring only correct data types are accepted by the database.

Regular expression denial of service (ReDoS) attacks are also discussed, demonstrating how complex regular expressions can potentially lead to service disruption. The course illustrates how to prevent this by leveraging efficient libraries instead of creating intricate regular expressions.

The course then shifts focus to Docker and the potential security misconfigurations that can occur within Dockerfiles. You will learn the importance of not granting root privileges within Docker images to prevent disastrous consequences.

One of the critical lessons in this course is the dangers of hard-coded credentials within application code. The course shows the benefits of using environment variables to store sensitive data, which enhances security and makes it easier to manage secrets.

The course also tackles the issue of mass assignment attacks in JavaScript apps and provides a solution using careful object property assignment and password encryption.

Finally, the course concludes with an insight into host header injection attacks. You will learn to avoid using host headers from user requests, which can be manipulated to generate malicious URLs.

This comprehensive course is designed to provide developers with a solid understanding of common web application vulnerabilities and how to prevent them. By learning to identify these vulnerabilities and implement secure coding practices, participants will be better equipped to build robust and secure web applications.

Watch the full course on [the freeCodeCamp.org YouTube channel](https://www.youtube.com/watch?v=ypNKKYUJE5o) (30 minute watch).

%[https://www.youtube.com/watch?v=ypNKKYUJE5o]


