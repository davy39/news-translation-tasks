---
title: JavaScript Sort() – Comment utiliser la fonction de tri en JS
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2023-05-16T20:29:44.000Z'
originalURL: https://freecodecamp.org/news/how-does-the-javascript-sort-function-work
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/blog_header2.png
tags:
- name: JavaScript
  slug: javascript
seo_title: JavaScript Sort() – Comment utiliser la fonction de tri en JS
seo_desc: 'In this article I will explain how to use, and maximize the full potential
  of the sort() function.

  What is the sort() Function?

  The sort() function allows you to sort an array object by either the default sorting
  order, or by a custom sorting functio...'
---

Dans cet article, je vais expliquer comment utiliser et maximiser tout le potentiel de la fonction `sort()`.

## Qu'est-ce que la fonction `sort()` ?

La fonction `sort()` vous permet de trier un objet de tableau soit par l'ordre de tri par défaut, soit par une fonction de tri personnalisée.

Par défaut, elle trie les éléments du tableau dans l'ordre ascendant en fonction de leurs valeurs Unicode de chaîne. La fonction prend les entrées, les convertit en chaînes, puis les trie en utilisant les valeurs Unicode.

### Qu'est-ce qu'Unicode ?

Unicode est une norme qui fournit une valeur numérique unique (point de code) pour chaque caractère utilisé dans les systèmes d'écriture du monde entier. Il permet aux ordinateurs de représenter et de gérer divers langues, symboles et caractères de manière cohérente.

Alphabet latin anglais :

```
U+0041 à U+005A : Lettres majuscules latines (A-Z)
U+0061 à U+007A : Lettres minuscules latines (a-z)
```

Ainsi, par exemple, le mot "Apple" de l'alphabet latin (anglais) est représenté en Unicode comme suit :

**A :** U+0041 <br>
**p :** U+0070 <br>
**p :** U+0070 <br>
**l :** U+006C <br>
**e :** U+0065 <br>

### Comment `sort()` utilise-t-il ces caractères Unicode ?

La fonction sort() trie le tableau en appliquant un algorithme de tri. Cela pourrait être l'algorithme de tri à bulles, de tri rapide, de tri par tas ou de tri par fusion, par exemple (il y en a d'autres aussi).

Le choix de l'algorithme peut dépendre de facteurs tels que la taille du tableau, les types de données triés et les stratégies d'optimisation du moteur.

**Note :** Le terme "moteur" fait référence au moteur JavaScript, qui est un composant logiciel exécutant le code JavaScript. Il est responsable de l'interprétation et de l'exécution des programmes JavaScript.

Les moteurs JavaScript sont généralement implémentés dans le cadre des navigateurs web, des plateformes JavaScript côté serveur ou des environnements d'exécution JavaScript autonomes.

Parmi les algorithmes de tri mentionnés, l'algorithme le plus couramment utilisé pour trier les tableaux en JavaScript est généralement le tri rapide ou une variation du tri rapide.

Si vous souhaitez en savoir plus sur l'algorithme de tri rapide, vous pouvez consulter le [site W3Resource ici](https://www.w3resource.com/javascript-exercises/searching-and-sorting-algorithm/searching-and-sorting-algorithm-exercise-1.php)

## Comment utiliser la fonction `sort()` de JavaScript

D'accord, maintenant que nous avons une idée de ce que `sort()` fait sous le capot, voyons comment utiliser la fonction.

Pour utiliser la fonction, il suffit d'appeler `{array}.sort()`. Cela implémentera l'action de tri par défaut décrite ci-dessus.

```javascript
const characters = [
  "Nebula",
  "Thanos",
  "Star Lord",
  "Groot",
  "Rocket",
  "Drax",
  "Gamora",
];

const sortedArray = characters.sort();

// Output:
["Drax", "Gamora", "Groot", "Nebula", "Rocket", "Star Lord", "Thanos"];
```

Comme vous pouvez le voir, les noms des personnages ont été triés par ordre ascendant selon leur représentation Unicode.

