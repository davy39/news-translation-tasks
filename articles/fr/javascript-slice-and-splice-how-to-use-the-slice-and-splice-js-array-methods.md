---
title: Comment utiliser les méthodes slice() et splice() des tableaux JavaScript
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-04-13T19:17:33.000Z'
originalURL: https://freecodecamp.org/news/javascript-slice-and-splice-how-to-use-the-slice-and-splice-js-array-methods
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pankaj-patel-1IW4HQuauSU-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser les méthodes slice() et splice() des tableaux JavaScript
seo_desc: "When you are first learning JavaScript, it might be difficult to know the\
  \ difference between the slice() and splice() array methods. \nIn this article,\
  \ I will walk you through how to use the slice() and splice() array methods using\
  \ code examples. \nHow..."
---

Lorsque vous commencez à apprendre JavaScript, il peut être difficile de connaître la différence entre les méthodes de tableau `slice()` et `splice()`.

Dans cet article, je vais vous expliquer comment utiliser les méthodes de tableau `slice()` et `splice()` à l'aide d'exemples de code.

## Comment utiliser la méthode slice() des tableaux JavaScript

La méthode `slice()` peut être utilisée pour créer une copie d'un tableau ou retourner une portion d'un tableau. Il est important de noter que la méthode `slice()` ne modifie pas le tableau original mais crée plutôt une copie superficielle.

Voici la syntaxe de base :

```js
slice(paramètre de début optionnel, paramètre de fin optionnel)
```

Examinons quelques exemples pour mieux comprendre comment fonctionne la méthode `slice()`.

## Comment utiliser la méthode slice() JavaScript sans les paramètres de début et de fin

Dans cet premier exemple, j'ai créé une liste de villes du monde entier.

```js
const cities = ["Tokyo","Cairo","Los Angeles","Paris","Seattle"];
```

Je peux utiliser la méthode `slice()` pour créer une copie superficielle de ce tableau.

```js
cities.slice()
```

Lorsque je `console.log` le résultat, je verrai tous les éléments de mon tableau `cities` copiés dans ce nouveau tableau.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-12-at-11.28.42-PM.png)

## Comment utiliser la méthode slice() JavaScript en utilisant le paramètre de début

Vous pouvez utiliser le paramètre de début optionnel pour définir une position de départ pour la sélection d'éléments dans le tableau. Il est important de se rappeler que les tableaux sont indexés à partir de zéro.

Dans cet exemple, nous allons définir la position de départ à l'index 2, ce qui sélectionnera les trois dernières villes du tableau et les retournera dans un nouveau tableau.

```js
const newCityArr = cities.slice(2);

console.log(newCityArr)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-12-at-11.34.10-PM.png)

Le tableau original n'a pas été modifié, comme nous pouvons le voir dans cet exemple.

```js
const cities = ["Tokyo","Cairo","Los Angeles","Paris","Seattle"];

const newCityArr = cities.slice(2);

console.log("Original: ", cities)
console.log("Nouveau: ", newCityArr)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-12-at-11.36.59-PM.png)

Vous pouvez également utiliser des index négatifs qui commenceront à extraire des éléments à partir de la fin du tableau.

Dans cet exemple, nous allons définir la position de départ à -2, ce qui sélectionnera les deux dernières villes du tableau et les retournera dans un nouveau tableau.

```js
const newCityArr = cities.slice(-2);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-12-at-11.43.34-PM.png)

Si le paramètre de début est supérieur au dernier index du tableau, alors un tableau vide sera retourné.

```js
const newCityArr = cities.slice(5);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-12-at-11.45.41-PM.png)

## Comment utiliser la méthode slice() JavaScript en utilisant les paramètres de début et de fin

Si une position de fin est spécifiée, alors la méthode `slice()` extraira les éléments de la position de début jusqu'à la position de fin. La position de fin ne sera pas incluse dans les éléments extraits pour le nouveau tableau.

Dans cet exemple, nous avons spécifié un index de début de 2 et un index de fin de 4. Le nouveau tableau retourné n'inclura que les villes aux index 2 et 3 car la position de fin n'est pas incluse dans les éléments extraits.

```js
const cities = ["Tokyo","Cairo","Los Angeles","Paris","Seattle"];

const newCityArr = cities.slice(2,4);
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-12-at-11.51.30-PM.png)

## Comment utiliser la méthode splice() des tableaux JavaScript

Contrairement à la méthode `slice()`, la méthode `splice()` modifiera le contenu du tableau original. La méthode `splice()` est utilisée pour ajouter ou supprimer des éléments d'un tableau existant et la valeur de retour sera les éléments supprimés du tableau.

Si rien n'a été supprimé du tableau, alors la valeur de retour sera simplement un tableau vide.

Voici la syntaxe de base.

```js
splice(début, compte de suppression optionnel, éléments à ajouter optionnels)
```

Dans cet exemple, nous avons un tableau d'éléments alimentaires.

```js
const food = ['pizza', 'cake', 'salad', 'cookie'];
```

Si nous voulions ajouter un autre élément alimentaire au tableau à l'index 1, alors nous pouvons utiliser le code suivant :

```js
food.splice(1,0,"burrito")
```

Le premier nombre est l'index de départ, et le deuxième nombre est le compte de suppression. Puisque nous ne supprimons aucun élément, notre compte de suppression est zéro.

Voici à quoi ressemblerait le résultat dans la console.

```js
const food = ['pizza', 'cake', 'salad', 'cookie'];

food.splice(1,0,"burrito")

console.log(food)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-13-at-12.09.13-AM.png)

Si nous `console.log(food.splice(1,0,"burrito"))`, alors nous obtiendrions un tableau vide car rien n'a été supprimé de notre tableau.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-13-at-12.11.34-AM.png)

Dans cet exemple suivant, nous voulons supprimer "salad" du tableau. Nous pouvons utiliser les paramètres de début et de suppression pour y parvenir.

```js
food.splice(2,1)
```

Le nombre 2 est la position de départ et le nombre 1 représente le compte de suppression. Puisque salad est à l'index 2, il sera supprimé du tableau.

Voici à quoi ressemble notre tableau maintenant :

```js
const food = ['pizza', 'cake', 'salad', 'cookie'];

food.splice(2,1)
console.log(food)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-13-at-12.21.53-AM.png)

## Conclusion

Les méthodes de tableau `slice` et `splice` peuvent sembler similaires, mais il existe quelques différences clés.

La méthode `slice()` peut être utilisée pour créer une copie d'un tableau ou retourner une portion d'un tableau. Il est important de noter que la méthode `slice()` ne modifie pas le tableau original mais crée plutôt une copie superficielle.

Voici la syntaxe de base :

```js
slice(paramètre de début optionnel, paramètre de fin optionnel)
```

Contrairement à la méthode `slice()`, la méthode `splice()` modifiera le contenu du tableau original. La méthode `splice()` est utilisée pour ajouter ou supprimer des éléments d'un tableau existant et la valeur de retour sera les éléments supprimés du tableau.

Si rien n'a été supprimé du tableau, alors la valeur de retour sera simplement un tableau vide.

Voici la syntaxe de base :

```js
splice(début, compte de suppression optionnel, éléments à ajouter optionnels)
```

J'espère que vous avez apprécié cet article sur JavaScript et je vous souhaite bonne chance dans votre parcours de développeur.