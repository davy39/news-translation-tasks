---
title: How to Deploy Changes to an Application – Deployment Strategies Explained
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2023-04-26T14:41:00.000Z'
originalURL: https://freecodecamp.org/news/application-deployment-strategies
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/cover-2.png
tags:
- name: deployment
  slug: deployment
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'When deploying changes to an application, there are several strategies
  you can use.

  In this article, I''ll explain the different strategies with an analogy, and then
  we''ll analyze the benefits and tradeoffs.

  Deployment Strategies

  Imagine you are the m...'
---

When deploying changes to an application, there are several strategies you can use.

In this article, I'll explain the different strategies with an analogy, and then we'll analyze the benefits and tradeoffs.

# Deployment Strategies

Imagine you are the manager of a popular pizza restaurant that is open 24/7 for deliveries. This restaurant has two chefs working in the kitchen and both are needed to ensure orders are fulfilled on time.

You have a new special recipe that will change how all pizzas are made. This new recipe involves using a different dough to make the pizza bread, using a different type of cheese, new toppings on the pizza, and changes to the pizza oven settings.

These are significant changes that you hope will lead to more delicious pizzas being made, which equals happier customers, which hopefully translates to more money.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc75206fe-9d56-48ce-9309-58d6772389df_2248x1492.png align="left")

This new recipe is quite complex and will take an hour for a single chef to learn. How do you teach the chefs this new recipe? Remember that this restaurant must be open 24/7. Your approach will be based on whether you are trying to:

* reduce the time it takes for both chefs to learn the new recipe
    
* ensure you have enough chefs to fulfill orders while once chef is learning the new recipe
    
* keep costs low during the recipe change
    
* be able to quickly revert back to the old recipe
    
* test the new recipe with a small subset of your customers
    

You would make a similar set of trade-offs when deciding on an application deployment strategy. Do you want to:

* minimise deployment time
    
* have zero downtime
    
* ensure capacity is maintained
    
* reduce deployment cost
    
* be able to rollback or easily revert changes
    
* test the change with a small subset of your users
    

The trade-off comes because you can’t have it all. As an example, having zero downtime, ensuring capacity is maintained and having the ability to rollback comes at the price of a longer deployment time and higher cost.

I'll explain the logic behind this example using the blue/green deployment strategy example. Ultimately, there are no solutions, only trade-offs.

We'll use a three-tiered web application as the example architecture for the different deployment types. This consists of a presentation, logic, and database tier as shown below.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f739c67-e79c-4995-b58d-71d695cccd47_1018x1682.png align="left")

*Example application architecture*

The presentation tier is responsible for presenting the user interface to the user. It includes the user interface components such as HTML, CSS, and JavaScript.

The logic tier is responsible for processing user requests and generating responses, by communicating with the database layer to retrieve or store data.

The database tier is responsible for storing and managing the application's data and allows access to its data through the logic tier.

## All At Once Deployment

In this type of deployment, you make changes to all instances of an application at once. In the three-tiered web application architecture, an all at once deployment that makes changes to the UI will take both instances in the presentation tier out of service during the deployment, as shown below.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa03758ef-ff46-49c7-9d7b-22596c842240_1018x1682.png align="left")

*Illustration of all at once deployment strategy*

This type of deployment has some pros:

* deployments are fast
    
* deployments are cheap
    

And some cons:

* downtime during deployment
    
* a failed deployment will have further downtime since you will need to rollback by deploying the previous version of the application to the instances
    
* rollbacks are manual
    

An all at once deployment is ideal in a situation when a deployment needs to be made quickly. It is also ideal for situations when there is a low impact of something going wrong. So for example, deployments in non-live environments like development and test environments, that don’t have any real users.

Any use case where the cons listed above are not acceptable would be an anti-pattern for an all at once deployment.

An all at once deployment is analogous to the two chefs being told to stop taking new orders as well as stopping any orders they were currently working on to learn the new pizza recipe. Then they would use that that recipe going forward.

While they are learning the new recipe, orders will go unfulfilled. If they can’t quite get to grips with the new recipe, any pizzas they make will also not be as good, will take longer to make, or both.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99f3efd5-9f11-4d90-9730-69bcbac1ffa4_1628x1080.png align="left")

