---
title: Un cours accéléré sur TypeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-30T22:31:53.000Z'
originalURL: https://freecodecamp.org/news/a-crash-course-in-typescript-e6bf9c10946
coverImage: https://cdn-media-1.freecodecamp.org/images/0*DKOL70niXLTiAr5x
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: Un cours accéléré sur TypeScript
seo_desc: 'By Gabriel Tanner

  Typescript is a typed superset of javascript which aims to ease the development
  of large javascript applications. Typescript adds common concepts such as classes,
  generics, interfaces and static types and allows developers to use to...'
---

Par Gabriel Tanner

TypeScript est un sur-ensemble typé de JavaScript qui vise à faciliter le développement de grandes applications JavaScript. TypeScript ajoute des concepts courants tels que les classes, les génériques, les interfaces et les types statiques, et permet aux développeurs d'utiliser des outils comme la vérification statique et le refactoring de code.

### Pourquoi se soucier de TypeScript :

Maintenant, la question reste de savoir pourquoi vous devriez utiliser TypeScript en premier lieu. Voici quelques raisons pour lesquelles les développeurs JavaScript devraient envisager d'apprendre TypeScript.

#### Typage statique :

JavaScript est typé dynamiquement, ce qui signifie qu'il ne connaît pas le type de votre variable jusqu'à ce qu'il l'instancie à l'exécution, ce qui peut causer des problèmes et des erreurs dans vos projets. TypeScript ajoute la prise en charge des types statiques à JavaScript, ce qui prend en charge les bugs causés par une mauvaise hypothèse sur le type d'une variable si vous l'utilisez correctement. Vous avez toujours un contrôle total sur la rigidité avec laquelle vous tapez votre code ou même si vous utilisez des types du tout.

#### Meilleure prise en charge de l'IDE :

L'un des plus grands avantages de TypeScript par rapport à JavaScript est la grande prise en charge de l'IDE, qui inclut Intellisense, des informations en temps réel du compilateur TypeScript, le débogage et bien plus encore. Il existe également quelques excellentes extensions pour améliorer davantage votre expérience de développement TypeScript.

#### Accès aux nouvelles fonctionnalités ECMAScript :

TypeScript vous donne accès aux dernières fonctionnalités ECMAScript et les transcrit aux cibles ECMAScript de votre choix. Cela signifie que vous pouvez développer vos applications en utilisant les derniers outils sans avoir à vous soucier de la compatibilité des navigateurs.

### Quand l'utiliser :

À présent, nous devrions savoir pourquoi TypeScript est utile et où il peut améliorer notre expérience de développement. Mais ce n'est pas la solution à tout et ne vous empêche certainement pas d'écrire un code terrible par lui-même. Alors, voyons où vous devriez définitivement utiliser TypeScript.

#### Quand vous avez une grande base de code :

TypeScript est un excellent ajout à une grande base de code car il vous aide à prévenir de nombreuses erreurs courantes. Cela s'applique particulièrement si plusieurs développeurs travaillent sur un seul projet.

#### Quand vous et votre équipe connaissez déjà les langages typés statiquement :

Une autre situation évidente pour utiliser TypeScript est lorsque vous et votre équipe connaissez déjà des langages typés statiquement comme Java et C# et ne voulez pas passer à l'écriture de JavaScript.

### Installation :

Pour installer TypeScript, nous devons simplement l'installer avec le gestionnaire de paquets npm et créer un nouveau fichier TypeScript.

```
npm install -g typescript
```

Après l'avoir installé, nous pouvons continuer à examiner la syntaxe et les fonctionnalités que TypeScript nous offre.

### Types :

Maintenant, examinons quels types sont disponibles pour nous dans TypeScript.

#### Nombre :

Tous les nombres dans TypeScript sont des valeurs à virgule flottante. Tous reçoivent le type nombre, y compris les valeurs binaires et hexadécimales.

```typescript
let num: number = 0.222;
let hex: number = 0xbeef;
let bin: number = 0b0010;
```

#### Chaîne de caractères :

Comme dans d'autres langages, TypeScript utilise le type de données String pour sauvegarder des données textuelles.

```
let str: string = 'Hello World!';
```

Vous pouvez également utiliser une chaîne de caractères multilingue et intégrer des expressions en entourant votre chaîne de caractères avec des backticks ``

```js
let multiStr: string = `A simple
multiline string!`
let expression = 'A new expression'
let expressionStr: string = `Expression str: ${ expression }`
```

