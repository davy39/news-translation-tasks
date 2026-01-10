---
title: Qu'est-ce que le Mocking ? Le Mocking en .NET Expliqué avec des Exemples
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2024-04-12T19:37:51.000Z'
originalURL: https://freecodecamp.org/news/explore-mocking-in-net
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/Mocking-in-Dotnet.png
tags:
- name: .NET
  slug: net
- name: Testing
  slug: testing
- name: unit testing
  slug: unit-testing
seo_title: Qu'est-ce que le Mocking ? Le Mocking en .NET Expliqué avec des Exemples
seo_desc: 'Let''s go on a journey to demystify the concept of mocking in .NET software
  development. Let''s delve into how straightforward and accessible mocking truly
  is. Join me as we navigate through this subject, as I cover:


  Understanding mocking: Why it''s ne...'
---

Embarquons pour un voyage afin de démystifier le concept de mocking dans le développement logiciel .NET. Plongeons dans la simplicité et l'accessibilité du mocking. Rejoignez-moi alors que nous naviguons à travers ce sujet, car je couvre :

* Comprendre le mocking : Pourquoi il est nécessaire pour construire une stratégie de test robuste.
* Explorer certaines des bibliothèques de mocking les plus courantes : telles que Moq, NSubstitute, FakeItEasy et Rhino Mocks.
* Maîtriser les techniques de mocking : Utiliser chacune de ces bibliothèques, vous équipant des connaissances pour choisir le meilleur outil de mocking pour vos besoins.

Le but de ce tutoriel est de vous donner les connaissances pour vous faire votre propre opinion sur la bibliothèque de mocking que vous préférez, afin que vous puissiez avancer et écrire des tests puissants dans votre application.

## Prérequis pour ce tutoriel

1. Compréhension de la programmation C#
2. Compréhension des tests unitaires C#
3. Un IDE (Rider, Visual Studio, etc.), ou un éditeur de code (VS Code, Sublime Text, Atom, etc.)

## Getting Started/Setup

Pour accélérer le processus, j'ai rendu un dépôt GitHub public disponible pour ce tutoriel. Vous pouvez le cloner et l'utiliser sur votre machine locale pour suivre.

