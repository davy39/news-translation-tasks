---
title: 'Aujourd''hui j''ai séché : comment trouver le plus petit nombre qui n''est
  pas dans le tableau'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-06T11:01:02.000Z'
originalURL: https://freecodecamp.org/news/tis-find-the-smallest-integer-that-is-not-in-the-array-80479cec15e4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uGGUGY-TAtzH7-XYMdzzvQ.jpeg
tags:
- name: Today I Spaced
  slug: today-i-spaced
- name: interview
  slug: interview
- name: JavaScript
  slug: javascript
- name: Life lessons
  slug: life-lessons
- name: 'tech '
  slug: tech
seo_title: 'Aujourd''hui j''ai séché : comment trouver le plus petit nombre qui n''est
  pas dans le tableau'
seo_desc: 'By Marin Abernethy

  TIS in my first technical interview. Here’s what I learned.


  ID 48395285 © Ojogabonitoo | Dreamstime.com

  Today I Spaced in my first technical interview, and could barely rememberhow to
  console.log()let alone find an optimal solutio...'
---

Par Marin Abernethy

#### J'ai séché lors de mon premier entretien technique. Voici ce que j'ai appris.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uGGUGY-TAtzH7-XYMdzzvQ.jpeg)
_ID 48395285 © Ojogabonitoo | Dreamstime.com_

Aujourd'hui, j'ai séché lors de mon premier entretien technique et je me souvenais à peine de la façon d'utiliser `console.log()`, encore moins de trouver une solution optimale.

D'abord, un résumé en une phrase de mon parcours en logiciel : pendant quelques années après ma licence, j'ai travaillé pour une petite société de conseil en logiciel en tant que développeur full stack avant d'obtenir mon master en génie logiciel, que j'ai terminé cette année.

Woah, d'accord. Peut-être que cela aurait dû être deux phrases. Le fait est que j'avais confiance en mes capacités d'ingénierie, mais la pression des entretiens a fait diminuer cette confiance.

J'ai séché lors de mon premier entretien technique téléphonique aujourd'hui en codant en direct, mais j'espère que mon moment "Aujourd'hui j'ai séché" (TIS) se transformera en un "Aujourd'hui j'ai appris" (TIL) après une revue de mon entretien. C'est parti...

### Le problème

L'intervieweur a présenté la question dans le contexte du produit que l'entreprise développe, mais cela revient à ceci : étant donné un tableau d'entiers, écrire une fonction qui trouve le plus petit entier qui **n'est pas** dans le tableau.

Par exemple, étant donné le tableau `[5, 2, 1, 4, 0, 2]`, la fonction doit retourner `3`.

Simple, non ? Laissez le séchage commencer.

### **Où j'ai fait erreur**

Hmm, par où commencer ? Dès que l'intervieweur a terminé d'expliquer la question, la panique interne a commencé. Je ne pouvais pas réfléchir.

**Monologue intérieur** : _RÉFLÉCHIS Marin, RÉFLÉCHIS. Pourquoi n'essaies-tu même pas de réfléchir au problème ? Aha ! Google sait toujours. Yo Google, dis-moi quoi faire... Oh, attends, je suis censé parler. Tous les conseils en ligne disent que je devrais expliquer mon raisonnement à voix haute. Ahhh d'accord d'accord d'accord. Je ne peux pas lire et parler en même temps. Bon, au revoir Google._

**Monologue extérieur** : « Euh, ah, bien... voyons voir. Hmmm. Oui donc, hm. »

Après quelques minutes d'hésitation et de silence, j'ai proposé cette solution (en JavaScript) :

Vous vous souvenez que j'ai dit que je ne me souvenais même pas comment utiliser `console.log()` ? Eh bien, après avoir terminé ma première tentative, j'étais confus lorsque [Coderpad](https://coderpad.io/) a exécuté ma fonction et que rien n'est apparu à l'écran. L'intervieweur a dû me rappeler que cela compilait correctement, mais que je devais utiliser `console.log()` si je voulais voir la sortie dans la console. Doh. Cue face to palm.

J'ai donc mis à jour : `console.log(count)`. Et cela a retourné la bonne réponse ! Wahooo ! ...Puis-je rentrer chez moi maintenant ?

« Très bien, quelle est la complexité temporelle de cet algorithme ? » a demandé l'intervieweur. J'avais imprimé une liste des différentes complexités pour m'aider si cela venait à être abordé. Il s'avère que je ne peux pas lire quand je suis nerveux.

_RÉFLÉCHIS, Marin. RÉFLÉCHIS._ Eh bien, ma solution est juste une seule boucle, non ? `Loop === Constant` était griffonné sur mon impression. J'ai donc dit « Constant, O(n) time », sans y réfléchir davantage.

_FAUX_. Oui, j'ai écrit une seule boucle `while`. Cependant, je n'ai pas reconnu la fonction JavaScript `includes()` comme autre chose que de la magie. Lorsque l'intervieweur a insisté sur ce point, j'ai réalisé que `includes()` parcourt également le tableau à chaque fois. Donc, en réalité, la complexité temporelle est O(n²). Cue face to palm round two.

Pendant un bref moment, les rouages ont commencé à tourner. Quelles structures de données ai-je lues ? Linked List ? Cela ne semble pas utile. Stack ? Non. HashTable ? Aha !

### Vers une solution

Deuxième tentative :

J'ai donc pensé que je pourrais mapper chaque entier du tableau à leur fréquence. En revoyant cette solution après l'entretien, j'ai réalisé qu'il était inutile de garder une trace du nombre de fois qu'un entier est apparu dans le tableau. Nous devons simplement savoir s'il est apparu, donc le booléen `true` aurait suffi. Dans les deux cas, la complexité temporelle est O(n).

En raison du temps limité restant, l'intervieweur m'a demandé comment je résoudrais ce problème avec uniquement des tableaux. _Ding !_ J'ai dit : « vous pourriez trier le tableau, puis le parcourir jusqu'à ce qu'il y ait un nombre manquant ». Voici ce que je voulais dire par là :

En regardant en arrière, je vois que non seulement j'aurais pu donner une explication plus claire, mais j'aurais également dû discuter des compromis entre cette solution et ma solution de hachage. C'est-à-dire que, comme cette solution est faite [in-place](https://www.geeksforgeeks.org/in-place-algorithm/), la complexité spatiale est O(1), ce qui est supérieur à la solution de hachage avec O(n). Cependant, il est raisonnable de supposer que l'algorithme de tri est de complexité temporelle O(n log n), ce qui est moins efficace que la solution précédente.

_Soupir_. Plus de pratique ! Plus d'entretiens ! À suivre.

### **TL;DR**

Mon cerveau, face à un choix de combat ou de fuite lors d'un entretien technique intimidant, a choisi la fuite. Peut-être qu'avec un peu plus de pratique, il choisira de se battre la prochaine fois.

Note à moi-même :

* Parlez de la solution avant de la coder. Cela peut vous aider à découvrir une solution plus efficace plus tôt (par exemple, l'intervieweur peut être plus qu'un simple interlocuteur, il donne parfois des indices)
* Oui, expliquer votre réponse est important, mais pas au détriment de votre solution finale. Prenez un moment pour réfléchir, si nécessaire.
* Les fonctions internes de JavaScript ne sont pas magiques ! Elles ont aussi une complexité temporelle et spatiale.