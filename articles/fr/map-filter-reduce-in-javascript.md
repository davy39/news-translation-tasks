---
title: Comment utiliser map(), filter() et reduce() en JavaScript
subtitle: ''
author: Bhavesh Rawat
co_authors: []
series: null
date: '2022-10-03T22:06:51.000Z'
originalURL: https://freecodecamp.org/news/map-filter-reduce-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/fCC-blog-2.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser map(), filter() et reduce() en JavaScript
seo_desc: 'If you want to learn React, it''s important to get a fair understanding
  of some core JavaScript concepts first.

  So if that''s what you''re doing, first of all – great job! You have made a wise
  decision by not starting directly with React.

  Second, React ...'
---

Si vous voulez apprendre React, il est important de bien comprendre certains concepts fondamentaux de JavaScript au préalable.

Si c'est ce que vous faites, tout d'abord – excellent travail ! Vous avez pris une sage décision en ne commençant pas directement par React.

Ensuite, React s'appuie sur des concepts clés tels que les méthodes JavaScript map(), filter() et reduce() (après tout – React est une bibliothèque JavaScript). Cela fait de ces méthodes un apprentissage indispensable.

Map, filter et reduce sont trois des méthodes de tableau d'ordre supérieur les plus utiles et les plus puissantes. Dans ce tutoriel, vous verrez comment chacune de ces méthodes fonctionne. Vous apprendrez également où et comment les utiliser, à l'aide d'analogies et d'exemples. Ce sera amusant !

## Comment utiliser la méthode `map()`

Supposons que vous ayez un tableau `arrOne` dans lequel vous avez stocké des nombres, et que vous souhaitiez effectuer des calculs sur chacun d'eux. Mais vous ne voulez pas non plus **modifier le tableau d'origine**.

C'est là que `map()` entre en jeu. La méthode `map` vous aidera à faire ceci :

```javascript
let arrOne = [32, 45, 63, 36, 24, 11]
```

map() prend un maximum de trois arguments, qui sont la valeur/l'élément, l'index et le tableau.

```javascript
arrOne.map(value/element, index, array)
```

Disons que vous voulez multiplier chaque élément par 5 sans modifier le tableau d'origine.

Voici le code pour faire cela :

```js
let arrOne = [32, 45, 63, 36, 24, 11]
const multFive = (num) => {
return num * 5; // 'num' ici est la valeur du tableau.
}
let arrTwo = arrOne.map(multFive)
console.log(arrTwo)
```

Et voici le résultat :

```js
[ 160, 225, 315, 180, 120, 55 ]
```

Alors, que se passe-t-il ici ? Eh bien, j'ai un tableau `arrOne` avec 6 éléments. Ensuite, j'ai initialisé une fonction fléchée `multFive` avec 'num' comme argument. Elle renvoie le produit de `num` et 5, où la variable 'num' est alimentée par les données de la méthode map().

Si vous débutez avec les fonctions fléchées mais que vous connaissez les fonctions classiques, une fonction fléchée est identique à ceci :

```js
function(num) 
	{  
    	return num * 5;
    }
```

Ensuite, j'ai initialisé une autre variable `arrTwo` qui stockera le nouveau tableau que la méthode map() va créer.

Sur le côté droit, j'ai appelé la méthode map() sur le tableau 'arrOne'. Ainsi, la méthode map() va prendre chaque valeur de ce tableau en commençant par l'index[0] et effectuer le calcul souhaité sur chaque valeur. Ensuite, elle formera un nouveau tableau avec les valeurs calculées.

**Important** : Remarquez comment j'insiste sur le fait de ne pas modifier le tableau d'origine. C'est parce que cette propriété est ce qui différencie la méthode map() de la méthode 'forEach()'. La méthode map() crée un nouveau tableau alors que la méthode 'forEach()' mute/modifie le tableau d'origine avec le tableau calculé.

## Comment utiliser la méthode `filter()`

Le nom est assez explicite, n'est-ce pas ? Vous utilisez cette méthode pour filtrer le tableau en fonction des conditions que vous fournissez. La méthode filter() crée également un nouveau tableau.

**Prenons un exemple** : Supposons que vous ayez un tableau `arrNum` et que ce tableau stocke un ensemble de nombres. Maintenant, vous aimeriez voir quels nombres peuvent être divisés par 3 et en faire un tableau séparé.

