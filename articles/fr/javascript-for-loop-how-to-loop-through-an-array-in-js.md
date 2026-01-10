---
title: Boucle For JavaScript – Comment parcourir un tableau en JS
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-08-03T19:53:47.000Z'
originalURL: https://freecodecamp.org/news/javascript-for-loop-how-to-loop-through-an-array-in-js
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/srinivas-jd-PtpB2jiakOE-unsplash.jpg
tags:
- name: arrays
  slug: arrays
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Boucle For JavaScript – Comment parcourir un tableau en JS
seo_desc: 'There are various types of loops in JavaScript, and all of them essentially
  do the same thing: they repeat an action again and again.

  Loops come in handy if you want to repeat the same block of code for a certain number
  of times. Basically, they are ...'
---

Il existe différents types de boucles en JavaScript, et elles font toutes essentiellement la même chose : elles répètent une action encore et encore.

Les boucles sont utiles si vous souhaitez répéter le même bloc de code un certain nombre de fois. Basiquement, elles sont un moyen rapide et efficace de répéter quelque chose.

Cet article se concentre sur la boucle `for` dans le langage de programmation JavaScript et passe en revue sa syntaxe de base.

De plus, j'expliquerai comment parcourir un tableau en utilisant une boucle `for`, ce qui est un concept fondamental en programmation.

## Qu'est-ce qu'une boucle for ? Une analyse de la syntaxe de base

Une boucle `for` répète une action tant qu'une condition spécifique est `true`. Elle arrête de répéter l'action lorsque la condition évalue finalement à `false`.

Une boucle `for` en JavaScript ressemble beaucoup à une boucle `for` en C et Java.

Il existe de nombreux types différents de boucles `for` en JavaScript, mais les plus basiques ressemblent à ceci :

```
for( initialisation de l'expression; condition; action pour l'expression initialisée ) {
  instruction à exécuter;
}
```

Ce type de boucle commence par le mot-clé `for`, suivi d'une paire de parenthèses. À l'intérieur, il y a trois expressions *optionnelles* séparées par un point-virgule, `;`. Enfin, il y a une paire d'accolades, `{}`, qui enferme l'instruction du bloc de code à exécuter.

Voici un exemple :

```Javascript
for (let i = 0; i < 10; i++) {
  console.log('Compter les nombres');
  // exécute et imprime "Compter les nombres" 10 fois
  // les valeurs de i vont de 0 à 9 
  }
```

Plus en détail, lorsqu'une boucle `for` est exécutée :

- Si une expression initiale est présente, elle est exécutée une seule fois avant que le code du bloc ne soit exécuté et avant que la boucle ne commence. Dans cette étape, il y a une initialisation d'un ou plusieurs compteurs et une déclaration d'une ou plusieurs variables utilisées dans la boucle, comme `let i =0`. Si plusieurs variables sont présentes, elles sont séparées par des virgules. 
- Ensuite, il y a la définition de l'expression de condition qui doit être remplie pour que la boucle s'exécute, `i < 10`. Comme mentionné précédemment, les instructions du bloc de code s'exécuteront uniquement lorsque cette condition évaluera à `true`. Si la valeur est `false`, la boucle arrête de s'exécuter. Si aucune condition n'est présente, elle est toujours `true`, ce qui crée une *boucle infinie*.
- Ensuite, l'instruction à l'intérieur du bloc avec les accolades, `{..}`, est exécutée. Il peut y en avoir plusieurs, sur plusieurs lignes.
- Après chaque exécution du bloc de code, il peut y avoir une action pour l'expression initialisée qui a lieu à la fin, comme une instruction d'incrémentation (`i++`) qui met à jour l'expression initiale.
- Après cela, la condition est vérifiée à nouveau et si elle évalue à `true`, le processus est répété.

## Qu'est-ce qu'un tableau ?

Un tableau est une structure de données.

C'est une collection ordonnée de plusieurs éléments, appelés éléments, sous le même nom stockés ensemble dans une liste. Cela permet ensuite de les trier ou de les rechercher facilement.

Les tableaux en JavaScript peuvent contenir des éléments avec des valeurs de différents types de données. Un tableau peut contenir des nombres, des chaînes de caractères, un autre tableau, des valeurs booléennes, et plus encore – en même temps.

L'indexation commence toujours à `0`. Cela signifie que le premier élément d'un tableau est référencé avec un index zéro, le deuxième élément a un index un, et le dernier élément est `longueur du tableau - 1`.

Le moyen le plus simple et le plus préférable de créer un tableau est avec la *notation littérale de tableau*, que vous pouvez faire avec des crochets contenant une liste d'éléments séparés par des virgules, comme le tableau de chaînes de caractères ci-dessous :

```Javascript
let programmingLanguages = ["JavaScript","Java","Python","Ruby"];
```

Pour accéder au premier élément, nous utilisons le numéro d'index :

```JavaScript
console.log(programmingLanguages[0]);
// imprime JavaScript
```

## Comment parcourir un tableau avec une boucle for

Chaque fois que la boucle `for` s'exécute, elle a une valeur différente – et c'est le cas avec les tableaux.

Une boucle for examine et parcourt chaque élément que le tableau contient de manière rapide, efficace et plus contrôlable.

Un exemple de base de parcours d'un tableau est :

```JavaScript

const myNumbersArray = [1, 2, 3, 4, 5];

for(let i = 0; i < myNumbersArray.length; i++) {
    console.log(myNumbersArray[i]);
}
```

Sortie :
```
1
2
3
4
5
```

Cela est beaucoup plus efficace que d'imprimer chaque valeur individuellement :

```javascript
console.log(myNumbersArray[0]);
console.log(myNumbersArray[1]);
console.log(myNumbersArray[2]);
console.log(myNumbersArray[3]);
console.log(myNumbersArray[4]);
```

Décomposons cela :

La variable d'itération `i` est initialisée à 0. `i` dans ce cas fait référence à l'accès à l'index du tableau. Cela signifie que la boucle accédera à la première valeur du tableau lorsqu'elle s'exécutera pour la première fois.

La condition `i < myNumbersArray.length` indique à la boucle quand s'arrêter, et l'instruction d'incrémentation `i++` indique de combien incrémenter la variable d'itération pour chaque boucle.

En d'autres termes, la boucle commence à l'`index 0`, vérifie la longueur du tableau, imprime la valeur à l'écran, puis augmente la variable de 1. La boucle imprime le contenu du tableau un par un et lorsqu'elle atteint sa longueur, elle s'arrête.

## Conclusion

Cet article a couvert les bases pour commencer avec les boucles `for` en JavaScript. Nous avons appris comment parcourir des tableaux en utilisant cette méthode, qui est l'une des plus courantes que vous utiliserez lorsque vous commencez à apprendre le langage.

Si vous souhaitez en savoir plus sur les autres méthodes de tableau en JavaScript, vous pouvez [tout lire à ce sujet ici](https://www.freecodecamp.org/news/complete-introduction-to-the-most-useful-javascript-array-methods/).

Merci d'avoir lu et bon codage !