Si nous voulions les avoir dans l'ordre alphabétique décroissant, nous pourrions enchaîner la fonction `reverse()`, inversant les éléments une fois qu'ils ont été triés.

```javascript
const characters = [
  "Nebula",
  "Thanos",
  "Star Lord",
  "Groot",
  "Rocket",
  "Drax",
  "Gamora",
];

const descending = characters.sort().reverse();
console.log(descending);

// Output:
["Thanos", "Star Lord", "Rocket", "Nebula", "Groot", "Gamora", "Drax"];
```

### Et pour le tri des nombres ?

Eh bien, essayons :

```javascript
const numbers = [9, 3, 12, 11, 40, 28, 5];

const sortedNumbers = numbers.sort();
console.log(sortedNumbers);

// Output:
[11, 12, 28, 3, 40, 5, 9];
```

Attendez une minute ! Ce n'est pas trié dans l'ordre attendu, n'est-ce pas ? Pourquoi pas ?

Eh bien, rappelez-vous quand j'ai dit que la méthode de tri par défaut utilise le tri des caractères Unicode, après conversion en chaîne ? Eh bien, c'est pourquoi. Les nombres sont convertis en leur équivalent de chaîne puis triés en fonction des valeurs Unicode.

En conséquence, tous les nombres '1' viennent avant tout le reste, donc il va trier '11' avant '3' et ainsi de suite.

Regardons les valeurs Unicode pour ceux-ci :

11 = U+0031 U+0031 </br>
12 = U+0031 U+0032 </br>
28 = U+0032 U+0038 </br>
3 = U+0033 </br>
40 = U+3034 U+0030</br>
5 = U+3035 </br>
9 = U+3039 </br>

Donc, espérons que vous pouvez voir que si nous trions en utilisant les caractères Unicode, 0031 < 0033. Donc chaque fois qu'il compare 1 avec 3, les nombres commençant par 1 seront poussés au début du tableau.

_"Eh bien, c'est ennuyeux"_ je vous entends dire. Ne vous inquiétez pas, il y a une solution : les fonctions de comparaison personnalisées.

## Comment utiliser une fonction de tri personnalisée

Comme mentionné ci-dessus, la fonction `sort()` peut également prendre un argument d'une fonction de comparaison personnalisée.

```javascript
sort(compareFn?: ((a: never, b: never) => number) | undefined): never[]

Fonction utilisée pour déterminer l'ordre des éléments. Elle est censée retourner une valeur négative si le premier argument est inférieur au second argument, zéro s'ils sont égaux, et une valeur positive sinon. Si elle est omise, les éléments sont triés dans l'ordre ascendant, selon l'ordre des caractères ASCII.

[11,2,22,1].sort((a, b) => a - b)

Trie un tableau en place. Cette méthode mute le tableau et retourne une référence au même tableau.
```

Alors, que signifie tout cela ?

La fonction de comparaison a certaines attentes. Elle s'attend à ce que vous retourniez des valeurs spécifiques :

* **-1** : si la valeur que vous comparez à gauche est inférieure à celle de droite.
* **0** : si la valeur que vous comparez à gauche est égale à celle de droite.
* **1** : si la valeur que vous comparez à gauche est supérieure à celle de droite.

Dans sa forme la plus simple, cela signifie que -1 déplace l'élément à gauche (avant la valeur de comparaison), 0 le maintient où il est, et 1 déplace l'élément à droite (après la valeur de comparaison).

Maintenant, regardons quelques exemples pour voir comment cela fonctionne.

En reprenant l'exemple précédent, si nous avons du mal à trier un tableau de nombres, nous pouvons corriger cela en utilisant notre fonction de comparaison personnalisée :

```javascript
const numberSortFn = (a, b) => {
  if (a < b) {
    return -1;
  } else if (a === b) {
    return 0;
  } else {
    return 1;
  }
};

const numbers = [9, 3, 12, 11, 40, 28, 5];
const sortedNumbers = numbers.sort(numberSortFn);
console.log(sortedNumbers);

// Output
[3, 5, 9, 11, 12, 28, 40];
```

