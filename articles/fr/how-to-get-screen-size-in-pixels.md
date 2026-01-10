---
title: Comment obtenir la taille de l'écran en pixels
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-11T22:34:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-screen-size-in-pixels
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9df4740569d1a4ca3a97.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment obtenir la taille de l'écran en pixels
seo_desc: 'There may be times where your JavaScript application needs to know what
  the size screen needs to be able to perform certain actions.

  Luckily for us, there are built in JavaScript functions that can easily grab different
  dimensions of the screen on th...'
---

Il peut arriver que votre application JavaScript ait besoin de connaître la taille de l'écran pour pouvoir effectuer certaines actions.

Heureusement pour nous, il existe des fonctions JavaScript intégrées qui peuvent facilement récupérer différentes dimensions de l'écran sur l'appareil de l'utilisateur en pixels. Celle que vous utilisez dépend de ce que vous souhaitez faire.

## **Obtenir la résolution de l'utilisateur**

Vous pourriez souhaiter faire quelque chose impliquant la résolution de l'appareil de l'utilisateur. Dans ce cas, vous devriez utiliser les propriétés intégrées `screen.width` et `screen.height`. Celles-ci vous donnent la taille de l'écran avec lequel vous travaillez.

**Ce n'est pas la zone avec laquelle vous avez à travailler sur la page**. **Ces valeurs représentent l'intégralité de l'écran**, c'est-à-dire **la résolution d'affichage de l'utilisateur**.

## **Obtenir la taille du navigateur**

Il pourrait y avoir une application intéressante pour traiter la taille actuelle du navigateur. Si vous devez accéder à ces dimensions, utilisez les propriétés `screen.availWidth` et `screen.availHeight` pour ce faire.

Rappelez-vous, ce sont les dimensions de l'ensemble de la fenêtre du navigateur, du haut de la fenêtre du navigateur jusqu'à l'endroit où le navigateur rencontre une barre des tâches ou le bord de votre bureau, selon votre configuration.

**Une note intéressante** : `screen.availHeight` peut également être utilisé pour déterminer la hauteur d'une barre des tâches sur un ordinateur. Si votre résolution de navigateur est, par exemple, `1366 x 768`, et que `screen.availHeight` indique 728 pixels, alors votre barre des tâches fait 40 pixels de haut. Vous pouvez également calculer la hauteur de la barre des tâches en soustrayant `screen.height` et `screen.availHeight` :

```text
var taskbarHeight = parseInt(screen.height,10) - parseInt(screen.availHeight,10) + " pixels";
/*
Pour un utilisateur ayant une résolution d'écran de 1366 x 768 pixels, sa barre des tâches fait probablement 40 pixels s'il utilise Windows 10 sans fonctionnalités d'accessibilité ajoutées.
*/
```

## **Obtenir la taille de la fenêtre d'affichage**

Ces propriétés sont intéressantes et peuvent être utilisées pour créer des effets ingénieux. Vous pouvez utiliser `window.innerHeight` et `window.innerWidth` pour obtenir la taille de la fenêtre de la page web telle que l'utilisateur la voit.

Gardez à l'esprit - ces valeurs ne sont pas statiques et changeront en fonction de ce qui se passe avec le navigateur lui-même. En d'autres termes, si le navigateur lui-même est petit, ces valeurs seront plus petites, et si le navigateur est maximisé, elles seront plus grandes.

Si, par exemple, vous travaillez dans Google Chrome et que vous ouvrez la console (doit être ancrée à un côté de la fenêtre), `window.innerHeight` changera pour refléter la hauteur de la console car une partie de la fenêtre sera bloquée.

Vous pouvez tester cela en appelant `window.innerHeight`, en notant la valeur, puis en augmentant la taille de la console, puis en appelant à nouveau `window.innerHeight`.

Ces propriétés changeront également si votre navigateur est maximisé ou redimensionné de quelque manière que ce soit. À la taille maximale d'un navigateur, la propriété `window.innerWidth` est la même que `screen.width` et `screen.availWidth` (sauf s'il y a une barre des tâches sur le côté, au quel cas `screen.availWidth` ne sera pas égal). `window.innerHeight` est égal à la quantité d'espace dans la fenêtre de la page elle-même (la zone de la page web).

## **Obtenir la hauteur et la largeur de la page web**

Si vous devez voir à quel point votre page web est haute ou large, il existe des propriétés pour récupérer ces dimensions : `document.body.offsetWidth` et `document.body.offsetHeight`.

Ces propriétés représentent la taille du contenu dans le corps de la page elle-même. Une page sans contenu a une valeur `document.body.offsetHeight` proche de celle de `window.innerHeight` en fonction des marges/remplissages définis sur le corps du document. Si les marges et le remplissage sont définis à `0` sur l'élément racine html et le corps du document, alors `document.body.offsetHeight` et `window.innerHeight` seront égaux sans contenu.

Ces propriétés peuvent être utilisées pour interagir avec votre page/application en fonction de ce que vous souhaitez faire.