---
title: Qu'est-ce qu'Amazon EC2 Auto Scaling ?
subtitle: ''
author: Destiny Erhabor
co_authors: []
series: null
date: '2024-05-06T16:32:47.000Z'
originalURL: https://freecodecamp.org/news/what-is-amazon-ec2-auto-scaling
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/christophe-hautier-902vnYeoWS4-unsplash.jpg
tags:
- name: Amazon
  slug: amazon
- name: ec2
  slug: ec2
- name: scaling
  slug: scaling
seo_title: Qu'est-ce qu'Amazon EC2 Auto Scaling ?
seo_desc: Auto scaling is like having a smart system that keeps an eye on how many
  people are visiting your website. When you have a lot of people, it quickly adds
  more servers to handle the extra traffic. And when things quiet down, it scales
  back to save you...
---

L'auto scaling est comme avoir un système intelligent qui surveille le nombre de personnes visitant votre site web. Lorsqu'il y a beaucoup de monde, il ajoute rapidement plus de serveurs pour gérer le trafic supplémentaire. Et lorsque les choses se calment, il réduit l'échelle pour vous faire économiser de l'argent.

Dans AWS, il existe deux services importants qui aident à cela : Amazon EC2 Auto Scaling et AWS Auto Scaling. Amazon EC2 Auto Scaling est spécifiquement pour gérer vos serveurs EC2, tandis qu'AWS Auto Scaling peut également gérer d'autres choses comme les tables DynamoDB et les bases de données Amazon Aurora.

Dans cet article, nous allons approfondir le fonctionnement d'Amazon EC2 Auto Scaling et comment vous pouvez l'utiliser pour garder votre site web en fonctionnement fluide sans dépenser trop pour les serveurs.

## Prérequis

* Avoir un compte AWS
* Compréhension de base des instances EC2

## Table des matières

