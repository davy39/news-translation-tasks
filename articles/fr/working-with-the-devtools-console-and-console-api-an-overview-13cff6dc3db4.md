---
title: 'Comment travailler avec la Console DevTools et l''API Console : un aperçu'
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-05-01T22:52:21.000Z'
originalURL: https://freecodecamp.org/news/working-with-the-devtools-console-and-console-api-an-overview-13cff6dc3db4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RCQMBXKwKkafg2vfeTvblQ.png
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: 'Comment travailler avec la Console DevTools et l''API Console : un aperçu'
seo_desc: 'Interested in learning JavaScript? Get my ebook at jshandbook.com


  Every browser exposes a console that lets you interact with the Web Platform APIs
  and gives you an inside look at the code by printing messages that are generated
  by your JavaScript c...'
---

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)

Chaque navigateur expose une console qui vous permet d'interagir avec les [Web Platform APIs](https://flaviocopes.com/web-platform/) et vous donne un aperçu du code en imprimant des messages générés par votre code [JavaScript](https://flaviocopes.com/javascript/) s'exécutant dans la page.

### Aperçu de la console

La barre d'outils de la console est simple. Il y a un bouton pour effacer les messages de la console, ce que vous pouvez également faire en cliquant sur `cmd-K` sous macOS (Mac), ou `ctrl-K` sous Windows (Win).

Un deuxième bouton active une barre latérale de filtrage qui vous permet de filtrer par texte ou par type de message. Vous pouvez filtrer par erreur, avertissement, info, log ou messages de débogage.

Vous pouvez également choisir de masquer les messages générés par le réseau et vous concentrer uniquement sur les messages de log JavaScript.

