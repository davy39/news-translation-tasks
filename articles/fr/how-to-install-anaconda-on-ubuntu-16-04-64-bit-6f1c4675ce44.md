---
title: 'Une introduction à Anaconda : qu''est-ce que c''est et comment l''installer'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-09T16:58:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-anaconda-on-ubuntu-16-04-64-bit-6f1c4675ce44
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5FCJgZ0I7Qo9bHe8USGfvw.png
tags:
- name: anaconda
  slug: anaconda
- name: Data Science
  slug: data-science
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: Ubuntu
  slug: ubuntu
seo_title: 'Une introduction à Anaconda : qu''est-ce que c''est et comment l''installer'
seo_desc: 'By Nandhini Saravanan

  A simple guide to Anaconda and its installation on Ubuntu 16.04 (64-bit).


  [Anaconda Logo](https://en.wikipedia.org/wiki/Anaconda(Python_distribution)" rel="noopener"
  target="blank" title=")

  Hey everyone. I wrote this post to gu...'
---

Par Nandhini Saravanan

#### Un guide simple pour Anaconda et son installation sur Ubuntu 16.04 (64-bit).

![Image](https://cdn-media-1.freecodecamp.org/images/1*5FCJgZ0I7Qo9bHe8USGfvw.png)
_[Logo Anaconda](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution)" rel="noopener" target="_blank" title=")_

Salut à tous. J'ai écrit cet article pour vous guider à travers l'installation d'Anaconda sur les versions Ubuntu. De plus, il couvre divers détails sur Anaconda et le domaine dans lequel il est utilisé.

### Pour commencer, qu'est-ce qu'Anaconda ?

Avant de nous pencher sur ce qu'Anaconda signifie vraiment et ce qu'il en est, nous allons d'abord apprendre à connaître Conda.

En citant le blog officiel de Conda :

> Conda est un **système de gestion de paquets open source** et un système de gestion d'environnements qui fonctionne sur Windows, macOS et Linux.

> Conda installe, exécute et met à jour rapidement les paquets et leurs dépendances. Conda crée, sauvegarde, charge et bascule facilement entre les environnements sur votre ordinateur local.

> Il a été créé pour les programmes **Python**, mais il peut **packager et distribuer des logiciels** pour n'importe quel langage.

La question suivante sur la table est : pourquoi Conda, tout à coup ? Nous savons tous que c'est un système de gestion de paquets utilisé pour installer et gérer des paquets logiciels écrits en Python.

Celui-ci a aussi ses limitations. Il ne peut être utilisé que pour les paquets Python.

`pip` est centré autour de Python, négligeant les dépendances de bibliothèques non-Python, telles que HDF5, MKL, LLVM qui n'ont pas de fichier de configuration dans leur code source.

Pour le dire en termes simples :

`pip` est un gestionnaire de paquets qui facilite l'installation, la mise à jour et la désinstallation de **paquets python**. Il fonctionne avec des environnements virtuels **python**.

`Conda` est un gestionnaire de paquets pour **n'importe quel logiciel** (installation, mise à jour et désinstallation). Il fonctionne avec des environnements virtuels **système**.

Conda est un outil de packaging et d'installation qui vise à faire plus que ce que `pip` fait : gérer les dépendances de bibliothèques _en dehors_ des paquets Python ainsi que les paquets Python eux-mêmes.

Conda crée également un environnement virtuel.

#### Comment Anaconda entre-t-il en jeu ?

Conda est écrit entièrement en Python, ce qui le rend plus facile à utiliser dans les environnements virtuels Python. De plus, nous pouvons utiliser Conda pour les bibliothèques C, les paquets R, les paquets Java, etc.

Il installe des binaires. L'outil `conda build` construit des paquets à partir de la source et `conda install` installe des choses à partir de paquets conda construits.

Conda est le gestionnaire de paquets d'Anaconda, la distribution Python fournie par Continuum Analytics. Une ligne succincte pour décrire Anaconda est celle-ci :

> **_Anaconda est une distribution Python et R. Elle vise à fournir tout ce dont vous avez besoin (en termes de Python) pour les tâches de science des données._**

Anaconda est un ensemble de binaires qui inclut Scipy, Numpy, Pandas ainsi que toutes leurs dépendances.

**Scipy** est un paquet d'analyse statistique.

**Numpy** est un paquet de calcul numérique.

**Pandas** est une couche d'abstraction de données qui expose un moyen de fusionner et de transformer des données.

**Anaconda nous aide en regroupant tout cela en une seule fois**.

Le binaire Anaconda est un installeur qui construit tous ces paquets et leurs dépendances dans votre système.

Pour plus d'informations sur Anaconda, visitez son blog officiel : [https://anaconda.org/](https://anaconda.org/)

### Installer de manière plus facile

L'installation de fichiers peut parfois être un vrai désordre, mais Anaconda est beaucoup plus convivial que vous ne le pensez. Je préfère Ubuntu, car l'installation ne nécessite que quelques commandes solides et une bonne connexion réseau. Cela semble beaucoup plus facile. Voici les étapes suivantes pour l'installation d'Anaconda.

(Tout ce processus d'installation fonctionne uniquement sur les ordinateurs 64 bits).

#### Étape 1 : Télécharger le script bash d'Anaconda

Téléchargez la dernière version du script bash d'installation d'Anaconda depuis leur [site officiel](https://anaconda.org/). Il peut être téléchargé en exécutant une commande curl. Si vous n'avez pas curl installé dans votre système, installez-le en exécutant la commande suivante.

```
sudo apt-get update
sudo apt-get install curl
```

Allez dans le dossier /tmp.

```
cd /tmp
```

Après avoir installé curl, exécutez la commande suivante en l'utilisant :

```
curl -O https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh
```

L'installation prend généralement quelques minutes car sa taille est d'environ 500 Mo. Veuillez attendre jusqu'à ce que le processus de téléchargement soit terminé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*utuN01gygzbxPM38z0-DMg.png)
_Processus d'installation d'Anaconda_

La capture d'écran jointe a été prise après le téléchargement du script. Assurez-vous d'avoir une connexion stable, sinon des erreurs de téléchargement pourraient survenir.

#### Étape 2 : Vérifier l'intégrité

Pour vérifier l'intégrité des données de l'installeur, nous utilisons un algorithme de hachage cryptographique appelé SHA-2 (Secure Hash Algorithm).

```
sha256sum Anaconda3-4.3.1-Linux-x86_64.sh
```

Une somme de contrôle sera générée à la ligne suivante après l'exécution de la commande.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nbv3yfy9C59Q_kLkpvVVPw.png)
_Vérification de l'intégrité des données à l'aide de la somme de contrôle_

#### Étape 3 : Exécuter le script bash

Nous y sommes presque. Le paquet est téléchargé et nous devons simplement exécuter le script en tapant cette commande.

```
bash Anaconda3-4.3.1-Linux-x86_64.sh
```

Une étape de vérification normale demande si vous souhaitez installer Anaconda. Tapez `yes` pour que l'installation continue.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mQnEPRvUKXMvgKTt4Yss8Q.png)
_Après avoir exécuté le script bash_

#### Étape 4 : Installer les bibliothèques cryptographiques

Cela fait partie du processus précédent. L'installeur demande à l'utilisateur s'il souhaite installer toutes les bibliothèques cryptographiques. Tapez `yes` et vous êtes prêt à partir. Reportez-vous à la capture d'écran ci-dessous. Vous obtiendrez des détails similaires.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LXq81Fwp6lWgrwM9-X7b4A.png)
_Bibliothèques cryptographiques_

#### Étape 5 : Confirmer l'emplacement

La dernière et dernière étape consiste à confirmer le chemin où vous souhaitez placer tous les paquets Anaconda. Après avoir spécifié le chemin, appuyez sur Entrée et vous avez terminé ! Anaconda commencera à installer tous les éléments essentiels dont vous aurez besoin !

![Image](https://cdn-media-1.freecodecamp.org/images/1*UQH2AdCUWxD7NYxcn4mPSg.png)
_Configuration du chemin d'Anaconda_

#### Étape 6 : Activer et vérifier

Pour activer l'installation, nous devons sourcer le fichier `~/.bashrc` en tapant la commande suivante :

```
source ~/.bashrc
```

Vérifiez votre installation en utilisant la commande `conda`.

```
conda list
```

La sortie de tous les paquets disponibles via l'installation d'Anaconda est affichée.

#### J'écris des histoires sur les leçons de vie, le codage, la technologie et les livres. Pour en lire plus, suivez-moi sur [Twitter](https://twitter.com/snandhini98) et [Medium.](http://medium.com/@nandhus05)