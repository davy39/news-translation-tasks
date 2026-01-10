---
title: 'Comment débuter avec ASP.NET Core et gRPC : Un manuel pour les développeurs'
subtitle: ''
author: Isaiah Clifford Opoku
co_authors: []
series: null
date: '2025-08-13T14:37:40.211Z'
originalURL: https://freecodecamp.org/news/get-started-with-aspnet-core-and-grpc-handbook
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1755043329753/f5ff4a61-79b7-44f0-9871-9dfef9f8d08a.png
tags:
- name: .NET
  slug: net
- name: Csharhp
  slug: csharhp
- name: handbook
  slug: handbook
seo_title: 'Comment débuter avec ASP.NET Core et gRPC : Un manuel pour les développeurs'
seo_desc: In today's distributed computing landscape, efficient service-to-service
  communication is crucial for building scalable, high-performance applications. gRPC
  (Google Remote Procedure Call) has emerged as one of the most powerful frameworks
  for creatin...
---

Dans le paysage informatique distribué d'aujourd'hui, une communication efficace de service à service est cruciale pour élaborer des applications évolutives et performantes. gRPC (Google Remote Procedure Call) est apparu comme l'un des Frameworks les plus puissants pour créer des API robustes et de type sécurisé, capables de gérer des milliers de requêtes par seconde avec une latence minimale.

gRPC est un Framework RPC moderne et open-source qui exploite HTTP/2, les Protocol Buffers et des capacités de streaming avancées pour offrir des performances exceptionnelles. Contrairement aux API REST traditionnelles, gRPC propose des contrats fortement typés, une génération automatique de code et un support intégré pour plusieurs langages de programmation. Cela en fait un choix idéal pour les architectures de microservices et le développement multiplateforme.

