---
title: Laissez-moi vous guider lors de votre premier rendez-vous avec Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-31T19:38:50.000Z'
originalURL: https://freecodecamp.org/news/let-me-guide-you-through-your-first-date-with-docker-f03f35567d95
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aKHmBi9PuIUTpp0buimRsA.jpeg
tags:
- name: containers
  slug: containers
- name: Docker
  slug: docker
- name: docker image
  slug: docker-image
- name: technology
  slug: technology
- name: visualization
  slug: visualization
seo_title: Laissez-moi vous guider lors de votre premier rendez-vous avec Docker
seo_desc: 'By Chandrabhan Singh

  Install Docker, create your first container, and more

  You may have seen Docker somewhere on the internet and you may feel curious about
  it. Now you want to take it to the next level. How about going on a date with Docker?
  No — I ...'
---

Par Chandrabhan Singh

#### Installez Docker, créez votre premier conteneur, et plus encore

Vous avez peut-être vu Docker quelque part sur Internet et vous êtes peut-être curieux à ce sujet. Maintenant, vous voulez passer à l'étape suivante. Que diriez-vous d'un rendez-vous avec Docker ? Non — je ne plaisante pas !

Mais comment planifier un premier rendez-vous parfait ? Que devriez-vous faire ? Où trouver les bonnes ressources ? Quels prérequis pourriez-vous avoir besoin ?

Les questions sont sans fin. Suivez ces directives pour le premier rendez-vous, et vous serez bien parti pour obtenir un deuxième.

### Planifier votre rendez-vous

Connaître votre rendez-vous avant de commencer à planifier est crucial pour créer une première expérience mémorable. Cela augmentera probablement votre confiance pendant la rencontre, également.

Il n'est jamais trop tard pour dire Bonjour. [Voici](https://medium.com/@chandrabhan_/docker-what-i-learned-bc3587e17f17) une courte introduction à ma première rencontre avec Docker si vous êtes intéressé.

D'accord ! Donc la feuille de route que nous allons suivre aujourd'hui ressemble à ceci :

1. Installation du lieu
2. La prise en charge
3. La conversation

### **Prélude**

L'endroit où nous allons organiser notre rendez-vous est le moteur Docker.

Le moteur Docker n'est pas différent des autres moteurs. C'est une combinaison de divers composants travaillant ensemble.

Nous verrons quelques-uns de ces composants plus tard dans cet article. Mais pour l'instant, décorons notre machine avec Docker. Le processus d'installation dépend de votre système d'exploitation.

