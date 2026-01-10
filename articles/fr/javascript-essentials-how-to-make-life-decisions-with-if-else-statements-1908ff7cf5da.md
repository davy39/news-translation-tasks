---
title: 'Les essentiels de JavaScript : comment prendre des décisions avec les instructions
  if/else'
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2017-12-13T16:55:06.000Z'
originalURL: https://freecodecamp.org/news/javascript-essentials-how-to-make-life-decisions-with-if-else-statements-1908ff7cf5da
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1d5_gKjzU-uk8T4AhrIDlw.jpeg
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
seo_title: 'Les essentiels de JavaScript : comment prendre des décisions avec les
  instructions if/else'
seo_desc: 'Let’s say you’re walking on a busy street in the middle of town. You’re
  about to cross the road when you notice the traffic light for pedestrians turns
  red. What do you do?

  You stop, don’t you?

  And what happens when the light turns green again? You s...'
---

Imaginez que vous marchez dans une rue animée en plein centre-ville. Vous êtes sur le point de traverser la route lorsque vous remarquez que le feu piéton passe au rouge. Que faites-vous ?

Vous vous arrêtez, n'est-ce pas ?

Et que se passe-t-il lorsque le feu repasse au vert ? Vous commencez à marcher.

Nous pouvons transposer cette analogie en code. Cela ressemble à quelque chose comme : « Si le feu passe au rouge, arrêtez de marcher. Sinon, continuez à marcher ».

Et cela, mon ami, est la base d'une instruction `if/else`.

### L'instruction if/else

L'instruction `if/else` aide à contrôler ce que votre programme fait dans des situations spécifiées. Elle ressemble à ceci :

```
if (condition) {     // Faire quelque chose } else {     // Faire autre chose }
```

La `condition` indique à JavaScript quoi vérifier avant de continuer. Si la condition évalue à `true`, JavaScript exécute le code dans le bloc `if`.

Si la condition évalue à `false`, JavaScript exécute le code du bloc `else`.

Dans l'exemple du feu de circulation, nous vérifions si le feu est rouge :

```
// Note : Cet exemple ne contient pas encore de code valide if (light is red) {  stop walking } else {  continue walking }
```

Si vous devez vérifier plus d'une condition, vous pouvez utiliser `else if`, qui se place entre `if` et `else`.

Quand auriez-vous besoin d'une deuxième condition ?

Eh bien, supposons que vous voulez traverser une petite route. S'il n'y a pas de voitures autour, attendriez-vous que le feu piéton passe au vert ? Vous traversez quand même, n'est-ce pas ?

En code, cela ressemblerait à ceci :

```
if (light is red) {   // Arrêter de marcher } else if (cars around) {   // Arrêter de marcher } else if (yet another condition) {   // Faire encore autre chose } else {   // Faire la dernière chose }
```

Dans ce cas, si la première condition évalue à `true`, JavaScript exécute le code dans le bloc `if`.

Si la première condition évalue à `false`, JavaScript vérifie la condition dans le bloc `else if` suivant et voit si elle évalue à `true`. Cela continue jusqu'à ce que tous les blocs `else if` soient épuisés.

Pour vérifier si une condition évalue à `true` ou `false`, JavaScript s'appuie sur deux choses :

1. Les opérateurs de comparaison
2. Les valeurs truthy et falsy

Parlons d'abord des opérateurs de comparaison.

### Les opérateurs de comparaison

Il existe quatre principaux types d'opérateurs de comparaison :

1. Supérieur à (`>`) ou supérieur ou égal à (`>=`)
2. Inférieur à (`<`) ou inférieur ou égal à (`<=`)
3. Strictement égal (`===`) ou égal (`==`)
4. Strictement inégal (`!==`) ou inégal (`!=`)

Les deux premiers types d'opérateurs de comparaison sont simples. Vous les utilisez pour comparer des nombres.

```
24 > 23 // Vrai 24 > 24 // Faux 24 >= 24 // Vrai 
```

```
24 < 25 // Vrai 24 < 24 // Faux 24 <= 24 // Vrai
```

Les deux autres types d'opérateurs de comparaison sont également assez simples. Vous les utilisez pour vérifier si les choses sont égales ou inégales les unes aux autres.

```
24 === 24 // Vrai 24 !== 24 // Faux
```

Cependant, il y a une différence entre strictement égal (`===`) et égal (`==`), et strictement inégal (`!==`) et inégal (`!=`) :

```
'24' === 24 // Faux '24' == 24 // Vrai 
```

```
'24' !== 24 // Vrai '24' != 24 // Faux
```

Comme vous pouvez le voir dans l'exemple ci-dessus, lorsque vous comparez une chaîne de caractères `24` avec le nombre 24, `===` évalue à `false` tandis que `==` évalue à `true`.

Pourquoi en est-il ainsi ? Regardons la différence entre strictement égal et égal.

### === vs == (ou !== vs !=)

JavaScript est un langage faiblement typé. Cela signifie que, lorsque nous déclarons des variables, nous ne nous soucions pas du type de valeur qui va dans la variable.

Vous pouvez déclarer n'importe quel type primitif ou objet, et JavaScript fait le reste pour vous automatiquement :

```
const aString = 'Some string' const aNumber = 123 const aBoolean = true
```

