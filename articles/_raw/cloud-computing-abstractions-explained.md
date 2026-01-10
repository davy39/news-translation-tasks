---
title: Cloud Computing Abstractions – IaaS, PaaS, FaaS, and SaaS Explained
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2023-05-16T16:31:36.000Z'
originalURL: https://freecodecamp.org/news/cloud-computing-abstractions-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pictures-2.001-2.jpeg
tags:
- name: abstraction
  slug: abstraction
- name: Cloud Computing
  slug: cloud-computing
seo_title: null
seo_desc: 'Abstracting is the process of reducing something to its most basic form.
  It is the hiding away of the inessential.

  For a drawing, this could be reducing it to its basic lines and shapes. Naturally,
  there are many levels of an abstraction, since what ...'
---

Abstracting is the process of reducing something to its most basic form. It is the hiding away of the inessential.

For a drawing, this could be reducing it to its basic lines and shapes. Naturally, there are many levels of an abstraction, since what is inessential is subjective.

This is illustrated in the image below showing a Greek temple and two drawings at different levels of abstraction.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd8cf1dcb-27a4-42fb-babb-b58fb8c659b3_1628x882.png align="left")

*Example of abstraction*

As you abstract away more of the details of the temple, you are left with something very simple. In its most basic form, a Greek temple can be thought of as a triangle sitting on top of a rectangle with vertical lines going across the rectangle.

Abstractions are everywhere around us. Google Maps is a good example of this. You can have a satellite, roadmap, terrain, traffic, cycling, public transport or street view, among others. Each of these options abstracts away some details, allowing you to focus on what you want to see.

Even a satellite map is an abstraction, since it is a point in time snapshot and cannot capture every new house, tree, or blade of grass.

The key point is that an abstraction simplifies something by **hiding away the underlying details.** It is a way of managing complexity.

But there is always a price to be paid. In exchange for hiding away complexity, you lose some lower level details which often means a loss of control if things go wrong.

# Abstractions in the Cloud

In cloud computing, abstractions are everywhere. When you choose a particular technology to solve a problem, you are implicitly choosing a level of abstraction.

There are four broad levels of abstraction in cloud computing. These are called the service models:

* IaaS (Infrastructure as a Service)
    
* PaaS (Platform as a Service)
    
* FaaS (Function as a Service)
    
* SaaS (Software as a Service).
    

These four broad service models are just a guide for splitting out the different levels of abstraction in cloud computing. You can think of them more like well thought-out opinions, rather than some hard rule of physics.

Some people only consider IaaS, PaaS and SaaS as the service models, ignoring FaaS. Others will include Container as a Service, Security as a Service, Database as a Service, and so on.

The examples can go on and on by simply appending “as a service” to different technologies. This makes sense since you can abstract at different levels, which makes any abstraction of the cloud a spectrum of possibilities.

Just like the Greek temple shown above, there can be many intermediary levels of abstraction between a life-like drawing of the temple and a drawing with a triangle sitting on top of a rectangle.

When you choose to use cloud computing instead of an on-premise solution, you are effectively choosing to abstract away some of the underlying tasks and pieces of infrastructure that you would otherwise need to manage.

The figure below shows the differences between an on-premise solution and IaaS, PaaS, FaaS, and SaaS.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f24811c-1b7f-4c93-b696-b42c5d41d576_1224x1080.png align="left")

*Figure illustrating the differences between an on-premise solution vs IaaS, PaaS, FaaS, and SaaS.*

As you move to the right in the above illustration, you abstract away more of the underlying infrastructure stack. This reduces the complexity of what you are trying to build, since there are fewer things to build and manage.

But the price you pay for this reduction in complexity is a loss of control. Sometimes, that is a worthy price to pay, and sometimes it is not.

## On-Premise Solutions

You are responsible for managing everything in the infrastructure stack, from the physical security of the data centre to the application itself.

In this case, almost nothing is abstracted away. This gives you increased control and flexibility to customise what you want. In exchange for that, you pay the price of managing the entire stack and bearing the risks associated with that.

This is analogous to opening a pizza restaurant, but instead of just renting some space, you build the restaurant from scratch.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0a01e351-835d-4431-8298-de50ef3666d5_1886x1008.png align="left")

*Building a pizza restaurant from the ground up is like managing on-premise solutions*

The upside is you have full control over how the restaurant will look. The downside is the large upfront expenditure you will need to make for plumbing, ventilation, electrical wiring, air conditioning, heating, and so on.

You will also be plagued with questions like “Is the restaurant big enough, or is it too big?” or “How do I expand or scale down based on growing or falling demand?”. Large upfront costs and higher levels of uncertainty are the price you pay for full control.

## **IaaS (Infrastructure as a Service)**

The physical security, data centre infrastructure, networking, servers and virtualisation (the process of creating multiple virtual machines out of a physical server) is abstracted away and managed by the cloud provider.

You are responsible for managing the operating system and everything above it in the infrastructure stack. You still get to customise what virtual machine you want, based on the choices made available by the cloud provider, and you will pay to use the virtual machine on a pay-as-you-go basis.

You don’t have to worry about purchasing more servers or cooling requirements for your servers. All of that is abstracted away and managed for you.

Virtual machines/instances are a good example of IaaS – EC2 from AWS, Compute Engine from GCP, and VMs from Azure.

IaaS is analogous to simply renting some space for your pizza restaurant. The electrical wiring, plumbing, heating, and so on is abstracted away since it is managed by the owner of the building.

