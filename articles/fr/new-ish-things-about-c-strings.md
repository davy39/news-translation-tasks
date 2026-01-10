---
title: Les chaînes de caractères en C# – Nouveautés expliquées avec des exemples de
  code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-26T13:49:06.000Z'
originalURL: https://freecodecamp.org/news/new-ish-things-about-c-strings
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/things-about-strings.png
tags:
- name: C
  slug: c
seo_title: Les chaînes de caractères en C# – Nouveautés expliquées avec des exemples
  de code
seo_desc: 'By Deborah Kurata

  Much of what we work with in our code are strings. Let''s look at some of the newish
  things about C# strings ... including raw string literals and raw string interpolation
  that are new in C# 11.

  Raw string literals make it easy to bu...'
---

Par Deborah Kurata

Une grande partie de ce avec quoi nous travaillons dans notre code sont des chaînes de caractères. Examinons certaines des nouveautés concernant les chaînes de caractères en C#, y compris les littéraux de chaîne brute et l'interpolation de chaîne brute, qui sont nouveaux dans C# 11.

Les littéraux de chaîne brute facilitent la création de chaînes complexes et multilingues, y compris du JSON, de manière simple et flexible. Et sans nécessiter d'échappement.

Regardez la vidéo associée ici :

%[https://youtu.be/A5FRgglBkJ8]

Trouvez le [code exemple ici](https://github.com/DeborahK/CSharp-Examples).

Dans cet article, nous commencerons par certaines des techniques actuelles que nous utilisons pour manipuler les chaînes de caractères, les problèmes que nous avons rencontrés en utilisant ces techniques, et les nouvelles fonctionnalités de C# 11 qui aident à la manipulation des chaînes de caractères.

## **Littéral de chaîne entre guillemets**

La manière principale dont nous avons travaillé avec les chaînes de caractères en C# est en utilisant un littéral de chaîne entre guillemets. Ceux-ci sont disponibles depuis le début de C#.

```csharp
string header = "<div class=\"card-header\">Vehicle Detail</div>"
```

Mais si nous avons des guillemets dans notre chaîne, la chaîne devient un peu désordonnée. Nous échappons ces guillemets avec une barre oblique inverse. Ainsi, le compilateur C# peut faire la différence entre les guillemets extérieurs et les guillemets à l'intérieur de la chaîne.

Les littéraux de chaîne entre guillemets standard sont souvent les meilleurs pour les chaînes sur une seule ligne sans caractères nécessitant d'être échappés.

## **Littéral de chaîne textuel**

Pour les chaînes qui s'étendent sur plusieurs lignes, nous utilisons un littéral de chaîne textuel. Nous définissons un littéral de chaîne textuel avec un arobase devant la première marque de guillemet. Textuel signifie "tel quel", et est destiné à définir une chaîne multilingue qui s'affiche "telle quelle".

```csharp
string header = @"
   <div class=""card"">
     <div class=""card-header"">
       Vehicle Detail
   </div>
";
```

Mais une fois de plus, les marques de guillemet sont un défi ! Les littéraux de chaîne textuelle nécessitent que nous utilisions des marques de guillemet doubles pour indiquer une marque de guillemet à l'intérieur d'une chaîne. Cela ne semble pas horrible dans ce cas ... mais lors de la création d'une chaîne avec de nombreuses marques de guillemet, comme la définition de JSON, cela peut être assez désordonné.

De plus, l'indentation des littéraux de chaîne textuelle peut poser problème.

```csharp
  foreach (var vehicle in vehicles)
  {
    if (goodCredit)
    {
      if (newVehicle)
      {
        message = @"
          Congratulations on your new vehicle!
          We hope you enjoy driving it as much as we enjoyed building it.
          ";
      }
     }
   }
```

Ci-dessus, nous avons un morceau de code typique avec plusieurs indentations. Et nous indentons le message correctement dans le bloc if. Mais ensuite, si nous affichons le message, les indentations sont incluses comme montré dans la Figure 1. Cela peut ne pas être le résultat souhaité.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/verbatim-string.png)
_Figure 1. Le littéral de chaîne textuelle conserve son indentation_

Pour le corriger, nous devrions désindenter le texte pour l'aligner avec la marge de gauche.

```csharp
  foreach (var vehicle in vehicles)
  {
    if (goodCredit)
    {
      if (newVehicle)
      {
        message = @"
Congratulations on your new vehicle!
We hope you enjoy driving it as much as we enjoyed building it.
";
      }
    }
   }
```

Le résultat est alors meilleur comme montré dans la Figure 2. Mais le code semble un peu désordonné. Et si un développeur insoupçonné vient "nettoyer" l'indentation, notre résultat n'est pas celui que nous avions prévu.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/indentation-not-saved.png)
_Figure 2. Le littéral de chaîne textuelle doit être désindenté dans le code pour apparaître sans indentation_

## **Littéral de chaîne brute (nouveau dans C#11)**

