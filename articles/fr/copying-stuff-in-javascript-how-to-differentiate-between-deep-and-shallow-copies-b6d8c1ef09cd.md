---
title: Comment différencier les copies profondes et superficielles en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-18T10:20:41.000Z'
originalURL: https://freecodecamp.org/news/copying-stuff-in-javascript-how-to-differentiate-between-deep-and-shallow-copies-b6d8c1ef09cd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CZaCLmeCWGIhvuhKnV7mVg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment différencier les copies profondes et superficielles en JavaScript
seo_desc: 'By Lukas Gisder-Dubé

  New is always better!

  You have most certainly dealt with copies in JavaScript before, even if you didn’t
  know it. Maybe you have also heard of the paradigm in functional programming that
  you shouldn’t modify any existing data. In...'
---

Par Lukas Gisder-Dubé

Nouveau est toujours mieux !

Vous avez certainement déjà traité des copies en JavaScript, même sans le savoir. Peut-être avez-vous également entendu parler du paradigme en programmation fonctionnelle selon lequel vous ne devriez modifier aucune donnée existante. Pour cela, vous devez savoir comment copier des valeurs en JavaScript de manière sûre. Aujourd'hui, nous allons voir comment faire cela tout en évitant les pièges !

Tout d'abord, qu'est-ce qu'une copie ?

Une copie ressemble simplement à l'original, mais ne l'est pas. Lorsque vous modifiez la copie, vous vous attendez à ce que l'original reste le même, tandis que la copie change.

En programmation, nous stockons des valeurs dans des variables. Faire une copie signifie que vous initialisez une nouvelle variable avec la ou les mêmes valeurs. Cependant, il y a un grand piège potentiel à considérer : la **copie profonde** vs. la **copie superficielle**. Une copie profonde signifie que toutes les valeurs de la nouvelle variable sont copiées et **déconnectées de la variable originale**. Une copie superficielle signifie que certaines (sous-)valeurs sont **toujours connectées** à la variable originale.

> Pour vraiment comprendre la copie, vous devez vous pencher sur la manière dont JavaScript stocke les valeurs.

#### Types de données primitifs

Les types de données primitifs incluent les suivants :

* Number — par exemple `1`
  
* String — par exemple `'Hello'`
  
* Boolean — par exemple `true`
  
* `undefined`
  
* `null`
  
Lorsque vous créez ces valeurs, elles sont étroitement couplées avec la variable à laquelle elles sont assignées. Elles n'existent qu'une seule fois. Cela signifie que vous n'avez pas vraiment à vous soucier de copier des types de données primitifs en JavaScript. Lorsque vous faites une copie, ce sera une vraie copie. Voyons un exemple :

```javascript
const a = 5
let b = a // ceci est la copie
b = 6

console.log(b) // 6
console.log(a) // 5
```

En exécutant `b = a`, vous faites la copie. Maintenant, lorsque vous réassignez une nouvelle valeur à `b`, la valeur de `b` change, mais pas celle de `a`.

#### Types de données composites — Objets et Tableaux

Techniquement, les tableaux sont aussi des objets, donc ils se comportent de la même manière. Je vais passer en revue les deux en détail plus tard.

Ici, cela devient plus intéressant. Ces valeurs sont en réalité stockées une seule fois lorsqu'elles sont instanciées, et assigner une variable crée simplement **un pointeur (référence) vers cette valeur**.

Maintenant, si nous faisons une copie `b = a`, et que nous changeons une valeur imbriquée dans `b`, cela change en réalité aussi la valeur imbriquée de `a`, puisque `a` et `b` pointent en réalité vers la même chose. Exemple :

```javascript
const a = {
  en: 'Hello',
  de: 'Hallo',
  es: 'Hola',
  pt: 'Olà'
}

let b = a
b.pt = 'Oi'

console.log(b.pt) // Oi
console.log(a.pt) // Oi
```

Dans l'exemple ci-dessus, nous avons en réalité fait une **copie superficielle**. Cela pose souvent problème, car nous nous attendons à ce que l'ancienne variable conserve les valeurs originales, et non les valeurs modifiées. Lorsque nous y accédons, nous obtenons parfois une erreur. Il peut arriver que vous essayiez de la déboguer pendant un certain temps avant de trouver l'erreur, car beaucoup de développeurs ne comprennent pas vraiment le concept et ne s'attendent pas à ce que ce soit l'erreur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*niSsr1dxva2RWXrvHT8hxg.jpeg align="left")

