---
title: Apprendre TypeScript – Un guide complet pour les débutants
subtitle: ''
author: Isaiah Clifford Opoku
co_authors: []
series: null
date: '2024-08-08T16:45:28.000Z'
originalURL: https://freecodecamp.org/news/typescript-for-beginners-guide
coverImage: https://www.freecodecamp.org/news/content/images/2024/08/Attractive.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: Apprendre TypeScript – Un guide complet pour les débutants
seo_desc: 'TypeScript has become an industry standard for building large-scale applications,
  with many organizations choosing it as their primary language for application development.

  This tutorial will serve as your introductory guide to TypeScript. It''s desig...'
---

TypeScript est devenu une norme industrielle pour la construction d'applications à grande échelle, de nombreuses organisations le choisissant comme langage principal pour le développement d'applications.

Ce tutoriel servira de guide d'introduction à TypeScript. Il est conçu pour répondre aux besoins des apprenants à tous les niveaux – des débutants aux utilisateurs avancés. Il enseigne à la fois les concepts fondamentaux et avancés de TypeScript, ce qui en fait une ressource utile pour toute personne souhaitant se plonger dans TypeScript.

Le but de ce guide n'est pas d'être une ressource exhaustive, mais plutôt une référence concise et pratique. Il distille l'essence de TypeScript dans un format digestible.

Que vous soyez un novice qui commence tout juste, un apprenant intermédiaire cherchant à consolider vos connaissances, ou un utilisateur avancé ayant besoin d'un rappel rapide, ce guide est conçu pour répondre à vos besoins d'apprentissage de TypeScript.

