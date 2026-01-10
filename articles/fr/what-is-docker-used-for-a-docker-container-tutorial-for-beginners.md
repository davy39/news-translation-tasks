---
title: À quoi sert Docker ? Un tutoriel sur les conteneurs Docker pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-12-09T17:11:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-docker-used-for-a-docker-container-tutorial-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/georg-wolf-WAgBaYHRaL4-unsplash.jpg
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: Docker Containers
  slug: docker-containers
seo_title: À quoi sert Docker ? Un tutoriel sur les conteneurs Docker pour débutants
seo_desc: "By Lucas Santos\nAs a developer, you have probably heard of Docker at some\
  \ point in your professional life. And you're likely aware that it has become important\
  \ tech for any application developer to know. \nIf you have no idea of what I'm\
  \ talking about..."
---

Par Lucas Santos

En tant que développeur, vous avez probablement déjà entendu parler de Docker à un moment donné de votre vie professionnelle. Et vous savez probablement qu'il est devenu une technologie importante pour tout développeur d'applications à connaître. 

Si vous n'avez aucune idée de ce dont je parle, ne vous inquiétez pas – c'est pour cela que cet article existe.

Nous allons partir à la découverte de ce qu'est ce Docker dont tout le monde parle et de ce que vous pouvez faire avec. À la fin, nous allons également créer, publier et exécuter notre première image Docker.

Mais d'abord, posons les bases de notre histoire. Je vais utiliser cet [article incroyable](https://blog.aquasec.com/a-brief-history-of-containers-from-1970s-chroot-to-docker-2016) de Rani Osnat qui explique toute l'histoire des conteneurs en profondeur. Et je vais la résumer ici pour que nous puissions nous concentrer sur les parties importantes.

## Un peu d'histoire des conteneurs

Docker est un runtime de conteneurs. Beaucoup de gens pensent que Docker a été le premier du genre, mais ce n'est pas vrai – les conteneurs Linux existent depuis les années 1970. 

Docker est important pour la communauté des développeurs et celle des conteneurs car il a rendu l'utilisation des conteneurs si facile que tout le monde a commencé à l'utiliser.

### Qu'est-ce que les conteneurs ?

Les conteneurs, ou conteneurs Linux, sont une technologie qui nous permet d'isoler certains processus du noyau et de leur faire croire qu'ils sont les seuls à s'exécuter sur un ordinateur complètement nouveau.

Contrairement aux machines virtuelles, un conteneur peut partager le noyau du système d'exploitation tout en ayant uniquement ses binaires/bibliothèques différentes chargées avec lui. 

En d'autres termes, vous n'avez pas besoin d'avoir un système d'exploitation différent entier (appelé **OS invité**) installé à l'intérieur de votre OS hôte. Vous pouvez avoir plusieurs conteneurs s'exécutant au sein d'un seul OS sans avoir plusieurs OS invités différents installés.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/image-166.png)
_Différence entre les machines virtuelles et les conteneurs Docker (Source : Docker)_

Cela rend les conteneurs beaucoup plus petits, plus rapides et plus efficaces. Alors qu'une VM peut prendre environ une minute pour démarrer et peut peser plusieurs gigaoctets, un conteneur pèse, en moyenne, 400 à 600 Mo (les plus grands). 

Ils ne prennent également que quelques secondes pour démarrer. Cela est principalement dû au fait qu'ils n'ont pas à démarrer un système d'exploitation entier avant d'exécuter le processus.

Et tout cela a commencé avec six caractères.

### Le début des conteneurs

L'histoire des conteneurs commence en 1979 avec Unix v7. À cette époque, je n'étais même pas né, et mon père avait 15 ans. Les conteneurs existaient-ils déjà en 1979 ? Non ! 

En 1979, la version 7 d'Unix a introduit un appel système appelé [chroot](https://en.wikipedia.org/wiki/Chroot), qui était le tout début de ce que nous connaissons aujourd'hui sous le nom de **virtualisation de processus**.

L'appel `chroot` permettait au noyau de changer le répertoire racine apparent d'un processus et de ses enfants. 

En bref, le processus pense qu'il s'exécute seul dans la machine, car son système de fichiers est séparé de tous les autres processus. Ce même appel système a été introduit dans BSD en 1982. Mais ce n'est que deux décennies plus tard que nous avons eu la première application généralisée de celui-ci.

