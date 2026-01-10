---
title: Guide du débutant pour Raspberry Pi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-23T22:26:53.000Z'
originalURL: https://freecodecamp.org/news/beginners-guide-to-raspberry-pi-6e55080fdaaf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rD9cweBR5NdgFg-l8koTOQ.png
tags:
- name: education
  slug: education
- name: Internet of Things
  slug: internet-of-things
- name: General Programming
  slug: programming
- name: Raspberry Pi
  slug: raspberry-pi
- name: technology
  slug: technology
seo_title: Guide du débutant pour Raspberry Pi
seo_desc: 'By Sean Choi

  It’s the little things that count.


  Raspberry Pi 3 Model B+

  Many question what the term Internet of Things (IoT) means or what it actually represents.
  In simple terms, IoT is a term for categorizing anything that can connect to the
  Inter...'
---

Par Sean Choi

#### Ce sont les petites choses qui comptent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rD9cweBR5NdgFg-l8koTOQ.png)
_Raspberry Pi 3 Model B+_

Beaucoup se demandent ce que signifie le terme _Internet des objets (IoT)_ ou ce qu'il représente réellement. En termes simples, _IoT_ est un terme pour catégoriser tout ce qui peut se connecter à Internet. Cela inclut votre Alexa, HomePod, montre Android, réfrigérateur intelligent Samsung et bien plus encore. Même si vous réalisez que l'IoT est un terme destiné à décrire un groupe de petits appareils qui se connectent à Internet et communiquent entre eux, il reste plutôt flou comment ces petits appareils font ce qu'ils font.

En revanche, tout le monde sait généralement ce que fait un Macbook ou un ordinateur et ce dont ils sont capables. Intéressamment, les composants internes de ces appareils IoT sont très similaires aux ordinateurs que nous utilisons tous les jours, qui incluent une unité de traitement, de la mémoire, un module réseau et/ou Bluetooth et quelques autres capteurs.

Ce que beaucoup de gens ne réalisent pas, c'est à quel point il est facile de créer votre propre appareil _IoT_ en utilisant un petit ordinateur. En fait, vous pourriez vous demander s'il existe même un petit ordinateur prêt à l'emploi, bon marché et puissant. La bonne nouvelle est qu'il existe réellement et qu'il est **vraiment** **puissant.**

### Raspberry Pi est EXACTEMENT Cela.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GzvXMi0Yw0nq3tMRkoSyWQ.png)
_Raspberry Pi 3 (raspberrypi.org)_

