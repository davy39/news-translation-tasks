---
title: Utilisation d'Entity Framework Core avec MongoDB
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2024-07-29T14:45:20.343Z'
originalURL: https://freecodecamp.org/news/using-entity-framework-core-with-mongodb
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1721834746254/fb4a9197-8076-48a5-b402-116d8289863c.png
tags:
- name: MongoDB
  slug: mongodb
- name: youtube
  slug: youtube
seo_title: Utilisation d'Entity Framework Core avec MongoDB
seo_desc: 'Entity Framework Core is a popular ORM (Object-Relational Mapper) for .NET
  applications, allowing developers to work with databases using .NET objects. It
  can be used with many types of databases, including MongoDB.

  In this article, you will learn ho...'
---

Entity Framework Core est un ORM (Object-Relational Mapper) populaire pour les applications .NET, permettant aux développeurs de travailler avec des bases de données en utilisant des objets .NET. Il peut être utilisé avec de nombreux types de bases de données, y compris MongoDB.

Dans cet article, vous apprendrez comment utiliser Entity Framework Core avec MongoDB. Cet article couvre les bases, explique les avantages et fournit un tutoriel étape par étape. Que vous soyez nouveau dans MongoDB ou Entity Framework Core, ou que vous cherchiez simplement à intégrer ces outils dans vos projets .NET, ce guide vous aidera à combler le fossé entre les bases de données relationnelles et NoSQL.

L'article commence par une brève introduction à MongoDB ainsi qu'une introduction à Entity Framework Core de Microsoft. Ensuite, il couvre comment utiliser le fournisseur MongoDB EF Core. Après avoir passé en revue les détails techniques avec quelques exemples de base, vous créerez un projet complet avec MongoDB et Entity Framework Core afin de voir comment tout fonctionne ensemble. Le projet utilisera les données d'exemple de MongoDB Atlas pour créer un système de réservation de restaurant.

