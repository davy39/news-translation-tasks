---
title: Comment penser de manière réactive et animer des objets en mouvement avec RxJs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-08T10:50:52.000Z'
originalURL: https://freecodecamp.org/news/thinking-reactively-how-to-animate-with-movement-objects-using-rxjs-692518b6f2ac
coverImage: https://cdn-media-1.freecodecamp.org/images/1*a3UqVMQj_k0k0gBUMRkbng.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment penser de manière réactive et animer des objets en mouvement avec
  RxJs
seo_desc: 'By Enrico Piccinin

  These days, many software systems have to deal with asynchronous behaviors and time-related
  issues.

  Continuous connectivity, distributed systems, microservices-based architectures,
  the cloud, non blocking platforms — the consequenc...'
---

Par Enrico Piccinin

De nos jours, de nombreux systèmes logiciels doivent gérer des comportements asynchrones et des problèmes liés au temps.

La connectivité continue, les systèmes distribués, les architectures basées sur les microservices, le cloud, les plateformes non bloquantes — la conséquence de toutes ces choses est que nous devons d'une manière ou d'une autre gérer l'asynchronicité et le temps. Nos systèmes logiciels doivent apprendre à gérer des flux d'événements, qui sont par nature asynchrones.

La programmation réactive fournit des outils puissants, basés sur un style de programmation fonctionnelle, qui nous aident à modéliser des systèmes qui fonctionnent dans un tel monde. Mais ces systèmes nous obligent à penser de manière réactive lorsque nous concevons nos solutions.

Penser de manière réactive représente souvent un défi, comme tout changement de perspective. En même temps, cela peut être plus facile que vous ne le pensez. Il suffit de regarder ce qui se passe dans le monde réel et d'essayer de le mapper de manière simple.

Dans cet article, je vise à vous montrer comment appliquer la pensée réactive et fonctionnelle pour résoudre un problème très connu de manière naturelle : comment animer un objet avec un mouvement contrôlé. La métaphore que j'utiliserai est celle d'un véhicule qui peut accélérer et freiner, en suivant les commandes émises par une télécommande.

Dans l'implémentation, nous utiliserons RxJs, la version JavaScript de ReactiveX, et TypeScript.

