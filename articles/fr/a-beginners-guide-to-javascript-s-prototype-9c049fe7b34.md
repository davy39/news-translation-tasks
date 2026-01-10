---
title: Guide du débutant sur le Prototype de JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-04T12:58:56.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-javascript-s-prototype-9c049fe7b34
coverImage: https://cdn-media-1.freecodecamp.org/images/1*45wTCahuSKO_9Ne260qf5w.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: prototype
  slug: prototype
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Guide du débutant sur le Prototype de JavaScript
seo_desc: 'By Tyler McGinnis

  This is part of our Advanced JavaScript course. If you enjoy this post, check it
  out.

  You can’t get very far in JavaScript without dealing with objects. They’re foundational
  to almost every aspect of the JavaScript programming langu...'
---

Par Tyler McGinnis

***Ceci fait partie de notre*** [***cours JavaScript Avancé***](https://tylermcginnis.com/courses/advanced-javascript/) ***. Si vous aimez cet article, consultez-le.***

Vous ne pouvez pas aller très loin en JavaScript sans traiter avec les objets. Ils sont fondamentaux pour presque tous les aspects du langage de programmation JavaScript. En fait, apprendre à créer des objets est probablement l'une des premières choses que vous avez étudiées lorsque vous avez commencé.

Cela dit, afin d'apprendre le plus efficacement possible les prototypes en JavaScript, nous allons faire appel à notre développeur Jr intérieur et revenir aux bases.

Si vous préférez regarder la vidéo plutôt que de lire cet article, vous pouvez le faire ici.

Les objets sont des paires clé/valeur. La manière la plus courante de créer un objet est avec des accolades `{}` et vous ajoutez des propriétés et des méthodes à un objet en utilisant la notation par points.

```javascript
let animal = {}
animal.name = 'Leo'
animal.energy = 10
animal.eat = function (amount) {
  console.log(`${this.name} est en train de manger.`)
  this.energy += amount
}
animal.sleep = function (length) {
  console.log(`${this.name} est en train de dormir.`)
  this.energy += length
}
animal.play = function (length) {
  console.log(`${this.name} est en train de jouer.`)
  this.energy -= length
}
```

Simple. Maintenant, il est probable que dans notre application, nous devrons créer plus d'un animal. Naturellement, l'étape suivante serait d'encapsuler cette logique à l'intérieur d'une fonction que nous pouvons invoquer chaque fois que nous avons besoin de créer un nouvel animal. Nous appellerons ce modèle `Instantiation Fonctionnelle` et nous appellerons la fonction elle-même une fonction "constructeur", puisque c'est elle qui est responsable de la "construction" d'un nouvel objet.

## Instantiation Fonctionnelle

```javascript
function Animal (name, energy) {
  let animal = {}
  animal.name = name
  animal.energy = energy
  animal.eat = function (amount) {
    console.log(`${this.name} est en train de manger.`)
    this.energy += amount
  }
  animal.sleep = function (length) {
    console.log(`${this.name} est en train de dormir.`)
    this.energy += length
  }
  animal.play = function (length) {
    console.log(`${this.name} est en train de jouer.`)
    this.energy -= length
  }
  return animal
}
const leo = Animal('Leo', 7)
const snoop = Animal('Snoop', 10)
```

`"Je pensais que c'était un cours de JavaScript Avancé...?" - Votre cerveau` **C'en est un. Nous y arriverons.**

Maintenant, chaque fois que nous voulons créer un nouvel animal (ou plus généralement parlant une nouvelle "instance"), tout ce que nous avons à faire est d'invoquer notre fonction `Animal`, en lui passant le `name` et le niveau d'`energy` de l'animal.

Cela fonctionne très bien et c'est incroyablement simple. Cependant, pouvez-vous repérer des faiblesses avec ce modèle ? La plus grande, et celle que nous allons tenter de résoudre, concerne les trois méthodes : `eat`, `sleep`, et `play`. Chacune de ces méthodes n'est pas seulement dynamique, mais elles sont aussi complètement génériques. Cela signifie qu'il n'y a aucune raison de recréer ces méthodes comme nous le faisons actuellement chaque fois que nous créons un nouvel animal. Nous gaspillons simplement de la mémoire et rendons chaque objet animal plus grand qu'il n'en a besoin.

Pouvez-vous penser à une solution ? Et si, au lieu de recréer ces méthodes chaque fois que nous créons un nouvel animal, nous les déplacions vers leur propre objet ? Ensuite, nous pouvons faire en sorte que chaque animal référence cet objet. Nous pouvons appeler ce modèle `Instantiation Fonctionnelle avec Méthodes Partagées`, un peu verbeux mais descriptif.

## Instantiation Fonctionnelle avec Méthodes Partagées

```javascript
const animalMethods = {
  eat(amount) {
    console.log(`${this.name} est en train de manger.`)
    this.energy += amount
  },
  sleep(length) {
    console.log(`${this.name} est en train de dormir.`)
    this.energy += length
  },
  play(length) {
    console.log(`${this.name} est en train de jouer.`)
    this.energy -= length
  }
}
function Animal (name, energy) {
  let animal = {}
  animal.name = name
  animal.energy = energy
  animal.eat = animalMethods.eat
  animal.sleep = animalMethods.sleep
  animal.play = animalMethods.play
  return animal
}
const leo = Animal('Leo', 7)
const snoop = Animal('Snoop', 10)
```

En déplaçant les méthodes partagées vers leur propre objet et en référençant cet objet à l'intérieur de notre fonction `Animal`, nous avons maintenant résolu le problème de gaspillage de mémoire et d'objets animaux trop volumineux.

## Object.create

Améliorons une fois de plus notre exemple en utilisant `Object.create`. Simplement dit, **Object.create vous permet de créer un objet qui déléguera à un autre objet en cas d'échec de recherche**.

Autrement dit, Object.create vous permet de créer un objet, et chaque fois qu'il y a un échec de recherche de propriété sur cet objet, il peut consulter un autre objet pour voir si cet autre objet a la propriété. Cela fait beaucoup de mots. Regardons un peu de code.

```javascript
const parent = {
  name: 'Stacey',
  age: 35,
  heritage: 'Irish'
}
const child = Object.create(parent)
child.name = 'Ryan'
child.age = 7
console.log(child.name) // Ryan
console.log(child.age) // 7
console.log(child.heritage) // Irish
```

Donc dans l'exemple ci-dessus, parce que `child` a été créé avec `Object.create(parent)`, chaque fois qu'il y a un échec de recherche de propriété sur `child`, JavaScript déléguera cette recherche à l'objet `parent`. Cela signifie que même si `child` n'a pas de propriété `heritage`, `parent` en a une, donc lorsque vous loggez `child.heritage`, vous obtiendrez le `heritage` du `parent` qui était `Irish`.

Maintenant que nous avons `Object.create` dans notre boîte à outils, comment pouvons-nous l'utiliser pour simplifier notre code `Animal` précédent ? Eh bien, au lieu d'ajouter toutes les méthodes partagées à l'animal une par une comme nous le faisons maintenant, nous pouvons utiliser Object.create pour déléguer à l'objet `animalMethods` à la place. Pour avoir l'air vraiment intelligent, appelons cela `Instantiation Fonctionnelle avec Méthodes Partagées et Object.create` ?

## Instantiation Fonctionnelle avec Méthodes Partagées et Object.create

```javascript
const animalMethods = {
  eat(amount) {
    console.log(`${this.name} est en train de manger.`)
    this.energy += amount
  },
  sleep(length) {
    console.log(`${this.name} est en train de dormir.`)
    this.energy += length
  },
  play(length) {
    console.log(`${this.name} est en train de jouer.`)
    this.energy -= length
  }
}
function Animal (name, energy) {
  let animal = Object.create(animalMethods)
  animal.name = name
  animal.energy = energy
  return animal
}
const leo = Animal('Leo', 7)
const snoop = Animal('Snoop', 10)
leo.eat(10)
snoop.play(5)
```

Donc maintenant, lorsque nous appelons `leo.eat`, JavaScript cherchera la méthode `eat` sur l'objet `leo`. Cette recherche échouera, puis, à cause de Object.create, elle déléguera à l'objet `animalMethods` où elle trouvera `eat`.

Jusqu'à présent, tout va bien. Il y a encore quelques améliorations que nous pouvons apporter, cependant. Il semble un peu "bricolé" de devoir gérer un objet séparé (`animalMethods`) afin de partager des méthodes entre les instances. Cela semble être une fonctionnalité courante que vous voudriez voir implémentée dans le langage lui-même. Il s'avère que c'est le cas, et c'est la raison pour laquelle vous êtes ici - `prototype`.

Alors, qu'est-ce exactement que `prototype` en JavaScript ? Eh bien, simplement dit, chaque fonction en JavaScript a une propriété `prototype` qui référence un objet. Anticlimax, n'est-ce pas ? Testons cela par nous-mêmes.

```javascript
function doThing () {}
console.log(doThing.prototype) // {}
```

Et si, au lieu de créer un objet séparé pour gérer nos méthodes (comme nous le faisons avec `animalMethods`), nous placions simplement chacune de ces méthodes sur le prototype de la fonction `Animal` ? Ensuite, tout ce que nous aurions à faire, au lieu d'utiliser Object.create pour déléguer à `animalMethods`, serait de l'utiliser pour déléguer à `Animal.prototype`. Nous appellerons ce modèle `Instantiation Prototypale`.

## Instantiation Prototypale

```javascript
function Animal (name, energy) {
  let animal = Object.create(Animal.prototype)
  animal.name = name
  animal.energy = energy
  return animal
}
Animal.prototype.eat = function (amount) {
  console.log(`${this.name} est en train de manger.`)
  this.energy += amount
}
Animal.prototype.sleep = function (length) {
  console.log(`${this.name} est en train de dormir.`)
  this.energy += length
}
Animal.prototype.play = function (length) {
  console.log(`${this.name} est en train de jouer.`)
  this.energy -= length
}
const leo = Animal('Leo', 7)
const snoop = Animal('Snoop', 10)
leo.eat(10)
snoop.play(5)
```

👏👏👏 Espérons que vous venez d'avoir un grand moment "aha". Encore une fois, `prototype` est juste une propriété que chaque fonction en JavaScript possède et, comme nous l'avons vu ci-dessus, il nous permet de partager des méthodes entre toutes les instances d'une fonction. Toutes nos fonctionnalités sont toujours les mêmes, mais maintenant, au lieu de devoir gérer un objet séparé pour toutes les méthodes, nous pouvons simplement utiliser un autre objet qui est intégré à la fonction `Animal` elle-même, `Animal.prototype`.

À ce stade, nous savons trois choses :

1. Comment créer une fonction constructeur.

2. Comment ajouter des méthodes au prototype de la fonction constructeur.

3. Comment utiliser Object.create pour déléguer les recherches échouées au prototype de la fonction.

Ces trois tâches semblent assez fondamentales pour tout langage de programmation. JavaScript est-il vraiment si mauvais qu'il n'y a pas de moyen plus facile, "intégré", pour accomplir la même chose ? Comme vous pouvez probablement le deviner à ce stade, il y en a un, et c'est en utilisant le mot-clé `new`.

Ce qui est bien dans l'approche lente et méthodique que nous avons prise pour en arriver là, c'est que vous aurez maintenant une compréhension approfondie de ce que le mot-clé `new` en JavaScript fait sous le capot.

En regardant en arrière notre constructeur `Animal`, les deux parties les plus importantes étaient la création de l'objet et son retour. Sans créer l'objet avec `Object.create`, nous ne pourrions pas déléguer au prototype de la fonction en cas d'échec de recherche. Sans l'instruction `return`, nous ne récupérerions jamais l'objet créé.

```javascript
function Animal (name, energy) {
  let animal = Object.create(Animal.prototype)
  animal.name = name
  animal.energy = energy
  return animal
}
```

Voici ce qui est cool avec `new` : lorsque vous invoquez une fonction en utilisant le mot-clé `new`, ces deux lignes sont faites pour vous implicitement ("sous le capot") et l'objet qui est créé est appelé `this`.

En utilisant des commentaires pour montrer ce qui se passe sous le capot et en supposant que le constructeur `Animal` est appelé avec le mot-clé `new`, il peut être réécrit comme ceci.

```javascript
function Animal (name, energy) {
  // const this = Object.create(Animal.prototype)
  this.name = name
  this.energy = energy
  // return this
}
const leo = new Animal('Leo', 7)
const snoop = new Animal('Snoop', 10)
```

et sans les commentaires "sous le capot"

```javascript
function Animal (name, energy) {
  this.name = name
  this.energy = energy
}
Animal.prototype.eat = function (amount) {
  console.log(`${this.name} est en train de manger.`)
  this.energy += amount
}
Animal.prototype.sleep = function (length) {
  console.log(`${this.name} est en train de dormir.`)
  this.energy += length
}
Animal.prototype.play = function (length) {
  console.log(`${this.name} est en train de jouer.`)
  this.energy -= length
}
const leo = new Animal('Leo', 7)
const snoop = new Animal('Snoop', 10)
```

Encore une fois, cela fonctionne et l'objet `this` est créé pour nous parce que nous avons appelé la fonction constructeur avec le mot-clé `new`. Si vous oubliez `new` lorsque vous invoquez la fonction, cet objet `this` n'est jamais créé et il n'est pas non plus retourné implicitement. Nous pouvons voir le problème avec cela dans l'exemple ci-dessous.

```javascript
function Animal (name, energy) {
  this.name = name
  this.energy = energy
}
const leo = Animal('Leo', 7)
console.log(leo) // undefined
```

Le nom de ce modèle est `Instantiation Pseudoclassique`.

Si JavaScript n'est pas votre premier langage de programmation, vous commencez peut-être à vous impatienter.

> *"WTH ce gars vient de recréer une version plus mauvaise d'une Classe" — Vous*

Pour ceux qui ne sont pas familiers, une Classe vous permet de créer un plan pour un objet. Ensuite, chaque fois que vous créez une instance de cette Classe, vous obtenez un objet avec les propriétés et méthodes définies dans le plan.

Cela vous semble familier ? C'est essentiellement ce que nous avons fait avec notre fonction constructeur `Animal` ci-dessus. Cependant, au lieu d'utiliser le mot-clé `class`, nous avons simplement utilisé une vieille fonction JavaScript régulière pour recréer la même fonctionnalité. Certes, cela a pris un peu plus de travail ainsi qu'une certaine connaissance de ce qui se passe "sous le capot" de JavaScript, mais les résultats sont les mêmes.

Voici la bonne nouvelle. JavaScript n'est pas un langage mort. Il est constamment amélioré et enrichi par le [comité TC-39](https://tylermcginnis.com/videos/ecmascript/)[. Ce que cela signifie](https://tylermcginnis.com/videos/ecmascript/), c'est que même si la version initiale de JavaScript ne supportait pas les classes, il n'y a aucune raison qu'elles ne puissent pas être ajoutées à la spécification officielle.

En fait, c'est exactement ce que le comité TC-3[9 a fait](https://tylermcginnis.com/videos/ecmascript/). En 2015, EcmaScript (la spécification officielle de JavaScript) 6 a été publié avec le support des Classes et du mot-clé `class`. Voyons à quoi ressemblerait notre fonction constructeur `Animal` ci-dessus avec la nouvelle syntaxe de classe.

```javascript
class Animal {
  constructor(name, energy) {
    this.name = name
    this.energy = energy
  }
  eat(amount) {
    console.log(`${this.name} est en train de manger.`)
    this.energy += amount
  }
  sleep(length) {
    console.log(`${this.name} est en train de dormir.`)
    this.energy += length
  }
  play(length) {
    console.log(`${this.name} est en train de jouer.`)
    this.energy -= length
  }
}
const leo = new Animal('Leo', 7)
const snoop = new Animal('Snoop', 10)
```

Assez propre, n'est-ce pas ?

Donc, si c'est la nouvelle façon de créer des classes, pourquoi avons-nous passé autant de temps à passer en revue l'ancienne façon ? La raison en est que la nouvelle façon (avec le mot-clé `class`) est principalement juste du "sucre syntaxique" sur la façon existante que nous avons appelée le modèle pseudoclassique. Afin de *complètement* comprendre la syntaxe de commodité des classes ES6, vous devez d'abord comprendre le modèle pseudoclassique.

À ce stade, nous avons couvert les bases du prototype de JavaScript. Le reste de cet article sera dédié à la compréhension d'autres sujets "bons à savoir" liés à celui-ci. Dans un autre article, nous verrons comment nous pouvons prendre ces bases et les utiliser pour comprendre comment l'héritage fonctionne en JavaScript.

***Si vous avez aimé cet article, envisagez de consulter notre*** [***cours JavaScript Avancé***](https://tylermcginnis.com/courses/advanced-javascript/)[***.***](https://tylermcginnis.com/courses/advanced-javascript/)

## **Méthodes de Tableau**

Nous avons parlé en profondeur ci-dessus de la manière dont, si vous voulez partager des méthodes entre les instances d'une classe, vous devriez placer ces méthodes sur le prototype de la classe (ou de la fonction). Nous pouvons voir ce même modèle démontré si nous regardons la classe `Array`. Historiquement, vous avez probablement créé vos tableaux comme ceci :

```javascript
const friends = []
```

Il s'avère que ce n'est que du sucre syntaxique pour créer une nouvelle instance de la classe `Array`.

```javascript
const friendsWithSugar = []
const friendsWithoutSugar = new Array()
```

Une chose à laquelle vous n'avez peut-être jamais pensé est comment chaque instance d'un tableau a toutes ces méthodes intégrées (`splice`, `slice`, `pop`, etc) ?

Eh bien, comme vous le savez maintenant, c'est parce que ces méthodes vivent sur `Array.prototype`. Et lorsque vous créez une nouvelle instance de `Array`, vous utilisez le mot-clé `new` qui met en place cette délégation à `Array.prototype` en cas d'échec de recherche.

Nous pouvons voir toutes les méthodes du tableau en loggant simplement `Array.prototype`.

```javascript
console.log(Array.prototype)
/*
  concat: 2n concat()
  constructor: 2n Array()
  copyWithin: 2n copyWithin()
  entries: 2n entries()
  every: 2n every()
  fill: 2n fill()
  filter: 2n filter()
  find: 2n find()
  findIndex: 2n findIndex()
  forEach: 2n forEach()
  includes: 2n includes()
  indexOf: 2n indexOf()
  join: 2n join()
  keys: 2n keys()
  lastIndexOf: 2n lastIndexOf()
  length: 0n
  map: 2n map()
  pop: 2n pop()
  push: 2n push()
  reduce: 2n reduce()
  reduceRight: 2n reduceRight()
  reverse: 2n reverse()
  shift: 2n shift()
  slice: 2n slice()
  some: 2n some()
  sort: 2n sort()
  splice: 2n splice()
  toLocaleString: 2n toLocaleString()
  toString: 2n toString()
  unshift: 2n unshift()
  values: 2n values()
*/
```

La même logique existe également pour les Objets. Tous les objets délégueront à `Object.prototype` en cas d'échec de recherche, ce qui explique pourquoi tous les objets ont des méthodes comme `toString` et `hasOwnProperty`.

## **Méthodes Statiques**

Jusqu'à présent, nous avons couvert le pourquoi et le comment du partage de méthodes entre les instances d'une Classe. Cependant, que faire si nous avions une méthode importante pour la Classe, mais qui n'avait pas besoin d'être partagée entre les instances ? Par exemple, que faire si nous avions une fonction qui prenait un tableau d'instances `Animal` et déterminait laquelle devait être nourrie ensuite ? Nous l'appellerons `nextToEat`.

```javascript
function nextToEat (animals) {
  const sortedByLeastEnergy = animals.sort((a,b) => {
    return a.energy - b.energy
  })
  return sortedByLeastEnergy[0].name
}
```

Il n'a pas de sens que `nextToEat` vive sur `Animal.prototype`, puisque nous ne voulons pas le partager entre toutes les instances. Au lieu de cela, nous pouvons le considérer comme une méthode d'assistance.

Donc, si `nextToEat` ne doit pas vivre sur `Animal.prototype`, où devons-nous le mettre ? Eh bien, la réponse évidente est que nous pourrions simplement placer `nextToEat` dans la même portée que notre classe `Animal`, puis le référencer lorsque nous en avons besoin, comme nous le ferions normalement.

```javascript
class Animal {
  constructor(name, energy) {
    this.name = name
    this.energy = energy
  }
  eat(amount) {
    console.log(`${this.name} est en train de manger.`)
    this.energy += amount
  }
  sleep(length) {
    console.log(`${this.name} est en train de dormir.`)
    this.energy += length
  }
  play(length) {
    console.log(`${this.name} est en train de jouer.`)
    this.energy -= length
  }
}
function nextToEat (animals) {
  const sortedByLeastEnergy = animals.sort((a,b) => {
    return a.energy - b.energy
  })
  return sortedByLeastEnergy[0].name
}
const leo = new Animal('Leo', 7)
const snoop = new Animal('Snoop', 10)
console.log(nextToEat([leo, snoop])) // Leo
```

Cela fonctionne, mais il y a une meilleure façon.

> *Chaque fois que vous avez une méthode qui est spécifique à une classe elle-même, mais qui n'a pas besoin d'être partagée entre les instances de cette classe, vous pouvez l'ajouter en tant que propriété* `static` *de la classe.*

```javascript
class Animal {
  constructor(name, energy) {
    this.name = name
    this.energy = energy
  }
  eat(amount) {
    console.log(`${this.name} est en train de manger.`)
    this.energy += amount
  }
  sleep(length) {
    console.log(`${this.name} est en train de dormir.`)
    this.energy += length
  }
  play(length) {
    console.log(`${this.name} est en train de jouer.`)
    this.energy -= length
  }
  static nextToEat(animals) {
    const sortedByLeastEnergy = animals.sort((a,b) => {
      return a.energy - b.energy
    })
    return sortedByLeastEnergy[0].name
  }
}
```

Maintenant, parce que nous avons ajouté `nextToEat` en tant que propriété `static` sur la classe, il vit sur la classe `Animal` elle-même (et non sur son prototype) et peut être accessible en utilisant `Animal.nextToEat`.

```javascript
const leo = new Animal('Leo', 7)
const snoop = new Animal('Snoop', 10)
console.log(Animal.nextToEat([leo, snoop])) // Leo
```

Parce que nous avons suivi un modèle similaire tout au long de cet article, voyons comment nous pourrions accomplir la même chose en utilisant ES5. Dans l'exemple ci-dessus, nous avons vu comment l'utilisation du mot-clé `static` placerait la méthode directement sur la classe elle-même. Avec ES5, ce même modèle est aussi simple que d'ajouter manuellement la méthode à l'objet fonction.

```javascript
function Animal (name, energy) {
  this.name = name
  this.energy = energy
}
Animal.prototype.eat = function (amount) {
  console.log(`${this.name} est en train de manger.`)
  this.energy += amount
}
Animal.prototype.sleep = function (length) {
  console.log(`${this.name} est en train de dormir.`)
  this.energy += length
}
Animal.prototype.play = function (length) {
  console.log(`${this.name} est en train de jouer.`)
  this.energy -= length
}
Animal.nextToEat = function (nextToEat) {
  const sortedByLeastEnergy = animals.sort((a,b) => {
    return a.energy - b.energy
  })
  return sortedByLeastEnergy[0].name
}
const leo = new Animal('Leo', 7)
const snoop = new Animal('Snoop', 10)
console.log(Animal.nextToEat([leo, snoop])) // Leo
```

## **Obtenir le prototype d'un objet**

Quelle que soit la méthode que vous avez utilisée pour créer un objet, obtenir le prototype de cet objet peut être accompli en utilisant la méthode `Object.getPrototypeOf`.

```javascript
function Animal (name, energy) {
  this.name = name
  this.energy = energy
}
Animal.prototype.eat = function (amount) {
  console.log(`${this.name} est en train de manger.`)
  this.energy += amount
}
Animal.prototype.sleep = function (length) {
  console.log(`${this.name} est en train de dormir.`)
  this.energy += length
}
Animal.prototype.play = function (length) {
  console.log(`${this.name} est en train de jouer.`)
  this.energy -= length
}
const leo = new Animal('Leo', 7)
const prototype = Object.getPrototypeOf(leo)
console.log(prototype)
// {constructor: 2, eat: 2, sleep: 2, play: 2}
prototype === Animal.prototype // true
```

Il y a deux points importants à retenir du code ci-dessus.

Premièrement, vous remarquerez que `proto` est un objet avec 4 méthodes : `constructor`, `eat`, `sleep`, et `play`. Cela a du sens. Nous avons utilisé `getPrototypeOf` en passant l'instance, `leo`, en obtenant le prototype de cette instance, qui est là où toutes nos méthodes résident.

Cela nous dit une autre chose sur `prototype` que nous n'avons pas encore abordée. Par défaut, l'objet `prototype` aura une propriété `constructor` qui pointe vers la fonction originale ou la classe à partir de laquelle l'instance a été créée. Ce que cela signifie également, c'est que parce que JavaScript place une propriété `constructor` sur le prototype par défaut, toute instance pourra accéder à son constructeur via `instance.constructor`.

Le deuxième point important à retenir ci-dessus est que `Object.getPrototypeOf(leo) === Animal.prototype`. Cela a également du sens. La fonction constructeur `Animal` a une propriété prototype où nous pouvons partager des méthodes entre toutes les instances, et `getPrototypeOf` nous permet de voir le prototype de l'instance elle-même.

```javascript
function Animal (name, energy) {
  this.name = name
  this.energy = energy
}
const leo = new Animal('Leo', 7)
console.log(leo.constructor) // Logs the constructor function
```

Pour relier ce dont nous avons parlé précédemment avec `Object.create`, cela fonctionne parce que toute instance de `Animal` va déléguer à `Animal.prototype` en cas d'échec de recherche. Donc lorsque vous essayez d'accéder à `leo.constructor`, `leo` n'a pas de propriété `constructor`, donc il déléguera cette recherche à `Animal.prototype` (qui a effectivement une propriété `constructor`). Si ce paragraphe n'a pas de sens, revenez en arrière et relisez la partie sur `Object.create` ci-dessus.

> *Vous avez peut-être vu* ***proto*** *utilisé auparavant pour obtenir le prototype d'une instance. C'est un vestige du passé. Au lieu de cela, utilisez* ***Object.getPrototypeOf(instance)*** *comme nous l'avons vu ci-dessus.*

## **Déterminer si une propriété vit sur le prototype**

Il existe certains cas où vous devez savoir si une propriété vit sur l'instance elle-même ou si elle vit sur le prototype auquel l'objet délègue. Nous pouvons voir cela en action en parcourant notre objet `leo` que nous avons créé. Supposons que l'objectif était de parcourir `leo` et de logger toutes ses clés et valeurs. En utilisant une boucle `for in`, cela ressemblerait probablement à ceci :

```javascript
function Animal (name, energy) {
  this.name = name
  this.energy = energy
}
Animal.prototype.eat = function (amount) {
  console.log(`${this.name} est en train de manger.`)
  this.energy += amount
}
Animal.prototype.sleep = function (length) {
  console.log(`${this.name} est en train de dormir.`)
  this.energy += length
}
Animal.prototype.play = function (length) {
  console.log(`${this.name} est en train de jouer.`)
  this.energy -= length
}
const leo = new Animal('Leo', 7)
for(let key in leo) {
  console.log(`Key: ${key}. Value: ${leo[key]}`)
}
```

À quoi vous attendriez-vous ? Très probablement, à quelque chose comme ceci :

```plaintext
Key: name. Value: Leo
Key: energy. Value: 7
```

Cependant, ce que vous avez vu si vous avez exécuté le code était ceci :

```javascript
Key: name. Value: Leo
Key: energy. Value: 7
Key: eat. Value: function (amount) {
  console.log(`${this.name} est en train de manger.`)
  this.energy += amount
}
Key: sleep. Value: function (length) {
  console.log(`${this.name} est en train de dormir.`)
  this.energy += length
}
Key: play. Value: function (length) {
  console.log(`${this.name} est en train de jouer.`)
  this.energy -= length
}
```

Pourquoi cela ? Eh bien, une boucle `for in` va parcourir toutes les **propriétés énumérables** à la fois sur l'objet lui-même ainsi que sur le prototype auquel il délègue. Parce que par défaut, toute propriété que vous ajoutez au prototype de la fonction est énumérable, nous voyons non seulement `name` et `energy`, mais nous voyons également toutes les méthodes sur le prototype - `eat`, `sleep`, et `play`.

Pour corriger cela, nous devons soit spécifier que toutes les méthodes du prototype sont non énumérables **ou** nous devons trouver un moyen de ne logger que si la propriété est sur l'objet `leo` lui-même et non sur le prototype auquel `leo` délègue en cas d'échec de recherche. C'est là que `hasOwnProperty` peut nous aider.

`hasOwnProperty` est une propriété sur chaque objet qui retourne un booléen indiquant si l'objet possède la propriété spécifiée en tant que propriété propre plutôt que sur le prototype auquel l'objet délègue. C'est exactement ce dont nous avons besoin. Maintenant, avec cette nouvelle connaissance, nous pouvons modifier notre code pour tirer parti de `hasOwnProperty` à l'intérieur de notre boucle `for in`.

```javascript
...
const leo = new Animal('Leo', 7)
for(let key in leo) {
  if (leo.hasOwnProperty(key)) {
    console.log(`Key: ${key}. Value: ${leo[key]}`)
  }
}
```

Et maintenant, ce que nous voyons, ce sont uniquement les propriétés qui sont sur l'objet `leo` lui-même plutôt que sur le prototype auquel `leo` délègue également.

```plaintext
Key: name. Value: Leo
Key: energy. Value: 7
```

Si vous êtes encore un peu confus au sujet de `hasOwnProperty`, voici un peu de code qui pourrait clarifier les choses :

```javascript
function Animal (name, energy) {
  this.name = name
  this.energy = energy
}
Animal.prototype.eat = function (amount) {
  console.log(`${this.name} est en train de manger.`)
  this.energy += amount
}
Animal.prototype.sleep = function (length) {
  console.log(`${this.name} est en train de dormir.`)
  this.energy += length
}
Animal.prototype.play = function (length) {
  console.log(`${this.name} est en train de jouer.`)
  this.energy -= length
}
const leo = new Animal('Leo', 7)
leo.hasOwnProperty('name') // true
leo.hasOwnProperty('energy') // true
leo.hasOwnProperty('eat') // false
leo.hasOwnProperty('sleep') // false
leo.hasOwnProperty('play') // false
```

## **Vérifier si un objet est une instance d'une Classe**

Parfois, vous voulez savoir si un objet est une instance d'une classe spécifique. Pour cela, vous pouvez utiliser l'opérateur `instanceof`. Le cas d'utilisation est assez simple, mais la syntaxe réelle est un peu étrange si vous ne l'avez jamais vue auparavant. Cela fonctionne comme ceci :

```javascript
object instanceof Class
```

L'instruction ci-dessus retournera true si `object` est une instance de `Class` et false si ce n'est pas le cas. En revenant à notre exemple `Animal`, nous aurions quelque chose comme ceci :

```javascript
function Animal (name, energy) {
  this.name = name
  this.energy = energy
}
function User () {}
const leo = new Animal('Leo', 7)
leo instanceof Animal // true
leo instanceof User // false
```

La manière dont `instanceof` fonctionne est qu'il vérifie la présence de `constructor.prototype` dans la chaîne de prototypes de l'objet.

Dans l'exemple ci-dessus, `leo instanceof Animal` est `true` parce que `Object.getPrototypeOf(leo) === Animal.prototype`. De plus, `leo instanceof User` est `false` parce que `Object.getPrototypeOf(leo) !== User.prototype`.

## **Créer de nouvelles fonctions constructeur agnostiques**

Pouvez-vous repérer l'erreur dans le code ci-dessous ?

```javascript
function Animal (name, energy) {
  this.name = name
  this.energy = energy
}
const leo = Animal('Leo', 7)
```

Même les développeurs JavaScript expérimentés se font parfois piéger par l'exemple ci-dessus. Parce que nous utilisons le `modèle pseudoclassique` dont nous avons parlé précédemment, lorsque la fonction constructeur `Animal` est invoquée, nous devons nous assurer de l'invoquer avec le mot-clé `new`. Si nous ne le faisons pas, alors le mot-clé `this` ne sera pas créé et il ne sera pas non plus retourné implicitement.

Pour rappel, les lignes commentées sont ce qui se passe en coulisses lorsque vous utilisez le mot-clé `new` sur une fonction.

```javascript
function Animal (name, energy) {
  // const this = Object.create(Animal.prototype)
  this.name = name
  this.energy = energy
  // return this
}
```

Cela semble être un détail trop important pour le laisser à la mémoire des autres développeurs. En supposant que nous travaillons en équipe avec d'autres développeurs, existe-t-il un moyen de nous assurer que notre constructeur `Animal` est toujours invoqué avec le mot-clé `new` ? Il s'avère qu'il y en a un, et c'est en utilisant l'opérateur `instanceof` que nous avons appris précédemment.

Si le constructeur a été appelé avec le mot-clé `new`, alors `this` à l'intérieur du corps du constructeur sera une `instanceof` de la fonction constructeur elle-même. Cela fait beaucoup de grands mots. Voici un peu de code :

```javascript
function Animal (name, energy) {
  if (this instanceof Animal === false) {
    console.warn('Oubli de l\'appel de Animal avec le mot-clé new')
  }
  this.name = name
  this.energy = energy
}
```

Maintenant, au lieu de simplement logger un avertissement à l'utilisateur de la fonction, que se passerait-il si nous réinvoquions la fonction, mais avec le mot-clé `new` cette fois-ci ?

```javascript
function Animal (name, energy) {
  if (this instanceof Animal === false) {
    return new Animal(name, energy)
  }
  this.name = name
  this.energy = energy
}
```

Maintenant, peu importe si `Animal` est invoqué avec le mot-clé `new`, il fonctionnera toujours correctement.

## **Recréer Object.create**

Tout au long de cet article, nous nous sommes fortement appuyés sur `Object.create` afin de créer des objets qui délèguent au prototype de la fonction constructeur. À ce stade, vous devriez savoir comment utiliser `Object.create` dans votre code. Mais une chose à laquelle vous n'avez peut-être pas pensé est comment `Object.create` fonctionne réellement sous le capot.

Afin que vous compreniez **vraiment** comment `Object.create` fonctionne, nous allons le recréer nous-mêmes. Tout d'abord, que savons-nous sur le fonctionnement de `Object.create` ?

1. Il prend en argument un objet.

2. Il crée un objet qui délègue à l'objet argument en cas d'échec de recherche.

3. Il retourne le nouvel objet créé.

Commençons par le point #1.

```javascript
Object.create = function (objToDelegateTo) { }
```

Assez simple.

Maintenant, le point #2 — nous devons créer un objet qui déléguera à l'objet argument en cas d'échec de recherche. Celui-ci est un peu plus délicat. Pour ce faire, nous allons utiliser nos connaissances sur le fonctionnement du mot-clé `new` et des prototypes en JavaScript.

Tout d'abord, à l'intérieur du corps de notre implémentation de `Object.create`, nous allons créer une fonction vide. Ensuite, nous allons définir le prototype de cette fonction vide égal à l'objet argument. Ensuite, afin de créer un nouvel objet, nous allons invoquer notre fonction vide en utilisant le mot-clé `new`. Si nous retournons cet objet nouvellement créé, cela terminera également le point #3.

```javascript
Object.create = function (objToDelegateTo) {
  function Fn(){}
  Fn.prototype = objToDelegateTo
  return new Fn()
}
```

Incroyable. Passons en revue.

Lorsque nous créons une nouvelle fonction, `Fn` dans le code ci-dessus, elle vient avec une propriété `prototype`. Lorsque nous l'invoquons avec le mot-clé `new`, nous savons ce que nous obtiendrons en retour, c'est un objet qui déléguera au prototype de la fonction en cas d'échec de recherche. Si nous remplaçons le prototype de la fonction, alors nous pouvons décider à quel objet déléguer en cas d'échec de recherche.

Donc dans notre exemple ci-dessus, nous remplaçons le prototype de `Fn` par l'objet qui a été passé lorsque `Object.create` a été invoqué, que nous appelons `objToDelegateTo`.

> *Notez que nous ne supportons qu'un seul argument pour Object.create. L'implémentation officielle supporte également un deuxième argument optionnel qui vous permet d'ajouter plus de propriétés à l'objet créé.*

## **Fonctions Fléchées**

Les fonctions fléchées n'ont pas leur propre mot-clé `this`. Par conséquent, les fonctions fléchées ne peuvent pas être des fonctions constructeur. Si vous essayez d'invoquer une fonction fléchée avec le mot-clé `new`, elle lancera une erreur.

```javascript
const Animal = () => {}
const leo = new Animal() // Error: Animal is not a constructor
```

De plus, parce que nous avons démontré ci-dessus que le modèle pseudoclassique ne peut pas être utilisé avec les fonctions fléchées, les fonctions fléchées n'ont pas non plus de propriété `prototype`.

```javascript
const Animal = () => {}
console.log(Animal.prototype) // undefined
```

***Cet article a été initialement publié sur*** [***tylermcginnis.com***](https://tylermcginnis.com/beginners-guide-to-javascript-prototype/) ***et fait partie de notre*** [***cours JavaScript Avancé***](https://tylermcginnis.com/courses/advanced-javascript) ***.***

***Connectez-vous avec*** [***Tyler***](http://twitter.com/tylermcginnis) ***sur Twitter !***