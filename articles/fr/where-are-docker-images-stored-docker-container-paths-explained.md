---
title: Où sont stockées les images Docker ? Explication des chemins des conteneurs
  Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-06T19:00:00.000Z'
originalURL: https://freecodecamp.org/news/where-are-docker-images-stored-docker-container-paths-explained
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/example-of-examples-word-embeddings_grey.jpg
tags:
- name: containerization
  slug: containerization
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: Kubernetes
  slug: kubernetes
- name: virtualization
  slug: virtualization
seo_title: Où sont stockées les images Docker ? Explication des chemins des conteneurs
  Docker
seo_desc: "By Sebastian Sigl\nDocker has been widely adopted and is used to run and\
  \ scale applications in production. Additionally, it can be used to start applications\
  \ quickly by executing a single Docker command. \nCompanies also are investing more\
  \ and more eff..."
---

Par Sebastian Sigl

Docker a été largement adopté et est utilisé pour exécuter et mettre à l'échelle des applications en production. De plus, il peut être utilisé pour démarrer rapidement des applications en exécutant une seule commande Docker. 

Les entreprises investissent également de plus en plus d'efforts pour améliorer le développement dans des conteneurs Docker locaux et distants, ce qui présente également de nombreux avantages.

Vous pouvez obtenir des informations de base sur votre configuration Docker en exécutant :

```shell
$ docker info

...
 Storage Driver: overlay2
 Docker Root Dir: /var/lib/docker
...

```

La sortie contient des informations sur votre pilote de stockage et votre répertoire racine Docker.

## L'emplacement de stockage des images et des conteneurs Docker

Un conteneur Docker se compose de paramètres réseau, de volumes et d'images. L'emplacement des fichiers Docker dépend de votre système d'exploitation. Voici un aperçu pour les systèmes d'exploitation les plus utilisés :  


* Ubuntu : `/var/lib/docker/`
* Fedora : `/var/lib/docker/`
* Debian : `/var/lib/docker/`
* Windows : `C:\ProgramData\DockerDesktop`
* MacOS : `~/Library/Containers/com.docker.docker/Data/vms/0/`

Sur macOS et Windows, Docker exécute des conteneurs Linux dans un environnement virtuel. Par conséquent, il y a quelques éléments supplémentaires à connaître.

### Docker pour Mac

Docker n'est pas nativement compatible avec macOS, donc [Hyperkit](https://github.com/moby/hyperkit) est utilisé pour exécuter une image virtuelle. Ses données d'image virtuelle sont situées dans :  

`~/Library/Containers/com.docker.docker/Data/vms/0`

Dans l'image virtuelle, le chemin est le chemin Docker par défaut `/var/lib/docker`.

Vous pouvez investiguer votre répertoire racine Docker en créant un shell dans l'environnement virtuel :

```shell
$ screen ~/Library/Containers/com.docker.docker/Data/vms/0/tty 
```

Vous pouvez tuer cette session en appuyant sur **Ctrl+a**, suivi de **k** et **y**.

### Docker pour Windows

Sur Windows, Docker est un peu fragmenté. Il existe des conteneurs Windows natifs qui fonctionnent de manière similaire aux conteneurs Linux. Les conteneurs Linux sont exécutés dans un environnement virtuel minimal basé sur Hyper-V.

La configuration et l'image virtuelle pour exécuter les images Linux sont sauvegardées dans le dossier racine Docker par défaut.

`C:\ProgramData\DockerDesktop`

Si vous inspectez des images régulières, vous obtiendrez des chemins Linux comme :

```shell
$ docker inspect nginx

...
"UpperDir": "/var/lib/docker/overlay2/585...9eb/diff"
...

```

Vous pouvez vous connecter à l'image virtuelle par :

```shell
docker run -it --privileged --pid=host debian nsenter -t 1 -m -u -i sh
```

Là, vous pouvez aller à l'emplacement référencé :

```shell
$ cd /var/lib/docker/overlay2/585...9eb/
$ ls -lah

drwx------    4 root     root        4.0K Feb  6 06:56 .
drwx------   13 root     root        4.0K Feb  6 09:17 ..
drwxr-xr-x    3 root     root        4.0K Feb  6 06:56 diff
-rw-r--r--    1 root     root          26 Feb  6 06:56 link
-rw-r--r--    1 root     root          57 Feb  6 06:56 lower
drwx------    2 root     root        4.0K Feb  6 06:56 work
```

## La structure interne du dossier racine Docker

À l'intérieur de `/var/lib/docker`, différentes informations sont stockées. Par exemple, des données pour les conteneurs, les volumes, les builds, les réseaux et les clusters.

```shell
$ ls -la /var/lib/docker

total 152
drwx--x--x   15 root     root          4096 Feb  1 13:09 .
drwxr-xr-x   13 root     root          4096 Aug  1  2019 ..
drwx------    2 root     root          4096 May 20  2019 builder
drwx------    4 root     root          4096 May 20  2019 buildkit
drwx------    3 root     root          4096 May 20  2019 containerd
drwx------    2 root     root         12288 Feb  3 19:35 containers
drwx------    3 root     root          4096 May 20  2019 image
drwxr-x---    3 root     root          4096 May 20  2019 network
drwx------    6 root     root         77824 Feb  3 19:37 overlay2
drwx------    4 root     root          4096 May 20  2019 plugins
drwx------    2 root     root          4096 Feb  1 13:09 runtimes
drwx------    2 root     root          4096 May 20  2019 swarm
drwx------    2 root     root          4096 Feb  3 19:37 tmp
drwx------    2 root     root          4096 May 20  2019 trust
drwx------   15 root     root         12288 Feb  3 19:35 volumes

```

