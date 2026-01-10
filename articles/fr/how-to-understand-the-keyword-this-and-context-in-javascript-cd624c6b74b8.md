---
title: Comment comprendre le mot-clé this et le contexte en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-21T17:03:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-understand-the-keyword-this-and-context-in-javascript-cd624c6b74b8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4Ufc1CWbaLhjEMhPgVV3Qw.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment comprendre le mot-clé this et le contexte en JavaScript
seo_desc: 'By Lukas Gisder-Dubé

  As mentioned in one of my earlier articles, mastering JavaScript fully can be a
  lengthy journey. You may have come across this on your journey as a JavaScript Developer.
  When I started out, I first saw it when using eventListener...'
---

Par Lukas Gisder-Dubé

Comme mentionné dans [un de mes articles précédents](https://levelup.gitconnected.com/10-things-to-learn-on-the-way-to-become-a-javascript-master-f4fc632b2bb7), maîtriser pleinement JavaScript peut être un long voyage. Vous avez peut-être rencontré `this` lors de votre parcours en tant que développeur JavaScript. Lorsque j'ai commencé, je l'ai d'abord vu en utilisant `eventListeners` et avec jQuery. Plus tard, j'ai dû l'utiliser souvent avec React et je suis sûr que vous aussi. Cela ne signifie pas que je comprenais vraiment ce que c'est et comment en prendre pleinement le contrôle.

Cependant, il est très utile de maîtriser le concept derrière celui-ci, et lorsqu'on l'aborde avec un esprit clair, ce n'est pas très difficile non plus.

#### Approfondir this

> _Expliquer `this` peut entraîner beaucoup de confusion, simplement par la dénomination du mot-clé._

`this` est étroitement lié au contexte dans lequel vous vous trouvez dans votre programme. Commençons tout en haut. Dans notre navigateur, si vous tapez simplement `this` dans la console, vous obtiendrez l'objet `window`, le contexte le plus externe pour votre JavaScript. Dans Node.js, si nous faisons :

```js
console.log(this)
```

nous obtenons `{}`, un objet vide. C'est un peu bizarre, mais il semble que Node.js se comporte ainsi. Si vous faites

```js
(function() {
  console.log(this);
})();
```

toutefois, vous recevrez l'objet `global`, le contexte le plus externe. Dans ce contexte, `setTimeout`, `setInterval`, sont stockés. N'hésitez pas à jouer un peu avec pour voir ce que vous pouvez faire avec. À partir de là, il n'y a presque aucune différence entre Node.js et le navigateur. J'utiliserai `window`. Rappelez-vous simplement que dans Node.js, ce sera l'objet `global`, mais cela ne fait pas vraiment de différence.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ucforPRGm6kR3bdZMHzHKQ.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/e_5NhSomvS4?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Chor Hung Tsang</a> sur <a href="https://unsplash.com/search/photos/top-level?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Rappelez-vous : Le contexte n'a de sens qu'à l'intérieur des fonctions

Imaginez que vous écriviez un programme sans imbriquer quoi que ce soit dans des fonctions. Vous écririez simplement une ligne après l'autre, sans descendre dans des structures spécifiques. Cela signifie que vous n'avez pas à garder une trace de l'endroit où vous vous trouvez. Vous êtes toujours au même niveau.

Lorsque vous commencez à avoir des fonctions, vous pouvez avoir différents niveaux de votre programme et `this` représente où vous êtes, quel objet a appelé la fonction.

#### Garder une trace de l'objet appelant

Examinons l'exemple suivant et voyons comment `this` change en fonction du contexte :

```js
const coffee = {
  strong: true,
  info: function() {
    console.log(`The coffee is ${this.strong ? '' : 'not '}strong`)
  },
}

coffee.info() // The coffee is strong
```

Puisque nous appelons une fonction qui est déclarée à l'intérieur de l'objet `coffee`, notre contexte change pour cet objet exactement. Nous pouvons maintenant accéder à toutes les propriétés de cet objet via `this`. Dans notre exemple ci-dessus, nous pourrions également simplement y faire référence directement en faisant `coffee.strong`. Cela devient plus intéressant lorsque nous ne savons pas dans quel contexte, quel objet, nous nous trouvons ou lorsque les choses deviennent simplement un peu plus complexes. Jetez un œil à l'exemple suivant :

```js
const drinks = [
  {
    name: 'Coffee',
    addictive: true,
    info: function() {
      console.log(`${this.name} is ${this.addictive ? '' : 'not '} addictive.`)
    },
  },
  {
    name: 'Celery Juice',
    addictive: false,
    info: function() {
      console.log(`${this.name} is ${this.addictive ? '' : 'not '} addictive.`)
    },
  },
]

function pickRandom(arr) {
  return arr[Math.floor(Math.random() * arr.length)]
}

pickRandom(drinks).info()
```

#### Classes et Instances

Les classes peuvent être utilisées pour abstraire votre code et partager des comportements. Répéter toujours la déclaration de la fonction `info` dans le dernier exemple n'est pas bon. Puisque les classes et leurs instances sont en fait des objets, elles se comportent de la même manière. Une chose à noter cependant, c'est que déclarer `this` dans le constructeur est en fait une prédiction pour l'avenir, lorsqu'il y aura une instance.

Examinons cela :

```js
class Coffee {
  constructor(strong) {
    this.strong = !!strong
  }
  info() {
    console.log(`This coffee is ${this.strong ? '' : 'not '}strong`)
  }
}

const strongCoffee = new Coffee(true)
const normalCoffee = new Coffee(false)

strongCoffee.info() // This coffee is strong
normalCoffee.info() // This coffee is not strong
```

#### Piège : appels de fonctions imbriquées de manière transparente

Parfois, nous nous retrouvons dans un contexte que nous n'avions pas vraiment prévu. Cela peut se produire lorsque nous appelons la fonction à l'intérieur d'un autre contexte d'objet sans le savoir. Un exemple très courant est lorsque nous utilisons `setTimeout` ou `setInterval` :

```js
// MAUVAIS EXEMPLE
const coffee = {
  strong: true,
  amount: 120,
  drink: function() {
    setTimeout(function() {
      if (this.amount) this.amount -= 10
    }, 10)
  },
}

coffee.drink()
```

Selon vous, quelle est la valeur de `coffee.amount` ?

...

..

.

Elle est toujours `120`. Tout d'abord, nous étions à l'intérieur de l'objet `coffee`, puisque la méthode `drink` est déclarée à l'intérieur de celui-ci. Nous avons simplement fait `setTimeout` et rien d'autre. C'est exactement cela.

Comme je l'ai expliqué précédemment, la méthode `setTimeout` est en fait déclarée dans l'objet `window`. Lorsque nous l'appelons, nous changeons en fait de contexte pour revenir à `window`. Cela signifie que nos instructions ont en fait tenté de changer `window.amount`, mais elles n'ont rien fait à cause de l'instruction `if`. Pour remédier à cela, nous devons `bind` nos fonctions (voir ci-dessous).

#### React

En utilisant React, cela sera bientôt une chose du passé, grâce aux Hooks. Pour l'instant, nous devons toujours `bind` tout (plus d'informations à ce sujet plus tard) d'une manière ou d'une autre. Lorsque j'ai commencé, je n'avais aucune idée de pourquoi je le faisais, mais à ce stade, vous devriez déjà savoir pourquoi c'est nécessaire.

