---
title: Comment construire un serveur de développement personnel sur un Raspberry Pi
  à 5 $
subtitle: ''
author: Michael Yuan
co_authors: []
series: null
date: '2020-07-17T20:46:37.000Z'
originalURL: https://freecodecamp.org/news/build-a-personal-dev-server-on-a-5-dollar-raspberry-pi
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/IMG_8632.JPG
tags:
- name: Docker
  slug: docker
- name: Git
  slug: git
- name: node js
  slug: node-js
- name: Raspberry Pi
  slug: raspberry-pi
- name: Rust
  slug: rust
seo_title: Comment construire un serveur de développement personnel sur un Raspberry
  Pi à 5 $
seo_desc: 'In this article, you''ll learn how to build a personal dev server by installing
  Git, Node.js, Rust, and Docker on a Raspberry Pi. The cheapest option costs just
  $5. You can get a starter kit ($25) for free here.

  The Raspberry Pi is a very powerful com...'
---

Dans cet article, vous apprendrez comment construire un serveur de développement personnel en installant Git, Node.js, Rust et Docker sur un Raspberry Pi. L'option la moins chère coûte seulement 5 $. [Vous pouvez obtenir un kit de démarrage (25 $) gratuitement ici](https://www.secondstate.io/articles/raspberry-pi-for-free-20200709/).

Le Raspberry Pi est un ordinateur très puissant dans un petit boîtier. L'option la moins chère, le [Raspberry Pi Zero](https://www.raspberrypi.org/products/raspberry-pi-zero/), est capable d'exécuter une distribution Linux complète et de piloter un écran haute définition. Il fait la taille de deux pièces de monnaie (US Quarters) et coûte 5 $.

À 10 $, le [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) est équipé du WiFi et du Bluetooth intégrés.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/img_8603.png align="left")

*Le Raspberry Pi Zero W à 10 $ dispose d'un CPU puissant, du WiFi, du Bluetooth et de tous types de connecteurs*

