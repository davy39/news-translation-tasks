---
title: How Apache Nifi works — surf on your dataflow, don’t drown in it
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-03T15:42:14.000Z'
originalURL: https://freecodecamp.org/news/nifi-surf-on-your-dataflow-4f3343c50aa2
coverImage: https://cdn-media-1.freecodecamp.org/images/0*cAhBbxvhy-AOtmml
tags:
- name: apache
  slug: apache
- name: data
  slug: data
- name: Productivity
  slug: productivity
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By François Paupier

  Introduction

  That’s a crazy flow of water. Just like your application deals with a crazy stream
  of data. Routing data from one storage to another, applying validation rules and
  addressing questions of data governance, reliability ...'
---

By François Paupier

### Introduction

That’s a crazy flow of water. Just like your application deals with a crazy stream of data. Routing data from one storage to another, applying validation rules and addressing questions of data governance, reliability in a Big Data ecosystem is hard to get right if you do it all by yourself.

Good news, you don’t have to build your dataflow solution from scratch — Apache NiFi got your back!

At the end of this article, you’ll be a NiFi expert — ready to build your data pipeline.

#### What I will cover in this article:

* What Apache NiFi is, in which situation you should use it, and what are the key concepts to understand in NiFi.

#### What I won’t cover:

* Installation, deployment, monitoring, security, and administration of a NiFi cluster.

For your convenience here is the table of content, feel free to go straight where your curiosity takes you. If you’re a NiFi first-timer, going through this article in the indicated order is advised.

#### Table of Content

