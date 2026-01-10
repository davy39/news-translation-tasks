---
title: Comment mettre en majuscule la première lettre de chaque mot dans une phrase
  en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-06T12:11:28.000Z'
originalURL: https://freecodecamp.org/news/title-case-a-sentence-in-javascript-929012c88574
coverImage: https://cdn-media-1.freecodecamp.org/images/1*opgaEHfHpqV67c5Lu3j1Bw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment mettre en majuscule la première lettre de chaque mot dans une phrase
  en JavaScript
seo_desc: 'By Dylan Attal

  Remember in grade school when your teachers showed you how to properly write a paper?
  The first thing you start with is a good title, and every good title is properly
  capitalized.

  During this algorithm scripting challenge, we’ll learn ...'
---

Par Dylan Attal

Vous souvenez-vous à l'école primaire lorsque vos enseignants vous montraient comment rédiger correctement une dissertation ? La première chose à faire est un bon titre, et chaque bon titre est correctement capitalisé.

Lors de ce défi algorithmique, nous allons apprendre comment mettre en majuscule la première lettre de chaque mot dans une phrase en JavaScript. En fin de compte, nous allons faire en sorte que notre algorithme prenne une phrase et capitalise la première lettre de chaque mot comme s'il s'agissait du titre d'une dissertation.

#### Instructions de l'algorithme

> Retournez la chaîne fournie avec la première lettre de chaque mot en majuscule. Assurez-vous que le reste du mot est en minuscule.

> Pour les besoins de cet exercice, vous devez également capitaliser les mots de liaison comme « the » et « of ».

#### Cas de test fournis

* `titleCase("I'm a little tea pot")` doit retourner une chaîne.
* `titleCase("I'm a little tea pot")` doit retourner `I'm A Little Tea Pot`.
* `titleCase("sHoRt AnD sToUt")` doit retourner `Short And Stout`.
* `titleCase("HERE IS MY HANDLE HERE IS MY SPOUT")` doit retourner `Here Is My Handle Here Is My Spout`.

### Solution #1 : .map( ) et .slice( )

#### PEDAC

**Comprendre le problème** : Nous avons une entrée, une chaîne de caractères. Notre sortie est également une chaîne de caractères. En fin de compte, nous voulons retourner la chaîne d'entrée avec la première lettre — et seulement la première lettre — de chaque mot en majuscule.

**Exemples/Cas de test** : Nos cas de test fournis montrent que nous devons avoir une lettre majuscule uniquement au début de chaque mot. Nous devons mettre le reste en minuscule. Les cas de test fournis montrent également que nous n'avons pas à gérer des mots composés bizarres séparés par des symboles au lieu d'espaces. C'est une bonne nouvelle pour nous !

**Structure de données** : Nous allons devoir transformer notre chaîne d'entrée en un tableau afin de manipuler chaque mot séparément.

Quelques notes sur les méthodes que nous allons utiliser :

Parlons de `[.map()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)` :

`.map()` crée un nouveau tableau avec les résultats de l'appel d'une fonction sur chaque élément du tableau.

En d'autres termes, `.map()` nous permet de manipuler chaque élément d'un tableau avec une fonction, puis de retourner un nouveau tableau avec les résultats de notre manipulation. La fonction peut cibler à la fois la valeur actuelle et l'index de cette valeur actuelle, comme suit :

```
array.map((currentValue, Index) => {  // manipuler la currentValue d'une certaine manière})
```

Nous n'avons pas toujours besoin d'utiliser l'Index. Il y aura des fois, cependant, où nous devrons cibler des éléments d'un tableau par leur index, donc c'est utile à garder à l'esprit.

Voyons maintenant un exemple de `.map()` en action. Nous avons un tableau rempli de nombres et nous voulons multiplier chaque nombre par 2.

```
let arrayOfNumbers = [3, 6, 10, 42, 98]arrayOfNumbers.map(number => number * 2)// retourne [6, 12, 20, 84, 196]
```

Maintenant, examinons `[.slice()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/slice)` :

`.slice()` extrait une section d'une chaîne et la retourne comme une nouvelle chaîne. Si vous appelez `.slice()` sur une chaîne sans lui passer d'informations supplémentaires, elle retournera la chaîne entière.

```
"Bastian".slice()// retourne "Bastian"
```

Nous avons la possibilité de passer à `.slice()` un beginIndex et un endIndex, comme suit :

```
.slice(beginIndex, endIndex)
```

Cela indique à `.slice()` où commencer la découpe et où la terminer. Gardez à l'esprit que les chaînes sont indexées à partir de zéro ! Donc si nous voulions retourner à partir de la lettre à l'index 2 de « Bastian » jusqu'à, mais sans inclure, la lettre à l'index 5 de « Bastian », nous pourrions faire ceci :

```
"Bastian".slice(2, 5)// retourne "sti"
```

Avec cela en tête, nous pouvons couper le début des mots et retourner le reste en passant uniquement un beginIndex, comme suit :

