---
title: Comment choisir la bonne orchestration de conteneurs et comment la déployer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-01T17:21:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-choose-the-right-container-orchestration-and-how-to-deploy-it-41844021c241
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bYL46jvuTzhBeoswADSHiw.jpeg
tags:
- name: Docker
  slug: docker
- name: Kubernetes
  slug: kubernetes
- name: Microservices
  slug: microservices
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment choisir la bonne orchestration de conteneurs et comment la déployer
seo_desc: 'By Michael Douglass

  Running server processes inside containers is here to stay. If your environment
  is small with a couple of servers running a few dozen containers, you can likely
  get away with doing everything by hand. Beyond that scale, you need g...'
---

Par Michael Douglass

L'exécution de processus serveur dans des conteneurs est là pour rester. Si votre environnement est petit avec quelques serveurs exécutant quelques dizaines de conteneurs, vous pouvez probablement tout faire manuellement. Au-delà de cette échelle, vous avez besoin d'outils performants pour gérer le travail lourd et fournir une fonctionnalité commune et de base. L'alternative est un travail manuel fastidieux, sujet aux erreurs, répétitif.

Si vous n'utilisez pas un pipeline CI/CD et un système d'orchestration, le développement et les opérations devront effectuer une collaboration et une coordination extrêmes et continues.

