---
title: Comment rendre un tableau de composants dans React
subtitle: ''
author: Matéu.sh
co_authors: []
series: null
date: '2024-02-27T19:18:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-render-array-of-components-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Array-components.png
tags:
- name: arrays
  slug: arrays
- name: components
  slug: components
- name: React
  slug: react
seo_title: Comment rendre un tableau de composants dans React
seo_desc: 'In this tutorial, I will show you how using indices to render an array
  of components in React can be problematic. I''ll also teach you how to mitigate
  array rendering issues with unique ids.

  As always, we''ll work on a real world example and solve prob...'
---

Dans ce tutoriel, je vais vous montrer comment l'utilisation d'indices pour rendre un tableau de composants dans React peut être problématique. Je vais également vous apprendre à atténuer les problèmes de rendu de tableau avec des identifiants uniques.

Comme toujours, nous travaillerons sur un exemple concret et résoudreons un problème auquel je me suis heurté en construisant mon jeu 2048 en React. Tous les extraits de code sont inspirés de ce projet. Si vous souhaitez examiner le code avant de lire cet article, vous pouvez [le trouver sur GitHub](https://mateuszsokola.github.io/2048-in-react/).

## Le jeu 2048

Permettez-moi d'expliquer d'abord les règles du jeu 2048. Le joueur doit combiner des tuiles qui ont les mêmes nombres jusqu'à atteindre le nombre 2048. Les tuiles ne peuvent contenir que des nombres qui représentent une puissance de deux à partir de 2 – cela signifie 2, 4, 8, 16, 32, et ainsi de suite – jusqu'à atteindre le nombre 2048. Le plateau a des dimensions de 4 x 4 tuiles, de sorte qu'il peut contenir jusqu'à 16 tuiles.

Voici un exemple :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/demo-1.gif)
_Aperçu du jeu 2048_

Dans cet article, je vais seulement vous apprendre à rendre des tableaux dans React et vous montrer quelques bonnes pratiques pour rendre des listes dans les composants React.

