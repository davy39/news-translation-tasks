---
title: How to Use Google Dataproc – Example with PySpark and Jupyter Notebook
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-03T15:14:31.000Z'
originalURL: https://freecodecamp.org/news/what-is-google-dataproc
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/My-project.jpg
tags:
- name: Google Cloud Platform
  slug: google-cloud-platform
- name: hadoop
  slug: hadoop
- name: Machine Learning
  slug: machine-learning
- name: spark
  slug: spark
seo_title: null
seo_desc: "By Sameer Shukla\nIn this article, I'll explain what Dataproc is and how\
  \ it works. \nDataproc is a Google Cloud Platform managed service for Spark and\
  \ Hadoop which helps you with Big Data Processing, ETL, and Machine Learning. It\
  \ provides a Hadoop clus..."
---

By Sameer Shukla

In this article, I'll explain what Dataproc is and how it works. 

Dataproc is a Google Cloud Platform managed service for Spark and Hadoop which helps you with Big Data Processing, ETL, and Machine Learning. It provides a Hadoop cluster and supports Hadoop ecosystems tools like Flink, Hive, Presto, Pig, and Spark.

Dataproc is an auto-scaling cluster which manages logging, monitoring, cluster creation of your choice and job orchestration. You'll need to manually provision the cluster, but once the cluster is provisioned you can submit jobs to Spark, Flink, Presto, and Hadoop.

Dataproc has implicit integration with other GCP products like Compute Engine, Cloud Storage, Bigtable, BigQuery, Cloud Monitoring, and so on. The jobs supported by Dataproc are MapReduce, Spark, PySpark, SparkSQL, SparkR, Hive and Pig.

Apart from that, Dataproc allows native integration with Jupyter Notebooks as well, which we'll cover later in this article.

In the article, we are going to cover:

1. Dataproc cluster types and how to set Dataproc up 
2. How to submit a PySpark job to Dataproc
3. How to create a Notebook instance and execute PySpark jobs through Jupyter Notebook. 

## How to Create a Dataproc Cluster

Dataproc has three cluster types:

1. Standard
2. Single Node
3. High Availability

The Standard cluster can consist of 1 master and N worker nodes. The Single Node has only 1 master and 0 worker nodes. For production purposes, you should use the High Availability cluster which has 3 master and N worker nodes. 

For our learning purposes, a single node cluster is sufficient which has only 1 master Node.

Creating Dataproc clusters in GCP is straightforward. First, we'll need to enable Dataproc, and then we'll be able to create the cluster.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-185.png)
_Start Dataproc cluster creation_

When you click "Create Cluster", GCP gives you the option to select Cluster Type, Name of Cluster, Location, Auto-Scaling Options, and more.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-199.png)
_Parameters required for Cluster_

Since we've selected the Single Node Cluster option, this means that auto-scaling is disabled as the cluster consists of only 1 master node. 

The Configure Nodes option allows us to select the type of machine family like Compute Optimized, GPU and General-Purpose. 

In this tutorial, we'll be using the General-Purpose machine option. Through this, you can select Machine Type, Primary Disk Size, and Disk-Type options.

The Machine Type we're going to select is n1-standard-2 which has 2 CPU’s and 7.5 GB of memory. The Primary Disk size is 100GB which is sufficient for our demo purposes here.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-200.png)
_Master Node Configuration_

We've selected the cluster type of Single Node, which is why the configuration consists only of a master node. If you select any other Cluster Type, then you'll also need to configure the master node and worker nodes.

From the Customise Cluster option, select the default network configuration:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-201.png)

Use the option "Scheduled Deletion" in case no cluster is required at a specified future time (or say after a few hours, days, or minutes).

![Image](https://www.freecodecamp.org/news/content/images/2022/05/5_ml_resize_x2_colored_toned_light_ai-1.jpg)
_Schedule Deleting Setting_

Here, we've set "Timeout" to be 2 hours, so the cluster will be automatically deleted after 2 hours.

We'll use the default security option which is a Google-managed encryption key. When you click "Create", it'll start creating the cluster.  

You can also create the cluster using the ‘gcloud’ command which you'll find on the ‘EQUIVALENT COMMAND LINE’ option as shown in image below. 

And you can create a cluster using a POST request which you'll find in the ‘Equivalent REST’ option.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-203.png)
_gcloud and REST option for Cluster creation_

After few minutes the cluster with 1 master node will be ready for use.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-204.png)
_Cluster Up and Running_

You can find details about the VM instances if you click on "Cluster Name":

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-205.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-206.png)

## How to Submit a PySpark Job

Let’s briefly understand how a PySpark Job works before submitting one to Dataproc. It’s a simple job of identifying the distinct elements from the list containing duplicate elements. 

```python
#! /usr/bin/python

import pyspark

#Create List
numbers = [1,2,1,2,3,4,4,6]

#SparkContext
sc = pyspark.SparkContext()

# Creating RDD using parallelize method of SparkContext
rdd = sc.parallelize(numbers)

#Returning distinct elements from RDD
distinct_numbers = rdd.distinct().collect()

#Print
print('Distinct Numbers:', distinct_numbers)
```

Upload the .py file to the GCS bucket, and we'll need its reference while configuring the PySpark Job.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-21.png)
_Job GCS Location_

Submitting jobs in Dataproc is straightforward. You just need to select “Submit Job” option:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-209.png)
_Job Submission_

For submitting a Job, you'll need to provide the Job ID which is the name of the job, the region, the cluster name (which is going to be the name of cluster, "first-data-proc-cluster"), and the job type which is going to be PySpark.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-223.png)
_Parameters required for Job Submission_

You can get the Python file location from the GCS bucket where the Python file is uploaded – you'll find it at gsutil URI.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-24.png)

No other additional parameters are required, and we can now submit the job:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-224.png)

After execution, you should be able to find the distinct numbers in the logs:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-213.png)
_Logs_

## How to Create a Jupyter Notebook Instance

You can associate a notebook instance with Dataproc Hub. To do that, GCP provisions a cluster for each Notebook Instance. We can execute PySpark and SparkR types of jobs from the notebook. 

To create a notebook, use the "Workbench" option like below:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-26.png)

Make sure you go through the usual configurations like Notebook Name, Region, Environment (Dataproc Hub), and Machine Configuration (we're using 2 vCPUs with 7.5 GB RAM). We're using the default Network settings, and in the Permission section, select the "Service account" option.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-225.png)
_Parameters required for Notebook Cluster Creation_

Click Create:

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-216.png)
_Notebook Cluster Up &amp; Running_

The "OPEN JUPYTYERLAB" option allows users to specify the cluster options and zone for their notebook.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-226.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-227.png)

Once the provisioning is completed, the Notebook gives you a few kernel options:

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-27.png)

Click on PySpark which will allow you to execute jobs through the Notebook.

A SparkContext instance will already be available, so you don't need to explicitly create SparkContext. Apart from that, the program remains the same.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-220.png)
_Code snapshot on Notebook_

## Conclusion

Working on Spark and Hadoop becomes much easier when you're using GCP Dataproc. The best part is that you can create a notebook cluster which makes development simpler.

