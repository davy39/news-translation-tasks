---
title: Portée lexicale en JavaScript – Qu'est-ce que la portée en JS ?
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2021-08-19T19:56:48.000Z'
originalURL: https://freecodecamp.org/news/javascript-lexical-scope-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/kristina-tripkovic-EGmwwDzme6s-unsplash-javascript-lexical-scope-codesweetly.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Lexical Scoping
  slug: lexical-scoping
seo_title: Portée lexicale en JavaScript – Qu'est-ce que la portée en JS ?
seo_desc: 'The term “lexical scope” may seem tricky to grasp at first glance. But
  it''s helpful to understand what each word means.

  So this article will explain lexical scope by first examining the meaning of “lexical”
  and “scope”.

  So, let’s get it started by un...'
---

Le terme **« portée lexicale »** peut sembler difficile à comprendre au premier abord. Mais il est utile de comprendre ce que signifie chaque mot.

Cet article expliquera donc la portée lexicale en examinant d'abord la signification de « lexical » et de « portée ».

Commençons donc par comprendre le terme « portée ».

## Qu'est-ce que la portée exactement ?

**Portée** fait référence à la _zone_ où un élément (comme une fonction ou une variable) est visible et accessible par d'autres [code](https://www.codesweetly.com/document-vs-data-vs-code/).

**Note :**

* **Portée** signifie zone, espace ou région.
* **Portée globale** signifie espace global ou espace public.
* **Portée locale** signifie une région locale ou une région restreinte.

**Voici un exemple :**

```js
// Définir une variable dans la portée globale :
const fullName = "Oluwatobi Sofela";

// Définir des fonctions imbriquées :
function profile() {
  function sayName() {
    function writeName() {
      return fullName;
    }
    return writeName();
  }
  return sayName();
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-fqqxjl?file=script.js)

Dans l'extrait ci-dessus, nous avons défini la variable `fullName` dans la portée globale. Cela signifie qu'elle est visible et accessible globalement à tout le code du script.

Mais nous avons défini `writeName()` dans la fonction `sayName()`, donc elle est locale à `sayName()`.

En d'autres termes, `writeName()` est visible et accessible localement uniquement pour le code dans la fonction `sayName()`.

Gardez à l'esprit que chaque fois que la fonction `writeName()` est appelée, l'ordinateur n'ira _pas_ directement à la portée globale pour appeler la variable `fullName`. Au lieu de cela, il doit passer séquentiellement par la [chaîne de portée](#heading-quest-ce-quune-chaine-de-portee) pour rechercher `fullName`.

## Qu'est-ce qu'une chaîne de portée ?

Une **chaîne de portée** fait référence aux espaces _uniques_ qui existent depuis la portée où une variable a été _appelée_ jusqu'à la portée globale.

**Voici un exemple :**

```js
// Définir une variable dans la portée globale :
const fullName = "Oluwatobi Sofela";

// Définir des fonctions imbriquées :
function profile() {
  function sayName() {
    function writeName() {
      return fullName;
    }
    return writeName();
  }
  return sayName();
}
```

Dans l'extrait ci-dessus, observez que la variable `fullName` a été appelée depuis la portée de la fonction `writeName()`.

Par conséquent, la chaîne de portée qui existe depuis l'appel de la variable jusqu'à la portée globale est :

**writeName() portée ---> sayName() portée ---> profile() portée ---> portée globale**

En d'autres termes, il y a quatre (4) espaces depuis la portée d'invocation de `fullName` jusqu'à sa portée lexicale (la _portée globale_ dans ce cas).

**Note :** La portée globale est le dernier maillon de la chaîne de portée de [JavaScript](https://www.codesweetly.com/html-css-javascript/).

## Comment fonctionne la chaîne de portée ?

La chaîne de portée de JavaScript détermine la hiérarchie des endroits par lesquels l'ordinateur doit passer — l'un après l'autre — pour trouver la portée lexicale (origine) de la variable spécifique qui a été appelée.

Par exemple, considérons le code ci-dessous :

```js
// Définir une variable dans la portée globale :
const fullName = "Oluwatobi Sofela";