Rendez-vous simplement sur [ce lien](https://github.com/grant-dot-dev/mocking-tutorial) et clonez le dépôt sur votre machine locale.

Rappel rapide si vous avez oublié de le faire : allez sur le lien ci-dessus, et dans le coin supérieur droit, cliquez sur "Code", puis copiez l'URL fournie.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/image-2.png)

![Image](https://www.freecodecamp.org/news/content/images/2024/04/image-3.png)

Trouvez votre dossier local **git** (si vous n'en avez pas, créez-en un dans votre dossier racine utilisateur). Ensuite, dans votre terminal préféré, naviguez vers votre dossier **git**, et exécutez la commande suivante.

```terminal
// (remplacez <url> par l'url)
git clone <url>
```

## Aperçu de l'application

La solution que vous venez de cloner est un projet d'API Web de base qui référence une bibliothèque de classes avec certains objets de domaine Todo et services qui modifieront une liste d'éléments Todo.

Pour les besoins de ce tutoriel, ces éléments sont stockés dans une liste en mémoire, plutôt que de se connecter à une base de données. Mais vous pouvez utiliser une base de données ou d'autres formes de méthodes de persistance des données.

Cependant, pour les besoins de ce tutoriel, nous nous soucions moins de la persistance des données, et plus de la simulation de ce service.

## Qu'est-ce que le Mocking ?

![Deux flèches avec le texte Real et Fake](https://www.freecodecamp.org/news/content/images/2024/03/image-112.png)
_Avec le mocking, vous ne verrez pas la différence_

Le mocking dans le développement logiciel est le concept de simuler un comportement ou un objet retourné d'une classe, méthode ou service dont une autre partie du système sous test dépend.

Lors du test d'un composant ou d'une unité de code particulière, il est souvent nécessaire de l'isoler de ses dépendances, telles que les bases de données, les services web ou d'autres classes, afin de s'assurer que le test se concentre uniquement sur la fonctionnalité de l'unité testée plutôt que de se préoccuper des aspects externes du code.

Le mocking permet aux développeurs de créer des objets simulés ou des implémentations factices de ces dépendances qui se comportent de manière prédéterminée, imitant le comportement des objets réels.

En utilisant des objets ou méthodes simulés, nous pouvons contrôler l'entrée et la sortie des dépendances. Cela facilite grandement le test de différents scénarios, où la logique métier dépend du résultat d'une dépendance.

### Exemple

Supposons que nous avons un endpoint d'API qui appelle un dépôt qui se connecte à une base de données. Notre type de réponse d'API dépend de la valeur retournée par le dépôt : nous retournons soit une réponse 400, soit une réponse 200 de notre API.

Nous pouvons simplement simuler la valeur de retour du dépôt et tester que notre API retourne la réponse correcte dans les deux scénarios sans avoir à toucher notre base de données.

En essence, le mocking aide les développeurs à écrire des tests plus fiables et efficaces en isolant le code sous test et en fournissant un comportement prévisible pour ses dépendances, améliorant ainsi la qualité globale du logiciel.

## Quels sont les avantages du Mocking ?

![Image montrant des pièces de puzzle, avec une pièce mise en avant disant Avantages](https://www.freecodecamp.org/news/content/images/2024/03/image-113.png)
_Avantages_

### Isolation du code

Comme je l'ai déjà expliqué, le mocking des dépendances permet l'isolation du code pour les tests. En simulant les dépendances, vous pouvez identifier les points de défaillance dans le code sous test, et non les dépendances elles-mêmes (sauf si vous les simulez incorrectement – ce que ce tutoriel vous aidera à éviter, je l'espère).

### Tests plus rapides

En remplaçant les dépendances réelles par des implémentations simulées, les tests peuvent être effectués plus rapidement. Vous ne luttez pas contre les incohérences, les résultats peu fiables ou imprévisibles de ces dépendances. Cela élimine le besoin de configurer et de supprimer des sources externes, ce qui peut parfois être complexe et chronophage.

### Tests déterministes

Les objets simulés offrent un environnement contrôlé, permettant aux développeurs de spécifier le comportement exact et les réponses des dépendances. Cette approche signifie que les tests sont cohérents, facilitant la recherche de bugs et le débogage des problèmes, en particulier pour ceux qui adoptent une approche TDD (Test Driven Development).

### Tests parallèles

Le mocking permet les tests parallèles (plusieurs tests exécutés en même temps) en supprimant les dépendances aux ressources externes qui peuvent être limitées ou inaccessibles pendant les tests.

Par exemple, si vous ne simuliez pas votre couche de connexion à la base de données, essayer d'exécuter des tests en parallèle pourrait causer des métriques de réussite/échec incohérentes, car un autre test pourrait affecter la table de base de données que vous utilisez dans un autre test. Simuler cette couche signifie que vos tests sont maintenant agnostiques à cette couche et peuvent être exécutés en même temps.

### Maintenance réduite des tests

Puisque les objets simulés encapsulent le comportement des dépendances, les changements apportés à ces dépendances ne nécessitent pas nécessairement des mises à jour des tests eux-mêmes. Cela réduit les frais généraux de maintenance associés aux bases de code et aux dépendances évolutives.

### Couverture de test améliorée

Le mocking permet aux développeurs de simuler une large gamme de scénarios et de cas limites. En contrôlant le comportement des dépendances, les développeurs peuvent s'assurer que leurs tests exercent tous les chemins pertinents à travers le code, supprimant toute limitation réelle ou physique.

## Choses à savoir sur le Mocking

![Image](https://www.freecodecamp.org/news/content/images/2024/04/image-20.png)

**Complexité :** Parfois, lors du mocking/test de zones complexes de l'application, le mocking peut également devenir complexe. Cependant, si le système est trop difficile à simuler, vous devrez peut-être réévaluer votre architecture.

**Courbe d'apprentissage :** Cela nécessite une compréhension de la syntaxe et des concepts de la bibliothèque de mocking, ce qui peut être difficile pour les développeurs qui sont nouveaux dans les tests unitaires ou le framework spécifique.

**Sur-spécification :** Le mocking peut conduire à une sur-spécification du comportement du code sous test. Cela signifie que les tests peuvent devenir étroitement couplés aux détails d'implémentation, les rendant fragiles et sujets à la rupture lorsque l'implémentation change. Il est essentiel de trouver un équilibre entre la vérification du comportement et la concentration sur les résultats souhaités.

**Soyez conscient des tests faux-positifs :** Bien que le mocking vous permette d'isoler des unités de code, il peut également créer un faux sentiment de sécurité. Les mocks simulent les dépendances, mais ils peuvent ne pas reproduire pleinement le comportement des dépendances réelles. Les tests d'[intégration](https://www.browserstack.com/guide/integration-testing) ou les tests [end-to-end](https://www.browserstack.com/guide/end-to-end-testing) sont encore nécessaires pour vérifier le comportement du système dans son ensemble.

## Bibliothèques de Mocking .NET Populaires

![Image](https://www.freecodecamp.org/news/content/images/2024/04/image-25.png)

Voici quelques bibliothèques de test .NET populaires :

* FakeItEasy
* NSubstitute
* Moq
* Rhino Mocks

Ce ne sont que quelques-unes des bibliothèques de mocking .NET les plus couramment utilisées disponibles en ligne, mais il en existe beaucoup d'autres. Je vous recommande vivement d'utiliser l'une de celles-ci car elles ont une communauté plus large, une base de code plus réputée et une bonne documentation (essentielle lorsque vous commencez).

Chacune de ces bibliothèques de mocking a sa propre syntaxe pour créer des mocks d'objets, mais elles suivent toutes les mêmes principes.

1. Déclarer l'objet/type/service que vous souhaitez simuler
2. Comment vous voulez que cet objet/type/service s'exécute (l'implémentation)
3. Quelle est la valeur retournée (lorsque nécessaire).

## Examen des Tests

Si vous ouvrez la solution et naviguez vers le projet "Test", vous pouvez voir que nous avons quatre fichiers avec chacun des différents tests de bibliothèque de mocking.

1. FakeItEasyApiTests.cs
2. MoqApiTests.cs
3. NSubstituteApiTests.cs
4. RhinoMocksApiTests.cs

Dans ces fichiers, vous verrez que nous avons quatre tests XUnit très basiques. Je les ai gardés brefs et simples pour les besoins de ce tutoriel.

## Plongée profonde dans la structure des tests

Chaque fichier de test utilise un constructeur pour initialiser une version privée de leurs services respectifs, et vous pouvez voir comment ceux-ci diffèrent d'une bibliothèque à l'autre, tout en suivant les mêmes concepts.

```csharp
// FakeItEasy
_fakeTodoService = A.Fake<ITodoService>();

// NSubstitute
_substituteTodoService = Substitute.For<ITodoService>();

// Moq
_mockTodoService = new Mock<ITodoService>();

// Rhino Mocks
_mockTodoService = MockRepository.GenerateMock<ITodoService>();
```

Choisir la "bonne" bibliothèque de mocking dépend entièrement des préférences personnelles et de ce que vous trouvez plus facile à écrire, à travailler et à lire/comprendre.

Certains peuvent trouver l'utilisation de mots comme `Fake`, ou `Substitute.For` plus facile à comprendre ou à lire. Alors que d'autres peuvent trouver `A.Fake` peu intuitif et préférer `new Mock<type>` plus évident.

## Arrange, Act et Assert

En suivant le principe de test AAA (Arrange, Act et Assert), nous pouvons structurer soigneusement nos tests, rendant évident ce que nous faisons et où.

L'approche AAA pour les tests implique trois étapes :

1. **Arrange** : Configurer l'environnement de test, les services simulés/dépendances externes.
2. **Act** : Effectuer l'action testée.
3. **Assert** : Vérifier le résultat attendu.

## Utilisation des Mocks pour simuler les éléments retournés

Testons le point de terminaison `getAll` (GetAllTodoItems) en simulant la méthode `TodoService.GetAllTodos` pour retourner une liste fictive de tâches.

Cette approche élimine le besoin de configurer et de peupler une base de données pour chaque scénario de test, garantissant un test ciblé de l'endpoint de l'API retournant des valeurs selon des critères spécifiques.

Les mocks fournissent une solution idéale, nous permettant de simuler le comportement souhaité sans interférence d'autres tests.

Nous pouvons faire cela comme suit (souvenez-vous que le code complet est disponible dans le dépôt) :

```csharp
// FakeItEasy
A.CallTo(() => _fakeTodoService.GetAllTodos()).Returns(expectedTodos);

// NSubstitute
_substituteTodoService.GetAllTodos().Returns(expectedTodos);

// Moq
_moqTodoService.Setup(s => s.GetAllTodos()).Returns(expectedTodos);

// Rhino Mocks
_mockTodoService.Stub(s => s.GetAllTodos()).Return(expectedTodos);
```

### Que font ces méthodes ?

Une caractéristique commune que vous verrez dans la majorité des bibliothèques est l'utilisation de fonctions lambda pour dicter quelle méthode est simulée.

La fonction lambda fournie dans la méthode de configuration est essentiellement une étape de configuration qui définit quelle action doit être entreprise lorsque la méthode simulée est appelée. Cette configuration est stockée et appliquée lorsque la méthode simulée est invoquée pendant le test.

Décomposons ce que nous faisons :

1. Le lambda spécifie quelle méthode sur le service simulé nous souhaitons configurer/préparer.

2. Le lambda que nous passons n'est pas exécuté immédiatement par la méthode de configuration. Nous ne disons pas au test d'exécuter la méthode immédiatement ; nous disons : "Souvenez-vous de cette instruction/configuration pour lorsque la méthode réelle est appelée pendant le test."

3. Lorsque la méthode que nous simulons est appelée pendant le test, elle vérifie si la signature de l'appel correspond à une configuration de configuration que nous avons fournie. Si elle correspond, le test suit les instructions données pendant la configuration.

### Notes importantes :

NSubstitute, en revanche, permet au développeur de simuler la méthode directement sur l'objet factice. Cela signifie que vous pouvez accéder à la méthode factice `GetAllTodos` et simplement définir la valeur de retour à votre valeur attendue.

Bien que Moq utilise une méthode Setup, elle diffère légèrement des autres méthodes. Moq crée interne un objet proxy qui représente l'objet simulé et expose une propriété `.Object` pour y accéder. Nous verrons comment cela fonctionne dans la prochaine partie.

## Comment appeler le système sous test (SUT)

```csharp
// FakeItEasy
var sut = new TodoController(_fakeTodoService);

// NSubstitute
var sut = new TodoController(_substituteTodoService);

// Moq -- légèrement différent des autres
var sut = new TodoController(_moqTodoService.Object);

// Rhino Mocks
var sut = new TodoController(_mockTodoService);
```

Dans trois des quatre bibliothèques, vous pouvez passer l'objet simulé directement. Cependant, Moq nécessite d'accéder à la propriété `.Object` sur le mock pour l'utiliser. Ainsi, nous avons passé `moqTodoService.Object` comme argument au contrôleur.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/image-26.png)
_une image montrant que tous les tests ont réussi_

En exécutant les tests, vous pouvez voir qu'ils réussissent tous. Si vous changez le code dans le dépôt, cela ne ferait aucune différence car le dépôt est simulé dans ces tests. Essayez, modifiez la fonctionnalité du dépôt et réexécutez les tests, ils continueront à réussir.

Nous nous concentrons sur la fonctionnalité de l'endpoint, et non sur ce que fait le dépôt simulé, et c'est la beauté du mocking.

## Les options avec le Mocking sont infinies

![Image](https://www.freecodecamp.org/news/content/images/2024/04/image-5.png)

Le mocking ne nous permet pas seulement de définir ce qui est retourné par un objet simulé, il peut également nous permettre de simuler l'implémentation, y compris la capacité à lancer des erreurs spécifiques afin que nous puissions tester la gestion des erreurs de notre API et les chemins d'erreur.

Cela est illustré dans le test `Delete_Returns500_AndErrorMessageThrown_WhenExceptionThrown` dans chaque fichier de test de bibliothèque.

```csharp
// FakeItEasy
A.CallTo(() => _fakeTodoService.Delete(1)).Throws(new Exception(errorMessage));

// NSubstitute
_substituteTodoService.When(x => x.Delete(1)).Do(x => throw new Exception(errorMessage));

// Moq
_moqTodoService.Setup(s => s.Delete(1)).Throws(new Exception(errorMessage));

// Rhino Mocks
_mockTodoService.Stub(s => s.Delete(1)).Throw(new Exception(errorMessage));
```

En utilisant les différentes bibliothèques, nous pouvons faire en sorte que la méthode `Delete` du service lance n'importe quelle exception que nous souhaitons. Cela est idéal lorsque vous voulez retourner différents codes de statut, ou gérer les erreurs de différentes manières en fonction du type d'exception lancée.

Par exemple, nous pourrions changer `Throws(new Exception(errorMessage)` en `Throws(new UnauthorizedAccessException())` et tester que si un code de statut 401 est retourné lorsqu'il est lancé.

## Configuration globale

Vous pouvez attribuer plusieurs configurations à la même méthode. Cela est idéal dans les situations où vous souhaitez configurer toutes vos configurations de l'objet simulé en un seul endroit. Par exemple, dans le constructeur de la classe de test.

Dans certains frameworks de test (comme NUnit), vous pouvez utiliser un attribut `[OneTimeSetUp]` au-dessus de votre méthode, qui est exécuté avant vos cas de test, ou simplement utiliser le constructeur de votre classe de test.

Dans ce scénario, vous pourriez faire quelque chose (dans Moq) comme :

```csharp
public MoqApiTests()
{
    _mockTodoService = new Mock<ITodoService>();
    _mockTodoService.Setup(x => x.Delete(1)).Throws(new Exception("This is a generic exception"));
    _mockTodoService.Setup(x => x.Delete(2)).Throws(new UnauthorizedAccessException("You cannot perform this action on this item"));
}
```

Dans cet exemple, nous montrons la configuration d'appels de service simulés à la même méthode avec divers arguments, chacun provoquant le lancement de différentes exceptions.

Cette approche est bénéfique pour tester différents résultats lorsque différentes exceptions se produisent dans des tests séparés, sans encombrer notre code de test avec une configuration répétitive.

Par exemple :

```csharp
// Test 1
var result = TodoController.Delete(1);
// Assert gère l'exception générale

// Test 2
var result = TodoController.Delete(2);
// Assert gère UnauthorizedAccessException
```

Je préfère configurer les mocks dans chaque test individuel pour m'assurer qu'il n'y a pas de facteurs externes influençant le mock.

De cette façon, je peux facilement identifier ce qui est simulé dans le test sans chercher l'objet simulé et la configuration ailleurs.

## Et si je ne me soucie pas de ce que je passe ?

Dans nos exemples de suppression, nous avons systématiquement passé un ID à l'implémentation simulée. Par conséquent, si nous devions appeler la méthode avec un ID différent comme `101` via l'appel `TodoController.DeleteTodoItem`, nous n'obtiendrions pas le même résultat.

Cela est dû au fait que nous avons explicitement instruit l'objet simulé à lancer une erreur lorsque la méthode simulée est appelée avec un ID de 1.

Pour résoudre ce problème, nous pouvons être moins spécifiques. Chaque bibliothèque a sa propre syntaxe pour cela, nous permettant de spécifier que si un entier est passé à la méthode, elle lancera une exception particulière.

```csharp
// FakeItEasy
A.CallTo(() => _fakeTodoService.Delete(A<int>._)).Throws(new Exception(errorMessage));

// NSubstitute
_substituteTodoService.When(x => x.Delete(Arg.Any<int>())).Do(x => throw new Exception(errorMessage));

// Moq
_mockTodoService.Setup(s => s.Delete(It.IsAny<int>())).Throws(new Exception(errorMessage));

// Rhino Mocks
_mockTodoService.Stub(s => s.Delete(Arg<int>.Is.Anything)).Throw(new Exception(errorMessage));
```

Ce code indique que lorsqu'un argument de type `int` est passé, il doit lancer cette exception.

NSubstitute diffère légèrement en syntaxe : il nécessite une instruction explicite pour lancer l'erreur spécifiée lors de la rencontre de ce scénario, contrairement à lorsque nous lui indiquions de retourner un objet. Cette différence provient des mécanismes internes de la bibliothèque.

## Vérification que les Mocks sont appelés

Dans certains cas, vous pourriez vouloir vérifier qu'un service simulé est appelé avec les arguments corrects. Cela est particulièrement utile lorsque vous traitez avec un service "fire-and-forget".

Dans ce scénario, votre endpoint d'API est appelé, et bien qu'il retourne toujours vrai, il déclenche également un service pour effectuer une action indépendamment, qui n'affecte pas le type de retour de l'API (peut-être un service de notification asynchrone).

Cela est l'une des rares instances où vous pourriez vouloir effectuer une vérification rapide pour vous assurer que votre service "fire-and-forget" est invoqué (bien que idéalement, vous effectueriez un test d'intégration avec ce service).

Si vous regardez le point de terminaison `DeleteTodoItem`, et le test `DeleteAPI_CallsNotificationService_WithTaskId_AndUserId` dans chaque fichier de test, vous pouvez voir des exemples complets de la manière dont cela peut être fait.

Nous vérifions que lorsque nous appelons `DeleteTodoItem`, sur notre chemin heureux, `NotificationService.NotifyUserTaskCompleted` est appelé avec l'ID de l'élément à supprimer, et l'ID d'utilisateur codé en dur.

En tant qu'exercice, vous pourriez créer un service utilisateur qui retourne un ID d'utilisateur connecté, et cela peut être utilisé pour passer l'ID au service. Cela peut également être simulé dans le test.

```csharp
// FakeItEasy
A.CallTo(() => _fakeNotificationService.NotifyUserTaskCompleted(1,1)).MustHaveHappened(1, Times.Exactly);

// NSubstitute
_notificationService.Received().NotifyUserTaskCompleted(1,1);

// Moq
_moqNotificationService.Verify(x => x.NotifyUserTaskCompleted(1,1)); // Par défaut Times.AtLeastOnce

// Rhino Mock
_mockNotificationService.AssertWasCalled(x=>x.NotifyUserTaskCompleted(1,1));
```

## Conclusion

En conclusion, la polyvalence des objets simulés offre une myriade d'applications, s'avérant indispensable dans le test d'unités individuelles de code.

Bien que j'aie couvert plusieurs fonctionnalités et validations réalisables avec des mocks, il y en a d'autres, telles que l'ordre des appels de méthode et la validation négative.

À mon avis, le choix d'une bibliothèque de mocking pour un projet est subjectif, sans option définitivement correcte ou incorrecte. Bien que certaines bibliothèques puissent offrir des extensions plus pratiques ou une syntaxe plus claire, la décision revient finalement aux préférences personnelles.

Mon espoir est que ce tutoriel vous ait fourni un aperçu du monde du mocking et ait éclairé les variations de syntaxe entre les différentes bibliothèques.

Comme toujours, n'hésitez pas à me contacter (liens dans la bio).