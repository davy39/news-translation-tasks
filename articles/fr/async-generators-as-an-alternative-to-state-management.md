---
title: Les générateurs asynchrones comme alternative à la gestion d'état
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-08T19:01:32.000Z'
originalURL: https://freecodecamp.org/news/async-generators-as-an-alternative-to-state-management
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/async-state.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: software architecture
  slug: software-architecture
seo_title: Les générateurs asynchrones comme alternative à la gestion d'état
seo_desc: 'By Vitalii Akimov

  Async Generators is a simple but powerful feature that is now a part of JavaScript.
  It unlocks many new tools to improve software architecture, making it more agile,
  simplifying extension and composition.

  TL;DR


  With Async Generator...'
---

Par Vitalii Akimov

Les générateurs asynchrones sont une fonctionnalité simple mais puissante qui fait maintenant partie de JavaScript. Ils déverrouillent de nombreux nouveaux outils pour améliorer l'architecture logicielle, la rendant plus agile, simplifiant l'extension et la composition.

#### TL;DR

* Avec les générateurs asynchrones, il n'est plus nécessaire d'avoir un état de composant, des outils de gestion d'état, des méthodes de cycle de vie de composant, et même les dernières API React Context, Hooks et Suspense. C'est beaucoup plus simple à développer, maintenir et tester.
* Contrairement à une approche de gestion d'état, les générateurs asynchrones maîtrisent l'asynchronicité en laissant les mutations sans danger (si elles sont visibles uniquement dans la portée du générateur).
* Cette approche a un fond de programmation fonctionnelle.
* La persistance de l'état pour des choses comme le voyage dans le temps, les applications universelles est également disponible.
* L'article utilise React et JavaScript, mais la technique est applicable dans tout autre framework ou langage de programmation avec des générateurs (coroutines).
* _Je ne fais la publicité de mon outil qu'à la fin et très brièvement. La majeure partie de l'article concerne les générateurs asynchrones sans aucune dépendance._

