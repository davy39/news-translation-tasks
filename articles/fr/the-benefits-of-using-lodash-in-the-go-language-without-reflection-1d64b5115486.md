---
title: Les avantages de l'utilisation de Lodash dans le langage Go sans réflexion
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-18T20:14:49.000Z'
originalURL: https://freecodecamp.org/news/the-benefits-of-using-lodash-in-the-go-language-without-reflection-1d64b5115486
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TiOHph4NBWwjeVHMvREuZw.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: golang
  slug: golang
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Les avantages de l'utilisation de Lodash dans le langage Go sans réflexion
seo_desc: 'By Tal Kol

  Working with Node.js, I’ve grown to rely on Lodash as an invaluable tool. It completes
  the JavaScript standard library with a set of handy functional operators over collections.
  I can’t recall a single JavaScript project I’ve worked on in ...'
---

Par Tal Kol

En travaillant avec Node.js, je me suis habitué à compter sur [Lodash](https://lodash.com/) comme un outil inestimable. Il complète la bibliothèque standard JavaScript avec un ensemble d'opérateurs fonctionnels pratiques pour les collections. Je ne me souviens pas d'un seul projet JavaScript sur lequel j'ai travaillé ces dernières années qui ne l'ait pas utilisé.

Mon expérience de passage à Go a été très agréable. Go résout de nombreux problèmes que j'ai eus avec Node.js au fil des ans et reste tout aussi productif. Cependant, une chose me manquait cruellement : une bibliothèque comme Lodash.

### Qu'est-ce qui rend Lodash si génial ?

JavaScript n'est pas un langage purement fonctionnel, et la plupart du code que j'écris en JavaScript tend à être impératif. Néanmoins, certains principes de la programmation fonctionnelle (comme l'enchaînement d'opérateurs et l'immuabilité) sont très pratiques lors de la manipulation de collections.

Supposons que j'ai un tableau avec des doublons que je veux supprimer. Avec Lodash, il suffit d'une ligne :

Supposons que je ne veux garder que les couleurs dont les noms font plus de 4 lettres. Cela prend également une ligne :

Et maintenant, supposons que je veux mettre en majuscule la première lettre de chaque couleur... oui, pas plus d'une ligne. Je peux même faire tout cela ensemble :

Lodash est probablement l'outil le plus pratique pour travailler avec des collections en JavaScript.

### Comment faire cela en Go ?

Commençons par la première tâche : obtenir une tranche unique. En cherchant une solution de meilleure pratique en Go, ce [billet de blog](https://kylewbanks.com/blog/creating-unique-slices-in-go) apparaît comme premier résultat. Voici le code, crédits à [Kyle Banks](https://www.freecodecamp.org/news/the-benefits-of-using-lodash-in-the-go-language-without-reflection-1d64b5115486/undefined) :

Vous pouvez imaginer que si nous devions également filtrer et mettre en majuscule la première lettre de chaque couleur, nous passerions beaucoup trop de temps sur la mécanique de ces actions. Cela serait un peu épuisant. Où sont mes lignes de code concises ?

### Des bibliothèques à la rescousse

Bien sûr, il existe des bibliothèques qui effectuent ces actions pratiques sur les collections pour nous. Étonnamment, il n'y en a pas beaucoup de populaires en Go. Pourquoi ?

Pour qu'une telle bibliothèque soit utile, elle devrait supporter de nombreux types de collections. Cela est dû au fait que vous pouvez avoir une tranche de chaînes, une tranche d'entiers ou une tranche de structures. Supporter un type **générique** de tranche n'est pas simple en Go.

Dans la plupart des langages strictement typés, cela est réalisé avec une construction de langage appelée [generics](https://en.wikipedia.org/wiki/Generic_programming). Malheureusement, Go ne le [supporte pas](https://golang.org/doc/faq#generics) actuellement.

Alors, comment pouvons-nous implémenter une telle bibliothèque sans generics ? Le gourou de Go, Rob Pike, montre un exemple d'implémentation de la fonction `filter` dans ce [dépôt Github](https://github.com/robpike/filter). Remarquez l'utilisation intensive de la [réflexion](https://github.com/robpike/filter/blob/master/reduce.go#L22). En effet, il n'est pas difficile d'étendre cette technique et d'implémenter les diverses méthodes utilitaires de Lodash. Vous pouvez voir un exemple de projet qui tente de faire exactement cela [ici](https://github.com/arifsetiawan/lodash-go).

### Pourquoi devrions-nous éviter la réflexion ?

La réflexion examine les types à l'exécution. En contournant le manque de generics de Go avec la réflexion, nous déplaçons le travail lourd de gestion de plusieurs types de collections du temps de compilation au temps d'exécution.

Les fonctions utilitaires de base qui travaillent avec des collections devraient être efficaces. Je n'ai pas fait de benchmarking approprié, mais compter sur la réflexion pour une tâche aussi courante semble tout simplement incorrect.

Alors, comme expérience de pensée, que pouvons-nous faire à la place ? Pouvez-nous créer une implémentation vraiment efficace de Lodash en Go qui rivalisera avec l'approche de la boucle **for** en termes de performance ?

### Génération de code au moment de la compilation

Générer du code dans le cadre de la chaîne d'outils de développement n'est pas un concept étranger en Go. Il est utilisé par le [compilateur Protobuf](https://github.com/golang/protobuf) pour générer des méthodes d'accès Go pour les définitions de protocoles. Il a même été introduit comme une fonctionnalité officielle de la chaîne d'outils Go avec `[go generate](https://blog.golang.org/generate)` depuis la version 1.4.

Et si nous voulions déplacer le travail lourd de gestion des types de collections génériques vers le temps de compilation ? La meilleure façon de faire cela (actuellement) est de générer du code spécifique à un type pour chacun des types dont nous avons besoin dans notre projet !

Considérons l'implémentation précédente de `uniq` sur une tranche de `string` :

Comment l'implémentation différerait-elle si nous avions besoin de support pour une tranche d'`int` ?

Comme vous pouvez le voir, c'est pratiquement identique, sauf que chaque occurrence de `string` a été remplacée par `int`.

Pouvons-nous faire cela automatiquement d'une manière ou d'une autre ?

### Lodash en Go sans réflexion

Commençons par concevoir notre API. Nous pouvons nous inspirer de l'implémentation originale de [Lodash](https://lodash.com/) en JavaScript. Là, la bibliothèque est utilisée avec le caractère de soulignement `_`. Par exemple, `_.uniq()`.

Nous pouvons rendre hommage en gardant la même convention. La différence est que dans notre cas, le soulignement sera suivi d'un type. Par exemple, `_int.Uniq()` pour les entiers et `_string.Uniq()` pour les chaînes. Nous devons spécifier le type explicitement puisque nous allons obtenir une implémentation entièrement nouvelle et dédiée de toute la bibliothèque pour le type spécifique dont nous avons besoin. Cela garantira que notre temps d'exécution est aussi efficace que possible.

L'utilisation est très simple. Il suffit d'importer l'implémentation que vous voulez :

Il existe des dizaines de types potentiels. Cela signifie-t-il que notre bibliothèque `go-dash/slice` doit venir avec chacun d'eux ? Pas vraiment, car cela ne serait pas pratique. Nous allons générer les implémentations requises dynamiquement au moment de la compilation !

Pour y parvenir, nous allons introduire un outil de ligne de commande intéressant : `_gen`, le générateur de code pour notre implémentation de bibliothèque Lodash (remarquez comment il commence également par un soulignement).

Lorsque `_gen` est exécuté à la racine source de n'importe quel projet, il parcourt tous les fichiers sources du projet et recherche les imports `github.com/go-dash/slice/_TYPE`. Dans l'exemple ci-dessus, il en trouvera un pour `_string` et un pour `_int`. Le générateur générera ensuite une implémentation pour ces types spécifiques dynamiquement et l'ajoutera à la bibliothèque trouvée dans l'espace de travail Go sous le chemin `$GOPATH/src/github.com/go-dash/slice`.

L'implémentation de `go-dash/slice` sur [Github](https://github.com/go-dash/slice) est en réalité très légère. Elle ne contient qu'une implémentation templatée pour un seul type générique. Le générateur de code s'appuie sur ce template pour créer les implémentations de types spécifiques selon vos exigences lorsque vous compilez votre projet.

### Et les types personnalisés ?

Supposons que votre projet définit un type complexe personnalisé comme `Person` :

Il serait assez pratique si nous pouvions utiliser notre bibliothèque Lodash sur une tranche de `Person` également. Eh bien, cela peut en fait fonctionner de la même manière. Il suffit d'importer une implémentation de `go-dash/slice` qui fonctionne sur `Person` et le générateur de code s'occupera du reste :

### Un prototype fonctionnel

Un prototype fonctionnel de la bibliothèque `go-dash/slice`, qui fournit plusieurs fonctions utiles comme `uniq`, `filter` et `chain`, est disponible sur [Github](https://github.com/go-dash/slice).

Le projet inclut également un [générateur de ligne de commande](https://github.com/go-dash/_gen) fonctionnel.

Le générateur de ligne de commande est facilement installable sur Mac via [Homebrew](https://brew.sh/) : `brew install go-dash/tools/gen`

Revenons à notre premier exemple : supposons que nous avons une tranche de noms de couleurs en chaîne que nous voulons garder uniques et filtrer pour les couleurs dont la longueur est supérieure à 4 lettres. Nous pouvons enfin implémenter cela en une ligne :

Si vous aimez cette direction et souhaitez contribuer à porter le reste des fonctions utiles de Lodash vers Go, veuillez contribuer.

### Quelques réflexions finales sur la syntaxe

La principale chose qui me dérange encore avec notre syntaxe choisie est que nous avons un import par type. Est-il possible de les combiner d'une manière ou d'une autre en une seule implémentation qui routera vers le bon endroit par type ?

Considérons ce qui suit :

Ce code combine toutes les implémentations en un `Uniq` unifié qui prend `interface{}`. Bien qu'il n'utilise pas la réflexion à proprement parler, il a toujours deux casts dynamiques à l'exécution et le switch qui affecteront les performances. Nous devrions probablement faire un benchmark pour voir combien d'impact cela ajoute. Nous devrions également probablement faire un benchmark de l'implémentation par réflexion et voir si notre suspicion concernant les performances à l'exécution était effectivement fondée dès le départ.

Néanmoins, ce fut une expérience de pensée amusante.

**_Tal est un fondateur chez Orbs.com — une infrastructure de blockchain publique pour des applications grand public à grande échelle avec des millions d'utilisateurs. Pour en savoir plus et lire les livres blancs d'Orbs [cliquez ici](https://orbs.com/white-papers). [Suivez sur [Telegram](https://t.me/orbs_network), [Twitter](https://twitter.com/orbs_network), [Reddit](https://www.reddit.com/r/ORBS_Network/)]_**

**_Note : si vous êtes intéressé par la blockchain — venez contribuer ! Orbs est un projet entièrement open source où tout le monde peut participer._**

![Image](https://cdn-media-1.freecodecamp.org/images/JWn9bUEABxzB3UAy7kCsYdYnHPsCsH8cDevu)