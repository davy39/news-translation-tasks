---
title: Comment déstructurer un tableau en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-05T14:38:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-destructure-an-array-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/code-1839406_1920.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
seo_title: Comment déstructurer un tableau en JavaScript
seo_desc: 'By Madison Kanna

  Array destructuring is an efficient way to extract multiple values from data that’s
  stored in an array.

  In this tutorial we’ll learn about array destructuring. We''ll go over examples
  to learn the ins and outs of how array destructuri...'
---

Par Madison Kanna

La déstructuration de tableau est une méthode efficace pour extraire plusieurs valeurs de données stockées dans un tableau.

Dans ce tutoriel, nous allons apprendre la déstructuration de tableau. Nous passerons en revue des exemples pour comprendre les tenants et aboutissants de son fonctionnement.

J'ai également créé une vidéo de ce tutoriel :

%[https://www.youtube.com/watch?v=x-ih5R5-DCc]

Commençons.

Ouvrons notre navigateur web, puis notre console JavaScript où nous écrirons notre code. Vous pouvez trouver des instructions pour ouvrir la console [ici](https://balsamiq.com/support/faqs/browserconsole/).

## Comment déstructurer des éléments d'un tableau

Créons un tableau appelé `animals` et ajoutons les valeurs `dog`, `cat` et `horse`.

```javascript
const animals = ['Dog', 'Cat', 'Horse']
```

Supposons que nous voulons créer une variable avec uniquement la valeur `dog`. Nous appellerons cette variable `dogVar`, abréviation de `dog variable`. Avant l'introduction de la déstructuration de tableau dans ES6, nous aurions fait ceci :

```javascript
dogVar = animals[0]
```

Supposons ensuite que nous voulons également les valeurs `cat` et `horse` dans leurs propres variables. Nous aurions écrit :

```javascript
const catVar = animals[1]

const horseVar = animals[2]
```

Ici, nous avons écrit 3 lignes de code distinctes. Utilisons plutôt la déstructuration de tableau et écrivons 1 ligne de code au lieu de 3.

## Comment fonctionne la déstructuration

Avec la déstructuration de tableau, nous pourrions écrire une seule ligne de code :

```javascript
const [firstElement, secondElement, thirdElement] = animals
```

Cela ressemble à la création d'un tableau, mais ce n'est pas le cas. Nous **déstructurons** ce tableau. La déstructuration permet de déballer les valeurs des tableaux dans des variables distinctes.

La déstructuration prend chaque variable du tableau du côté gauche et la mappe à l'élément du **même index** dans le tableau `animals`.

Lorsque nous écrivons `firstElement`, nous disons que nous voulons accéder au premier élément du tableau `animals` et l'**assigner** à la variable `firstElement`.

Avec `secondElement`, nous disons que nous voulons accéder au deuxième élément du tableau et l'assigner à la variable `secondElement`. Il en va de même pour la variable `thirdElement`.

Le point clé ici est que ces noms `[firstElement, secondElement, thirdElement]` n'ont pas d'importance. Ce qui compte, c'est l'ordre.

En regardant l'**ordre** de notre déstructuration, nous savons quels éléments du tableau sont assignés à quelles variables.

Regardons notre ligne de code où nous déstructurons le tableau. Imaginons que cette partie `[firstElement, secondElement, thirdElement]` soit un tableau.

Si c'était un tableau, `firstElement` serait à la position `0` du tableau. JavaScript verra que cette variable `firstElement` est à la position `0`, puis ira dans le tableau `animals` et trouvera l'élément à la position `0`, et assignera cet élément à la variable `firstElement`.

(Gardez à l'esprit que les tableaux sont indexés à partir de zéro, ce qui signifie simplement que nous commençons à les compter à partir de 0 au lieu de 1.)

Lors de la déstructuration, nous pouvons donner à nos variables n'importe quel nom. Encore une fois, l'ordre est ce qui compte, pas le nom. Si nous le voulions, nous pourrions écrire :

```javascript
const [dog, cat, horse] = animals
```

Maintenant, nous avons toutes nos valeurs. Si nous écrivons `dog`, `cat`, `horse`, nous voyons que nous obtenons tous les noms de variables avec les valeurs correctes :

```javascript
dog // retourne 'Dog'

cat // retourne 'Cat'

horse // retourne 'Horse'
```

Si nous revenons à notre code au début de cet exemple, nous avions 3 lignes de code pour créer des variables pour `dog`, `cat` et `horse`. Avec la déstructuration de tableau, nous utilisons une seule ligne de code. La déstructuration est simplement un raccourci. C'est un moyen facile et rapide d'extraire plusieurs valeurs d'un tableau.

Mais que faire si vous ne voulez obtenir qu'un seul élément d'un tableau, par exemple le deuxième ou troisième élément, et stocker cet élément dans une variable ?

## Comment déstructurer le deuxième ou troisième élément d'un tableau

Supposons que nous avons un tableau, `fruits` :

```javascript
const fruits = ['banana', 'apple', 'orange']
```

Que faire si nous voulons obtenir uniquement la valeur `apple` et l'assigner à la variable `apple` ?

Nous ne pouvons pas simplement faire `const [apple] = fruits`. Pourquoi ? Si nous le faisons, la variable `apple` aura incorrectement la valeur `'banana'`. Pourquoi cela ?

C'est parce que, encore une fois, l'ordre compte. Avec `const [apple] = fruits`, JavaScript regarde `apple`, voit qu'il est à la position `0`, puis trouve l'élément à la position 0 dans le tableau `fruits`, qui est `'banana'`, et assigne cet élément à la variable `apple`.

Nous ne voulons pas que cela se produise. Que faire alors ?

Au lieu de cela, nous pouvons écrire : `const [, apple] = fruits`

Cette virgule agit comme une sorte de placeholder. Cette virgule indique à JavaScript de se comporter comme si un premier élément était présent, et donc cette variable `apple` est maintenant le deuxième élément ici. En d'autres termes, `apple` est maintenant à la position `1`.

Supposons que nous voulions uniquement la valeur `orange` dans une variable, et que nous ne nous soucions pas des éléments `apple` ou `banana`. Nous pourrions à nouveau utiliser des virgules comme suit :

```javascript
const [, , orange] = fruits
```

Si nous écrivons `orange` dans notre console, nous voyons que nous avons réussi à créer la variable `orange` et qu'elle a la valeur `'orange'`.

Une dernière chose à noter est que si vous apprenez React, vous utiliserez probablement souvent la déstructuration de tableau avec les hooks React. Par exemple, vous pourriez voir quelque chose comme ceci :

```javascript
const [count, setCount] = useState(0)
```

Nous avons appris tout ce qu'il y a à savoir sur la déstructuration de tableau.

Merci d'avoir lu !

Si vous avez aimé cet article, **rejoignez mon [coding club](https://madisonkanna.us14.list-manage.com/subscribe/post?u=323fd92759e9e0b8d4083d008&id=033dfeb98f)**, où nous relevons des défis de codage ensemble chaque dimanche et nous soutenons mutuellement dans l'apprentissage de nouvelles technologies.

Si vous avez des commentaires ou des questions sur cet article, ou trouvez-moi sur Twitter [@madisonkanna](https://twitter.com/Madisonkanna).