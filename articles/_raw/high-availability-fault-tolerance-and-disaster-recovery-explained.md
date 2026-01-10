---
title: High Availability vs Fault Tolerance vs Disaster Recovery – Explained with
  an Analogy
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2022-11-07T17:10:24.000Z'
originalURL: https://freecodecamp.org/news/high-availability-fault-tolerance-and-disaster-recovery-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/Slide6.JPG
tags:
- name: availability
  slug: availability
- name: Disaster recovery
  slug: disaster-recovery
- name: software architecture
  slug: software-architecture
- name: System Architecture
  slug: system-architecture
seo_title: null
seo_desc: 'High availability, fault tolerance and disaster recovery are important
  things to consider when designing a system.

  These terms are sometimes used interchangeably by architects and developers. They
  are not, however, the same thing – and understanding ...'
---

High availability, fault tolerance and disaster recovery are important things to consider when designing a system.

These terms are sometimes used interchangeably by architects and developers. They are not, however, the same thing – and understanding the differences can save you many headaches, as well as time and money.

This article will go through the differences between the three terms and explain how you can implement them in AWS.

## Highly Available vs Fault Tolerant vs Disaster Recovery

A highly available system is one that aims to be online as often as possible. While downtime can still occur in a highly available system, the aim of high availability is to limit the duration of the downtime, not to completely eliminate it.

A fault tolerant system is one that can operate through a fault without any downtime. Fault tolerance aims to avoid downtime completely.

In a complete system failure however, high availability and fault tolerance are not enough. Disaster recovery describes how the system can continue to operate when the cushion of high availability and fault tolerance disappears in a system wide failure.

## What Does High Availability Mean?

First, let's describe what high availability is not. High availability does not mean that the system never fails or never experiences downtime. A highly available system is simply one that aims to be online as often as possible.

Imagine we have a pizza restaurant that is open 24 hours every day for 365 days. If that restaurant only has one chef, then its availability – that is, its ability to process orders – will not be 100%. This is because a single chef can only work for about eight hours a day with a one hour break – or effectively seven hours a day, for seven days in a week.

The chef can therefore only work for 49 hours in a week out of a possible 168 hours. This restaurant has an availability of 29%.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff3e3d174-070d-447d-9088-92c6f7377c99_1504x861.jpeg align="left")

*A low availability restaurant*

This is of course not a high enough availability for a restaurant that wants to be open for 24 hours in a day throughout the year.

So how do we get a higher availability for the restaurant? Hire more chefs. If we have four chefs working six hour shifts in a day for seven days in a week, this gives us a theoretical availability of 100%.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8b1538ad-5148-44f1-b025-c6705a5c3780_1504x830.jpeg align="left")

*A higher availability restaurant*

This 100% availability is only theoretical because it assumes no chef misses work in an entire year. This is a poor assumption as chefs can get sick, their cars can break down on the way to work, or they may have to leave work early to pick up their kids.

Let's say all this chef downtime adds up to five hours in a year. This gives you an availability of 99.94%.

How can you make the restaurant even more available? Hire standby chefs that are ready to come to the restaurant at a moment's notice. But this comes at a steep price since you have to pay these chefs to wait until they are needed.

What these standby chefs give you is **the ability to quickly recover from not having enough chefs to meet customer orders**. You can never have 100% availability because of the constraints of reality. You can only approach an availability of 100% at an increasingly steep price.

### What is Availability in a System?

Availability is the probability that a system will be able to respond to a request.

Note that high availability has nothing to say about the quality of the pizzas or how quickly they are delivered. High availability is simply concerned with the ability of the restaurant to respond to pizza orders from customers.

