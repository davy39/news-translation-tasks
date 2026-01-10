---
title: Comment écrire des fonctions composables et des programmes corrects
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-02T11:52:18.000Z'
originalURL: https://freecodecamp.org/news/monadic-composition-and-kleisli-arrows-1d96979bb32
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CUnuyHcCX5A1KV1v3V8nTw.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: Scala
  slug: scala
- name: software
  slug: software
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment écrire des fonctions composables et des programmes corrects
seo_desc: 'By Pavel Zaytsev

  An overview with monads and Kleisli arrows


  A few words on the traditions ?


  If you have not written about monads are you even a programmer?


  It is a well-known fact that any respectable programmer who blogs about tech must
  at least ...'
---

Par Pavel Zaytsev

#### Une vue d'ensemble avec les monades et les flèches de Kleisli

![Image](https://cdn-media-1.freecodecamp.org/images/1*CUnuyHcCX5A1KV1v3V8nTw.jpeg)

### Quelques mots sur les traditions ?

> Si vous n'avez pas écrit sur les monades, êtes-vous vraiment un programmeur ?

Il est bien connu que tout programmeur respectable qui blogue sur la technologie doit au moins une fois dans sa vie écrire un tutoriel sur les **monades**. La plupart du temps, cela commence par les **functeurs** et construit tout le reste. Des comparaisons difficiles sont faites ici et là avec de courts extraits de code éparpillés pour démontrer quelques applications — tout semble complètement orthogonal, bien sûr.

Le problème est qu'il existe un fossé conceptuel gigantesque entre « Qu'est-ce qu'une monade ? » et « Comment une monade est-elle utilisée en programmation ? ».

La principale raison de ce fossé est que les gens ne pensent généralement pas à leurs programmes de manière à avoir besoin d'une monade en premier lieu. Si vous venez d'un contexte impératif — et la plupart d'entre nous en viennent — même lorsque vous passez enfin au fonctionnel, il faut généralement un certain temps pour voir l'ensemble du tableau et comprendre la bonne façon de faire les choses. Nous prêchons souvent la transparence référentielle et la pureté. Nous avons souvent une idée générale de ce que ces choses signifient séparément, mais il faut un certain temps pour les rassembler en un concept cohérent.

Cet article ne parle pas des monades, mais plutôt de l'écriture de fonctions composables et de programmes corrects. Les monades apparaissent comme un sous-produit de cet objectif. La discussion suivante, espérons-le, facilitera également le comblement du fossé conceptuel mentionné précédemment.

### Tout est une question de composition ?‍♂️

En programmation, les problèmes intéressants et importants sont généralement trop complexes pour être traités dans leur ensemble. Les programmeurs les décomposent en morceaux plus petits et compréhensibles qu'ils résolvent un par un, puis rassemblent les solutions à ces sous-problèmes en une image claire. Il existe de nombreuses façons de procéder, mais on peut clairement définir deux écoles de pensée — les approches déclaratives et impératives.

L'approche impérative considère un programme comme une séquence de calculs dans le temps, et l'unité d'un programme est une instruction. Une instruction fait quelque chose. Par exemple, elle peut afficher une sortie sur une console, assigner une valeur à une variable ou calculer un résultat.

L'approche déclarative est globale. Elle ne se soucie que de l'état initial et final du système, et l'unité d'un programme est une expression. L'expression **toujours** évalue à une valeur. En général, il est plus difficile de raisonner sur une instruction que sur une expression, car une instruction est beaucoup trop large et non bornée, tandis qu'une expression évalue toujours de manière déterministe à la même valeur pour tous les programmes dans lesquels elle peut potentiellement apparaître.

Si vous êtes un programmeur fonctionnel et que vous suivez un paradigme déclaratif, vous voyez un programme comme une composition de fonctions, et les fonctions sont simplement des expressions. Vous pouvez penser à une composition comme une simple fusion de deux fonctions ou plus en une seule.

Si vous avez une fonction _f_ qui prend un argument de type A et retourne un résultat de type B, et une autre fonction _g_ qui prend un argument de type B et retourne un résultat de type C, vous pouvez les composer en passant le résultat de _f_ à _g_. Ce que vous obtenez est une nouvelle fonction qui accepte un argument de type A et produit le résultat de type C. Faites cela quelques fois, et vous obtenez un programme fonctionnel. Cela ressemble à un raisonnement déductif, qui est simplement une composition d'étapes logiques, qui suivent des prémisses aux conclusions.

Le problème est que dans la programmation réelle, ce n'est pas si simple, et de nombreuses fonctions n'évaluent pas à la même valeur tout le temps, même si leurs arguments le font. Ces fonctions effectuent des appels réseau, lisent des fichiers et des bases de données, écrivent dedans, traitent beaucoup de données différentes, impriment sur une console, etc. Les fonctions deviennent **dépendantes du contexte**, et plus elles sont dépendantes du contexte, plus il est difficile de les composer. Donc, si vous devez traiter des fonctions où chacune d'entre elles introduit une certaine complexité ici et là, vous feriez mieux de trouver un moyen de les composer.

### Le problème éternel ?

Comme je l'ai déjà mentionné, l'écriture de code utile implique de traiter le chaos du monde extérieur — un problème de gestion des effets et de l'état. Par effet, j'entends un effet sur le monde extérieur, comme l'écriture dans une base de données ou l'impression sur une console. Même un simple programme `HelloWorld` produit un effet.

De nombreuses situations sont traditionnellement résolues en abandonnant la pureté des fonctions, y compris, mais sans s'y limiter :

* les calculs qui accèdent/modifient un état en dehors du contexte d'un programme.
* les calculs qui peuvent échouer ou ne jamais se terminer
* les calculs dont le résultat ne peut être connu qu'à un moment donné dans le futur, aka calculs asynchrones
* l'entrée et la sortie de la console

Comme vous pouvez l'imaginer, les fonctions qui se comportent ainsi ne sont pas si faciles à composer. Supposons qu'une fonction, étant donné un nom d'utilisateur sous la forme d'une chaîne d'entrée, lise un fichier, trouve l'utilisateur donné, puis passe son nom de famille à la fonction suivante pour un traitement ultérieur. Comment représentez-vous une telle fonction ? `String => String` ? Mais cela ne serait pas entièrement correct, car vous obtenez bien une chaîne et vous en retournez une, mais vous faites aussi autre chose entre-temps et cela dépend du contexte — un système de fichiers et un fichier.

En programmation fonctionnelle, nous encodons généralement cette information dans le type de retour de la fonction. Nous plaçons le résultat d'un calcul dans une boîte, pour ainsi dire, et notre fonction passe de `A => B` à `A => Box[B]`.

Ce qui se passe à l'intérieur de cette boîte est spécifique à l'implémentation. Mais la définition d'une fonction décrit maintenant ce qu'elle fait et permet de gérer le comportement de la fonction et de la composer, beaucoup mieux.

Examinons les situations ci-dessus et essayons de trouver une boîte pour chacune d'entre elles.

### Encapsuler toutes les choses ?

Avertissement : Dans cet article, j'utiliserai Scala pour exprimer mes idées, car c'est probablement l'un des principaux langages de programmation fonctionnelle grand public. Mais les mêmes concepts peuvent être facilement traduits dans n'importe quel langage de programmation fonctionnelle avec un système de types statiques forts et des constructeurs de types (comme Haskell et OCaml).

Une fonction qui lit mais ne modifie pas l'état externe peut être considérée comme une fonction qui accepte également cet état externe comme argument et, étant donné un paramètre d'entrée, produit un résultat. Un exemple est la lecture d'une base de données ou d'un fichier de configuration.

Nous fournissons également une fonction `run` pour matérialiser un lecteur et calculer un résultat. Le cas d'utilisation classique serait de :

* fournir un fichier de configuration
* empiler les lecteurs pour configurer une application
* exécuter la fonction `run` à la fin sur l'instance du fichier de configuration.

Dans le monde OOP, une approche similaire est appelée **Injection de dépendances**.

Les fonctions qui transportent l'état d'un calcul acceptent deux arguments — un argument régulier, qui participe au calcul réel, et l'état qui sera propagé tout au long de la composition.

Nous fournissons une fonction `run` qui produit le résultat qu'un writer actuel contient. Un cas d'utilisation typique de `Writer` est de propager des messages et des erreurs pendant l'exécution du programme, et d'extraire le journal ainsi que le résultat final. Un autre cas d'utilisation serait d'enregistrer les séquences d'étapes dans un environnement multithread. Puisque le résultat d'un calcul est lié à un journal particulier, les messages ne s'entremêlent pas.

Une fonction qui ne se termine jamais (par exemple, un processus de longue durée) est élevée à un **type bottom** de `Nothing`. Si vous vous attendez à ce que votre calcul retourne soit une valeur, soit s'exécute indéfiniment, vous pouvez le modéliser comme une union disjointe d'un type de résultat et de `Nothing`. Un exemple serait un consommateur de flux qui traite des données indéfiniment jusqu'à ce qu'un événement le fasse produire un résultat.

Une fonction qui peut échouer peut être modélisée comme une fonction partielle — celle qui n'est pas définie pour certaines valeurs. Nous faisons donc exactement cela — pour certains cas, nous ne retournons rien et, pour d'autres, une valeur réelle. Si vous voulez des informations concernant l'échec et pour interagir avec les API Java qui lancent des exceptions, vous pouvez transporter les informations d'une erreur avec vous dans l'union disjointe.

Les calculs asynchrones ne s'exécutent pas sur la pile d'appels actuelle ou le flux principal du programme. Ils peuvent être modélisés comme une fonction qui accepte un gestionnaire, ou rappel. Lorsque ce gestionnaire est finalement appelé — par exemple par un autre thread ou un serveur web — le résultat est produit.

`ExecutionContext` gère les détails de l'exécution asynchrone. Sur la JVM, il s'agit d'un pool de threads, mais ce n'est pas nécessairement des threads qui traitent de l'asynchronisme. La fonction `run` le prend implicitement car les rappels doivent être appelés de manière asynchrone. Chaque fonction qui appelle `run` doit avoir un `ExecutionContext` **implicite** dans sa signature également. `ExecutionContext` rend également les appels asynchrones récursifs sûrs pour la pile car vous introduisez une **frontière asynchrone** chaque fois que vous appelez une fonction. Comme je l'ai mentionné précédemment, les calculs asynchrones ne s'exécutent pas sur la même pile d'appels. Plutôt astucieux.

L'entrée de la console peut être modélisée comme un processus en deux phases. Dans la première phase, nous **définissons** le calcul et un résultat que l'entrée de la console peut produire. Dans la deuxième phase, nous exécutons ou **interprétons** ce calcul. Le type de données qui contient le résultat de ce calcul est appelé `IO`. Ainsi, notre fonction prend un singleton et produit le résultat à l'intérieur d'un `IO`.

Remarquez, puisque j'ai mentionné que nous définissons d'abord le calcul, nous passons des paramètres par nom `=> A`. Ils ne s'exécutent que lorsque nous en avons besoin. L'entrée de la console peut être modélisée à travers `IO` également, avec notre fonction `run` produisant un type singleton `de Unit`.

### Donc, maintenant quoi ? ?

Nous avons, bien sûr, implémenté toutes les boîtes avec un paramètre de type pour tenir compte de la variabilité des types. Nous transformons, ou mappons, de certaines choses à d'autres en fournissant une fonction. Un mappage entre une catégorie de certaines choses et une catégorie d'autres choses est appelé un **foncteur**.

Les foncteurs sont cool car ils nous permettent de transformer des choses à l'intérieur, tout en préservant la structure de la catégorie originale, sans tout mélanger. Lorsque vous utilisez un foncteur, le respect des [lois des foncteurs](https://en.wikibooks.org/wiki/Haskell/The_Functor_class#The_functor_laws) prouve que les choses fonctionnent comme prévu. Il deviendra clair plus tard dans l'article pourquoi **ces** lois en particulier.

Définissons une méthode map qui effectue la transformation pour chacun des types de données dérivés :

Remarquez que nous avons défini ici une fonction `pure` qui nous permet d'élever un calcul pur en une valeur asynchrone.

Cool, maintenant nous pouvons mapper des choses à l'intérieur des boîtes. Le problème est — ce n'est pas utile car, bien que nous puissions séquencer des calculs au sein d'un foncteur, nous ne pouvons pas composer des fonctions produisant des foncteurs :

```
F1: A -> Functor[B] ==> F2: A -> Functor[B] ==> F3: A -> Functor[B]
```

Chacun de `F1`, `F2` et `F3` peut faire quelque chose de complètement différent. Nous devons en tenir compte, nous devons les composer. Heureusement, il existe une excellente façon de procéder.

### Oh non, c'est encore ce type ! ?

D'accord, je dois écrire une fonction qui compose les fonctions pour chacun des foncteurs dans `A => Functor[B]`. La définition mathématique de la composition est :

```
Si A => B et B => C alors A => C
```

Donc dans notre cas :

```
Si A => Functor[B] et B => Functor[C] alors A => Functor[C]
```

Commençons par un lecteur. Encore une fois, suivez simplement les types :

Nous avons défini la composition comme `andThen`. Nous avons également défini `pure`, qui élève une valeur dans un foncteur.

La composition dans toute catégorie suit **deux lois simples**.

1. Elle est associative :

2. Il existe une fonction, appelée **identité**, qui, lorsqu'elle est composée avec n'importe quelle fonction de gauche ou de droite, produit cette fonction à nouveau :

Vous pouvez prendre un stylo et une feuille de papier et essayer de dessiner ces deux lois. En substituant les entités par des cercles et les connexions entre eux par des flèches, vous pouvez prouver visuellement à vous-même que c'est le cas. Vous vous souvenez des lois des foncteurs plus tôt ? C'est la même chose. Ces lois établissent la composabilité dans chaque catégorie.

En tant que programmeurs, nous traitons principalement avec une catégorie d'ensembles — les objets sont des ensembles ou des types, et les flèches sont des fonctions. Toutes les structures mathématiques n'ont pas besoin d'avoir une identité, mais une catégorie en a certainement besoin.

L'identité, par exemple, peut être utilisée pour montrer si deux objets, « ensembles », sont isomorphes, ou égaux. Elle peut également fournir des garanties dans certaines instances comme nous le verrons plus tard dans l'article.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TNDCu4w78aQktMU5aisvPg.png)
_Une catégorie n'a que deux propriétés — assez simple._

