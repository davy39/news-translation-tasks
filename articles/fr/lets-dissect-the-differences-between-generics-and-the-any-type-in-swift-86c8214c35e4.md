---
title: Analysons les différences entre les génériques et le type Any en Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-09T23:30:10.000Z'
originalURL: https://freecodecamp.org/news/lets-dissect-the-differences-between-generics-and-the-any-type-in-swift-86c8214c35e4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HHsbUAAWhF6WcopEr39yuw.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: Analysons les différences entre les génériques et le type Any en Swift
seo_desc: 'By Boudhayan Biswas

  Swift is one of the topmost type-safe languages nowadays. ???

  Ohhh wait!! What does it mean if a language is type-safe? ?

  A type-safe language always ensures that an operation works with the right kind
  of data available at that po...'
---

Par Boudhayan Biswas

Swift est l'un des langages les plus sûrs en termes de typage de nos jours. ???

#### **_Ohhh attendez !! Que signifie le fait qu'un langage soit sûr en termes de typage ? ?_**

Un langage sûr en termes de typage garantit toujours qu'une opération fonctionne avec le bon type de données disponible à ce moment-là. ✅

Si un langage a la capacité de déclarer différents types de données (par exemple, Int, Float, String, Array, Dictionary) et qu'il a également la capacité de garantir qu'une variable déclarée avec un type de données particulier ne contiendra jamais un autre type de données, alors il est appelé un langage sûr en termes de typage.

Dans les langages sûrs en termes de typage, la vérification des types est toujours effectuée. Cela peut se produire à la compilation ou à l'exécution, selon le langage. ✅

#### **_Maintenant, que sont les génériques en Swift ??_**

Les génériques sont sûrs en termes de typage et nous aident à écrire des fonctions et des types flexibles et réutilisables. En utilisant les génériques, nous pouvons écrire du code qui fonctionne pour tous les types de données. Puisque Swift est un langage sûr en termes de typage, sans rompre cette caractéristique, nous sommes capables d'écrire des codes génériques qui peuvent éviter la duplication de code.

Prenons un exemple simple : un Array est une collection ordonnée qui peut contenir le même type de données. C'est pourquoi dans la définition d'un Array, nous pouvons voir qu'il prend un type générique d'**Element**. Ainsi, un Array devient un **type générique de Collection**.

**_D'accord. Cool. Alors, qu'est-ce que le type Any en Swift ?_** ???

Swift supporte également le type Any. Comme son nom l'indique, il peut représenter une instance de n'importe quel type comme une structure, une classe, une énumération et un type de fonction.

#### **_Alors, les types id d'Objective C et Any de Swift sont-ils les mêmes ?_** ?

Dans Swift 3, le type _id_ d'Objective C est mappé au type Any de Swift. Cela améliore la compatibilité entre Swift et Objective C.

#### **_Mais comment et pourquoi ??_**

Dans Swift 2, le type _id_ d'Objective C était mappé à l'objet Any de Swift. Cela fonctionnait bien pour la plupart des cas, mais parfois cela résultait en un comportement inattendu. L'un des concepts clés de Swift est les Value Types, et ce mappage ne rendait pas justice à ce concept.

Swift est juste un nouveau langage pour le développement iOS, et Objective C existe depuis des années. Donc, bien sûr, la plupart des projets ont été développés en Objective C uniquement. Maintenant, afin de convertir un projet Objective C en un projet Swift, l'exigence est venue qu'il devrait être possible de faire le pont entre n'importe quel type Swift et n'importe quel objet Objective C.

Mais cela n'était pas un problème pour les classes Swift et les types de valeur Swift comme Int, String, Float car ils ont déjà leurs homologues Objective C. Le problème est survenu pour les types de valeur Swift qui n'avaient pas d'homologues Objective C.

Donc, pour corriger cela, le type _id_ d'Objective C a été mappé au type Any de Swift. ✅✅✅

**Assez de définitions ?. Venons-en maintenant au sujet principal. D'après les points ci-dessus, il semble que les génériques et le type Any soient les mêmes. Mais le sont-ils vraiment ???**

