---
title: 10 nouvelles fonctionnalités JavaScript dans ES2020 que vous devez connaître
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-03T15:43:47.000Z'
originalURL: https://freecodecamp.org/news/javascript-new-features-es2020
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/es2020logo.jpg
tags:
- name: ecmascript
  slug: ecmascript
- name: JavaScript
  slug: javascript
seo_title: 10 nouvelles fonctionnalités JavaScript dans ES2020 que vous devez connaître
seo_desc: 'By Mehul Mohan

  Good news – the new ES2020 features are now finalised! This means we now have a
  complete idea of the changes happening in ES2020, the new and improved specification
  of JavaScript. So let''s see what those changes are.

  #1: BigInt

  BigInt,...'
---

Par Mehul Mohan

Bonne nouvelle – les nouvelles fonctionnalités d'ES2020 sont maintenant finalisées ! Cela signifie que nous avons maintenant une idée complète des changements apportés à ES2020, la nouvelle et améliorée spécification de JavaScript. Alors, voyons quels sont ces changements.

# #1: BigInt

BigInt, l'une des fonctionnalités les plus attendues en JavaScript, est enfin arrivée. Elle permet en réalité aux développeurs d'avoir une représentation entière beaucoup plus grande dans leur code JS pour le traitement des données.

Actuellement, le nombre maximum que vous pouvez stocker en tant qu'entier en JavaScript est `pow(2, 53) - 1`. Mais BigInt vous permet d'aller encore plus loin.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-03-at-8.21.47-PM.png)

Cependant, vous devez ajouter un `n` à la toute fin du nombre, comme vous pouvez le voir ci-dessus. Ce `n` indique qu'il s'agit d'un BigInt et qu'il doit être traité différemment par le moteur JavaScript (par le moteur v8 ou tout autre moteur qu'il utilise).

Cette amélioration n'est pas rétrocompatible car le système de nombres traditionnel est IEEE754 (qui ne peut tout simplement pas supporter des nombres de cette taille).

# #2: Import dynamique

Les imports dynamiques en JavaScript vous donnent la possibilité d'importer des fichiers JS dynamiquement en tant que modules dans votre application de manière native. C'est exactement comme vous le faites avec Webpack et Babel actuellement.

Cette fonctionnalité vous aidera à livrer du code à la demande, mieux connu sous le nom de code splitting, sans le surcoût de webpack ou d'autres bundlers de modules. Vous pouvez également charger du code conditionnellement dans un bloc if-else si vous le souhaitez.

Le bon point est que vous importez réellement un module, et donc il ne pollue jamais l'espace de noms global.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-03-at-8.26.27-PM.png)

# #3: Nullish Coalescing

Nullish coalescing ajoute la capacité de vérifier véritablement les valeurs `nullish` au lieu des valeurs `falsey`. Quelle est la différence entre les valeurs `nullish` et `falsey`, pourriez-vous demander ?

En JavaScript, de nombreuses valeurs sont `falsey`, comme les chaînes de caractères vides, le nombre 0, `undefined`, `null`, `false`, `NaN`, et ainsi de suite.

Cependant, de nombreuses fois, vous pourriez vouloir vérifier si une variable est nullish – c'est-à-dire si elle est soit `undefined` soit `null`, comme lorsque c'est acceptable pour une variable d'avoir une chaîne de caractères vide, ou même une valeur fausse.

Dans ce cas, vous utiliserez le nouvel opérateur nullish coalescing, `??`

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-03-at-8.47.03-PM.png)

Vous pouvez clairement voir comment l'opérateur OR retourne toujours une valeur truthy, tandis que l'opérateur nullish retourne une valeur non-nulllish.

# #4: Chaînage optionnel

La syntaxe de chaînage optionnel vous permet d'accéder aux propriétés d'objets profondément imbriquées sans vous soucier de l'existence ou non de la propriété. Si elle existe, super ! Sinon, `undefined` sera retourné.

Cela fonctionne non seulement sur les propriétés d'objets, mais aussi sur les appels de fonctions et les tableaux. Super pratique ! Voici un exemple :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-03-at-8.51.58-PM.png)

