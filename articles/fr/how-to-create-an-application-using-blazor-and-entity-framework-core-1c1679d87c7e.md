---
title: Comment créer une application utilisant Blazor et Entity Framework Core
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-29T23:13:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-application-using-blazor-and-entity-framework-core-1c1679d87c7e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QCtmxYqqBQJ_7fWmH61Tww.jpeg
tags:
- name: data
  slug: data
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: visual studio
  slug: visual-studio
- name: Web Development
  slug: web-development
seo_title: Comment créer une application utilisant Blazor et Entity Framework Core
seo_desc: 'By Ankit Sharma

  Microsoft has recently announced the release of a new .NET web framework called
  Blazor. In this article, we are going to create a web application using Blazor with
  the help of Entity Framework Core. We will be creating a sample Employ...'
---

Par Ankit Sharma

Microsoft a récemment annoncé la sortie d'un nouveau framework web .NET appelé Blazor. Dans cet article, nous allons créer une application web utilisant Blazor avec l'aide d'Entity Framework Core. Nous allons créer un système de gestion des dossiers des employés et effectuer des opérations CRUD dessus.

### Prérequis

* Installer .NET Core 2.1 Preview 2 SDK depuis [ici](https://www.microsoft.com/net/download/dotnet-core/sdk-2.1.300-preview2)
* Installer une version préliminaire de Visual Studio 2017 v15.7 depuis [ici](https://www.visualstudio.com/vs/preview/)
* Installer l'extension ASP.NET Core Blazor Language Services depuis [ici](https://marketplace.visualstudio.com/items?itemName=aspnet.blazor)
* SQL Server 2012 ou supérieur

Le framework Blazor n'est pas pris en charge par les versions antérieures à Visual Studio 2017 v15.7.

Avant de continuer, je vous suggère de lire mon article précédent sur [comment commencer avec Blazor](http://ankitsharmablogs.com/asp-net-core-getting-started-with-blazor/).

### Code source

Je vous recommande également de récupérer le code source depuis [Github](https://github.com/AnkitSharma-007/ASPCore.BlazorCrud) avant de commencer.

### Création de la table

Nous allons utiliser une table de base de données pour stocker tous les dossiers des employés.

Ouvrez SQL Server et utilisez le script suivant pour créer la table **tblEmployee** :

```
Create table tblEmployee(
    EmployeeId int IDENTITY(1,1) NOT NULL,
    Name varchar(20) NOT NULL,
    City varchar(20) NOT NULL,
    Department varchar(20) NOT NULL,
    Gender varchar(6) NOT NULL
)
```

Maintenant, passons à la création de notre application web.

### Créer l'application web Blazor

Ouvrez Visual Studio et sélectionnez Fichier >> Nouveau >> Projet.

Après avoir sélectionné le projet, une boîte de dialogue "Nouveau Projet" s'ouvrira. Sélectionnez .NET Core dans le menu Visual C# du panneau de gauche.

Ensuite, sélectionnez "Application Web ASP.NET Core" parmi les types de projets disponibles. Donnez le nom du projet **BlazorCrud** et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/zGPbNji-3eCLIIOUvtSMtoRsF5zr0zUoajr0)

Après avoir cliqué sur OK, une nouvelle boîte de dialogue s'ouvrira vous demandant de sélectionner le modèle de projet. Vous verrez deux menus déroulants en haut à gauche de la fenêtre de modèle. Sélectionnez ".NET Core" et "ASP.NET Core 2.0" dans ces menus déroulants. Ensuite, sélectionnez le modèle "Blazor (ASP .NET Core hébergé)" et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/YfbWL3ZmlR36U-JVcwWOJuFkW89Lw7Fy09W0)

Maintenant, notre solution Blazor sera créée. Vous pouvez observer la structure des dossiers dans l'Explorateur de solutions comme montré dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/vUXe0DvTLL5sdKJTteAZqSWCKnXE67Kp3-q7)

Vous verrez que nous avons 3 fichiers de projet créés dans cette solution :

1. BlazorCrud.Client — Il contient le code côté client et les pages qui seront rendues dans le navigateur.
2. BlazorCrud.Server — Il contient le code côté serveur, tel que les opérations liées à la base de données et l'API web.
3. BlazorCrud.Shared — Il contient le code partagé qui peut être accessible à la fois par le client et le serveur.

Exécutez le programme. Il ouvrira le navigateur et vous verrez une page similaire à celle montrée ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/3TiqY1os8SRNJEzJGkejhKBKVYjDDuN2GIzb)

Ici, vous pouvez voir un menu de navigation sur le côté gauche, qui contient la navigation vers les pages de notre application. Par défaut, nous avons les pages "Counter" et "Fetch Data" fournies dans notre application. Ces pages par défaut n'affecteront pas notre application, mais pour ce tutoriel, nous allons supprimer les pages **fetchdata** et **counter** du dossier **BlazorCrud.Client/Pages**.

### Ajout du modèle à l'application

Faites un clic droit sur le projet BlazorCrud.Shared, puis sélectionnez Ajouter >> Nouveau Dossier et nommez le dossier **Models**. Nous allons ajouter notre classe de modèle dans ce dossier.

Faites un clic droit sur le dossier Models et sélectionnez Ajouter >> Classe. Nommez votre classe **Employee.cs**. Cette classe contiendra les propriétés de notre modèle Employee. Maintenant, notre projet BlazorCrud.Shared a la structure suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/82zqiyP54mNDcU7wAnUoodOR35OfmJvdoJGx)

Ouvrez **Employee.cs** et mettez le code suivant dedans :

```
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Text;

namespace BlazorCrud.Shared.Models
{
    public class Employee
    {
        public int EmployeeId { get; set; }
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

Et ainsi, notre modèle a été créé. Maintenant, nous allons créer notre couche d'accès aux données.

### Création de la couche d'accès aux données pour l'application

Faites un clic droit sur le projet BlazorCrud.Server, puis sélectionnez Ajouter >> Nouveau Dossier et nommez le dossier **DataAccess**. Nous allons ajouter nos classes pour gérer les opérations liées à la base de données dans ce dossier.

Faites un clic droit sur le dossier **DataAccess** et sélectionnez Ajouter >> Classe. Nommez votre classe **EmployeeContext.cs**. Il s'agit de notre classe de contexte de base de données Entity Framework qui nous permet d'interagir avec la base de données. Ouvrez **EmployeeContext.cs** et mettez le code suivant dedans :

```
using BlazorCrud.Shared.Models;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorCrud.Server.DataAccess
{
    public class EmployeeContext : DbContext
    {
        public virtual DbSet<Employee> tblEmployee { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
                optionsBuilder.UseSqlServer(@"Put Your Connection string here");
            }
        }
    }
}
```

N'oubliez pas de mettre votre propre chaîne de connexion.

Ajoutez une autre classe au dossier **DataAccess** et nommez-la **EmployeeDataAccessLayer.cs**. Cette classe gérera nos opérations CRUD liées à la base de données. Ouvrez **EmployeeDataAccessLayer.cs** et mettez le code suivant dedans :

```
using BlazorCrud.Shared.Models;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace BlazorCrud.Server.DataAccess
{
    public class EmployeeDataAccessLayer
    {
        EmployeeContext db = new EmployeeContext();

        //Pour obtenir tous les détails des employés
        public IEnumerable<Employee> GetAllEmployees()
        {
            try
            {
                return db.tblEmployee.ToList();
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
                db.tblEmployee.Add(employee);
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
                Employee employee = db.tblEmployee.Find(id);
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
                Employee emp = db.tblEmployee.Find(id);
                db.tblEmployee.Remove(emp);
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

Maintenant, notre couche d'accès aux données est complète. Ensuite, nous allons procéder à la création de notre contrôleur d'API web.

### Ajout du contrôleur d'API web à l'application

Faites un clic droit sur le dossier **BlazorCrud.Server/Controllers** et sélectionnez Ajouter >> Nouvel Élément. Une boîte de dialogue "Ajouter un nouvel élément" s'ouvrira. Sélectionnez ASP.NET dans le panneau de gauche, puis sélectionnez "Classe de contrôleur d'API" dans le panneau des modèles et nommez-la **EmployeeController.cs**. Appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/RKROzzhcRCSFVHrkYQcltQmFt7xPha6jCZPM)

Cela créera notre classe d'API **EmployeeController**.

Nous allons appeler les méthodes de la classe **EmployeeDataAccessLayer** pour récupérer les données et les transmettre au côté client.

Ouvrez le fichier **EmployeeController.cs** et mettez le code suivant dedans :

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using BlazorCrud.Server.DataAccess;
using BlazorCrud.Shared.Models;
using Microsoft.AspNetCore.Mvc;

namespace BlazorCrud.Server.Controllers
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

À ce stade, notre projet **BlazorCrud.Server** a la structure suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/JtmrDM7QtuDas0bq-OqihzMpn2T0PaakQjLg)

Nous avons terminé avec notre logique backend. Nous allons maintenant procéder au codage de notre côté client.

### Ajout de la vue Razor à l'application

Faites un clic droit sur le dossier **BlazorCrud.Client/Pages** puis sélectionnez Ajouter >> Nouvel Élément. Une boîte de dialogue "Ajouter un nouvel élément" s'ouvrira, sélectionnez Web dans le panneau de gauche, puis sélectionnez "Vue Razor" dans le panneau des modèles et nommez-la **FetchEmployee.cshtml**.

![Image](https://cdn-media-1.freecodecamp.org/images/HqQn5jyacZB00aY6c9-e-GK7V7GZpqn77KUg)

Cela ajoutera une page **FetchEmployee.cshtml** à notre dossier **BlazorCrud.Client/Pages**. De même, ajoutez 3 pages supplémentaires : **AddEmployee.cshtml**, **EditEmployee.cshtml**, et **DeleteEmployee.cshtml**.

Maintenant, notre projet **BlazorCrud.Client** a la structure suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/DlAVomYnrhDMD1JCP8qExF5wGNTTOUMDlr9z)

Ajoutons du code à ces pages.

### FetchEmployee.cshtml

Cette page affichera tous les enregistrements d'employés présents dans la base de données. De plus, nous fournirons également les méthodes d'action **Edit** et **Delete** sur chaque enregistrement.

Ouvrez **FetchEmployee.cshtml** et mettez le code suivant dedans :

```
@using BlazorCrud.Shared.Models
@page "/fetchemployee"
@inject HttpClient Http

<h1>Données des employés</h1>
<p>Ce composant démontre la récupération des données des employés depuis le serveur.</p>
<p>
    <a href="/addemployee">Créer un nouveau</a>
</p>

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
                        <a href='/editemployee/@emp.EmployeeId'>Modifier</a> |
                        <a href='/delete/@emp.EmployeeId'>Supprimer</a>
                    </td>
                </tr>
            }
        </tbody>
    </table>
}

@functions {
    Employee[] empList;

    protected override async Task OnInitAsync()
    {
        empList = await Http.GetJsonAsync<Employee[]>("/api/Employee/Index");
    }
}
```

Comprenons ce code. En haut, nous avons inclus l'espace de noms **BlazorEFApp.Shared.Models** afin que nous puissions utiliser notre classe de modèle Employee dans cette page.

Nous définissons la route de cette page en utilisant la directive @page. Donc, dans cette application, si nous ajoutons "fetchemployee" à l'URL de base, nous serons redirigés vers cette page. Nous injectons également le service HttpClient pour activer l'appel à l'API web.

Ensuite, nous avons défini la partie HTML pour afficher tous les enregistrements des employés de manière tabulaire. Nous avons également ajouté deux liens d'action pour **Modifier** et **Supprimer** qui navigueront respectivement vers les pages **EditEmployee.cshtml** et **DeleteEmployee.cshtml**.

En bas de la page, nous avons une section @functions qui contient notre logique métier. Nous avons créé une variable de tableau **empList** de type Employee, et nous la remplissons dans la méthode **OnInitAsync** en appelant notre API web. Cela se liera à notre tableau HTML lors du chargement de la page.

### AddEmployee.cshtml

Cette page est utilisée pour créer un nouvel enregistrement d'employé.

Ouvrez **AddEmployee.cshtml** et mettez le code suivant dedans :

```
@using BlazorCrud.Shared.Models
@page "/addemployee"
@inject HttpClient Http
@inject Microsoft.AspNetCore.Blazor.Services.IUriHelper UriHelper

<h1>Créer</h1>
<h3>Employé</h3>
<hr />
<div class="row">
    <div class="col-md-4">
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
                <input asp-for="City" class="form-control" bind="@emp.City" />
            </div>
            <div class="form-group">
                <button type="submit" class="btn btn-default" onclick="@(async () => await CreateEmployee())">Enregistrer</button>
                <button class="btn" onclick="@cancel">Annuler</button>
            </div>
        </form>
    </div>
</div>

@functions {
    Employee emp = new Employee();

    protected async Task CreateEmployee()
    {
        await Http.SendJsonAsync(HttpMethod.Post, "/api/Employee/Create", emp);
        UriHelper.NavigateTo("/fetchemployee");
    }

    void cancel()
    {
        UriHelper.NavigateTo("/fetchemployee");
    }
}
```

Dans cette page, la route est "/addemployee".

Nous injectons également le service "Microsoft.AspNetCore.Blazor.Services.IUriHelper" pour activer la redirection d'URL. La partie HTML générera un formulaire pour obtenir les entrées de l'utilisateur. L'attribut "bind" est utilisé pour lier la valeur entrée dans la zone de texte aux propriétés de l'objet Employee.

Dans la section @functions, nous avons défini deux méthodes. La méthode **CreateEmployee** sera appelée en cliquant sur le bouton "Submit" et enverra une requête POST à notre API avec l'objet Employee emp.

La méthode **Cancel** sera appelée en cliquant sur le bouton d'annulation et redirigera l'utilisateur vers la page **FetchEmployee**.

### EditEmployee.cshtml

Cette page est utilisée pour modifier les détails d'un employé.

Ouvrez **EditEmployee.cshtml** et mettez le code suivant dedans :

```
@using BlazorCrud.Shared.Models
@page "/editemployee/{empID}"
@inject HttpClient Http
@inject Microsoft.AspNetCore.Blazor.Services.IUriHelper UriHelper

<h2>Modifier</h2>
<h4>Employés</h4>
<hr />
<div class="row">
    <div class="col-md-4">
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
            <div class=" form-group">
                <label asp-for="City" class="control-label">Ville</label>
                <input asp-for="City" class="form-control" bind="@emp.City" />
            </div>
            <div class="form-group">
                <input type="submit" value="Enregistrer" onclick="@(async () => await UpdateEmployee())" class="btn btn-default" />
                <input type="submit" value="Annuler" onclick="@cancel" class="btn" />
            </div>
        </form>
    </div>
</div>

@functions {
    [Parameter]
    string empID { get; set; }

    Employee emp = new Employee();

    protected override async Task OnInitAsync()
    {
        emp = await Http.GetJsonAsync<Employee>("/api/Employee/Details/" + Convert.ToInt32(empID));
    }

    protected async Task UpdateEmployee()
    {
        await Http.SendJsonAsync(HttpMethod.Put, "api/Employee/Edit", emp);
        UriHelper.NavigateTo("/fetchemployee");
    }

    void cancel()
    {
        UriHelper.NavigateTo("/fetchemployee");
    }
}
```

Dans cette page, nous avons défini la route comme "/editemployee/{empID}". **empID** est un paramètre d'URL de type string déclaré dans la section @functions. Nous allons utiliser l'attribut [Parameter] pour marquer la variable comme un paramètre. Pour naviguer vers cette page, nous devons passer l'ID de l'employé dans l'URL qui sera capturé dans la variable **empID**.

Si nous ne marquons pas la variable avec l'attribut [Parameter], nous obtiendrons l'erreur suivante : "L'objet de type 'BlazorCrud.Client.Pages.EditEmployee' a une propriété correspondant au nom 'empID', mais il n'a pas [ParameterAttribute] appliqué." Cela ne permettra pas à **empID** de se lier à la valeur de l'ID de l'employé passé en paramètre.

La partie HTML est similaire à celle de la page **AddEmployee.cshtml**. L'attribut "bind" est utilisé pour une liaison bidirectionnelle, c'est-à-dire lier les valeurs des zones de texte aux propriétés de l'objet employé, et vice versa.

Dans la section @functions, nous récupérons les enregistrements des employés dans la méthode **OnInitAsync** en fonction de l'employeeID passé en paramètre. Cela se liera aux champs du formulaire lors du chargement de la page.

La méthode **UpdateEmployee** enverra une requête PUT à notre API avec l'objet Employee emp. La méthode **Cancel** sera appelée en cliquant sur le bouton d'annulation et redirigera l'utilisateur vers la page **FetchEmployee**.

### DeleteEmployee.cshtml

Cette page sera utilisée pour supprimer un enregistrement d'employé.

Ouvrez **DeleteEmployee.cshtml** et mettez le code suivant dedans :

```
@using BlazorCrud.Shared.Models
@page "/delete/{empID}"
@inject HttpClient Http
@inject Microsoft.AspNetCore.Blazor.Services.IUriHelper UriHelper

<h2>Supprimer</h2>
<h3>Êtes-vous sûr de vouloir supprimer l'employé avec l'ID : @empID</h3>
<br />
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
        <input type="submit" value="Supprimer" onclick="@(async () => await Delete())" class="btn btn-default" />
        <input type="submit" value="Annuler" onclick="@cancel" class="btn" />
    </div>
</div>

@functions {
    [Parameter]
    string empID { get; set; }

    Employee emp = new Employee();

    protected override async Task OnInitAsync()
    {
        emp = await Http.GetJsonAsync<Employee>("/api/Employee/Details/" + Convert.ToInt32(empID));
    }

    protected async Task Delete()
    {
        await Http.DeleteAsync("api/Employee/Delete/" + Convert.ToInt32(empID));
        UriHelper.NavigateTo("/fetchemployee");
    }

    void cancel()
    {
        UriHelper.NavigateTo("/fetchemployee");
    }
}
```

La route de cette page est également paramétrée, car nous récupérons l'enregistrement de l'employé lors du chargement de la page.

La partie HTML affichera les données de l'employé et demandera à l'utilisateur de confirmer la suppression de l'enregistrement de l'employé.

Dans la section @functions, nous récupérons les enregistrements des employés dans la méthode **OnInitAsync** en fonction de l'employeeID passé en paramètre. Cela affichera les enregistrements des employés lors du chargement de la page.

La méthode **Delete** sera appelée en cliquant sur le bouton "Supprimer", qui enverra une requête de suppression à notre API avec l'ID de l'employé à supprimer. Après une suppression réussie, l'utilisateur sera redirigé vers la page **FetchEmployee**.

### Ajout d'un lien au menu de navigation

La dernière étape consiste à définir le menu de navigation pour notre application. Ouvrez le fichier **BlazorCrud.Client/Shared/NavMenu.cshtml** et mettez le code suivant dedans :

```
<div class="top-row pl-4 navbar navbar-dark">
    <a class="navbar-brand" href="/">BlazorCrud</a>
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
            <NavLink class="nav-link" href="/fetchemployee">
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

Et c'est tout. Nous avons créé notre première application **ASP.NET** Core en utilisant Blazor et Entity Framework Core.

### Démonstration d'exécution

Lancez l'application.

Une page web s'ouvrira comme montré dans l'image ci-dessous. Le menu de navigation à gauche affichera le lien de navigation pour les pages d'accueil et de récupération des employés.

![Image](https://cdn-media-1.freecodecamp.org/images/cV9HHW5sPNGBrNhpjj2G44EmN1wM5yJl6hrd)

Cliquez sur **Récupérer les employés** dans le menu de navigation. Il vous redirigera vers la vue **FetchEmployee** et affichera toutes les données des employés sur la page. Remarquez que l'URL a "fetchemployee" ajouté à celle-ci, comme nous l'avons défini en utilisant la directive @page.

![Image](https://cdn-media-1.freecodecamp.org/images/CmRK4F3HHkoZ5sSc3Z24Ql6YqXiyUTAEyRFV)

Puisque nous n'avons ajouté aucune donnée, elle est vide.

Cliquez sur **Créer un nouveau** pour naviguer vers la vue **AddEmployee**. Remarquez que l'URL a "addemployee" ajouté à celle-ci, comme nous l'avons défini en utilisant la directive @page. Ajoutez un nouvel enregistrement d'employé comme montré dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/nuRceVySlBWelVt1sdrknlR219XBQFrEKkyR)

Après avoir inséré des données dans tous les champs, cliquez sur le bouton "Enregistrer". Le nouvel enregistrement d'employé sera créé, et vous serez redirigé vers la vue **FetchEmployee**, qui affichera les enregistrements de tous les employés. Ici, nous pouvons également voir les méthodes d'action **Modifier** et **Supprimer** correspondant à chaque enregistrement.

![Image](https://cdn-media-1.freecodecamp.org/images/GC6B6tuFby6eiofdFQjlNHxyjTeD48NvrDtq)

Si nous voulons modifier un enregistrement d'employé existant, il suffit de cliquer sur le lien d'action **Modifier**. Il ouvrira la vue **Modifier** comme montré ci-dessous. Ici, nous pouvons changer les données de l'employé. Remarquez que nous avons passé l'ID de l'employé dans le paramètre d'URL.

![Image](https://cdn-media-1.freecodecamp.org/images/RSC3aHrWDT7cg2WdlXpOT9Bh6s0YqbriinOL)

Ici, nous avons changé la ville de l'employé Swati de New Delhi à Chennai. Cliquez sur "Enregistrer" pour revenir à la vue FetchEmployee et voir les modifications mises à jour comme indiqué dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/5Q4wzYh7cML-EqFzrTcKOxQY24f5G73yfdhk)

Maintenant, nous allons effectuer l'opération de suppression sur l'employé nommé Rahul. Cliquez sur le lien d'action **Supprimer** qui ouvrira la vue **Supprimer** demandant une confirmation de suppression. Remarquez que nous avons passé l'ID de l'employé dans le paramètre d'URL.

![Image](https://cdn-media-1.freecodecamp.org/images/GKJoohKLsrb7CNgy6I2t-kDh7K6qnM3VMDfO)

Une fois que nous cliquons sur le bouton Supprimer, il supprimera l'enregistrement de l'employé et nous serons redirigés vers la vue **FetchEmployee**. Ici, nous pouvons voir que l'employé nommé Rahul a été supprimé de notre enregistrement.

![Image](https://cdn-media-1.freecodecamp.org/images/XLbblGjSRJsEqyUoo4-ZfFnAPIMhwNUQWHc1)

### Hébergement de l'application

Pour apprendre comment héberger une application Blazor en utilisant IIS, référez-vous à [Déployer une application Blazor sur IIS](http://ankitsharmablogs.com/deploying-a-blazor-application-on-iis/).

### Voir aussi

* [ASP.NET Core — CRUD utilisant Angular 5 et Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-angular-5-and-entity-framework-core/)
* [Opérations CRUD avec ASP.NET Core utilisant Angular 5 et ADO.NET](http://ankitsharmablogs.com/crud-operations-asp-net-core-using-angular-5-ado-net/)
* [Commencer avec Angular 5 en utilisant Visual Studio Code](http://ankitsharmablogs.com/getting-started-with-angular-5-using-visual-studio-code/)
* [Opération CRUD avec ASP.NET Core MVC en utilisant Visual Studio Code et EF](http://ankitsharmablogs.com/crud-operation-asp-net-core-mvc-using-visual-studio-code-ef/)
* [Opération CRUD avec ASP.NET Core MVC en utilisant ADO.NET et Visual Studio 2017](http://ankitsharmablogs.com/crud-operation-with-asp-net-core-mvc-using-ado-net/)
* [Opération CRUD avec ASP.NET Core MVC en utilisant Visual Studio Code et ADO.NET](http://ankitsharmablogs.com/crud-operation-with-asp-net-core-mvc-using-visual-studio-code-and-ado-net/)

### Conclusion

Nous avons créé une application ASP.NET Core en utilisant le nouveau framework web Blazor et Entity Framework Core avec l'aide de Visual Studio 2017 et SQL Server 2012. Nous avons également effectué des opérations CRUD sur notre application.

Vous pouvez également forker cette application sur [Github](https://github.com/AnkitSharma-007/ASPCore.BlazorCrud). Essayez ce nouveau framework et faites-moi savoir ce que vous en pensez dans la section des commentaires ci-dessous.

Obtenez mon livre [Blazor Quick Start Guide](https://www.amazon.com/Blazor-Quick-Start-Guide-applications/dp/178934414X/ref=sr_1_1?ie=UTF8&qid=1542438251&sr=8-1&keywords=Blazor-Quick-Start-Guide) pour en savoir plus sur Blazor.

Vous pouvez également trouver cet article sur [C# Corner](https://www.c-sharpcorner.com/article/asp-net-core-crud-using-blazor-and-entity-framework-core/).

Vous pouvez vérifier mes autres articles sur ASP .NET Core [ici](http://ankitsharmablogs.com/category/asp-net-core/)

Publié à l'origine sur [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)