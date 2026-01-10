---
title: 'Apprendre ES6 à la manière cool Partie IV : Paramètres par défaut, Déstructuration
  et une nouvelle méthode !'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-06-17T22:09:51.000Z'
originalURL: https://freecodecamp.org/news/learn-es6-the-dope-way-part-iv-default-parameters-destructuring-assignment-a-new-es6-method-44393190b8c9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RuxaPPPrL6K09eF4pFhISw.jpeg
tags:
- name: education
  slug: education
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: 'Apprendre ES6 à la manière cool Partie IV : Paramètres par défaut, Déstructuration
  et une nouvelle méthode !'
seo_desc: 'By Mariya Diminsky

  Welcome to Part IV of Learn ES6 The Dope Way, a series created to help you easily
  understand ES6 (ECMAScript 6)!

  Today let’s explore two new ES6 concepts and introduce a new method!


  Default Function Parameters

  Destructuring Assign...'
---

Par Mariya Diminsky

Bienvenue dans la Partie IV de **Apprendre ES6 à la manière cool**, une série créée pour vous aider à comprendre facilement ES6 (ECMAScript 6) !

Aujourd'hui, explorons deux nouveaux concepts ES6 et introduisons une nouvelle méthode !

* Paramètres de fonction par défaut
* Déstructuration
* Une nouvelle méthode ES6 ❤

#### Paramètres de fonction par défaut

Avantages :

* Utile dans les situations où vous avez besoin de valeurs par défaut dans une fonction.
* Lorsque _undefined_ est passé, il utilisera toujours la valeur par défaut à la place !

Attention :

* Si vous définissez une fonction comme valeur par défaut à l'intérieur d'une autre fonction, cela générera une ReferenceError.
* L'emplacement de vos valeurs d'entrée, lorsque vous appelez une fonction, affectera si vous atteignez le paramètre avec la valeur par défaut. Par exemple, si vous aviez deux paramètres et que vous vouliez atteindre le deuxième paramètre, vous n'entreriez qu'un seul élément dans la fonction que vous appelez. Comme le deuxième paramètre serait manquant, la valeur par défaut apparaîtrait là. Voir les exemples ci-dessous pour plus d'explications.

Si vous avez déjà voulu créer une fonction qui aurait des valeurs par défaut comme sauvegarde... FÉLICITATIONS ! Ce jour glorieux est enfin arrivé !

