---
title: Apprenons à connaître Set et ses fonctionnalités uniques en JavaScript ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-17T16:29:45.000Z'
originalURL: https://freecodecamp.org/news/lets-learn-about-set-and-its-unique-functionality-in-javascript-5654c5c03de2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WHhLDFPAo2DnMjPoSXV3sw.png
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Apprenons à connaître Set et ses fonctionnalités uniques en JavaScript
  ?
seo_desc: 'By Asif Norzai

  SET ?

  ES2015/ES6 gave us a lot of useful tools and features, but one that stands out the
  most for me is Set. It’s not used to its full potential. I hope to convince you
  of its worth with this article, so that you can reap the full bene...'
---

Par Asif Norzai

### SET ?

ES2015/ES6 nous a apporté de nombreux outils et fonctionnalités utiles, mais l'un de ceux qui se démarque le plus pour moi est Set. Il n'est pas utilisé à son plein potentiel. J'espère vous convaincre de sa valeur avec cet article, afin que vous puissiez tirer pleinement parti de cette belle utilité.

#### Alors, qu'est-ce que Set, demandez-vous ?

> « L'objet **Set** vous permet de stocker des valeurs uniques de n'importe quel type, qu'il s'agisse de [valeurs primitives](https://developer.mozilla.org/en-US/docs/Glossary/Primitive) ou de références d'objets. », [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set).

Set supprime les entrées en double.

#### **Fonctionnalité de base** ?

Chaque fois que vous souhaitez utiliser `Set`, vous devez l'initialiser en utilisant le mot-clé `new` et passer une donnée [itérable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#The_iterable_protocol) initiale, la laisser vide ou `null`.

```js
// Toutes les façons valides d'initialiser un set
const newSet1 = new Set();
const newSet2 = new Set(null);
const newSet3 = new Set([1, 2, 3, 4, 5]);
```

### **Utilitaires/méthodes de Set** ?

`**add**`, comme son nom l'indique, ajoute de nouvelles entrées à la constante Set nouvellement initialisée. Si à un moment donné une valeur en double est ajoutée au set, elle sera rejetée en utilisant `l'égalité stricte`.

```js
const newSet = new Set();

newSet.add("C");
newSet.add(1);
newSet.add("C");

// fonctionnalité d'ajout en chaîne
newSet.add("H").add("C");

newSet.forEach(el => {
  console.log(el);
  // sortie attendue: C
  // sortie attendue: 1
  // sortie attendue: H
});
```

`**has**` vérifie si la valeur que vous passez existe dans la constante `newSet`. Si la valeur existe, elle retournera le booléen `true`, et elle retournera `false` si elle n'existe pas.

```js
const newSet = new Set(["A", 2, "B", 4, "C"]);

console.log(newSet.has("A"));
// sortie attendue: true

console.log(newSet.has(4));
// sortie attendue: true

console.log(newSet.has(5));
// sortie attendue: false
```

`**clear**` et `**delete**` sont deux des fonctionnalités les plus importantes de `Set` si vous souhaitez soit supprimer toutes les entrées, soit supprimer une valeur spécifique.

```js
const newSet = new Set(["A", 2, "B", 4, "C"]);

newSet.delete("C");
// sortie attendue: true

newSet.delete("C");
// sortie attendue: false

newSet.size
// sortie attendue: 4

newSet.clear();
// sortie attendue: undefined

newSet.size
// sortie attendue: 0
```

`**keys**` et `values` ont la même fonctionnalité, ce qui est étrange si vous pensez à leur comportement avec les objets JS. Ils retournent tous les deux un objet `iterator`. Cela signifie que vous pouvez accéder à la méthode `.next()` pour obtenir sa valeur.

```js
const newSet = new Set(null);

newSet.add("Apples");
newSet.add(12);

let iterator = newSet.keys();  // même chose que newSet.values();

console.log(iterator.next().value);
// sortie attendue: Apples

console.log(iterator.next().value);
// sortie attendue: 12

console.log(iterator.next().value);
// sortie attendue: undefined
```

### **Mettons tout ensemble**

Créons une fonction simple pour une fête de hackers. La fonction ajoute des utilisateurs à la liste uniquement s'ils ont l'approbation d'un administrateur. Vous devez donc avoir le nom d'un administrateur avec votre entrée, qui est secrète (pas dans cet article, cependant). À la fin du programme, il dira qui est invité.

```js
// Les administrateurs
const allowedAdminUsers = new Set(["Naimat", "Ismat", "Azad"]);

// Un Set vide, stocké en mémoire
const finalList = new Set();

// Une fonction pour ajouter des utilisateurs à la liste de permissions
const addUsers = ({user, admin}) => {
  
   // Vérifier si l'administrateur est dans la liste des administrateurs
   // et que l'utilisateur n'est pas déjà dans le set
  if(allowedAdminUsers.has(admin) && !finalList.has(user)) {
    
    // Retourner la liste des utilisateurs à la fin
   return finalList.add(user);
    
  }
  // Afficher ce message si la condition n'est pas remplie
  console.log(`user ${user} est déjà dans la liste ou n'est pas autorisé`); 
};

// Ajouter quelques entrées
addUsers({user: "Asep", admin: "Naimat"});
addUsers({user: "John", admin: "Ismat"});

// Ajoutons John à nouveau et cette fois, la fonction interne affichera une erreur
addUsers({user: "John", admin: "Azad"});

const inviationList = [...finalList].map(user => 
 `${user} est invité`);

console.log(inviationList);
// Sortie attendue:  ["Asep est invité", "John est invité"]
```

Cela suffit pour utiliser Set aujourd'hui dans nos projets. ?

![Image](https://cdn-media-1.freecodecamp.org/images/9HUfTsuNCDKzpF6NJsItRYlX-68khdXAb9hk)

**Avant de partir** : si vous avez aimé cet article, suivez-moi ici et aussi sur [Twitter](https://twitter.com/asepnorzai), où je publie et retweete du contenu lié au web.