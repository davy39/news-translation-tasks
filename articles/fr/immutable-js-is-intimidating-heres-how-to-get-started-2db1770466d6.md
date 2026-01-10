---
title: Immutable.js est intimidant. Voici comment commencer.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-16T22:58:26.000Z'
originalURL: https://freecodecamp.org/news/immutable-js-is-intimidating-heres-how-to-get-started-2db1770466d6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*INNhwAgxu9lkEdMBz0hp9Q.png
tags:
- name: full stack
  slug: full-stack
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: Immutable.js est intimidant. Voici comment commencer.
seo_desc: 'By William Woodhead

  You hear that you should be using Immutable. You know you should, but you aren’t
  quite sure why. And when you go to the docs, the first snippet of code looks like
  this:

  identity<T>(value: T): T

  You think: Nah… maybe another time.

  ...'
---

Par William Woodhead

Vous entendez dire que vous devriez utiliser [Immutable](https://facebook.github.io/immutable-js/). Vous savez que vous devriez, mais vous n'êtes pas tout à fait sûr pourquoi. Et lorsque vous allez dans la [documentation](https://facebook.github.io/immutable-js/docs/#/), le premier extrait de code ressemble à ceci :

```
identity<T>(value: T): T
```

Vous pensez : Non... peut-être une autre fois.

Alors, voici une introduction simple et rapide pour vous lancer avec Immutable. Vous ne le regretterez pas :

_Chez [Pilcro](https://www.pilcro.com/?utm_source=medium&utm_medium=immutable&utm_campaign=awareness), nous avons introduit [Immutable](https://facebook.github.io/immutable-js/) dans nos applications il y a environ 12 mois. Cela a été l'une des meilleures décisions que nous ayons prises. Nos applications sont désormais beaucoup plus lisibles, robustes, sans bugs et prévisibles._

### **Les bases**

#### Conversion en Immutable

En JavaScript normal, nous connaissons deux types de données courants : **Object** `{}` et **Array** `[]`.

Pour les traduire en Immutable :

* **Object** `{}` devient **Map** `Map({})`
* **Array** `[]` devient **List** `List([])`

Pour convertir du JavaScript normal en Immutable, nous pouvons utiliser les fonctions **Map**, **List** ou **fromJS** que fournit Immutable :

```
import { Map, List, fromJS } from 'immutable';
```

```
// JavaScript normal
```

```
const person = {  name: 'Will',  pets: ['cat', 'dog']};
```

```
// Pour créer l'équivalent en Immutable :
```

```
const immutablePerson = Map({  name: 'Will',  pets: List(['cat', 'dog'])});
```

```
// Ou ...
```

```
const immutablePerson = fromJS(person);
```

`fromJS` est une fonction utile qui convertit les données imbriquées en Immutable. Elle crée des `Maps` et des `Lists` lors de la conversion.

#### Conversion d'Immutable vers JavaScript normal

Il est très simple de récupérer vos données d'Immutable vers du JavaScript classique. Il suffit d'appeler la méthode `.toJS()` sur votre objet Immutable.

```
import { Map } from 'immutable';
```

```
const immutablePerson = Map({ name: 'Will' });const person = immutablePerson.toJS();
```

```
console.log(person); // imprime { name: 'Will' };
```

> **_À noter : Les structures de données doivent être considérées comme SOIT du JavaScript classique SOIT de l'Immutable._**

### Commencez à utiliser Immutable

Avant d'expliquer pourquoi Immutable est si utile, voici trois exemples simples où Immutable peut vous aider immédiatement.

#### 1. Obtenir une valeur imbriquée d'un objet sans vérifier si elle existe

D'abord en JavaScript normal :

```
const data = { my: { nested: { name: 'Will' } } };
```

```
const goodName = data.my.nested.name;console.log(goodName); // imprime Will
```

```
const badName = data.my.lovely.name;// lance une erreur : 'Cannot read name of undefined'
```

Et maintenant en Immutable :

```
const data = fromJS({ my: { nested: { name: 'Will' } } });
```

```
const goodName = data.getIn(['my', 'nested', 'name']);console.log(goodName); // imprime Will
```

```
const badName = data.getIn(['my', 'lovely', 'name']);console.log(badName); // imprime undefined - aucune erreur lancée
```

Dans les exemples ci-dessus, le code JavaScript normal lance une erreur, alors que celui d'Immutable ne le fait pas.

C'est parce que nous utilisons la fonction `getIn()` pour obtenir une valeur imbriquée. Si le chemin de la clé n'existe pas (c'est-à-dire que l'objet n'est pas structuré comme vous le pensiez), il retourne undefined plutôt que de lancer une erreur.

Vous n'avez pas besoin de vérifier les valeurs undefined tout au long de la structure imbriquée comme vous le feriez en JavaScript normal :

```
if (data && data.my && data.my.nested && data.my.nested.name) { ...
```

Cette fonctionnalité simple rend votre code beaucoup plus lisible, moins verbeux et beaucoup plus robuste.

#### 2. Chaînage des manipulations

D'abord en JavaScript normal :

```
const pets = ['cat', 'dog'];pets.push('goldfish');pets.push('tortoise');console.log(pets); // imprime ['cat', 'dog', 'goldfish', 'tortoise'];
```

Maintenant en Immutable :

```
const pets = List(['cat', 'dog']);const finalPets = pets.push('goldfish').push('tortoise');
```

```
console.log(pets.toJS()); // imprime ['cat', 'dog'];
```

```
console.log(finalPets.toJS());// imprime ['cat', 'dog', 'goldfish', 'tortoise'];
```

Parce que `List.push()` retourne le résultat de l'opération, nous pouvons "chaîner" l'opération suivante directement dessus. En JavaScript normal, la fonction `push` retourne la longueur du nouveau tableau.

C'est un exemple très simple de chaînage, mais il illustre la vraie puissance d'Immutable.

Cela vous libère pour faire toutes sortes de manipulations de données de manière plus fonctionnelle et plus concise.

> **_À noter : Les opérations sur un objet Immutable retournent le résultat de l'opération._**

#### 3. Données immutables

Après tout, cela s'appelle Immutable, alors nous devons parler de pourquoi cela est important !

Disons que vous créez un objet Immutable et que vous le mettez à jour — avec Immutable, la structure de données initiale n'est pas modifiée. Elle est immutable. (en minuscules ici !)

```
const data = fromJS({ name: 'Will' });const newNameData = data.set('name', 'Susie');
```

```
console.log(data.get('name')); // imprime 'Will'console.log(newNameData.get('name')); // imprime 'Susie'
```

Dans cet exemple, nous pouvons voir comment l'objet "data" original n'est pas modifié. Cela signifie que vous n'aurez pas de comportement imprévisible lorsque vous mettez à jour le nom en "Susie".

Cette fonctionnalité simple est vraiment puissante, particulièrement lorsque vous construisez des applications complexes. C'est le fondement de ce qu'est Immutable.

> **_À noter : Les opérations sur un objet Immutable ne modifient pas l'objet, mais créent plutôt un nouvel objet._**

### Pourquoi Immutable est utile

Les développeurs de [Facebook](https://www.facebook.com) résument les avantages sur la [page d'accueil](https://facebook.github.io/immutable-js/) de la documentation, mais c'est assez difficile à lire. Voici mon avis sur pourquoi vous devriez commencer à utiliser Immutable :

#### Vos structures de données changent de manière prévisible

Parce que vos structures de données sont immutables, vous êtes responsable de la manière dont vos structures de données sont manipulées. Dans les applications web complexes, cela signifie que vous n'avez pas de problèmes de re-rendu étranges lorsque vous modifiez un peu de données qui sont accessibles pour l'UI.

#### **Manipulation robuste des données**

En utilisant Immutable pour manipuler les structures de données, vos manipulations elles-mêmes sont beaucoup moins sujettes aux erreurs. Immutable fait beaucoup de travail difficile pour vous — il attrape les erreurs, offre des valeurs par défaut et construit des structures de données imbriquées directement.

#### Code concis et lisible

La conception fonctionnelle d'Immutable peut être déroutante au début, mais une fois que vous vous y habituez, le chaînage de fonctions rend votre code beaucoup plus court et plus lisible. Cela est idéal pour les équipes travaillant sur la même base de code.

### Prochaines étapes

La courbe d'apprentissage est indéniablement difficile avec Immutable, mais cela en vaut vraiment la peine. Commencez simplement en jouant un peu avec.

Voici les points clés qui ont été notés au fur et à mesure. Si vous pouvez garder ces points à l'esprit, vous adopterez Immutable comme un canard à l'eau !

1. Les structures de données doivent être considérées comme SOIT du JavaScript classique SOIT de l'Immutable.
2. Les opérations sur un objet Immutable retournent le résultat de l'opération.
3. Les opérations sur un objet Immutable ne modifient pas l'objet lui-même, mais créent plutôt un nouvel objet.

Bonne chance !

_Si vous avez aimé cette histoire, merci de ? et de la partager avec d'autres. Merci également de consulter mon entreprise [Pilcro.com](https://www.pilcro.com/?utm_source=medium&utm_medium=immutable&utm_campaign=awareness). Pilcro est un logiciel de marque pour G-Suite — pour les marketeurs et les agences de marque._

![Image](https://cdn-media-1.freecodecamp.org/images/ntTfRnp-62XC61l4808bH5vhCSTaRhOs7opG)