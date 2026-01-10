---
title: Comment fonctionnent les génériques TypeScript – Expliqué avec des exemples
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-02-27T13:45:54.000Z'
originalURL: https://freecodecamp.org/news/how-typescript-generics-work
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Neon-Green-Bold-Quote-Motivational-Tweet-Instagram-Post.png
tags:
- name: TypeScript
  slug: typescript
seo_title: Comment fonctionnent les génériques TypeScript – Expliqué avec des exemples
seo_desc: 'TypeScript, with its powerful type system, offers a feature called Generics,
  which enables developers to write reusable and type-safe code. Generics allow you
  to create components that can work over a variety of types rather than a single
  one.

  This a...'
---

TypeScript, avec son système de types puissant, offre une fonctionnalité appelée Génériques, qui permet aux développeurs d'écrire du code réutilisable et sécurisé en termes de types. Les génériques permettent de créer des composants qui peuvent fonctionner avec une variété de types plutôt qu'avec un seul.

Cet article explore les génériques TypeScript, fournissant des explications approfondies et des exemples de code pour illustrer leur utilisation et leurs avantages.

Vous pouvez obtenir tout le code source à partir d'[ici](https://github.com/dotslashbit/fcc-article-resources/blob/main/ts-generics/index.ts).

## Table des matières

