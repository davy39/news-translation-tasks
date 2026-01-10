---
title: How to Set Up Grafana on EC2
subtitle: ''
author: Onwubiko Emmanuel
co_authors: []
series: null
date: '2024-08-02T13:42:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-grafana-on-ec2
coverImage: https://www.freecodecamp.org/news/content/images/2024/08/pexels-kawserhamid-176342.jpg
tags:
- name: analytics
  slug: analytics
- name: Grafana
  slug: grafana
- name: monitoring
  slug: monitoring
seo_title: null
seo_desc: "In today's data-driven world, it's important to monitor and visualize system\
  \ metrics to make sure everything works consistently and performs well. \nGrafana\
  \ is an open-source analytics and monitoring platform. It has gained widespread\
  \ recognition amon..."
---

In today's data-driven world, it's important to monitor and visualize system metrics to make sure everything works consistently and performs well. 

Grafana is an open-source analytics and monitoring platform. It has gained widespread recognition among developers and enterprises looking to extract more insights from the data produced by their systems. 

Grafana has many powerful visualization features, and when combined with Amazon EC2's scalability and flexibility, it creates a stable environment for efficient monitoring. 

This article will walk you through setting up Grafana on Amazon EC2 and creating informative dashboards out of raw data. 

## **For Whom is this Intended?**

This tutorial is intended for both novices to the cloud and experts in DevOps. The goal of this post is to make the installation process easier so you can use Grafana on AWS to its fullest. Now let's get going.

## **How to Configure Your EC2 Instance**

You need to configure the inbound rule for your EC2 instance to access port 3000, as Grafana operates on this port. But first, you need to establish an EC2 instance. You can follow this guide on how to set up your [AWS EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) instance. It takes less than 5 minutes.

Once you have created your EC2 instance, you'll need to configure the network inbound rules. So head to your instance page and click on it. On the button widget, click on the **security** tab and click on the security group link (it should look like this: “**sg-547**********************”). 

Once you open the page in the inbound rules section, click on ‘**Edit inbound rules**’. Click on Add a new rule and add **3000** to the port range field, and on the source field, select **0.0.0.0/0.** Then save.

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721347239653_image.png)
_Inbound rules_

## **How to Create an IAM Role**

Now you need to construct an **IAM (Identity Access Management)** role. You're developing an identity role so that you can generate credentials that you'll subsequently use to log in to your Grafana service.

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721348061199_IAM+Dashboard.png)
_IAM Dashboard_

So, in the search field, type "**IAM service**" and click it. Click '**Create role**', and select the AWS service as the trusted entity type.

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721348079999_IAM+Role+creation.png)
_IAM Trusted Entity_

On the use case section, select EC2, then click next.

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721348098668_EC2+Use+Case.png)
_IAM role use case_

On the Add Permissions page, click on the **AdministratorAccess** policy, then click next. Enter a role name – in this case, I used **Grafana-Server-Role.**

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721348120427_IAM+role+modify+.png)
_Role creation_

## How to Download Grafana

Now that you've configured your EC2 inbound rule and also configured the IAM role, let's set up Grafana on your EC2 instance. 

So head over to [Grafana's download page](https://grafana.com/grafana/download). Since we'll be downloading the version for Amazon Linux in this tutorial, you need to type in the following command on your Linux command line. Note: You need to connect to your VM instance through SSH (Secure Shell). In this case, I am using the EC2 Instance Connect.

```bash
sudo yum install -y https://dl.grafana.com/enterprise/release/grafana-enterprise-11.1.0-1.x86_64.rpm
```

Now you'll enable the Grafana service on your terminal by typing the following command:

```bash
systemctl enable grafana-server.service
```

Then start the service:

```bash
systemctl start grafana-server.service
```

Check the status of the Grafana service on the EC2 instance by running this command:

```bash
systemctl status grafana-server.service
```

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721411484886_Grafana+Active+.png)
_Grafana Service Status_

Now that you've confirmed that the service is currently active, you'll also need to check if the Grafana service is active on **port 3000**, as you've already created an inbound rule to cater for this. 

You can do this by typing the following command:

```bash
netstat -tunpl | grep grafana
```

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721411578753_3000+active.png)
_Port 3000 confirmation_

Now that you've confirmed that the service runs on port 3000, you can go ahead and set up your Grafana dashboard.

You can access the Grafana dashboard by typing the Public IP of your EC2 instance and adding port 3000 on your web browser, something like this: **34.239.101.172:3000**.

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721411871355_Grafana.png)
_Grafana Login_

The default username and password for Grafana are admin, but you'll be given the option to change your password after you sign in with the default credentials. You can also skip the password change process if you like.

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721412805910_Grafana+Password.png)
_Change password on Grafana_

After this step, go to the home page. The next thing to do is to start connecting your Grafana dashboard to a data source. In this case, you're going to connect it to the AWS cloud watch service.

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721413426627_Grafana+home.png)
_Grafana_

## **How to Connect Data Sources to the Grafana Dashboard**

Click on the connections tab on the side menu and click on data sources. Search for the CloudWatch service.

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721413905866_image.png)
_Cloudwatch configuration_

Now you'll be prompted to input your access key ID and secret access key. You will need to create this on your AWS IAM service. 

So go back to your IAM management dashboard and go to the user's tab. If you haven’t created an IAM user, you can do so by checking out this [IAM user creation tutorial](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html). 

In the user IAM dashboard, scroll down to the access keys section and click on **Create access key.**

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721414737862_Access+Key.png)
_Access key_

Select the Command Line Interface use case.

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721414696820_Access+Key+2.png)
_Access key use case_

Set the description tag. This step is optional. Then click on the **Create access key.**

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721414844084_Access+Key+3.png)
_Access keys_

Now copy the Access Key ID and Secret access key and paste them into the CloudWatch Datasource configuration page on Grafana. Set your default cloud region – in this case, mine is **us-east-1**

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721414955923_image.png)
_Additional settings_

When you’re done, click on the save and test buttons. Grafana will query the Cloudwatch logs, and if it works fine it will save the configuration.

## **How to Create a Dashboard on Grafana**

Now that you have successfully configured your grafana service, let’s start creating dashboards.

Click on the dashboard tab on the side menu click on **New** and select new dashboard. You should see the screen below:

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721416576260_dashboard.png)
_Create a new dashboard_

Then select **Import dashboard.**

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721417832804_image.png)
_Import a dashboard_

For this case, you'll be importing an already-made dashboard from Grafana. Grafana has a lot of dashboards for a lot of use cases and services. But in this case, you'll be importing an EC2 dashboard ([Grafana EC2 dashboard](https://grafana.com/grafana/dashboards/11265-amazon-ec2/)). 

If you want to import it, you can easily copy the ID of the dashboard that you want to import. It is always accompanied by the dashboard.

So now copy the ID – in this case, it's **11265**. Then paste it into the import field on the import dashboard, and click on the load button.

![Image](https://paper-attachments.dropboxusercontent.com/s_4B51535633ABB1D019D79F3934180D191EF4BB549B6DD5EF46643EA16E05EAAE_1721418236847_Grafana+Dashboard.png)
_Grafana Dashboard_

Now you have successfully created a dashboard in Grafana. This dashboard lets you monitor the performance of your EC2 instance. You can monitor metrics such as CPU Utilization, CPU Credit, Disk Ops, Disk Bytes, Network, Network Packets, Status check, and so on.

## Wrapping Up

Thank you for reading! I hope this step by step guide has helped you learn how to create and set up efficient dashboards using Grafana. 

