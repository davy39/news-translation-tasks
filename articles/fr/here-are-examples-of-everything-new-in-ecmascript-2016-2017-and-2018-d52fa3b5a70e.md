---
title: Voici des exemples de tout ce qui est nouveau dans ECMAScript 2016, 2017 et
  2018
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-03T06:04:39.000Z'
originalURL: https://freecodecamp.org/news/here-are-examples-of-everything-new-in-ecmascript-2016-2017-and-2018-d52fa3b5a70e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Z-9unq6Am3vekNOa5fD1xg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Voici des exemples de tout ce qui est nouveau dans ECMAScript 2016, 2017
  et 2018
seo_desc: 'By rajaraodv

  It’s hard to keep track of what’s new in JavaScript (ECMAScript). And it’s even
  harder to find useful code examples.

  So in this article, I’ll cover all 18 features that are listed in the TC39’s finished
  proposals that were added in ES201...'
---

Par rajaraodv

Il est difficile de suivre ce qui est nouveau dans JavaScript (ECMAScript). Et il est encore plus difficile de trouver des exemples de code utiles.

Alors dans cet article, je vais couvrir les 18 fonctionnalités qui sont listées dans les [propositions finalisées du TC39](https://github.com/tc39/proposals/blob/master/finished-proposals.md) qui ont été ajoutées dans ES2016, ES2017 et ES2018 (brouillon final) et les montrer avec des exemples utiles.

> C'est un article assez long mais qui devrait être facile à lire. Pensez à cela comme à une "lecture en binge sur Netflix". À la fin de cela, je promets que vous aurez une tonne de connaissances sur toutes ces fonctionnalités.

#### **D'accord, passons-les en revue une par une.**

![Image](https://cdn-media-1.freecodecamp.org/images/44fYmBIMt2XrYNJgDfEFr5IX0SLCEdnNj2EP)

### `1. Array.prototype.includes`

`includes` est une méthode d'instance simple sur Array et aide à trouver facilement si un élément est dans le tableau (y compris `NaN` contrairement à `indexOf`).

![Image](https://cdn-media-1.freecodecamp.org/images/0FvN0UrpiwG3vS7AwCxhgFdkmUtRBzsty8Fg)
_ECMAScript 2016 ou ES7 — Array.prototype.includes()_

> Trivia : les gens du spécification JavaScript voulaient le nommer `contains`, mais cela était apparemment déjà utilisé par Mootools, donc ils ont utilisé `includes`.

#### `2.` Opérateur d'exponentiation `infix`

Les opérations mathématiques comme l'addition et la soustraction ont des opérateurs infixes comme `+` et `-`, respectivement. Similaire à eux, l'opérateur infixe `**` est couramment utilisé pour l'opération d'exponentiation. Dans ECMAScript 2016, `**` a été introduit au lieu de `Math.pow`.

![Image](https://cdn-media-1.freecodecamp.org/images/gtlnVadz1PTBCP3Quu9KLabgpNI-nC3Bw8-r)
_ECMAScript 2016 ou ES7 — Opérateur infixe d'exponentiation **_

![Image](https://cdn-media-1.freecodecamp.org/images/HmFguQSmejxvd4hxOcVsTnWT8XhUoWclGsOj)

### 1. Object.values()

`Object.values()` est une nouvelle fonction similaire à `Object.keys()` mais retourne toutes les valeurs des propriétés propres de l'objet, à l'exclusion de toute valeur dans la chaîne prototype.

![Image](https://cdn-media-1.freecodecamp.org/images/8R384SuwAciT2kI9YsAKBh-vxFrSvErxCjWa)
_ECMAScript 2017 (ES8)— Object.values()_

### 2. Object.entries()

`Object.entries()` est lié à `Object.keys`, mais au lieu de retourner simplement les clés, il retourne à la fois les clés et les valeurs à la manière d'un tableau. Cela rend très simple des choses comme l'utilisation d'objets dans des boucles ou la conversion d'objets en Maps.

**Exemple 1 :**

![Image](https://cdn-media-1.freecodecamp.org/images/1b3wqDqdI1DW2qx9U2aBNjVHkdsK2PHsOfJB)
_ECMAScript 2017 (ES8) — Utilisation de Object.entries() dans des boucles_

**Exemple 2 :**

![Image](https://cdn-media-1.freecodecamp.org/images/96Jw9lz3xZ7QUsymo0x73YGz9gfTaNnlUhUd)
_ECMAScript 2017 (ES8) — Utilisation de Object.entries() pour convertir un objet en Map_

### 3. Remplissage de chaîne

Deux méthodes d'instance ont été ajoutées à String — `String.prototype.padStart` et `String.prototype.padEnd` — qui permettent d'ajouter/préfixer soit une chaîne vide, soit une autre chaîne au début ou à la fin de la chaîne d'origine.

```js
'someString'.padStart(numberOfCharcters [,stringForPadding]); 

'5'.padStart(10) // '         5'
'5'.padStart(10, '=*') //'=*=*=*=*=5'

'5'.padEnd(10) // '5         '
'5'.padEnd(10, '=*') //'5=*=*=*=*='
```

> Cela s'avère utile lorsque nous voulons aligner des choses dans des scénarios comme l'affichage joli ou l'impression de terminal.

#### 3.1 Exemple de padStart :

Dans l'exemple ci-dessous, nous avons une liste de nombres de longueurs variées. Nous voulons préfixer "0" pour que tous les éléments aient la même longueur de 10 chiffres à des fins d'affichage. Nous pouvons utiliser `padStart(10, '0')` pour atteindre facilement cet objectif.

![Image](https://cdn-media-1.freecodecamp.org/images/pDLfNm4KHFG18gimi3kg37nufmeRaqlloadT)
_ECMAScript 2017 — Exemple de padStart_

#### 3.2 Exemple de padEnd :

`padEnd` est vraiment utile lorsque nous imprimons plusieurs éléments de longueurs variées et que nous voulons les aligner à droite correctement.

L'exemple ci-dessous est un bon exemple réaliste de la façon dont `padEnd`, `padStart` et `Object.entries` se combinent pour produire une belle sortie.

![Image](https://cdn-media-1.freecodecamp.org/images/HvUh0bvyojcU7KfimZiTWoPlHybupuK-Lpaf)
_ECMAScript 2017 — Exemple de padEnd, padStart et Object.Entries_

```js
const cars = {
  '?BMW': '10',
  '?Tesla': '5',
  '?Lamborghini': '0'
}

Object.entries(cars).map(([name, count]) => {
  //padEnd ajoute ' -' jusqu'à ce que le nom atteigne 20 caractères
  //padStart préfixe '0' jusqu'à ce que le compte atteigne 3 caractères.
  console.log(`${name.padEnd(20, ' -')} Count: ${count.padStart(3, '0')}`)
});

//Imprime..
// ?BMW - - - - - - -  Count: 010
// ?Tesla - - - - - -  Count: 005
// ?Lamborghini - - -  Count: 000
```

#### 3.3 ⚠️ padStart et padEnd sur les emojis et autres caractères double-octet

Les emojis et autres caractères double-octet sont représentés en utilisant plusieurs octets Unicode. Donc padStart et padEnd peuvent ne pas fonctionner comme prévu !⚠️

Par exemple : Supposons que nous essayons de remplir la chaîne `heart` pour atteindre `10` caractères avec l'emoji ❤️. Le résultat ressemblera à ceci :

```js
//Remarquez qu'au lieu de 5 cœurs, il n'y a que 2 cœurs et 1 cœur qui semble étrange !
'heart'.padStart(10, "❤️"); // imprime.. '❤️❤️❤️heart'
```

C'est parce que ❤️ est long de 2 points de code (`'\u2764\uFE0F'` ) ! Le mot `heart` lui-même fait 5 caractères, donc nous n'avons qu'un total de 5 caractères restants à remplir. Donc ce qui se passe, c'est que JS remplit deux cœurs en utilisant `'\u2764\uFE0F'` et cela produit ❤️❤️. Pour le dernier, il utilise simplement le premier octet du cœur `\u2764` qui produit ❤️

Donc nous nous retrouvons avec : `❤️❤️❤️heart`

> PS : Vous pouvez utiliser [ce lien](https://encoder.internetwache.org/#tab_uni) pour vérifier les conversions de caractères Unicode.

### 4. `Object.getOwnPropertyDescriptors`

Cette méthode retourne tous les détails (y compris les méthodes getter `get` et setter `set`) pour toutes les propriétés d'un objet donné. La principale motivation pour ajouter cela est de permettre une copie superficielle / clonage d'un objet dans un autre objet qui copie également les fonctions getter et setter contrairement à `Object.assign`.

**Object.assign copie superficiellement tous les détails sauf les fonctions getter et setter de l'objet source original.**

L'exemple ci-dessous montre la différence entre `Object.assign` et `Object.getOwnPropertyDescriptors` ainsi que `Object.defineProperties` pour copier un objet original `Car` dans un nouvel objet `ElectricCar`. Vous verrez qu'en utilisant `Object.getOwnPropertyDescriptors`, les fonctions getter et setter `discount` sont également copiées dans l'objet cible.

AVANT...

![Image](https://cdn-media-1.freecodecamp.org/images/7ZlAkKKdplx53IOn-jYMIPLdZSq90XhAP5jR)
_Avant — Utilisation de Object.assign_

APRÈS...

![Image](https://cdn-media-1.freecodecamp.org/images/23g3sL3-pFGkRri0wOT3g3N2Qzn-oDcKjxVB)
_ECMAScript 2017 (ES8) — Object.getOwnPropertyDescriptors_

```js
var Car = {
 name: 'BMW',
 price: 1000000,
 set discount(x) {
  this.d = x;
 },
 get discount() {
  return this.d;
 },
};

//Imprimer les détails de la propriété 'discount' de l'objet Car
console.log(Object.getOwnPropertyDescriptor(Car, 'discount'));
//imprime..
// { 
//   get: [Function: get],
//   set: [Function: set],
//   enumerable: true,
//   configurable: true
// }

//Copier les propriétés de Car vers ElectricCar en utilisant Object.assign
const ElectricCar = Object.assign({}, Car);

//Imprimer les détails de la propriété 'discount' de l'objet ElectricCar
console.log(Object.getOwnPropertyDescriptor(ElectricCar, 'discount'));
//imprime..
// { 
//   value: undefined,
//   writable: true,
//   enumerable: true,
//   configurable: true 
// }
//⚠️Remarquez que les getters et setters sont manquants dans l'objet ElectricCar pour la propriété 'discount' !?!

//Copier les propriétés de Car vers ElectricCar2 en utilisant Object.defineProperties 
//et extraire les propriétés de Car en utilisant Object.getOwnPropertyDescriptors
const ElectricCar2 = Object.defineProperties({}, Object.getOwnPropertyDescriptors(Car));

//Imprimer les détails de la propriété 'discount' de l'objet ElectricCar2
console.log(Object.getOwnPropertyDescriptor(ElectricCar2, 'discount'));
//imprime..
// { get: [Function: get],  ??????
//   set: [Function: set],  ??????
//   enumerable: true,
//   configurable: true 
// }
// Remarquez que les getters et setters sont présents dans l'objet ElectricCar2 pour la propriété 'discount' !
```

### 5. `Ajout de virgules finales dans les paramètres de fonction`

C'est une mise à jour mineure qui nous permet d'avoir des virgules finales après le dernier paramètre de fonction. Pourquoi ? Pour aider avec des outils comme git blame afin de s'assurer que seuls les nouveaux développeurs sont blâmés.

L'exemple ci-dessous montre le problème et la solution.

![Image](https://cdn-media-1.freecodecamp.org/images/KyY6NFFjMTOeAITlQNt-kKtE9q9E33vZrBbk)
_ECMAScript 2017 (ES 8) — Virgule finale dans le paramètre de fonction_

> Note : Vous pouvez également appeler des fonctions avec des virgules finales !

### 6. Async/Await

Cela, de loin, est la fonctionnalité la plus importante et la plus utile si vous me demandez. Les fonctions asynchrones nous permettent de ne pas traiter l'enfer des rappels et de rendre l'ensemble du code simple.

Le mot-clé `async` indique au compilateur JavaScript de traiter la fonction différemment. Le compilateur fait une pause chaque fois qu'il atteint le mot-clé `await` dans cette fonction. Il suppose que l'expression après `await` retourne une promesse et attend que la promesse soit résolue ou rejetée avant de continuer.

Dans l'exemple ci-dessous, la fonction `getAmount` appelle deux fonctions asynchrones `getUser` et `getBankBalance`. Nous pouvons le faire en promesse, mais utiliser `async await` est plus élégant et simple.

![Image](https://cdn-media-1.freecodecamp.org/images/JYCOVItTbISYtWjgbt2lDVdyk8KOOjYVk2sc)
_ECMAScript 2017 (ES 8) — Exemple de base Async Await_

#### **6.1** Les fonctions asynchrones elles-mêmes retournent une promesse.

Si vous attendez le résultat d'une fonction asynchrone, vous devez utiliser la syntaxe `then` de Promise pour capturer son résultat.

Dans l'exemple suivant, nous voulons journaliser le résultat en utilisant `console.log` mais pas dans doubleAndAdd. Donc nous voulons attendre et utiliser la syntaxe `then` pour passer le résultat à `console.log`.

![Image](https://cdn-media-1.freecodecamp.org/images/xnz7tfy5QVKp9VXjcVjqUoMXDwHZuGFX8rd1)
_ECMAScript 2017 (ES 8) — Async Await eux-mêmes retournent une promesse_

#### **6.2 Appel de async/await en parallèle**

Dans l'exemple précédent, nous appelons await deux fois, mais chaque fois nous attendons une seconde (total 2 secondes). Au lieu de cela, nous pouvons le paralléliser puisque `a` et `b` ne dépendent pas l'un de l'autre en utilisant `Promise.all`.

![Image](https://cdn-media-1.freecodecamp.org/images/kWJN5r5sz0F5o2XIpO1qmspgT1BujE0YTTtk)
_ECMAScript 2017 (ES 8) — Utilisation de Promise.all pour paralléliser async/await_

#### 6.3 Gestion des erreurs des fonctions async/await

Il existe diverses façons de gérer les erreurs lors de l'utilisation de async await.

#### **Option 1 — Utiliser try catch dans la fonction**

![Image](https://cdn-media-1.freecodecamp.org/images/PfUYa9Vo5hTFbCHaE5XnaiPjuV4VmUNVWtVh)
_ECMAScript 2017 — **Utiliser try catch dans la fonction async/await**_

```js
//Option 1 - Utiliser try catch dans la fonction
async function doubleAndAdd(a, b) {
 try {
  a = await doubleAfter1Sec(a);
  b = await doubleAfter1Sec(b);
 } catch (e) {
  return NaN; //retourner quelque chose
 }
return a + b;
}

//?Usage:
doubleAndAdd('one', 2).then(console.log); // NaN
doubleAndAdd(1, 2).then(console.log); // 6

function doubleAfter1Sec(param) {
 return new Promise((resolve, reject) => {
  setTimeout(function() {
   let val = param * 2;
   isNaN(val) ? reject(NaN) : resolve(val);
  }, 1000);
 });
}
```

#### **Option 2— Attraper chaque expression await**

Puisque chaque expression `await` retourne une promesse, vous pouvez attraper les erreurs sur chaque ligne comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/wGCb4bAga1z9mkI1FwKRhYFugCL00pUTeavM)
_ECMAScript 2017 — **Utiliser try catch sur chaque expression await**_

```js
//Option 2 - *Attraper* les erreurs sur chaque ligne await
//car chaque expression await est une promesse en soi
async function doubleAndAdd(a, b) {
 a = await doubleAfter1Sec(a).catch(e => console.log('"a" est NaN')); // ?
 b = await doubleAfter1Sec(b).catch(e => console.log('"b" est NaN')); // ?
 if (!a || !b) {
  return NaN;
 }
 return a + b;
}

//?Usage:
doubleAndAdd('one', 2).then(console.log); // NaN  et journalise :  "a" est NaN
doubleAndAdd(1, 2).then(console.log); // 6

function doubleAfter1Sec(param) {
 return new Promise((resolve, reject) => {
  setTimeout(function() {
   let val = param * 2;
   isNaN(val) ? reject(NaN) : resolve(val);
  }, 1000);
 });
}
```

#### **Option 3 — Attraper toute la fonction async-await**

![Image](https://cdn-media-1.freecodecamp.org/images/bYcQiaVTX1wRzOGg0Vh13TYg5WW8qSVu0DS6)
_ECMAScript 2017 — **Attraper toute la fonction async/await à la fin**_

```js
//Option 3 - Ne rien faire mais gérer en dehors de la fonction
//puisque async / await retourne une promesse, nous pouvons attraper l'erreur de toute la fonction
async function doubleAndAdd(a, b) {
 a = await doubleAfter1Sec(a);
 b = await doubleAfter1Sec(b);
 return a + b;
}

//?Usage:
doubleAndAdd('one', 2)
.then(console.log)
.catch(console.log); // ???<------- utiliser "catch"

function doubleAfter1Sec(param) {
 return new Promise((resolve, reject) => {
  setTimeout(function() {
   let val = param * 2;
   isNaN(val) ? reject(NaN) : resolve(val);
  }, 1000);
 });
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/G9wavF5qssi1AP4C2lF9WgiQ7Hm766eWGt6J)

> ECMAScript est actuellement en brouillon final et sortira en juin ou juillet 2018. Toutes les fonctionnalités couvertes ci-dessous sont en Stage-4 et feront partie d'ECMAScript 2018.

#### 1. [Mémoire partagée et atomiques](https://github.com/tc39/ecmascript_sharedmem)

C'est une fonctionnalité énorme, assez avancée et une amélioration majeure des moteurs JS.

**L'idée principale est d'apporter une sorte de fonctionnalité multithreading à JavaScript afin que les développeurs JS puissent écrire des programmes concurrents et haute performance à l'avenir en permettant de gérer la mémoire eux-mêmes au lieu de laisser le moteur JS gérer la mémoire.**

Cela est fait par un nouveau type d'objet global appelé [SharedArrayBuffer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer) qui stocke essentiellement les données dans un espace mémoire **partagé**. Ainsi, ces données peuvent être partagées entre le thread principal JS et les threads web-worker.

Jusqu'à présent, si nous voulions partager des données entre le thread principal JS et les web-workers, nous devions copier les données et les envoyer à l'autre thread en utilisant `postMessage`. Plus maintenant !

Vous utilisez simplement SharedArrayBuffer et les données sont instantanément accessibles à la fois par le thread principal et plusieurs threads web-worker.

Mais le partage de mémoire entre les threads peut causer des conditions de course. Pour aider à éviter les conditions de course, l'objet global "[_Atomics_](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics)" est introduit. _Atomics_ fournit diverses méthodes pour verrouiller la mémoire partagée lorsqu'un thread utilise ses données. Il fournit également des méthodes pour mettre à jour ces données dans cette mémoire partagée en toute sécurité.

> La recommandation est d'utiliser cette fonctionnalité via une bibliothèque, mais pour l'instant, il n'y a pas de bibliothèques construites sur cette fonctionnalité.

Si vous êtes intéressé, je recommande de lire :

1. [_From Workers to Shared Memory_](http://lucasfcosta.com/2017/04/30/JavaScript-From-Workers-to-Shared-Memory.html) — [lucasfcosta](http://lucasfcosta.com/)
2. [_A cartoon intro to SharedArrayBuffers_](https://hacks.mozilla.org/category/code-cartoons/a-cartoon-intro-to-sharedarraybuffers/) — [Lin Clark](https://www.freecodecamp.org/news/here-are-examples-of-everything-new-in-ecmascript-2016-2017-and-2018-d52fa3b5a70e/undefined)
3. [_Shared memory and atomics_](http://2ality.com/2017/01/shared-array-buffer.html) — [Dr. Axel Rauschmayer](http://rauschma.de/)

#### 2. Restriction des littéraux de modèle étiquetés supprimée

Tout d'abord, nous devons clarifier ce qu'est un "littéral de modèle étiqueté" afin de mieux comprendre cette fonctionnalité.

Dans ES2015+, il existe une fonctionnalité appelée littéral de modèle étiqueté qui permet aux développeurs de personnaliser la manière dont les chaînes sont interpolées. Par exemple, de manière standard, les chaînes sont interpolées comme ci-dessous...

![Image](https://cdn-media-1.freecodecamp.org/images/qijvAdivaNWMbUMxVg4rer3K1BWYl7bbCcO5)

Dans le littéral étiqueté, vous pouvez écrire une fonction pour recevoir les parties codées en dur du littéral de chaîne, par exemple `[ 'Hello ', '!' ]`, et les variables de remplacement, par exemple, `[ 'Raja']`, en tant que paramètres dans une fonction personnalisée (par exemple `greet`), et retourner ce que vous voulez de cette fonction personnalisée.

L'exemple ci-dessous montre que notre fonction "Tag" personnalisée `greet` ajoute l'heure de la journée comme "Bonjour !", "Bonjour", etc., selon l'heure de la journée au littéral de chaîne et retourne une chaîne personnalisée.

![Image](https://cdn-media-1.freecodecamp.org/images/aRMqlDhbYudFqPvnNhfrPYkyKXgTkaEn87t0)
_Exemple de fonction Tag qui montre l'interpolation de chaîne personnalisée_

```js
//Une fonction "Tag" retourne un littéral de chaîne personnalisé.
//Dans cet exemple, greet appelle timeGreet() pour ajouter Bonjour/Bon après-midi/Bonsoir selon l'heure de la journée.

function greet(hardCodedPartsArray, ...replacementPartsArray) {
 console.log(hardCodedPartsArray); //[ 'Hello ', '!' ]
 console.log(replacementPartsArray); //[ 'Raja' ]
    
let str = '';
 hardCodedPartsArray.forEach((string, i) => {
  if (i < replacementPartsArray.length) {
   str += `${string} ${replacementPartsArray[i] || ''}`;
  } else {
   str += `${string} ${timeGreet()}`; //<-- ajouter Bonjour/Bon après-midi/Bonsoir ici
  }
 });
 return str;
}

//?Usage:
const firstName = 'Raja';
const greetings = greet`Hello ${firstName}!`; //??<-- Littéral étiqueté

console.log(greetings); //'Hello  Raja! Good Morning!' ?

function timeGreet() {
 const hr = new Date().getHours();
 return hr < 12
  ? 'Good Morning!'
  : hr < 18 ? 'Good Afternoon!' : 'Good Evening!';
}
```

Maintenant que nous avons discuté de ce que sont les fonctions "Tagged", beaucoup de gens veulent utiliser cette fonctionnalité dans différents domaines, comme dans le Terminal pour les commandes et les requêtes HTTP pour composer des URIs, etc.

#### ⚠️Le problème avec le littéral de chaîne étiqueté

Le problème est que les spécifications ES2015 et ES2016 n'autorisent pas l'utilisation de caractères d'échappement comme "\u" (unicode), "\x" (hexadécimal) sauf s'ils ressemblent exactement à `\u00A9` ou \u{2F804} ou \xA9.

Donc si vous avez une fonction Tagged qui utilise en interne les règles d'un autre domaine (comme les règles du Terminal), qui peuvent avoir besoin d'utiliser **\ubla123abla** qui ne ressemble pas à \u0049 ou \u{@F804}, alors vous obtiendrez une erreur de syntaxe.

Dans ES2018, les règles sont assouplies pour permettre de tels caractères d'échappement apparemment invalides tant que la fonction Tagged retourne les valeurs dans un objet avec une propriété "cooked" (où les caractères invalides sont "undefined"), et ensuite une propriété "raw" (avec ce que vous voulez).

```js
function myTagFunc(str) { 
 return { "cooked": "undefined", "raw": str.raw[0] }
} 

var str = myTagFunc `hi \ubla123abla`; //appeler myTagFunc

str // { cooked: "undefined", raw: "hi \\unicode" }
```

### 3. Indicateur "dotall" pour les expressions régulières

Actuellement dans RegEx, bien que le point ("\.") soit censé correspondre à un seul caractère, il ne correspond pas aux caractères de nouvelle ligne comme `\n \r \f etc`.

Par exemple :

```js
//Avant
/first.second/.test('first\nsecond'); //false
```

Cette amélioration permet à l'opérateur point de correspondre à n'importe quel caractère unique. Pour s'assurer que cela ne casse rien, nous devons utiliser l'indicateur `\s` lorsque nous créons le RegEx pour que cela fonctionne.

```js
//ECMAScript 2018
/first.second/s.test('first\nsecond'); //true   Remarque : /s ??  
```

Voici l'API globale du document de [proposition](https://github.com/tc39/proposal-regexp-dotall-flag) :

![Image](https://cdn-media-1.freecodecamp.org/images/leiiozJApb5rPA97rUqBOvzvEtVguXtPcOrk)
_ECMAScript 2018 — La fonctionnalité dotAll de Regex permet de correspondre même à \n via "." via l'indicateur /s_

### 4. Captures de groupes nommés RegExp ?

Cette amélioration apporte une fonctionnalité RegExp utile d'autres langages comme Python, Java et ainsi de suite appelée "Groupes nommés". Cette fonctionnalité permet aux développeurs écrivant RegExp de fournir des noms (identifiants) au format `(?<name>...)` pour différentes parties du groupe dans le RegExp. Ils peuvent ensuite utiliser ce nom pour saisir facilement le groupe dont ils ont besoin.

#### 4.1 Exemple de groupe nommé de base

Dans l'exemple ci-dessous, nous utilisons les noms `(?<year>) (?<month>) et (?<day>)` pour regrouper différentes parties de la date RegEx. L'objet résultant contiendra maintenant une propriété `groups` avec les propriétés `year`, `month` et `day` avec les valeurs correspondantes.

![Image](https://cdn-media-1.freecodecamp.org/images/TkGEzq1zFYdE-YP8YJadJ7VacNhF9gsyf7FB)
_ECMAScript 2018 — Exemple de groupes nommés Regex_

#### **4.2 Utilisation des groupes nommés à l'intérieur de la regex elle-même**

Nous pouvons utiliser le format `\k<nom du groupe>` pour référencer le groupe dans la regex elle-même. L'exemple suivant montre comment cela fonctionne.

![Image](https://cdn-media-1.freecodecamp.org/images/hc1rRx9L0IPX0BG0CGtqUWIRf2KRAHC-5P7R)
_ECMAScript 2018 — Référencement arrière des groupes nommés Regex via \k<nom du groupe>_

#### **4.3 Utilisation des groupes nommés dans String.prototype.replace**

La fonctionnalité de groupe nommé est maintenant intégrée dans la méthode d'instance `replace` de String. Ainsi, nous pouvons facilement échanger des mots dans la chaîne.

Par exemple, changer "firstName, lastName" en "lastName, firstName".

![Image](https://cdn-media-1.freecodecamp.org/images/bQvxKQY6VfUNRGjeAsCXm0EJEDCbgPe0ti0S)
_ECMAScript 2018 — Utilisation de la fonctionnalité des groupes nommés de RegEx dans la fonction replace_

### 5. Propriétés rest pour les objets

L'opérateur rest `...` (trois points) nous permet d'extraire les propriétés d'objet qui ne sont pas déjà extraites.

#### **5.1 Vous pouvez utiliser rest pour aider à extraire uniquement les propriétés que vous voulez**

![Image](https://cdn-media-1.freecodecamp.org/images/WBZ31BCucgiEXjxal3IkEEdHFbkk3PwpbzGF)
_ECMAScript 2018 — Déstructuration d'objet via rest_

#### **5.2 Encore mieux, vous pouvez supprimer les éléments indésirables ! ??**

![Image](https://cdn-media-1.freecodecamp.org/images/jMNJhSOaReoiWi9Z6LZdQYmxT0aVHedQiRKO)
_ECMAScript 2018 — Déstructuration d'objet via rest_

### **6. Propriétés spread pour les objets**

**Les propriétés spread ressemblent également aux propriétés rest avec trois points `...` mais la différence est que vous utilisez spread pour créer (restructurer) de nouveaux objets.**

> **Astuce : l'opérateur spread est utilisé du côté droit du signe égal. Les rest sont utilisés du côté gauche du signe égal.**

![Image](https://cdn-media-1.freecodecamp.org/images/Kw63nZhNAIkprEucTKQou35zzTDcvoXenX4D)
_ECMAScript 2018 — Restructuration d'objet via spread_

### **7. Assertions de lookbehind RegExp**

C'est une amélioration de RegEx qui nous permet de nous assurer qu'une chaîne existe immédiatement *avant* une autre chaîne.

Vous pouvez maintenant utiliser un groupe `(?<=\u2026)` _(point d'interrogation, inférieur, égal)_ pour rechercher une assertion positive.

De plus, vous pouvez utiliser `(?<!\u2026)` _(point d'interrogation, inférieur, exclamation)_, pour rechercher une assertion négative. Essentiellement, cela correspondra tant que l'assertion négative passera.

**Assertion positive :** Supposons que nous voulons nous assurer que le signe `#` existe avant le mot `winning` (c'est-à-dire : `#winning`) et que nous voulons que le regex retourne simplement la chaîne "winning". Voici comment vous l'écrirez.

![Image](https://cdn-media-1.freecodecamp.org/images/sz6nM4Fzby9XVG96i8eUCvzoE705bGAEeHb7)
_ECMAScript 2018 — `(?&lt;=\u2026) pour l'assertion positive`_

**Assertion négative :** Supposons que nous voulons extraire des nombres de lignes qui ont des signes € et non des signes $ avant ces nombres.

![Image](https://cdn-media-1.freecodecamp.org/images/KA-ZXAVf2GOH65G1ndEwkkl7fEFyTaxWDPlL)
_ECMAScript 2018 — (?&lt;!\u2026) pour les assertions négatives_

### **8. [Échappements de propriété Unicode RegExp](https://github.com/tc39/proposal-regexp-unicode-property-escapes)**

Il n'était pas facile d'écrire RegEx pour correspondre à divers caractères Unicode. Des choses comme `\w`, `\W`, `\d` etc ne correspondent qu'aux caractères et chiffres anglais. Mais qu'en est-il des chiffres dans d'autres langues comme l'hindi, le grec, etc ?

C'est là que les échappements de propriété Unicode interviennent. **Il s'avère qu'Unicode ajoute des propriétés de métadonnées pour chaque symbole (caractère) et les utilise pour regrouper ou caractériser divers symboles.**

Par exemple, la base de données Unicode regroupe tous les caractères Hindi (\u0939\u093f\u0928\u094d\u0926\u0940) sous une propriété appelée `Script` avec la valeur `Devanagari` et une autre propriété appelée `Script_Extensions` avec la même valeur `Devanagari`. Ainsi, nous pouvons rechercher `Script=Devanagari` et obtenir tous les caractères Hindi.

_[Devanagari](https://en.wikipedia.org/wiki/Devanagari_(Unicode_block)) peut être utilisé pour diverses langues indiennes comme le Marathi, l'Hindi, le Sanskrit, etc._

À partir d'ECMAScript 2018, nous pouvons utiliser `\p` pour échapper les caractères avec `{Script=Devanagari}` pour correspondre à tous ces caractères indiens. **C'est-à-dire que nous pouvons utiliser :** `**\p{Script=Devanagari}**` **dans le RegEx pour correspondre à tous les caractères Devanagari.**

![Image](https://cdn-media-1.freecodecamp.org/images/zCjtuGGGmBvzUO9b2cCdqraXfEavM4KrQBhN)
_ECMAScript 2018 — montrant \p_

```js
//Ce qui suit correspond à plusieurs caractères hindi
/^\p{Script=Devanagari}+$/u.test('\u0939\u093f\u0928\u094d\u0926\u0940'); //true  
//PS: il y a 3 caractères hindi h
```

De même, la base de données Unicode regroupe tous les caractères grecs sous la propriété `Script_Extensions` (et `Script`) avec la valeur `Greek`. Ainsi, nous pouvons rechercher tous les caractères grecs en utilisant `Script_Extensions=Greek` ou `Script=Greek`.

**C'est-à-dire que nous pouvons utiliser :** `**\p{Script=Greek}**` **dans le RegEx pour correspondre à tous les caractères grecs.**

![Image](https://cdn-media-1.freecodecamp.org/images/hXu3bf5S3R68S0NgqCY6qpBP69HdAShaJdgx)
_ECMAScript 2018 — montrant \p_

```js
//Ce qui suit correspond à un seul caractère grec
/\p{Script_Extensions=Greek}/u.test('\u03c0'); // true
```

De plus, la base de données Unicode stocke divers types d'emojis sous les propriétés booléennes `Emoji`, `Emoji_Component`, `Emoji_Presentation`, `Emoji_Modifier`, et `Emoji_Modifier_Base` avec des valeurs de propriété à `true`. Ainsi, nous pouvons rechercher tous les emojis en sélectionnant simplement `Emoji` à true.

**C'est-à-dire que nous pouvons utiliser :** `**\p{Emoji}**`, `**\Emoji_Modifier**` **et ainsi de suite pour correspondre à divers types d'emojis.**

L'exemple suivant rendra tout cela clair.

![Image](https://cdn-media-1.freecodecamp.org/images/hp2GXlB3IanbeH9m1fEOzXglZJiofBKUxdY6)
_ECMAScript 2018 — montrant comment \p peut être utilisé pour divers emojis_

```js
//Ce qui suit correspond à un caractère Emoji
/\p{Emoji}/u.test('\u2764\ufe0f'); //true

//Ce qui suit échoue car les emojis jaunes n'ont pas besoin/n'ont pas Emoji_Modifier !
/\p{Emoji}\p{Emoji_Modifier}/u.test('\u270c\ufe0f'); //false

//Ce qui suit correspond à un caractère emoji \p{Emoji} suivi de \p{Emoji_Modifier}
/\p{Emoji}\p{Emoji_Modifier}/u.test('\u270c?'); //true

//Explication :
//Par défaut, l'emoji de victoire est de couleur jaune.
//Si nous utilisons une variation brune, noire ou autre de cet emoji, elles sont considérées
//comme des variations de l'emoji original et sont représentées en utilisant deux caractères unicode.
//Un pour l'emoji original, suivi d'un autre caractère unicode pour la couleur.
//
//Donc dans l'exemple ci-dessous, bien que nous ne voyions qu'un seul emoji de victoire brun,
//il utilise en réalité deux caractères unicode, un pour l'emoji et un autre
//pour la couleur brune.
//
//Dans la base de données Unicode, ces couleurs ont la propriété Emoji_Modifier.
//Donc nous devons utiliser à la fois \p{Emoji} et \p{Emoji_Modifier} pour correspondre correctement et
//complètement à l'emoji brun.
/\p{Emoji}\p{Emoji_Modifier}/u.test('\u270c?'); //true
```

**Enfin, nous pouvons utiliser le caractère d'échappement "P" majuscule (**`\P` **) au lieu du "p" minuscule (**`\p` **), pour négocier les correspondances.**

Références :

1. [_Proposition ECMAScript 2018_](https://mathiasbynens.be/notes/es-unicode-property-escapes)
2. [_https://mathiasbynens.be/notes/es-unicode-property-escapes_](https://mathiasbynens.be/notes/es-unicode-property-escapes)

### **8. Promise.prototype.finally()**

`finally()` est une nouvelle méthode d'instance qui a été ajoutée à Promise. L'idée principale est de permettre l'exécution d'un rappel après `resolve` ou `reject` pour aider à nettoyer les choses. Le rappel `finally` est appelé sans aucune valeur et est toujours exécuté quoi qu'il arrive.

Regardons différents cas.

![Image](https://cdn-media-1.freecodecamp.org/images/yQ99TgkxFshSnmlQqdfFMM73kQcxAcKH2VHl)
_ECMAScript 2018 — finally() dans le cas de résolution_

![Image](https://cdn-media-1.freecodecamp.org/images/KlH72OCk03Fj3AXXtaB-gXVnxDFKEtWz7nUp)
_ECMAScript 2018 — finally() dans le cas de rejet_

![Image](https://cdn-media-1.freecodecamp.org/images/WFFh7DJihhy4C2bGH86n2g5bZ9vyoNu1h7WU)
_ECMASCript 2018 — finally() dans le cas d'erreur lancée à partir de la promesse_

![Image](https://cdn-media-1.freecodecamp.org/images/Y34QmvZuh3kYeob2HC3W4fFXB2fFkpRLvfND)
_**ECMAScript 2018 — Erreur lancée à partir du cas catch**_

### **9. Itération asynchrone**

C'est une fonctionnalité *extrêmement* utile. Essentiellement, elle nous permet de créer des boucles de code asynchrone avec facilité !

Cette fonctionnalité ajoute une nouvelle boucle **"for-await-of"** qui nous permet d'appeler des fonctions asynchrones qui retournent des promesses (ou des tableaux avec un tas de promesses) dans une boucle. Le truc cool est que la boucle attend que chaque promesse soit résolue avant de passer à la boucle suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/XAZiwAIhT8JdwhA5y7GMP8Dm4oJ1tyqsI5Qo)
_ECMAScript 2018 — Itérateur asynchrone via for-await-of_

C'est à peu près tout !

Si cela était utile, veuillez cliquer sur le bouton d'applaudissements ? ci-dessous quelques fois pour montrer votre soutien ! F44FF44FF44F ??

### Mes autres articles

**[_https://medium.com/@rajaraodv/latest_](https://medium.com/@rajaraodv/latest)**

#### **Articles liés à ECMAScript 2015+**

1. **[_Découvrez ces conseils et astuces utiles d'ECMAScript 2015 (ES6)_](https://medium.freecodecamp.org/check-out-these-useful-ecmascript-2015-es6-tips-and-tricks-6db105590377)**
2. **[_5 parties "mauvaises" de JavaScript qui sont corrigées dans ES6_](https://medium.com/@rajaraodv/5-javascript-bad-parts-that-are-fixed-in-es6-c7c45d44fd81#.7e2s6cghy)**
3. **[_La "classe" dans ES6 est-elle la nouvelle partie "mauvaise" ?_](https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65#.4hqgpj2uv)**