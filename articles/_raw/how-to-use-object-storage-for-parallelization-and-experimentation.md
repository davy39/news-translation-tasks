---
title: How to Use Object Storage for Data Parallelization and Experimentation
subtitle: ''
author: Ry Vee
co_authors: []
series: null
date: '2021-09-27T14:09:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-object-storage-for-parallelization-and-experimentation
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/article-cover-pic.png
tags:
- name: big data
  slug: big-data
- name: data analysis
  slug: data-analysis
- name: data analytics
  slug: data-analytics
- name: storage
  slug: storage
seo_title: null
seo_desc: "By using big data, companies can learn a lot about how their businesses\
  \ are performing. Analytics on sales, churn rates, and other basic metrics are available\
  \ in almost real time as data comes in. \nThen there are more complex analyses that\
  \ you'll nee..."
---

By using big data, companies can learn a lot about how their businesses are performing. Analytics on sales, churn rates, and other basic metrics are available in almost real time as data comes in. 

Then there are more complex analyses that you'll need to do. At times relationships between two seemingly unrelated data sets can provide surprising insights and unveil important opportunities for the organization.

Data scientists and engineers are continuing to improve how they break down and work on data. Experimentation entails discovering the right correlations among data points. 

This means they also need to do some sort of parallelization of such data and resulting models. Parallelization simply means that the same data set is being operated upon in many different ways without damaging the integrity of the original data.

In this article we are going to talk about how you can make sure you're doing such experimentation and parallel processing efficiently and that it provides the maximum insights. We will be tackling different concepts related to data storage and data versioning.

# Block Storage vs Object Storage

For the uninitiated, we first must understand the difference between block and object storage and why the latter is the better option when dealing with data experimentation.

