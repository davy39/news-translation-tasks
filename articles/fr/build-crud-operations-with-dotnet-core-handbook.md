---
title: Comment créer des opérations CRUD avec .NET Core – Le guide de l'API Todo
date: '2024-05-24T14:33:16.000Z'
author: Isaiah Clifford Opoku
authorURL: https://www.freecodecamp.org/news/author/Clifftech/
originalURL: https://freecodecamp.org/news/build-crud-operations-with-dotnet-core-handbook
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/Attractive.png
tags:
- name: api
  slug: api
- name: crud
  slug: crud
- name: handbook
  slug: handbook
- name: .net core
  slug: net-core
seo_desc: "Welcome to this comprehensive guide on building CRUD operations with .NET\
  \ Core. We'll use a Todo API as our practical example so you can get hands-on experience\
  \ as you learn. \nThroughout this tutorial, you'll learn how to create, read, update,\
  \ and de..."
---


Bienvenue dans ce guide complet sur la création d'opérations CRUD avec .NET Core. Nous utiliserons une API Todo comme exemple pratique afin que vous puissiez acquérir une expérience concrète tout au long de votre apprentissage.

<!-- more -->

Tout au long de ce tutoriel, vous apprendrez à créer, lire, mettre à jour et supprimer des éléments Todo, et comment exploiter Entity Framework Core pour interagir avec une base de données.

## Table des matières

