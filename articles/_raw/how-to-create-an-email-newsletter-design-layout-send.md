---
title: How to Create an Email Newsletter – Design, Layout, Send
subtitle: ''
author: Naomi Carrigan
co_authors: []
series: null
date: '2021-05-13T21:19:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-email-newsletter-design-layout-send
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/pexels-anthony-shkraba-5206271.jpg
tags:
- name: email
  slug: email
- name: email marketing
  slug: email-marketing
- name: newsletters
  slug: newsletters
- name: writing tips
  slug: writing-tips
seo_title: null
seo_desc: 'If you manage a large community, chances are you need a way to communicate
  updates to your members quickly and efficiently. An email newsletter can be a very
  effective way to do so.

  In this article, I am going to provide some tips and suggestions for...'
---

If you manage a large community, chances are you need a way to communicate updates to your members quickly and efficiently. An email newsletter can be a very effective way to do so.

In this article, I am going to provide some tips and suggestions for maximizing the impact of your email newsletter: open rates, click-through rate, and not irritating your recipients.

I will also share some technical details and configurations you can use to maximize the deliverability of your email newsletter.

## How to Write an Impactful Subject Line

Your subject line is the first thing your readers will see when the email appears in their inbox. It's important, then, that you use something eye catching that encourages them to read the message.

### What to Include in the Subject Line

Your subject line should provide a brief summary of the email content or highlight the key information. Some examples would be:

> Learn Data Structures and Algorithms \[free 6-hour coding course\]

This headline comes from one of Quincy's email newsletters, and calls out the first article out of a weekly curated list of five articles.

> Our Community Reached 3,000 Members - Here's What's Next

Here the headline provides a clear summary of the email's content – an update on the community's success and future plans.

> The Observatory #4: Gravity is the key to community growth

