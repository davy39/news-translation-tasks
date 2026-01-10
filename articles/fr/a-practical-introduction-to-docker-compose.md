---
title: Une introduction pratique à Docker Compose
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-05T18:15:08.000Z'
originalURL: https://freecodecamp.org/news/a-practical-introduction-to-docker-compose
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/1_JK4VDnsrF6YnAb2nyhMsdQ-2.png
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: Docker compose
  slug: docker-compose
- name: Docker Containers
  slug: docker-containers
seo_title: Une introduction pratique à Docker Compose
seo_desc: 'By Faizan Bashir

  Docker containers opened a world of possibilities for the tech community, hassles
  in setting up new software were decreased unlike old times when a mess was to be
  sorted by a grievous format, it reduced the time to set up and use new...'
---

Par Faizan Bashir

Les conteneurs Docker ont ouvert un monde de possibilités pour la communauté technique, réduisant les tracas liés à la configuration de nouveaux logiciels, contrairement aux anciennes méthodes où un désordre devait être résolu par un formatage pénible. Cela a réduit le temps nécessaire pour configurer et utiliser de nouveaux logiciels, ce qui a finalement joué un grand rôle pour les technophiles afin d'apprendre de nouvelles choses, de les déployer dans un conteneur et de les abandonner une fois terminées. Les choses sont devenues plus faciles, et le meilleur dans tout cela, c'est que c'est open source, tout le monde peut l'utiliser, même si cela nécessite une petite courbe d'apprentissage.

Parmi les nombreuses possibilités, il y avait celle de mettre en œuvre des piles technologiques complexes pour nos applications, ce qui auparavant aurait été le domaine des experts. Aujourd'hui, avec l'aide des conteneurs, les ingénieurs logiciels ayant une bonne compréhension des systèmes sous-jacents peuvent implémenter une pile complexe, et pourquoi pas, c'est le besoin de l'heure. L'expression "Jack of all trades" a reçu une mise à niveau élégante : "Master of some" en fonction des besoins de l'époque. En termes simples, des compétences en forme de "T".

La possibilité de définir une pile complexe dans un fichier et de l'exécuter avec une seule commande, assez tentant, n'est-ce pas ? Les gars de Docker Inc. ont choisi de l'appeler Docker Compose.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1g8v7eeFV2OWt1Tkmoc-4A.jpeg align="left")

Dans cet article, nous utiliserons l'exemple d'application de vote de Docker et la déployerons en utilisant Docker Compose.

---

### Docker Compose

Selon les mots de Docker Inc.

> *Compose est un outil pour définir et exécuter des applications Docker multi-conteneurs. Avec Compose, vous utilisez un fichier YAML pour configurer les services de votre application. Ensuite, avec une seule commande, vous créez et démarrez tous les services à partir de votre configuration.*

---

### L'application de vote

Présentons l'application de démonstration préférée de la communauté Docker, "The Voting App", comme si elle avait besoin d'une introduction. Il s'agit d'une application simple basée sur une architecture de micro-services, composée de 5 services simples.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DIZdPFJO4EQbPNq0pR_b8g.png align="left")

*Architecture de l'application de vote :* [https://github.com/docker/example-voting-app](https://github.com/docker/example-voting-app)

1. **Voting-App** : Frontend de l'application écrit en Python, utilisé par les utilisateurs pour voter.

2. **Redis** : Base de données en mémoire, utilisée comme stockage intermédiaire.

3. **Worker** : Service .Net, utilisé pour récupérer les votes de Redis et les stocker dans la base de données Postgres.

4. **DB** : Base de données PostgreSQL, utilisée comme base de données.

5. **Result-App** : Frontend de l'application écrit en Node.js, affiche les résultats des votes.

Le dépôt Voting contient un fichier appelé `docker-compose.yml`. Ce fichier contient la configuration pour créer les conteneurs, exposer les ports, lier les volumes et connecter les conteneurs via les réseaux nécessaires au fonctionnement de l'application de vote. Cela ressemble à beaucoup de longues commandes `docker run` et `docker network create`, mais Docker Compose nous permet de mettre tout cela dans un seul fichier docker-compose au format [yaml](http://yaml.org/start.html).

```bash
version: "3"

services:
  vote:
    build: ./vote
    command: python app.py
    volumes:
     - ./vote:/app
    ports:
      - "5000:80"
    networks:
      - front-tier
      - back-tier

  result:
    build: ./result
    command: nodemon server.js
    volumes:
      - ./result:/app
    ports:
      - "5001:80"
      - "5858:5858"
    networks:
      - front-tier
      - back-tier

  worker:
    build:
      context: ./worker
    depends_on:
      - "redis"
    networks:
      - back-tier

  redis:
    image: redis:alpine
    container_name: redis
    ports: ["6379"]
    networks:
      - back-tier

  db:
    image: postgres:9.4
    container_name: db
    volumes:
      - "db-data:/var/lib/postgresql/data"
    networks:
      - back-tier

volumes:
  db-data:

networks:
  front-tier:
  back-tier:
```

