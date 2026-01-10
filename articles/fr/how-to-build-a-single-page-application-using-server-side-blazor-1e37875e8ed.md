---
title: Comment créer une application monopage en utilisant Blazor côté serveur
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
seo_title: Comment créer une application monopage en utilisant Blazor côté serveur
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we will create a Single Page Application (SPA) using server-side
  Blazor. We will use an Entity Framework Core database. Single-Page Applications
  are web applications that load a single HTML page. They dyn...'
---

Par Ankit Sharma

### Introduction

Dans cet article, nous allons créer une application monopage (SPA) en utilisant Blazor côté serveur. Nous allons utiliser une base de données Entity Framework Core. Les applications monopages sont des applications web qui chargent une seule page HTML. Elles mettent à jour cette page dynamiquement lorsque l'utilisateur interagit avec l'application.

Nous allons créer un système de gestion des dossiers des employés. Nous allons effectuer des opérations CRUD dessus. Une fenêtre modale affichera le formulaire pour gérer les entrées utilisateur. Le formulaire comportera également une liste déroulante qui sera liée à une table de la base de données. Nous fournirons également une option de filtre à l'utilisateur pour filtrer les dossiers des employés en fonction du nom de l'employé.

Nous allons utiliser Visual Studio 2017 et SQL Server 2017 pour notre démonstration.

Regardons l'application finale :

