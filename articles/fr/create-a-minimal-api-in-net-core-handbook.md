---
title: Comment créer une API minimale dans .NET Core – Un guide étape par étape
subtitle: ''
author: Isaiah Clifford Opoku
co_authors: []
series: null
date: '2024-12-02T16:55:35.566Z'
originalURL: https://freecodecamp.org/news/create-a-minimal-api-in-net-core-handbook
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1733158500882/9af04a12-2121-4efd-a66f-00330896e358.png
tags:
- name: dotnet
  slug: dotnet
- name: .NET
  slug: net
- name: Web API
  slug: web-api
- name: MinimalApi
  slug: minimalapi
- name: handbook
  slug: handbook
seo_title: Comment créer une API minimale dans .NET Core – Un guide étape par étape
seo_desc: 'Minimal APIs are an exciting feature introduced in .NET 6, designed to
  revolutionize how you create APIs.

  Imagine building robust APIs with minimal code and zero boilerplate—no more wrestling
  with controllers, routing, or middleware. That’s what mini...'
---

Les API minimales sont une fonctionnalité passionnante introduite dans .NET 6, conçue pour révolutionner la manière dont vous créez des API.

Imaginez construire des API robustes avec un code minimal et zéro code passe-partout—plus besoin de lutter avec les contrôleurs, le routage ou les middlewares. C'est ce que les API minimales vous permettent de faire. L'idée avec ces API est de rationaliser le processus de développement, le rendant incroyablement facile et efficace.

Dans cet article, nous allons plonger dans le monde des API minimales dans .NET 8 et vous guider à travers la création d'une API de librairie entièrement fonctionnelle. Vous apprendrez comment obtenir tous les livres, récupérer un livre par son ID, ajouter de nouveaux livres et même supprimer des livres. Commençons.

# Table des matières

