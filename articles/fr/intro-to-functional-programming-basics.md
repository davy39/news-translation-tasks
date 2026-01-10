---
title: Introduction aux bases de la programmation fonctionnelle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-17T23:52:00.000Z'
originalURL: https://freecodecamp.org/news/intro-to-functional-programming-basics
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c89740569d1a4ca32c7.jpg
tags:
- name: Functional Programming
  slug: functional-programming
- name: toothbrush
  slug: toothbrush
seo_title: Introduction aux bases de la programmation fonctionnelle
seo_desc: 'Functional Programming

  Functional programming is the process of building software by composing pure functions,
  avoiding shared state, mutable data, and side-effects. Functional programming is
  declarative (telling the computer what you want to do) rat...'
---

## **Programmation fonctionnelle**

La programmation fonctionnelle est le processus de construction de logiciels en composant des **fonctions pures**, en évitant l'**état partagé**, les **données mutables** et les **effets de bord**. La programmation fonctionnelle est **déclarative** (dire à l'ordinateur ce que vous voulez faire) plutôt qu'**impérative** (dire à l'ordinateur exactement comment faire cela), et l'état de l'application circule à travers des fonctions pures. Contrastons cela avec la programmation orientée objet, où l'état de l'application est généralement partagé et co-localisé avec les méthodes dans les objets.

### **Pourquoi la programmation fonctionnelle ?**

* Elle est généralement plus concise
* Elle est généralement plus prévisible
* Elle est plus facile à tester que le code orienté objet

### **Adoption par les langages de programmation**

De nombreux langages de programmation supportent la programmation fonctionnelle comme Haskell, F#, Common Lisp, Clojure, Erlang, OCaml. JavaScript possède également les propriétés d'un langage fonctionnel non typé.

### **Utilisations**

La programmation fonctionnelle est depuis longtemps populaire dans le milieu académique, mais avec peu d'applications industrielles. Cependant, récemment, plusieurs langages de programmation fonctionnelle importants ont été utilisés dans des systèmes commerciaux ou industriels. Par exemple, le langage de programmation Erlang, qui a été développé par l'entreprise suédoise Ericsson à la fin des années 1980, est utilisé pour construire une gamme d'applications dans des entreprises telles que T-Mobile, Nortel, Facebook, Électricité de France et WhatsApp.

### **Fonctions d'ordre supérieur**

Les fonctions d'ordre supérieur sont une grande partie de la programmation fonctionnelle. Une fonction d'ordre supérieur est une fonction qui prend une ou plusieurs fonctions comme paramètre ou qui retourne une fonction.

### **Map**

`map` est une fonction d'ordre supérieur qui appelle une fonction pour chaque élément d'une liste et retourne les résultats sous forme de _nouvelle_ liste.

Voici un exemple de `map` :

```javascript
const myList = [6, 3, 5, 29];

let squares = myList.map(num => num * num); // [36, 9, 25, 841]
```

### **Plus d'informations sur la programmation fonctionnelle :**

* [Apprendre la programmation fonctionnelle en Java - cours complet (vidéo)](https://www.freecodecamp.org/news/functional-programming-in-java-course/)
* [Comment apprendre la programmation fonctionnelle peut faire de vous un meilleur développeur](https://www.freecodecamp.org/news/learn-the-fundamentals-of-functional-programming/)
* [Comment utiliser la programmation fonctionnelle dans le JavaScript moderne](https://www.freecodecamp.org/news/how-and-why-to-use-functional-programming-in-modern-javascript-fda2df86ad1b/)