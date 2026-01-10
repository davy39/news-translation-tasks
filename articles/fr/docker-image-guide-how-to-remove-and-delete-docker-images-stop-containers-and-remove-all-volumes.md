---
title: 'Guide des images Docker : comment supprimer des images Docker, arrêter des
  conteneurs et supprimer tous les volumes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-30T01:00:00.000Z'
originalURL: https://freecodecamp.org/news/docker-image-guide-how-to-remove-and-delete-docker-images-stop-containers-and-remove-all-volumes
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/docker-container-volumes-images.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: containerization
  slug: containerization
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: Kubernetes
  slug: kubernetes
seo_title: 'Guide des images Docker : comment supprimer des images Docker, arrêter
  des conteneurs et supprimer tous les volumes'
seo_desc: 'By Sebastian Sigl

  Docker has been widely adopted and is a great vehicle to deploy an application to
  the cloud (or some other Docker-ready infrastructure). It is also useful for local
  development. You can start complex applications quickly, develop in...'
---

Par Sebastian Sigl

Docker a été largement adopté et est un excellent moyen de déployer une application dans le cloud (ou une autre infrastructure prête pour Docker). Il est également utile pour le développement local. Vous pouvez démarrer des applications complexes rapidement, développer en isolation et avoir tout de même de très bonnes performances.

Voici les commandes les plus importantes pour utiliser Docker efficacement dans votre travail quotidien.

## Lister toutes les images Docker

```shell
docker images

```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-52.png)

Dans mon cas, j'ai 3 images installées :

* MySQL, version 8.0.19, une étiquetée comme dernière version
* et Cassandra avec la dernière version.

Pour obtenir plus d'informations sur une image, vous pouvez l'inspecter :

```shell
docker inspect mysql:latest
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-51.png)

Cela retournera une liste d'informations. Alternativement, vous pouvez également utiliser l'ID de l'image pour obtenir les informations :

```shell
docker inspect 3a5e53f63281
```

La sortie peut être écrasante. Par conséquent, il existe une option pratique pour filtrer certaines informations :

```shell
docker inspect --format='{{.RepoTags}}  {{.Config.Image}}' 3a5e53f63281
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-50.png)

## Supprimer des images Docker

Une seule image peut être supprimée par :

```shell
docker rm mysql:latest
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-48.png)

Dans mon cas, l'image est toujours étiquetée avec _mysql:8.0.19_. Par conséquent, pour la supprimer complètement, je dois également supprimer une autre étiquette de version :

```shell
docker rm mysql:8.0.19
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-45.png)

Pour supprimer l'image directement, il est plus facile de supprimer l'image par son ID :

```shell
docker image rm 3a5e53f63281 -f
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-46.png)

L'option **-f** force l'exécution, car sinon vous obtiendriez une erreur si l'image est référencée par plus d'une étiquette.

## Démarrer une image Docker

Une image peut être démarrée au premier plan par :

```shell
docker run cassandra
```

Si l'image n'existe pas, elle sera téléchargée. Vous pouvez arrêter l'exécution en appuyant sur **CTRL+C**. Vous pouvez également l'exécuter en arrière-plan en ajoutant l'option **-d** :

```shell
docker run -d mysql
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-54.png)

Si le conteneur est démarré en arrière-plan, vous recevez l'ID du conteneur.

Par défaut, le conteneur s'exécute en isolation. Par conséquent, vous ne pourrez pas communiquer avec lui, et aucun fichier n'est stocké dans votre répertoire actuel.

## Transférer les ports d'un conteneur

Vous pouvez transférer les ports en utilisant l'option **-p** vers, par exemple, une page exposée par votre conteneur :

```shell
docker run -p 8080:80 nginx
```

Ce conteneur NGINX expose un serveur web sur le port 80. En utilisant -p 8080:80, le port local 8080 est transféré vers le port 80 du conteneur.

## Se connecter à un conteneur

Parfois, il est utile de se connecter à un conteneur. Cela n'est possible que si le conteneur a un shell installé. Vous obtiendrez une erreur si ce n'est pas le cas.

Tout d'abord, démarrez le conteneur détaché et donnez-lui un nom :

