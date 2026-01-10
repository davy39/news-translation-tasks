---
title: Qu'est-ce que l'héritage prototypal en JavaScript ? Explications avec des exemples
  de code
subtitle: ''
author: Austin Asoluka
co_authors: []
series: null
date: '2024-05-31T08:10:16.000Z'
originalURL: https://freecodecamp.org/news/javascript-prototypal-inheritance
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-05-29-at-00.19.30.png
tags:
- name: inheritance
  slug: inheritance
- name: JavaScript
  slug: javascript
seo_title: Qu'est-ce que l'héritage prototypal en JavaScript ? Explications avec des
  exemples de code
seo_desc: "Prototypal inheritance can feel like a complex concept shrouded in technical\
  \ jargon. But fear not! This guide will break it down using clear, relatable examples\
  \ that go beyond the typical textbook explanations. \nWe'll ditch the confusing\
  \ terms and fo..."
---

L'héritage prototypal peut sembler être un concept complexe enveloppé dans un jargon technique. Mais ne craignez rien ! Ce guide va le décortiquer en utilisant des exemples clairs et concrets qui vont au-delà des explications typiques des manuels scolaires.

Nous allons laisser de côté les termes déroutants pour nous concentrer sur des scénarios du monde réel que vous pourrez facilement comprendre.

À la fin de cet article, vous serez un pro de l'héritage prototypal, réalisant que ce n'était pas si difficile après tout !

## Table des matières

