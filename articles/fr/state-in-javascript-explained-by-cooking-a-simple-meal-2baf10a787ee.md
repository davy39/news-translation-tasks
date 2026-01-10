---
title: L'état en JavaScript expliqué par la cuisson d'un repas simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-29T17:37:57.000Z'
originalURL: https://freecodecamp.org/news/state-in-javascript-explained-by-cooking-a-simple-meal-2baf10a787ee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aZkorGpX907Zio5hZwkqUw.jpeg
tags:
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: L'état en JavaScript expliqué par la cuisson d'un repas simple
seo_desc: 'By Kevin Kononenko

  If you have ever cooked a meal at home, then you can understand how to write stateful
  code using object-oriented programming methods in JavaScript.

  When you start writing simple JavaScript programs, you don’t need to worry about
  th...'
---

Par Kevin Kononenko

*Si vous avez déjà cuisiné un repas à la maison, alors vous pouvez comprendre comment écrire du code avec état en utilisant des méthodes de programmation orientée objet en JavaScript.*

Lorsque vous commencez à écrire des programmes JavaScript simples, vous n'avez pas besoin de vous soucier du nombre de variables que vous utilisez, ou de la manière dont différentes fonctions et objets fonctionnent ensemble.

Par exemple, la plupart des gens commencent par utiliser beaucoup de variables globales, ou des variables qui sont définies au niveau supérieur du fichier. Elles ne font pas partie d'une classe, d'un objet ou d'une fonction individuelle.

Par exemple, voici une variable globale appelée _state_ :

```
let state = "global";
```

Mais une fois que votre programme commence à impliquer de nombreuses fonctions et/ou objets différents, vous devrez créer un ensemble de règles plus rigoureux pour votre code.

