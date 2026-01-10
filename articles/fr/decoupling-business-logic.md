---
title: Comment découpler la logique métier en utilisant les générateurs asynchrones
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-20T11:26:28.000Z'
originalURL: https://freecodecamp.org/news/decoupling-business-logic
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca159740569d1a4ca4e17.jpg
tags: []
seo_title: Comment découpler la logique métier en utilisant les générateurs asynchrones
seo_desc: 'By Vitalii Akimov

  Async generators are new in JavaScript. They are a remarkable extension. They provide
  a simple but very powerful tool for splitting programs into smaller parts, making
  sources easier to write, read, maintain and test.

  The article sh...'
---

Par Vitalii Akimov

Les générateurs asynchrones sont une nouveauté en JavaScript. Ils constituent une extension remarquable. Ils fournissent un outil simple mais très puissant pour diviser les programmes en parties plus petites, rendant les sources plus faciles à écrire, lire, maintenir et tester.

L'article montre cela à travers un exemple. Il implémente un composant typique de front-end, à savoir les opérations de glisser-déposer. La même technique n'est pas limitée au front-end. Il est difficile de trouver où elle ne peut pas être appliquée. J'utilise la même technique dans deux grands projets de compilateurs, et je suis très excité de voir à quel point cela simplifie les choses.

Le résultat final est un jouet, mais la plupart du code là-bas est utilisable dans une application réelle. Le seul objectif de l'article est de montrer comment diviser le programme en parties indépendantes plus petites en utilisant des fonctions de générateurs asynchrones. Ce n'est pas un article sur la façon d'implémenter le glisser-déposer.

