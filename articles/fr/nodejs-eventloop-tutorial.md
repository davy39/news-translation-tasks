---
title: Boucles d'événements dans NodeJS – Guide du débutant pour le code synchrone
  et asynchrone
subtitle: ''
author: Tejan Singh
co_authors: []
series: null
date: '2021-08-30T15:11:16.000Z'
originalURL: https://freecodecamp.org/news/nodejs-eventloop-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/oliver-hale-2cYueJxEDz8-unsplash.jpg
tags:
- name: asynchronous programming
  slug: asynchronous-programming
- name: JavaScript
  slug: javascript
- name: node
  slug: node
seo_title: Boucles d'événements dans NodeJS – Guide du débutant pour le code synchrone
  et asynchrone
seo_desc: "NodeJS is an asynchronous event-driven JavaScript runtime environment designed\
  \ to build scalable network applications. \nAsynchronous here refers to all those\
  \ functions in JavaScript that are processed in the background without blocking\
  \ any other requ..."
---

NodeJS est un environnement d'exécution JavaScript asynchrone piloté par événements, conçu pour construire des applications réseau scalables. 

Asynchrone fait ici référence à toutes ces fonctions en JavaScript qui sont traitées en arrière-plan sans bloquer aucune autre requête.

Dans cet article, vous apprendrez et comprendrez comment NodeJS fonctionne et gère toutes les fonctions ou requêtes envoyées à un serveur, soit de manière *synchrone* soit *asynchrone*. 

## Qu'est-ce qu'une boucle d'événements ?

Vous l'avez peut-être deviné – Node gère les requêtes en utilisant une **boucle d'événements** à l'intérieur de l'environnement NodeJS. Mais d'abord, comprenons quelques termes de base qui nous aideront à comprendre tout le mécanisme.

Une boucle d'événements est un **écouteur d'événements** qui fonctionne à l'intérieur de l'environnement NodeJS et est toujours prêt à écouter, traiter et produire un résultat pour un *événement*.

Un événement peut être n'importe quoi, d'un clic de souris à une pression de touche ou un délai d'attente.

## Qu'est-ce que la programmation synchrone et asynchrone ?

La **programmation synchrone** signifie que le code s'exécute dans la séquence où il est défini. Dans un programme synchrone, lorsqu'une fonction est appelée et a retourné une valeur, seulement alors la ligne suivante sera exécutée.

Comprenons avec cet exemple :

```js
const listItems = function(items) {
  items.forEach(function(item) {
    console.log(item)
  })
}

const items = ["Acheter du lait", "Acheter du café"]

listItems(items)
```

```
La sortie ressemblera à ceci :

"Acheter du lait"
"Acheter du café"

```

Dans cet exemple, lorsque la fonction `listItems(items)` est appelée, elle parcourt le tableau d'articles. La fonction `console.log(item)` est d'abord appelée pour le premier article du tableau et imprime `"Acheter du lait"`. Ensuite, `console.log(item)` est à nouveau exécutée et cette fois, elle passe le deuxième article du tableau et imprime `"Acheter du café"`.

Ainsi, vous pouvez dire que la fonction a été exécutée dans la **séquence** où elle a été définie.

La **programmation asynchrone**, en revanche, fait référence à un code qui ne s'exécute pas en séquence. Ces fonctions ne sont pas exécutées selon la séquence dans laquelle elles sont définies à l'intérieur d'un programme, mais seulement lorsque certaines conditions sont remplies. 

Par exemple, `setTimeOut()` effectue une tâche après un délai d'un certain nombre de millisecondes prédéfinies.

```js
setTimeOut(function(){
    return( console.log("Bonjour le monde !") )
}, 3000)
```

Ces fonctions ne s'exécutent pas ligne par ligne, mais seulement lorsqu'elles doivent s'exécuter, indépendamment de la déclaration de la fonction. Dans ce cas, la fonction s'exécute automatiquement après 3 secondes lorsque toutes les fonctions synchrones ont été exécutées.

*Note : Les fonctions asynchrones s'exécuteront et seront exécutées uniquement après que toutes les fonctions synchrones aient été exécutées. Jusqu'à ce moment, elles seront traitées en arrière-plan.*