Also, if you later found out that customers do not like how the new pizza's taste, you have to revert back to the old recipe. This means restocking your kitchen with the previous dough and cheese you used and getting rid of the new toppings.

This is not an ideal way of making a recipe change as you can lose customers if they don’t like the taste of the pizza.

On the plus side, this approach is cheap, in terms of up front cost at least. If it goes wrong, it can be very expensive as a result of lost future sales and upset customers.

It is also fast to implement. If it takes each chef an hour to pick up the new recipe and you show them both at the same time, the new recipe can be ready to go live in an hour.

## Rolling Deployment

In a rolling deployment, you make changes to an instance or a batch of instances at the same time. In the three-tiered web application example, UI changes will first be deployed to one instance and once that is complete, it will be repeated on the other instance.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76e9f8f4-c652-4eab-9bbc-7854aa7df6da_2276x1812.png align="left")

*Illustration of a rolling deployment strategy*

With this approach, you avoid downtime as changes are only made to one instance at a time. The drawback is that deployments will naturally take longer since you have to wait for the first deployment to finish before deploying to the second instance.

Bringing back the chef analogy, the new recipe will only be shown to one chef at a time. This means a reduced capacity to deal with orders, but orders will still be fulfilled since there will always be at least one chef available.

## Rolling with Additional Batch Deployment

This is similar to a rolling deployment, but an additional instance is added into the cluster during the deployment to maintain capacity, as shown below.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea5df353-96ed-45e9-b96d-33a0a6dbae67_2588x1330.png align="left")

*Illustration of rolling with additional batch deployment strategy*

First you **launch** a new instance and then **deploy** the new application there. After the deployment is successful, you **terminate** an instance running the older application.

These three steps of launching a new instance, deploying the new application there, and terminating the old instance are repeated until you have deployed the new application on all the instances.

The key point to note with this approach is that by adding a new instance with the new application version before terminating any instances, you are always maintaining capacity. If you need two instances running at the same time, this deployment strategy will ensure you always have two instances available. This is useful for applications that require high availability.

With this approach, some users will be routed to different instances during the deployment. This means customers will see different UI on the web page – some will see the old, others will see new UI while the instances are still being updated.

If a consistent user experience is absolutely necessary for all your users at all times, this deployment may not be right for you.

The rolling with additional batch deployment is analogous to hiring an extra chef to show the new recipe to while the two existing chefs still fulfill pizza orders. Once this new chef is familiar with the new recipe, orders are routed to him and one of the existing chefs. The third chef is then told to go home.

This is repeated until both chefs in the kitchen are new and familiar with the new recipe. But while this transition is happening, there are always a minimum of two chefs who can fulfil pizza orders in the kitchen.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff0d5d9c1-5e64-495b-97da-124c7943b652_1860x598.png align="left")

## Canary Deployment

The phrase ‘canary in the coal mine’ originates from an old practice in coal mining where miners would take a canary into the coal mine as an early warning alarm.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3da625e7-f768-440e-9850-a003fd3acb08_520x876.png align="left")

Canaries are highly sensitive to toxic gases like methane and carbon monoxide, which humans can’t easily detect, as they are odorless and colorless. The canary dying was a signal to evacuate the mine, since dangerous levels of toxic gases had built up to levels high enough to kill the bird. This was an effective, albeit brutal way of signalling potential danger to the miners.

In canary deployment, a separate set of instances will have the new application deployed on them, and a small percentage of all visitors will be routed to the new version. This can be done with the [weighted routing option using Route 53](https://lightcloud.substack.com/i/64925113/weighted-routing) (managed DNS service from AWS). With weighted routing, you can specify a weight for each target load balancer.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a074098-b40f-4f17-aeb2-b5d0c9a2a961_1124x1080.png align="left")

*Illustration of the canary deployment strategy*

In this example, Route 53 will initially point 90% of all users to the old application and 10% to the new application. The new application will then be closely monitored to see metrics like error rates, response times, and so on. If any issues arise with the new application at this stage, then the weights are simply updated so that all traffic points back to the old application.

Just like the canary in the coal mine, the initial monitoring on a small set of users serves as a cheap signal to give you confidence to either continue the transition to the new application, or revert back to the old.

For critical applications that cannot afford any downtime or other issues, this is an effective way of managing the risk of a new deployment while being able to immediately revert back to the old application.

If everything looks fine with the new application during the initial testing with a small number of users, then you can slowly increate the percentage of users routed there. As you gain confidence in its performance, you can eventually route all users to the new application and terminate the old instances

## Blue/green Deployment

Blue/green deployment involves creating two identical environments: a "blue" environment which hosts the current version of the application, and a "green" environment which hosts the new version of the application. This is shown in the image below:

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea56e413-b77d-4439-848e-c733bcab0c26_1852x1766.png align="left")

