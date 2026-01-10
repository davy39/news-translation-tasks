---
title: La récursivité en JavaScript expliquée à l'aide d'un défi freeCodeCamp
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-08T20:51:53.000Z'
originalURL: https://freecodecamp.org/news/learn-recursion-in-javascript-by-example
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/Marketing-Business-Corporate-Start-up-Facebook-Cover--1--1.png
tags:
- name: freeCodeCamp.org
  slug: freecodecamp
- name: JavaScript
  slug: javascript
- name: Recursion
  slug: recursion
seo_title: La récursivité en JavaScript expliquée à l'aide d'un défi freeCodeCamp
seo_desc: "By Nehemiah Kivelevitz\nIn this article I will touch on a few important\
  \ ideas to help you understand Recursion in JavaScript. I’m not going to give a\
  \ full definition here, but you can take a look at what Wikipedia has to say. \n\
  Let’s agree for the purp..."
---

Par Nehemiah Kivelevitz

Dans cet article, je vais aborder quelques idées importantes pour vous aider à comprendre la récursivité en JavaScript. Je ne vais pas donner une définition complète ici, mais vous pouvez consulter ce que Wikipedia [en dit](https://en.wikipedia.org/wiki/Recursion_%28computer_science%29). 

Mettons-nous d'accord pour les besoins de cet article que nous essayons de résoudre un problème en utilisant une fonction qui s'appellera ensuite elle-même.

## Le Défi

À la fin de la section Algorithmes et Structures de Données JavaScript — JavaScript de Base [sur freeCodeCamp](https://www.freecodecamp.org/learn/), vous tombez sur un problème intéressant : « Utiliser la Récursivité pour Créer une Plage de Nombres », où les instructions sont les suivantes :

> Nous avons défini une fonction nommée rangeOfNumbers avec deux paramètres. La fonction doit retourner un tableau d'entiers qui commence par un nombre représenté par le paramètre startNum et se termine par un nombre représenté par le paramètre endNum. Le nombre de départ sera toujours inférieur ou égal au nombre de fin. Votre fonction doit utiliser la récursivité en s'appelant elle-même et ne pas utiliser de boucles de quelque sorte que ce soit. Elle doit également fonctionner pour les cas où startNum et endNum sont identiques.

Cela semble assez simple — si vous exécutez rangeOfNumbers(1, 5), cela devrait retourner [1, 2, 3, 4, 5].

Si vous êtes comme moi, vous pouvez plus ou moins intuiter la réponse en vous basant sur l'exemple précédent de cette section. Mais cela peut encore être un peu flou de comprendre comment tout cela fonctionne.

**Alerte spoiler :** vous trouverez une réponse immédiatement ci-dessous. Mais ce n'est pas vraiment un spoiler puisque la réponse est assez facile à trouver sur Internet.

## Ma Solution

Il est très probable que vous puissiez lire le code et comprendre que lorsqu'il atteint son **cas de base**, il retournera la valeur de startNum dans le tableau. Ensuite, il continuera à ajouter les autres valeurs à ce tableau jusqu'à ce qu'il ait terminé toutes ses appels récursifs.

```javascript
function rangeOfNumbers(startNum, endNum) {
    if (startNum === endNum) {
        return [startNum];
    } else {       
        const numbers = rangeOfNumbers(startNum, endNum - 1);
        numbers.push(endNum);
        return numbers;
    }
}
```

Ce que j'ai trouvé délicat, c'est de comprendre exactement **comment** la pile d'appels fonctionnait et comment mes valeurs étaient retournées.

Alors, décomposons comment cette fonction retournera sa valeur finale.

### La Pile d'Appels

La première chose à comprendre est le fonctionnement de la **pile d'appels**. Je vous renvoie à l'explication du Mozilla Developer Network :

> Lorsque qu'un script appelle une fonction, l'interpréteur l'ajoute à la pile d'appels et commence à exécuter la fonction.  
>   
> Toute fonction appelée par cette fonction est ajoutée plus haut dans la pile d'appels et est exécutée lorsque ses appels sont atteints.  
>   
> Lorsque la fonction actuelle est terminée, l'interpréteur la retire de la pile et reprend l'exécution là où il s'était arrêté dans la dernière liste de code.

En utilisant cette explication, exécutons le code ci-dessus en utilisant _rangeOfNumbers(1,5)._

Tout d'abord, le contexte d'exécution rangeOfNumbers est créé et exécuté avec les valeurs suivantes :

![capture d'écran du code](https://www.freecodecamp.org/news/content/images/2020/06/numberrange.png)
_Capture d'écran de [http://www.pythontutor.com/javascript.html](http://www.pythontutor.com/javascript.html" data-href="http://www.pythontutor.com/javascript.html" class="markup--anchor markup--figure-anchor" rel="noopener" target="_blank)_

Nous avons donc ajouté un appel de fonction non résolu _rangeOfNumbers(1,5)_ à notre pile. Ensuite, nous passons à la création de l'exécution pour _rangeOfNumbers(1,4)_, et ainsi de suite, ajoutant chacun de ces appels à notre pile jusqu'à ce que nous **résolvions** enfin un appel de fonction. Ensuite, l'interpréteur retirera cette fonction de la pile et passera à la suivante.

### Examen de Notre Pile d'Appels

Notre pile finira par ressembler à ceci :

```
rangeOfNumbers(1,1)
rangeOfNumbers(1,2)
rangeOfNumbers(1,3)
rangeOfNumbers(1,4)
rangeOfNumbers(1,5)
```

_rangeOfNumbers(1,1)_ sera le dernier dans notre pile car, enfin, cet appel **RETOURNERA** une valeur nous permettant de passer à la fonction suivante dans la pile.

La valeur de retour de _rangeOfNumbers(1,1)_ est [1], comme nous l'avions supposé puisque c'est notre cas de base. Maintenant, nous retirons _rangeOfNumbers(1,1)_ de notre pile et retournons là où _rangeOfNumbers(1,2)_ s'était arrêté...

```
var numbers = rangeOfNumbers(1,2) // retourne un tableau de [1]
```

Numbers n'est plus _undefined_ et l'étape suivante consiste à ajouter le _endNum_, qui est 2, dans le tableau numbers. Cela nous donne [1,2] dans numbers, et maintenant nous retournons la valeur.

```
numbers.push(endNum) //numbers contient maintenant un tableau de [1,2]
return numbers; // termine notre fonction et retourne [1,2]
```

### Décomposition de la Partie Délicate

Nous retirons donc _rangeOfNumbers(1,2)_ qui avait une valeur de retour de [1,2]. Reprenons avec l'appel suivant dans notre pile _rangeOfNumbers(1,3)._ Numbers est actuellement [1,2] car c'est la valeur de retour de _rangeOfNumbers(1,2)._ C'est ce que nous avions inséré lorsque nous avons appelé _rangeOfNumbers(1,3)_ car, encore une fois, le 3 est soustrait de 1, c'est-à-dire _rangeOfNumbers(1,2)_, qui, comme nous l'avons dit, retourne [1,2]. 

Vous avez compris ? Super ! Si ce n'est pas le cas, relisez ce paragraphe, car c'est la partie la plus délicate à comprendre.

Si vous êtes à jour, continuons. Si la partie ci-dessus a fait tilt, le reste devrait sembler assez facile.

Retour à _rangeOfNumbers(1,3)_ : le tableau numbers est actuellement [1,2], donc nous ajoutons le _endNum_ qui est 3. Maintenant nous avons [1,2,3] et nous retournons cette valeur à nouveau. Nous retirons _rangeOfNumbers(1,3)_ de notre pile qui a retourné la valeur [1,2,3]. 

Comment avons-nous obtenu rangeOfNumbers(1,3) ? C'est exact, lorsque nous avons appelé _rangeOfNumbers(1,4)_ et endNum -1, c'est-à-dire → 3, et nous savons que _rangeOfNumbers(1,3)_ nous donne la valeur de retour [1,2,3] qui est exactement ce que nous avons dans notre tableau. 

Maintenant, nous ajoutons le _endNum (aussi connu sous le nom de 4)_ au tableau numbers, ce qui nous donne [1,2,3,4] et nous retournons cette valeur. Retirons à nouveau cet appel de fonction de la pile puisqu'il nous a donné ce que nous voulions.

### Mettre le tout ensemble 

Maintenant pour l'appel qui a tout commencé : _rangeOfNumbers(1,5)_. La première étape que nous faisons est de déterminer quelle valeur nous avons dans numbers. Lorsque nous mettons _rangeOfNumbers(1,4)_, nous obtenons, comme nous l'avons dit auparavant, [1,2,3,4]. Nous pouvons donc maintenant ajouter notre _endNum_ 5 dans le tableau et obtenir [1,2,3,4,5] que nous allons retourner, et notre pile est maintenant vide avec notre dernier appel.

Alors, faisons un rapide récapitulatif de ce qui a retourné quelle valeur et dans quel ordre.

```
rangeOfNumbers(1,1) → retourne [1]
rangeOfNumbers(1,2) → retourne [1,2]
rangeOfNumbers(1,3) → retourne [1,2,3]
rangeOfNumbers(1,4) → retourne [1,2,3,4]
rangeOfNumbers(1,5) → retourne [1,2,3,4,5]
```

Si cela reste confus, premièrement je comprends — c'est un sujet confus. Ensuite, je vous recommande de taper votre code dans cet excellent outil : [http://www.pythontutor.com/javascript.html](http://www.pythontutor.com/javascript.html)

Tout cela est possible car nous avons commencé avec un petit cas de base et nous avons essentiellement construit notre chemin en arrière. Chaque fois, notre valeur de retour est un peu plus grande que lors de son appel précédent, un peu comme si vous effectuiez cette même opération avec une boucle for.

Vous avez des questions ? N'hésitez pas à me demander sur Twitter : [@NehemiahK](https://twitter.com/NehemiahKiv)iv