![Image](https://lh4.googleusercontent.com/p8F4n7jqjmQtqquQasDGPEj1eRdxhNIsdMFxX9gIM03w6r6u-VRzU6rn2gMqdF1U3lrGOrjWEPwlBFzR-0cYVHWBWF7tigFiS4m_EtYjw0bU4tPATeWsZNYTFwpZTbyLBAzxqmbX=s0)
_[Image source](https://res.cloudinary.com/practicaldev/image/fetch/s--PYImgKrK--/c_imagga_scale,f_auto,fl_progressive,h_500,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/4519hl0nf6aze73pyvsr.png)_

## What is Block Storage?

It is called “block storage” (also known as [SAN](https://www.snia.org/education/storage_networking_primer/san/what_san)) because each dataset (in the form of files) is grouped into blocks stored in disks. 

A classic example of block storage is the file system on your personal computer. For enterprise-level use-cases, it is scaled through a network of hard drives connected through fiber optic cables. 

There are a few disadvantages to using block storage. First, if a sector (or a block) becomes corrupted, it can damage the files. Another problem is the lack of scalability (expanding the network of fiber optic cables is costly).

## What is Object Storage?

In object storage, data is stored as objects. Each object contains the actual data, called the blob, a unique identifier (UUID), and metadata, which contains information about the object (such as timestamp, version, and author).

Object storage makes it cost-effective to scale your data store—you don’t need complex hardware for this. It also makes data retrieval faster as each object can be retrieved through its UUID. 

This is in contrast to block storage, where each data location needs to be identified before the actual information can be retrieved.

One disadvantage of using object storage is that data can only be written once and cannot be updated. But this isn’t really a disadvantage as we will see further on in this article.

## What Problems Does Object Storage Solve?

As we have already seen, data retrieval can be incredibly fast with object storage (no matter the size of the data store). But when it comes to data experimentation and data parallelization, object storage shines the brightest.

As mentioned before, you can't overwrite any data already stored as an object. This ensures object storage is protected from unwanted (or unauthorized) data destruction or updating. That’s great to know if you do a lot of data processing where accidental corruption of information could happen.

One other problem that object storage can solve is that it doesn’t require data to be structured. As companies produce and consume tremendous amounts of information every moment, often non-structured data (such as PDFs, videos, images) are not so easily processed into useful forms (such as for analytics or dashboards). 

With object storage, this is now possible. You can now use non-structured data to develop machine learning models.

With data storage, it’s possible to have different versions of the same blob (with different metadata). As there is Git for code version control, we can have similar ways of managing different versions of the same data.

This brings us to the concept of data lakes.

## What are Data Lakes?

Data lakes are central repositories of data that don’t care which format such data is in. 

Companies produce and consume tremendous amounts of data. Such data traditionally sits in silos because they belong to different departments or are in different forms (for example, videos aren’t stored in the same directory as the data in the MySQL database). 

With data lakes, any department in the enterprise can store information without the need to pre-process it. Likewise, any data can be retrieved and analyzed by anybody from any department.

Data lakes are important because they make data analytics extremely fast and convenient.

## How Data Experimentation and Parallelization Work with Object Storage

As with developing software, working with data requires us to utilize tools that can aid us in our workflow. A powerful open source tool for experimenting with data and performing parallelization (that is working on the same data to create different sets of machine learning models) is LakeFS.

LakeFS is an open source platform that provides Git-like capabilities when working with data. This means you can create branches (allowing you to experiment with data) and commit versions of data (and data models).

### Why is this Git-like feature important?

First, you need to make sure that your data lake is [ACID](https://mariadb.com/resources/blog/acid-compliance-what-it-means-and-why-you-should-care/) compliant. This means that your data changes can happen in isolation (in branches). Thus, the integrity of the data is maintained in the master branch (until such changes are ready to be merged).

Another important feature of LakeFS is continuous integration of data (again, much like in software development). Enterprises need to incorporate new data quickly and without being disrupted. Therefore, this ability to have a [CI/CD](https://www.infoworld.com/article/3271126/what-is-cicd-continuous-integration-and-continuous-delivery-explained.html) workflow is invaluable. 

So, let’s see how we can get started with using LakeFS with our object storage experimentation and parallelization.

### How to Install LakeFS 

Locally you can install LakeFS by running the following command in your terminal:*  


![Image](https://lh4.googleusercontent.com/pTYRbQlB2_Mp8j_XGxUOvBI0PLf5kuuT1tYV5AxcPmrnq8K5sjLCUBwQqp4klk4rnraQnK9OD5hrudEFUwBLNcvmyNGQqDPkLQ_DkVBoVgCUfITIFdS6d1RxtkTFG_T40ZV0ia0L=s0)
_[Code source](https://carbon.now.sh/?bg=rgba%28171%2C+184%2C+195%2C+1%29&amp;t=seti&amp;wt=none&amp;l=application%2Fx-sh&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=2x&amp;wm=false&amp;code=curl%2520https%253A%252F%252Fcompose.lakefs.io%2520%257C%2520docker-compose%2520-f%2520-%2520up%250A)_

_*This is assuming you have Docker and Docker-Compose installed in your system. If you don’t have Docker and Docker-Compose, you may try other installation methods [here](https://docs.lakefs.io/quickstart/more_quickstart_options.html)._

Now visit [http://127.0.0.1:8000/setup](http://127.0.0.1:8000/setup) in your browser to verify you have installed it correctly.

### How to Create a Repository in LakeFS

Once you’ve verified that LakeFS is installed correctly, go ahead and create an admin user.

![Image](https://lh5.googleusercontent.com/kRpsNjJe60f7fiIEFC0O5ZbY88F9g-F4X-GRtl8L8WiVJ_sDiKcnz-0jmprZc-bVkfq029fYhq4K-jdBXyBQttc012Nv4v6j2vbJvk4jnbs71BF9Wulo_5JwsvmSjRE1nkQ-ltRe=s0)
_[Image source](https://docs.lakefs.io/assets/img/setup.png)_

![Image](https://lh3.googleusercontent.com/oez-1Q1JH6Q_cqUh0tKE1bW-IbEXg92UP4NVkTy_o-vVETELASw8R8CoPS5ogWDZNl4hH8W3cb68_PvEECO1os9U1sgfJFA2PMnc1J57wEjomp9SrN0ZZK-OXoOjJpZcF-LPZlhu=s0)
_[Image source](https://docs.lakefs.io/assets/img/setup_done.png)_

Click on the login link and log in as an administrator. 

On the page to which you get redirected, click on Create Repository. A popup will appear:

![Image](https://lh6.googleusercontent.com/2abxJeRjLk7IRzhohW7jlG3cKQKH4kRCjIyVbQkHe_Fa9qdcGPdrbcTsFRhW7lv3S5LQtfa4xBmnNu0wRqhFSvwi1hp5_ARB_fRJlcLgz1TmDa_a9DQ-apmcIiclMLwsgfuyoD9P=s0)
_[Image source](https://docs.lakefs.io/assets/img/create_repo_local.png)_

Congratulations! You now have your first repository. This is the main “bucket” in which you are going to store your data. 

Next, we’ll start adding some data.

### How to Add Data to your LakeFS Repository

Visit [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) to install AWS CLI.

With the credentials created during the admin-user creation phase, configure a new connection profile:

![Image](https://lh5.googleusercontent.com/D9FDuc11VgqsUr5LfN2UE_zTQYSKinNHB_saQxvr0MJj2yurnDCTqEC0cWA-dvOj3TYGMxJq52Una4zpaG6hrImrAaOWA43V1nMsUg0NpI9XIj8lKF6THD3ZoC0BNMqd-uRUsS6p=s0)
_[Code source](https://carbon.now.sh/?bg=rgba%28171%2C+184%2C+195%2C+1%29&amp;t=seti&amp;wt=none&amp;l=application%2Fx-sh&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=2x&amp;wm=false&amp;code=aws%2520configure%2520--profile%2520local%250A%2523%2520output%253A%250A%2523%2520AWS%2520Access%2520Key%2520ID%2520%255BNone%255D%253A%2520AKIAJVHTOKZWGCD2QQYQ%250A%2523%2520AWS%2520Secret%2520Access%2520Key%2520%255BNone%255D%253A%2520****************************************%250A%2523%2520Default%2520region%2520name%2520%255BNone%255D%253A%250A%2523%2520Default%2520output%2520format%2520%255BNone%255D%253A%250A)_

To test if the connection is working, run the following:

![Image](https://lh5.googleusercontent.com/oP-iisEz7w9qQM-zQaAUcdhXj_YMRGamhV-AwwNfFsDVm_p4HcKlGsw0sVD0aJS-Q-3rCy3VlhtcvtBxJgFCrHQLXrPB7ZyHVril1iGeWKP_mqPPrxizpw8NNAGWdNc2ZF36mfX4=s0)
_[Code source](https://carbon.now.sh/?bg=rgba%28171%2C+184%2C+195%2C+1%29&amp;t=seti&amp;wt=none&amp;l=application%2Fx-sh&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=2x&amp;wm=false&amp;code=aws%2520--endpoint-url%253Dhttp%253A%252F%252Flocalhost%253A8000%2520--profile%2520local%2520s3%2520ls%250A%2523%2520output%253A%250A%2523%25202021-06-15%252013%253A43%253A03%2520example-repo%250A)_

Now, to copy files into the main branch:

![Image](https://lh5.googleusercontent.com/Z_3sbfX6IMJzPkYeejJ1O9ftjkO3c4kPk_rlCJ1iOP2FgTnJTZ03cB8C8Ml2u4bet4cvBS60rHt7Ns-xgLWix422-w3ZvpGQCyeGKgBDd0Oog-sV-E4XSpV4ARpoYeQhR2INZV_H=s0)
_[Code source](https://carbon.now.sh/?bg=rgba%28171%2C+184%2C+195%2C+1%29&amp;t=seti&amp;wt=none&amp;l=application%2Fx-sh&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=2x&amp;wm=false&amp;code=aws%2520--endpoint-url%253Dhttp%253A%252F%252Flocalhost%253A8000%2520--profile%2520local%2520s3%2520cp%2520.%252Ffoo.txt%2520s3%253A%252F%252Fexample-repo%252Fmain%252F%250A%2523%2520output%253A%250A%2523%2520upload%253A%2520.%252Ffoo.txt%2520to%2520s3%253A%252F%252Fexample-repo%252Fmain%252Ffoo.txt%250A)_

Just note that we need to prefix the path with the name of the branch we want to use.

Now, we will see the file we’ve added in the UI:

![Image](https://lh6.googleusercontent.com/F8UCd8s43wM0y4WgRhHWy04p2rzBQ1ccvUZhppCzl30fE0FJEpMQb7Y1X06x-WDx3J9I5LELQv4FtFKOYWJqU2E9dENB5MMqjsv-MYfLI-oCEXLekhWH9xTcazm1-_Fmo4NxgDb_=s0)
_[Image source](https://docs.lakefs.io/assets/img/object_added.png)_

  
Next, we will need to know how to commit and create branches. To do that, we will need to install the LakeFS CLI.

### How to Install the LakeFS CLI

You need to first download the binary file [here](https://docs.lakefs.io/#downloads). 

Again, we need to use the earlier created admin credentials:

![Image](https://lh4.googleusercontent.com/KQntIwi6YaOyp2kKvKLxeYs4Il4czCGCv8fj2_PFhg2Bqy2RRGNNQtLsCxS8YT57DEH-Q63obz7emujS5tST4aoPx0qb4XLjJV3AeKEwRwQGATfJd6us3BA5Svo7Lz_i3k_Smy7N=s0)
_[Code source](https://carbon.now.sh/?bg=rgba%28171%2C+184%2C+195%2C+1%29&amp;t=seti&amp;wt=none&amp;l=application%2Fx-sh&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=2x&amp;wm=false&amp;code=lakectl%2520config%250A%2523%2520output%253A%250A%2523%2520Config%2520file%2520%252Fhome%252Fjanedoe%252F.lakectl.yaml%2520will%2520be%2520used%250A%2523%2520Access%2520key%2520ID%253A%2520AKIAJVHTOKZWGCD2QQYQ%250A%2523%2520Secret%2520access%2520key%253A%2520****************************************%250A%2523%2520Server%2520endpoint%2520URL%253A%2520http%253A%252F%252Flocalhost%253A8000%252Fapi%252Fv1%250A)_

Here are some of the commands we can run to try it out:

![Image](https://lh4.googleusercontent.com/4HuuBJwfpif6TzMS5spkzhkLQf_TC-rZ6WMjAiOOrsv3z8iF2vaTtKTjzicnm5qDjXmLq_aSGqXvAF7RE43BWd9hGB7gUSb76w1bt6ntyLJgAVFBMLwP7uYRPLFUd-1G27kVER7O=s0)
_[Code source](https://carbon.now.sh/?bg=rgba%28171%2C+184%2C+195%2C+1%29&amp;t=seti&amp;wt=none&amp;l=application%2Fx-sh&amp;ds=true&amp;dsyoff=20px&amp;dsblur=68px&amp;wc=true&amp;wa=true&amp;pv=56px&amp;ph=56px&amp;ln=false&amp;fl=1&amp;fm=Hack&amp;fs=14px&amp;lh=133%25&amp;si=false&amp;es=2x&amp;wm=false&amp;code=lakectl%2520branch%2520list%2520lakefs%253A%252F%252Fexample-repo%250A%2523%2520output%253A%250A%2523%2520%252B----------%252B------------------------------------------------------------------%252B%250A%2523%2520%257C%2520REF%2520NAME%2520%257C%2520COMMIT%2520ID%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%2520%257C%250A%2523%2520%252B----------%252B------------------------------------------------------------------%252B%250A%2523%2520%257C%2520main%2520%2520%2520%2520%2520%257C%2520a91f56a7e11be1348fc405053e5234e4af7d6da01ed02f3d9a8ba7b1f71499c8%2520%257C%250A%2523%2520%252B----------%252B------------------------------------------------------------------%252B%250A%2520%2520%2520%2520%2520%250Alakectl%2520commit%2520lakefs%253A%252F%252Fexample-repo%252Fmain%2520-m%2520%27added%2520our%2520first%2520file%21%27%250A%2523%2520output%253A%250A%2523%2520Commit%2520for%2520branch%2520%2522main%2522%2520done.%250A%2523%2520%250A%2523%2520ID%253A%2520901f7b21e1508e761642b142aea0ccf28451675199655381f65101ea230ebb87%250A%2523%2520Timestamp%253A%25202021-06-15%252013%253A48%253A37%2520%252B0300%2520IDT%250A%2523%2520Parents%253A%2520a91f56a7e11be1348fc405053e5234e4af7d6da01ed02f3d9a8ba7b1f71499c8%250A%2520%2520%250Alakectl%2520log%2520lakefs%253A%252F%252Fexample-repo%252Fmain%250A%2523%2520output%253A%2520%2520%250A%2523%2520commit%2520901f7b21e1508e761642b142aea0ccf28451675199655381f65101ea230ebb87%250A%2523%2520Author%253A%2520Example%2520User%2520%253Cuser%2540example.com%253E%250A%2523%2520Date%253A%25202021-06-15%252013%253A48%253A37%2520%252B0300%2520IDT%250A%2520%2520%2520%2520%2520%2520%2520%250A%2520%2520%2520%2520%2520%2520added%2520our%2520first%2520file%21%250A%2520%2520%2520%2520%2520%2520%2520)_

You can find all the other commands, such as branch creation, and so on, [online](https://docs.lakefs.io/reference/commands.html).

There you have it! Now, you can work with your data any way you like. Experiment without guilt and create multiple versions of your data models.

## In Closing

In this article, we covered a bit of ground. We learned the different kinds of data storage mechanisms and why object storage has a lot of edge when dealing with data experimentations and parallelism. 

Next, we looked into data lakes and LakeFS, which is a powerful tool for working with data.

At first, it might seem a daunting task. But, as we’ve shown here, with the right set of tools and knowledge, there’s a lot you can accomplish.

  


  


  


  


  


  

