---
title: JavaScript replaceAll() – Remplacer toutes les instances d'une chaîne en JS
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-07-28T16:15:26.000Z'
originalURL: https://freecodecamp.org/news/javascript-replaceall-replace-all-instances-of-a-string-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/pexels-christina-morillo-1181675.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript replaceAll() – Remplacer toutes les instances d'une chaîne en
  JS
seo_desc: 'When working with a JavaScript program, you might need to replace a character
  or word with another one.

  Specifically, you may need to replace not just one but all occurrences of that character
  or word with something else.

  There are a few ways you can...'
---

Lorsque vous travaillez avec un programme JavaScript, vous pourriez avoir besoin de remplacer un caractère ou un mot par un autre.

Plus précisément, vous pourriez avoir besoin de remplacer non pas une, mais toutes les occurrences de ce caractère ou de ce mot par autre chose.

Il existe plusieurs façons d'y parvenir avec JavaScript. 💡

L'une des méthodes consiste à utiliser la méthode intégrée `replaceAll()`, que vous apprendrez à utiliser dans cet article.

Voici ce que nous allons couvrir :

1. [Qu'est-ce que `replaceAll()` en JavaScript ?](#heading-installation)
    1. [Syntaxe de `replaceAll()`](#syntaxe)
2. [`replaceAll()` avec une chaîne comme premier paramètre](#chaine-param)
3. [`replaceAll()` avec une expression régulière comme premier paramètre](#expression-reguliere)
4. [`replaceAll()` VS `replace()`](#differences)

## Qu'est-ce que `replaceAll()` en JavaScript ? <a name="heading-installation"></a>

La méthode `replaceAll()` fait partie de la bibliothèque standard de JavaScript. Lorsque vous l'utilisez, vous remplacez toutes les instances d'une chaîne.

Il existe différentes façons de remplacer toutes les instances d'une chaîne. Cela dit, utiliser `replaceAll()` est la manière la plus simple et la plus rapide de le faire.

Il est important de noter que cette fonctionnalité a été introduite avec ES2021. ✨

Bien que la méthode `replaceAll()` soit compatible avec tous les principaux navigateurs, ce n'est pas la meilleure solution lors du développement pour des versions plus anciennes de navigateurs, car ces versions plus anciennes pourraient ne pas être en mesure de la comprendre et de la supporter.

### La méthode `replaceAll()` - Analyse de la syntaxe <a name="syntaxe"></a>

La syntaxe générale de la méthode `replaceAll()` ressemble à ceci :

```
string.replaceAll(pattern, replacement)
```

Décomposons cela :

- `string` est la chaîne originale avec laquelle vous travaillez et la chaîne sur laquelle vous allez appeler la méthode `replaceAll()`.
- La méthode `replaceAll()` prend 2 paramètres :
- `pattern` est le premier paramètre, qui peut être une sous-chaîne ou une expression régulière - cela fait référence à l'élément que vous souhaitez changer et remplacer par autre chose.
    - Si `pattern` est une **expression régulière**, vous devez inclure le drapeau `g` (où `g` signifie `g`lobal) ou `replaceAll()` lèvera une exception - spécifiquement, l'erreur sera une `TypeError`.
- `replacement` est le deuxième paramètre, qui peut être une autre chaîne ou une fonction pour remplacer `pattern`.

Il est important de noter ici que la méthode `replaceAll()` ne modifie pas la chaîne originale. Au lieu de cela, elle retourne une nouvelle copie.

Toutes les instances du `pattern` spécifié seront remplacées par `replacement`.

## Comment utiliser `replaceAll()` avec une chaîne comme premier paramètre <a name="chaine-param"></a>

Plus tôt, vous avez vu que la méthode `replaceAll()` accepte deux paramètres - `pattern` comme premier paramètre et `replacement` comme deuxième.

Vous avez également vu que `pattern` peut être une chaîne ou une expression régulière.

Maintenant, voyons comment `replaceAll()` fonctionne lorsqu'il prend une **chaîne** comme premier paramètre.

Supposons que vous ayez l'exemple suivant :

```js
const my_string = "J'aime les chiens car les chiens sont adorables !";

let pattern = "chiens";
let replacement = "chats";

let my_new_string = my_string.replaceAll(pattern, replacement);
```

Je stocke le texte `J'aime les chiens car les chiens sont adorables !` dans une variable nommée `my_string`.

C'est la chaîne originale avec laquelle je travaille et je veux modifier une partie de son contenu.

Plus précisément, je veux changer la sous-chaîne `chiens`, qui apparaît *deux fois* dans la chaîne originale - ce sera mon `pattern`.

Je stocke cette sous-chaîne que je veux remplacer par autre chose dans une variable appelée `pattern`.

Je stocke ensuite la chaîne `chats` dans une variable appelée `replacement` - c'est la chaîne qui remplacera `chiens`.

J'appelle ensuite la méthode `replaceAll()` sur la chaîne originale, je passe les deux sous-chaînes comme paramètres, et je stocke ce résultat dans une variable nommée `my_new_string`.

```js
console.log(my_new_string);

// J'aime les chats car les chats sont adorables !
```

La méthode `replaceAll()` remplacera *toutes* les instances de la sous-chaîne `chiens` dans la chaîne `J'aime les chiens car les chiens sont adorables !` par `chats`.

La chaîne originale restera inchangée.

Il est important de noter ici que la substitution lors de l'utilisation d'une chaîne comme premier paramètre est sensible à la casse. Cela signifie que seule la chaîne avec la même casse qui correspond au `pattern` est remplacée.

```js
const my_string = "J'aime les Chiens car les chiens sont adorables !";

let pattern = "chiens";
let replacement = "chats";

let my_new_string = my_string.replaceAll(pattern, replacement);

console.log(my_new_string);
```

Dans l'exemple ci-dessus, il y a deux instances de `chiens`, mais la première a un `C` majuscule.

Comme vous pouvez le voir par la sortie, la substitution était sensible à la casse :

```
J'aime les Chiens car les chats sont adorables !
```

## Comment utiliser `replaceAll()` avec une expression régulière comme premier paramètre <a name="expression-reguliere"></a>

Comme vous l'avez vu précédemment, vous pouvez passer une expression régulière (également connue sous le nom de regex) comme premier paramètre.

Une expression régulière est une séquence de caractères qui crée un motif de recherche.

La syntaxe générale pour faire cela ressemble à ce qui suit :

```
string.replaceAll(/pattern/g, replacement)
```

Prenons l'exemple de la section précédente, et au lieu d'une chaîne, utilisons une expression régulière comme premier paramètre :

```js
const my_string = "J'aime les chiens car les chiens sont adorables !";

let pattern = /chiens/g;
let replacement = "chats";

let my_new_string = my_string.replaceAll(pattern, replacement);

console.log(my_new_string);

// sortie

// J'aime les chats car les chats sont adorables !
```

Lorsque vous utilisez une expression régulière comme premier paramètre, assurez-vous d'utiliser le drapeau `g`.

Si vous ne le faites pas, vous finirez par obtenir une erreur dans votre code :

```js
const my_string = "J'aime les chiens car les chiens sont adorables !";

let pattern = /chiens/;
let replacement = "chats";

let my_new_string = my_string.replaceAll(pattern, replacement);

console.log(my_new_string);

// sortie

// test.js:6 Uncaught TypeError: String.prototype.replaceAll appelé avec un argument RegExp non global
//    at String.replaceAll (<anonymous>)
//   at test.js:6:31
```

Modifions un peu la chaîne originale.

```js
const my_string = "J'aime les Chiens car les chiens sont adorables !";

let pattern = /chiens/g;
let replacement = "chats";

let my_new_string = my_string.replaceAll(pattern, replacement);

console.log(my_new_string);
```

J'ai maintenant deux instances de `chiens`, mais l'une d'elles est avec un `C` majuscule.

Je finis par obtenir la sortie suivante :

```
J'aime les Chiens car les chats sont adorables !
```

À partir de cette sortie, vous pouvez constater qu'il s'agit d'un remplacement sensible à la casse.

Pour le rendre insensible à la casse, assurez-vous d'ajouter le drapeau `i` après le drapeau `g` comme suit :

```js
const my_string = "J'aime les Chiens car les chiens sont adorables !";

let pattern = /chiens/gi;
let replacement = "chats";

let my_new_string = my_string.replaceAll(pattern, replacement);

console.log(my_new_string);

// sortie

// J'aime les chats car les chats sont adorables !
```

L'expression régulière `/chiens/gi` correspondra à toutes les instances qui contiennent cette sous-chaîne et rendra le remplacement insensible à la casse.

## La méthode `replaceAll()` vs la méthode `replace()` - Quelle est la différence ? <a name="differences"></a>

La différence entre les méthodes `replaceAll()` et `replace()` est que `replaceAll()` effectue une substitution globale dès la sortie de la boîte.

La méthode `replaceAll()` substituera *toutes* les instances de la chaîne ou du motif d'expression régulière que vous spécifiez, alors que la méthode `replace()` ne remplacera que la *première* occurrence.

Voici comment `replace()` fonctionne avec une chaîne comme premier paramètre :

```js
const my_string = "J'aime les chiens car les chiens sont adorables !";

let pattern = "chiens";
let replacement = "chats";

let my_new_string = my_string.replace(pattern, replacement);

console.log(my_new_string);

// sortie
// J'aime les chats car les chiens sont adorables !
```

Et voici comment `replace()` fonctionne avec une expression régulière comme premier paramètre :

```js
const my_string = "J'aime les chiens car les chiens sont adorables !";

let pattern = /chiens/;
let replacement = "chats";

let my_new_string = my_string.replace(pattern, replacement);

console.log(my_new_string);

// sortie
// J'aime les chats car les chiens sont adorables !
```

La seule façon d'effectuer une substitution globale avec la méthode `replace()` est d'utiliser une expression régulière avec le drapeau `g` :

```js
const my_string = "J'aime les chiens car les chiens sont adorables !";

let pattern = /chiens/g;
let replacement = "chats";

let my_new_string = my_string.replace(pattern, replacement);

console.log(my_new_string);

// sortie

// J'aime les chats car les chats sont adorables !
```

## Conclusion

Et voilà ! Vous savez maintenant comment fonctionne la méthode `replaceAll()` et quelques façons de l'utiliser.

Pour en savoir plus sur JavaScript, rendez-vous sur la [Certification Algorithmes et Structures de Données JavaScript](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/) de freeCodeCamp.

C'est un programme gratuit, bien pensé et structuré où vous apprendrez de manière interactive. À la fin, vous construirez également 5 projets pour obtenir votre certification et consolider vos connaissances.

Merci d'avoir lu !