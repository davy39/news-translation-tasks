---
title: 'Pratique délibérée : Ce que j''ai appris en lisant le code source de classNames'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-25T00:44:36.000Z'
originalURL: https://freecodecamp.org/news/deliberate-practice-what-i-learned-from-reading-classnames-f9b89cb785e4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*t7iCRsAhtZQAYg3mSQ1jlA.jpeg
tags:
- name: GitHub
  slug: github
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: 'Pratique délibérée : Ce que j''ai appris en lisant le code source de classNames'
seo_desc: 'By Anthony Ng

  This is part of my plan for deliberate practice to improve as a developer. Take
  a look at this article to learn more.

  In this article, we’ll look at a library called classNames (here’s the GitHub repository).
  classNames provides a simpl...'
---

Par Anthony Ng

Cela fait partie de mon plan de pratique délibérée pour m'améliorer en tant que développeur. Jetez un œil à [cet article](https://medium.com/@newyork.anthonyng/deliberate-practice-becoming-an-open-sourcerer-27a4f7640940) pour en savoir plus.

Dans cet article, nous allons examiner une bibliothèque appelée `classNames` (voici le [dépôt GitHub](https://github.com/JedWatson/classnames)). `classNames` fournit une API simple pour construire des noms de classe dans React. Nous allons voir ce qu'elle fait et ce que j'ai appris en parcourant leur dépôt.

### Comment utiliser ?

L'API `classNames` est très simple. Ils ont de excellents exemples dans leur [README.md](https://github.com/JedWatson/classnames/blob/master/README.md).

Vous pouvez passer des arguments de chaîne comme ceci :

`classNames` accepte également des objets comme arguments. Si la valeur de la clé est fausse (false, null, undefined, 0, NaN, chaîne vide), `classNames` omet la valeur.

`classNames` accepte également des tableaux comme arguments. Les arguments de tableau sont récursivement aplatis et traités en utilisant les règles ci-dessus. Vous pouvez mélanger différents types d'arguments (chaînes, tableaux, objets).

### Utilisation avec React

Le cas d'utilisation principal de ce package est de simplifier la gestion des noms de classe de React.

Sans `classNames`, vous auriez peut-être utilisé la manipulation de chaînes pour créer les noms de classe de React.

Maintenant, avec le package `classNames`, cela ressemblerait à ceci :

### Erreurs courantes : noms de classe "undefined"

L'erreur la plus courante que je vois au travail avec `classNames` sont les noms de classe `undefined`.

Rappelez-vous que les valeurs fausses sont ignorées à l'intérieur du package `classNames`.

Sachant cela, nous pouvons mettre à jour notre exemple `classNames` comme suit :

### Différentes versions que vous pouvez choisir : Dedupe

Il y a 2 problèmes que vous pourriez rencontrer. Les voyez-vous ?

Heureusement, `classNames` nous fournit une version optionnelle de sa bibliothèque à utiliser, appelée `dedupe`.

C'est plus comme ça. Notez que `dedupe` est environ 5 fois plus lent que le package `classNames` par défaut. Utilisez cela uniquement si nécessaire.

### Différentes versions que vous pouvez choisir : Bind

`bind` est une autre version optionnelle de `classNames`. Elle est destinée à nous aider lorsque nous utilisons des modules CSS avec React. Mais je trouve que le package `classNames` par défaut fonctionne bien avec les modules CSS.

Jetez un œil au [README.md](https://github.com/JedWatson/classnames#alternate-bind-version-for-css-modules) pour plus d'informations.

### Object.create(null)

Il est considéré comme une bonne pratique d'utiliser `hasOwnProperty` lors de l'itération sur les clés d'un objet. Vous pouvez vérifier si la clé appartient à l'objet ou est héritée.

Nous utiliserions `hasOwnProperty` pour obtenir les propriétés qui appartiennent à notre objet créé.

Au lieu d'utiliser `hasOwnProperty`, nous pouvons créer un nouvel objet qui n'hérite de rien !

Mais cela signifie également que les méthodes que les objets héritent, telles que [toString](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/toString), n'existeront pas sur ce nouvel objet.

### Documentation et tests excellents

Jetez un œil au code source de `classNames`. Il est parsemé de commentaires et de documentation incroyables.

Une documentation excellente n'est pas quelque chose qui est exclusif aux projets open source.

Avez-vous trouvé un excellent extrait de code que vous avez utilisé sur votre projet personnel ?
Avez-vous passé des heures à chercher la réponse parfaite sur StackOverflow ? Incluez ces liens en tant que commentaires dans votre code ! Cela sauvera d'autres développeurs (et vous dans le futur) du temps lorsque vous essayez de comprendre ce qui se passe.

`classNames` a une documentation incroyable sur leur README.md. Il contient des exemples riches qui montrent tout ce que ce package peut faire.

La documentation et les commentaires sont excellents. Pourtant, ils peuvent pourrir et devenir désynchronisés avec ce que le code fait réellement. Mais les tests ne mentent pas ! Des tests bien écrits vous diront tout ce que le package devrait être capable de faire et ne pas faire. Si vous êtes nouveau dans une bibliothèque, consultez leurs tests pour mieux comprendre la bibliothèque.

### apply/call

Savoir comment utiliser `apply` et `call` de JavaScript sont de grandes questions d'entretien. Mais je les utilise rarement dans le monde réel. Les voir à l'intérieur du package `classNames` a été un bon rappel de ce qu'ils font.

`apply` et `call` font essentiellement la même chose. Ils définissent le `this` de la fonction appelante.

Par exemple,

La différence vient lorsque vous voulez passer des arguments dans la fonction appelante. Prenons un exemple de fonction qui prend des arguments.

Remarquez la petite différence ici. `apply` prend ses arguments dans un tableau (je m'en souviens en me rappelant que `apply` et `array` commencent tous les deux par `a`). `call` prend ses arguments fournis individuellement, comme le ferait une fonction normale.

`classNames` utilise `apply` pour gérer les arguments de tableau qui lui sont passés.

### Ne faites confiance à rien

Jetez un œil à l'extrait de code ci-dessous.

Pourquoi enregistrerions-nous la fonction `hasOwnProperty` dans une variable ? C'est parce que nous devons être défensifs sur les arguments donnés. Nous prenons `hasOwnProperty` de `Object.prototype`. Voyons pourquoi.

Cela a du sens. Mais que se passe-t-il si quelqu'un nous passe un objet comme ceci :

Utiliser la fonction `hasOwnProperty` de `Object.prototype` est une alternative plus sûre.

Mais notez que même cela n'est pas infaillible. Ce qui suit est toujours possible.

### Entités HTML

J'oublie toujours les entités HTML. Je cherche toujours une image fantaisiste, mais l'utilisation d'entités HTML est bien supportée et peut vous économiser une requête HTTP pour une image.

Avant de commencer à parcourir Google Images pour des ressources, jetez un œil à ce [tableau](https://dev.w3.org/html5/html-author/charref) pour voir s'il a ce dont vous avez besoin.

### Benchmark Performance

Vous n'avez plus besoin de discuter avec votre collègue sur les `for-loops` vs `for-each loops` ! Vous pouvez régler tous les différends en voyant comment cela se performe en utilisant des outils de benchmarking (tels que [jsPerf](https://jsperf.com/)).

`classNames` est téléchargé et utilisé par beaucoup, et la performance est d'une grande préoccupation. Les différences de performance sont examinées avant que toute demande de pull ne soit acceptée.

Vos projets personnels ne sont peut-être pas préoccupés par la performance. Mais il est bon de garder la performance à l'esprit. Prenez quelques minutes pour jouer avec [jsPerf](https://jsperf.com/) et configurez vos propres tests.

### travis.yml

![Image](https://cdn-media-1.freecodecamp.org/images/1*KbOOiRXqPSkUclWEKefK3g.png)
_Badges fantaisistes du README.md de `classNames`_

Intéressé à ajouter des badges fantaisistes à votre README.md ? Consultez ce excellent [tutoriel egghead](https://egghead.io/lessons/javascript-how-to-write-a-javascript-library-introduction) de Kent C. Dodds sur le démarrage de votre propre projet Open Source. Il couvre des sujets souvent ignorés, tels que la configuration de l'intégration continue, l'utilisation de la version sémantique, la publication sur npm, et plus encore.

### git blame, follow, history

Êtes-vous déjà tombé sur une certaine ligne de code et avez été curieux de savoir comment elle est apparue ? Utilisez la fonction `git blame` du site Web Github. Il vous dira quand elle a été écrite, qui l'a écrite et de quel commit elle provient.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sBl_QkREQClHV_yotMqELQ.png)
_git blame_

Vous pouvez également consulter l'historique d'un fichier et voir comment il a évolué en utilisant `git history`, situé juste à côté de `git blame`. Voir tous les commits vous montre comment un certain fichier a évolué au fil du temps.

Je vous recommande de trouver un projet Open Source que vous aimez et utilisez, et commencez à contribuer. Vous pouvez `surveiller` un dépôt et recevoir des notifications chaque fois qu'il y a des mises à jour. Vous ne serez peut-être pas prêt à pousser des modifications de code. Mais la mise à jour de la documentation ou l'aide avec les problèmes des autres sont également précieuses.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WpYuscwto8LVB7O_U1lU7A.png)
_surveiller_

Merci d'avoir lu ceci, et j'espère que vous avez appris quelque chose de nouveau.