# #5: Promise.allSettled

La méthode `Promise.allSettled` accepte un tableau de Promesses et ne se résout que lorsque toutes sont réglées – soit résolues soit rejetées.

Cela n'était pas disponible nativement auparavant, même si certaines implémentations proches comme `race` et `all` étaient disponibles. Cela apporte "Exécutez simplement toutes les promesses – je ne me soucie pas des résultats" nativement à JavaScript.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-03-at-8.54.58-PM.png)

# #6: String#matchAll

`matchAll` est une nouvelle méthode ajoutée au prototype `String` qui est liée aux expressions régulières. Cela retourne un itérateur qui retourne tous les groupes correspondants les uns après les autres. Jetons un coup d'œil à un exemple rapide :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-03-at-8.59.14-PM.png)

# #7: globalThis

Si vous avez écrit du code JS multiplateforme qui pourrait s'exécuter sur Node, dans l'environnement du navigateur, et aussi à l'intérieur des web-workers, vous auriez eu du mal à obtenir l'objet global.

C'est parce qu'il est `window` pour les navigateurs, `global` pour Node, et `self` pour les web workers. S'il y a plus de runtimes, l'objet global sera différent pour eux également.

Vous auriez donc dû avoir votre propre implémentation de détection de runtime et ensuite utiliser le global correct – c'est-à-dire, jusqu'à maintenant.

ES2020 nous apporte `globalThis` qui fait toujours référence à l'objet global, peu importe où vous exécutez votre code :

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-03-at-9.02.27-PM.png)

# #8: Exportations d'espace de noms de module

Dans les modules JavaScript, il était déjà possible d'utiliser la syntaxe suivante :

```js
import * as utils from './utils.mjs'
```

Cependant, aucune syntaxe `export` symétrique n'existait, jusqu'à maintenant :

```js
export * as utils from './utils.mjs'
```

Cela est équivalent à ce qui suit :

```js
import * as utils from './utils.mjs'
export { utils }
```

# #9: Ordre bien défini pour for-in

La spécification ECMA ne spécifiait pas dans quel ordre `for (x in y)` devait s'exécuter. Même si les navigateurs avaient implémenté un ordre cohérent de leur propre chef avant maintenant, cela a été officiellement standardisé dans ES2020.

# #10: import.meta

L'objet `import.meta` a été créé par l'implémentation ECMAScript, avec un prototype [`null`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null).

Considérons un module, `module.js` :

```html
<script type="module" src="module.js"></script>
```

Vous pouvez accéder aux métainformations sur le module en utilisant l'objet `import.meta` :

```js
console.log(import.meta); // { url: "file:///home/user/module.js" }
```

Il retourne un objet avec une propriété `url` indiquant l'URL de base du module. Cela sera soit l'URL à partir de laquelle le script a été obtenu (pour les scripts externes), soit l'URL de base du document contenant le script (pour les scripts en ligne).

# Conclusion

J'adore la cohérence et la rapidité avec lesquelles la communauté JavaScript a évolué et évolue. C'est incroyable et vraiment merveilleux de voir comment JavaScript est passé d'un langage qui était hué il y a 10 ans à l'un des langages les plus forts, les plus flexibles et les plus polyvalents de tous les temps aujourd'hui.

Souhaitez-vous apprendre JavaScript et d'autres langages de programmation d'une manière complètement nouvelle ? Rendez-vous sur une [nouvelle plateforme pour les développeurs](https://codedamn.com) sur laquelle je travaille pour l'essayer dès aujourd'hui !

Quelle est votre fonctionnalité préférée d'ES2020 ? Parlez-moi-en en tweettant et en me connectant sur [Twitter](https://twitter.com/mehulmpt) et [Instagram](https://instagram.com/mehulmpt) !

Ceci est un article de blog composé à partir de ma vidéo qui traite du même sujet. Cela signifierait le monde pour moi si vous pouviez lui montrer un peu d'amour !

%[https://www.youtube.com/watch?v=Fag_8QjBwtY]