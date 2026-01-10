---
title: How to Make an Awesome Inventory Management Application in PHP and MySQL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-05T02:35:39.000Z'
originalURL: https://freecodecamp.org/news/making-an-awesome-inventory-management-application-in-php-and-mysql-from-start-to-finish-90bc5996680a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*D8DAUz3T2nustjr2Pnn6QQ.jpeg
tags:
- name: business
  slug: business
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Richard

  You do not need bloated enterprise software to effectively track your inventory.
  This tutorial will help you develop your own custom inventory tracking application
  so you can make smart inventory decisions based on timely and accurate inve...'
---

By Richard

You do not need bloated enterprise software to effectively track your inventory. This tutorial will help you develop your own custom inventory tracking application so you can make smart inventory decisions based on timely and accurate inventory data.

### System Requirements

Our Inventory System requires the standard commercial phpGrid and phpChart license. It needs a few advanced features from both components.

* PHP 5.6+(**PHP 7.x is now highly recommended!**)
* MySQL / MariaDB
* phpGrid Lite (subgrid) -or- phpGrid Enterprise (Master detail, Grouping)
* phpChart (for reports)

### What is in an Inventory Management System

An inventory management system has several critical components. At its core, inventory control works by tracking the two main functions of a warehouse: receiving (incoming) and shipping (outgoing). Other activities such as the movement or relocation of inventory also take place. Raw materials are decremented and finished goods are incremented.

