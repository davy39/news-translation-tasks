---
title: Maîtriser la ligne de commande
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-05T17:11:11.000Z'
originalURL: https://freecodecamp.org/news/conquering-the-command-line-f85f5e46c07c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*NvuIEr51nwGNxv7O3TXcpA.png
tags:
- name: mac
  slug: mac
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: terminal
  slug: terminal
- name: unix
  slug: unix
seo_title: Maîtriser la ligne de commande
seo_desc: 'By Monica Powell

  A brief guide to getting started on UNIX/Mac OS terminal

  When I was first introduced to the command line I really had to adjust to navigating
  my computer in a black box with just text. So I avoided the command line as much
  as possibl...'
---

Par Monica Powell

#### Un guide rapide pour commencer sur le terminal UNIX/Mac OS

Lorsque j'ai été initiée à la ligne de commande, j'ai vraiment dû m'adapter à la navigation sur mon ordinateur dans une boîte noire avec seulement du texte. J'ai donc évité la ligne de commande autant que possible. J'étais habituée aux indices visuels et aux retours qu'un ordinateur fournit généralement. À bien des égards, cela donnait l'impression que je devais réapprendre à utiliser un ordinateur via la ligne de commande.

Pourtant, depuis que j'ai appris à naviguer sur mon ordinateur en utilisant les commandes UNIX, j'ai compris que la ligne de commande n'a pas à être une chose effrayante simplement parce qu'il n'y a pas de retour visuel lorsque l'on tape un mot de passe sur la ligne de commande. Pour des raisons de sécurité, rien ne s'affiche lorsque vous tapez votre mot de passe pour indiquer que des caractères ont été saisis.

#### Qu'est-ce que la ligne de commande ?

La ligne de commande est un logiciel qui exécute des commandes ou des instructions pour qu'un ordinateur manipule ou interagisse avec son système de fichiers.

### Qu'est-ce qu'UNIX ?

#### Pourquoi utiliser la ligne de commande ?