Voici le code pour faire cela :

```js
let arrNum = [15, 39, 20, 32, 30, 45, 22]
function divByFive(num) {
  return num % 3 == 0
}
let arrNewNum = arrNum.filter(divByFive)
console.log(arrNewNum)
```

Et voici le résultat :

```js
[ 15, 39, 30, 45 ]
```

Décomposons ce code. Ici, j'ai un tableau `arrNum` avec 7 éléments. Ensuite, j'ai initialisé une fonction `divByFive` avec 'num' comme argument. Elle renvoie vrai ou faux chaque fois qu'un nouveau 'num' est passé pour la comparaison, où la variable 'num' est alimentée par les données de la méthode filter().

Ensuite, j'ai initialisé une autre variable `arrNewNum` qui stockera le nouveau tableau que la méthode filter() va créer.

Sur le côté droit, j'ai appelé la méthode filter() sur le tableau `arrNum`. Ainsi, la méthode filter() va prendre chaque valeur de ce tableau en commençant par l'index[0] et effectuer l'opération sur chaque valeur. Ensuite, elle formera un nouveau tableau avec les valeurs calculées.

## Comment utiliser la méthode reduce()

Disons qu'on vous demande de trouver la somme de tous les éléments d'un tableau. Vous pourriez utiliser une boucle for ou la méthode forEach(), mais reduce est conçu pour ce genre de tâche.

La méthode `reduce()` réduit un tableau à une seule valeur en effectuant l'opération souhaitée sur les éléments collectivement.

Prenons l'exemple ci-dessus et utilisons reduce dessus :

```js
let arrNum = [15, 39, 20, 32, 30, 45, 22]
function sumOfEle(num, ind) {
  return num + ind;
}
let arrNum2 = arrNum.reduce(sumOfEle)
console.log(arrNum2)
```

Voici le résultat :

`203`

Tout est identique aux méthodes map() et filter() – mais ce qu'il est important de comprendre, c'est comment la méthode reduce fonctionne sous le capot.

Il n'y a pas une [syntaxe](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce#syntax) unique pour la méthode reduce(). Voyons la plus simple, elle vous donnera l'essentiel de toutes les façons d'utiliser reduce().

Voici un exemple de syntaxe pour `reduce()` :

```js
// En prenant le tableau ci-dessus comme exemple
let arrNum = [15, 39, 20, 32, 30, 45, 22]arr.reduce((a1, a2) => { 
 return a1 + a2
})
```

Regardez cette syntaxe. Ici, reduce prend deux arguments, `a1` et `a2`, où `a1` agit comme un accumulateur tandis que `a2` contient la valeur de l'index.

Maintenant, lors du premier passage, l'accumulateur est égal à zéro et `a2` contient le premier élément du tableau. Ce que fait reduce, c'est qu'il place dans l'accumulateur la valeur que contient a2 et passe à l'élément suivant. Après cela, la méthode reduce() effectue l'opération sur les deux opérandes. Dans ce cas, il s'agit d'une addition.

Donc, en gros, `a1` est l'accumulateur qui est actuellement à zéro et `a2` contient 15. Après le premier passage, l'accumulateur contient 15 et `a2` contient la valeur suivante qui est 39.

Soit, `0 + 15 = 15`

Maintenant, au deuxième passage, reduce place la valeur de `a2`, 39, dans l'accumulateur puis effectue l'opération sur les deux opérandes.

Soit, `15 + 39 = 54`

Maintenant, au troisième passage, l'accumulateur a une somme de 15 et 39, soit 54. `a2` contient maintenant 20, que la méthode reduce ajoute à l'accumulateur, ce qui donne `54 + 20 = 74`.

Ce processus continue jusqu'à la fin du tableau.

## Conclusion

Eh bien, c'est tout pour le moment ! J'espère que vous avez maintenant une bonne idée du fonctionnement de ces méthodes de tableau d'ordre supérieur. N'hésitez pas à partager si vous avez apprécié cette lecture et si vous l'avez trouvée utile.

Consultez mon dernier article [ici](https://medium.com/geekculture/5-reasons-why-you-should-invest-in-a-vpn-90e95e9524fe), et pour mon eBook sur Git, regardez [ici](https://bhaveshrawat.gumroad.com/l/lets-git-it-beginners-guide-to-git-bash-commands).