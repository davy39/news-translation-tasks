---
title: Comment utiliser LINQ en C# - Avec des exemples de code
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2024-07-15T20:59:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-linq
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/How-to-use-linq.png
tags:
- name: C
  slug: c
- name: .NET
  slug: net
seo_title: Comment utiliser LINQ en C# - Avec des exemples de code
seo_desc: '.Net (pronounced as "dot net") has many internal libraries and tools, but
  one that wields great power is LINQ (Language Integrated Query). It can be used
  in two ways: the language-level query syntax, or the LINQ API.

  In this article, we''ll explore:


  ...'
---

.Net (prononcé "dot net") dispose de nombreuses bibliothèques et outils internes, mais l'un d'entre eux qui possède un grand pouvoir est LINQ (Language Integrated Query). Il peut être utilisé de deux manières : la syntaxe de requête au niveau du langage, ou l'API LINQ.

Dans cet article, nous explorerons :

* Ce qu'est LINQ.
* Comment l'utiliser.
* Des exemples de quelques méthodes LINQ courantes.

## Table des matières

- [Syntaxe de requête au niveau du langage](#heading-syntaxe-de-requete-au-niveau-du-langage)
- [Syntaxe de méthode](#heading-syntaxe-de-methode)
- [Méthodes courantes de l'API LINQ](#heading-methodes-courantes-de-lapi-linq)
    - [Méthode OrderBy](#heading-methode-orderby)
    - [Méthode First](#heading-methode-first)
    - [Méthode Single/SingleOrDefault](#heading-methode-single-et-singleordefault)
    - [Méthode Select](#heading-methode-select)
- [Comment combiner les méthodes](#heading-comment-combiner-les-methodes)
- [Exécution différée](#heading-execution-differee)
- [Comment enchaîner les méthodes de l'API IQueryable](#heading-comment-enchainer-les-methodes-de-lapi-iqueryable)
- [Conclusion](#heading-conclusion)

Nous utiliserons une classe `Animal` dans cet article :

```csharp
public class Animal
{
    public string Name { get; set; }
    public int Age { get; set; }
    public string Sound { get; set; }
}
```

## Syntaxe de requête au niveau du langage

Vous pouvez voir quelque chose qui ressemble à une requête SQL dans certains extraits de code. Par exemple :

```csharp
var animals = new List<Animal>
{
    new Animal { Name = "Dog", Age = 2, Sound = "Bark" },
    new Animal { Name = "Cat", Age = 2, Sound = "Meow" },
    new Animal { Name = "Fox", Age = 5, Sound = "Bark" }
};


var barkingAnimals =
    from animal in animals
    where animal.Sound == "Bark"
    select animal;
```

Vous pouvez construire des requêtes similaires à SQL pour des tâches complexes, mais cela peut être excessif. Vous pouvez simplifier ces requêtes en utilisant la syntaxe des méthodes de l'API LINQ.

## Syntaxe de méthode

Les méthodes de l'API LINQ utilisent un prédicat (sous la forme d'une extension lambda) pour déterminer les critères.

Nous pouvons écrire la requête ci-dessus en utilisant la syntaxe de méthode comme suit :

```csharp
var barkingAnimals = animals.Where(x => x.Sound == "Bark").ToList();
```

C'est beaucoup plus facile à écrire et beaucoup plus concis pour une requête aussi simple.

Cela se lit aussi beaucoup mieux : les animaux qui aboient sont égaux à tous les animaux où la propriété sound est égale à `Bark`.

Les méthodes de requête LINQ retournent toutes un objet `IQueryable`. Cela informe le compilateur que la variable n'est pas le résultat de la requête, mais la définition de la requête. [voir l'exécution différée plus tard dans cet article.]

Afin d'utiliser les résultats de la requête, nous pouvons soit :

* Itérer sur l'objet "queryable" (par exemple : en utilisant une boucle ForEach)
* Convertir en un type IEnunerable. Par exemple : une Liste/Tableau.

## Méthodes courantes de l'API LINQ

### Méthode OrderBy

`OrderBy` est une méthode utile de l'API LINQ qui vous permet de trier n'importe quel objet IEnumerable.

Nous pouvons l'utiliser comme suit :

```csharp

var orderedByAge = people.OrderBy(x => x.Age);

// ou

var orderedByAgeDescending = people.OrderByDescending(x => x.Age);

```

Les exemples ci-dessus montrent comment trier par âge dans l'ordre croissant et décroissant.

### Méthode First

```csharp
var first = animals.First(x => x.Sound == "Bark");
```

Cela retournera le premier objet de la liste qui correspond aux critères.

### Méthode Single et SingleOrDefault

Cela est utilisé lorsque vous savez/vous attendez qu'il n'y aura qu'un seul objet qui correspond à vos critères.

Exemple :

```csharp
var cat = animals.Single(x => x.Name == "Cat");
```

Les données peuvent changer avec le temps, entraînant des résultats inattendus. Écrire du code défensif est important. Si plusieurs objets nommés "Cat" sont trouvés, une erreur non capturée se produira. Pour éviter cela, utilisez la méthode `SingleOrDefault`, qui retourne une valeur par défaut (null pour les chaînes) en cas d'erreur. Ensuite, vérifiez si la variable cat n'est pas null.

```csharp
var cat = animals.SingleOrDefault(x => x.Name == "Cat");

if(cat != null){
  Console.WriteLine("Un seul chat a été trouvé");
}
```

### Méthode Select

Supposons que vous souhaitiez retourner uniquement les types d'animaux, à partir de l'objet `Animal`. Cela peut être accompli avec la méthode `Select`. Cela créera un nouvel objet pour chaque élément de la liste/tableau.

```csharp
var typesOfAnimal = animals.Select(x => x.Name).ToList();
```

Mais que faire si vous voulez retourner leur nom et leur son ? C'est tout aussi facile avec la méthode `Select`. Cependant, vous devrez créer un objet anonyme au lieu de simplement retourner la propriété.

```csharp
var animals = animals.Select(x => new { Name = x.Name, 
Noise = x.Sound }).ToList();
```

Cela devrait maintenant retourner une liste d'objets anonymes, avec une propriété `Name` et une propriété `Sound`.

## Comment combiner les méthodes

En utilisant la classe `Person` :

```csharp
public class Person
{
    public string Name { get; set; }
    public string Address { get; set; }
}
```

```csharp
var people = new List<Person>()
{
    new() { Name = "Harry Potter", Address = "123 Privet Drive, Hogwarts, United Kingdom" },
    new() { Name = "Alex the Kidd", Address = "Rock Paper Scissors Avenue, United Kingdom" },
    new() { Name = "Donkey Kong", Address = " The Monkey Temple, Jungle" }
};
```

Vous pouvez combiner les méthodes de l'API LINQ pour effectuer plusieurs actions. Prenons le scénario suivant comme exemple :

Nous voulons trouver toutes les personnes dans une liste dont l'adresse contient "United Kingdom".

Pour accomplir cela, vous pouvez utiliser une combinaison de `Where()` et `Contains()`, en passant la fonction `Contains()` comme partie du prédicat.

```csharp
var ukResidents = peopleList.Where(p => p.Address.Contains("United Kingdom")).ToList();
```

## Exécution différée

Les requêtes LINQ utilisent ce qu'on appelle l'exécution différée. Cela signifie que la requête ne sera pas exécutée immédiatement lorsqu'elle est définie.

Au lieu de cela, elle est exécutée lorsque les résultats de la requête sont itérés ou lorsque certains opérateurs déclenchent explicitement l'exécution. Cette exécution différée permet des optimisations et améliore les performances en évitant des calculs inutiles.

Cela revient à ce que j'ai discuté précédemment avec la conversion de `IQueryable` en un autre objet. Par exemple, une liste utilisant `.ToList()`. C'est le `ToList()` qui convertit l'objet `IQueryable` en une liste et exécute réellement la requête.

Regardons un exemple :

```csharp
var people = new List<Person>()
{
    new() { Name = "Harry Potter", Address = "123 Privet Drive, Hogwarts, United Kingdom" },
    new() { Name = "Alex the Kidd", Address = "Rock Paper Scissors Avenue, United Kingdom" },
    new() { Name = "Donkey Kong", Address = " The Monkey Temple, Jungle" }
};

// puis nous définirons la requête
var peopleCalledHarryPotter = people.Where(x => x.Name == "Harry Potter");

// cela créera l'objet de requête, vous pourriez écrire d'autres codes ici.

// maintenant, convertissez l'objet de requête IQueryable en une liste, invoquant ainsi la requête réelle.

var list = peopleCalledHarryPotter.ToList();
```

Bien qu'il s'agisse d'un exemple basique, cela démontre que vous pouvez créer un objet queryable et exécuter du code supplémentaire avant d'exécuter réellement la requête en utilisant la méthode d'extension `.ToList()`.

## Comment enchaîner les méthodes de l'API IQueryable

De manière similaire à la combinaison de `Where` et `Contains`, vous pouvez améliorer davantage vos requêtes en enchaînant les méthodes de l'API LINQ.

Par exemple, utiliser `Where()` et `GroupBy()` ensemble vous permet de filtrer puis de regrouper les données par une propriété.

Appliquons ce que nous avons appris et enchaînons ces méthodes. Au lieu d'utiliser `.ToList()` pour créer une nouvelle variable avec les résultats, nous pouvons utiliser l'objet de requête dans une boucle `ForEach` pour exécuter la requête et itérer sur les résultats simultanément.

Mettez à jour la classe `Person` pour qu'elle ait une propriété `Age` :

```csharp
public class Person
{
    public string Name { get; set; }
    public string Address { get; set; }
    public int Age { get; set; }
}
```

Puis regardez le code suivant, qui filtrera d'abord la liste des personnes, puis les regroupera en fonction de `Age`.

```csharp
using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
    public static void Main()
    {
        List<Person> people = new List<Person>
        {
            new Person { Name = "John", Age = 30 },
            new Person { Name = "Alice", Age = 25 },
            new Person { Name = "Bob", Age = 30 },
            new Person { Name = "Charlie", Age = 25 },
            new Person { Name = "Eve", Age = 35 }
        };

        var groupsOfPeople = people
            .Where(p => p.Age >= 30)  // Filtrer les personnes dont l'âge est >= 30
            .GroupBy(p => p.Age);    // Regrouper les personnes par leur âge

        foreach (var group in groupsOfPeople)
        {
            Console.WriteLine($"Groupe d'âge : {group.Key}"); // afficher l'âge
            foreach (var person in group)
            {
                Console.WriteLine($"Nom : {person.Name}, Âge : {person.Age}");
            }
        }
    }
}
```

Cette combinaison de méthodes LINQ nous permet de définir des requêtes plus complexes sans utiliser la syntaxe de requête au niveau du langage.

Parfois, cela peut dépendre des préférences personnelles, mais je crois que la syntaxe de méthode est beaucoup plus lisible.

## Conclusion

Dans cet article, nous avons exploré la puissance de LINQ dans .NET, en comparant sa syntaxe de requête au niveau du langage et sa syntaxe de méthode. Nous avons démontré comment simplifier des requêtes complexes en utilisant les méthodes de l'API LINQ et discuté des méthodes courantes comme `OrderBy`, `First()`, `Single()`, `SingleOrDefault()`, et `Select`.

Nous avons souligné l'importance d'écrire du code défensif et le concept d'exécution différée, qui optimise les performances. En combinant et en enchaînant les méthodes LINQ, vous pouvez créer des requêtes complexes et lisibles de manière efficace.

LINQ est un outil polyvalent qui améliore votre capacité à gérer les données dans les applications .NET. Que vous utilisiez la syntaxe de requête ou la syntaxe de méthode, LINQ fournit un moyen puissant d'écrire du code efficace et maintenable.

Vous pouvez trouver des exemples utiles sur le site de Microsoft [ici](https://learn.microsoft.com/en-us/dotnet/csharp/tutorials/working-with-linq)

Comme toujours, je serais ravi de recevoir des commentaires ou des discussions sur le sujet. Vous pouvez me suivre sur [Twitter](https://twitter.com/grantdotdev)