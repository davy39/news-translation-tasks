---
title: Conteneurs de données Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-05T18:05:19.000Z'
originalURL: https://freecodecamp.org/news/docker-data-containers
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/1_AUiK5PwnsPG_xaT9jcVoSA-2.jpeg
tags:
- name: containerization
  slug: containerization
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: Docker Containers
  slug: docker-containers
seo_title: Conteneurs de données Docker
seo_desc: 'By Faizan Bashir

  There is more than one way to manage data in Docker container. Say hello to the
  Data Containers.

  Simply put data containers are containers whose job is just to store/manage data.

  Similar to other containers they are managed by the ho...'
---

Par Faizan Bashir

Il existe plusieurs façons de gérer les données dans un conteneur Docker. Dites bonjour aux conteneurs de données.

En termes simples, les conteneurs de données sont des conteneurs dont le rôle est simplement de stocker/gérer des données.

Comme les autres conteneurs, ils sont gérés par le système hôte. Cependant, ils n'apparaissent pas lorsque vous exécutez la commande `docker ps`.

Pour créer un conteneur de données, nous créons d'abord un conteneur avec un nom bien connu pour référence future. Nous utilisons _busybox_ comme base car il est petit et léger au cas où nous souhaiterions explorer et déplacer le conteneur vers un autre hôte.

Lors de la création du conteneur, nous fournissons également une option de volume `-v` pour définir où les autres conteneurs liront/écriront les données.

```
$ docker create -v /config --name dataContainer busybox
```

Avec le conteneur en place, nous pouvons maintenant copier des fichiers depuis notre répertoire client local dans le conteneur.

Pour copier des fichiers dans un conteneur, vous utilisez la commande `docker cp`. La commande suivante copiera le fichier _config.conf_ dans le répertoire _config_ de _dataContainer_.

```
$ docker cp config.conf dataContainer:/config/
```

Maintenant que notre conteneur de données contient notre configuration, nous pouvons référencer le conteneur lorsque nous lançons des conteneurs dépendants nécessitant le fichier de configuration.

En utilisant l'option magique `--volumes-from <container>`, nous pouvons utiliser les volumes montés d'autres conteneurs à l'intérieur du conteneur en cours de lancement. Dans ce cas, nous lancerons un conteneur Ubuntu qui a une référence à notre conteneur de données. Lorsque nous listons le répertoire config, il affichera les fichiers du conteneur attaché.

```
$ docker run --volumes-from dataContainer ubuntu ls/config
```

Si un répertoire _/config_ existait déjà, alors les volumes-from le remplaceraient et seraient le répertoire utilisé. Vous pouvez mapper plusieurs volumes à un conteneur.

---

### **Importer et exporter les données du conteneur**

Les données peuvent être importées et exportées depuis un conteneur, en utilisant la commande `docker export`.

Nous pouvons déplacer le conteneur de données vers une autre machine simplement en l'exportant vers un fichier .tar.

```
$ docker export dataContainer > dataContainer.tar
```

De même, nous pouvons importer le conteneur de données dans Docker.

```
$ docker import dataContainer.tar
```