### Images Docker

Les contenus les plus lourds sont généralement les images. Si vous utilisez le pilote de stockage par défaut overlay2, vos images Docker sont stockées dans `/var/lib/docker/overlay2`. Là, vous pouvez trouver différents fichiers qui représentent des couches en lecture seule d'une image Docker et une couche au-dessus qui contient vos modifications.

Explorons le contenu en utilisant un exemple :

```shell
$ docker image pull nginx
$ docker image inspect nginx

[
    {
        "Id": "sha256:207...6e1",
        "RepoTags": [
            "nginx:latest"
        ],
        "RepoDigests": [
            "nginx@sha256:ad5...c6f"
        ],
        "Parent": "",
 ...
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 126698063,
        "VirtualSize": 126698063,
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/585...9eb/diff:
                             /var/lib/docker/overlay2/585...9eb/diff",
                "MergedDir": "/var/lib/docker/overlay2/585...9eb/merged",
                "UpperDir": "/var/lib/docker/overlay2/585...9eb/diff",
                "WorkDir": "/var/lib/docker/overlay2/585...9eb/work"
            },
...

```

Le **LowerDir** contient les couches en lecture seule d'une image. La couche en lecture-écriture qui représente les modifications fait partie du **UpperDir**. Dans mon cas, le dossier **UpperDir** de NGINX contient les fichiers de log :

```shell
$ ls -la /var/lib/docker/overlay2/585...9eb/diff

total 8
drwxr-xr-x    2 root     root    4096 Feb  2 08:06 .
drwxr-xr-x    3 root     root    4096 Feb  2 08:06 ..
lrwxrwxrwx    1 root     root      11 Feb  2 08:06 access.log -> /dev/stdout
lrwxrwxrwx    1 root     root      11 Feb  2 08:06 error.log -> /dev/stderr
```

Le **MergedDir** représente le résultat du **UpperDir** et du **LowerDir** qui est utilisé par Docker pour exécuter le conteneur. Le **WorkDir** est un répertoire interne pour overlay2 et doit être vide.

### Volumes Docker

Il est possible d'ajouter un stockage persistant aux conteneurs pour conserver les données plus longtemps que le conteneur n'existe ou pour partager le volume avec l'hôte ou avec d'autres conteneurs. Un conteneur peut être démarré avec un volume en utilisant l'option **-v** :

```shell
$ docker run --name nginx_container -v /var/log nginx
```

Nous pouvons obtenir des informations sur l'emplacement du volume connecté par :

```shell
$ docker inspect nginx_container

...
"Mounts": [
            {
                "Type": "volume",
                "Name": "1e4...d9c",
                "Source": "/var/lib/docker/volumes/1e4...d9c/_data",
                "Destination": "/var/log",
                "Driver": "local",
                "Mode": "",
                "RW": true,
                "Propagation": ""
            }
        ],
...

```

Le répertoire référencé contient des fichiers de l'emplacement `/var/log` du conteneur NGINX.

```shell
$ ls -lah /var/lib/docker/volumes/1e4...d9c/_data

total 88
drwxr-xr-x    4 root     root        4.0K Feb  3 21:02 .
drwxr-xr-x    3 root     root        4.0K Feb  3 21:02 ..
drwxr-xr-x    2 root     root        4.0K Feb  3 21:02 apt
-rw-rw----    1 root     43             0 Jan 30 00:00 btmp
-rw-r--r--    1 root     root       34.7K Feb  2 08:06 dpkg.log
-rw-r--r--    1 root     root        3.2K Feb  2 08:06 faillog
-rw-rw-r--    1 root     43         29.1K Feb  2 08:06 lastlog
drwxr-xr-x    2 root     root        4.0K Feb  3 21:02 nginx
-rw-rw-r--    1 root     43             0 Jan 30 00:00 w

```

## Nettoyer l'espace utilisé par Docker

Il est recommandé d'utiliser la commande Docker pour nettoyer les conteneurs inutilisés. Les conteneurs, réseaux, images et le cache de build peuvent être nettoyés en exécutant :

```shell
$ docker system prune -a
```

De plus, vous pouvez également supprimer les volumes inutilisés en exécutant :

```shell
$ docker volumes prune
```

## **Résumé**

Docker est une partie importante de nombreux environnements et outils. Parfois, Docker semble un peu magique en résolvant des problèmes de manière très intelligente sans dire à l'utilisateur comment les choses sont faites en coulisses. Pourtant, Docker est un outil régulier qui stocke ses parties lourdes dans des emplacements qui peuvent être ouverts et modifiés. 

Parfois, le stockage peut se remplir rapidement. Par conséquent, il est utile d'inspecter son dossier racine, mais il n'est pas recommandé de supprimer ou de modifier manuellement des fichiers. Au lieu de cela, les commandes prune peuvent être utilisées pour libérer de l'espace disque.

J'espère que vous avez apprécié l'article. Si vous l'aimez et ressentez le besoin d'une salve d'applaudissements, [suivez-moi sur Twitter](https://twitter.com/sesigl). Je travaille chez eBay Kleinanzeigen, l'une des plus grandes entreprises de petites annonces au monde. Au fait, [nous recrutons](https://jobs.ebayclassifiedsgroup.com/ebay-kleinanzeigen) !

Bonne exploration de Docker :)

## Références

* Documentation du pilote de stockage Docker  
[https://docs.docker.com/storage/storagedriver/](https://docs.docker.com/storage/storagedriver/)
* Documentation du système de fichiers Overlay  
[https://www.kernel.org/doc/Documentation/filesystems/overlayfs.txt](https://www.kernel.org/doc/Documentation/filesystems/overlayfs.txt)