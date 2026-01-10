---
title: Comment gérer les références nulles dans la dernière version de C#
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-12-11T18:16:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-null-references-in-csharp
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/article-null.jpg
tags:
- name: C
  slug: c
seo_title: Comment gérer les références nulles dans la dernière version de C#
seo_desc: "By Zoran Horvat\nC# 12 has just been released, and it continues the long\
  \ tradition of improvements in the safety of the language's software design and\
  \ execution. \nOne of these improvements relates to manipulating null references,\
  \ a programming concept..."
---

Par Zoran Horvat

C# 12 vient d'être publié, et il poursuit la longue tradition d'améliorations dans la sécurité de la conception et de l'exécution du logiciel du langage. 

L'une de ces améliorations concerne la manipulation des références nulles, un concept de programmation que de nombreux développeurs n'aiment pas vraiment. 

L'utilisation de références nulles dans votre code peut causer toutes sortes de problèmes, comme des exceptions et un manque d'informations.

Cet article vous apprendra à gérer les références nulles dans la dernière version du langage de programmation C# et .NET. Le nom du jeu : ne laissez aucune référence nulle sans surveillance.

Cette démonstration comportera plusieurs étapes, chacune avec sa propre petite démonstration. Si vous souhaitez passer certaines étapes, veuillez utiliser la table des matières ci-dessous.

