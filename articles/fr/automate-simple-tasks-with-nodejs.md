---
title: Comment automatiser des tâches simples avec Node.js
subtitle: ''
author: Mihail Gaberov
co_authors: []
series: null
date: '2020-10-27T18:36:59.000Z'
originalURL: https://freecodecamp.org/news/automate-simple-tasks-with-nodejs
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9815740569d1a4ca1807.jpg
tags:
- name: automation
  slug: automation
- name: Node.js
  slug: nodejs
seo_title: Comment automatiser des tâches simples avec Node.js
seo_desc: 'Recently, I had to travel through several countries by car ?. There were
  a lot of tolls to pay? and a lot of gasoline⛽ to fill. Which meant a lot of bills.

  I collected the receipts? along the way. And I planned to calculate, at the end
  of the trip, h...'
---

Récemment, j'ai dû voyager à travers plusieurs pays en voiture ?. Il y avait beaucoup de péages à payer ? et beaucoup d'essence ⛽ à remplir. Ce qui signifiait beaucoup de factures.

J'ai collecté les reçus ? en cours de route. Et j'ai prévu de calculer, à la fin du voyage, combien le voyage entier m'a coûté.

À la fin, j'avais un sac plein de papiers. Ce qui signifiait que j'avais beaucoup de chiffres à additionner.

Je les ai mis dans une feuille de calcul sur mon PC, prêt à commencer à les calculer à la main. Et puis, mon esprit de programmeur a commencé à me parler - pourquoi devrais-je faire tout ce travail manuel ?‍♂️ alors que je pourrais écrire un court programme pour le faire à ma place ?

Ne vous méprenez pas, je suis conscient qu'il existe de nombreuses autres façons de faire de tels calculs. Mais puisque je voudrais me considérer comme un programmeur qui aime automatiser les choses, je voulais le faire moi-même. À l'ancienne.

