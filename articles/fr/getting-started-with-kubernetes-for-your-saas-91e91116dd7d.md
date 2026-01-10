---
title: Prise en main de Kubernetes pour votre SaaS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-29T16:21:53.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-kubernetes-for-your-saas-91e91116dd7d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hZx56ZEx75a9_xlC1smdOQ.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Devops
  slug: devops
- name: SaaS
  slug: saas
- name: software
  slug: software
- name: 'tech '
  slug: tech
seo_title: Prise en main de Kubernetes pour votre SaaS
seo_desc: 'By Ben Sears

  Kubernetes is a platform to manage and orchestrate your cloud infrastructure. It
  provides a configuration-driven framework where you can define a few different pieces
  and with one click get an entire network, disk, and application spun u...'
---

Par Ben Sears

[Kubernetes](https://kubernetes.io/) est une plateforme pour gérer et orchestrer votre infrastructure cloud. Il fournit un framework piloté par la configuration où vous pouvez définir différents éléments et, en un clic, obtenir un réseau complet, un disque et une application déployés de manière scalable et facile à gérer.

Déplacer votre application vers Kubernetes est une activité à forte intensité si vous n'avez pas conçu votre application avec des conteneurs dès le départ. Le but de cet article est de vous aider sur votre chemin vers la conteneurisation de vos applications avec une intégration Kubernetes en tête.

Soyez conscient que si vous essayez de forcer votre application dans Kubernetes sans l'architecture appropriée, vous vous tirerez essentiellement une balle dans le pied en perdant du temps et en accumulant de la dette technique.

### Étape 1 — Conteneurisez votre application ✨

Un conteneur est essentiellement une section partitionnée du système d'exploitation qui peut fonctionner comme une machine indépendante. Contrairement aux machines virtuelles traditionnelles, qui reposent sur un hyperviseur pour simuler un système d'exploitation, les conteneurs utilisent diverses fonctionnalités du noyau pour fournir un environnement isolé de la machine hôte.

![Image](https://cdn-media-1.freecodecamp.org/images/OnPF9sW3GZAZqG0BxOcBdRlVYyQHLUT9jjR1)
_Les applications conteneurisées peuvent s'exécuter de manière prévisible sur toutes les machines, pas seulement la vôtre_

La conteneurisation est un processus assez simple — en utilisant Docker, il suffit de définir un Dockerfile qui décrit les étapes nécessaires pour installer votre application sur un système d'exploitation (télécharger des packages, installer des dépendances, etc.).

Ensuite, construisez une image qui peut être utilisée par les développeurs. Plus d'informations sur le processus de conteneurisation peuvent être trouvées sur [le site web de Docker](https://docs.docker.com/engine/examples/).

### Étape 2 — Adoptez une architecture multi-instances 🚀

![Image](https://cdn-media-1.freecodecamp.org/images/Xmd3dBrgwkSRtjoOgvq-1uy-qn6duclrLyyx)
_La décision d'opter pour une architecture multi-locataire ou multi-instances vous mènera sur des chemins différents_

Avant de passer à Kubernetes, vous devez examiner attentivement la manière dont vous livrez actuellement votre application à l'utilisateur final.

Les applications web traditionnelles utilisent une architecture **multi-locataire**. Cela signifie que tous vos utilisateurs partageront une seule instance de base de données et une seule instance d'une application. Cela peut fonctionner dans Kubernetes — cependant, je vous exhorte à envisager de mettre en œuvre une architecture **multi-instances** pour tirer pleinement parti de la puissance de Kubernetes et des applications conteneurisées.

Certains avantages majeurs de l'adoption d'une architecture multi-instances sont :

* **Stabilité** — Au lieu d'un seul point de défaillance (l'instance unique de l'application), chaque client peut exister dans sa propre instance. Si une instance tombe en panne, les autres resteront indemnes.
* **Scalabilité** — Avec une architecture multi-instances, la montée en charge est une simple question d'ajout de plus de ressources. Cependant, avec une architecture multi-locataire, vous pourriez atteindre un point où vous devez concevoir une architecture d'application en cluster dont le déploiement est généralement loin d'être trivial.
* **Sécurité** — Lorsque vous utilisez une seule base de données, toutes vos données coexistent. Cela devient un problème majeur en cas de violation de sécurité, car les données de tous les clients peuvent devenir vulnérables lorsqu'un seul compte est compromis. Avec une architecture multi-instances, seules les données d'un seul client peuvent être à risque.

### Étape 3 — Déterminez la consommation de ressources de votre application ⚙️

Pour avoir l'infrastructure la plus rentable, vous devez déterminer combien de CPU, de mémoire et de stockage seront nécessaires pour exécuter une seule instance de votre application.

De cette manière, vous pouvez définir des limites pour obtenir une lecture précise de l'espace dont vos nœuds Kubernetes ont besoin, ainsi que pour vous assurer que vos nœuds ne vont pas devenir surchargés et peu fiables.

C'est généralement un processus d'essais et d'erreurs, mais vous pouvez utiliser une solution de surveillance telle que [Heapster](https://github.com/kubernetes/heapster/) pour obtenir une répartition claire des ressources que vos pods consomment. Cela vous permettra d'évaluer combien allouer.

![Image](https://cdn-media-1.freecodecamp.org/images/3SWNHqbaF-aFU8eHKYfW6YZwegsKrnKQR2UG)
_Heapster fournit des visualisations de l'utilisation des ressources de votre charge de travail_

Une fois que vous avez déterminé votre allocation de ressources, vous pouvez calculer les tailles optimales des serveurs pour vos nœuds Kubernetes afin d'obtenir le meilleur rapport qualité-prix.

Vous prenez la mémoire ou le CPU dont chaque instance a besoin pour fonctionner, et vous le multipliez par 100 (le nombre maximum de pods qu'un nœud peut contenir). Cela vous donnera une estimation approximative de la quantité de mémoire/CPU que vos nœuds devraient avoir.

Toutefois, vous devriez toujours tester votre application sous charge pour vous assurer qu'elle fonctionne correctement lorsque le nœud est rempli.

### Étape 4 — Intégrez avec Kubernetes ⚓

Une fois que votre cluster Kubernetes est opérationnel, il existe de nombreuses pratiques DevOps que vous pouvez commencer à développer pour vous faciliter la vie. Certains de ces points d'intégration prennent les formes suivantes :

#### Mise à l'échelle automatique des nœuds Kubernetes

Lorsque vos nœuds deviennent pleins, généralement vous souhaitez approvisionner plus de nœuds pour que tout continue à fonctionner correctement. Une façon de faire cela est avec un outil comme [kops](https://github.com/kubernetes/kops).

#### Mise à l'échelle automatique des applications

Certaines applications devront être mises à l'échelle en fonction de l'utilisation actuelle. Kubernetes fournit cette fonctionnalité directement avec des déclencheurs qui mettent automatiquement à l'échelle les déploiements. Par exemple, exécuter cette commande :

```
kubectl autoscale deployment myapp --cpu-percent=50 --min=1 --max=10
```

définira le déploiement _myapp_ pour qu'il monte jusqu'à 10 pods lorsque le pourcentage de CPU dépasse 50.

#### Approvisionnement automatique des instances à l'action de l'utilisateur

Pour une architecture multi-instances, les utilisateurs finaux demanderont finalement que des applications soient déployées dans Kubernetes. Pour fournir cela, vous devriez envisager d'intégrer votre application avec l'[API Kubernetes](https://kubernetes.io/docs/api-reference/v1.9/), ou utiliser une solution tierce telle que [ServiceBot](https://servicebot.io) pour fournir un portail de demande d'instances.

#### Définition personnalisée du nom d'hôte par l'action de l'utilisateur

Une tendance croissante ces derniers temps a été que les utilisateurs finaux attachent leur domaine aux applications. Kubernetes dispose d'outils pour faciliter ce processus et même en arriver au point où il devient en libre-service (les utilisateurs appuient sur un bouton pour que leur domaine pointe vers le pod). Vous pouvez utiliser un système tel que [Nginx Ingress](https://github.com/kubernetes/ingress-nginx) pour y parvenir.

### Conclusion

Kubernetes est un excellent moyen de gérer votre infrastructure cloud. Si vous êtes dans une situation où vous avez du mal à mettre à l'échelle votre application, envisagez de passer à une architecture basée sur Kubernetes. Vous verrez une augmentation significative de votre productivité DevOps en matière de déploiements, de clustering et de stabilité globale.

[_ServiceBot_](https://servicebot.io) _est une plateforme qui vous aide à gérer votre SaaS en automatisant la facturation, les déploiements et votre pipeline de ventes._

#### Vous cherchez à mettre à l'échelle votre SaaS ? [Parlons-en](http://bit.ly/sbotconsult).