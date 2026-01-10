---
title: Prototypes JavaScript et héritage – et pourquoi ils disent que tout en JS est
  un objet
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2022-05-03T16:05:43.000Z'
originalURL: https://freecodecamp.org/news/prototypes-and-inheritance-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-maor-attias-5192478.jpg
tags:
- name: inheritance
  slug: inheritance
- name: JavaScript
  slug: javascript
- name: object
  slug: object
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Prototypes JavaScript et héritage – et pourquoi ils disent que tout en
  JS est un objet
seo_desc: 'Hi everyone! In this short article we''re going to talk about prototypal
  inheritance in JavaScript, and what are the implications of it.

  Table of Contents


  Intro


  How to access a prototype’s properties and methods in JavaScript


  The prototype chain


  A...'
---

Bonjour à tous ! Dans cet article court, nous allons parler de **l'héritage prototypal** en JavaScript, et quelles en sont les implications.

## Table des matières

* [Intro](#heading-intro)
    
* [Comment accéder aux propriétés et méthodes d'un prototype en JavaScript](#heading-comment-acceder-aux-proprietes-et-methodes-dun-prototype-en-javascript)
    
* [La chaîne de prototypes](#heading-la-chaine-de-prototypes)
    
* [Un langage basé sur les prototypes](#heading-un-langage-base-sur-les-prototypes)
    
* [Les classes JavaScript](#heading-les-classes-javascript)
    
* [Conclusion](#heading-conclusion)
    

# Intro

Vous êtes-vous déjà demandé comment les chaînes de caractères, les tableaux ou les objets « connaissent » les méthodes qui leur sont associées ? Comment une chaîne sait-elle qu'elle peut `.toUpperCase()` ou un tableau sait-il qu'il peut `.sort()` ? Nous n'avons jamais défini ces méthodes manuellement, n'est-ce pas ?

La réponse est que ces méthodes sont intégrées dans chaque type de structure de données grâce à ce qu'on appelle **l'héritage prototypal**.

En JavaScript, un objet peut hériter des propriétés d'un autre objet. L'objet à partir duquel les propriétés sont héritées est appelé le prototype. En bref, les objets peuvent hériter des propriétés d'autres objets — les prototypes.

Vous vous demandez probablement : pourquoi avoir besoin d'héritage en premier lieu ? Eh bien, l'héritage résout le problème de duplication des données et de la logique. En héritant, les objets peuvent partager des propriétés et des méthodes sans avoir besoin de définir manuellement ces propriétés et méthodes sur chaque objet.

## **Comment accéder aux propriétés et méthodes d'un prototype en JavaScript**

Lorsque nous essayons d'accéder à une propriété d'un objet, la propriété n'est pas seulement recherchée dans l'objet lui-même. Elle est également recherchée dans le prototype de l'objet, dans le prototype du prototype, et ainsi de suite — jusqu'à ce qu'une propriété correspondant au nom soit trouvée ou que la fin de la **chaîne de prototypes** soit atteinte.

Si la propriété ou la méthode n'est trouvée nulle part dans la chaîne de prototypes, ce n'est qu'alors que JavaScript retournera `undefined`.

Chaque objet en JavaScript possède une propriété interne appelée `[[Prototype]]`.

Si nous créons un tableau et l'affichons dans la console comme ceci :

```javascript
const arr = [1,2,3]
console.log(arr)
```

Nous verrons ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image.png align="left")

Les doubles crochets qui entourent `[[Prototype]]` signifient que c'est une propriété interne et qu'elle ne peut pas être accédée directement dans le code.

Pour trouver le `[[Prototype]]` d'un objet, nous utiliserons la méthode `Object.getPrototypeOf()`.

```javascript
const arr = [1,2,3]
console.log(Object.getPrototypeOf(arr))
```

La sortie consistera en plusieurs propriétés et méthodes intégrées :

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-1.png align="left")

Gardez à l'esprit que les prototypes peuvent également être modifiés et changés grâce à différentes méthodes.

## **La chaîne de prototypes**

À la fin de la chaîne de prototypes se trouve `Object.prototype`. Tous les objets héritent des propriétés et méthodes de `Object`. Toute tentative de recherche au-delà de la fin de la chaîne aboutit à `null`.

Si vous cherchez le prototype du prototype d'un tableau, d'une fonction ou d'une chaîne, vous verrez que c'est un objet. Et c'est parce qu'en JavaScript, tous les objets sont des descendants ou des instances de `Object.prototype`, qui est un objet définissant des propriétés et méthodes pour tous les autres types de données JavaScript.

```javascript
const arr = [1,2,3]
const arrProto = Object.getPrototypeOf(arr)
console.log(Object.getPrototypeOf(arrProto))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-2.png align="left")

Chaque type de prototype (par exemple, le prototype de tableau) définit ses propres méthodes et propriétés, et dans certains cas, remplace les méthodes et propriétés de `Object.prototype` (c'est pourquoi les tableaux ont des méthodes que les objets n'ont pas).

Mais sous le capot et en remontant l'échelle de la chaîne de prototypes, **tout en JavaScript est construit sur** `Object.prototype`.

Si nous essayons de regarder le prototype de `Object.prototype`, nous obtenons `null`.

```javascript
const arr = [1,2,3]
const arrProto = Object.getPrototypeOf(arr)
const objectProto = Object.getPrototypeOf(arrProto)
console.log(Object.getPrototypeOf(objectProto))
```

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-3.png align="left")

## **Un langage basé sur les prototypes**

JavaScript est un **langage basé sur les prototypes**, ce qui signifie que les propriétés et méthodes des objets peuvent être partagées via des objets généralisés capables d'être clonés et étendus.

En ce qui concerne l'héritage, JavaScript n'a qu'une seule structure : les objets.

Chaque objet possède une propriété privée (appelée `[[Prototype]]`) qui maintient un lien vers un autre objet appelé son prototype. Ce prototype a son propre prototype, et ainsi de suite jusqu'à ce qu'un objet dont le prototype est `null` soit atteint.

Par définition, `null` n'a pas de prototype et agit comme le dernier maillon de cette chaîne de prototypes.

Cela est connu sous le nom d'héritage prototypal et diffère de l'héritage de classe. Parmi les langages de programmation orientés objet populaires, JavaScript est relativement unique, car d'autres langages notables tels que PHP, Python et Java sont des langages basés sur les classes, qui définissent plutôt les classes comme des plans pour les objets.

À ce stade, vous pourriez penser "Mais nous pouvons implémenter des classes en JavaScript !". Et oui, nous le pouvons, mais comme du sucre syntaxique. 🤫😄

## Les classes JavaScript

Les classes sont un moyen de définir un plan pour créer des objets avec des propriétés et méthodes prédéfinies. En créant une classe avec des propriétés et méthodes spécifiques, vous pouvez ensuite instancier des objets à partir de cette classe, qui hériteront de toutes les propriétés et méthodes que cette classe possède.

En JavaScript, nous pouvons créer des classes de la manière suivante :

```javascript
class Alien {
    constructor (name, phrase) {
        this.name = name
        this.phrase = phrase
        this.species = "alien"
    }
    fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!")
    sayPhrase = () => console.log(this.phrase)
}
```

Et ensuite, nous pouvons instancier un objet à partir de cette classe comme ceci :

```javascript
const alien1 = new Alien("Ali", "I'm Ali the alien!")
console.log(alien1.name) // sortie : "Ali"
```

Les classes sont utilisées comme un moyen de rendre le code plus modulaire, organisé et compréhensible, et sont largement utilisées en programmation OOP.

Mais gardez à l'esprit que JavaScript ne supporte pas vraiment les classes comme d'autres langages. Le mot-clé `class` a été introduit avec ES6 comme sucre syntaxique qui facilite cette façon d'organiser le code.

Pour visualiser cela, voyez que la même chose que nous avons faite en définissant précédemment une `class`, nous pouvons la faire en définissant une fonction et en modifiant le prototype de la manière suivante :

```javascript
function Alien(name, phrase) {
    this.name = name
    this.phrase = phrase
    this.species = "alien"
}

Alien.prototype.fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!")
Alien.prototype.sayPhrase = () => console.log(this.phrase)

const alien1 = new Alien("Ali", "I'm Ali the alien!")

console.log(alien1.name) // sortie "Ali"
console.log(alien1.phrase) // sortie "I'm Ali the alien!"
alien1.fly() // sortie "Zzzzzziiiiiinnnnnggggg"
```

Toute fonction peut être invoquée comme constructeur avec le mot-clé `new` et la propriété prototype de cette fonction est utilisée pour que l'objet hérite des méthodes. En JavaScript, « class » n'est utilisé que conceptuellement pour décrire la pratique ci-dessus — techniquement, ce ne sont que des fonctions. 😱

Bien que cela ne fasse pas nécessairement une grande différence (nous pouvons toujours parfaitement implémenter l'OOP et utiliser des classes comme dans la plupart des autres langages de programmation), il est important de se rappeler que JavaScript est construit avec l'héritage prototypal au cœur de son fonctionnement.

# Conclusion

C'est tout, tout le monde ! Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/germancocca/) ou [Twitter](https://twitter.com/CoccaGerman).

À bientôt et à la prochaine ! =D

![Image](https://www.freecodecamp.org/news/content/images/2022/04/AntiqueAthleticGuineapig-size_restricted.gif align="left")