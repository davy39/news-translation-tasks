---
title: Que signifie 'this' en JavaScript ? Le mot-clé this expliqué avec des exemples
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-06-15T21:19:12.000Z'
originalURL: https://freecodecamp.org/news/what-is-this-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/0001-2550990419_20210608_114432_0000.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Que signifie 'this' en JavaScript ? Le mot-clé this expliqué avec des exemples
seo_desc: 'To understand what this truly means in JavaScript, let''s take a look at
  a very similar concept in the English Language: Polysemy.

  Let''s consider the word "run". Run is a single word which could mean many different
  things depending on the context.


  “I...'
---

Pour comprendre ce que `this` signifie vraiment en JavaScript, examinons un concept très similaire en langue anglaise : **la polysémie**.

Prenons le mot "**run**". Run est un mot unique qui peut signifier beaucoup de choses différentes selon le **contexte**.

* "I will run home" – signifie se déplacer rapidement à pied

* "She ran the 1500m" – signifie courir dans une course

* "He is running for president" – signifie briguer un poste officiel

* "The app is running" – signifie que l'application logicielle est toujours ouverte et active

* "Go for a run" – signifie courir comme forme d'exercice

*et la liste continue.*

Un scénario similaire se produit lorsque vous utilisez le mot-clé `this` dans votre code JavaScript. Lorsque vous le faites, il se résout automatiquement en un objet ou une portée en fonction du contexte dans lequel il a été défini.

Quels sont les contextes possibles ? Et comment pouvons-nous utiliser ces informations pour déduire à quel objet un appel `this` se résoudra ?

## Contexte de `this`

Lorsqu'il est utilisé dans une fonction, le mot-clé `this` pointe simplement vers un objet auquel il est lié. Il répond à la question de **où il doit obtenir une valeur ou des données** :

```js
function alert() { 
  console.log(this.name + ' is calling'); 
}
```

Dans la fonction ci-dessus, le mot-clé `this` fait référence à un objet auquel il est lié **donc il obtient la propriété "name" de là**.

Mais comment savez-vous à quel objet la fonction est liée ? Comment découvrir à quoi `this` fait référence ?

Pour ce faire, nous devons examiner en détail comment les fonctions sont liées aux objets.

## Types de liaison en JavaScript

Il existe généralement quatre types de liaisons :

* Liaison par défaut

* Liaison implicite

* Liaison explicite

* Liaison d'appel de constructeur

### Liaison par défaut en JavaScript

L'une des premières règles à retenir est que si la fonction contenant une référence `this` est une **fonction autonome**, alors cette fonction est liée à l'**objet global**.

```javascript
function alert() { 
  console.log(this.name + ' is calling'); 
}

const name = 'Kingsley'; 
alert(); // Kingsley is calling
```

Comme vous pouvez le voir, `name()` est une fonction autonome et non attachée, donc elle est liée à la **portée globale**. Par conséquent, la référence `this.name` se résout en la variable globale `const name = 'Kingsley'`.

Cette règle, cependant, ne s'applique pas si `name()` était définie en mode strict :

```js
function alert() { 
  'use strict'; 
  console.log(this.name + ' is calling'); 
}

const name = 'Kingsley'; 
alert(); // TypeError: `this` est `undefined`
```

En mode strict, la référence `this` est définie sur undefined.

### Liaison implicite en JavaScript

Un autre scénario à surveiller est de savoir si la fonction est attachée à un objet (son contexte) **au site d'appel**.

Selon la règle de liaison en JavaScript, une fonction peut utiliser un objet comme son contexte uniquement si cet objet est lié à elle au site d'appel. Cette forme de liaison est connue sous le nom de liaison implicite.

Voici ce que je veux dire par là :

```js
function alert() { 
  console.log(this.age + ' years old'); 
}

const myObj = {
  age: 22,
  alert: alert
}

myObj.alert() // 22 years old
```

En termes simples, lorsque vous appelez une fonction en utilisant la notation par points, `this` est implicitement lié à l'objet à partir duquel la fonction est appelée.

Dans cet exemple, puisque `alert` est appelée à partir de `myObj`, le mot-clé `this` est lié à `myObj`. Donc lorsque `alert` est appelée avec `myObj.alert()`, `this.age` est 22, ce qui est la propriété `age` de `myObj`.

Regardons un autre exemple :

```js
function alert() { 
  console.log(this.age + ' years old'); 
}

const myObj = {
  age: 22,
  alert: alert,
  nestedObj: {
    age: 26,
    alert: alert
  }
}

myObj.nestedObj.alert(); // 26 years old
```

