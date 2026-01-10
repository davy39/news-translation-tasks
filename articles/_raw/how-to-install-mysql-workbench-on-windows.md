---
title: How to Install MySQL and MySQL Workbench on Windows
subtitle: ''
author: Md. Fahim Bin Amin
co_authors: []
series: null
date: '2023-06-30T18:23:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-mysql-workbench-on-windows
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/boitumelo-phetla-0DJHJcpwN9Q-unsplash.jpg
tags:
- name: database
  slug: database
- name: MySQL
  slug: mysql
- name: Windows
  slug: windows
seo_title: null
seo_desc: 'If you want to learn MySQL, starting with a good client is super helpful
  – especially when you are just beginning your journey.

  There are a lot of clients out there for your MySQL-based needs, like XAMPP, DataGrip,
  and others. Among all of them, I pr...'
---

If you want to learn MySQL, starting with a good client is super helpful – especially when you are just beginning your journey.

There are a lot of clients out there for your MySQL-based needs, like XAMPP, DataGrip, and others. Among all of them, I prefer the [MySQL Workbench](https://www.mysql.com/products/workbench/). It is completely free, by the way.

In this tutorial, I will show you how you can install and configure your Windows machine for this MySQL and MySQL workbench from scratch. 

If you enjoy learning from videos as well, then don't worry as I have also created a step-by-step video just for you:

%[https://www.youtube.com/watch?v=kZf_h-Phfds]

## How to Install MySQL Workbench 

#### ➡️ Download MySQL Workbench

Make sure to visit only the [official website](https://www.mysql.com/products/workbench/) for downloading the MySQL Workbench. You do not want to get into shoddy websites and download the wrong file that infects your favorite machine, right?

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-32.png)
_Find the official website for MySQL Workbench: https://www.mysql.com/products/workbench/_

Now click on the "DOWNLOADS" tab.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-32_1.png)

Scroll down until you find `MySQL Community (GPL) Downloads »`.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-32_2.png)

Click on `MySQL Community (GPL) Downloads »`. After that, on the new page, click "MySQL installer for Windows".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-32_3.png)

From the dropdown menu, select your operating system as "Microsoft Windows". Then download the file which is larger in size.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-33.png)

A `.msi` file will be downloaded. That is our installer file to install MySQL and MySQL workbench.

#### ➡️ Install both MySQL and MySQL Workbench 

Simply double click on the installer file. It will reload the necessary components and open the installer GUI selection window. Choose the setup type as custom and click "Next".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-34_1.png)
_Select Custom_

A new page will appear. Make sure to select the latest "MySQL Server", "MySQL Workbench" and "MySQL Shell". Selecting and clicking on the right side arrow will take the product name in the "Products to be installed section". Then click "Next".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-34-1.png)
_Install necessary components_

Click "Execute" to install the three necessary components. The process might take some time depending on your internet speed and computer configuration. After it gets finished, simply click "Next".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-35.png)
_Execute_

In the Product Configuration window, simply click "Next". It will install the three selected components for us.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-37.png)
_Next_

Keep everything as it is and simply click "Next". It will configure the MySQL Server.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-37_1.png)
_Next_

Keep everything as it is and simply click "Next". It will apply the TCP/IP connectivity for our MySQL server.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-37_2.png)
_Next_

Now give it a Root password. For testing purposes, I am using a very simple "1111" as my password, but I would recommend not doing the same. Also, make sure to remember the password as you will need it when you want to work in MySQL Workbench. Click "Next".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-37_3.png)
_Next_

Keep everything as it is, and simply click "Next". It will make sure to setup our root password for the MySQL workbench.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-38.png)
_Root password_

We want to run the service as a Standard System Account for our operating system. Therefore, keep everything as it is, and simply click "Next".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-38_1.png)
_Next_

Select the option to grant full access to the user running the Windows Service and then click "Next."

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-38_2.png)
_Next_

Then click "Execute". This will grant the full access to the user running the Windows service and the administrator group only, but the other users and groups will not have its access. 

So if you have multiple user accounts in your computer, then they will not be able to access the MySQL server/Workbench. If you want then you can change the settings here based on your need.

As I have only one user account in my Windows machine, I can safely keep the first option selected.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-38_3.png)
_Execute_

It might take some time. Then when you will receive a green check box in all configuration steps, simply click "Finish".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-38_4.png)
_Finish_

The configuration has beep applied successfully. Simply click "Next".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-39.png)
_Next_

Click "Finish" to complete the installation.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-39_1.png)
_Finish_

It will open the MySQL Workbench and MySQL Shell. Simply close all of them now.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-39_1-L.png)

## ➡️ Configuration

Now we need to configure the path variables for our operating system. Go to the drive where you have installed your Windows operating system. Like others, I have also installed my operating system on the "C" drive. 

Therefore, I am going to the "C" drive and opening the "Program Files" directory.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-40.png)

Go to the "MySQL" folder.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-40_1.png)

Then go to the MySQL Server folder.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-40_2.png)

Go to the "bin" folder.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-40_3.png)

Copy the path/address. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-40_4.png)

Now open the Environment Variables settings. Simply click on the Windows button and type "env". 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-40_5.png)

Click "Environment Variables".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-41.png)

Select the "Path" and click "Edit".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-41_1.png)

Click "New". A new blank box will appear. Paste the path/address that you copied earlier. Do not close the window now as we need to do the same thing for the MySQL Shell folder.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-41_2.png)

Now, we need to do the same thing for the MySQL Shell also. Open the MySQL Shell folder now.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-41_3.png)

Go to the "bin" folder.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-41_4.png)

Copy the path/directory.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-42.png)

Now apply the same process as you did earlier. Click "New" on the Edit environment variable window. Paste the path/directory in the new blank box.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-42_1.png)

Now click "OK".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-42_2.png)

Click "OK" again.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-42_3.png)

And click "OK" one more time.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-42_4.png)

## ➡️ Finishing Up

Our task is now finished. You can now open the MySQL Workbench.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-43.png)

Simply click on the Local instance. It will ask for the root password. Enter the password. If you do not want to go into the same hassle of entering a password every time, check the box on save password in the vault. Click "OK".

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-43_1.png)

This is your default MySQL Workbench workspace.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-43_2.png)
_Workbench workspace_

If you want then you can also hide the SQL Additions tab by clicking on the colored box.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-43_3.png)

For getting the Schemas, click on the "Schemas" tab from the navigator.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-43_4.png)

Your MySQL Workbench is also ready for any kind of development process. You can also use MySQL from your terminal as well.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_10-43_5.png)

![Image](https://www.freecodecamp.org/news/content/images/2023/06/2023-06-28_11-32.png)

## Conclusion

Thank you for reading the entire article.

If you have any questions, feel free to reach out to me using [Twitter](https://twitter.com/Fahim_FBA) or [LinkedIn](https://www.linkedin.com/in/fahimfba/).

Also, make sure to follow me on [GitHub](https://github.com/FahimFBA)!

You can also [subscribe to my YouTube channel](https://www.youtube.com/@FahimAmin?sub_confirmation=1) for more helpful video content.

If you are interested then you can also check my website: [https://fahimbinamin.com/](https://fahimbinamin.com/)

Have a great day! 😊

Cover: Photo by [Boitumelo Phetla](https://unsplash.com/@writecodenow?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/0DJHJcpwN9Q?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

