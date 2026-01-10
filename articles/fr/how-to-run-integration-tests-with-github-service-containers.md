---
title: Comment exécuter des tests d'intégration avec les conteneurs de service GitHub
subtitle: ''
author: Alex Pliutau
co_authors: []
series: null
date: '2025-01-07T19:31:49.189Z'
originalURL: https://freecodecamp.org/news/how-to-run-integration-tests-with-github-service-containers
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1735305764768/8e3d8980-456b-4828-abb7-dff749bbf1fd.png
tags:
- name: GitHub
  slug: github
- name: github-actions
  slug: github-actions-1
- name: Devops
  slug: devops
- name: containers
  slug: containers
- name: Testing
  slug: testing
- name: CI/CD
  slug: cicd
- name: Docker
  slug: docker
seo_title: Comment exécuter des tests d'intégration avec les conteneurs de service
  GitHub
seo_desc: Recently, I published an article about using Testcontainers to emulate external
  dependencies like a database and cache for backend integration tests. That article
  also explained the different ways of running the integration tests, environment
  scaffol...
---

Récemment, j'ai publié un [**article**](https://www.freecodecamp.org/news/integration-tests-using-testcontainers/) sur l'utilisation de [**Testcontainers**](https://testcontainers.com/) pour émuler des dépendances externes comme une base de données et un cache pour les tests d'intégration backend. Cet article expliquait également les différentes façons d'exécuter les tests d'intégration, l'échafaudage de l'environnement, et leurs avantages et inconvénients.

Dans cet article, je souhaite montrer une autre alternative si vous utilisez GitHub Actions comme plateforme CI (la solution CI/CD la plus populaire à l'heure actuelle). Cette alternative s'appelle [**Service Containers**](https://docs.github.com/en/actions/use-cases-and-examples/using-containerized-services/about-service-containers), et je me suis rendu compte que peu de développeurs semblent la connaître.

Dans ce tutoriel pratique, je vais démontrer comment créer un workflow GitHub Actions pour des tests d'intégration avec des dépendances externes (MongoDB et Redis) en utilisant l'[application de démonstration Go](https://github.com/plutov/packagemain/tree/master/testcontainers-demo) que nous avons créée dans le tutoriel précédent. Nous examinerons également les avantages et inconvénients des conteneurs de service GitHub.

## Prérequis

* Une compréhension de base des workflows GitHub Actions.

* Une familiarité avec les conteneurs Docker.

* Une connaissance de base de la chaîne d'outils Go.

## Table des matières

* [Qu'est-ce que les Service Containers ?](#heading-quest-ce-que-les-service-containers)

* [Pourquoi pas Docker Compose ?](#heading-pourquoi-pas-docker-compose)

* [Runtime du Job](#heading-runtime-du-job)

* [Vérification de santé de préparation](#heading-verification-de-sante-de-preparation)

* [Registres de conteneurs privés](#heading-registres-de-conteneurs-prives)

* [Partage de données entre services](#heading-partage-de-donnees-entre-services)

* [Tests d'intégration Golang](#heading-tests-dintegration-golang)

* [Expérience personnelle et limitations](#heading-experience-personnelle-et-limitations)

* [Conclusion](#heading-conclusion)

* [Ressources](#heading-ressources)

## Qu'est-ce que les Service Containers ?

Les Service Containers sont des conteneurs Docker qui offrent une manière simple et portable d'héberger des dépendances comme des bases de données (MongoDB dans notre exemple), des services web, ou des systèmes de cache (Redis dans notre exemple) dont votre application a besoin dans un workflow.

Cet article se concentre sur les tests d'intégration, mais il existe de nombreuses autres applications possibles pour les conteneurs de service. Par exemple, vous pouvez également les utiliser pour exécuter des outils de support requis par votre workflow, tels que des outils d'analyse de code, des linters, ou des scanners de sécurité.

## Pourquoi pas Docker Compose ?

Cela ressemble aux **services** dans Docker Compose, n'est-ce pas ? En effet, c'est le cas.

Mais bien que vous puissiez techniquement [utiliser Docker Compose](https://github.com/marketplace/actions/docker-compose-action) dans un workflow GitHub Actions en installant Docker Compose et en exécutant **docker-compose up**, les conteneurs de service offrent une approche plus intégrée et rationalisée, spécifiquement conçue pour l'environnement GitHub Actions.

De plus, bien qu'ils soient similaires, ils résolvent des problèmes différents et ont des objectifs généraux différents :

* Docker Compose est utile lorsque vous devez gérer une application multi-conteneurs sur votre machine locale ou un seul serveur. Il est mieux adapté aux environnements de longue durée.

* Les Service Containers sont éphémères et n'existent que pour la durée d'exécution d'un workflow, et ils sont définis directement dans votre fichier de workflow GitHub Actions.

Gardez simplement à l'esprit que l'ensemble des fonctionnalités des conteneurs de service (du moins pour l'instant) est plus limité par rapport à Docker Compose, alors soyez prêt à découvrir certains goulots d'étranglement potentiels. Nous aborderons certains d'entre eux à la fin de cet article.

## Runtime du Job

Vous pouvez exécuter des jobs GitHub directement sur une machine runner ou dans un conteneur Docker (en spécifiant la propriété **container**). La deuxième option simplifie l'accès à vos services en utilisant les labels que vous définissez dans la section **services**.

Pour exécuter directement sur une machine runner :

**.github/workflows/test.yaml**

```yaml
jobs:
  integration-tests:
    runs-on: ubuntu-24.04

    services:
      mongo:
        image: mongodb/mongodb-community-server:7.0-ubi8
        ports:
          - 27017:27017

    steps:
      - run: |
          echo "addr 127.0.0.1:27017"
```

Ou vous pouvez l'exécuter dans un conteneur ([Chainguard Go Image](https://images.chainguard.dev/directory/image/go/overview) dans notre cas) :

```yaml
jobs:
  integration-tests:
    runs-on: ubuntu-24.04
    container: cgr.dev/chainguard/go:latest

    services:
      mongo:
        image: mongodb/mongodb-community-server:7.0-ubi8
        ports:
          - 27017:27017
    steps:
      - run: |
          echo "addr mongo:27017"
```

Vous pouvez également omettre le port hôte, de sorte que le port du conteneur sera attribué aléatoirement à un port libre sur l'hôte. Vous pouvez ensuite accéder au port en utilisant la variable.

Avantages de l'omission du port hôte :

* Évite les conflits de ports – par exemple lorsque vous exécutez de nombreux services sur le même hôte.

* Améliore la portabilité – vos configurations deviennent moins dépendantes de l'environnement hôte spécifique.

```yaml
jobs:
  integration-tests:
    runs-on: ubuntu-24.04
    container: cgr.dev/chainguard/go:1.23

    services:
      mongo:
        image: mongodb/mongodb-community-server:7.0-ubi8
        ports:
          - 27017/tcp
    steps:
      - run: |
          echo "addr mongo:${{ job.services.mongo.ports['27017'] }}"
```

Bien sûr, chaque approche a ses avantages et ses inconvénients.

Exécution dans un conteneur :

* **Avantages** : Accès réseau simplifié (utilisation des labels comme noms d'hôte), et exposition automatique des ports dans le réseau du conteneur. Vous obtenez également une meilleure isolation/sécurité car le job s'exécute dans un environnement isolé.

* **Inconvénients** : Surcoût implicite de la conteneurisation.

Exécution sur la machine runner :

* **Avantages** : Potentiellement moins de surcoût que l'exécution du job dans un conteneur.

* **Inconvénients** : Nécessite un mappage manuel des ports pour l'accès aux conteneurs de service (en utilisant localhost:). Il y a également moins d'isolation/sécurité, car le job s'exécute directement sur la machine runner. Cela peut potentiellement affecter d'autres jobs ou le runner lui-même si quelque chose ne va pas.

## Vérification de santé de préparation

Avant d'exécuter les tests d'intégration qui se connectent à vos conteneurs provisionnés, vous devrez souvent vous assurer que les services sont prêts. Vous pouvez le faire en spécifiant les [options de création Docker](https://docs.docker.com/reference/cli/docker/container/create/#options) telles que **health-cmd**.

Cela est très important – sinon les services peuvent ne pas être prêts lorsque vous commencez à y accéder.

Dans le cas de MongoDB et Redis, voici ce que cela donnera :

```yaml
    services:
      mongo:
        image: mongodb/mongodb-community-server:7.0-ubi8
        ports:
          - 27017/27017
        options: >-
          --health-cmd "echo 'db.runCommand("ping").ok' | mongosh mongodb://localhost:27017/test --quiet"
          --health-interval 5s
          --health-timeout 10s
          --health-retries 10

      redis:
        image: redis:7
        ports:
          - 6379:6379
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 5s
          --health-timeout 10s
          --health-retries 10
```

Dans les logs des Actions, vous pouvez voir le statut de préparation :

![GitHub Actions Logs](https://cdn.hashnode.com/res/hashnode/image/upload/v1736245987630/0b0bf229-b8d3-4e4e-8e0b-e3bbe5f9a6d8.png align="center")

## Registres de conteneurs privés

Dans notre exemple, nous utilisons des images publiques de Dockerhub, mais il est possible d'utiliser des images privées de vos registres privés, tels que Amazon Elastic Container Registry (ECR), Google Artifact Registry, etc.

Assurez-vous de stocker les identifiants dans [Secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions) puis de les référencer dans la section **credentials**.

```yaml
services:
  private_service:
    image: ghcr.io/org/service_repo
    credentials:
      username: ${{ secrets.registry_username }}
      password: ${{ secrets.registry_token }}
```

## Partage de données entre services

Vous pouvez utiliser des volumes pour partager des données entre services ou d'autres étapes dans un job. Vous pouvez spécifier des volumes Docker nommés, des volumes Docker anonymes, ou des montages de liaison sur l'hôte. Mais il n'est pas directement possible de monter le code source comme un volume de conteneur. Vous pouvez vous référer à cette [discussion ouverte](https://github.com/orgs/community/discussions/42127) pour plus de contexte.

Pour spécifier un volume, vous spécifiez le chemin source et de destination : `<source>:<destinationPath>`

Le `<source>` est un nom de volume ou un chemin absolu sur la machine hôte, et `<destinationPath>` est un chemin absolu dans le conteneur.

```yaml
volumes:
  - /src/dir:/dst/dir
```

Les volumes dans Docker (et GitHub Actions utilisant Docker) fournissent un stockage de données persistant et un partage entre conteneurs ou étapes de job, découplant les données des images de conteneur.

## Configuration du projet

Avant de plonger dans le code source complet, configurons notre projet pour exécuter des tests d'intégration avec les conteneurs de service GitHub.

1. Créez un nouveau dépôt GitHub.

2. Initialisez un module Go en utilisant `go mod init`

3. Créez une application Go simple.

4. Ajoutez des tests d'intégration dans `integration_test.go`

5. Créez un répertoire `.github/workflows`.

6. Créez un fichier nommé `integration-tests.yaml` à l'intérieur du répertoire `.github/workflows`.

## Tests d'intégration Golang

Maintenant que nous pouvons provisionner nos dépendances externes, voyons comment exécuter nos tests d'intégration en Go. Nous le ferons dans la section **steps** de notre fichier de workflow.

Nous exécuterons nos tests dans un conteneur qui utilise l'image [Chainguard Go](https://images.chainguard.dev/directory/image/go/overview). Cela signifie que nous n'avons pas à installer/configurer Go. Si vous souhaitez exécuter vos tests directement sur une machine runner, vous devez utiliser l'Action [setup-go](https://github.com/actions/setup-go).

Vous pouvez trouver le code source complet avec les tests et ce workflow [ici](https://github.com/plutov/service-containers).

**.github/workflows/integration-tests.yaml**

```yaml
name: "integration-tests"

on:
  workflow_dispatch:
  push:
    branches:
      - main

jobs:
  integration-tests:
    runs-on: ubuntu-24.04
    container: cgr.dev/chainguard/go:latest

    env:
      MONGO_URI: mongodb://mongo:27017
      REDIS_URI: redis://redis:6379

    services:
      mongo:
        image: mongodb/mongodb-community-server:7.0-ubi8
        ports:
          - 27017:27017
        options: >-
          --health-cmd "echo 'db.runCommand("ping").ok' | mongosh mongodb://localhost:27017/test --quiet"
          --health-interval 5s
          --health-timeout 10s
          --health-retries 10

      redis:
        image: redis:7
        ports:
          - 6379:6379
        options: >-
          --health-cmd "redis-cli ping"
          --health-interval 5s
          --health-timeout 10s
          --health-retries 10

    steps:
      - name: Check out repository code
        uses: actions/checkout@v4

      - name: Download dependencies
        run: go mod download

      - name: Run Integration Tests
        run: go test -tags=integration -timeout=120s -v ./...
```

Pour résumer ce qui se passe ici :

1. Nous exécutons notre job dans un conteneur avec Go (**container**)

2. Nous lançons deux services : MongoDB et Redis (**services**)

3. Nous configurons des vérifications de santé pour nous assurer que nos services sont "Healthy" lorsque nous exécutons les tests (**options**)

4. Nous effectuons une vérification standard du code

5. Ensuite, nous exécutons les tests Go

Une fois l'Action terminée (cela a pris **~1 min** pour cet exemple), tous les services seront arrêtés et orphelins, donc nous n'avons pas à nous en soucier.

![GitHub Actions Logs: full run](https://miro.medium.com/v2/resize:fit:480/0*QLl4vjotU6o1osy-.png align="left")

## Expérience personnelle et limitations

Nous utilisons les conteneurs de service pour exécuter des tests d'intégration backend chez [BINARLY](https://www.binarly.io/) depuis un certain temps, et ils fonctionnent très bien. Mais la création initiale du workflow a pris un certain temps et nous avons rencontré les goulots d'étranglement suivants :

* Il n'est pas possible de remplacer ou d'exécuter des commandes personnalisées dans un conteneur de service d'action (comme vous le feriez dans Docker Compose en utilisant la propriété **command**). [Pull request ouvert](https://github.com/actions/runner/pull/1152)

    * Solution de contournement : nous avons dû trouver une solution qui n'exige pas cela. Dans notre cas, nous avons eu de la chance et avons pu faire la même chose avec des variables d'environnement.

* Il n'est pas directement possible de monter le code source comme un volume de conteneur. [Discussion ouverte](https://github.com/orgs/community/discussions/42127)

    * Bien que ce soit effectivement une grande limitation, vous pouvez copier le code de votre dépôt dans votre répertoire monté après que le conteneur de service ait démarré.

## Conclusion

Les conteneurs de service GitHub sont une excellente option pour échafauder un environnement de test éphémère en le configurant directement dans votre workflow GitHub. Avec une configuration quelque peu similaire à Docker Compose, il est facile d'exécuter toute application conteneurisée et de communiquer avec elle dans votre pipeline. Cela garantit que les runners GitHub s'occupent de tout arrêter à la fin.

Si vous utilisez GitHub Actions, cette approche fonctionne extrêmement bien car elle est spécifiquement conçue pour l'environnement GitHub Actions.

### Ressources

* [Code Source](https://github.com/plutov/service-containers)

* [Documentation GitHub](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#jobsjob_idservices)

* Découvrez plus d'articles sur [packagemain.tech](https://packagemain.tech/)