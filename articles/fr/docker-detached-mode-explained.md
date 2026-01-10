---
title: Mode détaché de Docker expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-05T19:55:00.000Z'
originalURL: https://freecodecamp.org/news/docker-detached-mode-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e2d740569d1a4ca3bc1.jpg
tags:
- name: Docker
  slug: docker
seo_title: Mode détaché de Docker expliqué
seo_desc: 'Docker detached mode

  Detached mode, shown by the option --detach or -d, means that a Docker container
  runs in the background of your terminal. It does not receive input or display output.

  docker run -d IMAGE


  If you run containers in the background, ...'
---

## **Mode détaché de Docker**

Le mode détaché, indiqué par l'option `--detach` ou `-d`, signifie qu'un conteneur Docker s'exécute en arrière-plan de votre terminal. Il ne reçoit pas d'entrée ni n'affiche de sortie.

```text
docker run -d IMAGE
```

Si vous exécutez des conteneurs en arrière-plan, vous pouvez obtenir leurs détails en utilisant `docker ps` et ensuite réattacher votre terminal à leur entrée et sortie.

#### **Plus d'informations :**

* [Se connecter et se détacher d'un conteneur en cours d'exécution | Documentation Docker](https://docs.docker.com/engine/reference/commandline/attach/#examples)
* [Mode détaché vs avant-plan | Documentation Docker](https://docs.docker.com/engine/reference/run/#detached-vs-foreground)

## Plus d'informations sur Docker

Docker est une plateforme ouverte pour construire, livrer et exécuter des applications distribuées. Il est écrit en Go. Il a été publié pour la première fois en 2013 et est développé par Docker, Inc.

Docker est utilisé pour exécuter des packages appelés « conteneurs ». Les conteneurs sont isolés les uns des autres et du système d'exploitation. Ils sont plus légers que les machines virtuelles car ils n'utilisent pas la machine hôte pour exécuter un système d'exploitation.

La conteneurisation, qui est une manière de déployer et d'exécuter des applications, exécute des services isolés qui s'exécutent nativement sur le noyau Linux. La mémoire peut être définie manuellement pour chaque conteneur dans Docker.

Docker est utilisé pour simplifier les configurations et assurer un flux continu d'intégration et de déploiement. Des conteneurs spécifiques peuvent être spécifiés pour les environnements de développement, de préproduction et de production. Une véritable implémentation d'un conteneur en production, selon le manuel Docker, est de l'exécuter en tant que service, en utilisant le fichier `docker-compose.yml` pour l'installation. Il s'agit d'un fichier YAML qui définit comment les conteneurs Docker doivent se comporter en production.

L'un des plus grands avantages de Docker est qu'il peut être utilisé par une équipe utilisant différents systèmes d'exploitation pour construire des projets sans avoir à se soucier des conflits logiciels.

### **Installation**

* Ubuntu : `sudo apt install docker`
* RedHat : `yum install docker-ce`
* Windows / macOS : [Télécharger](https://www.docker.com/get-started)
* Linux :

```text
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

#### **Plus d'informations :**

* Pour le téléchargement et la documentation, consultez le site officiel de Docker : [Site officiel de Docker](https://www.docker.com/)