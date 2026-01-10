---
title: How to Back Up and Restore Azure SQL Databases
subtitle: ''
author: Alex Tray
co_authors: []
series: null
date: '2024-01-24T22:34:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-back-up-and-restore-sql-azure-database
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/maxresdefault.jpg
tags:
- name: Azure
  slug: azure
- name: Backup
  slug: backup
- name: database
  slug: database
- name: SQL
  slug: sql
seo_title: null
seo_desc: Microsoft's Azure provides many services via a single cloud, which lets
  them offer one solution for multiple corporate infrastructures. Development teams
  often use Azure because they value the opportunity to run SQL databases in the cloud
  and complet...
---

Microsoft's Azure provides many services via a single cloud, which lets them offer one solution for multiple corporate infrastructures. Development teams often use Azure because they value the opportunity to run SQL databases in the cloud and complete simple operations via the Azure portal. 

But you'll need to have a way to back up your data, as it's crucial to ensuring the functionality of the production site and the stability of everyday workflows. So creating Azure SQL backups can help you and your team avoid data loss emergencies and have the shortest possible downtime while maintaining control over the [infrastructure](https://www.hostpapa.com/blog/technology/what-is-an-it-infrastructure/).

Another reason to have a current Azure database backup is Microsoft’s policy. Microsoft uses the shared responsibility model, which makes the user responsible for data integrity and recovery while Microsoft only ensures the availability of its services. Microsoft directly recommends using third-party solutions to create database backups. 

In case you run a local SQL Server, you'll need to prepare for the possibility of hardware failures that may result in data loss and downtime. An SQL database on Azure helps mitigate that risk, although it's still prone to human errors or cloud-specific threats like malware. 

These and other threats make enabling Azure SQL database backups necessary for any organization using Microsoft’s service to manage and process data. 

In this tutorial, you'll learn about backing up Azure databases and restoring your data on demand with native instruments provided by Microsoft, including methods like: 

* Built-in Azure database backup functionality
* Cloud archiving
* Secondary database and table management
* Linked server
* Stretch Database

## Why Backup Your SQL Azure Database? 

Although I covered this briefly in the intro, there are many reasons to back up your SQL Azure database data. 

### Disaster Recovery

Data centers can be damaged or destroyed by planned cyberattacks, random malware infiltration ([check out this article](https://www.nakivo.com/blog/how-to-protect-against-ransomware-attacks/) to discover more on ransomware protection), and natural disasters like floods or hurricanes, among others. Backups can be used to swiftly recover data and restore operations after various disaster cases.

### Data Loss Prevention

Data corruption, hardware failure, and accidental or malicious deletion lead to data loss and can threaten an organization. Backup workflows set up to run regularly mean you can quickly recover the data that was lost or corrupted.

### Compliance and Regulations

Compliance requirements and legislative regulations can be severe regardless of your organization’s industry. Mostly, laws require you to keep up with security and perform regular backups for compliance.

### Testing and Development

You can use backups to create Azure database copies for development, troubleshooting, or testing. Thus, you can fix, develop, or improve your organization’s workflows without involving the production environment.

## How to Back Up Your Azure SQL Database

Backing up your Azure SQL database can be challenging if you go through the process without preparation. So that's why I wrote this guide – to help you be prepared. Here's what we'll cover in the following sections:

* Requirements for SQL Azure database backup
* How to configure database backups in Azure with native tools
* Cloud archiving
* Backup verification and data restoration

### SQL Azure Database Backup Requirements

Before backing up your SQL Azure databases, you need to create and configure Azure storage. Before you do that, you'll need to go through the following steps:

First, open the Azure management portal and find **Create a Resource**.

Then, go to **Storage** > **Storage account**. Provide the information, including the location and names of a storage account and resource group according to your preferences. After you enter the information, hit **Next**.

![Image](https://lh7-us.googleusercontent.com/TbuVyIRHXKkKd1__mMSo8RJTktZVnJjK2r8ijtY1h5gvlY5KqkRE8NPsej18m-A1-p3UwF-YO0W0p9AzJa8AW7TwR1yXp531y7qXrm84hJQIuTIKUMwhbnU7WAiUoGRPIdL_SrQCv0nxav4RnCu389o)
_Storage account config_

  
Then go to the advanced section for additional settings. The optimal choice is to set _"_Secure transfer required" as **Enabled** and "Allow access" from **All** networks. For more resilience in case of human error, you can set "Blob soft delete" as **Enabled**. With that setting, you can quickly correct accidental deletions in the storage account.

After that, specify the tags you need to simplify navigating through your infrastructure.

![Image](https://lh7-us.googleusercontent.com/BTXJpa8dz9wKa7p9pQm84fmtqtwD5WEuRB9yh2_Htpa-pF86Zf70CuKP7j32uPR56igplljn6fehCuJEgnMkiCiAcZPZVU_FNEL2JZcrtVjunthzLKQOWp9wbtXLLLKMgYTerYNJpsiQxZjJcMlr05I)
_Azure backup storage tags_

Check the settings once more. If everything is configured correctly, hit **Create**. Your new storage account is now created.

Once the storage volume is created, it's time to configure a backup data storage container. 

Go to the storage account, find **Containers**, then hit the **+ Container** tab there. After that, specify a name for the new container and switch Public access level to **Private (no anonymous access)**.

![Image](https://lh7-us.googleusercontent.com/eGTyBc9-uiRO52QsQ0pGzlWPAZlvyMR0miExCMX-Pck9yPQvUlwKqa0_N-zWc908TzHONdzLC2Kv8ACU5UHJjuJ8G6kBOmgxONkLN5LE33ItBsKOx5XdIKtMg8oYDY6eKrdFrZ0bhuOD535QALtqxMU)
_Container Azure storage account_

  
You can then use the container as a backup storage (.bak files will be stored there in that case).

## Azure Database Backup Configuration

Now, everything is set up for you to back up your SQL Azure database. Do the following to create a database backup:

First, go to **SQL Management Studio**, and establish a connection with the SQL server. After that, right-click the database that should be backed up. The context menu appears, so go to **Tasks** there. Then hit **Back Up…**. 

![Image](https://lh7-us.googleusercontent.com/l5g6ajoZ6ZuBObluCiG7mra9pz9BPgP-iOCAoGh36SY5zfg1yv300oQQ1cvgrVFNL75Nu7roFIVp2BfPze3ag5nTzL1NQYiO_fhUokWSd9fVms1SDcoP5pJ7a4wWdB3fQJWeKbrNIK_-vo2-hiXTDl0)
_SQL server tasks backup_

Then find the Destination tab, and set **Back up to line to URL** there. After that, hit **New container**.

Next, sign in to Azure. Pick the container you created before. Provide your credentials, then hit **OK**.

You’ll see a message asking you to sign in to Azure subscription. Then, choose the container and hit **OK**.

Now, you'll see the configured backup destination URL listed. To start the workflow to back up your Azure data, hit **OK** once again.

When your SQL Azure database backup is completed, the message shows up: "_The backup of database ‘your database name’ completed successfully_."

The backup file in the target container should now be visible from the Azure portal.

Keep in mind that, when uploading backups to any cloud storage, you may face issues if your network connection is not fast enough. 

In case that’s true for you, you can reorganize your backup workflows: send backup data to a physical storage drive first, and then send another copy to the cloud. Thus, you can prevent operational challenges that might appear due to network bandwidth deficiency.

## Cloud Archiving for Azure Database Backups

Databases tend to grow in volume as the organization grows. This means that the storage space required to fit the data and that data's backup increases significantly. Also, the original data volume prolongs the duration of full backup workflows, posing another challenge. 

Of course, the first way to get more storage space is to revise your data regularly and erase records that are irrelevant, outdated, or unnecessary otherwise. Still, it's sometimes difficult to determine if data will be or become unnecessary or irrelevant, especially when dealing with issues of compliance. 

To keep your organization compliant in any case, data archiving can help you solve two problems at once: you can ensure data accessibility on one hand, and save storage space on the other hand.

To archive your SQL database in the cloud, you should first save that database copy to an Azure blob container. Then, to move a newly created blob to the archive tier in the Azure portal, do the following: 

1. Go to the required container where the SQL database is stored.
2. Choose the blob that you need to move.
3. Hit **Change tier**.

![Image](https://lh7-us.googleusercontent.com/p41GC9ys42mQBQGWW1jqcR2xCfACpCYF1MpGG7Qx6EdqzjDSK6xnuqlPRCtDuhEmH_-8E6Lz2gY8H3h1CoZ4_jpScQWUxB-21GXOnuDEBSHVJiGa1zBiHu4JJP2Xntq1fpbPLjbb1-APOTJMO2sdBMk)
_Azure blob container change tier_

4. In the **Access tier** dropdown menu, choose **Archive**.

![Image](https://lh7-us.googleusercontent.com/qlyKGop3uj6kfi71fSpVsqKkhf8vc1TiQRyoeHEiwjKdg1i3Dsz_LXLHcD5q-qR77utIPUbkLyWU7Xzn7ehl3Z1IWUQZjy0LndXLEcDA1PRZj4ufO8QGR0GCmEDGqoWQ6paFwo8pn0VbUH8RWjlRzLU)
_Azure blob change tier_

5. Hit **Save**.

Additionally, the Archive storage tier is the most affordable one in Azure, meaning that you can reduce your database data TCO with it.

### Secondary Database and Table Management

There exist several workflows that can help you set up Azure database backup archiving for your organization. When you need the data to stay in the initial database, for instance, creating a separate table and moving that data there can be your choice. However, the filegroup of that table should stay apart from the main database and be moved to a separate disk whenever possible. 

Most probably, you’ll want to let users access the data you send to a separate table. To make that happen, you can create a view merging the relevant tables and redirect the requests to that view, not to the original table. Doing things that way, you can keep the data accessible while dealing with maintenance faster.

### SQL Server Linking

If you can’t move the data to another database for internal reasons such as special Azure backup policies, you can consider maintaining your primary database accordingly. 

Here, the outcome is likely to be that of the previous case, but you need to link the SQL servers or configure apps so they can send direct requests to your second server. 

The downside here is that your SQL database, which was supposed to be a backup one, becomes a production database and gains appropriate importance for an organization.

There are two ways to create linked servers via SQL Server Management Studio (SSMS): 

* **sp_addlinkedserver** (Transact-SQL) system stored procedure that creates a linked server
* **SSMS GUI**

After you've ensured that you have appropriate access rights on both server instances you need to link, the network is configured appropriately to access them, and SSMS is installed, you'll need to go through the following steps:

First, open SSMS.

![Image](https://lh7-us.googleusercontent.com/6NS8wE2UmtV5Bs3-loE7kIASfehk4-hSaPP5y7Wm1oEVIUFDCPyxD_f1rLQzxsJVdCGaFJwcRHqKVrnypgETOSohLP5hQK50m4tj4pBZBIx6oTUj8WOJbcttfhy0IybUyC_CrJCyK8saEPnchKInp7g)
_Microsoft SSMS_

Connect to the instance where you need to establish a linked server. Then find **Object Explorer > Server Objects**, then right-click **Linked Servers**.

Pick **New Linked Server** from the dropdown:

![Image](https://lh7-us.googleusercontent.com/tD5YO2e1RtfLUmtBdRFNfiHQSyaxnQml9lBGnRPPzuNrW4Fcu-3alTg4N3-mdR-oQxcaUyMpyqp36l7r3aTfg29RzT6Jgx0Nb1eT2T-y-zotl1RujRUIC4gSwE25aslpfMJJUvNW4MMivP4BstyQu4o)
_New linked server SSMS_

Then configure the server properties, including name, server type, provider and product name:

![Image](https://lh7-us.googleusercontent.com/y-WSzJni8uyKBAcJywPqk-iufIeJ_4TTs1rf3e_9RYhj1Kt8nUsZfad9Vekec4yL6eFCX8doLR4Qr7iA6X3p78jnRfIs3AYlHMn1GOhR8Ya29CW5X9DIU-nbj_jDaTwAvwEJXNjr7npd5THmnD7Iv3A)
_Linked server configuration SSMS_

Then you'll just need to complete the security configuration, set up the server options, and complete connection testing.

### Original Data Deletion

When you don’t need 24/7 data availability but need the data stored due to internal policies or compliance requirements, you can choose what's probably the simplest solution to increase storage space efficiency. Just back up the data that can stay unavailable and then delete the originals from the main database. Accessing any records you may need will still be possible via the backup.

### Stretch Database

Aiming to make data management of organizations’ databases simpler, Microsoft implemented a Stretch Database feature in SQL Server 2016. With this feature, you can get an SQL backup to Azure after you send the data from the hosted database to an Azure SQL database. The method enables you to increase overall infrastructure cost-efficiency by simplifying backup workflows.

To enable this workflow in your environment, develop the policy specifying the data on a hosted server to send to Azure. You don’t need to introduce any changes in applications that use the production database: SQL Server can independently get the records from the Azure SQL Database.

### Azure Database Backups Verification and Restoration

During an SQL Azure database backup, you can choose to create such backups **WITH CHECKSUMS** or without them. When the workflow is complete, I recommend you use the following command: **`RESTORE VERIFYONLY`**. This command enables you to check the recoverability of backup files.  

To access the data, you can restore records from a backup to a different database. With Azure Automation scripts on backups, you can accelerate the restoration process, thus minimizing downtime and increasing the overall resilience of your Azure infrastructure. 

You need to follow only a few steps to restore an Azure SQL database to a required recovery point from a backup. Still, keep in mind that your subscription can define the available retention period which can vary from 7 to 35 days. A native tool for backup restoration to SQL servers is Server Management Studio.

## To Conclude

The critical nature of Azure SQL database data makes Azure SQL backups obligatory for any organization that uses this Microsoft solution. In this guide, we reviewed the process of creating SQL Azure database backup using native Microsoft tools. 

These tools provide data backup, backup verification, and recovery functionality along with some automation. 

You can also implement a specialized all-in-one data protection solution, such as [NAKIVO](https://www.nakivo.com/backup-to-azure-blob/), the company where I work. It can help you make your data backup workflows more efficient.

  

