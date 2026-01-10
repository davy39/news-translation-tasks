---
title: Comment installer le Intel Movidius Neural Compute Stick
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-26T16:12:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-the-intel-movidius-neural-compute-stick-b9db16d493a7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sPZNuScv3C93RsCfONjWUg.jpeg
tags:
- name: AI
  slug: ai
- name: Deep Learning
  slug: deep-learning
- name: iot
  slug: iot
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Comment installer le Intel Movidius Neural Compute Stick
seo_desc: 'By Rishal Hurbans

  In 2017 I was approached by Intel to join their Innovator Programme. After a couple
  interviews I was inducted as an Intel Innovator in the AI space. The idea of the
  initiative is to support technologists around the world involved in...'
---

Par Rishal Hurbans

En 2017, Intel m'a approché pour rejoindre leur Programme Innovateur. Après quelques entretiens, j'ai été intégré en tant qu'Innovateur Intel dans le domaine de l'IA. L'idée de cette initiative est de soutenir les technologues du monde entier impliqués dans la communauté en fournissant du matériel de pointe, des opportunités de prise de parole, et une plateforme pour promouvoir leur travail et engager plus de personnes.

Intel m'a envoyé un Movidius Neural Compute Stick. C'est une clé USB un peu plus grande qu'une clé USB standard, spécialement conçue pour entraîner et principalement exécuter des graphes de réseaux neuronaux, ce qui est particulièrement utile pour exécuter des réseaux d'apprentissage profond où l'apprentissage se fait à partir de médias tels que des images et des vidéos. Je couvrirai probablement l'apprentissage profond dans un futur article. Selon les benchmarks, le Movidius Neural Compute Stick promet d'exécuter des modèles jusqu'à cinq fois plus rapidement qu'un ordinateur portable standard.

À la réception de l'appareil, j'ai réalisé qu'il ne fonctionne actuellement que sur Ubuntu 16.04 et le Raspberry Pi 3. Étant un utilisateur de macOS, cela posait un peu problème, alors j'ai décidé de faire tourner une machine virtuelle Ubuntu pour commencer à bidouiller avec l'appareil. Ce guide décrit comment j'ai réussi à configurer un environnement acceptable pour le Movidius stick, et décrit brièvement ses capacités.

### Installation d'une machine virtuelle

La première étape consiste à mettre en place une machine virtuelle (VM). Bien qu'il existe plusieurs options logicielles pour les machines virtuelles, Virtual Box est une solution gratuite, simple à configurer et à utiliser. Des alternatives comme Parallels et VMWare peuvent offrir de meilleures performances si la VM est destinée à être utilisée comme poste de travail principal.

