---
title: How serverless stream processing will make decision-making easier
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-09T19:08:22.000Z'
originalURL: https://freecodecamp.org/news/how-serverless-stream-processing-will-make-decision-making-easier-d929502b43c8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0FKhwNV-o-OEiuFqSz_tSQ.jpeg
tags:
- name: analytics
  slug: analytics
- name: big data
  slug: big-data
- name: Productivity
  slug: productivity
- name: serverless
  slug: serverless
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Chamath Kirinde

  About a year ago, we started being a part of the digital transformation with the
  first ever cloud-based IDE for serverless development. It was no cakewalk — we’ve
  been burning the candle at both ends trying to cover the majority fr...'
---

By Chamath Kirinde

About a [year ago](https://globenewswire.com/news-release/2018/02/06/1333797/0/en/SLAppForge-Announces-Sigma-a-Cloud-IDE-for-Serverless-Computing.html), we started being a part of the digital transformation with the first ever cloud-based [IDE](https://sigma.slappforge.com/?utm_source=freecodecamp&utm_medium=blog&utm_campaign=guide&utm_content=Chamath) for serverless development. It was no cakewalk — we’ve been burning the candle at both ends trying to cover the majority from AWS’s [serverless stack](https://aws.amazon.com/serverless/#The_AWS_Serverless_Platform). Working with AWS Kinesis made me realise the [beauty of serverless](https://chummycharms.blogspot.com/2018/03/why-serverless-why-now.html) — of course, the exposure to streaming data with [Kafka](https://chummycharms.blogspot.com/2017/10/real-time-activity-tracking-with-kafka.html) spared me some time going through the rudiments.

![Image](https://cdn-media-1.freecodecamp.org/images/IBLdvoo4R41bu17WA8x0Wy7gia9EtFjG4BzO)
_Rational decision making: Photo by [Unsplash](https://unsplash.com/photos/o4c2zoVhjSw?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Raj Eiamworakul</a> on <a href="https://unsplash.com/search/photos/rational-decisions?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### TL;DR

Did you ever wonder…

* How **“Google Search”** suggests things to you when you’re half-typing your query?
* How **“Cheapest Airlines”** start to appear everywhere after you searched for a country?
* How online role-playing games adjust according to your decisions?
* How gambling sites predict the odds of a live game?
* Why were [Curry and Thompson benched](https://www.cbssports.com/nba/news/warriors-wearable-weapon-devices-to-monitor-players-while-on-the-court/) while Portland was handing the Warriors their worst loss in a 73-win NBA season?

![Image](https://cdn-media-1.freecodecamp.org/images/4vE1DrCz1W1TQwQIWA3IwAsGTeVgcT9Nh-7k)
_Google’s (sometimes so annoying) query autocomplete_

The power of real-time streaming data analytics is astonishing indeed. Now, since serverless technology is gaining some momentum, maybe you won’t have to worry about taking risky decisions on your own at all. This post covers the basics of “Serverless Streaming Data Processing” and how it will be an influential component of our decision making in the future.

### Data, Data Everywhere

Life is an endless series of events. The technology around us has made it a stream of digital actions emitting streams of data. If you turn back and investigate your life very carefully, you’ll see the never-ending string of data you have generated with your every digital action. It could be a lot to digest at first, but let’s explore some scenarios and try to find what applies to you and me.

* Online banking and convenient e-commerce purchasing capabilities
* Ride-sharing, modern-day traveling and transportation
* Industrial equipment and agricultural use cases like monitored machinery, autonomous tractors, and precision farming
* Automated power generation and smart grids, Zero-net Buildings, Smart metering
* Real-estate property recommendations based on geo-location, predictive maintenance
* Online dating and matchmaking relying on complex personality patterns and attribute distribution

![Image](https://cdn-media-1.freecodecamp.org/images/UoE9uNA5mdznpmW5aFLsmjQZkO4K5JibcOSh)
_Rational Romance: Will you be my Valentine?_

* Financial trading according to the real-time changes in the stock market, analytical risk management
* Movies, songs and other digital media with a better experience depending on the demographics, preference, and emotions
* Improved web and mobile application experience based on usage
* Dynamic and personalised experiences in online gaming
* Enhanced social media experiences with hyper-personalisation and predictive analytics
* Telemetry from connected devices, or remote data centres from geospatial or spatial services like weather, resource assessment
* Sports analytics to enhance the players’ performance reducing health risks

![Image](https://cdn-media-1.freecodecamp.org/images/VuM87-7-xwLq12dD8IBIKTsxcwY18TqGwyfH)
_Welcome Analytics_

All these events produce data — lots of it. Due to the frequency of this data emission, it has become an increasing burden to the digital space.

### What is Streaming Data?

In a [survey](https://www.domo.com/learn/data-never-sleeps-6) conducted last year about data, it’s estimated that with the current pace of data generation,

> 1.7 MB of data will be created every second for every person on earth by 2020

Data that is poured out continuously by a gazillion sources every second has become a fact we can’t just ignore. Big Data discipline was an eye-opener for the tech world to apply this once irritating data to do something useful. This same irksome data is collected and analysed by a new species, namely data scientists ?. Due to the nature of continuity and often being in small sizes (order of Kilobytes) these data flows — usually referred by the moniker streaming data — are collected simultaneously as records and sent in for further processing.

### From stream processing to smart decisions

A streaming data processing structure is usually comprised of two layers — a storage layer and a processing layer. The former is responsible for ordering large streams of records and facilitating persistence and accessibility at high speeds. The processing layer takes care of data consumption, executing computations, and notifying the storage layer to get rid of already processed records. Data processing is done for each record incrementally or by matching over sliding time windows. Processed data is then subjected to streaming analytics operations and the derived information is used to make context-based decisions.

For instance, companies can track public sentiment changes on their products by analysing social media streams continuously. The world’s most influential nations can [intervene in decisive events](https://www.bbc.com/news/technology-46590890) like presidential elections in other powerful countries. And mobile apps can offer personalised recommendations for products based on geo-location of devices and user emotions.

![Image](https://cdn-media-1.freecodecamp.org/images/QxndNC2SRx15iRq02C8qQBWHEAqe5v01WemR)
_Poor data analytics — Poor decisions_

Most applications collect a portion of their data at the outset to produce simple summary reports and take simple decisions such as triggering alarms or calculating a moving average value. As time flies by, these become more and more sophisticated, and companies might want to access profound insights to perform intricate activities in turn with the aid of Machine Learning algorithms and data analysis techniques.

The continual growth of data has made data scientists work around the clock to come up with trailblazing solutions to utilise as much data as possible to fabricate alternate futures with better decisions.

### Service Facilitators

Adoption of the ideal cloud provider to fit organisational requirements can be overwhelming. However, all the major cloud service providers are equipped with competitive options to accommodate stream processing due to its ubiquitous impact. Here’s a list of commonly used serverless services to bolster enterprise-grade applications, highly relying on streaming data.

![Image](https://cdn-media-1.freecodecamp.org/images/5cstIiKD2o7dl82UVruDBBvv8NmqHTqI0rRE)
_Infographic: Serverless Stream Processing Components_

### Live Examples

Many companies use insights from stream analytics to enhance the visibility of their businesses. This allows them to deliver customers a personalised experience. Additionally, near real-time transparency gives these firms the flexibility to promptly address emergencies.

The emerging serverless architecture has driven all the leading cloud service platforms to present complementary solutions. Stream processing was made available for serverless application development with fully-managed, cloud-based services for real-time data processing over large Distributed Data Streams.

#### 1. Hyper-personalised Television

![Image](https://cdn-media-1.freecodecamp.org/images/3tdMjLGeH4Oaf2zq84AKbmJvm1H-ejVMEK0H)
_Netflix: Photo by [Unsplash](https://unsplash.com/@jenskreuter?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Jens Kreuter</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Netflix, the leading online television network in the world, developed a solution which centralises their flow logs [using Amazon Kinesis Streams](https://aws.amazon.com/solutions/case-studies/netflix-kinesis-streams/). As a system processing billions of traffic flows every day, this eliminates plenty of complexity for them because of the absence of a database in the architecture. Due to the high scalability and lightning speed, they can discover and address issues as they arise, and monitor the application on a massive scale.

With the upgraded recommendation algorithm, video transcoding, and licensing popular media, this subsequently grants a seamless experience to subscribers. With the exponential growth of subscribers, the company’s responsibilities increase by the day. However, nothing seems to be a problem for Netflix since they are considered to have a [sound decision-making model](https://www.forbes.com/sites/danpontefract/2019/02/04/the-netflix-decision-making-model-is-why-theyre-so-successful/#11a4e67273bc).

#### 2. Improving the decisions of the decision makers

As a leading source of integrated and intelligent information for businesses and professionals, Thomson Reuters provide their services to decision makers in a wide range of domains like financing and risk, science, legal, technology. This company built an in-house analytics engine to take full control of data and moved to AWS because they were familiar with its capabilities and scale.

The new real-time [pipeline attached to Amazon Kinesis](https://aws.amazon.com/solutions/case-studies/thomson-reuters/) stream produces better results in perceptive customer experience with accurate economic forecasts, financial trends for beneficiaries including a range of government activities.

#### 3. Unicorn: a solution to traffic congestion

![Image](https://cdn-media-1.freecodecamp.org/images/Pz294qBcYfaEhKVPStwmt7eBxJ2YYAqVJsnL)
_Unicorn: Photo by [Unsplash](https://unsplash.com/@boudewijn_huysmans?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Boudewijn Huysmans</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Jakarta has become a heavily congested city where the motorcycle has been deemed the most efficient mode of transport. To exploit this business opportunity, GO-JEK — one of the few unicorn businesses in Southeast Asia — started as a call centre for motorcycle taxi bookings. However, to meet the demand in exceeding expectations, the company had to consider expansion. Now with the support of Google Cloud Professional Services, the business architecture built on Cloud Dataflow for stream inference enables them to predict changes in demand effectively.

There are more stories about how cloud platforms like [AWS](https://aws.amazon.com/lambda/resources/customer-case-studies/), [Google](https://cloud.google.com/customers/#/products=Big_Data_Analytics,Marketing_Analytics), [Microsoft Azure](https://azure.microsoft.com/en-us/case-studies/?service=stream-analytics%7Cevent-hubs&solution=serverless), and [IBM Cloud](https://console.bluemix.net/docs/openwhisk/openwhisk_use_cases.html#openwhisk_event_processing) are exploited by companies to make their clients’ lives better and secure.

### Limitations of Serverless Stream Processing

Serverless stream processing is increasingly becoming a vital part of decision-making engines. However, with the current set of features, it’s not the ideal solution for some scenarios. Implementing real-time analytics for sliding windows and temporal event patterns is not a course for the faint-hearted.

The best way to assimilate never-ending data of this magnitude is through real-time dashboards which requires additional data organisation and persisting. These manoeuvres introduce undesirable latency and data management issues into the context. However, technology is evolving and trying to catch up to the speeds with integration using advanced cloud data management techniques to produce materialised views.

![Image](https://cdn-media-1.freecodecamp.org/images/nT-vi3LfbSp5CwbMKlR-teyFq5br9oem6MYu)
_Security: A major concern_

Stream Processing often uses a time-based or record-based window to be processed in contrast to the batch-based processing, which can lead to challenges in use cases that require query re-execution.

Nowadays, application requirements grow beyond aggregated analytics. Increasing the window size seems to be an appropriate temporary solution, but it develops another intractable problem — Memory Management. Modern-day solutions usually provide advanced memory management and scheduling techniques to overcome this, but the world will see further improvements.

### Conclusion

All in all, it’s apparent that serverless stream processing has been playing a prominent role around us without us even knowing. With the power of serverless data stream processing, applications can evolve from traditional batch processing to real-time analytics. The revelation of profound insights will result in effective decision making without having to manage infrastructure.

Even today, many organizations practise orthodox decision-making strategies based on the analytics derived using the big data clusters that belonged to **THE PAST**. New horizons of serverless and real-time data processing are now equipped with the power to make effective decisions and create a more productive, relevant, and most importantly secure world around you.

Will serverless stream processing make emotional decision making obsolete and computerized rational judgement the norm?

What do you think?

### What should you do now?

* **Clap.** Appreciate and let others find this article.
* **Comment.** Share your thoughts.
* **Follow me.** [Chamath Kirinde](https://medium.com/@jchamath) to receive updates on articles like this.
* **Keep in touch.** [LinkedIn](https://www.linkedin.com/in/jchamath/), [Twitter](https://twitter.com/JChamath), [Chummy Charms](https://chummycharms.blogspot.com)
* **Think Serverless.** [SLAppForge](https://slappforge.com/blog)

_Originally published at [chummycharms.blogspot.com](https://chummycharms.blogspot.com/2019/03/serverless-stream-processing.html)._

