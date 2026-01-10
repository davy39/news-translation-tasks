---
title: ES6 Tagged Template Literals
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-18T16:35:00.000Z'
originalURL: https://freecodecamp.org/news/es6-tagged-template-literals-48a70ef3ed4d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZG68vCYoeNM8ID1pC3-f-A.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: ES6 Tagged Template Literals
seo_desc: 'By Sanket Meghani

  You may already be familiar with ES6 template literals, which allows string interpolation
  like this:

  const name = ''Steve'';const message = `Hello ${name}!`;

  console.log(message); // Output -> Hello Steve!

  ES6 also introduced a more a...'
---

Par Sanket Meghani

Vous êtes peut-être déjà familiarisé avec les littéraux de gabarit ES6, qui permettent l'interpolation de chaînes comme ceci :

```
const name = 'Steve';const message = `Bonjour ${name}!`;
```

```
console.log(message); // Sortie -> Bonjour Steve!
```

ES6 a également introduit un concept plus avancé et puissant de Tagged Template Literals. Une balise est une fonction qui a la capacité d'interpréter et de traiter le gabarit. Cela signifie que nous pouvons exécuter la chaîne de gabarit à travers une fonction et avoir plus de contrôle sur la manière dont le gabarit est converti en représentation de chaîne.

Les balises sont simplement des fonctions normales, mais pour être utiles, elles doivent être invoquées différemment. L'exemple suivant montre comment une balise est définie et invoquée :

La balise doit être invoquée en passant un littéral de gabarit sans utiliser de crochets comme montré à la ligne 9 ci-dessus.

Le littéral de gabarit est passé à la fonction de balise sous forme de plusieurs paramètres. Le premier argument est un tableau de chaînes contenant les littéraux de chaîne du gabarit : le premier élément du tableau est la chaîne commençant à l'index 0 jusqu'à la première valeur interpolée, le deuxième élément du tableau est la chaîne après la première valeur interpolée jusqu'à l'interpolation suivante et ainsi de suite jusqu'à la fin du gabarit.

Toutes les **expressions** interpolées sont évaluées et passées à la balise en tant que deuxième argument et suivants dans l'ordre de leur occurrence. La balise peut traiter les littéraux et les expressions évaluées pour former la valeur de retour.

### Qu'est-ce qui le rend puissant ?

La question évidente est : comment cela est-il plus puissant que les littéraux de gabarit normaux ?

Toutes les **expressions** interpolées sont évaluées et passées à la balise en tant que deuxième argument et suivants...

Cela nous permet d'utiliser des expressions de fonction comme valeurs interpolées qui peuvent être rappelées. Prenons un exemple pour clarifier davantage.

Lorsque l'interpolation contient une expression de fonction, elle est évaluée comme une chaîne normale dans le cas des littéraux de gabarit normaux.

Par exemple, `${() => myFunction`()} est évalué comme une chaîne () => myFunc`tion().

Alors que la même expression est évaluée comme une fonction dans le cas des littéraux de gabarit balisés et la balise peut appeler cette fonction. Comme montré dans l'exemple, lors de l'invocation de `myTag`, l'expression `{() => myFunction`()} est évaluée et passée comme fonction `in f`unc parameter que notre balise a invoquée en utilisant `fun`c() à la ligne 9.

### Conclusion

La capacité de la balise à utiliser des expressions de fonction comme interpolation — ainsi que sa capacité à interpréter un gabarit en utilisant toute logique souhaitée — la rend très puissante. Elle peut être utilisée pour créer un langage spécifique à un domaine et ouvre de nombreuses possibilités pour l'utilisation (ou l'abus) des littéraux de gabarit balisés.

Les littéraux de gabarit balisés permettent le développement de bibliothèques comme [styled-components](https://github.com/styled-components/styled-components). Veuillez commenter ci-dessous si vous pouvez penser à d'autres cas d'utilisation qui pourraient être activés par les littéraux de gabarit balisés.