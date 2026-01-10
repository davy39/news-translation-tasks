---
title: 'Docker : aussi simple que build, run, done !'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-22T19:51:54.000Z'
originalURL: https://freecodecamp.org/news/docker-easy-as-build-run-done-e174cc452599
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7a8Qffxkg7WuePBZUebYSw.png
tags:
- name: containers
  slug: containers
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: 'Docker : aussi simple que build, run, done !'
seo_desc: 'By Kangze Huang

  Docker has been getting a lot of buzz recently, and for good reason. The containerization
  service makes deploying microservices easy and stable, as each service can run an
  OS in its own virtual environment. That means full compatibili...'
---

Par Kangze Huang

Docker a beaucoup fait parler de lui récemment, et pour de bonnes raisons. Le service de conteneurisation rend le déploiement de microservices facile et stable, car chaque service peut exécuter un système d'exploitation dans son propre environnement virtuel. Cela signifie une compatibilité totale… plus besoin de s'inquiéter des versions de système d'exploitation, des dépendances et des différences entre vos machines de développement et de production ! Et pour couronner le tout, il est léger, vous pouvez donc exécuter plusieurs conteneurs Docker sur la même machine (instance EC2). Aujourd'hui, nous allons apprendre comment installer et déployer Docker sur Amazon EC2 en 3 étapes faciles !

Avant de commencer, jetez un coup d'œil à ce diagramme de haut niveau (courtoisie de [infoworld.com](http://www.infoworld.com/article/3072929/linux/containers-101-linux-containers-and-docker-explained.html)).

![Image](https://cdn-media-1.freecodecamp.org/images/i20ggtE0inu72rVUimBydJ0EHmL9xjWyWiuf)

À gauche se trouve votre configuration traditionnelle de machine virtuelle utilisant un hyperviseur. Un hyperviseur est simplement votre gestionnaire de VM responsable de l'allocation des ressources matérielles à chaque système d'exploitation virtuel. Si chaque système d'exploitation invité nécessite 1 Go de mémoire, et que l'hôte utilise 1 Go de mémoire, alors la configuration de gauche nécessiterait 4 Go au total.

À droite se trouve une configuration de conteneur, qui exécuterait un moteur de conteneur tel que Docker. La différence la plus significative est qu'un moteur de conteneur est plus léger car il peut partager certaines ressources matérielles avec son système d'exploitation hôte, contrairement aux machines virtuelles traditionnelles qui nécessitent leur propre allocation séparée. Cette configuration nécessite 1 Go pour le système d'exploitation hôte et peut-être 600 Mo par conteneur (car 300 Mo sont hypothétiquement partagés avec le système d'exploitation hôte), pour un total de 2,8 Go requis. Vous voyez ces avantages ? Cool, maintenant nous pouvons commencer !

### Pour commencer

