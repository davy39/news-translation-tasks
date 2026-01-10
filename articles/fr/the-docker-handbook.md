---
title: Le manuel Docker – Apprendre Docker pour les débutants
subtitle: ''
author: Farhan Hasin Chowdhury
co_authors: []
series: null
date: '2021-02-01T16:35:00.000Z'
originalURL: https://freecodecamp.org/news/the-docker-handbook
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/The-Docker-Handbook-Mockup.png
tags:
- name: containerization
  slug: containerization
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: Docker compose
  slug: docker-compose
- name: Docker Containers
  slug: docker-containers
- name: JavaScript
  slug: javascript
seo_title: Le manuel Docker – Apprendre Docker pour les débutants
seo_desc: 'The concept of containerization itself is pretty old. But the emergence
  of the Docker Engine in 2013 has made it much easier to containerize your applications.

  According to the Stack Overflow Developer Survey - 2020, Docker is the #1 most wanted
  plat...'
---

Le concept de conteneurisation lui-même est assez ancien. Mais l'émergence du [Docker Engine](https://docs.docker.com/get-started/overview/#docker-engine) en 2013 a rendu beaucoup plus facile la conteneurisation de vos applications.

Selon l'[Enquête des développeurs Stack Overflow - 2020](https://insights.stackoverflow.com/survey/2020#overview), [Docker](https://docker.com/) est la [plateforme la plus souhaitée](https://insights.stackoverflow.com/survey/2020#technology-most-loved-dreaded-and-wanted-platforms-wanted5), la [plateforme la plus aimée](https://insights.stackoverflow.com/survey/2020#technology-most-loved-dreaded-and-wanted-platforms-loved5), et également la [plateforme la plus populaire](https://insights.stackoverflow.com/survey/2020#technology-platforms).

Bien que cela soit très demandé, commencer peut sembler un peu intimidant au début. Alors dans ce livre, nous allons apprendre tout, des bases à un niveau plus intermédiaire de la conteneurisation. Après avoir parcouru l'ensemble du livre, vous devriez être capable de :

* Conteneuriser (presque) n'importe quelle application
* Télécharger des images Docker personnalisées vers des registres en ligne
* Travailler avec plusieurs conteneurs en utilisant Docker Compose

## Prérequis

* Familiarité avec le terminal Linux
* Familiarité avec JavaScript (certains projets ultérieurs utilisent JavaScript)

## Table des matières

