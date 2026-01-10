---
title: Passez SUPER SAIYAN avec les Observables RxJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-17T17:31:50.000Z'
originalURL: https://freecodecamp.org/news/go-super-saiyan-with-rxjs-observables-d4681ae51930
coverImage: https://cdn-media-1.freecodecamp.org/images/0*qE2wxzg_yiFOIN-Q
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: Reactive Programming
  slug: reactive-programming
- name: RxJS
  slug: rxjs
- name: 'tech '
  slug: tech
seo_title: Passez SUPER SAIYAN avec les Observables RxJS
seo_desc: 'By Yazeed Bzadough

  I loved DragonBall Z as a kid, and still love it as an adult.

  Among the ludicrous number of transformations, the original Super Saiyan remains
  my favorite.



  Nothing quite like the original


  I’m also loving RxJS the more I level up...'
---

Par Yazeed Bzadough

J'adorais DragonBall Z enfant, et je l'aime toujours autant adulte.

Parmi le nombre ridicule de transformations, le Super Saiyan original reste mon préféré.

![](https://cdn-media-1.freecodecamp.org/images/0*qE2wxzg_yiFOIN-Q)
> Rien ne vaut l'original

J'aime aussi de plus en plus RxJS à mesure que je monte en niveau, alors pourquoi ne pas combiner ces deux univers pour le showdown ultime ?

### Transformons-nous en Super Saiyan

Avec quatre feuilles de sprites et un peu de HTML, CSS et RxJS, nous pouvons recréer cette transformation légendaire !

![](https://cdn-media-1.freecodecamp.org/images/1*qgex4ns9jPE_tpCy_OTfWA.gif)

Voici ce que nous allons créer. Excitant, non ? ?

### Installation

Tout est sur [mon GitHub](https://github.com/yazeedb/dbz-rxjs).

```
cd ./où-vous-voulez
git clone [https://github.com/yazeedb/dbz-rxjs](https://github.com/yazeedb/dbz-rxjs)
cd dbz-rxjs
```

Ouvrez `index.html` dans votre navigateur préféré et le projet dans votre éditeur de texte préféré, et vous êtes prêt à commencer !

Pas de `npm install` aujourd'hui ?

Et pour la suite, j'utiliserai l'acronyme « SSJ » au lieu de « Super Saiyan » pour faire court.

### Premier jour d'entraînement

![](https://cdn-media-1.freecodecamp.org/images/1*FpxB4WdbNMmldqZDnpVp1g.png)

Vous remarquerez que Goku bouge déjà. Puisque nous nous concentrons sur RxJS, nous allons simplement survoler le point de départ du projet.

Voici le HTML principal :

```html
<div id="root">
  <div id="meter-container">
    <span>Maintenez une touche enfoncée pour MONTER EN PUISSANCE !</span>
    <div id="meter"></div>
  </div>

  <div id="sprite" class="base"></div>
</div>
```

La div du bas a `class="base"`, ce qui correspond à ce CSS :

```css
.base,
.ssj {
  width: 120px;
  height: 250px;
  animation: stand 0.8s steps(2) infinite;
}

.base {
  background-image: url('img/goku-standing-sheet.png');
}
```

Cela définit la largeur, la hauteur et l'animation de Goku en position debout.

Si vous regardez ses feuilles de sprites base/ssj, il y a deux positions différentes et nous basculons entre elles toutes les 0,8 secondes.

![](https://cdn-media-1.freecodecamp.org/images/1*Cy1fArcSxNJwGDc98YMHEA.png)![](https://cdn-media-1.freecodecamp.org/images/1*mNVDs7NKfcfkA8l86IxOTA.png)

Le basculement est géré vers le bas de `style.css` :

```css
@keyframes stand {
  from {
    background-position: 0px;
  }
  to {
    background-position: -255px;
  }
}
```

Même chose pour la montée en puissance :

![](https://cdn-media-1.freecodecamp.org/images/1*sSTHMTvkazP0BaZPubo4kg.png)![](https://cdn-media-1.freecodecamp.org/images/1*xkI3tsGLGRpVoH2RjaFK9w.png)

```css
@keyframes powerup {
  from {
    background-position: 0px;
  }
  to {
    background-position: -513px;
  }
}
```

Nous aborderons le compteur de puissance lorsque nous le manipulerons.

### Maîtriser les éléments du DOM

`index.html` inclut déjà `RxJS@6.2.1` via CDN, donc vous êtes couvert.

Dans `app.js`, capturons les éléments du DOM qui nous intéressent :

```js
const sprite = document.querySelector('#sprite');
const meterContainer = document.querySelector('#meter-container');
const meter = document.querySelector('#meter');
```

Je préfère aliaser `document.querySelector` pour éviter les douleurs au poignet.

```js
const $ = document.querySelector.bind(document);
const sprite = $('#sprite');
const meterContainer = $('#meter-container');
const meter = $('#meter');
```

Ensuite, nous allons créer une fonction `main` et l'appeler immédiatement.

```js
// ...

const main = () => {
  // faire quelque chose
};
main();
```

### Monter en puissance

Voici le premier extrait de code de `main` :

```js
const main = () => {
  const { fromEvent } = rxjs;

  const begin = fromEvent(document, 'keydown');
  const end = fromEvent(document, 'keyup');
};
```

Goku doit monter en puissance lorsqu'une touche est maintenue enfoncée et s'arrêter lorsque la touche est relâchée. Nous pouvons utiliser l'opérateur `fromEvent` pour créer deux observables :

- `begin` : Notifie lorsque l'utilisateur appuie sur une touche.
- `end` : Notifie lorsque l'utilisateur relâche une touche.

Ensuite, nous pouvons nous **abonner** à ces émissions et agir en conséquence. Pour obtenir l'animation de montée en puissance, donnez à `sprite` le nom de classe `powerup`.

```js
begin.subscribe(() => {
  sprite.classList.add('powerup');
});
```

![](https://cdn-media-1.freecodecamp.org/images/1*6-GLDooG9dTyGqNQ2XP0ww.png)

Cela fonctionne, mais appuyer sur une touche le fait monter en puissance indéfiniment...

Nous devons également nous abonner à l'observable `end` pour savoir quand la touche est relâchée.

```js
end.subscribe(() => {
  sprite.classList.remove('powerup');
});
```

Maintenant, il monte et descend en puissance sur votre commande.

### Construire un scouter

Tout fan de DBZ a vu un scouter, la petite lunette utilisée pour suivre les niveaux de puissance (jusqu'à l'épisode 20 environ...).

![](https://cdn-media-1.freecodecamp.org/images/0*8H9CSUZbfDPxmdgR.png)

> Blague obligatoire sur le niveau > 9000

À mesure que les Saiyans montent en puissance, leur niveau de puissance augmente. Inconcevable, non ?

Nous avons besoin d'un moyen de suivre le niveau de puissance de Goku alors qu'il s'élève, et de déclencher la transformation SSJ après, disons, 100 points.

Nous pouvons commencer son niveau de puissance à 1 et l'augmenter pendant que l'utilisateur maintient une touche enfoncée.

#### Opérateurs RxJS

Les opérateurs sont là où RxJS brille vraiment. Nous pouvons utiliser des fonctions pures pour décrire comment les données doivent se transformer à travers le flux.

Lorsque l'utilisateur maintient une touche enfoncée, transformons ces émissions en un nombre qui augmente avec le temps.

#### Scan

L'opérateur [scan](https://www.learnrxjs.io/operators/transformation/scan.html) est parfait pour cela. C'est comme `Array.reduce`, mais il émet **pendant qu'il réduit**.

Par exemple, si vous avez un tableau de nombres :

```js
nums = [1, 2, 3, 4, 5];
```

Et que vous souhaitez les additionner, `reduce` est un excellent choix.

```js
nums.reduce((a, b) => a + b, 0);
// 15
```

Que faire si vous voulez voir chaque addition au fur et à mesure ?

Entrez `scan`. Vous pouvez exécuter cela dans la console de notre application.

```js
const { from } = rxjs;
const { scan } = rxjs.operators;

from([1, 2, 3, 4, 5])
  .pipe(scan((a, b) => a + b, 0))
  .subscribe(console.log);

// 1 (0 + 1)
// 3 (1 + 2)
// 6 (3 + 3)
// 10 (6 + 4)
// 15 (10 + 5)
```

Voyez comment les émissions augmentent avec le temps ? Nous pouvons faire cela avec Goku alors qu'il monte en puissance !

```js
const { fromEvent } = rxjs;
const { scan, tap } = rxjs.operators;

const begin = fromEvent(document, 'keydown');
const end = fromEvent(document, 'keyup');

begin
  .pipe(
    scan((level) => level + 1, 1),
    tap((level) => {
      console.log({ level });
    })
  )
  .subscribe(() => {
    sprite.classList.add('powerup');
  });
```

Nous commençons son niveau à `1` et l'augmentons de 1 à chaque fois que l'événement `keydown` se déclenche.

Et l'opérateur [tap](https://www.learnrxjs.io/operators/utility/do.html) nous permet de logger rapidement la valeur sans perturber le pipeline.

![](https://cdn-media-1.freecodecamp.org/images/1*CviOotpl-fpRm5qrI7INhQ.png)

> Ma puissance approche infiniment le MAXIMUM !

### Devenir Super Saiyan

Nous nous sommes entraînés dur, il est temps de nous transformer.

L'opérateur `scan` suit le niveau de puissance de Goku. Maintenant, nous devons passer en SSJ lorsqu'il atteint 100.

J'ai construit une carte des `niveaux : transformations`. Vous pouvez la placer juste au-dessus de `main`.

```js
const powerLevels = {
  100: {
    current: 'base',
    next: 'ssj'
  }
};

const main = () => {
  // ...
};
```

C'est un peu excessif, mais cela devrait simplifier l'ajout de futures transformations.

Lorsque le niveau de puissance atteint un nombre dans cette carte `powerLevels`, nous retirerons sa classe `current` de `sprite` et ajouterons la classe `next`.

Cela nous permet de passer en douceur d'une transformation à l'autre.

Voici le code.

```js
const { fromEvent } = rxjs;
const { filter, map, scan, tap } = rxjs.operators;

const begin = fromEvent(document, 'keydown');
const end = fromEvent(document, 'keyup');

begin
  .pipe(
    scan((level) => level + 1, 1),
    tap((level) => {
      console.log({ level });
      sprite.classList.add('powerup');
    }),
    map((level) => powerLevels[level]),
    filter((level) => level && level.next)
  )
  .subscribe(({ current, next }) => {
    sprite.classList.remove(current);
    sprite.classList.add(next);
  });
```

#### Map et Filter

L'ajout de la classe `powerup` se fait maintenant dans `tap`, car cela doit toujours se produire. La transformation SSJ, cependant, **ne doit pas** toujours se produire.

En utilisant `map`, le dernier niveau de puissance devient une entrée dans la carte `powerLevels`. Nous utilisons `filter` pour vérifier si l'entrée existe **et** a une propriété `.next`.

Si c'est le cas, cela signifie que Goku peut aller encore plus loin ! Notre `.subscribe` échangera `current` et `next` en tant que noms de classe sur `sprite`.

Le résultat final ?

![](https://cdn-media-1.freecodecamp.org/images/1*q-ifHhrr8byMWPENjBpNyQ.gif)

### Compteur de puissance

Vous vous amusez autant que moi, non ? Malheureusement, notre utilisateur ne s'amusera pas.

Il ne peut pas voir à quel point le niveau de puissance de Goku est élevé ! Il ne saura pas comment ouvrir la console DevTools. Nous devons remédier à cela !

Améliorons notre UX en remplissant le compteur de puissance. Vous pouvez placer cela au-dessus de `main`.

```js
const fillMeter = (level) => {
  const limit = 100;

  if (level >= limit) {
    return;
  }

  const containerWidth = meterContainer.offsetWidth;
  const newWidth = (level / limit) * containerWidth;

  meter.style.width = `${newWidth}px`;
};
```

Et appelez-le dans `tap`.

```js
tap((level) => {
  console.log({ level });
  sprite.classList.add('powerup');
  fillMeter(level);
});
```

Et voici le résultat :

![](https://cdn-media-1.freecodecamp.org/images/1*qvr0L_5cmXzMI4g8sYtoyg.gif)

### Aller encore plus loin

Déverrouiller plus de transformations est simplement une question d'ajout de sprites et de mise à jour de notre carte `powerLevels`. Si vous êtes intéressé, soumettez une PR sur [le dépôt](https://github.com/yazeedb/dbz-rxjs) et nous en discuterons définitivement.

Voici [la feuille de sprites originale](https://www.deviantart.com/bruguii/art/goku-fin-jus-268665173). Amusez-vous !