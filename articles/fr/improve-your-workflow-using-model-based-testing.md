---
title: Comment améliorer votre flux de travail en utilisant les tests basés sur les
  modèles
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-18T12:43:13.000Z'
originalURL: https://freecodecamp.org/news/improve-your-workflow-using-model-based-testing
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/kaitlyn-baker-vZJdYl5JVXY-unsplash.jpg
tags:
- name: Software Testing
  slug: software-testing
- name: Testing
  slug: testing
- name: Web Development
  slug: web-development
seo_title: Comment améliorer votre flux de travail en utilisant les tests basés sur
  les modèles
seo_desc: 'By Anton Lawrence

  Unit testing is not enough – so let''s start using model-based testing to improve
  our workflows.

  Software testing is an important phase in building a scalable software system that
  usually has critical functions, business flows/logic,...'
---

Par Anton Lawrence

Les tests unitaires ne suffisent pas – alors commençons à utiliser les tests basés sur les modèles pour améliorer nos flux de travail.

Les tests logiciels sont une phase importante dans la construction d'un système logiciel évolutif qui a généralement des fonctions critiques, des flux/logiques métier et des entités externes connectées. Cette nature distribuée des systèmes logiciels induit un certain niveau de complexité lors de l'écriture de tests pour chaque unité, fonction ou flux.

Il existe divers types d'approches de test que vous pouvez utiliser. La meilleure approche que vous pouvez employer de manière transparente est le test basé sur les modèles. En termes simples, cela signifie créer un modèle de votre système (un peu comme un jumeau numérique qui décrit chaque aspect du système) et générer un test contre le modèle.

## Qu'est-ce que le test basé sur les modèles ?

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Mt98drDw.png)

Tout d'abord, nous devons savoir qu'un modèle est essentiellement la description et la représentation de la manière dont nous attendons que le système fonctionne. Les processus du système peuvent être définis en fonction de la série de séquences d'entrée, d'actions, de fonctions, de sortie et de flux de données commençant par l'entrée jusqu'à la sortie reçue.

Nous devons être capables de déterminer tous ces comportements lors des tests, et un modèle nous aide à le faire de manière transparente. Avec cela, nous pouvons ensuite générer des tests automatiquement basés sur les modèles du système.

En gros, le test basé sur les modèles est une technique de test logiciel dans laquelle les cas de test sont générés à partir d'un modèle qui décrit les aspects fonctionnels du système sous test. Il s'agit d'une nouvelle méthode de test logiciel qui emploie une implémentation secondaire, légère et efficace en temps d'une construction logicielle qui est appelée un modèle.

Nous prenons ce modèle couplé avec les exigences du système et générons des cas de test efficaces. Cette méthode de test logiciel est applicable à la fois aux tests matériels et logiciels.

## Pourquoi et comment cela améliore le flux de travail

L'automatisation des tests est inévitable car elle permet des tests logiciels plus rapides et plus efficaces. Vous pouvez rationaliser votre flux de travail et utiliser les dernières méthodologies de développement pour l'améliorer.

La plupart des développeurs et équipes logiciels trouvent difficile de créer et de mettre à jour des cas de test dans un environnement de dépendances et d'exigences en constante évolution.

De l'emploi des tests fonctionnels les plus simples aux méthodes lourds comme E2E, il y a eu de nombreuses méthodes de test conçues pour améliorer la fiabilité et l'efficacité des tests.

Il n'y a absolument rien de mal avec ces méthodes. Cependant, ces cas de test doivent être écrits manuellement pour chaque scénario. Chaque fois qu'il y a un changement dans les exigences du système, vous devez mettre à jour chaque cas de test affecté par le changement.

Ci-dessous, vous trouverez une exemplification graphique du processus de test basé sur les modèles :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/9YffXw8P.png)

Ces modèles sont utilisés pour générer des cas de test automatisés à l'aide d'outils MBT car ils décrivent le comportement attendu du système testé.

Nous avons essentiellement deux étapes ici :

1. Créer des modèles pour décrire le comportement et les processus du système.
2. Utiliser des outils MBT comme Spec Explorer, Graphwalker, fMBT ou Modbat, pour interpréter les modèles et générer des scripts de test pour les tests automatisés.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/hr1dyuLl.png)

Lors de l'utilisation des tests basés sur les modèles, la phase de création de modèles doit faire partie du cycle de vie du développement logiciel et être intégrée comme partie de la conception du produit dès la phase de spécification des exigences.

Cela permet à l'équipe de développement logiciel de concentrer son attention sur la construction d'un produit testable et de modèles qui améliorent l'expérience utilisateur.

Les tests basés sur les modèles peuvent améliorer notre flux de travail en :

1. Réduisant le temps passé à écrire des tests et permettant aux développeurs de se concentrer sur l'écriture de modèles pour couvrir uniquement les exigences du système et construire une application testable dès le départ.
2. Réduisant la maintenance de la suite de tests et générant plus de tests.
3. Aidant l'équipe à créer des scripts automatisés et augmentant la couverture des tests lorsqu'ils sont utilisés avec des outils de test et des frameworks d'automatisation.

