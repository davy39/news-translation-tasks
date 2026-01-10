---
title: Une introduction complète à Docker, aux machines virtuelles et aux conteneurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-05T03:18:04.000Z'
originalURL: https://freecodecamp.org/news/comprehensive-introductory-guide-to-docker-vms-and-containers-4e42a13ee103
coverImage: https://cdn-media-1.freecodecamp.org/images/1*r_TVGEzJr8PWwEkt38YuDQ.png
tags:
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Une introduction complète à Docker, aux machines virtuelles et aux conteneurs
seo_desc: 'By shota jolbordi

  Docker has been a buzzword for tech people for the last several years, and the more
  times goes by, the more often you hear about it. We’re seeing it more in job requirements,
  and more companies are starting to incorporate it. Nowada...'
---

Par shota jolbordi

Docker est un terme à la mode depuis plusieurs années pour les professionnels de la technologie, et plus le temps passe, plus on en entend parler. Nous le voyons de plus en plus dans les exigences des offres d'emploi, et de plus en plus d'entreprises commencent à l'incorporer. De nos jours, cela semble être quelque chose de si basique et courant dans le monde du développement que si vous ne le connaissez pas, vous êtes en retard par rapport à tout le monde.

_Non, mais sérieusement, qu'est-ce que ce "Docker" ? Pourquoi tout le monde en est-il si enthousiaste ? Qu'est-ce que c'est même ? Pouvez-vous le définir ? Est-ce une application de bureau ? Un outil CLI ? Un site web ? Un service ? Est-ce pour la production ou est-ce un outil de développement ? Les deux ? J'ai entendu dire qu'il a des choses comme des "images" et des "conteneurs" et c'est comme une machine virtuelle mais pas vraiment une machine virtuelle. Pourquoi en ai-je même besoin, et qu'est-ce que tout cela a à voir avec cette baleine bleue après tout ?_

Dans cet article, je vais essayer d'expliquer :

* ce qu'est exactement "docker"
* pourquoi vous pourriez en avoir besoin
* quels problèmes il essaie de résoudre
* en quoi il est différent d'une machine virtuelle
* quand l'utiliser plutôt qu'une machine virtuelle et vice versa
* ce que sont les images et les conteneurs en général
* et comment ils sont implémentés dans docker.

Je vais aborder tous les concepts dans un ordre spécifique afin que chaque autre sujet que j'explique nécessitera une compréhension des concepts précédents. Cependant, lors de la lecture de cet article, si vous ne comprenez pas quelque chose, ou si quelque chose semble vague, continuez simplement à lire, tout deviendra clair à la fin. Mon conseil concernant cet article serait de le lire 2 fois pour avoir vos "moments aha".

D'accord, assez parlé, commençons !

