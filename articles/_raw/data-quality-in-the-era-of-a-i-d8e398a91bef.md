---
title: Data Quality in the era of A.I.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-21T17:05:40.000Z'
originalURL: https://freecodecamp.org/news/data-quality-in-the-era-of-a-i-d8e398a91bef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mpT-JZf1lnZhAixk_fP7bQ.jpeg
tags:
- name: analytics
  slug: analytics
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: big data
  slug: big-data
- name: Data Science
  slug: data-science
- name: software development
  slug: software-development
seo_title: null
seo_desc: 'By George Krasadakis

  Data quality is of critical importance especially in the era of Artificial Intelligence
  and automated decisions. Do you have a strategy?


  _Database clipart from [dumielauxepices](https://dumielauxepices.net/wallpaper-70986"
  rel="...'
---

By George Krasadakis

#### Data quality is of critical importance especially in the era of Artificial Intelligence and automated decisions. Do you have a strategy?

![Image](https://cdn-media-1.freecodecamp.org/images/ssFde9l5rMynXaW4k2Mz9Gb0PpGh4Qcb2te0)
_Database clipart from [dumielauxepices](https://dumielauxepices.net/wallpaper-70986" rel="noopener" target="_blank" title=")._

### Data-intensive projects have a single point of failure: data quality

As the director of [datamine decision support systems](http://www.datamine.gr), I’ve delivered more than 80 data-intensive projects across several industries and high-profile corporations. These include **data warehousing**, **data integration**, **business intelligence**, **content performance**, and **predictive models**. In most cases, data quality proved to be a critical factor for the success of the project.

The obvious challenge in every single case was to effectively **query** heterogeneous data sources, then **extract** and **transform** data towards one or more **data models**.

The non-obvious challenge was the **early identification** of data issues, which — in most cases — were unknown to the data owners as well.

We strategically started every project with a data-quality assessment phase — which in many cases lead to project scope modifications and even additional data cleansing initiatives and projects.

### Data quality defined

There are many aspects to data quality, including **consistency, integrity, accuracy**, and **completeness**. According to [Wikipedia](https://en.wikipedia.org/wiki/Data_quality), data is generally considered high quality if it is “fit for [its] intended uses in operations, decision making and planning and data is deemed of high quality if it correctly represents the real-world construct to which it refers.”

I define data quality as the level of compliance of a data set with a contextual normality.

This **normality** is set by user-defined rules and/or statistically derived ones. it is contextual_,_ in the sense that rules **reflect the logic** of particular business processes, corporate knowledge, environmental, social or other conditions. For example, a property of the same entity could have different validation rules in different companies, markets, languages, or currencies.

Modern systems need to become aware of the quality in data I/O. They must instantly identify potential issues and **avoid exposing** dirty, inaccurate or incomplete data to connected production components/ clients.

This implies that, even if there is a sudden problematic situation resulting in poor-data quality entries, the system will be able to handle the quality issue and **proactively notify** the right users. Depending on how critical the issues are, it might also **deny serving data** to its clients — or serve data while raising the alert/ flagging the potential issues.

![Image](https://cdn-media-1.freecodecamp.org/images/mubexRhZMCnyoo7UTwMcJmC75FlGdAQr3uC-)
_Cyber infinity icon from [iconspng](https://www.iconspng.com/image/93060/cyber-infinity" rel="noopener" target="_blank" title=")._

### The importance of data quality

Data quality is of **critical importance** especially in the era of automated decisions, AI, and continuous process optimization. [Corporations need to be data-driven](https://medium.freecodecamp.org/the-data-driven-corporation-259b5b84f9c9) and data quality is a critical pre-condition to achieve this.

#### **Confusion, limited trust, poor decisions**

In most of the cases, data quality issues explain limited trust in data from corporate users, waste of resources or even **poor decisions**.

Consider a team of analysts trying to figure out if an outlier is a critical business discovery or an unknown/ poorly handled data issue. Even worse, consider real-time decisions being made by a system not able to identify and handle poor data which accidentally — or even intentionally — had been fed into the process.

#### **Failures due to low data quality**

I’ve seen great Business Intelligence, data warehousing, and similar initiatives failing due to **low engagement** by key users and stakeholders. In most of the cases, limited engagement was the direct result of **lack of trust** in the data. Users need to trust the data — if they don’t, they will gradually abandon the system impacting its major KPIs and success criteria.

Whenever you think you’ve done some major data discovery, cross-check for quality issues first!

#### Types and symptoms

Data quality issues can take many forms, for example:

* particular properties in a specific object have invalid or missing values
* a value coming in an unexpected or corrupted format
* duplicate instances
* inconsistent references or unit of measures
* incomplete cases
* broken URLs
* corrupted binary data
* missing packages of data
* gaps in the feeds
* mis-mapped properties

#### The root cause

Data quality issues are typically the result of:

* poor software implementations: bugs or improper handling of particular cases
* system-level issues: failures in certain processes
* changes in data formats, impacting the source and/or target data stores

Modern systems should be designed assuming that at some point there will be problematic data feeds and unexpected quality issues.

The validity of the data properties can be evaluated against [a] known, predefined rules and [b] dynamically derived rules and patterns based on statistical processing

### A strategy for data quality

A modern data-intensive project typically involves data streams, complex ETL processes, post-processing logic, and a range of analytical or cognitive components.

The key deliverable in such scenarios is a high-performance data processing pipeline, feeding and maintaining at least one data store. This defines a “data environment,” which then empowers advanced analytical models, real-time decision making, knowledge extraction and possibly AI applications. The following describes a strategy for ensuring data quality throughout this process.

#### Identify, understand, and document the data sources

You need to identify your data sources and, for each one, briefly document the following:

1. **Type of data contained** — for example customer records, web traffic, user documents, activity from a connected device (in an IoT context).

2. **Type of storage** — for instance is it a flat file, a relational database, a document store or a stream of events?

3. **Time frames** — how long do we have data for?

4. **Frequency and types** of updates — are you getting deltas, events, updates, aggregated data? All these can significantly impact the design of the pipeline and the ability to identify and handle data quality issues.

5. **The source of data and involved systems** — is data coming from another system? Is it a continuous feed of events or a batch process pulled from another integrated system? Is there manual data entry/ validation involved?

6. **Known data issues** and limitations can help speed up the initial data examination phase **if** provided upfront.

7. **The data models involved** in the particular data source — for example, an ER model representing customers, a flat file structure, an object, a star schema.

8. **Stakeholders involved** — this is very important in order to interpret issues and edge cases and also to validate the overall state of the data, with those having the deepest understanding of the data, the business and the related processes.

![Image](https://cdn-media-1.freecodecamp.org/images/KXylHmRJfqxCGwaTaGjjNjpr-rjjDCaui7eu)
_Clones computer cube data from [pixabay](https://pixabay.com/en/clones-computer-cube-data-2029896/" rel="noopener" target="_blank" title=")._

#### Start with data profiling

[**Data profiling**](https://en.wikipedia.org/wiki/Data_profiling) is the process of describing the data by performing basic descriptive statistical analysis and summarization. The **key** is to briefly document the findings thus creating a baseline — a reference point to be used for data validation throughout the process.

Data profiling depends on the type of the underlying data and the business context, but in a general scenario you should consider the following:

1. Identify the key **entities**, such as customer, user, product, the **events** involved , such as register, login, purchase, the **time frame**, the **geography**, and other key dimensions of your data.

2. Select the **typical time frame** to use for your analysis. This could be a day, week, month, and so forth depending on the business.

3. Analyse high-level **trends** involving the entities and events identified. Generate time series against the major events and the key entities. Identify trends, seasonality, peaks, and try to interpret them in the context of the particular business. Consult the owner of the data and capture/ document these “data stories.”

4. **Analyze** the data. For each of the properties of your key entities perform statistical summarization to capture the **shape** of the data. For numerical values you could start with the basics — min, average, max, standard deviation, quartiles — and then possibly visualize the distribution of the data. Having done so, examine the shape of the distribution and figure out if it makes sense to the business. For categorical values you could summarize the distinct number of values by frequency and, for example, document the top x values explaining z% of the cases.

5. Review a few **outliers.** Having the distribution of the values for a particular property — let’s say, the age of the customer — try to figure out “suspicious” values in the context of the particular business. Select a few of them and retrieve the actual instances of the entities. Then review their profile and activity — of the particular users, in this example — and try to interpret the suspicious values. Consult the owner of the data to advice on these findings.

6. **Document** your results. Create a compact document or report with clear structure to act as your baseline and data reference. You should append the findings of each of the data sources to this single document — with the same structure, time references, and metadata to ensure easier interpretation.

7. **Review, interpret, validate**. This is the phase where you need input from the data owner to provide an overall interpretation of the data, and to explain edge cases, outliers, or other unexpected data patterns. The outcome of the process could be to confirm the state of the data, explain known issues, and register new ones. This is where possible solutions to known data issues can be discussed and/or decided. Also, validation rules can be documented.

In an **ideal scenario** the data profiling process should be automated. There are several tools allowing quick data profiling by just connecting your data source and going through a quick wizard-like configuration. The output of the process in such scenarios is typically an interactive report enabling easy analysis of the data and sharing of the knowledge with the team.

![Image](https://cdn-media-1.freecodecamp.org/images/ty763uwNNP42a6p5TMPsTsz7CzfIBHjY6UkP)
_Data analyze from [kissclipart](https://www.kissclipart.com/data-analyze-clipart-data-analysis-31xywg/" rel="noopener" target="_blank" title=")._

#### Establish a data quality reference store

The purposes of the data quality reference (DQR) store are to capture and maintain **metadata** and **validity** rules about your data, and to make them available to external processes.

This could be a highly sophisticated system to automatically derive rules about the validity of your data and continuously assess the incoming (batches of) cases, with the capability to identify time-related and other patterns about your data. This could be a manually maintained set of rules which allow quick validation of the incoming data. This could be a hybrid setup.

In any case, the ETL process should be able to query the DQR store and load the data validation rules and patterns, along with fixing directives. Data validation rules should be **dynamic** instead of a fixed set of rules or hard-coded pieces of logic.

The DQR store should also be accessible via interactive reporting and standardized dashboards — to empower process owners and data analysts to understand the data, the process, trends, and issues.

**Check also**: [Choosing between R and Python](https://medium.com/innovation-machine/choosing-between-r-and-python-a-digital-analysts-guide-b7103f80aa4e)

#### Implement smart data validation

Enable your data processing **pipeline** to load data validation rules from the DQR store described above. The DQR store could be designed as an internal ETL subsystem or an external to the ETL service. In any case, the logic to validate data along with the suggested action should be dynamic to your ETL process.

The data processing pipeline should be continuously validating incoming (batches of) cases based on the latest version of the validation rules.

The system should be able to flag and possibly enrich the original incoming data with the outcome of the validation and related metadata, and feed back to the DQR store. The original data is stored, with proper flagging by the ETL, **unless** otherwise directed by the current validation policy.

With this approach, data quality can be measured and analysed against time, for example by data source, processing pipeline. Interactive reporting can help to easily explore the overall state of the ETL process and quickly identify and explore data quality concerns or specific issues.

The system could also support an overall “Index of Data Quality”. This can consider multiple aspects of quality, and assign more importance to specific entities and events. For example, an erroneous transaction record could be far more important than a broken hyperlink to an image.

The Index of Data Quality could also have specific **elasticity** — different by entity and event. For example, this could allow delays in receiving data for a particular entity while not for another.

Having an overall Index of Data Quality can help the corporation measure data quality over time and across key dimensions of the business. It can also help to set goals and quantify the impact of potential improvements of the ETL strategy.

> **Check also:** [How Artificial Intelligence is changing the world](https://medium.com/innovation-machine/artificial-intelligence-fe713f283cfb)

#### A smart notification layer

The overall process should be aware of any quality issues, trends, and sudden changes. Moreover, the system needs to know the importance — how critical an issue is. Based on this awareness and a smart configuration layer, the system knows when to notify who and through which particular channel.

Modern systems must be aware of the quality of the incoming data and capable of identifying, reporting and handling erroneous cases accordingly.

> **Read more on AI**

> [Artificial Intelligence: Risks & Concerns](https://medium.com/@gkrasadakis/artificial-intelligence-risks-concerns-2a19ba21cfd9)

> [Artificial Intelligence: the impact on employment and the workforce](https://hackernoon.com/artificial-intelligence-3c6d80072416)

> [Artificial Intelligence: A non-technical introduction — definition, applications and impact](https://hackernoon.com/artificial-intelligence-fe713f283cfb)

> [What’s next on AI, AR, VR, NUI, Robotics, Data & Visualization, Blockchain](https://medium.com/innovation-machine/2018-innovation-trends-and-opportunities-8a5d642fd661)

