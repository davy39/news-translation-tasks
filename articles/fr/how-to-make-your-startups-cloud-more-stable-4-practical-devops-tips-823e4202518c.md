---
title: 'Comment rendre le cloud de votre startup plus stable : 4 conseils DevOps pratiques'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T16:47:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-startups-cloud-more-stable-4-practical-devops-tips-823e4202518c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Qi_8eBa0Xe1vniGhxkDmGA.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: 'Comment rendre le cloud de votre startup plus stable : 4 conseils DevOps
  pratiques'
seo_desc: 'By Ben Sears

  In the startup world, there is a balancing act when it comes to where you invest
  your time. I’ve been in many situations where, due to the need to ship an MVP, DevOps
  practices take a backseat.

  I consider this to be normal and not really...'
---

Par Ben Sears

Dans le monde des startups, il y a un équilibre à trouver en ce qui concerne l'endroit où vous investissez votre temps. J'ai été dans de nombreuses situations où, en raison de la nécessité de livrer un MVP, les pratiques DevOps passent au second plan.

Je considère cela comme normal et pas vraiment une mauvaise chose car "MVP" devrait être "Minimal", et la plupart des problèmes résolus par de bonnes pratiques DevOps ne sont pas des problèmes à une si petite échelle.

Mais voici quelques choses qui devraient définitivement être faites (ou au moins considérées). Parce qu'il n'y a pas grand-chose de pire dans le monde des startups que de voir votre infrastructure cloud tomber en panne.