* Plus rapide pour modifier, naviguer entre les fichiers
* Capacité à installer des logiciels en tant que superutilisateur
* Peut voir les fichiers cachés dotfiles  
Les dotfiles sont des fichiers de configuration UNIX, ils tendent à être des fichiers précédés d'un `.` et sont cachés aux utilisateurs normaux.  
Vous pouvez [en apprendre davantage sur la prise en main des dotfiles dans cet article](https://medium.com/@webprolific/getting-started-with-dotfiles-43c3602fd789)).

Pour commencer sur la ligne de commande, vous devez naviguer vers vos applications et ouvrir l'application **Terminal**.

![Image](https://cdn-media-1.freecodecamp.org/images/0wX7Il6ZWb4qFXWhJ1rAvbrEAquvv0mWSDcV)
_Ci-dessus se trouve l'icône du Terminal sur Mac._

### Créer un dossier de site web de base sur la ligne de commande

![Image](https://cdn-media-1.freecodecamp.org/images/q-nEv8AuA5alFW0jj8uEDZfN7Re2bCsyWNbV)
_Structure de dossier d'un projet exemple_

Un dossier avec la structure ci-dessus peut être créé sur la ligne de commande en tapant les commandes à l'intérieur d'un répertoire vide :

![Image](https://cdn-media-1.freecodecamp.org/images/skROBs72rmbM9R19Xll-9fVTzLXZoEi1VHrc)
_Nous commençons à l'intérieur d'un répertoire vide !_

* Créer un répertoire (également appelé dossier) nommé personal-website  
`mkdir personal-website`

![Image](https://cdn-media-1.freecodecamp.org/images/nXYWE7E1AQgDoGiFXHYRmmop7jAGy7HR7Xt-)
_Nous avons créé un dossier nommé personal-website_

* Naviguer à l'intérieur du répertoire nommé personal-website  
`cd personal-website`
* créer un répertoire, à l'intérieur du dossier personal-website nommé assets  
`mkdir assets`

![Image](https://cdn-media-1.freecodecamp.org/images/hwOipEstl7aPZxV1youY746JZnJqcuv8j5VU)
_Nous avons créé un dossier à l'intérieur de personal-website pour contenir tous nos assets_

* Naviguer à l'intérieur du dossier assets qui se trouve à l'intérieur du dossier personal-website  
`cd assets`
* créer un répertoire, à l'intérieur du dossier assets nommé images  
`mdkir images`
* créer un répertoire, à l'intérieur du dossier assets nommé js  
`mkdir js`
* créer un répertoire, à l'intérieur du dossier assets nommé css  
`mkdir css`

![Image](https://cdn-media-1.freecodecamp.org/images/VjWywXJ3fXn8IIUSS1rUS82fWBelN6qVwg28)
_Nous avons créé des dossiers à l'intérieur de personal-website/assets pour stocker les assets de notre projet_

![Image](https://cdn-media-1.freecodecamp.org/images/loq-rOeylfEFovUlcja88GAhSSXTq4JRjjbC)

Oups ! Nous avons oublié de créer un fichier index.html :(

Nous sommes dans le dossier assets et voulons un fichier index.html dans notre dossier principal personal-website. Taper `cd ..` nous déplacera hors du dossier assets et dans le répertoire parent qui est personal-website. Maintenant que nous sommes dans le dossier personal-website, si nous tapons `touch index.html`, un fichier index.html vide sera créé.

![Image](https://cdn-media-1.freecodecamp.org/images/ws7T-u5nT2AWqrsKAipU2E5upuEmeN18gCC5)

### Voici quelques commandes de terminal fréquemment utilisées :

#### Commandes pour naviguer/manipuler le système de fichiers

**ls**  
 **lister** le contenu d'un répertoire

**pwd**  
**afficher le répertoire de travail** pour que le terminal affiche le répertoire dans lequel vous travaillez actuellement

**touch**   
créer ou ouvrir un fichier sans apporter de modifications  
très pratique lorsque vous souhaitez créer des fichiers vides sans quitter la ligne de commande

**sudo**   
cela vous permet d'exécuter des commandes en tant que **super utilisateur**

**mv**   
**déplacer** un fichier ou un répertoire  
cela peut être utilisé pour déplacer ou renommer un fichier en mettant à jour le chemin du fichier

**cd**   
**changer le répertoire actuel** sur lequel vous travaillez afin que vous puissiez accéder à des fichiers sur une autre partie du système  
`cd` vous déplace vers le répertoire racine (dossier de niveau supérieur sur l'ordinateur — généralement l'utilisateur actuel)  
`cd .` répertoire actuel   
`cd ..` navigue vers le répertoire deux niveaux plus haut

**mkdir**   
**créer** un nouveau **répertoire** (ou un dossier)

#### **Commandes pour installer des logiciels**

Vous pouvez installer certains logiciels à partir de la ligne de commande en utilisant les commandes suivantes :

* en Python `pip install <package nam`e>.   
Pip est un gestionnaire de paquets logiciels pour Python.
* en JavaScript `npm install <package na`me>   
NPM est un gestionnaire de paquets pour les pages JavaScript.

#### Commandes pour exécuter des logiciels

Pour exécuter un script sur la ligne de commande, vous devez fournir une invite de commande et un nom de fichier. Voici quelques exemples :

* en Java `javac filename.java` puis `java filename` compile les projets Java et les exécute.
* en Python `python filename` exécute les scripts Python.

Si vous trouvez que vous répétez beaucoup de commandes, vous pouvez faire défiler vos commandes récentes en utilisant les flèches haut/bas, les modifier et les réexécuter en naviguant jusqu'à elles puis en appuyant sur entrée.

#### Ressources supplémentaires pour commencer avec les invites de commande

* [MIT Terminus (jeu interactif pour apprendre la ligne de commande)](http://web.mit.edu/mprat/Public/web/Terminus/Web/main.html)
* [Codecademy Apprendre la ligne de commande](https://www.codecademy.com/learn/learn-the-command-line)
* [Apprendre Python à la dure : Cours accéléré sur la ligne de commande](https://learnpythonthehardway.org/book/appendixa.html)

#### Décorer la ligne de commande

Vous pouvez complètement personnaliser les couleurs et les sorties sur la ligne de commande pour mieux répondre à vos besoins visuels et esthétiques.

Voici comment j'ai rendu ma ligne de commande plus jolie :

Comment installer Tomorrow Night  
[https://github.com/chriskempson/tomorrow-theme/blob/master/OS%20X%20Terminal/Tomorrow%20Night.terminal](https://github.com/chriskempson/tomorrow-theme/blob/master/OS%20X%20Terminal/Tomorrow%20Night.terminal)

[**Personnaliser le terminal**](https://mindthecode.com/customize-the-terminal/)  
[_J'adore le terminal. En plus du fait qu'il vous donne l'air génial en l'utilisant, il peut aussi faire environ un milliard de choses..._mindthecode.com](https://mindthecode.com/customize-the-terminal/)

_Si vous avez aimé lire cet article, envisagez de cliquer sur le bouton d'applaudissements ?. Vous voulez voir plus de mon travail ? Consultez m[on GitHub](https://github.com/M0nica/) pour voir mon code et en savoir plus sur mon expérience de développement sur h[ttp://aboutmonica.com.](http://aboutmonica.com)_