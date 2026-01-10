---
title: How to Connect Amazon EC2 Using Microsoft Remote Desktop in macOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-09T01:22:54.000Z'
originalURL: https://freecodecamp.org/news/ec2-with-microsoft-remote-desktop
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/rdp.png
tags:
- name: configuration
  slug: configuration
- name: ec2
  slug: ec2
- name: macOS
  slug: macos
- name: rdp
  slug: rdp
seo_title: null
seo_desc: 'By Clark Jason Ngo

  I created this guide because of an experience I had while teaching. My students
  needed to use an application that was only available on Windows OS but the students
  only had macOS.

  We will be touching on the technologies shown below...'
---

By Clark Jason Ngo

I created this guide because of an experience I had while teaching. My students needed to use an application that was only available on Windows OS but the students only had macOS.

We will be touching on the technologies shown below:  


![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-56.png)

* Amazon EC2: launch a Windows Server 2019
* Microsoft Remote Desktop: macOS application to remote desktop connect (RDP) to EC2

## Amazon EC2

### Launching a Windows Server EC2 Instance

1. Sign in to your [AWS Management Console](https://aws.amazon.com/console/).
2. Choose **Services**, then **EC2**.
3. In the sidebar, click **Instances**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-57.png)
_EC2 sidebar_

4. Click **Launch Instance**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-58.png)
_Launch Instance button_

5. Scroll down and choose **Microsoft Windows Server 2019 Base**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-59.png)
_Choose AMI page_

6. At the bottom of the Choose Instance Type page, click **Review and Launch**. This will skip you to the Review page.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-60.png)
_Launch with minimal configuration_

7. In the Review page, click **Launch**. You'll be prompted to select an existing key pair or new key pair. 

If you choose **Create a new key pair**, you need to give the new key pair a name, then download the key pair.  Then you'll be able to proceed to choose **Launch Instance**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-61.png)
_Key pair to access the instance_

If you choose **Choose an existing key pair**, you need to select a key pair and tick the checkbox to acknowledge the use of the key pair.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-62.png)
_Last step to launch instance_

8. Click the generated Instance ID.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-63.png)
_Accessing the EC2 Instance_

9. Find and save the following information:

* Public DNS (IP Address)
* Username
* Password

To get the IP Address, scroll to the right of your EC2 instance:  

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-70.png)
_IP Address of EC2 Instance_

You can also find this in the Description tab below:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-67.png)
_IP Address of EC2 Instance_

10. To get the username and password, choose the EC2 instance (tick the checkbox), click **Actions**, then **Get Windows Password**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-68.png)
_Obtaining the username and password_

You may encounter _Password not available_ and you'll need to wait a couple of minutes.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-71.png)
_Provisioning the auto-generated password_

11. Locate the existing key pair or the newly created key pair you have downloaded in your local machine. Click **Choose File**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-72.png)
_Retrieve the key pair_

12. After uploading the key pair, click **Decrypt Password**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-73.png)

13. Copy the following information and save it in a file or clipboard. Click **Close** when you are done.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-74.png)
_Information for remote desktop connection_

## Microsoft Remote Desktop 

### Installing the application and connecting to EC2 instance

1. Open your App Store, then search for **Microsoft Remote Desktop**. Click Install (it shows UPDATE here as I already have installed).

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-64.png)
_Microsoft Remote Desktop in the App Store_

2. After installation, Open Microsoft Remote Desktop.

3. At the top, click the **+** Icon and choose **Desktop**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-65.png)
_Creating a new desktop connection_

4. In the PC name, copy the EC2 Instance IP address, then click **Add**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-66.png)
_Adding the IP address_

5. Copy the Administrator and Password from earlier and paste it here. Hit **Continue**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-75.png)
_Signing in with the username and password_

You are now connected to your Windows Server EC2 Instance.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-76.png)
_Windows Server EC2 Instance_

Note: To avoid getting charged after you have used up the free tier for EC2, either click **Stop** to have a lower cost, or **Terminate** to remove the instance and not be charged. 

You have access to this by selecting the instance and choosing **Actions > Instance State > Stop/Terminate**.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/image-77.png)

## Here's a video tutorial:

%[https://youtu.be/QQIivlr_CKk]

Connect with me on LinkedIn [here](https://www.linkedin.com/in/clarkngo/).

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-243.png)

