---
title: Comment parcourir un tableau en JavaScript – Tutoriel JS Itération
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-06-23T19:55:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-loop-through-an-array-in-javascript-js-iterate-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/cover-template--3-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Loops
  slug: loops
seo_title: Comment parcourir un tableau en JavaScript – Tutoriel JS Itération
seo_desc: 'An array is a single variable used to store elements of different datatypes
  so that they can be accessed through a single variable.

  It is an ordered list of values, and each value is referred to as an element, which
  is specified by an index.

  Knowing ...'
---

Un tableau est une variable unique utilisée pour stocker des éléments de différents types de données afin qu'ils puissent être accessibles via une seule variable.

Il s'agit d'une liste ordonnée de valeurs, et chaque valeur est appelée un élément, qui est spécifié par un index.

Sachant que ces variables uniques contiennent une liste d'éléments, vous pourriez vouloir créer une liste de ces éléments afin de pouvoir effectuer des fonctions individuelles avec eux et bien plus encore. C'est là que la boucle entre en jeu.

### Voici un scrim interactif sur la façon de parcourir un tableau en JavaScript :

<iframe src="https://scrimba.com/scrim/co0844e78b1b48c6e5bc87da1?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="480"></iframe>

## Qu'est-ce que les boucles en JavaScript ?

Une boucle est un type de programme informatique qui nous permet de répéter une opération spécifique un nombre prédéterminé de fois sans avoir à écrire cette opération individuellement.

Par exemple, si nous avons un tableau et que nous voulons afficher chaque élément du tableau, plutôt que d'utiliser le numéro d'index pour le faire un par un, nous pouvons simplement parcourir et effectuer cette opération une fois.

Il existe de nombreuses méthodes pour parcourir un tableau en JavaScript. Dans cet article, nous allons passer en revue les plus couramment utilisées afin que vous puissiez apprendre différentes approches et comprendre comment elles fonctionnent.

Nous allons utiliser le tableau suivant pour cet article :

```js
const scores = [22, 54, 76, 92, 43, 33];
```

## Comment parcourir un tableau avec une boucle While en JavaScript

Vous pouvez utiliser une boucle `while` pour évaluer une condition qui est enfermée dans des parenthèses `()`. Si la condition est `true`, le code à l'intérieur de la boucle `while` est exécuté. Si elle est `false`, la boucle est terminée.

Si nous voulons parcourir un tableau, nous pouvons utiliser la propriété `length` pour spécifier que la boucle doit continuer jusqu'à ce que nous atteignions le dernier élément de notre tableau.

Utilisons maintenant la méthode de la boucle while pour parcourir le tableau :

```js
let i = 0;

while (i < scores.length) {
    console.log(scores[i]);
    i++;
}
```

Cela retournera chaque élément de notre tableau un après l'autre :

```bash
22
54
76
92
43
33
```

Dans la boucle ci-dessus, nous avons d'abord initialisé le numéro d'index pour qu'il commence par `0`. Ensuite, le numéro continuera à augmenter et à afficher chaque élément jusqu'à ce que la condition que nous avons définie retourne false, indiquant que nous avons atteint la fin du tableau. Lorsque `i = 6`, la condition ne sera plus exécutée car le dernier index du tableau est `5`.

## Comment parcourir un tableau avec une boucle `do...while` en JavaScript

La boucle `do...while` est presque identique à la boucle while, sauf qu'elle exécute le corps d'abord avant d'évaluer la condition pour les exécutions suivantes. Cela signifie que le corps de la boucle est toujours exécuté au moins une fois.

Effectuons la même boucle avec la boucle `do...while` pour voir comment elle fonctionne :

```bash
let i = 0;

do {
    console.log(scores[i]);
    i++;
} while (i < scores.length);
```

Cela retournera chaque élément de notre tableau :

```bash
22
54
76
92
43
33
```

Comme mentionné précédemment, cela s'exécutera toujours une fois avant d'évaluer toute condition définie. Par exemple, si nous définissons l'index `i` à `6` et qu'il n'est plus inférieur à `scores.length`, le corps de la boucle s'exécutera d'abord avant de vérifier la condition :

```js
let i = 6;

do {
    console.log(scores[i]);
    i++;
} while (i < scores.length);
```

Cela retournera un seul `undefined` car nous n'avons pas d'élément dans le tableau d'index `6`, mais comme vous pouvez le voir, il s'est exécuté une fois avant de s'arrêter.

## Comment parcourir un tableau avec une boucle for en JavaScript

La boucle `for` est une instruction itérative qui vérifie certaines conditions puis exécute un bloc de code de manière répétée tant que ces conditions sont remplies.

Nous n'avons pas besoin d'initialiser l'index d'abord lorsque nous utilisons la méthode de la boucle `for` car l'initialisation, la condition et l'itération sont toutes gérées dans les crochets, comme montré ci-dessous :

```js
for (let i = 0; i < scores.length; i++) {
    console.log(scores[i]);
}
```

Cela retournera tous les éléments comme les autres méthodes l'ont fait :

```bash
22
54
76
92
43
33
```

## Comment parcourir un tableau avec une boucle `for...in` en JavaScript

La boucle `for...in` est une manière plus facile de parcourir les tableaux car elle nous donne la clé que nous pouvons maintenant utiliser pour obtenir les valeurs de notre tableau de cette manière :

```js
for (i in scores) {
    console.log(scores[i]);
}
```

Cela affichera tous les éléments de notre tableau :

```bash
22
54
76
92
43
33
```

## Comment parcourir un tableau avec une boucle `for...of` en JavaScript

La boucle `for...of` itère sur des objets itérables tels que les tableaux, les ensembles, les cartes, les chaînes, etc. Elle a la même syntaxe que la boucle `for...in`, mais au lieu d'obtenir la `clé`, elle obtient l'élément lui-même.

C'est l'une des méthodes les plus faciles pour parcourir un tableau et a été introduite dans les versions ultérieures de JavaScript ES6.

```bash
for (score of scores) {
    console.log(score);
}
```

Cela obtient chaque élément de notre tableau et nous n'avons plus besoin d'utiliser l'index pour obtenir chaque élément de notre tableau :

```bash
22
54
76
92
43
33
```

## Comment parcourir un tableau avec une boucle `forEach` en JavaScript

La méthode de tableau `forEach()` parcourt n'importe quel tableau, exécutant une fonction fournie une fois pour chaque élément de tableau dans l'ordre croissant de l'index. Cette fonction est connue sous le nom de fonction de rappel.

C'est une méthode plus avancée qui peut faire beaucoup plus que simplement parcourir chaque élément, mais vous pouvez également l'utiliser pour parcourir de cette manière :

```js
scores.forEach((score) => {
    console.log(score);
});
```

Vous pouvez écrire cela en une ligne de cette manière :

```js
scores.forEach((score) => console.log(score));
```

Et cela nous donnera la même sortie que toutes les méthodes précédentes :

```bash
22
54
76
92
43
33
```

## Conclusion

Dans cet article, nous avons examiné six méthodes différentes/standards pour parcourir un tableau.

Il est crucial que vous compreniez toutes ces méthodes et que vous déterminiez ensuite quelle méthode est préférable pour vous, plus propre à utiliser et plus facile à lire.

Embarquez dans un voyage d'apprentissage ! [Parcourez 200+ articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part.