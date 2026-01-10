---
title: 'Comment utiliser Docker avec Node.js : Un manuel pour les développeurs'
subtitle: ''
author: Oghenekparobo Stephen
co_authors: []
series: null
date: '2025-11-18T22:18:07.637Z'
originalURL: https://freecodecamp.org/news/how-to-use-to-docker-with-nodejs-handbook
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1763502750050/74610cbc-124b-48aa-9cb6-7ed861123511.png
tags:
- name: Docker
  slug: docker
- name: Devops
  slug: devops
- name: ci-cd
  slug: ci-cd
- name: 'Technical writing '
  slug: technical-writing-1
- name: handbook
  slug: handbook
- name: Node.js
  slug: nodejs
seo_title: 'Comment utiliser Docker avec Node.js : Un manuel pour les développeurs'
seo_desc: 'In this handbook, you’ll learn what Docker is and why it’s a must-have
  skill for backend and full-stack developers. And, most importantly, you’ll learn
  how to use it in real-world projects from start to finish.

  We will go far beyond the usual “Hello ...'
---

Dans ce manuel, vous apprendrez ce qu'est Docker et pourquoi c'est une compétence indispensable pour les développeurs backend et full-stack. Et, plus important encore, vous apprendrez comment l'utiliser dans des projets concrets de A à Z.

Nous irons bien au-delà des exemples habituels « Hello World » et nous vous accompagnerons dans la conteneurisation d'une application JavaScript full-stack complète (backend Node.js + Express, frontend HTML/CSS/JS, base de données MongoDB et interface d'administration Mongo Express).

Vous découvrirez la mise en réseau de plusieurs conteneurs, l'orchestration de l'ensemble avec Docker Compose, la construction et le versionnage de vos propres images, la persistance des données avec les volumes, et la publication sécurisée de vos images sur un dépôt privé AWS ECR pour le partage et le déploiement en production.

À la fin, vous serez en mesure d'éliminer les problèmes du type « ça marche sur ma machine », de gérer en toute confiance des applications multi-services, de déployer des environnements cohérents n'importe où et d'intégrer Docker dans votre flux de travail quotidien et vos pipelines CI/CD comme un pro.

Comme Docker est une compétence clé pour les développeurs backend, nous commencerons par couvrir ses concepts de base.

## **Prérequis**

Ce manuel technique est conçu pour les développeurs ayant une certaine expérience pratique du développement full-stack. Vous devez être à l'aise avec le déploiement d'applications et avoir une compréhension de base des pipelines CI/CD.

Bien que nous couvrions Docker depuis la base, ce guide n'est pas destiné aux développeurs débutants absolus. Je suppose que vous avez une expérience de développement en conditions réelles et que vous souhaitez améliorer votre workflow avec Docker.

Enfin, une familiarité de base avec AWS et les concepts généraux de déploiement sera également utile, bien qu'il ne soit pas nécessaire d'être un expert. Ce manuel est idéal pour les développeurs qui cherchent à renforcer leurs compétences de niveau production et à intégrer Docker en toute confiance dans leurs projets.

## Table des matières :

