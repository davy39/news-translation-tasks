---
title: Qu'est-ce que le monitoring ECS ? Explications avec des exemples
subtitle: ''
author: Chidiadi Anyanwu
co_authors: []
series: null
date: '2024-09-23T11:09:30.591Z'
originalURL: https://freecodecamp.org/news/ecs-monitoring-explained-with-examples
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727103254033/39d8dac3-4e18-46dc-8ad6-129386a165b3.avif
tags:
- name: AWS
  slug: aws
seo_title: Qu'est-ce que le monitoring ECS ? Explications avec des exemples
seo_desc: 'Amazon Elastic Container Service (ECS) is a container orchestration service
  provided by Amazon Web Services (AWS). It is a solution developed by AWS to take
  care of the problem of managing large clusters of containers.

  Why Use ECS?

  There are other co...'
---

Amazon Elastic Container Service (ECS) est un service d'orchestration de conteneurs fourni par Amazon Web Services (AWS). Il s'agit d'une solution développée par AWS pour répondre au problème de la gestion de grands clusters de conteneurs.

## Pourquoi utiliser ECS ?

Il existe d'autres outils d'orchestration de conteneurs, chacun avec ses mérites, mais ECS est conçu pour AWS et offre une intégration transparente dans l'écosystème AWS. Vous pouvez l'utiliser avec AWS Elastic Load Balancer (ELB), AWS Identity and Access Management (IAM), AWS CloudTrail, stocker des données persistantes dans AWS Elastic Block Store, ou le surveiller avec AWS CloudWatch.

Vous pouvez également l'utiliser avec AWS Fargate, qui est un moteur de calcul serverless fournissant des conteneurs entièrement gérés.

## **Qu'est-ce que le monitoring ?**

Le monitoring est le processus de suivi et d'observation de la performance, de la disponibilité et de la santé globale de vos ressources, services et applications. Cela aide à détecter et à dépanner les problèmes avant qu'ils n'impactent les utilisateurs, à améliorer la fiabilité et la disponibilité des applications, à optimiser l'utilisation des ressources et à renforcer la sécurité de vos applications.

C'est simplement un moyen de s'assurer que toute l'infrastructure fonctionne comme elle le devrait. Cela vous aide également à connaître le volume de trafic que votre application reçoit s'il s'agit d'une application web ou d'un site web, et ce qui s'y passe réellement.

Il existe différents aspects du monitoring, dont certains incluent :

*   **Monitoring de performance :** Ici, nous suivons et surveillons les métriques de performance de l'infrastructure, telles que l'utilisation du CPU, la consommation de mémoire, le disque, les E/S (I/O) et les réseaux, etc.
    
*   **Monitoring des erreurs et des logs :** Ici, nous collectons et analysons les journaux (logs) et les messages d'erreur.
    
*   **Monitoring de disponibilité :** Nous nous assurons que les systèmes sont opérationnels.
    
*   **Monitoring de sécurité :** Nous suivons et surveillons également les événements et activités liés à la sécurité pour répondre aux menaces et vulnérabilités potentielles. Le monitoring peut vous aider à détecter des éléments tels qu'une attaque DoS en identifiant des schémas inhabituels dans le trafic entrant.
    

## Que surveillez-vous sur ECS ?

Dans le monitoring cloud, les métriques sont utilisées pour surveiller la santé et la performance de l'infrastructure. Elles sont utilisées conjointement avec des dimensions. Les métriques sont les points de données collectés et surveillés pour mesurer la performance, la santé et l'utilisation de vos ressources et services cloud.

Les dimensions sont des attributs et des caractéristiques qui aident à filtrer, catégoriser et donner du contexte aux métriques. Elles sont représentées sous forme de paires clé/valeur.

Amazon ECS fournit diverses métriques pour la surveillance des ressources. En voici quelques-unes :

*   **CPUReservation :** Il s'agit du pourcentage d'unités CPU réservées par les tâches en cours d'exécution.
    
*   **MemoryReservation :** Pourcentage de mémoire réservée par les tâches en cours d'exécution.
    
*   **CPUUtilization :** Il s'agit du pourcentage d'unités CPU utilisées par les tâches en cours d'exécution.
    
*   **MemoryUtilization :** Il s'agit du pourcentage de mémoire utilisée par les tâches en cours d'exécution.
    
*   **ContainerInstances :** Il s'agit du nombre d'instances de conteneurs dans le cluster.
    
*   **RunningTasksCount :** Le nombre de tâches qui sont actuellement en cours d'exécution dans le cluster.
    