```shell
docker run -d --name my_container nginx
```

Cela retournera un ID de conteneur. Maintenant, vous pouvez exécuter un shell dans le conteneur et attacher votre entrée et sortie à celui-ci en utilisant les options **-i** et **-t** :

```shell
docker exec -it my_container bash
```

Au lieu du nom du conteneur, vous pouvez également utiliser l'ID du conteneur retourné pour toutes les opérations suivantes. Parfois, bash n'est pas disponible. Par conséquent, vous pouvez également essayer de lancer un shell de base :

```shell
docker exec -it my_container sh
```

## Lister les conteneurs en cours d'exécution

Après avoir démarré un conteneur, vous pouvez voir tous les conteneurs en cours d'exécution en exécutant :

```shell
docker ps
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-56.png)

En ajoutant **-a**, les conteneurs arrêtés seront également listés :

```shell
docker ps -a
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/image-57.png)

## Partager un dossier local avec un conteneur

Parfois, il est utile de synchroniser des fichiers entre le conteneur et le système de fichiers local. Vous pouvez le faire en exécutant un conteneur et en utilisant l'option **-v**. Sur Linux et macOS, vous pouvez partager un dossier temporaire local avec un conteneur par :

```shell
docker run --name=my_container -d -v $(pwd)/tmp:/var/log/nginx -p 8080:80 nginx
```

Sur Windows, vous pouvez exécuter :

```shell
docker run --name=my_container -d -v %cd%/tmp:/var/log/nginx -p 8080:80 nginx
```

## Arrêter les conteneurs en cours d'exécution

Il est possible d'arrêter un conteneur en cours d'exécution par :

```shell
docker stop my_container
```

L'arrêt d'un conteneur arrête tous les processus mais conserve les modifications dans le système de fichiers.

## Démarrer un conteneur arrêté

Un conteneur arrêté peut être démarré par :

```shell
docker start my_container
```

## Supprimer un conteneur

Pour supprimer un conteneur arrêté, vous pouvez exécuter :

```shell
docker rm my_container
```

Pour arrêter et supprimer le conteneur en une seule commande, vous pouvez ajouter l'option de force **-f**.

```shell
docker rm -f my_container
```

## Créer un volume et le partager avec plusieurs conteneurs

Un volume indépendant nommé **SharedData** peut être créé par :

```shell
docker volume create --name SharedData

docker run --name=my_container -d -v SharedData:/var/log/nginx -p 8080:80 nginx

docker run --name=my_container_2 -d -v SharedData:/var/log/nginx -p 8080:80 nginx
```

Les deux conteneurs auront un dossier partagé, et les fichiers seront synchronisés entre les deux conteneurs.

## Supprimer un volume

Pour supprimer un volume, tous les conteneurs qui utilisent le volume doivent être supprimés.

```shell
docker rm -f my_container
docker rm -f my_container_2
docker volume rm SharedData
```

## Supprimer les conteneurs arrêtés et les images inutilisées

Une commande de nettoyage sûre est :

```shell
docker system prune -a
```

## Supprimer tous les volumes inutilisés

Tous les volumes non montés peuvent être supprimés par :

```shell
docker volume prune
```

## Conclusion

Créer des conteneurs, se connecter à des conteneurs, transférer des ports et partager des volumes sont les commandes les plus importantes de votre interface de ligne de commande Docker. Elles constituent la base de systèmes comme Kubernetes et nous permettent de créer et d'exécuter des applications en isolation.

J'espère que vous avez apprécié l'article. Si vous l'aimez et ressentez le besoin d'une salve d'applaudissements, [suivez-moi sur Twitter](https://twitter.com/sesigl).

Je suis cofondateur de notre plateforme de voyage révolutionnaire appelée [Explore The World](https://www.urlaubsbaron.de). Nous sommes une jeune startup située à Dresde, en Allemagne, et ciblerons d'abord le marché allemand. Contactez-moi si vous avez des commentaires et des questions sur un sujet quelconque.

Bonne exploration de Docker :)

Références

* Documentation de la ligne de commande Docker
[https://docs.docker.com/engine/reference/commandline/docker/](https://docs.docker.com/engine/reference/commandline/docker/)