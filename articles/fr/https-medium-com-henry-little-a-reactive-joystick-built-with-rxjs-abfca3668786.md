---
title: Comment construire un Joystick réactif en tant que flux Observable unique RxJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-08T15:07:23.000Z'
originalURL: https://freecodecamp.org/news/https-medium-com-henry-little-a-reactive-joystick-built-with-rxjs-abfca3668786
coverImage: https://cdn-media-1.freecodecamp.org/images/1*X3xtviyY779db4yRZugTmg.gif
tags:
- name: Angular
  slug: angular
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: RxJS
  slug: rxjs
- name: 'tech '
  slug: tech
seo_title: Comment construire un Joystick réactif en tant que flux Observable unique
  RxJS
seo_desc: 'By Henri Little - Beyle

  We are all likely familiar with the concept of a Joystick.

  We start holding the handle of the Joystick, we move the handle around, and when
  we release it, the handle gently goes back to its initial position.

  Now, what if we wa...'
---

Par Henri Little - Beyle

Nous sommes tous probablement familiers avec le concept de Joystick.

Nous commençons par tenir le manche du Joystick, nous déplaçons le manche, et lorsque nous le relâchons, le manche revient doucement à sa position initiale.

Maintenant, que se passe-t-il si nous voulons construire un composant logiciel qui simule le comportement d'un Joystick dans le navigateur ?

