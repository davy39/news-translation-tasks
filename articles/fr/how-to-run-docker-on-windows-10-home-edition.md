---
title: Comment exécuter Docker sur Windows 10 Édition Familiale
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-22T09:38:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-docker-on-windows-10-home-edition
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/head-image-1.jpg
tags:
- name: ArchLinux
  slug: archlinux
- name: Docker
  slug: docker
- name: 'VirtualBox '
  slug: virtualbox
- name: vm
  slug: vm
- name: Windows 10
  slug: windows-10
seo_title: Comment exécuter Docker sur Windows 10 Édition Familiale
seo_desc: "By Mihail Gaberov\nRecently I have been watching a tutorial where, in order\
  \ to follow it, you need to have Docker running on your machine. So far, so good.\
  \ \nBut it turns out that the latest versions of Docker require Windows 10 Pro,\
  \ Enterprise, or Edu..."
---

Par Mihail Gaberov

Récemment, j'ai suivi un tutoriel qui nécessite d'avoir [Docker](https://docs.docker.com/docker-for-windows/install/) en cours d'exécution sur votre machine. Jusqu'à présent, tout va bien. 

Mais il s'avère que les dernières versions de Docker nécessitent Windows 10 Pro, Enterprise ou Education. Ce qui signifie que si vous êtes comme moi et que vous avez Windows 10 Édition Familiale sur votre ordinateur personnel, alors vous ne pouvez pas utiliser Docker... **ou peut-être que si**. 

Lisez la suite pour découvrir comment. ?

## Raisonnement

Tout d'abord, faisons un bref résumé de la situation. Que voulons-nous accomplir et que avons-nous actuellement ?

Nous avons Windows 10 OS Édition Familiale sur notre machine. Nous aimerions avoir Docker en cours d'exécution sur la même machine afin de pouvoir créer des images Docker, exécuter des conteneurs et apprendre mieux et grandir plus vite !

Ce dernier point est un peu hors du cadre de cet article, mais nous devons bien commencer quelque part, non ? ?.

## Actions

Après avoir défini ce que nous voulons, voyons comment l'atteindre. Voici les étapes que j'ai suivies. Cela a fonctionné pour moi, ce qui me donne envie de le partager avec vous. Et peut-être que je peux faire gagner quelques jours à quelqu'un en évitant d'aller et venir sur StackOverflow ! ?

Après quelques lectures, j'ai trouvé cet [article](http://support.divio.com/en/articles/646695-how-to-use-a-directory-outside-c-users-with-docker-toolbox-docker-for-windows). Il explique qu'il est possible d'utiliser Docker sous Windows 10 Édition Familiale en exploitant une machine virtuelle Linux et en ayant des conteneurs Docker en cours d'exécution sur celle-ci. Voyons comment cela fonctionne.

### Étape 1 : Installations

Tout d'abord, vous devez installer un logiciel appelé [Oracle VM VirtualBox](https://www.virtualbox.org/). Il vous donne la possibilité d'avoir plusieurs machines virtuelles installées sur votre machine physique. De cette façon, nous pouvons avoir une machine virtuelle qui exécutera Linux où notre Docker résidera.

Ensuite, utilisez Windows PowerShell et [Chocolatey](https://chocolatey.org/), votre gestionnaire de paquets Windows, pour installer une _docker-machine_ en exécutant ce qui suit :

```bash
choco install docker-machine
```

Ouvrez votre application de terminal bash préférée et exécutez ceci :

```bash
docker-machine create --driver virtualbox default
```

Cela créera une machine virtuelle Docker appelée 'default'.

### Étape 2 : Configurations

Ensuite, nous devons configurer quels ports sont exposés lors de l'exécution de conteneurs Docker. Vous pouvez le faire en allant dans Oracle VM VirtualBox -> machine virtuelle par défaut -> Paramètres -> Réseau -> Adaptateur 1 -> Redirection de port.

![VirtualBox Port Forwarding](https://mihail-gaberov.eu/static/fb9bdc0bd6814d55c65b8ea7c761c8bd/fcda8/port-forwarding.png)

C'était le **détail le plus critique** que j'ai oublié. Nous devons permettre à Docker de monter des volumes situés sur votre disque dur. Par défaut, vous ne pouvez monter que depuis le répertoire `C://Users/`. 

Pour ajouter un chemin différent, allez simplement dans l'interface graphique d'**Oracle VM VirtualBox**. Sélectionnez la VM **default** et allez dans _Paramètres > Dossiers partagés_. Si vous ne voyez pas d'inconvénient à utiliser les paramètres par défaut, n'oubliez pas de placer votre projet sous le répertoire 'Users', par exemple `C:\Users\{votre projet}`. 

Dans mon cas, j'ai oublié cela et j'ai dû passer quelques jours à me casser la tête jusqu'à ce que je comprenne pourquoi je recevais une erreur "Couldn't find package.json" lorsque j'essayais d'exécuter les [conteneurs](https://github.com/mihailgaberov/microservices), construits à travers ce [tutoriel](https://www.youtube.com/watch?v=6Yfm5gHQjaQ&list=PLnTRniWXnjf8YC9qJFLSVCrXfS6cyj6x6&index=2).

Démarrez la machine virtuelle en exécutant la commande suivante dans votre application de terminal :

```bash
docker-machine start default
```

### Étape 3 : Configuration des Variables d'Environnement

Ensuite, nous devons configurer les variables d'environnement Docker :

```bash
docker-machine env default
```

Cela permet au client Docker et à Docker Compose de communiquer avec le moteur Docker en cours d'exécution dans la VM Linux que nous avons nommée "default".

Vous devrez peut-être également exécuter :

```bash
@FOR /f "tokens=*" %i IN ('"C:\ProgramData\chocolatey\lib\docker-machine\bin\docker-machine.exe" env') DO @%i
```

afin de faire fonctionner Docker correctement. _Note : le chemin spécifié dans la commande ci-dessus peut varier en fonction de votre configuration_.

Si vous allez utiliser des commandes telles que `docker-compose up`, vous devrez également installer Docker Tools. Vous pouvez le faire en exécutant les commandes suivantes dans PowerShell :

```bash
choco install docker-cli
choco install docker-compose
```

Cela installera tout ce dont vous avez besoin pour commencer à utiliser Docker sur votre Windows 10 Édition Familiale.

## **Conclusion**

Maintenant que nous avons tout ce dont nous avons besoin, nous pouvons consacrer notre temps à l'apprentissage réel, soit en suivant un tutoriel lié à Docker, soit en lisant un livre. Peu importe ce que vous voulez faire ensuite, vous avez tous les outils dont vous aurez besoin. 

Personnellement, je vais essayer de [terminer](https://github.com/mihailgaberov/microservices) le tutoriel mentionné précédemment et ensuite, qui sait, peut-être que je commencerai à utiliser Docker pour chaque projet que je fais.

Au fait, lors du processus de recherche, j'ai trouvé un livre très prometteur qui est spécifiquement sur Docker. Il s'intitule _"Docker in Practice" par Ian Miell_. Si cela vous intéresse, vous pourriez vouloir y jeter un coup d'œil.

? Merci d'avoir lu ! ?

### **Références**

* [https://www.virtualbox.org/](https://www.virtualbox.org/)
* [https://www.sitepoint.com/docker-windows-10-home](https://www.sitepoint.com/docker-windows-10-home)
* [https://www.youtube.com/watch?v=6Yfm5gHQjaQ&list=PLnTRniWXnjf8YC9qJFLSVCrXfS6cyj6x6&index=2](https://www.youtube.com/watch?v=6Yfm5gHQjaQ&list=PLnTRniWXnjf8YC9qJFLSVCrXfS6cyj6x6&index=2)
* [https://github.com/mihailgaberov/microservices](https://github.com/mihailgaberov/microservices)
* [http://support.divio.com/en/articles/646695-how-to-use-a-directory-outside-c-users-with-docker-toolbox-docker-for-windows](http://support.divio.com/en/articles/646695-how-to-use-a-directory-outside-c-users-with-docker-toolbox-docker-for-windows)