---
title: Guide du débutant sur le prototype en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-28T21:04:03.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-javascripts-prototype
coverImage: https://www.freecodecamp.org/news/content/images/2019/05/1_45wTCahuSKO_9Ne260qf5w.png
tags:
- name: JavaScript
  slug: javascript
- name: prototype
  slug: prototype
- name: Web Development
  slug: web-development
seo_title: Guide du débutant sur le prototype en JavaScript
seo_desc: 'By Tyler McGinnis

  https://www.youtube.com/watch?v=XskMWBXNbp0

  You can''t get very far in JavaScript without dealing with objects. They''re foundational
  to almost every aspect of the JavaScript programming language. In fact, learning
  how to create objec...'
---

Par Tyler McGinnis

%[https://www.youtube.com/watch?v=XskMWBXNbp0]

On ne peut pas aller très loin en JavaScript sans manipuler des objets. Ils sont fondamentaux dans presque tous les aspects du langage de programmation JavaScript. En fait, apprendre à créer des objets est probablement l'une des premières choses que vous avez étudiées à vos débuts. Cela dit, afin d'apprendre le plus efficacement possible les prototypes en JavaScript, nous allons canaliser le développeur junior qui est en nous et revenir aux bases.

Les objets sont des paires clé/valeur. La façon la plus courante de créer un objet est d'utiliser des accolades `{}` et d'ajouter des propriétés et des méthodes à un objet en utilisant la notation par point.

```js
let animal = {}
animal.name = 'Leo'
animal.energy = 10

animal.eat = function (amount) {
  console.log(`${this.name} is eating.`)
  this.energy += amount
}

animal.sleep = function (length) {
  console.log(`${this.name} is sleeping.`)
  this.energy += length
}

animal.play = function (length) {
  console.log(`${this.name} is playing.`)
  this.energy -= length
}

```

Simple. Maintenant, il y a de fortes chances que dans notre application, nous ayons besoin de créer plus d'un animal. Naturellement, l'étape suivante consisterait à encapsuler cette logique à l'intérieur d'une fonction que nous pourrions invoquer chaque fois que nous aurions besoin de créer un nouvel animal. Nous appellerons ce modèle « Instanciation fonctionnelle » (Functional Instantiation) et nous appellerons la fonction elle-même une « fonction constructeur » puisqu'elle est responsable de la « construction » d'un nouvel objet.

#### Instanciation fonctionnelle

```js
function Animal (name, energy) {
  let animal = {}
  animal.name = name
  animal.energy = energy

  animal.eat = function (amount) {
    console.log(`${this.name} is eating.`)
    this.energy += amount
  }

  animal.sleep = function (length) {
    console.log(`${this.name} is sleeping.`)
    this.energy += length
  }

  animal.play = function (length) {
    console.log(`${this.name} is playing.`)
    this.energy -= length
  }

  return animal
}

const leo = Animal('Leo', 7)
const snoop = Animal('Snoop', 10)

```

`« Je pensais que c'était un cours de JavaScript avancé... ? » — Votre cerveau` 

**C'est le cas. Nous y arriverons.**

Désormais, chaque fois que nous voulons créer un nouvel animal (ou plus largement une nouvelle « instance »), tout ce que nous avons à faire est d'invoquer notre fonction `Animal`, en lui passant le `name` (nom) et le niveau d'`energy` (énergie) de l'animal. Cela fonctionne très bien et c'est incroyablement simple. Cependant, pouvez-vous déceler des faiblesses dans ce modèle ? La plus grande, et celle que nous allons tenter de résoudre, concerne les trois méthodes — `eat`, `sleep` et `play`. Chacune de ces méthodes est non seulement dynamique, mais elle est aussi complètement générique. Cela signifie qu'il n'y a aucune raison de recréer ces méthodes comme nous le faisons actuellement chaque fois que nous créons un nouvel animal. Nous gaspillons simplement de la mémoire et rendons chaque objet animal plus gros qu'il ne devrait l'être. Pouvez-vous penser à une solution ? Et si, au lieu de recréer ces méthodes à chaque fois que nous créons un nouvel animal, nous les déplacions vers leur propre objet, puis que chaque animal fasse référence à cet objet ? Nous pouvons appeler ce modèle « Instanciation fonctionnelle avec méthodes partagées », c'est un peu long mais descriptif ‍♂️.

#### Instanciation fonctionnelle avec méthodes partagées

```js
const animalMethods = {
  eat(amount) {
    console.log(`${this.name} is eating.`)
    this.energy += amount
  },
  sleep(length) {
    console.log(`${this.name} is sleeping.`)
    this.energy += length
  },
  play(length) {
    console.log(`${this.name} is playing.`)
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

En déplaçant les méthodes partagées vers leur propre objet et en référençant cet objet à l'intérieur de notre fonction `Animal`, nous avons maintenant résolu le problème du gaspillage de mémoire et des objets animaux trop volumineux.

#### Object.create

Améliorons encore une fois notre exemple en utilisant `Object.create`. Pour faire simple, **Object.create vous permet de créer un objet qui déléguera à un autre objet en cas de recherches infructueuses**. Autrement dit, Object.create vous permet de créer un objet et, chaque fois qu'une recherche de propriété échoue sur cet objet, il peut consulter un autre objet pour voir si cet autre objet possède la propriété. C'était beaucoup de mots. Voyons du code.

```js
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

Ainsi, dans l'exemple ci-dessus, parce que `child` a été créé avec `Object.create(parent)`, chaque fois qu'il y a une recherche de propriété infructueuse sur `child`, JavaScript déléguera cette recherche à l'objet `parent`. Cela signifie que même si `child` n'a pas de propriété `heritage`, `parent` en a une, donc lorsque vous affichez `child.heritage`, vous obtiendrez l'héritage du `parent` qui était `Irish`.

Maintenant que nous avons `Object.create` dans notre boîte à outils, comment pouvons-nous l'utiliser pour simplifier notre code `Animal` de tout à l'heure ? Eh bien, au lieu d'ajouter toutes les méthodes partagées à l'animal une par une comme nous le faisons actuellement, nous pouvons utiliser Object.create pour déléguer à l'objet `animalMethods` à la place. Pour avoir l'air vraiment intelligent, appelons celui-ci « Instanciation fonctionnelle avec méthodes partagées et Object.create » 💡.

#### Instanciation fonctionnelle avec méthodes partagées et Object.create

```js{17}
const animalMethods = {
  eat(amount) {
    console.log(`${this.name} is eating.`)
    this.energy += amount
  },
  sleep(length) {
    console.log(`${this.name} is sleeping.`)
    this.energy += length
  },
  play(length) {
    console.log(`${this.name} is playing.`)
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

✨ Ainsi, maintenant, lorsque nous appelons `leo.eat`, JavaScript cherchera la méthode `eat` sur l'objet `leo`. Cette recherche échouera, puis, grâce à Object.create, elle sera déléguée à l'objet `animalMethods`, qui est l'endroit où elle trouvera `eat`.

Jusqu'ici, tout va bien. Il y a encore quelques améliorations que nous pouvons apporter. Il semble un peu « bricolé » de devoir gérer un objet séparé (`animalMethods`) afin de partager des méthodes entre les instances. Cela ressemble à une fonctionnalité commune que vous voudriez voir implémentée dans le langage lui-même. Il s'avère que c'est le cas et c'est la raison même pour laquelle vous êtes ici : `prototype`.

Alors, qu'est-ce que `prototype` exactement en JavaScript ? Eh bien, pour faire simple, chaque fonction en JavaScript possède une propriété `prototype` qui fait référence à un objet. Décevant, n'est-ce pas ? Testez-le par vous-même.

```js
function doThing () {}
console.log(doThing.prototype) // {}

```

Et si, au lieu de créer un objet séparé pour gérer nos méthodes (comme nous le faisons avec `animalMethods`), nous mettions simplement chacune de ces méthodes sur le prototype de la fonction `Animal` ? Alors, tout ce que nous aurions à faire, au lieu d'utiliser Object.create pour déléguer à `animalMethods`, serait de l'utiliser pour déléguer à `Animal.prototype`. Nous appellerons ce modèle « Instanciation prototypale ».

#### Instanciation prototypale

```js{2,9-22}
function Animal (name, energy) {
  let animal = Object.create(Animal.prototype)
  animal.name = name
  animal.energy = energy

  return animal
}

Animal.prototype.eat = function (amount) {
  console.log(`${this.name} is eating.`)
  this.energy += amount
}

Animal.prototype.sleep = function (length) {
  console.log(`${this.name} is sleeping.`)
  this.energy += length
}

Animal.prototype.play = function (length) {
  console.log(`${this.name} is playing.`)
  this.energy -= length
}

const leo = Animal('Leo', 7)
const snoop = Animal('Snoop', 10)

leo.eat(10)
snoop.play(5)

```

??? J'espère que vous venez d'avoir un grand moment de déclic. Encore une fois, `prototype` n'est qu'une propriété que chaque fonction en JavaScript possède et, comme nous l'avons vu plus haut, elle nous permet de partager des méthodes entre toutes les instances d'une fonction. Toutes nos fonctionnalités restent les mêmes, mais maintenant, au lieu de devoir gérer un objet séparé pour toutes les méthodes, nous pouvons simplement utiliser un autre objet qui est intégré à la fonction `Animal` elle-même, `Animal.prototype`.

---

## Allons. Plus. Loin.

À ce stade, nous savons trois choses :

1. Comment créer une fonction constructeur.
2. Comment ajouter des méthodes au prototype de la fonction constructeur.
3. Comment utiliser Object.create pour déléguer les recherches infructueuses au prototype de la fonction.

Ces trois tâches semblent assez fondamentales pour n'importe quel langage de programmation. JavaScript est-il vraiment si mauvais qu'il n'existe pas de moyen plus simple et « intégré » d'accomplir la même chose ? Comme vous pouvez probablement le deviner à ce stade, il y en a un, et c'est en utilisant le mot-clé `new`.

Ce qui est bien avec l'approche lente et méthodique que nous avons adoptée pour en arriver là, c'est que vous aurez maintenant une compréhension approfondie de ce que fait exactement le mot-clé `new` en JavaScript sous le capot.

En repensant à notre constructeur `Animal`, les deux parties les plus importantes étaient la création de l'objet et son renvoi. Sans la création de l'objet avec `Object.create`, nous ne serions pas en mesure de déléguer au prototype de la fonction lors de recherches infructueuses. Sans l'instruction `return`, nous ne récupérerions jamais l'objet créé.

```js{2,6}
function Animal (name, energy) {
  let animal = Object.create(Animal.prototype)
  animal.name = name
  animal.energy = energy

  return animal
}

```

Voici la chose géniale à propos de `new` : lorsque vous invoquez une fonction en utilisant le mot-clé `new`, ces deux lignes sont effectuées pour vous implicitement (« sous le capot ») et l'objet qui est créé s'appelle `this`.

En utilisant des commentaires pour montrer ce qui se passe sous le capot et en supposant que le constructeur `Animal` est appelé avec le mot-clé `new`, il peut être réécrit comme ceci.

```js
function Animal (name, energy) {
  // const this = Object.create(Animal.prototype)

  this.name = name
  this.energy = energy

  // return this
}

const leo = new Animal('Leo', 7)
const snoop = new Animal('Snoop', 10)

```

et sans les commentaires « sous le capot »

```js
function Animal (name, energy) {
  this.name = name
  this.energy = energy
}

Animal.prototype.eat = function (amount) {
  console.log(`${this.name} is eating.`)
  this.energy += amount
}

Animal.prototype.sleep = function (length) {
  console.log(`${this.name} is sleeping.`)
  this.energy += length
}

Animal.prototype.play = function (length) {
  console.log(`${this.name} is playing.`)
  this.energy -= length
}

const leo = new Animal('Leo', 7)
const snoop = new Animal('Snoop', 10)

```

Encore une fois, la raison pour laquelle cela fonctionne et que l'objet `this` est créé pour nous est que nous avons appelé la fonction constructeur avec le mot-clé `new`. Si vous oubliez `new` lorsque vous invoquez la fonction, cet objet `this` n'est jamais créé et n'est pas non plus renvoyé implicitement. Nous pouvons voir le problème avec cela dans l'exemple ci-dessous.

```js{6-7}
function Animal (name, energy) {
  this.name = name
  this.energy = energy
}

const leo = Animal('Leo', 7)
console.log(leo) // undefined

```

Le nom de ce modèle est « Instanciation pseudoclassique » (Pseudoclassical Instantiation).

Si JavaScript n'est pas votre premier langage de programmation, vous commencez peut-être à vous impatienter.

`« C'est quoi ce délire, ce gars vient de recréer une version pourrie d'une Classe » — Vous` 

Pour ceux qui ne sont pas familiers, une Classe vous permet de créer un plan pour un objet. Ensuite, chaque fois que vous créez une instance de cette Classe, vous obtenez un objet avec les propriétés et les méthodes définies dans le plan.

Cela vous semble familier ? C'est essentiellement ce que nous avons fait avec notre fonction constructeur `Animal` ci-dessus. Cependant, au lieu d'utiliser le mot-clé `class`, nous avons juste utilisé une bonne vieille fonction JavaScript pour recréer la même fonctionnalité. Certes, cela a demandé un peu de travail supplémentaire ainsi qu'une certaine connaissance de ce qui se passe « sous le capot » de JavaScript, mais les résultats sont les mêmes.

Voici la bonne nouvelle. JavaScript n'est pas un langage mort. Il est constamment amélioré et complété par le [comité TC-39](https://tylermcginnis.com/ecmascript/). Cela signifie que même si la version initiale de JavaScript ne supportait pas les classes, il n'y a aucune raison pour qu'elles ne puissent pas être ajoutées à la spécification officielle. En fait, c'est exactement ce qu'a fait le comité TC-39. En 2015, EcmaScript (la spécification officielle de JavaScript) 6 est sorti avec le support des Classes et du mot-clé `class`. Voyons à quoi ressemblerait notre fonction constructeur `Animal` ci-dessus avec la nouvelle syntaxe de classe.

```js
class Animal {
  constructor(name, energy) {
    this.name = name
    this.energy = energy
  }
  eat(amount) {
    console.log(`${this.name} is eating.`)
    this.energy += amount
  }
  sleep(length) {
    console.log(`${this.name} is sleeping.`)
    this.energy += length
  }
  play(length) {
    console.log(`${this.name} is playing.`)
    this.energy -= length
  }
}

const leo = new Animal('Leo', 7)
const snoop = new Animal('Snoop', 10)

```

Plutôt propre, non ?

Alors si c'est la nouvelle façon de créer des classes, pourquoi avons-nous passé autant de temps à examiner l'ancienne façon ? La raison en est que la nouvelle façon (avec le mot-clé `class`) est principalement du « sucre syntaxique » (syntactical sugar) par rapport à la façon existante dont nous avons appelé le modèle pseudoclassique. Afin de comprendre *pleinement* la syntaxe de commodité des classes ES6, vous devez d'abord comprendre le modèle pseudoclassique.

---

À ce stade, nous avons couvert les principes fondamentaux du prototype de JavaScript. Le reste de cet article sera dédié à la compréhension d'autres sujets « bons à savoir » qui y sont liés. Dans un autre article, nous verrons comment nous pouvons prendre ces principes fondamentaux et les utiliser pour comprendre comment fonctionne l'héritage en JavaScript.

---

### Méthodes d'Array

Nous avons parlé en profondeur ci-dessus de la façon dont, si vous voulez partager des méthodes entre les instances d'une classe, vous devriez placer ces méthodes sur le prototype de la classe (ou de la fonction). Nous pouvons voir ce même modèle démontré si nous regardons la classe `Array`. Historiquement, vous avez probablement créé vos tableaux comme ceci

```js
const friends = []

```

Il s'avère que ce n'est que du sucre par rapport à la création d'une `new` instance de la classe `Array`.

```js
const friendsWithSugar = []

const friendsWithoutSugar = new Array()

```

Une chose à laquelle vous n'avez peut-être jamais pensé est : comment chaque instance d'un tableau possède-t-elle toutes ces méthodes intégrées (`splice`, `slice`, `pop`, etc.) ?

Eh bien, comme vous le savez maintenant, c'est parce que ces méthodes résident sur `Array.prototype` et lorsque vous créez une nouvelle instance de `Array`, vous utilisez le mot-clé `new` qui met en place cette délégation vers `Array.prototype` lors de recherches infructueuses.

Nous pouvons voir toutes les méthodes du tableau en affichant simplement `Array.prototype`.

```js
console.log(Array.prototype)

/*
  concat: ƒn concat()
  constructor: ƒn Array()
  copyWithin: ƒn copyWithin()
  entries: ƒn entries()
  every: ƒn every()
  fill: ƒn fill()
  filter: ƒn filter()
  find: ƒn find()
  findIndex: ƒn findIndex()
  forEach: ƒn forEach()
  includes: ƒn includes()
  indexOf: ƒn indexOf()
  join: ƒn join()
  keys: ƒn keys()
  lastIndexOf: ƒn lastIndexOf()
  length: 0n
  map: ƒn map()
  pop: ƒn pop()
  push: ƒn push()
  reduce: ƒn reduce()
  reduceRight: ƒn reduceRight()
  reverse: ƒn reverse()
  shift: ƒn shift()
  slice: ƒn slice()
  some: ƒn some()
  sort: ƒn sort()
  splice: ƒn splice()
  toLocaleString: ƒn toLocaleString()
  toString: ƒn toString()
  unshift: ƒn unshift()
  values: ƒn values()
*/


```

La même logique exacte existe également pour les Objets. Tous les objets délégueront à `Object.prototype` lors de recherches infructueuses, c'est pourquoi tous les objets ont des méthodes comme `toString` et `hasOwnProperty`.

### Méthodes statiques

Jusqu'à présent, nous avons couvert le pourquoi et le comment du partage de méthodes entre les instances d'une Classe. Cependant, que se passerait-il si nous avions une méthode importante pour la Classe, mais qui n'avait pas besoin d'être partagée entre les instances ? Par exemple, que se passerait-il si nous avions une fonction qui prenait un tableau d'instances `Animal` et déterminait laquelle devait être nourrie ensuite ? Nous l'appellerons `nextToEat`.

```js
function nextToEat (animals) {
  const sortedByLeastEnergy = animals.sort((a,b) => {
    return a.energy - b.energy
  })

  return sortedByLeastEnergy[0].name
}

```

Il n'est pas logique que `nextToEat` réside sur `Animal.prototype` puisque nous ne voulons pas la partager entre toutes les instances. Au lieu de cela, nous pouvons la considérer davantage comme une méthode utilitaire. Donc, si `nextToEat` ne doit pas résider sur `Animal.prototype`, où devrions-nous la mettre ? Eh bien, la réponse évidente est que nous pourrions simplement placer `nextToEat` dans la même portée que notre classe `Animal`, puis la référencer quand nous en avons besoin comme nous le ferions normalement.

```js
class Animal {
  constructor(name, energy) {
    this.name = name
    this.energy = energy
  }
  eat(amount) {
    console.log(`${this.name} is eating.`)
    this.energy += amount
  }
  sleep(length) {
    console.log(`${this.name} is sleeping.`)
    this.energy += length
  }
  play(length) {
    console.log(`${this.name} is playing.`)
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

Cela fonctionne, mais il y a une meilleure façon de faire.

Chaque fois que vous avez une méthode spécifique à une classe elle-même, mais qui n'a pas besoin d'être partagée entre les instances de cette classe, vous pouvez l'ajouter en tant que propriété `static` de la classe.

```js{18-24}
class Animal {
  constructor(name, energy) {
    this.name = name
    this.energy = energy
  }
  eat(amount) {
    console.log(`${this.name} is eating.`)
    this.energy += amount
  }
  sleep(length) {
    console.log(`${this.name} is sleeping.`)
    this.energy += length
  }
  play(length) {
    console.log(`${this.name} is playing.`)
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

Maintenant, parce que nous avons ajouté `nextToEat` en tant que propriété `static` sur la classe, elle réside sur la classe `Animal` elle-même (pas sur son prototype) et on peut y accéder en utilisant `Animal.nextToEat`.

```js{4}
const leo = new Animal('Leo', 7)
const snoop = new Animal('Snoop', 10)

console.log(Animal.nextToEat([leo, snoop])) // Leo

```

Parce que nous avons suivi un modèle similaire tout au long de cet article, voyons comment nous accomplirions la même chose en utilisant ES5. Dans l'exemple ci-dessus, nous avons vu comment l'utilisation du mot-clé `static` plaçait la méthode directement sur la classe elle-même. Avec ES5, ce même modèle est aussi simple que d'ajouter manuellement la méthode à l'objet fonction.

```js{21-27}
function Animal (name, energy) {
  this.name = name
  this.energy = energy
}

Animal.prototype.eat = function (amount) {
  console.log(`${this.name} is eating.`)
  this.energy += amount
}

Animal.prototype.sleep = function (length) {
  console.log(`${this.name} is sleeping.`)
  this.energy += length
}

Animal.prototype.play = function (length) {
  console.log(`${this.name} is playing.`)
  this.energy -= length
}

Animal.nextToEat = function (animals) {
  const sortedByLeastEnergy = animals.sort((a,b) => {
    return a.energy - b.energy
  })

  return sortedByLeastEnergy[0].name
}

const leo = new Animal('Leo', 7)
const snoop = new Animal('Snoop', 10)

console.log(Animal.nextToEat([leo, snoop])) // Leo

```

### Obtenir le prototype d'un objet

Quel que soit le modèle que vous avez utilisé pour créer un objet, l'obtention du prototype de cet objet peut être accomplie en utilisant la méthode `Object.getPrototypeOf`.

```js{24,25,27}
function Animal (name, energy) {
  this.name = name
  this.energy = energy
}

Animal.prototype.eat = function (amount) {
  console.log(`${this.name} is eating.`)
  this.energy += amount
}

Animal.prototype.sleep = function (length) {
  console.log(`${this.name} is sleeping.`)
  this.energy += length
}

Animal.prototype.play = function (length) {
  console.log(`${this.name} is playing.`)
  this.energy -= length
}

const leo = new Animal('Leo', 7)
const prototype = Object.getPrototypeOf(leo)

console.log(prototype)
// {constructor: ƒ, eat: ƒ, sleep: ƒ, play: ƒ}

prototype === Animal.prototype // true

```

Il y a deux points importants à retenir du code ci-dessus.

Premièrement, vous remarquerez que `prototype` est un objet avec 4 méthodes, `constructor`, `eat`, `sleep` et `play`. C'est logique. Nous avons utilisé `getPrototypeOf` en passant l'instance `leo` pour récupérer le prototype de cette instance, qui est l'endroit où résident toutes nos méthodes. Cela nous apprend également une chose de plus sur `prototype` dont nous n'avons pas encore parlé. Par défaut, l'objet `prototype` aura une propriété `constructor` qui pointe vers la fonction d'origine ou la classe à partir de laquelle l'instance a été créée. Cela signifie également que, parce que JavaScript place par défaut une propriété `constructor` sur le prototype, toutes les instances pourront accéder à leur constructeur via `instance.constructor`.

Le deuxième point important à retenir ci-dessus est que `Object.getPrototypeOf(leo) === Animal.prototype`. C'est également logique. La fonction constructeur `Animal` possède une propriété prototype où nous pouvons partager des méthodes entre toutes les instances, et `getPrototypeOf` nous permet de voir le prototype de l'instance elle-même.

```js
function Animal (name, energy) {
  this.name = name
  this.energy = energy
}

const leo = new Animal('Leo', 7)
console.log(leo.constructor) // Affiche la fonction constructeur

```

Pour faire le lien avec ce dont nous avons parlé plus tôt avec `Object.create`, la raison pour laquelle cela fonctionne est que toutes les instances de `Animal` vont déléguer à `Animal.prototype` lors de recherches infructueuses. Ainsi, lorsque vous essayez d'accéder à `leo.constructor`, `leo` n'a pas de propriété `constructor`, il déléguera donc cette recherche à `Animal.prototype` qui, en effet, possède une propriété `constructor`. Si ce paragraphe n'est pas clair, relisez la section sur `Object.create` ci-dessus.

Vous avez peut-être déjà vu `__proto__` utilisé pour obtenir le prototype d'une instance. C'est un vestige du passé. À la place, utilisez **Object.getPrototypeOf(instance)** comme nous l'avons vu plus haut.

### Déterminer si une propriété réside sur le prototype

Il y a certains cas où vous devez savoir si une propriété réside sur l'instance elle-même ou si elle réside sur le prototype auquel l'objet délègue. Nous pouvons voir cela en action en bouclant sur notre objet `leo` que nous avons créé. Disons que le but était de boucler sur `leo` et d'afficher toutes ses clés et valeurs. En utilisant une boucle `for in`, cela ressemblerait probablement à ceci.

```js
function Animal (name, energy) {
  this.name = name
  this.energy = energy
}

Animal.prototype.eat = function (amount) {
  console.log(`${this.name} is eating.`)
  this.energy += amount
}

Animal.prototype.sleep = function (length) {
  console.log(`${this.name} is sleeping.`)
  this.energy += length
}

Animal.prototype.play = function (length) {
  console.log(`${this.name} is playing.`)
  this.energy -= length
}

const leo = new Animal('Leo', 7)

for(let key in leo) {
  console.log(`Key: ${key}. Value: ${leo[key]}`)
}

```

À quoi vous attendriez-vous ? Très probablement, à quelque chose comme ceci -

```js
Key: name. Value: Leo
Key: energy. Value: 7

```

Cependant, ce que vous avez vu si vous avez exécuté le code, c'est ceci -

```js
Key: name. Value: Leo
Key: energy. Value: 7
Key: eat. Value: function (amount) {
  console.log(`${this.name} is eating.`)
  this.energy += amount
}
Key: sleep. Value: function (length) {
  console.log(`${this.name} is sleeping.`)
  this.energy += length
}
Key: play. Value: function (length) {
  console.log(`${this.name} is playing.`)
  this.energy -= length
}

```

Pourquoi cela ? Eh bien, une boucle `for in` va boucler sur toutes les **propriétés énumérables** (enumerable properties) à la fois sur l'objet lui-même et sur le prototype auquel il délègue. Comme, par défaut, toute propriété que vous ajoutez au prototype de la fonction est énumérable, nous voyons non seulement `name` et `energy`, mais nous voyons aussi toutes les méthodes sur le prototype — `eat`, `sleep` et `play`. Pour corriger cela, nous devons soit spécifier que toutes les méthodes du prototype sont non énumérables, **soit** nous avons besoin d'un moyen de n'afficher que si la propriété est sur l'objet `leo` lui-même et non sur le prototype auquel `leo` délègue lors de recherches infructueuses. C'est là que `hasOwnProperty` peut nous aider.

`hasOwnProperty` est une propriété présente sur chaque objet qui renvoie un booléen indiquant si l'objet possède la propriété spécifiée en tant que propriété propre plutôt que sur le prototype auquel l'objet délègue. C'est exactement ce dont nous avons besoin. Maintenant, avec cette nouvelle connaissance, nous pouvons modifier notre code pour tirer parti de `hasOwnProperty` à l'intérieur de notre boucle `for in`.

```js
...

const leo = new Animal('Leo', 7)

for(let key in leo) {
  if (leo.hasOwnProperty(key)) {
    console.log(`Key: ${key}. Value: ${leo[key]}`)
  }
}

```

Et maintenant, ce que nous voyons, ce sont uniquement les propriétés qui sont sur l'objet `leo` lui-même plutôt que sur le prototype auquel `leo` délègue également.

```js
Key: name. Value: Leo
Key: energy. Value: 7

```

Si vous êtes encore un peu confus à propos de `hasOwnProperty`, voici un code qui pourrait vous éclairer.

```js
function Animal (name, energy) {
  this.name = name
  this.energy = energy
}

Animal.prototype.eat = function (amount) {
  console.log(`${this.name} is eating.`)
  this.energy += amount
}

Animal.prototype.sleep = function (length) {
  console.log(`${this.name} is sleeping.`)
  this.energy += length
}

Animal.prototype.play = function (length) {
  console.log(`${this.name} is playing.`)
  this.energy -= length
}

const leo = new Animal('Leo', 7)

leo.hasOwnProperty('name') // true
leo.hasOwnProperty('energy') // true
leo.hasOwnProperty('eat') // false
leo.hasOwnProperty('sleep') // false
leo.hasOwnProperty('play') // false

```

### Vérifier si un objet est une instance d'une Classe

Parfois, vous voulez savoir si un objet est une instance d'une classe spécifique. Pour ce faire, vous pouvez utiliser l'opérateur `instanceof`. Le cas d'utilisation est assez simple, mais la syntaxe réelle est un peu étrange si vous ne l'avez jamais vue auparavant. Cela fonctionne comme ceci

```js
object instanceof Class

```

L'instruction ci-dessus renverra vrai si `object` est une instance de `Class` et faux si ce n'est pas le cas. En revenant à notre exemple `Animal`, nous aurions quelque chose comme ceci.

```js
function Animal (name, energy) {
  this.name = name
  this.energy = energy
}

function User () {}

const leo = new Animal('Leo', 7)

leo instanceof Animal // true
leo instanceof User // false

```

La façon dont `instanceof` fonctionne est qu'il vérifie la présence de `constructor.prototype` dans la chaîne de prototypes de l'objet. Dans l'exemple ci-dessus, `leo instanceof Animal` est `true` parce que `Object.getPrototypeOf(leo) === Animal.prototype`. De plus, `leo instanceof User` est `false` parce que `Object.getPrototypeOf(leo) !== User.prototype`.

### Créer des fonctions constructeurs agnostiques au mot-clé « new »

Pouvez-vous repérer l'erreur dans le code ci-dessous ?

```js
function Animal (name, energy) {
  this.name = name
  this.energy = energy
}

const leo = Animal('Leo', 7)

```

Même les développeurs JavaScript chevronnés se font parfois piéger par l'exemple ci-dessus. Parce que nous utilisons le « modèle pseudoclassique » que nous avons appris plus tôt, lorsque la fonction constructeur `Animal` est invoquée, nous devons nous assurer de l'invoquer avec le mot-clé `new`. Si nous ne le faisons pas, alors le mot-clé `this` ne sera pas créé et il ne sera pas non plus renvoyé implicitement.

Pour rappel, les lignes commentées correspondent à ce qui se passe en coulisses lorsque vous utilisez le mot-clé `new` sur une fonction.

```js
function Animal (name, energy) {
  // const this = Object.create(Animal.prototype)

  this.name = name
  this.energy = energy

  // return this
}

```

Cela semble être un détail trop important pour être laissé à la mémoire des autres développeurs. En supposant que nous travaillions en équipe avec d'autres développeurs, y a-t-il un moyen de s'assurer que notre constructeur `Animal` est toujours invoqué avec le mot-clé `new` ? Il s'avère que oui, et c'est en utilisant l'opérateur `instanceof` que nous avons appris précédemment.

Si le constructeur a été appelé avec le mot-clé `new`, alors `this` à l'intérieur du corps du constructeur sera une `instanceof` de la fonction constructeur elle-même. C'était beaucoup de grands mots. Voici du code.

```js
function Animal (name, energy) {
  if (this instanceof Animal === false) {
    console.warn('Forgot to call Animal with the new keyword')
  }

  this.name = name
  this.energy = energy
}

```

Maintenant, au lieu de simplement afficher un avertissement à l'utilisateur de la fonction, et si nous ré-invoquions la fonction, mais avec le mot-clé `new` cette fois ?

```js
function Animal (name, energy) {
  if (this instanceof Animal === false) {
    return new Animal(name, energy)
  }

  this.name = name
  this.energy = energy
}

```

Maintenant, que `Animal` soit invoqué avec le mot-clé `new` ou non, il fonctionnera toujours correctement.

### Recréer Object.create

Tout au long de cet article, nous nous sommes fortement appuyés sur `Object.create` afin de créer des objets qui délèguent au prototype de la fonction constructeur. À ce stade, vous devriez savoir comment utiliser `Object.create` dans votre code, mais une chose à laquelle vous n'avez peut-être pas pensé est la façon dont `Object.create` fonctionne réellement sous le capot. Pour que vous compreniez **vraiment** comment fonctionne `Object.create`, nous allons le recréer nous-mêmes. Tout d'abord, que savons-nous du fonctionnement de `Object.create` ?

1. Il prend en argument un objet.
2. Il crée un objet qui délègue à l'objet passé en argument lors de recherches infructueuses.
3. Il renvoie le nouvel objet créé.

Commençons par le n°1.

```js
Object.create = function (objToDelegateTo) {

}

```

Assez simple.

Maintenant le n°2 — nous devons créer un objet qui déléguera à l'objet passé en argument lors de recherches infructueuses. Celui-ci est un peu plus délicat. Pour ce faire, nous utiliserons nos connaissances sur le fonctionnement du mot-clé `new` et des prototypes en JavaScript. Tout d'abord, à l'intérieur du corps de notre implémentation de `Object.create`, nous allons créer une fonction vide. Ensuite, nous définirons le prototype de cette fonction vide comme étant égal à l'objet passé en argument. Ensuite, afin de créer un nouvel objet, nous invoquerons notre fonction vide en utilisant le mot-clé `new`. Si nous renvoyons cet objet nouvellement créé, cela terminera également le n°3.

```js
Object.create = function (objToDelegateTo) {
  function Fn(){}
  Fn.prototype = objToDelegateTo
  return new Fn()
}

```

Incroyable. Analysons cela.

Lorsque nous créons une nouvelle fonction, `Fn` dans le code ci-dessus, elle est livrée avec une propriété `prototype`. Lorsque nous l'invoquons avec le mot-clé `new`, nous savons que nous obtiendrons en retour un objet qui déléguera au prototype de la fonction lors de recherches infructueuses. Si nous surchargeons le prototype de la fonction, nous pouvons alors décider vers quel objet déléguer lors de recherches infructueuses. Ainsi, dans notre exemple ci-dessus, nous surchargeons le prototype de `Fn` avec l'objet qui a été passé lors de l'invocation de `Object.create`, que nous appelons `objToDelegateTo`.

Notez que nous ne supportons qu'un seul argument pour Object.create. L'implémentation officielle supporte également un deuxième argument optionnel qui vous permet d'ajouter plus de propriétés à l'objet créé.

### Fonctions fléchées

Les fonctions fléchées n'ont pas leur propre mot-clé `this`. Par conséquent, les fonctions fléchées ne peuvent pas être des fonctions constructeurs et si vous essayez d'invoquer une fonction fléchée avec le mot-clé `new`, elle renverra une erreur.

```js
const Animal = () => {}

const leo = new Animal() // Error: Animal is not a constructor

```

De plus, comme nous avons démontré plus haut que le modèle pseudoclassique ne peut pas être utilisé avec les fonctions fléchées, celles-ci n'ont pas non plus de propriété `prototype`.

```js
const Animal = () => {}
console.log(Animal.prototype) // undefined

```

---

<h2 style="font-weight: bold; color: white; margin: 0; background: rgb(255, 89, 74); padding: 15px; border-radius: 3px;">Ceci fait partie de notre <b><a style="color: #005999; text-decoration: none" href="https://tylermcginnis.com/courses/advanced-javascript">cours de JavaScript avancé</a></b>. Si vous avez aimé cet article, allez y jeter un œil.</h2>

---