* [Prérequis](#heading-prerequisites)
    
* [Introduction aux API minimales](#heading-introduction-aux-api-minimales)
    
* [Comment créer une API minimale](#heading-comment-creer-une-api-minimale)
    
* [Méthodes HTTP dans les API basées sur les contrôleurs et les API minimales](#heading-methodes-http-dans-les-api-basees-sur-les-controleurs-et-les-api-minimales)
    
* [Fichiers du projet d'API minimale](#heading-fichiers-du-projet-dapi-minimale)
    
* [Comment créer les modèles](#heading-comment-creer-les-modeles)
    
* [Comment créer le contexte de la base de données](#heading-comment-creer-le-contexte-de-la-base-de-donnees)
    
* [Comment créer un contrat](#heading-comment-creer-un-contrat)
    
* [Comment ajouter des services](#heading-comment-ajouter-des-services)
    
* [Comment créer des exceptions](#heading-comment-creer-des-exceptions)
    
* [Comment créer les points de terminaison de l'API](#heading-comment-creer-les-points-de-terminaison-de-lapi)
    
* [Comment ajouter des données de départ à la base de données](#heading-comment-ajouter-des-donnees-de-depart-a-la-base-de-donnees)
    
* [Comment effectuer une migration](#heading-comment-effectuer-une-migration)
    
* [Comment tester les points de terminaison de l'API](#heading-comment-tester-les-points-de-terminaison-de-lapi)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de commencer, assurez-vous d'avoir les prérequis suivants installés sur votre machine :

* [.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0)
    
* [Visual Studio Code](https://code.visualstudio.com/download) ou tout autre éditeur de code de votre choix
    
* [C# Dev Kit](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp) pour Visual Studio Code
    

Alternativement, vous pouvez utiliser Visual Studio 2022, qui inclut un support intégré pour .NET 8. Mais dans cet article, nous utiliserons Visual Studio Code. Il est léger, facile à utiliser et multiplateforme.

Nous utiliserons Swagger UI pour tester notre API. Swagger UI est un outil puissant qui vous permet d'interagir avec votre API directement depuis votre navigateur. Il fournit une interface conviviale pour tester vos points de terminaison d'API, ce qui facilite le test et le débogage de votre API.

Lorsque vous créez un nouveau projet, il installera automatiquement les packages nécessaires et configurera le projet pour utiliser Swagger UI. .NET 8 inclut Swagger UI par défaut, donc que vous créiez votre application dans Visual Studio ou avec .NET, Swagger UI sera configuré pour vous.

Exécutez votre application, et Swagger UI s'ouvrira automatiquement dans votre navigateur – mais comme nous utilisons VS Code, nous devons cliquer sur le numéro de port dans notre terminal.

Vous pouvez trouver le code source de ce projet sur [GitHub](https://github.com/Clifftech123/bookapi-minimal).

## Introduction aux API minimales

Imaginez travailler dans une base de code avec de nombreux points de terminaison, la rendant assez grande et complexe. Traditionnellement, la construction d'une API dans [ASP.NET](http://ASP.NET) Core implique l'utilisation de contrôleurs, de routage, de middlewares et d'une quantité importante de code passe-partout. Mais il existe deux approches pour construire une API dans ASP.NET Core : la manière traditionnelle et la manière minimale.

La manière traditionnelle est familière à la plupart des développeurs, impliquant des contrôleurs et un code d'infrastructure étendu. La manière minimale, introduite dans `.NET 6`, vous permet de créer des API avec un code minimal et zéro passe-partout. Cette approche simplifie le processus de développement, vous permettant de vous concentrer sur l'écriture de la logique métier plutôt que de traiter avec le code d'infrastructure.

Les API minimales sont légères, rapides et parfaites pour construire des API de petite à moyenne taille. Elles sont idéales pour le prototypage, la construction de microservices ou la création d'API simples qui ne nécessitent pas beaucoup de complexité. Dans ce guide, nous explorerons le monde des API minimales dans .NET 6 et apprendrons comment créer une API de librairie entièrement fonctionnelle à partir de zéro.

## Comment créer une API minimale

La création d'une API minimale est simple lorsque vous utilisez le `dotnet CLI`, car le modèle par défaut est déjà une API minimale. Mais si vous utilisez Visual Studio, vous devrez supprimer le code passe-partout qui accompagne le modèle de projet.

Commençons par utiliser le `dotnet CLI` pour créer un projet d'API minimale.

```bash

dotnet new webapi  -n BookStoreApi
```

La commande `dotnet new webapi` crée un nouveau projet d'API minimale nommé `BookStoreApi`. Ce projet contient les fichiers et dossiers nécessaires pour commencer.

![Structure des fichiers du projet d'API minimale](https://cdn.hashnode.com/res/hashnode/image/upload/v1732623879052/3db8614b-7b27-43ce-ad84-9fa66001b535.png align="left")

Explorons la structure du projet :

* `Program.cs` : Le point d'entrée de l'application, où l'hôte est configuré.
    
* `bookapi-minimal.sln` : Le fichier de solution qui contient le projet.
    
* `bookapi-minimal.http` : Un fichier qui contient des requêtes HTTP d'exemple pour tester l'API.
    
* `bookapi-minimal.csproj` : Le fichier de projet qui contient la configuration du projet.
    
* `appsettings.json` : Le fichier de configuration qui stocke les paramètres de l'application.
    
* `appsettings.Development.json` : Le fichier de configuration pour l'environnement de développement.
    

Lorsque vous ouvrez le fichier program.cs, vous remarquerez que le code est minimal. Le fichier `Program.cs` contient le code suivant :

```csharp

var builder = WebApplication.CreateBuilder(args);

// Ajouter des services au conteneur.
// En savoir plus sur la configuration de Swagger/OpenAPI à l'adresse https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configurer le pipeline de requêtes HTTP.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

var summaries = new[]
{
    "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
};

app.MapGet("/weatherforecast", () =>
{
    var forecast =  Enumerable.Range(1, 5).Select(index =>
        new WeatherForecast
        (
            DateOnly.FromDateTime(DateTime.Now.AddDays(index)),
            Random.Shared.Next(-20, 55),
            summaries[Random.Shared.Next(summaries.Length)]
        ))
        .ToArray();
    return forecast;
})
.WithName("GetWeatherForecast")
.WithOpenApi();

app.Run();

record WeatherForecast(DateOnly Date, int TemperatureC, string? Summary)
{
    public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);
}
```

Si vous ne comprenez pas encore complètement le code, ne vous inquiétez pas—nous le couvrirons en détail dans les sections à venir. Le point clé à retenir est que les API minimales nécessitent très peu de code, ce qui est l'un de leurs principaux avantages.

Le code par défaut configure une API simple de prévisions météorologiques que vous pouvez utiliser pour tester votre configuration. Il génère une liste de prévisions météorologiques et les retourne lorsque vous effectuez une requête `GET` vers le point de terminaison `/weatherforecast`. De plus, le code inclut Swagger UI pour vous aider à tester l'API.

Portez une attention particulière à la méthode `app.MapGet`, qui mappe une route à une fonction de gestionnaire. Dans ce cas, elle mappe la route `/weatherforecast` à une fonction qui retourne une liste de prévisions météorologiques. Nous utiliserons des méthodes similaires pour créer nos propres points de terminaison dans les prochaines sections.

Avant de commencer à créer notre structure de dossiers de projet, comprenons les méthodes HTTP dans les API basées sur les contrôleurs et les API minimales.

## Méthodes HTTP dans les API basées sur les contrôleurs et les API minimales

Dans une approche basée sur les contrôleurs, qui est la manière traditionnelle de créer des API web, vous devez créer une classe de contrôleur et définir des méthodes pour chaque méthode HTTP. Par exemple :

* Pour créer une méthode `GET`, vous utilisez l'attribut `[HttpGet]`.
    
* Pour créer une méthode `POST`, vous utilisez l'attribut `[HttpPost]`.
    
* Pour créer une méthode `PUT`, vous utilisez l'attribut `[HttpPut]`.
    
* Pour créer une méthode `DELETE`, vous utilisez l'attribut `[HttpDelete]`.
    

C'est ainsi que les points de terminaison sont créés dans une approche basée sur les contrôleurs.

En revanche, les API minimales utilisent des méthodes comme `app.MapGet`, `app.MapPost`, `app.MapPut` et `app.MapDelete` pour créer des points de terminaison. C'est la principale différence entre les deux approches : les API basées sur les contrôleurs utilisent des attributs pour définir les points de terminaison, tandis que les API minimales utilisent des méthodes.

Maintenant que vous comprenez comment gérer les requêtes HTTP dans les API basées sur les contrôleurs et les API minimales, créons notre structure de dossiers de projet.

Avant de créer notre structure de dossiers de projet, exécutons d'abord ce que nous avons. Comme nous l'avons appris précédemment, lorsque vous créez un projet avec Visual Studio ou .NET CLI, il inclut un projet WeatherForecast par défaut que nous pouvons exécuter et voir sur l'interface utilisateur. Exécutons-le pour nous assurer que tout fonctionne avant de créer notre structure de dossiers de projet.

Exécutez cette commande :

```bash

dotnet run
```

Vous devriez voir la sortie suivante :

```bash
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: http://localhost:5228
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
info: Microsoft.Hosting.Lifetime[0]
      Content root path: D:\Devolopemnt\Dotnet\bookapi-minimal
```

Cela signifie que l'application est en cours d'exécution et écoute sur [`http://localhost:5228`](http://localhost:5228). Comme je l'ai mentionné ci-dessus, puisque nous utilisons le `dotnet CLI` et Visual Studio Code, l'application n'ouvrira pas automatiquement le navigateur pour nous. Nous devons le faire manuellement.

Ouvrez votre navigateur et accédez à [`http://localhost:5228/swagger/index.html`](http://localhost:5228/swagger/index.html) pour voir la réponse par défaut de l'API.

Vous devriez voir quelque chose comme ceci :

![Swagger UI](https://cdn.hashnode.com/res/hashnode/image/upload/v1732623894640/b882a1ee-3957-4958-8f59-20b44fe7fb7d.png align="left")

La prochaine chose que nous devons faire est de trouver un moyen de structurer notre projet et de créer les fichiers et dossiers nécessaires pour commencer.

## Fichiers du projet d'API minimale

Pour organiser notre projet, nous allons créer une hiérarchie de dossiers structurée. Cela nous aidera à garder notre code propre et maintenable. Voici la structure de dossiers que nous allons utiliser :

* **AppContext** : Contient le contexte de la base de données et les configurations associées.
    
* **Configurations** : Contient les configurations d'Entity Framework Core et les données de départ pour la base de données.
    
* **Contracts** : Contient les objets de transfert de données (DTO) utilisés dans notre application.
    
* **Endpoints** : Où nous définissons et configurons nos points de terminaison d'API minimale.
    
* **Exceptions** : Contient les classes d'exceptions personnalisées utilisées dans le projet.
    
* **Extensions** : Contient les méthodes d'extension que nous utiliserons dans tout le projet.
    
* **Models** : Contient les modèles de logique métier.
    
* **Services** : Contient les classes de service qui implémentent la logique métier.
    
* **Interfaces** : Contient les définitions d'interfaces utilisées pour mapper nos services.
    

Dans Visual Studio Code, vous pouvez créer cette structure de dossiers comme suit :

```bash
- AppContext
- Configurations
- Contracts
- Endpoints
- Exceptions
- Extensions
- Models
- Services
- Interfaces
```

Après la configuration, la structure de dossiers de votre projet devrait ressembler à ceci :

![Structure des dossiers du projet BookApi](https://cdn.hashnode.com/res/hashnode/image/upload/v1732623997951/8118c444-0d28-4bb7-8cad-2a9fd88c8c25.png align="left")

Maintenant que notre structure de projet est configurée, nous pouvons commencer à écrire notre code. Commençons par créer nos modèles.

## Comment créer les modèles

Dans cette section, nous allons créer des modèles pour notre application. Les modèles sont les éléments de base de notre application, représentant les données avec lesquelles notre application travaillera. Pour notre exemple, nous allons créer un modèle pour un livre.

Pour commencer, créez un dossier nommé `Models` dans votre répertoire de projet. À l'intérieur de ce dossier, créez un fichier nommé `BookModel.cs` et ajoutez le code suivant :

```csharp
// Models/BookModel.cs


namespace bookapi_minimal.Models
{
    public class BookModel
    {
        public Guid Id { get; set; }
        public string Title { get; set; }
        public string Author { get; set; }
        public string Description { get; set; }
        public string Category { get; set; }
        public string Language { get; set; }
        public int TotalPages { get; set; }
    }
}
```

Cette classe `BookModel` définit les propriétés qui représentent les détails d'un livre, tels que son `titre`, `auteur`, `description`, `catégorie`, `langue` et `nombre total de pages`. Chaque propriété est conçue pour contenir des informations spécifiques sur le livre, ce qui facilite la gestion et la manipulation des données de livre au sein de notre application.

Maintenant que nous avons créé notre modèle, créons notre contexte de base de données.

## Comment créer le contexte de la base de données

Le contexte de la base de données est une classe qui représente une session avec la base de données. Il est responsable de l'interaction avec la base de données et de l'exécution des opérations de la base de données. Dans notre application, nous utiliserons Entity Framework Core pour interagir avec notre base de données.

### Installer les packages requis

Avant de créer notre contexte de base de données, nous devons installer les packages suivants :

* [`Microsoft.EntityFrameworkCore.Design`](http://Microsoft.EntityFrameworkCore.Design)
    
* `Microsoft.EntityFrameworkCore`
    
* `Microsoft.EntityFrameworkCore.SqlServer`
    
* [`Microsoft.EntityFrameworkCore.Tools`](http://Microsoft.EntityFrameworkCore.Tools)
    
* `FluentValidation.DependencyInjectionExtensions`
    

Vous pouvez installer ces packages en utilisant les commandes suivantes :

```bash
dotnet add package Microsoft.EntityFrameworkCore.Design
dotnet add package Microsoft.EntityFrameworkCore
dotnet add package Microsoft.EntityFrameworkCore.SqlServer
dotnet add package Microsoft.EntityFrameworkCore.Tools
dotnet add package FluentValidation.DependencyInjectionExtensions
```

### Vérifier l'installation des packages

Pour vérifier que les packages sont installés, ouvrez le fichier `bookapi-minimal.csproj` dans le répertoire racine de votre projet. Vous devriez voir les packages installés listés comme suit :

```xml
<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
    <RootNamespace>bookapi_minimal</RootNamespace>
  </PropertyGroup>

  <ItemGroup>
   <PackageReference Include="FluentValidation.DependencyInjectionExtensions" Version="11.9.2" />
    <PackageReference Include="Microsoft.AspNetCore.OpenApi" Version="8.0.6" />
    <PackageReference Include="Microsoft.EntityFrameworkCore" Version="8.0.8" />
    <PackageReference Include="Microsoft.EntityFrameworkCore.Design" Version="8.0.8">
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
      <PrivateAssets>all</PrivateAssets>
    </PackageReference>
    <PackageReference Include="Microsoft.EntityFrameworkCore.SqlServer" Version="8.0.8" />
    <PackageReference Include="Microsoft.EntityFrameworkCore.Tools" Version="8.0.8">
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
      <PrivateAssets>all</PrivateAssets>
    </PackageReference>
    <PackageReference Include="Swashbuckle.AspNetCore" Version="6.4.0" />
  </ItemGroup>

</Project>
```

Cela confirme que les packages ont été installés avec succès.

Maintenant, créons notre contexte de base de données.

Dans le dossier AppContext, créez un nouveau fichier nommé `ApplicationContext.cs` et ajoutez le code suivant :

```csharp
// AppContext/ApplicationContext.cs

using bookapi_minimal.Models;
using Microsoft.EntityFrameworkCore;

namespace bookapi_minimal.AppContext
{
 
    public class ApplicationContext(DbContextOptions<ApplicationContext> options) : DbContext(options)
    {

        // Schéma par défaut pour le contexte de la base de données
        private const string DefaultSchema = "bookapi";
     

       // DbSet pour représenter la collection de livres dans notre base de données
        public DbSet<BookModel> Books { get; set; }
        
        // Constructeur pour configurer le contexte de la base de données
        
        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);
            modelBuilder.HasDefaultSchema(DefaultSchema);

            modelBuilder.ApplyConfigurationsFromAssembly(typeof(ApplicationContext).Assembly);

            modelBuilder.ApplyConfigurationsFromAssembly(typeof(ApplicationContext).Assembly);

        }

    }
}
```

Analysons le code ci-dessus :

* Nous définissons une classe nommée `ApplicationContext` qui hérite de `DbContext`. La classe `DbContext` fait partie d'Entity Framework Core et représente une session avec la base de données.
    
* Le constructeur accepte une instance de `DbContextOptions<ApplicationContext>`. Ce constructeur est utilisé pour configurer les options du contexte de la base de données.
    
* Nous définissons une propriété nommée `Books` de type `DbSet<BookModel>`. Cette propriété représente la collection de livres dans notre base de données.
    
* Nous remplaçons la méthode `OnModelCreating` pour configurer le schéma de la base de données et appliquer les configurations définies dans notre application.
    

Maintenant que nous avons créé notre contexte de base de données, créons notre méthode d'extension et enregistrons notre contexte de base de données dans le conteneur d'injection de dépendances.

### Créer une méthode d'extension

Avant de créer la méthode d'extension, comprenons ce qu'est une méthode d'extension dans le contexte d'[ASP.NET](http://ASP.NET) Core.

Une méthode d'extension est une méthode statique qui ajoute une nouvelle fonctionnalité à un type existant sans modifier le type d'origine. Dans [ASP.NET](http://ASP.NET) Core, les méthodes d'extension sont couramment utilisées pour étendre la fonctionnalité de l'interface `IServiceCollection`, qui est utilisée pour enregistrer les services dans le conteneur d'injection de dépendances.

Les services sont des composants qui fournissent des fonctionnalités à une application, telles que l'accès à la base de données, la journalisation et la configuration. En créant une méthode d'extension pour l'interface `IServiceCollection`, vous pouvez simplifier le processus d'enregistrement de vos services dans le conteneur d'injection de dépendances.

Au lieu de tout mettre dans le fichier `Program.cs`, nous allons créer une méthode d'extension pour enregistrer nos services dans le conteneur d'injection de dépendances. Cela nous aidera à garder notre code propre et organisé.

Dans le dossier `Extensions`, créez un nouveau fichier nommé `ServiceExtensions.cs` et ajoutez le code suivant :

```csharp
using System.Reflection;
using bookapi_minimal.AppContext;
using FluentValidation;
using Microsoft.EntityFrameworkCore;

namespace bookapi_minimal.Extensions
{
    public static class ServiceExtensions
    {
        public static void AddApplicationServices(this IHostApplicationBuilder builder)
        {
            if (builder == null) throw new ArgumentNullException(nameof(builder));
            if (builder.Configuration == null) throw new ArgumentNullException(nameof(builder.Configuration));

            // Ajout du contexte de la base de données
            builder.Services.AddDbContext<ApplicationContext>(configure =>
            {
                configure.UseSqlServer(builder.Configuration.GetConnectionString("sqlConnection"));
            });

            // Ajout des validateurs depuis l'assembly actuel
            builder.Services.AddValidatorsFromAssembly(Assembly.GetExecutingAssembly());
        }
    }
}
```

Analysons le code ci-dessus :

* Nous définissons une classe statique nommée `ServiceExtensions` qui contient une méthode d'extension nommée `AddApplicationServices`. Cette méthode étend l'interface `IHostApplicationBuilder`, qui est utilisée pour configurer le pipeline de traitement des requêtes de l'application.
    
* La méthode `AddApplicationServices` accepte une instance de `IHostApplicationBuilder` comme paramètre. Ce paramètre est utilisé pour accéder à la configuration et aux services de l'application.
    
* Nous ajoutons le `ApplicationContext` au conteneur d'injection de dépendances et le configurons pour utiliser SQL Server comme fournisseur de base de données. Nous récupérons la chaîne de connexion à partir du fichier `appsettings.json` en utilisant la méthode `GetConnectionString`.
    
* Nous ajoutons les `validateurs` à partir de l'assembly actuel en utilisant la méthode `AddValidatorsFromAssembly`. Cette méthode analyse l'assembly actuel pour les classes qui implémentent l'interface IValidator et les enregistre dans le conteneur d'injection de dépendances.
    

Ensuite, nous devons ajouter la chaîne de connexion au fichier `appsettings.json`. Ajoutez le code suivant à votre fichier `appsettings.json` :

```json
{ 
     "ConnectionStrings": {
    "sqlConnection": "Server=localhost\\SQLEXPRESS02;Database=BookAPIMinimalAPI;Integrated Security=true;TrustServerCertificate=true;"
  }
  }
```

Assurez-vous de remplacer `your_password` par votre mot de passe SQL Server réel.

Votre fichier `appsettings.json` devrait ressembler à ceci :

```json

{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "ConnectionStrings": {
    "sqlConnection": "Server=localhost\\SQLEXPRESS02;Database=BookAPIMinimalAPI;Integrated Security=true;TrustServerCertificate=true;"
  },
  "AllowedHosts": "*"
}
```

Félicitations ! Vous avez créé avec succès le contexte de la base de données, la méthode d'extension et la chaîne de connexion pour votre application. Dans la section suivante, nous allons créer un contrat.

## Comment créer un contrat

Les contrats sont des objets de transfert de données (DTO) qui définissent la structure des données échangées entre le client et le serveur. Dans notre application, nous allons créer des contrats pour représenter les données envoyées et reçues par nos points de terminaison d'API.

Voici les contrats que nous allons créer :

* CreateBookRequest : Cela représente les données envoyées lors de la création d'un nouveau livre.
    
* UpdateBookRequest : Cela représente les données envoyées lors de la mise à jour d'un livre existant.
    
* BookResponse : Représente les données retournées lors de la récupération d'un livre.
    
* ErrorResponse : Représente la réponse d'erreur retournée lorsqu'une exception se produit.
    
* ApiResponse : Représente la réponse retournée par l'API.
    

Dans le dossier `Contracts`, créez un nouveau fichier nommé `CreateBookRequest` et ajoutez le code suivant :

```csharp
// Contracts/CreateBookRequest.cs

namespace bookapi_minimal.Contracts
{
  
    public record CreateBookRequest
    { 
    
        public string Title { get; init; }
        public string Author { get; init; }
        public string Description { get; init; }
        public string Category { get; init; }
        public string Language { get; init; }
        public int TotalPages { get; init; }
    }
}
```

Dans le dossier `Contracts`, créez un nouveau fichier nommé `UpdateBookRequest` et ajoutez le code suivant :

```csharp

// Contracts/UpdateBookRequest.cs

namespace bookapi_minimal.Contracts
{
   
    public record UpdateBookRequest
    {
       public string Title { get; set; }
        public string Author { get; set; }
        public string Description { get; set; }
        public string Category { get; set; }
        public string Language { get; set; }
        public int TotalPages { get; set; }

    }
}
```

Dans le dossier `Contracts`, créez un nouveau fichier nommé `BookResponse` et ajoutez le code suivant :

```csharp
// Contracts/BookResponse.cs
namespace bookapi_minimal.Contracts
{
  
    public record BookResponse
    {
        public Guid Id { get; set; }
        public string Title { get; set; }
        public string Author { get; set; }
        public string Description { get; set; }
        public string Category { get; set; }
        public string Language { get; set; }
        public int TotalPages { get; set; }
    }
}
```

Dans le dossier `Contracts`, créez un nouveau fichier nommé `ErrorResponse` et ajoutez le code suivant :

```csharp


// Contracts/ErrorResponse.cs
namespace bookapi_minimal.Contracts
{
    
        public record ErrorResponse
    {
        public string Title { get; set; }
        public int StatusCode { get; set; }
        public string Message { get; set; }

    }

}
```

Dans le dossier `Contracts`, créez un nouveau fichier nommé `ApiResponse` et ajoutez le code suivant :

```csharp
// Contracts/ApiResponse.cs
namespace bookapi_minimal.Contracts
{
  
    public class ApiResponse<T>
    {
        public T Data { get; set; }
        public string Message { get; set; }

        public ApiResponse(T data, string message)
        {
            Data = data;
            Message = message;
        }
    }
}
```

Ces contrats nous aident à définir la structure des données échangées entre le client et le serveur, ce qui facilite le travail avec les données dans notre application.

Dans la section suivante, nous allons créer des services pour implémenter la logique métier de notre application.

## Comment ajouter des services

Les services sont des composants qui fournissent des fonctionnalités à une application. Dans notre application, nous allons créer des services pour implémenter la logique métier de notre application. Nous allons créer des services pour gérer les opérations CRUD pour les livres, valider les données des livres et gérer les exceptions.

Dans ASP.NET Core, les services sont enregistrés dans le conteneur d'injection de dépendances et peuvent être injectés dans d'autres composants, tels que les contrôleurs et les points de terminaison. Mais comme il s'agit d'une API minimale, nous allons injecter les services directement dans les points de terminaison.

Créons une interface pour nos services. Dans le dossier `Interfaces`, créez un nouveau fichier nommé `IBookService.cs` et ajoutez le code suivant :

```csharp
 // Interfaces/IBookService.cs



using bookapi_minimal.Contracts;

namespace bookapi_minimal.Interfaces
{
      public interface IBookService
    {
        Task<BookResponse> AddBookAsync(CreateBookRequest createBookRequest);
        Task<BookResponse> GetBookByIdAsync(Guid id);
        Task<IEnumerable<BookResponse>> GetBooksAsync();
        Task<BookResponse> UpdateBookAsync(Guid id,  UpdateBookRequest  updateBookRequest);
        Task<bool> DeleteBookAsync(Guid id);
    }
}
```

Analysons le code ci-dessus : Nous avons défini une interface nommée `IBookService` qui contient des méthodes pour gérer les opérations CRUD pour les livres. L'interface définit les méthodes suivantes :

* `AddBookAsync` : Ajoute un nouveau livre à la base de données.
    
* `GetBookByIdAsync` : Récupère un livre par son ID.
    
* `GetBooksAsync` : Récupère tous les livres de la base de données.
    
* `UpdateBookAsync` : Met à jour un livre existant.
    

Nous utilisons le contrat que nous avons créé précédemment dans le dossier `Contracts`. L'interface `IBookService` définit la structure des méthodes qui seront implémentées par les classes de service. Cela nous aide à séparer l'interface de l'implémentation, ce qui facilite la maintenance et le test de notre code.

Maintenant que nous avons créé l'interface, créons la classe de service qui implémente l'interface.

### Comment implémenter le service de livre

Ce service implémentera l'interface `IBookService` et fournira la logique métier pour notre application. Dans le dossier `Services`, créez un nouveau fichier nommé `BookService.cs`. Votre fichier initial devrait ressembler à ceci :

```csharp

// Services/BookService.cs

namespace bookapi_minimal.Services
{
    public class BookService
    {
        
    }
}
```

La première chose que nous devons faire est d'ajouter l'interface à la classe `BookService`. Mettez à jour la classe `BookService` pour implémenter l'interface `IBookService` comme suit :

```csharp


// Services/BookService.cs



using bookapi_minimal.Interfaces;

namespace bookapi_minimal.Services
{
    public class BookService:IBookService
    {
        
    }
}
```

Lorsque vous faites cela, votre VS Code peut afficher une erreur car nous n'avons pas implémenté les méthodes dans l'interface. Allons-y et implémentons les méthodes dans la classe `BookService`.

Dans VS Code, vous pouvez utiliser le raccourci `Ctrl + .` pour implémenter les méthodes dans l'interface. Vous verrez alors le code suivant généré pour vous :

```csharp

using bookapi_minimal.Contracts;
using bookapi_minimal.Interfaces;

namespace bookapi_minimal.Services
{
     // Classe de service pour gérer les livres
   public class BookService : IBookService
   {
       // Méthode pour ajouter un nouveau livre à la base de données
       public Task<BookResponse> AddBookAsync(CreateBookRequest createBookRequest)
       {
           throw new NotImplementedException();
       }
      
      // Méthode pour supprimer un livre de la base de données
       public Task<bool> DeleteBookAsync(Guid id)
       {
           throw new NotImplementedException();
       }

       // Méthode pour obtenir un livre de la base de données par son ID

       public Task<BookResponse> GetBookByIdAsync(Guid id)
       {
           throw new NotImplementedException();
       }
      
      // Méthode pour obtenir tous les livres de la base de données
       public Task<IEnumerable<BookResponse>> GetBooksAsync()
       {
           throw new NotImplementedException();
       }
       
       // Méthode pour mettre à jour un livre dans la base de données
       public Task<BookResponse> UpdateBookAsync(Guid id, UpdateBookRequest updateBookRequest)
       {
           throw new NotImplementedException();
       }
   }
}
```

Maintenant, vous pouvez voir que les méthodes de l'interface ont été implémentées dans la classe `BookService`. Nous allons implémenter la logique métier pour chaque méthode dans la section suivante.

Avant de faire cela, ajoutons les dépendances nécessaires à la classe `BookService`. Nous devons injecter les dépendances `ApplicationContext` et `ILogger` dans la classe `BookService`. `ApplicationContext` est utilisé pour interagir avec la base de données, tandis que `ILogger` est utilisé pour la journalisation.

Pour injecter les dépendances, mettez à jour la classe `BookService` comme suit :

```csharp

// Services/BookService.cs

// ...
 private readonly ApplicationContext _context; // Contexte de la base de données
  private readonly ILogger<BookService> _logger; // Journal pour enregistrer les informations et les erreurs

//..
```

Puisque nous avons ajouté les dépendances, nous devons mettre à jour le constructeur de `BookService` pour accepter les dépendances. Mettez à jour le constructeur de `BookService` comme suit :

```csharp

// Services/BookService.cs

// ...

  // Constructeur pour initialiser le contexte de la base de données et le journal
 public BookService(ApplicationContext context, ILogger<BookService> logger)
 {
            _context = context;
            _logger = logger;
}

// ...
```

Maintenant que nous avons ajouté les dépendances et mis à jour le constructeur, nous pouvons implémenter la logique métier pour chaque méthode dans la classe `BookService`.

Créons la logique pour les opérations CREATE, READ, UPDATE et DELETE dans la classe `BookService`.

### Comment implémenter la méthode `AddBookAsync`

Comme je l'ai mentionné précédemment, nous utiliserons la méthode `AddBookAsync` pour ajouter un nouveau livre à la base de données. Dans cette méthode, nous allons créer une nouvelle entité de livre, mapper les données de l'objet `CreateBookRequest` à l'entité de livre et enregistrer l'entité de livre dans la base de données. Nous allons également retourner l'entité de livre sous forme d'objet `BookResponse`.

Mettez à jour la méthode `AddBookAsync` dans la classe `BookService` comme suit :

```csharp
// Services/BookService.cs

// ...
 /// <summary>
        /// Ajouter un nouveau livre
        /// </summary>
        /// <param name="createBookRequest">Requête de livre à ajouter</param>
        /// <returns>Détails du livre créé</returns>
        public async Task<BookResponse> AddBookAsync(CreateBookRequest createBookRequest)
        {
            try
            {
                var book = new BookModel
                {
                    Title = createBookRequest.Title,
                    Author = createBookRequest.Author,
                    Description = createBookRequest.Description,
                    Category = createBookRequest.Category,
                    Language = createBookRequest.Language,
                    TotalPages = createBookRequest.TotalPages
                };

                // Ajouter le livre à la base de données
                _context.Books.Add(book);
                await _context.SaveChangesAsync();
                _logger.LogInformation("Livre ajouté avec succès.");

                // Retourner les détails du livre créé
                return new BookResponse
                {
                    Id = book.Id,
                    Title = book.Title,
                    Author = book.Author,
                    Description = book.Description,
                    Category = book.Category,
                    Language = book.Language,
                    TotalPages = book.TotalPages
                };
            }
            catch (Exception ex)
            {
                _logger.LogError($"Erreur lors de l'ajout du livre : {ex.Message}");
                throw;
            }
        }
// ...
```

Dans ce code, nous créons une nouvelle entité de livre à partir de l'objet `CreateBookRequest`, mappons les données de l'objet `CreateBookRequest` à l'entité de livre, enregistrons l'entité de livre dans la base de données et retournons l'entité de livre sous forme d'objet `BookResponse`.

Nous enregistrons également les informations et les erreurs en utilisant la dépendance `ILogger`. Si une exception se produit pendant le processus, nous enregistrons le message d'erreur et relançons l'exception.

Maintenant que nous avons implémenté la méthode `AddBookAsync`, implémentons la méthode `GetBookByIdAsync`.

### Comment implémenter la méthode `GetBookByIdAsync`

La méthode `GetBookByIdAsync` est utilisée pour récupérer un livre par son ID dans la base de données. Dans cette méthode, nous allons interroger la base de données pour le livre avec l'ID spécifié, mapper l'entité de livre à un objet `BookResponse` et retourner l'objet `BookResponse`.

Mettez à jour la méthode `GetBookByIdAsync` dans la classe `BookService` comme suit :

```csharp

// Services/BookService.cs

//... 

    /// <summary>
        /// Obtenir un livre par son ID
        /// </summary>
        /// <param name="id">ID du livre</param>
        /// <returns>Détails du livre</returns>
        public async Task<BookResponse>  GetBookByIdAsync(Guid id)
        {
            try
            {
                // Trouver le livre par son ID
                var book = await _context.Books.FindAsync(id);
                if (book == null)
                {
                    _logger.LogWarning($"Livre avec l'ID {id} non trouvé.");
                    return null;
                }

                // Retourner les détails du livre
                return new BookResponse
                {
                    Id = book.Id,
                    Title = book.Title,
                    Author = book.Author,
                    Description = book.Description,
                    Category = book.Category,
                    Language = book.Language,
                    TotalPages = book.TotalPages
                };
            }
            catch (Exception ex)
            {
                _logger.LogError($"Erreur lors de la récupération du livre : {ex.Message}");
                throw;
            }
        }

//...
```

Dans ce code, nous interrogeons la base de données pour le livre avec l'ID spécifié, mappons l'entité de livre à un objet `BookResponse` et retournons l'objet `BookResponse`. Nous enregistrons également les informations et les erreurs en utilisant la dépendance `ILogger`.

Si le livre avec l'ID spécifié n'est pas trouvé, nous enregistrons un message d'avertissement et retournons null. Si une exception se produit pendant le processus, nous enregistrons le message d'erreur et relançons l'exception.

Maintenant que nous avons implémenté la méthode `GetBookByIdAsync`, implémentons la méthode `GetBooksAsync`.

### Comment implémenter la méthode `GetBooksAsync`

La méthode `GetBooksAsync` est utilisée pour récupérer tous les livres de la base de données. Dans cette méthode, nous allons interroger la base de données pour tous les livres, mapper chaque entité de livre à un objet `BookResponse` et retourner une liste d'objets `BookResponse`.

Mettez à jour la méthode `GetBooksAsync` dans la classe `BookService` comme suit :

```csharp


// Services/BookService.cs

//... 

   
  /// <summary>
        /// Obtenir tous les livres
        /// </summary>
        /// <returns>Liste de tous les livres</returns>
        public async Task<IEnumerable<BookResponse>> GetBooksAsync()
        {
            try
            {
                // Obtenir tous les livres de la base de données
                var books = await _context.Books.ToListAsync();

                // Retourner les détails de tous les livres
                return books.Select(book => new BookResponse
                {
                    Id = book.Id,
                    Title = book.Title,
                    Author = book.Author,
                    Description = book.Description,
                    Category = book.Category,
                    Language = book.Language,
                    TotalPages = book.TotalPages
                });
            }
            catch (Exception ex)
            {
                _logger.LogError($"Erreur lors de la récupération des livres : {ex.Message}");
                throw;
            }
        }
//...
```

Ici, nous interrogeons la base de données pour tous les livres, mappons chaque entité de livre à un objet `BookResponse` et retournons une liste d'objets `BookResponse`. Nous enregistrons également les informations et les erreurs en utilisant la dépendance `ILogger`. Si une exception se produit pendant le processus, nous enregistrons le message d'erreur et relançons l'exception.

Maintenant que nous avons implémenté la méthode `GetBooksAsync`, implémentons la méthode `UpdateBookAsync`.

### Comment implémenter la méthode `UpdateBookAsync`

La méthode `UpdateBookAsync` est utilisée pour mettre à jour un livre existant dans la base de données. Dans cette méthode, nous allons interroger la base de données pour le livre avec l'ID spécifié, mettre à jour l'entité de livre avec les données de l'objet `UpdateBookRequest`, enregistrer l'entité de livre mise à jour dans la base de données et retourner l'entité de livre mise à jour sous forme d'objet `BookResponse`.

Mettez à jour la méthode `UpdateBookAsync` dans la classe `BookService` comme suit :

```csharp
// Services/BookService.cs
 //...
 /// <summary>
        /// Mettre à jour un livre existant
        /// </summary>
        /// <param name="id">ID du livre à mettre à jour</param>
        /// <param name="book">Modèle de livre mis à jour</param>
        /// <returns>Détails du livre mis à jour</returns>
        public async Task<BookResponse> UpdateBookAsync(Guid id, UpdateBookRequest book)
        {
            try
            {
                // Trouver le livre existant par son ID
                var existingBook = await _context.Books.FindAsync(id);
                if (existingBook == null)
                {
                    _logger.LogWarning($"Livre avec l'ID {id} non trouvé.");
                    return null;
                }

                // Mettre à jour les détails du livre
                existingBook.Title = book.Title;
                existingBook.Author = book.Author;
                existingBook.Description = book.Description;
                existingBook.Category = book.Category;
                existingBook.Language = book.Language;
                existingBook.TotalPages = book.TotalPages;

                // Enregistrer les modifications dans la base de données
                await _context.SaveChangesAsync();
                _logger.LogInformation("Livre mis à jour avec succès.");

                // Retourner les détails du livre mis à jour
                return new BookResponse
                {
                    Id = existingBook.Id,
                    Title = existingBook.Title,
                    Author = existingBook.Author,
                    Description = existingBook.Description,
                    Category = existingBook.Category,
                    Language = existingBook.Language,
                    TotalPages = existingBook.TotalPages
                };
            }
            catch (Exception ex)
            {
                _logger.LogError($"Erreur lors de la mise à jour du livre : {ex.Message}");
                throw;
            }
        }
//...
```

Ici, nous interrogeons la base de données pour le livre avec l'ID spécifié, mettons à jour l'entité de livre avec les données de l'objet `UpdateBookRequest`, enregistrons l'entité de livre mise à jour dans la base de données et retournons l'entité de livre mise à jour sous forme d'objet `BookResponse`. Nous enregistrons également les informations et les erreurs en utilisant la dépendance `ILogger`.

Si le livre avec l'ID spécifié n'est pas trouvé, nous enregistrons un message d'avertissement et retournons null. Si une exception se produit pendant le processus, nous enregistrons le message d'erreur et relançons l'exception.

Maintenant que nous avons implémenté la méthode `UpdateBookAsync`, implémentons la méthode `DeleteBookAsync`.

### Comment implémenter la méthode `DeleteBookAsync`

La méthode `DeleteBookAsync` est utilisée pour supprimer un livre existant de la base de données. Dans cette méthode, nous allons interroger la base de données pour le livre avec l'ID spécifié, supprimer l'entité de livre de la base de données et retourner une valeur booléenne indiquant si le livre a été supprimé avec succès.

Mettez à jour la méthode `DeleteBookAsync` dans la classe `BookService` comme suit :

```csharp
// Services/BookService.cs

 //...


/// <summary>
        /// Supprimer un livre par son ID
        /// </summary>
        /// <param name="id">ID du livre à supprimer</param>
        /// <returns>Vrai si le livre a été supprimé, faux sinon</returns>
        public async Task<bool> DeleteBookAsync(Guid id)
        {
            try
            {
                // Trouver le livre par son ID
                var book = await _context.Books.FindAsync(id);
                if (book == null)
                {
                    _logger.LogWarning($"Livre avec l'ID {id} non trouvé.");
                    return false;
                }

                // Supprimer le livre de la base de données
                _context.Books.Remove(book);
                await _context.SaveChangesAsync();
                _logger.LogInformation($"Livre avec l'ID {id} supprimé avec succès.");
                return true;
            }
            catch (Exception ex)
            {
                _logger.LogError($"Erreur lors de la suppression du livre : {ex.Message}");
                throw;
            }
        }
//...
```

Dans ce code, nous interrogeons la base de données pour le livre avec l'ID spécifié, supprimons l'entité de livre de la base de données et retournons une valeur booléenne indiquant si le livre a été supprimé avec succès. Nous enregistrons également les informations et les erreurs en utilisant la dépendance `ILogger`.

Si le livre avec l'ID spécifié n'est pas trouvé, nous enregistrons un message d'avertissement et retournons false. Si une exception se produit pendant le processus, nous enregistrons le message d'erreur et relançons l'exception.

Maintenant, vous avez implémenté avec succès la logique métier pour les méthodes `AddBookAsync`, `GetBookByIdAsync`, `GetBooksAsync`, `UpdateBookAsync` et `DeleteBookAsync` dans la classe `BookService`. Ces méthodes gèrent les opérations CRUD pour les livres, valident les données des livres et gèrent les exceptions. À ce stade, votre classe `BookService` devrait ressembler à ceci :

```csharp


using bookapi_minimal.AppContext;
using bookapi_minimal.Contracts;
using bookapi_minimal.Interfaces;
using bookapi_minimal.Models;
using Microsoft.EntityFrameworkCore;

namespace bookapi_minimal.Services
{
    public class BookService : IBookService
    {
          private readonly ApplicationContext _context; // Contexte de la base de données
        private readonly ILogger<BookService> _logger; // Journal pour enregistrer les informations et les erreurs
          // Constructeur pour initialiser le contexte de la base de données et le journal
        public BookService(ApplicationContext context, ILogger<BookService> logger)
        {
            _context = context;
            _logger = logger;
        }
        
           /// Ajouter un nouveau livre
        /// </summary>
        /// <param name="createBookRequest">Requête de livre à ajouter</param>
        /// <returns>Détails du livre créé</returns>
        public async Task<BookResponse> AddBookAsync(CreateBookRequest createBookRequest)
        {
            try
            {
                var book = new BookModel
                {
                    Title = createBookRequest.Title,
                    Author = createBookRequest.Author,
                    Description = createBookRequest.Description,
                    Category = createBookRequest.Category,
                    Language = createBookRequest.Language,
                    TotalPages = createBookRequest.TotalPages
                };

                // Ajouter le livre à la base de données
                _context.Books.Add(book);
                await _context.SaveChangesAsync();
                _logger.LogInformation("Livre ajouté avec succès.");

                // Retourner les détails du livre créé
                return new BookResponse
                {
                    Id = book.Id,
                    Title = book.Title,
                    Author = book.Author,
                    Description = book.Description,
                    Category = book.Category,
                    Language = book.Language,
                    TotalPages = book.TotalPages
                };
            }
            catch (Exception ex)
            {
                _logger.LogError($"Erreur lors de l'ajout du livre : {ex.Message}");
                throw;
            }
        }

          /// <summary>
        /// Obtenir un livre par son ID
        /// </summary>
        /// <param name="id">ID du livre</param>
        /// <returns>Détails du livre</returns>
        public async Task<BookResponse>  GetBookByIdAsync(Guid id)
        {
            try
            {
                // Trouver le livre par son ID
                var book = await _context.Books.FindAsync(id);
                if (book == null)
                {
                    _logger.LogWarning($"Livre avec l'ID {id} non trouvé.");
                    return null;
                }

                // Retourner les détails du livre
                return new BookResponse
                {
                    Id = book.Id,
                    Title = book.Title,
                    Author = book.Author,
                    Description = book.Description,
                    Category = book.Category,
                    Language = book.Language,
                    TotalPages = book.TotalPages
                };
            }
            catch (Exception ex)
            {
                _logger.LogError($"Erreur lors de la récupération du livre : {ex.Message}");
                throw;
            }
        }

      
         
  /// <summary>
        /// Obtenir tous les livres
        /// </summary>
        /// <returns>Liste de tous les livres</returns>
        public async Task<IEnumerable<BookResponse>> GetBooksAsync()
        {
            try
            {
                // Obtenir tous les livres de la base de données
                var books = await _context.Books.ToListAsync();

                // Retourner les détails de tous les livres
                return books.Select(book => new BookResponse
                {
                    Id = book.Id,
                    Title = book.Title,
                    Author = book.Author,
                    Description = book.Description,
                    Category = book.Category,
                    Language = book.Language,
                    TotalPages = book.TotalPages
                });
            }
            catch (Exception ex)
            {
                _logger.LogError($"Erreur lors de la récupération des livres : {ex.Message}");
                throw;
            }
        }
      

         /// <summary>
        /// Mettre à jour un livre existant
        /// </summary>
        /// <param name="id">ID du livre à mettre à jour</param>
        /// <param name="book">Modèle de livre mis à jour</param>
        /// <returns>Détails du livre mis à jour</returns>
        public async Task<BookResponse> UpdateBookAsync(Guid id, UpdateBookRequest book)
        {
            try
            {
                // Trouver le livre existant par son ID
                var existingBook = await _context.Books.FindAsync(id);
                if (existingBook == null)
                {
                    _logger.LogWarning($"Livre avec l'ID {id} non trouvé.");
                    return null;
                }

                // Mettre à jour les détails du livre
                existingBook.Title = book.Title;
                existingBook.Author = book.Author;
                existingBook.Description = book.Description;
                existingBook.Category = book.Category;
                existingBook.Language = book.Language;
                existingBook.TotalPages = book.TotalPages;

                // Enregistrer les modifications dans la base de données
                await _context.SaveChangesAsync();
                _logger.LogInformation("Livre mis à jour avec succès.");

                // Retourner les détails du livre mis à jour
                return new BookResponse
                {
                    Id = existingBook.Id,
                    Title = existingBook.Title,
                    Author = existingBook.Author,
                    Description = existingBook.Description,
                    Category = existingBook.Category,
                    Language = existingBook.Language,
                    TotalPages = existingBook.TotalPages
                };
            }
            catch (Exception ex)
            {
                _logger.LogError($"Erreur lors de la mise à jour du livre : {ex.Message}");
                throw;
            }
        }

    

        /// <summary>
        /// Supprimer un livre par son ID
        /// </summary>
        /// <param name="id">ID du livre à supprimer</param>
        /// <returns>Vrai si le livre a été supprimé, faux sinon</returns>
        public async Task<bool> DeleteBookAsync(Guid id)
        {
            try
            {
                // Trouver le livre par son ID
                var book = await _context.Books.FindAsync(id);
                if (book == null)
                {
                    _logger.LogWarning($"Livre avec l'ID {id} non trouvé.");
                    return false;
                }

                // Supprimer le livre de la base de données
                _context.Books.Remove(book);
                await _context.SaveChangesAsync();
                _logger.LogInformation($"Livre avec l'ID {id} supprimé avec succès.");
                return true;
            }
            catch (Exception ex)
            {
                _logger.LogError($"Erreur lors de la suppression du livre : {ex.Message}");
                throw;
            }
        }

    }
}
```

Félicitations ! Vous avez implémenté avec succès la logique métier pour les méthodes `AddBookAsync`, `GetBookByIdAsync`, `GetBooksAsync`, `UpdateBookAsync` et `DeleteBookAsync` dans la classe `BookService`.

Il y a une chose que nous devons faire : nous devons enregistrer le service dans notre méthode d'extension. Allons-y et faisons cela.

Dans votre fichier `ServiceExtensions.cs`, ajoutez le code suivant :

```csharp

// Extensions/ServiceExtensions.cs

//..

 builder.Services.AddScoped<IBookService, BookService>();
//...
```

Cela enregistrera la classe `BookService` en tant que service scopé. Cela signifie que le service sera créé une fois par requête et supprimé après que la requête soit terminée.

Maintenant que nous avons le service qui fonctionne, allons-y et créons les classes d'exception.

## Comment créer des exceptions

Gérer correctement les exceptions est crucial pour garantir la stabilité et la fiabilité d'une application. Dans le contexte d'ASP.NET Core, il existe deux principaux types d'exceptions :

* **Exceptions système** : Ce sont des exceptions lancées par le runtime .NET ou le système sous-jacent.
    
* **Exceptions d'application** : Ce sont des exceptions lancées par le code de l'application pour gérer des erreurs ou des conditions spécifiques.
    

Dans ASP.NET Core avec .NET 8, une nouvelle fonctionnalité appelée gestion globale des exceptions a été introduite. Cette fonctionnalité vous permet de gérer les exceptions globalement dans votre application, ce qui facilite la gestion des erreurs et offre une expérience utilisateur cohérente.

Dans notre application, nous allons créer des classes d'exception personnalisées pour gérer des erreurs et des conditions spécifiques. Nous allons également tirer parti de la fonctionnalité de gestion globale des exceptions pour gérer les exceptions globalement, garantissant une approche uniforme de la gestion des erreurs dans toute l'application.

Nous allons créer les classes d'exception suivantes :

* `NoBookFoundException` : Levée lorsqu'aucun livre avec l'ID spécifié n'est trouvé.
    
* `BookDoesNotExistException` : Levée lorsqu'un livre avec l'ID spécifié n'existe pas.
    
* `GlobalExceptionHandler` : Gère les exceptions globalement dans l'application.
    

Dans le dossier `Exceptions`, créez un nouveau fichier nommé `NoBookFoundException.cs` et ajoutez le code suivant :

```csharp

// Exceptions/NoBookFoundException.cs

namespace bookapi_minimal.Exceptions
{
    
    public class NoBookFoundException : Exception
    {
        
        public NoBookFoundException() : base("Aucun livre trouvé")
        {}
    }
}
```

Dans ce code, nous créons une classe d'exception personnalisée nommée `NoBookFoundException` qui hérite de la classe `Exception`. La classe `NoBookFoundException` est utilisée pour gérer le scénario où aucun livre n'est trouvé dans la base de données. Nous fournissons également un message d'erreur personnalisé pour l'exception.

Dans le dossier `Exceptions`, créez un nouveau fichier nommé `BookDoesNotExistException.cs` et ajoutez le code suivant :

```csharp
namespace bookapi_minimal.Exceptions
{
     public class BookDoesNotExistException : Exception
    {
        private int id { get; set; }

        public BookDoesNotExistException(int id) : base($"Le livre avec l'ID {id} n'existe pas")
        {
            this.id = id;
        } 
        
    }
}
```

Dans ce code, nous créons une classe d'exception personnalisée nommée `BookDoesNotExistException` qui hérite de la classe `Exception`. La classe `BookDoesNotExistException` est utilisée pour gérer le scénario où un livre avec l'ID spécifié n'existe pas dans la base de données. Nous fournissons également un message d'erreur personnalisé pour l'exception.

Dans le dossier `Exceptions`, créez un nouveau fichier nommé `GlobalExceptionHandler.cs` et ajoutez le code suivant :

```csharp
// Exceptions/GlobalExceptionHandler.cs

using System.Net;
using bookapi_minimal.Contracts;
using Microsoft.AspNetCore.Diagnostics;

namespace bookapi_minimal.Exceptions
{
 
   // Classe de gestionnaire d'exceptions global implémentant IExceptionHandler
    public class GlobalExceptionHandler : IExceptionHandler
    {
        private readonly ILogger<GlobalExceptionHandler> _logger;

        // Constructeur pour initialiser le journal
        public GlobalExceptionHandler(ILogger<GlobalExceptionHandler> logger)
        {
            _logger = logger;
        }

        // Méthode pour gérer les exceptions de manière asynchrone
        public async ValueTask<bool> TryHandleAsync(
            HttpContext httpContext,
            Exception exception,
            CancellationToken cancellationToken)
        {
            // Journaliser les détails de l'exception
            _logger.LogError(exception, "Une erreur s'est produite lors du traitement de votre requête");

            var errorResponse = new ErrorResponse
            {
                Message = exception.Message,
                Title = exception.GetType().Name
            };

            // Déterminer le code de statut en fonction du type d'exception
            switch (exception)
            {
                case BadHttpRequestException:
                    errorResponse.StatusCode = (int)HttpStatusCode.BadRequest;
                    break;

                case NoBookFoundException:
                case BookDoesNotExistException:
                    errorResponse.StatusCode = (int)HttpStatusCode.NotFound;
                    break;

                default:
                    errorResponse.StatusCode = (int)HttpStatusCode.InternalServerError;
                    break;
            }

            // Définir le code de statut de la réponse
            httpContext.Response.StatusCode = errorResponse.StatusCode;

            // Écrire la réponse d'erreur au format JSON
            await httpContext.Response.WriteAsJsonAsync(errorResponse, cancellationToken);

            // Retourner vrai pour indiquer que l'exception a été gérée
            return true;
        }
    }
}
```

Analysons le code ci-dessus :

* Nous définissons une classe nommée `GlobalExceptionHandler` qui implémente l'interface `IExceptionHandler`. L'interface `IExceptionHandler` est utilisée pour gérer les exceptions globalement dans l'application.
    
* La classe `GlobalExceptionHandler` contient un constructeur qui initialise la dépendance `ILogger<GlobalExceptionHandler>`. Le `ILogger` est utilisé pour journaliser les informations et les erreurs.
    
* La méthode `TryHandleAsync` est utilisée pour gérer les exceptions de manière asynchrone. Cette méthode accepte les paramètres `HttpContext`, `Exception` et `CancellationToken`.
    
* Nous journalisons les détails de l'exception en utilisant la dépendance `ILogger`.
    
* Nous créons un objet `ErrorResponse` pour représenter la réponse d'erreur retournée par l'API. L'objet `ErrorResponse` contient le message d'erreur, le titre et le code de statut.
    
* Nous déterminons le code de statut en fonction du type d'exception. Si l'exception est une `BadHttpRequestException`, nous définissons le code de statut sur `BadRequest`. Si l'exception est une `NoBookFoundException` ou `BookDoesNotExistException`, nous définissons le code de statut sur `NotFound`. Sinon, nous définissons le code de statut sur `InternalServerError`.
    
* Nous définissons le code de statut de la réponse en utilisant la propriété `httpContext.Response.StatusCode`.
    
* Nous écrivons la réponse d'erreur au format JSON en utilisant la méthode `httpContext.Response.WriteAsJsonAsync`.
    
* Nous retournons `true` pour indiquer que l'exception a été gérée avec succès.
    

Maintenant que nous avons créé les classes d'exception, enregistrons le `GlobalExceptionHandler` dans le conteneur d'injection de dépendances. Puisque nous avons créé une méthode d'extension pour enregistrer les services dans le conteneur d'injection de dépendances, nous allons ajouter le `GlobalExceptionHandler` à la classe `ServiceExtensions`.

Mettez à jour la classe `ServiceExtensions` dans le dossier `Extensions` comme suit :

```csharp

// Extensions/ServiceExtensions.cs
//...
builder.Services.AddExceptionHandler<GlobalExceptionHandler>();

builder.Services.AddProblemDetails();

//...
```

La méthode `AddExceptionHandler` enregistre le `GlobalExceptionHandler` dans le conteneur d'injection de dépendances. La méthode `AddProblemDetails` enregistre la classe `ProblemDetails` dans le conteneur d'injection de dépendances.

Maintenant que nous avons enregistré le `GlobalExceptionHandler` dans le conteneur d'injection de dépendances, nous pouvons l'utiliser pour gérer les exceptions globalement dans notre application. Dans la section suivante, nous allons créer les points de terminaison de l'API pour interagir avec les données des livres.

## Comment créer les points de terminaison de l'API

Dans le contexte des API minimales dans ASP.NET Core, il existe de nombreuses façons de configurer vos points de terminaison.

Vous pouvez les définir directement dans votre fichier `Program.cs`. Mais à mesure que votre projet grandit et que vous devez ajouter plus de points de terminaison ou de fonctionnalités, il est utile d'organiser votre code de manière plus efficace. Une façon d'y parvenir est de créer une classe séparée pour gérer tous les points de terminaison.

Comme nous l'avons discuté précédemment, les API minimales n'utilisent pas de contrôleurs ou de vues comme les applications ASP.NET Core traditionnelles. Au lieu de cela, elles utilisent des méthodes telles que `MapGet`, `MapPost`, `MapPut` et `MapDelete` pour définir les méthodes HTTP et les routes pour les points de terminaison de l'API.

Pour commencer, accédez au dossier `Endpoints` et créez un nouveau fichier nommé `BookEndpoints.cs`. Ajoutez le code suivant au fichier :

```csharp

// Endpoints/BookEndpoints.cs



namespace bookapi_minimal.Endpoints
{
     public static class BookEndPoint
    {
        public static IEndpointRouteBuilder MapBookEndPoint(this IEndpointRouteBuilder app)
        {
           

            return app;
        }
    }
}
```

La classe `BookEndpoints` contient une méthode `MapBookEndPoint` qui retourne un objet `IEndpointRouteBuilder`. L'objet `IEndpointRouteBuilder` est utilisé pour définir les méthodes HTTP et les routes pour les points de terminaison de l'API. Dans les sections suivantes, nous définirons les points de terminaison de l'API pour la `création`, la `lecture`, la `mise à jour` et la `suppression` de livres.

### Comment créer le point de terminaison `AddBookAsync`

Dans cette section, nous allons créer le point de terminaison `AddBookAsync`. Ce point de terminaison acceptera un objet `Book` comme charge utile JSON et l'ajoutera à la base de données. Nous utiliserons la méthode `MapPost` pour définir la méthode HTTP et la route pour ce point de terminaison.

Ajoutez le code suivant à la classe `BookEndpoints` :

```csharp

// Endpoints/BookEndpoints.cs


//...
   // Point de terminaison pour ajouter un nouveau livre
      app.MapPost("/books", async (CreateBookRequest createBookRequest, IBookService bookService) =>
        {
        var result = await bookService.AddBookAsync(createBookRequest);
        return Results.Created($"/books/{result.Id}", result); 
        });


//...
```

* **Définition de la route** : La méthode MapPost définit la route pour le point de terminaison comme `/books`.
    
* **Modèle de requête** : Le point de terminaison accepte un objet `CreateBookRequest` comme charge utile JSON. L'objet `CreateBookRequest` contient les données nécessaires pour créer un nouveau livre.
    
* **Modèle de réponse** : Le point de terminaison retourne un objet `Book` comme charge utile JSON. L'objet `Book` contient les données pour le livre nouvellement créé.
    
* **Valeur de retour** : Le point de terminaison retourne un résultat `Created`. Le résultat `Created` contient l'emplacement du livre nouvellement créé et l'objet `Book`.
    

### Comment créer le point de terminaison `GetBookAsync`

Dans cette section, nous allons créer le point de terminaison `GetBookAsync`. Ce point de terminaison acceptera un ID de livre comme paramètre de requête et retournera le livre avec l'ID spécifié. Nous utiliserons la méthode `MapGet` pour définir la méthode HTTP et la route pour ce point de terminaison.

Ajoutez le code suivant à la classe `BookEndpoints` :

```csharp

// Endpoints/BookEndpoints.cs

// ...
    // Point de terminaison pour obtenir tous les livres
    app.MapGet("/books", async (IBookService bookService) =>
     {
    var result = await bookService.GetBooksAsync();
    return Results.Ok(result);
});


//...
```

* **Définition de la route** : La méthode MapGet définit la route pour le point de terminaison comme `/books`.
    
* **Modèle de requête** : Le point de terminaison accepte un objet `Book` comme charge utile JSON. L'objet `Book` contient les données nécessaires pour créer un nouveau livre.
    
* **Modèle de réponse** : Le point de terminaison retourne un objet `Book` comme charge utile JSON. L'objet `Book` contient les données pour le livre nouvellement créé.
    
* **Valeur de retour** : Le point de terminaison retourne un résultat `Ok`. Le résultat `Ok` contient l'objet `Book`.
    

### Comment créer le point de terminaison `GetBookByIdAsync`

Dans cette section, nous allons créer le point de terminaison `GetBookByIdAsync`. Ce point de terminaison acceptera un ID de livre comme paramètre de route et retournera le livre avec l'ID spécifié. Nous utiliserons la méthode `MapGet` pour définir la méthode HTTP et la route pour ce point de terminaison.

Ajoutez le code suivant à la classe `BookEndpoints` :

```csharp

// Endpoints/BookEndpoints.cs
//...
// Point de terminaison pour obtenir un livre par ID

  app.MapGet("/books/{id:guid}", async (Guid id, IBookService bookService) =>
  {
    var result = await bookService.GetBookByIdAsync(id);
    return result != null ? Results.Ok(result) : Results.NotFound();
});

//...
```

* **Définition de la route** : La méthode MapGet définit la route pour le point de terminaison comme `/books/{id:guid}`. Le paramètre `{id:guid}` spécifie que le paramètre `id` doit être un GUID.
    
* **Modèle de requête** : Le point de terminaison accepte un objet `Book` comme charge utile JSON. L'objet `Book` contient les données nécessaires pour créer un nouveau livre.
    
* **Modèle de réponse** : Le point de terminaison retourne un objet `Book` comme charge utile JSON. L'objet `Book` contient les données pour le livre nouvellement créé.
    
* **Valeur de retour** : Le point de terminaison retourne un résultat `Ok` si le livre est trouvé. Le résultat `NotFound` est retourné si le livre n'est pas trouvé.
    

### Comment créer le point de terminaison `UpdateBookAsync`

Dans cette section, nous allons créer le point de terminaison `UpdateBookAsync`. Ce point de terminaison acceptera un ID de livre comme paramètre de route et un objet `Book` comme charge utile JSON et mettra à jour le livre avec l'ID spécifié. Nous utiliserons la méthode `MapPut` pour définir la méthode HTTP et la route pour ce point de terminaison.

Ajoutez le code suivant à la classe `BookEndpoints` :

```csharp

// Endpoints/BookEndpoints.cs

//...
   // Point de terminaison pour mettre à jour un livre par ID
    app.MapPut("/books/{id:guid}", async (Guid id, UpdateBookRequest updateBookRequest, IBookService bookService) =>
 {
var result = await bookService.UpdateBookAsync(id, updateBookRequest);
return result != null ? Results.Ok(result) : Results.NotFound();
});

//...
```

* **Définition de la route** : La méthode MapPut définit la route pour le point de terminaison comme `/books/{id:guid}`. Le paramètre `{id:guid}` spécifie que le paramètre `id` doit être un GUID.
    
* **Modèle de requête** : Le point de terminaison accepte un objet `Book` comme charge utile JSON. L'objet `Book` contient les données nécessaires pour créer un nouveau livre.
    
* **Modèle de réponse** : Le point de terminaison retourne un objet `Book` comme charge utile JSON. L'objet `Book` contient les données pour le livre nouvellement créé.
    
* **Valeur de retour** : Le point de terminaison retourne un résultat `Ok` si le livre est trouvé. Le résultat `NotFound` est retourné si le livre n'est pas trouvé.
    

### Comment créer le point de terminaison `DeleteBookAsync`

Dans cette section, nous allons créer le point de terminaison `DeleteBookAsync`. Ce point de terminaison acceptera un ID de livre comme paramètre de route et supprimera le livre avec l'ID spécifié. Nous utiliserons la méthode `MapDelete` pour définir la méthode HTTP et la route pour ce point de terminaison.

Ajoutez le code suivant à la classe `BookEndpoints` :

```csharp

// Endpoints/BookEndpoints.cs

//...
   // Point de terminaison pour supprimer un livre par ID
 app.MapDelete("/books/{id:guid}", async (Guid id, IBookService bookService) =>
{
var result = await bookService.DeleteBookAsync(id);
   return result ? Results.NoContent() : Results.NotFound();
});


//...
```

* **Définition de la route** : La méthode MapDelete définit la route pour le point de terminaison comme `/books/{id:guid}`. Le paramètre `{id:guid}` spécifie que le paramètre `id` doit être un GUID.
    
* **Modèle de requête** : Le point de terminaison accepte un objet `Book` comme charge utile JSON. L'objet `Book` contient les données nécessaires pour créer un nouveau livre.
    
* **Modèle de réponse** : Le point de terminaison retourne un objet `Book` comme charge utile JSON. L'objet `Book` contient les données pour le livre nouvellement créé.
    
* **Valeur de retour** : Le point de terminaison retourne un résultat `NoContent` si le livre est supprimé avec succès. Le résultat `NotFound` est retourné si le livre n'est pas trouvé.
    

Maintenant, nous avons défini toutes les méthodes pour les points de terminaison des livres. Votre classe de point de terminaison devrait ressembler à ceci :

```csharp
// Endpoints/BookEndpoints.cs
using bookapi_minimal.Contracts;
using bookapi_minimal.Interfaces;

namespace bookapi_minimal.Endpoints
{
     public static class BookEndPoint
    {
        public static IEndpointRouteBuilder MapBookEndPoint(this IEndpointRouteBuilder app)
        {
            // Définir les points de terminaison

            // Point de terminaison pour ajouter un nouveau livre
            app.MapPost("/books", async (CreateBookRequest createBookRequest, IBookService bookService) =>
            {
                var result = await bookService.AddBookAsync(createBookRequest);
                return Results.Created($"/books/{result.Id}", result); 
            });
           

               // Point de terminaison pour obtenir tous les livres
            app.MapGet("/books", async (IBookService bookService) =>
            {
                var result = await bookService.GetBooksAsync();
                return Results.Ok(result);
            });

            // Point de terminaison pour obtenir un livre par ID
            app.MapGet("/books/{id:guid}", async (Guid id, IBookService bookService) =>
            {
                var result = await bookService.GetBookByIdAsync(id);
                return result != null ? Results.Ok(result) : Results.NotFound();
            });

        
            // Point de terminaison pour mettre à jour un livre par ID
            app.MapPut("/books/{id:guid}", async (Guid id, UpdateBookRequest updateBookRequest, IBookService bookService) =>
            {
                var result = await bookService.UpdateBookAsync(id, updateBookRequest);
                return result != null ? Results.Ok(result) : Results.NotFound();
            });

            // Point de terminaison pour supprimer un livre par ID
            app.MapDelete("/books/{id:guid}", async (Guid id, IBookService bookService) =>
            {
                var result = await bookService.DeleteBookAsync(id);
                return result ? Results.NoContent() : Results.NotFound();
            });

            return app;
        }
    }
}
```

Félicitations ! Vous avez créé tous les points de terminaison pour l'API de livres. Les points de terminaison gèrent les opérations CRUD pour les livres et retournent les réponses appropriées en fonction de la requête et des données.

### Comment enregistrer les points de terminaison

Après avoir défini les points de terminaison de l'API pour l'API de livres, l'étape suivante consiste à enregistrer ces points de terminaison dans le fichier `Program.cs`. Nous utiliserons la méthode `MapBookEndpoints` pour enregistrer les points de terminaison des livres.

Nous devons également nettoyer notre classe `Program.cs` pour nous assurer qu'elle reste organisée et maintenable.

```csharp
// Program.cs

using System.Reflection;
using bookapi_minimal.Endpoints;
using bookapi_minimal.Services;
using Microsoft.OpenApi.Models;

var builder = WebApplication.CreateBuilder(args);


builder.AddApplicationServices();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(c=>
{
    c.SwaggerDoc("v1", new OpenApiInfo { Title = "API minimale", Version = "v1", Description = "Montrant comment vous pouvez construire une API minimale " +
        "avec .net" });


    // Définir le chemin des commentaires pour le JSON et l'UI Swagger.
    var xmlFile = $"{Assembly.GetExecutingAssembly().GetName().Name}.xml";
    var xmlPath = Path.Combine(AppContext.BaseDirectory, xmlFile);
    c.IncludeXmlComments(xmlPath);

});
var app = builder.Build();

// Configurer le pipeline de requêtes HTTP.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.UseExceptionHandler();


app.MapGroup("/api/v1/")
   .WithTags("Points de terminaison des livres")
   .MapBookEndPoint();

app.Run();
```

Analysons les composants clés du fichier `Program.cs` :

* **AddApplicationServices** : Cette méthode enregistre les services nécessaires pour l'API. Il s'agit d'une méthode d'extension que nous avons créée précédemment pour ajouter des services au conteneur d'injection de dépendances.
    
* **AddSwaggerGen** : Cette méthode enregistre le générateur Swagger, qui est utilisé pour créer la documentation Swagger pour l'API. Nous spécifions le titre, la version et la description de l'API dans le document Swagger.
    
* **MapGroup** : Cette méthode regroupe les points de terminaison. Elle prend un chemin comme paramètre et retourne un objet `IEndpointRouteBuilder`. Nous utilisons la méthode `WithTags` pour ajouter des tags aux points de terminaison et la méthode `MapBookEndpoints` pour enregistrer les points de terminaison des livres.
    
* **Run** : Cette méthode démarre l'application.
    

Pour activer la documentation Swagger, vous devez ajouter la propriété `GenerateDocumentationFile` à votre fichier `.csproj`. Dans cet exemple, le fichier est nommé `bookapi-minimal.csproj`, mais le nom peut varier en fonction de votre projet.

Ajoutez la ligne suivante à votre fichier `.csproj` :

```xml
<PropertyGroup>
  <GenerateDocumentationFile>true</GenerateDocumentationFile>
</PropertyGroup>
```

À la fin, bookapi-minimal.csproj devrait ressembler à ceci :

```xml

<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
     <GenerateDocumentationFile>true</GenerateDocumentationFile>
    <RootNamespace>bookapi_minimal</RootNamespace>
  </PropertyGroup>

  <ItemGroup>
   <PackageReference Include="FluentValidation.DependencyInjectionExtensions" Version="11.9.2" />
    <PackageReference Include="Microsoft.AspNetCore.OpenApi" Version="8.0.6" />
    <PackageReference Include="Microsoft.EntityFrameworkCore" Version="8.0.8" />
    <PackageReference Include="Microsoft.EntityFrameworkCore.Design" Version="8.0.8">
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
      <PrivateAssets>all</PrivateAssets>
    </PackageReference>
    <PackageReference Include="Microsoft.EntityFrameworkCore.SqlServer" Version="8.0.8" />
    <PackageReference Include="Microsoft.EntityFrameworkCore.Tools" Version="8.0.8">
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
      <PrivateAssets>all</PrivateAssets>
    </PackageReference>
    <PackageReference Include="Swashbuckle.AspNetCore" Version="6.4.0" />
  </ItemGroup>

</Project>
```

Maintenant que nous avons enregistré les points de terminaison des livres dans le fichier `Program.cs`, nous pouvons exécuter l'application et tester les points de terminaison de l'API en utilisant Swagger.

Lorsque vous exécutez l'application, vous devriez voir la documentation Swagger à l'URL suivante : [`https://localhost:5001/swagger/index.html`](https://localhost:5001/swagger/index.html). La documentation Swagger fournit des informations sur les points de terminaison de l'API, les modèles de requête et de réponse, et vous permet de tester les points de terminaison directement depuis le navigateur. Vous devriez voir quelque chose comme ceci :

![Points de terminaison de l'API de livres Swagger UI](https://cdn.hashnode.com/res/hashnode/image/upload/v1732624213627/e1e3b3d1-2ecb-486a-b95b-28b958f52462.png align="left")

Félicitations ! Vous avez implémenté la logique métier pour le service de livres, créé des exceptions personnalisées, défini des points de terminaison d'API et enregistré les points de terminaison dans le fichier `Program.cs`. Vous avez également activé la documentation Swagger pour tester les points de terminaison de l'API.

## Comment ajouter des données de départ à la base de données

Une étape importante supplémentaire consiste à ensemencer la base de données avec des données initiales lorsque l'application démarre. Ces données de départ peupleront la base de données, vous permettant de tester vos points de terminaison d'API sans ajouter manuellement des données.

Ajoutons quelques données de départ avant d'effectuer des migrations et de tester nos points de terminaison d'API.

Pour ce faire, nous allons créer une nouvelle classe dans notre dossier Configuration appelée `BookTypeConfigurations` et ajouter le code suivant :

```csharp


using bookapi_minimal.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;

namespace bookapi_minimal.Configurations
{
    public class BookTypeConfigurations : IEntityTypeConfiguration<BookModel>
    {
        public void Configure(EntityTypeBuilder<BookModel> builder)
        {
            // Configurer le nom de la table
            builder.ToTable("Books");

            // Configurer la clé primaire
            builder.HasKey(x => x.Id);

            // Configurer les propriétés
            builder.Property(x => x.Id).ValueGeneratedOnAdd();
            builder.Property(x => x.Title).IsRequired().HasMaxLength(100);
            builder.Property(x => x.Author).IsRequired().HasMaxLength(100);
            builder.Property(x => x.Description).IsRequired().HasMaxLength(500);
            builder.Property(x => x.Category).IsRequired().HasMaxLength(100);
            builder.Property(x => x.Language).IsRequired().HasMaxLength(50);
            builder.Property(x => x.TotalPages).IsRequired();

            // Données de départ
            builder.HasData(
                new BookModel
                {
                    Id = Guid.NewGuid(),
                    Title = "L'Alchimiste",
                    Author = "Paulo Coelho",
                    Description = "L'Alchimiste suit le voyage d'un berger andalou",
                    Category = "Fiction",
                    Language = "Français",
                    TotalPages = 208
                },
                new BookModel
                {
                    Id = Guid.NewGuid(),
                    Title = "To Kill a Mockingbird",
                    Author = "Harper Lee",
                    Description = "Un roman sur les problèmes sérieux de viol et d'inégalité raciale.",
                    Category = "Fiction",
                    Language = "Anglais",
                    TotalPages = 281
                },
                new BookModel
                {
                    Id = Guid.NewGuid(),
                    Title = "1984",
                    Author = "George Orwell",
                    Description = "Un roman de science-fiction sociale dystopique et un conte moral sur les dangers du totalitarisme.",
                  Category = "Fiction",
                  Language = "Anglais",
                  TotalPages = 328
                } 
            );
        }
    }
}
```

Analysons le code ci-dessus :

Dans Entity Framework Core, vous pouvez utiliser l'interface `IEntityTypeConfiguration` pour configurer le type d'entité et les données de départ pour la base de données. La classe `BookTypeConfigurations` implémente l'interface `IEntityTypeConfiguration<BookModel>` et fournit la configuration pour l'entité `BookModel`.

* **Méthode Configure** : Cette méthode est utilisée pour configurer le type d'entité `BookModel`. Elle définit le nom de la table, la clé primaire et les propriétés pour l'entité `BookModel`.
    
    * **Nom de la table** : La méthode `ToTable` spécifie le nom de la table à créer dans la base de données. Dans ce cas, le nom de la table est défini sur "Books".
        
    * **Clé primaire** : La méthode `HasKey` spécifie la clé primaire pour l'entité `BookModel`. La clé primaire est définie sur la propriété `Id`.
        
    * **Propriétés** : La méthode `Property` configure les propriétés de l'entité `BookModel`. Elle spécifie le type de données, la longueur et les contraintes pour chaque propriété.
        
* **Données de départ** : La méthode `HasData` ensemence la base de données avec des données initiales. Elle crée trois objets `BookModel` avec des données d'exemple pour tester les points de terminaison de l'API.
    

Maintenant que nous avons créé la classe `BookTypeConfigurations`, nous devons enregistrer cette configuration dans la classe `ApplicationContext`. Cela garantit que la configuration est appliquée lorsque la base de données est créée ou migrée.

Nous sommes enfin presque prêts à tester notre API. Mais avant de le faire, nous devons effectuer des migrations pour créer la base de données et appliquer les données de départ.

Rappelons que nous avons ajouté notre chaîne de connexion de base de données dans le fichier `appsettings.json` ? Maintenant, effectuons une migration et mettons à jour notre base de données pour que la migration prenne effet.

## Comment effectuer une migration

Les migrations vous permettent de mettre à jour le schéma de la base de données en fonction des modifications apportées à vos classes de modèle. Dans Entity Framework Core, vous pouvez utiliser la commande `dotnet ef migrations add` pour créer une nouvelle migration reflétant ces modifications.

Pour effectuer une migration, exécutez la commande suivante dans le terminal :

```bash
dotnet ef migrations add InitialCreate
```

Si la commande est réussie, vous devriez voir une sortie similaire à ceci :

```bash
Build started...
Build succeeded.
Done. To undo this action, use 'ef migrations remove'
```

Vous verrez maintenant un nouveau dossier appelé `Migrations` dans votre projet. Ce dossier contient les fichiers de migration qui ont été créés en fonction des modifications apportées à vos classes de modèle. Ces fichiers de migration incluent les commandes SQL nécessaires pour mettre à jour le schéma de la base de données.

### Comment mettre à jour la base de données

Après avoir créé la migration, vous devez appliquer la migration pour mettre à jour le schéma de la base de données. Vous pouvez utiliser la commande `dotnet ef database update` pour appliquer la migration et mettre à jour la base de données. Assurez-vous que SQL Server est en cours d'exécution.

Exécutez la commande suivante dans le terminal :

```bash

dotnet ef database update
```

Cela mettra à jour le schéma de la base de données en fonction des modifications apportées à vos classes de modèle. Assurez-vous qu'il n'y a pas d'erreurs dans votre chaîne de connexion de base de données.

## Comment tester les points de terminaison de l'API

Maintenant, nous pouvons tester nos points de terminaison en utilisant Swagger. Pour ce faire, exécutez l'application en exécutant la commande suivante dans le terminal :

```bash

dotnet run
```

Cela exécutera notre application. Vous pouvez ouvrir votre navigateur et accéder à [`https://localhost:5001/swagger/index.html`](https://localhost:5001/swagger/index.html) pour accéder à la documentation Swagger. Vous devriez voir une liste de points de terminaison d'API, de modèles de requête et de réponse, et la possibilité de tester les points de terminaison directement depuis le navigateur.

Si votre numéro de port est différent de `5001`, ne vous inquiétez pas – cela fonctionnera toujours. Le port peut changer en fonction du type de machine que vous utilisez, mais il atteindra toujours le même résultat.

### Comment tester le point de terminaison `Get All Books`

Pour tester le point de terminaison `Get All Books`, suivez ces étapes :

1. Dans la documentation Swagger, cliquez sur le point de terminaison `GET /api/v1/books`.
    
2. Cliquez sur le bouton `Try it out`.
    
3. Cliquez sur le bouton `Execute`.
    

Cela enverra une requête à l'API pour récupérer tous les livres de la base de données.

Vous devriez voir la réponse de l'API, qui inclura la liste des livres qui ont été ensemencés dans la base de données.

L'image ci-dessous montre la réponse de l'API :

![Point de terminaison Get All Books Swagger UI](https://cdn.hashnode.com/res/hashnode/image/upload/v1732624950148/b497bc8e-727a-43c9-910f-755b3b6f208b.png align="left")

### Comment tester le point de terminaison `Get Book by ID`

Pour tester le point de terminaison `Get Book by ID`, suivez ces étapes :

1. Dans la documentation Swagger, cliquez sur le point de terminaison `GET /api/v1/books/{id}`.
    
2. Entrez l'ID d'un livre dans le champ `id`. Vous pouvez utiliser l'un des ID de livres qui a été ensemencé dans la base de données.
    
3. Cliquez sur le bouton `Try it out`.
    

Cela enverra une requête à l'API pour récupérer le livre avec l'ID spécifié. Vous devriez voir la réponse de l'API, qui inclura le livre avec l'ID spécifié.

L'image ci-dessous montre la réponse de l'API :

![Point de terminaison Get Book By ID Swagger UI](https://cdn.hashnode.com/res/hashnode/image/upload/v1732625042363/fe356453-afa6-4a78-b963-d0befff7bd63.png align="left")

### Comment tester le point de terminaison `Add Book`

Pour tester le point de terminaison `Add Book`, suivez ces étapes :

1. Dans la documentation Swagger, cliquez sur le point de terminaison `POST /api/v1/books`.
    
2. Cliquez sur le bouton `Try it out`.
    
3. Entrez les détails du livre dans le corps de la requête.
    
4. Cliquez sur le bouton `Execute`.
    

Cela enverra une requête à l'API pour ajouter un nouveau livre à la base de données.

Vous devriez voir la réponse de l'API, qui inclura le livre nouvellement créé.

L'image ci-dessous montre la réponse de l'API :

![Point de terminaison Add Book Swagger UI](https://cdn.hashnode.com/res/hashnode/image/upload/v1732625138350/faa54e57-e560-49ac-976a-b074e8eebb13.png align="left")

### Comment tester le point de terminaison `Update Book`

Pour tester le point de terminaison `Update Book`, suivez ces étapes :

1. Dans la documentation Swagger, cliquez sur le point de terminaison `PUT /api/v1/books/{id}`.
    
2. Entrez l'ID d'un livre dans le champ `id`. Vous pouvez utiliser l'ID de l'un des livres que nous venons d'ajouter.
    
3. Cliquez sur le bouton `Try it out`.
    

Cela enverra une requête à l'API pour mettre à jour le livre avec l'ID spécifié.

Vous devriez voir la réponse de l'API, qui inclura le livre mis à jour.

L'image ci-dessous montre la réponse de l'API :

![Point de terminaison Update Book Swagger UI](https://cdn.hashnode.com/res/hashnode/image/upload/v1732625300781/3de90d6c-92ca-40cb-a54e-2236ec921d86.png align="left")

### Comment tester le point de terminaison `Delete Book`

Pour tester le point de terminaison `Delete Book`, suivez ces étapes :

1. Dans la documentation Swagger, cliquez sur le point de terminaison `DELETE /api/v1/books/{id}`.
    
2. Entrez l'ID d'un livre dans le champ `id`. Vous pouvez utiliser l'un des ID des livres que nous venons d'ajouter ou des données de départ.
    
3. Cliquez sur le bouton `Try it out`.
    

Cela enverra une requête à l'API pour supprimer le livre avec l'ID spécifié.

L'image ci-dessous montre la réponse de l'API :

![Point de terminaison Delete Book Swagger UI](https://cdn.hashnode.com/res/hashnode/image/upload/v1732625225432/3b066f4c-2bf2-4f0c-a104-a94dbbad1706.png align="left")

Félicitations ! Vous avez implémenté toutes les opérations CRUD pour les livres et testé les points de terminaison de l'API en utilisant Swagger, vérifiant qu'ils fonctionnent comme prévu. Vous pouvez maintenant construire sur cette base pour ajouter plus de fonctionnalités à votre API.

## Conclusion

Ce guide a exploré comment créer une API minimale dans ASP.NET Core avec .NET 8. Nous avons construit une API de livres complète qui prend en charge les opérations CRUD, implémenté des exceptions personnalisées, défini et enregistré des points de terminaison d'API, et activé la documentation Swagger pour des tests faciles.

En suivant ce tutoriel, vous avez acquis une base solide pour construire des API minimales avec ASP.NET Core. Vous pouvez maintenant appliquer ces connaissances et créer des API robustes pour divers domaines et industries.

J'espère que vous avez trouvé ce tutoriel à la fois utile et informatif. Merci d'avoir lu !

N'hésitez pas à me contacter sur les réseaux sociaux :

* [Twitter](https://x.com/Clifftech_Dev)
    
* [LinkedIn](https://www.linkedin.com/in/isaiah-clifford-opoku/)
    
* [GitHub](https://github.com/Clifftech123)