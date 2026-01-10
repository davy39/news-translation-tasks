---
title: How to Import a Sample Database to your AWS RDS Microsoft SQL Server using
  S3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-29T10:13:35.000Z'
originalURL: https://freecodecamp.org/news/cjn-how-to-import-a-sample-database-to-your-aws-rds-microsoft-sql-server-using-s3
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-29-at-3.12.23-AM.png
tags:
- name: mssql
  slug: mssql-2
- name: Azure
  slug: azure
- name: Backup
  slug: backup
- name: database
  slug: database
- name: S3
  slug: s3
seo_title: null
seo_desc: 'By Clark Jason Ngo

  This guide was created because it was so hard to find a way to play around with
  a sample database using AWS RDS MSSQL Server. I hope you find this helpful.

  If you haven''t set up your AWS RDS Microsoft SQL Server and Azure Data Stud...'
---

By Clark Jason Ngo

This guide was created because it was so hard to find a way to play around with a sample database using AWS RDS MSSQL Server. I hope you find this helpful.

If you haven't set up your AWS RDS Microsoft SQL Server and Azure Data Studio, check this guide first: _[How to Connect your AWS RDS Microsoft SQL Server using Azure Data Studio](https://www.freecodecamp.org/news/cjn-how-to-connect-your-aws-rds-microsoft-sql-server-using-azure-data-studio/)_.

We will be touching the technologies shown below:  


![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-244.png)

* Database: AWS RDS Microsoft SQL Server Express Edition
* Database tool and GUI: Azure Data Studio
* Sample database backup copy: Amazon S3 Bucket



## AdventureWorks sample database backup copy

To get the OLTP downloads of AdventureWorks, go to this [link](https://docs.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver15) and choose any sample database. In my example, I choose `AdventureWorks2017.bak`. We will upload this to the S3 Bucket.

## Amazon S3 Bucket

### Creating the S3 Bucket

1. Create a bucket. You can choose any bucket name (example: yourname-sample-dbs).

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-202.png)



2. Make sure the region is same as the AWS RDS instance. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-203.png)

3. Tick the following checkboxes:

* Block public access to buckets and objects granted through _new_ access control lists (ACLs)
* Block public access and objects granted through _any_ access control lists (ACLs)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-204.png)

4. Access your bucket again by clicking on your created bucket.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-205.png)

### Uploading the file to the S3 bucket

1. Click **Upload**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-206.png)

2. Choose the database backup file. For example: `AdventureWorks2017.bak`. Keep choosing **Next** and choose **Upload** at the Review section.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-207.png)

3. Update your Bucket Policy to allow access to your S3 Bucket. Note that your ARN will differ to mine. Hit **Save** afterwards.

```json
{
    "Version": "2012-10-17",
    "Id": "Policy1548223592786",
    "Statement": [
        {
            "Sid": "Stmt1548223591553",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::changethis/*"
        }
    ]
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-208.png)



## AWS RDS - MSSQL Server Express  


### Creating an Option Group for your RDS instance

1. Click **Option groups**,

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-194.png)

2. Create an option group. Choose any name and description. For the Engine, it should match your RDS instance. In my example, I used SQL Server Express Edition so I choose `sqlserver-ex`.

Here are the following Engines and their abbreviations:

* SQL Server Enterprise Edition: `sqlserver-ee`
* SQL Server Standard Edition: `sqlserver-se`
* SQL Server Web Edition: `sqlserver-web`
* SQL Server Express Edition: `sqlserver-ex`

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-195.png)

3. Once you have created the option group, you'll need to **Add option**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-199.png)

4. Choose **SQLSERVER_BACKUP_RESTORE** for your Option name. For the IAM role, it is best to create a new role.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-200.png)

5. Choose the S3 bucket where your database file is hosted. For scheduling, choose **Immediately**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-201.png)

6. Go back to your AWS RDS MSSQL Server instance and click **Modify**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-196.png)

7. Choose the created option group with `sql-server-express-backup`, then Click Continue.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-197.png)

8. Choose to **Apply immediately** for scheduling of modifications. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-198.png)

9. Go back to your AWS RDS MSSQL Server instance page and scroll down and modify _Manage IAM Roles_. Add the IAM role you have created in S3. For the Feature, choose **S3_INTEGRATION**. 

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-210.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-211.png)

## Azure Data Studio

### Importing the sample database in S3 bucket through restore function

1. In your connected AWS RDS MSSQL Server, create a new query and type in the following:

```sql
exec msdb.dbo.rds_restore_database 
@restore_db_name='AdventureWorks-test', 
@s3_arn_to_restore_from='arn:aws:s3:::clark-sample-dbs/AdventureWorks2017.bak';
```



![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-209.png)

Refresh your Azure Data Studio. Also, try restarting the application if your database did not appear or don't have permission to access it.

Now you are done! Good job! ???

Resources:

* [https://aws.amazon.com/premiumsupport/knowledge-center/native-backup-rds-sql-server/](https://aws.amazon.com/premiumsupport/knowledge-center/native-backup-rds-sql-server/)

Connect with me on LinkedIn [here](https://www.linkedin.com/in/clarkngo/)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-243.png)

