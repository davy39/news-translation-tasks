---
title: Apprendre TypeScript – Le Guide Ultime pour Débutants
subtitle: ''
author: Danny
co_authors: []
series: null
date: '2022-01-27T17:47:36.000Z'
originalURL: https://freecodecamp.org/news/learn-typescript-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Cheat-Sheet-Poster--1-.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: TypeScript
  slug: typescript
seo_title: Apprendre TypeScript – Le Guide Ultime pour Débutants
seo_desc: "TypeScript has become increasingly popular over the last few years, and\
  \ many jobs are now requiring developers to know TypeScript. \nBut don't be alarmed\
  \ – if you already know JavaScript, you will be able to pick up TypeScript quickly.\
  \ \nEven if you do..."
---

TypeScript est devenu de plus en plus populaire ces dernières années, et de nombreux emplois exigent désormais que les développeurs connaissent TypeScript. 

Mais ne vous alarmez pas – si vous connaissez déjà JavaScript, vous pourrez apprendre TypeScript rapidement. 

Même si vous ne prévoyez pas d'utiliser TypeScript, l'apprendre vous donnera une meilleure compréhension de JavaScript – et fera de vous un meilleur développeur.

Dans cet article, vous apprendrez :

* Qu'est-ce que TypeScript et pourquoi devrais-je l'apprendre ?
* Comment configurer un projet avec TypeScript
* Tous les principaux concepts de TypeScript (types, interfaces, génériques, transtypage, et plus...)
* Comment utiliser TypeScript avec React

J'ai également créé une [feuille de triche TypeScript PDF](https://doabledanny.gumroad.com/l/typescript-cheat-sheet-pdf) et une [affiche](https://doabledanny.gumroad.com/l/typescript-cheat-sheet-poster) qui résument cet article en une seule page. Cela facilite la recherche et la révision rapide des concepts/syntaxe.

