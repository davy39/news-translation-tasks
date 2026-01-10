---
title: How to Optimize your AWS Cloud Architecture Costs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-15T18:45:44.000Z'
originalURL: https://freecodecamp.org/news/cost-optimization-in-aws
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/bram-naus-n8Qb1ZAkK88-unsplash-1.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: Cloud Services
  slug: cloud-services
- name: optimization
  slug: optimization
- name: software architecture
  slug: software-architecture
seo_title: null
seo_desc: 'By Sumeet Ninawe

  In this article, I''ll highlight what I mean by optimizing your costs in AWS cloud
  architecture. Then I''ll share how you can do it with respect to the AWS Well-Architected
  framework.

  The Problems of Maintaining IT Architecture

  The tra...'
---

By Sumeet Ninawe

In this article, I'll highlight what I mean by optimizing your costs in AWS cloud architecture. Then I'll share how you can do it with respect to the AWS Well-Architected framework.

## The Problems of Maintaining IT Architecture

The traditional maintenance of IT infrastructure was not very, hmm, efficient? I don't really have the words to describe this issue, mostly because I'll never understand the pain of handling on-prem data centers. 

But it involves provisioning the infrastructure, installing the OS and applications, configuring networking in a web of cables, constantly monitoring performance, and much more.

Imagine the effort required just to keep these data centers running – the procurement, the operations, building special facilities to keep the servers running, disaster recovery, and so on. It can take weeks if not months to scale this traditional infrastructure. 

This kind of situation also influences the development of applications. Older applications were often built as monoliths and the overall risk of failure was high. What was your business again?

## How Cloud Computing Helps

The emergence of cloud providers like AWS has changed this equation altogether. Imagine not having to do all of the above by yourself. Instead, a team of experts does it for you at a cost. 

Cloud computing does just that. It has also introduced new ways for applications to be built. Applications that are developed using cloud capabilities are called cloud-native applications.

As I mentioned earlier, all of this comes at a cost. But if you compare those costs with the way traditional infrastructure was handled, it's still cheaper. 

Still, that’s not all – it could be even cheaper if you manage your cloud services wisely. Cost Optimization is one of the pillars of an AWS Well-Architected Framework. This describes ways the costs can be optimized, not just by building cloud-native applications, but also other organizational aspects.

Cloud resources are scalable, easily managed, advanced, reliable, secure, cost-effective, and highly available. You don’t need to provision and pay for high-performing virtual machines from the beginning to manage a few traffic surges early on. This would be a typical lift and shift scenario. 

## Calculate Your Cloud Costs

If you are new to the cloud or are planning to migrate your existing workloads to AWS, AWS provides a nice service to calculate Total Cost of Ownership (TCO). It compares on-prem deployment with the costs which you would have to pay in the cloud. 

The TCO calculator considers aspects like storage costs, network costs, server costs, and operational costs. It also provides you with an estimate for a lift and shift arrangement.

Estimations provided by TCO calculators can be further reduced by implementing below cost optimization pillars in cloud architectures, like:

1. Rightsizing
2. Increased elasticity
3. Choosing the right pricing model
4. Matching the demand
5. Measuring and monitoring

## Cost Optimization Checklist

### Rightsizing

It is very important to understand the capacity requirements of your application and its functions. Guessing the capacity usually results in a mismatch – we end up provisioning less which might cause us to lose customers, or we end up provisioning more where we end up paying for more than we need. 

As a general rule, you should start small and monitor your usage for a while to establish a trend. Based on the trend you can scale out and purchase reserved instances or capacity which can help save computing costs up to 75%.

### Increased elasticity

To accommodate occasional traffic surges automatically, it is important to implement elastic cloud architecture. This allows auto-scaling groups to scale in and scale out based on your needs. This is where you match the capacity to the demand. 

Of course, this is not possible without monitoring your current usage. Monitoring helps you understand the compute requirements over time and allows you to define thresholds. You can use events which are generated this way to take scaling action.

### Choosing the right pricing model

Every service offered by AWS comes with a pricing model. In the case of computing and storage, AWS offers various types of pricing models that, in essence, define the terms of managed services. 

In the case of EC2 instances, the pricing model defines the availability and access at various levels. For example, on-demand instances can be created and destroyed anytime. On the other hand, reserved instances are fixed long-term instances that result in a cheaper expenditure. 

There are other pricing models as well, like Spot instances, Dedicated instances, Dedicated hosts, and more.

### Matching the demand

AWS Auto Scaling can be used to match the demand so that you pay less for periods when you're not active and only pay for times when demand surges. Over that period, you can also use reserved instances to further reduce your costs by committing to the long term. This is one example of cost optimization.

Moving to the cloud also calls for a cultural change in organizations, especially when it concerns cost optimization. Teams should be made aware of how the cloud works and what managed resources should be used in various scenarios. 

You can form a Cloud Centre of Excellence (CCoE) to work across verticals to monitor and suggest better ways of implementing the Cost Optimization principles below.

1. Define and enforce tagging
2. Effective account structures
3. Design and use metrics
4. Design cost-based architectures

## The Importance of Tagging

To deal with costs and answer expenditure-related questions, you should perform tagging as a best practice. Tagging of resources allows us to have greater visibility and more granular control over our cloud expenditures.

Standard tagging formats should be defined and enforced for each organization while creating cloud resources. The format may define aspects like the project, portfolio units, teams, and so on at an organizational level.

Going deeper, project-based conventions can also be defined to represent services supported by various cloud resources. However, be aware of the number of tags you choose – there shouldn’t be too many or too few tags defined. In general, tags can be categorized into two groups:

1. **Technical –** representing technical details like automation, security, and so on.
2. **Strategic –** representing organizational details like a cost center, access control, governance, and so on.

