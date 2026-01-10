---
title: Apprenez ces fondamentaux de JavaScript et devenez un meilleur développeur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-28T21:46:32.000Z'
originalURL: https://freecodecamp.org/news/learn-these-javascript-fundamentals-and-become-a-better-developer-2a031a0dc9cf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2K1k1leVNAnXnscL1KBjEQ.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
seo_title: Apprenez ces fondamentaux de JavaScript et devenez un meilleur développeur
seo_desc: 'By Cristian Salcescu

  Discover Functional JavaScript was named one of the best new Functional Programming
  books by BookAuthority!

  JavaScript has primitives, objects and functions. All of them are values. All are
  treated as objects, even primitives.

  Pr...'
---

Par Cristian Salcescu

[**Découvrez JavaScript Fonctionnel**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE) a été nommé l'un des [**meilleurs nouveaux livres sur la Programmation Fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781)**!**

JavaScript a des primitives, des objets et des fonctions. Tous sont des valeurs. Tous sont traités comme des objets, même les primitives.

### Primitives

Nombre, booléen, chaîne de caractères, `undefined` et `null` sont des primitives.

#### Nombre

Il n'y a qu'un seul type de nombre en JavaScript, le type nombre à virgule flottante 64 bits. L'arithmétique des nombres décimaux est inexacte.

Comme vous le savez peut-être déjà, `0.1 + 0.2` ne donne pas `0.3`. Mais avec les entiers, l'arithmétique est exacte, donc `1+2 === 3`.

Les nombres héritent des méthodes de l'objet `Number.prototype`. Les méthodes peuvent être appelées sur les nombres :

```
(123).toString();  //"123"
(1.23).toFixed(1); //"1.2"
```

Il existe des fonctions pour convertir des chaînes de caractères en nombres : `Number.parseInt()`, `Number.parseFloat()` et `Number()` :

```
Number.parseInt("1")       //1
Number.parseInt("texte")    //NaN
Number.parseFloat("1.234") //1.234
Number("1")                //1
Number("1.234")            //1.234
```

Les opérations arithmétiques invalides ou les conversions invalides ne lanceront pas d'exception, mais résulteront en la valeur `NaN` "Not-a-Number". `Number.isNaN()` peut détecter `NaN`.

L'opérateur `+` peut ajouter ou concaténer.

```
1 + 1      //2
"1" + "1"  //"11"
1 + "1"    //"11"
```

#### Chaîne de caractères

Une chaîne de caractères stocke une série de caractères Unicode. Le texte peut être à l'intérieur de guillemets doubles `""` ou de guillemets simples `''`.

Les chaînes de caractères héritent des méthodes de `String.prototype`. Elles ont des méthodes comme : `substring()`, `indexOf()` et `concat()`.

```
"texte".substring(1,3) //"ex"
"texte".indexOf('x')   //2
"texte".concat(" fin") //"texte fin"
```

Les chaînes de caractères, comme toutes les primitives, sont immuables. Par exemple, `concat()` ne modifie pas la chaîne de caractères existante mais en crée une nouvelle.

#### Booléen

Un booléen a deux valeurs : `true` et `false`.
Le langage a des valeurs "truthy" et "falsy".
`false`, `null`, `undefined`, `''` (chaîne de caractères vide), `0` et `NaN` sont falsy. Toutes les autres valeurs, y compris tous les objets, sont truthy.

La valeur truthy est évaluée à `true` lorsqu'elle est exécutée dans un contexte booléen. La valeur falsy est évaluée à `false`. Regardez l'exemple suivant affichant la branche `false`.

```
let texte = '';
if(texte) {
  console.log("C'est vrai");
} else {
  console.log("C'est faux");
}
```

L'opérateur d'égalité est `===`. L'opérateur de non-égalité est `!==`.

### Variables

Les variables peuvent être définies en utilisant `var`, `let` et `const`.

