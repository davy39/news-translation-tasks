---
title: Extensions Docker pour vous aider à améliorer votre flux de travail
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-05-05T16:10:05.000Z'
originalURL: https://freecodecamp.org/news/docker-extensions-to-improve-workflow
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Copy-of-What-is-Docker-compose.png
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
seo_title: Extensions Docker pour vous aider à améliorer votre flux de travail
seo_desc: "Docker is becoming increasingly popular, and many organizations have started\
  \ incorporating it into their development lifecycle. \nBecause of this, it's an\
  \ important tool to learn and can help you automate many of your tasks and workflows.\
  \ \nIf you are ..."
---

Docker devient de plus en plus populaire, et de nombreuses organisations ont commencé à l'intégrer dans leur cycle de développement. 

De ce fait, c'est un outil important à apprendre et il peut vous aider à automatiser de nombreuses tâches et flux de travail. 

Si vous êtes nouveau dans Docker, veuillez lire [mon tutoriel précédent](https://www.freecodecamp.org/news/what-is-docker-compose-how-to-use-it/) sur ce qu'est Docker et comment l'utiliser. Cela vous aidera à comprendre facilement le flux de travail dans Docker.

Dans ce tutoriel, nous allons explorer cinq extensions Docker simples et puissantes qui peuvent améliorer l'efficacité et la productivité de votre flux de travail Docker. 

Ces extensions sont conçues pour simplifier le processus de développement, augmenter la scalabilité et vous aider à économiser du temps et des ressources. Elles sont :

1. JFrog
2. Portainer
3. Utilisation du disque
4. Drone CI
5. Okteto

## 1. JFrog Scan

Si vous avez déjà travaillé avec des images Docker, vous savez peut-être que parfois vous devrez travailler avec des images Docker open-source. Cette extension est utile dans ces cas.

En utilisant l'extension Docker JFrog, vous pouvez analyser tout type d'image Docker. La plupart de vos images Docker internes n'auront pas de configurations nuisibles. Mais certaines images Docker open source peuvent contenir des vulnérabilités, donc cela est surtout utile pour les images Docker open-source ou tierces.

Vous pouvez l'installer depuis le marketplace Docker.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-337.png)
_Installation de JFrog dans le marketplace Docker_

Avant d'utiliser JFrog, vous aurez besoin d'un compte actif de JFrog. Vous pouvez créer un compte gratuitement.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-338.png)
_Console de connexion JFrog_

Après une connexion réussie, choisissez une image à analyser pour les vulnérabilités.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-339.png)
_Choisir une image à analyser pour les vulnérabilités_

Vous pouvez voir que l'image est en cours d'analyse pour les vulnérabilités. Cela peut prendre un certain temps. 

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-340.png)
_JFrog analyse les images_

Oups, cette image Docker a 25 vulnérabilités critiques, comme vous pouvez le voir dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-341.png)
_Vulnérabilités trouvées dans l'image Docker_

De même, vous pouvez analyser les images avant de les utiliser pour être conscient des vulnérabilités et les corriger.

## 2. Portainer

Portainer fournit une interface basée sur le web pour gérer les conteneurs, images, volumes, réseaux et autres ressources liées à Docker.

Vous pouvez utiliser cette extension pour gérer plus facilement les hôtes de conteneurs, les clusters Docker Swarm et les clusters Kubernetes.

En utilisant Portainer, vous pouvez gérer les conteneurs en cours d'exécution, les images et les environnements dans une interface utilisateur uniforme.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-342.png)
_Gestion des conteneurs en utilisant le tableau de bord Portainer_

### Quand utiliser Portainer :

1. Cette extension vous permet de gérer des hôtes Docker distants à partir d'une instance centrale de Portainer. Elle fournit un moyen de gérer plusieurs hôtes Docker à partir d'une seule interface.
2. Elle fournit une bibliothèque de modèles que vous pouvez utiliser pour déployer rapidement des applications populaires, telles que WordPress, Drupal et MySQL. Cette extension fournit également un ensemble de modèles pour déployer des applications conteneurisées sur des plateformes cloud populaires telles qu'AWS, Azure et Google Cloud.
3. Cette extension vous permet de sauvegarder et restaurer votre configuration et vos données Portainer. Elle peut être utilisée pour créer une capture instantanée de votre environnement Portainer, qui peut être utilisée pour restaurer votre environnement en cas de sinistre.
4. Cette extension vous permet de gérer des conteneurs s'exécutant sur des appareils de périphérie, tels que des Raspberry Pis ou d'autres appareils embarqués.

Nous pouvons rapidement effectuer toute action sur les conteneurs et les images.

## 3. Utilisation du disque

Utilisation du disque est une extension officielle Docker qui fournit aux développeurs des informations sur l'utilisation du disque Docker. Une fois installée, cette extension examine et catégorise minutieusement l'espace disque occupé par diverses entités, telles que les images, les conteneurs, les volumes locaux et le cache de construction. 

En utilisant cette extension, vous pouvez gérer efficacement votre espace disque en supprimant les objets inutiles.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-343.png)
_Utilisation de l'espace disque par Docker_

