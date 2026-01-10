---
title: Explication des tests unitaires
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-07T22:38:00.000Z'
originalURL: https://freecodecamp.org/news/unit-tests-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cb3740569d1a4ca33b2.jpg
tags:
- name: toothbrush
  slug: toothbrush
- name: unit testing
  slug: unit-testing
seo_title: Explication des tests unitaires
seo_desc: "Unit testing is a type of testing which is found at the bottom of the software\
  \ testing pyramid. It involves breaking the codebase down into smaller parts (or\
  \ units) and testing those in isolation. \nDepending on the type of programming\
  \ language (or pa..."
---

Les tests unitaires sont un type de test qui se trouve au bas de la pyramide des tests logiciels. Cela implique de diviser la base de code en parties plus petites (ou unités) et de tester celles-ci en isolation. 

Selon le type de langage de programmation (ou paradigme), ceux-ci peuvent être contre tout ce que vous définissez comme une unité, bien que la pratique la plus courante soit contre les fonctions.

### **Pourquoi le faire ?**

* **Protection** - Les tests unitaires protègent contre l'introduction de nouveaux ou anciens bugs pour la programmation défensive
* **Confiance** - Vous pouvez ajouter des changements, ou réutiliser ou refactoriser du code (les deux très courants) et être sûr de ne pas avoir ajouté de bug
* **Documentation** - Les tests unitaires documentent le comportement et le flux de code afin qu'il soit facile pour quelqu'un de nouveau dans le code de le comprendre
* **Isolation** - Il isole un module de la fonctionnalité entière. Cette approche vous force à penser à un module par lui-même, et à demander quel est son travail ?
* **Qualité** - Comme les tests unitaires vous obligent à penser et à utiliser votre propre API, ils imposent de bonnes interfaces/patterns extensibles. Ils peuvent pointer toute dépendance serrée ou sur-complexité qui devrait être adressée. Le mauvais code est généralement beaucoup plus difficile à tester
* **Norme de l'industrie** - Les tests unitaires sont une discipline courante ces jours-ci, et sont une exigence pour une grande portion des entreprises de logiciels
* **Moins de bugs** - Des recherches substantielles suggèrent que l'application de tests à une application peut réduire la densité de bugs en production de 40 % à 80 %.

### **Exemple (en JavaScript)**

Supposons qu'il y ait une fonction écrite dans le fichier **add.js**

```javascript
var add = function(number1, number2){
  return number1 + number2;
}
```

Maintenant, afin d'écrire un test unitaire pour cette fonction particulière, nous pouvons utiliser des outils de test comme [mocha](http://mochajs.org/) :

```javascript
const mocha = require('mocha')
const chai = require('chai')  // C'est une bibliothèque d'assertion
describe('Test pour vérifier la fonction add', function(){
  it('devrait additionner deux nombres', function(){
    (add(2,3)).should.equal(5)  // Vérification que 2+3 devrait être égal à 5 en utilisant la fonction add donnée
  });
});
```

### **Développement piloté par les tests**

Les tests unitaires sont une caractéristique clé de l'approche de développement logiciel basée sur le développement piloté par les tests (TDD).

Dans cette approche, le code pour des fonctionnalités ou fonctions spécifiques est écrit par l'utilisation répétée d'un cycle très court.

Tout d'abord, le développeur écrit un ensemble de tests unitaires automatisés et s'assure qu'ils échouent initialement. Ensuite, le développeur implémente le minimum de code requis pour passer les cas de test.

Une fois qu'il a été validé que le code se comporte comme prévu, le développeur revient en arrière et refactorise le code pour adhérer à toute norme de codage pertinente.

## Plus d'informations sur les tests unitaires :

* [Une introduction aux tests unitaires en Python](https://www.freecodecamp.org/news/an-introduction-to-testing-in-python/)
* [Une introduction aux tests unitaires avec Jasmine](https://www.freecodecamp.org/news/jasmine-unit-testing-tutorial-4e757c2cbf42/)
* [Comment tester unitairement votre premier composant Vue.js](https://www.freecodecamp.org/news/how-to-unit-test-your-first-vue-js-component-14db6e1e360d/)

## Plus sur le développement piloté par les tests :

* [Une introduction pratique au développement piloté par les tests](https://www.freecodecamp.org/news/practical-tdd-test-driven-development-84a32044ed0b/)
* [TDD : ce que c'est, et ce que ce n'est pas](https://www.freecodecamp.org/news/test-driven-development-what-it-is-and-what-it-is-not-41fa6bca02a2/)
* [Une introduction rapide au TDD avec Jest](https://www.freecodecamp.org/news/a-quick-introduction-to-test-driven-development-with-jest-cac71cb94e50/)
* [Pourquoi le TDD vaut votre temps](https://www.freecodecamp.org/news/test-driven-development-i-hated-it-now-i-cant-live-without-it-4a10b7ce7ed6/)