`var` déclare et initialise optionnellement une variable. Les variables déclarées avec `var` ont une portée de fonction. Elles sont traitées comme déclarées en haut de la fonction. Cela s'appelle le hoisting de variable.

La déclaration `let` a une portée de bloc.

La valeur d'une variable qui n'est pas initialisée est `undefined`.

Une variable déclarée avec `const` ne peut pas être réassignée. Sa valeur, cependant, peut encore être mutable. `const` gèle la variable, `Object.freeze()` gèle l'objet. La déclaration `const` a une portée de bloc.

### Objets

Un objet est une collection dynamique de propriétés.

La clé de propriété est une chaîne de caractères unique. Lorsqu'un non-chaîne est utilisé comme clé de propriété, il sera converti en chaîne de caractères. La valeur de propriété peut être une primitive, un objet ou une fonction.

La manière la plus simple de créer un objet est d'utiliser un littéral d'objet :

```
let obj = {
  message : "Un message",
  faireQuelqueChose : function() {}
}
```

Il existe deux manières d'accéder aux propriétés : la notation par point et la notation par crochets. Nous pouvons lire, ajouter, modifier et supprimer les propriétés d'un objet à tout moment.

* obtenir : `object.nom`, `object[expression]`
* définir : `object.nom = valeur`, `object[expression] = valeur`
* supprimer : `delete object.nom`, `delete object[expression]`

```
let obj = {}; //créer un objet vide
obj.message = "Un message"; //ajouter une propriété
obj.message = "Un nouveau message"; //modifier une propriété
delete obj.message; //supprimer une propriété
```

Les objets peuvent être utilisés comme des maps. Une map simple peut être créée en utilisant `Object.create(null)` :

```
let francais = Object.create(null);
francais["oui"] = "yes";
francais["non"]  = "no";
francais["oui"];//"yes"
```

Toutes les propriétés d'un objet sont publiques. `Object.keys()` peut être utilisé pour itérer sur toutes les propriétés.

```
function logProperty(nom){
  console.log(nom); //nom de la propriété
  console.log(obj[nom]); //valeur de la propriété
}
Object.keys(obj).forEach(logProperty);
```

`Object.assign()` copie toutes les propriétés d'un objet vers un autre. Un objet peut être cloné en copiant toutes ses propriétés vers un objet vide :

```
let livre = { titre: "Les bonnes parties" };
let clone = Object.assign({}, livre);
```

Un objet immuable est un objet qui, une fois créé, ne peut pas être changé. Si vous voulez rendre l'objet immuable, utilisez `Object.freeze()`.

#### Primitives vs Objets

Les primitives (sauf `null` et `undefined`) sont traitées comme des objets, dans le sens où elles ont des méthodes mais ne sont pas des objets.

Les nombres, les chaînes de caractères et les booléens ont des wrappers équivalents objets. Ce sont les fonctions `Number`, `String` et `Boolean`.

Afin de permettre l'accès aux propriétés sur les primitives, JavaScript crée un objet wrapper puis le détruit. Le processus de création et de destruction des objets wrappers est optimisé par le moteur JavaScript.

Les primitives sont immuables, et les objets sont mutables.

### Tableau

Les tableaux sont des collections indexées de valeurs. Chaque valeur est un élément. Les éléments sont ordonnés et accessibles par leur numéro d'index.

JavaScript a des objets de type tableau. Les tableaux sont implémentés en utilisant des objets. Les index sont convertis en chaînes de caractères et utilisés comme noms pour récupérer les valeurs.

Un tableau simple comme `let arr = ['A', 'B', 'C']` est émulé en utilisant un objet comme celui ci-dessous :

```
{
  '0': 'A',
  '1': 'B',
  '2': 'C'
}
```

Notez que `arr[1]` donne la même valeur que `arr['1']` : `arr[1] === arr['1']`.

Supprimer des valeurs du tableau avec `delete` laissera des trous. `splice()` peut être utilisé pour éviter le problème, mais il peut être lent.

