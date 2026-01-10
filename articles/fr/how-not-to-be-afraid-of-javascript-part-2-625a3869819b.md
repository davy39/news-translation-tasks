---
title: Comment ne pas avoir peur des parties amusantes de JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-13T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-not-to-be-afraid-of-javascript-part-2-625a3869819b
coverImage: https://cdn-media-1.freecodecamp.org/images/0*q6gPdqvGh9U6wkAg.jpg
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment ne pas avoir peur des parties amusantes de JavaScript
seo_desc: 'By Neil Kakkar

  Part 2 of our series discusses iteration protocols, for loops, and generator functions

  This is Part 2 of Javascript mastery — and probably the most exciting parts of the
  language. ( Until Part 3 comes around, anyway ;) )

  Part 1 covered...'
---

Par Neil Kakkar

#### Partie 2 de notre série traite des protocoles d'itération, des boucles for et des fonctions génératrices

Ceci est la Partie 2 de la maîtrise de Javascript — et probablement les parties les plus excitantes du langage. (Jusqu'à ce que la Partie 3 arrive, en tout cas ;) )

[La Partie 1 couvrait les bases du langage](https://neilkakkar.com/How-not-to-be-afraid-of-Javascript-anymore.html), et ici nous couvrirons les protocoles d'itération, leur utilisation dans les boucles for, et les fonctions génératrices.

Pourquoi les fonctions génératrices dans le mélange ? Si vous pensez que c'est un ajout aléatoire, continuez à lire ! Les générateurs sont liés à l'itération !

### Boucles For

Eh bien, vous connaissez la boucle for de base, n'est-ce pas ?

`for (let i = 0; i < arr.length; i++)`

Vous l'utiliseriez pour accéder aux éléments d'un tableau.

Vous utiliseriez quelque chose de similaire pour accéder aux propriétés / valeurs d'un objet :

`for ( let i = 0; i < Object.keys(obj).length; i++)`

Et encore, quelque chose de similaire pour `map`, `set` et tout autre objet personnalisé que vous définissez. Lorsque vous voulez simplement les valeurs / propriétés, écrire cette boucle peut conduire à des erreurs. Vous pourriez utiliser la propriété length de manière incorrecte, vous pourriez faire des erreurs de décalage d'un, ou vous pourriez penser que `Object.keys(obj).length` est simplement laid (je suis d'accord).

Puisqu'il devrait y avoir une meilleure façon de faire les choses, voici les boucles `for...of` et `for...in` ! ... Une seule meilleure chose, n'est-ce pas ?

Eh bien, oui. Ce sont toutes deux des boucles pour itérer sur quelque chose, mais c'est là que s'arrête la similitude, comme nous le verrons ci-dessous.

### Boucle For...of

Commençons par essayer d'itérer sur les valeurs d'un objet.

Pour accéder aux éléments d'un tableau : `for (let val of arr)`

Pour accéder aux valeurs d'un objet : `for (let var of Object.values(obj))`

Magnifique, n'est-ce pas ? Cela soulève cependant la question, pourquoi `for (let var of obj)` ne fonctionne-t-il pas simplement ?

Plongeons plus profondément dans le fonctionnement de cela et où vous pouvez utiliser la boucle `for...of`. Plus important encore, comment vos classes / objets peuvent-elles en tirer parti.

Bienvenue dans le monde des protocoles d'`itération`.

Tout d'abord, une courte note sur les protocoles.

Si vous avez déjà traité avec la [POO](https://en.wikipedia.org/wiki/Object-oriented_programming), alors vous savez probablement ce qu'est une interface : c'est une description des actions qu'un objet peut faire, comme un contrat. Si vous voulez faire `X`, vous devez avoir une fonction définie dans le contrat qui fait X. Par exemple, `doX(a,b,c)` qui prend les paramètres a,b,c. De la même manière, les protocoles sont des interfaces en Javascript.

Nous avons 2 protocoles d'itération en Javascript :

### Protocole Itérable

Ce protocole permet aux objets JS de déterminer leur comportement d'itération. Il permet à un objet d'être itéré. Il détermine également ce qui est exactement itéré. L'interface exige une méthode [Symbol.iterator] quelque part dans la chaîne de prototypes.

![Image](https://cdn-media-1.freecodecamp.org/images/tzVvXusT0bOcZiXmqE6r32LjQLZ2LEjioZxh)
_Documentation MDN_

### Protocole Itérateur

Ce protocole détermine la manière dont notre protocole itérable doit retourner les valeurs itérées. Eh ? Un exemple rendrait cela plus clair.

La façon dont je vois cela, le protocole itérateur définit l'interface de classe pour un itérateur. (Si vous regardez à nouveau le nom, cela semble assez évident, non ? Protocole Itérateur = Interface Itérateur. Regardez maman, je peux faire du JS maintenant.)

Revenons à notre chère documentation :

![Image](https://cdn-media-1.freecodecamp.org/images/Jx4mFiYHWkzInSy6Hw0ZRCFRpr6kkju6yeAJ)
_[Source](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols#The_iterator_protocol" rel="noopener" target="_blank" title=")_

Ainsi, notre interface itérateur est déterminée complètement par l'existence de la fonction `next()` sur un objet.

Un point clé à faire ici est qu'il est considéré comme une meilleure pratique de mettre en œuvre à la fois les protocoles itérateur et itérable, puisque certaines fonctions / syntaxes peuvent s'attendre à l'un, tandis que d'autres à l'autre. Faire cela vous permet d'utiliser les deux avec votre itérateur. Voici un exemple merveilleux :

```js
const iteratorObject = {
 next() {
     const value = Math.random();
     if ( value < this.threshold ) {
         return { done: false, value}; 
     }
     return { done: true};
 },
 [Symbol.iterator]: function() {
     return this;
 },
 threshold: 0.7
}
```

La beauté réside dans la partie `[Symbol.iterator]` de l'itérateur. En définissant cela, nous permettons à notre itérateur d'être exposé à une variété de fonctions et de syntaxes qui nécessitent un protocole itérable, pas seulement un protocole itérateur. Que pouvez-vous faire avec cela ?

Vous vous souvenez de l'opérateur de propagation ? — Il accepte également un protocole itérable !

```
>[...iteratorObject] 
[0.03085962239970308, 0.20649861146804716]
```

Et bien sûr, fonctionne avec `for...of`, où cette histoire a commencé.

```
>for (let val of iteratorObject) {
    console.log(val);
}
0.6234680935767514
0.525812241023621
```

Sous le capot, nous pouvons maintenant comprendre ce qui se passe : toutes ces méthodes utilisent le `[Symbol.iterator]` pour générer un itérateur, et itèrent sur celui-ci en utilisant `next` !

```js
>const iter = iteratorObject[Symbol.iterator]()
undefined
>iter.next();
{done: false, value: 0.04474940944875905}
>iter.next();
{done: true}
```

Cela rend les choses plus faciles lorsque vous n'avez pas à le faire vous-même. Il y a un point que nous n'avons pas abordé, qui va de pair avec les boucles `for...of`, qui est : `for...in`. Quelle est la différence ? Plongeons-nous, en commençant par notre exemple !

### Boucles For...In

```js
>for (const val in iteratorObject) {
    console.log(val);
}
next
threshold
```

À première vue, la différence semble évidente : `for...in` obtient les propriétés, tandis que `for...of` obtient les valeurs ! Pourquoi [Symbol.iterator] est-il manquant alors ? Eh bien, il y a 2 raisons.

Il existe un descripteur de propriété énumérable sur les propriétés. Cela détermine si la propriété donnée est énumérable, configurable ou modifiable.

```js
> Object.getOwnPropertyDescriptors(iteratorObject)
{ next:
   { value: [Function: next],
     writable: true,
     enumerable: true,
     configurable: true },
  threshold:
   { value: 0.7,
     writable: true,
     enumerable: true,
     configurable: true },
  [Symbol(Symbol.iterator)]:
   { value: [Function: [Symbol.iterator]],
     writable: true,
     enumerable: true,
     configurable: true } }
```

La boucle `for...in` parcourt les propriétés dont le descripteur énumérable est défini sur true, ainsi que les propriétés non-symbole. Cela explique cela, n'est-ce pas ? Juste pour confirmer, vous pourriez ajouter une nouvelle propriété à l'objet, avec énumérable défini sur false, et elle n'apparaîtrait pas dans la boucle `for...in`.

```js
Object.defineProperty(iteratorObject, "newHiddenProperty", {
    enumerable: false,
    value: "hidden",
})
```

En effet, elle n'y est toujours pas. `Object.keys()` utilise la méthodologie exacte.

```js
>for(const val in iteratorObject) {
    console.log(val);
}
next
threshold
```

Revenons à la question qui nous a fait descendre dans ce terrier — Pourquoi `for(let val of obj)` ne fonctionne-t-il pas simplement ? Maintenant vous savez, n'est-ce pas ? Parce qu'il n'existe pas de protocole itérable sur le prototype de l'objet !

Pourquoi pas ? La réponse simple est — choix de conception du langage. Pourquoi ont-ils choisi cela ? Parce que beaucoup d'objets héritent de l'objet de base. Avoir un protocole itérable sur l'objet de base signifierait rendre tous ces objets itérables. Par exemple : vos objets de date deviennent itérables, ce qui n'a aucun sens.

### Boucle ForEach

Cela nous amène au dernier type de boucles for : la boucle forEach. J'ai vu des gens se demander pourquoi `forEach` ne fonctionne pas partout (comme sur les objets) et je répondrai à cette question ici.

Réponse simple — `Array.prototype.forEach()`.

La boucle `forEach` est définie uniquement pour les tableaux ! Vous ne pouvez donc les utiliser qu'avec des tableaux. Maintenant, `forEach` ne se soucie pas de l'origine de ce tableau. Il pourrait s'agir d'un tableau natif simple, ou d'un tableau généré par des objets, comme Object.keys().

Pour terminer la section sur les boucles, un piège courant.

Lorsque vous utilisez des objets en JS comme des maps (ou dictionnaires, hashmap), vous pouvez rencontrer des problèmes lorsqu'une clé coïncide avec une propriété dans la chaîne de prototypes.

Considérez cet exemple :

Vous avez un objet avec certaines clés sur lesquelles vous voulez itérer.

```js
const baseObject = {
  a: 1,
  b: 2,
  someProperty: function() {
    return 4;
  }
}


const myObjectMap = Object.create(baseObject);

myObjectMap.c = 3; // clé définie dans la map pour une raison quelconque.

for(let val in myObjectMap) { // cela itère dans la chaîne !
  console.log(val);
}

> c
 a
 b
 someProperty
```

Vous vouliez probablement juste voir `c`, la clé que vous avez définie. Vous pouvez corriger cela via :

```js
for (let val in myObjectMap) {
  if (myObjectMap.hasOwnProperty(val)) {
    console.log(val);
  }
}

> c
```

Ainsi, deux règles pour éviter ce problème :

1. Utilisez toujours `hasOwnProperty()` pour vérifier si la clé que vous cherchez existe dans l'objet (et non dans la chaîne de prototypes)
2. N'utilisez jamais `hasOwnProperty` comme clé dans vos dictionnaires / maps.

Si vous avez remplacé `hasOwnProperty`, il existe encore un moyen de l'utiliser, puisque c'est une méthode du prototype de l'objet.

```
myObjectMap.hasOwnProperty = 4;

for(let val in myObjectMap) {
    if (myObjectMap.hasOwnProperty(val)) {
        console.log(val);
    }
}
> Uncaught TypeError: myObjectMap.hasOwnProperty is not a function
    at <anonymous>:4:21

// au lieu de cela, nous pouvons faire : 
for(let val in myObjectMap) {
    if (Object.prototype.hasOwnProperty.call(myObjectMap, val)) {
        console.log(val);
    }
}

> c
  hasOwnProperty
```

[Vous souvenez-vous de `call` et `apply` de la dernière partie ?](https://neilkakkar.com/How-not-to-be-afraid-of-Javascript-anymore.html#the-new-keyword-and-apply) C'est une façon géniale de les utiliser.

### Fonctions Génératrices

Les [fonctions génératrices](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*) permettent une entrée et une sortie à la demande d'une fonction. Les points d'entrée et de sortie sont fixes. C'est comme un visa à entrées multiples.

Ce sont des outils très puissants pour accomplir des choses difficiles.

La façon dont je vois les fonctions génératrices est la suivante : elles sont utiles pour créer une liste de valeurs à la volée, sans le surcoût d'avoir un tableau.

Pourquoi ne pas simplement itérer sur un tableau de valeurs ? Eh bien, les générateurs économisent de l'espace. Il n'y a pas de tableau au départ — juste le calcul (ou l'E/S) nécessaire pour obtenir l'élément suivant du « tableau ».

Plongeons dans le mécanisme de cela.

Appeler une fonction génératrice n'exécute pas le corps mais retourne un objet itérateur pour la fonction. Le corps est exécuté lorsque vous appelez la méthode `next()` de l'itérateur. Qu'en est-il du point de sortie fixe ? L'ensemble du corps n'est pas exécuté, mais seulement jusqu'à la prochaine expression `yield` dans le corps.

Cette expression `yield` spécifie également la valeur à retourner.

Rendons ce concept concret avec un exemple. Faisons l'exemple de tweet de la Partie 1.

```js
function * generateTweets(userID, numberOfTweets) {
    for(let i=0; i< numberOfTweets; i++) {
        const tweet = randomTweetGenerator(); // supposons que cela vous donne une chaîne de mots < 280 caractères.
        yield { tweet, userID, tweetID: i};
    }
}

const tweetList = generateTweets('neilkakkar', 3);
for( let tweet of tweetList) {
	  console.log(tweet);
}

> {tweet: "hi", userID: "neilkakkar", tweetID: 0}
  {tweet: "how's it going?", userID: "neilkakkar", tweetID: 1}
  {tweet: "I'm automagic", userID: "neilkakkar", tweetID: 2}


console.log(tweetList.next());
>    {value: undefined, done: true}
```

D'accord, il se passe beaucoup de choses ici. Décomposons cela.

Tout d'abord, nous avons la fonction génératrice, qui génère des tweets en fonction de l'ID utilisateur et du nombre de tweets à générer. Cette fonction retournerait un objet itérateur. Ainsi, c'est ce que `tweetList` est.

```js
> tweetList
generateTweets {<suspended>}
    __proto__: Generator
    [[GeneratorLocation]]: VM2668:1
    [[GeneratorStatus]]: "suspended"
    [[GeneratorFunction]]: ƒ * generateTweets(userID, numberOfTweets)
    [[GeneratorReceiver]]: Window
    [[Scopes]]: Scopes[3]
```

Suspended signifie que le générateur n'est pas encore fermé/terminé. Il y a donc des valeurs qu'il peut fournir. Nous pouvons y accéder via `tweetList.next()` - ce qui nous donnerait un objet avec deux clés, `value` et `done`.

D'un autre côté, les boucles `for...of` comprennent le protocole d'itération, donc elles peuvent itérer sur l'ensemble du générateur par elles-mêmes !

C'est précisément pourquoi nous pouvons faire le `for...of` sur `tweetList` et obtenir nos tweets.

À ce stade, le générateur est terminé. La boucle `for...of` consomme toutes les valeurs.

> Piège courant : Si une instruction break se trouve à l'intérieur de la boucle `for...of`, le générateur se ferme également. Vous ne pouvez donc pas le réutiliser. Voir : [Ne réutilisez pas les générateurs dans les boucles for..of](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of#Iterating_over_generators).

Nous avons ici

```js
> tweetList
generateTweets {<closed>}
    __proto__: Generator
    [[GeneratorLocation]]: VM2668:1
    [[GeneratorStatus]]: "closed"
    [[GeneratorFunction]]: ƒ * generateTweets(userID, numberOfTweets)
    [[GeneratorReceiver]]: Window
```

Ainsi, lorsque nous enregistrons la valeur suivante à la ligne suivante, nous obtenons `done: true` comme nous nous y attendions - et aucune valeur.

C'est tout pour l'exemple.

Mais l'histoire ne s'arrête pas là. Vous pouvez avoir des générateurs qui cèdent à d'autres générateurs également ! Vous faites cela via `yield *`.

```
function * generateTweetsForSomeUsers(users, numberOfTweets) {
    for(let user of users) {
        yield * generateTweets(user, numberOfTweets)
    }
}
```

Les générateurs peuvent également `return` au lieu de `yield`. Cela fait que le générateur se termine.

Eh bien, cela a duré assez longtemps, je pense que je garderai les autres parties intéressantes pour les prochaines parties. Le saviez-vous ? Nous allons nous débarrasser des boucles for une fois pour toutes. Bienvenue dans le monde de Map, Filter et Reduce.

Lisez plus de mes articles de blog sur [neilkakkar.com](https://neilkakkar.com/js-part-2.html).