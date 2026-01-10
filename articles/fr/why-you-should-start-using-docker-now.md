---
title: Pourquoi vous devriez commencer à utiliser Docker dès maintenant
subtitle: ''
author: Jason
co_authors: []
series: null
date: '2021-11-17T20:42:19.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-start-using-docker-now
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/why-use-docker-image.jpeg
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
seo_title: Pourquoi vous devriez commencer à utiliser Docker dès maintenant
seo_desc: 'About a year back, I was just about ready to release Caer, a Computer Vision
  library in Python that would be publicly available on PyPi. But first, I decided
  to send it to a friend in Alberta to tinker around with it.

  A few days later, I found that h...'
---

Il y a environ un an, j'étais sur le point de publier [Caer](https://github.com/jasmcaus/caer), une bibliothèque de vision par ordinateur en Python qui serait disponible publiquement sur PyPi. Mais d'abord, j'ai décidé de l'envoyer à un ami en Alberta pour qu'il puisse l'essayer.

Quelques jours plus tard, j'ai découvert qu'il essayait toujours de comprendre comment le faire fonctionner sur sa machine.

Après des dizaines d'heures, j'ai finalement découvert pourquoi

Caer implémentait du code des versions précédentes d'autres packages Python qui n'était tout simplement pas disponible dans leurs nouvelles versions.

Et donc, malgré le fait qu'il avait ces packages installés, mon ami n'a pas pu exécuter Caer.

Les problèmes comme celui-ci ne sont pas spécifiques aux packages Python. Vous pourriez rencontrer quelque chose de similaire lorsque vous déplacez du code construit localement en production et qu'il ne fonctionne pas à cause de différents systèmes d'exploitation.

Mais que se passerait-il s'il existait un moyen d'atténuer ce problème de portabilité ?

> Eh bien, il y en a un  Docker !

Avant de parler de Docker, vous devez comprendre l'intuition derrière un *conteneur*.

## Qu'est-ce qu'un conteneur ?

Un conteneur est un environnement d'exécution entier : une application avec toutes ses dépendances, bibliothèques, binaires et fichiers de configuration nécessaires pour l'exécuter, regroupés en un seul package.

![Ciel très bleu](https://images.unsplash.com/photo-1504383633899-a17806f7e9ad?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTc3M3wwfDF8c2VhcmNofDZ8fGNvbnRhaW5lcnxlbnwwfHx8fDE2MzY3NDEwMzM&ixlib=rb-1.2.1&q=80&w=2000 align="left")

*Photo par [Unsplash](https://unsplash.com/@victoire_jonch?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit"&gt;Victoire Joncheray / &lt;a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)*

La *conteneurisation* abstrait les différences dans les distributions de systèmes d'exploitation, les dépendances des applications et l'infrastructure sous-jacente.

## Les conteneurs sont comme des VMs, mais beaucoup plus petits

Avec la virtualisation, ces conteneurs sont appelés *machines virtuelles*. Ceux-ci incluent le système d'exploitation en plus de l'application. Un serveur exécutant trois machines virtuelles peut avoir trois systèmes d'exploitation différents fonctionnant dessus.

Imaginez à quel point cela peut devenir encombrant.

En revanche, vous pouvez avoir le même serveur exécuter 3 applications conteneurisées avec Docker qui fonctionnent toutes avec le *même* système d'exploitation. Les parties du système d'exploitation qui sont partagées sont en *lecture seule*, tandis qu'un conteneur a un point de montage (un moyen d'accéder au conteneur) pour l'écriture.

Alors que les VMs peuvent faire plusieurs gigaoctets, un conteneur peut faire seulement quelques mégaoctets.

## La magie des conteneurs

Lorsque les applications sont conteneurisées, seul le *système d'exploitation* est virtualisé, contrairement au matériel (comme c'est le cas avec les VMs). Au lieu de provisionner du matériel, un système d'exploitation virtuel est provisionné pour l'application, vous permettant d'exécuter plusieurs applications et de définir des limitations de ressources comme vous le souhaitez.

![Image](https://www.freecodecamp.org/news/content/images/2021/11/image-42.png align="left")

[*Source*](https://containerjournal.com/topics/container-ecosystems/kubernetes-vs-docker-a-primer/)*: Container Journal*

## Comment utiliser Docker

Docker est un outil de conteneurisation utilisé par les développeurs pour créer des environnements isolés et reproductibles pour leurs applications.

Il a un processus de développement rapide, il est facile à utiliser, il fonctionne de la même manière sur les machines locales, les serveurs de développement, de pré-production et de production, et il est extrêmement scalable.

Docker, en fait, a conduit le passage à la conteneurisation des applications, et n'est, sans surprise pour personne, le joueur le plus puissant sur le marché aujourd'hui.

#### Comment installer Docker

* Windows ou MacOS : Installer [Docker Desktop](https://www.docker.com/get-started)

* Linux : Installer [Docker](https://docs.docker.com/get-docker/) et [Docker Compose](https://docs.docker.com/compose/install/)

Si vous êtes sous Linux, vous devrez exécuter vos commandes en tant que *root* ou ajouter l'utilisateur au groupe Docker :

```bash
sudo usermod -aG docker $(thatsme)
```

## Comment créer un Dockerfile

En Python, pour conteneuriser une application, vous devrez la packager en tant qu'image Docker. Pour en générer une, vous devez définir un Dockerfile. Le nom de ce fichier est simplement **DOCKERFILE** (sans extension).

```dockerfile
# Définition d'une image de base (Python 3 dans notre cas)
FROM python:3# Ajout d'un script Python à exécuter

ADD hello_world_script.py /

# Si notre script utilise le package Caer, nous devrons l'installer avec pip :RUN pip install caer

# Pour exécuter le script Python :
CMD [ "python", "./hello_world_script.py" ]
```

* `FROM` indique à Docker quelle image l'application utilise comme base (un peu compliqué, je sais)

* `RUN` exécute des commandes supplémentaires (comme une installation pip)

* `CMD` exécute les commandes lorsque l'image est chargée

Pour cette démonstration, j'ai utilisé le package `caer` que vous pouvez installer avec un simple `pip install caer`.

Supposons que notre script `hello_world_script.py` ressemble à ceci :

```python

import caer

print(caer.__version__)

img = caer.imread('./img1.png')

print(img.shape) # forme de l'image
print(img) # tenseur de l'image
```

Pour construire l'image à partir du Dockerfile, allez-y et exécutez ce qui suit :

```bash
docker build -t caer-readimg .
```

Une fois l'image construite, vous pourrez l'exécuter en tant que conteneur.

Vous remarquerez également une image 'caer-readimg' (vous pouvez voir toutes vos images Docker en exécutant la commande `docker images`).

Pour exécuter cette image,

```bash
docker run caer-readimg
```

## Comment supprimer une image Docker

```bash
# L'image_id peut être trouvée lorsque vous exécutez `docker images`

docker rmi <image_id>
```

## Comment supprimer un conteneur Docker

```bash
# Récupérer l'ID du conteneur :
docker ps -a 

# Supprimer le conteneur
docker rm <container_id>
```

# Conclusion

C'est à quel point il est facile de commencer avec Docker. Bien sûr, vous n'avez probablement pas besoin de construire une image Docker si votre application est aussi simple que le code discuté ci-dessus  mais cela a du sens surtout si vous travaillez sur le même projet avec plusieurs personnes.

N'oubliez pas de [me suivre sur Twitter](http://twitter.com/jasmcaus) pour les mises à jour sur les futurs articles. Bon apprentissage !