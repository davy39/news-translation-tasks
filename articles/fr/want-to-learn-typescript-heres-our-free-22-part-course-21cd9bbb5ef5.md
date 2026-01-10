---
title: Apprenez TypeScript gratuitement avec ce cours interactif Scrimba
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-16T14:13:21.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-typescript-heres-our-free-22-part-course-21cd9bbb5ef5
coverImage: null
tags:
- name: JavaScript
  slug: javascript
- name: learn to code
  slug: learn-to-code
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: Apprenez TypeScript gratuitement avec ce cours interactif Scrimba
seo_desc: 'By Per Harald Borgen

  Click on the image to go to the Scrimba course

  TypeScript has been gaining a lot of popularity amongst JavaScript developers in
  the last few years. And it’s no wonder, as TypeScript code tends to be less error-prone,
  more readabl...'
---

Par Per Harald Borgen

[![Bannière du cours TypeScript](https://www.freecodecamp.org/news/content/images/2019/12/Screenshot-2019-12-04-at-06.35.08.png)](https://scrimba.com/g/gintrototypescript?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrototypescript_launch_article)*Cliquez sur l'image pour accéder au cours Scrimba*

TypeScript a gagné en popularité auprès des développeurs JavaScript ces dernières années. Et ce n'est pas surprenant, car le code TypeScript tend à être moins sujet aux erreurs, plus lisible et plus facile à maintenir.

Nous nous sommes donc associés à l'éminent instructeur en ligne [Dylan C. Israel](https://medium.com/u/7f21f9c02e5b) et avons créé un [cours gratuit sur TypeScript sur Scrimba](https://scrimba.com/g/gintrototypescript?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrototypescript_launch_article). Le cours contient 22 leçons et est **destiné aux personnes qui connaissent déjà JavaScript** mais qui veulent une introduction rapide à TypeScript.

Suivez le cours [gratuitement ici](https://scrimba.com/g/gintrototypescript?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrototypescript_launch_article).

Examinons maintenant chacune des leçons du cours.

### Partie #1 : Introduction

![Image](https://cdn-media-1.freecodecamp.org/images/1*_I4oz78IStdFL_PMkHNBpA.png)

Dans la vidéo d'introduction, Dylan donne un aperçu des raisons pour lesquelles vous devriez apprendre TypeScript, et de la manière dont le cours est structuré. Il vous parle également un peu de lui, afin que vous soyez familiarisé avec lui avant de plonger dans le code.

### Partie #2 : Types de variables

La vérification des types au moment de la compilation est l'une des fonctionnalités les plus importantes de TypeScript. Elle nous permet de détecter les erreurs liées aux types de données au moment de la compilation. Cette leçon explique les types de données disponibles dans TypeScript.

```ts
let firstName: string;

let age: number;

let isMarried: boolean;

```

Vous pouvez voir comment nous avons attaché des types à toutes les variables. Si nous essayons de mettre une valeur de chaîne à la place d'une variable de type nombre, TypeScript la détectera au moment de la compilation.

### Partie #3 : Types multiples

Dans TypeScript, nous gardons un seul type pour une variable, mais ce n'est pas toujours possible. TypeScript nous fournit donc le type `any`. Cela signifie que nous pouvons assigner plusieurs types de valeurs à une seule variable.

```ts
let myVariable: any = 'Hello World';  
myVariable = 10;  
myVariable = false;

```

Ci-dessus, nous avons déclaré `myVariable` avec le type `any`. Nous lui avons d'abord assigné une chaîne, puis un nombre, et enfin un booléen. Cela est possible grâce au type `any`.

### Partie #4 : Sous-types

Les sous-types sont utilisés lorsque nous ne connaissons pas la valeur de la variable. TypeScript nous fournit deux sous-types : `null` et `undefined`. Cette leçon explique quand nous devons utiliser l'un ou l'autre.

```ts
let myVariable: number = undefined;

```

La variable `myVariable` a été assignée à la valeur `undefined` car, à ce stade, nous ne savons pas ce qu'elle sera. Nous pouvons également utiliser `null` ici.

### Partie #5 : Typage implicite vs explicite

La partie 5 parle de la différence entre le typage implicite et explicite. Dans les exemples ci-dessus, nous avons vu des types explicites où nous définissons le type de la variable. Le typage implicite, en revanche, est effectué par le compilateur sans que nous déclarions le type de la variable.

```ts
let myVariable = 'Hello World';

```

Dans cet exemple, nous n'avons pas assigné de type à la variable. Nous pouvons vérifier le type de cette variable en utilisant la fonction `typeof`. Cela montrera que `myVariable` est de type `string` car le compilateur s'est occupé du typage.

### Partie #6 : Vérification des types

Dans cette leçon, nous apprendrons comment vérifier le type d'une variable, et détecter toute erreur ou effectuer toute opération. Elle utilise un exemple dans lequel nous testons si notre variable est de type `Bear` (où `Bear` est une `class`). Si nous voulons vérifier le type de notre variable, nous pouvons utiliser la méthode `instanceof`.

```ts
import { Bear } from 'somefile.ts';  
let bear = new Bear(3);  
if (bear instanceof Bear) {  
   //effectuer une opération  
}

```

### Partie #7 : Assertions de type

L'assertion de type signifie que nous pouvons convertir une variable en un type particulier, et nous disons à TypeScript de traiter cette variable en utilisant ce type. Essayons de comprendre cela avec un exemple :

```ts
let variable1: any = 'Hello World';  
if ((variable1 as string).length) {  
   //effectuer une opération  
}

```

`variable1` a le type `any`. Mais, si nous voulons vérifier sa longueur, cela produira une erreur jusqu'à ce que nous disions à TypeScript de la traiter comme une chaîne. Cette leçon explique plus de détails sur ce concept.

### Partie #8 : Tableaux

Cette partie du cours explique les tableaux TypeScript. En JavaScript, lorsque nous assignons des valeurs à un tableau, nous pouvons y mettre différents types d'éléments. Mais, avec TypeScript, nous pouvons déclarer un tableau avec des types également.

```ts
let array1: number[] = [1, 2, 3, 4, 5];

```

Dans l'exemple ci-dessus, nous avons déclaré un tableau de nombres en lui assignant le type `number`. Maintenant, TypeScript s'assurera que le tableau ne contient que des nombres.

### Partie #9 : Tuples

Parfois, nous devons stocker plusieurs types de valeurs dans une seule collection. Les tableaux ne serviront pas dans ce cas. TypeScript nous donne le type de données des tuples. Ceux-ci sont utilisés pour stocker des valeurs de plusieurs types.

```ts
let tuple_name = [10, 'Hello World'];

```

Cet exemple montre que nous pouvons avoir des éléments de données de types nombre **et** chaîne dans une seule collection. Cette leçon explique le concept des tuples plus en détail.

### Partie #10 : Enums

Dans cette leçon, nous apprendrons les enums dans TypeScript. Les enums sont utilisés pour définir un ensemble de constantes nommées qui peuvent être utilisées pour documenter l'intention ou pour créer un ensemble de cas différents.

```ts
**enum** Direction {   
   Up = "UP",       
   Down = "DOWN",       
   Left = "LEFT",      
   Right = "RIGHT"   
}

```

Voici un exemple de base de la manière dont les enums sont déclarés, et de la manière dont différentes propriétés sont créées à l'intérieur. Le reste des détails est expliqué dans cette section du cours.

### Partie #11 : Objet

En JavaScript, les objets jouent un rôle assez majeur dans la manière dont le langage a été défini et a évolué. Cette leçon parle des objets dans TypeScript — comment déclarer un objet, et quels types de valeurs peuvent être inclus dans le type objet.

### Partie #12 : Paramètres

En utilisant TypeScript, nous pouvons également assigner des types aux paramètres d'une fonction. Dans cette section du cours, Dylan explique comment nous pouvons ajouter des types aux paramètres. C'est une manière très utile de gérer les erreurs concernant le type de données dans une fonction.

```ts
const multiply = (num1: number, num2: number) => {   
   return num1 * num2;  
}

```

Nous avons déclaré une fonction `multiply` qui prend deux paramètres et retourne la valeur de leur multiplication. Nous avons ajouté un type `number` aux deux paramètres afin que seule une valeur numérique puisse leur être passée.

### Partie #13 : Types de retour

Comme pour les paramètres, nous pouvons également ajouter une vérification de type à la valeur de retour d'une fonction. De cette manière, nous pouvons nous assurer que la valeur de retour d'une fonction a un type attendu. Cette partie du cours explique le concept en détail.

```ts
const multiply = (num1: number, num2: number): number => {   
   return num1 * num2;  
}

```

Nous avons ajouté un type de `return` de `number` à la fonction. Maintenant, si nous retournons autre chose qu'un `number`, cela nous montrera une erreur.

### Partie #14 : Types personnalisés

Dans TypeScript, nous pouvons créer un type personnalisé en utilisant le mot-clé `type`. Nous pouvons ensuite vérifier le type des objets sur la base de ce type.

```ts
type person = {firstName: string};

const example3: person = {firstName: 'Dollan'};

```

Cette fonctionnalité est presque obsolète dans TypeScript, vous devriez donc plutôt utiliser `interface` ou `class` à cette fin. Cependant, il est important que vous la connaissiez, car vous pourriez rencontrer des types personnalisés lorsque vous commencerez à plonger dans le code TS.

### Partie #15 : Interfaces

Dans TypeScript, l'accent principal est mis sur la vérification des types qui impose l'utilisation d'un type particulier. Les interfaces sont un moyen de nommer ces types. C'est essentiellement un groupe de méthodes et de propriétés liées qui décrivent un objet. Cette partie du cours explique comment créer et utiliser des interfaces.

```ts
interface Person {  
   firstName: string,   
   lastName: string,  
   age: number  
}

```

Dans l'exemple ci-dessus, nous avons une interface `Person` qui a quelques propriétés typées. Notez que nous n'initialisons pas les données dans les interfaces, mais définissons plutôt les types que les paramètres auront.

### Partie #16 : Barrels

Un barrel est un moyen de regrouper les exports de plusieurs modules en un seul module. Un barrel est lui-même un module, qui exporte plusieurs modules à partir d'un seul fichier. Cela signifie qu'un utilisateur n'a qu'à importer un seul module au lieu de tous les modules séparément.

```ts
// Sans barrel  
import { Foo } from '../demo/foo';  
import { Bar } from '../demo/bar';  
import { Baz } from '../demo/baz';`

```

Au lieu d'utiliser ces multiples lignes séparément pour importer ces modules, nous pouvons créer un barrel. Le barrel exporterait tous ces modules et nous n'importerions que ce barrel.

```ts
// demo/barrel.ts export * from './foo'; 
// ré-exporter toutes ses exports
export * from './bar'; 
// ré-exporter toutes ses exports
export * from './baz'; 
// ré-exporter toutes ses exports

```

Nous pouvons simplement créer un fichier TypeScript et exporter les modules depuis leurs fichiers respectifs. Nous pouvons ensuite importer ce barrel partout où nous en avons besoin.

```ts
import { Foo, Bar, Baz } from '../demo'; // demo/barrel.ts

```

### Partie #17 : Modèles

Lorsque nous utilisons des interfaces, nous sommes souvent confrontés à un certain nombre de problèmes. Par exemple, les interfaces ne semblent pas pouvoir imposer quoi que ce soit provenant du côté serveur, et elles ne peuvent pas conserver la valeur par défaut. Pour résoudre ce problème, nous utilisons le concept des classes de modèles. Celles-ci agissent comme une interface, et peuvent également avoir des valeurs par défaut et des méthodes ajoutées.

### Partie #18 : Types d'intersection

Dans cette section, nous parlerons des types d'intersection. Ce sont les moyens par lesquels nous pouvons utiliser plusieurs types pour une seule entité ou classe. Parfois, nous devons utiliser plusieurs types pour mapper une entité et, à ce moment-là, cette fonctionnalité est très pratique.

```ts
import { FastFood, ItalianFood, HealthyFood} from ./interfaces;  
let food1: FastFood | HealthyFood;  
let food2: ItalianFood;  
let food3: FastFood;  
let food4: FastFood & ItalianFood;

```

Dans l'exemple ci-dessus, nous avons trois interfaces et nous créons différents objets à partir d'elles. Par exemple, `food1` sera soit `FastFood` **soit** `HealthyFood`. De même, `food4` sera `FastFood` **ainsi que** `ItalianFood`.

### Partie #19 : Génériques

En bref, les génériques sont un moyen de créer des composants réutilisables qui peuvent fonctionner sur une variété de types de données plutôt que sur un seul.

Le concept de génériques n'est en fait pas encore disponible en JavaScript, mais il est largement utilisé dans des langages orientés objet populaires tels que C# ou Java. Dans cette leçon, nous apprendrons comment utiliser les génériques dans TypeScript, et examinerons ses principaux avantages.

### Partie #20 : Modificateurs d'accès

L'idée des modificateurs d'accès est relativement nouvelle dans le domaine de JavaScript et TypeScript, mais ils sont disponibles dans d'autres langages orientés objet depuis longtemps. Les modificateurs d'accès contrôlent l'accessibilité des membres d'une classe.

Dans TypeScript, il existe deux modificateurs d'accès : public et private. Chaque membre d'une classe est public par défaut jusqu'à ce que vous le déclariez autrement.

```ts
class Customer {  
   customerId: number;  
   public companyName: string;  
   private address: string;  
}

```

`customerId` est un membre public par défaut, il est donc toujours disponible pour le monde extérieur. Nous avons spécifiquement déclaré `companyName` comme `public`, il sera donc également disponible en dehors de la classe. `address` est marqué comme `private`, il ne sera donc pas accessible en dehors de la classe.

### Partie #21 : Installation locale

Dans cette leçon, nous apprendrons les étapes pour installer et exécuter TypeScript sur des ordinateurs locaux. Ces étapes impliquent généralement l'installation de Node et TypeScript, puis la compilation des fichiers .ts.

![Cliquez sur l'image pour accéder au cours](https://cdn-media-1.freecodecamp.org/images/1*UYc7PRwJOGev2v0n5qQJuA.png)

_Cliquez sur l'image pour accéder au cours._

### Partie #22 : TSLint et bravo !

Hourra ! Vous avez terminé le cours. Dans la dernière partie de la vidéo, Dylan donnera quelques conseils sur la manière de poursuivre cet apprentissage et d'améliorer le code que nous écrivons aujourd'hui.

Dans cette leçon, il couvre également comment vous pouvez utiliser l'incroyable TSLint. Cet outil vous aide à écrire un meilleur code de niveau production en utilisant les meilleures pratiques et conventions. Il propose quelques paramètres de base que vous pouvez modifier pour répondre à vos besoins.

#### Alors, allez-y et suivez [ce cours gratuit aujourd'hui !](https://scrimba.com/g/gintrototypescript?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrototypescript_launch_article)

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le co-fondateur de [Scrimba](https://scrimba.com) — la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de conception web responsive](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=gintrototypescript_launch_article) si vous voulez apprendre à construire des sites web modernes de manière professionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=gintrototypescript_launch_article)_