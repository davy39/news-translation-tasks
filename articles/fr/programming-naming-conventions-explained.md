---
title: Conventions de nommage en programmation – Camel, Snake, Kebab et Pascal Case
  expliqués
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2022-08-22T15:16:55.000Z'
originalURL: https://freecodecamp.org/news/programming-naming-conventions-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/Programming-Naming-Conventions-Explained.jpg
tags:
- name: Naming Conventions
  slug: naming-conventions
- name: General Programming
  slug: programming
seo_title: Conventions de nommage en programmation – Camel, Snake, Kebab et Pascal
  Case expliqués
seo_desc: 'If you''ve been programming for a while, you may have heard the words "camel
  case" or "pascal case". And maybe you''re wondering what those terms mean. Well,
  let me explain.

  What are Naming Conventions in Programming?

  Apart from the hard and fast rules...'
---

Si vous programmez depuis un certain temps, vous avez peut-être entendu les termes "camel case" ou "pascal case". Et peut-être vous demandez-vous ce que signifient ces termes. Eh bien, laissez-moi vous expliquer.

## Qu'est-ce que les conventions de nommage en programmation ?

En plus des règles strictes que nous avons avec chaque langage de programmation, il existe également des conventions. Ce sont des ensembles de normes généralement acceptées par la majorité des développeurs.

Parmi toutes sortes de conventions, les conventions de nommage sont parmi les plus courantes. Parce qu'en tant que programmeurs, nous nommons beaucoup de choses. Comme les variables, les fonctions, les classes, les méthodes, les interfaces et ainsi de suite.

Au fil des années, les développeurs ont utilisé différents types de casse pour nommer différentes entités dans leur code. Et quatre d'entre eux se sont avérés être les plus populaires. Ils sont :

* [Camel Case](#heading-qu-est-ce-que-le-camel-case)
* [Snake Case](#heading-qu-est-ce-que-le-snake-case)
* [Kebab Case](#heading-qu-est-ce-que-le-kebab-case)
* [Pascal Case](#heading-qu-est-ce-que-le-pascal-case)

Regardons quelques exemples pour que vous puissiez voir comment cela fonctionne, d'accord ?

## Qu'est-ce que le Camel Case ?

En camel case, vous commencez un nom par une lettre minuscule. Si le nom comporte plusieurs mots, les mots suivants commenceront par une lettre majuscule :

Voici quelques exemples de camel case : `firstName` et `lastName`.

## Qu'est-ce que le Snake Case ?

Comme en camel case, vous commencez le nom par une lettre minuscule en snake case. Si le nom comporte plusieurs mots, les mots suivants commenceront par des lettres minuscules et vous utilisez un tiret bas (_) pour séparer les mots.

Voici quelques exemples de snake case : `first_name` et `last_name`.

## Qu'est-ce que le Kebab Case ?

Le kebab case est similaire au snake case, mais vous utilisez un tiret (-) au lieu d'un tiret bas (_) pour séparer les mots.

Voici quelques exemples de kebab case : `first-name` et `last-name`.

## Qu'est-ce que le Pascal Case ?

Contrairement aux exemples précédents, les noms en pascal case commencent par une lettre majuscule. Dans le cas des noms avec plusieurs mots, tous les mots commenceront par des lettres majuscules.

Voici quelques exemples de pascal case : `FirstName` et `LastName`.

## Quand utiliser chaque convention de nommage

Maintenant, selon le langage sur lequel vous travaillez et ce que vous nommez, le type de casse préféré peut changer.

Par exemple, selon le [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/), les noms de variables et de fonctions doivent utiliser le snake case :

```python
user_name = 'Farhan'

def reverse_name(name):
	return name[::-1]
```

Regardons maintenant JavaScript. Selon le [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript), les noms de variables et de fonctions doivent utiliser le camel case :

```javascript
const userName = "Farhan";

function reverseName(name) {
 	return name.split("").reverse().join("");
}
```

Bien que Python et JavaScript vous obligent à suivre différentes conventions lorsque vous nommez des variables et des fonctions, les deux langages vous obligent à utiliser le pascal case lors du nommage d'une classe.

Des guides de style sont disponibles pour plus ou moins tous les langages de programmation populaires. Voici quelques-uns des plus couramment utilisés :

* Python - [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
* JavaScript - [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)
* Java - [Java style guide](https://www.cs.cornell.edu/courses/JavaAndDS/JavaStyle.html)
* C# - [C# Coding Convention](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions)
* Go - [Uber Go Style Guide](https://github.com/uber-go/guide/blob/master/style.md)
* C++ - [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)
* PHP - [PSR-12: Extended Coding Style](https://www.php-fig.org/psr/psr-12/)

Ce sont quelques-uns des guides auxquels je me suis référé dans le passé. Il existe d'autres guides également. N'hésitez pas à faire vos propres recherches et à choisir celui que vous préférez. Assurez-vous simplement que le guide que vous suivez est réellement bien considéré par la communauté des développeurs.

## Conclusion

Ce sont les conventions de nommage les plus populaires que vous devriez connaître. Si vous souhaitez en savoir plus sur les différentes conventions de nommage, vous pouvez lire le guide de style pour le langage que vous utilisez.

Connaître les conventions du langage que vous apprenez est important. Bien que le non-respect des conventions ne cassera pas votre code, cela le rendra moins cohérent et plus difficile à utiliser.

Suivre ces simples conventions, en revanche, rendra votre code beaucoup plus lisible et plus facile à utiliser. Alors faites-vous et aux autres une faveur et suivez les conventions.