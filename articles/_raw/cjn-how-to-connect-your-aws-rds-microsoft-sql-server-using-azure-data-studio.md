---
title: How to Connect your AWS RDS Microsoft SQL Server using Azure Data Studio
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-29T09:41:13.000Z'
originalURL: https://freecodecamp.org/news/cjn-how-to-connect-your-aws-rds-microsoft-sql-server-using-azure-data-studio
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-29-at-2.36.26-AM.png
tags:
- name: AWS
  slug: aws
- name: Azure
  slug: azure
- name: database
  slug: database
- name: MSSQL
  slug: mssql
- name: SQL
  slug: sql
seo_title: null
seo_desc: "By Clark Jason Ngo\nThe goal of this guide is to play around with cloud\
  \ databases and connect one to a database tool. Once you are done with this guide,\
  \ you should be able to create databases and tables, and more. \nImporting a sample\
  \ database is a pai..."
---

By Clark Jason Ngo

The goal of this guide is to play around with cloud databases and connect one to a database tool. Once you are done with this guide, you should be able to create databases and tables, and more. 

Importing a sample database is a pain, so here's another guide that I created: [_How to Import a Sample Database to your AWS RDS Microsoft SQL Server using S3_](https://www.freecodecamp.org/news/cjn-how-to-import-a-sample-database-to-your-aws-rds-microsoft-sql-server-using-s3/).

Luckily as I was new to this, I also discovered how to connect to a MSSQL Server with Docker to Azure Data Studio. Check this guide: _[How to Connect your AWS RDS Microsoft SQL Server using Azure Data Studio](https://www.freecodecamp.org/news/cjn-how-to-connect-your-microsoft-sql-server-docker-container-with-azure-data-studio/)_.

We will be touching on the technologies shown below:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-242.png)

* Database: Amazon Relational RDS with MSSQL Server Express Edition
* Database tool and GUI: Azure Data Studio

## Creating and Configuring your AWS RDS MSSQL Server Instance

### Sign in to AWS.com:

1. Go to [https://aws.amazon.com/console/](https://aws.amazon.com/console/)
2. Click **Sign into your AWS account**

### Create a Microsoft SQL Server DB Instance:

1. In the Create database section, choose **Create database**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-213.png)

2.   Choose **Easy Create** for database creation method.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-216.png)

3.   Choose the **Microsoft SQL Server** icon for engine type.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-217.png)

4.   Select **Free Tier** for the DB instance size.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-218.png)

5.   Fill in the following details for DB instance identifier:

* **DB instance identifier:** myrdstest.
* **Master username:** Type a username
* **Master password:** Type a password that contains from 8 to 41 printable.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-221.png)

6.   Select **Create database**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-220.png)

Note: It might take a couple of minutes to provision

If you accidentally exit the page, you should see your database **myrdstest** under **RDS** > **Databases**.

For a more detailed tutorial, follow the steps in the [AWS docs](https://aws.amazon.com/getting-started/tutorials/create-microsoft-sql-db/).

### Allow Public Access to your RDS instance

1. Click **Modify**

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-223.png)

2.   Choose **Yes** in Public Accessibility under Network & Security.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-224.png)

3.  Choose **Apply immediately** under Scheduling of modifications, then Click **Modify DB instance**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-225.png)

### Allow Inbound Rules

1. Click **default (sg-0000d009)** under VPC security groups.

Note: the number is different in your own instance.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-226.png)

2.   Click **Inbound**, then click **Edit inbound rules**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-228.png)

3.  Choose **My IP** in Source, then click **Save rules**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-227.png)

## Test your Connection to AWS RDS

Open your terminal (MacOS), and type the following: **nc -zv _aws_rds_endpoint port_number_**

Successful connection example:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-229.png)

Failed connection example:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-230.png)

Make sure your RDS instance is Public and Inbound rules allows your IP.

## Download a SQL Server GUI - Azure Data Studio

[Azure Data Studio](https://database.guide/what-is-azure-data-studio/) (formerly SQL Operations Studio) is a free GUI management tool that you can use to manage SQL Server. You can use it to create and manage databases, write queries, backup and restore databases, and more.

Azure Data Studio is available on Windows, Mac, and Linux.

### Install Azure Data Studio

To install Azure Data Studio on a Mac:

1. Visit the [Azure Data Studio download page](https://docs.microsoft.com/en-us/sql/azure-data-studio/download), and click the .zip file for macOS
2. Once the .zip file has finished downloading, double click it to expand its contents
3. Drag the .app file to the Applications folder.

### Connect to SQL Server

Now that Azure Data Studio is installed, you can use it to connect to SQL Server:

1. Launch Azure Data Studio. It is located in your Applications folder.
2. Enter the login credentials and other information for the SQL Server instance that you’d like to connect to:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-231.png)

It should look similar to this:

* **Server Name**: [AWS RDS Endpoint], [port number]   
**Example**: myrdstest.blahblahblah.us-west-2/ds.amazonaws.com, 1433
* **Authentication Type**: SQL Login
* **User name**: [your AWS username]
* **Password**: [your AWS password]
* **Database Name**: <default>
* **Server Group**: <default>

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-232.png)

If you used a port other than the default 1433, click **Advanced** and enter it in the Port field.

Alternatively, you can append it to your server name with a comma in between. For example, if you used port 1400, type in localhost,1400.

If you get an error:

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-233.png)

Make sure your RDS instance is Public and Inbound rules allows your IP.

You can now go ahead and create databases, run scripts, and perform other SQL Server management tasks.

1. Click **New Query**

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-234.png)

2.   Type **SELECT @@VERSION**, then Click **Run Query**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-235.png)



You should be able to see: _Microsoft SQL Server_ in the Results

Congratulations! ???

## Resources:

* [How to Create a Microsoft SQL DB](https://aws.amazon.com/getting-started/tutorials/create-microsoft-sql-db/)

Connect with me on LinkedIn [here](https://www.linkedin.com/in/clarkngo/)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-184.png)