* I — [What is Apache NiFi?](#741e)  
- [Defining NiFi](#9421)   
- [Why using NiFi?](#6cf2)
* II — [Apache Nifi under the microscope](#b75e)  
- [FlowFile](#61bd)   
- [Processor](#d187)  
- [Process Group](#924a)  
- [Connection](#af10)  
- [Flow Controller](#8ca0)
* [Conclusion and call to action](#812c)

### What is Apache NiFi?

On the [website](https://nifi.apache.org/index.html) of the Apache Nifi project, you can find the following definition:

> An easy to use, powerful, and reliable system to process and distribute data.

Let’s analyze the keywords there.

#### Defining NiFi

**Process and distribute data**  
That’s the gist of Nifi. It moves data around systems and gives you tools to process this data.

Nifi can deal with a great variety of data sources and format. You take data in from one source, transform it, and push it to a different data sink.

![Image](https://cdn-media-1.freecodecamp.org/images/oizS79jFx3hHFoRF7DfXvQya-hmSTbdlUbc1)
_Ten thousand feet view of Apache Nifi — Nifi pulls data from multiple data sources, enrich it and transform it to populate a key-value store._

**Easy to use**  
Processors — _the boxes —_ linked by connectors — _the arrows_ create a flow_. N_iFi offers a [flow-based programming](https://www.wikiwand.com/en/Flow-based_programming) experience.

Nifi makes it possible to understand, at a glance, a set of dataflow operations that would take hundreds of lines of source code to implement.

Consider the pipeline below:

![Image](https://cdn-media-1.freecodecamp.org/images/SDRmBt5o7tQkjmIn5iObqW6-spFw-NFEzaH4)
_An overly minimalist data pipeline_

To translate the data flow above in NiFi, you go to NiFi graphical user interface, drag and drop three components into the canvas, and   
That’s it. It takes two minutes to build.

![Image](https://cdn-media-1.freecodecamp.org/images/phn6Q-c9SkDImkbUt6FVHkuiojIRTiBuuuzJ)
_A simple validation data flow as seen through Nifi canvas_

Now, if you write code to do the same thing, it’s likely to be a several hundred lines long to achieve a similar result.

You don’t capture the essence of the pipeline through code as you do with a flow-based approach. Nifi is more expressive to build a data pipeline; it’s _designed to do that_.

**Powerful**  
NiFi provides [many processors](https://www.nifi.rocks/apache-nifi-processors/) out of the box (293 in Nifi 1.9.2). You’re on the shoulders of a giant. Those standard processors handle the vast majority of use cases you may encounter.

NiFi is highly concurrent, yet its internals encapsulates the associated complexity. Processors offer you a high-level abstraction that hides the inherent complexity of parallel programming. Processors run simultaneously, and you can span multiple threads of a processor to cope with the load.

Concurrency is a computing Pandora’s box that you don’t want to open. NiFi conveniently shields the pipeline builder from the complexities of concurrency.

**Reliable**  
The theory backing NiFi is not new; it has solid theoretical anchors. It’s similar to models like [SEDA](http://sosp.org/2001/papers/welsh.pdf).

For a dataflow system, one of the main topics to address is [reliability](https://whatis.techtarget.com/definition/reliability). You want to be sure that data sent somewhere is effectively received.

NiFi achieves a high level of reliability through multiple mechanisms that keep track of the state of the system at any point in time. Those mechanisms are configurable so you can make the appropriate [tradeoffs](http://apache-nifi-users-list.2361937.n4.nabble.com/template/NamlServlet.jtp?macro=print_post&node=1532) between latency and throughput required by your applications.

NiFi tracks the history of each piece of data with its lineage and provenance features. It makes it possible to know what transformation happens on each piece of information.

The data lineage solution proposed by Apache Nifi proves to be an excellent tool for auditing a data pipeline. Data lineage features are essential to bolster confidence in big data and AI systems in a context where transnational actors such as the European Union propose [guidelines](https://ec.europa.eu/futurium/en/ai-alliance-consultation/guidelines/1#privacy) to support accurate data processing.

#### Why using Nifi?

First, I want to make it clear I’m not here to evangelize NiFi. My goal is to give you enough elements so you can make an informed decision on the best way to build your data pipeline.

It’s useful to keep in mind the [four Vs](https://www.dummies.com/careers/find-a-job/the-4-vs-of-big-data/) of big data when dimensioning your solution.

![Image](https://cdn-media-1.freecodecamp.org/images/9ct69RlHZVlEOBUUQXce2dQSUUyuQHlsycq2)
_The four Vs of Big Data_

* **Volume** — At what scale do you operate? In order of magnitude, are you closer to a few GigaBytes or hundreds of PetaBytes?
* **Variety** — How many data sources do you have? Are your data structured? If yes, does the schema vary often?
* **Velocity** — What is the frequency of the events you process? Is it credit cards payments? Is it a daily performance report sent by an IoT device?
* **Veracity** — Can you trust the data? Alternatively, do you need to apply multiple cleaning operations before manipulating it?

NiFi seamlessly ingests data from multiple data sources and provides mechanisms to handle different schema in the data. Thus, it shines when there is a high **variety** in the data.

Nifi is particularly valuable if data is of **low veracity**. Since it provides multiple processors to clean and format the data.

With its configuration options, Nifi can address a broad range of volume/velocity situations.

#### An increasing list of applications for data routing solutions

New regulations, the rise of the Internet of Things and the flow of data it generates emphasize the relevance of tools such as Apache NiFi.

* Microservices are trendy. In those loosely coupled services, the [data is the contract](https://auth0.com/blog/introduction-to-microservices-part-4-dependencies/) between the services. Nifi is a robust way to route data between those services.
* Internet of Things brings a multitude of data to the cloud. Ingesting and validating data from the edge to the cloud poses a lot of new challenges that NiFi can efficiently address (primarily through [MiniFi](https://nifi.apache.org/minifi/index.html), NiFi project for edge devices)
* New [guidelines](https://ec.europa.eu/futurium/en/ai-alliance-consultation/best-practices) and regulations are put in place to readjust the Big Data economy. In this context of increasing monitoring, it is vital for businesses to have a clear overview of their data pipeline. NiFi data lineage, for example, can be helpful in a path towards compliance to regulations.

#### Bridge the gap between big data experts and the others

As you can see by the user interface, a dataflow expressed in NiFi is excellent to communicate about your data pipeline. It can help members of your organization become more knowledgeable about what’s going on in the data pipeline.

* An analyst is asking for insights about why this data arrives here that way? Sit together and walk through the flow. In five minutes you give someone a strong understanding of the Extract Transform and Load _-ETL-_ pipeline.
* You want feedback from your peers on a new [error handling flow](https://community.hortonworks.com/questions/77336/nifi-best-practices-for-error-handling.html) you created? NiFi makes it a design decision to consider error paths as likely as valid outcomes. Expect the flow review to be shorter than a traditional code review.

#### Should you use it? Yes, No, Maybe?

NiFi brands itself as easy to use. Still, it is an enterprise dataflow platform. It offers a complete set of features from which you may only need a reduced subset. Adding a new tool to the stack is not benign.

If you are starting from scratch and manage a few data from trusted data sources, you may be better off setting up your Extract Transform and Load — _ETL_ pipeline. Maybe a [change data capture](https://martin.kleppmann.com/2015/06/02/change-capture-at-berlin-buzzwords.html) from a database and some data preparations scripts are all you need.

On the other hand, if you work in an environment with existing big data solutions in use (be it for [storage](https://fr.hortonworks.com/apache/hdfs/), [processing](https://spark.apache.org/) or [messaging](https://kafka.apache.org/) ), NiFi integrates well with them and is more likely to be a quick win. You can leverage the out of the box connectors to those other Big Data solutions.

It’s easy to be hyped by new solutions. List your requirements and **choose the solution that answers your needs as simply as possible**.

Now that we have seen the very high picture of Apache NiFi, we take a look at its key concepts and dissect its internals.

### Apache Nifi under the microscope

“NiFi is boxes and arrow programming” may be ok to communicate the big picture. However, if you have to operate with NiFi, you may want to understand a bit more about how it works.

In this second part, I explain the critical concepts of Apache NiFi with schemas. This black box model won’t be a black box to you afterward.

#### Unboxing Apache NiFi

When you start NiFi, you land on its web interface. The web UI is the blueprint on which you design and control your data pipeline.

![Image](https://cdn-media-1.freecodecamp.org/images/7RJGNI9l458xNVh4-2Y3rm0Jt0iKLUWgAMVJ)
_Apache NiFi user interface — build your pipeline by drag and dropping component on the interface_

In Nifi, you assemble _processors_ linked together by _connections_. In the sample dataflow introduced previously, there are three processors.

![Image](https://cdn-media-1.freecodecamp.org/images/2BFY2i1FOdRL91iGXkagqlQ3zNacNMFrDkZF)
_Three processors linked together by two queues_

The NiFi canvas user interface is the framework in which the pipeline builder evolves.

#### Making sense of Nifi terminology

To express your dataflow in Nifi, you must first master its language. No worries, a few terms are enough to grasp the concept behind it.

The black boxes are called _processors,_ and they exchange chunks of information named _FlowFiles_ through queues that are named _connections_. Finally, the _FlowFile Controller_ is responsible for managing the resources between those components.

![Image](https://cdn-media-1.freecodecamp.org/images/9F1Zm6QjmGg2HghZODu-E7c3-d9BcUxzLxuw)
_Processor, FlowFile, Connector, and the FlowFile Controller: four essential concepts in NiFi_

Let’s take a look at how this works under the hood.

#### FlowFile

In NiFi, the **FlowFile** is the information packet moving through the processors of the pipeline.

![Image](https://cdn-media-1.freecodecamp.org/images/IpdEyfHPnkqw-LLhHIcxHb7whRqxmsWg3unl)
_Anatomy of a FlowFile — It contains attributes of the data as well as a reference to the associated data_

A FlowFile comes in two parts:

* **Attributes**, which are key/value pairs. For example, the file name, file path, and a unique identifier are standard attributes.
* **Content**, a reference to the stream of bytes compose the FlowFile content.

The FlowFile does not contain the data itself. That would severely limit the throughput of the pipeline.

Instead, a FlowFile holds a pointer that references data stored at some place in the local storage. This place is called the [Content Repository](https://nifi.apache.org/docs/nifi-docs/html/nifi-in-depth.html#content-repository)_._

![Image](https://cdn-media-1.freecodecamp.org/images/YI-YbbYlradJJNETarUQDJgNeHrZOilsDt4E)
_The Content Repository stores the content of the FlowFile_

To access the content, the FlowFile [claims](https://nifi.apache.org/docs/nifi-docs/html/nifi-in-depth.html#deeper-view-content-claim) the resource from the Content Repository. The later keep tracks of the exact disk offset from where the content is and streams it back to the FlowFile.

**Not all processors need to access the content of the FlowFile** to perform their operations — for example, aggregating the content of two FlowFiles doesn’t require to load their content in memory.

When a processor modifies the content of a FlowFile, the previous data is kept. NiFi [copies-on-write](https://nifi.apache.org/docs/nifi-docs/html/nifi-in-depth.html#copy-on-write), it modifies the content while copying it to a new location. The original information is left intact in the Content Repository.

**Example**  
Consider a processor that compresses the content of a FlowFile. The original content remains in the Content Repository, and a new entry is created for the compressed content.

The Content Repository finally returns the reference to the compressed content. The FlowFile is updated to point to the compressed data.

The drawing below sums up the example with a processor that compresses the content of FlowFiles.

![Image](https://cdn-media-1.freecodecamp.org/images/3EOfYKGRFYXePKqfELvAfh5Ds2n02yqH4OPE)
_Copy-on-write in NiFi — The original content is still present in the repository after a FlowFile modification._

**Reliability**  
NiFi claims to be reliable, how is it in practice? The attributes of all the FlowFiles currently in use, as well as the reference to their content, are stored in the [FlowFile Repository.](https://nifi.apache.org/docs/nifi-docs/html/nifi-in-depth.html#flowfile-repository)

At every step of the pipeline, a modification to a Flowfile is first recorded in the FlowFile Repository, in a [write-ahead log](https://en.wikipedia.org/wiki/Write-ahead_logging), before it is performed.

For each FlowFile that currently exist in the system, the FlowFile repository stores:

* The FlowFile attributes
* A pointer to the content of the FlowFile located in the FlowFile repository
* The state of the FlowFile. For example: to which queue does the Flowfile belong at this instant.

![Image](https://cdn-media-1.freecodecamp.org/images/SUxFXGFyO5SGAez3bfU8danIRdGW-Mqm447x)
_The FlowFile Repository contains metadata about the files currently in the flow._

The FlowFile repository gives us the most current state of the flow; thus it’s a powerful tool to recover from an outage.

NiFi provides another tool to track the complete history of all the FlowFiles in the flow: the Provenance Repository.

**Provenance Repository**  
Every time a FlowFile is modified, NiFi takes a snapshot of the FlowFile and its context at this point. The name for this snapshot in NiFi is a _Provenance Event_. The [Provenance Repository](https://nifi.apache.org/docs/nifi-docs/html/nifi-in-depth.html#provenance-repository) records Provenance Events.

Provenance enables us to retrace the lineage of the data and build the full chain of custody for every piece of information processed in NiFi.

![Image](https://cdn-media-1.freecodecamp.org/images/2-hoPUXtfTmAm4GzXmHS9l7NBiO5rvVaOqnt)
_The Provenance Repository stores the metadata and context information of each FlowFile_

On top of offering the complete lineage of the data, the Provenance Repository also offers to replay the data from any point in time.

![Image](https://cdn-media-1.freecodecamp.org/images/rudXk2KywkeoBRQfmIIXTgzYfxdySlEGdLrB)
_Trace back the history of your data thanks to the Provenance Repository_

Wait, what’s the difference between the FlowFile Repository and the Provenance Repository?

The idea behind the FlowFile Repository and the Provenance Repository is quite similar, but they don’t address the same issue.

* The FlowFile repository is a log that contains only the latest state of the in-use FlowFiles in the system. It is the most recent picture of the flow and makes it possible to recover from an outage quickly.
* The Provenance Repository, on the other hand, is more exhaustive since it tracks the complete life cycle of every FlowFile that has been in the flow.

![Image](https://cdn-media-1.freecodecamp.org/images/gKcfJu7dHmXo7oRscnS1ZPXS1Hsu5LggJO4B)
_The Provenance Repository adds a time dimension where the FlowFile Repository is one snapshot_

If you have only the most recent picture of the system with the FlowFile repository, the Provenance Repository gives you a collection of photos — _a video_. You can rewind to any moment in the past, investigate the data, replay operations from a given time. It provides a complete lineage of the data.

#### FlowFile Processor

A **processor** is a black box that performs an operation. Processors have access to the attributes and the content of the FlowFile to perform all kind of actions. They enable you to perform many operations in data ingress, standard data transformation/validation tasks, and saving this data to various data sinks.

![Image](https://cdn-media-1.freecodecamp.org/images/8jBgnXwT8nBsYVkjUuIlec9CZRG0GXkRARff)
_Three different kinds of processors_

NiFi comes with many processors when you install it. If you don’t find the perfect one for your use case, it’s still possible to build your own processor. [Writing custom processors](https://community.hortonworks.com/articles/4318/build-custom-nifi-processor.html) is outside the scope of this blog post.

Processors are high-level abstractions that fulfill one task. This abstraction is very convenient because it shields the pipeline builder from the inherent difficulties of concurrent programming and the implementation of error handling mechanisms.

Processors expose an interface with multiple configuration settings to fine-tune their behavior.

![Image](https://cdn-media-1.freecodecamp.org/images/1DnkzZiW9KPhpovkcRIxrU6PI4yPIMhJCf53)
_Zoom on a NiFi Processor for [record validation](https://nifi.apache.org/docs/nifi-docs/components/org.apache.nifi/nifi-standard-nar/1.5.0/org.apache.nifi.processors.standard.ValidateRecord/index.html" rel="noopener" target="_blank" title=") — pipeline builder specifies the high-level configuration options and the black box hides the implementation details._

The properties of those processors are the last link between NiFi and the business reality of your application requirements.

The devil is in the details, and pipeline builders spend most of their time fine-tuning those properties to match the expected behavior.

**Scaling**  
For each processor, you can specify the number of concurrent tasks you want to run simultaneously. Like this, the _Flow Controller_ allocates more resources to this processor, increasing its throughput. Processors share threads. If one processor requests more threads, other processors have fewer threads available to execute. Details on how the Flow Controller allocates threads are available [here](https://community.hortonworks.com/articles/221808/understanding-nifi-max-thread-pools-and-processor.html).

**Horizontal scaling.** Another way to scale is to increase the number of nodes in your NiFi cluster. [Clustering](https://nifi.apache.org/docs/nifi-docs/html/administration-guide.html#clustering) servers make it possible to increase your processing capability using commodity hardware.

#### Process Group

This one is straightforward now that we’ve seen what processors are.

A bunch of processors put together with their connections can form a process group. You add an input port and an output port so it can receive and send data.

![Image](https://cdn-media-1.freecodecamp.org/images/o97mtJQX9Lv2qGbgy8NBP8C2r2jNfQnQRg3I)
_Building a new processor from three existing processors_

Processor groups are an easy way to create new processors based from existing ones.

#### Connections

Connections are the queues between processors. These queues allow processors to interact at differing rates. Connections can have different capacities like there exist different size of water pipes.

![Image](https://cdn-media-1.freecodecamp.org/images/8iRHt6Xy7l2S8OWCfZyPEYAKmNXqOhCGqQ5h)
_Various capacities for different connectors. Here we have capacity C1 &gt; capacity C2_

Because processors consume and produce data at different rates depending on the operations they perform, connections act as buffers of FlowFiles.

There is a limit on how many data can be in the connection. Similarly, when your water pipe is full, you can’t add water anymore, or it overflows.

In NiFi you can set limits on the number of FlowFiles and the size of their aggregated content going through the connections.

**What happens when you send more data than the connection can handle?**

If the number of FlowFiles or the quantity of data goes above the defined threshold, _backpressure_ is applied. The Flow Controller won’t schedule the previous processor to run again until there is room in the queue.

Let’s say you have a limit of 10 000 FlowFiles between two processors. At some point, the connection has 7 000 elements in it. It is ok since the limit is 10 000. _P1_ can still send data through the connection to _P2_.

![Image](https://cdn-media-1.freecodecamp.org/images/ZpaLFmUmNG2L16aBV7Kjk9ADhs8CCBc39Fzr)
_Two processors linked by a connector with its limit respected._

Now let’s say that processor one sends 4 000 new FlowFiles to the connection.   
7 0000 + 4 000 = 11 000 → We go above the connection threshold of 10 000 FlowFiles.

![Image](https://cdn-media-1.freecodecamp.org/images/wucrVEx2N8vgxf8e9Ss9gzR3C1PcOvo9uVDN)
_Processor P1 not scheduled until the connector goes back below its threshold._

The limits are _soft limits,_ meaning they can be exceeded. However, once they are, the previous processor, _P1_ won’t be scheduled until the connector goes back below its threshold value — 10 000 FlowFiles.

![Image](https://cdn-media-1.freecodecamp.org/images/KKOd45PcA8yEav1p593VDtzf2MCX5Fc8g2pG)
_Number of FlowFiles in the connector comes back below the threshold. The Flow Controller schedules the processor P1 for execution again._

This simplified example gives the big picture of how [backpressure](https://en.wikipedia.org/wiki/Back_pressure) works.

You want to setup connection thresholds appropriate to the Volume and Velocity of data to handle. _Keep in mind the Four Vs_.

The idea of exceeding a limit may sound odd. When the number of FlowFiles or the associated data go beyond the threshold, a [swap mechanism](https://community.hortonworks.com/articles/184990/dissecting-the-nifi-connection-heap-usage-and-perf.html) is triggered.

![Image](https://cdn-media-1.freecodecamp.org/images/0Qf2xfUhSaq43Ma5pWYkgVnqBAWkSvu1gVlV)
_Active queue and Swap in Nifi connectors_

For another example on backpressure, [this mail thread](http://mail-archives.apache.org/mod_mbox/nifi-users/201604.mbox/%3CBLU436-SMTP24995D5F6EDF5985AADFE23CE680@phx.gbl%3E) can help.

**Prioritizing FlowFiles**  
The connectors in NiFi are highly configurable. You can choose [how you prioritize](https://nifi.apache.org/docs/nifi-docs/html/user-guide.html#prioritization) FlowFiles in the queue to decide which one to process next.

Among the available possibility, there is, for example, the First In First Out order — _FIFO. However,_ you can even use an attribute of your choice from the FlowFile to prioritize incoming packets.

#### Flow Controller

The Flow Controller is the glue that brings everything together. It allocates and manages threads for processors. It’s what executes the dataflow.

![Image](https://cdn-media-1.freecodecamp.org/images/XrTQX8uhG36C9plkkVd-BtbBe3hn5JEpNi8N)
_The Flow Controller coordinates the allocation of resources for processors._

Also, the Flow Controller makes it possible to add Controller Services.

Those services facilitate the management of shared resources like database connections or cloud services provider credentials. Controller services are [daemons](http://www.linfo.org/daemon.html). They run in the background and provide configuration, resources, and parameters for the processors to execute.

For example, you may use an [AWS credentials provider service](https://nifi.apache.org/docs/nifi-docs/components/nifi-docs/components/org.apache.nifi/nifi-aws-nar/1.9.0/org.apache.nifi.processors.aws.credentials.provider.service.AWSCredentialsProviderControllerService/index.html) to make it possible for your services to interact with S3 buckets without having to worry about the credentials at the processor level.

![Image](https://cdn-media-1.freecodecamp.org/images/myXlwFSHLAuCL2di582ctwMQ9ulz-SpS7Lcu)
_An AWS credentials service provide context to two processors_

Just like with processors, a [multitude of controller services](https://nifi.apache.org/docs/nifi-docs/components/nifi-docs/) is available out of the box.

You can check out [this article](https://community.hortonworks.com/articles/90259/understanding-controller-service-availability-in-a.html) for more content on the controller services.

### Conclusion and call to action

In the course of this article, we discussed NiFi, an enterprise dataflow solution. You now have a strong understanding of what NiFi does and how you can leverage its data routing features for your applications.

If you’re reading this, congrats! You now know more about NiFi than 99.99% of the world’s population.

Practice makes perfect. You master all the concepts required to start building your own pipeline. **Make it simple; make it work first.**

Here is a list of exciting resources I compiled on top of my work experience to write this article.

#### Resources ?

#### The bigger picture

Because designing data pipeline in a complex ecosystem requires proficiency in multiple areas, I highly recommend the book [_Designing Data-Intensive Applications_](https://dataintensive.net/) from Martin Kleppmann. It covers the fundamentals.

* A cheat sheet with all the references quoted in Martin’s book is available on his [Github repo](https://github.com/ept/ddia-references).

This cheat sheet is a great place to start if you already know what kind of topic you’d like to study in-depth and you want to find quality materials.

#### Alternatives to Apache Nifi

Other dataflow solutions exist.

Open source:

* [Streamsets](https://streamsets.com/) is similar to NiFi; a good comparison is available on [this blog](https://statsbot.co/blog/open-source-etl/)

Most of the existing cloud providers offer dataflow solutions. Those solutions integrate easily with other products you use from this cloud provider. At the same time, it solidly ties you to a particular vendor.

* [Azure Data Factory](https://azure.microsoft.com/en-us/services/data-factory/), A Microsoft solution
* IBM has its [InfoSphere DataStage](https://www.ibm.com/us-en/marketplace/datastage)
* Amazon proposes a tool named [Data Pipeline](https://docs.aws.amazon.com/en_us/datapipeline/latest/DeveloperGuide/what-is-datapipeline.html)
* Google offers its [Dataflow](https://cloud.google.com/dataflow/)
* Alibaba cloud introduces a service [DataWorks](https://www.alibabacloud.com/help/doc-detail/30256.htm?spm=a2c63.p38356.b99.2.d115c242ZFQbSN) with similar features

#### NiFi related resources

* The official [Nifi documentation](https://nifi.apache.org/docs.html) and especially the [Nifi In-depth](https://nifi.apache.org/docs/nifi-docs/html/nifi-in-depth.html) section are gold mines.
* Registering to Nifi users mailing list is also a great way to be informed — for example, [this conversation](http://mail-archives.apache.org/mod_mbox/nifi-users/201604.mbox/%3CBLU436-SMTP24995D5F6EDF5985AADFE23CE680@phx.gbl%3E) explains back-pressure.
* Hortonworks, a big data solutions provider, has a community website full of engaging resources and _how-to_ for Apache Nifi.  
 — [This article](https://community.hortonworks.com/articles/184990/dissecting-the-nifi-connection-heap-usage-and-perf.html) goes in depth about connectors, heap usage, and back pressure.  
 — [This one](https://community.hortonworks.com/articles/135337/nifi-sizing-guide-deployment-best-practices.html) shares dimensioning best practices when deploying a NiFi cluster.
* The [NiFi blog](https://blogs.apache.org/nifi/) distills a lot of insights NiFi usage patterns as well as tips on how to build pipelines.
* [Claim Check pattern](https://www.enterpriseintegrationpatterns.com/patterns/messaging/StoreInLibrary.html) explained
* The theory behind Apache Nifi is not new, Seda referenced in Nifi Doc is extremely relevant  
 — Matt Welsh. Berkeley. SEDA: An Architecture for Well-Conditioned, Scalable Internet Services [online]. Retrieved: 21 Apr 2019, from [http://www.mdw.la/papers/seda-sosp01.pdf](http://www.mdw.la/papers/seda-sosp01.pdf)