Pulled from an [Orbit](https://orbit.love) newsletter, this subject line has two benefits: Like the others, it summarizes the content of the email. It also helps readers recognize this email as a serial newsletter, and track the number to ensure they have not missed one.

### What to Exclude from the Subject Line

You want to avoid headlines which are vague, uninformative, or may seem like spam.

> Click Here! Important Information Within!

Avoid words and phrases such as `click here`, `urgent`, `important`, and `priority`. These types of subject lines are often used in spam emails, and can cause your readers to disengage.

> April 2020 Community Update

While this subject is not going to seem like spam, it is also vague and uninformative. You want your subject to catch the reader's attention and be unique.

> Top Picks Just For You

Another vague subject line, this one also gives off a "click-bait" vibe. This type of subject line doesn't hook your readers or entice them in to reading your full email.

## How to Craft an Effective Email Body

The body of your email is where your core content will go. Having a well written and effective email body is essential.

### HTML vs. Plain Text in Emails

Using HTML in your email can make it look nice, certainly. However, HTML emails are more likely to be flagged as spam by the receiving providers.

Plain text emails are generally safer, though they offer less functionality. Additionally, a plain text email will ensure maximum compatibility with all devices, and ensure that your email can be viewed even over slower internet connections.

HTML, on the other hand, offers a much higher level of customization in terms of layout, content, and functionality. You can even implement things like interaction tracking to see who is opening (open rate), reading, and clicking on links in your email (click-through rate). Whether these features are worth the potential impact to delivery is or not is up to you.

### How to Handle Links in Emails

Speaking of links, there are some special considerations when it comes to handling links in your email. The key idea is to keep your links easily readable and verifiable.

One important aspect is the transparency of your links. You want to avoid using things like URL shorteners that hide the domain the link points to. Keeping your link's target clear ensures that your readers can trust the safety of the link.

Many sending providers offer click-tracking features, where they will provide metrics on how many of your readers click the links within your email.

While these metrics may seem useful, they do come at a cost – usually the links are obfuscated through a redirect via the provider's domain. This decreases the chance that your readers will click the link.

### Unsubscribe Links

If your email is considered commercial material (marketing, advertisements, and so on.), having an unsubscribe link is *required*. If it is a transactional (receipt, account updates) or relationship (communicating with existing contacts) email, then an unsubscribe link is not necessarily required but is still strongly recommended.

Having an unsubscribe link allows your recipients to quickly and easily opt-out of receiving future communications. While it may not seem ideal to lose your reader base, it is much better than having your emails flagged as spam (which can impact your sender reputation and cause future emails to anyone with that email provider to be blocked).

Your unsubscribe link does not need to be prominent or featured – a simple link with the text "Unsubscribe" at the bottom of your email is often sufficient.

### Content and Layout of Your Emails

The content and layout of your email body are also very important. If you are using plain text to send your email, then your biggest consideration will be the length of your paragraphs. In general, shorter paragraphs are easier to read than a "wall of text", and will help your readers stay engaged with the content.

If you are using HTML, then you have some additional obstacles to consider.

For example, including images may seem very tempting as they can make the email look more visually appealing. But each image increases the time it takes for the email to render on the reader's device, and images aren't as accessible for those who use screen readers as plain text is.

Remember that images should add to the content, not detract from the information.

Another aspect to consider when using HTML is the semantic structure. To avoid any rendering errors or accessibility concerns, you will want to keep your HTML semantically correct. I recommend using an [HTML Validator](https://validator.w3.org/) before sending the email to ensure you don't have any errors.

Content length itself is also important. You don't want to overwhelm your readers with too much information in a single email. If you have a lot of content you want to share, consider making a blog post or news article – then, link that article in your email with a brief summary of the content.

### How to Sign Off in an Email

The signature of your email is just as important as the main content. Signing off your email lets your readers know who sent it, and gives you the opportunity to close out the content.

You should include your name and your role within your organization, so that your readers see that the email came from a person. This creates the impression that it is a more personal communication and not an automatically generated email.

Finally, the signature and conclusion also give you the chance to thank your readers for their time. It is good to recognize that your readers took time out of their day to read your content. Time is valuable, and your readers have given you theirs.

## Technical Aspects of Email Newsletters

Now that you've drafted your first newsletter, you need to address the technical concerns. Namely, you'll need to figure out how you'll send this newsletter.

### Choose a Sending Provider

The first question to answer is what will you use to send this email? It is entirely possible to set up and run your own Secure Mail Transfer Protocol (SMTP) server, but that can be a significant investment of time and resources.

Instead, there are a number of providers that will handle sending the emails for you. Here at freeCodeCamp we use [SendGrid](https://www.sendgrid.com). Most providers will offer an API to request that emails be sent, or a UI to prepare your emails. Then they will handle the actual send process for you.

While these providers can get expensive at higher volumes, often times the cost is worth the access to additional features such as email validation and bounce report tracking.

### Set up Email Authentication

Another important technical aspect is email verification and authentication, especially if you are using a custom domain.

How does a provider such as Gmail confirm that the email has legitimately come from your organization and not someone pretending to be you?

There are a couple of security steps you can take to ensure that your emails are delivered while spoofed emails are not.

* **Sender Policy Framework (SPF):** You can use an SPF setting to validate that the mail server is authorized to send emails from your email domain. SPF is enabled via a `TXT` record in your domain settings. The content of that record will depend on the system you are using to send those emails.
    
* **DomainKeys Identified Mail (DKIM):** You can use DKIM to assert that the email message has not been modified in transit from the sending server to the receiving server. DKIM records are set up in your domain settings either as a `TXT` record or a `CNAME` record, depending on your provider. These records will indicate the public encryption/decryption keys.
    
* **Domain Message Authentication, Reporting, and Conformance (DMARC):** The final step, after enabling SPF and DKIM, is to set up a DMARC record. The DMARC record tells email providers what to do if an email from your domain fails SPF or DKIM, where to send delivery reports, and how often to apply the DMARC policy. A DMARC record is added as a `TXT` record to your domain settings, as `_dmarc.yourdomain.tld`.
    

Congratulations. Now that you have read this article, you should have a basic understanding of how to create and send your first email newsletter. I hope you found this article helpful.
