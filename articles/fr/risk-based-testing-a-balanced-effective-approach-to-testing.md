---
title: 'Test Basé sur les Risques : Une Approche Équilibrée et Efficace pour les Tests'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-25T15:58:46.000Z'
originalURL: https://freecodecamp.org/news/risk-based-testing-a-balanced-effective-approach-to-testing
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/photo-1574790398664-0cb03682ed1c--1-.jpg
tags:
- name: Quality Assurance
  slug: quality-assurance
- name: Software Testing
  slug: software-testing
- name: Testing
  slug: testing
seo_title: 'Test Basé sur les Risques : Une Approche Équilibrée et Efficace pour les
  Tests'
seo_desc: 'By Rashmi Sharma

  Stakeholders are always pushing searching for faster solutions. Project managers
  are rushing products to the delivery table. And there is isn''t necessarily anything
  wrong with doing it this way.

  But it can be challenging for QA testi...'
---

Par Rashmi Sharma

Les parties prenantes recherchent toujours des solutions plus rapides. Les chefs de projet précipitent les produits vers la livraison. Et il n'y a pas nécessairement de problème à procéder ainsi.

Mais cela peut être un défi pour les équipes de test QA qui doivent adopter ce calendrier ultra-rapide, puis convaincre l'équipe de développement de les suivre.

Les équipes logicielles savent à quel point les équipes de gestion des tests veulent respecter les délais lorsqu'elles font face à des changements et des ajustements constants.

Dans ce scénario, toute la responsabilité incombe à l'équipe de test, qui peut rapidement devenir une cible facile lorsque des bugs de production sont livrés. Et tout retard concernant les spécifications et la mise en œuvre dans la phase amont du cycle de développement logiciel (SDLC) aggravera les choses.

En outre, les exigences des parties prenantes qui veulent le produit disponible dès que possible ajoutent de l'huile sur le feu. Tout cela met l'équipe de test sous une pression immense.