![Image](https://cdn-media-1.freecodecamp.org/images/1*KlSEFFBTjyZKovSoQ0NnEw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZrJKJqBsksWd-8uKM9OvgA.png)

Commençons par une déclaration de la [page de motivation de Redux](https://redux.js.org/introduction/motivation) :

> _Cette complexité est difficile à gérer car **nous mélangeons deux concepts** très difficiles à comprendre pour l'esprit humain : **la mutation et l'asynchronicité.** Je les appelle [Mentos et Coke](https://en.wikipedia.org/wiki/Diet_Coke_and_Mentos_eruption). Les deux peuvent être formidables séparément, mais ensemble ils créent un désordre._

Redux et d'autres outils de gestion d'état se concentrent principalement sur la restriction ou le contrôle des mutations de données. Les générateurs asynchrones peuvent gérer l'asynchronicité. Cela rend les mutations sûres si elles sont visibles uniquement dans une portée de générateur particulière.

Toutes les techniques courantes de gestion d'état peuvent être divisées en deux grandes classes.

La première classe maintient un graphe de dépendances de données pour propager les changements à travers les gestionnaires — État des composants React, MobX, RxJS. Maintenir ces dépendances est une tâche complexe. Les bibliothèques sous-jacentes prennent en charge une partie de cette complexité en gérant les abonnements, en optimisant l'ordre d'exécution des gestionnaires, en les regroupant, mais cela reste parfois déroutant à utiliser, nécessitant souvent un réglage fin difficile, par exemple, avec la méthode `shouldComponentUpdate`.

Une autre approche limite la mutation à une seule cellule (stockage) (par exemple, Redux). Cela nécessite des bibliothèques beaucoup plus petites, avec moins de magie. C'est plus un modèle qu'une bibliothèque. Malheureusement, les programmes sont plus verbeux, et cela brise l'encapsulation des données. Il existe de nombreux modèles, enveloppes pour résoudre cela, mais ils rendent une approche à cellule unique plus similaire à celle basée sur un graphe.

La technique de cette histoire et Redux sont toutes deux basées sur le modèle Event Sourcing, et elles ont de nombreuses similitudes. Elle offre également des données encapsulées et un ordre déterministe synchrone d'exécutions pour les opérations avec effets de bord.

Cette approche peut être vue abstraitement comme un graphe de dépendances, mais les changements sont propagés dans le sens inverse, de sa racine vers les feuilles de son arbre couvrant. À chaque nœud, nous vérifions si la propagation doit se poursuivre vers les enfants ou non. Cela rend l'algorithme de planification très léger et facile à contrôler. Il ne nécessite aucune bibliothèque, basant uniquement sur les fonctionnalités intégrées de JavaScript.

Commençons par porter l'exemple [Redux VanillaJS counters](https://github.com/reduxjs/redux/blob/master/examples/counter-vanilla/index.html) pour illustrer l'idée.

<script async src="//jsfiddle.net/awto/uo8yvfhk/embed/"></script>

Le réducteur original est remplacé par une fonction de générateur asynchrone. La fonction calcule et stocke son état dans une variable locale. Elle renvoie également la valeur calculée, la nouvelle valeur est stockée dans le stockage singleton, et elle est visible depuis les gestionnaires d'événements. Je supprimerai ce stockage singleton dans les prochaines étapes.

Cette version ne semble pas très différente de Redux. Le générateur asynchrone pourrait être un middleware de stockage Redux. Cela viole cependant l'un des [principes](https://redux.js.org/introduction/three-principles) de Redux, à savoir le stockage de tout l'état de l'application uniquement dans le stockage. Même si le générateur n'a aucune variable locale, il a toujours son état d'exécution — la position dans le code où l'exécution est suspendue dans `yield` ou `await`.

#### Inverser les composants

Les fonctions de générateur sont des fonctions retournant des itérateurs. Nous pouvons faire avec elles tout ce que nous pouvons faire avec des fonctions simples. Par exemple, en composant des fonctions de générateur, nous pouvons diviser le calcul en plusieurs étapes indépendantes. Chaque étape a son propre état encapsulé. Chaque étape reçoit des messages qui ont été renvoyés à l'étape précédente, les traite en renvoyant un autre message et les transmet à l'étape suivante.

La charge utile des messages peut contenir des éléments VDOM. Au lieu d'avoir un arbre de composants monolithique, nous émettons des parties de celui-ci et les envoyons à l'étape suivante, où elles peuvent être assemblées ou transformées. Voici le même exemple de compteurs avec React.

<script async src="//jsfiddle.net/awto/y3x6L9wu/embed/"></script>

La fonction `pipe` est une composition de fonctions. Les fonctions prennent deux arguments. Le premier est un itérable asynchrone pour les messages de l'étape précédente. Et le second est pour envoyer un message au début du pipe. Il ne doit être appelé que depuis les gestionnaires d'événements. Cette fonction peut être remplacée bientôt par l'opérateur de pipeline intégré de JavaScript.

Lorsque nous composons des fonctions simples, la suivante dans la chaîne ne commence à s'exécuter qu'après que la précédente a terminé. Alors que pour les générateurs (et en fait n'importe quelle coroutine), l'exécution peut être suspendue et entrelacée avec d'autres fonctions. Cela rend la composition de différentes parties plus facile.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/lanes--1--1.svg)

L'exemple ci-dessus montre brièvement l'extensibilité en découplant quelques boutons de menu du composant racine dans une étape séparée. Au lieu d'abstraire les boutons de menu dans un composant séparé, il maintient un espace réservé où il injecte les composants qu'il reçoit dans les messages avec le type "MENU_ITEM". C'est une inversion de contrôle pour les composants. Les deux techniques, les composants React et ces composants inversés, peuvent bien sûr être utilisées ensemble.

#### Extension

Un point passionnant de cette technique est que rien ne doit être conçu à l'avance pour rendre le programme réutilisable et découplé. De nos jours, l'abstraction prématurée est probablement un mal plus grand que l'optimisation prématurée. Elle conduit presque certainement à un désordre surconçu impossible à utiliser. En utilisant des générateurs abstraits, il est facile de rester calme et d'implémenter les fonctionnalités requises, en divisant si nécessaire, sans penser aux extensions futures, facile à refactoriser ou à abstraire certaines parties communes après que plus de détails sont disponibles.

Redux est célèbre pour rendre les programmes plus simples à étendre et à réutiliser. L'approche de cette histoire est également basée sur l'Event Sourcing, mais il est beaucoup plus simple d'exécuter des opérations asynchrones et il n'a pas de goulot d'étranglement de stockage unique, rien ne doit être conçu prématurément.

De nombreux développeurs aiment le stockage unique car il est facile à contrôler. Le contrôle n'est pas une chose gratuite cependant. L'un des avantages largement acceptés du modèle Event Sourcing est l'absence d'une base de données centrale. Il est plus simple de changer une partie sans danger de casser autre chose. Il y a un autre problème de stockage unique discuté dans la section Persistence ci-dessous.

Il y a un article [Decouple Business Logic](https://medium.com/dailyjs/decoupling-business-logic-using-async-generators-cc257f80ab33) avec des études de cas plus détaillées. À une certaine étape, j'ai ajouté une fonctionnalité de multi-sélection au glisser-déposer sans changer quoi que ce soit dans la gestion des éléments uniques. Avec un seul stockage, cela signifierait changer son modèle de stockage d'un seul élément en cours de glisser à une liste.

Il existe des solutions similaires dans Redux, notamment l'application d'un réducteur d'ordre supérieur. Il pourrait prendre un réducteur travaillant avec un seul élément et le traduire en réducteur travaillant pour une liste. La solution des générateurs utilise des générateurs asynchrones d'ordre supérieur, prenant une fonction pour un seul élément et générant celle pour une liste. C'est similaire mais beaucoup moins verbeux, car le générateur encapsule les données et l'état de contrôle implicite.

À titre d'illustration, faisons une liste de compteurs. Cette étape est couverte dans l'article "Decouple Business Logic", je ne donne pas beaucoup de détails ici. La fonction `fork` est la fonction de transformation des itérateurs asynchrones, exécutant son argument dans des threads par élément. Ce n'est pas simple, mais c'est générique, cela fonctionne dans de nombreux contextes tel quel. Dans la section suivante, par exemple, je l'applique récursivement pour obtenir une vue en arbre.

<script async src="//jsfiddle.net/awto/0payhjvw/embed/"></script>

#### Performance

Le surcoût des générateurs asynchrones est beaucoup plus petit que pour les bibliothèques de gestion d'état. Mais il y a beaucoup de façons d'avoir des problèmes de performance ici aussi, par exemple, en inondant avec des messages. Mais il y a aussi beaucoup de façons presque sans effort pour améliorer les performances.

Dans l'exemple précédent, il y a des appels inutiles à `ReactDom.render`. C'est évidemment un problème de performance, et il y a une solution simple. Le résoudre rapidement en envoyant un autre message avec le type "FLUSH" après chaque événement diffusé. React render ne s'exécute qu'après avoir reçu ce message. Les étapes intermédiaires peuvent renvoyer ce dont elles ont besoin entre-temps.

Un autre côté génial de cette approche est que vous n'avez pas à vous soucier de la performance jusqu'à ce que ce soit un problème. Tout est structuré en petites étapes autonomes. Elles sont faciles à refactoriser, ou même sans refactorisation — de nombreux problèmes de performance peuvent être résolus en ajoutant un autre état générique dans le pipeline des étapes, par exemple, le regroupement, la priorisation, la sauvegarde de données intermédiaires, etc.

Par exemple, dans la démonstration, les éléments React construits sont sauvegardés dans des variables locales et React peut les réutiliser. Les changements sont propagés de la racine vers les feuilles, donc les optimisations comme la substitution de `shouldComponentUpdate` ne sont pas nécessaires.

#### Test

Comparé aux tests de réducteurs Redux, les générateurs s'adaptent à une stratégie de test un peu plus en boîte noire. Les tests n'ont pas accès à l'état actuel. Cependant, ils sont toujours très simples à écrire. Avec les snapshots Jest, le test peut être une liste de messages d'entrée avec comparaison de la sortie utilisant des snapshots.

```javascript
test("counterControl", async () => {
  expect.assertions(3)
  for await(const i of Counter.mainControl([
         {type:"MENU", value:<span>Menu</span>},
         {type:"VALUE", value:10},
         {type:"CONTROL", value:<span>Control</span>},
         {type:"FLUSH"},
         {type:"VALUE", value: 11},
         {type:"FLUSH"}]))
    if (i.type === "CONTROL")
      expect(renderer.create(i.value).toJSON()).toMatchSnapshot()
})
```

Si vous préférez les tests unitaires comme politique de documentation, il y a de nombreuses façons de créer une API auto-documentée pour les tests. Par exemple, une fonction `eventually`/`until` comme complément aux expressions BDD traditionnelles.

#### État persistant

Il y a une autre motivation pour Redux décrite dans l'article [You Might Not Need Redux](https://medium.com/@dan_abramov/you-might-not-need-redux-be46360cf367) par Dan Abramov — à savoir fournir un accès à l'état et il peut être sérialisé, cloné, différencié, corrigé, etc. Cela peut être utilisé pour le voyage dans le temps, le rechargement à chaud, les applications universelles et plus encore.

Pour que cela fonctionne, tout l'état de l'application doit être conservé dans le stockage Redux. De nombreuses applications Redux (même les échantillons Redux) ont une partie de l'état stockée en dehors de leur magasin. Ce sont l'état des composants, les fermetures, les générateurs ou l'état des fonctions asynchrones. Les outils basés sur Redux ne peuvent pas persister cet état.

Avoir une seule source de vérité comme un seul stockage Redux, bien sûr, rend les programmes plus simples. Malheureusement, c'est souvent impossible. Prenons par exemple une application distribuée, par exemple, les données sont partagées entre le frontend et le backend.

%[https://twitter.com/lindsey/status/575006945213485056?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E575006945213485056&ref_url=https%3A%2F%2Fmedium.com%2Fmedia%2Fd98d35ecbcc0c553da4da18f8485e6e8%3FpostId%3Df9871390ffca]

L'Event Sourcing est très réussi pour les applications distribuées. Avec les générateurs, nous pouvons écrire un proxy envoyant tous les messages entrants au côté distant et renvoyant tous les messages reçus. Il peut y avoir des pipelines séparés sur chaque pair, ou cela peut être la même application mais quelques processus en cours d'exécution. De nombreuses configurations sont faciles à mettre en place, à utiliser et à réutiliser.

Par exemple `pipe(task1, remoteTask2, task3)`. Ici `remoteTask2` peut être soit un proxy, soit il peut être défini ici, par exemple, à des fins de débogage.

Chaque partie maintient son propre état, il n'a pas besoin d'être persistant. Par exemple, si chaque tâche est implémentée par une équipe séparée, elles sont libres d'utiliser n'importe quel modèle pour l'état, de le changer à tout moment sans se soucier du travail de l'autre équipe.

Cela convient également bien pour le rendu côté serveur. Par exemple, il peut y avoir une fonction d'ordre supérieur particulière pour mettre en cache les valeurs résultantes en fonction des entrées sur le backend.

```javascript
const backend = pipe(
    commonTask1,    
    memo(pipe(         
        renderTask1,         
        renderTask2)),
    commonTask2)
```

Ici, la fonction d'ordre supérieur `memo` examine les messages entrants et peut découvrir qu'un calcul peut être réutilisé. Cela peut être une chaîne rendue côté serveur, et une étape suivante construit une réponse HTTP avec celle-ci.

Les tâches de rendu peuvent exécuter des opérations asynchrones, demandant quelque chose à distance. Pour une meilleure expérience utilisateur, nous voulons que les pages se chargent rapidement. Pour augmenter le temps de chargement initial des pages, les applications peuvent charger les composants de manière paresseuse en affichant un espace réservé de chargement au lieu du composant jusqu'à ce qu'il soit prêt. Avoir quelques composants de ce type sur une page avec un temps de chargement légèrement différent provoque des re-dispositions de page dégradant l'expérience utilisateur.

L'équipe React a récemment annoncé l'API Suspense pour résoudre ce problème. C'est une extension de React intégrée dans son moteur de rendu. Avec les composants inversés comme dans cet article, l'API Suspense n'est pas nécessaire, la solution est beaucoup plus simple et ne fait pas partie du framework UI.

Par exemple, l'application utilise des imports dynamiques pour charger des contrôles paresseux, cela peut être fait avec :

```javascript
yield {type:"LAZY_CONTROL"}
yield {type:"CONTROL", value: await import("./lazy_component")}
```

Il y a une autre étape générique suivante. Elle collecte tous les messages "LAZY_CONTROL", et attend soit que tous les messages "CONTROL" soient reçus après, soit qu'un intervalle de temps seuil. Après, elle émet des messages "CONTROL" soit avec le contrôle chargé, soit avec un espace réservé d'indicateur de chargement. Toutes les mises à jour suivantes peuvent également être regroupées en utilisant un délai spécifique pour minimiser les re-dispositions.

Un générateur peut également réorganiser les messages pour donner une plus grande priorité à l'animation qu'aux mises à jour des données du serveur. Je ne suis même pas sûr qu'il y ait besoin d'un framework côté serveur. Un petit générateur pourrait transformer la requête HTTP initiale en messages ou threads en fonction de l'URL, de la session d'authentification, etc.

#### Programmation fonctionnelle

Les outils de gestion d'état couramment utilisés ont un fond de programmation fonctionnelle. Le code de l'article ne ressemble pas à de la programmation fonctionnelle en JavaScript à cause des instructions impératives `for-of/switch/break`. Il a un concept correspondant en programmation fonctionnelle également. C'est ce qu'on appelle la notation do des monades. Par exemple, l'une de leurs utilisations en Haskell est de résoudre des problèmes comme le perçage des propriétés des composants React.

Pour garder cette histoire pratique, je ne m'écarte pas du sujet principal ici, il y a un autre article — [Using Generators as syntax sugar for side effects](https://medium.com/@vitaliy.akimov/using-generators-as-monads-do-notation-8600c53648cf).

#### Effectful.js

[Effectful.js](https://effectful.js.org/) est un pré-réglage babel implémentant la notation do fonctionnant pour toute monade sans aucune extension de syntaxe JavaScript. Il supporte également la persistance de l'état avec une implémentation de référence dans la bibliothèque [es-persist](https://github.com/awto/effectfuljs/tree/master/packages/es-persist). Par exemple, cela peut être utilisé pour convertir tous les exemples de générateurs asynchrones ci-dessus en fonctions pures.

La persistance de l'état n'est pas l'objectif principal de l'outil. Il est destiné à la description de la logique métier de haut niveau. Néanmoins, l'outil est abstrait et a de nombreux objectifs. J'écrirai plus à ce sujet bientôt.

Voici [l'exemple de résumé](https://github.com/awto/effectfuljs) sur GitHub avec toutes les fonctionnalités ci-dessus plus l'annulation/répétition automatique et le stockage de son état complet dans `localStorage`. Et voici la [version transpilée en cours d'exécution](https://effectful.js.org/demo/alternative/) (elle écrit dans le stockage local de votre navigateur mais aucune information n'est envoyée au serveur). Je ne donne pas beaucoup de détails dans cet article, il s'agit des générateurs asynchrones sans dépendance, mais je suppose que le code est simple à lire. Vérifiez par exemple [undoredo.js](https://github.com/awto/effectfuljs/blob/master/samples/persist-counters/undoredo.js) pour les détails de l'implémentation facile du voyage dans le temps.

L'exemple original nécessite presque aucune modification, j'ai seulement remplacé les promesses non sérialisables par les fonctions correspondantes de "es-persist" et remplacé les fermetures par des invocations de la fonction `R.bind` de la même bibliothèque. L'outil EffectfulJS a un autre transpileur pour rendre toutes les fonctions, y compris les fermetures, sérialisables, mais il n'est pas utilisé dans cet exemple pour le garder plus simple.

L'histoire n'est qu'une brève description de la technique. Je l'utilise depuis quelques années déjà, et je suis heureux grâce aux améliorations qu'elle apporte. Essayez-la, et je suis sûr que vous l'apprécierez aussi. Il y a beaucoup de choses à décrire en profondeur. Restez à l'écoute !