* [Introduction à la conteneurisation et Docker](#heading-introduction-a-la-conteneurisation-et-docker)
* [Comment installer Docker](#heading-comment-installer-docker)
  * [Comment installer Docker sur macOS](#heading-comment-installer-docker-sur-macos)
  * [Comment installer Docker sur Windows](#heading-comment-installer-docker-sur-windows)
  * [Comment installer Docker sur Linux](#heading-comment-installer-docker-sur-linux)
* [Hello World dans Docker - Introduction aux bases de Docker](#heading-hello-world-dans-docker-introduction-aux-bases-de-docker)
  * [Qu'est-ce qu'un conteneur ?](#heading-quest-ce-quun-conteneur)
  * [Qu'est-ce qu'une image Docker ?](#heading-quest-ce-quune-image-docker)
  * [Qu'est-ce qu'un registre Docker ?](#heading-quest-ce-quun-registre-docker)
  * [Aperçu de l'architecture Docker](#heading-apercu-de-larchitecture-docker)
  * [Le tableau complet](#heading-le-tableau-complet)
* [Bases de la manipulation des conteneurs Docker](#heading-bases-de-la-manipulation-des-conteneurs-docker)
  * [Comment exécuter un conteneur](#heading-comment-executer-un-conteneur)
  * [Comment publier un port](#heading-comment-publier-un-port)
  * [Comment utiliser le mode détaché](#heading-comment-utiliser-le-mode-detache)
  * [Comment lister les conteneurs](#heading-comment-lister-les-conteneurs)
  * [Comment nommer ou renommer un conteneur](#heading-comment-nommer-ou-renommer-un-conteneur)
  * [Comment arrêter ou tuer un conteneur en cours d'exécution](#heading-comment-arreter-ou-tuer-un-conteneur-en-cours-dexecution)
  * [Comment redémarrer un conteneur](#heading-comment-redemarrer-un-conteneur)
  * [Comment créer un conteneur sans l'exécuter](#heading-comment-creer-un-conteneur-sans-lexecuter)
  * [Comment supprimer les conteneurs suspendus](#heading-comment-supprimer-les-conteneurs-suspendus)
  * [Comment exécuter un conteneur en mode interactif](#heading-comment-executer-un-conteneur-en-mode-interactif)
  * [Comment exécuter des commandes à l'intérieur d'un conteneur](#heading-comment-executer-des-commandes-a-linterieur-dun-conteneur)
  * [Comment travailler avec des images exécutables](#heading-comment-travailler-avec-des-images-executables)
* [Bases de la manipulation des images Docker](#heading-bases-de-la-manipulation-des-images-docker)
  * [Comment créer une image Docker](#heading-comment-creer-une-image-docker)
  * [Comment étiqueter les images Docker](#heading-comment-etiqueter-les-images-docker)
  * [Comment lister et supprimer les images Docker](#heading-comment-lister-et-supprimer-les-images-docker)
  * [Comment comprendre les nombreuses couches d'une image Docker](#heading-comment-comprendre-les-nombreuses-couches-dune-image-docker)
  * [Comment construire NGINX à partir de la source](#heading-comment-construire-nginx-a-partir-de-la-source)
  * [Comment optimiser les images Docker](#heading-comment-optimiser-les-images-docker)
  * [Embrasser Alpine Linux](#heading-embrasser-alpine-linux)
  * [Comment créer des images Docker exécutables](#heading-comment-creer-des-images-docker-executables)
  * [Comment partager vos images Docker en ligne](#heading-comment-partager-vos-images-docker-en-ligne)
* [Comment conteneuriser une application JavaScript](#heading-comment-conteneuriser-une-application-javascript)
  * [Comment écrire le Dockerfile de développement](#heading-comment-ecrire-le-dockerfile-de-developpement)
  * [Comment travailler avec les montages de liaison dans Docker](#heading-comment-travailler-avec-les-montages-de-liaison-dans-docker)
  * [Comment travailler avec les volumes anonymes dans Docker](#heading-comment-travailler-avec-les-volumes-anonymes-dans-docker)
  * [Comment effectuer des constructions multi-étapes dans Docker](#heading-comment-effectuer-des-constructions-multi-etapes-dans-docker)
  * [Comment ignorer les fichiers inutiles](#heading-comment-ignorer-les-fichiers-inutiles)
* [Bases de la manipulation du réseau dans Docker](#heading-bases-de-la-manipulation-du-reseau-dans-docker)
  * [Bases du réseau Docker](#heading-bases-du-reseau-docker)
  * [Comment créer un pont défini par l'utilisateur dans Docker](#heading-comment-creer-un-pont-defini-par-lutilisateur-dans-docker)
  * [Comment attacher un conteneur à un réseau dans Docker](#heading-comment-attach-un-conteneur-a-un-reseau-dans-docker)
  * [Comment détacher des conteneurs d'un réseau dans Docker](#heading-comment-detacher-des-conteneurs-dun-reseau-dans-docker)
  * [Comment se débarrasser des réseaux dans Docker](#heading-comment-se-debarrasser-des-reseaux-dans-docker)
* [Comment conteneuriser une application JavaScript multi-conteneurs](#heading-comment-conteneuriser-une-application-javascript-multi-conteneurs)
  * [Comment exécuter le serveur de base de données](#heading-comment-executer-le-serveur-de-base-de-donnees)
  * [Comment travailler avec des volumes nommés dans Docker](#heading-comment-travailler-avec-des-volumes-nommes-dans-docker)
  * [Comment accéder aux journaux depuis un conteneur dans Docker](#heading-comment-acceder-aux-journaux-depuis-un-conteneur-dans-docker)
  * [Comment créer un réseau et attacher le serveur de base de données dans Docker](#heading-comment-creer-un-reseau-et-attach-le-serveur-de-base-de-donnees-dans-docker)
  * [Comment écrire le Dockerfile](#heading-comment-ecrire-le-dockerfile)
  * [Comment exécuter des commandes dans un conteneur en cours d'exécution](#heading-comment-executer-des-commandes-dans-un-conteneur-en-cours-dexecution)
  * [Comment écrire des scripts de gestion dans Docker](#heading-comment-ecrire-des-scripts-de-gestion-dans-docker)
* [Comment composer des projets en utilisant Docker-Compose](#heading-comment-composer-des-projets-en-utilisant-docker-compose)
  * [Bases de Docker Compose](#heading-bases-de-docker-compose)
  * [Comment démarrer les services dans Docker Compose](#heading-comment-demarrer-les-services-dans-docker-compose)
  * [Comment lister les services dans Docker Compose](#heading-comment-lister-les-services-dans-docker-compose)
  * [Comment exécuter des commandes à l'intérieur d'un service en cours d'exécution dans Docker Compose](#heading-comment-executer-des-commandes-a-linterieur-dun-service-en-cours-dexecution-dans-docker-compose)
  * [Comment accéder aux journaux depuis un service en cours d'exécution dans Docker Compose](#heading-comment-acceder-aux-journaux-depuis-un-service-en-cours-dexecution-dans-docker-compose)
  * [Comment arrêter les services dans Docker Compose](#heading-comment-arreter-les-services-dans-docker-compose)
  * [Comment composer une application full-stack dans Docker Compose](#heading-comment-composer-une-application-full-stack-dans-docker-compose)
* [Conclusion](#heading-conclusion)

## Code du projet

Le code des projets d'exemple peut être trouvé dans le dépôt suivant :

%[https://github.com/fhsinchy/docker-handbook-projects/]

Vous pouvez trouver le code complet dans la branche `completed`.

## Contributions

Ce livre est entièrement open-source et les contributions de qualité sont les bienvenues. Vous pouvez trouver le contenu complet dans le dépôt suivant :

%[https://github.com/fhsinchy/the-docker-handbook]

Je fais généralement mes modifications et mises à jour sur la version GitBook du livre en premier, puis je les publie sur freeCodeCamp. Vous pouvez trouver la version toujours mise à jour et souvent instable du livre au lien suivant :

%[https://docker-handbook.farhan.dev/]

Si vous cherchez une version figée mais stable du livre, alors freeCodeCamp sera le meilleur endroit où aller :

%[https://www.freecodecamp.org/news/the-docker-handbook/]

Quelle que soit la version du livre que vous finissez par lire, n'oubliez pas de me faire savoir votre opinion. Les critiques constructives sont toujours les bienvenues.

## Introduction à la conteneurisation et Docker

Selon [IBM](https://www.ibm.com/cloud/learn/containerization#toc-what-is-co-r25Smlqq),

> La conteneurisation implique l'encapsulation ou l'empaquetage du code logiciel et de toutes ses dépendances afin qu'il puisse s'exécuter uniformément et de manière cohérente sur toute infrastructure.

En d'autres termes, la conteneurisation vous permet de regrouper votre logiciel avec toutes ses dépendances dans un package autonome afin qu'il puisse être exécuté sans passer par un processus de configuration fastidieux.

Considérons un scénario réel ici. Supposons que vous avez développé une application de gestion de livres géniale qui peut stocker des informations concernant tous les livres que vous possédez, et qui peut également servir de système de prêt de livres pour vos amis.

Si vous faites une liste des dépendances, cette liste peut ressembler à ce qui suit :

* Node.js
* Express.js
* SQLite3

Eh bien, théoriquement, cela devrait suffire. Mais pratiquement, il y a aussi d'autres choses. Il s'avère que [Node.js](https://nodejs.org/) utilise un outil de construction connu sous le nom de `node-gyp` pour construire des modules complémentaires natifs. Et selon les [instructions d'installation](https://github.com/nodejs/node-gyp#installation) dans le [dépôt officiel](https://github.com/nodejs/node-gyp), cet outil de construction nécessite Python 2 ou 3 et une chaîne d'outils de compilation C/C++ appropriée.

En tenant compte de tout cela, la liste finale des dépendances est la suivante :

* Node.js
* Express.js
* SQLite3
* Python 2 ou 3
* Chaîne d'outils C/C++

L'installation de Python 2 ou 3 est assez simple quelle que soit la plateforme que vous utilisez. La configuration de la chaîne d'outils C/C++ est assez facile sur Linux, mais sur Windows et Mac, c'est une tâche pénible.

Sur Windows, le package d'outils de construction C++ mesure des gigaoctets et prend un certain temps à installer. Sur un Mac, vous pouvez soit installer l'application gigantesque [Xcode](https://developer.apple.com/xcode/), soit le package beaucoup plus petit [Command Line Tools for Xcode](https://developer.apple.com/downloads/).

Quelle que soit celle que vous installez, elle peut encore se casser lors des mises à jour du système d'exploitation. En fait, le problème est si répandu qu'il existe des [notes d'installation pour macOS Catalina](https://github.com/nodejs/node-gyp/blob/master/macOS_Catalina.md) disponibles sur le dépôt officiel.

Supposons que vous avez traversé toutes les difficultés de configuration des dépendances et que vous avez commencé à travailler sur le projet. Cela signifie-t-il que vous êtes hors de danger maintenant ? Bien sûr que non.

Que se passe-t-il si vous avez un coéquipier qui utilise Windows alors que vous utilisez Linux. Maintenant, vous devez prendre en compte les incohérences de la manière dont ces deux systèmes d'exploitation différents gèrent les chemins. Ou le fait que des technologies populaires comme [nginx](https://nginx.org/) ne sont pas bien optimisées pour fonctionner sur Windows. Certaines technologies comme [Redis](https://redis.io/) ne sont même pas pré-construites pour Windows.

Même si vous passez toute la phase de développement, que se passe-t-il si la personne responsable de la gestion des serveurs suit la mauvaise procédure de déploiement ?

Tous ces problèmes peuvent être résolus si seulement vous pouviez d'une manière ou d'une autre :

* Développer et exécuter l'application dans un environnement isolé (appelé conteneur) qui correspond à votre environnement de déploiement final.
* Mettre votre application dans un seul fichier (appelé image) avec toutes ses dépendances et les configurations de déploiement nécessaires.
* Et partager cette image via un serveur central (appelé registre) accessible par toute personne avec une autorisation appropriée.

Vos coéquipiers pourront alors télécharger l'image depuis le registre, exécuter l'application telle quelle dans un environnement isolé, exempt des incohérences spécifiques à la plateforme, ou même déployer directement sur un serveur, puisque l'image contient toutes les configurations de production appropriées.

C'est l'idée derrière la conteneurisation : mettre vos applications dans un package autonome, les rendant portables et reproductibles dans divers environnements.

**Maintenant, la question est « Quel rôle Docker joue-t-il ici ? »**

Comme je l'ai déjà expliqué, la conteneurisation est une idée qui résout une myriade de problèmes dans le développement logiciel en mettant les choses dans des boîtes.

Cette idée a plusieurs implémentations. [Docker](https://www.docker.com/) est une telle implémentation. C'est une plateforme de conteneurisation open-source qui vous permet de conteneuriser vos applications, de les partager en utilisant des registres publics ou privés, et aussi de les [orchestrer](https://docs.docker.com/get-started/orchestration/).

Maintenant, Docker n'est pas le seul outil de conteneurisation sur le marché, c'est simplement le plus populaire. Un autre moteur de conteneurisation que j'aime s'appelle [Podman](https://podman.io/) développé par Red Hat. D'autres outils comme [Kaniko](https://github.com/GoogleContainerTools/kaniko) par Google, [rkt](https://coreos.com/rkt/) par CoreOS sont incroyables, mais ils ne sont pas encore prêts à être un remplacement direct pour Docker.

De plus, si vous voulez une leçon d'histoire, vous pouvez lire l'incroyable [Une brève histoire des conteneurs : des années 1970 à aujourd'hui](https://blog.aquasec.com/a-brief-history-of-containers-from-1970s-chroot-to-docker-2016) qui couvre la plupart des principaux tournants de la technologie.

## Comment installer Docker

L'installation de Docker varie considérablement en fonction du système d'exploitation que vous utilisez. Mais elle est universellement simple sur tous les systèmes.

Docker fonctionne parfaitement sur les trois principales plateformes, Mac, Windows et Linux. Parmi les trois, le processus d'installation sur Mac est le plus facile, donc nous allons commencer par là.

### Comment installer Docker sur macOS

Sur un Mac, tout ce que vous avez à faire est de naviguer vers la page de [téléchargement officielle](https://www.docker.com/products/docker-desktop) et de cliquer sur le bouton _Download for Mac (stable)_.

Vous obtiendrez un fichier _Apple Disk Image_ d'apparence régulière et à l'intérieur du fichier, il y aura l'application. Tout ce que vous avez à faire est de glisser le fichier et de le déposer dans votre répertoire Applications.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/drag-docker-in-applications-directory.png)

Vous pouvez démarrer Docker en double-cliquant simplement sur l'icône de l'application. Une fois l'application démarrée, vous verrez l'icône Docker apparaître dans votre barre de menu.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/docker-icon-in-menubar.png)

Maintenant, ouvrez le terminal et exécutez `docker --version` et `docker-compose --version` pour vous assurer du succès de l'installation.

### Comment installer Docker sur Windows

Sur Windows, la procédure est presque la même, sauf qu'il y a quelques étapes supplémentaires que vous devrez suivre. Les étapes d'installation sont les suivantes :

1. Naviguez vers [ce site](https://docs.microsoft.com/en-us/windows/wsl/install-win10) et suivez les instructions pour installer WSL2 sur Windows 10.
2. Ensuite, naviguez vers la page de [téléchargement officielle](https://www.docker.com/products/docker-desktop) et cliquez sur le bouton _Download for Windows (stable)_.
3. Double-cliquez sur l'installateur téléchargé et passez par l'installation avec les paramètres par défaut.

Une fois l'installation terminée, démarrez _Docker Desktop_ soit à partir du menu démarrer soit de votre bureau. L'icône docker devrait apparaître sur votre barre des tâches.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/docker-icon-in-taskbar.png)

Maintenant, ouvrez Ubuntu ou toute autre distribution que vous avez installée depuis le Microsoft Store. Exécutez les commandes `docker --version` et `docker-compose --version` pour vous assurer que l'installation a réussi.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/docker-and-compose-version-on-windows.png)

Vous pouvez également accéder à Docker depuis votre invite de commande ou PowerShell habituel. C'est juste que je préfère utiliser WSL2 plutôt que toute autre ligne de commande sur Windows.

### Comment installer Docker sur Linux

L'installation de Docker sur Linux est un processus un peu différent, et selon la distribution que vous utilisez, cela peut varier encore plus. Mais pour être honnête, l'installation est tout aussi facile (si ce n'est plus facile) que les deux autres plateformes.

Le package Docker Desktop sur Windows ou Mac est une collection d'outils comme `Docker Engine`, `Docker Compose`, `Docker Dashboard`, `Kubernetes` et quelques autres goodies.

Sur Linux, cependant, vous n'obtenez pas un tel bundle. Au lieu de cela, vous installez tous les outils nécessaires manuellement. Les procédures d'installation pour différentes distributions sont les suivantes :

* Si vous êtes sur Ubuntu, vous pouvez suivre la section [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/) de la documentation officielle.
* Pour les autres distributions, des guides _d'installation par distribution_ sont disponibles dans la documentation officielle.
  * [Install Docker Engine on Debian](https://docs.docker.com/engine/install/debian/)
  * [Install Docker Engine on Fedora](https://docs.docker.com/engine/install/fedora/)
  * [Install Docker Engine on CentOS](https://docs.docker.com/engine/install/centos/)
* Si vous êtes sur une distribution qui n'est pas listée dans la documentation, vous pouvez suivre le guide [Install Docker Engine from binaries](https://docs.docker.com/engine/install/binaries/) à la place.
* Quelle que soit la procédure que vous suivez, vous devrez passer par certaines [étapes post-installation pour Linux](https://docs.docker.com/engine/install/linux-postinstall/) qui sont très importantes.
* Une fois que vous avez terminé l'installation de docker, vous devrez installer un autre outil nommé Docker Compose. Vous pouvez suivre le guide [Install Docker Compose](https://docs.docker.com/compose/install/) de la documentation officielle.

Une fois l'installation terminée, ouvrez le terminal et exécutez `docker --version` et `docker-compose --version` pour vous assurer du succès de l'installation.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/docker-and-compose-version-on-linux.png)

Bien que Docker fonctionne assez bien quelle que soit la plateforme que vous utilisez, je préfère Linux aux autres. Tout au long du livre, je vais alterner entre mes stations de travail [Ubuntu 20.10](https://releases.ubuntu.com/20.10/) et [Fedora 33](https://fedoramagazine.org/announcing-fedora-33/).

Une autre chose que je voudrais clarifier dès le départ, c'est que je n'utiliserai aucun outil GUI pour travailler avec Docker tout au long du livre.

Je suis conscient des bons outils GUI disponibles pour différentes plateformes, mais l'apprentissage des commandes docker courantes est l'un des objectifs principaux de ce livre.

## Hello World dans Docker – Introduction aux bases de Docker

Maintenant que vous avez Docker en cours d'exécution sur votre machine, il est temps pour vous d'exécuter votre premier conteneur. Ouvrez le terminal et exécutez la commande suivante :

```
docker run hello-world

# Unable to find image 'hello-world:latest' locally
# latest: Pulling from library/hello-world
# 0e03bdcc26d7: Pull complete 
# Digest: sha256:4cf9c47f86df71d48364001ede3a4fcd85ae80ce02ebad74156906caff5378bc
# Status: Downloaded newer image for hello-world:latest
# 
# Hello from Docker!
# This message shows that your installation appears to be working correctly.
# 
# To generate this message, Docker took the following steps:
#  1. The Docker client contacted the Docker daemon.
#  2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
#     (amd64)
#  3. The Docker daemon created a new container from that image which runs the
#     executable that produces the output you are currently reading.
#  4. The Docker daemon streamed that output to the Docker client, which sent it
#     to your terminal.
#
# To try something more ambitious, you can run an Ubuntu container with:
#  $ docker run -it ubuntu bash
# 
# Share images, automate workflows, and more with a free Docker ID:
#  https://hub.docker.com/
#
# For more examples and ideas, visit:
#  https://docs.docker.com/get-started/

```

L'image [hello-world](https://hub.docker.com/_/hello-world) est un exemple de conteneurisation minimale avec Docker. Elle contient un seul programme compilé à partir d'un fichier [hello.c](https://github.com/docker-library/hello-world/blob/master/hello.c) responsable de l'impression du message que vous voyez sur votre terminal.

Maintenant, dans votre terminal, vous pouvez utiliser la commande `docker ps -a` pour jeter un coup d'œil à tous les conteneurs qui sont actuellement en cours d'exécution ou qui ont été exécutés dans le passé :

```
docker ps -a

# CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES
# 128ec8ceab71        hello-world         "/hello"            14 seconds ago      Exited (0) 13 seconds ago                      exciting_chebyshev
```

Dans la sortie, un conteneur nommé `exciting_chebyshev` a été exécuté avec l'identifiant de conteneur `128ec8ceab71` en utilisant l'image `hello-world`. Il a `Exited (0) 13 seconds ago` où le code de sortie `(0)` signifie qu'aucune erreur n'a été produite pendant l'exécution du conteneur.

Maintenant, afin de comprendre ce qui vient de se passer en coulisses, vous devez vous familiariser avec l'architecture Docker et trois concepts très fondamentaux de la conteneurisation en général, qui sont les suivants :

* Conteneur
* Image
* Registre

J'ai listé les trois concepts par ordre alphabétique et commencerai mes explications avec le premier de la liste.

### Qu'est-ce qu'un conteneur ?

Dans le monde de la conteneurisation, il ne peut y avoir rien de plus fondamental que le concept de conteneur.

Le site officiel des ressources Docker [resources](https://www.docker.com/resources/what-container) dit -

> Un conteneur est une abstraction au niveau de l'application qui regroupe le code et les dépendances. Au lieu de virtualiser toute la machine physique, les conteneurs virtualisent uniquement le système d'exploitation hôte.

Vous pouvez considérer les conteneurs comme la prochaine génération de machines virtuelles.

Tout comme les machines virtuelles, les conteneurs sont des environnements complètement isolés du système hôte ainsi que les uns des autres. Ils sont également beaucoup plus légers que la machine virtuelle traditionnelle, donc un grand nombre de conteneurs peuvent être exécutés simultanément sans affecter les performances du système hôte.

Les conteneurs et les machines virtuelles sont en fait différentes façons de virtualiser votre matériel physique. La principale différence entre ces deux méthodes est la méthode de virtualisation.

Les machines virtuelles sont généralement créées et gérées par un programme connu sous le nom d'hyperviseur, comme [Oracle VM VirtualBox](https://www.virtualbox.org/), [VMware Workstation](https://www.vmware.com/), [KVM](https://www.linux-kvm.org/), [Microsoft Hyper-V](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/about/) et ainsi de suite. Ce programme hyperviseur se place généralement entre le système d'exploitation hôte et les machines virtuelles pour servir de moyen de communication.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/virtual-machines.svg)

Chaque machine virtuelle est livrée avec son propre système d'exploitation invité qui est tout aussi lourd que le système d'exploitation hôte.

L'application s'exécutant à l'intérieur d'une machine virtuelle communique avec le système d'exploitation invité, qui parle à l'hyperviseur, qui parle ensuite au système d'exploitation hôte pour allouer les ressources nécessaires de l'infrastructure physique à l'application en cours d'exécution.

Comme vous pouvez le voir, il y a une longue chaîne de communication entre les applications s'exécutant à l'intérieur des machines virtuelles et l'infrastructure physique. L'application s'exécutant à l'intérieur de la machine virtuelle peut ne prendre qu'une petite quantité de ressources, mais le système d'exploitation invité ajoute un surcoût notable.

Contrairement à une machine virtuelle, un conteneur effectue le travail de virtualisation de manière plus intelligente. Au lieu d'avoir un système d'exploitation invité complet à l'intérieur d'un conteneur, il utilise simplement le système d'exploitation hôte via le runtime du conteneur tout en maintenant l'isolation – tout comme une machine virtuelle traditionnelle.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/containers.svg)

Le runtime du conteneur, c'est-à-dire Docker, se place entre les conteneurs et le système d'exploitation hôte au lieu d'un hyperviseur. Les conteneurs communiquent ensuite avec le runtime du conteneur qui communique ensuite avec le système d'exploitation hôte pour obtenir les ressources nécessaires de l'infrastructure physique.

En conséquence de l'élimination de toute la couche du système d'exploitation invité, les conteneurs sont beaucoup plus légers et moins gourmands en ressources que les machines virtuelles traditionnelles.

Pour démontrer ce point, regardez le bloc de code suivant :

```
uname -a
# Linux alpha-centauri 5.8.0-22-generic #23-Ubuntu SMP Fri Oct 9 00:34:40 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux

docker run alpine uname -a
# Linux f08dbbe9199b 5.8.0-22-generic #23-Ubuntu SMP Fri Oct 9 00:34:40 UTC 2020 x86_64 Linux
```

Dans le bloc de code ci-dessus, j'ai exécuté la commande `uname -a` sur mon système d'exploitation hôte pour imprimer les détails du noyau. Ensuite, sur la ligne suivante, j'ai exécuté la même commande à l'intérieur d'un conteneur exécutant [Alpine Linux](https://alpinelinux.org/).

Comme vous pouvez le voir dans la sortie, le conteneur utilise effectivement le noyau de mon système d'exploitation hôte. Cela prouve le point que les conteneurs virtualisent le système d'exploitation hôte au lieu d'avoir leur propre système d'exploitation.

Si vous êtes sur une machine Windows, vous découvrirez que tous les conteneurs utilisent le noyau WSL2. Cela se produit parce que WSL2 agit comme le backend pour Docker sur Windows. Sur macOS, le backend par défaut est une VM s'exécutant sur l'hyperviseur [HyperKit](https://github.com/moby/hyperkit).

### Qu'est-ce qu'une image Docker ?

Les images sont des fichiers autonomes à plusieurs couches qui servent de modèle pour la création de conteneurs. Elles sont comme une copie gelée et en lecture seule d'un conteneur. Les images peuvent être échangées via des registres.

Par le passé, différents moteurs de conteneurs avaient différents formats d'images. Mais plus tard, l'[Open Container Initiative (OCI)](https://opencontainers.org/) a défini une spécification standard pour les images de conteneurs, qui est respectée par les principaux moteurs de conteneurisation. Cela signifie qu'une image construite avec Docker peut être utilisée avec un autre runtime comme Podman sans aucun problème supplémentaire.

Les conteneurs ne sont que des images en état d'exécution. Lorsque vous obtenez une image depuis Internet et exécutez un conteneur en utilisant cette image, vous créez essentiellement une autre couche temporaire modifiable par-dessus les précédentes couches en lecture seule.

Ce concept deviendra beaucoup plus clair dans les sections à venir de ce livre. Mais pour l'instant, gardez simplement à l'esprit que les images sont des fichiers en lecture seule à plusieurs couches transportant votre application dans un état souhaité.

### Qu'est-ce qu'un registre Docker ?

Vous avez déjà appris deux pièces très importantes du puzzle, les _Conteneurs_ et les _Images_. La pièce finale est le _Registre_.

Un registre d'images est un endroit centralisé où vous pouvez télécharger vos images et également télécharger des images créées par d'autres. [Docker Hub](https://hub.docker.com/) est le registre public par défaut pour Docker. Un autre registre d'images très populaire est [Quay](https://quay.io/) de Red Hat.

Tout au long de ce livre, j'utiliserai Docker Hub comme registre de mon choix.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/docker-hub.png)

Vous pouvez partager n'importe quel nombre d'images publiques sur Docker Hub gratuitement. Les gens du monde entier pourront les télécharger et les utiliser librement. Les images que j'ai téléchargées sont disponibles sur ma page de profil ([fhsinchy](https://hub.docker.com/u/fhsinchy)).

![Image](https://www.freecodecamp.org/news/content/images/2021/01/my-images-on-docker-hub.png)

En dehors de Docker Hub ou Quay, vous pouvez également créer votre propre registre d'images pour héberger des images privées. Il existe également un registre local qui s'exécute sur votre ordinateur et qui met en cache les images téléchargées depuis les registres distants.

### Aperçu de l'architecture Docker

Maintenant que vous êtes familier avec la plupart des concepts fondamentaux concernant la conteneurisation et Docker, il est temps pour vous de comprendre comment Docker, en tant que logiciel, a été conçu.

Le moteur se compose de trois composants principaux :

1. **Docker Daemon** : Le démon (`dockerd`) est un processus qui continue de s'exécuter en arrière-plan et attend les commandes du client. Le démon est capable de gérer divers objets Docker.
2. **Docker Client** : Le client (`docker`) est un programme d'interface de ligne de commande principalement responsable du transport des commandes émises par les utilisateurs.
3. **REST API** : L'API REST agit comme un pont entre le démon et le client. Toute commande émise à l'aide du client passe par l'API pour atteindre enfin le démon.

Selon la documentation officielle [docs](https://docs.docker.com/get-started/overview/#docker-architecture),

> « Docker utilise une architecture client-serveur. Le client Docker parle au démon Docker, qui effectue le travail lourd de construction, d'exécution et de distribution de vos conteneurs Docker ».

En tant qu'utilisateur, vous exécuterez généralement des commandes en utilisant le composant client. Le client utilise ensuite l'API REST pour atteindre le démon en cours d'exécution et faire votre travail.

### Le tableau complet

D'accord, assez parlé. Maintenant, il est temps pour vous de comprendre comment toutes ces pièces du puzzle que vous venez d'apprendre fonctionnent en harmonie. Avant de plonger dans l'explication de ce qui se passe réellement lorsque vous exécutez la commande `docker run hello-world`, laissez-moi vous montrer un petit diagramme que j'ai fait :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/docker-run-hello-world.svg)

Cette image est une version légèrement modifiée de celle trouvée dans la documentation officielle [docs](https://docs.docker.com/engine/images/architecture.svg). Les événements qui se produisent lorsque vous exécutez la commande sont les suivants :

1. Vous exécutez la commande `docker run hello-world` où `hello-world` est le nom d'une image.
2. Le client Docker contacte le démon et lui demande d'obtenir l'image `hello-world` et d'exécuter un conteneur à partir de celle-ci.
3. Le démon Docker recherche l'image dans votre dépôt local et réalise qu'elle n'y est pas, ce qui entraîne l'impression de `Unable to find image 'hello-world:latest' locally` sur votre terminal.
4. Le démon contacte ensuite le registre public par défaut, qui est Docker Hub, et télécharge la dernière copie de l'image `hello-world`, indiquée par la ligne `latest: Pulling from library/hello-world` dans votre terminal.
5. Le démon Docker crée ensuite un nouveau conteneur à partir de l'image fraîchement téléchargée.
6. Enfin, le démon Docker exécute le conteneur créé en utilisant l'image `hello-world`, affichant le mur de texte sur votre terminal.

C'est le comportement par défaut du démon Docker de rechercher des images dans le hub qui ne sont pas présentes localement. Mais une fois qu'une image a été récupérée, elle restera dans le cache local. Donc si vous exécutez la commande à nouveau, vous ne verrez pas les lignes suivantes dans la sortie :

```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
0e03bdcc26d7: Pull complete
Digest: sha256:d58e752213a51785838f9eed2b7a498ffa1cb3aa7f946dda11af39286c3db9a9
Status: Downloaded newer image for hello-world:latest
```

S'il existe une version plus récente de l'image disponible sur le registre public, le démon récupérera à nouveau l'image. Ce `:latest` est une balise. Les images ont généralement des balises significatives pour indiquer les versions ou les builds. Vous en apprendrez plus à ce sujet plus tard.

## Bases de la manipulation des conteneurs Docker

Dans les sections précédentes, vous avez appris les éléments de base de Docker et avez également exécuté un conteneur en utilisant la commande `docker run`.

Dans cette section, vous apprendrez la manipulation des conteneurs de manière beaucoup plus détaillée. La manipulation des conteneurs est l'une des tâches les plus courantes que vous effectuerez chaque jour, donc avoir une compréhension appropriée des différentes commandes est crucial.

Gardez à l'esprit, cependant, que ceci n'est pas une liste exhaustive de toutes les commandes que vous pouvez exécuter sur Docker. Je ne parlerai que des plus courantes. Chaque fois que vous voulez en savoir plus sur les commandes disponibles, visitez simplement la référence officielle pour la ligne de commande Docker.

### Comment exécuter un conteneur

Précédemment, vous avez utilisé `docker run` pour créer et démarrer un conteneur en utilisant l'image `hello-world`. La syntaxe générique de cette commande est la suivante :

```
docker run <nom de l'image>
```

Bien que ce soit une commande parfaitement valide, il existe une meilleure façon d'envoyer des commandes au démon `docker`.

Avant la version `1.13`, Docker n'avait que la syntaxe de commande mentionnée précédemment. Plus tard, la ligne de commande a été restructurée pour avoir la syntaxe suivante :

```
docker <objet> <commande> <options>
```

Dans cette syntaxe :

* `objet` indique le type d'objet Docker que vous allez manipuler. Cela peut être un objet `container`, `image`, `network` ou `volume`.
* `commande` indique la tâche à effectuer par le démon, c'est-à-dire la commande `run`.
* `options` peut être n'importe quel paramètre valide qui peut remplacer le comportement par défaut de la commande, comme l'option `--publish` pour le mappage de port.

Maintenant, en suivant cette syntaxe, la commande `run` peut être écrite comme suit :

```
docker container run <nom de l'image>
```

Le `nom de l'image` peut être celui de n'importe quelle image d'un registre en ligne ou de votre système local. Par exemple, vous pouvez essayer d'exécuter un conteneur en utilisant l'image [fhsinchy/hello-dock](https://hub.docker.com/r/fhsinchy/hello-dock). Cette image contient une simple application [Vue.js](https://vuejs.org/) qui s'exécute sur le port 80 à l'intérieur du conteneur.

Pour exécuter un conteneur en utilisant cette image, exécutez la commande suivante sur votre terminal :

```
docker container run --publish 8080:80 fhsinchy/hello-dock

# /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
# /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
# /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
# 10-listen-on-ipv6-by-default.sh: Getting the checksum of /etc/nginx/conf.d/default.conf
# 10-listen-on-ipv6-by-default.sh: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
# /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
# /docker-entrypoint.sh: Configuration complete; ready for start up
```

La commande est assez explicite. La seule partie qui peut nécessiter une explication est la partie `--publish 8080:80` qui sera expliquée dans la sous-section suivante.

### Comment publier un port

Les conteneurs sont des environnements isolés. Votre système hôte ne sait rien de ce qui se passe à l'intérieur d'un conteneur. Par conséquent, les applications s'exécutant à l'intérieur d'un conteneur restent inaccessibles depuis l'extérieur.

Pour permettre l'accès depuis l'extérieur d'un conteneur, vous devez publier le port approprié à l'intérieur du conteneur vers un port sur votre réseau local. La syntaxe courante pour l'option `--publish` ou `-p` est la suivante :

```
--publish <port hôte>:<port conteneur>
```

Lorsque vous avez écrit `--publish 8080:80` dans la sous-section précédente, cela signifiait que toute requête envoyée au port 8080 de votre système hôte sera transférée au port 80 à l'intérieur du conteneur.

Maintenant, pour accéder à l'application sur votre navigateur, visitez `http://127.0.0.1:8080`.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/hello-dock.png)

Vous pouvez arrêter le conteneur en appuyant simplement sur la combinaison de touches `ctrl + c` lorsque la fenêtre du terminal est en focus ou en fermant complètement la fenêtre du terminal.

### Comment utiliser le mode détaché

Une autre option très populaire de la commande `run` est l'option `--detach` ou `-d`. Dans l'exemple ci-dessus, pour que le conteneur continue de s'exécuter, vous deviez garder la fenêtre du terminal ouverte. La fermeture de la fenêtre du terminal a également arrêté le conteneur en cours d'exécution.

Cela est dû au fait que, par défaut, les conteneurs s'exécutent au premier plan et s'attachent au terminal comme tout autre programme normal invoqué depuis le terminal.

Afin de remplacer ce comportement et de garder un conteneur en cours d'exécution en arrière-plan, vous pouvez inclure l'option `--detach` avec la commande `run` comme suit :

```
docker container run --detach --publish 8080:80 fhsinchy/hello-dock

# 9f21cb77705810797c4b847dbd330d9c732ffddba14fb435470567a7a3f46cdc
```

Contrairement à l'exemple précédent, vous n'obtiendrez pas un mur de texte cette fois-ci. Au lieu de cela, ce que vous obtiendrez, c'est l'ID du conteneur nouvellement créé.

L'ordre des options que vous fournissez n'a pas vraiment d'importance. Si vous mettez l'option `--publish` avant l'option `--detach`, cela fonctionnera de la même manière. Une chose que vous devez garder à l'esprit dans le cas de la commande `run` est que le nom de l'image doit venir en dernier. Si vous mettez quoi que ce soit après le nom de l'image, cela sera passé comme argument au point d'entrée du conteneur (expliqué dans la sous-section [Exécuter des commandes à l'intérieur d'un conteneur](#executing-commands-inside-a-container)) et peut entraîner des situations inattendues.

### Comment lister les conteneurs

La commande `container ls` peut être utilisée pour lister les conteneurs qui sont actuellement en cours d'exécution. Pour ce faire, exécutez la commande suivante :

```
docker container ls

# CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                  NAMES
# 9f21cb777058        fhsinchy/hello-dock   "/docker-entrypoint."   5 seconds ago       Up 5 seconds        0.0.0.0:8080->80/tcp   gifted_sammet
```

Un conteneur nommé `gifted_sammet` est en cours d'exécution. Il a été créé `il y a 5 secondes` et le statut est `Up 5 seconds`, ce qui indique que le conteneur fonctionne correctement depuis sa création.

Le `CONTAINER ID` est `9f21cb777058` qui est les 12 premiers caractères de l'ID complet du conteneur. L'ID complet du conteneur est `9f21cb77705810797c4b847dbd330d9c732ffddba14fb435470567a7a3f46cdc` qui fait 64 caractères de long. Cet ID complet du conteneur a été imprimé comme résultat de la commande `docker container run` dans la section précédente.

Listé sous la colonne `PORTS`, le port 8080 de votre réseau local pointe vers le port 80 à l'intérieur du conteneur. Le nom `gifted_sammet` est généré par Docker et peut être quelque chose de complètement différent sur votre ordinateur.

La commande `container ls` ne liste que les conteneurs qui sont actuellement en cours d'exécution sur votre système. Afin de lister les conteneurs qui ont été exécutés dans le passé, vous pouvez utiliser l'option `--all` ou `-a`.

```
docker container ls --all

# CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS                     PORTS                  NAMES
# 9f21cb777058        fhsinchy/hello-dock   "/docker-entrypoint."   2 minutes ago       Up 2 minutes               0.0.0.0:8080->80/tcp   gifted_sammet
# 6cf52771dde1        fhsinchy/hello-dock   "/docker-entrypoint."   3 minutes ago       Exited (0) 3 minutes ago                          reverent_torvalds
# 128ec8ceab71        hello-world           "/hello"                 4 minutes ago       Exited (0) 4 minutes ago                          exciting_chebyshev
```

Comme vous pouvez le voir, le deuxième conteneur de la liste `reverent_torvalds` a été créé plus tôt et a quitté avec le code de statut 0, ce qui indique qu'aucune erreur n'a été produite pendant l'exécution du conteneur.

### Comment nommer ou renommer un conteneur

Par défaut, chaque conteneur a deux identifiants. Ils sont les suivants :

* `CONTAINER ID` - une chaîne aléatoire de 64 caractères.
* `NAME` - combinaison de deux mots aléatoires, joints par un trait de soulignement.

Faire référence à un conteneur basé sur ces deux identifiants aléatoires est un peu gênant. Ce serait bien si les conteneurs pouvaient être référencés en utilisant un nom défini par vous.

Le fait de nommer un conteneur peut être réalisé en utilisant l'option `--name`. Pour exécuter un autre conteneur en utilisant l'image `fhsinchy/hello-dock` avec le nom `hello-dock-container`, vous pouvez exécuter la commande suivante :

```
docker container run --detach --publish 8888:80 --name hello-dock-container fhsinchy/hello-dock

# b1db06e400c4c5e81a93a64d30acc1bf821bed63af36cab5cdb95d25e114f5fb
```

Le port 8080 sur le réseau local est occupé par le conteneur `gifted_sammet` (le conteneur créé dans la sous-section précédente). C'est pourquoi vous devrez utiliser un numéro de port différent, comme 8888. Maintenant, pour vérifier, exécutez la commande `container ls` :

```
docker container ls

# CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                  NAMES
# b1db06e400c4        fhsinchy/hello-dock   "/docker-entrypoint."   28 seconds ago      Up 26 seconds       0.0.0.0:8888->80/tcp   hello-dock-container
# 9f21cb777058        fhsinchy/hello-dock   "/docker-entrypoint."   4 minutes ago       Up 4 minutes        0.0.0.0:8080->80/tcp   gifted_sammet
```

Un nouveau conteneur avec le nom `hello-dock-container` a été démarré.

Vous pouvez même renommer les anciens conteneurs en utilisant la commande `container rename`. La syntaxe de la commande est la suivante :

```
docker container rename <identifiant du conteneur> <nouveau nom>
```

Pour renommer le conteneur `gifted_sammet` en `hello-dock-container-2`, exécutez la commande suivante :

```
docker container rename gifted_sammet hello-dock-container-2
```

La commande ne produit aucune sortie, mais vous pouvez vérifier que les changements ont eu lieu en utilisant la commande `container ls`. La commande `rename` fonctionne pour les conteneurs à la fois en état d'exécution et à l'état arrêté.

### Comment arrêter ou tuer un conteneur en cours d'exécution

Les conteneurs s'exécutant au premier plan peuvent être arrêtés en fermant simplement la fenêtre du terminal ou en appuyant sur `ctrl + c`. Les conteneurs s'exécutant en arrière-plan, cependant, ne peuvent pas être arrêtés de la même manière.

Il existe deux commandes qui traitent de cette tâche. La première est la commande `container stop`. La syntaxe générique de la commande est la suivante :

```
docker container stop <identifiant du conteneur>
```

Où `identifiant du conteneur` peut être soit l'ID soit le nom du conteneur.

J'espère que vous vous souvenez du conteneur que vous avez démarré dans la section précédente. Il est toujours en cours d'exécution en arrière-plan. Obtenez l'identifiant de ce conteneur en utilisant `docker container ls` (j'utiliserai le conteneur `hello-dock-container` pour cette démonstration). Maintenant, exécutez la commande suivante pour arrêter le conteneur :

```
docker container stop hello-dock-container

# hello-dock-container
```

Si vous utilisez le nom comme identifiant, vous obtiendrez le nom renvoyé comme sortie. La commande `stop` arrête un conteneur de manière élégante en envoyant un signal `SIGTERM`. Si le conteneur ne s'arrête pas dans un certain délai, un signal `SIGKILL` est envoyé, ce qui arrête immédiatement le conteneur.

Dans les cas où vous souhaitez envoyer un signal `SIGKILL` au lieu d'un signal `SIGTERM`, vous pouvez utiliser la commande `container kill` à la place. La commande `container kill` suit la même syntaxe que la commande `stop`.

```
docker container kill hello-dock-container-2

# hello-dock-container-2
```

### Comment redémarrer un conteneur

Lorsque je dis redémarrer, je veux dire deux scénarios spécifiques. Ils sont les suivants :

* Redémarrer un conteneur qui a été précédemment arrêté ou tué.
* Redémarrer un conteneur en cours d'exécution.

Comme vous l'avez déjà appris dans une sous-section précédente, les conteneurs arrêtés restent dans votre système. Si vous le souhaitez, vous pouvez les redémarrer. La commande `container start` peut être utilisée pour démarrer n'importe quel conteneur arrêté ou tué. La syntaxe de la commande est la suivante :

```
docker container start <identifiant du conteneur>
```

Vous pouvez obtenir la liste de tous les conteneurs en exécutant la commande `container ls --all`. Ensuite, recherchez les conteneurs avec le statut `Exited`.

```
docker container ls --all

# CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS                        PORTS               NAMES
# b1db06e400c4        fhsinchy/hello-dock   "/docker-entrypoint."   3 minutes ago       Exited (0) 47 seconds ago                         hello-dock-container
# 9f21cb777058        fhsinchy/hello-dock   "/docker-entrypoint."   7 minutes ago       Exited (137) 17 seconds ago                       hello-dock-container-2
# 6cf52771dde1        fhsinchy/hello-dock   "/docker-entrypoint."   7 minutes ago       Exited (0) 7 minutes ago                          reverent_torvalds
# 128ec8ceab71        hello-world           "/hello"                 9 minutes ago       Exited (0) 9 minutes ago                          exciting_chebyshev
```

Maintenant, pour redémarrer le conteneur `hello-dock-container`, vous pouvez exécuter la commande suivante :

```
docker container start hello-dock-container

# hello-dock-container
```

Maintenant, vous pouvez vous assurer que le conteneur est en cours d'exécution en regardant la liste des conteneurs en cours d'exécution en utilisant la commande `container ls`.

La commande `container start` démarre tout conteneur en mode détaché par défaut et conserve toute configuration de port effectuée précédemment. Donc si vous visitez `http://127.0.0.1:8080` maintenant, vous devriez pouvoir accéder à l'application `hello-dock` comme avant.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/hello-dock.png)

Maintenant, dans les scénarios où vous souhaitez redémarrer un conteneur en cours d'exécution, vous pouvez utiliser la commande `container restart`. La commande `container restart` suit la syntaxe exacte de la commande `container start`.

```
docker container restart hello-dock-container-2

# hello-dock-container-2
```

La principale différence entre les deux commandes est que la commande `container restart` tente d'arrêter le conteneur cible puis le redémarre, alors que la commande start démarre simplement un conteneur déjà arrêté.

Dans le cas d'un conteneur arrêté, les deux commandes sont exactement les mêmes. Mais dans le cas d'un conteneur en cours d'exécution, vous devez utiliser la commande `container restart`.

### Comment créer un conteneur sans l'exécuter

Jusqu'à présent dans cette section, vous avez démarré des conteneurs en utilisant la commande `container run` qui est en réalité une combinaison de deux commandes séparées. Ces commandes sont les suivantes :

* La commande `container create` crée un conteneur à partir d'une image donnée.
* La commande `container start` démarre un conteneur qui a déjà été créé.

Maintenant, pour effectuer la démonstration montrée dans la section "Comment exécuter un conteneur" en utilisant ces deux commandes, vous pouvez faire quelque chose comme ce qui suit :

```
docker container create --publish 8080:80 fhsinchy/hello-dock

# 2e7ef5098bab92f4536eb9a372d9b99ed852a9a816c341127399f51a6d053856

docker container ls --all

# CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS               NAMES
# 2e7ef5098bab        fhsinchy/hello-dock   "/docker-entrypoint."   30 seconds ago      Created                                 hello-dock
```

Comme le montre la sortie de la commande `container ls --all`, un conteneur nommé `hello-dock` a été créé en utilisant l'image `fhsinchy/hello-dock`. Le `STATUS` du conteneur est `Created` pour le moment, et, étant donné qu'il ne s'exécute pas, il ne sera pas listé sans l'utilisation de l'option `--all`.

Une fois le conteneur créé, il peut être démarré en utilisant la commande `container start`.

```
docker container start hello-dock

# hello-dock

docker container ls

# CONTAINER ID        IMAGE                 COMMAND                  CREATED              STATUS              PORTS                  NAMES
# 2e7ef5098bab        fhsinchy/hello-dock   "/docker-entrypoint."   About a minute ago   Up 29 seconds       0.0.0.0:8080->80/tcp   hello-dock
```

Le `STATUS` du conteneur est passé de `Created` à `Up 29 seconds`, ce qui indique que le conteneur est maintenant en état d'exécution. La configuration du port a également été affichée dans la colonne `PORTS`, qui était précédemment vide.

Bien que vous puissiez vous en sortir avec la commande `container run` pour la majorité des scénarios, il y aura certaines situations plus tard dans le livre qui nécessiteront l'utilisation de cette commande `container create`.

### Comment supprimer les conteneurs suspendus

Comme vous l'avez déjà vu, les conteneurs qui ont été arrêtés ou tués restent dans le système. Ces conteneurs suspendus peuvent prendre de la place ou entrer en conflit avec de nouveaux conteneurs.

Afin de supprimer un conteneur arrêté, vous pouvez utiliser la commande `container rm`. La syntaxe générique est la suivante :

```
docker container rm <identifiant du conteneur>
```

Pour savoir quels conteneurs ne sont pas en cours d'exécution, utilisez la commande `container ls --all` et recherchez les conteneurs avec le statut `Exited`.

```
docker container ls --all

# CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS                      PORTS                  NAMES
# b1db06e400c4        fhsinchy/hello-dock   "/docker-entrypoint."   6 minutes ago       Up About a minute           0.0.0.0:8888->80/tcp   hello-dock-container
# 9f21cb777058        fhsinchy/hello-dock   "/docker-entrypoint."   10 minutes ago      Up About a minute           0.0.0.0:8080->80/tcp   hello-dock-container-2
# 6cf52771dde1        fhsinchy/hello-dock   "/docker-entrypoint."   10 minutes ago      Exited (0) 10 minutes ago                          reverent_torvalds
# 128ec8ceab71        hello-world           "/hello"                 12 minutes ago      Exited (0) 12 minutes ago                          exciting_chebyshev
```

Comme on peut le voir dans la sortie, les conteneurs avec l'ID `6cf52771dde1` et `128ec8ceab71` ne sont pas en cours d'exécution. Pour supprimer le `6cf52771dde1`, vous pouvez exécuter la commande suivante :

```
docker container rm 6cf52771dde1

# 6cf52771dde1
```

Vous pouvez vérifier si le conteneur a été supprimé ou non en utilisant la commande `container ls`. Vous pouvez également supprimer plusieurs conteneurs à la fois en passant leurs identifiants les uns après les autres, séparés par des espaces.

Ou, au lieu de supprimer des conteneurs individuels, si vous souhaitez supprimer tous les conteneurs suspendus en une seule fois, vous pouvez utiliser la commande `container prune`.

Vous pouvez vérifier la liste des conteneurs en utilisant la commande `container ls --all` pour vous assurer que les conteneurs suspendus ont été supprimés :

```
docker container ls --all

# CONTAINER ID        IMAGE                 COMMAND                  CREATED             STATUS              PORTS                  NAMES
# b1db06e400c4        fhsinchy/hello-dock   "/docker-entrypoint."   8 minutes ago       Up 3 minutes        0.0.0.0:8888->80/tcp   hello-dock-container
# 9f21cb777058        fhsinchy/hello-dock   "/docker-entrypoint."   12 minutes ago      Up 3 minutes        0.0.0.0:8080->80/tcp   hello-dock-container-2
```

Si vous suivez le livre exactement comme écrit jusqu'à présent, vous devriez seulement voir `hello-dock-container` et `hello-dock-container-2` dans la liste. Je vous suggère d'arrêter et de supprimer les deux conteneurs avant de passer à la section suivante.

Il y a aussi l'option `--rm` pour les commandes `container run` et `container start` qui indique que vous voulez que les conteneurs soient supprimés dès qu'ils sont arrêtés. Pour démarrer un autre conteneur `hello-dock` avec l'option `--rm`, exécutez la commande suivante :

```
docker container run --rm --detach --publish 8888:80 --name hello-dock-volatile fhsinchy/hello-dock

# 0d74e14091dc6262732bee226d95702c21894678efb4043663f7911c53fb79f3
```

Vous pouvez utiliser la commande `container ls` pour vérifier que le conteneur est en cours d'exécution :

```
docker container ls

# CONTAINER ID   IMAGE                 COMMAND                  CREATED              STATUS              PORTS                  NAMES
# 0d74e14091dc   fhsinchy/hello-dock   "/docker-entrypoint."   About a minute ago   Up About a minute   0.0.0.0:8888->80/tcp   hello-dock-volatile
```

Maintenant, si vous arrêtez le conteneur et vérifiez à nouveau avec la commande `container ls --all` :

```
docker container stop hello-dock-volatile

# hello-dock-volatile

docker container ls --all

# CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

Le conteneur a été supprimé automatiquement. À partir de maintenant, j'utiliserai l'option `--rm` pour la plupart des conteneurs. Je mentionnerai explicitement où elle n'est pas nécessaire.

### Comment exécuter un conteneur en mode interactif

Jusqu'à présent, vous n'avez exécuté que des conteneurs créés à partir de l'image [hello-world](https://hub.docker.com/_/hello-world) ou de l'image [fhsinchy/hello-dock](https://hub.docker.com/r/fhsinchy/hello-dock). Ces images sont conçues pour exécuter des programmes simples qui ne sont pas interactifs.

Eh bien, toutes les images ne sont pas aussi simples. Les images peuvent encapsuler une distribution Linux entière.

Les distributions populaires telles que [Ubuntu](https://ubuntu.com/), [Fedora](https://fedora.org/), et [Debian](https://debian.org/) ont toutes des images Docker officielles disponibles dans le hub. Les langages de programmation tels que [python](https://hub.docker.com/_/python), [php](https://hub.docker.com/_/php), [go](https://hub.docker.com/_/golang) ou les environnements d'exécution comme [node](https://hub.docker.com/_/node) et [deno](https://hub.docker.com/r/hayd/deno) ont tous leurs images officielles.

Ces images ne se contentent pas d'exécuter un programme préconfiguré. Elles sont plutôt configurées pour exécuter un shell par défaut. Dans le cas des images de système d'exploitation, il peut s'agir de quelque chose comme `sh` ou `bash`, et dans le cas des langages de programmation ou des environnements d'exécution, il s'agit généralement de leur shell de langage par défaut.

Comme vous l'avez peut-être déjà appris de vos expériences précédentes avec les ordinateurs, les shells sont des programmes interactifs. Une image configurée pour exécuter un tel programme est une image interactive. Ces images nécessitent une option spéciale `-it` à passer dans la commande `container run`.

Par exemple, si vous exécutez un conteneur en utilisant l'image `ubuntu` en exécutant `docker container run ubuntu`, vous verrez que rien ne se passe. Mais si vous exécutez la même commande avec l'option `-it`, vous devriez atterrir directement sur bash à l'intérieur du conteneur Ubuntu.

```
docker container run --rm -it ubuntu

# root@dbb1f56b9563:/# cat /etc/os-release
# NAME="Ubuntu"
# VERSION="20.04.1 LTS (Focal Fossa)"
# ID=ubuntu
# ID_LIKE=debian
# PRETTY_NAME="Ubuntu 20.04.1 LTS"
# VERSION_ID="20.04"
# HOME_URL="https://www.ubuntu.com/"
# SUPPORT_URL="https://help.ubuntu.com/"
# BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
# PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
# VERSION_CODENAME=focal
# UBUNTU_CODENAME=focal
```

Comme vous pouvez le voir à partir de la sortie de la commande `cat /etc/os-release`, je suis effectivement en interaction avec le bash s'exécutant à l'intérieur du conteneur Ubuntu.

L'option `-it` prépare le terrain pour que vous puissiez interagir avec tout programme interactif à l'intérieur d'un conteneur. Cette option est en fait deux options séparées combinées.

* L'option `-i` ou `--interactive` vous connecte au flux d'entrée du conteneur, afin que vous puissiez envoyer des entrées à bash.
* L'option `-t` ou `--tty` garantit que vous obtenez un bon formatage et une expérience de type terminal natif en allouant un pseudo-tty.

Vous devez utiliser l'option `-it` chaque fois que vous souhaitez exécuter un conteneur en mode interactif. Un autre exemple peut être l'exécution de l'image `node` comme suit :

```
docker container run -it node

# Welcome to Node.js v15.0.0.
# Type ".help" for more information.
# > ['farhan', 'hasin', 'chowdhury'].map(name => name.toUpperCase())
# [ 'FARHAN', 'HASIN', 'CHOWDHURY' ]
```

Tout code JavaScript valide peut être exécuté dans le shell node. Au lieu d'écrire `-it`, vous pouvez être plus verbeux en écrivant `--interactive --tty` séparément.

### Comment exécuter des commandes à l'intérieur d'un conteneur

Dans la section [Hello World dans Docker](https://www.freecodecamp.org/news/@fhsinchy/s/the-docker-handbook/~/drafts/-MS1b3opwENd_9qH1jTO/hello-world-in-docker) de ce livre, vous m'avez vu exécuter une commande à l'intérieur d'un conteneur Alpine Linux. Cela s'est passé comme suit :

```
docker run alpine uname -a
# Linux f08dbbe9199b 5.8.0-22-generic #23-Ubuntu SMP Fri Oct 9 00:34:40 UTC 2020 x86_64 Linux
```

Dans cette commande, j'ai exécuté la commande `uname -a` à l'intérieur d'un conteneur Alpine Linux. Des scénarios comme celui-ci (où tout ce que vous voulez faire est d'exécuter une certaine commande à l'intérieur d'un certain conteneur) sont assez courants.

Supposons que vous souhaitez encoder une chaîne en utilisant le programme `base64`. C'est quelque chose qui est disponible dans presque tous les systèmes d'exploitation basés sur Linux ou Unix (mais pas sur Windows).

Dans cette situation, vous pouvez rapidement lancer un conteneur en utilisant des images comme [busybox](https://hub.docker.com/_/busybox) et le laisser faire le travail.

La syntaxe générique pour encoder une chaîne en utilisant `base64` est la suivante :

```
echo -n my-secret | base64

# bXktc2VjcmV0
```

Et la syntaxe générique pour passer une commande à un conteneur qui n'est pas en cours d'exécution est la suivante :

```
docker container run <nom de l'image> <commande>
```

Pour effectuer l'encodage base64 en utilisant l'image busybox, vous pouvez exécuter la commande suivante :

```
docker container run --rm busybox sh -c "echo -n my-secret | base64

# bXktc2VjcmV0
```

Ce qui se passe ici, c'est que dans une commande `container run`, tout ce que vous passez après le nom de l'image est transmis au point d'entrée par défaut de l'image.

Un point d'entrée est comme une passerelle vers l'image. La plupart des images, à l'exception des images exécutables (expliquées dans la sous-section [Travailler avec des images exécutables](https://www.freecodecamp.org/news/@fhsinchy/s/the-docker-handbook/~/drafts/-MS1b3opwENd_9qH1jTO/container-manipulation-basics#working-with-executable-images)), utilisent le shell ou `sh` comme point d'entrée par défaut. Ainsi, toute commande shell valide peut leur être passée comme arguments.

### Comment travailler avec des images exécutables

Dans la section précédente, j'ai brièvement mentionné les images exécutables. Ces images sont conçues pour se comporter comme des programmes exécutables.

Prenons par exemple mon projet [rmbyext](https://github.com/fhsinchy/rmbyext). Il s'agit d'un simple script Python capable de supprimer récursivement des fichiers d'extensions données. Pour en savoir plus sur le projet, vous pouvez consulter le dépôt :

%[https://github.com/fhsinchy/rmbyext]

Si vous avez à la fois Git et Python installés, vous pouvez installer ce script en exécutant la commande suivante :

```
pip install git+https://github.com/fhsinchy/rmbyext.git#egg=rmbyext
```

En supposant que Python a été correctement configuré sur votre système, le script devrait être disponible partout via le terminal. La syntaxe générique pour utiliser ce script est la suivante :

```
rmbyext <extension de fichier>
```

Pour le tester, ouvrez votre terminal dans un répertoire vide et créez quelques fichiers avec différentes extensions. Vous pouvez utiliser la commande `touch` pour ce faire. Maintenant, j'ai un répertoire sur mon ordinateur avec les fichiers suivants :

```
touch a.pdf b.pdf c.txt d.pdf e.txt

ls

# a.pdf  b.pdf  c.txt  d.pdf  e.txt
```

Pour supprimer tous les fichiers `pdf` de ce répertoire, vous pouvez exécuter la commande suivante :

```
rmbyext pdf

# Removing: PDF
# b.pdf
# a.pdf
# d.pdf
```

Une image exécutable pour ce programme devrait être capable de prendre des extensions de fichiers comme arguments et de les supprimer comme le programme `rmbyext` l'a fait.

L'image [fhsinchy/rmbyext](https://hub.docker.com/r/fhsinchy/rmbyext) se comporte de manière similaire. Cette image contient une copie du script `rmbyext` et est configurée pour exécuter le script sur un répertoire `/zone` à l'intérieur du conteneur.

Maintenant, le problème est que les conteneurs sont isolés de votre système local, donc le programme `rmbyext` s'exécutant à l'intérieur du conteneur n'a aucun accès à votre système de fichiers local. Donc, si d'une manière ou d'une autre vous pouvez mapper le répertoire local contenant les fichiers `pdf` au répertoire `/zone` à l'intérieur du conteneur, les fichiers devraient être accessibles au conteneur.

Une façon de donner à un conteneur un accès direct à votre système de fichiers local est d'utiliser des [montages de liaison](https://docs.docker.com/storage/bind-mounts/).

Un montage de liaison vous permet de former une liaison de données bidirectionnelle entre le contenu d'un répertoire du système de fichiers local (source) et un autre répertoire à l'intérieur d'un conteneur (destination). De cette manière, toute modification apportée dans le répertoire de destination aura un effet sur le répertoire source et vice versa.

Voyons un montage de liaison en action. Pour supprimer des fichiers en utilisant cette image au lieu du programme lui-même, vous pouvez exécuter la commande suivante :

```
docker container run --rm -v $(pwd):/zone fhsinchy/rmbyext pdf

# Removing: PDF
# b.pdf
# a.pdf
# d.pdf
```

Comme vous l'avez peut-être déjà deviné en voyant la partie `-v $(pwd):/zone` dans la commande, l'option `-v` ou `--volume` est utilisée pour créer un montage de liaison pour un conteneur. Cette option peut prendre trois champs séparés par des deux-points (`:`). La syntaxe générique de l'option est la suivante :

```
--volume <chemin absolu du répertoire du système de fichiers local>:<chemin absolu du répertoire du système de fichiers du conteneur>:<accès en lecture-écriture>
```

Le troisième champ est facultatif, mais vous devez passer le chemin absolu de votre répertoire local et le chemin absolu du répertoire à l'intérieur du conteneur.

Le répertoire source dans mon cas est `/home/fhsinchy/the-zone`. Étant donné que mon terminal est ouvert à l'intérieur du répertoire, `$(pwd)` sera remplacé par `/home/fhsinchy/the-zone` qui contient les fichiers `.pdf` et `.txt` mentionnés précédemment.

Vous pouvez en savoir plus sur la [substitution de commande ici](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html) si vous le souhaitez.

L'option `--volume` ou `-v` est valable pour les commandes `container run` ainsi que pour les commandes `container create`. Nous explorerons les volumes plus en détail dans les sections à venir, donc ne vous inquiétez pas si vous ne les avez pas très bien compris ici.

La différence entre une image régulière et une image exécutable est que le point d'entrée d'une image exécutable est défini sur un programme personnalisé au lieu de `sh`, dans ce cas, le programme `rmbyext`. Et comme vous l'avez appris dans la sous-section précédente, tout ce que vous écrivez après le nom de l'image dans une commande `container run` est passé au point d'entrée de l'image.

Ainsi, à la fin, la commande `docker container run --rm -v $(pwd):/zone fhsinchy/rmbyext pdf` se traduit par `rmbyext pdf` à l'intérieur du conteneur. Les images exécutables ne sont pas si courantes dans la nature, mais peuvent être très utiles dans certains cas.

## Bases de la manipulation des images Docker

Maintenant que vous avez une solide compréhension de l'exécution des conteneurs en utilisant des images publiquement disponibles, il est temps pour vous d'apprendre à créer vos propres images.

Dans cette section, vous apprendrez les bases de la création d'images, de l'exécution de conteneurs en les utilisant, et de leur partage en ligne.

Je vous suggère d'installer [Visual Studio Code](https://code.visualstudio.com/) avec l'extension officielle [Docker Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) depuis le marketplace. Cela améliorera grandement votre expérience de développement.

### Comment créer une image Docker

Comme je l'ai déjà expliqué dans la section [Hello World dans Docker](#image), les images sont des fichiers autonomes à plusieurs couches qui servent de modèle pour la création de conteneurs Docker. Elles sont comme une copie gelée et en lecture seule d'un conteneur.

Afin de créer une image en utilisant l'un de vos programmes, vous devez avoir une vision claire de ce que vous voulez de l'image. Prenez l'image officielle [nginx](https://hub.docker.com/_/nginx), par exemple. Vous pouvez démarrer un conteneur en utilisant cette image simplement en exécutant la commande suivante :

```
docker container run --rm --detach --name default-nginx --publish 8080:80 nginx

# b379ecd5b6b9ae27c144e4fa12bdc5d0635543666f75c14039eea8d5f38e3f56

docker container ls

# CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
# b379ecd5b6b9        nginx               "/docker-entrypoint."   8 seconds ago       Up 8 seconds        0.0.0.0:8080->80/tcp   default-nginx
```

Maintenant, si vous visitez `http://127.0.0.1:8080` dans le navigateur, vous verrez une page de réponse par défaut.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/nginx-default.png)

C'est bien et bon, mais que faire si vous voulez créer une image NGINX personnalisée qui fonctionne exactement comme l'officielle, mais qui est construite par vous ? C'est un scénario complètement valide, à vrai dire. En fait, faisons cela.

Afin de créer une image NGINX personnalisée, vous devez avoir une image claire de l'état final de l'image. À mon avis, l'image devrait être comme suit :

* L'image doit avoir NGINX préinstallé, ce qui peut être fait en utilisant un gestionnaire de paquets ou peut être construit à partir de la source.
* L'image doit démarrer NGINX automatiquement lors de l'exécution.

C'est simple. Si vous avez cloné le dépôt du projet lié dans ce livre, allez à l'intérieur de la racine du projet et cherchez un répertoire nommé `custom-nginx`.

Maintenant, créez un nouveau fichier nommé `Dockerfile` à l'intérieur de ce répertoire. Un `Dockerfile` est une collection d'instructions qui, une fois traitées par le démon, résultent en une image. Le contenu du `Dockerfile` est le suivant :

```dockerfile
FROM ubuntu:latest

EXPOSE 80

RUN apt-get update && \
    apt-get install nginx -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["nginx", "-g", "daemon off;"]
```

Les images sont des fichiers à plusieurs couches et dans ce fichier, chaque ligne (appelée instructions) que vous avez écrite crée une couche pour votre image.

* Chaque `Dockerfile` valide commence par une instruction `FROM`. Cette instruction définit l'image de base pour votre image résultante. En définissant `ubuntu:latest` comme image de base ici, vous obtenez toutes les fonctionnalités d'Ubuntu déjà disponibles dans votre image personnalisée, afin que vous puissiez utiliser des choses comme la commande `apt-get` pour une installation facile des paquets.
* L'instruction `EXPOSE` est utilisée pour indiquer le port qui doit être publié. L'utilisation de cette instruction ne signifie pas que vous n'aurez pas besoin de `--publish` le port. Vous devrez toujours utiliser l'option `--publish` explicitement. Cette instruction `EXPOSE` fonctionne comme une documentation pour quelqu'un qui essaie d'exécuter un conteneur en utilisant votre image. Elle a également d'autres utilisations que je ne discuterai pas ici.
* L'instruction `RUN` dans un `Dockerfile` exécute une commande à l'intérieur du shell du conteneur. La commande `apt-get update && apt-get install nginx -y` vérifie les versions mises à jour des paquets et installe NGINX. La commande `apt-get clean && rm -rf /var/lib/apt/lists/*` est utilisée pour effacer le cache des paquets car vous ne voulez pas de bagages inutiles dans votre image. Ces deux commandes sont des trucs Ubuntu simples, rien de fantaisiste. Les instructions `RUN` ici sont écrites sous forme `shell`. Elles peuvent également être écrites sous forme `exec`. Vous pouvez consulter la [référence officielle](https://docs.docker.com/engine/reference/builder/#run) pour plus d'informations.
* Enfin, l'instruction `CMD` définit la commande par défaut pour votre image. Cette instruction est écrite sous forme `exec` ici, composée de trois parties distinctes. Ici, `nginx` fait référence à l'exécutable NGINX. Les options `-g` et `daemon off` sont des options pour NGINX. L'exécution de NGINX en tant que processus unique à l'intérieur des conteneurs est considérée comme une meilleure pratique, d'où l'utilisation de cette option. L'instruction `CMD` peut également être écrite sous forme `shell`. Vous pouvez consulter la [référence officielle](https://docs.docker.com/engine/reference/builder/#cmd) pour plus d'informations.

Maintenant que vous avez un `Dockerfile` valide, vous pouvez construire une image à partir de celui-ci. Tout comme les commandes liées aux conteneurs, les commandes liées aux images peuvent être émises en utilisant la syntaxe suivante :

```
docker image <commande> <options>
```

Pour construire une image en utilisant le `Dockerfile` que vous venez d'écrire, ouvrez votre terminal à l'intérieur du répertoire `custom-nginx` et exécutez la commande suivante :

```
docker image build .

# Sending build context to Docker daemon  3.584kB
# Step 1/4 : FROM ubuntu:latest
#  ---> d70eaf7277ea
# Step 2/4 : EXPOSE 80
#  ---> Running in 9eae86582ec7
# Removing intermediate container 9eae86582ec7
#  ---> 8235bd799a56
# Step 3/4 : RUN apt-get update &&     apt-get install nginx -y &&     apt-get clean && rm -rf /var/lib/apt/lists/*
#  ---> Running in a44725cbb3fa
### LONG INSTALLATION STUFF GOES HERE ###
# Removing intermediate container a44725cbb3fa
#  ---> 3066bd20292d
# Step 4/4 : CMD ["nginx", "-g", "daemon off;"]
#  ---> Running in 4792e4691660
# Removing intermediate container 4792e4691660
#  ---> 3199372aa3fc
# Successfully built 3199372aa3fc
```

Pour effectuer une construction d'image, le démon a besoin de deux informations très spécifiques. Il s'agit du nom du `Dockerfile` et du contexte de construction. Dans la commande émise ci-dessus :

* `docker image build` est la commande pour construire l'image. Le démon trouve tout fichier nommé `Dockerfile` dans le contexte.
* Le `.` à la fin définit le contexte pour cette construction. Le contexte signifie le répertoire accessible par le démon pendant le processus de construction.

Maintenant, pour exécuter un conteneur en utilisant cette image, vous pouvez utiliser la commande `container run` couplée avec l'ID de l'image que vous avez reçu comme résultat du processus de construction. Dans mon cas, l'ID est `3199372aa3fc`, comme en témoigne la ligne `Successfully built 3199372aa3fc` dans le bloc de code précédent.

```
docker container run --rm --detach --name custom-nginx-packaged --publish 8080:80 3199372aa3fc

# ec09d4e1f70c903c3b954c8d7958421cdd1ae3d079b57f929e44131fbf8069a0

docker container ls

# CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                  NAMES
# ec09d4e1f70c        3199372aa3fc        "nginx -g 'daemon of"   23 seconds ago      Up 22 seconds       0.0.0.0:8080->80/tcp   custom-nginx-packaged
```

Pour vérifier, visitez `http://127.0.0.1:8080` et vous devriez voir la page de réponse par défaut.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/nginx-default.png)

### Comment étiqueter les images Docker

Tout comme les conteneurs, vous pouvez attribuer des identifiants personnalisés à vos images au lieu de vous fier à l'ID généré aléatoirement. Dans le cas d'une image, on parle d'étiquetage plutôt que de nommage. L'option `--tag` ou `-t` est utilisée dans de tels cas.

La syntaxe générique de l'option est la suivante :

```
--tag <dépôt d'image>:<étiquette d'image>
```

Le dépôt est généralement connu sous le nom de nom de l'image et l'étiquette indique une certaine version ou build.

Prenons l'image officielle [mysql](https://hub.docker.com/_/mysql), par exemple. Si vous souhaitez exécuter un conteneur en utilisant une version spécifique de MySQL, comme 5.7, vous pouvez exécuter `docker container run mysql:5.7` où `mysql` est le dépôt de l'image et `5.7` est l'étiquette.

Afin d'étiqueter votre image NGINX personnalisée avec `custom-nginx:packaged`, vous pouvez exécuter la commande suivante :

```
docker image build --tag custom-nginx:packaged .

# Sending build context to Docker daemon  1.055MB
# Step 1/4 : FROM ubuntu:latest
#  ---> f63181f19b2f
# Step 2/4 : EXPOSE 80
#  ---> Running in 53ab370b9efc
# Removing intermediate container 53ab370b9efc
#  ---> 6d6460a74447
# Step 3/4 : RUN apt-get update &&     apt-get install nginx -y &&     apt-get clean && rm -rf /var/lib/apt/lists/*
#  ---> Running in b4951b6b48bb
### LONG INSTALLATION STUFF GOES HERE ###
# Removing intermediate container b4951b6b48bb
#  ---> fdc6cdd8925a
# Step 4/4 : CMD ["nginx", "-g", "daemon off;"]
#  ---> Running in 3bdbd2af4f0e
# Removing intermediate container 3bdbd2af4f0e
#  ---> f8837621b99d
# Successfully built f8837621b99d
# Successfully tagged custom-nginx:packaged
```

Rien ne changera sauf le fait que vous pouvez maintenant faire référence à votre image en tant que `custom-nginx:packaged` au lieu d'une longue chaîne aléatoire.

Dans les cas où vous avez oublié d'étiqueter une image pendant le build, ou peut-être que vous voulez changer l'étiquette, vous pouvez utiliser la commande `image tag` pour faire cela :

```
docker image tag <id de l'image> <dépôt de l'image>:<étiquette de l'image>

## ou ##

docker image tag <dépôt de l'image>:<étiquette de l'image> <nouveau dépôt de l'image>:<nouvelle étiquette de l'image>
```

### Comment lister et supprimer les images Docker

Tout comme la commande `container ls`, vous pouvez utiliser la commande `image ls` pour lister toutes les images de votre système local :

```
docker image ls

# REPOSITORY     TAG        IMAGE ID       CREATED         SIZE
# <none>         <none>     3199372aa3fc   7 seconds ago   132MB
# custom-nginx   packaged   f8837621b99d   4 minutes ago   132MB
```

Les images listées ici peuvent être supprimées en utilisant la commande `image rm`. La syntaxe générique est la suivante :

```
docker image rm <identifiant de l'image>
```

L'identifiant peut être l'ID de l'image ou le dépôt de l'image. Si vous utilisez le dépôt, vous devrez également identifier l'étiquette. Pour supprimer l'image `custom-nginx:packaged`, vous pouvez exécuter la commande suivante :

```
docker image rm custom-nginx:packaged

# Untagged: custom-nginx:packaged
# Deleted: sha256:f8837621b99d3388a9e78d9ce49fbb773017f770eea80470fb85e0052beae242
# Deleted: sha256:fdc6cdd8925ac25b9e0ed1c8539f96ad89ba1b21793d061e2349b62dd517dadf
# Deleted: sha256:c20e4aa46615fe512a4133089a5cd66f9b7da76366c96548790d5bf865bd49c4
# Deleted: sha256:6d6460a744475a357a2b631a4098aa1862d04510f3625feb316358536fcd8641
```

Vous pouvez également utiliser la commande `image prune` pour nettoyer toutes les images suspendues non étiquetées comme suit :

```
docker image prune --force

# Deleted Images:
# deleted: sha256:ba9558bdf2beda81b9acc652ce4931a85f0fc7f69dbc91b4efc4561ef7378aff
# deleted: sha256:ad9cc3ff27f0d192f8fa5fadebf813537e02e6ad472f6536847c4de183c02c81
# deleted: sha256:f1e9b82068d43c1bb04ff3e4f0085b9f8903a12b27196df7f1145aa9296c85e7
# deleted: sha256:ec16024aa036172544908ec4e5f842627d04ef99ee9b8d9aaa26b9c2a4b52baa

# Total reclaimed space: 59.19MB
```

L'option `--force` ou `-f` saute toute question de confirmation. Vous pouvez également utiliser l'option `--all` ou `-a` pour supprimer toutes les images mises en cache dans votre registre local.

### Comment comprendre les nombreuses couches d'une image Docker

Dès le début de ce livre, j'ai dit que les images sont des fichiers à plusieurs couches. Dans cette sous-section, je vais démontrer les différentes couches d'une image et comment elles jouent un rôle important dans le processus de construction de cette image.

Pour cette démonstration, j'utiliserai l'image `custom-nginx:packaged` de la sous-section précédente.

Pour visualiser les nombreuses couches d'une image, vous pouvez utiliser la commande `image history`. Les différentes couches de l'image `custom-nginx:packaged` peuvent être visualisées comme suit :

```
docker image history custom-nginx:packaged

# IMAGE               CREATED             CREATED BY                                      SIZE                COMMENT
# 7f16387f7307        5 minutes ago       /bin/sh -c #(nop)  CMD ["nginx" "-g" "daemon   0B                             
# 587c805fe8df        5 minutes ago       /bin/sh -c apt-get update &&     apt-get ins   60MB                
# 6fe4e51e35c1        6 minutes ago       /bin/sh -c #(nop)  EXPOSE 80                    0B                  
# d70eaf7277ea        17 hours ago        /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B                  
# <missing>           17 hours ago        /bin/sh -c mkdir -p /run/systemd && echo 'do   7B                  
# <missing>           17 hours ago        /bin/sh -c [ -z "$(apt-get indextargets)" ]     0B                  
# <missing>           17 hours ago        /bin/sh -c set -xe   && echo '#!/bin/sh' > /   811B                
# <missing>           17 hours ago        /bin/sh -c #(nop) ADD file:435d9776fdd3a1834   72.9MB
```

Il y a huit couches de cette image. La couche la plus haute est la plus récente et en descendant, les couches deviennent plus anciennes. La couche la plus haute est celle que vous utilisez généralement pour exécuter des conteneurs.

Maintenant, examinons de plus près les images en commençant par l'image `d70eaf7277ea` jusqu'à `7f16387f7307`. J'ignorerai les quatre couches du bas où l'`IMAGE` est `<missing>` car elles ne nous concernent pas.

* `d70eaf7277ea` a été créé par `/bin/sh -c #(nop)  CMD ["/bin/bash"]` ce qui indique que le shell par défaut à l'intérieur d'Ubuntu a été chargé avec succès.
* `6fe4e51e35c1` a été créé par `/bin/sh -c #(nop)  EXPOSE 80` qui était la deuxième instruction dans votre code.
* `587c805fe8df` a été créé par `/bin/sh -c apt-get update && apt-get install nginx -y && apt-get clean && rm -rf /var/lib/apt/lists/*` qui était la troisième instruction dans votre code. Vous pouvez également voir que cette image a une taille de `60MB` étant donné que tous les paquets nécessaires ont été installés pendant l'exécution de cette instruction.
* Enfin, la couche la plus haute `7f16387f7307` a été créée par `/bin/sh -c #(nop)  CMD ["nginx", "-g", "daemon off;"]` qui définit la commande par défaut pour cette image.

Comme vous pouvez le voir, l'image est composée de nombreuses couches en lecture seule, chacune enregistrant un nouvel ensemble de changements d'état déclenchés par certaines instructions. Lorsque vous démarrez un conteneur en utilisant une image, vous obtenez une nouvelle couche modifiable par-dessus les autres couches.

Ce phénomène de superposition qui se produit chaque fois que vous travaillez avec Docker a été rendu possible par un concept technique incroyable appelé système de fichiers union. Ici, union signifie union en théorie des ensembles. Selon [Wikipedia](https://en.wikipedia.org/wiki/UnionFS) -

> Il permet aux fichiers et répertoires de systèmes de fichiers séparés, connus sous le nom de branches, d'être superposés de manière transparente, formant un seul système de fichiers cohérent. Les contenus de répertoires qui ont le même chemin au sein des branches fusionnées seront vus ensemble dans un seul répertoire fusionné, au sein du nouveau système de fichiers virtuel.

En utilisant ce concept, Docker peut éviter la duplication de données et peut utiliser les couches précédemment créées comme cache pour les constructions ultérieures. Cela entraîne des images compactes et efficaces qui peuvent être utilisées partout.

### Comment construire NGINX à partir de la source

Dans la sous-section précédente, vous avez appris les instructions `FROM`, `EXPOSE`, `RUN` et `CMD`. Dans cette sous-section, vous apprendrez beaucoup plus sur d'autres instructions.

Dans cette sous-section, vous allez à nouveau créer une image NGINX personnalisée. Mais le twist est que vous allez construire NGINX à partir de la source au lieu de l'installer en utilisant un gestionnaire de paquets comme `apt-get` comme dans l'exemple précédent.

Pour construire NGINX à partir de la source, vous avez d'abord besoin de la source de NGINX. Si vous avez cloné mon dépôt de projets, vous verrez un fichier nommé `nginx-1.19.2.tar.gz` dans le répertoire `custom-nginx`. Vous utiliserez cette archive comme source pour construire NGINX.

Avant de plonger dans l'écriture de code, planifions d'abord le processus. Le processus de création d'image cette fois peut être fait en sept étapes. Elles sont les suivantes :

* Obtenez une bonne image de base pour construire l'application, comme [ubuntu](https://hub.docker.com/_/ubuntu).
* Installez les dépendances de construction nécessaires sur l'image de base.
* Copiez le fichier `nginx-1.19.2.tar.gz` à l'intérieur de l'image.
* Extrayez le contenu de l'archive et débarrassez-vous-en.
* Configurez la construction, compilez et installez le programme en utilisant l'outil `make`.
* Débarrassez-vous du code source extrait.
* Exécutez l'exécutable `nginx`.

Maintenant que vous avez un plan, commençons par ouvrir l'ancien `Dockerfile` et mettons à jour son contenu comme suit :

```
FROM ubuntu:latest

RUN apt-get update && \
    apt-get install build-essential\ 
                    libpcre3 \
                    libpcre3-dev \
                    zlib1g \
                    zlib1g-dev \
                    libssl1.1 \
                    libssl-dev \
                    -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY nginx-1.19.2.tar.gz .

RUN tar -xvf nginx-1.19.2.tar.gz && rm nginx-1.19.2.tar.gz

RUN cd nginx-1.19.2 && \
    ./configure \
        --sbin-path=/usr/bin/nginx \
        --conf-path=/etc/nginx/nginx.conf \
        --error-log-path=/var/log/nginx/error.log \
        --http-log-path=/var/log/nginx/access.log \
        --with-pcre \
        --pid-path=/var/run/nginx.pid \
        --with-http_ssl_module && \
    make && make install

RUN rm -rf /nginx-1.19.2

CMD ["nginx", "-g", "daemon off;"]
```

Comme vous pouvez le voir, le code à l'intérieur du `Dockerfile` reflète les sept étapes dont j'ai parlé ci-dessus.

* L'instruction `FROM` définit Ubuntu comme image de base, créant un environnement idéal pour construire n'importe quelle application.
* L'instruction `RUN` installe les packages standard nécessaires pour construire NGINX à partir de la source.
* L'instruction `COPY` ici est quelque chose de nouveau. Cette instruction est responsable de la copie du fichier `nginx-1.19.2.tar.gz` à l'intérieur de l'image. La syntaxe générique de l'instruction `COPY` est `COPY <source> <destination>` où la source est dans votre système de fichiers local et la destination est à l'intérieur de votre image. Le `.` comme destination signifie le répertoire de travail à l'intérieur de l'image qui est par défaut `/` sauf si défini autrement.
* La deuxième instruction `RUN` ici extrait le contenu de l'archive en utilisant `tar` et s'en débarrasse ensuite.
* Le fichier d'archive contient un répertoire appelé `nginx-1.19.2` contenant le code source. Donc à l'étape suivante, vous devrez `cd` à l'intérieur de ce répertoire et effectuer le processus de construction. Vous pouvez lire l'article [Comment installer un logiciel à partir du code source... et le supprimer ensuite](https://itsfoss.com/install-software-from-source-code/) pour en savoir plus sur le sujet.
* Une fois la construction et l'installation terminées, vous supprimez le répertoire `nginx-1.19.2` en utilisant la commande `rm`.
* À l'étape finale, vous démarrez NGINX en mode processus unique comme vous l'avez fait auparavant.

Maintenant, pour construire une image en utilisant ce code, exécutez la commande suivante :

```
docker image build --tag custom-nginx:built .

# Step 1/7 : FROM ubuntu:latest
#  ---> d70eaf7277ea
# Step 2/7 : RUN apt-get update &&     apt-get install build-essential                    libpcre3                     libpcre3-dev                     zlib1g                     zlib1g-dev                     libssl-dev                     -y &&     apt-get clean && rm -rf /var/lib/apt/lists/*
#  ---> Running in 2d0aa912ea47
### LONG INSTALLATION STUFF GOES HERE ###
# Removing intermediate container 2d0aa912ea47
#  ---> cbe1ced3da11
# Step 3/7 : COPY nginx-1.19.2.tar.gz .
#  ---> 7202902edf3f
# Step 4/7 : RUN tar -xvf nginx-1.19.2.tar.gz && rm nginx-1.19.2.tar.gz
 ---> Running in 4a4a95643020
### LONG EXTRACTION STUFF GOES HERE ###
# Removing intermediate container 4a4a95643020
#  ---> f9dec072d6d6
# Step 5/7 : RUN cd nginx-1.19.2 &&     ./configure         --sbin-path=/usr/bin/nginx         --conf-path=/etc/nginx/nginx.conf         --error-log-path=/var/log/nginx/error.log         --http-log-path=/var/log/nginx/access.log         --with-pcre         --pid-path=/var/run/nginx.pid         --with-http_ssl_module &&     make && make install
#  ---> Running in b07ba12f921e
### LONG CONFIGURATION AND BUILD STUFF GOES HERE ###
# Removing intermediate container b07ba12f921e
#  ---> 5a877edafd8b
# Step 6/7 : RUN rm -rf /nginx-1.19.2
#  ---> Running in 947e1d9ba828
# Removing intermediate container 947e1d9ba828
#  ---> a7702dc7abb7
# Step 7/7 : CMD ["nginx", "-g", "daemon off;"]
#  ---> Running in 3110c7fdbd57
# Removing intermediate container 3110c7fdbd57
#  ---> eae55f7369d3
# Successfully built eae55f7369d3
# Successfully tagged custom-nginx:built
```

Ce code est correct, mais il y a quelques endroits où nous pouvons apporter des améliorations.

* Au lieu de coder en dur le nom de fichier comme `nginx-1.19.2.tar.gz`, vous pouvez créer un argument en utilisant l'instruction `ARG`. De cette façon, vous pourrez changer la version ou le nom de fichier en changeant simplement l'argument.
* Au lieu de télécharger l'archive manuellement, vous pouvez laisser le démon télécharger le fichier pendant le processus de construction. Il existe une autre instruction comme `COPY` appelée l'instruction `ADD` qui est capable d'ajouter des fichiers depuis Internet.

Ouvrez le fichier `Dockerfile` et mettez à jour son contenu comme suit :

```dockerfile
FROM ubuntu:latest

RUN apt-get update && \
    apt-get install build-essential\ 
                    libpcre3 \
                    libpcre3-dev \
                    zlib1g \
                    zlib1g-dev \
                    libssl1.1 \
                    libssl-dev \
                    -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ARG FILENAME="nginx-1.19.2"
ARG EXTENSION="tar.gz"

ADD https://nginx.org/download/${FILENAME}.${EXTENSION} .

RUN tar -xvf ${FILENAME}.${EXTENSION} && rm ${FILENAME}.${EXTENSION}

RUN cd ${FILENAME} && \
    ./configure \
        --sbin-path=/usr/bin/nginx \
        --conf-path=/etc/nginx/nginx.conf \
        --error-log-path=/var/log/nginx/error.log \
        --http-log-path=/var/log/nginx/access.log \
        --with-pcre \
        --pid-path=/var/run/nginx.pid \
        --with-http_ssl_module && \
    make && make install && \
    cd / && rm -rfv /${FILENAME} && \
    apt-get remove build-essential \ 
                    libpcre3-dev \
                    zlib1g-dev \
                    libssl-dev \
                    -y && \
    apt-get autoremove -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["nginx", "-g", "daemon off;"]
```

Le code est presque identique au bloc de code précédent, à l'exception d'une nouvelle instruction appelée `ARG` aux lignes 13, 14 et de l'utilisation de l'instruction `ADD` à la ligne 16. L'explication du code mis à jour est la suivante :

* L'instruction `ARG` vous permet de déclarer des variables comme dans d'autres langages. Ces variables ou arguments peuvent ensuite être accessibles en utilisant la syntaxe `${nom de l'argument}`. Ici, j'ai mis le nom de fichier `nginx-1.19.2` et l'extension de fichier `tar.gz` dans deux arguments séparés. De cette façon, je peux passer d'une version à une autre de NGINX ou du format d'archive en apportant une modification à un seul endroit. Dans le code ci-dessus, j'ai ajouté des valeurs par défaut aux variables. Les valeurs des variables peuvent être passées en tant qu'options de la commande `image build`. Vous pouvez consulter la [référence officielle](https://docs.docker.com/engine/reference/builder/#arg) pour plus de détails.
* Dans l'instruction `ADD`, j'ai formé l'URL de téléchargement dynamiquement en utilisant les arguments déclarés ci-dessus. La ligne `https://nginx.org/download/${FILENAME}.${EXTENSION}` donnera quelque chose comme `https://nginx.org/download/nginx-1.19.2.tar.gz` pendant le processus de construction. Vous pouvez changer la version du fichier ou l'extension en la modifiant à un seul endroit grâce à l'instruction `ARG`.
* L'instruction `ADD` n'extrait pas les fichiers obtenus depuis Internet par défaut, d'où l'utilisation de `tar` à la ligne 18.

Le reste du code est presque inchangé. Vous devriez être capable de comprendre l'utilisation des arguments par vous-même maintenant. Enfin, essayons de construire une image à partir de ce code mis à jour.

```
docker image build --tag custom-nginx:built .

# Step 1/9 : FROM ubuntu:latest
#  ---> d70eaf7277ea
# Step 2/9 : RUN apt-get update &&     apt-get install build-essential                    libpcre3                     libpcre3-dev                     zlib1g                     zlib1g-dev                     libssl-dev                     -y &&     apt-get clean && rm -rf /var/lib/apt/lists/*
#  ---> cbe1ced3da11
### LONG INSTALLATION STUFF GOES HERE ###
# Step 3/9 : ARG FILENAME="nginx-1.19.2"
#  ---> Running in 33b62a0e9ffb
# Removing intermediate container 33b62a0e9ffb
#  ---> fafc0aceb9c8
# Step 4/9 : ARG EXTENSION="tar.gz"
#  ---> Running in 5c32eeb1bb11
# Removing intermediate container 5c32eeb1bb11
#  ---> 36efdf6efacc
# Step 5/9 : ADD https://nginx.org/download/${FILENAME}.${EXTENSION} .
# Downloading [==================================================>]  1.049MB/1.049MB
#  ---> dba252f8d609
# Step 6/9 : RUN tar -xvf ${FILENAME}.${EXTENSION} && rm ${FILENAME}.${EXTENSION}
#  ---> Running in 2f5b091b2125
### LONG EXTRACTION STUFF GOES HERE ###
# Removing intermediate container 2f5b091b2125
#  ---> 2c9a325d74f1
# Step 7/9 : RUN cd ${FILENAME} &&     ./configure         --sbin-path=/usr/bin/nginx         --conf-path=/etc/nginx/nginx.conf         --error-log-path=/var/log/nginx/error.log         --http-log-path=/var/log/nginx/access.log         --with-pcre         --pid-path=/var/run/nginx.pid         --with-http_ssl_module &&     make && make install
#  ---> Running in 11cc82dd5186
### LONG CONFIGURATION AND BUILD STUFF GOES HERE ###
# Removing intermediate container 11cc82dd5186
#  ---> 6c122e485ec8
# Step 8/9 : RUN rm -rf /${FILENAME}}
#  ---> Running in 04102366960b
# Removing intermediate container 04102366960b
#  ---> 6bfa35420a73
# Step 9/9 : CMD ["nginx", "-g", "daemon off;"]
#  ---> Running in 63ee44b571bb
# Removing intermediate container 63ee44b571bb
#  ---> 4ce79556db1b
# Successfully built 4ce79556db1b
# Successfully tagged custom-nginx:built
```

Maintenant, vous devriez être en mesure d'exécuter un conteneur en utilisant l'image `custom-nginx:built`.

```
docker container run --rm --detach --name custom-nginx-built --publish 8080:80 custom-nginx:built

# 90ccdbc0b598dddc4199451b2f30a942249d85a8ed21da3c8d14612f17eed0aa

docker container ls

# CONTAINER ID        IMAGE                COMMAND                  CREATED             STATUS              PORTS                  NAMES
# 90ccdbc0b598        custom-nginx:built   "nginx -g 'daemon of"   2 minutes ago       Up 2 minutes        0.0.0.0:8080->80/tcp   custom-nginx-built
```

Un conteneur utilisant l'image `custom-nginx:built-v2` a été exécuté avec succès. Le conteneur devrait être accessible à `http://127.0.0.1:8080` maintenant.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/nginx-default.png)

Et voici la page de réponse par défaut fiable de NGINX. Vous pouvez visiter le site de [référence officielle](https://docs.docker.com/engine/reference/builder/) pour en savoir plus sur les instructions disponibles.

### Comment optimiser les images Docker

L'image que nous avons construite dans la dernière sous-section est fonctionnelle mais très non optimisée. Pour prouver mon point, jetons un coup d'œil à la taille de l'image en utilisant la commande `image ls` :

```
docker image ls

# REPOSITORY         TAG       IMAGE ID       CREATED          SIZE
# custom-nginx       built     1f3aaf40bb54   16 minutes ago   343MB
```

Pour une image contenant uniquement NGINX, c'est trop. Si vous téléchargez l'image officielle et vérifiez sa taille, vous verrez à quel point elle est petite :

```
docker image pull nginx:stable

# stable: Pulling from library/nginx
# a076a628af6f: Pull complete 
# 45d7b5d3927d: Pull complete 
# 5e326fece82e: Pull complete 
# 30c386181b68: Pull complete 
# b15158e9ebbe: Pull complete 
# Digest: sha256:ebd0fd56eb30543a9195280eb81af2a9a8e6143496accd6a217c14b06acd1419
# Status: Downloaded newer image for nginx:stable
# docker.io/library/nginx:stable

docker image ls

# REPOSITORY         TAG       IMAGE ID       CREATED          SIZE
# custom-nginx       built     1f3aaf40bb54   25 minutes ago   343MB
# nginx              stable    b9e1dc12387a   11 days ago      133MB
```

Afin de trouver la cause profonde, jetons un coup d'œil au `Dockerfile` d'abord :

```dockerfile
FROM ubuntu:latest

RUN apt-get update && \
    apt-get install build-essential\ 
                    libpcre3 \
                    libpcre3-dev \
                    zlib1g \
                    zlib1g-dev \
                    libssl1.1 \
                    libssl-dev \
                    -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ARG FILENAME="nginx-1.19.2"
ARG EXTENSION="tar.gz"

ADD https://nginx.org/download/${FILENAME}.${EXTENSION} .

RUN tar -xvf ${FILENAME}.${EXTENSION} && rm ${FILENAME}.${EXTENSION}

RUN cd ${FILENAME} && \
    ./configure \
        --sbin-path=/usr/bin/nginx \
        --conf-path=/etc/nginx/nginx.conf \
        --error-log-path=/var/log/nginx/error.log \
        --http-log-path=/var/log/nginx/access.log \
        --with-pcre \
        --pid-path=/var/run/nginx.pid \
        --with-http_ssl_module && \
    make && make install

RUN rm -rf /${FILENAME}}

CMD ["nginx", "-g", "daemon off;"]
```

Comme vous pouvez le voir à la ligne 3, l'instruction `RUN` installe beaucoup de choses. Bien que ces packages soient nécessaires pour construire NGINX à partir de la source, ils ne sont pas nécessaires pour l'exécuter.

Sur les 6 packages que nous avons installés, seulement deux sont nécessaires pour exécuter NGINX. Il s'agit de `libpcre3` et `zlib1g`. Une meilleure idée serait donc de désinstaller les autres packages une fois le processus de construction terminé.

Pour ce faire, mettez à jour votre `Dockerfile` comme suit :

```dockerfile
FROM ubuntu:latest

EXPOSE 80

ARG FILENAME="nginx-1.19.2"
ARG EXTENSION="tar.gz"

ADD https://nginx.org/download/${FILENAME}.${EXTENSION} .

RUN apt-get update && \
    apt-get install build-essential \ 
                    libpcre3 \
                    libpcre3-dev \
                    zlib1g \
                    zlib1g-dev \
                    libssl1.1 \
                    libssl-dev \
                    -y && \
    tar -xvf ${FILENAME}.${EXTENSION} && rm ${FILENAME}.${EXTENSION} && \
    cd ${FILENAME} && \
    ./configure \
        --sbin-path=/usr/bin/nginx \
        --conf-path=/etc/nginx/nginx.conf \
        --error-log-path=/var/log/nginx/error.log \
        --http-log-path=/var/log/nginx/access.log \
        --with-pcre \
        --pid-path=/var/run/nginx.pid \
        --with-http_ssl_module && \
    make && make install && \
    cd / && rm -rfv /${FILENAME} && \
    apt-get remove build-essential \ 
                    libpcre3-dev \
                    zlib1g-dev \
                    libssl-dev \
                    -y && \
    apt-get autoremove -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

CMD ["nginx", "-g", "daemon off;"]
```

Comme vous pouvez le voir, à la ligne 10, une seule instruction `RUN` effectue tout le travail nécessaire. La chaîne exacte d'événements est la suivante :

* Des lignes 10 à 17, tous les packages nécessaires sont installés.
* À la ligne 18, le code source est extrait et l'archive téléchargée est supprimée.
* Des lignes 19 à 28, NGINX est configuré, construit et installé sur le système.
* À la ligne 29, les fichiers extraits de l'archive téléchargée sont supprimés.
* Des lignes 30 à 36, tous les packages inutiles sont désinstallés et le cache est effacé. Les packages `libpcre3` et `zlib1g` sont nécessaires pour exécuter NGINX, donc nous les conservons.

Vous pouvez demander pourquoi je fais autant de travail dans une seule instruction `RUN` au lieu de les diviser proprement en plusieurs instructions comme nous l'avons fait précédemment. Eh bien, les diviser serait une erreur.

Si vous installez des packages puis les supprimez dans des instructions `RUN` séparées, ils vivront dans des couches séparées de l'image. Bien que l'image finale n'aura pas les packages supprimés, leur taille sera toujours ajoutée à l'image finale puisqu'ils existent dans l'une des couches constituant l'image. Assurez-vous donc d'apporter ces types de modifications sur une seule couche.

Construisons une image en utilisant ce `Dockerfile` et voyons les différences.

```
docker image build --tag custom-nginx:built .

# Sending build context to Docker daemon  1.057MB
# Step 1/7 : FROM ubuntu:latest
#  ---> f63181f19b2f
# Step 2/7 : EXPOSE 80
#  ---> Running in 006f39b75964
# Removing intermediate container 006f39b75964
#  ---> 6943f7ef9376
# Step 3/7 : ARG FILENAME="nginx-1.19.2"
#  ---> Running in ffaf89078594
# Removing intermediate container ffaf89078594
#  ---> 91b5cdb6dabe
# Step 4/7 : ARG EXTENSION="tar.gz"
#  ---> Running in d0f5188444b6
# Removing intermediate container d0f5188444b6
#  ---> 9626f941ccb2
# Step 5/7 : ADD https://nginx.org/download/${FILENAME}.${EXTENSION} .
# Downloading [==================================================>]  1.049MB/1.049MB
#  ---> a8e8dcca1be8
# Step 6/7 : RUN apt-get update &&     apt-get install build-essential                     libpcre3                     libpcre3-dev                     zlib1g                     zlib1g-dev                     libssl-dev                     -y &&     tar -xvf ${FILENAME}.${EXTENSION} && rm ${FILENAME}.${EXTENSION} &&     cd ${FILENAME} &&     ./configure         --sbin-path=/usr/bin/nginx         --conf-path=/etc/nginx/nginx.conf         --error-log-path=/var/log/nginx/error.log         --http-log-path=/var/log/nginx/access.log         --with-pcre         --pid-path=/var/run/nginx.pid         --with-http_ssl_module &&     make && make install &&     cd / && rm -rfv /${FILENAME} &&     apt-get remove build-essential                     libpcre3-dev                     zlib1g-dev                     libssl-dev                     -y &&     apt-get autoremove -y &&     apt-get clean && rm -rf /var/lib/apt/lists/*
#  ---> Running in e5675cad1260
### LONG INSTALLATION AND BUILD STUFF GOES HERE ###
# Removing intermediate container e5675cad1260
#  ---> dc7e4161f975
# Step 7/7 : CMD ["nginx", "-g", "daemon off;"]
#  ---> Running in b579e4600247
# Removing intermediate container b579e4600247
#  ---> 512aa6a95a93
# Successfully built 512aa6a95a93
# Successfully tagged custom-nginx:built

docker image ls

# REPOSITORY         TAG       IMAGE ID       CREATED              SIZE
# custom-nginx       built     512aa6a95a93   About a minute ago   81.6MB
# nginx              stable    b9e1dc12387a   11 days ago          133MB
```

Comme vous pouvez le voir, la taille de l'image est passée de 343 Mo à 81,6 Mo. L'image officielle fait 133 Mo. C'est une construction assez optimisée, mais nous pouvons aller un peu plus loin dans la sous-section suivante.

### Embrasser Alpine Linux

Si vous avez joué avec des conteneurs depuis un certain temps, vous avez peut-être entendu parler de quelque chose appelé [Alpine Linux](https://alpinelinux.org/). C'est une distribution [Linux](https://en.wikipedia.org/wiki/Linux) complète comme [Ubuntu](https://ubuntu.com/), [Debian](https://www.debian.org/) ou [Fedora](https://getfedora.org/).

Mais le bon côté d'Alpine est qu'il est construit autour de `musl` `libc` et `busybox` et est léger. Alors que la dernière image [ubuntu](https://hub.docker.com/_/ubuntu) pèse environ 28 Mo, [alpine](https://hub.docker.com/_/alpine) fait 2,8 Mo.

En plus de sa nature légère, Alpine est également sécurisé et est beaucoup mieux adapté pour créer des conteneurs que les autres distributions.

Bien que pas aussi convivial que les autres distributions commerciales, la transition vers Alpine est encore très simple. Dans cette sous-section, vous apprendrez à recréer l'image `custom-nginx` en utilisant l'image Alpine comme base.

Ouvrez votre `Dockerfile` et mettez à jour son contenu comme suit :

```dockerfile
FROM alpine:latest

EXPOSE 80

ARG FILENAME="nginx-1.19.2"
ARG EXTENSION="tar.gz"

ADD https://nginx.org/download/${FILENAME}.${EXTENSION} .

RUN apk add --no-cache pcre zlib && \
    apk add --no-cache \
            --virtual .build-deps \
            build-base \ 
            pcre-dev \
            zlib-dev \
            openssl-dev && \
    tar -xvf ${FILENAME}.${EXTENSION} && rm ${FILENAME}.${EXTENSION} && \
    cd ${FILENAME} && \
    ./configure \
        --sbin-path=/usr/bin/nginx \
        --conf-path=/etc/nginx/nginx.conf \
        --error-log-path=/var/log/nginx/error.log \
        --http-log-path=/var/log/nginx/access.log \
        --with-pcre \
        --pid-path=/var/run/nginx.pid \
        --with-http_ssl_module && \
    make && make install && \
    cd / && rm -rfv /${FILENAME} && \
    apk del .build-deps

CMD ["nginx", "-g", "daemon off;"]
```

Le code est presque identique à l'exception de quelques changements. Je vais lister les changements et les expliquer au fur et à mesure :

* Au lieu d'utiliser `apt-get install` pour installer des packages, nous utilisons `apk add`. L'option `--no-cache` signifie que le package téléchargé ne sera pas mis en cache. De même, nous utiliserons `apk del` au lieu de `apt-get remove` pour désinstaller des packages.
* L'option `--virtual` pour la commande `apk add` est utilisée pour regrouper un ensemble de packages dans un seul package virtuel pour une gestion plus facile. Les packages nécessaires uniquement pour la construction du programme sont étiquetés `.build-deps` qui sont ensuite supprimés à la ligne 29 en exécutant la commande `apk del .build-deps`. Vous pouvez en savoir plus sur les [virtuels](https://docs.alpinelinux.org/user-handbook/0.1a/Working/apk.html#_virtuals) dans la documentation officielle.
* Les noms des packages sont un peu différents ici. Habituellement, chaque distribution Linux a son dépôt de packages disponible pour tous où vous pouvez rechercher des packages. Si vous connaissez les packages nécessaires pour une certaine tâche, vous pouvez simplement vous rendre sur le dépôt désigné pour une distribution et les rechercher. Vous pouvez [rechercher les packages Alpine Linux ici](https://pkgs.alpinelinux.org/packages).

Maintenant, construisez une nouvelle image en utilisant ce `Dockerfile` et voyez la différence de taille de fichier :

```
docker image build --tag custom-nginx:built .

# Sending build context to Docker daemon  1.055MB
# Step 1/7 : FROM alpine:latest
#  ---> 7731472c3f2a
# Step 2/7 : EXPOSE 80
#  ---> Running in 8336cfaaa48d
# Removing intermediate container 8336cfaaa48d
#  ---> d448a9049d01
# Step 3/7 : ARG FILENAME="nginx-1.19.2"
#  ---> Running in bb8b2eae9d74
# Removing intermediate container bb8b2eae9d74
#  ---> 87ca74f32fbe
# Step 4/7 : ARG EXTENSION="tar.gz"
#  ---> Running in aa09627fe48c
# Removing intermediate container aa09627fe48c
#  ---> 70cb557adb10
# Step 5/7 : ADD https://nginx.org/download/${FILENAME}.${EXTENSION} .
# Downloading [==================================================>]  1.049MB/1.049MB
#  ---> b9790ce0c4d6
# Step 6/7 : RUN apk add --no-cache pcre zlib &&     apk add --no-cache             --virtual .build-deps             build-base             pcre-dev             zlib-dev             openssl-dev &&     tar -xvf ${FILENAME}.${EXTENSION} && rm ${FILENAME}.${EXTENSION} &&     cd ${FILENAME} &&     ./configure         --sbin-path=/usr/bin/nginx         --conf-path=/etc/nginx/nginx.conf         --error-log-path=/var/log/nginx/error.log         --http-log-path=/var/log/nginx/access.log         --with-pcre         --pid-path=/var/run/nginx.pid         --with-http_ssl_module &&     make && make install &&     cd / && rm -rfv /${FILENAME} &&     apk del .build-deps
#  ---> Running in 0b301f64ffc1
### LONG INSTALLATION AND BUILD STUFF GOES HERE ###
# Removing intermediate container 0b301f64ffc1
#  ---> dc7e4161f975
# Step 7/7 : CMD ["nginx", "-g", "daemon off;"]
#  ---> Running in b579e4600247
# Removing intermediate container b579e4600247
#  ---> 3e186a3c6830
# Successfully built 3e186a3c6830
# Successfully tagged custom-nginx:built

docker image ls

# REPOSITORY         TAG       IMAGE ID       CREATED         SIZE
# custom-nginx       built     3e186a3c6830   8 seconds ago   12.8MB
```

Alors que la version ubuntu était de 81,6 Mo, celle d'alpine est descendue à 12,8 Mo, ce qui représente un gain massif. En plus du gestionnaire de paquets `apk`, il y a quelques autres choses qui diffèrent dans Alpine par rapport à Ubuntu, mais ce n'est pas si grave. Vous pouvez simplement rechercher sur Internet chaque fois que vous êtes bloqué.

### Comment créer des images Docker exécutables

Dans la section précédente, vous avez travaillé avec l'image [fhsinchy/rmbyext](https://hub.docker.com/r/fhsinchy/rmbyext). Dans cette section, vous apprendrez comment créer une telle image exécutable.

Pour commencer, ouvrez le répertoire où vous avez cloné le dépôt qui accompagne ce livre. Le code de l'application `rmbyext` se trouve dans le sous-répertoire du même nom.

Avant de commencer à travailler sur le `Dockerfile`, prenez un moment pour planifier ce que devrait être le résultat final. À mon avis, cela devrait ressembler à quelque chose comme ceci :

* L'image doit avoir Python préinstallé.
* Elle doit contenir une copie de mon script `rmbyext`.
* Un répertoire de travail doit être défini où le script sera exécuté.
* Le script `rmbyext` doit être défini comme point d'entrée afin que l'image puisse prendre des noms d'extension comme arguments.

Pour construire l'image mentionnée ci-dessus, suivez les étapes suivantes :

* Obtenez une bonne image de base pour exécuter des scripts Python, comme [python](https://hub.docker.com/_/python).
* Configurez le répertoire de travail dans un répertoire facilement accessible.
* Installez Git afin que le script puisse être installé depuis mon dépôt GitHub.
* Installez le script en utilisant Git et pip.
* Supprimez les packages inutiles de la construction.
* Définissez `rmbyext` comme point d'entrée pour cette image.

Maintenant, créez un nouveau `Dockerfile` dans le répertoire `rmbyext` et mettez le code suivant dedans :

```dockerfile
FROM python:3-alpine

WORKDIR /zone

RUN apk add --no-cache git && \
    pip install git+https://github.com/fhsinchy/rmbyext.git#egg=rmbyext && \
    apk del git

ENTRYPOINT [ "rmbyext" ]
```

L'explication des instructions de ce fichier est la suivante :

* L'instruction `FROM` définit [python](https://hub.docker.com/_/python) comme image de base, créant un environnement idéal pour exécuter des scripts Python. Le tag `3-alpine` indique que vous voulez la variante Alpine de Python 3.
* L'instruction `WORKDIR` définit le répertoire de travail par défaut sur `/zone` ici. Le nom du répertoire de travail est complètement aléatoire ici. J'ai trouvé que zone était un nom approprié, vous pouvez utiliser ce que vous voulez.
* Étant donné que le script `rmbyext` est installé depuis GitHub, `git` est une dépendance d'installation. L'instruction `RUN` à la ligne 5 installe `git`, puis installe le script `rmbyext` en utilisant Git et pip. Il se débarrasse également de `git` par la suite.
* Enfin, à la ligne 9, l'instruction `ENTRYPOINT` définit le script `rmbyext` comme point d'entrée pour cette image.

Dans ce fichier entier, la ligne 9 est la magie qui transforme cette image apparemment normale en une image exécutable. Maintenant, pour construire l'image, vous pouvez exécuter la commande suivante :

```
docker image build --tag rmbyext .

# Sending build context to Docker daemon  2.048kB
# Step 1/4 : FROM python:3-alpine
# 3-alpine: Pulling from library/python
# 801bfaa63ef2: Already exists 
# 8723b2b92bec: Already exists 
# 4e07029ccd64: Already exists 
# 594990504179: Already exists 
# 140d7fec7322: Already exists 
# Digest: sha256:7492c1f615e3651629bd6c61777e9660caa3819cf3561a47d1d526dfeee02cf6
# Status: Downloaded newer image for python:3-alpine
#  ---> d4d4f50f871a
# Step 2/4 : WORKDIR /zone
#  ---> Running in 454374612a91
# Removing intermediate container 454374612a91
#  ---> 7f7e49bc98d2
# Step 3/4 : RUN apk add --no-cache git &&     pip install git+https://github.com/fhsinchy/rmbyext.git#egg=rmbyext &&     apk del git
#  ---> Running in 27e2e96dc95a
### LONG INSTALLATION STUFF GOES HERE ###
# Removing intermediate container 27e2e96dc95a
#  ---> 3c7389432e36
# Step 4/4 : ENTRYPOINT [ "rmbyext" ]
#  ---> Running in f239bbea1ca6
# Removing intermediate container f239bbea1ca6
#  ---> 1746b0cedbc7
# Successfully built 1746b0cedbc7
# Successfully tagged rmbyext:latest

docker image ls

# REPOSITORY         TAG        IMAGE ID       CREATED         SIZE
# rmbyext            latest     1746b0cedbc7   4 minutes ago   50.9MB
```

Ici, je n'ai pas fourni d'étiquette après le nom de l'image, donc l'image a été étiquetée comme `latest` par défaut. Vous devriez être en mesure d'exécuter l'image comme vous l'avez vu dans la section précédente. N'oubliez pas de vous référer au nom d'image réel que vous avez défini, au lieu de `fhsinchy/rmbyext` ici.

### Comment partager vos images Docker en ligne

Maintenant que vous savez comment créer des images, il est temps de les partager avec le monde. Partager des images en ligne est facile. Tout ce dont vous avez besoin est un compte sur l'un des registres en ligne. J'utiliserai [Docker Hub](https://hub.docker.com/) ici.

Naviguez vers la page [Inscription](https://hub.docker.com/signup) et créez un compte gratuit. Un compte gratuit vous permet d'héberger des dépôts publics illimités et un dépôt privé.

Une fois que vous avez créé le compte, vous devrez vous connecter à celui-ci en utilisant l'interface de ligne de commande Docker. Donc, ouvrez votre terminal et exécutez la commande suivante pour ce faire :

```
docker login

# Login with your Docker ID to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com to create one.
# Username: fhsinchy
# Password: 
# WARNING! Your password will be stored unencrypted in /home/fhsinchy/.docker/config.json.
# Configure a credential helper to remove this warning. See
# https://docs.docker.com/engine/reference/commandline/login/#credentials-store
#
# Login Succeeded
```

Vous serez invité à entrer votre nom d'utilisateur et votre mot de passe. Si vous les entrez correctement, vous devriez être connecté à votre compte avec succès.

Afin de partager une image en ligne, l'image doit être étiquetée. Vous avez déjà appris à étiqueter dans une sous-section précédente. Juste pour rafraîchir votre mémoire, la syntaxe générique pour l'option `--tag` ou `-t` est la suivante :

```
--tag <dépôt d'image>:<étiquette d'image>
```

Par exemple, partageons l'image `custom-nginx` en ligne. Pour ce faire, ouvrez une nouvelle fenêtre de terminal dans le répertoire du projet `custom-nginx`.

Pour partager une image en ligne, vous devrez l'étiqueter en suivant la syntaxe `<nom d'utilisateur docker hub>/<nom de l'image>:<étiquette de l'image>`. Mon nom d'utilisateur est `fhsinchy`, donc la commande ressemblera à ceci :

```
docker image build --tag fhsinchy/custom-nginx:latest --file Dockerfile.built .

# Step 1/9 : FROM ubuntu:latest
#  ---> d70eaf7277ea
# Step 2/9 : RUN apt-get update &&     apt-get install build-essential                    libpcre3                     libpcre3-dev                     zlib1g                     zlib1g-dev                     libssl-dev                     -y &&     apt-get clean && rm -rf /var/lib/apt/lists/*
#  ---> cbe1ced3da11
### LONG INSTALLATION STUFF GOES HERE ###
# Step 3/9 : ARG FILENAME="nginx-1.19.2"
#  ---> Running in 33b62a0e9ffb
# Removing intermediate container 33b62a0e9ffb
#  ---> fafc0aceb9c8
# Step 4/9 : ARG EXTENSION="tar.gz"
#  ---> Running in 5c32eeb1bb11
# Removing intermediate container 5c32eeb1bb11
#  ---> 36efdf6efacc
# Step 5/9 : ADD https://nginx.org/download/${FILENAME}.${EXTENSION} .
# Downloading [==================================================>]  1.049MB/1.049MB
#  ---> dba252f8d609
# Step 6/9 : RUN tar -xvf ${FILENAME}.${EXTENSION}
#  ---> Running in 2f5b091b2125
### LONG EXTRACTION STUFF GOES HERE ###
# Removing intermediate container 2f5b091b2125
#  ---> 2c9a325d74f1
# Step 7/9 : RUN cd ${FILENAME} &&     ./configure         --sbin-path=/usr/bin/nginx         --conf-path=/etc/nginx/nginx.conf         --error-log-path=/var/log/nginx/error.log         --http-log-path=/var/log/nginx/access.log         --with-pcre         --pid-path=/var/run/nginx.pid         --with-http_ssl_module &&     make && make install
#  ---> Running in 11cc82dd5186
### LONG CONFIGURATION AND BUILD STUFF GOES HERE ###
# Removing intermediate container 11cc82dd5186
#  ---> 6c122e485ec8
# Step 8/9 : RUN rm -rf /${FILENAME}}
#  ---> Running in 04102366960b
# Removing intermediate container 04102366960b
#  ---> 6bfa35420a73
# Step 9/9 : CMD ["nginx", "-g", "daemon off;"]
#  ---> Running in 63ee44b571bb
# Removing intermediate container 63ee44b571bb
#  ---> 4ce79556db1b
# Successfully built 4ce79556db1b
# Successfully tagged fhsinchy/custom-nginx:latest
```

Dans cette commande, `fhsinchy/custom-nginx` est le dépôt de l'image et `latest` est l'étiquette. Le nom de l'image peut être n'importe quoi que vous voulez et ne peut pas être changé une fois que vous avez téléchargé l'image. L'étiquette peut être changée à tout moment et reflète généralement la version du logiciel ou différents types de builds.

Prenez l'image `node` comme exemple. L'image `node:lts` fait référence à la version à support long terme de Node.js alors que la version `node:lts-alpine` fait référence à la version de Node.js construite pour Alpine Linux, qui est beaucoup plus petite que la version régulière.

Si vous ne donnez aucune étiquette à l'image, elle sera automatiquement étiquetée comme `latest`. Mais cela ne signifie pas que l'étiquette `latest` fera toujours référence à la dernière version. Si, pour une raison quelconque, vous étiquetez explicitement une ancienne version de l'image comme `latest`, alors Docker ne fera aucun effort supplémentaire pour vérifier cela.

Une fois que l'image a été construite, vous pouvez la télécharger en exécutant la commande suivante :

```
docker image push <dépôt de l'image>:<étiquette de l'image>
```

Donc dans mon cas, la commande sera la suivante :

```
docker image push fhsinchy/custom-nginx:latest

# The push refers to repository [docker.io/fhsinchy/custom-nginx]
# 4352b1b1d9f5: Pushed 
# a4518dd720bd: Pushed 
# 1d756dc4e694: Pushed 
# d7a7e2b6321a: Pushed 
# f6253634dc78: Mounted from library/ubuntu 
# 9069f84dbbe9: Mounted from library/ubuntu 
# bacd3af13903: Mounted from library/ubuntu 
# latest: digest: sha256:ffe93440256c9edb2ed67bf3bba3c204fec3a46a36ac53358899ce1a9eee497a size: 1788
```

Selon la taille de l'image, le téléchargement peut prendre un certain temps. Une fois terminé, vous devriez pouvoir trouver l'image dans votre page de profil hub.

## Comment conteneuriser une application JavaScript

Maintenant que vous avez une idée de la façon de créer des images, il est temps de travailler avec quelque chose de plus pertinent.

Dans cette sous-section, vous travaillerez avec le code source de l'image [fhsinchy/hello-dock](https://hub.docker.com/r/fhsinchy/hello-dock) avec laquelle vous avez travaillé dans une section précédente. Dans le processus de conteneurisation de cette application très simple, vous serez introduit aux volumes et aux constructions multi-étapes, deux des concepts les plus importants dans Docker.

### Comment écrire le Dockerfile de développement

Pour commencer, ouvrez le répertoire où vous avez cloné le dépôt qui accompagne ce livre. Le code de l'application `hello-dock` réside dans le sous-répertoire du même nom.

Il s'agit d'un projet JavaScript très simple alimenté par le projet [vitejs/vite](https://github.com/vitejs/vite). Ne vous inquiétez pas, vous n'avez pas besoin de connaître JavaScript ou vite pour suivre cette sous-section. Avoir une compréhension de base de [Node.js](https://nodejs.org/) et [npm](https://www.npmjs.com/) suffira.

Tout comme tout autre projet que vous avez fait dans la sous-section précédente, vous commencerez par faire un plan de la manière dont vous voulez que cette application s'exécute. À mon avis, le plan devrait être le suivant :

* Obtenez une bonne image de base pour exécuter des applications JavaScript, comme [node](https://hub.docker.com/_/node).
* Définissez le répertoire de travail par défaut à l'intérieur de l'image.
* Copiez le fichier `package.json` dans l'image.
* Installez les dépendances nécessaires.
* Copiez le reste des fichiers du projet.
* Démarrez le serveur de développement `vite` en exécutant la commande `npm run dev`.

Ce plan devrait toujours provenir du développeur de l'application que vous conteneurisez. Si vous êtes vous-même le développeur, alors vous devriez déjà avoir une compréhension appropriée de la manière dont cette application doit être exécutée.

Maintenant, si vous mettez le plan mentionné ci-dessus dans `Dockerfile.dev`, le fichier devrait ressembler à ce qui suit :

```dockerfile
FROM node:lts-alpine

EXPOSE 3000

USER node

RUN mkdir -p /home/node/app

WORKDIR /home/node/app

COPY ./package.json .
RUN npm install

COPY . .

CMD [ "npm", "run", "dev" ]
```

L'explication de ce code est la suivante :

* L'instruction `FROM` ici définit l'image officielle Node.js comme base, vous offrant toutes les fonctionnalités de Node.js nécessaires pour exécuter n'importe quelle application JavaScript. Le tag `lts-alpine` indique que vous souhaitez utiliser la variante Alpine, la version à support long terme de l'image. Les tags disponibles et la documentation nécessaire pour l'image peuvent être trouvés sur la page [node](https://hub.docker.com/_/node) du hub.
* L'instruction `USER` définit l'utilisateur par défaut pour l'image comme `node`. Par défaut, Docker exécute les conteneurs en tant qu'utilisateur root. Mais selon les [Meilleures pratiques Docker et Node.js](https://github.com/nodejs/docker-node/blob/master/docs/BestPractices.md), cela peut poser une menace pour la sécurité. Il est donc préférable d'exécuter en tant qu'utilisateur non-root chaque fois que possible. L'image node est livrée avec un utilisateur non-root nommé `node` que vous pouvez définir comme utilisateur par défaut en utilisant l'instruction `USER`.
* L'instruction `RUN mkdir -p /home/node/app` crée un répertoire appelé `app` à l'intérieur du répertoire personnel de l'utilisateur `node`. Le répertoire personnel de tout utilisateur non-root sous Linux est généralement `/home/<nom d'utilisateur>` par défaut.
* Ensuite, l'instruction `WORKDIR` définit le répertoire de travail par défaut sur le répertoire nouvellement créé `/home/node/app`. Par défaut, le répertoire de travail de toute image est la racine. Vous ne voulez pas que des fichiers inutiles soient dispersés dans votre répertoire racine, n'est-ce pas ? Vous changez donc le répertoire de travail par défaut en quelque chose de plus sensé comme `/home/node/app` ou ce que vous voulez. Ce répertoire de travail sera applicable à toute instruction `COPY`, `ADD`, `RUN` et `CMD` ultérieure.
* L'instruction `COPY` ici copie le fichier `package.json` qui contient des informations concernant toutes les dépendances nécessaires pour cette application. L'instruction `RUN` exécute la commande `npm install` qui est la commande par défaut pour installer les dépendances en utilisant un fichier `package.json` dans les projets Node.js. Le `.` à la fin représente le répertoire de travail.
* La deuxième instruction `COPY` copie le reste du contenu du répertoire actuel (`.`) du système de fichiers hôte vers le répertoire de travail (`.`) à l'intérieur de l'image.
* Enfin, l'instruction `CMD` ici définit la commande par défaut pour cette image qui est `npm run dev` écrite en forme `exec`.
* Le serveur de développement `vite` s'exécute par défaut sur le port `3000`, et ajouter une commande `EXPOSE` semblait être une bonne idée, donc la voici.

Maintenant, pour construire une image à partir de ce `Dockerfile.dev`, vous pouvez exécuter la commande suivante :

```
docker image build --file Dockerfile.dev --tag hello-dock:dev .

# Step 1/7 : FROM node:lts
#  ---> b90fa0d7cbd1
# Step 2/7 : EXPOSE 3000
#  ---> Running in 722d639badc7
# Removing intermediate container 722d639badc7
#  ---> e2a8aa88790e
# Step 3/7 : WORKDIR /app
#  ---> Running in 998e254b4d22
# Removing intermediate container 998e254b4d22
#  ---> 6bd4c42892a4
# Step 4/7 : COPY ./package.json .
#  ---> 24fc5164a1dc
# Step 5/7 : RUN npm install
#  ---> Running in 23b4de3f930b
### LONG INSTALLATION STUFF GOES HERE ###
# Removing intermediate container 23b4de3f930b
#  ---> c17ecb19a210
# Step 6/7 : COPY . .
#  ---> afb6d9a1bc76
# Step 7/7 : CMD [ "npm", "run", "dev" ]
#  ---> Running in a7ff529c28fe
# Removing intermediate container a7ff529c28fe
#  ---> 1792250adb79
# Successfully built 1792250adb79
# Successfully tagged hello-dock:dev
```

Étant donné que le nom de fichier n'est pas `Dockerfile`, vous devez explicitement passer le nom de fichier en utilisant l'option `--file`. Un conteneur peut être exécuté en utilisant cette image en exécutant la commande suivante :

```
docker container run \
    --rm \
    --detach \
    --publish 3000:3000 \
    --name hello-dock-dev \
    hello-dock:dev

# 21b9b1499d195d85e81f0e8bce08f43a64b63d589c5f15cbbd0b9c0cb07ae268
```

Maintenant, visitez `http://127.0.0.1:3000` pour voir l'application `hello-dock` en action.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/hello-dock-dev.png)

Félicitations pour avoir exécuté votre première application du monde réel à l'intérieur d'un conteneur. Le code que vous venez d'écrire est correct, mais il y a un gros problème et quelques endroits où il peut être amélioré. Commençons par le problème d'abord.

### Comment travailler avec les montages de liaison dans Docker

Si vous avez déjà travaillé avec un framework JavaScript front-end, vous devriez savoir que les serveurs de développement de ces frameworks sont généralement dotés d'une fonction de rechargement à chaud. C'est-à-dire que si vous apportez une modification à votre code, le serveur se rechargera, reflétant automatiquement toute modification que vous avez apportée immédiatement.

Mais si vous apportez des modifications à votre code maintenant, vous verrez que rien ne se passe avec votre application s'exécutant dans le navigateur. Cela est dû au fait que vous apportez des modifications au code que vous avez dans votre système de fichiers local, mais l'application que vous voyez dans le navigateur réside à l'intérieur du système de fichiers du conteneur.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/local-vs-container-file-system.svg)

Pour résoudre ce problème, vous pouvez à nouveau utiliser un [montage de liaison](https://docs.docker.com/storage/bind-mounts/). En utilisant des montages de liaison, vous pouvez facilement monter l'un de vos répertoires du système de fichiers local à l'intérieur d'un conteneur. Au lieu de faire une copie du système de fichiers local, le montage de liaison peut référencer directement le système de fichiers local depuis l'intérieur du conteneur.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/bind-mounts.svg)

De cette manière, toute modification que vous apportez à votre code source local se reflétera immédiatement à l'intérieur du conteneur, déclenchant la fonction de rechargement à chaud du serveur de développement `vite`. Les modifications apportées au système de fichiers à l'intérieur du conteneur seront également reflétées sur votre système de fichiers local.

Vous avez déjà appris dans la sous-section [Travailler avec des images exécutables](#working-with-executable-images), les montages de liaison peuvent être créés en utilisant l'option `--volume` ou `-v` pour les commandes `container run` ou `container start`. Juste pour vous rappeler, la syntaxe générique est la suivante :

```
--volume <chemin absolu du répertoire du système de fichiers local>:<chemin absolu du répertoire du système de fichiers du conteneur>:<accès en lecture-écriture>
```

Arrêtez votre conteneur `hello-dock-dev` précédemment démarré, et démarrez un nouveau conteneur en exécutant la commande suivante :

```
docker container run \
    --rm \
    --publish 3000:3000 \
    --name hello-dock-dev \
    --volume $(pwd):/home/node/app \
    hello-dock:dev

# sh: 1: vite: not found
# npm ERR! code ELIFECYCLE
# npm ERR! syscall spawn
# npm ERR! file sh
# npm ERR! errno ENOENT
# npm ERR! hello-dock@0.0.0 dev: `vite`
# npm ERR! spawn ENOENT
# npm ERR!
# npm ERR! Failed at the hello-dock@0.0.0 dev script.
# npm ERR! This is probably not a problem with npm. There is likely additional logging output above.
# npm WARN Local package.json exists, but node_modules missing, did you mean to install?
```

Gardez à l'esprit que j'ai omis l'option `--detach` et c'est pour démontrer un point très important. Comme vous pouvez le voir, l'application ne s'exécute pas du tout maintenant.

C'est parce que, bien que l'utilisation d'un volume résout le problème des rechargements à chaud, elle introduit un autre problème. Si vous avez une expérience précédente avec Node.js, vous savez peut-être que les dépendances d'un projet Node.js vivent à l'intérieur du répertoire `node_modules` à la racine du projet.

Maintenant que vous montez la racine du projet sur votre système de fichiers local en tant que volume à l'intérieur du conteneur, le contenu à l'intérieur du conteneur est remplacé ainsi que le répertoire `node_modules` contenant toutes les dépendances. Cela signifie que le package `vite` a disparu.

### Comment travailler avec des volumes anonymes dans Docker

Ce problème peut être résolu en utilisant un volume anonyme. Un volume anonyme est identique à un montage de liaison sauf que vous n'avez pas besoin de spécifier le répertoire source ici. La syntaxe générique pour créer un volume anonyme est la suivante :

```
--volume <chemin absolu du répertoire du système de fichiers du conteneur>:<accès en lecture-écriture>
```

Ainsi, la commande finale pour démarrer le conteneur `hello-dock` avec les deux volumes devrait être la suivante :

```
docker container run \
    --rm \
    --detach \
    --publish 3000:3000 \
    --name hello-dock-dev \
    --volume $(pwd):/home/node/app \
    --volume /home/node/app/node_modules \
    hello-dock:dev

# 53d1cfdb3ef148eb6370e338749836160f75f076d0fbec3c2a9b059a8992de8b
```

Ici, Docker prendra l'ensemble du répertoire `node_modules` de l'intérieur du conteneur et le rangera dans un autre répertoire géré par le démon Docker sur votre système de fichiers hôte et montera ce répertoire en tant que `node_modules` à l'intérieur du conteneur.

### Comment effectuer des constructions multi-étapes dans Docker

Jusqu'à présent dans cette section, vous avez construit une image pour exécuter une application JavaScript en mode développement. Maintenant, si vous souhaitez construire l'image en mode production, de nouveaux défis se présentent.

En mode développement, la commande `npm run serve` démarre un serveur de développement qui sert l'application à l'utilisateur. Ce serveur ne se contente pas de servir les fichiers, mais fournit également la fonction de rechargement à chaud.

En mode production, la commande `npm run build` compile tout votre code JavaScript en fichiers HTML, CSS et JavaScript statiques. Pour exécuter ces fichiers, vous n'avez pas besoin de node ou d'autres dépendances d'exécution. Tout ce dont vous avez besoin est un serveur comme `nginx`, par exemple.

Pour créer une image où l'application s'exécute en mode production, vous pouvez suivre les étapes suivantes :

* Utilisez `node` comme image de base et construisez l'application.
* Installez `nginx` à l'intérieur de l'image node et utilisez-le pour servir les fichiers statiques.

Cette approche est complètement valide. Mais le problème est que l'image `node` est volumineuse et que la plupart des éléments qu'elle transporte sont inutiles pour servir vos fichiers statiques. Une meilleure approche pour ce scénario est la suivante :

* Utilisez l'image `node` comme base et construisez l'application.
* Copiez les fichiers créés en utilisant l'image `node` vers une image `nginx`.
* Créez l'image finale basée sur `nginx` et supprimez tout ce qui est lié à `node`.

De cette façon, votre image ne contient que les fichiers nécessaires et devient très pratique.

Cette approche est une construction multi-étapes. Pour effectuer une telle construction, créez un nouveau `Dockerfile` dans votre répertoire de projet `hello-dock` et mettez le contenu suivant dedans :

```dockerfile
FROM node:lts-alpine as builder

WORKDIR /app

COPY ./package.json ./
RUN npm install

COPY . .
RUN npm run build

FROM nginx:stable-alpine

EXPOSE 80

COPY --from=builder /app/dist /usr/share/nginx/html
```

Comme vous pouvez le voir, le `Dockerfile` ressemble beaucoup à vos précédents avec quelques particularités. L'explication de ce fichier est la suivante :

* La ligne 1 commence la première étape de la construction en utilisant `node:lts-alpine` comme image de base. La syntaxe `as builder` attribue un nom à cette étape afin qu'elle puisse être référencée plus tard.
* De la ligne 3 à la ligne 9, il s'agit de choses standard que vous avez vues de nombreuses fois auparavant. La commande `RUN npm run build` compile en réalité toute l'application et la place dans le répertoire `/app/dist` où `/app` est le répertoire de travail et `/dist` est le répertoire de sortie par défaut pour les applications `vite`.
* La ligne 11 commence la deuxième étape de la construction en utilisant `nginx:stable-alpine` comme image de base.
* Le serveur NGINX s'exécute sur le port 80 par défaut, donc la ligne `EXPOSE 80` est ajoutée.
* La dernière ligne est une instruction `COPY`. La partie `--from=builder` indique que vous souhaitez copier certains fichiers de l'étape `builder`. Après cela, il s'agit d'une instruction de copie standard où `/app/dist` est la source et `/usr/share/nginx/html` est la destination. La destination utilisée ici est le chemin du site par défaut pour NGINX, donc tout fichier statique que vous y placez sera automatiquement servi.

Comme vous pouvez le voir, l'image résultante est une image de base `nginx` contenant uniquement les fichiers nécessaires à l'exécution de l'application. Pour construire cette image, exécutez la commande suivante :

```
docker image build --tag hello-dock:prod .

# Step 1/9 : FROM node:lts-alpine as builder
#  ---> 72aaced1868f
# Step 2/9 : WORKDIR /app
#  ---> Running in e361c5c866dd
# Removing intermediate container e361c5c866dd
#  ---> 241b4b97b34c
# Step 3/9 : COPY ./package.json ./
#  ---> 6c594c5d2300
# Step 4/9 : RUN npm install
#  ---> Running in 6dfabf0ee9f8
# npm WARN deprecated fsevents@2.1.3: Please update to v 2.2.x
#
# > esbuild@0.8.29 postinstall /app/node_modules/esbuild
# > node install.js
#
# npm notice created a lockfile as package-lock.json. You should commit this file.
# npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@~2.1.2 (node_modules/chokidar/node_modules/fsevents):
# npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@2.1.3: wanted {"os":"darwin","arch":"any"} (current: {"os":"linux","arch":"x64"})
# npm WARN hello-dock@0.0.0 No description
# npm WARN hello-dock@0.0.0 No repository field.
# npm WARN hello-dock@0.0.0 No license field.
#
# added 327 packages from 301 contributors and audited 329 packages in 35.971s
#
# 26 packages are looking for funding
#   run `npm fund` for details
#
# found 0 vulnerabilities
#
# Removing intermediate container 6dfabf0ee9f8
#  ---> 21fd1b065314
# Step 5/9 : COPY . .
#  ---> 43243f95bff7
# Step 6/9 : RUN npm run build
#  ---> Running in 4d918cf18584
#
# > hello-dock@0.0.0 build /app
# > vite build
#
# - Building production bundle...
#
# [write] dist/index.html 0.39kb, brotli: 0.15kb
# [write] dist/_assets/docker-handbook-github.3adb4865.webp 12.32kb
# [write] dist/_assets/index.eabcae90.js 42.56kb, brotli: 15.40kb
# [write] dist/_assets/style.0637ccc5.css 0.16kb, brotli: 0.10kb
# - Building production bundle...
#
# Build completed in 1.71s.
#
# Removing intermediate container 4d918cf18584
#  ---> 187fb3e82d0d
# Step 7/9 : EXPOSE 80
#  ---> Running in b3aab5cf5975
# Removing intermediate container b3aab5cf5975
#  ---> d6fcc058cfda
# Step 8/9 : FROM nginx:stable-alpine
# stable: Pulling from library/nginx
# 6ec7b7d162b2: Already exists 
# 43876acb2da3: Pull complete 
# 7a79edd1e27b: Pull complete 
# eea03077c87e: Pull complete 
# eba7631b45c5: Pull complete 
# Digest: sha256:2eea9f5d6fff078ad6cc6c961ab11b8314efd91fb8480b5d054c7057a619e0c3
# Status: Downloaded newer image for nginx:stable
#  ---> 05f64a802c26
# Step 9/9 : COPY --from=builder /app/dist /usr/share/nginx/html
#  ---> 8c6dfc34a10d
# Successfully built 8c6dfc34a10d
# Successfully tagged hello-dock:prod
```

Une fois l'image construite, vous pouvez exécuter un nouveau conteneur en exécutant la commande suivante :

```
docker container run \
    --rm \
    --detach \
    --name hello-dock-prod \
    --publish 8080:80 \
    hello-dock:prod

# 224aaba432bb09aca518fdd0365875895c2f5121eb668b2e7b2d5a99c019b953
```

L'application en cours d'exécution devrait être disponible sur `http://127.0.0.1:8080` :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/hello-dock.png)

Ici, vous pouvez voir mon application `hello-dock` dans toute sa gloire. Les constructions multi-étapes peuvent être très utiles si vous construisez de grandes applications avec beaucoup de dépendances. Si elles sont configurées correctement, les images construites en plusieurs étapes peuvent être très optimisées et compactes.

### Comment ignorer les fichiers inutiles

Si vous avez travaillé avec `git` depuis un certain temps, vous connaissez peut-être les fichiers `.gitignore` dans les projets. Ceux-ci contiennent une liste de fichiers et de répertoires à exclure du dépôt.

Eh bien, Docker a un concept similaire. Le fichier `.dockerignore` contient une liste de fichiers et de répertoires à exclure des constructions d'images. Vous pouvez trouver un fichier `.dockerignore` pré-créé dans le répertoire `hello-dock`.

```.dockerignore
.git
*Dockerfile*
*docker-compose*
node_modules
```

Ce fichier `.dockerignore` doit être dans le contexte de construction. Les fichiers et répertoires mentionnés ici seront ignorés par l'instruction `COPY`. Mais si vous faites un montage de liaison, le fichier `.dockerignore` n'aura aucun effet. J'ai ajouté des fichiers `.dockerignore` là où c'est nécessaire dans le dépôt du projet.

## Bases de la manipulation du réseau dans Docker

Jusqu'à présent dans ce livre, vous n'avez travaillé qu'avec des projets à conteneur unique. Mais dans la vie réelle, la majorité des projets avec lesquels vous devrez travailler auront plus d'un conteneur. Et pour être honnête, travailler avec un ensemble de conteneurs peut être un peu difficile si vous ne comprenez pas les nuances de l'isolation des conteneurs.

Ainsi, dans cette section du livre, vous vous familiariserez avec les bases de la mise en réseau avec Docker et vous travaillerez concrètement avec un petit projet multi-conteneurs.

Vous avez déjà appris dans la section précédente que les conteneurs sont des environnements isolés. Considérez maintenant un scénario où vous avez une application `notes-api` alimentée par [Express.js](https://expressjs.com/) et un serveur de base de données [PostgreSQL](https://www.postgresql.org/) s'exécutant dans deux conteneurs séparés.

Ces deux conteneurs sont complètement isolés l'un de l'autre et ignorent l'existence de l'autre. **Alors, comment connectez-vous les deux ? Cela ne serait-il pas un défi ?**

Vous pouvez penser à deux solutions possibles à ce problème. Elles sont les suivantes :

* Accéder au serveur de base de données en utilisant un port exposé.
* Accéder au serveur de base de données en utilisant son adresse IP et son port par défaut.

La première solution implique d'exposer un port du conteneur `postgres` et le `notes-api` se connectera à travers celui-ci. Supposons que le port exposé du conteneur `postgres` est 5432. Maintenant, si vous essayez de vous connecter à `127.0.0.1:5432` depuis l'intérieur du conteneur `notes-api`, vous constaterez que le `notes-api` ne trouve pas du tout le serveur de base de données.

La raison est que lorsque vous dites `127.0.0.1` à l'intérieur du conteneur `notes-api`, vous faites simplement référence au `localhost` de ce conteneur et de ce conteneur uniquement. Le serveur `postgres` n'existe tout simplement pas là. Par conséquent, l'application `notes-api` a échoué à se connecter.

La deuxième solution à laquelle vous pouvez penser est de trouver l'adresse IP exacte du conteneur `postgres` en utilisant la commande `container inspect` et de l'utiliser avec le port. En supposant que le nom du conteneur `postgres` est `notes-api-db-server`, vous pouvez facilement obtenir l'adresse IP en exécutant la commande suivante :

```
docker container inspect --format='{{range .NetworkSettings.Networks}} {{.IPAddress}} {{end}}' notes-api-db-server

#  172.17.0.2
```

Maintenant, étant donné que le port par défaut pour `postgres` est `5432`, vous pouvez très facilement accéder au serveur de base de données en vous connectant à `172.17.0.2:5432` depuis le conteneur `notes-api`.

Il y a aussi des problèmes dans cette approche. Utiliser des adresses IP pour faire référence à un conteneur n'est pas recommandé. De plus, si le conteneur est détruit et recréé, l'adresse IP peut changer. Suivre ces adresses IP changeantes peut être assez fastidieux.

Maintenant que j'ai écarté les réponses possibles incorrectes à la question initiale, la réponse correcte est, **vous les connectez en les mettant sous un réseau de pont défini par l'utilisateur.**

### Bases du réseau Docker

Un réseau dans Docker est un autre objet logique comme un conteneur et une image. Tout comme les deux autres, il existe une pléthore de commandes sous le groupe `docker network` pour manipuler les réseaux.

Pour lister les réseaux de votre système, exécutez la commande suivante :

```
docker network ls

# NETWORK ID     NAME      DRIVER    SCOPE
# c2e59f2b96bd   bridge    bridge    local
# 124dccee067f   host      host      local
# 506e3822bf1f   none      null      local
```

Vous devriez voir trois réseaux dans votre système. Maintenant, regardez la colonne `DRIVER` du tableau ici. Ces pilotes peuvent être traités comme le type de réseau.

Par défaut, Docker dispose de cinq pilotes de réseau. Ils sont les suivants :

* `bridge` - Le pilote de réseau par défaut dans Docker. Cela peut être utilisé lorsque plusieurs conteneurs s'exécutent en mode standard et doivent communiquer entre eux.
* `host` - Supprime complètement l'isolation du réseau. Tout conteneur s'exécutant sous un réseau `host` est essentiellement attaché au réseau du système hôte.
* `none` - Ce pilote désactive le réseau pour les conteneurs. Je n'ai pas encore trouvé de cas d'utilisation pour cela.
* `overlay` - Cela est utilisé pour connecter plusieurs démons Docker à travers des ordinateurs et est hors du cadre de ce livre.
* `macvlan` - Permet l'attribution d'adresses MAC aux conteneurs, les faisant fonctionner comme des appareils physiques dans un réseau.

Il existe également des plugins tiers qui permettent d'intégrer Docker avec des piles réseau spécialisées. Parmi les cinq mentionnés ci-dessus, vous ne travaillerez qu'avec le pilote de réseau `bridge` dans ce livre.

### Comment créer un pont défini par l'utilisateur dans Docker

Avant de commencer à créer votre propre pont, je voudrais prendre un peu de temps pour discuter du réseau de pont par défaut qui vient avec Docker. Commençons par lister tous les réseaux de votre système :

```
docker network ls

# NETWORK ID     NAME      DRIVER    SCOPE
# c2e59f2b96bd   bridge    bridge    local
# 124dccee067f   host      host      local
# 506e3822bf1f   none      null      local
```

Comme vous pouvez le voir, Docker est livré avec un réseau de pont par défaut nommé `bridge`. Tout conteneur que vous exécutez sera automatiquement attaché à ce réseau de pont :

```
docker container run --rm --detach --name hello-dock --publish 8080:80 fhsinchy/hello-dock
# a37f723dad3ae793ce40f97eb6bb236761baa92d72a2c27c24fc7fda0756657d

docker network inspect --format='{{range .Containers}}{{.Name}}{{end}}' bridge
# hello-dock
```

Les conteneurs attachés au réseau de pont par défaut peuvent communiquer entre eux en utilisant des adresses IP, ce que j'ai déjà déconseillé dans la sous-section précédente.

Un pont défini par l'utilisateur, cependant, a quelques fonctionnalités supplémentaires par rapport au pont par défaut. Selon la documentation officielle [docs](https://docs.docker.com/network/bridge/#differences-between-user-defined-bridges-and-the-default-bridge) sur ce sujet, certaines fonctionnalités supplémentaires notables sont les suivantes :

* **Les ponts définis par l'utilisateur fournissent une résolution DNS automatique entre les conteneurs :** Cela signifie que les conteneurs attachés au même réseau peuvent communiquer entre eux en utilisant le nom du conteneur. Donc si vous avez deux conteneurs nommés `notes-api` et `notes-db`, le conteneur API pourra se connecter au conteneur de base de données en utilisant le nom `notes-db`.
* **Les ponts définis par l'utilisateur fournissent une meilleure isolation :** Tous les conteneurs sont attachés au réseau de pont par défaut, ce qui peut causer des conflits entre eux. Attacher des conteneurs à un pont défini par l'utilisateur peut assurer une meilleure isolation.
* **Les conteneurs peuvent être attachés et détachés des réseaux définis par l'utilisateur à la volée :** Pendant la durée de vie d'un conteneur, vous pouvez le connecter ou le déconnecter des réseaux définis par l'utilisateur à la volée. Pour supprimer un conteneur du réseau de pont par défaut, vous devez arrêter le conteneur et le recréer avec différentes options de réseau.

Maintenant que vous avez appris beaucoup de choses sur un réseau défini par l'utilisateur, il est temps d'en créer un pour vous-même. Un réseau peut être créé en utilisant la commande `network create`. La syntaxe générique de la commande est la suivante :

```
docker network create <nom du réseau>
```

Pour créer un réseau avec le nom `skynet`, exécutez la commande suivante :

```
docker network create skynet

# 7bd5f351aa892ac6ec15fed8619fc3bbb95a7dcdd58980c28304627c8f7eb070

docker network ls

# NETWORK ID     NAME     DRIVER    SCOPE
# be0cab667c4b   bridge   bridge    local
# 124dccee067f   host     host      local
# 506e3822bf1f   none     null      local
# 7bd5f351aa89   skynet   bridge    local
```

Comme vous pouvez le voir, un nouveau réseau a été créé avec le nom donné. Aucun conteneur n'est actuellement attaché à ce réseau. Dans la sous-section suivante, vous apprendrez à attacher des conteneurs à un réseau.

### Comment attacher un conteneur à un réseau dans Docker

Il existe principalement deux façons d'attacher un conteneur à un réseau. Tout d'abord, vous pouvez utiliser la commande network connect pour attacher un conteneur à un réseau. La syntaxe générique de la commande est la suivante :

```
docker network connect <identifiant du réseau> <identifiant du conteneur>
```

Pour connecter le conteneur `hello-dock` au réseau `skynet`, vous pouvez exécuter la commande suivante :

```
docker network connect skynet hello-dock

docker network inspect --format='{{range .Containers}} {{.Name}} {{end}}' skynet

#  hello-dock

docker network inspect --format='{{range .Containers}} {{.Name}} {{end}}' bridge

#  hello-dock
```

Comme vous pouvez le voir à partir des sorties des deux commandes `network inspect`, le conteneur `hello-dock` est maintenant attaché à la fois au réseau `skynet` et au réseau de pont par défaut.

La deuxième façon d'attacher un conteneur à un réseau est d'utiliser l'option `--network` pour les commandes `container run` ou `container create`. La syntaxe générique de l'option est la suivante :

```
--network <identifiant du réseau>
```

Pour exécuter un autre conteneur `hello-dock` attaché au même réseau, vous pouvez exécuter la commande suivante :

```
docker container run --network skynet --rm --name alpine-box -it alpine sh

# vous place dans le shell alpine linux

/ # ping hello-dock

# PING hello-dock (172.18.0.2): 56 data bytes
# 64 bytes from 172.18.0.2: seq=0 ttl=64 time=0.191 ms
# 64 bytes from 172.18.0.2: seq=1 ttl=64 time=0.103 ms
# 64 bytes from 172.18.0.2: seq=2 ttl=64 time=0.139 ms
# 64 bytes from 172.18.0.2: seq=3 ttl=64 time=0.142 ms
# 64 bytes from 172.18.0.2: seq=4 ttl=64 time=0.146 ms
# 64 bytes from 172.18.0.2: seq=5 ttl=64 time=0.095 ms
# 64 bytes from 172.18.0.2: seq=6 ttl=64 time=0.181 ms
# 64 bytes from 172.18.0.2: seq=7 ttl=64 time=0.138 ms
# 64 bytes from 172.18.0.2: seq=8 ttl=64 time=0.158 ms
# 64 bytes from 172.18.0.2: seq=9 ttl=64 time=0.137 ms
# 64 bytes from 172.18.0.2: seq=10 ttl=64 time=0.145 ms
# 64 bytes from 172.18.0.2: seq=11 ttl=64 time=0.138 ms
# 64 bytes from 172.18.0.2: seq=12 ttl=64 time=0.085 ms

--- hello-dock ping statistics ---
13 packets transmitted, 13 packets received, 0% packet loss
round-trip min/avg/max = 0.085/0.138/0.191 ms
```

Comme vous pouvez le voir, l'exécution de `ping hello-dock` depuis l'intérieur du conteneur `alpine-box` fonctionne parce que les deux conteneurs sont sous le même réseau de pont défini par l'utilisateur et la résolution DNS automatique fonctionne.

Gardez à l'esprit, cependant, que pour que la résolution DNS automatique fonctionne, vous devez attribuer des noms personnalisés aux conteneurs. L'utilisation du nom généré aléatoirement ne fonctionnera pas.

### Comment détacher des conteneurs d'un réseau dans Docker

Dans la sous-section précédente, vous avez appris à attacher des conteneurs à un réseau. Dans cette sous-section, vous apprendrez à les détacher.

Vous pouvez utiliser la commande `network disconnect` pour cette tâche. La syntaxe générique de la commande est la suivante :

```
docker network disconnect <identifiant du réseau> <identifiant du conteneur>
```

Pour détacher le conteneur `hello-dock` du réseau `skynet`, vous pouvez exécuter la commande suivante :

```
docker network disconnect skynet hello-dock
```

Tout comme la commande `network connect`, la commande `network disconnect` ne donne aucune sortie.

### Comment se débarrasser des réseaux dans Docker

Tout comme les autres objets logiques dans Docker, les réseaux peuvent être supprimés en utilisant la commande `network rm`. La syntaxe générique de la commande est la suivante :

```
docker network rm <identifiant du réseau>
```

Pour supprimer le réseau `skynet` de votre système, vous pouvez exécuter la commande suivante :

```
docker network rm skynet
```

Vous pouvez également utiliser la commande `network prune` pour supprimer tout réseau inutilisé de votre système. La commande dispose également des options `-f` ou `--force` et `-a` ou `--all`.

## Comment conteneuriser une application JavaScript multi-conteneurs

Maintenant que vous avez appris suffisamment sur les réseaux dans Docker, dans cette section, vous apprendrez à conteneuriser un projet multi-conteneurs complet. Le projet sur lequel vous travaillerez est une simple `notes-api` alimentée par Express.js et PostgreSQL.

Dans ce projet, il y a deux conteneurs au total que vous devrez connecter en utilisant un réseau. En plus de cela, vous apprendrez également des concepts comme les variables d'environnement et les volumes nommés. Alors sans plus attendre, plongeons directement.

### Comment exécuter le serveur de base de données

Le serveur de base de données de ce projet est un simple serveur PostgreSQL et utilise l'image officielle [postgres](https://hub.docker.com/_/postgres).

Selon la documentation officielle, afin d'exécuter un conteneur avec cette image, vous devez fournir la variable d'environnement `POSTGRES_PASSWORD`. En plus de celle-ci, je vais également fournir un nom pour la base de données par défaut en utilisant la variable d'environnement `POSTGRES_DB`. PostgreSQL écoute par défaut sur le port `5432`, vous devez donc le publier également.

Pour exécuter le serveur de base de données, vous pouvez exécuter la commande suivante :

```
docker container run \
    --detach \
    --name=notes-db \
    --env POSTGRES_DB=notesdb \
    --env POSTGRES_PASSWORD=secret \
    --network=notes-api-network \
    postgres:12

# a7b287d34d96c8e81a63949c57b83d7c1d71b5660c87f5172f074bd1606196dc

docker container ls

# CONTAINER ID   IMAGE         COMMAND                  CREATED              STATUS              PORTS      NAMES
# a7b287d34d96   postgres:12   "docker-entrypoint.s"   About a minute ago   Up About a minute   5432/tcp   notes-db
```

L'option `--env` pour les commandes `container run` et `container create` peut être utilisée pour fournir des variables d'environnement à un conteneur. Comme vous pouvez le voir, le conteneur de base de données a été créé avec succès et est en cours d'exécution maintenant.

Bien que le conteneur soit en cours d'exécution, il y a un petit problème. Les bases de données comme PostgreSQL, MongoDB et MySQL persistent leurs données dans un répertoire. PostgreSQL utilise le répertoire `/var/lib/postgresql/data` à l'intérieur du conteneur pour persister les données.

Maintenant, que se passe-t-il si le conteneur est détruit pour une raison quelconque ? Vous perdrez toutes vos données. Pour résoudre ce problème, un volume nommé peut être utilisé.

### Comment travailler avec des volumes nommés dans Docker

Précédemment, vous avez travaillé avec des montages de liaison et des volumes anonymes. Un volume nommé est très similaire à un volume anonyme sauf que vous pouvez faire référence à un volume nommé en utilisant son nom.

Les volumes sont également des objets logiques dans Docker et peuvent être manipulés en utilisant la ligne de commande. La commande `volume create` peut être utilisée pour créer un volume nommé.

La syntaxe générique de la commande est la suivante :

```
docker volume create <nom du volume>
```

Pour créer un volume nommé `notes-db-data`, vous pouvez exécuter la commande suivante :

```
docker volume create notes-db-data

# notes-db-data

docker volume ls

# DRIVER    VOLUME NAME
# local     notes-db-data
```

Ce volume peut maintenant être monté sur `/var/lib/postgresql/data` à l'intérieur du conteneur `notes-db`. Pour ce faire, arrêtez et supprimez le conteneur `notes-db` :

```
docker container stop notes-db

# notes-db

docker container rm notes-db

# notes-db
```

Maintenant, exécutez un nouveau conteneur et attribuez le volume en utilisant l'option `--volume` ou `-v`.

```
docker container run \
    --detach \
    --volume notes-db-data:/var/lib/postgresql/data \
    --name=notes-db \
    --env POSTGRES_DB=notesdb \
    --env POSTGRES_PASSWORD=secret \
    --network=notes-api-network \
    postgres:12

# 37755e86d62794ed3e67c19d0cd1eba431e26ab56099b92a3456908c1d346791
```

Maintenant, inspectez le conteneur `notes-db` pour vous assurer que le montage a réussi :

```
docker container inspect --format='{{range .Mounts}} {{ .Name }} {{end}}' notes-db

#  notes-db-data
```

Maintenant, les données seront stockées en toute sécurité dans le volume `notes-db-data` et pourront être réutilisées à l'avenir. Un montage de liaison peut également être utilisé au lieu d'un volume nommé ici, mais je préfère un volume nommé dans de tels scénarios.

### Comment accéder aux journaux depuis un conteneur dans Docker

Afin de voir les journaux d'un conteneur, vous pouvez utiliser la commande `container logs`. La syntaxe générique de la commande est la suivante :

```
docker container logs <identifiant du conteneur>
```

Pour accéder aux journaux du conteneur `notes-db`, vous pouvez exécuter la commande suivante :

```
docker container logs notes-db

# The files belonging to this database system will be owned by user "postgres".
# This user must also own the server process.

# The database cluster will be initialized with locale "en_US.utf8".
# The default database encoding has accordingly been set to "UTF8".
# The default text search configuration will be set to "english".
#
# Data page checksums are disabled.
#
# fixing permissions on existing directory /var/lib/postgresql/data ... ok
# creating subdirectories ... ok
# selecting dynamic shared memory implementation ... posix
# selecting default max_connections ... 100
# selecting default shared_buffers ... 128MB
# selecting default time zone ... Etc/UTC
# creating configuration files ... ok
# running bootstrap script ... ok
# performing post-bootstrap initialization ... ok
# syncing data to disk ... ok
#
#
# Success. You can now start the database server using:
#
#     pg_ctl -D /var/lib/postgresql/data -l logfile start
#
# initdb: warning: enabling "trust" authentication for local connections
# You can change this by editing pg_hba.conf or using the option -A, or
# --auth-local and --auth-host, the next time you run initdb.
# waiting for server to start....2021-01-25 13:39:21.613 UTC [47] LOG:  starting PostgreSQL 12.5 (Debian 12.5-1.pgdg100+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 8.3.0-6) 8.3.0, 64-bit
# 2021-01-25 13:39:21.621 UTC [47] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
# 2021-01-25 13:39:21.675 UTC [48] LOG:  database system was shut down at 2021-01-25 13:39:21 UTC
# 2021-01-25 13:39:21.685 UTC [47] LOG:  database system is ready to accept connections
#  done
# server started
# CREATE DATABASE
#
#
# /usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*
#
# 2021-01-25 13:39:22.008 UTC [47] LOG:  received fast shutdown request
# waiting for server to shut down....2021-01-25 13:39:22.015 UTC [47] LOG:  aborting any active transactions
# 2021-01-25 13:39:22.017 UTC [47] LOG:  background worker "logical replication launcher" (PID 54) exited with exit code 1
# 2021-01-25 13:39:22.017 UTC [49] LOG:  shutting down
# 2021-01-25 13:39:22.056 UTC [47] LOG:  database system is shut down
#  done
# server stopped
#
# PostgreSQL init process complete; ready for start up.
#
# 2021-01-25 13:39:22.135 UTC [1] LOG:  starting PostgreSQL 12.5 (Debian 12.5-1.pgdg100+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 8.3.0-6) 8.3.0, 64-bit
# 2021-01-25 13:39:22.136 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
# 2021-01-25 13:39:22.136 UTC [1] LOG:  listening on IPv6 address "::", port 5432
# 2021-01-25 13:39:22.147 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
# 2021-01-25 13:39:22.177 UTC [75] LOG:  database system was shut down at 2021-01-25 13:39:22 UTC
# 2021-01-25 13:39:22.190 UTC [1] LOG:  database system is ready to accept connections
```

Comme l'indique le texte à la ligne 57, la base de données est opérationnelle et prête à accepter les connexions de l'extérieur. Il existe également l'option `--follow` ou `-f` pour la commande qui vous permet d'attacher la console à la sortie des journaux et d'obtenir un flux continu de texte.

### Comment créer un réseau et attacher le serveur de base de données dans Docker

Comme vous l'avez appris dans la section précédente, les conteneurs doivent être attachés à un réseau de pont défini par l'utilisateur afin de communiquer entre eux en utilisant les noms des conteneurs. Pour ce faire, créez un réseau nommé `notes-api-network` dans votre système :

```
docker network create notes-api-network
```

Maintenant, attachez le conteneur `notes-db` à ce réseau en exécutant la commande suivante :

```
docker network connect notes-api-network notes-db
```

### Comment écrire le Dockerfile

Allez dans le répertoire où vous avez cloné le code du projet. À l'intérieur, allez dans le répertoire `notes-api/api`, et créez un nouveau `Dockerfile`. Mettez le code suivant dans le fichier :

```
# stage one
FROM node:lts-alpine as builder

# install dependencies for node-gyp
RUN apk add --no-cache python make g++

WORKDIR /app

COPY ./package.json .
RUN npm install --only=prod

# stage two
FROM node:lts-alpine

EXPOSE 3000
ENV NODE_ENV=production

USER node
RUN mkdir -p /home/node/app
WORKDIR /home/node/app

COPY . .
COPY --from=builder /app/node_modules  /home/node/app/node_modules

CMD [ "node", "bin/www" ]
```

Il s'agit d'une construction multi-étapes. La première étape est utilisée pour construire et installer les dépendances en utilisant `node-gyp` et la deuxième étape est pour exécuter l'application. Je vais passer brièvement en revue les étapes :

* L'étape 1 utilise `node:lts-alpine` comme base et utilise `builder` comme nom de l'étape.
* À la ligne 5, nous installons `python`, `make` et `g++`. L'outil `node-gyp` nécessite ces trois packages pour fonctionner.
* À la ligne 7, nous définissons le répertoire `/app` comme `WORKDIR`.
* Aux lignes 9 et 10, nous copions le fichier `package.json` dans le `WORKDIR` et installons toutes les dépendances.
* L'étape 2 utilise également `node-lts:alpine` comme base.
* À la ligne 16, nous définissons la variable d'environnement `NODE_ENV` sur `production`. Cela est important pour que l'API fonctionne correctement.
* Des lignes 18 à 20, nous définissons l'utilisateur par défaut sur `node`, créons le répertoire `/home/node/app` et définissons celui-ci comme `WORKDIR`.
* À la ligne 22, nous copions tous les fichiers du projet et à la ligne 23, nous copions le répertoire `node_modules` de l'étape `builder`. Ce répertoire contient toutes les dépendances construites nécessaires pour exécuter l'application.
* À la ligne 25, nous définissons la commande par défaut.

Pour construire une image à partir de ce `Dockerfile`, vous pouvez exécuter la commande suivante :

```
docker image build --tag notes-api .

# Sending build context to Docker daemon  37.38kB
# Step 1/14 : FROM node:lts-alpine as builder
#  ---> 471e8b4eb0b2
# Step 2/14 : RUN apk add --no-cache python make g++
#  ---> Running in 5f20a0ecc04b
# fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/main/x86_64/APKINDEX.tar.gz
# fetch http://dl-cdn.alpinelinux.org/alpine/v3.11/community/x86_64/APKINDEX.tar.gz
# (1/21) Installing binutils (2.33.1-r0)
# (2/21) Installing gmp (6.1.2-r1)
# (3/21) Installing isl (0.18-r0)
# (4/21) Installing libgomp (9.3.0-r0)
# (5/21) Installing libatomic (9.3.0-r0)
# (6/21) Installing mpfr4 (4.0.2-r1)
# (7/21) Installing mpc1 (1.1.0-r1)
# (8/21) Installing gcc (9.3.0-r0)
# (9/21) Installing musl-dev (1.1.24-r3)
# (10/21) Installing libc-dev (0.7.2-r0)
# (11/21) Installing g++ (9.3.0-r0)
# (12/21) Installing make (4.2.1-r2)
# (13/21) Installing libbz2 (1.0.8-r1)
# (14/21) Installing expat (2.2.9-r1)
# (15/21) Installing libffi (3.2.1-r6)
# (16/21) Installing gdbm (1.13-r1)
# (17/21) Installing ncurses-terminfo-base (6.1_p20200118-r4)
# (18/21) Installing ncurses-libs (6.1_p20200118-r4)
# (19/21) Installing readline (8.0.1-r0)
# (20/21) Installing sqlite-libs (3.30.1-r2)
# (21/21) Installing python2 (2.7.18-r0)
# Executing busybox-1.31.1-r9.trigger
# OK: 212 MiB in 37 packages
# Removing intermediate container 5f20a0ecc04b
#  ---> 637ca797d709
# Step 3/14 : WORKDIR /app
#  ---> Running in 846361b57599
# Removing intermediate container 846361b57599
#  ---> 3d58a482896e
# Step 4/14 : COPY ./package.json .
#  ---> 11b387794039
# Step 5/14 : RUN npm install --only=prod
#  ---> Running in 2e27e33f935d
#  added 269 packages from 220 contributors and audited 1137 packages in 140.322s
#
# 4 packages are looking for funding
#   run `npm fund` for details
#
# found 0 vulnerabilities
#
# Removing intermediate container 2e27e33f935d
#  ---> eb7cb2cb0b20
# Step 6/14 : FROM node:lts-alpine
#  ---> 471e8b4eb0b2
# Step 7/14 : EXPOSE 3000
#  ---> Running in 4ea24f871747
# Removing intermediate container 4ea24f871747
#  ---> 1f0206f2f050
# Step 8/14 : ENV NODE_ENV=production
#  ---> Running in 5d40d6ac3b7e
# Removing intermediate container 5d40d6ac3b7e
#  ---> 31f62da17929
# Step 9/14 : USER node
#  ---> Running in 0963e1fb19a0
# Removing intermediate container 0963e1fb19a0
#  ---> 0f4045152b1c
# Step 10/14 : RUN mkdir -p /home/node/app
#  ---> Running in 0ac591b3adbd
# Removing intermediate container 0ac591b3adbd
#  ---> 5908373dfc75
# Step 11/14 : WORKDIR /home/node/app
#  ---> Running in 55253b62ff57
# Removing intermediate container 55253b62ff57
#  ---> 2883cdb7c77a
# Step 12/14 : COPY . .
#  ---> 8e60893a7142
# Step 13/14 : COPY --from=builder /app/node_modules  /home/node/app/node_modules
#  ---> 27a85faa4342
# Step 14/14 : CMD [ "node", "bin/www" ]
#  ---> Running in 349c8ca6dd3e
# Removing intermediate container 349c8ca6dd3e
#  ---> 9ea100571585
# Successfully built 9ea100571585
# Successfully tagged notes-api:latest
```

Avant d'exécuter un conteneur en utilisant cette image, assurez-vous que le conteneur de base de données est en cours d'exécution et est attaché au `notes-api-network`.

```
docker container inspect notes-db

# [
#     {
#         ...
#         "State": {
#             "Status": "running",
#             "Running": true,
#             "Paused": false,
#             "Restarting": false,
#             "OOMKilled": false,
#             "Dead": false,
#             "Pid": 11521,
#             "ExitCode": 0,
#             "Error": "",
#             "StartedAt": "2021-01-26T06:55:44.928510218Z",
#             "FinishedAt": "2021-01-25T14:19:31.316854657Z"
#         },
#         ...
#         "Mounts": [
#             {
#                 "Type": "volume",
#                 "Name": "notes-db-data",
#                 "Source": "/var/lib/docker/volumes/notes-db-data/_data",
#                 "Destination": "/var/lib/postgresql/data",
#                 "Driver": "local",
#                 "Mode": "z",
#                 "RW": true,
#                 "Propagation": ""
#             }
#         ],
#         ...
#         "NetworkSettings": {
#             ...
#             "Networks": {
#                 "bridge": {
#                     "IPAMConfig": null,
#                     "Links": null,
#                     "Aliases": null,
#                     "NetworkID": "e4c7ce50a5a2a49672155ff498597db336ecc2e3bbb6ee8baeebcf9fcfa0e1ab",
#                     "EndpointID": "2a2587f8285fa020878dd38bdc630cdfca0d769f76fc143d1b554237ce907371",
#                     "Gateway": "172.17.0.1",
#                     "IPAddress": "172.17.0.2",
#                     "IPPrefixLen": 16,
#                     "IPv6Gateway": "",
#                     "GlobalIPv6Address": "",
#                     "GlobalIPv6PrefixLen": 0,
#                     "MacAddress": "02:42:ac:11:00:02",
#                     "DriverOpts": null
#                 },
#                 "notes-api-network": {
#                     "IPAMConfig": {},
#                     "Links": null,
#                     "Aliases": [
#                         "37755e86d627"
#                     ],
#                     "NetworkID": "06579ad9f93d59fc3866ac628ed258dfac2ed7bc1a9cd6fe6e67220b15d203ea",
#                     "EndpointID": "5b8f8718ec9a5ec53e7a13cce3cb540fdf3556fb34242362a8da4cc08d37223c",
#                     "Gateway": "172.18.0.1",
#                     "IPAddress": "172.18.0.2",
#                     "IPPrefixLen": 16,
#                     "IPv6Gateway": "",
#                     "GlobalIPv6Address": "",
#                     "GlobalIPv6PrefixLen": 0,
#                     "MacAddress": "02:42:ac:12:00:02",
#                     "DriverOpts": {}
#                 }
#             }
#         }
#     }
# ]

```

J'ai raccourci la sortie pour une visualisation facile ici. Sur mon système, le conteneur `notes-db` est en cours d'exécution, utilise le volume `notes-db-data` et est attaché au pont `notes-api-network`.

Une fois que vous êtes assuré que tout est en place, vous pouvez exécuter un nouveau conteneur en exécutant la commande suivante :

```
docker container run \
    --detach \
    --name=notes-api \
    --env DB_HOST=notes-db \
    --env DB_DATABASE=notesdb \
    --env DB_PASSWORD=secret \
    --publish=3000:3000 \
    --network=notes-api-network \
    notes-api
    
# f9ece420872de99a060b954e3c236cbb1e23d468feffa7fed1e06985d99fb919
```

Vous devriez être capable de comprendre cette longue commande par vous-même, donc je vais passer brièvement en revue les variables d'environnement.

L'application `notes-api` nécessite que trois variables d'environnement soient définies. Elles sont les suivantes :

* `DB_HOST` - Il s'agit de l'hôte du serveur de base de données. Étant donné que le serveur de base de données et l'API sont attachés au même réseau de pont défini par l'utilisateur, le serveur de base de données peut être référencé en utilisant son nom de conteneur qui est `notes-db` dans ce cas.
* `DB_DATABASE` - La base de données que cette API utilisera. Dans [Exécuter le serveur de base de données](https://www.freecodecamp.org/news/@fhsinchy/s/the-docker-handbook/~/drafts/-MS2MtB5zjVVjK3Ujaz4/containerizing-a-multi-container-javascript-application#running-the-database-server), nous avons défini le nom de la base de données par défaut sur `notesdb` en utilisant la variable d'environnement `POSTGRES_DB`. Nous allons l'utiliser ici.
* `DB_PASSWORD` - Mot de passe pour se connecter à la base de données. Cela a également été défini dans la sous-section [Exécuter le serveur de base de données](https://www.freecodecamp.org/news/@fhsinchy/s/the-docker-handbook/~/drafts/-MS2MtB5zjVVjK3Ujaz4/containerizing-a-multi-container-javascript-application#running-the-database-server) en utilisant la variable d'environnement `POSTGRES_PASSWORD`.

Pour vérifier si le conteneur fonctionne correctement ou non, vous pouvez utiliser la commande `container ls` :

```
docker container ls

# CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS          PORTS                    NAMES
# f9ece420872d   notes-api     "docker-entrypoint.s"   12 minutes ago   Up 12 minutes   0.0.0.0:3000->3000/tcp   notes-api
# 37755e86d627   postgres:12   "docker-entrypoint.s"   17 hours ago     Up 14 minutes   5432/tcp                 notes-db
```

Le conteneur est en cours d'exécution maintenant. Vous pouvez visiter `http://127.0.0.1:3000/` pour voir l'API en action.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/bonjour-mon-ami.png)

L'API a cinq routes au total que vous pouvez voir dans le fichier `/notes-api/api/api/routes/notes.js`.

Bien que le conteneur soit en cours d'exécution, il y a une dernière chose que vous devrez faire avant de pouvoir commencer à l'utiliser. Vous devrez exécuter la migration de la base de données nécessaire pour configurer les tables de la base de données, et vous pouvez le faire en exécutant la commande `npm run db:migrate` à l'intérieur du conteneur.

### Comment exécuter des commandes dans un conteneur en cours d'exécution

Vous avez déjà appris à exécuter des commandes dans un conteneur arrêté. Un autre scénario est l'exécution d'une commande à l'intérieur d'un conteneur en cours d'exécution.

Pour cela, vous devrez utiliser la commande `exec` pour exécuter une commande personnalisée à l'intérieur d'un conteneur en cours d'exécution.

La syntaxe générique de la commande `exec` est la suivante :

```
docker container exec <identifiant du conteneur> <commande>
```

Pour exécuter `npm run db:migrate` à l'intérieur du conteneur `notes-api`, vous pouvez exécuter la commande suivante :

```
docker container exec notes-api npm run db:migrate

# > notes-api@ db:migrate /home/node/app
# > knex migrate:latest
#
# Using environment: production
# Batch 1 run: 1 migrations
```

Dans les cas où vous souhaitez exécuter une commande interactive à l'intérieur d'un conteneur en cours d'exécution, vous devrez utiliser le drapeau `-it`. Par exemple, si vous souhaitez accéder au shell en cours d'exécution à l'intérieur du conteneur `notes-api`, vous pouvez exécuter la commande suivante :

```
docker container exec -it notes-api sh

# / # uname -a
# Linux b5b1367d6b31 5.10.9-201.fc33.x86_64 #1 SMP Wed Jan 20 16:56:23 UTC 2021 x86_64 Linux
```

### Comment écrire des scripts de gestion dans Docker

Gérer un projet multi-conteneurs avec le réseau et les volumes et autres signifie écrire beaucoup de commandes. Pour simplifier le processus, j'ai généralement de l'aide de simples [scripts shell](https://opensource.com/article/17/1/getting-started-shell-scripting) et un [Makefile](https://opensource.com/article/18/8/what-how-makefile).

Vous trouverez quatre scripts shell dans le répertoire `notes-api`. Ils sont les suivants :

* `boot.sh` - Utilisé pour démarrer les conteneurs s'ils existent déjà.
* `build.sh` - Crée et exécute les conteneurs. Il crée également les images, les volumes et les réseaux si nécessaire.
* `destroy.sh` - Supprime tous les conteneurs, volumes et réseaux associés à ce projet.
* `stop.sh` - Arrête tous les conteneurs en cours d'exécution.

Il y a aussi un `Makefile` qui contient quatre cibles nommées `start`, `stop`, `build` et `destroy`, chacune invoquant les scripts shell mentionnés précédemment.

Si le conteneur est en cours d'exécution dans votre système, l'exécution de `make stop` devrait arrêter tous les conteneurs. L'exécution de `make destroy` devrait arrêter les conteneurs et tout supprimer. Assurez-vous d'exécuter les scripts à l'intérieur du répertoire `notes-api` :

```
make destroy

# ./shutdown.sh
# stopping api container --->
# notes-api
# api container stopped --->

# stopping db container --->
# notes-db
# db container stopped --->

# shutdown script finished

# ./destroy.sh
# removing api container --->
# notes-api
# api container removed --->

# removing db container --->
# notes-db
# db container removed --->

# removing db data volume --->
# notes-db-data
# db data volume removed --->

# removing network --->
# notes-api-network
# network removed --->

# destroy script finished
```

Si vous obtenez une erreur de permission refusée, exécutez `chmod +x` sur les scripts :

```
chmod +x boot.sh build.sh destroy.sh shutdown.sh
```

Je ne vais pas expliquer ces scripts car ce sont des instructions `if-else` simples avec quelques commandes Docker que vous avez déjà vues de nombreuses fois. Si vous avez une certaine compréhension du shell Linux, vous devriez être en mesure de comprendre les scripts également.

## Comment composer des projets en utilisant Docker-Compose

Dans la section précédente, vous avez appris à gérer un projet multi-conteneurs et les difficultés qui y sont associées. Au lieu d'écrire autant de commandes, il existe une manière plus facile de gérer les projets multi-conteneurs, un outil appelé [Docker Compose](https://docs.docker.com/compose/).

Selon la documentation Docker [documentation](https://docs.docker.com/compose/) -

> Compose est un outil pour définir et exécuter des applications Docker multi-conteneurs. Avec Compose, vous utilisez un fichier YAML pour configurer les services de votre application. Ensuite, avec une seule commande, vous créez et démarrez tous les services à partir de votre configuration.

Bien que Compose fonctionne dans tous les environnements, il est plus axé sur le développement et les tests. L'utilisation de Compose dans un environnement de production n'est pas du tout recommandée.

### Bases de Docker Compose

Allez dans le répertoire où vous avez cloné le dépôt qui accompagne ce livre. Allez dans le répertoire `notes-api/api` et créez un fichier `Dockerfile.dev`. Mettez le code suivant dedans :

```dockerfile
# stage one
FROM node:lts-alpine as builder

# install dependencies for node-gyp
RUN apk add --no-cache python make g++

WORKDIR /app

COPY ./package.json .
RUN npm install

# stage two
FROM node:lts-alpine

ENV NODE_ENV=development

USER node
RUN mkdir -p /home/node/app
WORKDIR /home/node/app

COPY . .
COPY --from=builder /app/node_modules /home/node/app/node_modules

CMD [ "./node_modules/.bin/nodemon", "--config", "nodemon.json", "bin/www" ]
```

Le code est presque identique au `Dockerfile` avec lequel vous avez travaillé dans la section précédente. Les trois différences dans ce fichier sont les suivantes :

* À la ligne 10, nous exécutons `npm install` au lieu de `npm run install --only=prod` car nous voulons également les dépendances de développement.
* À la ligne 15, nous définissons la variable d'environnement `NODE_ENV` sur `development` au lieu de `production`.
* À la ligne 24, nous utilisons un outil appelé [nodemon](https://nodemon.io/) pour obtenir la fonction de rechargement à chaud pour l'API.

Vous savez déjà que ce projet a deux conteneurs :

* `notes-db` - Un serveur de base de données alimenté par PostgreSQL.
* `notes-api` - Une API REST alimentée par Express.js

Dans le monde de Compose, chaque conteneur qui compose l'application est connu sous le nom de service. La première étape pour composer un projet multi-conteneurs est de définir ces services.

Tout comme le démon Docker utilise un `Dockerfile` pour construire des images, Docker Compose utilise un fichier `docker-compose.yaml` pour lire les définitions de service.

Rendez-vous dans le répertoire `notes-api` et créez un nouveau fichier `docker-compose.yaml`. Mettez le code suivant dans le fichier nouvellement créé :

```yaml
version: "3.8"

services: 
    db:
        image: postgres:12
        container_name: notes-db-dev
        volumes: 
            - notes-db-dev-data:/var/lib/postgresql/data
        environment:
            POSTGRES_DB: notesdb
            POSTGRES_PASSWORD: secret
    api:
        build:
            context: ./api
            dockerfile: Dockerfile.dev
        image: notes-api:dev
        container_name: notes-api-dev
        environment: 
            DB_HOST: db ## same as the database service name
            DB_DATABASE: notesdb
            DB_PASSWORD: secret
        volumes: 
            - /home/node/app/node_modules
            - ./api:/home/node/app
        ports: 
            - 3000:3000

volumes:
    notes-db-dev-data:
        name: notes-db-dev-data
```

Tout fichier `docker-compose.yaml` valide commence par définir la version du fichier. Au moment de l'écriture, `3.8` est la dernière version. Vous pouvez consulter la dernière version [ici](https://docs.docker.com/compose/compose-file/).

Les blocs dans un fichier YAML sont définis par l'indentation. Je vais passer en revue chacun des blocs et expliquer ce qu'ils font.

* Le bloc `services` contient les définitions de chacun des services ou conteneurs de l'application. `db` et `api` sont les deux services qui composent ce projet.
* Le bloc `db` définit un nouveau service dans l'application et contient les informations nécessaires pour démarrer le conteneur. Chaque service nécessite soit une image pré-construite, soit un `Dockerfile` pour exécuter un conteneur. Pour le service `db`, nous utilisons l'image officielle PostgreSQL.
* Contrairement au service `db`, une image pré-construite pour le service `api` n'existe pas. Nous allons donc utiliser le fichier `Dockerfile.dev`.
* Le bloc `volumes` définit tout volume nommé nécessaire pour l'un des services. À ce moment-là, il ne répertorie que le volume `notes-db-dev-data` utilisé par le service `db`.

Maintenant que vous avez une vue d'ensemble de haut niveau du fichier `docker-compose.yaml`, examinons de plus près les services individuels.

Le code de définition du service `db` est le suivant :

```yaml
db:
    image: postgres:12
    container_name: notes-db-dev
    volumes: 
        - db-data:/var/lib/postgresql/data
    environment:
        POSTGRES_DB: notesdb
        POSTGRES_PASSWORD: secret
```

* La clé `image` contient le dépôt et le tag de l'image utilisés pour ce conteneur. Nous utilisons l'image `postgres:12` pour exécuter le conteneur de base de données.
* Le `container_name` indique le nom du conteneur. Par défaut, les conteneurs sont nommés selon la syntaxe `<nom du répertoire du projet>_<nom du service>`. Vous pouvez remplacer cela en utilisant `container_name`.
* Le tableau `volumes` contient les mappages de volumes pour le service et prend en charge les volumes nommés, les volumes anonymes et les montages de liaison. La syntaxe `<source>:<destination>` est identique à ce que vous avez vu précédemment.
* La carte `environment` contient les valeurs des différentes variables d'environnement nécessaires pour le service.

Le code de définition du service `api` est le suivant :

```yaml
api:
    build:
        context: ./api
        dockerfile: Dockerfile.dev
    image: notes-api:dev
    container_name: notes-api-dev
    environment: 
        DB_HOST: db ## same as the database service name
        DB_DATABASE: notesdb
        DB_PASSWORD: secret
    volumes: 
        - /home/node/app/node_modules
        - ./api:/home/node/app
    ports: 
        - 3000:3000
```

* Le service `api` ne vient pas avec une image pré-construite. Au lieu de cela, il a une configuration de construction. Sous le bloc `build`, nous définissons le contexte et le nom du Dockerfile pour construire une image. Vous devriez avoir une compréhension du contexte et du Dockerfile maintenant, donc je ne passerai pas de temps à les expliquer.
* La clé `image` contient le nom de l'image à construire. Si elle n'est pas assignée, l'image sera nommée selon la syntaxe `<nom du répertoire du projet>_<nom du service>`.
* Dans la carte `environment`, la variable `DB_HOST` démontre une fonctionnalité de Compose. C'est-à-dire que vous pouvez faire référence à un autre service dans la même application en utilisant son nom. Donc le `db` ici sera remplacé par l'adresse IP du conteneur du service `api`. Les variables `DB_DATABASE` et `DB_PASSWORD` doivent correspondre respectivement à `POSTGRES_DB` et `POSTGRES_PASSWORD` de la définition du service `db`.
* Dans la carte `volumes`, vous pouvez voir un volume anonyme et un montage de liaison décrits. La syntaxe est identique à ce que vous avez vu dans les sections précédentes.
* La carte `ports` définit tout mappage de port. La syntaxe, `<port hôte>:<port conteneur>` est identique à l'option `--publish` que vous avez utilisée auparavant.

Enfin, le code pour les `volumes` est le suivant :

```yaml
volumes:
    db-data:
        name: notes-db-dev-data
```

Tout volume nommé utilisé dans l'un des services doit être défini ici. Si vous ne définissez pas de nom, le volume sera nommé selon la syntaxe `<nom du répertoire du projet>_<clé du volume>` et la clé ici est `db-data`.

Vous pouvez en savoir plus sur les différentes options de configuration des volumes dans la documentation officielle [docs](https://docs.docker.com/compose/compose-file/compose-file-v3/#volumes).

### Comment démarrer les services dans Docker Compose

Il existe quelques façons de démarrer les services définis dans un fichier YAML. La première commande que vous apprendrez est la commande `up`. La commande `up` construit les images manquantes, crée des conteneurs et les démarre en une seule fois.

Avant d'exécuter la commande, assurez-vous d'avoir ouvert votre terminal dans le même répertoire où se trouve le fichier `docker-compose.yaml`. Cela est très important pour chaque commande `docker-compose` que vous exécutez.

```
docker-compose --file docker-compose.yaml up --detach

# Creating network "notes-api_default" with the default driver
# Creating volume "notes-db-dev-data" with default driver
# Building api
# Sending build context to Docker daemon  37.38kB
#
# Step 1/13 : FROM node:lts-alpine as builder
#  ---> 471e8b4eb0b2
# Step 2/13 : RUN apk add --no-cache python make g++
#  ---> Running in 197056ec1964
### LONG INSTALLATION STUFF GOES HERE ###
# Removing intermediate container 197056ec1964
#  ---> 6609935fe50b
# Step 3/13 : WORKDIR /app
#  ---> Running in 17010f65c5e7
# Removing intermediate container 17010f65c5e7
#  ---> b10d12e676ad
# Step 4/13 : COPY ./package.json .
#  ---> 600d31d9362e
# Step 5/13 : RUN npm install
#  ---> Running in a14afc8c0743
### LONG INSTALLATION STUFF GOES HERE ###
#  Removing intermediate container a14afc8c0743
#  ---> 952d5d86e361
# Step 6/13 : FROM node:lts-alpine
#  ---> 471e8b4eb0b2
# Step 7/13 : ENV NODE_ENV=development
#  ---> Using cache
#  ---> b7c12361b3e5
# Step 8/13 : USER node
#  ---> Using cache
#  ---> f5ac66ca07a4
# Step 9/13 : RUN mkdir -p /home/node/app
#  ---> Using cache
#  ---> 60094b9a6183
# Step 10/13 : WORKDIR /home/node/app
#  ---> Using cache
#  ---> 316a252e6e3e
# Step 11/13 : COPY . .
#  ---> Using cache
#  ---> 3a083622b753
# Step 12/13 : COPY --from=builder /app/node_modules /home/node/app/node_modules
#  ---> Using cache
#  ---> 707979b3371c
# Step 13/13 : CMD [ "./node_modules/.bin/nodemon", "--config", "nodemon.json", "bin/www" ]
#  ---> Using cache
#  ---> f2da08a5f59b
# Successfully built f2da08a5f59b
# Successfully tagged notes-api:dev
# Creating notes-api-dev ... done
# Creating notes-db-dev  ... done
```

L'option `--detach` ou `-d` ici fonctionne de la même manière que celle que vous avez vue précédemment. L'option `--file` ou `-f` n'est nécessaire que si le fichier YAML n'est pas nommé `docker-compose.yaml` (mais je l'ai utilisée ici à des fins de démonstration).

En plus de la commande `up`, il y a la commande `start`. La principale différence entre ces deux commandes est que la commande `start` ne crée pas de conteneurs manquants, elle ne démarre que les conteneurs existants. C'est essentiellement la même chose que la commande `container start`.

L'option `--build` pour la commande `up` force une reconstruction des images. Il existe d'autres options pour la commande `up` que vous pouvez voir dans la documentation officielle [docs](https://docs.docker.com/compose/reference/up/).

### Comment lister les services dans Docker Compose

Bien que les conteneurs de service démarrés par Compose puissent être listés en utilisant la commande `container ls`, il y a la commande `ps` pour lister uniquement les conteneurs définis dans le YAML.

```
docker-compose ps

#     Name                   Command               State           Ports         
# -------------------------------------------------------------------------------
# notes-api-dev   docker-entrypoint.sh ./nod ...   Up      0.0.0.0:3000->3000/tcp
# notes-db-dev    docker-entrypoint.sh postgres    Up      5432/tcp
```

Ce n'est pas aussi informatif que la sortie de `container ls`, mais c'est utile lorsque vous avez des tonnes de conteneurs en cours d'exécution simultanément.

### Comment exécuter des commandes à l'intérieur d'un service en cours d'exécution dans Docker Compose

J'espère que vous vous souvenez de la section précédente que vous devez exécuter certains scripts de migration pour créer les tables de la base de données pour cette API.

Tout comme la commande `container exec`, il y a une commande `exec` pour `docker-compose`. La syntaxe générique de la commande est la suivante :

```
docker-compose exec <nom du service> <commande>
```

Pour exécuter la commande `npm run db:migrate` à l'intérieur du service `api`, vous pouvez exécuter la commande suivante :

```
docker-compose exec api npm run db:migrate

# > notes-api@ db:migrate /home/node/app
# > knex migrate:latest
# 
# Using environment: development
# Batch 1 run: 1 migrations
```

Contrairement à la commande `container exec`, vous n'avez pas besoin de passer le drapeau `-it` pour les sessions interactives. `docker-compose` le fait automatiquement.

### Comment accéder aux journaux d'un service en cours d'exécution dans Docker Compose

Vous pouvez également utiliser la commande `logs` pour récupérer les journaux d'un service en cours d'exécution. La syntaxe générique de la commande est la suivante :

```
docker-compose logs <nom du service>
```

Pour accéder aux journaux du service `api`, exécutez la commande suivante :

```
docker-compose logs api

# Attaching to notes-api-dev
# notes-api-dev | [nodemon] 2.0.7
# notes-api-dev | [nodemon] reading config ./nodemon.json
# notes-api-dev | [nodemon] to restart at any time, enter `rs`
# notes-api-dev | [nodemon] or send SIGHUP to 1 to restart
# notes-api-dev | [nodemon] ignoring: *.test.js
# notes-api-dev | [nodemon] watching path(s): *.*
# notes-api-dev | [nodemon] watching extensions: js,mjs,json
# notes-api-dev | [nodemon] starting `node bin/www`
# notes-api-dev | [nodemon] forking
# notes-api-dev | [nodemon] child pid: 19
# notes-api-dev | [nodemon] watching 18 files
# notes-api-dev | app running -> http://127.0.0.1:3000
```

Ceci n'est qu'une partie de la sortie des journaux. Vous pouvez vous accrocher à la sortie du flux du service et obtenir les journaux en temps réel en utilisant l'option `-f` ou `--follow`. Tout journal ultérieur apparaîtra instantanément dans le terminal tant que vous ne quitterez pas en appuyant sur `ctrl + c` ou en fermant la fenêtre. Le conteneur continuera à s'exécuter même si vous quittez la fenêtre des journaux.

### Comment arrêter les services dans Docker Compose

Pour arrêter les services, il y a deux approches que vous pouvez adopter. La première est la commande `down`. La commande `down` arrête tous les conteneurs en cours d'exécution et les supprime du système. Elle supprime également tous les réseaux :

```
docker-compose down --volumes

# Stopping notes-api-dev ... done
# Stopping notes-db-dev  ... done
# Removing notes-api-dev ... done
# Removing notes-db-dev  ... done
# Removing network notes-api_default
# Removing volume notes-db-dev-data
```

L'option `--volumes` indique que vous souhaitez supprimer tout volume nommé défini dans le bloc `volumes`. Vous pouvez en savoir plus sur les options supplémentaires de la commande `down` dans la documentation officielle [docs](https://docs.docker.com/compose/reference/down/).

Une autre commande pour arrêter les services est la commande `stop` qui fonctionne de manière identique à la commande `container stop`. Elle arrête tous les conteneurs de l'application et les conserve. Ces conteneurs peuvent ensuite être démarrés avec la commande `start` ou `up`.

### Comment composer une application full-stack dans Docker Compose

Dans cette sous-section, nous allons ajouter un front-end à notre API de notes et en faire une application full-stack complète. Je ne vais pas expliquer les fichiers `Dockerfile.dev` dans cette sous-section (sauf celui pour le service `nginx`) car ils sont identiques à certains des autres que vous avez déjà vus dans les sous-sections précédentes.

Si vous avez cloné le dépôt du code du projet, allez dans le répertoire `fullstack-notes-application`. Chaque répertoire à l'intérieur de la racine du projet contient le code de chaque service et le `Dockerfile` correspondant.

Avant de commencer avec le fichier `docker-compose.yaml`, regardons un diagramme de la façon dont l'application va fonctionner :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/fullstack-application-design.svg)

Au lieu d'accepter les requêtes directement comme nous l'avons fait précédemment, dans cette application, toutes les requêtes seront d'abord reçues par un service NGINX (appelons-le routeur).

Le routeur vérifie ensuite si le point de terminaison demandé contient `/api`. Si oui, le routeur achemine la requête vers le back-end, sinon le routeur achemine la requête vers le front-end.

Vous faites cela parce que lorsque vous exécutez une application front-end, elle ne s'exécute pas à l'intérieur d'un conteneur. Elle s'exécute dans le navigateur, servie à partir d'un conteneur. En conséquence, la mise en réseau Compose ne fonctionne pas comme prévu et l'application front-end ne parvient pas à trouver le service `api`.

NGINX, en revanche, s'exécute à l'intérieur d'un conteneur et peut communiquer avec les différents services de toute l'application.

Je ne vais pas entrer dans la configuration de NGINX ici. Ce sujet est un peu hors du cadre de ce livre. Mais si vous voulez y jeter un coup d'œil, allez-y et consultez les fichiers `/notes-api/nginx/development.conf` et `/notes-api/nginx/production.conf`. Le code pour `/notes-api/nginx/Dockerfile.dev` est le suivant :

```
FROM nginx:stable-alpine

COPY ./development.conf /etc/nginx/conf.d/default.conf
```

Tout ce qu'il fait est de copier le fichier de configuration dans `/etc/nginx/conf.d/default.conf` à l'intérieur du conteneur.

Commençons à écrire le fichier `docker-compose.yaml`. En plus des services `api` et `db`, il y aura les services `client` et `nginx`. Il y aura également quelques définitions de réseau que j'aborderai bientôt.

```yaml
version: "3.8"

services: 
    db:
        image: postgres:12
        container_name: notes-db-dev
        volumes: 
            - db-data:/var/lib/postgresql/data
        environment:
            POSTGRES_DB: notesdb
            POSTGRES_PASSWORD: secret
        networks:
            - backend
    api:
        build: 
            context: ./api
            dockerfile: Dockerfile.dev
        image: notes-api:dev
        container_name: notes-api-dev
        volumes: 
            - /home/node/app/node_modules
            - ./api:/home/node/app
        environment: 
            DB_HOST: db ## same as the database service name
            DB_PORT: 5432
            DB_USER: postgres
            DB_DATABASE: notesdb
            DB_PASSWORD: secret
        networks:
            - backend
    client:
        build:
            context: ./client
            dockerfile: Dockerfile.dev
        image: notes-client:dev
        container_name: notes-client-dev
        volumes: 
            - /home/node/app/node_modules
            - ./client:/home/node/app
        networks:
            - frontend
    nginx:
        build:
            context: ./nginx
            dockerfile: Dockerfile.dev
        image: notes-router:dev
        container_name: notes-router-dev
        restart: unless-stopped
        ports: 
            - 8080:80
        networks:
            - backend
            - frontend

volumes:
    db-data:
        name: notes-db-dev-data

networks: 
    frontend:
        name: fullstack-notes-application-network-frontend
        driver: bridge
    backend:
        name: fullstack-notes-application-network-backend
        driver: bridge

```

Le fichier est presque identique au précédent avec lequel vous avez travaillé. La seule chose qui nécessite une explication est la configuration du réseau. Le code pour le bloc `networks` est le suivant :

```yaml
networks: 
    frontend:
        name: fullstack-notes-application-network-frontend
        driver: bridge
    backend:
        name: fullstack-notes-application-network-backend
        driver: bridge
```

J'ai défini deux réseaux de pont. Par défaut, Compose crée un réseau de pont et attache tous les conteneurs à celui-ci. Dans ce projet, cependant, je voulais une isolation de réseau appropriée. J'ai donc défini deux réseaux, un pour les services front-end et un pour les services back-end.

J'ai également ajouté un bloc `networks` dans chacune des définitions de service. De cette façon, les services `api` et `db` seront attachés à un réseau et le service `client` sera attaché à un réseau séparé. Mais le service `nginx` sera attaché aux deux réseaux afin qu'il puisse fonctionner comme routeur entre les services front-end et back-end.

Démarrez tous les services en exécutant la commande suivante :

```
docker-compose --file docker-compose.yaml up --detach

# Creating network "fullstack-notes-application-network-backend" with driver "bridge"
# Creating network "fullstack-notes-application-network-frontend" with driver "bridge"
# Creating volume "notes-db-dev-data" with default driver
# Building api
# Sending build context to Docker daemon  37.38kB
# 
# Step 1/13 : FROM node:lts-alpine as builder
#  ---> 471e8b4eb0b2
# Step 2/13 : RUN apk add --no-cache python make g++
#  ---> Running in 8a4485388fd3
### LONG INSTALLATION STUFF GOES HERE ###
# Removing intermediate container 8a4485388fd3
#  ---> 47fb1ab07cc0
# Step 3/13 : WORKDIR /app
#  ---> Running in bc76cc41f1da
# Removing intermediate container bc76cc41f1da
#  ---> 8c03fdb920f9
# Step 4/13 : COPY ./package.json .
#  ---> a1d5715db999
# Step 5/13 : RUN npm install
#  ---> Running in fabd33cc0986
### LONG INSTALLATION STUFF GOES HERE ###
# Removing intermediate container fabd33cc0986
#  ---> e09913debbd1
# Step 6/13 : FROM node:lts-alpine
#  ---> 471e8b4eb0b2
# Step 7/13 : ENV NODE_ENV=development
#  ---> Using cache
#  ---> b7c12361b3e5
# Step 8/13 : USER node
#  ---> Using cache
#  ---> f5ac66ca07a4
# Step 9/13 : RUN mkdir -p /home/node/app
#  ---> Using cache
#  ---> 60094b9a6183
# Step 10/13 : WORKDIR /home/node/app
#  ---> Using cache
#  ---> 316a252e6e3e
# Step 11/13 : COPY . .
#  ---> Using cache
#  ---> 3a083622b753
# Step 12/13 : COPY --from=builder /app/node_modules /home/node/app/node_modules
#  ---> Using cache
#  ---> 707979b3371c
# Step 13/13 : CMD [ "./node_modules/.bin/nodemon", "--config", "nodemon.json", "bin/www" ]
#  ---> Using cache
#  ---> f2da08a5f59b
# Successfully built f2da08a5f59b
# Successfully tagged notes-api:dev
# Building client
# Sending build context to Docker daemon  43.01kB
# 
# Step 1/7 : FROM node:lts-alpine
#  ---> 471e8b4eb0b2
# Step 2/7 : USER node
#  ---> Using cache
#  ---> 4be5fb31f862
# Step 3/7 : RUN mkdir -p /home/node/app
#  ---> Using cache
#  ---> 1fefc7412723
# Step 4/7 : WORKDIR /home/node/app
#  ---> Using cache
#  ---> d1470d878aa7
# Step 5/7 : COPY ./package.json .
#  ---> Using cache
#  ---> bbcc49475077
# Step 6/7 : RUN npm install
#  ---> Using cache
#  ---> 860a4a2af447
# Step 7/7 : CMD [ "npm", "run", "serve" ]
#  ---> Using cache
#  ---> 11db51d5bee7
# Successfully built 11db51d5bee7
# Successfully tagged notes-client:dev
# Building nginx
# Sending build context to Docker daemon   5.12kB
# 
# Step 1/2 : FROM nginx:stable-alpine
#  ---> f2343e2e2507
# Step 2/2 : COPY ./development.conf /etc/nginx/conf.d/default.conf
#  ---> Using cache
#  ---> 02a55d005a98
# Successfully built 02a55d005a98
# Successfully tagged notes-router:dev
# Creating notes-client-dev ... done
# Creating notes-api-dev    ... done
# Creating notes-router-dev ... done
# Creating notes-db-dev     ... done
```

Maintenant, visitez `http://localhost:8080` et voilà !

![Image](https://www.freecodecamp.org/news/content/images/2021/01/notes-application.png)

Essayez d'ajouter et de supprimer des notes pour voir si l'application fonctionne correctement. Le projet est également livré avec des scripts shell et un `Makefile`. Explorez-les pour voir comment vous pouvez exécuter ce projet sans l'aide de `docker-compose` comme vous l'avez fait dans la section précédente.

## Conclusion

Je tiens à vous remercier du fond du cœur pour le temps que vous avez passé à lire ce livre. J'espère que vous l'avez apprécié et que vous avez appris toutes les bases de Docker.

En plus de celui-ci, j'ai écrit des manuels complets sur d'autres sujets compliqués disponibles gratuitement sur [freeCodeCamp](https://www.freecodecamp.org/news/author/farhanhasin/).

Ces manuels font partie de ma mission de simplifier les technologies difficiles à comprendre pour tous. Chacun de ces manuels prend beaucoup de temps et d'efforts à écrire.

Si vous avez apprécié mon écriture et que vous voulez me motiver, envisagez de laisser des étoiles sur [GitHub](https://github.com/fhsinchy/) et de m'endosser pour des compétences pertinentes sur [LinkedIn](https://www.linkedin.com/in/farhanhasin/). J'accepte également les parrainages, donc vous pouvez envisager de [m'offrir un café](https://www.buymeacoffee.com/farhanhasin) si vous le souhaitez.

Je suis toujours ouvert aux suggestions et aux discussions sur [Twitter](https://twitter.com/frhnhsin) ou [LinkedIn](https://www.linkedin.com/in/farhanhasin/). Envoyez-moi des messages directs.

En fin de compte, envisagez de partager les ressources avec les autres, car

> Partager les connaissances est l'acte le plus fondamental de l'amitié. Parce que c'est une façon de donner quelque chose sans perdre quelque chose. — Richard Stallman

Jusqu'au prochain, restez en sécurité et continuez à apprendre.