*Photo par* [*Thomas Millot*](https://unsplash.com/photos/7ocA9xwN3yQ) *sur* [*Unsplash*](https://unsplash.com/s/photos/fungi)

Examinons comment nous pouvons faire des copies d'objets et de tableaux.

### Objets

Il existe plusieurs façons de faire des copies d'objets, surtout avec la nouvelle spécification JavaScript en expansion et en amélioration.

#### Opérateur de décomposition

Introduit avec ES2015, cet opérateur est simplement génial, car il est si court et simple. Il 'décompose' toutes les valeurs dans un nouvel objet. Vous pouvez l'utiliser comme suit :

```javascript
const a = {
  en: 'Bye',
  de: 'Tschüss'
}

let b = {...a}
b.de = 'Ciao'

console.log(b.de) // Ciao
console.log(a.de) // Tschüss
```

Vous pouvez également l'utiliser pour fusionner deux objets ensemble, par exemple `const c = {...a, ...b}`.

#### Object.assign

Cela était principalement utilisé avant que l'opérateur de décomposition n'existe, et il fait essentiellement la même chose. Vous devez cependant être prudent, car le premier argument de la méthode `Object.assign()` est en réalité modifié et retourné. Assurez-vous donc de passer l'objet à copier au moins comme deuxième argument. Normalement, vous passeriez simplement un objet vide comme premier argument pour éviter de modifier des données existantes.

```javascript
const a = {
  en: 'Bye',
  de: 'Tschüss'
}

let b = Object.assign({}, a)
b.de = 'Ciao'

console.log(b.de) // Ciao
console.log(a.de) // Tschüss
```

#### Piège : Objets imbriqués

Comme mentionné précédemment, il y a un grand piège lors de la copie d'objets, qui s'applique aux deux méthodes listées ci-dessus. Lorsque vous avez un objet imbriqué (ou un tableau) et que vous le copiez, les objets imbriqués à l'intérieur de cet objet ne seront pas copiés, car ils ne sont que des pointeurs/références. Par conséquent, si vous modifiez l'objet imbriqué, vous le modifierez pour les deux instances, ce qui signifie que vous finirez par faire une **copie superficielle à nouveau**. Exemple :// MAUVAIS EXEMPLE

```javascript
const a = {
  foods: {
    dinner: 'Pasta'
  }
}

let b = {...a}
b.foods.dinner = 'Soup' // change pour les deux objets

console.log(b.foods.dinner) // Soup
console.log(a.foods.dinner) // Soup
```

Pour faire une **copie profonde d'objets imbriqués**, vous devriez considérer cela. Une façon de l'éviter est de copier manuellement tous les objets imbriqués :

```javascript
const a = {
  foods: {
    dinner: 'Pasta'
  }
}

let b = {foods: {...a.foods}}
b.foods.dinner = 'Soup'

console.log(b.foods.dinner) // Soup
console.log(a.foods.dinner) // Pasta
```

Au cas où vous vous demanderiez quoi faire lorsque l'objet a plus de clés que seulement `foods`, vous pouvez utiliser tout le potentiel de l'opérateur de décomposition. Lorsque vous passez plus de propriétés après le `...spread`, elles écrasent les valeurs originales, par exemple `const b = {...a, foods: {...a.foods}}`.

#### Faire des copies profondes sans réfléchir

Que faire si vous ne savez pas à quel point les structures imbriquées sont profondes ? Il peut être très fastidieux de parcourir manuellement de grands objets et de copier chaque objet imbriqué à la main. Il existe un moyen de copier tout sans réfléchir. Vous `stringifiez` simplement votre objet et le `parsez` immédiatement après :

```javascript
const a = {
  foods: {
    dinner: 'Pasta'
  }
}

let b = JSON.parse(JSON.stringify(a))
b.foods.dinner = 'Soup'

console.log(b.foods.dinner) // Soup
console.log(a.foods.dinner) // Pasta
```

Ici, vous devez considérer que vous ne pourrez pas copier les instances de classes personnalisées, donc vous ne pouvez l'utiliser que lorsque vous copiez des objets avec des **valeurs JavaScript natives** à l'intérieur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hepu5hNOaAqnhE60z-oicA.jpeg align="left")

