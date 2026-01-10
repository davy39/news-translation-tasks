---
title: Vous voulez en savoir plus sur les boucles for de JavaScript ? Ce plongeur
  SCUBA animé peut vous aider !
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-07T12:41:26.000Z'
originalURL: https://freecodecamp.org/news/want-to-learn-about-javascripts-for-loops-this-animated-scuba-diver-can-help-76a038a09cc8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8Q1ePeYeNEi-H1-bVnX2FA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Vous voulez en savoir plus sur les boucles for de JavaScript ? Ce plongeur
  SCUBA animé peut vous aider !
seo_desc: 'By Kevin Kononenko

  For loops can be tough to follow if you are learning to code for the first time.
  This animated explanation should make it slightly easier.

  For loops are a fundamental part of pretty much every language used in web development.
  You ...'
---

Par Kevin Kononenko

Les boucles **for** peuvent être difficiles à suivre si vous apprenez à coder pour la première fois. Cette explication animée devrait rendre les choses un peu plus faciles.

Les boucles **for** sont un élément fondamental de presque tous les langages utilisés dans le développement web. Vous en apprenez les bases dès la première semaine de tout cours d'initiation à l'informatique, et elles font partie de tout cours en ligne d'introduction.

Pourtant, si JavaScript est votre premier langage de programmation (comme ce fut le cas pour moi), le concept d'une boucle for peut encore sembler un peu mystérieux. Bien sûr, vous pouvez comprendre le principe. Mais une fois que vous commencez à superposer d'autres concepts par-dessus — comme les tableaux, les objets et des mathématiques plus compliquées — vous pourriez constater que vous ne les comprenez pas aussi clairement que vous le souhaiteriez.

Alors, j'ai voulu créer une explication cristalline qui restera gravée dans votre esprit. Lorsque vous serez confronté à des concepts plus compliqués, il sera facile de les utiliser à l'intérieur de vos boucles for.

#### Alors, qu'est-ce qu'une boucle for ?

Si vous n'êtes pas déjà familier, les boucles for vous permettent d'agir sur une liste d'éléments sans nommer explicitement chaque élément.

Supposons que vous ayez la liste d'éléments suivante : 0,1,2,3,4. Vous ne voudriez pas insérer manuellement chacun d'eux dans une fonction ou accéder à l'index d'un tableau. Vous voudriez parcourir la liste et effectuer automatiquement l'action pour chaque élément. Je vais expliquer plus en détail dans un instant.

#### Pourquoi diable ai-je besoin d'une explication sur les boucles for ?

Examinons une boucle basique.

Cela donnerait comme sortie :

```
01234
```

Voici les deux problèmes que je vois :

* Quel est le concept de _i_ ? Il est utilisé différemment des autres variables.
* Où se produit l'itération ? En d'autres termes, quand est-ce que _i_ augmente ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*DE9ODjXM6QXqMfq0c-K5RQ.png)

Nous allons examiner les boucles for d'une manière différente. **Imaginez que vous êtes un plongeur sous-marin**, et que vous planifiez une excursion d'une journée dans un nouvel endroit. Vous explorez un nouveau récif, donc vous voudrez probablement faire plusieurs plongées pour vous assurer de voir tous les coraux et la vie marine.

#### Préparation de la plongée (initialisation et condition)

Avant de commencer votre plongée, vous devez déterminer combien de bouteilles d'oxygène vous aurez besoin au cours de la journée.

_let i= 0;_

C'est l'**initialisation**. Elle vous indique la valeur de la première bouteille d'oxygène. Dans ce cas, vous commencez à la bouteille 0.

![Image](https://cdn-media-1.freecodecamp.org/images/1*OcULbAvuWwufuJoH3KNMfA.png)

_i <_; 5

C'est la **condition**. C'est un peu comme la capacité du bateau. Vous ne pouvez ajouter que autant de bouteilles d'oxygène que votre bateau peut en contenir.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YsJJ0s4DbgW8WcIcftPXyQ.png)

#### Mise en place des bouteilles d'oxygène (mise à jour)

Jusqu'à présent, nous savons que notre première bouteille d'oxygène a une valeur de 0, et que la dernière doit être inférieure à 5. Mais combien de bouteilles devez-vous préparer ?

La dernière partie, appelée **mise à jour**, nous indique combien de bouteilles nous devons aligner.

_i++_

C'est une abréviation pour : _i = i+1_

Cela signifie qu'à chaque fois que nous terminons une boucle, nous ajouterons 1 à i. Puisque i commence à 0, voici à quoi cela ressemble.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kY-ArC5Hs5oQIbw6H1mOIA.gif)

Nous continuons à ajouter des bouteilles d'oxygène jusqu'à atteindre la limite. Lorsque nous ajoutons une bouteille à la fois, la dernière valeur qui remplit la **condition** est 4.

#### Le plongeur fait sa première plongée (itération)

Jusqu'à présent, nous connaissons la valeur de départ de _i_ (0) et chaque valeur de _i_ qui remplit la **condition** (0–4). Nous sommes prêts. Maintenant, nous devons faire intervenir le plongeur et exécuter les instructions à l'intérieur de la boucle for.

Imaginez que nous exécutons cette boucle :

Ainsi, votre plongeur commence avec une valeur de 0.

![Image](https://cdn-media-1.freecodecamp.org/images/1*n__pDZLTVnYhr5xMDHiAGw.png)

Voyez-vous où nous allons avec cela ? Votre plongeur est en fait _i_ ! Et il va parcourir le contenu de la boucle for, puis remonter pour une autre bouteille.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fEwGM-iXwM738RmLmkbfCQ.gif)

Pour l'instant, la boucle ne contient qu'une seule instruction. Voici ce qui se passera lors de la première itération.

![Image](https://cdn-media-1.freecodecamp.org/images/1*w1q3AVZpxgGwfB6cs-bMNA.gif)

La console enregistrerait : « The current value is 0 » puisque _i_ est 0. Votre plongeur transporte la valeur de chaque bouteille d'oxygène lorsqu'il parcourt le tableau.

#### Remontée à la surface (deuxième itération)

Puisque cette boucle for ne contient qu'une seule instruction, vous venez de terminer la première itération. Maintenant, vous devez l'exécuter à nouveau avec la valeur suivante.

Vous constaterez généralement que vos boucles for contiennent de nombreuses lignes de code. Mais pour l'instant, nous nous en tenons à une seule ligne afin que vous puissiez suivre le chemin de _i_.

Voici ce qui se passe lorsque vous atteignez cette dernière accolade : }.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VVGnJnOjP1-sBvD1HEp8-Q.gif)

