---
title: How to deploy a Blazor application on Azure
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-23T19:48:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-blazor-application-on-azure-cf6f3b1f03a0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q_9GcuoDUbWGTSFjdIkduA.jpeg
tags:
- name: Azure
  slug: azure
- name: General Programming
  slug: programming
- name: SQL
  slug: sql
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we will learn how to deploy an ASP.NET Core hosted Blazor application
  on Azure. We will use Visual Studio 2017 to publish the app. We will create a SQL
  database server on Azure to handle DB operations.

  Pr...'
---

By Ankit Sharma

### Introduction

In this article, we will learn how to deploy an ASP.NET Core hosted Blazor application on Azure. We will use Visual Studio 2017 to publish the app. We will create a SQL database server on Azure to handle DB operations.

### Prerequisites

* Install the .NET Core 2.1 or above SDK from [here](https://www.microsoft.com/net/learn/dotnet/hello-world-tutorial#windowscmd)
* Install Visual Studio 2017 v15.7 or above from [here](https://visualstudio.microsoft.com/downloads/)
* Install ASP.NET Core Blazor Language Services extension from [here](https://marketplace.visualstudio.com/items?itemName=aspnet.blazor)
* An Azure subscription account. You can create a free Azure account [here](https://azure.microsoft.com/en-in/free/)

Please refer to my previous article [Cascading DropDownList in Blazor Using EF Core](https://ankitsharmablogs.com/cascading-dropdownlist-in-blazor-using-ef-core/) to create the application that we will be deploying in this tutorial.

### Create a resource group on Azure portal

We will create a resource group on Azure portal to contain all our resources on Azure.

Login to Azure portal and click on `Resource groups` on the left menu and then click Add. It will open a “Resource group” window as shown in the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/20T1IWmzWvOLuzHR1enxqFy0-7bq2BtIKbUf)

In this window we need to fill the following details:

* **Resource group name**: Give a unique name to your resource group. Here we will use the name `BlazorDDLGroup`.
* **Subscription**: Select your subscription type from the drop down. Here we are selecting the “free trial” subscription.
* **Resource group location**: Select a location for your resource group from the drop down.

### Creating SQL DB and DB server on Azure

We will create the SQL database and a database server on the Azure portal to handle our DB operations.

Click on `SQL databases` on the left menu of your Azure portal and then click Add. It will open a “SQL Database” window as shown in the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/38Z5Qh737F4cvXYy5tmwFw1hIbOozmawjBUX)

Here you need to fill in the following details:

* **Database name**: Put in a name for your database. Here we will use `DDLDemodb` as our DB name.
* **Subscription**: Select your subscription type from the drop down. Here we are selecting the “free trial” subscription.
* **Resource group**: Select the resource group name that we have created in the previous step.
* **Select source**: This drop down contains a list of databases with predefined data provided by Azure. Since we are creating our custom database, select `Blank database` from this dropdown.
* **Pricing tier**: Select a pricing tier for your database.

Before creating the database, we need to create a database server for the SQL database. Click on the “Server configure required settings” and then click `Create a new server`. It will open a “New server” window as shown in the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/r6hMMqOkb0djwPQN42D3UI5nznTp72qdhhou)

Here we need to furnish the following details:

* **Server name**: Provide a name for your DB server. Here we will use `ddldemoserver`. The DB server will be created by appending `.database.windows.net` to the user provided server name. Hence, the server name will be `ddldbserver.database.windows.net` in this case.
* **Server admin login**: Put an admin login name for your DB server.
* **Password**: Put the login password corresponding to the admin login for your DB server.
* **Location**: Select a location for your server from the dropdown.

Check the “Allow Azure services to access server” check box and click on `Select` to create your DB Server.

**Note:** The word “admin” is restricted for the administrator user name of the database server. Use any other username than “admin”.

Once the DB server gets created, you will be redirected back to the “SQL Database” window. You need to click on the “Create” button to create your database.

Here is the whole process explained in a gif.

![Image](https://cdn-media-1.freecodecamp.org/images/6D4EPQq3NvDVgHHYLyldCYjHAf-rv2aRYlWH)

### Creating DB tables

The database `DDLDemodb` do not contain the tables that we are using in our application. We will connect to Azure database using SQL Server Management Studio (SSMS) to create our DB objects.

Open SSMS in your machine and put the server name as `ddldbserver.database.windows.net`. Provide the admin user id and password that you have configured in the previous section. Then click on “Connect”.

You will get a pop up window for configuring the firewall rule to access the Azure DB. Login with your Azure account credentials and add your machine’s IP address under `Firewall rule`. Click on OK to connect to the Azure database server. Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/3EZsH1Q0JygMDppF3q9vfDrDo4P4FL9sfOiC)

Once the connection is successful, you can see the `DDLDemodb` database on the server. Refer to my previous article [Cascading DropDownList in Blazor Using EF Core](https://ankitsharmablogs.com/cascading-dropdownlist-in-blazor-using-ef-core/). Run the SQL commands to create and insert sample data in the Country and Cities tables that we are using in our application.

### Setting the DB connection string

After creating the database objects, we need to replace the connection string of local database in our application with the connection string of the Azure database.

Open Azure portal and click on `SQL databases` on the left menu. It will open a window displaying the list of all the databases that you created on the Azure portal. Click on `DDLDemodb` database and select `Connection strings` from the menu. Select the `ADO.NET` tab and copy the connection string. Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/TyolX9Lz7LWJaCjPWslSDToB1sxtKguXBfNp)

You need to put the admin user id and password for the database server that you have configured earlier in this connection string.

Open the `BlazorDDL` application using Visual Studio, navigate to `BlazorDDL.Shared/Models/myTestDBContext.cs` and replace the local connection sting with this new connection string.

Launch your application from Visual Studio to verify if the new connection string is configured correctly and you are able to access the Azure database.

If the application is not working and you are unable to connect to the database, then check if your connection string is correct or not. Once the application is working as expected in your local machine then move to the next section to publish it on Azure.

### Publishing the Blazor application to Azure

To publish the Blazor app on Azure, Right-click on the Server project of your solution and click publish. In this case, it will be `BlazorDDL.Server >> P`ublish.

It will open the `Pick a publish target` window. Select `App Service` from the left menu. Select the `Create New` radio button and click on the “Create profile” button. Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/gUBsJCxOAcKBI4MT3gklIr4NAgVeF2UhYCB6)

The next window will ask you to login to your Azure account if you are not logged in. Once the login is successful, a `Create App Service` window will open. Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/XhCbINl98SIiBYISo1rWwho10j6RcQSi2VtM)