Il y a une [démo transpilée](https://effectful.js.org/demo/decoupling/) de ce que nous obtiendrons à la fin de la journée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uSfRm31oD_2bgNgYt-Hfaw.gif)

Vous pouvez faire glisser des boîtes depuis une palette en haut et les déposer dans l'une des zones grises. Chaque zone de dépôt a ses actions spécifiques. Quelques éléments peuvent être sélectionnés. Ceux en jaune ont un mouvement inertiel.

Toutes les fonctionnalités sont indépendantes. Elles sont divisées en étapes pour chaque fonctionnalité. Elles sont simples à activer, désactiver, développer, tester et déboguer séparément. Plusieurs développeurs ou équipes pourraient travailler productivement en parallèle.

Je suppose une connaissance très basique des générateurs asynchrones (ou au moins des fonctions asynchrones et des générateurs séparément) et quelques fondamentaux du DOM HTML (au moins savoir ce que c'est). Il n'y a pas de dépendances aux bibliothèques ou frameworks JavaScript tiers, mais la même technique peut être utilisée avec n'importe lequel d'entre eux.

Pour la démo, prétendons que nous ne connaissons pas l'ensemble complet des exigences et ajoutons une nouvelle fonctionnalité seulement après avoir terminé quelque chose et que cela fonctionne. Jouer avec un logiciel déjà fonctionnel à des étapes intermédiaires stimule généralement la créativité. C'est l'un des principaux composants du cœur du développement agile de logiciels - mieux vaut écrire quelque chose de non parfaitement conçu mais fonctionnel d'abord. Ensuite, nous pouvons toujours l'améliorer en utilisant le refactoring. Les générateurs asynchrones aideront.

Au début de tout projet, je ne veux pas passer de temps à choisir le bon framework, la bonne bibliothèque ou même une architecture. Je ne veux pas surconcevoir. Avec l'aide des itérateurs asynchrones, je peux reporter les décisions difficiles à un moment où j'ai assez de connaissances pour faire un choix. Plus je prends une option tôt, plus il y a de chances de faire des erreurs. Peut-être que je n'aurai besoin de rien du tout.

Je vais décrire seulement quelques étapes. Les autres étapes sont petites et peuvent être lues directement depuis le code sans effort. Elles ne sont qu'une question de travail avec le DOM.

#### Générateurs asynchrones

Tous les exemples partagent les sources du nano-framework. Il est développé une fois, au début et copié-collé sans aucun changement. Dans le projet réel, ce sont des modules séparés, importés dans d'autres modules si nécessaire. Le framework ne fait qu'une seule chose. Il convertit les événements DOM en éléments d'itérateur asynchrone.

Les itérateurs asynchrones ont la même méthode `next` que les itérateurs ECMAScript simples, mais ils retournent une Promesse qui se résout en objets avec les champs `value`, `done`.

Les générateurs asynchrones combinent la fonctionnalité des fonctions asynchrones et des générateurs. Dans le corps de telles fonctions, nous pouvons utiliser `await` avec des expressions `yield`, et ils font exactement ce que ces expressions font dans les fonctions asynchrones et les générateurs, respectivement. À savoir, ils suspendent le contrôle d'exécution jusqu'à ce que la Promesse dans l'argument `await` soit résolue, et pour `yield`, ils sortent une valeur et suspendent jusqu'à ce que l'appelant demande la valeur suivante.

Voici l'implémentation du nano-framework, avec la première version de la logique métier (monolithique pour l'instant) :

<script async src="//jsfiddle.net/awto/afjs2467/embed/js,html,result/dark/"></script>

C'est un exemple fonctionnel, appuyez sur **Result** pour le voir en action. Il y a quatre éléments que vous pouvez faire glisser dans la page. Les principaux composants sont `send`, `produce` et `consume`. L'application s'abonne aux événements DOM et les redirige dans le framework en utilisant la fonction `send`. La fonction convertit les arguments en éléments de l'itérateur asynchrone retourné par l'appel `produce`. L'itérateur ne se termine jamais et est appelé au niveau supérieur d'un module.

Il y a une boucle `for(;;)` dans `produce`. Je sais, cela semble suspect, vous pouvez même l'avoir refusé dans votre liste de contrôle de révision de code d'équipe ou par une règle de lint. Pour la lisibilité du code, nous voulons bien sûr que la condition de sortie des boucles soit évidente. Mais cette boucle ne doit jamais sortir, car elle est censée être infinie. Elle ne consomme pas de cycles CPU puisque la plupart du temps elle dormira dans les expressions `await` et `yield`.

Il y a aussi la fonction `consume`. Elle lit n'importe quel itérateur asynchrone dans son argument, ne faisant rien avec les éléments, ne retournant jamais. Nous en avons besoin pour garder notre framework en cours d'exécution.

```javascript
async function consume(input) {  
    for await(const i of input) {}
}
```

C'est une fonction asynchrone (pas un générateur), mais elle utilise la nouvelle instruction `for-await-of`, une extension de l'instruction `for-of`. Elle lit les itérateurs asynchrones, plutôt que l'itérateur ECMAScript original, et attend chaque élément. Son implémentation simplifiée pourrait transpiler le code `consume` original en quelque chose comme ceci :

```javascript
async function consume(input) {
    const iter = input[Symbol.asyncIterator]()    
    for(let i;(i = await iter.next()).done;) {}
}
```

La fonction `main` est le point d'entrée de la logique métier de l'application. La fonction est appelée entre `produce` et `consume` au niveau supérieur du module.

```javascript
consume(main(produce()))
```

Il y a aussi une petite fonction `share`. Nous en avons besoin pour utiliser le même itérateur dans quelques instructions `for-await-of`.

La première version monolithique de la logique métier est entièrement définie dans `main`. C'est une première version de brouillon, mais la puissance des générateurs asynchrones est déjà visible. L'état de l'application (où nous avons commencé à faire glisser les variables `x`, `y`) est juste des variables locales simples, encapsulées à l'intérieur de la fonction.

Outre l'état des données, il y a aussi l'état de contrôle d'exécution. C'est une sorte de variable locale implicite stockant la position où le générateur est suspendu (soit sur `await` ou `yield`). Bien que la vraie magie commence lorsque nous commençons à diviser le `main`.

#### Division

La combinaison de fonctions la plus souvent utilisée est leur composition : par exemple, pour les fonctions `f` et `g`, une composition de deux fonctions est `a => f(g(a))`.

Si nous composons des fonctions simples, la suivante commence à faire son travail seulement après que la précédente existe. Si ce sont des générateurs en cours d'exécution, leur exécution est entrelacée.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/lanes--1-.svg)
_Composition de fonctions_

Quelques fonctions génératrices composées font un pipeline parallèle. Comme dans tout processus de fabrication, par exemple les voitures, la division des tâches en quelques étapes utilisant une chaîne de montage augmente considérablement la productivité. De même, dans le pipeline basé sur les générateurs asynchrones, une fonction peut envoyer des messages à la suivante en utilisant les valeurs que son itérateur de résultat produit. La fonction suivante peut faire quelque chose de spécifique à l'application en fonction du contenu du message ou le transmettre à l'étape suivante.

Ces fonctions d'étape sont le composant de la logique métier. Plus formellement, ce sont des fonctions JavaScript, prenant un itérateur asynchrone comme paramètre et retournant un autre itérateur asynchrone comme résultat. Dans la plupart des cas, ce sera une fonction génératrice asynchrone, mais pas nécessairement.

Il y a beaucoup de noms couramment utilisés pour de telles fonctions maintenant. Par exemple, Middleware, Epic, etc. J'aime le nom Transducer et l'utiliserai dans l'article.

Les transducteurs sont libres de faire ce qu'ils veulent avec le flux d'entrée. Voici des exemples de ce que cela peut être :

* transmettre le message à l'étape suivante (avec `yield i`)
* changer quelque chose et transmettre à la suivante (`yield {
...i,one:1}`)
* générer un nouveau message (`yield {type:
"two
",two:2})`
* ne rien produire du tout, filtrant ainsi le message
* tamponner les messages dans un tableau et les sortir sur une condition (`yield* buf`), par exemple, retarder le début du glisser pour éviter une fausse réponse
* effectuer des opérations asynchrones (`await query()`)

Les transducteurs écoutent principalement les messages entrants dans les boucles `for-await-of`. Il peut y avoir quelques boucles de ce type dans un seul corps de transducteur. Cela utilise l'état de contrôle d'exécution pour implémenter certaines exigences de la logique métier.

Voyons comment cela fonctionne. Nous allons diviser la fonction `main` monolithique de l'exemple ci-dessus en deux étapes. L'une convertit les événements DOM en messages de glisser-déposer — `makeDragMessages` (types `"dragstart"`, `"dragging"`, `"drop"`) et l'autre met à jour les positions DOM — `setPositions`. La fonction `main` est juste une composition des deux.

<script async src="//jsfiddle.net/awto/ms9txpuq/embed/"></script>

Je divise le programme ici parce que je veux insérer quelques nouveaux gestionnaires de messages entre eux. C'est la même chose que lors de l'écriture d'un nouveau logiciel, je ne me concentrerais pas trop sur la façon de diviser correctement le code avant de comprendre pourquoi j'en avais besoin. Il doit satisfaire une contrainte de taille raisonnable. Ils doivent également être séparés sur des fonctionnalités logiquement différentes.

La fonction `main` là-bas est en fait aussi un transducteur (prend un itérable asynchrone et retourne un itérable asynchrone). C'est un exemple de transducteur qui n'est pas un générateur asynchrone lui-même. Une application plus grande peut injecter `main` de ce module dans d'autres pipelines.

C'est la version finale du nano-framework. Rien n'est à changer là-bas, quelle que soit la nouvelle fonctionnalité que nous ajoutons. Les nouvelles fonctionnalités sont des fonctions spécifiées quelque part dans la chaîne dans `main`.

#### Premières fonctionnalités

Maintenant, revenons à la création de quelque chose de nouveau. Juste faire glisser quelque chose sur une page n'est pas suffisant. Nous avons des noms de messages spéciaux pour le glisser (`"dragstart"`, `"dragging"`, `"drop"`). Ensuite, les transducteurs peuvent les utiliser à la place des événements souris/tactiles. Par exemple, nous pouvons ajouter un support clavier, sans changer quoi que ce soit pour cela.

Créons un moyen de créer de nouveaux éléments glissables, une zone d'où nous pouvons les faire glisser, et quelque chose pour les supprimer. Nous allons aussi l'agrémenter avec une animation lors du dépôt d'un élément dans la zone de corbeille ou en dehors de toute zone.

<script async src="//jsfiddle.net/awto/Lrn10smc/embed/"></script>

Tout d'abord, tout commence avec le transducteur `palette`. Il détecte le début du glisser sur l'un de ses éléments, le clone dans un nouvel élément, et remplace tous les événements de glisser originaux après avec le clone. C'est absolument transparent pour tous les transducteurs suivants. Ils ne savent rien de la palette. Pour eux, c'est comme une autre opération de glisser d'un élément existant.

Ensuite, le transducteur `assignOver` ne fait rien de visible pour l'utilisateur final, mais il aide les transducteurs suivants. Il détecte les éléments HTML sur lesquels un utilisateur fait glisser un élément et les ajoute à tous les messages en utilisant la propriété `over`. L'information est utilisée dans les transducteurs `trash` et `validateOver` pour décider si nous devons supprimer l'élément ou annuler le glisser. 

Les transducteurs ne le font pas eux-mêmes mais envoient plutôt des messages `"remove"` ou `"dragcancel"` pour être traités par quelque chose ensuite. Le message d'annulation est converti en `"remove"` par `removeCancelled`. Et les messages `"remove"` sont finalement traités dans `applyRemove` en les supprimant du DOM.

En introduisant un autre type de message, nous pouvons injecter de nouvelles implémentations de fonctionnalités au milieu sans remplacer quoi que ce soit dans le code original. Dans cet exemple, c'est l'animation. Sur `"dragcancel"`, l'élément revient à sa position d'origine, et sur `"remove"`, sa taille est réduite à zéro. Activer/désactiver l'animation est juste une question de suppression/insertion de transducteurs à une position spécifique.

L'animation continuera à fonctionner si quelque chose d'autre génère `"dragcancel"` ou `"remove"`. Nous pouvons arrêter de penser à où l'appliquer. Notre logique métier devient plus haut niveau.

L'implémentation de l'animation utilise également des générateurs asynchrones mais pas sous la forme de transducteurs. C'est une fonction qui retourne des valeurs de zéro à un dans les frames d'animation avec un délai spécifié, qui par défaut est de 200ms. Et la fonction appelante l'utilise de la manière qui lui plaît. Vérifiez la fonction de démo `animRemove` dans le fiddle ci-dessus.

De nombreuses autres options d'animation sont simples à ajouter. Les valeurs peuvent ne pas être linéaires mais sorties avec une fonction spline. Ou elles peuvent être basées non pas sur le délai mais sur la vitesse. Cela n'est pas significatif pour les fonctions invoquant `anim`.

#### Multi-sélection

Maintenant, ajoutons progressivement une autre fonctionnalité. Nous commençons à partir de zéro, à partir du nano-framework. Nous fusionnerons toutes les étapes à la fin sans effort. De cette façon, le code de l'étape précédente n'interférera pas avec le nouveau développement. Il est beaucoup plus facile de déboguer et d'écrire des tests pour cela. Il n'y a pas non plus de dépendances indésirables.

La prochaine fonctionnalité est une multi-sélection. Je la mets en avant ici parce qu'elle nécessite une autre combinaison de fonctions d'ordre supérieur. Mais au premier abord, elle semble simple à implémenter. L'idée est de simuler des messages de glisser pour tous les éléments sélectionnés lorsqu'un utilisateur fait glisser l'un d'eux.

L'implémentation est très simple mais elle rompt les étapes suivantes dans le pipeline. Certains transducteurs (comme `setPosition`) s'attendent à une séquence exacte de messages. Pour un seul élément, il devrait y avoir `"dragstart"` suivi de quelques `"dragging"` et un `"drop"` à la fin. Ce n'est plus vrai.

Un utilisateur fait glisser plusieurs éléments en même temps. Il y aura donc maintenant des messages pour plusieurs éléments simultanément. Il n'y a qu'une seule coordonnée de départ dans les variables locales `x` et `y` de `setPosition`. Et son flux de contrôle est défini pour un seul élément. Après `"dragstart"`, il est dans la boucle imbriquée. Il ne reconnaît aucun `"dragstart"` suivant jusqu'à ce qu'il quitte cette boucle sur `"drop"`.

Le problème peut être résolu en recourant au stockage de l'état, y compris un état de contrôle, dans une sorte de carte pour chaque élément actuellement en cours de glisser. Cela briserait bien sûr tous les avantages des générateurs asynchrones. J'ai également promis qu'il n'y aurait aucun changement dans le nano-framework. Ce n'est donc pas la solution.

Ce dont nous avons besoin ici, c'est d'exécuter des transducteurs s'attendant à travailler avec un seul élément dans une sorte de thread séparé. Il y a une fonction `byElement` pour cela. Elle multiplexe l'entrée dans quelques instances d'un transducteur passé comme argument. Les instances sont créées en appelant le transducteur dans l'argument en fournissant son itérateur source filtré. Chaque source pour chaque instance ne sort que des messages avec le même champ `element`. Les sorties de toutes les instances sont fusionnées en un seul flux. Tout ce que nous avons à faire est d'envelopper les transducteurs avec `byElement`.

<script async src="//jsfiddle.net/awto/pykuduLf/embed/"></script>

Tout d'abord, il convertit les événements DOM en messages spécifiques à l'application dans `makeSelectMessages`. La deuxième étape ajoute un indicateur de sélection et met en surbrillance les éléments sélectionnés après la fin des sélections dans `selectMark`. Rien de nouveau dans les deux premières. Le troisième transducteur vérifie si un utilisateur fait glisser un élément mis en surbrillance. Si c'est le cas, il obtient tous les autres éléments mis en surbrillance et génère des messages de glisser-déposer pour chacun d'eux dans `propagateSelection`. Ensuite, `setPosition` s'exécute dans un thread par élément.

#### Résultat final

Après que la fonctionnalité de multi-sélection est implémentée, c'est fait une fois pour toutes. Les autres fonctionnalités fonctionnent automatiquement avec elle. Tout ce que nous devons changer est de l'ajouter à `main` et d'envelopper correctement les autres transducteurs avec `byElement` si nécessaire. Cela peut être fait soit dans `main`, soit dans un module où les transducteurs sont importés.

Voici le fiddle avec la démo finale avec toutes les fonctionnalités fusionnées :

<script async src="//jsfiddle.net/awto/up398xzh/embed/"></script>

Tous les transducteurs sont en fait des threads très légers. Contrairement aux vrais threads, ils sont déterministes mais ils utilisent des événements DOM non déterministes comme source. Ils doivent donc être considérés comme non déterministes également.

Cela rend tous les problèmes typiques des environnements multi-threads possibles, malheureusement. Ce sont les courses, les blocages, les séquences, etc. Heureusement, ils sont simples à éviter. Il suffit de ne pas utiliser de données partagées mutables.

Je viole cette contrainte dans la démo en interrogeant et en mettant à jour l'arbre DOM. Cela ne conduit pas à des problèmes ici, mais dans une application réelle, c'est quelque chose à prendre en compte. Pour corriger cela, certaines étapes initiales peuvent lire tout ce qui est nécessaire depuis un DOM et l'emballer dans des messages. L'étape finale peut effectuer certaines mises à jour du DOM basées sur les messages reçus. Cela peut être un rendu de DOM virtuel, par exemple.

Communiquer uniquement avec les messages permet d'isoler encore plus le thread. Cela peut être un Web Worker, ou même un serveur distant.

Mais encore une fois, je ne m'inquiéterais pas avant que cela ne devienne un problème. Grâce aux itérateurs asynchrones, le programme est un ensemble de petits composants isolés et autonomes. Il est simple de changer quoi que ce soit lorsque (si) il y a un problème.

La technique est compatible avec d'autres techniques de conception. Elle fonctionnera pour la POO ou la PF. Tout modèle de conception classique s'applique. Lorsque la fonction `main` devient grande, nous pouvons ajouter une injection de dépendances pour gérer le pipeline, par exemple.

La technique réduit les soucis concernant les architectures des applications. Il suffit d'écrire un transducteur spécifique pour chaque fonctionnalité que vous devez implémenter. Abstraire les parties communes en transducteurs autonomes. Divisez-le en quelques-uns si quelque chose d'autre doit être fait au milieu. Généralisez certaines parties en combinateurs réutilisables abstraits seulement lorsque (si) vous avez assez de connaissances pour cela.

#### Relation avec d'autres bibliothèques

Si vous êtes familier avec les node-streams ou les bibliothèques réactives fonctionnelles telles que [RxJS](http://reactivex.io/rxjs/), vous pouvez probablement déjà repérer de nombreuses similitudes. La seule différence est l'interface utilisée pour les flux.

Les transducteurs n'ont pas besoin d'être des générateurs asynchrones. C'est juste une fonction prenant un flux et retournant un autre flux, quelle que soit l'interface du flux. La même technique pour diviser la logique métier peut être appliquée à d'autres interfaces de flux. Les générateurs asynchrones fournissent simplement une excellente extension de syntaxe pour eux.

Si vous êtes familier avec [Redux](https://redux.js.org/), vous pouvez remarquer que les gestionnaires de messages sont très similaires à la composition des middlewares ou des réducteurs. Les itérateurs asynchrones peuvent également être convertis en middleware Redux. Quelque chose comme ceci, par exemple, est fait dans la bibliothèque [redux-observable](https://github.com/redux-observable/redux-observable) mais pour une interface de flux différente.

Cependant, cela viole les [principes de Redux](https://redux.js.org/docs/introduction/ThreePrinciples.html). Il n'y a plus de stockage unique. Chaque générateur asynchrone a son propre état encapsulé. Même s'il n'utilise pas de variables locales, l'état est toujours là. C'est l'état de contrôle actuel et la position dans le code où le générateur a été suspendu. L'état n'est également pas sérialisable.

Le framework s'intègre bien avec les modèles sous-jacents de Redux, comme [Event Sourcing](https://martinfowler.com/eaaDev/EventSourcing.html). Nous pouvons avoir un type spécifique de message propageant certaines diffs d'état global. Et les transducteurs peuvent réagir en conséquence, mettant probablement à jour leurs variables locales si nécessaire.

Le nom, transducteur, est généralement associé aux [transducteurs de style Clojure](https://clojure.org/reference/transducers) dans le monde JavaScript. Les deux sont les mêmes choses à un niveau supérieur. Ils sont à nouveau simplement des transformateurs d'objets de flux avec différentes interfaces. Bien que les transducteurs Clojure transforment les consommateurs de flux, les transducteurs d'itérateurs asynchrones de cet article transforment les producteurs de flux. Un peu plus de détails peuvent être trouvés [ici](https://medium.com/@vitaliy.akimov/simpler-transducers-for-javascript-4d02a0926648).

#### Extensions

Je travaille maintenant sur un transpileur pour [l'intégration d'effets en JavaScript](https://github.com/awto/effectfuljs). Il peut gérer les extensions de syntaxe de fonctions asynchrones, de générateurs et de générateurs asynchrones ECMAScript pour surcharger le comportement par défaut.

En fait, la démo transpilée ci-dessus a été construite avec. Contrairement à des outils similaires comme regenerator, il est abstrait. Tout autre effet peut être intégré de manière transparente dans le langage en utilisant une bibliothèque implémentant son interface abstraite. Cela peut simplifier considérablement les programmes JavaScript.

Par exemple, les applications possibles sont :

* des effets standard plus rapides,
* sauvegarder l'exécution actuelle dans un fichier ou une base de données et la restaurer sur un serveur différent ou récupérer après une panne matérielle,
* déplacer le contrôle entre le front-end et le back-end,
* lors de la modification des données d'entrée, réexécuter uniquement la partie pertinente du programme, utiliser des transactions, appliquer des techniques de programmation logique, même les principes Redux pour les générateurs asynchrones peuvent être récupérés.

L'implémentation du compilateur elle-même utilise la technique décrite dans l'article. Il utilise des générateurs non asynchrones puisqu'il n'a pas de source de messages asynchrones. L'approche a considérablement simplifié la version précédente du compilateur faite avec des Visiteurs. Il a maintenant presque cent options. Leur implémentation est presque indépendante, et il est toujours simple à lire et à étendre.