```
let arr = ['A', 'B', 'C'];
delete arr[1];
console.log(arr); // ['A', empty, 'C']
console.log(arr.length); // 3
```

Les tableaux de JavaScript ne lancent pas d'exceptions "index out of range". Si l'index n'est pas disponible, il retournera `undefined`.

La pile et la file d'attente peuvent facilement être implémentées en utilisant les méthodes de tableau :

```
let pile = [];
pile.push(1);           // [1]
pile.push(2);           // [1, 2]
let dernier = pile.pop();  // [1]
console.log(dernier);       // 2

let file = [];
file.push(1);           // [1]
file.push(2);           // [1, 2]
let premier = file.shift();//[2]
console.log(premier);      // 1
```

## Fonctions

Les fonctions sont des unités indépendantes de comportement.

Les fonctions sont des objets. Les fonctions peuvent être assignées à des variables, stockées dans des objets ou des tableaux, passées comme argument à d'autres fonctions, et retournées par des fonctions.

Il existe trois manières de définir une fonction :

* Déclaration de fonction (aka Instruction de fonction)
* Expression de fonction (aka Littéral de fonction)
* Fonction fléchée

## La Déclaration de Fonction

* `function` est le premier mot-clé sur la ligne
* elle doit avoir un nom
* elle peut être utilisée avant sa définition. Les déclarations de fonction sont déplacées, ou "hoistées", en haut de leur portée.

```
function faireQuelqueChose(){}
```

L'Expression de Fonction

* `function` n'est pas le premier mot-clé sur la ligne
* le nom est optionnel. Il peut y avoir une expression de fonction anonyme ou une expression de fonction nommée.
* elle doit être définie, puis elle peut s'exécuter
* elle peut s'auto-exécuter après définition (appelée "IIFE" Immediately Invoked Function Expression)

```
let faireQuelqueChose = function() {}
```

## Fonction Fléchée

La fonction fléchée est une syntaxe sucrée pour créer une expression de fonction anonyme.

```
let faireQuelqueChose = () => {};
```

Les fonctions fléchées n'ont pas leur propre `this` et `arguments`.

## Invocation de Fonction

Une fonction, définie avec le mot-clé `function`, peut être invoquée de différentes manières :

* Forme de fonction

```
faireQuelqueChose(arguments)
```

* Forme de méthode

```
lObjet.faireQuelqueChose(arguments)
lObjet["faireQuelqueChose"](arguments)
```

* Forme de constructeur

```
new Constructeur(arguments)
```

* Forme Apply

```
 faireQuelqueChose.apply(lObjet, [arguments])
 faireQuelqueChose.call(lObjet, arguments)
```

Les fonctions peuvent être invoquées avec plus ou moins d'arguments que ceux déclarés dans la définition. Les arguments supplémentaires seront ignorés, et les paramètres manquants seront définis à `undefined`.

Les fonctions (sauf les fonctions fléchées) ont deux pseudo-paramètres : `this` et `arguments`.

## this

Les méthodes sont des fonctions qui sont stockées dans des objets. Les fonctions sont indépendantes. Pour qu'une fonction sache sur quel objet travailler, `this` est utilisé. `this` représente le contexte de la fonction.

Il n'y a pas d'intérêt à utiliser `this` lorsqu'une fonction est invoquée avec la forme de fonction : `faireQuelqueChose()`. Dans ce cas, `this` est `undefined` ou est l'objet `window`, selon que le mode strict est activé ou non.

Lorsque qu'une fonction est invoquée avec la forme de méthode `lObjet.faireQuelqueChose()`, `this` représente l'objet.

Lorsque qu'une fonction est utilisée comme constructeur `new Constructeur()`, `this` représente le nouvel objet créé.

La valeur de `this` peut être définie avec `apply()` ou `call()` : `faireQuelqueChose.apply(lObjet)`. Dans ce cas, `this` est l'objet envoyé comme premier paramètre à la méthode.

