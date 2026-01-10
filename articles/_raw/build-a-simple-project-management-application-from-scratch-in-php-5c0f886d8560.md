---
title: How to build a Project Management Application in PHP & MySQL from scratch
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-06T07:47:30.000Z'
originalURL: https://freecodecamp.org/news/build-a-simple-project-management-application-from-scratch-in-php-5c0f886d8560
coverImage: https://cdn-media-1.freecodecamp.org/images/1*p6kGOdvkbqMJQKuSYgDvOg.jpeg
tags:
- name: PHP
  slug: php
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Richard

  Trying to find a project management application is a daunting task: you want a system
  with powerful features and you must get a buy-in from your colleagues. Most of the
  time, you wind up with a bloated system filled with features you’ll ne...'
---

By Richard

Trying to find a project management application is a daunting task: you want a system with powerful features and you must get a buy-in from your colleagues. Most of the time, you wind up with a bloated system filled with features you’ll never use.

The good news is that it turns out it is not that difficult to build one from scratch yourself. After reading this tutorial, you should have a clean, well-designed project management application up and running in less than an hour.

### What IS a Project Management Application?

A project management application is a software system used for project planning, resource allocation, tracking of project components, and change management.

In this tutorial, we are going to build a simple project management system in PHP which employees and managers can use for collaboration and communication between project stakeholders.

### What is IN a Project Management Application?

We will be creating a simple and easily customizable PM system to tracks projects, including milestones, tasks, hours, costs, and more. Since every project is unique, this tutorial merely means to build an application foundation; you should be able to easily extend it based on your requirements.

**In our project management application, employees will be able to:**

* View their tasks
* Log in hours worked

**Managers will be able to:**

* Manage projects
* Manage milestones
* Manage tasks
* Manage costs and hours
* Manage employee resources

### The Building Blocks of a Project Management System

