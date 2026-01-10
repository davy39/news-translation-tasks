---
title: Comment gérer l'intersection de la viewport et la mise au point de l'entrée
  avec des Hooks React personnalisés
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-15T15:39:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-viewport-intersection-and-input-focus-with-custom-react-hooks-1ec3403a8d80
coverImage: https://cdn-media-1.freecodecamp.org/images/1*itzX4RFL7kMtNv5UkvC_bA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Comment gérer l'intersection de la viewport et la mise au point de l'entrée
  avec des Hooks React personnalisés
seo_desc: 'By Dane David

  React Hooks have been here for a while, and there are many packages, recipes and
  discussions going on about the same. This article goes through a similar path. It
  explains through two custom hook implementations to show how well code ca...'
---

Par Dane David

[React Hooks](https://reactjs.org/docs/hooks-intro.html) existent depuis un certain temps, et il y a de nombreux packages, recettes et discussions à ce sujet. Cet article suit un chemin similaire. Il explique, à travers deux implémentations de hooks personnalisés, à quel point le code peut être réutilisé. Il peut exister des bibliothèques ou des gists qui offrent la fonctionnalité exacte (ou peut-être améliorée) que cet article explique. Il est toujours utile d'écrire du code adapté à vos besoins, un code avec lequel vous pouvez raisonner.

Cet article suppose une compréhension et une connaissance de base de React et des hooks React. Si ce n'est pas le cas, vous pouvez lire la documentation et en savoir plus sur l'API React Hooks.

#### L'installation

Au lieu d'être révélée à la fin, nous pouvons d'abord voir quelle fonctionnalité nous essayons de construire. La version live de ce que nous allons construire est hébergée ici : [https://danedavid.github.io/use-focus](https://danedavid.github.io/use-focus/).

L'application se compose d'une liste horizontale de composants React qui peuvent être parcourus. Chaque composant peut être différent ou identique (ici, deux types différents de composants sont utilisés, uniquement pour montrer que le code peut être réutilisé entre les composants). La seule chose qu'ils ont tous en commun : un champ de saisie.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EJfGOb35AOJ4j4M-AxVV6w.gif)
_L'élément dans la viewport est toujours l'élément actif (surligné en vert) et a le focus._

**Notre objectif** : Toujours faire en sorte que l'élément à l'intérieur de la viewport soit l'élément « actif ». Donner le focus au champ de saisie à l'intérieur de ce composant, tout au long du défilement.

Nous pouvons gérer un état `activeElement` à l'intérieur de notre composant racine, qui stocke un ID correspondant à l'élément actif à tout moment. Le code pour le composant racine est alors :

Les composants `NumberInputFormElement` et `TextInputFormElement` sont des composants très similaires. Le premier rend un `input[type="number"]`. Tandis que le second rend un champ de saisie de texte. C'est la seule différence.

#### useActiveOnIntersect

Le premier hook à ajouter est celui qui définira l'élément actif une fois que l'élément atteint la viewport. C'est-à-dire que le hook `useActiveOnIntersect` doit appeler `setActiveElement` passé depuis le parent, une fois que l'élément est dans la viewport. Il existe une API bien connue du navigateur pour cela : `window.IntersectionObserver`. Si vous n'êtes pas familier, je vous suggère de lire plus à ce sujet [ici](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API).

Le hook doit essentiellement créer une instance de `IntersectionObserver` et écouter quand il entre dans le champ de vision. Nous avons donné un attribut `id=intersector` à la `div` la plus externe. Cette `div` servira d'élément racine pour IntersectionObserver. L'élément doit écouter quand il est totalement (ou au moins à 95%) à l'intérieur de cet élément racine. Nous utilisons le hook `useEffect` pour enregistrer l'instance IntersectionObserver. Et nous passons une fonction de rappel qui invoque `setActiveElement` lors de l'intersection (dans notre cas, lorsque le ratio d'intersection est supérieur à 95%). Le code pour `useActiveOnIntersect` est donné ci-dessous :

Le hook fait ce qu'il est censé faire : enregistrer une instance `observer` qui écoute l'intersection avec l'élément racine, donné dans les options comme `document.querySelector('#intersector')`, et invoquer `setActiveElement` si l'élément est en intersection. `elementRef` est la référence React pointant vers l'élément conteneur DOM.

Comment `setActiveElement` sait-il quel élément est l'élément actif ? Nous allons le passer depuis l'intérieur du composant lorsque nous appelons ce hook :

```
useActiveOnIntersect(() => setActiveElement(id), containerEl);
```

Ici, `id` est la valeur à définir comme `activeElement` dans le composant `App`. `containerEl` est la référence React faisant référence au conteneur du champ de saisie.

#### useFocusOnActive

Maintenant que nous sommes sûrs que `activeElement` pointe toujours vers l'élément qui est à l'intérieur de la viewport (élément racine) à tout moment, nous devons nous assurer que le champ de saisie à l'intérieur du composant obtient le focus. Encore une fois, nous utilisons le hook `useEffect` pour focaliser le champ de saisie une fois qu'il est actif, et la fonction de nettoyage floute le champ de saisie une fois qu'il n'est plus l'élément actif. Le code est concis et direct :

`inputRef` est la référence React pointant vers le champ de saisie, et `active` est l'état actif de l'élément conteneur.

#### Conclusion

Le code pour un composant qui utilise ces deux hooks est donné ci-dessous :

Nous avons utilisé le hook `useRef` pour créer des références pour les éléments conteneur et de saisie et les passer à leurs hooks respectifs. La fonctionnalité peut même être écrite à l'intérieur d'un seul hook. La raison derrière l'écriture de deux hooks séparés est que chacun représente un effet différent.

Le code complet peut être trouvé ici : [https://github.com/danedavid/use-focus](https://github.com/danedavid/use-focus).

J'espère que cet article a été utile et court ! Allez-y et écrivez votre propre hook React personnalisé maintenant !

Si vous avez aimé l'article, cliquez sur le bouton d'applaudissements ci-dessous. Vous pouvez également me suivre sur medium ou [twitter](https://twitter.com/this_dane) pour plus de contenu !

Bon codage !