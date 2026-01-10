---
title: Les Promesses JavaScript Expliquées par le Jeu dans un Casino
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-24T21:22:24.000Z'
originalURL: https://freecodecamp.org/news/javascript-promises-explained-by-gambling-at-a-casino-28ad4c5b2573
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WcIi4QEeGRC0btw4nImRVQ.jpeg
tags:
- name: education
  slug: education
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Les Promesses JavaScript Expliquées par le Jeu dans un Casino
seo_desc: 'By Kevin Kononenko

  Promises might seem confusing… until you find yourself in “callback hell.” Then
  they seem reasonable!

  We all love the asynchronous capabilities of JavaScript. In fact, we love them so
  much that sometimes, we overindulge. And then w...'
---

Par Kevin Kononenko

#### Les promesses peuvent sembler déroutantes… jusqu'à ce que vous vous retrouviez dans l'« enfer des callbacks ». Ensuite, elles semblent raisonnables !

Nous aimons tous les capacités asynchrones de JavaScript. En fait, nous les aimons tellement que parfois, nous en abusons. Et ensuite, nous obtenons du code qui ressemble à cette « pyramide de la mort » (pyramid of doom), à laquelle vous voudrez répondre en lançant un Hadouken :

![Image](https://cdn-media-1.freecodecamp.org/images/1*mL04Mh-tDosU6_OlqexwyQ.jpeg)

Ceci est communément appelé l'« enfer des callbacks » parce que vous ne voulez probablement pas relire ce code et essayer de comprendre comment tout fonctionne, et dans quel ordre. En fait, personne dans votre équipe ne le veut non plus.

Voici un autre exemple, plus simple :

Quelques éléments sont difficiles dans l'exemple ci-dessus :

* Gestion des erreurs peu claire. Que se passe-t-il si quelque chose va mal ?
* Chaque fonction dépend de la fonction précédente. Vous n'avez pas besoin du style asynchrone. Vous voulez rendre l'ordre clair pour les autres qui lisent le code. Lorsque vous enchaînez autant de fonctions ensemble, un style de code synchrone sera plus lisible.
* Vous devez suivre continuellement les variables pour l'entrée dans une fonction, puis la sortie. Et aussi suivre la logique qui s'applique à chaque sortie. Cela devient épuisant.

Vous pourriez rendre tout ce processus plus compréhensible en utilisant des **promesses**. Si vous êtes comme moi, vous avez peut-être entendu parler des promesses une ou deux fois, mais vous les avez ignorées parce qu'elles semblaient confuses. Les utilisations de base des promesses sont en fait assez simples si vous comprenez les callbacks.

Les promesses sont un peu comme aller au casino, et si vous cherchez à nettoyer un bloc de code désordonné, elles sont une excellente solution. Les promesses encouragent des fonctions simples et à usage unique qui vous permettront d'écrire un code clair et de comprendre chaque étape sans maux de tête.

Note : Si vous n'avez pas d'expérience avec les callbacks, consultez [mon explication](https://medium.freecodecamp.com/javascript-callbacks-explained-using-minions-da272f4d9bcd#.slyskqmt8) sur les principes des callbacks. Si vous cherchez une explication plus technique des promesses, consultez [ce guide](http://www.telerik.com/blogs/what-is-the-point-of-promises) ou [ce guide](https://www.promisejs.org/) ou [cette vidéo](https://www.youtube.com/watch?v=obaSQBBWZLk).

#### Que les paris commencent !

**Une promesse tient la place d'une valeur qui n'existe pas encore, mais qui existera certainement dans le futur.** Cela vous permet de suivre clairement une fonction et de comprendre son début et sa fin. Comme montré ci-dessus, les promesses sont un excellent moyen de donner de la clarté aux fonctions asynchrones consécutives et de clarifier les entrées et les sorties.

Supposons que vous partiez en vacances d'un week-end dans un casino. Vous avez deux semaines de salaire dans votre poche, et vous allez profiter de chaque moment en les pariant, jusqu'au dernier sou. Vous obtenez votre chambre d'hôtel, puis vous dirigez vers le casino. Les tables du casino n'acceptent pas d'argent liquide, cependant. Vous devez vous rendre à un guichet pour échanger votre argent (disons 1 000 $) contre des jetons de casino, comme ceux-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*rjNGiLJjB1bLbhmsopH_8A.jpeg)
_Par Podknox, User:AlanM1 — Recadré de [1], CC BY 2.0, [https://commons.wikimedia.org/w/index.php?curid=21571904](https://commons.wikimedia.org/w/index.php?curid=21571904" rel="noopener" target="_blank" title=")_

Arrêtez-vous ici. C'est le début d'une promesse ! Vous avez une valeur connue pour commencer, mais c'est un substitut, pas un produit final. Vous ne pouvez pas dépenser ces jetons de casino en dehors du casino, et vous n'êtes pas venu au casino pour collectionner des jetons de casino. Vous y êtes allé pour jouer à des jeux, et les jetons de casino sont le point de départ qui vous permettra de traduire vos 1 000 $ en espèces en un produit final, espérons-le plus de 1 000 $.

Après avoir obtenu vos jetons, vous essayez tous vos jeux préférés. Vous jouez 20 mains de blackjack, pariez 30 % de votre argent et perdez 200 $. Cela a été rapide. Vous passez à la roulette, et pariez 5 % sur le noir jusqu'à ce que vous gagniez 50 $. Vous passez au poker, pariez 50 % de votre argent, puis perdez 500 $ après être devenu trop confiant.

Voici ce processus en code :

Quelques points à noter sur ce scénario :

* Vous ne pouvez pas jouer à deux tables à la fois, donc un jeu doit suivre l'autre.
* Il n'y a pas grand-chose à faire dans un casino à part jouer à des jeux, donc vous voulez passer directement d'un jeu à l'autre.
* La seule entrée pertinente lorsque vous commencez un jeu particulier est le nombre de jetons que vous pouvez utiliser pour parier.
* La sortie d'un jeu particulier sera également des jetons.
* Si vous n'avez plus de jetons, vous ne pourrez pas commencer un autre jeu. Vous pouvez soit vous plaindre au directeur à ce moment-là et essayer de gagner sa sympathie, soit (plus probablement) commencer à boire.

**Chacune des trois instructions .then() dans la séquence ci-dessus est une promesse**. Elle commence avec une valeur de substitution définitive, et retournera une quantité inconnue de jetons, selon le déroulement du jeu. Une fois le jeu terminé, il retourne la valeur et l'alimente immédiatement à la promesse suivante. La promesse précédente est considérée comme « remplie ».

Voici l'exemple ci-dessus, de manière extensible :

Dans cet exemple, toutes les fonctions sont réutilisables ! Donc si vous voulez jouer aux jeux dans un ordre différent, vous pouvez facilement les permuter aux lignes 4–6.

Pour comparaison, voici le même code sans promesses :

Assez difficile à lire ! De plus, les messages d'erreur sont répétitifs. Vous pourriez lancer cette erreur si la promesse est rejetée en raison d'une valeur inférieure ou égale à 0 $. Le style asynchrone est inutile, car nous savons que ceci est une séquence d'actions consécutives.

#### Approfondir ces exemples

Si vous comprenez les promesses à ce stade, je suis impressionné ! Approfondissons le premier exemple pour le décomposer ligne par ligne.

**Ligne 3 :** Vous convertissez vos 1 000 $ en espèces en jetons en utilisant la fonction getCasinoTokens(), non représentée ici.

**Ligne 4 :** L'instruction .then() signifie que le bloc de code suivant utilisera les résultats de la fonction getCasinoTokens(). Ces résultats seront passés via l'argument _tokens_. Ce segment, aux lignes 4–6, est maintenant une **promesse non remplie**. Nous avons pris la valeur _tokens_, et nous attendons de transformer cette valeur avant de pouvoir continuer. Une instruction return la remplira.

**Ligne 5 :** Nous appelons la fonction playBlackjack() avec 30 % des jetons. Puisque le blackjack ne peut être joué qu'avec des jetons, il est important que cet argument soit sous la forme d'un nombre. S'il s'agissait d'une chaîne, d'un tableau ou d'un objet, cette fonction lancerait une erreur, et nous rejeterions la promesse. Lorsque la promesse est rejetée, nous descendons à la fonction .catch() à la ligne 13 pour voir quoi faire si une erreur se produit. Heureusement, tokens est un nombre, la fonction se termine, et cette promesse est remplie. Nous avons entré un montant de jetons, fait quelques paris, et sommes sortis avec un nouveau montant de jetons.

**Ligne 7 :** Il y a une autre fonction .then(), ce qui signifie que nous avons maintenant une autre promesse non remplie. La valeur d'entrée pour cette promesse est le **résultat de l'instruction return de la fonction précédente**. Dans ce cas, il s'agit d'un compte de jetons après avoir joué au blackjack. Cela est alimenté dans la promesse via l'argument _moreTokens_. Si vous étiez au casino, vous auriez pris votre pile résultante de jetons et vous seriez dirigé directement vers le jeu suivant, la roulette.

**Ligne 8 :** Si la fonction playRoulette() est complétée avec succès, cette promesse sera remplie. Dans ce cas, tant que moreTokens est un nombre, elle se complétera avec succès. Et puis nous répétons ce processus pour chaque fonction .then() consécutive.

**Ligne 13 :** La fonction catch() gère les erreurs, donc nous n'avons pas besoin de faire de gestion des erreurs dans chaque fonction individuelle ou de négliger entièrement la gestion des erreurs.

La clé des promesses est le concept de non remplie, remplie ou rejetée. Une fois que vous créez une séquence de ces promesses, vous avez un flux clair d'entrées et de sorties, et un code clair pour les autres à lire. Vous pouvez utiliser les 3 états différents pour suivre la progression de toute la chaîne de promesses. Le style est synchrone (séquentiel), même si l'exécution réelle est asynchrone.

Merci d'avoir lu. J'espère que cette analogie vous a aidé à mieux comprendre JavaScript et les promesses.

Cliquez sur le ? ci-dessous pour que d'autres personnes voient cet article ici sur Medium.