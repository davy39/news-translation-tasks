---
title: 'Une bibliothèque de streaming avec un superpouvoir : FS2 et la programmation
  fonctionnelle'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-19T21:20:26.000Z'
originalURL: https://freecodecamp.org/news/a-streaming-library-with-a-superpower-fs2-and-functional-programming-6f602079f70a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Mi3HukEz9_JHfv3Z5lp93g.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: General Programming
  slug: programming
- name: Scala
  slug: scala
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Une bibliothèque de streaming avec un superpouvoir : FS2 et la programmation
  fonctionnelle'
seo_desc: 'By Daniel Sebban

  Scala has a very special streaming library called FS2 (Functional Streams for Scala).
  This library embodies all the advantages of functional programming (FP). By understanding
  its design goals you will get exposure to the core ideas ...'
---

Par Daniel Sebban

Scala possède une bibliothèque de streaming très spéciale appelée FS2 (Functional Streams for Scala). Cette bibliothèque incarne tous les avantages de la programmation fonctionnelle (FP). En comprenant ses objectifs de conception, vous serez exposé aux idées fondamentales qui rendent la FP si attrayante.

FS2 a un type central : `**Stream[Effect,Output]**`

Vous pourriez déduire de ce type qu'il s'agit d'un `Stream` et qu'il émet des valeurs de type `Output`.

La question évidente ici est : qu'est-ce que `Effect` ? Quel est le lien entre `Effect` et `Output` ? Et quels sont les avantages de FS2 par rapport aux autres bibliothèques de streaming ?

### Aperçu

Je commencerai par passer en revue les problèmes que FS2 résout. Ensuite, je comparerai `List` et `Stream` avec plusieurs exemples de code. Après cela, je me concentrerai sur la façon d'utiliser `Stream` avec une base de données ou toute autre opération d'entrée/sortie. C'est là que FS2 brille et où le type `Effect` est utilisé. Une fois que vous comprendrez ce qu'est `Effect`, les avantages de la programmation fonctionnelle devraient vous apparaître clairement.

À la fin de cet article, vous obtiendrez les réponses aux questions suivantes :

* Quels problèmes puis-je résoudre avec FS2 ?
* Que puis-je faire avec `Stream` que `List` ne peut pas faire ?
* Comment puis-je alimenter `Stream` avec des données provenant d'une API, d'un fichier ou d'une base de données ?
* Qu'est-ce que ce type `Effect` et comment est-il lié à la programmation fonctionnelle ?

Note : Le code est en Scala et devrait être compréhensible même sans connaissance préalable de la syntaxe.

### Quels problèmes puis-je résoudre avec FS2 ?

1. Streaming I/O : Chargement incrémental de grands ensembles de données qui ne tiennent pas en mémoire et opération sur ceux-ci sans saturer votre heap.
2. Contrôle de flux (non couvert) : Déplacement de données d'une ou plusieurs bases de données, fichiers ou API vers d'autres de manière déclarative.
3. Concurrence (non couverte) : Exécution de différents streams en parallèle et communication entre eux. Par exemple, chargement de données à partir de plusieurs fichiers et traitement concurrent au lieu de séquentiel. Vous pouvez faire des choses avancées ici. Les streams peuvent communiquer ensemble **pendant** la phase de traitement et pas seulement à la fin.

### `List` vs `Stream`

`List` est la structure de données la plus connue et utilisée. Pour comprendre comment elle diffère d'un `Stream` FS2, nous allons passer par quelques cas d'utilisation. Nous verrons comment `Stream` peut résoudre des problèmes que `List` ne peut pas.

### Vos données sont trop volumineuses et ne tiennent pas en mémoire

Supposons que vous avez un très gros fichier (40 Go) `fahrenheit.txt`. Le fichier contient une température sur chaque ligne et vous souhaitez le convertir en `celsius.txt`.

### Chargement d'un gros fichier en utilisant `List`

```scala
import scala.io.Source
val list = Source.fromFile("testdata/fahrenheit.txt").getLines.toList
java.lang.OutOfMemoryError: Java heap space
  java.util.Arrays.copyOfRange(Arrays.java:3664)
  java.lang.String.<init>(String.java:207)
  java.io.BufferedReader.readLine(BufferedReader.java:356)
  java.io.BufferedReader.readLine(BufferedReader.java:389)
```