En 2000, un fournisseur d'hébergement recherchait de meilleures façons de gérer les sites web de ses clients, puisque tous étaient installés sur la même machine et concurrençaient pour les mêmes ressources. 

Cette solution s'appelait `jails`, et c'était l'une des premières tentatives réelles d'isoler des éléments au niveau du processus. Les Jails permettaient à tout utilisateur de FreeBSD de partitionner le système en plusieurs systèmes indépendants et plus petits (qui sont appelés `jails`). Chaque jail peut avoir sa propre configuration IP et système.

Les Jails étaient la première solution pour étendre les utilisations de `chroot` afin de permettre non seulement la ségrégation au niveau du système de fichiers, mais aussi la virtualisation des utilisateurs, du réseau, des sous-systèmes et ainsi de suite.

En 2008, LXC (**L**inu**X** **C**ontainers) a été lancé. C'était, à l'époque, la première et la plus complète implémentation d'un système de gestion de conteneurs. Il utilisait des groupes de contrôle, des espaces de noms et beaucoup de ce qui avait été construit jusqu'alors. La plus grande avancée était qu'il était utilisé directement à partir d'un noyau Unix, il ne nécessitait aucun correctif.

## Docker

Enfin, en 2010, Solomon Hykes et Sebastien Pahl ont créé Docker lors du groupe d'incubation de startups Y Combinator. En 2011, la plateforme a été lancée. 

À l'origine, Hykes a commencé le projet Docker en France dans le cadre d'un projet interne de dotCloud, une société PaaS qui a été fermée en 2016.

Docker n'a pas ajouté grand-chose aux runtimes de conteneurs à l'époque – la plus grande contribution de Docker à l'écosystème des conteneurs était la **sensibilisation**. Son CLI facile à utiliser et ses concepts ont démocratisé l'utilisation des conteneurs pour les développeurs ordinaires, et pas seulement pour les entreprises de hacking profond qui avaient besoin de conteneurs pour une raison quelconque.

