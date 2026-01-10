---
title: Automatisation des tests d'interface utilisateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-22T22:28:56.000Z'
originalURL: https://freecodecamp.org/news/user-interface-test-automation-3da36b132077
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MAoFtzMOZQV7fGIcvizZDg.jpeg
tags:
- name: automation
  slug: automation
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
- name: UI
  slug: ui
seo_title: Automatisation des tests d'interface utilisateur
seo_desc: 'By Aditya Parab

  Test Automation has become one of the important aspects in the Software development
  world. Everyone in this community must be aware of the below Agile Test Automation
  Pyramid. It is concept developed my Mike Cohn.

  Unit tests should fo...'
---

Par Aditya Parab

L'automatisation des tests est devenue l'un des aspects les plus importants dans le monde du développement logiciel. Tout le monde dans cette communauté doit connaître la pyramide de l'automatisation des tests agiles ci-dessous. C'est un concept développé par Mike Cohn.

Les tests unitaires doivent constituer la base de cette pyramide. Les tests de niveau service forment la couche suivante et enfin les tests d'interface utilisateur (UI) forment le sommet.

![Image](https://cdn-media-1.freecodecamp.org/images/91E5LbriJvgfm9TWbyaMUnpYN0hXgKrU4CEp)
_Pyramide de l'automatisation des tests agiles_

Traditionnellement, les tests automatisés consistaient à tester le flux d'exécution de bout en bout au niveau de l'interface utilisateur. Mais avec le concept ci-dessus et la mise en œuvre de l'agile, cela a changé. Les tests unitaires et de niveau service constituent la majeure partie de la stratégie d'automatisation. Les tests UI n'en sont qu'une petite partie.

Il existe des raisons valables pour avoir moins de tests d'automatisation UI dans votre stratégie d'automatisation. Ci-dessous, j'en ai listé quelques-unes :

* Ces tests sont **lents**.
* Ces tests sont **fragiles** et peuvent donner de faux positifs ou de faux négatifs.
* Basés sur l'interface utilisateur, ils nécessitent donc beaucoup de **changements** et de **maintenance**.

Cela dit, l'automatisation des tests UI reste importante car elle teste la partie par laquelle votre utilisateur naviguera. Les retours à ce sujet aident certainement à améliorer l'expérience utilisateur lors de l'utilisation de l'application.

Voici quelques cas dans lesquels l'automatisation des tests UI est précieuse :

* Tests de régression. L'automatisation peut libérer les testeurs humains du processus ennuyeux et répétitif des tests de régression.
* Tester des applications qui n'ont pas de tests unitaires développés. Cela aide à introduire les tests automatisés dans les applications héritées (legacy).
* Tests multi-navigateurs et multi-plateformes. Il s'agit principalement d'exécuter les mêmes tests sur différentes versions. C'est également le cas pour les applications mobiles pour tester différentes versions d'OS et modèles d'appareils.
* Tests de performance car ils nécessitent une charge plus élevée que ce que les tests manuels ne peuvent générer.

Avec une stratégie appropriée, l'automatisation des tests UI peut constituer une partie très utile de votre suite d'automatisation des tests. Quelques pistes pour développer une stratégie de test efficace :

### Identifier les bons cas à automatiser

L'aspect le plus important de tout test est l'identification des bons cas de test. Il en va de même pour les tests automatisés.

Voici quelques critères pour sélectionner les cas de test à automatiser :

1. Cas de test fréquemment exécutés dans le cadre des tests de fumée (smoke tests) et de régression
2. Cas de test qui implémentent une logique et des calculs complexes
3. Cas de test qui doivent être exécutés sur plusieurs plateformes
4. Cas de test où l'exécution manuelle peut être difficile, par exemple la performance

### Se préparer dès le début

La préparation de l'automatisation de toute fonctionnalité commence dès la phase de conception. Impliquez les ingénieurs de test dans cette phase aux côtés des développeurs. Créez une stratégie pour les tests d'automatisation. Décidez quels tests sont couverts au niveau unitaire et service afin qu'il n'y ait pas de doublons dans les tests UI.

Dans le cas d'une application construite à partir de zéro, concevez le code pour faciliter l'automatisation une fois que l'application est stable. Il peut s'agir de petites choses. Par exemple, suivre des conventions de nommage spécifiques pour les éléments de l'interface utilisateur. Ainsi que de nommer de manière similaire des éléments similaires sur différentes pages. Cela aide également à maintenir la cohérence des scripts d'automatisation.

En cas de modifications dans une application existante, commencez l'automatisation en même temps que le développement. Comme les changements effectués sont incrémentiels, exécutez les tests dès qu'ils sont disponibles. C'est bénéfique pour l'agile et la livraison continue (continuous delivery). De petits incréments doivent y être prêts pour une mise en œuvre continue.

### Exécution continue et parallèle

Planifiez fréquemment l'exécution des tests automatisés. Au moins une fois par jour. Cela fournit un retour continu sur les changements effectués. Cela donne également une bonne idée de la stabilité de l'environnement de test.

L'exécution est plus lente car ces tests sont exécutés sur l'interface utilisateur. Mais avec les tests continus, nous voulons un retour plus rapide. L'exécution parallèle est l'un des moyens de résoudre ce problème. De plus, avec les exécutions parallèles, les tests sur plusieurs plateformes peuvent être réalisés.

### Refactorisation et maintenance

Les scripts de tests automatisés UI doivent être considérés au même titre que le code de l'application. Cela permet d'apporter l'attention et la concentration nécessaires. Tout comme le code de l'application, ces scripts nécessitent également une refactorisation et une maintenance continues.

Avec une maintenance appropriée, l'exécution des tests devient cohérente. De plus, cela aidera à améliorer les performances de l'exécution des tests et facilitera les changements futurs.

Avec une conception et une stratégie d'exécution appropriées, l'automatisation des tests UI peut s'avérer être une étape utile pour améliorer la qualité et accélérer la livraison continue.