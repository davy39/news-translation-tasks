---
title: Un guide pour débutants sur Amazon Elastic Container Service
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-20T17:25:22.000Z'
originalURL: https://freecodecamp.org/news/amazon-ecs-terms-and-architecture-807d8c4960fd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*F_Av332fsAf6RJ97gM2h8w.png
tags:
- name: Amazon
  slug: amazon
- name: AWS
  slug: aws
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: technology
  slug: technology
seo_title: Un guide pour débutants sur Amazon Elastic Container Service
seo_desc: 'By Dominic Fraser

  This article is a beginner’s high level look at Amazon ECS. We’ll cover core concepts,
  terms, simple architecture diagrams, and abstracted examples. So let’s get started!

  Docker

  To appreciate Amazon ECS, you first have to understand...'
---

Par Dominic Fraser

Cet article est une introduction de haut niveau à Amazon ECS pour les débutants. Nous allons couvrir les concepts de base, les termes, des diagrammes d'architecture simples et des exemples abstraits. Alors, commençons !

### Docker

Pour apprécier Amazon ECS, vous devez d'abord comprendre Docker.

Docker est une application client-serveur qui peut être installée sur Linux, Windows et MacOS et qui vous permet d'exécuter des [conteneurs](https://en.wikipedia.org/wiki/Operating-system-level_virtualization) Docker. Les conteneurs sont des environnements légers contenant tout ce qui est nécessaire pour exécuter une application spécifique ou une partie d'une application. Plusieurs conteneurs différents peuvent être exécutés sur une seule machine, à condition qu'elle ait le logiciel Docker installé.

Si vous êtes intéressé par **comment** ils fonctionnent et comment Docker est différent d'une machine virtuelle, alors cette [introduction à Docker](https://medium.com/pintail-labs/docker-series-what-is-docker-9eddca88f434) est un excellent point de départ.

