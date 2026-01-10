---
title: 'Apprendre ES6 à la manière cool Partie I : const, let & var'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-01T05:40:02.000Z'
originalURL: https://freecodecamp.org/news/learn-es6-the-dope-way-i-const-let-var-ae828580472b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RuxaPPPrL6K09eF4pFhISw.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Apprendre ES6 à la manière cool Partie I : const, let & var'
seo_desc: 'By Mariya Diminsky

  Welcome to Part I of Learn ES6 The Dope Way, a series created to help you easily
  understand ES6 (ECMAScript 6)!

  First up, what’s the deal with const, let, and var?

  You’ve probably been a witness to one of these situations — let and...'
---

Par Mariya Diminsky

Bienvenue dans la Partie I de **Apprendre ES6 à la manière cool**, une série créée pour vous aider à comprendre facilement ES6 (ECMAScript 6) !

Commençons par comprendre ce qu'il en est de _const_, _let_ et _var_.

Vous avez probablement été témoin de l'une de ces situations — _let_ et/ou _const_ remplaçant _var_, ou _let_ et _const_ étant utilisés dans le même code en même temps, ou encore plus déroutant, _let_, _const_ ET _var_ tous utilisés en même temps !

Hey, pas de souci, je vous couvre. Clarifions cela ensemble :

#### const

Avantages :

* Utile si vous définissez une variable que vous ne prévoyez pas de changer.
* Protège et empêche vos variables d'être réassignées.
* Dans les langages compilés, il y a une augmentation de l'efficacité d'exécution de votre code et ainsi une amélioration globale des performances par rapport à l'utilisation du vieux _var_.

Attention :

* Fonctionne comme prévu dans Chrome et Firefox. Mais pas dans Safari. Au lieu de cela, il agit comme une variable normale, comme si c'était _var_, et peut donc être réassigné.
* Généralement, il y a une convention de programmation pour définir le nom en majuscules pour montrer aux autres lisant votre code que la valeur de la _const_ ne doit pas être changée — vous verrez à la fois des situations de codage _const_ en minuscules et en majuscules. Juste quelque chose à garder à l'esprit.

Exemples :

```js
// parfois utilisé en minuscules comme lors de la configuration de votre serveur.
const express = require('express');
const app = express();

// parfois en majuscules.
const DONT_CHANGE_ME_MAN = "Je ne change pour personne, mec."

// tentative de changement #1 
const DONT_CHANGE_ME_MAN = "J'ai dit que je ne changeais pour personne."
// tentative de changement #2
var DONT_CHANGE_ME_MAN = "Toujours pas de changement, frère."
// tentative de changement #3
DONT_CHANGE_ME_MAN = "Haha, belle tentative, ça n'arrive toujours pas."

// même erreur pour les 3 tentatives, la valeur const reste la même :
Uncaught TypeError: Identifier 'const DONT_CHANGE_ME_MAN' has already been declared.

// DONT_CHANGE_ME_MAN donne toujours "Je ne change pour personne, mec."
```

Cela a-t-il du sens ?

> Pensez à const, comme la mer constante — *sans fin, jamais changeante…*
>   
> …sauf dans Safari.

#### let

Les étudiants et les programmeurs expérimentés venant d'un background Ruby ou Python vont adorer _let_, car il impose la portée de bloc !

Alors que vous migrez vers le pays ES6, vous pouvez remarquer que vous vous ajustez à une nouvelle métamorphose _let_ prenant le dessus sur votre style de codage, et vous trouverez moins probable d'utiliser _var_ désormais. Avec _let_, il est beaucoup plus clair maintenant d'où viennent vos valeurs sans vous soucier de leur élévation !

Avantages :

* Portée de bloc, les valeurs de vos variables sont exactement comme elles devraient être dans cette portée actuelle et elles ne sont pas élevées comme avec _var_.
* Super utile si vous ne voulez pas que vos valeurs soient écrasées, comme dans une boucle for.