![Image](https://cdn-media-1.freecodecamp.org/images/wDTPXRKp2UYA6T1fjeG8oRZREJ9gfnCQhGhN)

La console n'est pas seulement un endroit où vous pouvez voir des messages, mais aussi le meilleur moyen d'interagir avec le code JavaScript, et souvent avec le DOM. Ou simplement obtenir des informations de la page.

Tapons notre premier message. Remarquez le `&`gt;.

Cliquons là et tapons :

```
console.log('test')
```

La console agit comme un **REPL**, ce qui signifie read–eval–print loop. En bref, elle interprète notre code JavaScript et imprime quelque chose.

### Utiliser le formatage de console.log

Comme vous le voyez, `console.log('test')` imprime `test` dans la Console.

Utiliser `console.log` dans votre code JavaScript peut vous aider à déboguer, par exemple en imprimant des chaînes statiques. Mais vous pouvez également lui passer une variable, qui peut être un type natif JavaScript, comme un entier ou un objet.

Vous pouvez passer plusieurs variables à `console.log` :

```
console.log('test1', 'test2')
```

Nous pouvons également formater de jolies phrases en passant des variables et un spécificateur de format :

```
console.log("My %s has %d years", 'cat', 2)
```

* `%s` formate une variable en tant que chaîne
* `%d` ou `%i` formate une variable en tant qu'entier
* `%f` formate une variable en tant que nombre à virgule flottante
* `%o` peut être utilisé pour imprimer un élément DOM
* `%O` utilisé pour imprimer une représentation d'objet

Par exemple :

```
console.log("%o, %O", document.body, document.body)
```

![Image](https://cdn-media-1.freecodecamp.org/images/8ODzQol1-tDzsGRZUM8T9CX47e0cUJ87B-DZ)

Un autre spécificateur de format utile est `%c`, qui nous permet de passer du CSS pour formater une chaîne :

```
console.log("%c My %s has %d years", "color: yellow; background:black; font-size: 16pt", "cat", 2)
```

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

### Effacer la console

Il existe trois façons d'effacer la console pendant que vous travaillez dessus, avec diverses méthodes d'entrée.

La première façon est de cliquer sur le bouton **Effacer le journal de la console** dans la barre d'outils de la console.

La deuxième méthode consiste à taper `console.clear()` à l'intérieur de la console, ou dans votre [fonction JavaScript](https://flaviocopes.com/javascript-functions/) qui s'exécute dans votre application / site.

Vous pouvez également simplement taper `clear()`.

La troisième façon est par un raccourci clavier. C'est `cmd-k` (Mac) ou `ctrl + l` (Win).

### Compter les éléments

`console.count()` est une méthode pratique.

Prenons ce code :

```
const x = 1const y = 2const z = 3
```

```
console.count("The value of x is " + x + " and has been checked .. how many times?")console.count("The value of x is " + x + " and has been checked .. how many times?")console.count("The value of y is " + y + " and has been checked .. how many times?")
```

Ce qui se passe, c'est que `count` comptera le nombre de fois qu'une chaîne est imprimée, et imprimera le compte à côté :

![Image](https://cdn-media-1.freecodecamp.org/images/PFfiMSrS0rWwW1Kt-nlzkX4KJcUbZPo764VA)

Vous pouvez simplement compter les pommes et les oranges :

```
const oranges = ['orange', 'orange']const apples = ['just one apple']
```

```
oranges.forEach((fruit) => {  console.count(fruit)})
```

```
apples.forEach((fruit) => {  console.count(fruit)})
```

![Image](https://cdn-media-1.freecodecamp.org/images/PZvOr2UA6q-SAU7ajARWSemhoQPjIzlrfPBD)

### Journaliser des objets plus complexes

`console.log` est assez incroyable pour inspecter des variables. Vous pouvez également lui passer un objet, et il fera de son mieux pour l'imprimer de manière lisible. La plupart du temps, cela signifie qu'il imprime une représentation sous forme de chaîne de l'objet.

Essayons :

```
console.log([1, 2])
```

Une autre option pour imprimer des objets est d'utiliser `console.dir` :

```
console.dir([1, 2])
```

Comme vous pouvez le voir, cette méthode imprime la variable dans une représentation de type JSON, afin que vous puissiez inspecter toutes ses propriétés.

La même chose que ce que `console.dir` produit est réalisable en faisant :

```
console.log("%O", [1,2])
```

![Image](https://cdn-media-1.freecodecamp.org/images/IhPWlFqNWXxtw3C0KdpEJnKNTtj6KrbdZ1oS)

Celui à utiliser dépend de ce que vous devez déboguer, bien sûr. Vous devrez décider lequel des deux peut faire le meilleur travail pour vous.

Une autre fonction est `console.table()` qui imprime un joli tableau.

Nous devons simplement lui passer un tableau d'éléments, et il imprimera chaque élément du tableau dans une nouvelle ligne :

```
console.table([[1,2], ['x', 'y']])
```

Vous pouvez également définir des noms de colonnes, en passant un littéral d'objet au lieu d'un tableau, afin qu'il utilise la propriété de l'objet comme nom de colonne :

```
console.table([{x: 1, y: 2, z: 3}, {x: "First column", y: "Second column", z: null}])
```

![Image](https://cdn-media-1.freecodecamp.org/images/zw4xZy5O9hY2g4kkkmQSCgmCiIVOXKDX1R0b)

`console.table` peut également être plus puissant. Si vous lui passez un littéral d'objet qui contient à son tour un objet, et que vous passez un tableau avec les noms de colonnes, il imprimera un tableau avec les index de ligne pris à partir du littéral d'objet.

Par exemple :

```
const shoppingCart = {}
```

```
shoppingCart.firstItem  = {'color': 'black', 'size': 'L'}shoppingCart.secondItem = {'color': 'red',   'size': 'L'}shoppingCart.thirdItem  = {'color': 'white', 'size': 'M'}
```

```
console.table(shoppingCart, ["color", "size"])
```

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

### Journaliser différents niveaux d'erreur

Comme nous l'avons vu, console.log est idéal pour imprimer des messages dans la Console.

Nous allons maintenant découvrir trois autres méthodes pratiques qui nous aideront à déboguer, car elles indiquent implicitement divers niveaux d'erreur.

**console.info()**  
Comme vous pouvez le voir, un petit 'i' est imprimé à côté, indiquant clairement que le message de log est juste une information.

**console.warn()**  
Imprime un point d'exclamation jaune.

Si vous activez la barre d'outils de filtrage de la Console, vous pouvez voir que la Console vous permet de filtrer les messages en fonction du type, il est donc vraiment pratique de différencier les messages. Par exemple, si nous cliquons maintenant sur 'Avertissements', tous les messages imprimés qui ne sont pas des avertissements seront masqués.

**console.error()**  
Cela est un peu différent des autres, car en plus d'imprimer une croix rouge qui indique clairement qu'il y a une erreur, nous avons la trace de la pile complète de la fonction qui a généré l'erreur. Nous pouvons ensuite aller essayer de la corriger.

![Image](https://cdn-media-1.freecodecamp.org/images/S8jw2S-p8xUE4qAwtPP3kPx0q-Ck1tSb1f3T)

Les messages de la console sont effacés à chaque navigation de page, sauf si vous cochez **Préserver le journal** dans les paramètres de la console :

![Image](https://cdn-media-1.freecodecamp.org/images/8GvRXSsX4Ov46TjaYqPsHxcBcBAClp5tVC5v)

### Regrouper les messages de la console

Les messages de la Console peuvent augmenter en taille, et le bruit lorsque vous essayez de déboguer une erreur peut être écrasant.

Pour limiter ce problème, l'API Console offre une fonctionnalité pratique : le regroupement des messages de la Console.

Faisons d'abord un exemple :

```
console.group("Testing the location") 
```

```
console.log("Location hash", location.hash) console.log("Location hostname", location.hostname) console.log("Location protocol", location.protocol) 
```

```
console.groupEnd()
```

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Comme vous pouvez le voir, la Console crée un groupe, et nous avons les messages de log.

Vous pouvez faire de même, mais afficher un message réduit que vous pouvez ouvrir à la demande pour limiter davantage le bruit :

```
console.groupCollapsed("Testing the location") 
```

```
console.log("Location hash", location.hash) console.log("Location hostname", location.hostname) console.log("Location protocol", location.protocol) 
```

```
console.groupEnd()
```

![Image](https://cdn-media-1.freecodecamp.org/images/NhtoHr1zrCDGaHZwSLpxhNiHpGDpSqCqdZ-S)

L'avantage est que ces groupes peuvent être imbriqués, vous pouvez donc finir par faire :

```
console.group("Main")console.log("Test")console.group("1")console.log("1 text")console.group("1a")console.log("1a text")console.groupEnd()console.groupCollapsed("1b")console.log("1b text")console.groupEnd()console.groupEnd()
```

![Image](https://cdn-media-1.freecodecamp.org/images/ZQRjpr0JPl3EplgTZrshyZxr0q2WzStZyoxF)

### Imprimer la trace de la pile

Il peut y avoir des cas où il est utile d'imprimer la trace de la pile d'appels d'une fonction, peut-être pour répondre à la question : « Comment avez-vous atteint cette partie du code ? »

Vous pouvez le faire en utilisant `console.trace()` :

```
const function2 = () => console.trace() const function1 = () => function2() function1()
```

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

### Calculer le temps écoulé

Vous pouvez facilement calculer combien de temps une fonction met à s'exécuter, en utilisant `time()` et `timeEnd()`.

```
const doSomething = () => console.log('test')const measureDoingSomething = () => {  console.time('doSomething()')  //faire quelque chose, et mesurer le temps que cela prend  doSomething()  console.timeEnd('doSomething()')}measureDoingSomething()
```

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

### Générer un profil CPU

Les DevTools vous permettent d'analyser les performances du profil CPU de n'importe quelle fonction.

Vous pouvez démarrer cela manuellement. Mais la manière la plus précise de le faire est d'encadrer ce que vous voulez surveiller entre les commandes `profile()` et `profileEnd()`.

Elles sont similaires à `time()` et `timeEnd()`, sauf qu'elles ne mesurent pas seulement le temps, mais créent un rapport plus détaillé :

```
const doSomething = () => console.log('test')const measureDoingSomething = () => {  console.profile("doSomething()")  //faire quelque chose, et mesurer ses performances  doSomething()  console.profileEnd()}measureDoingSomething()
```

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

> Intéressé par l'apprentissage de JavaScript ? Obtenez mon ebook sur [jshandbook.com](https://jshandbook.com/)