Comme vous pouvez le voir, cela fonctionne maintenant comme nous l'attendions, avec les nombres triés dans l'ordre numérique ascendant. Alors pourquoi est-ce différent ? Parce que maintenant l'opérateur "inférieur à" compare les côtés gauche et droit en tant que nombres, plutôt qu'en tant que chaînes.

## Autres utilisations de la fonction de comparaison personnalisée

### Tri d'objets en fonction d'une propriété

Vous pouvez utiliser la fonction de comparaison personnalisée pour trier des objets en utilisant leurs propriétés. Ci-dessous un exemple de tri d'un tableau d'objets (livres) en fonction de leur année de publication.

```javascript
const books = [
  { title: "Book A", year: 2010 },
  { title: "Book B", year: 2005 },
  { title: "Book C", year: 2018 },
];

const booksSortedByYearAsc = books.sort((a, b) => a.year - b.year);
console.log(booksSortedByYearAsc);

// Output:
[
  { title: "Book B", year: 2005 },
  { title: "Book A", year: 2010 },
  { title: "Book C", year: 2018 },
];
```

Nous indiquons à la fonction de comparaison de comparer spécifiquement en fonction de la propriété `.year` lors de l'exécution de la comparaison.

### Tri en fonction du contenu de la chaîne

Allons un peu plus loin et disons que nous avons un groupe de participants à un séminaire, et que nous voulons tous les lister pour un registre. Mais nous voulons que tous les Docteurs soient listés en haut, car ce sont les conférenciers principaux.

Nous pouvons faire cela avec une fonction de comparaison personnalisée :

```javascript
const names = ["Mike Smith", "Dr. Johnson", "John Doe", "Dr. Williams"];

names.sort((a, b) => {
  if (a.startsWith("Dr.") && !b.startsWith("Dr.")) {
    return -1;
  } else if (!a.startsWith("Dr.") && b.startsWith("Dr.")) {
    return 1;
  } else {
    return a.localeCompare(b); // trier par ordre alphabétique
  }
});

console.log(names);

// Output:
["Dr. Johnson", "Dr. Williams", "John Doe", "Mike Smith"];
```

Ainsi, ci-dessus, nous indiquons que si la chaîne commence par "Dr" et que la valeur suivante ne commence pas par "Dr", elle doit passer avant la valeur de droite, et vice versa pour la deuxième instruction if.

Si aucune des valeurs de comparaison ne contient "Dr", alors la fonction utilisera la fonction `localCompare`. Cela revient essentiellement à la comparaison Unicode par défaut comme discuté précédemment dans cet article.

### Chaînes de nombres et de lettres

Supposons que vous souhaitiez trier un tableau contenant à la fois des nombres et des lettres. Vous voulez que les nombres apparaissent avant les lettres, et au sein de chaque groupe, vous voulez que les éléments soient triés numériquement et alphabétiquement, respectivement. Voici comment vous pouvez y parvenir :

```javascript
const items = ["b", "3", "a", "2", "c", "1"];

items.sort((a, b) => {
  const aIsNumber = !isNaN(a); // isNaN = is Not a Number
  const bIsNumber = !isNaN(b);

  if (aIsNumber && !bIsNumber) {
    return -1; // les nombres doivent être triés avant les lettres
  } else if (!aIsNumber && bIsNumber) {
    return 1; // les lettres doivent être triées après les nombres
  } else if (aIsNumber && bIsNumber) {
    return a - b; // trier les nombres numériquement
  } else {
    return a.localeCompare(b); // trier les lettres par ordre alphabétique
  }
});

console.log(items);

// Output
["1", "2", "3", "a", "b", "c"];
```

Tout d'abord, nous vérifions si chaque valeur est un nombre en nous attendant à ce que `isNaN` retourne false, car `isNaN()` retourne si la valeur n'est pas un nombre. Ainsi, en vérifiant si false est retourné, nous savons qu'il s'agit en fait d'un nombre.