* [Prérequis](#heading-prerequisites)
* [Exemple de cas d'utilisation](#heading-example-use-case)
* [Avantages d'Amazon EC2 Auto Scaling](#advantages-of-amazon-ec2-auto-scaling)
* [Composants d'EC2 Auto Scaling](#heading-components-of-ec2-auto-scaling)
* [Qu'est-ce que les configurations de lancement vs les modèles de lancement](#what-is-launch-configurations-vs-launch-templates)
* [Comment créer un modèle de lancement](#heading-how-to-create-a-launch-template)
* [Qu'est-ce que les groupes Auto Scaling (ASGs)](#heading-what-are-auto-scaling-groups-asgs)
* [Comment créer un groupe Auto Scaling](#heading-how-to-create-an-auto-scaling-group)
* [Qu'est-ce que les politiques de mise à l'échelle](#heading-what-are-scaling-policies)
* [Conclusion](#heading-conclusion)

## Exemple de cas d'utilisation

### Scénario :

Imaginez que vous gérez un site web qui vend des vêtements à la mode. Parfois, beaucoup de personnes visitent votre site en même temps, surtout pendant les pauses déjeuner ou les soirées. À d'autres moments, c'est assez calme.

### Problème :

Vous avez besoin de suffisamment de serveurs pour gérer les périodes chargées, mais vous ne voulez pas gaspiller de l'argent avec trop de serveurs lorsque c'est calme.

### Solution avec Amazon EC2 Auto Scaling :

**Analyse du trafic** : Regardez quand les gens visitent votre site le plus. Cela vous aide à comprendre quand vous avez besoin de plus de serveurs.

**Définir des règles** : Décidez quand ajouter ou supprimer des serveurs automatiquement. Par exemple, vous pourriez dire : "Si plus de 70 % de nos serveurs sont occupés pendant plus de 5 minutes, ajoutez un serveur supplémentaire."

**Ajuster le nombre de serveurs** : Dites à Amazon le nombre minimal et maximal de serveurs dont vous avez besoin. Vous pouvez également indiquer combien vous aimeriez en moyenne. Par exemple, vous pourriez dire : "Gardez au moins 2 serveurs en fonctionnement tout le temps. Mais s'il y a du monde, montez jusqu'à 10 serveurs. Et habituellement, nous en avons besoin d'environ 4."

**Équilibrage de charge** : Assurez-vous que tous les serveurs reçoivent du travail. Utilisez un équilibreur de charge pour envoyer les visiteurs vers le serveur le moins occupé. Cela maintient tout en fonctionnement fluide même si vous avez de nombreux serveurs.

**Test et surveillance** : Avant de tout faire confiance, testez pour voir si cela fonctionne comme prévu. Gardez un œil dessus ensuite pour vous assurer qu'il fait bien son travail.

**Économies** : Avec l'auto scaling, vous ne payez pas pour les serveurs que vous n'utilisez pas. Lorsque le trafic est faible, il réduit le nombre de serveurs, vous faisant économiser de l'argent. Lorsque le trafic augmente, il ajoute plus de serveurs, afin que votre site reste rapide.

## Avantages de l'utilisation d'Amazon EC2 Auto Scaling

**Optimisation des coûts** : EC2 Auto Scaling aide à optimiser les coûts en ajustant automatiquement le nombre d'instances EC2 en fonction de la demande. Pendant les périodes de faible trafic, il réduit le nombre d'instances, économisant ainsi les coûts opérationnels. Inversement, pendant les périodes de fort trafic, il augmente l'échelle pour garantir des performances optimales sans sur-provisionner les ressources.

**Disponibilité améliorée** : En distribuant automatiquement le trafic entrant sur plusieurs instances et en assurant la tolérance aux pannes de votre application. Si une instance tombe en panne/est malsaine, le groupe Auto Scaling la remplace par une nouvelle, garantissant ainsi une perturbation minimale de vos services.

**Évolutivité** : EC2 Auto Scaling permet à votre application de gérer les pics soudains de trafic ou l'augmentation de la charge de travail sans intervention manuelle.

**Performance améliorée** : Avec EC2 Auto Scaling, vous pouvez maintenir des niveaux de performance constants même pendant les périodes de pointe. En ajoutant automatiquement plus d'instances lorsque le trafic augmente, il empêche la dégradation des performances et garantit une expérience utilisateur fluide.

**Facilité de gestion** : EC2 Auto Scaling simplifie la gestion de votre flotte EC2 en automatisant le provisionnement, la mise à l'échelle et la surveillance des instances.

**Intégration avec les services AWS** : EC2 Auto Scaling s'intègre parfaitement avec d'autres services AWS tels que Elastic Load Balancing (ELB) et Amazon CloudWatch.

**Hautement personnalisable** : EC2 Auto Scaling offre des options de flexibilité et de personnalisation pour répondre aux besoins spécifiques de votre application.

## Composants d'EC2 Auto Scaling

Comprenons mieux comment fonctionne l'Auto Scaling à travers ses différents composants.

Il y a deux étapes distinctes pour la configuration. La première étape est la création d'une configuration de lancement ou d'un modèle de lancement. La seconde est la création d'un groupe Auto Scaling.

## Configurations de lancement et modèles de lancement

Les configurations de lancement ou les modèles de lancement définissent les paramètres de configuration pour les instances EC2 qui seront lancées par le groupe Auto Scaling.

Ces paramètres incluent l'AMI (Amazon Machine Image), le type d'instance, les groupes de sécurité, la paire de clés et les données utilisateur.

Les configurations de lancement sont plus anciennes et sont progressivement remplacées par les modèles de lancement, qui offrent plus de fonctionnalités et de flexibilité.

### Comment créer un modèle de lancement

Tout d'abord, naviguez vers la page des instances EC2

![Page des instances AWS](https://www.freecodecamp.org/news/content/images/2024/05/launch-template-1.png)
_Page des instances AWS_

Sélectionnez les modèles de lancement sous les instances et cliquez sur le bouton créer.

![Modèles de lancement AWS](https://www.freecodecamp.org/news/content/images/2024/05/launch-template-2.png)
_Modèles de lancement AWS_

L'écran suivant devrait apparaître, presque similaire au lancement d'une `instance EC2`. Vous pouvez remplir les informations requises en conséquence.

![Créer des modèles de lancement AWS](https://www.freecodecamp.org/news/content/images/2024/05/screencapture-us-east-1-console-aws-amazon-ec2-home-2024-05-03-22_52_38-1.png)
_Créer des modèles de lancement AWS_

Après la configuration, cliquez sur le bouton "Créer un modèle de lancement" et laissez-le créer, puis affichez votre nouveau modèle de lancement avec la version par défaut et la plus récente comme 1. Vous pouvez utiliser ce modèle de lancement pour créer un autre modèle de lancement et spécifier une version différente pour celui-ci.

![Voir les modèles de lancement AWS](https://www.freecodecamp.org/news/content/images/2024/05/launch-template-3-1.png)
_Voir les modèles de lancement AWS_

L'auto scaling nécessite soit un modèle de lancement, soit une configuration de lancement pour identifier l'instance qu'il lance et ses configurations.

## Qu'est-ce que les groupes Auto Scaling (ASGs)

Les groupes Auto Scaling sont le composant central d'EC2 Auto Scaling. Ils définissent le groupe d'instances EC2 qui sont gérées ensemble et partagent les mêmes politiques de mise à l'échelle. Les ASGs garantissent que votre application peut automatiquement augmenter (ajouter des instances) ou réduire (supprimer des instances) en fonction de la demande.

### Comment créer un groupe Auto Scaling

Tout d'abord, naviguez vers la page des instances EC2 et sous le groupe Auto Scaling, sélectionnez et cliquez sur le bouton créer.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/asg-1.png)
_création d'un groupe Auto Scaling_

Sur l'écran de création, la première étape consiste à donner à votre ASG un `Nom` puis à sélectionner votre `modèle de lancement` créé à partir des étapes ci-dessus.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/asg-2.png)
_création d'un modèle de lancement_

L'étape suivante nécessite de sélectionner ou de remplacer un modèle de lancement d'instance. Vous sélectionnez également un VPC et un sous-réseau.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/asg-3.png)
_sélection du modèle de lancement d'instance_

L'étape suivante consiste à configurer des options avancées telles que l'ajout d'un équilibreur de charge et la surveillance. Vous pouvez attacher ou ajouter un nouvel équilibreur de charge, mais pour cet article, nous allons sauter cette partie.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/asg-4.png)
_configuration des options avancées_

Ensuite, configurez la taille du groupe et la mise à l'échelle. Ici, nous voulons configurer l'échelle entre un minimum de 2 et un maximum de 5. Définissez également le type de métriques pour suivre l'utilisation du CPU (réglé à 50 – vous pouvez augmenter à 70 ou plus) pour la mise à l'échelle.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/screencapture-us-east-1-console-aws-amazon-ec2-home-2024-05-03-23_41_58.png)
_configuration de la taille du groupe et de la mise à l'échelle_

Les deux étapes suivantes consistent à ajouter des notifications (vous devrez créer un service SNS pour cela) et des tags. Dans cet article, nous allons sauter ces étapes et créer notre ASG.

Créez et affichez l'ASG créé. À partir de son dossier **activité**, vous pouvez voir ces deux instances lancées. De plus, à partir de la page des instances, vous devriez voir deux instances EC2. Cela est dû au fait que nous avons défini notre état souhaité à 2.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/asg-5.png)
_Groupes Auto Scaling_

![Image](https://www.freecodecamp.org/news/content/images/2024/05/asg-6.png)
_Groupes Auto Scaling_

## Qu'est-ce que les politiques de mise à l'échelle ?

Les politiques de mise à l'échelle définissent les règles qui régissent la manière dont le groupe Auto Scaling augmente ou réduit en réponse à l'évolution de la demande. Il existe quatre types de politiques de mise à l'échelle :

Décortiquons chaque type de mise à l'échelle avec des exemples :

### Mise à l'échelle manuelle

La mise à l'échelle manuelle implique l'ajustement du nombre d'instances EC2 dans votre groupe Auto Scaling manuellement, sans dépendre de déclencheurs ou de politiques automatisées. Ce type de mise à l'échelle est généralement effectué en réponse à des événements prévisibles ou à des changements planifiés de la demande.

**Exemple** : Supposons que vous gérez un site web de commerce électronique, et vous savez qu'il y aura un événement de vente flash qui attirera un grand nombre de visiteurs. Pour gérer l'afflux attendu de trafic, vous pouvez augmenter manuellement la capacité souhaitée de votre groupe Auto Scaling avant l'événement, en ajoutant plus d'instances EC2 à l'avance de la pointe de demande anticipée. Après l'événement, vous pouvez réduire manuellement la capacité souhaitée à son niveau normal.

##### Avantages :

* **Contrôle** : Offre un contrôle direct sur le nombre d'instances EC2 dans le groupe Auto Scaling.
* **Flexibilité** : Permet des ajustements immédiats en fonction de exigences ou d'événements spécifiques.

##### Inconvénients :

* **Intervention manuelle** : Dépend de l'intervention humaine, ce qui peut être chronophage et sujet aux erreurs.
* **Manque d'automatisation** : Ne convient pas pour gérer efficacement les fluctuations dynamiques ou imprévisibles de la demande.

### Mise à l'échelle planifiée

La mise à l'échelle planifiée implique la définition de plannings prédéfinis pour ajuster le nombre d'instances EC2 dans votre groupe Auto Scaling automatiquement. Ce type de mise à l'échelle est utile pour les applications avec des schémas de trafic prévisibles, tels que les fluctuations quotidiennes ou hebdomadaires de la demande.

**Exemple** : Considérez un service de streaming vidéo qui connaît un pic de trafic le soir et les week-ends. Vous pouvez configurer une politique de mise à l'échelle planifiée pour augmenter la capacité souhaitée de votre groupe Auto Scaling chaque soir à 18h et la réduire chaque matin à 6h. Cela garantit que vous avez suffisamment de capacité pour gérer les périodes de pointe sans surpayer les ressources pendant les heures creuses.

##### Avantages :

* **Prévisibilité** : Bien adapté aux applications avec des schémas de trafic prévisibles, tels que les fluctuations quotidiennes ou hebdomadaires.
* **Optimisation des coûts** : Aide à optimiser les coûts en alignant les ressources avec les schémas de demande attendus.

##### Inconvénients :

* **Adaptabilité limitée** : Peut ne pas être réactif aux changements soudains de la demande ou aux pics de trafic inattendus.
* **Nécessite une planification** : Nécessite une planification et une configuration préalables des plannings basés sur des données historiques ou des informations commerciales.

### Mise à l'échelle dynamique

La mise à l'échelle dynamique ajuste le nombre d'instances EC2 dans votre groupe Auto Scaling automatiquement en fonction de métriques en temps réel, telles que l'utilisation du CPU, le trafic réseau ou d'autres métriques spécifiques à l'application. Ce type de mise à l'échelle est réactif aux fluctuations de la demande et aide à garantir des performances optimales et une rentabilité.

##### Types :

* **Mise à l'échelle par étapes** : Cette politique met à l'échelle le nombre d'instances en fonction d'une série d'ajustements de mise à l'échelle définis par des ajustements par étapes et des seuils de métriques associés.
* **Suivi de cible** : Cette politique ajuste automatiquement le nombre d'instances pour maintenir une métrique cible spécifiée, telle que l'utilisation moyenne du CPU ou le trafic réseau.

Lors de l'ajout d'instances à l'ASG, cela prendra quelques minutes pour qu'elles soient en ligne et gèrent la charge. C'est pourquoi une politique de refroidissement doit être définie.

**Périodes de refroidissement de mise à l'échelle** : Les périodes de refroidissement de mise à l'échelle aident à prévenir les fluctuations rapides du nombre d'instances en imposant une période de refroidissement après qu'une activité de mise à l'échelle est déclenchée. Pendant cette période de refroidissement, EC2 Auto Scaling ne lancera ni ne terminera d'instances supplémentaires, permettant aux instances nouvellement lancées de se stabiliser ou à l'impact des instances terminées d'être observé.

**Exemple** : Supposons que vous exploitez une plateforme de covoiturage où la demande peut varier de manière imprévisible tout au long de la journée. Avec la mise à l'échelle dynamique, vous pouvez configurer des politiques Auto Scaling pour ajouter plus d'instances EC2 lorsque le nombre de demandes de trajet dépasse un certain seuil, et supprimer des instances lorsque la demande diminue. Cela vous permet de vous adapter dynamiquement aux schémas de trafic changeants en temps réel, garantissant une expérience fluide pour les conducteurs et les passagers.

##### Avantages :

* **Réactivité en temps réel** : Ajuste l'allocation des ressources dynamiquement en réponse à la demande réelle, garantissant des performances optimales.
* **Efficacité des coûts** : Met automatiquement à l'échelle les ressources vers le haut ou vers le bas, aidant à optimiser les coûts en n'utilisant que ce qui est nécessaire.

##### Inconvénients :

* **Sur-provisionnement potentiel** : Peut conduire à un sur-provisionnement pendant les pics soudains de demande si les politiques de mise à l'échelle ne sont pas correctement configurées.
* **Complexité** : Nécessite une configuration minutieuse des politiques de mise à l'échelle et une surveillance des métriques pour garantir un comportement de mise à l'échelle efficace.

### Mise à l'échelle prédictive

La mise à l'échelle prédictive utilise des algorithmes d'apprentissage automatique et des données historiques pour prévoir la demande future et ajuster proactivement le nombre d'instances EC2 dans votre groupe Auto Scaling. Ce type de mise à l'échelle aide à prévenir le sous-provisionnement ou le sur-provisionnement des ressources en anticipant les changements de demande avant qu'ils ne se produisent.

**Exemple** : Supposons que vous exploitez une application de prévision météorologique qui connaît une demande accrue pendant les événements météorologiques sévères. En analysant les données historiques sur les schémas météorologiques et le comportement des utilisateurs, la mise à l'échelle prédictive peut prédire quand une augmentation du trafic est susceptible de se produire et mettre automatiquement à l'échelle la capacité de votre groupe Auto Scaling à l'avance. Cela garantit que votre application reste réactive et disponible pendant les périodes de pointe sans gaspillage inutile de ressources.

##### Avantages :

* **Optimisation proactive** : Anticipe la demande future en fonction des données historiques, garantissant que les ressources sont provisionnées à l'avance.
* **Gestion des coûts améliorée** : Aide à prévenir le sous-provisionnement et le sur-provisionnement, optimisant l'utilisation des ressources et les coûts.

#### Inconvénients :

* **Dépendance aux données** : Dépend de données historiques précises et de modèles d'apprentissage automatique efficaces pour des prédictions précises.
* **Configuration initiale** : Nécessite une configuration initiale et une configuration des modèles de mise à l'échelle prédictive, ce qui peut être complexe et consommer des ressources.

## Conclusion

En conclusion, Amazon EC2 Auto Scaling offre une gamme de stratégies pour gérer et optimiser efficacement les performances des applications s'exécutant sur des instances EC2.

Qu'il s'agisse d'ajustements manuels, de mise à l'échelle planifiée, de réponses dynamiques aux métriques en temps réel ou de mesures proactives basées sur l'analyse prédictive, EC2 Auto Scaling fournit la flexibilité et l'automatisation nécessaires pour garantir que les ressources sont alignées sur la demande.

En tirant parti de ces capacités de mise à l'échelle, les entreprises peuvent améliorer la disponibilité, optimiser l'efficacité des coûts et offrir une expérience utilisateur fluide, conduisant finalement à de meilleurs résultats pour leurs applications et clients sur la plateforme AWS.

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/destiny-erhabor) ou [Twitter](https://twitter.com/caesar_sage).