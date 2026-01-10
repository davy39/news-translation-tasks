---
title: JavaScript Minify – Minifier JS avec un Minifier ou jsmin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-02T23:50:39.000Z'
originalURL: https://freecodecamp.org/news/javascript-minify-minifying-js-with-a-minifier-or-jsmin
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/3.-minifying-js.png
tags:
- name: JavaScript
  slug: javascript
- name: performance
  slug: performance
- name: web performance
  slug: web-performance
seo_title: JavaScript Minify – Minifier JS avec un Minifier ou jsmin
seo_desc: 'By Dillion Megida

  You might be wondering – what is minification and how does it improve your JavaScript
  applications? What tools can you use to minify your JS? I''ll answer these questions
  in this article.

  What is Minification?

  Minification is the pro...'
---

Par Dillion Megida

Vous vous demandez peut-être – qu'est-ce que la minification et comment améliore-t-elle vos applications JavaScript ? Quels outils pouvez-vous utiliser pour minifier votre JS ? Je répondrai à ces questions dans cet article.

## Qu'est-ce que la Minification ?

La minification est le processus de "minimisation" du code en supprimant les parties non pertinentes du code. À quoi cela ressemble-t-il ?

Jetez un œil au code JavaScript suivant :

```js
const variable = "Variable";

function print() {
  console.log(variable);
};

print(); // "Variable"
```

Ici, nous avons la déclaration `variable`, la déclaration `print`, et l'exécution `print()`. Nous avons aussi un commentaire.

En JavaScript, nous savons qu'un point-virgule est utilisé pour terminer une instruction. Cela aide l'interpréteur à différencier les instructions.

Dans notre code ci-dessus, vous pouvez voir les points-virgules à la fin de certaines lignes pour montrer où l'instruction se termine.

Une version "minifiée" du code JavaScript ci-dessus ressemblerait à ceci :

```js
const variable="Variable";function print(){console.log(variable);};print();
```

Les deux versions produiront les mêmes résultats. La différence est que la première version est facilement lisible, tandis que la seconde ne l'est pas. Ainsi, la première version est bonne pour le **développement** tandis que la seconde est adaptée pour la **production** (vous comprendrez cela en continuant votre lecture).

La taille de la première version sur mon ordinateur est de **100 octets**, tandis que la seconde est de **75 octets**. Bien sûr, cela est assez insignifiant ici – mais dans de grandes bases de code comme l'image ci-dessous, la différence serait évidente :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-242.png)
_Capture d'écran obtenue depuis [StackOverflow](https://stackoverflow.com/questions/51766230/difference-between-the-output-of-minified-js-and-css-files)_

## L'interpréteur JavaScript n'a pas besoin d'espaces blancs et de commentaires

L'interpréteur pour exécuter le code JavaScript n'a pas besoin d'**espaces blancs** (espaces, sauts de ligne, etc.). Il n'a pas non plus besoin de commentaires pour son exécution.

L'espacement et la mise en commentaire de notre code sont des choses que nous faisons en tant que développeurs pour améliorer notre expérience de développement. Ces choses rendent le code plus facile à lire et nous aident à nous souvenir pourquoi nous avons pris certaines décisions. Mais ils sont pour nous en tant que développeurs, pas pour votre navigateur. Votre navigateur **N'A PAS BESOIN** de ces choses.

Ce qui se passe alors, c'est que si vous avez beaucoup de commentaires/espaces blancs dans votre code, cela pourrait rendre la taille du fichier inutilement grande.

Avec la minification, les espaces blancs inutiles et les commentaires sont supprimés. Le code minifié produit le même résultat d'exécution que l'original, sauf que le code minifié est compressé et aura une taille de fichier plus petite.

## Pourquoi la taille du fichier est-elle importante ?

Lorsque vous allez à une URL sur votre navigateur, le navigateur récupère les ressources stockées sur le serveur pour cette URL. Il récupère le fichier `.html`, qui à son tour récupère les fichiers de feuille de style et de script liés.