![Image](https://cdn-media-1.freecodecamp.org/images/N-3HpONvjcv4ZhAeMBN43aO1XfLfwDcOL2oe)
_Adapté de Docker's [bins/libs](https://docs.docker.com/get-started/#container-diagram" rel="noopener" target="_blank" title="">get started</a>, voir ici pour [Filesystem Hierarchy Standard](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard" rel="noopener" target="_blank" title=")_

L'utilisation de conteneurs Docker permet aux équipes d'avoir un environnement de développement cohérent en abstraisant le logiciel, le système d'exploitation et la configuration matérielle en un bloc de construction standard qui peut être exécuté sur n'importe quelle machine.

Chaque conteneur a exactement ce dont il a besoin — par exemple, certaines versions d'un langage ou d'une bibliothèque — et rien de plus. Plusieurs conteneurs peuvent être utilisés pour différentes parties de votre application si vous le souhaitez, et ils peuvent être configurés pour communiquer entre eux lorsque cela est nécessaire.

En utilisant des conteneurs Docker spécifiés pour exécuter votre code de production, vous pouvez être sûr que votre environnement de développement est exactement le même que votre environnement de production.

À mesure que votre application grandit, la gestion du déploiement, de la structure, de la planification et de la mise à l'échelle de ces conteneurs devient rapidement très compliquée. C'est là qu'intervient un « service de gestion de conteneurs ». Il vise à permettre des options de configuration simples et à gérer les tâches lourdes pendant que vous retournez à l'écriture de l'application.

### Une introduction à Amazon ECS

Amazon [Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) (ECS) est, selon Amazon,

> _...un service de gestion de conteneurs hautement scalable et rapide qui facilite l'exécution, l'arrêt et la gestion des conteneurs Docker sur un cluster._

Il est comparable à [Kubernetes](https://kubernetes.io/), [Docker Swarm](https://docs.docker.com/swarm/overview/), et [Azure Container Service](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/microsoft.acs).

![Image](https://cdn-media-1.freecodecamp.org/images/4wqn-TABgSmokYgU0tGgbvk8kTng0ibENfLX)

ECS exécute vos conteneurs sur un cluster d'instances de [Amazon EC2](https://aws.amazon.com/ec2/) (Elastic Compute Cloud) [machines virtuelles](https://www.youtube.com/watch?v=TsRBftzZsQo) préinstallées avec Docker. Il gère l'installation des conteneurs, la mise à l'échelle, la surveillance et la gestion de ces instances via une API et la console de gestion AWS. Il vous permet de simplifier votre vue des instances EC2 en un pool de ressources, telles que le CPU et la mémoire. L'instance spécifique sur laquelle un conteneur s'exécute, et la maintenance de toutes les instances, est gérée par la plateforme. Vous n'avez pas à y penser.

Il est important de noter qu'il est intégré à l'infrastructure Amazon, contrairement à certains autres fournisseurs qui permettent plus de flexibilité. Cependant, cela signifie qu'il offre une excellente intégration avec d'autres services AWS.

### Termes et architecture

Donnons un contexte imaginaire aux définitions que nous allons examiner. Supposons que vous construisez une application qui s'exécute sur deux conteneurs Docker, peut-être un pour l'application principale et un pour la gestion des métriques. Les deux sont nécessaires pour que l'application fonctionne comme prévu. Si vous aviez de grandes quantités de trafic, vous pourriez avoir besoin d'exécuter plusieurs paires de conteneurs.

Ici, nous arrivons à deux ensembles de nouveaux termes :

* une **Définition de Tâche**, **Tâche** et **Service**, et
* un **Cluster**, **Instance de Conteneur ECS** et **Agent de Conteneur ECS**.

#### Définition de Tâche

C'est le plan décrivant quels conteneurs Docker exécuter et représentant votre application. Dans notre exemple, ce serait deux conteneurs. Il détaillerait les images à utiliser, le CPU et la mémoire à allouer, les variables d'environnement, les ports à exposer et comment les conteneurs interagissent.

#### Tâche

Une instance d'une Définition de Tâche, exécutant les conteneurs détaillés dans celle-ci. Plusieurs Tâches peuvent être créées par une seule Définition de Tâche, selon la demande.

![Image](https://cdn-media-1.freecodecamp.org/images/eL718lUcFCktxO96DKpdAIu1uBguoNqOKHRF)
_Une Définition de Tâche crée plusieurs Tâches identiques_

#### Service

Définir le nombre minimum et maximum de Tâches d'une seule Définition de Tâche exécutées à un moment donné, la mise à l'échelle automatique et l'équilibrage de charge. Dans notre exemple, si le CPU était à son maximum avec la seule tâche que nous avions en cours d'exécution, nous pourrions vouloir ajouter une Tâche supplémentaire.

Cependant, nous pourrions vouloir limiter le nombre maximum de Tâches qu'il peut exécuter, car nous savons que l'exécution de Tâches supplémentaires utilise des ressources supplémentaires qui coûtent de l'argent.

![Image](https://cdn-media-1.freecodecamp.org/images/Ff1BK5c7YRL7KAv71Hu7ZSwByYpeJPTaolzT)
_Définition du Service définissant les alarmes pour la mise à l'échelle de la capacité_

Maintenant que nous avons notre Service, ses Tâches doivent être exécutées quelque part pour être accessibles. Il doit être placé sur un **Cluster**, et le service de gestion de conteneurs gérera son exécution sur une ou plusieurs **Instances de Conteneur ECS**.

#### Instances de Conteneur ECS et Agents de Conteneur ECS

![Image](https://cdn-media-1.freecodecamp.org/images/1NSrmTZQxI3ErrpE9qMvTZkjYIZ9zS9BLZrJ)
_Une Instance de Conteneur ECS exécutant 8 Tâches de plusieurs Services différents_

Il s'agit d'une [instance EC2](http://AWS EC2 for Beginners) sur laquelle Docker et un Agent de Conteneur ECS sont en cours d'exécution. Une Instance de Conteneur peut exécuter de nombreuses Tâches, provenant du même Service ou de Services différents.

L'Agent prend en charge la communication entre ECS et l'instance, fournissant le statut des conteneurs en cours d'exécution et gérant l'exécution de nouveaux conteneurs.

#### Cluster

![Image](https://cdn-media-1.freecodecamp.org/images/scH1QJHgrQ6NgA1jQo9ITuCiQGkAawRHmzSc)
_Un exemple de cluster ECS, avec un Service exécutant quatre Tâches sur deux Instances de Conteneur ECS_

Comme le montre l'image ci-dessus, un Cluster est un groupe d'Instances de Conteneur ECS. Amazon ECS gère la logique de planification, de maintenance et de gestion des demandes de mise à l'échelle de ces instances. Il élimine également le travail de trouver l'emplacement optimal de chaque Tâche en fonction de vos besoins en CPU et en mémoire.

Un Cluster peut exécuter de nombreux Services. Si vous avez plusieurs applications dans le cadre de votre produit, vous pouvez souhaiter en mettre plusieurs sur un seul Cluster. Cela permet une utilisation plus efficace des ressources disponibles et minimise le temps de configuration.

![Image](https://cdn-media-1.freecodecamp.org/images/W3Xl8d3AHiLkuxV4ZdmvrqtPoFplOtp3hmcY)
_Multiples Services alloués sur plusieurs Instances de Conteneur ECS s'exécutant sur un Cluster_

### Conclusion

Nous avons vu comment une application Dockerisée peut être représentée par une **Définition de Tâche** qui a une relation un-à-un avec un **Service** qui, à son tour, l'utilise pour créer de nombreuses instances de **Tâche** différentes.

Ce **Service** est déployé sur un **Cluster** d'**Instances de Conteneur ECS** qui fournissent le pool de ressources nécessaires pour exécuter et mettre à l'échelle votre application. Des Services supplémentaires peuvent être déployés sur le même Cluster.

Amazon ECS, ou tout service de gestion de conteneurs, vise à rendre cela aussi simple que possible, en abstraisant de nombreuses complexités de l'exécution d'une infrastructure à grande échelle.

![Image](https://cdn-media-1.freecodecamp.org/images/wRtGhAtM8NLLnpTkp4PAUc80YHObxKVnFFhM)
_Un Cluster exécutant 3 Services, chacun exécutant un nombre différent de Tâches, sur deux Instances de Conteneur ECS_

À mesure que vos besoins deviennent plus complexes, le service de gestion de conteneurs garantit que cela reste gérable. En utilisant son API ou sa console de gestion, vous pouvez mettre en place des définitions pour ajouter de nouvelles Instances de Conteneur selon vos besoins. Cela garantit qu'il y a toujours un nombre sain de Tâches en cours d'exécution et alloue intelligemment les ressources entre les Services.

Merci d'avoir lu !

#### Ressources

* [Introduction en douceur au fonctionnement d'AWS ECS avec un tutoriel d'exemple](https://medium.com/boltops/gentle-introduction-to-how-aws-ecs-works-with-example-tutorial-cea3d27ce63d)
* [Déploiement d'applications Akka en cluster sur Amazon ECS](https://medium.com/@ukayani/deploying-clustered-akka-applications-on-amazon-ecs-fbcca762a44c)
* [Blocs de construction d'Amazon ECS](https://medium.com/containers-on-aws/building-blocks-of-amazon-ecs-db7fdfeeaa6f)
* [Introduction à Amazon EC2 Container Service (ECS) — Gestion Docker sur AWS](https://www.youtube.com/watch?v=zBqjh61QcB4)
* [Amazon ECS : Concepts de base](https://www.youtube.com/watch?v=eq4wL2MiNqo)
* [AWS EC2 pour débutants](https://hackernoon.com/aws-ec2-for-beginners-56df2e820d7f)
* [Une meilleure expérience Dev/Test : Docker et AWS](https://medium.com/aws-activate-startup-blog/a-better-dev-test-experience-docker-and-aws-291da5ab1238)
* [Architectures basées sur des clusters utilisant Docker et Amazon EC2 Container Service](https://medium.com/aws-activate-startup-blog/cluster-based-architectures-using-docker-and-amazon-ec2-container-service-f74fa86254bf)