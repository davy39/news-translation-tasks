---
title: How ignoring UX hurts your API and what you can do about it
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-21T08:48:12.000Z'
originalURL: https://freecodecamp.org/news/how-ignoring-ux-hurts-your-api-and-what-to-do-about-it-e4f600f9cbfa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8c333d_YNEHG4q3UDb1wTA.jpeg
tags:
- name: api
  slug: api
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ifeoluwa Arowosegbe

  Creating experiences that users love is crucial to the success of any product. Companies
  invest lots of resources trying to make sure they have kickass landing pages and
  cool page transitions. Yet, these efforts are often in sh...'
---

By Ifeoluwa Arowosegbe

Creating experiences that users love is crucial to the success of any product. Companies invest lots of resources trying to make sure they have kickass landing pages and cool page transitions. Yet, these efforts are often in sharp contrast with developers’ experiences when they try to consume their APIs.

Quick Note: This is about APIs in the context of RESTful services.

Your API is a full-fledged product. It is consumed by developers who are considered to be technically sound, but that doesn’t mean they are less-deserving of top notch, premium treatment. **Developers are users, too**.

> “The goal of user experience design in industry is to improve customer satisfaction and loyalty through the utility, ease of use, and pleasure provided in the interaction with a product.” — [UX Curve](https://academic.oup.com/iwc/article/23/5/473/660020)

### You’re Losing Money

Long before a developer decides to recommend your product/service to the tech lead or company, you should know that they’ve already scoured your API documentation page. They’ve tried calling several endpoints, and have made sure that they’re comfortable — and in rare cases, happy — with your offering(s).

You lose revenue if anything (docs, response time, and so on) doesn’t meet the developer’s standards. They’d rather go in search of more desirable alternatives than stick around trying to figure out the correct way to consume your API.

### You’re Missing Out On Talent

A [study](https://www.glassdoor.com/employers/popular-topics/hr-stats.htm) by Glassdoor shows that 61% of their users actively conduct research about a company before deciding to apply for a job there. We can only expect this number to be steeper for professional developers that have a 98% employment rate (3.9% work part-time), according to [StackOverflow’s Developer Survey](https://insights.stackoverflow.com/survey/2017#work).

Developers put your company and products under the microscope when considering an opportunity to work with you. For companies that offer publicly accessible APIs, it’s a portal into the engineering practices in your company (and offers the possibility of discovering major red flags).

Seemingly basic things like using the wrong HTTP methods to perform actions on resources, not versioning endpoints, and poor documentation could be all a developer needs to decide if they’ll consider joining your engineering team or move on instead.

I’m sure you’d agree that losing top talent to the competitor is the last thing any ambitious business would want.

### Avoiding Bad UX

The effects of neglecting user experience as it relates to your APIs can be really costly. You make less revenue and rack up huge load on customer support because almost all your users can barely use your service without needing help.

If you’re interested in making the lives of developers that use your products easier, the following steps might help.

#### **Documentation Is Key**

The documentation is simply the gateway to your product. It contains detailed instructions on how your API can be used, and you don’t want to get it wrong. It should be complete, well-structured so that information is easy to find, and it must contain examples.

Also, all information needed to use your API must be in one place. Your users shouldn’t have to visit different sources just to understand the proper way to call an endpoint.

You should especially avoid sharing API documentation in pdf formats. It introduces more problems than it solves, and you don’t want to get support tickets because the user is trying to consume your API using an obsolete document as a guide.

There are tools available online that allow users to visualize and consume endpoints. It is advisable to leverage these tools for creating and maintaining robust API documentations.

#### Embrace Standard Practices

You’re trying to sell a product. The aim is to attract as many customers as you can while eliminating barriers that might prevent users from using your product.

When you’re trying to get as many developers as possible to use your API, you have no business shipping your own API development standards or patterns. Huge companies with a large customer base can afford to perform this sort of experiment, but even then the results are usually not favorable.

Version your APIs, use correct HTTP methods to perform actions on resources, ensure that your response is well-structured, and return correct status codes depending on the success or failure of a request.

The [OpenAPI](https://www.openapis.org) is one widely accepted spec for designing REST APIs. It is backed by Microsoft, Google, and many other leaders in the tech space.

An even better approach would be to conduct a study or send out surveys to developers that represent your target market. Try to find out which of these specs they adhere to and attempt to tailor your APIs to those.

Developers are less likely to adopt unfamiliar technologies when there are more familiar alternatives. You definitely don’t want to give them any excuse to not use the product you’re offering.

#### Ultra-Active Support Channels

Having several dedicated support channels for handling customer complaints and requests for help is highly important. Software developers want to get swift solutions to blockers they might encounter while consuming your APIs, making response time of utmost importance.

Companies have started moving on from e-mail as the default means of providing support to users because it is just too slow. And, asking developers to send code snippets back and forth through e-mail is one of the best ways to get them to abandon your product.

[Flutterwave](https://www.freecodecamp.org/news/how-ignoring-ux-hurts-your-api-and-what-to-do-about-it-e4f600f9cbfa/undefined) and Twitter have dedicated forums for promptly attending to issues consumers might have with using their products. [Paystack](https://paystack.com/) also has a dedicated Slack group to help out users with issues they might encounter while trying to consume their APIs.

Using real-time communication channels to handle customer support issues is not debatable. Your users are software developers, and it is essential that they get help quickly.

Also, making sure code snippets can easily be shared through whatever medium you chose to handle customer support requests will earn you bonus points from your users.

#### Communicate

A tiny change in your request/response formats can cause considerable damage to your user’s product(s) and entire business. It is very important that you let your users know about planned changes, and provide enough time for them to prepare for these changes. As long as you’re sharing useful and relevant information, your users shouldn’t have cause to complain.

Send emails and follow up emails reminding your customers of that endpoint you’ll be shelving in the coming months. Inform them promptly about security concerns and let them know what to do to be safe.

Let your customers know when they’re using old versions of your product and encourage them to upgrade. Making users aware of the improvements you’ve made is a great way to motivate them to consider an upgrade. Most times, your users just want to be assured that the upgrade contains changes they need.

Every consumer that decides to use your API is doing so because they have a reasonable level of trust in your product’s offering. It is only fair that you repay this trust by effectively communicating with them regarding the state of your product and how best they think you can improve your product in order to serve them better.

#### Conclusion

Product development is hard. Even more so when you’re in the business of creating APIs that will be consumed by software developers.

That said, it is not impossible to create APIs that developers will love to use. It just takes a lot of conscious effort, and I hope these steps will help you in creating web services we’d all love to use.

If you have questions or contributions regarding other steps that might help developers enjoy working with our APIs, kindly leave a comment. I’d be happy to read and respond to them.

