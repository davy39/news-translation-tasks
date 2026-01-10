---
title: Une introduction rapide aux Proxies JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-04T19:48:23.000Z'
originalURL: https://freecodecamp.org/news/a-quick-intro-to-javascript-proxies-55695ddc4f98
coverImage: https://cdn-media-1.freecodecamp.org/images/1*angpGt6Kog97_mI5sbi7Hg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Une introduction rapide aux Proxies JavaScript
seo_desc: 'By Chuks Opia

  What is a JavaScript proxy? you might ask. It is one of the features that shipped
  with ES6. Sadly, it seems not to be widely used.

  According to the MDN Web Docs:


  The Proxy object is used to define custom behavior for fundamental operat...'
---

Par Chuks Opia

Qu'est-ce qu'un proxy JavaScript ? vous pourriez demander. C'est l'une des fonctionnalités qui ont été introduites avec ES6. Malheureusement, il semble qu'elle ne soit pas largement utilisée.

Selon les [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) :

> L'objet **Proxy** est utilisé pour définir un comportement personnalisé pour les opérations fondamentales (par exemple, la recherche de propriété, l'assignation, l'énumération, l'invocation de fonction, etc.).

En termes simples, les proxies sont des **getters** et des **setters** avec beaucoup de style. Un objet proxy se place entre un objet et le monde extérieur. Ils interceptent les appels aux attributs et méthodes d'un objet même si ces attributs et méthodes n'existent pas.

Pour comprendre comment fonctionnent les proxies, nous devons définir trois termes utilisés par les proxies :

1. **handler** : L'objet placeholder qui contient les traps (ce sont les interceptors).
2. **traps** : Les méthodes qui fournissent l'accès aux propriétés (elles vivent à l'intérieur du handler).
3. **target** : L'objet que le proxy virtualise.

#### Syntaxe

```js
let myProxy = new Proxy(target, handler);
```

### Pourquoi utiliser les proxies ?

Puisque les proxies sont similaires aux **getters** et **setters**, pourquoi devrions-nous les utiliser ? Voyons pourquoi :

```js
const staff = {
  _name: "Jane Doe",
  _age: 25,
  get name() {
    console.log(this._name);
  },
  get age() {
    console.log(this._age);
  },
  set age(newAge) {
    this._age = newAge;
    console.log(this._age)
  }
};
staff.name // => "Jane Doe"
staff.age // => 25
staff.age = 30
staff.age // => 30
staff.position // => undefined
```

Écrivons le même code avec des proxies :

```js
const staff = {
  name: "Jane Doe",
  age: 25
}
const handler = {
  get: (target, name) => {
    name in target ? console.log(target[name]) : console.log('404 not found');
  },
  set: (target, name, value) => {
    target[name] = value;
  }
}
const staffProxy = new Proxy(staff, handler);
staffProxy.name // => "Jane Doe"
staffProxy.age // => 25
staffProxy.age = 30
staffProxy.age // => 30
staffProxy.position // => '404 not found'
```

Dans l'exemple ci-dessus utilisant des **getters** et **setters**, nous devons définir un **getter** et un **setter** pour chaque attribut dans l'objet `staff`. Lorsque nous essayons d'accéder à une propriété inexistante, nous obtenons `undefined`.

Avec les proxies, nous n'avons besoin que d'un seul `get` et `set` trap pour gérer les interactions avec chaque propriété de l'objet `staff`. Chaque fois que nous essayons d'accéder à une propriété inexistante, nous obtenons un message d'erreur personnalisé.

Il existe de nombreux autres cas d'utilisation pour les proxies. Explorons-en quelques-uns :

### Validation avec les proxies

Avec les proxies, nous pouvons imposer des validations de valeurs dans les objets JavaScript. Supposons que nous avons un schéma `staff` et que nous souhaitons effectuer certaines validations avant qu'un membre du personnel puisse être enregistré :

```js
const validator = {
  set: (target, key, value) => {
    const allowedProperties = ['name', 'age', 'position'];
    if (!allowedProperties.includes(key)) {
      throw new Error(`${key} is not a valid property`)
    }
    
    if (key === 'age') {
      if (typeof value !== 'number' || Number.isNaN(value) || value <= 0) {
        throw new TypeError('Age must be a positive number')
      }
    }
    if (key === 'name' || key === 'position') {
      if (typeof value !== 'string' || value.length <= 0) {
        throw new TypeError(`${key} must be a valid string`)
      }
    }
   target[key] = value; // sauvegarder la valeur
   return true; // indiquer le succès
  }
}
const staff = new Proxy({}, validator);
staff.stats = "malicious code" //=> Uncaught Error: stats is not a valid property
staff.age = 0 //=> Uncaught TypeError: Age must be a positive number
staff.age = 10
staff.age //=> 10
staff.name = '' //=> Uncaught TypeError: name must be a valid string
```

Dans l'extrait de code ci-dessus, nous déclarons un handler `validator` où nous avons un tableau de `allowedProperties`. Dans le `set` trap, nous vérifions si la clé en cours de définition fait partie de nos `allowedProperties`. Si ce n'est pas le cas, nous lançons une erreur. Nous vérifions également si les valeurs en cours de définition sont de certains types de données avant de sauvegarder la valeur.

### Proxies révocables

Et si nous voulions révoquer l'accès à un objet ? Eh bien, les proxies JavaScript ont une méthode `Proxy.revocable()` qui crée un proxy révocable. Cela nous donne la possibilité de révoquer l'accès à un proxy. Voyons comment cela fonctionne :

```js
const handler = {
  get: (target, name) => {
    name in target ? console.log(target[name]) : console.log('404 not found');
    console.log(target)
  },
  
  set: (target, name, value) => {
    target[name] = value;
  }
}
const staff = {
  name: "Jane Doe",
  age: 25
}
let { proxy, revoke } = Proxy.revocable(staff, handler);
proxy.age // => 25
proxy.name // => "Jane Doe"
proxy.age = 30
proxy.age // => 30
revoke() // révoquer l'accès au proxy
proxy.age // => Uncaught TypeError: Cannot perform 'get' on a proxy that has been revoked
proxy.age = 30 // => Uncaught TypeError: Cannot perform 'set' on a proxy that has been revoked
```

Dans l'exemple ci-dessus, nous utilisons la déstructuration pour accéder aux propriétés `proxy` et `revoke` de l'objet retourné par `Proxy.revocable()`.

Après avoir appelé la fonction `revoke`, toute opération appliquée à `proxy` provoque une `TypeError`. Avec cela dans notre code, nous pouvons empêcher les utilisateurs d'effectuer certaines actions sur certains objets.

Les proxies JavaScript sont un moyen puissant de créer et de gérer les interactions entre les objets. D'autres applications réelles pour les Proxies incluent :

* Étendre les constructeurs
* Manipuler les nœuds DOM
* Correction de valeur et propriété supplémentaire
* Tracer les accès aux propriétés
* Intercepter les appels de fonction

Et la liste continue.

Il y a plus à savoir sur les proxies que ce que nous avons couvert ici. Vous pouvez consulter la [documentation MDN sur Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) pour découvrir tous les traps disponibles et comment les utiliser.

J'espère que vous avez trouvé ce tutoriel utile. N'hésitez pas à le partager afin que d'autres puissent trouver cet article. Contactez-moi sur Twitter @d[evelopia_](https://twitter.com/developia_) pour des questions ou pour discuter.