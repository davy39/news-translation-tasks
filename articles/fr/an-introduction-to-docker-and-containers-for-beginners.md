---
title: Une Introduction à Docker et aux Conteneurs pour Débutants
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2024-11-26T11:11:06.148Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-docker-and-containers-for-beginners
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1731093934598/6f2fa740-63e6-48e9-8e17-364544d1fcc6.png
tags:
- name: Docker
  slug: docker
- name: containers
  slug: containers
seo_title: Une Introduction à Docker et aux Conteneurs pour Débutants
seo_desc: 'In the world of modern software development, efficiency and consistency
  are key. Developers and operations teams need solutions that help them manage, deploy,
  and run applications seamlessly across different environments.

  Containers and Docker are te...'
---

Dans le monde du développement logiciel moderne, l'efficacité et la cohérence sont essentielles. Les développeurs et les équipes opérationnelles ont besoin de solutions qui les aident à gérer, déployer et exécuter des applications de manière transparente dans différents environnements.

Les conteneurs et Docker sont des technologies qui ont révolutionné la manière dont les logiciels sont construits, testés et déployés.

Que vous soyez nouveau dans le monde de la technologie ou que vous cherchiez simplement à comprendre les bases de Docker, cet article vous guidera à travers les essentiels.

## Table des Matières

