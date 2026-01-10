---
title: Comment utiliser l'enchaînement optionnel en JavaScript
subtitle: ''
author: Natalie Pina
co_authors: []
series: null
date: '2022-02-07T17:13:35.000Z'
originalURL: https://freecodecamp.org/news/javascript-optional-chaining
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/pexels-pixabay-220237.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser l'enchaînement optionnel en JavaScript
seo_desc: 'Optional chaining is a safe and concise way to perform access checks for
  nested object properties.

  The optional chaining operator ?. takes the reference to its left and checks if
  it is undefined or null. If the reference is either of these nullish va...'
---

L'enchaînement optionnel est une manière sûre et concise de effectuer des vérifications d'accès pour les propriétés d'objets imbriqués.

L'opérateur d'enchaînement optionnel `?.` prend la référence à sa gauche et vérifie si elle est indéfinie ou nulle. Si la référence est l'une de ces valeurs nulles, les vérifications s'arrêteront et retourneront indéfini. Sinon, la chaîne de vérifications d'accès se poursuivra sur le chemin heureux vers la valeur finale.

```
// Un objet person vide avec des informations de localisation optionnelles manquantes
const person = {}

// Ce qui suit sera équivalent à undefined au lieu d'une erreur
const currentAddress = person.location?.address


```

L'enchaînement optionnel a été introduit dans ES2020. Selon [TC39](https://github.com/tc39/proposal-optional-chaining), il est actuellement à l'étape 4 du processus de proposition et est préparé pour l'inclusion dans la norme finale ECMAScript. Cela signifie que vous pouvez l'utiliser, mais notez que les anciens navigateurs peuvent encore nécessiter l'utilisation de polyfill.

L'enchaînement optionnel est une fonctionnalité utile qui peut vous aider à écrire un code plus propre. Maintenant, apprenons comment nous pouvons l'utiliser.

## Syntaxe de l'enchaînement optionnel

Dans cet article, je couvrirai principalement comment accéder aux propriétés des objets. Mais vous pouvez également utiliser l'enchaînement optionnel comme vérification sur les fonctions.

Voici tous les cas d'utilisation de l'enchaînement optionnel :

```
obj?.prop       // accès optionnel à une propriété statique
obj?.[expr]     // accès optionnel à une propriété dynamique
func?.(...args) // appel optionnel de fonction ou de méthode

```

Source : [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)

### Exemple :

```
const value = obj?.propOne?.propTwo?.propThree?.lastProp;
```

Dans l'extrait de code ci-dessus, nous vérifions si `obj` est null ou undefined, puis `propOne`, puis `propTwo`, et ainsi de suite. L'enchaînement optionnel porte bien son nom. Dans la chaîne d'accès aux propriétés de l'objet, nous pouvons vérifier que chaque valeur n'est pas indéfinie ou nulle.

Cette vérification peut être extrêmement utile lors de l'accès à des valeurs d'objets profondément imbriquées. C'est une fonctionnalité très attendue et elle vous évite d'avoir à effectuer de nombreuses vérifications de nullité. Cela signifie également que vous n'avez pas besoin d'utiliser des variables temporaires pour stocker des valeurs vérifiées, par exemple :

```
const neighborhood = city.nashville && city.nashvile.eastnashville;

```

Ici, nous pouvons vérifier que `nashville` est une propriété dans `city` avant d'essayer d'accéder à la propriété de quartier intérieur de `eastnashville`. Nous pouvons convertir ce qui précède pour utiliser l'enchaînement optionnel, comme suit :

```
const neighborhood = city?.nashville?.eastnashville;
```

L'enchaînement optionnel simplifie cette expression.

## Gestion des erreurs avec l'enchaînement optionnel

L'enchaînement optionnel est particulièrement utile lors de la manipulation de données d'API. Si vous n'êtes pas sûr qu'une propriété optionnelle existe, vous pouvez utiliser l'enchaînement optionnel.

### Un mot de prudence

N'utilisez pas l'enchaînement optionnel à chaque opportunité. Cela pourrait entraîner le silence des erreurs en ayant potentiellement undefined retourné à de nombreux endroits.

Il est également important de se rappeler que la vérification s'arrêtera et "court-circuiter" dès qu'elle rencontrera une valeur nulle. Tenez-en compte pour les propriétés suivantes dans la chaîne et ce qui se produira si elles ne peuvent pas être atteintes.

Il est préférable d'utiliser cette vérification lorsque vous savez que quelque chose peut ne pas avoir de valeur, comme une propriété optionnelle. Si une valeur requise a une vérification de nullité, elle peut être silencée avec undefined retourné au lieu de retourner une erreur pour signaler ce problème.

## Enchaînement optionnel + Coalescence des valeurs nulles

L'enchaînement optionnel se marie bien avec la coalescence des valeurs nulles `??` pour fournir des valeurs de repli.

```
const data = obj?.prop ?? "chaîne de repli";
```

```
const data = obj?.prop?.func() ?? fallbackFunc();
```

Si l'élément à gauche de `??` est nul, l'élément à droite sera retourné.

Nous savons que si une vérification `?.` équivaut à une valeur nulle dans la chaîne, elle retournera `undefined`. Nous pouvons donc utiliser notre coalescence des valeurs nulles pour répondre au résultat indéfini et définir une valeur de repli explicite.

```
const meal = menu.breakfast?.waffles ?? "No Waffles Found."
```

### Conclusion

L'enchaînement optionnel est une fonctionnalité récente pratique de JavaScript qui vous permet de vérifier les valeurs nulles lors de l'accès aux valeurs des propriétés. Vous pouvez également l'utiliser avec l'opérateur `?.`.

J'espère que cet article a aidé à introduire ou à clarifier l'enchaînement optionnel. Bon codage !