[Raspberry Pi](https://amzn.to/2PLBxk1) est un petit ordinateur qui tient confortablement dans votre main. Ne vous laissez pas tromper par sa taille et regardez simplement les spécifications matérielles pour la dernière génération (3+) de Raspberry Pi.

* 1,4 GHz 64 bits quad-core [ARM Cortex-A53](https://en.wikipedia.org/wiki/ARM_Cortex-A53), 1 Go de RAM
* 2,4/5 GHz double bande 802.11ac Wireless LAN, Ethernet 10/100/1000 Mbps
* Bluetooth 4.2
* 4 ports USB, port HDMI complet, port audio jack combiné 3,5 mm et port vidéo composite, 40 broches GPIO
* Emplacement pour carte micro SD, cœur graphique 3D VideoCore IV, interface caméra (CSI), interface d'affichage (DSI),

Comme vous pouvez le voir, cette petite bête abrite un CPU Quad-Core, un sans fil rapide, un module Bluetooth et suffisamment de RAM pour faire la plupart des choses que vous faites sur votre ordinateur. Mieux encore, [cela ne coûte que 35 $](https://amzn.to/2PLBxk1), ou environ un dîner raisonnable (ou [3 toasts à l'avocat à SF](https://sf.eater.com/2017/5/23/15677684/avocado-toast-prices-menu-costs-san-francisco)).

Les Raspberry Pis ont une convention de nommage intéressante. Ils sont catégorisés par une combinaison de nom de modèle et de génération. Les noms de modèles incluent A, A+, B, B+, Zero et Compute Module (Compute Module est principalement destiné aux applications industrielles, donc nous n'en parlerons pas dans cet article).

Chaque modèle est différencié par les connecteurs disponibles et la taille de la carte principale. Il existe diverses générations construites jusqu'à présent, qui sont largement catégorisées par des nombres de 1 à 3. Chaque génération est principalement différenciée par la performance de la puce. La version la plus récente et la plus puissante s'appelle _Raspberry Pi 3+ Model B+_.

Pour référence, voici quelques images qui montrent les parties disponibles dans chacun des modèles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sgjYyv_QE0J8ZHyh48mCiQ.png)
_Raspberry Pi Model Zero_

![Image](https://cdn-media-1.freecodecamp.org/images/1*Zm0VfWGhkxG_wJPyMTXvNA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*E4pQ7ipQ7hGuMt2kstmORQ.png)
_Raspberry Pi 1 Model A (gauche), Raspberry Pi 1 Model A+ révision 1.1 (droite)_

![Image](https://cdn-media-1.freecodecamp.org/images/1*t0OXJ9YgOHEDDPYn63yPxg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*fdW23Z7okJlTkNMyqqT9vQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*NjVZqwr3uKVZu_nd1f5d3g.png)
_Raspberry Pi 1 Model B (gauche), Raspberry Pi 1,2 Model B+ (milieu), Raspberry Pi 3 Model B+ (droite)_

Chaque modèle a ses propres compromis. Par exemple, le Raspberry Pi Model Zero est le plus petit de tous et consomme seulement 100 mA (0,5 W) de puissance en moyenne. (Un ordinateur de bureau moyen abrite une alimentation de 200~1400 W). Mais, il n'abrite qu'un CPU monocœur, a moins de RAM et manque d'un port HDMI complet.

Cependant, sa taille plus petite lui permet de s'adapter à plus d'espaces, ce qui le rend utile pour construire des appareils qui sont contraints par l'espace et la puissance. Ainsi, avoir plusieurs modèles à choisir augmente vos options pour votre projet.

### Quel logiciel utilise-t-il ?

Malheureusement, Raspberry Pi ne fonctionne pas avec Mac OS X ou Windows. Au lieu de cela, il exécute une version de Linux appelée [Raspbian](https://www.raspberrypi.org/downloads/raspberry-pi-desktop/). Vous pouvez choisir d'installer Raspbian sur une carte micro SD vous-même avec l'installateur NOOBS, ou acheter une carte micro SD préchargée comme celle vue [ici](http://amzn.to/2DO09P0). Une fois que vous insérez la carte micro SD avec Raspbian installé et allumez le Raspberry Pi, vous obtenez l'écran de chargement suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*HBm9igWAM0uNQJdViGyGag.jpeg)
_Écran de chargement de Raspbian. Image de [https://alternativeto.net/software/raspbian/](https://alternativeto.net/software/raspbian/" rel="noopener" target="_blank" title=")_

Comme vous pouvez le voir, le bureau ressemble à un bureau régulier sur votre grand PC. Par défaut, vous obtenez un navigateur web, un terminal, un visualiseur d'images, une calculatrice et bien d'autres fonctionnalités.

Raspbian vous permet également d'installer des tonnes de logiciels depuis son propre dépôt de logiciels open source sans frais. Le processus d'installation d'un logiciel est également assez simple. Vous pouvez utiliser la commande _apt-get_, une commande Linux populaire pour installer des logiciels depuis divers dépôts, pour installer tout logiciel disponible.

Par exemple, `sudo apt-get install scratch2` installera le langage de programmation populaire [scratch](https://scratch.mit.edu/). Parcourez divers dépôts et StackOverflow, et vous réaliserez bientôt que vous pouvez faire presque tout avec ces appareils.

### Que pouvez-vous FAIRE ACTUELLEMENT avec cela ?

D'accord, vous avez donc un petit ordinateur qui exécute un tas de logiciels gratuits. Que pouvez-vous faire avec ? Eh bien, voici un projet Python facile et amusant que j'ai mis en œuvre avec un groupe d'élèves de collège dans le cadre d'un cours de codage.

En utilisant un [capteur de température/humidité/pression compatible avec Raspberry Pi avec écran LED](https://amzn.to/2NCMdwd), j'ai enseigné le concept de randomness en utilisant des couleurs aléatoires sur l'écran LED plutôt que des nombres. Mes élèves ont adoré pouvoir interagir visuellement et physiquement avec leur propre code. Vous pouvez voir la vidéo du projet ici :

En utilisant le même appareil, nous avons également construit une calculatrice, un appareil de jeu, une station météo et bien plus encore. Je les ai trouvés très utiles et rentables pour enseigner la programmation introductive aux jeunes étudiants. Je prévois de couvrir les détails de mes programmes dans un article une autre fois.

Un de mes collègues de Stanford a construit une machine à espresso sécurisée personnalisée avec Raspberry Pi pour protéger notre précieux café. L'idée est quelque peu similaire à une serrure de porte sécurisée avec Raspberry Pi comme vu [ici](https://www.youtube.com/watch?v=bAcK80fm1_0).

![Image](https://cdn-media-1.freecodecamp.org/images/1*6oZ2WsV6LCygftHXzgbcig.jpeg)
_Serrure de porte sécurisée avec Raspberry Pi par HackerHouse_

Il existe de nombreux articles sur l'utilisation d'un Raspberry Pi pour construire des appareils IoT amusants et utiles. En voici quelques-uns que j'ai trouvés : [Caméra de sécurité Raspberry Pi](https://pimylifeup.com/raspberry-pi-security-camera/), [Centre multimédia Raspberry Pi](https://www.makeuseof.com/tag/kodi-raspberry-pi-media-center/), [Club de code Raspberry Pi](https://projects.raspberrypi.org/en/codeclub).

### Conclusion

J'espère que cet article donne quelques informations de base sur ce que sont les Raspberry Pis, comment ils sont construits et à quoi ils servent. De plus, j'espère que cet article démystifie quelque peu ce que signifie vraiment l'IoT.

En essence, l'IoT est un mouvement pour connecter des millions de petites choses en utilisant Internet, et Raspberry Pi est l'une des façons de alimenter ces petites choses. Je crois vraiment que l'avenir réside dans l'IoT et j'espère que tout le monde essaiera de participer à le rapprocher de nous.

> Ce sont les petites choses qui comptent, des centaines d'entre elles.

> — Cliff Shaw.

_C'est mon premier article sur Medium ! Tout commentaire pour des corrections, des améliorations et des applaudissements est grandement apprécié !_