**À un niveau élevé, Any peut sembler similaire aux génériques. Mais essayons de trouver quelques différences-???**

**Nous savons tous ce qu'est une **Stack** en structures de données, n'est-ce pas ? Une stack est une structure de données linéaire de base où l'insertion et la suppression d'éléments se font à une seule extrémité.**

**Maintenant, nous allons implémenter la structure Stack en Swift. D'abord, nous allons l'implémenter en utilisant les génériques, puis avec le type Any.**

#### **Implémentation de Stack en utilisant les génériques :**

**L'implémentation de Stack ci-dessus utilise les génériques. La structure prend un type générique d'élément **Element** et implémente une stack en utilisant cet élément. Maintenant, faisons quelques opérations avec la Stack générique :**

**Elle déclare une Stack générique qui peut contenir un élément de type Integer. Nous poussons l'élément entier dans la stack. Jusqu'à ce point, tout fonctionne bien.**

**Mais que se passe-t-il si je veux pousser un élément float sur cette genericStack ?**

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ir_5WJ9UvNMUqRlGihdgoA.png)

**❌❌ Oups ! Erreur de compilation ! ❌❌**

#### **Implémentation de Stack en utilisant le type Any :**

**Dans cette implémentation de Stack, le tableau items peut contenir n'importe quel type d'élément. Nous ne spécifions pas quel sera le type de données exact de l'élément du tableau _items_ dans la définition. Maintenant, faisons les mêmes opérations de base sur cette stack :**

**Pas de problèmes, n'est-ce pas ? Tout fonctionne bien ici aussi. Initialement, nous avons déclaré une stack et poussé deux éléments entiers dedans. Lorsque nous appelons la méthode _show()_, elle imprime le tableau exact _[3, 4]._**

**Maintenant, poussons une valeur float dedans. ☀️**

![Image](https://cdn-media-1.freecodecamp.org/images/1*07nwXABEbmgViY7OXJC60Q.png)

**✅✅ Pas d'erreur ! Tout fonctionne bien ! ✅✅**

#### **_Alors, que se passe-t-il derrière les scènes ? Pourquoi ne recevons-nous aucune erreur ???_** ?

**Les génériques disent essentiellement au compilateur :**

> **J'ai déclaré un type générique et je vais vous donner un type exact plus tard. Je veux que vous appliquiez ce type partout où je le spécifie.**

**Le type Any dit essentiellement au compilateur :**

> **Ne vous inquiétez pas pour cette variable, pas besoin d'appliquer un type ici, laissez-moi faire ce que je veux faire.**

**Les génériques peuvent être utilisés pour définir des fonctions flexibles, mais les types d'arguments sont toujours vérifiés par le compilateur. Le type Any peut être utilisé pour contourner le système de typage de Swift. ?**

**Dans la déclaration de la stack générique**, nous disons au compilateur que la stack doit prendre uniquement le type entier. Ensuite, lorsque nous essayons d'insérer un élément de type float dedans, cela signifie que nous rompons cette promesse. Par conséquent, cela génère une erreur de compilation. Il s'attend toujours à ce que l'élément soit de type entier.

**Mais pour la stack Any**, nous ne recevons aucune erreur de compilation ou d'exécution. Même si nous appelons la méthode _show()_, elle imprime la stack comme _[3, 4, 5.0]_ ce qui signifie que la stack contient des valeurs de type entier et float. Donc dans une stack Any, il n'y a pas de restriction de type, nous pouvons pousser n'importe quel type de valeur dedans (mais il y a des possibilités d'exceptions à l'exécution).

### **Conclusion**

**Donc, si nous utilisons les génériques, nous pouvons écrire des fonctions, des structures, des classes et des protocoles flexibles sans compromettre la sécurité des types de Swift. Mais si nous utilisons le type Any, alors nous sommes un peu notre propre patron, nous pouvons faire presque tout ce que nous voulons.**

**_??? Santé !!! Merci d'avoir lu !! ???_