Après 2013, plusieurs entreprises ont commencé à adopter Docker comme runtime de conteneurs par défaut car il a standardisé l'utilisation des conteneurs dans le monde entier. En 2013, Red Hat a annoncé une collaboration avec Docker, en 2014 c'était au tour de [Microsoft](https://azure.microsoft.com/blog/microsoft-and-docker-collaborate-on-new-ways-to-deploy-containers-on-azure/?WT.mc_id=containers-11424-ludossan), AWS, Stratoscale et IBM.

En 2016, la première version de Docker pour un système d'exploitation différent de Linux a été annoncée. Windocks a publié un port du projet OSS de Docker conçu pour s'exécuter sur Windows. Et, à la fin de la même année, [Microsoft](https://azure.microsoft.com/blog/microsoft-and-docker-collaborate-on-new-ways-to-deploy-containers-on-azure/?WT.mc_id=containers-11424-ludossan) a annoncé que Docker était désormais pris en charge nativement sur [Windows](https://azure.microsoft.com/blog/microsoft-and-docker-collaborate-on-new-ways-to-deploy-containers-on-azure/?WT.mc_id=containers-11424-ludossan) via [Hyper-V](https://docs.microsoft.com/virtualization/hyper-v-on-windows/about/?WT.mc_id=containers-11424-ludossan).

> En 2019, Microsoft a annoncé le [WSL2](https://docs.microsoft.com/windows/wsl/install-win10?WT.mc_id=containers-11424-ludossan), qui a permis à Docker de s'exécuter sur Windows sans avoir besoin d'une machine virtualisée sur [Hyper-V](https://docs.microsoft.com/virtualization/hyper-v-on-windows/about/?WT.mc_id=containers-11424-ludossan). Docker est désormais nativement multiplateforme tout en tirant parti de l'approche des conteneurs Linux.

Enfin, en 2020, Docker est devenu le choix mondial pour les conteneurs. Cela ne s'est pas produit nécessairement parce qu'il est meilleur que les autres, mais parce qu'il unifie toutes les implémentations sous une seule plateforme facile à utiliser avec un CLI et un Daemon. Et il fait tout cela en utilisant des concepts simples que nous allons explorer dans les prochaines sections.

## Comment fonctionne Docker ?

Docker emballe une application et toutes ses dépendances dans un conteneur virtuel qui peut s'exécuter sur n'importe quel serveur Linux. C'est pourquoi nous les appelons des conteneurs. Parce qu'ils contiennent toutes les dépendances nécessaires dans un seul morceau de logiciel.

Docker est composé des éléments suivants :

* un Daemon, qui est utilisé pour construire, exécuter et gérer les conteneurs
* une API de haut niveau qui permet à l'utilisateur de communiquer avec le Daemon, 
* et un CLI, l'interface que nous utilisons pour rendre tout cela disponible.

### Conteneurs Docker

Les conteneurs sont des abstractions de la couche d'application. Ils emballent tout le code, les bibliothèques et les dépendances ensemble. Cela permet à plusieurs conteneurs de s'exécuter sur le même hôte, afin que vous puissiez utiliser les ressources de cet hôte plus efficacement.

Chaque conteneur s'exécute comme un processus isolé dans l'espace utilisateur et prend moins de place que les VM régulières en raison de leur architecture en couches. 

Ces couches sont appelées **images intermédiaires**, et ces images sont créées chaque fois que vous exécutez une nouvelle commande dans le `Dockerfile`, par exemple, si vous avez un Dockerfile qui ressemble à ceci :

```dockerfile
FROM node:stable

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN npm install grpc

RUN npm install

ENTRYPOINT ["npm", "start"]

```

À chaque commande comme `COPY` ou `RUN`, vous allez créer une autre couche au-dessus de votre image de conteneur. Cela permet à Docker de diviser et de séparer chaque commande en une partie distincte. Ainsi, si vous utilisez à nouveau cette image `node:stable`, il ne sera pas nécessaire de télécharger toutes ses couches, car vous avez déjà installé cette image. 

De plus, toutes les couches sont hachées, ce qui signifie que Docker peut mettre en cache ces couches et optimiser les temps de construction pour les couches qui n'ont pas changé entre les constructions. Vous n'aurez pas besoin de reconstruire et de recopier tous les fichiers si l'étape COPY n'a pas changé, ce qui réduit considérablement le temps passé dans les processus de construction.

À la fin du processus de construction, Docker crée une nouvelle couche vide au-dessus de toutes les couches appelée **couche mince inscriptible**. Cette couche est celle à laquelle vous accédez lorsque vous utilisez `docker exec -it <container> <command>`. De cette façon, vous pouvez effectuer des modifications interactives dans l'image et les valider en utilisant `docker commit`, tout comme vous le feriez avec un fichier suivi par Git.

Cette architecture de couches à différenciation par hachage est possible grâce au système de fichiers AuFS. Il s'agit d'un système de fichiers en couches qui permet d'empiler des fichiers et des répertoires en couches les uns sur les autres. 

AuFS pose certains problèmes lors de l'utilisation de DnD (Docker in Docker), mais c'est un sujet pour un autre article ! Vous pouvez consulter une explication plus détaillée dans [cet article](https://medium.com/@BeNitinAgarwal/docker-containers-filesystem-demystified-b6ed8112a04a).

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-13.png)

Les couches peuvent être différenciées par hachage entre les versions. De cette façon, Docker peut vérifier si une couche a changé lors de la construction d'une image et décider si elle doit être reconstruite, ce qui permet de gagner beaucoup de temps. 

Ainsi, si vous avez déjà téléchargé l'image Ubuntu sur votre ordinateur et que vous construisez une nouvelle image qui repose sur une ou plusieurs couches de cette image, Docker ne les reconstruira pas. Il réutilisera simplement les mêmes couches. 

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-14.png)
_(source : Packt) Explication des couches Docker_

Si vous souhaitez approfondir les couches, [cet article](https://medium.com/@jessgreb01/digging-into-docker-layers-c22f948ed612) donne beaucoup de détails sur la façon de les trouver, de les lister et de les gérer.

### Pourquoi les conteneurs Docker sont géniaux

Vous avez probablement entendu la phrase iconique "Ça marche sur ma machine". Eh bien, pourquoi ne pas donner cette machine au client ? 

C'est exactement le problème que Docker et les conteneurs résolvent en général. Un conteneur Docker est une collection emballée de toutes les bibliothèques et dépendances de l'application déjà préconstruites et prêtes à être exécutées.

Beaucoup d'entreprises ont migré des VM aux conteneurs non seulement parce qu'ils sont beaucoup plus légers et plus rapides à démarrer, mais aussi parce qu'ils sont extrêmement faciles à maintenir. 

Un seul conteneur peut être versionné en utilisant son `Dockerfile` (nous aborderons les images dans la section suivante), ce qui facilite grandement pour un développeur (ou même une petite équipe de développeurs) l'exécution et la maintenance d'un écosystème entier de conteneurs. D'un autre côté, vous auriez besoin d'une personne en infrastructure juste pour pouvoir exécuter et maintenir des VM.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-68.png)
_(source : Docker) Votre centre de données avec des VM et des conteneurs_

Cela signifie-t-il que nous n'avons plus besoin de VM ? Non, au contraire, les VM sont encore très nécessaires si vous voulez avoir un système d'exploitation complet pour chaque client ou si vous avez simplement besoin de tout l'environnement comme un bac à sable. Les VM sont généralement utilisées comme couches intermédiaires lorsque vous avez un grand rack de serveurs et plusieurs clients qui l'utiliseront.

La facilité d'utilisation et de maintenance nous amène à un autre aspect important de pourquoi les conteneurs sont si géniaux : il est beaucoup moins cher pour une entreprise d'utiliser des conteneurs que des VM entièrement fonctionnelles. 

Ce n'est pas parce que l'infrastructure ou le matériel est moins cher, mais parce que vous avez besoin de moins de personnes pour maintenir les conteneurs, ce qui signifie que vous pouvez mieux organiser votre équipe pour vous concentrer sur le produit au lieu de vous concentrer sur la maintenance.

Toujours en relation avec les économies, une seule VM de taille moyenne peut exécuter environ 3 à 8 conteneurs. Cela dépend du nombre de ressources que vos conteneurs utilisent et de la quantité du système d'exploitation sous-jacent dont ils ont besoin pour démarrer avant d'exécuter l'application entière. 

Certains langages, comme Go, vous permettent de construire une image avec uniquement le binaire compilé et rien d'autre. Cela signifie que le conteneur Docker aura beaucoup moins à charger et utilisera donc moins de ressources. De cette façon, vous pouvez démarrer plus de conteneurs par VM et utiliser votre matériel plus efficacement.

Puisque les conteneurs sont conçus pour être éphémères, cela signifie que toutes les données à l'intérieur sont perdues lorsque le conteneur est supprimé. C'est génial, car nous pouvons utiliser des conteneurs pour des tâches ponctuelles comme le CI. 

L'utilisation de conteneurs a apporté un tout nouveau niveau d'avancées DevOps. Maintenant, vous pouvez simplement démarrer de nombreux conteneurs, chacun effectuant une petite étape de votre pipeline de déploiement, puis les supprimer sans vous soucier d'avoir laissé quelque chose derrière vous. 

La nature sans état des conteneurs en fait l'outil parfait pour des charges de travail rapides.

Maintenant que nous avons vu à quel point les conteneurs sont géniaux, comprenons comment nous pouvons en construire un !

## Qu'est-ce que les images Docker ?

Les images Docker sont des instructions écrites dans un fichier spécial appelé `Dockerfile`. Il a sa propre syntaxe et définit les étapes que Docker suivra pour construire votre conteneur.

Puisque les conteneurs ne sont que des couches de changements, chaque nouvelle commande que vous créez dans une image Docker créera une nouvelle couche dans le conteneur. 

La dernière couche est ce que nous appelons une **couche mince inscriptible**. Une couche vide qui peut être modifiée par l'utilisateur et validée en utilisant la commande `docker commit`.

Voici un exemple d'une image simple pour une application Node.js :

```dockerfile
FROM node:stable
COPY . /usr/src/app/
RUN npm install && npm run build
EXPOSE 3000
ENTRYPOINT ["npm", "start"]
```

Dans cet exemple simple, nous créons une nouvelle image. Toutes les images sont basées sur une image existante, ou une image scratch (que j'explique dans mes articles de blog en portugais, [ici](https://blog.lsantos.dev/um-mergulho-em-imagens-de-containers-parte-1/), [ici](https://blog.lsantos.dev/um-mergulho-em-imagens-de-containers-parte-2/), et [ici](https://blog.lsantos.dev/um-mergulho-em-imagens-de-containers-parte-3/)). 

Ces images sont téléchargées depuis un **registre de conteneurs**, un dépôt pour stocker des images de conteneurs. Le plus courant est le [Docker Hub](https://hub.docker.com/), mais vous pouvez également créer un registre privé en utilisant des solutions cloud comme [Azure Container Registry](https://azure.microsoft.com/services/container-registry/?WT.mc_id=containers-11424-ludossan).

Lorsque vous exécutez `docker build .` dans le même répertoire que le Dockerfile, le démon Docker commencera à construire l'image et à l'emballer pour que vous puissiez l'utiliser. Ensuite, vous pouvez exécuter `docker run <image-name>` pour démarrer un nouveau conteneur.

Remarquez que nous exposons certains ports dans le Dockerfile. Docker nous permet de séparer les réseaux au sein de notre propre OS, ce qui signifie que vous pouvez mapper des ports de votre ordinateur vers le conteneur et vice-versa. De plus, vous pouvez exécuter des commandes à l'intérieur des conteneurs avec `docker exec`. 

Mettons cette connaissance en pratique.

## Comment déployer votre application Dockerisée

Ce sera un guide simple et facile sur la façon de créer une image Docker de base en utilisant un serveur Node.js et de la faire fonctionner sur votre ordinateur.

Tout d'abord, commencez un nouveau projet dans un répertoire de votre choix, et exécutez `npm init -y` pour créer un nouveau fichier `package.json`. Maintenant, créons un autre répertoire appelé `src`. Dans ce répertoire, nous créerons un nouveau fichier appelé `server.js`.

Maintenant, dans votre fichier `package.json`, changez la clé `main` en `src/server.js`. Supprimez également le script `test` qui a été créé et remplacez-le par `"start": "node src/server.js"`. Votre fichier devrait ressembler à ceci :

```json
{
  "name": "your-project",
  "version": "1.0.0",
  "description": "",
  "main": "src/server.js",
  "scripts": {
    "start": "node src/server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}

```

Maintenant, créez un fichier appelé `Dockerfile` (sans extension). Écrivons notre image !

```dockerfile
FROM node:lts-alpine
COPY . /usr/src/app/
WORKDIR /usr/src/app
EXPOSE 8089
ENTRYPOINT ["npm", "start"]
```

Expliquons cela :

1. Tout d'abord, nous obtenons l'image node depuis Docker Hub. Puisque les images sont enregistrées par leurs noms, nous différencions les images par leurs tags. Vous pouvez vérifier tous les tags [ici](https://hub.docker.com/_/node).
2. Ensuite, nous utilisons `COPY` pour copier tous les fichiers dans le répertoire courant (en utilisant `.`) vers un nouveau répertoire dans le conteneur appelé `/usr/src/app`. Le répertoire est créé automatiquement. Cela est nécessaire car nous avons besoin de tous nos fichiers d'application là-bas.
3. Maintenant, nous changeons notre répertoire de démarrage en `/usr/src/app`, afin que nous puissions exécuter des choses depuis le répertoire racine de notre application.
4. Nous exposons notre port,
5. Et nous disons que, dès que notre conteneur s'exécute, nous allons exécuter "npm start".

Construisons l'image en exécutant `docker build . -t simple-node-image`. De cette façon, nous allons taguer notre image et lui donner un nom.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-15.png)

Vous verrez qu'il va créer et télécharger l'image, ainsi que toutes les couches nécessaires. Exécutons cette image avec la commande suivante :

```bash
docker run -p 80:8089 simple-node-image 
```

Nous mappons notre port `80` au port `8089` à l'intérieur du conteneur. Nous pouvons vérifier cela en tapant `docker ps` comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-17.png)

Maintenant, essayez d'accéder à `localhost:80`, et voyez ce qui se passe :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/image-18.png)

## À quoi sert Docker ?

Maintenant que nous avons vu comment construire un conteneur Docker, passons à quelques utilisations pratiques de Docker et comment vous pouvez en tirer le meilleur parti.

### Bases de données éphémères

Avez-vous déjà essayé de développer une application qui nécessite une base de données pour fonctionner ? Ou pire, essayé d'exécuter l'application de quelqu'un d'autre qui a besoin d'une base de données que vous n'avez pas installée ? 

L'ancienne solution était d'installer d'abord la base de données, puis d'exécuter l'application. Avec Docker, vous avez juste besoin d'exécuter le conteneur de la base de données. Exécutons un simple conteneur MongoDB :

```bash
$ docker run -p 27017:27017 --name my-ephemeral-db mongo

```

C'est tout ! Maintenant vous pouvez accéder à votre base de données depuis votre ordinateur via le port 27017, comme vous le feriez normalement.

### Bases de données persistantes

Le problème avec l'exemple précédent est que, si vous supprimez le conteneur, toutes vos données seront perdues. Alors, que se passe-t-il si vous voulez exécuter une base de données locale sans avoir besoin de l'installer, mais garder les données après sa suppression ? Vous pouvez lier Docker à un volume !

Lorsque vous liez Docker à un volume local, vous montez essentiellement votre système de fichiers dans le conteneur ou vice-versa. Voyons cela :

```bash
$ docker run -p 27017:27017 -v /home/my/path/to/db:/data/db --name my-persistent-db mongo

```

Dans cette commande, nous montons `/data/db` dans `/home/my/path/to/db`. Maintenant, si nous utilisons `docker stop my-persistent-db` et `docker rm my-persistent-db`, toutes nos données continueront à être stockées là.

Plus tard, si nous avons besoin de la base de données à nouveau, nous pouvons la monter en utilisant la même commande, et toutes les données seront de retour.

### Outils à usage unique

Une autre chose que tous les développeurs font : nous installons des applications que nous n'utilisons qu'une seule fois. Par exemple, ce simple CLI pour accéder à cette ancienne base de données, ou ce simple GUI pour un serveur CI. 

De nombreux outils ont déjà des conteneurs Docker, et vous pouvez les utiliser comme ceci, afin de ne pas avoir à installer un autre outil dans votre ordinateur.

Le meilleur exemple est Redis. Il a le `redis-cli` intégré dans un autre conteneur, donc vous n'avez pas besoin d'installer le `redis-cli` dans votre shell si vous l'utilisez rarement. 

Imaginons que vous lanciez une instance Redis avec `docker run -d --name redis redis --bind 127.0.0.1` liée à l'interface localhost. Vous pouvez y accéder via un autre conteneur en utilisant :

```bash
$ docker run --rm -it --network container:redis redis-cli -h 127.0.0.1

```

Le drapeau `--rm` indique à Docker qu'il doit supprimer le conteneur dès qu'il est arrêté, tandis que les drapeaux `-it` lui indiquent que nous voulons une session interactive (avec un shell) et que nous aurons besoin d'un TTY.

### Exécuter des piles entières

Si vous devez tester une application qui dépend d'une autre application, comment feriez-vous ? Docker facilite cela en fournissant `docker-compose`. C'est un autre outil dans votre boîte à outils qui vous permet de coder un fichier `docker-compose.yml` décrivant votre environnement. 

Le fichier ressemble à ceci :

```yml
version: "3.8"
services:
  web:
    build: .
    ports:
      - "5000:5000"

  redis:
    image: "redis:alpine"
    ports:
      - "6379:6379"

```

Comme vous pouvez le voir, nous définissons deux services, l'un s'appelle `web` et exécute `docker build` sur le chemin `web.build`. C'est un `Dockerfile`. 

Après cela, il expose le port `5000` à la fois sur l'hôte et dans le conteneur. L'autre service est `redis`, qui télécharge et exécute l'image `redis` sur le port `6379`. 

Le meilleur, c'est que la couche réseau est partagée, en d'autres termes, vous pouvez accéder à `redis` depuis le service `web` en tapant simplement `redis` et le port.

Vous pouvez démarrer ce fichier avec un simple `docker-compose up`, et voir la magie opérer. 

## Conclusion

C'est tout ! Voici l'histoire de Docker, comment il est apparu et comment il fonctionne en 3000 mots. J'espère que vous l'avez apprécié, et j'espère que cela a rendu votre avancée avec Docker un peu plus facile.

Comme vous avez pu le constater, la plupart des utilisations de Docker sont destinées à faciliter la vie des développeurs lors du développement d'applications. Mais il existe de nombreuses autres utilisations, telles que les couches d'infrastructure et la maintenance de vos applications.

Si vous souhaitez me contacter, envoyez-moi un message sur l'un de mes réseaux sociaux sur [mon site web](https://lsantos.dev).

_Photo de couverture par [Georg Wolf](https://unsplash.com/@georgewolf?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/s/photos/whale?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)_