Un foncteur qui participe à `A => Functor[B]` et suit ces lois de composition, et donc compose pour tous les objets dans la même catégorie, n'est pas un burrito. C'est une monade.

En conséquence, les fonctions que nous essayons de composer sont en fait `A => Monad[B]`. Un wrapper autour d'elles, une catégorie qui est naturellement associée à `a Monad[B]`, est appelée une catégorie de Kleisli. `A => Monad[B]` ou les flèches de Kleisli est simplement un moyen de composer ces types de fonctions, rien de plus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pd47LtHoY8Hl4g_coz9SsQ.png)
_Kleisli a les mêmes objets que la catégorie originale, mais les flèches entre a et b dans Kleisli correspondent aux flèches entre a et Fb, où F est un foncteur._

### Composer toutes les choses ! ?

Nous remplaçons `andThen` de style Java par une flèche `>==>`. Cela s'appelle un opérateur fish car il ressemble à un poisson ?. Nous définissons également une fonction `flatMap` qui, étant donné un `Monad[A]` et `A => Monad[B]`, produit `A => Monad[B]`. Cela facilitera l'implémentation des flèches :

#### Monoïdes

Pour qu'un writer soit une monade, un second type doit également être composable, et il n'est composable que s'il s'agit d'un **monoïde**. Quelque chose est un monoïde seulement s'il peut être combiné de manière associative et possède un élément vide, qui est un élément identité.