![Image](https://cdn-media-1.freecodecamp.org/images/1*UlZUWinmrB6UXBV0D3CDeQ.jpeg)
_Building blocks of a typical project management system_

Here are the primary functions of a project management system:

* **Project planning**: To define a project schedule, a project manager may use the software to map project tasks and visually describe task interactions.
* **Task management**: Allows the project manager to create and assign tasks, establish deadlines, and produce status reports.
* **Resource management**: Defines responsibilities — who is supposed to do what.
* **Budgeting and cost tracking**: A good project management application facilitates budget reporting as well as viewing, notifying, and updating costs for stakeholders.
* **Time tracking**: The software must have the ability to track time spent on all tasks and maintain records for third-party consultants.

### System Requirements

* PHP 5.3+
* MySQL or MariaDB
* phpGrid

### Creating a Project Management Database

We will start by creating our project management database. The main tables we will use are:

* **Clients** — customer company data
* **Contacts** — client contact data. A client can have one or more contacts.
* **Projects** — project information
* **Milestones** — project milestone
* **Tasks** — project tasks
* **Hours** — time spent on each task
* **Costs** — cost of a task
* **Users** — user data; one can be either an employee or a manager

![Image](https://cdn-media-1.freecodecamp.org/images/0*4LoHe5Bje3Yxtxry.png)

Other tables ([lookup tables):](https://www.quora.com/In-database-what-are-lookup-tables)

* **ms_status**
* **proj_status**
* **task_status**

#### Complete Database Schema Diagram

A database schema is the structure that represents the logical view of the entire database: tables, views, and primary and foreign keys. A database schema includes all entities and the relationships between them.

Below is the database diagram of our simple project management application. The key symbol in each table represents the table’s primary key while the magnifying glass indicates a foreign key linking it to another table (lookup table) in the database.

![Image](https://cdn-media-1.freecodecamp.org/images/0*r5SvnI9MG2xR8Nlk.png)

#### simple_pm_install.sql

Once you have an understanding of the database’s table structure, obtain the [**simple_pm_install.sql**](https://github.com/phpcontrols/phpgrid-project-management/blob/master/db/simple_pm_install.sql) sql script from this tutorial’s GitHub repo, and then execute the sql script using a MySQL tool such as MySQL Workbench or Sequel Pro. This will create a new database named `simple_pm` and tables we need in this tutorial.

### Setup phpGrid

Our simple project management contains many DataGrids. The DataGrid is a spreadsheet-like data table which displays rows and columns representing records and fields from the database table. The DataGrid provides the end-user with the ability to read and write to the database tables on a web page.

To create the DataGrid, we use a dataGrid tool from [phpGrid](https://phpgrid.com/) . The reason why we use a tool instead of building our grids from scratch is that developing a DataGrid in php is usually extremely tedious and prone to errors. The phpGrid DataGrid library will handle all internal database **CRUD (Create, Remove, Update, and Delete)** operations for us offering faster and better results with minimal coding.

To install phpGrid, follow these steps:

1. Unzip the phpGrid download file.
2. Upload the phpGrid folder to the `**phpGrid**` folder.
3. Complete the installation by configuring the `**conf.php**` file.

Before we begin coding, we must include the following information in `conf.php` the phpGrid configuration file. Here is an example of the database connection settings:

```
define(‘PHPGRID_DB_HOSTNAME’, ‘localhost’); define(‘PHPGRID_DB_USERNAME’, ‘root’); define(‘PHPGRID_DB_PASSWORD’, ‘’); define(‘PHPGRID_DB_NAME’, ‘custom_pm’); define(‘PHPGRID_DB_TYPE’, ‘mysql’);
```

* **PHPGRID_DB_HOSTNAME** — web server IP or host name
* **PHPGRID_DB_USERNAME** — database user name
* **PHPGRID_DB_PASSWORD** — database password
* **PHPGRID_DB_NAME** — database name
* **PHPGRID_DB_TYPE** — type of database
* **PHPGRID_DB_CHARSET** — always ‘utf8’ in MySQL

### Page Template

![Image](https://cdn-media-1.freecodecamp.org/images/0*0wRyhPo3UlSTHqBR.png)

Our page will be comprised of a **header**, **menu**, **body**, and **footer**. Instead of creating the same page elements repeatedly, we will start by creating a reusable page template.

#### head.php

This is a basic HTML5 template header; it includes a link to a custom stylesheet that will be created in a later step.

#### menu.php

![Image](https://cdn-media-1.freecodecamp.org/images/0*AwNHOfr7NQte7_PV.png)

Notice the usage of `$_GET['currentPage']`. Each page will set a value that will highlight the name of the current page on the top menu bar.

Include the following code in `**style.css**` for menu styling; it will transform the above unordered list into a menu.

#### footer.php

Simply includes the closing tags for the elements we opened in the header:

### Our Complete Reusable Page Template

The main content will go after the section title.

### Project Management Main Pages

![Image](https://cdn-media-1.freecodecamp.org/images/1*unOpP83dlvhHy5MlQjg1Uw.jpeg)

Our project management application for managers has four pages:

* **Clients**
* **Client Details**
* **Projects**
* **Project Details**

The **Clients** page displays a list of clients with links to individual client details (**Client Details** page).

The **Projects** page displays a list of projects being managed with links to project details (**Project Details** page).

#### Design Mockup

Here is our project management application design mockup for project managers who manage one or more projects and assign tasks to employees.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ozCobyEZ-YFB0v4e.png)

#### Clients

When a manager logs in to the project management system, the first page he sees is the **Clients** page which contains a complete list of companies.

The following code will give us a list of clients.

* The first line creates a phpGrid object by passing the SELECT SQL statement with its primary key `**id**` followed by the name of the database table – `**clients**`.
* The second line creates a dynamic URL from the primary key “id”; it uses a function called `**set_col_dynalink()**`. This function sets a specific column-to-display HTML hyperlink URL based on dynamic values. If the primary key “id” has the value 100, it will display a URL like this `**client-details.php?id=100**` which drills down the client detail page.
* The third line, `[**enable_edit()**](https://phpgrid.com/documentation/enable_editedit/)`, makes the DataGrid editable and all CRUD (Create, Read, Update, Delete) operations are now accessible.
* The last line calls the `[**display()**](https://phpgrid.com/documentation/display/)` function to render the DataGrid on the screen.

You can find out more demos below using those functions:

[**Display Dynamic URL | phpGrid**](https://phpgrid.com/example/display-dynamic-url/)  
[_From example above, we learn that phpGrid can display simple, static URL using set_col_link() method. However, it is…_phpgrid.com](https://phpgrid.com/example/display-dynamic-url/)[**CRUD PHP Datagrid (Editable Datagrid) * | phpGrid**](https://phpgrid.com/example/edit-datagrid/)  
[_The PHP datagrid is not editable by default. You can enable edit by simply calling enable_edit(). Whala!_phpgrid.com](https://phpgrid.com/example/edit-datagrid/)

#### Client Details

From the **Clients** page, the client name has a hyperlink that redirects to the **Client Details** page for that client when clicked.

![Image](https://cdn-media-1.freecodecamp.org/images/0*P8YU_L6z6plrZ2OD.png)

From the **Client Details** page, we need to obtain the Client ID that is passed as the URL parameter.

In our application, the Client ID should always be an integer. Thus, we use the PHP `[**intval()**](http://php.net/manual/en/function.intval.php)` function to ensure the Client ID is returned as an integer.

The following code displays projects associated with the current `$clientId` using the filter function `[**set_query_filter()**](https://phpgrid.com/documentation/set_query_filterwhere/)`. In addition, we make the DataGrid editable with the `[**enable_edit()**](https://phpgrid.com/documentation/enable_editedit/)` function; phpGrid will take care of any CRUD operations for us.

**Client Details > Proje**cts

As you may notice, we again use the same function, `**set_col_dynalink()**`, to create hyperlinks to the **Project Details** table using the Project ID. We will get into the `**project-details.php**` page next.

```
<h4>Projects</h4>
```

**Client Details > Conta**cts

Under the **Projects** DataGrid, a list of contacts associated with the `$clientid` is displayed using the same functions `[**set_query_filter()**](https://phpgrid.com/documentation/set_query_filterwhere/)` and `[**enable_edit()**](https://phpgrid.com/documentation/enable_editedit/)`.

#### Contacts

#### Projects

Now, let’s build the **Projects** page.

The **Projects** page displays a list of managed projects. It is very similar to the **Clients** page except that the database table is “Projects,” and the hyperlinks have the URL `**project-details.php**` instead of `**client-details.php**`.

#### Project Details

From the **Projects** page, each project name has a hyperlink which redirects to each individual **Project Details** page when clicked.

![Image](https://cdn-media-1.freecodecamp.org/images/0*i5TQaclrfxGruHgv.png)

And from the **Project Details** page, we retrieve the Project ID for the URL parameter.

Look familiar? Because it is! It should because both **Projects** and **Project Details** pretty much follow the same coding pattern used in the **Clients** and **Client Details** pages; there are not really that many surprises.

The **Project Details** page is made of the following grids, all filtered by the `$projectId` obtained from the URL parameter.

* **Milestones**
* **Tasks**
* **Hours**
* **Costs**

#### Milestones

A milestone marks a major event in a project timeline. Here, we can easily display all the milestones of a project by filtering the value `$projectId`. Project managers have the necessary access rights to modify the milestones.

Likewise, we can easily filter and display a list of tasks for the current project.

I think you are probably getting the hang of it now. Here’s the code for the two remaining datagrids.

### Employees Page

We can now move on to the final part of the tutorial, the **Employees** page. Employees can login to view active project tasks assigned to them, track task hours, and costs. Their responsibility is simple: to monitor the tasks and log hours worked on any specific project task.

### Design Mockup

![Image](https://cdn-media-1.freecodecamp.org/images/0*rTydMfZp34UUZDmq.png)

#### Menu

The **Employees** page has only one menu item: **Tasks**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*r6uIHldzshuM7tTM.png)

#### My Active Tasks

The first part of the page shows a list of active tasks assigned to the current employee. Each task will have the hours reported by the current employee; this is a perfect situation in which to use a [phpGrid subgrid](https://phpgrid.com/example/subgrid/).

We also need to use `[**set_query_filter()**](https://phpgrid.com/documentation/set_query_filterwhere/)` to display only active tasks that have Status value "2", and only for the current employee.

For demo purposes, we hard-coded the Employee ID to 2. In a real-world application, the Employee ID value should be stored and retrieved using [PHP SESSION](http://php.net/manual/en/book.session.php).

We then create the active **Tasks** DataGrid for the current employee. Notice the filter function.

Once we’ve defined the grid for the active tasks, we create a DataGrid to log the hours reported by the current employee.

Lastly, `[**set_subgrid()**](https://phpgrid.com/documentation/set_subgrid/)` causes the **Hours** DataGrid to become a subgrid of the **Tasks** DataGrid. The linking field in the **Hours** subgrid is ‘TaskID’, which is the second parameter, and in the main grid **Tasks**, it is “id,” the third parameter.

![Image](https://cdn-media-1.freecodecamp.org/images/0*nhIZDWCH9ED_BMCi.png)

#### My Hours History

Lastly, we would like to display a read-only DataGrid using data from the **Hours** table for the current employee for reviewing purposes.

Notice we used a function called `[**set_jq_gridName()**](https://phpgrid.com/documentation/set_jq_gridname/)`. You can find more documentation [here](https://phpgrid.com/documentation/set_jq_gridname/). This function sets a unique object name for the DataGrid. By default, phpGrid uses the database table name as its internal object name. Since we already created a DataGrid from the **Hours** table in the last part, we must set a unique name for our second **Hours** DataGrid.

### Application Screenshots

#### Managers

![Image](https://cdn-media-1.freecodecamp.org/images/0*0nxynYSGiECfL0X7.png)

![Image](https://cdn-media-1.freecodecamp.org/images/0*nXppkdoX82Cu90yz.png)

#### Employee

![Image](https://cdn-media-1.freecodecamp.org/images/0*5-IFndGjMJ_h82dJ.png)

### Live Demo

[Login as manager](https://www.phpdatagrid.com/apps/phpgrid-project-management/manager/clients.php) | [Login as employee](https://www.phpdatagrid.com/apps/phpgrid-project-management/employee/tasks.php)

### Download Source Code

[**phpcontrols/phpgrid-project-management**](https://github.com/phpcontrols/phpgrid-project-management)  
[_phpgrid-project-management — phpGrid Complete Project Management Demo Application_github.com](https://github.com/phpcontrols/phpgrid-project-management)

### Thanks for reading. If you enjoyed this article, please hit that clap button ? to help others find it and f[ollow me on Twitter.](https://twitter.com/midlifesaas)

![Image](https://cdn-media-1.freecodecamp.org/images/1*v-_G34PI1sMmIxI1xstaYQ.png)

