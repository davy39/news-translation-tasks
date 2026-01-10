---
title: Le Guide Définitif de TypeScript – Apprendre TypeScript pour Débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-10T22:26:23.000Z'
originalURL: https://freecodecamp.org/news/the-definitive-typescript-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/ts-1.png
tags:
- name: Career
  slug: career
- name: JavaScript
  slug: javascript
- name: programing
  slug: programing
- name: TypeScript
  slug: typescript
seo_title: Le Guide Définitif de TypeScript – Apprendre TypeScript pour Débutants
seo_desc: 'By Gustavo Azevedo

  TypeScript is the one of the tools people want to learn most, according to a Stack
  Overflow Survey of 90,000 developers.

  TypeScript has exploded in popularity, community size, and adoption over the past
  few years. Today, even Faceb...'
---

Par Gustavo Azevedo

TypeScript est l'un des outils que les gens veulent le plus apprendre, selon une [enquête Stack Overflow](https://insights.stackoverflow.com/survey/2019#most-loved-dreaded-and-wanted) auprès de 90 000 développeurs.

TypeScript a explosé en popularité, en taille de communauté et en adoption au cours des dernières années. Aujourd'hui, même [le projet Jest de Facebook passe à TypeScript](https://github.com/facebook/jest/pull/7554#issuecomment-454358729).

# Qu'est-ce que TypeScript ?

TypeScript est un sur-ensemble statiquement typé de JavaScript qui vise à faciliter le développement de grandes applications JavaScript. Il est également connu sous le nom de _JavaScript qui scale_.

## **Pourquoi utiliser TypeScript ?**

JavaScript a beaucoup évolué au cours des dernières années. C'est le langage le plus polyvalent multiplateforme utilisé à la fois pour le client et le serveur.

Mais JavaScript n'a jamais été conçu pour le développement d'applications à grande échelle. C'est un langage dynamique sans système de types, ce qui signifie qu'une variable peut avoir n'importe quel type de valeur, comme une chaîne de caractères ou un booléen.

Les systèmes de types améliorent la qualité du code, la lisibilité et facilitent la maintenance et le refactoring du code. Plus important encore, les erreurs peuvent être détectées à la compilation plutôt qu'à l'exécution.

Sans système de types, il est difficile de faire évoluer JavaScript pour construire des applications complexes avec de grandes équipes travaillant sur le même code.

TypeScript fournit des garanties entre différentes parties du code au moment de la compilation. Une erreur de compilation vous indique généralement exactement où quelque chose a mal tourné et ce qui a mal tourné, alors qu'une erreur d'exécution est accompagnée d'une trace de pile qui peut être trompeuse et entraîne une quantité significative de temps passé en débogage.

## **Avantages de TypeScript**

1. Détecter les erreurs potentielles plus tôt dans le cycle de développement.
2. Gérer de grandes bases de code.
3. Refactoring plus facile.
4. Faciliter le travail en équipe – Lorsque les contrats dans le code sont plus forts, il est plus facile pour différents développeurs de travailler sur la base de code sans casser accidentellement des choses.
5. Documentation – Les types informent une sorte de documentation que votre futur vous et que d'autres développeurs peuvent suivre.

## Inconvénients de TypeScript

1. C'est quelque chose d'additionnel à apprendre – _C'est un compromis entre un ralentissement à court terme et une amélioration à long terme de l'efficacité et de la maintenance._
2. Les erreurs de type peuvent être incohérentes.
3. La configuration change radicalement son comportement.

# Types

## **Booléen**

```typescript
const isLoading: boolean = false;
```

## **Nombre**

```typescript
const decimal: number = 8;
const binary: number = 0b110;
```

## **Chaîne de caractères**

```typescript
const fruit: string = "orange";
```

## **Tableau**

Les types de tableau peuvent être écrits de l'une des deux manières suivantes :

```typescript
// Le plus courant
let firstFivePrimes: number[] = [2, 3, 5, 7, 11];
// Moins courant. Utilise des types génériques (plus là-dessus plus tard)
let firstFivePrimes2: Array<number> = [2, 3, 5, 7, 11];
```

## **Tuple**

Les types tuple vous permettent d'exprimer un tableau organisé où le type d'un nombre fixe d'éléments est connu. Cela signifie que vous obtiendrez une erreur.

```typescript
let contact: [string, number] = ['John', 954683];
contact = ['Ana', 842903, 'argument supplémentaire']  /* Erreur ! 
Le type '[string, number, string]' n'est pas assignable au type '[string, number]'. */
```

