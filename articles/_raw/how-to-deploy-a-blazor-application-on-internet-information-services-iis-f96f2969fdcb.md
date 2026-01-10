---
title: How to deploy a Blazor Application on Internet Information Services (IIS)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-14T15:12:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-blazor-application-on-internet-information-services-iis-f96f2969fdcb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qZqIAFSLGBjADpNTsnu9Pw.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: Blazor
  slug: blazor
- name: Microsoft
  slug: microsoft
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we will learn how to deploy an ASP.NET Core hosted Blazor application
  with the help of IIS 10 on a Windows 10 machine. We will be using Visual Studio
  2017 to publish the app and SQL Server 2014 to handle ...'
---

By Ankit Sharma

### Introduction

In this article, we will learn how to deploy an ASP.NET Core hosted Blazor application with the help of IIS 10 on a Windows 10 machine. We will be using Visual Studio 2017 to publish the app and SQL Server 2014 to handle DB operations. We will also troubleshoot some of the common hosting issues for a Blazor application.

### Prerequisites

* Install IIS in your machine
* Install URL Rewrite module from [here](https://www.iis.net/downloads/microsoft/url-rewrite)

Please refer to my previous article, [How to create a cascading DropDownList in Blazor using EF Core](https://medium.freecodecamp.org/how-to-create-a-cascading-dropdownlist-in-blazor-using-ef-core-d230bb5bff5f), to create the application that we will be deploying in this tutorial.

### **Installing .NET Core hosting bundle**

Since we are going to deploy an ASP.NET Core hosted Blazor application, the first step is to install the .NET Core hosting bundle in our machine.

Follow the below steps to download the .NET Core hosting bundle:

#### **Step 1**

Open [https://www.microsoft.com/net/download/all](https://www.microsoft.com/net/download/all)

#### **Step 2**

Select the latest non-preview .NET Core runtime from the list. For this tutorial, we will select .NET Core Runtime 2.0.7.

Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/yP2moxch5u2x6B6mUdKoT4PRFIKtScQSZgqp)

#### **Step 3**

On the .NET Core runtime download page, scroll down to Windows section, select the “Hosting Bundle Installer” link to download the “.NET Core Hosting Bundle”_._ Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/blMT51CVhgidICtzTNRUxy3XfyyHMysiXuSN)

Once the download is finished, double-click to start installing it. You will see a window similar to the one shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/jWrEFc9edDlLk9VwB8yRaXKDUiSUQHPRQj-7)

#### **Important Note**

1. The .NET Core hosting bundle should be installed only after installing IIS. If you the bundle before installing IIS then you need to repair the bundle after installing IIS so that it will update its dependencies for IIS.
2. Restart the machine after installing the .NET Core hosting bundle.

### Publishing the Blazor application

Once the .NET Core hosting bundle installation is successful and you have restarted your machine, open the Blazor application solution using VS 2017.

Right click on the Server project of your solution and click publish. In this case it will be BlazorDDL.Server >> Publish.

![Image](https://cdn-media-1.freecodecamp.org/images/9SX4ook9WusBea8tm8oajC4uxAsxZJ5cGcye)

You will see a screen similar to what’s shown below. Select Folder from the left menu and provide a folder path. You can provide any folder path where you want to publish your app.

![Image](https://cdn-media-1.freecodecamp.org/images/p7U2FgDb0YjAqkvO-obPuDhbqfrSOf1VrDlT)

Click on publish. Visual Studio will start publishing your application. If there are no build errors, then your application will be published successfully to the folder you have mentioned.

After the publishing is successful, we will move on to configure IIS.

### Configuring IIS

Open IIS and right click on Sites >> Add Web Site.

An “Add Website” pop up box will open. Here we need to furnish details in three fields

1. Site name: Put any name of your choice. Here I will put “ankitsite”.
2. Physical Path: The path to the folder where you have published your application.
3. Host name: This is the name we put in browser to access our application. We will put **ankitsite.com** for this demo.

Click on OK to create the website. Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/gYvAyWLMlngmRpVgIDgAW0j7ZOcZHtVEDGyR)

The next step is to configure the “Application Pool” for our site. The application pool name will be same as the “Site name” we provided in the last step. Therefore, in this case the application pool name will be “ankitsite”.

Click to “Application Pools” from the left panel and double click on the pool “ankitsite”. It will open an “edit application pool” window. Select “No Managed Code” from the .NET CLR version dropdown. Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/6Vzduhtg1YwMvYQUBDZuX6VSaHiSWhwa7Ako)

