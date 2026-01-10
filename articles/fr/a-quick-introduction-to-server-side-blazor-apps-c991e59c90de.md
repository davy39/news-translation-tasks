---
title: Une introduction rapide aux applications Blazor côté serveur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-09T23:29:28.000Z'
originalURL: https://freecodecamp.org/news/a-quick-introduction-to-server-side-blazor-apps-c991e59c90de
coverImage: https://cdn-media-1.freecodecamp.org/images/1*INENIFhB5lJNvVrYuxXX4w.png
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
seo_title: Une introduction rapide aux applications Blazor côté serveur
seo_desc: 'By Ankit Sharma

  Introduction

  We all know that the Blazor framework is a client-side web framework. But is it
  possible to run a Blazor application separate from a UI thread? The latest version
  0.5.0 of Blazor gives us the flexibility to run it in a se...'
---

Par Ankit Sharma

### Introduction

Nous savons tous que le framework Blazor est un framework web côté client. Mais est-il possible d'exécuter une application Blazor séparément d'un thread UI ? La dernière version 0.5.0 de Blazor nous offre la flexibilité de l'exécuter dans un processus séparé du processus de rendu. Nous allons explorer Blazor côté serveur dans cet article.

### Qu'est-ce que Blazor côté serveur ?

Puisque Blazor est un framework web côté client, la logique des composants et l'interaction avec le DOM se produisent dans le même processus.