## **Any**

`any` est compatible avec tous les types du système de types, ce qui signifie que n'importe quoi peut lui être assigné et qu'il peut être assigné à n'importe quoi. Il vous donne le pouvoir de vous soustraire à la vérification des types.

```typescript
let variable: any = 'une chaîne';
variable = 5;
variable = false;
variable.someRandomMethod(); /* Okay, 
someRandomMethod pourrait exister à l'exécution. */
```

## **Void**

`void` est l'absence totale de type. Il est couramment utilisé comme type de retour d'une fonction qui ne retourne pas de valeur.

```typescript
function sayMyName(name: string): void {
  console.log(name);
}
sayMyName('Heisenberg');
```

## **Never**

Le type `never` représente le type de valeurs qui ne se produisent jamais. Par exemple, `never` est le type de retour d'une fonction qui lancera toujours une exception ou n'atteindra pas son point final.

```typescript
// lance une exception
function error(message: string): never {
  throw new Error(message);
}

// point final inaccessible
function continuousProcess(): never {
  while (true) {
      // ...
  }
}
```

## **Null** et **Undefined**

`undefined` et `null` ont en réalité leurs propres types nommés `undefined` et `null`, respectivement. Tout comme `void`, ils ne sont pas extrêmement utiles seuls mais deviennent utiles lorsqu'ils sont utilisés dans les types union _(plus là-dessus dans un instant)_

```typescript
type someProp = string | null | undefined;
```

## **Unknown**

TypeScript 3.0 introduit le type `unknown` qui est le pendant sûr en termes de types de `any`. Tout est assignable à `unknown`, mais `unknown` n'est pas assignable à autre chose qu'à lui-même et à `any`. Aucune opération n'est permise sur un `unknown` sans d'abord l'affirmer ou le réduire à un type plus spécifique.

```typescript
type I1 = unknown & null;    // null
type I2 = unknown & string;  // string
type U1 = unknown | null;    // unknown
type U2 = unknown | string;  // unknown
```

## **Alias de Type**

L'alias de type fournit des noms pour les annotations de type vous permettant de l'utiliser à plusieurs endroits. Ils sont créés en utilisant la syntaxe suivante :

```typescript
type Login = string;
```

## **Type Union**

TypeScript nous permet d'utiliser plus d'un type de données pour une propriété. Cela s'appelle le type union.

```typescript
type Password = string | number;
```

## **Type Intersection**

Les types intersection sont des types qui combinent les propriétés de tous les types membres.

```typescript
interface Person {
  name: string;
  age: number;
}

interface Worker {
  companyId: string;
}

type Employee = Person & Worker;

const bestOfTheMonth: Employee = {
  name: 'Peter'
  age: 39,
  companyId: '123456'
```

# Interface

Les interfaces sont comme un contrat entre vous et le compilateur dans lequel vous spécifiez en une seule annotation nommée exactement quelles propriétés attendre avec leurs annotations de type respectives. 
_Note de bas de page : Les interfaces n'ont aucun impact sur le runtime JS, elles sont utilisées uniquement pour la vérification de type._

* Vous pouvez déclarer des **propriétés optionnelles** en les marquant avec un `?`, ce qui signifie que les objets de l'interface peuvent ou non définir ces propriétés.
* Vous pouvez déclarer des **propriétés en lecture seule**, ce qui signifie qu'une fois qu'une propriété est assignée à une valeur, elle ne peut pas être changée.

```typescript
interface ICircle {
  readonly id: string;
  center: {
    x: number;
    y: number;
  },
  radius: number;
  color?: string;  // Propriété optionnelle
}
  
const circle1: ICircle = {
  id: '001',
  center: { x: 0 },
  radius: 8,
};  /* Erreur ! La propriété 'y' est manquante dans le type '{ x: number; }' 
mais requise dans le type '{ x: number; y: number; }'. */

const circle2: ICircle = {
  id: '002',
  center: { x: 0, y: 0 },
  radius: 8,
}  // Okay

circle2.color = '#666';  // Okay
circle2.id = '003';  /* Erreur ! 
Impossible d'assigner à 'id' car c'est une propriété en lecture seule. */
```

## **Extension d'Interfaces**

Les interfaces peuvent étendre une ou plusieurs interfaces. Cela rend l'écriture des interfaces flexible et réutilisable.

