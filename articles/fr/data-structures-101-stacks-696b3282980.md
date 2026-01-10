---
title: 'Structures de données 101 : Les piles'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-06T14:23:39.000Z'
originalURL: https://freecodecamp.org/news/data-structures-101-stacks-696b3282980
coverImage: https://cdn-media-1.freecodecamp.org/images/0*NEPg2w2qm-aTdb1a
tags:
- name: coding
  slug: coding
- name: Computer Science
  slug: computer-science
- name: data structures
  slug: data-structures
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: 'Structures de données 101 : Les piles'
seo_desc: 'By Kevin Turney

  A Stack is the most elemental of the data structures in computer science.

  Data structures are a way to organize our information. They provide a means of storing
  different types of data in unique ways and methods to access either all o...'
---

Par Kevin Turney

### Une pile est la structure de données la plus élémentaire en informatique.

Les structures de données sont un moyen d'organiser nos informations. Elles fournissent un moyen de stocker différents types de données de manière unique et des méthodes pour accéder à tout ou partie de celles-ci.

### Commencer avec une pile

Avez-vous déjà utilisé une pile ? Bien sûr ! Votre email est une forme de pile, les nouveaux emails arrivent et sont placés sur le dessus. Lorsque vous avez fini de lire le dernier email, vous le retirez du dessus. En développement, chaque fois que vous appelez une fonction, celle-ci est placée sur une pile dans le moteur qui traite le code.

La manière dont nous utilisons les piles est un système de traitement **Last In, First Out** (dernier entré, premier sorti).

Une analogie serait une recette. Supposons que nous voulons faire un bol de spaghetti. Quelles sont les étapes ?

1. Prendre une casserole
2. Ajouter de l'eau
3. Porter l'eau à ébullition
4. Ajouter du sel à l'eau
5. Ajouter les spaghetti
6. Cuire les spaghetti jusqu'à ce qu'ils soient tendres

Maintenant que les spaghetti sont cuits, nous devons revenir à notre point de départ, une cuisine propre. Nous avons besoin d'une méthode pour organiser notre liste de tâches et nous aider à revenir là où nous nous sommes arrêtés.

JavaScript est un langage à thread unique. En termes simples, cela signifie qu'il ne peut faire qu'une seule chose à la fois, tout comme nous. Alors, comment notre langage de choix gère-t-il cela de manière organisée ? Avec des piles !

![Image](https://cdn-media-1.freecodecamp.org/images/K4D9kYqy74hwfMaEvoj6TMVAioUxmyUY5vfG)

Comme vous pouvez le voir, la pile est un moyen propre de gérer les tâches, de les supprimer et de revenir finalement au début.

Les piles ont un coût : la mémoire. Pour chaque élément que nous plaçons sur la pile, nous lui allouons un cadre de pile. Pensez à un index de tableau. Chaque index se voit allouer de l'espace pour contenir quelque chose. Si nous continuons à ajouter et à ajouter à une pile, nous risquons de manquer d'espace, comme un parking qui est plein. Lorsque cela se produit, nous avons un débordement, d'où le terme "débordement de pile". Cela peut entraîner des plantages et des processus bloqués.

![Image](https://cdn-media-1.freecodecamp.org/images/2oeYQbArqT5t5TfIjqkI5i86QjaFUynSqyY5)

Comment récupérons-nous la mémoire ? Lorsque un élément est retiré de la pile, JavaScript utilise la "collecte des déchets" pour libérer des ressources et récupérer l'espace de stockage précédemment utilisé.

### Implémentation

Tout d'abord, comment stockons-nous les données ? Que pouvons-nous utiliser en JavaScript pour contenir des données ? Nous pouvons utiliser des objets natifs comme les tableaux, avec lesquels nous sommes familiers et utiliser les méthodes intégrées, push et pop. Ok, je suppose que nous avons terminé, à plus tard...

Non, pour comprendre comment une pile fonctionne sous le capot, nous utilisons la forme de base de l'objet.

Nous avons besoin d'un constructeur pour établir le mécanisme de stockage et les propriétés lors de son invocation.

```
const Stack = function(capacity) {  this.storage = {};  this.capacity = capacity || Infinity;  this._count = 0;}
```

Cela constitue un mécanisme de stockage de pile. Comment pouvons-nous pousser des données dans la pile de manière LIFO ? Ajoutez push au prototype de Stack.

```
Stack.prototype.push = function(value) {  if (this._count < this._capacity){    this.storage[this._count++] = value;    return this._count;  }  return "Capacité maximale atteinte, veuillez retirer une valeur avant d'en insérer une nouvelle";}
```

La méthode push vérifie notre capacité. Si vrai, nous ajoutons la valeur au stockage et retournons combien d'éléments sont dans la pile.

[this._count++] est d'abord évalué à 0, et nous utilisons l'opérateur postfix, ++ pour incrémenter le compte. Notre pile a une valeur à this.storage['0'], et nous retournons 1 parce que nous avons un élément dans notre pile.

Retirons des éléments ou 'pop' les de la pile.

```
Stack.prototype.pop = function() {  let value = this.storage[--this._count];  delete this.storage[this._count];  if (this._count < 0) {    this._count = 0;  }  return value;}
```

Avec pop, nous stockons la dernière valeur de la pile. Si nous la retirons d'abord, nous ne l'aurons pas comme valeur de retour. Grâce à l'opérateur préfixe, --, nous trouvons la valeur de this.count et la décrémentons d'abord avant de l'évaluer. Si nous avons this.count === 1, this.storage[--this.count] est évalué comme this.storage['0'].

Qu'en est-il de voir ce qu'il y a au sommet de la pile ? L'interface pour cela est 'peek'.

```
Stack.prototype.peek = function() {  return this.storage[this._count -1]}
```

Enfin, count...

```
Stack.prototype.count = function(){  return this._count;}
```

L'implémentation complète en style ES6 avec la classe Stack :

```
class Stack {  constructor(capacity) {    this.storage = {};    this._count = 0;    this.capacity = capacity || Infinity;  }
```

```
  push(value) {    if (this._count < this.capacity){    this.storage[this._count++] = value;    return this._count;    }    return "Capacité maximale atteinte, veuillez retirer une valeur avant d'en insérer une nouvelle";  }
```

```
  pop() {    let value = this.storage[--this._count];    delete this.storage[this._count];    if (this._count < 0) {      this._count = 0;    }    return value;  }  peek() {    return this.storage[this._count - 1];  }  count() {    return this._count;  }};let stack = new Stack();stack; // Stack { storage: {}, _count: 0, capacity: Infinity }stack.push('yea')stack.push('oh yea');
```

```
stack; // Stack {storage: { 0: 'yea', 1: 'oh yea' },  _count: 2,  capacity: Infinity }
```

```
stack.pop(); // 'oh yea'stack; // Stack { storage: { 0: 'yea' }, _count: 1, capacity: Infinity }
```

```
stack.push('nope');stack.push('yup');stack; // Stack {storage: { 0: 'yea', 1: 'nope', 2: 'yup' },  _count: 3,  capacity: Infinity }
```

```
stack.count(); // 3stack.peek(); // 'yup'stack; // Stack {storage: { 0: 'yea', 1: 'nope', 2: 'yup' },  _count: 3,  capacity: Infinity }
```

Merci d'avoir lu cet article. Mon objectif était de donner une explication claire et sans encombrement des piles, de leur utilisation et de pourquoi nous en avons besoin. [Prochainement : Les files d'attente](https://medium.freecodecamp.org/data-structures-101-queues-a6960a3c98).