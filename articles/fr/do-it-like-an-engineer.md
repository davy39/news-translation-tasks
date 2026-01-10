---
title: Faites-le comme un ingénieur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-20T17:01:50.000Z'
originalURL: https://freecodecamp.org/news/do-it-like-an-engineer
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/engineering_hubris.png
tags:
- name: best practices
  slug: best-practices
- name: engineering
  slug: engineering
- name: framework
  slug: framework
- name: Problem Solving
  slug: problem-solving
- name: software development
  slug: software-development
seo_title: Faites-le comme un ingénieur
seo_desc: 'By Luca Florio

  The work of a Software Engineer is to solve problems. Everything can be reduced
  to this activity. This is why it is important to have a solid methodology to tackle
  problems. We are engineers after all, and we are trained to solve probl...'
---

Par Luca Florio

Le travail d'un ingénieur logiciel est de résoudre des problèmes. Tout peut être réduit à cette activité. C'est pourquoi il est important d'avoir une méthodologie solide pour aborder les problèmes. Après tout, nous sommes des ingénieurs et nous sommes formés pour résoudre des problèmes. Nous devons le faire comme un ingénieur.


### Comprendre les exigences

La première étape est de **comprendre les exigences**. Pour résoudre un problème, vous devez comprendre exactement quel est le problème. Il m'est arrivé qu'une fonctionnalité qui aurait dû prendre 2/3 semaines de travail soit devenue 3 mois inutiles de "Oh, il y a aussi cela…", "Oh, nous n'avons pas pensé à cela !", et "Peut-être que ce serait mieux si…". Ma faute. Leçon apprise.
Lorsque vous commencez à résoudre un problème, assurez-vous de comprendre le **point de départ**, le **but final**, et les **obstacles entre les deux**. La pire chose possible est de produire une solution qui ne fait pas ce qui est attendu.
En guise de note finale, rappelez-vous que *vous* et seulement *vous* décidez *comment* résoudre le problème. C'est votre travail, tout comme c'est le travail de celui qui vous donne les exigences de la nouvelle fonctionnalité de les exprimer de la meilleure manière possible. Si quelqu'un qui n'est pas ingénieur essaie de vous dire comment résoudre le problème, donnez-lui un coup de poing dans la figure. Vous êtes parfaitement justifié. Au moins par moi.

### Comprendre la taille

Nous sommes tous d'accord pour dire que servir 100 000 requêtes par seconde est un peu différent de servir 100 requêtes par minute. L'approche pour résoudre le problème est différente. C'est pourquoi il est important de comprendre ce qu'est la "taille de l'entrée" ou, en d'autres termes, **la taille du problème**. Sinon, il y a deux scénarios. Le meilleur cas est que vous passiez 6 mois à concevoir et à implémenter un système qui n'est utilisé qu'à 10 %. Le pire cas est lorsque vous passez 1 mois à concevoir un système qui est utilisé à 180 %. Si le meilleur cas est une perte de temps/ressources, vous ne voulez pas vous retrouver dans le pire cas. Pour éviter cette situation, nous devons poser les bonnes questions.
- *Combien de requêtes le système doit-il satisfaire ?*
- *Quel est le temps de réponse attendu ?*
- *Combien de ressources avons-nous ?*
- *Qu'en est-il des délais ?*
Les bonnes questions dépendent du contexte, mais l'objectif est unique : **comprendre la taille du problème**.

### Se tenir sur les épaules des géants…

Je vais vous révéler un secret. La probabilité que quelqu'un d'autre ait déjà résolu votre problème est élevée. **Très élevée**. Tout ce que vous avez à faire est une recherche dans la littérature pour découvrir s'il existe une solution pour un problème correspondant à votre cas d'utilisation. Évitez les solutions maison pour des problèmes bien connus, elles ne font qu'apporter d'autres problèmes. Il existe de nombreuses entreprises ayant "leur Hibernate", "leur Kafka", etc. parce que :
- *"Nous avons un cas d'utilisation différent"* (Je veux le voir)
- *"Les performances de la technologie X ne sont pas suffisantes pour nous"* (vraiment ?)
- *"Nous pouvons le faire mieux"* (c'est le plus drôle ?)
En résumé : une fois que vous connaissez vos exigences et la taille du problème, faites une recherche dans la littérature. **Il n'y a aucun intérêt à réinventer la roue**.

### …Mais rappelez-vous que vous n'êtes pas un géant

Il est acceptable de construire sur des solutions existantes, mais évitez de trop en faire. Rappelez-vous que [vous n'êtes pas Google](https://blog.bradfieldcs.com/you-are-not-google-84912cf44afb). Dans l'océan de technologies cool qui existent, la plus célèbre/innovante/utilisée n'est pas toujours la meilleure pour vous. Déployer un cluster Kafka pour traiter 5 messages par jour n'est probablement pas une bonne idée. Choisissez la technologie qui **fera le travail avec un minimum de complexité**. Cette décision vous sera bénéfique à long terme.

### Développement piloté par grand-mère

Implémentez votre solution en essayant de la rendre compréhensible par votre grand-mère. Évitez les implémentations fantaisistes et super complexes. Mettez-les de côté en faveur d'une solution *simple* et *compréhensible*. Cela rendra le code plus maintenable. Laissez l'optimisation pour le moment où elle sera nécessaire.
Plus formellement, votre implémentation devrait suivre la [Règle du Moindre Pouvoir](https://en.wikipedia.org/wiki/Rule_of_least_power). La règle originale fait référence au choix du langage de programmation. Dans ce contexte, nous pouvons la lire comme suit :
> "Parmi les solutions disponibles, choisissez celle qui a le moins de pouvoir et qui peut résoudre votre problème."

J'ai appris cette règle lorsque j'ai commencé à utiliser la programmation fonctionnelle. Elle permet d'implémenter des solutions avec une élégance inégalée. Cependant, de telles solutions sont parfois trop complexes. Je préfère une implémentation un peu moins élégante et efficace, mais beaucoup plus compréhensible et maintenable. **Vous ne serez pas le seul à lire votre code**.

### Conclusion

Nous sommes des ingénieurs, notre travail est de résoudre des problèmes, sous quelque forme qu'ils apparaissent. Nous devons appliquer nos compétences d'ingénierie et analyser le problème *de manière pragmatique* pour livrer la solution correcte. Nous devons nous rappeler que ce n'est pas la solution qui produit le résultat souhaité. C'est celle qui le fait en nécessitant **le moins d'effort**, et avec **le moins de complexité**. J'espère que la méthodologie que j'ai décrite dans cette histoire vous aidera à faire un pas vers un tel accomplissement.

À bientôt ! 😊