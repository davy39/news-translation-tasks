---
title: Composition de fonctions en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-20T22:35:00.000Z'
originalURL: https://freecodecamp.org/news/function-composition-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c7a740569d1a4ca3270.jpg
tags:
- name: JavaScript
  slug: javascript
- name: toothbrush
  slug: toothbrush
seo_title: Composition de fonctions en JavaScript
seo_desc: 'Function composition is the pointwise application of one function to the
  result of another. Developers do it in a manual manner every day when they nest
  functions:

  compose = (fn1, fn2) => value => fn2(fn1(value))


  But this is hard to read. There is a...'
---

La composition de fonctions est l'application ponctuelle d'une fonction au résultat d'une autre. Les développeurs le font de manière manuelle tous les jours lorsqu'ils imbriquent des fonctions :

```javascript
compose = (fn1, fn2) => value => fn2(fn1(value))
```

Mais cela est difficile à lire. Il existe une meilleure façon en utilisant la composition de fonctions. Au lieu de les lire de l'intérieur vers l'extérieur :

```javascript
add2AndSquare = (n) => square(add2(n))
```

Nous pouvons utiliser une fonction d'ordre supérieur pour les enchaîner de manière ordonnée.

```javascript
add2AndSquare = compose( add2, square)
```

Une implémentation simple de compose serait :

```javascript
compose = (f1, f2) => value => f2( f1(value) );
```

Pour obtenir encore plus de flexibilité, nous pouvons utiliser la fonction reduceRight :

```javascript
compose = (...fns) => (initialVal) => fns.reduceRight((val, fn) => fn(val), initialVal);
```

Lire compose de gauche à droite permet un enchaînement clair des fonctions d'ordre supérieur. Des exemples concrets sont l'ajout d'authentifications, de journalisation et de propriétés de contexte. C'est une technique qui permet la réutilisabilité au plus haut niveau. Voici quelques exemples de son utilisation :

```javascript
// exemple
const add2        = (n) => n + 2;
const times2      = (n) => n * 2;
const times2add2  = compose(add2, times2);
const add6        = compose(add2, add2, add2);

times2add2(2);  // 6
add2tiems2(2);  // 8
add6(2);        // 8
```

Vous pourriez penser que cela relève de la programmation fonctionnelle avancée et que ce n'est pas pertinent pour la programmation frontend. Mais c'est aussi utile dans les applications monopages (Single Page Applications). Par exemple, vous pouvez ajouter un comportement à un composant React en utilisant des composants d'ordre supérieur :

```javascript
function logProps(InputComponent) {
  InputComponent.prototype.componentWillReceiveProps = function(nextProps) {
    console.log('Current props: ', this.props);
    console.log('Next props: ', nextProps);
  };
  return InputComponent;
}

// EnhancedComponent journalisera chaque fois que des props sont reçues
const EnhancedComponent = logProps(InputComponent);
```

En conclusion, la composition de fonctions permet la réutilisabilité de la fonctionnalité à un niveau très élevé. Si les fonctions sont bien structurées, cela permet aux développeurs de créer de nouveaux comportements basés sur des comportements existants.

Cela améliore également la lisibilité des implémentations. Au lieu d'imbriquer des fonctions, vous pouvez clairement enchaîner des fonctions et créer des fonctions d'ordre supérieur avec des noms significatifs.