---
title: Que sont les prédicats de type dans TypeScript ? Explication avec des exemples
  de code
subtitle: ''
author: Ashutosh Biswas
co_authors: []
series: null
date: '2024-09-10T15:43:50.541Z'
originalURL: https://freecodecamp.org/news/what-are-type-predicates-in-typescript
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725630140316/a95bd310-5465-4d0c-85fe-e42b91c2452e.jpeg
tags:
- name: TypeScript
  slug: typescript
seo_title: Que sont les prédicats de type dans TypeScript ? Explication avec des exemples
  de code
seo_desc: Type predicates are an interesting syntactical feature in TypeScript. While
  they appear in the same place as return type annotations, they look more like short
  affirmative sentences than typical annotations. This gives you greater control over
  type c...
---

Les prédicats de type (type predicates) sont une fonctionnalité syntaxique intéressante de TypeScript. Bien qu'ils apparaissent au même endroit que les annotations de type de retour, ils ressemblent davantage à de courtes phrases affirmatives qu'à des annotations typiques. Cela vous donne un meilleur contrôle sur la vérification des types.

Depuis la sortie de TypeScript 5.5, travailler avec les prédicats de type est devenu plus intuitif car ils peuvent désormais être inférés automatiquement dans de nombreux cas. Mais si vous parcourez des bases de code légèrement plus anciennes, vous rencontrerez probablement plus souvent des prédicats de type écrits à la main.

Dans cet article, nous allons explorer brièvement ce que sont les prédicats de type et pourquoi ils sont utiles. Commençons par examiner le problème qu'ils résolvent.

## Le problème

La meilleure façon de comprendre l'utilité des prédicats de type, je pense, est de remarquer les problèmes qui surviennent lorsque nous ne les avons pas :

```ts
function isString(value: unknown): boolean {
  return typeof value === "string";
}

function padLeft(padding: number | string, input: string) {
  if (isString(padding)) {
    return padding + input;
        //   ^
        // string | number
  }
  return " ".repeat(padding) + input; // Oups, erreur de type ici
                 //   ^
                 // string | number
}
```

Ici, le type de retour de `isString` est défini sur `boolean`, et nous l'utilisons dans une fonction appelée `padLeft` pour ajouter un espacement à gauche d'une chaîne de caractères d'entrée. Le `padding` peut être soit une chaîne donnée, soit un nombre spécifié de caractères d'espace.

Vous vous demandez peut-être pourquoi j'ai codé en dur le type de retour à `boolean`. C'est pour illustrer le problème. Si vous n'ajoutez aucune annotation de type de retour et que vous utilisez la dernière version de TypeScript, vous ne remarquerez aucun problème ici. Pour l'instant, soyez patient – nous discuterons des différences liées à la version sous peu.

La fonction fonctionnera parfaitement à l'exécution, mais TypeScript ne peut effectuer aucun affinement de type (type narrowing) avec `isString`. Par conséquent, le type de `padding` reste `string | number` à la fois à l'intérieur et à l'extérieur de l'instruction `if`. Cela conduit à un conflit avec l'attente de `repeat` pour son premier argument, provoquant l'erreur de type.

## La solution : les prédicats de type

Même si vous n'êtes pas familier avec le terme prédicat, vous les avez probablement déjà utilisés. En programmation, les prédicats sont simplement des fonctions qui renvoient un booléen pour répondre à une question par oui/non. Plusieurs méthodes de tableau intégrées à JavaScript, telles que `filter`, `find`, `every` et `some`, utilisent des prédicats pour faciliter la prise de décision.

Les prédicats de type sont un moyen de rendre les prédicats plus utiles pour l'affinement de type. Nous pouvons résoudre le problème en utilisant un prédicat de type comme type de retour :

```ts
function isString(value: unknown): value is string {
  return typeof value === "string";
}
```

Ici, le prédicat de type est `value is string`. Il exprime trois choses :

* La fonction est un prédicat. Ainsi, TypeScript affichera une erreur si vous essayez de renvoyer autre chose qu'une valeur booléenne.
    
* Si elle renvoie `true`, alors `value` est de type string.
    
* Si elle renvoie `false`, alors `value` n'est pas de type string.
    

Les prédicats de type vous permettent de créer des protections de type (type guards) définies par l'utilisateur. Les protections de type sont des vérifications logiques qui vous permettent d'affiner les types vers des types plus spécifiques. Ainsi, la fonction ci-dessus est également un type guard défini par l'utilisateur.

