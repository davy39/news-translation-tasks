---
title: Comment automatiser la construction et la publication d'images Docker avec
  Pack CLI et GitHub Actions
subtitle: ''
author: Destiny Erhabor
co_authors: []
series: null
date: '2023-07-12T21:55:00.000Z'
originalURL: https://freecodecamp.org/news/automating-docker-image-builds-and-publishing-with-pack-cli
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/pexels-jiyoung-kim-4513940.jpg
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: GitHub Actions
  slug: github-actions
seo_title: Comment automatiser la construction et la publication d'images Docker avec
  Pack CLI et GitHub Actions
seo_desc: Building and publishing Docker images is a crucial aspect of modern software
  development. The traditional approach often involves writing complex Dockerfiles
  and managing dependencies. But in this tutorial post, I'll show you a simpler way
  that uses ...
---

La construction et la publication d'images Docker sont des aspects cruciaux du développement logiciel moderne. L'approche traditionnelle implique souvent l'écriture de Dockerfiles complexes et la gestion des dépendances. Mais dans ce tutoriel, je vais vous montrer une méthode plus simple qui utilise le Pack CLI.

Pack CLI s'appuie sur les Cloud Native Buildpacks pour transformer votre code source d'application en images pouvant s'exécuter sur n'importe quel cloud. Ils sont généralement responsables d'un composant de langage, d'une chaîne d'outils ou d'un composant d'application, tel que Python, pip ou un serveur web. Vous pouvez en apprendre plus sur leur [site web](https://buildpacks.io/).

Dans cet article, nous allons parcourir un workflow GitHub étape par étape pour construire une image Docker pour une application de portfolio personnel et la publier sur Docker Hub en utilisant cet outil puissant.

## Table des matières

