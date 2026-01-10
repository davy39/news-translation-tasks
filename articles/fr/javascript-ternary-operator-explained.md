---
title: Comment utiliser l'opérateur ternaire en JavaScript – Expliqué avec des exemples
subtitle: ''
author: Franklin Okolie
co_authors: []
series: null
date: '2024-02-27T13:04:50.000Z'
originalURL: https://freecodecamp.org/news/javascript-ternary-operator-explained
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/ternary-operator-1.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser l'opérateur ternaire en JavaScript – Expliqué avec des
  exemples
seo_desc: 'Tired of bulky if-else statements? JavaScript''s ternary operator offers
  a powerful solution. This handy tool lets you condense complex conditional logic
  into a single line, making your code cleaner, more elegant, and efficient.

  In this article, we''ll...'
---

Fatigué des instructions if-else encombrantes ? L'opérateur ternaire de JavaScript offre une solution puissante. Cet outil pratique vous permet de condenser une logique conditionnelle complexe en une seule ligne, rendant votre code plus propre, plus élégant et plus efficace.

Dans cet article, nous allons plonger en profondeur dans l'opérateur ternaire, comprendre sa syntaxe et présenter des exemples concrets pour vous aider à comprendre son fonctionnement et à exploiter tout son potentiel.

## Voici ce que nous allons couvrir :

