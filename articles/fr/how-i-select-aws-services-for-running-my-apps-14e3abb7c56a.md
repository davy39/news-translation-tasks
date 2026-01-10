---
title: Comment je sélectionne les services AWS pour exécuter mes applications
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-23T16:20:23.000Z'
originalURL: https://freecodecamp.org/news/how-i-select-aws-services-for-running-my-apps-14e3abb7c56a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*q3V3mcHYJdMAoV_bkkQj8g.gif
tags:
- name: AWS
  slug: aws
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment je sélectionne les services AWS pour exécuter mes applications
seo_desc: 'By Peter Mbanugo

  Choosing which AWS service to use for running your application might be somewhat
  confusing to some of us. Even for the experienced, it may take some time to make
  a decision. Perhaps you are new to AWS, and you may still need to under...'
---

Par Peter Mbanugo

Choisir quel service AWS utiliser pour exécuter votre application peut être quelque peu déroutant pour certains d'entre nous. Même pour les expérimentés, cela peut prendre un certain temps pour prendre une décision. Peut-être êtes-vous nouveau sur AWS et devez encore comprendre le quoi et le pourquoi des différents services AWS. Ou peut-être savez-vous comment utiliser AWS, mais cela vous prend encore plus de temps parce que vous n'avez pas de processus pour faciliter une sélection facile. Laissez-moi vous montrer comment je fais cela et le processus que je suis.

### Un regard sur le processus

Lorsque vous sélectionnez le service à utiliser pour exécuter une application, essayez de répondre aux questions suivantes.

### Question 1 : De combien de contrôle ai-je besoin ?

En répondant à cette question, je décide ce que je veux contrôler par rapport à ce que je souhaite laisser à AWS.

Je choisis si je veux contrôler quel système d'exploitation (OS) il exécutera, comment le réseau est configuré, le serveur, le code de l'application et sa configuration.

Mais avec plus de contrôle vient une grande responsabilité. Par exemple, si je contrôle l'OS, je serai responsable de sa mise à jour, de sa sécurisation et de la configuration de ce qui est exposé au réseau public.

Les différentes options de cloud computing vous donnent du contrôle et de la responsabilité. Examinons ces options et ce que nous pouvons contrôler.

#### Option 1 : Infrastructure en tant que Service (IaaS) :

L'informatique IaaS vous offre le plus haut niveau de flexibilité et de contrôle de gestion sur vos ressources informatiques. Elle fournit un accès aux fonctionnalités de réseau, aux ordinateurs (virtuels ou sur matériel dédié) et à l'espace de stockage de données. Utilisez cette option si vous souhaitez contrôler les machines physiques exécutant votre application et gérer toutes les responsabilités pour les éléments suivants :

1. Configuration de l'application
2. Code de l'application
3. Maintenance et configuration du serveur
4. Système d'exploitation
5. Antivirus
6. Réseau

Les services disponibles en tant qu'IaaS sont :

1. Elastic Compute Cloud (EC2) Instances
2. Amazon Lightsail
3. EC2 Container Service (ECS)
4. Elastic Container Service pour Kubernetes (EKS)
5. AWS Batch

#### Option 2 : Plateforme en tant que Service (PaaS)

L'informatique PaaS élimine le besoin pour vous de gérer l'infrastructure sous-jacente (matériel, OS, réseau). Avec cela, vous vous concentrez sur la création et l'exécution d'applications, plutôt que sur la construction et la maintenance de l'infrastructure et des services sous-jacents. Utilisez cette option si vous souhaitez contrôler :

1. Configuration de l'application
2. Code de l'application
3. Configuration du serveur

tout en laissant d'autres responsabilités à AWS.

Les services disponibles en tant que PaaS sont :

1. Elastic Beanstalk
2. Mobile Hub

#### Option 3 : Fonctions en tant que Service (FaaS)

L'informatique FaaS vous offre la possibilité de déployer du code et de définir la configuration nécessaire pour exécuter le code. Vous laissez à AWS la gestion de l'infrastructure et du réseau sous-jacents. Utilisez cette option si vous souhaitez contrôler la logique et la configuration de votre application.

De plus, une autre raison importante de l'utiliser est si l'application s'exécutera occasionnellement. C'est-à-dire, pas toujours en marche et en cours d'exécution, contrairement aux applications dans les autres types d'offres de services cloud.

Les services disponibles dans cette catégorie sont :

1. Lambda
2. Step Functions

### Question 2 : Comment les utilisateurs utiliseront-ils l'application ?

Une autre question à considérer est de savoir comment les utilisateurs utiliseront l'application.

1. **Sera-t-elle toujours en marche et en cours d'exécution, en attente d'entrées/données à traiter ?** Même si aucune entrée/donnée/demande n'arrive, elle sera simplement inactive, consommant des ressources serveur et de l'infrastructure.
2. **S'exécutera-t-elle uniquement lorsque nécessaire ?** Dans ce cas, l'application démarre lorsqu'elle a une demande ou des données à traiter et s'arrête une fois terminée.

Si le modèle d'utilisation de mon application satisfait la question **1**, alors j'aurai besoin d'utiliser le modèle classique pour exécuter des applications. Je pourrais utiliser des instances EC2, ECS ou Elastic Beanstalk. Si elle satisfait la question **2**, je choisirai Lambda.

Parfois, nous voulons exécuter des tâches en arrière-plan. Elles varieront en fonction de leur durée d'exécution et des ressources dont elles auront besoin pour bien fonctionner. Confronté à ce problème, je choisirai entre l'utilisation de Lambda et Batch. Je choisirai Lambda si j'ai besoin qu'une tâche s'exécute dans le temps de traitement maximal autorisé qui ne nécessite pas plus de ressources que ce que Lambda peut fournir. Si c'est l'inverse, je choisirai Batch.

Ces deux questions m'aident dans mon processus de sélection d'un service dans AWS. Le tableau ci-dessous montre comment choisir en répondant à des questions plus spécifiques et en sachant quels services répondent aux critères.

#### Sélection d'un produit IaaS

![Image](https://cdn-media-1.freecodecamp.org/images/h62U5mxevaQkMn2X46D60gVvOk5cy4fjE3YJ)
_sélection des services IaaS_

#### Sélection d'un produit PaaS

![Image](https://cdn-media-1.freecodecamp.org/images/4oqXOGAm8OBOELjP5kMpvgot1g4tuACufMpK)
_sélection des services PaaS_

#### Sélection d'un produit FaaS

![Image](https://cdn-media-1.freecodecamp.org/images/7TjqbgkFajgcXK17OSfN4pSp4X2cVeSfnp-1)
_sélection des services FaaS_

Les étapes ci-dessus devraient vous guider et vous permettre de prendre vos décisions plus rapidement et facilement, alors j'espère que vous les avez trouvées utiles.

C'est mon processus, et il est susceptible de changer à l'avenir, mais j'essaierai de garder cet article à jour. J'ai omis certains services liés aux données/stockage, que je partagerai dans un futur article.

Veuillez laisser un commentaire si vous souhaitez partager vos pensées ou corriger quelque chose que vous pensez que j'ai mal compris. J'ai appris certaines de ces étapes de mon ami [Barry Luijbregts](https://twitter.com/AzureBarry).

> _Peter est un développeur de logiciels, rédacteur technique et créateur de Hamoni Sync. Il travaille actuellement avec Field Intelligence où il aide à construire des applications logistiques et de chaîne d'approvisionnement. Il participe également à la recherche en design et au support client pour ces produits. Il est également contributeur à Hoodie et membre de la communauté Offline-First._