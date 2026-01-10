---
title: Qu'est-ce que l'effacement de type en TypeScript ?
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2021-12-06T19:21:41.000Z'
originalURL: https://freecodecamp.org/news/what-is-type-erasure-in-typescript
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/TypeErasure--1-.png
tags:
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: Qu'est-ce que l'effacement de type en TypeScript ?
seo_desc: 'TypeScript is a transpiled language, and there is a step in the process
  called type erasure.

  So what exactly is transpiling, and what is type erasure?

  Higher Level vs Lower Level Programming Languages

  Before we explain further, we have to understand ...'
---

TypeScript est un langage **transpilé**, et il y a une étape dans le processus appelée **effacement de type**.

Alors, qu'est-ce que la **transpilation**, et qu'est-ce que l'**effacement de type** ?

# Langages de programmation de haut niveau vs de bas niveau

Avant d'expliquer davantage, nous devons comprendre les langages de haut et de bas niveau.

Les langages de haut niveau sont plus abstraits que les langages de bas niveau. Par abstraits, je veux dire qu'ils sont plus faciles à comprendre pour les humains.

Par exemple, vous diriez que le code machine (binaire) est de bas niveau et plus proche de l'ordinateur que JavaScript. Les langages de haut niveau sont généralement plus simples à écrire et à comprendre que les langages de bas niveau (comme l'Assembleur, par exemple), où vous devez comprendre et gérer directement les adresses mémoire, etc.

La **compilation** et la **transpilation** sont des étapes très similaires, mais elles ne sont pas identiques. Je vais expliquer les deux afin que vous connaissiez la différence.

## Qu'est-ce que la compilation ?

La compilation est un terme général pour transformer le code que vous avez écrit en un exécutable de bas niveau pour l'ordinateur (généralement du code machine).

Des exemples de langages compilés sont Java, C# ou C. Parfois, la compilation se fait en plusieurs étapes, chaque étape optimisant le code et le rapprochant du code machine à chaque "passe".

À travers ce processus, un langage de haut niveau, plus proche du langage humain, finit par être "plus bas" ou plus proche du binaire.

## Qu'est-ce que la transpilation ?

Les transpileurs sont parfois appelés "compilateurs source à source" – une façon abrégée de dire "code source à code source". La transpilation signifie convertir un langage de haut niveau en un autre langage de haut niveau.

Par exemple, TypeScript est un langage de haut niveau, mais après sa transpilation, il est transformé en JavaScript (un autre langage de haut niveau). Ou Babel, par exemple, peut transpiler du code JavaScript ES6 en JavaScript ES5.

Les avantages de la transpilation sont que vous pouvez écrire un langage de haut niveau et toujours obtenir un autre langage de haut niveau.

# Effacement de type en TypeScript

Une partie de ce processus de **transpilation** est appelée **effacement de type**.

L'**effacement de type** est tout simplement lorsque tous les types sont supprimés du code TypeScript lors de sa transpilation en JavaScript.

Les types que vous utilisez en TypeScript ne peuvent pas être inspectés à l'exécution, lorsque JavaScript est exécuté. Les **types** ne sont accessibles que pendant l'étape de compilation/transpilation.

Le code TypeScript qui ressemble à ceci :

`let name: string = 'Kealan';`

Est finalement compilé/transpilé en ceci :

`let name = 'Kealan'`

La sortie peut varier en fonction de vos étapes de construction spécifiques (la variable peut être renommée ou intégrée), mais l'exemple d'**effacement de type** reste valable.

Ce n'est pas seulement avec les types primitifs comme `number` ou `string` – mais même avec vos propres types personnalisés que vous pouvez créer :

```
type StringType = string;

const firstName: StringType = "Kealan";
```

## Effacement de type en pratique

Plus que de comprendre conceptuellement ce qu'est l'**effacement de type**, ce concept explique une étape importante dans le processus de transpilation où les types sont supprimés et ne sont pas utilisés dans le code source que vous générez.

Cela signifie également que des parties de votre code ne sont même pas "utilisées" en JavaScript lors de l'étape de transpilation – et le code est simplement complètement supprimé. Ainsi, votre interface de 100 lignes que vous créez est simplement supprimée, et le code envoyé à l'utilisateur est plus petit.

Vous pouvez voir un exemple de cela dans le [TypeScript playground](https://www.typescriptlang.org/play?#code/JYOwLgpgTgZghgYwgAgApQPYHMpwLZ7TIDeAUMhciPhAFzIDOYUoWANOZQDbADWEDekxYh2nCpAQALEF2wBPAKoMIAEyHNWAbQC6pAL6lSCDCCbJLnBD102XASIBeEuKo16AcgDSEKzZeHJTIPPyCyF4AwlICDEHukjJyWEoq6shaXgBScABucADKCCwADmBBkQAq8qUQxWUVbJEASv4ITZEAchiqEF46yAZAA), où une interface utilisée dans le code TypeScript est absente dans le JavaScript transpilé.

# Conclusion

J'espère que certaines des étapes que TypeScript prend pour transformer votre code en JavaScript sont un peu plus claires, et que vous avez une bonne vue d'ensemble des différences entre la **compilation** et la **transpilation**.

Je tweete mes articles [ici](https://twitter.com/kealanparr) si vous souhaitez en lire davantage.