*Photo par* [*Robert Zunikoff*](https://unsplash.com/photos/close-up-photo-of-goosebumps-slappy-the-dummy-ventriloquist-doll-j0vIeF69Jgc) *sur* [*Unsplash*](https://unsplash.com/s/photos/dolls)

### Tableaux

Copier des tableaux est aussi courant que copier des objets. Beaucoup de la logique derrière cela est similaire, puisque les tableaux sont aussi simplement des objets sous le capot.

#### Opérateur de décomposition

Comme avec les objets, vous pouvez utiliser l'opérateur de décomposition pour copier un tableau :

```javascript
const a = [1,2,3]
let b = [...a]
b[1] = 4

console.log(b[1]) // 4
console.log(a[1]) // 2
```

#### Fonctions de tableau — map, filter, reduce

Ces méthodes retourneront un nouveau tableau avec toutes (ou certaines) valeurs de l'original. En faisant cela, vous pouvez également modifier les valeurs, ce qui est très pratique :

```javascript
const a = [1,2,3]
let b = a.map(el => el)
b[1] = 4

console.log(b[1]) // 4
console.log(a[1]) // 2
```

Alternativement, vous pouvez changer l'élément souhaité tout en copiant :

```javascript
const a = [1,2,3]
const b = a.map((el, index) => index === 1 ? 4 : el)

console.log(b[1]) // 4
console.log(a[1]) // 2
```

#### Array.slice

Cette méthode est normalement utilisée pour retourner un sous-ensemble des éléments, commençant à un index spécifique et se terminant optionnellement à un index spécifique du tableau original. En utilisant `array.slice()` ou `array.slice(0)`, vous obtiendrez une copie du tableau original.

```javascript
const a = [1,2,3]
let b = a.slice(0)
b[1] = 4

console.log(b[1]) // 4
console.log(a[1]) // 2
```

#### Tableaux imbriqués

Similaire aux objets, l'utilisation des méthodes ci-dessus pour copier un tableau avec un autre tableau ou objet à l'intérieur générera une **copie superficielle**. Pour éviter cela, utilisez également `JSON.parse(JSON.stringify(someArray))`.

#### BONUS : copier une instance de classes personnalisées

Lorsque vous êtes déjà un pro en JavaScript et que vous traitez avec vos fonctions constructrices ou classes personnalisées, peut-être souhaitez-vous copier des instances de celles-ci également.

Comme mentionné précédemment, vous ne pouvez pas simplement stringifier + parser celles-ci, car vous perdrez vos méthodes de classe. Au lieu de cela, vous voudrez ajouter une méthode `copy` personnalisée pour créer une nouvelle instance avec toutes les anciennes valeurs. Voyons comment cela fonctionne :

```javascript
class Counter {
  constructor() {
     this.count = 5
  }
  copy() {
    const copy = new Counter()
    copy.count = this.count
    return copy
  }
}

const originalCounter = new Counter()
const copiedCounter = originalCounter.copy()

console.log(originalCounter.count) // 5
console.log(copiedCounter.count) // 5

copiedCounter.count = 7

console.log(originalCounter.count) // 5
console.log(copiedCounter.count) // 7
```

Pour traiter les objets et tableaux qui sont référencés à l'intérieur de votre instance, vous devrez appliquer vos nouvelles compétences sur la **copie profonde** ! Je vais simplement ajouter une solution finale pour la méthode `copy` du constructeur personnalisé pour la rendre plus dynamique :

```javascript
class Counter {
  constructor() {
    this.count = 5

    this.add = function() {
      this.count++
    }
  }

  copy() {
    const copy = new Counter()

    Object.keys(this).forEach(key => {
      const value = this[key]

      switch(typeof value) {
        case 'function':
          break
        case 'object':
          copy[key] = JSON.stringify(JSON.parse(value))
          break
        default:
          copy[key] = value
          break
      }
    })
    
    return copy
  }
}
```

Avec cette méthode de copie, vous pouvez mettre autant de valeurs que vous le souhaitez dans votre constructeur, sans avoir à tout copier manuellement !

*À propos de l'auteur : Lukas Gisder-Dubé a cofondé et dirigé une startup en tant que CTO pendant 1 an et demi, construisant l'équipe technique et l'architecture. Après avoir quitté la startup, il a enseigné la programmation en tant que Lead Instructor chez* [*Ironhack*](https://www.freecodecamp.org/news/copying-stuff-in-javascript-how-to-differentiate-between-deep-and-shallow-copies-b6d8c1ef09cd/undefined) *et construit maintenant une Agence & Consultance de Startup à Berlin. Consultez* [*dube.io*](https://dube.io) *pour en savoir plus.*

![Image](https://cdn-media-1.freecodecamp.org/images/1*p-l0Cee1IHvX0RQkVTOceQ.png align="left")