![Image](https://cdn-media-1.freecodecamp.org/images/1*qeasRs1GFBlXKdWjpU2INw.png)

### Qu'est-ce que Docker ?

Il existe de nombreux noms "docker" que vous pourriez entendre sur Internet, et pour un débutant, cela peut être écrasant. Prenons un moment pour définir certains de ces noms afin de savoir au moins lequel est lequel.

* Docker, Inc
* docker engine (communauté / entreprise)
* docker pour Mac
* docker pour Windows
* docker client
* docker host
* docker server
* docker hub
* docker registry
* docker compose
* docker swarm
* docker machine
* docker daemon

Assez de dockers ici, hein ? Je vais vous donner une courte définition pour chacun des termes ici afin que vous sachiez ce qu'ils sont.

#### Docker (entreprise)

**Docker, Inc** a été cofondée en 2010 par Solomon Hykes (CTO) à San Francisco, et à cette époque, elle s'appelait **dotCloud, Inc**. Ils exploitaient une entreprise de type PaaS (plateforme en tant que service), similaire à [Heroku](https://www.heroku.com/). Pour implémenter cela, ils utilisaient des conteneurs Linux.

En mars 2013, lors de PyCon, Solomon a révélé un nouveau produit de **dotCloud, Inc** appelé "docker". La motivation, comme il le décrit dans son [discours](https://www.youtube.com/watch?v=wW9CAH9nSLs) (le premier discours où docker a été mentionné), était que les gens étaient très intéressés par les conteneurs Linux et comment ils pouvaient construire quelque chose avec eux, mais le problème était que les conteneurs Linux étaient très compliqués. Chez **dotCloud, Inc**, ils ont décidé de simplifier l'utilisation des conteneurs Linux et de les rendre accessibles à tous, donc le logiciel "docker" est né.

Plus tard en 2013, **dotCloud, Inc** a annoncé qu'ils changeaient leur nom en **Docker, inc** et que leur produit principal à partir de maintenant serait "docker" (logiciel). Ils ont séparé leur activité PaaS vers une autre entreprise et le reste est de l'histoire.

Pour nous, nous nous intéressons principalement au logiciel docker, pas à l'entreprise elle-même, mais je pense qu'il est bon de connaître un peu l'histoire derrière.

#### Docker (logiciel)

Docker est disponible en 2 éditions : Docker Community Edition (CE) et Docker Enterprise Edition (EE). Pour un environnement de développement et des petites équipes, CE est la solution à adopter, donc dans cet article, nous ne couvrirons pas EE. CE est gratuit et EE est la manière dont **Docker, Inc** gagne réellement de l'argent.

Le logiciel Docker se compose de 2 programmes distincts, à savoir le moteur docker, également connu sous le nom de démon docker (parce que c'est, en fait, un démon, qui s'exécute en arrière-plan) et le client docker.

#### Moteur / Démon

Le moteur Docker est ce qui permet réellement aux conteneurs Linux de fonctionner — c'est le "cerveau de docker", pour ainsi dire.

Le moteur Docker est responsable de l'exécution des processus dans des environnements isolés. Pour chaque processus, il génère un nouveau conteneur Linux, alloue un nouveau système de fichiers pour celui-ci, alloue une interface réseau, définit une IP pour celui-ci, définit le NAT pour celui-ci, puis exécute les processus à l'intérieur.

Il gère également des choses telles que la création, la suppression d'images, la récupération d'images depuis le registre de votre choix, la création, le redémarrage, la suppression de conteneurs et bien d'autres choses. Le moteur Docker expose l'API REST qui peut être utilisée pour contrôler le démon.

#### Client

Le client Docker fournit le CLI pour contrôler le démon docker. Ce n'est qu'un wrapper pour l'API HTTP. En gros, le client docker envoie des requêtes API au moteur docker qui, en lui-même, effectue toute la magie. Le client et le démon docker n'ont pas besoin d'être sur la même machine. Vous pouvez accéder au CLI avec la commande `docker` depuis le terminal.

#### Hôte

L'hôte Docker est un ordinateur sur lequel le démon docker est en cours d'exécution. Parfois, on l'appelle aussi serveur docker.

#### Hub

[Docker hub](https://hub.docker.com) est un registre d'images docker fourni par **Docker, Inc** lui-même. Il permet aux utilisateurs de pousser des images vers leur dépôt, de les rendre publiques ou privées, et de tirer différentes images, le tout en utilisant le CLI du client docker.

Il existe des images pour presque tout ce qui est fait par d'autres personnes ou entreprises, chaque langage, chaque base de données, chaque version de celle-ci. C'est comme GitHub pour les images docker. Il existe des registres d'images Docker disponibles par d'autres entreprises, tels que [Quay](https://quay.io/), [Google container registry](https://cloud.google.com/container-registry), et [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/). Alternativement, vous pouvez héberger votre propre registre docker.

#### Registre

Le registre Docker est une application côté serveur qui vous permet d'héberger votre propre dépôt docker. Il est fourni sous la forme d'une image hébergée sur docker hub. Pour le faire fonctionner, vous devez tirer une image appelée "registry" depuis docker hub et lancer le conteneur à partir de celle-ci. Un hôte Docker exécutant un conteneur "registry" est maintenant un serveur de registre.

#### Pour Mac

Docker pour Mac est un logiciel distinct de docker, fourni par **Docker, Inc**, qui simplifie le développement avec docker sur Mac OS. Le package inclut le client docker, la machine virtuelle complète fonctionnant sur l'hyperviseur natif HyperKit de Mac OS, le démon docker installé dans cette machine, docker-compose et les outils d'orchestration docker-machine. Les ports exposés des conteneurs sont automatiquement transférés de la VM vers localhost.

#### Pour Windows

Docker pour Windows est configuré spécifiquement pour Windows. Il utilise Hyper-v (la solution de virtualisation native de Windows 10) pour son logiciel de virtualisation et vous donne également la possibilité d'exécuter des conteneurs Windows aux côtés des conteneurs Linux.

#### Machine

Docker machine est un outil d'orchestration qui vous permet de gérer plusieurs hôtes docker. Il vous permet de provisionner plusieurs hôtes docker virtuels localement, ou sur le cloud, et de les gérer avec les commandes `docker-machine`. Vous pouvez démarrer, redémarrer et inspecter les hôtes gérés. Vous pouvez pointer le client docker vers l'un des hôtes et ensuite gérer le démon sur cet hôte directement. Il existe de nombreuses façons de gérer les hôtes docker avec cet outil, consultez simplement la [référence](https://docs.docker.com/machine/reference/) CLI.

#### Compose

Docker compose est également un outil d'orchestration pour docker. Il vous permet de gérer facilement plusieurs conteneurs dépendants les uns des autres au sein d'un seul hôte docker via le CLI `docker-compose`. Vous utilisez un fichier YAML pour configurer tous les conteneurs. Avec une seule commande, vous pouvez démarrer tous les conteneurs dans le bon ordre et configurer la mise en réseau entre eux. Voici la [référence](https://docs.docker.com/compose/reference/overview/).

#### Swarm

Docker swarm est un autre outil d'orchestration visant à gérer un cluster d'hôtes docker. Alors que docker-compose gère plusieurs conteneurs Docker au sein d'un seul hôte docker, docker swarm gère plusieurs hôtes docker gérant plusieurs conteneurs Docker.

Contrairement à docker-compose et docker-machine, docker swarm n'est pas un logiciel d'orchestration autonome. Le mode Swarm est intégré au moteur docker et est géré via le client Docker.

Pour créer un swarm, vous devez vous connecter en SSH à une machine que vous souhaitez transformer en swarm et exécuter `docker swarm init --advertise-addr <ip à publier>`. Cette commande rendra une machine accessible sur <ip à publier>. D'autres hôtes docker peuvent maintenant rejoindre le swarm sur cette IP.

#### Résumé

D'accord, alors qu'avons-nous appris jusqu'à présent ?

Docker n'est pas un logiciel autonome, c'est une plateforme pour gérer les conteneurs Linux. Chaque fois que quelqu'un mentionne docker dans le contexte du logiciel, il parle de docker CE ou docker EE.

Docker est développé par **Docker, Inc** pour simplifier l'utilisation des conteneurs Linux. La plateforme se compose de plusieurs outils pour exécuter et gérer les conteneurs Linux, qui incluent :

* Le démon/moteur Docker qui est responsable de la génération et de l'exécution des conteneurs Linux.
* Le client Docker qui est une application distincte qui contrôle le démon docker via l'API REST.
* Docker-compose, docker-machine et docker swarm sont des outils d'orchestration, ils ne sont pas nécessaires pour exécuter des processus à l'intérieur des conteneurs Linux, mais ils rendent la gestion des conteneurs très simple. Pour être franc, dans les scénarios de la vie réelle, ils sont presque une nécessité, car gérer tous ces conteneurs, hôtes et clusters d'hôtes manuellement est... eh bien, disons que c'est une mauvaise stratégie commerciale.
* Docker hub est un service qui fournit un registre d'images docker. Nous pouvons stocker nos images sur le docker hub et tirer des images faites par d'autres pour que nous puissions les utiliser.
* Docker registry nous permet d'héberger notre propre registre privé au cas où nous ne voudrions pas utiliser un registre existant.
* Docker pour Mac et Docker pour Windows sont des outils distincts qui simplifient le développement avec docker sur Mac ou Windows.

Si vous êtes un débutant, c'est normal si vous ne comprenez pas tout ce qui est mentionné ci-dessus à 100 %. Certaines choses peuvent être vagues, vous pouvez avoir des questions, et c'est normal. J'ai mentionné des images et des conteneurs à plusieurs reprises mais je n'ai pas expliqué ce qu'ils sont.

Cette section est destinée à vous aider à naviguer entre tous ces noms, à éliminer l'incertitude et à comprendre ce qui est quoi afin que vous ne soyez pas submergé en entendant tous ces différents titres de type "docker <insérer du texte>".

Avec cela dit, je pense que sur la base de ce que nous avons appris jusqu'à présent, vous devriez être en mesure de comprendre plus ou moins l'image suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*bIQOZL_pZujjrfaaYlQ_gQ.png)

Comme vous pouvez le voir, le client docker et le démon docker sont sur des machines différentes ici, donc cela peut répondre à certaines de vos questions comme...

_Pourquoi ont-ils divisé docker en client et moteur ? Pourquoi n'ont-ils pas fait en sorte que le CLI contrôle le moteur directement au lieu de l'API REST ?_

Eh bien, parce que cela permet d'avoir le client et le moteur sur des machines différentes, donc plusieurs hôtes différents peuvent être gérés à partir d'un seul ordinateur.

Avec toutes ces choses clarifiées, nous pouvons approfondir.

### Machines Virtuelles

_Hé, hé, attendez une minute — parlons-nous de docker ici ou quoi ?_

Oui, nous le faisons, cependant, à un moment donné dans l'apprentissage de docker, une question naturelle émergera :

_Quelle est la différence entre les VM et les conteneurs, et pourquoi utiliser l'un plutôt que l'autre ?_

Tout le monde qui apprend docker passe par cela, et je pense que nous pourrions aussi bien le faire maintenant et en finir.

Il y a beaucoup de choses sur la façon dont les machines virtuelles fonctionnent sous le capot. Nous ne pouvons pas passer en revue tous les détails dans cet article, mais je vais expliquer juste assez pour que vous compreniez la différence entre les VM et les conteneurs.

Chaque ordinateur, qu'il s'agisse du serveur web gigantesque fonctionnant sous Linux ou de votre iPhone X surévalué, possède 4 composants **physiques** essentiels :

* Processeur (CPU),
* Mémoire (RAM),
* Stockage (HDD / SSD),
* La carte réseau (NIC).

La tâche principale de tout système d'exploitation est de gérer ces 4 ressources. La partie du système d'exploitation qui fait cela est appelée le Noyau, également appelé le Cœur.

Le noyau, simplement dit, est une partie du système d'exploitation qui contrôle le matériel. Le noyau contrôle les pilotes pour différents périphériques d'E/S tels qu'une souris, un clavier, des écouteurs, un microphone... etc. Le noyau est le premier programme chargé lorsque l'ordinateur est allumé, juste après le chargeur de démarrage, puis il gère le reste du processus de démarrage. La grande majorité du temps qu'il faut pour allumer l'ordinateur est due au Noyau.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wITUVuuUzfYvqOeZu2ksbw.jpeg)

Chaque système d'exploitation a sa propre implémentation du noyau, mais en fait, ils font tous la même chose : ils contrôlent le matériel.

Alors, comment est-il possible de faire fonctionner un système d'exploitation à l'intérieur d'un autre ? Essentiellement, ce dont nous avons besoin est un programme qui permet au système d'exploitation invité (le système d'exploitation qui fonctionne à l'intérieur d'un autre système d'exploitation) de contrôler le matériel du système d'exploitation hôte (un système d'exploitation qui a un système d'exploitation invité fonctionnant à l'intérieur).

#### Hyperviseur

L'hyperviseur, également appelé Virtual Machine Manager (VMM), est ce qui permet la virtualisation (l'exécution de plusieurs systèmes d'exploitation sur un seul ordinateur physique). Il permet à l'ordinateur hôte de partager ses ressources entre les VM.

Il existe 2 types d'hyperviseurs :

**Type 1, également appelé "Bare Metal Hypervisor"**

Ce logiciel est installé directement sur le matériel de la machine sous-jacente (donc, dans ce cas, il n'y a pas de système d'exploitation hôte, il n'y a que des systèmes d'exploitation invités). Vous feriez cela sur une machine dont le but était d'exécuter de nombreuses machines virtuelles.

Les hyperviseurs de type 1 ont leurs propres pilotes de périphériques et interagissent directement avec le matériel contrairement aux hyperviseurs de type 2. C'est ce qui les rend plus rapides, plus simples et donc plus stables.

**Type 2, également appelé "Hosted Hypervisor"**

Il s'agit d'un programme installé sur le système d'exploitation. Vous en êtes probablement plus familier, comme VirtualBox ou VMware Workstation. Ce type d'hyperviseur est une sorte de "traduction" qui traduit les appels système du système d'exploitation invité en appels système du système d'exploitation hôte.

Les appels système (syscalls) sont un moyen par lequel un programme demande un service au noyau, et le noyau fait — rappelez-vous quoi ? Il gère le matériel sous-jacent.

Par exemple, dans votre programme, disons que vous voulez copier le contenu d'un fichier dans un autre. Assez simple, n'est-ce pas ? Pour cela, vous devez prendre quelques octets d'une partie de votre disque dur et les mettre dans une autre partie. Donc, en gros, vous faites des choses avec une ressource physique, le disque dur dans cet exemple, et vous devrez initier un appel système pour le faire. Bien sûr, dans tous les langages de programmation, cela est abstrait pour vous, mais vous comprenez le point.

Puisque tous les noyaux des systèmes d'exploitation, malgré être implémentés de différentes manières, font le même travail (contrôler le matériel), nous avons juste besoin d'un programme qui "traduira" les appels système d'un système d'exploitation invité pour contrôler le matériel.

Un avantage de l'hyperviseur de type 2 est que dans ce cas, nous n'avons pas à nous soucier du matériel sous-jacent et de ses pilotes. Nous devons simplement déléguer le travail au système d'exploitation hôte, qui gérera cela pour nous. L'inconvénient est qu'il crée une surcharge de ressources, et plusieurs couches superposées rendent les choses compliquées et réduisent les performances.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QTKTyBFtMPg0ZdT-nk7kjw.png)

### Conteneurs

Les machines virtuelles ne sont pas la seule technique de virtualisation. Dans le cas d'une machine virtuelle, nous avons un ordinateur virtuel complet, dans son intégralité, avec son propre noyau dédié. Nous allouons de la RAM pour celui-ci, nous allouons de la mémoire pour celui-ci, et nous interagissons avec lui comme s'il s'agissait d'un ordinateur autonome.

Il y a plusieurs problèmes avec cela. Le premier et le plus évident est la gestion inefficace des ressources. Une fois que vous allouez certaines ressources à une VM, elle va les conserver tant qu'elle est en cours d'exécution.

Par exemple : si vous allouez 4 Go de RAM et 40 Go de mémoire disque pour une VM, une fois que vous la lancez, ces ressources seront indisponibles tant que cette VM est en cours d'exécution. Elle pourrait n'avoir besoin que de 1 Go de RAM à un moment donné, et vous pourriez manquer de RAM pour un autre processus dans une autre VM ou machine hôte. Mais puisque elle a cette quantité de RAM allouée, elle va simplement rester là inutilisée.

Un autre problème est le temps de démarrage. Puisque la VM a son propre noyau, si vous devez redémarrer votre machine, elle devra démarrer un noyau entier. Pendant que la machine redémarre, votre service qui était en cours d'exécution dans la VM sera indisponible.

#### Les conteneurs à la rescousse

Pour faire simple, un conteneur est une machine virtuelle sans noyau. Au lieu de cela, il utilise le noyau du système d'exploitation hôte. Pour rendre cela possible, nous avons besoin d'un ensemble de logiciels et de bibliothèques qui permettront aux conteneurs d'utiliser le noyau du système d'exploitation sous-jacent, et de les "lier" en quelque sorte si vous le souhaitez. De telles bibliothèques sont, par exemple, "liblxc" et "libcontainer" (cette dernière est développée par **Docker, Inc** et est utilisée à l'intérieur du moteur docker).

Les conteneurs ont leur propre système de fichiers alloué et leur propre IP. Les bibliothèques, les binaires, les services sont installés à l'intérieur d'un conteneur, cependant, tous les appels système et les fonctionnalités du noyau proviennent du système d'exploitation hôte sous-jacent.

Les conteneurs sont très légers. Le démarrage et le redémarrage se font très rapidement car ils n'ont pas besoin de démarrer le noyau à chaque fois. Ils ne gaspillent pas les ressources physiques puisqu'ils n'ont pas besoin qu'elles soient allouées pour leur noyau, car ils n'ont pas de noyau séparé.

Un inconvénient est qu'il n'est possible d'exécuter que des conteneurs du même type que le système d'exploitation sous-jacent. Vous ne pouvez pas exécuter de conteneurs Linux sur Windows ou Mac, car ils ont besoin du noyau Linux pour fonctionner. La solution pour les utilisateurs de Mac et Windows serait d'installer un hyperviseur de type 2 tel que VirtualBox ou WMware Workstation, de démarrer la machine Linux, puis d'exécuter des conteneurs Linux à l'intérieur (en fait, c'est ce que Docker pour Mac et Docker pour Windows font, mais ils utilisent des hyperviseurs natifs qui accompagnent le système d'exploitation respectif).

La configuration et l'exécution de conteneurs Linux ne sont pas si simples. C'est fastidieux et nécessite une connaissance décente de Linux. Les gérer est encore plus fastidieux.

Comme je l'ai mentionné ci-dessus, ce que fait **Docker, Inc**, c'est qu'il rend les conteneurs Linux faciles à utiliser et accessibles à tous, et vous n'avez pas besoin d'être un geek de Linux pour utiliser les conteneurs Linux de nos jours grâce à docker.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GnByVbz5fbHfboeXyTbYAQ.jpeg)

### Conteneurs VS Machines Virtuelles

De la section précédente sur les conteneurs, vous pourriez penser que les conteneurs sont simplement de meilleures solutions de virtualisation que les VM, mais ce n'est pas le cas.

Le but d'un conteneur est d'exécuter des processus dans un environnement isolé, pour docker chaque conteneur pour chaque processus unique. Les VM sont pour émuler une machine entière. De nos jours, seuls les conteneurs Linux et Windows existent, mais il existe toutes sortes d'hyperviseurs pour émuler n'importe quel type de système d'exploitation. Vous pouvez exécuter Windows 10 à l'intérieur d'un iPad si vous le souhaitez. Ces deux technologies sont différentes et elles ne se font pas concurrence.

Les VM sont plus sécurisées, puisque les conteneurs effectuent des appels système directement au noyau. Cela ouvre toute une variété de vulnérabilités.

Certains logiciels de bas niveau qui interfèrent directement avec un noyau doivent être mis en bac à sable à l'intérieur d'une machine virtuelle.

Souvent, vous pouvez voir des conteneurs docker fonctionnant à l'intérieur de machines virtuelles dans l'environnement de production, donc les VM et les conteneurs s'associent en fait très bien.

### Images et conteneurs Docker

Docker introduit plusieurs concepts qui simplifient... ou je dirais plutôt révolutionnent l'utilisation des conteneurs Linux.

Les conteneurs Linux dans Docker sont créés à partir de modèles appelés "images". Une image est essentiellement un fichier binaire qui contient l'état d'une machine Linux (sans le noyau, bien sûr). Vous pouvez établir un parallèle avec les images de disque des VM telles que les fichiers `.vdi`, `.vmdk` ou `.vhd`.

L'approche de Docker pour les images est différente de celle d'une VM. Dans une VM, vous monteriez simplement une image de disque, exécuteriez la VM, et vous auriez une instance en cours d'exécution de la machine. Chaque fois que vous modifiez le système de fichiers dans la VM, installez ou supprimez quelque chose, tout cela est reflété sur l'image que vous avez montée. L'image est essentiellement le disque dur de la machine.

Dans Docker, les images sont en lecture seule — vous n'exécutez pas les images directement, au lieu de cela, vous faites une copie de l'image et vous l'exécutez. Cette instance en cours d'exécution de l'image est appelée un conteneur. En faisant cela, vous pouvez avoir plusieurs instances du même conteneur Linux en cours d'exécution en même temps, créées à partir du même modèle, qui sont des images. Tout ce qui arrive à un conteneur n'affecte pas l'image à partir de laquelle il a été créé. Vous pouvez créer autant d'instances d'un conteneur à partir d'une image que votre matériel vous permet d'exécuter.

#### Fusionner des images via Union Mount

Pour créer et stocker des images, Docker utilise Union Filesystem. C'est un service dans Linux, FreeBSD et NetBSD. Les Union Filesystems nous permettent de créer un système de fichiers à partir de plusieurs systèmes de fichiers différents en les fusionnant tous ensemble. Le contenu des répertoires qui ont le même chemin sera vu ensemble dans un seul répertoire fusionné. Le processus de fusion est appelé "union mounting".

![Image](https://cdn-media-1.freecodecamp.org/images/1*Jj_uyd_r7udev8MOabO9ow.png)

Voici à peu près comment cela fonctionne :

Il y a 3 couches qui entrent en jeu : la couche de base, la couche de superposition et la couche de différence. Lors de la fusion de 2 systèmes de fichiers, le processus ressemble à quelque chose comme ceci (gardant à l'esprit que je simplifie ici) :

Nous avons donc un système de fichiers de base, et nous voulons introduire quelques modifications, ajouter des fichiers/dossiers, supprimer des fichiers/dossiers.

Tout d'abord, nous allons créer un système de fichiers de superposition (vide à ce stade) et un système de fichiers de différence (également vide à ce stade). Ensuite, nous allons monter ces systèmes de fichiers en utilisant le service de système de fichiers union intégré à Linux. En regardant dans le système de fichiers de superposition, il nous donnera la vue du système de fichiers de base. Nous pouvons ajouter des éléments, supprimer des éléments, car le système de fichiers de base réel ne sera pas affecté. Au lieu de cela, toutes les modifications apportées au système de fichiers de superposition seront stockées dans le système de fichiers de différence. Le système de fichiers de différence montre la différence entre les systèmes de fichiers de base et de superposition.

Après avoir terminé la modification du système de fichiers de superposition, nous allons le démonter. À la fin, nous avons le système de fichiers fusionné des couches de superposition et de base, et le système de fichiers de base réel n'est pas affecté.

C'est exactement comment les images Docker sont "empilées" les unes sur les autres. Docker utilise cette technologie exacte pour fusionner les systèmes de fichiers des images.

Pour créer votre image sur une image déjà existante, vous devez `touch Dockerfile`. Il s'agit d'un fichier texte avec un ensemble d'instructions sur la façon de construire une image. Regardez cet exemple simple.

À l'intérieur du terminal, exécutez :

`docker build <chemin du dossier avec Dockerfile dedans>`.

Cette commande construira une image basée sur les instructions données dans le Dockerfile.

Première ligne : `FROM nodesource/trusty5.1`

Cette ligne indique que la couche de base de cette image est une autre image appelée `nodesource/trusty5.1`. Par défaut, Docker essaiera d'abord de rechercher cette image localement. Si elle n'est pas là, elle tirera cette image depuis Docker Hub, ou depuis un autre registre d'images Docker. Vous devez donc simplement configurer le client Docker pour rechercher des images dans un autre registre d'images.

Deuxième ligne : `WORKDIR /app`

Cette ligne indique à Docker que toutes les commandes suivantes exécutées via `RUN` dans le Dockerfile seront exécutées à partir de `/app`.

Troisième ligne : `ADD . /app`

Cette ligne indique à Docker quels systèmes de fichiers fusionner lors de la construction. Dans cet exemple, nous voyons que la couche de superposition est le répertoire courant, relatif au Dockerfile, et que la couche de base est `/app` à l'intérieur de `nodesource/trusty5.1` (une image). Le sous-système de fichiers `/app` du système de fichiers de base sera fusionné avec un système de fichiers de superposition. Si le système de fichiers `/app` n'existe pas dans la couche de base, il sera créé en tant que dossier vide.

La commande `RUN` exécutera une commande à l'intérieur d'une image lors de sa construction via le shell par défaut `/bin/sh`.

`RUN <commande>` ; === /bin/sh <commande>

La commande `EXPOSE` servira de documentation pour un utilisateur afin de voir quel port l'application utilise. Ce n'est pas nécessaire.

`CMD` exécutera une commande dans un conteneur qui sera construit à partir de cette image au démarrage.

Dans cet exemple, `nodesource/thrusty5.1` est une image Ubuntu avec nodeJs 5.1 installé à l'intérieur. Dans le répertoire `./app` relatif au Dockerfile, nous avons une application nodeJs. En les fusionnant, nous obtiendrons une image d'Ubuntu avec nodeJs 5.1 installé et mon application à l'intérieur dans le répertoire `/app`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8DpWaxi69Ztn6YUS0c-oAQ.png)

Nous pouvons ensuite lancer autant de conteneurs que nous le souhaitons à partir de ce modèle. Chaque conteneur exécutera `npm start` à l'intérieur du répertoire `/app` d'un conteneur au démarrage.

#### Conteneurs Docker

Les conteneurs Docker, comme vous le savez déjà, sont des copies en cours d'exécution d'une image. Une chose supplémentaire que Docker fait lors de la création d'un conteneur à partir d'une image est qu'il ajoute un système de fichiers en lecture-écriture par-dessus le système de fichiers de l'image, car le système de fichiers de l'image est en lecture seule.

Les conteneurs Docker sont un peu différents des conteneurs Linux habituels. Les conteneurs Docker sont conçus spécifiquement pour exécuter un seul processus dans un environnement isolé d'un conteneur Linux. C'est pourquoi nous avons `CMD` dans le Dockerfile, qui indique quel processus cela va être. Le conteneur Docker sera automatiquement terminé une fois qu'il n'y a plus de processus en cours d'exécution à l'intérieur.

Les conteneurs Docker ne sont pas censés maintenir d'état, donc vous ne pouvez pas vous connecter en SSH à votre conteneur Docker (bien que techniquement vous puissiez, mais ne le faites pas). Vous ne devez pas avoir plusieurs processus en cours d'exécution simultanément, comme, par exemple, la base de données et l'application qui l'utilise. Dans ce cas, vous utiliseriez 2 conteneurs séparés et les feriez communiquer entre eux. Les conteneurs Docker sont un cas d'utilisation spécifique des conteneurs Linux pour construire des applications sans état faiblement couplées en tant que services.

#### Communication inter-conteneurs

Comme je l'ai mentionné ci-dessus, chaque conteneur ne doit exécuter qu'un seul processus. Donc, peut-être qu'une question naturelle émergera maintenant : _si, par exemple, mon application est en cours d'exécution dans un conteneur et la base de données est en cours d'exécution dans un autre, comment me connecter de mon application à une base de données qui est en cours d'exécution dans un autre conteneur ? Vous ne pouvez pas vous connecter à localhost dans ce cas._

Docker a introduit la mise en réseau pour les conteneurs autonomes. Un aperçu de très haut niveau de l'utilisation du réseau ressemble à ceci : vous créez un nouveau réseau, qui crée un sous-réseau pour ce réseau seul. Vous démarrez un conteneur et l'attachez à ce réseau, et tous les conteneurs attachés au même réseau pourront se ping les uns les autres, comme s'ils étaient sur un LAN. Ensuite, vous pouvez vous connecter d'un service en cours d'exécution dans un conteneur à un service en cours d'exécution dans un autre, tant qu'ils sont sur le même réseau.

_D'accord, à quoi cela ressemble-t-il maintenant ?_

Exécutez `docker network create <un nom>` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*LNlVkn4I93vFW1sNrasDqA.png)

Vous pouvez lister tous les réseaux disponibles en exécutant `docker network list` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*qBG1grwllDP8zOe7q5MW7w.png)

Exécutez `docker network inspect <id ou nom du réseau>` pour voir le sous-réseau du réseau et quels conteneurs y sont actuellement attachés :

![Image](https://cdn-media-1.freecodecamp.org/images/1*X4gU1bu0sbpz8TJt1DFtjw.png)

Comme vous pouvez le voir, il montre le sous-réseau du réseau, la passerelle par défaut, et nous voyons également qu'il n'y a pas de conteneurs attachés.

Maintenant, je vais créer 2 conteneurs, à partir de 2 images différentes, `nodejsapi`, `mongo` et les exécuter. Les options `--net` indiquent quel réseau utiliser :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Qfi-pZtUAXRoiqfveX7N1Q.png)

`docker run <nom de l'image>` crée un conteneur à partir d'une image et le démarre. Maintenant, je vais inspecter le réseau à nouveau :

![Image](https://cdn-media-1.freecodecamp.org/images/1*b6fFSJUXra7O2UU4a1HF7A.png)

Comme vous pouvez le voir maintenant, 2 conteneurs sont en cours d'exécution attachés à ce réseau. Nous pouvons également voir les IP qu'ils utilisent et qu'ils sont en cours d'exécution sur le même sous-réseau. Je devrais être en mesure de ping un conteneur depuis un autre maintenant.

Obtenons une IP de l'un des conteneurs en cours d'exécution :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ethtune7MW6uy8hhFuK2ig.png)

Ici, j'ai exécuté la commande `ifconfig` à l'intérieur d'un conteneur avec l'id `8d3aaca5750f` et j'ai redirigé la sortie vers mon terminal.

L'IP est `172.19.0.2`.

Depuis ce conteneur, je devrais être en mesure de ping un autre avec une IP de `172.19.0.3` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*p8c-70461vvKD1Tt_C_9IA.png)

C'était juste un simple exemple de réseaux docker. Il y a beaucoup plus à découvrir, alors consultez la [documentation officielle](https://docs.docker.com/network/network-tutorial-standalone/).

#### Volumes

Comme je l'ai dit auparavant, les conteneurs Docker ne sont pas censés maintenir d'état. Mais que faire si nous avons besoin d'état ? En fait, certains processus sont intrinsèquement étatiques, comme une base de données. Par exemple, une base de données doit maintenir tous les fichiers avec les données, car c'est le but de la base de données. Si nous stockons ces données à l'intérieur d'un conteneur, lorsqu'il disparaît, les données aussi. De plus, nous ne pouvons pas partager ces données entre plusieurs instances du conteneur.

Pour résoudre ce problème, Docker a introduit les volumes. Les volumes nous permettent de stocker des données sur la machine hôte, ou sur n'importe quelle autre machine d'ailleurs, même dans le cloud et de lier le conteneur (ou plusieurs conteneurs) à ce stockage.

Par exemple, vous avez pu voir précédemment comment j'ai créé un conteneur à partir d'une image MongoDB et l'ai exécuté en utilisant cette commande :

`docker run -d --net=myTestNetwork mongo`

Lors de l'exécution d'un conteneur comme celui-ci, Mongo DB s'exécutera à l'intérieur de ce conteneur Linux, et enregistrera les fichiers de la base de données sous le répertoire `/data/db` à l'intérieur du conteneur.

Maintenant, considérons ceci :

`docker run -d -v /folder-on-host-machine/data/db:/data/db --net=myTestNetwork mongo`.

Le drapeau `-v` monte un volume sur un conteneur, donc maintenant les données entre le dossier de l'hôte `/folder-on-host-machine/data/db` et le conteneur `/data/db` seront synchronisées. Maintenant, nous pouvons potentiellement exécuter plusieurs instances d'un conteneur MongoDB et les lier toutes à ce volume sur une machine hôte. Si l'une des instances s'arrête, une autre est toujours disponible et les données ne sont pas perdues car les données sont stockées sur une machine hôte, pas à l'intérieur d'un conteneur. Le conteneur lui-même est sans état, comme il se doit.

Il y a beaucoup plus à apprendre sur les volumes, comme les détails et les cas d'utilisation, mais nous ne les couvrirons pas dans cet article. Ici, j'ai juste expliqué ce qu'ils sont et pourquoi nous en avons besoin.

### Mots finaux

Donc, voici Docker, en un mot ! C'est une technologie incroyable qui révolutionne la façon dont nous développons, déployons et mettons à l'échelle nos applications. Ici, nous n'avons fait qu'effleurer la surface, il y a plus à découvrir.

Tout retour constructif est apprécié.

Si vous êtes arrivé jusqu'ici, veuillez me donner quelques "claps" :)

![Image](https://cdn-media-1.freecodecamp.org/images/1*puO9QPsENQ5ww1QKNuf6tw.gif)