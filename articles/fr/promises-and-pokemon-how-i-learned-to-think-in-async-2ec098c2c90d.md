---
title: Promesses et Pokémon — comment j'ai appris à penser en asynchrone
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-10T23:38:59.000Z'
originalURL: https://freecodecamp.org/news/promises-and-pokemon-how-i-learned-to-think-in-async-2ec098c2c90d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*J1GQbpmhZFXJ2AxGHLC1Og.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Promesses et Pokémon — comment j'ai appris à penser en asynchrone
seo_desc: 'By Kalalau Cantrell

  If you’ve been learning JavaScript, you may have heard about promises and how awesome
  they are.

  So, you decided to research the basics. Perhaps you came across the MDN docs on
  promises or great articles like this one by Eric Ellio...'
---

Par Kalalau Cantrell

Si vous apprenez JavaScript, vous avez peut-être entendu parler des promesses et de leur utilité.

Alors, vous avez décidé de rechercher les bases. Peut-être êtes-vous tombé sur la [documentation MDN sur les promesses](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises) ou sur d'excellents articles comme [celui-ci](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-promise-27fc71e77261) d'Eric Elliott ou [celui-ci](https://codeburst.io/javascript-learn-promises-f1eaa00c5461) de Brandon Morelli. Si vous avez lu tout cela et plus encore, vous avez probablement vu l'exemple typique des promesses en action.

Une fois que vous avez vu suffisamment de ces types d'exemples, cependant, vous commencez à vous demander si vous comprenez vraiment les promesses. À ce stade, si vous êtes comme moi, vous comprenez conceptuellement ce qui les rend géniales — elles permettent d'écrire du code asynchrone dans un motif synchrone — mais vous avez hâte de voir un exemple de ce qu'elles peuvent faire autre que séquencer une série de `console.log` qui s'exécutent à différents moments.

Alors, qu'ai-je fait ? J'ai construit un simple jeu Pokémon, mettant en scène un combat tour par tour contre un [Électabuzz](https://bulbapedia.bulbagarden.net/wiki/Electabuzz_(Pok%C3%A9mon)).

**Cet article suppose que vous comprenez l'exemple de promesses mentionné ci-dessus. Veuillez consulter les ressources liées dans le paragraphe d'introduction si vous avez besoin d'un rappel.**

### Fonctionnalité de base

L'Électabuzz et le joueur commencent chacun avec une certaine quantité de points de vie (PV). La première chose qui se produit est qu'Électabuzz attaque et le joueur perd quelques PV. Ensuite, le jeu **attend** jusqu'à ce que le joueur choisisse une attaque à utiliser contre Électabuzz.

Oui, le jeu attend... et attend... c'est à ce moment-là que j'ai vraiment commencé à apprécier la valeur de l'utilisation des promesses. Une fois que le joueur choisit une attaque, Électabuzz perd quelques PV et ensuite il attaque à nouveau. Cette boucle continue jusqu'à ce que les PV d'Électabuzz ou ceux du joueur atteignent zéro.

### Le Pseudo-Code

Assez simple jusqu'à présent. Maintenant, ajustons cela un peu pour qu'Électabuzz attaque avec un timing plus naturel. Je voulais qu'il semble "réfléchir" à son mouvement avant de le faire.

Pendant que nous y sommes, ajoutons un peu d'action de promesses pour que nous puissions enchaîner des fonctions qui s'exécuteront une fois qu'Électabuzz aura terminé son attaque et pas une milliseconde plus tôt. C'est après tout un jeu tour par tour.

Super, cette configuration nous permettra de faire cela plus tard.

Maintenant, passons au code pour le joueur.

Comment écrivons-nous une fonction qui, lorsqu'elle est appelée, attendra l'entrée de l'utilisateur avant de terminer son exécution ? Nous savons qu'elle doit impliquer un **écouteur d'événement** d'une manière ou d'une autre pour la partie entrée de l'utilisateur. Nous savons également que nous devrions pouvoir utiliser des **promesses** d'une manière ou d'une autre pour la partie asynchrone... mais comment combiner les deux ?

Ce que j'ai découvert, c'est que si vous 1) créez une promesse, et 2) dans cette promesse ajoutez un écouteur d'événement pour, dans notre cas, l'événement de clic d'un bouton, et 3) si la fonction appelée par l'écouteur d'événement résout la promesse, vous pouvez obtenir cet effet d'attente.

Voilà ! Maintenant, nous sommes capables de faire cela.

Notez que chaque appel à `playerTurn()` dans le code ci-dessus attendra... et attendra... jusqu'à ce que le joueur choisisse d'attaquer. Ce n'est qu'alors que l'exécution continuera au tour d'Électabuzz et ensuite reviendra.

Mais pourquoi l'écrire de cette manière alors que le même code peut être écrit dans sa forme équivalente async/await, qui semble beaucoup plus propre ? Si vous avez pu suivre ce que nous avons fait avec les promesses jusqu'à présent, ce n'est pas un grand pas pour voir comment fonctionne async/await. Comparez le code ci-dessous avec celui ci-dessus et vous verrez qu'ils sont équivalents mais que le code ci-dessous est plus facile à comprendre.

Approfondissez async/await en consultant [cet article](https://medium.freecodecamp.org/oh-yes-async-await-f54e5a079fc1) de Tiago Lopes Ferreira ou [ces diapositives](https://wesbos.github.io/Async-Await-Talk/#1) de Wes Bos.

Donc, maintenant notre code est capable de lancer quelques rounds de combat tour par tour avec Électabuzz. Mais nous avons besoin d'un moyen pour que le jeu se termine.

Enfin, nous aimerions que le jeu continue à fonctionner seul jusqu'à ce que les conditions de fin de jeu soient remplies. Au lieu de répéter manuellement la logique `cpuTurn()` et `playerTurn()` comme nous l'avons fait, nous pouvons appeler récursivement notre fonction `gameLoop()`.

Maintenant, la `gameLoop` s'exécutera et continuera à s'appeler elle-même et à fonctionner jusqu'à ce qu'Électabuzz réduise nos PV à zéro ou que nous réduisions les siens à zéro. Si vous voulez en savoir plus sur la récursion, regardez [cette vidéo YouTube](https://youtu.be/k7-N8R0-KY4) de MPJ. Pendant que vous y êtes, consultez les autres vidéos sur la chaîne Fun Fun Function de MPJ. Il est excellent pour expliquer des sujets complexes de manière amusante.

Examinons le pseudo-code dans son intégralité :

### Le Code

Maintenant que nous avons terminé le pseudo-code, voici un Pen montrant comment j'ai implémenté cette logique avec du JavaScript réel :

### Conclusion

Merci d'avoir lu. Cette petite expérience avec les promesses m'a montré qu'il y a beaucoup de choses que les promesses simplifient lorsqu'il s'agit de composer du code asynchrone. Bien que l'exemple typique de promesses avec console.logs et setTimeouts ait illustré le concept, cela ne m'a pas vraiment excité, alors j'ai décidé de créer ce simple jeu pour me motiver à propos des promesses. J'espère que vous avez ressenti un peu de cette excitation. Si des experts en asynchrone lisent ceci, ce serait génial d'avoir vos retours sur de meilleures façons d'atteindre la même fonctionnalité (avec des générateurs, par exemple). Si quelque chose n'était pas clair pour quelqu'un, faites-le moi savoir et j'essaierai de clarifier.

**N'hésitez pas à dire bonjour sur [Twitter](https://www.twitter.com/kalalaucantrell).**