![Feuille de triche TypeScript PDF](https://www.freecodecamp.org/news/content/images/2022/01/TypeScript-Cheat-Sheet--DARK-.png)
_Feuille de triche TypeScript PDF_

## Qu'est-ce que TypeScript ?

TypeScript est un sur-ensemble de JavaScript, ce qui signifie qu'il fait tout ce que JavaScript fait, mais avec quelques fonctionnalités supplémentaires.

La principale raison d'utiliser TypeScript est d'ajouter un typage statique à JavaScript. Le typage statique signifie que le type d'une variable ne peut pas être changé à aucun moment dans un programme. Cela peut prévenir BEAUCOUP de bugs !

D'autre part, JavaScript est un langage à typage dynamique, ce qui signifie que les variables peuvent changer de type. Voici un exemple :

```ts
// JavaScript
let foo = "hello";
foo = 55; // foo a changé de type d'une chaîne à un nombre - aucun problème

// TypeScript
let foo = "hello";
foo = 55; // ERREUR - foo ne peut pas changer de chaîne à nombre
```

TypeScript ne peut pas être compris par les navigateurs, il doit donc être compilé en JavaScript par le compilateur TypeScript (TSC) – que nous discuterons bientôt.

## TypeScript en vaut-il la peine ?

### Pourquoi vous devriez utiliser TypeScript

* Des recherches ont montré que TypeScript peut détecter 15 % des bugs courants.
* Lisibilité – il est plus facile de voir ce que le code est censé faire. Et lorsque vous travaillez en équipe, il est plus facile de voir ce que les autres développeurs voulaient faire.
* C'est populaire – connaître TypeScript vous permettra de postuler à plus de bons emplois.
* Apprendre TypeScript vous donnera une meilleure compréhension et une nouvelle perspective sur JavaScript.

[Voici un court article que j'ai écrit démontrant comment TypeScript peut prévenir des bugs irritants](https://www.doabledanny.com/why-typescript-over-javascript).

### Inconvénients de TypeScript

* TypeScript prend plus de temps à écrire que JavaScript, car vous devez spécifier les types, donc pour les petits projets solo, cela ne vaut peut-être pas la peine de l'utiliser.
* TypeScript doit être compilé – ce qui peut prendre du temps, surtout dans les grands projets.

Mais le temps supplémentaire que vous devez passer à écrire un code plus précis et à compiler sera plus que compensé par le nombre de bugs que vous aurez en moins dans votre code. 

Pour de nombreux projets – surtout les projets de taille moyenne à grande – TypeScript vous fera gagner beaucoup de temps et de maux de tête.

Et si vous connaissez déjà JavaScript, TypeScript ne sera pas trop difficile à apprendre. C'est un excellent outil à avoir dans votre arsenal.

## Comment Configurer un Projet TypeScript


### Installer Node et le Compilateur TypeScript

Tout d'abord, assurez-vous d'avoir [Node](https://nodejs.org/en/download/) installé globalement sur votre machine.

Ensuite, installez le compilateur TypeScript globalement sur votre machine en exécutant la commande suivante : 

```bash
npm i -g typescript
```

Pour vérifier si l'installation est réussie (elle retournera le numéro de version si elle est réussie) :

```bash
tsc -v
```

### Comment Compiler TypeScript

Ouvrez votre éditeur de texte et créez un fichier TypeScript (par exemple, index.ts).

Écrivez du JavaScript ou TypeScript :

```ts
let sport = 'football';

let id = 5;
```

Nous pouvons maintenant compiler cela en JavaScript avec la commande suivante :

```bash
tsc index
```

TSC compilera le code en JavaScript et le sortira dans un fichier appelé index.js :

```js
var sport = 'football';
var id = 5;
```

Si vous souhaitez spécifier le nom du fichier de sortie :

`tsc index.ts --outfile file-name.js`

Si vous souhaitez que TSC compile votre code automatiquement, chaque fois que vous faites une modification, ajoutez le flag "watch" :

`tsc index.ts -w`

Une chose intéressante à propos de TypeScript est qu'il signale les erreurs dans votre éditeur de texte pendant que vous codez, mais il compilera toujours votre code – qu'il y ait des erreurs ou non. 

Par exemple, ce qui suit fait que TypeScript signale immédiatement une erreur :

```
var sport = 'football';
var id = 5;

id = '5'; // Erreur : Le type 'string' ne peut pas être assigné au type 'number'.
```

Mais si nous essayons de compiler ce code avec `tsc index`, le code sera toujours compilé, malgré l'erreur. 

C'est une propriété importante de TypeScript : il suppose que le développeur en sait plus. Même s'il y a une erreur TypeScript, cela n'empêche pas la compilation du code. Il vous dit qu'il y a une erreur, mais c'est à vous de décider si vous faites quelque chose à ce sujet.

### Comment Configurer le Fichier tsconfig

Le fichier tsconfig doit être dans le répertoire racine de votre projet. Dans ce fichier, nous pouvons spécifier les fichiers racine, les options du compilateur et à quel point nous voulons que TypeScript soit strict dans la vérification de notre projet.

Tout d'abord, créez le fichier tsconfig :

`tsc --init`

Vous devriez maintenant avoir un fichier `tsconfig.json` à la racine du projet.

Voici quelques options qu'il est bon de connaître (si vous utilisez un framework frontend avec TypeScript, la plupart de ces choses sont prises en charge pour vous) :

```
{
    "compilerOptions": {
        ...
        /* Modules */
        "target": "es2016", // Changer en "ES2015" pour compiler en ES6
        "rootDir": "./src", // Où compiler depuis
        "outDir": "./public", // Où compiler vers (généralement le dossier à déployer sur le serveur web)
        
        /* Support JavaScript */
        "allowJs": true, // Autoriser les fichiers JavaScript à être compilés
        "checkJs": true, // Vérifier les fichiers JavaScript et signaler les erreurs
        
        /* Émission */
        "sourceMap": true, // Créer des fichiers de carte source pour les fichiers JavaScript émis (bon pour le débogage)
         "removeComments": true, // Ne pas émettre les commentaires
    },
    "include": ["src"] // Assurer que seuls les fichiers dans src sont compilés
}
```

Pour compiler tout et surveiller les changements :

`tsc -w`



Remarque : lorsque des fichiers d'entrée sont spécifiés sur la ligne de commande (par exemple, `tsc index`), les fichiers `tsconfig.json` sont ignorés.

## Les Types en TypeScript

### Types primitifs

En JavaScript, une valeur primitive est une donnée qui n'est pas un objet et n'a pas de méthodes. Il existe 7 types de données primitifs :

* string
* number
* bigint
* boolean
* undefined
* null
* symbol

Les primitifs sont immuables : ils ne peuvent pas être altérés. Il est important de ne pas confondre un primitif lui-même avec une variable à laquelle une valeur primitive est assignée. La variable peut être réassignée à une nouvelle valeur, mais la valeur existante ne peut pas être changée de la manière dont les objets, les tableaux et les fonctions peuvent être altérés. 

Voici un exemple :

```
let name = 'Danny';
name.toLowerCase();
console.log(name); // Danny - la méthode de chaîne n'a pas muté la chaîne

let arr = [1, 3, 5, 7];
arr.pop();
console.log(arr); // [1, 3, 5] - la méthode de tableau a muté le tableau

name = 'Anna' // L'assignation donne au primitif une nouvelle valeur (non mutée)
```

En JavaScript, toutes les valeurs primitives (à part null et undefined) ont des équivalents objets qui enveloppent les valeurs primitives. Ces objets enveloppants sont String, Number, BigInt, Boolean et Symbol. Ces objets enveloppants fournissent les méthodes qui permettent de manipuler les valeurs primitives.

Revenons à TypeScript, nous pouvons définir le type que nous voulons qu'une variable soit en ajoutant `: type` (appelé une "annotation de type" ou une "signature de type") après avoir déclaré une variable. Exemples :

```ts
let id: number = 5;
let firstname: string = 'danny';
let hasDog: boolean = true;

let unit: number; // Déclarer une variable sans assigner de valeur
unit = 5;
```

Mais il est généralement préférable de ne pas indiquer explicitement le type, car TypeScript infère automatiquement le type d'une variable (inférence de type) :

```
let id = 5; // TS sait que c'est un nombre
let firstname = 'danny'; // TS sait que c'est une chaîne
let hasDog = true; // TS sait que c'est un booléen

hasDog = 'yes'; // ERREUR
```

Nous pouvons également définir une variable pour qu'elle puisse être un type d'union. **Un type d'union est une variable à laquelle peuvent être assignés plus d'un type** :

```
let age: string | number;
age = 26;
age = '26';
```

### Types de référence

En JavaScript, presque "tout" est un objet. En fait (et de manière confuse), les chaînes, les nombres et les booléens peuvent être des objets s'ils sont définis avec le mot-clé `new` :

```
let firstname = new String('Danny');
console.log(firstname); // String {'Danny'}
```

Mais lorsque nous parlons de types de référence en JavaScript, nous faisons référence aux tableaux, aux objets et aux fonctions.

#### Avertissement : types primitifs vs types de référence

Pour ceux qui n'ont jamais étudié les types primitifs vs les types de référence, discutons de la différence fondamentale.

Si un type primitif est assigné à une variable, nous pouvons considérer que cette variable _contient_ la valeur primitive. Chaque valeur primitive est stockée dans un emplacement unique en mémoire.

Si nous avons deux variables, x et y, et qu'elles contiennent toutes deux des données primitives, alors elles sont complètement indépendantes l'une de l'autre :

![Les données primitives sont stockées dans des emplacements mémoire uniques](https://www.freecodecamp.org/news/content/images/2022/01/image-66.png)
_X et Y contiennent tous deux des données primitives uniques et indépendantes_

```
let x = 2;
let y = 1;

x = y;
y = 100;
console.log(x); // 1 (même si y a changé pour 100, x est toujours 1)
```

Ce n'est pas le cas avec les types de référence. Les types de référence font référence à un emplacement mémoire où l'objet est stocké.

![Emplacements mémoire des types de référence](https://www.freecodecamp.org/news/content/images/2022/01/image-67.png)
_point1 et point2 contiennent une référence à l'adresse où l'objet est stocké_

```ts
let point1 = { x: 1, y: 1 };
let point2 = point1;

point1.y = 100;
console.log(point2.y); // 100 (point1 et point2 font référence à la même adresse mémoire où l'objet point est stocké)
```

C'était un rapide aperçu des types primaires vs les types de référence. Consultez cet article si vous avez besoin d'une explication plus approfondie : [Types primitifs vs types de référence](https://codeburst.io/explaining-value-vs-reference-in-javascript-647a975e12a0).

#### Tableaux en TypeScript

En TypeScript, vous pouvez définir quel type de données un tableau peut contenir :

```js
let ids: number[] = [1, 2, 3, 4, 5]; // ne peut contenir que des nombres
let names: string[] = ['Danny', 'Anna', 'Bazza']; // ne peut contenir que des chaînes
let options: boolean[] = [true, false, false]; // ne peut contenir que true ou false
let books: object[] = [
  { name: 'Fooled by randomness', author: 'Nassim Taleb' },
  { name: 'Sapiens', author: 'Yuval Noah Harari' },
]; // ne peut contenir que des objets
let arr: any[] = ['hello', 1, true]; // any reviens essentiellement à JavaScript

ids.push(6);
ids.push('7'); // ERREUR : L'argument de type 'string' ne peut pas être assigné au paramètre de type 'number'.
```

Vous pouvez utiliser des types d'union pour définir des tableaux contenant plusieurs types :

```ts
let person: (string | number | boolean)[] = ['Danny', 1, true];
person[0] = 100;
person[1] = {name: 'Danny'} // Erreur - le tableau person ne peut pas contenir d'objets
```

Si vous initialisez une variable avec une valeur, il n'est pas nécessaire de préciser explicitement le type, car TypeScript l'inférera :

```ts
let person = ['Danny', 1, true]; // Cela est identique à l'exemple ci-dessus
person[0] = 100;
person[1] = { name: 'Danny' }; // Erreur - le tableau person ne peut pas contenir d'objets
```

Il existe un type spécial de tableau qui peut être défini en TypeScript : les Tuples. **Un tuple est un tableau avec une taille fixe et des types de données connus.** Ils sont plus stricts que les tableaux réguliers.

```
let person: [string, number, boolean] = ['Danny', 1, true];
person[0] = 100; // Erreur - La valeur à l'index 0 ne peut être qu'une chaîne
```

#### Objets en TypeScript

Les objets en TypeScript doivent avoir toutes les propriétés correctes et les types de valeurs :

```ts
// Déclarer une variable appelée person avec une annotation de type d'objet spécifique
let person: {
  name: string;
  location: string;
  isProgrammer: boolean;
};

// Assigner person à un objet avec toutes les propriétés nécessaires et les types de valeurs
person = {
  name: 'Danny',
  location: 'UK',
  isProgrammer: true,
};

person.isProgrammer = 'Yes'; // ERREUR : devrait être un booléen


person = {
  name: 'John',
  location: 'US',
}; 
// ERREUR : il manque la propriété isProgrammer
```

Lors de la définition de la signature d'un objet, vous utiliserez généralement une **interface**. Cela est utile si nous devons vérifier que plusieurs objets ont les mêmes propriétés spécifiques et les mêmes types de valeurs :

```ts
interface Person {
  name: string;
  location: string;
  isProgrammer: boolean;
}

let person1: Person = {
  name: 'Danny',
  location: 'UK',
  isProgrammer: true,
};

let person2: Person = {
  name: 'Sarah',
  location: 'Germany',
  isProgrammer: false,
};

```

Nous pouvons également déclarer des propriétés de fonction avec des signatures de fonction. Nous pouvons le faire en utilisant des fonctions JavaScript classiques (`sayHi`), ou des fonctions fléchées ES6 (`sayBye`) :

```ts
interface Speech {
  sayHi(name: string): string;
  sayBye: (name: string) => string;
}

let sayStuff: Speech = {
  sayHi: function (name: string) {
    return `Hi ${name}`;
  },
  sayBye: (name: string) => `Bye ${name}`,
};

console.log(sayStuff.sayHi('Heisenberg')); // Hi Heisenberg
console.log(sayStuff.sayBye('Heisenberg')); // Bye Heisenberg

```

Notez que dans l'objet `sayStuff`, `sayHi` ou `sayBye` pourrait être donné une fonction fléchée ou une fonction JavaScript commune – TypeScript ne s'en soucie pas.

#### Fonctions en TypeScript

Nous pouvons définir les types des arguments de la fonction, ainsi que le type de retour de la fonction :

```ts
// Définir une fonction appelée circle qui prend une variable diam de type number, et retourne une chaîne
function circle(diam: number): string {
  return 'La circonférence est ' + Math.PI * diam;
}

console.log(circle(10)); // La circonférence est 31.41592653589793
```

La même fonction, mais avec une fonction fléchée ES6 :

```ts
const circle = (diam: number): string => {
  return 'La circonférence est ' + Math.PI * diam;
};

console.log(circle(10)); // La circonférence est 31.41592653589793
```

Remarquez comment il n'est pas nécessaire de préciser explicitement que `circle` est une fonction ; TypeScript l'infère. TypeScript infère également le type de retour de la fonction, donc il n'est pas nécessaire de le préciser non plus. Cependant, si la fonction est grande, certains développeurs préfèrent préciser explicitement le type de retour pour plus de clarté.

```ts
// Utilisation du typage explicite 
const circle: Function = (diam: number): string => {
  return 'La circonférence est ' + Math.PI * diam;
};

// Typage inféré - TypeScript voit que circle est une fonction qui retourne toujours une chaîne, donc pas besoin de le préciser explicitement
const circle = (diam: number) => {
  return 'La circonférence est ' + Math.PI * diam;
};
```

Nous pouvons ajouter un point d'interrogation après un paramètre pour le rendre optionnel. Remarquez également ci-dessous comment `c` est un type d'union qui peut être un nombre ou une chaîne :

```ts
const add = (a: number, b: number, c?: number | string) => {
  console.log(c);

  return a + b;
};

console.log(add(5, 4, 'Je pourrais passer un nombre, une chaîne, ou rien ici !'));
// Je pourrais passer un nombre, une chaîne, ou rien ici !
// 9

```

Une fonction qui ne retourne rien est dite retourner void – une absence totale de toute valeur. Ci-dessous, le type de retour void a été explicitement précisé. Mais encore une fois, cela n'est pas nécessaire car TypeScript l'inférera.

```ts
const logMessage = (msg: string): void => {
  console.log('Ceci est le message : ' + msg);
};

logMessage('TypeScript est superbe'); // Ceci est le message : TypeScript est superbe
```

Si nous voulons déclarer une variable de fonction, mais ne pas la définir (dire exactement ce qu'elle fait), **alors utilisez une signature de fonction.** Ci-dessous, la fonction `sayHello` doit suivre la signature après les deux-points :

```ts
// Déclarer la variable sayHello, et lui donner une signature de fonction qui prend une chaîne et ne retourne rien.
let sayHello: (name: string) => void;

// Définir la fonction, satisfaisant sa signature
sayHello = (name) => {
  console.log('Bonjour ' + name);
};

sayHello('Danny'); // Bonjour Danny

```

#### Voici un scrim interactif pour vous aider à en apprendre davantage sur les fonctions en TypeScript :

<iframe src="https://scrimba.com/scrim/cob6c429eb261c1c2a8506801?embed=freecodecamp,mini-header" width="100%" height="480"></iframe>

### Types dynamiques (any)

En utilisant le type `any`, nous pouvons essentiellement revenir à JavaScript :

```ts
let age: any = '100';
age = 100;
age = {
  years: 100,
  months: 2,
};

```

Il est recommandé d'éviter d'utiliser le type `any` autant que possible, car il empêche TypeScript de faire son travail – et peut entraîner des bugs.

### Alias de types

Les alias de types peuvent réduire la duplication de code, en gardant notre code DRY. Ci-dessous, nous pouvons voir que l'alias de type `PersonObject` a évité la répétition et agit comme une source unique de vérité pour les données qu'un objet person devrait contenir.

```ts
type StringOrNumber = string | number;

type PersonObject = {
  name: string;
  id: StringOrNumber;
};

const person1: PersonObject = {
  name: 'John',
  id: 1,
};

const person2: PersonObject = {
  name: 'Delia',
  id: 2,
};

const sayHello = (person: PersonObject) => {
  return 'Hi ' + person.name;
};

const sayGoodbye = (person: PersonObject) => {
  return 'Seeya ' + person.name;
};

```

### Le DOM et le transtypage

TypeScript n'a pas accès au DOM comme JavaScript. Cela signifie que chaque fois que nous essayons d'accéder aux éléments du DOM, TypeScript n'est jamais sûr qu'ils existent réellement.

L'exemple ci-dessous montre le problème :

```ts
const link = document.querySelector('a');

console.log(link.href); // ERREUR : L'objet est éventuellement 'null'. TypeScript ne peut pas être sûr que la balise d'ancrage existe, car il ne peut pas accéder au DOM
```

Avec l'opérateur d'affirmation non-null (!) nous pouvons dire au compilateur explicitement qu'une expression a une valeur autre que `null` ou `undefined`. Cela peut être utile lorsque le compilateur ne peut pas inférer le type avec certitude, mais que nous avons plus d'informations que le compilateur.

```ts
// Ici, nous disons à TypeScript que nous sommes certains que cette balise d'ancrage existe
const link = document.querySelector('a')!;

console.log(link.href); // www.freeCodeCamp.org
```

Remarquez comment nous n'avons pas eu à préciser le type de la variable `link`. Cela est dû au fait que TypeScript peut clairement voir (via l'inférence de type) qu'il est de type `HTMLAnchorElement`.

Mais que faire si nous devons sélectionner un élément DOM par sa classe ou son id ? TypeScript ne peut pas inférer le type, car il pourrait être n'importe quoi.

```ts
const form = document.getElementById('signup-form');

console.log(form.method);
// ERREUR : L'objet est éventuellement 'null'.
// ERREUR : La propriété 'method' n'existe pas sur le type 'HTMLElement'.

```

Ci-dessus, nous obtenons deux erreurs. Nous devons dire à TypeScript que nous sommes certains que `form` existe, et que nous savons qu'il est de type `HTMLFormElement`. Nous faisons cela avec le transtypage :

```ts
const form = document.getElementById('signup-form') as HTMLFormElement;

console.log(form.method); // post
```

Et TypeScript est content !

TypeScript a également un objet Event intégré. Donc, si nous ajoutons un écouteur d'événement de soumission à notre formulaire, TypeScript nous donnera une erreur si nous appelons des méthodes qui ne font pas partie de l'objet Event. Regardez à quel point TypeScript est cool – il peut nous dire quand nous avons fait une faute de frappe :

```ts
const form = document.getElementById('signup-form') as HTMLFormElement;

form.addEventListener('submit', (e: Event) => {
  e.preventDefault(); // empêche la page de se rafraîchir

  console.log(e.tarrget); // ERREUR : La propriété 'tarrget' n'existe pas sur le type 'Event'. Vouliez-vous dire 'target' ?
});


```

### Voici un scrim interactif pour vous aider à en apprendre davantage sur les types en TypeScript :

<iframe src="https://scrimba.com/scrim/co84a432fa0e3ae761c178813?embed=freecodecamp,mini-header" width="100%" height="480"></iframe>

## Classes en TypeScript

Nous pouvons définir les types que chaque morceau de données devrait être dans une classe :

```ts
class Person {
  name: string;
  isCool: boolean;
  pets: number;

  constructor(n: string, c: boolean, p: number) {
    this.name = n;
    this.isCool = c;
    this.pets = p;
  }

  sayHello() {
    return `Hi, my name is ${this.name} and I have ${this.pets} pets`;
  }
}

const person1 = new Person('Danny', false, 1);
const person2 = new Person('Sarah', 'yes', 6); // ERREUR : L'argument de type 'string' n'est pas assignable au paramètre de type 'boolean'.

console.log(person1.sayHello()); // Hi, my name is Danny and I have 1 pets
```

Nous pourrions ensuite créer un tableau `people` qui ne contient que des objets construits à partir de la classe `Person` :

```ts
let People: Person[] = [person1, person2];
```

Nous pouvons ajouter des modificateurs d'accès aux propriétés d'une classe. TypeScript fournit également un nouveau modificateur d'accès appelé `readonly`.

```ts
class Person {
  readonly name: string; // Cette propriété est immuable - elle ne peut être que lue
  private isCool: boolean; // Peut uniquement accéder ou modifier depuis les méthodes de cette classe
  protected email: string; // Peut accéder ou modifier depuis cette classe et les sous-classes
  public pets: number; // Peut accéder ou modifier depuis n'importe où - y compris en dehors de la classe

  constructor(n: string, c: boolean, e: string, p: number) {
    this.name = n;
    this.isCool = c;
    this.email = e;
    this.pets = p;
  }

  sayMyName() {
    console.log(`Your not Heisenberg, you're ${this.name}`);
  }
}

const person1 = new Person('Danny', false, 'dan@e.com', 1);
console.log(person1.name); // Bien
person1.name = 'James'; // Erreur : lecture seule
console.log(person1.isCool); // Erreur : propriété privée - accessible uniquement dans la classe Person
console.log(person1.email); // Erreur : propriété protégée - accessible uniquement dans la classe Person et ses sous-classes
console.log(person1.pets); // Propriété publique - donc aucun problème
```

Nous pouvons rendre notre code plus concis en construisant les propriétés de classe de cette manière :

```ts
class Person {
  constructor(
    readonly name: string,
    private isCool: boolean,
    protected email: string,
    public pets: number
  ) {}

  sayMyName() {
    console.log(`Your not Heisenberg, you're ${this.name}`);
  }
}

const person1 = new Person('Danny', false, 'dan@e.com', 1);
console.log(person1.name); // Danny

```

En l'écrivant de la manière ci-dessus, les propriétés sont automatiquement assignées dans le constructeur – nous évitant d'avoir à tout écrire.

Notez que si nous omettons le modificateur d'accès, par défaut la propriété sera publique.

Les classes peuvent également être étendues, comme en JavaScript régulier :

```ts
class Programmer extends Person {
  programmingLanguages: string[];

  constructor(
    name: string,
    isCool: boolean,
    email: string,
    pets: number,
    pL: string[]
  ) {
    // L'appel super doit fournir tous les paramètres pour la classe de base (Person), car le constructeur n'est pas hérité.
    super(name, isCool, email, pets);
    this.programmingLanguages = pL;
  }
}
```

[Pour plus d'informations sur les classes, consultez la documentation officielle de TypeScript](https://www.typescriptlang.org/docs/handbook/2/classes.html).

### Voici un scrim interactif pour vous aider à en apprendre davantage sur les classes en TypeScript :

<iframe src="https://scrimba.com/scrim/co52541818fd74bc8663ac381?embed=freecodecamp,mini-header" width="100%" height="480"></iframe>

## Modules en TypeScript

En JavaScript, un module est simplement un fichier contenant du code lié. La fonctionnalité peut être importée et exportée entre les modules, gardant le code bien organisé.

TypeScript supporte également les modules. Les fichiers TypeScript seront compilés en plusieurs fichiers JavaScript.

Dans le fichier `tsconfig.json`, changez les options suivantes pour supporter l'importation et l'exportation modernes :

```ts
 "target": "es2016",
 "module": "es2015"
```

(Bien que, pour les projets Node, vous voulez très probablement `"module": "CommonJS"` – Node ne supporte pas encore l'importation/exportation modernes.)

Maintenant, dans votre fichier HTML, changez l'importation du script pour qu'il soit de type module :

```html
<script type="module" src="/public/script.js"></script>

```

Nous pouvons maintenant importer et exporter des fichiers en utilisant ES6 :

```ts
// src/hello.ts
export function sayHi() {
  console.log('Bonjour !');
}

// src/script.ts
import { sayHi } from './hello.js';

sayHi(); // Bonjour !

```

Remarque : importer toujours en tant que fichier JavaScript, même dans les fichiers TypeScript.

## Interfaces en TypeScript

Les interfaces définissent à quoi un objet devrait ressembler :

```ts
interface Person {
  name: string;
  age: number;
}

function sayHi(person: Person) {
  console.log(`Hi ${person.name}`);
}

sayHi({
  name: 'John',
  age: 48,
}); // Hi John

```

Vous pouvez également définir un type d'objet en utilisant un alias de type :

```ts
type Person = {
  name: string;
  age: number;
};

function sayHi(person: Person) {
  console.log(`Hi ${person.name}`);
}

sayHi({
  name: 'John',
  age: 48,
}); // Hi John
```

Ou un type d'objet pourrait être défini anonymement :

```ts
function sayHi(person: { name: string; age: number }) {
  console.log(`Hi ${person.name}`);
}

sayHi({
  name: 'John',
  age: 48,
}); // Hi John

```

Les interfaces sont très similaires aux alias de types, et dans de nombreux cas, vous pouvez utiliser l'un ou l'autre. La distinction clé est que les alias de types ne peuvent pas être rouverts pour ajouter de nouvelles propriétés, contrairement à une interface qui est toujours extensible. 

Les exemples suivants sont tirés de la [documentation TypeScript](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#differences-between-type-aliases-and-interfaces).

Extension d'une interface :

```ts
interface Animal {
  name: string
}

interface Bear extends Animal {
  honey: boolean
}

const bear: Bear = {
  name: "Winnie",
  honey: true,
}
```

Extension d'un type via des intersections :

```ts
type Animal = {
  name: string
}

type Bear = Animal & {
  honey: boolean
}

const bear: Bear = {
  name: "Winnie",
  honey: true,
}
```

Ajout de nouveaux champs à une interface existante :

```ts
interface Animal {
  name: string
}

// Réouverture de l'interface Animal pour ajouter un nouveau champ
interface Animal {
  tail: boolean
}

const dog: Animal = {
  name: "Bruce",
  tail: true,
}
```

Voici la différence clé : un type ne peut pas être changé après avoir été créé :

```ts
type Animal = {
  name: string
}

type Animal = {
  tail: boolean
}
// ERREUR : Identifiant 'Animal' en double.
```

En règle générale, la documentation TypeScript recommande d'utiliser des interfaces pour définir des objets, jusqu'à ce que vous ayez besoin d'utiliser les fonctionnalités d'un type.

Les interfaces peuvent également définir des signatures de fonction :

```
interface Person {
  name: string
  age: number
  speak(sentence: string): void
}

const person1: Person = {
  name: "John",
  age: 48,
  speak: sentence => console.log(sentence),
}
```

Vous vous demandez peut-être pourquoi nous utiliserions une interface plutôt qu'une classe dans l'exemple ci-dessus. 

Un avantage d'utiliser une interface est qu'elle est uniquement utilisée par TypeScript, pas par JavaScript. Cela signifie qu'elle ne sera pas compilée et n'ajoutera pas de bloat à votre JavaScript. Les classes sont des fonctionnalités de JavaScript, donc elles seraient compilées.

De plus, une classe est essentiellement une _usine à objets_ (c'est-à-dire un plan de ce à quoi un objet est censé ressembler et ensuite implémenté), tandis qu'une interface est une structure utilisée uniquement pour le _contrôle de type_.

Alors qu'une classe peut avoir des propriétés et des méthodes initialisées pour aider à créer des objets, une interface définit essentiellement les propriétés et le type qu'un objet peut avoir.

### Interfaces avec classes

Nous pouvons dire à une classe qu'elle doit contenir certaines propriétés et méthodes en implémentant une interface :

```ts
interface HasFormatter {
  format(): string;
}

class Person implements HasFormatter {
  constructor(public username: string, protected password: string) {}

  format() {
    return this.username.toLocaleLowerCase();
  }
}

// Doit être des objets qui implémentent l'interface HasFormatter
let person1: HasFormatter;
let person2: HasFormatter;

person1 = new Person('Danny', 'password123');
person2 = new Person('Jane', 'TypeScripter1990');

console.log(person1.format()); // danny
```

Assurez-vous que `people` est un tableau d'objets qui implémentent `HasFormatter` (assure que chaque personne a la méthode format) :

```ts
let people: HasFormatter[] = [];
people.push(person1);
people.push(person2);
```

## Types littéraux en TypeScript

En plus des types généraux `string` et `number`, nous pouvons nous référer à des chaînes et des nombres spécifiques dans les positions de type :

```
// Type d'union avec un type littéral dans chaque position
let favouriteColor: 'red' | 'blue' | 'green' | 'yellow';

favouriteColor = 'blue';
favouriteColor = 'crimson'; // ERREUR : Le type '"crimson"' n'est pas assignable au type '"red" | "blue" | "green" | "yellow"'.
```

### Voici un scrim interactif pour vous aider à en apprendre davantage sur les types littéraux en TypeScript :

<iframe src="https://scrimba.com/scrim/coe7d49b596c09a2f4b75c73d?embed=freecodecamp,mini-header" width="100%" height="480"></iframe>

## Génériques

Les génériques vous permettent de créer un composant qui peut fonctionner sur une variété de types, plutôt que sur un seul, **ce qui aide à rendre le composant plus réutilisable.**

Passons par un exemple pour vous montrer ce que cela signifie...

La fonction `addID` accepte n'importe quel objet, et retourne un nouvel objet avec toutes les propriétés et valeurs de l'objet passé, plus une propriété `id` avec une valeur aléatoire entre 0 et 1000. En bref, elle donne un ID à n'importe quel objet.

```ts
 const addID = (obj: object) => {
  let id = Math.floor(Math.random() * 1000);

  return { ...obj, id };
};

let person1 = addID({ name: 'John', age: 40 });

console.log(person1.id); // 271
console.log(person1.name); // ERREUR : La propriété 'name' n'existe pas sur le type '{ id: number; }'.

```

Comme vous pouvez le voir, TypeScript donne une erreur lorsque nous essayons d'accéder à la propriété `name`. Cela est dû au fait que lorsque nous passons un objet à `addID`, nous ne spécifions pas quelles propriétés cet objet devrait avoir – donc TypeScript n'a aucune idée des propriétés que l'objet a (il ne les a pas "capturées"). Donc, la seule propriété que TypeScript connaît sur l'objet retourné est `id`.

Alors, comment pouvons-nous passer n'importe quel objet à `addID`, mais toujours dire à TypeScript quelles propriétés et valeurs l'objet a ? Nous pouvons utiliser un _générique_, `<T>` – où `T` est connu comme le _paramètre de type_ :

```ts
// <T> est juste la convention - par exemple, nous pourrions utiliser <X> ou <A>
const addID = <T>(obj: T) => {
  let id = Math.floor(Math.random() * 1000);

  return { ...obj, id };
};
```

Qu'est-ce que cela fait ? Eh bien, maintenant lorsque nous passons un objet dans `addID`, nous avons dit à TypeScript de capturer le type – donc `T` devient n'importe quel type que nous passons. `addID` saura maintenant quelles propriétés sont sur l'objet que nous passons.

Mais, nous avons maintenant un problème : n'importe quoi peut être passé dans `addID` et TypeScript capturera le type et ne signalera aucun problème :

```ts
let person1 = addID({ name: 'John', age: 40 });
let person2 = addID('Sally'); // Passer une chaîne - aucun problème

console.log(person1.id); // 271
console.log(person1.name); // John

console.log(person2.id);
console.log(person2.name); // ERREUR : La propriété 'name' n'existe pas sur le type '"Sally" & { id: number; }'.
```

Lorsque nous avons passé une chaîne, TypeScript n'a vu aucun problème. Il n'a signalé une erreur que lorsque nous avons essayé d'accéder à la propriété `name`. Donc, nous avons besoin d'une contrainte : nous devons dire à TypeScript que seuls les objets doivent être acceptés, en faisant de notre type générique, `T`, une extension de `object` :

```ts
const addID = <T extends object>(obj: T) => {
  let id = Math.floor(Math.random() * 1000);

  return { ...obj, id };
};

let person1 = addID({ name: 'John', age: 40 });
let person2 = addID('Sally'); // ERREUR : L'argument de type 'string' n'est pas assignable au paramètre de type 'object'.
```

L'erreur est détectée immédiatement – parfait... eh bien, pas tout à fait. En JavaScript, les tableaux sont des objets, donc nous pouvons encore nous en tirer en passant un tableau :

```ts
let person2 = addID(['Sally', 26]); // Passer un tableau - aucun problème

console.log(person2.id); // 824
console.log(person2.name); // Erreur : La propriété 'name' n'existe pas sur le type '(string | number)[] & { id: number; }'.
```

Nous pourrions résoudre cela en disant que l'argument objet devrait avoir une propriété name avec une valeur de chaîne :

```ts
const addID = <T extends { name: string }>(obj: T) => {
  let id = Math.floor(Math.random() * 1000);

  return { ...obj, id };
};

let person2 = addID(['Sally', 26]); // ERREUR : l'argument devrait avoir une propriété name avec une valeur de chaîne
```

Le type peut également être passé dans `<T>`, comme ci-dessous – mais cela n'est pas nécessaire la plupart du temps, car TypeScript l'inférera.

```ts
// Ci-dessous, nous avons explicitement précisé quel type l'argument devrait être entre les chevrons.
let person1 = addID<{ name: string; age: number }>({ name: 'John', age: 40 });
```

**Les génériques vous permettent d'avoir une sécurité de type dans les composants où les arguments et les types de retour sont inconnus à l'avance.**

**En TypeScript, les génériques sont utilisés lorsque nous voulons décrire une correspondance entre deux valeurs.** Dans l'exemple ci-dessus, le type de retour était lié au type d'entrée. Nous avons utilisé un _générique_ pour décrire la correspondance.

Un autre exemple : Si nous avons besoin d'une fonction qui accepte plusieurs types, il est préférable d'utiliser un générique plutôt que le type `any`. Ci-dessous montre le problème avec l'utilisation de `any` :

```ts
function logLength(a: any) {
  console.log(a.length); // Aucune erreur
  return a;
}

let hello = 'Hello world';
logLength(hello); // 11

let howMany = 8;
logLength(howMany); // undefined (mais aucune erreur TypeScript - sûrement nous voulons que TypeScript nous dise que nous avons essayé d'accéder à une propriété length sur un nombre !)
```

Nous pourrions essayer d'utiliser un générique :

```ts
function logLength<T>(a: T) {
  console.log(a.length); // ERREUR : TypeScript n'est pas certain que `a` est une valeur avec une propriété length
  return a;
}
```

Au moins nous obtenons maintenant un retour que nous pouvons utiliser pour resserrer notre code.

Solution : utiliser un générique qui étend une interface qui garantit que chaque argument passé a une propriété length :

```ts
interface hasLength {
  length: number;
}

function logLength<T extends hasLength>(a: T) {
  console.log(a.length);
  return a;
}

let hello = 'Hello world';
logLength(hello); // 11

let howMany = 8;
logLength(howMany); // Erreur : les nombres n'ont pas de propriétés length
```

Nous pourrions également écrire une fonction où l'argument est un tableau d'éléments qui ont tous une propriété length :

```ts
interface hasLength {
  length: number;
}

function logLengths<T extends hasLength>(a: T[]) {
  a.forEach((element) => {
    console.log(element.length);
  });
}

let arr = [
  'This string has a length prop',
  ['This', 'arr', 'has', 'length'],
  { material: 'plastic', length: 30 },
];

logLengths(arr);
// 29
// 4
// 30
```

Les génériques sont une fonctionnalité géniale de TypeScript !

### Génériques avec interfaces

Lorsque nous ne savons pas quel type une certaine valeur dans un objet aura à l'avance, nous pouvons utiliser un générique pour passer le type :

```ts
// Le type, T, sera passé
interface Person<T> {
  name: string;
  age: number;
  documents: T;
}

// Nous devons passer le type de `documents` - un tableau de chaînes dans ce cas
const person1: Person<string[]> = {
  name: 'John',
  age: 48,
  documents: ['passport', 'bank statement', 'visa'],
};

// Encore une fois, nous implémentons l'interface `Person`, et passons le type pour documents - dans ce cas une chaîne
const person2: Person<string> = {
  name: 'Delia',
  age: 46,
  documents: 'passport, P45',
};
```

## Énumérations en TypeScript

Les énumérations sont une fonctionnalité spéciale que TypeScript apporte à JavaScript. Les énumérations nous permettent de définir ou déclarer une collection de valeurs liées, qui peuvent être des nombres ou des chaînes, comme un ensemble de constantes nommées.

```ts
enum ResourceType {
  BOOK,
  AUTHOR,
  FILM,
  DIRECTOR,
  PERSON,
}

console.log(ResourceType.BOOK); // 0
console.log(ResourceType.AUTHOR); // 1

// Pour commencer à 1
enum ResourceType {
  BOOK = 1,
  AUTHOR,
  FILM,
  DIRECTOR,
  PERSON,
}

console.log(ResourceType.BOOK); // 1
console.log(ResourceType.AUTHOR); // 2
```

Par défaut, les énumérations sont basées sur des nombres – elles stockent des valeurs de chaîne sous forme de nombres. Mais elles peuvent également être des chaînes :

```ts
enum Direction {
  Up = 'Up',
  Right = 'Right',
  Down = 'Down',
  Left = 'Left',
}

console.log(Direction.Right); // Right
console.log(Direction.Down); // Down
```

Les énumérations sont utiles lorsque nous avons un ensemble de constantes liées. Par exemple, au lieu d'utiliser des nombres non descriptifs dans votre code, les énumérations rendent le code plus lisible avec des constantes descriptives. 

Les énumérations peuvent également prévenir les bugs, car lorsque vous tapez le nom de l'énumération, l'intellisense apparaît et vous donne la liste des options possibles qui peuvent être sélectionnées.

## Mode strict de TypeScript

Il est recommandé d'avoir toutes les opérations de vérification de type strict activées dans le fichier `tsconfig.json`. Cela fera que TypeScript signalera plus d'erreurs, mais aidera à prévenir de nombreux bugs de s'infiltrer dans votre application.

```ts
 // tsconfig.json
 "strict": true
```

Discutons de quelques-unes des choses que le mode strict fait : pas de any implicite, et des vérifications de null strictes.

### Pas de any implicite

Dans la fonction ci-dessous, TypeScript a inféré que le paramètre `a` est de type `any`. Comme vous pouvez le voir, lorsque nous passons un nombre à cette fonction, et essayons de logger une propriété `name`, aucune erreur n'est signalée. Pas bien.

```ts
function logName(a) {
  // Aucune erreur ??
  console.log(a.name);
}

logName(97);
```

Avec l'option `noImplicitAny` activée, TypeScript signalera immédiatement une erreur si nous ne précisons pas explicitement le type de `a` :

```ts
// ERREUR : Le paramètre 'a' a implicitement un type 'any'.
function logName(a) {
  console.log(a.name);
}
```

### Vérifications de null strictes

Lorsque l'option `strictNullChecks` est désactivée, TypeScript ignore effectivement `null` et `undefined`. Cela peut entraîner des erreurs inattendues à l'exécution.

Avec `strictNullChecks` défini sur true, `null` et `undefined` ont leurs propres types, et vous obtiendrez une erreur de type si vous les assigner à une variable qui attend une valeur concrète (par exemple, `string`).

```ts
let whoSangThis: string = getSong();

const singles = [
  { song: 'touch of grey', artist: 'grateful dead' },
  { song: 'paint it black', artist: 'rolling stones' },
];

const single = singles.find((s) => s.song === whoSangThis);

console.log(single.artist);

```

Ci-dessus, `singles.find` n'a aucune garantie qu'il trouvera la chanson – mais nous avons écrit le code comme s'il le ferait toujours.

En définissant `strictNullChecks` sur true, TypeScript signalera une erreur parce que nous n'avons pas garanti que `single` existe avant d'essayer de l'utiliser :

```ts
const getSong = () => {
  return 'song';
};

let whoSangThis: string = getSong();

const singles = [
  { song: 'touch of grey', artist: 'grateful dead' },
  { song: 'paint it black', artist: 'rolling stones' },
];

const single = singles.find((s) => s.song === whoSangThis);

console.log(single.artist); // ERREUR : L'objet est éventuellement 'undefined'.
```

TypeScript nous dit essentiellement de nous assurer que `single` existe avant de l'utiliser. Nous devons vérifier s'il n'est pas `null` ou `undefined` d'abord :

```ts
if (single) {
  console.log(single.artist); // rolling stones
}

```

## Rétrécissement en TypeScript

Dans un programme TypeScript, **une variable peut passer d'un type moins précis à un type plus précis.** Ce processus est appelé rétrécissement de type.

Voici un exemple simple montrant comment TypeScript rétrécit le type moins spécifique de `string | number` à des types plus spécifiques lorsque nous utilisons des instructions if avec `typeof` :

```ts
function addAnother(val: string | number) {
  if (typeof val === 'string') {
    // TypeScript traite `val` comme une chaîne dans ce bloc, donc nous pouvons utiliser des méthodes de chaîne sur `val` et TypeScript ne criera pas
    return val.concat(' ' + val);
  }

  // TypeScript sait que `val` est un nombre ici
  return val + val;
}

console.log(addAnother('Woooo')); // Woooo Woooo
console.log(addAnother(20)); // 40

```

Un autre exemple : ci-dessous, nous avons défini un type d'union appelé `allVehicles`, qui peut être soit de type `Plane` soit `Train`.

```ts
interface Vehicle {
  topSpeed: number;
}

interface Train extends Vehicle {
  carriages: number;
}

interface Plane extends Vehicle {
  wingSpan: number;
}

type PlaneOrTrain = Plane | Train;

function getSpeedRatio(v: PlaneOrTrain) {
  // Ici, nous voulons retourner topSpeed/carriages, ou topSpeed/wingSpan
  console.log(v.carriages); // ERREUR : 'carriages' n'existe pas sur le type 'Plane'
}

```

Puisque la fonction `getSpeedRatio` travaille avec plusieurs types, nous avons besoin d'un moyen de distinguer si `v` est un `Plane` ou un `Train`. Nous pourrions faire cela en donnant aux deux types une propriété distinctive commune, avec une valeur de chaîne littérale :

```ts
// Tous les trains doivent maintenant avoir une propriété type égale à 'Train'
interface Train extends Vehicle {
  type: 'Train';
  carriages: number;
}

// Tous les trains doivent maintenant avoir une propriété type égale à 'Plane'
interface Plane extends Vehicle {
  type: 'Plane';
  wingSpan: number;
}

type PlaneOrTrain = Plane | Train;
```

Maintenant, nous, et TypeScript, pouvons rétrécir le type de `v` :

```ts
function getSpeedRatio(v: PlaneOrTrain) {
  if (v.type === 'Train') {
    // TypeScript sait maintenant que `v` est définitivement un `Train`. Il a rétréci le type du type moins spécifique `Plane | Train`, au type plus spécifique `Train`
    return v.topSpeed / v.carriages;
  }

  // Si ce n'est pas un Train, TypeScript rétrécit que `v` doit être un Plane - intelligent !
  return v.topSpeed / v.wingSpan;
}

let bigTrain: Train = {
  type: 'Train',
  topSpeed: 100,
  carriages: 20,
};

console.log(getSpeedRatio(bigTrain)); // 5
```

## Bonus : TypeScript avec React

TypeScript prend entièrement en charge React et JSX. Cela signifie que nous pouvons utiliser TypeScript avec les trois frameworks React les plus courants : 

* create-react-app ([configuration TS](https://create-react-app.dev/docs/adding-typescript/))
* Gatsby ([configuration TS](https://www.gatsbyjs.com/docs/how-to/custom-configuration/typescript/))
* Next.js ([configuration TS](https://nextjs.org/learn/excel/typescript))

Si vous avez besoin d'une configuration React-TypeScript plus personnalisée, vous pourriez configurer [Webpack](https://webpack.js.org/) (un bundler de modules) et configurer le `tsconfig.json` vous-même. Mais la plupart du temps, un framework fera le travail.

Pour configurer create-react-app avec TypeScript, par exemple, exécutez simplement :

```ts
npx create-react-app my-app --template typescript

# ou

yarn create react-app my-app --template typescript
```

Dans le dossier src, nous pouvons maintenant créer des fichiers avec les extensions `.ts` (pour les fichiers TypeScript réguliers) ou `.tsx` (pour TypeScript avec React) et écrire nos composants avec TypeScript. Cela sera ensuite compilé en JavaScript dans le dossier public.

### Props React avec TypeScript

Ci-dessous, nous disons que `Person` devrait être un composant fonctionnel React qui accepte un objet props avec les props `name`, qui devrait être une chaîne, et `age`, qui devrait être un nombre.

```tsx
// src/components/Person.tsx
import React from 'react';

const Person: React.FC<{
  name: string;
  age: number;
}> = ({ name, age }) => {
  return (
    <div>
      <div>{name}</div>
      <div>{age}</div>
    </div>
  );
};

export default Person;

```

Mais la plupart des développeurs préfèrent utiliser une interface pour spécifier les types de props :

```tsx
interface Props {
  name: string;
  age: number;
}

const Person: React.FC<Props> = ({ name, age }) => {
  return (
    <div>
      <div>{name}</div>
      <div>{age}</div>
    </div>
  );
};
```

Nous pouvons ensuite importer ce composant dans `App.tsx`. Si nous ne fournissons pas les props nécessaires, TypeScript donnera une erreur.

```tsx
import React from 'react';
import Person from './components/Person';

const App: React.FC = () => {
  return (
    <div>
      <Person name='John' age={48} />
    </div>
  );
};

export default App;

```

Voici quelques exemples de ce que nous pourrions avoir comme types de props :

```tsx
interface PersonInfo {
  name: string;
  age: number;
}

interface Props {
  text: string;
  id: number;
  isVeryNice?: boolean;
  func: (name: string) => string;
  personInfo: PersonInfo;
}
```

### Hooks React avec TypeScript

#### useState()

Nous pouvons déclarer les types qu'une variable d'état devrait être en utilisant des chevrons. Ci-dessous, si nous omettons les chevrons, TypeScript inférera que `cash` est un nombre. Donc, si nous voulons lui permettre d'être également null, nous devons le spécifier :

```tsx
const Person: React.FC<Props> = ({ name, age }) => {
  const [cash, setCash] = useState<number | null>(1);

  setCash(null);

  return (
    <div>
      <div>{name}</div>
      <div>{age}</div>
    </div>
  );
};
```

#### useRef()

`useRef` retourne un objet mutable qui persiste pendant toute la durée de vie du composant. Nous pouvons dire à TypeScript à quoi l'objet ref devrait faire référence – ci-dessous nous disons que la prop devrait être un `HTMLInputElement` :

```tsx
const Person: React.FC = () => {
  // Initialiser la propriété .current à null
  const inputRef = useRef<HTMLInputElement>(null);

  return (
    <div>
      <input type='text' ref={inputRef} />
    </div>
  );
};
```

Pour plus d'informations sur React avec TypeScript, consultez ces [superbes feuilles de triche React-TypeScript](https://react-typescript-cheatsheet.netlify.app/).

## Ressources utiles et lectures complémentaires

* [La documentation officielle de TypeScript](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)
* [La série vidéo TypeScript de The Net Ninja](https://www.youtube.com/watch?v=2pZmKW9-I_k&list=PL4cUxeGkcC9gUgr39Q_yD6v-bSyMwKPUI&ab_channel=TheNetNinja) (géniale !)
* [La vidéo TypeScript avec React de Ben Awad](https://www.youtube.com/watch?v=Z5iWr6Srsj8&ab_channel=BenAwad)
* [Le rétrécissement en TypeScript](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) (une fonctionnalité très intéressante de TS que vous devriez apprendre)
* [Les surcharges de fonction](https://www.typescriptlang.org/docs/handbook/2/functions.html#function-overloads)
* [Les valeurs primitives en JavaScript](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
* [Les objets JavaScript](https://www.w3schools.com/js/js_object_definition.asp)

## Merci d'avoir lu !

J'espère que cela a été utile. Si vous êtes arrivé jusqu'ici, vous connaissez maintenant les principes fondamentaux de TypeScript et pouvez commencer à l'utiliser dans vos projets.

Encore une fois, vous pouvez également télécharger ma [feuille de triche TypeScript PDF d'une page](https://doabledanny.gumroad.com/l/typescript-cheat-sheet-pdf) ou [commander une affiche physique](https://doabledanny.gumroad.com/l/typescript-cheat-sheet-poster).

Pour plus de contenu de ma part, vous pouvez me trouver sur [Twitter](https://mobile.twitter.com/doabledanny) et [YouTube](https://www.youtube.com/channel/UC0URylW_U4i26wN231yRqvA).

À bientôt !