---
title: Amazon Web Services (AWS) explained by operating a brewery
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-31T00:09:02.000Z'
originalURL: https://freecodecamp.org/news/amazon-web-services-aws-explained-by-operating-a-brewery-8f1e91eacc40
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QGoJbSOAuIoW-bkOxyY8iQ.jpeg
tags:
- name: AWS
  slug: aws
- name: education
  slug: education
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Kevin Kononenko

  If you understand how a brewery works, then you can understand Amazon Web Services
  (AWS).


  _Photo by [Unsplash](https://unsplash.com/photos/5sAzXev5-jA?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopen...'
---

By Kevin Kononenko

#### **If you understand how a brewery works, then you can understand Amazon Web Services (AWS).**

![Image](https://cdn-media-1.freecodecamp.org/images/1*QGoJbSOAuIoW-bkOxyY8iQ.jpeg)
_Photo by [Unsplash](https://unsplash.com/photos/5sAzXev5-jA?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Elevate</a> on <a href="https://unsplash.com/search/photos/brewery?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

When you are working on building your first web app, you ALWAYS hear about the ease of launching a new product compared to past years.

People will say things like, _“Back in my day, you had to buy your own server and configure it yourself!”_

Or, _“We would stay up all night debugging the latest issue with our server infrastructure.”_

Fortunately, those days are long gone. You can deploy your new web app for $10 a month within an hour, if you know what you are doing.

But, there is one small problem. Standard tools like Amazon Web Services (AWS) can be pretty complicated, at least to a newbie. Although they offer the incredible ability to scale from your first users to hundreds of millions of users… they also require some configuration.

I wanted to learn about all the major options that AWS offers. After thinking about it for a few hours, I realized that the AWS ecosystem is similar to all the different parts of a large-scale brewery.

Here’s a quick preview:

![Image](https://cdn-media-1.freecodecamp.org/images/0*vdBGfOwhkhaQ2lTd)

So, here is how 5 popular AWS tools work behind the scenes of a web app. I’ll also explain [Heroku](http://heroku.com/), a popular tool for deploying web apps that offers less flexibility but is easier to get started with.

The official video from AWS gives some context about the tools we will be discussing:

In order to understand this tutorial, you just need to understand the concept of the [client-server model](https://blog.codeanalogies.com/2018/02/02/localhost-explained-by-trying-to-start-a-microbrewery/), which you can [learn more about here](https://blog.codeanalogies.com/2018/02/02/localhost-explained-by-trying-to-start-a-microbrewery/).

#### The Context of Amazon Web Services

Let’s imagine that you are passionate about brewing beer. You start in your kitchen by brewing for yourself and friends. Soon, word escapes about your delicious work. In order to meet the growing demand, you decide to rent some equipment and space in a warehouse to see if you can create a full-blown company. You will take orders from distributors, restaurants, and independent businesses.

![Image](https://cdn-media-1.freecodecamp.org/images/0*2zJ-RgXq4mX3eN-t)

In the example above, an order comes in from a **client** — one of the restaurants or distributors. That’s called a **request**. Your brewery will provide the order and collect payment via an invoice. That’s called the **response**.

Similarly, web browsers send requests to servers based on actions taken by users. The server returns the required information via a response.

![Image](https://cdn-media-1.freecodecamp.org/images/0*MsF4PEVc5qVit5Xc)

This is just a high-level view, of course. We are going to dig into all the different processes that happen on the **server side** in our exploration of AWS. In our brewery analogy, we are assuming that the orders are already coming in left and right. It is now our job to organize a whole brewery so we can deliver those orders reliably.

### Heroku Explained — A Much Simpler Alternative to AWS

Before we get into the 5 parts of AWS, you probably should know about the simpler alternative. Heroku manages many of these systems for you. In fact, it is built on top of AWS infrastructure.

Heroku allows you to deploy new versions of your app straight from your command line using _git push heroku master_. It also has a [rich library of add-ons](https://elements.heroku.com/addons) that allow you to add new functionality to your _dynos_, or virtual servers.

Heroku is kind of like hiring a 3rd party contractor to manage your brewery. All you need to do is provide the recipes, and this contractor will use their expertise in brewery operation to produce the beer. They provide the team, the equipment, and relationships with suppliers.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ho0-aZixv74gV3-v0RbTyA.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*dosvXrcjnrJ9UetnJVZTyw.jpeg)

This may feel miraculous. Now you can skip all that painful time and energy that you would need to spend on learning how to run a brewery! But there are two reasons to be cautious.

1. This approach will be more expensive. You are paying the firm for their expertise alongside the cost of salaries, raw materials, etc.
2. They may not scale up like you would like them to. Let’s imagine that you start receiving millions of dollars in orders, and you need to grow your operation. They may not be prepared to scale as quickly as you are.

Heroku has the same pros/cons. It is a little more expensive but allows you to get started immediately. If you scale up, you may need to migrate your services to AWS, which will mean that you will need to learn the AWS system anyways.

With that, let’s get into the different tools within AWS.

### AWS Storage Tools

This is the first of three categories that are going to seem similar, so buckle up! Within our brewery, there are plenty of **static assets** that do not change but are necessary for any type of brewing. Think about the machinery, the assembly line or the power tools that the workers use. You cannot take these items apart and recombine them. But, they can be used over and over again and still be useful.

This is kind of like [Amazon S3](https://en.wikipedia.org/wiki/Amazon_S3). S3 is the cloud service that allows you to store static assets like images. It stands for Simple Storage Service.

![Image](https://cdn-media-1.freecodecamp.org/images/1*e9abmVhUIIGeLSkYlbHb6Q.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*n053ea_uJrzL4Wb0kBmp8A.jpeg)

The concept of “storage of static assets”, in this case, is a little different than what you might think about in real life. In real life, storing static items might mean putting something in an attic and forgetting about it. But when it comes to cloud services, it means preparing an object or image to be used within milliseconds.

This is different than database storage, because data in a database can be **queried**. Static assets can only be **requested**.

### AWS Database Services

Amazon Relational Database Service (RDS) allows you to set up and operate your relational database within AWS. Some common examples include MySQL, PostGreSQL and Microsoft SQL Server.

In our brewery example, this is kind of like the parts of the brewery that store bottles, labels, hops, malt and any other ingredients you will need to make the beer. And I guess it would also include your company bank account, since that is a form of dynamic storage.

You might be wondering why we are discussing storage AGAIN after the previous section. It’s because all of these elements are much more dynamic- they are being constantly combined or modified to handle requests from the users/customers.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ci_kNJOcrUCpn0mcW6VHqg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*wWmbObMp__nfxL14zzW3cQ.jpeg)

This is the type of data that you will **query**, rather than request, like in the previous example. If you were managing the databases for Facebook, for example, this would be user data and posts that would later be included in the News Feed.

One more final note: this data (or hops/malt/bottles) is only useful for actually delivering a response to the user. If you wanted to measure your brewery’s performance, you would need to set up a new process for your operations team.

Imagine if your operations team was frantically running around your brewery, trying to keep track of your performance while the normal workers were trying to produce and bottle as much beer as possible. These two teams have separate interests.

That is where the data warehouse comes into play.

### AWS Data Warehouse Tools

Let’s make one thing clear here: “data warehouse” is a terrible name for cloud service. Okay sure, it might make sense to a developer with years of experience, but to a newbie… how many things in web development are similar to a warehouse? MANY.

One common example of a [data warehouse product](https://en.wikipedia.org/wiki/Data_warehouse) is [Redshift](https://en.wikipedia.org/wiki/Amazon_Redshift). These types of tools make it easy for developers to analyze their data. They include data from relational databases, as well as ERP, CRM and marketing automation data.

Let’s return to our brewery analogy. So far, in our brewery, all of our “data” is not in a very accessible form. It’s in the format of bottles, hop bags and whatever other raw materials are lying around the facility. An analyst would need to manually count all of these physical items if they wanted to analyze the factory’s efficiency.

You need a way to convert that physical data into machine-readable data, which your ops team can use to make the brewery more efficient. Think of it like a sensor system around the facility. The sensors convert the physical movement of raw materials into machine-readable data, which can later be analyzed.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EySamZAufAFciP0g2y3U8g.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*AtoYuA5nKYjrwlOEBNL0gQ.jpeg)

So now, as our factory operates, data is automatically collected and shared with the factory ops team so they can analyze efficiency.

See how this reduces stress on both the factory and production team? The production team can focus on making beer on the floor while the operations team can analyze from their office. This is a good reason to use a data warehouse tool as well. It reduces the number of queries on your database, which can slow performance.

Hopefully, you see why “data warehouse” tool is slightly misleading. Yes, this does create a new dataset strictly for analysis. But, it is hard to tell why it is more “warehouse-like” than any other part of the system.

### AWS Computing Tools

In all of the diagrams so far, have you noticed that “brewery” is in the middle, regardless of whether the diagram shows an actual brewery or a cloud computing environment?

That is because we haven’t yet covered the service that ties this all together: [EC2, or Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html). EC2 allows you to launch virtual instances, which are kind of like the brewery in this analogy.

Instances are **virtual servers**. Unlike previous technologies, where your code was tied to one physical server, virtual servers allow you to launch your own environment in the cloud, which is composed of many connected servers. This is the part that ties all the other AWS services together.

It’s kind of like being able to start up or shut down a new brewery at any time in any part of the world by copying your existing brewery. That may not be possible in real life, but it is possible in the AWS ecosystem. EC2 provides similar functionality to both the physical space and the workers in the brewery.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TbPj10B8QH10Dx_tiIC-Iw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*l0y3g0gR4MUX7O8t5HhVvA.jpeg)

The diagram may be slightly misleading, because a virtual server does not take up a whole server. It exists within a network of servers. But that was too complicated to show in a small diagram. So I kept it.

### AWS Management Tools

The final category of tools is management tools, like Elastic Beanstalk or CloudWatch. These tools can:

1. Monitor other tools listed above
2. Set up processes to help tools from multiple categories work together

![Image](https://cdn-media-1.freecodecamp.org/images/0*V5AvyPtgGhHLXZF2)
_Image Cred: FreeCodeCamp_

In the graphic above, you can see how many tools can help with deploying and maintaining your app. That’s why these tools are similar to the company’s management team. They are not personally producing beer for your company, but instead, they help all the divisions work together.

There is a wide variety of tools in the management category, so I am not going to cover any individual one in depth. They sit at a level above the other tools discussed.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8hrWANJasTDpQaERaaF-aQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*d_Kx52WUCIS0tYPVGHm18Q.jpeg)

### Get The Latest Visual Tutorials

Did you enjoy this tutorial? Give it a “clap”, or sign up here to get my latest web development explanations.

