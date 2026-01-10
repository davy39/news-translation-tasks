---
title: 'Une introduction aux types génériques en Java : covariance et contravariance'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-21T04:00:37.000Z'
originalURL: https://freecodecamp.org/news/understanding-java-generic-types-covariance-and-contravariance-88f4c19763d2
coverImage: https://cdn-media-1.freecodecamp.org/images/0*h03xxe8xFKcFv262.jpg
tags:
- name: generics
  slug: generics
- name: Java
  slug: java
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Une introduction aux types génériques en Java : covariance et contravariance'
seo_desc: 'By Fabian Terh

  Types

  Java is a statically typed language, which means you must first declare a variable
  and its type before using it.

  For example: int myInteger = 42;

  Enter generic types.

  Generic types

  Definition: “A generic type is a generic class o...'
---

Par Fabian Terh

### Types

Java est un langage à typage statique, ce qui signifie que vous devez d'abord déclarer une variable et son type avant de l'utiliser.

Par exemple : `int myInteger = 42;`

Voici les types génériques.

#### Types génériques

[Définition](https://docs.oracle.com/javase/tutorial/java/generics/types.html) : « Un _type générique_ est une classe ou une interface générique qui est paramétrée sur des types. »

Essentiellement, les types génériques vous permettent d'écrire une classe générale et générique (ou méthode) qui fonctionne avec différents types, permettant la réutilisation du code.

Plutôt que de spécifier que `obj` est de type `int`, ou de type `String`, ou de tout autre type, vous définissez la classe `Box` pour accepter un paramètre de type `<T>`. Ensuite, vous pouvez utiliser T pour représenter ce type générique dans n'importe quelle partie de votre classe.

Maintenant, voici la covariance et la contravariance.

### Covariance et contravariance

#### Définition

La variance fait référence à la manière dont le sous-typage entre des types plus complexes est lié au sous-typage entre leurs composants ([source](https://en.wikipedia.org/wiki/Covariance_and_contravariance_(computer_science))).

Une définition facile à retenir (et extrêmement informelle) de la covariance et de la contravariance est :

* Covariance : accepter les sous-types
* Contravariance : accepter les supertypes

#### Tableaux

En Java, **les tableaux sont covariants**, ce qui a 2 implications.

Premièrement, un tableau de type `T[]` peut contenir des éléments de type `T` et ses sous-types.

```
Number[] nums = new Number[5];nums[0] = new Integer(1); // Oknums[1] = new Double(2.0); // Ok
```

Deuxièmement, un tableau de type `S[]` est un sous-type de `T[]` si `S` est un sous-type de `T`.

```
Integer[] intArr = new Integer[5];Number[] numArr = intArr; // Ok
```

Cependant, il est important de se rappeler que : (1) `numArr` est une référence de type de référence `Number[]` à l'objet « réel » `intArr` de type « réel » `Integer[]`.

Par conséquent, la ligne suivante se compilera sans problème, mais produira une exception `ArrayStoreException` à l'exécution (en raison de la pollution de la mémoire) :

```
numArr[0] = 1.23; // Pas ok
```

Elle produit une exception à l'exécution, car Java sait à l'exécution que l'objet « réel » `intArr` est en fait un tableau de `Integer`.

#### Génériques

Avec les types génériques, Java n'a aucun moyen de connaître à l'exécution les informations de type des paramètres de type, en raison de l'effacement de type. Par conséquent, il ne peut pas protéger contre la pollution de la mémoire à l'exécution.

**Ainsi, les génériques sont invariants.**

```
ArrayList<Integer> intArrList = new ArrayList<>();ArrayList<Number> numArrList = intArrList; // Pas okArrayList<Integer> anotherIntArrList = intArrList; // Ok
```

Les paramètres de type doivent correspondre exactement, pour protéger contre la pollution de la mémoire.

Mais voici les caractères génériques.

#### Caractères génériques, covariance et contravariance

Avec les caractères génériques, il est possible pour les génériques de supporter la covariance et la contravariance.

En modifiant l'exemple précédent, nous obtenons ceci, qui fonctionne !

```
ArrayList<Integer> intArrList = new ArrayList<>();ArrayList<? super Integer> numArrList = intArrList; // Ok
```

Le point d'interrogation « ? » fait référence à un caractère générique qui représente un type inconnu. Il peut être borné inférieurement, ce qui restreint le type inconnu à être un type spécifique ou son supertype.

Par conséquent, dans la ligne 2, `? super Integer` se traduit par « n'importe quel type qui est un type Integer ou son supertype ».

Vous pourriez également borner supérieurement le caractère générique, ce qui restreint le type inconnu à être un type spécifique ou son sous-type, en utilisant `? extends Integer`.

#### Lecture seule et écriture seule

La covariance et la contravariance produisent des résultats intéressants. **Les types covariants sont en lecture seule, tandis que les types contravariants sont en écriture seule.**

Rappelez-vous que les types covariants acceptent les sous-types, donc `ArrayList<? extends Number>` peut contenir n'importe quel objet qui est soit `d'un` type Number ou de son sous-type.

Dans cet exemple, la ligne 9 fonctionne, car nous pouvons être certains que tout ce que nous obtenons de l'ArrayList peut être converti en un type `Number` (parce que s'il étend `Number`, par définition, c'est un `Number`).

Mais `nums.add()` ne fonctionne pas, car nous ne pouvons pas être sûrs du « type réel » de l'objet. Tout ce que nous savons, c'est qu'il doit être un `Number` ou ses sous-types (par exemple, Integer, Double, Long, etc.).

Avec la contravariance, l'inverse est vrai.

La ligne 9 fonctionne, car nous pouvons être certains que, quel que soit le « type réel » de l'objet, il doit être `Integer` ou son supertype, et ainsi accepter un objet `Integer`.

Mais la ligne 10 ne fonctionne pas, car nous ne pouvons pas être sûrs que nous obtiendrons un `Integer`. Par exemple, `nums` pourrait référencer un ArrayList d'`Objects`.

#### Applications

Par conséquent, puisque les types covariants sont en lecture seule et les types contravariants sont en écriture seule (en termes généraux), nous pouvons déduire la règle suivante : **« Producteur étend, consommateur super »**.

Un objet de type producteur qui produit des objets de type `T` peut être de paramètre de type `<? extends T>`, tandis qu'un objet de type consommateur qui consomme des objets de type T peut être de paramètre de type `<? super T>`.