Here is the whole process of configuring IIS explained in a gif image.

![Image](https://cdn-media-1.freecodecamp.org/images/dNoMZnLndfBk7e1Elct13SB0ovTqhMUb136h)

### Configuring the DNS host

The last step is to configure our DNS host file.

Navigate to the **C:\Windows\System32\drivers\etc** path in your machine and open the “hosts” file using any text editor.

![Image](https://cdn-media-1.freecodecamp.org/images/R9jJHC5-mkBuAYjO0Lk17QlzeFxSVyFNFBiQ)

We need to add the hostname that we provided in IIS against the localhost IP address. Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/U1dOrUOXwAcK6EhDnbSOJJja7ex9n7QBrTL-)

And now we have successfully hosted a Blazor application on IIS.

### Execution Demo

Open any browser on your machine and enter the hostname you have configured. You can see that the application will open in the browser window.

![Image](https://cdn-media-1.freecodecamp.org/images/Vcb7-n8EFzMdE9H9MWDQZU8-seObr43fOGPs)

### Troubleshooting common hosting issues

In this section, we will look into some of the common problems that you can face while hosting a Blazor application.

1. You are unable to open the website and get a DNS not found error

Check if the hostname is configured correctly in the host file. Make sure that your machine is not connected to any VPN server. Also, if you are using any Web proxy, then disable it.

2. HTTP Error 500.19 — Internal Server Error — The requested page cannot be accessed because the related configuration data for the page is invalid.

This error message is clear. The publish folder is inaccessible because of insufficient permissions. Grant Read permission to the IIS_IUSRS group on the publish folder so that it can access the Web.config file.

3. The website is loading but data is not getting populated, and you get a 500 Internal server error

Make sure that your connection string is in the correct format. The user id that you have specified in your connection string should have db_datareader and db_datawriter permissions. If the issue persists, then provide the user with db_owner permission.

4. The data is not getting populated and you get an “operation not allowed” exception.

This issue generally appears when you try to do a PUT, POST or DELETE operation in your web API. To mitigate this issue we need to alter the IIS setup configuration.

Navigate to Control Panel >> Turn Windows feature on or off. Then navigate to Internet Information Services >> World Wide Web Services >> Common HTTP Features and uncheck the “WebDAV Publishing” option and click ok. Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/YA0t4fAfl53A7-LJfqT2ovgkXX1FQmH9PqpL)

5. “Failed to load <web API> : No ‘Access-Control-Allow-Origin’ header is present on the requested resource.

The cause of this error is that the client and the server of the application are not on the same port. The browser will restrict the application to make web API calls due to same-origin policy. To resolve this issue, you need to enable Cross-Origin Requests (CORS) in your application. Please refer to the Microsoft documents on [Enable Cross-Origin Requests (CORS) in ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/security/cors?view=aspnetcore-2.1).

When you republish the application, do not forget to refresh your website as well as the application pool in IIS.

### Conclusion

In this article, we learned how to deploy a Blazor application on IIS on a Windows machine. We also learned how to resolve some of the common hosting issues while deploying a Blazor application.

Get my book [Blazor Quick Start Guide](https://www.amazon.com/Blazor-Quick-Start-Guide-applications/dp/178934414X/ref=sr_1_1?ie=UTF8&qid=1542438251&sr=8-1&keywords=Blazor-Quick-Start-Guide) to learn more about Blazor.

You can check out my other articles on Blazor [here](http://ankitsharmablogs.com/category/blazor/).

You can also find this article at [C# Corner](https://www.c-sharpcorner.com/article/deploying-a-blazor-application-on-iis/).

### See Also

* [ASP.NET Core — Getting Started With Blazor](http://ankitsharmablogs.com/asp-net-core-getting-started-with-blazor/)
* [ASP.NET Core — CRUD Using Blazor And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-blazor-and-entity-framework-core/)
* [ASP.NET Core — CRUD Using Angular 5 And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-angular-5-and-entity-framework-core/)
* [ASP.NET Core — CRUD With React.js And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-with-react-js-and-entity-framework-core/)
* [ASP.NET Core — Using Highcharts With Angular 5](http://ankitsharmablogs.com/asp-net-core-using-highcharts-with-angular-5/)

Originally published at [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)