* [Introduction au concept](#heading-introduction-au-concept)
* [Que sont les objets JavaScript ?](#heading-que-sont-les-objets-javascript)
* [Qu'est-ce qu'un prototype d'objet ?](#heading-quest-ce-quun-prototype-dobjet)
* [Comment travailler avec l'objet .prototype d'un constructeur](#heading-comment-travailler-avec-lobjet-prototype-dun-constructeur)
* [Comment modifier le prototype d'un constructeur](#heading-comment-modifier-le-prototype-dun-constructeur)
* [La propriété __proto__](#heading-la-propriete-proto)
* [Résumé](#heading-resume)

## Introduction au concept

Imaginez que je suis un parent et que j'ai un enfant et un petit-enfant. Si vous deviez représenter mon arbre généalogique dans un diagramme, il ressemblerait à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-09-at-23.12.29.png)
_**Fig 1** : Représentation de la structure d'héritage avec une famille_

Vous pouvez voir que le `grandparent` (grand-parent) est au sommet de cet arbre généalogique, tandis que le `parent` est un descendant direct du `grandparent`, et le `child` (enfant) est un descendant du `parent`.

Si vous essayez de remonter le chemin, vous verrez que le `grandchild` (petit-enfant) est l'enfant du `parent` et que son propre parent est un `child` du `grandparent`.

## Que sont les objets JavaScript ?

Vous avez peut-être déjà rencontré cette affirmation : "En JavaScript, presque tout est un Objet".

Remarquez comment j'ai écrit `Object` ? Lorsque j'utiliserai Object (avec une majuscule) et objet tout au long de cet article, ils signifieront des choses différentes.

Object est un constructeur utilisé pour créer des objets. C'est-à-dire : l'un est le parent/ancêtre et l'autre est l'enfant.

En utilisant l'illustration de la **Fig 1** ci-dessus, essayons de démontrer comment l'arbre généalogique fonctionne en JavaScript.

`Object` est le grand-parent.

Les constructeurs comme `Array`, `String`, `Number`, `Function` et `Boolean` sont tous des descendants d' `Object`.

Ils produisent tous une progéniture de types différents : `array`, `string`, `number`, `function` et `boolean`. Cependant, si vous remontez à leur origine, ce sont tous des `Objects`.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-10-at-00.08.57.png)
_**Fig 2** : Object est au sommet de l'arbre d'héritage en JavaScript_

Ainsi, si l'on vous demande pourquoi tout (sauf `null` et `undefined`) est considéré comme un objet en JavaScript, c'est parce qu'ils sont tous des descendants du constructeur `Object`.

Les constructeurs listés dans l'image ci-dessus sont responsables des différents types de données que vous utilisez en JavaScript. C'est-à-dire qu'ils sont utilisés en coulisses pour créer les types de données familiers (et vous pouvez également les utiliser pour créer explicitement des valeurs de différents types).

Essayons quelques extraits de code.

### Comment créer un objet

```js
// En utilisant la syntaxe d'objet classique
const newObj = {}

// En utilisant le constructeur Object
const newObjWithConstructor = new Object()
```

### Comment créer un tableau (array)

```js
// En utilisant la syntaxe de tableau classique
const newArr = []

// En utilisant le constructeur Array
const newArrWithConstructor = new Array()
```

### Comment créer un nombre

```js
// En utilisant la syntaxe classique
const num = 3

// En utilisant le constructeur Number
const numWithConstructor = new Number(3)
```

### Comment créer une fonction

```js
// En utilisant la syntaxe de fonction classique
function logArg (arg) {
	console.log(arg)
}

// En utilisant le constructeur Function
const logArgWithConstructor = new Function('arg1', 'console.log(arg1)')
```

### Comment créer un booléen

```js
// En utilisant la syntaxe de booléen classique
const isValid = true

// En utilisant le constructeur Boolean
const isValidWithConstructor = new Boolean(true)
```

Vous pouvez voir, d'après les exemples ci-dessus, qu'il est possible de créer explicitement des valeurs en utilisant le constructeur approprié, ou simplement en utilisant la syntaxe simple et en laissant JavaScript créer la valeur avec le type approprié pour nous.

**Note** : Il est important de préciser que chaque méthode de création de valeurs possède ses propres cas d'utilisation et effets secondaires, mais nous n'aborderons pas cela dans cet article.

Les constructeurs de ces différentes valeurs ont quelque chose appelé un prototype.

## Qu'est-ce qu'un prototype d'objet ?

En JavaScript, il existe quelque chose appelé `prototype`. Le concept le plus proche est l'ADN humain.

Tout comme l'ADN agit comme un plan définissant les caractéristiques transmises de génération en génération dans l'arbre généalogique humain, les `prototypes` en JavaScript sont utilisés pour définir les propriétés et les méthodes qui sont héritées par les objets dans l'arbre des objets JavaScript.

Combinons les **Fig 1** et **Fig 2** ci-dessus, en les mettant à jour pour intégrer le concept d'ADN et de prototype.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-10-at-01.01.47.png)
_Fig 3 : Comparaison de l'héritage JavaScript avec le concept d'héritage chez les humains_

En JavaScript, tous les constructeurs ont un prototype. Le prototype d'un constructeur est un dictionnaire de tout ce que les valeurs créées avec le constructeur doivent hériter.

Relisez la ligne ci-dessus ☝️ et continuez quand c'est clair.

Considérez le constructeur comme un parent et le prototype comme l'ADN. Lorsque le constructeur (parent) crée (donne naissance à) une progéniture (valeur), la progéniture hérite de l'ADN (prototype) de son parent le constructeur.

Considérons un autre diagramme :

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-10-at-01.28.05.png)
_Fig 4 : Représentation schématique de l'héritage de l'ADN chez l'humain_

À partir de la **Fig 4**, vous pouvez voir qu'un enfant hérite directement de ses parents et que ses parents héritent des traits du grand-parent. Dans cette chaîne d'héritage, l'enfant hérite en fait à la fois du grand-parent et du parent.

En fait, les traits de caractère de l'enfant sont fortement influencés par la combinaison de l'ADN de chaque ancêtre avant lui.

C'est ainsi que fonctionne l'héritage prototypal en JavaScript.

Les propriétés dans le prototype d'un constructeur sont héritées par les enfants créés par ce constructeur. Cela continue le long de la chaîne. Vous pouvez le raisonner ainsi :

Chaque descendant dans la chaîne d'héritage hérite de tout ce qui est disponible dans le prototype de ses ancêtres.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-10-at-02.07.22.png)
_Fig 5 : Chaîne d'héritage prototypal_

D'après le diagramme ci-dessus, vous pouvez voir que tous les autres prototypes héritent du prototype d'Object. Par conséquent, toute valeur créée avec le constructeur Array (par exemple) héritera du prototype d'Array, et également du prototype d'Object.

C'est ainsi car le prototype d'Array hérite du prototype d'Object.

Le terme prototype d'Array s'écrit `Array.prototype` en JavaScript, tandis que le prototype d'Object est `Object.prototype`.

**Note** : Il est important de noter que le concept d'ADN est complexe ; si on poussait l'analogie trop loin, on découvrirait vite des nuances et des différences entre le fonctionnement de l'ADN et celui des prototypes, mais à haut niveau, ils sont très similaires.

Par conséquent, une compréhension de l'héritage dans l'arbre généalogique humain nous donnera une solide compréhension de l'héritage prototypal en JavaScript.

Si vous apprenez mieux avec des vidéos, [regardez celle-ci](https://www.youtube.com/watch?v=TzqJPmEkZ0o) avant de continuer.

## Comment travailler avec `.prototype` d'un constructeur

![Image](https://www.freecodecamp.org/news/content/images/2024/05/Screenshot-2024-05-10-at-02.16.07.png)

Pour voir le contenu du prototype d'un constructeur, nous écrivons simplement `nomDuConstructeur.prototype`. Par exemple : `Array.prototype`, `Object.prototype`, `String.prototype` et ainsi de suite.

Vous êtes-vous déjà demandé comment il est possible d'écrire `[2, 8, 10].map(...)` ? C'est parce que, dans le prototype du constructeur Array, il y a une clé appelée `map`. Ainsi, même si vous n'avez pas créé la propriété `map` vous-même, elle a été héritée par la valeur de type tableau parce que cette valeur a été créée par le constructeur `Array` en interne.

Lisez l'affirmation ci-dessus ainsi : vous êtes-vous déjà demandé pourquoi vous avez votre groupe sanguin spécifique ? C'est parce que vous tenez votre groupe sanguin des gènes hérités de vos parents !

Ainsi, la prochaine fois que vous utiliserez des propriétés et des méthodes comme `.length`, `.map`, `.reduce`, `.valueOf`, `.find`, `.hasOwnProperty` sur une valeur, rappelez-vous simplement qu'elles sont toutes héritées du prototype du constructeur ou d'un prototype plus haut dans la chaîne de prototypes (l'ascendance).

Vous pouvez voir le prototype du constructeur comme le prototype de l'entité utilisée pour construire/créer/fabriquer une valeur.

Sachez que le `.prototype` de chaque constructeur est un objet. Le constructeur lui-même est une fonction, mais son prototype est un objet.

```js
console.log(typeof Array) // function
console.log(typeof Array.prototype) // object
```

**Note** : Une exception à cela est le prototype du constructeur Function. C'est un objet fonction, mais il possède toujours des propriétés qui lui sont attachées et ces propriétés sont accessibles comme nous le ferions avec des objets ordinaires (en utilisant la notation par points `.`).

Si vous vous souvenez bien, nous pouvons ajouter de nouvelles propriétés et récupérer les valeurs des propriétés déjà existantes des objets en utilisant la notation par points `.`. Par exemple : `nomObjet.nomPropriete`

```js
const user = {
	name: "asoluka_tee",
    stack: ["Python", "JavaScript", "Node.js", "React", "MongoDB"],
    twitter_url: "https://twitter.com/asoluka_tee"
}

// En utilisant la syntaxe nomObjet.nomPropriete, pour accéder à la clé name nous écrirons ; user.name 
const userName = user.name;
console.log(userName) // asoluka_tee

// Pour ajouter une nouvelle propriété à l'objet nous écrirons ;
user.eyeColor = "black"

// Si nous affichons l'objet user dans la console maintenant, nous devrions voir eyeColor comme faisant partie des propriétés de l'objet avec la valeur 'black'
```

Avez-vous déjà entendu parler de mutation d'ADN ? C'est l'idée de modifier l'ADN d'une personne. En JavaScript, c'est possible avec les prototypes.

Tout comme la mutation de l'ADN est une chose extrêmement dangereuse à tenter et que le résultat pourrait être incertain ou causer des effets secondaires indésirables, modifier le prototype d'un constructeur n'est pas une bonne idée, à moins que vous ne sachiez exactement ce que vous faites.

## Comment modifier le prototype d'un constructeur

En JavaScript, il est possible de modifier l'objet prototype d'un constructeur de la même manière que vous le feriez avec un objet JavaScript ordinaire (comme montré ci-dessus).

Cette fois, il suffit de suivre cette syntaxe : `nomConstructeur.prototype.nomNouvellePropriete = valeur`. Par exemple, si vous voulez ajouter une nouvelle propriété nommée `currentDate` à l'objet prototype du constructeur Array, vous écririez :

```js
//nomConstructeur.prototype.nomNouvellePropriete
Array.prototype.currentDate = new Date().toDateString();
```

Désormais, dans votre code, puisque `currentDate` existe maintenant dans le prototype du constructeur `Array` (`Array.prototype`), chaque tableau créé dans notre programme peut y accéder ainsi : `[1, 2, 3].currentDate` et le résultat sera la date du jour.

Si vous voulez que chaque objet de votre programme JavaScript ait accès à `currentDate`, vous devez l'ajouter à l'objet prototype du constructeur `Object` (`Object.prototype`) à la place :

```js
//nomConstructeur.prototype.nomNouvellePropriete
Object.prototype.currentDate = new Date().toDateString();

const newArr = [1, 2, 3]
const newObj = {}
const newBool = true

// NB : La date affichée est la date de rédaction de cet article
console.log(newArr.currentDate) // 'Fri May 10 2024'
console.log(newObj.currentDate) // 'Fri May 10 2024'
console.log(newBool.currentDate) // 'Fri May 10 2024'
```

C'est possible parce que l'objet prototype de tous les constructeurs hérite de l'objet prototype du constructeur `Object`.

Écrivons notre propre version de deux méthodes de tableau populaires et utilisons-les comme nous utiliserions les originales.

1. **Array.prototype.reduce** : Nous appellerons la nôtre `.reduceV2`

```js
// Ajouter notre nouvelle fonction à l'objet prototype du constructeur Array
Array.prototype.reduceV2 = function (reducer, initialValue) {
  let accum = initialValue;
  for (let i = 0; i < this.length; i++) {
    accum = reducer(accum, this[i]);
  }
  return accum;
};

// Créer un tableau de scores
let scores = [10, 20, 30, 40, 50];

// Utiliser notre propre version de Array.prototype.reduce pour additionner les valeurs du tableau
const result = scores.reduceV2(function reducer(accum, curr) {
  return accum + curr;
}, 0);

// Afficher le résultat dans la console
console.log(result);
```

L'objectif ici n'est pas d'expliquer toute la syntaxe, mais de vous montrer qu'en tirant parti de la chaîne de prototypes, vous pouvez créer vos propres méthodes et les utiliser exactement comme celles fournies par JavaScript.

Notez que vous pourriez simplement remplacer notre `.reduceV2` par l'original `.reduce` et cela fonctionnerait toujours (les cas particuliers ne sont pas gérés ici).

2. **Array.prototype.map** : Nous appellerons la nôtre `.mapV2` 

```js
// Ajouter la méthode mapV2 à l'objet prototype du constructeur Array
Array.prototype.mapV2 = function (func) {
  let newArray = [];
  this.forEach((item, index) => newArray.push(func(item, index)));
  return newArray;
};

// Créer un tableau de scores 
const scores = [1, 2, 3, 4, 5];

// Utiliser notre méthode mapV2 pour incrémenter chaque élément du tableau scores de 2
const scoresTimesTwo = scores.mapV2(function (curr, index) {
	return curr * 2;
})

// Afficher la valeur de scoresTimesTwo dans la console.
console.log(scoresTimesTwo)
```

**Note** : Il est important de préciser qu'il ne s'agit nullement d'une implémentation parfaite de la version originale de la méthode `map` de JavaScript. C'est juste une tentative de vous montrer ce qui est possible avec l'objet prototype d'un constructeur.

Avant de terminer cette leçon, il y a une dernière chose que je dois mentionner : la propriété `__proto__` de chaque objet.

## La propriété __proto__

`__proto__` est un accesseur (setter et getter) pour la propriété interne [[prototype]] d'un objet. Cela signifie qu'elle est utilisée pour définir ou obtenir le prototype d'un objet (par exemple, l'objet dont hérite un autre objet).

Considérez cet extrait de code ;

```js
const user = {}
const scores = []

user.prototype // undefined
scores.prototype // undefined
```

Dans l'extrait ci-dessus, nous avons essayé d'accéder à l'objet prototype directement depuis les valeurs. Ce n'est pas possible en JavaScript.

C'est logique puisque seuls les constructeurs ont la propriété `prototype` qui leur est attachée.

Tout comme la mutation de l'ADN est risquée, il peut être chaotique de modifier l'objet prototype si vous ne savez pas absolument ce que vous faites.

Dans des circonstances normales, un enfant ne devrait pas essayer de modifier l'ADN de son ancêtre ou même déterminer de qui il doit hériter ses traits 😉

Le langage JavaScript nous offre cependant un moyen d'accéder à l'objet prototype à partir de valeurs qui ne sont pas des constructeurs en utilisant la propriété `__proto__`.

C'est une méthode obsolète (dépréciée) et elle ne devrait pas être utilisée pour de nouveaux projets. Je mentionne `__proto__` car vous pourriez être amené à travailler sur une base de code qui l'utilise encore.

`__proto__` permet à une valeur d'accéder directement à l'objet prototype de son constructeur. Donc si pour une raison quelconque vous souhaitez voir ce qui est disponible dans la chaîne de prototypes de l'ancêtre immédiat d'une valeur, la propriété `__proto__` peut être utilisée à cet effet.

Vous pouvez également utiliser `__proto__` pour déterminer de quel objet une valeur doit hériter.

Par exemple, nous avons un objet appelé `human`, et nous voulons qu'un autre objet appelé `parent` hérite de `human` ; cela peut être fait avec la propriété `__proto__` de `parent` comme ceci :

```js
// Créer un objet human
const human = {
    walk: function () { console.log('walking') },
    talk: function () { console.log('talking') },
	sleep: function () { console.log('sleeping') }
}

// Créer un objet parent et le configurer pour hériter de human.
const parent = {
    __proto__: human
}

// Utiliser une méthode de l'ancêtre de parent
parent.sleep() // sleeping
```

Remarquez comment nous pouvons appeler la méthode `sleep` sur `parent` parce que `parent` hérite maintenant de `human`.

Il existe des méthodes plus modernes recommandées pour interagir avec l'objet prototype comme `Object.getPrototypeOf` et `Object.setPrototypeOf`.

```js
const user = {}
const scores = []

// Obtenir le prototype de l'objet user
console.log(Object.getPrototypeOf(user))

// Changer le prototype du tableau scores. C'est comme changer d'ascendance et cela doit être fait avec beaucoup de précaution.
console.log(Object.setPrototypeOf(scores, {}))

// Vérifier le prototype de scores maintenant
console.log(Object.getPrototypeOf(scores)) // {}
```

Ces méthodes doivent être utilisées avec une grande prudence. En fait, vous devriez en apprendre davantage à leur sujet dans la documentation MDN JS pour obtenir plus d'informations sur leurs avantages et inconvénients.

Si vous avez lu jusqu'ici, vous connaissez maintenant les fondamentaux de `Array.prototype` et, à partir de maintenant, l'apprentissage de tout autre concept construit par-dessus cela en JavaScript sera plus facile à comprendre.

Résumons ce que vous avez appris jusqu'à présent.

## Résumé

Nous avons différents constructeurs en JavaScript : `Array`, `Boolean`, `Function`, `Number`, `String` et `Object`.

Object est le parent de tous les autres constructeurs.

Chaque constructeur possède un objet `.prototype` et cet objet contient des propriétés et des méthodes qui pourraient être consultées par les valeurs créées à l'aide du constructeur. Par exemple, une valeur créée à l'aide du constructeur `Array` aura accès à toutes les propriétés et méthodes disponibles dans l'objet `Array.prototype`, et cet héritage remonte jusqu'au sommet.

C'est-à-dire qu'une valeur créée à l'aide du constructeur `Array` (que ce soit implicitement ou explicitement), aura non seulement accès aux propriétés et méthodes de l'objet `Array.prototype`, mais aussi aux propriétés et méthodes de l'objet `Object.prototype`.

C'est dû au concept d'héritage prototypal. `Object` est le parent d' `Array` et chaque enfant produit par `Array` aura accès aux caractéristiques d' `Array` et d' `Object`.

C'est ce qui se passe lorsque vous essayez d'obtenir une propriété d'une valeur qui n'est pas explicitement déclarée sur cette valeur. Voir l'extrait de code ci-dessous :

```js
const user = {}

// tentative de récupération de la propriété .valueOf de l'objet user
console.log(user.valueOf)
```

Évidemment, l'objet `user` n'a pas de propriété `.valueOf`, il remonte donc sa chaîne de prototypes pour trouver un prototype qui possède cette propriété et si elle est trouvée, la valeur est renvoyée. Sinon, nous obtenons `undefined`.

Nous avons également appris que nous pouvons modifier le prototype de n'importe quel constructeur pour ajouter des fonctionnalités et que cela doit être fait avec prudence.

Enfin, nous avons appris comment `__proto__`, `getPrototypeOf` et `setPrototypeOf` peuvent être utilisés pour récupérer et définir le prototype d'une valeur.

### En quoi est-ce utile ?

Imaginez que vous vouliez créer une méthode qui crée un nouvel objet basé sur un tableau et le renvoie lorsqu'elle est appelée sur le tableau.

C'est à vous d'essayer par vous-même.

```js
// Array.prototype.toObject
const names = ['Austin', 'Tola', 'Joe', 'Victor'];

// Écrivez votre implémentation de toObject ici.

console.log(names.toObject()) // {0: 'Austin', 1: 'Tola', 2: 'Joe', 3: 'Victor'}
```

Hurray !!! Je sais que vous vous sentez déjà comme un ninja de JavaScript.

Si vous apprenez mieux avec des vidéos, abonnez-vous à ma chaîne [YouTube](https://www.youtube.com/@asoluka_tee), je publierai bientôt des vidéos de cours.

Merci de m'avoir lu ! Bon codage !