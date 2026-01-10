---
title: Comment mettre en majuscule la première lettre de chaque mot en JavaScript
  – un tutoriel JS sur les majuscules
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-26T17:24:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-capitalize-words-in-javascript
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9905740569d1a4ca1d64.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment mettre en majuscule la première lettre de chaque mot en JavaScript
  – un tutoriel JS sur les majuscules
seo_desc: 'By Catalin Pit

  In this article, you are going to learn how to capitalize the first letter of any
  word in JavaScript. After that, you are going to capitalize the first letter of
  all words from a sentence.

  The beautiful thing about programming is that ...'
---

Par Catalin Pit

Dans cet article, vous allez apprendre comment mettre en majuscule la première lettre de n'importe quel mot en JavaScript. Ensuite, vous allez mettre en majuscule la première lettre de tous les mots d'une phrase.

La belle chose à propos de la programmation, c'est qu'il n'y a pas une solution universelle pour résoudre un problème. Par conséquent, dans cet article, vous allez voir plusieurs façons de résoudre le même problème.

# Mettre en majuscule la première lettre d'un mot

Tout d'abord, commençons par mettre en majuscule la première lettre d'un seul mot. Une fois que vous aurez appris à faire cela, nous passerons au niveau suivant – le faire pour chaque mot d'une phrase. Voici un exemple :

```js
const publication = "freeCodeCamp";

```

En JavaScript, nous commençons à compter à partir de 0. Par exemple, si nous avons un tableau, la première position est 0, et non 1.

De plus, nous pouvons accéder à chaque lettre d'une chaîne de caractères de la même manière que nous accédons à un élément d'un tableau. Par exemple, la première lettre du mot "_freeCodeCamp_" est à la position 0.

Cela signifie que nous pouvons obtenir la lettre **f** de _freeCodeCamp_ en faisant `publication[0]`.

De la même manière, vous pouvez accéder à d'autres lettres du mot. Vous pouvez remplacer "0" par n'importe quel nombre, tant que vous ne dépassez pas la longueur du mot. En dépassant la longueur du mot, je veux dire essayer de faire quelque chose comme `publication[25]`, ce qui génère une erreur car il n'y a que douze lettres dans le mot "freeCodeCamp".

### Comment mettre en majuscule la première lettre

Maintenant que nous savons comment accéder à une lettre d'un mot, mettons-la en majuscule.

En JavaScript, nous avons une méthode appelée `toUpperCase()`, que nous pouvons appeler sur des chaînes de caractères ou des mots. Comme nous pouvons le déduire du nom, vous l'appelez sur une chaîne/un mot, et elle va retourner la même chose mais en majuscules.

Par exemple :

```js
const publication = "freeCodeCamp";
publication[0].toUpperCase();

```

En exécutant le code ci-dessus, vous allez obtenir un **F** majuscule au lieu de f. Pour obtenir le mot entier, nous pouvons faire ceci :

```js
const publication = "freeCodeCamp";
publication[0].toUpperCase() + publication.substring(1);

```

Maintenant, il concatène "F" avec "reeCodeCamp", ce qui signifie que nous obtenons le mot "FreeCodeCamp". C'est tout !

### Récapitulons

Pour être sûr que les choses sont claires, récapitulons ce que nous avons appris jusqu'à présent :

* En JavaScript, le comptage commence à partir de 0.
* Nous pouvons accéder à une lettre d'une chaîne de caractères de la même manière que nous accédons à un élément d'un tableau - par exemple `string[index]`.
* N'utilisez pas un index qui dépasse la longueur de la chaîne (utilisez la méthode length - `string.length` - pour trouver la plage que vous pouvez utiliser).
* Utilisez la méthode intégrée `toUpperCase()` sur la lettre que vous voulez transformer en majuscule.

# Mettre en majuscule la première lettre de chaque mot d'une chaîne de caractères

L'étape suivante consiste à prendre une phrase et à mettre en majuscule chaque mot de cette phrase. Prenons la phrase suivante :

```js
const mySentence = "freeCodeCamp is an awesome resource";

```

### Diviser en mots

Nous devons mettre en majuscule la première lettre de chaque mot de la phrase `freeCodeCamp is an awesome resource`.

La première étape que nous entreprenons est de diviser la phrase en un tableau de mots. **Pourquoi ?** Pour que nous puissions manipuler chaque mot individuellement. Nous pouvons faire cela comme suit :

```js
const mySentence = "freeCodeCamp is an awesome resource";
const words = mySentence.split(" ");

```

### Itérer sur chaque mot

Après avoir exécuté le code ci-dessus, la variable `words` est assignée à un tableau avec chaque mot de la phrase. Le tableau est le suivant `["freeCodeCamp", "is", "an", "awesome", "resource"]`.

