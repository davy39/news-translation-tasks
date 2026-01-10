---
title: Les Génériques TypeScript – Cas d'Utilisation et Exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-07T20:49:10.000Z'
originalURL: https://freecodecamp.org/news/typescript-generics-use-case-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-hitarth-jadhav-220357.jpg
tags:
- name: generics
  slug: generics
- name: TypeScript
  slug: typescript
seo_title: Les Génériques TypeScript – Cas d'Utilisation et Exemples
seo_desc: 'By Aman Kalra

  In this tutorial, you''ll learn the basics of generics in TypeScript. We''ll discuss
  how to use them and when they''re useful in your code.

  Use Case for Generics

  Let''s start with a simple example, where you want to print the value of an ar...'
---

Par Aman Kalra

Dans ce tutoriel, vous apprendrez les bases des génériques en TypeScript. Nous verrons comment les utiliser et quand ils sont utiles dans votre code.

## Cas d'Utilisation des Génériques

Commençons par un exemple simple, où vous souhaitez afficher la valeur d'un argument passé :

```typescript
function printData(data: number) {
    console.log("data: ", data);
}

printData(2);
```

Supposons maintenant que vous souhaitiez faire de `printData` une fonction plus générique, à laquelle vous pouvez passer n'importe quel type d'argument tel que : **number**/ **string**/ **boolean**. Vous pourriez donc penser à suivre une approche comme celle ci-dessous :

```typescript
function printData(data: number | string | boolean) {
    console.log("data: ", data);
}

printData(2);
printData("hello");
printData(true);
```

Mais à l'avenir, vous pourriez vouloir afficher un tableau de nombres en utilisant la même fonction. Dans ce cas, les types augmenteront et il deviendra fastidieux de maintenir tous ces types différents.

C'est là que les **Génériques** entrent en jeu.

## Comment Fonctionnent les Génériques en TS

Les génériques sont comme des variables – pour être précis, des variables de type – qui stockent le type (par exemple number, string, boolean) en tant que valeur.

Vous pouvez donc résoudre le problème dont nous avons discuté ci-dessus avec les génériques comme indiqué ci-dessous :

```typescript
function printData<T>(data: T) {
    console.log("data: ", data);
}

printData(2);
printData("hello");
printData(true);
```

Dans l'exemple ci-dessus `printData-generics.ts`, il y a une légère différence de syntaxe :

1. Vous utilisez une variable de type à l'intérieur de chevrons après le nom de la fonction `<T>`
2. Vous assignez ensuite la variable de type au paramètre `data: T`

Explorons ces différences un peu plus en détail.

Pour utiliser les génériques, vous devez utiliser des chevrons, puis spécifier une variable de type à l'intérieur. Les développeurs utilisent généralement `T`, `X` et `Y`. Mais cela peut être n'importe quoi selon votre préférence.

Vous pouvez ensuite assigner le même nom de variable que le type au paramètre de la fonction.

Désormais, quel que soit l'argument que vous passez à la fonction, il est inféré et il n'est pas nécessaire de coder en dur le type n'importe où.

Même si vous passez un tableau de nombres ou un objet à la fonction `printData`, tout s'affichera correctement sans que TS ne se plaigne :

```typescript
function printData<T>(data: T) {
    console.log("data: ", data);
}

printData(2);
printData("hello");
printData(true);
printData([1, 2, 3, 4, 5, 6]);
printData([1, 2, 3, "hi"]);
printData({ name: "Ram", rollNo: 1 });
```

Voyons un autre exemple :

```typescript
function printData<X,Y>(data1: X, data2: Y) {
    console.log("Output is: ", data1, data2);
}

printData("Hello", "World");
printData(123, ["Hi", 123]);
```

Dans l'exemple ci-dessus, nous avons passé 2 arguments à `printData` et utilisé `X` et `Y` pour désigner les types des deux paramètres. `X` fait référence à la 1ère valeur de l'argument et `Y` fait référence à la 2ème valeur de l'argument.

Ici aussi, les types de `data1` et `data2` ne sont pas spécifiés explicitement car TypeScript gère l'inférence de type à l'aide des génériques.

### Comment Utiliser les Génériques avec les Interfaces

Vous pouvez même utiliser des génériques avec des interfaces. Voyons comment cela fonctionne à l'aide d'un extrait de code :

```typescript
interface UserData<X,Y> {
    name: X;
    rollNo: Y;
}

const user: UserData<string, number> = {
    name: "Ram",
    rollNo: 1
}
```

Dans l'extrait ci-dessus, `<string, number>` sont passés à l'interface `UserData`. De cette façon, `UserData` devient une interface réutilisable dans laquelle n'importe quel type de données peut être assigné en fonction du cas d'utilisation.

Ici, dans cet exemple, `name` et `rollNo` seront toujours respectivement `string` et `number`. Mais cet exemple visait à montrer comment vous pouvez utiliser les génériques avec des interfaces en TS.

### Merci de m'avoir lu !

Si vous avez trouvé cet article utile, n'hésitez pas à le partager avec vos amis et collègues.