Par exemple, les entiers qui s'additionnent sont un monoïde avec un élément identité de 0. Les chaînes qui se concatènent sont un monoïde avec un élément identité de chaîne vide. Les ensembles qui s'unissent sont un monoïde avec un élément identité d'ensemble vide. Les ensembles qui s'intersectent forment un semi-groupe et non un monoïde. L'intersection d'un ensemble non vide avec un ensemble vide produit un ensemble vide. Vous voyez pourquoi l'identité est utile ?

Toutes les autres monades sont faciles à implémenter :

Nous entrerons dans les détails de pourquoi `IO` ressemble à cela et aurons une discussion sur `Free` probablement dans un autre article.

### Quand utiliser lequel ? ?

`Kleisli` et `Monad` sont les deux faces d'une même pièce. De nombreux langages fonctionnels les supportent nativement, mais pour Scala, au moins dans la version actuelle 2.12.8, vous pouvez les obtenir à partir de bibliothèques comme Cats et Scalaz. Ils ont des classes de types pour `Kleisli` et `Monad` : `Kleisli[F[_], A, B]` et `Monad[A]` respectivement.

Les monades sont meilleures pour exprimer le séquençage des calculs qui se produisent dans un certain contexte. En Scala, nous faisons généralement ce séquençage contextuel en utilisant des comprehensions for.