![Image](https://cdn-media-1.freecodecamp.org/images/ZRTmNPBsvuaLTCz8U0fFrX7mzhY7jZxxvMu4)

Les paramètres de fonction par défaut vous permettent d'initialiser des valeurs par défaut si aucune valeur n'est passée, ou si _undefined_ est passé. Avant, si vous aviez quelque chose comme ceci :

```js
function add(x, y) {
  console.log(x+y);
}
add(); // => NaN
```

Vous obtiendriez _NaN_, pas un nombre. Mais maintenant vous pouvez faire ceci :

```js
function add(x=5, y=7) {
  console.log(x+y);
}
add(); // => 12
```

Vous obtenez 12 ! Cela signifie que si vous n'ajoutez pas spécifiquement de valeurs à cette fonction lorsque vous l'appelez, elle utilisera les valeurs par défaut. Vous pouvez donc également faire ceci :

```js
function add(x=5, y=7) {
  console.log(x+y);
}
add(12, 15); // => 27
add(); // => 12

// ET CECI :
function haveFun(action='burrowing', time=3) {
  console.log(`I will go ${action} with Bunny for ${time} hours.`)
}
haveFun(); // => I will go burrowing with Bunny for 3 hours.
haveFun('swimming', 2); // => I will go swimming with Bunny for 2 hours.
```

L'écrasement des valeurs par défaut se produira en fonction de la position à laquelle vous entrez vos valeurs d'entrée lorsque vous appelez la fonction. Par exemple :

```js
function multiply(a, b = 2) {
  return a*b;
}
multiply(3) // => 6 (retourne 3 * 2)
multiply(5, 10) // => 50 (retourne 5 * 10 puisque 10 remplace la valeur par défaut)
```

Lorsque vous passez des valeurs indéfinies, la valeur par défaut est toujours choisie :

```js
// TESTEZ-LE ICI : http://goo.gl/f6y1xb
function changeFontColor(elementId, color='blue') {
  document.getElementById(elementId).style.color = color;
}
changeFontColor('title') // => définit le titre en bleu
changeFontColor('title', 'pink') // => définit le titre en rose
changeFontColor('title', undefined) // => définit le titre en bleu
```

Si aucune valeur par défaut n'est assignée à un paramètre, elle retournera simplement undefined, comme d'habitude :

```js
function test(word1='HeyHeyHey', word2) {
  return `${word1} there, ${word2}!`
}
test(); // => HeyHeyHey there, undefined!

// IMPORTANT :
// Pour atteindre le deuxième paramètre et écraser la fonction par défaut,
// nous devons inclure la première entrée également :
test('Hi', 'Bunny') // => Hi there, Bunny!
```

#### Déstructuration

Avantages :

* Extrait les données des tableaux et des objets et les assigne à des variables
* Simplifie le nombre de frappes nécessaires et améliore la lisibilité
* Super utile lorsque vous devez passer une grande quantité de données avec les mêmes propriétés (comme des profils d'utilisateurs)

Attention :

* Peut être un peu compliqué à comprendre au début, mais une fois que vous comprenez ses avantages, revoyez simplement les exemples fournis et faites des recherches supplémentaires. Vous allez comprendre ! :)

Faisons un pas en arrière et apprenons la déstructuration, et comment elle est utilisée en relation avec les tableaux, les objets, et même en combinaison avec les paramètres par défaut !

Tout d'abord, pratiquons avec les tableaux en créant un tableau des aliments préférés de Bunny. Nous pourrions accéder au premier et au cinquième élément du tableau de la manière traditionnelle :

```js
var BunnyFavFoods = ['Carrots', 'Carrot Bits', 'Grass', 'Berries', 'Papaya', 'Apples'];
console.log(BunnyFavFoods[0]) // => Carrots
console.log(BunnyFavFoods[4]) // => Papaya
```

Ou nous pourrions utiliser la déstructuration ! Nous faisons cela en supprimant le nom de la variable et en passant une parenthèse qui pointera vers les éléments que nous voulons dans le tableau lorsque nous l'appelons :

```js
var [firstItem, fifthItem] = ['Carrots', 'Carrot Bits', 'Grass', 'Berries', 'Papaya', 'Apples'];
console.log(firstItem) // => Carrots
console.log(fifthItem) // => Carrot Bits
```

Oh oh oh ! Qu'est-il arrivé ? Où est notre Papaya ?

AHA ! Je vous ai eu là !

![Image](https://cdn-media-1.freecodecamp.org/images/VhvNuGj9otpoPJB9N1vIctw0Dt7yjLG8SgQg)

Regardez ceci — _firstItem_ et _fifthItem_ sont juste des mots. Le vrai truc ici est où ils sont placés. L'emplacement du mot que vous placez dans les crochets correspondra à l'emplacement de l'élément que vous voulez dans le tableau.

C'est pourquoi le premier mot dans les crochets — _firstItem —_ correspond au premier élément dans le tableau 'Carrots' et le deuxième mot — _fifthItem —_ correspond au deuxième élément dans le tableau, 'Carrot Bits'.

Voici comment accéder à un emplacement différent avec le même mot :

```js
// Chaque virgule supplémentaire ajoutée représentera l'élément suivant dans le tableau.
var [firstItem,,,,fifthItem] = ['Carrots', 'Carrot Bits', 'Grass', 'Berries', 'Papaya', 'Apples'];
console.log(firstItem) // => Carrots
console.log(fifthItem) // => Papaya

// Youpi ! Essayons encore ! Quel élément dans le tableau cela obtiendra-t-il ?
var [firstItem,,guessThisItem,,fifthItem] = ['Carrots', 'Carrot Bits', 'Grass', 'Berries', 'Papaya', 'Apples'];
console.log(firstItem) // => Carrots
console.log(guessThisItem) // => Grass
console.log(fifthItem) // => Papaya

// Remarquez-vous un motif ? Une virgule sépare un mot d'un autre et
// chaque virgule supplémentaire avant un mot représente une place dans le tableau.
// Ok, que se passerait-il si nous ajoutions une virgule au début ?
var [,firstItem,,guessThisItem,,fifthItem] = ['Carrots', 'Carrot Bits', 'Grass', 'Berries', 'Papaya', 'Apples'];
console.log(firstItem) // => Carrot Bits
console.log(guessThisItem) // => Berries
console.log(fifthItem) // => Apples

// Tout se décale d'une place !
// Et si nous déplacions tout en arrière et ajoutions un mot à la fin ?
var [firstItem,,guessThisItem,,fifthItem, whichOneAmI] = ['Carrots', 'Carrot Bits', 'Grass', 'Berries', 'Papaya', 'Apples'];
console.log(firstItem) // => Carrots
console.log(guessThisItem) // => Grass
console.log(fifthItem) // => Papaya
console.log(whichOneAmI) // => Apples
```

Jouez avec ce code dans votre console pour mieux comprendre ce nouveau concept, et dites-nous tous dans la section des commentaires ce que vous trouvez. :)

Ok, nous avons compris les tableaux, alors maintenant comment faire avec la déstructuration des objets ? Commençons par voir la manière typique d'accéder aux éléments dans un objet :

```js
var iceCream = {
  cost: 3.99,
  title: 'Ice Cream Flavors',
  type: ['chocolate', 'vanilla', 'caramel', 'strawberry', 'watermelon']
}

console.log(iceCream.cost, iceCream.title, iceCream.type[2]); 
//=> 3.99 'Ice Cream Flavors' 'caramel'
```

Maintenant, déstructurons cet objet en utilisant une approche similaire à celle que nous avons utilisée avec les tableaux. Supprimez le nom de la variable et à sa place, mettez des accolades — car c'est un objet — tout comme nous l'avons fait avec les crochets pour les tableaux.

À l'intérieur des accolades, passez les propriétés de l'objet auxquelles nous voulons accéder :

```js
var {cost, title, type} = {
  cost: 3.99,
  title: 'Ice Cream Flavors',
  type: ['chocolate', 'vanilla', 'caramel', 'strawberry', 'watermelon']
}

// ET VOILÀ !
console.log(cost, title, type[2]) 
//=> 3.99 'Ice Cream Flavors' 'caramel'
```

Voici une manière légèrement plus compliquée mais utile d'utiliser la déstructuration :

Disons que vous avez une fonction à laquelle vous voulez accéder à tous les objets avec les mêmes propriétés mais des valeurs différentes. Cela peut être particulièrement utile pour les grands ensembles de données, comme les profils d'utilisateurs. Mais dans cet exemple, nous utiliserons les choses préférées de Bunny pour clarifier le concept :

```js
var iceCream = {
  cost: 3.99,
  name: 'Ice Cream Flavors',
  type: ['chocolate', 'vanilla', 'caramel', 'strawberry', 'watermelon']
}

var sushi = {
  cost: 5.99,
  name: 'Sushi Combinations',
  type: ['Eel Roll', 'Philadelphia Roll', 'Spicy Salmon Handroll', 'Rainbow Roll', 'Special Roll']
}

var fruit = {
  cost: 1.99,
  name: 'Fruits', 
  type: ['cherry', 'watermelon', 'strawberry', 'cantaloupe', 'mangosteen']
}

function favThings({cost, name, type}) {
  var randomNum = Math.floor((Math.random() * 4) + 1);
  console.log(`Bunny loves her ${name}! She especially loves ${type[randomNum]} for only $${cost}!`);
}

// Généré aléatoirement pour le paramètre type.
// Première fois :
favThings(iceCream) // => Bunny loves her Ice Cream Flavors! She especially loves caramel for only $3.99!
favThings(sushi) // => Bunny loves her Sushi Combinations! She especially loves Philadelphia Roll for only $5.99!
favThings(fruit) // => Bunny loves her Fruits! She especially loves cantaloupe for only $1.99!

// Deuxième fois :
favThings(iceCream) // => Bunny loves her Ice Cream Flavors! She especially loves vanilla for only $3.99!
favThings(sushi) // => Bunny loves her Sushi Combinations! She especially loves Spicy Salmon Handroll for only $5.99!
favThings(fruit) // => Bunny loves her Fruits! She especially loves mangosteen for only $1.99!

// Essayez-le dans la console vous-même et voyez ce que vous obtenez !
```

Alors, qu'est-il arrivé ?

Lorsque nous avons passé nos objets (iceCream, sushi, fruit), la fonction favThings les a analysés et nous a permis d'accéder à ces propriétés parce que nous avons utilisé les mêmes noms de propriétés dans chaque objet.

#### Combinaison de la déstructuration avec les paramètres par défaut

Étudiez l'exemple ci-dessous :

```js
function profilePage({favColor: favColor} = {favColor: 'vintage pink'}, [name, age] = ['Bunny', 24]) {
  console.log(`My name is ${name}. I am ${age} years old and my favorite color is ${favColor}!`)
}

profilePage(); 
// => My name is Bunny. I am 24 years old and my favorite color is vintage pink!
profilePage({favColor: 'blue'}, ['Ed', 30]) 
// => My name is Ed. I am 30 years old and my favorite color is blue!
```

Ou si vous aviez un objet et un tableau prêts pour la déstructuration :

```js
var aboutEdward = {
  info: ['Edward', 30],
  favColor: 'blue',
  favSushiRoll: 'Squidy squid squid'
}

function profilePage({favColor} = {favColor: 'vintage pink'}, [name, age] = ['Bunny', 24]) {
  console.log(`My name is ${name}. I am ${age} years old and my favorite color is ${favColor}!`)
}
profilePage(); 
// => My name is Bunny. I am 24 years old and my favorite color is vintage pink!
profilePage(aboutEdward, aboutEdward.info); 
// => My name is Edward. I am 30 years old and my favorite color is blue!
```

#### Une nouvelle méthode ES6 ❤

Avantages :

* Répéter des chaînes sans utiliser votre propre algorithme

Attention :

* Les nombres négatifs et l'infini provoqueront une erreur de type _RangeError_
* Les nombres décimaux seront arrondis à l'entier inférieur

Vous avez déjà vu cet algorithme, celui que vous obtenez généralement lorsque vous commencez à apprendre les algorithmes et qu'il vous demande de répéter un mot/une chaîne plusieurs fois ?

FÉLICITATIONS !

Vos jours d'algorithmes de répétition de chaînes sont révolus !

![Image](https://cdn-media-1.freecodecamp.org/images/Gmhzyylidg2RgnlYdMijrfnnyy7Z1zV6rrHV)

Présentation de la nouvelle méthode _repeat()_ apportée par ES6 !

Voici comment cela fonctionne :

```js
// La syntaxe générale : str.repeat(count);

// Exemples :
'Bunny'.repeat(3); // => BunnyBunnyBunny
'Bunny'.repeat(2.5)// => BunnyBunny
'Bunny'.repeat(10/2) // => BunnyBunnyBunnyBunnyBunny
'Bunny'.repeat(-3) // => RangeError: Invalid count value
'Bunny'.repeat(1/0) // => RangeError: Invalid count value
```

Bien que si vous lisez ceci et que vous apprenez les algorithmes ou que vous n'avez pas encore commencé à les apprendre, je vous conseillerais vivement de créer une fonction pour répéter une chaîne et de ne pas utiliser cette méthode, car cela irait à l'encontre du but d'apprendre et de résoudre des défis. Une fois que vous l'aurez compris, allez-y et utilisez cette méthode à votre guise. YIPEE !

Félicitations ! Vous avez réussi à traverser **Apprendre ES6 à la manière cool** Partie IV et vous avez maintenant acquis deux concepts ES6 super importants : les paramètres de fonction par défaut et la déstructuration, ainsi qu'une nouvelle méthode amusante pour répéter une chaîne ! Hourra ! Allez-y !

N'oubliez pas que si vous voulez utiliser ES6, il y a encore des problèmes de compatibilité avec les navigateurs, alors utilisez des compilateurs comme _Babel_ ou un bundler de modules comme _Webpack_ avant de publier votre code. Tout cela sera discuté dans les futures éditions de **Apprendre ES6 à la manière cool ! Merci pour la lecture** **❤**

Gardez votre sagesse à jour en aimant et en suivant car plus de **Apprendre ES6 à la manière cool** arrive bientôt sur Medium !

**[Partie I : const, let & var](https://www.freecodecamp.org/news/learn-es6-the-dope-way-i-const-let-var-ae828580472b/)**

**[Partie II : Fonctions (fléchées) => et mot-clé 'this'](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-ii-arrow-functions-and-the-this-keyword-381ac7a32881/)**

**[Partie III : Littéraux de gabarit, opérateurs de propagation & générateurs !](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iii-template-literals-spread-operators-generators-592765337294/)**

**[Partie IV : Paramètres par défaut, déstructuration et une nouvelle méthode ES6 !](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-iv-default-parameters-destructuring-assignment-a-new-es6-method-44393190b8c9/)**

**[Partie V : Classes, transpilation du code ES6 & plus de ressources !](https://www.freecodecamp.org/news/learn-es6-the-dope-way-part-v-classes-browser-compatibility-transpiling-es6-code-47f62267661/)**

Vous pouvez également me trouver sur github ❤ [https://github.com/Mashadim](https://github.com/Mashadim)