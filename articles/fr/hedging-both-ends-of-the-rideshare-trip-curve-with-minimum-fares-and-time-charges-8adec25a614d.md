---
title: L'objectif des tarifs minimaux et des frais de temps d'Uber
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-28T01:24:26.000Z'
originalURL: https://freecodecamp.org/news/hedging-both-ends-of-the-rideshare-trip-curve-with-minimum-fares-and-time-charges-8adec25a614d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tGaXyva_lSx9CeBM8PBhDw.png
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: uber
  slug: uber
seo_title: L'objectif des tarifs minimaux et des frais de temps d'Uber
seo_desc: 'By Ignacio Chavarria

  Uber and Cabify, the leading non-taxi rideshare companies in Latin America, both
  charge minimum fares. Only Uber has implemented time charges.

  After running a simulation of 72,000 trips, we were able to observe the financial
  impa...'
---

Par Ignacio Chavarria

Uber et Cabify, les principales entreprises de covoiturage non-taxi en Amérique latine, facturent toutes deux des tarifs minimaux. Seule Uber a mis en place des frais de temps.

Après avoir simulé 72 000 trajets, nous avons pu observer l'impact financier de l'option d'inclusion ou d'exclusion de fonctionnalités que nous identifions comme des outils précieux qui couvrent les deux extrémités de la _courbe de risque partenaire-conducteur_.

#### La courbe de risque partenaire-conducteur

Supposons que la société XYZ ne facture que par kilomètre et un tarif de base appelé _banderazo_ en Colombie et _bandeirada_ au Brésil. Au fait, **le tarif de base n'est [pas le même](https://www.quora.com/What-is-the-difference-between-Ubers-base-and-minimum-fare) que le tarif minimum.**

Pour un conducteur utilisant l'application de la société XYZ, tous les trajets ne sont pas égaux. Le graphique suivant montre comment le risque d'un conducteur variera en fonction de la longueur et de la vitesse des trajets, lorsqu'il n'est facturé que par distance. Le graphique suppose que tous les autres facteurs du trajet sont les mêmes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bbnzcEHhYey3atWlnnkAgQ.jpeg)
_En vous déplaçant vers la droite sur l'axe des X, la distance des trajets s'allonge. En montant sur l'axe des Y, cela signifie que les voitures se déplacent à des vitesses moyennes plus élevées. Le risque des conducteurs pour la société XYZ augmente dans la direction opposée par rapport à la vitesse moyenne du trajet. Cela est dû au fait que les conducteurs passent plus de temps sur les trajets sans facturer ce temps. Ce graphique n'est pas destiné à impliquer que les trajets suivent une distribution gaussienne. Les trajets suivent probablement une distribution asymétrique à droite, de type Pareto, comme le montre la simulation ci-dessous._

Comme montré ci-dessus, les conducteurs de la société XYZ n'aiment probablement pas les **trajets courts à faible vitesse** (en raison des embouteillages, des arrêts clients ou d'autres raisons) et surtout les **trajets longs à faible vitesse**. Les trajets longs à faible vitesse posent un risque beaucoup plus élevé aux conducteurs de la société XYZ, les forçant à assumer le coût d'opportunité (et les dépenses de carburant) du temps passé dans les embouteillages. **Lorsque les conducteurs ne facturent pas le temps, ce _risque de queue_ est directement placé sur eux.**

#### Simulation des trajets de covoiturage à Kanyeville

Pour le reste de cette étude, nous utiliserons les données obtenues en un mois à partir d'une simulation que nous avons réalisée pour un marché imaginaire appelé Kanyeville (oui, nommé d'après Yeezy).

La simulation fonctionne avec les hypothèses suivantes :

