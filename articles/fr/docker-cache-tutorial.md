---
title: Cache Docker – Comment effectuer une reconstruction propre de l'image et vider
  le cache de Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-28T18:51:57.000Z'
originalURL: https://freecodecamp.org/news/docker-cache-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/docker-cache-guide.png
tags:
- name: cache
  slug: cache
- name: containers
  slug: containers
- name: Docker
  slug: docker
seo_title: Cache Docker – Comment effectuer une reconstruction propre de l'image et
  vider le cache de Docker
seo_desc: "By Sebastian Sigl\nContainers enable you to package your application in\
  \ a portable way that can run in many environments. The most popular container platform\
  \ is Docker. \nThis tutorial will explain how to use the Docker build cache to your\
  \ advantage.\nD..."
---

Par Sebastian Sigl

Les conteneurs vous permettent d'empaqueter votre application de manière portable afin qu'elle puisse s'exécuter dans de nombreux environnements. La plateforme de conteneurs la plus populaire est [Docker](https://www.docker.com/). 

Ce tutoriel expliquera comment utiliser le cache de build Docker à votre avantage.

## Cache de build Docker

La construction d'images doit être rapide, efficace et fiable. Le concept d'images Docker repose sur des couches immuables. Chaque commande que vous exécutez produit une nouvelle couche qui contient les modifications par rapport à la couche précédente. 

Toutes les couches précédemment construites sont mises en cache et peuvent être réutilisées. Cependant, si votre installation dépend de ressources externes, le cache Docker peut causer des problèmes.

## Comment tirer parti du cache de build Docker

