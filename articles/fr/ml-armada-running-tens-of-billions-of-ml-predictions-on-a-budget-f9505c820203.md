---
title: Comment créer une Armada ML et exécuter des milliards de prédictions ML avec
  un budget limité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-09T02:03:50.000Z'
originalURL: https://freecodecamp.org/news/ml-armada-running-tens-of-billions-of-ml-predictions-on-a-budget-f9505c820203
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Q0NBrOiL1bfHO5NekJzQLA.jpeg
tags:
- name: AWS
  slug: aws
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer une Armada ML et exécuter des milliards de prédictions ML
  avec un budget limité
seo_desc: 'By Marcelo Lotif

  In this guide, we will go through a step-by-step process on how to set up AWS’s
  SpotFleet with Docker containers configured to run Tensorflow and Keras applications.

  Docker makes it very easy to install Tensorflow and Keras and to re...'
---

Par Marcelo Lotif

Dans ce guide, nous allons passer par un processus étape par étape sur la façon de configurer [AWS SpotFleet](https://aws.amazon.com/blogs/compute/powering-your-amazon-ecs-clusters-with-spot-fleet/) avec des conteneurs Docker configurés pour exécuter des applications Tensorflow et Keras.

Docker facilite grandement l'installation de Tensorflow et Keras et permet de reproduire cette installation de manière fiable à plusieurs reprises sur différentes machines. En même temps, SpotFleet est un excellent outil pour démarrer un certain nombre de machines tout en tirant parti des économies réalisées avec [les instances spot d'AWS](https://aws.amazon.com/ec2/spot/). En combinant ces deux éléments, vous obtenez une combinaison gagnante de puissance de traitement puissante et économique.

La configuration décrite ici a été conçue pour être réalisée à partir de zéro et pour vous mettre en route rapidement sans configurations complexes — juste le strict minimum pour commencer sans tomber dans les pièges courants.

Ce sera donc une explication détaillée mais simple sur la façon d'assembler toutes les pièces. Je m'attends à ce que vous connaissiez la configuration de base d'AWS et que vous soyez à l'aise avec la ligne de commande. Cependant, si l'une des sections ci-dessous vous est déjà familière, vous pouvez les sauter en utilisant ces liens :

1. [Création d'une image Docker compatible Tensorflow+Keras](#heading-installation)
2. [Pousser votre image docker vers AWS et créer des définitions de tâches](#heading-pousser-image)
3. [Demander un SpotFleet](#heading-demander-spotfleet)
4. [Configurer votre cluster ECS pour exécuter des conteneurs Docker sur des machines SpotFleet](#heading-configurer-ecs)
5. [Application réelle et résultats](#heading-application-reelle)

La dernière section explique comment cette configuration nous aide à exécuter des milliards de prédictions nécessaires pour l'un de nos backfills dans l'entreprise pour laquelle je travaille (non divulguée pour l'instant) — et nous fait économiser de l'argent par rapport à d'autres solutions prêtes à l'emploi sur le marché.

### 1. Création d'une image Docker compatible Tensorflow+Keras

Nous allons commencer par [tirer parti du travail effectué par l'équipe tensorflow](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/docker/README.md) en utilisant l'une des [images Docker publiques tensorflow/tensorflow](https://hub.docker.com/r/tensorflow/tensorflow/) pour construire notre propre image.

Tout d'abord, clonez le [projet hello world Keras/Docker](https://github.com/lotif/keras-docker-hello-world) que j'ai créé pour nous aider à démarrer :

```
$ git clone https://github.com/lotif/keras-docker-hello-world.git
```

**Note :** J'ai essayé de faire le strict minimum dont vous aurez besoin pour construire une image Docker qui entraîne un modèle d'exemple. Pour créer le fichier `hello_world.py`, j'ai utilisé [ce tutoriel](https://elitedatascience.com/keras-tutorial-deep-learning-in-python) avec quelques modifications mineures pour le faire fonctionner avec Keras 2.

Je n'entre pas dans les détails sur la façon de configurer tout cela, mais si vous avez des questions, n'hésitez pas à demander — soit ici, soit dans le dépôt Github.

Deuxièmement, [installez Docker sur votre machine locale](https://docs.docker.com/install/) si vous ne l'avez pas déjà fait, et construisez l'image localement :

```
$ docker build -t hello-world .
```

Une fois terminé, vous devriez voir des logs comme ceux-ci à la fin :

```
[...]Successfully built 3841f29fa5b9Successfully tagged hello-world:latest
```

Maintenant, il est temps de le tester :

```
$ docker run hello-world:latest
```

Tout le plaisir va maintenant commencer — le modèle va être construit et il devrait commencer à s'entraîner. Il va s'exécuter pendant quelques minutes, et lorsqu'il aura terminé, il produira des messages de log comme ceux-ci :

```
[...]Epoch 9/1060000/60000 [===============] - 12s - loss: 0.1022 - acc: 0.9679     Epoch 10/1060000/60000 [===============] - 12s - loss: 0.0991 - acc: 0.9695#############################Score: [0.06286391887611244, 0.9799]Training Finished! Exiting...
```

Super ! Maintenant, nous avons une image Docker fonctionnelle qui entraîne un modèle. Il est temps de la mettre dans le cloud :)

### 2. Pousser votre image docker vers AWS et créer des définitions de tâches

Vous devriez [installer la ligne de commande AWS sur votre machine locale](https://docs.aws.amazon.com/cli/latest/userguide/installing.html) et suivre essentiellement [ce guide AWS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html#use-ecr) avec un changement important :

* Dans la partie [prochaines étapes](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html#docker_next_steps), j'ai simplifié le JSON pour qu'il ressemble au code ci-dessous. Assurez-vous de remplacer `<aws-account-id>` par votre identifiant de compte AWS avant de l'exécuter.

De plus, ne vous inquiétez pas de l'étape « **Pour exécuter une tâche avec la définition de tâche `hello-world`** » pour l'instant. Nous allons configurer ECS plus tard.

Il y a deux modifications principales. Premièrement, il y a la suppression de certaines configurations dont nous n'aurons pas besoin pour l'instant. Deuxièmement, nous allons utiliser l'attribut `memoryReservation` au lieu de `memory`. Ainsi, votre conteneur ne plantera pas s'il dépasse la limite de mémoire. Troisièmement, il y a l'attribut `command` qui a été emprunté au _Dockerfile_. Vous pouvez modifier cela comme vous le jugez approprié pour votre projet.

Vous pouvez vérifier à quoi ressemble votre définition de tâche en allant dans la section [définitions de tâches d'ECS](https://console.aws.amazon.com/ecs/home?region=us-east-1#/taskDefinitions) sur AWS.

Maintenant, nous sommes prêts à configurer notre flotte !

### 3. Demander un SpotFleet

J'ai élaboré un JSON simplifié pour vous aider à démarrer, mais l'interface utilisateur pour les demandes Spot n'est pas mauvaise si vous préférez l'utiliser. Des instructions rapides pour cela se trouvent à la fin de cette section.

Je préfère personnellement l'approche JSON, car elle est facilement documentable et versionnable, ainsi que plus rapide et plus flexible. Il y a aussi des choses que vous ne pouvez pas faire en utilisant l'interface utilisateur, comme [la pondération des instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html#spot-instance-weighting). Vous pouvez consulter les [documents de référence AWS](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotFleetRequestConfigData.html) pour les spécifications complètes de son schéma.

Les configurations de la flotte peuvent être modifiées comme vous le souhaitez. Cependant, il y a quelques choses que vous devez faire pour qu'elle fonctionne correctement avec les clusters ECS :

1. **AMI :** il doit s'agir de l'un des identifiants AMI optimisés pour ECS dans [cette liste](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html). Choisissez celui de la zone dans laquelle vous créez la flotte.
2. **Paire de clés :** le nom d'une paire de clés AWS que vous possédez afin de pouvoir vous connecter en _ssh_ aux instances si vous devez vérifier les logs Docker ou déboguer quoi que ce soit. Si vous n'en avez pas encore, vous pouvez aller dans [Paires de clés sur EC2](https://console.aws.amazon.com/ec2/v2/home#KeyPairs) et cliquer sur **Créer une paire de clés**.
3. **Rôle IAM de la flotte :** attribuez un rôle IAM pour le service EC2 avec la politique `AmazonEC2SpotFleetRole`. Vous devrez peut-être en créer un nouveau pour cela.
4. **Profil d'instance IAM :** attribuez un rôle IAM pour le service EC2 avec la politique `AmazonEC2ContainerServiceforEC2Role`. Vous devrez peut-être en créer un nouveau pour cela.

Placez ces valeurs dans les espaces réservés du fichier ci-dessous pour obtenir la demande finale de flotte spot en JSON :

Avec le fichier final en main, vous pouvez maintenant exécuter la commande `request-spot-fleet` ci-dessous (spécifications complètes [ici](https://docs.aws.amazon.com/cli/latest/reference/ec2/request-spot-fleet.html)) et elle demandera la flotte pour vous :

> **Attention :** cette commande demandera réellement des instances EC2 si elle trouve des machines moins chères que le prix de l'offre spot, ce qu'elle fera probablement étant donné les configurations.

```
$ aws ec2 request-spot-fleet --spot-fleet-request-config file:///path/to/spot-fleet-config.json
```

Vous avez terminé ! Vous devriez maintenant pouvoir accéder à la page [Demandes Spot EC2](https://console.aws.amazon.com/ec2sp/v1/spot/home) et voir votre flotte là-bas. Il est également possible de vérifier l'état et d'arrêter la flotte à partir de là.

Vous pouvez ajouter autant de types d'instances que vous le souhaitez dans la liste `LaunchSpecifications`. Puisque nous avons défini la stratégie d'allocation sur `lowestPrice`, SpotFleet va demander des instances pour le type le moins cher en fonction des prix spot actuels.

Pour faire cela via l'interface utilisateur, [accédez à la page Demandes Spot](https://console.aws.amazon.com/ec2sp/v1/spot/home) et cliquez sur le bouton **Demander des instances Spot**. Ensuite, cliquez sur **Demander et maintenir**, et vous devriez pouvoir demander une flotte spot. N'oubliez pas de changer les quatre mêmes éléments que j'ai mentionnés ci-dessus, sinon elle ne pourra pas rejoindre un cluster ECS.

### 4. Configurer votre cluster ECS pour exécuter des conteneurs Docker sur des machines SpotFleet

En créant une flotte avec les configurations ci-dessus, vous allez également permettre de créer un cluster par défaut pour vous sur ECS et d'assigner les instances de la flotte à celui-ci. Vous pouvez maintenant accéder à la [page des clusters ECS](https://console.aws.amazon.com/ecs/home?#/clusters), et vous devriez pouvoir voir ce cluster par défaut et le gérer.

Dans la page du cluster par défaut, il y a un onglet appelé **Instances ECS** où vous devriez pouvoir voir les instances de la flotte que vous venez de démarrer. Elles sont actuellement en cours d'exécution à vide.

Maintenant, il est temps de faire faire le travail aux machines ! Pour cela, un service ECS doit être créé afin qu'il puisse automatiquement assigner des tâches Docker à ces machines et commencer à les exécuter.

Pour cela, utilisez la commande `create-service` (spécifications complètes [ici](https://docs.aws.amazon.com/cli/latest/reference/ecs/create-service.html)) :

```
aws ecs create-service --service-name hello-world-service --cluster default --task-definition hello-world-task-def --desired-count 4
```

Maintenant, vous devriez pouvoir accéder à l'onglet **Services** de votre cluster et voir votre service nouvellement créé là.

Vous avez peut-être remarqué que j'ai défini le nombre souhaité dans la commande ci-dessus à 4. Vous avez peut-être également remarqué que j'ai défini la capacité cible de la flotte à 2. Si vous lui donnez quelques minutes, ce service va automatiquement répartir ces tâches sur les instances, en démarrant 2 conteneurs Docker sur chacune d'entre elles. Super, n'est-ce pas ?

Vous pouvez personnaliser ce comportement en changeant le paramètre `--placement-strategy` dans la commande `create-service`.

Les conteneurs Docker vont démarrer et exécuter la commande dans la définition de la tâche. Lorsqu'elle est terminée, la tâche s'arrête et le service en démarre une autre pour tout recommencer, en essayant toujours de maintenir son compte de 4 tâches en cours d'exécution.

Pour voir les logs et vérifier si les conteneurs Docker s'exécutent correctement, vous devez vous connecter en _ssh_ aux machines, faire un `docker container ls`, récupérer le numéro de hachage de votre conteneur, et faire un `docker logs <container-hash>`. Mais cela n'est pas scalable pour un grand nombre de machines. La consolidation de tous les logs dont nous avons besoin pourrait faire l'objet d'un autre article :)

Il y a beaucoup d'autres configurations que vous pouvez faire sur les services, y compris la stratégie d'allocation, les vérifications de santé et l'autoscaling. Vous devriez ajuster celles-ci en fonction de vos besoins.

### 5. Application réelle et résultats

Maintenant, je vais présenter notre raisonnement pour cette solution, et comment elle aide à résoudre les problèmes les plus pressants de mon entreprise pour adopter le Machine Learning à grande échelle dans notre application.

#### Pourquoi SpotFleet ?

[Les instances spot d'AWS](https://aws.amazon.com/ec2/spot/) sont un outil merveilleux. Ce sont des machines qui sont simplement inactives, et AWS les propose pour seulement [une fraction du prix complet](https://aws.amazon.com/ec2/spot/pricing/).

Si vous travaillez avec le Machine Learning, vous avez probablement réalisé que certaines choses prennent simplement trop de temps à s'exécuter. L'entraînement de modèles de Machine Learning est un processus très intensif en ressources pour des ensembles de données réels composés de centaines de milliers à des millions d'échantillons d'entraînement.

Un autre point de douleur bien connu est le backfilling. Lorsque vous avez un très grand ensemble de données, même essayer d'exécuter quelques prédictions pour chacun des points de données devient une entreprise majeure.

Pour terminer tout cela dans un délai raisonnable (lire : pendant que vous êtes encore en vie) et sans faire un trou énorme dans les finances de votre entreprise, vous avez besoin de beaucoup de puissance de traitement bon marché. SpotFleet offre un moyen de démarrer de nombreuses instances spot et des conteneurs Docker de manière transparente pour les faire faire tout ce dont vous avez besoin avec une parallélisation maximale pour une fraction du coût complet.

#### Améliorations réelles

Après avoir exécuté quelques benchmarks pour notre backfill, nous avons décidé d'opter pour une machine capable de faire un peu plus de 1000 prédictions par minute pour des raisons de rapport coût-bénéfice. Il nous en coûterait 1,42 $ pour exécuter un million de prédictions sur cette machine si nous utilisons les prix AWS réguliers.

Cela semble correct, mais en utilisant les prix spot, ce même nombre de prédictions ne nous coûterait que 0,50 $ ! Des économies assez impressionnantes.

Un autre problème est le temps. Nous devons effectuer des dizaines de milliards de prédictions, et une seule de ces machines prendrait des décennies pour tout terminer. Pas bon.

Mais avec SpotFleet, nous pouvons démarrer un grand nombre de ces machines en même temps, en ajustant ce nombre facilement selon nos besoins.

Dans l'un de nos tests, nous avons pu démarrer une flotte de 650 machines et atteindre un pic de 35 millions de prédictions par heure à un coût de 19 $/h. À ce rythme, nous pourrions remplir toutes nos données en seulement quelques mois. Maintenant, cela semble faisable :)

Dans un autre test avec des machines plus puissantes mais toujours abordables, nous avons pu atteindre des pics de 25 000 prédictions par seconde, soit plus de 2 milliards par jour !

#### Comparaison des prix avec d'autres solutions de traitement d'images à la demande

Comparons ces chiffres à quelques-unes des plus grandes solutions ML préconstruites pour le traitement d'images sur le marché. Notre coût de base avec les instances spot est de **0,50 $ par million d'images**.

[**Google Vision - 600 $ par million d'images**](https://cloud.google.com/vision/pricing) : Il existe différents niveaux en fonction de la demande. Le prix baisse de presque un tiers si vous franchissez la barre des 5M images par mois, et nous le ferons définitivement. Pour simplifier les calculs, je ne considérerai que l'option la moins chère, et cela nous coûterait tout de même la somme astronomique de 600 $ pour analyser un million d'images.

[**Amazon Rekognition - 400 $ par million d'images**](https://aws.amazon.com/rekognition/pricing/) : Leur niveau de prix le moins cher ne commence à s'appliquer qu'après 100M images par mois. Si nous considérons à nouveau le prix le plus bas pour simplifier le calcul, cela nous coûterait 400 $ pour analyser un million d'images.

[**Amazon SageMaker - 3,97 $ par million d'images**](https://aws.amazon.com/sagemaker/pricing/) : Il s'agit d'une solution ML plus générale comme celle de ce guide, et il est plus facile d'établir une comparaison ici car ils offrent les mêmes machines que celles sur lesquelles nous avons benchmarké notre backfill. Celle capable de faire 1000 prédictions par minute nous coûterait 3,97 $ pour un million d'images. C'est plus du double du prix régulier pour cette machine, et presque 8 fois le coût du prix spot.

Faites-moi savoir dans la section des commentaires comment cette configuration fonctionne pour vous. Toutes les suggestions et améliorations sont les bienvenues, et commentez si vous savez comment améliorer cela. Amusez-vous bien !