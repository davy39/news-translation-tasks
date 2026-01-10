---
title: Qu'est-ce que Docker Compose ? Comment l'utiliser avec un exemple
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-04-07T19:29:48.000Z'
originalURL: https://freecodecamp.org/news/what-is-docker-compose-how-to-use-it
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/What-is-Docker-compose-1.png
tags:
- name: containers
  slug: containers
- name: Docker compose
  slug: docker-compose
seo_title: Qu'est-ce que Docker Compose ? Comment l'utiliser avec un exemple
seo_desc: "Docker helps you setup a development environment on your machine quickly.\
  \ It only takes a couple of minutes to go through the entire process. \nBut let's\
  \ assume you were assigned on a project which requires at least 10 different services\
  \ in a running ..."
---

Docker vous aide à configurer un environnement de développement sur votre machine rapidement. Il ne faut que quelques minutes pour parcourir tout le processus. 

Mais supposons que vous avez été assigné à un projet qui nécessite au moins 10 services différents en état de fonctionnement pour exécuter votre projet. Par exemple, disons que votre projet nécessite Java 8, Node 14, MySQL, MongoDB, Ruby on Rails, RabbitMQ, et autres. 

Dans un tel cas, vous devez tirer toutes ces images individuellement de Docker et les démarrer toutes dans leurs conteneurs. À un moment donné, un processus peut dépendre d'un autre pour s'exécuter. Vous devez donc les ordonner. 

Ce serait bien si c'était un processus ponctuel. Mais, pas seulement une fois – tous les jours, chaque fois que vous commencez à travailler sur votre projet – vous devez démarrer tous ces services.

C'est un processus fastidieux, n'est-ce pas ?

Pour surmonter cela, Docker a introduit un concept appelé Multi Conteneurs (Docker Compose). Avant d'apprendre Docker Compose, apprenons rapidement comment démarrer un hôte de base de données dans Docker. 

Dans la partie exemple de ce tutoriel, nous allons lancer un conteneur NodeJS et un conteneur MongoDB ensemble. Apprendre MongoDB au début vous donnera une bonne compréhension lorsque nous passerons à Docker Compose. 

Nous allons diviser ce tutoriel en 2 sections :

1. Comment utiliser Docker comme hôte de base de données (MongoDB)
2. Comment Docker Compose fonctionne avec un exemple (NodeJS et MongoDB)

## Comment utiliser Docker comme hôte de base de données

Si vous avez de l'expérience avec le développement backend, vous avez peut-être eu l'occasion de gérer plusieurs bases de données. Par exemple, des bases de données comme MySQL/Postgres pour gérer les données relationnelles et Cassandra/MongoDB pour gérer les données non structurées.

Voulez-vous connaître un secret ? Vous pouvez travailler sur le développement backend sans installer la base de données sur votre machine localement. Oui, vous pouvez utiliser Docker comme hôte de base de données. Il contient toutes les dépendances par défaut dans le fichier d'image particulier.

## Pourquoi avons-nous besoin de la base de données Docker ?

Docker nous aide à maintenir des versions cohérentes sur différentes plateformes et environnements. Supposons qu'il y ait un groupe de personnes travaillant dans votre équipe sur MongoDB version 5.0. Si un nouveau membre rejoint votre équipe, il devra configurer la même version avec la configuration exacte manuellement. Et s'il installe la dernière version de MongoDB (6.0) ? Cela entraînera certains conflits. Ce sera un cauchemar si cela se propage à tous les autres appareils.

Pour contourner cela, vous pouvez utiliser MongoDB dans Docker avec une configuration personnalisée et pousser l'image MongoDB vers Docker Hub en interne. Si une nouvelle personne arrive, elle peut tirer l'image et commencer l'implémentation sans aucune configuration manuelle.

Regardons les avantages d'utiliser une base de données dans Docker.

1. En utilisant cette implémentation, nous pouvons nous assurer que tout le monde dans une équipe utilise les mêmes environnements d'exécution et configurations sans ressources externes.
2. C'est très facile à configurer et nous pouvons démarrer/arrêter le serveur rapidement en utilisant Docker Desktop

## Comment configurer MongoDB en utilisant Docker

Si vous n'êtes pas familier avec Docker Hub, voici une courte introduction. Docker Hub est une plateforme où vous pouvez trouver et partager des images Docker qui sont publiques ou privées. C'est assez similaire à GitHub / GitLab. En résumé, c'est un dépôt pour les images Docker.

La première étape consiste à tirer l'image Docker officielle de Docker Hub.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-43.png)
_Image MongoDB dans Docker Hub_

```bash
docker pull mongo:latest
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-44.png)
_Sortie d'exemple pour tirer l'image Mongo de Docker Hub_

Une fois que vous avez terminé de tirer l'image Mongo, ouvrez votre Docker Desktop et vous pourrez la voir là.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-45.png)
_Image Mongo disponible dans Docker Desktop_

Lançons notre image MongoDB en utilisant la commande `docker run`.

```bash
docker run -d -p 27017:27017 --name mongo-server-local mongo:latest
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-46.png)
_Sortie d'exemple pour exécuter MongoDB dans Docker_

Nous avons exécuté avec succès l'image Docker. Maintenant, nous pouvons voir le conteneur en cours d'exécution sur Docker Desktop.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-48.png)
_Conteneur Mongo en cours d'exécution dans Docker Desktop_