The major cloud providers typically have [SLAs](https://www.cio.com/article/274740/outsourcing-sla-definitions-and-solutions.html) that describe the availability of a system.

Take a blob storage system, for example. AWS S3 standard has an availability SLA of 99.99%. This is the same figure for Azure blob storage and Google cloud storage.

What exactly does 99.99% availability mean? It means that in any year, there is a 99.99% probability that the system will be online. An uptime of 99.99% equals a downtime of 0.01%. This is equivalent to a downtime of approximately 53 minutes - just under an hour for an entire year.

How about an availability of 99.9%? Such a system would have a downtime of 0.1% which is 8.8 hours in a year.

While 99.9% availability may seem high, for a bank processing payments, air traffic control system, or any other critical system, such amount of downtime may simply be unacceptable.

What is the right amount of availability you should target? That depends on the requirements of the system you are building.

You are of course constrained by the availability SLAs of the cloud providers, so there is limited flexibility in achieving say 99.999% availability for a blob storage system, for example. And, the higher the availability you want to achieve, the more expensive and complex the solution becomes.

## What Does Fault Tolerance Mean?

If a failure within a system occurs, can the system continue to operate without any disruption? If it can, then the system is fault tolerant.

So what is the difference between high availability and fault tolerance? With a highly available system, failures that cause downtime will occur, but rarely. The system is also able to recover from such failures. **But when the system is down, it cannot respond to requests.**

In a fault tolerant system, the system **can continue to operate in spite of a failure.**

Let's use the pizza restaurant as an example again. If the restaurant experiences a power outage, then no amount of chefs in the kitchen or chefs on standby will help with making pizzas for customers since the ovens need a power supply.

A backup generator that kicks in immediately when a power loss is experienced makes the restaurant fault tolerant.

Another good example of this is a commercial aircraft powered by jet engines. These aircraft are built to be fault tolerant so in the event that one engine fails, the aircraft can continue to fly and land without disruption or having to fix the failed engine in flight.

Helicopters or single engine aircraft, on the other hand, are not fault tolerant. A failure of the engine means the aircraft cannot fly. Such failures are usually catastrophic and partly explain the higher rate of helicopter and single engine aircraft crashes compared to dual engine aircraft.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fdfafca0a-1940-4215-ac2b-39a7a84b9660_1504x861.jpeg align="left")

*An aircraft with two engines is fault tolerant*

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F964241a9-8fc6-4d65-86c2-48f509a5951a_1504x861.jpeg align="left")

*Helicopters and single engine aircraft are not fault tolerant*

## What Does Disaster Recovery Mean?

If the scale of the system failure is so large that the high availability and fault tolerance of the system are effectively neutralised, can the system continue to operate?

Let's go back to the restaurant example. If a fire, flood, or any other disaster befalls your pizza restaurant, how can you continue to make pizzas for your customers?

This is a somewhat facetious example since in the event of a fire, worrying about customer orders is not the main priority – but the logic of the example still holds.

In this instance, high availability is of no help. Having an infinite number of chefs in the kitchen or on standby in a restaurant engulfed in flames = no pizzas for customers.

Fault tolerance is also of no help. A backup generator is useless for the appliances it is meant to power if they have been destroyed.

The only way the system (restaurant) can continue to operate is by routing orders to another nearby restaurant unaffected by the fire. Disaster recovery is a proactive plan of action that details how to recover **after a disaster has happened**.

## Bringing it All Together

Now, let's look at a single architecture that is simultaneously highly available, fault tolerant, and has built-in disaster recovery.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3995b811-f03f-44b5-8118-8f7965e7f09a_893x560.jpeg align="left")

*All in one - high availability, fault tolerance, and disaster recovery in a single architecture*

The architecture above shows a multi-availability zone (AZ) Relational Database Service (Amazon RDS) deployment. It shows an RDS database with a standby instance in a separate AZ, a single read-only replica, and an S3 bucket used to store backups of the database on a daily basis.