## Comment implémenter les tests basés sur les modèles

L'implémentation des tests basés sur les modèles ne peut pas être introduite soudainement dans un système, car elle doit être faite progressivement. Il serait trop de l'introduire dans l'ensemble des processus et opérations du système.

Elle est mieux adaptée à la phase initiale du produit, car les choses sont encore très minimes. Il est facile de l'intégrer avec les exigences du système alors, car lorsque les choses deviennent plus grandes, vous n'avez qu'à mettre à jour le modèle.

Pour implémenter les tests basés sur les modèles, vous devez commencer par créer les modèles. Les modèles peuvent couvrir n'importe quel niveau d'exigences, de la logique métier à l'histoire utilisateur, et peuvent être connectés les uns aux autres.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/ZJrmhPS3.png)

Ensuite, vous pouvez générer automatiquement des cas de test basés sur les modèles une fois qu'ils sont créés. Et bien sûr, si vous apportez des modifications aux modèles, les tests seront mis à jour automatiquement.

Vous pouvez facilement intégrer ces tests dans vos processus et outils CI une fois que vous êtes en mesure de générer des tests automatisés à partir de modèles.

## Avantages des tests basés sur les modèles

1. Optimise le temps et le coût des tests logiciels
2. Vous pouvez générer des scripts de test pour chaque scénario avec simplement un clic.
3. Cela garantit que l'équipe de test logiciel peut communiquer le comportement attendu du système.
4. Permet une détection précoce des irrégularités des exigences.
5. La génération et l'exécution automatisées des cas de test rendent la solution de test globale plus efficace et moins sujette aux erreurs.
6. Il aide à générer un nombre minimal de cas de test pour valider un flux fonctionnel ou de données donné afin de s'assurer que le système sous test fonctionne sans faille et ne fait jamais rien d'indésirable.
7. La maintenance du projet est minime.

## Inconvénients des tests basés sur les modèles

1. Demande un investissement élevé ainsi que des efforts.
2. Nécessite un testeur logiciel qualifié et discipliné.
3. Le premier cas de test prend plus de temps à générer car il nécessite plus de travail en amont que les tests manuels traditionnels.
4. La courbe d'apprentissage des tests basés sur les modèles est assez raide et sa complexité le rend plus difficile à comprendre pour les débutants.

## Comment cela diffère des tests d'interface utilisateur

Maintenant, nous savons ce qu'est le test basé sur les modèles, et nous avons déjà compris les avantages de son utilisation par rapport à l'utilisation de la méthode de test traditionnelle.

Les tests d'interface utilisateur (UI/Frontend Testing) sont un type de [test logiciel](https://en.wikipedia.org/wiki/Software_testing) qui implique simplement le processus de test de la fonction de l'interface utilisateur, en s'assurant que l'interface du système réagit comme elle est censée le faire.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/FBdLkRsl.jpeg)

Ce processus implique des tests manuels, et chaque scénario de test doit être écrit à la main. Toute modification apportée à l'interface utilisateur brisera l'ensemble du cas de test à moins qu'il ne soit mis à jour avec les modifications. Il utilise des WebDrivers et la plupart du temps Selenium afin de simuler complètement la manière dont les utilisateurs interagissent avec l'interface et valider la sortie attendue.

Les tests d'interface utilisateur peuvent être employés à n'importe quelle étape du produit car ils n'ont clairement pas beaucoup d'exigences et la courbe d'apprentissage est très facile par rapport à MBT.

Le coût des tests est assez faible et pourrait être réduit à zéro. Le temps passé peut également être peu. La maintenance peut être très élevée en fonction de la complexité de l'interface du produit.

Cela ne nécessite pas un développeur ou un logiciel très compétent. Tout développeur ayant des connaissances de base en test peut s'en emparer. Il y a tant de différences lorsque vous approfondissez cela, cependant, les deux sont bons pour différents cas d'utilisation.

## Conclusion

Le test basé sur les modèles est une technique puissante, rentable et profitable pour les grandes entreprises à long terme.

Cependant, l'introduction de cette approche dans les processus d'une grande entreprise peut être un grand défi, surtout lorsqu'il s'agit de réviser entièrement leur approche du développement et des tests logiciels.

Le test basé sur les modèles doit devenir une partie du [flux de travail de développement](https://hackernoon.com/how-do-we-setup-a-proper-development-workflow-f708031370d9), mais cela s'accompagne de ses propres défis, y compris des changements dans l'ensemble de l'infrastructure. Cela rend également une courbe d'apprentissage déjà raide encore plus difficile.

Heureusement, il y a certaines choses qui peuvent aider à identifier quand le test basé sur les modèles peut vraiment être utile. Par exemple, si vous avez un ensemble infini de systèmes avec des exigences que vous pouvez couvrir de différentes manières. Ou si vous avez un système distribué ou réactif, cela peut également être une raison d'envisager cette approche.

Le test basé sur les modèles peut aller très loin dans les tests et économiser un temps et des efforts significatifs lorsqu'il est implémenté correctement.