---
title: How to perform CRUD operations using Blazor with MongoDB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-01T16:04:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-perform-crud-operations-using-blazor-with-mongodb-8ee216ad513e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wQLUVCBOZVZo-PxJLLdrzQ.gif
tags:
- name: JavaScript
  slug: javascript
- name: MongoDB
  slug: mongodb
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we will create a Blazor application using MongoDB as our database
  provider. We will create a Single Page Application (SPA) and perform CRUD operations
  on it. A modal popup will display the form to handle ...'
---

By Ankit Sharma

### Introduction

In this article, we will create a Blazor application using MongoDB as our database provider. We will create a Single Page Application (SPA) and perform CRUD operations on it. A modal popup will display the form to handle the user inputs. The form also has a dropdown list, which will bind to a DB collection.

We will use Visual Studio 2017 and MongoDB 4.0.

Take a look at the final application.

![Image](https://cdn-media-1.freecodecamp.org/images/VtnrpPoR5nyDc5lkeDMM54y45KfjCfL0defG)

### Prerequisites

* Install the .NET Core 2.1 or above SDK from [here](https://www.microsoft.com/net/learn/get-started-with-dotnet-tutorial#windowscmd)
* Install Visual Studio 2017 v15.7 or above from [here](https://www.visualstudio.com/downloads/)
* Install ASP.NET Core Blazor Language Services extension from [here](https://marketplace.visualstudio.com/items?itemName=aspnet.blazor)
* Download and install MongoDB community edition. You can find the installation guide [here](https://docs.mongodb.com/manual/administration/install-community/).

Visual Studio 2017 versions below v15.7 do not support Blazor framework.

### Source Code

Get the source code from [GitHub](https://github.com/AnkitSharma-007/Blazor-CRUD-With-MongoDB).

### Configuring MongoDB

After installing the MongoDB, we need to add the path of MongoDB binaries to the System PATH variable. The default installation path in a Windows machine is `C:\Program Files\MongoDB`. Hence you need to include `C:\Program Files\MongoDB\Server\4.0\bin` in the System PATH variable. If you are not using Windows then you can find the process of configuring the MongoDB binaries at the installation guide link provided in the prerequisites section above.

### Working With MongoDB

We need to set up the path where the data will be stored in our machine. Open the command prompt as administrator and run the following command to set the data storage path in your machine.

```
mongod --dbpath C:\MongoData
```

You can provide the path of any folder where you want to store the data. This command will connect to MongoDB on port 27017 (the default port for MongoDB connection). Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/LoKmouJOGBC6qO8YNmPysnVN-V0J7Fa7N6nP)

**Important Note:**

> _It is advisable to use the command prompt over PowerShell while executing MongoDB commands as all MongoDB commands do not work in PowerShell._

Open a new command prompt window and execute the command `mongo` to start the mongo server. Refer to the image below.

![Image](https://cdn-media-1.freecodecamp.org/images/sZPec9cuTRIYkXI2lNnMtMsrSRIDq0uj8SNz)

Run the following command to create the database:

```
use EmployeeDB
```

This will create our database `EmployeeDB`. Execute the following command to create a new collection inside the database:

```
db.createCollection('EmployeeRecord')
```

This will create a collection `EmployeeRecord` in our database. MongoDB stores data in JSON-like documents. Let us insert a sample document in our `EmployeeRecord` collection. Run the following command.

```
db.EmployeeRecord.insert({'Name':'Ankit','Gender':'Male','Department':'HR','City':'Mumbai'})
```

You can observe that we have provided the data in a JSON format as a key-value pair. Run the following command to list all the documents from the EmployeeRecord collection.

```
db.EmployeeRecord.find({})
```

The database schema will add _id property to each document in the collection. This property is of type ObjectId and it will be generated automatically. We will use this _id property to uniquely identify a document in the collection. Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/F1PYd2lqR1RAF7g9Y7vB0y0vi4OdKoXwOnjL)

If you want to remove all the documents from the EmployeeRecord collection then you need to run the following command:

```
db.EmployeeRecord.remove({})
```

We will create another collection to store a list of city names which is used to populate the City field of `EmployeeRecord` collection. We will also bind this collection to a dropdown list in our web application from which the user will select the desired city.

Run the following command to create the `Cities` collection.

```
db.createCollection('Cities')
```

We will insert five sample city names in this collection. To insert the documents in bulk in the `Cities` collection, run the following command:

```
db.Cities.insertMany([   { CityName : "New Delhi" },   { CityName : "Mumbai"},   { CityName : "Hyderabad"},   { CityName : "Chennai"},   { CityName : "Bengaluru" }])
```

Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/wYdXE-rZ2FscqYR1-pN5f8-cXof9pU-O0ijq)

### Create a Blazor Web Application

Open Visual Studio and select File >> New >> Project.

After selecting the project, a “New Project” dialog will open. Select .NET Core inside Visual C# menu from the left panel. Then, select “ASP.NET Core Web Application” from available project types. Put the name of the project as `BlazorWithMongo` and press OK.

![Image](https://cdn-media-1.freecodecamp.org/images/xghuCK555DbyDnK9k6AdshsxqZpyGhyir1S0)

After clicking on OK, a new dialog will open asking you to select the project template. You can observe two drop-down menus at the top left of the template window. Select “.NET Core” and “ASP.NET Core 2.0” from these dropdowns. Then, select “Blazor (ASP .NET Core hosted)” template and press OK.

![Image](https://cdn-media-1.freecodecamp.org/images/XZgVOb9wpPPpoVgM43XToSbehGqTU2d52Q-7)

Now, our Blazor solution will be created. You can observe that we have three project files created in this solution

1. BlazorWithMongo.Client — It has the client side code and contains the pages that will be rendered on the browser.
2. BlazorWithMongo.Server — It has the server side codes such as data access layer and web API.
3. BlazorWithMongo.Shared — It contains the shared code that can be accessed by both client and server. It contains our Model class and DB context class.

### Installing MongoDB driver

To access the MongoDB from our application we need to install the MongoDB driver using package manager console. We will install it in BlazorWithMongo.Shared project so that it can be accessible to Server project also.

Navigate to Tools >> NuGet Package Manager >> Package Manager Cons`ole. Select BlazorWith`Mongo.Shared from Default project drop-down and run the following command:

```
Install-Package MongoDB.Driver
```

Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/emAD07arocn53VcdFKVSeNCdf3ipQTH5QBJk)

### Creating the Model

We will create our model class in `BlazorWithMongo.Shared` project. Right click on `BlazorWithMongo.Shared` and select Add >> New Folder. Name the folder as Models. Again, right click on the Models folder and select Add >> Class to add a new class file. Put the name of your class as Employee.cs and click Add.

Open the Employee.cs class and put the following code into it.

```
using System;using System.Collections.Generic;using System.Text;using MongoDB.Bson;using MongoDB.Bson.Serialization.Attributes;namespace BlazorWithMongo.Shared.Models{    public class Employee    {        [BsonId]        [BsonRepresentation(BsonType.ObjectId)]        public string Id { get; set; }        public string Name { get; set; }        public string City { get; set; }        public string Department { get; set; }        public string Gender { get; set; }    }}
```

We have included the Id property of the type ObjectId in our class definition and decorated it with `[BsonId]` attribute. This property is required to map the model objects to the MongoDB collection.

Similarly, create another class file `Cities.cs` and put the following code into it.

```
using System;using System.Collections.Generic;using System.Text;using MongoDB.Bson;using MongoDB.Bson.Serialization.Attributes;namespace BlazorWithMongo.Shared.Models{    public class Cities    {        [BsonId]        [BsonRepresentation(BsonType.ObjectId)]        public string Id { get; set; }        public string CityName { get; set; }    }}
```

### Creating the DB context class

Add a new class file to the Models folder and name it `EmployeeDBContext.cs`. Put the following code into it:

```
using MongoDB.Driver;using System;using System.Collections.Generic;using System.Text;namespace BlazorWithMongo.Shared.Models{    public class EmployeeDBContext    {        private readonly IMongoDatabase _mongoDatabase;        public EmployeeDBContext()        {            var client = new MongoClient("mongodb://localhost:27017");            _mongoDatabase = client.GetDatabase("EmployeeDB");        }        public IMongoCollection<Employee> EmployeeRecord        {            get            {                return _mongoDatabase.GetCollection<Employee>("EmployeeRecord");            }        }        public IMongoCollection<Cities> CityRecord        {            get            {                return _mongoDatabase.GetCollection<Cities>("Cities");            }        }    }}
```

Here we have defined a `MongoClient` which will connect to the MongoDB server instance using the default connection string for MongoDB. We are using the GetDatabase method to fetch the database instance. The method `EmployeeRecord` is used to fetch the `EmployeeRecord` collection from our database and map it to the Employee model class. Similarly, the method `CityRecord` will fetch the Cities collection from the database and map it to the Cities model class.

### Creating Data Access Layer for the Application

Right-click on `BlazorWithMongo.Server` project and then select Add >> New Folder and name the fold_er as Data_Access. We will be adding our class to handle database related operations inside this folder only.

Right click on _DataAccess_ folder and select Add >> Class. Name your `class EmployeeDataAccessLa`_ye_r.cs. `Open EmployeeDataAccessLa`yer.cs and put the following code into it:

```
using BlazorWithMongo.Shared.Models;using MongoDB.Driver;using System;using System.Collections.Generic;using System.Linq;using System.Threading.Tasks;namespace BlazorWithMongo.Server.DataAccess{    public class EmployeeDataAccessLayer    {        EmployeeDBContext db = new EmployeeDBContext();        //To Get all employees details               public List<Employee> GetAllEmployees()        {            try            {                return db.EmployeeRecord.Find(_ => true).ToList();            }            catch            {                throw;            }        }        //To Add new employee record               public void AddEmployee(Employee employee)        {            try            {                db.EmployeeRecord.InsertOne(employee);            }            catch            {                throw;            }        }        //Get the details of a particular employee              public Employee GetEmployeeData(string id)        {            try            {                FilterDefinition<Employee> filterEmployeeData = Builders<Employee>.Filter.Eq("Id", id);                return db.EmployeeRecord.Find(filterEmployeeData).FirstOrDefault();            }            catch            {                throw;            }        }        //To Update the records of a particular employee              public void UpdateEmployee(Employee employee)        {            try            {                db.EmployeeRecord.ReplaceOne(filter: g => g.Id == employee.Id, replacement: employee);            }            catch            {                throw;            }        }        //To Delete the record of a particular employee              public void DeleteEmployee(string id)        {            try            {                FilterDefinition<Employee> employeeData = Builders<Employee>.Filter.Eq("Id", id);                db.EmployeeRecord.DeleteOne(employeeData);            }            catch            {                throw;            }        }        // To get the list of Cities          public List<Cities> GetCityData()        {            try            {                return db.CityRecord.Find(_ => true).ToList();            }            catch            {                throw;            }        }    }}
```

Here we have defined the methods to perform CRUD operations on the EmployeeDB database.

### Adding the web API Controller to the Application

Right-click on `BlazorWithMongo.Server/Controllers` folder and select Add >> New Item. An “Add New Item” dialog box will open. S_ele_ct Web from the left panel, then select “API Controller Class” from the templates panel and put the na`me as EmployeeControl`ler.cs. Click Add.

![Image](https://cdn-media-1.freecodecamp.org/images/J1T5eoviTbmZyzQ84E99r7MxOhxQGHQXA2dk)

This will create our API _EmployeeController_ class. We will call the methods of _EmployeeDataAccessLayer_ class to fetch data and pass on the data to the client side

Open `EmployeeController.cs` file and put the following code into it:

```
using System;using System.Collections.Generic;using System.Linq;using System.Threading.Tasks;using BlazorWithMongo.Server.DataAccess;using BlazorWithMongo.Shared.Models;using Microsoft.AspNetCore.Mvc;namespace BlazorWithMongo.Server.Controllers{    public class EmployeeController : Controller    {        EmployeeDataAccessLayer objemployee = new EmployeeDataAccessLayer();        [HttpGet]        [Route("api/Employee/Index")]        public IEnumerable<Employee> Index()        {            return objemployee.GetAllEmployees();        }        [HttpPost]        [Route("api/Employee/Create")]        public void Create([FromBody] Employee employee)        {            objemployee.AddEmployee(employee);        }        [HttpGet]        [Route("api/Employee/Details/{id}")]        public Employee Details(string id)        {            return objemployee.GetEmployeeData(id);        }        [HttpPut]        [Route("api/Employee/Edit")]        public void Edit([FromBody]Employee employee)        {            objemployee.UpdateEmployee(employee);        }        [HttpDelete]        [Route("api/Employee/Delete/{id}")]        public void Delete(string id)        {            objemployee.DeleteEmployee(id);        }        [HttpGet]        [Route("api/Employee/GetCities")]        public List<Cities> GetCities()        {            return objemployee.GetCityData();        }    }}
```

We have now finished the coding for our backend logic. Therefore, we will now proceed to code our client side.

### Creating the View Component

We will add the view page in `BlazorWithMongo.Client/Pages` folder. By default, we have “Counter” and “Fetch Data” pages provided in our application. These default pages will not affect our application. For the sake of this tutorial, we will delete _fetchdata_ and _counter_ pages from this folder.

Right-click on `BlazorWithMongo.Client/Pages` folder and then select Add >> New Item. An “Add New Item” dialog box will open. Select “ASP.NET Core” from the left panel. Then select “Razor Page” from templates panel and na`me it EmployeeData.`cshtml. Click Add. Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/Q6RqbEEXFCYIUCKmXLucA1NaNoQyquSOKdSf)

This will add an `EmployeeData.cshtml` page to our `BlazorSPA.Client/Pages` folder. This razor page will have two files – _EmployeeData.cshtml_ and _EmployeeData.cshtml.cs._

Now, we will add code to these pages.

### EmployeeData.cshtml

Open `EmployeeData.cshtml` page and put the following code into it:

```
@page "/fetchemployee"@inherits EmployeeDataModel<h1>Employee Data</h1><h3>CRUD operation with Blazor using MongoDB</h3><br /><div>    <div style="float:left">        <button class="btn btn-primary" onclick="@AddEmp">Add Employee</button>    </div></div><br />@if (empList == null){    <p><em>Loading...</em></p>}else{    <table class='table'>        <thead>            <tr>                <th>Name</th>                <th>Gender</th>                <th>Department</th>                <th>City</th>            </tr>        </thead>        <tbody>            @foreach (var emp in empList)            {                <tr>                    <td>@emp.Name</td>                    <td>@emp.Gender</td>                    <td>@emp.Department</td>                    <td>@emp.City</td>                    <td>                        <button class="btn btn-info" onclick="@(async () => await EditEmployee(@emp.Id))">Edit</button>                        <button class="btn btn-danger" onclick="@(async () => await DeleteConfirm(@emp.Id))">Delete</button>                    </td>                </tr>            }        </tbody>    </table>    if (isAdd)    {        <div class="modal" tabindex="-1" style="display:block" role="dialog">            <div class="modal-dialog">                <div class="modal-content">                    <div class="modal-header">                        <h3 class="modal-title">@modalTitle</h3>                        <button type="button" class="close" onclick="@closeModal">                            <span aria-hidden="true">X</span>                        </button>                    </div>                    <div class="modal-body">                        <form>                            <div class="form-group">                                <label for="Name" class="control-label">Name</label>                                <input for="Name" class="form-control" bind="@emp.Name" />                            </div>                            <div class="form-group">                                <label asp-for="Gender" class="control-label">Gender</label>                                <select asp-for="Gender" class="form-control" bind="@emp.Gender">                                    <option value="">-- Select Gender --</option>                                    <option value="Male">Male</option>                                    <option value="Female">Female</option>                                </select>                            </div>                            <div class="form-group">                                <label asp-for="Department" class="control-label">Department</label>                                <input asp-for="Department" class="form-control" bind="@emp.Department" />                            </div>                            <div class="form-group">                                <label asp-for="City" class="control-label">City</label>                                <select asp-for="City" class="form-control" bind="@emp.City">                                    <option value="">-- Select City --</option>                                    @foreach (var city in cityList)                                    {                                        <option value="@city.CityName">@city.CityName</option>                                    }                                </select>                            </div>                        </form>                    </div>                    <div class="modal-footer">                        <button class="btn btn-block btn-success" onclick="@(async () => await SaveEmployee())" data-dismiss="modal">Save</button>                    </div>                </div>            </div>        </div>    }    if (isDelete)    {        <div class="modal" tabindex="-1" style="display:block" role="dialog">            <div class="modal-dialog">                <div class="modal-content">                    <div class="modal-header">                        <h3 class="modal-title">Delete Employee</h3>                    </div>                    <div class="modal-body">                        <h4>Do you want to delete this employee ??</h4>                        <table class="table">                            <tr>                                <td>Name</td>                                <td>@emp.Name</td>                            </tr>                            <tr>                                <td>Gender</td>                                <td>@emp.Gender</td>                            </tr>                            <tr>                                <td>Department</td>                                <td>@emp.Department</td>                            </tr>                            <tr>                                <td>City</td>                                <td>@emp.City</td>                            </tr>                        </table>                    </div>                    <div class="modal-footer">                        <button class="btn btn-danger" onclick="@(async () => await DeleteEmployee(emp.Id))" data-dismiss="modal">YES</button>                        <button class="btn btn-warning" onclick="@closeModal">NO</button>                    </div>                </div>            </div>        </div>    }}
```

Let us understand this code. At the top we have defined the route of this page as “/fetchemployee”. This means if we append “/fetchemployee” to the root URL of the app, we will be redirected to this page.

We are also inheriting `EmployeeDataModel` class, which is defined in `EmployeeData.cshtml.cs` file. This will allow us to use the methods defined in `EmployeeDataModel` class.

After this, we have defined a button to add a new employee record. When clicked, this button will open a modal popup to handle the user inputs.

The list of employee documents returned from the database is stored in the _empList_ variable. If the variable is not null then we will bind the values to a table to display the employee documents in a tabular fashion. Each row in the table has two action links. _Edit_ to edit the employee document. _Delete_ to delete the employee document.

To handle the user inputs we are using a form. We are using a single form for both Add Employee and Edit Employee functionality. The form is defined in a modal popup and the modal popup is displayed on the screen based on the value of a Boolean property isAdd. The value of this Boolean property is set in the code behind (.cshtml.cs) page.

The City dropdown list inside the form is binding to our Cities collection in the database with the help of _cityList_ variable. The cityList will be populated as the application boots up.

The form will have a _Save_ button which will invoke `SaveEmployee` method. This method is defined in the code behind file to Add or Update an employee document.

Similar to the _Add_ modal popup, we also have a _Delete_ modal popup. It will be a read-only modal and will ask for a confirmation to delete an employee document. Upon clicking “Yes”, it will invoke the `DeleteEmployee` method to delete the employee document.

### EmployeeData.cshtml.cs

Open `EmployeeData.cshtml.cs` and put the following code into it:

```
using System;using System.Collections.Generic;using System.Linq;using System.Threading.Tasks;using System.Net.Http;using Microsoft.AspNetCore.Blazor;using Microsoft.AspNetCore.Blazor.Components;using BlazorWithMongo.Shared.Models;namespace BlazorWithMongo.Client.Pages{    public class EmployeeDataModel : BlazorComponent    {        [Inject]        protected HttpClient Http { get; set; }        protected List<Employee> empList;        protected List<Cities> cityList = new List<Cities>();        protected Employee emp = new Employee();        protected string modalTitle { get; set; }        protected Boolean isDelete = false;        protected Boolean isAdd = false;        protected string SearchString { get; set; }        protected override async Task OnInitAsync()        {            await GetEmployee();            await GetCities();        }        protected async Task GetEmployee()        {            empList = await Http.GetJsonAsync<List<Employee>>("api/Employee/Index");        }        protected async Task GetCities()        {            cityList = await Http.GetJsonAsync<List<Cities>>("api/Employee/GetCities");        }        protected void AddEmp()        {            emp = new Employee();            this.modalTitle = "Add Employee";            this.isAdd = true;        }        protected async Task EditEmployee(string ID)        {            emp = await Http.GetJsonAsync<Employee>("/api/Employee/Details/" + ID);            this.modalTitle = "Edit Employee";            this.isAdd = true;        }        protected async Task SaveEmployee()        {            if (emp.Id != null)            {                await Http.SendJsonAsync(HttpMethod.Put, "api/Employee/Edit", emp);            }            else            {                await Http.SendJsonAsync(HttpMethod.Post, "/api/Employee/Create", emp);            }            this.isAdd = false;            await GetEmployee();        }        protected async Task DeleteConfirm(string ID)        {            emp = await Http.GetJsonAsync<Employee>("/api/Employee/Details/" + ID);            this.isDelete = true;        }        protected async Task DeleteEmployee(string ID)        {            await Http.DeleteAsync("api/Employee/Delete/" + ID);            this.isDelete = false;            await GetEmployee();        }        protected void closeModal()        {            this.isAdd = false;            this.isDelete = false;        }    }}
```

In this file, we have defined a class `EmployeeDataModel` that will hold all the methods that we will be using in `EmployeeData.cshtml` page. We are also injecting the `HttpClient` service to enable web API calls.

The variables _empList_ and _cityList_ are defined to hold the data from the Employee table and Cities table respectively. The variables are getting populated inside the OnInitAsync to make sure that the data is available to us as the page loads.

Clicking on the “Add Employee” button will invoke the `AddEmp` method. It will initialize an empty instance of Employee model and set the value of _isAdd_ Boolean flag to true. This will open a modal popup with a form, asking the user to enter the value for a new employee document. Similarly, we have defined an `EditEmployee` method, which will fetch the record of the employee based on the Id for which it is invoked. It will also set the value of _isAdd_ to true to open the modal popup to edit the employee document.

The `SaveEmployee` method will check if it is invoked to add a new employee record or to edit an existing employee record. If the Id is not null, then it is an “edit” request and we will send a PUT request to the Web API to update the existing employee document.

If the Id is null, then it is a “create” request and we will send a POST request to the Web API to create a new employee document.

We will then fetch the updated list of employee documents by calling `GetEmployee` method. We also set the value of _isAdd_ to false, thus closing the modal popup.

The `DeleteConfirm` method is invoked by clicking the Delete button corresponding to an employee record. It will set the value of isDelete Boolean flag to true, which will display a Delete confirmation modal popup. Upon clicking YES inside this popup, `DeleteEmployee` method is invoked. It sends a Delete Web API call to delete the employee document. It also sets the _isDelete_ Boolean flag to false thus closing the modal popup.

### Adding Link to Navigation menu

The last step is to add the link to our “EmployeeData” page in the navigation menu. Open the `BlazorWithMongo/Shared/NavMenu.cshtml` page and put the following code into it.

```
<div class="top-row pl-4 navbar navbar-dark">    <a class="navbar-brand" href="">BlazorWithMongo</a>    <button class="navbar-toggler" onclick=@ToggleNavMenu>        <span class="navbar-toggler-icon"></span>    </button></div><div class=@(collapseNavMenu ? "collapse" : null) onclick=@ToggleNavMenu>    <ul class="nav flex-column">        <li class="nav-item px-3">            <NavLink class="nav-link" href="" Match=NavLinkMatch.All>                <span class="oi oi-home" aria-hidden="true"></span> Home            </NavLink>        </li>        <li class="nav-item px-3">            <NavLink class="nav-link" href="fetchemployee">                <span class="oi oi-list-rich" aria-hidden="true"></span> Employee data            </NavLink>        </li>    </ul></div>@functions {bool collapseNavMenu = true;void ToggleNavMenu(){    collapseNavMenu = !collapseNavMenu;}}
```

Hence, we have successfully created a Single Page Application (SPA) using Blazor with the help of MongoDB as the database provider.

### Execution Demo

Press F5 to launch the application.

A web page will open as shown in the image below. The navigation menu on the left is showing the navigation link for the Employee data page.

![Image](https://cdn-media-1.freecodecamp.org/images/ss83hFQ3sh7bAKrlYgxPn7V6I4uoQCaWnlsu)

Click on “Employee data” link, it will redirect to EmployeeData view. Here you can see all the employee data in a tabular fashion. Notice the URL has “/fetchemployee” appended to it.

![Image](https://cdn-media-1.freecodecamp.org/images/2pLLNuvyTz2aH8f4BBTCtwVdC6kC-u84QPRm)

Click on the _Add Employee_ button to open the “Add Employee” modal popup. Enter the data in all the fields and click on Save to create a new employee document.

![Image](https://cdn-media-1.freecodecamp.org/images/U29tFaA9kmEvateUk-Or3uQCf2xd-3tHpRQ7)

This will create a new employee document and display the data in the View table. Click on Edit button corresponding to any row in the table, it will again open the modal popup for editing the employee record. Edit the input fields and click on save to update the employee document.

![Image](https://cdn-media-1.freecodecamp.org/images/nzPHXVURlvoAMEF02Nv817GeNtGbS4o08Fa3)

If you click on the Delete button corresponding to the employee record, it will open a delete confirmation popup asking for a confirmation to delete the employee record.

![Image](https://cdn-media-1.freecodecamp.org/images/6BBQF2IqYhIJVdkDdxKTtFliZ0yql3mfkAvt)

Clicking on YES will delete the employee data and show the updated list of employees by refreshing the view table.

### Conclusion

We have created a Single Page Application (SPA) using Blazor with the help of MongoDB as the database provider. We created a sample employee record management system and performed CRUD operations on it. To handle the user input, we used a form in a modal popup. We have used Visual Studio 2017 and MongoDB 4.0 for our demo.

Please get the source code from [GitHub](https://github.com/AnkitSharma-007/Blazor-CRUD-With-MongoDB) and play around to get a better understanding.

Get my book [Blazor Quick Start Guide](https://www.amazon.com/Blazor-Quick-Start-Guide-applications/dp/178934414X/ref=sr_1_1?ie=UTF8&qid=1542438251&sr=8-1&keywords=Blazor-Quick-Start-Guide) to learn more about Blazor.

You can check out my other articles [here](http://ankitsharmablogs.com/).

Preparing for interviews? Read my article on [C# Coding Questions For Technical Interviews](http://ankitsharmablogs.com/csharp-coding-questions-for-technical-interviews/).

### See Also

* [Understanding Server-Side Blazor](http://ankitsharmablogs.com/understanding-server-side-blazor/)
* [Single Page Application Using Server-Side Blazor](http://ankitsharmablogs.com/single-page-application-using-server-side-blazor/)
* [Creating a SPA Using Razor Pages With Blazor](http://ankitsharmablogs.com/creating-a-spa-using-razor-pages-with-blazor/)
* [ASP.NET Core — CRUD Using Blazor And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-blazor-and-entity-framework-core/)
* [Deploying a Blazor Application on IIS](http://ankitsharmablogs.com/deploying-a-blazor-application-on-iis/)
* [JavaScript Interop in Blazor](http://ankitsharmablogs.com/javascript-interop-in-blazor/)

Originally published at [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)