Lorsque vous comparez des choses avec strictement égal (`===`) ou strictement inégal (`!==`), JavaScript vérifie le type de la variable. C'est pourquoi une **chaîne** de caractères `24` et un **nombre** `24` ne sont pas égaux.

```
'24' === 24 // Faux '24' !== 24 // Vrai
```

Lorsque vous comparez des choses avec égal (`==`) ou inégal (`!=`), JavaScript convertit (ou caste) les types pour qu'ils correspondent.

Généralement, JavaScript essaie de convertir tous les types en nombres lorsque vous utilisez un opérateur de conversion. Dans l'exemple ci-dessous, la **chaîne** `24` est convertie en **nombre** 24 avant la comparaison.

C'est pourquoi une chaîne de caractères `24` est égale à un nombre 24 lorsque vous utilisez `==`.

```
'24' == 24 // Vrai '24' != 24 // Faux
```

Les booléens peuvent également être convertis en nombres. Lorsque JavaScript convertit les booléens en nombres, `true` devient 1 et `false` devient 0.

```
0 == false // Vrai 1 == true // Vrai 2 == true // Faux
```

La conversion automatique de type (lors de l'utilisation des opérateurs de comparaison) est l'une des causes courantes de bugs difficiles à trouver. **Lorsque vous comparez pour l'égalité, utilisez toujours les versions strictes** (`===` ou `!==`).

### Comparaison d'objets et de tableaux

Essayez de comparer des objets et des tableaux avec `===` ou `==`. Vous serez très surpris.

```
const a = { isHavingFun: true } const b = { isHavingFun: true } 
```

```
console.log(a === b) // faux console.log(a == b) // faux
```

Dans l'exemple ci-dessus, `a` et `b` **semblent** exactement identiques. Ce sont tous deux des objets, ils ont les mêmes valeurs.

L'étrange chose est que `a === b` sera toujours faux. Pourquoi ?

Imaginez que vous avez un frère ou une sœur jumeau(e) identique. Vous ressemblez exactement à votre jumeau. Même couleur de cheveux, même visage, mêmes vêtements, tout est identique. Comment les gens peuvent-ils vous différencier ? Ce serait difficile.

En JavaScript, chaque objet a une « carte d'identité ». Cette carte d'identité est appelée la **référence** à l'objet. Lorsque vous comparez des objets avec des opérateurs d'égalité, vous demandez à JavaScript de vérifier si les deux objets ont la même référence (la même carte d'identité).

Est-ce une surprise que `a === b` soit toujours faux maintenant ?

Modifions un peu cela et assignons `a` à `b`.

```
const a = { isHavingFun: true } const b = a
```

Dans ce cas, `a === b` évalue à vrai parce que `b` pointe maintenant vers la même référence que `a`.

```
console.log(a === b) // vrai
```

### Truthy et Falsy

Si vous écrivez une seule variable (comme `hasApples` dans l'exemple ci-dessous) comme condition d'une instruction `if/else`, JavaScript vérifie une valeur truthy ou falsy.

```
const hasApples = 'true' 
```

```
if (hasApples) {   // Manger une pomme } else {   // Acheter des pommes }
```

Une valeur **falsy** est une valeur qui évalue à `false` lorsqu'elle est convertie en booléen. Il y a six valeurs possibles falsy en JavaScript :

1. `false`
2. `undefined`
3. `null`
4. `0` (zéro numérique)
5. `""` (chaîne vide)
6. `NaN` (Not A Number)

Une valeur **truthy**, en revanche, est une valeur qui évalue à `true` lorsqu'elle est convertie en booléen. Dans le cas des nombres, tout ce qui n'est pas `0` se convertit en `true`.

**La conversion automatique de type en valeurs truthy et falsy est fortement encouragée en JavaScript**, car elle rend le code plus court et plus facile à comprendre.

Par exemple, si vous voulez vérifier si une chaîne est vide, vous pouvez utiliser la chaîne dans la condition directement.

```
const str = '' 
```

```
if (str) {   // Faire quelque chose si la chaîne n'est pas vide } else {   // Faire quelque chose si la chaîne est vide }
```

### Conclusion

Les instructions `if/else` sont utilisées pour contrôler ce que votre programme fait dans des situations spécifiques. Elles vous permettent de déterminer si vous devez marcher ou traverser la route, en fonction des conditions qui vous sont données.

Pour vérifier si une condition est vraie ou fausse, JavaScript s'appuie sur deux choses :

1. les opérateurs de comparaison
2. les valeurs truthy/falsy

Si vous avez aimé cet article, vous allez adorer **Apprendre JavaScript** — un cours qui vous aide à apprendre à **construire de vrais composants à partir de zéro** avec JavaScript. [Cliquez ici pour en savoir plus sur Apprendre JavaScript](https://learnjavascript.today/) si vous êtes intéressé.

(Oh, au fait, si vous avez aimé cet article, je vous serais reconnaissant si vous pouviez [le partager](http://twitter.com/share?text=What%20determines%20if%20a%20condition%20is%20true%20or%20false%3F%0A%0A1.%20comparison%20operators.%0A2.%20Truthy%2Ffalsy%20values%0A%0ABy%20%40zellwk%20?%20&url=https://zellwk.com/blog/js-if-else/&hashtags=). ?)

_Article original publié sur [zellwk.com](https://zellwk.com/blog/js-if-else/)._