#### Booléen :

TypeScript prend également en charge le type de données le plus basique de tous, le booléen, qui ne peut être que vrai ou faux.

```js
let boolFalse: boolean = false;
let boolTrue: boolean = true;
```

### Attribution de types :

Maintenant que nous avons les types de données de base, nous pouvons voir comment vous attribuez des types dans TypeScript. Basiquement, vous devez simplement écrire le type de votre variable après le nom et un deux-points.

#### Type unique :

Voici un exemple où nous attribuons le type de données String à notre variable :

```
let str: string = 'Hello World'
```

C'est la même chose avec tous les types de données.

#### Types multiples :

Vous pouvez également attribuer plusieurs types de données à vos variables en utilisant l'opérateur |.

```js
let multitypeVar: string | number = 'String'
multitypeVar = 20
```

Ici, nous attribuons deux types à notre variable en utilisant l'opérateur |. Maintenant, nous pouvons y stocker des chaînes de caractères et des nombres.

### Vérification des types :

Maintenant, voyons comment nous pouvons vérifier si notre variable a le bon type. Nous avons plusieurs options pour le faire, mais ici je ne montre que deux des plus utilisées.

#### Typeof :

La commande _typeof_ ne connaît que les types de données de base. Cela signifie qu'elle ne peut vérifier que si la variable est l'un des types de données que nous avons définis ci-dessus.

```js
let str: string = 'Hello World!'
if(typeof str === number){
 console.log('Str est un nombre')
} else {
 console.log('Str n\'est pas un nombre')
}
```

Dans cet exemple, nous créons une variable de type chaîne de caractères et utilisons la commande _typeof_ pour vérifier si str est de type nombre (ce qui est toujours faux). Ensuite, nous imprimons si c'est un nombre ou non.

#### Instanceof :

L'opérateur instanceof est presque le même que typeof sauf qu'il peut également vérifier les types personnalisés qui ne sont pas déjà définis par JavaScript.

```js
class Human{
 name: string;
 constructor(data: string) {
  this.name = data;
 }
}
let human = new Human('Gabriel')
if(human instanceof Human){
 console.log(`${human.name} est un humain`)
}
```

Ici, nous créons un type personnalisé que nous discuterons plus tard dans cet article, puis créons une instance de celui-ci. Après cela, nous vérifions si c'est vraiment une variable de type Human et imprimons dans la console si c'est le cas.

### Assertions de type :

Parfois, nous devrons également convertir nos variables en un type de données spécifique. Cela se produit souvent lorsque vous avez attribué un type général comme any et que vous souhaitez utiliser des fonctions du type concret.

Il existe plusieurs options pour résoudre ce problème, mais ici je partage simplement deux d'entre elles.

#### Mot-clé As :

Nous pouvons facilement convertir notre variable en utilisant le mot-clé as après le nom de la variable et le suivre avec le type de données.

```js
let str: any = 'I am a String'
let strLength = (str as string).length
```

Ici, nous convertissons notre variable str en String afin de pouvoir utiliser le paramètre length. (Cela pourrait même fonctionner sans la conversion si vos paramètres TSLINT le permettent)

#### Opérateur <> :

Nous pouvons également utiliser l'opérateur <> qui a exactement le même effet que le mot-clé avec juste une différence de syntaxe.

```js
let str: any = 'I am a String'
let strLength = (<string>str).length
```

Ce bloc de code a exactement la même fonctionnalité que le bloc de code ci-dessus. Il ne diffère que par la syntaxe.

### Tableaux :

Les tableaux dans TypeScript sont des collections des mêmes objets et peuvent être créés de deux manières différentes.

#### Création de tableaux

**En utilisant [] :**

Nous pouvons définir un tableau d'un objet en écrivant le type suivi de [] pour indiquer qu'il s'agit d'un tableau.

```
let strings: string[] = ['Hello', 'World', '!']
```

Dans cet exemple, nous créons un tableau de chaînes de caractères qui contient trois valeurs de chaînes de caractères différentes.

**En utilisant le type de tableau générique :**

Nous pouvons également définir un tableau en utilisant le type générique en écrivant Array<Type>.

```
let numbers: Array<number> = [1, 2, 3, 4, 5]
```

Ici, nous créons un tableau de nombres qui contient 5 valeurs de nombres différentes.

#### Tableaux multitypes :

De plus, nous pouvons également attribuer plusieurs types à un seul tableau en utilisant l'opérateur |.