La clé pour une exécution sans interruption est de toujours se référer à un site officiel. Docker a ce guide [fantastique](https://docs.docker.com/install/), où vous pouvez en savoir plus sur l'installation.

Docker existe en deux versions : Docker Community Edition (CE) et Docker Enterprise Edition (E.E.). Pour nos besoins de démonstration, nous devons nous en tenir à l'édition communautaire. L'édition Enterprise est payante. Et de plus, faire une réservation coûteuse pour votre premier rendez-vous n'est pas la meilleure idée ?

### Le lieu

Le mantra de base pour tout rendez-vous propice est de choisir le bon lieu de rencontre. Rencontrer Docker n'est pas différent. D'abord, nous devrions décider de la plateforme. Cloud ? Mac ? Linux ? Ou Windows ? Une fois que nous connaissons notre environnement, nous pouvons choisir le moyen le plus simple de configurer le lieu de rencontre.

#### Windows

Si votre choix est Windows, le processus de configuration est assez simple. Souvenez-vous de notre processus préféré : Suivant, Suivant, Suivant, et Terminer.

Allez à la page de [téléchargement](https://store.docker.com/editions/community/docker-ce-desktop-windows) et choisissez le canal "Edge". Edge a des fonctionnalités expérimentales et convient le mieux à nos besoins d'apprentissage.

**Note !** Docker pour Windows nécessite la fonctionnalité "Hyper-V", mais il n'y a rien à craindre — Docker l'activera pour vous. Cependant, cela signifie que vous ne pouvez pas utiliser Virtual Box.

#### Linux

Lorsque j'ai commencé à expérimenter sur une machine Linux, je pensais que cela allait être un cauchemar. Mais à mon soulagement, l'installation de Docker sur une distribution Linux s'est avérée simple. Encore une fois, il existe de nombreuses façons d'installer Docker sur une distribution Linux.

Ma préférée est : "Installer en utilisant le script de commodité". Nous récupérons un long script shell depuis Internet et le transmettons à un terminal shell.

Comment ? Comme ceci :

```
sudo wget -qO- https://get.docker.com |sh
```

**Terminé** ! Oui, vous avez Docker sur votre machine et il fonctionne.

Maintenant que le lieu est prêt, nous sommes prêts à continuer. Mais d'abord, faisons quelques vérifications pour nous assurer que tout fonctionne bien ici. Comme vous pourriez le faire avec un restaurant avant de réserver une table ?.

Exécutons la commande suivante dans le terminal :

```
docker version
```

Vous devriez voir les détails de l'installation. Cela vous donne des informations sur la version du **Client** et du **Serveur**, la version de **Go-lang**, et ainsi de suite.

Si la sortie de votre commande ressemble à celle ci-dessous, le soleil brille et le monde est beau. **Prochaine étape** : il est temps de se préparer pour la "Prise en charge".

![Image](https://cdn-media-1.freecodecamp.org/images/n435DcbT4csc32tM5JOtrQrRDrvGHZZqhUx2)
_Sortie de la commande_

### **La prise en charge**

Comme vous le savez peut-être déjà, Docker utilise des **Images** pour créer des conteneurs. Ces images sont de grands fichiers binaires immuables.

Une image contient des binaires d'application et leurs dépendances. Elle peut également contenir d'autres composants tels qu'un serveur web ou même un système d'exploitation.

Nous aurons besoin de telles images pour créer un conteneur et exécuter une application à l'intérieur.

Alors, où vivent ces images ? Question simple, réponse simple : sur un hôte. Cet hôte peut être votre machine ou un registre quelque part sur Internet. [Docker](http://docker.io/) a son propre registre appelé Docker-Hub.

#### Pour éviter de vous perdre, vous devriez connaître le bon lieu de prise en charge pour votre rendez-vous.

Pour rendre votre premier rendez-vous plus fluide, j'ai trouvé l'emplacement exact d'une image que je peux partager avec vous. Assez excité ? Voici !

```
docker pull chandrabhan/dotnetconsole
```

Confirmons que nous sommes au bon endroit. ?

```
docker image ls
```

![Image](https://cdn-media-1.freecodecamp.org/images/ESkhGnOlmgnvsNWlJwQi45OdWHMWXM0m2wPD)
_sortie de la commande_

Ici, vous pouvez voir diverses propriétés des images sur votre machine. Cool, il semble que les choses se passent bien jusqu'à présent.

Avant d'aller plus loin, décomposons les deux commandes précédentes et comprenons ce qui se passe ici.

Avec `Docker pull`, nous avons demandé au démon Docker de récupérer une image pour nous. Le démon n'a pas trouvé l'image dans le registre local, il est donc allé chercher une copie distante sur Docker-Hub.

Grâce à `docker image ls`, nous avons vu toutes les images disponibles et leurs propriétés.

Je dois admettre que je suis excité. Nous avons fait un excellent travail jusqu'à présent. Ensuite, laissez l'interaction commencer.

### La conversation

#### Commencez la conversation, et les choses tourneront en votre faveur.

Alors encore une fois, pour vous faciliter la tâche, je veux vous offrir quelques brise-glaces.

Nous allons créer quelques conteneurs pour des applications du framework .Net Core. Le premier sera une simple application console. L'autre sera un peu plus coloré — une application web.

```
docker run chandrabhan/dotnetconsole
```

![Image](https://cdn-media-1.freecodecamp.org/images/CX7U8rR4b1bPzulYe15hEShC5IFrYEAy1Y3k)
_sortie de la commande_

Magnifique ! Avez-vous vu ce qui s'est passé là ? Ce truc est incroyable. Une application .Net core s'exécute à l'intérieur d'un conteneur. Docker est allé de l'avant et a créé un conteneur et exécuté l'application à l'intérieur. Et dès que l'application console se termine, le conteneur existe !

Voyons combien de conteneurs nous avons sur notre machine :

```
docker container ls -a
```

![Image](https://cdn-media-1.freecodecamp.org/images/tuXcPX2nL8L7UQ5huyqHwvKip6Lm8-qFu0Cv)
_sortie de la commande_

Ce que vous voyez ici est la liste des conteneurs sur votre machine. Vous pouvez identifier un conteneur par son `**ID**`. La sortie nous indique quand le conteneur a été `**CRÉÉ**` et quel est son `**STATUT**` actuel. Le conteneur que nous avons créé est en statut `**Exited**`. Vous vous souvenez ? Notre application est terminée ! Tout comme le conteneur.

Il semble que la conversation progresse bien, alors continuons.

```
docker run -it --rm -p 5000:80 --name app chandrabhan/aspdotnet
```

Allez dans votre navigateur préféré et naviguez vers `http://localhost:5000`. Vous devriez voir plus de choses incroyables.

Une application web ASP.Net core s'exécute à l'intérieur d'un conteneur :

![Image](https://cdn-media-1.freecodecamp.org/images/bE3jqk9-iKAtDEdeHgqqiNYhCe2SXvAEOZ1c)
_application ASP.Net conteneurisée - exemple_

Avant d'aller plus loin, voyons l'anatomie de la commande ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/inCu2ZgNwFRlxd4z9BN4hM7344sBOG53BB4I)
_anatomie de la commande_

Avez-vous remarqué ? Cette fois, nous n'avons pas récupéré l'image, mais nous avons tout de même pu créer un conteneur à partir de celle-ci. Lorsque vous exécutez `docker run`, le démon Docker essaie de trouver une copie locale de l'image. Si ce n'est pas possible, il va chercher dans le registre par défaut (Docker-Hub dans ce cas).

Je crois que notre planification était excellente et que l'exécution l'était aussi. Reprenons ce que nous avons fait et revoyons comment nous avons planifié un rendez-vous propice avec Docker ?.

### **Retour en arrière**

1. Tout d'abord, nous avons installé Docker. Nous avons vu comment le processus d'installation varie en fonction du système d'exploitation.
2. Ensuite, nous avons récupéré une image du registre Docker-Hub, une simple application console .Net Core.
3. Une fois cette image sur notre machine, nous avons utilisé Docker pour créer un conteneur à partir de cette image.
4. Nous avons également vu comment récupérer une image et exécuter un conteneur via une seule commande.

Voici une illustration qui peut vous aider à comprendre une image de haut niveau.

![Image](https://cdn-media-1.freecodecamp.org/images/PuQLeHlccMgOtNb5VFtvC0uuYnEjuaVb9J22)
_illustration : client et démon Docker_

### Suivi

#### Loin des yeux, loin du cœur

Le suivi est aussi important que toute autre étape pendant le rendez-vous. Maintenant, je devrais vous laisser avec votre rendez-vous et aimerais savoir comment cela s'est passé. Voici quelques liens qui peuvent être utiles :

* [Github](https://github.com/SinghChandrabhan/DockerSamples)
* [Docker hub](https://hub.docker.com/u/chandrabhan)