---
title: How Modern Compute Platforms Work
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-02-07T20:22:32.000Z'
originalURL: https://freecodecamp.org/news/modern-compute-platforms
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-panumas-nikhomkhai-1148820--1-.jpg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: serverless
  slug: serverless
- name: servers
  slug: servers
seo_title: null
seo_desc: "The way things sit now, if you were somehow allergic to computers, you'd\
  \ be hard pressed to really banish them from your life, no matter where you found\
  \ yourself. \nTaking a quiet walk in the woods? What about the smartphone in your\
  \ pocket. Left the p..."
---

The way things sit now, if you were somehow allergic to computers, you'd be hard pressed to really banish them from your life, no matter where you found yourself. 

Taking a quiet walk in the woods? What about the smartphone in your pocket. Left the phone in the car? See that cell phone tower just behind those trees? The odds are good that the tower is more than just an antenna. It could also be hosting an edge computing server. And don't think that there weren't computers embedded into the under-the-hood workings of the car (or bus) that drove you over.

Allergies aside, if you want to fully grasp the current state of the compute world, it'll be helpful to understand all the places computers can pop up and what they might look like. 

In this article, we'll enumerate the classes into which modern compute devices can fall, and describe their strengths, weaknesses, and potential.

This is a chapter taken from the book, [Keeping Up: Backgrounders to All the Big Technology Trends You Can't Afford to Ignore](https://amzn.to/3FXXAfb). If you'd prefer to watch this chapter as a video, feel free to follow along here:

%[https://www.youtube.com/watch?v=0IW2GCTkCjI]

# What is a Server?

Honestly, I'd been working as a professional system administrator for a while before I could have properly answered that question. 

The truth is that every server is a computer, and any computer can be a server. The term _server_ simply implies that the device is providing some _service_ to at least one external device (known as a _client_).

If the printer that's plugged into your desktop computer can be shared by the other computers in your local network, then your desktop is a server (a _printer server_, to be precise). 

The WiFi router provided by your internet service provider is, by all definitions, a _network server_ – as it _serves_ network access to its clients. 

And the tiny, $5 Raspberry Pi Zero single board device that powers your homemade surveillance camera is a _video server_ – although that won't work without attaching a $7 camera module.

But that's not what most people are thinking about when they use the term. The first time I ever walked into the server room belonging to a mid-sized business, I was hit by the sound of dozens of powerful chassis fans and the heat from hard-working CPUs and fast-spinning disk drives. Instantly, I knew how folks normally use the word. 

I also soon discovered that the heat was a problem: the admins were struggling to keep their server room properly cooled and would, over time, end up having to write off some expensive hardware due to heat-related failures.

So, by "server," we usually mean computers installed within those rack-mounted, stackable cases built to efficiently house and protect highly performant, expensive, and delicate components. 

Server racks will normally live in well vented and cooled rooms with easy access to ample electrical power. You may have to search for them, but such rooms will also always contain colorful bundles of cabling, connecting the servers to networks.

As a rule, servers won't usually have displays or even keyboards plugged in, as they're likely to be managed remotely or, even more likely, fully automated and requiring no administration at all. 

Server farms belonging to giant cloud providers like Amazon Web Services will have many thousands of commodity computers running within aisle after aisle of vast warehouses. When one fails, a monitoring panel somewhere will light up and a technician will eventually be dispatched to remove the server, throw it out, and slide a replacement into the newly-available rack.

No tears are shed when we say goodbye to hardworking and devoted old hardware in those places.

# What is Linux?

Speaking of servers, did I mention that they all need some kind of operating system installed? 

And did I mention further that the vast majority of the servers powering the vast majority of the operations that make the internet and all its functionality possible are running the Linux operating system? Oh, and did you know that the open source Linux operating system is available for free?

I didn't mention all that? My bad.

Well, servers need operating systems. Most servers (well over 90 percent of the virtual machine instances running on Amazon's AWS EC2, for instance) run Linux. And Linux is, indeed, freely available for any use on any server, laptop, desktop, router, embedded system, or supercomputer. 

In fact every last one of the world's top 100 supercomputers uses Linux. And the Android smartphone OS? Yup. It's Linux, too.

Strictly speaking, "Linux" is the software kernel that allows a computer user to take control of a computer's physical hardware elements. The kernel translates your keystrokes into a format that will be understood by the drivers controlling your storage drives, memory, network interfaces, displays, and – in fact – keyboard and mouse. 

Many thousands of additional software programs are closely associated with Linux, but they're actually part of the user space that hovers "above" the Linux kernel.

Having said all that, Linux, including its broader software ecosystem, dominates the server computing market right now. The fact that you can freely install and fire up as many physical or virtual instances as you like makes Linux very attractive, especially in the scripted workload orchestration world. 

Virtualized Linux instances will often be brought to life and then, after completing a task that takes even a few seconds, killed off again. 

The versatility and flexibility Linux brings to computing have been the spark of some deeply impressive innovation and creativity.

Part of the Linux versatility is the fact that you can choose from among hundreds of variations (known as _distributions_). 

Are you looking to run enterprise-supported servers? Internet of Things (IoT) devices? Security testing machines? Multimedia management? Video or audio production? All of the above? None of the above? There's bound to be a distribution that's a good match for you. 

And if the exact specs you need can't be found, feel free to rewrite the kernel itself and create your own distro.

Full disclosure: I know a thing or three about Linux, being the author of Linux in Action (Manning), a coauthor of Ubuntu Bible (Wiley), and the author of the Linux Fundamentals learning path at Pluralsight.

Fuller disclosure: I'm writing this on an Ubuntu Linux workstation in my home, where all of our many devices have been Linux-powered for more than a decade.

# What is Virtualization?

We've already discussed virtualization in some depth as part of Chapter 3 (Understanding the Cloud), so we'll just cover some big-picture conceptual basics here.

In the old days, you'd come up with an idea for a new compute project and submit a proposal with your managers asking for money. When the project was green lighted, you'd estimate your requirements, solicit bids from hardware vendors, order a new server and, when it finally arrived, load it up with your application software. Then you'd fire it up, and let the world see what you'd done. 

That's the way things usually worked: One project. One server. Lots of waiting time.

But what if you overestimated your compute needs by 50 percent? That'd be a few thousand dollars down the drain. And if an important but lightweight project didn't really need a full, standalone server, you'd often have to buy it anyway. 

How about if the project would only have to run for a few months? Spend the money and hope you'll find a new use for the thing once your initial project shut down.

Awkward. Mountains of awkward.

Virtualization is a (mostly) software trick that lets you fool multiple installed operating systems into thinking they're all alone on a physical computer when they're really sharing it with other OS's. You can provision and run a single virtualization _host_ of one flavor or another and then fill it up with one or a hundred virtual servers.

One of those servers might need a lot of system memory but only a GB or two of storage space. Another one might be heavy on video conversion tasks and storage but is only needed for a half an hour a day. A third could be a 24/7 monitoring system that just needs a quiet place to do its thing without anyone bothering it. 

As long as you never push the physical host past its overall resource limits, the virtual machines can all coexist happily together. And when one service is no longer needed, you can reassign its freed-up resources to something else.

The ramp-ups and ramp-downs of a typical virtual server's life cycle are fast. For all intents and purposes, they'll generally launch and shut down instantly. 

This is possible because the underlying hardware is always running – and because the OS image is small and, usually, optimized for virtual environments.

As [we saw back in Chapter 3](https://www.freecodecamp.org/news/what-is-cloud-computing-beginners-guide/), cloud-hosted services are all virtualized. As more and more IT infrastructure moves to the cloud, more and more of your online activities will be driven by virtual machines. 

You won't notice the difference, but every time you search the internet or authenticate to an online account, there's a good chance that it's a container or VM you're connecting to, and not directly to a physical machine.

# Cloud Computing Terminology

Like virtualization, we also talked about the cloud back in chapter 3. We mentioned how the public cloud market was dominated by AWS and, to a lesser extent, by Microsoft's Azure. 

I'll just take a minute or two here to add a quick guide through some of the cloud industry's worst jargon.

**Infrastructure as a Service (IaaS)** environments give you full access to virtual server instances. The provider will ensure the underlying hardware, networking, and security elements are in place and functioning, while it's your job to manage the OS and other software running on your instance. 

Major IaaS players include Amazon's Elastic Compute Cloud (EC2) and Azure's Compute.

**Platform as a Service (PaaS)** environments hide most or all of the infrastructure administration tasks from you, leaving you with an interface where you can run your own data or code. 

One good example is AWS Elastic Beanstalk, which lets you upload your application code from where it'll be automatically deployed to Amazon's cloud. Other providers in this space include Heroku and Salesforce Lightning Platform.

**Software as a Service (SaaS)** environments expose only an end-user interface, managing all layers of the administration infrastructure invisibly. 

Microsoft's Office 365 and Google's G Suite are widely used SaaS office productivity tools. 

But there's a growing marketplace of SaaS tools providing online software equivalents to many applications that, in years past, could only be used on standalone workstations. Those applications include accounting, computer assisted design (CAD), and graphic design solutions.

**Consumption-based pricing** or, as it's sometimes known, pay-as-you-go billing, is a cornerstone of the cloud concept. The idea is that you don't have to gamble by investing up-front in infrastructure, but you can pay incremental amounts for units of compute services as you use them.

It might not always come out cheaper in the long-run. But pay-as-you-go definitely makes it easy to test application stacks and experiment with multiple alternative configurations before pulling the trigger on a full deployment. 

It also means that – assuming you don't make any dumb configuration mistakes – it's nearly impossible to badly over-provision.

**On-demand** is also sometimes referred to as self-service. The ability to request instant delivery of compute resources any time of the day/week/year gives you complete control over your organization's application life cycles. You're never at the mercy of other people's schedules and limitations.

**Service Level Agreements (SLAs)** are legal disclosures published by companies in the business of providing services. 

Even if the standard of resource reliability provided by the major public cloud platforms is generally excellent, accidents will happen. When you pay hourly or monthly fees for cloud services, the company's SLA tells you that you should anticipate downtime of a certain number of minutes or hours each month. 

As an example, Amazon's SLA sets its EC2 availability rate at 99.99% each month. If, in a particular month, you encounter greater downtime, you might be eligible for service credits or refunds.

**Multitenancy** is the placement of virtual instances belonging to multiple cloud customer accounts on a single hardware resource. 

A multitenancy setup for a server instance will probably be significantly less expensive than a dedicated instance. Choosing a dedicated instance, however, would guaranty that your instance will never be hosted on a physical server alongside an instance from a second account. Security or regulatory considerations might require that you avoid multitenancy.

**Migration** describes the process involved with moving existing business application and database workloads from local (on-premises) deployments to a cloud provider. Providers often make specialized tools and free tech support available for migrations.

**Elasticity** describes the ways virtualized cloud resources can be quickly added to meet growing demand or, equally quickly, reduced in response to dropping demand. 

Elastic resources are especially well-suited to maintaining application availability and health without incurring unnecessary costs. Elasticity can usually be automated, so applications will respond instantly to changing environments without the need for manual intervention.

# What is "Serverless" Computing?

Serverless computing is no different from server computing. It's just that, even if you squint your eyes real tight, you don't get to see the server. 

Or, to put it another way, serverless computing is like running a virtual server instance, but without having to configure its instance settings or log in to set things up.

In other words, you can't run software code of any kind without a computer somewhere processing your commands. So let's say that serverless is a form of virtualization where everything except your application code is abstracted. 

In that sense, serverless platforms like Amazon's Lambda and Azure's Functions are a lot like the model used by Amazon Elastic Beanstalk. But they're so simple to use that they can easily be incorporated into a larger, highly automated multi-tier workload.

# What is Edge Computing?

Latency is the term we use to describe the time it takes for data to travel from a remote server across a network to your computer – or back in the other direction. Assuming you prefer fast service over slow service (which seems a safe assumption), high latency numbers are a bad thing.

Network engineers can invoke various magical spells – Oops! I mean clever configuration efficiencies – to reduce delays due to latency. 

But no matter how many tricks they're hiding in their mysterious black bags, they can't ignore the laws of physics. Even using the best connections and configuration profiles, data still has to physically move across the distances between remote locations.

The only way to reduce this kind of latency is to shorten the distance. I suppose that one way would be for online service providers to very politely ask their customers to sell their houses and move somewhere closer to the servers running in the office (as if real estate prices weren't already high enough in Silicon Valley). 

Alternatively, though, how about moving the server closer to the customer?

Ah. You've discovered edge computing: the fine art of installing large distributed networks of smaller servers where mirror copies of server data can be stored and, when necessary, fed to any customers in the area who initiate requests. 

If you've got enough of those servers spread evenly through the geographic regions where you customers live, then you can significantly reduce the latency they experience.

One kind of edge computing that performs this function is known as a content distribution network (CDN). Cloudflare and Amazon's CloudFront are among the larger CDNs currently in operation.

Edge computing resources like those used by CDNs have also increasingly been used to manage large streams of data from and to IoT devices like the computers embedded in cars. Placing capable compute devices at the edges of large networks makes it possible to consume and transform such data sets faster than by moving the data all the way back to the more distant cloud.

# What Are the Key Compute Form Factors?

Computers, like egos, come in all shapes and sizes. Would you like to carry a rack full of bare metal servers around in your pocket to pay for your shopping? You're probably better off using some kind of mobile payment app on your smartphone.

Size matters. A lot. A device's form factor will determine the dimensions and capacity of its internal components. That means the particular motherboard, memory modules, storage drives, peripheral ports, and power supply you select for a device will be limited by your overall form factor.

The form factor you choose – for either a new project or just for your personal use – will generally be obvious (server racks can be heavy and don't handle travel well). But knowing what's available can make it easier to plan.

## Devices using video displays

The term _personal computer_ (PC), these days, is used to describe either desktop or laptop computers. 

Laptops, since they're designed to be mobile, are largely self-contained. Desktops, by contrast, generally come with the core compute elements within a box that includes external ports for connecting peripherals like keyboards and monitors. 

While you can find computers with power and functionality that's comparable to PCs in very small (credit-card sized) cases, the larger boxes used by desktops allow for easier customization and upgrades.

Gaming consoles – like Sony's PlayStation, Microsoft's Xbox, and the Nintendo Switch – are effectively the equivalent of desktop PCs, except that their software is built on closed systems. 

They're "closed" in the sense that their software interface exposes only the functionality the manufacturer wants you to see. Modifying or customizing the OS or internal works of a game console is normally impossible.

A touchscreen device uses the gestures and taps it senses from users as input devices in place of the traditional mouse or keyboard. Touchscreen technologies are the primary inspiration behind smaller form factors for consumers, since there's no need for external input devices. 

This, more than just about anything else, has driven the tremendous growth of the tablet and smartphone markets. (It also explains the freakishly agile thumbs of entire generations of young people.)

## Devices without video displays

The router that connects devices to a network through either WiFi or ethernet cables contains pretty much the same internal motherboard and network interfaces that you'd find in any other compute device. 

The big difference is that there's no HDMI, DVI, or VGA video port. Routers are meant to run autonomously and, when administration is necessary, it'll usually happen through a browser interface across a network.

You launch an admin session with your router by entering its IP address into your browser and authenticating when prompted. In some cases, you can also launch terminal sessions through the Secure Shell (SSH) protocol.

This remote administration model is shared by many display-less device types. Those will include medical (and non-medical) implants or _wearables_ that come with tiny computers built to monitor, report, or even interact with their host environments. 

(In the context of wearables, I would at least briefly discuss smart watches here but, for the life of me, I can't figure out why anyone would want one.)

Display-free computers are also embedded in medical devices, appliances, cars, logistics fleets and industrial machinery. All of those embedded computers are components of the growing internet of things.

Thanks for reading!

_YouTube videos of all ten chapters from this book [are available here](https://www.youtube.com/playlist?list=PLSiZCpRYoTZ6UWl4xialvwLOKyHYYJUiC). Lots more tech goodness - in the form of books, courses, and articles - [can be had here](https://bootstrap-it.com). And consider taking my [AWS, security, and container technology courses here](https://www.udemy.com/user/david-clinton-12/)._