![Image](https://cdn-media-1.freecodecamp.org/images/SE8WnGMv3amme5Z6z5vClAJiTPXhzNUq1h5E)

Cependant, la conception du framework Blazor est intelligente et suffisamment flexible pour exécuter l'application séparément du processus de rendu. Par exemple, nous pouvons exécuter Blazor dans un thread web worker séparément du thread UI.

Dans ce scénario, le thread UI poussera les événements vers le thread worker Blazor, et Blazor poussera les mises à jour de l'UI vers le thread UI selon les besoins. Bien que Blazor ne supporte pas encore cette fonctionnalité, le framework Blazor est conçu pour gérer de tels scénarios et est censé le supporter dans les futures versions.

![Image](https://cdn-media-1.freecodecamp.org/images/0o-zbwSglIvnNx8gUvHA37oJWSf5OMj1kCkt)

À partir de Blazor 0.5.0, nous pouvons exécuter une application Blazor sur le serveur. Cela signifie que nous pouvons exécuter un composant Blazor côté serveur sur .NET Core tandis que d'autres fonctionnalités, telles que l'UI, se mettent à jour. La gestion des événements et les appels JavaScript interop sont gérés par une connexion SignalR via le réseau. La partie .NET s'exécute sous CoreCLR au lieu de WebAssembly, ce qui nous donne accès à l'écosystème .NET complet, au débogage, à la compilation JIT, etc. Cela ajoute de l'extensibilité au framework Blazor, car Blazor côté serveur utilise le même modèle de composant que l'exécution d'une application Blazor côté client.

![Image](https://cdn-media-1.freecodecamp.org/images/eWgI2AVm7-gGqD0B9fxWq5QlQ0wHiB06glT4)

Créons notre première application Blazor côté serveur et explorons-la pour mieux comprendre cette nouvelle fonctionnalité.

### Prérequis

* Installer le SDK .NET Core 2.1 ou supérieur depuis [ici](https://www.microsoft.com/net/learn/get-started-with-dotnet-tutorial#windowscmd)
* Installer Visual Studio 2017 v15.7 ou supérieur depuis [ici](https://visualstudio.microsoft.com/downloads/)
* Installer l'extension ASP.NET Core Blazor Language Services depuis [ici](https://marketplace.visualstudio.com/items?itemName=aspnet.blazor)

Les versions de Visual Studio 2017 antérieures à v15.7 ne supportent pas le framework Blazor.

### Création d'une application Blazor côté serveur

Ouvrez Visual Studio et sélectionnez Fichier >> Nouveau >> Projet.

Après avoir sélectionné le projet, une boîte de dialogue « Nouveau Projet » s'ouvrira. Sélectionnez .NET Core dans le menu Visual C# du panneau de gauche. Ensuite, sélectionnez « Application Web ASP.NET Core » parmi les types de projets disponibles. Nommez le projet **ServerSideBlazor** et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/PVahH9QmYcbo2PgExBUIPugyXrOr-qxbCQho)

Après avoir cliqué sur OK, une nouvelle boîte de dialogue s'ouvrira vous demandant de sélectionner le modèle de projet. Vous pouvez voir deux menus déroulants en haut à gauche de la fenêtre de modèle. Sélectionnez « .NET Core » et « ASP.NET Core 2.1 » dans ces menus déroulants. Ensuite, sélectionnez le modèle « Blazor (côté serveur dans ASP.NET Core) » et appuyez sur OK.

![Image](https://cdn-media-1.freecodecamp.org/images/apVoM-bwspujj5zLwGZ1bNJdWNelcHQSdXEd)

Cela créera notre solution Blazor côté serveur. Vous pouvez voir la structure des dossiers dans l'Explorateur de solutions, comme montré dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/cuCSqzS3yfGhGWLsjFrd0xsE0ijhORI2zvxi)

La solution contient deux fichiers de projet :

1. ServerSideBlazor.App : il s'agit de notre projet hébergé ASP.NET Core.
2. ServerSideBlazor.Server : il contient notre application Blazor côté serveur.

Toute notre logique de composant se trouve dans l'application Blazor côté serveur. Cependant, cette logique ne s'exécute pas côté client dans le navigateur, mais plutôt côté serveur dans l'application hôte ASP.NET Core. Cette application utilise **blazor.server.js** pour le démarrage au lieu de blazor.webassembly.js qui est utilisé par les applications Blazor normales. Cela permet à l'application d'établir une connexion SignalR via le réseau pour gérer les mises à jour de l'UI et le transfert d'événements. Le fichier **blazor.server.js** est présent dans le dossier « \ServerSideBlazor.App\bin\Debug\netstandard2.0\dist\_framework », et la balise <script> pour l'inclure dans le projet est présente dans le fichier **wwwroot/index.html**.

![Image](https://cdn-media-1.freecodecamp.org/images/tC8zrjwd8WrCeS9hAiPxoqTmLmHU3HVJPenZ)

Le fichier **blazor.server.js** est le seul composant qui distingue une application Blazor côté serveur d'une application Blazor côté client. Si nous fournissons une référence à **blazor.webassembly.js** au lieu de **blazor.server.js** dans le fichier index.html, alors cette application se comportera comme une application Blazor côté client.

L'application Blazor est hébergée par l'application ASP.NET Core, qui configure également le point de terminaison SignalR. Puisque l'application Blazor s'exécute sur le serveur, la logique de gestion des événements peut accéder directement aux ressources et services du serveur.

Par exemple, si nous voulons récupérer des données, nous n'avons plus besoin d'émettre une requête HTTP. Au lieu de cela, nous pouvons configurer un service sur le serveur et l'utiliser pour récupérer les données.

Dans l'application exemple que nous avons créée, le **WeatherForecastService** est défini dans le dossier « ServerSideBlazor.App/Services ».

```
using System;using System.Linq;using System.Threading.Tasks;namespace ServerSideBlazor.App.Services{    public class WeatherForecastService    {        private static string[] Summaries = new[]        {            "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"        };        public Task<WeatherForecast[]> GetForecastAsync(DateTime startDate)        {            var rng = new Random();            return Task.FromResult(Enumerable.Range(1, 5).Select(index => new WeatherForecast            {                Date = startDate.AddDays(index),                TemperatureC = rng.Next(-20, 55),                Summary = Summaries[rng.Next(Summaries.Length)]            }).ToArray());        }    }}
```

Ensuite, nous devons configurer le service dans la méthode **ConfigureServices** du fichier « ServerSideBlazor.App/startup.cs ».

```
public void ConfigureServices(IServiceCollection services){    services.AddSingleton<WeatherForecastService>();}
```

Nous allons ensuite injecter le service dans la page de vue **FetchData.cshtml**, où la méthode **GetForecastAsync** est appelée pour récupérer les données.

```
@using ServerSideBlazor.App.Services@page "/fetchdata"@inject WeatherForecastService ForecastService// HTML DOM ici.@functions {    WeatherForecast[] forecasts;    protected override async Task OnInitAsync()    {        forecasts = await ForecastService.GetForecastAsync(DateTime.Now);    }}
```

Allez-y et lancez l'application dans Google Chrome. Cela ouvrira une fenêtre de navigateur et l'application ressemblera à une application Blazor normale. Ouvrez les outils de développement Chrome. Allez dans l'onglet « Réseau » et vous pouvez voir que l'application n'a pas téléchargé de runtime .NET ou d'assembly d'application.

![Image](https://cdn-media-1.freecodecamp.org/images/jjiNmnaV4euLEWb1OFxiqAAf9IM7jbeKMngv)

Cela est dû au fait que l'application s'exécute côté serveur sur .NET Core. Puisque les dépendances ne sont pas téléchargées au démarrage de l'application, la taille de l'application est plus petite. Elle se chargera également plus rapidement par rapport à une application Blazor normale.

### Avantages de Blazor côté serveur

Les applications Blazor côté serveur nous offrent de nombreux avantages :

1. Puisque la mise à jour de l'UI est gérée via une connexion SignalR, nous pouvons éviter les rafraîchissements de page inutiles.
2. La taille de téléchargement de l'application est plus petite et le chargement initial de l'application est plus rapide.
3. Le composant Blazor peut tirer pleinement parti des capacités du serveur, telles que l'utilisation d'API compatibles avec .NET Core.
4. Il supportera également les outils .NET existants comme le débogage de l'application et la compilation JIT.
5. Puisque Blazor côté serveur s'exécute sous un processus natif .NET Core et non sous Mono WebAssembly, il est également supporté sur les navigateurs qui n'ont pas de support WebAssembly.

Mais il y a aussi quelques inconvénients pour les applications Blazor côté serveur :

1. Puisque l'interaction avec l'UI implique une communication SignalR, cela ajoute une étape supplémentaire dans les appels réseau, ce qui entraîne une certaine latence.
2. La scalabilité des applications (gestion de plusieurs connexions client) est également un défi.

### Conclusion

Nous avons appris à connaître la dernière application Blazor côté serveur introduite avec la version 0.5.0 de Blazor, et nous comprenons maintenant comment elle est différente d'une application Blazor côté client normale. Nous avons également discuté des avantages et des inconvénients de l'utilisation d'une application Blazor côté serveur par rapport à une application Blazor côté client.

Obtenez mon livre [Blazor Quick Start Guide](https://www.amazon.com/Blazor-Quick-Start-Guide-applications/dp/178934414X/ref=sr_1_1?ie=UTF8&qid=1542438251&sr=8-1&keywords=Blazor-Quick-Start-Guide) pour en apprendre davantage sur Blazor.

Vous pouvez consulter mes autres articles sur Blazor [ici](http://ankitsharmablogs.com/category/blazor/).

Vous préparez des entretiens ? Lisez mon article sur [C# Coding Questions For Technical Interviews](http://ankitsharmablogs.com/csharp-coding-questions-for-technical-interviews/)

### Voir aussi

* [ASP.NET Core — Getting Started With Blazor](http://ankitsharmablogs.com/asp-net-core-getting-started-with-blazor/)
* [ASP.NET Core — CRUD Using Blazor And Entity Framework Core](http://ankitsharmablogs.com/asp-net-core-crud-using-blazor-and-entity-framework-core/)
* [Cascading DropDownList In Blazor Using EF Core](http://ankitsharmablogs.com/cascading-dropdownlist-in-blazor-using-ef-core/)
* [Creating a SPA Using Razor Pages With Blazor](http://ankitsharmablogs.com/creating-a-spa-using-razor-pages-with-blazor/)
* [Deploying a Blazor Application on IIS](http://ankitsharmablogs.com/deploying-a-blazor-application-on-iis/)
* [JavaScript Interop in Blazor](http://ankitsharmablogs.com/javascript-interop-in-blazor/)

Publié à l'origine sur [https://ankitsharmablogs.com/](https://ankitsharmablogs.com/)