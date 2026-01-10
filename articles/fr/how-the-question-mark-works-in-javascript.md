---
title: Comment l'opérateur Point d'interrogation (?) fonctionne en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-03T17:13:24.000Z'
originalURL: https://freecodecamp.org/news/how-the-question-mark-works-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--5--1.png
tags:
- name: JavaScript
  slug: javascript
- name: js
  slug: js
- name: Web Development
  slug: web-development
seo_title: Comment l'opérateur Point d'interrogation (?) fonctionne en JavaScript
seo_desc: 'By Nishant Kumar

  The conditional or question mark operator, represented by a ?, is one of the most
  powerful features in JavaScript. The ? operator is used in conditional statements,
  and when paired with a :, can function as a compact alternative to i...'
---

Par Nishant Kumar

L'opérateur conditionnel ou point d'interrogation, représenté par un `?`, est l'une des fonctionnalités les plus puissantes en JavaScript. L'opérateur `?` est utilisé dans les instructions conditionnelles, et lorsqu'il est associé à un `:`, il peut fonctionner comme une alternative compacte aux instructions `if...else`.

Mais il y a plus à découvrir que ce qui est visible au premier abord. Il existe trois utilisations principales pour l'opérateur `?`, dont deux que vous n'avez peut-être pas utilisées ou même entendues. Apprenons-les toutes en détail.

## Trois utilisations principales du point d'interrogation (`?`) en JavaScript :

1. Opérateur Ternaire
2. Chaînage Optionnel
3. Fusion des Nuls

Nous allons examiner chacune de ces utilisations en détail, en commençant par la manière la plus courante d'utiliser l'opérateur `?` – en tant qu'opérateur ternaire.

## 1. Opérateur Ternaire

Le terme ternaire signifie composé de trois éléments ou parties. L'opérateur `?` est également appelé opérateur ternaire car, contrairement à d'autres opérateurs tels que l'égalité stricte (`===`) ou le reste (`%`), c'est le seul qui prend trois opérandes.

En commençant par `?`, nous ajoutons une condition du côté gauche et une valeur du côté droit à retourner lorsque la condition est vraie. Ensuite, nous ajoutons un deux-points (`:`) suivi d'une valeur à retourner si la condition est fausse.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--1-.png)

L'opérateur ternaire est essentiellement un raccourci pour une instruction `if...else` traditionnelle.

Comparons un opérateur ternaire avec une instruction `if...else` plus longue :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--22-.png)

Ici, l'opérateur ternaire n'occupe qu'une seule ligne de code, alors que le `if...else` en prend sept.

Utiliser un opérateur ternaire est beaucoup plus efficace, n'est-ce pas ?

## 2. Chaînage Optionnel

En 2020, une nouvelle fonctionnalité géniale connue sous le nom de Chaînage Optionnel a été introduite.

Pour comprendre comment cela fonctionne, imaginez ce scénario.

Supposons que vous avez du code qui appelle une propriété d'objet qui n'existe pas, ce qui déclenche une erreur à l'exécution. Cela peut être dû à une valeur manquante ou non définie dans votre base de données ou provenant d'une API :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--23--2.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-01-25-00-56-06.png)
_Une erreur courante – `TypeError: Cannot read property 'salary' of undefined`_

Grâce au Chaînage Optionnel, vous pouvez simplement insérer un `?` entre le nom de la propriété et la période entre la propriété suivante. 

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--24-.png)

Avec cela, il retournera simplement `undefined` au lieu de lancer une erreur disgraciée.

Le Chaînage Optionnel est vraiment une fonctionnalité qui change la vie pour les développeurs JavaScript. 

## 3. Fusion des Nuls

Dans certains cas, vous devez définir une valeur par défaut pour un nom ou une valeur de propriété manquante. 

Par exemple, supposons que nous créons une Application Météo dans laquelle nous récupérons la température, l'humidité, la vitesse du vent, la pression, l'heure du lever et du coucher du soleil, et l'image de la ville. Nous avons saisi un lieu, disons _Bangalore_, mais pour une raison quelconque, son image n'est pas dans la base de données.

Lorsque l'application récupère et affiche les données, l'image sera vide, ce qui peut sembler disgracié. Ce que nous pouvons faire, dans ce cas, c'est définir une image par défaut pour les villes qui n'ont pas d'image, Bangalore dans notre cas. 

De cette façon, lorsque l'application affiche les données, l'image par défaut sera présente pour les villes sans images.

Vous pouvez faire cela en utilisant l'opérateur `||`, connu sous le nom d'opérateur OU logique :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--4-.png)

Mais si vous utilisez `||` pour fournir une valeur par défaut, vous pouvez rencontrer des comportements inattendus si vous considérez certaines valeurs comme utilisables (par exemple, `''` ou `0`).

Considérez un scénario où une variable a la valeur de 0 ou une chaîne vide. Si nous utilisons (`||`), elle sera considérée comme non définie ou NULL et retournera une valeur par défaut que nous avons fixée.

Au lieu de l'opérateur OU logique (`||`), vous pouvez utiliser des doubles points d'interrogation (`??`), ou Fusion des Nuls. 

Apprenons avec un exemple.

```javascript
const value1 = 0 || 'default string';
console.log(value1);


const value2 = '' || 1000;
console.log(value2);
```

Ici, nous avons '0' et 'default string' dans la variable value1. Si nous enregistrons sa valeur dans la console, nous obtiendrons 'default string', ce qui est étrange. Au lieu de la chaîne par défaut, nous devrions obtenir 0, car zéro n'est pas non défini ou null. Donc, '`||`' échoue à faire le travail ici.

De même, c'est la même chose avec value2.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--25-.png)
_Sortie pour '`||`'_

```javascript
const value1 = 0 ?? 'default string';
console.log(value1);


const value2 = '' ?? 1000;
console.log(value2);
```

Mais si nous remplaçons '`||`' par '`??`', nous obtiendrons 0 et une chaîne vide, ce qui est vraiment cool.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Pink-Cute-Chic-Vintage-90s-Virtual-Trivia-Quiz-Presentations--26-.png)
_Sortie pour '`??`'_

La Fusion des Nuls fonctionne exactement comme l'opérateur OU logique, sauf que vous obtiendrez la valeur du côté droit lorsque la valeur du côté gauche est `undefined` ou `null`.

En d'autres termes, `??` n'autorise que les valeurs `undefined` et `null`, et non les chaînes vides (`''`) ou les `0`.

## Conclusion

Maintenant, espérons que vous comprenez comment l'opérateur `?` fonctionne en JavaScript. Il semble simple, mais c'est l'un des caractères les plus puissants du langage. Il fournit du sucre syntaxique de trois manières géniales mais différentes. 

Essayez-les et faites-moi savoir comment cela se passe.

Bon apprentissage !