```js
const mySentence = "freeCodeCamp is an awesome resource";
const words = mySentence.split(" ");

for (let i = 0; i < words.length; i++) {
    words[i] = words[i][0].toUpperCase() + words[i].substr(1);
}

```

Maintenant, l'étape suivante consiste à parcourir le tableau de mots et à mettre en majuscule la première lettre de chaque mot.

Dans le code ci-dessus, chaque mot est pris séparément. Ensuite, il met en majuscule la première lettre, et enfin, il concatène la première lettre en majuscule avec le reste de la chaîne.

### Joindre les mots

Que fait le code ci-dessus ? Il itère sur chaque mot et le remplace par la majuscule de la première lettre + le reste de la chaîne.

Si nous prenons "freeCodeCamp" comme exemple, cela ressemble à ceci `freeCodeCamp = F + reeCodeCamp`.

Après avoir itéré sur tous les mots, le tableau `words` est `["FreeCodeCamp", "Is", "An", "Awesome", "Resource"]`. Cependant, nous avons un tableau, et non une chaîne de caractères, ce qui n'est pas ce que nous voulons.

La dernière étape consiste à joindre tous les mots pour former une phrase. Alors, comment faisons-nous cela ?

En JavaScript, nous avons une méthode appelée `join`, que nous pouvons utiliser pour retourner un tableau sous forme de chaîne. La méthode prend un séparateur comme argument. C'est-à-dire que nous spécifions ce qu'il faut ajouter entre les mots, par exemple un espace.

```js
const mySentence = "freeCodeCamp is an awesome resource";
const words = mySentence.split(" ");

for (let i = 0; i < words.length; i++) {
    words[i] = words[i][0].toUpperCase() + words[i].substr(1);
}

words.join(" ");

```

Dans l'extrait de code ci-dessus, nous pouvons voir la méthode join en action. Nous l'appelons sur le tableau `words`, et nous spécifions le séparateur, qui dans notre cas est un espace.

Par conséquent, `["FreeCodeCamp", "Is", "An", "Awesome", "Resource"]` devient `FreeCodeCamp Is An Awesome Resource`.

# Autres méthodes

En programmation, il y a généralement plusieurs façons de résoudre le même problème. Alors, voyons une autre approche.

```js
const mySentence = "freeCodeCamp is an awesome resource";
const words = mySentence.split(" ");

words.map((word) => { 
    return word[0].toUpperCase() + word.substring(1); 
}).join(" ");

```

**Quelle est la différence entre la solution ci-dessus et la solution initiale ?** Les deux solutions sont très similaires, la différence étant que dans la deuxième solution, nous utilisons la fonction `map`, alors que dans la première solution, nous avons utilisé une boucle `for`.

Allons encore plus loin et essayons de faire une **solution en une ligne**. Attention ! Les solutions en une ligne peuvent sembler cool, mais dans le monde réel, elles sont rarement utilisées car il est difficile de les comprendre. La lisibilité du code passe toujours en premier.

```js
const mySentence = "freeCodeCamp is an awesome resource";

const finalSentence = mySentence.replace(/(^\w{1})|(\s+\w{1})/g, letter => letter.toUpperCase());

```

Le code ci-dessus utilise **RegEx** pour transformer les lettres. Le RegEx peut sembler confus, alors laissez-moi expliquer ce qui se passe :

* `^` correspond au début de la chaîne.
* `\w` correspond à n'importe quel caractère de mot.
* `{1}` ne prend que le premier caractère.
* Ainsi, `^\w{1}` correspond à la première lettre du mot.
* `|` fonctionne comme le booléen `OR`. Il correspond à l'expression avant et après le `|`.
* `\s+` correspond à n'importe quelle quantité d'espaces blancs entre les mots (par exemple, des espaces, des tabulations ou des sauts de ligne).

Ainsi, avec une seule ligne, nous avons accompli la même chose que nous avons accomplie dans les solutions ci-dessus. Si vous voulez jouer avec le RegEx et en apprendre davantage, vous pouvez utiliser [ce site web](https://regexr.com/).

# Conclusion

Félicitations, vous avez appris une nouvelle chose aujourd'hui ! Pour récapituler, dans cet article, vous avez appris comment :

* accéder aux caractères d'une chaîne
* mettre en majuscule la première lettre d'un mot
* diviser une chaîne en un tableau de mots
* joindre les mots d'un tableau pour former une chaîne
* utiliser RegEx pour accomplir la même tâche

Merci d'avoir lu ! Si vous voulez rester en contact, connectons-nous sur Twitter [@catalinmpit](https://twitter.com/intent/follow?screen_name=catalinmpit). Je publie également des articles régulièrement sur mon blog [catalins.tech](https://catalins.tech) si vous voulez lire plus de contenu de ma part.