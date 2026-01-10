---
title: Digital Connectivity – How We Connect to the Internet and IoT Explained
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-01-24T17:08:41.000Z'
originalURL: https://freecodecamp.org/news/digital-connectivity-internet-and-iot-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-andrea-piacquadio-935743.jpg
tags:
- name: internet
  slug: internet
- name: Internet of Things
  slug: internet-of-things
seo_title: null
seo_desc: "Telephones changed the way we all talked to each other and went about our\
  \ work (well, the way our great-grandparents did, at any rate). Information could\
  \ now be communicated instantly, rather than being sent over slow, overland routes.\
  \ \nBut that's ha..."
---

Telephones changed the way we all talked to each other and went about our work (well, the way our great-grandparents did, at any rate). Information could now be communicated instantly, rather than being sent over slow, overland routes. 

But that's hardly news to anyone these days. The modern network – best known through its internet iteration – similarly boosted communication, although this time it was the movement of data rather than voice that got a boost.

In the fifty years or so since the birth of the internet, it's been trusted with the movement, storage, and management of more and more of our data. 

These changes have brought tremendous opportunities, risks, and pressures. Just getting connected is now a basic necessity. Managing all of our many connected devices and leveraging the ways we authenticate to extend our identities also present challenges. We'll discuss all that here.

