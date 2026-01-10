---
title: The anatomy of a Bootstrap dashboard that earns $1,000s each month
subtitle: ''
author: Alexandru Paduraru
co_authors: []
series: null
date: '2017-08-28T14:31:58.000Z'
originalURL: https://freecodecamp.org/news/the-anatomy-of-a-bootstrap-dashboard-that-earns-1-000s-each-month-ed3404010d25
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oNcZnFrvQFeINnPcWVI6VA.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'We at Creative Tim have always wanted to deliver great tools to all the
  web developers who are using our products. If you want to read more about how we’ve
  built our business and what is our drive, you can check this article: Growing a
  side project i...'
---

We at [Creative Tim](https://www.creative-tim.com/) have always wanted to deliver great tools to all the web developers who are using our products. If you want to read more about how we’ve built our business and what is our drive, you can check this article: [Growing a side project into a $17,000 month business](https://medium.freecodecamp.com/growing-a-side-project-into-a-17-000-month-business-46024d2aa87f).

We want to see better websites and web apps on the internet. So we decided to share some of the “secret ingredients” that form the base of one of our most popular dashboards: [Light Bootstrap Dashboard](http://demos.creative-tim.com/light-bootstrap-dashboard/dashboard). Of course, they won’t be a secret anymore, because we’re going to share them with you. ?

In this case study, I will share how we got the idea to create a dashboard, where we got inspiration, how we implemented everything, how it was used inside **Stanford**’s internal tools and how we financed the development and the support of it. Here is an overview of the article:

1. The basic structure and core functionality
2. How the design was created
3. Built on top of open source and why you should stand on shoulders of giants
4. Launch, Rise and Shine
5. How we finance the support and solve the requests of the developers
6. Future development plans

I will try to give as much information as I can, with hopes that this tutorial won’t be like this:

### 1. The basic structure and core functionality

You should think of the process behind creating the dashboard as a test that you have to take after you learn a lot. Of course you will learn a lot during the development of the product. But first, you need to have strong knowledge of what is “that” and how it “is used”. Before writing the first line of code you should do some research, make plans, create to-do lists and sketches, and try to visualize what you will want to have in the end.

Since you are not reinventing the wheel, you need to look around at companies that create great products to get inspiration (such as [Heroku](https://dashboard.heroku.com/), [Slack](https://slack.com/), [Mailchimp](https://mailchimp.com/), [Stripe](https://stripe.com/)). Also look at your competition. You will get a lot of information. And when you start, it will be easier to develop the product because you did your homework. You have to sharpen your ax, before starting to cut:

> “If I had eight hours to chop down a tree, I’d spend six hours sharpening my ax.” — Abraham Lincoln

We did our homework and we’ve got a huge list of over 100 free dashboards as examples from which we can get inspiration. Here are some of them:

![Image](https://cdn-media-1.freecodecamp.org/images/1*xR1NimY3i5LO1lxM9SL2RQ.jpeg)

You have a huge list of dashboards, with a lot of colors, animations, beautiful icons, small charts, big charts, static or fixed sidebar and hundreds of different features. How do you know which is the best option for your audience?

Since we didn’t know what people want inside a dashboard, we decided to write down all the features that these dashboards contain and use only the most common. We realized that the **core features** solve around 95% of the cases where you need a dashboard. The remaining 5% solve very specific problems.

The basic elements are buttons, icons, typography, sidebar, main panel, navbars and dropdowns. The core features in most of the dashboards are:

1. Tables
2. Notifications
3. Tasks Lists
4. Cards (for different type of forms and easier visualization of the information)
5. Charts (donut chart, line chart, bar chart)
6. Google Maps

With small visual adjustments, you can reproduce 95% of any dashboard from any company in the world just by using the core elements. Then you have the remaining 5%, which is always different depending on the company and the problems it solves. Here we can find:

1. [Kanban System Cards](https://en.wikipedia.org/wiki/Kanban)
2. [Drag & Drop](https://en.wikipedia.org/wiki/Drag_and_drop) functionality
3. Timeline components
4. WYSIWYG Editor
5. 8-Level Navigation Sidebar Menu
6. Multi File Uploader + Drag & Drop File Uploader
7. Form X-Editable
8. Morris Chart, Google Chart, Flot Chart, amChart, Flows Chart and many other types of charts
9. And the list can continue to more than 200 features

The problem is that each of these new plugins adds extra CSS, JavaScript or jQuery libraries, and HTML. We’ve built the product on plain HTML, no frameworks or modular tricks, so all the CSS/JavaScript would be in a single file.

Don’t get me wrong, I’m not saying that the features were not good. These are great plugins developed by awesome people. But it wasn’t something that we wanted to have in our simple dashboard.

So we decided to keep the product as light as possible (remember the name?). **Light Bootstrap Dashboard**. And we decided to implement only the features that were solving the core 95%.

![Image](https://cdn-media-1.freecodecamp.org/images/1*G0F-0tf2aAVrevfgCdih0w.jpeg)

### 2. How the design was created

After we made our plan for the elements that the product would have, we had to think of a design that would be outstanding. A user-friendly design that would make people want to have this dashboard inside their content management system. We already had the famous Bootstrap [Get Shit Done Kit](http://demos.creative-tim.com/get-shit-done/index.html). Web developers loved it and it has been downloaded more than 30,000 times. So we decided to use that as the core design for basic elements like Buttons, Navbars, Inputs, etc.

We realized that we need more than that though, to make an impact and to make people badly want our product. We didn’t want to be “another dashboard based on Bootstrap”. **Where do you go when you want great design resource?**

![Image](https://cdn-media-1.freecodecamp.org/images/1*ruqs_QCLXE8wX6XpCufnEg.png)

If you search “[dashboard](https://dribbble.com/search?q=dashboard)” on Dribbble, you will find a lot of incredibly beautiful dashboards and admin panels. Actually, for those who don’t know, [Dribbble](https://dribbble.com/) is like visual cocaine. Check some of these examples made by [Cosmin Capitanu](https://dribbble.com/radium) and [Mike from CreativeMints](https://dribbble.com/creativemints):

![Image](https://cdn-media-1.freecodecamp.org/images/1*JQV190Vy6Yx69mv4sJg7tg.jpeg)
_[https://dribbble.com/shots/1423171-Some-Analytics](https://dribbble.com/shots/1423171-Some-Analytics" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/1*EJeWQQxhA0lRYvao9sqZog.jpeg)
_[https://dribbble.com/shots/1592816-Probability-theory](https://dribbble.com/shots/1592816-Probability-theory" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/1*BG1kjWkGjIoJZoUKE5FO2g.jpeg)
_[https://dribbble.com/shots/1738453-Xonom](https://dribbble.com/shots/1738453-Xonom" rel="noopener" target="_blank" title=")_

Seeing all these beautiful examples made us realize that if we build something like that we will definitely stand out of the crowd. Also, even if the dashboards or the charts are looking very good, they will be very hard or impossible for us to actually code in HTML, CSS and JavaScript. Or they are solving a very specific problem, like the latest dashboard with Body Measurements.

It was impossible 2 years ago, because our level of knowledge and experience with HTML/CSS wasn’t so high. I’m sure that if we‘d like to implement them today, we’d have a good chance of creating something very similar. Also, the technology and browser capacities will help us more.

We wanted to build something that can be used by many people from diverse business fields. There were some simple and beautiful dashboards too, but we didn’t want to use them as inspiration because we wanted something different.

I can’t explain exactly what we wanted, but we didn’t feel comfortable with any of the examples. So we continued to do our research until we found something that we really liked:

![Image](https://cdn-media-1.freecodecamp.org/images/1*5RdaH9YoQG-K-QKHl08Zlg.png)
_Heroku Dashboard in 2015_

It wasn’t perfect nor as outstanding as we wanted it to be. But we felt that it is the right choice and it is a very good example from which we can build our dashboard. Even Pablo Picasso said that great designers steal and Apple respected his word:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Cz3GzYXXv4Hwx23qeXyFBA.jpeg)

We couldn’t do that. The dashboard from Heroku was good enough that it gave us that spark. So we decided to use it only for inspiration and not for the final result. Here is the first iteration:

![Image](https://cdn-media-1.freecodecamp.org/images/1*IqdqX0EyCAfRFbaQ8EC8nQ.png)
_Iteration #1_

It’s a pretty good start. To have a better view of how it will look, we just have to populate the right area with some cards with charts:

![Image](https://cdn-media-1.freecodecamp.org/images/1*Sg4Mv-PM0dPndSRVyC8ldw.png)
_Iteration #2_

The cards’ colors didn’t look so good. They were too bright for how the left sidebar was looking. So we started to test different combinations of colors for the charts and the sidebar.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZGOomWV2jePE1-U1f0t1ng.png)
_Iteration #3_

At this point we realized that we don’t have to keep only 1 color for the sidebar’s background. And we should let our users choose which color they want. We knew that Apple had some beautiful gradients for their Fitness App, so we decided to use those gradients as the base for our future gradients.

We’ve always thought that if we are watching what the best companies in the world are doing in terms of Design and UX, we will set very high standards for our interfaces. In this way, more and more web developers will have free access to high-quality products.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ShULysSXSDmqIhjETzgB-w.jpeg)
_Apple’s Fitness App_

![Image](https://cdn-media-1.freecodecamp.org/images/1*Mf08D8vG-nCAO1nlP_TQYw.jpeg)

While we were doing all these different combinations of colors, gradients, cards and charts we saw that the guys from [Metalab](http://www.metalab.co), who built the interface for Slack, wrote an article: [Slack’s 2.8 Billion Dollar Secret Sauce](https://medium.com/@awilkinson/slack-s-2-8-billion-dollar-secret-sauce-5c5ec7117908#.h63snwe27). This ended up being an inspiration for the next steps. The overall idea of the article was that Slack’s secret sauce is created by the combination of a great and playful interface with small interactions, which makes the product more user-friendly.

> “It looks different, it feels different and it sounds different.”

We wanted to add something that **none of the other dashboards** had. I’ve always loved how a gradient with some transparency can look over an image. And I’ve started to play with different images and gradient’s opacity. By the way, the Duotone Gradient Image that we used in 2015 (we didn’t even know that it has a name) seems to be one of the [trends in web design for 2017](https://thenextweb.com/dd/2016/12/22/web-design-trends-can-expect-see-2017/#.tnw_bdot2Bdf). This is pretty cool, isn’t it? ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*Azvsp9VybyIELu5tujGYmA.png)
_Iteration #4_

Not fully satisfied…

![Image](https://cdn-media-1.freecodecamp.org/images/1*vs9QCRMn4U3sj5BfND-9IQ.png)
_Final iteration_

This was the view that made us feel happy, it was just perfect for us ?. We also added small interactions like the opening dropdown animation or the show effect of the notification:

Adding the image with the gradients over and the small animations made us feel like this guy:

![Image](https://cdn-media-1.freecodecamp.org/images/1*zF1jGXJhQHO7fglF9Rn2tQ.gif)
_[https://www.instagram.com/nusr_et](https://www.instagram.com/nusr_et" rel="noopener" target="_blank" title=")_

### 3. Built on top of open source and why you should stand on the shoulders of giants

As we said in the beginning, we didn’t want to reinvent the wheel. Nor did we have the money to contract experts capable of building the elements needed for the dashboard. We decided that the best option for us is to use what other people created and **shared for free** or **open source**.

We recently discovered that what we actually did was stand on the shoulders of giants. That means we used as much as we could from tools that are already powerful and well maintained by big communities. For more about this and why you should use this technique when you want to build something from scratch read this awesome article, written by [Quincy Larson](https://twitter.com/ossia): [How to stand on shoulders of giants](https://medium.freecodecamp.com/how-to-stand-on-shoulders-16e8cfbc127b#.iyojaorb8).

#### Let’s have a look at what is actually under the hood.

* Framework: [Bootstrap](http://getbootstrap.com/) — Bootstrap is the most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web.
* Design Layer: [Get Shit Done Kit](http://demos.creative-tim.com/get-shit-done/index.html) — Free Bootstrap 3 User Interface Kit. This is the best starting point for any online project you are building. It has become a trademark for the online community of a clean and nice looking interface.
* Font: [Roboto](https://fonts.google.com/specimen/Roboto) — a Google Font that has a dual nature. It has a mechanical skeleton and the forms are largely geometric.
* Small icons: [Font Awesome](http://fontawesome.io/) — Font Awesome gives you scalable vector icons that can be customized using CSS.
* Large icons: [Stroke 7 Icons](http://www.pixeden.com/icon-fonts/stroke-7-icon-font-set) — This is a complete set of 202 thin stroke icons inspired by iOS 7.
* Charts: [Chartist.js](https://gionkunz.github.io/chartist-js/) — Chartist.js is the product of a community that was disappointed about the abilities provided by other charting libraries.
* Notifications: [Bootstrap Notify](http://bootstrap-notify.remabledesigns.com/) — This plugin helps you turn standard bootstrap alerts into “growl” like notifications.
* Maps: [Google Maps](https://developers.google.com/maps/) — Plugin for viewing maps.
* Photos: [Unsplash](https://unsplash.com/) — Free ([do whatever you want](https://unsplash.com/license)) high-resolution photos.

> “There is no such thing as something for nothing. Everything, including your personal success, has a price that must be paid” — Napoleon Hill

Since we used a lot from the community it would be fair to give back to the community. So we decided a couple of weeks ago to release it [under MIT License](https://github.com/creativetimofficial/light-bootstrap-dashboard/blob/master/LICENSE.md). In this way, more developers can contribute and use it without any legal constraints, for personal and commercial projects.

### 4. Launch, Rise and Shine

Doing the research for around 50-60 days (sharpening the ax) gave us the possibility to develop the dashboard in just 15 days (chopping the tree). ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*MjHrLjPnk2DkClh34OB94w.png)

What do you do after you launch a project? You need to see what the feedback for it is, if people would like to use it and if the simple dashboard you created is solving a problem for them. If they don’t want to use it, then, you don’t have a business. We submitted it on different communities and it was doing very well. For example, it got:

* [170 upvotes](https://news.ycombinator.com/item?id=10184982) on Hacker News, peak to position 9 and over 88.000 views for that week
* [247 upvotes](https://www.reddit.com/r/webdev/comments/3jyyye/light_bootstrap_dashboard_an_useful_freebie_for/) on /r/webdev subreddit
* [80 upvotes](https://www.reddit.com/r/webdev/comments/3jyyye/light_bootstrap_dashboard_an_useful_freebie_for/) on /r/web_design subreddit (blocked at 80 because it got the “spam” tag, we had some subscribe popups… which we later removed?)

![Image](https://cdn-media-1.freecodecamp.org/images/1*s2t5EiBh6omkaJVO1dJEKA.png)

The community validated the idea. We’ve also got a lot of feedback, to add the SASS files for easier customization or post it on GitHub.

Then we’ve seen that there were a lot of beginners who just wanted to learn how to use this dashboard. It was so beautiful that people who didn’t interact with something like that wanted to learn how to work with it.

We spent around 3 weeks developing a series of video tutorials on how to replicate the WordPress dashboard using our product. We chose to use the WordPress dashboard because it is a very popular dashboard. And we wanted to let people understand that they can build anything using our product.

The tutorials were very well received and have over 78,000 views as of today. Here is the first video on [How to create a responsive admin template using Light Bootstrap Dashboard 1/3](https://www.youtube.com/watch?v=c3M3NQtFyqM).

### 5. How we finance the support and requests from the web developers

![Image](https://cdn-media-1.freecodecamp.org/images/1*ozYKavzDtpbWrnOw34kKBg.jpeg)
_[https://youtu.be/sz_LgBAGYyo?list=PL5q_lef6zVkaTY_cT1k7qFNF2TidHCe-1](https://youtu.be/sz_LgBAGYyo?list=PL5q_lef6zVkaTY_cT1k7qFNF2TidHCe-1" rel="noopener" target="_blank" title=")_

Building a product it easy, keeping it alive is hard.

There are a lot of great plugins/template out there which are dying because their creators don’t have enough cash or they don’t make enough revenue in order to continue the development or to fix the issues.

We didn’t want the same case for our product. The best option to keep the product alive was to create a PRO version which can generate enough revenue to support to continuous development.

We used the feedback from web developers and decided to create a Premium version with more elements and plugins. We wanted to help also some of the guys who wanted specific features and were in the 5% category. Choosing the right plugins which can help as much as we could from the 5% category was very hard for us.

We started again to do research on the premium dashboard. And we added plugins like [Full Calendar](https://fullcalendar.io/), [DataTables.net](https://datatables.net/), [Sweet Alert](https://limonte.github.io/sweetalert2/), [Bootstrap Wizard](http://vinceg.github.io/twitter-bootstrap-wizard/) and some extra pages like [Login Page](http://demos.creative-tim.com/light-bootstrap-dashboard-pro/examples/pages/login.html), [Register Page](http://demos.creative-tim.com/light-bootstrap-dashboard-pro/examples/pages/register.html), [Lock Page](http://demos.creative-tim.com/light-bootstrap-dashboard-pro/examples/pages/lock.html).

![Image](https://cdn-media-1.freecodecamp.org/images/1*D8XWOYaGPt019gwke0EiCg.jpeg)

Here is the [live preview](http://demos.creative-tim.com/light-bootstrap-dashboard-pro/examples/dashboard.html) of the PRO version. You will see that we kept the same structure and wanted to make it light, without too many options and features.

Having the revenue from the PRO version made us not only support the product but also create new file types like the [PSD/Sketch version](http://www.pixelsvibe.com/product/light-dashboard) or [Angular 2 version](https://www.creative-tim.com/product/light-bootstrap-dashboard-angular2). Both are shared for free.

### 6. Future development plans

Here are some stats about the dashboard:

![Image](https://cdn-media-1.freecodecamp.org/images/1*el4d2GAaEt9A9yTJrrpA8Q.jpeg)

It is very easy to customize it to match your brand. It was used in internal tools like Stanford’s Department of Emergency Medicine Catalog:

![Image](https://cdn-media-1.freecodecamp.org/images/1*fJgKUWlS4RBv_OXME1wLAQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*99B_ST6PqMpj6DhNf7fX0Q.png)

We’ve got many requests from web developers who want to have the Dashboard built on different frameworks like [Angular 2](https://angular.io/), [Angular CLI](https://cli.angular.io/), [React](https://facebook.github.io/react/), [Meteor](https://www.meteor.com/), [VueJS](https://vuejs.org/) or as a Rails Gem. Creating all these versions and supporting them for free under MIT license will work only if we will have PRO versions for each one. We started with Angular 2 and we’ve seen a lot of people who use it and we’ve got a lot of feedback on how to improve it. So if you want to get involved for the other frameworks or if you have any ideas on how to make these products better, we would be glad to talk more.

![Image](https://cdn-media-1.freecodecamp.org/images/1*poZ5puqDlTWowjhJrdLwMg.jpeg)

It took a lot of courage to show our sources and the process that we had behind building [Light Bootstrap Dashboard](http://www.creative-tim.com/product/light-bootstrap-dashboard). Hope you will learn something from this and if you have any feedback or suggestions, I would be glad to talk to you in the comments.

Useful links:

* Download HTML version from [www.creative-tim.com](https://www.creative-tim.com/product/light-bootstrap-dashboard)
* Download Angular version from [www.creative-tim.com](https://www.creative-tim.com/product/light-bootstrap-dashboard-angular2)
* Download PSD/Sketch version from [www.pixelsvibe.com](http://www.pixelsvibe.com/product/light-dashboard)
* Play with it on the [live preview](http://demos.creative-tim.com/light-bootstrap-dashboard/dashboard)
* Contribute and report issues on the [GitHub repository](https://github.com/creativetimofficial/light-bootstrap-dashboard)
* Check our blog: [http://blog.creative-tim.com/](http://blog.creative-tim.com/)

Find me on:

* Email: [alex@creative-tim.com](mailto:alex@creative-tim.com)
* Facebook: [https://www.facebook.com/axelut](https://www.facebook.com/axelut)
* Twitter: [https://twitter.com/axelut](https://twitter.com/axelut)

