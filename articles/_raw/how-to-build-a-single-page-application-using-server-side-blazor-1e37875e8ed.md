---
title: How to build a single page application using server-side Blazor
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-17T15:22:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-single-page-application-using-server-side-blazor-1e37875e8ed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*r8lWHbH-mgWkl462lQsYuQ.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we will create a Single Page Application (SPA) using server-side
  Blazor. We will use an Entity Framework Core database. Single-Page Applications
  are web applications that load a single HTML page. They dyn...'
---

By Ankit Sharma

### Introduction

In this article, we will create a Single Page Application (SPA) using server-side Blazor. We will use an Entity Framework Core database. Single-Page Applications are web applications that load a single HTML page. They dynamically update that page as the user interacts with the app.

We will be creating a sample Employee Record Management System. We will perform CRUD operations on it. A modal popup will display the form to handle user inputs. The form will also have a dropdown list which will bind to a database table. We will also provide a filter option to the user to filter the employee records based on employee name.

We will be using Visual Studio 2017 and SQL Server 2017 for our demo.

Let us look at the final application:

![Image](https://cdn-media-1.freecodecamp.org/images/aI57jsCNIw1NRiqTqY99wr3rwJBCf-vE-FgP)

### What is Server-Side Blazor?

The release 0.5.0 of Blazor allows us to run Blazor applications on the server. This means that we can run the Blazor component server-side on .NET Core. A SignalR connection over the network will handle other functionalities such as UI updates, event handling, and JavaScript interop calls.

For more information, refer to my previous article on [Understanding Server-Side Blazor](http://ankitsharmablogs.com/understanding-server-side-blazor/).

### Prerequisites

* Install the .NET Core 2.1 or above SDK from [here](https://www.microsoft.com/net/learn/get-started-with-dotnet-tutorial#windowscmd)
* Install Visual Studio 2017 v15.7 or above from [here](https://visualstudio.microsoft.com/downloads/)
* Install ASP.NET Core Blazor Language Services extension from [here](https://marketplace.visualstudio.com/items?itemName=aspnet.blazor)
* SQL Server 2012 or above.

Visual Studio 2017 versions below v15.7 do not support the Blazor framework.

### Source Code

Get the source code for this application from [GitHub](https://github.com/AnkitSharma-007/Blazor-Server-Side-SPA).

Important Note :

**This article is valid for Blazor 0.5.0 release. The server-side Blazor might undergo breaking changes in future releases of Blazor.**

### Creating a Table

We will be using two tables to store our data.

1. Employee: Used to store employee details. It contains fields such as EmployeeID, Name, City, Department, and Gender.
2. Cities: This contains the list of cities. It is used to populate the _City_ field of the Employee table. It contains two fields, CityID and CityName

Execute the following commands to create both tables:

```sql
CREATE TABLE Employee (  
EmployeeID int IDENTITY(1,1) PRIMARY KEY,  
Name varchar(20) NOT NULL ,  
City varchar(20) NOT NULL ,  
Department varchar(20) NOT NULL ,  
Gender varchar(6) NOT NULL  
)    
GO      
      
CREATE TABLE Cities (      
CityID int IDENTITY(1,1) NOT NULL PRIMARY KEY,      
CityName varchar(20) NOT NULL       
)      
GO
```

Now, we will put some data into the Cities table. We will be using this table to bind a dropdown list in our web application. The user will select the desired city from this dropdown. Use the following insert statements:

```sql
INSERT INTO Cities VALUES('New Delhi');  
INSERT INTO Cities VALUES('Mumbai');  
INSERT INTO Cities VALUES('Hyderabad');  
INSERT INTO Cities VALUES('Chennai');  
INSERT INTO Cities VALUES('Bengaluru');
```

Now, our Database part is complete. So we will proceed to create the server side application using Visual Studio 2017.

### Create The Server Side Blazor Application

Open Visual Studio and select File >> New >> Project.

After selecting the project, a “New Project” dialog will open. Select .NET Core inside the Visual C# menu from the left panel. Then, select “ASP.NET Core Web Application” from the available project types. For project name, put in _ServerSideSPA_ and press OK.

![Image](https://cdn-media-1.freecodecamp.org/images/189S93tL5-3DZBX5e4h0rd9jgLOAla4DHA1V)

After clicking on OK, a new dialog will open asking you to select the project template. You will see two drop-down menus at the top left of the template window. Select “.NET Core” and “ASP.NET Core 2.1” from these dropdowns. Then, select the “Blazor (Server-side in ASP.NET Core)” template and press OK

![Image](https://cdn-media-1.freecodecamp.org/images/koiBPXcDf1INRT--9ZBVhLcDMJ8WIqy9w7PU)

This will create our server-side Blazor solution. You can observe the folder structure in solution explorer, as shown in the below image:

![Image](https://cdn-media-1.freecodecamp.org/images/dBOrb-cKYR8pXh04n7IE1jA71yP-nZTiR1Hv)

The solution has two project files:

1. ServerSideSPA.App: This is our server-side Blazor app. This project has all our component logic and our services. We will also create our models and data access layer in this project.
2. ServerSideSPA.Server: This is the ASP.NET Core hosted application. Instead of running client-side in the browser, the server-side Blazor app will run in the ASP.NET Core host application.

In future releases of Blazor, these two projects might be merged into one. But for now, the separation is required due to the differences in the Blazor compilation model.

### Scaffolding the Model to the Application

We are using Entity Framework core database first approach to create our models. We will create our model class in _ServerSideSPA.App_ project.  
Navigate to Tools >> NuGet Package Manager >> Package Manager Conso_le. Select “S_e_rve_rSideSPA.App” from the Default project drop-down. Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/apHcquWdcINo4yx7ZTRSY4GVrQSPOsyTWp8m)

First, we will install the package for the database provider that we are targeting which is SQL Server in this case. Hence, run the following command:

```
Install-Package Microsoft.EntityFrameworkCore.SqlServer
```

Since we are using Entity Framework Tools to create a model from the existing database, we will install the tools package as well. Hence, run the following command:

```
Install-Package Microsoft.EntityFrameworkCore.Tools
```

After you have installed both packages, we will scaffold our model from the database tables using the following command:

```
Scaffold-DbContext "Your connection string here" Microsoft.EntityFrameworkCore.SqlServer -OutputDir Models -Tables Employee, Cities
```

Do not forget to put your own connection string (inside “ ”). After this command executes successfully, it creates a models folder inside _ServerSideSPA.App_ project. It contains three class files: _myTestDBContext.cs, Cities.cs_ and _Employee.cs_. Hence, we have successfully scaffolded our Models using EF core database first approach.

### Creating the Data Access Layer for the Application

Right-click on ServerSideSPA.App project and then select Add >> New Folder and name the f_older Data_Access. We will be adding our class to handle database related operations inside this folder only.

Right click on the _DataAccess_ folder and select Add >> Class.

Name your class _EmployeeDataAccessLayer.cs._ Open _EmployeeDataAccessLayer.cs_ and put the following code into it:

```cs
using Microsoft.EntityFrameworkCore;
using ServerSideSPA.App.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ServerSideSPA.App.DataAccess
{
    public class EmployeeDataAccessLayer
    {
        myTestDBContext db = new myTestDBContext();

        //To Get all employees details     
        public List<Employee> GetAllEmployees()
        {
            try
            {
                return db.Employee.AsNoTracking().ToList();
            }
            catch
            {
                throw;
            }
        }

        //To Add new employee record       
        public void AddEmployee(Employee employee)
        {
            try
            {
                db.Employee.Add(employee);
                db.SaveChanges();
            }
            catch
            {
                throw;
            }
        }

        //To Update the records of a particluar employee      
        public void UpdateEmployee(Employee employee)
        {
            try
            {
                db.Entry(employee).State = EntityState.Modified;
                db.SaveChanges();
            }
            catch
            {
                throw;
            }
        }

        //Get the details of a particular employee      
        public Employee GetEmployeeData(int id)
        {
            try
            {
                var employee = db.Employee.Find(id);
                db.Entry(employee).State = EntityState.Detached;
                return employee;
            }
            catch
            {
                throw;
            }
        }

        //To Delete the record of a particular employee      
        public void DeleteEmployee(int id)
        {
            try
            {
                Employee emp = db.Employee.Find(id);
                db.Employee.Remove(emp);
                db.SaveChanges();
            }
            catch
            {
                throw;
            }
        }

        // To get the list of Cities
        public List<Cities> GetCityData()
        {
            try
            {
                return db.Cities.ToList();
            }
            catch
            {
                throw;
            }
        }
    }
}
```

Here, we have defined the methods to handle database operations:

* _GetAllEmployees_ will fetch all the employee data from the Employee table.
* _AddEmployee_ will create a new employee record.
* _UpdateEmployee_ will update the record of an existing employee.
* _GetEmployeeData_ will fetch the record of the employee corresponding to the employee ID passed to it.
* _DeleteEmployee_ will delete the employee record corresponding to the employee id passed to it.
* _GetCityData_ will fetch the list of all the cities from _Cities_ table.

### Creating the Service class

Right click on the _Services_ folder and select Add >> Class. Give it a name of “EmployeeService.cs” and _cli_ck Add. This will ad_d the EmployeeS_ervice class to the Services folder.

Open EmployeeService.cs and put the following code into it:

```cs
using ServerSideSPA.App.DataAccess;
using ServerSideSPA.App.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ServerSideSPA.App.Services
{
    public class EmployeeService
    {
        EmployeeDataAccessLayer objemployee = new EmployeeDataAccessLayer();

        public Task<List<Employee>> GetEmployeeList()
        {
            return Task.FromResult(objemployee.GetAllEmployees());
        }

        public void Create(Employee employee)
        {
            objemployee.AddEmployee(employee);
        }
        
        public Task<Employee> Details(int id)
        {
            return Task.FromResult(objemployee.GetEmployeeData(id));
        }
        
        public void Edit(Employee employee)
        {
            objemployee.UpdateEmployee(employee);
        }
        
        public void Delete(int id)
        {
            objemployee.DeleteEmployee(id);
        }
        
        public Task<List<Cities>> GetCities()
        {
            return Task.FromResult(objemployee.GetCityData());
        }
    }
}
```

We will invoke the methods of _EmployeeDataAccessLayer_ class from our service. The service will be injected into our components. The components will call the service methods to access the database.

At this point in time, the ServerSideSPA.App project has the following structure:

![Image](https://cdn-media-1.freecodecamp.org/images/fG4Y1m1kRP7kxp4yRSZ1OxoNQ2BLyuFw2jA2)

### Configuring the Service

To make the service available to the components, we need to configure it on the server-side app. Open ServerSideSPA.App >> Startup.cs file. Add the following line insid_e the ConfigureSer_vices method of the Startup class.

```cs
services.AddSingleton<EmployeeService>();
```

Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/jCNjuzfmweuNj40kQePIJR1lxoIZRDnRdvzh)

Now we will proceed to create our view component.

### Creating The View Component

We will add the Razor page in the _ServerSideSPA.App /Pages_ folder. By default, we have “Counter” and “Fetch Data” pages provided in our application. These default pages will not affect our application. For the sake of this tutorial, delete both of them from the _ServerSideSPA.App /Pages_ folder.

Right-click on ServerSideSPA.App _/Pages_ folder and then select Add >> New Item. An “Add New Item” dialog box will open. Select “ASP.NET Core” from the left panel. Then select “Razor Page” from the templates panel and na_me it EmployeeData._cshtml. Click Add.

![Image](https://cdn-media-1.freecodecamp.org/images/ZfAJA4ZPi6uK8snnXGwPmJFH5vrlzyOOLmZW)

This will add an _EmployeeData.cshtml_ page to the _Pages_ folder. This razor page will have two files, _EmployeeData.cshtml_ and _EmployeeData.cshtml.cs._  
Now, we will add code to these pages.

### EmployeeData.cshtml

Open the _EmployeeData.cshtml_ page and put the following code into it:

```cs
@page "/fetchemployee"
@inherits EmployeeDataModel

<h1>Employee Data</h1>
<p>This component demonstrates CRUD operation on Employee data</p>

<div>
    <div style="float:left">
        <button class="btn btn-primary" onclick="@AddEmp">Add Employee</button>
    </div>
    <div style="float:right; width:40%;">
        <div class="col-sm-6" style="float:left">
            <input class="form-control" type="text" placeholder="Search" bind="@SearchString" />
        </div>
        <div>
            <button type="submit" class="btn btn-default btn-info" onclick="@FilterEmp">Filter</button>
        </div>
    </div>
</div>

@if (empList == null)
{
    <p><em>Loading...</em></p>
}
else
{
    <table class='table'>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Gender</th>
                <th>Department</th>
                <th>City</th>
            </tr>
        </thead>
        <tbody>
            @foreach (var emp in empList)
            {
                <tr>
                    <td>@emp.EmployeeId</td>
                    <td>@emp.Name</td>
                    <td>@emp.Gender</td>
                    <td>@emp.Department</td>
                    <td>@emp.City</td>
                    <td>
                        <button class="btn btn-default" onclick="@(async () => await EditEmployee(@emp.EmployeeId))">Edit</button>
                        <button class="btn btn-danger" onclick="@(async () => await DeleteConfirm(@emp.EmployeeId))">Delete</button>
                    </td>
                </tr>
            }
        </tbody>
    </table>

    if (isAdd)
    {
        <div class="modal" tabindex="-1" style="display:block" role="dialog">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h3 class="modal-title">@modalTitle</h3>
                        <button type="button" class="close" onclick="@closeModal">
                            <span aria-hidden="true">X</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <form>
                            <div class="form-group">
                                <label for="Name" class="control-label">Name</label>
                                <input for="Name" class="form-control" bind="@emp.Name" />
                            </div>
                            <div class="form-group">
                                <label asp-for="Gender" class="control-label">Gender</label>
                                <select asp-for="Gender" class="form-control" bind="@emp.Gender">
                                    <option value="">-- Select Gender --</option>
                                    <option value="Male">Male</option>
                                    <option value="Female">Female</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label asp-for="Department" class="control-label">Department</label>
                                <input asp-for="Department" class="form-control" bind="@emp.Department" />
                            </div>
                            <div class="form-group">
                                <label asp-for="City" class="control-label">City</label>
                                <select asp-for="City" class="form-control" bind="@emp.City">
                                    <option value="">-- Select City --</option>
                                    @foreach (var city in cityList)
                                    {
                                        <option value="@city.CityName">@city.CityName</option>
                                    }
                                </select>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button class="btn btn-block btn-info" onclick="@(async () => await SaveEmployee())" data-dismiss="modal">Save</button>
                    </div>
                </div>
            </div>
        </div>
    }

    if (isDelete)
    {
        <div class="modal" tabindex="-1" style="display:block" role="dialog">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h3 class="modal-title">Delete Employee</h3>
                    </div>
                    <div class="modal-body">
                        <h4>Do you want to delete this employee ??</h4>
                        <table class="table">
                            <tr>
                                <td>Name</td>
                                <td>@emp.Name</td>
                            </tr>
                            <tr>
                                <td>Gender</td>
                                <td>@emp.Gender</td>
                            </tr>
                            <tr>
                                <td>Department</td>
                                <td>@emp.Department</td>
                            </tr>
                            <tr>
                                <td>City</td>
                                <td>@emp.City</td>
                            </tr>
                        </table>
                    </div>
                    <div class="modal-footer">
                        <button class="btn btn-danger" onclick="@(async () => await DeleteEmployee(emp.EmployeeId))" data-dismiss="modal">YES</button>
                        <button class="btn btn-warning" onclick="@closeModal">NO</button>
                    </div>
                </div>
            </div>
        </div>
    }
}
```

Let me explain this code. At the top, we have defined the route for this page as “/fetchemployee”. This means if we append “/fetchemployee” to the root URL of the app, we will be redirected to this page.

We are also inheriting _EmployeeDataModel_ class which is defined in _EmployeeData.cshtml.cs_ file. This will allow us to use the methods defined in EmployeeDataModel class.

After this, we have defined a button to add a new employee record. When clicked, this button will open a modal popup to handle the user inputs.

We have also defined a searchbox and a corresponding button to filter the employee records based on employee name. If you enter an employee name and click on the filter button, it will show all matching employee records. If we click on the filter button without entering any value in the search box, it will return all the employee records.

The employee records returned from the database are stored in the _empList_ variable. If the variable is not null, then we will bind the values to a table to display the employee records in a tabular fashion. Each employee record will also have two action links — _Edit_ to edit the employee record, and _Delete_ to delete the employee record.

To handle the user inputs, we are using a form. We are using a single form for both Add Employee and Edit Employee functionality. The form is defined in a modal popup. The modal popup is displayed on the screen based on the value of the Boolean property isAdd. The value of this Boolean property is set in the code behind (.cshtml.cs) page.

The City dropdown list inside the form is binding to our Cities table in the database with the help of the _cityList_ variable. The cityList will be populated as the application boots up.

The form will have a _Save_ button which will invoke the SaveEmployee method. This method is defined in the code behind file to Add or update an employee record.

Similar to _Add_ modal popup, we also have a _Delete_ modal popup. It will be a read-only modal and ask for a confirmation to delete an employee record. Upon clicking “Yes”, it will invoke the _DeleteEmployee_ method to delete the employee record.

### EmployeeData.cshtml.cs

Open _EmployeeData.cshtml.cs_ and put the following code into it.

```cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Blazor;
using Microsoft.AspNetCore.Blazor.Components;
using Microsoft.AspNetCore.Blazor.Services;
using ServerSideSPA.App.Models;
using ServerSideSPA.App.Services;

namespace ServerSideSPA.App.Pages
{
    public class EmployeeDataModel : BlazorComponent
    {
        [Inject]
        protected EmployeeService employeeService { get; set; }

        protected List<Employee> empList;
        protected List<Cities> cityList = new List<Cities>();
        protected Employee emp = new Employee();
        protected string modalTitle { get; set; }
        protected Boolean isDelete = false;
        protected Boolean isAdd = false;

        protected string SearchString { get; set; }

        protected override async Task OnInitAsync()
        {
            await GetCities();
            await GetEmployee();
        }

        protected async Task GetCities()
        {
            cityList = await employeeService.GetCities();
        }

        protected async Task GetEmployee()
        {
            empList = await employeeService.GetEmployeeList();
        }

        protected async Task FilterEmp()
        {
            await GetEmployee();
            if (SearchString != "")
            {
                empList = empList.Where(x => x.Name.IndexOf(SearchString, StringComparison.OrdinalIgnoreCase) != -1).ToList();
            }
        }

        protected void AddEmp()
        {
            emp = new Employee();
            this.modalTitle = "Add Employee";
            this.isAdd = true;
        }

        protected async Task EditEmployee(int empID)
        {
            emp = await employeeService.Details(empID);
            this.modalTitle = "Edit Employee";
            this.isAdd = true;
        }

        protected async Task SaveEmployee()
        {
            if (emp.EmployeeId != 0)
            {
                await Task.Run(() =>
                {
                    employeeService.Edit(emp);
                });
            }
            else
            {
                await Task.Run(() =>
                {
                    employeeService.Create(emp);
                });
            }
            this.isAdd = false;
            await GetEmployee();
        }

        protected async Task DeleteConfirm(int empID)
        {
            emp = await employeeService.Details(empID);
            this.isDelete = true;
        }

        protected async Task DeleteEmployee(int empID)
        {
            await Task.Run(() =>
            {
                employeeService.Delete(empID);
            });
            this.isDelete = false;
            await GetEmployee();
        }
        protected void closeModal()
        {
            this.isAdd = false;
            this.isDelete = false;
        }
    }
}
```

Let me explain this code. We have defined a class _EmployeeDataModel._ It will hold all the methods that we will be using in _EmployeeData.cshtml_ page.

We are injecting our _EmployeeService_ to the _EmployeeDataModel_ class so that the client-side methods can invoke our services.

The variables _empList_ and _cityList_ hold the data from the Employee and Cities tables. The variables are getting populated inside the OnInitAsync to make sure that the data is available to us as the page loads.

We will use the _FilterEmp_ method to filter the employee data based on the employee name property. This property will ignore the text case of the search string. It returns all the records that match either fully or partially with the search string.

Clicking the “Add Employee” button will invoke the _AddEmp_ method. It will initialize an empty instance of Employee model and set the value of the _isAdd_ Boolean flag to true. This will open a modal popup with a form, asking the user to enter a new employee record. Similarly, we have defined an _EditEmployee_ method. It fetches the record of the employee based on the employee id for which it is invoked. It will also set the value of _isAdd_ to true to open the modal popup to edit the employee record.

The _SaveEmployee_ method will check if it is invoked to add a new employee record or to edit an existing employee record. If the EmployeeId property is set, then it is an “edit” request, and we will invoke the Edit method of our service. If EmployeeId is not set, then it is a “create” request, and we will invoke the Create method of our service. We will then fetch the updated employee record by calling the _GetEmployee_ method and will also set the value of _isAdd_ to false, thus closing the modal popup.

The _DeleteConfirm_ method is invoked by clicking the Delete button corresponding to an employee record. It will set the value of the isDelete Boolean flag to true. This will display a Delete confirmation modal popup. Upon clicking YES inside this popup, DeleteEmployee method is invoked. This will delete the employee record and set the _isDelete_ Boolean flag to false to close the modal popup.

### Adding Link to Navigation menu

The last step is to add the link to our “EmployeeData” page in the navigation menu. Open _ServerSideSPA.App/Shared/NavMenu.cshtml_ page and put the following code into it:

```cs
<div class="top-row pl-4 navbar navbar-dark">
    <a class="navbar-brand" href="">ServerSideSPA</a>
    <button class="navbar-toggler" onclick=@ToggleNavMenu>
        <span class="navbar-toggler-icon"></span>
    </button>
</div>

<div class=@(collapseNavMenu ? "collapse" : null) onclick=@ToggleNavMenu>
    <ul class="nav flex-column">
        <li class="nav-item px-3">
            <NavLink class="nav-link" href="" Match=NavLinkMatch.All>
                <span class="oi oi-home" aria-hidden="true"></span> Home
            </NavLink>
        </li>
        <li class="nav-item px-3">
            <NavLink class="nav-link" href="fetchemployee">
                <span class="oi oi-list-rich" aria-hidden="true"></span> Fetch employee
            </NavLink>
        </li>
    </ul>
</div>

@functions {
bool collapseNavMenu = true;

void ToggleNavMenu()
{
    collapseNavMenu = !collapseNavMenu;
}
}
```

This completes our Single Page Application using server-side Blazor.

### Execution Demo

Press F5 to launch the application.

A web page will open as shown in the image below. The navigation menu on the left is showing a navigation link for the Employee data page.

![Image](https://cdn-media-1.freecodecamp.org/images/dRbCSiMHUSfAh-saQWs4F0zQYNRhxXGcOnPa)

Clicking on the “Employee data” link will redirect to the EmployeeData view. Here you can see all the employee data on the page. Notice the URL has “/fetchemployee” appended to it.

![Image](https://cdn-media-1.freecodecamp.org/images/7etEYM3gWebYu79-hS0AGSGaIGrHGlBT27YX)

Click on the _Add Employee_ button to open the “Add Employee” modal popup. Enter the data in all the fields and click on Save to create a new employee record.

![Image](https://cdn-media-1.freecodecamp.org/images/bFeFopdYlNO0e7K93KBNclUZyhiY5OQ5z65Q)

This will create a new employee record and display the data in the view table. Add a few more records, and the view will be similar to the one shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/zscFfBz2XUJcQkWomqHYqZez9pI6sX6nXlBD)

Clicking on the Edit button will open the modal popup for editing the employee record. Edit the input fields and click on save to update the employee record.

![Image](https://cdn-media-1.freecodecamp.org/images/JzSm73w1LdEDHCFex9p8AuvfcZNEJXq30rs5)

To filter the employee records, enter the employee name in the search box and click on the Filter button. The search text is case independent. The filter operation will return all the employee records matching the name entered in the search field. Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/SWi6lzLgiTQ-4rRVRMtGX7zycc6E-xm3wvYy)

If you click on the Delete button corresponding to the employee record, it will open a delete confirmation popup asking for a confirmation to delete the employee record.

![Image](https://cdn-media-1.freecodecamp.org/images/zP0C6qdbR7jYKJZh2IzN7nKSjCHBQLGPf4ZZ)

Clicking on YES will delete the employee data and show the updated list of employees by refreshing the view table.

### Conclusion

We have created a server-side Blazor application using Entity Framework Core DB first approach with the help of Visual Studio 2017 and SQL Server 2017. We used a modal popup to handle user inputs via a form. We also implemented the search functionality on the employee records.

Please get the source code from [GitHub](https://github.com/AnkitSharma-007/Blazor-Server-Side-SPA) and play around to get a better understanding.

Get my book [Blazor Quick Start Guide](https://www.amazon.com/Blazor-Quick-Start-Guide-applications/dp/178934414X/ref=sr_1_1?ie=UTF8&qid=1542438251&sr=8-1&keywords=Blazor-Quick-Start-Guide) to learn more about Blazor.

You can check out my other articles on Blazor [here](http://ankitsharmablogs.com/category/blazor/).

Preparing for interviews? Read my article on [C# Coding Questions For Technical Interviews](http://ankitsharmablogs.com/csharp-coding-questions-for-technical-interviews/)

### See Also

* [ASP.NET Core — Getting Started With Blazor](http://ankitsharmablogs.com/asp-net-core-getting-started-with-blazor/)
* [ASP.NET Core — CRUD Using Blazor And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-blazor-and-entity-framework-core/)
* [Cascading DropDownList In Blazor Using EF Core](http://ankitsharmablogs.com/cascading-dropdownlist-in-blazor-using-ef-core/)
* [Creating an SPA Using Razor Pages With Blazor](http://ankitsharmablogs.com/creating-a-spa-using-razor-pages-with-blazor/)
* [Deploying a Blazor Application on IIS](http://ankitsharmablogs.com/deploying-a-blazor-application-on-iis/)

Originally published at [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)

