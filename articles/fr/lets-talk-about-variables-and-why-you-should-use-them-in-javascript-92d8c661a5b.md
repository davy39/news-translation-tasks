---
title: Parlons des variables — et pourquoi vous devriez les utiliser en JavaScript.
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2017-11-16T09:00:00.000Z'
originalURL: https://freecodecamp.org/news/lets-talk-about-variables-and-why-you-should-use-them-in-javascript-92d8c661a5b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OrxTL4xEQZ5um_8gxoddbQ.jpeg
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Parlons des variables — et pourquoi vous devriez les utiliser en JavaScript.
seo_desc: 'The main purpose of coding is to solve problems. For example, what happens
  when you click on a button? That’s a problem for us to solve.

  So, let’s begin this article by solving a simple problem.

  Counting apples

  If you have 4 apples and you buy 27 mor...'
---

Le but principal de la programmation est de résoudre des problèmes. Par exemple, que se passe-t-il lorsque vous cliquez sur un bouton ? C'est un problème que nous devons résoudre.

Alors, commençons cet article en résolvant un problème simple.

### Compter les pommes

Si vous avez 4 pommes et que vous en achetez 27 de plus, combien de pommes avez-vous ? Prenez un moment et écrivez votre réponse dans votre éditeur de texte.

Quelle est votre réponse ?

```
// Cela ? 31  
```

```
// Ou cela ? 4 + 27
```

Les deux réponses sont correctes, mais la deuxième méthode est meilleure — parce que vous déléguez le calcul à JavaScript. Vous lui apprenez comment arriver à la réponse.

Mais il y a encore un problème avec le code.

Si vous regardez `4 + 27` sans aucun contexte de notre problème de pommes, savez-vous que nous calculons le nombre de pommes que vous avez actuellement ?

Probablement pas.

Donc, une meilleure façon est d'utiliser l'algèbre pour substituer 4 et 27 par des variables. Lorsque vous le faites, vous obtenez la capacité d'écrire du code qui a du sens :

```
pommesInitiales + pommesAchetees
```

Le processus de substitution de 4 par une variable appelée `pommesInitiales` s'appelle la déclaration de variables.

### Déclarer des variables

Vous déclarez des variables avec la syntaxe suivante :

```
const nomVariable = 'valeur'
```

Il y a quatre parties auxquelles vous devez prêter attention :

1. Le `nomVariable`
2. La `valeur`
3. Le signe `=`
4. Le mot-clé `const`

### Le nomVariable

`nomVariable` est le nom de la variable que vous déclarez. Vous pouvez le nommer comme vous voulez, tant qu'il suit ces règles :

1. Il doit être en un seul mot
2. Il doit être composé uniquement de lettres, de chiffres ou de traits de soulignement (0–9, a-z, A-Z, `_`).
3. Il ne peut pas commencer par un chiffre.
4. Il ne peut pas être l'un de ces [mots-clés réservés](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#Keywords)

Si vous devez utiliser deux mots ou plus pour nommer votre variable, joignez simplement les mots ensemble mais mettez en majuscule la première lettre de chaque mot suivant. Cette capitalisation étrange est appelée **camel case**.

Un bon exemple de variable en camel case est `pommesAAcheter`.

### La valeur

La valeur est ce que vous voulez que la variable soit. Elle peut être des primitives (comme des chaînes de caractères et des nombres) ou des objets (comme des tableaux et des fonctions).

### = en JavaScript

`=` en JavaScript ne fonctionne pas comme `=` en mathématiques. Ne vous y trompez pas.

En JavaScript, `=` signifie **affectation**. Lorsque vous utilisez `=`, vous définissez (ou affectez) la valeur du côté droit (RHS) du signe `=` au côté gauche (LHS) du signe `=`.

Dans l'instruction suivante, vous définissez la variable `pommesInitiales` au nombre 4.

```
const pommesInitiales = 4
```

Si vous utilisez `console.log` sur cette variable, vous pouvez voir que `pommesInitiales` est 4.

```
console.log(pommesInitiales) // 4
```

### Évaluation avant affectation

Chaque variable ne peut prendre qu'une seule valeur. Donc, si vous avez une équation qui doit être évaluée du côté RHS, elle sera évaluée avant d'être affectée à la variable.