Avec tout récupéré correctement, vous voyez une page sur votre navigateur avec des éléments stylisés et des interactions (réalisées avec JavaScript) fonctionnant.

Deux choses qui peuvent ralentir le processus de réception des ressources demandées sont :

* une connexion internet faible
* des tailles importantes des ressources

Vous ne pouvez pas contrôler la connexion internet que les utilisateurs de vos applications web peuvent avoir, mais vous pouvez contrôler les tailles de vos fichiers.

### Une taille de fichier plus petite améliore les temps de chargement

Plus la taille du fichier est grande, plus le téléchargement (récupération) prend du temps à se terminer. Et plus la taille du fichier est petite, plus le téléchargement se termine rapidement.

En minifiant vos fichiers JavaScript, vous pouvez **améliorer les temps de chargement des ressources** car le navigateur nécessitera moins de temps pour télécharger complètement ces fichiers.

### Une taille de fichier plus petite améliore le temps d'analyse initial

Lorsque le navigateur récupère un fichier JavaScript, le moteur JavaScript essaie d'abord d'analyser le fichier. L'analyse implique de parcourir le code ligne par ligne, en ignorant explicitement les espaces blancs et les commentaires, et en vérifiant si le code est syntaxiquement correct.

Si ce n'est pas le cas, vous obtenez des erreurs. Si c'est le cas, alors le code est traduit en code machine qui peut être compris par le navigateur.

Plus la taille du fichier est grande, plus il faudra de temps pour analyser le fichier. Plus la taille est petite, moins le parseur prendra de temps.

Ainsi, la minification de vos fichiers JavaScript **améliore le temps d'analyse initial**.

Ces choses peuvent améliorer les performances générales et le temps de réponse de vos applications web.

## Outils de Minification pour JS

Alors, comment utiliser les espaces blancs, les commentaires et autres choses dont vous avez besoin pour une bonne expérience de développement tout en livrant des fichiers minifiés pour la production ? L'idée est d'avoir une version **développement** et une version **production** de votre code.

La première est pour lorsque vous écrivez du code et construisez l'application, et la seconde est ce que vous stockez sur le serveur qui est livré au navigateur.

Vous n'avez pas à faire ce processus de minification vous-même. C'est presque impossible. Je vais partager deux outils de minification que vous pouvez utiliser.

### Minify

Cet outil supprime les espaces blancs, retire les commentaires, combine les fichiers et optimise quelques motifs de programmation courants. Vous installez l'outil sur votre appareil et le configurez dans votre code avec le chemin JavaScript que vous souhaitez minifier pour la production.

Vous pouvez vous référer au [dépôt](https://github.com/matthiasmullie/minify) pour en savoir plus sur l'outil et voir comment il est utilisé.

### jsmin

Cette bibliothèque NPM fonctionne de manière similaire à Minify, pour supprimer les commentaires et les espaces blancs dans les fichiers JavaScript.

En tant que module Node.js, vous pouvez l'installer globalement et utiliser la commande CLI pour minifier votre projet JavaScript.

Consultez la [bibliothèque sur NPM](https://www.npmjs.com/package/jsmin) pour en savoir plus à son sujet, son installation et son utilisation.

## Conclusion

La minification est un processus qui améliore les performances de vos applications en réduisant les temps de chargement et la bande passante pour la récupération des fichiers depuis les serveurs. Vous pouvez effectuer ce processus pour divers fichiers de code tels que HTML, CSS et JavaScript.

Dans cet article, j'ai expliqué ce qu'est la minification, pourquoi elle est bénéfique et comment elle peut être appliquée aux fichiers JavaScript. Vous pouvez également en apprendre davantage sur la [Minification CSS ici](https://www.freecodecamp.org/news/minify-css-css-minifying-and-compression-explained/).