```typescript
interface ICircleWithArea extends ICircle {
  getArea: () => number;
}

const circle3: ICircleWithArea = {
  id: '003',
  center: { x: 0, y: 0 },
  radius: 6,
  color: '#fff',
  getArea: function () {
    return (this.radius ** 2) * Math.PI;
  },
};
```

## Implémentation d'une Interface

Une classe implémentant une interface doit strictement se conformer à la structure de l'interface.

```typescript
interface IClock {
  currentTime: Date;
  setTime(d: Date): void;
}

class Clock implements IClock {
  currentTime: Date = new Date();
  setTime(d: Date) {
    this.currentTime = d;
  }
  constructor(h: number, m: number) { }
}
```

# **Énumérations**

Une `enum` (ou énumération) est un moyen d'organiser une collection de valeurs liées qui peuvent être des valeurs numériques ou des chaînes de caractères.

```typescript
enum CardSuit {
  Clubs,
  Diamonds,
  Hearts,
  Spades
}

let card = CardSuit.Clubs;

card = "not a card suit"; /* Erreur ! Le type '"not a card suit"' 
n'est pas assignable au type 'CardSuit'. */
```

Sous le capot, les énumérations sont basées sur des nombres par défaut. Les valeurs `enum` commencent à zéro et s'incrémentent de 1 pour chaque membre.

Le code JavaScript généré par notre exemple précédent :

```typescript
var CardSuit;
(function (CardSuit) {
  CardSuit[CardSuit["Clubs"] = 0] = "Clubs";
  CardSuit[CardSuit["Diamonds"] = 1] = "Diamonds";
  CardSuit[CardSuit["Hearts"] = 2] = "Hearts";
  CardSuit[CardSuit["Spades"] = 3] = "Spades";
})(CardSuit || (CardSuit = {}));

/**
 * Ce qui résulte en l'objet suivant :
 * {
 *   0: "Clubs",
 *   1: "Diamonds",
 *   2: "Hearts",
 *   3: "Spades",
 *   Clubs: 0,
 *   Diamonds: 1,
 *   Hearts: 2,
 *   Spades: 3
 * }
 */
```

Alternativement, les énumérations peuvent être initialisées avec des valeurs de chaîne, ce qui est une approche plus lisible.

```typescript
enum SocialMedia {
  Facebook = 'FACEBOOK',
  Twitter = 'TWITTER',
  Instagram = 'INSTAGRAM',
  LinkedIn = 'LINKEDIN'
}
```

## Mappage Inverse

`enum` supporte le mappage inverse, ce qui signifie que nous pouvons accéder à la valeur d'un membre ainsi qu'au nom d'un membre à partir de sa valeur. 
Revenons à notre exemple CardSuit :

```typescript
const clubsAsNumber: number = CardSuit.Clubs; // 3
const clubsAsString: string = CardSuit[0];    // 'Clubs'
```

# **Fonctions**

Vous pouvez ajouter des types à chacun des paramètres et ensuite à la fonction elle-même pour ajouter un type de retour.

```typescript
function add(x: number, y: number): number {
  return x + y;
}
```

## Surcharge de Fonctions

TypeScript vous permet de déclarer des _surcharges de fonctions_. Basiquement, vous pouvez avoir plusieurs fonctions avec le même nom mais des types de paramètres et de retour différents. Considérez l'exemple suivant :

```typescript
function padding(a: number, b?: number, c?: number, d?: any) {
  if (b === undefined && c === undefined && d === undefined) {
    b = c = d = a;
  }
  else if (c === undefined && d === undefined) {
    c = a;
    d = b;
  }
  return {
    top: a,
    right: b,
    bottom: c,
    left: d
  };
}
```

La signification de chaque paramètre change en fonction du nombre de paramètres passés à la fonction. De plus, cette fonction attend uniquement un, deux ou quatre paramètres. Pour créer une surcharge de fonction, vous déclarez simplement l'en-tête de la fonction plusieurs fois. Le dernier en-tête de fonction est celui qui est réellement actif _à l'intérieur_ du corps de la fonction mais n'est pas disponible pour le monde extérieur.