Ici, parce que `alert` est finalement appelée à partir de `nestedObj`, `this` est implicitement lié à `nestedObj` au lieu de `myObj`.

Un moyen facile de déterminer à quel objet `this` est implicitement lié est de regarder quel objet se trouve à gauche du point (`.`) :

```js
function alert() { 
  console.log(this.age + ' years old'); 
}

const myObj = {
  age: 22,
  alert: alert,
  nestedObj: {
    age: 26,
    alert: alert
  }
}

myObj.alert(); // `this` est lié à `myObj` -- 22 years old
myObj.nestedObj.alert(); // `this` est lié à `nestedObj` -- 26 years old
```

### Liaison explicite en JavaScript

Nous avons vu que la liaison implicite avait à voir avec le fait d'avoir une référence dans cet objet.

Mais que faire si nous voulons **forcer** une fonction à utiliser un objet comme son contexte sans mettre une référence de fonction de propriété sur l'objet ?

Nous avons deux méthodes utilitaires pour y parvenir : `call()` et `apply()`.

Avec quelques autres ensembles de fonctions utilitaires, ces deux utilitaires sont disponibles pour toutes les fonctions en JavaScript via le mécanisme \[\[Prototype\]\].

Pour lier explicitement un appel de fonction à un contexte, vous devez simplement invoquer `call()` sur cette fonction et passer l'objet de contexte en tant que paramètre :

```js
function alert() { 
  console.log(this.age + ' years old'); 
}

const myObj = {
  age: 22
}

alert.call(myObj); // 22 years old
```

Maintenant, voici la partie amusante. Même si vous deviez passer cette fonction plusieurs fois à de nouvelles variables (currying), chaque invocation utilisera le même contexte car il a été verrouillé (lié explicitement) à cet objet. Cela s'appelle **hard binding**.

```js
function alert() { 
  console.log(this.age); 
} 

const myObj = { 
  age: 22 
}; 

const bar = function() { 
  alert.call(myObj); 
}; 

bar(); // 22
setTimeout(bar, 100); // 22 
// une fonction `bar` liée de manière rigide ne peut plus avoir son contexte `this` outrepassé 
bar.call(window); // toujours 22
```

La liaison rigide est un moyen parfait de verrouiller un contexte dans un appel de fonction et de transformer véritablement cette fonction en une méthode.

### Liaison d'appel de constructeur en JavaScript

La dernière et peut-être la plus intéressante des liaisons est la nouvelle liaison qui accentue également le comportement inhabituel de JavaScript par rapport à d'autres langages basés sur les classes.

Lorsque une fonction est invoquée avec le mot-clé `new` devant elle, également connu sous le nom d'**appel de constructeur**, les choses suivantes se produisent :

1. Un tout nouvel objet est créé (ou construit)

2. Le nouvel objet construit est lié par \[\[Prototype\]\] à la fonction qui l'a construit

3. Le nouvel objet construit est défini comme la liaison `this` pour cet appel de fonction.

Regardons cela en code pour mieux comprendre :

```js
function giveAge(age) { 
  this.age = age; 
} 

const bar = new giveAge(22); 
console.log(bar.age); // 22
```

En appelant `giveAge(...)` avec `new` devant, nous avons construit un nouvel objet et défini cet nouvel objet comme `this` pour l'appel de `foo(...)`. Donc `new` est la dernière façon dont vous pouvez lier le `this` d'un appel de fonction.

## Conclusion

En résumé,

* Le mot-clé `this`, lorsqu'il est utilisé dans une fonction, lie cette fonction à un objet de contexte

* Il existe quatre types de liaisons : *liaison par défaut, liaison implicite, liaison explicite et liaison d'appel de constructeur* (*new*)

* Connaître ces quatre règles vous aidera à discerner facilement le contexte pour une référence `this`.

![Une image expliquant le mot-clé 'this'](https://www.freecodecamp.org/news/content/images/2021/06/12.png align="left")

*Une image expliquant le mot-clé 'this'*

![Une image expliquant le mot-clé 'this'](https://www.freecodecamp.org/news/content/images/2021/06/13.png align="left")

*Une image expliquant le mot-clé 'this'*

Si vous avez aimé ou bénéficié de cet article et que vous souhaitez me soutenir, vous pouvez m'offrir un café [ici](https://buymeacoffee.com/ubahthebuilder).

Vous pouvez également me rejoindre sur [Twitter](https://twitter.com/UbahTheBuilder). N'oubliez pas de consulter mon [blog](https://ubahthebuilder.tech) pour plus de contenu lié à JavaScript et à la programmation.

Merci et à bientôt.