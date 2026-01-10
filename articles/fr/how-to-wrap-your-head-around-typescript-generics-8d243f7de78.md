---
title: Comment comprendre les génériques de TypeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-14T17:12:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-wrap-your-head-around-typescript-generics-8d243f7de78
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gKVGuI3cUiJ043SjQn81hw.png
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: Comment comprendre les génériques de TypeScript
seo_desc: 'By Nadeesha Cabral

  Sometime back when the “Flow vs. Typescript” debate was raging, I had to pick a
  side. And I picked Typescript. Fortunately, that was one of the better decisions
  I made. When I had to make that decision, ultimately what convinced me...'
---

Par Nadeesha Cabral

Il y a quelque temps, lorsque le débat "Flow vs. TypeScript" faisait rage, j'ai dû choisir un camp. Et j'ai choisi TypeScript. Heureusement, c'était l'une des meilleures décisions que j'ai prises. Lorsque j'ai dû prendre cette décision, ce qui m'a finalement convaincu, c'était [le support de TypeScript pour les génériques au moment de l'appel](https://medium.com/@nadeesha/why-i-choose-typescript-specifying-generic-parameters-during-call-time-706003f55675).

Aujourd'hui, laissez-moi essayer de vous expliquer ce que les génériques accomplissent et comment ils nous aident à écrire un code plus sûr, plus propre et plus maintenable.

### Exemple #1 : Assertion d'un type simple

Supposons que nous avons besoin d'une fonction qui prend n'importe quelle valeur et la place dans un objet. Une implémentation naïve de cela en TypeScript ressemblerait à ceci et s'exécuterait comme suit :

```typescript
function wrapInObject(myValue) {
  return { myValue };
}

const wrapped = wrapInObject(2);
```

Beaucoup pour la sécurité des types.

Il est vrai que `myValue` peut être de n'importe quel type. Mais ce que nous devons dire au contrôleur, c'est que la sortie de la fonction, bien qu'elle ne puisse pas être prévue par le développeur écrivant le code, peut être "déduite" par le type du type d'entrée. En d'autres termes, nous pouvons avoir une "définition générique" de ce qu'est la sortie.

L'implémentation générique de la fonction ci-dessus serait quelque chose comme ceci :

```typescript
function wrapInObject<T>(myValue: T) {
  return { myValue };
}

const wrapped = wrapInObject(2);
```

Ce que nous disons simplement, c'est que `myValue` peut avoir un type de `T`. Il peut être "n'importe quel type" mais pas `any` type. En d'autres termes, il a un type qui nous intéresse.

Si vous essayez d'écrire l'exécution précédente en TypeScript, vous ne pourrez pas l'exécuter, car le compilateur donne un avertissement utile :

![Image](https://cdn-media-1.freecodecamp.org/images/1*1uIU75xsSfWbGWVOmOUsKg.png)

### Exemple #2 : Écrire idx avec des génériques

`idx` est une "Bibliothèque pour accéder à des propriétés arbitrairement imbriquées, potentiellement nulles, sur un objet JavaScript". Elle est particulièrement utile lorsque vous travaillez avec des objets JavaScript complexes comme les réponses d'API REST qui peuvent avoir des champs nuls.

Si vous ne me dérangez pas de simplifier un peu cela, elle accomplit cela en "essayant" essentiellement la fonction donnée comme deuxième paramètre avec `props`. Si cela échoue, elle "attrape" et retourne une valeur `undefined` en toute sécurité, sans lever d'erreur.

Encore une fois, une implémentation naïve de cela serait :

```typescript
function idx(props, selector) {
  try {
    return selector(props);
  } catch (e) {
    return undefined;
  }
}
```

Mais, si nous sommes un peu malins avec les génériques, nous pouvons faire en sorte que TypeScript nous aide avec cela.

Nous avons introduit deux génériques ici.

`T` pour le type d'entrée, et nous "suggérons" que c'est un objet en disant `T extends {}`. `U` est pour le type de sortie. Et avec ceux-ci, nous pouvons exprimer que la fonction `selector` est quelque chose qui prend `T` et retourne `U` ou undefined.

Maintenant, si vous essayez d'écrire le même code qu'avant avec cette définition de `idx`, vous obtiendrez une erreur de compilation :

![Image](https://cdn-media-1.freecodecamp.org/images/1*pdasjNVJPY2ClKdENWBw6A.png)

### Exemple #3 : Utiliser l'inférence de type et les génériques pour obtenir le type de retour d'une fonction

Supposons que j'ai une fonction, et que je dois fournir au consommateur le type de sortie. Si j'appelle ce type `FooOutput`, j'écrirai quelque chose comme :

```typescript
type FooOutput = number;

function foo(): FooOutput {
  return 1;
}
```

Mais en utilisant les génériques et l'inférence de type, je peux écrire un type générique `ReturnType`, qui peut "déduire" le type de retour d'une fonction :

```typescript
type ReturnType<T extends (...args: any[]) => any> = T extends (
  ...args: any[]
) => infer R
  ? R
  : any;
```

Nous jouons avec un `T extends (...args: any[]) => any` ici. Cela signifie simplement que T est un type de fonction générique qui prend n'importe quel nombre d'arguments et produit une valeur. Ensuite, nous l'utilisons pour "déduire" un autre type R, et le retourner.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gKVGuI3cUiJ043SjQn81hw.png)

En utilisant cela, j'évite le besoin d'écrire mon type de retour dans l'exemple ci-dessus manuellement. Puisque `foo` est une fonction et que j'ai besoin du type de cette fonction pour utiliser `ReturnType`, je dois obtenir le type de `foo` en utilisant `typeof`.

### Utilitaires utiles dans ma boîte à outils ?

J'utilise un tas de ces utilitaires dans la programmation quotidienne. La plupart des génériques utilitaires sont définis dans le fichier `lib.es5.d.ts` de TypeScript [ici](https://github.com/Microsoft/TypeScript/blob/master/lib/lib.es5.d.ts#L1411). Certains de ceux que j'utilise le plus incluent :

- `Partial<T>` : Rendre toutes les propriétés de T optionnelles.
- `Record<K, T>` : Créer un type avec des propriétés de type K et des valeurs de type T.
- `Pick<T, K>` : Créer un type en choisissant un ensemble de propriétés de T.
- `Exclude<T, U>` : Exclure les types de T qui sont assignables à U.
- `ReturnType<T>` : Obtenir le type de retour d'une fonction.

Espérons que cela vous aide à mieux comprendre les génériques de TypeScript. Si vous avez des questions, n'hésitez pas à laisser une question ci-dessous.