![Image](https://cdn-media-1.freecodecamp.org/images/aI57jsCNIw1NRiqTqY99wr3rwJBCf-vE-FgP)

### Qu'est-ce que Blazor côté serveur ?

La version 0.5.0 de Blazor nous permet d'exécuter des applications Blazor sur le serveur. Cela signifie que nous pouvons exécuter le composant Blazor côté serveur sur .NET Core. Une connexion SignalR via le réseau gérera d'autres fonctionnalités telles que les mises à jour de l'interface utilisateur, la gestion des événements et les appels d'interopérabilité JavaScript.

Pour plus d'informations, consultez mon article précédent sur [Comprendre Blazor côté serveur](http://ankitsharmablogs.com/understanding-server-side-blazor/).

### Prérequis

* Installer le SDK .NET Core 2.1 ou supérieur depuis [ici](https://www.microsoft.com/net/learn/get-started-with-dotnet-tutorial#windowscmd)
* Installer Visual Studio 2017 v15.7 ou supérieur depuis [ici](https://visualstudio.microsoft.com/downloads/)
* Installer l'extension ASP.NET Core Blazor Language Services depuis [ici](https://marketplace.visualstudio.com/items?itemName=aspnet.blazor)
* SQL Server 2012 ou supérieur.

Les versions de Visual Studio 2017 antérieures à v15.7 ne supportent pas le framework Blazor.

### Code source

Obtenez le code source de cette application depuis [GitHub](https://github.com/AnkitSharma-007/Blazor-Server-Side-SPA).

Note importante :

**Cet article est valable pour la version 0.5.0 de Blazor. Blazor côté serveur pourrait subir des changements majeurs dans les futures versions de Blazor.**

### Création d'une table

Nous allons utiliser deux tables pour stocker nos données.

1. Employee : Utilisée pour stocker les détails des employés. Elle contient des champs tels que EmployeeID, Name, City, Department et Gender.
2. Cities : Cette table contient la liste des villes. Elle est utilisée pour remplir le champ _City_ de la table Employee. Elle contient deux champs, CityID et CityName.

Exécutez les commandes suivantes pour créer les deux tables :

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

Maintenant, nous allons insérer des données dans la table Cities. Nous allons utiliser cette table pour lier une liste déroulante dans notre application web. L'utilisateur sélectionnera la ville souhaitée dans cette liste déroulante. Utilisez les instructions d'insertion suivantes :

```sql
INSERT INTO Cities VALUES('New Delhi');  
INSERT INTO Cities VALUES('Mumbai');  
INSERT INTO Cities VALUES('Hyderabad');  
INSERT INTO Cities VALUES('Chennai');  
INSERT INTO Cities VALUES('Bengaluru');
```

Maintenant, notre partie base de données est complète. Nous allons donc procéder à la création de l'application côté serveur en utilisant Visual Studio 2017.

### Créer l'application Blazor côté serveur

Ouvrez Visual Studio et sélectionnez Fichier >> Nouveau >> Projet.

Après avoir sélectionné le projet, une boîte de dialogue "Nouveau Projet" s'ouvrira. Sélectionnez .NET Core dans le menu Visual C# du panneau de gauche. Ensuite, sélectionnez "Application Web ASP.NET Core" parmi les types de projets disponibles. Pour le nom du projet, mettez _ServerSideSPA_ et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/189S93tL5-3DZBX5e4h0rd9jgLOAla4DHA1V)

Après avoir cliqué sur OK, une nouvelle boîte de dialogue s'ouvrira vous demandant de sélectionner le modèle de projet. Vous verrez deux menus déroulants en haut à gauche de la fenêtre de modèle. Sélectionnez ".NET Core" et "ASP.NET Core 2.1" dans ces menus déroulants. Ensuite, sélectionnez le modèle "Blazor (côté serveur dans ASP.NET Core)" et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/koiBPXcDf1INRT--9ZBVhLcDMJ8WIqy9w7PU)

Cela créera notre solution Blazor côté serveur. Vous pouvez observer la structure des dossiers dans l'explorateur de solutions, comme montré dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/dBOrb-cKYR8pXh04n7IE1jA71yP-nZTiR1Hv)

La solution contient deux fichiers de projet :

1. ServerSideSPA.App : C'est notre application Blazor côté serveur. Ce projet contient toute la logique de nos composants et nos services. Nous créerons également nos modèles et notre couche d'accès aux données dans ce projet.
2. ServerSideSPA.Server : C'est l'application hébergée ASP.NET Core. Au lieu de s'exécuter côté client dans le navigateur, l'application Blazor côté serveur s'exécutera dans l'application hôte ASP.NET Core.

Dans les futures versions de Blazor, ces deux projets pourraient être fusionnés en un seul. Mais pour l'instant, la séparation est nécessaire en raison des différences dans le modèle de compilation de Blazor.

### Échafaudage du modèle vers l'application

Nous utilisons l'approche "database first" d'Entity Framework Core pour créer nos modèles. Nous allons créer notre classe de modèle dans le projet _ServerSideSPA.App_.

Naviguez vers Outils >> Gestionnaire de packages NuGet >> Console du gestionnaire de packages. Sélectionnez "ServerSideSPA.App" dans le menu déroulant Projet par défaut. Référez-vous à l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/apHcquWdcINo4yx7ZTRSY4GVrQSPOsyTWp8m)

Tout d'abord, nous allons installer le package pour le fournisseur de base de données que nous ciblons, qui est SQL Server dans ce cas. Exécutez donc la commande suivante :

```
Install-Package Microsoft.EntityFrameworkCore.SqlServer
```

Puisque nous utilisons les outils Entity Framework pour créer un modèle à partir de la base de données existante, nous allons également installer le package d'outils. Exécutez donc la commande suivante :

```
Install-Package Microsoft.EntityFrameworkCore.Tools
```

Après avoir installé les deux packages, nous allons échafauder notre modèle à partir des tables de la base de données en utilisant la commande suivante :

```
Scaffold-DbContext "Votre chaîne de connexion ici" Microsoft.EntityFrameworkCore.SqlServer -OutputDir Models -Tables Employee, Cities
```

N'oubliez pas de mettre votre propre chaîne de connexion (à l'intérieur de " "). Après l'exécution de cette commande, elle crée un dossier models dans le projet _ServerSideSPA.App_. Il contient trois fichiers de classe : _myTestDBContext.cs, Cities.cs_ et _Employee.cs_. Ainsi, nous avons échafaudé nos modèles avec succès en utilisant l'approche "database first" d'EF Core.

### Création de la couche d'accès aux données pour l'application

Faites un clic droit sur le projet ServerSideSPA.App, puis sélectionnez Ajouter >> Nouveau dossier et nommez le dossier Data_Access. Nous ajouterons notre classe pour gérer les opérations liées à la base de données uniquement dans ce dossier.

Faites un clic droit sur le dossier _DataAccess_ et sélectionnez Ajouter >> Classe.

Nommez votre classe _EmployeeDataAccessLayer.cs_. Ouvrez _EmployeeDataAccessLayer.cs_ et mettez le code suivant dedans :

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

        //Pour obtenir tous les détails des employés     
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

        //Pour ajouter un nouvel enregistrement d'employé       
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

        //Pour mettre à jour les enregistrements d'un employé particulier      
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

        //Obtenir les détails d'un employé particulier      
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

        //Pour supprimer l'enregistrement d'un employé particulier      
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

        // Pour obtenir la liste des villes
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

Ici, nous avons défini les méthodes pour gérer les opérations de la base de données :

* _GetAllEmployees_ récupérera tous les données des employés de la table Employee.
* _AddEmployee_ créera un nouvel enregistrement d'employé.
* _UpdateEmployee_ mettra à jour l'enregistrement d'un employé existant.
* _GetEmployeeData_ récupérera l'enregistrement de l'employé correspondant à l'ID d'employé qui lui est passé.
* _DeleteEmployee_ supprimera l'enregistrement de l'employé correspondant à l'ID d'employé qui lui est passé.
* _GetCityData_ récupérera la liste de toutes les villes de la table _Cities_.

### Création de la classe de service

Faites un clic droit sur le dossier _Services_ et sélectionnez Ajouter >> Classe. Donnez-lui le nom "EmployeeService.cs" et cliquez sur Ajouter. Cela ajoutera la classe EmployeeService au dossier Services.

Ouvrez EmployeeService.cs et mettez le code suivant dedans :

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

Nous allons invoquer les méthodes de la classe _EmployeeDataAccessLayer_ depuis notre service. Le service sera injecté dans nos composants. Les composants appelleront les méthodes du service pour accéder à la base de données.

À ce stade, le projet ServerSideSPA.App a la structure suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/fG4Y1m1kRP7kxp4yRSZ1OxoNQ2BLyuFw2jA2)

### Configuration du service

Pour rendre le service disponible pour les composants, nous devons le configurer sur l'application côté serveur. Ouvrez le fichier ServerSideSPA.App >> Startup.cs. Ajoutez la ligne suivante à l'intérieur de la méthode ConfigureServices de la classe Startup.

```cs
services.AddSingleton<EmployeeService>();
```

Référez-vous à l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/jCNjuzfmweuNj40kQePIJR1lxoIZRDnRdvzh)