// Définir des fonctions imbriquées :
function profile() {
  function sayName() {
    function writeName() {
      return fullName;
    }
    return writeName();
  }
  return sayName();
}
```

Dans l'extrait ci-dessus, chaque fois que la fonction `profile()` est appelée, l'ordinateur appellera d'abord la fonction `sayName()` (qui est le seul code dans la fonction `profile()`).

Deuxièmement, l'ordinateur appellera la fonction `writeName()` (qui est le seul code dans la fonction `sayName()`).

À ce stade, puisque le code dans `writeName()` demande à l'ordinateur d'appeler et de retourner le contenu de la variable `fullName`, l'ordinateur appellera `fullName`. Mais il n'ira pas directement à la portée globale pour appeler `fullName`.

Au lieu de cela, l'ordinateur doit passer _étape par étape_ par la _chaîne de portée_ pour rechercher la _portée lexicale_ de `fullName`.

Voici donc les étapes séquentielles que l'ordinateur doit suivre pour localiser la portée lexicale de `fullName` :

1. Tout d'abord, l'ordinateur vérifiera si `fullName` a été définie localement dans la fonction `writeName()`. Mais il ne trouvera aucune définition de `fullName` là, donc il passera à la portée suivante pour continuer sa quête.
2. Deuxièmement, l'ordinateur recherchera la définition de `fullName` dans `sayName()` (l'espace suivant dans la chaîne de portée). Toujours sans succès, il monte à la portée suivante.
3. Troisièmement, l'ordinateur recherchera la définition de `fullName` dans la fonction `profile()`. Pourtant, `fullName` n'est toujours pas trouvée là. L'ordinateur passe donc à la recherche de la portée lexicale de `fullName` dans la région suivante de la chaîne de portée.
4. Quatrièmement, l'ordinateur se rend à la _portée globale_ (la portée suivante après `profile()`). Heureusement, il trouve la définition de fullName là ! Il obtient donc son contenu (`"Oluwatobi Sofela"`) et le retourne.

## Temps de pratiquer avec la portée 🧘‍♂️🏃‍♀️🏊‍♀️

Considérez le script ci-dessous. Quelle des trois variables `fullName` l'ordinateur appellera-t-il ?

```js
// Première variable fullName définie dans la portée globale :
const fullName = "Oluwatobi Sofela";

// Fonctions imbriquées contenant deux autres variables fullName :
function profile() {
  const fullName = "Tobi Sho";
  function sayName() {
    const fullName = "Oluwa Sofe";
    function writeName() {
      return fullName;
    }
    return writeName();
  }
  return sayName();
}
```

L'ordinateur appellera-t-il la première, la deuxième ou la troisième variable `fullName` ?

**Note :** Vous bénéficierez beaucoup plus de ce tutoriel si vous essayez l'exercice vous-même.

Si vous êtes bloqué, ne vous découragez pas. Au lieu de cela, révisez la leçon et essayez à nouveau.

Une fois que vous aurez fait de votre mieux (vous ne tricherez que vous-même si vous ne le faites pas !), allez-y pour voir la réponse correcte ci-dessous.

## Avez-vous trouvé la bonne réponse ?

Parmi les trois _définitions_ de `fullName` présentes dans le script ci-dessus, l'ordinateur appellera et retournera celle définie dans la fonction `sayName()`.

La variable `fullName` de `sayName()` sera appelée car `sayName()` est la portée dans laquelle l'ordinateur trouvera d'abord une définition de `fullName`.

Par conséquent, lorsque `profile()` est appelée, la valeur retournée sera `"Oluwa Sofe"`.

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/web-platform-9mpvfv?file=script.js)

**Quelques points à retenir :**

* Supposons que l'ordinateur n'ait pas trouvé la définition de `fullName` dans aucune des portées. Dans un tel cas, l'ordinateur retournera `Uncaught ReferenceError: fullName is not defined`.
* La portée globale est toujours la dernière portée de toute chaîne de portée JavaScript. En d'autres termes, la portée globale est l'endroit où toutes les recherches se termineront.
* Une portée interne (enfant) a accès à sa portée parente (externe), mais une portée externe n'a pas accès à sa portée enfant. Par exemple, dans l'extrait ci-dessus, `writeName()` peut accéder aux codes à l'intérieur de n'importe quelle portée parente (`sayName()`, `profile()`, ou la _portée globale_). Cependant, ni `sayName()`, ni `profile()`, ni la _portée globale_ ne peuvent accéder à aucun des codes de `writeName()`.

## Révision rapide de la portée jusqu'à présent

La portée JavaScript concerne l'espace.

Donc, la prochaine fois que votre partenaire vous appelle dans sa portée privée, rappelez-vous qu'il vous invite dans son espace privé 😜 !

Lorsque vous y serez, assurez-vous de lui demander quel est son meilleur jeu lexical...

Mais que signifie lexical, je vous entends demander ? Découvrons-le ci-dessous.

## Que signifie lexical ?

**Lexical** fait référence à la définition des choses.

Tout ce qui est lié à la création de mots, d'expressions ou de variables est qualifié de _lexical_.

Par exemple, un jeu de [scrabble](https://en.wikipedia.org/wiki/Scrabble) est une activité lexicale car il est lié à la création de mots.

De plus, quelqu'un dont le travail est lié à la linguistique (l'étude des langues) a une carrière lexicale.

**Note :** Un autre nom pour un dictionnaire est un _lexique_. En d'autres termes, un lexique est un dictionnaire où les mots sont listés et définis.

Maintenant que nous savons ce que signifient portée et lexical, nous pouvons parler de la portée lexicale.

## Qu'est-ce que la portée lexicale en JavaScript ?

**Portée lexicale** est la zone de _définition_ d'une expression.

En d'autres termes, la portée lexicale d'un élément est l'endroit où l'élément a été _créé_.

**Note :**

* Un autre nom pour la portée lexicale est _portée statique_.
* L'endroit où un élément a été appelé (ou invoqué) n'est pas nécessairement la portée lexicale de l'élément. Au lieu de cela, l'_espace de définition_ d'un élément est sa portée lexicale.

### Exemple de portée lexicale

Considérez le code ci-dessous :

```js
// Définir une variable dans la portée globale :
const myName = "Oluwatobi";