La valeur de `this` dépend de la manière dont la fonction a été invoquée, et non de l'endroit où la fonction a été définie. Cela est bien sûr une source de confusion.

## arguments

Le pseudo-paramètre `arguments` donne tous les arguments utilisés lors de l'invocation. C'est un objet de type tableau, mais pas un tableau. Il manque les méthodes de tableau.

```
function log(message){
  console.log(message);
}

function logAll(){
  let args = Array.prototype.slice.call(arguments);
  return args.forEach(log);
}

logAll("msg1", "msg2", "msg3");
```

Une alternative est la nouvelle syntaxe des paramètres rest. Cette fois, `args` est un objet tableau.

```
function logAll(...args){
  return args.forEach(log);
}
```

## return

Une fonction sans instruction `return` retourne `undefined`. Faites attention à l'insertion automatique de point-virgule lors de l'utilisation de `return`. La fonction suivante ne retournera pas un objet vide, mais plutôt un `undefined`.

```
function getObject(){ 
  return 
  {
  }
}
getObject()
```

Pour éviter le problème, utilisez `{` sur la même ligne que `return` :

```
function getObject(){ 
  return {
  }
}
```

## Typage Dynamique

JavaScript a un typage dynamique. Les valeurs ont des types, les variables non. Les types peuvent changer à l'exécution.

```
function log(valeur){
  console.log(valeur);
}

log(1);
log("texte");
log({message : "texte"});
```

L'opérateur `typeof()` peut vérifier le type d'une variable.

```
let n = 1;
typeof(n);   //number

let s = "texte";
typeof(s);   //string

let fn = function() {};
typeof(fn);  //function
```

## Un Seul Thread

Le runtime principal de JavaScript est mono-thread. Deux fonctions ne peuvent pas s'exécuter en même temps. Le runtime contient une File d'Événements qui stocke une liste de messages à traiter. Il n'y a pas de conditions de course, pas de deadlocks. Cependant, le code dans la File d'Événements doit s'exécuter rapidement. Sinon, le navigateur deviendra non réactif et demandera de tuer la tâche.

## Exceptions

JavaScript a un mécanisme de gestion des exceptions. Il fonctionne comme vous pourriez vous y attendre, en enveloppant le code à l'aide de l'instruction `try/catch`. L'instruction a un seul bloc `catch` qui gère toutes les exceptions.

Il est bon de savoir que JavaScript a parfois une préférence pour les erreurs silencieuses. Le code suivant ne lancera pas d'exception lorsque j'essaie de modifier un objet gelé :

```
let obj = Object.freeze({});
obj.message = "texte";
```

Le mode strict élimine certaines erreurs silencieuses de JavaScript. `"use strict";` active le mode strict.

## Modèles de Prototype

`Object.create()`, fonction constructeur et `class` construisent des objets sur le système de prototype.

Considérez l'exemple suivant :

```
let servicePrototype = {
 faireQuelqueChose : function() {}
}

let service = Object.create(servicePrototype);
console.log(service.__proto__ === servicePrototype); //true
```

`Object.create()` construit un nouvel objet `service` qui a l'objet `servicePrototype` comme prototype. Cela signifie que `faireQuelqueChose()` est disponible sur l'objet `service`. Cela signifie également que la propriété `__proto__` de `service` pointe vers l'objet `servicePrototype`.

Construisons maintenant un objet similaire en utilisant `class`.

```
class Service {
  faireQuelqueChose(){}
}

let service = new Service();
console.log(service.__proto__ === Service.prototype);
```

Toutes les méthodes définies dans la classe `Service` seront ajoutées à l'objet `Service.prototype`. Les instances de la classe `Service` auront le même objet prototype (`Service.prototype`). Toutes les instances délégueront les appels de méthode à l'objet `Service.prototype`. Les méthodes sont définies une fois sur `Service.prototype` puis héritées par toutes les instances.

## Chaîne de Prototype

Les objets héritent d'autres objets. Chaque objet a un prototype et hérite de ses propriétés. Le prototype est disponible via la propriété "cachée" `__proto__`.