Pour comprendre les problèmes de cache de build Docker, construisons une application Docker [nginx](https://nginx.org/en/) personnalisée simple. Avant de construire l'image, créez un Dockerfile qui met à jour les bibliothèques et ajoute une page d'accueil personnalisée :

```dockerfile
FROM nginx:1.21.6

# Mettre à jour tous les paquets
RUN apt-get update && apt-get -y upgrade

# Utiliser une page d'accueil personnalisée
RUN echo '<html><bod>My Custom Startpage</body></html>' > /usr/share/nginx/html/index.html
```

Vous pouvez maintenant construire l'image Docker :

```shell
$  docker build -t my-custom-nginx .

=> [1/3] FROM docker.io/library/nginx:1.21.6@sha256:e12...  5.8s
=> [2/3] RUN apt-get update && apt-get -y upgrade           3.6s
=> [3/3] RUN echo '<html><bod>My Custom Startpage...        0.2s

=> exporting to image                                       0.1s
=> exporting layers                                         0.1s
=> writing image                                            0.0s
=> naming to docker.io/library/my-custom-nginx

[+] Building 11.3s (7/7) FINISHED
```

Dans cet exemple, j'ai supprimé une partie de la sortie pour plus de lisibilité. Si vous construisez l'image pour la première fois, vous verrez que cela prend un certain temps, dans mon cas `11.3s`. 

Une étape d'exécution longue est `apt-get update && apt-get -y upgrade` selon le nombre de dépendances mises à jour et la vitesse de votre connexion internet. Elle vérifie les mises à jour de paquets sur le système d'exploitation et les installe si elles sont disponibles.

Maintenant, exécutez-la à nouveau, et vous bénéficierez du cache de build Docker :

```shell
$ docker build -t my-custom-nginx .

=> [1/3] FROM docker.io/library/nginx:1.21.6@sha256:e1211ac1…   0.0s
=> CACHED [2/3] RUN apt-get update && apt-get -y upgrade        0.0s
=> CACHED [3/3] RUN echo '<html><bod>My Custom Startpage...     0.0s

=> exporting to image                                           0.0s
=> exporting layers                                             0.0s
=> writing image                                                0.0s
=> naming to docker.io/library/my-custom-nginx

Building 1.1s (7/7) FINISHED
```

Cette fois, la construction de l'image est très rapide car elle peut réutiliser toutes les images précédemment construites. Lorsque vous personnalisez votre page d'accueil dans le Dockerfile, vous voyez comment le comportement de mise en cache est affecté :

```dockerfile
FROM nginx:1.21.6

# Mettre à jour tous les paquets
RUN apt-get update && apt-get -y upgrade

# Utiliser une page d'accueil personnalisée
RUN echo '<html><bod>New Startpage</body></html>' > /usr/share/nginx/html/index.html
```

Maintenant, construisez à nouveau l'image :

```shell
$ docker build -t my-custom-nginx .

=> [1/3] FROM docker.io/library/nginx:1.21.6@sha256:e1211ac1…   0.0s
=> CACHED [2/3] RUN apt-get update && apt-get -y upgrade        0.0s
=> [3/3] RUN echo '<html><bod>My Custom Startpage...            0.2s

=> exporting to image                                           0.0s
=> exporting layers                                             0.0s
=> writing image                                                0.0s
=> naming to docker.io/library/my-custom-nginx

Building 2.1s (7/7) FINISHED
```

Cette fois, il n'a reconstruit que la dernière couche car il a reconnu que la commande `RUN` avait changé. Mais il a réutilisé la deuxième étape de construction intensive et n'a pas mis à jour les dépendances du système d'exploitation.

Le comportement de mise en cache est intelligent. Dès qu'une étape doit être reconstruite, chaque étape suivante est reconstruite à nouveau. Par conséquent, il est préférable de placer les parties qui changent fréquemment à la fin d'un `Dockerfile` pour réutiliser les couches de construction précédentes.

Pourtant, vous voudrez peut-être forcer la reconstruction d'une couche mise en cache pour forcer une mise à jour de paquet. Forcer une reconstruction peut être nécessaire parce que vous voulez garder votre application sécurisée et utiliser les dernières mises à jour lorsqu'elles sont disponibles.

## Comment utiliser l'option --no-cache de Docker build

Il peut y avoir différentes raisons de désactiver le cache de build. Vous pouvez reconstruire l'image à partir de l'image de base sans utiliser les couches mises en cache en utilisant l'option `--no-cache`.

```shell
$ docker build -t my-custom-nginx .

=> CACHED [1/3] FROM docker.io/library/nginx:1.21.6@sha256:...  0.0s
=> [2/3] RUN apt-get update && apt-get -y upgrade               3.5s
=> [3/3] RUN echo '<html><bod>My Custom Startpage...            0.2s

=> exporting to image                                           0.1s
=> exporting layers                                             0.0s
=> writing image                                                0.0s
=> naming to docker.io/library/my-custom-nginx

Building 5.5s (7/7) FINISHED
```

De nouvelles couches ont été construites et utilisées. Le `docker build` exécute les deux commandes cette fois-ci, ce qui correspond à une approche du tout ou rien. Soit vous fournissez l'option `--no-cache` qui exécute toutes les commandes, soit vous mettrez en cache autant que possible.

## Comment utiliser les arguments Docker pour l'invalidation du cache (Cache-Busting)

Une autre option permet de fournir un petit point de départ dans le Dockerfile. Vous devez modifier votre Dockerfile comme ceci :

```dockerfile
FROM nginx:1.21.6

# Mettre à jour tous les paquets
RUN apt-get update && apt-get -y upgrade

# Invalidation personnalisée du cache
ARG CACHEBUST=1

# Utiliser une page d'accueil personnalisée
RUN echo '<html><bod>New Startpage</body></html>' > /usr/share/nginx/html/index.html
```

Vous ajoutez un argument `CACHEBUST` à votre Dockerfile à l'endroit où vous souhaitez imposer une reconstruction. Maintenant, vous pouvez construire l'image Docker et fournir une valeur toujours différente qui provoque la réexécution de toutes les commandes suivantes :

```shell
$ docker build -t my-custom-nginx --build-arg CACHEBUST=$(date +%s) .

=> [1/3] FROM docker.io/library/nginx:1.21.6@sha256:e1211ac1...    0.0s
=> CACHED [2/3] RUN apt-get update && apt-get -y upgrade           0.0s
=> [3/3] RUN echo '<html><bod>My Custom Startpage...               0.3s

=> exporting to image                                              0.0s
=> exporting layers                                                0.0s
=> writing image                                                   0.0s
=> naming to docker.io/library/my-custom-nginx

Building 1.0s (7/7) FINISHED
```

En fournissant `--build-arg CACHEBUST=$(date +%s)`, vous définissez le paramètre sur une valeur toujours différente qui provoque la reconstruction de toutes les couches suivantes.

## Résumé

Le cache de build de Docker est une fonctionnalité pratique. Il accélère les constructions Docker grâce à la réutilisation des couches précédemment créées. 

Vous pouvez utiliser l'option `--no-cache` pour désactiver la mise en cache ou utiliser un argument de build Docker personnalisé pour imposer la reconstruction à partir d'une certaine étape.

Comprendre le cache de build Docker est puissant et vous rendra plus efficace dans la construction de votre conteneur Docker.

J'espère que vous avez apprécié cet article.

Si vous l'avez aimé et que vous ressentez le besoin de m'applaudir ou si vous voulez simplement me contacter, [suivez-moi sur Twitter](https://twitter.com/sesigl).

Je travaille chez eBay Kleinanzeigen, l'une des plus grandes entreprises de petites annonces au monde. D'ailleurs, [nous recrutons](http://ebay-kleinanzeigen.de/careers) !

## Références

* [Instruction Docker arg](https://www.geeksforgeeks.org/docker-arg-instruction/)
* [Stackoverflow : Désactiver le cache pour des commandes RUN spécifiques](https://stackoverflow.com/questions/35134713/disable-cache-for-specific-run-commands)
* [Baeldung : Comment fonctionne le cache de build Docker et quand ne pas l'utiliser](https://www.baeldung.com/linux/docker-build-cache)