`List` échoue lamentablement car, bien sûr, le fichier est trop gros pour tenir en mémoire. Si vous êtes curieux, vous pouvez consulter la solution complète utilisant `Stream` [ici](https://functional-streams-for-scala.github.io/fs2/#about) — mais faites-le plus tard, continuez à lire :)

### Quand List ne suffit pas... Stream à la rescousse !

Supposons que j'ai réussi à lire mon fichier et que je veux l'écrire à nouveau. Je souhaite préserver la structure des lignes. J'ai besoin d'insérer un caractère de nouvelle ligne `\n` après chaque température.

Je peux utiliser le combinateur `intersperse` pour faire cela

```scala
import fs2._
Stream(1,2,3,4).intersperse("\n").toList
```

Un autre exemple intéressant est `zipWithNext`

```scala
scala> Stream(1,2,3,4).zipWithNext.toList
res1: List[(Int, Option[Int])] = List((1,Some(2)), (2,Some(3)), (3,Some(4)), (4,None))
```

Il regroupe les éléments consécutifs ensemble, très utile si vous voulez [supprimer les doublons consécutifs](https://gist.github.com/dsebban/bb34ea4671bda8d52e2f083e2b160778).

Ce ne sont que quelques exemples parmi une longue liste de combinateurs très utiles, voici la [liste complète](https://oss.sonatype.org/service/local/repositories/releases/archive/co/fs2/fs2-core_2.12/0.10.5/fs2-core_2.12-0.10.5-javadoc.jar/!/fs2/Stream.html).

Évidemment, `Stream` peut faire beaucoup de choses que `List` ne peut pas, mais la meilleure fonctionnalité arrive dans la section suivante, il s'agit de l'utilisation de `Stream` dans le monde réel avec des bases de données, des fichiers, des API...

### Comment puis-je alimenter `Stream` avec des données provenant d'une API, d'un fichier ou d'une base de données ?

Disons simplement pour l'instant que voici notre programme

```scala
scala> Stream(1,2,3)
res2: fs2.Stream[fs2.Pure,Int] = Stream(..)
```

Que signifie ce `Pure` ? Voici la scaladoc du code source :

```scala
/**
    * Indique qu'un stream n'évalue aucun effet.
    *
    * Un `Stream[Pure,O]` peut être converti en toute sécurité en un `Stream[F,O]` pour tous les `F`.
*/
type Pure[A] <: Nothing
```

Cela signifie aucun effet, d'accord..., mais **qu'est-ce qu'un effet ?** et plus spécifiquement, quel est l'effet de notre programme `Stream(1,2,3)` ?

Ce programme n'a littéralement aucun _effet_ sur le monde. Son seul effet sera de faire fonctionner votre CPU et de consommer de l'énergie !! Il n'affecte pas le monde qui vous entoure.

Par affecter le monde, j'entends qu'il **consomme** une ressource significative comme un fichier, une base de données, ou qu'il **produit** quelque chose comme un fichier, télécharge des données quelque part, écrit dans votre terminal, etc.

### Comment transformer un stream `Pure` en quelque chose d'utile ?

Supposons que je veux charger des identifiants d'utilisateurs depuis une base de données, on me donne cette fonction, elle effectue un appel à la base de données et retourne l'identifiant utilisateur sous forme de `Long`.

```scala
import scala.concurrent.Future
def loadUserIdByName(userName: String): Future[Long] = ???
```

Elle retourne un `[Future](https://www.scala-lang.org/api/2.12.3/scala/concurrent/Future.html)` qui indique que cet appel est asynchrone et que la valeur sera disponible à un moment donné dans le futur. Il encapsule la valeur retournée par la base de données.

J'ai ce stream `Pure`.

```scala
scala> val names = Stream("bob", "alice", "joe")
names: fs2.Stream[fs2.Pure,String] = Stream(..)
```

Comment obtenir un `Stream` d'identifiants ?

L'approche naïve serait d'utiliser la fonction `map`, elle devrait exécuter la fonction pour chaque valeur dans le `Stream`.

```scala
scala> userIdsFromDB.compile
res5: fs2.Stream.ToEffect[scala.concurrent.Future,Long] = fs2.Stream$ToEffect@fc0f18da
```

J'ai toujours un `Pure` ! J'ai donné au `Stream` une fonction qui _affecte le monde_ et j'ai toujours un `Pure`, ce n'est pas cool... Cela aurait été bien si FS2 avait détecté automatiquement que la fonction `loadUserIdByName` a un _effet_ sur le monde et m'avait retourné quelque chose qui n'est pas `Pure`, mais cela ne fonctionne pas comme ça. Vous devez utiliser un combinateur spécial au lieu de `map` : vous devez utiliser `evalMap`.

```scala
scala> userIdsFromDB.toList
<console>:18: error: value toList is not a member of fs2.Stream[scala.concurrent.Future,Long]
       userIdsFromDB.toList
                     ^
```

Plus de `Pure` ! nous avons `Future` à la place, youpi ! Que s'est-il passé ?

Il a pris :

* `loadUserIdByName: Future[Long]`
* `Stream[Pure, String]`

Et a changé les types du stream en

* `Stream[Future, Long]`

Il a séparé le `Future` et l'a isolé ! Le côté gauche qui était le paramètre de type `Effect` est maintenant le type concret `Future`.

Astuce ingénieuse, mais comment cela m'aide-t-il ?

Vous venez d'assister à une véritable **séparation des préoccupations**. Vous pouvez continuer à opérer sur le stream avec tous les combinateurs sympas de type `List` et vous n'avez pas à vous soucier si la base de données est hors ligne, lente ou de toutes les choses liées aux préoccupations du réseau (effet).

Tout fonctionne jusqu'à ce que je veuille utiliser `toList` pour récupérer les valeurs

```scala
scala> userIdsFromDB.toList
<console>:18: error: value toList is not a member of fs2.Stream[scala.concurrent.Future,Long]
       userIdsFromDB.toList
                     ^
```

Quoi ???!!! Je pourrais jurer que j'ai utilisé `toList` avant et que cela fonctionnait, comment peut-il dire que `toList` n'est plus un membre de `fs2.Stream[Future,String]` ? C'est comme si cette fonction avait été supprimée au moment où j'ai commencé à utiliser un stream avec effet, c'est impressionnant ! Mais comment récupérer mes valeurs ?

```scala
scala> userIdsFromDB.compile
res5: fs2.Stream.ToEffect[scala.concurrent.Future,Long] = fs2.Stream$ToEffect@fc0f18da
```

Tout d'abord, nous utilisons `compile` pour dire au `Stream` de combiner tous les effets en un seul, ce qui revient à regrouper tous les appels à `loadUserIdByName` en un seul grand `Future`. Cela est nécessaire pour le framework, et il deviendra apparent pourquoi cette étape est nécessaire bientôt.

Maintenant, `toList` devrait fonctionner

```scala
scala> userIdsFromDB.compile.toList
<console>:18: error: could not find implicit value for parameter F: cats.effect.Sync[scala.concurrent.Future]
       userIdsFromDB.compile.toList
                             ^
```

Quoi ?! le compilateur se plaint encore. C'est parce que `Future` n'est pas un bon type `Effect` — il brise la philosophie de la séparation des préoccupations comme expliqué dans la section suivante très importante.

### IMPORTANT : La seule chose à retenir de cet article

Un point clé ici est que la base de données n'a pas été appelée à ce stade. Rien ne s'est vraiment passé, le programme complet ne produit rien.

```scala
def loadUserIdByName(userName: String): Future[Long] = ???
Stream("bob", "alice", "joe").evalMap(loadUserIdByName).compile
```

### Séparer la description du programme de son évaluation

Oui, cela peut être surprenant, mais le thème principal de la FP est de séparer

* **La description** de votre programme : un bon exemple est le programme que nous venons d'écrire, c'est une description pure du problème « Je vous donne des noms et une base de données, donnez-moi des identifiants »

Et

* **L'exécution** de votre programme : exécuter le code réel et lui demander d'aller dans la base de données

Une fois de plus, notre programme n'a littéralement aucun _effet_ sur le monde, à part faire chauffer votre ordinateur, exactement comme notre stream `Pure`.

Le code qui n'a pas d'effet est appelé **pur** et c'est de cela que traite toute la programmation fonctionnelle : écrire des programmes avec des fonctions qui sont **pures**. Bravo, vous savez maintenant ce qu'est la FP.

Pourquoi voudriez-vous écrire du code de cette manière ? Simple : pour atteindre la séparation des préoccupations entre les parties IO et le reste de notre code.

Maintenant, corrigeons notre programme et occupons-nous de ce problème de `Future`.

Comme nous l'avons dit, `Future` est un mauvais type `Effect`, il va à l'encontre du principe de séparation des préoccupations. En effet, `Future` est eager en Scala : au moment où vous en créez un, il commence à s'exécuter sur un thread, vous n'avez pas le contrôle de l'exécution et cela brise donc le principe. FS2 en est bien conscient et ne vous laisse pas compiler. Pour corriger cela, nous devons utiliser un type appelé `IO` qui encapsule notre mauvais `Future`.

Cela nous amène à la dernière partie, qu'est-ce que ce type `IO` ? et comment puis-je enfin récupérer ma liste de `usedIds` ?

```scala
scala> import cats.effect.IO
import cats.effect.IO
scala> Stream("bob", "alice", "joe").evalMap(name => IO.fromFuture(IO(loadUserIdByName(name)))).compile.toList
res8: cats.effect.IO[List[Long]] = IO$2104439279
```

Il nous retourne maintenant une `List`, mais nous n'avons toujours pas récupéré nos identifiants, donc une dernière chose doit manquer.

![Image](https://cdn-media-1.freecodecamp.org/images/ivbIHjwyNlEmckvLT6thLcPRcVRUkRGgw-dH)

### Que signifie vraiment `IO` ?

`IO` provient de la bibliothèque [cats-effect](https://typelevel.org/cats-effect/datatypes/io.html). Terminez d'abord notre programme et récupérons enfin les identifiants de la base de données.

```scala
scala> userIds.compile.toList.unsafeRunSync
<console>:18: error: not found: value userIds
       userIds.compile.toList.unsafeRunSync
       ^
```

La preuve qu'il fait quelque chose est le fait qu'il échoue.

```
loadUserIdByName(userName: String): Future[Long] = ???
```

Lorsque `???` est appelé, vous obtiendrez cette exception, cela signifie que la fonction a été exécutée (par opposition à avant où nous avons fait le point que rien ne se passait vraiment). Lorsque nous implémentons cette fonction, elle ira dans la base de données et chargera les identifiants, et elle aura un **effet** sur le monde (réseau/système de fichiers).

`IO[Long]` est une **description** de **comment** obtenir une valeur de type `Long` et cela implique très certainement de faire de l'I/O, c'est-à-dire aller sur le réseau, charger un fichier, etc.

C'est le **Comment** et non le **Quoi**. Il décrit comment obtenir la valeur du réseau. Si vous voulez exécuter cette description, vous pouvez utiliser `unsafeRunSync` (ou d'autres fonctions préfixées `unsafe`). Vous pouvez deviner pourquoi elles sont appelées ainsi : en effet, un appel à une base de données est intrinsèquement non sécurisé car il pourrait échouer si, par exemple, votre connexion Internet est coupée.

### Récapitulatif

Jetons un dernier coup d'œil à `**Stream[Effect,Output]**`**.**

`Output` est le type que le stream émet (peut être un stream de `String`, `Long` ou tout autre type que vous avez défini).

`Effect` est la manière (la recette) de produire le `Output` (c'est-à-dire aller dans la base de données et me donner un `id` de type `Long`).

Il est important de comprendre que si ces types sont séparés pour faciliter les choses, décomposer un problème en sous-problèmes vous permet de raisonner sur les sous-problèmes indépendamment. Vous pouvez ensuite les résoudre et combiner leurs solutions.

Le lien entre ces 2 types est le suivant :

Pour que le `Stream` émet un élément de type

* `Output`

Il doit évaluer un type

* `Effect`

Un type spécial qui encode une action effective en tant que valeur de type `IO`, cette valeur `IO` permet la séparation de 2 préoccupations :

* **Description** : `IO` est une valeur immutable simple, c'est une recette pour obtenir un type `A` en faisant un certain type d'IO (réseau/système de fichiers/...)
* **Exécution** : pour que `IO` fasse quelque chose, vous devez l'_exécuter/lancer_ en utilisant `io.unsafeRunSync`

#### Mettre tout ensemble

`Stream[IO,Long]` dit :

Ceci est un `Stream` qui émet des valeurs de type `Long` et pour ce faire, il doit exécuter une fonction _effective_ qui produit `IO[Long]` pour chaque valeur.

C'est beaucoup de détails dans ce type très court. Plus vous obtenez de détails sur la façon dont les choses se passent, moins vous faites d'erreurs.

### Points clés

* `Stream` est une version **super chargée** de `List`
* `Stream(1,2,3)` est de type `Stream[Pure, Int]`, le deuxième type `Int` est le type de toutes les valeurs que ce stream émettra
* `Pure` signifie aucun _effet_ sur le monde. Il fait simplement fonctionner votre CPU et consomme de l'énergie, mais à part cela, il n'affecte pas le monde qui vous entoure.
* Utilisez `evalMap` au lieu de `map` lorsque vous voulez appliquer une fonction qui a un effet comme `loadUserIdByName` à un `Stream`.
* `Stream[IO, Long]` sépare les préoccupations du Quoi et du Comment en vous permettant de travailler uniquement avec les valeurs et sans vous soucier de la manière de les obtenir (chargement depuis la base de données).
* Séparer la description du programme de son évaluation est un aspect clé de la FP.
* Tous les programmes que vous écrivez avec `Stream` ne feront rien jusqu'à ce que vous utilisiez `unsafeRunSync`. Avant cela, votre code est effectivement _pur_.
* `IO[Long]` est un type d'effet qui vous indique : vous obtiendrez des valeurs `Long` à partir d'IO (peut être un fichier, le réseau, la console...). C'est une description et non un wrapper !
* `Future` ne respecte pas cette philosophie et n'est donc pas compatible avec FS2, vous devez utiliser le type `IO` à la place.

### Vidéos sur FS2

* Screencast pratique par Michael Pilquist : [https://www.youtube.com/watch?v=B1wb4fIdtn4](https://www.youtube.com/watch?v=B1wb4fIdtn4)
* Conférence par Fabio Labella [https://www.youtube.com/watch?v=x3GLwl1FxcA](https://www.youtube.com/watch?v=x3GLwl1FxcA)