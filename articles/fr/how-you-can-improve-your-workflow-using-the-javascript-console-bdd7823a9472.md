---
title: Comment améliorer votre flux de travail en utilisant la console JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-11T19:53:53.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-improve-your-workflow-using-the-javascript-console-bdd7823a9472
coverImage: https://cdn-media-1.freecodecamp.org/images/1*U62GMx7Z7U56CArkK2tfCQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment améliorer votre flux de travail en utilisant la console JavaScript
seo_desc: 'By Riccardo Canella

  As a web developer, you know very well the need to debug your code. We often use
  external libraries for logs, and to format and/or display them in some cases, but
  the console of our browsers is much more powerful than we think.

  Wh...'
---

Par Riccardo Canella

En tant que développeur web, vous connaissez très bien le besoin de déboguer votre code. Nous utilisons souvent des bibliothèques externes pour les logs, et pour les formater et/ou les afficher dans certains cas, mais la console de nos navigateurs est beaucoup plus puissante que nous le pensons.

Lorsque nous pensons à la console, la première chose qui nous vient à l'esprit est le `console.log`, n'est-ce pas ? Mais il existe beaucoup plus de méthodes que celles que nous imaginons. Maintenant, nous allons voir comment tirer le meilleur parti de l'utilisation de la console, et je vous donnerai quelques conseils pour rendre ces méthodes plus lisibles.

### Qu'est-ce que la Console ?

La console JavaScript est une fonctionnalité intégrée dans les navigateurs modernes qui vient avec des outils de développement prêts à l'emploi dans une interface de type shell. Elle permet à un développeur de :

* Voir un journal des erreurs et des avertissements qui se produisent sur une page web.
* Interagir avec la page web en utilisant des commandes JavaScript.
* Déboguer des applications et parcourir le DOM directement dans le navigateur.
* Inspecter et analyser l'activité du réseau.

En gros, elle vous permet d'écrire, de gérer et de surveiller JavaScript directement dans votre navigateur.

#### Console.log, Console.error, Console.warn et Console.info

Ce sont probablement les méthodes les plus utilisées de toutes. Vous pouvez passer plus d'un paramètre à ces méthodes. Chaque paramètre est évalué et concaténé dans une chaîne délimitée par l'espace, mais dans le cas d'objets ou de tableaux, vous pouvez naviguer entre leurs propriétés.

![Image](https://cdn-media-1.freecodecamp.org/images/mb28MA52eZS1oW000KV2KHJfjW93hGAkaFln)

#### Console.group

Cette méthode vous permet de regrouper une série de `console.log` (mais aussi des erreurs, des infos, etc.) sous un groupe qui peut être réduit. La syntaxe est vraiment très simple : il suffit de placer tous les `console.log` que nous voulons regrouper avant un `console.group()` (ou `console.groupCollapsed()` si nous voulons qu'il soit fermé par défaut). Ensuite, ajoutez un `console.groupEnd()` à la fin pour fermer le groupe.

![Image](https://cdn-media-1.freecodecamp.org/images/HmjCThNsjXDndqMmnXsoJfhaDvJWSe9HthWY)
_Exemple de comment utiliser console.group_

Les résultats ressembleront à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/oaS8o7IqXG2FYAlTwpMxjAoVaV94nCpjTDHw)

#### Console.table

Depuis que j'ai découvert `console.table`, ma vie a changé. Afficher des JSON ou des tableaux JSON très grands à l'intérieur d'un `console.log` est une expérience terrifiante. Le `console.table` nous permet de visualiser ces structures à l'intérieur d'un beau tableau où nous pouvons nommer les colonnes et les passer en paramètres.

![Image](https://cdn-media-1.freecodecamp.org/images/zTSGqfZmTDJNuDtoUsC8UuRBB8PAZ5OMME87)
_Exemple de comment utiliser console.table_

Le résultat est magnifique et très utile pour le débogage :

![Image](https://cdn-media-1.freecodecamp.org/images/nLfvcHJ1b6LuD5CzcZxk36jl9YzlUF3I41h1)

#### Console.count, Console.time et Console.timeEnd

Ces trois méthodes sont le couteau suisse pour tout développeur qui a besoin de déboguer. Le `console.count` compte et affiche le nombre de fois que `count()` a été invoqué sur la même ligne et avec la même étiquette. Le `console.time` démarre un minuteur avec un nom spécifié comme paramètre d'entrée, et peut exécuter jusqu'à 10 000 minuteurs simultanés sur une page donnée. Une fois initié, nous utilisons un appel à `console.timeEnd` pour arrêter le minuteur et imprimer le temps écoulé dans la console.

![Image](https://cdn-media-1.freecodecamp.org/images/2pxTmE0ZHBasKm2ZmZaj-ajMYHvhjhVDGhID)
_Exemple de comment utiliser console.time et console.count_

La sortie ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Tt4dNjkK0yCpYzAHD6ZEFluIQ6IHl9cjv-nl)

#### Console.trace et Console.assert

Ces méthodes impriment simplement une trace de la pile à partir du point où elles ont été appelées. Imaginez que vous créez une bibliothèque JS et que vous souhaitez informer l'utilisateur de l'endroit où l'erreur a été générée. Dans ce cas, ces méthodes peuvent être très utiles. Le `console.assert` est comme le `console.trace` mais n'imprimera que si la condition passée n'a pas été remplie.

![Image](https://cdn-media-1.freecodecamp.org/images/wXYN1gjig-dXgTSQPtf7rPPWR3uNvFrtsrGw)

Comme nous pouvons le voir, la sortie est exactement ce que React (ou toute autre bibliothèque) nous montrerait lorsque nous générons une exception.

![Image](https://cdn-media-1.freecodecamp.org/images/ZH4tfVHdbM-xG0R2TcTuQ58RuuozuPTGddug)

### Supprimer toutes les consoles ?

L'utilisation fréquente des consoles nous oblige souvent à les éliminer. Ou parfois, nous oublions la version de production (et ne les remarquons que par erreur des jours et des jours plus tard). Bien sûr, je ne conseille à personne d'abuser des consoles là où elles ne sont pas nécessaires (la console dans le gestionnaire de changement d'entrée peut être supprimée après avoir vu qu'elle fonctionne). Vous devriez laisser les logs d'erreurs ou les logs de trace en mode développement pour vous aider à déboguer. J'utilise beaucoup Webpack, tant au travail que dans mes propres projets. Cet outil vous permet de supprimer toutes les consoles que vous ne souhaitez pas conserver (par type) de la version de production en utilisant le [uglifyjs-webpack-plugin](https://github.com/webpack-contrib/uglifyjs-webpack-plugin).

```
const UglifyJsPlugin = require('uglifyjs-webpack-plugin')var debug = process.env.NODE_ENV !== "production";.....optimization: {        minimizer: !debug ? [            new UglifyJsPlugin({                // Options spécifiques à la compression                uglifyOptions: {                    // Éliminer les commentaires                    comments: false,                    compress: {                       // supprimer les avertissements                       warnings: false,                       // Supprimer les déclarations de console                       drop_console: true                    },                }           })] : []}
```

La configuration est vraiment triviale et simplifie le travail, alors amusez-vous avec la console (mais n'en abusez pas !).

> Si vous avez aimé l'article, applaudissez et suivez-moi :)   
> Merci et restez à l'écoute ?  
> Suivez mes dernières nouvelles et conseils sur F[acebook](https://www.facebook.com/CanellaRiccardo/)