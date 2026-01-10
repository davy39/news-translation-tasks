---
title: Comment utiliser Python pour construire votre propre contrôleur CNC et imprimante
  3D
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-05T15:06:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-3-d-printer-using-cnc-controller-in-python-bd3cd5e28516
coverImage: https://cdn-media-1.freecodecamp.org/images/1*H-6cuBQ6gIL2dyhpocFWRQ.jpeg
tags:
- name: Internet of Things
  slug: internet-of-things
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment utiliser Python pour construire votre propre contrôleur CNC et
  imprimante 3D
seo_desc: 'By Nikolay Khabarov

  This article discusses the process I used to build the first ever CNC machine controller
  implementation on pure Python.

  Computer numerical control (CNC) machine controllers are typically implemented using
  the C or C++ programming ...'
---

Par Nikolay Khabarov

Cet article traite du processus que j'ai utilisé pour construire la première implémentation de contrôleur de machine CNC en Python pur.

Les contrôleurs de machines à commande numérique (CNC) sont généralement implémentés en utilisant les langages de programmation C ou C++. Ils fonctionnent sur des systèmes d'exploitation sans OS ou en temps réel avec des microcontrôleurs simples.

Dans cet article, je vais décrire comment construire un contrôleur CNC — une imprimante 3D en particulier — en utilisant des cartes ARM modernes (Raspberry Pi) avec un langage de haut niveau moderne (Python).

Une telle approche moderne ouvre une large gamme d'options d'intégration avec d'autres technologies, solutions et infrastructures de pointe. Cela rend le projet entier convivial pour les développeurs.

### À propos du projet

