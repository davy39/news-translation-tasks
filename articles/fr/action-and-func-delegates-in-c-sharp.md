---
title: Action et Func Delegates en C# – Expliqués avec des Exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-06T19:46:15.000Z'
originalURL: https://freecodecamp.org/news/action-and-func-delegates-in-c-sharp
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Untitled--Copy
seo_title: Action et Func Delegates en C# – Expliqués avec des Exemples
---

1-.png
tags:
- name: C
  slug: c
seo_title: null
seo_desc: "Par Umoh Tobby\nEn C#, les types appelés délégués représentent des références à des méthodes\n  \ avec des signatures spécifiques. \nLes développeurs utilisent les délégués pour implémenter des méthodes de rappel,\
  \ gérer des événements et effectuer des tâches où l'exécution d'une méthode à un moment ultérieur est nécessaire.\
  \ \nC#..."
---

Par Umoh Tobby

En C#, les types appelés délégués représentent des références à des méthodes avec des signatures spécifiques. 

Les développeurs utilisent les délégués pour implémenter des méthodes de rappel, gérer des événements et effectuer des tâches où l'exécution d'une méthode à un moment ultérieur est nécessaire. 

C# offre divers délégués, et deux des plus couramment utilisés sont Action et Func, tous deux définis dans l'espace de noms System.

Dans ce tutoriel, vous apprendrez à connaître les délégués Action et Func en C#.

Pour télécharger le code source de cet article, visitez ce **[Dépôt GitHub](https://github.com/TobbyJay/ActionAndFuncDelegate)**.

Commençons par discuter du délégué Action et explorer son utilisation

## Qu'est-ce que le Délégué Action en C#?

Le délégué Action est un type de délégué prédéfini qui encapsule une méthode avec zéro ou plusieurs paramètres d'entrée qui ne retourne pas de valeur. En d'autres termes, un délégué Action représente une méthode retournant void.

Considérez cet exemple, démontrant l'utilisation d'un délégué Action dans une simple application de calculatrice console:

```c#
Action<int, int> ActionCalculator = (a, b) =>
{
    Console.WriteLine($"Résultat de l'addition: {a + b}");
    Console.WriteLine($"Résultat de la soustraction: {a - b}");
    Console.WriteLine($"Résultat de la multiplication: {a * b}");
    Console.WriteLine($"Résultat de la division: {a / b}");
};

ActionCalculator(4, 2);
```

Dans cet exemple, nous avons défini un délégué Action nommé ActionCalculator. Il prend deux paramètres entiers et effectue quatre opérations arithmétiques de base en utilisant ces paramètres. Ensuite, nous invoquons le délégué avec les valeurs 4 et 2.

L'application a produit la sortie suivante lors de l'exécution:

```c#
Résultat de l'addition: 6
Résultat de la soustraction: 2
Résultat de la multiplication: 8
Résultat de la division: 2
```

Comme vous pouvez le voir, l'utilisation d'un délégué Action simplifie le processus de passage d'une méthode en tant que paramètre à une autre méthode.

## Qu'est-ce que le Délégué Func en C#?

Le délégué Func est un autre type de délégué prédéfini qui représente une méthode avec zéro ou plusieurs paramètres d'entrée qui retourne une valeur. Contrairement au délégué Action, le type de retour d'un délégué Func peut être n'importe quel type.

Considérons un exemple d'utilisation d'un délégué Func dans une simple application de calculatrice console.

Dans cet exemple, nous définissons une classe Calculator:

```c#
public class Calculator
{
    public int Add(int a, int b) => a + b;
    public int Subtract(int a, int b) => a - b;
    public int Multiply(int a, int b) => a * b;
    public int Divide(int a, int b) => a / b;
}
```

La classe Calculator contient des méthodes pour effectuer quatre opérations arithmétiques de base.

Ensuite, nous créons quatre délégués Func, chaque délégué pointant vers l'une des méthodes de la calculatrice:

```c#
var FuncCalculator = new Calculator();

Func<int, int, int> add = FuncCalculator.Add;
Func<int, int, int> subtract = FuncCalculator.Subtract;
Func<int, int, int> multiply = FuncCalculator.Multiply;
Func<int, int, int> divide = FuncCalculator.Divide;

Console.WriteLine($"Résultat de l'addition: {add(4, 2)}");
Console.WriteLine($"Résultat de la soustraction: {subtract(4, 2)}");
Console.WriteLine($"Résultat de la multiplication: {multiply(4, 2)}");
Console.WriteLine($"Résultat de la division: {divide(4, 2)}");
```

Enfin, nous invoquons chacun des délégués avec les valeurs 4 et 2 et imprimons les résultats sur la console.

L'application de calculatrice a affiché la sortie suivante lors de l'exécution:

```c#
Résultat de l'addition: 6
Résultat de la soustraction: 2
Résultat de la multiplication: 8
Résultat de la division: 2
```

Les délégués Func offrent une approche simple pour définir et utiliser des méthodes en les passant en tant que paramètres et en les retournant en tant que résultats.

## **Conclusion**

En conclusion, les délégués Action et Func fournissent un moyen d'encapsuler un appel de méthode dans un objet délégué. 

Les développeurs utilisent les délégués Action lorsqu'une méthode ne retourne pas de valeur, et les délégués Func lorsqu'une méthode retourne une valeur.