Examinons deux simples composants de classe React :

```js
// MAUVAIS EXEMPLE
import React from 'react'

class Child extends React.Component {
  render() {
    return <button onClick = {
      this.props.getCoffee
    } > Get some Coffee! < /button>
  }
}

class Parent extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      coffeeCount: 0,
    }
    // changer pour en faire un bon exemple – normalement nous ferions :
    // this._getCoffee = this._getCoffee.bind(this)
  }
  render() {
    return ( <
      React.Fragment >
      <
      Child getCoffee = {
        this._getCoffee
      }
      /> < /
      React.Fragment >
    )
  }

  _getCoffee() {
    this.setState({
      coffeeCount: this.state.coffeeCount + 1,
    })
  }
}
```

Lorsque nous cliquons maintenant sur le bouton rendu par le `Child`, nous recevrons une erreur. Pourquoi ? Parce que React a changé notre contexte lors de l'appel de la méthode `_getCoffee`.

Je suppose que React appelle la méthode de rendu de nos composants dans un autre contexte, via des classes d'assistance ou similaires (même si je devrais creuser plus profondément pour en être sûr). Par conséquent, `this.state` est indéfini et nous essayons d'accéder à `this.state.coffeeCount`. Vous devriez recevoir quelque chose comme `Cannot read property coffeeCount of undefined`.

Pour résoudre le problème, vous devez `bind` (nous y viendrons) les méthodes dans nos classes, dès que nous les passons en dehors du composant où elles sont définies.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nkgR5atcQtIeHQLeY8XMRQ.jpeg)
_Combien de cafés avez-vous bus jusqu'à présent ? / Photo par [Unsplash](https://unsplash.com/photos/7X96RNhpxBc?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Ozgu Ozden</a> sur <a href="https://unsplash.com/search/photos/coffee?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Examinons un autre exemple générique :

