---
title: How to Select the Right EC2 Instance – A Guide to EC2 Instances and Their Capabilities
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2022-12-15T19:08:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-select-the-right-ec2-instance
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/cover-photo.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: ec2
  slug: ec2
seo_title: null
seo_desc: 'EC2 (Elastic Compute Cloud) is the most widely-used compute service from
  AWS. It''s also one of the oldest services launched by AWS, as it was started in
  2006.

  In this article, I will go through some things you should consider when selecting
  an EC2 in...'
---

EC2 (Elastic Compute Cloud) is the most widely-used compute service from AWS. It's also one of the oldest services launched by AWS, as it was started in 2006.

In this article, I will go through some things you should consider when selecting an EC2 instance.

You can think of an EC2 instance as not too different from your personal computer. If you are going to buy a computer, three broad technical considerations may cross your mind (ignoring any aesthetic or design preferences you may have, of course):

1. How much processing can it handle?
    
2. How much memory does it have?
    
3. How much storage does it have?
    

These three questions should also cross your mind when selecting an EC2 instance. The difference being, you are only renting the instance from AWS, instead of buying it as you would with a personal computer.

Each EC2 instance is composed of:

1. CPU – how much processing can be achieved
    
2. Memory
    
3. Storage – this only applies to some instances that have physically attached storage (called the [instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)). For other EC2 instances, you'll need to choose network storage using EBS (Elastic Block Storage) separately.
    

## Compute, Memory, and Storage – An Analogy

A good analogy for an EC2 instance is your work desk.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F44e98a5c-f6fb-4f23-8840-477a52ef0b6c_1257x690.png align="left")

Your brain is the compute, the surface of your desk is the memory, and your desk drawer is the storage. Note that this analogy (like all analogies) has its limitations. Its purpose is to neatly spilt the role of compute, memory, and storage in an EC2 instance.

What exactly does compute mean? Compute is concerned with *parallelism –* the ability to execute multiple tasks simultaneously.

Human brains can handle some level of parallelism. You might be able talk on the phone while taking notes simultaneously, for example. You cannot, however, write two different letters simultaneously, or talk on the phone while taking notes and reading a book.

These activities cannot be executed in parallel because our brain can be crudely thought of as a CPU with a single core. To increase compute, we need to increase parallelism, and this can be achieved by having multiple CPU cores. More cores equals more parallelism which equals more compute power.

Memory and storage are theoretically the same thing. We use them both for storing data. Practically, though, they are physically distinct pieces of infrastructure simply because there is no single storage device that is both fast and non volatile.

Memory is fast and volatile while storage is slow and non-volatile. Things kept on the surface of your desk are quickly and easily accessible, just like data in a computer’s memory. But anything left on your desk overnight in a busy office is at risk of being moved, lost, or stolen. The surface of your desk, just like a computer’s memory, is volatile.

Storage, on the other hand, is non-volatile but slower to read/write from. Just like items in your desk drawers are less likely to go missing but take longer to get your hands on.

## How to Select the Right EC2 Instance

So, CPU, memory, and sometimes storage are the three levers you can pull when selecting an EC2 Instance. Recall that storage is often selected separately from the EC2 instance using EBS volumes, except for storage optimized instances that have physically attached storage.

When you select an instance type, you are effectively selecting for the **lowest price per unit of the metric most important for your workload**. This metric can be CPU/GPU performance, memory, or storage.

There are five AWS instance types:

* general purpose: By choosing a general purpose instance, you are taking a balanced approach and not optimizing for any one metric.
    
* compute optimized: By choosing a compute optimized instance, you are optimizing for the lowest price per unit of CPU performance (number of CPU cores).
    
* accelerated computing: By choosing an accelerated computing instance, you are optimizing for the lowest price per unit of GPU performance (think of this as a specialised CPU needed for high performance compute workloads).
    
* storage optimized: By choosing a storage optimized instance, you are optimizing for the lowest price per unit of storage capacity and efficiency.
    
* memory optimized: And by choosing a memory optimized instance, you are optimizing for the lowest price per unit of memory.
    

Let’s go through the instance types in more detail.

AWS has a great outline of this [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) that I have summarised below:

1. **General Purpose** – For workloads that require a balance of compute, memory and networking. Ideal use case is web servers.
    
2. **Compute Optimized** – For workloads that require high performance processors. Lowest dollar cost per number of CPU cores. Ideal for compute intensive workloads like scientific modelling and gaming.
    
3. **Accelerated Computing** – For workloads that require even larger amounts of compute resources than compute optimized instances. This type of instance uses GPUs (graphical processing units) which is a specialised CPU designed for machine learning and high performance computing workloads.
    
4. **Storage Optimized** - For workloads that require high rates of reads and writes for large amounts of data, that is high IOPS (Input/Output Operations per second).
    

Unlike other instances, these do not use separate EBS volumes for storage. Instead they come with physically attached storage volumes (called the [instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)). This means that data does not have to go through a network, allowing it to achieve high IOPS.

Ideal use case is NoSQL databases – like Elasticsearch, MongoDB, Cassandra and some data warehousing applications. Instance store volumes, however come with a catch: any data stored there does not persist beyond the life of the instance. So, if the instance stops, hibernates, terminates or fails, you lose all data on that instance.