Une nouvelle fonctionnalité de C# 11, sortie en 2022, est le **littéral de chaîne brute**. Un littéral de chaîne brute est un nouveau format pour les littéraux de chaîne. Ils permettent des espaces blancs, des nouvelles lignes, des guillemets intégrés, d'autres caractères spéciaux, ou tout ce que vous voulez !

Un littéral de chaîne brute commence par au moins 3 guillemets. Et se termine par un ensemble correspondant de guillemets. Tout ce qui se trouve sur les lignes entre les guillemets d'ouverture et de fermeture est la chaîne souhaitée.

```csharp
 string header = """
      <div class="card">
        <div class="card-header">
          Vehicle Detail
        </div>
      </div>
    """;
```

Remarquez qu'il n'est pas nécessaire de doubler les guillemets ou d'utiliser des caractères d'échappement. La chaîne s'affiche exactement telle qu'elle est. C'est un choix bien meilleur pour les chaînes multilingues par rapport au littéral de chaîne textuelle d'origine.

Une autre caractéristique importante des littéraux de chaîne brute est que la chaîne résultante s'aligne sur les guillemets de fermeture. Dans l'exemple ci-dessous, nous alignons le message avec le début du guillemet de fermeture.

```csharp
  foreach (var vehicle in vehicles)
  {
    if (goodCredit)
    {
      if (newVehicle)
      {
        message = """
          Congratulations on your new vehicle!
          We hope you enjoy driving it as much as we enjoyed building it.
          """;
      }
     }
   }
```

Lorsque nous affichons cette chaîne, elle est alignée de manière appropriée sur la marge de gauche comme montré dans la Figure 3.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/indented-based-on-closing-quote.png)
_Figure 3. Le littéral de chaîne brute est indenté en fonction du guillemet de fermeture_

Rappelons que j'ai dit que les littéraux de chaîne brute commencent par **au moins** trois guillemets. L'équipe C# voulait que la fonctionnalité ait une longue durée de vie, alors ils l'ont rendue configurable. Si pour une raison quelconque vous avez besoin de guillemets triples à l'intérieur de la chaîne, vous pourriez utiliser des guillemets quadruples pour enfermer le littéral de chaîne brute. Assurez-vous simplement que la chaîne se termine par le même nombre de guillemets.

Un littéral de chaîne brute sur une seule ligne nécessite que les guillemets d'ouverture et de fermeture soient sur la même ligne. Voici un littéral de chaîne brute sur une seule ligne. Remarquez les trois marques de guillemet au début et à la fin. Ensuite, les guillemets intégrés ne nécessitent aucun caractère spécial.

```csharp
string text = """He said, "None shall Pass"."""
```

Un littéral de chaîne brute sur plusieurs lignes nécessite que les guillemets d'ouverture soient sur la ligne au-dessus de la chaîne brute et que les guillemets de fermeture soient sur leur propre ligne en dessous de la chaîne brute. Voici une chaîne JSON définie en utilisant un littéral de chaîne brute. Remarquez que nous pouvons utiliser des marques de guillemet normales autour des noms de champs et des valeurs de chaîne. Ainsi, notre JSON ressemble à du JSON.

```csharp
  string vehicleJSON = """
    {
      "id": 1,
      "name": "AT-AT",
      "price": 19416.13
    }
    """;
```

Puisque l'indentation du littéral de chaîne brute est définie par le début des guillemets de fermeture, le texte ne doit **pas** être désindenté par rapport à cet ensemble de guillemets de fermeture.

L'exemple ci-dessous a l'accolade de fermeture à gauche des guillemets de fermeture. Donc ce code génère une erreur de syntaxe comme montré dans la Figure 4.

```csharp
  string vehicleJSON = """
    {
      "id": 1,
      "name": "AT-AT",
      "price": 19416.13
  }
    """;
```

