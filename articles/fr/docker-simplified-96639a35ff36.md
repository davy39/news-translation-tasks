---
title: 'Docker Simplifié : Un Guide Pratique pour les Débutants Absolus'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-18T16:07:03.000Z'
originalURL: https://freecodecamp.org/news/docker-simplified-96639a35ff36
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8TdTKJ6wtOoX7hZEbNFK-A.png
tags:
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Docker Simplifié : Un Guide Pratique pour les Débutants Absolus'
seo_desc: 'By Shahzan

  Whether you are planning to start your career in DevOps, or you are already into
  it, if you do not have Docker listed on your resume, it’s undoubtedly time for you
  to think about it, as Docker is one of the critical skill for anyone who is...'
---

Par Shahzan

Que vous prévoyiez de commencer votre carrière dans le DevOps, ou que vous soyez déjà impliqué, si vous n'avez pas Docker listé sur votre CV, il est sans doute temps d'y penser, car Docker est l'une des compétences critiques pour quiconque est dans l'arène DevOps.

Dans cet article, je vais essayer de mon mieux d'expliquer Docker de la manière la plus simple possible.

Avant de plonger en profondeur et de commencer à explorer Docker, jetons un coup d'œil aux sujets que nous allons aborder dans le cadre de ce guide pour débutants.

