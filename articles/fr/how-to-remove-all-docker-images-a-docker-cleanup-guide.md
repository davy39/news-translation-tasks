---
title: Comment supprimer toutes les images Docker – Un guide de nettoyage Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-14T20:25:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-all-docker-images-a-docker-cleanup-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/docker-cleanup-guide.png
tags:
- name: Docker
  slug: docker
- name: docker image
  slug: docker-image
seo_title: Comment supprimer toutes les images Docker – Un guide de nettoyage Docker
seo_desc: "By Sebastian Sigl\nContainers are everywhere in today’s tech world. The\
  \ most popular technology for container management is Docker. It makes using containers\
  \ easy and helps you easily get applications up and running. \nUnfortunately, this\
  \ can take a lo..."
---

Par Sebastian Sigl

Les conteneurs sont partout dans le monde technologique d'aujourd'hui. La technologie la plus populaire pour la gestion des conteneurs est [Docker](https://www.docker.com/). Elle facilite l'utilisation des conteneurs et vous aide à déployer et à faire fonctionner facilement des applications.

Malheureusement, cela peut consommer beaucoup d'espace disque, et vous finirez par vous retrouver avec un disque plein.

Peu importe que vous utilisiez Docker sur votre appareil ou sur un serveur. Ce guide vous montre comment analyser l'espace disque utilisé et comment nettoyer les différentes ressources Docker.

Tout ce dont vous avez besoin est un démon Docker en cours d'exécution et un terminal.

## Comment analyser l'espace utilisé par Docker

Vous pouvez vérifier l'espace utilisé en exécutant la commande suivante :

```sh
$ docker system df

TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          61        16        21.1GB    15.25GB (72%)
Containers      69        0         12.26MB   12.26MB (100%)
Local Volumes   3         2         539.1MB   50.04MB (9%)
Build Cache     76        0         1.242GB   1.242GB
```

Vous pouvez obtenir plus d'informations en utilisant l'option verbeuse `-v` :

```sh
$ docker system df -v

REPOSITORY        TAG   IMAGE ID     CREATED       SIZE      SHARED 
teamatldocker/jira    e50b8390945c   4 weeks ago     842.3MB   0B       
vw                    ed9e125a8925   2 months ago    1.659GB   134.8MB 

Containers space usage:

CONTAINER ID   IMAGE                    COMMAND                   SIZE 
94e03a4a17d0   teamatldocker/jira       "/sbin/tini -- /usr/…"    1.4MB 

Local Volumes space usage:

VOLUME NAME                     LINKS     SIZE
play-with-jira_postgresqldata   1         84.19MB   
play-with-jira_jiradata         1         404.8MB

Build cache usage: 1.242GB

CACHE ID       CACHE TYPE     SIZE      CREATED        LAST USED 
oxil5sdicb91   regular        135MB     2 months ago   2 months ago  
kxz13fmdbodg   regular        13B       2 months ago   2 months ago 
nysus21ej7pf   regular        0B        2 months ago   2 months ago
```

Comme vous pouvez le voir, vous obtenez des informations sur :

* L'utilisation de l'espace par les images,
* L'utilisation de l'espace par les conteneurs,
* L'utilisation de l'espace par les volumes locaux, et
* L'utilisation du cache de construction.

## Comment tout nettoyer dans Docker

Vous pouvez tout nettoyer ou nettoyer des ressources spécifiques dans Docker comme les images, les volumes de conteneurs ou le cache de construction.

Pour nettoyer autant que possible, en excluant les composants en cours d'utilisation, exécutez cette commande :

```sh
$ docker system prune -a
```

`-a` inclut les conteneurs inutilisés et en suspens. Ne pas fournir `-a` ne supprimerait que les images en suspens, qui sont des images sans étiquette n'ayant aucun lien avec d'autres images.

Si vous souhaitez nettoyer la plupart des ressources Docker tout en conservant les images étiquetées, vous pouvez exécuter cette commande :

```sh
$ docker system prune
```

C'est tout ce dont vous avez besoin pour libérer rapidement de l'espace disque. De plus, vous pouvez nettoyer les composants séparément.

Voici quelques autres commandes utiles :

### Nettoyer les images inutilisées et en suspens

```sh
$ docker image prune
```

### Nettoyer uniquement les images en suspens

```sh
$ docker image prune -a
```

### Nettoyer les conteneurs arrêtés

```sh
$ docker container prune
```

### Nettoyer les volumes inutilisés

```sh
$ docker volume prune
```

## Comment gérer efficacement et en continu votre espace Docker utilisé

Vous pouvez exécuter une commande quotidiennement ou au démarrage. Pour ignorer l'invite habituelle, vous devez ajouter `-f` à la commande que vous souhaitez exécuter automatiquement.

Gardez à l'esprit que cela vous obligera à télécharger des images beaucoup plus souvent car vous supprimez régulièrement les ressources Docker.

Si vous n'avez pas de problème d'espace disque, ne vous inquiétez pas. Nettoyez simplement les choses dès qu'une utilisation intensive du disque par Docker attire votre attention.

## Conclusion

Aujourd'hui, il existe de nombreuses façons de nettoyer l'espace disque de Docker en utilisant la commande `docker`. Vous pouvez même exécuter ces commandes automatiquement si vous souhaitez nettoyer les ressources Docker régulièrement.

J'espère que vous avez apprécié cet article.

Si vous l'avez aimé et que vous avez envie de m'applaudir ou si vous voulez simplement me contacter, [suivez-moi sur Twitter](https://twitter.com/sesigl).

Je travaille chez eBay Kleinanzeigen, l'une des plus grandes entreprises de petites annonces au monde. D'ailleurs, [nous recrutons](https://jobs.ebayclassifiedsgroup.com/ebay-kleinanzeigen) !