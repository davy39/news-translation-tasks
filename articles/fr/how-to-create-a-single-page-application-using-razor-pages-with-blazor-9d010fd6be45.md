---
title: Comment créer une application monopage en utilisant Razor Pages avec Blazor
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-11T16:21:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-single-page-application-using-razor-pages-with-blazor-9d010fd6be45
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vVXicFhmOOyYASuzkM570w.jpeg
tags:
- name: entity framework
  slug: entity-framework
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: ' Single Page Applications '
  slug: single-page-applications
- name: technology
  slug: technology
seo_title: Comment créer une application monopage en utilisant Razor Pages avec Blazor
seo_desc: 'By Ankit Sharma

  In this article, we are going to create a Single Page Application (SPA) using Razor
  pages in Blazor, with the help of the Entity Framework Core database first approach.

  Introduction

  Single Page Application (SPAs) are web applications ...'
---

Par Ankit Sharma

Dans cet article, nous allons créer une application monopage (SPA) en utilisant Razor Pages dans Blazor, avec l'aide de l'approche Entity Framework Core "database first".

### Introduction

Les applications monopage (SPA) sont des applications web qui chargent une seule page HTML et mettent à jour dynamiquement cette page lorsque l'utilisateur interagit avec l'application. Nous allons créer un système de gestion des dossiers des employés et effectuer des opérations CRUD dessus.

Nous utiliserons Visual Studio 2017 et SQL Server 2014.

Jetez un œil à l'application finale.

