---
title: Les épics sont morts. Voici ce que nous devrions faire à la place.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-18T21:59:26.000Z'
originalURL: https://freecodecamp.org/news/epics-are-dead-heres-what-we-should-do-instead-279bada1e644
coverImage: https://cdn-media-1.freecodecamp.org/images/0*OaKd4OM6oZkPAvbQ.jpg
tags:
- name: agile
  slug: agile
- name: business
  slug: business
- name: Productivity
  slug: productivity
- name: Scrum
  slug: scrum
- name: technology
  slug: technology
seo_title: Les épics sont morts. Voici ce que nous devrions faire à la place.
seo_desc: 'By Bertil Muth

  What has not been declared dead already? Test Driven Development was buried years
  ago. Still, it continues to spread. Of course, Agile is dead as well. But even traditional
  companies come into contact with Scrum. The dead continue to l...'
---

Par Bertil Muth

Qu'est-ce qui n'a pas encore été déclaré mort ? Le [Développement Piloté par les Tests (TDD)](https://dhh.dk//2014/tdd-is-dead-long-live-testing.html) a été enterré il y a des années. Pourtant, il continue de se répandre. Bien sûr, [l'Agile est mort](https://www.youtube.com/watch?v=a-BOSpxYJ9M) également. Mais même les entreprises traditionnelles entrent en contact avec Scrum. Les morts continuent de vivre, mais déclarer quelque chose de mort est toujours bon pour un titre accrocheur. En ce sens, assistez à la manière dont je détruis les épics en tant que pratique agile.

### Qu'est-ce que les épics ?

Le terme est vague. Cela présente des avantages. Les épics sont plus pour la communication que pour la spécification. Le flou les rend polyvalents. Mais il y a un risque de malentendus. Je m'en tiens à la définition de Mike Cohn :

> Un épic Scrum est une grande histoire utilisateur. ([Source](https://www.mountaingoatsoftware.com/blog/stories-epics-and-themes))

J'utilise le terme comme suit : Un épic est une histoire trop grande pour être implémentée dans un sprint Scrum. Les éléments en haut du Product Backlog ne sont donc pas des épics, mais de petites histoires. Plus bas dans le backlog, vous trouverez typiquement des épics. Avec le temps, les épics sont « découpés » en histoires qui peuvent être intégrées dans un sprint.

C'est ce que j'ai enseigné pendant des années dans mes cours de formation. Cela semble être le consensus général. Intuitif à première vue. Je suis ici pour expliquer pourquoi ce n'est pas pratique.

### 3 façons peu pratiques de gérer les épics

Jusqu'à présent, j'ai rencontré trois façons dont les entreprises gèrent les épics. Aucune d'entre elles n'est pratique. Appelons-les :

#### Dissolution

![Image](https://cdn-media-1.freecodecamp.org/images/OO4-EKucR2gZhVJilqHLfLwnBOBxvqM0fgkA)
_1. Dissolution_

#### Liens

![Image](https://cdn-media-1.freecodecamp.org/images/hT9ibQZCCuFNl60RAWY2ZkOvmR7-1idajU0k)
_2. Liens_

#### Arbres

![Image](https://cdn-media-1.freecodecamp.org/images/9PrBM9HZpNEftSfygOJFwVKtoCpYMVZj15ga)
_3. Arbres_

### 1. Dissolution

Le principe de dissolution est simple. Un épic est complètement décomposé en ses composants, les petites histoires individuelles.

Par exemple, un épic « Réserver un vol » d'un portail de vols en ligne peut être décomposé en étapes de processus individuelles. Ainsi, « Se connecter », « Rechercher un vol », et ainsi de suite. Chaque étape de processus devient une histoire. L'équipe estime l'histoire. Tant qu'elle est trop grande, l'équipe continue de la découper. Une fois que toutes les histoires sont assez petites pour tenir dans des sprints, l'équipe supprime l'épic et commence le développement des histoires.

C'est l'idée sous-jacente de complétude qui me dérange. La dissolution suggère qu'un sujet peut être complété avec un périmètre prédéterminé. Mais si des changements aux histoires sont possibles pendant le développement, vous ne pouvez pas définir toutes les histoires à l'avance.

Le Guide Scrum dit :

> Un product backlog n'est jamais complet. [] Les exigences ne cessent jamais de changer.

Si vous devez livrer un périmètre fixe, arrêtez de prétendre. Oubliez les épics et décrivez les exigences détaillées à l'avance. Ne prétendez simplement pas être agile alors.

### 2. Liens

Si vous ne dissolvez pas complètement vos épics, il est logique d'utiliser des liens. Les épics restent, en bas du backlog. Vous liez de nouvelles petites histoires aux épics dont elles dérivent.

Le risque est qu'avec le temps, le nombre d'épic augmente. Le backlog devient gonflé. Il contient des épics dont vous n'avez plus besoin. Le partie prenante n'est plus dans l'entreprise. Ou le sujet n'est plus pertinent.

Bien sûr, vous pouvez nettoyer votre backlog de temps en temps. Je considère cela comme un travail sans valeur ajoutée. Et vous pouvez l'éviter, comme je le décrirai plus tard.

### 3. Arbres

Une autre façon est la représentation des épics et des histoires sous forme d'arbre :

![Image](https://cdn-media-1.freecodecamp.org/images/fQdxdGv7x3ec26JpDMXcMLhbuvOwBjyXHO8F)
_Représentation des épics sous forme d'arbre_

Vous regroupez les petites histoires par épic. Pas une mauvaise idée. Mais ce que vous perdez, c'est la liste ordonnée du backlog. Comment déterminez-vous l'ordre de mise en œuvre alors ?

Bien sûr, vous pouvez utiliser un outil numérique qui prend en charge les deux vues. Le risque : vous investissez trop de temps et d'efforts dans les outils. Quelles sont les vues ? Quels sont les attributs ? Quel est le modèle de données sous-jacent ? Des questions intéressantes. Mais dans une approche agile, elles ne devraient pas avoir une priorité élevée.

En résumé, l'idée de regroupement est bonne. Mais le faire est chronophage.

### L'alternative aux épics

Il existe depuis longtemps une alternative. Elle est même mentionnée dans le même article de blog de Mike Cohn, que j'ai lié ci-dessus.

Je parle des _thèmes_.

Un thème peut être considéré comme un attribut supplémentaire des histoires. Normalement, plusieurs histoires partagent le même thème. L'histoire « Rechercher un vol » pourrait avoir le thème « Réserver un vol ». Un extrait du backlog pourrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/-iL6f0xFP4aFfnxgRCmzK3Nkouv1csAh-S5m)
_Histoires utilisateur avec thème_

Les thèmes ne sont pas gérés comme des éléments de backlog séparés. Cela élimine le travail de nettoyage discuté dans le chapitre Liens. C'est bien.

Mais ce que vous perdez, c'est le processus d'affinage progressif des grands épics aux histoires qui peuvent être implémentées dans un sprint. C'est mauvais.

Heureusement, il existe des pratiques qui permettent de faire cet affinage en dehors du backlog. Une façon d'identifier les thèmes est un diagramme de cas d'utilisation :

![Image](https://cdn-media-1.freecodecamp.org/images/A9k8qh6lfEKpCj0aqpFMpxLiuE4igVNT5cua)

Ce qui est bien avec ces diagrammes, c'est qu'ils montrent le « Big Picture » grâce au haut niveau d'abstraction et à la représentation graphique. Pour cela, un backlog est inadapté.

Les noms des cas d'utilisation deviennent ensuite des thèmes dans le backlog. Mais comment passe-t-on des cas d'utilisation aux histoires ? Pour cela, le Story Mapping de Jeff Patton est bien adapté :

![Image](https://cdn-media-1.freecodecamp.org/images/KrweoAjq2JO5T6ckmRnIY7DRq5pPCd3HlH3E)

Les deux premières lignes de la carte d'exemple montrent les cas d'utilisation « Réserver un vol » et « Gérer le profil » et leur flux de base. Sous les étapes individuelles, l'équipe accroche les alternatives : autres processus, erreurs, etc. Ces notes jaunes sont appelées tâches utilisateur.

Lors de l'affinage du backlog, l'équipe dérive les histoires des tâches utilisateur. Une tâche peut servir de titre à l'histoire. L'équipe ajoute des détails comme les critères d'acceptation aux histoires.

### Les conséquences

L'application de cette approche alternative a des conséquences. Par exemple, le Product Backlog ne contiendra que des histoires pour les 1-2 prochains sprints. Donc peut-être 10-20 histoires.

Toutes les activités comme la priorisation supplémentaire, l'estimation et l'élaboration des critères d'acceptation n'ont lieu qu'avec ces histoires. Comme le dit le 10ème principe agile :

> Simplicité — l'art de maximiser la quantité de travail non fait — est essentiel.

Si la direction veut avoir des informations sur l'avancement du développement, cela est possible à trois niveaux :

* Les **diagrammes de cas d'utilisation ou les thèmes** fournissent la perspective à long terme pour la direction. Pour 1 an, ou même au-delà. Mais : ils ne sont pas adaptés pour spécifier les détails.
* Les **story maps** forment la base pour la planification des releases. Les parties prenantes intéressées par la release créent la story map avec les membres de l'équipe. (En raison de nouvelles découvertes, le périmètre peut changer pendant le développement.)
* Ceux qui veulent avoir un aperçu approfondi et influencer les détails pendant le développement participent à la **Revue de Sprint** et à l'**Affinement du Backlog**.

Ce n'est qu'à basse altitude que nous voyons les détails. Et le Product Backlog est essentiellement comme une liste de courses. Écririez-vous ce que vous voulez acheter dans un an ?

Enfin, mais non des moindres, la mort des épics annonce la fin du consumérisme. Si vous voulez quelque chose, vous devez vous mettre d'accord avec l'équipe et travailler en étroite collaboration.

### Post mortem

Dans la discussion avec des collègues, ils ont souligné que même après une dissolution d'un épic, de petites histoires peuvent être ajoutées. C'est vrai, et pour moi c'est une solution acceptable. Ce qui est perdu dans ce cas, cependant, c'est le « Big Picture » que j'ai montré dans le diagramme de cas d'utilisation.

En fin de compte, l'adéquation d'un produit pour les utilisateurs détermine son succès. Pas la manière dont il a été fait. Cela s'applique à toutes les pratiques de développement, y compris les épics. Peut-être avez-vous trouvé une manière sensée de gérer les épics ?

_Apprenez à [gérer votre Product Backlog efficacement](https://skl.sh/2Edz9Zu) en visitant mon cours en ligne. Cet article a été publié pour la première fois sur [HOOD Blog](https://blog.hood-group.com/blog/2019/01/02/epics-sind-tot/) en allemand._