* [Prérequis](#heading-prerequisites)
* [Comment créer le workflow](#heading-how-to-create-the-workflow)
* [Découpage du workflow](#heading-workflow-breakdown)
* [Workflow complet](#heading-full-workflow)
* [Conclusion](#heading-conclusion)

## Prérequis

Avant de plonger dans le workflow, assurez-vous d'avoir les prérequis suivants :

* **Docker** : Bien qu'optionnel pour les builds locaux, il est recommandé d'avoir Docker installé.
* **Pack CLI** : Cet outil est essentiel pour les builds locaux et peut être installé à partir de la documentation officielle.
* **Compte Docker Hub** : Vous aurez besoin d'un compte Docker Hub authentifié pour publier les images.
* **Compte GitHub** : Le workflow sera déclenché par des actions sur GitHub.

**Avant de commencer** : Pour suivre l'exemple de workflow GitHub, assurez-vous d'avoir cloné le dépôt [personal_website](https://github.com/Caesarsage/personal_website.git). Vous pouvez également utiliser tout autre projet pour lequel vous souhaitez construire l'image et la publier sur Docker Hub.

Maintenant, commençons avec notre workflow :

## Comment créer le workflow

Pour simplifier le processus de construction et de publication d'images Docker, nous allons utiliser Pack CLI et un workflow puissant sur GitHub.

Ce workflow élimine le besoin d'écrire des Dockerfiles complexes et rationalise le processus de construction d'images.

## Découpage du workflow

Voici un découpage du workflow :

### Déclencher le workflow :

```yaml
on:
  push:
    branches:
      - main
  pull_request_target:
    branches:
      - main
```

Le workflow est déclenché à chaque fois qu'il y a un push sur la branche main ou une pull request vers la branche main. Vous pouvez personnaliser les conditions de déclenchement en fonction de vos besoins spécifiques.

### Définir les variables d'environnement :

```yaml
env:
  BUILDER: "heroku/builder:22"
  IMG_NAME: 'personal-portfolio'
  USERNAME: "caesarsage"
```

Cette section définit les variables d'environnement qui seront utilisées tout au long du workflow.

La variable `BUILDER` spécifie l'image Docker qui sera utilisée pour construire l'application. La variable `IMG_NAME` spécifie le nom de l'image Docker qui sera construite et publiée. La variable `USERNAME` spécifie votre nom d'utilisateur Docker Hub.

### Cloner le dépôt :

```yaml
jobs:
  version:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
```

Cette section définit un job appelé "version" qui s'exécute sur un environnement Ubuntu. L'action `actions/checkout@v2` est utilisée pour cloner le code depuis le dépôt GitHub. Cette étape nous permet d'accéder au code source de l'application pour construire l'image Docker.

### Définir le nom de l'application :

```yaml
dockerhub_remote_build:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v2
        
    - name: Set App Name
      run: 'echo "IMG_NAME=$(echo ${USERNAME})/$(echo ${IMG_NAME})" >> $GITHUB_ENV'
```

Cette section définit la variable d'environnement `IMG_NAME`, qui inclut le nom d'utilisateur Docker Hub et le nom de l'image souhaité.

Le job `dockerhub_remote_build` s'exécute sur un environnement Ubuntu et utilise l'action `actions/checkout@v2` pour cloner le code. L'étape `run` définit la variable `IMG_NAME` en utilisant le nom d'utilisateur Docker Hub et le nom de l'image fournis.

### Se connecter à Docker Hub :

```yaml
- name: login
  uses: docker/login-action@v1
  with:
    username: ${{ env.USERNAME }}
    password: ${{ secrets.DOCKER_PASSWORD }}
```

Cette étape se connecte à Docker Hub en utilisant le nom d'utilisateur et le mot de passe Docker Hub fournis.

L'action `docker/login-action@v1` est utilisée pour authentifier le workflow avec Docker Hub. Le nom d'utilisateur Docker Hub est pris depuis la variable `env.USERNAME`, et le mot de passe est stocké de manière sécurisée dans les secrets du dépôt.

### Construire l'image Docker avec Pack CLI :

```yaml
- name: Pack Remote Build
  uses: dfreilich/pack-action@v2.1.1
  with:
    args: 'build ${{ env.IMG_NAME }} --builder ${{ env.BUILDER }} --publish'
```

Voici la partie principale du workflow. Cette étape utilise l'action `dfreilich/pack-action@v2.1.1`, qui est une action GitHub pour exécuter des commandes Pack CLI.

Le paramètre `args` spécifie la commande Pack CLI pour construire l'image Docker. La variable `env.IMG_NAME` est utilisée pour spécifier le nom de l'image, et la variable `env.BUILDER` définit l'image de construction à utiliser. Le flag `--publish` indique à Pack CLI de publier l'image construite sur Docker Hub.

### Tester l'application :

```yaml
- name: Test App
  run: |
    docker run -d -p 8080:8080 --name personal-portfolio ${{ env.IMG_NAME }}
    sleep 30s
    curl --request GET --url http://localhost:8080
```

Cette étape exécute l'image Docker qui a été construite et publiée dans l'étape précédente.

Elle démarre le conteneur en mode détaché (`-d` flag) et mappe le port 8080 de l'hôte au port 8080 du conteneur. Ensuite, elle attend 30 secondes (`sleep 30s`) pour permettre à l'application de démarrer. Enfin, elle effectue une simple requête HTTP GET à l'application en utilisant `curl` pour tester si elle fonctionne comme prévu.

### Rebaser l'image Docker :

```yaml
- name: Pack Rebase
  uses: dfreilich/pack-action@v2.1.1
  with:
    args: 'rebase ${{ env.IMG_NAME }}'
```

Pour s'assurer que l'image Docker est reproductible et mise à jour, cette étape utilise la commande `rebase` de Pack CLI pour rebaser l'image.

Ce processus aide à incorporer les changements ou mises à jour qui pourraient avoir eu lieu dans l'image de base ou les dépendances, rendant l'image plus maintenable à long terme.

### Inspecter l'image Docker :

```yaml
- name: Inspect Image
  uses: dfreilich/pack-action@v2.1.1
  with:
    args: 'inspect-image ${{ env.IMG_NAME }}'
```

Cette étape utilise la commande `inspect-image` de Pack CLI pour recueillir des informations détaillées sur l'image Docker. Elle fournit des informations sur les couches de l'image, les métadonnées et autres détails pertinents.

Cette inspection peut être utile pour le dépannage, l'optimisation de la taille de l'image et pour s'assurer que l'image est construite correctement.

### Nettoyage

```yaml
- name: Clean Up
  run: |
    docker container stop 'personal-portfolio'
```

Pour assurer une bonne gestion des ressources, cette étape arrête le conteneur Docker qui a été démarré dans la phase de test précédente. Elle arrête le conteneur nommé 'personal-portfolio' en utilisant la commande `docker container stop`.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/docker-hub.png)

## Workflow complet

Pour voir le workflow complet avec toutes les étapes définies, y compris leurs configurations, vous pouvez vous référer au fichier [main-pack-cli.yaml.yml](https://chat.openai.com/c/.github/workflows/main-pack-cli.yaml.yml) dans le dépôt.

## Conclusion

Avec Pack CLI et les Cloud Native Buildpacks, la construction et la publication d'images Docker deviennent plus simples et plus efficaces. En éliminant le besoin d'écrire des Dockerfiles, le processus est rationalisé, réduisant la complexité et les erreurs potentielles.

Dans ce tutoriel, nous avons exploré un workflow étape par étape qui démontre la puissance de Pack CLI dans la simplification de la gestion des images Docker. En suivant ce workflow, vous pouvez facilement adapter le processus à vos propres projets, accélérant ainsi votre processus de construction et de publication d'images Docker.

J'espère que cette explication vous aide à comprendre le code et le workflow plus en détail.