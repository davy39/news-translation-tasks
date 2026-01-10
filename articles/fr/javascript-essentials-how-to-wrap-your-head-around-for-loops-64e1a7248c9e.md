---
title: 'Les essentiels de JavaScript : comment comprendre les boucles for'
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2017-12-13T17:04:02.000Z'
originalURL: https://freecodecamp.org/news/javascript-essentials-how-to-wrap-your-head-around-for-loops-64e1a7248c9e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TqBCXYI6enDiSuoVEOeVoA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Les essentiels de JavaScript : comment comprendre les boucles for'
seo_desc: 'Let’s say you want to run a function, bounceBall, four times. How would
  you do it? Like this?

  function bounceBall() {   // bounce the ball here }

  bounceBall() bounceBall() bounceBall() bounceBall()

  This approach is great if you need to bounceBall onl...'
---

Disons que vous voulez exécuter une fonction, `bounceBall`, quatre fois. Comment feriez-vous ? Comme ceci ?

```
function bounceBall() {   // faire rebondir la balle ici } 
```

```
bounceBall() bounceBall() bounceBall() bounceBall()
```

Cette approche est idéale si vous devez faire rebondir la balle seulement quelques fois. Que se passe-t-il si vous devez faire rebondir la balle cent fois ?

La meilleure façon est d'utiliser une boucle `for`.

### La boucle for

La boucle `for` exécute un bloc de code autant de fois que vous le souhaitez. Voici une boucle for qui exécute `bounceBall` dix fois :

```
for (let i = 0; i < 10; i++) {   bounceBall() }
```

Elle est divisée en quatre parties — l'`initialExpression`, la `condition`, l'`incrementalExpression`, et la `statement` :

```
for (initialExpression; condition; incrementExpression) {   statement }
```

Avant de boucler, vous devez avoir une **statement**. Cette statement est le bloc de code que vous souhaitez exécuter plusieurs fois. Vous pouvez écrire n'importe quel nombre de lignes de code ici. Vous pouvez même utiliser des fonctions.

Voici à quoi ressemble la boucle `for` avec `bounceBall` comme statement :

```
for (initialExpression; condition; incrementExpression) {     bounceBall() }
```

Ensuite, vous avez besoin d'une **expression initiale** pour commencer une boucle. C'est ici que vous déclarez une variable. Pour la plupart des boucles, cette variable est appelée `i`. Elle est également définie à 0.

Voici à quoi cela ressemble lorsque vous mettez l'`initialExpression` dans la boucle `for` :

```
for (let i = 0; condition; incrementExpression) {   bounceBall() }
```

Après que la statement s'exécute, la variable `i` est augmentée ou diminuée. Vous augmentez ou diminuez la valeur de `i` dans l'**increment expression**.

Pour augmenter la valeur de `i` de un, vous réassignez `i` de sorte qu'elle devienne `i + 1` avec `i = i + 1`. La forme abrégée de cette réassignation est `i++`, que vous trouverez dans la plupart des boucles `for`.

Pour diminuer la valeur de `i` de un, vous réassignez `i` de sorte qu'elle devienne `i - 1` avec `i = i - 1`. La forme abrégée de cette réassignation est `i--`, qui est une autre variation de ce que vous trouverez dans la plupart des boucles `for`.

Dans l'exemple `bounceBall` ci-dessus, nous avons augmenté la variable `i` de un à chaque fois que le code s'exécute :

```
for (let i = 0; condition; i++) {   bounceBall() }
```

Mais devriez-vous augmenter ou diminuer `i` ?

La réponse réside dans la **condition**. Cette statement de condition évalue soit `true` soit `false`. Si la statement évalue `true`, la statement s'exécute.

Lorsque la statement a été exécutée, JavaScript exécute l'increment expression et vérifie si la condition évalue `true` à nouveau. Il répète ce processus jusqu'à ce que la condition évalue `false`.

Une fois que la condition évalue `false`, JavaScript saute la boucle et continue avec le reste de votre code.

Ainsi, si vous ne voulez pas que la boucle s'exécute, vous pouvez définir une condition qui évalue immédiatement à false :

```
// Cette boucle ne s'exécutera pas puisque la condition évalue à false for (let i = 0; i < 0; i++) {   bounceBall()   const timesBounced = i + 1   console.log('The ball has bounced ' + timesBounced + ' times') } 
```

```
// Vous ne verrez que ceci console.log('next line of code')
```

![Image](https://cdn-media-1.freecodecamp.org/images/SXFTUbdOUIUpS6r2614f1jst5qkyyZzIYh3h)

Si vous voulez que la boucle **s'exécute deux fois**, vous changez la condition de sorte qu'elle évalue à false lorsque l'increment expression a été exécutée deux fois.

```
// Cette boucle s'exécutera deux fois for (let i = 0; i < 2; i++) {   bounceBall()   const timesBounced = i + 1   console.log('The ball has bounced ' + timesBounced + ' times')") } 
```

```
console.log('next line of code')
```

![Image](https://cdn-media-1.freecodecamp.org/images/5ssuIegeT3CruvHrbE9cDiw2Hgzhz4h7SQbA)

Si vous voulez que la boucle **s'exécute dix fois**, vous changez la condition de sorte qu'elle évalue à false lorsque l'increment expression a été exécutée dix fois.

```
// Cette boucle s'exécutera dix fois for (let i = 0; i < 10; i++) {   bounceBall()   const timesBounced = i + 1   console.log('The ball has bounced ' + timesBounced + ' times')") } 
```

```
console.log('next line of code')
```

![Image](https://cdn-media-1.freecodecamp.org/images/b15Gl3ujfERmjQFZ5cc9GHXo9OB2lBsmj7l4)

### Boucles infinies

Les boucles infinies se produisent lorsque la **condition** de vos boucles `for` retourne toujours `true`. Votre navigateur se bloquera si vous exécutez une boucle infinie.

Pour récupérer d'une boucle infinie, vous devez quitter votre navigateur de force. Sur un Mac, cela signifie que vous cliquez avec le bouton droit sur l'icône de votre navigateur et sélectionnez « forcer à quitter ». Sur une machine Windows, vous ouvrez le gestionnaire des tâches Windows avec `ctrl` + `alt` + `del`, sélectionnez votre navigateur et cliquez sur « Fin de tâche ».

### Parcourir des tableaux

En pratique, vous n'écrivez presque jamais une boucle qui s'exécute dix fois comme dans l'exemple `bounceBall` ci-dessus. Vous parcourrez toujours un tableau ou un objet.

Lorsque vous parcourez (ou itérez) un tableau, vous passez par chaque élément du tableau une fois. Pour ce faire, vous pouvez utiliser la longueur du tableau comme condition :

```
const fruitBasket = ['banana', 'pear', 'guava'] 
```

```
// fruitBasket.length est 3 for (let i = 0; i < fruitBasket.length; i++) {   console.log("There's a " + fruitBasket[i] + " in the basket") } 
```

```
// => There's a banana in the basket // => There's a pear in the basket // => There's a guava in the basket
```

L'autre façon d'écrire cette boucle `for` est d'utiliser une expression d'incrément négative. Cette version s'exécute légèrement plus vite que la boucle `for` ci-dessus, mais parcourt le tableau depuis la fin.

```
for (let i = fruitBasket.length - 1; i >= 0; i--) {  console.log("There's a " + fruitBasket[i] + " in the basket") } 
```

```
// => There's a guava in the basket // => There's a pear in the basket // => There's a banana in the basket
```

### Parcourir des tableaux avec for of

Une autre (beaucoup meilleure) façon de parcourir un tableau est d'utiliser une boucle `for...of`. Il s'agit d'une nouvelle syntaxe de boucle qui vient avec ES6. Elle ressemble à ceci :

```
const fruitBasket = ['banana', 'pear', 'guava'] 
```

```
for (let fruit of fruitBasket) {   console.log(fruit) } 
```

```
// => There's a banana in the basket // => There's a pear in the basket // => There's a guava in the basket
```

La boucle `for...of` est préférable à la boucle `for` standard car elle parcourt toujours le tableau une fois. Il n'est pas nécessaire d'écrire `array.length`, ce qui rend votre code beaucoup plus facile à lire et à maintenir.

Vous pouvez utiliser `for...of` avec n'importe quel objet itérable. Ce sont des objets qui contiennent la propriété `Symbol.iterator`. Les tableaux sont un tel objet. Si vous `console.log` un tableau vide, vous verrez qu'il a le `Symbol.iterator` comme l'une de ses clés (dans la clé Array `__proto__`) :

![Image](https://cdn-media-1.freecodecamp.org/images/MKAx1db1lQjOZE9FAG2A06V4H6nGBN41rLRA)

### Logique dans les boucles

Vous pouvez utiliser `if/else` ou toute autre logique dans une boucle for.

Par exemple, disons que vous avez une liste de nombres, et que vous voulez créer une deuxième liste de nombres qui sont plus petits que 20.

Pour atteindre cet objectif, vous parcourez d'abord les nombres.

```
const numbers = [25, 22, 12, 56, 8, 18, 34]
```

```
for (let num of numbers) {   // faire quelque chose ici }
```

Ici, vous voulez vérifier si chaque `num` est plus petit que 20.

```
const numbers = [25, 22, 12, 56, 8, 18, 34]
```

```
for (let num of numbers) {   if (num < 20) {     // faire quelque chose   } }
```

Si `num` est plus petit que 20, vous voulez l'ajouter à un autre tableau. Pour ce faire, vous utilisez la méthode `push`.

```
const numbers = [25, 22, 12, 56, 8, 18, 34]let smallerThan20 = [] 
```

```
for (let num of numbers) {   if (num < 20) {     smallerThan20.push(num)   } } 
```

```
// smallerThan20 === [12, 8 , 18]
```

### Conclusion

Une boucle `for` est utilisée lorsque vous voulez exécuter la même tâche (ou un ensemble de tâches) plusieurs fois.

Vous ne parcourrez rarement le code exactement dix fois. Normalement, vous voudrez parcourir un tableau.

Pour parcourir un tableau exactement une fois, vous pouvez utiliser la boucle `for...of`, qui est beaucoup plus facile à écrire et à comprendre par rapport à la boucle `for` traditionnelle.

N'oubliez pas que vous pouvez écrire n'importe quelle quantité de logique que vous voulez dans les boucles. Vous pouvez utiliser des fonctions, des statements `if/else`, ou même utiliser des boucles dans des boucles.

Si vous avez aimé cet article, vous aimerez apprendre **Learn JavaScript** — un cours qui vous aide à apprendre à **construire de vrais composants à partir de zéro** avec Javascript. [Cliquez ici pour en savoir plus sur Learn JavaScript](https://learnjavascript.today/) si vous êtes intéressé.

(Oh, au fait, si vous avez aimé cet article, je vous serais reconnaissant si vous pouviez [le partager](http://twitter.com/share?text=Understanding%20Javascript%20for%20Loops%3A%20you%20can%20write%20any%20amount%20of%20logic%20you%20want%20in%20loops.%20You%20can%20use%20functions%2C%20%60if%2Felse%60%20statements%20or%20even%20use%20loops%20in%20loops%20?%20&url=https://zellwk.com/blog/js-for-loops/&hashtags=). ?)

_Originalement publié sur [zellwk.com](https://zellwk.com/blog/js-for-loops/)._