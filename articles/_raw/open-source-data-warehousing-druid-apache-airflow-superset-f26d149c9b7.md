---
title: Use these open-source tools for Data Warehousing
subtitle: ''
author: Simon Späti
co_authors: []
series: null
date: '2018-11-29T06:00:53.000Z'
originalURL: https://freecodecamp.org/news/open-source-data-warehousing-druid-apache-airflow-superset-f26d149c9b7
coverImage: https://cdn-media-1.freecodecamp.org/images/0*vp7sdOKpaw8JiXnP.png
tags:
- name: big data
  slug: big-data
- name: data-engineering
  slug: data-engineering
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'These days, everyone talks about open-source software. However, this is
  still not common in the Data Warehousing (DWH) field. Why is this?

  For this post, I chose some open-source technologies and used them together to build
  a full data architecture f...'
---

These days, everyone talks about open-source software. However, this is still not common in the Data Warehousing (DWH) field. Why is this?

For this post, I chose some open-source technologies and used them together to build a full data architecture for a Data Warehouse system.

I went with [Apache Druid](http://www.druid.io/) for data storage, [Apache Superset](https://superset.incubator.apache.org/) for querying, and [Apache Airflow](https://airflow.apache.org/) as a task orchestrator.

### Druid — the data store

Druid is an open-source, column-oriented, distributed data store written in Java. It’s designed to quickly ingest massive quantities of event data, and provide low-latency queries on top of the data.

![Image](https://cdn-media-1.freecodecamp.org/images/X5ERR00kMGXwmbNaZ3a-6OuTgGhV6JosZGqX align="left")

#### Why use Druid?

Druid has many key features, including sub-second OLAP queries, real-time streaming ingestion, scalability, and cost effectiveness.

With the [comparison of modern OLAP Technologies](http://www.sspaeti.com/blog/olap-whats-coming-next#Comparison_modern_OLAP_Technologies) in mind, I chose Druid over ClickHouse, Pinot and Apache Kylin. Recently, [Microsoft announced they will add Druid](https://azure.microsoft.com/en-us/blog/azure-hdinsight-brings-next-generation-hadoop-3-0-and-enterprise-security-to-the-cloud/) to their Azure HDInsight 4.0.

#### Why not Druid?

Carter Shanklin wrote [a detailed post about Druid’s limitations](https://de.hortonworks.com/blog/apache-hive-druid-part-1-3/) at Horthonwork.com. The main issue is with its support for SQL joins, and advanced SQL capabilities.

### The Architecture of Druid

Druid is scalable due to its cluster architecture. You have three different node types — the Middle-Manager-Node, the Historical Node and the Broker.

The great thing is that you can add as many nodes as you want in the specific area that fits best for you. If you have many queries to run, you can add more Brokers. Or, if a lot of data needs to be batch-ingested, you would add middle managers and so on.

A simple architecture is shown below. You can read more about Druid’s design [here](http://druid.io/docs/latest/design/).

![Image](https://cdn-media-1.freecodecamp.org/images/xeRSbDmEa6pmf5ZOOxBF-hsunHv9i27cfHfU align="left")

### Apache Superset — the UI

The easiest way to query against Druid is through a lightweight, open-source tool called [Apache Superset](https://superset.incubator.apache.org/).

It is easy to use and has all common chart types like Bubble Chart, Word Count, Heatmaps, Boxplot and [many more](https://superset.incubator.apache.org/gallery.html).

Druid provides a Rest-API, and in the newest version also a SQL Query API. This makes it easy to use with any tool, whether it is standard SQL, any existing BI-tool or a custom application.

### Apache Airflow — the Orchestrator

As mentioned in [Orchestrators — Scheduling and monitor workflows](https://www.sspaeti.com/blog/olap-whats-coming-next/#Orchestrators), this is one of the most critical decisions.

In the past, ETL tools like Microsoft SQL Server Integration Services (SSIS) and others were widely used. They were where your data transformation, cleaning and normalisation took place.

In more modern architectures, these tools aren’t enough anymore.

Moreover, code and data transformation logic are much more valuable to other data-savvy people in the company.

I highly recommend you read a blog post from [Maxime Beauchemin](https://medium.com/@maximebeauchemin) about [Functional Data Engineering — a modern paradigm for batch data processing](https://medium.com/@maximebeauchemin/functional-data-engineering-a-modern-paradigm-for-batch-data-processing-2327ec32c42a). This goes much deeper into how modern data pipelines should be.

Also, consider the read of [The Downfall of the Data Engineer](https://medium.com/@maximebeauchemin/the-downfall-of-the-data-engineer-5bfb701e5d6b) where Max explains about the breaking “data silo” and much more.

#### Why use Airflow?

[Apache Airflow](https://airflow.apache.org/) is a very popular tool for this task orchestration. Airflow is written in Python. Tasks are written as Directed Acyclic Graphs ([DAGs](https://en.wikipedia.org/wiki/Directed_acyclic_graph)). These are also written in Python.

Instead of encapsulating your critical transformation logic somewhere in a tool, you place it where it belongs to inside the Orchestrator.

Another advantage is using plain Python. There is no need to encapsulate other dependencies or requirements, like fetching from an FTP, copying data from A to B, writing a batch-file. You do that and everything else in the same place.

#### Features of Airflow

Moreover, you get a fully functional overview of all current tasks in one place.

![Image](https://cdn-media-1.freecodecamp.org/images/RoR-Nl7GwR7qSU1rWxUX8RYAywKVwfqfgMPO align="left")

More relevant features of Airflow are that you write workflows as if you are writing programs. External jobs like Databricks, Spark, etc. are no problems.

Job testing goes through Airflow itself. That includes passing parameters to other jobs downstream or verifing what is running on Airflow and seeing the actual code. The log files and other meta-data are accessible through the web GUI.

(Re)run only on parts of the workflow and dependent tasks is a crucial feature which comes out of the box when you create your workflows with Airflow. The jobs/tasks are run in a context, the scheduler passes in the necessary details plus the work gets distributed across your cluster at the task level, not at the DAG level.

For many more feature visit the [full list](https://gtoonstra.github.io/etl-with-airflow/great.html).

#### ETL with Apache Airflow

If you want to start with Apache Airflow as your new ETL-tool, please start with this [ETL best practices with Airflow](https://gtoonstra.github.io/etl-with-airflow/) shared with you. It has simple [ETL](https://gtoonstra.github.io/etl-with-airflow/etlexample.html)\-examples, with plain SQL, with [HIVE](https://gtoonstra.github.io/etl-with-airflow/hiveexample.html), with [Data Vault](https://gtoonstra.github.io/etl-with-airflow/datavault.html), [Data Vault 2](https://gtoonstra.github.io/etl-with-airflow/datavault2.html), and [Data Vault with Big Data processes](https://gtoonstra.github.io/etl-with-airflow/datavault-bigdata.html). It gives you an excellent overview of what’s possible and also how you would approach it.

At the same time, there is a Docker container that you can use, meaning you don’t even have to set-up any infrastructure. You can pull the container from [here](https://gtoonstra.github.io/etl-with-airflow/etlexample.html#run-airflow-from-docker).

For the GitHub-repo follow the link on [etl-with-airflow](https://github.com/gtoonstra/etl-with-airflow).

### Conclusion

If you’re searching for open-source data architecture, you cannot ignore Druid for speedy OLAP responses, Apache Airflow as an orchestrator that keeps your data lineage and schedules in line, plus an easy to use dashboard tool like Apache Superset.

My experience so far is that Druid is bloody fast and a perfect fit for [OLAP cube replacements](https://medium.com/@sspaeti/olap-whats-coming-next-be01c1567b87) in a traditional way, but still needs a more relaxed startup to install clusters, ingest data, view logs etc. If you need that, have a look at [Impy](https://imply.io/) which was created by the founders of Druid. It creates all the services around Druid that you need. Unfortunately, though, it’s not open-source.

Apache Airflow and its features as an orchestrator are something which has not happened much yet in traditional Business Intelligence environments. I believe this change comes very naturally when you start using open-source and more new technologies.

And Apache Superset is an easy and fast way to be up and running and showing data from Druid. There for better tools like Tableau, etc., but not for free. That’s why Superset fits well in the ecosystem if you’re already using the above open-source technologies. But as an enterprise company, you might want to spend some money in that category because that is what the users can see at the end of the day.

Related Links:

* [Understanding Apache Airflow’s key concepts](https://medium.com/@dustinstansbury/understanding-apache-airflows-key-concepts-a96efed52b1a)
    
* [How Druid enables analytics at Airbnb](https://medium.com/airbnb-engineering/druid-airbnb-data-platform-601c312f2a4c)
    
* [Google launches Cloud Composer, a new workflow automation tool for developers](https://techcrunch.com/2018/05/01/google-launches-cloud-composer-a-new-workflow-automation-tool-for-developers/)
    
* [A fully managed workflow orchestration service built on Apache Airflow](https://cloud.google.com/composer/)
    
* [Integrating Apache Airflow and Databricks: Building ETL pipelines with Apache Spark](https://databricks.com/blog/2016/12/08/integrating-apache-airflow-databricks-building-etl-pipelines-apache-spark.html)
    
* [ETL with Apache Airflow](https://gtoonstra.github.io/etl-with-airflow/)
    
* [What is Data Engineering and the future of Data Warehousing](https://hackernoon.com/data-engineering-the-future-of-data-warehousing-81bc953a9b00)
    
* [Imply — Managed Druid platform (closed-source)](https://imply.io/)
    
* [Ultra-fast OLAP Analytics with Apache Hive and Druid](https://de.hortonworks.com/blog/apache-hive-druid-part-1-3/)
    

*Originally published at* [*www.sspaeti.com*](https://www.sspaeti.com/blog/open-source-data-warehousing-druid-airflow-superset/) *on November 29, 2018.*