This RDS is a fully managed DB as a service offering from AWS where AWS manages the underlying hardware, software, and application of the DB. You can find more information here on [AWS RDS](https://aws.amazon.com/rds/) and [availability zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/).

Now let's dissect how this system would work and how the design ensures it is highly available, fault tolerant and can recover from a disaster.

### How High Availability is Achieved

The primary RDS instance in AZ A synchronously replicates its data to the standby instance in AZ B.

With synchronous replication, the primary instance waits until the standby has received the latest write operation before the transaction is recorded as successful. This ensures that both databases have identical information – that is, they are consistent, admittedly at the expense of increased transaction latency.

The primary and standby instances are in an active-passive configuration. Only the primary receives read and write request. The job of the standby is to simply take over as the primary in the event of a failure of the primary instance.

The time it takes to failover from the primary to the standby instance is called the Recovery Time Objective (RTO). The RTO simply describes how long it takes to recover from a failure. In this case, the failover time for RDS in a multi-AZ configuration is currently between 1-2 minutes.

The standby instance has one purpose: to increase the availability of the system. If the primary instance fails, or if the entire AZ A goes down, the standby instance in a separate AZ will be promoted to the primary. This failover process takes 1-2 minutes. That is 1-2 minutes of downtime.

Recall that high availability is not about preventing downtime, but simply reducing it. Without a standby instance, there is a high probability that downtime will exceed the 1-2 mins it takes to recover with a standby instance.

Note that the standby instance does not help with fault tolerance, since the failure of the primary will still lead to downtime.

### How Fault Tolerance is Achieved

To eliminate downtime, you need a configuration that involves no failover. This is a job for read-only replicas. These are asynchronously replicated copies of the primary instance. Writes are only made to the primary instance. Read replicas are, as the name implies, read only.

Such an approach is ideal for read heavy application since read replicas can remove the additional burden of read requests from the primary instance.

In asynchronous replication, writes to a primary instance do not wait for a response from the read-only replica before the transaction is recorded as a success. This means that, for a time, data across the primary and read replica may not be identical (but rather, inconsistent) after a write to the primary.

This eventual consistency (a topic for another article) is a drawback of asynchronous replication. The benefit of asynchronous replication is that it does not wait for the read replica to respond before the transaction is recorded as a success.

This is important because if the read replica is down or there is a network failure, the primary can still accept subsequent writes without waiting for a response from the read replica, confirming that the previous write was successfully replicated.

The architecture above has two replicas: one synchronous and the other asynchronous. If all replicas are synchronous, then a failure in the standby replica or the read only replica, or even a network failure, brings the entire cluster down. This is a fragile design that exposes the entire system to failure if a single component fails. Having some replicas that are synchronous and others that are asynchronous improves the fault tolerance of the system.

Where else does fault tolerance come in? Like an aircraft with two jet engines that provide thrust, a read replica and a primary can work together simultaneously. The the primary instance processes writes and the read replica responds to read requests.

Failure of the primary instance has no effect on the read replica's ability to respond to read requests. There is no downtime for reads since only the read replica responds to reads.

How about writes? The read replica can be promoted to a primary, although with RDS, this is currently a manual process.

### How Disaster Recovery is Achieved

With the architecture above, you can handle disaster recovery in two ways. There is no constraint to limit disaster recovery to only one approach, so you can use both at the same time. And in fact, the more approaches you have, the better, since this provides extra redundancy.

Ultimately, you should weigh all this against cost, as implementing disaster recovery strategies can be expensive.

The first method is through automatic backups. Backups are taken from the standby instance, preventing performance degradation of the primary instance that has to serve writes (and reads if not configured with a read replica). Since there is synchronous replication between the primary and the standby, we have a guarantee that the standby is an up to date copy of the primary, so it's ideal to take backups from.

With RDS, backups are taken on a fixed schedule once a day (specified by you) and stored in an S3 bucket. Since this is an entirely separate component, any RDS-related system-wide failures will not affect the durability of the backups.

With backups, a loss of the primary, standby, and read-replicas does not equal a permanent loss of data. Backups can then be used to restore the database to a new DB instance.

The second method is to promote the read-only replica to a standalone instance if the primary instance fails. The read replica can be configured in another [AWS region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/). This way, if there is a disaster on a regional scale where multiple AZs are down, a cross regional read replica will ensure that another instance is available in a different AWS region to serve read and write requests.

This is analogous to diverting orders to another restaurant in the event of a fire.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fcb353885-8d22-4542-8155-2f92e3d49314_943x635.jpeg align="left")

*How different components improve the availability, fault tolerance and disaster recovery of a solution*

## Wrapping Up

Availability is measured in percentages - the larger the number, the more available the system is (hence less downtime).

Very few systems aim for 100% availability – although pacemakers are a notable exception. An availability of 99.999% has a downtime of 0.001% = 5 minutes of downtime in a year. This tends to be the upper limit for most software systems.

Aiming for higher levels of availability above this is increasingly complicated, expensive, and often unnecessary. This is especially true when you consider that the software system you are building relies on infrastructure like the power grid and internet service providers, which may have lower availability levels.

Fault tolerance, on other hand, cannot be measured. Your design is either fault tolerant or it is not. Similarly, disaster recovery cannot be measured. You either have a plan of action that precisely outlines how your system can recover from a disaster or you do not.

Knowing the difference between high availability, fault tolerance, and disaster recovery is important. It ensures you are building the correct architecture based on customer needs.

Over-engineering a solution by providing disaster recovery when all that is required is high availability or fault tolerance is often an expensive and complex exercise.

On the other hand, under-engineering a solution by only providing high availability when fault tolerance is required can lead to severe consequences for some critical systems that cannot afford any downtime.
