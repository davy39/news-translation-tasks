---
title: Types Littéraux et Collectifs en TypeScript
subtitle: ''
author: Kealan Parr
co_authors: []
series: null
date: '2021-12-07T15:55:33.000Z'
originalURL: https://freecodecamp.org/news/typescript-literal-and-collective-types
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/Literal-Types-vs-Collective-Types--1-.png
tags:
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: Types Littéraux et Collectifs en TypeScript
seo_desc: 'TypeScript offers us a level of "safety" in our code by adding static types.

  We can guarantee that certain properties or functions are present in our code by
  making them conform to types.

  This can hugely reduce the amount of client-side errors you mi...'
---

TypeScript nous offre un niveau de "sécurité" dans notre code en ajoutant des types statiques.

Nous pouvons garantir que certaines propriétés ou fonctions sont présentes dans notre code en les faisant conformes à des types.

Cela peut considérablement réduire le nombre d'erreurs côté client que vous pourriez avoir sur votre site web, car cela réduit les bugs dus à l'erreur humaine comme l'appel de fonctions sur les mauvais objets, par exemple.

TypeScript fait cela en utilisant les **Types Collectifs** et les **Types Littéraux**.

Alors, quelle est la différence ?

# Types Collectifs en TypeScript

Les **Types Collectifs** sont un concept familier pour la plupart des développeurs qui travaillent avec TypeScript. Par exemple :

`const addOne = (numb: number) => num + 1;` 

Ce code utilise des **Types Collectifs**.

Les **Types Collectifs** sont des types comme `number`, `string`, `boolean` ou `number[]`.

Ces types englobent un grand nombre de variables présentes – le type `number`, par exemple, peut couvrir : 1, 2, 3, 4, 5... et ainsi de suite.

Mais TypeScript nous offre également des sous-types de ces **Types Collectifs** qui sont plus stricts.

# Types Littéraux en TypeScript

Vous pouvez également utiliser des _valeurs_ comme types, donc `let eleven: 11 = 11` est un code TypeScript parfaitement valide.

Quand j'ai vu cela pour la première fois, j'ai trouvé que cela avait l'air un peu bizarre.

Mais cela est largement utilisé et peut vraiment rendre votre code plus lisible.

Vous pouvez commencer à construire des types similaires aux énumérations et strictement n'autoriser que certaines valeurs à être assignées, par exemple :

`type Door = 'open' | 'closed' | 'ajar'`

Le type `Door` peut maintenant être utilisé dans tout votre code – avec un ensemble de valeurs plus strict que celui que le type `string` aurait permis.

Si le `|` dans le code ci-dessus n'est pas clair, il s'agit d'un [Union Type](https://www.typescriptlang.org/docs/handbook/unions-and-intersections.html) – et signifie essentiellement `OU`. Tout type qui se conforme à `Door` ne peut être que `open` OU `closed` OU `ajar`.

# Conclusion

Les **Types Littéraux** sont des sous-types des **Types Collectifs**. 

Nous pouvons dire que tous les Types Littéraux sont des Types Collectifs – mais que tous les Types Collectifs ne sont pas des Types Littéraux. Pour être plus clair, nous pourrions dire que le **Type Littéral** `11` est un `number`, mais que tous les types `number` ne sont pas `11`.

J'espère que la différence entre les deux types est plus claire maintenant, et si vous avez besoin de restreindre strictement les types, vous pouvez utiliser les **Types Littéraux**.

Je tweete mes articles [ici](https://twitter.com/kealanparr) si vous souhaitez en lire plus.