Ce processus d'optimisation est crucial pour libérer de l'espace disque pour les ressources critiques. L'extension Utilisation du disque est facilement accessible dans l'onglet des extensions Docker et peut être activée facilement.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-344.png)
_Détails de l'utilisation du disque par les images Docker, les conteneurs et les volumes locaux_

Vous pouvez récupérer l'espace en supprimant les images inutilisées, les images suspendues et les caches de construction. L'extension d'image disque elle-même donne quelques suggestions.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-345.png)
_Récupérer l'utilisation de l'espace disque par Docker_

## 4. Drone CI

Avant de vous lancer dans cette extension, vous devriez connaître la CI. CI signifie Intégration Continue. Lorsque vous commencez avec DevOps, la première chose que vous devez apprendre est l'intégration continue. 

De nos jours, les développeurs s'attendent à ce que les changements de code se reflètent immédiatement sur le serveur de production ou de test en quelques clics. Pour automatiser cela, vous pouvez activer les pipelines CI/CD dans le cycle de développement.

DroneCI est une application open-source qui vous aide à déployer votre application en continu sur votre serveur souhaité. 

DroneCI est simple à configurer et à utiliser. Voyons comment déployer et tester une application NodeJS en utilisant DroneCI.

Vous pouvez l'installer depuis le marketplace des extensions Docker.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screenshot-from-2023-05-05-12-01-55.png)
_Installation de l'extension Drone CI_

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-330.png)
_Importer de nouveaux pipelines_

Avant d'importer le pipeline, vous devez avoir un fichier `.drone.yml`.

```
kind: pipeline
type: docker
name: default

platform:
 os: linux
 arch: arm64

steps:
- name: message
  image: busybox

- name: test
  image: node
  commands:
  - npm install
  - npm test
```

Placez ce fichier à la racine de votre projet Node.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-331.png)
_Pipelines importés_

Après avoir importé le pipeline, vous pouvez exécuter le pipeline.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-346.png)
_Exécuter le pipeline de l'application_

Ici, nous exécutons uniquement pour tester l'application NodeJS. Vous pouvez suivre les mêmes étapes pour la déployer également.

## 5. Okteto

Okteto est un outil utile qui améliore votre productivité et votre satisfaction en vous fournissant des environnements préconfigurés. Cela vous permet de gagner du temps en évitant de configurer manuellement les environnements. 

Cela accélère le processus de développement logiciel et les cycles de publication lorsqu'il est combiné avec une plateforme CI/CD appropriée. Il vous permet également de créer des environnements de prévisualisation ressemblant à des environnements de test et de développement, vous permettant de tester les changements avant de les déployer en production. Avec Okteto, le développement natif cloud devient beaucoup plus facile.

L'extension Okteto est facilement disponible dans le marketplace des extensions Docker Desktop et vous pouvez l'installer en un simple clic. 

Pour tirer parti des avantages d'Okteto, vous devrez configurer le manifeste Okteto pour votre application. Après avoir installé l'extension, elle vous invite à lancer un environnement distant. Choisissez le dossier de l'application avec le fichier manifeste Okteto et commencez à explorer. 

En termes simples, vous pouvez vous connecter à un environnement distant en utilisant Okteto cloud. Pour plus d'informations sur la configuration et l'utilisation d'Okteto, consultez leur [documentation officielle](https://www.okteto.com/docs/).

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-358.png)
_Okteto se connecte à l'environnement distant_

Pour vous connecter à Okteto, vous avez besoin d'une adresse e-mail professionnelle. 

Après une connexion réussie, vous devez choisir le fichier `docker-compose.yml`.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-359.png)
_Okteto se connecte à l'environnement distant_

## Conclusion

Docker est un outil puissant qui simplifie le processus de développement et permet aux développeurs de construire, tester et déployer des applications rapidement et efficacement. 

En utilisant ces extensions Docker, vous pouvez tirer parti de fonctionnalités et de fonctionnalités supplémentaires pour rationaliser votre flux de travail et optimiser votre environnement Docker. 

Outre les extensions mentionnées ci-dessus, il existe d'autres extensions importantes qui peuvent être très utiles :

* Pour automatiser les applications multi-conteneurs, vous pouvez utiliser Docker Compose
* Pour mettre à l'échelle les applications, Docker Swarm est très utile
* Vous pouvez gérer les images Docker avec Docker Registry

Et ainsi de suite. Ces extensions peuvent considérablement améliorer les capacités de Docker et améliorer l'efficacité de votre flux de travail de développement logiciel. 

J'espère que ce guide a été informatif et vous aide à tirer le meilleur parti des extensions Docker.

Pour en savoir plus sur Docker, abonnez-vous à ma newsletter par e-mail sur mon [site](https://5minslearn.gogosoon.com/?ref=fcc_docker_extensions) ([https://5minslearn.gogosoon.com](https://5minslearn.gogosoon.com/?ref=fcc_docker_extensions)) et suivez-moi sur les réseaux sociaux.