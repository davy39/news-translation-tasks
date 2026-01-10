---
title: Qu'est-ce qu'une fonction pure en JavaScript ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-03T21:31:37.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-pure-function-in-javascript-acb887375dfe
coverImage: https://cdn-media-1.freecodecamp.org/images/0*4rGYQyYm_m8Byoyj.png
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
seo_title: Qu'est-ce qu'une fonction pure en JavaScript ?
seo_desc: 'By Yazeed Bzadough

  Pure functions are the atomic building blocks in functional programming. They are
  adored for their simplicity and testability.

  This post covers a quick checklist to tell if a function’s pure or not.


  The Checklist

  A function must p...'
---

Par Yazeed Bzadough

Les fonctions pures sont les éléments de base atomiques en programmation fonctionnelle. Elles sont adorées pour leur simplicité et leur facilité de test.

Cet article couvre une liste de vérification rapide pour déterminer si une fonction est pure ou non.

![](https://cdn-media-1.freecodecamp.org/images/0*a_yub2gTwY-1eK8j.png)

### La liste de vérification

Une fonction doit passer deux tests pour être considérée comme "pure" :

1. Les mêmes entrées retournent **toujours** les mêmes sorties
2. Aucun effet de bord

Examinons chacun d'eux.

### 1. Même entrée => Même sortie

Comparez ceci :

```js
const add = (x, y) => x + y;

add(2, 4); // 6
```

À ceci :

```js
let x = 2;

const add = (y) => {
  x += y;
};

add(4); // x === 6 (la première fois)
```

#### Fonctions pures = Résultats cohérents

Le premier exemple retourne une valeur basée sur les paramètres donnés, peu importe où/quand vous l'appelez.

Si vous passez `2` et `4`, vous obtiendrez toujours `6`.

Rien d'autre n'affecte la sortie.

#### Fonctions impures = Résultats incohérents

Le deuxième exemple ne retourne rien. Il repose sur un **état partagé** pour faire son travail en incrémentant une variable en dehors de sa propre portée.

Ce modèle est le cauchemar des développeurs.

L'**état partagé** introduit une dépendance temporelle. Vous obtenez différents résultats selon le moment où vous appelez la fonction. La première fois, le résultat est `6`, la fois suivante `10`, et ainsi de suite.

#### Quelle version est la plus facile à comprendre ?

Laquelle est la moins susceptible de générer des bugs qui ne se produisent que dans certaines conditions ?

Laquelle est la plus susceptible de réussir dans un environnement multithread où les dépendances temporelles peuvent briser le système ?

Definitely the first one.

### 2. Aucun effet de bord

![](https://cdn-media-1.freecodecamp.org/images/0*4rGYQyYm_m8Byoyj.png)

Ce test lui-même est une liste de vérification. Voici quelques exemples d'effets de bord :

1. Mutation de votre entrée
2. `console.log`
3. Appels HTTP (AJAX/fetch)
4. Modification du système de fichiers (fs)
5. Interrogation du DOM

En gros, tout travail qu'une fonction effectue et qui n'est pas lié au calcul de la sortie finale.

Voici une fonction impure avec un effet de bord.

#### Pas si grave

```js
const impureDouble = (x) => {
  console.log('doubling', x);

  return x * 2;
};

const result = impureDouble(4);
console.log({ result });
```

`console.log` est l'effet de bord ici, mais en pratique, cela ne nous fera pas de mal. Nous obtiendrons toujours les mêmes sorties, étant donné les mêmes entrées.

_Cela_, cependant, peut causer un problème.

#### Changement "impur" d'un objet

```js
const impureAssoc = (key, value, object) => {
  object[key] = value;
};

const person = {
  name: 'Bobo'
};

const result = impureAssoc('shoeSize', 400, person);

console.log({
  person,
  result
});
```

La variable `person` a été changée pour toujours parce que notre fonction a introduit une instruction d'assignation.

L'état partagé signifie que l'impact de `impureAssoc` n'est plus entièrement évident. Comprendre son effet sur un système implique maintenant de suivre chaque variable qu'elle a jamais touchée et de connaître leurs historiques.

> État partagé = dépendances temporelles.

Nous pouvons purifier `impureAssoc` en retournant simplement un nouvel objet avec les propriétés souhaitées.

#### Purification

```js
const pureAssoc = (key, value, object) => ({
  ...object,
  [key]: value
});

const person = {
  name: 'Bobo'
};

const result = pureAssoc('shoeSize', 400, person);

console.log({
  person,
  result
});
```

Maintenant, `pureAssoc` retourne un résultat testable et nous ne nous inquiéterons jamais de savoir si elle a muté quelque chose ailleurs.

Vous pourriez même faire ce qui suit et rester pur :

#### Une autre façon pure

```js
const pureAssoc = (key, value, object) => {
  const newObject = { ...object };

  newObject[key] = value;

  return newObject;
};

const person = {
  name: 'Bobo'
};

const result = pureAssoc('shoeSize', 400, person);

console.log({
  person,
  result
});
```

Muter votre entrée peut être dangereux, mais muter une copie de celle-ci ne pose pas de problème. Notre résultat final est toujours une fonction testable et prévisible qui fonctionne peu importe où/quand vous l'appelez.

La mutation est limitée à cette petite portée et vous retournez toujours une valeur.

### Clonage profond des objets

Attention ! L'utilisation de l'opérateur de propagation `...` crée une copie **superficielle** d'un objet. Les copies superficielles ne sont pas sûres contre les mutations imbriquées.

Merci à [Rodrigo Fernández Díaz](https://medium.com/@rodrigo_98972) pour avoir attiré mon attention sur ce point !

#### Mutation imbriquée non sécurisée

```js
const person = {
  name: 'Bobo',
  address: { street: 'Main Street', number: 123 }
};

const shallowPersonClone = { ...person };
shallowPersonClone.address.number = 456;

console.log({ person, shallowPersonClone });
```

![](https://cdn-media-1.freecodecamp.org/images/1*SQ9xC_YZWBtp6B0wzNojuA.png)

Les deux `person` et `shallowPersonClone` ont été mutés parce que leurs enfants partagent la même référence !

#### Mutation imbriquée sécurisée

Pour muter en toute sécurité les propriétés imbriquées, nous avons besoin d'un clone **profond**.

```js
const person = {
  name: 'Bobo',
  address: { street: 'Main Street', number: 123 }
};

const deepPersonClone = JSON.parse(JSON.stringify(person));
deepPersonClone.address.number = 456;

console.log({ person, deepPersonClone });
```

![](https://cdn-media-1.freecodecamp.org/images/1*jHvmu2WnepV_UbhIQw-9vQ.png)

Maintenant, vous êtes garanti en sécurité parce qu'ils sont vraiment deux entités séparées !

### Résumé

![](https://cdn-media-1.freecodecamp.org/images/0*_FwSya9ut_O6gmfe.png)

- Une fonction est pure si elle est exemptée d'effets de bord et retourne la même sortie, étant donné la même entrée.
- Les effets de bord incluent : la mutation de l'entrée, les appels HTTP, l'écriture sur le disque, l'impression à l'écran.
- Vous pouvez cloner en toute sécurité, puis muter, votre entrée. Laissez simplement l'original intact.
- La syntaxe de propagation (`...`) est le moyen le plus facile de cloner superficiellement des objets.
- `JSON.parse(JSON.stringify(object))` est le moyen le plus facile de cloner profondément des objets. Merci encore à [Rodrigo Fernández Díaz](https://medium.com/@rodrigo_98972) !

### Mon cours gratuit

Ce tutoriel provient de **mon cours entièrement gratuit** sur Educative.io, [Functional Programming Patterns With RamdaJS](https://www.educative.io/collection/5070627052453888/5738600293466112?authorName=Yazeed%20Bzadough) !

Veuillez envisager de le suivre/le partager si vous avez aimé ce contenu.

Il est rempli de leçons, de graphiques, d'exercices et d'exemples de code exécutables pour vous enseigner un style de programmation fonctionnelle de base en utilisant RamdaJS.

Merci pour la lecture ! À la prochaine.