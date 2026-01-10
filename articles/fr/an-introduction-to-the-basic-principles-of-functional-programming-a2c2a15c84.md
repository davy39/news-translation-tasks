---
title: Une introduction aux principes de base de la programmation fonctionnelle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-15T20:41:39.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-the-basic-principles-of-functional-programming-a2c2a15c84
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OtbWm_2OFtg7suie4zEtqA.png
tags:
- name: coding
  slug: coding
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Une introduction aux principes de base de la programmation fonctionnelle
seo_desc: 'By TK

  After a long time learning and working with object-oriented programming, I took
  a step back to think about system complexity.


  "Complexity is anything that makes software hard to understand or to modify." —
  John Outerhout


  Doing some research, ...'
---

Par TK

Après avoir passé beaucoup de temps à apprendre et à travailler avec la programmation orientée objet, j'ai fait un pas en arrière pour réfléchir à la complexité des systèmes.

> "`La complexité est tout ce qui rend le logiciel difficile à comprendre ou à modifier.`" — John Outerhout

En faisant quelques recherches, j'ai découvert des concepts de programmation fonctionnelle comme l'immuabilité et les fonctions pures. Ces concepts sont de grands avantages pour construire des fonctions sans effets secondaires, ce qui facilite la maintenance des systèmes — avec quelques autres [avantages](https://hackernoon.com/why-functional-programming-matters-c647f56a7691).

Dans cet article, je vais vous en dire plus sur la programmation fonctionnelle et quelques concepts importants, avec beaucoup d'exemples de code.

Cet article utilise Clojure comme exemple de langage de programmation pour expliquer la programmation fonctionnelle. Si vous n'êtes pas à l'aise avec un langage de type LISP, j'ai également publié le même article en JavaScript. Jetez un œil : [**Principes de la programmation fonctionnelle en JavaScript**](https://medium.freecodecamp.org/functional-programming-principles-in-javascript-1b8fc6c3563f)

### Qu'est-ce que la programmation fonctionnelle ?

> **La programmation fonctionnelle** est un paradigme de programmation — un style de construction de la structure et des éléments des programmes informatiques — qui traite le calcul comme l'évaluation de fonctions mathématiques et évite de changer l'état et les données mutables — [Wikipedia](https://en.wikipedia.org/wiki/Functional_programming)

### Fonctions pures

![Image](https://cdn-media-1.freecodecamp.org/images/0*FMur6URY7yAVjeuP)
_"goutte d'eau" par [Unsplash](https://unsplash.com/@martinmohan?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Mohan Murugesan</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Le premier concept fondamental que nous apprenons lorsque nous voulons comprendre la programmation fonctionnelle est celui des **fonctions pures**. Mais que signifie réellement cela ? Qu'est-ce qui rend une fonction pure ?

Alors, comment savons-nous si une fonction est `pure` ou non ? Voici une définition très stricte de la pureté :

* Elle retourne le même résultat si on lui donne les mêmes arguments (on dit aussi qu'elle est `déterministe`)
* Elle ne provoque aucun effet secondaire observable

#### Elle retourne le même résultat si on lui donne les mêmes arguments

Imaginons que nous voulons implémenter une fonction qui calcule l'aire d'un cercle. Une fonction impure recevrait `radius` comme paramètre, puis calculerait `radius * radius * PI`. En Clojure, l'opérateur vient en premier, donc `radius * radius * PI` devient `(* radius radius PI)` :

Pourquoi cette fonction est-elle impure ? Tout simplement parce qu'elle utilise un objet global qui n'a pas été passé en paramètre à la fonction.

Maintenant, imaginons que des mathématiciens soutiennent que la valeur de `PI` est en fait `[42](https://en.wikipedia.org/wiki/Phrases_from_The_Hitchhiker%27s_Guide_to_the_Galaxy#Answer_to_the_Ultimate_Question_of_Life,_the_Universe,_and_Everything_(42))` et changent la valeur de l'objet global.

Notre fonction impure donnera maintenant `10 * 10 * 42` = `4200`. Pour le même paramètre (`radius = 10`), nous avons un résultat différent. Corrigons cela !

TA-DA ?! Maintenant, nous passerons toujours la valeur de `PI` en tant que paramètre à la fonction. Ainsi, nous n'accédons qu'aux paramètres passés à la fonction. Aucun `objet externe`.

* Pour les paramètres `radius = 10` & `PI = 3.14`, nous aurons toujours le même résultat : `314.0`
* Pour les paramètres `radius = 10` & `PI = 42`, nous aurons toujours le même résultat : `4200`

#### Lecture de fichiers

Si notre fonction lit des fichiers externes, ce n'est pas une fonction pure — le contenu du fichier peut changer.

#### Génération de nombres aléatoires

Toute fonction qui dépend d'un générateur de nombres aléatoires ne peut pas être pure.

#### Elle ne provoque aucun effet secondaire observable

Des exemples d'effets secondaires observables incluent la modification d'un objet global ou d'un paramètre passé par référence.

Maintenant, nous voulons implémenter une fonction pour recevoir une valeur entière et retourner la valeur augmentée de 1.

Nous avons la valeur `counter`. Notre fonction impure reçoit cette valeur et réassigne le compteur avec la valeur augmentée de 1.

**Observation** : la mutabilité est découragée en programmation fonctionnelle.

Nous modifions l'objet global. Mais comment la rendre `pure` ? Il suffit de retourner la valeur augmentée de 1. C'est aussi simple que cela.

Voyez que notre fonction pure `increase-counter` retourne 2, mais la valeur `counter` reste la même. La fonction retourne la valeur incrémentée sans altérer la valeur de la variable.

Si nous suivons ces deux règles simples, il devient plus facile de comprendre nos programmes. Maintenant, chaque fonction est isolée et incapable d'impacter d'autres parties de notre système.

Les fonctions pures sont stables, cohérentes et prévisibles. Étant donné les mêmes paramètres, les fonctions pures retourneront toujours le même résultat. Nous n'avons pas besoin de penser à des situations où le même paramètre donne des résultats différents — car cela n'arrivera jamais.

#### Avantages des fonctions pures

Le code est définitivement plus facile à tester. Nous n'avons pas besoin de simuler quoi que ce soit. Nous pouvons donc tester unitairement les fonctions pures avec différents contextes :

* Étant donné un paramètre `A` → s'attendre à ce que la fonction retourne la valeur `B`
* Étant donné un paramètre `C` → s'attendre à ce que la fonction retourne la valeur `D`

Un exemple simple serait une fonction pour recevoir une collection de nombres et s'attendre à ce qu'elle incrémente chaque élément de cette collection.

Nous recevons la collection `numbers`, utilisons `map` avec la fonction `inc` pour incrémenter chaque nombre, et retournons une nouvelle liste de nombres incrémentés.

Pour l'`input` `[1 2 3 4 5]`, l'`output` attendu serait `[2 3 4 5 6]`.

### Immuabilité

> _Inchangeable dans le temps ou incapable d'être changé._

![Image](https://cdn-media-1.freecodecamp.org/images/0*MGlzHgISuw0dXwsf)
_"Néon changeant" par [Unsplash](https://unsplash.com/@rossf?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Ross Findon</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Lorsque les données sont immuables, leur **état ne peut pas changer** **après leur création**. Si vous voulez changer un objet immuable, vous ne pouvez pas. Au lieu de cela, **vous créez un nouvel objet avec la nouvelle valeur**.

En JavaScript, nous utilisons couramment la boucle `for`. Cette instruction `for` suivante a quelques variables mutables.

À chaque itération, nous changeons l'état de `i` et de `sumOfValue`. Mais comment gérer la mutabilité dans l'itération ? La récursivité ! Retour à Clojure !

Ici, nous avons la fonction `sum` qui reçoit un vecteur de valeurs numériques. Le `recur` saute en arrière dans la `loop` jusqu'à ce que nous obtenions le vecteur vide ([notre cas de base de récursivité](https://en.wikipedia.org/wiki/Recursion_(computer_science)#Recursive_functions_and_algorithms)). Pour chaque "itération", nous ajouterons la valeur à l'accumulateur `total`.

Avec la récursivité, nous gardons nos **variables** immuables.

**Observation** : Oui ! Nous pouvons utiliser `reduce` pour implémenter cette fonction. Nous verrons cela dans le sujet des `Fonctions d'ordre supérieur`.

Il est également très courant de construire l'état **final** d'un objet. Imaginons que nous avons une chaîne de caractères, et que nous voulons transformer cette chaîne en un `slug d'URL`.

En POO en Ruby, nous créerions une classe, disons, `UrlSlugify`. Et cette classe aurait une méthode `slugify!` pour transformer l'entrée de chaîne en un `slug d'URL`.

Magnifique ! C'est implémenté ! Ici, nous avons une programmation impérative qui dit exactement ce que nous voulons faire dans chaque processus `slugify` — d'abord en minuscules, puis enlever les espaces blancs inutiles et, enfin, remplacer les espaces blancs restants par des traits d'union.

Mais nous mutons l'état d'entrée dans ce processus.

Nous pouvons gérer cette mutation en faisant de la composition de fonctions, ou de l'enchaînement de fonctions. En d'autres termes, le résultat d'une fonction sera utilisé comme entrée pour la fonction suivante, sans modifier la chaîne d'entrée originale.

Ici, nous avons :

* `trim` : supprime les espaces blancs des deux extrémités d'une chaîne
* `lower-case` : convertit la chaîne en minuscules
* `replace` : remplace toutes les instances de correspondance par un remplacement dans une chaîne donnée

Nous combinons les trois fonctions et nous pouvons "slugifier" notre chaîne.

En parlant de **combinaison de fonctions**, nous pouvons utiliser la fonction `comp` pour composer les trois fonctions. Jetons un coup d'œil :

### Transparence référentielle

![Image](https://cdn-media-1.freecodecamp.org/images/0*K0VAbQjAwmKZb1at)
_"personne tenant des lunettes" par [Unsplash](https://unsplash.com/@joshcala?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Josh Calabrese</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Implémentons une fonction `carré` :

Cette fonction (pure) aura toujours la même sortie, étant donné la même entrée.

Passer "2" comme paramètre de la fonction `carré` retournera toujours 4. Donc maintenant nous pouvons remplacer `(carré 2)` par 4. C'est tout ! Notre fonction est `référentiellement transparente`.

En gros, si une fonction produit constamment le même résultat pour la même entrée, elle est référentiellement transparente.

**fonctions pures + données immuables = transparence référentielle**

Avec ce concept, une chose cool que nous pouvons faire est de mémoriser la fonction. Imaginons que nous avons cette fonction :

Le `(+ 5 8)` est égal à `13`. Cette fonction donnera toujours `13`. Donc nous pouvons faire ceci :

Et cette expression donnera toujours `16`. Nous pouvons remplacer toute l'expression par une constante numérique et la [mémoriser](https://en.wikipedia.org/wiki/Memoization).

### Fonctions en tant qu'entités de première classe

![Image](https://cdn-media-1.freecodecamp.org/images/0*K6m1Ftw54Wm6tfFB)
_"première classe" par [Unsplash](https://unsplash.com/@andrewtneel?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Andrew Neel</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

L'idée des fonctions en tant qu'entités de première classe est que les fonctions sont **aussi** traitées comme des valeurs **et** utilisées comme des données.

En Clojure, il est courant d'utiliser `defn` pour définir des fonctions, mais ce n'est que du sucre syntaxique pour `(def foo (fn ...))`. `fn` retourne la fonction elle-même. `defn` retourne une `var` qui pointe vers un objet fonction.

Les fonctions en tant qu'entités de première classe peuvent :

* y faire référence à partir de constantes et de variables
* la passer en tant que paramètre à d'autres fonctions
* la retourner en tant que résultat d'autres fonctions

L'idée est de traiter les fonctions comme des valeurs et de passer des fonctions comme des données. De cette façon, nous pouvons combiner différentes fonctions pour créer de nouvelles fonctions avec de nouveaux comportements.

Imaginons que nous avons une fonction qui additionne deux valeurs puis double la valeur. Quelque chose comme ceci :

Maintenant une fonction qui soustrait des valeurs et retourne le double :

Ces fonctions ont une logique similaire, mais la différence est les fonctions opérateurs. Si nous pouvons traiter les fonctions comme des valeurs et les passer en tant qu'arguments, nous pouvons construire une fonction qui reçoit la fonction opérateur et l'utilise à l'intérieur de notre fonction. Construisons-la !

Fini ! Maintenant nous avons un argument `f`, et nous l'utilisons pour traiter `a` et `b`. Nous avons passé les fonctions `+` et `-` pour composer avec la fonction `double-operator` et créer un nouveau comportement.

### Fonctions d'ordre supérieur

Lorsque nous parlons de fonctions d'ordre supérieur, nous parlons d'une fonction qui soit :

* prend une ou plusieurs fonctions comme arguments, ou
* retourne une fonction comme résultat

La fonction `double-operator` que nous avons implémentée ci-dessus est une fonction d'ordre supérieur car elle prend une fonction opérateur comme argument et l'utilise.

Vous avez probablement déjà entendu parler de `filter`, `map` et `reduce`. Jetons un coup d'œil à ceux-ci.

#### Filtrer

Étant donné une collection, nous voulons filtrer par un attribut. La fonction de filtrage attend une valeur `true` ou `false` pour déterminer si l'élément **doit ou ne doit pas** être inclus dans la collection de résultats. Basiquement, si l'expression de rappel est `true`, la fonction de filtrage inclura l'élément dans la collection de résultats. Sinon, elle ne le fera pas.

Un exemple simple est lorsque nous avons une collection d'entiers et que nous voulons seulement les nombres pairs.

**Approche impérative**

Une façon impérative de le faire avec Javascript est de :

* créer un vecteur vide `evenNumbers`
* itérer sur le vecteur `numbers`
* pousser les nombres pairs vers le vecteur `evenNumbers`

Nous pouvons utiliser la fonction d'ordre supérieur `filter` pour recevoir la fonction `even?`, et retourner une liste de nombres pairs :

Un problème intéressant que j'ai résolu sur [Hacker Rank FP](https://www.hackerrank.com/domains/fp) Path était le [**problème de filtrage de tableau**](https://www.hackerrank.com/challenges/fp-filter-array/problem). L'idée du problème est de filtrer un tableau donné d'entiers et de sortir seulement ces valeurs qui sont inférieures à une valeur spécifiée `X`.

Une solution impérative en Javascript à ce problème serait quelque chose comme :

Nous disons exactement ce que notre fonction doit faire — itérer sur la collection, comparer l'élément courant de la collection avec `x`, et pousser cet élément vers `resultArray` s'il passe la condition.

**Approche déclarative**

Mais nous voulons une manière plus déclarative de résoudre ce problème, et utiliser la fonction d'ordre supérieur `filter` également.

Une solution déclarative en Clojure serait quelque chose comme ceci :

Cette syntaxe semble un peu étrange au premier abord, mais elle est facile à comprendre.

`#(> x %)` est juste une fonction anonyme qui reçoit `x` et le compare avec chaque élément de la collection. `%` représente le paramètre de la fonction anonyme — dans ce cas, l'élément courant à l'intérieur du filtre.

Nous pouvons aussi faire cela avec des maps. Imaginons que nous avons une map de personnes avec leur `nom` et `âge`. Et nous voulons filtrer seulement les personnes au-dessus d'une valeur d'âge spécifiée, dans cet exemple les personnes qui ont plus de 21 ans.

Résumé du code :

* nous avons une liste de personnes (avec `nom` et `âge`).
* nous avons la fonction anonyme `#(< 21 (:age %))`. Rappelez-vous que `%` représente l'élément courant de la collection ? Eh bien, l'élément de la collection est une map de personnes. Si nous faisons `(:age {:name "TK" :age 26})`, cela retourne la valeur de l'âge, 26 dans ce cas.
* nous filtrons toutes les personnes basées sur cette fonction anonyme.

#### Map

L'idée de map est de transformer une collection.

> La méthode `_map_` transforme une collection en appliquant une fonction à tous ses éléments et en construisant une nouvelle collection à partir des valeurs retournées.

Prenons la même collection `people` ci-dessus. Nous ne voulons pas filtrer par "âge" maintenant. Nous voulons simplement une liste de chaînes, quelque chose comme `TK a 26 ans`. Donc la chaîne finale pourrait être `:name a :age ans` où `:name` et `:age` sont des attributs de chaque élément dans la collection `people`.

En JavaScript impératif, ce serait :

En Clojure déclaratif, ce serait :

L'idée est de transformer une collection donnée en une nouvelle collection.

Un autre problème intéressant de Hacker Rank était le [**problème de mise à jour de liste**](https://www.hackerrank.com/challenges/fp-update-list/problem). Nous voulons simplement mettre à jour les valeurs d'une collection donnée avec leurs valeurs absolues.

Par exemple, l'entrée `[1 2 3 -4 5]` doit avoir pour sortie `[1 2 3 4 5]`. La valeur absolue de `-4` est `4`.

Une solution simple serait une mise à jour en place pour chaque valeur de la collection.

Nous utilisons la fonction `Math.abs` pour transformer la valeur en sa valeur absolue, et faisons la mise à jour en place.

Ce n'est **pas** une manière fonctionnelle d'implémenter cette solution.

Premièrement, nous avons appris l'immuabilité. Nous savons à quel point l'immuabilité est importante pour rendre nos fonctions plus cohérentes et prévisibles. L'idée est de construire une nouvelle collection avec toutes les valeurs absolues.

Deuxièmement, pourquoi ne pas utiliser `map` ici pour "transformer" toutes les données ?

Ma première idée était de construire une fonction `to-absolute` pour gérer une seule valeur.

Si elle est négative, nous voulons la transformer en une valeur positive (la valeur absolue). Sinon, nous n'avons pas besoin de la transformer.

Maintenant que nous savons comment faire `absolute` pour une valeur, nous pouvons utiliser cette fonction pour la passer en argument à la fonction `map`. Vous vous souvenez qu'une `fonction d'ordre supérieur` peut recevoir une fonction comme argument et l'utiliser ? Oui, map peut le faire !

Wow. Si beau ! ?

#### Réduire

L'idée de réduire est de recevoir une fonction et une collection, et de retourner une valeur créée en combinant les éléments.

Un exemple courant dont les gens parlent est d'obtenir le montant total d'une commande. Imaginez que vous êtes sur un site de shopping. Vous avez ajouté `Produit 1`, `Produit 2`, `Produit 3`, et `Produit 4` à votre panier (commande). Maintenant, nous voulons calculer le montant total du panier.

De manière impérative, nous itérerions sur la liste de commandes et additionnerions chaque montant de produit au montant total.

En utilisant `reduce`, nous pouvons construire une fonction pour gérer la `somme des montants` et la passer en argument à la fonction `reduce`.

Ici, nous avons `shopping-cart`, la fonction `sum-amount` qui reçoit le `total-amount` actuel, et l'objet `current-product` pour les `sum`.

La fonction `get-total-amount` est utilisée pour `réduire` le `shopping-cart` en utilisant le `sum-amount` et en commençant par `0`.

Une autre façon d'obtenir le montant total est de composer `map` et `reduce`. Que veux-je dire par là ? Nous pouvons utiliser `map` pour transformer le `shopping-cart` en une collection de valeurs `amount`, puis simplement utiliser la fonction `reduce` avec la fonction `+`.

La fonction `get-amount` reçoit l'objet produit et retourne seulement la valeur `amount`. Donc ce que nous avons ici est `[10 30 20 60]`. Et ensuite le `reduce` combine tous les éléments en les additionnant. Magnifique !

Nous avons jeté un coup d'œil à la façon dont chaque fonction d'ordre supérieur fonctionne. Je veux vous montrer un exemple de la façon dont nous pouvons composer les trois fonctions dans un exemple simple.

En parlant de `panier d'achat`, imaginons que nous avons cette liste de produits dans notre commande :

Nous voulons le montant total de tous les livres dans notre panier. C'est aussi simple que cela. L'algorithme ?

* **filtrer** par type de livre
* transformer le panier en une collection de montants en utilisant **map**
* combiner tous les éléments en les additionnant avec **reduce**

Fini ! ?

### Ressources

J'ai organisé quelques ressources que j'ai lues et étudiées. Je partage celles que j'ai trouvées vraiment intéressantes. Pour plus de ressources, visitez mon [**dépôt Github sur la programmation fonctionnelle**](https://github.com/LeandroTk/learning-functional-programming).

* [Ressources spécifiques à Ruby](https://github.com/LeandroTk/learning-functional-programming/tree/master/ruby)
* [Ressources spécifiques à Javascript](https://github.com/LeandroTk/learning-functional-programming/tree/master/javascript)
* [Ressources spécifiques à Clojure](https://github.com/LeandroTk/learning-functional-programming/tree/master/clojure)

#### Introductions

* [Apprendre la PF en JS](https://www.youtube.com/watch?v=e-5obm1G_FY)
* [Intro à la PF avec Python](https://codewords.recurse.com/issues/one/an-introduction-to-functional-programming)
* [Aperçu de la PF](https://blog.codeship.com/overview-of-functional-programming)
* [Une rapide intro au JS fonctionnel](https://hackernoon.com/a-quick-introduction-to-functional-javascript-7e6fe520e7fa)
* [Qu'est-ce que la PF ?](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-functional-programming-7f218c68b3a0)
* [Jargon de la programmation fonctionnelle](https://github.com/hemanth/functional-programming-jargon)

#### Fonctions pures

* [Qu'est-ce qu'une fonction pure ?](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-pure-function-d1c076bec976)
* [Programmation fonctionnelle pure 1](https://www.fpcomplete.com/blog/2017/04/pure-functional-programming)
* [Programmation fonctionnelle pure 2](https://www.fpcomplete.com/blog/2017/05/pure-functional-programming-part-2)

#### Données immuables

* [Structures de données immuables pour la programmation fonctionnelle](https://www.youtube.com/watch?v=Wo0qiGPSV-s)
* [Pourquoi l'état mutable partagé est la racine de tous les maux](http://henrikeichenhardt.blogspot.com/2013/06/why-shared-mutable-state-is-root-of-all.html)
* [Partage structurel en Clojure : Partie 1](http://hypirion.com/musings/understanding-persistent-vector-pt-1)
* [Partage structurel en Clojure : Partie 2](http://hypirion.com/musings/understanding-persistent-vector-pt-2)
* [Partage structurel en Clojure : Partie 3](http://hypirion.com/musings/understanding-persistent-vector-pt-3)
* [Partage structurel en Clojure : Partie finale](http://hypirion.com/musings/persistent-vector-performance-summarised)

#### Fonctions d'ordre supérieur

* [Eloquent JS : Fonctions d'ordre supérieur](https://eloquentjavascript.net/05_higher_order.html)
* [Fun fun function Filter](https://www.youtube.com/watch?v=BMUiFMZr7vk&t=0s&list=PL0zVEGEvSaeEd9hlmCXrk5yUyqUag-n84&index=2&ab_channel=FunFunFunction)
* [Fun fun function Map](https://www.youtube.com/watch?v=bCqtb-Z5YGQ&index=2&list=PL0zVEGEvSaeEd9hlmCXrk5yUyqUag-n84&ab_channel=FunFunFunction)
* [Fun fun function Basic Reduce](https://www.youtube.com/watch?v=Wl98eZpkp-c&list=PL0zVEGEvSaeEd9hlmCXrk5yUyqUag-n84&index=3&frags=wn&ab_channel=FunFunFunction)
* [Fun fun function Advanced Reduce](https://www.youtube.com/watch?v=1DMolJ2FrNY&list=PL0zVEGEvSaeEd9hlmCXrk5yUyqUag-n84&index=4&ab_channel=FunFunFunction)
* [Fonctions d'ordre supérieur en Clojure](https://clojure.org/guides/higher_order_functions)
* [Purely Function Filter](https://purelyfunctional.tv/lesson/filter/)
* [Purely Functional Map](https://purelyfunctional.tv/lesson/map/)
* [Purely Functional Reduce](https://purelyfunctional.tv/lesson/reduce/)

#### Programmation déclarative

* [Programmation déclarative vs impérative](https://tylermcginnis.com/imperative-vs-declarative-programming/)

### C'est tout !

Salut les gens, j'espère que vous avez pris plaisir à lire cet article, et j'espère que vous avez appris beaucoup ici ! C'était ma tentative de partager ce que j'apprends.

[**Voici le dépôt avec tous les codes**](https://github.com/LeandroTk/functional-programming-article-source-code) de cet article.

Venez apprendre avec moi. Je partage des ressources et mon code dans ce [**dépôt d'apprentissage de la programmation fonctionnelle**](https://github.com/LeandroTk/learning-functional-programming).

J'espère que vous avez vu quelque chose d'utile pour vous ici. Et à la prochaine fois ! :)

Mon [Twitter](https://twitter.com/LeandroTk_) & [Github](https://github.com/LeandroTk). ☺

TK.