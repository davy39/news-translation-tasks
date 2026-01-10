---
title: Comment utiliser l'opérateur ternaire en JavaScript – Exemple de condition
  JS
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-02-27T18:40:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-ternary-operator-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-ken-tomita-389818.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser l'opérateur ternaire en JavaScript – Exemple de condition
  JS
seo_desc: 'The ternary operator is a helpful feature in JavaScript that allows you
  to write concise and readable expressions that perform conditional operations on
  only one line.

  In this article, you will learn why you may want to use the ternary operator, and
  ...'
---

L'opérateur ternaire est une fonctionnalité utile en JavaScript qui permet d'écrire des expressions concises et lisibles effectuant des opérations conditionnelles en une seule ligne.

Dans cet article, vous apprendrez pourquoi vous pourriez vouloir utiliser l'opérateur ternaire, et vous verrez un exemple de son utilisation. Vous apprendrez également certaines des meilleures pratiques à garder à l'esprit lorsque vous l'utilisez.

Commençons !

## Qu'est-ce que l'opérateur ternaire en JavaScript ?

L'opérateur ternaire (`?:`), également connu sous le nom d'opérateur conditionnel, est une manière abrégée d'écrire des instructions conditionnelles en JavaScript – vous pouvez utiliser un opérateur ternaire au lieu d'une instruction `if..else`.

Un opérateur ternaire évalue une condition donnée, également connue sous le nom d'expression booléenne, et retourne un résultat qui dépend du fait que cette condition évalue à `true` ou `false`.

### Pourquoi utiliser l'opérateur ternaire en JavaScript ?

Vous pourriez vouloir utiliser l'opérateur ternaire pour plusieurs raisons :

- **Votre code sera plus concis** : L'opérateur ternaire a une syntaxe minimale. Vous écrirez des instructions conditionnelles courtes et moins de lignes de code, ce qui rend votre code plus facile à lire et à comprendre.
- **Votre code sera plus lisible** : Lors de l'écriture de conditions simples, l'opérateur ternaire rend votre code plus facile à comprendre par rapport à une instruction `if..else`.
- **Votre code sera plus organisé** : L'opérateur ternaire rendra votre code plus organisé et plus facile à maintenir. Cela s'avère utile lors de l'écriture de plusieurs instructions conditionnelles. L'opérateur ternaire réduira la quantité de nesting qui se produit lors de l'utilisation d'instructions `if..else`.
- **Il offre de la flexibilité** : L'opérateur ternaire a de nombreux cas d'utilisation, dont certains incluent : l'assignation d'une valeur à une variable, le rendu de contenu dynamique sur une page web, la gestion des arguments de fonction, la validation de données et la gestion des erreurs, et la création d'expressions complexes.
- **Il améliore les performances** : Dans certains cas, l'opérateur ternaire peut performer mieux qu'une instruction `if..else` car l'opérateur ternaire est évalué en une seule étape.
- **Il retourne toujours une valeur** : L'opérateur ternaire doit toujours retourner quelque chose.

## Comment utiliser l'opérateur ternaire en JavaScript – Aperçu de la syntaxe

L'opérateur est appelé "ternaire" car il est composé de trois parties : une condition et deux expressions.

La syntaxe générale de l'opérateur ternaire ressemble à ceci :

```
condition ? ifTrueExpression : ifFalseExpression;
```

Décomposons cela :

- `condition` est l'expression booléenne que vous souhaitez évaluer pour déterminer si elle est `true` ou `false`. La condition est suivie d'un point d'interrogation, `?`.
- `ifTrueExpression` est exécutée si la condition évalue à `true`.
- `ifFalseExpression` est exécutée si la condition évalue à `false`.
- Les deux expressions sont séparées par un deux-points, `:`.

L'opérateur ternaire retourne toujours une valeur que vous assignerez à une variable :

```
const returnValue = condition ? ifTrueExpression : ifFalseExpression;
```

Ensuite, examinons un exemple de fonctionnement de l'opérateur ternaire.

## Comment utiliser l'opérateur ternaire en JavaScript

Supposons que vous souhaitiez vérifier si un utilisateur est un adulte :

```javascript
// obtenir l'entrée de l'utilisateur
const age = prompt("Quel est votre âge ?");

// vérifier la condition
const message = (age >= 18) ? "Vous êtes un adulte" : "Vous n'êtes pas encore un adulte";

console.log(message);
```

Dans cet exemple, j'ai utilisé l'opérateur ternaire pour déterminer si l'âge d'un utilisateur est supérieur ou égal à `18`.

Tout d'abord, j'ai utilisé la fonction intégrée `prompt()` de JavaScript.

Cette fonction ouvre une boîte de dialogue avec le message `Quel est votre âge ?` et l'utilisateur peut entrer une valeur.

Je stocke l'entrée de l'utilisateur dans la variable `age`.

Ensuite, la condition (`age >= 18`) est évaluée.

Si la condition est `true`, la première expression, `Vous êtes un adulte`, est exécutée.

Supposons que l'utilisateur entre la valeur `18`.

La condition `age >= 18` évalue à `true` :

```
Quel est votre âge ? 18

// sortie
Vous êtes un adulte
```

Si la condition est `false`, la deuxième expression, `Vous n'êtes pas encore un adulte`, est exécutée.

Supposons que l'utilisateur entre la valeur `17`.

La condition `age >= 18` évalue maintenant à `false` :

```
Quel est votre âge ? 17

// sortie
Vous n'êtes pas encore un adulte
```

Comme mentionné précédemment, vous pouvez utiliser l'opérateur ternaire au lieu d'une instruction `if..else`.

Voici comment vous écririez le même code utilisé dans l'exemple ci-dessus en utilisant une instruction `if..else` :

```javascript
// obtenir l'entrée de l'utilisateur
const age = prompt("Quel est votre âge ?");

// vérifier la condition

if (age >= 18) {
  console.log("Vous êtes un adulte");
} else {
  console.log("Vous n'êtes pas encore un adulte");
}
```

## Bonnes pratiques de l'opérateur ternaire en JavaScript

Une chose à garder à l'esprit lors de l'utilisation de l'opérateur ternaire est de le garder simple et de ne pas le compliquer.

L'objectif principal est que votre code soit lisible et facilement compréhensible pour les autres développeurs de votre équipe.

Ainsi, envisagez d'utiliser l'opérateur ternaire pour des instructions simples et comme alternative concise aux instructions `if..else` qui peuvent être écrites en une ligne.

Si vous en faites trop, cela peut rapidement devenir illisible.

Par exemple, dans certains cas, l'utilisation d'opérateurs ternaires imbriqués peut rendre votre code difficile à lire :

```javascript
// obtenir l'entrée de l'utilisateur
const age = prompt("Quel est votre âge ?");

// vérifier la condition
const message = (age >= 18) ? (age == 18 ? "Vous avez exactement 18 ans" : "Vous avez plus de 18 ans") : "Vous avez moins de 18 ans";

console.log(message);
```

Si vous vous retrouvez à imbriquer trop d'opérateurs ternaires, envisagez d'utiliser des instructions `if...else` à la place.

## Conclusion

Dans l'ensemble, l'opérateur ternaire est une fonctionnalité utile en JavaScript car il aide à rendre votre code plus lisible et concis.

Utilisez-le lorsqu'une instruction conditionnelle peut être écrite en une seule ligne et gardez à l'esprit la lisibilité du code.

Merci d'avoir lu, et bon codage ! :)