```
let stringsAndNumbers: (string | number)[] = ['Age', 20]
```

Dans cet exemple, nous avons créé un tableau qui peut contenir des valeurs de chaînes de caractères et de nombres.

#### Tableau multidimensionnel :

TypeScript nous permet également de définir des tableaux multidimensionnels, ce qui signifie que nous pouvons sauvegarder un tableau dans un autre tableau. Nous pouvons créer un tableau multidimensionnel en utilisant plusieurs opérateurs [] les uns après les autres.

```
let numbersArray: number[][] = [[1,2,3,4,5], [6,7,8,9,10]]
```

Ici, nous créons un tableau qui contient un autre tableau de nombres.

### Tuples :

Les tuples sont essentiellement comme un tableau avec une différence clé. Nous pouvons définir quel type de données peut être stocké dans chaque position. Cela signifie que nous pouvons imposer des types pour les index en les énumérant à l'intérieur de crochets carrés.

```
let exampleTuple: [number, string] = [20, 'https://google.com'];
```

Dans cet exemple, nous créons un tuple simple avec un nombre à l'index 0 et une chaîne de caractères à l'index 1. Cela signifie qu'il générerait une erreur si nous essayions de placer un autre type de données à cet index.

Voici un exemple de tuple invalide :

```
const exampleTuple: [string, number] = [20, 'https://google.com'];
```

### Énumérations :

Les énumérations dans TypeScript, comme dans la plupart des autres langages de programmation orientés objet, nous permettent de définir un ensemble de constantes nommées. TypeScript fournit également des énumérations numériques et basées sur des chaînes de caractères. Les énumérations dans TypeScript sont définies en utilisant le mot-clé enum.

#### Numérique :

Tout d'abord, nous allons examiner les énumérations numériques où nous associons une valeur clé à un index.

```js
enum State{
 Playing = 0,
 Paused = 1,
 Stopped = 2
}
```

Ci-dessus, nous définissons une énumération numérique où Playing est initialisé avec 0, Paused avec 1 et ainsi de suite.

```js
enum State{
 Playing,
 Paused,
 Stopped
}
```

Nous pourrions également laisser les initialisateurs vides et TypeScript les indexerait automatiquement en commençant par zéro.

#### Chaîne de caractères :

Définir une énumération de chaînes de caractères dans TypeScript est assez facile — nous devons simplement initialiser nos valeurs avec des chaînes de caractères.

```js
enum State{
 Playing = 'PLAYING',
 Paused = 'PAUSED',
 Stopped = 'STOPPED'
}
```

Ici, nous définissons une énumération de chaînes de caractères en initialisant nos États avec des chaînes de caractères.

### Objets :

Un objet dans TypeScript est une instance qui contient un ensemble de paires clé-valeur. Ces valeurs peuvent être des variables, des tableaux ou même des fonctions. Il est également considéré comme le type de données qui représente les types non primitifs.

Nous pouvons créer des objets en utilisant des accolades.

```js
const human = {
 firstName: 'Frank',
 age: 32,
 height: 185
};
```

Ici, nous créons un objet humain qui a trois paires clé-valeur différentes.

Nous pouvons également ajouter des fonctions à notre objet :

```js
const human = {
 firstName: 'Frank',
 age: 32,
 height: 185,
 greet: function(){
  console.log("Greetings stranger!")
 }
};
```

### Types personnalisés :

TypeScript nous permet également de définir des types personnalisés appelés alias que nous pouvons facilement réutiliser plus tard. Pour créer un type personnalisé, nous devons simplement utiliser le mot-clé type et définir notre type.

```
type Human = {firstName: string, age: number, height: number}
```

Dans cet exemple, nous définissons un type personnalisé avec le nom Human et trois propriétés. Maintenant, voyons comment nous pouvons créer un objet de ce type.

```
const human: Human = {firstName: 'Franz', age: 32, height: 185}
```

Ici, nous créons une instance de notre type personnalisé et définissons les propriétés requises.

### Paramètres de fonction et types de retour :

TypeScript nous permet de définir les types pour nos paramètres de fonction et notre type de retour. Maintenant, examinons la syntaxe pour définir une fonction en utilisant TypeScript.

```js
function printState(state: State): void {
 console.log(`The song state is ${state}`)
}
function add(num1: number, num2: number): number {
 return num1 + num2
}
```

