---
title: La manière facile d'installer Docker sur un Raspberry Pi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-28T16:25:05.000Z'
originalURL: https://freecodecamp.org/news/the-easy-way-to-set-up-docker-on-a-raspberry-pi-7d24ced073ef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SlD_OCnoe1dvKRij1whLIw.png
tags:
- name: Docker
  slug: docker
- name: Microservices
  slug: microservices
- name: General Programming
  slug: programming
- name: Raspberry Pi
  slug: raspberry-pi
- name: 'tech '
  slug: tech
seo_title: La manière facile d'installer Docker sur un Raspberry Pi
seo_desc: 'By Ryan Gordon

  Docker is a very useful tool for running containerized versions of popular applications
  (such as databases) or setting up some IoT service on an internet-connected device.

  But installing Docker can sometimes be a hassle if it needs to ...'
---

Par Ryan Gordon

Docker est un outil très utile pour exécuter des versions conteneurisées d'applications populaires (comme les bases de données) ou pour configurer un service IoT sur un appareil connecté à Internet.

Mais installer Docker peut parfois être fastidieux si cela doit être fait plusieurs fois sur différents ordinateurs. La bonne nouvelle, cependant, est qu'il existe une astuce pratique cachée dans la documentation de Docker détaillant comment installer Docker avec seulement deux lignes dans le terminal.

![Image](https://cdn-media-1.freecodecamp.org/images/furVV9L-htV7JcYivVuH9OFp17YIHkfqzKeX)

Oui, vous avez bien entendu ! Avec seulement deux lignes, vous pouvez charger et installer Docker.

L'installation de Docker peut être gérée par un script bash qui automatisera toute l'installation. Docker fournit un tel script à l'adresse `get.docker.com`. La première commande consistera à utiliser cette URL pour rechercher un fichier appelé `get-docker.sh`. Une fois obtenu, nous exécutons simplement le script. Les deux commandes peuvent être enchaînées pour former une instruction comme suit :

```
curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
```

Maintenant, vous avez Docker installé, et l'installation n'a pris que deux lignes.

Comme vous venez de le voir, les deux commandes ci-dessus sont enchaînées à l'aide de l'opérateur « && ». Cela signifie que les commandes s'exécuteront l'une après l'autre, mais peuvent être tapées sur la même ligne.

Un petit problème, cependant, est que vous pourriez rencontrer des difficultés à exécuter des commandes Docker sans sudo. Cela peut être corrigé, mais cela prendra quelques lignes de plus.

### Comment configurer Docker pour l'exécuter sans utiliser sudo tout le temps

J'ai découvert cette solution sur [AskUbuntu](https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo) après avoir rencontré le problème. Passons en revue cela maintenant.

#### Il y a 3 étapes :

1. Ajoutez le groupe Docker s'il n'existe pas déjà :

```
sudo groupadd docker
```

2. Ajoutez l'utilisateur connecté « $USER » au groupe docker. Changez le nom d'utilisateur pour correspondre à votre utilisateur préféré si vous ne souhaitez pas utiliser votre utilisateur actuel :

```
sudo gpasswd -a $USER docker
```

3. À partir de là, vous avez deux options : soit vous déconnecter puis vous reconnecter, soit exécuter `newgrp docker` pour que les changements prennent effet.

Vous devriez maintenant pouvoir exécuter Docker sans sudo. Pour tester, essayez ceci :

```
docker run hello-world
```

Si cela a fonctionné, vous devriez voir un joli message de Docker :

![Image](https://cdn-media-1.freecodecamp.org/images/TAfV1RgUTurTJwxhQcKjGkMoNF6xbN7hxuek)

Encore une fois, tout le mérite de cette solution revient à cette excellente [réponse AskUbuntu](https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo) que j'ai trouvée. Sans avoir à taper sudo tout le temps, les commandes seront beaucoup plus faciles à utiliser.

### Mais attendez, il y a plus !

Et si vous vouliez aussi docker-compose ? Vous pourriez essayer d'installer la source docker-compose de manière similaire à la façon dont nous avons installé Docker. Une approche intéressante que j'ai trouvée dans la documentation de Google Cloud Engines est que vous pouvez en fait exécuter docker-compose en tant que conteneur lui-même !

Faire cela signifie que vous avez une installation jetable de docker-compose qui sera utilisée pour composer vos services. À tout moment, vous pouvez le jeter et répéter les étapes pour un nouveau docker-compose.

La première étape consistera à exécuter docker-compose en tant que conteneur et à lui donner accès aux volumes.

```
docker run \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v "$PWD:/rootfs/$PWD" \
    -w="/rootfs/$PWD" \
    docker/compose:1.13.0 up
```

Ensuite, créez un alias pour docker-compose :

```
echo alias docker-compose="'"'docker run \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v "$PWD:/rootfs/$PWD" \
    -w="/rootfs/$PWD" \
    docker/compose:1.13.0'"'" >> ~/.bashrc
```

Puis rechargez bash :

```
source ~/.bashrc
```

Maintenant, vous avez un accès complet à docker-compose. L'alias défini ci-dessus signifie que plutôt que de devoir taper des commandes docker lorsque vous souhaitez utiliser le conteneur compose, vous pouvez simplement utiliser « docker-compose » comme vous le feriez normalement.

### Avis important concernant Docker sur RPi

Les Raspberry Pi utilisent l'architecture ARM et, par conséquent, ne seront pas compatibles avec tous les conteneurs dès la sortie de la boîte. Les images devront être construites à partir d'une image de base ARM.

Vous pouvez voir cela en action en exécutant une instance Redis conteneurisée sur un Raspberry Pi (ce qui est assez pertinent pour une série à venir que j'écris). Cela nécessitera de travailler avec une image de base. À condition que nous utilisions une image compatible ARM, aucun problème ne devrait survenir. Le problème est de trouver une image bien maintenue.

Si vous avez aimé cet article, donnez-lui un clap.

J'ai d'autres articles sur ma page liés aux Microservices, Ionic, et plus encore.