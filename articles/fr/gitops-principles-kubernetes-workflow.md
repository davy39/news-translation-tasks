---
title: Qu'est-ce que GitOps ? Principes, meilleures pratiques et flux de travail Kubernetes
subtitle: ''
author: ania kubow
co_authors: []
series: null
date: '2021-11-23T22:50:29.000Z'
originalURL: https://freecodecamp.org/news/gitops-principles-kubernetes-workflow
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/gitops.jpeg
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Cloud Services
  slug: cloud-services
- name: Kubernetes
  slug: kubernetes
seo_title: Qu'est-ce que GitOps ? Principes, meilleures pratiques et flux de travail
  Kubernetes
seo_desc: "In this talk, CTO Cornelia Davis will teach you what GitOps is and what\
  \ its four main principles are. \nWhat is GitOps?\nThe first thing you need to know\
  \ is that GitOps is a set of modern best practises for deploying and managing cloud\
  \ native infrastru..."
---

Dans cette présentation, la CTO Cornelia Davis vous expliquera ce qu'est GitOps et quels sont ses quatre principes principaux. 

## Qu'est-ce que GitOps ?

La première chose à savoir est que GitOps est un ensemble de meilleures pratiques modernes pour déployer et gérer des infrastructures et applications cloud natives. 

Et cela peut être difficile à comprendre si vous n'avez jamais travaillé avec la gestion de clusters ou la livraison d'applications auparavant. Mais heureusement, Cornelia fait un excellent travail pour l'expliquer dans cette présentation de 30 minutes.

Regardez-la, puis vous trouverez un récapitulatif ci-dessous.

%[https://www.youtube.com/watch?v=wdoLEA7U8_M]

Maintenant que nous avons couvert les bases de GitOps, voici un récapitulatif de ses 4 principes principaux. Espérons que vous pourrez les utiliser pour commencer à gérer votre propre cluster avec des flux de travail GitOps.

## Principes de GitOps

### Décrire de manière déclarative

Par 'Déclarative', nous entendons simplement que nous écrivons notre configuration comme un ensemble de faits directement dans notre code source sur Git. Cela devient notre seule 'source de vérité'. 

Par exemple, je peux déclarer mes environnements, tels qu'un 'environnement de test', un 'environnement de staging' ou 'production', et ainsi de suite, ainsi que la version de l'application qui réside dans cet environnement.

### Assurer la versioning de l'état

Avec nos déclarations maintenant stockées dans un système de contrôle de version et agissant comme notre 'source de vérité', nous avons maintenant un seul endroit d'où tout est dérivé. Nous pouvons facilement lancer des versions précédentes de l'application ou effectuer des retours en arrière si nécessaire.

### Automatiser les approbations de changement

Nous devons également permettre à toute modification de nos états déclarés d'être automatiquement appliquée à notre système. Cela vaut la peine d'être mentionné, car maintenant que nous travaillons dans des environnements séparés, nous n'avons plus besoin d'identifiants de cluster pour apporter des modifications à notre système.

### Alerter sur les différences

Maintenant que nous avons l'état de notre système déclaré et versionné, nous pouvons utiliser des agents pour vérifier si tout fonctionne comme il se doit. Cela est considéré comme une 'Boucle de Feedback et de Contrôle'. Si quelque chose 'semble' différent et pas correct, nous en serons alertés.

Pour une analyse plus approfondie de ces 4 principes, vous pouvez regarder la présentation de Cornelia Davis ci-dessus.

Cet article a été écrit par Ania Kubow en soutien à la présentation de conférence faite par Cornelia Davis.

<figure class="kg-card kg-bookmark-card"><a class="kg-bookmark-container" href="https://www.youtube.com/channel/UC5DNytAJ6_FISueUfzZCVsw"><div class="kg-bookmark-content"><div class="kg-bookmark-title">Code with Ania Kubów</div><div class="kg-bookmark-description">Bonjour à tous. Cette chaîne est gérée par Ania Kubow. Dans cette chaîne, je vous enseignerai JavaScript, React, HTML, CSS, React-native, Node.js et bien plus encore ! Un peu à mon sujet : Mon parcours est dans les marchés financiers, où j'ai travaillé comme courtier en dérivés après l'université. Après avoir commencé m</div><div class="kg-bookmark-metadata"><img class="kg-bookmark-icon" src="https://www.youtube.com/s/desktop/6b151e52/img/favicon_144.png"><span class="kg-bookmark-publisher">YouTube</span></div></div><div class="kg-bookmark-thumbnail"><img src="https://yt3.ggpht.com/ytc/AAUvwnjSRt8sIbeM7P--pHoUDh67sDhaNTCMF_XiNOCvUw=s900-c-k-c0x00ffffff-no-rj"></div></a></figure>