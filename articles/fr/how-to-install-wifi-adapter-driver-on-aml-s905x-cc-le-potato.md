---
title: Comment installer un pilote d'adaptateur Wifi sur AML-S905X-CC (Le Potato)
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2022-11-30T17:27:33.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-wifi-adapter-driver-on-aml-s905x-cc-le-potato
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/How-to-install-driver-for-external-wifi-adapter-in-Le-Potato-3.png
tags:
- name: Raspberry Pi
  slug: raspberry-pi
- name: wifi
  slug: wifi
seo_title: Comment installer un pilote d'adaptateur Wifi sur AML-S905X-CC (Le Potato)
seo_desc: "If you're a developer, you might be familiar with Raspberry Pi. But you\
  \ might not know about the Libre Computer AML-S905X-CC – also called Le Potato.\
  \ \nThere was a chip shortage during the pandemic that has resulted in increased\
  \ Raspberry Pi prices. O..."
---

Si vous êtes un développeur, vous êtes probablement familier avec Raspberry Pi. Mais vous ne connaissez peut-être pas le Libre Computer AML-S905X-CC – également appelé Le Potato. 

Il y a eu une pénurie de puces pendant la pandémie qui a entraîné une augmentation des prix des Raspberry Pi. D'autres événements mondiaux ont également fait flamber les prix des Raspberry Pi, et la fabrication de quelques modèles a même été arrêtée. Vous pouvez en lire plus à ce sujet [ici](https://www.raspberrypi.com/news/supply-chain-shortages-and-our-first-ever-price-increase/). 

À cause de cela, j'ai pensé que passer à une alternative à Raspberry Pi serait une bonne option pour un projet sur lequel je voulais travailler.

Le Potato est similaire à Raspberry Pi en termes d'apparence, de configuration, et ainsi de suite. Il a également la capacité de faire tourner de nombreux systèmes d'exploitation tels qu'Ubuntu, Debian, Raspbian, Android, et autres. 

Mais malheureusement, il ne vient pas avec un module wifi préinstallé, alors que le Raspberry Pi a le module wifi préinstallé. 

Dans cet article, je vais vous donner des instructions claires étape par étape pour installer un pilote d'adaptateur wifi externe dans Le Potato fonctionnant sous **Ubuntu OS**. Pour ceux qui utilisent d'autres systèmes d'exploitation, vous pouvez essayer les étapes suivantes, mais je ne peux pas vous assurer que cela fonctionnera définitivement. 

Jetons un coup d'œil rapide à mes accessoires. 

##### Voici mon appareil Le Potato :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Le-Potato.jpeg)
_Appareil Le Potato_

##### Et voici mon adaptateur Wifi externe Zebronics :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Wifi-Device-1.jpeg)
_Adaptateur Wifi externe Zebronics_

## Essais et erreurs – Ce qui n'a pas fonctionné

Avant de trouver ma solution finale et de finir par installer le pilote wifi et de pouvoir accéder à Internet avec mon adaptateur wifi, j'ai essayé de nombreuses approches. Mais aucune d'entre elles n'a fonctionné. 

Voici ce que j'ai essayé en cours de route :

1. J'ai essayé d'installer le pilote fourni sur le CD qui était livré avec l'adaptateur wifi. Mais je n'ai pas compris les étapes qu'ils m'ont demandé de suivre et j'ai finalement obtenu beaucoup d'erreurs.
2. J'ai téléchargé le pilote exact pour cet appareil depuis le site officiel de Zebronics. Là encore, cela n'a pas bien payé.
3. J'ai essayé d'installer certains pilotes open source depuis GitHub, fourchus par de nombreuses personnes à partir de la source Realtek. Cela n'a pas non plus fonctionné comme prévu.

Finalement, j'ai trouvé une réponse sur le [forum Q&A d'Ubuntu](https://askubuntu.com/questions/1415466/wireless-usb-apapter-not-show-any-available-networks) et j'ai pu l'installer du premier coup. Bien que les étapes n'étaient pas très claires au début, j'ai réussi à les comprendre. Je vais donc expliquer comment faire ici. 

## Comment installer le pilote de l'adaptateur Wifi pour Le Potato sous Ubuntu

Suivez les étapes ci-dessous pour installer le pilote sur votre appareil :

### Installer les dépendances

La première étape consiste à installer le logiciel requis. 

Vous devez installer `git`, `dkms`, `build-essential` et `linux-headers` pour votre architecture système. 

Vous pouvez tous les installer ensemble dans une seule commande :

```bash
sudo apt-get install -y build-essential git dkms linux-headers-$(uname -r)
```

Si vous avez été invité (oui/non) lors de l'exécution de la commande ci-dessus, appuyez simplement sur `y` (ce qui revient à accepter l'installation du logiciel dans votre système). 

### Télécharger la source du pilote

Les pilotes pour certains appareils ne seront pas disponibles dans des formats installables/exécutables. Dans de tels cas, vous devez télécharger, compiler et installer le code source directement sur la machine. Malheureusement, ce pilote entre également dans cette catégorie. 

