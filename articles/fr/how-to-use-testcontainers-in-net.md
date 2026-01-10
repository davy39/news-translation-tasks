---
title: Comment utiliser TestContainers dans .Net
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2025-03-25T15:30:05.104Z'
originalURL: https://freecodecamp.org/news/how-to-use-testcontainers-in-net
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1742773343798/44c64acc-3862-4325-af21-6b7de417d300.jpeg
tags:
- name: C#
  slug: csharp
- name: Testcontainers
  slug: testcontainers
- name: Testing
  slug: testing
- name: Integration Testing
  slug: integration-testing
- name: Tutorial
  slug: tutorial
seo_title: Comment utiliser TestContainers dans .Net
seo_desc: At some point in your development lifecycle, you will need to test that
  your system can integrate with another system, whether it be another API, a database,
  or caching service, for example. This can be a laborious task of spinning up other
  servers h...
---

À un moment donné dans votre cycle de développement, vous devrez tester que votre système peut s'intégrer avec un autre système, qu'il s'agisse d'une autre API, d'une base de données ou d'un service de cache, par exemple. Cela peut être une tâche fastidieuse de démarrer d'autres serveurs hébergeant la réplique de l'API tierce, ou d'héberger en permanence une base de données SQL alimentée avec des données de test.

Dans cet article, je vais vous apprendre à utiliser la bibliothèque TestContainers pour rendre l'exécution des tests d'intégration beaucoup plus facile et plus gérable.

## Table des matières

