---
title: Comment créer une liste déroulante en cascade dans Blazor en utilisant EF Core
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-11T22:21:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-cascading-dropdownlist-in-blazor-using-ef-core-d230bb5bff5f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-F0evvZudQwAMDUb9ygC8Q.jpeg
tags:
- name: data
  slug: data
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: visual studio
  slug: visual-studio
seo_title: Comment créer une liste déroulante en cascade dans Blazor en utilisant
  EF Core
seo_desc: 'By Ankit Sharma

  Introduction

  In this article, we are going to create a cascading dropdown list in Blazor using
  Entity Framework Core database first approach. We will create two dropdown lists
  — Country and City. Upon selecting the value from the coun...'
---

Par Ankit Sharma

### Introduction

Dans cet article, nous allons créer une liste déroulante en cascade dans Blazor en utilisant l'approche database first d'Entity Framework Core. Nous allons créer deux listes déroulantes — **Pays** et **Ville**. Lors de la sélection de la valeur dans la liste déroulante des pays, nous allons changer la valeur de la liste déroulante des villes.

Nous allons utiliser Visual Studio 2017 et SQL Server 2014.

Jetons un coup d'œil au produit final.

![Image](https://cdn-media-1.freecodecamp.org/images/R6rX0AxiRQV668mITyMfa7Zl6bUW8SE53IJj)

### Prérequis

* Installer le SDK .NET Core 2.1 Preview 2 depuis [ici](https://www.microsoft.com/net/download/dotnet-core/sdk-2.1.300-preview2)
* Installer Visual Studio 2017 v15.7 ou supérieur depuis [ici](https://www.visualstudio.com/downloads/)
* Installer l'extension ASP.NET Core Blazor Language Services depuis [ici](https://marketplace.visualstudio.com/items?itemName=aspnet.blazor)
* SQL Server 2008 ou supérieur

Le framework Blazor n'est pas supporté par les versions inférieures à Visual Studio 2017 v15.7.

### Code Source

Avant de continuer, je vous recommande de récupérer le code source depuis [GitHub](https://github.com/AnkitSharma-007/Blazor-CascadingDDL-EFCore).

### Création des Tables

Nous allons utiliser deux tables pour stocker nos données.

1. Country : utilisée pour stocker le nom du pays. Elle contient deux champs — CountryId et CountryName.
2. Cities : celle-ci contient la liste des villes pour les pays que nous allons insérer dans la table Country. Elle contient trois champs — CityId, CountryId et CityName. La colonne CountryId est une clé étrangère faisant référence à CountryId dans la table Country.

Exécutez les commandes suivantes pour créer les deux tables :

```
CREATE TABLE Country(CountryId VARCHAR(5) PRIMARY KEY,CountryName VARCHAR(20) NOT NULL)GOCREATE TABLE Cities(CityId VARCHAR(5) PRIMARY KEY,CountryId VARCHAR(5) FOREIGN KEY REFERENCES Country(CountryId),CityName VARCHAR(20) NOT NULL)GO
```

Maintenant, nous allons mettre quelques données dans les deux tables. Ouvrez la table Country et exécutez l'instruction d'insertion suivante.

```
INSERT INTO Country VALUES ('C1', 'India')INSERT INTO Country VALUES ('C2', 'China')INSERT INTO Country VALUES ('C3', 'USA')
```

Ensuite, exécutez les instructions d'insertion suivantes pour insérer des données dans la table Cities.

```
INSERT INTO Cities VALUES ('P1','C1','New Delhi')INSERT INTO Cities VALUES ('P2','C1','Mumbai')INSERT INTO Cities VALUES ('P3','C1','Chennai')INSERT INTO Cities VALUES ('P4','C1','Hyderabad')INSERT INTO Cities VALUES ('P5','C1','Bengaluru')INSERT INTO Cities VALUES ('P6','C2','Beijing')INSERT INTO Cities VALUES ('P7','C2','Shanghai')INSERT INTO Cities VALUES ('P8','C2','Hong Kong')INSERT INTO Cities VALUES ('P9','C2','Macau')INSERT INTO Cities VALUES ('P10','C3','New York')INSERT INTO Cities VALUES ('P11','C3','Chicago')INSERT INTO Cities VALUES ('P12','C3','Las Vegas')
```

### Créer une Application Web Blazor

Ouvrez Visual Studio et sélectionnez Fichier >> Nouveau >> Projet.

Après avoir sélectionné le projet, une boîte de dialogue « Nouveau Projet » s'ouvrira. Sélectionnez .NET Core dans le menu Visual C# du panneau de gauche. Ensuite, sélectionnez « Application Web ASP.NET Core » parmi les types de projets disponibles. Nommez le projet « BlazorDDL » et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/aA8aVK7FJ9e7thD2fBpNscpiI0ttTX-tLCdU)

Après avoir cliqué sur OK, une nouvelle boîte de dialogue s'ouvrira vous demandant de sélectionner le modèle de projet. Vous pouvez voir deux menus déroulants en haut à gauche de la fenêtre de modèle. Sélectionnez « .NET Core » et « ASP.NET Core 2.0 » dans ces menus déroulants. Ensuite, sélectionnez le modèle « Blazor (ASP .NET Core hébergé) » et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/DK6ivh2qgXWJpzHbnuPegwrxXeOAVEQjGpRn)

Maintenant, notre solution Blazor sera créée. Vous pouvez voir la structure des dossiers dans l'Explorateur de solutions comme montré dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/lfVaeOOv4QxaWlf9lU8BzEOvajxIIZb-RoT0)

Vous pouvez voir que nous avons trois fichiers de projet créés dans cette solution.

1. BlazorDDL.Client : il contient le code côté client et les pages qui seront rendues sur le navigateur.
2. BlazorDDL.Server : il contient le code côté serveur, tel que les opérations liées à la base de données et l'API web.
3. BlazorDDL.Shared : il contient le code partagé qui peut être accessible à la fois par le client et le serveur.

### Scaffolding du Modèle vers l'Application

Nous utilisons l'approche database first d'Entity Framework Core pour créer nos modèles. Nous allons créer notre classe de modèle dans le projet « BlazorDDL.Shared » afin qu'elle soit accessible à la fois par le projet client et serveur.

Accédez à Outils >> Gestionnaire de packages NuGet >> Console du gestionnaire de packages. Sélectionnez « BlazorDDL.Shared » dans le menu déroulant Projet par défaut. Reportez-vous à l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/5pv33HzsBpS5pQ8O8CmSw-O2jsyhBaN8LO4W)

Tout d'abord, nous allons installer le package pour le fournisseur de base de données que nous ciblons, qui est SQL Server dans ce cas. Exécutez la commande suivante :

```
Install-Package Microsoft.EntityFrameworkCore.SqlServer
```

Puisque nous utilisons les outils Entity Framework pour créer un modèle à partir de la base de données existante, nous allons également installer le package d'outils. Exécutez la commande suivante :

```
Install-Package Microsoft.EntityFrameworkCore.Tools
```

Après avoir installé les deux packages, nous allons créer notre modèle à partir des tables de la base de données en utilisant la commande suivante :

```
Scaffold-DbContext "Votre chaîne de connexion ici" Microsoft.EntityFrameworkCore.SqlServer -OutputDir Models -Tables Country, Cities
```

N'oubliez pas de mettre votre propre chaîne de connexion (à l'intérieur de " "). Après que cette commande soit exécutée avec succès, vous pouvez voir qu'un dossier Models a été créé et contient trois fichiers de classe : « myTestDBContext.cs », « Cities.cs » et « Country.cs ». Et ainsi nous avons réussi à créer nos modèles en utilisant l'approche database first d'EF Core.

À ce stade, le dossier Models aura la structure suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/ZyxM9Q56JAl9a7NLVwOwAhoJBFz1f7aQxd6L)

### Création de la Couche d'Accès aux Données pour l'Application

Faites un clic droit sur le projet « BlazorDDL.Server » puis sélectionnez Ajouter >> Nouveau Dossier et nommez le dossier « DataAccess ». Nous allons ajouter notre classe pour gérer les opérations liées à la base de données dans ce dossier uniquement.

Faites un clic droit sur le dossier « DataAccess » et sélectionnez Ajouter >> Classe. Nommez votre classe « DataAccessLayer.cs ». Cette classe gérera nos opérations liées à la base de données.

Ouvrez « DataAccessLayer.cs » et mettez le code suivant dedans.

```
using BlazorDDL.Shared.Models;using System;using System.Collections.Generic;using System.Linq;using System.Threading.Tasks;namespace BlazorDDL.Server.DataAccess{    public class DataAccessLayer    {        myTestDBContext db = new myTestDBContext();        public IEnumerable<Country> GetAllCountries()        {            try            {                return db.Country.ToList();            }            catch            {                throw;            }        }        public IEnumerable<Cities> GetCityData(string id)        {            try            {                List<Cities> lstCity = new List<Cities>();                lstCity = (from CityName in db.Cities where CityName.CountryId == id select CityName).ToList();                return lstCity;            }            catch            {                throw;            }        }    }}
```

Ici, nous avons défini deux méthodes :

1. GetAllCountries : elle récupérera toutes les données des pays depuis la table des pays.
2. GetCityData : elle récupérera les données des villes correspondant à l'identifiant du pays fourni.

Maintenant, notre couche d'accès aux données est complète. Nous allons procéder à la création de notre contrôleur d'API web.

### Ajout du Contrôleur d'API Web à l'Application

Faites un clic droit sur le dossier « BlazorDDL.Server/Controllers » et sélectionnez Ajouter >> Nouvel Élément. Une boîte de dialogue « Ajouter un nouvel élément » s'ouvrira. Sélectionnez « ASP.NET » dans le panneau de gauche, puis sélectionnez « Classe de Contrôleur d'API » dans le panneau des modèles et nommez-la « CountriesController.cs ». Appuyez sur Ajouter.

![Image](https://cdn-media-1.freecodecamp.org/images/0U0myNn7E3ix92ez7eJ23-1mFPV9WQd3Y5E9)

Cela créera notre classe d'API « CountriesController ».

Nous allons appeler les méthodes de la classe « DataAccessLayer » pour récupérer les données et transmettre les données au côté client.

Ouvrez le fichier « CountriesController.cs » et mettez le code suivant dedans.

```
using System;using System.Collections.Generic;using System.Linq;using System.Threading.Tasks;using BlazorDDL.Server.DataAccess;using BlazorDDL.Shared.Models;using Microsoft.AspNetCore.Mvc;using Microsoft.AspNetCore.Http;namespace BlazorDDL.Server.Controllers{    public class CountriesController : Controller    {        DataAccessLayer objCountry= new DataAccessLayer();        [HttpGet]        [Route("api/Countries/GetCountryList")]        public IEnumerable<Country> GetCountryList()        {            return objCountry.GetAllCountries();        }        [HttpGet]        [Route("api/Countries/GetCities/{id}")]        public IEnumerable<Cities> GetCities(string id)        {            return objCountry.GetCityData(id);        }    }}
```

À ce stade, notre projet BlazorDDL.Server a la structure suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/CZyT1rhgPUQJDkNFnFSOru1uZhBIKGY8Gq9O)

Nous avons terminé avec notre logique backend. Par conséquent, nous allons maintenant procéder au codage de notre côté client.

### Ajout de la Vue Razor à l'Application

Faites un clic droit sur le dossier « BlazorDDL.Client/Pages » puis sélectionnez Ajouter >> Nouvel Élément. Une boîte de dialogue « Ajouter un nouvel élément » s'ouvrira. Sélectionnez Web dans le panneau de gauche, puis sélectionnez « Vue Razor » dans le panneau des modèles et nommez-la « CountryData.cshtml ».

![Image](https://cdn-media-1.freecodecamp.org/images/j8cycgQmG0qdEo2ix46ZdPdR0UmGqyn2mZiD)

Cela ajoutera une page « CountryData.cshtml » à notre dossier « BlazorDDL.Client/Pages ».

Ouvrez la page « CountryData.cshtml » et mettez le code suivant dedans.

```
@using BlazorDDL.Shared.Models@page "/country"@inject HttpClient Http<h1>Données des Pays</h1><p>Ce composant démontre les listes déroulantes en cascade en utilisant Entity Framework Core</p><hr />@if (countryList == null){    <p><em>Chargement...</em></p>}else{    <div class="row">        <div class="col-md-4">            <label for="Country" class="control-label">Pays</label>        </div>        <div class="col-md-4">            <label asp-for="Cities" class="control-label">Villes</label>        </div>    </div>    <div class="row" style="padding-top:10px">        <div class="col-md-4">            <select class="form-control" onchange="@CountryClicked">                <option value="">-- Sélectionner un Pays --</option>                @foreach (var country in countryList)                {                    <option value="@country.CountryId">@country.CountryName</option>                }            </select>        </div>        <div class="col-md-4">            <select class="form-control" onchange="@CityClicked">                <option value="">-- Sélectionner une Ville --</option>                @if (cityList != null)                {                    @foreach (var city in cityList)                    {                        <option value="@city.CityName">@city.CityName</option>                    }                }            </select>        </div>    </div>    <div class="row" style="padding-top:50px">        <div class="col-md-4">            <label class="control-label">Nom du Pays : @countryName</label>        </div>        <div class="col-md-4">            <label class="control-label">Nom de la Ville : @cityName</label>        </div>    </div>}@functions {List<Country> countryList = new List<Country>();List<Cities> cityList = new List<Cities>();string countryId { get; set; }string countryName { get; set; }string cityName { get; set; }protected override async Task OnInitAsync(){    countryList = await Http.GetJsonAsync<List<Country>>("api/Countries/GetCountryList");}protected async void CountryClicked(UIChangeEventArgs countryEvent){    cityList.Clear();    cityName = string.Empty;    countryId = countryEvent.Value.ToString();    countryName = countryList.FirstOrDefault(s => s.CountryId == countryId).CountryName;    cityList = await Http.GetJsonAsync<List<Cities>>("api/Countries/GetCities/" + countryId);    this.StateHasChanged();}void CityClicked(UIChangeEventArgs cityEvent){    cityName = cityEvent.Value.ToString();    this.StateHasChanged();}}
```

Comprenons ce code.

En haut, nous avons inclus l'espace de noms BlazorDDL.Shared.Models afin de pouvoir utiliser nos classes de modèle Country et Cities sur cette page. Nous définissons la route de cette page en utilisant la directive @page. Donc, dans cette application, si nous ajoutons « /country » à l'URL de base, nous serons redirigés vers cette page. Nous injectons également le service HttpClient pour activer l'appel à l'API web.

Ensuite, nous avons défini la section HTML pour afficher deux listes déroulantes sur notre page web. Nous appelons la méthode « CountryClicked » sur l'événement « onchange » de la liste déroulante des pays. Cette méthode appellera la méthode de l'API web « GetCities » pour récupérer les données des villes depuis la table Cities correspondant à l'identifiant du pays sélectionné.

Nous définissons également la valeur de la propriété « countryName » sur le pays sélectionné. La méthode « StateHasChanged » est invoquée pour rafraîchir l'interface utilisateur. Cela garantira que la liste déroulante des villes sera actualisée lors du changement de la liste déroulante des pays.

De même, nous avons une autre liste déroulante pour afficher les données des villes correspondant à chaque pays. Sur l'événement « onchange » de la liste déroulante des villes, nous définissons la valeur de la propriété « cityName » sur la ville sélectionnée.

Nous affichons également le nom du pays sélectionné et la valeur du nom de la ville sur la page web.

La section @functions contient toutes nos propriétés et méthodes. Nous avons défini deux variables : countryList de type Country et cityList de type City. Celles-ci gèrent les données des pays et des villes, respectivement. Nous avons également déclaré trois propriétés pour gérer les données countryId, countryName et cityName.

À l'intérieur de la méthode « OnInitAsync », nous appelons la méthode de l'API web GetCountryList pour remplir countryList. Cette variable est utilisée pour lier les données à la liste déroulante des pays lors du chargement de la page.

### Ajout du Lien au Menu de Navigation

La dernière étape consiste à ajouter le lien vers notre page « CountryData » dans le menu de navigation. Ouvrez la page « BlazorDDL.Client/Shared/NavMenu.cshtml » et mettez le code suivant dedans.

```
<div class="top-row pl-4 navbar navbar-dark">    <a class="navbar-brand" href="/">BlazorDDL</a>    <button class="navbar-toggler" onclick=@ToggleNavMenu>        <span class="navbar-toggler-icon"></span>    </button></div><div class=@(collapseNavMenu ? "collapse" : null) onclick=@ToggleNavMenu>    <ul class="nav flex-column">        <li class="nav-item px-3">            <NavLink class="nav-link" href="/" Match=NavLinkMatch.All>                <span class="oi oi-home" aria-hidden="true"></span> Accueil            </NavLink>        </li>        <li class="nav-item px-3">            <NavLink class="nav-link" href="/counter">                <span class="oi oi-plus" aria-hidden="true"></span> Compteur            </NavLink>        </li>        <li class="nav-item px-3">            <NavLink class="nav-link" href="/fetchdata">                <span class="oi oi-list-rich" aria-hidden="true"></span> Récupérer les données            </NavLink>        </li>        <li class="nav-item px-3">            <NavLink class="nav-link" href="/country">                <span class="oi oi-list-rich" aria-hidden="true"></span> Pays            </NavLink>        </li>    </ul></div>@functions {bool collapseNavMenu = true;void ToggleNavMenu(){    collapseNavMenu = !collapseNavMenu;}}
```

Maintenant, nous avons terminé notre application de liste déroulante en cascade.

### Démonstration d'Exécution

Lancez l'application.

Une page web s'ouvrira comme montré dans l'image ci-dessous. Le menu de navigation à gauche montre le lien de navigation vers la page CountryData.

![Image](https://cdn-media-1.freecodecamp.org/images/r6L1EKqQvVQYBNuPYvZqLndvhr1y9LoqPpga)

Cliquez sur « country » dans le menu de navigation. Il vous redirigera vers la vue CountryData où vous pouvez voir deux listes déroulantes — Pays et Villes — sur la page. Remarquez que l'URL a « /country » ajouté à celle-ci comme nous l'avons défini en utilisant la directive @page.

![Image](https://cdn-media-1.freecodecamp.org/images/Fq5uDHelWT5tLTm5viD8CeSTfuO6oQtrOx88)

Ici, vous pouvez voir les deux listes déroulantes. La liste déroulante des pays est déjà remplie avec les données des pays. Si nous sélectionnons un nom de pays dans cette liste déroulante, alors la liste déroulante des villes sera également remplie avec les données des villes correspondantes. Nous pouvons également voir les valeurs du pays et de la ville sélectionnés dans les libellés sous les deux listes déroulantes.

![Image](https://cdn-media-1.freecodecamp.org/images/kKA-ZvMJYGII82wAiK8QiKz8zsDdCcxoMN-K)

### Hébergement de l'application

Pour apprendre comment héberger une application Blazor en utilisant IIS, référez-vous à [Déployer une Application Blazor sur IIS](http://ankitsharmablogs.com/deploying-a-blazor-application-on-iis/)

### Conclusion

Nous avons appris comment créer des listes déroulantes en cascade dans Blazor en utilisant l'approche database first d'Entity Framework Core avec l'aide de Visual Studio 2017 et SQL Server 2014. Veuillez récupérer le code source depuis [GitHub](https://github.com/AnkitSharma-007/Blazor-CascadingDDL-EFCore) et jouez avec pour obtenir une meilleure compréhension.

Obtenez mon livre [Blazor Quick Start Guide](https://www.amazon.com/Blazor-Quick-Start-Guide-applications/dp/178934414X/ref=sr_1_1?ie=UTF8&qid=1542438251&sr=8-1&keywords=Blazor-Quick-Start-Guide) pour en apprendre davantage sur Blazor.

Vous pouvez consulter mes autres articles sur Blazor [ici](http://ankitsharmablogs.com/category/blazor/)

Vous pouvez également trouver cet article sur [C# Corner](https://www.c-sharpcorner.com/article/cascading-dropdownlist-in-blazor-using-ef-core/).

### Voir aussi

* [ASP.NET Core — Getting Started With Blazor](http://ankitsharmablogs.com/asp-net-core-getting-started-with-blazor/)
* [ASP.NET Core — CRUD Using Blazor And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-blazor-and-entity-framework-core/)
* [ASP.NET Core — CRUD Using Angular 5 And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-angular-5-and-entity-framework-core/)
* [ASP.NET Core — CRUD With React.js And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-with-react-js-and-entity-framework-core/)
* [ASP.NET Core — Using Highcharts With Angular 5](http://ankitsharmablogs.com/asp-net-core-using-highcharts-with-angular-5/)

_Publié à l'origine sur_ [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)