```typescript
function padding(all: number);
function padding(topAndBottom: number, leftAndRight: number);
function padding(top: number, right: number, bottom: number, left: number);
function padding(a: number, b?: number, c?: number, d?: number) {
  if (b === undefined && c === undefined && d === undefined) {
    b = c = d = a;
  }
  else if (c === undefined && d === undefined) {
    c = a;
    d = b;
  }
  return {
    top: a,
    right: b,
    bottom: c,
    left: d
  };
}

padding(1);       // Okay
padding(1,1);     // Okay
padding(1,1,1,1); // Okay
padding(1,1,1);   /* Erreur ! Aucune surcharge n'attend 3 arguments, mais
des surcharges existent qui attendent soit 2 soit 4 arguments. */
```

# **Classes**

Vous pouvez ajouter des types aux propriétés et aux arguments des méthodes.

```typescript
class Greeter {
  greeting: string;
  constructor(message: string) {
    this.greeting = message;
  }
  greet(name: string) {
    return `Hi ${name}, ${this.greeting}`;
  }
}
```

## **Modificateurs d'Accès**

TypeScript supporte les modificateurs `public`, `private`, `protected`, qui déterminent l'accessibilité d'un membre de classe.

* Un membre `public` fonctionne de la même manière que les membres JavaScript simples et est le modificateur par défaut.
* Un membre `private` ne peut pas être accédé depuis l'extérieur de sa classe conteneur.
* Un membre `protected` diffère d'un membre privé car il peut également être accédé dans les classes dérivées.

```markdown
| Accessible sur  | public | protected | private |
| :------------- | :----: | :-------: | :-----: |
| classe          |   oui  |    oui    |   oui   |
| enfants de classe |   oui  |    oui    |    non   |
| instance de classe |   oui  |     non    |    non   |
```

## **Modificateur Readonly**

Une propriété `readonly` doit être initialisée à sa déclaration ou dans le constructeur.

```typescript
class Spider {
  readonly name: string;
  readonly numberOfLegs: number = 8;
  constructor (theName: string) {
    this.name = theName;
  }
}
```

## **Propriétés de Paramètre**

Les _propriétés de paramètre_ vous permettent de créer et d'initialiser un membre en un seul endroit. Elles sont déclarées en préfixant un paramètre de constructeur avec un modificateur.

```typescript
class Spider {
  readonly numberOfLegs: number = 8;
  constructor(readonly name: string) {
  }
}
```

## **Abstract**

Le mot-clé abstract peut être utilisé à la fois pour les classes et pour les méthodes de classe abstraites.

* **Les classes abstraites** ne peuvent pas être instanciées directement. Elles sont principalement destinées à l'héritage où la classe qui étend la classe abstraite doit définir toutes les méthodes abstraites.
* **Les membres abstraits** ne contiennent pas d'implémentation, donc ne peuvent pas être accédés directement. Ces membres doivent être implémentés dans les classes enfants _(un peu comme une interface)_

# **Assertion de Type**

TypeScript vous permet de remplacer ses types inférés de la manière que vous souhaitez. Cela est utilisé lorsque vous avez une meilleure compréhension du type d'une variable que le compilateur seul.

```typescript
const friend = {};
friend.name = 'John';  // Erreur ! La propriété 'name' n'existe pas sur le type '{}'

interface Person {
  name: string;
  age: number;
}

const person = {} as Person;
person.name = 'John';  // Okay
```

À l'origine, la syntaxe pour l'assertion de type était <type>

```typescript
let person = <Person> {};
```

Mais cela a créé une ambiguïté lorsqu'il était utilisé dans JSX. Par conséquent, il est recommandé d'utiliser `as` à la place.

Les assertions de type sont généralement utilisées lors de la migration de code depuis JavaScript et vous pouvez connaître un type plus précis de la variable que ce qui est actuellement assigné. Mais l'assertion peut être **considérée comme dangereuse.**

Prenons un exemple avec notre interface Person de l'exemple précédent. Avez-vous remarqué quelque chose de mal ? Si vous avez remarqué la propriété manquante **age**, félicitations ! Le compilateur pourrait vous aider en fournissant l'autocomplétion pour les propriétés de Person mais il ne se plaindra pas si vous manquez des propriétés.

# **Inférence de Type**

TypeScript infère les types de variables lorsqu'il n'y a pas d'information explicite disponible sous forme d'annotations de type.

```typescript
/**
 * Définition de variable
 */
let a = "une chaîne";
let b = 1;
a = b;  // Erreur ! Le type 'number' n'est pas assignable au type 'string'.

// Dans le cas d'objets complexes, TypeScript cherche le type le plus commun
// pour inférer le type de l'objet.
const arr = [0, 1, false, true];  // (number | boolean)[]


/**
 * Types de retour de fonction
 */
function sum(x: number, y: number) {
  return x + y;  // infère pour retourner un nombre
}
```