Après avoir lu attentivement ce tutoriel et pratiqué les exemples qu'il contient, vous devriez avoir les compétences nécessaires pour construire des applications TypeScript robustes, évolutives et maintenables. Nous aborderons les concepts clés de TypeScript tels que les types, les fonctions, les classes, les interfaces, les génériques, et bien plus encore.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [À qui s'adresse ce guide ?](#heading-a-qui-sadresse-ce-guide)
    
* [TypeScript vs. JavaScript](#heading-typescript-vs-javascript)
    
* [Avantages de TypeScript](#heading-avantages-de-typescript)
    
* [Génération de code](#heading-generation-de-code)
    
* [Installation](#heading-installation)
    
* [Configuration](#heading-configuration)
    
* [Comprendre tsconfig.json](#heading-comprendre-tsconfig-json)
    
* [Bases de TypeScript](#heading-bases-de-typescript)
    
* [Déclarations de types et variables dans TypeScript](#heading-declarations-de-types-et-variables-dans-typescript)
    
* [Fonctions dans TypeScript](#heading-fonctions-dans-typescript)
    
* [Classes et objets dans TypeScript](#heading-classes-et-objets-dans-typescript)
    
* [Interfaces dans TypeScript](#heading-interfaces-dans-typescript)
    
* [Énumérations dans TypeScript](#heading-enumerations-dans-typescript)
    
* [Génériques dans TypeScript](#heading-generiques-dans-typescript)
    

## Prérequis

Avant de commencer à parcourir ce guide, vous devriez avoir une compréhension de base de JavaScript. La familiarité avec les concepts de programmation orientée objet tels que les classes, les interfaces et l'héritage est également recommandée.

Mais si vous êtes nouveau dans ces concepts, ne vous inquiétez pas - nous les aborderons en détail dans ce guide.

## À qui s'adresse ce guide ?

Ce guide est destiné à toute personne souhaitant apprendre TypeScript. Que vous soyez débutant, apprenant intermédiaire ou utilisateur avancé, ce guide est conçu pour répondre à vos besoins d'apprentissage de TypeScript.

C'est également une référence pratique pour toute personne souhaitant rafraîchir ses compétences en TypeScript.

## TypeScript vs JavaScript

TypeScript est un sur-ensemble de JavaScript à typage statique, conçu pour améliorer le développement d'applications à grande échelle.

Il introduit le `typage statique` optionnel, les `classes` et les `interfaces` à `JavaScript`, établissant des parallèles avec des langages comme `C#` et `Java`. Le code TypeScript est transpilé en JavaScript simple, assurant la compatibilité dans divers environnements JavaScript.

Bien que TypeScript et JavaScript puissent fonctionner dans le même environnement, ils présentent des différences clés. La principale est que TypeScript est à typage statique, offrant une sécurité de type, tandis que JavaScript est à typage dynamique.

Explorons certaines de ces différences :

Le code TypeScript est écrit dans des fichiers `.ts` ou `.tsx`, tandis que le code JavaScript réside dans des fichiers `.js` ou `.jsx`. Les extensions `.tsx` et `.jsx` indiquent que le fichier peut contenir la syntaxe JSX, un choix populaire pour le développement d'interfaces utilisateur dans des bibliothèques comme React.

Explorons les différences entre JavaScript et TypeScript à travers un exemple :

```js
// JavaScript
function add(a, b) {
  return a + b;
}

// Appel de la fonction
add(1, 2); // Retourne : 3
```

Dans l'exemple JavaScript ci-dessus, la fonction `add` prend deux paramètres, `a` et `b`, et retourne leur somme. La fonction est appelée avec les arguments `1` et `2`, donnant `3`. Remarquez que les paramètres de la fonction ne sont pas annotés avec des types, ce qui est typique en JavaScript.

Maintenant, voyons comment nous pouvons écrire la même fonction en TypeScript :

```ts
// TypeScript
function add(a: number, b: number): number {
  return a + b;
}

// Appel de la fonction
add(1, 2); // Retourne : 3
```

Dans la version TypeScript, nous avons annoté les paramètres `a` et `b` avec le type `number`. Nous avons également spécifié que la fonction retourne un `number`.

C'est une différence clé entre JavaScript et TypeScript. TypeScript impose la sécurité des types, ce qui signifie qu'il vérifie les types des valeurs au moment de la compilation et génère des erreurs si elles ne correspondent pas aux types attendus.

Cette fonctionnalité aide à détecter les erreurs tôt dans le processus de développement, faisant de TypeScript un choix populaire pour les applications à grande échelle.

TypeScript et JavaScript sont tous deux des langages puissants utilisés dans une large gamme d'applications. Résumons leurs principales différences :

| Fonctionnalité | TypeScript | JavaScript |
| --- | --- | --- |
| Système de types | Typage statique (les types sont vérifiés au moment de la compilation) | Typage dynamique (les types sont vérifiés à l'exécution) |
| Sur-ensemble | Oui, TypeScript est un sur-ensemble de JavaScript | N/A |
| Compilation | Doit être compilé (ou transpilé) en JavaScript | N'a pas besoin d'être compilé |
| Fonctionnalités OOP | Inclut des fonctionnalités OOP avancées telles que les interfaces, les génériques et les décorateurs | Prend en charge l'OOP via des prototypes, ne prend pas en charge nativement les interfaces ou les génériques |
| Outillage | Offre un meilleur outillage avec autocomplétion, vérification de type et prise en charge des cartes sources | Outillage de base |
| Communauté et écosystème | Plus récent, communauté et écosystème plus petits | Grande communauté et vaste écosystème de bibliothèques et de frameworks depuis 1995 |
| Courbe d'apprentissage | Plus raide en raison des fonctionnalités supplémentaires | Généralement plus facile pour les débutants |
| Cas d'utilisation | Typiquement utilisé dans des bases de code plus grandes où les avantages de la vérification de type et de l'autocomplétion sont les plus notables | Utilisé pour le développement côté client et côté serveur, peut être exécuté nativement dans le navigateur |

## Avantages de TypeScript

TypeScript offre plusieurs avantages par rapport à JavaScript :

2. **Outillage amélioré** : Le typage statique de TypeScript permet une meilleure prise en charge de l'outillage. Des fonctionnalités comme l'`autocomplétion`, l'`inférence de type` et la vérification de type rendent le processus de développement plus efficace et agréable.
    
3. **Meilleure documentation** : Les bases de code TypeScript sont souvent plus faciles à comprendre et à maintenir. Les annotations de type servent de documentation implicite, facilitant la compréhension des types de valeurs qu'une fonction attend et retourne.
    
4. **Fonctionnalités avancées** : TypeScript prend en charge les fonctionnalités avancées de JavaScript telles que les `décorateurs` et `async/await`, et introduit également des fonctionnalités non disponibles en JavaScript, telles que les `interfaces`, les `énumérations` et les `tuples`.
    
5. **Refactoring** : L'outillage de TypeScript rend le refactoring de grandes bases de code plus sûr et plus prévisible. Vous pouvez apporter des modifications à grande échelle en toute confiance.
    
6. **Adoption progressive** : TypeScript est un sur-ensemble de JavaScript, ce qui signifie que vous pouvez adopter progressivement TypeScript dans vos projets. Vous pouvez commencer par renommer vos fichiers `.js` en `.ts` puis ajouter progressivement des annotations de type selon vos besoins.
    
7. **Communauté et écosystème** : TypeScript dispose d'une communauté et d'un écosystème en croissance. De nombreuses bibliothèques JavaScript populaires, telles que React et Angular, disposent de définitions TypeScript, ce qui facilite leur utilisation dans un projet TypeScript.
    

## Génération de code

Le code TypeScript n'est pas compris nativement par les navigateurs ou Node.js, il doit donc être transpilé en JavaScript. Ce processus de transpilation est géré par le compilateur TypeScript (`tsc`), qui lit le code TypeScript et génère le code JavaScript équivalent.

Pour transpiler un fichier TypeScript, vous pouvez utiliser la commande `tsc` suivie du nom du fichier :

```bash
$ tsc index.ts
```

Cette commande transpile le fichier `index.ts` en un fichier `index.js` dans le même répertoire. Le code JavaScript résultant peut être exécuté dans n'importe quel environnement JavaScript, tel qu'un navigateur ou Node.js.

### Surveillance des modifications de fichiers

Pendant le développement actif, il est bénéfique d'avoir votre code TypeScript automatiquement recompilé chaque fois que vous apportez des modifications. Le compilateur TypeScript fournit une option `--watch` à cet effet :

```shell
$ tsc index.ts --watch
```

Avec cette commande, le compilateur surveillera le fichier `index.ts` et le recompilera automatiquement chaque fois qu'il détectera une modification.

### Configuration du compilateur TypeScript

Pour les projets plus importants, il est courant d'avoir un fichier de configuration, `tsconfig.json`, pour gérer les options du compilateur. Ce fichier vous permet de spécifier les fichiers de niveau racine et les options du compilateur nécessaires pour compiler le projet.

Voici un exemple de fichier `tsconfig.json` :

```json
{
  "compilerOptions": {
    "target": "es5",
    "module": "commonjs",
    "strict": true,
    "outDir": "./dist"
  },
  "include": ["src/**/*.ts"],
  "exclude": ["node_modules"]
}
```

Dans cette configuration, l'objet `compilerOptions` contient des options pour le compilateur. L'option `target` spécifie la version cible d'ECMAScript, l'option `module` définit le système de modules, l'option `strict` active une large gamme de comportements de vérification de type, et l'option `outDir` spécifie le répertoire de sortie pour les fichiers JavaScript compilés.

Les options `include` et `exclude` sont utilisées pour spécifier les fichiers à inclure et à ignorer, respectivement.

Pour compiler le projet en fonction du fichier `tsconfig.json`, vous pouvez exécuter la commande `tsc` sans aucun argument :

```bash
$ tsc
```

Cette commande compilera tous les fichiers TypeScript du projet selon les options spécifiées dans le fichier `tsconfig.json`.

## Bases de TypeScript

Dans cette section, nous allons passer en revue les bases de TypeScript. Vous verrez plus d'exemples de la façon dont TypeScript est à typage statique, et vous en apprendrez davantage sur son outillage et sa vérification des erreurs.

### Installation

Avant de plonger dans TypeScript, vous devez vous assurer que Node.js est installé sur votre système. `Node.js` est un environnement d'exécution qui vous permet d'exécuter JavaScript en dehors du navigateur. Vous pouvez télécharger Node.js depuis le [site officiel](https://nodejs.org/en/download/).

Une fois Node.js installé, vous pouvez installer TypeScript en utilisant le gestionnaire de paquets Node (npm), qui est fourni avec Node.js.

Ouvrez votre terminal et exécutez la commande suivante :

```bash
npm install -g typescript
```

Cette commande installe TypeScript globalement sur votre système. Vous pouvez confirmer l'installation en exécutant la commande `tsc`, qui signifie `TypeScript` `compiler` :

```bash
tsc --version
```

Cette commande doit afficher la version de TypeScript que vous avez installée.

Maintenant que TypeScript est installé, nous sommes prêts à commencer notre voyage dans le monde de TypeScript !

### Configuration

Super ! Maintenant que nous avons installé TypeScript, parlons d'autre chose d'important : la `configuration`. Pour les projets plus importants, il est courant d'avoir un fichier de configuration, `tsconfig.json`, pour gérer les options du compilateur. Ce fichier vous permet de spécifier les fichiers de niveau racine et les options du compilateur nécessaires pour compiler le projet.

Lorsque vous exécutez la commande `tsc`, le compilateur recherche un fichier `tsconfig.json` dans le répertoire courant. S'il en trouve un, il utilise les options spécifiées dans le fichier pour compiler le projet. S'il n'en trouve pas, il utilise les options par défaut.

Pour générer un fichier `tsconfig.json`, vous pouvez exécuter la commande suivante :

```bash
tsc --init
```

### Comprendre `tsconfig.json`

Maintenant que nous avons installé et configuré TypeScript, plongeons plus profondément dans le fichier `tsconfig.json`. Ce fichier est une partie cruciale de tout projet TypeScript. Il contient divers paramètres qui déterminent comment votre code TypeScript est compilé en JavaScript.

Pour créer un fichier `tsconfig.json`, vous pouvez utiliser la commande `tsc --init` comme je l'ai montré ci-dessus. Cette commande génère un fichier `tsconfig.json` dans votre répertoire courant avec certains paramètres par défaut.

Voici un exemple de ce à quoi un fichier `tsconfig.json` peut ressembler :

```json
{
 "compilerOptions": {
    "target": "es5",
    "module": "commonjs",
    "strict": true,
    "outDir": "./dist"
 },
 "include": ["src/**/*.ts"],
 "exclude": ["node_modules"]
}
```

Dans cette configuration :

* L'objet `compilerOptions` contient des paramètres pour le compilateur TypeScript.
    
* L'option `target` indique au compilateur quelle version d'ECMAScript utiliser pour compiler votre code.
    
* L'option `module` définit le système de modules pour votre projet.
    
* L'option `strict` active une large gamme de comportements de vérification de type.
    
* L'option `outDir` spécifie le répertoire où les fichiers JavaScript compilés seront placés.
    
* Les options `include` et `exclude` indiquent au compilateur quels fichiers inclure et exclure pendant le processus de compilation.
    

Après avoir configuré votre fichier `tsconfig.json`, vous pouvez compiler votre projet TypeScript en exécutant simplement la commande `tsc` dans votre terminal. Cette commande compilera tous les fichiers TypeScript de votre projet selon les options spécifiées dans votre fichier `tsconfig.json`.

### Déclarations de types et variables dans TypeScript

Apprenons maintenant davantage sur les types. TypeScript prend en charge plusieurs types, notamment `number`, `string`, `boolean`, `object`, `null`, `undefined`, `symbol`, `bigint` et `any`. Explorons chacun de ces types en détail.

1. `number` : Ce type est utilisé pour les valeurs numériques. Il peut s'agir d'une valeur entière ou à virgule flottante.
    

Exemple :

```typescript
let age: number = 30;
let weight: number = 65.5;
```

2. `string` : Ce type est utilisé pour les données textuelles. Il peut être défini en utilisant des guillemets simples, des guillemets doubles ou des littéraux de gabarit.
    

Exemple :

```typescript
let name: string = 'John Doe';
let greeting: string = `Hello, ${name}`;
```

3. `boolean` : Ce type est utilisé pour les valeurs logiques. Il ne peut être que `true` ou `false`.
    

Exemple :

```typescript
let isAdult: boolean = true;
let isStudent: boolean = false;
```

4. `object` : Ce type est utilisé pour les structures de données complexes. Un objet peut avoir des propriétés et des méthodes.
    

Exemple :

```typescript
let person: object = { name: 'John Doe', age: 30 };
let date: object = new Date();
```

5. `null` : Ce type n'a qu'une seule valeur : `null`. Il est utilisé lorsque vous souhaitez explicitement définir une variable pour qu'elle n'ait aucune valeur ou objet.
    

Exemple :

```typescript
let emptyValue: null = null;
let anotherEmptyValue: null = null;
```

6. `undefined` : Ce type n'a qu'une seule valeur : `undefined`. Il est utilisé lorsqu'une variable a été déclarée mais n'a pas encore été assignée à une valeur.
    

Exemple :

```typescript
let unassignedValue: undefined = undefined;
let anotherUnassignedValue: undefined;
```

7. `symbol` : Ce type est utilisé pour créer des identifiants uniques pour les objets.
    

Exemple :

```typescript
let symbol1: symbol = Symbol('symbol1');
let symbol2: symbol = Symbol('symbol2');
```

8. `bigint` : Ce type est utilisé pour les nombres entiers plus grands que `2^53 - 1`, qui est la limite supérieure pour le type `number`.
    

Exemple :

```typescript
let bigNumber: bigint = 9007199254740993n;
let anotherBigNumber: bigint = BigInt(9007199254740993);
```

9. `any` : Ce type est utilisé lorsque le type d'une variable pourrait être n'importe quoi. C'est une façon de se soustraire à la vérification de type.
    

Exemple :

```typescript
let variable: any = 'I am a string';
variable = 42; // I am a number now
```

Maintenant, parlons de différentes façons de déclarer des variables dans TypeScript.

TypeScript fournit un moyen de définir la forme d'un objet, y compris ses propriétés et méthodes, en utilisant des déclarations de type. Cela vous permet de créer des types réutilisables qui peuvent être utilisés pour définir la structure des objets dans votre base de code.

1. **Aliases de type** : Les aliases de type sont un moyen de créer un nouveau nom pour un type existant. Ils sont souvent utilisés pour définir des types complexes utilisés à plusieurs endroits.
    

Exemple :

```typescript
type Point = {
  x: number;
  y: number;
}

let origin: Point = { x: 0, y: 0 };
```

Dans cet exemple, `Point` est un alias de type pour un objet avec des propriétés `x` et `y`. Il est utilisé pour définir le type de l'objet `origin`.

2. **Types d'intersection** : Les types d'intersection sont un moyen de combiner plusieurs types en un seul type. Ils sont souvent utilisés pour créer des types complexes qui ont les propriétés de plusieurs autres types.
    

Exemple :

```typescript
type Printable = {
  print: () => void;
};

type Loggable = {
  log: () => void;
};

type Logger = Printable & Loggable;

let logger: Logger = {
  print: () => console.log('Printing...'),
  log: () => console.log('Logging...'),
};
```

Dans cet exemple, `Printable` et `Loggable` sont deux types qui ont une méthode `print` et `log`, respectivement. Le type `Logger` est une intersection de `Printable` et `Loggable`, donc il a à la fois une méthode `print` et `log`.

3. **Types d'union** : Les types d'union sont un moyen de définir un type qui peut être l'un des plusieurs types différents. Ils sont souvent utilisés pour créer des types flexibles qui peuvent représenter une variété de valeurs.
    

Exemple :

```typescript
type ID = string | number;

let id: ID = '123';
id = 123;
```

Dans cet exemple, `ID` est un type d'union qui peut être soit une `string` soit un `number`. Il est utilisé pour définir le type de la variable `id`, qui peut être assignée à une `string` ou à un `number`.

4. **Assertions de type** : Les assertions de type sont un moyen d'indiquer au compilateur TypeScript que vous en savez plus sur le type d'une valeur que lui. Elles sont similaires au casting de type dans d'autres langages.
    

Exemple :

```typescript
let value: any = 'Hello, TypeScript!';
let length: number = (value as string).length;
```

Dans cet exemple, le mot-clé `as` est utilisé pour affirmer que `value` est de type `string`. Cela nous permet d'accéder à la propriété `length` de la chaîne.

### Fonctions dans TypeScript

Les fonctions sont les éléments de base de tout langage de programmation. Elles encapsulent la logique en unités de code réutilisables, favorisant la réutilisation du code et la modularité. Dans TypeScript, les fonctions peuvent être définies en utilisant le mot-clé `function` ou les fonctions fléchées (`=>`). Les deux méthodes ont leurs propres cas d'utilisation et caractéristiques.

Parlons de certains types de fonctions dans TypeScript :

1. **Déclarations de fonction** : Les fonctions peuvent être déclarées en utilisant le mot-clé `function` suivi d'un nom de fonction unique. Le corps de la fonction est enfermé dans des accolades `{}`.
    

Exemple :

```typescript
function greet(name: string): void {
  console.log(`Hello, ${name}!`);
}

greet('Alice');  // Affiche : Hello, Alice!
```

Dans cet exemple, `greet` est une fonction qui prend un paramètre, `name`, de type `string`. La fonction ne retourne rien, donc son type de retour est `void`.

2. **Fonctions fléchées** : Les fonctions fléchées sont une syntaxe plus moderne pour écrire des fonctions dans TypeScript et JavaScript. Elles sont particulièrement utiles lors de l'écriture de petites fonctions en ligne.
    

Exemple :

```typescript
const greet = (name: string): void => {
  console.log(`Hello, ${name}!`);
}

greet('Bob');  // Affiche : Hello, Bob!
```

Dans cet exemple, `greet` est une fonction fléchée qui se comporte exactement comme la fonction `greet` dans l'exemple précédent. Le symbole `=>` sépare les paramètres de la fonction et le corps de la fonction.

3. **Types de fonction** : Dans TypeScript, vous pouvez spécifier les types des paramètres et la valeur de retour d'une fonction. Cela fournit une sécurité de type, garantissant que la fonction est appelée avec les types corrects d'arguments et qu'elle retourne le type correct de valeur.
    

Exemple :

```typescript
function add(a: number, b: number): number {
  return a + b;
}

let sum: number = add(1, 2);  // sum est 3
```

Dans cet exemple, la fonction `add` prend deux paramètres, `a` et `b`, tous deux de type `number`, et retourne un `number`.

4. **Paramètres optionnels et par défaut** : TypeScript permet aux paramètres de fonction d'être optionnels ou d'avoir des valeurs par défaut.
    

Exemple :

```typescript
function greet(name: string, greeting: string = 'Hello'): void {
  console.log(`${greeting}, ${name}!`);
}

greet('Charlie');  // Affiche : Hello, Charlie!
greet('Charlie', 'Hi');  // Affiche : Hi, Charlie!
```

Dans cet exemple, la fonction `greet` a deux paramètres, `name` et `greeting`. Le paramètre `greeting` est optionnel et a une valeur par défaut de 'Hello'.

5. **Paramètres rest** : TypeScript prend en charge les paramètres rest, qui permettent de passer un nombre arbitraire d'arguments à une fonction.
    

Exemple :

```typescript
function sum(...numbers: number[]): number {
  return numbers.reduce((a, b) => a + b, 0);
}

let total: number = sum(1, 2, 3, 4, 5); // total est 15
```

Dans cet exemple, la fonction `sum` prend un nombre arbitraire d'arguments et retourne leur somme.

### Classes et objets dans TypeScript

Les classes sont une partie fondamentale de la programmation orientée objet (POO). Elles sont des modèles pour créer des objets, fournissant des valeurs initiales pour l'état (variables membres) et des implémentations de comportement (fonctions membres ou méthodes).

TypeScript prend en charge les classes, qui sont déclarées en utilisant le mot-clé `class`. Un avantage des classes TypeScript est qu'elles prennent en charge les fonctionnalités de programmation orientée objet (POO) telles que l'`héritage`, l'`encapsulation` et le `polymorphisme`.

1. **Déclaration de classe** : Dans TypeScript, les classes sont déclarées en utilisant le mot-clé `class`.
    

Exemple :

```typescript
class Person {
  name: string;
  age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }

  greet(): void {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }
}

let john = new Person('John', 25);
john.greet(); // Affiche : Hello, my name is John and I am 25 years old.
```

Dans cet exemple, `Person` est une classe avec deux propriétés, `name` et `age`, et une méthode `greet`. Le `constructor` est une méthode spéciale pour créer et initialiser un objet créé avec une classe.

2. **Héritage** : TypeScript prend en charge l'héritage, un mécanisme de baser une classe sur une autre classe, conservant une implémentation similaire. L'héritage est réalisé en utilisant le mot-clé `extends`.
    

Exemple :

```typescript
class Employee extends Person {
  department: string;

  constructor(name: string, age: number, department: string) {
    super(name, age);
    this.department = department;
  }

  greet(): void {
    super.greet();
    console.log(`I work in ${this.department}.`);
  }
}

let jane = new Employee('Jane', 30, 'HR');
jane.greet(); // Affiche : Hello, my name is Jane and I am 30 years old. I work in HR.
```

Dans cet exemple, `Employee` est une classe qui étend `Person`. Elle ajoute une nouvelle propriété `department` et remplace la méthode `greet`. Le mot-clé `super` est utilisé pour appeler les méthodes correspondantes de la classe parente.

3. **Classes abstraites** : Les classes abstraites sont des classes qui ne peuvent pas être instanciées directement. Elles sont utilisées comme classes de base pour d'autres classes et peuvent contenir des méthodes abstraites qui doivent être implémentées par les classes dérivées.
    

Exemple :

```typescript
abstract class Shape {
  abstract area(): number;
}

class Circle extends Shape {
  radius: number;

  constructor(radius: number) {
    super();
    this.radius = radius;
  }

  area(): number {
    return Math.PI * this.radius ** 2;
  }
}

let circle = new Circle(5);
console.log(circle.area()); // Affiche : 78.54
```

Dans cet exemple, `Shape` est une classe abstraite avec une méthode abstraite `area`. La classe `Circle` étend `Shape` et implémente la méthode `area`. Les classes abstraites sont utiles pour définir une interface commune pour un ensemble de classes.

4. **Encapsulation** : L'encapsulation est le regroupement de données (propriétés) et de méthodes qui opèrent sur les données (méthodes) en une seule unité appelée classe. Dans TypeScript, l'encapsulation est réalisée en utilisant des modificateurs d'accès tels que public, private et protected.
    

Exemple :

```ts
class Person {
  private name: string;
  protected age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }

  greet(): void {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }
}

let john = new Person("John", 25);
console.log(john.name); // Erreur : La propriété "name" est privée
console.log(john.age);  // Erreur : La propriété "age" est protégée
```

Dans cet exemple, `name` est une propriété privée de la classe `Person`, donc elle ne peut pas être accessible depuis l'extérieur de la classe. `age` est une propriété protégée, donc elle peut être accessible depuis les sous-classes mais pas depuis l'extérieur de la classe.

5. **Polymorphisme** : Le polymorphisme est la capacité d'un objet à prendre de nombreuses formes. Dans TypeScript, le polymorphisme est réalisé par le biais de la substitution de méthodes, où une méthode dans une sous-classe a le même nom et la même signature qu'une méthode dans sa superclasse.
    

Exemple :

```typescript
class Animal {
  speak(): void {
    console.log('Animal makes a sound');
  }
}

class Dog extends Animal {
  speak(): void {
    console.log('Dog barks');
  }
}

let animal: Animal = new Dog();
animal.speak(); // Affiche : Dog barks
```

Dans cet exemple, `Animal` est une classe de base avec une méthode `speak`. `Dog` est une sous-classe qui remplace la méthode `speak`. Lorsqu'une instance de `Dog` est assignée à une variable de type `Animal`, la méthode `speak` de `Dog` est appelée.

6. **Modificateurs d'accès** : TypeScript prend en charge les modificateurs d'accès `public`, `private` et `protected`. Par défaut, chaque membre est `public`.
    

Exemple :

```typescript
class Animal {
  private name: string;

  constructor(name: string) {
    this.name = name;
  }

  public getName(): string {
    return this.name;
  }
}

let dog = new Animal('Dog');
console.log(dog.getName()); // Affiche : Dog
```

Dans cet exemple, `name` est un membre privé de la classe `Animal`. Il ne peut être accessible qu'au sein de la classe `Animal`. La méthode `getName` est publique, donc elle peut être appelée depuis l'extérieur de la classe.

### Interfaces dans TypeScript

Les interfaces dans TypeScript sont des moyens puissants de définir des contrats au sein de votre code. Elles sont utilisées pour vérifier le type d'un objet afin de voir s'il correspond à une certaine structure.

En définissant une interface, nous pouvons nommer une combinaison spécifique de variables, en nous assurant qu'elles seront toujours utilisées comme un ensemble.

1. **Déclaration d'interface** : Les interfaces sont déclarées avec le mot-clé `interface`.
    

Exemple :

```typescript
interface Person {
  name: string;
  age: number;
}

let john: Person = { name: 'John', age: 25 };
```

Dans cet exemple, `Person` est une interface qui décrit un objet ayant un `name` de type `string` et un `age` de type `number`.

2. **Propriétés optionnelles** : Les propriétés d'interface peuvent être marquées comme optionnelles avec `?`.
    

Exemple :

```typescript
interface Person {
  name: string;
  age?: number;
}

let alice: Person = { name: 'Alice' };
```

Dans cet exemple, `age` est une propriété optionnelle dans l'interface `Person`. L'objet `alice` est toujours une `Person` même s'il n'a pas d'`age`.

3. **Types de fonction** : Les interfaces peuvent également décrire des types de fonction.
    

Exemple :

```typescript
interface GreetFunction {
  (name: string, age: number): string;
}

let greet: GreetFunction = function(name: string, age: number): string {
  return `Hello, my name is ${name} and I am ${age} years old.`;
};
```

Dans cet exemple, `GreetFunction` est une interface qui décrit une fonction prenant un `name` et un `age` et retournant une `string`.

4. **Extension d'interfaces** : Les interfaces peuvent s'étendre les unes les autres, créant une nouvelle interface qui hérite des membres de l'interface de base.
    

Exemple :

```typescript
interface Animal {
  name: string;
}

interface Dog extends Animal {
  breed: string;
}

let myDog: Dog = { name: 'Rex', breed: 'German Shepherd' };
```

Dans cet exemple, `Dog` étend `Animal`, donc un `Dog` a à la fois un `name` et un `breed`.

### Énumérations dans TypeScript

Les énumérations sont un moyen de définir un ensemble de constantes nommées. Elles sont souvent utilisées pour représenter un ensemble de valeurs liées, telles que les jours de la semaine ou les mois de l'année.

TypeScript prend en charge les énumérations numériques et de chaînes, offrant une manière flexible de définir et de travailler avec des ensembles de constantes.

1. **Énumérations numériques** : Les énumérations numériques sont un moyen de définir un ensemble de constantes nommées avec des valeurs numériques. Par défaut, les valeurs des constantes commencent à 0 et augmentent de 1 pour chaque constante suivante.
    

Exemple :

```typescript
enum Day {
  Sunday,
  Monday,
  Tuesday,
  Wednesday,
  Thursday,
  Friday,
  Saturday
}

let today: Day = Day.Monday;
```

Dans cet exemple, `Day` est une énumération numérique qui représente les jours de la semaine. Les constantes `Sunday`, `Monday`, `Tuesday`, etc., se voient attribuer des valeurs numériques commençant à partir de 0.

2. **Énumérations de chaînes** : Les énumérations de chaînes sont un moyen de définir un ensemble de constantes nommées avec des valeurs de chaîne. Contrairement aux énumérations numériques, les valeurs des constantes dans une énumération de chaînes sont initialisées avec la valeur du nom de la constante.
    

Exemple :

```typescript
enum Month {
  January = 'January',
  February = 'February',
  March = 'March',
  April = 'April',
  May = 'May',
  June = 'June',
  July = 'July',
  August = 'August',
  September = 'September',
  October = 'October',
  November = 'November',
  December = 'December'
}

let currentMonth: Month = Month.June;
```

Dans cet exemple, `Month` est une énumération de chaînes qui représente les mois de l'année. Les constantes `January`, `February`, `March`, etc., se voient attribuer des valeurs de chaîne égales à leurs noms.

3. **Énumérations calculées** : Les énumérations peuvent avoir des valeurs calculées, qui sont initialisées avec une expression au lieu d'une valeur constante. Cela permet une plus grande flexibilité dans la définition des valeurs des constantes.
    

Exemple :

```typescript
enum Color {
  Red = 1,
  Green = Math.pow(2, 2),
  Blue = Math.pow(2, 3)
}

let color: Color = Color.Green;
```

Dans cet exemple, `Color` est une énumération avec des valeurs calculées. Les constantes `Red`, `Green` et `Blue` se voient attribuer les valeurs 1, 4 et 8, respectivement, en utilisant la fonction `Math.pow`.

4. **Mappage inverse** : Les énumérations dans TypeScript prennent en charge le mappage inverse, ce qui signifie que vous pouvez accéder au nom d'une constante à partir de sa valeur. Cela est utile pour le débogage et la journalisation.
    

Exemple :

```typescript
enum Day {
  Sunday,
  Monday,
  Tuesday,
  Wednesday,
  Thursday,
  Friday,
  Saturday
}

let dayName: string = Day[1]; // 'Monday'
```

Dans cet exemple, l'énumération `Day` est utilisée pour accéder au nom

### Génériques dans TypeScript

Les génériques sont un moyen de définir une fonction ou une classe qui peut être utilisée avec différents types de données. Ils sont souvent utilisés pour créer des composants réutilisables qui peuvent fonctionner avec différents types de données.

TypeScript prend en charge les génériques, vous permettant d'écrire du code sécurisé en termes de types qui est flexible et réutilisable.

Examinons maintenant quelques exemples de fonctions et de classes génériques.

1. **Fonctions génériques** : Les fonctions génériques sont des fonctions qui peuvent fonctionner avec une variété de types de données. Elles sont définies en utilisant des paramètres de type, qui sont des espaces réservés pour les types réels qui seront utilisés lorsque la fonction est appelée.
    

Exemple :

```typescript
function identity<T>(value: T): T {
  return value;
}

let result1: number = identity<number>(42);
let result2: string = identity<string>('Hello, TypeScript!');
```

Dans cet exemple, `identity` est une fonction générique qui prend un paramètre de type `T` et retourne une valeur de type `T`. Le paramètre de type `T` est utilisé pour spécifier le type de l'argument et la valeur de retour.

2. **Classes génériques** : Les classes génériques sont des classes qui peuvent fonctionner avec une variété de types de données. Elles sont définies en utilisant des paramètres de type, qui sont des espaces réservés pour les types réels qui seront utilisés lorsque la classe est instanciée.
    

Exemple :

```typescript
class Box<T> {
  value: T;

  constructor(value: T) {
    this.value = value;
  }
}

let box1: Box<number> = new Box<number>(42);
let box2: Box<string> = new Box<string>('Hello, TypeScript!');
```

Dans cet exemple, `Box` est une classe générique qui prend un paramètre de type `T` et a une propriété `value` de type `T`. Le paramètre de type `T` est utilisé pour spécifier le type de la valeur stockée dans la boîte.

3. **Contraintes génériques** : Les contraintes génériques sont un moyen de restreindre les types qui peuvent être utilisés avec une fonction ou une classe générique. Elles sont définies en utilisant le mot-clé `extends`, suivi du type ou de l'interface que le paramètre de type doit étendre.
    

Exemple :

```typescript
interface Printable {
  print(): void;
}

function printValue<T extends Printable>(value: T): void {
  value.print();
}

class Person implements Printable {
  print(): void {
    console.log('Printing person...');
  }
}

let person: Person = new Person();
printValue(person);
```

Dans cet exemple, `Printable` est une interface qui définit une méthode `print`. La fonction `printValue` est une fonction générique qui prend un paramètre de type `T` qui doit étendre `Printable`. La classe `Person` implémente l'interface `Printable`.

À ce stade, vous avez une compréhension de base de TypeScript et vous pouvez commencer à plonger dans des concepts plus avancés.

## Conclusion

Dans cet article, vous avez appris les bases de TypeScript.

Nous avons parlé de la syntaxe de base de TypeScript, telle que les variables, les fonctions et les classes.

Vous avez également appris les types intégrés de TypeScript, tels que les nombres, les chaînes et les booléens.

Nous avons discuté des énumérations intégrées de TypeScript, telles que les énumérations numériques, les énumérations de chaînes et les énumérations calculées. Et vous avez appris les types génériques de TypeScript, tels que les fonctions et les classes génériques.

Merci d'avoir lu !