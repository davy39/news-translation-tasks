---
title: Comment utiliser FakeLogger pour faciliter les tests dans .Net
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2025-02-17T22:24:54.995Z'
originalURL: https://freecodecamp.org/news/how-to-use-fakelogger-to-make-testing-easier-in-net
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1739486043718/2d1e6339-fb93-4719-a89a-5b29e30c2bfc.png
tags:
- name: C#
  slug: csharp
- name: Testing
  slug: testing
- name: Tutorial
  slug: tutorial
seo_title: Comment utiliser FakeLogger pour faciliter les tests dans .Net
seo_desc: When writing unit tests in .NET, you may need to verify that methods are
  logging exceptions, errors, or other key information. You might think, No problem,
  I'll just mock ILogger using my favourite mocking library – for example Moq, NSubstitute,
  or F...
---

Lorsque vous écrivez des tests unitaires dans .NET, vous pouvez avoir besoin de vérifier que les méthodes enregistrent les exceptions, les erreurs ou d'autres informations clés. Vous pourriez penser, *Pas de problème, je vais simplement simuler* `ILogger` *en utilisant ma bibliothèque de simulation préférée* – par exemple Moq, NSubstitute ou FakeItEasy.

Bien que `ILogger` lui-même soit une interface et puisse être simulé, beaucoup de ses méthodes de journalisation couramment utilisées (comme `LogInformation()`, `LogError()`, etc.) sont ce qu'on appelle des méthodes statiques ou d'extension. Comme les méthodes statiques et d'extension ne peuvent pas être simulées directement, vous avez souvent besoin d'une couche d'abstraction personnalisée (LoggingService) ou d'un décorateur à passer à diverses autres méthodes ou services.

Il existe cependant une autre méthode beaucoup plus simple. Dans cet article, je vais vous montrer comment utiliser la fonctionnalité relativement nouvelle disponible à partir de .Net 8 appelée `FakeLogger`.

## Table des matières

