---
title: Guide d'assurance qualité logicielle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-01T19:48:00.000Z'
originalURL: https://freecodecamp.org/news/software-quality-assurance-guide
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c58740569d1a4ca3194.jpg
tags:
- name: QA
  slug: qa
- name: Quality Assurance
  slug: quality-assurance
- name: Software Engineering
  slug: software-engineering
- name: toothbrush
  slug: toothbrush
seo_title: Guide d'assurance qualité logicielle
seo_desc: 'Quality Assurance

  Quality Assurance (commonly known as QA) is the means by which a product in development
  is checked to make sure it works as it’s supposed to. The actual methods used in
  QA processes vary hugely depending on the size and nature of th...'
---

## **Assurance Qualité**

L'assurance qualité (communément appelée QA) est le moyen par lequel un produit en développement est vérifié pour s'assurer qu'il fonctionne comme prévu. Les méthodes réelles utilisées dans les processus QA varient énormément en fonction de la taille et de la nature du produit.

Pour un projet personnel, vous testerez probablement au fur et à mesure, en demandant à d'autres de fournir des commentaires à des étapes appropriées. En revanche, une application bancaire doit avoir chaque aspect de chaque fonctionnalité vérifié et documenté de manière exhaustive pour s'assurer qu'elle est à la fois fonctionnelle et sécurisée.

Quelle que soit la formalité ou le détail d'un processus QA, son objectif est d'identifier les bugs afin qu'ils puissent être résolus avant la sortie du produit.

## Méthodologies

### Agile

Dans une approche Agile du développement, l'objectif est que chaque cycle de travail (« sprint ») produise un logiciel fonctionnel qui peut être ajouté et amélioré de manière itérative. Cela fait des processus QA une partie intrinsèque du cycle de développement.

En testant les composants logiciels à chaque étape de leur production, vous réduisez le risque de bugs présents lors de la sortie.

## Terminologie

### Tests Automatisés

Tests effectués avec des scripts pré-écrits conçus pour contrôler l'exécution des tests.

### Boîte Noire

Ces tests ne regardent pas à l'intérieur du système sous test, mais le traitent comme « fermé » de la même manière que l'utilisateur final l'expérimentera.

### Défaut

Tout écart par rapport aux spécifications d'une application ; souvent appelé « bug ».

### Tests Exploratoires

Une approche non scriptée des tests, qui repose sur la créativité unique du testeur dans un effort pour trouver des bugs inconnus et identifier des régressions.

### Tests d'Intégration

Tests de composants/modules individuels ensemble pour s'assurer qu'ils se connectent et interagissent bien les uns avec les autres.

### Tests de Chemin Négatif

Un scénario de test conçu pour produire un état d'erreur dans une fonctionnalité/application et vérifier que l'erreur est gérée avec élégance. Un exemple de cela est de saisir une série de nombres dans le champ email d'un formulaire d'inscription utilisateur et de vérifier que l'inscription n'est pas acceptée jusqu'à ce qu'une adresse email réelle soit fournie.

### Tests de Régression

Tests effectués sur une nouvelle version pour s'assurer que la nouvelle fonctionnalité n'a pas involontairement cassé la fonctionnalité précédemment testée.

### Tests de Fumée

Une approche minimaliste des tests destinée à s'assurer que la fonctionnalité de base fonctionne avant que des tests plus approfondis ne prennent place. Se produit généralement au début du processus de test.

### Cas de Test

Préconditions, étapes et résultats attendus spécifiés auxquels un testeur/ingénieur QA se réfère pour déterminer si une fonctionnalité effectue sa tâche comme prévu.

### Boîte Blanche

Fait référence aux tests effectués à un niveau structurel, au sein de la base de code. Les programmeurs vérifiant que les entrées et les sorties de fonctions ou de composants spécifiques seraient des tests de boîte blanche.

Aussi connu sous le nom de « Glass Box », « Clear Box », « Transparent Box » car le testeur peut « voir à l'intérieur » du système sous test.

Les principales catégories sont

* **Tests unitaires** (les unités individuelles de code font ce qu'elles devraient faire)
* **Tests d'intégration** (les unités/composants interagissent correctement les uns avec les autres)
* **Tests de régression** (réapplication des tests à des étapes ultérieures du développement pour s'assurer qu'ils fonctionnent toujours)

Il existe trois techniques principales :

* **Partitionnement d'équivalence** (les valeurs d'entrée testées sont représentatives de grands ensembles de données d'entrée)
* **Analyse des Valeurs Limites** (le système est testé avec des entrées choisies où le comportement et donc la sortie devraient changer)
* **Graphique Cause-Effet** (les tests sont conçus à partir d'une visualisation des relations entrée-sortie)

### **Autres Ressources**

* [Comment rédiger une documentation QA qui fonctionne réellement](https://www.freecodecamp.org/news/how-to-write-qa-documentation-that-will-work/)
* [Développement Piloté par les Tests](https://guide.freecodecamp.org/agile/test-driven-development)
* [Tests unitaires](https://guide.freecodecamp.org/software-engineering/unit-tests/)