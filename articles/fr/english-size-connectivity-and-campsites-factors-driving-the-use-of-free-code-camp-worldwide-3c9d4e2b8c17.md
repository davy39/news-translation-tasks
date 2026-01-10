---
title: Anglais, Population, Connectivité et Campsites
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-01-20T08:02:19.000Z'
originalURL: https://freecodecamp.org/news/english-size-connectivity-and-campsites-factors-driving-the-use-of-free-code-camp-worldwide-3c9d4e2b8c17
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wOQNiJVfv1weV_KLotsnyA.jpeg
tags:
- name: data
  slug: data
- name: Data Science
  slug: data-science
- name: education
  slug: education
- name: social media
  slug: social-media
- name: technology
  slug: technology
seo_title: Anglais, Population, Connectivité et Campsites
seo_desc: 'By Evaristo Caraballo

  Factors driving the use of Free Code Camp worldwide

  Free Code Camp offers a coding education that’s open source, free, and accessible.
  Sounds ideal, right?

  Actually, there are several areas where it can improve significantly — e...'
---

Par Evaristo Caraballo

#### Facteurs influençant l'utilisation de Free Code Camp dans le monde

Free Code Camp offre une éducation en codage qui est open source, gratuite et accessible. Cela semble idéal, n'est-ce pas ?

En réalité, il existe plusieurs domaines où il peut s'améliorer significativement — surtout pour les personnes en dehors des États-Unis.

J'ai récemment analysé les données ouvertes de Free Code Camp et j'ai découvert que l'adoption mondiale de Free Code Camp est affectée par plusieurs facteurs. Pour être juste, ceux-ci semblent être les mêmes facteurs qui affectent d'autres programmes en ligne complets et des cours en ligne (MOOCs). Ces facteurs incluent la richesse du pays d'origine des apprenants, la connectivité, la taille de la population, la maîtrise de l'anglais et — bien que moins documenté — l'existence de communautés hors ligne actives.

On peut le constater en lisant les publications sur les réseaux sociaux des campeurs — les membres de la communauté de Free Code Camp — que la maîtrise de l'anglais et la socialisation affectent l'utilité de Free Code Camp pour un campeur donné. Cet article explorera ces points, ainsi que des facteurs moins évidents.

Pour obtenir une approximation de la manière dont la géographie affecte l'utilité de Free Code Camp, j'ai recherché des différences dans les **_nombres de sessions_** (provenant de Google Analytics) pour les régions et les pays, en basant la comparaison sur des données démographiques pertinentes.

J'ai commencé par comparer de manière générale le nombre _absolu_ de sessions entre les régions subcontinentales. Il suffit de jeter un coup d'œil à cette carte pour réaliser que l'adoption de Free Code Camp en Afrique, en Asie centrale et dans les plus petites îles du Pacifique est très en retard par rapport aux autres régions.

