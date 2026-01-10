---
title: Comment j'automatise toutes les parties ennuyeuses de mon travail avec Create
  React App DevOps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-15T19:06:16.000Z'
originalURL: https://freecodecamp.org/news/designing-a-newspaper-as-a-freakin-progressive-web-app-22acf4eb5a68
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vx2DokMCll5imkF7cFP0EQ.png
tags:
- name: Design
  slug: design
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: UX
  slug: ux
seo_title: Comment j'automatise toutes les parties ennuyeuses de mon travail avec
  Create React App DevOps
seo_desc: 'By James Y Rauhut

  A lot of my work lately has been making design system specs and tools for IBM. Yet,
  I needed a break back into product design. So over the last couple of weeks, I spent
  free time working on a fun design challenge.

  I am going to walk...'
---

Par James Y Rauhut

Beaucoup de mon travail récemment a consisté à créer des spécifications et des outils de système de design pour IBM. Pourtant, j'avais besoin d'une pause pour revenir à la conception de produits. Ainsi, au cours des dernières semaines, j'ai passé mon temps libre à travailler sur un défi de design amusant.

Je vais vous guider à travers comment j'ai identifié un problème, je me suis poussé dans une nouvelle direction et j'ai appris quelques nouveaux trucs.

Notez que j'ai écrit un article complémentaire sur la façon de coder ce site d'actualités Progressive Web App [ici](https://medium.freecodecamp.org/coding-a-newspaper-as-a-freakin-progressive-web-app-e456d4a2b9cd).

### Identifier le problème

Concevoir pour soi-même est le projet le plus facile que vous aurez jamais.

En travaillant, j'ai remarqué un nouveau comportement au travail. Je m'ennuyais sur une tâche après un certain temps et je vérifiais ensuite r/WorldNews sur Reddit. Le problème était que je voulais parcourir cette page pour me sentir à jour sur les événements actuels, mais ce n'est pas ce qui s'est passé.

La page se concentre sur les aspects communautaires avec les votes positifs et les commentaires. Certes, c'est pour cela que Reddit a été conçu.

![Image](https://cdn-media-1.freecodecamp.org/images/-boLCoBQcsUN0UY-OK0PMo6beW-w866aomRI)

L'avantage de r/WorldNews est que les titres en haut sont votés positivement parce que d'autres les ont trouvés importants ou intéressants.

Je voulais me concentrer sur ces titres et avoir également la possibilité d'approfondir une histoire. Les commentaires me distrairaient de le faire. J'ai déjà vu une étude disant que les utilisateurs de Reddit étaient plus susceptibles d'aller directement aux commentaires au lieu de cliquer sur le lien publié. Je savais que c'était vrai d'après mon propre comportement et cela m'a empêché d'atteindre mon objectif initial de lire les articles.

J'ai donc fixé un objectif pour l'expérience utilisateur :

> Un utilisateur peut rester à jour sur les principales actualités du web sans les distractions de la communauté.

### Rester skeuomorphe

Écoutez, parfois vous avez besoin d'une pause dans ce sur quoi vous travaillez. Vous devez faire un pas en arrière et faire exactement le contraire. Dans ce cas, j'avais besoin de m'éloigner de mes designs plus plats qu'une crêpe. J'avais besoin d'arrêter d'abstraire l'UI comme Jackson Pollock.

J'avais besoin de revenir à la folie skeuomorphe de la fin des années 2000. Tout ressemblait à des objets analogiques. J'ai décidé de devenir skeuomorphe avec les journaux.

Le dimanche matin, enfant, mon père et moi allions dans un restaurant Tex-Mex pour manger des tacos de petit-déjeuner et lire le journal local. Il y avait un bonheur dans ces moments parce que vous scanniez les histoires pendant une heure. Vos yeux sautaient pour trouver la prochaine histoire que vous priorisiez. Il n'y avait pas d'opinions à part Dear Amy qui me disait comment gérer mon harceleur inexistant au travail.

J'ai donc fixé un objectif pour le design visuel :

> L'apparence n'intégrera des éléments basés sur le web que si nécessaire et émulera un journal physique autant que possible.

![Image](https://cdn-media-1.freecodecamp.org/images/55lt7sDiboOY5SCaip30Vi8MmLrqMFIFGcGm)

J'avais déjà vu que le [New York Times](https://www.nytimes.com/) et le [Financial Times](https://www.ft.com/) faisaient un excellent travail d'émulation de leurs racines non numériques. Mais je suis resté à l'écart d'eux pour voir quels motifs je pouvais reconnaître à partir des mises en page des journaux eux-mêmes.

C'était un plaisir de parcourir les journaux, et il y avait beaucoup de tendances identifiables :

* Échelle de typographie dramatique
* Mise en page en maçonnerie
* Texte justifié
* Juste assez d'images pour capter l'attention initiale
* Une rupture d'en-tête avec les détails de l'édition
* Texture douce et froissée

### Aller à la presse

Rester fidèle aux tendances des journaux m'a aidé à itérer sur le design. Les seuls croquis que je devrais montrer sont des rectangles solides pour la mise en page. Cela est dû au fait que je travaille plus rapidement en prototypant directement dans le code. La seule fois où j'ai eu l'impression de rompre le skeuomorphisme était pour supporter le mode hors ligne.

Dans cette situation, je devais informer l'utilisateur qu'il regardait des histoires obsolètes en fonction de sa connexion :

![Image](https://cdn-media-1.freecodecamp.org/images/CACKFDpBpQwxTgyfydPUy09GOJge5daB5cjc)

Beaucoup de motifs UX hors ligne incluent une interaction "tentative de reconnexion", mais je croyais que cela allait à l'encontre de l'objectif visuel que je m'étais fixé précédemment. La raison était que les utilisateurs savent déjà comment actualiser une page dans leur navigateur et que les histoires seraient automatiquement mises à jour si leur appareil retrouvait une connexion de toute façon.

Une statistique de performance basée sur les utilisateurs qui se portait mal pendant que je travaillais sur cela était l'indice de vitesse perceptuelle. Cela mesure la rapidité avec laquelle l'utilisateur perçoit l'expérience en fonction de la rapidité avec laquelle les éléments apparaissent visuellement. Le faible score était dû à un chargement rapide de la page, mais ensuite à un délai pour que les histoires apparaissent réellement. J'ai pu améliorer le score avec des squelettes de chargement pour les histoires.

**Note de côté** : Vous pouvez en apprendre davantage sur l'indice de vitesse perceptuelle et comment le mesurer dans ce guide : [The Quick, New Way Designers Can Test User-Centric Metrics](https://medium.com/design-ibm/the-quick-new-way-designers-can-test-user-centric-metrics-37e78daf48df).

![Image](https://cdn-media-1.freecodecamp.org/images/j2qXx8HKSKvFrrrYt0NDQ0CojZ1C-J1PbHn3)

Le dernier détail que j'ai senti obligé de développer était une conversion. Quelle action pourrais-je mesurer comme un accomplissement de ma part ? Se contenter de visiter le site n'était pas suffisant pour mesurer le succès. J'ai donc fini par positionner des "publicités" dans l'expérience.

Il existe deux types différents de publicités :

1. Tout le monde voit des liens pour faire un don à une œuvre de bienfaisance. L'espoir est que si un utilisateur devient un utilisateur fréquent, il cliquerait sur la même publicité caritative qu'il voit encore et encore.
2. Les utilisateurs avec des navigateurs Chrome et Firefox à jour voient des liens pour installer l'extension de navigateur. L'extension, Global Upvote Tab, fait de chaque nouvel onglet The Global Upvote tout en donnant à l'utilisateur un contrôle immédiat de sa barre d'URL.

### Le résultat final

![Image](https://cdn-media-1.freecodecamp.org/images/sbFMpLcnd-qO4qubK7VOJwyI3-6jUlTiSxCO)

Je suis satisfait de la façon dont ce projet parallèle de deux semaines s'est déroulé ! Respecter l'expérience utilisateur minimaliste et les objectifs visuels a permis de garder le projet bref, mais ciblé. Bien qu'il puisse s'agir d'une tricherie que je me considère comme l'utilisateur, je continue à apprécier [The Global Upvote](https://www.globalupvote.com/) comme mon expérience de nouvel onglet.

Si je revenais en arrière et faisais quelque chose de différent, je créerais plusieurs mises en page qui tournent lorsque l'utilisateur visite à différents moments. Cela éviterait à l'utilisateur de se lasser de toujours voir des images et des publicités à des endroits similaires. Le seul avantage que j'ai, grâce aux données dynamiques, est des hauteurs toujours changeantes.

J'espère que vous avez apprécié cette étude de cas !

Encore une fois, j'ai écrit un article complémentaire sur la façon de coder ce site d'actualités Progressive Web App [ici](https://medium.freecodecamp.org/coding-a-newspaper-as-a-freakin-progressive-web-app-e456d4a2b9cd).

Pour plus d'informations : N'hésitez pas à me contacter via les commentaires, [email](mailto:james@seejamescode.com), ou [@seejamescode](https://twitter.com/seejamescode). Je travaille à ATX pour IBM Design et j'adore toujours discuter avec la communauté du design web.