1. [Qu'est-ce qu'un conteneur ?](#heading-qu-est-ce-qu-un-conteneur)
    
2. [Docker vs Machines Virtuelles](#heading-docker-vs-machines-virtuelles)
    
3. [Installation de Docker](#heading-installation-de-docker)
    
4. [Commandes Docker de base](#heading-commandes-docker-de-base)
    
5. [Pratique avec JavaScript](#heading-pratique-avec-javascript)
    
    * [Comment récupérer l'image MongoDB](#heading-comment-recuperer-l-image-mongodb)
        
    * [Comment récupérer l'image Mongo Express](#heading-comment-recuperer-l-image-mongo-express)
        
    * [Réseau Docker](#heading-reseau-docker)
        
6. [Comment lancer le conteneur Mongo](#heading-comment-lancer-le-conteneur-mongo)
    
7. [Comment lancer le conteneur Mongo Express](#heading-comment-lancer-le-conteneur-mongo-express)
    
8. [Comment connecter Node.js à MongoDB](#heading-comment-connecter-nodejs-a-mongodb)
    
9. [Comment utiliser Docker Compose](#heading-comment-utiliser-docker-compose)
    
    * [Pourquoi utiliser Docker Compose ?](#heading-pourquoi-utiliser-docker-compose)
        
10. [Comment construire notre propre image Docker](#heading-comment-construire-notre-propre-image-docker)
    
    * [La solution](#heading-la-solution)
        
    * [Pourquoi MongoDB fonctionne](#heading-pourquoi-mongodb-fonctionne)
        
    * [Ajouter votre application à Docker Compose](#heading-ajouter-votre-application-a-docker-compose)
        
    * [Démarrer tous les services](#heading-demarrer-tous-les-services)
        
    * [Vérifier que tout fonctionne](#heading-verifier-que-tout-fonctionne)
        
    * [Ce qui a changé et pourquoi ça fonctionne](#heading-ce-qui-a-change-et-pourquoi-ca-fonctionne)
        
11. [Comment gérer vos conteneurs](#heading-comment-gerer-vos-conteneurs)
    
12. [Comment créer un dépôt Docker privé](#heading-comment-creer-un-depot-docker-prive)
    
    * [Étape 1 : Obtenir vos clés d'accès AWS](#heading-etape-1-obtenir-vos-cles-d-acces-aws)
        
    * [Étape 2 : Vérifier si AWS CLI est installé](#heading-etape-2-verifier-si-aws-cli-est-installe)
        
    * [Étape 3 : Configurer AWS CLI](#heading-etape-3-configurer-aws-cli)
        
    * [Étape 4 : Tester votre configuration AWS](#heading-etape-4-tester-votre-configuration-aws)
        
    * [Étape 5 : Se connecter à ECR (Registre Docker)](#heading-etape-5-se-connecter-a-ecr-registre-docker)
        
    * [Comprendre le nommage des images dans les dépôts Docker](#heading-comprendre-le-nommage-des-images-dans-les-depots-docker)
        
    * [Étape 6 : Construire, taguer et pousser votre image](#heading-etape-6-construire-taguer-et-pousser-votre-image)
        
13. [Exercice : Créer et pousser une nouvelle version](#heading-exercice-creer-et-pousser-une-nouvelle-version)
    
    * [Déploiement de notre image](#heading-deploiement-de-notre-image)
        
    * [Pourquoi devons-nous utiliser l'URL complète de l' image pour ECR](#heading-pourquoi-devons-nous-utiliser-l-url-complete-de-l-image-pour-ecr)?
        
    * [Déployer votre application avec Docker Compose](#heading-deployer-votre-application-avec-docker-compose)
        
    * [Partager notre image Docker privée](#heading-partager-notre-image-docker-privee)
        
14. [Volumes Docker](#heading-volumes-docker)
    
    * [Comment fonctionnent les volumes Docker](#heading-comment-fonctionnent-les-volumes-docker)
        
    * [Types de volumes Docker](#heading-types-de-volumes-docker)
        
    * [Exemple de fichier Docker Compose utilisant des volumes](#heading-exemple-de-fichier-docker-compose-utilisant-des-volumes)
        
    * [Démarrer votre application](#heading-demarrer-votre-application)
        
15. [Conclusion](#heading-conclusion)
    

## Qu'est-ce qu'un conteneur ?

Un conteneur est un moyen d'empaqueter une application avec tout ce dont elle a besoin, y compris ses dépendances, ses bibliothèques et ses fichiers de configuration.

Comme les conteneurs sont portables, ils peuvent être partagés entre les équipes et déployés sur n'importe quelle machine sans se soucier de la compatibilité.

![images de conteneurs empilés pour illustrer l'idée de conteneurs dans Docker](https://cdn.hashnode.com/res/hashnode/image/upload/v1762863191484/827d0731-a392-419f-b17b-9a3611a4f3b4.jpeg align="center")

### Où vivent les conteneurs ?

Puisque les conteneurs sont portables et peuvent être partagés entre équipes et systèmes, ils ont besoin d'un endroit où résider. C'est là qu'interviennent les dépôts de conteneurs (repositories) – des lieux de stockage spéciaux pour les conteneurs. Les organisations peuvent avoir des dépôts privés pour un usage interne, tandis que les dépôts publics comme [Docker Hub](https://hub.docker.com/) permettent à quiconque de parcourir et d'utiliser des conteneurs partagés.

![image de Docker Hub montrant un catalogue d'images](https://cdn.hashnode.com/res/hashnode/image/upload/v1762863680430/caddd581-08e1-45c7-a676-818ad364f56b.png align="center")

Si vous visitez la page du catalogue sur Docker Hub, vous verrez une variété de dépôts de conteneurs, officiels ou créés par la communauté, provenant de développeurs et d'équipes comme Redis, Jenkins et bien d'autres.

Autrefois, lorsque plusieurs développeurs travaillaient sur différents projets, chacun devait installer manuellement les services sur son propre système. Comme les développeurs utilisent souvent des systèmes d'exploitation différents comme Linux, macOS et Windows, le processus de configuration n'était jamais le même. Cela prenait beaucoup de temps, entraînait de nombreuses erreurs et faisait de la configuration de nouveaux environnements un véritable casse-tête, surtout lorsqu'il fallait le répéter pour plusieurs services.

Docker a changé la donne pour les développeurs et les équipes. Au lieu d'installer manuellement chaque service et dépendance, vous pouvez simplement lancer une seule commande Docker pour démarrer un conteneur. Chaque conteneur possède son propre environnement isolé avec tout ce dont il a besoin, de sorte qu'il fonctionne de la même manière sur n'importe quelle machine, qu'il s'agisse de Windows, macOS ou Linux. Cela rend la collaboration plus fluide et élimine tous les goulots d'étranglement liés aux configurations différentes, aux dépendances manquantes ou aux incompatibilités de version.

En résumé, Docker est une plateforme qui empaquette votre application et ses dépendances dans un conteneur unique et portable, afin qu'elle fonctionne de la même manière partout.

## Docker vs Machines Virtuelles

Docker et les machines virtuelles (VM) sont deux façons d'exécuter des applications dans un environnement « virtuel », mais ils fonctionnent différemment. Pour comprendre les différences, il est utile d'en savoir un peu plus sur la façon dont les ordinateurs exécutent les logiciels.

Un coup d'œil rapide sur les couches :

* **Kernel (Noyau) :** C'est la partie du système d'exploitation qui communique avec le matériel de votre ordinateur, comme le CPU, la mémoire et le disque. Considérez-le comme l'intermédiaire entre vos applications et votre ordinateur.
    
* **Couche applicative :** C'est là que les programmes et les applications s'exécutent. Elle se situe au-dessus du noyau et l'utilise pour accéder aux ressources matérielles.
    

Entrons maintenant un peu plus dans les détails des machines virtuelles. Une VM virtualise l'**intégralité du système d'exploitation**, ce qui signifie qu'elle possède son propre noyau et sa propre couche applicative. Lorsque vous téléchargez une VM, vous obtenez essentiellement un OS complet à l'intérieur de votre ordinateur, pesant souvent plusieurs gigaoctets.

Parce qu'elles doivent démarrer leur propre OS, les VM démarrent lentement. Mais les VM sont très compatibles et peuvent s'exécuter sur presque n'importe quel hôte car elles incluent tout ce dont elles ont besoin.

Docker, en revanche, ne virtualise que la **couche applicative**, pas l'OS complet. Les conteneurs partagent le noyau du système hôte mais incluent tout ce dont l'application a besoin : dépendances, bibliothèques et configuration.

Les images Docker sont petites, souvent quelques mégaoctets seulement. Les conteneurs démarrent presque instantanément car ils ne lancent pas un OS complet. Un conteneur Docker peut s'exécuter partout où Docker est installé, quel que soit le système d'exploitation utilisé par votre ordinateur.

En termes simples, pour résumer :

* Une VM, c'est comme faire tourner un ordinateur entier dans votre ordinateur – gros, lourd et lent.
    
* Un conteneur Docker est comme un paquet d'application autonome – petit, rapide et portable.
    

Voici une comparaison rapide :

| Caractéristique | Machine Virtuelle | Conteneur Docker |
| --- | --- | --- |
| Taille | Go (volumineux) | Mo (petit) |
| Vitesse de démarrage | Lente | Rapide |
| Couche OS | OS complet + noyau | Partage le noyau hôte |
| Portabilité | S'exécute sur hôte compatible | S'exécute partout où Docker est installé |

## Installation de Docker

Maintenant que vous savez ce qu'est Docker, installons-le sur votre machine.

Docker fonctionne sur Windows, macOS et Linux, mais chaque système a des étapes légèrement différentes. La [documentation](https://docs.docker.com/get-started/introduction/) officielle de Docker contient des instructions claires pour tous les systèmes d'exploitation sous la rubrique Docker Docs : Install Docker.

Si vous apprenez mieux visuellement, cette vidéo YouTube vous guide pas à pas dans l'installation de Docker sur Windows et Linux : [Regarder ici](https://www.youtube.com/watch?v=BuGEGM_elXY).

Voici une feuille de route simple :

Tout d'abord, vérifiez la configuration requise pour votre système. Docker ne fonctionne pas sur tous les ordinateurs, assurez-vous donc que la version de votre OS est prise en charge (la [doc](https://docs.docker.com/engine/install/) officielle contient une liste de contrôle).

1. Utilisateurs Windows et macOS :
    
    * **Systèmes récents :** Téléchargez et installez [**Docker Desktop**](https://docs.docker.com/desktop/)**.** C'est le moyen le plus simple de commencer.
        
    * **Systèmes plus anciens :** Si votre ordinateur ne prend pas en charge Docker Desktop (par exemple, absence d'Hyper-V ou anciennes versions d'OS), vous pouvez utiliser [**Docker Toolbox**](https://docker-docs.uclv.cu/toolbox/toolbox_install_windows/). Toolbox installe Docker à l'aide d'une machine virtuelle légère, ce qui vous permet de faire tourner des conteneurs même sur des machines anciennes.
        
2. Utilisateurs Linux : Vous installerez généralement Docker via votre gestionnaire de paquets (`apt` pour Ubuntu/Debian, `yum` pour CentOS/Fedora, etc.). La [doc](https://docs.docker.com/desktop/setup/install/linux/) officielle indique les commandes pour votre distribution.
    

Vérifiez ensuite votre installation : ouvrez un terminal ou une invite de commande et tapez :

```bash
docker --version
```

Si vous voyez la version de Docker s'afficher, félicitations ! Docker est prêt à l'emploi.

![version de Docker affichée dans le CLI](https://cdn.hashnode.com/res/hashnode/image/upload/v1762871221981/6b01cf18-a8b5-4aa9-b213-38cffd4ae5f4.png align="center")

Une fois Docker installé, vous serez prêt à lancer des conteneurs, à récupérer des images et à expérimenter vos applications dans un environnement sûr et isolé.

**Conseil pour les débutants :**

Si vous êtes sur une machine ancienne et utilisez Docker Toolbox, les commandes sont pratiquement les mêmes, mais vous les exécuterez dans le **Docker Quickstart Terminal**, qui configure la machine virtuelle pour vous.

## Commandes Docker de base

Jusqu'à présent, nous avons utilisé des termes comme images et conteneurs, parfois de manière interchangeable. Mais il existe une différence importante :

* **Image Docker :** Considérez une image comme un **plan** (blueprint) ou un paquet. Elle contient tout ce dont votre application a besoin : le code, les bibliothèques, les dépendances et la configuration, mais elle n'est pas encore en cours d'exécution.
    
* **Conteneur Docker :** Un conteneur est une **instance en cours d'exécution d'une image**. Lorsque vous démarrez un conteneur, Docker prend l'image et l'exécute dans son propre environnement isolé.
    

Un moyen simple de s'en souvenir est celui-ci : l'image est la recette, tandis que le conteneur est le gâteau. Vous pouvez avoir une seule recette (image) et faire plusieurs gâteaux (conteneurs) à partir de celle-ci.

**Note importante :** Docker Hub stocke des images, pas des conteneurs. Ainsi, lorsque vous récupérez quelque chose sur Docker Hub, vous téléchargez une image. Par exemple :

```bash
docker pull redis
```

Voici ce que vous verrez :

![docker run redis affiché dans le CLI](https://cdn.hashnode.com/res/hashnode/image/upload/v1762872367018/39039261-9617-4e5f-8156-9529697d0667.png align="center")

Cette commande télécharge l'image Redis sur votre machine. Une fois le téléchargement terminé, vous pouvez voir toutes les images que vous avez localement avec :

```bash
docker images
```

![exécution de docker images dans le CLI](https://cdn.hashnode.com/res/hashnode/image/upload/v1762872440545/bfdb401f-7dd6-4f72-920b-545fbf5193e1.png align="center")

À partir de là, vous pouvez démarrer un conteneur à partir d'une image dès que vous en avez besoin :

```bash
docker run -d --name my-redis redis
```

Cette commande démarre un conteneur, `my-redis`, à partir de l'image `redis` que vous venez de récupérer.

* `docker run` dit à Docker de démarrer un nouveau conteneur à partir d'une image.
    
* `-d` signifie « mode détaché » (detached mode). Cela signifie que le conteneur s'exécute en arrière-plan afin que vous puissiez continuer à utiliser votre terminal.
    
* `--name my-redis` donne à votre conteneur un nom convivial (`my-redis`) au lieu de laisser Docker en assigner un au hasard. Cela facilite la gestion ultérieure.
    
* `redis` est l'image que vous utilisez pour démarrer le conteneur.
    

Pour voir tous les conteneurs actuellement en cours d'exécution, vous pouvez utiliser :

```bash
docker ps
```

![exécution de docker ps dans le terminal pour lister les conteneurs actifs](https://cdn.hashnode.com/res/hashnode/image/upload/v1762873018123/2e184c25-e4f1-445c-b182-81987929c014.png align="center")

Cela listera les conteneurs avec des détails tels que :

* L'ID du conteneur
    
* Le nom
    
* Le statut (en cours d'exécution ou arrêté)
    
* L'image à partir de laquelle il s'exécute
    

Si vous voulez voir tous les conteneurs, même ceux qui ne sont pas en cours d'exécution, vous pouvez ajouter le drapeau `-a` :

```bash
docker ps -a
```

### Comment spécifier une version d'une image :

Par défaut, Docker récupère la **dernière version** (latest) d'une image. Mais vous pourriez parfois avoir besoin d'une version spécifique. Vous pouvez le faire en utilisant deux points (`:`) suivis du tag de version. Par exemple :

```bash
docker pull redis:7.2
docker run -d --name my-redis redis:7.2
```

Pour savoir quelles versions sont disponibles, vous pouvez visiter [**Docker Hub**](https://hub.docker.com/repositories) ou vérifier les tags d'image en ligne. De plus, l'exécution de `docker images` sur votre machine vous montrera toutes les images téléchargées et leurs versions.

### Comment arrêter, démarrer et supprimer un conteneur

Si vous voulez arrêter un conteneur en cours d'exécution, lancez ceci :

```bash
docker stop my-redis
```

Pour le redémarrer :

```bash
docker start my-redis
```

Vous pouvez également **supprimer un conteneur** si vous n'en avez plus besoin :

```bash
docker rm my-redis
```

### Comment redémarrer un conteneur

Vous pouvez redémarrer un conteneur en utilisant son **ID de conteneur** (ou son nom) si quelque chose plante, nécessite un rafraîchissement ou si vous voulez simplement appliquer des changements.

Par exemple :

```bash
docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS      NAMES
c002bed0ae9a   redis     "docker-entrypoint.s…"   3 minutes ago   Up 3 minutes   6379/tcp   my-redis
```

Redémarrez-le comme ceci :

```bash
docker restart c002bed0ae9a
```

ou par son nom :

```bash
docker restart my-redis
```

Autres moyens pratiques :

* **Arrêter puis démarrer**
    
    ```bash
    docker stop c002bed0ae9a
    docker start c002bed0ae9a
    ```
    
* **Démarrer avec les logs**
    
    ```bash
    docker start c002bed0ae9a && docker logs -f c002bed0ae9a
    ```
    

![démarrage d'un conteneur Docker avec les logs](https://cdn.hashnode.com/res/hashnode/image/upload/v1762873445952/ffb56b5d-f850-4b53-998d-467ed431a191.png align="center")

### Comment exécuter plusieurs conteneurs Redis et comprendre les ports

Actuellement, vous avez un conteneur Redis en cours d'exécution :

```bash
docker ps
```

Il affiche quelque chose comme ceci :

```bash
CONTAINER ID   IMAGE     COMMAND                  STATUS          PORTS      NAMES
c002bed0ae9a   redis     "docker-entrypoint.s…"   Up 20 minutes   6379/tcp   my-redis
```

Notez la colonne **PORTS** : `6379/tcp`. Cela signifie que le conteneur exécute Redis sur son port interne 6379. Par défaut, ce port est à l'intérieur du conteneur et n'est pas automatiquement exposé à votre ordinateur (l'hôte). Docker ne le mappe que si vous le spécifiez.

#### Essayer d'exécuter un autre conteneur Redis sur le même port

Si vous essayez :

```bash
docker run -d --name my-redis2 redis:7.4.7-alpine
```

Il échouera à mapper le port hôte 6379 car le premier conteneur l'utilise déjà. C'est là qu'intervient la liaison de ports (port binding).

#### Qu'est-ce que la liaison de ports (Port Binding) ?

La liaison de ports (également appelée mappage de ports) est le mécanisme utilisé par Docker pour connecter un port à l'intérieur d'un conteneur à un port sur votre machine hôte (votre ordinateur portable/bureau/serveur).

Sans liaison de ports, tout service s'exécutant à l'intérieur d'un conteneur est complètement isolé : il peut écouter sur ses ports internes (par exemple, Redis sur 6379, une application Node.js sur 3000, MongoDB sur 27017), mais rien à l'extérieur du conteneur, y compris votre navigateur, une autre application sur votre ordinateur ou même un autre conteneur sur un réseau différent, ne peut l'atteindre.

* **Port du conteneur** : Le port à l'intérieur du conteneur où l'application s'exécute (Redis utilise par défaut `6379`).
    
* **Port hôte** : Le port sur votre ordinateur que vous souhaitez utiliser pour accéder à ce conteneur.
    

Docker vous permet de mapper un port de conteneur à un port hôte différent en utilisant le drapeau `-p`.

#### Exécuter un deuxième conteneur Redis sur un port hôte différent

```bash
docker run -d --name my-redis2 -p 6380:6379 redis:7.4.7-alpine
```

`-p 6380:6379` mappe le port hôte 6380 au port du conteneur 6379.

* Vous pouvez maintenant vous connecter à Redis dans le deuxième conteneur en utilisant `localhost:6380`.
    
* À l'intérieur du conteneur, Redis s'exécute toujours sur le port 6379.
    

Vérifiez les deux conteneurs :

```bash
docker ps
```

La sortie ressemblera à ceci :

```bash
CONTAINER ID   IMAGE     STATUS          PORTS             NAMES
c002bed0ae9a   redis     Up 20 minutes   6379/tcp          my-redis
d123abcd5678   redis     Up 1 minute     0.0.0.0:6380->6379/tcp   my-redis2
```

Le premier conteneur s'exécute en interne sur 6379 (port hôte non exposé), tandis que le second conteneur est mappé de sorte que le port hôte 6380 transfère le trafic vers le port du conteneur 6379.

Imaginez chaque conteneur comme une pièce avec une ligne téléphonique (port du conteneur).

* Vous voulez appeler cette pièce de l'extérieur (hôte).
    
* Vous ne pouvez pas utiliser la même ligne téléphonique externe pour deux pièces en même temps.
    
* Avec la **liaison de ports**, vous assignez une ligne externe différente pour chaque pièce, même si le numéro de téléphone interne est le même.
    

#### Pourquoi la liaison de ports existe

1. **Éviter les conflits de ports sur l'hôte :** Un seul processus sur votre ordinateur peut utiliser un port donné à la fois. Si vous avez déjà un conteneur Redis utilisant le port hôte 6379, un deuxième conteneur ne peut pas se lier au même port hôte. La liaison de ports vous permet d'exécuter de nombreux conteneurs identiques côte à côte en mappant chacun d'eux à un port hôte différent (6379 → 6380, 6381, etc.).
    
2. **Accéder aux services conteneurisés depuis votre hôte :** Votre navigateur, Postman, MongoDB Compass, redis-cli, curl, etc., s'exécutent tous sur l'hôte. Sans -p, ils n'ont aucun moyen de communiquer avec les services à l'intérieur des conteneurs.
    
3. **Exposition sélective :** Vous n'avez pas besoin d'exposer chaque port utilisé par un conteneur. Ne mappez que les ports dont vous avez réellement besoin à l'extérieur, en gardant les autres privés et sécurisés.
    

Cela vous donne également plus de flexibilité en développement et en production. En développement, vous pourriez mapper le conteneur 3000 sur l'hôte 3000. Mais en production (par exemple, derrière un reverse proxy), vous pourriez mapper le conteneur 3000 sur l'hôte 80 ou 443, ou ne pas l'exposer du tout et laisser un autre conteneur lui parler via le réseau interne de Docker.

### Comment explorer un conteneur

Pour explorer un conteneur, lancez :

```bash
docker exec -it my-redis2 /bin/sh
```

* `docker exec` exécute une commande dans le conteneur.
    
* `-it` terminal interactif (vous permet de taper et de voir la sortie).
    
* `/bin/sh` démarre un shell à l'intérieur du conteneur.
    

Une fois à l'intérieur, votre invite de commande change pour quelque chose comme :

```bash
/data #
```

Vous pouvez maintenant **lister les fichiers**, naviguer dans les répertoires ou exécuter des programmes, le tout à l'intérieur du conteneur, sans affecter votre machine hôte.

![résultat de l'exécution de docker exec -it my-redis2 /bin/sh](https://cdn.hashnode.com/res/hashnode/image/upload/v1762876729378/d16e8f00-ab9c-447b-b274-76d613b30ce3.png align="center")

### `docker run` vs `docker start`

Nous avons utilisé `docker run` et `docker start` tout au long de cet article, mais voici pourquoi la différence est importante :

* **Éviter les doublons accidentels :** Utiliser `docker run` à chaque fois crée un nouveau conteneur. Si vous voulez simplement redémarrer quelque chose que vous avez déjà configuré, `docker start` est plus rapide et plus sûr.
    
* **Conserver la configuration :** `docker start` préserve les paramètres d'origine du conteneur, les ports, les volumes et les noms, de sorte que vous ne risquez pas de casser quoi que ce soit en changeant les options.
    
* **Travailler efficacement avec plusieurs conteneurs :** Lorsque vous exécutez plusieurs services ou différentes versions de la même application, savoir quand utiliser `run` ou `start` vous aide à gérer les ressources, à éviter les conflits de ports et à maintenir la fluidité de votre flux de travail.
    
* **Accélérer votre workflow :** Le démarrage de conteneurs existants est presque instantané, tandis que la création d'un nouveau prend un peu plus de temps.
    

**En résumé** : `docker run` = créer quelque chose de nouveau, tandis que `docker start` = reprendre ce que vous avez déjà.

## Pratique avec JavaScript

Maintenant que nous avons couvert les concepts fondamentaux de Docker, passons à l'action. Dans cette section, nous allons conteneuriser un projet JavaScript simple composé de :

* **Un frontend :** Construit avec HTML, CSS et JavaScript
    
* **Un backend :** Un serveur Node.js simple (`server.js`)
    
* **Une base de données :** Une instance MongoDB récupérée directement sur Docker Hub
    
* **Une interface pour MongoDB :** Utilisation de **Mongo Express** pour visualiser et gérer notre base de données
    

Cet exemple démontre comment Docker peut gérer plusieurs composants d'une application, y compris le code, les dépendances et les services dans des environnements isolés et cohérents.

Vous pouvez [récupérer le projet de départ sur GitHub ici](https://github.com/Oghenekparobo/docker_tut_js).

Ou clonez-le directement via votre terminal :

```bash
git clone https://github.com/Oghenekparobo/docker_tut_js.git
cd docker_tut_js
```

Cela contient les fichiers HTML et JavaScript de base ainsi que le backend Node.js.

Ensuite, nous allons nous préparer à configurer notre base de données. Rendez-vous sur [Docker Hub](https://hub.docker.com/) et tapez **« mongo »** dans la barre de recherche. Vous verrez l'image officielle de MongoDB publiée par Docker.

![base de données MongoDB officielle sur Docker Hub](https://cdn.hashnode.com/res/hashnode/image/upload/v1762950041097/89f54e21-f607-488a-8d98-d688733270c4.png align="center")

### Comment récupérer l'image MongoDB

Maintenant que vous avez exploré l'image officielle de MongoDB sur Docker Hub, récupérons-la réellement dans votre environnement local.

Ouvrez votre terminal, naviguez vers le répertoire de votre projet (par exemple, `docker_tut_js`), et lancez :

```bash
docker pull mongo
```

Cette commande dit à Docker de télécharger la dernière version de l'image MongoDB depuis Docker Hub.

Vous verrez une sortie similaire à celle-ci :

```bash
Using default tag: latest
latest: Pulling from library/mongo
b8a35db46e38: Already exists 
a637dbfff7e5: Pull complete 
0c9047ace63c: Pull complete 
02cd4cf70021: Pull complete 
dfb5d357a025: Pull complete 
007bf0024f67: Pull complete 
67fd8af3998d: Pull complete 
d702312e8109: Pull complete 
Digest: sha256:7d1a1a613b41523172dc2b1b02c706bc56cee64144ccd6205b1b38703c85bf61
Status: Downloaded newer image for mongo:latest
docker.io/library/mongo:latest
```

Voici ce qui se passe :

* **« Using default tag: latest »** : Docker récupère la version la plus récente de MongoDB puisqu'aucune version spécifique n'a été fournie.
    
* **« Pulling from library/mongo »** : Le téléchargement s'effectue depuis la bibliothèque d'images officielle de Docker.
    
* **« Pull complete »** : Chaque ligne représente une couche de l'image téléchargée avec succès.
    
* **« Downloaded newer image for mongo:latest »** : Confirme que l'image MongoDB est maintenant stockée localement sur votre système.
    

Vous pouvez confirmer qu'elle est disponible en lançant :

```bash
docker images
```

Vous devriez voir **mongo** listé dans la colonne repository.

![MongoDB listé dans la colonne repository après l'exécution de docker images](https://cdn.hashnode.com/res/hashnode/image/upload/v1762950246712/343d4d23-9c61-4480-956c-a5c2cd391889.png align="center")

### Comment récupérer l'image Mongo Express

Maintenant que l'image MongoDB est prête, récupérons l'image **Mongo Express**.

Mongo Express est une interface web légère qui vous permet de visualiser et de gérer vos collections MongoDB via un navigateur, de la même manière que phpMyAdmin fonctionne pour MySQL.

Ouvrez votre terminal (toujours dans le répertoire de votre projet) et lancez :

```bash
docker pull mongo-express
```

Vous verrez une sortie similaire à celle-ci :

```bash
Using default tag: latest
latest: Pulling from library/mongo-express
b8a35db46e38: Already exists
a637dbfff7e5: Pull complete
4e0e0977e9c3: Pull complete
02cd4cf70021: Pull complete
Digest: sha256:3d6dbac587ad91d0e2eab83f09a5b31a1c8f9d91a8825ddaa6c7453c25cb4812
Status: Downloaded newer image for mongo-express:latest
docker.io/library/mongo-express:latest
```

Voici ce que cela signifie :

* `docker pull mongo-express` télécharge l'image officielle de Mongo Express depuis Docker Hub.
    
* Chaque ligne **« Pull complete »** représente une couche de l'image téléchargée avec succès.
    
* `mongo-express:latest` confirme que la dernière version est maintenant stockée localement.
    

Pour vérifier que les deux images sont disponibles, lancez :

```bash
docker images
```

Vous devriez voir mongo et mongo-express listés dans la sortie.

![commande docker images montrant les images MongoDB et Mongo Express](https://cdn.hashnode.com/res/hashnode/image/upload/v1762951088081/06345eb1-80c9-4fcd-8585-5ff309ed2779.png align="center")

Maintenant que les deux images sont téléchargées, l'étape suivante consiste à lancer les conteneurs pour s'assurer que MongoDB est opérationnel et accessible, puis à le connecter à Mongo Express pour pouvoir le gérer via le navigateur.

Avant cela, examinons brièvement comment ces deux conteneurs vont communiquer.

### Réseau Docker

Lorsque MongoDB et Mongo Express s'exécutent dans des conteneurs séparés, ils ont besoin d'un moyen de se parler. Docker gère cela à l'aide d'un **Réseau Docker (Docker Network)**, un pont virtuel qui permet aux conteneurs de communiquer de manière sécurisée sans exposer les ports internes au monde extérieur.

Lorsque vous lancez des conteneurs dans Docker, celui-ci crée automatiquement un réseau isolé pour eux. Considérez cela comme un espace privé où vos conteneurs peuvent discuter en toute sécurité sans tout exposer à l'extérieur.

Par exemple, si notre conteneur MongoDB et notre conteneur Mongo Express sont sur le même réseau Docker, ils peuvent communiquer simplement en utilisant leurs noms de conteneurs (comme `mongo` ou `mongo-express`). Vous n'avez pas besoin d'utiliser `localhost` ou des numéros de port, car Docker gère cette partie en interne.

Cependant, tout ce qui se trouve en dehors du réseau Docker (comme votre machine hôte ou une application Node.js) se connecte via les ports exposés.

Ainsi, plus tard, lorsque nous empaquetterons l'intégralité de notre application (le backend Node.js, MongoDB, Mongo Express et même le frontend `index.html`) dans Docker, tous ces conteneurs interagiront de manière fluide via le réseau Docker. Le navigateur de votre ordinateur se connectera ensuite à votre application Node.js en utilisant l'adresse de l'hôte et le port que nous avons exposé.

Par défaut, Docker fournit déjà quelques réseaux intégrés. Vous pouvez les voir en lançant :

```bash
docker network ls
```

Vous obtiendrez quelque chose comme ceci :

```bash
NETWORK ID     NAME      DRIVER    SCOPE
712a7144f1a0   bridge    bridge    local
4ae27eedea5b   host      host      local
4806000201ce   none      null      local
```

Ceux-ci sont créés automatiquement par Docker. Vous n'avez pas à vous en soucier pour le moment – nous allons simplement nous concentrer sur la création de notre propre réseau personnalisé.

Pour notre configuration, nous allons créer un réseau séparé que MongoDB et Mongo Express pourront partager. Appelons-le mongo-network :

```bash
docker network create mongo-network
```

![mongo-network créé avec docker network create](https://cdn.hashnode.com/res/hashnode/image/upload/v1762953968310/bdf51a4e-1986-48a4-922b-6f312ff99414.png align="center")

## Comment lancer le conteneur Mongo

Pour s'assurer que nos conteneurs MongoDB et Mongo Express peuvent communiquer, nous devons les exécuter dans le même réseau Docker. C'est pourquoi nous avons créé mongo-network précédemment.

Commençons par MongoDB. Rappelez-vous, la commande `docker run` est utilisée pour démarrer un conteneur à partir d'une image. Dans ce cas, nous allons exécuter l'image officielle de MongoDB et l'attacher à notre réseau.

Nous allons également exposer le port par défaut de MongoDB 27017 afin qu'il soit accessible depuis l'extérieur du conteneur, et configurer des variables d'environnement pour le nom d'utilisateur et le mot de passe racine.

Voici la commande :

```bash
docker run -p 27017:27017 -d \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=password \
  --name mongo \
  --network mongo-network \
  mongo
```

Voici ce que fait chaque partie :

* `-p 27017:27017` mappe le port MongoDB du conteneur sur votre machine hôte.
    
* `-d` lance le conteneur en mode détaché (en arrière-plan).
    
* `-e` définit les variables d'environnement pour les identifiants racine de la base de données.
    
* `--name mongo` donne au conteneur un nom personnalisé pour une référence plus facile.
    
* `--network mongo-network` connecte le conteneur au réseau que nous avons créé.
    

Une fois qu'il s'exécute avec succès, votre instance MongoDB sera opérationnelle à l'intérieur du réseau Docker, prête à ce que d'autres conteneurs comme Mongo Express s'y connectent.

Après avoir créé votre conteneur MongoDB, vous pouvez facilement vérifier s'il fonctionne correctement.

Tout d'abord, lancez `docker ps` pour voir tous les conteneurs actifs. Vous devriez voir votre conteneur MongoDB (`mongo`) listé avec son port `27017` exposé. Pour obtenir plus de détails sur ce qui se passe à l'intérieur du conteneur, vous pouvez consulter ses logs en utilisant `docker logs mongo` ou, si vous préférez, en utilisant l'ID du conteneur (par exemple : `docker logs 7abb38175ae28`). Les logs afficheront les messages de démarrage de MongoDB, et vous devrez chercher les lignes indiquant que la base de données a démarré avec succès et est prête à accepter des connexions.

C'est un moyen rapide de vérifier que tout fonctionne correctement avant de connecter d'autres services, comme Mongo Express, à celle-ci.

```bash
docker ps
```

Cela listera tous les **conteneurs en cours d'exécution**. Vous devriez voir votre conteneur MongoDB (`mongo`) avec son port `27017` exposé.

```bash
docker logs mongo # ou l'id du conteneur
```

Cela affichera les messages de démarrage. Cherchez les lignes indiquant que MongoDB a démarré avec succès.

![vérification du fonctionnement du conteneur mongo](https://cdn.hashnode.com/res/hashnode/image/upload/v1762956236708/44dbe331-b736-4526-8dae-019150b618d8.png align="center")

## Comment lancer le conteneur Mongo Express

Maintenant que MongoDB est opérationnel, nous pouvons lancer Mongo Express, qui est une interface web pour gérer et visualiser vos bases de données MongoDB. Nous allons le connecter au même réseau (`mongo-network`) afin qu'il puisse communiquer avec MongoDB.

Voici la commande :

```bash
docker run -d \
  -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
  -e ME_CONFIG_MONGODB_ADMINPASSWORD=password \
  -e ME_CONFIG_MONGODB_SERVER=mongo \
  --name mongo-express \
  --network mongo-network \
  -p 8081:8081 \
  mongo-express
```

Voici ce que fait chaque partie :

* `-d` lance le conteneur en mode détaché (en arrière-plan).
    
* `-e ME_CONFIG_MONGODB_ADMINUSERNAME=admin` définit le nom d'utilisateur admin MongoDB que Mongo Express doit utiliser.
    
* `-e ME_CONFIG_MONGODB_ADMINPASSWORD=password` définit le mot de passe MongoDB correspondant.
    
* `-e ME_CONFIG_MONGODB_SERVER=mongo` indique à Mongo Express à quel serveur MongoDB se connecter. Ici, nous utilisons le nom du conteneur `mongo` car les deux conteneurs sont sur le même réseau.
    
* `--name mongo-express` donne au conteneur un nom convivial.
    
* `--network mongo-network` connecte le conteneur au même réseau Docker que MongoDB.
    
* `-p 8081:8081` expose l'interface web de Mongo Express sur le port `8081` de votre machine hôte.
    
* `mongo-express` le nom de l'image Docker que nous exécutons.
    

Une fois le conteneur lancé, vous pouvez ouvrir votre navigateur et visiter `http://localhost:8081` pour accéder à Mongo Express et interagir avec votre instance MongoDB.

Pour plus de détails sur les variables d'environnement et les options disponibles, vous pouvez consulter la page officielle Docker Hub de Mongo Express [ici](https://hub.docker.com/_/mongo-express).

Avant d'ouvrir votre navigateur sur [`http://localhost:8081`](http://localhost:8081), il est conseillé de vérifier si le conteneur Mongo Express fonctionne correctement. Vous pouvez le faire en consultant ses logs :

```bash
docker logs mongo-express
```

Vous devriez voir une sortie similaire à celle-ci :

```bash
Waiting for mongo:27017...
No custom config.js found, loading config.default.js
Welcome to mongo-express 1.0.2
------------------------
Mongo Express server listening at http://0.0.0.0:8081
Server is open to allow connections from anyone (0.0.0.0)
basicAuth credentials are "admin:pass", it is recommended you change this in your config.js!
```

Cela confirme que Mongo Express est opérationnel et prêt à se connecter à votre instance MongoDB.

Notez les identifiants basicAuth affichés dans les logs (admin:pass). Si ces identifiants sont présents, vous devrez les utiliser pour accéder à Mongo Express depuis votre navigateur. Plus tard, vous pourrez les modifier dans un fichier config.js personnalisé pour une meilleure sécurité.

Une fois que tout semble correct dans les logs, vous pouvez visiter [`http://localhost:8081`](http://localhost:8081) en toute sécurité.

![interface mongo-express sur http://localhost:8081](https://cdn.hashnode.com/res/hashnode/image/upload/v1762957766334/f64b1f06-87a8-4ffb-b905-47e1871cca64.png align="center")

Si votre navigateur demande un nom d'utilisateur et un mot de passe, utilisez les identifiants basicAuth indiqués dans les logs du conteneur :

```bash
Username: admin
Password: pass
```

Ce sont les identifiants par défaut, et il est **fortement recommandé** de les changer plus tard.

Lorsque vous ouvrirez Mongo Express, vous remarquerez que certaines bases de données par défaut sont déjà créées. Pour ce projet, nous allons créer une nouvelle base de données appelée `todos`. Une fois créée, votre application Node.js pourra se connecter à cette base de données pour stocker et récupérer des données.

## Comment connecter Node.js à MongoDB

Vous avez déjà MongoDB qui tourne dans un conteneur Docker (mongo). Le conteneur expose le port MongoDB par défaut 27017 à l'hôte, de sorte que n'importe quel processus sur votre ordinateur peut l'atteindre via [localhost:27017](http://localhost:27017).

**Important :** L'application Node.js est **en dehors de Docker** (c'est juste un processus `node server.js` classique que vous lancez depuis votre terminal).

Comme l'application est externe, nous **devons utiliser** [**localhost**](http://localhost) (ou 127.0.0.1) comme nom d'hôte – et **non** le nom du conteneur `mongo`.

Une fois que nous aurons conteneurisé l'application Node.js et que nous l'aurons placée sur le même réseau Docker, nous passerons l'hôte à `mongo`. Pour l'instant, gardez [localhost](http://localhost).

### Backend Node.js

Voici une version de notre `server.js` utilisant MongoDB :

```javascript
const express = require("express");
const multer = require("multer");
const path = require("path");
const fs = require("fs");
const { MongoClient, ObjectId } = require("mongodb");

const app = express();
const PORT = 3000;

// Host = localhost  →  communique avec le conteneur MongoDB via le port exposé
// Port = 27017      →  port MongoDB par défaut
// User / Pass       →  admin / password (les identifiants donnés au conteneur)
const mongoUrl = "mongodb://admin:password@localhost:27017";
const dbName = "todos";
let db;

MongoClient.connect(mongoUrl)
  .then((client) => {
    db = client.db(dbName);
    console.log("Connecté à MongoDB →", dbName);
  })
  .catch((err) => console.error("Erreur de connexion MongoDB :", err));

const uploadDir = path.join(__dirname, "uploads");
if (!fs.existsSync(uploadDir)) fs.mkdirSync(uploadDir);

const storage = multer.diskStorage({
  destination: (req, file, cb) => cb(null, uploadDir),
  filename: (req, file, cb) => {
    const unique = Date.now() + "-" + Math.round(Math.random() * 1e9);
    cb(null, "photo-" + unique + path.extname(file.originalname));
  },
});
const upload = multer({ storage });

app.use(express.static(__dirname));
app.use("/uploads", express.static(uploadDir));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get("/todos", async (req, res) => {
  const todos = await db.collection("todos").find().toArray();
  res.json(todos);
});

app.post("/todos", upload.single("photo"), async (req, res) => {
  const text = req.body.text?.trim();
  if (!text) return res.status(400).json({ error: "Texte requis" });

  const todo = {
    text,
    image: req.file ? `/uploads/${req.file.filename}` : null,
    createdAt: new Date(),
  };

  const result = await db.collection("todos").insertOne(todo);
  todo._id = result.insertedId;
  res.json(todo);
});

// Démarrer le serveur
app.listen(PORT, () => {
  console.log(`Serveur → http://localhost:${PORT}`);
});
```

### **Frontend**

`index.html` :

```xml
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <title>Todo + Image</title>
    <style>
      body {
        font-family: sans-serif;
        margin: 2rem;
        max-width: 800px;
      }
      .todo {
        border: 1px solid #ccc;
        padding: 1rem;
        margin-bottom: 1rem;
        border-radius: 8px;
      }
      .todo img {
        max-height: 150px;
        margin-top: 0.5rem;
      }
      .error {
        color: red;
      }
      input[type="text"] {
        width: 100%;
        padding: 0.5rem;
        margin-bottom: 0.5rem;
      }
      #preview {
        max-width: 300px;
        margin-top: 0.5rem;
        display: none;
      }
    </style>
  </head>
  <body>
    <h1>Liste de tâches avec images</h1>

    <div id="addForm">
      <input type="text" id="textInput" placeholder="Que faut-il faire ?" />
      <input type="file" id="imageInput" accept="image/*" />
      <img id="preview" alt="aperçu" />
      <button id="addBtn">Ajouter</button>
      <p id="status"></p>
    </div>

    <h2>Tâches</h2>
    <div id="todos"></div>

    <script>
      const $ = document.querySelector.bind(document);

      const textInput = $("#textInput");
      const imageInput = $("#imageInput");
      const preview = $("#preview");
      const addBtn = $("#addBtn");
      const status = $("#status");
      const todosDiv = $("#todos");

      imageInput.addEventListener("change", () => {
        const file = imageInput.files[0];
        if (!file) {
          preview.style.display = "none";
          return;
        }
        const reader = new FileReader();
        reader.onload = (e) => {
          preview.src = e.target.result;
          preview.style.display = "block";
        };
        reader.readAsDataURL(file);
      });

      addBtn.addEventListener("click", async () => {
        const text = textInput.value.trim();
        if (!text) {
          status.textContent = "Veuillez entrer un texte.";
          status.className = "error";
          return;
        }

        const form = new FormData();
        form.append("text", text);
        if (imageInput.files[0]) form.append("photo", imageInput.files[0]);

        try {
          const res = await fetch("/todos", { method: "POST", body: form });
          const data = await res.json();
          if (!res.ok) throw new Error(data.error || "échec");
          status.textContent = "Tâche ajoutée !";
          status.className = "";
          textInput.value = "";
          imageInput.value = "";
          preview.style.display = "none";
          loadTodos(); // rafraîchir la liste
        } catch (err) {
          status.textContent = "Erreur : " + err.message;
          status.className = "error";
        }
      });

      async function loadTodos() {
        const res = await fetch("/todos");
        const todos = await res.json();
        todosDiv.innerHTML = "";
        todos.forEach((t) => {
          const div = document.createElement("div");
          div.className = "todo";
          div.innerHTML = `<strong>${escapeHtml(t.text)}</strong>`;
          if (t.image) {
            div.innerHTML += `<br><img src="${t.image}" alt="image todo">`;
          }
          todosDiv.appendChild(div);
        });
      }

      function escapeHtml(s) {
        const div = document.createElement("div");
        div.textContent = s;
        return div.innerHTML;
      }

      loadTodos();
    </script>
  </body>
</html>
```

Maintenant, votre application Node.js peut se connecter au conteneur MongoDB s'exécutant dans Docker. Comme l'application s'exécute en dehors de Docker pour le moment, elle se connecte via `localhost:27017` en utilisant les identifiants que vous avez définis (`admin` / `password`).

Une fois connecté, votre backend Node.js stocke et récupère les tâches directement depuis la base de données `todos` dans MongoDB. Plus tard, si vous conteneurisez l'application Node.js et la placez sur le même réseau Docker que MongoDB, vous pourrez changer l'hôte de `localhost` vers le nom du conteneur `mongo`. Nous y arrivons.

Vous pouvez trouver le code complet prêt à l'emploi ici : [Dépôt GitHub](https://github.com/Oghenekparobo/docker_tut_js/tree/mongodb-connection).

## Comment utiliser Docker Compose

Nous avons maintenant notre application Node.js connectée à MongoDB et Mongo Express, tous deux s'exécutant dans des conteneurs. Nous avons créé le réseau, démarré les conteneurs, et tout communique parfaitement.

Mais soyons honnêtes : taper toutes ces longues commandes `docker run` à chaque fois peut devenir fastidieux. Vous voulez probablement un moyen plus simple et plus propre de tout lancer avec une seule commande. C'est là qu'intervient **Docker Compose**.

Docker Compose est un outil qui vous permet de définir et d'exécuter des applications multi-conteneurs avec une seule commande. Au lieu d'exécuter manuellement plusieurs commandes `docker run`, vous décrivez votre configuration dans un simple fichier `docker-compose.yml`, en spécifiant chaque service (comme votre application Node.js, MongoDB et Mongo Express), leurs configurations, les variables d'environnement et les réseaux partagés.

En gros, cela vous permet de gérer plusieurs conteneurs comme un seul projet, facile à démarrer, à arrêter et à maintenir avec un seul fichier et une seule commande.

La convention de nommage standard est `docker-compose.yml` (ou `docker-compose.yaml`).

Docker le détecte automatiquement lorsque vous lancez :

```bash
docker compose up
```

Maintenant, au lieu de taper ces longues commandes à chaque fois, nous allons les combiner et tout lancer d'un coup en utilisant un **fichier Docker Compose**.

Le fichier `docker-compose.yml` sera situé à la racine de notre projet Node.js.

![fichier docker-compose.yml à la racine du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1763032152636/7fc026ba-d593-4097-a34c-945b398f2aeb.png align="center")

Voici à quoi ressemble notre fichier `docker-compose.yml` :

```yaml
version: "3.8"

services:
  mongodb:
    image: mongo
    container_name: mongo
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: password

  mongo-express:
    image: mongo-express
    container_name: mongo-express
    ports:
      - "8081:8081"
    environment:
      ME_CONFIG_MONGODB_ADMINUSERNAME: admin
      ME_CONFIG_MONGODB_ADMINPASSWORD: password
      ME_CONFIG_MONGODB_SERVER: mongodb
    depends_on:
      - mongodb
```

Analysons ce qui se passe ici :

* `version: "3.8"` : Définit la **version du fichier Compose**. La version 3.8 est moderne et fonctionne avec le dernier moteur Docker.
    
* `services:` : Tous les conteneurs que nous voulons exécuter sont définis ici. Dans notre cas, deux services : `mongodb` et `mongo-express`.
    

**Service MongoDB :**

* `image: mongo` récupère l'image officielle MongoDB.
    
* `container_name: mongo` donne un nom convivial au conteneur.
    
* `ports: "27017:27017"` expose le port par défaut de MongoDB sur notre hôte.
    
* `environment:` configure le nom d'utilisateur et le mot de passe racine.
    

**Service Mongo Express :**

* `image: mongo-express` est l'image officielle Mongo Express.
    
* `container_name: mongo-express` est un nom convivial.
    
* `ports: "8081:8081"` expose l'interface web sur le port hôte 8081.
    
* `environment:` indique à Mongo Express comment se connecter à MongoDB.
    
* `depends_on: - mongodb` garantit que MongoDB démarre en premier.
    

### Pourquoi utiliser Docker Compose ?

* **Commande unique** : Au lieu de plusieurs commandes `docker run`, lancez simplement :
    

```bash
docker compose up -d
```

* **Réseautage automatique** : Compose crée un réseau par défaut pour que les services communiquent via leurs **noms de service** (`mongodb` dans notre cas).
    
* **Maintenance facilitée** : Vous pouvez arrêter, démarrer ou reconstruire tous les services avec des commandes simples.
    

Avant de lancer notre nouveau `docker-compose.yml`, il est important de s'assurer qu'aucun conteneur conflictuel n'est en cours d'exécution. Arrêtez et supprimez les conteneurs précédents :

```bash
# Arrêter et supprimer tous les conteneurs du projet
docker stop mongo mongo-express
docker rm mongo mongo-express
```

Une fois l'environnement propre, lancez Docker Compose :

```bash
docker compose up -d
```

Vous devriez voir une sortie indiquant que le réseau et les conteneurs ont été créés et démarrés.

![docker compose up -d a créé les conteneurs avec succès](https://cdn.hashnode.com/res/hashnode/image/upload/v1763034021801/c4f806d2-080f-4b52-9f36-7b2044a7f8c5.png align="center")

À ce stade, sachez que les données ajoutées à MongoDB sont temporaires. Si vous supprimez les conteneurs, les données disparaissent. Nous verrons comment rendre les données persistantes plus tard avec les **volumes Docker**.

Vous pouvez obtenir un échantillon complet, incluant le Dockerfile **et** le fichier docker-compose, [ici](https://github.com/Oghenekparobo/docker_tut_js/tree/docker-compose).

## Comment construire notre propre image Docker

Maintenant que nous avons testé notre application localement, l'étape suivante est de la préparer pour le déploiement en créant une image Docker. Cela permet d'empaqueter l'application avec toutes ses dépendances dans une unité portable unique.

Pour conteneuriser notre application, nous avons besoin d'un **Dockerfile**. C'est un plan qui indique à Docker comment construire l'image.

Créez un fichier nommé `Dockerfile` (avec un `D` majuscule) à la racine de votre projet :

```yaml
# Utiliser Node 18 complet (basé sur Debian)
FROM node:18

# Définir les variables d'environnement
ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PASSWORD=password

# Définir le répertoire de travail
WORKDIR /home/app

# Copier les fichiers package
COPY package*.json ./

# Installer les dépendances
RUN npm install

# Copier le code source
COPY . .

# Exposer le port
EXPOSE 3000

# Démarrer l'application
CMD ["node", "server.js"]
```

### Construire l'image

Lancez la commande suivante dans votre terminal :

```bash
docker build -t todo-app:1.0 .
```

* `-t todo-app:1.0` donne un nom et un tag à votre image.
* `.` indique que le contexte de construction est le répertoire actuel.

### La solution au problème de connexion

Si vous lancez le conteneur et obtenez une erreur `ENOTFOUND mongodb`, c'est parce que `localhost` dans un conteneur se réfère au conteneur lui-même. Vous devez modifier `server.js` pour utiliser le nom du service défini dans Docker Compose :

```javascript
// Changez ceci :
const mongoUrl = "mongodb://admin:password@localhost:27017";

// Par ceci :
const mongoUrl = "mongodb://admin:password@mongodb:27017";
```

### Pourquoi `mongodb` fonctionne

Le nom d'hôte `mongodb` correspond au nom du service dans votre `docker-compose.yml`. Docker fournit un DNS interne qui résout ces noms en adresses IP de conteneurs.

### Ajouter votre application à Docker Compose

Mettez à jour votre `docker-compose.yml` :

```yaml
services:
  # ... services mongodb et mongo-express ...

  todo-app:
    image: todo-app:1.0
    container_name: todo-app
    ports:
      - "3000:3000"
    depends_on:
      - mongodb
```

### Démarrer tous les services

```bash
docker compose down
docker compose up -d
```

### Vérifier que tout fonctionne

Accédez à `http://localhost:3000` pour votre application et `http://localhost:8081` pour Mongo Express.

## Comment gérer vos conteneurs

* **Arrêter tout** : `docker compose down`
* **Voir les logs** : `docker compose logs -f todo-app`
* **Reconstruire après modif** : `docker build -t todo-app:1.0 .` puis `docker compose up -d`.

## Comment créer un dépôt Docker privé

Nous allons utiliser [**AWS Elastic Container Registry (ECR)**](https://aws.amazon.com/ecr/) pour stocker notre image de manière sécurisée.

1. Créez un dépôt nommé `todo-app` dans la console AWS ECR.
2. Obtenez vos clés d'accès AWS (Access Key ID et Secret Access Key).
3. Configurez AWS CLI : `aws configure`.
4. Connectez Docker à ECR :

```bash
aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin <VOTRE_ID_AWS>.dkr.ecr.eu-north-1.amazonaws.com
```

### Étape 6 : Construire, taguer et pousser votre image

```bash
# Taguer l'image pour ECR
docker tag todo-app:1.0 <VOTRE_ID_AWS>.dkr.ecr.eu-north-1.amazonaws.com/todo-app:1.0

# Pousser l'image
docker push <VOTRE_ID_AWS>.dkr.ecr.eu-north-1.amazonaws.com/todo-app:1.0
```

## **Exercice : Créer et pousser une nouvelle version**

Faites une petite modification dans votre code, reconstruisez l'image avec le tag `2.0` et poussez-la sur ECR.

### Déploiement de notre image

Dans votre `docker-compose.yml`, remplacez l'image locale par l'URI complète d'ECR :

```yaml
image: <VOTRE_ID_AWS>.dkr.ecr.eu-north-1.amazonaws.com/todo-app:1.0
```

## Volumes Docker

Pour éviter de perdre vos données MongoDB à chaque redémarrage, utilisez des **volumes**.

### Types de volumes Docker

1. **Volumes nommés** : Gérés par Docker, parfaits pour les bases de données.
2. **Bind Mounts** : Mappent un dossier de l'hôte vers le conteneur, idéal pour le développement.

### Exemple de fichier Docker Compose utilisant des volumes

```yaml
services:
  my-app:
    # ...
    volumes:
      - ./uploads:/usr/src/app/uploads

  mongodb:
    # ...
    volumes:
      - mongo-data:/data/db

volumes:
  mongo-data:
```

### Démarrer votre application

Lancez `docker compose up -d`. Vos données MongoDB seront désormais conservées dans le volume `mongo-data` même après un `docker compose down`.

## Conclusion

Félicitations, vous avez terminé ce tutoriel complet sur Docker ! Vous avez appris à conteneuriser une application, à utiliser Docker Compose, à gérer la persistance avec les volumes et à déployer sur un registre privé AWS ECR.

Ces compétences transformeront votre façon de développer et de déployer. Continuez à expérimenter et à explorer l'écosystème Docker !

Retrouvez le code final ici : [https://github.com/Oghenekparobo/docker_tut_js/tree/final](https://github.com/Oghenekparobo/docker_tut_js/tree/final)