Fait amusant : Si vous composez des flèches `Kleisli` pour la monade `IO`, vous obtiendrez une description de votre programme informatique. Votre programme informatique est essentiellement une gigantesque flèche `Kleisli`, avec une certaine entrée et sortie de `Unit` qui agit comme une description, et un environnement d'exécution qui exécute ce programme fonctionne comme un interpréteur.

Ainsi, chaque programme, par défaut, a un contexte `IO`. Si vous avez une fonction qui produit une erreur, elle crée un contexte de `Option` ou `Either`. Ainsi, chaque fonction ultérieure doit avoir une signature de `A => Option[A]` ou `A => Either[A, B]`. Dans un programme `IO`, c'est `A => IO[Option[A]]` et `A => IO[Either[A, B]]`. Vous décidez quand réduire ce contexte ou l'imbriquer encore plus. Les transformateurs de monades peuvent aider avec le séquençage des contextes imbriqués, mais c'est un sujet pour un autre article.

Les calculs asynchrones ne sont séquencés qu'à l'aide de monades, car les monades résolvent explicitement les problèmes de synchronisation et d'ordonnancement dans le temps. Si vous utilisez des combinateurs Future, par exemple, c'est dans un contexte monadique.

`Kleisli` est meilleur lorsque le combinateur de flèches est plus adapté. Par exemple, nous pouvons avoir un ensemble de fonctions effectives ou impures, et nous pouvons les fusionner sans envelopper le résultat dans `IO`. Vous pouvez également créer un ensemble de programmes individuels et les combiner en une seule flèche `Kleisli` à la fin et l'exécuter si vous le souhaitez, bien sûr.