Le plongeur lâche la bouteille 0 et grimpe l'échelle pour remonter chercher la deuxième bouteille, qui a une valeur de 1. Le plongeur fait une sorte de course de relais solitaire bizarre, mais c'est la nature d'une boucle for. Vous voulez qu'elle soit aussi rapide que possible. Maintenant, le plongeur est prêt à parcourir à nouveau la boucle avec une valeur de 1.

#### Le reste des bouteilles d'oxygène (chaque itération)

Maintenant, le plongeur doit prendre chaque bouteille d'oxygène à travers la boucle jusqu'à ce qu'elles soient toutes épuisées.

À chaque fois, nous enregistrerons un nouveau message dans la console.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-6-NXQWEqARvOTgObuKR5A.gif)

La sortie finale serait :

```
The current value is 0The current value is 1The current value is 2The current value is 3The current value is 4
```

À la fin de la boucle, _i_ est égal à 4 et ne peut plus augmenter en raison de la **condition**, donc la boucle est terminée. Si vous exécutez à nouveau la boucle, _i_ recommencera à 0 en raison de l'**initialisation**.

Pourquoi n'y a-t-il pas plusieurs plongeurs ? Parce qu'il n'y a qu'un seul _i_ ! Il ne peut y avoir qu'une seule valeur de _i_ parcourant la boucle à la fois. _i_ doit remonter en haut pour prendre la valeur suivante.

#### Changer les conditions

Supposons maintenant que, au lieu de compter de 0 à 5, vous voulez compter à rebours chaque nombre entier de 10 à 2. Comment pourriez-vous faire cela ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*XoFg1YUcFk4JnjIJUq_i5g.png)

Puisque la valeur de départ est 10, vous devez **initialiser** _i_ à 10.

_let i= 10;_

Ensuite, puisque vous voulez que le dernier nombre soit 2, vous devez définir une **condition** pour tous les nombres supérieurs à 1.

_i >_; 1

Et, au lieu de i++, nous utilisons _i - -_, ce qui est équivalent à _i= i-1_.

Code complet :

```
for ( let i = 10; i > 1; i --){}
```

#### Utilisation des boucles for avec les tableaux

Avant de lire cette section, vous devriez comprendre les tableaux. Si vous ne les avez pas étudiés auparavant, consultez [mon guide ici](https://medium.freecodecamp.org/javascript-arrays-and-objects-are-just-like-books-and-newspapers-6e1cbd8a1746).

Les boucles for sont couramment utilisées pour parcourir les tableaux. Supposons que vous avez un tableau rempli de notes de test.

```
var testScores = [64, 86, 73, 82, 95, 62, 87, 99];
```

Vous voulez enregistrer un message lié à chaque note dans la console. Au fur et à mesure que vous parcourez votre boucle, vous devez pouvoir aligner la valeur actuelle de _i_ avec l'**index** du tableau. Par conséquent, vous devez vous assurer que la boucle for parcourt chaque élément du tableau, peu importe le nombre de notes de test qu'il contient.

Nous pouvons utiliser la propriété [length](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length) du tableau pour découvrir combien d'éléments il contient. Dans ce cas, il y en a 8. N'oubliez pas que les tableaux sont également [0-indexés](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array), ce qui signifie que le premier élément du tableau a un index de 0.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sTvu3W0YFTXJnZXojwh_kw.png)

Nous **initialisons** _i_ à 0. Nous pouvons en fait utiliser testScores.length dans la condition, afin que cela fonctionne quel que soit le nombre d'éléments dans le tableau.

_i< testScores.len_gth

Nous pouvons référencer chaque élément du tableau en utilisant _i_ comme index.

_testScores[i]_

Retour à notre plongeur : il doit faire autant de plongées qu'il y a d'éléments dans le tableau. C'est pourquoi il est si important pour nous de suivre _i_. Dans cet exemple, les valeurs des bouteilles correspondent à des éléments spécifiques du tableau.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BTH-FD_G2oPdsCLod0snmA.gif)

L'exemple ci-dessus montre la troisième itération de la boucle, qui accédera au troisième élément du tableau à l'index 2. Voyez-vous comment cela peut être trompeur ?

Voici le code final pour cela :

Avez-vous aimé cela ? Applaudissez pour que d'autres puissent le découvrir également. Et, si vous voulez être informé lorsque je publierai de futurs tutoriels utilisant des analogies, inscrivez-vous ici :