Le code pour une implémentation complète de démonstration peut être trouvé [ici](https://github.com/EnricoPicci/mobile-object-observables).

Si vous aimez cela, [voici un second article](https://medium.com/@enrico.piccinin/reactive-thinking-how-to-design-a-distributed-system-with-rxjs-websockets-and-node-57d772f89260) autour de ces thèmes.

### Un rapide rappel des bases simples de la dynamique

Si vous voulez changer la vitesse d'un objet, vous devez appliquer une force qui imprime une accélération à cet objet. Si vous connaissez la valeur de l'accélération **A** de l'objet, vous pouvez calculer la variation de sa vitesse **dV** dans un certain intervalle de temps **dT** avec la formule

**_dV = A * dT_**

De même, si vous connaissez la vitesse **V**, alors vous pouvez calculer la variation dans l'espace **dS** dans un intervalle de temps **dT** avec la formule

**_dS = V * dT_**

Conclusion : si vous avez une accélération **A** appliquée à un objet dont la vitesse initiale est **V0**, vous pouvez approximer la vitesse de l'objet dans l'intervalle de temps **dT** avec sa moyenne, comme ceci :

**_averageVel = (V0 + V1) / 2 = (V0 + V0 + dV) / 2 = V0 + A/2 * dT_**

et ensuite calculer la variation approximative de l'espace **dS** dans le même intervalle **dT** avec la formule

**_dS = averageVel * dT = V0 * dT + A/2 * dT²_**

Plus l'intervalle de temps **dT** est court, meilleure est l'approximation.

### Ce que signifie "animer un objet avec mouvement"

Si nous voulons animer un objet avec un mouvement contrôlé par l'accélération (c'est-à-dire si nous voulons simuler comment un objet se déplacerait s'il était soumis à des forces), nous devons introduire la dimension du temps.

Nous devons diviser le temps en intervalles, dT, calculer l'espace parcouru pour chaque dT, et montrer la nouvelle position à chaque intervalle.

#### Utilisation de l'approche PULL — demander des informations

Nous pouvons utiliser la fonction ci-dessus et **extraire** les informations dont nous avons besoin (combien l'objet s'est déplacé pendant le dernier intervalle de temps **dT** étant donnée une certaine accélération **A** et une vitesse initiale **V**). Nous prendrions le résultat de la fonction et l'utiliserions pour calculer la nouvelle position, tant que nous sommes capables de nous souvenir d'une manière ou d'une autre de la position précédente.

Si nous nous basons sur une approche pull, c'est l'appelant (le composant logiciel) qui appelle la fonction qui fait la majeure partie du travail. Il conserve et met à jour l'état, contrôle le temps et gère l'ensemble du mouvement.

#### **La manière réactive : l'approche PUSH (et commande)**

Si vous pensez à un véhicule contrôlé à distance par quelqu'un, vous imaginerez probablement que :

* le véhicule transmet à une fréquence régulière sa position et sa vitesse au contrôleur
* le contrôleur peut changer l'accélération du véhicule (le braquage et le freinage ne sont que des changements d'accélération le long de l'axe de l'espace) pour guider le mouvement du véhicule

![Image](https://cdn-media-1.freecodecamp.org/images/xMJxr0MCDKLyK2hdk2SlSGeAoCC76IlmF6M1)

Une telle approche a l'avantage de séparer clairement les responsabilités :

1. le véhicule est responsable de la transmission de son état à tout moment à toute partie intéressée
2. le contrôleur est responsable de l'écoute des données transmises par le véhicule et de l'émission des bonnes commandes

La programmation réactive fournit les outils pour construire une solution logicielle à ce problème en reflétant exactement ce modèle. C'est probablement ce à quoi vous vous attendriez dans le monde réel :

* un véhicule qui transmet les détails de sa dynamique (par exemple, vitesse, position, direction) — l'Observable
* un contrôleur qui écoute ces transmissions et émet des commandes pour accélérer, décélérer, diriger et freiner — l'Observer

### Implémentation réactive — RxJs

Pour développer la solution, nous utilisons TypeScript comme langage de programmation et le modèle ReactiveX via l'implémentation RxJs. Mais les concepts peuvent être facilement transposés à de nombreux autres langages supportés par ReactiveX.

#### **La classe MobileObject — une représentation des objets qui se déplacent dans l'espace**

Nous allons construire notre simulateur en utilisant des techniques réactives avec un style de programmation fonctionnelle. Mais nous utiliserons toujours de bons vieux concepts orientés objet (OO) pour construire un cadre clair pour notre implémentation. Commençons donc par la classe MobileObject :

```typescript
export class MobileObject {

}
```

Cette classe représentera les objets qui transmettent à intervalles réguliers toutes les données pertinentes sur leur dynamique, comme la vitesse, la position et l'accélération. Au sein de cette classe, nous travaillerons de manière réactive.

#### Présentons M. Observable, le cœur de notre MobileObject

Comme nous le savons, pour être contrôlé à distance, un véhicule doit transmettre en continu à son contrôleur des données sur lui-même, à savoir :

* sa vitesse actuelle
* sa position actuelle
* combien sa position et sa vitesse ont varié depuis le dernier intervalle de temps

Ce n'est qu'un **flux de données dans le temps** émis par le véhicule. L'**Observable** de ReactiveX est un moyen de modéliser des **flux d'événements transportant des données dans le temps**. Nous pouvons donc utiliser des Observables pour modéliser les données transmises par notre véhicule.

#### **Notre horloge : une séquence d'intervalles de temps**

La première chose dont nous avons besoin est de créer une séquence d'intervalles de temps. Chaque événement émis dans cette séquence connaît le temps écoulé depuis son prédécesseur, comme illustré dans le diagramme suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/ahrBFMkgyRbltV-TnWmVL9aMM0HOwf3ZsEqP)
_Notre horloge : une séquence d'intervalles de temps_

Avec RxJs, nous pouvons créer une telle **horloge** avec un Observable en utilisant la fonction suivante :

```typescript
private buildClock(frameApproximateLenght: number) {
  let t0 = Date.now();
  let t1: number;
  return Observable.timer(0, frameApproximateLenght)
    .do(() => t1 = Date.now())
    .map(() => t1 - t0)
    .tap(() => t0 = t1)
    .share();
}
const clock = buildClock(xxx);
```

Appelons cet observable **_clock_**. Notre **_clock_** émet approximativement toutes les _xxx_ millisecondes. Chaque événement émis par **_clock_** portera le nombre exact de millisecondes écoulées depuis l'émission précédente.

Nous verrons plus tard, en parlant des frames d'animation, pourquoi cette méthode pour créer un observable d'intervalles de temps est pratique. Plus tard, nous aborderons également pourquoi il est important d'utiliser l'opérateur `share` lors de la création de **_clock_**.

#### **Calculer la variation de vitesse et d'espace dans un intervalle de temps**

Supposons que MobileObject est soumis à une accélération **A**. Maintenant que nous avons une **_clock_**, nous pouvons calculer la variation de vitesse **dV** en utilisant la formule **dV = A * dT**. En utilisant cette formule et l'opérateur `map` de RxJs, nous pouvons créer un Observable qui émet la variation de vitesse dans le temps :

![Image](https://cdn-media-1.freecodecamp.org/images/izVvKH1QuAKcn-91IPyl1fY9qBv5d2k4h8H3)
_Variation de vitesse comme une séquence d'événements dans le temps_

Si nous stockons dans une variable `vel` la vitesse à l'instant _tX_, nous pouvons calculer la variation approximative dans l'espace à l'intervalle de temps suivant _t(X+1)_ avec la formule **dS = vel * dT + A / 2 * dT²**. Encore une fois, en utilisant l'opérateur `map`, nous pouvons obtenir un Observable qui émet la variation de l'espace dans le temps.

![Image](https://cdn-media-1.freecodecamp.org/images/aSBleP5jlzAajO2KZlTPJFs7v91LmCTnzIzI)
_Variation de l'espace comme une séquence d'événements dans le temps_

En utilisant la même approche, nous pouvons construire un observable qui émet à chaque tick de **_clock_** toutes les informations pertinentes sur la dynamique de MobileObject, en partant simplement de son accélération **A**. Nous appelons cet observable **_dynamics_**. 

![Image](https://cdn-media-1.freecodecamp.org/images/fxt4zKEqeOh91UekArw663MwbqkMZ3y5QgT9)

**Mais l'accélération peut changer — alors quoi ?**

Cela fonctionne si nous connaissons l'accélération **A** et si **A** est une constante.

Que se passe-t-il si l'accélération change dans le temps ? Peut-être commençons-nous avec une accélération **A0**, puis après une période de temps **P0**, une force la change en **A1**, puis après **P1**, elle change en **A2**, puis en **A3**, comme dans le diagramme suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/NlTiHdfTk2bnKTEZe3ivmx4QWWDO8qdM9anG)
_Accélération dans le temps comme un observable_

**_acceleration_** ressemble à un Observable, n'est-ce pas ? Chaque événement représente un changement dans l'accélération de MobileObject (c'est-à-dire le fait qu'une nouvelle force a été appliquée à MobileObject).

Connaissant **A0**, nous pouvons calculer la vitesse et la position de MobileObject pour la période **P0** en utilisant un observable **_dyn0_**, construit selon la logique décrite ci-dessus. Lorsque l'accélération change, nous pouvons toujours calculer la vitesse et la position, mais nous devons abandonner **_dyn0_** et `**_switcher_**` vers un nouvel Observable **_dyn1_**, qui est construit avec la même logique que **_dyn0_**, mais en utilisant maintenant la nouvelle accélération **A1**. Le même changement est répété lorsque l'accélération devient **A2** puis **A3**.

![Image](https://cdn-media-1.freecodecamp.org/images/xZFwskoz-QaNZv7pLtXmMsy525c1KA7JXZEy)
_Changer d'observable lorsque l'accélération change_

C'est là que l'opérateur `switchMap` est utile. Via `switchMap`, nous pouvons transformer l'observable **_acceleration_** en une nouvelle version de l'observable **_dynamics_**. Il peut recevoir une nouvelle valeur émise par **_acceleration_**, démarrer un nouvel observable **dynX**, compléter l'observable précédent **_dynX-1_**, et émettre tous les événements générés par les divers observables de type **_dynX_** qu'il a créés pendant ce traitement. Le diagramme suivant illustre le mécanisme `switchMap`.

![Image](https://cdn-media-1.freecodecamp.org/images/UWDKevUFEvJw5uFGQMP4yoQZ1DL9z8thhq-v)

#### Bienvenue maintenant à M. Subject — la pédale d'accélérateur de MobileObject

Pour que cela fonctionne, nous devons créer la pédale d'accélérateur. C'est un mécanisme qui permet aux **contrôleurs** externes de changer l'accélération de MobileObject.

**L'accélération doit être contrôlée, donc nous avons besoin d'un mécanisme de commande.**

Pour changer l'accélération de MobileObject, nous devons faire en sorte que l'observable **_acceleration_** émette des événements lorsque le **contrôleur** le décide. Si nous devons contrôler quand un Observable émet, nous devons regarder **Subject**, un autre type fourni par RxJs.

Un Subject est un Observable qui offre les méthodes suivantes :

* **next(val)** : émet un événement avec **val** comme valeur
* **error()** : se termine avec une erreur
* **complete()** : se termine correctement

Donc, si nous voulons changer l'accélération dans le temps, nous pouvons créer l'observable **_acceleration_** comme un Subject, puis utiliser la méthode next() pour émettre l'événement lorsque nécessaire.

![Image](https://cdn-media-1.freecodecamp.org/images/qvAl5YmGtLEPGhOFLZ4rQaN5Sq9eFtiK0FEE)
_L'accélération comme un Subject_

#### Regrouper tout dans la classe MobileObject

Maintenant que nous avons toutes les parties nécessaires, nous devons simplement les assembler dans une classe MobileObject cohérente.

![Image](https://cdn-media-1.freecodecamp.org/images/bVtpSszZRlZabVfeuKflJ53eq-H5asbdKTu2)

En résumé, voici comment un MobileObject est modélisé dans un monde réactif. Il y a :

* certains observables, _dynamicsX_ et _dynamicsY_ de l'exemple, qui émettent des données sur sa dynamique le long des diverses dimensions de l'espace (dans l'exemple ci-dessus, seulement 2, X et Y, dans un plan bi-dimensionnel)
* certains sujets, _accelerationX_ et _accelerationY_ de l'exemple, qui permettent aux contrôleurs de changer l'accélération le long des diverses dimensions
* une horloge interne qui établit la fréquence des intervalles de temps

Dans un espace à deux dimensions, nous avons 2 observables différents émettant la variation de l'espace. Ces observables doivent `**_partager_**` la même **_clock_** si nous voulons un mouvement cohérent. Et **_clock_** est en soi un observable. Ainsi, pour qu'ils puissent partager le même observable, nous avons ajouté l'opérateur `share()` à la fin de la fonction `buildClock()` que nous avons décrite précédemment.

### Dernière touche : le frein

Regardons cela de manière très simpliste. Si vous voulez arrêter ou ralentir une voiture qui se déplace avec une vitesse **V0**, vous devez appliquer à la voiture une accélération dans la direction opposée à celle de sa vitesse.

Après une période de temps, la vitesse de la voiture deviendra 0, et à ce moment-là, aucune accélération supplémentaire n'est appliquée à la voiture.

![Image](https://cdn-media-1.freecodecamp.org/images/czXu7Xwqr0ENn8L4RqrXOjq2ed-2FKAhRafB)
_Ce que signifie freiner_

Pour obtenir un effet de freinage, nous devons donc connaître la direction de MobileObject et arrêter l'accélération négative lorsque MobileObject atteint une vitesse de 0.

Connaître la direction est facile. Nous devons simplement prendre le premier événement émis par l'observable **_dynamicsX_** ou **_dynamicsY_**, selon l'axe qui nous intéresse, et vérifier si la vitesse du dernier événement est positive ou négative. Le signe de la vitesse est la direction.

```typescript
directionX = mobileObject.dynamicsX
.take(1)
.map(dynamics => dynamics.vel > 0 ? 1 : -1)
```

**_directionX_** est un observable qui émet un seul événement. La valeur émise est 1 si la vitesse est positive, -1 sinon.

Ainsi, lorsque MobileObject reçoit la commande de freinage, tout ce qu'il a à faire est d'obtenir la direction et d'appliquer une accélération opposée, comme ceci :

```typescript
directionX
.switchMap(
   // BRAKE est une constante d'accélération lorsque mobileObject freine
   dir => mobileObject.accelerationX.next(-1 * dir * BRAKE)
)
```

Nous y sommes presque. Nous devons simplement nous assurer que, une fois la vitesse atteinte à 0, ou proche de 0, nous supprimons toute accélération. Et voici comment nous pouvons obtenir ce que nous voulons.

```typescript
directionX
.switchMap(
   // BRAKE est une constante d'accélération lorsque mobileObject freine
   dir => {
      mobileObject.accelerationX.next(-1 * dir * BRAKE);
      return mobileObject.dynamicsX
      // VEL_0 est une petite valeur en dessous de laquelle nous considérons vel comme 0
      .filter(dynamics => Math.abs(dynamics.vel) < VEL_0)
      .do(() => mobileObject.accelerationX.next(0)
      .take(1)
   }
).subscribe()
```

Ici, après avoir émis la commande d'accélération de freinage, nous sélectionnons simplement le premier événement de l'observable **_dynamicsX_** où la vitesse est suffisamment petite pour être considérée comme 0. Ensuite, nous émettons une commande pour appliquer une accélération égale à zéro. Le dernier opérateur `take(1)` est ajouté pour s'assurer que nous nous désabonnons immédiatement, puisque l'observable de freinage a terminé son travail.

Ce code nécessite quelques raffinements pour fonctionner vraiment en douceur, mais il est suffisant pour transmettre les bases du freinage réactif.

### Retour au début : l'animation

Tout cela peut sembler bien, mais nous voulons toujours animer notre MobileObject. Par exemple, nous voulons créer une application où un utilisateur peut émettre des commandes d'accélération via une console à 4 boutons et voir le MobileObject se déplacer en conséquence.

![Image](https://cdn-media-1.freecodecamp.org/images/Wrg61mYRd8Mjjrh63qfxXI9pMPIrWdcci6wm)
_Une application exemple pour contrôler MobileObject et voir son mouvement_

Une telle application agit comme le **contrôleur** de MobileObject et comme le moniteur pour montrer l'animation.

#### **Émettre des commandes**

Contrôler le mouvement de MobileObject signifie que nous devons appliquer une accélération. L'application navigateur peut le faire en utilisant le **_accelerationX_** subject fourni par MobileObject, comme le montre l'extrait suivant.

```typescript
<button id="positiveAccX" 
   (mousedown)="pAccX()" (mouseup)="releaseAccX()"/>

// mobileObject contient l'instance que nous voulons contrôler
const accelerationValue = 100;
pAccX() {
   mobileObject.accelerationX.next(accelerationValue);
}
releaseAccX() {
   mobileObject.accelerationX.next(0);
}
```

Une accélération de 100 est appliquée lorsque le bouton de la souris est enfoncé et l'accélération est mise à 0 lorsque le bouton de la souris est relâché, simulant la pédale d'accélérateur.

#### **Montrer le mouvement animé**

MobileObject expose **_dynamicsX_** et **_dynamicsY_**, 2 Observables qui émettent en continu des données sur le mouvement le long de l'axe respectif (par exemple, deltaSpace, vitesse actuelle, accélération le long de X et Y). Ainsi, l'application navigateur doit s'y abonner pour recevoir ces flux d'événements et changer la position de MobileObject à chaque événement émis, comme le montre cet extrait de code :

```typescript
interface Dynamics {deltaVel: number; vel: number; deltaSpace: number; space: number}
const mobileObjectElement = document.querySelector('.mobileobj');
mobileObject.dynamicsX.subscribe(
   (dyn: Dynamics) => {
     const currentPositionX = mobileObjectElement.style.left;
     const deltaSpaceX = dyn.deltaSpace;
     mobileObjectElement.style.left = currentPositionX + deltaSpace;
   }
)
```

#### **Frame d'animation**

Le navigateur fonctionne de manière asynchrone, et il n'est pas possible de prédéterminer quand il est prêt à afficher une nouvelle frame. L'animation, ou la simulation de mouvement, est fournie en changeant la position d'un objet dans le temps. Une animation fluide change la position à chaque frame affichée par le navigateur.

RxJs fournit un **Scheduler** appelé `animationFrame` qui enveloppe l'API `requestAnimationFrame` du navigateur. Un **Scheduler** est un type de RxJs qui contrôle quand les événements émis par un observable se produisent réellement.

Nous pouvons utiliser `animationFrame` et la méthode statique `interval` de Observable pour créer un observable qui émet un événement chaque fois que le navigateur est prêt à afficher une nouvelle frame.

```
Observable.interval(0, animationFrame)
```

Maintenant, nous devons simplement ajouter la longueur de temps écoulé depuis la dernière frame aux événements émis par cet observable, et nous avons ce dont nous avons besoin : un observable qui émet chaque fois que le navigateur est prêt à afficher une nouvelle frame avec la quantité de temps écoulé depuis l'affichage de la dernière frame.

![Image](https://cdn-media-1.freecodecamp.org/images/FzjfjgMujwYxJrPRUCOCTFbQ3nC-h4C2uf4j)
_Horloge synchronisée avec la frame d'animation_

C'est la nouvelle **_clock_** que nous utilisons dans MobileObject pour fournir un flux d'événements relatifs aux mouvements (**_dynamicsX_** et **_dynamicsY_**). Ces mouvements sont synchronisés avec le moment où le navigateur est prêt à montrer une nouvelle frame.

Vous avez peut-être remarqué que, dans cet dernier exemple de code, la syntaxe a légèrement changé. Nous utilisons maintenant les opérateurs "pipeable". Nous ne les avons pas utilisés auparavant, car ils n'ajoutent rien à notre raisonnement. Cependant, il est utile de les introduire car ils représentent une nouvelle syntaxe que vous pouvez utiliser depuis RxJS 6.

Vous avez peut-être également remarqué la fonction `defer`. Il s'agit d'une fonction RxJs qui retourne un Observable, mais qui s'assure que la logique définie dans la fonction passée en paramètre à `defer` n'est exécutée que lorsque l'Observable est souscrit.

Cela nous permet d'exécuter la méthode `buildClock()` à tout moment, peut-être lors de l'initialisation d'un composant UI. Cela nous permet également d'être sûrs que l'horloge ne commencera à fonctionner qu'une fois souscrite et avec le bon timing. Plus spécifiquement, `let startOfPreviousFrame = animationFrame.now();` ne sera exécuté que lorsque l'observable **_clock_** sera souscrit.

### Dernier point, mais non des moindres, quelques mots sur le style de programmation fonctionnelle

Au début de notre discussion, nous avons parlé de la construction du flux de données représentant le mouvement de MobileObject dans le temps. Nous avons appelé cela l'observable **_dynamics_**, et utilisé la logique de transformation suivante :

```
map(dT => {
  const dV = A * dT;
  vel = vel + dV;
  const dS = vel * dT + A / 2 * dT * dT; 
  space = space + dS;
  return {dV, vel, dS, space};
})
```

Cela suppose que nous avons défini les variables `vel` et `space` quelque part afin qu'elles soient visibles dans la portée de la fonction passée en paramètre à l'opérateur `map`.

La première solution qui pourrait venir à l'esprit d'un programmeur OO traditionnel est de définir ces variables comme propriétés de la classe MobileObject. Mais cela signifierait stocker des informations d'état au niveau de l'objet qui ne devraient être modifiées que par la transformation définie dans l'opérateur `map` montré ci-dessus.

Si vous rendez ces informations d'état accessibles à potentiellement n'importe quelle partie de la logique dans MobileObject, vous risquez de les modifier par erreur, rendant l'objet entier incohérent. De plus, chaque fois que cet état est modifié, nous devons penser à d'autres parties de la logique qui dépendent potentiellement de cet état. Nous devons considérer les conséquences de telles dépendances, qui parfois peuvent être assez bien cachées.

C'est là que la programmation fonctionnelle vient à notre secours.

#### Fonctions de niveau supérieur

Une **fonction de niveau supérieur** est une fonction qui retourne une fonction. Le nom peut vous rappeler les **observables de niveau supérieur**, qui sont des observables qui émettent d'autres observables.

L'observable **_dynamics_** de MobileObject peut être construit si nous avons l'observable **_clock_** et que nous connaissons l'accélération **A**. Nous pouvons donc dire que **_dynamics_** est une fonction de l'observable **_clock_** et de la valeur d'accélération **A**. 

![Image](https://cdn-media-1.freecodecamp.org/images/F0T4AxwqGDWhq1MppFERaV-OKh0Pj5Q5XvlL)

Nous pouvons également créer une fonction, **dynamicsF**, qui retourne une fonction **dF**. Celle-ci, à son tour, lorsqu'elle est appelée, retourne l'observable **_dynamics_**, comme le montre l'extrait ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/LhTgux7QBkkkMhgCEh0ROZmdkzLqslbAS4RZ)
_Exemple de fonction d'ordre supérieur_

Remarquez que dans **dynamicsF**, nous avons défini les variables `vel` et `space`, qui sont parfaitement visibles depuis **dF**, rendant notre code cohérent et correct.

Si nous avons une variable `clock` où nous stockons l'observable **_clock_** et une variable `acc` où nous stockons la valeur de l'accélération **A**, nous pouvons utiliser la fonction **dynamicsF**, que nous venons de définir, pour construire notre observable **_dynamics_** comme le montre l'extrait suivant.

```
const dynFunction = dynamicsF();
const dynamics = dynFunction(clock, A);
```

Le point clé est que maintenant **dynFunction** contient en interne les variables `vel` et `space`. Elle les stocke en interne dans son propre état, un état qui n'est pas visible à l'extérieur de la fonction.

En supposant que **dynamicsF** est une méthode de la classe MobileObject, la version finale du code qui crée l'observable **_dynamics_** dans le constructeur de MobileObject peut être écrite comme suit

```
const dfX = this.dynamicsF();
this.dynamicsX = this.accelerationX
                     .swithMap(a => dfX(this.clock, a));
```

En faisant cela, nous avons confiné les informations d'état sur la vitesse actuelle et l'espace dans la fonction `dfX`. Nous avons également supprimé le besoin de définir des propriétés pour la vitesse actuelle et l'espace dans MobileObject. Et nous avons amélioré la réutilisation, puisque **dynamicsF()** n'a aucune référence à un axe et peut être utilisée pour calculer à la fois **_dynamicsX_** et **_dynamicsY_** via la composition de fonctions.

En appliquant un style de programmation fonctionnelle (dans ce cas, un isolement plus élevé), nous avons gagné une sécurité accrue pour notre code et une réutilisation accrue.

### Conclusion

Cela a été un voyage assez long. Nous avons vu l'utilisation de certains des opérateurs RxJs les plus importants et comment les Subjects peuvent être pratiques. Nous avons également vu comment utiliser un style de programmation fonctionnelle pour augmenter la sécurité de notre code ainsi que sa réutilisabilité.

J'espère avoir pu montrer comment, en utilisant une approche de pensée réactive pour ce problème, il est possible de construire une solution logicielle qui reflète très naturellement un modèle de la vie réelle pour les objets qui sont contrôlés à distance.

Chaque fois que vous devez faire face à un problème où le temps et l'asynchronicité jouent un rôle, alors la pensée réactive soutenue par des bibliothèques réactives telles que RxJs peut vous mener à une conception plus simple et plus solide. Dans ce monde de connectivité constante, le cloud, les plateformes non bloquantes et les microservices, le temps et l'asynchronicité vont jouer un rôle de plus en plus important.

Si vous avez aimé ce que vous venez de lire, vous pourriez être intéressé par [la lecture de cet article](https://medium.com/@enrico.piccinin/reactive-thinking-how-to-design-a-distributed-system-with-rxjs-websockets-and-node-57d772f89260), où je décris comment construire un système distribué pour contrôler et afficher en action plusieurs MobileObjects dans un environnement distribué.

L'ensemble du code peut être trouvé [ici](https://github.com/EnricoPicci/mobile-object-observables).

Je tiens à remercier Ben Lesh qui a inspiré cet article avec [l'une de ses conférences](https://www.youtube.com/watch?v=X_RnO7KSR-4).