## How to Track Your Cloud Computing Costs

There are a number of ways you can keep track of what you're spending on cloud computing. Let's look at the main ones now.

### Cost Explorer

AWS provides a few highly useful services like **Cost Explorer** that gives you insight into your cloud spending over time. It offers a nice visual interface representing monthly or daily costs. It also gives you a default dashboard representing the monthly costs incurred per service.

AWS Cost Explorer helps you generate and export cost reports at a high level as well as granular and specific reports. You can build your reports and dashboard based on your interests and focus.

Cost Explorer helps you set budgets which helps monitor your costs. Budgets are a great way to keep your costs under control. Using budgets, you can define an expenditure baseline in AWS and set up threshold breach notifications.

For example, if the costs exceed more than 80% of the baseline budget, you can opt to get a notification which will then help you take action.

Cost Explorer also gives you rightsizing recommendations which help you identify where you might be provisioning more than the required infrastructure in terms of instance type, pricing model, and so on.

### QuickSight

If you need a more detailed reporting tool, AWS offers its **QuickSight** service. It is a business analytic solution for cost reporting. It is fast and highly scalable and includes ML capabilities.

You can explore, analyze and collaborate on cost expenditure topics in a much better way. However, this is not a free service like Cost Explorer and it works on a pay-per-session basis.

### AWS Trusted Advisor

**AWS Trusted Advisor** is a service that embodies a virtual service from AWS that advises you about the framework. It performs a series of checks with AWS best practices and highlights them in the below format if any actions are required.

1. no problem detected – meaning implementation is as per the required standards.
2. investigation recommended – for warnings.
3. action recommended – for any aspect which is totally out of place.

AWS Trusted Advisor continuously monitors how many of your provisioned resources you've used and generates recommendations. In the case of Cost Optimization, it highlights if any resources are underutilized, if instances are idle, whether reserved instances are going to expire, and more.

### AWS CloudFront

You don't always have to wait for AWS Trusted Advisor to advise on optimizations before you take action. **AWS CloudFront** is a service that provides resource metrics that we can use to monitor performance ourselves and identify underutilized resources.

AWS CloudWatch is the easiest way to collect metrics since it integrates with several AWS Services directly. By gaining operational visibility and insights, you can act on improvements and optimize costs.

### EC2 instance tenancy

AWS offers various options to provision a virtual machine on their infrastructure. These options are created to suit your need depending on how critical your service is.

In any given implementation, not all the services require dedicated high-performing nodes. Similarly, not everything can work on low compute and less available nodes.

This provides us with a gap to explore and define our compute infrastructure that is most suitable for the business and most cost-efficient. Let us take a look at some of the compute types (EC2) provided by AWS.

1. **Reserved Instances –** long-term commitment, low cost.
2. **Spot instances –** very low cost, uses sparing EC2 capacity, released when capacity not available, good for fault-tolerant applications.
3. **On-Demand instances –** no commitment, regular costs.
4. **Dedicated instances –** instances created from resources that are not shared.
5. **Dedicated hosts –** dedicated instance with access to hardware options like ports.
6. **Reserved capacity –** Reserved capacity can be purchased and used within an instance family. Instances can be resized, based on the normalization factor. Helps reduce cost with flexibility.

Based on your requirements, you can select the appropriate options from above to host your workload. For example, when you are sure that a certain node will exist for the long term, you can take advantage of reserved instances instead of on-demand instances and save up to 75% of the costs.

There is no point in provisioning an on-demand instance for loads that are ephemeral and non-critical. Spot instances can be used in this case that can help reduce costs up to 90%.

### Rightsizing AWS Storage

AWS provides various types of storage and you can use appropriate storage based on how hot or cold you want your data to be stored. Various types of storage offered by AWS are Object, Block, File, Hybrid, Edge, and Backup.

Let's look at an example of object storage. Below are storage classes offered by AWS S3. Which object storage class you choose will depend on how frequently the data is accessed and what retention period you require.

1. **Standard Storage –** standard storage, regular costs, immediate access.
2. **Standard Infrequent Access –** reduced availability, reduced costs.
3. **One Zone Infrequent Access –** reduced redundancy, reduced costs.
4. **Intelligent Tiering –** for unknown access patterns, data is moved in and out of various classes based on file usage frequency.
5. **Glacier –** Long term storage, cheap, minutes or hours to retrieve.
6. **Glacier Deep Archive –** Longer-term storage, cheaper, hours to retrieve.

Lifecycle policies can be used to transition the old data to cheaper long-term storage.

Every type of storage comes with various levers which you can set appropriately to optimize your storage costs on AWS. I recommend making use of AWS **Data Lifecycle Manager** while provisioning your storage capabilities.

## A Final note

There are many cost optimizations you can apply to resources in AWS, but how you apply these optimizations depends on your business priorities. 

Mainly you need to decide if your focus is on costs or on time-to-market. The main bases of cost optimization are:

1. **Time-based –** to optimize over time.
2. **Demand-based –** to optimize based on demand/traffic.
3. **Buffer-based –** to optimize based on secondary workloads.

The cost optimization pillar of a well-architected framework suggests that while designing, developing, and deploying applications on AWS it is a good practice to keep cost optimization in perspective. 

You should continually monitor your costs to reap the most benefits from your cloud investment.

In this post, we discussed various aspects of cloud cost optimization with respect to AWS Well-Architected Framework. If you have stuck with me up until now, cheers to you!

Hey, if you like this content, do consider subscribing, following, and sharing this blog post! [Let'sDoTech](https://letsdotech.dev), [Instagram](https://www.instagram.com/letsdotech/), [Twitter](https://twitter.com/letsdotech_dev), [LinkedIn](https://www.linkedin.com/company/letsdotech).