```
const pommesInitiales = 4 const pommesAAcheter = 27 const totalPommes = pommesInitiales + pommesAAcheter
```

Dans cet exemple, JavaScript évaluera la réponse de `pommesInitiales` + `pommesAAcheter` (ce qui donne 31) avant d'affecter les résultats à `totalPommes`. C'est pourquoi vous obtenez `31` si vous essayez de logger `totalPommes`.

```
console.log(totalPommes) // 31
```

### Le mot-clé const

`const` est l'un des trois mots-clés que vous pouvez utiliser pour déclarer des variables. Il y a deux autres mots-clés – `let` et `var`.

Les trois mots-clés déclarent des variables, mais ils sont légèrement différents les uns des autres.

### Const vs let vs var

`const` et `let` sont des mots-clés mis à notre disposition dans ES6. Ils sont meilleurs pour créer des variables que `var` parce qu'ils sont [à portée de bloc tandis que var est à portée de fonction](https://zellwk.com/blog/es6/#let-and-const).

Pour l'instant, concentrons-nous sur la différence entre `const` et `let`.

### Const vs let

Si vous déclarez une variable avec `const`, **vous ne pouvez pas la réaffecter** avec une nouvelle valeur. Le code suivant produit une erreur :

```
const pommesAAcheter = 22 
```

```
// Réaffecter à une variable déclarée avec const entraîne une erreur pommesAAcheter = 27
```

![Image](https://cdn-media-1.freecodecamp.org/images/BQnsRFT3Iau5NHn0R9FU4cvuUYHVorRWwppL)

Si vous déclarez une variable avec `let`, **vous pouvez la réaffecter avec une nouvelle valeur.**

```
let pommesAAcheter = 22 pommesAAcheter = 27 console.log(pommesAAcheter)
```

![Image](https://cdn-media-1.freecodecamp.org/images/oZrfI-Rk-6onxPz3o4vfv4cn8OIBfXNd-Xdg)

### Devriez-vous utiliser const ou let ?

Comprendre si vous devriez utiliser `const` ou `let` est un sujet plus avancé.

Lorsque vous commencez, utiliser `let` serait beaucoup plus simple que d'utiliser `const`.

Cependant, à mesure que vous écrivez plus de programmes, vous réaliserez lentement que vous voulez éviter de réaffecter vos variables. Vous commencerez donc à utiliser `const` plutôt que `let`. Mais c'est un sujet différent pour un autre jour.

Puisque vous allez utiliser `const` plutôt que `let` de toute façon lorsque vous écrivez des programmes plus avancés, il est préférable de prendre l'habitude de préférer `const` à `let` lorsque vous commencez.

Au cas où vous vous poseriez la question, n'utilisez plus `var` — il n'y a plus besoin. `let` et `const` sont bien meilleurs que `var`.

### Conclusion

En JavaScript, les variables sont utilisées pour contenir une valeur. Elles peuvent contenir n'importe quelle valeur, des primitives aux objets.

Le signe `=` en JavaScript n'est pas le même que le signe `=` en mathématiques. En JavaScript, `=` signifie affectation.

Lorsque vous déclarez des variables, utilisez le camelCase pour nommer vos variables. Évitez les mots-clés réservés.

Vous pouvez déclarer des variables avec soit `const`, `let` ou `var`. Dans la mesure du possible, vous voudrez utiliser `const` plutôt que `let`. Utilisez `let` lorsque vous devez réaffecter des valeurs. Il n'y a plus besoin d'utiliser `var`.

**Cet article est un exemple de leçon de Learn JavaScript** — un cours qui vous aide à apprendre JavaScript et à construire des composants réels et pratiques à partir de zéro. Si vous avez trouvé cet article utile, je vous invite à [en savoir plus sur Learn JavaScript](https://learnjavascript.today/).

(Oh, au fait, si vous avez aimé cet article, j'apprécierais que vous puissiez [le partager](http://twitter.com/share?text=Use%20const%20over%20let%20when%20declaring%20variables.%20No%20need%20to%20use%20var%20anymore%20?%20&url=https://zellwk.com/blog/javascript-variables/&hashtags=). ?)

*Originalement publié sur [zellwk.com](https://zellwk.com/blog/javascript-variables/).