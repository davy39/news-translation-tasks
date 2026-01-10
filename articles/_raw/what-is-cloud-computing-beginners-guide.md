---
title: What is Cloud Computing? Explained for Beginners
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-01-16T19:03:48.000Z'
originalURL: https://freecodecamp.org/news/what-is-cloud-computing-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-pixabay-210158--1-.jpg
tags:
- name: Cloud
  slug: cloud
- name: Cloud Computing
  slug: cloud-computing
seo_title: null
seo_desc: "You may not always be aware of it, but you're enjoying the many fruits\
  \ of the cloud just about every hour of every day. Many of the joys (and horrors)\
  \ of modern life would be impossible without it. \nBefore we talk about what it\
  \ does and where it's ta..."
---

You may not always be aware of it, but you're enjoying the many fruits of the cloud just about every hour of every day. Many of the joys (and horrors) of modern life would be impossible without it. 

Before we talk about what it does and where it's taking us, we should explain exactly what it is.

## What is The Cloud?

The "cloud" is all about using other people's computers rather than your own. That's it. No, really.

Cloud providers run lots of compute servers (which are just computers that exist to "serve" applications and data in response to external requests), storage devices, and networking hardware. Whenever the impulse takes you, you can provision units of those servers, devices, and networking capacity for your own workloads. 

When you add millions more users taken by similar impulses, you get the modern cloud.

For many – although not all – applications, there are enormous cost and performance benefits to be realized by deploying to a cloud. And countless applications – whether small, large or smokin' colossal – have found productive homes on one cloud platform or another. 

So let's see how it all works and what you might be able to do with it.