C'est là que le concept d'[état](https://en.wikipedia.org/wiki/State_(computer_science)) entre en jeu. L'état décrit le statut de l'ensemble du programme ou d'un objet individuel. Il peut s'agir de texte, d'un nombre, d'un booléen ou d'un autre type de données.

C'est un outil courant pour coordonner le code. Par exemple, une fois que vous mettez à jour l'état, un ensemble de fonctions différentes peut réagir instantanément à ce changement.

[Cet article décrit l'état dans le contexte de React](https://blog.codeanalogies.com/2016/10/04/react-props-state-explained-through-darth-vaders-hunt-for-the-rebels/), une bibliothèque JavaScript populaire.

Mais devinez quoi ? Même l'état peut vous donner des maux de tête une fois que votre code devient compliqué ! Changer l'état peut entraîner des conséquences imprévues.

Arrêtons-nous là. L'état est un outil populaire en programmation orientée objet, ou POO. Mais de nombreux programmeurs préfèrent la programmation fonctionnelle, qui décourage les changements d'état. JavaScript supporte les deux paradigmes.

D'accord, c'est beaucoup de terminologie à la fois. Je voulais trouver un moyen de montrer comment la POO et la programmation fonctionnelle peuvent accomplir les mêmes objectifs, même si la programmation fonctionnelle n'utilise pas l'état.

Ce tutoriel montrera comment vous pourriez cuisiner un repas de spaghetti et de sauce d'un point de vue POO et fonctionnel.

Voici un aperçu rapide des deux approches différentes :

![Image](https://cdn-media-1.freecodecamp.org/images/oTkNmmVjtCJc5aYh4VHa5JX4KVRCqQBVyCN5)

Plongeons-nous dedans. Pour comprendre ce tutoriel, vous devez simplement comprendre les fonctions et les objets en JavaScript.

### Méthode Orientée Objet (Utilisation de l'État)

Dans le graphique ci-dessus, nous avons montré deux approches différentes pour préparer ce dîner de pâtes :

1. Une méthode qui se concentre sur l'état des différents outils, comme la cuisinière, la casserole et les pâtes.
2. Une méthode qui se concentre sur la progression de la nourriture elle-même, sans mention de l'état des outils individuels (casseroles, cuisinières, etc.)

L'approche orientée objet se concentre sur la mise à jour de l'état, donc notre code aura un état à deux niveaux différents :

1. Global, ou l'état de ce repas entier.
2. Local pour chaque objet.

Nous allons utiliser la syntaxe ES6 dans ce tutoriel pour créer des objets. Voici un exemple d'état global et du prototype « Pot ».

```
let stoveTemp = 500;
```

```
function Pot(){  this.boilStatus = '';  this.startBoiling = function(){    if( stoveTemp > 400)      this.boilStatus = "boiling";  }}
```

```
let pastaPot = new Pot();pastaPot.startBoiling();
```

```
console.log(pastaPot);// Pot { boilStatus = 'boiling'; }
```

**Note :** J'ai simplifié l'instruction `console.log` pour me concentrer sur la mise à jour de l'état.

Voici une représentation visuelle de cette logique :

**Avant**

![Image](https://cdn-media-1.freecodecamp.org/images/jCElYWldFL5A51IYYRw6aI5I-5WbADmRQdz5)

**Après**

![Image](https://cdn-media-1.freecodecamp.org/images/hpCl6rpFZPboXnYk8GMTzh06g8bQxOOl451a)

Il y a deux états, et lorsque `pastaPot` est créé via le prototype `Pot`, il a initialement un `boilStatus` vide. Mais ensuite, il y a un changement d'état.

Nous exécutons `pastaPot.startBoiling()`, et maintenant le `boilStatus` (état local) est « boiling », puisque l'état global de `stoveTemp` est supérieur à 400.

Allons maintenant un peu plus loin. Nous allons permettre aux pâtes de devenir cuites en fonction de l'état de `pastaPot`.

Voici le code que nous allons ajouter à l'extrait ci-dessus :

```
function Pasta (){  this.cookedStatus = false;  this.addToPot = function (boilStatus){    if(boilStatus == "boiling")      this.cookedStatus = true;  }}
```

```
let myMeal = new Pasta();myMeal.addToPot(pastaPot.boilStatus);
```

```
console.log(myMeal.cookedStatus);// true
```

Woah ! C'est beaucoup à la fois. Voici ce qui s'est passé.

1. Nous avons créé un nouveau prototype de « Pasta », où chaque objet aura un état local appelé `cookedStatus`
2. Nous avons créé une nouvelle instance de Pasta appelée `myMeal`
3. Nous avons utilisé l'état de l'objet `pastaPot` que nous avons créé dans le dernier extrait pour déterminer si nous devions mettre à jour l'état appelé `cookedStatus` dans `myMeal` à cuit.
4. Puisque l'état de `boilStatus` dans `pastaPot` était « boiling », nos pâtes sont maintenant cuites !

Voici ce processus visuellement :

Avant

![Image](https://cdn-media-1.freecodecamp.org/images/G2kKUbpleDg1N7uQt5EYBtgevLfbSjJcc-qK)

Après

![Image](https://cdn-media-1.freecodecamp.org/images/CUwOXRurvC2FtZPpD7hbufQzgiaeRrT7YIzv)

Nous avons donc maintenant l'état local d'un objet, qui dépend de l'état local d'un autre objet. Et cet état local dépendait d'un état global ! Vous pouvez voir comment cela peut être difficile. Mais, c'est au moins facile à suivre pour l'instant, puisque les états sont mis à jour explicitement.

### Méthode Fonctionnelle (sans état)

Pour comprendre pleinement l'état, vous devriez être capable de trouver un moyen d'accomplir le même résultat que le code ci-dessus sans modifier réellement l'état. C'est là que la programmation fonctionnelle aide !

La programmation fonctionnelle a deux valeurs fondamentales qui la distinguent de la POO : l'immuabilité et les fonctions pures.

Je ne vais pas entrer dans trop de détails sur ces sujets, mais si vous voulez en savoir plus, je vous encourage à [consulter ce guide de la programmation fonctionnelle](https://opensource.com/article/17/6/functional-javascript) en JavaScript.

Ces deux principes découragent l'utilisation de la modification de l'état dans votre code. Cela signifie que nous ne pouvons pas utiliser d'état local ou global.

La programmation fonctionnelle nous encourage plutôt à passer des paramètres à des fonctions individuelles. Nous pouvons utiliser des variables externes, mais nous ne pouvons pas les utiliser comme état.

Voici un exemple de fonction qui fera bouillir les pâtes :

```
const stoveTemp = 500;
```

```
const cookPasta = (temp) => {  if(temp > 400)    return 'cooked';}
```

```
console.log(cookPasta(stoveTemp));// 'cooked'
```

Ce code retournera avec succès une chaîne de caractères 'cooked'. Mais remarquez — il n'y a pas d'objet que nous mettons à jour. La fonction retourne simplement la valeur qui sera utilisée dans l'étape suivante.

Au lieu de cela, nous nous concentrons sur les entrées et les sorties d'une fonction : `cookPasta`.

Cette perspective examine la transformation de la nourriture elle-même, plutôt que les outils utilisés pour la cuisiner. C'est un peu plus difficile à visualiser, mais nous n'avons pas besoin que la fonction dépende de l'état externe.

Voici à quoi cela ressemble :

![Image](https://cdn-media-1.freecodecamp.org/images/tQ95faSj05pk6NEAxkI9X3UjU8H3ZtSu9cUz)

Pensez-y comme une « vue chronologique » pour la progression du repas — cette fonction particulière ne couvre que la première partie, la transition des pâtes sèches aux pâtes cuites.

Maintenant, couvrons la deuxième partie alors que la nourriture est servie. Voici le code qui servira le repas. Il viendra après le bloc de code ci-dessus :

```
const serveMeal = (pasta) => { if (pasta == 'cooked')   return 'Dinner is ready.'}
```

```
console.log( serveMeal(cookPasta(stoveTemp)) );// 'Dinner is ready.'
```

Maintenant, nous livrons les résultats de la fonction `cookPasta` directement dans la fonction `serveMeal`. Encore une fois, nous sommes capables de faire cela sans changer d'état, ou changer de structures de données.

Voici un diagramme qui utilise la « vue chronologique » pour montrer comment ces deux fonctions fonctionnent ensemble :

![Image](https://cdn-media-1.freecodecamp.org/images/Jle5IaajEswG3c0QFU2-d9uXv4TT6PWao8ay)

### Intéressé par plus de tutoriels visuels ?

Si vous avez aimé ce guide, donnez-lui un « clap » !

Et, si vous souhaitez lire plus de tutoriels visuels sur HTML, CSS et JavaScript, consultez le [site principal CodeAnalogies](http://codeanalogies.com/) pour 50+ tutoriels.