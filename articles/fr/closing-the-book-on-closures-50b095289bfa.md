---
title: Fermer le livre sur les fermetures
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-10-30T12:56:58.000Z'
originalURL: https://freecodecamp.org/news/closing-the-book-on-closures-50b095289bfa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*l0PQ97Jq6F1NbCvTmuMqWQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Fermer le livre sur les fermetures
seo_desc: 'By William Countiss

  JavaScript closures are an important, but notoriously confusing concept. There’s
  no escaping it — if you want to grow as a developer, you need to understand what
  closures are and how to use them.

  Don’t let the fancy name scare you...'
---

Par William Countiss

Les fermetures JavaScript sont un concept important, mais notoirement confus. Il n'y a pas moyen d'y échapper — si vous voulez grandir en tant que développeur, vous devez comprendre ce que sont les fermetures et comment les utiliser.

Ne laissez pas le nom fantaisiste vous effrayer — une fois que vous aurez un peu joué avec les fermetures, vous réaliserez qu'il n'y a vraiment pas grand-chose à comprendre.

Commençons par quelque chose de simple :

```
  1 function sayGreeting(greeting) {  2  3     return function(name) {  4  5         console.log(greeting + " " + name);  6     }  7  8 }
```

Vous remarquerez tout de suite que notre fonction, **sayGreeting**, retourne une autre fonction. Je peux faire cela en JavaScript parce que les fonctions sont considérées comme **_de première classe_**, ce qui signifie qu'elles peuvent être passées comme n'importe quel autre type de données, comme un nombre, une chaîne de caractères ou un booléen. Cela peut donner une syntaxe intéressante :

```
  1 function sayGreeting (greeting) {  2  3     return function (name) {  4  5         console.log (greeting + " " + name);  6     }  7  8 }  9 sayGreeting("Hello")("William");
```

Alors, que pensez-vous voir dans la console lorsque nous exécutons ce code ? Réfléchissez-y un instant, puis regardez l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MhLMnx7HjUuYunG3ohethw.png)

Si vous avez deviné « Hello William », vous avez raison. Allez-y et donnez-vous une tape dans le dos. Maintenant, examinons de plus près _pourquoi_.

```
sayGreeting("Hello")("William");
```

Rappelez-vous que sayGreeting **retourne** une fonction. Comme nous l'avons mentionné précédemment, les fonctions en JavaScript sont de première classe et peuvent être passées comme n'importe quelle autre structure de données. Ainsi, lorsque **sayGreeting("Hello") est invoquée** pour la première fois, elle s'exécute et retourne une fonction anonyme. Une fonction retournée peut également être invoquée, et c'est pourquoi vous voyez le second ensemble de parenthèses : sayGreeting("Hello")**("William")**

Pour rendre cela un peu plus facile à suivre, modifions un peu le code en attribuant la première invocation à une variable :

```
  1 function sayGreeting (greeting) {  2  3     return function(name) {  4  5         console.log(greeting + " " + name);  6     }  7  8 }  9 10 var sayHello = sayGreeting("Hello"); 11 sayHello("William");
```

Si vous exécutez cela dans votre console, vous obtiendrez le même résultat qu'avant. Mais comment sayHello("William") connaît-il la valeur du paramètre **greeting** de la fonction **sayGreeting** ? Pour comprendre cela, nous devons approfondir un peu.

Chaque fois qu'une fonction est invoquée, de la mémoire est réservée pour cette fonction et son contenu, qui persistent même après que la fonction a fini de s'exécuter. Nous pouvons visualiser cela en enveloppant la variable **sayHello** avec un **console.dir()**

```
  1 function sayGreeting(greeting) {  2  3     return function(name) {  4  5         console.log(greeting + " " + name);  6     }  7  8 }  9 10 var sayHello = sayGreeting("Hello"); 11 12 console.dir(sayHello); 13 sayHello("William");
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*xx14GLxJtxjbE0KpHwjrDw.png)

Vous verrez dans la console que la variable **sayHello** est une fonction anonyme, et dans sa portée, il y a une **fermeture** avec une paire **nom:valeur**,

**greeting: "Hello"**

Cela devrait vous sembler familier puisque "greeting" est le nom du paramètre de la fonction sayGreeting(greeting) { … } à la ligne 1, et "Hello" était la chaîne que nous avons passée lorsque nous avons invoqué la fonction pour la première fois à la ligne 10. De la mémoire a ensuite été réservée pour ces valeurs et est disponible en tant que **référence externe** lorsque nous invoquons la fonction à la ligne 13.

Pour aider à visualiser cela, écrivons le corps de la fonction **sayHello** tel qu'il est exécuté à la ligne 13.

```
  1 function (name) {  2  3     console.log (greeting + " " + name);  4 }
```

La chaîne "William" est passée pour le paramètre name, puis à la ligne 3, console.log(**greeting** + " " + **name**) est exécutée.

Elle recherche ensuite les valeurs de **greeting** et **name**.

Notre fonction trouve une valeur pour **name** : "William". Mais elle n'a pas de valeur pour **greeting**. Il est donc temps d'aller pêcher, et elle regarde sa référence externe (où elle se situe en termes de portée lexicale) dans une tentative de trouver une valeur pour greeting.

En d'autres termes, elle se souvient où elle a été explicitement écrite dans le code, qui est **à l'intérieur** de la fonction sayGreeting.

```
  1 function sayGreeting(greeting) {  2  3     return function(name) {  4  5         console.log(greeting + ' ' + name);  6     }  7  8 }
```

Lorsque la fonction trouve la valeur de **greeting** dans sa référence externe, nous appelons cela **fermer** une variable externe, et lorsque cela se produit, vous avez une **fermeture**.

Ce n'était pas si mal, n'est-ce pas ?

Ceci est un exemple très basique, mais même dans des applications complexes, les règles restent les mêmes. Chaque fois qu'une fonction ne peut pas trouver la valeur de quelque chose en elle-même, elle suivra la chaîne de portée jusqu'au bout (ou vers le haut, selon la manière dont vous l'envisagez) et recherchera cette valeur pour créer la fermeture.