* [Prérequis](#heading-prerequisites)
    
* [Qu'est-ce que TestContainers ?](#heading-questce-que-testcontainers)
    
* [Comment tout cela fonctionne-t-il ?](#heading-comment-tout-cela-fonctionne-t-il)
    
* [Comment configurer votre premier test](#heading-comment-configurer-votre-premier-test)
    
* [Comportements clés de IAsyncLifetime dans une classe de test](#heading-comportements-cles-de-iasynclifetime-dans-une-classe-de-test)
    
* [Comment améliorer les performances](#heading-comment-ameliorer-les-performances)
    
* [Explication des différences](#heading-explication-des-differences)
    
* [Comment partager votre conteneur entre plusieurs classes de test](#heading-comment-partager-votre-conteneur-entre-plusieurs-classes-de-test)
    
* [Résumé des approches](#heading-resume-des-approches)
    
* [Comment créer plusieurs conteneurs](#heading-comment-creer-plusieurs-conteneurs)
    
* [Comment simplifier votre configuration avec des images personnalisées](#heading-comment-simplifier-votre-configuration-avec-des-images-personnalisees)
    
* [Réflexions finales](#heading-reflexions-finales)
    

## Prérequis

* Compréhension de Docker
    
* Compréhension de xUnit et des tests
    
* Installation des packages suivants :
    
    * `TestContainers`
        
    * `TestContainers.MsSql`
        
    * xUnit
        
    * >= .Net 8
        
    * `FluentAssertions`
        
    * `Microsoft.Data.SqlClient`
        

## Qu'est-ce que TestContainers ?

[TestContainers](https://testcontainers.com) est une bibliothèque open source qui vous fournit des instances de conteneurs facilement jetables pour des choses comme l'hébergement de bases de données, les brokers de messages, les navigateurs et plus encore - essentiellement tout ce qui peut s'exécuter dans un conteneur Docker.

Elle élimine la nécessité de maintenir des environnements hébergés pour les tests dans le cloud ou sur des machines locales. Tant que la machine de l'utilisateur et l'hôte CI/CD supportent Docker, les tests TestContainer peuvent facilement être exécutés.

## Comment tout cela fonctionne-t-il ?

Vous définissez l'image que vous souhaitez utiliser et spécifiez une configuration.

La bibliothèque TestContainer démarre un conteneur Docker avec l'image configurée.

### **Fournit les détails de connexion**

Après avoir démarré le conteneur, TestContainers expose les chaînes de connexion (par exemple, une URL de connexion à la base de données), afin que vos tests puissent utiliser le service réel, plutôt que de devoir configurer cela vous-même.

### **Nettoie automatiquement**

Lorsque le test se termine, TestContainers supprime automatiquement le conteneur, garantissant qu'il n'y a pas de ressources résiduelles. C'est l'une des meilleures choses à propos de l'utilisation de TestContainers : toute la création, la suppression et la configuration du conteneur sont gérées dans la bibliothèque elle-même, ce qui la rend parfaite pour une utilisation dans les pipelines de livraison.

## Comment configurer votre premier test

Pour les besoins de ce tutoriel, nous allons garder les choses simples et n'utiliser qu'une image `MS Sql Server`.

La première chose que nous allons faire est de configurer notre conteneur Docker Microsoft SQL Server via l'API fluide TestContainer.

Créez votre classe de test comme ci-dessous :

```csharp
public class IntegrationTests: IAsyncLifetime 
{
    private MsSqlContainer _container;
    private FakeLogger _logger

    public async Task InitializeAsync()
    {
           _container = new MsSqlBuilder()
                .WithImage("mcr.microsoft.com/mssql/server:2022-latest")
                .WithPassword("P@ssw0rd123")
                .WithPortBinding(1443)
                .WithWaitStrategy(Wait.ForUnixContainer().UntilPortIsAvailable(1433))
                .Build();

            _logger = new FakeLogger();
    }

    public async Task DisposeAsync() => await _container.DisposeAsync();
}
```

Ici, nous utilisons l'interface `IAsyncLifetime` de xUnit. C'est une interface dans xUnit qui fournit un moyen de gérer la configuration et le nettoyage asynchrones pour les classes de test. Elle est utile lorsque vous devez initialiser et nettoyer des ressources de manière asynchrone. Nous utilisons la méthode `InitializeAsync()` pour configurer et définir notre conteneur de base de données Microsoft SQL ainsi que pour démarrer le conteneur, puis nous utilisons la méthode `DisposeAsync()` pour arrêter et supprimer notre conteneur.

### Explication des méthodes du constructeur

* `WithImage()` : cela nous permet de spécifier l'image que nous voulons que Docker télécharge et exécute. Nous avons opté pour la dernière version de SQL Server 2022.
    
* `WithPassword()` : Cela nous permet de spécifier le mot de passe pour la base de données (lors de la création de la plupart des bases de données, un mot de passe est généralement requis).
    
* `WithPortBinding()` : Cela nous permet de spécifier à la fois le numéro de port d'hébergement sur votre machine, ainsi que le numéro de port du conteneur.
    
* `WithWaitStrategy()` : Ici, nous pouvons spécifier une stratégie d'attente, qui informe notre conteneur d'attendre une condition avant que le conteneur soit prêt à être utilisé. Cela est important car certains services (comme les bases de données ou les API) prennent du temps à démarrer complètement.
    
* `Build()` : C'est la commande qui construit le conteneur de test en fonction de la configuration. Cela **ne** démarre **pas** ou ne lance **pas** le conteneur - vous pouvez le faire en utilisant la méthode `container.StartAsync()` comme mentionné précédemment.
    

#### **Pourquoi** `WithWaitStrategy()` **est-il nécessaire ?**

Par défaut, TestContainers suppose que le conteneur est prêt dès qu'il commence à s'exécuter. Mais certains services peuvent :

* Prendre du temps pour s'initialiser.
    
* Nécessiter un message de journal spécifique avant d'être prêts.
    
* Avoir besoin qu'un port soit accessible avant de pouvoir se connecter.
    

En utilisant `WithWaitStrategy()`, vous pouvez personnaliser la manière dont TestContainers attend avant de considérer le conteneur comme "prêt".

### Ajout du test

```csharp
public class IntegrationTests: IAsyncLifetime 
{
    private MsSqlContainer _container;
    private FakeLoger _logger;

    public async Task InitializeAsync()
    {
           _container = new MsSqlBuilder()
                .WithImage("mcr.microsoft.com/mssql/server:2022-latest")
                .WithPassword("P@ssw0rd123")
                .WithPortBinding(1443)
                .WithWaitStrategy(Wait.ForUnixContainer().UntilPortIsAvailable(1433))
                .Build();

            await _container.StartAsync();
            _logger = new FakeLogger();
    }

    public async Task DisposeAsync() => await _container.DisposeAsync();

    [Fact]
    public async Task Test_Database_Connection()
    {
        var connectionString = _container.GetConnectionString();
        using var conn = new SqlConnection(connectionString);
        await conn.OpenAsync();
        
        Assert.True(conn.State == System.Data.ConnectionState.Open);
    }
}
```

Le test ci-dessus, bien qu'il soit simple, illustre à quel point il est facile de démarrer un conteneur et de créer un test simple. Le test ci-dessus fonctionnera, mais il peut conduire à des tests de faible performance et à une utilisation élevée des ressources de la machine s'il n'est pas utilisé correctement. Laissez-moi expliquer :

L'utilisation de `IAsyncLifetime` est nécessaire, car nous appelons des méthodes de configuration asynchrones (`StartAsync`), par exemple. Mais les méthodes `InitializeAsync() / DisposeAsync()` lorsqu'elles sont situées dans une classe de test sont exécutées avant et après chaque test (`Fact` dans xUnit).

Cela signifie que chaque fois qu'un test commence, il :

* crée un tout nouveau conteneur Docker,
    
* télécharge l'image MS Sql,
    
* crée la base de données,
    
* exécute les tests, et
    
* supprime le conteneur.
    

Vous pouvez tester cela en copiant et collant le test `Test_Database_Connection()` ci-dessus plusieurs fois, en ajoutant un numéro à chaque test dupliqué (pour satisfaire le compilateur), et en ouvrant Docker Desktop. En exécutant tous les tests, vous verrez un nouveau conteneur (avec un nom différent) être créé pour chaque exécution de test.

Maintenant, cela peut être acceptable si vous avez un nombre limité de tests dans votre classe de test. Mais cela peut avoir des conséquences négatives sur les classes de test avec un plus grand nombre de tests, ce qui signifie que la maintenance et la planification des tests sont essentielles. C'est utile, cependant, lorsque vous voulez vous assurer que la base de données est dans un état complètement propre avant chaque test, garantissant qu'il n'y a pas de contamination des données par d'autres tests en cours d'exécution.

## **Comportements clés de** `IAsyncLifetime` **dans une classe de test**

Lorsque votre classe de test implémente `IAsyncLifetime`, le comportement par défaut de xUnit est :

1. Crée une nouvelle instance de la classe de test pour chaque méthode de test.  
2. Appelle `InitializeAsync()` avant chaque test.  
3. Appelle `DisposeAsync()` après chaque test.

### **Que signifie cela pour TestContainers ?**

* Dans notre cas, puisque `InitializeAsync()` configure un nouveau conteneur, un nouveau conteneur est créé pour chaque test.
    
* `DisposeAsync()` arrête le conteneur après chaque test.
    
* Assure un état de base de données complètement frais pour chaque test, évitant la contamination des données.
    
* Est lent et consomme beaucoup de ressources, surtout si vous avez de nombreuses méthodes de test.
    

Une vue plus visuelle d'une classe de test pourrait ressembler à ceci :

🏆 InitializeAsync() → Nouveau conteneur créé (Pour Test_1)

🧪 Exécution de Test_1

💣 DisposeAsync() → Conteneur arrêté (Après Test_1)

🏆 InitializeAsync() → Nouveau conteneur créé (Pour Test_2)

🧪 Exécution de Test_2

💣 DisposeAsync() → Conteneur arrêté (Après Test_2)

### **Quand est-ce utile ?**

* Vous avez besoin d'un état de base de données ou d'un conteneur complètement frais pour chaque test.
    
* Évite la contamination des données de test.
    
* Chaque test commence à partir d'une ardoise propre.
    

### **Quand est-ce un problème ?**

* Cela entraîne une exécution lente - un nouveau conteneur est démarré pour chaque test.
    
* C'est gourmand en ressources - plusieurs conteneurs s'exécutent séquentiellement.
    
* Et ce n'est pas évolutif - des centaines de tests prendront beaucoup de temps à s'exécuter.
    

## Comment améliorer les performances

D'accord, nous avons donc vu comment créer des conteneurs une fois par test, et exploré des scénarios où cela serait utile, mais que faire si les performances et les coûts sont une préoccupation ?

Ici, nous pouvons combiner `IClassFixture` et `IAsyncLiftetime` pour atteindre une approche *une fois par classe de test*, où nous créons un conteneur et une base de données, et leur cycle de vie est la durée complète de la classe de test (c'est-à-dire que tous les tests s'exécutent contre la même base de données).

### Comment écrire cela

Nous pouvons utiliser une classe TestFixture qui hérite de l'interface IAsyncLifetime, exposant les méthodes `InitializeAsync()` et `DisposeAsync()` comme avant.

```csharp
using DotNet.Testcontainers.Builders;
using Microsoft.Extensions.Logging.Testing;
using Testcontainers.MsSql;

namespace IntegrationTests;

public class TestClassFixture : IAsyncLifetime
{
    public MsSqlContainer Container { get; set; }
    private FakeLogger _logger;

    public async Task InitializeAsync()
    {
        Container = new MsSqlBuilder()
            .WithImage("mcr.microsoft.com/mssql/server:2022-latest")
            .WithPassword("P@ssw0rd123")
            .WithPortBinding(1443)
            .WithWaitStrategy(Wait.ForUnixContainer().UntilPortIsAvailable(1433))
            .Build();

        _logger = new FakeLogger();
        await Container.StartAsync();
    }

    public async Task DisposeAsync()
    {
        await Container.DisposeAsync();
    }
}
```

En utilisant l'interface `IClassFixture` de xUnit, nous pouvons passer notre `TestClassFixture` et faire en sorte que notre classe de test hérite de celle-ci. Une fixture de test n'est exécutée qu'une fois par classe de test, ce qui la rend parfaite pour notre scénario.

```csharp

public class IntegrationFixtureTests : IClassFixture<TestClassFixture>
{
    private readonly string _connectionString;

    public IntegrationFixtureTests(TestClassFixture testClassFixture)
    {
        _connectionString = testClassFixture.Container.GetConnectionString();

        // autre configuration spécifique à la classe de test va ici
    }

    [Fact]
    public async Task Test_Database_Connection()
    {
        await using var conn = new SqlConnection(_connectionString);
        await conn.OpenAsync();

        Assert.True(conn.State == System.Data.ConnectionState.Open);
    }
}
```

Nous avons maintenant une classe de test beaucoup plus propre, et toute notre logique de conteneur est gérée par `IClassFixture` à la place. Si vous devez ajouter du code spécifique à la classe de test, par exemple pour alimenter la base de données avant l'exécution, ou pour mock des ressources, vous pouvez placer ce code dans le constructeur.

## Explication des différences

Nous avons défini notre propriété `Container` comme publique, plutôt que privée, afin que notre classe de test puisse accéder au conteneur. La fixture de test est injectée par les mécanismes internes d'injection de dépendances de xUnit lorsque vous utilisez `IClassFixture<T>`.

xUnit crée automatiquement une instance de la classe de fixture et la passe dans le constructeur de la classe de test.

Le conteneur est démarré dans la méthode `InitializeAsync()` sur la **TestFixture** maintenant, plutôt que dans la classe de test, ce qui signifie qu'il n'est démarré qu'une seule fois et est prêt à être utilisé pour tous les tests. Cela améliore les performances et la vitesse des tests (plus d'attente pour que chaque conteneur se lance avant chaque test).

Le flux de test ressemblerait maintenant à quelque chose comme ceci :

🏆 InitializeAsync() → Conteneur créé → Conteneur démarré

🧪 Exécution de Test_1

🧪 Exécution de Test_2

💣 DisposeAsync() → Conteneur arrêté → Conteneur supprimé

### Avantages et inconvénients

#### ✅ **Exécution plus rapide**

Réduit considérablement les frais généraux de configuration/nettoyage, surtout lors de l'utilisation de services à démarrage lent comme les bases de données.

#### ✅ **Utilisation moindre des ressources**

L'exécution d'un conteneur une fois par classe de test consomme beaucoup moins de ressources système par rapport à un conteneur par test. Cela est particulièrement bénéfique lors de l'exécution de tests d'intégration dans des pipelines CI/CD où l'utilisation des ressources doit être optimisée pour garder les coûts bas.

#### ✅ **Tests plus réalistes**

Dans des scénarios réels, les applications ne redémarrent pas leurs bases de données entre les appels API, alors pourquoi vos tests d'intégration devraient-ils le faire ?

#### ❌ **Contamination des données**

Une gestion efficace des données de test est essentielle pour maintenir des tests fiables. Si les données de test ne sont pas correctement isolées, cela peut entraîner des interférences non intentionnelles entre les tests.

Par exemple, un test qui crée un nouvel enregistrement peut introduire des données inattendues, provoquant l'échec d'un test de récupération s'il s'exécute ensuite. Ce type de contamination des données est un problème courant lorsque tous les tests d'une classe de test partagent la même configuration de base de données. Mais, avec une conception de test minutieuse—comme une isolation appropriée des données, des stratégies de nettoyage, ou l'utilisation de rollbacks transactionnels—ces problèmes peuvent être atténués ou entièrement évités.

#### ❌ **Plus de précautions doivent être prises concernant l'idempotence**

L'« idempotence » fait référence à la capacité d'exécuter n'importe quel test de manière indépendante dans n'importe quel ordre. Si la classe de test accède à des données provenant des mêmes zones, les assertions peuvent échouer lorsqu'elles sont exécutées dans certains ordres plutôt que dans d'autres. Par exemple :

* Test_1 insère un enregistrement.
    
* Test_2 suppose que la table est vide et affirme que `QueryByName()` doit retourner 1 enregistrement
    
* Test_2 échoue parce que Test_1 a déjà inséré son propre enregistrement
    

## Comment partager votre conteneur entre plusieurs classes de test

Nous avons donc couvert un conteneur par test et un conteneur par classe de test. Mais qu'en est-il de partager un conteneur pour plusieurs classes de test ? Eh bien, c'est aussi simple que d'utiliser l'interface `ICollectionFixture` au lieu de `IClassFixture`, et elle peut être utilisée comme suit :

```csharp
[CollectionDefinition("Database collection")]
public class DatabaseCollection : ICollectionFixture<TestClassFixture>
{
    // Cette classe n'a pas de code,
    // elle est juste utilisée pour appliquer l'attribut [Collection] aux classes de test.
}
```

Le mécanisme `ICollectionFixture<T>` dans xUnit lie automatiquement l'instance de la fixture à toutes les classes de test marquées avec l'attribut `[Collection("Collection Name")]`, par exemple :

```csharp
using IntegrationTests;
using Microsoft.Data.SqlClient;

[Collection("Database collection")]
public class IntegrationFixtureTests
{
    private readonly string _connectionString;

    public IntegrationFixtureTests(TestClassFixture testClassFixture)
    {
        _connectionString = testClassFixture.Container.GetConnectionString();
    }

    [Fact]
    public async Task Test_Database_Connection()
    {
        await using var conn = new SqlConnection(_connectionString);
        await conn.OpenAsync();

        Assert.True(conn.State == System.Data.ConnectionState.Open);
    }
}

[Collection("Database collection")]
public class AnotherIntegrationTest
{
    private readonly string _connectionString;

    public AnotherIntegrationTest(TestClassFixture testClassFixture)
    {
        _connectionString = testClassFixture.Container.GetConnectionString();
    }

    [Fact]
    public async Task Another_Database_Test()
    {
        await using var conn = new SqlConnection(_connectionString);
        await conn.OpenAsync();

        Assert.True(conn.State == System.Data.ConnectionState.Open);
    }
}
```

Vous pouvez maintenant regrouper vos tests d'intégration, qu'il s'agisse de tous les tests de lecture ou de tous les tests d'écriture - rendant vos tests beaucoup plus maintenables.

## Résumé des approches :

| **Approche** | **Création de conteneur** | **Meilleur pour** |
| --- | --- | --- |
| `IAsyncLifetime` à l'intérieur de la classe de test | **Un par test** | Lorsqu'un état de base de données frais par test est nécessaire, évitant la contamination des tests |
| `IClassFixture<T>` avec `IAsyncLifetime` | **Un par classe de test** | Exécution plus rapide, partage de l'instance de la base de données entre les tests d'une classe |
| `ICollectionFixture<T>` avec `IAsyncLifetime` | **Un pour plusieurs classes de test** | Partage d'une instance de base de données entre différentes classes de test |

## Comment créer plusieurs conteneurs

Oui, vous pouvez créer plusieurs conteneurs qui peuvent héberger différentes images, ce qui est parfait lorsque vous avez plusieurs systèmes avec lesquels vous devez vous intégrer - par exemple Microsoft SQL Server et une instance Redis.

Vous pouvez le faire en appelant le constructeur du package TestContainer pertinent comme ci-dessous :

```csharp
public class TestContainersFixture : IAsyncLifetime
{
    public MsSqlContainer SqlContainer { get; private set; }
    public RedisContainer RedisContainer { get; private set; }

    public async Task InitializeAsync()
    {
        // Conteneur SQL Server
        SqlContainer = new MsSqlBuilder()
            .WithImage("mcr.microsoft.com/mssql/server:2022-latest")
            .WithPassword("P@ssw0rd123")
            .WithPortBinding(1433)
            .WithWaitStrategy(Wait.ForUnixContainer().UntilPortIsAvailable(1433))
            .Build();

        // Conteneur Redis
        RedisContainer = new RedisContainerBuilder()
            .WithImage("redis:latest")
            .WithPortBinding(6379)
            .WithWaitStrategy(Wait.ForUnixContainer().UntilPortIsAvailable(6379))
            .Build();

        await Task.WhenAll(SqlContainer.StartAsync(), RedisContainer.StartAsync());
    }

    public async Task DisposeAsync()
    {
        await Task.WhenAll(SqlContainer.DisposeAsync(), RedisContainer.DisposeAsync());
    }
}
```

Et voilà, nous avons une instance SQL Server et une instance Redis prêtes pour les tests d'intégration.

## Comment simplifier votre configuration avec des images personnalisées

Pour faciliter les tests et tirer parti de la puissance de Docker et de TestContainers, voici un excellent conseil. TestContainers prend entièrement en charge l'utilisation d'images personnalisées, y compris celles préconfigurées avec des bases de données alimentées. Au lieu de tout définir dans la configuration du test, vous pouvez créer et utiliser une image Docker personnalisée qui contient déjà le schéma requis et les données de test.

Lors de la création de votre propre package personnalisé à utiliser, vous pouvez :

1. Télécharger votre image personnalisée sur DockerHub et y faire référence :
    

```csharp
 SqlContainer = new MsSqlBuilder()
            .WithImage("your-dockerhub-username/custom-sql-image") 
            .WithPassword("P@ssw0rd123")
            .WithPortBinding(1433)
            .WithWaitStrategy(Wait.ForUnixContainer().UntilPortIsAvailable(1433))
            .Build();
```

2. Construire votre image Docker localement - si vous utilisez une image locale dans TestContainers, vous pouvez simplement référencer le nom de l'image (par exemple, `my-custom-sql-image`) dans votre code. TestContainers vérifiera d'abord votre Docker Desktop local pour l'image avant d'essayer de la télécharger depuis un registre comme Docker Hub.
    

```csharp
SqlContainer = new MsSqlBuilder()
    .WithImage("custom-sql-image") // Référencez votre image locale
    .WithPassword("P@ssw0rd123")
    .WithPortBinding(1433)
    .WithWaitStrategy(Wait.ForUnixContainer().UntilPortIsAvailable(1433))
    .Build();
```

Avoir une image pré-construite peut accélérer vos tests, surtout dans les pipelines CI/CD, sans parler du fait qu'elle les rend plus lisibles en supprimant le code d'alimentation.

Pour accéder à votre image personnalisée dans un pipeline CI/CD, vous pouvez la télécharger sur DockerHub ou GitHub Container Registry (GHCR) et y accéder depuis vos tests. Construisez votre DockerFile et poussez-le vers l'un ou l'autre système avant d'y accéder dans vos tests.

## Réflexions finales

L'utilisation de TestContainers dans .NET est un changement de jeu pour les tests d'intégration. C'est un moyen léger et automatisé de gérer les dépendances externes comme les bases de données, les systèmes de cache, et plus encore. En utilisant des conteneurs de test dans une classe de test, TestFixture, ou ICollectionFixture, vous pouvez créer des tests plus propres et plus fiables avec des environnements isolés.

TestContainers peut également vous faire économiser de l'argent en éliminant le besoin d'environnements de test dédiés avec des dépendances de longue durée. Vous pouvez les créer et les détruire à la volée, ou même les intégrer dans vos pipelines CI/CD, surtout dans GitHub où Docker peut être facilement utilisé.

Comme toujours, j'espère que vous avez trouvé cet article utile, et si vous avez des questions, n'hésitez pas à me contacter sur X / Twitter - [@grantdotdev](https://x.com/grantdotdev)