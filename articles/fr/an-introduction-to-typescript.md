---
title: Comment utiliser TypeScript – Tutoriel TS pour débutants
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2022-03-29T01:28:31.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-typescript
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-hitarth-jadhav-220357.jpg
tags:
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: Comment utiliser TypeScript – Tutoriel TS pour débutants
seo_desc: 'Hi everyone! In this article we''ll talk about what TypeScript is, why
  is it cool, and how can you use it.

  Table of Contents


  Intro


  About Types


  Strings


  Numbers


  Booleans


  Undefined


  Null


  Objects


  Arrays


  Functions




  What''s the Deal with Types and...'
---

Salut tout le monde ! Dans cet article, nous allons voir ce qu'est TypeScript, pourquoi c'est génial et comment vous pouvez l'utiliser.

## Table des matières

* [Introduction](#heading-introduction)
    
* [À propos des types](#heading-a-propos-des-types)
    
    * [Chaînes de caractères](#heading-chaines-de-caracteres)
        
    * [Nombres](#heading-nombres)
        
    * [Booléens](#heading-booleens)
        
    * [Indéfini](#heading-indefini)
        
    * [Null](#heading-null)
        
    * [Objets](#heading-objets)
        
    * [Tableaux](#heading-tableaux)
        
    * [Fonctions](#heading-fonctions)
        
* [C'est quoi le problème avec les types et JavaScript ?](#heading-cest-quoi-le-probleme-avec-les-types-et-javascript)
    
* [L'arrivée de TypeScript](#heading-larrivee-de-typescript)
    
* [Les bases de TypeScript](#heading-les-bases-de-typescript)
    
    * [Types par inférence](#heading-types-par-inference)
        
    * [Déclarer des types](#heading-declarer-des-types)
        
        * [Interfaces](#heading-interfaces)
            
        * [Conditionnels](#heading-conditionnels)
            
        * [Unions](#heading-unions)
            
        * [Typer des fonctions](#heading-typer-des-fonctions)
            
        * [Typer des tableaux](#heading-typer-des-tableaux)
            
* [Le compilateur de TypeScript](#heading-le-compilateur-de-typescript)
    
* [Comment créer un projet TypeScript](#heading-comment-creer-un-projet-typescript)
    
    * [Un mot sur les bibliothèques](#heading-un-mot-sur-les-bibliotheques)
        
* [Autres fonctionnalités de TypeScript](#heading-autres-fonctionnalites-de-typescript)
    
* [Synthèse](#heading-synthese)
    

# Introduction

TypeScript est un **sur-ensemble** de JavaScript. "Sur-ensemble" signifie qu'il ajoute des fonctionnalités par-dessus ce que JavaScript propose. TypeScript reprend toutes les fonctionnalités et structures que JavaScript fournit en tant que langage, et y ajoute quelques éléments.

Le principal apport de TypeScript est le **typage statique**. Pour vraiment comprendre ce que cela signifie, nous devons d'abord comprendre ce que sont les types. Voyons cela de plus près.

# À propos des types

Dans un langage de programmation, les types font référence au **genre ou au type d'information** qu'un programme donné stocke. Les informations ou données peuvent être classées en différents types selon leur contenu.

Les langages de programmation possèdent généralement des types de données intégrés. En JavaScript, il existe **six types de données de base** qui peuvent être divisés en **trois catégories principales** :

* Types de données primitifs
    
* Types de données composites
    
* Types de données spéciaux
    

* String (chaîne), Number (nombre) et Boolean (booléen) sont des types de données **primitifs**.
    
* Object (objet), Array (tableau) et Function (fonction) (qui sont tous des types d'objets) sont des types de données **composites**.
    
* Alors que Undefined (indéfini) et Null sont des types de données **spéciaux**.
    

Les types de données **primitifs** ne peuvent contenir **qu'une seule valeur à la fois**, tandis que les types de données **composites** peuvent contenir des **collections de valeurs** et des entités plus complexes.

Jetons un coup d'œil rapide à chacun de ces types de données.

## Chaînes de caractères

Le type de données string est utilisé pour représenter des données textuelles (c'est-à-dire des séquences de caractères). Les chaînes sont créées en utilisant des guillemets simples ou doubles entourant un ou plusieurs caractères, comme illustré ci-dessous :

```ts
let a = "Salut !";
```

## Nombres

Le type de données number est utilisé pour représenter des nombres positifs ou négatifs, avec ou sans décimales :

```ts
let a = 25;
```

Le type de données Number inclut également certaines valeurs spéciales qui sont : `Infinity`, `-Infinity` et `NaN`.

`Infinity` représente l'infini mathématique ∞, qui est supérieur à n'importe quel nombre. `-Infinity` est le résultat de la division d'un nombre non nul par 0. Tandis que `NaN` représente une valeur spéciale "Not-a-Number" (pas un nombre). C'est le résultat d'une opération mathématique invalide ou indéfinie, comme prendre la racine carrée de -1 ou diviser 0 par 0, etc.

## Booléens

Le type de données Boolean ne peut contenir que deux valeurs : `true` (vrai) ou `false` (faux). Il est typiquement utilisé pour stocker des valeurs comme oui (vrai) ou non (faux), allumé (vrai) ou éteint (faux), etc., comme démontré ci-dessous :

```ts
let areYouEnjoyingTheArticle = true;
```

## Indéfini

Le type de données undefined ne peut avoir qu'une seule valeur, la valeur spéciale `undefined`. Si une variable a été déclarée mais qu'aucune valeur ne lui a été assignée, elle a la valeur undefined.

```ts
let a;

console.log(a); // Sortie : undefined
```

## Null

Une valeur null signifie qu'il n'y a pas de valeur. Ce n'est pas l'équivalent d'une chaîne vide ("") ou de 0, c'est simplement rien du tout.

```ts
let thisIsEmpty = null;
```

## Objets

L'objet est un type de données complexe qui vous permet de stocker des collections de données. Un objet contient des **propriétés**, définies comme des **paires clé-valeur**.

Une clé de propriété (nom) est toujours une chaîne de caractères, mais la valeur peut être n'importe quel type de données, comme des chaînes, des nombres, des booléens, ou des types de données complexes comme des tableaux, des fonctions et d'autres objets.

```ts
let car = {
  modal: "BMW X3",
  color: "white",
  doors: 5
};
```

## Tableaux

Un tableau (array) est un type d'objet utilisé pour stocker plusieurs valeurs dans une seule variable. Chaque valeur (appelée aussi élément) dans un tableau possède une position numérique, connue sous le nom d'**index**, et peut contenir des données de n'importe quel type (nombres, chaînes, booléens, fonctions, objets, et même d'autres tableaux).

L'index d'un tableau commence à 0, de sorte que le premier élément du tableau est `arr[0]`.

```ts
let arr = ["I", "love", "freeCodeCamp"];

console.log(arr[2]); // Sortie : freeCodeCamp
```

## Fonctions

Une fonction est un objet appelable qui exécute un bloc de code. Vous déclarez d'abord la fonction et, à l'intérieur, le code que vous souhaitez qu'elle exécute. Et plus tard, vous appelez simplement la fonction chaque fois que vous voulez que son code s'exécute.

Puisque les fonctions sont des objets, il est possible de les assigner à des variables, comme le montre l'exemple ci-dessous :

```ts
let greeting = function () {
  return "Hello World!";
};

console.log(greeting()); // Sortie : Hello World!
```

# C'est quoi le problème avec les types et JavaScript ?

Maintenant que nous avons une idée claire de ce que sont les types, nous pouvons commencer à discuter de la façon dont cela fonctionne avec JavaScript – et pourquoi quelque chose comme TypeScript est nécessaire en premier lieu.

Le fait est que JavaScript est un **langage dynamiquement et faiblement typé**. Cela signifie qu'en JavaScript, les variables ne sont pas directement associées à un type de valeur particulier, et n'importe quelle variable peut se voir assigner (et ré-assigner) des valeurs de tous types.

Regardez l'exemple suivant :

```ts
let foo = 42; // foo est maintenant un nombre
foo = "bar";  // foo est maintenant une chaîne de caractères
foo = true;   // foo est maintenant un booléen
```

Vous pouvez voir comment nous pouvons changer le contenu et le type de la variable sans aucun problème.

Cela a été fait à dessein lors de la création de JavaScript, car il était censé être un langage de script convivial pour les programmeurs et les designers, utilisé uniquement pour ajouter des fonctionnalités aux sites web.

Mais JavaScript a énormément évolué au fil des ans et a commencé à être utilisé non seulement pour ajouter des fonctionnalités simples, mais aussi pour construire d'énormes applications. Et lors de la construction de grandes applications, les types dynamiques peuvent entraîner des bugs stupides dans la base de code.

Voyons cela avec un exemple simple. Disons que nous avons une fonction qui reçoit trois paramètres et retourne une chaîne de caractères :

```ts
const personDescription = (name, city, age) =>
  `${name} lives in ${city}. he's ${age}. In 10 years he'll be ${age + 10}`;
```

Si nous appelons la fonction de cette façon, nous obtenons la sortie correcte :

```ts
console.log(personDescription("Germán", "Buenos Aires", 29));
// Sortie : Germán lives in Buenos Aires. he's 29. In 10 years he'll be 39.
```

Mais si par accident nous passons le troisième paramètre à la fonction sous forme de chaîne de caractères, nous obtenons une sortie erronée :

```ts
console.log(personDescription("Germán", "Buenos Aires", "29"));
// Sortie : Germán lives in Buenos Aires. he's 29. In 10 years he'll be **2910**.
```

JavaScript n'affiche pas d'erreur car le programme n'a aucun moyen de savoir quel type de données la fonction doit recevoir. Il prend simplement les paramètres que nous avons donnés et effectue l'action programmée, indépendamment du type de données.

Il est facile de faire cette erreur en tant que développeur, surtout en travaillant sur de grandes bases de code sans être familier avec les paramètres requis par les fonctions ou les API. Et c'est exactement ce que TypeScript vient résoudre.

# L'arrivée de TypeScript

TypeScript a été lancé en 2012. Il a été développé et est actuellement maintenu par Microsoft.

Dans TypeScript, tout comme dans d'autres langages de programmation tels que Java ou C#, nous devons déclarer un type de données chaque fois que nous créons une structure de données.

En déclarant son type de données, nous donnons au programme des informations pour évaluer plus tard si les valeurs assignées à cette structure de données correspondent aux types déclarés ou non.

S'il y a correspondance, le programme s'exécute, et sinon, nous obtenons une erreur. Et ces erreurs sont très précieuses, car en tant que développeurs, nous pouvons intercepter les bugs plus tôt. ;)

Répétons l'exemple précédent mais cette fois avec TypeScript.

En TypeScript, ma fonction ressemblerait à ceci (voyez qu'elle est exactement identique, sauf qu'à côté de chaque paramètre, je déclare son type de données) :

```ts
const personDescription = (name: string, city: string, age: number) =>
  `${name} lives in ${city}. he's ${age}. In 10 years he'll be ${age + 10}.`;
```

Maintenant, si j'essaie d'appeler la fonction avec le mauvais type de données pour un paramètre, j'obtiens l'erreur suivante :

```ts
console.log(personDescription("Germán", "Buenos Aires", "29"));
// Erreur : TSError: ⨯ Unable to compile TypeScript: Argument of type 'string' is not assignable to parameter of type 'number'.
```

La beauté de TypeScript est qu'il reste aussi simple que le code JavaScript, nous y ajoutons seulement les déclarations de type. C'est pourquoi TypeScript est appelé un sur-ensemble de JavaScript, car TypeScript ne fait qu'**ajouter** certaines fonctionnalités à JavaScript.

# Les bases de TypeScript

Jetons un coup d'œil à la syntaxe de TypeScript et apprenons à travailler avec.

## Types par inférence

Il existe plusieurs façons de déclarer des types dans TypeScript.

La première que nous allons apprendre est l'**inférence**, dans laquelle vous ne déclarez aucun type, mais TypeScript l'infère (le devine) pour vous.

Disons que nous déclarons une variable de type chaîne comme ceci :

```ts
let helloWorld = "Hello World";
```

Si plus tard j'essaie de lui réassigner un nombre, j'obtiendrai l'erreur suivante :

```ts
helloWorld = 20;
// Type 'number' is not assignable to type 'string'.ts(2322)
```

En créant une variable et en lui assignant une valeur particulière, TypeScript utilisera cette valeur comme type.

Comme mentionné dans la [documentation de TypeScript](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html) :

> En comprenant comment JavaScript fonctionne, TypeScript peut construire un système de types qui accepte le code JavaScript tout en ayant des types. Cela offre un système de types sans avoir besoin d'ajouter des caractères supplémentaires pour rendre les types explicites dans votre code.

C'est ainsi que TypeScript "sait" que `helloWorld` est une chaîne de caractères dans l'exemple ci-dessus.

Bien qu'il s'agisse d'une fonctionnalité intéressante qui vous permet d'implémenter TypeScript sans code supplémentaire, il est beaucoup plus lisible et recommandé de déclarer explicitement vos types.

## Déclarer des types

La syntaxe pour déclarer des types est assez simple : il suffit d'ajouter deux-points et le type à droite de ce que vous déclarez.

Par exemple, lors de la déclaration d'une variable :

```ts
let myName: string = "Germán";
```

Si j'essaie de réassigner cela à un nombre, j'obtiendrai l'erreur suivante :

```ts
myName = 36; // Erreur : Type 'number' is not assignable to type 'string'.
```

### Interfaces

Lorsque vous travaillez avec des **objets**, nous avons une syntaxe différente pour déclarer les types, appelée **interface**.

Une interface ressemble beaucoup à un objet JavaScript – mais nous utilisons le mot-clé `interface`, nous n'avons pas de signe égal ni de virgules, et à côté de chaque clé, nous avons son type de données au lieu de sa valeur.

Plus tard, nous pourrons déclarer cette interface comme le type de données de n'importe quel objet :

```ts
interface myData {
  name: string;
  city: string;
  age: number;
}

let myData: myData = {
  name: "Germán",
  city: "Buenos Aires",
  age: 29
};
```

Si, encore une fois, je passe l'âge sous forme de chaîne de caractères, j'obtiendrai l'erreur suivante :

```ts
let myData: myData = {
  name: "Germán",
  city: "Buenos Aires",
  age: "29" // Sortie : Type 'string' is not assignable to type 'number'.
};
```

### Conditionnels

Si, par exemple, je voulais rendre une clé facultative (conditionnelle), permettant qu'elle soit présente ou non, il suffit d'ajouter un point d'interrogation à la fin de la clé dans l'interface :

```ts
interface myData {
  name: string;
  city: string;
  age?: number;
}
```

### Unions

Si je veux qu'une variable puisse se voir assigner plus d'un type de données différent, je peux le déclarer en utilisant des **unions** comme ceci :

```ts
interface myData {
  name: string;
  city: string;
  age: number | string;
}

let myData: myData = {
  name: "Germán",
  city: "Buenos Aires",
  age: "29" // Je n'ai plus d'erreur maintenant
};
```

### Typer des fonctions

Lors du typage des fonctions, nous pouvons typer ses paramètres ainsi que sa valeur de retour :

```ts
interface myData {
  name: string;
  city: string;
  age: number;
  printMsg: (message: string) => string;
}

let myData: myData = {
  name: "Germán",
  city: "Buenos Aires",
  age: 29,
  printMsg: (message) => message
};

console.log(myData.printMsg("Hola!"));
```

### Typer des tableaux

Pour typer les tableaux, la syntaxe est la suivante :

```ts
let numbersArray: number[] = [1, 2, 3]; // Nous n'acceptons que des nombres dans ce tableau
let numbersAndStringsArray: (number | string)[] = [1, "two", 3]; // Ici, nous acceptons des nombres et des chaînes.
```

Les **tuples** sont des tableaux de taille fixe avec des types définis pour chaque position. Ils peuvent être construits comme ceci :

```ts
let skill: [string, number];
skill = ["Programming", 5];
```

# Le compilateur de TypeScript

La manière dont TypeScript vérifie les types que nous avons déclarés passe par son **compilateur**. Un compilateur est un programme qui convertit les instructions en code machine ou en une forme de plus bas niveau afin qu'elles puissent être lues et exécutées par un ordinateur.

Chaque fois que nous exécutons notre fichier TypeScript, TypeScript compile notre code et vérifie à ce moment-là les types. Le programme ne s'exécute que si tout est correct. C'est pourquoi nous pouvons détecter des erreurs avant l'exécution du programme.

D'un autre côté, en JavaScript, les types sont vérifiés à l'exécution (run time). Cela signifie que les types ne sont pas vérifiés tant que le programme ne s'exécute pas.

Il est également important de mentionner que TypeScript **transpile** le code en JavaScript.

> La transpilation est le processus consistant à prendre du code source écrit dans un langage et à le transformer dans un autre langage.

Les navigateurs ne lisent pas le TypeScript, mais ils peuvent exécuter des programmes écrits en TypeScript parce que le code est converti en JavaScript au moment de la construction (build time).

Nous pouvons également choisir vers quelle "version" de JavaScript nous voulons transpiler, par exemple es4, es5, etc. Cette option et bien d'autres peuvent être configurées à partir du fichier `tsconfig.json` qui est généré chaque fois que nous créons un projet TypeScript.

```ts
{
  "compilerOptions": {
    "module": "commonjs",
    "esModuleInterop": true,
    "target": "es6",
    "moduleResolution": "node",
    "sourceMap": true,
    "outDir": "dist"
  },
  "lib": ["es2015"]
}
```

Nous n'irons pas en profondeur dans le compilateur de TypeScript car ceci est censé être une introduction. Mais sachez qu'il y a énormément de choses que vous pouvez configurer à partir de ce fichier et d'autres, pour adapter TypeScript exactement à vos besoins.

# Comment créer un projet TypeScript

Nous pouvons démarrer un nouveau projet TypeScript en exécutant simplement quelques commandes dans notre terminal. Vous aurez besoin de Node et NPM installés sur votre système.

Une fois dans le répertoire de votre projet, exécutez d'abord `npm i typescript --save-dev`. Cela installera TypeScript et l'enregistrera comme une dépendance de développement.

Ensuite, exécutez `npx tsc --init`. Cela initialisera votre projet en créant un fichier `tsconfig.json` dans votre répertoire. Comme mentionné, ce fichier `tsconfig.json` vous permettra de configurer et de personnaliser davantage l'interaction entre TypeScript et le compilateur `tsc`.

Vous verrez que ce fichier contient un ensemble d'options par défaut et un grand nombre d'options commentées, vous permettant de voir tout ce qui est à votre disposition et de l'implémenter selon vos besoins.

```ts
{
  "compilerOptions": {
    /* Visitez https://aka.ms/tsconfig.json pour en savoir plus sur ce fichier */

    /* Projets */
    // "incremental": true,                              /* Activer la compilation incrémentale */
    // "composite": true,                                /* Activer les contraintes permettant d'utiliser un projet TypeScript avec des références de projet. */
    // "tsBuildInfoFile": "./",                          /* Spécifier le dossier pour les fichiers de compilation incrémentale .tsbuildinfo. */
    // "disableSourceOfProjectReferenceRedirect": true,  /* Désactiver la préférence pour les fichiers sources au lieu des fichiers de déclaration lors du référencement de projets composites */
    // "disableSolutionSearching": true,                 /* Exclure un projet de la vérification des références multi-projets lors de l'édition. */
    // "disableReferencedProjectLoad": true,             /* Réduire le nombre de projets chargés automatiquement par TypeScript. */

    ...
```

Et voilà. Nous pouvons ensuite créer un fichier avec l'extension `.ts` et commencer à écrire notre code TypeScript. Chaque fois que nous avons besoin de transpiler notre code en JavaScript pur, nous pouvons le faire en exécutant `tsc <nom du fichier>`.

Par exemple, j'ai un fichier `index.ts` dans mi projet avec le code suivant :

```ts
const personDescription = (name: string, city: string, age: number) =>
  `${name} lives in ${city}. he's ${age}. In 10 years he'll be ${age + 10}.`;
```

Après avoir exécuté `tsc index.ts`, un nouveau fichier `index.js` est automatiquement créé dans le même répertoire avec le contenu suivant :

```ts
var personDescription = function (name, city, age) { return name + " lives in " + city + ". he's " + age + ". In 10 years he'll be " + (age + 10) + "."; };
```

Plutôt simple, non ? =)

## Un mot sur les bibliothèques

Si vous travaillez avec React, sachez que [create-react-app](https://create-react-app.dev/docs/adding-typescript/) propose un template TypeScript, afin que TypeScript soit installé et configuré pour vous lors de la création du projet.

Des templates similaires sont également disponibles pour les applications back-end Node-Express et pour les applications React Native.

Une autre remarque : lorsque vous travaillez avec des bibliothèques externes, elles vous fournissent normalement des types spécifiques que vous pouvez installer et utiliser pour vérifier les types de ces bibliothèques.

Par exemple, en utilisant le template TypeScript pour create-react-app que j'ai mentionné, la dépendance suivante sera installée :

`"@types/react":`

Et cela nous permettra de typer nos composants de la manière suivante :

```ts
const AboutPage: React.FC = () => {
  return (
    <h1>This is the about page</h1>
  )
}
```

Nous examinerons plus en détail comment utiliser TypeScript avec React à l'avenir. Mais pour commencer, sachez simplement que cela existe. ;)

# Autres fonctionnalités de TypeScript

TypeScript peut également être considéré comme un **linter**, un outil qui fait des suggestions en temps réel au développeur pendant l'écriture du code. Surtout lorsqu'il est combiné avec VS Code, TypeScript peut faire des suggestions pertinentes basées sur nos types déclarés, ce qui permet souvent de gagner du temps et d'éviter des erreurs.

Une autre fonctionnalité de TypeScript est celle d'**outil de documentation automatique**. Imaginez que vous obteniez un nouveau poste et que vous deviez vous familiariser avec une énorme base de code. Avoir les types déclarés pour chaque fonction est d'une aide précieuse lors de leur première utilisation et réduit la courbe d'apprentissage de n'importe quel projet.

# Synthèse

Voilà pour les bases de TypeScript. Comme nous l'avons vu, cela peut ajouter un peu de code redondant (boilerplate) à notre projet. Mais cela en vaut certainement la peine en prévenant les bugs, en nous aidant à nous familiariser avec notre base de code et, globalement, en améliorant notre expérience de développement, en particulier lors du travail sur des projets volumineux et complexes.

J'espère que vous avez apprécié cet article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/germancocca/) ou [Twitter](https://twitter.com/CoccaGerman).

Santé et à la prochaine ! =D