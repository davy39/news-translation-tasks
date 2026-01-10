---
title: Comment pirater une voiture — un cours accéléré
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-21T17:40:44.000Z'
originalURL: https://freecodecamp.org/news/hacking-cars-a-guide-tutorial-on-how-to-hack-a-car-5eafcfbbb7ec
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LVuumyKElZ0zrQRQgjjSpw.jpeg
tags:
- name: cars
  slug: cars
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment pirater une voiture — un cours accéléré
seo_desc: 'By Kenny Kuchera

  The goal of this article is to get you started hacking cars — fast, cheap, and easy.
  In order to do this, we’ll spoof the RPM gauge as an example.

  The following is by no means an exhaustive tutorial. It instead aims to provide
  just e...'
---

Par Kenny Kuchera

Le but de cet article est de vous initier au piratage de voitures — rapidement, à moindre coût et facilement. Pour ce faire, nous allons usurper le compteur de régime comme exemple.

Ce qui suit n'est en aucun cas un tutoriel exhaustif. Il vise plutôt à fournir juste assez d'informations pour vous mettre en route. Si vous souhaitez approfondir, vous pouvez consulter les lectures incontournables à la fin.

Si vous décidez de réaliser ce tutoriel dans la vie réelle, vous aurez besoin d'un ordinateur Linux (ou d'une machine virtuelle Linux), et d'un dispositif CAN vers USB (que nous examinerons plus tard).

### Une voiture est un réseau