# **Compatibilité de Type**

La compatibilité de type est basée sur la typage structurel, qui relie les types uniquement en fonction de leurs membres.

La règle de base pour le type structurel est que `x` est compatible avec `y` si `y` a au moins les mêmes membres que `x`.

```typescript
interface Person {
  name: string;
}

let x: Person;  // Okay, malgré le fait de ne pas être une implémentation de l'interface Person
let y = { name: 'John', age: 20 };  // type { name: string; age: number }
x = y;

// Veuillez noter que x est toujours de type Person. 
// Dans l'exemple suivant, le compilateur affichera un message d'erreur car il ne
// s'attend pas à la propriété age dans Person mais le résultat sera comme prévu :
console.log(x.age); // 20
```

Comme `y` a un membre `name: string`, il correspond aux propriétés requises pour l'interface Person, ce qui signifie que `x` est un sous-type de `y`. Ainsi, l'assignation est autorisée.

## _Fonctions_

**Nombre d'arguments**  
Dans un appel de fonction, vous devez passer au moins assez d'arguments, ce qui signifie que les arguments supplémentaires ne causeront aucune erreur.

```typescript
function consoleName(person: Person) {
  console.log(person.name);
}
consoleName({ name: 'John' });           // Okay
consoleName({ name: 'John', age: 20 });  // Argument supplémentaire toujours Okay
```

**Type de retour**  
Le type de retour doit contenir au moins assez de données.

```typescript
let x = () => ({name: 'John'});
let y = () => ({name: 'John', age: 20 });
x = y;  // OK
y = x;  /* Erreur ! La propriété 'age' est manquante dans le type '{ name: string; }'
mais requise dans le type '{ name: string; age: number; }' */
```

# **Garde de Type**

Les gardes de type vous permettent de réduire le type d'un objet dans un bloc conditionnel.

## **typeof**

En utilisant typeof dans un bloc conditionnel, le compilateur saura que le type d'une variable est différent. Dans l'exemple suivant, TypeScript comprend qu'en dehors du bloc conditionnel, `x` pourrait être un booléen et que la fonction `toFixed` ne peut pas être appelée dessus.

```typescript
function example(x: number | boolean) {
  if (typeof x === 'number') {
    return x.toFixed(2);
  }
  return x.toFixed(2); // Erreur ! La propriété 'toFixed' n'existe pas sur le type 'boolean'.
}
```

## **instanceof**

```typescript
class MyResponse {
  header = 'header example';
  result = 'result example';
  // ...
}
class MyError {
  header = 'header example';
  message = 'message example';
  // ...
}
function example(x: MyResponse | MyError) {
  if (x instanceof MyResponse) {
    console.log(x.message); // Erreur ! La propriété 'message' n'existe pas sur le type 'MyResponse'.
    console.log(x.result);  // Okay
  } else {
    // TypeScript sait que ceci doit être MyError

    console.log(x.message); // Okay
    console.log(x.result);  // Erreur ! La propriété 'result' n'existe pas sur le type 'MyError'.
  }
}
```

## **in**

L'opérateur `in` vérifie l'existence d'une propriété sur un objet.

```typescript
interface Person {
  name: string;
  age: number;
}

const person: Person = {
  name: 'John',
  age: 28,
};

const checkForName = 'name' in person; // true
```

# **Types Littéraux**

Les littéraux sont des _valeurs exactes_ qui sont des primitives JavaScript. Ils peuvent être combinés dans une union de types pour créer des abstractions utiles.

```typescript
type Orientation = 'landscape' | 'portrait';
function changeOrientation(x: Orientation) {
  // ...
}
changeOrientation('portrait'); // Okay
changeOrientation('vertical'); /* Erreur ! L'argument de type '"vertical"' n'est pas 
assignable au paramètre de type 'Orientation'. */
```

## **Types Conditionnels**

Un type conditionnel décrit un test de relation de type et sélectionne l'un des deux types possibles, en fonction du résultat de ce test.

```typescript
type X = A extends B ? C : D;
```

Cela signifie que si le type `A` est assignable au type `B`, alors `X` est du même type que `C`. Sinon, `X` est du même type que `D`;

# **Types Génériques**