* La distance des trajets suit une distribution asymétrique à droite
* La distance moyenne des trajets est de 4 km
* 20 % des trajets ont une vitesse moyenne lente de 5 km/h, tandis que 80 % ont une vitesse moyenne normale de 40 km/h
* Chaque entreprise de covoiturage à Kville (comme l'appellent les locaux) a une moyenne de 200 conducteurs actifs quotidiens. Chaque conducteur effectue en moyenne douze trajets par jour, totalisant 72 000 trajets par mois et par entreprise.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gPbhggsiQV0kCxeIFYo2Ow.png)
_Données générées en utilisant [SciPy](https://www.scipy.org/" rel="noopener" target="_blank" title=")_

Le premier graphique montre la distribution des trajets, par distance, à l'échelle normale. Le second utilise une échelle logarithmique pour augmenter la visibilité de la queue de la courbe. Dans le graphique logarithmique, la forte variance dans la queue indique que **les trajets longs, ceux au-dessus de la distance moyenne des trajets (DMT), peuvent varier considérablement.** Dans cet échantillon, les conducteurs ont effectué des trajets allant jusqu'à 60 km.

Dans cette étude, nous avons analysé deux fonctionnalités de tarification qui impactent différentes extrémités de la courbe. **Les tarifs minimaux augmentent la monétisation à l'extrémité avant de la courbe** (où se trouvent les trajets courts, ce qui signifie que ceux en dessous de la DMT représentent environ 80 % du total des trajets). **Les frais de temps ont leur impact positif le plus élevé sur la queue de la courbe**, où se trouvent les trajets plus longs.

Bien sûr, les frais de temps affectent tous les trajets. Quiconque a déjà été dans une voiture connaît la différence entre être coincé dans les embouteillages en conduisant quelques pâtés de maisons et être coincé dans un embouteillage sur l'autoroute. Maintenant, imaginez être un conducteur de covoiturage qui n'est payé que par la distance. Nous mesurerons également ce que cette différence signifie financièrement pour les conducteurs.

### L'impact du tarif minimum

Pour mesurer l'impact du tarif minimum, le script suivant simule la valeur des tarifs des conducteurs sur un mois, avec et sans tarif minimum (TM) :

Les résultats de la simulation sont présentés dans l'illustration ci-dessous. Les tarifs bruts quotidiens sont comparés sous différents angles. Chaque scénario suppose une charge de 0,50 $/km et un tarif minimum de 2,50 $ :

![Image](https://cdn-media-1.freecodecamp.org/images/1*_TOt4l-GqVKA3a6xisSVOg.png)

Les graphiques de gauche comparent les distributions de fréquence pour les tarifs quotidiens. Les tarifs minimaux se déplacent de l'extrémité avant de la courbe vers des valeurs plus élevées. L'écart dans le graphique en haut à droite montre comment **les tarifs quotidiens moyens doublent presque** parce qu'un tarif minimum est facturé. Enfin, le graphique en bas à droite montre le bénéfice quotidien, en dollars, des tarifs minimaux. Il montre un **bénéfice quotidien moyen d'environ 17 $ par conducteur**. Pour être clair, ce sont les valeurs des tarifs bruts quotidiens et elles n'ont pas été ajustées pour les commissions de l'entreprise.

En termes de probabilité cumulative, le graphique suivant compare les courbes des valeurs des tarifs quotidiens pour les scénarios avec et sans tarif minimum :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zBsq-_63b4udfOGPzs0UmQ.png)

Les avantages des tarifs minimaux sont une fois de plus très clairs. **Près de 50 % des conducteurs de Kanyeville gagnent plus de 40 $/jour en tarifs bruts lorsqu'ils facturent des tarifs minimaux. Seulement 10 % des conducteurs qui ne facturent pas de tarif minimum gagnent plus de 40 $/jour.**

Ces résultats constituent un bon argument en faveur des tarifs minimaux. C'est probablement pourquoi les tarifs minimaux sont si courants. Mais quel est l'impact de la facturation à la minute ? Nous examinerons cela dans la section suivante.

#### L'impact des frais de temps

Pour mesurer l'impact de la facturation à la seconde, le script ci-dessous a été exécuté pour simuler un mois de tarifs de trajets individuels, par conducteur, avec et sans frais de temps :

_Note : Dans cette section, nous imaginons qu'il y a deux entreprises de covoiturage à Kanyeville : la société U et la société C. La seule différence entre leur structure tarifaire est que la première a un frais de temps de 0,05 $/minute._

Les résultats de la simulation sont présentés dans les quatre graphiques ci-dessous. Les tarifs des trajets individuels sont comparés entre les deux entreprises. Une entreprise ne facture que par distance (0,50 $/km) et l'autre facture à la fois par distance et par temps (0,50 $/km et 0,05 $/minute) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*qFl7V_AWz49RZSsQXDdt9w.png)
_En haut à gauche : Montre la distribution de fréquence des tarifs de trajet lorsque les entreprises facturent uniquement par distance. En haut à droite : Montre la distribution de fréquence des tarifs de trajet lorsque les entreprises facturent à la fois par distance et par temps. En bas à gauche : Identique au graphique en haut à gauche, mais sur une échelle logarithmique. En bas à droite : Identique au graphique en haut à droite, mais sur une échelle logarithmique._

Dans le graphique ci-dessus, la rangée du haut compare les distributions de fréquence des tarifs de trajet entre deux entreprises. Une entreprise facture uniquement pour la distance du trajet (en haut à gauche). Une autre entreprise facture à la fois pour la distance et le temps (en haut à droite). La deuxième rangée utilise une échelle logarithmique pour augmenter la visibilité de la queue pour les deux courbes.

Pourquoi utiliser une échelle logarithmique pour les résultats ? Parce qu'à l'échelle normale, les deux distributions semblent similaires (avec la plupart des occurrences de prix de tarif à l'avant des courbes). À l'échelle logarithmique, l'impact des frais de temps est beaucoup plus clair. La queue plus longue montre un plus grand nombre de trajets à tarifs élevés. Il est important de noter que **pour les entreprises représentées dans ce graphique, les valeurs moyennes des tarifs étaient de 3,50 $ et 4,00 $, respectivement. Cela indique une augmentation de 14 % des tarifs moyens.**

Les graphiques ci-dessous séparent les trajets à faible tarif des trajets à tarif élevé, pour les deux modèles de tarification, afin de revoir le changement des tarifs moyens et maximums.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WHzA1boF8NsV2Rw8dm4Rgg.png)

Les **frais de temps** ont à peine eu un impact sur les trajets à faible tarif (ceux en dessous de la moyenne), où ils ont augmenté les tarifs moyens de seulement environ 1 %. Cependant, les frais de temps **ont joué un rôle crucial sur les trajets à tarif élevé, où ils ont augmenté les tarifs moyens de 31 % et doublé les valeurs des tarifs maximums.**

De plus, les graphiques en violon suivants séparent les données par structure tarifaire, distance de trajet et vitesse de trajet :

![Image](https://cdn-media-1.freecodecamp.org/images/1*FhZor0hNr7ix9CY7kD10lA.png)

Comme prévu, **les trajets de longue distance avec des vitesses moyennes lentes ont vu la plus forte augmentation du prix des tarifs — plus du double — lorsqu'un frais de temps a été ajouté.** Sur les 41 000 $ de tarifs mensuels totaux dans cette simulation, **66 % provenaient de trajets longs et lents. Ceux-ci ne se sont produits que 5 % du temps.**

La fréquence des augmentations de tarifs peut être résumée succinctement comme suit :

* Il n'y a pas eu d'augmentation de tarif 60 % du temps
* Il y a eu une augmentation moyenne de tarif de 4 %, 15 % du temps
* Il y a eu une augmentation moyenne de tarif de 14 %, 20 % du temps
* Il y a eu une augmentation moyenne de tarif de 119 %, 5 % du temps

Les chances de voir une augmentation de tarif peuvent être mieux observées dans le graphique de probabilité cumulative suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*DZ1R_mhCcjWitUuchc1x2g.png)

**L'expérience du passager reste principalement la même.** Seule rarement (5 % du temps), des augmentations de prix élevées se déclenchent. **Cependant, pour les conducteurs, lorsque cette augmentation se déclenche, elle agit comme une couverture.** L'augmentation réduit efficacement l'impact que les embouteillages et/ou les arrêts des passagers auraient autrement sur le revenu quotidien des conducteurs.

**Essentiellement, lorsqu'une entreprise de covoiturage ajoute des frais de temps à son modèle de tarification, elle embrasse les événements de queue longue. Cela inclut les trajets longs dans un trafic dense, ce qui favorise principalement les conducteurs** (qui prennent un pourcentage plus élevé des tarifs)**.** Les entreprises qui ne facturent que par distance restent fragiles face à ces événements. Les risques d'événements de queue longue sont entièrement transférés aux conducteurs, qui doivent assumer des coûts supplémentaires — tels que l'essence, le coût d'opportunité de leur temps et l'usure de leurs voitures — sans réaliser de revenus supplémentaires.

Bien sûr, la deuxième entreprise pourrait soutenir qu'elle favorise délibérément le passager en faisant assumer le risque de queue par le conducteur. Mais on doit se demander si cela est réellement durable. Après tout, **les passagers et les conducteurs ont des impacts asymétriques sur les opérations de leur entreprise**.

Une bonne façon de quantifier cette asymétrie est d'observer la différence marquée que les entreprises de covoiturage paieront pour de nouveaux passagers et conducteurs. Par exemple, certaines entreprises _dépenseront_ de l'argent pour attirer les conducteurs de leurs concurrents à essayer leur application — j'ai vu des offres aller jusqu'à 500 $/conducteur — mais, **a-t-on déjà offert autant à un passager ?**

Je n'ai jamais vu un nouveau passager se voir offrir plus de 25 $. Mais disons que 50 $ étaient offerts. Ce nombre _valorise_ toujours un conducteur 10 fois plus qu'un passager. Avec cela à l'esprit, **il est logique pour les entreprises de covoiturage de protéger leurs utilisateurs à plus haute valeur — les conducteurs — en transférant le risque de queue aux passagers.**

Merci d'avoir lu ! Si vous avez apprécié l'article, maintenez le bouton ? ci-dessous enfoncé pour aider à diffuser le message.

Vous pouvez trouver le dépôt de code sur mon [Github](https://github.com/ignaciochr/rideshare-pricing/blob/master/trip-simulations.ipynb). Utilisez-le pour exécuter vos propres simulations de tarification !

Si vous avez des questions sur la mise en œuvre pour votre propre analyse, ou si vous souhaitez collaborer à un futur article, ou simplement dire « Salut », contactez-moi sur [Twitter](https://twitter.com/ignacio_chr) et/ou [LinkedIn](https://www.linkedin.com/in/ignacio-chavarria-19a3a420/).