Nous pouvons ensuite utiliser une logique intelligente pour déterminer l'ordre des choses.

- **a est un nombre, et b n'est PAS un nombre** = nous savons que le nombre doit venir en premier, donc nous pouvons retourner -1
- **a n'est PAS un nombre, et b est un nombre** = nous savons que la lettre doit être déplacée à droite, donc 1 est retourné.
- **les deux valeurs sont des nombres** = nous pouvons simplement soustraire b de a, retournant ainsi un nombre négatif, 0 ou positif. Cela indique quoi faire avec les valeurs en relation avec l'ordre.

Si aucune de ces conditions n'est vraie, nous trions simplement par valeurs Unicode à nouveau, car nous savons que les deux valeurs sont des chaînes par élimination.

### Tri par ordre décroissant

Plus tôt, nous avons utilisé la fonction `sort().reverse()` pour ordonner la liste des personnages. Nous pouvons également utiliser la fonction `sort(compareFn)` comme suit :

```javascript
const characters = [
  "Nebula",
  "Thanos",
  "Star Lord",
  "Groot",
  "Rocket",
  "Drax",
  "Gamora",
];

const sortedArray = characters.sort((a, b) => b.localeCompare(a));
console.log(sortedArray);

// Output:
["Thanos", "Star Lord", "Rocket", "Nebula", "Groot", "Gamora", "Drax"];
```

Attendez, ne comparons-nous pas normalement `a` à `b` ? Oui, si nous voulons l'ordre ascendant – mais dans ce cas, parce que nous voulons l'ordre décroissant, nous comparons `b` à `a`.

### Quels sont les impacts sur les performances ?

C'est quelque chose dont vous devez être conscient lors du tri des tableaux, mais cela peut vraiment dépendre, par exemple :

- quel moteur JS exécute le code
- la taille du tableau
- la complexité de la fonction personnalisée

**Différences de temps :**

Regardons un tableau composé de 100 mots triés dans l'ordre ascendant, en utilisant à la fois le `sort()` par défaut et les implémentations `sort(compareFn)`.

```

sort() => 1.812ms;
sort(compareFn) => 0.14ms
```

Cependant, si nous devions trier le même tableau dans l'ordre décroissant, nous obtenons les temps suivants :

```

sort().reverse() =>  1.764ms
sort(compareFn) => 7.77ms
```

Vous pouvez voir que l'enchaînement `sort().reverse()` est beaucoup plus rapide. Cela peut être dû au fait que nous effectuons un algorithme de tri simple qui a été optimisé par ECMAScript, puis exécutons une fonction d'inversion de base pour retourner dans l'ordre décroissant.

En comparaison, l'exécution d'une fonction personnalisée ajoute une couche de complexité au processus et un calcul supplémentaire.

Une différence de 6 ms peut sembler très petite (et ne vous méprenez pas, c'est toujours extrêmement rapide). Mais cela pourrait augmenter à mesure que la taille du tableau grandit.

En règle générale, je recommande d'utiliser la méthode `sort()` par défaut/intégrée lorsque vous le pouvez, car celle-ci a été optimisée, laissant les fonctions personnalisées pour des exigences plus complexes.

## Conclusion

Dans cet article, nous avons exploré :

- Ce qu'est la fonction `sort()`
- Un regard sous la surface sur son fonctionnement
- Les utilisations courantes de la fonction `sort()`
- Certaines utilisations plus élaborées de la fonction `sort()` pour mieux comprendre les nombreuses tâches que vous pouvez effectuer avec elle
- Certaines considérations lors du tri des tableaux

J'espère que vous avez trouvé cet article utile pour mieux comprendre la fonction `sort()` de JavaScript et à quel point elle peut être puissante.

N'hésitez pas à me suivre sur Twitter à [gWeaths](https://twitter.com/gweaths) si vous souhaitez savoir quand j'ai publié d'autres articles.