![Image](https://cdn-media-1.freecodecamp.org/images/pA8DDQa-ek6BJEKFbMN8ukjS2nv8fFxMJ9In)

### Prérequis

* Installer le SDK .NET Core 2.1 Preview 2 depuis [ici](https://www.microsoft.com/net/download/dotnet-core/sdk-2.1.300-preview2)
* Installer Visual Studio 2017 v15.7 ou supérieur depuis [ici](https://www.visualstudio.com/downloads/)
* Installer l'extension ASP.NET Core Blazor Language Services depuis [ici](https://marketplace.visualstudio.com/items?itemName=aspnet.blazor)
* SQL Server 2008 ou supérieur

Le framework Blazor n'est pas supporté par les versions antérieures à Visual Studio 2017 v15.7.

### Code source

Obtenez le code source depuis [GitHub](https://github.com/AnkitSharma-007/SPA-With-Blazor).

### Création de la table

Nous allons utiliser une table de base de données pour stocker tous les enregistrements des employés.

Ouvrez SQL Server et utilisez le script suivant pour créer la table `Employee`.

```
CREATE TABLE Employee (
  EmployeeID int IDENTITY(1,1) PRIMARY KEY,
  Name varchar(20) NOT NULL,
  City varchar(20) NOT NULL,
  Department varchar(20) NOT NULL,
  Gender varchar(6) NOT NULL
)
```

### Création de l'application web Blazor

Ouvrez Visual Studio et sélectionnez "Fichier" > "Nouveau" > "Projet".

Après avoir sélectionné le projet, une boîte de dialogue "Nouveau Projet" s'ouvrira. Dans le panneau de gauche, sélectionnez ".NET Core" dans le menu Visual C#. Ensuite, sélectionnez "Application Web ASP.NET Core" parmi les types de projets disponibles. Donnez le nom du projet "BlazorSPA" et appuyez sur "OK".

![Image](https://cdn-media-1.freecodecamp.org/images/Mzs4TvnFTePBJQ5wDxkyXwI7VFBjDHUAVZ4e)

Après avoir cliqué sur "OK", une nouvelle boîte de dialogue s'ouvrira vous demandant de sélectionner le modèle de projet. Vous pouvez observer deux menus déroulants en haut à gauche de la fenêtre de modèle. Sélectionnez ".NET Core" et "ASP.NET Core 2.0" dans ces menus déroulants. Ensuite, sélectionnez le modèle "Blazor (hébergé ASP.NET Core)" et appuyez sur "OK".

![Image](https://cdn-media-1.freecodecamp.org/images/GyYuYmaGwKBRknv04cVsMhZzS65vVbH7qRm3)

Notre solution Blazor sera maintenant créée. Vous pouvez observer la structure des dossiers dans l'Explorateur de solutions comme montré dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/n69NyMxPfNGl7qLqWWrx8YmQOiQeXJy6qUyN)

Vous pouvez observer que nous avons trois fichiers de projet créés dans cette solution.

1. BlazorSPA.Client — contient le code côté client et les pages qui seront rendues dans le navigateur.
2. BlazorSPA.Server — contient le code côté serveur tel que les opérations liées à la base de données et l'API web.
3. BlazorSPA.Shared — contient le code partagé qui peut être accessible à la fois par le client et le serveur. Il contient nos classes de modèle.

### Échafaudage du modèle dans l'application

Nous utilisons l'approche Entity Framework Core "database first" pour créer nos modèles. Nous allons créer notre classe de modèle dans le projet "BlazorSPA.Shared" afin qu'elle soit accessible à la fois par le client et le serveur.

Accédez à "Outils" > "Gestionnaire de packages NuGet" > "Console du gestionnaire de packages". Sélectionnez "BlazorSPA.Shared" dans le menu déroulant "Projet par défaut". Référez-vous à l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/SjjP3ntvRWEycZ-3dX20CSBzezpMxs645EGF)

Tout d'abord, nous allons installer le package pour le fournisseur de base de données que nous ciblons, qui est SQL Server dans ce cas. Exécutez la commande suivante :

```
Install-Package Microsoft.EntityFrameworkCore.SqlServer
```

Puisque nous utilisons les outils Entity Framework pour créer un modèle à partir de la base de données existante, nous allons également installer le package d'outils. Exécutez la commande suivante :

```
Install-Package Microsoft.EntityFrameworkCore.Tools
```

Après avoir installé les deux packages, nous allons échafauder notre modèle à partir des tables de la base de données en utilisant la commande suivante :

```
Scaffold-DbContext "Votre chaîne de connexion ici" Microsoft.EntityFrameworkCore.SqlServer -OutputDir Models -Tables Employee
```

**N'oubliez pas** de mettre votre propre chaîne de connexion (à l'intérieur de `""`). Après l'exécution réussie de cette commande, vous pouvez observer qu'un dossier "Models" a été créé. Il contient deux fichiers de classe, "myTestDBContext.cs" et "Employee.cs". Ainsi, nous avons échafaudé avec succès nos modèles en utilisant l'approche Entity Framework Core "database first".

À ce stade, le dossier Models aura la structure suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/gY0lV5KolvXUTFdFkN-gnXvzb0aObcOmAXZz)

### Création de la couche d'accès aux données pour l'application

Faites un clic droit sur le projet "BlazorSPA.Server" puis sélectionnez "Ajouter" > "Nouveau Dossier" et nommez le dossier "DataAccess". Nous ajouterons notre classe pour gérer les opérations liées à la base de données dans ce dossier.

Faites un clic droit sur le dossier "DataAccess" et sélectionnez "Ajouter" > "Classe". Nommez votre classe "EmployeeDataAccessLayer.cs".

Ouvrez "EmployeeDataAccessLayer.cs" et mettez le code suivant dedans :

```
using BlazorSPA.Shared.Models;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorSPA.Server.DataAccess
{
    public class EmployeeDataAccessLayer
    {
        myTestDBContext db = new myTestDBContext();

        // Pour obtenir tous les détails des employés
        public IEnumerable<Employee> GetAllEmployees()
        {
            try
            {
                return db.Employee.ToList();
            }
            catch
            {
                throw;
            }
        }

        // Pour ajouter un nouvel enregistrement d'employé
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

        // Pour mettre à jour les enregistrements d'un employé particulier
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

        // Obtenir les détails d'un employé particulier
        public Employee GetEmployeeData(int id)
        {
            try
            {
                Employee employee = db.Employee.Find(id);
                return employee;
            }
            catch
            {
                throw;
            }
        }

        // Pour supprimer l'enregistrement d'un employé particulier
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
    }
}
```

Ici, nous avons défini des méthodes pour gérer les opérations de base de données. `GetAllEmployees` récupérera toutes les données des employés depuis la table Employee. De même, `AddEmployee` créera un nouvel enregistrement d'employé, et `UpdateEmployee` mettra à jour l'enregistrement d'un employé existant. `GetEmployeeData` récupérera l'enregistrement de l'employé correspondant à l'ID d'employé passé, et `DeleteEmployee` supprimera l'enregistrement de l'employé correspondant à l'ID d'employé passé.

### Ajout du contrôleur d'API web à l'application

Faites un clic droit sur le dossier "BlazorSPA.Server/Controllers" et sélectionnez "Ajouter" > "Nouvel Élément". Une boîte de dialogue "Ajouter un nouvel élément" s'ouvrira. Sélectionnez "ASP.NET" dans le panneau de gauche, puis sélectionnez "Classe de contrôleur d'API" dans le panneau des modèles, et donnez le nom "EmployeeController.cs". Cliquez sur "Ajouter".

![Image](https://cdn-media-1.freecodecamp.org/images/OZjyShEwULZNifr-ZNzRWY0bjYkAaQKHMNeI)

Cela créera notre classe de contrôleur d'API `EmployeeController`.

Nous appellerons les méthodes de la classe `EmployeeDataAccessLayer` pour récupérer les données et les transmettre au côté client.

Ouvrez le fichier "EmployeeController.cs" et mettez le code suivant dedans :

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using BlazorSPA.Server.DataAccess;
using BlazorSPA.Shared.Models;
using Microsoft.AspNetCore.Mvc;

namespace BlazorSPA.Server.Controllers
{
    public class EmployeeController : Controller
    {
        EmployeeDataAccessLayer objemployee = new EmployeeDataAccessLayer();

        [HttpGet]
        [Route("api/Employee/Index")]
        public IEnumerable<Employee> Index()
        {
            return objemployee.GetAllEmployees();
        }

        [HttpPost]
        [Route("api/Employee/Create")]
        public void Create([FromBody] Employee employee)
        {
            if (ModelState.IsValid)
                objemployee.AddEmployee(employee);
        }

        [HttpGet]
        [Route("api/Employee/Details/{id}")]
        public Employee Details(int id)
        {
            return objemployee.GetEmployeeData(id);
        }

        [HttpPut]
        [Route("api/Employee/Edit")]
        public void Edit([FromBody]Employee employee)
        {
            if (ModelState.IsValid)
                objemployee.UpdateEmployee(employee);
        }

        [HttpDelete]
        [Route("api/Employee/Delete/{id}")]
        public void Delete(int id)
        {
            objemployee.DeleteEmployee(id);
        }
    }
}
```

À ce stade, notre projet "BlazorSPA.Server" a la structure suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/DnpONEsQobR0N3YDjCyWRteruR0P-8CvxFug)

Nous avons terminé avec notre logique backend. Par conséquent, nous allons maintenant procéder au codage de notre côté client.

### Ajout de la page Razor à l'application

Nous allons ajouter la page Razor dans le dossier "BlazorSPA.Client/Pages". Par défaut, nous avons les pages "Counter" et "Fetch Data" fournies dans notre application. Ces pages par défaut n'affecteront pas notre application mais, pour les besoins de ce tutoriel, nous allons supprimer les pages "fetchdata" et "counter" du dossier "BlazorSPA.Client/Pages".

Faites un clic droit sur le dossier "BlazorSPA.Client/Pages" puis sélectionnez "Ajouter" > "Nouvel Élément". Une boîte de dialogue "Ajouter un nouvel élément" s'ouvrira. Sélectionnez "ASP.NET Core" dans le panneau de gauche, puis sélectionnez "Page Razor" dans le panneau des modèles et nommez-la "EmployeeData.cshtml". Cliquez sur "Ajouter".

![Image](https://cdn-media-1.freecodecamp.org/images/tR2ue0vJJqAb0HROVGJxob8ZJy13WgbFUav7)

Cela ajoutera une page "EmployeeData.cshtml" à notre dossier "BlazorSPA.Client/Pages". Cette page Razor aura deux fichiers, "EmployeeData.cshtml" et "EmployeeData.cshtml.cs".

Maintenant, nous allons ajouter du code à ces pages.

### EmployeeData.cshtml.cs

Ouvrez "EmployeeData.cshtml.cs" et mettez le code suivant dedans :

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using BlazorSPA.Shared.Models;
using Microsoft.AspNetCore.Blazor;
using Microsoft.AspNetCore.Blazor.Components;
using Microsoft.AspNetCore.Blazor.Services;

namespace BlazorSPA.Client.Pages
{
    public class EmployeeDataModel : BlazorComponent
    {
        [Inject]
        protected HttpClient Http { get; set; }

        [Inject]
        protected IUriHelper UriHelper { get; set; }

        [Parameter]
        protected string paramEmpID { get; set; } = "0";

        [Parameter]
        protected string action { get; set; }

        protected List<Employee> empList = new List<Employee>();
        protected Employee emp = new Employee();
        protected string title { get; set; }

        protected override async Task OnParametersSetAsync()
        {
            if (action == "fetch")
            {
                await FetchEmployee();
                this.StateHasChanged();
            }
            else if (action == "create")
            {
                title = "Ajouter un employé";
                emp = new Employee();
            }
            else if (paramEmpID != "0")
            {
                if (action == "edit")
                {
                    title = "Modifier un employé";
                }
                else if (action == "delete")
                {
                    title = "Supprimer un employé";
                }
                emp = await Http.GetJsonAsync<Employee>("/api/Employee/Details/" + Convert.ToInt32(paramEmpID));
            }
        }

        protected async Task FetchEmployee()
        {
            title = "Données des employés";
            empList = await Http.GetJsonAsync<List<Employee>>("api/Employee/Index");
        }

        protected async Task CreateEmployee()
        {
            if (emp.EmployeeId != 0)
            {
                await Http.SendJsonAsync(HttpMethod.Put, "api/Employee/Edit", emp);
            }
            else
            {
                await Http.SendJsonAsync(HttpMethod.Post, "/api/Employee/Create", emp);
            }
            UriHelper.NavigateTo("/employee/fetch");
        }

        protected async Task DeleteEmployee()
        {
            await Http.DeleteAsync("api/Employee/Delete/" + Convert.ToInt32(paramEmpID));
            UriHelper.NavigateTo("/employee/fetch");
        }

        protected void Cancel()
        {
            title = "Données des employés";
            UriHelper.NavigateTo("/employee/fetch");
        }
    }
}
```

Comprenons ce code. Nous avons défini une classe `EmployeeDataModel` qui contiendra toutes nos méthodes que nous utiliserons dans la page "EmployeeData.cshtml".

Nous injectons le service `HttpClient` pour activer l'appel de l'API web et le service `IUriHelper` pour activer la redirection d'URL. Après cela, nous avons défini nos attributs de paramètre — `paramEmpID` et `action`. Ces paramètres sont utilisés dans "EmployeeData.cshtml" pour définir les routes de notre page. Nous avons également déclaré une propriété `title` pour afficher l'en-tête afin de spécifier l'action actuelle qui est en cours d'exécution sur la page.

La méthode `OnParametersSetAsync` est invoquée chaque fois que les paramètres d'URL sont définis pour la page. Nous vérifierons la valeur du paramètre `action` pour identifier l'opération actuelle sur la page.

Si l'action est définie sur `fetch`, alors nous invoquerons la méthode `FetchEmployee` pour récupérer la liste mise à jour des employés depuis la base de données et rafraîchir l'interface utilisateur en utilisant la méthode `StateHasChanged`.

Nous vérifierons si l'attribut d'action du paramètre est défini sur `create`, puis nous définirons le titre de la page sur "Ajouter un employé" et créerons un nouvel objet de type `Employee`. Si `paramEmpID` n'est pas "0", alors c'est soit une action `edit`, soit une action `delete`. Nous définirons la propriété title en conséquence, puis invoquerons notre méthode d'API web pour récupérer les données pour l'ID d'employé défini dans la propriété `paramEmpID`.

La méthode `FetchEmployee` définira le titre sur "Données des employés" et récupérera toutes les données des employés en invoquant notre méthode d'API web.

La méthode `CreateEmployee` vérifiera si elle est invoquée pour ajouter un nouvel enregistrement d'employé, ou pour modifier un enregistrement d'employé existant. Si la propriété `EmployeeId` est définie, alors c'est une requête `edit` et nous enverrons une requête PUT à l'API web. Si `EmployeeId` n'est pas défini, alors c'est une requête `create` et nous enverrons une requête POST à l'API web. Nous définirons la propriété `title` en fonction de la valeur correspondante de l'action, puis invoquerons notre méthode d'API web pour récupérer les données pour l'ID d'employé défini dans la propriété `paramEmpID`.

La méthode `DeleteEmployee` supprimera l'enregistrement de l'employé pour l'ID d'employé défini dans la propriété `paramEmpID`. Après la suppression, l'utilisateur est redirigé vers la page "/employee/fetch".

Dans la méthode `Cancel`, nous définirons la propriété title sur "Données des employés" et redirigerons l'utilisateur vers la page "/employee/fetch".

### EmployeeData.cshtml

Ouvrez la page "EmployeeData.cshtml" et mettez le code suivant dedans :

```
@page "/employee/{action}/{paramEmpID}"
@page "/employee/{action}"
@inherits EmployeeDataModel

<h1>@title</h1>

@if (action == "fetch")
{
    <p>
        <a href="/employee/create">Créer un nouveau</a>
    </p>
}

@if (action == "create" || action == "edit")
{
    <form>
        <table class="form-group">
            <tr>
                <td>
                    <label for="Name" class="control-label">Nom</label>
                </td>
                <td>
                    <input type="text" class="form-control" bind="@emp.Name" />
                </td>
                <td width="20"> </td>
                <td>
                    <label for="Department" class="control-label">Département</label>
                </td>
                <td>
                    <input type="text" class="form-control" bind="@emp.Department" />
                </td>
            </tr>
            <tr>
                <td>
                    <label for="Gender" class="control-label">Genre</label>
                </td>
                <td>
                    <select asp-for="Gender" class="form-control" bind="@emp.Gender">
                        <option value="">-- Sélectionner le genre --</option>
                        <option value="Male">Homme</option>
                        <option value="Female">Femme</option>
                    </select>
                </td>
                <td width="20"> </td>
                <td>
                    <label for="City" class="control-label">Ville</label>
                </td>
                <td>
                    <input type="text" class="form-control" bind="@emp.City" />
                </td>
            </tr>
            <tr>
                <td></td>
                <td>
                    <input type="submit" class="btn btn-success" onclick="@(async () => await CreateEmployee())" style="width:220px;" value="Enregistrer" />
                </td>
                <td></td>
                <td width="20"> </td>
                <td>
                    <input type="submit" class="btn btn-danger" onclick="@Cancel" style="width:220px;" value="Annuler" />
                </td>
            </tr>
        </table>
    </form>
}
else if (action == "delete")
{
    <div class="col-md-4">
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
        <div class="form-group">
            <input type="submit" class="btn btn-danger" onclick="@(async () => await DeleteEmployee())" value="Supprimer" />
            <input type="submit" value="Annuler" onclick="@Cancel" class="btn" />
        </div>
    </div>
}

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
                        <a href='/employee/edit/@emp.EmployeeId'>Modifier</a>  |
                        <a href='/employee/delete/@emp.EmployeeId'>Supprimer</a>
                    </td>
                </tr>
            }
        </tbody>
    </table>
}
```

En haut, nous avons défini les routes pour notre page. Il y a deux routes définies :

1. `/employee/{action}/{paramEmpID}` : Cela acceptera le nom de l'action ainsi que l'ID de l'employé. Cette route est invoquée lorsque nous effectuons une opération de modification ou de suppression. Lorsque nous appelons une action `edit` ou `delete` sur les données d'un employé particulier, l'ID de l'employé est également passé en tant que paramètre d'URL.
2. `/employee/{action}` : Cela n'acceptera que le nom de l'action. Cette route est invoquée lorsque nous créons de nouvelles données d'employé, ou lorsque nous récupérons les enregistrements de tous les employés.

Nous héritons également de la classe `EmployeeDataModel`, qui est définie dans le fichier "EmployeeData.cshtml.cs". Cela nous permettra d'utiliser les méthodes définies dans la classe `EmployeeDataModel`.

Après cela, nous définissons le titre qui sera affiché sur notre page. Le titre est dynamique et change en fonction de l'action qui est actuellement exécutée sur la page.

Nous afficherons le lien "Créer un nouveau" uniquement si l'action est `fetch`. Si l'action est `create` ou `edit`, alors le lien "Créer un nouveau" sera masqué et nous afficherons le formulaire pour obtenir l'entrée de l'utilisateur. À l'intérieur du formulaire, nous avons également défini les deux boutons "Enregistrer" et "Annuler". Cliquer sur "Enregistrer" invoquera la méthode `CreateEmployee`, tandis que cliquer sur "Annuler" invoquera la méthode `Cancel`.

Si l'action est `delete`, alors un tableau sera affiché avec les données de l'employé sur lequel l'action `delete` est invoquée. Nous affichons également deux boutons — "Supprimer" et "Annuler". Cliquer sur le bouton "Supprimer" invoquera la méthode `DeleteEmployee`, et cliquer sur "Annuler" invoquera la méthode `Cancel`.

À la fin, nous avons un tableau pour afficher toutes les données des employés depuis la base de données. Chaque enregistrement d'employé aura également deux liens d'action : "Modifier" pour modifier l'enregistrement de l'employé et "Supprimer" pour supprimer l'enregistrement de l'employé. Ce tableau est toujours affiché sur la page, et nous le mettrons à jour après chaque action.

### Ajout du lien au menu de navigation

La dernière étape consiste à ajouter le lien vers notre page "EmployeeData" dans le menu de navigation. Ouvrez la page "BlazorSPA.Client/Shared/NavMenu.cshtml" et mettez le code suivant dedans :

```
<div class="top-row pl-4 navbar navbar-dark">
    <a class="navbar-brand" href="/">BlazorSPA</a>
    <button class="navbar-toggler" onclick=@ToggleNavMenu>
        <span class="navbar-toggler-icon"></span>
    </button>
</div>

<div class=@(collapseNavMenu ? "collapse" : null) onclick=@ToggleNavMenu>
    <ul class="nav flex-column">
        <li class="nav-item px-3">
            <NavLink class="nav-link" href="/" Match=NavLinkMatch.All>
                <span class="oi oi-home" aria-hidden="true"></span> Accueil
            </NavLink>
        </li>
        <li class="nav-item px-3">
            <NavLink class="nav-link" href="/employee/fetch">
                <span class="oi oi-list-rich" aria-hidden="true"></span> Données des employés
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

Ainsi, nous avons créé avec succès une SPA en utilisant Blazor, avec l'aide de l'approche Entity Framework Core "database first".

### Démo d'exécution

Lancez l'application.

Une page web s'ouvrira comme montré dans l'image ci-dessous. Le menu de navigation à gauche montre le lien de navigation vers la page des données des employés.

![Image](https://cdn-media-1.freecodecamp.org/images/5aytCUZiGENxmbG8UmH3Kkn93L6QlmU3o90I)

Cliquer sur le lien "Données des employés" redirigera vers la vue "Données des employés". Ici, vous pouvez voir toutes les données des employés sur la page. Remarquez que l'URL a "employee/fetch" ajouté à celle-ci.

![Image](https://cdn-media-1.freecodecamp.org/images/e1LB246vIs1UwwYqU4hb7kgEqktwtXg6QxIW)

Nous n'avons ajouté aucune donnée, donc elle est vide. Cliquez sur "Créer un nouveau" pour ouvrir le formulaire "Ajouter un employé" afin d'ajouter de nouvelles données d'employé. Remarquez que l'URL a "employee/create" ajouté à celle-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/GhLUT-gjoQoOLHv8ldQElEqINjpFE-YoCyd4)

Après avoir inséré des données dans tous les champs, cliquez sur le bouton "Enregistrer". Le nouvel enregistrement d'employé sera créé, et le tableau des données des employés sera actualisé.

![Image](https://cdn-media-1.freecodecamp.org/images/VkPKhxGiT5Pg9aEjgZtsSiSqFdaT3fUnosFe)

Si nous voulons modifier un enregistrement d'employé existant, alors cliquez sur le lien d'action "Modifier". Il ouvrira la vue de modification comme montré ci-dessous. Ici, nous pouvons changer les données de l'employé. Remarquez que nous avons passé l'ID de l'employé dans le paramètre d'URL.

![Image](https://cdn-media-1.freecodecamp.org/images/a83joAzqvLOvLkrBphgo1X1iNMCJZX4h3hW1)

Ici, nous avons changé la ville de l'employé Swati de Mumbai à Kolkata. Cliquez sur "Enregistrer" pour actualiser le tableau des données des employés afin de voir les modifications mises à jour comme souligné dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/YTVLVrodvmccRgROnCHeUoYjJDc4gCYo9ma0)

Maintenant, nous allons effectuer une opération de suppression sur l'employé nommé Dhiraj. Cliquez sur le lien d'action "Supprimer", qui ouvrira la vue de suppression demandant une confirmation pour supprimer. Remarquez que nous avons passé l'ID de l'employé dans le paramètre d'URL.

![Image](https://cdn-media-1.freecodecamp.org/images/vh9OcLX0TZBjpK4FZZRgNdULvxM45sPSZfBq)

Une fois que nous cliquons sur le bouton "Supprimer", il supprimera l'enregistrement de l'employé et le tableau des données des employés sera actualisé. Ici, nous pouvons voir que l'employé nommé Dhiraj a été supprimé de notre enregistrement.

![Image](https://cdn-media-1.freecodecamp.org/images/6GYVO2fxT7YUq9pkt5taPVC9dCtTQOlnPnMj)

### Déploiement de l'application

Pour apprendre comment déployer une application Blazor en utilisant IIS, référez-vous à [Déployer une application Blazor sur IIS](http://ankitsharmablogs.com/deploying-a-blazor-application-on-iis/).

### Conclusion

Nous avons créé une application monopage avec Razor Pages dans Blazor en utilisant l'approche Entity Framework Core "database first" avec l'aide de Visual Studio 2017 et SQL Server 2014. Nous avons également effectué des opérations CRUD sur notre application.

Veuillez obtenir le code source depuis [GitHub](https://github.com/AnkitSharma-007/SPA-With-Blazor) et jouez avec pour obtenir une meilleure compréhension.

Obtenez mon livre [Blazor Quick Start Guide](https://www.amazon.com/Blazor-Quick-Start-Guide-applications/dp/178934414X/ref=sr_1_1?ie=UTF8&qid=1542438251&sr=8-1&keywords=Blazor-Quick-Start-Guide) pour en apprendre davantage sur Blazor.

Vous pouvez également lire cet article sur [C# Corner](https://www.c-sharpcorner.com/article/creating-a-spa-using-razor-pages-with-blazor/)

Vous pouvez vérifier mes autres articles sur Blazor [ici](http://ankitsharmablogs.com/category/blazor/).

### Voir aussi

* [ASP.NET Core — Getting Started With Blazor](http://ankitsharmablogs.com/asp-net-core-getting-started-with-blazor/)
* [ASP.NET Core — CRUD Using Blazor And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-blazor-and-entity-framework-core/)
* [Cascading DropDownList In Blazor Using EF Core](http://ankitsharmablogs.com/cascading-dropdownlist-in-blazor-using-ef-core/)
* [Razor Page Web Application With ASP.NET Core Using ADO.NET](https://www.c-sharpcorner.com/article/razor-page-web-application-with-asp-net-core-using-ado-net/)
* [ASP.NET Core — CRUD Using Angular 5 And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-angular-5-and-entity-framework-core/)
* [ASP.NET Core — CRUD With React.js And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-with-react-js-and-entity-framework-core/)

Publié à l'origine sur [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)