Ici, nous avons deux fonctions d'exemple qui ont toutes deux des paramètres avec des types définis. Nous voyons également que nous définissons le type de retour après les parenthèses fermantes.

Maintenant, nous pouvons appeler notre fonction comme en JavaScript normal, mais le compilateur vérifiera si nous fournissons à la fonction les bons paramètres.

```js
add(2, 5)
add(1) // Erreur, trop peu de paramètres
add(5, '2') // Erreur, le deuxième argument doit être de type nombre
```

#### Propriétés optionnelles :

TypeScript nous permet également de définir des propriétés optionnelles pour notre fonction. Nous pouvons le faire en utilisant l'opérateur Elvis ?. Voici un exemple simple :

```
function printName(firstName: string, lastName?: string) {
if (lastName) 
 console.log(`Firstname: ${firstName}, Lastname: ${lastName}`);
else console.log(`Firstname: ${firstName}`);
}
```

Dans cet exemple, lastName est un paramètre optionnel, ce qui signifie que nous n'obtiendrons pas d'erreur du compilateur lorsque nous ne le fournissons pas en appelant la fonction.

```
printName('Gabriel', 'Tanner')
printName('Gabriel')
```

Cela signifie que ces deux cas seraient considérés comme corrects.

#### Valeurs par défaut :

La deuxième méthode que nous pouvons utiliser pour rendre une propriété optionnelle est de lui attribuer une valeur par défaut. Nous pouvons le faire en attribuant la valeur directement dans l'en-tête de la fonction.

```js
function printName(firstName: string, lastName: string = 'Tanner') {
 console.log(`Firstname: ${firstName}, Lastname: ${lastName}`);
}
```

Dans cet exemple, nous avons attribué une valeur par défaut à lastName, ce qui signifie que nous n'avons pas besoin de la fournir chaque fois que nous appelons la fonction.

### Interfaces :

Les interfaces dans TypeScript sont utilisées pour définir des contrats avec notre code ainsi qu'avec le code extérieur à notre projet. Les interfaces ne contiennent que les déclarations de nos méthodes et propriétés, mais ne les implémentent pas. L'implémentation des méthodes et propriétés est la responsabilité de la classe qui implémente l'interface.

Regardons un exemple pour clarifier ces déclarations :

```js
interface Person{
 name: string
}
const person: Person = {name: 'Gabriel'}
const person2: Person = {names: 'Gabriel'} // n'est pas assignable au type Person
```

Ici, nous créons une interface avec une propriété qui doit être implémentée lorsque nous implémentons l'interface. C'est pourquoi la deuxième variable person générera une erreur.

#### Propriétés optionnelles :

Dans TypeScript, toutes les propriétés d'une interface n'ont pas besoin d'être requises. Les propriétés peuvent également être définies comme optionnelles en utilisant l'opérateur ? après le nom de la propriété.

```js
interface Person{
 name: string
 age?: number
}
const person: Person = {name: 'Frank', age: 28}
const person2: Person = {name: 'Gabriel'}
```

Ici, nous créons une interface avec une propriété normale et une propriété optionnelle qui est définie en utilisant l'opérateur ?. C'est pourquoi les deux initialisations de person sont valides.

#### Propriétés en lecture seule :

Certaines propriétés de notre interface ne doivent également être modifiées que lorsque l'objet est créé pour la première fois. Nous pouvons spécifier cette fonctionnalité en plaçant le mot-clé _readonly_ avant le nom de notre propriété.

```js
interface Person{
 name: string
 readonly id: number
 age?: number
}
const person: Person = {name: 'Gabriel', id: 3127831827}
person.id = 200 // Impossible d'assigner à id car il est en lecture seule
```

Dans cet exemple, la propriété id est en lecture seule et ne peut pas être modifiée après la création d'un objet.

### Barils :

Les barils nous permettent de regrouper plusieurs modules d'exportation dans un seul module plus pratique.

Nous devons simplement créer un nouveau fichier qui exportera plusieurs modules de notre projet.

```js
export * from './person';
export * from './animal';
export * from './human';
```

Après avoir fait cela, nous pouvons importer tous ces modules en utilisant une seule instruction d'importation pratique.

```
import { Person, Animal, Human } from 'index';
```

### Génériques :

Les génériques nous permettent de créer des composants qui sont compatibles avec une grande variété de types plutôt qu'avec un seul. Cela nous aide à rendre notre composant « ouvert » et réutilisable.

