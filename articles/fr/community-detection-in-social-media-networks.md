---
title: Comment l'algorithme Fast Unfolding détecte les communautés dans les grands
  réseaux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-14T18:22:56.000Z'
originalURL: https://freecodecamp.org/news/community-detection-in-social-media-networks
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/fig1.png
tags:
- name: algorithms
  slug: algorithms
- name: data analysis
  slug: data-analysis
- name: Data Science
  slug: data-science
seo_title: Comment l'algorithme Fast Unfolding détecte les communautés dans les grands
  réseaux
seo_desc: 'By Aakash Jhawar

  Social network analysis involves studying patterns in large real life networks that
  are comprised of millions of nodes. If you have a basic knowledge of graph theory.),
  you can perform these analyses.

  The digital world has opened up ...'
---

Par Aakash Jhawar

L'analyse des réseaux sociaux implique l'étude des motifs dans de grands réseaux réels composés de millions de nœuds. Si vous avez une connaissance de base de la [théorie des graphes](https://en.wikipedia.org/wiki/Graph_theory#:~:text=In%20mathematics%2C%20graph%20theory%20is,also%20called%20links%20or%20lines).), vous pouvez effectuer ces analyses.

Le monde numérique a ouvert une manière totalement différente de créer des relations. Il a également libéré un océan de données que nous pouvons analyser pour mieux comprendre le comportement humain. 

Les données des réseaux sociaux désignent toutes les informations brutes et les insights collectés à partir de l'activité d'un individu sur les réseaux sociaux. Nous pouvons créer des réseaux à partir de ces activités sur les réseaux sociaux pour obtenir une meilleure perception de cet individu.

Ces réseaux peuvent varier largement et peuvent inclure vos amis Facebook, les produits que vous avez récemment achetés sur Amazon, les tweets que vous avez aimés ou retweetés, votre nourriture préférée que vous avez commandée sur Zomato, la recherche que vous avez faite sur Google, ou l'image que vous avez récemment aimée sur Instagram.

Les entreprises utilisent ces réseaux pour classer leurs utilisateurs en différents groupes. Cela les aide à 

* faire des recherches de marché
* générer des leads
* mieux servir leurs clients
* trouver et partager des photos et des vidéos
* découvrir et discuter du contenu tendance
* partager des informations sur les services et les restaurants
* se connecter avec d'autres autour d'un intérêt ou d'un hobby partagé 
* et plus encore. 

La liste est pratiquement sans fin.

Avant de trop nous perdre dans les détails, décomposons rapidement la distinction entre les différents composants d'un réseau.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/fig3.png)
_[Communautés dans un réseau social ](https://ieeexplore.ieee.org/document/9198574)_

### Qu'est-ce qu'un réseau ?

Un réseau est un ensemble de relations personnelles interconnectées. Par exemple, différents individus peuvent communiquer les uns avec les autres dans un groupe de réseaux sociaux à travers un ensemble dynamique de relations. 

Un réseau est composé de _nœuds_ (acteurs individuels, personnes ou choses au sein du réseau) et des _liens_, _arêtes_ ou _connexions_ (relations ou interactions) qui les relient.

### Qu'est-ce qu'un groupe ?

Reicher S. D. dans [_The determination of collective behavior_](https://ethos.bl.uk/OrderDetails.do?uin=uk.bl.ethos.593332) décrit un groupe comme une collection d'individus qui se considèrent comme un groupe. Les membres du même groupe ont un ensemble de croyances et de comportements partagés.

### Qu'est-ce qu'une communauté ?

Selon David W. McMillan ([_Sense of Community: A Definition and Theory_](https://www.researchgate.net/publication/235356904_Sense_of_Community_A_Definition_and_Theory)_), la communauté peut être définie comme suit :

> _"Le sentiment de communauté est un sentiment d'appartenance, un sentiment que les membres comptent les uns pour les autres et pour le groupe, et une foi partagée que les besoins des membres seront satisfaits grâce à leur engagement à être ensemble."_

Les communautés ou sous-unités sont les sous-réseaux dans un réseau qui sont des nœuds hautement interconnectés. 

La communauté indique l'existence de structures internes qui ont des caractéristiques spéciales ou jouent le même rôle dans un réseau. 

Les groupes hautement connectés d'individus ou d'objets à l'intérieur de ces réseaux sont des communautés. Cela se situe généralement au point d'intersection du réseau et du groupe.

Maintenant que nous avons une idée claire de ce qu'est un réseau, un groupe et une communauté, plongeons plus profondément dans la manière dont ces réseaux sont divisés en petites communautés.

Nous allons examiner le populaire _[Fast Unfolding Algorithm](https://arxiv.org/pdf/0803.0476.pdf)_. Vincent C. Blondel et les co-auteurs de l'article ont comparé cet algorithme avec d'autres algorithmes de détection de communautés. Ils ont découvert que cet algorithme surpasse tous les autres algorithmes dans les grands réseaux.

## Qu'est-ce que l'algorithme Fast Unfolding ?

L'algorithme Fast Unfolding a été utilisé pour identifier les communautés linguistiques dans un réseau de téléphonie mobile belge de 2,6 millions de clients. 

Il a également été utilisé pour analyser un graphe web de 118 millions de nœuds et plus d'un milliard de liens. 

L'identification des communautés dans un réseau aussi vaste a pris seulement 152 minutes. Cet algorithme est donc à la fois rapide et efficace.

### Comment fonctionne l'algorithme

L'algorithme fonctionne en deux phases :

**Phase 1**

1. Attribuer une communauté différente à chaque nœud dans un réseau.
2. Ensuite, pour chaque nœud, _i_ considère le nœud _j_ et évalue le gain en modularité en retirant le nœud _i_ de sa communauté et en le plaçant dans la communauté de _j_.
3. Le nœud _i_ est placé dans la communauté pour laquelle il obtient un gain maximal de modularité, mais le gain doit être positif. Si le gain est négatif, alors le nœud _i_ reste dans la même communauté.

**Phase 2**

1. La deuxième phase de l'algorithme consiste à construire un nouveau réseau dont les nœuds sont maintenant les communautés trouvées lors de la première phase. Nous construisons donc des nœuds en fusionnant tous les nœuds de la communauté en un seul nœud.
2. Les poids des liens entre les nœuds sont donnés par la somme des poids des liens entre les nœuds dans les deux communautés correspondantes.
3. Les liens entre les nœuds de la même communauté conduisent à des boucles auto-référentielles pour la communauté dans le nouveau réseau.
4. Répéter la **Phase 1** jusqu'à ce qu'aucune amélioration supplémentaire ne puisse être atteinte.

### Comment le gain en modularité est calculé

La Qualité de Partition (_Q_) est mesurée par la [**Modularité**](https://en.wikipedia.org/wiki/Modularity_%28networks%29) (aka modularité de partition). C'est une valeur scalaire entre -1 et 1, et mesure la densité des liens à l'intérieur des communautés par rapport aux liens entre les communautés.

Le **Gain en Modularité** (ΔQ) obtenu en déplaçant un nœud isolé _i_ dans une communauté C peut facilement être calculé par :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/gif--3-.gif)

_Σin_ est la somme des poids des liens à l'intérieur de C.

_Σtot_ est la somme des poids des liens incidents aux nœuds dans C.

_ki_ est la somme des poids des liens de _i_ vers le nœud dans C.

_m_ est la somme des poids de tous les liens dans le réseau.

Le Gain en Modularité est évalué en retirant _i_ de sa communauté et en le déplaçant ensuite dans une communauté voisine. Si le gain est positif, alors ce nœud est placé dans la communauté voisine.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2020-09-26-at-4.39.20-PM.png)
_Fonctionnement de l'algorithme Fast Unfolding_

### Exécution à sec de l'algorithme

Dans le réseau de gauche (15 nœuds), nous attribuons d'abord une communauté unique à chaque nœud. Ensuite, nous évaluons la Modularité de chaque nœud et réattribuons la communauté en fonction du gain. Cela s'appelle **l'optimisation de la modularité**.

Dans la phase suivante, nous construisons des nœuds en fusionnant tous les nœuds de cette communauté en un seul nœud. Dans la communauté verte, nous avons un total de 5 nœuds et il y a un total de 7 arêtes entre eux. 

Ainsi, après **l'agrégation de la communauté**, le poids de la boucle auto-référentielle du nœud vert sera de 14 (7 * 2 car il s'agit d'un lien bidirectionnel). De même, le poids de la boucle auto-référentielle du nœud rouge sera de 16, celui du nœud bleu sera de 4 et celui du nœud bleu clair sera de 2.

Le poids de l'arête entre le nœud vert et le nœud bleu sera de 4 car il y a un total de 4 arêtes entre la communauté verte et bleue après l'optimisation de la modularité.

À l'étape suivante, nous réévaluons la Modularité pour les nouveaux nœuds et répétons le même processus.

Enfin, nous obtenons deux communautés, _Verte_ et _Bleu Clair_. La communauté Verte a 26 boucles auto-référentielles car il y a un total de 13 arêtes entre les nœuds de la communauté verte. Et nous avons 12 arêtes dans la communauté bleu clair, soit un total de 24 boucles auto-référentielles.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/fast-unfolding--1-.gif)
_Détection de communautés dans un réseau_

### Avantages de l'algorithme

1. Ses étapes sont intuitives et faciles à mettre en œuvre, et le résultat est non supervisé.
2. L'algorithme est extrêmement rapide. Les simulations informatiques sur des réseaux modulaires très grands suggèrent que sa complexité est linéaire sur les données typiques et clairsemées. Cela pourrait être dû au fait que le Gain en Modularité est facile à calculer et que le nombre de communautés diminue drastiquement après seulement quelques passes.

### Limites de l'algorithme

1. L'optimisation de la modularité échoue à identifier les communautés plus petites qu'une certaine échelle. Elle provoque donc une limite de résolution sur la communauté calculée en utilisant une approche d'optimisation de la modularité pure.
2. Pour les petits réseaux, la probabilité que deux communautés séparées puissent être fusionnées en déplaçant chaque nœud est très faible.

## Conclusion

Si vous avez tenu jusqu'ici... merci ! J'espère qu'il y a eu des informations précieuses pour vous. 

Maintenant, vous savez comment fonctionne l'algorithme Fast Unfolding, et qu'il est extrêmement efficace pour détecter les communautés dans des réseaux très grands. 

La manière dont il calcule le Gain en Modularité rend l'algorithme plus performant que tous les autres algorithmes existants. Laissez-moi un mot si vous le trouvez utile ou si vous avez des questions de suivi.

_Merci d'avoir lu !_