Donc, le serveur MongoDB est en cours d'exécution sur votre machine. Confirmons cela dans le navigateur. Allez sur [http://localhost:27017](http://localhost:27017) dans votre navigateur et vous devriez pouvoir voir le message comme indiqué dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-49.png)
_Sortie d'exemple "Il semble que vous essayez d'accéder à MongoDB via HTTP sur le port natif du pilote" pour l'exécution du serveur MongoDB en utilisant Docker_

Intéressant, n'est-ce pas ?

Nous pouvons arrêter/démarrer le serveur MongoDB en utilisant Docker chaque fois que nous en avons besoin.

### Note importante

1. Il n'est pas recommandé d'utiliser Docker comme base de données pour la production
2. N'utilisez pas la base de données Docker pour les applications à grande échelle

## Qu'est-ce que docker-compose ?

Revenons à docker-compose.

Docker Compose est un outil que vous pouvez utiliser pour définir et partager des applications multi-conteneurs. Cela signifie que vous pouvez exécuter un projet avec plusieurs conteneurs en utilisant une seule source.

Par exemple, supposons que vous construisez un projet avec NodeJS et MongoDB ensemble. Vous pouvez créer une seule image qui démarre les deux conteneurs en tant que service – vous n'avez pas besoin de démarrer chacun séparément.

Intéressant, n'est-ce pas ? Et cela résout le problème que j'ai mentionné au tout début de cet article.

Pour y parvenir, nous devons définir un `docker-compose.yml`.

### Fichier docker-compose.yml

Le fichier compose est un fichier YML définissant les services, réseaux et volumes pour un conteneur Docker. Il existe plusieurs versions du format de fichier compose disponibles – 1, 2, 2.x, et 3.x.

Avant de continuer, voici une note importante de l'équipe [Docker Compose](https://docs.docker.com/compose/).

> À partir de la fin juin 2023, Compose V1 ne sera plus supporté et sera retiré de toutes les versions de Docker Desktop. 

Nous utilisons la version 3 dans cet article.

```docker-compose
version: '3'
services:
  app:
    image: node:latest
    container_name: app_main
    restart: always
    command: sh -c "yarn install && yarn start"
    ports:
      - 8000:8000
    working_dir: /app
    volumes:
      - ./:/app
    environment:
      MYSQL_HOST: localhost
      MYSQL_USER: root
      MYSQL_PASSWORD: 
      MYSQL_DB: test
  mongo:
    image: mongo
    container_name: app_mongo
    restart: always
    ports:
      - 27017:27017
    volumes:
      - ~/mongo:/data/db
volumes:
  mongodb:
```

Démontons le code ci-dessus et comprenons-le pièce par pièce :

* `version` fait référence à la version de docker-compose (Dernière 3)
* `services` définit les services que nous devons exécuter
* `app` est un nom personnalisé pour l'un de vos conteneurs
* `image` est l'image que nous devons tirer. Ici, nous utilisons `node:latest` et `mongo`.
* `container_name` est le nom pour chaque conteneur
* `restart` démarre/redémarre un conteneur de service
* `port` définit le port personnalisé pour exécuter le conteneur
* `working_dir` est le répertoire de travail actuel pour le conteneur de service
* `environment` définit les variables d'environnement, telles que les identifiants de la base de données, etc.
* `command` est la commande pour exécuter le service

### Comment exécuter le multi-conteneur

Nous devons construire notre multi-conteneur en utilisant docker build.

```bash
docker compose build
```

Après avoir construit avec succès, nous pouvons exécuter les conteneurs en utilisant la commande `up`.

```bash
docker compose up
```

Si vous souhaitez exécuter le conteneur en mode détaché, utilisez simplement le drapeau `-d`.

```bash
docker compose up -d
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-50.png)
_Sortie d'exemple pour exécuter plusieurs conteneurs en utilisant docker-compose en mode détaché_

Bien, nous sommes prêts à partir. Les conteneurs sont en cours d'exécution. Vérifions la liste des conteneurs.

```bash
docker compose ps
```

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-51.png)
_Sortie d'exemple pour lister les services de conteneurs en cours d'exécution_

Hourra, nous pouvons voir qu'il y a deux conteneurs en cours d'exécution en même temps.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-54.png)
_Sortie d'exemple pour l'exécution du service nodejs en utilisant docker_

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-55.png)
_Sortie d'exemple pour l'exécution du service mongodb en utilisant docker_

Pour voir les données dans votre MongoDB, vous devez installer MongoDB Compass.

Voici une capture d'écran.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-56.png)
_Vue du serveur MongoDB dans mongodb compass_

## Conclusion

Dans cet article, vous avez appris comment Docker Compose fonctionne avec un exemple. En utilisant plusieurs conteneurs, vous pouvez lancer n'importe quel type de service tel que RabbitMQ ou Apache Kafka et l'exécuter dans une seule source de service. J'espère que vous avez apprécié la lecture de cet article.

Si vous souhaitez en savoir plus sur Docker, abonnez-vous à mon article sur mon [site](https://5minslearn.gogosoon.com/?ref=fcc_docker_compose) ([https://5minslearn.gogosoon.com](https://5minslearn.gogosoon.com/?ref=fcc_docker_compose)) qui contient une liste consolidée de tous mes blogs.