Eh bien, avec RxJS, cela s'avère assez simple. C'est aussi un exercice intéressant pour prouver votre pensée réactive. Vous pouvez sauter directement au code [ici](https://github.com/EnricoPicci/reactive-joystick) si vous le souhaitez, sinon continuez à lire et voyez ce que nous pouvons faire.

### Quels sont les événements qui nous intéressent ?

Le comportement du Joystick peut être vu comme une série d'événements combinés ensemble de quelque manière.

Le premier événement qui nous intéresse est lorsque l'utilisateur appuie sur la souris sur le manche (`mousedown`) - le manche est simplement la partie centrale de l'image du Joystick.

Si vous maintenez la souris enfoncée, vous pouvez vous déplacer et vous voyez le manche bouger en conséquence — les événements `mousemove` de la souris sont donc la deuxième série d'événements que nous voulons capturer.

Enfin, nous devons considérer lorsque l'utilisateur relâche la souris (`mouseup`) puisque c'est l'événement qui fait revenir le manche du Joystick à sa position initiale.

![Image](https://cdn-media-1.freecodecamp.org/images/nl-lPdU3SnW8QP6FtuGXwFhwftNOJvwzy2fF)
_Événements pertinents pour le cas du Joystick_

La séquence entière peut être répétée après que le manche soit relâché. La souris est pressée sur le manche, puis elle est déplacée, puis elle est relâchée. Encore et encore.

Cette répétition peut être vue comme un flux d'événements. Nous pouvons dire que le comportement d'un joystick est gouverné par ce flux d'événements.

![Image](https://cdn-media-1.freecodecamp.org/images/PSeMoBEzyvtgqnNjQFIMNhKZBVk0UyhSr5Ii)
_Le flux d'événements d'un Joystick_

Si nous sommes capables de construire un tel flux d'événements, nous sommes en bonne position pour atteindre notre objectif — c'est-à-dire, implémenter un composant logiciel de Joystick pour le navigateur en utilisant RxJS.

### Les blocs de construction avec RxJS

Le navigateur nous fournit en fait la notification des événements qui nous intéressent : l'événement `mousedown` sur l'élément DOM représentant le manche du Joystick, et les événements `mousemove` et `mouseup` au niveau du document DOM.

RxJS, de son côté, vient avec la fonction `fromEvent` qui nous permet de créer un Observable à partir d'un événement du navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/E5gArW8EsLVN47YdlzZQDfsr-J-v7wRYha2w)
_Créer un Observable avec la fonction `fromEvent` de RxJS_

En utilisant ce mécanisme, nous pouvons créer les trois flux d'événements qui vont être les blocs de construction de notre solution : **mouse_DOWN_Obs**, **mouse_MOVE_Obs**, **mouse_UP_Obs**.

![Image](https://cdn-media-1.freecodecamp.org/images/18oYzRw8TkzIoscKyhouvoJEe08erjL0cnfL)
_Les flux d'événements qui sont nos blocs de construction_

Mais ce ne sont que nos blocs de construction. Nous devons faire quelque chose avec eux afin d'obtenir ce que nous voulons : nous devons ignorer tous les événements `mousemove` qui se produisent avant le premier `mousedown` et ensuite ignorer tous les événements `mousemove` qui se produisent après le prochain `mouseup`. Ensuite, nous répétons tout cela à nouveau lorsqu'un nouvel événement `mousedown` se produit. Ceux-ci composent le **"flux d'événements pour le Joystick"**_._

![Image](https://cdn-media-1.freecodecamp.org/images/57-sjEw-zvOm53BVKUeUh9KaC55f7ytcUHA-)
_Flux d'événements du Joystick construit à partir de blocs de construction_

### La transformation des Observables via la composition d'opérateurs

Tout commence lorsque l'utilisateur appuie sur la souris sur le manche du Joystick, c'est-à-dire **mouse_DOWN_Obs**. Nous pouvons l'appeler l'Observable source.

Une fois que nous sommes informés d'un événement de **mouse_DOWN_Obs**, nous devons _basculer_ et commencer à écouter **mouse_MOVE_Obs**.

![Image](https://cdn-media-1.freecodecamp.org/images/s3esbte2H8imrlxNz2pHYtOGaXC7NMYd-Ytt)
_La première transformation avec switchMap_

Il peut sembler que nous n'avons pas accompli grand-chose, mais en fait nous sommes maintenant en position de _prendre_ les notifications **mouse_MOVE_Obs** _jusqu'à_ ce que nous entendions de **mouse_UP_Obs**. À ce moment-là, nous nous arrêtons pour redémarrer à la prochaine notification de **mouse_DOWN_Obs**.

![Image](https://cdn-media-1.freecodecamp.org/images/zfSEa0bNUZx0i52yfZXkpg1-FqxBSGaREnJy)
_La deuxième transformation avec takeUntil_

Remarquez que nous appliquons `takeUntil` à **mouse_MOVE_Obs**, car c'est l'Observable que nous voulons compléter. Si nous avions appliqué un niveau plus haut, à **mouse_DOWN_Obs**, voici ce qui se serait passé :

![Image](https://cdn-media-1.freecodecamp.org/images/ZS1GyApmXIMmbSunvKPbVTBWGsJf1TZmS3FT)

Seulement la première séquence d'événements de déplacement aurait été notifiée, et ensuite le flux d'événements aurait été fermé. Plus d'événements pour le Joystick.

### Maintenant, c'est le moment des effets secondaires

Nous avons appris comment construire un flux de tous les événements pertinents pour un Joystick. Pour faire quelque chose d'utile avec ce flux, nous devons lier les événements à une sorte d'action que nous voulons faire. Plus spécifiquement :

* lorsque nous détectons un événement `mousemove`, nous devons changer la position du manche sur le navigateur
* lorsque nous détectons un événement `mouseup`, nous devons déplacer doucement le manche vers sa position d'origine, en définissant un style de transition
* lorsque nous détectons un événement `mousedown`, nous devons réinitialiser le style de transition

Mais attention. Tous ne sont pas des événements `mousemove`, tous ne sont pas des événements `mouseup`, et tous ne sont pas des événements `mousedown`. Seulement ceux qui appartiennent à l'ensemble des **"événements pertinents pour le Joystick"**_._ Par exemple, nous ne sommes pas intéressés par tous les événements `mousemove` qui se produisent avant que le Joystick n'ait été activé (appuyer sur la souris sur le manche) ou après que le manche du Joystick ait été relâché.

![Image](https://cdn-media-1.freecodecamp.org/images/jMq3dPUHgqbRRovbFLXCKmSG9XueC-dIMa0V)
_Où nous avons besoin d'effets secondaires_

Revenons à notre principale ligne de raisonnement. Nous devons faire quelque chose à l'occurrence de certains événements. Quelque chose qui change l'état du système. Dans notre cas, il s'agit de la position du manche sur le navigateur. En termes de programmation **fonctionnelle**, ceux-ci sont appelés **effets secondaires**, c'est-à-dire des fonctions qui changent l'état du système.

![Image](https://cdn-media-1.freecodecamp.org/images/jHOP52U5BPDPSJOF2BLBvcHzCg6ZW7ZZ9m8J)
_Effets secondaires en tant que fonctions — Fonctions en tant qu'effets secondaires_

RxJS nous donne deux façons d'implémenter les **effets secondaires**.

La première est la méthode `subscribe` de l'Observable. La seconde est l'opérateur `tap`, anciennement connu sous le nom de `do`, qui "effectue un **effet secondaire** pour chaque émission sur l'Observable source, mais retourne un Observable qui est identique à la source" — l'**effet secondaire** est déterminé par la fonction passée à `tap` en tant que paramètre. `tap` est la méthode que nous allons utiliser.

Finalement, voici le cœur du code qui implémente notre Joystick Réactif

```
const handle = document.getElementById("handle");const mouse_DOWN_Obs = rxjs.fromEvent(handle, 'mousedown');const mouse_MOVE_Obs = rxjs.fromEvent(document, 'mousemove');const mouse_UP_Obs = rxjs.fromEvent(document, 'mouseup');
```

```
function activateJoytick() {  mouse_DOWN_Obs.pipe(    rxjs.operators.tap(() => joystickActivated()),    rxjs.operators.switchMap(() => mouse_MOVE_Obs.pipe(      rxjs.operators.takeUntil(mouse_UP_Obs.pipe(        rxjs.operators.tap(() => joystickReleased())      )),    )),    rxjs.operators.tap(event => showHandleInNewPosition(event))  )  .subscribe();}
```

### Exemple de code

Vous pouvez trouver l'exemple de code [ici](https://github.com/EnricoPicci/reactive-joystick), où vous pouvez comparer l'implémentation RxJS avec une implémentation construite en utilisant du JavaScript pur.