Voici le code complet :

```ts
function isString(value: unknown): value is string {
  return typeof value === "string";
}

function padLeft(padding: number | string, input: string) {
  if (isString(padding)) {
    return padding + input;
        //   ^
        // string
  }
  return " ".repeat(padding) + input;
                 //   ^
                 // number
}
```

Ici, TypeScript affine correctement le type de `padding` à l'intérieur et à l'extérieur de l'instruction `if`.

Voyons maintenant brièvement comment les prédicats de type fonctionnaient avant TypeScript 5.5 et ce que cette version a amélioré.

## Les prédicats de type avant TypeScript 5.5

Dans notre exemple précédent, si nous ne spécifions aucun type de retour, il sera inféré comme `boolean` :

```ts
function isString(value: unknown) {
  return typeof value === "string";
}

function padLeft(padding: number | string, input: string) {
  if (isString(padding)) {
    return padding + input;
        //   ^
        // string | number
  }
  return " ".repeat(padding) + input; // Oups, erreur de type ici
                 //   ^
                 // string | number
}
```

Par conséquent, nous avons la même erreur que lorsque nous avons écrit manuellement le type de retour `boolean`. [Voici le lien vers le playground TypeScript](https://www.typescriptlang.org/play/?ts=5.4.5#code/GYVwdgxgLglg9mABDAzgZSgJxmA5gCgDcBDAGxAFMAuRcAazDgHcwBKRAbwFgAoRRTBSghMSKAE8ADhTjBEJchUQBeVYgBEKLDlzqA3LwC+vXqEiwEiScQAmAGQrAo+azZs6aYEAFsARhUxEAB9ELWw8ABpkMEkQKBownXZuPmQ5fFQMcIJXdzxWZN5+fkFhUStbPNxEAGpo2KgDVONU0pEkdQ0AOkFpYmdcpNr6uKbDIA) pour le fragment de code ci-dessus. Allez-y et survolez les fonctions ou les variables pour mieux visualiser les types. Voyez ensuite comment l'écriture du prédicat de type résout le problème.

Si nous ne spécifions pas le prédicat de type, l'utilisation de méthodes comme `filter` peut également entraîner une détection de type incorrecte :

```ts
function isString(value: unknown) {
  return typeof value === "string";
}

const numsOrStrings = [1, 'hello', 2, 'world'];
//      ^
//    strings: (string | number)[]

const strings = numsOrStrings.filter(isString);
//      ^
//    strings: (string | number)[]
```

Voyons maintenant comment TypeScript 5.5 améliore la situation.

## Les prédicats de type après TypeScript 5.5

L'une des fonctionnalités phares de TypeScript 5.5 est sa capacité à inférer les prédicats de type en analysant le corps de la fonction. Donc, si vous utilisez TypeScript 5.5 ou une version ultérieure, vous n'avez pas besoin d'écrire le prédicat de type comme type de retour de `isString`. TypeScript le fait pour vous, et un code comme celui que vous voyez dans l'exemple ci-dessous fonctionne parfaitement :

```ts
function isString(value: unknown) {
  return typeof value === "string";
}

function padLeft(padding: number | string, input: string) {
  if (isString(padding)) {
    return padding + input;
        //   ^
        // string
  }
  return " ".repeat(padding) + input; // Oups, erreur de type ici
                 //   ^
                 // number
}

const numsOrStrings = [1, 'hello', 2, 'world'];

const strings = numsOrStrings.filter(isString);
//      ^
//    strings : string[]

const numbers = numsOrStrings.filter((v) => !isString(v));
//      ^
//    numbers : number[]
```

Je n'ai pas encore trouvé de situation où je suis mécontent de l'inférence automatique des prédicats de type. Si vous en trouvez une, vous pouvez toujours écrire le vôtre manuellement.

## Études complémentaires

Dans cet article, nous avons brièvement exploré les prédicats de type dans TypeScript. Si vous souhaitez en savoir plus et comprendre les cas particuliers, voici les guides officiels :

* [Quoi de neuf → TypeScript 5.5 → Inferred Type Predicates](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-5.html#inferred-type-predicates)
    
* [Manuel → Narrowing → Using type predicates](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#using-type-predicates)
    

Merci de votre lecture ! À la prochaine !

L'image de couverture provient de [Mona Eendra](https://unsplash.com/@monaeendra?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) sur [Unsplash](https://unsplash.com/photos/flowers-beside-yellow-wall-vC8wj_Kphak?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)