Amazon ECS fournit également des dimensions, dont certaines sont :

*   **ContainerName :** Le nom du conteneur.
    
*   **ClusterName :** Le nom du cluster ECS.
    
*   **ServiceName :** Le nom du service.
    
*   **ServiceNameSpace :** L'espace de noms utilisé pour regrouper un ensemble de services dans un cluster.
    
*   **InstanceType :** Cela fait référence au type d'instance EC2 utilisé. Par exemple : t2.micro, c4.large, r5.xlarge, etc.
    
*   **TaskID :** L'identifiant unique attribué à chaque tâche.
    

Dans AWS ECS, vous pouvez surveiller vos ressources à différents niveaux. Par exemple, au niveau du cluster, vous pouvez examiner des éléments tels que CPUUtilization, CPUReservation, MemoryUtilization et MemoryReservation. Au niveau du service, vous pouvez voir des éléments comme CPUUtilization et MemoryUtilization.

## Comment surveillez-vous ECS ?

Vous pouvez le faire en utilisant :

**Amazon CloudWatch :** Il s'agit d'un service de monitoring d'AWS qui vous permet de collecter, d'analyser et de visualiser les données de vos ressources AWS. Il vous aide également à configurer des alarmes et à être averti lorsqu'un seuil est atteint.

**Console de gestion AWS (AWS Management Console) :** Vous pouvez également consulter les métriques de votre cluster ou de votre service directement sur la console de gestion.

**L'API ECS :** L'API ECS fournit un accès programmatique au service ECS afin que vous puissiez l'utiliser pour créer, modifier et surveiller des clusters et des ressources depuis l'extérieur d'AWS.

**Outils tiers :** Il existe des outils tiers comme Datadog, Prometheus et d'autres qui peuvent être utilisés pour surveiller ces métriques. Certains d'entre eux fonctionneront de manière transparente avec AWS, d'autres nécessiteront l'installation d'un agent.

Pour le monitoring d'ECS sur des instances EC2, vous avez un accès direct aux instances EC2 sous-jacentes et pouvez utiliser des outils de monitoring de serveur traditionnels pour surveiller les métriques sur l'OS. Pour ECS sur Fargate, cependant, vous n'avez pas accès aux instances EC2.

### Comment surveiller les clusters ECS avec AWS CloudWatch

Avec AWS CloudWatch, vous pouvez surveiller vos clusters ECS de plusieurs manières, des métriques aux logs, en passant par la configuration d'alarmes. Dans ce guide, je vais vous montrer comment utiliser les Tableaux de bord automatiques (Automatic Dashboards) pour visualiser les métriques des clusters ECS. Pour ce faire, suivez ces étapes :

1. Depuis la Console de gestion AWS, ouvrez CloudWatch et allez dans Tableaux de bord (Dashboards) dans la barre latérale.
    

![Image du tableau de bord](https://cdn.hashnode.com/res/hashnode/image/upload/v1726955177185/348508ff-c765-4962-bb7a-d61fdb11f496.png align="center")

2. Cliquez sur l'onglet Tableaux de bord automatiques (Automatic Dashboards).
    

![Image du tableau de bord automatique](https://cdn.hashnode.com/res/hashnode/image/upload/v1726955263446/9fd7ffbb-e906-4db2-be57-f3dc85406a4b.png align="center")

3. Cliquez sur ECS Cluster. Cela vous mènera au tableau de bord où vous verrez les métriques pré-configurées pour vos clusters ECS.
    

![Cliquez sur le cluster ECS](https://cdn.hashnode.com/res/hashnode/image/upload/v1726955373129/cf2a20fa-06b3-4ead-a454-849bfb12bba1.png align="center")

![Tableau de bord du cluster ECS](https://cdn.hashnode.com/res/hashnode/image/upload/v1726955502141/12a0e538-8983-42be-825d-343ddf840625.png align="center")

Vous pouvez également agrandir les métriques individuelles.

![Métrique du nombre de tâches](https://cdn.hashnode.com/res/hashnode/image/upload/v1726955515843/eafca64b-fe22-4580-8243-8e55e3e92496.png align="center")

## **Conclusion**

Dans cet article, vous avez découvert le monitoring ECS. Vous avez appris les différentes métriques que vous pouvez surveiller et comment les suivre.

Enfin, vous avez appris à surveiller les clusters ECS à l'aide d'AWS CloudWatch.

Merci de m'avoir lu. Vous pouvez me contacter sur [LinkedIn](https://linkedin.com/in/chidiadi-anyanwu) ou me suivre sur [X](https://x.com/chidiadi01).