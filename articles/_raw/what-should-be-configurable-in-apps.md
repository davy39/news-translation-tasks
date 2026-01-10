---
title: What Items Should Be Configurable in an Application?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-27T20:30:15.000Z'
originalURL: https://freecodecamp.org/news/what-should-be-configurable-in-apps
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/sigmund-f0dJjQMhfXo-unsplash.jpg
tags:
- name: configuring settings
  slug: configuring-settings
- name: configuration
  slug: configuration
- name: Web Applications
  slug: web-applications
seo_title: null
seo_desc: "By Kenneth Angelo Reyes\nConfiguration is an essential part of every application.\
  \ It helps enhance an application's flexibility and maintainability. \nWith this\
  \ in mind, it's very important that developers are able to correctly identify what\
  \ items shou..."
---

By Kenneth Angelo Reyes

Configuration is an essential part of every application. It helps enhance an application's flexibility and maintainability. 

With this in mind, it's very important that developers are able to correctly identify what items should be in configuration.

In this article, I'll walk you through 8 items that should be configurable in your applications.

## Define "Configuration"

We will not be aligning with any existing platforms out there.

For the context of this article, an application configuration has the following characteristics:

* A set of simple or complex values that can affect an application's behavior
* Values can easily be changed without requiring any code deployment

With that out of the way, let's go to our list!

## The "Configurables"

Here are the 8 items that should be configurable in your applications.

### Magic Numbers

These are special numbers that are used in certain displays, validations, or business rules.

**Examples:**

* Number of days before an SLA (Service Level Agreement) is breached
* Number of decimal places when rendering a currency

### URLs

When connecting to 3rd-party services, there's no knowing when their URLs will change. It's best to keep these values configurable. Additionally, configurable URLs can help you control the value in different environments.

**Examples:**

* API Endpoints
* External websites

### Feature Toggle

This is helpful when there is a feature that's already in production, but which can only be enabled after a certain time.

An example of this is a feature that can only be enabled after a live stream event. Normally, this can be a Boolean value, but you can also use Date Time for this. This just means that the feature will automatically be enabled once that time has passed.

### Regex Patterns

Some Regex patterns, especially those used in validation, have the potential to change regularly.

An example of this is phone number validation. Initially, your application might allow phone numbers from several countries. Then, perhaps a change in requirements came about where you now have to allow only phone numbers from specific countries. 

If your validation pattern is in configuration, then you can quickly make this change.

### Special Dates

Not the romantic ones! In some applications, there's a need to "block" certain dates from being selected by users.

A perfect example of this are public holidays. Since these dates can change regularly, they should be placed in configuration.

### Connection Strings

Database connection strings should never be placed in your code! When you place connection strings in configuration, you'll also be able to set a different value per environment.

### Formulas

For finance-related applications, making formulas configurable is very important. For these type of applications, adapting to policy or regulatory changes as soon as possible is a must.

### Special Messages

This may be more applicable to non-CMS applications. In some cases, the regular changes in text messages are tied to legal or regulatory policies. Therefore, these messages should be easy to update.

A good example of this is an announcement that shows whether the application is currently facing any issues or is under maintenance.

## Conclusion

These are the 8 items that I believe should be configurable in every application. I'm sure you have other items on your mind. Let me know! Looking forward to hearing from you.

Glad you reached the end of this article. I hope you learned something new from me today.

_[Cover photo](https://unsplash.com/photos/f0dJjQMhfXo) [f](https://unsplash.com/@sigmund?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)rom [Unsplash](https://unsplash.com/s/photos/settings?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)_