Malheureusement, nous ne pouvons pas créer le jeu entier car cela rendrait cet article confus. Mais si vous voulez le faire à partir de zéro, vous devriez envisager de vous inscrire à mon [cours sur Udemy](https://www.udemy.com/course/2048-in-react-and-nextjs/?referralCode=AC3FD6336BAB9C402106) où je vous guiderai à travers la création du jeu 2048 avec des animations dans React 18.

## **P**rérequis****

Avant de commencer, assurez-vous de connaître quelques bases de React. Rien de sophistiqué – assurez-vous simplement d'avoir travaillé avec React auparavant, sinon vous pourriez vous sentir un peu perdu.

Si vous ne connaissez pas encore React, freeCodeCamp propose un [cours React de 5 heures pour débutants](https://www.freecodecamp.org/news/learn-react-course/) alors n'hésitez pas à le regarder avant de lire cet article. Vous pouvez également vous inscrire à mon [cours React 18](https://www.udemy.com/course/2048-in-react-and-nextjs/?referralCode=AC3FD6336BAB9C402106).

Maintenant, commençons.

## **Comment rendre les éléments d'un tableau**

Comme je l'ai mentionné au début, le plateau de jeu a des dimensions de 4 x 4 tuiles. Cela signifie que la meilleure structure de données pour stocker les tuiles sur le plateau sera un tableau multidimensionnel, comme celui que vous voyez ci-dessous :

```js
const board = [
    [0, 0, 0, 0],
    [2, 0, 0, 0],
    [2, 0, 0, 0],
    [0, 0, 0, 0],
]
```

Malheureusement, cette structure de données sera coûteuse, car elle nécessite des boucles imbriquées itérant les unes sur les autres. C'est pourquoi j'ai décidé d'aplatir ce tableau en un tableau unidimensionnel :

```js
const tilesOnBoard = [0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0]
```

Comme vous pouvez le voir, il y a beaucoup d'éléments vides dans ce tableau, et cela laisse place à des améliorations supplémentaires. Nous pouvons réduire le nombre d'opérations en remplaçant les valeurs des tuiles par des objets contenant des informations sur les tuiles.

Par exemple, vous pouvez introduire un nouveau type pour stocker les métadonnées de chaque tuile comme ceci :

```ts
type TileModel = {
  position: [number, number];
  value: number;
};

```

Comme vous pouvez le voir, ce type de données rend les tuiles intelligentes. Chaque tuile connaîtra sa position et sa valeur. J'ai décidé de stocker la position sous forme de tableau de deux éléments. Ces éléments représenteront les coordonnées `x` et `y`. Plutôt que des pixels, j'utiliserai les indices de tableau sur le tableau de plateau que j'ai mentionné dans la première étape.

Améliorons maintenant le tableau `tilesOnBoard` et faisons en sorte qu'il ne stocke que les tuiles existantes sans valeurs vides :

```js
const tilesOnBoard = [
	{ position: [1, 0], value: 2 },
    { position: [2, 0], value: 2 },
]
```

Grâce à cette simplification, je peux rendre les tuiles en utilisant le simple foncteur `map` qui itérera à travers tous les éléments du tableau et créera des composants Tile à partir de ceux-ci.

```jsx
const renderTiles = () => {
  return tilesOnBoard.map((tile: TileModel, index: number) => (
    <Tile key={index} {...tile} />
  ));
};
```

Concentrons-nous un instant sur le deuxième argument du foncteur `map`. Comme vous pouvez le voir, il utilise l'index de l'élément du tableau `tilesOnBoard`. Je l'utilise comme propriété `key` pour initialiser les composants React – dans ce cas, les composants `Tile`.

Si vous n'avez jamais utilisé les props `key`, React a besoin de clés pour identifier quels éléments ont changé, sont ajoutés ou sont supprimés. Les clés doivent être attribuées à chaque élément à l'intérieur du tableau de composants.

C'est pourquoi j'ai attribué des indices de tableau à toutes les tuiles. Malheureusement, les indices de tableau ne sont pas les meilleurs identifiants uniques, comme vous pouvez le voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/array-indexes.gif)
_Comportement étrange lorsque les indices de tableau sont utilisés comme props de clé_

Il peut être difficile de repérer ce qui se passe ici, alors laissez-moi vous expliquer brièvement. En gros, React réutilise les éléments HTML existants pour rendre les nouvelles tuiles. Ce n'est pas un comportement intentionnel – au lieu de cela, j'aurais dû supprimer les tuiles fusionnées et créer une nouvelle tuile après chaque mouvement.

Mais pourquoi cela se produit-il ? Après que les tuiles sont fusionnées, une nouvelle tuile est créée, et cela signifie que le tableau a toujours deux éléments avec les mêmes indices de tableau.

React utilise un mécanisme appelé le Virtual DOM pour détecter les changements et modifier les éléments sur l'arbre DOM. Malheureusement, ce mécanisme est optimisé pour la vitesse de sorte qu'il n'analyse pas tout le composant mais seulement la prop `key`. Cela signifie que React ne peut pas différencier la création d'une nouvelle tuile d'un changement de style sur un élément div existant. C'est pourquoi nous rencontrons ce problème.

Pour confirmer que mon raisonnement est correct, prenons un bref aperçu de l'onglet _Element_ dans Chrome DevTools :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/reusing-html-elements.gif)
_Réutilisabilité des éléments DOM due aux indices de tableau utilisés comme props de clé_

Comme vous pouvez le voir, deux éléments div existants ont seulement changé leurs attributs de style mais rien n'a été ajouté ou supprimé. Ce n'est pas un comportement intentionnel, mais cela nous indique que les indices de tableau sont de mauvais identifiants uniques pour les composants React.

Si vous n'êtes pas familier avec les outils de développement Chrome, vous devriez lire mon article sur la mise en œuvre des [événements tactiles mobiles dans React 18](https://www.freecodecamp.org/news/how-to-build-mobile-swiping-component-in-react/) où je fais une plongée profonde sur la façon de l'utiliser.

## **Identifiants uniques comme props de clé**

Pour résoudre les problèmes de rendu de tableau dans React, nous devrons utiliser des identifiants uniques tels que des ids incrémentiels, des uuids, ou autres. Pour me concentrer sur l'essentiel, j'ai décidé d'utiliser une bibliothèque appelée `uid`, que vous pouvez installer en exécutant la commande suivante dans votre terminal :

```bash
npm install --save uid
```

Maintenant, je dois modifier les tuiles pour supporter ces identifiants. Tout d'abord, j'ai ajouté une nouvelle propriété `id` dans le type de métadonnées des tuiles :

```ts
type TileModel = {
  id: string;
  position: [number, number];
  value: number;
};
```

Et j'ai attribué un id à chaque élément dans le tableau `tilesOnBoard` (c'est là que la bibliothèque `uid` entre en jeu) :

```js
const tilesOnBoard = [
	{ id: uid(), position: [1, 0], value: 2 },
    { id: uid(), position: [2, 0], value: 2 },
]
```

La dernière chose que j'ai faite a été de changer l'assistant `renderTiles` :

```jsx
const renderTiles = () => {
  return tilesOnBoard.map((tile: TileModel) => (
    <Tile key={tile.id} {...tile} />
  ));
};
```

Comme vous pouvez le voir, j'ai supprimé l'argument d'index du foncteur `map`, et remplacé la prop `key` par un id unique que j'ai ajouté aux métadonnées des tuiles.

Maintenant, le jeu 2048 fonctionne comme un charme :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/array-tile-ids.gif)

## **Conclusion**

Dans cet article, vous avez appris que les indices ne sont pas la meilleure option pour rendre des tableaux de composants dans React et qu'ils peuvent conduire à des comportements étranges. Si vous ne devez retenir qu'une seule chose de cet article, c'est que vous devez toujours utiliser des identifiants uniques comme prop `key` des composants React.

Vous voulez apprendre plus de trucs comme celui-ci ? Vous devriez rejoindre mon [cours React 18 sur Udemy](https://www.udemy.com/course/2048-in-react-and-nextjs/?referralCode=AC3FD6336BAB9C402106). Je vous apprendrai à **créer un jeu 2048 en React** à partir de zéro et vous montrerai des solutions aux erreurs les plus courantes que commettent les développeurs React.