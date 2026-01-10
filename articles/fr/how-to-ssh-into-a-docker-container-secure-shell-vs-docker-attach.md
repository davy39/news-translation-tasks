---
title: Comment accéder en SSH à un conteneur Docker – Secure Shell vs Docker Attach
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-24T19:47:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-ssh-into-a-docker-container-secure-shell-vs-docker-attach
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/ssh-into-docker-container-image-1.png
tags:
- name: Docker
  slug: docker
- name: ssh
  slug: ssh
seo_title: Comment accéder en SSH à un conteneur Docker – Secure Shell vs Docker Attach
seo_desc: "By Sebastian Sigl\nContainers are the bread and butter for running applications\
  \ today. And the most popular container technology is called Docker. \nKnowing how\
  \ to SSH into a container is essential to using, debugging, and operating containers\
  \ on your ..."
---

Par Sebastian Sigl

Les conteneurs sont la base de l'exécution des applications aujourd'hui. Et la technologie de conteneurs la plus populaire s'appelle [Docker](https://www.docker.com/). 

Savoir comment se connecter en SSH à un conteneur est essentiel pour utiliser, déboguer et faire fonctionner des conteneurs sur votre système d'exploitation local ou sur une installation distante. 

Cet article décrira différentes méthodes pour y parvenir ainsi que leurs contraintes.

## Méthode 1 – S'attacher à un conteneur en cours d'exécution via `docker exec`

La commande la plus courante et la plus utile pour obtenir un shell dans un conteneur est `docker exec -it`. Elle exécute une nouvelle commande dans le conteneur, ce qui vous permet de démarrer un nouveau shell interactif :

```sh
# démarrer un conteneur
$ docker run --name nginx --rm -p 8080:80  -d nginx

# créer et se connecter à un shell bash dans le conteneur
$ docker exec -it nginx bash

root@a84ad71521b1:/#
```

Vous pouvez quitter le shell actuel en appuyant sur `control + d` ou en tapant `exit`.

Cela fonctionne parce que :

* `docker exec` exécute une nouvelle commande,
* `-i` ajoute un flux stdin,
* `-t` ajoute un pilote de terminal,
* `-it` combine `-i` et `-t`, ce qui vous permet d'interagir avec le processus.

‌‌Il peut arriver que bash ne soit pas installé dans votre conteneur. Si vous ne pouvez pas démarrer bash, vous pouvez essayer de démarrer un shell `sh` :

```sh
docker exec -it nginx sh
```

‌‌De plus, il se peut qu'aucun shell ne soit installé dans le conteneur. Par conséquent, il n'y a aucun moyen d'obtenir un shell dans ce conteneur dans un univers Docker classique et vous ne pouvez démarrer aucun shell.‌‌

Selon votre outil d'orchestration de conteneurs, vous pourriez toujours être en mesure d'accéder au conteneur. Par exemple, les [conteneurs distroless](https://github.com/GoogleContainerTools/distroless) deviennent de plus en plus populaires pour réduire l'empreinte du conteneur. Si vous utilisez Kubernetes, une fonctionnalité de [conteneur éphémère](https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/) vous permet de déboguer des conteneurs sans shell ainsi que des conteneurs ayant planté.

## Méthode 2 – S'attacher à un conteneur en cours d'exécution via `docker attach`

> La commande `docker attach` attache l'entrée, la sortie et l'erreur standard de votre terminal à un conteneur en cours d'exécution en utilisant l'ID ou le nom du conteneur. (Source [docker.com](https://docs.docker.com/engine/reference/commandline/attach/))

En pratique, cela signifie que tout ce que vous saisissez est transmis au conteneur, et tout ce qui est affiché apparaîtra dans votre console.

Maintenant, vous vous attachez au conteneur en cours d'exécution :

```sh
$ docker attach nginx                              

172.17.0.1 - - [18/Mar/2022:08:37:14 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36" "-"

```

Pendant l'exécution, vous pouvez ouvrir [http://localhost:8080](http://localhost:8080). Comme le conteneur affiche les logs d'accès à chaque page ouverte, vous verrez la sortie dans votre terminal.

De plus, l'entrée est également transmise au conteneur. Donc, si vous appuyez sur `control + c`, ce qui déclenche un signal d'arrêt, votre conteneur s'arrêtera.

```sh
$ docker attach nginx                              
172.17.0.1 - - [18/Mar/2022:08:37:14 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36" "-"
^[[A^C2022/03/18 08:39:50 [notice] 1#1: signal 2 (SIGINT) received, exiting
2022/03/18 08:39:50 [notice] 32#32: exiting

```

Se détacher peut être délicat car `control + c` est également utilisé pour le détachement. Pour pouvoir vous détacher sans arrêter le conteneur, vous pouvez vous attacher au conteneur en désactivant le transfert des signaux :

```sh
# démarrer à nouveau le conteneur
docker run --name nginx --rm -p 8080:80  -d nginx

# s'attacher sans relayer les signaux
docker attach --sig-proxy=false nginx
```

## Conclusion

Pour vous connecter à un conteneur en utilisant des commandes Docker classiques, vous pouvez utiliser `docker exec` et `docker attach`.

`docker exec` est beaucoup plus populaire car vous pouvez exécuter une nouvelle commande qui vous permet de lancer un nouveau shell. Vous pouvez vérifier les processus, les fichiers et opérer comme dans votre environnement local.

`docker attach` est plus limité car il attache l'entrée, la sortie et l'erreur standard de votre terminal au processus principal d'un conteneur en cours d'exécution.

J'espère que vous avez apprécié cet article.

Si vous l'avez aimé et que vous ressentez le besoin de m'applaudir ou si vous voulez simplement me contacter, [suivez-moi sur Twitter](https://twitter.com/sesigl).

Je travaille chez eBay Kleinanzeigen, l'une des plus grandes entreprises de petites annonces au monde. D'ailleurs, [nous recrutons](https://jobs.ebayclassifiedsgroup.com/ebay-kleinanzeigen) !

### Références

* [How to SSH into a Running Docker Container and Run Commands](https://phoenixnap.com/kb/how-to-ssh-into-docker-container)
* [How to Detach From a Docker Container Without Stopping It](https://www.cloudsavvyit.com/14226/how-to-detach-from-a-docker-container-without-stopping-it/#:~:text=Docker%20supports%20a%20keyboard%20combination,alive%2C%20keeping%20your%20container%20running.)
* [Docker attach documentation](https://docs.docker.com/engine/reference/commandline/attach/)
* [Docker exec documentation](https://docs.docker.com/engine/reference/commandline/exec/)