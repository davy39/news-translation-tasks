---
title: Build Secure Web Applications with PHP, Symfony, and MongoDB
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2025-09-11T13:30:55.425Z'
originalURL: https://freecodecamp.org/news/build-secure-web-applications-with-php-symfony-and-mongodb
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1757573041841/0bbcb80c-76b9-4792-be3b-fba79ea344b1.png
tags:
- name: MongoDB
  slug: mongodb
- name: Symfony
  slug: symfony
- name: PHP
  slug: php
- name: youtube
  slug: youtube
seo_title: null
seo_desc: 'Data breaches are a constant threat, and traditional encryption practices
  often aren''t enough to protect sensitive information throughout its entire lifecycle.

  We just posted a course on the freeCodeCamp.org YouTube channel that will teach
  you how to...'
---

Data breaches are a constant threat, and traditional encryption practices often aren't enough to protect sensitive information throughout its entire lifecycle.

We just posted a course on the freeCodeCamp.org YouTube channel that will teach you how to build applications that are truly secure from the ground up using PHP, Symfony, and MongoDB.

I developed this course. I will teach you how to build a system where data is protected not just at rest and in transit, but also while it's in use.

Throughout this comprehensive, step-by-step tutorial, you will build a fully functional personal finance application. The application will allow users to create accounts, log transactions, and view their financial information.

The core of this course focuses on solving a major challenge in application security which is how to perform queries on encrypted data. You'll learn how to find a user by their social security number or search for transactions within a specific amount range, all without ever decrypting the information on the database server.

I use MongoDB's Queryable Encryption to encrypt sensitive data on the client-side. This data is then stored as fully randomized encrypted fields in the database, yet you can still run equality and range-check queries on it. The server never has access to the unencrypted data or the encryption keys, keeping the data secure throughout its entire life cycle.

This tutorial is designed for developers who have some experience with PHP and a framework like Symfony or Laravel, but even if you're new to these technologies, you should be able to follow along.

Watch the full course now [on the freeCodeCamp.org YouTube channel](https://youtu.be/UuknxVdqzb4) (1-hour watch).

%[https://www.youtube.com/watch?v=UuknxVdqzb4]