Les cartes ARM modernes utilisent généralement Linux comme système d'exploitation de référence. Cela nous donne accès à toute l'infrastructure Linux avec tous les paquets logiciels Linux. Nous pouvons héberger un serveur web sur une carte, utiliser la connectivité Bluetooth, utiliser [OpenCV](http://opencv.org/) pour la reconnaissance d'images, et construire un cluster de cartes, entre autres.

Ce sont des tâches bien connues qui peuvent être implémentées sur des cartes ARM, et elles peuvent être vraiment utiles pour des machines CNC personnalisées. Par exemple, le positionnement automatique utilisant la compuvision peut être très pratique pour certaines machines.

Linux n'est pas un système d'exploitation en temps réel. Cela signifie que nous ne pouvons pas générer des impulsions avec les temporisations requises pour contrôler directement les moteurs pas à pas à partir des broches de la carte avec un logiciel en cours d'exécution, même en tant que module noyau. Alors, comment pouvons-nous utiliser les moteurs pas à pas et les fonctionnalités de haut niveau de Linux ? Nous pouvons utiliser deux puces — un microcontrôleur avec une implémentation classique de CNC, et une carte ARM connectée à ce microcontrôleur via UART (récepteur-transmetteur asynchrone universel).

Et si aucune fonctionnalité de firmware appropriée n'existe pour ce microcontrôleur ? Et si nous devons contrôler des axes supplémentaires qui ne sont pas implémentés dans le microcontrôleur ? Toute modification du firmware C/C++ existant nécessitera beaucoup de temps et d'efforts de développement. Voyons si nous pouvons simplifier cela et même économiser de l'argent sur les microcontrôleurs en les supprimant simplement.

### PyCNC

[PyCNC](https://github.com/Nikolay-Kha/PyCNC) est un interpréteur G-code et contrôleur CNC/imprimante 3D open-source et haute performance. Il peut fonctionner sur diverses cartes basées sur ARM et alimentées par Linux, telles que Raspberry Pi, Odroid, Beaglebone, et autres. Cela vous donne la flexibilité de choisir n'importe quelle carte et d'utiliser tout ce que Linux offre. Et vous pouvez garder l'ensemble de l'environnement G-code sur une seule carte sans avoir besoin d'un microcontrôleur séparé pour les opérations en temps réel.

Choisir Python comme langage de programmation principal réduit considérablement la base de code par rapport aux projets C/C++. Cela réduit également le code spécifique aux microcontrôleurs et le code boilerplate, et rend le projet accessible à un public plus large.

### Comment cela fonctionne

Le projet utilise le DMA (Direct Memory Access) sur le module matériel de la puce. Il copie simplement le tampon des états GPIO (General Purpose Input Output) alloué en RAM vers les registres GPIO réels. Ce processus de copie est synchronisé par l'horloge système et fonctionne complètement indépendamment des cœurs CPU. Ainsi, une séquence d'impulsions pour l'axe du moteur pas à pas est générée en mémoire et ensuite le DMA les envoie précisément.

Approfondissons le code pour comprendre les bases et comment accéder aux modules matériels depuis Python.

### GPIO

Un module General Purpose Input Output contrôle les états des broches. Chaque broche peut avoir un état bas ou haut. Lorsque nous programmons le micro-contrôleur, nous utilisons généralement des variables définies par le SDK (kit de développement logiciel) pour écrire sur cette broche. Par exemple, pour activer un état haut pour les broches 1 et 3 :

```
PORTA = (1 << PIN1) | (1 << PIN3)
```

Si vous regardez dans le SDK, vous trouverez la déclaration de cette variable, et elle ressemblera à :

```
#define PORTA (*(volatile uint8_t *)(0x12345678))
```

Ce n'est qu'un pointeur. Il ne pointe pas vers l'emplacement en RAM, mais vers l'adresse du processeur physique. Le module GPIO réel est situé à cette adresse.

Pour gérer les broches, nous pouvons écrire et lire des données. Le processeur ARM de Raspberry Pi n'est pas une exception, et il a le même module. Pour contrôler les broches, nous pouvons écrire/lire des données. Nous pouvons trouver les adresses et les structures de données dans la [documentation officielle](https://www.raspberrypi.org/app/uploads/2012/02/BCM2835-ARM-Peripherals.pdf) pour les périphériques du processeur.

Lorsque nous exécutons un processus dans l'environnement utilisateur, le processus démarre dans l'espace d'adressage virtuel. Le périphérique réel est accessible directement. Mais nous pouvons toujours accéder aux adresses physiques réelles avec le périphérique `'/dev/mem'`.

Voici un simple code en Python qui contrôle l'état d'une broche en utilisant cette approche :

Décomposons-le ligne par ligne :

**Lignes 1–6** : en-têtes, imports.

**Ligne 7** : ouvre l'accès au périphérique `'/dev/mem'` à l'adresse physique.

**Ligne 8** : nous utilisons l'appel système [mmap](http://man7.org/linux/man-pages/man2/mmap.2.html) pour mapper un fichier (bien que dans notre cas, ce fichier représente la mémoire physique) dans la mémoire virtuelle du processus. Nous spécifions la longueur et le décalage de la zone de mappage. Pour la longueur, nous prenons la taille de la page. Et le décalage est `0x3F200000`.

La documentation indique que l'adresse de **bus** `0x7E200000` contient les registres GPIO, et nous devons spécifier l'adresse **physique**. La documentation indique (page 6, paragraphe 1.2.3) que l'adresse de bus `0x7E000000` est mappée à l'adresse physique `0x20000000`, mais cette documentation est pour Raspberry 1. 
   
Veuillez noter que toutes les adresses de bus des modules sont les mêmes pour Raspberry Pi 1–3, mais ce mappage a été changé en `0x3F000000` pour RPi 2 et 3. Donc, l'adresse ici est `0x3F200000`. Pour Raspberry Pi 1, changez-la en `0x20200000`.

Après cela, nous pouvons écrire dans la mémoire virtuelle de notre processus, mais cela écrit en réalité dans le module GPIO.

**Ligne 9** : ferme le descripteur de fichier, puisque nous n'avons pas besoin de le stocker.

**Lignes 11–14** : nous lisons et écrivons dans notre mappage avec le décalage `0x08`. Selon la documentation, il s'agit du registre GPFSEL2 GPIO Function Select 2. Et ce registre contrôle les fonctions des broches.

Nous définissons (effaçons tout, puis définissons avec l'opérateur OR) 3 bits avec le 3ème bit défini à `001`. Cette valeur signifie que la broche fonctionne comme une sortie. Il y a beaucoup de broches et de modes possibles pour elles. C'est pourquoi le registre des modes est divisé en plusieurs registres, où chacun contient les modes pour 10 broches.

**Lignes 16 et 22** : configurent le gestionnaire d'interruption 'Ctrl+C'.

**Ligne 17** : boucle infinie.

**Ligne 18** : définit la broche à l'état **haut** en écrivant dans le registre GPSET0.

Veuillez noter que Raspberry Pi n'a pas de registres comme PORTA (microcontrôleurs AVR). Nous ne pouvons pas écrire l'état GPIO complet de toutes les broches. Il y a simplement des registres **set** et **clear** qui sont utilisés pour définir et effacer les broches spécifiées avec un masque binaire.

**Lignes 19 et 21** : délai

**Ligne 20** : définit la broche à l'état bas avec le registre GPCLR0.

**Lignes 25 et 26** : basculent la broche à l'état par défaut, l'état d'entrée. Fermet la carte mémoire.

Ce code doit être exécuté avec des privilèges superutilisateur. Nommez le fichier `'gpio.py'` et exécutez-le avec `'sudo python gpio.py'`. Si vous avez une LED connectée à la broche 21, elle clignotera.

### DMA

L'accès direct à la mémoire est un module spécial conçu pour copier des blocs de mémoire d'une zone à une autre. Nous allons copier des données du tampon mémoire vers le module GPIO. Tout d'abord, nous avons besoin d'une zone solide en RAM physique qui sera copiée.

Il existe quelques solutions possibles :

1. Nous pouvons créer un simple pilote de noyau qui allouera, verrouillera et nous rapportera l'adresse de cette mémoire.
2. Dans certaines implémentations, la mémoire virtuelle est allouée et utilise `'/proc/self/pagemap'` pour convertir l'adresse en adresse physique. Je ne recommanderais pas cette approche, surtout lorsque nous devons allouer une grande zone. Toute mémoire allouée virtuellement (même verrouillée, voir la [documentation du noyau](https://www.kernel.org/doc/Documentation/vm/unevictable-lru.txt)) peut être déplacée vers la zone physique.
3. Tous les Raspberry Pi ont un périphérique `'/dev/vcio'`, qui fait partie du pilote graphique et peut allouer de la mémoire physique pour nous. Un [exemple officiel](https://github.com/raspberrypi/userland/blob/master/host_applications/linux/apps/hello_pi/hello_fft/mailbox.c) montre comment le faire. Et nous pouvons l'utiliser au lieu de créer le nôtre.

Le module DMA lui-même est simplement un ensemble de registres situés quelque part à une adresse physique. Nous pouvons contrôler ce module via ces registres. En fait, il y a des registres source, destination et de contrôle. Vérifions un simple code qui montre comment utiliser les modules DMA pour gérer le GPIO.

Puisque du code supplémentaire est nécessaire pour allouer de la mémoire physique avec `'/dev/vcio'`, nous utiliserons un [fichier](https://github.com/Nikolay-Kha/PyCNC/blob/master/cnc/hal_raspberry/rpgpio_private.py) avec une implémentation existante de la classe PhysicalMemory CMA. Nous utiliserons également la classe PhysicalMemory, qui effectue l'astuce avec memap de l'exemple précédent.

Décomposons-le ligne par ligne :

**Lignes 1–3** : en-têtes, imports.

**Lignes 5–6** : constantes avec le numéro de canal DMA et la broche GPIO que nous utiliserons.

**Lignes 8–15** : initialisent la broche GPIO spécifiée comme sortie, et l'allument pendant une demi-seconde pour le contrôle visuel. En fait, c'est la même chose que nous avons faite dans l'exemple précédent, écrit de manière plus pythonique.

**Ligne 17** : alloue `64` octets en mémoire physique.

**Ligne 18** : crée des structures spéciales — blocs de contrôle pour le module DMA. Les lignes suivantes décomposent la structure de ce bloc. Chaque champ a une longueur de `32` bits.

**Ligne 19** : drapeaux d'information de transfert. Vous pouvez trouver une description complète de chaque drapeau à la page 50 de la documentation officielle.

**Ligne 20** : adresse source. Cette adresse doit être une adresse de bus, donc nous appelons `_get_bus_address()_`. Le bloc de contrôle DMA doit être aligné sur 32 octets, mais la taille de **ce bloc** est de `24` octets. Nous avons donc 8 octets, que nous utilisons comme stockage.

**Ligne 21** : adresse de destination. Dans notre cas, il s'agit de l'adresse du registre SET du module GPIO.

**Ligne 22** : longueur de transmission — `4` octets.

**Ligne 23** : stride. Nous n'utilisons pas cette fonctionnalité, définissons `0`.

**Ligne 24** : adresse du prochain bloc de contrôle, dans notre cas, les 32 prochains octets.

**Ligne 25** : padding. Mais puisque nous avons utilisé cette adresse comme source de données, mettons un bit, qui devrait déclencher le GPIO.

**Ligne 26** : padding.

**Lignes 28–37** : remplissent le deuxième bloc de contrôle DMA. La différence est que nous écrivons dans le registre CLEAR GPIO et définissons notre premier bloc comme prochain bloc de contrôle pour boucler la transmission.

**Lignes 38–39** : écrivent les blocs de contrôle en mémoire physique.

**Ligne 41** : obtient l'objet du module DMA avec le canal sélectionné.

**Lignes 42–43** : réinitialise le module DMA.

**Ligne 44** : spécifie l'adresse du premier bloc.

**Ligne 45** : exécute le module DMA.

**Lignes 49–52** : nettoyage. Arrête le module DMA et bascule la broche GPIO à l'état par défaut.

Connectons l'oscilloscope à la broche spécifiée et exécutons cette application (n'oubliez pas les privilèges sudo). Nous observerons des impulsions carrées d'environ 1,5 MHz :

![Image](https://cdn-media-1.freecodecamp.org/images/ZxBtfiQNWX7SffPshqWST0ZhvMx82iqjCUia)

### Défis du DMA

Il y a plusieurs choses que vous devez prendre en considération avant de construire une vraie machine CNC.

Premièrement, la taille du tampon DMA peut être de centaines de mégaoctets.

Deuxièmement, le module DMA est conçu pour une copie rapide de données. Si plusieurs canaux DMA fonctionnent, nous pouvons dépasser la bande passante mémoire, et le tampon sera copié avec des retards qui peuvent causer des jitters dans les impulsions de sortie. Il est donc préférable d'avoir un mécanisme de synchronisation.

Pour surmonter cela, j'ai créé un design spécial pour les blocs de contrôle :

![Image](https://cdn-media-1.freecodecamp.org/images/E5J6HMgMMLODKP13TjtWXyZ9Vv7zl54llWur)

L'oscillogramme en haut de l'image montre les états GPIO souhaités. Les blocs en dessous représentent les blocs de contrôle DMA qui génèrent cette forme d'onde. « Delay 1 » spécifie la longueur de l'impulsion, et « Delay 2 » est la longueur de la pause entre les impulsions. Avec cette approche, la taille du tampon dépend uniquement du nombre d'impulsions.

Par exemple, pour une machine avec une longueur de déplacement de 200 mm et 400 impulsions par mm, chaque impulsion prendrait 128 octets (4 blocs de contrôle par 32 octets), et la taille totale serait d'environ 9,8 Mo. Nous aurions plus d'un axe, mais la plupart des impulsions se produiraient en même temps. Et ce serait des dizaines de mégaoctets, pas des centaines.

J'ai résolu le deuxième défi, lié à la synchronisation, en introduisant des retards temporaires via les blocs de contrôle. Le module DMA a une fonctionnalité spéciale : il peut attendre un signal de prêt spécial du module où il écrit les données. Le module le plus adapté pour nous est le module PWM (modulation de largeur d'impulsion), qui nous aidera également avec la synchronisation.

Le module PWM peut sérialiser les données et les envoyer à une vitesse fixe. Dans ce mode, il génère un signal de prêt pour le tampon FIFO (premier entré, premier sorti) du module PWM. Donc, écrivons des données dans le module PWM et utilisons-le uniquement pour la synchronisation.

En fait, nous devrions activer un drapeau spécial dans le mappage perceptuel du drapeau d'information de transfert, puis exécuter le module PWM avec la fréquence souhaitée. L'implémentation est assez longue — vous pouvez [l'étudier](https://github.com/Nikolay-Kha/PyCNC/blob/master/cnc/hal_raspberry/rpgpio.py) vous-même.

Au lieu de cela, créons un simple code qui peut utiliser le module existant pour générer des impulsions précises.

```
import rpgpio
```

```
PIN=21PINMASK = 1 << PINPULSE_LENGTH_US = 1000PULSE_DELAY_US = 1000DELAY_US = 2000 g = rpgpio.GPIO()g.init(PIN, rpgpio.GPIO.MODE_OUTPUT) dma = rpgpio.DMAGPIO()for i in range(1, 6): for i in range(0, i): dma.add_pulse(PINMASK, PULSE_LENGTH_US) dma.add_delay(PULSE_DELAY_US) dma.add_delay(DELAY_US)dma.run(True) raw_input("Press Enter to stop")dma.stop()g.init(PIN, rpgpio.GPIO.MODE_INPUT_NOPULL)
```

Le code est assez simple, et il n'est pas nécessaire de le décomposer. Si vous exécutez ce code et connectez un oscilloscope, vous verrez :

![Image](https://cdn-media-1.freecodecamp.org/images/zPJ37jLULml7544lV8qBJK3bGY-U-Zb42TlM)

Et maintenant nous pouvons créer un vrai interpréteur de G-code et contrôler les moteurs pas à pas. Mais attendez ! C'est déjà implémenté [ici](https://github.com/Nikolay-Kha/PyCNC). Vous pouvez utiliser ce projet, car il est distribué sous la licence MIT.

### Matériel

Le projet Python peut être adopté pour vos besoins. Mais pour vous inspirer, je vais décrire l'implémentation matérielle originale de ce projet — une imprimante 3D. Elle contient essentiellement les composants suivants :

1. Raspberry Pi 3
2. [Carte RAMPSv1.4](http://reprap.org/wiki/RAMPS_1.4)
3. 4 modules A4988 ou DRV8825
4. Cadre RepRap Prusa i3 avec équipement (butées de fin de course, moteurs, chauffages et capteurs)
5. Alimentation 12V 15A
6. Module convertisseur abaisseur LM2596S DC-DC
7. Puce MAX4420
8. Module convertisseur analogique-numérique ADS1115
9. Câble ruban IDE UDMA133
10. Verre acrylique
11. Supports de PCB
12. Ensemble de connecteurs avec un pas de 2,54 mm

Le câble ruban IDE à 40 broches est adapté pour le connecteur à 40 broches du Raspberry Pi, mais l'extrémité opposée nécessite un peu de travail. Coupez le connecteur existant de l'extrémité opposée et sertissez des connecteurs sur les fils du câble.

La carte RAMPSv1.4 a été initialement conçue pour la connexion au connecteur [Arduino](https://www.arduino.cc/en/Main/arduinoBoardMega) Mega, donc il n'y a pas de moyen facile de connecter cette carte au Raspberry Pi. La méthode suivante vous permet de simplifier la connexion des cartes. Vous devrez connecter moins de 40 fils.

![Image](https://cdn-media-1.freecodecamp.org/images/EN-JNl9sm5cJ68bdtcKITvmDRyc9RM6p0h79)
_Connexion de référence PyCNC_

J'espère que ce schéma de connexion est assez simple et facilement dupliqué. Il est préférable de connecter certaines broches (2ème extrudeur, servos) pour une utilisation future, même si elles ne sont pas actuellement nécessaires.

Vous vous demandez peut-être — pourquoi avons-nous besoin de la puce MAX4420 ? Les broches du Raspberry Pi fournissent 3,3V pour les sorties GPIO, et les broches peuvent fournir un courant très faible. Ce n'est pas suffisant pour commuter la grille du MOSFET (transistor à effet de champ à semi-conducteur à oxyde métallique). De plus, l'un des MOSFET fonctionne sous une charge de 10A d'un chauffage de lit. En conséquence, avec une connexion directe à un Raspberry Pi, ce transistor surchaufferait. Par conséquent, il est préférable de connecter un pilote de MOSFET spécial entre le MOSFET fortement chargé et le Raspberry Pi. Il peut commuter le MOSFET de manière efficace et réduire son échauffement.

L'ADS1115 est un convertisseur analogique-numérique (ADC). Puisque le Raspberry Pi n'a pas de module ADC intégré, j'ai utilisé un module externe pour mesurer la température à partir des thermistances de 100k Ohm. Le module RAMPSv1.4 a déjà un diviseur de tension pour les thermistances. Le convertisseur abaisseur LM2596S doit être ajusté à une sortie de 5V, et il est utilisé pour alimenter la carte Raspberry Pi elle-même.

Maintenant, il peut être monté sur le cadre de l'imprimante 3D et la carte RAMPSv1.4 doit être connectée au cadre équipé.

![Image](https://cdn-media-1.freecodecamp.org/images/Wa2vq72NhEoEqS2hxcPkXSyk7yv5lz2G2EN5)

C'est tout. L'imprimante 3D est assemblée, et vous pouvez copier le code source sur le Raspberry Pi et l'exécuter. `sudo ./pycnc` l'exécutera dans un shell G-Code interactif. `sudo ./pycnc filename.gcode` exécutera un fichier G Code. Vérifiez la [configuration prête](https://github.com/Nikolay-Kha/PyCNC/blob/master/extra/sample-Slic3r-config.ini) pour [Slic3r](http://slic3r.org/).

Et dans [cette vidéo](https://www.youtube.com/watch?v=41wdmmztTNA), vous pouvez voir comment cela fonctionne réellement.

Si vous avez trouvé cet article utile, veuillez m'applaudir pour que plus de gens le voient. Merci !

![Image](https://cdn-media-1.freecodecamp.org/images/AzJ9Gt6Nl3OfLXNoiI1Oxp45I8EU0Hxdsbr-)

_L'IoT est tout sur le prototypage rapide des idées. Pour le rendre possible, nous avons développé [DeviceHive](https://devicehive.com/?utm_source=medium&utm_medium=social&utm_campaign=d-spring-2018), une plateforme IoT/M2M open source. DeviceHive fournit une base solide et des blocs de construction pour créer toute solution IoT/M2M, comblant le fossé entre le développement embarqué, les plateformes cloud, le big data et les applications client._

![Image](https://cdn-media-1.freecodecamp.org/images/UA7ESnWpENlYCxEvgEiV3ENq60vytsMCzgzF)