Un type générique est un type qui doit inclure ou référencer un autre type pour être complet. Il impose des contraintes significatives entre diverses variables.  
Dans l'exemple suivant, une fonction retourne un tableau de n'importe quel type que vous passez.

```typescript
function reverse<T>(items: T[]): T[] {
  return items.reverse();
}
reverse([1, 2, 3]); // number[]
reverse([0, true]); // (number | boolean)[]
```

## **keyof**

L'opérateur `keyof` interroge l'ensemble des clés pour un type donné.

```typescript
interface Person {
  name: string;
  age: number;
}
type PersonKeys = keyof Person; // 'name' | 'age'
```

## **Types Mappés**

Les types mappés vous permettent de créer de nouveaux types à partir de types existants en mappant sur les types de propriétés. Chaque propriété du type existant est transformée selon une règle que vous spécifiez.

## **Partial**

```typescript
type Partial<T> = {
  [P in keyof T]?: T[P];
}
```

* Le type générique Partial est défini avec un seul paramètre de type `T`.
* `keyof T` représente l'union de tous les noms de propriétés de `T` en tant que types littéraux de chaîne.
* `[P in keyof T]?: T[P]` indique que le type de chaque propriété `P` de type `T` doit être optionnel et transformé en `T[P]`.
* `T[P]` représente le type de la propriété `P` du type `T`.

## **Readonly**

Comme nous l'avons couvert dans la section Interface, TypeScript vous permet de créer des propriétés en lecture seule. Il existe un type `Readonly` qui prend un type `T` et définit toutes ses propriétés comme readonly.

```typescript
type Readonly<T> = {
  readonly [P in keyof T]: T[P];
};
```

## **Exclude**

`Exclude` vous permet de supprimer certains types d'un autre type. `Exclude` de `T` tout ce qui est assignable à `T`.

```typescript
/**
 * type Exclude<T, U> = T extends U ? never : T;
 */
type User = {
  _id: number;
  name: string;
  email: string;
  created: number;
};

type UserNoMeta = Exclude<keyof User, '_id' | 'created'>
```

## **Pick**

`Pick` vous permet de choisir certains types d'un autre type. `Pick` de `T` tout ce qui est assignable à `T`.

```typescript
/**
 * type Pick<T, K extends keyof T> = {
 *   [P in K]: T[P];
 *  };
 */
type UserNoMeta = Pick<User, 'name' | 'email'>
```

## _infer_

Vous pouvez utiliser le mot-clé `infer` pour inférer une variable de type dans la clause `extends` d'un type conditionnel. Une telle variable de type inférée ne peut être utilisée que dans la branche vraie du type conditionnel.

## **ReturnType**

Obtient le type de retour d'une fonction.

```typescript
/**
 * ReturnType original de TypeScript
 * type ReturnType<T extends (...args: any) => any> = T extends (...args: any) => infer R ? R : any;
 */
type MyReturnType<T> = T extends (...args: any) => infer R ? R : any;

type TypeFromInfer = MyReturnType<() => number>;  // number
type TypeFromFallback = MyReturnType<string>;     // any
```

Décomposons `MyReturnType` :

* Le type de retour de `T` est ...
* Tout d'abord, est-ce que `T` est une fonction ?
* Si oui, alors le type se résout au type de retour inféré `R`.
* Sinon, le type se résout à `any`.

# Références & Liens Utiles

[https://basarat.gitbooks.io/typescript/](https://basarat.gitbooks.io/typescript/)

[https://www.typescriptlang.org/docs/home.html](https://www.typescriptlang.org/docs/home.html)

[https://www.tutorialsteacher.com/typescript](https://www.tutorialsteacher.com/typescript)

[https://github.com/dzharii/awesome-typescript](https://github.com/dzharii/awesome-typescript)

[https://github.com/typescript-cheatsheets/react-typescript-cheatsheet](https://github.com/typescript-cheatsheets/react-typescript-cheatsheet)

---

Afin d'étudier et d'essayer TypeScript, j'ai construit une simple application CurrencyConverter en utilisant TS et React-Native avec des hooks. Vous pouvez vérifier ce projet [ici](https://github.com/gustavoaz7/React-Native_Learning/tree/master/CurrencyConverter).

Merci et félicitations pour avoir lu jusqu'à ce point ! Si vous avez des pensées à ce sujet, n'hésitez pas à laisser un commentaire.

Vous pouvez me trouver sur [Twitter](https://twitter.com/intent/follow?screen_name=gustavoaz7_).