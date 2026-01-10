---
title: 'Types récursifs en TypeScript : Une brève exploration'
subtitle: ''
author: Eda Eren
co_authors: []
series: null
date: '2025-05-07T15:09:24.581Z'
originalURL: https://freecodecamp.org/news/recursive-types-in-typescript-a-brief-exploration
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1746625684891/6a4e2dae-a7b2-415d-a65d-be47c5d73253.png
tags:
- name: TypeScript
  slug: typescript
seo_title: 'Types récursifs en TypeScript : Une brève exploration'
seo_desc: 'It is said that there are two different worlds in TypeScript that exist
  side by side: the type world and the value world.

  Consider this line of code:

  const firstName: string = ''Maynard'';


  While firstName and ''Maynard'' live in the value world, string ...'
---

[Il est dit](https://www.totaltypescript.com/books/total-typescript-essentials/the-weird-parts#the-type-and-value-worlds) qu'il existe deux mondes différents en TypeScript qui coexistent : le monde des types et le monde des valeurs.

Considérons cette ligne de code :

```typescript
const firstName: string = 'Maynard';
```

Alors que `firstName` et `'Maynard'` vivent dans le monde des valeurs, `string` appartient au monde des types.

Ou, considérons l'opérateur `typeof` qui existe dans les deux mondes.

Le voici dans le monde des valeurs :

```typescript
console.log(typeof 42); // number
```

Et, le voici dans le monde des types, utilisé pour extraire le type de la fonction `increment`, qui est ensuite passé à [un type utilitaire appelé `ReturnType`](https://www.typescriptlang.org/docs/handbook/utility-types.html#returntypetype) :

```typescript
function increment(n: number) {
  return n + 1;
}

type T = ReturnType<typeof increment>; // number
```

L'une des merveilles du monde des types est l'existence de types récursifs – des types qui se réfèrent à eux-mêmes. Ils sont quelque peu similaires aux fonctions récursives que vous connaissez peut-être déjà.

Voici une fonction récursive :

```typescript
function addUpTo(n: number): number {
  if (n === 0) {
    return n;
  }

  return n + addUpTo(n - 1);
}
```

Et, voici un type récursif :

```typescript
type JSONValue =
  | string
  | number
  | boolean
  | null
  | { [key: string]: JSONValue };
```

La fonction `addUpTo` s'appelle elle-même, chaque fois avec une valeur inférieure de `n`, atteignant progressivement le cas de base. (`n` est supposé être un nombre non négatif, sinon, nous aurons l'erreur `Maximum call stack size exceeded`.)

Le type `JSONValue` est un type union qui a une *signature d'index* dans l'un de ses types possibles (`{ [key: string]: JSONValue }`), et la valeur est une référence à lui-même.

Pour le voir avec un exemple, disons que nous avons un objet `person` qui a les propriétés `name`, `age`, et `friends` :

```typescript
const person = {
  name: 'Alice',
  age: 25,
  friends: {
    0: {
      name: 'Bob',
      age: 23,
      friends: {
        // ...
      }
    },
    1: {
      name: 'Carol',
      age: 28,
      friends: {
        // ...
      }
    },
    // ...
  }
};
```

La valeur de `friends` est un objet qui a des nombres comme propriétés, chacun ayant une valeur qui ressemble à la personne que nous venons de définir. Nous pouvons donc créer un type `Person` où la valeur de `friends` est un objet qui a également le type de valeur `Person` :

```typescript
type Person = {
  name: string;
  age: number;
  friends: {
    [key: number]: Person;
  };
};
```

**Note** : En JavaScript, les clés d'objet sont soit des chaînes de caractères, soit des symboles. Même si nous définissons `key` comme un `number`, JavaScript finira par convertir les clés d'objet en chaînes de caractères.

Dans cet article, nous allons non seulement examiner ce que sont les types récursifs en TypeScript, mais nous verrons également comment ils peuvent s'appliquer aux structures de données récursives et comment ils peuvent être utiles avec deux cas d'utilisation différents.

Cela peut être un excellent outil dans votre boîte à outils pour des circonstances très spécifiques, comme lorsque vous devez étendre un type utilitaire ou obtenir le type "interne" d'un tableau multidimensionnel.

Commençons notre exploration.

### Voici ce que nous allons couvrir :

1. [Types récursifs pour les arbres et les listes chaînées](#heading-types-recursifs-pour-les-arbres-et-les-listes-chainees)

2. [Récursion avec les types mappés et conditionnels](#heading-recursion-avec-les-types-mappes-et-conditionnels)

3. [Cas d'utilisation pour les types récursifs](#heading-cas-dutilisation-pour-les-types-recursifs)

   * [Cas d'utilisation 1 : DeepPartial](#heading-cas-dutilisation-1-deeppartial)

   * [Cas d'utilisation 2 : UnwrapArray](#heading-cas-dutilisation-2-unwraparray)

4. [Conclusion (et un avertissement !)](#heading-conclusion-et-un-avertissement)

## Types récursifs pour les arbres et les listes chaînées

Les types récursifs sont probablement mieux compris avec une structure de données comme un arbre :

![Un arbre binaire où le nœud racine a deux enfants, gauche et droit. L'enfant gauche a des enfants gauche et droit, chacun d'eux a également ses propres enfants gauche et droit. L'enfant droit du nœud racine a un enfant gauche qui a son propre enfant gauche, et un enfant droit qui est un nœud feuille.](https://cdn.hashnode.com/res/hashnode/image/upload/v1746454664280/0eed3e38-151e-403f-8d88-028519e23f3e.png align="center")

Par exemple, un nœud d'un arbre binaire a au plus deux enfants, gauche et droit. Un nœud enfant, s'il a également des enfants, est la racine d'un sous-arbre lui-même.

Nous pouvons créer un type `TreeNode` pour un arbre binaire :

```typescript
type TreeNode<T> = {
  value: T;
  left: TreeNode<T> | null;
  right: TreeNode<T> | null;
};
```

C'est un type générique, donc la `value` peut être de n'importe quel type que nous lui passons. Les enfants `left` et `right` peuvent être soit `TreeNode` eux-mêmes, soit `null`.

Disons que nous avons cet arbre binaire :

![Un arbre binaire qui a la valeur 8 comme nœud racine. Il a un enfant gauche avec la valeur 3 et un enfant droit avec la valeur 10. L'enfant gauche a un nœud enfant gauche qui a la valeur 1 et un nœud enfant droit qui a la valeur 6, qui a un nœud enfant gauche avec la valeur 4 et un nœud enfant droit avec la valeur 7. L'enfant droit du nœud racine qui a la valeur 10 a un nœud enfant droit avec la valeur 14, qui a un nœud enfant gauche qui a la valeur 13.](https://cdn.hashnode.com/res/hashnode/image/upload/v1746456573014/d748d7fb-1893-44af-9e37-bffcfaffec5d.png align="right")

Nous pouvons le représenter comme ceci, avec le type `TreeNode` que nous venons de définir :

```typescript
const binaryTree: TreeNode<number> = {
  value: 8,
  left: {
    value: 3,
    left: {
      value: 1,
      left: null,
      right: null
    },
    right: {
      value: 6,
      left: {
        value: 4,
        left: null,
        right: null
      },
      right: {
        value: 7,
        left: null,
        right: null
      }
    }
  },
  right: {
    value: 10,
    left: null,
    right: {
      value: 14,
      left: {
        value: 13,
        left: null,
        right: null
      },
      right: null
    }
  }
};
```

Puisque c'est un type générique, nous lui passons le type `number` qui est utilisé comme type de `value`.

De même, nous pouvons créer un type pour une liste chaînée où chaque nœud a une `value` et une propriété `next` qui pointe soit vers un autre nœud, soit vers `null` :

```typescript
type LinkedList<T> = {
  value: T;
  next: LinkedList<T> | null;
};
```

Donc, si notre liste chaînée ressemble à ceci :

![Une liste chaînée où la tête pointe vers le nœud avec la valeur 1, qui pointe vers le nœud avec la valeur 2, qui pointe vers le nœud avec la valeur 3 qui pointe vers null.](https://cdn.hashnode.com/res/hashnode/image/upload/v1746456962646/9996894c-162a-4c71-b2b3-3c9369592551.jpeg align="center")

Nous pouvons la représenter comme ceci, avec le type `LinkedList` :

```typescript
const linkedList: LinkedList<number> = {
  value: 1,
  next: {
    value: 2,
    next: {
      value: 3,
      next: null
    }
  }
};
```

**Note** : Nous avons utilisé des alias de type dans les exemples ci-dessus, mais nous pouvons également utiliser une `interface` à la place :

```typescript
interface TreeNode<T> {
  value: T;
  left: TreeNode<T> | null;
  right: TreeNode<T> | null;
}

interface LinkedList<T> {
  value: T;
  next: LinkedList<T> | null;
}
```

## Récursion avec les types mappés et conditionnels

Appliquer des types récursifs à des valeurs représentant des structures de données récursives est un peu évident et pas trop excitant, mais nous pouvons explorer d'autres options où la récursion peut également être utilisée, comme les types mappés et conditionnels.

Les types mappés sont un moyen pratique de créer un nouveau type basé sur un autre. Nous pouvons, par exemple, créer un nouveau type en utilisant les clés d'un objet, où nous *mappons* les clés à un type de valeur différent.

Disons que nous avons un objet `colors` qui contient des noms de couleurs et les valeurs hexadécimales correspondantes. Les valeurs sont de type `string`, mais disons que nous voulons créer un type d'objet où les clés sont les mêmes, sauf que le type des valeurs doit être `boolean` :

```typescript
const colors = {
  aquamarine: '#7fffd4',
  black: '#000000',
  blueviolet: '#8a2be2',
  goldenrod: '#daa520',
  indigo: '#4b0082',
  lavender: '#e6e6fa',
  silver: '#c0c0c0'
};

type ColorsToBoolean<T> = {
  [K in keyof T]: boolean;
};

type Result = ColorsToBoolean<typeof colors>;
```

Le type `Result` ressemblera alors à ceci :

![Une capture d'écran du bloc de code défini ci-dessus lorsqu'il est survolé sur le type `Result`. Les clés sont les mêmes que celles de l'objet `colors`, et toutes les valeurs sont `boolean`.](https://cdn.hashnode.com/res/hashnode/image/upload/v1746481133106/390515bd-4f98-4072-a8f8-94a3ef39cec4.png align="center")

Pour créer un type mappé *récursif*, cependant, nous avons besoin d'une référence au même type que nous créons, comme ceci :

```typescript
type Recursive<T> = {
  [K in keyof T]: Recursive<T[K]>;
};
```

Avant d'aller plus loin, examinons également les types conditionnels, qui ressemblent beaucoup aux expressions conditionnelles utilisant [l'opérateur ternaire](https://www.freecodecamp.org/news/javascript-ternary-operator-explained/) :

```typescript
AType extends AnotherType ? ResultTypeIfTrue : ResultTypeIfFalse;
```

Il a cette forme familière :

```plaintext
condition ? resultIfTrue : resultIfFalse
```

Maintenant, nous pouvons combiner les types mappés et conditionnels pour créer un type conditionnel mappé récursif :

```typescript
type Recursive<T> = {
  [K in keyof T]: T[K] extends number ? T[K] : Recursive<T[K]>;
};
```

Nous mappons les clés du type d'objet donné au même type de valeur si c'est un `number`, sinon, nous continuons avec la récursion.

## Cas d'utilisation pour les types récursifs

### Cas d'utilisation 1 : `DeepPartial`

Un cas d'utilisation des types récursifs est l'extension des capacités du type utilitaire `Partial`.

Disons que nous avons un type pour un article, en utilisant une `interface` cette fois :

```typescript
interface IArticle {
  title: string;
  description: string;
  url: string;
  author: {
    name: string;
    age: number;
  };
}
```

`Partial` rend toutes les propriétés d'un type d'objet qui lui est donné optionnelles.

Mais, si nous essayons de faire ceci :

```typescript
const article: Partial<IArticle> = {
  title: 'Naviguer dans les mystères',
  description:
    'Alors que nous marchons avec nos questions vers un avenir troublé, le conteur et mythologue Martin Shaw nous invite à subvertir les voix de certitude d\'aujourd\'hui et à faire le travail difficile de s\'ouvrir au mystère.',
  url: 'https://emergencemagazine.org/essay/navigating-the-mysteries',
  author: {
    name: 'Martin Shaw'
  }
};
```

Nous aurons une erreur : `La propriété 'age' est manquante dans le type '{ name: string; }' mais requise dans le type '{ name: string; age: number; }'`. Toutes les propriétés sont optionnelles comme prévu, sauf pour `age` qui est une propriété de la propriété `author`. Donc, `Partial` ne va pas fonctionner pour les objets avec plus d'un niveau de profondeur.

Dans notre exemple, nous ne voulons pas passer une propriété `age` pour `author`, donc nous devons trouver un moyen de le faire fonctionner.

En fait, le type conditionnel mappé récursif que nous venons de définir ci-dessus est un cas d'utilisation parfait pour cela. Nous pouvons utiliser la récursion pour que toutes les propriétés soient optionnelles, quel que soit leur niveau de profondeur :

```typescript
type DeepPartial<T> = {
  [K in keyof T]?: T[K] extends object ? DeepPartial<T[K]> : T[K];
};
```

Maintenant, si nous essayons notre exemple avec `DeepPartial`, il n'y a pas d'erreurs, et le problème est résolu :

```typescript
const article: DeepPartial<IArticle> = {
  title: 'Naviguer dans les mystères',
  description:
    'Alors que nous marchons avec nos questions vers un avenir troublé, le conteur et mythologue Martin Shaw nous invite à subvertir les voix de certitude d\'aujourd\'hui et à faire le travail difficile de s\'ouvrir au mystère.',
  author: {
    name: 'Martin Shaw'
  }
};
```

### Cas d'utilisation 2 : `UnwrapArray`

Un autre cas d'utilisation que nous pouvons examiner est lorsque nous avons besoin d'obtenir le type "interne" d'un tableau multidimensionnel.

Considérons ceci :

```typescript
type UnwrapArray<A> = A extends Array<infer T> ? UnwrapArray<T> : A;
```

Nous définissons un type générique `UnwrapArray`. Si le type que nous lui passons est un autre tableau (`A extends Array`), alors il est passé à `UnwrapArray` à nouveau jusqu'à ce que nous atteignions un type qui n'étend pas `Array`.

**Note** que nous utilisons le mot-clé `infer` pour extraire le type. `infer` n'est utilisé qu'avec les types conditionnels lorsque `extends` est utilisé, donc c'est parfait pour notre objectif ici.

Maintenant, nous pouvons obtenir le type interne :

```typescript
type Result = UnwrapArray<string[][][]>; // string
```

L'utilisation du mot-clé `Array` donnera le même résultat :

```typescript
type Result = UnwrapArray<Array<Array<Array<string>>>>; // string
```

## Conclusion (et un avertissement !)

L'univers des types récursifs en TypeScript est fascinant et très puissant. Mais, bien sûr, avec un grand pouvoir vient une grande responsabilité. La documentation de TypeScript nous avertit :

> Gardez à l'esprit que bien que ces types récursifs soient puissants, ils doivent être utilisés de manière responsable et parcimonieuse. [(Source)](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-1.html#recursive-conditional-types)

Ce n'est pas seulement que les types récursifs peuvent entraîner un temps plus long pour la vérification des types, mais avec suffisamment de complexité, cela peut également entraîner une erreur de compilation. En fait, la documentation nous dit également de ne pas les utiliser du tout si possible.

Alors, tout cet apprentissage était-il pour rien ?

La réponse dépend de ce que vous en faites. La récursion est un concept puissant qui a définitivement des cas d'utilisation en TypeScript comme nous l'avons vu dans cet article, et si elle est utilisée de manière responsable, elle peut être un excellent outil.