![Image](https://cdn-media-1.freecodecamp.org/images/k305qMPtQ5JQ-YTmewSKZ4QMr3yDxxi4Lhso)
_C'est difficile de trouver du temps pour le DevOps dans une startup quand il y a tant d'autres choses à faire_

### Conseil #1 : Planifiez des sauvegardes de vos données ?

C'est une nécessité pour toute startup qui se soucie d'avoir des données persistantes. Vous devez sauvegarder automatiquement vos données critiques ou vous risquez de perdre plus que des fichiers, vous perdrez également la confiance des clients, ce qui affectera votre croissance future.

Je généralement automatise deux types de méthodes de sauvegarde lors du démarrage de projets

#### Sauvegardes de base de données

Cela prend généralement la forme d'un script planifié, comme un travail cron qui s'exécute chaque nuit et pousse un dump de la base de données quelque part sur le cloud comme un bucket S3 privé. Vous pouvez avoir des solutions plus sophistiquées avec certaines solutions de sauvegarde, mais celles-ci tendent à être plus axées sur les entreprises et vous coûteront beaucoup de temps et d'argent (pas adapté aux startups).

![Image](https://cdn-media-1.freecodecamp.org/images/xVaOSbJdAg94fofj9T705IRPpB8xOnY5ttfH)

#### Instantanés de disque

Quand tout le reste échoue, si vous avez une copie de votre disque, vous serez généralement en sécurité. La plupart des grands fournisseurs de cloud ont des solutions en place qui vous permettent de prendre des instantanés de disque selon un calendrier de votre choix, alors essayez d'éviter d'écrire des scripts qui se connectent directement à l'API cloud, car vous serez responsable de leur maintenance.

#### ? ?Assurez-vous de tester votre méthode de restauration de sauvegarde ou risquez ce qui est arrivé à GitLab où toutes leurs 5 méthodes de sauvegarde ont échoué parce qu'ils n'ont jamais testé la restauration??

### Conseil #2 : Configurez la surveillance et soyez alerté des problèmes ?

Saurez-vous quand un serveur tombe en panne ou qu'une application plante en raison d'un manque d'espace disque ? Si ce n'est pas le cas, vous devriez envisager de résoudre ce problème (cela ne prend pas trop de temps).

La manière la plus simple de configurer la surveillance serait généralement une solution de fournisseur cloud comme [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) ou [GCP Stackdriver](https://cloud.google.com/monitoring/). Vous pouvez configurer des métriques à surveiller et avoir différents types d'alertes en réponse à ces événements se produisant dans votre infrastructure cloud, par exemple recevoir un email lorsque votre disque est presque plein.

Si vous ne voulez pas opter pour la solution d'un fournisseur, il existe également des options agnostiques de cloud qui peuvent surveiller votre cloud. Des solutions simples existent, comme la planification de [scripts shell qui envoient des emails](http://www.linuxjournal.com/content/tech-tip-send-email-alert-when-your-disk-space-gets-low) pour s'exécuter périodiquement, mais une solution plus complète qui vous donne une vue de tableau de bord de votre système est généralement meilleure et beaucoup plus évolutive. Des options comme [Blue Medora](https://bluemedora.com/) et [Solar Winds](https://www.solarwinds.com/) existent pour le cloud privé d'entreprise, mais la plupart des startups doivent économiser de l'argent, ce qui signifie se tourner vers des solutions open source telles que [Countly](https://count.ly/).

En résumé, je recommanderais d'opter pour une solution basée sur un fournisseur cloud, car celles-ci seront garanties stables, faciles à configurer et, à l'échelle d'une startup, ne vous coûteront pas beaucoup plus.

### Conseil #3 : Passez à un pipeline CI/CD ?

![Image](https://cdn-media-1.freecodecamp.org/images/u3t9eAehi-11vaS36FCSnYsIYtc94mPTGuoS)

L'un des défis courants que je vois avec les startups est le processus de publication de code. Beaucoup n'ont pas encore pris le temps de développer un pipeline de publication stable, ce qui signifie que le code qui est poussé vers le contrôle de version est soit testé, construit et publié manuellement, ce qui est à la fois sujet aux erreurs et chronophage pour votre équipe de développement.

#### Intégration continue — Assurer que les changements ne sont pas cassants

Le but de l'intégration continue est d'avoir un pipeline qui est déclenché chaque fois que le code est prêt à être validé.

![Image](https://cdn-media-1.freecodecamp.org/images/M-Dh7rZOrTVvpB7ExmQgrwq971QiOmVcPv5C)
_L'intégration continue protège la stabilité de votre base de code_

1. Le code est validé dans le contrôle de version
2. Un système d'automatisation comme Jenkins crée une build de l'application
3. Des tests automatisés sont effectués pour valider que le système fonctionne toujours correctement
4. Une fois tous les tests passés, le code est autorisé à être ajouté à la base de code stable
5. Le nouveau code est maintenant prêt pour le déploiement (c'est là que le déploiement continu entre en jeu)

#### Déploiement continu — Automatiser vos publications en production

Le déploiement continu commence après que votre pipeline d'intégration continue ait fait son travail de validation que le nouveau code ne cassera pas votre build. Cela consiste généralement à créer une nouvelle build de production, comme ce qui a été fait dans l'étape d'intégration continue, et à remplacer l'ancienne build (infrastructure immuable).

Techniquement, vous pouvez avoir un déploiement continu sans intégration continue, mais les risques de le faire sont grands. Vous pousseriez essentiellement du code non testé directement aux clients (?B**AD?**)

#### **Par où commencer lorsque vous passez à CI/CD ? — Les tests automatisés !**

Ce n'est un secret pour personne, la plupart des développeurs n'aiment pas écrire des tests. Ils ont tendance à nécessiter des mises à jour constantes à mesure que les applications évoluent et sont un grand puits de temps, donc naturellement, de nombreuses startups négligeront l'écriture de tests parce que "MVP".

Si vous n'avez pas une suite de tests complète, je ne m'embêterais pas à penser à CI/CD jusqu'à ce que cela soit remedied. À mesure que la couverture des tests s'améliore, vous commencerez à voir des gains d'efficacité majeurs à mesure que vous verrez de moins en moins de bugs en production. C'est à ce moment-là que vous devriez passer aux autres pièces de votre pipeline CI/CD.

### Conseil #4 : Conteneurisez votre application ?

![Image](https://cdn-media-1.freecodecamp.org/images/Rl8fBg6SSZ2ixPA3NjmdWfzYRuFgfQ9HT1AB)
_Les conteneurs facilitent la création de builds automatisées d'applications_

N'ayez pas peur des conteneurs, bien que la technologie elle-même soit complexe et difficile à comprendre sans une connaissance fondamentale des noyaux, en tirer parti et convertir des applications en conteneurs est vraiment assez trivial.

Cela prend généralement moins d'une heure pour assembler un Dockerfile (selon la complexité de votre application) et avant que vous ne le sachiez, vous pouvez déployer votre application instantanément et tirer parti de grands systèmes tels que Kubernetes.

Voici quelques avantages que vous pouvez obtenir immédiatement en conteneurisant votre application.

#### **Builds cohérents**

Plus de problèmes "ça marche sur ma machine" — Si le conteneur se construit, il fonctionnera de la même manière sur n'importe quelle machine.

#### **Déploiements sans douleur**

Vous savez comment, lorsque vous voulez configurer un projet open-source, vous devez passer par toutes sortes d'étapes manuelles, configurer des bases de données et installer des packages requis ? Avec les conteneurs, ce n'est plus le cas, toutes ces étapes sont intégrées dans le processus de build et tout ce que vous avez à faire est d'exécuter une seule commande pour démarrer vos serveurs.

#### **Un écosystème de conteneurs vibrant**

Les plateformes de conteneurs comme Docker et Kubernetes ont un écosystème très large et en croissance de produits et services pour vous aider à gérer vos applications plus facilement. Beaucoup de maux de tête autour de choses comme le stockage, la mise en réseau et l'allocation de ressources sont essentiellement éliminés, vous faisant économiser du temps et de l'argent.

### Conclusion

De nombreuses startups ne consacrent pas beaucoup de temps ou de réflexion à leur infrastructure cloud. Cela est généralement dû à la philosophie MVP de livrer d'abord et de nettoyer la dette technique ensuite.

Lorsque vous cherchez à développer votre infrastructure DevOps, envisagez des sauvegardes planifiées, la surveillance, CI/CD et la conteneurisation. Ce sont généralement des gains faciles et mèneront à un cloud beaucoup plus stable.

### Vous voulez développer votre infrastructure cloud ? [ServiceBot peut aider](https://servicebot.io?ref=medium3).