Maintenant, vous vous demandez peut-être pourquoi nous n'utilisons pas simplement le type any pour accepter plus d'un seul type pour notre composant. Regardons un exemple pour mieux comprendre la situation.

Nous voulons une fonction factice simple qui retourne le paramètre qui lui a été passé.

```js
function dummyFun(arg: any): any {
 return arg;
}
```

Bien que any soit générique dans le sens où il accepte tous les types pour l'argument, il a une grande différence. Nous perdons l'information sur le type qui a été passé et retourné de la fonction.

Alors, voyons comment nous pouvons accepter tous les types tout en connaissant le type qu'il retourne.

```js
function dummyFun<T>(arg: T): T {
 return arg
}
```

Ici, nous avons utilisé le paramètre générique T afin de capturer le type de variable et de l'utiliser plus tard. Nous l'utilisons également comme notre paramètre de retour, ce qui nous permet de voir le type correspondant lorsque nous inspectons le code.

Pour une explication plus détaillée des génériques, vous pouvez consulter l'article de [Charly Poly](https://www.freecodecamp.org/news/a-crash-course-in-typescript-e6bf9c10946/undefined) sur les [Génériques et surcharges](https://medium.com/@wittydeveloper/typescript-generics-and-overloads-999679d121cf).

### Modificateurs d'accès :

Les modificateurs d'accès contrôlent l'accessibilité des membres de nos classes. TypeScript prend en charge trois modificateurs d'accès — public, private et protected.

#### **Public :**

Les membres publics sont disponibles de partout sans aucune restriction. Il s'agit également du modificateur standard, ce qui signifie que vous n'avez pas besoin de préfixer les variables avec le mot-clé public.

#### **Private :**

Les membres privés ne peuvent être accessibles que dans la classe où ils sont définis.

#### Protected :

Les membres protégés ne peuvent être accessibles que dans la classe où ils sont définis et dans chaque sous-classe/classe enfant.

### TSLINT :

TSLINT est le linter standard pour TypeScript et peut nous aider à écrire un code propre, maintenable et lisible. Il peut être personnalisé avec nos propres règles de lint, configurations et formateurs.

#### Installation :

Tout d'abord, nous devons installer TypeScript et TSLINT, nous pouvons le faire localement ou globalement :

```js
npm install tslint typescript --save-dev
npm install tslint typescript -g
```

Après cela, nous pouvons utiliser l'interface de ligne de commande TSLINT pour initialiser TSLINT dans notre projet.

```
tslint --init
```

Maintenant que nous avons notre fichier _tslint.json_, nous sommes prêts à commencer à configurer nos règles.

#### Configuration :

TSLINT nous permet de configurer nos propres règles et de personnaliser l'apparence de notre code. Par défaut, le fichier tslint.json ressemble à ceci et utilise simplement les règles par défaut.

```js
{
"defaultSeverity": "error",
"extends": [
 "tslint:recommended"
],
"jsRules": {},
"rules": {},
"rulesDirectory": []
}
```

Nous pouvons ajouter d'autres règles en les plaçant dans l'objet rules.

```js
"rules": {
 "no-unnecessary-type-assertion": true,
 "array-type": [true, "array"],
 "no-double-space": true,
 "no-var-keyword": true,
 "semicolon": [true, "always", "ignore-bound-class-methods"]
},
```

Pour un aperçu de toutes les règles disponibles, vous pouvez consulter la [documentation officielle](https://palantir.github.io/tslint/rules/).

#### Lectures recommandées :

[**Une introduction au DOM JavaScript**](https://medium.freecodecamp.org/an-introduction-to-the-javascript-dom-512463dd62ec)  
[_Le DOM JavaScript (Document Object Model) est une interface qui permet aux développeurs de manipuler le contenu, la structure..._medium.freecodecamp.org](https://medium.freecodecamp.org/an-introduction-to-the-javascript-dom-512463dd62ec)

### Conclusion

Vous avez réussi jusqu'à la fin ! J'espère que cet article vous a aidé à comprendre les bases de TypeScript et comment vous pouvez l'utiliser dans vos projets.

Si vous souhaitez lire plus d'articles comme celui-ci, vous pouvez visiter mon [site web](https://gabrieltanner.org/) ou commencer à suivre ma [newsletter](https://gabrieltanner.us20.list-manage.com/subscribe/post?u=9d67fc028348a0eb71318768e&id=6845ed3555).

Si vous avez des questions ou des commentaires, faites-le moi savoir dans les commentaires ci-dessous.