Attention :

* Vous ne voudrez peut-être pas toujours utiliser _let_. Par exemple, dans des situations où les variables ne sont pas aussi facilement à portée de bloc, _var_ peut être plus pratique.

Exemples :

```js
// Lorsque nous utilisons var, que obtenons-nous ?
var bunny = "mange carotte";

if(bunny) {
  var bunny = "mange brindille";
  console.log(bunny) //  "mange brindille"
}

console.log(bunny)// "mange brindille"

// Lorsque nous utilisons let, que obtenons-nous ?
let bunny = "mange carotte";

if(bunny) {
  let bunny = "mange brindille";
  console.log(bunny) // "mange brindille"
}

console.log(bunny)// "mange carotte"
```

Voyez-vous la différence ? Tout est une question de portée. Avec _var_, il a accès à sa portée parente/extérieure et peut ainsi changer la valeur à l'intérieur de l'instruction if. Contrairement à _let_ qui est à portée de bloc et ne peut être altéré que dans la portée actuelle dans laquelle il se trouve.

_let_ est super simple. C'est comme une personne qui vous parle directement et vous dit exactement ce dont elle a besoin sur le moment, tandis que _var_ fait de même mais peut occasionnellement répondre avec des réponses inattendues — en raison de l'élévation et de l'accès aux variables de portée extérieure. Selon la situation, l'un ou l'autre peut être en votre faveur.

Un autre excellent exemple sur les avantages de _let_ :

Disons que vous voulez créer un plateau de jeu de 30 divs et que chacun a sa propre valeur. Si vous deviez faire cela avec _var_, l'index _i_ serait écrasé à chaque itération — chaque div aurait la valeur de 30 ! Aïe !

D'autre part, avec _let_, chaque div a sa propre valeur, car sa propre portée de div est maintenue pour chaque itération ! Voyez la différence :

```js
// avec var. Voir l'exemple en direct : https://jsfiddle.net/maasha/gsewf5av/
for(var i= 0; i<30; i++){
  var div = document.createElement('div');
  div.onclick = function() {
    alert("vous avez cliqué sur une boîte " + i);
   };
   document.getElementsByTagName('section')[0].appendChild(div);
}

// avec let. Voir l'exemple en direct : https://jsfiddle.net/maasha/xwrq8d5j/
for(let i=0; i<30; i++) {
  var div=document.createElement('div');
  div.onclick = function() {
    alert("vous avez cliqué sur une boîte " + i);
   };
   document.getElementsByTagName('section')[0].appendChild(div);
}
```

Félicitations ! Vous avez réussi à traverser **Apprendre ES6 à la manière cool** Partie I et maintenant vous connaissez les principales différences entre const, let et var ! Hourra ! Vous êtes une rockstar, vous :)

Gardez vos connaissances à jour en aimant et en suivant car plus de **Apprendre ES6 à la manière cool** arrive bientôt sur Medium !

**[Partie I : const, let & var](https://www.freecodecamp.org/news/learn-es6-the-dope-way-i-const-let-var-ae828580472b/)**

**[Partie II : Fonctions (fléchées) => et mot-clé 'this'](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-ii-arrow-functions-and-the-this-keyword-381ac7a32881/)**

**[Partie III : Littéraux de gabarit, opérateurs de propagation & générateurs !](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iii-template-literals-spread-operators-generators-592765337294/)**

**[Partie IV : Paramètres par défaut, affectation par décomposition, et une nouvelle méthode ES6 !](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iv-default-parameters-destructuring-assignment-a-new-es6-method-44393190b8c9/)**

**[Partie V : Classes, transpilation du code ES6 & plus de ressources !](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-v-classes-browser-compatibility-transpiling-es6-code-47f62267661/)**

Vous pouvez également me trouver sur github ❤ [https://github.com/Mashadim](https://github.com/Mashadim)