Clonez le dépôt de l'application de vote avec Git et accédez-y.

[**dockersamples/example-voting-app**](https://github.com/dockersamples/example-voting-app)
[\_example-voting-app - Exemple d'application Docker Compose\_github.com](https://github.com/dockersamples/example-voting-app)

---

### Temps de Compose

Avec toute notre application définie dans un seul fichier compose, nous pouvons soupirer de soulagement, nous détendre et simplement exécuter l'application. La beauté de compose réside dans le fait qu'une seule commande crée tous les services, configure les réseaux (littéralement), monte tous les volumes et expose les ports. Il est temps d'accueillir la commande `up`, elle effectue toutes les tâches mentionnées ci-dessus.

```bash
$ docker-compose up
```

Après de nombreux "Pull complete", des centaines de mégaoctets et quelques minutes (peut-être plus)...

Et voilà, nous avons l'application de vote opérationnelle.

La commande `docker ps` liste tous les conteneurs en cours d'exécution.

```bash
$ docker ps -a --format="table {{.Names}}\t{{.Image}}\t{{.Ports}}" 
NAMES               IMAGE               PORTS
voting_worker_1     voting_worker      
db                  postgres:9.4        5432/tcp
voting_vote_1       voting_vote         0.0.0.0:5000->80/tcp
voting_result_1     voting_result       0.0.0.0:5858->5858/tcp, 0.0.0.0:5001->80/tcp
redis               redis:alpine        0.0.0.0:32768->6379/tcp
```

La commande ci-dessus affiche tous les conteneurs en cours d'exécution, leurs images respectives et les numéros de ports exposés.

L'application de vote peut être accessible sur [http://localhost:5000](http://localhost:5000/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*2OBAYVFG35tX6dHI08TWPg.png align="left")

De même, l'application de résultats de vote peut être accessible sur [http://localhost:5001](http://localhost:5001/)

![Image](https://cdn-media-1.freecodecamp.org/images/1*E-WleHhSji49ZLIafS8xgQ.png align="left")

Chaque vote émis sur l'application de vote est d'abord stocké dans la base de données en mémoire Redis, le service worker .Net récupère le vote et le stocke dans la base de données Postgres, qui est accessible par le frontend Node.js.

---

### Fonctionnalités de Compose

Compose offre la flexibilité d'utiliser un nom de projet pour isoler les environnements les uns des autres. Le nom du projet est le nom de base du répertoire qui contient le projet. Dans notre application de vote, cela est signifié par le nom des conteneurs `voting_worker_1` où `voting` est le nom de base du répertoire. Nous pouvons définir un nom de projet personnalisé en utilisant le drapeau `-p` suivi du nom personnalisé.

Compose préserve tous les volumes utilisés par les services définis dans le fichier compose, ainsi aucune donnée n'est perdue lorsque les conteneurs sont recréés en utilisant `docker-compose up`. Une autre fonctionnalité intéressante est que seuls les conteneurs qui ont changé sont recréés, les conteneurs dont l'état n'a pas changé restent intacts.

Une autre fonctionnalité intéressante est la prise en charge des variables dans le fichier compose. Nous pouvons définir des variables dans un fichier `.env` et les utiliser dans le fichier docker-compose. Ici, `POSTGRES_VERSION=9.4` peut être défini dans le fichier d'environnement ou peut être défini dans le shell. Il est utilisé dans le fichier compose de la manière suivante :

```bash
db:  
  image: "postgres:${POSTGRES_VERSION}"
```

---

### Aide-mémoire des commandes

C'est facile comme bonjour de démarrer, arrêter et jouer avec compose.

```bash
$ docker-compose up -d
$ docker-compose down
$ docker-compose start
$ docker-compose stop
$ docker-compose build
$ docker-compose logs -f db
$ docker-compose scale db=4
$ docker-compose events
$ docker-compose exec db bash
```

---

### Résumé

Docker Compose est un excellent outil pour déployer et abandonner rapidement des conteneurs. Le fichier compose peut s'exécuter de manière transparente sur n'importe quelle machine installée avec docker-compose. L'expérimentation et l'apprentissage des technologies ne sont qu'à un fichier Compose de distance ;).

J'espère que cet article a aidé à comprendre Docker Compose. J'adorerais entendre comment vous utilisez Docker Compose dans vos projets. Partagez les connaissances, aidez-les à atteindre plus de personnes.