This article was taken from the book, [Keeping Up: Backgrounders to All the Big Technology Trends You Can't Afford to Ignore](https://amzn.to/3FXXAfb). If you'd prefer to watch this chapter as a video, feel free to follow along here:

%[https://www.youtube.com/watch?v=FnTCMZFe2ww]

# How We Connect to the Internet

These days, after food and shelter, pretty much the most basic resource of all is internet connectivity. If you can't access the internet, you'll find it difficult to do your banking, educate yourself, book travel arrangements, or even figure out exactly where you are. 

It's not for nothing that widespread, reliable, and relatively fast internet access is critical for a region's general economic development.

Even though the internet was originally build as a decentralized, distributed network of resources, you still need to establish some kind of connection to access it. 

The best connections are run by network carriers, known as _tier 1 networks._ Theses networks can reach all other networks through a peering arrangement that doesn't require payment for IP transit. You can think of these networks as the backbone of the internet, and their network infrastructure is its structure.

Examples of companies managing tier 1 networks include AT&T and Verizon in the US, Tata Communications (India), and Deutsche Telekom (Germany). Those carriers will resell bandwidth to smaller internet service providers (ISPs) who, in turn, sell access to end users like you and me.

## Broadband Options

Individuals looking for broadband access in their homes or small businesses can usually choose between one of four access models:

* **Cable**. Since they're already in the business of providing data to millions of homes over existing physical connections, cable TV providers can easily transmit internet over the same wires.
* **Digital subscriber line (DSL)**. A family of technologies that permit digital data across copper telephone lines, DSL can provide a roughly similar level of service as cable, but without the need for an underlying cable subscription. In fact, using a "dry copper" connection, you don't even need a telephone landline account.
* **Fibre optics**. Due to some arcane technical details (including the laws of physics), transmitting digital signals as infrared light can happen faster and require fewer repeaters than comparable electrical cables. A fibre optics internet connection could typically deliver transfer speeds of 10-40Gbit/s – a thousand times faster than currently standard rates using cable or DSL.
* **Satellite**. Running new cable through densely populated cities is expensive, but companies can quickly make their money back through the many access contracts they'll sign. But sparsely populated rural regions are much more difficult to service. Partly to fill a rural connectivity gap, a number of companies ambitiously working to launch constellations of thousands of orbiting satellites to provide universal internet coverage. As of this writing, SpaceX is furthest along with its project, having already successfully launched more than 500 satellites as part of the Starlink system.

Besides those dominant technologies, there have been more than a few alternate connectivity solutions attempted. Some are experimental but promising, and others are a bit more speculative. 

Google's Balloon Internet (known officially as Loon LLC), is an attempt to float fleets of high-altitude balloons providing a 1 Mbps signal to anyone within range on the ground. 

Loon is designed to provide low-end broadband in hard-to-reach regions where reliable service has been difficult or even impossible. As of 2020, the project seems to be in a late experimental stage.

Broadband over power line (BPL) can take advantage of all the electrical grid that connects power authorities with homes and businesses to provide internet data. Ultimately, the technology delivers limited bandwidth because line noise causes significant data signal loss. 

Data carrying power lines can also cause interference with high frequency radio communications. In the end, relatively low signal quality and strong competition from other technologies mean that BPL will probably never be widely adopted.

Networks using forms of wireless Internet service provider (WISP) can service homes and offices across larger geographic areas without the need to physically wire every building. Wired connections are installed in an area's center and, where necessary, connected backhauls are installed in elevated areas to strengthen the wireless signals aimed at consumers. 

Existing radio towers or other tall structures can be used for the backhaul repeaters, making a WISP system relatively inexpensive to install.

Smaller-scaled wireless network co-ops can be shared locally using a neighborhood internet service provider (NISP) (using rooftop antennas) or a wireless mesh network (where network-connected devices act as peer nodes) to efficiently share a single physical connection.

Those systems are primarily designed to serve us where we live and work. But mobile data access is definitely also a thing. I'm sure you're already familiar with data plans that mobile phone companies can provide alongside their calling and texting services.

## Mobile Phone Data Access

Cell connectivity is distributed through geographic areas (known as "cells") from individual radio transmitters spread throughout the cell. 

Since the transmitters within each cell will use different radio frequencies than the cells around it, modern wireless technologies permit a seamless, automated "handover" as a user moves between cells.

The technologies used for wireless telephony have changed since the 80s, when what's now known as 1G ("First Generation") cell phones were introduced. To describe the evolution of cell phones in very general terms, we could say that:

* **1G** phones carried only voice communications and had a maximum transfer speed of 2.4 Kbps.
* **2G** phones could carry Short Message Service (SMS) and Multimedia Messaging Service (MMS) messaging, which could include short videos and images.
* **3G** phones had much higher transfer rates (as high as 2 Mbps) than any variant of 2G and was therefore dubbed, "mobile broadband."
* **4G** phones could reach speeds as high as 100 Mbps, which permitted HD mobile TV, online gaming, and video conferencing.
* **5G** phones – when used on compatible networks – are expected to reach transfer speeds of up to 20 Gbps at a very low latency, permitting fully immersive virtual environments. Should the 5G rollout be successful (and, at the time of writing, this isn't yet clear), the range and limits of new service categories that could be deployed is not yet known.

When it comes to planning a new venture, it's long been the accepted wisdom that there's no replacement for solid market research. Without knowing who your customers will be, where they live, and what they like, how can you properly serve them? 

Well, now you can add to that list "how reliable and robust is their internet connectivity," because without digital access, they may never find you or be able to consume your service.

# Talking to the Internet of Things

Two recent changes are, more than anything else, responsible for the internet of things (IoT) ecosystem: the availability of cheap, embedded, single-board computers (like the Raspberry Pi) and cheap and always-on internet connectivity.

Those tiny single-boards – often smaller than a credit card – are easy to incorporate into just about anything you're planning to manufacture. 

Such devices cost very little – sometimes just a few dollars a piece – and they're generally built to run fully-powered (and free) Linux distributions. And network availability means that the vast streams of data generated by all those on-board cameras, sensors, and other peripherals, can be automatically sent back "home" for processing and analysis.

## The Dream of IoT

Here are some ways that IoT applications are already actively changing business and consumer practices:

### Inventory control

The very first IoT device was – arguably at least – a Coca-Cola vending machine at Carnegie Mellon University. Back in the early 80s, the machine was modified to digitally report its ongoing inventory. 

The simple idea that physical devices can monitor themselves and their surroundings, providing accurate, up-to-the-minute status reports to remote servers, lies at the heart of countless modern industrial solutions. 

Modern retail, wholesale, logistics, and manufacturing operations now have constant access to their inventories, allowing them to understand trends and anticipate problems.

### Agriculture

Increasingly, modern farming incorporates robotic irrigation, fertilization, planting, and even harvesting technologies. 

All those robots running around your property are generating data and, from time to time, getting themselves into trouble. 

Moving that data "back" to administration servers is critical for keeping track of what's going on, what might need fixing, and how your actual farm is performing. You can, therefore, expect that each of those devices will be part of someone's IoT.

### Military

Communication is key for military operations. But if even weapons, vehicles, and other equipment can communicate autonomously, and if there are servers dedicated to interpreting and acting on that communication, then you're already way ahead of the game. 

Sensors connected to each of hundreds of components for, say, a fighter jet, can contribute to giving planners an unprecedented view of what's really going on.

### Smart cities

When sensors embedded in buildings, roads, public lighting, smartphones, and electrical systems are combined with data coming from traffic cameras and public departments, the potential for data-driven insights is huge. 

Properly understood data can help cities manage their resources, utilities, and even traffic more efficiently, and better maintain their physical infrastructure.

### Smart homes

On a far smaller scale than smart cities, home appliances can be connected and monitored and controlled through smartphone apps or remote servers. 

Smart home devices already include heating and cooling systems, light bulbs, robotic vacuum cleaners, garage doors, and security systems. Smart home devices can be controlled through phone apps but, in many cases, also through voice controlled devices like Amazon Echo (Alexa).

Conversations about IoT are always just one step away from _buzzwordism_ – where words lose meaning and exaggeration becomes an acceptable lifestyle choice. 

Not all IoT stuff is actually IoT. Or, to put it another way, not all IoT is worth talking about. But here's one good way to categorize a particular technology: if, hour after hour, something generates more data than any human being could possibly absorb, then it's probably an IoT device.

Effectively dealing with all that data can be a problem. And that's not the only potential for trouble in IoT land.

## The Nightmare of IoT

In the information technology world, as a general rule, the more active network connections you have in your infrastructure, the greater your risk of being successfully attacked. 

That's because successful hacker intrusions usually come through badly configured or unpatched devices. The more public-facing devices you're exposing, the greater the chance one of them will have a serious vulnerability.

What kind of vulnerabilities are we talking about? Well, the US government's Common Vulnerabilities and Exposures database contains nearly 140,000 individual entries, each one representing a unique software weakness that could allow unauthorized access to and destruction of an IT system. 

There are threats impacting all operating systems (Windows, Linux, macOS), all formats (server, PC, smartphone), and all ages (there are active threats going back to the 1990s). And many hundreds of new entries are added each month.

In that sense, IoT devices are no different than any other kind of computer. But there is one way that they're a whole lot worse. Because you don't normally directly interact with IoT devices on an OS level, and because they're often commodity items that are purchased and deployed by the dozens or thousands, you don't instinctively treat them like computers.

Most of us, as an example, are aware that we should create complex and unique passwords for our laptops and WiFi routers. But your fridge? Just plug it in and it'll be fine! The problem is that many IoT devices – like "smart" fridges – have their own embedded operating systems and, usually, their own network interfaces.

There's a good chance that anyone driving down your quiet residential street can scan for available networks, quickly identify the brand of IoT device you're using, assume that you haven't changed the authentication credentials from their factory defaults, and log in to your private network. 

What makes things much worse is that many device manufacturers are still shipping their products with authentication credentials using some variation of admin/admin.

That's a big problem.

# Leveraging Federated Identities

All this talk about the dangers presented by authentication and credentials should make you curious about how they can be used to generate some _good_ connectivity stuff. 

In a single word, that'd be _federation._ Identity federation is a technology for linking a single person's identity across multiple network services. Federation is what lets you log in to online gaming or web application sites using, say, your Google account credentials.

The upside of federation is that a single login can be all you'll need as you move between many of the online services you regularly use. That lets you reduce the risk of exposing your password through a vulnerable website. 

Of course, it also increases the damage that can come from a serious data breach of the servers used by your federation provider.

Federation can be used to integrate with third party single sign-on (SSO) authentication systems, like Kerberos, the Lightweight Directory Access Protocol (LDAP), and Microsoft's Active Directory (AD). When used with cloud services, SSO systems can securely permit automated as-needed access to private account resources for consumers or processes.

Besides convenience, all this authentication goodness drives opportunities for secure remote collaboration on large, complex projects – itself a fast-growing trend.

_YouTube videos of all ten chapters from this book [are available here](https://www.youtube.com/playlist?list=PLSiZCpRYoTZ6UWl4xialvwLOKyHYYJUiC). Lots more tech goodness - in the form of books, courses, and articles - [can be had here](https://bootstrap-it.com). And consider taking my [AWS, security, and container technology courses here](https://www.udemy.com/user/david-clinton-12/)._

