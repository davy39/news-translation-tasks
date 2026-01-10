---
title: Mailto Link – How to Make an HTML Email Link [Example Code]
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2021-11-16T22:58:22.000Z'
originalURL: https://freecodecamp.org/news/mailto-link-how-to-make-an-html-email-link-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/brett-jordan-LPZy4da9aRo-unsplash.jpg
tags:
- name: email
  slug: email
- name: HTML
  slug: html
seo_title: null
seo_desc: 'A mailto link allows users to send emails straight from a website using
  the user''s default email client. But how do you create a mailto link in HTML?

  In this article, I will walk you through how to create a mailto link in HTML using
  example code.

  Bas...'
---

A mailto link allows users to send emails straight from a website using the user's default email client. But how do you create a mailto link in HTML?

In this article, I will walk you through how to create a mailto link in HTML using example code.

## Basic `mailto` link Syntax

Here is the basic syntax for the mailto link:

```html
<a href="mailto:johndoe@fakeemail.com">Example mailto link</a>

```

In the browser, the user can click on the link and it will open up their default email client. 

In this example, when I click on the link it opens up my Mail app and the email address is already populated in the `to` field. 

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.07.32-AM.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.05.15-AM.png)

Using this method, I would be able to send a quick email and return to the website. 

## How to add multiple email addresses to the mailto link

You can add multiple email addresses to the mailto link using this syntax: 

```html
<a href="mailto:johndoe@fakeemail.com, janedoe@fakeemail.com">
    Multiple email addresses
</a>

```

It is important to separate the multiple email addresses using commas. 

When I click on the link in the browser, it will open up the `Mail` app and populate the email addresses in the `to` field.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.18.17-AM.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.18.42-AM.png)

## How to add a subject line to the mailto link

Here is some example code that shows you how to add a subject line to the mailto link.

```html
<a href="mailto:johndoe@fakeemail.com, janedoe@fakeemail.com?subject=this is how to use the mailto link">
    Using the subject parameter
</a>
```

After the email addresses, you need to add an `?` to separate the emails and the `subject` parameter. If you omit that `?`, then the subject link will not work.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.32.41-AM.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.34.08-AM.png)

## How to add CC and BCC to the mailto link

This is an example that shows you how to add CC (carbon copy) and BCC (blind carbon copy) recipients to the mailto link.

```html
<a
    href="mailto:johndoe@fakeemail.com, janedoe@fakeemail.com?cc=jackdoe@fakeemail.com &bcc=jennydoe@fakeemail.com &subject=this is how to use the mailto link">
    Using the CC and BCC parameters
</a>
```

After the email addresses, you need to add a `?` to separate the emails and the `CC` parameter. You also need to add an `&` before the `BCC` and `subject` parameters. 

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.44.29-AM.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.45.03-AM.png)

## How to add the body parameter to the mailto link

This is an example that shows you how to use the body parameter with the mailto link. This lets you add text to the body of your email.

```html
<a
   href="mailto:johndoe@fakeemail.com, janedoe@fakeemail.com?cc=jackdoe@fakeemail.com &bcc=jennydoe@fakeemail.com &subject=this is how to use the mailto link &body=this is an article on how to use the mailto link">
    Using the body parameter
</a>
```

You need to add an `&` before the `body` parameter.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.57.00-AM.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/11/Screen-Shot-2021-11-14-at-12.57.17-AM.png)

## Are there downsides to using mailto links?

One of the downsides to using a mailto link is that it does often come across as spam by users. Unfortunately, a lot of spammers will use this option to send emails to users. So just keep that in mind when you're using it.

## Advantages of using mailto links

A good reason to use a mailto link is if you are sending emails to a group of people that you know. If that entire group is using a default email client, then using a mailto link would be a good option over a contact form. 



## 