* Incoming shipments
* Outgoing orders
* Inventory
* Suppliers
* [Barcode scanner](https://medium.com/@chensformers/inventory-management-system-with-barcode-scanner-in-php-a-definitive-guide-d18fdc165511) (1/2019 New!)

### Inventory System Database Design

Typically, an inventory system has four basic elements: products, purchases, orders, and suppliers. Each element must be tracked based on its location, SKU, and quantity. Current inventory, or products on hand, is updated by tracking incoming shipments and outgoing orders. Order alerts can be set to trigger when inventory levels fall below custom-defined minimum levels.

![Image](https://cdn-media-1.freecodecamp.org/images/ZH5FJWHyUxVNeNFNMqOKPwde7lqBS5Lwvtkp)

### Setting up the Inventory Manager Database

Download the `**InventoryManager.sql**` SQL script from this tutorial’s [GitHub repo](https://github.com/phpcontrols/inventory-manager), and then execute the script using a MySQL tool such as [MySQL Workbench](https://www.mysql.com/products/workbench/). This will create a new database named `**InventoryManager**` as well as the tables needed for this tutorial.

### A Side Note on ZenBase

```
The Inventory Management System is also one of the many application templates readily available at ZenBase (built on the top of phpGrid) for anyone — with or without coding skills — to use and customize for their own needs.
```

### Set up phpGrid

Let’s move on.

We will use a datagrid component by [phpGrid](https://phpgrid.com) to handle all internal database **CRUD (Create, Remove, Update, and Delete)** operations.

Be sure to [download a copy of phpGrid](https://phpgrid.com/download/) before you proceed.

To install phpGrid, follow these steps:

1. Unzip the phpGrid download file.
2. Upload the `**phpGrid**` folder to the phpGrid folder.
3. Complete the installation by configuring the `**conf.php**` file.

Before we begin coding, we must include the following information in `**conf.php**`, the phpGrid configuration file.

### Creating the User Interface (UI)

Our inventory system comprises four pages:

* Current Inventory
* Incoming Purchases
* Orders to Ship
* Reports

![Image](https://cdn-media-1.freecodecamp.org/images/5AWVXClN4dV5xDNjuSOuNyHn2iJWDJ3Xu4PL)

### Menus

The include file for the menu is stored in an `**inc**` folder named `**menu.php**`. The code for the menu is straightforward. For the sake of focus, we will not go into great detail. Feel free to look at the code inside the `[**inc**](https://github.com/phpcontrols/inventory-manager/tree/master/inc)` folder.

We have also added a menu item named `Reports`.

![Image](https://cdn-media-1.freecodecamp.org/images/nL2WOBl0IY3-KmkHLxyWenxsQ5CmYZcKTC-k)

### Pages

We will use the same page template we used for the [CRM](https://phpgrid.com/example/build-first-simple-crm-scratch/) and [Project Management](https://phpgrid.com/example/build-project-management-application-scratch/) tutorials.

#### Current Inventory

![Image](https://cdn-media-1.freecodecamp.org/images/AVz5Mdch-aEydKuRqCNgKCUz24E7XCreeaIM)

Let’s start with the Current Inventory page.

Incoming purchases increase the inventory while outgoing orders decrease it. From a master-detail perspective, the Current Inventory has not one, but two detail datagrids — the **Purchases** (incoming purchases) and the **Orders** (outgoing orders).

So the Current Inventory page is composed of one master grid (the Current Inventory in stock) and two detail grids (Incoming Purchases and Outgoing Orders). We can easily present these relationships using the phpGrid one master and multiple detail datagrids feature.

### phpGrid Lite vs. Professional and Enterprise

> **Master detail and Grouping features require phpGrid Professional or Enterprise edition. If you are on the free Lite version, you can still use [subgrid](https://phpgrid.com/documentation/set_subgrid/) in place of Master detail albeit less advanced. Professional or Enterprise versions are highly recommended.**

If you have read the last tutorial [Building a Donation Manager from Scratch](https://medium.com/@chensformers/a-step-by-step-guide-to-building-a-donation-manager-from-scratch-in-php-part-i-514a7d34ee82), you will have no problem following the code below.

Note the use of the [set_col_format()](https://phpgrid.com/documentation/set_col_format/) function used to format the integers.

That’s it for the Current Inventory datagrid. Here’s what it looks like so far:

![Image](https://cdn-media-1.freecodecamp.org/images/z4aLzzcqepAfvKzy8SgY-hpYfAkRjh6NAbDE)

Now, let’s make a few changes to enhance our **Product** datagrid.

First of all, we will add some conditional formatting: whenever the **InventoryOnHand** is set to zero or a negative value, it is displayed using a different background color. We will use the [set_conditional_format()](https://phpgrid.com/documentation/set_conditional_format/) function for this purpose.

The above code adds a display condition so that whenever the `InventoryOnHand` field has a value that is less than (`lt`) one, the text color changes to `red` and the background color to dark gray (`#DCDCDC`).

Secondly, whenever the `InventoryOnHand` is less than the value shown in `MinimumRequired`, we would like to alert the user by displaying it in a prominent background color such as gold. To compare values between two fields, we must switch to Javascript because the [set_conditional_format()](https://phpgrid.com/documentation/set_conditional_format/) function only works with a single field.

The code below uses a `for` loop to iterate through each row in the **Products** datagrid. It compares the `inventoryOnHand` with the`minimumRequired` and, when the condition is met, it will use the`setCell` function to change the background color.

You can learn more about [comparing multiple cell values](https://phpgrid.uservoice.com/knowledgebase/articles/909546-conditional-format-compare-two-cells) on the phpGrid support website.

Next, on the same page, we need to see the purchases coming in (**Incoming**) and orders going out (**Outgoing**) for a specific product.

#### Purchases Detail Grid (Incoming)

#### Orders Detail Grid (Outgoing)

Both detail grids use the same foreign key `ProductId` to link to the master datagrid (**Products**).

Finally, our complete code to manage the **Current Inventory** page is:

Here’s the a snapshot of the inventory page:

![Image](https://cdn-media-1.freecodecamp.org/images/Spe5wb7oEkaVAikkKBEJrPzQExFzFj70EZTf)

### Incoming Purchases

![Image](https://cdn-media-1.freecodecamp.org/images/luyVRlrvSLQ10tITWdwYUHJ4A5flLdxEtuaZ)

The next page is the **Incoming Purchase** page. It is similar to the **Purchase Detail Grid** we saw when setting up the **Current Inventory** page. We group the purchases by `ProductId` and display the sum in`NumberReceived`. Any incoming purchases will increase the inventory.

> **Note: Grouping feature is only available in the phpGrid Professional and Enterprise edition. To filter without the grouping, use the [integration search](https://phpgrid.com/example/integrated-search/).**

The complete code:

Here’s a screenshot of our **Incoming Purchases** page with grouping enabled:

![Image](https://cdn-media-1.freecodecamp.org/images/8sDg-Tnhm0s1ZH5td-xdCWokJ3oO3ulAzf-T)

### Outgoing Orders

![Image](https://cdn-media-1.freecodecamp.org/images/9ymBPuuoXXvfEoCntXG-WPBxpUqIiGOpUACw)

The next page is the **Outgoing Orders** page. It is similar to the **Orders Detail Grid** from the **Current Inventory** page. Here, we will introduce an advanced function called [set_grid_method()](https://phpgrid.com/documentation/set_grid_method/).

### Summary

This tutorial builds a simple and extendable inventory system in less than 50 lines of code. The progressive style of these tutorials also helps the reader to ultimately become more familar and comfortable with phpGrid by introducing a limited number of new phpGrid features in each one.

### What’s Coming Up

This marks the end of the code needed to create the datagrids required for this tutorial. However, we are not done yet. There is still one more page we need to create — Reports. We will cover that after the jump.

What’s the use of an inventory system without some of type of report? In this section, you will learn how to use [phpChart](http://phpchart.com/) — which seamlessly integrates with phpGrid — to create visually pleasing and useful reports for your Inventory Manager application.

Here’s what our page will look like when it’s done:

![Image](https://cdn-media-1.freecodecamp.org/images/rLTmQ3BPx8zS1nbHXhPPaTDHB81SDxBrWqDE)

Before we start, we need to install phpChart. It is recommended that you obtain the [full version of phpChart](https://phpchart.com/download/) since the free version (phpChart Lite) supports only the line chart.

### Setup phpChart

It’s important that we keep phpGrid and phpChart in separate folders. Below is the **recommended** folder hierarchy.

```
www    +-- Donation_Manager    |   |-- phpGrid    |   |   +-- conf.php    |   |-- phpChart    |   |   +-- conf.php    |   +-- ...
```

### Report Design

We will place a pie chart next to an inventory summary grid. The datagrid provides the series data to plot the pie chart.

![Image](https://cdn-media-1.freecodecamp.org/images/oBEgm5-eYi2TXN1Ay5YQ-wgwGZveIgLFZpAp)

### phpGrid and phpChart Integration

First of all, include calls to both `**conf.php**` files at the beginning of the code.

```
require_once("phpGrid/conf.php"); require_once("phpChart/conf.php");
```

### Pie Chart

Below is the complete code to create our pie chart:

Let’s walk through the code.

The first line is the constructor. We pass `array(null)` as the series data because we don’t wish to have any data displayed in the pie chart initially. The inventory data used to plot the chart is not yet available when it is first initialized. The data is fed from the datagrid later in JSON.

We also give our chart a unique name, `PieChart`.

Next, we give it a title. Nothing fancy here.

Once we have the title, we call the [series default](https://phpchart.com/phpChart/docs/output/C_PhpChartX_set_series_default@.html) function to set the `renderer` to `PieRenderer`. Unlike a bar chart, a pie chart does not have a Y axis.

We can also set the `rendererOptions` property. We will not go into each option in detail here, but you can find more information in the [online documentation](https://phpchart.com/documentation/).

We also want to show a legend. The set_legend command below shows the legend to the west (noted by`w`) or to the left of the pie chart.

We will also remove the border and the background.

Finally, we draw our chart by giving it a height and width in pixels.

However, if you execute the code now, you will not see the chart because the data used to render it isn’t available yet.

### Inventory Summary Datagrid

Here, we will use the same the inventory datagrid as we did in the **Products** page. We just need to add one more thing — an event handler.

In phpGrid, we can add an event handler with the [add_event()](https://phpgrid.com/documentation/add_event/) function. add_event() binds an event handler, which is essentially a JavaScript function, to a specific phpGrid event. A list of possible events can be found [here](https://phpgrid.com/documentation/add_event/).

Since we must wait for the datagrid to finish loading **before** it can send the data to plot the chart, we use the event `jqGridLoadComplete`.

**phpGrid 101 — jqGridLoadComplete Event**

jqGridLoadComplete is last event that occurs once the whole datagrid body has finished loading. Note that the grid body will be reloaded if the user changes the sort order of a column or sets a filter.

#### Sending Data with Javascript

The following is the Javascript event handler for `jqGridLoadComplete`.

The complete code:

Now there you have it. Your just built your very first inventory management system from scratch using PHP and MySQL!

Thank you for reading! If you enjoyed this post, please give me some claps so more people see it.

### New to Programming? Fear Not!

If you are new to programming and are not yet comfortable with coding, you may want to check out [ZenBase](https://getzenbase.com/) that is built on the top of the phpGrid. The Inventory Management System is but one of the [many application templates](https://getzenbase.com/templates/) readily available at ZenBase for anyone — _with or without_ coding skills — to use and customize for their own needs.

### Online Demo

* [Current Inventory](https://phpdatagrid.com/apps/inventory-manager/products.php)
* [Incoming Purchases](https://phpdatagrid.com/apps/inventory-manager/incoming-purchases.php)
* [Outgoing orders](https://phpdatagrid.com/apps/inventory-manager/outgoing-order.php)
* [Reports](https://phpdatagrid.com/apps/inventory-manager/reports.php) (with datagrid side-by-side)

### Next: Add the barcode scanner

[Add the barcode scanner to our inventory management system](https://medium.com/@chensformers/inventory-management-system-with-barcode-scanner-in-php-a-definitive-guide-d18fdc165511)

![Image](https://cdn-media-1.freecodecamp.org/images/VqWE2ltTZhdjoJld8PcEnfrTL4g645hyQJTv)

### Download Source Code on Github

[**phpcontrols/inventory-manager**](https://github.com/phpcontrols/inventory-manager)  
[_Source code of inventory-manager the awesome Inventory Management Application in PHP and MySQL from Start to Finish_github.com](https://github.com/phpcontrols/inventory-manager)

### **Common Issue:**

**Fatal error**: Uncaught Error: Class ‘phpGrid\C_DataGrid’ not found

**How to fix:**  
If you are using the free Lite version, you can either comment out the first line

```
// use phpGrid\C_DataGrid;
```

— OR —

Add a global namespace symbol — single backslash — BEFORE the constructor

```
$dg = new \C_DataGrid(“SELECT * FROM orders”, “orderNumber”, “orders”);
```

### You may be also interested in those tutorials:

[**Build a Project Management Application From Scratch**](https://phpgrid.com/example/build-project-management-application-scratch/)  
[_What is a Project Management Application?_](https://phpgrid.com/example/build-project-management-application-scratch/)[**Build a Simple CRM from Start to Finish**](https://phpgrid.com/example/build-first-simple-crm-scratch/)   
[_Customer Relationship Management (CRM) is a system that manages customer interactions and data throughout the customer…_](https://phpgrid.com/example/build-first-simple-crm-scratch/)[**Building a Donation Manager from Scratch in PHP**](https://medium.com/@chensformers/a-step-by-step-guide-to-building-a-donation-manager-from-scratch-in-php-part-i-514a7d34ee82)

### Thanks for reading. If you enjoyed this article, please hit that clap button ? to help others find it and f[ollow me on Twitter.](https://twitter.com/midlifesaas)

![Image](https://cdn-media-1.freecodecamp.org/images/vOBVYAx4FtRWyDloyXcnKPsRfAh4OMvCI9zC)

### **Would you like to see more tutorials like this? Send a request to my [Twitter](https://twitter.com/midlifesaas) or leave a comment below!**