1. [Qu'est-ce qu'un opérateur ternaire ?](#heading-quest-ce-quun-operateur-ternaire)
2. [Comment utiliser l'opérateur ternaire](#heading-comment-utiliser-loperateur-ternaire)
3. [Comment refactoriser les instructions if-else en opérateur ternaire](#heading-comment-refactoriser-les-instructions-if-else-en-operateur-ternaire)
4. [Comment enchaîner les opérateurs ternaires](#heading-comment-enchainer-les-operateurs-ternaires)
5. [Bonnes pratiques lors de l'utilisation de l'opérateur ternaire](#heading-bonnes-pratiques-lors-de-lutilisation-de-loperateur-ternaire)
6. [Conclusion](#heading-conclusion)

## Qu'est-ce qu'un opérateur ternaire ?

Un opérateur ternaire est un opérateur conditionnel en JavaScript qui évalue une expression conditionnelle et retourne soit une valeur truthy, soit une valeur falsy.

Pour comprendre comment cela fonctionne, examinons de plus près sa syntaxe ci-dessous :

```js
conditionalExpression ? truthyValue : falsyValue
```

D'après la syntaxe ci-dessus, `conditionalExpression` est l'expression qui sert de point d'évaluation, déterminant soit une valeur truthy, soit une valeur falsy.

Suivant le `?` (point d'interrogation), la valeur fournie est retournée si l'expression est évaluée à truthy, tandis que la valeur suivant le `:` (deux-points) est retournée si l'expression donne un résultat falsy.

Les `truthyValue` et `falsyValue` peuvent être n'importe quoi en JavaScript. Cela peut inclure diverses entités telles que des fonctions, des valeurs stockées dans des variables, des objets, des nombres, des chaînes de caractères, et plus encore. L'opérateur ternaire vous offre la flexibilité de retourner n'importe quelle valeur souhaitée, offrant ainsi une grande polyvalence dans votre code.

## Comment utiliser l'opérateur ternaire

Maintenant que nous avons examiné la syntaxe et son fonctionnement, explorons comment utiliser l'opérateur ternaire pour approfondir notre compréhension.

Considérons ce scénario : nous construisons une plateforme de jeu qui n'autorise que les utilisateurs âgés de 18 ans et plus. Nous allons concevoir une fonction pour vérifier l'âge d'un utilisateur. S'il a moins de 18 ans, l'accès lui sera refusé ; sinon, il pourra accéder à la plateforme.

```js
function canAccessPlatform(age) {
  const shouldAccess = age >= 18 ? true : false;

  return shouldAccess;
}
```

D'après l'extrait de code ci-dessus, nous avons créé une fonction, `canAccessPlatform`, qui évalue si un utilisateur, représenté par son paramètre `age`, remplit la condition pour accéder à la plateforme.

Elle utilise un opérateur ternaire pour déterminer si l'âge est de 18 ans ou plus, attribuant `true` à `shouldAccess` si la condition est remplie, et `false` sinon. Enfin, elle retourne la valeur de `shouldAccess`, indiquant si l'utilisateur peut accéder à la plateforme ou non.

Si l'âge est de 18 ans ou plus, l'expression devient vraie, donc l'opérateur retourne true après le `?`. Sinon, il retourne false. Ce résultat est enregistré dans une variable puis retourné par la fonction.

Bien que ce cas d'utilisation de base simplifie le code et améliore la lisibilité en remplaçant les blocs if-else inutiles, il est important de l'utiliser avec parcimonie pour éviter d'encombrer et de compliquer votre code. Plus tard, nous discuterons des bonnes pratiques pour utiliser l'opérateur ternaire.

Voici un autre exemple illustrant l'utilisation de l'opérateur ternaire. Nous allons créer une fonction pour déterminer si un nombre est pair ou impair. Consultez l'extrait de code ci-dessous :

```js
function checkEvenOrOdd(number) {
  const result = number % 2 === 0 ? "even" : "odd";
  return result;
}

// Utilisation :
console.log(checkEvenOrOdd(4)); // Sortie : "even"
console.log(checkEvenOrOdd(7)); // Sortie : "odd"
```

D'après l'extrait de code ci-dessus :

* Nous définissons une fonction `checkEvenOrOdd` qui prend un paramètre `number`.
* À l'intérieur de la fonction, nous utilisons l'opérateur ternaire pour vérifier si le nombre est pair ou impair.
* Si le nombre modulo 2 est égal à 0 (ce qui signifie qu'il est divisible par 2 sans reste), alors la condition est évaluée à true, et la chaîne "even" est attribuée à la variable `result`.
* Si la condition est évaluée à false (ce qui signifie que le nombre est impair), la chaîne "odd" est attribuée à `result`.
* Enfin, la fonction retourne la valeur de `result`, qui indique si le nombre est pair ou impair.

Ce code montre comment l'opérateur ternaire vérifie rapidement si un nombre est pair ou impair, rendant le code plus facile à lire et à comprendre.

## Comment refactoriser les instructions if-else en opérateur ternaire

Un avantage de l'opérateur ternaire est d'éviter les blocs if-else inutiles, qui peuvent compliquer la lisibilité et la maintenance du code. Dans cette section, nous allons refactoriser certaines instructions if-else en opérations ternaires, offrant une compréhension plus claire de l'utilisation efficace des opérateurs ternaires.

Commençons par notre premier exemple :

```js
function decideActivity(weather) {
  let activity;

  if (weather === "sunny") {
    activity = "go out";
  } else {
    activity = "stay in";
  }

  console.log(activity);
}

// Utilisation
console.log(decideActivity("raining")); // Sortie : "stay in"
console.log(decideActivity("snowing")); // Sortie : "stay in"
console.log(decideActivity("sunny")); // Sortie : "go out"
```

Cette fonction, `decideActivity`, prend un paramètre `weather` et détermine l'activité appropriée en fonction de la condition météorologique.

Si le temps est "sunny", elle suggère de "go out". Sinon, elle conseille de "stay in". Lorsque nous appelons la fonction avec différentes conditions météorologiques comme "raining" ou "snowing", elle affiche la recommandation d'activité correspondante en utilisant `console.log()`.

Par exemple, appeler `decideActivity("raining")` affichera "stay in". De même, `decideActivity("snowing")` affichera également "stay in". Lorsque `decideActivity("sunny")` est appelé, il affiche "go out". Cette fonction simple aide à décider des activités en fonction de la condition météorologique fournie.

Maintenant, nous pouvons refactoriser ces blocs de code pour les rendre plus simples et plus nets. Voyons comment faire cela ci-dessous :

```js
function decideActivity(weather){
   const activity = weather === "sunny" ? "go out" : "stay in";
   
   console.log(activity)

}

// Utilisation
console.log(decideActivity("raining")); // Sortie : "stay in"
console.log(decideActivity("snowing")); // Sortie : "stay in"
console.log(decideActivity("sunny")); // Sortie : "go out"
```

D'après l'exemple de code ci-dessus, cette fonction, `decideActivity`, utilise l'opérateur ternaire pour déterminer rapidement l'activité en fonction de la condition météorologique. Elle vérifie si le temps est "sunny" et attribue "go out" si vrai, sinon "stay in".

Nous avons simplifié les instructions if-else en un opérateur ternaire en une ligne. Cela rend notre code plus propre, plus clair et plus facile à lire.

Prenons un autre exemple :

```js
function checkNumber(number) {
  let result;
  if (number > 0) {
    result = "positive";
  } else {
    result = "non-positive";
  }
  return result;
}

// Utilisation
console.log(checkNumber(5)); // Sortie : "positive"
console.log(checkNumber(-2)); // Sortie : "non-positive"

```

Expliquons ce que fait le code ci-dessus :

* **Définition de la fonction** : Nous commençons par définir une fonction nommée `checkNumber` qui prend un seul paramètre appelé `number`.
* **Déclaration de variable** : À l'intérieur de la fonction, nous déclarons une variable nommée `result` sans lui attribuer de valeur pour l'instant. Cette variable stockera le résultat de notre vérification.
* **Instruction conditionnelle (if-else)** : Nous avons une instruction conditionnelle qui vérifie si le paramètre `number` est supérieur à 0.
* Si la condition est vraie (ce qui signifie que le nombre est positif), nous attribuons la chaîne "positive" à la variable `result`.
* Si la condition est fausse (ce qui signifie que le nombre n'est pas positif, c'est-à-dire qu'il est soit négatif soit zéro), nous attribuons la chaîne "non-positive" à la variable `result`.
* **Instruction de retour** : Enfin, nous retournons la valeur stockée dans la variable `result`.
* **Appels de fonction** : Nous appelons ensuite la fonction `checkNumber` deux fois avec différents arguments : 5 et -2.

Lorsque nous appelons `checkNumber(5)`, la fonction retourne "positive", qui est ensuite enregistrée dans la console.

De même, lorsque nous appelons `checkNumber(-2)`, la fonction retourne "non-positive", qui est à nouveau enregistrée dans la console.

Cette fonction détermine efficacement si un nombre est positif ou non positif et fournit le résultat approprié en fonction de la condition.

Simplifions et améliorons le code en le réécrivant en utilisant un opérateur ternaire.

```js
function checkNumber(number) {
  const result = number > 0 ? "positive" : "non-positive";
  return result;
}

// Utilisation
console.log(checkNumber(5)); // Sortie : "positive"
console.log(checkNumber(-2)); // Sortie : "non-positive"

```

Excellent travail ! En refactorisant la fonction et en utilisant l'opérateur ternaire pour l'évaluation conditionnelle, nous avons obtenu un code plus propre, plus concis et plus lisible.

Ce code, utilisant l'opérateur ternaire, semble plus concis et élégant. Il détermine efficacement si un nombre est positif ou non positif, rendant le code plus propre et plus facile à comprendre. Lorsque nous appelons `checkNumber(5)`, il retourne "positive", tandis que `checkNumber(-2)` retourne "non-positive". Globalement, l'opérateur ternaire améliore la lisibilité du code.

## Comment enchaîner les opérateurs ternaires

Lorsqu'il s'agit de vérifications conditionnelles, parfois une seule condition ne suffit pas. Dans de tels cas, nous utilisons des instructions 'else-if' avec 'if/else' pour incorporer plusieurs conditions.

Examinons la syntaxe :

```js
function exampleFn() {
  return conditionalExpression1
    ? value1
    : conditionalExpression2
    ? value2
    : conditionalExpression3
    ? value3
    : value4;
}
```

Cela peut être traduit en une chaîne if/else :

```js
function exampleFn() {
  if (conditionalExpression1) {
    return value1;
  } else if (conditionalExpression2) {
    return value2;
  } else if (conditionalExpression3) {
    return value3;
  } else {
    return value4;
  }
}

```

Explorons un exemple ci-dessous :

```js
function checkNumber(number) {
  let message;

  if (number > 0) {
    message = "Positive";
  } else if (number === 0) {
    message = "Zero";
  } else {
    message = "Negative";
  }

  return message;
}

// Utilisation
console.log(checkNumber(5)); // Sortie : "Positive"
console.log(checkNumber(0)); // Sortie : "Zero"
console.log(checkNumber(-3)); // Sortie : "Negative"

```

Ce code ci-dessus définit une fonction appelée `checkNumber` qui prend un paramètre `number` et détermine son statut (positif, zéro ou négatif). Il utilise un bloc if-else avec une instruction else-if pour évaluer la valeur du nombre. Si le nombre est supérieur à 0, il est considéré comme positif et s'il est égal à 0, il est zéro. Sinon, il est négatif. La fonction retourne le résultat.

Refactorisons ce code en utilisant un opérateur ternaire pour obtenir la même fonctionnalité.

```js
function checkNumber(number) {
  return number > 0 ? "Positive" : number === 0 ? "Zero" : "Negative";
}

// Utilisation
console.log(checkNumber(5)); // Sortie : "Positive"
console.log(checkNumber(0)); // Sortie : "Zero"
console.log(checkNumber(-3)); // Sortie : "Negative"

```

C'est tout ! Nous avons refactorisé la fonction, et en y regardant de plus près, nous pouvons observer que les opérateurs sont enchaînés. Maintenant, explorons comment fonctionne l'opérateur ternaire enchaîné dans la fonction `checkNumber`.

Dans le premier opérateur ternaire :

* La première partie `number > 0` vérifie si le nombre est supérieur à 0.
* Si c'est vrai, l'expression retourne "Positive".

Dans le deuxième opérateur ternaire (enchaîné) :

* Si la première condition est fausse (ce qui signifie que le nombre n'est pas supérieur à 0), il passe à la partie suivante de l'expression : `number === 0`.
* Cette partie vérifie si le nombre est égal à 0.
* Si c'est vrai, l'expression retourne "Zero".

Et la valeur par défaut :

* Si aucune des conditions ci-dessus n'est vraie (ce qui signifie que le nombre n'est pas supérieur à 0 et n'est pas égal à 0), il passe par défaut à la dernière partie de l'expression : `"Negative"`.
* Cette partie agit comme la valeur par défaut si aucune des conditions précédentes n'est remplie.

En résumé, l'opérateur ternaire enchaîné évalue plusieurs conditions en une seule ligne de code. Il vérifie chaque condition séquentiellement, et la première condition qui est évaluée à vrai détermine le résultat de l'expression entière. Cela permet une logique conditionnelle concise et efficace.

Examinons un autre exemple d'opérateur ternaire enchaîné.

```js
function getDrink(age) {
  return age >= 21
    ? "Enjoy a cocktail"
    : age >= 18
    ? "Have a beer"
    : age >= 16
    ? "Grab a soft drink"
    : "Sorry, you're too young to drink";
}

// Utilisation
console.log(getDrink(25)); // Sortie : "Enjoy a cocktail"
console.log(getDrink(19)); // Sortie : "Have a beer"
console.log(getDrink(16)); // Sortie : "Grab a soft drink"
console.log(getDrink(10)); // Sortie : "Sorry, you're too young to drink"

```

Dans l'exemple de code donné, les opérateurs ternaires sont enchaînés pour fournir différentes suggestions de boissons en fonction de l'âge fourni. Chaque expression conditionnelle de la chaîne évalue une plage d'âge spécifique.

Si la première condition est vraie (truthy), elle retourne 'Enjoy a cocktail'. Si elle est fausse (falsy), elle passe à l'expression conditionnelle suivante, et ainsi de suite. Ce processus d'enchaînement continue jusqu'à ce qu'une condition soit évaluée à vraie. Si aucune des conditions de la chaîne n'est vraie, la dernière valeur est retournée comme solution de repli, similaire au bloc 'else' dans une instruction if/else.

Le concept d'« enchaînement » des opérateurs ternaires implique de lier des expressions conditionnelles en fonction de la valeur de l'expression précédente. Cela peut être comparé à la structure `else if` dans une instruction `if/else`, offrant un moyen concis de gérer plusieurs conditions en JavaScript.

## Bonnes pratiques lors de l'utilisation de l'opérateur ternaire

L'utilisation efficace de l'opérateur ternaire peut considérablement améliorer la lisibilité et la concision du code. Dans cette section, nous allons explorer les meilleures pratiques pour utiliser efficacement l'opérateur ternaire.

1. **Gardez-le simple et lisible** : Écrivez des expressions concises qui sont faciles à comprendre d'un coup d'œil. Évitez d'imbriquer trop d'opérateurs ternaires ou d'écrire des conditions trop complexes.
2. **Utilisez pour des affectations simples** : Les opérateurs ternaires sont idéaux pour des affectations simples où il n'y a que deux résultats possibles basés sur une condition. Pour des scénarios plus complexes, envisagez d'utiliser des instructions `if/else`.
3. **Sachez quand l'utiliser** : Utilisez l'opérateur ternaire lorsque vous devez effectuer une vérification conditionnelle simple et attribuer une valeur basée sur le résultat. Il est particulièrement utile pour attribuer des valeurs par défaut ou déterminer la valeur d'une variable basée sur une condition.
4. **Testez minutieusement** : Testez votre code minutieusement pour vous assurer que l'opérateur ternaire se comporte comme prévu dans différentes conditions. Vérifiez les cas limites et validez l'exactitude des valeurs attribuées.
5. **Évitez les ternaires imbriqués** : Bien que l'enchaînement des ternaires soit possible, une imbrication excessive peut conduire à un code difficile à lire. Préférez la clarté et envisagez d'utiliser `if/else` pour des conditions complexes.
6. **Gardez les ternaires courts** : Efforcez-vous de garder les expressions ternaires courtes et concises. Les ternaires longs peuvent être difficiles à lire et à comprendre, entraînant des défis de maintenance du code.

Ces bonnes pratiques décrivent des lignes directrices pour utiliser efficacement l'opérateur ternaire. Bien qu'elles ne soient pas des règles strictes, elles offrent des informations précieuses pour améliorer la clarté et la lisibilité de votre code.

## Conclusion

Alors que nous concluons cet article, vous avez acquis une compréhension approfondie de l'opérateur ternaire—son application dans les tâches de codage quotidiennes, la conversion des instructions if/else, l'enchaînement des opérateurs et les bonnes pratiques. Je suis convaincu que vous avez acquis des informations précieuses qui amélioreront vos pratiques de codage en utilisant l'opérateur ternaire.

Merci d'avoir lu, et à la prochaine !

### Informations de contact

Souhaitez-vous entrer en contact avec moi ? N'hésitez pas à me contacter via l'un des canaux suivants :

* Twitter / X : [@developeraspire](https://twitter.com/developeraspire)
* Email : developeraspire5@gmail.com