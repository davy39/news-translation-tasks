---
title: Comment Mozilla prend soin de la santé de Firefox — et ce que vous pouvez en
  apprendre
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-24T21:55:03.000Z'
originalURL: https://freecodecamp.org/news/here-is-how-we-take-care-of-firefox-health-at-mozilla-8f7f9b085955
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3orZX4NPEQbwNxUgz7Wm4Q.jpeg
tags:
- name: Firefox
  slug: firefox
- name: internships
  slug: internships
- name: Mozilla
  slug: mozilla
- name: open source
  slug: open-source
- name: 'tech '
  slug: tech
seo_title: Comment Mozilla prend soin de la santé de Firefox — et ce que vous pouvez
  en apprendre
seo_desc: 'By Syeda Aimen Batool

  Currently, I’m working on a Firefox health dashboard as a part of my Outreachy internship
  with Mozilla. And here are the major goals we intend to achieve during the internship.


  Add new features to the graphical presentation of ...'
---

Par Syeda Aimen Batool

Actuellement, je travaille sur un [tableau de bord de santé de Firefox](https://github.com/mozilla-frontend-infra/firefox-health-dashboard) dans le cadre de mon [stage Outreachy avec Mozilla](https://medium.freecodecamp.org/how-i-got-a-remote-paid-internship-at-mozilla-through-outreachy-60958fe9264a). Et voici les [objectifs principaux](https://github.com/mozilla-frontend-infra/firefox-health-dashboard/projects/2) que nous entendons atteindre pendant le stage.

* Ajouter de nouvelles fonctionnalités à la présentation graphique des données de performance
* Transférer le tableau de bord existant de l'équipe JS (Performance Firefox) vers le tableau de bord de santé
* Améliorer les informations existantes sur les graphiques et corriger quelques bugs

Le but principal de cet article est d'expliquer le projet à quelqu'un qui n'est pas dans la communauté et qui n'est pas familier avec ce que nous faisons chez Mozilla. L'intention est d'aider les nouveaux et les autres contributeurs à comprendre le tableau de bord afin qu'ils puissent contribuer à ce projet open source avec une meilleure compréhension de ce qui se passe à l'intérieur.

![Image](https://cdn-media-1.freecodecamp.org/images/Amkrf0TIX5AYgBBaD9bSbFGQg0eL7mVGCdrr)
_Photo par [Unsplash](https://unsplash.com/photos/0-SGyQFiDRI?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">rawpixel</a> sur <a href="https://unsplash.com/search/photos/health?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Qu'est-ce que le tableau de bord de santé de Firefox ?

La santé de Firefox est un projet visant à créer des tableaux de bord pour les chefs de projet et les ingénieurs. Il affiche les métriques et les insights de Firefox pour aider à répondre aux critères de publication. Il permet d'inclure des données/métriques provenant du suivi des problèmes de Mozilla (Bugzilla), des données de performance (Perfherder), des métriques de produit (Télémétrie) et de quelques autres sources. Toutes les données sont affichées sous forme de graphiques en utilisant une bibliothèque de graphiques open source ChartJS pour afficher les insights contre différentes dates et plateformes.

Il était auparavant connu sous le nom de Platform Health. Il a été [refactorisé en janvier 2018](https://github.com/mozilla-frontend-infra/firefox-health-dashboard/issues/29) en tant que tableau de bord de santé de Firefox. L'un des principaux changements dans cette refactorisation a été de séparer le backend du front-end. Cela a amélioré la maintenabilité du code.

#### Technologies :

Le [backend](https://github.com/mozilla/firefox-health-backend) est écrit en utilisant NodeJS et Koa. Le [front-end](https://github.com/mozilla-frontend-infra/firefox-health-dashboard) est construit en utilisant ReactJS ainsi qu'une bibliothèque de graphiques open source ChartJS. Certaines des données proviennent de différents hôtes via différentes bibliothèques. Par exemple, perf-google interroge Perfherder de Mozilla pour les données de performance. Les informations sur les bugs signalés proviennent de Bugzilla. Donc, si vous prévoyez de contribuer à l'avenir, vous devez avoir une compréhension des technologies mentionnées ci-dessus.

Ce tableau de bord traite de la performance des différentes versions et appareils de Firefox. Mais aujourd'hui, nous allons parler de [Firefox Android](https://health.graphics/android) et de la manière dont les ingénieurs de Mozilla prennent soin de ses performances.

### Données/métriques pour Firefox Android

Actuellement, les données pour Firefox Android proviennent de différentes sources. Nous affichons les données sous forme de graphiques pour une meilleure compréhension et analyse. Vous pouvez voir tous les insights sur [Firefox Android sur le tableau de bord de santé](https://health.graphics/android). Voici quelques sources et informations sur Firefox Android pour aider les ingénieurs à améliorer les performances du navigateur.

#### Bugzilla :

Développé par Mozilla, Bugzilla est un outil gratuit et open-source pour suivre les bugs, les problèmes et les demandes de changement dans les applications complexes et volumineuses. Il est utilisé par des milliers d'organisations pour suivre les performances de leurs produits. Nous l'utilisons dans le tableau de bord de santé pour surveiller les bugs qui apparaissent dans Firefox Android.

![Image](https://cdn-media-1.freecodecamp.org/images/dKEOkAJGbvDDvS3M-pUPMS8GvHtasek7oJ1D)
_Un graphique affichant les bugs de Bugzilla_

Comme mentionné ci-dessus, nous utilisons ChartJS pour afficher les données. Ici, nous avons un graphique représentant le nombre de bugs signalés à différentes dates pour Firefox Android sur Bugzilla. Les bugs avec l'étiquette P1 ont la priorité la plus élevée. Ils doivent être corrigés dès que possible. Ensuite viennent les bugs P2 avec la deuxième priorité la plus élevée. Les bugs de niveau P3 ont la priorité la plus basse et les ingénieurs peuvent les corriger lorsqu'ils ont le temps. Cela aide les développeurs et les chefs de produit à examiner les bugs de différentes priorités plus efficacement et à les résoudre selon la priorité.

#### NimbleDroid :

Nous utilisons un service tiers appelé NimbleDroid pour obtenir des insights de données après avoir exécuté les tests contre Firefox Android. NimbleDroid est un service de test de performance fonctionnelle pour les appareils Android et iOS.

> Surveillez chaque flux utilisateur critique pour chaque build de votre application mobile. Identifiez les problèmes qui dégradent l'expérience utilisateur tôt dans le cycle de développement. Intégrez-vous de manière transparente à votre workflow CI. — Site officiel

![Image](https://cdn-media-1.freecodecamp.org/images/QtqHkLwQwTP0szF2tkiNZyvA-HWLQ1Sl7jkP)
_Affichage des insights de données fournis par NimbleDroid_

#### Télémétrie :

La télémétrie est un outil capable de fournir des informations sur les performances et l'utilisation à Mozilla pour aider les ingénieurs et les décideurs à mesurer les performances de Firefox dans le monde réel. Il a la capacité de collecter des informations sur les performances, le matériel, l'utilisation, la personnalisation et d'autres informations non personnelles de l'utilisateur de Firefox et de les envoyer à Mozilla quotidiennement pour aider les ingénieurs à améliorer la qualité et l'efficacité du navigateur.

![Image](https://cdn-media-1.freecodecamp.org/images/xshtOGlnr9LFHhteDt7yxJFkOif5bD80akVO)
_Vue graphique de la télémétrie_

Pour un appareil Android, le navigateur mesure le temps qu'il faut pour charger une page de contenu sur un appareil et le rapporte via la télémétrie. Nous l'affichons ensuite sous forme graphique. Par exemple, la capture d'écran indique que 75 % des utilisateurs ont signalé un temps total de chargement de la page de contenu de 4,9 secondes le 19 septembre 2018. Et ces données sont recueillies à partir de différents appareils de différents utilisateurs. Cela aide les ingénieurs à surveiller le temps de chargement du navigateur pour améliorer sa vitesse et le rendre plus efficace.

#### Perfherder :

Perfherder est un système pour aider les ingénieurs à visualiser et analyser les données de performance produites par les nombreux tests automatisés exécutés contre les produits Mozilla tels que Firefox ou Firefox Android. Perfherder fait partie du projet Treeherder. C'est un autre tableau de bord pour les check-ins des projets de Mozilla. Le but principal de cet outil est de s'assurer que les performances de Firefox s'améliorent avec le temps. Il aide les développeurs à comprendre leurs changements et les corrections potentielles en signalant les régressions.

Dans les prochains articles, nous parlerons de Firefox Quantum et du tableau de bord de l'équipe JS. Nous verrons comment ces outils fonctionnent pour améliorer les performances du navigateur Firefox.

#### Guide de contribution :

Si vous vous souciez de la santé de Firefox ou si vous êtes intéressé à contribuer au projet, voici comment faire.

* Clonez et configurez le [projet](https://github.com/mozilla-frontend-infra/firefox-health-dashboard) sur votre machine locale
* Suivez le [readme](https://github.com/mozilla-frontend-infra/firefox-health-dashboard#firefox-health-dashboard)
* Et commencez avec les [good-first-issues](https://github.com/mozilla-frontend-infra/firefox-health-dashboard/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) si vous trouvez cela écrasant pour commencer

Restez à l'écoute pour en savoir plus sur les choses géniales que nous faisons chez Mozilla.