```js
// MAUVAIS EXEMPLE
class Viking {
  constructor(name) {
    this.name = name
  }

  prepareForBattle(increaseCount) {
    console.log(`I am ${this.name}! Let's go fighting!`)
    increaseCount()
  }
}

class Battle {
  constructor(vikings) {
    this.vikings = vikings
    this.preparedVikingsCount = 0

    this.vikings.forEach(viking => {
      viking.prepareForBattle(this.increaseCount)
    })
  }

  increaseCount() {
    this.preparedVikingsCount++
    console.log(`${this.preparedVikingsCount} vikings are now ready to fight!`)
  }
}

const vikingOne = new Viking('Olaf')
const vikingTwo = new Viking('Odin')

new Battle([vikingOne, vikingTwo])
```

Nous passons `increaseCount` d'une classe à une autre. Lorsque nous appelons la méthode `increaseCount` dans `Viking`, nous avons déjà changé de contexte et `this` pointe en fait vers `Viking`, ce qui signifie que notre méthode `increaseCount` ne fonctionnera pas comme prévu.

#### Solution — bind

La solution la plus simple pour nous est de `bind` les méthodes qui seront passées en dehors de notre objet ou classe d'origine. Il existe différentes manières de lier des fonctions, mais la plus courante (également dans React) est de les lier dans le constructeur. Nous devrions donc ajouter cette ligne dans le constructeur `Battle` avant la ligne 18 :

```js
this.increaseCount = this.increaseCount.bind(this)
```

Vous pouvez lier n'importe quelle fonction à n'importe quel contexte. Cela ne signifie pas que vous devez toujours lier la fonction au contexte dans lequel elle est déclarée (c'est le cas le plus courant, cependant). Au lieu de cela, vous pourriez la lier à un autre contexte. Avec `bind`, vous définissez toujours **le contexte pour une déclaration de fonction**. Cela signifie que tous les appels de cette fonction recevront le contexte lié en tant que `this`. Il existe deux autres aides pour définir le contexte.

> Les fonctions fléchées `() => {}` lient automatiquement la fonction au contexte de déclaration

![Image](https://cdn-media-1.freecodecamp.org/images/1*acg_8b0T63Aiv8TAbtn5_w.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/kMMY3V6IUrw?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Mario Klassen</a> sur <a href="https://unsplash.com/search/photos/pointing?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

#### Apply et call

Ils font tous les deux essentiellement la même chose, seule la syntaxe est différente. Pour les deux, vous passez le contexte en tant que premier argument. `apply` prend un tableau pour les autres arguments, avec `call` vous pouvez simplement séparer les autres arguments par une virgule. Maintenant, que font-ils ? Ces deux méthodes définissent le contexte pour **un appel de fonction spécifique**. Lorsque vous appelez la fonction sans `call`, le contexte est défini sur le contexte par défaut (ou même un contexte lié). Voici un exemple :

```js
class Salad {
  constructor(type) {
    this.type = type
  }
}

function showType() {
  console.log(`The context's type is ${this.type}`)
}

const fruitSalad = new Salad('fruit')
const greekSalad = new Salad('greek')

showType.call(fruitSalad) // The context's type is fruit
showType.call(greekSalad) // The context's type is greek

showType() // The context's type is undefined
```

Pouvez-vous deviner quel est le contexte du dernier appel `showType()` ?

...

..

.

Vous avez raison, c'est la portée la plus externe, `window`. Par conséquent, `type` est `undefined`, il n'y a pas de `window.type`.

C'est tout, j'espère que vous avez maintenant une compréhension claire de la façon d'utiliser `this` en JavaScript. N'hésitez pas à laisser des suggestions pour le prochain article dans les commentaires.

_À propos de l'auteur : Lukas Gisder-Dubé a cofondé et dirigé une startup en tant que CTO pendant 1 an et demi, construisant l'équipe technique et l'architecture. Après avoir quitté la startup, il a enseigné la programmation en tant que Lead Instructor chez [Ironhack](https://www.freecodecamp.org/news/how-to-understand-the-keyword-this-and-context-in-javascript-cd624c6b74b8/undefined) et construit maintenant une Agence & Consultance de Startup à Berlin. Consultez [dube.io](https://dube.io) pour en savoir plus._

![Image](https://cdn-media-1.freecodecamp.org/images/1*p-l0Cee1IHvX0RQkVTOceQ.png)