* [Qu'est-ce que Docker ?](https://medium.com/p/96639a35ff36#questceque)
* [Le problème que Docker résout](https://medium.com/p/96639a35ff36#leprobleme)
* [Avantages et inconvénients de l'utilisation de Docker](https://medium.com/p/96639a35ff36#avantagesetinconvenients)
* [Composants principaux de Docker](https://medium.com/p/96639a35ff36#composantsprincipaux)
* [Terminologie Docker](https://medium.com/p/96639a35ff36#terminologie)
* [Qu'est-ce que Docker Hub ?](https://medium.com/p/96639a35ff36#questcedockerhub)
* [Éditions Docker](https://medium.com/p/96639a35ff36#editions)
* [Installation de Docker](https://medium.com/p/96639a35ff36#installation)
* [Quelques commandes Docker essentielles pour bien démarrer](https://medium.com/p/96639a35ff36#commandes)
* [Conclusion](https://medium.com/p/96639a35ff36#conclusion)

### Commençons par comprendre, Qu'est-ce que Docker ?

En termes simples, Docker est une plateforme logicielle qui simplifie le processus de construction, d'exécution, de gestion et de distribution d'applications. Il le fait en virtualisant le système d'exploitation de l'ordinateur sur lequel il est installé et exécuté.

La première édition de Docker a été publiée en 2013.

Docker est développé en utilisant le langage de programmation GO.

![Image](https://cdn-media-1.freecodecamp.org/images/1*waybfdGDf7yb8ZpDfIgEsA.png)

> Compte tenu de l'ensemble riche de fonctionnalités que Docker a à offrir, il a été largement adopté par certaines des principales organisations et universités du monde, telles que **Visa, PayPal, Cornell University et Indiana University** (pour n'en nommer que quelques-unes) pour exécuter et gérer leurs applications en utilisant Docker.

### Essayons maintenant de comprendre le problème, et la solution que Docker a à offrir

#### Le Problème

Supposons que vous avez trois applications différentes basées sur Python que vous prévoyez d'héberger sur un seul serveur (qui peut être une machine physique ou virtuelle).

Chacune de ces applications utilise une version différente de Python, ainsi que les bibliothèques et dépendances associées, qui diffèrent d'une application à l'autre.

Puisque nous ne pouvons pas avoir différentes versions de Python installées sur la même machine, cela nous empêche d'héberger les trois applications sur le même ordinateur.

#### La Solution

Voyons comment nous pourrions résoudre ce problème sans utiliser Docker. Dans un tel scénario, nous pourrions résoudre ce problème soit en ayant trois machines physiques, soit une seule machine physique, suffisamment puissante pour héberger et exécuter trois machines virtuelles.

Les deux options nous permettraient d'installer différentes versions de Python sur chacune de ces machines, ainsi que leurs dépendances associées.

Quelle que soit la solution que nous choisissons, les coûts associés à l'acquisition et à la maintenance du matériel sont assez élevés.

Maintenant, voyons comment Docker pourrait être une solution efficace et économique à ce problème.

Pour comprendre cela, nous devons examiner comment Docker fonctionne exactement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MbxLUFB2HRPmLAn60tQKZA.png)

La machine sur laquelle Docker est installé et exécuté est généralement appelée un Hôte Docker ou simplement Hôte.

Ainsi, chaque fois que vous prévoyez de déployer une application sur l'hôte, il créerait une entité logique pour héberger cette application. En terminologie Docker, nous appelons cette entité logique un Conteneur ou Conteneur Docker pour être plus précis.

Un Conteneur Docker n'a pas de système d'exploitation installé et exécuté. Mais il aurait une copie virtuelle de la table des processus, de l'interface réseau et du point de montage du système de fichiers. Ceux-ci ont été hérités du système d'exploitation de l'hôte sur lequel le conteneur est hébergé et exécuté.

Alors que le noyau du système d'exploitation de l'hôte est partagé entre tous les conteneurs qui y sont exécutés.

Cela permet à chaque conteneur d'être isolé des autres présents sur le même hôte. Ainsi, il supporte plusieurs conteneurs avec différentes exigences et dépendances d'applications pour s'exécuter sur le même hôte, tant qu'ils ont les mêmes exigences de système d'exploitation.

Pour comprendre comment Docker a été bénéfique pour résoudre ce problème, vous devez vous référer à la section suivante, qui traite des avantages et inconvénients de l'utilisation de Docker.

En bref, Docker virtualiserait le système d'exploitation de l'hôte sur lequel il est installé et exécuté, plutôt que de virtualiser les composants matériels.

### Les Avantages et Inconvénients de l'utilisation de Docker

#### Avantages de l'utilisation de Docker

Certains des principaux avantages de l'utilisation de Docker sont listés ci-dessous :

* Docker supporte plusieurs applications avec différentes exigences et dépendances d'applications, pour être hébergées ensemble sur le même hôte, tant qu'elles ont les mêmes exigences de système d'exploitation.
* Optimisation du stockage. Un grand nombre d'applications peuvent être hébergées sur le même hôte, car les conteneurs sont généralement de quelques mégaoctets et consomment très peu d'espace disque.
* Robustesse. Un conteneur n'a pas de système d'exploitation installé. Ainsi, il consomme très peu de mémoire par rapport à une machine virtuelle (qui aurait un système d'exploitation complet installé et exécuté). Cela réduit également le temps de démarrage à quelques secondes, contre quelques minutes nécessaires pour démarrer une machine virtuelle.
* Réduction des coûts. Docker est moins exigeant en termes de matériel nécessaire pour l'exécuter.

#### Inconvénients de l'utilisation de Docker

* Les applications avec différentes exigences de système d'exploitation ne peuvent pas être hébergées ensemble sur le même Hôte Docker. Par exemple, supposons que nous avons 4 applications différentes, dont 3 applications nécessitent un système d'exploitation basé sur Linux et l'autre application nécessite un système d'exploitation basé sur Windows. Dans un tel scénario, les 3 applications qui nécessitent un système d'exploitation basé sur Linux peuvent être hébergées sur un seul Hôte Docker, tandis que l'application qui nécessite un système d'exploitation basé sur Windows doit être hébergée sur un Hôte Docker différent.

### Composants Principaux de Docker

**Docker Engine** est l'un des composants principaux de Docker. Il est responsable du fonctionnement global de la plateforme Docker.

**Docker Engine** est une application basée sur le modèle client-serveur et se compose de 3 composants principaux.

1. Serveur
2. API REST
3. Client

![Image](https://cdn-media-1.freecodecamp.org/images/1*MYX0ClbWoitxS0RNUVvj8A.png)
_Source de l'image : [https://docs.docker.com](https://docs.docker.com/v17.12/engine/docker-overview/" rel="noopener" target="_blank" title=")_

Le **Serveur** exécute un démon connu sous le nom de **dockerd** **(Docker Daemon)**, qui n'est rien d'autre qu'un processus. Il est responsable de la création et de la gestion des Images Docker, des Conteneurs, des Réseaux et des Volumes sur la plateforme Docker.

L'**API REST** spécifie comment les applications peuvent interagir avec le Serveur, et lui donner des instructions pour accomplir leur travail.

Le **Client** n'est rien d'autre qu'une interface de ligne de commande, qui permet aux utilisateurs d'interagir avec **Docker** en utilisant des commandes.

### Terminologie Docker

Jetons un coup d'œil rapide à certains des termes associés à Docker.

**Images Docker** et **Conteneurs Docker** sont les deux choses essentielles que vous rencontrerez quotidiennement en travaillant avec **Docker**.

En termes simples, une **Image Docker** est un modèle qui contient l'application, et toutes les dépendances nécessaires pour exécuter cette application sur Docker.

D'autre part, comme indiqué précédemment, un **Conteneur Docker** est une entité logique. En termes plus précis, c'est une instance en cours d'exécution de l'Image Docker.

#### Qu'est-ce que Docker Hub ?

**Docker Hub** est le dépôt en ligne officiel où vous pouvez trouver toutes les Images Docker qui sont disponibles pour nous à utiliser.

**Docker Hub** nous permet également de stocker et de distribuer nos images personnalisées si nous le souhaitons. Nous pouvons également les rendre publiques ou privées, en fonction de nos besoins.

Veuillez noter : Les utilisateurs gratuits sont uniquement autorisés à garder une Image Docker privée. Si nous souhaitons garder plus d'une Image Docker privée, nous devons souscrire à un plan d'abonnement payant.

### Éditions Docker

Docker est disponible en 2 éditions différentes, comme listé ci-dessous :

* **Édition Communauté (CE)**
* **Édition Entreprise (EE)**

L'**Édition Communauté** est adaptée aux développeurs individuels et aux petites équipes. Elle offre des fonctionnalités limitées, par rapport à l'Édition Entreprise.

L'**Édition Entreprise**, en revanche, est adaptée aux grandes équipes et à l'utilisation de Docker dans des environnements de production.

L'Édition Entreprise est également catégorisée en trois éditions différentes, comme listé ci-dessous :

* **Édition Basique**
* **Édition Standard**
* **Édition Avancée**

### Installation de Docker

Une dernière chose que nous devons savoir avant de passer à la pratique avec Docker est d'avoir Docker installé.

Voici les liens vers les guides d'installation officiels de Docker CE. Vous pouvez suivre ces guides pour installer Docker sur votre machine, car ils sont simples et directs.

* [CentOS Linux](https://docs.docker.com/install/linux/docker-ce/centos/)
* [Debian Linux](https://docs.docker.com/install/linux/docker-ce/debian/)
* [Fedora Linux](https://docs.docker.com/install/linux/docker-ce/fedora/)
* [Ubuntu Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [Microsoft Windows](https://docs.docker.com/docker-for-windows/install/)
* [MacOS](https://docs.docker.com/docker-for-mac/install/)

#### Vous voulez sauter l'installation et passer directement à la pratique de Docker ?

Au cas où vous vous sentirez trop paresseux pour installer Docker, ou si vous n'avez pas assez de ressources disponibles sur votre ordinateur, vous n'avez pas à vous inquiéter, voici la solution à votre problème.

Vous pouvez vous rendre sur [Play with Docker](https://labs.play-with-docker.com/), qui est un terrain de jeu en ligne pour Docker. Il permet aux utilisateurs de pratiquer les commandes Docker immédiatement, sans avoir à installer quoi que ce soit sur votre machine. Le meilleur, c'est qu'il est simple à utiliser et disponible gratuitement.

### Commandes Docker

Maintenant, il est temps de se salir les mains avec les commandes Docker, pour lesquelles nous avons tous attendu jusqu'à présent.

#### docker create

La première commande que nous allons examiner est la commande **docker create**.

Cette commande nous permet de créer un nouveau conteneur.

La syntaxe de cette commande est la suivante :

```
docker create [options] IMAGE [commandes] [arguments]
```

Veuillez noter : Tout ce qui est enfermé dans des crochets est facultatif. Cela s'applique à toutes les commandes que vous verrez dans ce guide.

Certains exemples d'utilisation de cette commande sont présentés ci-dessous :

```
$ docker create fedora
```

```
02576e880a2ccbb4ce5c51032ea3b3bb8316e5b626861fc87d28627c810af03
```

Dans l'exemple ci-dessus, la commande docker create créerait un nouveau conteneur en utilisant la dernière image Fedora.

Avant de créer le conteneur, il vérifiera si la dernière image officielle de Fedora est disponible sur l'Hôte Docker ou non. Si la dernière image n'est pas disponible sur l'Hôte Docker, elle ira de l'avant et téléchargera l'image Fedora depuis Docker Hub avant de créer le conteneur. Si l'image Fedora est déjà présente sur l'Hôte Docker, elle utilisera cette image et créera le conteneur.

Si le conteneur a été créé avec succès, Docker retournera l'ID du conteneur. Par exemple, dans l'exemple ci-dessus, 02576e880a2ccbb4ce5c51032ea3b3bb8316e5b626861fc87d28627c810af03 est l'ID du conteneur retourné par Docker.

Chaque conteneur a un ID de conteneur unique. Nous faisons référence au conteneur en utilisant son ID de conteneur pour effectuer diverses opérations sur le conteneur, telles que le démarrage, l'arrêt, le redémarrage, etc.

Maintenant, faisons référence à un autre exemple de commande docker create, qui a des options et des commandes qui lui sont passées.

```
$ docker create -t -i ubuntu bash
```

```
30986b73dc0022dbba81648d9e35e6e866b4356f026e75660460c3474f1ca005
```

Dans l'exemple ci-dessus, la commande docker create crée un conteneur en utilisant l'image Ubuntu (comme indiqué précédemment, si l'image n'est pas disponible sur l'Hôte Docker, elle ira de l'avant et téléchargera la dernière image depuis Docker Hub avant de créer le conteneur).

Les options -t et -i instruisent Docker d'allouer un terminal au conteneur afin que l'utilisateur puisse interagir avec le conteneur. Il instruit également Docker d'exécuter la commande bash chaque fois que le conteneur est démarré.

#### docker ps

La commande suivante que nous allons examiner est la commande **docker ps**.

La commande **docker ps** nous permet de voir tous les conteneurs qui s'exécutent sur l'Hôte Docker.

```
$ docker ps
```

```
CONTAINER ID IMAGE  COMMAND CREATED        STATUS            PORTS NAMES30986b73dc00 ubuntu "bash"  45 minutes ago Up About a minute                 elated_franklin
```

Elle n'affiche que les conteneurs qui sont actuellement en cours d'exécution sur l'Hôte Docker.

Si vous souhaitez voir tous les conteneurs qui ont été créés sur cet Hôte Docker, indépendamment de leur statut actuel, comme s'ils sont en cours d'exécution ou arrêtés, vous devrez inclure l'option -a, qui à son tour affichera tous les conteneurs qui ont été créés sur cet Hôte Docker.

```
$ docker ps -a
```

```
CONTAINER ID IMAGE  COMMAND     CREATED           STATUS       PORTS NAMES30986b73dc00 ubuntu "bash"      About an hour ago Up 29 minutes elated_franklin02576e880a2c fedora "bin/bash" About an hour ago Created hungry_sinoussi
```

Avant de continuer, essayons de décoder et de comprendre la sortie de la commande **docker ps**.

**CONTAINER ID** : Une chaîne unique composée de caractères alphanumériques, associée à chaque conteneur.

**IMAGE** : Nom de l'Image Docker utilisée pour créer ce conteneur.

**COMMAND** : Toute commande spécifique à l'application qui doit être exécutée lorsque le conteneur est démarré.

**CREATED** : Cela montre le temps écoulé depuis la création de ce conteneur.

**STATUS** : Cela montre le statut actuel du conteneur, ainsi que le temps écoulé, dans son état actuel.

Si le conteneur est en cours d'exécution, il affichera Up avec la période de temps écoulée (par exemple, Up About an hour ou Up 3 minutes).

Si le conteneur est arrêté, il affichera Exited suivi du code de statut de sortie entre parenthèses, avec la période de temps écoulée (par exemple, Exited (0) 3 weeks ago ou Exited (137) 15 seconds ago, où 0 et 137 sont les codes de sortie).

**PORTS** : Cela affiche les mappages de ports définis pour le conteneur.

**NAMES** : En plus de l'ID du conteneur, chaque conteneur se voit également attribuer un nom unique. Nous pouvons faire référence à un conteneur soit en utilisant son ID de conteneur, soit son nom unique. Docker attribue automatiquement un nom unique et amusant à chaque conteneur qu'il crée. Mais si vous souhaitez spécifier votre propre nom pour le conteneur, vous pouvez le faire en incluant l'option `--name` (double trait d'union nom) à la commande docker create ou docker run (nous examinerons la commande docker run plus tard).

J'espère que cela vous donne une meilleure compréhension de la sortie de la commande docker ps.

#### docker start

La commande suivante que nous allons examiner est la commande **docker start**.

Cette commande démarre tout conteneur arrêté.

La syntaxe de cette commande est la suivante :

```
docker start [options] CONTAINER ID/NAME [CONTAINER ID/NAME...]
```

Nous pouvons démarrer un conteneur soit en spécifiant les premiers caractères uniques de son ID de conteneur, soit en spécifiant son nom.

Certains exemples d'utilisation de cette commande sont présentés ci-dessous :

```
$ docker start 30986
```

Dans l'exemple ci-dessus, Docker démarre le conteneur commençant par l'ID de conteneur 30986.

```
$ docker start elated_franklin
```

Alors que dans cet exemple, Docker démarre le conteneur nommé elated_franklin.

#### docker stop

La commande suivante sur la liste est la commande **docker stop**.

Cette commande arrête tout conteneur en cours d'exécution.

La syntaxe de cette commande est la suivante :

```
docker stop [options] CONTAINER ID/NAME [CONTAINER ID/NAME...]
```

Elle est similaire à la commande docker start.

Nous pouvons arrêter le conteneur soit en spécifiant les premiers caractères uniques de son ID de conteneur, soit en spécifiant son nom.

Certains exemples d'utilisation de cette commande sont présentés ci-dessous :

```
$ docker stop 30986
```

Dans l'exemple ci-dessus, Docker arrêtera le conteneur commençant par l'ID de conteneur 30986.

```
$ docker stop elated_franklin
```

Alors que dans cet exemple, Docker arrêtera le conteneur nommé elated_franklin.

#### docker restart

La commande suivante que nous allons examiner est la commande **docker restart**.

Cette commande redémarre tout conteneur en cours d'exécution.

La syntaxe de cette commande est la suivante :

```
docker restart [options] CONTAINER ID/NAME [CONTAINER ID/NAME...]
```

Nous pouvons redémarrer le conteneur soit en spécifiant les premiers caractères uniques de son ID de conteneur, soit en spécifiant son nom.

Certains exemples d'utilisation de cette commande sont présentés ci-dessous :

```
$ docker restart 30986
```

Dans l'exemple ci-dessus, Docker redémarrera le conteneur commençant par l'ID de conteneur 30986.

```
$ docker restart elated_franklin
```

Alors que dans cet exemple, Docker redémarrera le conteneur nommé elated_franklin.

#### docker run

La commande suivante que nous allons examiner est la commande **docker run**.

Cette commande crée d'abord le conteneur, puis le démarre. En bref, cette commande est une combinaison de la commande docker create et de la commande docker start.

La syntaxe de cette commande est la suivante :

```
docker run [options] IMAGE [commandes] [arguments]
```

Elle a une syntaxe similaire à celle de la commande docker create.

Certains exemples d'utilisation de cette commande sont présentés ci-dessous :

```
$ docker run ubuntu
```

```
30fa018c72682d78cf168626b5e6138bb3b3ae23015c5ec4bbcc2a088e67520
```

Dans l'exemple ci-dessus, Docker créera le conteneur en utilisant la dernière image Ubuntu, puis le démarrera immédiatement.

Si nous exécutons la commande ci-dessus, elle démarrera le conteneur et l'arrêtera immédiatement — nous n'aurons aucune chance d'interagir avec le conteneur.

Si nous voulons interagir avec le conteneur, nous devons spécifier les options : -it (trait d'union suivi de i et t) à la commande docker run nous présente le terminal, en utilisant lequel nous pourrions interagir avec le conteneur en tapant les commandes appropriées. Voici un exemple de la même chose.

```
$ docker run -it ubuntu
```

```
root@e4e633428474:/#
```

Pour sortir du conteneur, vous devez taper exit dans le terminal.

#### docker rm

Passons à la commande suivante — si nous voulons supprimer un conteneur, nous utilisons la commande **docker rm**.

La syntaxe de cette commande est la suivante :

```
docker rm [options] CONTAINER ID/NAME [CONTAINER ID/NAME...]
```

Certains exemples d'utilisation de cette commande sont présentés ci-dessous :

```
$ docker rm 30fa elated_franklin
```

Dans l'exemple ci-dessus, nous instruisons Docker de supprimer 2 conteneurs dans une seule commande. Le premier conteneur à supprimer est spécifié en utilisant son ID de conteneur, et le deuxième conteneur à supprimer est spécifié en utilisant son nom.

Veuillez noter : Les conteneurs doivent être à l'état arrêté pour pouvoir être supprimés.

#### docker images

**docker images** est la commande suivante sur la liste.

Cette commande liste toutes les Images Docker qui sont présentes sur votre Hôte Docker.

```
$ docker images
```

```
REPOSITORY  TAG      IMAGE          CREATED        SIZEmysql       latest   7bb2586065cd   38 hours ago   477MBhttpd       latest   5eace252f2f2   38 hours ago   132MBubuntu      16.04    9361ce633ff1   2 weeks ago    118MBubuntu      trusty   390582d83ead   2 weeks ago    188MBfedora      latest   d09302f77cfc   2 weeks ago    275MBubuntu      latest   94e814e2efa8   2 weeks ago    88.9MB
```

Décodons la sortie de la commande **docker images**.

**REPOSITORY** : Cela représente le nom unique de l'Image Docker.

**TAG** : Chaque image est associée à une étiquette unique. Une étiquette représente essentiellement une version de l'image.

Une étiquette est généralement représentée soit par un mot, soit par un ensemble de chiffres, soit par une combinaison de caractères alphanumériques.

**IMAGE ID** : Une chaîne unique composée de caractères alphanumériques, associée à chaque image.

**CREATED** : Cela montre le temps écoulé depuis la création de cette image.

**SIZE** : Cela montre la taille de l'image.

#### docker rmi

La commande suivante sur la liste est la commande **docker rmi**.

La commande **docker rmi** nous permet de supprimer une ou plusieurs images de l'Hôte Docker.

La syntaxe de cette commande est la suivante :

```
docker rmi [options] IMAGE NAME/ID [IMAGE NAME/ID...]
```

Certains exemples d'utilisation de cette commande sont présentés ci-dessous :

```
docker rmi mysql
```

La commande ci-dessus supprime l'image nommée mysql de l'Hôte Docker.

```
docker rmi httpd fedora
```

La commande ci-dessus supprime les images nommées httpd et fedora de l'Hôte Docker.

```
docker rmi 94e81
```

La commande ci-dessus supprime l'image commençant par l'ID d'image 94e81 de l'Hôte Docker.

```
docker rmi ubuntu:trusty
```

La commande ci-dessus supprime l'image nommée ubuntu, avec l'étiquette trusty de l'Hôte Docker.

Ce sont quelques-unes des commandes Docker de base que vous verrez. Il y a beaucoup plus de commandes Docker à explorer.

### Conclusion

La conteneurisation a récemment reçu l'attention qu'elle mérite, bien qu'elle existe depuis longtemps. Certaines des principales entreprises technologiques comme Google, Amazon Web Services (AWS), Intel, Tesla et Juniper Networks ont leur propre version personnalisée de moteurs de conteneurs. Elles s'appuient fortement sur eux pour construire, exécuter, gérer et distribuer leurs applications.

> **Docker** est un moteur de conteneurisation extrêmement puissant, et il a beaucoup à offrir en matière de construction, d'exécution, de gestion et de distribution efficaces de vos applications.

Vous venez de voir Docker à un niveau très élevé. Il y a beaucoup plus à apprendre sur Docker, comme :

* Commandes Docker (Commandes plus puissantes)
* Images Docker (Construisez vos propres images personnalisées)
* Réseautage Docker (Configuration et configuration du réseau)
* Services Docker (Regroupement de conteneurs utilisant la même image)
* Pile Docker (Regroupement de services requis par une application)
* Docker Compose (Outil pour gérer et exécuter plusieurs conteneurs)
* Docker Swarm (Regroupement et gestion d'une ou plusieurs machines sur lesquelles Docker est en cours d'exécution)
* Et bien plus encore...

Si vous avez trouvé Docker fascinant et que vous êtes intéressé à en apprendre davantage, je vous recommande de vous inscrire aux cours qui sont listés ci-dessous. Je les ai trouvés très informatifs et directs.

Si vous êtes un débutant absolu, je vous suggère de [vous inscrire à ce cours](http://bit.ly/2YLH23G), qui a été conçu pour les débutants.

Si vous avez une bonne connaissance de Docker et que vous êtes assez confiant avec les bases et que vous souhaitez approfondir vos connaissances, je vous suggère de [vous inscrire à ce cours](http://bit.ly/2UaTGe8), qui est plus axé sur les sujets avancés liés à Docker.

**Docker** est une compétence à l'épreuve du temps et prend simplement de l'ampleur.

Investir votre temps et votre argent dans l'apprentissage de Docker ne serait pas quelque chose que vous regretteriez.

> J'espère que vous avez trouvé cet article informatif. N'hésitez pas à le partager. Cela signifie beaucoup pour moi.

### Avant de dire au revoir...

Restez en contact, [cliquez ici pour entrer votre adresse e-mail](https://forms.gle/3U1uBNEC4mDkSpMJ7) (Utilisez ce lien si le widget ci-dessus ne s'affiche pas sur votre écran).

Merci beaucoup d'avoir pris votre temps précieux pour lire cet article.

Avis de non-responsabilité : Tous les noms de produits et de sociétés sont des marques de commerce™ ou des marques déposées® de leurs détenteurs respectifs. Leur utilisation n'implique aucune approbation de leur part. Il peut y avoir des liens d'affiliation dans cet article.