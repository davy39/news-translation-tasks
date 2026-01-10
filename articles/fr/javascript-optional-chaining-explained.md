---
title: L'opérateur de chaînage optionnel `?.` en JavaScript expliqué - Fonctionnement
  et cas d'usage
subtitle: ''
author: Shruti Kapoor
co_authors: []
series: null
date: '2020-08-25T15:39:34.000Z'
originalURL: https://freecodecamp.org/news/javascript-optional-chaining-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c990e740569d1a4ca1d97.jpg
tags:
- name: Babel
  slug: babel
- name: JavaScript
  slug: javascript
seo_title: L'opérateur de chaînage optionnel `?.` en JavaScript expliqué - Fonctionnement
  et cas d'usage
seo_desc: "What is optional chaining?\nOptional chaining, represented by ?. in JavaScript,\
  \ is a new feature introduced in ES2020. \nOptional chaining changes the way properties\
  \ are accessed from deeply nested objects. It fixes the problem of having to do\
  \ multiple..."
---

## Qu'est-ce que le chaînage optionnel ?

Le chaînage optionnel, représenté par `?.` en JavaScript, est une nouvelle fonctionnalité introduite dans ES2020.

Le chaînage optionnel modifie la manière d'accéder aux propriétés d'objets profondément imbriqués. Il résout le problème des multiples vérifications de nullité lors de l'accès à une longue chaîne de propriétés d'objet en JavaScript.

Statut actuel : `Proposition ECMAScript à l'étape 4 du processus.` : https://github.com/tc39/proposal-optional-chaining
                
## Cas d'usage

1. Accéder à des propriétés potentiellement `null` ou `undefined` d'un objet.
2. Obtenir des résultats d'une variable qui peut ne pas être encore disponible.
3. Obtenir des valeurs par défaut.
4. Accéder à de longues chaînes de propriétés.

Imaginez que vous attendiez qu'une API retourne un objet de ce type :

```javascript
obj = {
  prop1: {
    prop2: {
      someProp: "value"
    }
  }
};
```

Mais vous ne savez peut-être pas si chacun de ces champs est disponible à l'avance. Certains peuvent ne pas avoir été renvoyés par l'API, ou peuvent être revenus avec des valeurs null.

Voici un exemple :

```javascript
//attendu
obj = {
  id: 9216,
  children: [
    { id: 123, children: null },
    { id: 124, children: [{ id: 1233, children: null }] }
  ]
};

//réel
obj = {
  id: 9216,
  children: null
};
```

Cela arrive très souvent avec les fonctions qui appellent des API. Vous avez peut-être vu du code dans React qui tente de se prémunir contre ces problèmes comme ceci :

```jsx
render = () => {
  const obj = {
    prop1: {
      prop2: {
        someProp: "value",
      },
    },
  };

  return (
    <div>
      {obj && obj.prop1 && obj.prop1.prop2 && obj.prop1.prop2.someProp && (
        <div>{obj.prop1.prop2.someProp}</div>
      )}
    </div>
  );
};

```

Pour mieux se préparer à ce problème, nous avons souvent utilisé `Lodash` dans le passé, spécifiquement la méthode `_.get` :

```javascript
_.get(obj, 'prop1.prop2.someProp');

```

Cela retourne `undefined` si l'une de ces propriétés est `undefined`. **Le chaînage optionnel est exactement cela** ! Maintenant, au lieu d'utiliser une bibliothèque externe, cette fonctionnalité est intégrée.


## Comment fonctionne le chaînage optionnel ?

`?.` peut être utilisé pour enchaîner des propriétés qui peuvent être `null` ou `undefined`.

```
const propNeeded = obj?.prop1?.prop2?.someProp;

```

Si l'une de ces propriétés enchaînées est `null` ou `undefined`, JavaScript retournera `undefined`.

Que faire si nous voulons retourner quelque chose de significatif ? Essayez ceci :

```javascript
let familyTree = {
    us: {
        children: {}
    }
}


// avec _.get
const grandChildren = _.get(familyTree, 'us.children.theirChildren', 'got no kids' );

//avec chaînage optionnel et coalescence de null
const nullCoalescing = familyTree?.us?.children?.theirChildren ?? 'got no kids'
console.log(nullCoalescing) //got no kids

```

Cela fonctionne également pour les objets qui peuvent être `null` ou `undefined` :

```
let user;
console.log(user?.id) // undefined

```


## Comment obtenir cette nouvelle fonctionnalité

1. Essayez-la dans la console de votre navigateur : Il s'agit d'une ajout récent et les anciens navigateurs peuvent nécessiter des polyfills. Vous pouvez l'essayer dans Chrome ou Firefox dans la console du navigateur. Si cela ne fonctionne pas, essayez d'activer les fonctionnalités expérimentales de JavaScript en visitant `chrome://flags/` et en activant "Experimental JavaScript".
  
2. Essayez-la dans votre application Node en utilisant Babel :
```
{
  "plugins": ["@babel/plugin-proposal-optional-chaining"]
}
```

## Ressources

1. https://dmitripavlutin.com/javascript-optional-chaining/
2. Documentation de Babel : https://babeljs.io/docs/en/babel-plugin-proposal-optional-chaining

## TL;DR
Utilisez le chaînage optionnel `?.` pour les objets ou les longues chaînes de propriétés qui peuvent être `null` ou `undefined`. La syntaxe est la suivante :

```javascript
let user = {};
console.log(user?.id?.name)
```
****

Intéressé par plus de tutoriels et JSBytes de ma part ? [Inscrivez-vous à ma newsletter.](https://tinyletter.com/shrutikapoor) ou [suivez-moi sur Twitter](https://twitter.com/shrutikapoor08)