*Illustration of blue/green deployment strategy*

Once the new version of the application is deployed to the green environment, the Route 53 DNS record is updated to only point to the load balancer of the green environment in front of the presentation tier, as shown below. The instances of the presentation tier in the blue environment can also be stopped to save cost. You can restart them again when there is a new version of the application to deploy.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff6caffdc-d822-410d-889c-f5212c80a6c5_1852x1760.png align="left")

*Example of blue/green deployment with presentation tier instances in separate environment*

In this example of blue/green, only the instances in the presentation tier are in a separate environment.

But you could have an identical copy of the blue and green environments across all tiers. This would make it so that if you were making changes to the logic or database tiers of the application, there would also be no downtime during deployment, with the ability to easily rollback. You can see that scenario below:

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6329476-8072-44a9-9228-d452c14df946_1852x1794.png align="left")

*Blue/green deployment with no downtime and easy ability to roll back*

The main benefit of blue/green deployment is zero downtime during deployments, since all you have to do is update the DNS record to point to the load balancer of the ‘green’ environment.

Blue/green is similar to canary deployment, but instead of initially sending a small percentage of users to the new version of the application, all users are sent to the new version once it is deployed and thoroughly tested. There is no live testing with real users in a blue/green deployment.

Blue/green deployment is analogous to having two restaurant branches, each with two sets of chefs there. The ‘blue’ restaurant uses the current pizza recipe and all takeaway orders are at first routed to this restaurant as shown below.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1c339e6d-d970-4639-b794-71bc4b3b95c0_1456x852.png align="left")

The ‘green’ restaurant has perfected the new recipe and is ready to receive orders. Customer orders are then routed to this restaurant as shown below.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12fa5167-f6fb-4711-b195-f0d458b0afdc_1456x852.png align="left")

If customers complain about the delivery time or quality of the pizza (which shouldn’t happen if the new recipe has been tested with real customers beforehand), the manager can simply route the orders back to the blue restaurant making the old recipe. Then they can figure out what went wrong with the new recipe, make some tweaks, and try again.

# Bringing it Together

The right deployment strategy for your application depends on what you are trying to optimise for.

All at once deployments are ideal is you want to minimise deploy time and upfront cost. The price you pay, however, is application downtime, with further downtime if the deployment fails (as well as a manual rollback process).

Rolling deployments will take longer to deploy than an all at once deployment. However, there will be no downtime since deployments are made incrementally on an instance or a set of instances. But there will be reduced capacity during deployment, so this may not be ideal for an application that requires high availability.

Rolling with additional batch deployment addresses the issue of reduced capacity with a rolling update. An additional instance or batch of instances with the new version is added to the cluster in order to maintain the same capacity. Only then are instances running the older version of the application terminated.

Canary deployment has no downtime and no reduced capacity during deployment. It is also safer as it allows for testing with a fraction of the users and closely monitoring performance before gradually routing all users to the new version.

But this does not come for free. Additional infrastructure is required. Also, detailed monitoring and observability of the application has to be in place. This means it is more expensive and more complex to deploy using this strategy.

It is important to caveat ‘more expensive’. This approach will incur higher upfront costs, but for a critical application with lots of users that cannot afford any downtime, it could be more expensive (through lost future revenue, unhappy customers or a ruined reputation) to use another deployment strategy that is ‘cheaper’ but ultimately less robust to failures.

Finally, blue/green is ideal for zero downtime deployments that are easy to rollback. It however requires additional cost for a separate set of identical infrastructure to be provisioned.

Thank you for reading!