Une équipe QA doit avoir une réponse rationnelle et empirique à ce défi. La solution à ce problème réside dans le [test basé sur les risques (RBT)](https://www.kualitee.com/test-management/best-test-management-tools-must-used-2019/), qui peut aider l'équipe de test à respecter ses délais.

Votre équipe de test peut économiser beaucoup d'efforts avec la stratégie RBT, et cela permet de réaliser des économies importantes tout en livrant le projet à temps.

## Qu'est-ce que le Test Basé sur les Risques ? Les Bases du RBT

![Image](https://www.freecodecamp.org/news/content/images/2021/02/dm.png)

Dans la gestion des tests basée sur les risques, vous identifiez les plus grandes menaces du marché (qui auraient un effet néfaste sur l'entreprise tel que défini par le consommateur) tôt dans le cycle de développement, puis vous pouvez les contrer en prenant des mesures préventives.

Ces menaces du marché peuvent inclure une augmentation des coûts, une déception des consommateurs, une mauvaise interface utilisateur et une perte de clients. Et le RBT peut vous aider à les atténuer en effectuant des tests de telle manière que, même si un client rencontre une erreur, il peut continuer à utiliser l'application (et l'organisation n'est pas grandement affectée).

Le RBT implique des tests effectués en fonction des risques du produit. Il est utile pour découvrir la probabilité qu'une fonctionnalité ou une capacité spécifique échoue dans le produit final. Il vous aidera également à déterminer l'effet de cet échec sur l'entreprise en termes de coûts et d'autres dommages, bien à l'avance. Et il le fait en utilisant une stratégie de priorisation pour les cas de test.

Ainsi, l'évaluation basée sur les risques fonctionne en priorisant les tests de la fonctionnalité, des composants et des caractéristiques d'un produit ou d'un logiciel. Cette priorisation est basée sur le risque de possibilité d'échec dans le développement de la fonctionnalité ou de la fonctionnalité et son effet sur les clients.

## Comment Évaluer les Risques avec le RBT

Le RBT inclut la gestion des risques et la priorisation des tests en fonction du facteur de risque de chaque test. Le facteur de risque est le résultat de la probabilité et de l'effet possible du risque futur.

Mais comment pouvons-nous obtenir ces valeurs ? Pour attribuer un facteur de risque à un risque spécifique, voici trois exigences à considérer.

### Complexité du Code

![Image](https://www.freecodecamp.org/news/content/images/2021/02/complexity.jpg)
_Complexité Cyclomatique_

Plus le code est ambigu, plus il est probable que des défauts soient découverts. En termes simples, il est plus probable qu'un code plus compliqué contienne des bugs. L'inverse est également vrai : plus le code est propre et simple, moins il est susceptible de contenir des erreurs.

Le problème est alors de savoir comment calculer la complexité du code. Une mesure est la [complexité cyclomatique](https://www.tutorialspoint.com/software_testing_dictionary/cyclomatic_complexity.htm), qui fait référence au nombre de chemins potentiels. Le nombre minimal de cas de test dont vous avez besoin pour tester complètement une fonctionnalité est déterminé par ce nombre. En fait, un code avec une complexité cyclomatique élevée, qui peut augmenter le nombre d'erreurs, peut être plus difficile à lire.

### Churn ou nombre de modifications du code

Le churn implique ici le nombre de modifications qu'un fichier ou un module spécifié subit. Une zone d'application que les développeurs modifient plus fréquemment est plus susceptible de contenir des bugs qu'une zone qu'ils touchent rarement.

Un excellent exemple de cela est une application de commerce électronique qui est en développement depuis de nombreuses années. L'équipe logicielle est susceptible de faire des ajustements fréquents aux offres, d'introduire de nouvelles fonctionnalités et d'essayer des expériences pour stimuler les achats. Les sections affectées du code changent régulièrement et sont donc plus susceptibles de produire des erreurs.

Lorsque le [churn](https://dzone.com/articles/code-churn-a-magical-metric-for-software-quality) est significatif, des tests approfondis doivent être proposés pour la planification basée sur les risques : plus de tests UI, plus de tests unitaires, plus de tests d'intégration, etc.

### Criticité

La criticité implique le calcul de l'influence d'un [défaut logiciel](https://techbeacon.com/app-dev-testing/how-slash-high-cost-defects) sur votre application. La criticité n'est pas répartie uniformément dans une base de code. De nombreux systèmes sont censés avoir un noyau de code à haute criticité sur lequel le reste de l'application repose.

Si le code ne fonctionne pas correctement, plusieurs parties du logiciel pourraient être compromises et cela créerait probablement des défauts. Si cela s'applique à un logiciel lié à la sécurité, un défaut critique peut entraîner une perte de données, une divulgation de données sensibles et peut-être même mettre des vies en danger.

Lors de la mesure de la partie effet du facteur de risque, la criticité peut être utile.

Si un bug apparaît dans l'environnement le plus important de l'application, les effets pourraient être beaucoup plus extrêmes que s'il existait dans une zone qui ne contenait que du code utilitaire.

Nous nous appuyons sur nos algorithmes dans nos frameworks de gestion des tests pour classer les composants du site. Si les composants web ne peuvent pas être détectés par l'algorithme et le code principal associé, l'UI vérifie si nos clients feront des erreurs ou échoueront, créant de la frustration, des retravaux, des appels de service et un manque de confiance dans notre solution.

Pire encore, si des faux positifs sont générés par notre application, cela interrompra le processus CI/CD et entravera la mise en œuvre d'une application légitime.

## Le Test Intelligent est la Solution

Les entreprises de développement logiciel ont besoin d'une meilleure stratégie en matière de tests logiciels que "tester simplement tout". Tout le code n'est pas égal, toutes les menaces ne sont pas crédibles et tous les bugs ne déclenchent pas des dommages égaux.

Pour prendre des décisions éclairées sur la manière de répartir les ressources et de les tester plus efficacement, les entreprises technologiques doivent prendre en compte ces considérations RBT.

Si vous souhaitez rester au fait de vos Tests Logiciels Basés sur les Risques, vous pouvez consulter [Kualitee](https://www.kualitee.com/) – nous sommes une entreprise de tests logiciels et de sécurité de l'information.