`Reader[A]` est mieux exprimé avec `Kleisli` qu'avec des compositions monadiques car nous pouvons facilement composer de petites flèches `Kleisli` locales en une flèche `Kleisli` qui représente la configuration globale de notre programme. La grande flèche `Kleisli` dépend d'un certain environnement, par exemple un fichier de configuration pour la production et le développement. Ensuite, nous pouvons l'exécuter à la toute fin et configurer l'ensemble de l'application.

Cette approche imite le concept d'**injection de dépendances**. Ici, nous démontrons `KleisliIO`, une flèche `Kleisli` effective de [ZIO](https://github.com/scalaz/scalaz-zio) qui effectue une fonctionnalité de lecteur pour configurer l'application (le type d'erreur est omis pour économiser de l'espace) :

### Fin ?

Ouf, c'était une explosion. J'espère que vous avez apprécié cet article et que vous comprenez maintenant un peu mieux ce qui se passe :).

Voici quelques liens utiles pour en savoir plus sur Kleisli et la composition :

* [www.cse.chalmers.se/~rjmh/Papers/arrows.pdf](http://www.cse.chalmers.se/~rjmh/Papers/arrows.pdf)
* [https://www.youtube.com/watch?v=qL6Viix3npA](https://www.youtube.com/watch?v=qL6Viix3npA)