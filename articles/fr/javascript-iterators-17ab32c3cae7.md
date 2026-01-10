---
title: Un aperçu des itérateurs JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-11T07:01:00.000Z'
originalURL: https://freecodecamp.org/news/javascript-iterators-17ab32c3cae7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wEv6UnPpMocWKCoH2x1HSA.jpeg
tags:
- name: education
  slug: education
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: technology
  slug: technology
seo_title: Un aperçu des itérateurs JavaScript
seo_desc: 'By Joanna Gaudyn

  The difference between for, for…in and for…of loops


  _[source](https://unsplash.com/photos/kJAl5OPoRgQ" rel="noopener" target="blank"
  title=")

  Iteration might be one of the most commonly used operations in programming. It is
  taking a...'
---

Par Joanna Gaudyn

#### La différence entre les boucles for, for...in et for...of

![Image](https://cdn-media-1.freecodecamp.org/images/tS2k4SixOdqRW2ZATfBIIOTtNTaqjv2hU3ba)
_[source](https://unsplash.com/photos/kJAl5OPoRgQ" rel="noopener" target="_blank" title=")_

L'itération est peut-être l'une des opérations les plus couramment utilisées en programmation. Elle consiste à prendre un ensemble d'éléments et à effectuer une opération donnée sur chacun d'eux dans une séquence. Les boucles permettent de faire quelque chose de manière répétée, rapide et facile.

En JavaScript, différents mécanismes de boucle vous permettent de définir le début et la fin d'une boucle de différentes manières. Il n'y a pas de réponse facile à la question de savoir quel mécanisme est le meilleur, car différentes situations nécessitent des approches différentes, ce qui signifie que vos besoins peuvent être mieux servis par un type de boucle plutôt que par un autre.

Voici ce que vous pouvez utiliser pour [boucler en JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration) :

* instruction do...while
* instruction while
* instruction étiquetée
* instruction break
* instruction continue
* instruction for
* instruction for...in
* instruction for...of

Examinons de plus près les trois dernières. Elles peuvent être assez déroutantes lorsque vous commencez à travailler avec JavaScript, car les noms ne facilitent pas vraiment la mémorisation des mécanismes qui les sous-tendent. J'espère que quelques exemples aideront à clarifier les concepts si vous êtes encore un peu incertain.

![Image](https://cdn-media-1.freecodecamp.org/images/PjMWkwqImDEcv4L38v-POyEuuE8LndiFaRKz)
_[source](https://www.pexels.com/photo/red-surface-1412212/" rel="noopener" target="_blank" title=")_

#### La boucle 'for'

La boucle `for` est le type de boucle le plus courant et vous avez peut-être déjà rencontré ce type de boucle dans d'autres langages de programmation, alors faisons un rapide rappel.

Voici la syntaxe de base :

```js
for ([initialExpression]; [exit condition]; [incrementExpression]) {
  do something;
}
```

Prenons un exemple :

```js
const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

for (let i = 0; i < numbers.length; i++) {
  console.log(numbers[i]);
}
```

Affiche :

> 0  
>  1  
>  2  
>  3  
>  4  
>  5  
>  6  
>  7  
>  8  
>  9

Alors, que se passe-t-il vraiment ici ? Une boucle `for` se répète jusqu'à ce qu'une condition spécifiée évalue à faux. Dans notre cas, nous commençons un compteur (variable `i`) à 0, nous affichons un nombre de notre tableau `numbers` qui se trouve à l'index `i` du tableau, et enfin nous incrémentons le compteur. Nous déclarons également que notre boucle doit se rompre lorsque le compteur n'est plus inférieur à la taille du tableau (`numbers.length`).

Les principaux inconvénients d'une boucle `for` sont de devoir suivre un compteur et une condition de sortie. La syntaxe n'est pas non plus très intuitive, et pour comprendre ce qui se passe, vous devez vraiment mémoriser ce que chaque partie du code représente. Même si une boucle `for` peut être une solution pratique pour parcourir un tableau, il existe souvent des moyens plus propres de le faire.

![Image](https://cdn-media-1.freecodecamp.org/images/nR8ENaf2lEQW1NzZH9sxELuxxwm3C1oFrNDf)
_[source](https://unsplash.com/photos/wKTF65TcReY" rel="noopener" target="_blank" title=")_

#### La boucle for...in

La boucle `for ... in` élimine les deux principales faiblesses de la boucle `for`. Il n'est pas nécessaire de penser à un compteur ou à une condition de sortie.

```js
const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

for (const index in numbers) {
  console.log(numbers[index]);
}
```

Affiche :

> 0  
>  1  
>  2  
>  3  
>  4  
>  5  
>  6  
>  7  
>  8  
>  9

Le principal inconvénient de cette solution est que nous devons toujours utiliser un index pour accéder aux éléments du tableau.

Une autre chose qui peut poser problème est que les boucles `for ... in` parcourent toutes les propriétés énumérables. Que signifie cela en pratique ? Si vous devez ajouter une méthode supplémentaire à votre objet (dans notre cas : tableau), cette méthode apparaîtra également dans votre boucle.

Jetez un coup d'œil à cet exemple :

```js
Array.prototype.decimalfy = function() {
  for (let i = 0; i < this.length; i++) {
    this[i] = this[i].toFixed(4);
  }
};

const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

for (const index in numbers) {
  console.log(numbers[index]);
}
```

Affiche :

> 0  
>  1  
>  2  
>  3  
>  4  
>  5  
>  6  
>  7  
>  8  
>  9  
>  function() {  
>  for (let i = 0; i < this.length; i++) {  
>  this[i] = this[i].toFixed(2);  
>  }  
>  }

Je suppose que vous serez d'accord pour dire que ce n'est pas exactement ce que nous recherchions. Lorsque vous parcourez des tableaux, essayez d'éviter les boucles `for ... in` pour éviter les surprises inattendues.

![Image](https://cdn-media-1.freecodecamp.org/images/SGFyxaY3XVEM7kIYdpwHLHVREdS1C4cjKm3b)
_[source](https://pixabay.com/en/tiger-and-turtle-duisburg-looping-1940551/" rel="noopener" target="_blank" title=")_

#### La boucle for...of

La boucle for...of est la dernière addition à la famille des boucles `for` en JavaScript.

Elle combine les forces de la boucle `for` et de la boucle `for ... in`, vous permettant de parcourir tout type de type de données qui est itérable (= suit le [protocole itérable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)), tel que chaîne de caractères, tableau, ensemble ou carte. Notez que l'objet ( `{}`) n'est pas itérable par défaut.

La syntaxe d'une boucle `for ... of` est presque la même que celle d'une boucle `for ... in` :

```js
const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

for (const number of numbers) {
  console.log(number);
}
```

Affiche :

> 0  
>  1  
>  2  
>  3  
>  4  
>  5  
>  6  
>  7  
>  8  
>  9

Un grand avantage est que nous n'avons plus besoin d'un index et pouvons accéder aux éléments de notre tableau directement. Cela fait de la boucle `for ... of` la plus compacte de toute la famille des boucles for.

De plus, le mécanisme de la boucle `for ... of` permet une rupture de boucle, selon votre condition. Jetez un coup d'œil à cet exemple :

```js
const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

for (const number of numbers) {
  if (number % 2 !== 0) {
    continue;
  }
  console.log(number);
}
```

Affiche :

> 0  
>  2  
>  4  
>  6  
>  8

De plus, l'ajout de nouvelles méthodes aux objets n'affecte pas la boucle `for ... of` :

```js
Array.prototype.decimalfy = function() {
  for (i = 0; i < this.length; i++) {
    this[i] = this[i].toFixed(4);
  }
};
const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
for (const number of numbers) {
  console.log(number);
}
```

Affiche :

> 0  
>  1  
>  2  
>  3  
>  4  
>  5  
>  6  
>  7  
>  8  
>  9

Cela fait de la boucle `for ... of` la plus puissante de toutes !

#### Remarque : la boucle forEach

Il peut également être utile de mentionner la boucle `forEach`. Notez cependant que `forEach()` est une méthode de tableau et ne peut donc pas être utilisée sur d'autres objets JavaScript. Cette méthode peut être utile si votre cas remplit deux conditions : vous souhaitez parcourir un tableau et vous n'avez pas besoin d'arrêter la boucle avant la fin de ce tableau :

```js
const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

numbers.forEach(function(number) {
  console.log(number);
});
```

Affiche :

> 0  
>  1  
>  2  
>  3  
>  4  
>  5  
>  6  
>  7  
>  8  
>  9

J'espère que ces exemples vous ont aidé à comprendre tous les différents mécanismes d'itération en JavaScript.

Commencez-vous tout juste votre parcours en programmation ? Voici quelques articles qui pourraient également vous intéresser :

* [Un bootcamp de codage est-il fait pour vous ?](https://medium.freecodecamp.org/is-a-coding-bootcamp-something-for-you-974c3b5bd3b2)
* [Le changement de carrière est-il vraiment possible ?](https://medium.com/datadriveninvestor/is-career-change-really-possible-c29c9a0d791c)
* [Pourquoi Ruby est un excellent langage pour commencer la programmation](https://medium.com/@aska.gaudyn/why-ruby-is-a-great-language-to-start-programming-with-2f17e0c2907a)