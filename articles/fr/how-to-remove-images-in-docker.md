---
title: Comment supprimer des images et des conteneurs dans Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-09T21:12:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-images-in-docker
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e04740569d1a4ca3ae5.jpg
tags:
- name: Docker
  slug: docker
- name: toothbrush
  slug: toothbrush
seo_title: Comment supprimer des images et des conteneurs dans Docker
seo_desc: 'Docker rmi

  docker rmi removes images by their ID.

  To remove the image, you first need to list all the images to get the Image IDs,
  Image name and other details. By running simple command docker images -a or docker
  images.

  After that you make sure whi...'
---

## **Docker rmi**

`docker rmi` supprime les images par leur ID.

Pour supprimer l'image, vous devez d'abord lister toutes les images pour obtenir les ID des images, le nom de l'image et autres détails. En exécutant la commande simple `docker images -a` ou `docker images`.

Après cela, assurez-vous de l'image que vous souhaitez supprimer, pour cela, exécutez cette commande simple `docker rmi <votre-id-image>`. Ensuite, vous pouvez confirmer que l'image a été supprimée ou non en listant toutes les images et en vérifiant.

### **Supprimer plusieurs images**

Il existe un moyen de supprimer plus d'une image à la fois, lorsque vous souhaitez supprimer plusieurs images spécifiques. Pour cela, obtenez d'abord les ID des images simplement en listant les images, puis exécutez la commande suivante.

`docker rmi <votre-id-image> <votre-id-image> ...`

Écrivez les ID des images dans la commande suivis d'espaces entre eux.

### **Supprimer toutes les images en une fois**

Pour supprimer toutes les images, il existe une commande simple pour cela. `docker rmi $(docker images -q)`

Dans la commande ci-dessus, il y a deux commandes, la première qui s'exécute dans `$()` est une syntaxe shell et retourne les résultats de ce qui est exécuté dans cette syntaxe. Donc ici, `-q` est une option utilisée pour retourner les ID uniques, `$()` retourne les résultats des ID d'images et ensuite `docker rmi` supprime toutes ces images.

#### **Pour plus d'informations :**

* [Docker CLI docs: rmi](https://docs.docker.com/engine/reference/commandline/rm/)

## **Docker rm**

`docker rm` supprime les conteneurs par leur nom ou ID.

Lorsque vous avez des conteneurs Docker en cours d'exécution, vous devez d'abord les arrêter avant de les supprimer.

* Arrêter tous les conteneurs en cours d'exécution : `docker stop $(docker ps -a -q)`
* Supprimer tous les conteneurs arrêtés : `docker rm $(docker ps -a -q)`

### **Supprimer plusieurs conteneurs**

Vous pouvez arrêter et supprimer plusieurs conteneurs en passant aux commandes une liste des conteneurs que vous souhaitez supprimer. La syntaxe shell `$()` retourne les résultats de ce qui est exécuté dans les crochets. Vous pouvez ainsi créer votre liste de conteneurs à l'intérieur de celle-ci pour la passer aux commandes `stop` et `rm`.

### Voici une explication de docker ps -a -q

* `docker ps` liste les conteneurs
* `-a` l'option pour lister tous les conteneurs, même ceux arrêtés. Sans cela, il liste par défaut uniquement les conteneurs en cours d'exécution
* `-q` l'option silencieuse pour fournir uniquement les ID numériques des conteneurs, plutôt qu'un tableau complet d'informations sur les conteneurs

#### **Plus d'informations :**

* [Docker CLI docs: rm](https://docs.docker.com/engine/reference/commandline/rm/)

## Plus d'informations sur les images dans Docker :

* [Guide des images Docker](https://www.freecodecamp.org/news/docker-image-guide-how-to-remove-and-delete-docker-images-stop-containers-and-remove-all-volumes/)
* [Où sont stockées les images Docker ?](https://www.freecodecamp.org/news/where-are-docker-images-stored-docker-container-paths-explained/)

## Plus d'informations sur les conteneurs dans Docker :

* [Comment automatiser le déploiement de conteneurs Docker](https://www.freecodecamp.org/news/automate-docker-container-deployment-via-maven-53a855e26d3e/)
* [Comment corriger les vulnérabilités des conteneurs Docker](https://www.freecodecamp.org/news/how-to-find-and-fix-docker-container-vulnerabilities-in-2020/)

## Plus d'informations sur Docker :

* [Un guide pour débutants sur Docker](https://www.freecodecamp.org/news/a-beginners-guide-to-docker-how-to-create-your-first-docker-application-cc03de9b639f/)
* [Cours Docker DevOps (cours vidéo gratuit)](https://www.freecodecamp.org/news/docker-devops-course/)
* [Docker 101 : de la création au déploiement](https://www.freecodecamp.org/news/docker-101-creation-to-deployment/)