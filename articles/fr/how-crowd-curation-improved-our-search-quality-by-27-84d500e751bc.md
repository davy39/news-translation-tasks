---
title: Comment le crowd curation a amélioré notre qualité de recherche de 27%
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-09T22:30:29.000Z'
originalURL: https://freecodecamp.org/news/how-crowd-curation-improved-our-search-quality-by-27-84d500e751bc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qRLVVbI9mEUK2IOyLbGJ-w.jpeg
tags:
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment le crowd curation a amélioré notre qualité de recherche de 27%
seo_desc: 'By Thanesh Sunthar

  The bigger your platform gets, the more vital search becomes. And if you run a content-heavy
  platform like ours, it’s even more critical that you get search right.

  Retrieving relevant information from millions — potentially billion...'
---

Par Thanesh Sunthar

Plus votre plateforme grandit, plus la recherche devient vitale. Et si vous gérez une plateforme riche en contenu comme la nôtre, il est encore plus crucial de bien faire les choses en matière de recherche.

Récupérer des informations pertinentes parmi des millions — potentiellement des milliards — d'enregistrements n'est pas une tâche triviale. Le problème de la recherche est si complexe qu'il a sa propre discipline dédiée à sa résolution, appelée _Science de l'Information_.

![Image](https://cdn-media-1.freecodecamp.org/images/0rri81CA7EmZFg7HClsESnuYWg1aUfcYSMYy)
_Les 6 sites web les plus visités montrant l'importance de la recherche_

Les six sites web les plus visités au monde présentent tous une barre de recherche proéminente dans leur panneau de navigation. Facebook, YouTube et Amazon ont choisi de placer la barre de recherche juste à côté de leur logo, soulignant à quel point la recherche est devenue importante pour ces plateformes. Google, le site web numéro un au monde, a été initialement construit autour de ce seul problème — la recherche !

### **La recherche est une navigation**

La recherche est le moyen principal par lequel les gens découvrent du contenu sur une plateforme. Peu de gens prendront vraiment le temps d'apprendre la hiérarchie de votre plateforme. Dans chaque catégorie, il y a de nombreuses autres plateformes qui rivalisent pour le temps de vos utilisateurs, donc ces hiérarchies évoluent constamment, de toute façon.

Quand était la dernière fois que vous avez utilisé une _barre de menu_ ? Ou même utilisé des _filtres de recherche avancés_ ? À moins que vous ne forciez les utilisateurs à utiliser ces outils, ils tendent naturellement à les éviter. Donc, si ce n'est pas assez facile pour les utilisateurs de découvrir votre contenu via la recherche, ils perdront intérêt et passeront à autre chose.

### **_Curating Search Results_**

Lorsque les résultats de recherche ne sont pas pertinents pour l'utilisateur, ils ne prendront pas l'action suivante et ne cliqueront sur aucun des résultats. La curation aide à augmenter la pertinence des résultats de recherche.

Mon entreprise, Flipp, prend les circulaires hebdomadaires des détaillants et les rend recherchables. Voici la différence entre les résultats _non curatés_ et _manuellement curatés_ lorsque vous recherchez « cake » sur Flipp :

![Image](https://cdn-media-1.freecodecamp.org/images/4vOcnEFNgSIPg9id9H0fadNxv2H4IxuMAFf5)
_Résultats de recherche non curatés VS résultats de recherche manuellement curatés_

La curation manuelle est le processus par lequel un humain vérifie chaque terme de recherche, puis organise manuellement l'ordre de tri des résultats. Il est clair que notre version manuellement curatée montre un ensemble de résultats de recherche beaucoup plus propre et plus pertinent pour l'utilisateur.

Vous pouvez automatiser certains aspects de la curation manuelle, mais cela reste une tâche intensive en ressources.

### **_Enter Crowd Curation_**

Bien que la curation manuelle soit un excellent moyen de commencer, ce n'est pas une solution évolutive. Nous avons besoin d'une meilleure approche.

C'est là que la _crowd curation_ entre en jeu. Elle utilise la [sagesse de la foule](https://en.wikipedia.org/wiki/Wisdom_of_the_crowd) pour trier l'ordre des résultats de recherche.

Une approche simple consiste à voir quels éléments les utilisateurs cliquent le plus, puis à les faire remonter en haut des résultats de recherche. Voici un exemple des résultats de recherche pour la requête « bbq » avant et après la crowd curation :

![Image](https://cdn-media-1.freecodecamp.org/images/eYGMBJVAEUf4b19qA2JeBYajeqtuoYr4kF77)
_Crowd curation du terme de recherche « bbq »_

Comme vous pouvez le voir, mesurer le nombre de clics sur un élément et trier les résultats en fonction de cela donne de bien meilleurs résultats de recherche. Mais parce que les éléments changent quotidiennement dans notre application, nos résultats de recherche nécessitent un réajustement périodique. Nous gardons les résultats de recherche frais afin que les offres expirées disparaissent et que les offres plus nouvelles et plus « dignes d'intérêt » montent en haut.

Nous devons nous assurer de ne pas pénaliser les nouveaux éléments des circulaires par rapport aux anciens éléments, qui ont reçu plus d'impressions et donc collecté plus de clics. Cela crée d'autres défis intéressants pour notre équipe de développement.

La recherche est également légèrement différente sur les plateformes mobiles. Parce que la taille de l'écran est plus petite, nous devons également prendre en compte ce qui est réellement affiché dans la fenêtre d'affichage.

Il y a plus de chances qu'un utilisateur clique sur un élément qui est affiché en haut (au-dessus de la ligne de flottaison) plutôt que sur des éléments plus bas dans la liste qu'ils doivent faire défiler (en dessous de la ligne de flottaison). Si l'utilisateur fait l'effort de faire défiler vers le bas pour trouver un élément, cela doit également être pris en compte lorsque nous améliorons l'ordre de tri de nos résultats de recherche.

### **_Mesurer la qualité de la recherche_**

La mesure la plus importante d'un moteur de recherche est la qualité de ses résultats de recherche. Ici, l'écart entre les recherches et les clics s'élargit, et la recherche se dégrade :

![Image](https://cdn-media-1.freecodecamp.org/images/XcQYOnxEAlWX6zZ8O4tYrBokpDfCKYw89kKU)
_Recherches VS Clicks_

Nous utilisons le [Taux de Clics](https://en.wikipedia.org/wiki/Click-through_rate) — le ratio des utilisateurs qui cliquent sur un élément spécifique par rapport au nombre total d'utilisateurs qui voient ces résultats de recherche — pour mesurer l'efficacité de notre moteur de recherche.

Nous utilisons également le [Gain Cumulatif Actualisé](https://en.wikipedia.org/wiki/Discounted_cumulative_gain) pour mesurer la qualité de nos algorithmes de classement.

Une façon simple de visualiser l'« uplift » — l'amélioration des résultats — est de mesurer les clics supplémentaires générés à chaque rang des résultats de recherche. Nous avons utilisé cela pour conclure que **en utilisant la crowd curation, nous avons vu une augmentation de 27% des clics générés à partir du premier résultat.**

La plupart des clics se sont déplacés vers les rangs supérieurs, prouvant que nous avions amélioré la qualité et la pertinence de nos résultats de recherche.

![Image](https://cdn-media-1.freecodecamp.org/images/xseM5VYbnXNcigoso5S1fpMCn0h5SoXIbX7Q)
_Augmentation des clics dans les résultats de recherche_

Et oui, notre algorithme tient également compte de la durée pendant laquelle un élément a été disponible dans la recherche.

Par exemple, si un circulaire est sorti le mercredi, la « dignité d'intérêt » des éléments de ce circulaire diminuerait à mesure que nous avançons dans la semaine, donnant plus d'importance aux éléments des circulaires sortis plus récemment que le mercredi. Nous équilibrons cela avec le nombre de clics.

En d'autres termes :

_Classement de l'élément = Formule(Âge de l'élément, Clics)_

De cette façon, nous sommes en mesure d'atténuer quelque peu les effets de [winner-takes-all](https://en.wikipedia.org/wiki/Winner_takes_all).

Chez Flipp, nous voulons que l'expérience utilisateur soit magique. Nous sommes une entreprise axée sur les données qui examine constamment les données pour trouver de nouvelles façons d'améliorer la vie de millions d'utilisateurs. La recherche n'est qu'un domaine où nous appliquons ce principe, mais c'est un domaine important.

_Je suis Thanesh, un chef de produit senior chez [Flipp](https://flipp.com/). J'ai publié une autre version de ceci sur le [blog d'ingénierie de Flipp](http://eng.flipp.com/using-crowd-curation-to-enrich-search/). Si vous êtes intéressé à réinventer la façon dont les gens achètent des choses, consultez nos [offres d'emploi actuelles](https://corp.flipp.com/jobs)._