* [Qu'est-ce que les génériques](#heading-quest-ce-que-les-generiques)
* [Cas d'utilisation des génériques TypeScript](https://www.freecodecamp.org/news/how-typescript-generics-work/typescript-generics-use-cases)
* [Conclusion](#heading-conclusion)

## Qu'est-ce que les génériques ?

Les génériques en TypeScript permettent d'écrire du code qui peut fonctionner avec une variété de types de données tout en maintenant la sécurité des types. Ils permettent la création de composants, fonctions et structures de données réutilisables sans sacrifier la vérification des types.

Les génériques sont représentés par des paramètres de type, qui agissent comme des espaces réservés pour les types. Ces paramètres sont spécifiés entre chevrons (`<>`) et peuvent être utilisés dans tout le code pour définir les types de variables, les paramètres de fonction, les types de retour, et plus encore.

## Cas d'utilisation des génériques TypeScript

### Utilisation de base des génériques

Commençons par un exemple simple de fonction générique :

```typescript
function identity<T>(arg: T): T {
    return arg;
}

let output = identity<string>("hello");
console.log(output); // Sortie : hello

```

Dans cet exemple, `identity` est une fonction générique qui prend un paramètre de type `T`. Le paramètre `arg` est de type `T`, et le type de retour de la fonction est également `T`. Lorsque l'on appelle `identity<string>("hello")`, le paramètre de type `T` est déduit comme `string`, assurant la sécurité des types.

### Comment utiliser les classes génériques

Les génériques ne sont pas limités aux fonctions – ils peuvent également être utilisés avec des classes. Considérons l'exemple suivant d'une classe générique `Box` :

```typescript
class Box<T> {
    private value: T;

    constructor(value: T) {
        this.value = value;
    }

    getValue(): T {
        return this.value;
    }
}

let box = new Box<number>(42);
console.log(box.getValue()); // Sortie : 42

```

Ici, `Box` est une classe générique avec un paramètre de type `T`. Le constructeur prend une valeur de type `T`, et la méthode `getValue` retourne une valeur de type `T`. Lorsque l'on crée une instance de `Box<number>`, elle ne peut stocker et retourner que des valeurs de type `number`.

### Comment appliquer des contraintes sur les génériques

Parfois, vous pouvez vouloir restreindre les types qui peuvent être utilisés avec les génériques. TypeScript permet de spécifier des contraintes sur les paramètres de type en utilisant le mot-clé `extends`. Voici un exemple :

```typescript
interface Lengthwise {
    length: number;
}

function loggingIdentity<T extends Lengthwise>(arg: T): T {
    console.log(arg.length);
    return arg;
}

let result = loggingIdentity("hello");
console.log(result); // Sortie : hello

```

Dans cet exemple, la fonction `loggingIdentity` prend un paramètre de type `T` qui doit étendre l'interface `Lengthwise`, ce qui garantit que `arg` a une propriété `length`. Cette contrainte permet d'accéder à la propriété `length` sans causer d'erreur de compilation.

### Comment utiliser les génériques avec les interfaces

Les génériques peuvent également être utilisés avec des interfaces pour créer des définitions flexibles et réutilisables. Considérons l'exemple suivant :

```typescript
interface Pair<T, U> {
    first: T;
    second: U;
}

let pair: Pair<number, string> = { first: 1, second: "two" };
console.log(pair); // Sortie : { first: 1, second: "two" }

```

Ici, `Pair` est une interface avec deux paramètres de type `T` et `U`, représentant les types des propriétés `first` et `second` respectivement. Lorsque l'on déclare `pair` comme `Pair<number, string>`, cela impose que la propriété `first` doit être un nombre, et la propriété `second` doit être une chaîne de caractères.

### Comment utiliser les fonctions génériques avec un tableau

```typescript
function reverse<T>(array: T[]): T[] {
    return array.reverse();
}

let numbers: number[] = [1, 2, 3, 4, 5];
let reversedNumbers: number[] = reverse(numbers);
console.log(reversedNumbers); // Sortie : [5, 4, 3, 2, 1]

```

Dans cet exemple, la fonction `reverse` prend un tableau de type `T` et retourne un tableau inversé du même type. En utilisant les génériques, la fonction peut fonctionner avec des tableaux de n'importe quel type, assurant la sécurité des types.

### Comment utiliser les contraintes génériques avec `keyof`

```typescript
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

let person = { name: "John", age: 30, city: "New York" };
let age: number = getProperty(person, "age");
console.log(age); // Sortie : 30

```

Ici, la fonction `getProperty` prend un objet de type `T` et une clé de type `K`, où `K` étend les clés de `T`. Elle retourne ensuite la valeur de la propriété correspondante de l'objet. Cet exemple démontre comment utiliser les génériques avec `keyof` pour renforcer la sécurité des types lors de l'accès aux propriétés d'un objet.

### Comment utiliser les fonctions utilitaires génériques

```typescript
function toArray<T>(value: T): T[] {
    return [value];
}

let numberArray: number[] = toArray(42);
console.log(numberArray); // Sortie : [42]

let stringArray: string[] = toArray("hello");
console.log(stringArray); // Sortie : ["hello"]

```

La fonction `toArray` convertit une seule valeur de type `T` en un tableau contenant cette valeur. Cette simple fonction utilitaire montre comment les génériques peuvent être utilisés pour créer du code réutilisable qui s'adapte à différents types de données sans effort.

### Comment utiliser les interfaces génériques avec une fonction

```typescript
interface Transformer<T, U> {
    (input: T): U;
}

function uppercase(input: string): string {
    return input.toUpperCase();
}

let transform: Transformer<string, string> = uppercase;
console.log(transform("hello")); // Sortie : HELLO

```

Dans cet exemple, nous définissons une interface `Transformer` avec deux paramètres de type `T` et `U`, représentant respectivement les types d'entrée et de sortie. Nous déclarons ensuite une fonction `uppercase` et l'assignons à une variable `transform` de type `Transformer<string, string>`. Cela démontre comment les génériques peuvent être utilisés pour définir des interfaces flexibles pour les fonctions.

## Conclusion

Que ce soit pour les fonctions, les classes ou les interfaces, les génériques fournissent un mécanisme robuste pour construire des applications TypeScript évolutives et maintenables. Comprendre et maîtriser les génériques peut considérablement améliorer votre capacité à écrire du code efficace et sans erreur.

Si vous avez des commentaires, envoyez-moi un message sur [Twitter](https://twitter.com/introvertedbot) ou [Linkedin](https://www.linkedin.com/in/sahil-mahapatra/).