Nous pouvons télécharger la source de ce pilote depuis GitHub. Exécutez la commande suivante dans votre terminal pour télécharger le code source :

```bash
git clone https://github.com/kelebek333/rtl8188fu
```

### Construire et installer le pilote

Avant de construire et d'installer le pilote, vous devez connaître la commande `dkms` sous Linux. Si vous connaissez `dkms`, vous pouvez sauter ce paragraphe et passer au suivant. 

DKMS signifie Dynamic Kernel Module Support. C'est un programme/cadre qui vous permet d'installer des versions supplémentaires de modules du noyau. Un package peut être compilé et installé dans l'arborescence du noyau. DKMS est appelé automatiquement lors de l'installation de nouveaux packages d'images du noyau Ubuntu, et ainsi les modules ajoutés à DKMS seront automatiquement portés à travers les mises à jour. 

C'est le package source que nous avons téléchargé à l'étape précédente. Nous devons ajouter, compiler et installer le package source dans notre arborescence du noyau. 

Exécutez les commandes suivantes séquentiellement pour ajouter, compiler et installer le package du pilote :

#### Ajouter la source au noyau

```bash
sudo dkms add ./rtl8188fu
```

#### Compiler le package source

```bash
sudo dkms build rtl8188fu/1.0
```

#### Installer le package dans l'arborescence du noyau

```bash
sudo dkms install rtl8188fu/1.0
```

#### Copier le firmware

Le fichier binaire du firmware compilé doit ensuite être copié dans l'emplacement du firmware par défaut sous Linux, c'est-à-dire `/lib/firmware`. 

Le **Firmware** est un logiciel qui permet la communication entre le matériel et le logiciel. Il donne à la machine des instructions qui font fonctionner le matériel. 

Exécutez la commande suivante pour copier le firmware compilé :

```bash
sudo cp ./rtl8188fu/firmware/rtl8188fufw.bin /lib/firmware/rtlwifi/
```

### Désactiver les modes d'économie d'énergie et de suspension automatique sur le noyau

Il est toujours bon de désactiver les modes d'économie d'énergie et de suspension automatique pour les pilotes wifi. Vous devrez donc ajouter cette option par défaut lors de la mise à jour du noyau. Vous pouvez ajouter cette configuration dans le fichier `.conf` dans le répertoire `/etc/modprobe.d/`. 

Nous créons ce fichier conf dans le répertoire `/etc/modprobe.d` car nous devons charger ce module personnalisé avec les modifications persistantes. 

Vous utilisez le drapeau `rtw_power_mgnt` pour contrôler le mode d'économie d'énergie :

* 0 - Désactive l'économie d'énergie
* 1 - Économie d'énergie activée avec minPS
* 2 - Économie d'énergie activée avec maxPS

Vous utilisez le drapeau `rtw_enusbss` pour contrôler le mode de suspension automatique :

* 0 - Désactive la suspension automatique
* 1 - Active la suspension automatique

Exécutez les commandes suivantes pour créer un fichier `.conf` et stocker les options :

```bash
sudo mkdir -p /etc/modprobe.d/
sudo touch /etc/modprobe.d/rtl8188fu.conf
echo "options rtl8188fu rtw_power_mgnt=0 rtw_enusbss=0" | sudo tee /etc/modprobe.d/rtl8188fu.conf
```

### Blacklister le module existant

Vous devez blacklister le module que vous avez essayé d'installer auparavant. 

**Note :** Blacklister un module ne permettra pas son chargement automatique, mais le module peut être chargé si un autre module non blacklisté en dépend ou s'il est chargé manuellement. 

Supposons que vous avez ajouté un module nommé `rtl8188au`. Vous devez alors le blacklister en ajoutant la ligne suivante à la fin du fichier `/etc/modprobe.d/blacklist.conf`. 

```bash
blacklist rtl8188au
```

Si vous n'avez pas ajouté de tel module, vous pouvez ignorer la partie blacklist. 

### Recharger le module

Vous devez recharger le module pour qu'il commence à fonctionner. 

Voici la commande pour recharger le module que nous avons ajouté :

```bash
sudo modprobe -rv rtl8188fu && sudo modprobe -v rtl8188fu
```

Et c'est tout ! Vous devriez pouvoir voir le wifi activé sur votre Le Potato fonctionnant sous Ubuntu OS. Si vous ne le voyez pas, redémarrez votre système et tout devrait être en ordre.  

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-98.png)
_Essai de connexion à un réseau après l'installation du pilote_

![Image](https://www.freecodecamp.org/news/content/images/2022/11/image-97.png)
_Connecté à mon réseau wifi_

## Conclusion

Dans cet article, nous avons passé en revue les étapes pour installer le pilote de notre adaptateur wifi externe. 

Ce sont les étapes exactes (basiques) que vous devez suivre pour ajouter un module externe à votre noyau. 

Abonnez-vous à ma [newsletter](https://5minslearn.gogosoon.com/) pour recevoir plus d'articles aussi instructifs, livrés directement dans votre boîte de réception.