The fields of this window have default values in them as per the configuration of your Azure account. However, you can change these values depending on your requirements.

You can fill the details as mentioned below:

* **App Name**: Provide an app name for your application. The app name is subject to availability. If the app name you provided is already in use, then you need to give a new app name. The website’s public URL will be App Name followed by `.azurewebsites.net`. Here we are using the name `BlazorDDLDemo`, hence the URL for our website will be `BlazorDDLDemo.azurewebsites.net`.
* **Subscription**: Select your subscription type from the drop down list.
* **Resource Group**: Select your resource group name, which is `BlazorDDLGroup` in this case.
* **Hosting Plan**: You can either use the existing plan or select a new plan by clicking on the “New…” link.
* **Application Insights**: You can choose a value from the dropdown list. It will provide analytics for your website.

Click on the “Create” button to start the application deployment on Azure. It will take few minutes to complete depending on your internet connection speed.

After the deployment is successful, click on the “Publish” button to publish the app to Azure. Once the application is published successfully, the website will be launched automatically in the default browser of your machine. You can also access the website using the URL `BlazorDDLDemo.azurewebsites.net`.

You can see the application in your browser as shown in the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/awDc-mIvjrILWDsq7X4lhTMlA9iAAH9UcJKd)

### Conclusion

In this article, we learned how to deploy and publish a Blazor application on Azure. We created a SQL database and DB server on Azure and used them in our application to handle the DB operations.

Get my book [Blazor Quick Start Guide](https://www.amazon.com/Blazor-Quick-Start-Guide-applications/dp/178934414X/ref=sr_1_1?ie=UTF8&qid=1542438251&sr=8-1&keywords=Blazor-Quick-Start-Guide) to learn more about Blazor.

You can also read my other articles [here](https://ankitsharmablogs.com/).

### See Also

* [Deploying A Blazor Application On IIS](https://ankitsharmablogs.com/deploying-a-blazor-application-on-iis/)
* [Blazor — CRUD Using MongoDB](https://ankitsharmablogs.com/crud-using-blazor-with-mongodb/)
* [JavaScript Interop In Blazor](https://ankitsharmablogs.com/javascript-interop-in-blazor/)
* [Understanding Server-Side Blazor](https://ankitsharmablogs.com/understanding-server-side-blazor/)
* [Single Page Application Using Server-Side Blazor](https://ankitsharmablogs.com/single-page-application-using-server-side-blazor/)
* [ASP.NET Core — CRUD Using Blazor And Entity Framework Core](https://ankitsharmablogs.com/asp-net-core-crud-using-blazor-and-entity-framework-core/)

Originally published at [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)