```
"Bastian".slice(3)// retourne "tian"
```

**Algorithme** :

1. Mettez toutes les lettres de `str` en minuscules.
2. Divisez la chaîne `str` en minuscules en un tableau, chaque mot étant un élément séparé dans le tableau.
3. Capitalisez la première lettre de chaque élément dans le tableau.
4. Joignez chaque élément du tableau en une seule chaîne, en séparant chaque mot par un espace.
5. Retournez la chaîne en cas de titre.

**Code** : Voir ci-dessous !

J'ai créé beaucoup de variables locales inutiles dans le code ci-dessus pour montrer l'effet de chaque méthode sur l'entrée. Ci-dessous, j'ai supprimé les variables locales, enchaîné toutes les méthodes ensemble et supprimé les commentaires.

### Solution #2 : regex

**Attention ! Regex n'est pas la meilleure solution pour les débutants. Les expressions régulières sont difficiles en elles-mêmes, et leur complexité est un grief courant pour de nombreux développeurs expérimentés.** Mais bon, je me sens aventureux en écrivant ceci, et j'aime me challenger pour mieux comprendre regex chaque fois que je le peux. Ce défi algorithmique se prête bien à regex, alors examinons-le et voyons si nous pouvons approfondir notre compréhension de regex !

#### PEDAC

**Comprendre le problème** : Nous avons une entrée, une chaîne de caractères. Notre sortie est également une chaîne de caractères. En fin de compte, nous voulons retourner la chaîne d'entrée avec la première lettre — et seulement la première lettre — de chaque mot en majuscule.

**Exemples/Cas de test** : Nos cas de test fournis montrent que nous devons avoir une lettre majuscule uniquement au début de chaque mot. Nous devons mettre le reste en minuscule. Les cas de test fournis montrent également que nous n'avons pas à gérer des mots composés bizarres séparés par des symboles au lieu d'espaces. C'est une bonne nouvelle pour nous !

**Structure de données** : Nous ne transformerons pas notre chaîne en tableau lors de l'utilisation d'expressions régulières. JavaScript dispose d'une méthode pratique `[.replace()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)` qui nous permet de cibler presque tout ce que nous voulons dans une chaîne et de le remplacer par autre chose. Nous utilisons des expressions régulières pour cibler ce que nous voulons remplacer.

Il y a tant de symboles utilisés dans les expressions régulières que je ne peux espérer donner un aperçu général ici. Je peux cependant vous diriger vers cette [feuille de triche](https://www.rexegg.com/regex-quickstart.html), que j'utilise chaque fois que je dois employer regex.

Ce que je peux faire, c'est vous dire que regex avec `.replace()` en JavaScript suit un modèle de base. `.replace()` prend deux arguments : un motif (généralement une expression régulière) et un remplacement (peut être une chaîne ou une fonction).

```
string.replace(regex, function)
```

Dans notre solution, nous allons remplacer la lettre au début de chaque mot. Comment faire en sorte que regex fasse cela pour nous ? Nous disons à `.replace()` de correspondre à n'importe quel caractère suivant un espace ou correspondant au premier caractère de toute la chaîne (car le tout premier mot de la chaîne n'a pas d'espace avant lui).

Décomposons la partie regex de notre solution. Pour cela, regardons le premier argument de la fonction `.replace()`. Il s'agit du code regex qui détermine quel motif nous cherchons à correspondre et à remplacer.

```
// solution complète :
```

```
function titleCase(str) {  return str.toLowerCase().replace(/(^|\s)\S/g,  (firstLetter) => firstLetter.toUpperCase());}
```

Nous voulons finalement trouver tous les caractères non-espace, ce qui est représenté par `\S`.

Ensuite, nous voulons spécifier que nous voulons correspondre à ces caractères non-espace au début d'une chaîne `^` ou `|` après n'importe quel caractère d'espace `\s`.

Nous ajoutons le modificateur global `g` pour rechercher et remplacer tous ces motifs dans toute la chaîne.

**Algorithme** :

1. Mettez toutes les lettres de `str` en minuscules.
2. Remplacez la première lettre de chaque mot dans la chaîne par la lettre majuscule.
3. Retournez la chaîne en cas de titre.

**Code** : Voir ci-dessous !

Si vous avez d'autres solutions et/ou suggestions, n'hésitez pas à les partager dans les commentaires !

#### Cet article fait partie de la série [freeCodeCamp Algorithm Scripting](https://medium.com/@DylanAttal/freecodecamp-algorithm-scripting-b96227b7f837).

#### Cet article référence [freeCodeCamp Basic Algorithm Scripting: Title Case a Sentence](https://learn.freecodecamp.org/javascript-algorithms-and-data-structures/basic-algorithm-scripting/title-case-a-sentence)

Vous pouvez me suivre sur [Medium](https://medium.com/@DylanAttal), [LinkedIn](https://www.linkedin.com/in/dylanattal/), et [GitHub](https://github.com/DylanAttal) !