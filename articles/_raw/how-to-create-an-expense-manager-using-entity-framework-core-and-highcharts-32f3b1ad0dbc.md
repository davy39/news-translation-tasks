---
title: How to create an expense manager using Entity Framework Core and Highcharts
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-19T21:18:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-expense-manager-using-entity-framework-core-and-highcharts-32f3b1ad0dbc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Lwm464tBKse1OcAWuak1sg.png
tags:
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we will be creating a personal expense manager using ASP.NET Core
  2.1 and Entity Framework (EF) core Code First approach. This expense manager tracks
  your daily expenses and provides comparative charts to...'
---

By Ankit Sharma

### Introduction

In this article, we will be creating a personal expense manager using ASP.NET Core 2.1 and Entity Framework (EF) core Code First approach. This expense manager tracks your daily expenses and provides comparative charts to show your expense summary. We are using modal dialog to handle user inputs and to show monthly and weekly expense summary chart using Highcharts. Hence, this will be a Single Page Application (SPA).

We will be using Visual Studio 2017 and SQL Server 2017 for our demo.

Let us look at the final application:

![Image](https://cdn-media-1.freecodecamp.org/images/xO0BJntS6-EbjUgVPIHp0V7axFs1trr1eoj4)

### Prerequisites

* Install .NET Core 2.1 SDK from [here](https://www.microsoft.com/net/learn/get-started/windows#windowscmd)
* Install the latest version of Visual Studio 2017 from [here](https://visualstudio.microsoft.com/downloads/)
* SQL Server 2008 or above

### Source Code

Before proceeding, I recommend you get the source code from [GitHub](https://github.com/AnkitSharma-007/ExpenseManager-ASPCore-EFCore-Highchart).

### Create the ASP.NET Core project

Open Visual Studio and select “File” > “New” > “Project”.

After selecting the project, a “New Project” dialog will open. Select “.NET Core” in the left panel inside the Visual C# menu.

Then, select “ASP.NET Core Web Application” from the available project types. Put the name of the project as “ExpenseManager” and press “OK” to create the ASP.NET Core Project.

![Image](https://cdn-media-1.freecodecamp.org/images/BdP-AFHko5M6RuXPqwXBRJerxtTGGXrV36q7)

After clicking on OK, a new dialog will open asking you to select the project template.

You will see two drop-down menus at the top left of the template window. Select “.NET Core” and “ASP.NET Core 2.1” from these dropdowns. Then, select “Web application (Model-View-Controller)” template and press “OK”.

![Image](https://cdn-media-1.freecodecamp.org/images/sB3aRxylwpRxe2PKhpuDik35Y8f12tKJ160A)

### Adding the model to the application

Since we are using the EF core Code First approach, first we will create our model class. Then we will generate our database tables using the model.

Right click on the “Models” folder and select “Add” > “Class”. Name your class “ExpenseReport._cs_”. This class will contain our “Employee” model properties.

Open the “ExpenseReport.cs” file and put in the following code:

```cs
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Threading.Tasks;

namespace ExpenseManager.Models
{
    public class ExpenseReport
    {
        [Key]
        public int ItemId { get; set; }
        [Required]
        public string ItemName { get; set; }

        [Required]
        [DataType(DataType.Currency)]
        [Column(TypeName = "decimal(10, 2)")]
        public decimal Amount { get; set; }

        [DataType(DataType.Date)]
        [DisplayFormat(DataFormatString = "{0:MM/dd/yyyy}", ApplyFormatInEditMode = true)]
        [Required]
        public DateTime ExpenseDate { get; set; } = DateTime.Now;

        [Required]
        public string Category { get; set; }
    }
}
```

We have used the `[Key]` attribute with `ItemId` to make it the primary key while creating the database table.

### Creating the database table using the EF Core Code First approach

In order to create our tables using EF Core Code First approach, we need to install few NuGet packages.

Navigate to “Tools” > “NuGet Package Manager” > “Package Manager Console”.

We have to install the package for the database provider that we are targeting. In this case, it is SQL Server. Hence, run the following command:

```
Install-Package Microsoft.EntityFrameworkCore.SqlServer
```

Since we are using EF Tools to create a table from the existing model, we will install the Tools package as well. Run the following command:

```
Install-Package Microsoft.EntityFrameworkCore.Tools
```

After the package installations are successful, we will create a `dbcontext` class. Add a file “ExpenseDBContext.cs” in the Models folder and put in the following code:

```cs
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ExpenseManager.Models
{
    public class ExpenseDBContext : DbContext
    {
        public virtual DbSet<ExpenseReport> ExpenseReport { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
#warning To protect potentially sensitive information in your connection string, you should move it out of source code. See http://go.microsoft.com/fwlink/?LinkId=723263 for guidance on storing connection strings.
                optionsBuilder.UseSqlServer("Your connection string");
            }
        }
    }
}
```

**Do not forget** to put your own connection string (inside `“”`).

We will create a dataset migration which is used to keep the database schema in sync with the model. There is no database at this moment, so the first migration will create it, **and** add tables for the entities represented by the `DbSet` properties on the `ExpenseDBContext` that we have created.

To create the dataset migration, navigate to the project folder and open the PowerShell window. Execute the following command in it:

```
dotnet ef  migrations add ExpenseMigration
```

Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/z3Hc9XEFxvh-GjO2mv3crU58GpiCfCKptBPg)

This will create a folder named “Migrations” into our project, which contains the code for the migration **and** a model snapshot. Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/c1K51nGiW4uooQUPy9EMyRGvCXPexQEdhJe8)

Enter the following command in the PowerShell window to execute the migration:

```
dotnet ef database update
```

Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/o5iXSve2WjqSeO5gAX2x8mf6ZHptiTFjD3i8)

This will create the table “ExpenseReport” in our database that we have mentioned in the connection string. You can see that the column `ItemId` is the primary key here.

![Image](https://cdn-media-1.freecodecamp.org/images/KSFtxL-C-Bv7fwTvn2OpFwKwgXYB5ABbFql2)

Hence, the database creation is completed successfully using the EF Code First approach.

### Adding the Data Access layer to our application

Add a class file “ExpensesDataAcessLayer.cs” into the “Models” folder and put in the following code:

```cs
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ExpenseManager.Models
{
    public class ExpensesDataAcessLayer
    {
        ExpenseDBContext db = new ExpenseDBContext();
        public IEnumerable<ExpenseReport> GetAllExpenses()
        {
            try
            {
                return db.ExpenseReport.ToList();
            }
            catch
            {
                throw;
            }
        }

        // To filter out the records based on the search string 
        public IEnumerable<ExpenseReport> GetSearchResult(string searchString)
        {
            List<ExpenseReport> exp = new List<ExpenseReport>();
            try
            {
                exp = GetAllExpenses().ToList();
                return exp.Where(x => x.ItemName.IndexOf(searchString, StringComparison.OrdinalIgnoreCase) != -1);
            }
            catch
            {
                throw;
            }
        }

        //To Add new Expense record       
        public void AddExpense(ExpenseReport expense)
        {
            try
            {
                db.ExpenseReport.Add(expense);
                db.SaveChanges();
            }
            catch
            {
                throw;
            }
        }

        //To Update the records of a particluar expense  
        public int UpdateExpense(ExpenseReport expense)
        {
            try
            {
                db.Entry(expense).State = EntityState.Modified;
                db.SaveChanges();

                return 1;
            }
            catch
            {
                throw;
            }
        }

        //Get the data for a particular expense  
        public ExpenseReport GetExpenseData(int id)
        {
            try
            {
                ExpenseReport expense = db.ExpenseReport.Find(id);
                return expense;
            }
            catch
            {
                throw;
            }
        }

        //To Delete the record of a particular expense  
        public void DeleteExpense(int id)
        {
            try
            {
                ExpenseReport emp = db.ExpenseReport.Find(id);
                db.ExpenseReport.Remove(emp);
                db.SaveChanges();

            }
            catch
            {
                throw;
            }
        }

        // To calculate last six months expense
        public Dictionary<string, decimal> CalculateMonthlyExpense()
        {
            ExpensesDataAcessLayer objexpense = new ExpensesDataAcessLayer();
            List<ExpenseReport> lstEmployee = new List<ExpenseReport>();

            Dictionary<string, decimal> dictMonthlySum = new Dictionary<string, decimal>();

            decimal foodSum = db.ExpenseReport.Where
                (cat => cat.Category == "Food" && (cat.ExpenseDate > DateTime.Now.AddMonths(-7)))
                .Select(cat => cat.Amount)
                .Sum();

            decimal shoppingSum = db.ExpenseReport.Where
               (cat => cat.Category == "Shopping" && (cat.ExpenseDate > DateTime.Now.AddMonths(-7)))
               .Select(cat => cat.Amount)
               .Sum();

            decimal travelSum = db.ExpenseReport.Where
               (cat => cat.Category == "Travel" && (cat.ExpenseDate > DateTime.Now.AddMonths(-7)))
               .Select(cat => cat.Amount)
               .Sum();

            decimal healthSum = db.ExpenseReport.Where
               (cat => cat.Category == "Health" && (cat.ExpenseDate > DateTime.Now.AddMonths(-7)))
               .Select(cat => cat.Amount)
               .Sum();

            dictMonthlySum.Add("Food", foodSum);
            dictMonthlySum.Add("Shopping", shoppingSum);
            dictMonthlySum.Add("Travel", travelSum);
            dictMonthlySum.Add("Health", healthSum);

            return dictMonthlySum;
        }

        // To calculate last four weeks expense
        public Dictionary<string, decimal> CalculateWeeklyExpense()
        {
            ExpensesDataAcessLayer objexpense = new ExpensesDataAcessLayer();
            List<ExpenseReport> lstEmployee = new List<ExpenseReport>();

            Dictionary<string, decimal> dictWeeklySum = new Dictionary<string, decimal>();

            decimal foodSum = db.ExpenseReport.Where
                (cat => cat.Category == "Food" && (cat.ExpenseDate > DateTime.Now.AddDays(-7)))
                .Select(cat => cat.Amount)
                .Sum();

            decimal shoppingSum = db.ExpenseReport.Where
               (cat => cat.Category == "Shopping" && (cat.ExpenseDate > DateTime.Now.AddDays(-28)))
               .Select(cat => cat.Amount)
               .Sum();

            decimal travelSum = db.ExpenseReport.Where
               (cat => cat.Category == "Travel" && (cat.ExpenseDate > DateTime.Now.AddDays(-28)))
               .Select(cat => cat.Amount)
               .Sum();

            decimal healthSum = db.ExpenseReport.Where
               (cat => cat.Category == "Health" && (cat.ExpenseDate > DateTime.Now.AddDays(-28)))
               .Select(cat => cat.Amount)
               .Sum();

            dictWeeklySum.Add("Food", foodSum);
            dictWeeklySum.Add("Shopping", shoppingSum);
            dictWeeklySum.Add("Travel", travelSum);
            dictWeeklySum.Add("Health", healthSum);

            return dictWeeklySum;
        }
    }
}
```

This file will have methods to handle CRUD operations on our database. We are also calculating the totals for the last six months’ expenses and the last four weeks’ expenses for each category.

### Adding the controller to the application

Right click on the “Controllers” folder and select “Add” > “New Item”. An “Add New Item” dialog box will open. Select “ASP.NET Core” from the left panel, then select “Controller Class” from the templates panel, and put the name as “ExpenseController.cs”. Press “Add”.

![Image](https://cdn-media-1.freecodecamp.org/images/iS8NP1beORaP0LpY6MLAH1ygwkgRD1yDpJHU)

This will create our controller `ExpenseController` **inside** the _“_Controllers” folder. Open the “ExpenseController.cs” file and put in the following code:

```cs
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using ExpenseManager.Models;
using Microsoft.AspNetCore.Mvc;

namespace ExpenseManager.Controllers
{
    public class ExpenseController : Controller
    {
        ExpensesDataAcessLayer objexpense = new ExpensesDataAcessLayer();
        public IActionResult Index(string searchString)
        {
            List<ExpenseReport> lstEmployee = new List<ExpenseReport>();
            lstEmployee = objexpense.GetAllExpenses().ToList();

            if (!String.IsNullOrEmpty(searchString))
            {
                lstEmployee = objexpense.GetSearchResult(searchString).ToList();
            }
            return View(lstEmployee);
        }

        public ActionResult AddEditExpenses(int itemId)
        {
            ExpenseReport model = new ExpenseReport();
            if (itemId > 0)
            {
                model = objexpense.GetExpenseData(itemId);
            }
            return PartialView("_expenseForm", model);
        }

        [HttpPost]
        public ActionResult Create(ExpenseReport newExpense)
        {
            if (ModelState.IsValid)
            {
                if (newExpense.ItemId > 0)
                {
                    objexpense.UpdateExpense(newExpense);
                }
                else
                {
                    objexpense.AddExpense(newExpense);
                }
            }
            return RedirectToAction("Index");
        }

        [HttpPost]
        public IActionResult Delete(int id)
        {
            objexpense.DeleteExpense(id);
            return RedirectToAction("Index");
        }

        public ActionResult ExpenseSummary()
        {
            return PartialView("_expenseReport");
        }

        public JsonResult GetMonthlyExpense()
        {
            Dictionary<string, decimal> monthlyExpense = objexpense.CalculateMonthlyExpense();
            return new JsonResult(monthlyExpense);
        }

        public JsonResult GetWeeklyExpense()
        {
            Dictionary<string, decimal> weeklyExpense = objexpense.CalculateWeeklyExpense();
            return new JsonResult(weeklyExpense);
        }
    }
}
```

The Controller will have the methods to call our data access layer methods to handle database operations.

### Adding views to the application

We will create three view files:

1. “Index.cshtml” — this view will display all the expense data, and contains a search box to search for a particular item.
2. “_expenseForm.cshtml” — this is a partial view, which contains the form to handle user inputs. This is used for both add and edit functionality, and will be rendered in a modal dialog.
3. “_expenseReport.cshtml”:— this is also a partial view, which will show the expense summary in a bar chart using Highcharts. It is also rendered as a modal dialog.

#### Index view

To create the view file, right click on the “Index” method in our controller and select “Add View…”. This will open an “Add MVC View” dialog box. Put in the name of view as “Index” and click “Add”. **Make sure** that the “Create as a partial view” check box is **not** checked. Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/2dTGSQGR0dLh0apD3msjTibU-zxftGF4Ummi)

This will create the “Index.cshtml” file inside the “Expense” folder, under the “Views” folder. Open the “Index.cshtml” file and put in the following code:

```cs
@model IEnumerable<ExpenseManager.Models.ExpenseReport>

@{
    ViewData["Title"] = "Personal Expense Manager";
}
<link href="~/lib/bootstrap/dist/css/bootstrap.css" rel="stylesheet" />
<script src="~/lib/jquery/dist/jquery.min.js"></script>
<script src="~/lib/bootstrap/dist/js/bootstrap.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.8.0/js/bootstrap-datepicker.js"></script>
<link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.8.0/css/bootstrap-datepicker.css" rel="stylesheet">

<h2>Personal Expense Manager</h2>
<br />
<div>
    <div style="float:left">
        <button class="btn btn-primary" onclick="AddEditExpenses(0)">Add Expense</button>
        <button class="btn btn-success" onclick="ReportExpense()">Expense Report</button>
    </div>
    <div style="float:right; width:40%;">
        <form asp-controller="Expense" asp-action="Index" class="form-group">
            <div class="col-sm-6">
                <input class="form-control" type="text" name="SearchString" placeholder="Search">
            </div>
            <button type="submit" class="btn btn-default btn-info">Filter</button>
        </form>
    </div>
</div>
<br />
<br />
<table class="table">
    <thead>
        <tr>
            <th>@Html.DisplayNameFor(model => model.ItemId)</th>
            <th>@Html.DisplayNameFor(model => model.ItemName)</th>
            <th>@Html.DisplayNameFor(model => model.Amount)</th>
            <th>@Html.DisplayNameFor(model => model.ExpenseDate)</th>
            <th>@Html.DisplayNameFor(model => model.Category)</th>
            <th>Action Item</th>
        </tr>
    </thead>
    <tbody>
        @foreach (var item in Model)
        {
            <tr>
                <td>@Html.DisplayFor(modelItem => item.ItemId)</td>
                <td>@Html.DisplayFor(modelItem => item.ItemName)</td>
                <td>@Html.DisplayFor(modelItem => item.Amount)</td>
                <td>@Html.DisplayFor(modelItem => item.ExpenseDate)</td>
                <td>@Html.DisplayFor(modelItem => item.Category)</td>
                <td>
                    <button class="btn btn-default" onclick="AddEditExpenses(@item.ItemId)">Edit</button>
                    <button class="btn btn-danger" onclick="DeleteExpense(@item.ItemId)">Delete</button>
                </td>
            </tr>
        }
    </tbody>
</table>

<div class="modal fade" id="expenseFormModel" role="dialog">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <a href="#" class="close" data-dismiss="modal">&times;</a>
                <h3 id="title" class="modal-title">Add Expense</h3>
            </div>
            <div class="modal-body" id="expenseFormModelDiv">
            </div>
        </div>
    </div>
</div>

<div class="modal fade" id="expenseReportModal" role="dialog">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <a href="#" class="close" data-dismiss="modal">&times;</a>
                <h3 class="modal-title">Expense Report</h3>
            </div>
            <div class="modal-body" id="expenseReportModalDiv">
            </div>
        </div>
    </div>
</div>

<script>

    var AddEditExpenses = function (itemId) {
        var url = "/Expense/AddEditExpenses?itemId=" + itemId;
        if (itemId > 0)
            $('#title').html("Edit Expense");

        $("#expenseFormModelDiv").load(url, function () {
            $("#expenseFormModel").modal("show");

        });

        $('#expenseFormModel').on('shown.bs.modal', function () {

            $('#calender-container .input-group.date').datepicker({
                todayBtn: true,
                calendarWeeks: true,
                todayHighlight: true,
                autoclose: true,
                container: '#expenseFormModel modal-body'
            });

        });
    }

    var ReportExpense = function () {
        var url = "/Expense/ExpenseSummary";

        $("#expenseReportModalDiv").load(url, function () {
            $("#expenseReportModal").modal("show");
        })
    }

    var DeleteExpense = function (itemId) {

        var ans = confirm("Do you want to delete item with Item Id: " + itemId);

        if (ans) {
            $.ajax({
                type: "POST",
                url: "/Expense/Delete/" + itemId,
                success: function () {
                    window.location.href = "/Expense/Index";
                }
            })
        }
    }
</script>

<script>

    $('body').on('click', "#btnSubmit", function () {
        var myformdata = $("#expenseForm").serialize();

        $.ajax({
            type: "POST",
            url: "/Expense/Create",
            data: myformdata,
            success: function () {
                $("#myModal").modal("hide");
                window.location.href = "/Expense/Index";
            },
            error: function (errormessage) {
                alert(errormessage.responseText);
            }
        })
    })
</script>
```

Let us understand this code.

At the top, we have included the bootstrap and jQuery references.

After that, we have added two buttons for adding a new expense, and for creating the expense summary.

We have also included a form containing a search box to filter out the records. On clicking of “Filter” button, the form is submitted and it invokes the `Index` method in our controller — which will return the items matching the search criteria. The search functionality is provided only on the item name field.

We are using a table to display all the expense records in our database. Each record has two action buttons corresponding to it — “Edit” and “Delete”.

We have also created two modal dialogs. One is for adding/editing the expense data, and the other for displaying the expense summary report.

In the script section, we have defined an`AddEditExpenses` function. This function will be invoked when the “Add Expense” or “Edit” button is clicked. We are passing the `itemId` as the parameter in this method. If the `ItemId` value **is not set**, then it is considered an `Add` function. If the `ItemId` **is set,** then it is an `Edit` function.

We will call `AddEditExpenses` in our controller which will return the partial view “_expenseForm” and bind it to the ExpenseReport model. The modal dialog will be empty for an `Add` call and will contain the expense item data in case of an `Edit` call. We are using a bootstrap datepicker to select the expense date, hence we have set the datepicker properties on modal dialog load.

The `ReportExpense` function will call the `ExpenseSummary` method in our controller. This will return the partial view “_expenseReport” to be displayed as a modal dialog. This partial view will display the monthly and weekly expense summary chart using Highcharts.

The `DeleteExpense` function is used to delete the record of a particular expense. This will invoke the `Delete` method in our controller to remove the expense record from our database.

We are also using dynamic binding to bind the submit event of the “expenseForm” modal. This form is defined in the “_expenseForm.cshtml” view. On submitting the form, we are invoking an ajax call to the `Create` method in our controller class.

Since we are using the same form for both the `Edit` and `Add` functionality, we need to distinguish between both using the `ItemId` value. In the `Create` method of the controller, if the `ItemId` is set, then we will invoke the `UpdateExpense` method. Otherwise, the `AddExpense` method is invoked. After a successful submit, we will close the modal and redirect to the Index view to show the updated list of expenses.

#### ExpenseForm view

This is a partial view that will be displayed in a modal dialog on clicking the “Add Expense” button in the “Index” view.

To create the view file, right click anywhere inside our controller file and select “Add View…”. This will open an “Add MVC View” dialog box. Put in the name of the view as “_expenseForm” and click “Add”. **Make sure** that the “Create as a partial view” check box **is** selected. Refer to the image below:

![Image](https://cdn-media-1.freecodecamp.org/images/ahA3bCK-ViyDNYQpP6oPWGFQcy0jg9jUWu37)

Open the “_expenseForm.cshtml file” and put in the following code:

```cs
@model ExpenseManager.Models.ExpenseReport

<script src="//cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.3.0/js/bootstrap-datepicker.js"></script>
<link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.8.0/css/bootstrap-datepicker.css" rel="stylesheet">

<div>
    <div class="row">
        <div class="col-md-8">
            <form id="expenseForm">
                <input type="hidden" asp-for="ItemId" />
                <div class="form-group">
                    <label asp-for="ItemName" class="control-label"></label>
                    <input asp-for="ItemName" class="form-control" />
                </div>
                <div class="form-group">
                    <label asp-for="Category" class="control-label"></label>
                    <select asp-for="Category" class="form-control">
                        <option value="">-- Select Category --</option>
                        <option value="Food">Food</option>
                        <option value="Shopping">Shopping</option>
                        <option value="Travel">Travel</option>
                        <option value="Health">Health</option>
                    </select>
                </div>
                <div class="form-group">
                    <label asp-for="Amount" class="control-label"></label>
                    <input asp-for="Amount" class="form-control" />
                </div>
                <div class="form-group" id="calender-container">
                    <label asp-for="ExpenseDate" class="control-label"></label>
                    <div class="input-group date">
                        <input asp-for="ExpenseDate" type="text" class="form-control"><span class="input-group-addon"><i class="glyphicon glyphicon-calendar"></i></span>
                    </div>
                </div>
                <div class="form-group">
                    <button type="button" id="btnSubmit" class="btn btn-block btn-info">Save</button>
                </div>
            </form>
        </div>
    </div>
</div>
```

At the top, we are including the `cdn` reference to the bootstrap-datepicker so that we can use it in our modal dialog. Then we have a `<fo`rm> element, which binds to our model. We also h`ave a` submit button which will post the form data t`o the` Create method in our controller using an ajax call.

#### ExpenseReport view

This is a partial view that is displayed in the modal dialog on clicking the “Expense Report” button in the “Index” view.

Create a new partial view “_expenseReport.cshtml” and put in the following code:

```cs
<script src="https://code.highcharts.com/highcharts.js"></script>

<button id="btnMonthlyReport" class="btn btn-info">Monthly Report</button>
<button id="btnWeeklyReport" class="btn btn-warning">Weekly Report</button>
<div id="container" style="min-width: 400px; height: 400px; margin: 0 auto">

</div>

<script>

    $(document).ready(function () {
        $("#btnWeeklyReport").click(function () {
            var titleMessage = "Expenses in last four weeks is : ";

            $.ajax({
                type: "GET",
                url: "/Expense/GetWeeklyExpense",
                contentType: "application/json",
                dataType: "json",
                success: function (result) {
                    var keys = Object.keys(result);
                    var weeklydata = new Array();
                    var totalspent = 0.0;
                    for (var i = 0; i < keys.length; i++) {
                        var arrL = new Array();
                        arrL.push(keys[i]);
                        arrL.push(result[keys[i]]);
                        totalspent += result[keys[i]];
                        weeklydata.push(arrL);
                    }
                    createCharts(weeklydata, titleMessage, totalspent.toFixed(2));
                }
            })
        })

        $("#btnMonthlyReport").click(function () {
            var titleMessage = "Expenses in last six months is : ";

            $.ajax({
                type: "GET",
                url: "/Expense/GetMonthlyExpense",
                contentType: "application/json",
                dataType: "json",
                success: function (result) {
                    var keys = Object.keys(result);
                    var monthlydata = new Array();
                    var totalspent = 0.0;
                    for (var i = 0; i < keys.length; i++) {
                        var arrL = new Array();
                        arrL.push(keys[i]);
                        arrL.push(result[keys[i]]);
                        totalspent += result[keys[i]];
                        monthlydata.push(arrL);
                    }
                    createCharts(monthlydata, titleMessage, totalspent.toFixed(2));
                }
            })
        })
    })

    function createCharts(sum, titleText, totalspent) {
        Highcharts.chart('container', {
            chart: {
                type: 'column'
            },
            title: {
                text: titleText + ' ' + totalspent
            },
            xAxis: {
                type: 'category',
                labels: {
                    rotation: -45,
                    style: {
                        fontSize: '13px',
                        fontFamily: 'Verdana, sans-serif'
                    }
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: 'Money spent'
                }
            },
            legend: {
                enabled: false
            },
            tooltip: {
                pointFormat: 'Total money spent: <b>{point.y:.2f} </b>'
            },
            series: [{
                type: 'column',
                data: sum,
            }]
        });
    }

</script>
```

At the top, we included the `cdn` reference to Highcharts. We have also provided two buttons. One is used to view a monthly report of the last six months. The other is to view a weekly report for the last four weeks. The report will be generated as a bar chart to provide a comparative study of expense summaries.

On clicking the weekly report button, we will invoke the `GetWeeklyExpense` method of our controller. This will return the data in JSON format. We will pass this data to the `createCharts` function to create the weekly expense bar chart using Highcharts.

Similarly, we will invoke the `GetMonthlyExpense` method of our controller on clicking the “Monthly Report” button. The JSON result will be passed to the `createCharts` function to create the monthly expense bar chart using Highcharts.

### Configure route URL

Open the “Startup.cs” file to set the format for app routes. Scroll down to the `app.UseMvc` method where you can set the route URL.

Make sure that your route URL is set like this:

```cs
app.UseMvc(routes =>
{
    routes.MapRoute(
        name: "default",
        template: "{controller=Expense}/{action=Index}");
});
```

This URL pattern sets `ExpenseController` as the default controller and the `Index` method as the default action method. Default route parameters need not be present in the URL path for a match.

If we do not append any controller name in the URL, then it will take `ExpenseController` as the default controller and the `Index` method of `ExpenseController` as default action method.

Similarly, if we append only `/Expense` to the URL, it will navigate to the `Index` action method of the Expense controller.

### Execution demo

Press F5 to launch the application. You can see a page similar to the one shown below:

![Image](https://cdn-media-1.freecodecamp.org/images/5HefeZhwLyl19br2rRQfo9jG7cFbASxDk77m)

Here we have an “Add Expense” button to add a new expense report. The “Expense Report” button will open a dialog box to show the bar chart of monthly and weekly expense data. On the top right corner, we have a search box to search the records using item name.

Look at the below GIF image for the demo of application:

![Image](https://cdn-media-1.freecodecamp.org/images/puUdMVO3Vug0wmuTAMxsLEGjbbOW-kIrP-12)

### Conclusion

We created a personal expense manager application using ASP.NET Core and Entity Framework Core with the help of Visual Studio 2017 and SQL Server 2017. We have also used Highcharts to create a bar chart for monthly and weekly expense summary.

Please download the source code from [GitHub](https://github.com/AnkitSharma-007/ExpenseManager-ASPCore-EFCore-Highchart) and play around to get a better understanding.

You can read my other articles on ASP .NET Core [here](http://ankitsharmablogs.com/category/asp-net-core/).

Are you preparing for interviews? Read my article on [C# Coding Questions For Technical Interviews](http://ankitsharmablogs.com/csharp-coding-questions-for-technical-interviews/).

### Other useful resources

* [CRUD Operation With ASP.NET Core MVC Using Visual Studio Code and EF](http://ankitsharmablogs.com/crud-operation-asp-net-core-mvc-using-visual-studio-code-ef/)
* [ASP.NET Core — CRUD With React.js And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-with-react-js-and-entity-framework-core/)
* [ASP.NET Core — CRUD Using Angular 5 And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-angular-5-and-entity-framework-core/)
* [CRUD Operation With ASP.NET Core MVC Using ADO.NET and Visual Studio 2017](http://ankitsharmablogs.com/crud-operation-with-asp-net-core-mvc-using-ado-net/)
* [CRUD Operation With ASP.NET Core MVC using Visual Studio Code and ADO.NET](http://ankitsharmablogs.com/crud-operation-with-asp-net-core-mvc-using-visual-studio-code-and-ado-net/)
* [ASP.NET Core — Using Highcharts With Angular 5](http://ankitsharmablogs.com/asp-net-core-using-highcharts-with-angular-5/)

Originally published at [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)