You are responsible for paying rent to use the space, hiring chefs, a manager, waiters and cleaners, buying equipment and furniture, choosing decor, building a menu, marketing and getting customers through the door.

Still a lot of work, but all of the non-pizza making activities are hidden away, allowing you to focus on doing what you do best – making pizza.

## **PaaS (Platform as a Service)**

Here, you manage the runtime and everything above it. The runtime is a software environment that provides the necessary resources and services for an application to run. Examples include the Java Virtual machine for Java applications, Python runtime for Python applications, and Node.js for JavaScript applications.

With PaaS, you have abstracted away all of the physical infrastructure. All you need to worry about is your runtime.

Good examples of PaaS are AWS Beanstalk and GCP App Engine. Also, managed database services like AWS RDS and GCP Cloud SQL fall under PaaS.

PaaS is analogous to opening a franchise pizza restaurant. When you open a franchise, you are provided with a pre-built restaurant space, equipment, branding, and a set of processes to follow. You are responsible for the core activities of running the restaurant such as hiring staff, managing inventory, and creating menus.

PaaS works in a similar way, providing developers with a pre-built platform that abstracts away the underlying infrastructure, allowing them to focus on building and deploying applications.

## **FaaS (Function as a Service)**

Here, you manage the functions and the application while the cloud provider manages the rest.

What exactly is a function and how is it different from a runtime? A function is a block of code that performs a specific task, while a runtime is the environment in which that code is executed.

Functions are typically triggered by events such as HTTP requests, database updates, or messages from a queue. When an event occurs, the function is automatically executed, and the result is returned to the calling application.

This is analogous to hiring a freelance pizza chef to cook for you on-demand. When you hire this freelance chef, though, you only pay for the time they spend cooking. The chef starts getting paid in reaction to an event, that is the moment an order comes in, and stops getting paid once the pizza is ready. The rest of the time, the chef is just idle, waiting for the next order but not costing you any money.

Ignoring the corporate sleaze and potential illegality of such a practise, doing something like this will save you money since you are only paying for the duration of a pizza being made.

## **SaaS (Software as a Service)**

Here, you don’t manage anything, but simply consume the service offered. Prime Video, Gmail, and Outlook are great examples of SaaS. When you use these, you don’t care about how the application works. All of that is abstracted away. You simply access the software through a web browser or a mobile app and use as needed.

Drawing on the restaurant analogy, this can be compared to simply ordering a pizza from the restaurant. The restaurant abstracts all the the steps needed to make the pizza.

# Examples of IaaS, PaaS, FaaS & SaaS

The table below shows examples of IaaS, PaaS, FaaS and SaaS offerings from the main cloud providers – AWS, GCP & Azure.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe6ce9fab-512a-4d23-b7f7-0608e3042ec6_1524x970.png align="left")

# Bringing it Together with an Example

If you are building a e-commerce site like Amazon.com, you will need a transactional database to store details about customers like their names, payment details, address, orders, inventories, and so on. How do you choose the right level of abstraction for your database?

You have four options to choose for you database. Starting from the option that abstracts the most from the infrastructure stack:

1. You could choose the use a FaaS option like [AWS Aurora Serverless](https://aws.amazon.com/rds/aurora/serverless/). This automatically starts up the database when it is being used and shuts it down when not in use, allowing you to save money by only paying for when it's in use. This is ideal for an infrequently used database with unpredictable workloads
    
2. You could choose a PaaS option like [AWS RDS](https://aws.amazon.com/rds/). This is a managed database where AWS abstracts away and manages administrative tasks like OS patching, scaling, database backups and other admin tasks that would otherwise require a database admin (DBA) to manage
    
3. You could choose an IaaS option by installing a relational database management system (RDBMS) like MySQL on an EC2 instance. AWS will manage the hardware, but you will be responsible for managing the OS and the database application. So, admin tasks like OS patching, scaling, database backups, among others, will be your responsibility
    
4. You can choose an on premise solution. Here, you will self-host the database and manage the hardware yourself, in addition to all the database admin tasks as described above
    

Which is the right option to choose? First, it depends on your use case and the benefits and tradeoffs you are comfortable with. This is trite but nevertheless true.

However, a good heuristic that will work most of the time for most problems is to focus on what to avoid. You generally want to avoid an extreme or outlier solution, unless the problem you are trying to solve is indeed extreme or an outlier. And most problems, by definition, cannot be outliers.

The FaaS option using Aurora, and the on premise solution are not ideal, unless your use case specifically demands the features that these options posses.

Aurora serverless is not a very popular service, so finding patterns for integration with other technologies or help with troubleshooting technical problems may be more difficult. Also, there can be some technical issues with using a serverless database like Aurora.

For example, waking it up from an idle state in response to a request can sometimes take a few seconds. And this can be a delay long enough to lose a customer on your e-commerce application.

The on premise solution is not ideal either, because an e-commerce application will have fluctuations in demand as a result of holidays, discounts or some product going viral. On premise solutions are bad at handling large fluctuations in demand.

This simple heuristic of focusing on what to avoid yields two acceptable solutions – the IaaS option of running your database on an EC2 instance or the PaaS option of using a managed database service like RDS. Either of these is fine for the use case described.

The key point to remember is that an abstraction simplifies something by **hiding away the underlying details.** It is a way of managing complexity.

The higher abstraction solution of using RDS is the less complex solution, since AWS manages all of the underlying complexities of OS patching, scaling, database backups and other admin tasks. The price you pay for this reduction in complexity is less control of the database and a higher AWS bill.

I hope this helps you choose the solution that's right for you. Thank you for reading!