Il existe également une version vidéo de cet article que vous pouvez [regarder sur la chaîne YouTube de freeCodeCamp.org](https://youtu.be/fv2-A5e-KHA).

%[https://youtu.be/fv2-A5e-KHA] 

# Introduction à MongoDB

MongoDB est une base de données NoSQL populaire conçue pour gérer de grands volumes de données et offrir des performances élevées, une évolutivité et une flexibilité. Contrairement aux bases de données relationnelles traditionnelles, MongoDB stocke les données dans des documents flexibles, similaires à JSON. Cette approche orientée document permet le stockage de structures de données complexes de manière plus naturelle et intuitive.

Dans MongoDB, les données sont stockées dans des collections, qui sont similaires aux tables dans les bases de données relationnelles mais sans schéma fixe. Cela signifie que vous pouvez avoir des documents avec différentes structures dans la même collection. Cette flexibilité est l'un des principaux avantages de l'utilisation de MongoDB, en particulier lors de la gestion de données non structurées ou semi-structurées.

Prenons un exemple de document MongoDB. Imaginez que nous avons une collection appelée `users` qui stocke des informations sur les utilisateurs dans une application. Voici à quoi pourrait ressembler un document typique :

```json
{
    "_id": "12345",
    "name": "John Doe",
    "email": "johndoe@example.com",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    },
    "hobbies": ["reading", "travelling", "coding"]
}
```

Dans ce document, nous avons divers champs tels que `name`, `email`, `age`, et `address`. Le champ `address` lui-même est un document intégré contenant plusieurs sous-champs comme `street`, `city`, `state`, et `zip`. De plus, le champ `hobbies` est un tableau de chaînes.

Bien que cela ressemble à du JSON, MongoDB stocke les données dans un format binaire appelé BSON (Binary JSON). BSON étend le modèle JSON pour fournir des types de données supplémentaires, tels que des entiers, des flottants, des dates et des données binaires. Ce format binaire est optimisé pour les performances et la flexibilité, permettant à MongoDB de stocker et de récupérer efficacement les données.

Une autre caractéristique importante de MongoDB est sa capacité à évoluer horizontalement. Cela signifie que vous pouvez distribuer vos données sur plusieurs serveurs, ce qui facilite la gestion de grands ensembles de données et assure une haute disponibilité. MongoDB prend également en charge les requêtes riches, l'indexation et l'agrégation, ce qui en fait un outil puissant pour une large gamme d'applications.

Par exemple, vous pouvez effectuer une requête pour trouver tous les utilisateurs qui vivent dans une ville spécifique :

```json
db.users.find({ "address.city": "Anytown" })
```

Ou vous pouvez trouver les utilisateurs qui ont un hobby spécifique :

```json
db.users.find({ "hobbies": "coding" })
```

MongoDB est largement utilisé dans divers secteurs, du commerce électronique et de la gestion de contenu à l'analyse en temps réel et aux applications de l'Internet des objets (IoT). Sa flexibilité et son évolutivité en font un excellent choix pour les applications modernes qui doivent gérer des données diverses et dynamiques.

Maintenant que nous avons une compréhension de base de ce qu'est MongoDB et pourquoi il est populaire, passons à un autre outil essentiel de notre stack technique : Entity Framework Core de Microsoft.

# Introduction à Entity Framework Core de Microsoft

Entity Framework Core, souvent abrégé en EF Core, est un mappeur objet-base de données moderne pour .NET. Il permet aux développeurs de travailler avec une base de données en utilisant des objets .NET, éliminant ainsi le besoin de la plupart du code d'accès aux données que les développeurs doivent généralement écrire.

EF Core est une version légère, extensible et multiplateforme de la populaire technologie d'accès aux données Entity Framework (EF). Il prend en charge une variété de moteurs de base de données, y compris SQL Server, SQLite et MongoDB.

L'un des principaux avantages de l'utilisation d'EF Core est qu'il permet aux développeurs de travailler avec des données de manière plus intuitive et orientée objet. Au lieu d'écrire des requêtes SQL brutes, vous pouvez interagir avec votre base de données en utilisant LINQ (Language Integrated Query) et des classes fortement typées.

Prenons un exemple de base. Imaginez que nous avons une classe `Product` :

```csharp
public class Product
{
    public int ProductId { get; set; }
    public string Name { get; set; }
    public decimal Price { get; set; }
}
```

C'est assez simple avec seulement trois champs. En utilisant EF Core, vous pouvez créer une classe de contexte qui représente une session avec la base de données et inclut un `DbSet` pour chaque type d'entité que vous souhaitez interroger ou sauvegarder :

```csharp
public class AppDbContext : DbContext
{
    public DbSet<Product> Products { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)   
    {
        optionsBuilder.Use<Your_SQL_Database_function>("YourConnectionStringHere");
    }
}
```

Ce code définit une classe nommée `AppDbContext` qui hérite de la classe `DbContext` d'Entity Framework Core. Cette classe est utilisée pour interagir avec la base de données. À l'intérieur de cette classe, il y a une propriété `DbSet<Product>` appelée `Products`, qui représente une collection d'entités `Product` et correspond à une table nommée `Products` dans la base de données. La méthode `OnConfiguring` est substituée pour configurer la connexion à la base de données, vous pouvez spécifier diverses bases de données comme fournisseur de base de données. La méthode utilise un `optionsBuilder` pour établir la connexion avec un espace réservé pour la chaîne de connexion réelle à la base de données. Cette chaîne de connexion doit évidemment être remplacée par la vraie contenant les détails nécessaires pour se connecter à la base de données. Lorsque vous créez une instance de `AppDbContext` dans l'application, elle utilise cette configuration pour effectuer des opérations comme l'interrogation ou la sauvegarde d'entités `Product` dans la table `Products`.

Avec cette configuration, vous pouvez effectuer des opérations CRUD (Create, Read, Update, Delete) en utilisant EF Core. Par exemple, pour ajouter un nouveau produit à la base de données, vous pouvez utiliser ce code.

```csharp
using (var context = new AppDbContext())
{
    var product = new Product { Name = "Laptop", Price = 999.99M };
    context.Products.Add(product);
    context.SaveChanges();
}
```

Ce code montre comment ajouter un nouveau produit à la base de données en utilisant Entity Framework Core. Une instance de `AppDbContext` est créée, et dans ce contexte, un nouvel objet `Product` avec le nom "Laptop" et le prix 999.99 est instancié. Ce nouveau produit est ensuite ajouté à la collection `Products` gérée par le `AppDbContext`. Enfin, la méthode `SaveChanges` est appelée pour sauvegarder les modifications dans la base de données, insérant ainsi le nouveau produit dans la table `Products`.

Pour interroger les produits, vous pouvez utiliser LINQ :

```csharp
using (var context = new AppDbContext())
{
    var products = context.Products.Where(p => p.Price > 500).ToList();
    foreach (var product in products)
    {
        Console.WriteLine($"Product: {product.Name}, Price: {product.Price}");  
    }
}
```

Ce code montre comment interroger la base de données en utilisant Entity Framework Core. Une instance de `AppDbContext` est créée, et dans ce contexte, une requête est faite pour récupérer tous les produits avec un prix supérieur à 500. Les résultats sont stockés dans une liste appelée `products`. Ensuite, une boucle parcourt chaque produit dans la liste, imprimant le nom et le prix de chaque produit sur la console.

EF Core se charge de traduire ces requêtes LINQ en commandes SQL appropriées pour votre base de données, rendant l'accès aux données plus simple et plus maintenable.

EF Core prend également en charge des fonctionnalités avancées comme le suivi des modifications, le chargement paresseux et les migrations, qui vous aident à gérer les changements de schéma de base de données au fil du temps.

En résumé, EF Core est un ORM puissant qui simplifie l'accès aux données dans les applications .NET en vous permettant de travailler avec vos données en utilisant des objets .NET et LINQ. Son support pour plusieurs moteurs de base de données et son extensibilité en font un choix polyvalent pour une large gamme d'applications.

Ensuite, nous verrons comment le fournisseur MongoDB EF Core comble le fossé entre MongoDB et EF Core, nous permettant d'utiliser les motifs familiers d'EF Core avec une base de données MongoDB.

# Comment le fournisseur MongoDB EF Core comble le fossé

Le fournisseur MongoDB Entity Framework Core est un outil qui permet aux développeurs d'utiliser MongoDB avec Entity Framework Core (EF Core), combinant la flexibilité de MongoDB avec l'API familière et les motifs de conception d'EF Core. Ce fournisseur vous permet de travailler avec MongoDB en utilisant les mêmes méthodologies de code-first et de requêtes LINQ que vous utiliseriez avec des bases de données relationnelles, simplifiant le développement et réduisant la courbe d'apprentissage pour ceux qui sont déjà familiers avec EF Core.

Le fournisseur MongoDB EF Core comble le fossé entre MongoDB et EF Core en prenant en charge les opérations CRUD de base, les requêtes LINQ et les documents intégrés, entre autres fonctionnalités. Voici quelques capacités clés :

1. **Workflows Code-First** : Vous pouvez définir vos modèles de données en C# et utiliser EF Core pour générer le schéma MongoDB, plutôt que de commencer par le schéma de la base de données et de générer du code à partir de celui-ci. Cela est particulièrement utile pour les développeurs qui préfèrent gérer la structure de leur base de données via du code.
    
2. **Opérations CRUD** : Le fournisseur prend en charge les opérations de base create, read, update et delete. Par exemple, vous pouvez ajouter un nouvel enregistrement à la base de données en utilisant le même code que nous avons vu précédemment :
    
    ```csharp
    using (var context = new AppDbContext())
    {
        var product = new Product { Name = "Laptop", Price = 999.99M };
        context.Products.Add(product);
        context.SaveChanges();
    }
    ```
    
3. **Support des requêtes LINQ** : Vous pouvez utiliser LINQ pour effectuer des requêtes contre MongoDB, vous permettant de tirer parti de vos connaissances existantes en C# et .NET pour interagir avec la base de données.
    
    ```csharp
    using (var context = new AppDbContext())
    {
        var products = context.Products.Where(p => p.Price > 500).ToList();
        foreach (var product in products)
        {
            Console.WriteLine($"Product: {product.Name}, Price: {product.Price}");
        }
    }
    ```
    
4. **Suivi des modifications** : Les capacités de suivi des modifications d'EF Core sont prises en charge, permettant la détection et la sauvegarde automatiques des modifications apportées à vos entités de données.
    
5. **Documents intégrés** : Le fournisseur prend en charge les documents intégrés, vous permettant de stocker des données liées au sein d'un seul document, ce qui est un motif courant dans MongoDB.
    
6. **Mappage de classe et sérialisation** : Vos classes C# sont mappées aux collections MongoDB, avec prise en charge de divers types de données et paramètres de sérialisation pour garantir que les données sont stockées correctement.
    

# Modélisation des données et opérations CRUD utilisant MongoDB Atlas

Maintenant, nous allons passer en revue un exemple rapide sur la façon d'utiliser le fournisseur MongoDB EF Core. Mais bientôt, nous créerons un projet complet dans Visual Studio Code afin que vous puissiez voir tout cela en contexte.

Dans cette section, nous explorerons comment définir des modèles de données et effectuer des opérations CRUD (Create, Read, Update, Delete) en utilisant le fournisseur MongoDB Entity Framework Core (EF) avec MongoDB Atlas. Cette intégration vous permet de tirer parti de la flexibilité de MongoDB avec les motifs familiers d'EF Core.

#### Configuration de votre environnement

Pour commencer, vous devez ajouter les packages NuGet nécessaires à votre projet :

```bash
dotnet add package MongoDB.EntityFrameworkCore
```

Le package MS EF Core et le pilote C# MongoDB sont ajoutés comme dépendance lorsque vous ajoutez le package du fournisseur MongoDB EF Core. Ces packages permettent à votre application d'interagir avec MongoDB via EF Core, en utilisant le même contexte et les mêmes définitions d'entités que vous utiliseriez avec une base de données relationnelle.

#### Configuration de MongoDB Atlas

Avant de pouvoir effectuer des opérations CRUD, vous devez configurer un cluster MongoDB Atlas et connecter votre application à celui-ci.

Voici les étapes. Notez que nous allons les passer en revue en détail lorsque nous créerons le projet bientôt.

1. **Créer un compte MongoDB Atlas** : Inscrivez-vous pour un compte gratuit sur [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register?utm_campaign=freecodecamp_ef&utm_source=freecodecamp&utm_medium=referral).
    
2. **Créer un cluster** : Configurez un nouveau cluster. MongoDB Atlas propose un niveau gratuit qui est parfait pour le développement et les applications à petite échelle.
    
3. **Obtenir la chaîne de connexion** : Obtenez votre chaîne de connexion depuis le tableau de bord MongoDB Atlas. Elle ressemblera à quelque chose comme ceci :
    
    ```plaintext
    mongodb+srv://<username>:<password>@cluster0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
    ```
    

#### Définition du modèle de données

Définissez une classe à utiliser comme modèle pour votre entité. Pour cet exemple, nous allons créer une classe `Customer` :

```csharp
public class Customer
{
    public ObjectId Id { get; set; }
    public String Name { get; set; }
    public String Order { get; set; }
}
```

Cette classe `Customer` représente la structure des documents stockés dans la collection MongoDB.

#### Créer une classe de contexte de base de données

Pour commencer à utiliser Entity Framework Core, créez une classe de contexte qui dérive de DBContext. L'instance de la classe dérivée de `DBContext` représente une session de base de données et est utilisée pour interroger et sauvegarder des instances de vos entités.

La classe `DBContext` expose des propriétés `DBSet` qui spécifient les entités avec lesquelles vous pouvez interagir lors de l'utilisation de ce contexte.

Cet exemple crée une instance d'une classe dérivée de `DBContext` et spécifie l'objet `Customer` comme propriété `DBSet` :

```csharp
public class MyDbContext : DbContext
{
    public DbSet<Customer> Customers { get; init; }

    public MyDbContext(DbContextOptions options)
        : base(options)
    {
    }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);
        modelBuilder.Entity<Customer>().ToCollection("customers");
    }
}
```

#### Workflow Code-First

Avec le fournisseur MongoDB EF, vous pouvez utiliser un workflow code-first. Cela signifie que vous définissez vos classes en premier, et EF Core gérera la création et la gestion du schéma MongoDB sous-jacent. Cela est particulièrement utile pour MongoDB, qui n'impose pas de schéma, permettant des structures de données flexibles et dynamiques.

**Utiliser MongoDB**

Une fois que nous avons créé une classe `DBContext`, nous devons construire un objet `DbContextOptionsBuilder` et appeler sa méthode `UseMongoDB()`. Cette méthode prend deux paramètres : une instance `MongoClient` et le nom de la base de données qui stocke les collections avec lesquelles vous travaillez.

La méthode `UseMongoDB()` retourne un objet `DbContextOptions`. Passez la propriété `Options` de cet objet au constructeur de votre classe `DBContext`.

```csharp
var mongoClient = new MongoClient("<Your MongoDB Connection URI>");

var dbContextOptions =
    new DbContextOptionsBuilder<MyDbContext>().UseMongoDB(mongoClient, "<Database Name");  

var db = new MyDbContext(dbContextOptions.Options);
```

### Opérations CRUD

Maintenant, voyons comment coder les opérations CRUD. Nous allons nous concentrer sur chaque opération individuellement.

#### Opération de création

Pour créer un nouveau document dans MongoDB, vous utilisez la méthode `Add` sur le `DbSet` et appelez `SaveChanges`. Voici un exemple de création d'un nouveau client :

```csharp
using (var context = new MyDbContext(options))
{
    var customer = new Customer { Name = "Beau Carnes", Order = "Laptop" };
    context.Customers.Add(customer);
    context.SaveChanges();
}
```

Ce code crée une nouvelle instance de `Customer` et l'ajoute à la collection `Customers`. La méthode `SaveChanges` sauvegarde le nouveau client dans la base de données MongoDB.

#### Opération de lecture

Pour lire des documents à partir de la collection MongoDB, vous pouvez utiliser des requêtes LINQ sur le `DbSet`. Voici un exemple de récupération de tous les clients :

```csharp
using (var context = new MyDbContext(options))
{
    var customers = context.Customers.ToList();
    foreach (var customer in customers)
    {
        Console.WriteLine($"Customer: {customer.Name}, Order: {customer.Order}"); 
    }
}
```

Ce code récupère tous les clients de la collection `Customers` et imprime leurs détails.

#### Opération de mise à jour

Pour mettre à jour un document existant, vous récupérez le document, modifiez ses propriétés et appelez `SaveChanges`. Voici un exemple de mise à jour de la commande d'un client :

```csharp
using (var context = new MyDbContext(options))
{
    var customer = context.Customers.FirstOrDefault(c => c.Name == "Beau Carnes"); 
    if (customer != null)
    {
        customer.Order = "Smartphone";
        context.SaveChanges();
    }
}
```

Ce code trouve le client nommé "Beau Carnes" et met à jour sa commande en "Smartphone".

#### Opération de suppression

Pour supprimer un document, vous récupérez le document, le supprimez du `DbSet` et appelez `SaveChanges`. Voici un exemple de suppression d'un client :

```csharp
using (var context = new MyDbContext(options))
{
    var customer = context.Customers.FirstOrDefault(c => c.Name == "Beau Carnes"); 
    if (customer != null)
    {
        context.Customers.Remove(customer);
        context.SaveChanges();
    }
}
```

Ce code trouve le client nommé "Beau Carnes" et le supprime de la collection `Customers`.

#### Suivi des modifications

Les capacités de suivi des modifications d'EF Core sont entièrement prises en charge, permettant des mises à jour efficaces des documents. Lorsque vous modifiez une entité et appelez `SaveChanges`, EF Core générera les commandes MongoDB nécessaires pour mettre à jour uniquement les champs modifiés.

En utilisant le fournisseur MongoDB EF, vous pouvez intégrer de manière transparente le modèle de document flexible de MongoDB avec les capacités robustes d'ORM d'EF Core, fournissant un ensemble d'outils puissant pour les développeurs .NET afin de construire des applications modernes.

# Tutoriel

Maintenant, mettons tout cela ensemble et créons un système de réservation de restaurant.

## Prérequis

Pour suivre ce tutoriel, vous aurez besoin de quelques éléments :

* .NET 7.0.
    
* Connaissance de base d'ASP.NET MVC et de C#.
    
* Compte gratuit [**MongoDB Atlas et cluster de niveau gratuit**.](https://www.mongodb.com/try)
    

## Créer le projet

ASP.NET Core est un framework web très flexible, permettant de créer différents types d'applications web qui ont des différences mineures en termes d'interface utilisateur ou de structure. Pour ce tutoriel, nous allons créer un projet MVC qui utilisera des fichiers statiques et des contrôleurs. Il existe d'autres types de front-end que vous pourriez utiliser, comme React, mais MVC avec des vues .cshtml est le plus couramment utilisé. Pour créer le projet, nous allons utiliser l'interface de ligne de commande .NET :

```plaintext
dotnet new mvc -o RestRes
```

Parce que nous avons utilisé l'interface de ligne de commande, bien que ce soit plus facile, elle ne crée que le fichier csproj et non le fichier solution qui nous permet de l'ouvrir dans Visual Studio, donc nous allons corriger cela.

```plaintext
cd RestRes
dotnet new sln
dotnet sln .\RestRes.sln add .\RestRes.csproj
```

## Ajouter les packages NuGet

Maintenant que nous avons créé le nouveau projet, nous allons ajouter les packages NuGet requis. En utilisant soit le gestionnaire de packages NuGet, soit la commande .NET CLI ci-dessous, ajoutez le package MongoDB MongoDB.EntityFrameworkCore.

```plaintext
dotnet add package MongoDB.EntityFrameworkCore
```

## Créer les modèles

Avant de commencer à implémenter les nouveaux packages que nous venons d'ajouter, nous devons créer les modèles qui représentent les entités que nous voulons dans notre système de réservation de restaurant, qui seront bien sûr stockées dans MongoDB Atlas sous forme de documents. Dans les sous-sections suivantes, nous créerons les modèles suivants :

* Restaurant
    
* Réservation
    
* MongoDBSettings
    

### Restaurant

Tout d'abord, nous devons créer notre modèle de restaurant qui représentera les restaurants disponibles pour être réservés dans notre système.

1. Créez un nouveau fichier dans le dossier Models appelé Restaurant.cs.
    
2. Ajoutez le code suivant :
    

```csharp
using MongoDB.Bson;
using MongoDB.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations;


namespace RestRes.Models
{
    [Collection("restaurants")]    
    public class Restaurant
    {
       
        public ObjectId Id { get; set; }
       
        [Required(ErrorMessage = "Vous devez fournir un nom")]
        [Display(Name = "Nom")]
        public string? name { get; set; }

      
        [Required(ErrorMessage = "Vous devez ajouter un type de cuisine")]
        [Display(Name = "Cuisine")]
        public string? cuisine { get; set; }


        [Required(ErrorMessage = "Vous devez ajouter le quartier du restaurant")]
        public string? borough { get; set; }

    }
}
```

L'attribut de collection avant la classe indique à l'application quelle collection dans la base de données nous utilisons. Cela nous permet d'avoir des noms ou des capitalisations différents entre notre classe et notre collection si nous le souhaitons.

### Réservation

Nous devons également créer une classe de réservation pour représenter toute réservation que nous prenons dans notre système.

1. Créez un nouveau fichier dans le dossier Models appelé Reservation.cs.
    
2. Ajoutez le code suivant :
    

```csharp
using MongoDB.Bson;
using MongoDB.EntityFrameworkCore;
using System.ComponentModel.DataAnnotations;


namespace RestRes.Models
{
    [Collection("reservations")]
    public class Reservation
    {
        public ObjectId Id { get; set; }


        public ObjectId RestaurantId { get; set; }


        public string? RestaurantName { get; set; }

        [Required(ErrorMessage = "La date et l'heure sont requises pour effectuer cette réservation")]
        [Display(Name = "Date")]
        public DateTime date { get; set; }

    }
}
```

### MongoDBSettings

Bien qu'il ne s'agira pas d'un document dans notre base de données, nous avons besoin d'une classe de modèle pour stocker nos paramètres liés à MongoDB afin qu'ils puissent être utilisés dans toute l'application.

1. Créez un autre fichier dans Models appelé MongoDBSettings.cs.
    
2. Ajoutez le code suivant :
    

```csharp
namespace RestRes.Models
{
  public class MongoDBSettings
  {
      public string AtlasURI { get; set; }
      public string DatabaseName { get; set; }
  }
}
```

## Configuration d'EF Core

C'est la partie excitante. Nous allons commencer à implémenter EF Core et à tirer parti du nouveau fournisseur MongoDB. Si vous êtes habitué à travailler avec EF Core, certaines de ces étapes vous seront familières.

### RestaurantReservationDbContext

1. Créez un dossier Services, puis créez un fichier appelé RestaurantReservationDbContext.cs.
    
2. Remplacez le code à l'intérieur du namespace par le suivant :
    

```csharp
using Microsoft.EntityFrameworkCore;
using RestRes.Models;

namespace RestRes.Services
{
    public class RestaurantReservationDbContext : DbContext
    {
        public DbSet<Restaurant> Restaurants { get; init; }      


        public DbSet<Reservation> Reservations { get; init; }


        public RestaurantReservationDbContext(DbContextOptions options)
        : base(options)
        {
        }


        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);


            modelBuilder.Entity<Restaurant>();
            modelBuilder.Entity<Reservation>();
        }
    }
}
```

Si vous êtes habitué à EF Core, cela vous sera familier. La classe étend le DbContext et nous créons des propriétés DbSet qui stockent les modèles qui seront également présents dans la base de données. Nous substituons également la méthode OnModelCreating. Vous remarquerez que contrairement à l'utilisation de SQL Server, nous n'appelons pas .ToTable(). Nous pourrions appeler ToCollection à la place, mais cela n'est pas requis ici car nous spécifions la collection en utilisant des attributs sur les classes.

### Ajouter la chaîne de connexion et les détails de la base de données à appsettings

Plus tôt, nous avons créé un modèle MongoDBSettings, et maintenant nous devons ajouter les valeurs auxquelles les propriétés sont mappées dans notre appsettings.

1. Dans appsettings.json et appsettings.Development.json, ajoutez la nouvelle section suivante :
    
    ```csharp
     "MongoDBSettings": {
       "AtlasURI": "mongodb+srv://<username>:<password>@<url>",
       "DatabaseName": "restaurants"
     }
    ```
    
2. Remplacez l'URI Atlas par votre propre chaîne de connexion depuis Atlas.
    

### Mise à jour de program.cs

Maintenant que nous avons configuré nos modèles et DbContext, il est temps de les ajouter à notre fichier program.cs.

Après la ligne existante [`builder.Services`](http://builder.Services)`.AddControllersWithViews();`, ajoutez le code suivant :

```csharp
var mongoDBSettings = builder.Configuration.GetSection("MongoDBSettings").Get<MongoDBSettings>();
builder.Services.Configure<MongoDBSettings>(builder.Configuration.GetSection("MongoDBSettings"));

builder.Services.AddDbContext<RestaurantReservationDbContext>(options =>
options.UseMongoDB(mongoDBSettings.AtlasURI ?? "", mongoDBSettings.DatabaseName ?? ""));
```

## Création des services

Maintenant, il est temps d'ajouter les services que nous utiliserons pour communiquer avec la base de données via le RestaurantBookingDbContext que nous avons créé. Pour chaque service, nous créerons une interface et la classe qui l'implémente.

### IRestaurantService et RestaurantService

La première interface et service que nous implémenterons est pour effectuer les opérations CRUD sur la collection des restaurants. Cela est connu sous le nom de modèle de dépôt. Vous pouvez voir des personnes interagir directement avec le DbContext. Mais la plupart des gens utilisent ce modèle, c'est pourquoi nous l'incluons ici.

1. Si vous ne l'avez pas déjà fait, créez un dossier Services pour stocker nos nouvelles classes.
    
2. Créez une interface IRestaurantService et ajoutez le code suivant pour les méthodes que nous implémenterons :
    

```csharp
using MongoDB.Bson;
using RestRes.Models;

namespace RestRes.Services
{
    public interface IRestaurantService
    {
        IEnumerable<Restaurant> GetAllRestaurants();
        Restaurant? GetRestaurantById(ObjectId id);

        void AddRestaurant(Restaurant newRestaurant);

        void EditRestaurant(Restaurant updatedRestaurant);

        void DeleteRestaurant(Restaurant restaurantToDelete);
    }
}
```

1. Créez un fichier de classe RestaurantService.
    
2. Mettez à jour la déclaration de la classe RestaurantService pour qu'elle implémente l'IRestaurantService que nous venons de créer :
    

```csharp
using Microsoft.EntityFrameworkCore;
using MongoDB.Bson;
using MongoDB.Driver;
using RestRes.Models;

namespace RestRes.Services
{
  public class RestaurantService : IRestaurantService
  {
    private readonly RestaurantReservationDbContext _restaurantDbContext;
    public RestaurantService(RestaurantReservationDbContext restaurantDbContext)
    {
        _restaurantDbContext = restaurantDbContext;
    }

    public void AddRestaurant(Restaurant restaurant)
    {
      _restaurantDbContext.Restaurants.Add(restaurant);

      _restaurantDbContext.ChangeTracker.DetectChanges();
      Console.WriteLine(_restaurantDbContext.ChangeTracker.DebugView.LongView);

      _restaurantDbContext.SaveChanges();
    }

    public void DeleteRestaurant(Restaurant restaurant)
    {
      var restaurantToDelete = _restaurantDbContext.Restaurants.Where(c => c.Id == restaurant.Id).FirstOrDefault();

      if(restaurantToDelete != null) {
          _restaurantDbContext.Restaurants.Remove(restaurantToDelete);
        _restaurantDbContext.ChangeTracker.DetectChanges();
          Console.WriteLine(_restaurantDbContext.ChangeTracker.DebugView.LongView);
          _restaurantDbContext.SaveChanges();
          }
        else {
            throw new ArgumentException("Le restaurant à supprimer est introuvable.");
        }
    }

    public void EditRestaurant(Restaurant restaurant)
    {
          var restaurantToUpdate = _restaurantDbContext.Restaurants.FirstOrDefault(c => c.Id == restaurant.Id);

        if(restaurantToUpdate != null)
        {                
            restaurantToUpdate.name = restaurant.name;
            restaurantToUpdate.cuisine = restaurant.cuisine;
            restaurantToUpdate.borough = restaurant.borough;

            _restaurantDbContext.Restaurants.Update(restaurantToUpdate);

            _restaurantDbContext.ChangeTracker.DetectChanges();
            Console.WriteLine(_restaurantDbContext.ChangeTracker.DebugView.LongView);

            _restaurantDbContext.SaveChanges();
                
        }
      else
        {
            throw new ArgumentException("Le restaurant à mettre à jour est introuvable. ");
        }
    }        

    public IEnumerable<Restaurant> GetAllRestaurants()
    {
      return _restaurantDbContext.Restaurants.OrderByDescending(c => c.Id).Take(20).AsNoTracking().AsEnumerable<Restaurant>();
    }

    public Restaurant? GetRestaurantById(ObjectId id)
    {
      return _restaurantDbContext.Restaurants.FirstOrDefault(c  => c.Id == id);
    }
  }

}
```

### IReservationService et ReservationService

Ensuite, nous avons notre IReservationService et ReservationService.

Créez l'interface IReservationService et ajoutez les méthodes suivantes :

```csharp
using MongoDB.Bson;
using RestRes.Models;

namespace RestRes.Services
{
    public interface IReservationService
    {
        IEnumerable<Reservation> GetAllReservations();
        Reservation? GetReservationById(ObjectId id);

        void AddReservation(Reservation newReservation);

        void EditReservation(Reservation updatedReservation);

        void DeleteReservation(Reservation reservationToDelete);
    }
}
```

Créez la classe ReservationService, et remplacez votre classe par le code suivant qui implémente toutes les méthodes :

```csharp
using Microsoft.EntityFrameworkCore;
using MongoDB.Bson;
using RestRes.Models;

namespace RestRes.Services
{
    public class ReservationService : IReservationService
    {
        private readonly RestaurantReservationDbContext _restaurantDbContext;

        public ReservationService(RestaurantReservationDbContext restaurantDbContext)
        {
            _restaurantDbContext = restaurantDbContext;
        }
        public void AddReservation(Reservation newReservation)
        {
            var bookedRestaurant = _restaurantDbContext.Restaurants.FirstOrDefault(c => c.Id == newReservation.RestaurantId);
            if (bookedRestaurant == null)
            {
                throw new ArgumentException("Le restaurant à réserver est introuvable.");
            }

            newReservation.RestaurantName = bookedRestaurant.name;

            _restaurantDbContext.Reservations.Add(newReservation);

            _restaurantDbContext.ChangeTracker.DetectChanges();
            Console.WriteLine(_restaurantDbContext.ChangeTracker.DebugView.LongView);

            _restaurantDbContext.SaveChanges();
        }

        public void DeleteReservation(Reservation reservation)
        {
            var reservationToDelete = _restaurantDbContext.Reservations.FirstOrDefault(b => b.Id == reservation.Id);

            if(reservationToDelete != null)
            {
                _restaurantDbContext.Reservations.Remove(reservationToDelete);

                _restaurantDbContext.ChangeTracker.DetectChanges();
                Console.WriteLine(_restaurantDbContext.ChangeTracker.DebugView.LongView);

                _restaurantDbContext.SaveChanges();
            }
            else
            {
                throw new ArgumentException("La réservation à supprimer est introuvable.");
            }
        }

        public void EditReservation(Reservation updatedReservation)
        {
           var reservationToUpdate = _restaurantDbContext.Reservations.FirstOrDefault(b => b.Id == updatedReservation.Id);
           
            
            if (reservationToUpdate != null)
            {               
                reservationToUpdate.date = updatedReservation.date;

                _restaurantDbContext.Reservations.Update(reservationToUpdate);

                _restaurantDbContext.ChangeTracker.DetectChanges();
                _restaurantDbContext.SaveChanges();

                Console.WriteLine(_restaurantDbContext.ChangeTracker.DebugView.LongView);
            }  
            else 
            { 
                throw new ArgumentException("La réservation à mettre à jour est introuvable");
            }
            
        }

        public IEnumerable<Reservation> GetAllReservations()
        {
            return _restaurantDbContext.Reservations.OrderBy(b => b.date).Take(20).AsNoTracking().AsEnumerable<Reservation>();
        }

        public Reservation? GetReservationById(ObjectId id)
        {
            return _restaurantDbContext.Reservations.AsNoTracking().FirstOrDefault(b => b.Id == id);
        }
        
    }
}
```

Ce code est très similaire au code de la classe RestaurantService mais pour les réservations.

### Ajout au conteneur d'injection de dépendances

La dernière étape pour les services est de les ajouter au conteneur d'injection de dépendances.

Dans Program.cs, ajoutez le code suivant après le code que nous avons ajouté précédemment :

```csharp
builder.Services.AddScoped<IRestaurantService, RestaurantService>();
builder.Services.AddScoped<IReservationService, ReservationService>();
```

## Création des modèles de vue

Avant d'implémenter le front-end, nous devons ajouter les modèles de vue qui serviront de messager entre notre front-end et notre back-end lorsque cela est nécessaire. Même si notre application est assez simple, l'implémentation du modèle de vue est toujours une bonne pratique car elle aide à découpler les pièces de l'application.

### RestaurantListViewModel

Le premier que nous ajouterons est le RestaurantListViewModel. Celui-ci sera utilisé comme modèle dans notre page Razor plus tard pour lister les restaurants dans notre base de données.

1. Créez un nouveau dossier à la racine du projet appelé ViewModels.
    
2. Ajoutez un nouveau fichier appelé RestaurantListViewModel.cs.
    
3. Ajoutez le code suivant :
    

```csharp
using RestRes.Models;

namespace RestRes.ViewModels
{
    public class RestaurantListViewModel
    {        
        public IEnumerable<Restaurant>? Restaurants { get; set; }
    }
}
```

### RestaurantAddViewModel

Nous voulons également un modèle de vue qui peut être utilisé par la vue Add que nous ajouterons plus tard.

1. Dans le dossier ViewModels, créez un nouveau fichier appelé RestaurantAddViewMode.cs.
    
2. Ajoutez :
    

```csharp
using RestRes.Models;

namespace RestRes.ViewModels
{
    public class RestaurantAddViewModel
    {
        public Restaurant? Restaurant { get; set; } 
    }
}
```

### ReservationListViewModel

Maintenant, nous voulons faire quelque chose de très similaire pour les réservations, en commençant par ReservationListViewModel.

1. Créez un nouveau fichier dans le dossier ViewModels appelé ReservationListViewModel.cs.
    
2. Ajoutez :
    

```csharp
using RestRes.Models;

namespace RestRes.ViewModels
{
    public class ReservationListViewModel
    {
        public IEnumerable<Reservation>? Reservations { get; set; }
    }
}
```

### ReservationAddViewModel

Enfin, nous avons notre ReservationAddViewModel.

Créez le fichier et ajoutez ce code :

```csharp
using RestRes.Models;

namespace RestRes.ViewModels
{
    public class ReservationAddViewModel
    {
        public Reservation? Reservation { get; set; }
    }
}
```

### Ajout à \_ViewImports

Plus tard, nous ajouterons des références à nos modèles et modèles de vue dans les vues. Pour que l'application sache ce qu'ils sont, nous devons ajouter des références à eux dans le fichier \_ViewImports.cshtml à l'intérieur du dossier Views.

Il y aura déjà certaines références, y compris TagHelpers, donc nous voulons ajouter des références à nos dossiers .Models et .ViewModels. Donc le haut du fichier devrait ressembler à ceci :

```csharp
@using RestRes
@using RestRes.Models
@using RestRes.ViewModels
```

## Création des contrôleurs

Maintenant que nous avons l'implémentation backend et les modèles de vue auxquels nous ferons référence, nous pouvons commencer à travailler vers le front-end. Nous allons créer deux contrôleurs : un pour Restaurant et un pour Reservation.

### RestaurantController

Le premier contrôleur que nous ajouterons est pour le restaurant.

1. À l'intérieur du dossier Controllers existant, ajoutez un nouveau fichier de contrôleur appelé RestaurantController.cs. Si vous utilisez Visual Studio, utilisez le modèle de contrôleur MVC - contrôleur vide.
    
2. Ajoutez ce code :
    

```csharp
using Microsoft.AspNetCore.Mvc;
using MongoDB.Bson;
using RestRes.Models;
using RestRes.Services;
using RestRes.ViewModels;

namespace RestRes.Controllers
{
    public class RestaurantController : Controller
    {
        private readonly IRestaurantService _RestaurantService;

        public RestaurantController(IRestaurantService RestaurantService)
        {
            _RestaurantService = RestaurantService;
        }
        public IActionResult Index()
        {
            RestaurantListViewModel viewModel = new()
            {
                Restaurants = _RestaurantService.GetAllRestaurants(),
            };
            return View(viewModel);
        }

        public IActionResult Add()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Add(RestaurantAddViewModel restaurantAddViewModel)
        {
            if(ModelState.IsValid)
            {
                Restaurant newRestaurant = new()
                {
                    name = restaurantAddViewModel.Restaurant.name,
                    borough = restaurantAddViewModel.Restaurant.borough,
                    cuisine = restaurantAddViewModel.Restaurant.cuisine
                };

                _RestaurantService.AddRestaurant(newRestaurant);
                return RedirectToAction("Index");
            }

            return View(restaurantAddViewModel);         
        }

        public IActionResult Edit(ObjectId id)
        {
            if(id == null || id == ObjectId.Empty)
            {
                return NotFound();
            }

            var selectedRestaurant = _RestaurantService.GetRestaurantById(id);
            return View(selectedRestaurant);
        }

        [HttpPost]
        public IActionResult Edit(Restaurant restaurant)
        {
            try
            {
                if(ModelState.IsValid)
                {
                    _RestaurantService.EditRestaurant(restaurant);
                    return RedirectToAction("Index");
                }
                else
                {
                    return BadRequest();
                }
            }
            catch (Exception ex)
            {
                ModelState.AddModelError("", $"La mise à jour du restaurant a échoué, veuillez réessayer ! Erreur : {ex.Message}");
            }

            return View(restaurant);
        }

        public IActionResult Delete(ObjectId id) {
            if (id == null || id == ObjectId.Empty)
            {
                return NotFound();
            }

            var selectedRestaurant = _RestaurantService.GetRestaurantById(id);
            return View(selectedRestaurant);
        }

        [HttpPost]
        public IActionResult Delete(Restaurant restaurant)
        {
            if (restaurant.Id == ObjectId.Empty)
            {
                ViewData["ErrorMessage"] = "La suppression du restaurant a échoué, ID invalide !";
                return View();
            }

            try
            {
                _RestaurantService.DeleteRestaurant(restaurant);
                TempData["RestaurantDeleted"] = "Restaurant supprimé avec succès !";

                return RedirectToAction("Index");
            }
            catch (Exception ex)
            {
                ViewData["ErrorMessage"] = $"La suppression du restaurant a échoué, veuillez réessayer ! Erreur : {ex.Message}";
            }

            var selectedRestaurant = _RestaurantService.GetRestaurantById(restaurant.Id);
            return View(selectedRestaurant);
        }        
    }
}
```

### ReservationController

Maintenant, pour le contrôleur de réservation. Cela est très similaire au RestaurantController mais il a une référence à la fois au service de restaurant et de réservation, car nous devons associer un restaurant à une réservation. Cela est dû au fait que pour le moment, le fournisseur EF Core ne prend pas en charge les relations entre entités, donc nous pouvons relier les entités d'une autre manière.

1. Créez un autre fichier de contrôleur MVC vide appelé ReservationController.cs.
    
2. Collez le code suivant :
    

```csharp
using Microsoft.AspNetCore.Mvc;
using MongoDB.Bson;
using RestRes.Models;
using RestRes.Services;
using RestRes.ViewModels;

namespace RestRes.Controllers
{
    public class ReservationController : Controller
    {
        private readonly IReservationService _ReservationService;
        private readonly IRestaurantService _RestaurantService;        

        public ReservationController(IReservationService ReservationService, IRestaurantService RestaurantService)
        {
            _ReservationService = ReservationService;
            _RestaurantService = RestaurantService;
        }

        public IActionResult Index()
        {
            ReservationListViewModel viewModel = new ReservationListViewModel()
            {
                Reservations = _ReservationService.GetAllReservations()
            };
            return View(viewModel);
        }

        public IActionResult Add(ObjectId restaurantId)
        {
            var selectedRestaurant = _RestaurantService.GetRestaurantById(restaurantId);
            
            ReservationAddViewModel reservationAddViewModel = new ReservationAddViewModel();

            reservationAddViewModel.Reservation = new Reservation();
            reservationAddViewModel.Reservation.RestaurantId = selectedRestaurant.Id;
            reservationAddViewModel.Reservation.RestaurantName = selectedRestaurant.name;
            reservationAddViewModel.Reservation.date = DateTime.UtcNow;

            return View(reservationAddViewModel);
        }

        [HttpPost]
        public IActionResult Add(ReservationAddViewModel reservationAddViewModel)
        {
                Reservation newReservation = new()
                {
                    RestaurantId = reservationAddViewModel.Reservation.RestaurantId,                   
                    date = reservationAddViewModel.Reservation.date,
                };

                _ReservationService.AddReservation(newReservation);
                return RedirectToAction("Index");   
        }

        public IActionResult Edit(string Id)
        {
            if(Id == null || string.IsNullOrEmpty(Id))
            {
                return NotFound();
            }

            var selectedReservation = _ReservationService.GetReservationById(new ObjectId(Id));
            return View(selectedReservation);
        }

        [HttpPost]
        public IActionResult Edit(Reservation reservation)
        {
            try
            {
                var existingReservation = _ReservationService.GetReservationById(reservation.Id);
                if (existingReservation != null)
                {
                    _ReservationService.EditReservation(reservation);
                    return RedirectToAction("Index");
                }
                else
                {
                    ModelState.AddModelError("", $"La réservation avec l'ID {reservation.Id} n'existe pas !");
                }
            }
            catch (Exception ex)
            {
                ModelState.AddModelError("", $"La mise à jour de la réservation a échoué, veuillez réessayer ! Erreur : {ex.Message}");
            }

            return View(reservation);
        }

        public IActionResult Delete(string Id)
        {
            if (Id == null || string.IsNullOrEmpty(Id))
            {
                return NotFound();
            }

            var selectedReservation = _ReservationService.GetReservationById(new ObjectId(Id));
            return View(selectedReservation);
        }

        [HttpPost]
        public IActionResult Delete(Reservation reservation)
        {
            if(reservation.Id == null)
            {
                ViewData["ErrorMessage"] = "La suppression de la réservation a échoué, ID invalide !";
                return View();
            }

            try
            {
                _ReservationService.DeleteReservation(reservation);
                TempData["ReservationDeleted"] = "Réservation supprimée avec succès";

                return RedirectToAction("Index");
            }
            catch (Exception ex)
            {
                ViewData["ErrorMessage"] = $"La suppression de la réservation a échoué, veuillez réessayer ! Erreur : {ex.Message}";
            }

            var selectedRestaurant = _ReservationService.GetReservationById(reservation.Id);
            return View(selectedRestaurant);
        }
    }
}
```

## Création des vues

Maintenant que nous avons le backend et les contrôleurs prêts avec les endpoints pour notre système de réservation de restaurant, il est temps d'implémenter les vues. Cela utilisera des pages Razor. Vous verrez également des références à des classes de Bootstrap car c'est le framework CSS qui vient avec les applications MVC dès le départ. Nous fournirons des vues pour les opérations CRUD pour les deux listes et réservations.

### Liste des restaurants

Tout d'abord, nous fournirons une vue qui sera mappée à la racine de /Restaurant, qui, par convention, regardera la méthode Index que nous avons implémentée.

[ASP.NET](http://ASP.NET) Core MVC utilise un modèle de convention où vous nommez le fichier .cshtml avec le nom de l'endpoint/méthode qu'il utilise et il vit à l'intérieur d'un dossier nommé d'après son contrôleur.

1. À l'intérieur du dossier Views, créez un nouveau sous-dossier appelé Restaurant.
    
2. À l'intérieur de ce dossier Restaurant, ajoutez une nouvelle vue en créant un fichier appelé `Index.cshtml`. Si vous utilisez les modèles disponibles, vous voulez Razor View - Empty. Nommez la vue Index.
    
3. Ajoutez ce code :
    

```csharp
@model RestaurantListViewModel

@if (TempData["RestaurantDeleted"] != null)
{
    <p class="text-success">@TempData["RestaurantDeleted"]</p>
}


@if (!Model.Restaurants.Any())
{
    <p>Aucun résultat</p>
}
else
{
    <table class="table table-condensed table-bordered">
        <tr>
            <th>
                Nom
            </th>
            <th>
                Cuisine
            </th>
            <th>
                Quartier
            </th>            
            <th>
                Actions
            </th>
        </tr>

        @foreach (var restaurant in Model.Restaurants)
        {
            <tr>
                <td>@restaurant.name</td>
                <td>@restaurant.cuisine</td>
                <td>@restaurant.borough</td>                
                <td>
                    <a asp-action="Edit" asp-route-id="@restaurant.Id.ToString()">Modifier</a>
                    <a asp-action="Delete" asp-route-id="@restaurant.Id.ToString()">Supprimer</a>
                    <a asp-controller="Reservation" asp-action="Add" asp-route-restaurantId="@restaurant.Id.ToString()">Réserver</a>
                </td>
            </tr>
        }

    </table>
}

<p>
    <a class="btn btn-primary" asp-action="Add">Ajouter un nouveau restaurant</a>
</p>
```

Maintenant, mettons à jour la route par défaut de Home vers /Restaurant.

Dans Program.cs, à l'intérieur de `app.MapControllerRoute`, remplacez la ligne de motif par ce qui suit :

```csharp
pattern: "{controller=Restaurant}/{action=Index}/{id?}");
```

Si nous exécutons cela maintenant, les boutons mèneraient à des erreurs 404 car nous n'avons pas encore implémenté ces fonctionnalités. Alors faisons cela maintenant.

### Ajout de restaurants

Nous allons commencer par le formulaire pour ajouter de nouveaux restaurants.

1. Ajoutez une nouvelle vue Razor vide à l'intérieur du sous-dossier Restaurant appelée Add.cshtml.
    
2. Ajoutez le code suivant :
    

```csharp
@model RestaurantAddViewModel

<h2>Créer un nouveau restaurant</h2>
<hr />

@if (ViewData["ErrorMessage"] != null)
{
    <p class="text-danger">@ViewData["ErrorMessage"]</p>
}

<form method="post" asp-controller="Restaurant" asp-action="Add">
    <div asp-validation-summary="All" class="text-danger"></div>

    <div class="mb-3">
        <label asp-for="Restaurant.name" class="form-label"></label>
        <input asp-for="Restaurant.name" class="form-control" />
        <span asp-validation-for="Restaurant.name" class="text-danger"></span>
    </div>

    <div class="mb-3">
        <label asp-for="Restaurant.cuisine" class="form-label"></label>
        <input asp-for="Restaurant.cuisine" class="form-control" />
        <span asp-validation-for="Restaurant.cuisine" class="text-danger"></span>
    </div>

      <div class="mb-3">
        <label asp-for="Restaurant.borough" class="form-label">Quartier</label>
        <input asp-for="Restaurant.borough" class="form-control" />
        <span asp-validation-for="Restaurant.borough" class="text-danger"></span>
    </div>

    <input type="submit" value="Ajouter un restaurant" class="btn btn-primary" />
</form>

<div>
    <a asp-controller="Restaurant" asp-action="Index">Retour à la liste</a>
</div>
```

### Modification des restaurants

Le code pour la page de modification est presque identique à celui de l'ajout, mais il utilise le Restaurant comme modèle car il utilisera le restaurant qui lui est passé pour pré-remplir le formulaire de modification.

1. Ajoutez une autre vue à l'intérieur du sous-dossier Restaurant appelée Edit.cshtml.
    
2. Ajoutez le code suivant :
    

```csharp
@model Restaurant

<h2>Mettre à jour @Model.name</h2>
<hr />

<form method="post" asp-controller="Restaurant" asp-action="Edit">
    <div asp-validation-summary="ModelOnly" class="text-danger"></div>
    <input type="hidden" asp-for="Id" />

    <div class="mb-3">
        <label asp-for="name" class="form-label">Nom</label>
        <input asp-for="name" class="form-control" />
        <span asp-validation-for="name" class="text-danger"/>
    </div>
    <div class="mb-3">
        <label asp-for="cuisine" class="form-label"></label>
        <input asp-for="cuisine" class="form-control" />
        <span asp-validation-for="cuisine" class="text-danger"/>
    </div>
    <div class="mb-3">
        <label asp-for="borough" class="form-label">Quartier</label>
        <input asp-for="borough" class="form-control" />
        <span asp-validation-for="borough" class="text-danger"/>
    </div>
    <input type="submit" value="Mettre à jour le restaurant" class="btn btn-primary" />
</form>
<div>
    <a asp-controller="Restaurant" asp-action="Index">Retour à la liste</a>
</div>
```

### Suppression des restaurants

La dernière page que nous devons implémenter est la page qui est appelée lorsque le bouton de suppression est cliqué.

1. Créez une nouvelle vue vide appelée Delete.cshtml.
    
2. Ajoutez le code suivant :
    

```csharp
@model Restaurant

<h2>Suppression de @Model.name</h2>
<hr />

@if(ViewData["ErrorMessage"] != null)
{
    <p class="text-danger">@ViewData["ErrorMessage"]</p>
}

<div>
    <dl class="row">
        <dt class="col-sm-4">
            <label asp-for="name">Nom</label>
        </dt>
        <dd class="col-sm-10">
            @Model?.name
        </dd>
        <dt class="col-sm-2">
            <label asp-for="cuisine"></label>
        </dt>
        <dd class="col-sm-10">
            @Model?.cuisine
        </dd>
        <dt class="col-sm-2">
            <label asp-for="borough">Quartier</label>
        </dt>
        <dd class="col-sm-10">
            @Model?.borough
        </dd>

    </dl>
</div>

<form method="post" asp-action="Delete">
    <input type="hidden" asp-for="Id" />
    <input type="submit" value="Supprimer le restaurant" class="btn btn-danger" onclick="javascript: return confirm('Êtes-vous sûr de vouloir supprimer ce restaurant ?');" />
</form>

<div>
    <a asp-controller="Restaurant" asp-action="Index">Retour à la liste</a>
</div>
```

### Liste des réservations

Nous avons ajouté les vues pour les restaurants, maintenant nous allons ajouter les vues pour les réservations, en commençant par lister les réservations existantes.

1. Créez un nouveau dossier à l'intérieur du dossier Views appelé Reservation.
    
2. Créez un nouveau fichier de vue vide appelé Index.cshtml.
    
3. Ajoutez le code suivant pour afficher les réservations, si elles existent :
    

```csharp
@model ReservationListViewModel

@if (TempData["ReservationDeleted"] != null)
{
    <p class="text-success">@TempData["ReservationDeleted"]</p>
}

@if (!Model.Reservations.Any())
{
    <p>Aucun résultat</p>
}

else
{    
    <table class="table table-condensed table-bordered">
        <tr>
            <th>
                Restaurant réservé
            </th>
            <th>
                Date et heure
            </th>
            <th>
                Actions
            </th>
        </tr>

        @foreach(var reservation in Model.Reservations)
        {
            <tr>
                <td>@reservation.RestaurantName</td>
                <td>@reservation.date.ToLocalTime()</td>
                <td>
                    <a asp-action="Edit" asp-route-id="@reservation.Id.ToString()">Modifier</a>
                    <a asp-action="Delete" asp-route-id="@reservation.Id.ToString()">Supprimer</a>
                </td>
            </tr>
        }

    </table>   

}
```

### Ajout de réservations

L'ajout de réservations est la prochaine étape.

1. Créez une vue vide appelée Add.cshtml.
    
2. Ajoutez le code suivant :
    

```csharp
@model ReservationAddViewModel


@if (ViewData["ErrorMessage"] != null)
{
    <p class="text-danger">@ViewData["ErrorMessage"]</p>
}

<form method="post" asp-controller="Reservation" asp-action="Add">
    <div asp-validation-summary="All" class="text-danger"></div>
    <input type="hidden" asp-for="Reservation.Id" />
    <input type="hidden" asp-for="Reservation.RestaurantId" />

    <div class="mb-3">
        <label asp-for="Reservation.date" class="form-label"></label>
        <input asp-for="Reservation.date" type="datetime-local" class="form-control" value="@DateTime.Now.ToString("yyyy-MM-ddTHH:mm")" />
        <span asp-validation-for="Reservation.date" class="text-danger"></span>
    </div>

    <input type="submit" value="Réserver une table" class="btn btn-primary" />
</form>
```

### Modification des réservations

La modification des réservations est la prochaine étape.

1. Créez une vue vide appelée Edit.cshtml.
    
2. Ajoutez le code suivant :
    

```csharp
@model Reservation

<h2>Modification de la réservation pour @Model.RestaurantName le @Model.date.ToLocalTime()</h2>
<hr />

<form method="post" asp-controller="Reservation" asp-action="Edit">
    <div asp-validation-summary="ModelOnly" class="text-danger"></div>
    <input type="hidden" asp-for="Id" />

    <div class="mb-3">
        <label asp-for="date" class="form-label"></label>
        <input asp-for="date" value="@Model.date.ToLocalTime().ToString("yyyy-MM-ddTHH:mm")" class="form-control" />
        <span asp-validation-for="date" class="text-danger" />
    </div>
    <input type="submit" value="Mettre à jour la réservation" class="btn btn-primary" />
</form>
<div>
    <a asp-controller="Reservation" asp-action="Index">Retour aux réservations</a>
</div>
```

### Suppression des réservations

La suppression des réservations est la prochaine étape.

1. Créez une vue vide appelée Delete.cshtml.
    
2. Ajoutez le code suivant :
    

```csharp
@model Reservation

<h2>Supprimer la réservation</h2>
<hr />

@if (ViewData["ErrorMessage"] != null)
{
    <p class="text-danger">@ViewData["ErrorMessage"]</p>
}

<div>
    <dl class="row">
        <dt class="col-sm-2">
            <label asp-for="RestaurantName">Nom</label>
        </dt>
        <dd class="col-sm-10">
            @Model?.RestaurantName
        </dd>
        <dt class="col-sm-2">
            <label asp-for="date"></label>
        </dt>
        <dd class="col-sm-10">
            @Model?.date.ToLocalTime()
        </dd>
        </dl>
</div>

<form method="post" asp-action="Delete">
    <input type="hidden" asp-for="Id" />
    <input type="hidden" asp-for="RestaurantId" />
    <input type="submit" value="Supprimer la réservation" class="btn btn-danger" onclick="javascript: return confirm('Êtes-vous sûr de vouloir supprimer cette réservation ?');" />
</form>

<div>
    <a asp-controller="Reservation" asp-action="Index">Retour à la liste</a>
</div>
```

## Mise à jour de la barre de navigation

La dernière chose à ajouter est de mettre à jour la barre de navigation de l'application afin que nous puissions facilement basculer entre les restaurants et les réservations.

Accédez au fichier situé à `Views/Shared/_Layout.cshtml`. Trouvez le `div` avec la classe `navbar-collapse`. Supprimez cette section entière et ajoutez le code suivant :

```csharp
<div class="collapse navbar-collapse justify-content-between">
    <ul class="navbar-nav flex-grow-1">
        <li class="nav-item">
            <a class="nav-link text-dark" asp-area="" asp-controller="Restaurant" asp-action="Index">Restaurants</a>
        </li>
        <li class="nav-item">
            <a class="nav-link text-dark" asp-area="" asp-controller="Reservation" asp-action="Index">Réservations</a>
        </li>
    </ul>
</div>
```

## Test de notre application

Nous avons maintenant une application fonctionnelle qui utilise le nouveau fournisseur MongoDB pour EF Core. Il est temps de tout tester et de visiter nos endpoints pour nous assurer que tout fonctionne.

Dans le terminal, exécutez la commande suivante :

`dotnet run`

Essayez de modifier des restaurants et d'ajouter des réservations. Vous pouvez ensuite naviguer vers la page de la base de données MongoDB Atlas et voir que vos modifications sont reflétées dans la base de données.

# Opérations avancées de MongoDB : Atlas Search et Vector Search

Le fournisseur EF Core est construit sur le pilote C# de MongoDB. Puisque nous avons déjà accès au MongoClient lors de la création du DbContext, cela nous permet d'effectuer des opérations avancées de MongoDB telles que Atlas Search et Vector Search. Ces fonctionnalités améliorent les capacités de votre application en permettant des fonctionnalités de recherche puissantes tout en tirant parti du framework EF Core familier.

#### Atlas Search

Atlas Search est un moteur de recherche en texte intégral fourni par MongoDB Atlas. Il vous permet d'exécuter des requêtes de recherche sophistiquées sur vos données MongoDB. Avec Atlas Search, vous pouvez implémenter des fonctionnalités comme l'autocomplétion, la recherche à facettes et le tri basé sur la pertinence.

Pour utiliser Atlas Search avec le fournisseur EF Core, suivez ces étapes :

1. **Configuration des index dans MongoDB Atlas** :
    
    * Allez dans votre cluster MongoDB Atlas.
        
    * Accédez à l'onglet "Search" et créez un nouvel index sur votre collection. Définissez les champs que vous souhaitez rendre recherchables.
        
2. **Définir les champs recherchables dans vos modèles** : Dans vos modèles C#, assurez-vous que les champs que vous souhaitez rechercher sont correctement définis. Voici un exemple de la définition d'un modèle de produit.
    
    ```csharp
    public class Product
    {
        public ObjectId Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
        public decimal Price { get; set; }
        public string Category { get; set; }
    }
    ```
    
3. **Effectuer des requêtes de recherche** : Utilisez les capacités du pilote .NET de MongoDB pour effectuer des recherches textuelles. Puisque EF Core lui-même ne prend pas directement en charge la syntaxe de recherche spécifique à MongoDB, vous devrez utiliser le pilote en conjonction avec EF Core. Voici un exemple :
    
    ```csharp
    using MongoDB.Driver;
    using MongoDB.Driver.Linq;
    
    var client = new MongoClient("your-mongodb-connection-string");
    var database = client.GetDatabase("your-database-name");
    var collection = database.GetCollection<Product>("Products");
    
    var searchResult = collection.Aggregate()
        .Match(Builders<Product>.Filter.Text("search term"))
        .ToList();
    ```
    

Cet exemple montre comment effectuer une recherche textuelle sur la collection `Products`. Le filtre `Text` aide à rechercher dans tous les champs indexés définis dans votre index Atlas Search.

#### Vector Search

Vector Search dans MongoDB est utilisé pour rechercher des documents basés sur des similitudes vectorielles, ce qui est particulièrement utile pour les applications impliquant l'apprentissage automatique, les recommandations et le traitement du langage naturel. Vector Search vous permet d'interroger des documents en utilisant des vecteurs représentant du texte, des images ou d'autres données à haute dimension.

1. **Créer et stocker des vecteurs** : Tout d'abord, assurez-vous que vos documents contiennent des vecteurs. Vous devrez peut-être pré-traiter vos données pour générer ces vecteurs en utilisant des modèles d'apprentissage automatique.
    
2. **Indexer les vecteurs dans MongoDB Atlas** : Créez un index spécial sur le champ vectoriel dans MongoDB Atlas pour permettre des recherches de similitude vectorielle efficaces.
    
3. **Effectuer des recherches vectorielles** : Utilisez le pilote .NET de MongoDB pour interroger en fonction de la similitude vectorielle.
    

#### Intégration avec EF Core

Bien que le fournisseur MongoDB EF Core simplifie les opérations CRUD, certaines fonctionnalités avancées comme Atlas Search et Vector Search nécessitent l'utilisation directe du pilote .NET de MongoDB. Cependant, vous pouvez toujours intégrer ces opérations dans votre application basée sur EF Core en utilisant le pilote pour les fonctionnalités de recherche et EF Core pour d'autres tâches de gestion de données.

En combinant EF Core et les fonctionnalités avancées de MongoDB, vous pouvez construire des applications puissantes et flexibles qui tirent le meilleur des deux mondes—les modèles d'accès aux données structurées d'EF Core et les puissantes capacités de recherche de MongoDB Atlas.