1. [Télécharger Virtual Box](https://www.virtualbox.org/wiki/Downloads).
2. Installer Virtual Box en utilisant l'installateur téléchargé.
3. [Télécharger Virtual Box Extension Pack](https://www.virtualbox.org/wiki/Downloads).
4. Installer Virtual Box Extension Pack en utilisant l'installateur téléchargé.
5. [Télécharger l'image ISO 64 bits d'Ubuntu 16.04](http://releases.ubuntu.com/16.04/).
6. Créer une nouvelle machine virtuelle.
7. Charger l'image Ubuntu 16.04 comme disque optique sur la nouvelle machine virtuelle.
8. Démarrer la machine virtuelle.
9. Suivre les étapes pour installer Ubuntu sur la machine virtuelle.

Mes spécifications de machine virtuelle :

Voici les configurations que j'ai utilisées. N'hésitez pas à ajuster la mémoire (RAM) et l'allocation du disque dur selon vos besoins. Gardez à l'esprit que sur-allouer les ressources entraînera de mauvaises performances sur le système d'exploitation hôte.

* Nom : Ubuntu 16.04
* Type : Linux
* Taille de la mémoire : 3072 Mo
* Disque dur virtuel : 40 Go

### Prérequis sur Ubuntu 16.04

Avant de faire fonctionner le SDK et les exemples, certaines dépendances sont nécessaires pour garantir que l'environnement de développement est prêt et que les outils nécessaires sont disponibles. Cela implique de mettre à jour Ubuntu et de s'assurer que vous avez Python, PIP (PIP Installs Packages), et Git pour cloner les dépôts de code.

1. Mettre à jour Ubuntu : Une fenêtre contextuelle devrait apparaître pour mettre à jour Ubuntu ou vous pouvez utiliser cette commande dans le Terminal : `sudo apt-get upgrade`
2. Pour utiliser le Terminal, cliquez simplement sur le menu Ubuntu et recherchez l'application "Terminal".
3. Assurez-vous que Python 3 est installé en utilisant le Terminal : `python3 --version`
4. Si Python 3 n'est pas installé, installez-le en utilisant le Terminal : `sudo apt install python3`
5. Assurez-vous que pip 3 est installé en utilisant le Terminal : `pip3 --version`
6. Si pip 3 n'est pas installé, installez-le en utilisant le Terminal : `sudo apt install python3-pip`
7. Assurez-vous que Git est installé en utilisant le Terminal : `git --version`
8. Si Git n'est pas installé, installez-le en utilisant le Terminal : `sudo apt install git-all`

### Assurez-vous que le Movidius Stick est reconnu

Ensuite, nous passons à la configuration du Movidius stick. Cela implique de s'assurer que l'appareil USB est reconnu par la machine virtuelle. Puisqu'une machine virtuelle accède au matériel via le système d'exploitation hôte, une certaine configuration est nécessaire pour des appareils comme le Movidius où les pilotes ne sont pas distribués couramment.

1. Branchez le Movidius stick dans un port USB.
2. Utilisez la commande `lsusb` dans le Terminal pour déterminer s'il est reconnu par la VM et Ubuntu. Vous devriez voir le Movidius stick dans la liste des appareils USB.
3. S'il n'est pas reconnu, éteignez la VM et suivez les instructions ci-dessous.
4. Accédez aux paramètres de la VM dans Virtual Box. Choisissez Ports > USB.
5. Ajoutez un nouveau filtre pour USB 2 en fournissant uniquement l'ID du fournisseur comme `03e7`
6. Ajoutez un nouveau filtre pour USB 3 en fournissant uniquement l'ID du fournisseur comme `040e`
7. Démarrez la VM Ubuntu.
8. Utilisez la commande `lsusb` pour lister les appareils USB, et le Movidius stick devrait maintenant être reconnu. Dans mon cas, il a fonctionné en étant branché dans un port USB 3 mais il a été reconnu comme USB 2 avec l'ID du fournisseur `03e7`.

### Installer NCSDK

Le NCSDK est nécessaire pour interagir avec le Movidius stick. Le but du SDK est de fournir une interface pour le matériel de calcul neuronal. Cela signifie que des programmes d'apprentissage automatique peuvent être écrits pour tirer parti de l'optimisation du matériel spécifique en utilisant ce SDK.

1. Clonez le dépôt NCSDK (Neural Compute Software Development Kit) dans le Terminal : `git clone https://github.com/movidius/ncsdk.git`
2. Si vous avez des problèmes avec le dépôt, téléchargez le NCSDK ici. J'ai utilisé la version 1 :

1.12.00.01 : 
[https://ncs-forum-uploads.s3.amazonaws.com/ncsdk/ncsdk-01_12_00_01-full/ncsdk-1.12.00.01.tar.gz](https://ncs-forum-uploads.s3.amazonaws.com/ncsdk/ncsdk-01_12_00_01-full/ncsdk-1.12.00.01.tar.gz)

2.05.00.02 : 
[https://ncs-forum-uploads.s3.amazonaws.com/ncsdk/ncsdk-02_05_00_02-full/ncsdk-2.05.00.02.tar.gz](https://ncs-forum-uploads.s3.amazonaws.com/ncsdk/ncsdk-02_05_00_02-full/ncsdk-2.05.00.02.tar.gz)

Ensuite, effectuez les étapes suivantes :

1. Accédez au répertoire NCSDK dans le Terminal.
2. Construisez le SDK dans le Terminal : `make install`
3. Construisez les exemples : `make examples`

### Construire et exécuter des exemples

Enfin, nous allons exécuter quelques exemples et voir le Movidius en action. Le Neural Compute App Zoo est un dépôt d'exemples qui démontrent comment le NC SDK et le Movidius stick peuvent être utilisés pour entraîner et traiter des graphes de réseaux neuronaux plus efficacement que les CPU typiques.

L'exemple que nous allons examiner est la classification d'images. Au lieu de créer notre propre modèle, ce qui prendrait d'innombrables heures de collecte de données, de traitement de données et d'entraînement, nous allons simplement utiliser GoogLeNet — un modèle bien entraîné pour la classification d'images par Google. Le moteur de graphe utilisé pour traiter le modèle sera Caffe. Caffe est un framework de vision par machine largement utilisé qui excelle dans les tâches liées aux images.

1. Clonez le dépôt d'exemples dans le Terminal : `git clone https://github.com/movidius/ncappzoo.git`
2. Accédez au répertoire cloné : `cd ncappzoo`
3. Construisez les exemples : `make`
4. Installez sk-image s'il est manquant : `pip3 install scikit-image`
5. Créez le graphe GoogleImageNet de Caffe : `cd caffe && make`
6. Accédez à image-classifier : `cd apps/image-classifier`
7. Exécutez l'exemple : `python3 image-classifier.py`
8. Succès ! Vous devriez voir les résultats du classificateur d'images de base.

![Image](https://cdn-media-1.freecodecamp.org/images/hj7Llu4g4V5eQA3NMcyMQy0qdtz9Pxwo8d4C)

### Allez de l'avant et conquérez

Bien que le Movidius Neural Compute Stick ne supporte actuellement que Raspbian et Ubuntu, il est possible de le faire fonctionner sur votre plateforme. Bientôt, nous verrons l'IA sur des appareils de périphérie tels que des drones, des caméras de domotique et d'autres appareils IoT via des solutions matérielles spécifiques comme le Movidius. Explorez les exemples et construisez votre propre IA, partagez votre travail et aidez à façonner l'avenir.

Restez en contact ✉️ Je suis actif sur Twitter : [@RishalHurbans](http://twitter.com/RishalHurbans)

Je suis disponible par email via rishal[at]prolificidea[dot]com

Je suis également en train d'écrire plus, alors suivez-moi sur Medium.

**Si vous avez aimé cet article, n'hésitez pas à l'applaudir, une fois, cinq fois, ou cinquante fois. Cela aidera les autres à le voir.**