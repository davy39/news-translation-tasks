---
title: Un déluge de données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-02-16T00:10:44.000Z'
originalURL: https://freecodecamp.org/news/a-flood-of-data-714f287d75a0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*z0xcDaE65IjAIE6AoSpGTA.jpeg
tags:
- name: Design
  slug: design
- name: social media
  slug: social-media
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Un déluge de données
seo_desc: 'By BerkeleyTrue

  Free Code Camp’s data has been doubling each month, thanks to a flood of highly-active
  campers. This rising tide of data has exposed several weaknesses in our codebase.

  What started out 15 months ago as a small effort has since grown ...'
---

Par BerkeleyTrue

Les données de Free Code Camp ont doublé chaque mois, grâce à une vague de campeurs très actifs. Cette marée montante de données a révélé plusieurs faiblesses dans notre base de code.

Ce qui a commencé il y a 15 mois comme un petit effort s'est depuis transformé en une communauté open source dynamique. Près de 300 contributeurs se sont impliqués pour nous aider à construire rapidement des fonctionnalités.

Comme d'habitude, maintenir cette vitesse de développement effrénée a un prix. Nous avons accumulé beaucoup de dette technique.

Prendre de la dette technique, c'est comme jouer à Jenga — vous pouvez construire votre tour de plus en plus haute, mais au détriment de la stabilité. Tôt ou tard, vous devez rembourser votre dette technique, ou votre tour s'écroulera.

![Image](https://cdn-media-1.freecodecamp.org/images/1*z23k2LpK6Btt7flpnoGU6w.jpeg)

La semaine dernière, notre dette technique nous a rattrapés dans notre back-end — littéralement et figurativement.

Pendant les heures de pointe, nos serveurs MongoDB ont atteint leur capacité maximale, et le taux auquel ils envoyaient des données à nos serveurs Node a ralenti au point de ramper. Nous devions régler cela, et vite. Mais d'abord, nous devions comprendre ce qui causait le problème.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iDigQ6lfx2Q_pLXSarQ-yQ.png)
_Nos serveurs MongoDB saturant le CPU_

Nous avons initialement écrit la plupart de notre back-end en mode crunch, les yeux fatigués. Nous n'avons pas pris le temps d'optimiser nos requêtes. Au lieu de cela, nous avons choisi de nous concentrer sur des fonctionnalités que nous pensions avoir un impact plus immédiat sur l'expérience utilisateur.

Nous avons audité notre base de code et trouvé beaucoup d'écritures fréquentes et inefficaces dans nos bases de données. Par exemple, chaque fois qu'un campeur complétait un défi, nous apportions les modifications appropriées à son instance utilisateur, puis appelions l'action « save ». Cela provoquait l'envoi de l'objet utilisateur entier de nos serveurs Node à nos serveurs MongoDB, qui devaient ensuite réconcilier toutes les données.

Ce n'était pas un problème au début, car la plupart de nos objets utilisateur étaient petits. Mais à mesure que nous ajoutions des fonctionnalités, les objets utilisateur ont gonflé en taille, provoquant beaucoup plus de données à circuler.

Nous avions également l'habitude de sauvegarder chaque solution qu'un campeur soumettait. Cela a entraîné des tableaux completedChallenge encore plus grands, ce qui a encore aggravé les allers-retours.

En plus de cela, cela signifiait que certains campeurs devaient chercher parmi plusieurs solutions pour le même défi pour trouver celle qu'ils voulaient référencer. Bien que cela ait pu être un exercice intéressant pour certains, c'était une distraction par rapport au codage et à la construction de projets.

Notre solution a impliqué deux étapes :

1. trouver les endpoints API très fréquentés qui provoquaient l'écriture dans la base de données, et les changer d'une action « save » à une action « update » (ce qui minimise le volume de données envoyées sur le réseau).
2. modifier la façon dont nous stockons les défis complétés, en passant d'un grand tableau à une carte clé-valeur.

Ainsi, un campeur ne pouvait avoir qu'une seule solution par défi. Cela a considérablement réduit la taille de l'objet completedChallenges.

Nous avons déployé notre correctif au milieu d'un jeudi après-midi, alors que nous avions environ 400 campeurs simultanés. C'était un pari, mais cela a payé. Nous avons immédiatement vu une amélioration de l'utilisation de notre CPU.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8OJTlQT0LuXHHqN5Lnk6xQ.png)
_Le résultat immédiat_

Le grand enseignement est le suivant : si votre application semble ralentir, il y a de fortes chances que cela soit dû à des requêtes de base de données inefficaces.

Si vous pouvez les trouver et les corriger, vous pourrez reporter les extensions coûteuses de votre infrastructure, tout en maintenant la vitesse à laquelle vos utilisateurs se sont habitués.