// Appeler la variable myName depuis une fonction :
function getName() {
  return myName;
}
```

Dans l'extrait ci-dessus, notez que nous avons _définie_ la variable `myName` dans la portée globale et l'avons _appelée_ dans la fonction `getName()`.

**Question :** Lequel des deux espaces est la portée lexicale de `myName` ? Est-ce la _portée globale_ ou la portée locale de la fonction `getName()` ?

**Réponse :** Rappelez-vous que _portée lexicale_ signifie _espace de définition_ — et non _espace d'invocation_. Par conséquent, la portée lexicale de `myName` est la _portée globale_ car nous avons défini `myName` dans l'environnement global.

### Un autre exemple de portée lexicale

```js
function getName() {
  const myName = "Oluwatobi";
  return myName;
}
```

**Question :** Où se trouve la portée lexicale de `myName` ?

**Réponse :** Remarquez que nous avons créé et appelé `myName` dans `getName()`. Par conséquent, la portée lexicale de `myName` est l'environnement local de `getName()` car `getName()` est l'espace de définition de `myName`.

## Comment fonctionne la portée lexicale ?

L'environnement de définition d'une expression JavaScript détermine le [code](https://www.codesweetly.com/document-vs-data-vs-code/) autorisé à y accéder.

En d'autres termes, seul le code dans la portée lexicale d'un élément peut y accéder.

Par exemple, considérons le code ci-dessous :

```js
// Définir une fonction :
function showLastName() {
  const lastName = "Sofela";
  return lastName;
}

// Définir une autre fonction :
function displayFullName() {
  const fullName = "Oluwatobi " + lastName;
  return fullName;
}

// Invoquer displayFullName() :
console.log(displayFullName());

// L'invocation ci-dessus retournera :
Uncaught ReferenceError: lastName is not defined
```

Remarquez que l'invocation de `displayFullName()` dans l'extrait ci-dessus a retourné une `Uncaught ReferenceError`. L'erreur est retournée car seul le code dans la portée lexicale d'un élément peut accéder à cet élément.

Par conséquent, ni la fonction `displayFullName()` ni son code interne ne peuvent accéder à la variable `lastName` car `lastName` a été définie dans une portée différente.

En d'autres termes, la portée lexicale de `lastName` est différente de celle de `displayFullName()`.

L'espace de définition de `lastName` est `showLastName()` tandis que la portée lexicale de `displayFullName()` est l'environnement global.

Maintenant, considérons ce autre code ci-dessous :

```js
function showLastName() {
  const lastName = "Sofela";
  return lastName;
}

// Définir une autre fonction :
function displayFullName() {
  const fullName = "Oluwatobi " + showLastName();
  return fullName;
}

// Invoquer displayFullName() :
console.log(displayFullName());

// L'invocation ci-dessus retournera :
"Oluwatobi Sofela"
```

Dans l'extrait ci-dessus, `displayFullName()` a retourné avec succès `"Oluwatobi Sofela"` car `displayFullName()` et `showLastName()` sont dans la même portée lexicale.

En d'autres termes, `displayFullName()` a pu invoquer `showLastName()` car les deux fonctions sont définies dans la portée globale.

**Note :**

* Dans l'exemple 2 ci-dessus, `displayFullName()` n'a pas obtenu l'accès à la variable `lastName` de `showLastName()`. Au lieu de cela, `displayFullName()` a invoqué `showLastName()` — qui a ensuite retourné le contenu de sa variable `lastName`.
* Une alternative à la portée lexicale est la [portée dynamique](https://en.wikipedia.org/wiki/Scope_(computer_science)#Lexical_scope_vs._dynamic_scope_2) — mais elle est rarement utilisée en programmation. Seules quelques langues, comme bash, utilisent la portée dynamique.

## Conclusion

Chaque fois que vous entendez le mot lexical, pensez définition.

Ainsi, la portée lexicale d'une voiture, d'une variable, d'un téléphone, d'une fonction ou d'un maillot de bain fait référence à sa région de définition.

## Aperçu

Cet article a discuté de ce que signifie la portée lexicale en [JavaScript](https://www.codesweetly.com/html-css-javascript/). Nous avons également examiné pourquoi c'est un concept de programmation important.

Merci d'avoir lu !