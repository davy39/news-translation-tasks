---
title: Comment commencer à apprendre TypeScript – Un guide pour débutants
subtitle: ''
author: Akande Olalekan Toheeb
co_authors: []
series: null
date: '2025-01-24T01:19:16.521Z'
originalURL: https://freecodecamp.org/news/start-learning-typescript-beginners-guide
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1737681395105/19aeca8f-e763-4833-9ac3-5c4db7d12fe7.png
tags:
- name: TypeScript
  slug: typescript
- name: JavaScript
  slug: javascript
- name: Beginner Developers
  slug: beginners
- name: Programming Blogs
  slug: programming-blogs
- name: 'Technical writing '
  slug: technical-writing-1
- name: Tutorial
  slug: tutorial
seo_title: Comment commencer à apprendre TypeScript – Un guide pour débutants
seo_desc: 'JavaScript is the most widely-used programming language for web development.
  But it lacks type-checking support, which is an essential feature of modern programming
  languages.

  JavaScript was originally designed as a simple scripting language. Its loo...'
---

JavaScript est le langage de programmation le plus largement utilisé pour le développement web. Mais il manque de support pour la vérification des types, une fonctionnalité essentielle des langages de programmation modernes.

JavaScript a été initialement conçu comme un simple langage de script. Sa nature flexible et l'absence de fonctionnalités cruciales de **Programmation Orientée Objet (POO)** posent certains défis pour les développeurs :

1. Documentation limitée et complétion automatique.
   
2. Incapacité à utiliser les concepts de la POO.
   
3. Manque de sécurité des types, entraînant des erreurs d'exécution.
   
4. Défis dans le refactoring et la maintenance.
   
5. Absence d'interfaces et de points d'intégration.
   

TypeScript résout ces problèmes. Il a été conçu pour rendre JavaScript un langage de programmation moderne plus parfait. Il aide à améliorer l'expérience des développeurs, offre de nombreuses fonctionnalités utiles et améliore l'interopérabilité.

Cet article plonge dans les bases de TypeScript. Je vais vous apprendre comment installer TS et configurer un projet. Ensuite, nous couvrirons quelques fondamentaux importants. Vous apprendrez également comment TypeScript se compile en JavaScript, le rendant compatible avec les navigateurs et les environnements Node.js.

### [Ce que nous allons couvrir :](#heading-ce-que-nous-allons-couvrir)