Lorsque vous demandez une propriété que l'objet ne contient pas, JavaScript cherchera dans la chaîne de prototype jusqu'à ce qu'il trouve la propriété demandée, ou jusqu'à ce qu'il atteigne la fin de la chaîne.

## Modèles Fonctionnels

JavaScript a des fonctions de première classe et des fermetures. Ce sont des concepts qui ouvrent la voie à la Programmation Fonctionnelle en JavaScript. Par conséquent, les fonctions d'ordre supérieur sont possibles.

`filter()`, `map()`, `reduce()` sont la boîte à outils de base pour travailler avec des tableaux dans un style fonctionnel.

`filter()` sélectionne des valeurs dans une liste en fonction d'une fonction prédicat qui décide quelles valeurs doivent être conservées.

`map()` transforme une liste de valeurs en une autre liste de valeurs en utilisant une fonction de mappage.

```
let nombres = [1,2,3,4,5,6];

function estPair(nombre){
  return nombre % 2 === 0;
}

function doublerNombre(x){
  return x*2;
}

let nombresPairs = nombres.filter(estPair);
//2 4 6
let nombresDoubles = nombres.map(doublerNombre);
//2 4 6 8 10 12
```

`reduce()` réduit une liste de valeurs à une seule valeur.

```
function ajouterNombre(total, valeur){
  return total + valeur;
}

function somme(...args){
  return args.reduce(ajouterNombre, 0);
}

somme(1,2,3); //6
```

Une fermeture est une fonction interne qui a accès aux variables de la fonction parente, même après que la fonction parente a été exécutée. [Regardez l'exemple suivant](https://jsfiddle.net/cristi_salcescu/wxzy52mq/?source=post_page---------------------------) :

```
function creerCompteur(){
   let etat = 0;
   return function compter(){
      etat += 1;
      return etat;
   }
}

let compter = creerCompteur();
console.log(compter()); //1
console.log(compter()); //2
```

`compter()` est une fonction imbriquée. `compter()` accède à la variable `etat` de son parent. Elle survit à l'invocation de la fonction parente `creerCompteur()`. `compter()` est une fermeture.

Une fonction d'ordre supérieur est une fonction qui prend une autre fonction en entrée, retourne une fonction, ou fait les deux.

`filter()`, `map()`, `reduce()` sont des fonctions d'ordre supérieur.

Une fonction pure est une fonction qui retourne une valeur basée uniquement sur son entrée. Les fonctions pures n'utilisent pas de variables des fonctions externes. Les fonctions pures ne causent pas de mutations.

Dans les exemples précédents, `estPair()`, `doublerNombre()`, `ajouterNombre()` et `somme()` sont des fonctions pures.

## Conclusion

La puissance de JavaScript réside dans sa simplicité.

Connaître les fondamentaux de JavaScript nous rend meilleurs pour comprendre et utiliser le langage.

Apprenez **React fonctionnel**, de manière basée sur des projets, avec [**Architecture Fonctionnelle avec React et Redux**](https://read.amazon.com/kp/embed?asin=B0846NRJYR&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_o.hlEbDD02JB2)**.**

[**Découvrez JavaScript Fonctionnel**](https://read.amazon.com/kp/embed?asin=B07PBQJYYG&preview=newtab&linkCode=kpe&ref_=cm_sw_r_kb_dp_cm5KCbE5BDJGE&source=post_page---------------------------) a été nommé l'un des [**meilleurs nouveaux livres sur la Programmation Fonctionnelle par BookAuthority**](https://bookauthority.org/books/new-functional-programming-books?t=7p46zt&s=award&book=1095338781&source=post_page---------------------------)**!**

**Pour plus d'informations sur l'application des techniques de programmation fonctionnelle dans React, consultez** **[Functional React](https://www.amazon.com/dp/B088FZQ1XN).**

[Suivez sur Twitter](https://twitter.com/cristi_salcescu)