Une voiture est composée de plusieurs ordinateurs pour contrôler le moteur, la transmission, les fenêtres, les serrures, les lumières, etc. Ces ordinateurs sont appelés [unités de contrôle électronique](https://en.wikipedia.org/wiki/Electronic_control_unit) (ECU) et communiquent entre eux via un réseau.

Par exemple, lorsque vous appuyez sur le bouton de votre volant pour augmenter le volume de la radio, l'ECU du volant envoie une commande pour augmenter le volume sur le réseau, l'ECU de la radio voit ensuite cette commande et agit en conséquence.

Il existe plusieurs réseaux dans une voiture, généralement au moins deux :

* Un pour les données critiques telles que les messages du moteur et de la transmission
* Et un pour les données moins critiques telles que la radio et les serrures de porte

Le réseau critique utilise un protocole rapide et fiable tandis que le réseau non critique utilise un protocole plus lent, moins fiable mais moins cher. Le nombre de réseaux ainsi que les ECU qui sont connectés ensemble dépendent de la marque, du modèle et de l'année de la voiture. Un ECU pourrait également être connecté à plusieurs réseaux.

### Connexion à un réseau

Certains réseaux peuvent être accessibles via le port OBD-II. [OBD-II](https://en.wikipedia.org/wiki/On-board_diagnostics) est obligatoire sur toutes les voitures et camions légers construits aux États-Unis après 1996 et en Europe après 2004.

Le connecteur est à portée de main du siège du conducteur. Vous devrez peut-être enlever un couvercle en plastique, mais il est toujours accessible sans outils.

![Image](https://cdn-media-1.freecodecamp.org/images/es1vbS1QkS9VxyYYGFdmMFLLK8s-m2nW4nm5)
_Connecteur OBD-II._

La norme OBD-II permet [cinq](https://en.wikipedia.org/wiki/On-board_diagnostics#OBD-II_signal_protocols) protocoles de signalisation. C'est au fabricant de décider lequel utiliser. [CAN](https://en.wikipedia.org/wiki/CAN_bus) est le plus populaire et c'est celui dont nous allons discuter. Il est accessible via les broches 6 et 14 du connecteur OBD-II. Si votre voiture dispose d'un bus CAN, vous verrez des conducteurs métalliques sur les broches comme dans l'image ci-dessus.

Le bus CAN est un bus fiable et haute vitesse utilisé pour envoyer des données critiques. Malheureusement, les paquets de données sur le bus ne sont pas standardisés, vous devrez donc les inverser pour savoir ce qu'ils signifient. La norme OBD-II laisse également de la place pour des broches spécifiques au fabricant qui peuvent être utilisées pour des protocoles spécifiques au fabricant. Cela facilite le diagnostic des problèmes par le concessionnaire.

Sur ma voiture (GM), j'ai un bus CAN standard sur les broches 6 et 14, et un bus CAN à fil unique spécifique au fabricant sur la broche 1. Le bus CAN standard est un protocole fiable et haute vitesse (500 kbps) également appelé CAN haute vitesse (HS-CAN). Il est utilisé pour les données critiques. Le bus CAN à fil unique (SW-CAN) ou GMLAN est plus lent (33,3 kbps) et moins fiable mais moins cher car il n'utilise qu'un seul fil. Ce bus est utilisé pour les données non critiques.

Si vous voyez une broche spécifique au fabricant et ne savez pas quel protocole est utilisé, recherchez sur Google « <marque> OBD pinout ». Il existe également le CAN basse vitesse (LS-CAN) et le CAN moyenne vitesse (MS-CAN). Le MS-CAN est généralement sur les broches 3 et 11, fonctionnant à 125 kbps sur les voitures Ford et Volvo.

### Outils

Vous aurez besoin à la fois d'un dispositif capable d'interpréter les données CAN ainsi que d'un logiciel pour analyser les données.

#### Matériel

Pour recevoir et transmettre des paquets CAN, vous avez besoin d'un dispositif capable de le faire. Vous rencontrerez souvent des dispositifs basés sur ELM327. Bien qu'ils aient leur utilité, ils sont terribles pour le piratage. Ils sont beaucoup trop lents pour surveiller le bus CAN.

Il existe également des dispositifs haut de gamme comme Kvaser, Peak ou EMS Wünsche. Ils feront le travail mais sont surdimensionnés et assez chers.

Certains dispositifs haut de gamme nécessitent également l'achat de logiciels. Le [USB2CAN](http://www.8devices.com/products/usb2can/) est une interface CAN native pour Linux qui offre un excellent rapport qualité-prix.

Vous pourriez également utiliser [Cantact](http://linklayer.github.io/cantact/) ou [CANUSB](http://www.can232.com/?page_id=16). Cependant, ceux-ci ne sont pas des dispositifs CAN natifs sous Linux et utilisent un protocole basé sur ASCII. Cela signifie qu'ils sont légèrement plus compliqués à configurer et ont des performances moindres. En revanche, ils sont bien supportés sur plusieurs systèmes d'exploitation.

J'utilise [CANalyze](https://kkuchera.github.io/canalyze/) que j'ai conçu pour mes besoins. Il est similaire à USB2CAN en ce sens qu'il s'agit d'une interface CAN native abordable, mais il utilise un microcontrôleur plus récent, est open source et peut être construit à l'aide d'outils open source. Le reste de ce tutoriel suppose que vous utilisez une interface CAN native.

#### Logiciel

Pour communiquer avec le dispositif, vous devez installer le paquet can-utils sur votre machine Linux. Vous pouvez le faire en tapant ce qui suit dans l'invite Linux :

```
sudo apt-get install can-utils
```

Can-utils facilite grandement l'envoi, la réception et l'analyse des paquets CAN. Voici les commandes que nous utiliserons.

* **cansniffer** affiche uniquement les paquets qui changent
* **candump** affiche tous les paquets reçus
* **cansend** envoie un paquet

Linux dispose d'un support CAN intégré au noyau via [SocketCAN](https://www.kernel.org/doc/Documentation/networking/can.txt). Cela facilite l'écriture de vos propres programmes supplémentaires. Vous pouvez interagir avec le bus CAN de la même manière que vous interagiriez avec n'importe quel autre réseau, c'est-à-dire via des sockets.

### Bus CAN

Avant de commencer à inverser, vous devez avoir une certaine compréhension du fonctionnement du bus CAN. Il se compose de 2 fils et utilise une signalisation différentielle. Puisqu'il s'agit d'un bus, plusieurs dispositifs peuvent être connectés à ces deux fils. Lorsqu'une trame CAN est envoyée sur le bus, elle est reçue par tous les ECU mais n'est traitée que si elle est utile pour l'ECU. Si plusieurs trames CAN sont envoyées en même temps, celle avec la priorité la plus élevée l'emporte. Une trame CAN a 3 parties qui nous concernent.

* **identifiant d'arbitrage** L'identifiant d'un message. Un ECU l'utilise pour décider de traiter ou d'ignorer la trame reçue. Il représente également la priorité du message. Un nombre plus bas a une priorité plus élevée. Par exemple, si vous étiez un ingénieur concevant le réseau, vous donneriez à la trame pour le déploiement des airbags une priorité très élevée ou un identifiant d'arbitrage bas. D'autre part, vous donneriez une priorité plus basse ou un identifiant d'arbitrage plus élevé aux données destinées aux serrures de porte.
* **code de longueur de données (DLC)** Indique la longueur du champ de données en octets. Une trame CAN peut avoir au plus 8 octets de données.
* **champ de données** Contient jusqu'à 8 octets de données.

### Inverser le bus CAN

L'approche générale pour inverser le bus CAN est de générer le comportement que vous souhaitez imiter et de trouver le message qui provoque ce comportement. Par exemple, supposons que le système d'assistance au maintien de voie (LKAS) de votre voiture est médiocre et que vous avez créé le vôtre.

Pour qu'il contrôle la direction, vous devez savoir quels messages envoyer. La façon de le découvrir est d'activer le LKAS d'origine, de surveiller le bus CAN et d'identifier les paquets responsables de la rotation du volant. Une fois que vous avez identifié ces paquets, votre propre LKAS peut envoyer ces paquets sur le bus CAN pour contrôler le volant.

Dans notre cas, nous voulons usurper le compteur de régime, nous devons donc changer le régime en appuyant sur l'accélérateur avec la voiture allumée et au point mort, puis essayer de trouver le paquet responsable du changement de régime.

#### Installation

Branchez le dispositif CAN dans le port OBD-II de la voiture et le port USB de l'ordinateur. Activez l'interface CAN en exécutant ce qui suit dans votre invite Linux :

```
sudo ip link set can0 up type can bitrate 500000
```

ce qui active l'interface `can0` (toujours `can0` si vous n'avez qu'un seul dispositif connecté) à un débit binaire de 500 kbps, ce qui est standard.

#### Identification

Lorsque la voiture est éteinte, les ECU sont généralement en veille, vous devez donc allumer la voiture ou la mettre en mode accessoire. Vous pouvez regarder les données CAN brutes en exécutant ce qui suit dans votre invite Linux :

```
candump can0
```

Cela imprime les données CAN à l'écran dès qu'elles sont reçues. Cependant, cela est très désorganisé et il est très difficile de voir quels paquets correspondent à un certain événement. Vous pouvez appuyer sur ctrl+c pour arrêter le programme. Pour rendre les données plus lisibles, nous utilisons cansniffer qui regroupe les paquets par identifiant d'arbitrage et n'affiche que les paquets qui changent. Pour le démarrer, exécutez la commande dans votre invite Linux :

```
cansniffer -c can0
```

où `-c` colorise les octets changeants et `can0` est l'interface à surveiller. Il faut quelques secondes pour supprimer les paquets constants.

Vous devriez voir quelque chose de similaire à l'image ci-dessous, bien que les nombres seront probablement complètement différents.

![Image](https://cdn-media-1.freecodecamp.org/images/nEapzF0RhUbqCQs6A08MXiICNUkvbIbebLHp)
_Cansniffer avec le moteur au ralenti._

La première colonne (delta) montre le taux en secondes auquel les paquets avec cet identifiant d'arbitrage sont reçus. La deuxième colonne (ID) contient l'identifiant d'arbitrage. Les colonnes alphanumériques restantes (données ...) contiennent les octets de données. Si les données ont une représentation ASCII, elle peut être vue à droite, sinon c'est un point.

Lorsque vous appuyez sur l'accélérateur avec le moteur en marche pour augmenter le régime, de nouveaux messages CAN peuvent apparaître à l'écran et/ou des messages existants peuvent changer.

Nous devons trouver un message CAN où les octets changeants correspondent au changement de régime. Nous pouvons nous attendre à ce que la valeur augmente/diminue à mesure que le régime augmente/diminue.

La première trame CAN dans cansniffer qui semble varier avec le régime est la trame avec l'identifiant d'arbitrage `C9`. Il y a probablement plusieurs paquets potentiels qui varient avec le régime, c'est juste le premier.

![Image](https://cdn-media-1.freecodecamp.org/images/x--6G22ywelTLjofYtu5cEDmDvtt3XnLmdht)
_Paquet détecté correspondant au régime._

Il y a 4 octets qui changent (colorés en rouge) dans ce message, mais tous ne représentent pas nécessairement le régime. Les variations dans le troisième octet `07` ne semblent pas correspondre à un régime variable. Le dernier octet `1B` le fait.

Cependant, dès que nous relâchons l'accélérateur, il passe à `00`. Cela indiquerait qu'il représente la position de l'accélérateur et non le régime.

Enfin, il y a les deux octets `21 C0` qui semblent correspondre à un changement de régime. De plus, il varie comme un entier 16 bits, c'est-à-dire que lorsque le deuxième octet `C0` déborde, le premier octet `21` est augmenté de un. De plus, il semble que `21` corresponde à environ 2000 tr/min. C'est bon à noter lorsque vous allez rejouer le message.

#### Replay

Une fois que vous avez un candidat, envoyez-le sur le bus CAN avec la commande suivante dans votre invite Linux :

```
cansend can0 0C9#8021C0071B101000
```

où la trame a le format `<arb_id>#`{data} et doit être substituée avec votre propre message CAN.

Votre voiture peut être en marche ou en mode accessoire pour cela. Assurez-vous d'utiliser un paquet que vous avez obtenu lorsque le moteur n'était pas au ralenti, sinon vous ne verrez rien changer lorsque vous le rejouez alors que votre moteur est au ralenti.

Si vous envoyez simplement le paquet une fois, vous ne verrez probablement rien changer sur le tableau de bord. Cela est dû au fait que le message original est toujours envoyé en continu sur le bus à des intervalles de 0,2 seconde par l'ECU, donc votre message sera simplement ignoré.

Rappelez-vous que le taux est donné dans la première colonne de cansniffer. Il existe deux façons de contourner cela, outre la déconnexion de l'ECU qui génère ces messages. Une option consiste à envoyer les paquets à une fréquence beaucoup plus élevée que ceux actuellement envoyés. Vous pouvez le faire en exécutant ce qui suit dans votre invite Linux :

```
while true; do cansend can0 0C9#8021C0071B101000; sleep 0.002; done
```

et en substituant le message CAN par celui que vous avez identifié. Appuyez sur ctrl+c pour arrêter.

Une autre option consiste à surveiller le bus, et chaque fois que vous détectez le paquet que vous souhaitez usurper, envoyez votre propre paquet immédiatement après. Cela peut être fait en exécutant dans votre invite Linux :

```
candump can0 | grep " 0C9 " | while read line; do cansend can0 0C9#8021C0071B101000; done
```

où vous devez substituer le message CAN et `0C9` avec le message CAN que vous avez identifié et son identifiant d'arbitrage respectivement. Vous pouvez expérimenter les deux approches pour voir laquelle fonctionne le mieux.

Si le compteur de régime change, bon travail, vous l'avez trouvé ! Sinon, identifiez le message suivant qui correspond au régime et rejouez-le.

#### Fuzzing

Maintenant que vous avez la trame CAN qui définit le régime sur le tableau de bord, vous pouvez jouer avec les données que vous envoyez pour voir ce qui se passe. Nous avons noté que les deux octets qui correspondent au régime se comportent comme un entier 16 bits, donc pour régler le compteur à 8k tr/min, nous exécutons ce qui suit dans votre invite Linux :

```
while true; do cansend can0 0C9#0080000000101000; sleep 0.002; done
```

et le résultat est...

![Image](https://cdn-media-1.freecodecamp.org/images/cLHGxBiVaL0RmJD0poozz3r6yg6uWovtZ9tL)
_Régime usurpé avec le moteur éteint._

C'est tout ! Vous pouvez maintenant essayer de contrôler le compteur de vitesse, la radio, les lumières, les serrures de porte, etc. en utilisant la même approche.

### Problèmes possibles

* Bien que le bus CAN soit le réseau le plus populaire, ce n'est pas le seul réseau. Si vous ne trouvez pas le message que vous cherchez sur le bus CAN, essayez un autre réseau. Surtout les messages non critiques tels que la radio, les lumières et les serrures de porte seront probablement sur un autre réseau.
* Comme mentionné, les données exactes transmises sur CAN dépendent de la marque, du modèle et de l'année de la voiture. Certaines voitures utilisent un compteur dans le message CAN pour s'assurer que le même message n'est pas traité plusieurs fois. Cela est légèrement plus difficile, mais vous devriez être en mesure de le faire avec les informations fournies. Certaines voitures utilisent également une somme de contrôle pour garantir l'intégrité des données. Calculer cette somme de contrôle peut être difficile. Si vous avez une Toyota, consultez [Adventures in Automotive Networks and Control Units](http://illmatics.com/car_hacking.pdf), p10, Checksum-Toyota. Tout le monde devrait vraiment lire l'ensemble du document.
* Lorsque vous rejouez le paquet identifié sur le bus, votre dispositif CAN vers USB peut passer en état « bus off ». Cela fait partie de la norme CAN et se produit lorsque le dispositif a rencontré trop d'erreurs. Cela se produit généralement lorsqu'il y a beaucoup de trafic sur le bus. Pour contourner cela, vous pouvez jouer avec les délais et le timing, peut-être essayer de rejouer le message immédiatement après avoir mis la voiture en mode accessoire, essayer d'attendre un peu, essayer avec la voiture allumée, etc. Si vous avez identifié les ECU connectés au bus, vous pouvez également retirer leur fusible pour les empêcher d'envoyer des messages et réduire le trafic sur le bus.

### Lectures incontournables

* [Car Hacker's Handbook](http://opengarages.org/handbook/)
* Les [recherches](http://illmatics.com/carhacking.html) de Charlie Miller et Chris Valasek, oui, toutes
* Les [recherches](http://www.autosec.org/publications.html) de l'Université de Californie à San Diego et de l'Université de Washington.

Assurez-vous également de consulter [Open Garages](https://opengarages.org) et leurs [vidéos](https://www.youtube.com/playlist?list=PLBqtCp9s_lnEOtf6I1DDMEANIzJJLXRhe).