* [Prérequis](#heading-prerequis)
   
* [Commencer – Comment installer TypeScript](#heading-commencer-comment-installer-typescript)
   
* [Comment organiser vos projets TypeScript](#heading-comment-organiser-vos-projets-typescript)
   
* [Comment fonctionne la typage dans TypeScript](#heading-comment-fonctionne-la-typage-dans-typescript)
   
   * [Techniques de typage](#heading-techniques-de-typage)
       
   * [Typage statique vs. dynamique dans TypeScript](#heading-typage-statique-vs-dynamique-dans-typescript)
       
   * [Inférence de type et types d'union](#heading-inference-de-type-et-types-dunion)
       
* [Comment gérer les objets, les tableaux et les types de fonctions dans TypeScript](#heading-comment-gerer-les-objets-les-tableaux-et-les-types-de-fonctions-dans-typescript)
   
   * [Types d'objets dans TypeScript](#heading-types-dobjets-dans-typescript)
       
   * [Types de tableaux dans TypeScript](#heading-types-de-tableaux-dans-typescript)
       
   * [Comment utiliser les tableaux dans TypeScript](#heading-comment-utiliser-les-tableaux-dans-typescript)
       
   * [Types de fonctions dans TypeScript](#heading-types-de-fonctions-dans-typescript)
       
* [Comment créer des types personnalisés dans TypeScript](#heading-comment-creer-des-types-personnalises-dans-typescript)
   
   * [Le mot-clé Type](#heading-le-mot-cle-type)
       
   * [Interfaces TypeScript](#heading-interfaces-typescript)
       
   * [Quand utiliser les interfaces](#heading-quand-utiliser-les-interfaces)
       
   * [Génériques et types littéraux](#heading-generiques-et-types-litteraux)
       
* [Comment fusionner les types dans TypeScript](#heading-comment-fusionner-les-types-dans-typescript)
   
   * [Quand utiliser chaque approche](#heading-quand-utiliser-chaque-approche)
       
* [Bundling et transformations dans TypeScript](#heading-bundling-et-transformations-dans-typescript)
   
* [Construire un meilleur code avec TypeScript](#heading-construire-un-meilleur-code-avec-typescript)
   

## Prérequis

Avant de plonger dans TypeScript, il est important d'avoir une compréhension fondamentale de certains concepts pour assurer un parcours d'apprentissage plus fluide. Bien que TypeScript améliore JavaScript avec un typage statique et d'autres fonctionnalités puissantes, il s'appuie sur les principes fondamentaux de JavaScript. Voici ce que vous devez savoir :

#### **1. Fondamentaux de JavaScript**

TypeScript est un sur-ensemble de JavaScript, ce qui signifie qu'il étend les capacités de JavaScript. Pour apprendre efficacement TypeScript, vous devez d'abord avoir une solide compréhension des bases de JavaScript, y compris :

* **Syntaxe et types de données** : Comprendre comment déclarer des variables (`let`, `const`, et `var`), travailler avec des types primitifs (chaînes de caractères, nombres, booléens), et gérer des tableaux et des objets.
   
* **Contrôle de flux** : Être familier avec les boucles (`for`, `while`), les conditionnelles (`if-else`, `switch`), et comment elles contrôlent l'exécution du programme.
   
* **Fonctions** : Savoir comment définir et invoquer des fonctions, travailler avec des paramètres, des valeurs de retour, et comprendre des concepts comme les fonctions fléchées et les fermetures.
   
* **Programmation Orientée Objet (POO)** : Apprendre à créer et travailler avec des objets, des classes et l'héritage. Les fonctionnalités basées sur les classes de TypeScript s'appuient fortement sur le modèle POO de JavaScript.
   
* **Gestion des erreurs** : Comprendre comment utiliser les blocs `try-catch` pour gérer les erreurs d'exécution.
   

#### **2. Bases de HTML et CSS**

Bien que TypeScript soit un langage principalement utilisé avec JavaScript, avoir une compréhension de base de HTML et CSS est utile, surtout pour les développeurs front-end. Cela est dû au fait que la plupart des projets TypeScript impliquent la création ou le travail avec des applications web.

* **HTML** : Comprendre comment structurer des pages web en utilisant des balises, des attributs et des éléments.
   
* **CSS** : Apprendre à styliser des éléments en utilisant des sélecteurs, des propriétés et des valeurs. La familiarité avec des frameworks CSS comme Bootstrap est un bonus.
   

#### **3. Familiarité avec les outils de développement**

* **Un éditeur de code** comme Visual Studio Code, qui offre un excellent support pour TypeScript et des extensions.
   
* **Node.js et npm** : Comprendre comment configurer un environnement de développement, exécuter JavaScript en dehors du navigateur, et utiliser npm (Node Package Manager) pour installer des dépendances.
   
* **Contrôle de version (Git)** : Apprendre les bases de Git pour suivre les changements et collaborer efficacement sur des projets TypeScript.
   

## Commencer – Comment installer TypeScript

Pour commencer à travailler avec TypeScript, vous devrez l'installer. Ce n'est pas un processus compliqué. Avec TypeScript installé, vous pouvez exploiter sa puissance pour créer des solutions de haute qualité.

Vous pouvez installer TS de deux manières :

1. **Installation globale** : permet d'accéder au compilateur depuis n'importe quel répertoire sur votre machine. Pour installer TypeScript globalement, exécutez la commande suivante :
   

```bash
npm install -g typescript
```

Cette commande utilise le gestionnaire de paquets Node.js, `npm`. Elle installe TypeScript globalement, rendant la commande disponible dans la ligne de commande.

2. **Installation locale** : dans ce cas, TypeScript est installé uniquement dans un projet spécifique. Cette méthode assure la compatibilité des versions et la cohérence entre les membres de l'équipe. Pour installer TypeScript localement, exécutez la commande suivante :
   

```bash
npm install typescript --save-dev
```

Différente de l'installation globale, cette commande installe TypeScript comme une dépendance de développement. La commande `tsc` est uniquement disponible pour une utilisation spécifique au projet, c'est-à-dire le projet spécifique où vous exécutez la commande.

**Pouvez-vous installer TypeScript de manière transparente maintenant ? J'espère que oui !**

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1737293526617/2f630f4c-c74f-4525-a291-9febf06d8d8b.gif align="center")

## Comment organiser vos projets TypeScript

Organiser un projet TypeScript implique de structurer ses fichiers avec des noms et des répertoires significatifs, de séparer les préoccupations et d'utiliser des modules pour l'encapsulation et la réutilisabilité.

L'extension `.ts` désigne les fichiers TypeScript et contient du code qui se convertit en JavaScript pour l'exécution.

TypeScript supporte également les fichiers `.d.ts`, également connus sous le nom de fichiers de définition de types. Ces fichiers offrent des informations de type sur les bibliothèques ou modules JavaScript externes, aidant à une meilleure vérification des types et à la complétion de code ainsi qu'à l'amélioration de l'efficacité du développement. Voici un exemple d'une bonne structure de projet TS :

```plaintext
my-ts-project/
├── src/ 
│   ├── components/ 
│   │   ├── Button.tsx
│   │   ├── Input.tsx
│   │   └── Modal.tsx
│   ├── services/ 
│   │   ├── api.ts
│   │   └── authService.ts
│   ├── utils/ 
│   │   ├── helpers.ts 
│   │   └── validators.ts
│   ├── models/ 
│   │   ├── User.ts
│   │   └── Product.ts
│   ├── index.tsx 
│   └── styles/ 
│       ├── global.css
│       └── theme.css
├── public/ 
│   ├── index.html
│   └── assets/ 
│       ├── images/
│       └── fonts/
├── tsconfig.json
└── package.json 
```

Comprenons ce qui se passe ici :

1. `src/` : Ce répertoire contient tout le code source du projet.
   
   * `components/` : Contient des composants UI réutilisables (par exemple, `Button`, `Input`, `Modal`). L'utilisation de `.tsx` (TypeScript JSX) vous permet d'écrire du JSX avec une sécurité de type.
       
   * `services/` : Contient des services qui interagissent avec des API externes ou gèrent la logique de l'application (par exemple, `api.ts` pour les appels API, `authService.ts` pour l'authentification).
       
   * `utils/` : Contient des fonctions d'assistance et des classes utilitaires pour des tâches courantes (par exemple, `helpers.ts` pour le formatage de dates, `validators.ts` pour la validation des entrées).
       
   * `models/` : Définit des interfaces ou des classes TypeScript pour représenter des structures de données (par exemple, `User.ts`, `Product.ts`).
       
   * `index.tsx` : Le point d'entrée principal de l'application.
       
   * `styles/` : Contient des fichiers CSS ou d'autres fichiers de style.
       
2. `public/` : Ce répertoire contient des actifs statiques qui ne sont pas traités par TypeScript (par exemple, HTML, images, polices).
   
3. `tsconfig.json` : Le fichier de configuration TypeScript, spécifiant les options du compilateur.
   
4. `package.json` : Le fichier manifeste du projet, listant les dépendances, les scripts et autres métadonnées du projet.
   

Juste une petite note sur les conventions de nommage pour que vous les compreniez ici :

* Utilisez PascalCase pour les noms de classes (par exemple, `User`, `Product`).
   
* Utilisez camelCase pour les noms de fonctions et de variables (par exemple, `getUser`, `firstName`).
   
* Utilisez des noms significatifs et descriptifs pour les fichiers et les répertoires.
   

Cette structure favorise la modularité, la réutilisabilité et une meilleure organisation, rendant vos projets TypeScript plus faciles à maintenir et à faire évoluer.

Organiser correctement vos projets TS améliore la maintenabilité, la lisibilité et la collaboration dans les flux de travail de développement TypeScript.

## Comment fonctionne la typage dans TypeScript

Comme tout autre langage de programmation typé, TypeScript repose sur des définitions de types, généralement appelées **Typage**.

Le typage est un terme utilisé en programmation pour définir les types de données des variables, des paramètres de méthode et des valeurs de retour dans le code.

Le typage vous permet de détecter rapidement les erreurs et tôt dans le développement, un superpouvoir qui aide à maintenir une meilleure qualité de code.

Pour spécifier un type dans TypeScript, placez un deux-points (`:`) et le type de données souhaité après le nom de votre variable. Voici un exemple :

```typescript
let age: number = 2;
```

La variable ci-dessus est déclarée avec le type `number`. Dans TypeScript, cela signifie qu'elle ne peut stocker que des nombres et rien d'autre.

### Techniques de typage

Dans TypeScript, les données peuvent être typées de deux manières principales :

1. **Typage statique** : Le typage statique fait référence à la spécification explicite du type de données des variables et d'autres entités dans le code pendant le développement. Le compilateur TypeScript applique ces définitions de type, aidant à détecter les erreurs liées aux types tôt. Par exemple :
   

```typescript
let age: number = 25;
```

Ici, la variable `age` est explicitement déclarée comme ayant le type `number`. Cela garantit que seules des valeurs numériques peuvent lui être assignées, réduisant le risque d'erreurs d'exécution.

2. **Typage dynamique** : Le typage dynamique dans TypeScript fait référence aux scénarios où le type d'une variable est déterminé à l'exécution. Cela peut se produire lorsque des variables sont assignées au type `any`, qui leur permet de contenir des valeurs de n'importe quel type. TypeScript ne effectue pas de vérification de type sur les opérations impliquant des variables avec le type `any`.
   

```typescript
let value: any;
value = 25; // Nombre
value = "Hello"; // Chaîne de caractères
```

Bien que TypeScript soit principalement un langage à typage statique, le typage dynamique peut encore être utile dans des cas spécifiques, tels que :

* Travailler avec des bibliothèques tierces qui manquent de définitions de types.
   
* Interfacer avec des données structurées dynamiquement (par exemple, des réponses JSON d'API avec des structures inconnues).
   
* Prototypage rapide ou lorsque les informations de type ne sont pas disponibles pendant la phase initiale de développement.
   

### Typage statique vs. dynamique dans TypeScript

Le typage statique est significativement plus courant dans TypeScript, car c'est l'une des fonctionnalités principales qui distingue TypeScript de JavaScript. En appliquant des vérifications de type strictes, le typage statique améliore la maintenabilité du code, réduit les bugs et améliore la productivité des développeurs.

Le typage dynamique est généralement réservé aux cas où la flexibilité est requise ou lors de la manipulation de données dont la structure ne peut pas être déterminée à l'avance. Gardez simplement à l'esprit que le fait de s'appuyer fortement sur le typage dynamique (par exemple, en surutilisant le type `any`) est généralement déconseillé, car cela compromet les avantages du système de typage statique de TypeScript.

Ainsi, bien que le typage dynamique ait sa place dans certains cas particuliers, le typage statique est l'approche préférée et la plus couramment utilisée dans le développement TypeScript.

### Inférence de type et types d'union

#### **Inférence de type**

L'inférence de type est une fonctionnalité puissante de TypeScript qui permet au compilateur de déduire automatiquement le type d'une variable en fonction de la valeur qui lui est assignée lors de l'initialisation. En termes plus simples, TypeScript examine la valeur que vous assignez à une variable et décide quel type elle doit avoir, même si vous ne déclarez pas explicitement le type.

Par exemple :

```typescript
typescriptCopyEditlet age = 25; // TypeScript déduit que 'age' est de type 'number'
age = "hello"; // Erreur : Le type 'string' ne peut pas être assigné au type 'number'
```

Dans cet exemple, la variable `age` est automatiquement déduite comme étant un `number` en raison de sa valeur initiale, `25`. Toute tentative de réassignation de `age` à une valeur d'un type différent (comme une chaîne de caractères) entraînera une erreur de type.

L'inférence de type est particulièrement utile car elle réduit le besoin d'annotations de type explicites, rendant votre code plus propre et plus lisible. Cependant, elle offre toujours la sécurité et la fiabilité de la vérification de type de TypeScript.

##### Quand utiliser l'inférence de type :

* **Assignations simples** : Utilisez l'inférence de type pour des assignations simples où le type est évident à partir de la valeur.
   
* **Valeurs par défaut** : Lorsque vous fournissez des valeurs par défaut pour des variables ou des paramètres de fonction, l'inférence de type garantit que le type correct est appliqué sans nécessiter d'annotations manuelles.
   
* **Prototypage rapide** : Pendant les premières étapes du développement, l'inférence de type peut réduire le code redondant tout en appliquant la sécurité de type.
   

#### **Types d'union**

Les types d'union permettent à une variable de contenir des valeurs de plusieurs types. Ils sont définis en plaçant un pipe (`|`) entre les types. Cette fonctionnalité est particulièrement utile lorsqu'une variable peut légitimement avoir plus d'un type au cours de son cycle de vie.

Par exemple :

```typescript
typescriptCopyEditlet numOrString: number | string; // 'numOrString' peut contenir soit un nombre, soit une chaîne de caractères
numOrString = 25; // Valide
numOrString = "hello"; // Valide
numOrString = true; // Erreur : Le type 'boolean' ne peut pas être assigné au type 'number | string'
```

Vous pouvez même définir des types d'union avec plus de deux types possibles :

```typescript
typescriptCopyEditlet multiType: number | string | boolean;
multiType = 42; // Valide
multiType = "TypeScript"; // Valide
multiType = false; // Valide
```

##### Quand utiliser les types d'union :

* **Paramètres de fonction flexibles** : Lorsqu'une fonction peut accepter plusieurs types d'entrée.
   
   ```typescript
   typescriptCopyEditfunction printValue(value: string | number) {
     console.log(value);
   }
   ```
   
* **Gestion de structures de données diverses** : Lorsque vous travaillez avec des API ou des sources de données externes où les champs peuvent varier en type.
   
* **Variables optionnelles ou multi-états** : Par exemple, une variable qui peut représenter un état de chargement comme un booléen, une erreur comme une chaîne de caractères, ou des données valides comme un objet :
   
   ```typescript
   typescriptCopyEditlet status: boolean | string | { success: boolean; data: any };
   ```
   

## Comment gérer les objets, les tableaux et les types de fonctions dans TypeScript

Pour maîtriser TypeScript, vous devez comprendre les différents types de données supportés dans TypeScript et comment et quand les utiliser.

Les [types primitifs JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#primitive_values) tels que *strings*, *numbers*, *booleans*, et plus encore définissent également les blocs de construction fondamentaux des données dans TypeScript. Mais en particulier, `Objects`, `Arrays` et `Functions` sont essentiels pour construire des applications robustes. Avec les objets, les tableaux et les fonctions, vous pouvez mieux gérer les données et les utiliser efficacement dans le développement.

### Types d'objets dans TypeScript

Les types d'objets représentent le plan pour créer des objets dans TypeScript. Vous pouvez utiliser des objets pour définir leur forme, similaire à la manière dont les [classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes) sont utilisées en **programmation orientée objet (POO)**. Mais les objets manquent des aspects comportementaux et de l'encapsulation que les classes offrent.

Pour définir un type d'objet, définissez explicitement le plan de l'objet après le deux-points (`:`). Par exemple :

```typescript
// Initialisation du type d'objet

let student: {
    name: string;
    age: number;
    matricNumber: string | number;
 };
 
// Assignation de l'objet avec des données réelles

student = {
	name: "Akande"
	age: 21,
	matricNumber: 21/52 + "HP" + 19,
};
```

Remarquez que les propriétés se terminent par un point-virgule `;` au lieu d'une virgule `,` qui les termine dans un objet réel.

Ceci est la manière principale de définir un objet dans TypeScript. Une autre manière est d'utiliser des `interfaces`, que je couvrirai plus tard dans cet article.

### Types de tableaux dans TypeScript

Les tableaux dans TypeScript vous permettent de stocker plusieurs valeurs du même type ou de types différents dans une seule variable. Ils améliorent la sécurité et la clarté de votre code en appliquant une cohérence de type à travers les éléments du tableau.

Dans TypeScript, les types de tableaux peuvent être définis de deux manières :

#### **1. En utilisant le modèle** `Array<type>`

Cette syntaxe utilise le type générique `Array`, où `type` représente le type des éléments que le tableau peut contenir.

```typescript
typescriptCopyEditlet numbers: Array<number> = [1, 2, 3, 4, 5];
let mixedArray: Array<number | string> = [1, 2, 3, 4, 5, "Hello"];
```

* Exemple `numbers` : Ce tableau ne peut contenir que des nombres. Toute tentative d'ajout d'une chaîne de caractères ou d'un autre type à ce tableau entraînera une erreur de type.
   
   ```typescript
   typescriptCopyEditnumbers.push(6); // Valide
   numbers.push("Hello"); // Erreur : Le type 'string' ne peut pas être assigné au type 'number'
   ```
   
* Exemple `mixedArray` : Ce tableau utilise un type d'union (`number | string`), lui permettant de stocker à la fois des nombres et des chaînes de caractères.
   
   ```typescript
   typescriptCopyEditmixedArray.push(42); // Valide
   mixedArray.push("TypeScript"); // Valide
   mixedArray.push(true); // Erreur : Le type 'boolean' ne peut pas être assigné au type 'number | string'
   ```
   

#### **2. En utilisant le modèle** `type[]`

Cette syntaxe ajoute des crochets (`[]`) au type des éléments que le tableau peut contenir.

```typescript
typescriptCopyEditconst numbers: number[] = [1, 2, 3, 4, 5];
const mixedArray: (string | number)[] = [1, 2, 3, 4, 5, "Hello"];
```

* Exemple `numbers` : Similaire à l'exemple `Array<number>`, ce tableau ne peut contenir que des nombres.
   
   ```typescript
   typescriptCopyEditnumbers[0] = 10; // Valide
   numbers.push("Hi"); // Erreur : Le type 'string' ne peut pas être assigné au type 'number'
   ```
   
* Exemple `mixedArray` : Comme le précédent `mixedArray`, ce tableau permet à la fois des nombres et des chaînes de caractères, offrant une flexibilité là où le type de données peut varier.
   
   ```typescript
   typescriptCopyEditmixedArray[1] = "World"; // Valide
   mixedArray.push(true); // Erreur : Le type 'boolean' ne peut pas être assigné au type 'string | number'
   ```
   

### **Comment utiliser les tableaux dans TypeScript**

Les tableaux sont polyvalents et couramment utilisés pour stocker des collections de données liées. Voici quelques scénarios pratiques :

**Stocker des données homogènes :**  
Lorsque tous les éléments du tableau partagent le même type, comme une liste d'ID d'utilisateurs ou de prix de produits :

```typescript
typescriptCopyEditconst userIds: number[] = [101, 102, 103];
const productPrices: Array<number> = [29.99, 49.99, 19.99];
```

**Stocker des données hétérogènes :**  
Lorsque les éléments peuvent avoir différents types, comme une liste de messages contenant du texte et des métadonnées optionnelles :

```typescript
typescriptCopyEditconst messages: (string | object)[] = [
  "Welcome",
  { type: "error", text: "Something went wrong" },
];
```

**Itérer sur les tableaux :**  
Les tableaux dans TypeScript peuvent être utilisés dans des boucles avec une sécurité de type complète :

```typescript
typescriptCopyEditconst scores: number[] = [80, 90, 70];
scores.forEach((score) => console.log(score + 5)); // Ajoute 5 à chaque score
```

**Paramètres de fonction et types de retour :**  
Les tableaux peuvent également être passés comme paramètres de fonction ou retournés par des fonctions avec un typage strict :

```typescript
typescriptCopyEditfunction getNumbers(): number[] {
  return [1, 2, 3];
}
function printStrings(strings: string[]): void {
  strings.forEach((str) => console.log(str));
}
```

### Types de fonctions dans TypeScript

Les types de fonctions dans TypeScript décrivent la forme des fonctions, y compris les types de paramètres et les types de retour. Les types de fonctions sont définis en spécifiant explicitement les types de paramètres lors de la déclaration. Le type de retour est spécifié en ajoutant `:` et le type à retourner immédiatement après les parenthèses. Par exemple :

```typescript
function addition (a: number, b: number): number {
return a + b;
}
```

La fonction ci-dessus prend deux nombres, les additionne et retourne un nombre. La fonction ne fonctionnera pas si l'un de ses arguments n'est pas un nombre et si elle retourne autre chose qu'un nombre. Par exemple :

1. Appeler la fonction avec une chaîne de caractères comme argument :
   

```typescript
// Cela ne fonctionnera pas car il attend des nombres, et l'un des arguments est une chaîne de caractères

addition(1, "two");
```

2. Réécrire la fonction pour retourner une chaîne de caractères :
   

```typescript
// La fonction retournera une erreur car elle retourne une chaîne de caractères

function addition (a: number, b: number): string {
	let result = a + b;
	let returnStatement = `Addition of ${a} and ${b} is: ${result}`;
	return returnStatement;
}
```

Testez le code par vous-même pour voir comment ces exemples fonctionnent.

Comprendre et gérer efficacement les objets, les tableaux et les fonctions dans TypeScript vous permet d'écrire du code sécurisé et maintenable, améliorant la fiabilité et l'évolutivité de vos applications.

## Comment créer des types personnalisés dans TypeScript

Souvent, votre modèle de conception ne suit pas les types de données intégrés dans TypeScript. Par exemple, vous pouvez avoir des modèles qui utilisent la programmation dynamique. Et cela peut causer des problèmes dans votre base de code. TypeScript offre une solution pour créer des **types personnalisés** pour résoudre ce problème.

Les types personnalisés vous permettent de définir votre structure de données et vos formes selon vos besoins. Cela améliore la lisibilité et la maintenabilité du code.

### Le mot-clé Type

Le mot-clé `type` vous permet de créer des **alias de type**, offrant un moyen de créer des types personnalisés. Les types que vous créez peuvent être réutilisés dans toute votre base de code. Les alias de type aident à définir des types d'union ou à combiner des types en un seul alias. La syntaxe pour créer un type personnalisé est la suivante :

```typescript
// Syntaxe

type TypeAlias = type;
```

Et voici un exemple :

![type Example](https://i.ibb.co/qBZ3Zcw/Screenshot-2024-02-16-at-4-17-27-PM.png align="left")

Le code ci-dessus crée un type personnalisé `UserName`, une union de nombres et de chaînes de caractères. Il utilise le type créé pour définir deux variables relativement pour vérifier si le type fonctionne.

Notez qu'il est recommandé de commencer un alias de type par une majuscule.

Le mot-clé Type est généralement utilisé pour les primitives – mais comment créer un type d'objet personnalisé ?

C'est là que les **Interfaces** entrent en jeu.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1737294121435/5be475e2-efae-428e-b9ed-bbcce7ce260d.jpeg align="center")

### Interfaces TypeScript

Les interfaces dans TypeScript sont utilisées pour définir la structure des objets. Elles servent de plans, spécifiant les propriétés qu'un objet doit avoir et leurs types respectifs. Cela garantit que les objets se conforment à une forme cohérente, permettant une sécurité de type et un code plus clair.

#### Définir une interface

Une interface est définie en utilisant le mot-clé `interface`. La syntaxe ressemble à ceci :

```typescript
typescriptCopyEditinterface InterfaceName {
  property1: Type;
  property2: Type;
}
```

#### Exemple :

```typescript
typescriptCopyEditinterface User {
  id: number;
  name: string;
  email: string;
}

const user: User = {
  id: 1,
  name: "Alice",
  email: "alice@example.com",
};
```

Voici ce qui se passe dans cet exemple :

1. **Déclaration de l'interface (**`interface User`):
   
   * Ici, nous définissons un plan pour un objet `User`. Il spécifie que tout objet de type `User` doit avoir les propriétés suivantes :
       
       * `id` de type `number`
           
       * `name` de type `string`
           
       * `email` de type `string`
           
2. **Utilisation de l'interface (**`const user: User`):
   
   * Nous déclarons un objet `user` de type `User`.
       
   * L'objet doit avoir toutes les propriétés définies dans l'interface `User`, avec des valeurs des types spécifiés. Si une propriété est manquante ou si son type ne correspond pas, TypeScript générera une erreur de compilation.
       
   
   Par exemple :
   
   ```typescript
   typescriptCopyEditconst invalidUser: User = {
     id: 1,
     name: "Alice",
     // Erreur : La propriété 'email' est manquante dans le type
   };
   ```
   

Vous vous demandez peut-être pourquoi vous devriez utiliser des interfaces ?

* **Sécurité de type** : Garantit que les objets se conforment à la structure attendue, évitant les erreurs d'exécution.
   
* **Réutilisabilité** : La même interface peut être réutilisée dans différentes parties de l'application, réduisant la duplication.
   
* **Clarté du code** : Rend le code plus facile à lire et à comprendre en décrivant explicitement la forme des objets.
   

#### Fonctionnalités avancées des interfaces

1. **Propriétés optionnelles** : Vous pouvez rendre les propriétés optionnelles en ajoutant un point d'interrogation (`?`).
   
   ```typescript
   typescriptCopyEditinterface Product {
     id: number;
     name: string;
     description?: string; // Propriété optionnelle
   }
   
   const product: Product = {
     id: 101,
     name: "Laptop",
   }; // Valide, car 'description' est optionnelle
   ```
   
2. **Propriétés en lecture seule** : Utilisez `readonly` pour empêcher les propriétés d'être modifiées après l'initialisation.
   
   ```typescript
   typescriptCopyEditinterface Point {
     readonly x: number;
     readonly y: number;
   }
   
   const point: Point = { x: 10, y: 20 };
   point.x = 15; // Erreur : Impossible d'assigner à 'x' car c'est une propriété en lecture seule
   ```
   
3. **Extension d'interfaces** : Les interfaces peuvent hériter des propriétés d'autres interfaces, permettant la composition.
   
   ```typescript
   typescriptCopyEditinterface Person {
     name: string;
     age: number;
   }
   
   interface Employee extends Person {
     employeeId: number;
   }
   
   const employee: Employee = {
     name: "John",
     age: 30,
     employeeId: 1234,
   };
   ```
   

### **Quand utiliser les interfaces**

Il existe divers scénarios où il est judicieux d'utiliser des interfaces. Vous pouvez les utiliser lorsque vous souhaitez définir et appliquer la structure des objets passés dans votre code.

Elles sont également utiles dans les réponses d'API, car elles vous aident à vérifier le type des objets reçus des API. Cela garantit que les données se conforment à vos attentes.

Les interfaces sont également pratiques lorsque vous travaillez avec des types réutilisables. Lorsque plusieurs parties de votre application utilisent des objets avec la même structure, les interfaces évitent la duplication.

En exploitant les interfaces, vous pouvez créer des applications robustes, maintenables et sécurisées. Elles sont une fonctionnalité essentielle de TypeScript qui favorise un code propre et prévisible.

### Génériques et types littéraux

Les **génériques** dans TypeScript vous permettent de créer des composants réutilisables qui peuvent fonctionner avec divers types de données. Ils vous permettent d'écrire des fonctions, des classes et des interfaces sans spécifier le type exact à l'avance, rendant votre code plus flexible et maintenable.

Voici un exemple de fonction générique et d'interface générique dans TypeScript :

```typescript
// Interface générique pour une boîte qui peut contenir n'importe quelle valeur 

interface  Box<T> { 
	value: T; 
}

// Exemples d'utilisation

let  numberBox: Box<number> = { value: 10 };
let  stringBox: Box<string> = { value: "TypeScript" };

console.log(numberBox.value); // Sortie : 10  
console.log(stringBox.value); // Sortie : TypeScript
```

Vous pouvez utiliser des génériques lorsque vous n'êtes pas sûr de votre type de données.

Contrairement aux génériques, les **types littéraux** vous permettent de spécifier des valeurs exactes qu'une variable peut contenir. Cela ajoute une spécificité et une sécurité de type accrues à votre code, empêchant les valeurs non intentionnelles d'être assignées. Voici un exemple :

```typescript
type Direction = 'up' | 'down' | 'left' | 'right';
```

Une variable créée avec le type ci-dessus ne peut être assignée qu'aux chaînes de caractères up, down, left et right.

Globalement, l'utilisation de types personnalisés dans TypeScript vous permet de créer des structures de données expressives, réutilisables et sécurisées, vous aidant à développer des applications plus robustes et maintenables.

## Comment fusionner les types dans TypeScript

La fusion de types dans TypeScript combine plusieurs déclarations de types en un seul type unifié. Cette capacité permet aux développeurs de construire des types complexes à partir de morceaux plus petits et réutilisables, améliorant la clarté du code, la réutilisabilité et la maintenabilité.

### **1. Fusion de déclarations dans les interfaces**

TypeScript supporte la **fusion de déclarations**, où plusieurs déclarations d'interface avec le même nom sont automatiquement combinées en une seule interface. Cela vous permet d'augmenter une interface existante en définissant des propriétés ou méthodes supplémentaires.

##### **Exemple :**

```typescript
typescriptCopyEditinterface User {
  id: number;
  name: string;
}

interface User {
  email: string;
}

const user: User = {
  id: 1,
  name: "Alice",
  email: "alice@example.com",
};
```

##### **Comment cela fonctionne :**

* L'interface `User` est déclarée deux fois, chacune avec des propriétés différentes.
   
* TypeScript fusionne automatiquement ces déclarations en une seule interface :
   
   ```typescript
   typescriptCopyEditinterface User {
     id: number;
     name: string;
     email: string;
   }
   ```
   
* Lorsque vous créez l'objet `user`, toutes les propriétés de l'interface fusionnée doivent être présentes. Si une propriété est manquante, TypeScript générera une erreur.
   

La fusion de déclarations est particulièrement utile lorsque vous travaillez avec des bibliothèques tierces. Vous pouvez étendre ou ajouter de nouvelles propriétés à une interface existante sans modifier le code source de la bibliothèque.

### **2. Fusion d'interfaces en utilisant le mot-clé** `extends`

Le mot-clé `extends` permet à une interface d'hériter des propriétés et méthodes d'une autre, créant une nouvelle interface qui combine les propriétés des deux.

##### **Exemple :**

```typescript
typescriptCopyEditinterface Person {
  name: string;
  age: number;
}

interface Employee extends Person {
  employeeId: number;
}

const employee: Employee = {
  name: "John",
  age: 30,
  employeeId: 101,
};
```

##### **Comment cela fonctionne :**

* L'interface `Person` définit deux propriétés : `name` et `age`.
   
* L'interface `Employee` utilise le mot-clé `extends` pour hériter des propriétés de `Person`.
   
* L'interface `Employee` ajoute également une nouvelle propriété, `employeeId`.
   
* L'objet `employee` doit inclure toutes les propriétés de `Person` et `Employee`.
   

Cette approche est idéale pour les relations hiérarchiques. Par exemple, vous pouvez définir une interface de base pour les propriétés partagées et l'étendre pour des types spécialisés.

### **3. Fusion de types en utilisant l'opérateur** `&`

L'opérateur `&`, connu sous le nom de type d'intersection, permet de combiner plusieurs types en un seul type. Le type résultant inclut toutes les propriétés et méthodes de chaque type.

##### **Exemple :**

```typescript
typescriptCopyEdittype Address = {
  city: string;
  country: string;
};

type ContactInfo = {
  email: string;
  phone: string;
};

type EmployeeDetails = Address & ContactInfo;

const employee: EmployeeDetails = {
  city: "New York",
  country: "USA",
  email: "john.doe@example.com",
  phone: "123-456-7890",
};
```

##### **Comment cela fonctionne :**

* `Address` et `ContactInfo` sont deux types séparés.
   
* `EmployeeDetails` est un type d'intersection créé en utilisant `Address & ContactInfo`.
   
* L'objet `employee` doit inclure toutes les propriétés de `Address` et `ContactInfo`. Les propriétés manquantes ou incorrectement typées entraîneront une erreur TypeScript.
   

Les types d'intersection sont utiles lorsque vous devez combiner des types non liés ou créer des types composites pour des cas d'utilisation spécifiques, comme les réponses d'API qui fusionnent différentes structures de données.

### **Quand utiliser chacune de ces approches**

1. **Fusion de déclarations** : Utilisez lorsque vous souhaitez étendre ou augmenter une interface existante, en particulier dans les bibliothèques tierces ou les bases de code partagées.
   
2. **Mot-clé** `extends` : Utilisez pour les relations hiérarchiques où une interface de base peut être spécialisée en types plus spécifiques.
   
3. **Types d'intersection (**`&`) : Utilisez lorsque vous devez combiner plusieurs types non liés en un seul type pour des cas d'utilisation spécifiques.
   

En comprenant ces techniques de fusion et leurs implications, vous pouvez structurer votre code TypeScript efficacement, améliorant la réutilisabilité et la maintenabilité tout en maintenant la sécurité de type.

## Bundling et transformations dans TypeScript

Tous les navigateurs ne supportent pas le dernier JavaScript utilisé par TypeScript. Vous pouvez donc utiliser le **compilateur TypeScript**, ou `tsc`, pour convertir le code TypeScript (.ts files) en JavaScript conventionnel (.js files) qui est universellement compatible avec tous les navigateurs. `tsc` traduit les éléments spécifiques à TypeScript comme les types et les classes en code JavaScript que les navigateurs peuvent interpréter.

Pour exécuter des fichiers TypeScript, `tsc` est votre outil de prédilection. Vous pouvez installer `tsc` en utilisant npm et ensuite transformer vos fichiers .ts en fichiers .js. Pour utiliser `tsc`, spécifiez simplement le nom du fichier TypeScript avant la commande `tsc`. Par exemple, si vous avez un fichier nommé `app.ts`, vous pouvez l'exécuter en tapant :

```bash
tsc app.ts
```

Webpack ou Parcel sont fréquemment employés pour déployer du code TypeScript sur les navigateurs. Ces outils bundlent tous les fichiers JavaScript, y compris ceux de TypeScript, pour améliorer les performances et faciliter la mise en œuvre du site web. Ils optimisent également le chargement du code en réduisant sa taille et en améliorant la vitesse du navigateur.

## Construire un meilleur code avec TypeScript

Adopter TypeScript en tant que développeur JavaScript ouvre des possibilités pour écrire un code plus robuste et maintenable. En comprenant les bases et les concepts fondamentaux décrits dans ce guide, vous pouvez exploiter le système de typage statique de TypeScript pour détecter les erreurs tôt dans le développement, conduisant à moins de bugs et à une maintenance de code plus fluide.

En utilisant TypeScript, les développeurs JavaScript peuvent améliorer la qualité de leur code et leur productivité. Alors que vous continuez à explorer et à pratiquer avec TypeScript, vous découvrirez encore plus de fonctionnalités et de fonctionnalités puissantes.

Continuez à repousser vos limites et plongez plus profondément dans le monde de TypeScript. 😉