![Image](https://www.freecodecamp.org/news/content/images/2024/04/error-message.png)
_Figure 4. Message d'erreur lorsque le littéral de chaîne brute est désindenté au-delà des guillemets de fermeture_

Utilisez des littéraux de chaîne brute au lieu de chaînes textuelles lorsque vous travaillez avec plusieurs lignes ou des chaînes avec des guillemets ou d'autres caractères spéciaux nécessitant des séquences d'échappement.

Avec la puissance, la flexibilité et la clarté des littéraux de chaîne brute, vous n'utiliserez peut-être plus jamais de littéral de chaîne textuelle !

## **Interpolation de chaîne**

Nous voulons souvent inclure la valeur d'une variable ou d'une expression dans une chaîne. C'est le but de l'interpolation. L'interpolation de chaîne nous permet d'insérer une expression dans un littéral de chaîne.

```csharp
string pageTitle = "Vehicle Detail";
string header = $"Header: {pageTitle}";
```

Nous identifions une chaîne interpolée avec un signe dollar devant la première guillemet. Nous ajoutons une ou plusieurs expressions dans la chaîne en utilisant des accolades. Les accolades agissent comme un espace réservé.

À l'exécution, l'expression est évaluée et la valeur appropriée apparaît dans la chaîne à la place des accolades et de l'expression. Ainsi, nous pouvons intégrer la valeur d'une variable ou d'une expression dans un littéral de chaîne.

Voici quelques exemples. Nous pouvons inclure un calcul ou appeler une méthode. Toute expression C# valide peut être insérée dans les accolades.

```csharp
string answer = $"Answer: { 20 * 2 + 2 }";

string pageTitle = "Vehicle Detail";
string header = $"Header: {PrepareTitle(pageTitle)}";
```

### Interpolation de chaîne constante (Nouveau dans C# 10)

Depuis C# 10, nous pouvons définir une chaîne interpolée comme une constante ... mais seulement si l'expression interpolée est une constante, comme dans cet exemple.

```csharp
const string pageTitle = "Vehicle Detail";
const string header = $"Header: {pageTitle}";
```

Puisque l'expression interpolée est une constante dans cet exemple, la chaîne interpolée peut être définie comme une constante. Cela peut ne pas être une exigence très courante, mais c'est bien de savoir que la fonctionnalité est disponible si vous en avez besoin.

## Sauts de ligne dans les expressions d'interpolation (Nouveau dans C# 11)

Nouveau dans C# 11, nous pouvons utiliser des expressions interpolées multilingues. Cela peut rendre le code à l'intérieur des accolades un peu plus facile à lire.

Dans cet exemple, nous utilisons l'opérateur conditionnel ternaire. Si la variable de titre de page est vide, nous définissons "no title", sinon nous définissons le titre de page. Remarquez que nous devons enfermer l'opérateur conditionnel ternaire dans des parenthèses à l'intérieur des accolades.

```csharp
    string pageTitle = "";

    string header = $"Header: {
      (pageTitle == ""
        ? "No title"
        : pageTitle)
    }";
```

Mettre trop de code à l'intérieur d'une expression d'interpolation rend ce code difficile à déboguer et à tester. Soyez donc prudent quant à la quantité de code que vous écrivez dans l'expression interpolée. Dans certains cas, il peut être préférable de mettre le code dans une fonction et d'appeler cette fonction à partir de l'expression interpolée.

## **Interpolation de chaîne textuelle**

Nous pouvons combiner l'interpolation de chaîne avec des chaînes textuelles en utilisant `@$` ou `$@`. Ainsi, nous pouvons avoir plusieurs lignes de texte et, éventuellement, plusieurs lignes pour notre expression d'interpolation.

```csharp
    string pageTitle = "Vehicle Detail";
    string header = @$"
      <div class=""card"">
        <div class=""card-header"">
          {(pageTitle == ""
           ? "No title"
           : pageTitle)}
        </div>
      </div>
    ";
```

Mais puisque c'est une chaîne textuelle, nous avons à nouveau besoin de guillemets doubles pour les guillemets intégrés.

## **Interpolation de chaîne brute (Nouveau dans C# 11)**

Une meilleure option pour l'interpolation de chaîne est l'interpolation de chaîne brute, disponible dans C# 11. Ici, nous ajoutons le signe dollar devant nos trois ensembles de guillemets. Ensuite, nous pouvons définir plusieurs lignes de texte et plusieurs lignes pour notre expression d'interpolation.

```csharp
 string pageTitle = "Vehicle Detail";
  string header = $"""
      <div class="card">
        <div class="card-header">
          {(pageTitle == ""
           ? "No title"
           : pageTitle)}
        </div>
      </div>
    """;
```

Examinons un autre exemple, la création d'une chaîne JSON. C'est la chaîne que nous voulons créer. Mais nous voulons utiliser l'interpolation pour le prix au lieu de le coder en dur.

```csharp
   {
      "id": 1,
      "name": "AT-AT",
      "price": 19416.13
    }
```

Remarquez que la syntaxe JSON nécessite des accolades autour de l'objet. Mais si nous voulons utiliser une chaîne interpolée, l'interpolation a besoin d'accolades. Alors allons-nous devoir échapper ces accolades ? Non !

L'équipe C# voulait une solution d'interpolation de chaîne qui soit configurable. Donc pour l'interpolation de chaîne brute, nous pouvons optionnellement utiliser **deux** signes dollar. Les **deux** signes dollar signifient que nous avons besoin de **deux** ensembles d'accolades pour l'interpolation. Ainsi, l'ensemble unique d'accolades peut être interprété comme faisant partie du littéral de chaîne.

```csharp
    decimal price = 19416.13M;
    string vehicleJSON = $$"""
      {
        "id": 1,
        "name": "AT-AT",
        "price": {{price}}
      }
      """;
```

Ou nous pourrions utiliser trois signes dollar avec trois ensembles d'accolades, et ainsi de suite. Le nombre de signes dollar indique le nombre de paires d'accolades requises pour l'interpolation.

Très cool !

## **Conclusion**

Ce tutoriel a passé en revue les options pour définir des littéraux de chaîne et pour l'interpolation de chaîne.

Le nouveau littéral de chaîne brute et l'interpolation de chaîne brute simplifient la gestion des chaînes, offrant une solution flexible pour travailler avec des chaînes.

Regardez la vidéo ici :

%[https://youtu.be/A5FRgglBkJ8]

Ou essayez le [code exemple ici](https://github.com/DeborahK/CSharp-Examples).