![Image](https://cdn-media-1.freecodecamp.org/images/1*J8ILk6IET7PbHh7chTkWEg.png)
_Carte de la prévalence des sessions de Free Code Camp (en pourcentages) par sous-continents dans le monde (carte vierge des continents de [boragetaqs.es.tl](http://boragetaqs.es.tl/continents-map-blank.htm" rel="noopener" target="_blank" title="))_

Cela indique que le fait d'avoir une **_économie saine_** ou d'appartenir à sa périphérie _pourrait être_ un facteur pertinent affectant l'adoption du programme. En fait, la richesse du pays pourrait être fortement liée à l'adoption du programme, comme nous pouvons le voir en explorant certaines données démographiques des 20 premiers pays en termes de sessions.

Le tableau ci-dessous inclut également certaines des nations les plus riches, contenant 16 des 79 pays avec un PIB par habitant supérieur à la moyenne (PIB mondial par habitant (2015) = Int'l $14 982, [wikipedia en janvier 2016](https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28PPP%29_per_capita)).

![Image](https://cdn-media-1.freecodecamp.org/images/1*R1tRk7yV3te39uLNSafB9Q.png)

Cependant, avoir une économie saine ne suffit pas pour expliquer le tableau. Un examen plus approfondi suggère que la **_taille de la population internet_** est un facteur déterminant d'influence : la liste représente 60 % de la population totale mondiale, mais plus important encore, elle représente **_68 %_** de la population internet **_mondiale_**. 

D'accord, jusqu'à présent, nous avons trouvé des preuves que la richesse économique et la taille de la population (internet) affectent la probabilité qu'une personne donnée rejoigne la communauté Free Code Camp. Quels sont les autres facteurs ?

Un facteur semble être la maîtrise de l'anglais. L'autre semble être la présence de campsites — des chapitres basés dans les villes de Free Code Camp où les campeurs se rencontrent et codent ensemble.

Pour le découvrir, nous devons examiner les données **_en termes relatifs_** et éliminer les enregistrements exceptionnels afin de révéler leur impact.

Pour cette étape, j'ai filtré les grands pays comme les États-Unis, le Canada, le Royaume-Uni, l'Inde et la Chine, ainsi que comparé uniquement les pays avec des données complètes.

J'ai également recalculé le nombre de sessions et le nombre de campsites _contrôlés par_ la taille de la population internet, afin qu'ils montrent une tendance relative.

Au lieu d'un simple tableau, je me suis appuyé sur un nuage de points des nombres modifiés de campsites et de sessions, avec quelques fonctionnalités supplémentaires :

* la **taille** du point représentait la taille comparable de la **population internet** dans chaque pays (grande si supérieure à la moyenne, petite si inférieure à la moyenne)
* la **couleur** du point indique la **maîtrise de l'anglais** (basée sur l'[_English Proficiency Index_](http://www.ef.nl/epi/) d'Education First) pour chaque pays sélectionné — violet si supérieur à la moyenne, vert si inférieur à la moyenne

![Image](https://cdn-media-1.freecodecamp.org/images/1*q0xrVWW1Tix3Heo5H7MMmg.png)
_Nuage de points des campsites vs sessions : les relations entre le nombre relatif de sessions vs campsites ou la maîtrise de l'anglais sont suggérées (résidus non standardisés après transformation en log10 et contrôle des deux variables pour la population internet ; les points ont été traduits)_

Le graphique ci-dessus révèle plusieurs informations simultanément :

1. Plus le nombre de campsites est élevé, plus la quantité relative de sessions est élevée. Cet effet est particulièrement flagrant entre les pays avec de grandes populations internet.
2. Les pays avec une meilleure maîtrise de l'anglais (points violets) pourraient être considérés comme plus actifs _en termes relatifs_ que ceux avec une maîtrise de l'anglais plus faible (points verts), peu importe la taille de la population internet du pays.

Ainsi, non seulement la richesse d'un pays donné et la taille de sa population internet sont importantes — la **maîtrise de l'anglais** et une **communauté hors ligne active** semblent également affecter la diffusion de Free Code Camp dans un pays donné.

En résumé :

1. À un _niveau élevé_, les régions les plus riches sont celles qui ont le plus de sessions ; nos campeurs proviennent largement de pays de ces régions, comme les États-Unis, le Canada ou plusieurs pays européens.
2. Cependant, en comparant les pays _indépendamment_, nous pouvons affirmer que l'existence d'une grande population internet est en fait très pertinente lorsque nous parlons de nombres absolus. Certains exemples de cela sont l'Inde, le Brésil, la Russie, les Philippines et probablement la Chine (nous capturons seulement une fraction des sessions là-bas puisque le Grand Pare-feu bloque Google Analytics pour tout le trafic non-VPN).
3. Les pays avec une forte maîtrise de l'anglais adoptent plus largement Free Code Camp, bien que pour le voir, nous devions _contrôler par_ la taille de la population internet.
4. Enfin, si vous contrôlez pour la taille de la population internet, vous pouvez voir que le nombre de campsites semble être lié au nombre de sessions, suggérant que le codage en personne augmente l'activité des campeurs sur le site web de Free Code Camp.

#### Que fait donc Free Code Camp à propos de tout cela ?

Même avant cette analyse, notre communauté a pris des mesures pour réduire les barrières linguistiques à l'adoption. Une petite armée de campeurs a volontairement traduit le programme open source de Free Code Camp, le wiki et d'autres ressources pédagogiques dans différentes langues du monde.

Vladimir Tamara, un membre de l'équipe principale à Bogotá, en Colombie, a déjà supervisé la traduction du programme en espagnol. Il coordonne maintenant l'effort de traduction pour d'autres langues du monde et aide à écrire le code qui gérera les options de langue.

Dans un effort pour réduire l'impact d'une mauvaise connectivité et du grand nombre de campeurs qui utilisent des smartphones comme leur appareil internet principal — ou unique —, Free Code Camp améliore continuellement l'expérience mobile. Nous travaillons également sur un mode hors ligne pour les campeurs qui manquent d'un accès internet stable et d'électricité.

Une tendance intéressante qui a émergé de mon analyse est la relation entre le nombre de sessions et le nombre de campsites dans un pays donné. Ces groupes en personne peuvent servir à attirer et à impliquer des campeurs qui n'auraient autrement pas l'initiative de persévérer dans un programme exigeant comme Free Code Camp.

Justin Richardsson, un designer visuel à Toronto, au Canada, a récemment rejoint notre équipe principale pour se concentrer sur les campsites. Il a déjà organisé de nombreux événements de codage par l'intermédiaire du campsite de Toronto. Son objectif est d'apprendre des autres responsables de campsites et de diffuser leurs connaissances aux campsites du monde entier.

Je travaille également sur des visualisations connexes à [bl.ocks.org/evaristoc](http://bl.ocks.org/evaristoc).

Cette analyse ne fait qu'effleurer la surface de ce que nous pouvons apprendre des [données ouvertes de Free Code Camp](https://medium.freecodecamp.com/free-code-camp-christmas-special-giving-the-gift-of-data-6ecbf0313d62#.79rr68eop). Rejoignez notre [salon de discussion Data Science](http://gitter.im/freecodecamp/datascience) et aidez-nous à donner un sens à toutes ces données.