-   [Prérequis][1]
-   [Comment améliorer votre expérience de développement avec les extensions Visual Studio Code][2]
-   [Objectifs d'apprentissage][3]
-   [Qu'est-ce que .NET Core ?][4]
-   [.NET Core vs .NET Framework][5]
-   [Étape 1 : Configurer le répertoire de votre projet][6]
-   [Étape 2 : Établir la structure de votre projet][7]
-   [Étape 3 : Créer le modèle Todo][8]
-   [Étape 4 : Configurer le contexte de base de données][9]
-   [Étape 5 : Définir les objets de transfert de données (DTO)][10]
-   [Étape 6 : Implémenter le mapping d'objets pour l'API Todo][11]
-   [Étape 7 : Implémenter un middleware de gestion globale des exceptions][12]
-   [Étape 8 : Implémenter la couche de service et l'interface de service][13]
-   [Étape 9 : Implémenter la méthode CreateTodoAsync dans la classe de service][14]
-   [Étape 10 : Implémenter la méthode GetAllAsync dans la classe de service][15]
-   [Étape 11 : Créer la classe TodoController][16]
-   [Étape 12 : Implémenter la méthode CreateTodoAsync dans la classe TodoController][17]
-   [Étape 13 : Implémenter les migrations et mettre à jour la base de données][18]
-   [Étape 14 : Vérifier votre API avec Postman][19]
-   [Étape 15 : Récupérer tous les éléments Todo][20]
-   [Étape 16 : Implémenter la méthode GetByIdAsync][21]
-   [Étape 17 : Implémenter la méthode UpdateTodoAsync][22]
-   [Étape 18 : Implémenter la méthode DeleteTodoAsync][23]
-   [Étape 19 : Tester vos points de terminaison API avec Postman][24]
-   [Conclusion][25]

Avant de commencer, assurons-nous que vous disposez des prérequis nécessaires.

## Prérequis

Avant de débuter, assurez-vous d'avoir installé les outils nécessaires sur votre machine. Voici les liens de téléchargement :

-   [.NET SDK][26]
-   [Visual Studio Code][27]
-   [Visual Studio 2019][28]
-   [Postman][29]
-   [SQLServer][30]

Après avoir installé le SDK .NET, il est important de vérifier son installation et de contrôler la version. Pour ce tutoriel, nous utiliserons .NET 8.0.

Pour vérifier la version du SDK .NET installée sur votre machine, ouvrez le terminal et exécutez la commande suivante :

```
dotnet --version
```

Si le SDK .NET est correctement installé, le numéro de version s'affichera dans le terminal :

```
8.0
```

Si vous voyez un numéro de version différent, assurez-vous d'avoir installé .NET 8.0 sur votre machine.

## Comment améliorer votre expérience de développement avec les extensions Visual Studio Code

Visual Studio Code, un éditeur de code léger et open source, est un excellent outil pour créer des applications .NET Core. Vous pouvez encore améliorer ses fonctionnalités avec des extensions qui simplifient le processus de développement.

Voici deux extensions recommandées pour le développement .NET Core :

-   [C# pour Visual Studio Code][31]
-   [C# Namespace Autocompletion][32]

Pour installer ces extensions, suivez ces étapes :

1.  Ouvrez Visual Studio Code.
2.  Cliquez sur l'icône Extensions dans la barre d'activité sur le côté de la fenêtre pour ouvrir la vue Extensions.
3.  Dans la barre de recherche, tapez le nom de l'extension.
4.  Dans les résultats de la recherche, localisez l'extension correcte et cliquez sur le bouton Installer.

Voici à quoi ressemble la vue Extensions dans Visual Studio Code :

-   Extension C# Devkit pour Visual Studio Code ![Vue Extensions pour Devkit](https://www.freecodecamp.org/news/content/images/2024/05/DevKIt.png)
    
-   Extension Namespace Autocompletion pour Visual Studio Code ![Vue Extensions pour Namespace Autocompletion](https://www.freecodecamp.org/news/content/images/2024/05/NameSpace.png)
    

Dans les images ci-dessus, les extensions sont déjà installées. Si elles ne le sont pas sur votre système, vous pouvez le faire en cliquant sur le bouton Installer.

Avec ces outils essentiels en place, nous sommes maintenant prêts à commencer la construction de notre API Todo.

## Objectifs d'apprentissage

À la fin de ce tutoriel, vous aurez appris à :

-   Configurer un nouveau projet .NET Core à l'aide de la CLI .NET Core
-   Définir un modèle pour un élément Todo
-   Créer un contexte de base de données pour interagir avec la base de données
-   Implémenter le routage et les contrôleurs pour l'API Todo
-   Créer une classe de service pour gérer la logique métier
-   Implémenter les opérations CRUD pour l'API Todo
-   Gérer les exceptions globalement à l'aide d'un middleware
-   Tester les points de terminaison de l'API à l'aide de Postman

Si vous débutez avec C# et .NET, ne vous inquiétez pas. J'expliquerai tous les concepts en profondeur pour m'assurer que vous les comprenez. Pour plus d'informations, vous pouvez vous référer à la [documentation C#][33].

Avant d'approfondir le code, clarifions ce qu'est .NET Core.

## Qu'est-ce que .NET Core ?

.NET Core, également connu sous le nom d'ASP.NET Core, est un framework multiplateforme qui facilite la création d'applications web, d'API et de services. C'est un framework gratuit, open source et performant, conçu pour créer des applications modernes, basées sur le cloud et connectées à Internet. C'est le successeur du .NET Framework.

Mais quelle est la différence entre .NET Core et .NET Framework ?

## .NET Core vs .NET Framework

.NET Core et .NET Framework sont deux frameworks distincts utilisés pour le développement d'applications. .NET Core est un framework multiplateforme qui fonctionne sur Windows, macOS et Linux. C'est un framework modulaire, open source et gratuit, conçu pour créer des applications modernes, basées sur le cloud et connectées à Internet.

D'un autre côté, le `.NET Framework` est un `framework réservé à Windows` utilisé pour créer des `applications de bureau Windows`, des `applications web` et des services. Contrairement à .NET Core, il n'est ni open source ni gratuit. Cependant, c'est un framework mature qui existe depuis longtemps.

Avec une compréhension fondamentale de .NET Core et .NET Framework, nous sommes prêts à nous lancer dans la construction de notre API Todo.

Dans ce tutoriel, nous exploiterons .NET Core pour construire une API Todo qui effectue des opérations CRUD. Notre parcours nous mènera à travers la création d'un nouveau projet, la définition du modèle Todo, la configuration de la base de données et l'implémentation des opérations CRUD.

Commençons avec Visual Studio Code. Dans ce tutoriel, nous utiliserons la CLI .NET Core pour créer notre projet et construire notre API. Si vous préférez Visual Studio 2019, vous pouvez également suivre en utilisant cet IDE, mais nous utiliserons Visual Studio Code pour cet article.

## Étape 1 : Configurer le répertoire de votre projet

Tout d'abord, naviguez vers le répertoire où vous souhaitez héberger votre projet. Il peut s'agir de n'importe quel dossier de votre système où vous souhaitez stocker votre code.

Une fois dans le répertoire souhaité, ouvrez le terminal. Vous pouvez le faire dans Visual Studio Code en allant dans `Affichage -> Terminal` ou en appuyant sur Ctrl + ` (backtick).

Le terminal étant ouvert, tapez la commande suivante :

```
dotnet new webapi -n TodoAPI
```

Cette commande demande à la CLI .NET Core de créer un nouveau projet d'API web nommé `TodoAPI`. L'option `-n` spécifie le nom du projet.

![Création d'une nouvelle API avec la CLI .NET Core](https://www.freecodecamp.org/news/content/images/2024/05/TerminalCreatingNewAPI.png)

L'image ci-dessus illustre comment exécuter la commande dans le terminal.

Après avoir appuyé sur la touche 'Entrée', la CLI .NET Core commencera à générer les fichiers nécessaires pour votre projet.

![Structure des dossiers du projet .NET](https://www.freecodecamp.org/news/content/images/2024/05/ProjectFile.png)

L'image ci-dessus présente la structure de projet générée. Elle comprend tous les fichiers et répertoires nécessaires pour un projet d'API web .NET Core.

Avec les fichiers et dossiers de projet générés par la CLI .NET Core, prenons un moment pour comprendre le rôle de chaque fichier.

-   `appsettings.json` : Ce fichier contient les paramètres de configuration de l'application. C'est l'endroit idéal pour stocker les chaînes de connexion, les configurations de journalisation et d'autres paramètres.
    
-   `Program.cs` : Servant de point d'entrée de l'application, ce fichier est responsable de la configuration de l'hôte et des services.
    
-   `TodoAPI.csproj` : Ce fichier de projet contient des métadonnées sur votre projet, y compris les références aux packages et bibliothèques nécessaires.
    
-   `appsettings.Development.json` : Ce fichier est conçu pour les paramètres de configuration spécifiques à l'environnement de développement. Il est idéal pour stocker des paramètres propres à l'environnement. Mais pour les besoins de ce tutoriel, nous utiliserons plutôt le fichier `appsettings.json`.
    
-   `TodoAPI.http` : Ce fichier est généralement utilisé pour tester les points de terminaison de l'API à l'aide de l'extension REST Client dans Visual Studio Code, car il contient des exemples de requêtes. Cependant, dans ce tutoriel, nous utiliserons Postman pour les tests, nous n'aurons donc pas besoin de ce fichier et nous procéderons à sa suppression.
    

## Étape 2 : Établir la structure de votre projet

Après avoir configuré le répertoire de notre projet, il est temps d'en définir la structure. Nous allons créer plusieurs dossiers, chacun ayant un but spécifique :

![structure des dossiers du projet](https://www.freecodecamp.org/news/content/images/2024/05/ProjectFolder.png)

-   `AppDataContext` : Ce dossier contiendra le contexte de base de données, qui est responsable de l'interaction avec la base de données.
-   `Contracts` : Ce dossier hébergera nos objets de transfert de données (DTO), qui sont utilisés pour formater les données envoyées entre le client et le serveur.
-   `Models` : Ce dossier contiendra le modèle Todo, qui représente la structure d'un élément Todo.
-   `Controllers` : Ce dossier hébergera le TodoController, qui gère les requêtes HTTP entrantes et envoie les réponses.
-   `Interfaces` : Ce dossier contiendra l'interface IService, qui définit le contrat pour notre classe de service.
-   `Services` : Ce dossier hébergera la classe Service, qui implémente l'interface IService et contient la logique métier de notre application.
-   `Mapping` : Ce dossier contiendra le profil de mapping, utilisé pour mapper les propriétés entre différents objets.
-   `Middleware` : Ce dossier hébergera le middleware d'exception, qui gère les exceptions de manière globale dans toute notre application.

*Félicitations !* Vous avez configuré avec succès le répertoire de votre projet et établi sa structure. Dans la section suivante, nous nous pencherons sur la définition du modèle Todo.

### Comment ajuster le fichier Program.cs pour ControllerBase

Lors de la création d'une nouvelle application à l'aide de la commande `dotnet new webapi` dans .NET 6 et versions ultérieures, le projet généré est un projet d'API web minimal. Mais pour ce tutoriel, nous utiliserons la méthode traditionnelle de création d'API, ce qui nécessite quelques ajustements au fichier `Program.cs`.

Avant de passer aux modifications, discutons brièvement de ce qu'est une API minimale.

### Comprendre les API minimales

Dans .NET 6, Microsoft a introduit une nouvelle fonctionnalité connue sous le nom d'API minimales (Minimal APIs). Ces API sont plus simples et plus légères que les API traditionnelles. Elles vous permettent de définir vos routes et points de terminaison API à l'aide d'un seul fichier, sans avoir besoin de contrôleurs ou de classes de démarrage. Cette approche facilite la création de petites API ciblées, rapides à construire et faciles à maintenir.

Cependant, pour les besoins de ce tutoriel, nous nous en tiendrons à la structure d'API traditionnelle. Procédons aux modifications nécessaires dans le fichier `Program.cs`.

![Vue initiale de Program.cs](https://www.freecodecamp.org/news/content/images/2024/05/Program.cs.png)

L'image ci-dessus montre l'état initial du fichier `Program.cs` lorsque vous créez un nouveau projet d'API web. Pour l'adapter à une utilisation avec ControllerBase, nous devons supprimer du code et en ajouter de nouveaux.

Commencez par tout supprimer dans le fichier `Program.cs` et remplacez-le par le code suivant :

```csharp
 // program.cs
var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllers();

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();
```

Nous pouvons maintenant passer à l'étape suivante, où nous définirons le modèle Todo.

## Étape 3 : Créer le modèle Todo

Avant de nous lancer dans la création de notre modèle Todo, il est important de savoir à quoi sert un modèle dans `.NET CORE`. Considérez un `modèle` comme un `plan` (blueprint) pour le type de données avec lequel notre application va travailler. Il nous aide à organiser et à gérer ces données efficacement.

Pour notre application de liste Todo, nous avons besoin d'une image claire de ce à quoi ressemble chaque élément Todo. Cela signifie décider de choses comme les noms, les descriptions, s'il est terminé ou non, les échéances, les priorités et quand il a été créé ou modifié. En étant clairs sur ces détails, nous pouvons gérer et afficher correctement nos éléments Todo.

### Présentation du modèle Todo

Maintenant, concrétisons notre idée en créant le modèle `Todo`. Ce modèle est comme un modèle pour nos éléments Todo, garantissant qu'ils ont tous les bons éléments.

Créons un nouveau fichier appelé `Todo.cs` dans le dossier `Models` et remplissons-le avec ce code :

```csharp
// Models/Todo.cs
using System.ComponentModel.DataAnnotations;

namespace TodoAPI.Models
{
    public class Todo
    {
        [Key]
        public Guid Id { get; set; }
        public string Title { get; set; }
        public string Description { get; set; }
        public bool IsComplete { get; set; }
        public DateTime DueDate { get; set; }
        public int Priority { get; set; }
        public DateTime CreatedAt { get; set; }
        public DateTime UpdatedAt { get; set; }

        public Todo()
        {
            IsComplete = false;
        }
    }
}
```

Voici ce que signifie chaque partie du modèle `Todo` :

-   **Id** : Un numéro spécial qui rend chaque élément Todo unique.
-   **Title** : Le nom de l'élément Todo.
-   **Description** : Détails supplémentaires sur l'élément Todo.
-   **IsComplete** : Indique si l'élément Todo est terminé ou non.
-   **DueDate** : La date à laquelle l'élément Todo doit être terminé.
-   **Priority** : L'importance de l'élément Todo.
-   **CreatedAt** et **UpdatedAt** : Quand l'élément Todo a été créé pour la première fois et modifié pour la dernière fois.

La balise `[Key]` nous indique que `Id` est le moyen principal d'identifier chaque élément Todo dans notre base de données.

En ayant un modèle `Todo` clair, nous pouvons facilement suivre et afficher nos éléments Todo de la meilleure façon possible.

Dans ASP.NET Core, les modèles peuvent être utilisés pour représenter diverses choses. L'un de ces cas d'utilisation est la gestion des erreurs. Lorsqu'une erreur survient dans notre application, nous pouvons créer un modèle pour cette erreur et le renvoyer au client.

Créons un modèle spécifiquement pour la gestion des erreurs dans notre application.

```csharp
// Models/ErrorResponse.cs

namespace TodoAPI.Models
{
       public class ErrorResponse
 {
     public string Title { get; set; }
     public int StatusCode { get; set; }
     public string Message { get; set; }
 }
}
```

Ce modèle ErrorResponse sera utilisé pour renvoyer des messages d'erreur au client lorsqu'une erreur survient dans notre application. Il comprend un titre pour l'erreur, un message et un code d'état, fournissant au client des informations utiles sur ce qui s'est mal passé.

Définissons un autre modèle pour gérer notre chaîne de connexion à la base de données.

```csharp
// Models/DbSettings.cs 

namespace TodoAPI.Models
{
    public class DbSettings
    {
        public string ConnectionString { get; set; }
    }
}
```

Le modèle `DbSettings` est conçu pour encapsuler la chaîne de connexion de notre base de données. Il contient une seule propriété, `ConnectionString`, qui stockera la valeur réelle de la chaîne de connexion.

Avec notre modèle `Todo` en place, nous sommes maintenant prêts à procéder à la configuration du contexte de base de données.

Avant de commencer à configurer notre base de données, nous devons installer les packages nécessaires pour notre projet.

### Installation des packages

Pour configurer notre projet, nous devons installer plusieurs packages. Nous utiliserons la CLI dotnet pour cette tâche.

Avant de commencer, assurez-vous d'être dans le répertoire racine de votre projet. Si vous n'êtes pas sûr de votre emplacement actuel dans le terminal, vous pouvez le vérifier en exécutant la commande suivante :

```
ls
```

Cette commande listera tous les fichiers et dossiers de votre répertoire actuel. L'image ci-dessous montre la sortie du terminal après l'exécution de la commande `ls`.

![Terminal ls file](https://www.freecodecamp.org/news/content/images/2024/05/ls-terminal.png)

Si la sortie de votre terminal correspond à l'image ci-dessus, vous êtes dans le bon répertoire pour installer les packages.

Maintenant, installons les packages :

```
dotnet add package Microsoft.EntityFrameworkCore --version 8.0.0 
dotnet add package Microsoft.EntityFrameworkCore.Design --version 8.0.0
dotnet add package Microsoft.EntityFrameworkCore.SqlServer --version 8.0.0
dotnet add package AutoMapper --version 13.0.1
```

Voici un bref aperçu de ce que font ces packages :

-   `Microsoft.EntityFrameworkCore` : Fournit les fonctionnalités de base d'Entity Framework Core, nous permettant d'interagir avec notre base de données.
-   `Microsoft.EntityFrameworkCore.Design` : Comprend des composants de conception pour Entity Framework Core, tels que les migrations.
-   `Microsoft.EntityFrameworkCore.SqlServer` : Nous permet d'utiliser SQL Server comme fournisseur de base de données.
-   `AutoMapper` : Simplifie le mapping d'objet à objet, facilitant le transfert de propriétés entre différents objets.

**Note** : Assurez-vous d'installer les mêmes versions des packages que celles indiquées ci-dessus pour éviter tout problème de compatibilité.

Pour confirmer que tous les packages ont été installés avec succès, accédez au fichier `TodoAPI.csproj` situé dans le répertoire racine de votre projet. Les packages installés doivent être répertoriés sous la section `ItemGroup`.

```xml
<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
    <InvariantGlobalization>true</InvariantGlobalization>
  </PropertyGroup>

  <ItemGroup>
    <PackageReference Include="AutoMapper" Version="13.0.1" />
    <PackageReference Include="Microsoft.AspNetCore.OpenApi" Version="8.0.0" />
    <PackageReference Include="Microsoft.EntityFrameworkCore" Version="8.0.0" />
    <PackageReference Include="Microsoft.EntityFrameworkCore.Design" Version="8.0.0">
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
      <PrivateAssets>all</PrivateAssets>
    </PackageReference>
    <PackageReference Include="Microsoft.EntityFrameworkCore.SqlServer" Version="8.0.0" />
    <PackageReference Include="Swashbuckle.AspNetCore" Version="6.4.0" />
  </ItemGroup>

</Project>
```

Le fichier `TodoAPI.csproj` ci-dessus montre les packages installés répertoriés sous la section `ItemGroup`. Si votre fichier `TodoAPI.csproj` reflète la même chose, cela confirme que les packages ont été installés avec succès.

Avec les packages nécessaires installés, nous sommes maintenant prêts à configurer le contexte de base de données pour notre API Todo.

## Étape 4 : Configurer le contexte de base de données

Dans ASP.NET Core, le contexte de base de données est un composant crucial qui gère les interactions avec la base de données. Il est responsable de tâches telles que l'établissement d'une connexion à la base de données, l'interrogation des données et l'enregistrement des modifications.

Pour permettre à notre `API Todo` d'interagir avec la base de données, nous devons créer un contexte de base de données.

Créons un nouveau fichier nommé `TodoDbContext` dans le dossier `AppDataContext` et remplissons-le avec le code suivant :

```csharp
// AppDataContext/TodoDbContext.cs

using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Options;
using TodoAPI.Models;

namespace TodoAPI.AppDataContext
{

    // La classe TodoDbContext hérite de DbContext
     public class TodoDbContext : DbContext
     {

        // Champ DbSettings pour stocker la chaîne de connexion
         private readonly DbSettings _dbsettings;

            // Constructeur pour injecter le modèle DbSettings
         public TodoDbContext(IOptions<DbSettings> dbSettings)
         {
             _dbsettings = dbSettings.Value;
         }


        // Propriété DbSet pour représenter la table Todo
         public DbSet<Todo> Todos { get; set; }

         // Configuration du fournisseur de base de données et de la chaîne de connexion

         protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
         {
             optionsBuilder.UseSqlServer(_dbsettings.ConnectionString);
         }

            // Configuration du modèle pour l'entité Todo
         protected override void OnModelCreating(ModelBuilder modelBuilder)
         {
             modelBuilder.Entity<Todo>()
                 .ToTable("TodoAPI")
                 .HasKey(x => x.Id);
         }
     }
}
```

Voici une décomposition de la classe `TodoDbContext` :

-   **`TodoDbContext`** : Cette classe, qui hérite de `DbContext` (faisant partie d'Entity Framework Core), est la classe principale qui interagit avec la base de données.
-   **`_dbsettings`** : Ce champ privé stocke la chaîne de connexion pour notre base de données. Nous injectons le modèle `DbSettings`, que nous avons créé précédemment pour gérer la chaîne de connexion, dans la classe `TodoDbContext`.
-   **`Todos`** : Cette propriété représente la table `Todo` dans notre base de données. C'est un `DbSet` d'objets `Todo`, ce qui nous permet d'interroger et d'enregistrer des instances de `Todo`.
-   **`OnConfiguring`** : Cette méthode configure le fournisseur de base de données et la chaîne de connexion. Nous utilisons SQL Server comme fournisseur de base de données, et la chaîne de connexion est récupérée à partir du modèle `DbSettings`.
-   **`OnModelCreating`** : Cette méthode configure le modèle pour l'entité `Todo`. Nous spécifions le nom de la table, la clé primaire et d'autres configurations pour l'entité `Todo`.

Pour utiliser notre `TodoDbContext` pour interagir avec la base de données, nous devons l'enregistrer dans le fichier `Program.cs`. Ce processus d'enregistrement fait partie de la configuration du conteneur d'injection de dépendances (DI) dans .NET Core.

Voici comment faire :

```csharp
// Program.cs


using TodoAPI.AppDataContext;
using TodoAPI.Models;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();



 // Ajoutez ceci dans le fichier Program.cs
builder.Services.Configure<DbSettings>(builder.Configuration.GetSection("DbSettings")); // Ajoutez cette ligne
builder.Services.AddSingleton<TodoDbContext>(); // Ajoutez cette ligne




var app = builder.Build();

// Ajoutez cette ligne

{
    using var scope = app.Services.CreateScope(); // Ajoutez cette ligne
    var context = scope.ServiceProvider; // Ajoutez cette ligne
}


if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.UseExceptionHandler();
app.UseAuthorization();

app.MapControllers();

app.Run();
```

Dans l'extrait de code ci-dessus, nous faisons deux choses :

-   Configuration des paramètres de base de données en liant la section `DbSettings` du fichier `appsettings.json` à la classe `DbSettings`. Cela nous permet d'accéder à la chaîne de connexion de la base de données dans notre application.
-   Enregistrement du `TodoDbContext` auprès du conteneur DI en tant que service singleton. Cela signifie qu'une seule instance de `TodoDbContext` sera créée et partagée dans toute l'application.

Le contexte de base de données étant enregistré, nous pouvons maintenant l'utiliser pour effectuer des opérations CRUD sur nos éléments Todo.

Vérifions maintenant si tout fonctionne correctement en lançant l'application.

```
dotnet run
```

Si vous voyez la sortie suivante, cela signifie que votre application fonctionne avec succès :

```
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: http://localhost:5086
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
info: Microsoft.Hosting.Lifetime[0]
Content root path: E:\Todo\TodoAPI
```

**Note** : Si vous rencontrez des erreurs, assurez-vous simplement d'avoir suivi toutes les étapes correctement et que les packages nécessaires ont été installés avec succès. Si vous voyez des avertissements, vous pouvez les ignorer pour le moment.

La classe `TodoDbContext` étant maintenant configurée, nous sommes prêts à définir les contrats (Contracts) pour notre application.

## Étape 5 : Définir les objets de transfert de données (DTO)

Dans le contexte du développement .NET, un objet de transfert de données (DTO) est un objet simple qui transporte des données entre les processus. Il est souvent utilisé conjointement avec une couche de service pour formater les données envoyées entre le client et le serveur.

Pour notre API Todo, nous définirons deux DTO : `CreateTodoRequest` et `UpdateTodoRequest`. Ces DTO nous aideront à imposer la structure et la validation des données envoyées à notre API.

Accédez au dossier `Contracts` et créez deux nouveaux fichiers : `CreateTodoRequest.cs` et `UpdateTodoRequest.cs`.

### Le fichier `CreateTodoRequest`

Le DTO `CreateTodoRequest` définira la structure et les règles de validation pour la création d'un nouvel élément Todo. Ajoutez le code suivant au fichier `CreateTodoRequest.cs` :

```csharp
public class CreateTodoRequest
{
    [Required]
    [StringLength(100)]
    public string Title { get; set; }

    [StringLength(500)]
    public string Description { get; set; }

    [Required]
    public DateTime DueDate { get; set; }

    [Range(1, 5)]
    public int Priority { get; set; }
}
```

Dans ce DTO, nous avons défini des propriétés pour `Title`, `Description`, `DueDate` et `Priority`. Nous avons également ajouté des attributs de validation tels que `[Required]`, `[StringLength]` et `[Range]` pour imposer certaines règles sur ces propriétés.

### Le fichier `UpdateTodoRequest`

Le DTO `UpdateTodoRequest` définira la structure et les règles de validation pour la mise à jour d'un élément Todo existant. Ajoutez le code suivant au fichier `UpdateTodoRequest.cs` :

```csharp
public class UpdateTodoRequest
{
    [StringLength(100)]
    public string Title { get; set; }

    [StringLength(500)]
    public string Description { get; set; }

    public bool? IsComplete { get; set; }

    public DateTime? DueDate { get; set; }

    [Range(1, 5)]
    public int? Priority { get; set; }

    public UpdateTodoRequest()
    {
        IsComplete = false;
    }
}
```

Dans ce DTO, nous avons défini des propriétés pour `Title`, `Description`, `IsComplete`, `DueDate` et `Priority`. La propriété `IsComplete` est nullable, ce qui signifie qu'elle peut être définie sur `null` si elle n'est pas fournie. Nous avons également ajouté des attributs de validation tels que `[StringLength]` et `[Range]` pour imposer certaines règles sur ces propriétés.

Avec ces DTO en place, nous sommes maintenant prêts à implémenter la couche de service pour notre API Todo.

Testez maintenant l'application pour voir s'il y a des erreurs.

```
 dotnet  build
```

Si vous voyez la sortie suivante, cela signifie que votre application fonctionne avec succès :

```
MSBuild version 17.8.3+195e7f5a3 for .NET
  Determining projects to restore...
  All projects are up-to-date for restore.
  TodoAPI -> E:\Todo\TodoAPI\bin\Debug\net8.0\TodoAPI.dll

Build succeeded.
    0 Warning(s)
    0 Error(s)

Time Elapsed 00:00:00.94
```

**Note** : Si vous rencontrez des erreurs, assurez-vous d'avoir suivi toutes les étapes correctement et que les packages nécessaires ont été installés avec succès. Si vous voyez des avertissements, vous pouvez les ignorer pour le moment.

Les DTO étant définis, nous sommes maintenant prêts à implémenter le mapping pour l'API Todo.

## Étape 6 : Implémenter le mapping d'objets pour l'API Todo

Après avoir défini les DTO pour notre API Todo, l'étape suivante consiste à implémenter le mapping d'objets. Ce processus nous permet de convertir les DTO en modèle Todo et vice-versa, un aspect critique de la transformation des données dans notre application.

Pour simplifier ce processus, nous utiliserons la bibliothèque `AutoMapper`. AutoMapper est une bibliothèque largement utilisée qui simplifie le mapping d'objet à objet, facilitant le transfert de propriétés entre différents objets.

Nous avons déjà installé le package `AutoMapper` dans notre projet. Maintenant, dans le dossier `MappingProfiles`, créez un nouveau fichier nommé `AutoMapperProfile.cs` et ajoutez le code suivant :

```csharp
using AutoMapper;
using TodoAPI.Contracts;
using TodoAPI.Models;

namespace TodoAPI.MappingProfiles
{
    public class AutoMapperProfile : Profile
    {
        public AutoMapperProfile()
        {
            CreateMap<CreateTodoRequest, Todo>()
                .ForMember(dest => dest.Id, opt => opt.Ignore())
                .ForMember(dest => dest.CreatedAt, opt => opt.Ignore())
                .ForMember(dest => dest.UpdatedAt, opt => opt.Ignore());

            CreateMap<UpdateTodoRequest, Todo>()
                .ForMember(dest => dest.Id, opt => opt.Ignore())
                .ForMember(dest => dest.CreatedAt, opt => opt.Ignore())
                .ForMember(dest => dest.UpdatedAt, opt => opt.Ignore());
        }
    }
}
```

Décomposons la classe `AutoMapperProfile` :

-   **AutoMapperProfile** : Cette classe, qui hérite de `Profile` (une classe fournie par AutoMapper), nous permet de définir des configurations de mapping.
-   **CreateMap** : Cette méthode crée un mapping entre deux objets. Ici, nous mappons de `CreateTodoRequest` vers `Todo` et de `UpdateTodoRequest` vers `Todo`.
-   **ForMember** : Cette méthode configure le mapping pour une propriété spécifique. Nous l'utilisons pour ignorer les propriétés `Id`, `CreatedAt` et `UpdatedAt` lors du mapping des DTO vers le modèle `Todo`.

Ajoutons maintenant l'AutoMapper au conteneur DI dans le fichier `Program.cs`.

```csharp
// Program.cs

using TodoAPI.AppDataContext;
using TodoAPI.Models;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();



 // Ajoutez ceci dans le fichier Program.cs
builder.Services.AddAutoMapper(AppDomain.CurrentDomain.GetAssemblies());  // Ajoutez cette ligne


// .....

var app = builder.Build();



// .....
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseExceptionHandler();
app.UseAuthorization();

app.MapControllers();

app.Run();
```

Les profils de mapping étant en place, nous pouvons maintenant implémenter la couche de service pour notre API Todo.

## Étape 7 : Implémenter un middleware de gestion globale des exceptions

Au fur et à mesure que nous progressons avec notre API Todo, il est crucial d'implémenter un mécanisme pour gérer les exceptions globalement. Cela garantit que toutes les exceptions survenant pendant l'exécution de notre application sont capturées et traitées de manière appropriée, en fournissant des messages d'erreur significatifs au client.

.NET 8 introduit l'interface `IExceptionHandler`, qui simplifie le processus de création d'un gestionnaire d'exceptions personnalisé. Ce gestionnaire capturera toutes les exceptions survenant dans notre application et renverra une réponse d'erreur cohérente au client.

Créons un gestionnaire d'exceptions global dans le dossier `Middleware`. Créez un nouveau fichier nommé `GlobalExceptionHandler.cs` et ajoutez le code suivant :

```csharp
// Middleware/GlobalExceptionHandler.cs

using System.Net;
using Microsoft.AspNetCore.Diagnostics;
using TodoAPI.Models;

namespace TodoAPI.Middleware
{
    public class GlobalExceptionHandler : IExceptionHandler
    {
        private readonly ILogger<GlobalExceptionHandler> _logger;

        public GlobalExceptionHandler(ILogger<GlobalExceptionHandler> logger)
        {
            _logger = logger;
        }

        public async ValueTask<bool> TryHandleAsync(
            HttpContext httpContext,
            Exception exception,
            CancellationToken cancellationToken)
        {
            _logger.LogError(
                $"An error occurred while processing your request: {exception.Message}");

            var errorResponse = new ErrorResponse
            {
                Message = exception.Message
            };

            switch (exception)
            {
                case BadHttpRequestException:
                    errorResponse.StatusCode = (int)HttpStatusCode.BadRequest;
                    errorResponse.Title = exception.GetType().Name;
                    break;

                default:
                    errorResponse.StatusCode = (int)HttpStatusCode.InternalServerError;
                    errorResponse.Title = "Internal Server Error";
                    break;
            }

            httpContext.Response.StatusCode = errorResponse.StatusCode;

            await httpContext
                .Response
                .WriteAsJsonAsync(errorResponse, cancellationToken);

            return true;
        }
    }
}
```

Voici une décomposition de la classe `GlobalExceptionHandler` :

-   **GlobalExceptionHandler** : Cette classe implémente l'interface `IExceptionHandler`, permettant la gestion globale des exceptions dans notre application.
-   **TryHandleAsync** : Cette méthode est invoquée lorsqu'une exception survient. Elle enregistre le message d'erreur, crée un objet `ErrorResponse`, définit le code d'état et le titre en fonction du type d'exception, et renvoie une réponse d'erreur cohérente au client.
-   **ErrorResponse** : Cette classe représente la réponse d'erreur renvoyée au client lorsqu'une exception survient. Elle contient des propriétés pour le message d'erreur, le code d'état et le titre.
-   **BadHttpRequestException** : Ce cas gère les exceptions de type `BadHttpRequestException` et définit le code d'état et le titre en conséquence.

Après avoir configuré le gestionnaire d'exceptions global, nous devons l'enregistrer dans notre fichier `Program.cs` :

```csharp
// Program.cs

using TodoAPI.AppDataContext;
using TodoAPI.Interface;
using TodoAPI.Middleware;
using TodoAPI.Models;
using TodoAPI.Services;

var builder = WebApplication.CreateBuilder(args);



builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();



// ....



builder.Services.AddExceptionHandler<GlobalExceptionHandler>(); // Ajoutez cette ligne

builder.Services.AddProblemDetails();  // Ajoutez cette ligne

// Ajout de la journalisation (logging)
builder.Services.AddLogging();  // Ajoutez cette ligne



var app = builder.Build();


// ......


if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection(); // Ajoutez cette ligne

app.UseExceptionHandler();
app.UseAuthorization();

app.MapControllers();

app.Run();


// ...
```

## Étape 8 : Implémenter la couche de service et l'interface de service

Dans le développement .NET, la couche de service encapsule la logique métier principale d'une application. Elle sert de pont entre le contrôleur et la base de données, assurant une séparation claire des préoccupations.

Tout d'abord, définissons une interface pour notre couche de service.

```csharp
// Interfaces/ITodoServices.cs 

using TodoAPI.Contracts;
using TodoAPI.Models;

namespace TodoAPI.Interface
{
     public interface ITodoServices
     {
         Task<IEnumerable<Todo>> GetAllAsync();
         Task<Todo> GetByIdAsync(Guid id);
         Task CreateTodoAsync(CreateTodoRequest request);
         Task UpdateTodoAsync(Guid id, UpdateTodoRequest request);
         Task DeleteTodoAsync(Guid id);
     }
}
```

Voici un bref aperçu des méthodes définies dans l'interface `ITodoServices` :

-   `GetAllAsync` : Récupère tous les éléments Todo de la base de données.
-   `GetByIdAsync` : Récupère un élément Todo spécifique par son `Id`.
-   `CreateTodoAsync` : Ajoute un nouvel élément Todo à la base de données.
-   `UpdateTodoAsync` : Modifie un élément Todo existant dans la base de données.
-   `DeleteTodoAsync` : Supprime un élément Todo de la base de données.

Maintenant, créons une classe de service qui implémente ces méthodes. Nous utiliserons l'injection de dépendances pour injecter l'interface `ITodoServices` dans la classe de service, rendant notre code plus modulaire, testable et maintenable.

```csharp
// Services/TodoServices.cs

using TodoAPI.Interface;

namespace TodoAPI.Services
{
    public class TodoServices : ITodoServices
    {

    }
}
```

À ce stade, vous rencontrerez une erreur car nous n'avons pas encore implémenté les méthodes de l'interface `ITodoServices` dans la classe `TodoServices`.

L'image ci-dessous montre le message d'erreur qui apparaît lorsque les méthodes de l'interface `ITodoServices` ne sont pas implémentées dans la classe `TodoServices`.

![Erreur dans la classe TodoServices](https://www.freecodecamp.org/news/content/images/2024/05/InterfaceError.png)

Pour résoudre ce problème, survolez `ITodoServices`, cliquez sur l'icône de l'ampoule qui apparaît et sélectionnez 'Implement interface'. Cela générera automatiquement des squelettes pour les méthodes définies dans l'interface `ITodoServices`.

L'image ci-dessous montre l'option 'Implement interface' qui apparaît lors du survol de `ITodoServices` dans la classe `TodoServices`.

![Implémentation de l'interface ITodoServices](https://www.freecodecamp.org/news/content/images/2024/05/QickFixt.png)

Après avoir implémenté l'interface, la classe `TodoServices` devrait ressembler à ceci :

```csharp
// Services/TodoServices.cs
using TodoAPI.Contracts;
using TodoAPI.Interface;
using TodoAPI.Models;

namespace TodoAPI.Services
{
    public class TodoServices : ITodoServices
    {
        public Task CreateTodoAsync(CreateTodoRequest request)
        {
            throw new NotImplementedException();
        }

        public Task DeleteTodoAsync(Guid id)
        {
            throw new NotImplementedException();
        }

        public Task<IEnumerable<Todo>> GetAllAsync()
        {
            throw new NotImplementedException();
        }

        public Task<Todo> GetByIdAsync(Guid id)
        {
            throw new NotImplementedException();
        }

        public Task UpdateTodoAsync(Guid id, UpdateTodoRequest request)
        {
            throw new NotImplementedException();
        }
    }
}
```

### Comment améliorer la classe TodoServices avec l'injection de dépendances

Maintenant, enrichissons notre classe `TodoServices` avec quelques propriétés essentielles. Ces propriétés fourniront les outils nécessaires pour interagir avec la base de données, la journalisation et le mapping d'objets.

Au sommet de la classe `TodoServices`, ajoutez les propriétés suivantes :

```csharp
// Services/TodoServices.cs

// ...

private readonly TodoDbContext _context;
private readonly ILogger<TodoServices> _logger;
private readonly IMapper _mapper;

// ...
```

Voici une brève explication de ces propriétés :

-   `_context` : Une instance de la classe `TodoDbContext`, nous permettant d'interagir avec la base de données.
-   `_logger` : Une instance de la classe `ILogger`, facilitant la journalisation dans toute notre application.
-   `_mapper` : Une instance de la classe `IMapper`, nous permettant d'effectuer un mapping d'objet à objet à l'aide d'AutoMapper.

Ensuite, nous mettrons à jour le constructeur de la classe `TodoServices` pour injecter ces dépendances :

```csharp
// Services/TodoServices.cs

// ...

public TodoServices(TodoDbContext context, ILogger<TodoServices> logger, IMapper mapper)
{
    _context = context;
    _logger = logger;
    _mapper = mapper;
}

// ...
```

Avec ces dépendances injectées, nous sommes maintenant prêts à implémenter les méthodes définies dans l'interface `ITodoServices`. Nous commencerons par la méthode `GetAllAsync` dans la section suivante.

## Étape 9 : Implémenter la méthode CreateTodoAsync dans la classe TodoServices

Maintenant, implémentons la méthode `CreateTodoAsync` dans la classe `TodoServices`. Cette méthode gérera la création de nouveaux éléments Todo dans notre base de données.

Accédez à la classe `TodoServices` et ajoutez le code suivant à la méthode `CreateTodoAsync` :

```csharp
// Services/TodoServices.cs

// ...

public async Task CreateTodoAsync(CreateTodoRequest request)
{
    try
    {
        var todo = _mapper.Map<Todo>(request);
        todo.CreatedAt = DateTime.UtcNow;
        _context.Todos.Add(todo);
        await _context.SaveChangesAsync();
    }
    catch (Exception ex)
    {
        _logger.LogError(ex, "An error occurred while creating the Todo item.");
        throw new Exception("An error occurred while creating the Todo item.");
    }
}

// ...
```

Voici une décomposition de la méthode `CreateTodoAsync` :

-   **Mapping** : Nous utilisons AutoMapper pour convertir l'objet `CreateTodoRequest` en une entité `Todo`.
-   **CreatedAt** : Nous définissons la propriété `CreatedAt` de l'entité `Todo` sur la date et l'heure UTC actuelles.
-   **Ajout à la base de données** : Nous ajoutons l'entité `Todo` au DbSet `Todos` dans notre contexte et enregistrons les modifications de manière asynchrone.
-   **Gestion des erreurs** : Nous capturons toutes les exceptions qui pourraient survenir pendant le processus, enregistrons l'erreur et lançons une nouvelle exception avec un message d'erreur descriptif.

La méthode `CreateTodoAsync` étant implémentée, nous pouvons maintenant créer de nouveaux éléments Todo dans notre base de données.

## Étape 10 : Implémenter la méthode GetAllAsync dans la classe de service

Ensuite, implémentons la méthode `GetAllAsync` dans la classe `TodoServices`. Cette méthode récupérera tous les éléments Todo de la base de données.

Accédez à la classe `TodoServices` et ajoutez le code suivant à la méthode `GetAllAsync` :

```csharp
// Services/TodoServices.cs

// ...


 // Récupérer tous les éléments TODO de la base de données 
 public async Task<IEnumerable<Todo>> GetAllAsync()
 {
     var todo= await _context.Todos.ToListAsync();
     if (todo == null)
     {
         throw new Exception(" No Todo items found");
     }
     return todo;

 }

// ...
```

Voici une décomposition de la méthode `GetAllAsync` :

-   **Récupération des éléments Todo** : Nous utilisons la méthode `ToListAsync` d'Entity Framework Core pour récupérer tous les éléments Todo de la base de données.
    
-   **Gestion des erreurs** : Si aucun élément Todo n'est trouvé, nous lançons une exception avec un message d'erreur descriptif.
    

Maintenant, votre classe de service devrait ressembler à ceci :

```csharp
using AutoMapper;
using Microsoft.EntityFrameworkCore;
using TodoAPI.AppDataContext;
using TodoAPI.Contracts;
using TodoAPI.Interface;
using TodoAPI.Models;

namespace TodoAPI.Services
{
    public class TodoServices : ITodoServices
    {
        private readonly TodoDbContext _context;
        private readonly ILogger<TodoServices> _logger;
        private readonly IMapper _mapper;

        public TodoServices(TodoDbContext context, ILogger<TodoServices> logger, IMapper mapper)
        {
            _context = context;
            _logger = logger;
            _mapper = mapper;
        }




        // Créer un Todo pour qu'il soit enregistré dans la base de données 

        public async Task CreateTodoAsync(CreateTodoRequest request)
        {
            try
            {
                var todo = _mapper.Map<Todo>(request);
                todo.CreatedAt = DateTime.Now;
                _context.Todos.Add(todo);
                await _context.SaveChangesAsync();
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "An error occurred while creating the todo item.");
                throw new Exception("An error occurred while creating the todo item.");
            }
        }

        public async Task<IEnumerable<Todo>> GetAllAsync()
        {
            var todo = await _context.Todos.ToListAsync();
            if (todo == null)
            {
                throw new Exception(" No Todo items found");
            }
            return todo;

        }
        public Task DeleteTodoAsync(Guid id)
        {
            throw new NotImplementedException();
        }

        // Récupérer tous les éléments TODO de la base de données 


        public Task<Todo> GetByIdAsync(Guid id)
        {
            throw new NotImplementedException();
        }

        public Task UpdateTodoAsync(Guid id, UpdateTodoRequest request)
        {
            throw new NotImplementedException();
        }
    }
}
```

Nous avons maintenant implémenté les méthodes `CreateTodoAsync` et `GetAllAsync` dans la classe `TodoServices`. Avant de procéder à l'implémentation des méthodes restantes, créons des routes pour notre API dans le dossier Controllers. Créons maintenant la classe TodoController.

## Étape 11 : Créer la classe TodoController

Dans ASP.NET Core, les contrôleurs sont responsables du traitement des requêtes HTTP entrantes et de l'envoi des réponses. Ils servent de point d'entrée pour notre API, définissant les routes et les actions avec lesquelles les clients peuvent interagir.

Créons un nouveau fichier nommé `TodoController.cs` dans le dossier `Controllers` et ajoutons le code suivant :

```csharp
using Microsoft.AspNetCore.Mvc;
using TodoAPI.Interface;

namespace TodoAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class TodoController : ControllerBase
    {
        private readonly ITodoServices _todoServices;

        public TodoController(ITodoServices todoServices)
        {
            _todoServices = todoServices;
        }

    }
}
```

La classe `TodoController` hérite de `ControllerBase`, une classe de base fournie par ASP.NET Core pour créer des contrôleurs. Nous avons également ajouté un préfixe de route `api/[controller]` au contrôleur, qui sera utilisé comme route de base pour toutes les actions du contrôleur.

## Étape 12 : Implémenter la méthode CreateTodoAsync dans la classe TodoController

Maintenant que nous avons notre classe Controller, implémentons la méthode `CreateTodoAsync` dans la classe `TodoController`. Cette méthode gérera la création de nouveaux éléments Todo dans notre base de données.

Accédez à la classe `TodoController` et ajoutez le code suivant à la méthode `CreateTodoAsync` :

```csharp
// Controllers/TodoController.cs

// ...
  [HttpPost]
  public async Task<IActionResult> CreateTodoAsync(CreateTodoRequest request)
  {
      if (!ModelState.IsValid)
      {
          return BadRequest(ModelState);
      }


      try
      {

          await _todoServices.CreateTodoAsync(request);
          return Ok(new { message = "Blog post successfully created" });

      }
      catch (Exception ex)
      {
          return StatusCode(500, new { message = "An error occurred while creating the  crating Todo Item", error = ex.Message });

      }
  }
  // ...
```

Voici une décomposition de la méthode `CreateTodoAsync` :

-   **Validation du modèle** : Nous vérifions si le modèle de requête est valide à l'aide de `ModelState.IsValid`. Si le modèle n'est pas valide, nous renvoyons une réponse `BadRequest` avec les erreurs d'état du modèle.
    
-   **Création d'un élément Todo** : Nous appelons la méthode `CreateTodoAsync` de l'interface `ITodoServices` pour créer un nouvel élément Todo dans la base de données.
    
-   **Réponse de succès** : Si l'élément Todo est créé avec succès, nous renvoyons une réponse `Ok` avec un message de succès.
    
-   **Gestion des erreurs** : Si une erreur survient pendant le processus de création, nous renvoyons une réponse `500 Internal Server Error` avec un message d'erreur.
    

Implémentons maintenant la méthode `GetAllAsync` dans la classe `TodoController`. Cette méthode récupérera tous les éléments Todo de la base de données.

Accédez à la classe `TodoController` et ajoutez le code suivant à la méthode `GetAllAsync` :

```csharp
// Controllers/TodoController.cs 

// ...

  [HttpGet]
  public async Task<IActionResult> GetAllAsync()
  {
      try
      {
          var todo = await _todoServices.GetAllAsync();
          if (todo == null || !todo.Any())
          {
              return Ok(new { message = "No Todo Items  found" });
          }
          return Ok(new { message = "Successfully retrieved all blog posts", data = todo });

      }
      catch (Exception ex)
      {
          return StatusCode(500, new { message = "An error occurred while retrieving all Tood it posts", error = ex.Message });


      }
  }

// ...
```

Voici une décomposition de la méthode `GetAllAsync` :

-   **Récupération des éléments Todo** : Nous appelons la méthode `GetAllAsync` de l'interface `ITodoServices` pour récupérer tous les éléments Todo de la base de données.
    
-   **Réponse de succès** : Si les éléments Todo sont récupérés avec succès, nous renvoyons une réponse `Ok` avec un message de succès et la liste des éléments Todo.
    
-   **Gestion des erreurs** : Si une erreur survient pendant le processus de récupération, nous renvoyons une réponse `500 Internal Server Error` avec un message d'erreur.
    

Maintenant, votre classe `TodoController` devrait ressembler à ceci :

```csharp
using Microsoft.AspNetCore.Mvc;
using TodoAPI.Contracts;
using TodoAPI.Interface;

namespace TodoAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class TodoController : ControllerBase
    {
        private readonly ITodoServices _todoServices;

        public TodoController(ITodoServices todoServices)
        {
            _todoServices = todoServices;
        }



// Création d'un nouvel élément Todo
[HttpPost]
  public async Task<IActionResult> CreateTodoAsync(CreateTodoRequest request)
  {
      if (!ModelState.IsValid)
      {
          return BadRequest(ModelState);
      }


      try
      {

          await _todoServices.CreateTodoAsync(request);
          return Ok(new { message = "Blog post successfully created" });

      }
      catch (Exception ex)
      {
          return StatusCode(500, new { message = "An error occurred while creating the  crating Todo Item", error = ex.Message });

      }
  }

    // Récupérer tous les éléments Todo

      [HttpGet]
  public async Task<IActionResult> GetAllAsync()
  {
      try
      {
          var todo = await _todoServices.GetAllAsync();
          if (todo == null || !todo.Any())
          {
              return Ok(new { message = "No Todo Items  found" });
          }
          return Ok(new { message = "Successfully retrieved all blog posts", data = todo });

      }
      catch (Exception ex)
      {
          return StatusCode(500, new { message = "An error occurred while retrieving all Tood it posts", error = ex.Message });


      }
  }

    }
}
```

À ce stade, nous avons implémenté les méthodes `CreateTodoAsync` et `GetAllAsync` dans la classe `TodoController`. Ces méthodes nous permettent de créer de nouveaux éléments Todo et de récupérer tous les éléments Todo de la base de données. Essayons de lancer l'application et voyons si tout fonctionne correctement.

Lancez l'application en exécutant la commande suivante :

```
dotnet run
```

Si vous voyez la sortie suivante, cela signifie que votre application fonctionne avec succès :

```
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: http://localhost:5086
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
info: Microsoft.Hosting.Lifetime[0]
      Hosting environment: Development
info: Microsoft.Hosting.Lifetime[0]
      Content root path: E:\Todo\TodoAPI4
```

Bien que nous utiliserons Postman dans Visual Studio Code pour effectuer des requêtes API, il est utile de noter que .NET 8 inclut une interface utilisateur Swagger intégrée. Cette fonctionnalité nous permet d'interagir avec nos points de terminaison API directement depuis un navigateur web. Pour accéder à l'interface Swagger, ouvrez votre navigateur et accédez à `https://localhost:5086/swagger/index.html`. Vous devriez voir une page similaire à celle ci-dessous :

![SwaggerUI](https://www.freecodecamp.org/news/content/images/2024/05/SwaggerUI.png) Cela indique que nous avons fait des progrès significatifs. Nous avons créé une API capable de créer et de récupérer des éléments Todo. Testons cela en essayant de créer un nouvel élément Todo à l'aide de notre API.

Ouvrez Postman et créez une nouvelle requête POST avec l'URL suivante : `https://localhost:5086/api/todo`. Définissez le corps de la requête sur l'objet JSON suivant :

```json
{
    "title": "Learn ASP.NET Core",
    "description": "Learn how to build web applications with ASP.NET Core",
    "dueDate": "2022-12-31T00:00:00",
    "priority": 5
}
```

Lors de l'exécution de cette requête, vous pourriez rencontrer une erreur. C'est parce que nous n'avons pas encore ajouté notre chaîne de connexion au fichier `appsettings.json`. Rectifions cela.

![PostmanError](https://www.freecodecamp.org/news/content/images/2024/05/PostmanError.png)

**Note** : L'erreur ci-dessus est due à l'absence de chaîne de connexion dans le fichier `appsettings.json`. Ajoutons la chaîne de connexion au fichier `appsettings.json`.

Avant de faire cela, configurons notre base de données SQL Server. Tout d'abord, ouvrez votre SQL Server Management Studio et vous devriez voir l'écran ci-dessous :

![SQLServerManagementStudio](https://www.freecodecamp.org/news/content/images/2024/05/SQLServerManagementStudio.png)

Pour vous connecter au serveur SQL, là où il est écrit `Server Name`, vous pouvez taper `localhost` ou `.` et cliquer sur le bouton `Connect`.

Après vous être connecté au serveur SQL, vous verrez l'écran suivant :

![SQLServerManagementStudio2](https://www.freecodecamp.org/news/content/images/2024/05/SQLServerManagementStudio2.png)

Allez maintenant dans votre fichier `appsettings.json` et ajoutez la chaîne de connexion suivante :

```json
//appsettings.json
{
  "DbSettings": {
    "ConnectionString": "Server=localhost;Database=TodoAPIDb;  Integrated Security=true;  TrustServerCertificate=true;"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft": "Warning",
      "Microsoft.Hosting.Lifetime": "Information"
    },
    "AllowedHosts": "*"
  }
}
```

Laissez-moi vous expliquer la chaîne de connexion ci-dessus :

-   `Server` : C'est le nom du serveur où la base de données est hébergée. Dans ce cas, nous utilisons `localhost` pour nous connecter à l'instance locale de SQL Server.
-   `Database` : C'est le nom de la base de données à laquelle nous voulons nous connecter. Nous l'avons définie sur `TodoAPIDb`.
-   `Integrated Security` : Ce paramètre spécifie que nous utilisons l'authentification Windows pour nous connecter à la base de données.
-   `TrustServerCertificate` : Ce paramètre spécifie que nous faisons confiance au certificat du serveur lors de la connexion à la base de données.

Nous devons maintenant enregistrer notre `Service` et `Iservices` dans le fichier `Program.cs`.

Ajoutez le service au fichier `Program.cs` :

```csharp
// Program.cs

// ...

builder.Services.AddScoped<ITodoServices, TodoServices>();

// ...
```

## Étape 13 : Implémenter les migrations et mettre à jour la base de données

Les migrations dans Entity Framework Core fournissent un mécanisme pour maintenir le schéma de la base de données synchronisé avec le modèle de données de l'application. Elles génèrent des scripts SQL qui peuvent être appliqués à la base de données pour refléter les modifications du modèle de données, éliminant ainsi le besoin de mises à jour manuelles du schéma de la base de données.

Pour créer une migration, assurez-vous d'être dans le répertoire racine de votre projet et exécutez la commande suivante dans le terminal :

```
dotnet ef migrations add InitialCreate
```

Une fois l'exécution réussie, vous verrez une sortie similaire à la suivante :

```
dotnet ef migrations add InitialCreate
Build started...
Build succeeded.
Done. To undo this action, use 'ef migrations remove'
```

Cette commande génère une nouvelle migration nommée `InitialCreate`, qui contient des scripts SQL dérivés des modifications de notre modèle de données. Un nouveau dossier nommé `Migrations` apparaîtra dans le répertoire de votre projet.

Pour appliquer la migration et mettre à jour la base de données, exécutez la commande suivante :

```
dotnet ef database update
```

Vous pourriez rencontrer une erreur comme celle-ci :

```
  at Microsoft.EntityFrameworkCore.Design.OperationExecutor.UpdateDatabase.<>c__DisplayClass0_0.<.ctor>b__0()
   at Microsoft.EntityFrameworkCore.Design.OperationExecutor.OperationBase.Execute(Action action)
Only the invariant culture is supported in globalization-invariant mode. See https://aka.ms/GlobalizationInvariantMode for more information. (Parameter 'name')
en-us is an invalid culture identifier.
```

Cette erreur indique que la culture `en-us` n'est pas prise en charge en mode invariant de globalisation. Pour résoudre ce problème, ouvrez le fichier `TodoAPI.csproj` et changez `<InvariantGlobalization>true</InvariantGlobalization>` en `<InvariantGlobalization>false</InvariantGlobalization>`.

Après avoir effectué ce changement, exécutez à nouveau la commande `dotnet ef database update`. Si la migration réussit, vous verrez une sortie similaire à la suivante :

```
Build started...
Build succeeded.
Applying migration '20240518180222_InitialCreate'.
Done.
```

Cela indique que la migration a été appliquée avec succès et que la base de données a été mise à jour avec les modifications de schéma nécessaires.

Félicitations ! Vous avez créé avec succès une migration et mis à jour le schéma de la base de données. Maintenant, testons notre API en créant un nouvel élément Todo à l'aide de Postman.

## Étape 14 : Vérifier votre API avec Postman

Avant de pouvoir interagir avec notre API, nous devons nous assurer que notre application est opérationnelle. Lancez l'application en exécutant la commande suivante dans le terminal :

```
dotnet run
```

L'application étant lancée, nous pouvons maintenant utiliser Postman pour envoyer des requêtes à notre API. Créons un nouvel élément Todo :

1.  Ouvrez Postman et créez une nouvelle requête.
2.  Définissez la méthode de requête sur `POST`.
3.  Entrez l'URL suivante : `https://localhost:5086/api/todo`.
4.  Dans l'onglet `Headers`, définissez le `Content-Type` sur `application/json`.
5.  Dans l'onglet `Body`, sélectionnez `raw` et entrez l'objet JSON suivant :

```json
{
    "title": "Learn ASP.NET Core",
    "description": "Learn how to build web applications with ASP.NET Core",
    "dueDate": "2022-12-31T00:00:00",
    "priority": 5
}
```

6.  Cliquez sur le bouton `Send` pour exécuter la requête.

Si la requête réussit, vous recevrez une réponse similaire à celle ci-dessous :

```json
{
    "message": "Todo item successfully created"
}
```

L'image ci-dessous illustre la création réussie d'un nouvel élément Todo à l'aide de Postman :

![PostmanSuccess](https://www.freecodecamp.org/news/content/images/2024/05/PostmanSuccess.png)

Maintenant que nous avons créé avec succès un nouvel élément Todo, récupérons tous les éléments Todo de la base de données à l'aide de notre API.

## Étape 15 : Récupérer tous les éléments Todo

Pour récupérer tous les éléments Todo de la base de données, suivez ces étapes :

1.  Ouvrez Postman et créez une nouvelle requête.
    
2.  Définissez la méthode de requête sur `GET`.
    
3.  Entrez l'URL suivante : `https://localhost:5086/api/todo`.
    
4.  Cliquez sur le bouton `Send` pour exécuter la requête.
    

Si la requête réussit, vous recevrez une réponse similaire à celle ci-dessous :

```json
   {
    "message": "Successfully retrieved all blog posts",
    "data": [
        {
            "id": "e9898d1b-9ad3-4482-ad65-08dc77664fab",
            "title": "string",
            "description": "string",
            "isComplete": false,
            "dueDate": "2024-05-18T16:52:22.054Z",
            "priority": 5,
            "createdAt": "2024-05-18T18:14:08.1755565+00:00",
            "updatedAt": "0001-01-01T00:00:00"
        }
    ]
}
```

L'image ci-dessous illustre la récupération réussie de tous les éléments Todo à l'aide de Postman :

![PostmanGetAll](https://www.freecodecamp.org/news/content/images/2024/05/PostmanGetAll.png)

Félicitations ! Vous avez créé avec succès une API capable de créer et de récupérer des éléments Todo. Cela marque la fin de notre projet d'API Todo. Vous avez appris à configurer un projet .NET Core, à définir des modèles, à créer un contexte de base de données, à implémenter une couche de service et à créer des points de terminaison API. Vous avez également appris à utiliser Postman pour interagir avec votre API et tester ses fonctionnalités.

Passons maintenant à la création des méthodes `GetByIdAsync`, `UpdateTodoAsync` et `DeleteTodoAsync` dans la classe `TodoServices` et la classe `TodoController`.

## Étape 16 : Implémenter la méthode GetByIdAsync

La méthode `GetByIdAsync` récupère un élément Todo spécifique par son `Id`. Nous implémenterons cette méthode dans les classes `TodoServices` et `TodoController`.

### La classe `TodoServices`

Dans la classe `TodoServices`, ajoutez le code suivant à la méthode `GetByIdAsync` :

```csharp
// Services/TodoServices.cs

public async Task<Todo> GetByIdAsync(Guid id)
{
    var todo = await _context.Todos.FindAsync(id);
    if (todo == null)
    {
        throw new KeyNotFoundException($"No Todo item with Id {id} found.");
    }
    return todo;
}
```

Cette méthode utilise la méthode `FindAsync` d'Entity Framework Core pour récupérer un élément Todo par son `Id`. Si aucun élément Todo n'est trouvé, elle lance une `KeyNotFoundException` avec un message d'erreur descriptif.

### La classe `TodoController`

Dans la classe `TodoController`, ajoutez le code suivant à la méthode `GetByIdAsync` :

```csharp
// Controllers/TodoController.cs

[HttpGet("{id:guid}")]
public async Task<IActionResult> GetByIdAsync(Guid id)
{
    try
    {
        var todo = await _todoServices.GetByIdAsync(id);
        if (todo == null)
        {
            return NotFound(new { message = $"No Todo item with Id {id} found." });
        }
        return Ok(new { message = $"Successfully retrieved Todo item with Id {id}.", data = todo });
    }
    catch (Exception ex)
    {
        return StatusCode(500, new { message = $"An error occurred while retrieving the Todo item with Id {id}.", error = ex.Message });
    }
}
```

Cette méthode appelle la méthode `GetByIdAsync` de l'interface `ITodoServices` pour récupérer un élément Todo par son `Id`. Si un élément Todo est récupéré avec succès, elle renvoie une réponse `Ok` avec un message de succès et l'élément Todo. Si une erreur survient pendant le processus de récupération, elle renvoie une réponse `500 Internal Server Error` avec un message d'erreur.

## Étape 17 : Implémenter la méthode UpdateTodoAsync

La méthode `UpdateTodoAsync` dans la classe `TodoServices` modifie un élément Todo existant dans la base de données. Implémentons cette méthode maintenant.

Accédez à la classe `TodoServices` et ajoutez le code suivant à la méthode `UpdateTodoAsync` :

```csharp
// Services/TodoServices.cs

// ...

 public async Task UpdateTodoAsync(Guid id, UpdateTodoRequest request)
 {
     try
     {
         var todo = await _context.Todos.FindAsync(id);
         if (todo == null)
         {
             throw new Exception($"Todo item with id {id} not found.");
         }

         if (request.Title != null)
         {
             todo.Title = request.Title;
         }

         if (request.Description != null)
         {
             todo.Description = request.Description;
         }

         if (request.IsComplete != null)
         {
             todo.IsComplete = request.IsComplete.Value;
         }

         if (request.DueDate != null)
         {
             todo.DueDate = request.DueDate.Value;
         }

         if (request.Priority != null)
         {
             todo.Priority = request.Priority.Value;
         }

         todo.UpdatedAt = DateTime.Now;

         await _context.SaveChangesAsync();
     }
     catch (Exception ex)
     {
         _logger.LogError(ex, $"An error occurred while updating the todo item with id {id}.");
         throw;
     }
 }

// ...
```

Voici une décomposition de la méthode `UpdateTodoAsync` :

-   **Récupération d'un élément Todo spécifique** : Nous utilisons la méthode `FindAsync` d'Entity Framework Core pour récupérer un élément Todo par son `Id`.
    
-   **Mise à jour de l'élément Todo** : Nous mettons à jour les propriétés de l'élément Todo en fonction des valeurs fournies dans l'objet `UpdateTodoRequest`.
    
-   **Gestion des erreurs** : Si aucun élément Todo n'est trouvé avec l' `Id` spécifié, nous lançons une exception avec un message d'erreur descriptif.
    

Implémentons maintenant la méthode `UpdateTodoAsync` dans la classe `TodoController`. Cette méthode modifiera un élément Todo existant dans la base de données.

Accédez à la classe `TodoController` et ajoutez le code suivant à la méthode `UpdateTodoAsync` :

```csharp
// Controllers/TodoController.cs

// ... 
   [HttpPut("{id:guid}")]

   public async Task<IActionResult> UpdateTodoAsync(Guid id, UpdateTodoRequest request)
   {

       if (!ModelState.IsValid)
       {
           return BadRequest(ModelState);
       }

       try
       {

           var todo = await _todoServices.GetByIdAsync(id);
           if (todo == null)
           {
               return NotFound(new { message = $"Todo Item  with id {id} not found" });
           }

           await _todoServices.UpdateTodoAsync(id, request);
           return Ok(new { message = $" Todo Item  with id {id} successfully updated" });

       }
       catch (Exception ex)
       {
           return StatusCode(500, new { message = $"An error occurred while updating blog post with id {id}", error = ex.Message });


       }


   }

// ...
```

Voici une décomposition de la méthode `UpdateTodoAsync` :

-   **Validation du modèle** : Nous vérifions si le modèle de requête est valide à l'aide de `ModelState.IsValid`. Si le modèle n'est pas valide, nous renvoyons une réponse `BadRequest` avec les erreurs d'état du modèle.
    
-   **Récupération d'un élément Todo spécifique** : Nous appelons la méthode `GetByIdAsync` de l'interface `ITodoServices` pour récupérer un élément Todo par son `Id`.
    
-   **Mise à jour de l'élément Todo** : Si l'élément Todo est trouvé, nous appelons la méthode `UpdateTodoAsync` de l'interface `ITodoServices` pour mettre à jour l'élément Todo.
    
-   **Réponse de succès** : Si l'élément Todo est mis à jour avec succès, nous renvoyons une réponse `Ok` avec un message de succès.
    
-   **Gestion des erreurs** : Si une erreur survient pendant le processus de mise à jour, nous renvoyons une réponse `500 Internal Server Error` avec un message d'erreur.
    

## Étape 18 : Implémenter la méthode DeleteTodoAsync

La méthode `DeleteTodoAsync` dans la classe `TodoServices` supprime un élément Todo de la base de données. Implémentons cette méthode maintenant.

Accédez à la classe `TodoServices` et ajoutez le code suivant à la méthode `DeleteTodoAsync` :

```csharp
// Services/TodoServices.cs

// ...


 public async Task DeleteTodoAsync(Guid id)
 {

     var todo = await _context.Todos.FindAsync(id);
     if(todo != null)
     {
          _context.Todos.Remove(todo);
         await _context.SaveChangesAsync();

     }
     else
     {
         throw new Exception($"No  item found with the id {id}");
     }


 }

// ...
```

Voici une décomposition de la méthode `DeleteTodoAsync` :

-   **Récupération d'un élément Todo spécifique** : Nous utilisons la méthode `FindAsync` d'Entity Framework Core pour récupérer un élément Todo par son `Id`.
    
-   **Suppression de l'élément Todo** : Si l'élément Todo est trouvé, nous le supprimons du DbSet `Todos` dans notre contexte et enregistrons les modifications de manière asynchrone.
    
-   **Gestion des erreurs** : Si aucun élément Todo n'est trouvé avec l' `Id` spécifié, nous lançons une exception avec un message d'erreur descriptif.
    

Implémentons maintenant la méthode `DeleteTodoAsync` dans la classe `TodoController`. Cette méthode supprimera un élément Todo de la base de données.

Accédez à la classe `TodoController` et ajoutez le code suivant à la méthode `DeleteTodoAsync` :

```csharp
// Controllers/TodoController.cs

// ...

 [HttpDelete("{id:guid}")]
 public async Task<IActionResult> DeleteTodoAsync(Guid id)
 {
     try
     {
         await _todoServices.DeleteTodoAsync(id);
         return Ok(new { message = $"Todo  with id {id} successfully deleted" });

     }
     catch (Exception ex)
     {
         return StatusCode(500, new { message = $"An error occurred while deleting Todo Item  with id {id}", error = ex.Message });

     }
 }



// ...
```

Voici une décomposition de la méthode `DeleteTodoAsync` :

-   **Suppression de l'élément Todo** : Nous appelons la méthode `DeleteTodoAsync` de l'interface `ITodoServices` pour supprimer un élément Todo par son `Id`.
    
-   **Réponse de succès** : Si l'élément Todo est supprimé avec succès, nous renvoyons une réponse `Ok` avec un message de succès.
    
-   **Gestion des erreurs** : Si une erreur survient pendant le processus de suppression, nous renvoyons une réponse `500 Internal Server Error` avec un message d'erreur.
    

Maintenant, votre classe `TodoServices` devrait ressembler à ceci :

```csharp
// Services/TodoServices.cs

using AutoMapper;
using Microsoft.EntityFrameworkCore;
using TodoAPI.AppDataContext;
using TodoAPI.Contracts;
using TodoAPI.Interface;
using TodoAPI.Models;

namespace TodoAPI.Services
{
    public class TodoServices : ITodoServices
    {
        private readonly TodoDbContext _context;
        private readonly ILogger<TodoServices> _logger;
        private readonly IMapper _mapper;

        public TodoServices(TodoDbContext context, ILogger<TodoServices> logger, IMapper mapper)
        {
            _context = context;
            _logger = logger;
            _mapper = mapper;
        }




        // Créer un Todo pour qu'il soit enregistré dans la base de données 

        public async Task CreateTodoAsync(CreateTodoRequest request)
        {
            try
            {
                var todo = _mapper.Map<Todo>(request);
                todo.CreatedAt = DateTime.Now;
                _context.Todos.Add(todo);
                await _context.SaveChangesAsync();
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "An error occurred while creating the todo item.");
                throw new Exception("An error occurred while creating the todo item.");
            }
        }


        public async Task<Todo> GetByIdAsync(Guid id)
        {
            var todo = await _context.Todos.FindAsync(id);
            if (todo == null)
            {
                throw new Exception($" No Items with {id} found ");
            }
            return todo;
        }

        public async Task UpdateTodoAsync(Guid id, UpdateTodoRequest request)
        {
            try
            {
                var todo = await _context.Todos.FindAsync(id);
                if (todo == null)
                {
                    throw new Exception($"Todo item with id {id} not found.");
                }

                if (request.Title != null)
                {
                    todo.Title = request.Title;
                }

                if (request.Description != null)
                {
                    todo.Description = request.Description;
                }

                if (request.IsComplete != null)
                {
                    todo.IsComplete = request.IsComplete.Value;
                }

                if (request.DueDate != null)
                {
                    todo.DueDate = request.DueDate.Value;
                }

                if (request.Priority != null)
                {
                    todo.Priority = request.Priority.Value;
                }

                todo.UpdatedAt = DateTime.Now;

                await _context.SaveChangesAsync();
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, $"An error occurred while updating the todo item with id {id}.");
                throw;
            }
        }
        public async Task<IEnumerable<Todo>> GetAllAsync()
        {
            var todo = await _context.Todos.ToListAsync();
            if (todo == null)
            {
                throw new Exception(" No Todo items found");
            }
            return todo;

        }
        public async Task DeleteTodoAsync(Guid id)
        {

            var todo = await _context.Todos.FindAsync(id);
            if (todo != null)
            {
                _context.Todos.Remove(todo);
                await _context.SaveChangesAsync();

            }
            else
            {
                throw new Exception($"No  item found with the id {id}");
            }


        }




    }
}
```

Maintenant, votre classe `TodoController` devrait ressembler à ceci :

```csharp
using Microsoft.AspNetCore.Mvc;
using TodoAPI.Contracts;
using TodoAPI.Interface;

namespace TodoAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class TodoController : ControllerBase
    {
        private readonly ITodoServices _todoServices;

        public TodoController(ITodoServices todoServices)
        {
            _todoServices = todoServices;
        }



        // Création d'un nouvel élément Todo
        [HttpPost]
        public async Task<IActionResult> CreateTodoAsync(CreateTodoRequest request)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }


            try
            {

                await _todoServices.CreateTodoAsync(request);
                return Ok(new { message = "Blog post successfully created" });

            }
            catch (Exception ex)
            {
                return StatusCode(500, new { message = "An error occurred while creating the  crating Todo Item", error = ex.Message });

            }
        }

        // Récupérer tous les éléments Todo

        [HttpGet]
        public async Task<IActionResult> GetAllAsync()
        {
            try
            {
                var todo = await _todoServices.GetAllAsync();
                if (todo == null || !todo.Any())
                {
                    return Ok(new { message = "No Todo Items  found" });
                }
                return Ok(new { message = "Successfully retrieved all blog posts", data = todo });

            }
            catch (Exception ex)
            {
                return StatusCode(500, new { message = "An error occurred while retrieving all Tood it posts", error = ex.Message });


            }
        }

        [HttpGet("{id:guid}")]
        public async Task<IActionResult> GetByIdAsync(Guid id)
        {
            try
            {

                var todo = await _todoServices.GetByIdAsync(id);
                if (todo == null)
                {
                    return NotFound(new { message = $"Now Todo item with id {id} not found" });

                }
                return Ok(new { message = $"Successfully retrieved  todo item with id {id}", data = todo });

            }
            catch (Exception ex)
            {
                return StatusCode(500, new { message = $"An error occurred while retrieving   todo item  with id {id}", error = ex.Message });

            }
        }



        [HttpPut("{id:guid}")]

        public async Task<IActionResult> UpdateTodoAsync(Guid id, UpdateTodoRequest request)
        {

            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            try
            {

                var todo = await _todoServices.GetByIdAsync(id);
                if (todo == null)
                {
                    return NotFound(new { message = $"Todo Item  with id {id} not found" });
                }

                await _todoServices.UpdateTodoAsync(id, request);
                return Ok(new { message = $" Todo Item  with id {id} successfully updated" });

            }
            catch (Exception ex)
            {
                return StatusCode(500, new { message = $"An error occurred while updating blog post with id {id}", error = ex.Message });


            }


        }


        [HttpDelete("{id:guid}")]
        public async Task<IActionResult> DeleteTodoAsync(Guid id)
        {
            try
            {
                await _todoServices.DeleteTodoAsync(id);
                return Ok(new { message = $"Todo  with id {id} successfully deleted" });

            }
            catch (Exception ex)
            {
                return StatusCode(500, new { message = $"An error occurred while deleting Todo Item  with id {id}", error = ex.Message });

            }
        }


    }
}
```

Maintenant que nous avons implémenté les méthodes `GetByIdAsync`, `UpdateTodoAsync` et `DeleteTodoAsync` dans les classes `TodoServices` et `TodoController`, nous pouvons tester notre API pour nous assurer que tout fonctionne comme prévu.

## Étape 19 : Tester vos points de terminaison API avec Postman

Avec notre application opérationnelle, nous pouvons maintenant tester tous nos points de terminaison API. Nous allons créer de nouveaux éléments Todo, récupérer tous les éléments Todo, récupérer un élément Todo spécifique par son `Id`, mettre à jour un élément Todo et supprimer un élément Todo à l'aide de Postman. Commençons par créer trois nouveaux éléments Todo.

Notez que nous créerons ces éléments Todo un par un, et non tous en même temps. Suivez ces étapes pour chaque élément Todo :

1.  Ouvrez Postman et créez une nouvelle requête.
2.  Définissez la méthode de requête sur `POST`.
3.  Entrez l'URL suivante : `http://localhost:5086/api/todo`.
4.  Dans l'onglet `Headers`, définissez le `Content-Type` sur `application/json`.
5.  Dans l'onglet `Body`, sélectionnez `raw` et entrez l'un des objets JSON suivants :

Pour le premier élément Todo :

```json
{
    "title": "Learn ASP.NET Core",
    "description": "Learn how to build web applications with ASP.NET Core",
    "dueDate": "2022-12-31T00:00:00",
    "priority": 2
}
```

Pour le deuxième élément Todo :

```json
{
    "title": "Learn C#",
    "description": "Learn how to build web applications with C#",
    "dueDate": "2022-12-31T00:00:00",
    "priority": 3
}
```

Pour le troisième élément Todo :

```json
{
    "title": "Learn SQL",
    "description": "Learn how to build web applications with SQL",
    "dueDate": "2022-12-31T00:00:00",
    "priority": 1
}
```

6.  Cliquez sur le bouton `Send` pour exécuter la requête pour chaque élément Todo.

Si chaque requête réussit, vous recevrez une réponse similaire à celle ci-dessous :

```json
{
    "message": "Todo item successfully created"
}
```

Cela indique que l'élément Todo a été créé avec succès. Répétez les étapes pour chaque élément Todo.

### Comment récupérer tous les éléments Todo

Pour récupérer tous les éléments Todo de la base de données, suivez ces étapes :

1.  Lancez Postman et initiez une nouvelle requête.
2.  Définissez la méthode HTTP sur `GET`.
3.  Saisissez l'URL suivante : `http://localhost:5086/api/todo`.
4.  Cliquez sur le bouton `Send` pour exécuter la requête.

L'image ci-dessous illustre une récupération réussie de tous les éléments Todo à l'aide de Postman :

![PostmanGetAll-1](https://www.freecodecamp.org/news/content/images/2024/05/PostmanGetAll-1.png)

### Comment récupérer un élément Todo spécifique par son Id

Pour récupérer un élément Todo spécifique à l'aide de son `Id`, suivez ces étapes :

1.  Lancez Postman et initiez une nouvelle requête.
2.  Définissez la méthode HTTP sur `GET`.
3.  Saisissez l'URL suivante : `http://localhost:5086/api/todo/{id}`, en remplaçant `{id}` par l' `Id` de l'élément Todo que vous souhaitez récupérer. Par exemple, `http://localhost:5086/api/todo/e9898d1b-9ad3-4482-ad65-08dc77664fab`.
4.  Cliquez sur le bouton `Send` pour exécuter la requête.

Une fois l'exécution réussie, vous recevrez une réponse similaire à celle ci-dessous :

```json
{
    "message": "Successfully retrieved  todo item with id e9898d1b-9ad3-4482-ad65-08dc77664fab",
    "data": {
        "id": "e9898d1b-9ad3-4482-ad65-08dc77664fab",
        "title": "string",
        "description": "string",
        "isComplete": false,
        "dueDate": "2024-05-18T16:52:22.054",
        "priority": 5,
        "createdAt": "2024-05-18T18:14:08.1755565",
        "updatedAt": "0001-01-01T00:00:00"
    }
}
```

L'image ci-dessous illustre la récupération réussie d'un élément Todo spécifique à l'aide de Postman :

![PostmanGetById](https://www.freecodecamp.org/news/content/images/2024/05/PostmanGetById.png))

### Comment mettre à jour un élément Todo

Dans notre modèle Todo, nous avons une propriété `isComplete` qui est initialement définie sur `false` lorsqu'un élément Todo est créé. Cette propriété est utilisée pour indiquer si une tâche a été terminée ou non. Pour marquer une tâche comme terminée, nous devons mettre à jour cette propriété sur `true`. Notez que nous ne pouvons mettre à jour qu'un seul élément Todo à la fois, et nous identifions l'élément à mettre à jour par son `Id`.

Récupérons tous les éléments Todo, sélectionnons-en un et mettons-le à jour en définissant la propriété `isComplete` sur `true`.

Suivez ces étapes pour mettre à jour un élément Todo :

1.  Lancez Postman et initiez une nouvelle requête.
2.  Définissez la méthode HTTP sur `PUT`.
3.  Saisissez l'URL suivante : `http://localhost:5086/api/todo/{id}`, en remplaçant `{id}` par l' `Id` de l'élément Todo que vous souhaitez mettre à jour. Par exemple, `http://localhost:5086/api/todo/e9898d1b-9ad3-4482-ad65-08dc77664fab`.
4.  Dans l'onglet `Headers`, définissez le `Content-Type` sur `application/json`.
5.  Dans l'onglet `Body`, sélectionnez `raw` et entrez l'objet JSON suivant :

```json
{
    "id": "21ebe2c2-79c0-45d4-4139-08dc789e3eb2",
    "title": "Learn C#",
    "description": "Learn how to build web applications with C#",
    "isComplete": true, // Définissez isComplete sur true
    "dueDate": "2022-12-31T00:00:00",
    "priority": 3,
    "createdAt": "2024-05-20T07:27:39.3730049+00:00",
    "updatedAt": "0001-01-01T00:00:00"
}
```

6.  Cliquez sur le bouton `Send` pour exécuter la requête.

Une fois l'exécution réussie, vous recevrez une réponse similaire à celle ci-dessous :

```json
{
    "message": "Todo Item with id 21ebe2c2-79c0-45d4-4139-08dc789e3eb2 successfully updated"
}
```

L'image ci-dessous illustre la mise à jour réussie d'un élément Todo à l'aide de Postman :

![PostmanUpdate](https://www.freecodecamp.org/news/content/images/2024/05/PostmanUpdate.png)

**Note** : La propriété `isComplete` de l'élément Todo a été mise à jour sur `true`. Désormais, lorsque vous récupérerez tous les éléments Todo de la base de données, vous verrez que la propriété `isComplete` est `true` pour l'élément Todo mis à jour.

Voyons maintenant comment supprimer un élément Todo de la base de données.

### Comment supprimer un élément Todo

Pour supprimer un élément Todo de la base de données, suivez ces étapes :

1.  Ouvrez Postman et créez une nouvelle requête.
2.  Définissez la méthode HTTP sur `DELETE`.
3.  Entrez l'URL suivante : `http://localhost:5086/api/todo/{id}`, en remplaçant `{id}` par l' `Id` de l'élément Todo que vous avez l'intention de supprimer. Par exemple, `http://localhost:5086/api/todo/e9898d1b-9ad3-4482-ad65-08dc77664fab`.
4.  Cliquez sur le bouton `Send` pour exécuter la requête.

Si la requête réussit, vous recevrez une réponse similaire à celle ci-dessous :

```json
{
    "message": "Todo item with id 21ebe2c2-79c0-45d4-4139-08dc789e3eb2 successfully deleted"
}
```

L'image ci-dessous illustre la suppression réussie d'un élément Todo à l'aide de Postman :

![PostmanDelete](https://www.freecodecamp.org/news/content/images/2024/05/PostmanDelete.png)

Bien joué ! Vous avez implémenté avec succès les méthodes `GetByIdAsync`, `UpdateTodoAsync` et `DeleteTodoAsync` dans les classes `TodoServices` et `TodoController`. Vous avez également vérifié vos points de terminaison API à l'aide de Postman pour vous assurer qu'ils fonctionnent comme prévu.

### Code source

L'intégralité du code source de ce projet est disponible dans le dépôt GitHub [TodoAPI][34]. Je vous encourage à explorer la base de code, à tester diverses fonctionnalités et à renforcer vos compétences dans la création d'API à l'aide d'ASP.NET Core 8.

## Conclusion

Dans ce guide, nous avons parcouru le processus de construction d'une API Todo robuste en utilisant la puissance d'ASP.NET Core 8. Nous avons initié notre projet à partir de zéro, en définissant méticuleusement les modèles essentiels qui forment l'épine dorsale de notre application Todo.

Nous avons ensuite créé un contexte de base de données, une étape cruciale qui a facilité notre interaction avec la base de données. Pour simplifier davantage cette interaction, nous avons implémenté une couche de service, en extrayant efficacement les complexités des opérations directes sur la base de données.

Ensuite, nous avons créé nos points de terminaison API. Ces points de terminaison servent de passerelles pour `créer`, `récupérer`, `mettre à jour` et `supprimer` des éléments Todo, fournissant ainsi une fonctionnalité complète à notre application.

La dernière étape de notre voyage a consisté à tester rigoureusement notre API à l'aide de Postman. Cela a permis de s'assurer que notre application était non seulement construite conformément à notre conception, mais qu'elle fonctionnait également comme prévu, fournissant un service fiable et efficace.

Pour conclure, il est important de se rappeler que les connaissances acquises ici constituent une base solide pour construire des API plus complexes et riches en fonctionnalités. Le voyage d'apprentissage et d'exploration ne s'arrête pas là – ce n'est que le début. Bon codage !

[1]: #heading-prerequis
[2]: #heading-comment-ameliorer-votre-experience-de-developpement-avec-les-extensions-visual-studio-code
[3]: #heading-objectifs-d-apprentissage
[4]: #heading-qu-est-ce-que-net-core
[5]: #heading-net-core-vs-net-framework
[6]: #heading-etape-1-configurer-le-repertoire-de-votre-projet
[7]: #heading-etape-2-etablir-la-structure-de-votre-projet
[8]: #heading-etape-3-creer-le-modele-todo
[9]: #heading-etape-4-configurer-le-contexte-de-base-de-donnees
[10]: #heading-etape-5-definir-les-objets-de-transfert-de-donnees-dto
[11]: #heading-etape-6-implementer-le-mapping-d-objets-pour-l-api-todo
[12]: #heading-etape-7-implementer-un-middleware-de-gestion-globale-des-exceptions
[13]: #heading-etape-8-implementer-la-couche-de-service-et-l-interface-de-service
[14]: #heading-etape-9-implementer-la-methode-createtodoasync-dans-la-classe-todoservices
[15]: #heading-etape-10-implementer-la-methode-getallasync-dans-la-classe-de-service
[16]: #heading-etape-11-creer-la-classe-todocontroller
[17]: #heading-etape-12-implementer-la-methode-createtodoasync-dans-la-classe-todocontroller
[18]: #heading-etape-13-implementer-les-migrations-et-mettre-a-jour-la-base-de-donnees
[19]: #heading-etape-14-verifier-votre-api-avec-postman
[20]: #heading-etape-15-recuperer-tous-les-elements-todo
[21]: #heading-etape-16-implementer-la-methode-getbyidasync
[22]: #heading-etape-17-implementer-la-methode-updatetodoasync
[23]: #heading-etape-18-implementer-la-methode-deletetodoasync
[24]: #heading-etape-19-tester-vos-points-de-terminaison-api-avec-postman
[25]: #heading-conclusion
[26]: https://dotnet.microsoft.com/download
[27]: https://code.visualstudio.com/download
[28]: https://visualstudio.microsoft.com/downloads/
[29]: https://www.postman.com/downloads/
[30]: https://www.microsoft.com/en-us/sql-server/sql-server-downloads
[31]: https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit
[32]: https://marketplace.visualstudio.com/items?itemName=adrianwilczynski.namespace
[33]: https://docs.microsoft.com/en-us/dotnet/csharp/
[34]: https://github.com/Clifftech123/TodoAPI