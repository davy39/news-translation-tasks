---
title: 'Apprendre Scala de 0 à 60 : Les bases'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-16T19:20:45.000Z'
originalURL: https://freecodecamp.org/news/learning-scala-from-0-60-part-i-dc095d274b78
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q0JQttpYtxDBv_BPT_apQg.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: Scala
  slug: scala
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: 'Apprendre Scala de 0 à 60 : Les bases'
seo_desc: 'By Durga Prasana

  Scala is a general purpose, high-level programming language that offers a balance
  between developing functional and object-oriented programs.

  What is functional programming all about? In simple terms, functions are the first-class
  ci...'
---

Par Durga Prasana

Scala est un langage de programmation généraliste et de haut niveau qui offre un équilibre entre le développement de programmes fonctionnels et orientés objet.

En quoi consiste la programmation fonctionnelle ? En termes simples, les fonctions sont les citoyens de première classe en programmation fonctionnelle. Afin d'étendre un ensemble de fonctionnalités principales d'un programme, nous avons tendance à écrire des classes supplémentaires en nous basant sur certaines directives / interfaces. En programmation fonctionnelle, les fonctions nous aident à atteindre le même objectif.

Nous utiliserons [le REPL Scala](https://docs.scala-lang.org/overviews/repl/overview.html) pour toutes les explications. C'est un outil très pratique et informatif pour apprendre Scala. Il enregistre de petits messages mignons sur la façon dont notre code est interprété et exécuté.

Commençons par les bases.

#### **1. Variables**

Nous pouvons définir des variables immuables en utilisant `val` :

```
scala> val name = "King"name: String = King
```

Les variables mutables peuvent être définies et modifiées en utilisant `var` :

```
scala> var name = "King"name: String = King
```

```
scala> name = "Arthur"name: String = Arthur
```

Nous utilisons `def` pour assigner une étiquette à une valeur immuable dont l'évaluation est différée pour une utilisation ultérieure. Cela signifie que la valeur de l'étiquette est évaluée de manière paresseuse à chaque utilisation.

```
scala> var name = "King"name: String = King
```

```
scala> def alias = namealias: String
```

```
scala> aliasres2: String = King
```

Avez-vous observé quelque chose d'intéressant ?

Lors de la définition de `alias`, aucune valeur n'a été assignée à `alias: String` car il est associé de manière paresseuse, lorsque nous l'invoquons. Que se passerait-il si nous changions la valeur de `name` ?

```
scala> aliasres5: String = King
```

```
scala> name = "Arthur, King Arthur"name: String = Arthur, King Arthur
```

```
scala> aliasres6: String = Arthur, King Arthur
```

#### 2. Contrôle de flux

Nous utilisons des instructions de contrôle de flux pour exprimer notre logique de décision.

Vous pouvez écrire une instruction `if-else` comme suit :

```
if(name.contains("Arthur")) {  print("Entombed sword")} else {  print("You're not entitled to this sword")}
```

Ou, vous pouvez utiliser `while` :

```
var attempts = 0while (attempts < 3) {  drawSword()  attempts += 1}
```

#### 3. Collections

Scala distingue explicitement les collections immuables des collections mutables — dès l'espace de noms du package lui-même (`scala.collection.immutable` ou `scala.collection.mutable`).

Contrairement aux collections immuables, les collections mutables peuvent être mises à jour ou étendues en place. Cela nous permet de changer, d'ajouter ou de supprimer des éléments comme effet secondaire.

Mais effectuer des opérations d'ajout, de suppression ou de mise à jour sur des collections immuables retourne une nouvelle collection à la place.

Les collections immuables sont toujours automatiquement importées via `scala._` (qui contient également un alias pour `scala.collection.immutable.List`).

Cependant, pour utiliser des collections mutables, vous devez explicitement importer `scala.collection.mutable.List`.

Dans l'esprit de la programmation fonctionnelle, nous baserons principalement nos exemples sur les aspects immuables du langage, avec de petites incursions dans le côté mutable.

#### **Liste**

Nous pouvons créer une liste de différentes manières :

```
scala> val names = List("Arthur", "Uther", "Mordred", "Vortigern")
```

```
names: List[String] = List(Arthur, Uther, Mordred, Vortigern)
```

Une autre approche pratique consiste à définir une liste en utilisant l'opérateur cons `::`. Cela joint un élément de tête avec le reste de la queue d'une liste.

```
scala> val name = "Arthur" :: "Uther" :: "Mordred" :: "Vortigern" :: Nil
```

```
name: List[String] = List(Arthur, Uther, Mordred, Vortigern)
```

Ce qui est équivalent à :

```
scala> val name = "Arthur" :: ("Uther" :: ("Mordred" :: ("Vortigern" :: Nil)))
```

```
name: List[String] = List(Arthur, Uther, Mordred, Vortigern)
```

Nous pouvons accéder directement aux éléments de la liste par leur index. Rappelez-vous que Scala utilise un indexage basé sur zéro :

```
scala> name(2)
```

```
res7: String = Mordred
```

Certaines méthodes d'aide courantes incluent :

`list.head`, qui retourne le premier élément :

```
scala> name.head
```

```
res8: String = Arthur
```

`list.tail`, qui retourne la queue d'une liste (qui inclut tout sauf la tête) :

```
scala> name.tail
```

```
res9: List[String] = List(Uther, Mordred, Vortigern)
```

#### **Set**

`Set` nous permet de créer un groupe d'entités non répétées. `List` n'élimine pas les doublons par défaut.

```
scala> val nameswithDuplicates = List("Arthur", "Uther", "Mordred", "Vortigern", "Arthur", "Uther")
```

```
nameswithDuplicates: List[String] = List(Arthur, Uther, Mordred, Vortigern, Arthur, Uther)
```

Ici, 'Arthur' est répété deux fois, et il en va de même pour 'Uther'.

Créons un Set avec les mêmes noms. Remarquez comment il exclut les doublons.

```
scala> val uniqueNames = Set("Arthur", "Uther", "Mordred", "Vortigern", "Arthur", "Uther")
```

```
uniqueNames: scala.collection.immutable.Set[String] = Set(Arthur, Uther, Mordred, Vortigern)
```

Nous pouvons vérifier l'existence d'un élément spécifique dans Set en utilisant `contains()` :

```
scala> uniqueNames.contains("Vortigern")res0: Boolean = true
```

Nous pouvons ajouter des éléments à un Set en utilisant la méthode + (qui prend des `varargs`, c'est-à-dire des arguments de longueur variable)

```
scala> uniqueNames + ("Igraine", "Elsa", "Guenevere")res0: scala.collection.immutable.Set[String] = Set(Arthur, Elsa, Vortigern, Guenevere, Mordred, Igraine, Uther)
```

De même, nous pouvons supprimer des éléments en utilisant la méthode `-`

```
scala> uniqueNames - "Elsa"
```

```
res1: scala.collection.immutable.Set[String] = Set(Arthur, Uther, Mordred, Vortigern)
```

#### **Map**

`Map` est une collection itérable qui contient des mappages d'éléments `key` vers des éléments `value` respectifs, qui peuvent être créés comme suit :

```
scala> val kingSpouses = Map( | "King Uther" -> "Igraine", | "Vortigern" -> "Elsa", | "King Arthur" -> "Guenevere" | )
```

```
kingSpouses: scala.collection.immutable.Map[String,String] = Map(King Uther -> Igraine, Vortigern -> Elsa, King Arthur -> Guenevere)
```

Les valeurs pour une clé spécifique dans la map peuvent être accessibles comme suit :

```
scala> kingSpouses("Vortigern")res0: String = Elsa
```

Nous pouvons ajouter une entrée à Map en utilisant la méthode `+` :

```
scala> kingSpouses + ("Launcelot" -> "Elaine")res0: scala.collection.immutable.Map[String,String] = Map(King Uther -> Igraine, Vortigern -> Elsa, King Arthur -> Guenevere, Launcelot -> Elaine)
```

Pour modifier un mappage existant, nous réajoutons simplement la clé-valeur mise à jour :

```
scala> kingSpouses + ("Launcelot" -> "Guenevere")res1: scala.collection.immutable.Map[String,String] = Map(King Uther -> Igraine, Vortigern -> Elsa, King Arthur -> Guenevere, Launcelot -> Guenevere)
```

Notez que puisque la collection est immuable, chaque opération d'édition retourne une nouvelle collection (`res0`, `res1`) avec les modifications appliquées. La collection originale `kingSpouses` reste inchangée.

#### 4. Combinateurs fonctionnels

Maintenant que nous avons appris à regrouper un ensemble d'entités, voyons comment nous pouvons utiliser des combinateurs fonctionnels pour générer des transformations significatives sur de telles collections.

Selon les mots simples de John Hughes :

> Un combinateur est une fonction qui construit des fragments de programme à partir de fragments de programme.

Un examen approfondi du fonctionnement des combinateurs dépasse le cadre de cet article. Mais nous essayerons tout de même de toucher à une compréhension de haut niveau du concept.

Prenons un exemple.

Supposons que nous voulons trouver les noms de toutes les reines en utilisant la collection map `kingSpouses` que nous avons créée.

Nous voudrions faire quelque chose comme examiner chaque entrée dans la map. Si la `key` contient le nom d'un roi, alors nous nous intéressons au nom de son épouse (c'est-à-dire la reine).

Nous utiliserons le combinateur `filter` sur la map, qui a une signature comme :

```
collection.filter( /* une méthode de condition de filtre qui retourne vrai sur les entrées de map correspondantes */)
```

Globalement, nous effectuerons les étapes suivantes pour trouver les reines :

* Trouver les paires (key, value) avec les noms des rois comme clés.
* Extraire les valeurs (noms des reines) uniquement pour ces tuples.

Le `filter` est une fonction qui, lorsqu'on lui donne une paire (key, value), retourne vrai / faux.

1. Trouver les entrées de map concernant les rois.

Définissons notre fonction prédicat de filtrage. Puisque `key_value` est un tuple de (key, value), nous extrayons la clé en utilisant `._1` (et devinez ce que `._2` retourne ?)

```
scala> def isKingly(key_value: (String, String)): Boolean = key_value._1.toLowerCase.contains("king")
```

```
isKingly: (key_value: (String, String))Boolean
```

Maintenant, nous utiliserons la fonction de filtrage définie ci-dessus pour `filter` les entrées royales.

```
scala> val kingsAndQueens = kingSpouses.filter(isKingly)
```

```
kingsAndQueens: scala.collection.immutable.Map[String,String] = Map(King Uther -> Igraine, King Arthur -> Guenevere)
```

2. Extraire les noms des reines respectives à partir des tuples filtrés.

```
scala> kingsAndQueens.values
```

```
res10: Iterable[String] = MapLike.DefaultValuesIterable(Igraine, Guenevere)
```

Affichons les noms des reines en utilisant le combinateur `foreach` :

```
scala> kingsAndQueens.values.foreach(println)IgraineGuenevere
```

D'autres combinateurs utiles sont `foreach`, `filter`, `zip`, `partition`, `find`.

Nous reverrons certains de ces éléments après avoir appris à définir des fonctions et à passer des fonctions comme arguments à d'autres fonctions dans les fonctions d'ordre supérieur.

Faisons un récapitulatif de ce que nous avons appris :

* Différentes façons de définir des variables
* Diverses instructions de contrôle de flux
* Quelques bases sur diverses collections
* Aperçu de l'utilisation des combinateurs fonctionnels sur les collections

J'espère que vous avez trouvé cet article utile. Il s'agit du premier d'une série d'articles à suivre sur l'apprentissage de Scala.

Dans la deuxième partie, nous apprendrons à définir des classes, des traits, l'encapsulation et d'autres concepts orientés objet.

N'hésitez pas à me faire part de vos commentaires et suggestions sur la façon dont je peux améliorer le contenu. En attendant, ❤️ codez bien.