* [Qu'est-ce que les Conteneurs ?](#heading-quest-ce-que-les-conteneurs)
    
* [Qu'est-ce que Docker ?](#heading-quest-ce-que-docker)
    
* [Pourquoi Docker ?](#heading-pourquoi-docker)
    
* [Architecture de Docker](#heading-architecture-de-docker)
    
* [Runtime de Conteneur de Docker : containerd](#heading-runtime-de-conteneur-de-docker-containerd)
    
* [Comment Créer un Conteneur Simple en Utilisant Docker](#heading-comment-creer-un-conteneur-simple-en-utilisant-docker)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que les Conteneurs ?

Avant de plonger dans Docker, comprenons d'abord les conteneurs. Imaginez que vous travaillez sur un projet, et que votre application fonctionne parfaitement sur votre ordinateur portable. Mais lorsque vous essayez d'exécuter la même application sur une autre machine, elle échoue. Cela est souvent dû à des différences d'environnements : différents systèmes d'exploitation, versions de logiciels installés ou configurations.

Les conteneurs résolvent ce problème en emballant une application et toutes ses dépendances comme les bibliothèques, les frameworks et les fichiers de configuration dans une seule unité standardisée. Cela garantit que l'application s'exécute de la même manière, peu importe où elle est déployée, que ce soit sur votre ordinateur portable, un serveur ou dans le cloud.

Caractéristiques clés des conteneurs :

* **Légers** : Les conteneurs partagent le noyau du système hôte, contrairement aux machines virtuelles (VM) qui nécessitent des instances de système d'exploitation séparées, les rendant ainsi plus rapides et plus efficaces.
    
* **Portables** : Une fois construits, un conteneur peut s'exécuter de manière cohérente dans divers environnements.
    
* **Isolés** : Les conteneurs s'exécutent dans des processus isolés, ce qui signifie qu'ils n'interfèrent pas avec d'autres applications s'exécutant sur le même système.
    

## Qu'est-ce que Docker ?

Maintenant que nous comprenons les conteneurs, parlons de Docker, la plateforme qui a rendu les conteneurs grand public.

Docker est un outil open-source conçu pour simplifier le processus de création, de gestion et de déploiement de conteneurs. Lancé en 2013, Docker est rapidement devenu la solution de référence pour la conteneurisation grâce à sa facilité d'utilisation, son support communautaire et son puissant écosystème d'outils.

### Concepts Clés dans Docker

1. **Images Docker** : Considérez une image Docker comme un plan pour votre conteneur. Elle contient tout ce qui est nécessaire pour exécuter l'application, y compris le code, les bibliothèques et les dépendances système. Les images sont construites à partir d'un ensemble d'instructions écrites dans un Dockerfile.
    
2. **Conteneurs Docker** : Un conteneur est une instance en cours d'exécution d'une image Docker. Lorsque vous créez et démarrez un conteneur, Docker lance l'image dans un environnement isolé où votre application peut s'exécuter.
    
3. **Dockerfile** : Il s'agit d'un fichier texte qui contient les étapes nécessaires pour créer une image Docker. C'est là que vous définissez à quoi ressemblera votre conteneur, y compris l'image de base, le code de l'application et toute dépendance supplémentaire.
    
4. **Docker Hub** : Docker Hub est un registre public où les développeurs peuvent partager et accéder à des images pré-construites. Si vous travaillez sur une application ou une pile technologique courante, il y a de fortes chances qu'une image soit déjà disponible sur Docker Hub, ce qui vous fait gagner du temps.
    
5. **Docker Compose** : Pour les applications qui nécessitent plusieurs conteneurs (par exemple, un serveur web et une base de données), Docker Compose vous permet de définir et de gérer des environnements multi-conteneurs à l'aide d'un simple fichier YAML.
    

## Pourquoi Docker ?

La popularité de Docker provient de sa capacité à résoudre une variété de défis auxquels les développeurs sont confrontés aujourd'hui :

* **Cohérence à travers les Environnements** : Les développeurs peuvent "construire une fois, exécuter partout", garantissant que la même application fonctionne de la même manière dans différents environnements, du développement local à la production.
    
* **Vitesse** : Les conteneurs Docker sont rapides à démarrer et à arrêter, ce qui les rend idéaux pour les pipelines de test et de déploiement.
    
* **Utilisation Efficace des Ressources** : Puisque les conteneurs partagent les ressources du système hôte plus efficacement que les machines virtuelles, ils réduisent les frais généraux et permettent une plus grande densité dans les déploiements.
    
* **Contrôle de Version pour Vos Applications** : Docker vous permet de contrôler les versions non seulement de votre code, mais aussi de l'environnement dans lequel votre code s'exécute. Cela est particulièrement utile pour revenir à des versions précédentes ou pour déboguer des problèmes en production.
    

## Architecture de Docker

Lorsque vous commencez à utiliser Docker, vous pouvez le traiter comme une boîte qui "fonctionne simplement". Bien que cela soit suffisant pour commencer, une compréhension plus approfondie de l'architecture de Docker vous aidera à résoudre les problèmes, à optimiser les performances et à prendre des décisions éclairées concernant votre stratégie de conteneurisation.

L'architecture de Docker est conçue pour assurer l'efficacité, la flexibilité et l'évolutivité. Elle est composée de plusieurs composants qui travaillent ensemble pour créer, gérer et exécuter des conteneurs. Examinons de plus près chacun de ces composants.

### Architecture de Docker : Composants Clés

L'architecture de Docker est construite autour d'un modèle client-serveur qui inclut les composants suivants :

* **Client Docker**
    
* **Démon Docker (dockerd)**
    
* **Moteur Docker**
    
* **Images Docker**
    
* **Conteneurs Docker**
    
* **Registres Docker**
    

![Architecture de Docker](https://docs.docker.com/get-started/images/docker-architecture.webp align="left")

#### 1. Client Docker

Le Client Docker est le moyen principal par lequel les utilisateurs interagissent avec Docker. Il s'agit d'un outil en ligne de commande qui envoie des instructions au Démon Docker (que nous aborderons ensuite) en utilisant des API REST. Les commandes comme `docker build`, `docker pull` et `docker run` sont exécutées à partir du Client Docker.

Lorsque vous tapez une commande comme `docker run nginx`, le Client Docker la traduit en une requête que le Démon Docker peut comprendre et exécuter. Essentiellement, le Client Docker agit comme une interface frontale pour interagir avec les composants backend plus complexes de Docker.

#### 2. Démon Docker (dockerd)

Le Démon Docker, également connu sous le nom de **dockerd**, est le cerveau de toute l'opération Docker. Il s'agit d'un processus en arrière-plan qui écoute les requêtes du Client Docker et gère les objets Docker comme les conteneurs, les images, les réseaux et les volumes.

Voici ce dont le Démon Docker est responsable :

* **Construction et exécution des conteneurs** : Lorsque le client envoie une commande pour exécuter un conteneur, le démon récupère l'image, crée le conteneur et le démarre.
    
* **Gestion des ressources Docker** : Le démon gère des tâches comme les configurations réseau et la gestion des volumes.
    

* Le Démon Docker s'exécute sur la machine hôte et communique avec le Client Docker en utilisant une API REST, des sockets Unix ou une interface réseau. Il est également responsable de l'interaction avec les runtimes de conteneurs, qui gèrent l'exécution réelle des conteneurs.
    

#### 3. Moteur Docker

Le Moteur Docker est la partie centrale de Docker. C'est ce qui fait fonctionner l'ensemble de la plateforme, combinant le client, le démon et le runtime de conteneur. Le Moteur Docker peut s'exécuter sur divers systèmes d'exploitation, y compris Linux, Windows et macOS.

Il existe deux versions du Moteur Docker :

* **Docker CE (Community Edition)** : Il s'agit de la version gratuite et open-source de Docker, largement utilisée pour des projets personnels et à plus petite échelle.
    
* **Docker EE (Enterprise Edition)** : La version payante et de niveau entreprise de Docker offre des fonctionnalités supplémentaires comme une sécurité renforcée, un support et une certification.
    

Le Moteur Docker simplifie les complexités de l'orchestration de conteneurs en intégrant les divers composants nécessaires pour construire, exécuter et gérer des conteneurs.

#### 4. Images Docker

Une Image Docker est un modèle en lecture seule qui contient tout ce dont votre application a besoin pour s'exécuter—code, bibliothèques, dépendances et configurations. Les images sont les blocs de construction des conteneurs. Lorsque vous exécutez un conteneur, vous créez essentiellement une couche modifiable par-dessus une image Docker.

Les Images Docker sont généralement construites à partir de Dockerfiles, qui sont des fichiers texte contenant des instructions sur la manière de construire l'image. Par exemple, un Dockerfile de base pourrait commencer avec une image de base comme `nginx` ou `ubuntu` et inclure des commandes pour copier des fichiers, installer des dépendances ou définir des variables d'environnement.

Voici un exemple simple d'un Dockerfile :

```bash
dockerfileCopy codeFROM nginx:latest
COPY ./html /usr/share/nginx/html
EXPOSE 80
```

Dans cet exemple, nous utilisons l'image officielle Nginx comme base et copions nos fichiers HTML locaux dans le répertoire web du conteneur.

Une fois l'image construite, elle peut être stockée dans un Registre Docker et partagée avec d'autres.

#### 5. Conteneurs Docker

Un Conteneur Docker est une instance en cours d'exécution d'une Image Docker. Il est léger et isolé des autres conteneurs, mais partage le noyau du système d'exploitation hôte. Chaque conteneur a son propre système de fichiers, mémoire, allocation de CPU et paramètres réseau, ce qui le rend portable et reproductible.

Les conteneurs peuvent être créés, démarrés, arrêtés et détruits, et ils peuvent même persister entre les redémarrages. Parce que les conteneurs sont basés sur des images, ils garantissent que les applications se comporteront de la même manière, peu importe où elles sont exécutées.

Quelques caractéristiques clés des conteneurs Docker :

* **Isolation** : Les conteneurs sont isolés les uns des autres et de l'hôte, mais partagent toujours le même noyau du système d'exploitation.
    
* **Portabilité** : Les conteneurs peuvent s'exécuter n'importe où, que ce soit sur votre machine locale, une machine virtuelle ou un fournisseur de cloud.
    

#### 6. Registres Docker

Un Registre Docker est un endroit centralisé où les Images Docker sont stockées et distribuées. Le registre le plus populaire est Docker Hub, qui héberge des millions d'images publiques. Les organisations peuvent également configurer des registres privés pour stocker et distribuer leurs propres images de manière sécurisée.

Les Registres Docker offrent plusieurs fonctionnalités clés :

* **Versionnage des Images** : Les images sont versionnées à l'aide de balises, ce qui facilite la gestion de différentes versions d'une application.
    
* **Contrôle d'Accès** : Les registres peuvent être publics ou privés, avec un contrôle d'accès basé sur les rôles pour gérer qui peut tirer ou pousser des images.
    
* **Distribution** : Les images peuvent être tirées d'un registre et déployées n'importe où, ce qui facilite le partage et la réutilisation des applications conteneurisées.
    

## Runtime de Conteneur de Docker : containerd

Un développement important récent dans l'architecture de Docker est l'utilisation de containerd. Docker utilisait autrefois son propre runtime de conteneur, mais maintenant il utilise containerd, un runtime de conteneur qui suit les normes de l'industrie et est également utilisé par d'autres plateformes comme Kubernetes.

1. containerd est responsable de :
    
    * Démarrer et arrêter les conteneurs
        
    * Gérer le stockage et le réseau pour les conteneurs
        
    * Tirer les images de conteneurs des registres
        

En séparant le runtime de conteneur des fonctionnalités de haut niveau de Docker, Docker est devenu plus modulaire, permettant à d'autres outils d'utiliser containerd tandis que Docker se concentre sur les fonctionnalités orientées utilisateur.

## Comment Créer un Conteneur Simple en Utilisant Docker

**Tirer l'Image Linux**

Commencez par tirer l'image `alpine` depuis Docker Hub. L'image `alpine` est une distribution Linux minimale, conçue pour être légère et rapide.

Exécutez la commande suivante :

```bash
docker pull alpine
```

Cela téléchargera l'image `alpine` sur votre système local.

**Exécuter le Conteneur**

Créez et démarrez un conteneur en utilisant l'image `alpine`. Nous lancerons également une session de terminal à l'intérieur du conteneur.

```bash
docker run -it alpine /bin/sh
```

Voici ce que signifie chaque option :

* `docker run` : Crée et démarre un nouveau conteneur.
    
* `-it` : Vous permet d'interagir avec le conteneur (mode interactif + terminal).
    
* `alpine` : Spécifie l'image à utiliser.
    
* `/bin/sh` : Spécifie la commande à exécuter à l'intérieur du conteneur (une session shell dans ce cas).
    

**Explorer le Conteneur**

Une fois le conteneur en cours d'exécution, vous verrez une invite de shell qui ressemble à ceci :

```bash
/ #
```

Cela indique que vous êtes à l'intérieur du conteneur Alpine Linux. Vous pouvez maintenant exécuter des commandes Linux. Par exemple :

Vérifiez le répertoire courant :

```bash
pwd
```

Liste des fichiers dans le répertoire :

```bash
ls
```

Sortie : Une structure de répertoire minimale, car Alpine est une image légère.

Vous pouvez également installer un package (Alpine utilise `apk` comme gestionnaire de packages) :

```bash
apk add curl
```

**Quitter le Conteneur**

Lorsque vous avez terminé l'exploration, tapez `exit` pour fermer la session et arrêter le conteneur :

```bash
bashCopy codeexit
```

**Accéder au Conteneur Après Son Arrêt**

Si vous souhaitez accéder à nouveau au conteneur après l'avoir arrêté, vous pouvez utiliser cette commande pour lister tous les conteneurs (y compris ceux arrêtés) :

```bash
docker ps -a
```

Vous verrez une liste de conteneurs avec leurs identifiants et statuts, puis vous pourrez démarrer le conteneur arrêté :

```bash
docker start <container-id>
```

Vous pouvez vous attacher au shell du conteneur en utilisant cette commande :

```bash
docker exec -it <container-id> /bin/sh
```

Si vous n'avez plus besoin du conteneur, vous pouvez le supprimer :

1. Arrêtez le conteneur (s'il est encore en cours d'exécution) :
    
    ```bash
    docker stop <container-id>
    ```
    
2. Supprimez le conteneur :
    
    ```bash
    docker rm <container-id>
    ```
    

**Récapitulatif des Commandes Docker Clés**

| **Commande** | **Description** |
| --- | --- |
| `docker pull alpine` | Télécharge l'image Alpine Linux. |
| `docker run -it alpine /bin/sh` | Crée et démarre un conteneur interactif. |
| `docker ps -a` | Liste tous les conteneurs (en cours d'exécution et arrêtés). |
| `docker start <container-id>` | Démarre un conteneur arrêté. |
| `docker exec -it <container-id>` | S'attache à un conteneur en cours d'exécution. |
| `docker stop <container-id>` | Arrête un conteneur en cours d'exécution. |
| `docker rm <container-id>` | Supprime un conteneur arrêté. |

## Conclusion

Maintenant que vous avez une compréhension de base, il est temps de mettre vos connaissances en pratique. Commencez à expérimenter avec Docker, construisez votre premier conteneur et explorez son vaste écosystème.

Vous comprendrez bientôt pourquoi Docker est devenu une pierre angulaire du DevOps moderne et de l'ingénierie logicielle.

Vous pouvez me suivre sur :

* [Twitter](https://twitter.com/Kedar__98)
    
* [LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)