Entrez dans votre instance EC2 et clonez [Kangzeroos-ES6-React-Redux-Boilerplate](https://github.com/kangzeroo/Kangzeroos-ES6-React-Redux-Boilerplate) depuis Github. Le code que vous voyez sera pour configurer cette application web, mais les étapes sont les mêmes pour tout projet. Une fois téléchargé, allez dans le dossier et trouvez les fichiers ci-dessous. Ce sont les fichiers que nous utiliserons avec Docker.

```bash
Dockerfile
build.sh
run.sh
```

Avant de pouvoir utiliser Docker, nous devons d'abord l'installer. Voici la méthode rapide et simple pour installer Docker, mais si vous souhaitez la configuration complète, consultez la [documentation officielle](https://docs.docker.com/engine/installation/linux/ubuntulinux/).

```bash
$ sudo apt-get update
$ sudo apt-get install docker-engine
$ sudo service docker start
$ sudo docker run hello-world
```

La dernière commande vérifie si Docker est en cours d'exécution, puis se termine. Si tout cela fonctionne, vous êtes prêt à commencer à Dockeriser !

### Étape 1 : Construire le Dockerfile

La première étape consiste à configurer les fichiers nécessaires pour que Docker construise une image. Les images Docker sont simplement des plans d'environnements que vous souhaitez créer, tandis que les conteneurs sont les environnements en cours d'exécution et fonctionnels dans lesquels votre application sera exécutée. À la racine de notre répertoire d'application, il y a un dossier appelé `App`. L'application web elle-même réside dans ce dossier `App`, tandis que tout ce qui concerne Docker est à l'extérieur. Cela est nécessaire car Docker conteneurisera tout ce qui se trouve dans `App`. Alors créons le premier fichier Docker appelé `Dockerfile` (sans extension de fichier `Dockerfile.sh`, juste `Dockerfile`) et parcourons-le ligne par ligne.

```docker
FROM ubuntu 

# configuration ubuntu
RUN apt-get update -y
RUN apt-get upgrade -y 
RUN apt-get install nodejs -y && apt-get install npm -y 

# installer curl pour n
RUN apt-get install curl -y
RUN apt-get install vim -y 

# obtenir la dernière version stable de node
RUN npm cache clean -f
RUN npm install -g n
RUN n stable 

# configurer le répertoire de travail
# ADD /App /App
WORKDIR /App
RUN npm install 

# exposer le port
EXPOSE 8080
```

La première ligne est `FROM ubuntu`. Le but de `Dockerfile` est de configurer le système d'exploitation et les programmes à l'intérieur du système d'exploitation, il est donc logique que la première ligne spécifie quelle version du système d'exploitation utiliser. `ubuntu` ici fait référence à une image spécifique hébergée sur [Docker Hub](https://hub.docker.com/_/ubuntu/), spécifiquement l'image officielle du système d'exploitation Ubuntu.

```docker
# configuration ubuntu
RUN apt-get update -y
RUN apt-get upgrade -y 
RUN apt-get install curl -y
RUN apt-get install vim -y
```

Le prochain ensemble de lignes est la configuration dans Ubuntu. Nous voulons vérifier les mises à jour d'Ubuntu avec `RUN apt-get update -y` et les mises à niveau avec `RUN apt-get upgrade -y`… des choses assez standard pour configurer votre environnement. Installez également curl `RUN apt-get install curl -y` et vim `RUN apt-get install vim -y`, tous deux utiles à avoir pour des fins générales.

```docker
# obtenir la dernière version stable de node
RUN apt-get install nodejs -y && apt-get install npm -y
RUN npm cache clean -f
RUN npm install -g n
RUN n stable
```

Le prochain ensemble de lignes est la configuration spécifique à NodeJS. Puisque nous voulons utiliser les fonctionnalités ES6, nous aurons besoin de la dernière version de NodeJS obtenue via le module node `n`. Installez NodeJS et NPM avec `RUN apt-get install nodejs -y && apt-get install npm -y`. Ensuite, nettoyez npm pour faire place à `n` en utilisant `RUN npm cache clean -f`. Installez `n` avec `RUN npm install -g n`. Et enfin, nous pouvons exécuter `n` (dernière version de NodeJS) avec `RUN n stable`.

NodeJS est pour Javascript, mais si vous travailliez avec d'autres langages comme Python, vous installeriez les programmes nécessaires pour exécuter votre application Python.

```docker
# configurer le répertoire de travail
ADD /App /App
WORKDIR /App
RUN npm install

# exposer le port
EXPOSE 8080
```

La dernière partie de `Dockerfile` consiste à configurer le répertoire de travail de l'application elle-même. `ADD /App /App` prend le dossier `App` de notre machine et le copie dans le conteneur Docker. Ensuite, `WORKDIR /App` définit le répertoire de travail Docker sur `/App` afin que toute commande que vous exécutez dans Docker soit exécutée dans `/App`. Cela est nécessaire pour que `npm install` installe au bon endroit (c'est-à-dire `/App` du conteneur Docker).

Enfin, nous exécutons `RUN npm install` qui installe nos dépendances NodeJS dans notre machine. Enfin, nous allons explicitement exposer le port 8080 de notre image Docker avec `EXPOSE 8080` afin que le monde extérieur puisse accéder à notre application. Le monde extérieur inclut Internet ainsi que d'autres conteneurs Docker s'exécutant sur la même machine.

### Étape 2 : Le script de build

```bash
docker build -t kangzeroo .
```

Créez un nouveau fichier dans le répertoire racine de votre application appelé `build.sh`. Il s'agit d'un fichier shell pour construire notre conteneur Docker. Ce fichier `build.sh` n'est pas réellement nécessaire car nous pouvons directement exécuter cette commande dans le terminal. Cependant, il est vraiment utile pour simplifier le processus.

Voici la décomposition de cette ligne : `docker build` est la commande qui indique à Docker de construire une image. `-t kangzeroo` définit le nom de l'étiquette de l'image Docker sur `kangzeroo`, que nous pouvons référencer plus tard. Veuillez noter que pour avoir un nom d'étiquette valide, il doit être en minuscules et sans espaces (utilisez la nomenclature snake-case). Enfin, `.` indique à Docker où chercher le `Dockerfile` nécessaire pour la construction ( `.` signifie ici).

Si vous êtes dans une instance EC2, nous pouvons exécuter `bash build.sh` depuis le répertoire racine de notre projet. Cela démarrera le processus de construction Docker alors qu'il parcourt les étapes du `Dockerfile` que nous avons créé. Cela peut prendre un certain temps… à la fin, cela devrait ressembler à ceci : (Ne vous inquiétez pas des erreurs non critiques telles que la dépendance optionnelle ignorée dans la capture d'écran ci-dessous).

![Image](https://cdn-media-1.freecodecamp.org/images/JkB7ysJBDpmxI9EQPD4xLOcTSx4bUTcixmVp)

Maintenant, vérifions si notre image a été créée. Tapez `docker images` pour voir les images actuellement en cours d'exécution sur notre machine. Vous devriez voir un résultat comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/u4LjgBDkjUNFqSP6pqqKPPE8MI7-Md056wl4)

Si nous voulons supprimer cette image, tapez simplement `docker rmi kangzeroo`. Si vous tapez `docker images` à nouveau après la suppression, vous verrez que l'image n'est plus là. Pour l'instant, laissons l'image car nous allons l'utiliser pour construire le conteneur Docker pour que notre application s'y exécute.

### Étape 3 : Le script d'exécution

Maintenant que notre image a été créée, créons `run.sh`. Rappelez-vous que les images Docker sont simplement des plans d'environnements que vous souhaitez créer. Les conteneurs sont les environnements en cours d'exécution et fonctionnels dans lesquels votre application sera exécutée. Donc `run.sh` transformera nos images en conteneurs. Voici à quoi ressemble `run.sh` :

```bash
docker run -d -it -p 80:8080 --name=kz kangzeroo npm run ec2 -- --host=0.0.0.0
```

Parcourons ce court script. `docker run` est la commande pour exécuter un conteneur à partir d'une image. `-d -it` est la commande pour `daemon` (exécution des tâches en arrière-plan) et `interactive terminal` (nous donnant un moyen d'interagir avec le conteneur). Si vous omettez `-d`, alors le conteneur docker ne s'exécutera pas en arrière-plan et vous verrez la sortie du journal de l'application. `-p 80:8080` mappe le port 80 de notre machine au port 8080 du conteneur. Rappelez-vous que précédemment nous avons spécifié `EXPOSE 8080` dans notre `Dockerfile`. Maintenant, nous prenons les connexions entrantes sur le port 80 de notre machine (le port 80 est le port par défaut pour http) et les redirigeons vers le port 8080 de notre conteneur. Si votre application n'est pas une page web, alors vous pouvez exclure ce mappage de port. `--name=kz` donne à notre conteneur le nom `kz`. Enfin, `kangzeroo npm run ec2` fait référence à notre image appelée `kangzeroo` et `npm run ec2` est une commande spécifique à cette application boilerplate (pour démarrer l'application). La dernière partie `--host=0.0.0.0` configure le boilerplate pour s'exécuter sur 0.0.0.0 au lieu de localhost (cela aussi est spécifique au boilerplate). Si vous exécutiez une application backend Python, cela ressemblerait à `docker run -d -it --name=kz kangzeroo python app.py`.