![Image](https://cdn-media-1.freecodecamp.org/images/321SoCA0X4RdnVeQZsY4ttSZPRd4cBi2pdZf)
_Image Courtesy Julius Silver - [Pexels.com](https://www.pexels.com/photo/white-water-boat-753331/" rel="noopener" target="_blank" title=") — J'espère vraiment qu'ils ont une orchestration pour la façon dont les conteneurs sont chargés sur ces navires… Je ne peux pas imaginer les variables impliquées : Répartition du poids. Destination et ordre de retrait. Volatilité. Cette image me rend heureux de travailler dans le logiciel où je peux aider à gérer la complexité !_

Lorsque j'ai commencé à explorer le monde des microservices plus tôt cette année, je n'avais aucune idée de l'extensive infrastructure de support que je découvrirais. Kubernetes a été une véritable mine d'or, et Istio semble être simplement incroyable pour les microservices — même si je sais que je n'ai fait qu'effleurer la surface de ces deux technologies.

Depuis ses modestes débuts il y a moins de trois ans, Kubernetes a rapidement évolué pour devenir un moteur d'orchestration incroyable utilisé par d'innombrables entreprises et intégré dans de nombreux autres projets. En tant que concepteur de logiciels avec plusieurs décennies d'expérience, je suis très impressionné par l'architecture de Kubernetes. Elle est extrêmement modulaire et construite dans l'attente que de nombreuses pièces puissent être remplacées. Dans certains cas, il existe déjà de nombreux choix pour un composant donné.

Toute cette nouveauté et cette multiplicité de choix peuvent rendre le démarrage assez intimidant. Alors que je suis sur le point de me lancer à fond dans Kubernetes, je suis frappé par une décision plus fondamentale…

### Faire le bon choix d'orchestration de conteneurs

Alors que je commençais à creuser plus profondément dans le monde de l'orchestration de conteneurs, il est devenu évident qu'il existe plus de quelques choix disponibles. Mon instinct me disait que Kubernetes est la solution à utiliser, mais j'ai également commencé à me demander comment je saurais si j'avais raison. Rien de tel que l'incertitude pour pousser à creuser plus profondément.

La première question que je me suis posée était : quelles sont les alternatives pour l'orchestration de conteneurs ?

Après avoir passé un temps raisonnable à rechercher et à lire, voici la liste des systèmes d'orchestration que j'ai pu trouver :

* [Kubernetes](http://kubernetes.io) - Le grand-père apparent de tous. Le projet lui-même est très actif, et l'architecture me donne confiance que le développement continuera à être rapide et sûr. C'est mon choix instinctif.
* [Docker Swarm](https://docs.docker.com/engine/swarm/) - Cela est intégré à Docker par défaut, et possède beaucoup de fonctionnalités de base que vous souhaitez dans un système. Il a beaucoup de parité avec Kubernetes, mais il manque un élément clé : la version gratuite et open-source est le Contrôle d'Accès Basé sur les Rôles (RBAC). Vous pouvez obtenir cela dans la version payante, Enterprise.
* [Marathon](https://github.com/mesosphere/marathon) sur [Mesos](http://mesos.apache.org/) - Mesos lui-même est un système de clustering hautement scalable pour exécuter des tâches de toutes sortes. Il repose sur des frameworks pour supporter différents types de tâches, et Marathon est le plugin qui fournit le support pour l'orchestration de conteneurs dans l'écosystème Mesos. La [liste des frameworks](http://mesos.apache.org/documentation/latest/frameworks/) est impressionnante.
* [Titus](https://github.com/Netflix/titus) - Alors que j'écrivais ceci, Netflix a [open-sourcé](https://medium.com/netflix-techblog/titus-the-netflix-container-management-platform-is-now-open-source-f868c9fb5436) leur système d'orchestration interne. Merci Netflix ! Titus a été conçu pour fournir la plus étroite des intégrations avec l'infrastructure Amazon AWS (où Netflix maintient ses opérations). L'une de leurs intentions est que d'autres projets utiliseront leur technologie afin que Netflix puisse les utiliser à l'avenir.
* [Cattle](https://github.com/rancher/cattle) - Il s'agit du moteur d'orchestration conçu pour et intégré dans le système Rancher. Je n'ai pas donné un regard très approfondi à Cattle, puisque son projet parent a apparemment adopté Kubernetes comme son moteur d'orchestration préféré et principal. Le titre principal sur le site web de Rancher dit : « Enterprise Kubernetes Made Easy. » La page est remplie de la manière dont il vous aide à exécuter des clusters Kubernetes. Aucune mention de Cattle n'existe sur la page web. Il est clair que le projet Rancher a fait son choix.
* [Nomad](https://www.nomadproject.io/) - D'accord, c'est Hashicorp. En tant que grand fan de Hashicorp, je me sentirais injuste si je ne donnais pas à leur produit au moins un coup d'œil. Le produit semble intéressant en surface avec quelques préoccupations majeures de paywall. Les espaces de noms ne sont disponibles que dans la version entreprise. Pour la découverte de services, vous devriez ajouter Consul, et pour la gestion des secrets, vous devriez ajouter Vault. D'après une revue de la documentation, il semble également manquer de configuration CNI de base — la discussion principale pour la configuration réseau porte sur le mappage des ports et les mappages IP statiques.
* Kontena - Il s'agit d'un produit visuellement époustouflant. Vous pouvez exécuter dans leur offre cloud, ou vous pouvez configurer votre propre maître de plateforme sur votre infrastructure de choix. Si vous choisissez d'apporter votre propre infrastructure, vous pouvez choisir de la connecter au Kontena Cloud pour 15 $/mois ou non. L'interface web joliment conçue est ce à quoi vous renoncez dans ce cas. N'ayant pas approfondi au-delà de quelques heures de recherche sur leur site, je ne suis pas certain de l'impact que cela causerait.

Il en existe encore d'autres que vous trouverez des indices si vous cherchez suffisamment : Deis, Mantl, Cloud Foundry, et Amazon ECS pour n'en nommer que quelques-uns. Ces projets méritent probablement plus qu'une simple mention honorable.

#### Exigences d'abord

Faire le choix ici est difficile. Bien sûr, cela dépend de vos exigences, alors laissez-moi lister quelques-unes importantes pour moi :

1. **Développement actif** : Le monde de l'orchestration de conteneurs est relativement jeune. Les projets inactifs seront rapidement laissés pour compte et signifieront que les bugs ne sont pas traités. J'ai le sentiment que Cattle est sur le déclin. Je le raye donc de la liste.
2. **Pas de verrouillage par un fournisseur de cloud** : Je ne suis pas intéressé à être lié à un seul fournisseur de cloud pour le moment. Titus est éliminé ici en raison de son intégration étroite avec AWS, ce qui est définitivement un inconvénient.
3. **Simplicité** : Plus un système est complexe, plus il sera difficile à exploiter. Cette exigence me fait éliminer Mesos de la course, car ce n'est pas un système d'orchestration de conteneurs en premier lieu. Il essaie d'être beaucoup de choses pour beaucoup de gens, et cela semble être un mauvais ajustement.
4. **Réseautage CNI** : La capacité à avoir une connectivité réseau triviale entre mes services est importante. Je ne veux pas que les développeurs passent du temps sur du code spécialisé pour trouver des services dépendants. Docker Swarm et Kubernetes, vous êtes toujours dans la course.
5. **Espaces de noms avec RBAC** - Je travaille dans un environnement d'entreprise, et l'un de mes objectifs est de fournir des configurations de développement, de QA, de staging et de production qui ne se chevauchent pas. Je pourrais configurer un cluster séparé pour chacun, ou je pourrais utiliser RBAC et partager ma puissance de calcul. Docker Swarm, je suis désolé de vous voir partir, mais c'est la fin de notre voyage ensemble. J'adore Hashicorp, mais Nomad met également cette fonctionnalité derrière un paywall.

Vous l'avez, quelques exigences de haut niveau qui réduisent rapidement le champ de jeu. Cela peut ne pas sembler juste d'éliminer Mesos dans la catégorie « simplicité ». Mais si vous passez la moitié du temps que j'ai passé à investiguer toutes ces options, vous comprendrez qu'à un moment donné, vous devez simplifier votre processus de décision afin de commencer à avancer.

Je me retrouve dans l'état bizarre d'avoir toujours Kubernetes et Kontena sur la liste. Kontena est littéralement une investigation de la onzième heure. J'ai presque laissé cela relégué à la liste des autres. Si je l'avais fait, cette dernière heure d'écriture aurait été moins douloureuse. Mais le voici. Une décision doit être prise, et bien que je reviendrai éventuellement à Kontena, Kubernetes est mon vote actuel.

Je me sens coupable de laisser tant de projets incroyables sur le carreau. C'est ce qui arrive dans le monde d'aujourd'hui avec ses options incroyables couplées au besoin ancestral de prendre une décision.

### Commencer avec Kubernetes

J'ai donc choisi Kubernetes comme mon système d'orchestration de conteneurs de choix. Comment puis-je obtenir un cluster opérationnel pour des tests et une utilisation en production ? Les réponses à cette question sont également assez variées.

#### Méthodes de déploiement de Kubernetes

* [Minikube](https://github.com/kubernetes/minikube) : La méthode recommandée pour obtenir un Kubernetes à nœud unique fonctionnant rapidement pour des tests et des fins de développement. Je préfère voir les choses en action complète, donc je n'ai pas opté pour un déploiement à nœud unique pour mes tests.
* [Kubeadm](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/) : Cela est fourni par kubernetes.io comme méthode pour déployer un cluster à maître unique et multi-nœuds. Il existe des instructions supplémentaires pour configurer une configuration multi-maîtres. J'ai précédemment utilisé Kubeadm via quelques scripts Terraform pour configurer mes clusters de test Digital Ocean.
* [Docker Enterprise 2.0](https://www.docker.com/enterprise-edition) : Alors que je travaillais sur cet article, Docker a annoncé la mise à niveau vers EE 2.0. Cette nouvelle version intègre désormais un déploiement complet de Kubernetes intégré au produit. D'après une lecture rapide, ils utilisent Swarm pour démarrer le cluster et déployer Kubernetes.
* [Rancher](https://rancher.com/) : « Enterprise Kubernetes Made Easy » est leur affirmation. En effet, j'ai pu obtenir un cluster Kubernetes complet fonctionnant sur Digital Ocean en moins d'une heure en suivant leur guide. Ma réaction initiale a été : « Wow ! Rancher est incroyable. » Il supporte la gestion des déploiements Kubernetes dans de nombreux environnements et simplifie le déploiement de haute disponibilité. Il prétend permettre la gestion de plusieurs clusters ainsi que la gestion d'autres alternatives d'orchestration, y compris leur propre Cattle et Apache Mesos.
* [Mesosphere DC/OS](https://mesosphere.com/) : Peut-être arrivant comme un champion encore plus lourd en tant que système d'orchestration de conteneurs à part entière, mais maintenant également capable d'administrer des clusters Kubernetes. Ce produit semble assez convaincant… Sauf que les vraiment bonnes choses sont derrière le [paywall Enterprise](https://mesosphere.com/pricing/). Je ne suis pas non plus certain sur leur site web si la version DC/OS est gratuite et si la version DC/OS Enterprise est payante (ou si les deux sont payantes). Chaque fois que je vois un « Contactez-nous pour les prix », j'ai tendance à passer mon chemin. Cela m'empêchera de regarder de trop près — mes excuses à quiconque j'ai offensé.
* [Pharos de Kontena](https://pharos.sh/) - Il semble que même les entreprises qui ont leur propre alternative complète à Kubernetes ne peuvent pas garder leurs mains hors des initiatives logicielles de déploiement de Kubernetes. Leur documentation sur l'[« Utilisation avec Terraform »](https://pharos.sh/docs/usage/terraform.html) semble avoir beaucoup de puissance pour faire de votre installation Kubernetes une étape distincte et composable. Vous pouvez configurer votre infrastructure en une étape en utilisant l'outil de votre choix pour cela, puis configurer Kubernetes par-dessus. `setup-infrastructure | install-kubernetes > pro`fit

La liste continue : Kubo de Pivitol, Kismatic d'Apprenda, Tectonic de CoreOS, RedHat Openshift v3, Openshift Origin, et certainement plus.

#### Options hébergées

* [Amazon EKS](https://aws.amazon.com/eks/) - Elastic Container Service pour Kubernetes — Un cluster Kubernetes hébergé par Amazon. Il s'agit actuellement d'une technologie « En Préversion » par Amazon. Cela témoigne de la viabilité et de l'avenir de Kubernetes…
* [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine/) — Il s'agit de l'offre hébergée de Google. J'aimerais en dire plus, mais pour une raison quelconque, mon compte est bloqué en ce qui concerne l'accès à celui-ci.
* [OpenShift](https://www.openshift.com/) - Le service de conteneurs en ligne de Red Hat.

#### Mon choix de déploiement de Kubernetes ?

Pour le déploiement de Kubernetes, je prévois de continuer à travailler avec Kubeadm (peut-être en le remplaçant par Pharos) ainsi qu'avec Rancher.

Rancher a montré une grande promesse la première fois que je l'ai utilisé. Le seul inconvénient est que je dois d'abord avoir une machine de contrôle sur laquelle j'installe Rancher, mais c'est un petit prix à payer. Je ne suis pas certain que je voudrai utiliser l'interface Rancher pour interagir avec mon cluster Kubernetes, et tant qu'elle ne se met pas en travers de mon utilisation de `kubectl` pour contrôler le cluster, nous pouvons nous entendre très bien.

### Qu'est-ce qui suit ?

Maintenant que j'ai fait l'exercice de comprendre le monde des options, je suis prêt à me plonger et à expérimenter avec Kubernetes. Il y a beaucoup d'exploration que je dois faire avec mes méthodes de déploiement de choix.

J'ai également parlé auparavant d'Istio qui s'appuie sur Kubernetes pour fournir encore plus de fondations pour supporter la communication et la surveillance des microservices. Attendez-vous à en entendre plus dans les prochains articles. Oh, et maintenant que j'ai trébuché sur Kontena, je me sens attiré pour lui donner un essai. 😊