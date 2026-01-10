---
title: Comment convertir une chaîne en entier en C# – Tutoriel avec exemple de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-29T20:03:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-a-string-to-an-int-in-c-tutorial-with-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/youtube-cover.jpg
tags:
- name: C
  slug: c
- name: Tutorial
  slug: tutorial
seo_title: Comment convertir une chaîne en entier en C# – Tutoriel avec exemple de
  code
seo_desc: 'By Ondrej Polesny

  Converting a string to an integer is common practice when you''re dealing with user
  input, JSON data, API responses, or regular expressions. But what''s the right way
  to do it for each scenario?

  In this article, I''ll explain three way...'
---

Par Ondrej Polesny

Convertir une chaîne en entier est une pratique courante lorsque vous traitez des entrées utilisateur, des données JSON, des réponses d'API ou des expressions régulières. Mais quelle est la bonne façon de le faire pour chaque scénario ?

Dans cet article, je vais expliquer trois façons de convertir une chaîne en nombre en C# et je vais vous montrer comment choisir la bonne méthode pour votre scénario.

## Déterminer la source de vos données

Tout d'abord, voyons d'où proviennent vos données. Il est facile de convertir la chaîne "123" en entier, mais dans le monde réel, ce n'est jamais aussi simple. 

La "chaîne de nombre" peut provenir d'une base de données, d'un fichier texte, d'une API ou d'un utilisateur de votre application. Alors, à quel point êtes-vous sûr qu'il s'agit vraiment d'un nombre ?

| Source de données | Confiance | Ce qui peut arriver |
| ------------- |:-------------:| ----- |
| Entrée utilisateur | 🤁 | "1.23"<br/>"hello" |
| Données JSON | 😐 | "123.1"<br/>"" |
| Réponse API | 😐 | "11,7"<br/>"" |
| Correspondance d'expression régulière | 🤢 | expression invalide permettant non seulement des nombres |

## À quel point votre nombre peut-il être grand ?

Vous devez également savoir à quel point votre nombre cible peut être grand. Dans le cadre de cet article, nous parlons de Int. Cela est généralement considéré comme `Int32` (`int`), mais vous pouvez également utiliser `Int16` (`short`) et `Int64` (`long`) selon la taille des nombres que vous attendez.

| Type | Plus grand nombre |
| ------------- | ------------- |
| `Int16` (`short`) | 32767 (`Int16.MaxValue`) |
| `Int32` (`int`) | 2,147,483,647 (`Int32.MaxValue`) |
| `Int64` (`long`) | 9,223,372,036,854,775,807 (`Int64.MaxValue`) |

## int.Parse(String) – confiance de l'entrée : élevée 🤢

Utilisez `int.Parse` lorsque vous êtes sûr que l'entrée est vraiment un nombre. Il peut également analyser des nombres dans des formats spécifiques à une culture ou d'autres formats largement connus, mais vous devez connaître le format exact :

| Signature | Sortie |
| ---- | ---- |
| `int.Parse("123")` | 123 |
| `int.Parse("")` | lance `FormatException` |
| `int.Parse(null)` | lance `ArgumentNullException` |
| `int.Parse("123,000")` | lance `FormatException` |
| `int.Parse("123,000",`<br/>`  System.Globalization.NumberStyles.AllowThousands,`<br/>`  new System.Globalization.CultureInfo("en-US"))` | 123000 |

## Convert.ToInt32(String) – confiance de l'entrée : moyenne 😐

`Convert` est très similaire à `int.Parse` avec une exception : `null` est converti en 0 et ne lance pas d'exception. Il peut également gérer d'autres types de données d'entrée (pas seulement des chaînes) :

| Signature | Sortie |
| ---- | ---- |
| `Convert.ToInt32("123")` | 123 |
| `Convert.ToInt32("")` | lance `FormatException` |
| `Convert.ToInt32(null)` | 0 |
| `Convert.ToInt32("123,000")` | lance `FormatException` |
| `Convert.ToInt32("1.23")` | lance `FormatException` |
| `Convert.ToInt32(1.23)` | 1 |

_Note : Vous pouvez utiliser_ `_Convert.ToInt32_` _pour supprimer la précision d'un nombre derrière un point décimal. Cependant, pour assurer une bonne lisibilité du code, vous devriez utiliser_ `_Math.Floor_` _pour accomplir cette tâche._

## Int*.TryParse(String, Int32) - confiance de l'entrée : faible 🤁

Utilisez `TryParse` chaque fois que vous ne faites pas confiance à votre source de données. Par exemple, lorsque vous obtenez une entrée utilisateur ou analysez et validez des données provenantes de formulaires soumis :

| Signature | Sortie |
| ---- | ---- |
| `int number;`<br/>`bool convertible = Int32.TryParse("123", out number)` | number = 123<br/>convertible = True |
| `int number;`<br/>`bool convertible = Int32.TryParse("hello", out number)` | number = 0<br/>convertible = False |
| `int number;`<br/>`bool convertible = Int32.TryParse("", out number)` | number = 0<br/>convertible = False |

_Note : Vous pouvez également déplacer la définition du nombre dans l'appel de la méthode `TryParse` en tapant `out int number`._

L'exemple le plus typique est avec `Console.ReadLine` :

```csharp
while (!Int32.TryParse(Console.ReadLine(), out int number))
{
	Console.WriteLine("Veuillez entrer un nombre");
}
Console.WriteLine(number);
```

## Conclusion

Dans cet article, je vous ai montré trois façons de convertir un nombre en chaîne en C# et expliqué comment décider quelle méthode utiliser en fonction de la source de vos données et de la confiance que vous avez en elle.

Si vous ne voulez pas manquer mes nouveaux articles, suivez-moi sur [Twitter](https://twitter.com/ondrabus).