À l'extrémité "haut de gamme", vous pouvez acheter un [kit de bureau Raspberry Pi 4](https://www.raspberrypi.org/products/raspberry-pi-4-desktop-kit/) pour moins de 100 $. Il dispose d'un CPU ARM 4 cœurs fonctionnant à 1,5 GHz, d'un GPU, de 2 Go (jusqu'à 8 Go) de RAM, de 16 Go (jusqu'à 2 To) de stockage sur des cartes MicroSD, de connecteurs WiFi et Ethernet, de ports USB, de ports HDMI pouvant piloter des écrans 4K, ainsi que d'un clavier et d'une souris.

Le Raspberry Pi est également plus qu'un ordinateur standard. Il est amusant et modifiable. Le Raspberry Pi expose une rangée de broches GPIO (General Purpose Input Output). Vous pouvez attacher des capteurs simples (par exemple, température, humidité, lumière) à ces broches et capturer leurs données à partir de vos applications exécutées sur le Pi.

Vous pourriez également attacher des lumières LED et des moteurs à ces broches et utiliser votre application Pi pour piloter ces périphériques.

Pour des capteurs ou des dispositifs plus complexes, tels que des modules de caméra, vous pouvez également vous connecter au Pi via USB ou WiFi et y accéder en logiciel. Le Pi est un excellent dispositif pour l'apprentissage et le bidouillage matériel. Pour cette raison, il est largement utilisé dans les contextes éducatifs.

Cependant, le plaisir et l'apprentissage ne sont pas réservés aux enfants. Avec autant de puissance de calcul et de mise en réseau facile, le Raspberry Pi peut facilement devenir un serveur d'applications personnel pour vous.

Par exemple, vous pouvez mettre une application web (par exemple, une application de prise de notes collaborative, ou simplement quelques documents/vidéos à partager) sur un Pi, l'apporter à une réunion et la rendre accessible à tous dans la salle. Vous n'avez même pas besoin d'Internet. Il est complètement décentralisé et résistant à la censure.

Le serveur personnel est particulièrement utile pour les développeurs. Vous pouvez avoir un environnement séparé pour déployer et tester vos applications côté serveur sans avoir à modifier votre ordinateur portable. Un serveur de développement personnel est comme Docker sur stéroïdes. Dans cet article, je vais vous apprendre comment en configurer un.

## D'abord, procurez-vous un Raspberry Pi

Si c'est votre premier Raspberry Pi, le moyen le plus facile (et le plus cher) de le configurer est simplement d'acheter un [kit de bureau pour environ 100 $](https://www.raspberrypi.org/products/raspberry-pi-4-desktop-kit/). Il contient tout ce dont vous avez besoin pour un ordinateur, à l'exception de l'écran.

Si vous utilisez le Pi comme serveur de développement personnel, vous n'aurez PAS besoin d'un écran après la configuration initiale. Vous pouvez simplement vous connecter en SSH depuis votre ordinateur portable une fois qu'il est allumé !

[Apprenez comment](https://www.secondstate.io/articles/raspberry-pi-for-free-20200709/) obtenir votre kit de démarrage Raspberry Pi gratuitement lorsque vous participez à cet [exercice d'apprentissage d'application web haute performance](https://www.secondstate.io/articles/getting-started-with-rust-function/).

Bien sûr, si vous avez des pièces d'ordinateur de rechange, telles que des cartes MicroSD, une alimentation USB, un clavier et une souris, vous pourriez économiser de l'argent en n'achetant que les cartes. Vous pourriez obtenir une carte Raspberry Pi Zero pour 5 $ et une carte Raspberry Pi 4 pour 35 $.

Mais ce qui manque à la carte est une carte MicroSD qui sert de "disque dur" pour stocker le système d'exploitation et les données. Vous pouvez acheter une carte MicroSD de 16 Go pour 10 $ en ligne, un lecteur de carte MicroSD, et utiliser le [Raspberry Pi Imager](https://www.raspberrypi.org/downloads/) pour charger un système d'exploitation sur la carte MicroSD depuis votre ordinateur portable.

Les deux choix populaires sont Raspberry Pi OS et Ubuntu Linux. Tous deux sont des distributions Linux basées sur Debian. La plupart des kits de démarrage préinstallent le Raspberry Pi OS sur leurs cartes MicroSD (il est appelé NOOBS).

Dans les deux sections suivantes, je vais vous guider à travers les deux systèmes d'exploitation.

## Comment configurer Raspberry Pi OS

Une fois que vous avez inséré la carte MicroSD avec NOOBS et connecté un écran, un clavier et une souris, vous pouvez allumer l'alimentation !

À partir de là, suivez simplement les instructions à l'écran pour installer Raspberry Pi OS (précédemment connu sous le nom de Raspbian OS). Ensuite, configurez un mot de passe pour l'utilisateur pi et configurez la connexion WiFi.

Après vous être connecté, allez dans le menu Préférences → Configuration de Raspberry Pi et activez SSH. Cela vous permettra de vous connecter au Pi depuis un autre ordinateur.

**Note** : afin d'utiliser le Pi comme serveur "sans tête", vous pourriez demander une adresse IP statique à votre routeur. À l'avenir, vous pourrez simplement allumer le Pi et vous y connecter via SSH depuis vos autres ordinateurs ou téléphones.

Le Raspberry Pi OS est dérivé de la distribution Linux Debian. Il est livré avec un environnement UI de bureau complet avec un navigateur web moderne, un terminal de ligne de commande et des programmes d'apprentissage tels que des IDE pour Python, Java et Scratch.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/IMG_8672.JPG align="left")

*Mon Raspberry Pi 4 avec Raspberry Pi OS configuré. Remarquez la petite taille de l'ordinateur lui-même.*

Pour nos besoins, nous nous intéressons principalement à l'installation de logiciels de développement et de serveur via le terminal de ligne de commande.

À ce stade, vous pouvez également trouver l'adresse IP du Pi sur votre réseau local en exécutant la commande suivante. Ensuite, vous pouvez vous connecter en SSH au Pi en utilisant cette adresse IP locale, le nom d'utilisateur pi et le mot de passe que vous avez donné à pi pendant la configuration.

```javascript
$ hostname -I
192.168.2.108 172.17.0.1
```

Vous pouvez trouver une [liste complète des paquets logiciels installés sur Raspberry Pi OS ici](https://n8henrie.com/2019/08/list-of-default-packages-on-raspbian-buster-lite/). Il est toujours bon de mettre à jour et de passer à la dernière version des paquets. Exécutez la commande ci-dessous et soyez patient. Cela peut prendre une heure.

```javascript
$ sudo apt update && sudo apt upgrade
```

## Comment configurer Ubuntu Server 20.04

Le Raspberry Pi OS est principalement orienté vers une expérience de bureau. Pour les développeurs qui souhaitent utiliser le dispositif comme serveur ou appareil IoT, Ubuntu Linux est un bien meilleur choix. Il dispose des derniers paquets logiciels et bibliothèques, et pourrait être bien plus efficace sans les fenêtres de bureau, le navigateur web, Java, les jeux et les outils d'apprentissage.

Vous pouvez télécharger les [images Ubuntu Server pour Raspberry Pi](https://ubuntu.com/download/raspberry-pi) depuis le web et les charger sur une carte MicroSD. Mais peut-être qu'une méthode beaucoup plus facile est d'utiliser simplement le [Raspberry Pi Imager](https://www.raspberrypi.org/downloads/), de sélectionner Ubuntu Server 20.04 TLS dans le menu et d'écrire sur une carte MicroSD vide.

Une fois la carte MicroSD préparée, vous devriez [suivre ces instructions](https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi#3-wifi-or-ethernet) pour entrer le nom et le mot de passe de votre réseau WiFi. Cela permet à l'appareil Raspberry Pi de se connecter au réseau dès qu'il démarre.

En gros, vous pouvez simplement insérer la carte MicroSD dans le Raspberry Pi, connecter l'alimentation USB, puis attendre qu'il se connecte. Vous pouvez trouver l'adresse IP de l'appareil `raspberrypi` depuis votre routeur WiFi, puis vous y connecter en SSH depuis n'importe quel ordinateur de votre réseau.

Le nom d'utilisateur et le mot de passe initiaux sont `ubuntu / ubuntu`. Il n'est même pas nécessaire de connecter un moniteur ou un clavier. C'est tout pour une configuration complètement sans tête !

**Note** : si, pour une raison quelconque, votre Raspberry Pi ne peut pas se connecter au WiFi au démarrage, vous pouvez y connecter un écran HDMI et un clavier USB. Ensuite, [suivez ces instructions](https://linuxconfig.org/ubuntu-20-04-connect-to-wifi-from-command-line) pour déboguer et configurer le WiFi sur le système en cours d'exécution.

Ensuite, installons la pile d'outils de développement sur le Pi.

## Installer Git

J'installe toujours Git sur tous mes environnements de développement car beaucoup de logiciels peuvent être directement récupérés depuis des dépôts Git. Cela me évite de télécharger et de copier.

Git me permet également de sauvegarder et de sauvegarder mon propre travail dans des dépôts privés. Pour un petit ordinateur comme le Raspberry Pi, je vous recommande de sauvegarder votre travail dans Git au cas où vous perdriez l'appareil ou la carte MicroSD.

La commande suivante installe Git :

```javascript
$ sudo apt install git
```

## Installer Node.js

Pour transformer le Raspberry Pi en un serveur de développement personnel pour les applications web, vous devez installer un environnement d'exécution d'application web moderne.

Pour la plupart des développeurs aujourd'hui, le meilleur point de départ est Node.js, qui vous permet d'écrire des applications côté serveur en JavaScript. Les deux commandes suivantes installent Node.js sur votre Pi.

```javascript
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo bash -
$ sudo apt install nodejs
```

Vous pouvez vérifier que l'installation est correcte en exécutant les deux commandes suivantes. Node et npm sont maintenant disponibles.

```javascript
$ node -v
v10.19.0
$ npm -v
5.8.0
```

À partir de là, vous pouvez utiliser npm pour installer des modules. Par exemple, un module npm couramment utilisé est le framework express pour les applications web.

```javascript
$ npm install express
```

Maintenant, vous pouvez suivre l'[exemple hello world d'ExpressJS](https://expressjs.com/en/starter/hello-world.html) pour créer un serveur web sur votre Pi et utiliser des navigateurs web depuis n'importe quel ordinateur de votre réseau pour accéder à l'application !

## Installer Rust

Rust est un langage de programmation en pleine croissance pour écrire à la fois des applications système et web. Il est proche du matériel, performant et sûr en mémoire. Cela fait de Rust un excellent langage pour écrire des applications sur des appareils à ressources limitées comme le Raspberry Pi.

De plus, Rust est le langage de programmation le plus apprécié par les utilisateurs de StackOverflow depuis cinq ans consécutifs. Cela vaut vraiment la peine d'apprendre !

Un cas d'utilisation important de Rust est de compiler [des fonctions Rust en WebAssembly et de les exécuter dans des applications Node.js](https://www.secondstate.io/articles/getting-started-with-rust-function/) pour atteindre [des performances, une sécurité et une portabilité du code](https://www.secondstate.io/articles/why-webassembly-server/). C'est un excellent choix pour exécuter des applications web intensives en calcul sur un petit [appareil Raspberry Pi](https://www.secondstate.io/articles/get-started-with-raspberry-pi-20200708/). En fait, vous pourriez [obtenir un kit de démarrage Raspberry Pi gratuit](https://www.secondstate.io/articles/raspberry-pi-for-free-20200709/) si vous apprenez à le faire.

Note : strictement parlant, vous n'avez pas besoin d'installer les outils Rust sur le Pi. Vous avez généralement seulement besoin d'exécuter des programmes Rust sur le Pi. Vous pouvez compiler votre programme Rust sur n'importe quel ordinateur, puis copier les binaires compilés sur le Pi.

Mais avec le CPU puissant, vous pouvez compiler des programmes Rust sur le Raspberry Pi. Alors pourquoi pas ?

La commande suivante installe la chaîne d'outils du compilateur Rust sur le Pi.

```javascript
$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Exécutez la commande suivante pour configurer le bon chemin sans vous déconnecter et vous reconnecter.

```javascript
$ source $HOME/.cargo/env
```

La commande ci-dessus installe également le gestionnaire de paquets Rust appelé cargo. La plupart des développeurs Rust utilisent cargo pour construire et partager leur travail.

```javascript
$ cargo -V
cargo 1.44.1 (88ba85757 2020-06-11)
```

Ensuite, vous pouvez cloner notre [dépôt d'apprentissage Rust](https://github.com/second-state/wasm-learning/) et apprendre à partir d'exemples.

```javascript
$ git clone https://github.com/second-state/wasm-learning.git
```

Voici l'[exemple hello world](https://www.secondstate.io/articles/a-rusty-hello-world/). Amusez-vous !

```javascript
$ cd wasm-learning/rust/hello
$ cargo build
   Compiling hello v0.1.0 (/home/pi/Dev/wasm-learning/rust/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 4.35s
$ target/debug/hello
Hello, world!
```

Consultez le [site web officiel de Rust](https://www.rust-lang.org/learn) et le livre [Rust by Example](https://rust-by-example-ext.com/) pour plus de ressources d'apprentissage.

## Apprendre Docker

Nous avons vu que Raspberry Pi OS et Ubuntu Server sont tous deux des distributions Linux très capables avec de nombreux paquets logiciels.

Mais que faire si je veux tester des applications sur d'autres systèmes d'exploitation ? Dois-je tout effacer et réinstaller un système d'exploitation différent sur la carte MicroSD ? La réponse est non. Vous pouvez simplement utiliser Docker ! Les deux commandes suivantes installent Docker sur le Raspberry Pi :

```javascript
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh
```

Exécutez la commande suivante pour pouvoir utiliser Docker en tant qu'utilisateur pi :

```javascript
$ sudo usermod -aG docker pi
```

La commande d'information Docker montre que Docker est maintenant installé sur un système ARM avec Raspberry Pi OS.

```javascript
$ docker info
... ...
 Kernel Version: 4.19.118-v7l+
 Operating System: Raspbian GNU/Linux 10 (buster)
 OSType: linux
 Architecture: armv7l
 CPUs: 4
 Total Memory: 3.814GiB
 Name: raspberrypi
 ID: XERI:ZVVZ:XQVA:HXSH:KRPI:6GL2:5QRE:E7GZ:Z72Q:6SGF:CEI6:GKTC
 Docker Root Dir: /var/lib/docker
... ...
```

Ensuite, vous pouvez tirer une image Docker pour la dernière distribution Ubuntu, l'exécuter et vous connecter à Ubuntu en tant qu'utilisateur de ligne de commande.

```javascript
$ docker pull ubuntu
... ...
$ docker run -it ubuntu bash
root# ... entrer des commandes ...
```

## Qu'est-ce qui suit ?

Dans cet article, nous avons abordé les bases et appris comment transformer votre appareil Raspberry Pi 4 en un serveur de développement personnel pour les développeurs de logiciels.

Il y a beaucoup à apprendre sur Git, Node.js, Rust, WebAssembly et Docker. Il existe également de nombreuses autres piles de développement que vous pouvez installer sur le Raspberry Pi.

[Obtenez votre kit Raspberry Pi gratuit](https://www.secondstate.io/articles/raspberry-pi-for-free-20200709/) et faites-nous savoir ce que vous en avez fait !

[Abonnez-vous à notre newsletter](https://webassemblytoday.substack.com/) et restez en contact.