This article was taken from the book, [Keeping Up: Backgrounders to All the Big Technology Trends You Can't Afford to Ignore](https://amzn.to/3FXXAfb). If you'd prefer to watch this chapter as a video, feel free to follow along here:

%[https://www.youtube.com/watch?v=eufNv-vpLZE]

# Application Server Deployment Models

Over the decades, we've been through a number of models for running server workloads. In a way, all those changes have been the product of just two technologies:

* Networking protocols that permit communication between connected nodes
* Virtualization which permits fast, efficient, and cost-effective use of hardware resources for multiple and parallel uses

Networking, largely because it's now such a stable and well established technology, isn't something we'll focus on here. But we will get back to virtualization a bit later.

## How Local Data Centers Work

In the old days, if you wanted to fire up a new server to perform a compute task, it was quite a process.

You would spend a week or so calculating how much compute power you'd need for your job, contact the sales reps at a few hardware vendors, wait for them to get back to you with bid tenders, and then compare the bids. Then, when you've selected one, you'd wait another couple of weeks for your new hardware to be delivered. Then you'd put all the pieces together, plug it all in, and start loading software.

The room where your servers ran would need a reliable and robust power supply and some kind of cooling system: like angry children, servers generate a great deal of heat but don't like being hot. You probably wouldn't want to do any other work in that room, since the noise of your servers' powerful internal cooling fans would be difficult to ignore.

While locally-deployed servers gave you all the direct, manual control over your hardware that you could need, it came at a cost. 

For one thing, opportunities for infrastructure redundancy (and the reliability that comes with it) were limited. After all, even if you regularly backed up your data (and assuming your backups were reliable), they still wouldn't protect you from a facility-wide incident like a catastrophic fire. 

You would also need to manage your own networking, something that could be particularly tricky – and risky – when remote clients required access from beyond your building.

By the way, don't be fooled by my misleading use of past tense here ("were limited," "backed up"). There are still plenty of workloads of all sizes happily spinning away in on-premises data centers. But the trend is, without question, headed in the other direction.

## What is Virtualization?

As I hinted earlier, virtualization is the technology that, more than any other, defines the modern internet and the many services it enables. 

At its core, virtualization is a clever software trick that lets you convince an operating system that it's all alone on a bare metal computer when it is, in fact, just one of many OSs sharing a single set of physical resources. 

A virtual OS will be assigned space on a virtual storage disk, bandwidth through a virtual network interface, and memory from a virtual RAM module.

Here's why that's such a big deal. Suppose the storage disks on your server host have a total capacity of two terabytes and you've got 64GB of RAM. You might need 10GB of storage and 10GB of memory for the host OS (or, _hypervisor_ as some virtualization hosts are called). 

That leaves you a lot of room for your virtual operating system instances. You could easily fire up several virtual instances, each allocated enough resources to get their individual jobs done. 

When a particular instance is no longer needed, you can shut it down, releasing its resources so they'll instantly be available for other instances performing other tasks.

But the real benefits come from the way virtualization can be so efficient with your resources. One instance could, say, be given RAM and storage that, later, proves insufficient. You can easily allocate more of each from the pool – often without even shutting your instance down. Similarly, you can reduce the allocation for an instance as its needs drop.

This takes all the guesswork out of server planning. You only need to purchase (or rent) generic hardware resources and assign them in incremental units as necessary. There's no longer any need to peer into the distant future as you try to anticipate what you'll be doing in five years. Five _minutes_ is more than enough planning.

Now imagine all this happening on a much larger scale: Suppose you've got many thousands of servers running in a warehouse somewhere that are hosting workloads for thousands of customers. Perhaps one customer suddenly requests another terabyte of storage space. 

Even if the disk that customer is currently using is maxed out, you can easily add another terabyte from some other disk, perhaps one plugged in a few hundred meters away on the other side of the warehouse. The customer will never know the difference, but the change can be virtually instant.

### Cattle vs pets

Server virtualization has changed the way we look at computing and even at software development. 

No longer is it so important to build configuration interfaces into your applications that'll allow you to tweak and fix things on the fly. It's often more effective for your developers and sysadmins to build a custom operating system _image_ (nearly always Linux-based) with all the software pre-set. You can then launch new virtual instances based on your image whenever an update is needed.

If something goes wrong or you need to apply a change, you simply create a new image, shut down your instance, and then replace it with an instance running your new image. 

Effectively, you're treating your virtual servers the way a dairy farmer treats cows: when the time comes (as it inevitably will), you remove an old or sick cow, and then bring in another (younger) one to replace it.

Anyone who's ever been involved with legacy server room administration would gasp at such a thought! Our old physical machines would be treated like beloved pets. At the slightest sign of distress, we'd be standing, concerned, at its side, trying to diagnose what the problem was and how it can be fixed. 

If all else failed, we'd be forced to reboot the server, hoping against hope that it came back up again. If even _that_ wasn't enough, we'd give in and replace the hardware.

But the modularity we get from virtualization gives us all kinds of new flexibility. Now that hardware considerations have been largely abstracted out of the way, our main focus is on software (whether entire operating systems or individual applications). And software, thanks to scripting languages, can be automated. 

So using orchestration tools like Ansible, Terraform, and Puppet, you can automate the creation,  provisioning, and full life cycle management of application service instances. Even error handling can be built into your orchestration, so your applications could be designed to magically fix their own problems.

### Virtual machines vs containers

Virtual instances come in two flavors. Virtual machines (or VMs) are complete operating systems that run on top of – but to some degree independent of – the host machine. 

This is the kind of virtualization that uses a hypervisor to administrate the access each VM gets to the underlying hardware resources, but such VMs are generally left to live whichever way they choose. 

Examples of hypervisor environments include the open source Xen project, VMware ESXi, Oracle's VirtualBox, and Microsoft Hypver-V.

Containers, on the other hand, will share not only hardware, but also their host operating system's software kernel. This makes container instances much faster and more lightweight (since their images don't need to include a kernel). 

Not only does this mean that containers can launch nearly instantly, but that their file systems can be transported between hosts and shared. Portability means that instance environments can be reliably reproduced anywhere, making collaboration and automated deployment not only possible, but easy.

Examples of container technologies include LXD and Docker. And enterprise container implementations include Google's open source Kubernetes orchestration system.

## How Public Clouds Work

Public cloud platforms have elevated the abstraction and dynamic allocation of compute resources into an art form. The big cloud providers leverage vast networks of hundreds of thousands of servers and unfathomable numbers of storage devices spread across data centers around the world.

Anyone, anywhere, can create a user account with a provider, request an instance using a custom-defined capacity, and have a fully-functioning and public-facing web server running within a couple of minutes. And since you only pay for what you use, your charges will closely reflect your real-world needs.

A web server I run on Amazon Web Services (AWS) to host two or three of my moderately busy websites costs me only $50 a year or so. And it has enough power left over to handle quite a bit more traffic. 

The AWS resources used by the video streaming company Netflix will probably cost a big more – undoubtedly in the millions of dollars per year. But they clearly think they're getting a good deal and prefer using AWS over hosting their infrastructure themselves.

Just who are all those public cloud providers, I'm sure you're asking? Well that conversation must begin (and, often, end) with AWS. They're the elephant in every room. The millions of workloads running within Amazon's enormous and ubiquitous data centers, along with their frantic pace of innovation, make them the player to beat in this race. And that's not even considering the billions of dollars in net profits they pocket each quarter.

At this point, the only serious competition to AWS are Microsoft's Azure which is doing a pretty good job keeping up with service categories and, by all accounts, is making good money in the process. There's also Alibaba Cloud which is mostly focused on the Asian market at this point. Google Cloud is in the game, but appears to be focusing on a narrower set of services where they can realistically compete.

As the barrier to entry in the market is formidable, there are only a few others who are getting noticed, including Oracle Cloud, IBM Cloud and, with a welcome naming convention, Digital Ocean.

## How Private Clouds Work

Cloud goodness can also be had closer to home, if that's what you're after. There's nothing stopping you from building your own cloud environments on infrastructure located within your own data center. 

In fact, there are plenty of mature software packages that'll handle the process for you. Prominent among those are the open source OpenStack (openstack.org) and VMware's vSphere (vmware.com/products/vsphere.html) environments.

Building and running a cloud is a very complicated process and not for the hobbyist or faint of heart. And I wouldn't try downloading and testing out OpenStack – even just to experiment – unless you've got a fast and powerful workstation to act as your cloud hosts and at least a couple of machines for nodes.

You can also have it both ways by maintaining certain operations close to home while outsourcing other operations in the cloud. This is called a hybrid cloud deployment. 

Perhaps, as an example, regulatory restrictions require you to keep a backend database of sensitive customer health information within the four walls of your own operation, but you'd like your public-facing web servers to run in a public cloud. It's possible to connect resources from one domain (say, AWS) to another (your data center) to create just such an arrangement.

In fact, there are ways to closely integrate your local and cloud resources. The _VMware Cloud on AWS_ service makes it (relatively) easy to use VMware infrastructure deployed locally to seamlessly manage AWS resources (aws.amazon.com/vmware).

# The Value of Outsourcing Your Compute Operations

Why might you want to migrate workloads to the cloud? You might end up saving a lot of money. So there's that. Of course, it's not going to work out that way for every deployment, but there do seem to be a lot of use cases where it does. 

To help you make informed decisions, cloud platforms often provide sophisticated calculators for you to compare the costs of running an application locally as opposed to what it would cost in the cloud. The AWS version of that is here: aws.amazon.com/tco-calculator

Part of the pricing calculus is the _way_ you pay. The traditional on-premises model involved large up-front investments for expensive server hardware that you hoped would deliver enough value over the next five to ten years to justify the purchase. These investments are known as _capital expenses_ ("Capex").

Cloud services, on the other hand, are billed incrementally (by the hour, or even minute) according to the number of service units you actually consume. This is normally classified as _operating expenses_ (Opex). 

Using the Opex model, if you need to run a server workload only once every few days for five minutes at a time in response to an external triggering event, you can automate the use of a "serverless" workload (using a service like Amazon's Lambda) to run only when needed. Total costs: perhaps only a few pennies a month to cover those minutes the service is actually running.

Besides cost considerations, there's a lot more going on in the cloud world that should attract your consideration. You've already seen how the lag time between the decision to deploy a new server on-premises and its actual deployment (weeks or months) compares to a similar decision/deployment process in a public cloud (a few minutes). But large cloud providers are also positioned to deliver environments that are significantly more secure and reliable.

As an example, you may remember our story about the DDoS attack from my article on [Understanding Digital Security](https://www.freecodecamp.org/news/understanding-digital-security/). That was the incident where the equivalent of 380,000 PDF books worth of data were used to bombard an AWS-hosted web service each second...and the service survived. Are you confident you could do that yourself?

And how about reliability through redundancy? Would your on-premises infrastructure survive a catastrophic loss of your premises? Even if you did the right thing and maintained off-site backups, how long would it take you to apply them to rebuilt, network-connected, and functioning hardware?

The big cloud platforms run data centers across physically distant locations around the world. They make it easy (and in some cases unavoidable) to replicate your data and applications in multiple locations so that, even if one data center goes down, the others will be fine. Can you reproduce that?

Cloud providers also manage content distribution networks (CDNs) allowing you to expose cached copies of frequently-accessed data at edge locations near to wherever on earth your clients live. This greatly reduces latency, improving the user experience your customers will get. Is _that_ something you can do on your own?

One more thought. Most of the big investments into new IT technologies these days are being plowed into cloud ecosystems. That's partly because the big cloud providers are generating cash far faster than they can hope to spend it. But it's also because they're involved in a live-or-die race to capture new segments of the infrastructure market before the competitions claims them.

The result is that the sheer rate of innovation in the cloud is staggering. I earn a living keeping a close eye on AWS, and even I regularly miss new product announcements. 

One of the reasons I avoid including screenshots of the AWS management console in my books and video courses is because their console is updated so often, the images will often be out-of-date before the book hits the street.

In some cases, this might mean that local deployments will run at a built-in disadvantage simply because they won't have access to the equivalent cutting edge technologies.

# The Risks of Outsourcing Your Compute Operations

Having said all that, as with most things in life, choosing between cloud and local isn't always going to be as easy as I may have made it sound. 

There may still be, for instance, laws and rules forcing you to keep your data local. There will also be cases where the math just doesn't work out: sometimes it really is cheaper to do things in your own data center.

You should also worry about platform lock-in. The learning curve necessary before you'll be ready to launch complex, multi-tier cloud deployments isn't trivial. And you can be sure that the way it works on AWS, probably won't be quite the same as what's happening on MS Azure. The knowledge investment you'll need to make once you make your choice will probably be expensive.

But what happens to that investment if the provider's policies suddenly change in a way that forces you off the platform? Or if they actually go out of business (could happen: Kodak, Blockbuster Video, and Palm were once big, too)? 

And what about getting locked out of your account for some reason? How hard would it be for you to retool and reload everything somewhere else?

Just think ahead and make sure you're making a rational choice.

Thank you for reading!

_YouTube videos of all ten chapters from this book [are available here](https://www.youtube.com/playlist?list=PLSiZCpRYoTZ6UWl4xialvwLOKyHYYJUiC). Lots more tech goodness - in the form of books, courses, and articles - [can be had here](https://bootstrap-it.com). And consider taking my [AWS, security, and container technology courses here](https://www.udemy.com/user/david-clinton-12/)._

