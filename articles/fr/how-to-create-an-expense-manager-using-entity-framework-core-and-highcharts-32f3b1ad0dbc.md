---
title: Comment créer un gestionnaire de dépenses avec Entity Framework Core et Highcharts
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
seo_title: Comment créer un gestionnaire de dépenses avec Entity Framework Core et
  Highcharts
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we will be creating a personal expense manager using ASP.NET Core
  2.1 and Entity Framework (EF) core Code First approach. This expense manager tracks
  your daily expenses and provides comparative charts to...'
---

Par Ankit Sharma

### Introduction

Dans cet article, nous allons créer un gestionnaire de dépenses personnel en utilisant ASP.NET Core 2.1 et l'approche Code First d'Entity Framework (EF) Core. Ce gestionnaire de dépenses suit vos dépenses quotidiennes et fournit des graphiques comparatifs pour montrer le résumé de vos dépenses. Nous utilisons une boîte de dialogue modale pour gérer les entrées utilisateur et pour afficher les graphiques de résumé des dépenses mensuelles et hebdomadaires en utilisant Highcharts. Par conséquent, ce sera une application monopage (SPA).

Nous utiliserons Visual Studio 2017 et SQL Server 2017 pour notre démonstration.

Regardons l'application finale :

![Image](https://cdn-media-1.freecodecamp.org/images/xO0BJntS6-EbjUgVPIHp0V7axFs1trr1eoj4)

### Prérequis

* Installer le SDK .NET Core 2.1 depuis [ici](https://www.microsoft.com/net/learn/get-started/windows#windowscmd)
* Installer la dernière version de Visual Studio 2017 depuis [ici](https://visualstudio.microsoft.com/downloads/)
* SQL Server 2008 ou supérieur

### Code source

Avant de continuer, je vous recommande de récupérer le code source depuis [GitHub](https://github.com/AnkitSharma-007/ExpenseManager-ASPCore-EFCore-Highchart).

### Créer le projet ASP.NET Core

Ouvrez Visual Studio et sélectionnez « Fichier » > « Nouveau » > « Projet ».

Après avoir sélectionné le projet, une boîte de dialogue « Nouveau Projet » s'ouvrira. Sélectionnez « .NET Core » dans le panneau de gauche à l'intérieur du menu Visual C#.

Ensuite, sélectionnez « Application Web ASP.NET Core » parmi les types de projets disponibles. Donnez le nom du projet « ExpenseManager » et appuyez sur « OK » pour créer le projet ASP.NET Core.

![Image](https://cdn-media-1.freecodecamp.org/images/BdP-AFHko5M6RuXPqwXBRJerxtTGGXrV36q7)

Après avoir cliqué sur OK, une nouvelle boîte de dialogue s'ouvrira vous demandant de sélectionner le modèle de projet.

Vous verrez deux menus déroulants en haut à gauche de la fenêtre de modèle. Sélectionnez « .NET Core » et « ASP.NET Core 2.1 » dans ces menus déroulants. Ensuite, sélectionnez le modèle « Application Web (Modèle-Vue-Contrôleur) » et appuyez sur « OK ».

![Image](https://cdn-media-1.freecodecamp.org/images/sB3aRxylwpRxe2PKhpuDik35Y8f12tKJ160A)

### Ajouter le modèle à l'application

Puisque nous utilisons l'approche Code First d'EF Core, nous allons d'abord créer notre classe de modèle. Ensuite, nous allons générer nos tables de base de données en utilisant le modèle.

Faites un clic droit sur le dossier « Models » et sélectionnez « Ajouter » > « Classe ». Nommez votre classe « ExpenseReport.cs ». Cette classe contiendra les propriétés de notre modèle « Employee ».

Ouvrez le fichier « ExpenseReport.cs » et insérez le code suivant :

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

Nous avons utilisé l'attribut `[Key]` avec `ItemId` pour en faire la clé primaire lors de la création de la table de la base de données.

### Créer la table de la base de données en utilisant l'approche EF Core Code First

Afin de créer nos tables en utilisant l'approche EF Core Code First, nous devons installer quelques packages NuGet.

Accédez à « Outils » > « Gestionnaire de packages NuGet » > « Console du gestionnaire de packages ».

Nous devons installer le package pour le fournisseur de base de données que nous ciblons. Dans ce cas, il s'agit de SQL Server. Exécutez donc la commande suivante :

```
Install-Package Microsoft.EntityFrameworkCore.SqlServer
```

Puisque nous utilisons les outils EF pour créer une table à partir du modèle existant, nous allons également installer le package des outils. Exécutez la commande suivante :

```
Install-Package Microsoft.EntityFrameworkCore.Tools
```

Après que les installations des packages soient réussies, nous allons créer une classe `dbcontext`. Ajoutez un fichier « ExpenseDBContext.cs » dans le dossier Models et insérez le code suivant :

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
#warning Pour protéger les informations potentiellement sensibles dans votre chaîne de connexion, vous devez la déplacer hors du code source. Voir http://go.microsoft.com/fwlink/?LinkId=723263 pour obtenir des conseils sur le stockage des chaînes de connexion.
                optionsBuilder.UseSqlServer("Votre chaîne de connexion");
            }
        }
    }
}
```

**N'oubliez pas** de mettre votre propre chaîne de connexion (à l'intérieur de `""`).

Nous allons créer une migration de jeu de données qui est utilisée pour garder le schéma de la base de données synchronisé avec le modèle. Il n'y a pas de base de données pour le moment, donc la première migration la créera, **et** ajoutera des tables pour les entités représentées par les propriétés `DbSet` sur le `ExpenseDBContext` que nous avons créé.

Pour créer la migration de jeu de données, accédez au dossier du projet et ouvrez la fenêtre PowerShell. Exécutez la commande suivante :

```
dotnet ef  migrations add ExpenseMigration
```

Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/z3Hc9XEFxvh-GjO2mv3crU58GpiCfCKptBPg)

Cela créera un dossier nommé « Migrations » dans notre projet, qui contient le code pour la migration **et** un instantané du modèle. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/c1K51nGiW4uooQUPy9EMyRGvCXPexQEdhJe8)

Entrez la commande suivante dans la fenêtre PowerShell pour exécuter la migration :

```
dotnet ef database update
```

Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/o5iXSve2WjqSeO5gAX2x8mf6ZHptiTFjD3i8)

Cela créera la table « ExpenseReport » dans notre base de données que nous avons mentionnée dans la chaîne de connexion. Vous pouvez voir que la colonne `ItemId` est la clé primaire ici.

![Image](https://cdn-media-1.freecodecamp.org/images/KSFtxL-C-Bv7fwTvn2OpFwKwgXYB5ABbFql2)

Ainsi, la création de la base de données est terminée avec succès en utilisant l'approche EF Code First.

### Ajouter la couche d'accès aux données à notre application

Ajoutez un fichier de classe « ExpensesDataAcessLayer.cs » dans le dossier « Models » et insérez le code suivant :

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

        // Pour filtrer les enregistrements en fonction de la chaîne de recherche 
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

        //Pour ajouter un nouvel enregistrement de dépense       
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

        //Pour mettre à jour les enregistrements d'une dépense particulière  
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

        //Obtenir les données pour une dépense particulière  
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

        //Pour supprimer l'enregistrement d'une dépense particulière  
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

        // Pour calculer les dépenses des six derniers mois
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

        // Pour calculer les dépenses des quatre dernières semaines
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

Ce fichier contiendra des méthodes pour gérer les opérations CRUD sur notre base de données. Nous calculons également les totaux des dépenses des six derniers mois et des quatre dernières semaines pour chaque catégorie.

### Ajouter le contrôleur à l'application

Faites un clic droit sur le dossier « Controllers » et sélectionnez « Ajouter » > « Nouvel élément ». Une boîte de dialogue « Ajouter un nouvel élément » s'ouvrira. Sélectionnez « ASP.NET Core » dans le panneau de gauche, puis sélectionnez « Classe de contrôleur » dans le panneau des modèles, et donnez le nom « ExpenseController.cs ». Appuyez sur « Ajouter ».

![Image](https://cdn-media-1.freecodecamp.org/images/iS8NP1beORaP0LpY6MLAH1ygwkgRD1yDpJHU)

Cela créera notre contrôleur `ExpenseController` **dans** le dossier « Controllers ». Ouvrez le fichier « ExpenseController.cs » et insérez le code suivant :

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

Le contrôleur aura les méthodes pour appeler nos méthodes de couche d'accès aux données afin de gérer les opérations de la base de données.

### Ajouter des vues à l'application

Nous allons créer trois fichiers de vue :

1. « Index.cshtml » — cette vue affichera toutes les données de dépenses et contient une boîte de recherche pour rechercher un article particulier.
2. « _expenseForm.cshtml » — il s'agit d'une vue partielle qui contient le formulaire pour gérer les entrées utilisateur. Elle est utilisée pour les fonctionnalités d'ajout et d'édition et sera rendue dans une boîte de dialogue modale.
3. « _expenseReport.cshtml » : il s'agit également d'une vue partielle qui affichera le résumé des dépenses dans un graphique à barres en utilisant Highcharts. Elle est également rendue sous forme de boîte de dialogue modale.

#### Vue Index

Pour créer le fichier de vue, faites un clic droit sur la méthode « Index » dans notre contrôleur et sélectionnez « Ajouter une vue... ». Cela ouvrira une boîte de dialogue « Ajouter une vue MVC ». Donnez le nom de la vue « Index » et cliquez sur « Ajouter ». **Assurez-vous** que la case à cocher « Créer en tant que vue partielle » **n'est pas** cochée. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/2dTGSQGR0dLh0apD3msjTibU-zxftGF4Ummi)

Cela créera le fichier « Index.cshtml » à l'intérieur du dossier « Expense », sous le dossier « Views ». Ouvrez le fichier « Index.cshtml » et insérez le code suivant :

```cs
@model IEnumerable<ExpenseManager.Models.ExpenseReport>

@{
    ViewData["Title"] = "Gestionnaire de dépenses personnelles";
}
<link href="~/lib/bootstrap/dist/css/bootstrap.css" rel="stylesheet" />
<script src="~/lib/jquery/dist/jquery.min.js"></script>
<script src="~/lib/bootstrap/dist/js/bootstrap.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.8.0/js/bootstrap-datepicker.js"></script>
<link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.8.0/css/bootstrap-datepicker.css" rel="stylesheet">

<h2>Gestionnaire de dépenses personnelles</h2>
<br />
<div>
    <div style="float:left">
        <button class="btn btn-primary" onclick="AddEditExpenses(0)">Ajouter une dépense</button>
        <button class="btn btn-success" onclick="ReportExpense()">Rapport de dépenses</button>
    </div>
    <div style="float:right; width:40%;">
        <form asp-controller="Expense" asp-action="Index" class="form-group">
            <div class="col-sm-6">
                <input class="form-control" type="text" name="SearchString" placeholder="Rechercher">
            </div>
            <button type="submit" class="btn btn-default btn-info">Filtrer</button>
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
            <th>Action</th>
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
                    <button class="btn btn-default" onclick="AddEditExpenses(@item.ItemId)">Modifier</button>
                    <button class="btn btn-danger" onclick="DeleteExpense(@item.ItemId)">Supprimer</button>
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
                <h3 id="title" class="modal-title">Ajouter une dépense</h3>
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
                <h3 class="modal-title">Rapport de dépenses</h3>
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
            $('#title').html("Modifier la dépense");

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

        var ans = confirm("Voulez-vous supprimer l'élément avec l'ID : " + itemId);

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

Comprenons ce code.

En haut, nous avons inclus les références à Bootstrap et jQuery.

Après cela, nous avons ajouté deux boutons pour ajouter une nouvelle dépense et pour créer le rapport de dépenses.

Nous avons également inclus un formulaire contenant une boîte de recherche pour filtrer les enregistrements. En cliquant sur le bouton « Filtrer », le formulaire est soumis et il invoque la méthode `Index` dans notre contrôleur, qui retournera les éléments correspondant aux critères de recherche. La fonctionnalité de recherche est fournie uniquement sur le champ de nom de l'article.

Nous utilisons un tableau pour afficher tous les enregistrements de dépenses dans notre base de données. Chaque enregistrement a deux boutons d'action correspondants : « Modifier » et « Supprimer ».

Nous avons également créé deux boîtes de dialogue modales. L'une est pour ajouter/modifier les données de dépenses, et l'autre pour afficher le rapport de résumé des dépenses.

Dans la section script, nous avons défini une fonction `AddEditExpenses`. Cette fonction sera invoquée lorsque le bouton « Ajouter une dépense » ou « Modifier » est cliqué. Nous passons l'`itemId` comme paramètre dans cette méthode. Si la valeur `ItemId` **n'est pas définie**, alors elle est considérée comme une fonction `Add`. Si l'`ItemId` **est défini**, alors il s'agit d'une fonction `Edit`.

Nous allons appeler `AddEditExpenses` dans notre contrôleur qui retournera la vue partielle « _expenseForm » et la liera au modèle ExpenseReport. La boîte de dialogue modale sera vide pour un appel `Add` et contiendra les données de l'article de dépense dans le cas d'un appel `Edit`. Nous utilisons un sélecteur de date Bootstrap pour sélectionner la date de la dépense, donc nous avons défini les propriétés du sélecteur de date lors du chargement de la boîte de dialogue modale.

La fonction `ReportExpense` appellera la méthode `ExpenseSummary` dans notre contrôleur. Cela retournera la vue partielle « _expenseReport » à afficher sous forme de boîte de dialogue modale. Cette vue partielle affichera le graphique de résumé des dépenses mensuelles et hebdomadaires en utilisant Highcharts.

La fonction `DeleteExpense` est utilisée pour supprimer l'enregistrement d'une dépense particulière. Cela invoquera la méthode `Delete` dans notre contrôleur pour supprimer l'enregistrement de dépense de notre base de données.

Nous utilisons également la liaison dynamique pour lier l'événement de soumission du modal « expenseForm ». Ce formulaire est défini dans la vue « _expenseForm.cshtml ». Lors de la soumission du formulaire, nous invoquons un appel ajax à la méthode `Create` dans notre classe de contrôleur.

Puisque nous utilisons le même formulaire pour les fonctionnalités `Edit` et `Add`, nous devons distinguer les deux en utilisant la valeur `ItemId`. Dans la méthode `Create` du contrôleur, si l'`ItemId` est défini, alors nous invoquerons la méthode `UpdateExpense`. Sinon, la méthode `AddExpense` est invoquée. Après une soumission réussie, nous fermerons le modal et redirigerons vers la vue Index pour montrer la liste mise à jour des dépenses.

#### Vue ExpenseForm

Il s'agit d'une vue partielle qui sera affichée dans une boîte de dialogue modale en cliquant sur le bouton « Ajouter une dépense » dans la vue « Index ».

Pour créer le fichier de vue, faites un clic droit n'importe où dans notre fichier de contrôleur et sélectionnez « Ajouter une vue... ». Cela ouvrira une boîte de dialogue « Ajouter une vue MVC ». Donnez le nom de la vue « _expenseForm » et cliquez sur « Ajouter ». **Assurez-vous** que la case à cocher « Créer en tant que vue partielle » **est** cochée. Voir l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/ahA3bCK-ViyDNYQpP6oPWGFQcy0jg9jUWu37)

Ouvrez le fichier « _expenseForm.cshtml » et insérez le code suivant :

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
                        <option value="">-- Sélectionner une catégorie --</option>
                        <option value="Food">Nourriture</option>
                        <option value="Shopping">Shopping</option>
                        <option value="Travel">Voyage</option>
                        <option value="Health">Santé</option>
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
                    <button type="button" id="btnSubmit" class="btn btn-block btn-info">Enregistrer</button>
                </div>
            </form>
        </div>
    </div>
</div>
```

En haut, nous incluons la référence `cdn` au sélecteur de date Bootstrap afin de pouvoir l'utiliser dans notre boîte de dialogue modale. Ensuite, nous avons un élément `<form>`, qui se lie à notre modèle. Nous avons également un bouton de soumission qui enverra les données du formulaire à la méthode `Create` dans notre contrôleur en utilisant un appel ajax.

#### Vue ExpenseReport

Il s'agit d'une vue partielle qui est affichée dans la boîte de dialogue modale en cliquant sur le bouton « Rapport de dépenses » dans la vue « Index ».

Créez une nouvelle vue partielle « _expenseReport.cshtml » et insérez le code suivant :

```cs
<script src="https://code.highcharts.com/highcharts.js"></script>

<button id="btnMonthlyReport" class="btn btn-info">Rapport mensuel</button>
<button id="btnWeeklyReport" class="btn btn-warning">Rapport hebdomadaire</button>
<div id="container" style="min-width: 400px; height: 400px; margin: 0 auto">

</div>

<script>

    $(document).ready(function () {
        $("#btnWeeklyReport").click(function () {
            var titleMessage = "Dépenses des quatre dernières semaines : ";

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
            var titleMessage = "Dépenses des six derniers mois : ";

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
                    text: 'Argent dépensé'
                }
            },
            legend: {
                enabled: false
            },
            tooltip: {
                pointFormat: 'Total de l\'argent dépensé: <b>{point.y:.2f} </b>'
            },
            series: [{
                type: 'column',
                data: sum,
            }]
        });
    }

</script>
```

En haut, nous avons inclus la référence `cdn` à Highcharts. Nous avons également fourni deux boutons. L'un est utilisé pour afficher un rapport mensuel des six derniers mois. L'autre est pour afficher un rapport hebdomadaire des quatre dernières semaines. Le rapport sera généré sous forme de graphique à barres pour fournir une étude comparative des résumés de dépenses.

En cliquant sur le bouton de rapport hebdomadaire, nous invoquerons la méthode `GetWeeklyExpense` de notre contrôleur. Cela retournera les données au format JSON. Nous passerons ces données à la fonction `createCharts` pour créer le graphique à barres des dépenses hebdomadaires en utilisant Highcharts.

De même, nous invoquerons la méthode `GetMonthlyExpense` de notre contrôleur en cliquant sur le bouton « Rapport mensuel ». Le résultat JSON sera passé à la fonction `createCharts` pour créer le graphique à barres des dépenses mensuelles en utilisant Highcharts.

### Configurer l'URL de routage

Ouvrez le fichier « Startup.cs » pour définir le format des routes de l'application. Faites défiler jusqu'à la méthode `app.UseMvc` où vous pouvez définir l'URL de routage.

Assurez-vous que votre URL de routage est définie comme suit :

```cs
app.UseMvc(routes =>
{
    routes.MapRoute(
        name: "default",
        template: "{controller=Expense}/{action=Index}");
});
```

Ce modèle d'URL définit `ExpenseController` comme contrôleur par défaut et la méthode `Index` comme méthode d'action par défaut. Les paramètres de route par défaut n'ont pas besoin d'être présents dans le chemin de l'URL pour une correspondance.

Si nous n'ajoutons aucun nom de contrôleur dans l'URL, alors il prendra `ExpenseController` comme contrôleur par défaut et la méthode `Index` de `ExpenseController` comme méthode d'action par défaut.

De même, si nous ajoutons uniquement `/Expense` à l'URL, il naviguera vers la méthode d'action `Index` du contrôleur Expense.

### Démonstration d'exécution

Appuyez sur F5 pour lancer l'application. Vous pouvez voir une page similaire à celle montrée ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/5HefeZhwLyl19br2rRQfo9jG7cFbASxDk77m)

Ici, nous avons un bouton « Ajouter une dépense » pour ajouter un nouveau rapport de dépenses. Le bouton « Rapport de dépenses » ouvrira une boîte de dialogue pour montrer le graphique à barres des données de dépenses mensuelles et hebdomadaires. Dans le coin supérieur droit, nous avons une boîte de recherche pour rechercher les enregistrements en utilisant le nom de l'article.

Regardez l'image GIF ci-dessous pour la démonstration de l'application :

![Image](https://cdn-media-1.freecodecamp.org/images/puUdMVO3Vug0wmuTAMxsLEGjbbOW-kIrP-12)

### Conclusion

Nous avons créé une application de gestionnaire de dépenses personnel en utilisant ASP.NET Core et Entity Framework Core avec l'aide de Visual Studio 2017 et SQL Server 2017. Nous avons également utilisé Highcharts pour créer un graphique à barres pour le résumé des dépenses mensuelles et hebdomadaires.

Veuillez télécharger le code source depuis [GitHub](https://github.com/AnkitSharma-007/ExpenseManager-ASPCore-EFCore-Highchart) et explorez-le pour mieux comprendre.

Vous pouvez lire mes autres articles sur ASP .NET Core [ici](http://ankitsharmablogs.com/category/asp-net-core/).

Vous préparez-vous pour des entretiens ? Lisez mon article sur [C# Coding Questions For Technical Interviews](http://ankitsharmablogs.com/csharp-coding-questions-for-technical-interviews/).

### Autres ressources utiles

* [CRUD Operation With ASP.NET Core MVC Using Visual Studio Code and EF](http://ankitsharmablogs.com/crud-operation-asp-net-core-mvc-using-visual-studio-code-ef/)
* [ASP.NET Core — CRUD With React.js And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-with-react-js-and-entity-framework-core/)
* [ASP.NET Core — CRUD Using Angular 5 And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-angular-5-and-entity-framework-core/)
* [CRUD Operation With ASP.NET Core MVC Using ADO.NET and Visual Studio 2017](http://ankitsharmablogs.com/crud-operation-with-asp-net-core-mvc-using-ado-net/)
* [CRUD Operation With ASP.NET Core MVC using Visual Studio Code and ADO.NET](http://ankitsharmablogs.com/crud-operation-with-asp-net-core-mvc-using-visual-studio-code-and-ado-net/)
* [ASP.NET Core — Using Highcharts With Angular 5](http://ankitsharmablogs.com/asp-net-core-using-highcharts-with-angular-5/)

Publié à l'origine sur [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)