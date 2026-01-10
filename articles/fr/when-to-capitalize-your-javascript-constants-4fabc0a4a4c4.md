---
title: Quand mettre en majuscules vos constantes JavaScript
subtitle: ''
author: Brandon Wozniewicz
co_authors: []
series: null
date: '2019-03-08T18:14:14.000Z'
originalURL: https://freecodecamp.org/news/when-to-capitalize-your-javascript-constants-4fabc0a4a4c4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XhNtWWMZPXU--QwrKShjpQ.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: variables
  slug: variables
seo_title: Quand mettre en majuscules vos constantes JavaScript
seo_desc: Many JavaScript style guides suggest capitalizing constant names. Personally,
  I rarely see this convention used where I thought it should be. This was because
  my definition of a constant was a bit off. I decided to do a bit of digging and
  become a bi...
---

De nombreux guides de style JavaScript suggèrent de mettre en majuscules les noms des constantes. Personnellement, je vois rarement cette convention utilisée là où je pensais qu'elle devrait l'être. Cela était dû au fait que ma définition d'une constante était un peu erronée. J'ai décidé de faire quelques recherches et de me familiariser un peu plus avec cette convention.

#### Comment définissons-nous le terme « constante » ?

En programmation, une constante est quelque chose qui ne change pas.

> [Il s'agit d'une valeur qui ne peut pas être modifiée par le programme pendant l'exécution normale](https://en.wikipedia.org/wiki/Constant_(computer_programming)).

Alors, JavaScript nous donne-t-il un moyen de déclarer une valeur qui ne peut pas être changée ? Avant de répondre à cette question, examinons les origines de cette convention.

#### La convention de capitalisation a des racines dans le langage C

C est un langage compilé. Cela signifie qu'un autre programme convertit tout votre code en code machine avant qu'il ne s'exécute.

JavaScript, en revanche, est un langage interprété. Un interpréteur lit votre code, ligne par ligne, au fur et à mesure qu'il s'exécute.

La différence entre la compilation et l'interprétation joue un rôle dans la manière dont nous déclarons les valeurs constantes en C.

En C, je peux déclarer une variable comme ceci :

`int hoursInDay = 24;`

Ou une constante comme ceci :

`#define hoursInDay 24`

Le deuxième exemple est appelé une **constante symbolique**. Les constantes symboliques peuvent être une séquence de caractères, une constante numérique ou une chaîne de caractères. Ce sont également appelées valeurs primitives. Les valeurs primitives en JavaScript sont les chaînes de caractères, les nombres, les booléens, null, undefined, symbol (à ne pas confondre avec les constantes symboliques) et big int.

Maintenant, revisitons la compilation.

Avant la compilation, il y a une phase de pré-compilation. Ici, le pré-compilateur remplace toutes les instances de constantes symboliques par la valeur respective. Le compilateur ne sait jamais que le programmeur a écrit `hoursInDay`. Il ne voit que le nombre `24`.

La capitalisation aide le programmeur à voir ces valeurs vraiment constantes.

`#define HOURS_IN_DAY 24`

#### Les constantes JavaScript sont différentes des constantes symboliques

Avant ES6, nous stockions la plupart des valeurs dans des variables, même celles que vous vouliez garder constantes.

La capitalisation nous aidait à voir les valeurs que nous voulions garder constantes.

```js
var HOURS_IN_DAY = 24;
var hoursRemaining = currentHour - HOURS_IN_DAY;
var MY_NAME = 'Brandon';
MY_NAME = ... // oops, ne voulez pas faire cela.
```

ES6 a introduit la déclaration `const` qui n'est pas une « constante » au sens le plus pur.

ES6 a ajouté les termes `const` et `let` comme moyens de créer des variables avec des intentions différentes.

Avec ces deux termes, vous pourriez penser que nous devons soit :

1. ne rien mettre en majuscules puisque nous pouvons clairement voir quelles variables sont destinées à rester les mêmes, ou

2. nous devons mettre en majuscules tout ce que nous déclarons avec `const`.

Par définition, `const` crée une constante qui est une référence en lecture seule à une valeur. Cela ne signifie pas que la valeur qu'elle contient est immuable. Cela signifie seulement que [l'identifiant de la variable ne peut pas être réassigné](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const).

En d'autres termes, certaines références `const` peuvent changer.

```js
const firstPerson = {
  favoriteNumber: 10,
};
const secondPerson = firstPerson;
console.log(secondPerson.favoriteNumber); //10
firstPerson.favoriteNumber +=1;
console.log(secondPerson.favoriteNumber); //11
```

L'exemple ci-dessus montre que la déclaration `const` ne garantit pas que la variable est immuable.

`const` nous empêche seulement d'essayer de réassigner le nom de la variable. Cela n'empêche pas la propriété de l'objet de changer. Rappelez-vous : les objets sont passés par référence.

```js
// "TypeError: Assignment to constant variable."
secondPerson = 'something else';
const secondPerson = 'Me'
secondPerson = 'something else';
```

Ainsi, pour JavaScript, nous devons aller au-delà de la simple recherche d'une déclaration `const`. Nous devons poser deux questions pour déterminer si une variable est une constante :

1. La valeur de la variable est-elle primitive ?

2. Avons-nous l'intention de garder le nom de la variable pointant vers la même valeur tout au long de notre programme ?

Si la réponse est oui aux deux, nous devons déclarer la variable avec `const` et pouvons mettre le nom en majuscules.

Remarquez que j'ai dit « pouvons ». L'esprit de cette convention vient de différents langages qui avaient de vraies constantes. JavaScript n'en a pas. Du moins, pas au sens le plus pur. Cela peut être la raison pour laquelle vous voyez cette convention moins souvent que vous pourriez vous y attendre. [Airbnb a une excellente section dans leur guide de style avec leur avis ici.](https://github.com/airbnb/javascript/#naming--uppercase)

Le **point clé à retenir** est de reconnaître que la définition d'une constante en JavaScript doit inclure les intentions du programmeur.

De plus, toutes les conventions d'un langage ne sont pas nécessairement pertinentes dans un autre langage. Enfin, je peux seulement imaginer que de nombreuses conventions étaient utilisées bien avant que les IDE aient les capacités qu'ils ont aujourd'hui. Je suis convaincu que mon IDE prend plaisir à me dire que j'ai tort. Cela arrive souvent.

Merci d'avoir lu !

woz

Suivez-moi sur [Twitter.](https://twitter.com/Brandonwoz)

#### Notes

* Vous vous demandez peut-être pourquoi je n'ai pas utilisé `PI` dans ces exemples. Les acronymes, en particulier ceux de deux lettres, tendent à être soit toujours en majuscules, soit toujours en minuscules par convention.