The ideal use case for storage optimized instances is thus for workloads that require high IOPs **and** can tolerate the failure of an instance (usually by having data replicated to another instance for redundancy). 5. **Memory Optimized –** For workloads that require large amounts of RAM. Lowest dollar cost per unit of RAM. Ideal for in memory databases, caches, SQL databases.

## Anatomy of an EC2 Instance Name

You may have come across EC2 instance names like t2.nano, r6a.large or i3en.6xlarge. What exactly do the letters and numbers mean?

Let’s take a complex name like i3en.6xlarge as an example and break it down.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5f1844b-80a3-4f87-b7de-1027f4c16aec_1280x720.jpeg align="left")

*Anatomy of an EC2 instance name broken down*

### Instance Family

Reading from left to right, the first letter is the instance family. Every family belongs to only one of the instance types, that is general purpose, compute optimized, accelerated computing, storage optimized or memory optimized.

There is no need to cram trying to learn which instance family belongs to which instance type. As you work more with AWS, it will become almost second nature. You can have a look [here](https://aws.amazon.com/ec2/instance-types/) for reference if you'd like.

The i3en.6xlarge instance above belongs to the “i” family, which is a storage optimized instance.

### Instance Generation

This is a number that shows the instance generation. The higher the number, the more recent the generation.

When given the option between different generations for the same instance, you should, ideally, always select the latest generation. The latest generation instance usually comes with the latest hardware. This typically means lower cost per unit of performance relative to older generations.

The i3en.6xlarge instance in the example above is a third generation instance.

### Special Features

These are optional letters that come after the instance generation. Each letter denotes some special feature about the instance.

In this case the “**e**” signifies **extra** **capacity** (can be RAM or storage) and “**n**” signifies that the instance is **network** **optimized**. This means that it has high network bandwidth, meaning the instance can handle a high data transfer rate, typically measured in Gb per second.

Other special feature characters and their capabilities are as follows:

* **a** – AMD processors
    
* **g** – AWS Graviton processors
    
* **i** – Intel processors
    
* **d** – Instance store volumes
    
* **b** – Block storage optimization
    
* **z** – High frequency
    

These extra features do not come for free, so only select an instance with extra features if you need these additional features.

### Instance Size

The size appears after the full stop. It consists of two parts: a number and letters denoting size. The size options range from nano to xlarge (extra large).

The number only appears with xlarge instances. It denotes how much larger the instance is compared to an xlarge. So a 2xlarge is twice as large as an xlarge and a 6xlarge is six times as large as the xlarge.

But, what does twice or six times as large really mean?

For the same instance type, the number after the full stop acts as a multiplier for the compute (number of vCPUs), memory (amount of RAM), and storage size (not all the time – some instances use EBS volumes where storage can scale independently of the instance. Storage optimized instances, on the other hand, use physically attached instance storage that scales based on the instance size.).

An i3en.xlarge instance has 4 vCPUs, 32 GiB memory, and 2500 GB storage capacity. An i3en.**6**xlarge is six times larger since it has **six times** the number of vCPUs (24), six times the memory (192 GiB), and six times the storage capacity (15,000 GB).

## Bringing it All Together – How to Select Your Instance

So, let’s say you need to select an EC2 instance for your web server, or your NoSQL database – what are some logical steps to follow?

### Step 1: Select instance type

Choosing between general purpose, compute optimized, accelerated computing, storage optimized and memory optimized is the first and most important decision. Every subsequent decision will be driven by this one.

Here, the decision you are making is primarily one of cost - you are trying to **optimize for the lowest dollar cost per unit of the metric that's most important for your workload**.

If your workload is generic, like a web server, choose a general purpose instance. If your workload is compute intensive, go with a compute optimized instance type. The same logic applies if your workload is memory or storage intensive.

### Step 2: Select instance family

A good mental model for choosing the right instance family is to go through the technical documentation for the application you plan to run on that instance and use their recommendation.

For example, Elasticsearch (a full-text search engine database) recommends the “i” family of instances – specifically the “i3”. Recall that the number after the instance family is simply the instance generation, and the latest is usually the greatest.

When a newer generation of the “i” family arrives, Elasticsearch will likely recommend the “i4” instance. You can reason by analogy when selecting the instance family. Look at what the application recommends, as it's a great way to reduce any errors of omission or commission.

The company behind the application will have a lot of experience testing different families and will have done the experimentation on your behalf. No need to re-invent the wheel (unless, of course, your workload is truly niche and no best practice exists).

### Step 3: Select an instance with special features

Do this only if absolutely needed. You will be paying extra for this.

### Step 4: Select an instance size

This is purely specific to your workload and is usually an iterative process. You can run some tests while monitoring CPU and memory utilisation to see if the size you selected is appropriate.

You usually try to have some safety margin, so if your workload is consuming, on average, 90% of memory and CPU, you may need to choose a larger instance. A utilisation of 90% does not provide much headroom for any estimation errors you may have made during testing.

Deciding on the amount of headroom you need is more art than engineering, so there are no hard qualitative numbers on this. But as a rough guide, utilisation in the 90% range is bad, 80% range is acceptable, and 70% and below is good.

You need to provide some headroom to prevent any performance problems from occurring during peak demand.

## Wrapping Up

When you select an instance type, you are effectively selecting for the lowest price per unit of the metric most important for your workload. This is an important foundation in any project you are working on, as it ensures you are paying the lowest dollar amount per unit of performance.

Selecting the instance size is the most difficult piece of the puzzle and is likely to be an iterative process where you start small, test, and then scale up as required.
