---
title: Comment effectuer des opérations CRUD avec ASP.NET Core en utilisant VS Code
  et ADO.NET
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T19:46:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-perform-crud-operations-with-asp-net-core-using-vs-code-and-ado-net-b12404aef708
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BRbi2bxkmtZNcrnmaSFqUw.jpeg
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment effectuer des opérations CRUD avec ASP.NET Core en utilisant VS
  Code et ADO.NET
seo_desc: 'By Ankit Sharma

  Introduction

  In this article we are going to create a web application using ASP.NET Core MVC
  with the help of Visual Studio Code and ADO.NET. We will be creating a sample Employee
  Record Management System and performing CRUD operation...'
---

Par Ankit Sharma

### Introduction

Dans cet article, nous allons créer une application web en utilisant ASP.NET Core MVC avec l'aide de Visual Studio Code et ADO.NET. Nous allons créer un système de gestion des dossiers des employés et effectuer des opérations CRUD dessus.

Nous utiliserons VS Code et SQL Server pour notre démonstration.

### Prérequis

* Installer le SDK .NET Core 2.0.0 ou supérieur depuis [ici](https://www.microsoft.com/net/core#windowscmd)
* Télécharger et installer Visual Studio Code depuis [ici](https://code.visualstudio.com/)
* SQL Server 2008 ou supérieur

### Code Source

Avant de continuer, je vous recommande de télécharger le code source depuis [GitHub](https://github.com/AnkitSharma-007/CRUD.With.VSCode.ADO).

### Création de la Table et des Procédures Stockées

Nous allons utiliser une table de base de données pour stocker tous les enregistrements des employés.

Ouvrez SQL Server et utilisez le script suivant pour créer la table **tblEmployee**.

```
Create table tblEmployee(
    EmployeeId int IDENTITY(1,1) NOT NULL,
    Name varchar(20) NOT NULL,
    City varchar(20) NOT NULL,
    Department varchar(20) NOT NULL,
    Gender varchar(6) NOT NULL
)
```

Maintenant, nous allons créer des procédures stockées pour ajouter, supprimer, mettre à jour et obtenir les données des employés.

#### Pour Insérer un Enregistrement d'Employé

```
Create procedure spAddEmployee
(
    @Name VARCHAR(20),
    @City VARCHAR(20),
    @Department VARCHAR(20),
    @Gender VARCHAR(6)
)
as
Begin
    Insert into tblEmployee (Name,City,Department, Gender)
    Values (@Name,@City,@Department, @Gender)
End
```

#### Pour Mettre à Jour un Enregistrement d'Employé

```
Create procedure spUpdateEmployee
(
    @EmpId INTEGER ,
    @Name VARCHAR(20),
    @City VARCHAR(20),
    @Department VARCHAR(20),
    @Gender VARCHAR(6)
)
as
begin
    Update tblEmployee
    set Name=@Name,
    City=@City,
    Department=@Department,
    Gender=@Gender
    where EmployeeId=@EmpId
End
```

#### Pour Supprimer un Enregistrement d'Employé

```
Create procedure spDeleteEmployee
(
    @EmpId int
)
as
begin
    Delete from tblEmployee where EmployeeId=@EmpId
End
```

#### Pour Voir tous les Enregistrements d'Employés

```
Create procedure spGetAllEmployees
as
Begin
    select *
    from tblEmployee
    order by EmployeeId End
```

Maintenant, notre partie base de données est terminée. Nous allons donc procéder à la création de l'application MVC en utilisant Visual Studio code.

### Créer l'Application Web MVC

Nous allons créer un projet source à partir de la fenêtre de terminal dans Visual Studio Code. Ouvrez VS code et naviguez vers view >> Integrated Terminal.

![Image](https://cdn-media-1.freecodecamp.org/images/ozt7SgV0eV7boyC5xE220nW4-IBY3FDvxrYM)

Cela ouvrira la fenêtre de terminal comme montré dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/PMh7C3wCuPVBVh5m3I4mn4aqkEdnWOUeZCWY)

Tapez la séquence de commandes suivante dans la fenêtre de terminal. Cela créera notre application MVC « MvcAdoDemo ».

* mkdir MvcAdoDemo
* cd MvcAdoDemo
* dotnet new mvc

![Image](https://cdn-media-1.freecodecamp.org/images/Hqm1Tlz2cGibvb7TzOvMYvAoj6l147NLWyAL)

Ouvrez maintenant ce fichier de projet « MvcAdoDemo » en utilisant VS code. Si un message s'affiche « Required assets to build and debug are missing from MvcAdoDemo. Add them? », sélectionnez « Yes ».

![Image](https://cdn-media-1.freecodecamp.org/images/KMYb7f5vUhpAUDnJnRhLyfh5CejGTlg9pvhS)

Vous pouvez observer dans l'explorateur de solutions que nous avons déjà des dossiers créés avec les noms Controllers, Models et Views. Nous ajouterons nos fichiers de code dans ces dossiers uniquement.

### Ajout du Modèle à l'Application

Faites un clic droit sur le dossier Models et sélectionnez « New File ». Nommez-le **Employee.cs**. Cela créera un fichier à l'intérieur du dossier Models.

![Image](https://cdn-media-1.freecodecamp.org/images/IJ01dH2qDOQ1SCcChQ-q5axA7RX6o6T50XjI)

Ajoutez un autre fichier au dossier Models. Nommez-le **EmployeeDataAccessLayer.cs**. Cette classe contiendra nos opérations liées à la base de données.

Ouvrez **Employee.cs** et placez le code suivant à l'intérieur. Puisque nous ajoutons les validateurs requis aux champs de la classe Employee, nous devons utiliser System.ComponentModel.DataAnnotations en haut :

```
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace MVCAdoDemo.Models
{
    public class Employee
    {
        public int ID { get; set; }
        [Required]
        public string Name { get; set; }
        [Required]
        public string Gender { get; set; }
        [Required]
        public string Department { get; set; }
        [Required]
        public string City { get; set; }
    }
}
```

Ouvrez **EmployeeDataAccessLayer.cs** et placez le code suivant pour gérer les opérations de la base de données. Assurez-vous de mettre votre propre chaîne de connexion.

```
using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Threading.Tasks;

namespace MVCAdoDemo.Models
{
    public class EmployeeDataAccessLayer
    {
        string connectionString = "Votre Chaîne de Connexion ici";

        // Pour voir tous les détails des employés
        public IEnumerable<Employee> GetAllEmployees()
        {
            List<Employee> lstemployee = new List<Employee>();
            using (SqlConnection con = new SqlConnection(connectionString))
            {
                SqlCommand cmd = new SqlCommand("spGetAllEmployees", con);
                cmd.CommandType = CommandType.StoredProcedure;

                con.Open();
                SqlDataReader rdr = cmd.ExecuteReader();
                while (rdr.Read())
                {
                    Employee employee = new Employee();
                    employee.ID = Convert.ToInt32(rdr["EmployeeID"]);
                    employee.Name = rdr["Name"].ToString();
                    employee.Gender = rdr["Gender"].ToString();
                    employee.Department = rdr["Department"].ToString();
                    employee.City = rdr["City"].ToString();
                    lstemployee.Add(employee);
                }
                con.Close();
            }
            return lstemployee;
        }

        // Pour ajouter un nouvel enregistrement d'employé
        public void AddEmployee(Employee employee)
        {
            using (SqlConnection con = new SqlConnection(connectionString))
            {
                SqlCommand cmd = new SqlCommand("spAddEmployee", con);
                cmd.CommandType = CommandType.StoredProcedure;

                cmd.Parameters.AddWithValue("@Name", employee.Name);
                cmd.Parameters.AddWithValue("@Gender", employee.Gender);
                cmd.Parameters.AddWithValue("@Department", employee.Department);
                cmd.Parameters.AddWithValue("@City", employee.City);

                con.Open();
                cmd.ExecuteNonQuery();
                con.Close();
            }
        }

        // Pour mettre à jour les enregistrements d'un employé particulier
        public void UpdateEmployee(Employee employee)
        {
            using (SqlConnection con = new SqlConnection(connectionString))
            {
                SqlCommand cmd = new SqlCommand("spUpdateEmployee", con);
                cmd.CommandType = CommandType.StoredProcedure;

                cmd.Parameters.AddWithValue("@EmpId", employee.ID);
                cmd.Parameters.AddWithValue("@Name", employee.Name);
                cmd.Parameters.AddWithValue("@Gender", employee.Gender);
                cmd.Parameters.AddWithValue("@Department", employee.Department);
                cmd.Parameters.AddWithValue("@City", employee.City);

                con.Open();
                cmd.ExecuteNonQuery();
                con.Close();
            }
        }

        // Obtenir les détails d'un employé particulier
        public Employee GetEmployeeData(int? id)
        {
            Employee employee = new Employee();
            using (SqlConnection con = new SqlConnection(connectionString))
            {
                string sqlQuery = "SELECT * FROM tblEmployee WHERE EmployeeID= " + id;
                SqlCommand cmd = new SqlCommand(sqlQuery, con);

                con.Open();
                SqlDataReader rdr = cmd.ExecuteReader();
                while (rdr.Read())
                {
                    employee.ID = Convert.ToInt32(rdr["EmployeeID"]);
                    employee.Name = rdr["Name"].ToString();
                    employee.Gender = rdr["Gender"].ToString();
                    employee.Department = rdr["Department"].ToString();
                    employee.City = rdr["City"].ToString();
                }
            }
            return employee;
        }

        // Pour supprimer l'enregistrement d'un employé particulier
        public void DeleteEmployee(int? id)
        {
            using (SqlConnection con = new SqlConnection(connectionString))
            {
                SqlCommand cmd = new SqlCommand("spDeleteEmployee", con);
                cmd.CommandType = CommandType.StoredProcedure;

                cmd.Parameters.AddWithValue("@EmpId", id);
                con.Open();
                cmd.ExecuteNonQuery();
                con.Close();
            }
        }
    }
}
```

Pour utiliser les fonctionnalités ADO.NET dans VS code, nous devons ajouter la référence du package nuget à **System.Data.SqlClient**. Ouvrez le fichier **MvcAdoDemo.csproj** et placez le code suivant à l'intérieur.

```
<PackageReference Include="System.Data.SqlClient" Version="4.4.0" />
```

Placez ce code à l'emplacement mis en évidence dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/rY9smz8tHP3DzNoAASNKRJcMaaaQQNmBBOuO)

### Ajout du Contrôleur à l'Application

Faites un clic droit sur le dossier Controllers et sélectionnez « New File ». Nommez-le **EmployeeController.cs**. Cela créera un nouveau fichier à l'intérieur du dossier Controllers.

![Image](https://cdn-media-1.freecodecamp.org/images/gLY-C8N2jh5NfKg4LZQ1k7l7FG2L6gTwolb7)

Maintenant, notre **EmployeeController** a été créé. Nous allons mettre toute notre logique métier dans ce contrôleur.

### Ajout des Vues à l'Application

Pour ajouter des vues pour notre classe de contrôleur, nous devons créer un dossier à l'intérieur du dossier **Views** avec le même nom que notre contrôleur, puis ajouter nos vues à ce dossier.

Faites un clic droit sur le dossier Views, et sélectionnez « New Folder » et nommez le dossier **Employee**.

![Image](https://cdn-media-1.freecodecamp.org/images/q46Crt245HstIcDlnbYeeJBjQdS30gH1m5Vm)

Pour ajouter des fichiers de vue, faites un clic droit sur le dossier Employee à l'intérieur du dossier Views et sélectionnez « New File ». Nommez-le **Index.cshtml**. Cela créera un fichier de vue à l'intérieur du dossier Employee. Ainsi, nous avons créé notre première vue. Ajoutez 4 vues supplémentaires dans le dossier Views/Employee : **Create.cshtml, Delete.cshtml, Details.cshtml,** et **Edit.cshtml.**

Maintenant, notre dossier Views ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/ess0Xg9UQ7zPf7ZtvWoKu5v4D0tuZjDxbc2k)

Puisque toutes nos vues ont été créées, nous allons mettre du code dans la vue et le contrôleur pour effectuer des opérations CRUD.

### Vue Index

Cette vue affichera tous les enregistrements d'employés présents dans la base de données. De plus, nous fournirons également les méthodes d'action Edit, Details et Delete sur chaque enregistrement.

Ouvrez **Index.cshtml** et placez le code suivant à l'intérieur.

```
@model IEnumerable<MVCAdoDemo.Models.Employee>
@{ 
    ViewData["Title"] = "Index";
}
<h2>Index</h2>
<p>
    <a asp-action="Create">Créer Nouveau</a>
</p>
<table class="table">
    <thead>
        <tr>
            <th>
                @Html.DisplayNameFor(model => model.Name)
            </th>
            <th>
                @Html.DisplayNameFor(model => model.Gender)
            </th>
            <th>
                @Html.DisplayNameFor(model => model.Department)
            </th>
            <th>
                @Html.DisplayNameFor(model => model.City)
            </th>
            <th></th>
        </tr>
    </thead>
    <tbody>
        @foreach (var item in Model)
        {
            <tr>
                <td>
                    @Html.DisplayFor(modelItem => item.Name)
                </td>
                <td>
                    @Html.DisplayFor(modelItem => item.Gender)
                </td>
                <td>
                    @Html.DisplayFor(modelItem => item.Department)
                </td>
                <td>
                    @Html.DisplayFor(modelItem => item.City)
                </td>
                <td>
                    <a asp-action="Edit" asp-route-id="@item.ID">Éditer</a> |
                    <a asp-action="Details" asp-route-id="@item.ID">Détails</a> |
                    <a asp-action="Delete" asp-route-id="@item.ID">Supprimer</a>
                </td>
            </tr>
        }
    </tbody>
</table>
```

Ouvrez votre fichier **EmployeeController.cs**. Vous verrez qu'il est vide. Placez le code suivant à l'intérieur.

```
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using MVCAdoDemo.Models;

namespace MVCAdoDemo.Controllers
{
    public class EmployeeController : Controller
    {
        EmployeeDataAccessLayer objemployee = new EmployeeDataAccessLayer();

        public IActionResult Index()
        {
            List<Employee> lstEmployee = new List<Employee>();
            lstEmployee = objemployee.GetAllEmployees().ToList();

            return View(lstEmployee);
        }
    }
}
```

Pour gérer les opérations de la base de données, nous avons créé un objet de la classe **EmployeeDataAccessLayer** à l'intérieur de la classe **EmployeeController**.

### Vue Create

Cette vue sera utilisée pour ajouter de nouvelles données d'employé à la base de données.

Ouvrez **Create.cshtml** et placez le code suivant à l'intérieur.

```
@model MVCAdoDemo.Models.Employee
@{ 
    ViewData["Title"] = "Create";
}
<h2>Créer</h2>
<h4>Employés</h4>
<hr />
<div class="row">
    <div class="col-md-4">
        <form asp-action="Create">
            <div asp-validation-summary="ModelOnly" class="text-danger"></div>
            <div class="form-group">
                <label asp-for="Name" class="control-label"></label>
                <input asp-for="Name" class="form-control" />
                <span asp-validation-for="Name" class="text-danger"></span>
            </div>
            <div class="form-group">
                <label asp-for="Gender" class="control-label"></label>
                <select asp-for="Gender" class="form-control">
                    <option value="">-- Sélectionner le Genre --</option>
                    <option value="Male">Homme</option>
                    <option value="Female">Femme</option>
                </select>
                <span asp-validation-for="Gender" class="text-danger"></span>
            </div>
            <div class="form-group">
                <label asp-for="Department" class="control-label"></label>
                <input asp-for="Department" class="form-control" />
                <span asp-validation-for="Department" class="text-danger"></span>
            </div>
            <div class="form-group">
                <label asp-for="City" class="control-label"></label>
                <input asp-for="City" class="form-control" />
                <span asp-validation-for="City" class="text-danger"></span>
            </div>
            <div class="form-group">
                <input type="submit" value="Créer" class="btn btn-default" />
            </div>
        </form>
    </div>
</div>
<div>
    <a asp-action="Index">Retour à la Liste</a>
</div>
@section Scripts {
    @{await Html.RenderPartialAsync("_ValidationScriptsPartial");}
}
```

Pour gérer la logique métier de **create**, ouvrez **EmployeeController.cs** et placez le code suivant à l'intérieur.

```
[HttpGet]
public IActionResult Create()
{
    return View();
}

[HttpPost]
[ValidateAntiForgeryToken]
public IActionResult Create([Bind] Employee employee)
{
    if (ModelState.IsValid)
    {
        objemployee.AddEmployee(employee);
        return RedirectToAction("Index");
    }
    return View(employee);
}
```

L'attribut [Bind] est utilisé avec le paramètre « employee » pour se protéger contre le sur-postage. Pour en savoir plus sur le sur-postage, visitez [ce lien](https://docs.microsoft.com/en-gb/aspnet/mvc/overview/getting-started/getting-started-with-ef-using-mvc/implementing-basic-crud-functionality-with-the-entity-framework-in-asp-net-mvc-application#overpost).

### Vue Edit

Cette vue nous permettra de modifier les données d'un employé existant.

Ouvrez **Edit.cshtml** et placez le code suivant à l'intérieur.

```
@model MVCAdoDemo.Models.Employee
@{ 
    ViewData["Title"] = "Edit";
}
<h2>Éditer</h2>
<h4>Employés</h4>
<hr />
<div class="row">
    <div class="col-md-4">
        <form asp-action="Edit">
            <div asp-validation-summary="ModelOnly" class="text-danger"></div>
            <input type="hidden" asp-for="ID" />
            <div class="form-group">
                <label asp-for="Name" class="control-label"></label>
                <input asp-for="Name" class="form-control" />
                <span asp-validation-for="Name" class="text-danger"></span>
            </div>
            <div class="form-group">
                <label asp-for="Gender" class="control-label"></label>
                <select asp-for="Gender" class="form-control">
                    <option value="">-- Sélectionner le Genre --</option>
                    <option value="Male">Homme</option>
                    <option value="Female">Femme</option>
                </select>
                <span asp-validation-for="Gender" class="text-danger"></span>
            </div>
            <div class="form-group">
                <label asp-for="Department" class="control-label"></label>
                <input asp-for="Department" class="form-control" />
                <span asp-validation-for="Department" class="text-danger"></span>
            </div>
            <div class="form-group">
                <label asp-for="City" class="control-label"></label>
                <input asp-for="City" class="form-control" />
                <span asp-validation-for="City" class="text-danger"></span>
            </div>
            <div class="form-group">
                <input type="submit" value="Sauvegarder" class="btn btn-default" />
            </div>
        </form>
    </div>
</div>
<div>
    <a asp-action="Index">Retour à la Liste</a>
</div>
@section Scripts {
    @{await Html.RenderPartialAsync("_ValidationScriptsPartial");}
}
```

Pour gérer la logique métier de la vue **Edit**, ouvrez **EmployeeController.cs** et ajoutez le code suivant à l'intérieur.

```
[HttpGet]
public IActionResult Edit(int? id)
{
    if (id == null)
    {
        return NotFound();
    }
    Employee employee = objemployee.GetEmployeeData(id);

    if (employee == null)
    {
        return NotFound();
    }
    return View(employee);
}

[HttpPost]
[ValidateAntiForgeryToken]
public IActionResult Edit(int id, [Bind]Employee employee)
{
    if (id != employee.ID)
    {
        return NotFound();
    }
    if (ModelState.IsValid)
    {
        objemployee.UpdateEmployee(employee);
        return RedirectToAction("Index");
    }
    return View(employee);
}
```

Vous verrez que nous avons deux méthodes d'action Edit : une pour HttpGet et une autre pour HttpPost. La méthode d'action Edit HttpGet récupère les données de l'employé et remplit les champs de la vue d'édition. Une fois que l'utilisateur clique sur le bouton Sauvegarder après avoir modifié l'enregistrement, une requête Post sera générée qui est gérée par la méthode d'action Edit HttpPost.

### Vue Details

Cette vue affichera les détails d'un employé particulier.

Ouvrez **Details.cshtml** et placez le code suivant à l'intérieur.

```
@model MVCAdoDemo.Models.Employee
@{ 
    ViewData["Title"] = "Details";
}
<h2>Détails</h2>
<div>
    <h4>Employés</h4>
    <hr />
    <dl class="dl-horizontal">
        <dt>
            @Html.DisplayNameFor(model => model.Name)
        </dt>
        <dd>
            @Html.DisplayFor(model => model.Name)
        </dd>
        <dt>
            @Html.DisplayNameFor(model => model.Gender)
        </dt>
        <dd>
            @Html.DisplayFor(model => model.Gender)
        </dd>
        <dt>
            @Html.DisplayNameFor(model => model.Department)
        </dt>
        <dd>
            @Html.DisplayFor(model => model.Department)
        </dd>
        <dt>
            @Html.DisplayNameFor(model => model.City)
        </dt>
        <dd>
            @Html.DisplayFor(model => model.City)
        </dd>
    </dl>
</div>
<div>
    <a asp-action="Edit" asp-route-id="@Model.ID">Éditer</a> |
    <a asp-action="Index">Retour à la Liste</a>
</div>
```

Pour gérer la logique métier de la vue **Details**, ouvrez **EmployeeController.cs** et ajoutez le code suivant à l'intérieur.

```
[HttpGet]
public IActionResult Details(int? id)
{
    if (id == null)
    {
        return NotFound();
    }
    Employee employee = objemployee.GetEmployeeData(id);

    if (employee == null)
    {
        return NotFound();
    }
    return View(employee);
}
```

### Vue Delete

Cette vue nous aidera à supprimer les données d'un employé.

Ouvrez **Delete.cshtml** et placez le code suivant à l'intérieur.

```
@model MVCAdoDemo.Models.Employee
@{ 
    ViewData["Title"] = "Delete";
}
<h2>Supprimer</h2>
<h3>Êtes-vous sûr de vouloir supprimer ceci ?</h3>
<div>
    <h4>Employés</h4>
    <hr />
    <dl class="dl-horizontal">
        <dt>
            @Html.DisplayNameFor(model => model.Name)
        </dt>
        <dd>
            @Html.DisplayFor(model => model.Name)
        </dd>
        <dt>
            @Html.DisplayNameFor(model => model.Gender)
        </dt>
        <dd>
            @Html.DisplayFor(model => model.Gender)
        </dd>
        <dt>
            @Html.DisplayNameFor(model => model.Department)
        </dt>
        <dd>
            @Html.DisplayFor(model => model.Department)
        </dd>
        <dt>
            @Html.DisplayNameFor(model => model.City)
        </dt>
        <dd>
            @Html.DisplayFor(model => model.City)
        </dd>
    </dl>
    <form asp-action="Delete">
        <input type="hidden" asp-for="ID" />
        <input type="submit" value="Supprimer" class="btn btn-default" /> |
        <a asp-action="Index">Retour à la Liste</a>
    </form>
</div>
```

Pour gérer la logique métier de la vue **Delete**, ouvrez **EmployeeController.cs** et ajoutez le code suivant à l'intérieur.

```
[HttpGet]
public IActionResult Delete(int? id)
{
    if (id == null)
    {
        return NotFound();
    }
    Employee employee = objemployee.GetEmployeeData(id);

    if (employee == null)
    {
        return NotFound();
    }
    return View(employee);
}

[HttpPost, ActionName("Delete")]
[ValidateAntiForgeryToken]
public IActionResult DeleteConfirmed(int? id)
{
    objemployee.DeleteEmployee(id);
    return RedirectToAction("Index");
}
```

Pour compléter l'opération de suppression, nous avons besoin de deux méthodes Delete qui acceptent le même paramètre (Employee Id). Mais deux méthodes avec le même nom et la même signature de méthode créeront une erreur de compilation. Et si nous renommons la méthode Delete, alors le routage ne pourra pas la trouver, car asp.net mappe les segments d'URL aux méthodes d'action par nom.

Donc, pour résoudre ce problème, nous ajoutons l'attribut ActionName("Delete") à la méthode DeleteConfirmed. Cet attribut effectue le mappage pour le système de routage afin qu'une URL qui inclut /Delete/ pour une requête POST trouve la méthode DeleteConfirmed.

Lorsque nous cliquons sur le lien Supprimer dans la page Index, il enverra une requête Get et retournera une vue de l'employé en utilisant la méthode Delete HttpGet. Lorsque nous cliquons sur le bouton Supprimer dans cette vue, il enverra une requête Post pour supprimer l'enregistrement qui est gérée par la méthode DeleteConfirmed HttpPost.

Effectuer une opération de suppression en réponse à une requête Get (ou, pour cette matière, effectuer une opération d'édition, de création ou toute autre opération qui change les données) ouvre une faille de sécurité. Par conséquent, nous avons deux méthodes séparées.

### Configurer l'URL de routage

Avant de lancer l'application, nous allons configurer les URL de routage. Ouvrez le fichier **Startup.cs** pour définir le format de routage. Faites défiler jusqu'à la méthode **app.UseMvc**, où vous pouvez définir l'URL de routage.

Assurez-vous que votre URL de routage est définie comme ceci :

```
app.UseMvc(routes =>
{
    routes.MapRoute(
        name: "default",
        template: "{controller=Home}/{action=Index}/{id?}");
});
```

Ce modèle d'URL définit HomeController comme le contrôleur par défaut et la méthode Index comme la méthode d'action par défaut (tandis que le paramètre Id est facultatif). Les paramètres de route par défaut et facultatifs n'ont pas besoin d'être présents dans le chemin d'URL pour une correspondance.

Si nous n'ajoutons aucun nom de contrôleur dans l'URL, alors il prendra HomeController comme contrôleur par défaut et la méthode Index de HomeController comme méthode d'action par défaut. De même, si nous ajoutons uniquement le nom du contrôleur dans l'URL, il naviguera vers la méthode d'action Index de ce contrôleur.

### Démo d'Exécution

Maintenant, appuyez sur F5 pour lancer l'application et naviguez vers le contrôleur Employee en ajoutant **/Employee** à l'URL.

Vous pouvez voir la page comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/wHDh5w3V82jZaQYnStYGiwwZXDoKMLHlZ8eu)

Cliquez sur **Créer Nouveau** pour naviguer vers la vue **Create**. Ajoutez un nouvel enregistrement d'employé comme montré dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/fPgjtJ80Y0S9DRJ74EPgG-4bzxkU5JJclcR1)

Si nous manquons les données dans un champ lors de la création de l'enregistrement de l'employé, nous obtiendrons un message d'erreur de validation de champ requis.

![Image](https://cdn-media-1.freecodecamp.org/images/Yam4xcN67M-9bk4vSEtxyaq0RWDIfhs9AbYA)

Après avoir inséré les données dans tous les champs, cliquez sur le bouton « Créer ». Le nouvel enregistrement d'employé sera créé et vous serez redirigé vers la vue Index, qui affiche les enregistrements de tous les employés. Ici, nous pouvons également voir les méthodes d'action Éditer, Détails et Supprimer.

![Image](https://cdn-media-1.freecodecamp.org/images/evhF3e0t1-b3T2nRNfK-I3fr2owXg8pZttQh)

Si nous voulons modifier un enregistrement d'employé existant, cliquez sur le lien d'action Éditer. Il ouvrira la vue Éditer comme ci-dessous où nous pouvons changer les données de l'employé.

![Image](https://cdn-media-1.freecodecamp.org/images/eVE71HWjPJm-VIJYx1oAW67miKJpoIHoExDR)

Ici, nous avons changé la ville de l'employé Dhiraj de Mumbai à New Delhi. Cliquez sur « Sauvegarder » pour revenir à la vue Index et voir les modifications mises à jour comme mis en évidence dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/sGY1P9hyo39tYbLSJAko5CtjXziuS9ZkGqC0)

Si nous manquons des champs lors de l'édition de l'enregistrement de l'employé, alors la vue Éditer affichera également le message d'erreur de validation de champ requis.

![Image](https://cdn-media-1.freecodecamp.org/images/cDkBhfjFPqYPOrarYICCysXA1-SNBcDcFmsu)

Si vous voulez voir les détails de n'importe quel employé, cliquez sur le lien d'action Détails, qui ouvrira la vue Détails, comme montré dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/QgscvR0qBducegEFloNH0Zyc0UXwtxvibMX9)

Cliquez sur « Retour à la Liste » pour revenir à la vue Index. Maintenant, nous allons effectuer une opération de suppression sur un employé nommé Rahul. Cliquez sur le lien d'action Supprimer qui ouvrira la vue Supprimer demandant une confirmation pour supprimer.

![Image](https://cdn-media-1.freecodecamp.org/images/izhHIcJ8tWNHf506tk3BDZ8AdY0UQQXwO32f)

Une fois que nous cliquons sur le bouton Supprimer, il enverra une requête HttpPost pour supprimer l'enregistrement de l'employé, et nous serons redirigés vers la vue Index. Ici, nous pouvons voir que l'employé avec le nom Rahul a été supprimé de notre enregistrement.

![Image](https://cdn-media-1.freecodecamp.org/images/ehuId4jihuu2Zgxktndd4571m2jPQYEun-uU)

### Conclusion

Nous avons appris à créer une application web MVC de démonstration en utilisant ASP.Net Core 2.0, ADO.NET et un serveur SQL avec l'aide de Visual Studio Code.

Téléchargez le code source depuis [GitHub](https://github.com/AnkitSharma-007/CRUD.With.VSCode.ADO) et jouez avec pour mieux comprendre.

Vous pouvez consulter mes autres articles sur ASP .NET Core [ici](http://ankitsharmablogs.com/category/asp-net-core/)

Préparation aux entretiens ? Lisez mon article sur [C# Coding Questions For Technical Interviews](http://ankitsharmablogs.com/csharp-coding-questions-for-technical-interviews/).

### Voir Aussi

* [CRUD Operation With ASP.NET Core MVC Using ADO.NET and Visual Studio 2017](http://ankitsharmablogs.com/crud-operation-with-asp-net-core-mvc-using-ado-net/)
* [CRUD Operation With ASP.NET Core MVC Using Visual Studio Code and EF](http://ankitsharmablogs.com/crud-operation-asp-net-core-mvc-using-visual-studio-code-ef/)
* [ASP.NET Core — CRUD With React.js And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-with-react-js-and-entity-framework-core/)
* [CRUD Operations With ASP.NET Core Using Angular 5 and ADO.NET](http://ankitsharmablogs.com/crud-operations-asp-net-core-using-angular-5-ado-net/)
* [ASP.NET Core — Getting Started With Blazor](http://ankitsharmablogs.com/asp-net-core-getting-started-with-blazor/)
* [Cookie Authentication With ASP.NET Core 2.0](http://ankitsharmablogs.com/cookie-authentication-with-asp-net-core-2-0/)

Publié à l'origine sur [ankitsharmablogs.com](http://ankitsharmablogs.com/asp-net-core-crud-using-angular-5-and-entity-framework-core/)