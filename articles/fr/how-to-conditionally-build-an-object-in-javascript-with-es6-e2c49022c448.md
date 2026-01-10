---
title: Comment construire conditionnellement un objet en JavaScript avec ES6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-03T22:30:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-conditionally-build-an-object-in-javascript-with-es6-e2c49022c448
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_CMG7dT4YMldUiVPueOmXw.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: Comment construire conditionnellement un objet en JavaScript avec ES6
seo_desc: 'By Knut Melvær

  Moving user-generated data between sources often requires you to check if a field
  has values or not. You then build the output based on that. This is how you can
  use some of the ES6 features in JavaScript to do it more concisely.

  Since...'
---

Par Knut Melvær

Le déplacement de données générées par les utilisateurs entre différentes sources nécessite souvent de vérifier si un champ contient des valeurs ou non. Vous construisez ensuite la sortie en fonction de cela. Voici comment vous pouvez utiliser certaines des fonctionnalités ES6 en JavaScript pour le faire de manière plus concise.

Depuis que [Sanity.io](https://sanity.io) (où je travaille) a sponsorisé [Syntax](https://syntax.fm/show/068/design-tips-for-developers), je m'amuse avec les flux RSS pour les podcasts dans [CLIs](https://github.com/sanity-io/podcast-to-sanity), [Express, et les fonctions Serverless.](https://github.com/sanity-io/Syntax) Cela implique l'analyse et la construction d'objets complexes avec de nombreux champs et informations. Comme vous traitez avec des données générées par les utilisateurs provenant de différentes sources, vous n'êtes pas assuré que les champs sont toujours remplis. Certains champs sont également optionnels. Et vous ne voulez pas sortir de balises sans valeurs dans un RSS XML ou [JSON FEED](https://jsonfeed.org).

Auparavant, je gérais cela en appliquant de nouvelles clés sur un objet comme ceci :

Ce n'est pas exactement fluide (mais cela fonctionne), et si vous avez beaucoup de champs, vous vous retrouvez rapidement avec beaucoup d'instructions `if-`. Je pouvais aussi faire des choses astucieuses en bouclant sur les clés de l'objet, etc. Cela signifierait un code un peu plus compliqué et vous ne obtenez pas une bonne idée de ce qu'est l'objet de données non plus.

Encore une fois, la nouvelle syntaxe ES6 vient à la rescousse. J'ai trouvé un modèle où j'ai pu réécrire le code comme ceci :

Cette fonction a quelques caractéristiques. La première est la [**destructuration d'objets de paramètres**](https://www.youtube.com/watch?v=-vR3a11Wzt0), qui est un bon modèle si vous voulez gérer beaucoup d'arguments dans une fonction. Au lieu de ce modèle :

```
function episodeParser(data) {  const id = data.id  const title = data.title  // et ainsi de suite...}
```

Vous écrivez :

```
function({id, title}) {  // et ainsi de suite...}
```

C'est aussi une bonne façon d'éviter d'avoir de nombreux arguments multiples dans une fonction. Notez également la partie `description = 'No summary'` de la destructuration de l'objet. C'est ce que nous appelons la valeur par défaut des paramètres. Cela signifie que si `description` est indéfini, il sera défini avec la chaîne `No summary` comme solution de repli.

La deuxième caractéristique est les trois points de la [**syntaxe de décomposition**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax) (`...`). Elle est utilisée pour "déballer" l'objet si la condition est vraie (c'est à cela que servent les `&&`) :

```
{  id: 'some-id',  ...(true && { optionalField: 'something'})}
```

```
// est la même chose que
```

```
{  id: 'some-id',  optionalField: 'something'}
```

Ce que vous obtenez, c'est une fonction concise et soignée qui est également facile à tester. Un point important à noter lors de l'utilisation de l'opérateur `&&` est que le nombre 0 sera considéré comme `false`. Vous devez donc faire attention aux types de données que vous utilisez.

Si nous mettons la fonction en action, cela ressemblerait à ceci :

Vous pouvez la voir en action dans notre implémentation de flux de podcast pour [express.js](https://github.com/sanity-io/Syntax/blob/master/routeHandlers/rss.js) et [netlify lambdas](https://github.com/sanity-io/Syntax/blob/master/functions/rss.js). Si vous souhaitez essayer Sanity.io pour ces implémentations vous-même, vous pouvez vous rendre sur [sanity.io/freecodecamp](https://sanity.io/freecodecamp?utm_source=freecodecamp&utm_medium=blog&utm_campaign=jq) et obtenir un plan développeur gratuit amélioré. ✨

*Originalement publié sur [www.sanity.io](https://www.sanity.io/blog/how-to-conditionally-build-an-object-in-es6).*