Maintenant, nous allons procéder à la création de notre composant de vue.

### Création du composant de vue

Nous allons ajouter la page Razor dans le dossier _ServerSideSPA.App /Pages_. Par défaut, nous avons les pages "Counter" et "Fetch Data" fournies dans notre application. Ces pages par défaut n'affecteront pas notre application. Pour simplifier ce tutoriel, supprimez-les du dossier _ServerSideSPA.App /Pages_.

Faites un clic droit sur le dossier ServerSideSPA.App _/Pages_ puis sélectionnez Ajouter >> Nouvel élément. Une boîte de dialogue "Ajouter un nouvel élément" s'ouvrira. Sélectionnez "ASP.NET Core" dans le panneau de gauche. Ensuite, sélectionnez "Page Razor" dans le panneau des modèles et nommez-la EmployeeData._cshtml. Cliquez sur Ajouter.

![Image](https://cdn-media-1.freecodecamp.org/images/ZfAJA4ZPi6uK8snnXGwPmJFH5vrlzyOOLmZW)

Cela ajoutera une page _EmployeeData.cshtml_ au dossier _Pages_. Cette page Razor aura deux fichiers, _EmployeeData.cshtml_ et _EmployeeData.cshtml.cs_.

Maintenant, nous allons ajouter du code à ces pages.

### EmployeeData.cshtml

Ouvrez la page _EmployeeData.cshtml_ et mettez le code suivant dedans :

```cs
@page "/fetchemployee"
@inherits EmployeeDataModel

<h1>Données des employés</h1>
<p>Ce composant démontre l'opération CRUD sur les données des employés</p>

<div>
    <div style="float:left">
        <button class="btn btn-primary" onclick="@AddEmp">Ajouter un employé</button>
    </div>
    <div style="float:right; width:40%;">
        <div class="col-sm-6" style="float:left">
            <input class="form-control" type="text" placeholder="Rechercher" bind="@SearchString" />
        </div>
        <div>
            <button type="submit" class="btn btn-default btn-info" onclick="@FilterEmp">Filtrer</button>
        </div>
    </div>
</div>

@if (empList == null)
{
    <p><em>Chargement...</em></p>
}
else
{
    <table class='table'>
        <thead>
            <tr>
                <th>ID</th>
                <th>Nom</th>
                <th>Genre</th>
                <th>Département</th>
                <th>Ville</th>
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
                        <button class="btn btn-default" onclick="@(async () => await EditEmployee(@emp.EmployeeId))">Modifier</button>
                        <button class="btn btn-danger" onclick="@(async () => await DeleteConfirm(@emp.EmployeeId))">Supprimer</button>
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
                                <label for="Name" class="control-label">Nom</label>
                                <input for="Name" class="form-control" bind="@emp.Name" />
                            </div>
                            <div class="form-group">
                                <label asp-for="Gender" class="control-label">Genre</label>
                                <select asp-for="Gender" class="form-control" bind="@emp.Gender">
                                    <option value="">-- Sélectionner le genre --</option>
                                    <option value="Male">Homme</option>
                                    <option value="Female">Femme</option>
                                </select>
                            </div>
                            <div class="form-group">
                                <label asp-for="Department" class="control-label">Département</label>
                                <input asp-for="Department" class="form-control" bind="@emp.Department" />
                            </div>
                            <div class="form-group">
                                <label asp-for="City" class="control-label">Ville</label>
                                <select asp-for="City" class="form-control" bind="@emp.City">
                                    <option value="">-- Sélectionner la ville --</option>
                                    @foreach (var city in cityList)
                                    {
                                        <option value="@city.CityName">@city.CityName</option>
                                    }
                                </select>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button class="btn btn-block btn-info" onclick="@(async () => await SaveEmployee())" data-dismiss="modal">Enregistrer</button>
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
                        <h3 class="modal-title">Supprimer l'employé</h3>
                    </div>
                    <div class="modal-body">
                        <h4>Voulez-vous supprimer cet employé ??</h4>
                        <table class="table">
                            <tr>
                                <td>Nom</td>
                                <td>@emp.Name</td>
                            </tr>
                            <tr>
                                <td>Genre</td>
                                <td>@emp.Gender</td>
                            </tr>
                            <tr>
                                <td>Département</td>
                                <td>@emp.Department</td>
                            </tr>
                            <tr>
                                <td>Ville</td>
                                <td>@emp.City</td>
                            </tr>
                        </table>
                    </div>
                    <div class="modal-footer">
                        <button class="btn btn-danger" onclick="@(async () => await DeleteEmployee(emp.EmployeeId))" data-dismiss="modal">OUI</button>
                        <button class="btn btn-warning" onclick="@closeModal">NON</button>
                    </div>
                </div>
            </div>
        </div>
    }
}
```

Permettez-moi d'expliquer ce code. En haut, nous avons défini la route pour cette page comme "fetchemployee". Cela signifie que si nous ajoutons "fetchemployee" à l'URL racine de l'application, nous serons redirigés vers cette page.

Nous héritons également de la classe _EmployeeDataModel_ qui est définie dans le fichier _EmployeeData.cshtml.cs_. Cela nous permettra d'utiliser les méthodes définies dans la classe EmployeeDataModel.

Après cela, nous avons défini un bouton pour ajouter un nouvel enregistrement d'employé. Lorsqu'il est cliqué, ce bouton ouvrira une fenêtre modale pour gérer les entrées utilisateur.

Nous avons également défini une boîte de recherche et un bouton correspondant pour filtrer les enregistrements des employés en fonction du nom de l'employé. Si vous entrez un nom d'employé et cliquez sur le bouton de filtre, il affichera tous les enregistrements d'employés correspondants. Si nous cliquons sur le bouton de filtre sans entrer de valeur dans la boîte de recherche, il retournera tous les enregistrements d'employés.

Les enregistrements des employés retournés par la base de données sont stockés dans la variable _empList_. Si la variable n'est pas nulle, alors nous lierons les valeurs à un tableau pour afficher les enregistrements des employés sous forme de tableau. Chaque enregistrement d'employé aura également deux liens d'action — _Modifier_ pour modifier l'enregistrement de l'employé, et _Supprimer_ pour supprimer l'enregistrement de l'employé.

Pour gérer les entrées utilisateur, nous utilisons un formulaire. Nous utilisons un seul formulaire pour les fonctionnalités d'ajout et de modification d'employé. Le formulaire est défini dans une fenêtre modale. La fenêtre modale est affichée à l'écran en fonction de la valeur de la propriété booléenne isAdd. La valeur de cette propriété booléenne est définie dans la page de code-behind (.cshtml.cs).

La liste déroulante des villes dans le formulaire est liée à notre table Cities dans la base de données à l'aide de la variable _cityList_. La cityList sera remplie au démarrage de l'application.

Le formulaire aura un bouton _Enregistrer_ qui invoquera la méthode SaveEmployee. Cette méthode est définie dans le fichier de code-behind pour ajouter ou mettre à jour un enregistrement d'employé.

Similaire à la fenêtre modale _Ajouter_, nous avons également une fenêtre modale _Supprimer_. Ce sera une fenêtre modale en lecture seule et demandera une confirmation pour supprimer un enregistrement d'employé. En cliquant sur "Oui", elle invoquera la méthode _DeleteEmployee_ pour supprimer l'enregistrement de l'employé.

### EmployeeData.cshtml.cs

Ouvrez _EmployeeData.cshtml.cs_ et mettez le code suivant dedans.

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
            this.modalTitle = "Ajouter un employé";
            this.isAdd = true;
        }

        protected async Task EditEmployee(int empID)
        {
            emp = await employeeService.Details(empID);
            this.modalTitle = "Modifier l'employé";
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

Permettez-moi d'expliquer ce code. Nous avons défini une classe _EmployeeDataModel_. Elle contiendra toutes les méthodes que nous utiliserons dans la page _EmployeeData.cshtml_.

Nous injectons notre _EmployeeService_ dans la classe _EmployeeDataModel_ afin que les méthodes côté client puissent invoquer nos services.

Les variables _empList_ et _cityList_ contiennent les données des tables Employee et Cities. Les variables sont remplies dans OnInitAsync pour s'assurer que les données sont disponibles lorsque la page se charge.

Nous utiliserons la méthode _FilterEmp_ pour filtrer les données des employés en fonction de la propriété du nom de l'employé. Cette propriété ignorera la casse du texte de la chaîne de recherche. Elle retourne tous les enregistrements qui correspondent entièrement ou partiellement à la chaîne de recherche.

En cliquant sur le bouton "Ajouter un employé", la méthode _AddEmp_ sera invoquée. Elle initialisera une instance vide du modèle Employee et définira la valeur du drapeau booléen _isAdd_ à vrai. Cela ouvrira une fenêtre modale avec un formulaire, demandant à l'utilisateur d'entrer un nouvel enregistrement d'employé. De même, nous avons défini une méthode _EditEmployee_. Elle récupère l'enregistrement de l'employé en fonction de l'ID de l'employé pour lequel elle est invoquée. Elle définira également la valeur de _isAdd_ à vrai pour ouvrir la fenêtre modale afin de modifier l'enregistrement de l'employé.

La méthode _SaveEmployee_ vérifiera si elle est invoquée pour ajouter un nouvel enregistrement d'employé ou pour modifier un enregistrement d'employé existant. Si la propriété EmployeeId est définie, alors il s'agit d'une demande de "modification", et nous invoquerons la méthode Edit de notre service. Si EmployeeId n'est pas défini, alors il s'agit d'une demande de "création", et nous invoquerons la méthode Create de notre service. Nous récupérerons ensuite l'enregistrement de l'employé mis à jour en appelant la méthode _GetEmployee_ et définirons également la valeur de _isAdd_ à false, fermant ainsi la fenêtre modale.

La méthode _DeleteConfirm_ est invoquée en cliquant sur le bouton Supprimer correspondant à un enregistrement d'employé. Elle définira la valeur du drapeau booléen isDelete à vrai. Cela affichera une fenêtre modale de confirmation de suppression. En cliquant sur OUI dans cette fenêtre, la méthode DeleteEmployee est invoquée. Cela supprimera l'enregistrement de l'employé et définira le drapeau booléen _isDelete_ à faux pour fermer la fenêtre modale.

### Ajout du lien au menu de navigation

La dernière étape consiste à ajouter le lien vers notre page "EmployeeData" dans le menu de navigation. Ouvrez la page _ServerSideSPA.App/Shared/NavMenu.cshtml_ et mettez le code suivant dedans :

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
                <span class="oi oi-home" aria-hidden="true"></span> Accueil
            </NavLink>
        </li>
        <li class="nav-item px-3">
            <NavLink class="nav-link" href="fetchemployee">
                <span class="oi oi-list-rich" aria-hidden="true"></span> Récupérer les employés
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

Cela complète notre application monopage utilisant Blazor côté serveur.

### Démonstration d'exécution

Appuyez sur F5 pour lancer l'application.

Une page web s'ouvrira comme montré dans l'image ci-dessous. Le menu de navigation à gauche montre un lien de navigation vers la page des données des employés.

![Image](https://cdn-media-1.freecodecamp.org/images/dRbCSiMHUSfAh-saQWs4F0zQYNRhxXGcOnPa)

En cliquant sur le lien "Données des employés", vous serez redirigé vers la vue EmployeeData. Ici, vous pouvez voir toutes les données des employés sur la page. Remarquez que l'URL a "fetchemployee" ajouté à celle-ci.

![Image](https://cdn-media-1.freecodecamp.org/images/7etEYM3gWebYu79-hS0AGSGaIGrHGlBT27YX)

Cliquez sur le bouton _Ajouter un employé_ pour ouvrir la fenêtre modale "Ajouter un employé". Entrez les données dans tous les champs et cliquez sur Enregistrer pour créer un nouvel enregistrement d'employé.

![Image](https://cdn-media-1.freecodecamp.org/images/bFeFopdYlNO0e7K93KBNclUZyhiY5OQ5z65Q)

Cela créera un nouvel enregistrement d'employé et affichera les données dans le tableau de vue. Ajoutez quelques autres enregistrements, et la vue sera similaire à celle montrée ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/zscFfBz2XUJcQkWomqHYqZez9pI6sX6nXlBD)

En cliquant sur le bouton Modifier, vous ouvrirez la fenêtre modale pour modifier l'enregistrement de l'employé. Modifiez les champs d'entrée et cliquez sur Enregistrer pour mettre à jour l'enregistrement de l'employé.

![Image](https://cdn-media-1.freecodecamp.org/images/JzSm73w1LdEDHCFex9p8AuvfcZNEJXq30rs5)

Pour filtrer les enregistrements des employés, entrez le nom de l'employé dans la boîte de recherche et cliquez sur le bouton Filtrer. Le texte de recherche est indépendant de la casse. L'opération de filtre retournera tous les enregistrements des employés correspondant au nom entré dans le champ de recherche. Référez-vous à l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/SWi6lzLgiTQ-4rRVRMtGX7zycc6E-xm3wvYy)

Si vous cliquez sur le bouton Supprimer correspondant à l'enregistrement de l'employé, cela ouvrira une fenêtre de confirmation de suppression demandant une confirmation pour supprimer l'enregistrement de l'employé.

![Image](https://cdn-media-1.freecodecamp.org/images/zP0C6qdbR7jYKJZh2IzN7nKSjCHBQLGPf4ZZ)

En cliquant sur OUI, cela supprimera les données de l'employé et affichera la liste mise à jour des employés en actualisant le tableau de vue.

### Conclusion

Nous avons créé une application Blazor côté serveur en utilisant l'approche "database first" d'Entity Framework Core avec l'aide de Visual Studio 2017 et SQL Server 2017. Nous avons utilisé une fenêtre modale pour gérer les entrées utilisateur via un formulaire. Nous avons également implémenté la fonctionnalité de recherche sur les enregistrements des employés.

Veuillez obtenir le code source depuis [GitHub](https://github.com/AnkitSharma-007/Blazor-Server-Side-SPA) et jouez avec pour obtenir une meilleure compréhension.

Obtenez mon livre [Blazor Quick Start Guide](https://www.amazon.com/Blazor-Quick-Start-Guide-applications/dp/178934414X/ref=sr_1_1?ie=UTF8&qid=1542438251&sr=8-1&keywords=Blazor-Quick-Start-Guide) pour en savoir plus sur Blazor.

Vous pouvez consulter mes autres articles sur Blazor [ici](http://ankitsharmablogs.com/category/blazor/).

Vous préparez des entretiens ? Lisez mon article sur [C# Coding Questions For Technical Interviews](http://ankitsharmablogs.com/csharp-coding-questions-for-technical-interviews/)

### Voir aussi

* [ASP.NET Core — Getting Started With Blazor](http://ankitsharmablogs.com/asp-net-core-getting-started-with-blazor/)
* [ASP.NET Core — CRUD Using Blazor And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-blazor-and-entity-framework-core/)
* [Cascading DropDownList In Blazor Using EF Core](http://ankitsharmablogs.com/cascading-dropdownlist-in-blazor-using-ef-core/)
* [Creating an SPA Using Razor Pages With Blazor](http://ankitsharmablogs.com/creating-a-spa-using-razor-pages-with-blazor/)
* [Deploying a Blazor Application on IIS](http://ankitsharmablogs.com/deploying-a-blazor-application-on-iis/)

Publié à l'origine sur [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)