Super ! Enregistrez ce fichier et exécutez-le avec `bash run.sh`. Ensuite, vérifiez si le conteneur est en cours d'exécution en tapant `docker ps -a`. Voici à quoi cela devrait ressembler :

![Image](https://cdn-media-1.freecodecamp.org/images/4IeTxhM0cdOFBjxK5VTO0A5n83aj9avS4pB0)

Votre application est maintenant en ligne et s'exécute dans un conteneur Docker ! Vérifiez si cela fonctionne… pour ce boilerplate, vous pouvez vérifier depuis un navigateur web.

![Image](https://cdn-media-1.freecodecamp.org/images/LJagISP2Dvr9TTLYnhJD6yLwIK7HqB6ony8i)

Et cela fonctionne ! Super, maintenant éteignons notre conteneur Docker. Tapez `docker ps -a` pour voir tous les conteneurs à nouveau. Tapez `docker stop kz` et cela arrête le conteneur. Si vous tapez `docker ps`, vous ne verrez plus le conteneur, mais vous le verrez si vous tapez `docker ps -a` ( `-a` signifie tous, y compris les conteneurs en cours d'exécution et non en cours d'exécution. omettez `-a` si vous ne voulez voir que les conteneurs en cours d'exécution). Pour supprimer le conteneur, tapez `docker rm kz`. Si vous tapez `docker ps -a`, vous ne verrez plus le conteneur.

### Conclusion

C'était Docker ! Tout bien considéré, Docker est beaucoup plus facile que la configuration d'une VM basée sur un hyperviseur, et vous pouvez voir comment une architecture de microservices devient beaucoup plus facile à gérer lorsque vous adoptez des conteneurs. Avec nos fichiers `Dockerfile`, `build.sh` et `run.sh` créés dans EC2, nous pouvons résumer les 3 étapes pour exécuter Docker depuis le répertoire racine de notre application :

```bash
$ bash build.sh
$ bash run.sh
$ exit
```

C'est tout ! Docker : aussi simple que build, run, done !

### Bonus : Aide-mémoire

Puisque ce tutoriel a adopté une approche étape par étape pour enseigner Docker, je pense qu'il est approprié de vous laisser avec un aperçu de toutes les commandes Docker dont vous aurez besoin pour une utilisation générale.

```bash
$ docker images                     // Pour voir les images installées
$ docker rmi <IMAGE_NAME>           // Pour supprimer une image installée

$ docker ps -a                      // Pour voir tous les conteneurs docker
$ docker stop <CONTAINER_NAME>      // Pour arrêter un conteneur docker
$ docker rm <CONTAINER_NAME>        // Pour supprimer un conteneur docker

$ docker exec -it <CONTAINER_NAME> bash    // Exécuter dans le conteneur et lancer bash

* Si vous voulez voir la sortie du journal d'un conteneur docker, omettez le -d de run.sh
```

> Ces méthodes ont été partiellement utilisées dans le déploiement de [renthero.ca](http://renthero.ca)