J'ai décidé d'utiliser [Node.js](https://nodejs.org/) pour résoudre ce problème, principalement parce que je suis assez à l'aise avec JavaScript. Et cela devait être une **solution très rapide** à laquelle j'ai pensé pendant une tasse de café ☕ le matin.

Voici donc ce que j'ai fait :

Tout d'abord, j'ai saisi tous les chiffres que j'avais dans un fichier txt, chacun sur une nouvelle ligne.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-112.png align="left")

*Source de données dans un fichier txt*

Ensuite, j'ai écrit un petit programme qui lisait le fichier source de données, analysait les chiffres sur une nouvelle ligne comme une valeur séparée à ajouter, et faisait la somme.

```javascript
var fs = require('fs');

calculate = () => {
    fs.readFile('data.txt', 'utf8', (err, data) => {
        if (err) {
            throw new Error(err)
        }

        const arr = data.split('\r\n');
        const result = arr
            .filter(e => e)
            .map(parseFloat)
            .reduce((curr, next) => curr + next);
        console.log('RESULT: ', result);
    });
}
```

## Comment j'ai construit cet outil

Je vais dire quelques mots sur l'implémentation d'abord. Ensuite, nous passerons en revue une brève discussion sur les **autres options** que j'aurais pu choisir.

Il s'agit d'une fonction très courte qui utilise un package Node.js, `fs`. Il nous permet d'interagir avec le système d'exploitation (par exemple, pour lire ou écrire des fichiers). C'est exactement ce dont nous avons besoin pour pouvoir lire notre fichier source de données.

Le code lui-même suit le mécanisme standard de [rappel Node.js](https://www.javatpoint.com/nodejs-callbacks). Et à l'intérieur de la fonction de rappel, j'ai utilisé une approche un peu fonctionnelle : [Piping](https://en.wikipedia.org/wiki/Pipeline_(software)) plusieurs méthodes qui obtiennent les données du traitement précédent, font quelque chose dessus, puis les transmettent à la suivante.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-113.png align="left")

*Méthodes de piping*

La première méthode, `split`, analyse les données qui sont lues à partir du fichier texte en utilisant le séparateur `\r\n`. Ces [symboles](https://en.wikipedia.org/wiki/Newline) sont utilisés dans le monde de la programmation pour spécifier quand une nouvelle ligne (dans un fichier) arrive.

À ce stade de notre programme, nous avons nos chiffres qui ont été lus et analysés à partir du fichier txt. Maintenant, nous utilisons la méthode `filter`. Cette étape supprime les données de toute valeur vide.

Ensuite, nous passons à la méthode `map` - il s'agit d'une [méthode de tableau JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map) qui accepte une fonction de rappel. Ce rappel sera exécuté sur chacun des arguments d'un tableau donné.

Dans notre cas, les données sont transmises implicitement – ce qui provient de la sortie de la méthode `filter` ira en entrée pour la méthode `map`. Et chacun des membres de cette entrée sera traité par la méthode `parseFloat`.

Il s'agit d'une [autre méthode JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseFloat) qui analyse un argument, le convertit en chaîne de caractères d'abord si nécessaire, et retourne un nombre à virgule flottante. Nous devons effectuer cette étape pour garantir que nous obtenons un calcul correct.

La dernière étape de notre pipeline est la méthode `reduce`, une troisième [méthode de tableau JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce) que nous allons utiliser.

Cette méthode a [plusieurs applications](https://www.digitalocean.com/community/tutorials/js-finally-understand-reduce), mais dans notre cas, nous l'utilisons simplement pour additionner les nombres dans le tableau tout en l'itérant.

La fonction de rappel de réduction que cette méthode accepte fait le vrai travail. J'ai extrait la mienne dans une méthode nommée séparée pour améliorer la lisibilité du code.

## Ce que nous devons faire vs ce que nous pouvons faire

Dans la dernière section, j'ai promis une brève discussion sur ce que nous pourrions utiliser d'autre pour atteindre le même objectif.

*Il est maintenant temps de s'arrêter un moment et de réfléchir à ce que nous devons faire par rapport à ce que nous pouvons faire et comment nous pouvons le faire.*

Dans ce cas précis, mon objectif était très simple. J'avais des chiffres que je devais additionner automatiquement.

Cela m'a fait réfléchir – quelle structure de données devrais-je utiliser pour mettre les données afin d'avoir plusieurs choix pour un traitement facile ? C'est ainsi que j'ai pensé à un tableau. Après tout, c'est l'une des structures de données les plus simples et les plus utilisées en JavaScript.

Et à partir de là, vous avez plusieurs options :

1. Vous pourriez faire comme je l'ai fait dans mon exemple – utiliser des méthodes de tableau JavaScript telles que map, filter et reduce de manière plus fonctionnelle. Ou,

2. Vous pourriez utiliser la méthode traditionnelle et utiliser des [boucles](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration) régulières pour itérer sur le tableau et faire le calcul. De telles boucles pourraient être des boucles for-, while-, forEach ou même do-while JavaScript. Dans de tels petits programmes, la performance est négligeable, donc c'est à vous de choisir quoi utiliser.

Les deux choix fonctionneraient bien. Ce qui est plus important ici, c'est que **vous devez toujours prendre vos décisions en fonction de votre objectif final.**

Dans cet article, j'ai discuté d'un outil d'automatisation très court et rapide à mettre en œuvre. Il a fait le travail dont j'avais besoin. Étant donné que je n'avais pas beaucoup de temps à investir, la première solution fonctionnelle était suffisamment bonne.

Mais il y aura des cas où vous devrez effectuer une analyse beaucoup plus sophistiquée à l'avance afin de finir avec un logiciel de bonne qualité à la fin.

> Gardez votre objectif final comme guide lorsque vous décidez quoi faire et comment le faire, et vous serez toujours sur la bonne voie.

## Essayez-le

Si vous voulez essayer vous-même, assurez-vous d'avoir installé Node.js sur votre système. Ensuite, allez-y et consultez ce [dépôt](https://github.com/mihailgaberov/calc-expenses).

Pour exécuter le programme, utilisez la commande suivante lorsque vous êtes dans le répertoire où se trouve le fichier calc.js :

```bash
node calc.js
```

Vérifiez votre fenêtre de console pour voir le résultat. La mienne ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-114.png align="left")

*Sortie de la console*

C'est tout ce que je voulais partager avec vous. J'espère qu'une partie de cette expérience restera avec vous pour vos futures tâches d'automatisation.

? Merci d'avoir lu ! ?