## Table des matières

  1. [Prérequis](#heading-installation)
  1. [Comment utiliser les types de référence nullable](#heading-comment-utiliser-les-types-de-reference-nullable)
  1. [Comment utiliser les motifs `is null` et `is not null`](#heading-comment-utiliser-les-motifs-is-null-et-is-not-null)
  1. [Comment utiliser les motifs `Type-Test-and-Set`](#heading-comment-utiliser-les-motifs-type-test-and-set)
  1. [Comment utiliser les motifs `Property`](#heading-comment-utiliser-les-motifs-property)
  1. [Comment utiliser les opérateurs de propagation de null et de coalescence de null](#heading-comment-utiliser-les-operateurs-de-propagation-de-null-et-de-coalescence-de-null)
  1. [Comment travailler avec des objets optionnels](#heading-comment-travailler-avec-des-objets-optionnels)
  1. [Notes finales](#heading-notes-finales)

## Prérequis

Il y a quelques prérequis que vous devrez remplir avant de continuer. Je suppose que vous avez écrit suffisamment de code C# pour voir des références nulles dans leur habitat naturel. Et je m'attends à ce que vous compreniez qu'elles peuvent menacer la conception et la stabilité du code. 

Cet article clarifiera ces concepts et identifiera les problèmes et solutions en utilisant la syntaxe et les bibliothèques C#.

Si vous êtes prêt, nous pouvons commencer avec les types de référence nullable. Cela nous permettra de configurer l'environnement de travail et de nous mettre à niveau pour les démonstrations plus complexes qui suivront.

## Comment utiliser les types de référence nullable

Les types de référence nullable ont été introduits dans C# 8 et sont rapidement devenus un pilier.

L'histoire courte est que vous pouvez soit déclarer une référence nullable (par exemple, `string? s`) ou non-nullable (`string s`). 

Notez le rebondissement : ce qui était autrefois juste une référence avant C# 8 (`string s` était une référence ordinaire à une chaîne *nullable*) est maintenant devenu quelque chose de plus : une référence qui ne devrait jamais être définie à null. 

C'était le changement radical, peut-être le premier en une décennie d'évolution de la syntaxe C# !

Le compilateur fera de son mieux pour vérifier si toutes les affectations à une référence non-nullable (celle sans le point d'interrogation) la définissent à un objet approprié. S'il trouve un chemin d'exécution qui pourrait la définir à null, le compilateur émettra un avertissement à la compilation. Cela s'appelle "l'analyse d'affectation définitive", car le compilateur tente de prouver que chaque référence non-nullable est *définie* à un objet.

Si vous vous êtes déjà habitué aux types de référence nullable, j'ai une question : envisageriez-vous de ne pas les utiliser aujourd'hui ? Probablement pas.

Commençons avec un peu de code. Ci-dessous, vous voyez deux enregistrements – l'un dérivant de l'autre. Les types d'enregistrement sont arrivés avec C# 9. Je les utilise ici uniquement pour la brièveté. Considérez ces deux types comme simplement la classe de base et la classe dérivée.

``` cs
record Person(string FirstName, string LastName);

record Celebrity(string FirstName, string LastName, string KnownFor)
    : Person(FirstName, LastName);
```

Nous pouvons soit instancier un enregistrement et assigner l'instance à une référence, soit assigner une référence à null.

C'est là que l'analyse d'affectation définitive entre en jeu. Si une séquence d'instructions fait que la référence se termine par null, nous devons utiliser le point d'interrogation pour indiquer que la référence peut être null.

``` cs
Person? left = null;
Person? bob = new Person("Bob", "Coder");
Person fowler = new Celebrity("Martin", "Fowler", "famous books");
Person martin = new Celebrity("Bob", "Martin", "SOLID principles");
```

Vous pouvez voir que la deuxième référence (`bob`) est assignée à un objet approprié mais est toujours déclarée nullable. Cela est parfaitement valable dans les scénarios où un objet provient de l'extérieur, et vous ne savez peut-être pas s'il sera présent ou non.

Assurez-vous de ne pas assigner une référence nullable à une référence non-nullable, cependant. Cela causerait un avertissement à la compilation, que vous pouvez élever au niveau d'erreur de compilation si vous préférez.

Il est essentiel de comprendre que la nullabilité n'est pas une propriété du type mais plutôt une indication donnée au compilateur. Les types de référence nullable sont uniquement utilisés lors de l'analyse à la compilation et ne sont jamais stockés dans le type compilé lui-même.

Une conséquence est que vous ne pouvez pas déclarer un paramètre de type nullable dans un type générique. Cela n'aurait pas de sens car le compilateur n'a pas d'endroit où mettre cette information dans le type compilé ! 

Mais voici un rebondissement : nous sommes libres d'indiquer toute référence du type de paramètre générique comme nullable, comme dans le code ci-dessous. Une telle référence est soumise à l'analyse d'affectation définitive comme toute autre.

``` cs
void Showcase<T>(string caption, Action<T?> action, params T?[] objects)
{
    Console.WriteLine($"Showcasing {caption}:".ToUpper());
    foreach (T obj in objects) action(obj);
    Console.WriteLine();
}
```

Nous avons défini la fonction utilitaire pour présenter toutes les situations incorporant des références nulles dans le reste de cet article. Comme je l'ai déjà souligné, ce serait une erreur de compilation de déclarer cette fonction générique comme `Showcase<T?>`, tandis qu'accepter un `T?` nullable dans la liste d'arguments serait parfaitement valide. Cela fait tourner la tête !

Un mystère encore plus grand est à venir : pourquoi ne pas supprimer nullable de la liste d'arguments ? Que signifierait cela ?

``` cs
void Showcase<T>(string caption, Action<T> action, params T[] objects)
{
    Console.WriteLine($"Showcasing {caption}:".ToUpper());
    foreach (T obj in objects) action(obj);
    Console.WriteLine();
}
```

Cela laisserait à l'appelant la détermination de la nullabilité car – maintenant, faites attention ! – un type de paramètre générique concret *peut* être nullable. Il détermine la nullabilité des références, ce qui est une réalité pendant la compilation.

J'espère que vous avez commencé à mieux comprendre ces concepts maintenant. Malheureusement, il faudrait beaucoup d'espace pour expliquer ce concept en profondeur, mais je vous conseillerais certainement d'en apprendre davantage sur la nullabilité des types. Elle fait maintenant partie de C# et est là pour rester.

Permettez-moi de vous donner une rapide démonstration présentant les deux choix possibles :

``` cs
Showcase<Person?>("Nullable reference types", Console.WriteLine,
                  left, bob, fowler, martin);
Showcase<Person>("Non-nullable reference types", Console.WriteLine,
                  fowler, martin);
```

Le premier appel ci-dessus permet des références nulles dans les arguments, tandis que le second appel impose des références non-nullables. Ainsi, le compilateur vérifierait les références passées en arguments dans ce cas et émettrait un avertissement si l'une d'elles est, ou pourrait être, nulle.

Cela conclut notre cours accéléré sur les types de référence nullable en C#. Nous sommes prêts à passer à des sujets plus avancés. 

Avant cela, voici la sortie produite par le code tel que nous l'avons jusqu'à présent :

``` text
SHOWCASING NULLABLE REFERENCE TYPES:
                                                    <-- null est ici !
Person { FirstName = Bob, LastName = Coder }
Celebrity { FirstName = Martin, LastName = Fowler, KnownFor = famous books }
Celebrity { FirstName = Bob, LastName = Martin, KnownFor = SOLID principles }

SHOWCASING NON-NULLABLE REFERENCE TYPES:
Celebrity { FirstName = Martin, LastName = Fowler, KnownFor = famous books }
Celebrity { FirstName = Bob, LastName = Martin, KnownFor = SOLID principles }

```

Faites attention à la ligne vide dans la sortie. C'est là que nous avons passé null à `Console.WriteLine`. La méthode `WriteLine` accepte null et le traite de la même manière qu'une chaîne vide.

## Comment utiliser les motifs `is null` et `is not null`

Une fois que nous avons bien compris la nullabilité, nous pouvons commencer à faire de la logique autour. La plus simple de toutes les opérations consiste à demander si une référence est égale à null.

``` cs
void IsNull(Person? person)
{
    if (person is null)
        Console.WriteLine("Désolé de vous voir partir.");

    if (person is not null)
        Console.WriteLine($"Tout le monde dit bonjour à {person}"!);
}

Showcase("is null and is not null patterns", IsNull,
         left, bob, fowler, martin);
```

L'opérateur `is` teste un objet contre un motif. Nous rencontrerons cet opérateur plusieurs fois dans les sections à venir. 

Dans cette démonstration, vous pouvez voir son utilisation la plus simple : tester contre le motif `null`. Il y a deux possibilités, `is null` et `is not null`, avec la signification qui semble ne nécessiter aucune explication supplémentaire. Oh, mais ce serait une grosse erreur !

Un cas particulier est couvert par les motifs `is null` et `is not null`, qui pourrait être la raison principale de l'introduction de ces motifs en premier lieu. Les deux motifs éviteront d'appeler toute surcharge des opérateurs `==` et `!=`.

Ainsi, en théorie, une classe pourrait surcharger les opérateurs `==` et `!=` et, ce faisant, déclarer qu'un objet particulier devrait être considéré comme égal à une référence nulle. Mais le motif `is null` n'appellera pas la surcharge de l'opérateur – ainsi, il rejettera catégoriquement la comparaison de cet objet non-null à null.

C'est un cas particulier mineur, mais il enseigne comment C# fonctionne sous le capot. Le point essentiel est : vous devriez favoriser `is null` plutôt que `==`, et `is not null` plutôt que `!=` lors des tests pour null/non-null.

Voici l'impression produite lorsque nous exécutons la fonction ci-dessus sur quelques références, l'une d'elles étant null.

``` text
SHOWCASING IS NULL AND IS NOT NULL PATTERNS:
Désolé de vous voir partir.
Tout le monde dit bonjour à Person { FirstName = Bob, LastName = Coder }
Tout le monde dit bonjour à Celebrity { FirstName = Martin, LastName = Fowler, KnownFor = famous books }
Tout le monde dit bonjour à Celebrity { FirstName = Bob, LastName = Martin, KnownFor = SOLID principles }
```

## Comment utiliser les motifs `Type-Test-and-Set`

Le moment est venu d'élever la barre et d'utiliser certaines des méthodes plus complexes de traitement des références nulles. Nous resterons avec l'opérateur `is`, mais cette fois, nous utiliserons sa forme plus puissante : les motifs de test de type.

Chaque référence en C# se résout en un objet (ou un manque de – un null), et chaque objet auquel nous faisons référence possède le descripteur de type. C'est au cœur de tout langage orienté objet. 

Il est donc assez facile pour le runtime .NET de vérifier si une référence pointe vers un objet – et, si oui, si le type d'exécution de cet objet dérive d'un type spécifique, directement ou indirectement.

C'était un peu long, n'est-ce pas ? Décomposons cela en morceaux :

  - Pour tester si une référence référence un objet réel, c'est le motif `person is not null`.
  - Pour ajouter le test si cet objet peut être assigné à un type particulier, nous utilisons le motif de type à la place : `person is Celebrity`.
  - Enfin, pour capturer la référence au type souhaité et l'utiliser dans les instructions et expressions suivantes, nous utilisons l'expression complète de test de type et de définition : `person is Celebrity celeb`.

Ce sont les trois étapes de l'extraction d'informations à partir d'une référence, chacune plus puissante que l'autre. 

Sans plus attendre, voici la méthode qui exerce la forme la plus détaillée : tester contre null et downcasting, le tout dans une expression condensée :

``` cs
void TypeTestAndSet(Person? person)
{
    string report = person switch
    {
        Celebrity celebrity =>
            $"{celebrity.FirstName} {celebrity.LastName} known for {celebrity.KnownFor}",
        Person commonPerson =>
            $"{commonPerson.FirstName} {commonPerson.LastName}",
        _ => string.Empty,
    };
    if (!string.IsNullOrEmpty(report)) Console.WriteLine(report);

    if (person is Celebrity celeb) Console.WriteLine("*** Did you see a celebrity?");
}

Showcase("Type test and set patterns", TypeTestAndSet,
         left, bob, fowler, martin);
```

Vous avez peut-être remarqué que ces expressions implémentent effectivement un downcasting sûr. Le downcasting a été critiqué pendant des décennies, accusé (souvent à juste titre) de causer des défauts de code et des défauts de conception. 

Mais les temps changent ! Les expressions de test de type et de définition viennent du développement logiciel de la programmation fonctionnelle. 

Cet article n'est pas un endroit pour discuter des différences entre le test de type et le downcasting tel que nous le connaissions dans les langages orientés objet du passé. Je vous encourage fortement à en apprendre davantage sur ce sujet intrigant avant de juger.

``` text
SHOWCASING TYPE TEST AND SET PATTERNS:
Bob Coder
Martin Fowler known for famous books
*** Did you see a celebrity?
Bob Martin known for SOLID principles
*** Did you see a celebrity?
```

Ici, vous pouvez voir la sortie produite par la fonction ci-dessus. Comme vous pouvez le voir, chaque type réel est capturé correctement, créant sa sortie spécifique. Et le redouté null a été laissé de côté – j'ai effectivement passé une référence nulle à la fonction à un moment donné mais n'ai pas correspondu à l'un des motifs, et a donc été ignoré.

Cette démonstration serait incomplète sans une note cruciale. L'expression `switch` (de C# 8) attend des motifs dans l'ordre du plus spécifique au plus général. Ce serait une erreur de lister un motif plus spécifique après un motif plus général. Le motif général éclipserait le suivant, ne laissant jamais sa main droite s'exécuter. Par conséquent, l'expression `switch` comme celle ci-dessous cause une erreur de compilation en C#.

``` cs
person switch
{
    Person commonPerson =>
        $"{commonPerson.FirstName} {commonPerson.LastName}",
    Celebrity celebrity =>              // <-- error
        $"{celebrity.FirstName} {celebrity.LastName} known for {celebrity.KnownFor}",
    _ => string.Empty,
};
```

## Comment utiliser les motifs `Property`

Un développement passionnant suit si vous poussez la correspondance de motifs encore plus loin. Une forme spécifique est le motif de propriétés – celui visant à faire correspondre les valeurs et les attributs des propriétés d'un objet (si l'objet existe !).


``` cs
void PropertyPatterns(Person? person)
{
    if (person is { FirstName: "Bob"})
        Console.WriteLine($"Salut Bob, le seul et unique {person.FirstName} {person.LastName}!");
    else
        Console.WriteLine("Pas un Bob");
}

Showcase("Property patterns", PropertyPatterns,
         left, bob, fowler, martin);
```

Vous n'avez pas besoin de spécifier le type si vous n'êtes pas intéressé par le downcasting. Ce sera le type de la référence à gauche de l'opérateur `is`. 

Mais l'utilisation de l'opérateur `is` implique un test de null. Toute référence passant le test `is` sera non-null et sûre à vérifier ses valeurs de propriété du côté droit de l'expression.

Par conséquent, nous lisons la condition de cette instruction `if` comme suit : Si `person` n'est pas null, et que sa propriété `FirstName` a une valeur Bob, alors...

Voici la sortie produite lorsque nous appelons la fonction ci-dessus :

``` text
SHOWCASING PROPERTY PATTERNS:
Pas un Bob
Salut Bob, le seul et unique Bob Coder!
Pas un Bob
Salut Bob, le seul et unique Bob Martin!
```

## Comment utiliser les opérateurs de propagation de null et de coalescence de null

Jusqu'à présent, nous avons fait des choses aux objets, ce qui est maladroit dans une conception orientée objet. Rappelez-vous, en programmation orientée objet, c'est l'objet qui expose le comportement, et, en tant qu'utilisateurs de l'objet, nous ne faisons que des appels à ses méthodes.

Les problèmes surviennent toujours lorsque la référence que nous attendons pour pointer vers un objet est nullable. Faire un appel non protégé sur la référence nulle était la source principale de défauts. Mais maintenant, avec les références nulles et les vérifications d'affectation définitive faites pour nous, nous devrions être protégés des redoutées `NullReferenceExceptions`.

Considérez avoir une méthode exposée par la classe. Nous pouvons utiliser `ToString` comme un exemple simple.

``` cs
record Person(string FirstName, string LastName)
{
    public override string ToString() =>
        $"{FirstName} {LastName}";
}

record Celebrity(string FirstName, string LastName, string KnownFor)
    : Person(FirstName, LastName)
{
    public override string ToString() =>
        $"{base.ToString()} known for {KnownFor}";
}
```

Il y a une différence substantielle entre appeler `ToString` sur les types `Person` et `Person?`. Ce dernier est nullable, et donc un appel non protégé pourrait causer un déréférencement d'une référence nulle, conduisant à une redoutée `NullReferenceException`, comme vous pouvez l'imaginer.

``` cs
Person a = ...;
Person? b = ...;

string x = a.ToString();      // safe
string y = b.ToString();      // unsafe
```

Entrez l'opérateur de propagation de null (`?.`) ! Nous pouvons faire un appel optionnel à une méthode, à condition que la référence soit non-null.

``` cs
Person a = ...;
Person? b = ...;

string x = a.ToString();      // safe
string? y = b?.ToString();    // safe
```

Mais observez les conséquences. Si la méthode retourne `void`, l'appel sera ignoré sur une référence nulle. Si la méthode retourne un type, alors le résultat sera la version nullable de ce type. Vous ne pouvez pas vous attendre à une chaîne de `ToString` sur une référence nullable, vous voyez ? Le compilateur ne peut promettre qu'une chaîne nullable à la place.

Et que faire si nous voulions vraiment une chaîne, une vraie ? Entrez l'opérateur de coalescence de null (`??`) ! Nous pouvons facilement convertir une référence nullable en une référence non-nullable en fournissant une valeur par défaut à prendre lorsque la valeur réelle est nulle à l'exécution.

``` cs
void NullPropagationAndCoalescing(Person? person)
{
    string report = person?.ToString() ?? string.Empty;
    if (!string.IsNullOrEmpty(report)) Console.WriteLine(report);
}

Showcase("Null propagation and null coalescing operators",
         NullPropagationAndCoalescing,
         left, bob, fowler, martin);
```

Dans cet exemple, nous faisons d'abord un appel optionnel à la méthode `ToString` mais court-circuitons ensuite le résultat à une chaîne vide si la référence était nulle. Le résultat est que toute référence nulle produirait une chaîne vide pour l'impression.

``` text
SHOWCASING NULL PROPAGATION AND NULL COALESCING OPERATORS:
                            <-- Une chaîne vide imprimée ici
Bob Coder
Martin Fowler known for famous books
Bob Martin known for SOLID principles
```

## Comment travailler avec des objets optionnels

La dernière méthode pour traiter les nulls dans cet article n'utilisera en fait pas de nulls. Une autre énigme ! L'idée est d'éviter complètement les nulls en modélisant les objets comme potentiellement manquants. Notez le mot "potentiellement" – cela deviendra partie de la déclaration de type de la même manière que la nullabilité.

Si vous êtes nouveau dans les objets optionnels, alors cette courte explication sera tout sauf suffisante pour en apprendre à leur sujet. C# n'a pas de support natif pour les objets optionnels. Vous pouvez choisir l'une des nombreuses implémentations disponibles sur NuGet, la plus populaire étant la bibliothèque LanguageExt.

``` text
dotnet add package LanguageExt.Core
```

Un objet optionnel d'un certain type est un objet qui existe ou n'existe pas. Dans les deux cas, l'objet optionnel lui-même existera toujours. Une autre énigme pour vous à résoudre ! 

Voici comment nous déclarerions quelques objets optionnels :

``` cs
using LanguageExt;

Option<Person>[] maybePeople = 
{
    Option<Person>.None,
    Option<Person>.Some(bob),
    Option<Person>.Some(fowler),
    Option<Person>.Some(martin),
};
```

Les deux formes d'un objet optionnel sont généralement appelées `None` et `Some`. La variante `Some` doit contenir un objet réel. Cela complète la création d'objets optionnels et le code qui n'aura jamais de référence nulle.

Mais quelle est la différence par rapport aux références nulles ? Pourquoi devrions-nous utiliser des objets optionnels ?

L'histoire courte est que les objets optionnels nous permettent d'appliquer des fonctions au contenu de l'objet optionnel – si présent. L'objet optionnel invoquera soit la fonction et passera le contenu à celle-ci, soit ignorera complètement l'appel s'il n'y a pas de contenu.

Par conséquent, un type optionnel est un seul endroit où ce protocole d'appel est maintenant implémenté, le protocole étant en de nombreux points équivalent à un déréférencement sûr des références nulles.

``` cs
void Optional(Option<Person> maybePerson)
{
    string report = maybePerson.Match(
        person => person.ToString(),
        string.Empty);
    maybePerson.Do(Console.WriteLine);
}

Showcase("Optional objects", Optional, maybePeople);
```

La méthode `Match` couvre les deux possibilités : elle mappe soit l'objet `Person` à une chaîne, soit substitue une chaîne vide si la personne est manquante. La méthode `Do` ne passera le contenu à la console que si le contenu existe.

Voici l'impression produite par la méthode `Do` :

``` text
SHOWCASING OPTIONAL OBJECTS:
Bob Coder
Martin Fowler known for famous books
Bob Martin known for SOLID principles
```

Vous ne verrez que les variantes `Some` imprimées. Le seul objet manquant dans le tableau d'entrée n'a produit aucune sortie car cette instance optionnelle a ignoré l'action passée à sa méthode `Do`.

Le bénéfice le plus significatif de l'utilisation d'objets optionnels par rapport aux références nulles est leur capacité à appliquer d'autres fonctions. Nous avons peut-être déjà de nombreuses classes et méthodes différentes implémentées dans notre base de code, toutes les méthodes fonctionnant sur des références non-nullables. Les objets optionnels peuvent combler l'écart entre les objets potentiellement manquants et les méthodes courantes qui ne sont opérationnelles que lorsque rien ne manque.

## Notes finales

Dans ce tutoriel, nous avons commencé par déclarer des objets nulles et tester leur existence en utilisant l'opérateur `is`.

Ensuite, nous avons étendu l'exemple en affichant la richesse des expressions de correspondance de motifs : les expressions de test de type et de définition et les motifs de propriétés.

Nous avons ensuite déplacé le focus de la consommation d'objets à l'appel de leur comportement, de l'opérateur de propagation de null à l'opérateur de coalescence de null, en atterrissant dans le vaste domaine de la programmation fonctionnelle et des objets optionnels.

J'espère que vous avez apprécié le voyage. En guise d'au revoir, je vous invite à en apprendre davantage sur les objets optionnels en C# en regardant ma récente vidéo [How to Avoid Null Reference Exceptions: Optional Objects in C#](https://youtu.be/8-2xr_kBRnQ).