1. [Installation du didacticiel](#heading-installation)

2. [Comment tester la fonctionnalité de journalisation](#heading-comment-tester-la-fonctionnalite-de-journalisation)

3. [Comment utiliser FakeLogger](#heading-comment-utiliser-fakelogger)

   * [Installation de FakeLogger et FluentAssertions](#heading-installation-de-fakelogger-et-fluentassertions)

   * [Utilisation de la classe FakeLogger](#heading-utilisation-de-la-classe-fakelogger)

   * [Qu'est-ce que Collector ?](#heading-questce-que-collector)

   * [Propriétés utiles de Collector](#heading-proprietes-utiles-de-collector)

4. [Comment vérifier que les arguments de journalisation structurée sont passés correctement](#heading-comment-verifier-que-les-arguments-de-journalisation-structuree-sont-passes-correctement)

5. [Comment vérifier qu'un message a été appelé à tout moment](#heading-comment-verifier-quun-message-a-ete-appele-a-tout-moment)

6. [Réflexions finales](#heading-reflexions-finales)

## Installation

Imaginons que vous avez créé un service de commande et de facturation en ligne. Les tests de code logique ont été effectués, mais vous devez maintenant tester la fonctionnalité de journalisation.

Pour ce didacticiel, nous utiliserons les classes `OrderService` et `InvoiceService` définies ci-dessous. J'ai fourni des commentaires pour illustrer où votre logique irait normalement, mais comme cela n'est pas pertinent pour ce didacticiel, les commentaires suffiront.

```csharp
namespace FakeLogger_Tutorial;

public class OrderService(ILogger logger, IInvoiceService invoiceService)
{
    public void ProcessOrder(Order order)
    {
        logger.LogInformation("Traitement de la commande...");

        // Le code de traitement de la commande va ici

        logger.LogInformation("Commande traitée avec succès.");

        invoiceService.SendInvoice(order);
    }
}

public class InvoiceService(ILogger logger) : IInvoiceService
{
    public void SendInvoice(Order order)
    {
        // Envoyer la commande au service de livraison
        logger.LogInformation("Commande expédiée : {OrderId}", order.ID);

        // Générer le code de facture

        SendEmail();
    }

    private void SendEmail()
    {
        // Envoyer un email au client
        logger.LogInformation("Envoi de la facture au client");

        // Effectuer la logique d'envoi d'email...

        logger.LogInformation("Email envoyé avec succès.");
    }
}

public interface IInvoiceService
{
    void SendInvoice(Order order);
}
```

Ainsi qu'une classe `Order` et `Product` très basique :

```csharp
public class Order
{
    public Guid ID { get; set; }
    public required Guid CustomerId { get; set; }

    public List<Product> Products = [];

    public decimal TotalPrice => Products.Sum(x => x.Price);

    public DateTime OrderDate { get; set; }
}

public class Product
{
    public Guid ID { get; set; }
    public string Name { get; set; }
    public decimal Price { get; set; }
}
```

## Comment tester la fonctionnalité de journalisation

Comme pour la plupart des aspects de la programmation, il existe plusieurs façons d'y parvenir. L'approche recommandée consiste à simuler le logger et à faire des assertions contre l'objet logger simulé plutôt que contre une instance concrète. Cela permet des tests contrôlés, isolés et vérifiables sans dépendre de dépendances externes ou du comportement réel de journalisation – ce qui signifie des tests plus propres et plus maintenables.

Vous pouvez le faire en utilisant votre bibliothèque de simulation préférée, telle que **Moq**, **FakeItEasy** ou **NSubstitute**. Vous pouvez en apprendre davantage sur ces bibliothèques et sur la façon de simuler avec succès dans un autre tutoriel que j'ai écrit, que vous pouvez trouver [ici](https://www.freecodecamp.org/news/explore-mocking-in-net/).

Vos premières pensées pourraient être d'écrire des tests comme l'exemple ci-dessous en utilisant `Moq` et `XUnit`, mais cela ne fonctionnera pas, et je vais expliquer pourquoi.

```csharp
using FakeLogger_Tutorial;
using Microsoft.Extensions.Logging;
using Moq;

namespace UnitTests;

public class FailingTestCases
{
    [Fact]
    public void LogError_Should_Call_LogError()
    {
        // Arrange
        var mockLogger = new Mock<ILogger>();

        // passer le mockedLogger à notre service
        var orderService = new OrderService(
            mockLogger.Object, 
            new Mock<IInvoiceService>().Object
        );

        var customerId = Guid.NewGuid();
        var order = new Order
        {
            ID = Guid.NewGuid(),
            CustomerId = customerId,
            Products = [new Product { ID = Guid.NewGuid(), Name = "Ballons de ping-pong", Price = 1.00M }],
            OrderDate = default,
        };

        // Act
        orderService.ProcessOrder(order);      

        // Assert
        mockLogger.Verify(x => x.LogInformation("Traitement de la commande..."), Times.Once);
        mockLogger.Verify(x => x.LogInformation("Commande traitée avec succès."), Times.Once);
    }
}
```

Lorsque vous exécutez ce code, il **échouera** avec l'erreur suivante :

```markdown
System.NotSupportedException: 
Expression non prise en charge : x => x.LogInformation("Traitement de la commande...", new[] {  })
```

### Pourquoi cela se produit-il ?

Les bibliothèques de simulation ont du mal avec les méthodes statiques comme `LogInformation` car elles appartiennent au type lui-même, et non à une instance. Certains outils, comme JustMock, peuvent gérer cela en utilisant des techniques avancées comme la réécriture IL ou des shims, mais ceux-ci ajoutent de la complexité.

Une solution courante consiste à envelopper `ILogger` dans un service de journalisation pour faciliter les tests, avec des avantages comme l'abstraction et la maintenabilité. Mais pour une approche plus simple, nous allons nous concentrer sur la nouvelle classe `FakeLogger`.

Vous pourriez tester ILogger en utilisant la méthode `Verify` dans Moq, en utilisant des méthodes trop compliquées et verbeuses comme ci-dessous. Le code de test fonctionnera, mais il est un peu trop complexe et difficile à lire, surtout à première vue.

```csharp
using FakeLogger_Tutorial;
using Microsoft.Extensions.Logging;
using Moq;

namespace UnitTests;

public class FailingTestCases
{
    [Fact]
    public void LogError_Should_Call_Logger_LogError()
    {
        // Arrange
        var mockLogger = new Mock<ILogger>();
        var mockInvoiceService = new Mock<IInvoiceService>();

        var orderService = new OrderService(
            mockLogger.Object, 
            mockInvoice.Object           
        );

        var customerId = Guid.NewGuid();
        var order = new Order
        {
            ID = Guid.NewGuid(),
            CustomerId = customerId,
            Products = [new Product { ID = Guid.NewGuid(), Name = "Ballons de ping-pong", Price = 1.00M }],
            OrderDate = default,
        };

        // Act
        orderService.ProcessOrder(order);

        // Assert
        mockLogger.Verify(logger => logger.Log(
                It.Is<LogLevel>(logLevel => logLevel == LogLevel.Information),
                It.Is<EventId>(eventId => eventId.Id == 0),
                It.Is<It.IsAnyType>((@object, @type) =>
                    @object.ToString() == "Traitement de la commande..."),
                It.IsAny<Exception>(),
                It.IsAny<Func<It.IsAnyType, Exception, string>>()),
            Times.Once);
    }
}
```

## Comment utiliser FakeLogger

Avec .NET 8, nous pouvons utiliser la classe `FakeLogger` pour rendre les tests plus clairs pour les autres développeurs. Si vous n'avez pas encore mis à jour, je vous le recommande vivement—.NET 8 offre un support à long terme (LTS) et débloque de nombreuses autres fonctionnalités utiles.

Microsoft définit la classe comme suit :

> Ce type est destiné à être utilisé dans les tests unitaires. Il capture tout l'état du journal en mémoire et vous permet de l'inspecter pour valider que votre code journalise ce qu'il devrait.

En termes simples, cela signifie que FakeLogger agit comme une collection en mémoire de tous les journaux et de leurs données associées, ce qui signifie que nous pouvons accéder à ceux-ci pendant nos tests unitaires. Il expose toutes les méthodes d'extension que nous trouverions sur l'implémentation `ILogger`, ce qui en fait le moyen idéal pour tester notre fonctionnalité de journalisation.

### Installation de FakeLogger et FluentAssertions

FluentAssertions est une excellente bibliothèque de test qui rend votre code plus facile à tester et à lire. Elle se concentre sur l'utilisation de fonctions d'assertion clairement nommées, comme `Should(), Have()` / `Be()`.

Vous pouvez l'installer en utilisant le gestionnaire de packages Nuget dans votre IDE préféré, ou via le terminal avec la commande suivante :

```csharp
dotnet add package FluentAssertions
```

**IMPORTANT : Ne dépassez pas la version 7.x.x de FluentAssertions, car la v8 est payante, tandis que tout ce qui précède est gratuit.**

Une fois installé, vous devrez installer `Microsoft.Extensions.Diagnostics.Testing` comme avant, en utilisant soit le gestionnaire de console de packages, le terminal, ou votre méthode préférée.

```csharp
dotnet add package Microsoft.Extensions.Diagnostics.Testing
```

### Utilisation de la classe FakeLogger

C'est aussi simple que d'utiliser n'importe quelle autre classe en C#. Nous pouvons l'instancier comme suit :

```csharp
using Microsoft.Extensions.Diagnostics.Testing;

var fakeLogger = new FakeLogger();
```

Maintenant, au lieu de passer `mockLogger.Object` à notre OrderService comme avant, nous allons plutôt passer notre nouvel objet `fakeLogger` comme suit :

```csharp
var loggingService = new OrderService(fakeLogger);
```

Voici un exemple de la façon dont nous pouvons utiliser `FakeLogger` pour vérifier si un message *Information* a été journalisé.

```csharp
    public void OrderService_ProcessOrder_ShouldLogProgress()
    {
        // Arrange
        var fakeLogger = new FakeLogger();
        var mockInvoiceService = new Mock<IInvoiceService>();

        var orderService = new OrderService(
            fakeLogger,
            mockInvoiceService.Object
        );

        var customerId = Guid.NewGuid();
        var order = new Order
        {
            ID = Guid.NewGuid(),
            CustomerId = customerId,
            Products = [new Product { ID = Guid.NewGuid(), Name = "Ballons de ping-pong", Price = 1.00M }],
            OrderDate = default,
        };

        // Act
        orderService.ProcessOrder(order);

        // Assert
        fakeLogger.Collector.Count.Should().Be(2);
        fakeLogger.Collector.LatestRecord.Level.Should().Be(LogLevel.Information);
        fakeLogger.Collector.LatestRecord.Message.Should().Be("Commande traitée avec succès.");
    }
```

Comme vous pouvez le voir, c'est beaucoup plus facile à lire que l'implémentation précédente de `Moq`. La solution `FakeLogger` combinée avec `FluentAssertions` est beaucoup plus concise et lisible pour les développeurs de tous niveaux.

### Qu'est-ce que `Collector` ?

La propriété `Collector` dans `FakeLogger` est une instance de `FakeLogCollector`, qui collecte et stocke les informations de journalisation. Elle stocke les messages dans le même ordre où ils ont été appelés, ce qui facilite les assertions ultérieures.

#### **But de la propriété** `Collector`

* Elle **stocke tous les messages de journalisation** capturés par le `FakeLogger`.

* Vous pouvez accéder, filtrer et faire des assertions contre les journaux dans vos tests.

* Utile lorsque vous vérifiez les journaux structurés ou assurez les niveaux de journalisation corrects.

### Propriétés utiles de Collector

### `LatestRecord`

Il existe plus d'une façon d'accéder et d'assertion des messages journalisés. Dans l'exemple ci-dessus, nous utilisons la propriété `LatestRecord`. La propriété `LatestRecord` retourne le dernier `FakeLogRecord` enregistré. Cela provient de la propriété interne `Records`, retournant le dernier enregistrement dans la liste.

L'objet `FakeLogRecord` a les propriétés suivantes :

```csharp
Level
Id 
State
Exception
Message
Scopes
Category
LevelEnabled
Timestamp
```

Nous pouvons donc vérifier l'une de ces propriétés dans nos assertions.

### `GetSnapshot()`

GetSnapshot() retourne tous les enregistrements de journalisation collectés.

* Cette méthode est utile lorsque vous souhaitez inspecter **tous** les messages journalisés, pas seulement le plus récent.

* Elle retourne une **collection immutable**, garantissant que les journaux ne sont pas modifiés de manière inattendue.

Comme `GetSnapshot()` retourne une collection immutable de messages. Nous pouvons accéder à ceux-ci comme à n'importe quelle autre collection de données, tout en étant capable d'utiliser LINQ pour filtrer, trier et interroger les journaux. Cela peut être très utile lorsque nous souhaitons faire des assertions sur le premier, le dernier, ou tout autre message journalisé.

Le test suivant utilise une instance concrète de `InvoiceService` car nous souhaitons tester le flux réel des journaux, à travers les deux services.

```csharp
    [Fact]
    public void ProcessOrder_ShouldLogMultipleMessages()
    {
        // Arrange
        var fakeLog = new FakeLogger();
        var invoiceService = new InvoiceService(fakeLog);
        var orderService = new OrderService(fakeLog, invoiceService);
        var testOrder = new Order
        {
            ID = Guid.NewGuid(),
            CustomerId = Guid.NewGuid(),
            Products =
            [
                new Product { ID = Guid.NewGuid(), Name = "Produit 1", Price = 99.99m },
                new Product { ID = Guid.NewGuid(), Name = "Produit 2", Price = 199.99m }
            ],
        };

        // Act
        orderService.ProcessOrder(testOrder);

        // Assert
        fakeLog.Collector.GetSnapshot()[0].Message.Should().Be("Traitement de la commande...");
        fakeLog.Collector.GetSnapshot()[0].Level.Should().Be(LogLevel.Information);

        fakeLog.Collector.GetSnapshot()[1].Message.Should().Be("Commande traitée avec succès.");
        fakeLog.Collector.GetSnapshot()[1].Level.Should().Be(LogLevel.Information);

        fakeLog.Collector.GetSnapshot()[2].Message.Should().Be($"Commande expédiée : {testOrder.ID}");
        fakeLog.Collector.GetSnapshot()[2].Level.Should().Be(LogLevel.Information);

        fakeLog.Collector.GetSnapshot()[3].Message.Should().Be("Envoi de la facture au client");
        fakeLog.Collector.GetSnapshot()[3].Level.Should().Be(LogLevel.Information);

        fakeLog.Collector.GetSnapshot()[4].Message.Should().Be("Email envoyé avec succès.");
        fakeLog.Collector.GetSnapshot()[4].Level.Should().Be(LogLevel.Information);
    }
```

Ce test démontre à quel point il est simple de vérifier que le logger capture les messages dans l'ordre d'exécution avec le bon `LogLevel` et le bon message. Il met également en évidence la lisibilité du test.

## **Comment vérifier que les arguments de journalisation structurée sont passés correctement**

La journalisation structurée nous permet de passer des objets et des variables comme arguments aux messages de journalisation, fournissant des journaux plus riches et plus recherchables. Dans `ILogger`, nous pouvons passer un objet comme ceci :

```csharp
_logger.LogInformation("Commande traitée : {OrderId}", order.ID);
```

Par défaut, les fournisseurs de journalisation (comme le fournisseur `ILogger` intégré de .NET) remplacent immédiatement les espaces réservés dans le message de journalisation final.

Avec le `ILogger` intégré, le message de journalisation est entièrement formaté au moment de l'exécution, par exemple :

```csharp
_logger.LogInformation("Numéro de commande {OrderId} expédiée", 123);
```

**Journal final enregistré est :**

```csharp
"Numéro de commande 123 expédiée"
```

Cela signifie que lors de la récupération des journaux dans les tests en utilisant le fournisseur de journalisation par défaut, nous ne pouvons vérifier que la chaîne formatée finale lors de l'utilisation de `FakeLogger` car il capture le message de journalisation entièrement rendu.

**Important :** Cela diffère des fournisseurs de journalisation structurée tels que Serilog, où les modèles de messages et les propriétés structurées sont stockés séparément. Dans Serilog, la colonne `Message` stocke la chaîne de modèle brute originale, tandis que les propriétés / objets structurés sont stockés dans un champ JSON séparé.

Cela ne signifie pas que vous ne pouvez pas utiliser `FakeLogger` avec Serilog—vous pouvez absolument le faire. Mais lors de l'assertion des journaux, vous devez ajuster vos assertions en fonction de si vous vérifiez le message entièrement formaté ou les propriétés structurées.

Si nous journalisons une expédition de commande :

```csharp
logger.LogInformation("Commande expédiée : {OrderId}", order.ID);
```

Contrairement à Serilog, `FakeLogger` ne stocke pas `{OrderId}` comme une propriété séparée. Au lieu de cela, il capture le message entièrement formaté :

```csharp
"Commande expédiée : 550e8400-e29b-41d4-a716-446655440000"
```

Ainsi, lors des tests avec `FakeLogger`, nous **devons** faire des assertions contre la chaîne formatée finale.

Même si `FakeLogger` ne stocke pas le modèle de message original, il capture les données structurées séparément. Cela vous permet d'assertion à la fois :

1. Le message formaté final (puisque les espaces réservés sont remplacés au moment de l'exécution).

2. Les données structurées (objets ou propriétés passés comme arguments).

Le test ci-dessous fait des assertions sur le message formaté final, ainsi que sur un objet `StructuredState` (les informations de journalisation structurée enregistrées).

```csharp
[Fact]
    public void InvoiceOrder_ShouldLog_StructuredLogInfo()
    {
        // Arrange
        var fakeLogger = new FakeLogger<InvoiceService>();
        var service = new InvoiceService(fakeLogger);
        var testOrder = new Order
        {
            ID = Guid.NewGuid(),
            CustomerId = Guid.NewGuid(),
            Products =
            [
                new Product { ID = Guid.NewGuid(), Name = "Produit 1", Price = 99.99m },
                new Product { ID = Guid.NewGuid(), Name = "Produit 2", Price = 199.99m }
            ],
        };

        // Act
        service.SendInvoice(testOrder);

        // Assert
        fakeLogger.Collector.GetSnapshot()[0].Message.Should().Be($"Commande expédiée : {testOrder.ID}");
        var keyValuePairs = fakeLogger.Collector.GetSnapshot()[0].StructuredState;

        var orderIdProperty = keyValuePairs != null && keyValuePairs
            .Any(x => x.Key == "OrderId" && x.Value == testOrder.ID.ToString());

        orderIdProperty.Should().BeTrue();
    }
```

## Comment vérifier qu'un message a été appelé à tout moment

Et si vous souhaitez tester qu'un message ou un ensemble de messages sont appelés **n'importe où** dans la pile d'appels ? Vous pouvez facilement le faire avec l'aide de LINQ (si vous n'êtes pas familier avec LINQ, vous pouvez lire à ce sujet dans mon autre article [ici](https://www.freecodecamp.org/news/how-to-use-linq/)).

Nous ne souhaitons pas faire d'assertion que les messages sont envoyés dans le bon ordre, juste que les messages sont journalisés. Nous pouvons le faire comme suit :

```csharp
    [Fact]
    public void AllMessages_Should_BeSentInAnyOrder()
    {
        // Arrange
        var testOrder = new Order
        {
            ID = Guid.NewGuid(),
            CustomerId = Guid.NewGuid(),
            Products =
            [
                new Product { ID = Guid.NewGuid(), Name = "Produit 1", Price = 99.99m },
                new Product { ID = Guid.NewGuid(), Name = "Produit 2", Price = 199.99m }
            ],
        };

        var fakeLogger = new FakeLogger();
        var invoiceService = new InvoiceService(fakeLogger);
        var orderService = new OrderService(fakeLogger, invoiceService);
        var expectedMessages = new List<string>
        {
            $"Commande expédiée : {testOrder.ID}",         
            "Traitement de la commande...",
            "Facture envoyée"
        };

        // Act
        orderService.ProcessOrder(testOrder);

        // Assert
        fakeLogger.Collector.GetSnapshot()
            .Select(x => x.Message)
            .Should().IntersectWith(expectedMessages);
    }
```

Ici, nous pouvons utiliser la puissance de LINQ et FluentAssertions pour `Select` chaque message stocké dans la propriété `Collector`, puis faire une assertion que le tableau de messages peut `IntersectWith` les messages attendus.

La méthode `IntersectWith` fait une assertion que la collection partage un ou plusieurs éléments avec la collection fournie, ce qui est parfait pour ce type de scénario où nous ne nous soucions pas de l'ordre des messages journalisés – seulement qu'à un moment donné ils sont journalisés.

## Réflexions finales

Tester la journalisation dans les applications .NET a traditionnellement été délicat en raison des méthodes d'extension dans `ILogger`. Mais avec le `FakeLogger` de .NET 8, nous avons maintenant un moyen plus propre, plus lisible et plus efficace de vérifier les messages de journalisation dans les tests unitaires.

En utilisant `FakeLogger` avec `FluentAssertions`, nous pouvons simplifier les assertions, améliorer la lisibilité des tests et garantir que notre comportement de journalisation est correctement implémenté sans la complexité des bibliothèques de simulation traditionnelles.

Que vous vérifiiez le contenu des messages, les journaux structurés ou l'ordre d'exécution, `FakeLogger` fournit une solution robuste qui s'intègre parfaitement dans les pratiques de test .NET modernes. Si vous ne l'avez pas encore fait, je vous recommande vivement de passer à .NET 8 pour tirer pleinement parti de cette fonctionnalité puissante.

J'espère que vous avez trouvé cela utile ! Si vous souhaitez discuter davantage, n'hésitez pas à me contacter sur [Twitter](https://x.com/grantdotdev).