Si vous souhaitez en savoir plus sur NodeJS et la programmation asynchrone, vous pouvez vous référer à cet [article](https://www.freecodecamp.org/news/node-js-what-when-where-why-how-ab8424886e2/)

Mais comment NodeJS gère-t-il les fonctions asynchrones en arrière-plan et exécute-t-il toutes les fonctions synchrones en premier ? Tous ces mécanismes peuvent être facilement expliqués avec la boucle d'événements de NodeJS.

## Comment fonctionne une boucle d'événements ?
Maintenant, voyons comment les boucles d'événements de NodeJS peuvent exécuter un programme synchrone simple en utilisant un diagramme de boucle d'événements NodeJS. Ensuite, nous examinerons comment Node exécute le programme ligne par ligne.

Au fur et à mesure que nous parcourons cette section, vous commencerez à comprendre ce que vous voyez ici :
![1](https://www.freecodecamp.org/news/content/images/2021/08/1.PNG)

Dans le coin supérieur gauche, vous avez un fichier Node qui va être exécuté. En bas à gauche, vous avez un terminal de sortie pour le programme. Ensuite, vous avez *Pile d'appels, API Node et File d'attente de rappels.* Tous ces éléments constituent ensemble l'environnement NodeJS.

Pour la programmation synchrone, vous devez vous concentrer uniquement sur la pile d'appels. C'est la seule partie de l'environnement NodeJS qui fonctionnera dans ce cas.

Une pile de rappels est une structure de données que vous utilisez pour suivre l'exécution de toutes les fonctions qui s'exécuteront à l'intérieur du programme. Cette structure de données n'a qu'une seule extrémité ouverte pour ajouter ou supprimer les éléments du haut.

Lorsque le programme commence à s'exécuter, il est d'abord enveloppé dans une fonction anonyme `main()`. Cela est automatiquement défini par NodeJS. Ainsi, `main()` est d'abord poussé dans la pile de rappels.

![2](https://www.freecodecamp.org/news/content/images/2021/08/2.PNG)

Ensuite, les variables `a` et `b` sont créées et leur somme est stockée dans une variable `sum`. Toutes ces valeurs sont stockées en mémoire. 

Maintenant, `console.log()` est une fonction qui est appelée et poussée à l'intérieur de la pile de rappels. Elle est exécutée et vous pouvez voir la sortie sur l'écran du terminal.

![3](https://www.freecodecamp.org/news/content/images/2021/08/3.PNG)

Après que cette fonction soit exécutée, elle est supprimée de la pile de rappels. Ensuite, `main()` est également supprimé car il ne reste plus rien à appeler depuis le programme. C'est ainsi qu'un programme synchrone est exécuté.

![4](https://www.freecodecamp.org/news/content/images/2021/08/4.PNG)
![5](https://www.freecodecamp.org/news/content/images/2021/08/5.PNG)

Maintenant, voyons comment les fonctions ou programmes asynchrones sont exécutés à l'intérieur de NodeJS. Nous avons besoin de la pile de rappels, des API Node et de la file d'attente de rappels pour traiter une fonction asynchrone.

Commençons par regarder cet exemple :

![1-1](https://www.freecodecamp.org/news/content/images/2021/08/1-1.PNG)

Comme d'habitude, lorsque le programme commence à s'exécuter, la fonction `main()` est d'abord ajoutée à la pile de rappels. Ensuite, `console.log("Start")` est appelée et ajoutée à la pile de rappels. Après le traitement, la sortie est visible sur le terminal et elle est ensuite supprimée de la pile de rappels. 

![2-1](https://www.freecodecamp.org/news/content/images/2021/08/2-1.PNG)
![3-1](https://www.freecodecamp.org/news/content/images/2021/08/3-1.PNG)

Maintenant, la fonction `setTimeOut(...Zero...)` est ajoutée à la pile de rappels. 

Étant donné que c'est une fonction asynchrone, elle **ne** sera **pas** traitée dans la pile de rappels. Elle est ensuite ajoutée de la pile de rappels aux API Node où un événement est enregistré et une fonction de rappel est définie pour être traitée en arrière-plan. 

![4-1](https://www.freecodecamp.org/news/content/images/2021/08/4-1.PNG)
![5-1](https://www.freecodecamp.org/news/content/images/2021/08/5-1.PNG)

Ensuite, c'est au tour de `setTimeOut(...Two..)` qui est également ajouté aux API Node depuis la pile de rappels car c'est une fonction asynchrone. Ensuite, une autre fonction de rappel est définie pour être traitée après un délai de 2 secondes en arrière-plan. Jusqu'à ce point, d'autres fonctions peuvent être exécutées. 

Cela s'appelle un comportement **non bloquant** où toutes les fonctions synchrones sont traitées et exécutées en premier et les fonctions asynchrones sont traitées en arrière-plan en attendant leur tour pour être exécutées.

![6](https://www.freecodecamp.org/news/content/images/2021/08/6.PNG)
![7](https://www.freecodecamp.org/news/content/images/2021/08/7.PNG)

Ensuite, la fonction `console.log("End")` est appelée en dernier dans la pile de rappels et est traitée ici. Vous pouvez voir la sortie sur le terminal. Maintenant, toutes les fonctions synchrones sont traitées, et `main()` est supprimé de la pile de rappels.

En arrière-plan, toutes les fonctions asynchrones sont traitées et leurs rappels sont stockés dans la file d'attente de rappels. Celle qui est traitée en premier sera ajoutée en premier dans la file d'attente pour l'exécution dans la pile de rappels.

![8](https://www.freecodecamp.org/news/content/images/2021/08/8.PNG)
![9](https://www.freecodecamp.org/news/content/images/2021/08/9.PNG)
![10](https://www.freecodecamp.org/news/content/images/2021/08/10.PNG)

*Note : Les fonctions asynchrones ne peuvent pas s'exécuter à l'intérieur d'une pile de rappels tant qu'elle n'est pas vidée. Cela signifie qu'après que `main()` est supprimé de la pile d'appels, seules les fonctions asynchrones peuvent commencer à s'exécuter.*

Maintenant, une par une, elles sont poussées dans la pile de rappels en utilisant la **boucle d'événements** et sont finalement exécutées. Chacune des fonctions de rappel imprimera la valeur avec la fonction `console.log()` appelée à chaque fois.

![11](https://www.freecodecamp.org/news/content/images/2021/08/11.PNG)

Enfin, celles-ci sont également supprimées après avoir été exécutées et maintenant la pile de rappels est vide.

![12](https://www.freecodecamp.org/news/content/images/2021/08/12.PNG)

C'est ainsi que NodeJS exécutera les fonctions synchrones et asynchrones à l'intérieur de l'environnement et comment la boucle d'événements parvient à appeler les fonctions asynchrones.

## Conclusion
Dans cet article, vous avez appris le fonctionnement interne de NodeJS et vu comment les programmes asynchrones sont exécutés. 

Maintenant, vous devriez comprendre pourquoi la fonction de délai de deux secondes ne bloque pas le reste du programme pour s'exécuter. Vous savez également pourquoi la fonction de délai de zéro seconde imprime la valeur à la fin après que "End" soit imprimé.

C'est tout ! J'espère que vous avez apprécié la lecture de cet article et appris quelque chose de nouveau. N'hésitez pas à partager cet article si vous le trouvez utile.