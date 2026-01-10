---
title: Comment convaincre votre patron et vos collègues développeurs que vous avez
  raison (et qu'ils ont tort).
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-22T23:05:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-convince-your-boss-and-your-fellow-devs-that-you-are-right-and-they-are-wrong-6e1131298194
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IZcJKz3761vChU1VFHfzkw.jpeg
tags:
- name: communication
  slug: communication
- name: Life lessons
  slug: life-lessons
- name: personal development
  slug: personal-development
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Comment convaincre votre patron et vos collègues développeurs que vous
  avez raison (et qu'ils ont tort).
seo_desc: 'By Petr Zaparka

  As a developer, I’ve picked up some non-negotiable habits and good practices over
  the years. But sometimes, I’ve had to work with people who were not on the same
  wavelength as I was. Most of the time it’s the management.


  You can’t co...'
---

Par Petr Zaparka

En tant que développeur, j'ai adopté au fil des années certaines habitudes et bonnes pratiques non négociables. Mais parfois, j'ai dû travailler avec des personnes qui n'étaient pas sur la même longueur d'onde que moi. La plupart du temps, c'est la direction.

> Vous ne pouvez convaincre personne de quoi que ce soit. Vous pouvez seulement leur donner les bonnes informations, afin qu'ils se convainquent eux-mêmes.

> — Eben Pegan

La raison principale est généralement que nous regardons les problèmes et leurs solutions différemment. Nous savons par expérience que prendre des raccourcis nous reviendra sous forme de dette technique ou simplement de frustration.

J'écris cet article pour vous montrer comment vous pouvez changer l'opinion de votre manager — ou même celle de vos pairs.

### Communiquer de la bonne manière

Votre message peut être très important, mais si vous échouez à le transmettre, alors c'est de votre faute. Voici une façon de transmettre votre message efficacement :

> « Pour communiquer efficacement, nous devons atteindre les gens à travers leur Tendance, et non la nôtre. »

> - Gretchen Rubin

Comme vous le savez, les gens ne sont pas tous les mêmes. Certains peuvent être faciles à raisonner, et d'autres peuvent être têtus. Selon Gretchen Rubin, nous pouvons catégoriser les gens en quatre Tendances principales.

Gretchen a écrit un livre intitulé [The Four Tendencies](https://www.goodreads.com/book/show/33566873-the-four-tendencies?from_search=true). Elle a remarqué cette division parmi les gens, et comment nous pouvons les utiliser et en tirer avantage dans nos vies. Ces Tendances sont **Upholder**, **Obliger**, **Questioner**, et **Rebel**.

Voici une petite blague qui aide à les décrire :

_Comment faire changer une ampoule à un Upholder ?_  
_Réponse : Il l'a déjà changée._

_Comment faire changer une ampoule à un Questioner ?_  
_Réponse : Pourquoi avons-nous besoin de cette ampoule de toute façon ?_

_Comment faire changer une ampoule à un Obliger ?_  
_Réponse : Demandez-lui de la changer._

_Comment faire changer une ampoule à un Rebel ?_  
_Réponse : Faites-le vous-même._

#### Une étude de cas

Supposons que vous avez un product owner (PO) sur un nouveau projet. Le PO ne se concentre que sur les choses que vous livrez. Ils ne veulent pas que vous passiez du temps sur autre chose, comme écrire des tests.

Voici quatre façons différentes de convaincre votre PO que l'écriture de tests est importante. Mais n'oubliez pas que ce n'est qu'un exemple — vous devriez pouvoir utiliser ces cadres dans n'importe quel contexte.

C'est parti.

#### 1. PO en tant que Questioner

Selon Gretchen,

> Les Questioners adorent la recherche, trouver des efficacités et éliminer les processus irrationnels. Ils rejettent les explications paresseuses comme celle-ci :

> « C'est comme ça qu'on a toujours fait. »

> Parce que les Questioners ont une grande foi en leur propre analyse et jugement, ils peuvent devenir convaincus de la justesse de leurs vues et refuser d'être persuadés autrement.

Lorsque vous traitez avec un Questioner, apportez des raisonnements à la table. Ayez un point valide soutenu par des preuves.

Voici un exemple de conversation avec un PO nommé Alex :

**Moi** : Salut Alex, pouvons-nous parler des bonnes pratiques un instant ?

**Alex** : Bien sûr, qu'est-ce qui te préoccupe ?  
   
**Moi** : Je pense que nous poussons trop fort sur la livraison des fonctionnalités et que nous ne pensons pas assez à notre dette technique. Nous n'avons pas beaucoup de temps pour les tests.

**Alex** : Eh bien, je ne suis pas convaincu que passer beaucoup de temps sur les tests nous aidera à livrer mieux et plus vite. Nous corrigeons les bugs au fur et à mesure et cela semble fonctionner.   
   
**Moi** : J'ai regardé combien de temps nous passons à corriger les bugs, et le nombre augmente avec le temps. J'ai travaillé sur beaucoup de projets similaires. C'est plus rapide d'ignorer les tests au début, mais vous arriverez à un point où ce ne sera plus efficace. Je pense que nous en sommes là maintenant.   
   
**Alex** : Hmm, mais je ne veux pas embaucher une autre personne pour faire les tests, nous n'avons pas de budget pour cela.

**Moi** : J'ai une solution : ajoutons les tests à la portée de chaque ticket. Cela rendra les développeurs heureux, et vous pourrez comparer la vélocité. Si vous souhaitez en savoir plus, j'ai quelques exemples de livres et d'articles sur l'importance des tests.  
   
**Alex** : D'accord, rappelle-moi cela lors de notre prochaine planification de sprint, et je m'assurerai que tout le monde est sur la même longueur d'onde.

**Moi** : Merci.

#### 2. PO en tant qu'Upholder

> Les Upholders peuvent faire de grands collègues. Ils sont autonomes et très intéressés par la performance. Mais les Upholders deviennent parfois impatients lorsque les autres ont du mal à répondre aux attentes.

Je ne pense pas que vous devriez convaincre un Upholder de l'importance d'écrire des tests. Ils réagiraient comme ceci :

**Moi** : Salut Alex, je pense que nous en sommes au point où nous devons passer plus de temps à écrire des tests. Notre dette technique grandit.  
   
**Alex** : Je suis d'accord avec cela. N'hésite pas à écrire plus de tests et à faire du refactoring. Mais assure-toi que nous livrons toujours les fonctionnalités que nous avons promises.

#### 3. PO en tant qu'Obliger

> Les Obligers répondent aux attentes que les situations de travail fournissent presque inévitablement — avec des délais, des évaluations et des livrables.

Donc, pour les convaincre, nous pouvons utiliser un autre motivateur qu'ils suivent.

**Moi** : Salut Alex, je pense que nous en sommes au point où nous devons passer plus de temps à écrire des tests. Notre dette technique grandit.

**Alex** : Nous avons un délai à respecter — cela va-t-il l'affecter ?  
   
**Moi** : Nous pourrions être retardés dans le prochain sprint. Mais en écrivant plus de tests, nous pourrons réduire le temps de développement. Ainsi, nous devrions être plus rapides dans la prochaine étape et respecter le délai suivant avec facilité. Écrire des tests est également une bonne pratique de développement. Je peux vous montrer une série d'études qui le soutiennent si vous êtes intéressé.

#### 4. PO en tant que Rebel

Je me sens un peu machiavélique à ce sujet. Voici un exemple du livre :

> Un enfant rebelle pourrait mieux répondre si vous demandez : « As-tu envie de jouer du piano maintenant ? » Alors qu'un enfant Upholder serait heureux d'être rappelé, « Il est temps de pratiquer le piano. »

Donc, si je voulais convaincre un product owner rebelle de l'importance des tests, je ne suis pas sûr de ce que je ferais. Je passerais probablement du temps sur les tests et le refactoring du code sans demander.

Gretchen note que « Ils accordent une grande valeur à la liberté, au choix, à l'identité et à l'expression de soi. » Donc, en réagissant de ma propre initiative et en prenant soin des choses, je correspondrais à cette spécification. Je serais le rebelle !

En fin de compte, vous devez savoir qui est votre audience. Vous devriez découvrir quelles sont les priorités de votre projet. Ensuite, rendez votre argument plus convaincant en mentionnant ces priorités.