Dans ce manuel, je vous accompagnerai d'un niveau débutant complet jusqu'à la construction de services gRPC prêts pour la production avec [ASP.NET](http://ASP.NET) Core. Que vous migriez depuis des API REST ou que vous débutiez avec gRPC, ce guide vous apportera une expérience pratique et des exemples concrets.

**Ce que vous apprendrez :**

* Comment configurer votre premier service gRPC dans .NET
    
* Comment définir des contrats de service avec Protocol Buffers
    
* Comment implémenter des opérations unaires, de streaming serveur et de streaming client
    
* Comment construire des opérations CRUD (Création, Lecture, Mise à jour, Suppression)
    

Plongeons-nous dans le sujet et découvrons comment gRPC peut révolutionner votre expérience de développement d'API !

Vous pouvez trouver tout le code dans ce [**Répertoire GitHub**](https://github.com/Clifftech123/IsaiahCliffordOpokuBlog)**.**

### Table des matières

1. [Aperçu de gRPC et son fonctionnement avec .NET](#heading-apercu-de-grpc-et-son-fonctionnement-avec-net)
    
2. [Comment configurer gRPC avec .NET](#heading-comment-configurer-grpc-avec-net)
    
3. [Comment créer le modèle de produit](#heading-comment-creer-le-modele-de-produit)
    
4. [Comment configurer la base de données SQLite](#heading-comment-configurer-la-base-de-donnees-sqlite)
    
5. [Comment créer les Protocol Buffers de produit](#heading-comment-creer-les-protocol-buffers-de-produit)
    
6. [Comment implémenter les services d'opérations CRUD avec gRPC](#heading-comment-implementer-les-services-doperations-crud-avec-grpc)
    
7. [Comment implémenter les opérations de base de données CRUD gRPC avec SQLite](#heading-comment-implementer-les-operations-de-base-de-donnees-crud-grpc-avec-sqlite)
    
8. [Comment tester les services gRPC avec Postman](#heading-comment-tester-les-services-grpc-avec-postman)
    
9. [Comment tester la création de produit](#heading-comment-tester-la-creation-de-produit)
    
10. [Comment tester toutes les opérations de produit](#heading-comment-tester-toutes-les-operations-de-produit)
    
11. [Conclusion](#heading-conclusion)
    

### Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

* [.NET SDK](https://dotnet.microsoft.com/download)
    
* [Visual Studio Code](https://code.visualstudio.com/download)
    
* [Postman](https://www.postman.com/downloads/)
    

## Aperçu de gRPC et son fonctionnement avec .NET

gRPC est un Framework multiplateforme haute performance qui fonctionne de manière transparente avec de nombreuses technologies, dont .NET Core.

### Pourquoi choisir gRPC avec .NET ?

Il existe de nombreuses raisons pour lesquelles cette combinaison est pertinente. Tout d'abord, ce duo est jusqu'à 8 fois plus rapide que l'utilisation d'API REST avec du JSON. Ses contrats fortement typés aident également à prévenir les erreurs d'exécution.

Il bénéficie également d'un support intégré pour le streaming client, serveur et bidirectionnel, ainsi que d'une intégration transparente entre différents langages et plateformes. Enfin, il exploite HTTP/2 pour le multiplexage et la compression d'en-têtes – comme vous pouvez le voir, ces deux outils forment une paire extrêmement efficace.

Pour comprendre plus en détail pourquoi gRPC est si précieux, explorons un scénario réel courant.

### Le défi : Communication entre microservices

Imaginez que vous construisez une application de commerce électronique de grande envergure. Pour une meilleure maintenance et évolutivité, vous décidez de diviser votre application monolithique en services plus petits et spécialisés :

* **Service de Produits** – Gère le catalogue de produits, l'inventaire et la gestion des produits.
    
* **Service d'Authentification** – Gère l'authentification des utilisateurs, les autorisations et les profils utilisateurs.
    

Ces services doivent communiquer fréquemment entre eux. Par exemple, avant qu'un utilisateur puisse ajouter un produit à son panier, le Service de Produits doit vérifier auprès du Service d'Authentification que l'utilisateur est connecté et possède les permissions appropriées.

### Approche traditionnelle : API REST HTTP

Traditionnellement, dans les applications .NET, nous résolvons cette communication inter-services en utilisant `HttpClient` pour effectuer des appels d'API REST entre les services. Bien que cela fonctionne, cela comporte plusieurs défis :

* Échecs réseau : Les appels d'API peuvent échouer de manière inattendue, même quand tout semble correct.
    
* Goulots d'étranglement de performance : La sérialisation/désérialisation JSON ajoute une surcharge.
    
* Temps de réponse lents : Les limitations de HTTP/1.1 affectent les performances sous forte charge.
    
* Sécurité de typage : Aucune validation de contrat au moment de la compilation entre les services.
    
* Payloads volumineux : Le JSON peut être encombrant par rapport aux formats binaires.
    

### La solution gRPC

C'est ici que gRPC brille. Il répond à ces défis en fournissant des fonctionnalités très utiles en plus de celles déjà mentionnées, comme les Protocol Buffers, la génération de code pour le client et le serveur, et plus encore.

### Quand utiliser gRPC dans .NET

gRPC est particulièrement bénéfique dans certains scénarios, mais n'est pas forcément le meilleur choix pour d'autres. Voici quelques exemples de cas d'utilisation, ainsi que certains à éviter :

**✅ Parfait pour :**

* **Architecture de microservices** : Communication service à service haute fréquence.
    
* **Applications en temps réel** : Applications de chat, mises à jour en direct, jeux.
    
* **API haute performance** : Quand la vitesse et l'efficacité sont critiques.
    
* **Environnements polyglottes** : Services écrits dans différents langages de programmation.
    
* **API internes** : Services backend qui n'ont pas besoin de compatibilité avec les navigateurs.
    

**❌ Envisagez des alternatives quand :**

* **Applications basées sur un navigateur** : Support limité du navigateur (utilisez gRPC-Web à la place).
    
* **API publiques** : REST pourrait être plus familier pour les développeurs externes.
    
* **Opérations CRUD simples** : Là où la simplicité de REST est suffisante.
    
* **Intégration de systèmes hérités** : Quand les systèmes existants ne supportent que HTTP/1.1.
    

### gRPC vs REST : Une comparaison rapide

Voici une comparaison rapide de leurs principales caractéristiques :

| Fonctionnalité | gRPC | REST |
| --- | --- | --- |
| Protocole | HTTP/2 | HTTP/1.1 |
| Format de données | Protocol Buffers (Binaire) | JSON (Texte) |
| Performance | Haute | Modérée |
| Support Navigateur | Limité (nécessite gRPC-Web) | Complet |
| Streaming | Intégré | Limité |
| Génération de code | Automatique | Manuelle |

Dans ce manuel, nous allons construire un système complet de gestion de produits utilisant gRPC avec .NET, démontrant comment implémenter une communication service à service efficace avec des opérations CRUD complètes.

## Comment configurer gRPC avec .NET

Dans ce tutoriel, nous utiliserons Visual Studio Code pour construire notre application gRPC complète. Commençons par créer un nouveau projet gRPC à l'aide de l'interface CLI .NET.

### Création de votre premier projet gRPC

Commencez par ouvrir votre terminal (vous pouvez utiliser le terminal intégré de VS Code ou celui de votre système) et accédez au répertoire souhaité pour créer le projet.

Exécutez la commande suivante pour créer un nouveau projet gRPC :

```bash
dotnet new grpc -o ProductGrpc
```

**Ce que fait cette commande :**

* `dotnet new grpc` crée un nouveau projet en utilisant le template gRPC.
    
* `-o ProductGrpc` spécifie le nom du répertoire de sortie pour notre projet.
    

Ensuite, accédez au répertoire du projet :

```bash
cd ProductGrpc
```

Puis ouvrez le projet dans Visual Studio Code :

```bash
code .
```

### Comprendre la structure du projet

Après avoir exécuté la commande, vous devriez voir une sortie similaire à la suivante dans votre terminal, confirmant que le projet a été créé avec succès :

![Structure initiale du projet dans VS Code](https://cdn.hashnode.com/res/hashnode/image/upload/v1753873861602/6d135358-2065-40eb-9fe9-9a58bd8dc2eb.png align="left")

Explorons ce que le template .NET gRPC a généré pour nous :

```makefile
ProductGrpc/
├── Protos/
│   └── greet.proto          # Fichier de définition Protocol Buffer
├── Services/
│   └── GreeterService.cs    # Implémentation du service gRPC d'exemple
├── Program.cs               # Point d'entrée de l'application
├── ProductGrpc.csproj       # Fichier projet
└── appsettings.json         # Fichier de configuration
```

Fichiers clés :

* `Protos/greet.proto`: Définit le contrat de service en utilisant Protocol Buffers.
    
* `Services/GreeterService.cs`: Contient l'implémentation réelle du service.
    
* `Program.cs`: Configure et démarre le serveur gRPC.
    
* `ProductGrpc.csproj`: Contient les dépendances du projet et les paramètres de build.
    

### Vérification de la configuration

Assurons-nous que tout fonctionne correctement en exécutant l'application par défaut :

```yaml
dotnet run
```

Vous devriez voir une sortie indiquant que le serveur gRPC est en cours d'exécution :

```json
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: https://localhost:7042
info: Microsoft.Hosting.Lifetime[0]
      Application started. Press Ctrl+C to shut down.
```

**🎉 Félicitations !** Vous avez créé avec succès votre première application gRPC à l'aide de la CLI .NET. Le serveur est maintenant opérationnel et prêt à accepter des requêtes gRPC.

Passons à la section suivante, où nous commencerons à construire notre système de gestion de produits.

## Comment créer le modèle de produit

Maintenant que notre projet gRPC est configuré, créons notre modèle Product. Dans les applications .NET, les modèles représentent la structure des données et les entités métier avec lesquelles notre application va travailler. Considérez les modèles comme des plans qui définissent les propriétés que nos objets de données doivent posséder.

### Comprendre les modèles dans les applications gRPC

Les modèles remplissent plusieurs fonctions importantes :

* **Structure des données** : Ils définissent la forme et les propriétés de nos entités métier.
    
* **Sécurité de typage** : Ils assurent la validation de nos données au moment de la compilation.
    
* **Logique métier** : Ils représentent les objets du monde réel dans notre application.
    
* **Mapping base de données** : Ils servent d'entités pour les opérations de base de données.
    

### Création du dossier Models

Organisons notre code en créant un dossier dédié à nos modèles appelé `Models` à la racine de votre projet.

À l'intérieur du dossier Models, créez un nouveau fichier nommé `Product.cs`.

La structure de votre projet devrait maintenant ressembler à ceci :

```yaml
ProductGrpc/
├── Models/
│   └── Product.cs           # Notre nouveau modèle Product
├── Protos/
├── Services/
└── ...
```

### Implémentation du modèle Product

Ajoutez le code suivant à votre fichier `Product.cs` :

```csharp
// Models/Product.cs
using System.ComponentModel.DataAnnotations;

namespace ProductGrpc.Models
{
    public class Product
    {
        public Guid Id { get; set; }
        public required string Name { get; set; }
        public required string Description { get; set; }
        public decimal Price { get; set; }
        
        public DateTime Created { get; set; } = DateTime.UtcNow;
        
        public DateTime Updated { get; set; } = DateTime.UtcNow;
        public string? Tags { get; set; }
    }
}
```

Fonctionnalités C# modernes :

* Mot-clé `required` : Garantit que les propriétés doivent être initialisées lors de la création d'un objet.
    
* `string?` : Type de référence nullable pour les propriétés optionnelles.
    
* Valeurs par défaut : `Created` et `Updated` sont automatiquement réglés sur l'heure UTC actuelle.
    

### Pourquoi utiliser Guid pour l'ID ?

Nous utilisons `Guid` au lieu de `int` pour notre clé primaire pour plusieurs raisons :

* **Unicité** : Garanti unique à travers différents systèmes.
    
* **Sécurité** : Plus difficile à deviner que des entiers séquentiels.
    
* **Systèmes distribués** : Pas besoin de génération d'ID centralisée.
    
* **Évolutivité** : Parfait pour une architecture de microservices.
    

### Considérations sur l'espace de noms (Namespace)

**Note importante :** Si vous avez changé le nom de votre projet lors de sa création, assurez-vous que votre namespace correspond au nom de votre projet. Par exemple :

* Si votre projet s'appelle `MyProductService`, utilisez `namespace MyProductService.Models`.
    
* Si votre projet s'appelle `ProductGrpc`, utilisez `namespace ProductGrpc.Models`.
    

🎉 **Excellent travail !** Vous avez créé avec succès votre premier modèle métier qui servira de base à toute notre application gRPC.

### Étapes suivantes

Maintenant que notre modèle Product est prêt, passons à la configuration de SQLite comme base de données et à la configuration d'Entity Framework Core pour gérer la persistance de nos données. Cela nous permettra de stocker et de récupérer nos données de produits efficacement.

## Comment configurer la base de données SQLite

Pour persister nos données de produits, nous avons besoin d'une base de données capable de gérer nos opérations CRUD (Create, Read, Update, Delete) efficacement. Nous utiliserons **SQLite** pour ce tutoriel car il est léger, ne nécessite aucune installation de serveur séparé et fonctionne parfaitement pour le développement d'applications de petite à moyenne taille.

### Installer les packages requis

Avant de créer notre contexte de base de données, nous devons installer les packages Entity Framework Core nécessaires. Ouvrez votre terminal, assurez-vous d'être dans le répertoire racine de votre projet, puis exécutez ces commandes :

```powershell
dotnet add package Microsoft.EntityFrameworkCore.Design
```

```powershell
dotnet add package Microsoft.EntityFrameworkCore.Sqlite
```

Ce que font ces packages :

* **Microsoft.EntityFrameworkCore.Design** fournit des outils de conception pour EF Core (migrations, scaffolding).
    
* **Microsoft.EntityFrameworkCore.SQLite** est le fournisseur de base de données SQLite pour Entity Framework Core.
    

Vous devriez voir une sortie confirmant que les packages ont été ajoutés avec succès :

```bash
info : PackageReference for 'Microsoft.EntityFrameworkCore.Design' version 'x.x.x' added to file 'ProductGrpc.csproj'.
info : PackageReference for 'Microsoft.EntityFrameworkCore.Sqlite' version 'x.x.x' added to file 'ProductGrpc.csproj'.
```

### Création du contexte de base de données

Créons maintenant notre contexte de base de données, qui agit comme un pont entre nos objets .NET et la base de données.

Tout d'abord, créez un nouveau dossier appelé `Data` à la racine de votre projet. À l'intérieur du dossier Data, créez un fichier nommé `AppDbContext.cs`.

La structure de votre projet devrait maintenant ressembler à ceci :

```yaml
ProductGrpc/
├── Data/
│   └── AppDbContext.cs      # Notre nouveau contexte de base de données
├── Models/
│   └── Product.cs
├── Protos/
├── Services/
└── ...
```

Ajoutez le code suivant à votre fichier `AppDbContext.cs` :

```cs
// Data/AppDbContext.cs
using Microsoft.EntityFrameworkCore;
using ProductGrpc.Models;

namespace ProductGrpc.Data
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options)
        {
        }

        public DbSet<Product> Products { get; set; }
    }
}
```

Comprenons les composants clés de DbContext :

* **Constructeur** : Accepte `DbContextOptions` pour la configuration (chaîne de connexion, fournisseur, etc.).
    
* **DbSet Products** : Représente la table Products dans notre base de données.
    

### Enregistrement du contexte de base de données

Nous devons maintenant enregistrer notre `AppDbContext` auprès du conteneur d'injection de dépendances pour que notre application puisse l'utiliser.

Ouvrez votre fichier `Program.cs` et ajoutez la configuration de la base de données :

```cs
// Program.cs
using ProductGrpc.Data;
using ProductGrpc.Services;
using Microsoft.EntityFrameworkCore; // Assurez-vous d'avoir cet import

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddDbContext<AppDbContext>(opt=> 
    opt.UseSqlite("Data Source=ProductGrpc.db"));

// Ajouter les services au conteneur.
builder.Services.AddGrpc();

var app = builder.Build();

// Configurer le pipeline des requêtes HTTP.
app.MapGrpcService<GreeterService>();
app.MapGet("/", () => "Communication with gRPC endpoints must be made through a gRPC client. To learn how to create a client, visit: https://go.microsoft.com/fwlink/?linkid=2086909");

app.Run();
```

`Data Source=ProductGrpc.db` crée un fichier de base de données SQLite nommé `ProductGrpc.db` dans le répertoire de votre projet.

### Création et exécution des migrations

Nous devons maintenant créer une migration pour générer le schéma de la base de données basé sur notre modèle Product.

Commencez par créer la migration initiale :

```powershell
dotnet ef migrations add InitialCreate
```

Cette commande va :

* Analyser vos modèles et votre DbContext.
    
* Générer des fichiers de migration dans un dossier `Migrations`.
    
* Créer les commandes SQL nécessaires pour construire le schéma de votre base de données.
    

Vous devriez voir une sortie comme celle-ci :

```powershell
Build succeeded.
Done. To undo this action, use 'dotnet ef migrations remove'
```

Appliquez la migration pour créer la base de données :

```powershell
dotnet ef database update
```

Cette commande va :

* Exécuter les commandes SQL de la migration.
    
* Créer le fichier `ProductGrpc.db` dans le répertoire de votre projet.
    
* Configurer la table Products avec toutes les colonnes correctes.
    

Vous devriez voir une sortie confirmant que la base de données a été créée :

```powershell
Build succeeded.
Applying migration '20240101000000_InitialCreate'.
Done.
```

### Vérification de la configuration

Après avoir exécuté la migration, vous devriez voir :

1. Un nouveau dossier `Migrations` dans votre projet avec les fichiers de migration.
    
2. Un fichier `ProductGrpc.db` à la racine de votre projet (c'est votre base de données SQLite).
    
3. Aucune erreur dans la sortie du terminal.
    

La structure de votre projet devrait maintenant ressembler à ceci :

```yaml
ProductGrpc/
├── Data/
│   └── AppDbContext.cs
├── Migrations/
│   ├── 20240101000000_InitialCreate.cs
│   └── AppDbContextModelSnapshot.cs
├── Models/
│   └── Product.cs
├── ProductGrpc.db            # Votre fichier de base de données SQLite
└── ...
```

Félicitations ! Vous avez installé avec succès les packages Entity Framework Core, créé un contexte de base de données, enregistré le contexte avec l'injection de dépendances, généré et appliqué votre première migration, et créé une base de données SQLite fonctionnelle. Ouf !

### Quelle est la suite ?

Maintenant que notre base de données est configurée et prête, nous pouvons passer à la création de nos définitions Protocol Buffer (fichiers `.proto`) et à l'implémentation de nos services gRPC pour les opérations CRUD.

## Comment créer les Protocol Buffers de produit

Les Protocol Buffers (protobuf) sont le cœur de la communication gRPC. Ils définissent la structure de vos données et services de manière neutre par rapport au langage, qui est ensuite compilée en code C# natif. Les Protocol Buffers utilisent le protocole efficace **HTTP/2**, rendant la communication de service à service rapide et fiable.

### Comprendre Protocol Buffers vs API REST

Pour mieux comprendre les Protocol Buffers, comparons-les à ce que vous connaissez peut-être déjà avec le développement d'API REST.

Dans le développement d'API REST, vous définissez généralement vos points de terminaison d'API à l'aide de contrôleurs et de méthodes d'action. Le contrat entre le client et le serveur est souvent documenté séparément (comme avec OpenAPI/Swagger), et il n'y a aucune garantie au moment de la compilation que votre documentation corresponde à votre implémentation réelle.

```csharp
[ApiController]
[Route("api/[controller]")]
public class ProductsController : ControllerBase
{
    [HttpGet("{id}")]
    public async Task<ActionResult<ProductDto>> GetProduct(int id) { ... }
```

Avec **gRPC,** le contrat de service est défini d'abord dans le fichier `.proto` à l'aide du mot-clé `service`. Ce contrat devient la source unique de vérité, et le code du client comme celui du serveur en sont générés, garantissant qu'ils sont toujours synchronisés.

```csharp
service ProductService {
  rpc GetProduct(GetProductRequest) returns (GetProductResponse);
}
```

### Transfert de données et sérialisation

Les API REST utilisent généralement JSON pour le transfert de données, qui est lisible par l'homme et largement supporté. Mais le JSON est basé sur du texte, ce qui présente quelques inconvénients. D'abord, il a des tailles de payload plus importantes dues à l'encodage texte. Il s'accompagne également d'une surcharge d'analyse à l'exécution. Il ne possède aucune validation de schéma intégrée et il existe un risque élevé de fautes de frappe dans les noms de champs.

```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "name": "Casque sans fil",
  "price": 99.99
}
```

gRPC utilise plutôt des Protocol Buffers, qui sérialisent les données dans un format binaire compact. Cela permet d'obtenir des payloads nettement plus petits (jusqu'à 6 fois plus petits que le JSON), une sérialisation/désérialisation plus rapide, un typage fort avec validation à la compilation, et une évolution du schéma sans changements cassants.

#### Différences de protocole de transport

Les API REST fonctionnent sur **HTTP/1.1**, qui présente certaines limitations :

* Un cycle requête-réponse par connexion.
    
* En-têtes textuels (surcharge plus importante).
    
* Pas de multiplexage intégré.
    
* Capacités de streaming limitées.
    

gRPC exploite **HTTP/2**, qui offre plusieurs avantages :

* **Multiplexage** : Plusieurs requêtes sur une seule connexion.
    
* **Compression d'en-tête** : Surcharge réduite avec HPACK.
    
* **Server push** : Le serveur peut initier des flux vers les clients.
    
* **Contrôle de flux** : Meilleure gestion des consommateurs lents.
    

#### Définitions de structures de données

Dans les API REST, vous définissez les **DTO (Data Transfer Objects)** comme des classes régulières :

```csharp
public class ProductDto
{
    public string Id { get; set; }
    public string Name { get; set; }
    public decimal Price { get; set; }
}
```

Ces DTO n'existent que dans votre langage spécifique et nécessitent une synchronisation manuelle entre différents services ou langages.

Dans gRPC, vous définissez des **Messages** dans le fichier proto :

```csharp
message ProductModel {
  string id = 1;
  string name = 2;
  double price = 3;
}
```

Ces définitions de messages sont agnostiques au langage et génèrent automatiquement des classes équivalentes dans n'importe quel langage de programmation supporté.

Voici un tableau de comparaison rapide pour résumer ces différences :

| Concept API REST | Équivalent gRPC | Objectif |
| --- | --- | --- |
| Interface | Service | Définit les opérations disponibles |
| DTO (Data Transfer Object) | Message | Définit une structure de données |
| Requête/Réponse JSON | Protocol Buffer Binaire | Format de sérialisation des données |
| HTTP/1.1 | HTTP/2 | Protocole de transport |

### Création du fichier Proto de produit

Accédez au dossier `Protos` dans votre projet et créez un nouveau fichier nommé `product.proto`. Assurez-vous que l'extension du fichier est bien `.proto`.

La structure de votre projet devrait ressembler à ceci :

```yaml
ProductGrpc/
├── Protos/
│   ├── greet.proto          # Fichier template par défaut
│   └── product.proto        # Notre nouveau fichier proto
└── ...
```

### Configuration de l'en-tête du fichier Proto

Ajoutez l'en-tête suivant à votre fichier `product.proto` :

```cs
// Protos/product.proto
syntax = "proto3";

option csharp_namespace = "ProductGrpc";

package product;
```

Voici ce qui se passe :

* `syntax = "proto3"` : Spécifie que nous utilisons la version 3 de Protocol Buffers.
    
* `option csharp_namespace = "ProductGrpc"` : Définit le namespace C# pour le code généré.
    
* `package product` : Définit le nom du package protobuf.
    

**Note :** Si vous avez nommé votre projet différemment, assurez-vous que `csharp_namespace` corresponde au nom de votre projet.

### Définition du service Product

Dans gRPC, les services définissent les opérations disponibles (semblables aux interfaces dans les API REST). Ajoutez la définition de service suivante :

```csharp
// Protos/product.proto
service ProductsServiceProto {
  rpc CreateProduct(CreateProductRequest) returns (CreateProductResponse);
  rpc GetProduct(GetProductRequest) returns (GetProductResponse);
  rpc ListProducts(ListProductsRequest) returns (ListProductsResponse);
  rpc UpdateProduct(UpdateProductRequest) returns (UpdateProductResponse);
  rpc DeleteProduct(DeleteProductRequest) returns (DeleteProductResponse);
}
```

Explication des méthodes de service :

* `rpc` : Définit un appel de procédure à distance.
    
* `CreateProduct` : Nom de la méthode.
    
* `(CreateProductRequest)` : Type de message d'entrée.
    
* `returns (CreateProductResponse)` : Type de message de sortie.
    

### Définition des messages Protocol Buffer

Les messages dans gRPC sont l'équivalent des DTO dans les API REST. Ils définissent la structure des données échangées. Créons tous les messages dont nous avons besoin :

#### Message de modèle de produit :

```yaml
// product.proto
message ProductModel {
  string id = 1;
  string name = 2;
  string description = 3;
  double price = 4;
  string created_at = 5;
  string updated_at = 6;
  string tags = 7;
}
```

#### Messages d'opération de création :

```cs
// Protos/product.proto
message CreateProductRequest {
  string name = 1;
  string description = 2;
  double price = 3;
  string tags = 4;
}

message CreateProductResponse {
  bool success = 1;
  string message = 2;
  ProductModel product = 3;
}
```

#### Messages d'opération de lecture :

```cs
// Protos/product.proto
message GetProductRequest {
  string id = 1;
}

message GetProductResponse {
  bool success = 1;
  string message = 2;
  ProductModel product = 3;
}

message ListProductsRequest {
  int32 page = 1;
  int32 page_size = 2;
}

message ListProductsResponse {
  bool success = 1;
  string message = 2;
  repeated ProductModel products = 3;
  int32 total_count = 4;
}
```

#### Messages d'opération de mise à jour :

```cs
 // Protos/product.proto
message UpdateProductRequest {
  string id = 1;
  string name = 2;
  string description = 3;
  double price = 4;
  string tags = 5;
}

message UpdateProductResponse {
  bool success = 1;
  string message = 2;
  ProductModel product = 3;
}
```

#### Messages d'opération de suppression :

```cs
// Protos/product.proto
message DeleteProductRequest {
  string id = 1;
}

message DeleteProductResponse {
  bool success = 1;
  string message = 2;
}
```

### Comprendre la syntaxe Protocol Buffer

Il y a quelques concepts clés à comprendre sur le fonctionnement des Protocol Buffers :

* **Numéros de champs** : Chaque champ possède un numéro unique (par exemple, `= 1`, `= 2`) utilisé pour l'encodage binaire.
    
* **Types de champs** : `string`, `int32`, `double`, `bool` sont des types scalaires courants.
    
* **repeated** : Indique un tableau/liste (par exemple, `repeated ProductModel products`).
    
* **Imbrication de messages** : Les messages peuvent contenir d'autres messages (par exemple, `ProductModel product`).
    

Gardez à l'esprit que les numéros de champs doivent être uniques au sein d'un message, que les numéros de 1 à 15 utilisent un encodage de 1 octet (plus efficace), et que vous ne devriez jamais réutiliser des numéros de champs (pour la compatibilité ascendante).

### Fichier Proto de produit complet

Voici votre fichier `product.proto` complet :

```cs
// Protos/product.proto
syntax = "proto3";

option csharp_namespace = "ProductGrpc";

package product;

// Définition du service de produits
service ProductsServiceProto {
  rpc CreateProduct(CreateProductRequest) returns (CreateProductResponse);
  rpc GetProduct(GetProductRequest) returns (GetProductResponse);
  rpc ListProducts(ListProductsRequest) returns (ListProductsResponse);
  rpc UpdateProduct(UpdateProductRequest) returns (UpdateProductResponse);
  rpc DeleteProduct(DeleteProductRequest) returns (DeleteProductResponse);
}

// Message du modèle de produit
message ProductModel {
  string id = 1;
  string name = 2;
  string description = 3;
  double price = 4;
  string created_at = 5;
  string updated_at = 6;
  string tags = 7;
}

// Messages d'opération de création
message CreateProductRequest {
  string name = 1;
  string description = 2;
  double price = 3;
  string tags = 4;
}

message CreateProductResponse {
  bool success = 1;
  string message = 2;
  ProductModel product = 3;
}

// Messages d'opération de lecture
message GetProductRequest {
  string id = 1;
}

message GetProductResponse {
  bool success = 1;
  string message = 2;
  ProductModel product = 3;
}

message ListProductsRequest {
  int32 page = 1;
  int32 page_size = 2;
}

message ListProductsResponse {
  bool success = 1;
  string message = 2;
  repeated ProductModel products = 3;
  int32 total_count = 4;
}

// Messages d'opération de mise à jour
message UpdateProductRequest {
  string id = 1;
  string name = 2;
  string description = 3;
  double price = 4;
  string tags = 5;
}

message UpdateProductResponse {
  bool success = 1;
  string message = 2;
  ProductModel product = 3;
}

// Messages d'opération de suppression
message DeleteProductRequest {
  string id = 1;
}

message DeleteProductResponse {
  bool success = 1;
  string message = 2;
}
```

### Build du projet pour générer le code C#

Maintenant que nous avons défini notre contrat Protocol Buffer, nous devons builder le projet pour générer le code C# correspondant :

```bash
dotnet build
```

Cette commande va compiler vos fichiers `.proto` en classes C#, générer le code client et serveur, et créer des classes de requête/réponse fortement typées.

Vous devriez voir une sortie confirmant que le build a réussi :

```bash
Restore complete (0.6s)
  ProductGrpc succeeded (9.5s) → bin\Debug\net9.0\ProductGrpc.dll

Build succeeded in 11.1s
```

### Qu'est-ce qui est généré ?

Après le build, le compilateur Protocol Buffer génère plusieurs fichiers C# (vous ne les verrez pas directement, mais ils sont disponibles dans votre code) :

* **ProductModel** : Classe C# représentant vos données de produit.
    
* **CreateProductRequest/Response** : Classes de requête et de réponse pour les opérations de création.
    
* **ProductService.ProductServiceBase** : Classe de base pour implémenter votre service.
    
* **ProductService.ProductServiceClient** : Classe client pour appeler le service.
    

Félicitations ! Vous avez créé avec succès une définition Protocol Buffer complète, défini un contrat de service CRUD complet, mis en place une structure de message fortement typée et généré le code C# à partir de votre fichier proto.

### Quelle est la suite ?

Maintenant que notre contrat Protocol Buffer est défini, nous pouvons commencer à implémenter les méthodes réelles du service gRPC. Dans la section suivante, nous allons créer la classe `ProductService` et implémenter chaque opération CRUD.

**Rappel :** Les Protocol Buffers sont agnostiques au langage, donc ce même fichier `.proto` pourrait être utilisé pour générer du code client en Python, Java, Go ou tout autre langage supporté.

## Comment implémenter les services d'opérations CRUD avec gRPC

Maintenant que notre base de données est configurée et que nos contrats Protocol Buffer sont définis, il est temps d'implémenter les fonctionnalités CRUD (Create, Read, Update, Delete). Nous allons créer un service gRPC qui réunit nos modèles de base de données et nos définitions Protocol Buffer.

### Comprendre l'architecture d'implémentation

Avant de commencer à coder, comprenons comment les pièces s'assemblent :

```bash
Protocol Buffer (.proto) → Code C# généré → Notre implémentation de service → Base de données
```

Concepts clés dans ce code :

* **Service Proto :** Interface (définit quelles méthodes sont disponibles).
    
* **Messages Proto** : DTO (définissent la structure des données).
    
* **Implémentation du service** : Logique métier (ce qui se passe).
    
* **Contexte de base de données** : Couche de persistance des données.
    

### Configuration du build du fichier Proto

D'abord, nous devons nous assurer que notre fichier `product.proto` est compilé en code C# pendant le processus de build.

Ouvrez votre fichier `ProductGrpc.csproj` et localisez la section `<ItemGroup>` qui référence les fichiers proto :

```xml
  <!-- ProductGrpc.csproj -->
<Project Sdk="Microsoft.NET.Sdk.Web">

  <PropertyGroup>
    <TargetFramework>net9.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
  </PropertyGroup>

  <ItemGroup>
    <Protobuf Include="Protos\greet.proto" GrpcServices="Server" />
    <!-- Ajoutez cette ligne pour inclure notre fichier product.proto -->
    <Protobuf Include="Protos\product.proto" GrpcServices="Server" />
  </ItemGroup>

  <ItemGroup>
    <PackageReference Include="Grpc.AspNetCore" Version="2.64.0" />
    <PackageReference Include="Microsoft.EntityFrameworkCore.Design" Version="9.0.6">
      <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
      <PrivateAssets>all</PrivateAssets>
    </PackageReference>
    <PackageReference Include="Microsoft.EntityFrameworkCore.Sqlite" Version="9.0.6" />
  </ItemGroup>
</Project>
```

Ce que fait cette configuration :

* `Include="Protos\product.proto"` indique à .NET de traiter notre fichier proto.
    
* `GrpcServices="Server"` génère le code côté serveur (classes de base de service).
    

### Build du projet

Maintenant, buildons le projet pour générer le code C# à partir de notre fichier proto :

```bash
dotnet build
```

Cette commande compilera vos fichiers `.proto` en classes C#, générera la classe `ProductsServiceProto.ProductsServiceProtoBase` dont nous hériterons, créera toutes les classes de messages de requête/réponse et validera que tout se compile correctement.

Vous devriez voir une sortie comme :

```yaml
Build succeeded.
    0 Warning(s)
    0 Error(s)
```

### Création de la classe ProductService

Accédez au dossier `Services` et créez un nouveau fichier nommé `ProductService.cs`. Il contiendra notre implémentation du service gRPC.

La structure de votre projet devrait maintenant ressembler à ceci :

```yaml
ProductGrpc/
├── Services/
│   ├── GreeterService.cs    # Service template par défaut
│   └── ProductService.cs    # Notre nouveau service de produit
└── ...
```

### Mise en place de la base du service

Commencez par créer la structure de base de la classe de service :

```csharp
 // Services/ProductService.cs
using Grpc.Core;
using Microsoft.EntityFrameworkCore;
using ProductGrpc.Data;
using ProductGrpc.Models;

namespace ProductGrpc.Services
{
    public class ProductService : ProductsServiceProto.ProductsServiceProtoBase
    {
        private readonly AppDbContext _dbContext;
        private readonly ILogger<ProductService> _logger;

        public ProductService(AppDbContext dbContext, ILogger<ProductService> logger)
        {
            _dbContext = dbContext;
            _logger = logger;
        }

        // Les méthodes CRUD seront implémentées ici
    }
}
```

Composants clés de ce code :

* **Héritage** : `ProductsServiceProto.ProductsServiceProtoBase` est généré à partir de notre fichier proto.
    
* **Injection de dépendances** : Nous injectons `AppDbContext` pour les opérations de base de données et `ILogger` pour les logs.
    
* **Constructeur** : Initialise nos dépendances.
    

### Implémentation des signatures de méthodes

Ajoutons maintenant toutes les signatures de méthodes que nous avons définies dans notre fichier proto. Ces méthodes surchargent les méthodes virtuelles de la classe de base :

```csharp
 //Services/ProductService.cs
using Grpc.Core;
using Microsoft.EntityFrameworkCore;
using ProductGrpc.Data;
using ProductGrpc.Models;

namespace ProductGrpc.Services
{
    public class ProductService : ProductsServiceProto.ProductsServiceProtoBase
    {
        private readonly AppDbContext _dbContext;
        private readonly ILogger<ProductService> _logger;

        public ProductService(AppDbContext dbContext, ILogger<ProductService> logger)
        {
            _dbContext = dbContext;
            _logger = logger;
        }

        public override async Task<CreateProductResponse> CreateProduct(
            CreateProductRequest request, 
            ServerCallContext context)
        {
            // L'implémentation ira ici
            throw new NotImplementedException();
        }

        public override async Task<GetProductResponse> GetProduct(
            GetProductRequest request, 
            ServerCallContext context)
        {
            // L'implémentation ira ici
            throw new NotImplementedException();
        }

        public override async Task<ListProductsResponse> ListProducts(
            ListProductsRequest request, 
            ServerCallContext context)
        {
            // L'implémentation ira ici
            throw new NotImplementedException();
        }

        public override async Task<UpdateProductResponse> UpdateProduct(
            UpdateProductRequest request, 
            ServerCallContext context)
        {
            // L'implémentation ira ici
            throw new NotImplementedException();
        }

        public override async Task<DeleteProductResponse> DeleteProduct(
            DeleteProductRequest request, 
            ServerCallContext context)
        {
            // L'implémentation ira ici
            throw new NotImplementedException();
        }
    }
}
```

### Comprendre les paramètres de méthode

Chaque méthode gRPC reçoit deux paramètres :

1. **Paramètre de requête** : Contient les données envoyées par le client (par exemple, `CreateProductRequest`).
    
2. **ServerCallContext** : Fournit un accès aux métadonnées de la requête, aux jetons d'annulation et aux en-têtes de réponse.
    

**Modèle de signature de méthode :**

```csharp
public override async Task<ResponseType> MethodName(
    RequestType request, 
    ServerCallContext context)
```

### Enregistrement du service

Avant d'implémenter les méthodes, nous devons enregistrer notre service auprès de l'application. Ouvrez `Program.cs` et ajoutez le service :

```cs
 // Program.cs
using Microsoft.EntityFrameworkCore;
using ProductGrpc.Data;
using ProductGrpc.Services; // Ajoutez cet import

var builder = WebApplication.CreateBuilder(args);

// Ajouter les services au conteneur.
builder.Services.AddGrpc();

// Enregistrer notre contexte de base de données
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlite("Data Source=ProductGrpc.db"));

var app = builder.Build();

// Configurer le pipeline des requêtes HTTP.
app.MapGrpcService<GreeterService>();
app.MapGrpcService<ProductService>(); // Ajoutez cette ligne

app.MapGet("/", () => "Communication with gRPC endpoints must be made through a gRPC client. To learn how to create a client, visit: https://go.microsoft.com/fwlink/?linkid=2086909");

app.Run();
```

### Gestion des avertissements du compilateur

Vous pourriez voir des avertissements tels que :

```bash
This async method lacks 'await' operators and will run synchronously.
```

C'est normal car nous n'avons pas encore implémenté la logique réelle. Ces avertissements disparaîtront une fois que nous aurons ajouté l'implémentation dans les sections suivantes.

### Création de méthodes utilitaires

Avant d'implémenter les opérations CRUD, ajoutons quelques méthodes utilitaires pour la conversion entre nos modèles de base de données et les messages Protocol Buffer :

```cs
// Services/ProductService.cs
// Ajoutez ces méthodes utilitaires à votre classe ProductService

private static ProductModel MapToProductModel(Product product)
{
    return new ProductModel
    {
        Id = product.Id.ToString(),
        Name = product.Name,
        Description = product.Description,
        Price = (double)product.Price,
        CreatedAt = product.Created.ToString("yyyy-MM-ddTHH:mm:ssZ"),
        UpdatedAt = product.Updated.ToString("yyyy-MM-ddTHH:mm:ssZ"),
        Tags = product.Tags ?? string.Empty
    };
}
```

Excellent travail ! Vous avez réussi à :

* Configurer la compilation du fichier proto.
    
* Créer la structure de la classe ProductService.
    
* Mettre en place l'injection de dépendances.
    
* Définir toutes les signatures de méthodes CRUD.
    
* Enregistrer le service auprès de l'application.
    
* Créer des méthodes utilitaires pour le mapping des données.
    

### Quelle est la suite ?

Maintenant que la base de notre service est prête, nous allons implémenter chaque opération CRUD une par une :

1. **CreateProduct** : Ajouter de nouveaux produits à la base de données.
    
2. **GetProduct** : Récupérer un seul produit par son ID.
    
3. **ListProducts** : Obtenir une liste paginée de produits.
    
4. **UpdateProduct** : Modifier des produits existants.
    
5. **DeleteProduct** : Supprimer des produits de la base de données.
    

Dans les sections suivantes, nous approfondirons chaque implémentation, en gérant les cas d'erreur, la validation et les meilleures pratiques.

**💡 Conseil de pro :** Le paramètre `ServerCallContext` fournit des informations utiles comme les jetons d'annulation de requête, les métadonnées client et les en-têtes de réponse. Nous les utiliserons dans nos implémentations pour une meilleure gestion des erreurs et des logs.

**Note :** Le mot-clé `override` est crucial – il indique à C# que nous implémentons les méthodes virtuelles définies dans la classe de base générée à partir de notre fichier proto.

## Comment implémenter les opérations de base de données CRUD gRPC avec SQLite

Maintenant que la base de notre service est prête, implémentons chaque opération CRUD. Chaque méthode gérera les opérations de base de données, la gestion des erreurs et renverra les réponses appropriées en utilisant nos messages Protocol Buffer.

### Comprendre l'architecture d'implémentation

Chaque opération CRUD suit un modèle cohérent :

1. **Validation des entrées** : Valider les paramètres de la requête.
    
2. **Opération de base de données** : Effectuer le travail réel sur la base de données.
    
3. **Mapping de réponse** : Convertir les modèles de base de données en messages Protocol Buffer.
    
4. **Gestion des erreurs** : Capturer et gérer les exceptions avec élégance.
    

### Création du service `CreateProduct` 

La méthode `CreateProduct` gère l'ajout de nouveaux produits à notre base de données. C'est le **"C"** de CRUD (Create).

```cs
//Services/ProductService.cs
public override async Task<CreateProductResponse> CreateProduct(
    CreateProductRequest request, 
    ServerCallContext context)
{
    try
    {
        // Validation des entrées
        if (string.IsNullOrWhiteSpace(request.Name))
        {
            return new CreateProductResponse
            {
                Success = false,
                Message = "Le nom du produit est requis"
            };
        }

        if (request.Price <= 0)
        {
            return new CreateProductResponse
            {
                Success = false,
                Message = "Le prix du produit doit être supérieur à zéro"
            };
        }

        // Créer une nouvelle entité de produit
        var productItem = new Product
        {
            Id = Guid.NewGuid(),
            Name = request.Name,
            Description = request.Description,
            Price = Convert.ToDecimal(request.Price),
            Created = DateTime.UtcNow,
            Updated = DateTime.UtcNow,
            Tags = request.Tags
        };

        // Ajouter à la base de données
        _dbContext.Products.Add(productItem);
        await _dbContext.SaveChangesAsync();

        _logger.LogInformation("Produit créé avec succès avec l'ID : {ProductId}", productItem.Id);

        // Renvoyer une réponse de succès
        return new CreateProductResponse
        {
            Success = true,
            Message = "Produit créé avec succès",
            Product = MapToProductModel(productItem)
        };
    }
    catch (Exception ex)
    {
        _logger.LogError(ex, "Erreur lors de la création du produit");
        
        return new CreateProductResponse
        {
            Success = false,
            Message = $"Erreur lors de la création du produit : {ex.Message}"
        };
    }
}
```

Voici les détails importants de l'implémentation :

* **Génération d'ID unique** : `Guid.NewGuid()` crée un identifiant unique.
    
* **Gestion des horodatages** : `DateTime.UtcNow` assure une gestion cohérente des fuseaux horaires.
    
* **Conversion de type** : `Convert.ToDecimal()` convertit un double en décimal pour le stockage en base de données.
    
* **Validation des entrées** : Vérifie les champs requis et les valeurs valides.
    
* **Logs** : Enregistre les opérations réussies et les erreurs pour le débogage.
    

### Création du service `GetProduct` 

La méthode `GetProduct` récupère un seul produit par son ID. C'est le **"R"** de CRUD (Read).

```cs
//Services/ProductService.cs
public override async Task<GetProductResponse> GetProduct(
    GetProductRequest request, 
    ServerCallContext context)
{
    try
    {
        // Valider et parser l'ID du produit
        if (!Guid.TryParse(request.Id, out var productId))
        {
            return new GetProductResponse
            {
                Success = false,
                Message = "Format d'ID de produit invalide. Veuillez fournir un GUID valide."
            };
        }

        // Trouver le produit en base de données
        var product = await _dbContext.Products.FindAsync(productId);
        
        if (product == null)
        {
            _logger.LogWarning("Produit non trouvé avec l'ID : {ProductId}", productId);
            
            return new GetProductResponse
            {
                Success = false,
                Message = "Produit non trouvé"
            };
        }

        _logger.LogInformation("Produit récupéré avec succès avec l'ID : {ProductId}", productId);

        // Renvoyer une réponse de succès avec les données du produit
        return new GetProductResponse
        {
            Success = true,
            Message = "Produit récupéré avec succès",
            Product = MapToProductModel(product)
        };
    }
    catch (Exception ex)
    {
        _logger.LogError(ex, "Erreur lors de la récupération du produit avec l'ID : {ProductId}", request.Id);
        
        return new GetProductResponse
        {
            Success = false,
            Message = $"Erreur lors de la récupération du produit : {ex.Message}"
        };
    }
}
```

Détails d'implémentation importants :

* **Validation de l'ID** : `Guid.TryParse()` valide le format de l'ID en toute sécurité.
    
* **Requête de base de données** : `FindAsync()` trouve efficacement les enregistrements par clé primaire.
    
* **Vérification de nullité** : Gère les cas où le produit n'existe pas.
    
* **Logs détaillés** : Suit à la fois les récupérations réussies et les produits manquants.
    

### Création du service `ListProducts` 

La méthode `ListProducts` récupère plusieurs produits avec un support pour la pagination. Cela fait également partie du **"R"** de CRUD (Read).

```cs
// Services/ProductService.cs
public override async Task<ListProductsResponse> ListProducts(
    ListProductsRequest request, 
    ServerCallContext context)
{
    try
    {
        // Définir les valeurs de pagination par défaut
        var pageSize = request.PageSize <= 0 ? 10 : Math.Min(request.PageSize, 100); // Max 100 articles par page
        var page = request.Page <= 0 ? 1 : request.Page;

        // Calculer le montant de saut (skip) pour la pagination
        var skip = (page - 1) * pageSize;

        // Obtenir le compte total pour les métadonnées de pagination
        var totalCount = await _dbContext.Products.CountAsync();

        // Récupérer les produits paginés
        var products = await _dbContext.Products
            .OrderBy(p => p.Created) // Tri cohérent
            .Skip(skip)
            .Take(pageSize)
            .ToListAsync();

        // Créer la réponse
        var response = new ListProductsResponse
        {
            Success = true,
            Message = products.Any() 
                ? $"Récupération de {products.Count} produits (Page {page} sur {Math.Ceiling((double)totalCount / pageSize)})"
                : "Aucun produit trouvé",
            TotalCount = totalCount
        };

        // Ajouter les produits à la réponse
        response.Products.AddRange(products.Select(MapToProductModel));

        _logger.LogInformation("Liste de {ProductCount} produits pour la page {Page}", products.Count, page);

        return response;
    }
    catch (Exception ex)
    {
        _logger.LogError(ex, "Erreur lors de la récupération de la liste des produits");
        
        return new ListProductsResponse
        {
            Success = false,
            Message = $"Erreur lors de la récupération des produits : {ex.Message}",
            TotalCount = 0
        };
    }
}
```

Voici les points clés de l'implémentation :

* **Logique de pagination** : Calcule les valeurs `skip` et `take` pour une récupération efficace des données.
    
* **Valeurs par défaut** : Définit des défauts raisonnables pour la taille de la page et le numéro de page.
    
* **Optimisation des performances** : Utilise `Skip()` et `Take()` pour la pagination au niveau de la base de données.
    
* **Tri cohérent** : `OrderBy()` assure des résultats prévisibles entre les requêtes.
    
* **Métadonnées** : Renvoie le compte total pour l'interface de pagination côté client.
    

### Création du service `UpdateProduct` 

La méthode `UpdateProduct` modifie des produits existants. C'est le **"U"** de CRUD (Update).

```cs
// Services/ProductService.cs
public override async Task<UpdateProductResponse> UpdateProduct(
    UpdateProductRequest request, 
    ServerCallContext context)
{
    try
    {
        // Valider l'ID du produit
        if (!Guid.TryParse(request.Id, out var productId))
        {
            return new UpdateProductResponse
            {
                Success = false,
                Message = "Format d'ID de produit invalide. Veuillez fournir un GUID valide."
            };
        }

        // Validation des entrées
        if (string.IsNullOrWhiteSpace(request.Name))
        {
            return new UpdateProductResponse
            {
                Success = false,
                Message = "Le nom du produit est requis"
            };
        }

        if (request.Price <= 0)
        {
            return new UpdateProductResponse
            {
                Success = false,
                Message = "Le prix du produit doit être supérieur à zéro"
            };
        }

        // Trouver le produit existant
        var existingProduct = await _dbContext.Products.FindAsync(productId);
        
        if (existingProduct == null)
        {
            return new UpdateProductResponse
            {
                Success = false,
                Message = "Produit non trouvé"
            };
        }

        // Mettre à jour les propriétés du produit
        existingProduct.Name = request.Name;
        existingProduct.Description = request.Description;
        existingProduct.Price = Convert.ToDecimal(request.Price);
        existingProduct.Tags = request.Tags;
        existingProduct.Updated = DateTime.UtcNow; // Suivre la date de mise à jour

        // Sauvegarder les changements en base de données
        await _dbContext.SaveChangesAsync();

        _logger.LogInformation("Produit mis à jour avec succès avec l'ID : {ProductId}", productId);

        // Renvoyer la réponse de succès avec le produit mis à jour
        return new UpdateProductResponse
        {
            Success = true,
            Message = "Produit mis à jour avec succès",
            Product = MapToProductModel(existingProduct)
        };
    }
    catch (Exception ex)
    {
        _logger.LogError(ex, "Erreur lors de la mise à jour du produit avec l'ID : {ProductId}", request.Id);
        
        return new UpdateProductResponse
        {
            Success = false,
            Message = $"Erreur lors de la mise à jour du produit : {ex.Message}"
        };
    }
}
```

Détails clés :

* **Vérification d'existence** : Vérifie que le produit existe avant de tenter une mise à jour.
    
* **Mises à jour sélectives** : Met à jour uniquement les champs fournis dans la requête.
    
* **Suivi d'horodatage** : Met à jour le champ `Updated` pour suivre le moment de la modification.
    
* **Validation des entrées** : Assure l'intégrité des données avant la sauvegarde.
    
* **Opération atomique** : Tous les changements sont sauvegardés ensemble ou pas du tout.
    

### Création du service `DeleteProduct` 

La méthode `DeleteProduct` supprime des produits de la base de données. C'est le **"D"** de CRUD (Delete).

```cs
 // Services/ProductService.cs
public override async Task<DeleteProductResponse> DeleteProduct(
    DeleteProductRequest request, 
    ServerCallContext context)
{
    try
    {
        // Valider l'ID du produit
        if (!Guid.TryParse(request.Id, out var productId))
        {
            return new DeleteProductResponse
            {
                Success = false,
                Message = "Format d'ID de produit invalide. Veuillez fournir un GUID valide."
            };
        }

        // Trouver le produit à supprimer
        var product = await _dbContext.Products.FindAsync(productId);
        
        if (product == null)
        {
            return new DeleteProductResponse
            {
                Success = false,
                Message = "Produit non trouvé"
            };
        }

        // Supprimer le produit de la base de données
        _dbContext.Products.Remove(product);
        await _dbContext.SaveChangesAsync();

        _logger.LogInformation("Produit supprimé avec succès avec l'ID : {ProductId}", productId);

        // Renvoyer une réponse de succès
        return new DeleteProductResponse
        {
            Success = true,
            Message = "Produit supprimé avec succès"
        };
    }
    catch (Exception ex)
    {
        _logger.LogError(ex, "Erreur lors de la suppression du produit avec l'ID : {ProductId}", request.Id);
        
        return new DeleteProductResponse
        {
            Success = false,
            Message = $"Erreur lors de la suppression du produit : {ex.Message}"
        };
    }
}
```

Détails clés :

* **Suppression logique vs physique** : Ceci implémente une suppression physique (retrait permanent).
    
* **Vérification d'existence** : Vérifie si le produit existe avant la suppression.
    
* **Retrait propre** : Utilise la méthode `Remove()` d'Entity Framework.
    
* **Confirmation** : Renvoie un message de succès confirmant la suppression.
    

### Implémentation complète de ProductService

Voici votre fichier `ProductService.cs` complet avec toutes les opérations CRUD :

```cs
// Services/ProductService.cs
using Grpc.Core;
using Microsoft.EntityFrameworkCore;
using ProductGrpc.Data;
using ProductGrpc.Models;

namespace ProductGrpc.Services
{
    public class ProductService : ProductsServiceProto.ProductsServiceProtoBase
    {
        private readonly AppDbContext _dbContext;
        private readonly ILogger<ProductService> _logger;

        public ProductService(AppDbContext dbContext, ILogger<ProductService> logger)
        {
            _dbContext = dbContext;
            _logger = logger;
        }

        // Méthode utilitaire pour mapper l'entité Product au message ProductModel
        private static ProductModel MapToProductModel(Product product)
        {
            return new ProductModel
            {
                Id = product.Id.ToString(),
                Name = product.Name,
                Description = product.Description,
                Price = (double)product.Price,
                CreatedAt = product.Created.ToString("yyyy-MM-ddTHH:mm:ssZ"),
                UpdatedAt = product.Updated.ToString("yyyy-MM-ddTHH:mm:ssZ"),
                Tags = product.Tags ?? string.Empty
            };
        }

        // Toutes les méthodes CRUD vont ici (telles qu'implémentées ci-dessus)
        // CreateProduct, GetProduct, ListProducts, UpdateProduct, DeleteProduct
    }
}
```

Excellent travail ! Vous avez implémenté avec succès toutes les opérations CRUD :

* **Create** : Ajouter de nouveaux produits avec validation.
    
* **Read** : Récupérer des produits individuels et des listes paginées.
    
* **Update** : Modifier des produits existants avec validation.
    
* **Delete** : Supprimer des produits en toute sécurité.
    

### Quelle est la suite ?

Maintenant que notre service gRPC est entièrement implémenté, nous devons le tester ! Dans la section suivante, nous apprendrons comment tester nos points de terminaison gRPC à l'aide de Postman.

## Comment tester les services gRPC avec Postman

Tester des services gRPC nécessite des outils et des approches différents de ceux des API REST traditionnelles. Alors que les API REST utilisent HTTP/1.1 avec des payloads JSON, gRPC utilise HTTP/2 avec des messages Protocol Buffer binaires. Heureusement, Postman offre un excellent support pour les tests gRPC, ce qui facilite le test de notre service sans écrire de code client.

### Pourquoi les tests gRPC sont différents

Voici un résumé des différences importantes entre les tests gRPC et les API REST :

| Aspect | API REST | gRPC |
| --- | --- | --- |
| **Protocole** | HTTP/1.1 | HTTP/2 |
| **Format de données** | JSON/XML | Protocol Buffers (Binaire) |
| **Schéma** | Optionnel (OpenAPI/Swagger) | Requis (fichiers .proto) |
| **Content-Type** | application/json | application/grpc |
| **Outils de test** | N'importe quel client HTTP | Clients gRPC spécialisés |

Pourquoi nous avons besoin du fichier proto :

* gRPC a besoin du contrat de service (fichier .proto) pour comprendre les méthodes disponibles.
    
* Les Protocol Buffers ont besoin de la définition du schéma pour la sérialisation/désérialisation.
    
* Postman utilise le fichier proto pour générer la structure correcte de requête/réponse.
    

### Configurer Postman pour les tests gRPC

#### Étape 1 : Lancer Postman

Ouvrez Postman sur votre machine. Vous devriez voir le tableau de bord principal semblable à ceci :

![Tableau de bord principal de Postman montrant l'interface de l'espace de travail](https://cdn.hashnode.com/res/hashnode/image/upload/v1753879108777/a98c6fa4-08c7-49f1-94a4-9138b69ad0a1.png align="left")

#### Étape 2 : Créer une nouvelle requête gRPC

Cliquez sur "New" dans le coin supérieur gauche ou utilisez le bouton "+". Sélectionnez ensuite "gRPC Request" parmi les options disponibles.

Vous devriez voir une boîte de dialogue modale avec différents types de requêtes :

![Fenêtre modale de nouvelle requête Postman montrant l'option gRPC](https://cdn.hashnode.com/res/hashnode/image/upload/v1753879545910/840f2004-73c5-4c1e-97a6-62b39eb278f9.png align="left")

Cliquez sur "gRPC Request" pour créer une nouvelle requête gRPC.

#### Étape 3 : Configurer l'interface de requête gRPC

Après avoir créé une requête gRPC, vous verrez l'interface de requête :

![Interface de requête Postman gRPC avec la section de définition de service](https://cdn.hashnode.com/res/hashnode/image/upload/v1753879652894/b339e198-27e9-4618-8cdb-54718da65841.png align="left")

Voici les composants notables de l'interface gRPC :

* **Server URL** : L'adresse où votre service gRPC est exécuté.
    
* **Service definition** : L'endroit où vous importez votre fichier .proto.
    
* **Method selection** : Choisissez quelle méthode RPC appeler.
    
* **Message body** : Payload de la requête basé sur les définitions proto.
    

### Importer le fichier Proto

#### Étape 4 : Accéder à la définition de service

Localisez la section "Service definition" dans l'interface de requête gRPC. Cliquez ensuite sur "Import .proto file" ou une option similaire.

![Section de définition de service où les fichiers proto sont importés](https://cdn.hashnode.com/res/hashnode/image/upload/v1753879690499/b2d53cab-3d0c-4c84-8a12-7777480e6860.png align="left")

#### Étape 5 : Importer votre fichier Proto

1. Cliquez sur le bouton "Select Files" ou "Import".
    
2. Naviguez vers le répertoire de votre projet.
    
3. Allez dans le dossier `Protos`.
    
4. Sélectionnez le fichier `product.proto`.
    
5. Cliquez sur "Open" pour importer.
    

**Structure du chemin de fichier :**

```bash
VotreProjet/
├── Protos/
│   ├── greet.proto
│   └── product.proto    ← Sélectionnez ce fichier
└── ...
```

#### Étape 6 : Configurer les paramètres d'importation

Lors de l'importation, vous verrez des options comme :

![Configuration de l'importation du fichier proto dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1753879892390/625b1fbd-cdd6-4437-af9e-441a39780c5e.png align="left")

**Configuration de l'importation :**

* **Import as** : Sélectionnez "API".
    
* **API name** : Choisissez un nom descriptif (par exemple, "ProductGrpc API").
    
* **Import location** : Sélectionnez votre espace de travail (workspace).
    

Il est préférable d'importer en tant qu'API car cela crée une définition d'API réutilisable, permet à plusieurs membres de l'équipe d'utiliser les mêmes définitions proto et offre une meilleure organisation pour plusieurs services.

#### Étape 7 : Vérifier l'importation réussie

Après une importation réussie, vous devriez voir :

1. **API Collection** : Votre API nommée apparaît dans la barre latérale gauche sous "APIs".
    
2. **Méthodes disponibles** : Toutes les méthodes RPC de votre fichier proto sont listées.
    
3. **Schémas de requête/réponse** : Postman comprend vos structures de messages.
    

![Fichier proto importé avec succès montrant les méthodes disponibles](https://cdn.hashnode.com/res/hashnode/image/upload/v1753879919558/a9c264a6-b021-4c7a-8221-557350c07f53.png align="left")

### Comprendre l'interface de requête gRPC

Une fois connecté, vous verrez une liste déroulante de sélection de méthodes avec les éléments suivants :

* CreateProduct
    
* GetProduct
    
* ListProducts
    
* UpdateProduct
    
* DeleteProduct
    

Excellent ! Vous avez réussi à créer une requête gRPC dans Postman, à importer votre fichier proto, à configurer la connexion au serveur et à mettre en place la collection d'API pour une réutilisation future.

### Quelle est la suite ?

Maintenant que Postman est configuré avec votre fichier proto, vous êtes prêt à tester chaque opération CRUD :

1. **CreateProduct** : Tester l'ajout de nouveaux produits.
    
2. **GetProduct** : Tester la récupération de produits individuels.
    
3. **ListProducts** : Tester la pagination et le listage.
    
4. **UpdateProduct** : Tester la modification de produits existants.
    
5. **DeleteProduct** : Tester la suppression de produits.
    

Dans la section suivante, nous passerons en revue le test de chaque opération avec des données d'exemple et les réponses attendues.

## Comment tester la création de produit

Maintenant que nous avons Postman configuré avec notre fichier proto, il est temps de tester notre service gRPC ! Nous allons commencer par tester la méthode `CreateProduct` pour ajouter un nouveau produit à notre base de données.

### Structure de la requête

Avant d'envoyer votre première requête dans Postman, sélectionnez la méthode RPC dans la liste déroulante. La forme du corps de la requête provient directement des définitions Protocol Buffer de votre fichier `.proto`. Postman affiche ces messages proto sous forme de JSON pour faciliter l'édition, mais les types proto s'appliquent toujours : chaque champ doit correspondre au type défini dans le schéma (y compris les messages imbriqués, les enums et les champs répétés).

### Étape 1 : Sélectionner la méthode CreateProduct

Ouvrez votre requête gRPC dans Postman et cliquez sur le menu déroulant des méthodes (il devrait afficher les méthodes disponibles). Sélectionnez "CreateProduct" dans la liste.

Vous devriez voir toutes les méthodes que nous avons définies dans notre fichier proto :

* CreateProduct
    
* GetProduct
    
* ListProducts
    
* UpdateProduct
    
* DeleteProduct
    

### Étape 2 : Schéma de la requête

Lorsque vous sélectionnez `CreateProduct`, Postman génère automatiquement la structure de la requête basée sur notre message `CreateProductRequest` du fichier proto :

**Rappel de la définition Proto :**

```csharp
message CreateProductRequest {
  string name = 1;
  string description = 2;
  double price = 3;
  string tags = 4;
}
```

**Représentation JSON dans Postman :**

```json
{
  "name": "",
  "description": "",
  "price": 0,
  "tags": ""
}
```

### Étape 3 : Préparer les données de test

Créons notre premier produit avec des données de test significatives. Dans le corps de la requête, saisissez :

```json
{
  "name": "MacBook Pro 16 pouces",
  "description": "Apple MacBook Pro avec puce M2 Pro, 16 Go de RAM, 512 Go de SSD",
  "price": 2499.99,
  "tags": "ordinateur portable, apple, professionnel"
}
```

À quoi correspondent ces champs ?

* **name** : Titre du produit (requis, chaîne de caractères).
    
* **description** : Informations détaillées sur le produit (chaîne de caractères).
    
* **price** : Coût du produit (double/nombre, doit être &gt; 0).
    
* **tags** : Mots-clés séparés par des virgules (chaîne de caractères).
    

### Étape 4 : Envoyer la requête

Cliquez sur le bouton "Invoke" (ou "Send" selon la version de Postman) et attendez la réponse (cela devrait être très rapide pour un test local). Vérifiez ensuite le statut de la réponse (cela devrait afficher un succès).

### Étape 5 : Analyser la réponse

Si tout fonctionne correctement, vous devriez recevoir une réponse comme celle-ci :

```json
{
  "success": true,
  "message": "Produit créé avec succès",
  "product": {
    "id": "920b98d2-4feb-4705-8303-ce6e28bd3694",
    "name": "MacBook Pro 16 pouces",
    "description": "Apple MacBook Pro avec puce M2 Pro, 16 Go de RAM, 512 Go de SSD",
    "price": 2499.99,
    "created_at": "2024-01-15T16:11:38Z",
    "updated_at": "2024-01-15T16:11:38Z",
    "tags": "ordinateur portable, apple, professionnel"
  }
}
```

Champs de réponse :

* **success** : Booléen indiquant le succès de l'opération.
    
* **message** : Message de statut lisible par l'homme.
    
* **product** : Le produit créé avec les champs générés.
    
    * **id** : GUID généré automatiquement.
        
    * **created\_at/updated\_at** : Horodatages UTC.
        
    * **Autres champs** : Écho des données d'entrée.
        

### Confirmation visuelle dans Postman

Voici à quoi ressemble une requête réussie dans Postman :

![Interface Postman montrant la création réussie d'un produit avec requête et réponse](https://cdn.hashnode.com/res/hashnode/image/upload/v1753880143034/f7e81267-8d45-4835-b1d9-ad091563b99c.png align="left")

Félicitations ! Vous avez réussi à effectuer votre première requête gRPC avec Postman ! Vous avez également créé un produit dans la base de données, reçu une réponse correctement formatée et vérifié l'ID et les horodatages générés automatiquement.

### Quelle est la suite ?

Maintenant que nous avons testé avec succès la création de produit, testons les autres opérations CRUD :

1. **GetProduct** : Récupérer le produit que nous venons de créer.
    
2. **ListProducts** : Voir tous les produits avec pagination.
    
3. **UpdateProduct** : Modifier le produit existant.
    
4. **DeleteProduct** : Supprimer le produit de la base de données.
    

Chaque opération nous aidera à vérifier que notre service gRPC complet fonctionne correctement.

## Comment tester toutes les opérations de produit

Maintenant que nous avons créé un produit avec succès, testons toutes les opérations CRUD restantes pour nous assurer que notre service gRPC complet fonctionne correctement.

### Obtenir tous les produits (ListProducts)

La méthode `ListProducts` récupère tous les produits de notre base de données avec un support pour la pagination. Puisque nous avons créé des produits, nous devrions être en mesure de les voir dans la réponse.

#### Étape 1 : Sélectionner la méthode ListProducts

Cliquez sur le menu déroulant des méthodes dans votre requête gRPC Postman. Sélectionnez ensuite "ListProducts" parmi les méthodes disponibles. Notez la structure de la requête – elle inclut des paramètres de pagination.

#### Étape 2 : Configurer la requête

`ListProductsRequest` supporte des paramètres de pagination :

```json
{
  "page": 1,
  "pageSize": 10
}
```

Voici ce qui se passe avec ces paramètres :

* **page** : La page de résultats à récupérer (par défaut : 1).
    
* **pageSize** : Nombre de produits par page (par défaut : 10, max : 100).
    

#### Étape 3 : Envoyer la requête

Cliquez sur "Invoke" pour envoyer la requête et attendez la réponse contenant tous vos produits.

#### Étape 4 : Réponse

Vous devriez recevoir une réponse semblable à celle-ci :

```json
{
  "success": true,
  "message": "Récupération de 2 produits (Page 1 sur 1)",
  "totalCount": 2,
  "products": [
    {
      "id": "920b98d2-4feb-4705-8303-ce6e28bd3694",
      "name": "MacBook Pro 16 pouces",
      "description": "Apple MacBook Pro avec puce M2 Pro, 16 Go de RAM, 512 Go de SSD",
      "price": 2499.99,
      "created_at": "2024-01-15T16:11:38Z",
      "updated_at": "2024-01-15T16:11:38Z",
      "tags": "ordinateur portable, apple, professionnel"
    },
    {
      "id": "a1b2c3d4-5e6f-7890-abcd-ef1234567890",
      "name": "iPhone 15 Pro",
      "description": "Dernier iPhone avec design en titane",
      "price": 999.99,
      "created_at": "2024-01-15T16:15:22Z",
      "updated_at": "2024-01-15T16:15:22Z",
      "tags": "smartphone, apple, premium"
    }
  ]
}
```

Structure de la réponse :

* **success** : Statut de l'opération.
    
* **message** : Message descriptif avec informations de pagination.
    
* **totalCount** : Nombre total de produits dans la base de données.
    
* **products** : Tableau d'objets produits.
    

![Postman montrant la récupération réussie de tous les produits avec pagination](https://cdn.hashnode.com/res/hashnode/image/upload/v1753880306062/af0bd1d4-24d0-4be8-96a1-f59404f36672.png align="left")

### Tester la pagination

Testons maintenant différents scénarios de pagination :

**Obtenir les 5 premiers produits :**

```json
{
  "page": 1,
  "pageSize": 5
}
```

**Obtenir la deuxième page :**

```json
{
  "page": 2,
  "pageSize": 5
}
```

### Obtenir un produit par ID (GetProduct)

La méthode `GetProduct` récupère un seul produit en utilisant son ID unique. Contrairement aux API REST, où l'ID fait partie du chemin de l'URL, gRPC transmet l'ID dans le corps du message.

#### Étape 1 : Sélectionner la méthode GetProduct

Sélectionnez "GetProduct" dans la liste déroulante des méthodes. Notez que la structure de la requête nécessite un champ ID.

#### Étape 2 : Préparer la requête

Copiez un ID de produit à partir de votre réponse `ListProducts` précédente :

```json
{
  "id": "920b98d2-4feb-4705-8303-ce6e28bd3694"
}
```

Notes importantes :

* **Format de l'ID** : Doit être une chaîne GUID valide.
    
* **Sensibilité à la casse** : Les GUID ne sont pas sensibles à la casse.
    
* **Validation** : Les GUID invalides renverront une erreur.
    

#### Étape 3 : Envoyer la requête

Collez un ID de produit valide de votre réponse ListProducts. Cliquez sur "Invoke" pour envoyer la requête.

#### Étape 4 : Analyser la réponse

Réponse réussie :

```json
{
  "success": true,
  "message": "Produit récupéré avec succès",
  "product": {
    "id": "920b98d2-4feb-4705-8303-ce6e28bd3694",
    "name": "MacBook Pro 16 pouces",
    "description": "Apple MacBook Pro avec puce M2 Pro, 16 Go de RAM, 512 Go de SSD",
    "price": 2499.99,
    "created_at": "2024-01-15T16:11:38Z",
    "updated_at": "2024-01-15T16:11:38Z",
    "tags": "ordinateur portable, apple, professionnel"
  }
}
```

![Postman montrant la récupération réussie d'un seul produit par ID](https://cdn.hashnode.com/res/hashnode/image/upload/v1753880592637/ebbacee5-1333-4328-8c46-ab7dd24d824d.png align="left")

### Mettre à jour un produit (UpdateProduct)

La méthode `UpdateProduct` modifie un produit existant. Vous devez fournir l'ID du produit et les champs que vous souhaitez mettre à jour.

#### Étape 1 : Sélectionner la méthode UpdateProduct

Sélectionnez "UpdateProduct" dans le menu déroulant. Examinez la structure de la requête qui inclut l'ID et tous les champs modifiables.

#### Étape 2 : Préparer la requête de mise à jour

```json
{
  "id": "920b98d2-4feb-4705-8303-ce6e28bd3694",
  "name": "MacBook Pro 16 pouces (Mis à jour)",
  "description": "Apple MacBook Pro avec puce M2 Pro, 16 Go de RAM, 1 To de SSD - Stockage mis à jour",
  "price": 2799.99,
  "tags": "ordinateur portable, apple, professionnel, mis à jour"
}
```

Directives de mise à jour :

* **ID** : Doit correspondre à un produit existant.
    
* **Tous les champs** : Actuellement requis (pas de mises à jour partielles).
    
* **Prix** : Doit être supérieur à 0.
    
* **Nom** : Ne peut pas être vide.
    

#### Étape 3 : Envoyer la requête de mise à jour

Assurez-vous que l'ID existe (utilisez-en un de votre réponse ListProducts). Cliquez ensuite sur "Invoke" pour envoyer la mise à jour.

#### Étape 4 : Vérifier la mise à jour

Réponse réussie :

```json
{
  "success": true,
  "message": "Produit mis à jour avec succès",
  "product": {
    "id": "920b98d2-4feb-4705-8303-ce6e28bd3694",
    "name": "MacBook Pro 16 pouces (Mis à jour)",
    "description": "Apple MacBook Pro avec puce M2 Pro, 16 Go de RAM, 1 To de SSD - Stockage mis à jour",
    "price": 2799.99,
    "created_at": "2024-01-15T16:11:38Z",
    "updated_at": "2024-01-15T16:25:14Z",
    "tags": "ordinateur portable, apple, professionnel, mis à jour"
  }
}
```

Notez les changements :

* **updated\_at** : L'horodatage a changé pour refléter la mise à jour.
    
* **Champs modifiés** : Tous les champs mis à jour reflètent les nouvelles valeurs.
    
* **created\_at** : Reste inchangé (heure de création originale).
    

![Postman montrant la mise à jour réussie d'un produit avec les champs modifiés](https://cdn.hashnode.com/res/hashnode/image/upload/v1753880928160/d12e58ff-3c14-49f6-a3dd-1d1d2c452e09.png align="left")

### Supprimer un produit par ID (DeleteProduct)

La méthode `DeleteProduct` supprime définitivement un produit de la base de données en utilisant son ID.

#### Étape 1 : Sélectionner la méthode DeleteProduct

Sélectionnez "DeleteProduct" dans le menu déroulant. Notez la structure simple de la requête – elle ne nécessite qu'un ID.

#### Étape 2 : Préparer la requête de suppression

```json
{
  "id": "a1b2c3d4-5e6f-7890-abcd-ef1234567890"
}
```

**⚠️ Attention** : Cette opération supprime définitivement le produit. Assurez-vous d'utiliser le bon ID.

#### Étape 3 : Envoyer la requête de suppression

Vérifiez deux fois l'ID du produit que vous souhaitez supprimer. Cliquez sur "Invoke" pour envoyer la requête de suppression.

#### Étape 4 : Confirmer la suppression

Réponse réussie :

```json
{
  "success": true,
  "message": "Produit supprimé avec succès"
}
```

Étapes de vérification :

1. **Essayez GetProduct** avec le même ID – il devrait renvoyer "Produit non trouvé".
    
2. **Exécutez ListProducts** – le produit ne devrait plus apparaître dans la liste.
    
3. **Vérifiez totalCount** – il devrait être réduit de 1.
    

![Postman montrant la suppression réussie d'un produit](https://cdn.hashnode.com/res/hashnode/image/upload/v1753880987953/23bb19f0-7ca0-4cec-b9bb-3774737f98c9.png align="left")

## Conclusion

Félicitations ! 🎉 Vous avez terminé avec succès ce voyage complet dans la construction de services gRPC avec ASP.NET Core. Tout au long de ce manuel, vous avez acquis une expérience pratique de l'un des Frameworks de communication les plus puissants et efficaces disponibles pour les applications distribuées modernes.

### Ce que vous avez accompli

Récapitulons les compétences et connaissances impressionnantes que vous avez acquises :

#### Construction des fondations

* Mise en place d'un projet gRPC complet à partir de zéro avec la CLI .NET.
    
* Configuration d'une base de données SQLite avec Entity Framework Core.
    
* Création de modèles de données robustes avec validation appropriée.
    
* Implémentation des migrations de base de données et du seeding.
    

#### Apprentissage des Protocol Buffers

* Conception de fichiers .proto complets avec définitions de services.
    
* Création de contrats de messages fortement typés pour toutes les opérations CRUD.
    
* Compréhension des avantages de la sérialisation binaire par rapport au JSON.
    
* Implémentation d'objets de transfert de données (DTO) efficaces.
    

#### Implémentation du service

* Construction d'un ProductService complet avec toutes les opérations CRUD.
    
* Implémentation d'une gestion des erreurs et d'une validation appropriées.
    
* Ajout de logs complets pour le débogage et la surveillance.
    
* Création d'une pagination efficace pour les grands jeux de données.
    
* Gestion du mapping des données entre les entités et les messages Protocol Buffer.
    

#### Test et validation

* Configuration de Postman pour les tests gRPC.
    
* Test de toutes les opérations CRUD avec des données réelles.
    
* Vérification de l'intégrité des données et du formatage correct des réponses.
    

### Compétences techniques clés acquises

**Expertise gRPC :**

* Compréhension des avantages du protocole HTTP/2.
    
* Conception et évolution de schémas Protocol Buffer.
    
* Modèles de communication de service à service.
    
* Techniques d'optimisation des performances.
    

#### 🔗 Vous pouvez accéder au code [dans ce Répertoire GitHub](https://github.com/Clifftech123/IsaiahCliffordOpokuBlog).

### Merci !

Merci d'avoir suivi ce tutoriel complet. Votre dévouement à l'apprentissage de ces concepts avancés vous servira grandement dans la construction de la prochaine génération d'applications distribuées.

**Bon codage, et que vos services soient rapides, fiables et évolutifs !**

Si vous souhaitez en savoir plus sur .NET Core, vous pouvez vous abonner à ma chaîne YouTube [ici](https://youtube.com/@clifftech?si=QgdE39q4iYIPEN23).

**🔗 Connectez-vous avec l'auteur :**

* GitHub : [@CliffTech123](https://github.com/Clifftech123)
    
* Twitter : [@Clifftech\_Dev](https://x.com/Clifftech_Dev)
    
* LinkedIn : [Isaiah Clifford Opoku](https://www.linkedin.com/in/isaiah-clifford-opoku/)