---
title: Comment rendre vos transformations de données plus efficaces en utilisant des
  transducteurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-20T10:57:07.000Z'
originalURL: https://freecodecamp.org/news/efficient-data-transformations-using-transducers-c779043ba655
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3kXGy7LMUX2qPG3gapZD5Q.jpeg
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
seo_title: Comment rendre vos transformations de données plus efficaces en utilisant
  des transducteurs
seo_desc: 'By Guido Schmitz

  Transforming large collections of data can be expensive, especially when you’re
  using higher order functions like map and filter.

  This article will show the power of transducers to create efficient data transformation
  functions, whic...'
---

Par Guido Schmitz

Transformer de grandes collections de données peut être coûteux, surtout lorsque vous utilisez des [fonctions d'ordre supérieur](https://medium.freecodecamp.org/higher-order-functions-in-javascript-d9101f9cf528) comme _map_ et _filter_.

Cet article montrera la puissance des transducteurs pour créer des fonctions de transformation de données efficaces, qui ne créent pas de collections temporaires. Les collections temporaires sont créées lorsque les fonctions _map_ et _filter_ sont enchaînées. Cela est dû au fait que ces fonctions retournent une nouvelle collection et transmettent le résultat à la fonction suivante.

Imaginez avoir des enregistrements de **1 000 000** de personnes et vouloir créer un sous-ensemble de "noms de femmes âgées de plus de 18 ans vivant aux Pays-Bas". Il existe différentes façons de résoudre ce problème, mais commençons par l'approche d'_enchaînement_.

Si cette approche est nouvelle pour vous, ou si vous souhaitez en apprendre davantage, j'ai écrit un article de blog sur l'utilisation des [fonctions d'ordre supérieur](https://medium.freecodecamp.org/higher-order-functions-in-javascript-d9101f9cf528).

```
const ageAbove18 = (person) => person.age > 18;
const isFemale = (person) => person.gender === 'female';
const livesInTheNetherlands = (person) => person.country === 'NL';
const pickFullName = (person) => person.fullName;
```

```
const output = bigCollectionOfData
  .filter(livesInTheNetherlands)
  .filter(isFemale)
  .filter(ageAbove18)
  .map(pickFullName);
```

Ci-dessous se trouve la visualisation de l'utilisation de l'approche enchaînée qui crée des tableaux temporaires. Imaginez le coût de parcourir 1 000 000 d'enregistrements 3 fois !

![Image](https://cdn-media-1.freecodecamp.org/images/G7mX8Ht-mfOiYsTYYv-kesUmfmOfrdYVo74O)

Bien sûr, les collections filtrées seront réduites d'une certaine quantité, mais cela reste assez coûteux.

Une idée clé, cependant, est que _map_ et _filter_ peuvent être définis en utilisant _reduce_. Implémentons le code ci-dessus en termes de _reduce_.

```
const mapReducer = (mapper) => (result, input) => {
  return result.concat(mapper(input));
};
```

```
const filterReducer = (predicate) => (result, input) => {
  return predicate(input) ? result.concat(input) : result;
};
```

```
const personRequirements = (person) => ageAbove18(person)
  && isFemale(person)
  && livesInTheNetherlands(person);
```

```
const output = bigCollectionOfData
  .reduce(filterReducer(personRequirements), [])
  .reduce(mapReducer(pickFullName), []);
```

Nous pouvons simplifier davantage le _filterReducer_ en utilisant la [**composition de fonctions**](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-function-composition-20dfb109a1a0).

```
filterReducer(compose(ageAbove18, isFemale, livesInTheNetherlands));
```

En utilisant cette approche, nous réduisons (haha !) le nombre de fois où nous créons un tableau temporaire. Ci-dessous se trouve une visualisation de la transformation lors de l'utilisation de l'approche _reduce_.

![Image](https://cdn-media-1.freecodecamp.org/images/dtnQEQo-2hzZ25uM-ycsYAbh8MCV51WRuvJs)

Magnifique, n'est-ce pas ? Mais nous parlions de transducteurs. Où sont nos transducteurs ?
Il s'avère que le _filterReducer_ et le _mapReducer_ que nous avons créés sont des **fonctions de réduction**. Nous pouvons l'exprimer comme suit :

```
reducing-function :: result, input -> result
```

Les transducteurs sont des fonctions qui acceptent une **fonction de réduction** et retournent une fonction de réduction. Cela peut être exprimé comme suit :

```
transducer :: (result, input -> result) -> (result, input -> result)
```

La partie la plus intéressante est que les transducteurs sont approximativement symétriques dans leur signature de type. Ils prennent une fonction de réduction et en retournent une autre.

Grâce à cela, nous pouvons composer n'importe quel nombre de transducteurs en utilisant la composition de fonctions.

#### **Créer vos propres transducteurs**

Espérons que tout commence à avoir plus de sens maintenant. Créons nos propres fonctions de transducteurs pour _map_ et _filter_.

```
const mapTransducer = (mapper) => (reducingFunction) => {
  return (result, input) => reducingFunction(result, mapper(input));
}
```

```
const filterTransducer = (predicate) => (reducingFunction) => {
  return (result, input) => predicate(input)
    ? reducingFunction(result, input)
    : result;
}
```

En utilisant les transducteurs que nous avons créés ci-dessus, transformons quelques nombres. Nous utiliserons la fonction [_compose_](http://ramdajs.com/docs/#compose) de RamdaJS.

[**RamdaJS**](http://ramdajs.com) est une bibliothèque qui fournit des méthodes fonctionnelles pratiques et est spécifiquement conçue pour les styles de programmation fonctionnelle.

```
const concatReducer = (result, input) => result.concat(input);
const lowerThan6 = filterTransducer((value) => value < 6);
const double = mapTransducer((value) => value * 2);
```

```
const numbers = [1, 2, 3];
```

```
// Utilisation de la composition de Ramda ici
const xform = R.compose(double, lowerThan6);
```

```
const output = numbers.reduce(xform(concatReducer), []); // [2, 4]
```

Le _concatReducer_ est appelé la **fonction itérative**. Cela sera appelé à chaque itération et sera responsable de la transformation de la sortie de la fonction de transducteur.

Dans cet exemple, nous concaténons simplement le résultat. Parce que chaque transducteur n'accepte qu'une fonction de réduction, nous ne pouvons pas utiliser _value.concat_.

Lorsque nous composons plusieurs transducteurs en une seule fonction, la plupart du temps, cela s'appelle un transducteur _xform_. Donc, lorsque vous voyez cela quelque part, vous savez ce que cela signifie.

#### **Composition de plusieurs transducteurs**

Nous avons utilisé la composition de fonctions ordinaire dans l'exemple précédent, et vous vous demandez peut-être quel est l'ordre d'évaluation. Bien que la composition de fonctions applique les fonctions de droite à gauche, les transformations seront en réalité évaluées de gauche à droite au moment de l'exécution — ce qui est beaucoup plus intuitif pour ceux d'entre nous qui lisent dans des langues de gauche à droite.

Il faut un peu de réflexion pour comprendre pourquoi c'est vrai : étant donné notre transducteur _double_ qui retourne une fonction de réduction, et notre transducteur _lowerThan6_ qui retourne également une fonction de réduction, lorsque vous composez _double_ et _lowerThan6_, la sortie de _double_ sera transmise à _lowerThan6_, qui retournera ensuite la fonction de réduction de _lowerThan6_. Ainsi, _double_ est le résultat de la composition et l'ordre d'évaluation est effectivement de gauche à droite.

J'ai créé un exemple JSBin [**ici**](https://jsbin.com/kezugajaqa/1/edit?js,console) avec quelques instructions _console.log_, afin que vous puissiez le consulter par vous-même.

#### **Utilisation de RamdaJS pour améliorer la lisibilité**

Puisque les transducteurs sont un exemple parfait pour un style de programmation fonctionnelle, examinons comment Ramda peut nous aider en utilisant leur ensemble de méthodes.

```
const lowerThan6 = R.filter((value) => value < 6);
const double = R.map((value) => value * 2);
const numbers = [1, 2, 3];
```

```
const xform = R.compose(double, lowerThan6);
```

```
const output = R.into([], xform, numbers); // [2,4]
```

Avec Ramda, nous pouvons utiliser leurs méthodes _map_ et _filter_. Cela est dû au fait que la méthode interne [_reduce_](https://github.com/ramda/ramda/blob/v0.25.0/source/internal/_reduce.js) de Ramda utilise le [Protocole de Transducteur](https://github.com/cognitect-labs/transducers-js#the-transducer-protocol) sous le capot.

> _"Le but du Protocole de Transducteur est que toutes les implémentations de transducteurs JavaScript interopèrent indépendamment de l'API de surface. Il appelle les transducteurs indépendamment du contexte de leurs sources d'entrée et de sortie et spécifie uniquement l'essence de la transformation en termes d'élément individuel._
> _Parce que les transducteurs sont découplés des sources d'entrée ou de sortie, ils peuvent être utilisés dans de nombreux processus différents — collections, flux, canaux, observables, etc. Les transducteurs se composent directement, sans connaissance de l'entrée ou création d'agrégats intermédiaires."_

#### **Conclusion**

Les transducteurs sont un moyen puissant et composable de construire des transformations que vous pouvez réutiliser dans de nombreux contextes. Une fois que vous avez un transducteur, vous pouvez faire un ensemble ouvert de choses.

Ils sont particulièrement utiles lors de la transformation de grands ensembles de données, mais vous pouvez également utiliser le même transducteur pour transformer un seul enregistrement.

Si vous souhaitez en apprendre davantage sur ce sujet, je recommande les articles suivants :

[https://clojure.org/reference/transducers](https://clojure.org/reference/transducers)
[http://blog.cognitect.com/blog/2014/8/6/transducers-are-coming](http://blog.cognitect.com/blog/2014/8/6/transducers-are-coming)
[https://github.com/cognitect-labs/transducers-js#the-transducer-protocol](https://github.com/cognitect-labs/transducers-js#the-transducer-protocol)

#### ?? Si vous avez aimé cet article, cliquez sur ce bouton d'applaudissements ci-dessous ?. Cela signifierait beaucoup pour moi et cela aide d'autres personnes à voir ce post.

#### Suivez-moi pour être notifié de plus de contenu de programmation comme celui-ci.