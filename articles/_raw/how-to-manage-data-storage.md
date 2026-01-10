---
title: How to Manage Data Storage
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-02-14T19:44:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-data-storage
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-tima-miroshnichenko-6549629.jpg
tags:
- name: data
  slug: data
- name: database
  slug: database
- name: storage
  slug: storage
seo_title: null
seo_desc: "We've all been at this 21st Century thing for a while. And by now it's\
  \ pretty clear that data is the big driver of, well, of everything. \nGovernments\
  \ build their policies around economic and population data. Scientists build their\
  \ theories around env..."
---

We've all been at this 21st Century thing for a while. And by now it's pretty clear that data is the big driver of, well, of everything. 

Governments build their policies around economic and population data. Scientists build their theories around environmental, physical, and biological data. Businesses build their plans around production, sales, and consumer behavior data.

This article was taken from the book, [Keeping Up: Backgrounders to All the Big Technology Trends You Can't Afford to Ignore](https://amzn.to/3FXXAfb). If you'd prefer to watch this chapter as a video, feel free to follow along here:

%[https://youtu.be/JvoguWXO-lg]

Data is being generated at rates previously undreamed of. I've read that the sensors on a pair of General Electric GEnx engines on a Boeing 787 Dreamliner generate a terabyte of data each day. 

A single network-connected car (like a Tesla) might upload around 100MB of location, performance, and maintenance-related data on any average day. 

Multiply that by the millions of such cars that will soon be in use around the world, and multiply _that_ number by the thousands of other devices that are out there, and the scale of the data "problem" should be clear.

Got plans to add your own data to the flood and you feel the need to save and store it, too? You'll need to be able to explain why you need it so you'll know how it should be done. 

I can't help you with that "why," but I think I can give you some useful thoughts about the "how."

The _way_ you store data will depend on what it looks like as it's produced and how you may need to access it later. _Where_ you store your data will depend on how much of it there is, how deeply you'd be impacted by its loss, and how often you'll need to take it out and play with it. Let's take a look at both of those variables.

# Data Storage Formats

Since not all data is created equal, it'll make sense to look for the tools and environments that'll most closely match the work you're planning to do. Here are some options:

## Spreadsheets

They may be flashy, colorful, consumer-facing applications, but spreadsheets are no lightweights when it comes to serious data processing. 

As we'll see in more detail a bit later, spreadsheets have their limitations. But when it comes to presenting data in visually accessible ways, applying mathematical, statistical, and financial operations to that data, and even integrating remote data sources (like stock market quotes), no other tool comes close.

Spreadsheets can import simple, plain text data from files of just about any size as long as the text can be delimited. That is, breaks between data divisions should be marked by some consistent character. 

When you import the data, you can specify the appropriate delimiter. Tabs, hard returns, and commas are common delimiting characters. In fact, the popular acronym _CSV_ stands for _comma-separated values._ 

Here's what a few lines of CSV text might look like. Note that the first row contains column headings. Spreadsheets can easily understand how those should be treated differently.

```
Year,Volume,Rate,Growth
2015,56,10,15
2020,90,11,(2)
2022,109,8,12

```

Spreadsheets display their data in cells, which are arranged into horizontal rows and vertical columns. You an apply functions to the contents of individual cells or to some or all of the cells in a column or row, and can incorporate values in cells in relative locations. 

Data sets within a spreadsheet can be rendered as graphs. Spreadsheets can also be used as web forms where users can input data that's saved for future use.

The most popular spreadsheet is probably Microsoft's Excel, which is part of their Microsoft 365 Office Suite. But feature for feature, the open source Calc that comes with the LibreOffice suite is a viable alternative. Google Sheets is a cloud-based spreadsheet solution that may lack some of the feature depth of the others, but is a strong collaboration tool.

## Databases

As a rule, databases are not built for visualizing data in attractive and intuitive formats. And, on their own, they're not known for complex mathematical calculations either. But boy, can they handle extra-large data sets and multi-table relationships.

When I say that databases don't really help you visualize your data, that's generally because they're meant to be used "behind" front end applications in multi-tier deployments.

For instance, an e-commerce website will display web pages where users can browse what you've got for sale, add items to a virtual shopping cart, and check out using their payment information. 

The web page itself just draws a graphical interface and shows you where to click your mouse, but the information about the items you're selling - including their price and associated images - are probably retrieved from a backend database whenever the page loads.

Similarly, your selections and, eventually, payment information will be written to a different database. The software process that handles your shipping might later consult the payment database for the shipping address. Databases are there at every stage, but no one will ever actually see them.

Administrating large databases so they're efficient, secure, and reliable takes serious engineering and, in some cases, an enormous amount of money. 

Before you build your database deployment, you'll need to know whether your operation requires strong Atomicity, Consistency, Isolation, and Durability (ACID) and support for complex and flexible queries. If it does, you may be looking for a relational database engine like SQL Server, MariaDB, or Amazon's Aurora. 

Or perhaps you need speedy performance and would prefer a more flexible schema-less environment (suggesting you'd be better off with a NoSQL solution, like MongoDB or Redis).

_SQL_, by the way, stands for _structured query language_ - which is an established syntax for using language-like code for interacting with your data.

Counterintuitively, depending on who you ask, _NoSQL_ might not stand for _Not SQL_. Some prefer to think of it as _Not Only SQL_ instead.

## Jupyter Notebook

Don't think you have to consume your data using the same tool that's storing it. It's possible, for example, to import existing data that's stored either locally or at a remote site into an interactive compute environment like a Jupyter Notebook. 

The advantage of this kind of setup is that the data can now be addressed within the context of, say, a robust Python programming environment without actually touching - or potentially corrupting - the original source.

The open source JupyterLab is a popular resource for working with large data sets using Python. You can download and build your own JupyterLab or run it remotely through a cloud provider like Amazon's Elastic Map Reduce service, or Microsoft's Azure Notebooks. 

For particularly large data sets - especially those that already live in the cloud - an existing cloud platform can make sense.

# Data Storage Devices

Although it's not quite this simple, let's say that there are four broad categories of data storage media drives:

* Magnetic tape on open reels, cartridges, or cassettes
* Optical including Compact Disk (CD) and Digital Video Disc (DVD)
* Magnetic media in 2.5 and 3.5 inch drive casing - including spinning hard drives
* Solid state including SSD drives in 2.5 and 3.5 inch drive casing, SD cards, and USB flash drives

A few magnetic tape systems may still exist here and there, but the days of laboriously and slowly copying large data sets to banks of multiple backup tapes - and hoping the backup would actually work - are pretty much over. Trust me: no one is complaining. 

CDs and DVDs are headed the same direction. Their maximum capacities are no match for the sheer volume of today's enterprise data needs, and consumers don't make local copies of nearly as many large media files as they once did.

Which leaves spinning magnetic and solid state drives.

Gigabyte for gigabyte, spinning hard drives are probably still a bit less expensive than their solid state equivalents (although the price difference is narrowing), but the performance gains delivered by SSDs are very noticeable. 

Some time ago, I realized that I could actually _save_ money by buying smaller capacity SSDs for my personal workstations and laptops instead of larger hard disk drives (HDDs).

Let me explain. The way we use data on our personal computers has changed in recent years. Rather than storing media and software archives locally, we're much more likely to assume they'll be available to stream or download whenever we need them. 

For most of us, faster download speeds have made "living in the cloud" easy. So we normally just don't need as much storage space any more. 

The 500GB SSD drive plugged into my busy workstation is barely half full - even taking into account the dozen or so virtual machines and the many ISO images I've got there. And the drive cost me less than I would have paid for a one or two terabyte HDD.

One of the primary roles of storage is data backup. Rather than physically transferring backups between media, local data archiving - using either SSD or HDD media - generally works by moving archives across networks. 

The trick is designing a backup system that automatically provides you with sufficient duplicates of your archives, rotates them through appropriate life cycles (where, eventually, they're retired and destroyed), and all without generating unnecessary network traffic overhead.

Besides backups, you'll also often want to share data among users working throughout your campus. 

Two tools for managing both backups and file sharing are network-attached storage (NAS) and storage area networks (SAN). Their similar names suggest they're in the same business. Trust me: they're not.

## Network-attached storage (NAS)

NAS is a relatively simple and inexpensive way to share files across a local network. It works through a standalone server device that contains multiple storage drives. The drives will normally be configured as a Redundant array of inexpensive disks (RAID) array to provide redundancy and performance benefits.

The NAS device connects to the network over ethernet cabling and uses regular TCP/IP networking. Client machines in the LAN will see the NAS resources through standard file sharing protocols like Server Message Block (SMB) and Network File System (NFS).

NAS solutions can be great for smaller home or office environments, but the fun will quickly fade as you grow. NAS devices themselves are generally not powerful enough to handle too much of a client workload, and working with large files over an ethernet network may slow things down.

## Storage area network (SAN)

If NAS setups are "relatively simple and inexpensive," SANs are complex and expensive. Not by accident were they designed for large enterprise deployments. As a result of the high end hardware you throw into a NAS system, performance will be great and you'll scale much further.

Rather than ethernet, SANs run through much faster Fibre Channel switches (or, sometimes, the slower iSCSI). They provide block-based storage rather than file systems and are mounted on client machines as local drives.

# Data Storage Services

As internet connection speeds have improved, it's become more practical to move at least some data archives to the cloud. 

Instead of local backups - which could be lost in a catastrophic event like a fire - data could regularly be saved to online platforms. Once there, you'd have a viable, off-site backup. But, if you wanted, you'd also have access to that data from anywhere on earth. If you work remotely with a distributed team, that can be helpful.

You probably already own and have even collaborated on documents that live on Dropbox, Microsoft 365, or Google Drive. For most people, the primary point of interaction for those services is a web browser. 

But serious data management - or even relatively complex and regular file backups - aren't practical within a browser. So cloud computing providers offer storage and archiving services whose administration can be scripted and automated.

Cloud storage services, like Amazon's Simple Storage Service (S3), provide full archive life cycle management. Data that must remain highly available could, for example, be saved to the S3 Standard storage class. 

After a few months - when you're less likely to need the data, but must still retain a copy for regulatory reasons - you could move your archive to the cheaper S3 Glacier class. Data in Glacier is secure and durable, but would take much longer to access. 

After a full year you might be able to delete it altogether. Better yet, there are simple ways to automate the way your data moves through its life cycle.

All major cloud providers will have their own comparable data storage services. Naturally, prices and exact service features will differ from one another. And, of course, feature and pricing details will often change.

It may not always be practical to transfer data to the cloud over the internet. Extremely large data sets can take a very long time to upload even using fast internet connections. 

Sure, if you're lucky enough to have a fibre optics connection giving you one gigabyte/second, then a one terabyte upload would take only two and a half hours or so (assuming no one else was using the connection).

But what about 100 TBs of data (that'll take you more than ten days)? And what if you only get 100MB/second (more than three months)? In cases like these, if you're uploading jumbo-sized archives weekly or have other uses for your internet connection, then uploading isn't an option.

For such cases, you can still get your data into the cloud, but it'll have to find another ride. AWS, as it turns out, offers their Snow Family services. 

Snowball is a large, secure storage device. It can be safely shipped to AWS customers, loaded up with dozens of terabytes of data, and then shipped back. Once back home at Amazon, the data will be directly uploaded to a bucket in the customer's account. Alternatively, Snowballs can be kept on-location and used as edge compute devices.

Snowball's big brother is AWS Snowmobile, a 45-foot long secure shipping container capable of handling Exabyte-scale digital migration. 

Snowball's little cousin, AWS Snowcone, is a rugged container the size of a tissue box that can handle eight TB of usable storage, along with the possibility of virtual cloud instances and network connectivity to the AWS cloud. Besides transferring your data, Snowcones can be used as highly mobile edge compute devices in their own right.

And that's it for today. Thank you for reading. Now, hopefully you better understand how we store data and what your data storage options are.

_YouTube videos of all ten chapters from this book [are available here](https://www.youtube.com/playlist?list=PLSiZCpRYoTZ6UWl4xialvwLOKyHYYJUiC). Lots more tech goodness - in the form of books, courses, and articles - [can be had here](https://bootstrap-it.com). And consider taking my [AWS, security, and container technology courses here](https://www.udemy.com/user/david-clinton-12/)._

