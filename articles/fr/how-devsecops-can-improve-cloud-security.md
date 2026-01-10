---
title: Comment DevSecOps peut améliorer la sécurité du cloud ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-26T21:28:20.000Z'
originalURL: https://freecodecamp.org/news/how-devsecops-can-improve-cloud-security
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/devsecops-role-guide.jpg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: Devops
  slug: devops
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
seo_title: Comment DevSecOps peut améliorer la sécurité du cloud ?
seo_desc: 'By Andrej Kovacevic

  There’s no doubt that DevSecOps is on the rise, as the need for fast but highly
  secure application delivery increases.

  A report by Emergen Research shows that the DevSecOps market is set to reach a $23.42
  billion value in 2028 wit...'
---

Par Andrej Kovacevic

Il ne fait aucun doute que DevSecOps est en pleine croissance, car le besoin de livraison rapide mais hautement sécurisée des applications augmente.

Un [rapport d'Emergen Research](https://www.prnewswire.com/news-releases/devsecops-market-size-to-reach-usd-23-42-billion-in-2028--rising-need-for-repeatable-and-adaptive-processes-and-increasing-need-for-custom-code-security-are-key-factors-driving-industry-demand-says-emergen-research-301481508.html) montre que le marché DevSecOps devrait atteindre une valeur de 23,42 milliards de dollars en 2028 avec un TCAC de 32,2 % sur la période de prévision 2020-2028.

Notamment, cette croissance ne répond pas seulement à l'importance croissante de la sécurité dans le développement et la livraison rapides d'applications. Elle a également un impact positif significatif sur la sécurité du cloud.

Alors que les organisations voient une utilisation accrue de l'informatique en nuage et des applications SaaS, l'adoption de DevSecOps devient également plus attrayante.

## La situation actuelle de la sécurité du cloud

Une [enquête](https://cloudsecurityalliance.org/blog/2022/05/02/the-state-of-data-security-in-2022) sur l'état de la sécurité des données dans le cloud en 2022, menée en partenariat avec Gartner, montre qu'une majorité écrasante d'organisations (plus de 90 %) déclarent avoir du mal à faire respecter les politiques de sécurité autour de leurs données. Cela est dû à diverses raisons, qui ajoutent aux difficultés de la sécurité du cloud.

Les solutions conventionnelles ne suffisent plus, et la [sécurité du cloud](https://www.checkpoint.com/cyber-hub/cloud-security/what-is-cloud-security/) doit monter d'un niveau pour répondre aux différents défis apportés par l'adoption croissante du cloud et les complexités qui l'accompagnent.

Ces défis incluent les suivants :

### Inadéquations de la visibilité et du suivi

Alors que les organisations adoptent les applications Software-as-a-Service (SaaS) et le modèle Infrastructure-as-a-Service (IaaS), elles sont confrontées au défi de protéger les données et les actifs qui sont généralement hors de leur contrôle.

Typiquement, les fournisseurs de services cloud ne donnent pas aux clients un contrôle total sur la couche infrastructure. Cela produit un manque de visibilité et de contrôle dans le contexte de la sécurité.

### Surfaces d'attaque plus larges

Les acteurs de la menace sont particulièrement attirés par les organisations qui utilisent l'environnement cloud public. Il est relativement facile d'attaquer avec des attaques zero-day, des logiciels malveillants, des prises de contrôle de compte et d'autres attaques en l'absence de solutions de sécurité fiables.

### Changements de charge de travail

La nature dynamique de la provision et de la désaffectation des actifs cloud rend difficile leur protection, surtout lorsque la mise à l'échelle et l'agilité sont impliquées.

### Environnements complexes

Les environnements hybrides et multi-cloud semblent être préférés par de nombreuses organisations actuellement en raison de [divers avantages](https://www.techradar.com/news/benefits-of-a-hybrid-multicloud-strategy). Mais cela entraîne des complexités de gestion de la sécurité et le besoin d'outils et de solutions de sécurité qui fonctionnent de manière transparente ensemble.

### Le besoin de gestion granulaire des privilèges et des clés

En raison du nombre d'utilisateurs qui accèdent aux actifs cloud, il n'est pas rare que l'accès ou les privilèges soient accordés de manière lâche. Des privilèges étendus sont généralement fournis pour éviter d'avoir à implémenter des configurations spécifiques pour différents utilisateurs ou groupes d'utilisateurs.

Cela peut poser problème pour la sécurité. Avec l'utilisation d'applications SaaS, par exemple, lorsque les clés et les privilèges sont accordés de manière négligente, les sessions peuvent être exposées à divers risques de sécurité.

### Affaiblissement des avantages de conformité aux normes cloud

Les principaux fournisseurs de services cloud annoncent notamment leur conformité à diverses accréditations ou normes de sécurité telles que le NIST 800-53, PCI 3.2 et GDPR. Mais les avantages de la conformité sont dilués ou presque entièrement érodés parce que la gestion des processus de charge de travail et de données est généralement reléguée aux clients (organisations).

Puisque la plupart des organisations ont des difficultés de visibilité et de suivi, des capacités de gestion de surface d'attaque médiocres et un manque de gestion granulaire des privilèges, la conformité de sécurité des fournisseurs de cloud ne bénéficie pas nécessairement à leurs clients.

### La montée de DevOps

De nombreuses organisations ont adopté DevOps alors qu'elles cherchent à raccourcir le cycle de vie du développement des systèmes et à promouvoir une livraison rapide et continue des applications.

Cela peut avoir un impact sur la sécurité du cloud, surtout lorsqu'il y a des changements liés à la sécurité mis en œuvre après le déploiement de la charge de travail.

## Comment DevSecOps peut aider

Comme je l'ai expliqué ci-dessus, ce n'est pas seulement l'expansion des surfaces d'attaque et les complexités de gestion de la sécurité qui accompagnent l'adoption du cloud qui rendent la sécurité du cloud plus difficile. L'adoption accrue des pratiques DevOps ajoute également au problème. C'est là que DevSecOps entre en jeu.

DevSecOps ajoute le composant crucial de la sécurité à DevOps et guide les développeurs à adopter la "sécurité par conception".

C'est une évolution par rapport à la stratégie précédente de déplacement et d'adoption utilisée dans le re-platforming incrémental du cloud. Il implique une équipe intégrée de spécialistes multiqualifiés dans le domaine du cloud et de la cybersécurité travaillant ensemble sous un paradigme opérationnel commun.

Les équipes peuvent établir un centre d'excellence (généralement dirigé par la personne responsable de la transformation numérique de l'organisation) pour prendre en charge la coordination des spécialistes du cloud et de la cybersécurité travaillant ensemble dans le nouveau modèle opérationnel de développement.

DevSecOps garantit que les pratiques flexibles et agiles ne négligent pas la sécurité, permettant aux processus de développement de progresser au même rythme que celui auquel une organisation souhaite faire avancer son activité.

Les équipes peuvent y parvenir en mettant l'accent sur les responsabilités partagées. Les organisations favorisent la collaboration, le développement de compétences croisées et le travail en équipe croisée pour obtenir de meilleurs résultats.

[Diana Kearns-Manolatos](https://devops.com/devsecops-rethinking-and-reengineering-cloud-security/), Senior Manager au Centre for Integrated Research de Deloitte, caractérise DevSecOps comme "plus que le déplacement des processus de sécurité existants plus tôt dans le processus de développement".

DevSecOps implique de repenser et de réarchitecturer la manière dont les processus de conception d'applications fonctionnent. "Il s'agit d'élever, d'intégrer et de faire évoluer la réponse aux risques de (votre) organisation", ajoute Kearns-Manolatos.

Pour répondre à la question "Quel est le rôle de DevSecOps dans la sécurité du cloud ?", les équipes doivent intégrer la sécurité dans l'efficacité, la rapidité et la continuité de DevOps.

En termes simples, il s'agit de déployer rapidement des applications ou des produits logiciels déjà sécurisés pour mieux gérer l'expansion des surfaces d'attaque cyber.

Au lieu d'avoir une autre équipe (l'équipe de sécurité) entreprendre un examen rigoureux de la sécurité des applications, les applications peuvent être déployées immédiatement. Des ajustements et des correctifs seront toujours nécessaires éventuellement, mais ils ne seront plus aussi épuisants que par rapport au déploiement d'applications développées de manière conventionnelle.

## DevSecOps en pratique – Pas facile mais tout à fait réalisable

Adopter DevSecOps pour réaliser le déploiement rapide, sécurisé et efficace des applications ou des produits logiciels ne sera pas une promenade de santé. Mais ce n'est pas non plus excessivement compliqué pour être restrictivement réalisable.

Les organisations seront confrontées au besoin d'innovation dans les processus et devront repenser leurs opérations de sécurité du cloud et de développement.

Un facteur crucial pour adopter avec succès les pratiques DevSecOps afin d'améliorer les résultats de développement (en particulier en termes de sécurité) est la communication.

Les équipes doivent communiquer correctement entre elles pour s'assurer que tout le monde est sur la même longueur d'onde pendant le processus de développement. Le partage des connaissances en temps réel est important et il peut également être nécessaire d'intégrer [ChatOps](https://www.techtarget.com/searchitoperations/definition/ChatOps), l'automatisation ainsi que l'intelligence artificielle dans le processus.

## Réflexions finales

DevSecOps et la sécurité du cloud peuvent sembler être des concepts sans rapport ou faiblement connectés. Mais le premier a bel et bien un impact sur le second.

DevSecOps ne résoudra pas tous les problèmes ou menaces de sécurité du cloud. Mais il peut rendre les applications pilotées par DevOps utilisées sur le cloud ou dans des environnements hybrides moins vulnérables, et peut limiter les moyens pour les acteurs de la menace de pénétrer les défenses cyber.

Si vous souhaitez en savoir plus sur DevSecOps en profondeur, [consultez cet article et ce cours gratuits de freeCodeCamp](https://www.freecodecamp.org/news/what-is-devsecops/).

_Image via Murrstock / Adobe Stock_