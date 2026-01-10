---
title: Volume de Montage Docker – Comment Monter un Répertoire Local
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-04T20:08:50.000Z'
originalURL: https://freecodecamp.org/news/docker-mount-volume-guide-how-to-mount-a-local-directory
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/Docker-mount-volume-guide.png
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
seo_title: Volume de Montage Docker – Comment Monter un Répertoire Local
seo_desc: "By Sebastian Sigl\nContainers make software engineering easier and more\
  \ efficient, and Docker containers are popular and easy to use. \nContainers are\
  \ essential for local development. They let you test-run your applications in local\
  \ environments and st..."
---

Par Sebastian Sigl

Les conteneurs rendent l'ingénierie logicielle plus facile et plus efficace, et les conteneurs [Docker](https://www.docker.com/) sont populaires et faciles à utiliser. 

Les conteneurs sont essentiels pour le développement local. Ils vous permettent de tester vos applications dans des environnements locaux et de commencer à construire l'infrastructure requise.

Les conteneurs Docker sont immutables par nature. Cela signifie que le redémarrage d'un conteneur efface toutes vos données stockées dans le conteneur. Mais Docker fournit des volumes et des montages de liaison, qui sont deux mécanismes pour persister les données dans votre conteneur Docker.

Ce tutoriel vous apprendra à lier des répertoires locaux à votre conteneur Docker et à utiliser des volumes gérés par Docker en alternative. Connaître les deux vous permet d'utiliser les conteneurs Docker pour de nombreux autres cas d'utilisation qui peuvent augmenter votre productivité.

## Comment Monter des Répertoires Locaux en utilisant `docker run -v`

> La commande `docker run` crée d'abord une couche de conteneur modifiable sur l'image spécifiée, puis commence à utiliser la commande spécifiée. (Source [docker.com](https://www.bing.com/search?form=MOZLBR&ptag=MOZZ0000000011&pc=MOZD&q=docker+run+))

L'utilisation du paramètre `-v` vous permet de lier un répertoire local.

`-v` ou `--volume` vous permet de monter des répertoires et fichiers locaux dans votre conteneur. Par exemple, vous pouvez démarrer une base de données MySQL et monter le répertoire de données pour stocker les données réelles dans votre répertoire monté.

```shell
# exécuter le conteneur mysql en arrière-plan

$ docker run --name mysql-db -v $(pwd)/datadir:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:8.0.28-debian

# afficher le contenu du répertoire de données
$ ls -la datadir
total 383848
-rw-r-----    1 sebarthel  staff    196608 Mar 26 22:47 #ib_16384_0.dblwr
-rw-r-----    1 sebarthel  staff   8585216 Mar 26 22:47 #ib_16384_1.dblwr
drwxr-x---   12    sebarthel  staff       384 Mar 26 22:47 #innodb_temp
drwxr-xr-x@  27 sebarthel  staff       864 Mar 26 22:47 .
drwxr-xr-x    3 sebarthel  staff        96 Mar 26 22:47 ..
-rw-r-----    1 sebarthel  staff        56 Mar 26 22:47 auto.cnf
-rw-r-----    1 sebarthel  staff       913 Mar 26 22:47 binlog.000001
(plus de répertoires)

# arrêter le conteneur mysql
docker rm -f mysql-db
```

La liaison d'un répertoire est une synchronisation bidirectionnelle. Chaque fichier que vous modifiez sur l'hôte est modifié dans le conteneur, et chaque fichier qui est modifié dans le conteneur est modifié sur l'hôte. Ainsi, si vous arrêtez et redémarrez la base de données, vous pouvez monter le même répertoire, et votre configuration et vos données stockées seront disponibles.

Les avantages de cette méthode sont qu'elle est simple à utiliser et facile d'accès. Vous devriez utiliser la liaison de répertoires locaux pour les fichiers que vous souhaitez modifier ou observer sur l'hôte, comme les fichiers de configuration et les fichiers journaux.

## Comment Utiliser les Volumes Docker pour Persister les Modifications

Au lieu de lier votre répertoire local, vous pouvez utiliser des volumes Docker. Un volume Docker est un répertoire quelque part dans votre répertoire de stockage Docker et peut être monté sur un ou plusieurs conteneurs. Ils sont entièrement gérés et ne dépendent pas de certaines spécificités du système d'exploitation.

Créons un volume Docker et montons-le pour persister les données MySQL :

```shell
# créer un volume
docker volume create mysql-data

# exécuter le conteneur mysql en arrière-plan
$ docker run --name mysql-db -v mysql-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:latest

# arrêter le conteneur mysql
docker rm -f mysql-db

# supprimer le volume
docker volume remove mysql-data
```

Avant de supprimer le volume Docker, vous pouvez ouvrir votre interface graphique Docker et inspecter le volume en cliquant sur l'onglet `data`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/docker-ui-volume.png)

Vous voyez les fichiers, mais ils sont isolés dans un volume Docker. Il est recommandé de les utiliser pour persister les fichiers que vous n'avez pas besoin d'observer ou de modifier depuis votre système hôte. Cette méthode est connue pour avoir de meilleures performances que les liaisons de répertoires locaux.

# Résumé

Les conteneurs Docker deviennent plus puissants lorsque vous savez comment persister vos données et ne pas les perdre lorsque vous arrêtez un conteneur. 

Vous liez des répertoires locaux et des volumes à un conteneur en fournissant le paramètre Docker run `-v`. Vous devez donner le chemin local absolu ou un nom de volume et le mapper à un répertoire dans le conteneur `-v <source>:<target>`.

J'espère que vous avez apprécié l'article.

Si vous l'avez aimé et que vous avez envie de m'applaudir ou simplement de prendre contact, [suivez-moi sur Twitter](https://twitter.com/sesigl).

Je travaille chez eBay Kleinanzeigen, l'une des plus grandes entreprises de petites annonces au monde. Au fait, [nous recrutons](https://www.ebay-kleinanzeigen.de/careers) !

### Références

* [Comment monter un répertoire dans un conteneur Docker](https://towardsdatascience.com/how-to-mount-a-directory-inside-a-docker-container-4cee379c298b)
* [Image Docker pour MySql](https://hub.docker.com/_/mysql/)
* [Syntaxe Docker-Compose volume ou montage de liaison](https://maximorlov.com/docker-compose-syntax-volume-or-bind-mount/)
* [Comment mettre en pause et reprendre les conteneurs Docker](https://www.thegeekdiary.com/how-to-pause-and-resume-docker-containers/)
* [Volumes Docker vs montages de liaison](https://blog.logrocket.com/docker-volumes-vs-bind-mounts/)
* [Documentation Docker : commande volume create](https://docs.docker.com/engine/reference/commandline/volume_create/)
* [Documentation Docker : Volumes sauvegarde et restauration](https://docs.docker.com/storage/volumes/#backup-restore-or-migrate-data-volumes)
* [Conteneurs Docker sur le bureau](https://blog.jessfraz.com/post/docker-containers-on-the-desktop/)