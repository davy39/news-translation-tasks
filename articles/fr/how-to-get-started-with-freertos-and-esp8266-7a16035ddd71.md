---
title: Comment commencer avec FreeRTOS et ESP8266
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-03T15:57:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-freertos-and-esp8266-7a16035ddd71
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2fa1eXR1ZEeWUA54bbY3Ag.jpeg
tags:
- name: Electronics
  slug: electronics
- name: ESP8266
  slug: esp8266
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: wifi
  slug: wifi
seo_title: Comment commencer avec FreeRTOS et ESP8266
seo_desc: 'By Denis Nuțiu

  Recently, I purchased a NodeMCU from AliExpress for about $4. The reason I did this
  was to find out what all the fuss is about with ESP8266.

  NodeMCU is an open source IoT platform. It includes firmware which runs on the ESP8266
  Wi-Fi S...'
---

Par Denis Nuțiu

Récemment, j'ai acheté un NodeMCU sur AliExpress pour environ 4 $. La raison pour laquelle j'ai fait cela était de découvrir ce qui fait tant parler de l'ESP8266.

NodeMCU est une plateforme IoT open source. Elle inclut un firmware qui fonctionne sur le SoC Wi-Fi ESP8266 d'Espressif Systems, et du matériel basé sur le module ESP-12.

![Image](https://cdn-media-1.freecodecamp.org/images/WWQgoFxzsaqMPtrLF33j93TOcM5hBstHKqON)
_Source : Fiche technique ESP8266_

Comparé à l'Arduino UNO, mon ESP8266 le surpasse complètement en termes de puissance CPU et de prix.

L'ESP8266 est 500 % plus rapide et 82 % moins cher que l'Arduino. L'ESP8266 dispose également d'une connectivité WiFi.

J'ai été très surpris lorsque j'ai visité le [site web d'Espressif](https://www.espressif.com/en/products/hardware/esp8266ex/overview) pour l'ESP8266. Il y a beaucoup de documentation et de ressources que vous pouvez utiliser. Par exemple, il y a une application Android qui indique à votre ESP8266 de se connecter à votre WiFi. L'application envoie le SSID et le mot de passe sous forme de paquets, l'ESP8266 les interceptent, puis il se connecte à votre WiFi. Cela s'appelle SmartConfig, et a été inventé par Texas Instruments.

Dans cet article, je vais vous guider pour installer et exécuter l'exemple Smart Config du SDK RTOS d'Espressif.

#### Voici ce dont vous aurez besoin :

* Un ordinateur moderne.
* Une carte NodeMCU avec ESP12-E
* VirtualBox ([https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads))
* Ubuntu Server LTS ([https://www.ubuntu.com/download/server](https://www.ubuntu.com/download/server))

### Configurer VirtualBox pour le développement

1. Téléchargez VirtualBox et installez Ubuntu Server. Cela devrait être facile à faire, mais si vous ne savez pas comment, cherchez sur Google ou consultez ce guide graphique [pas à pas](https://dalanzg.github.io/tips-tutorials/ubuntu/2016/04/15/install-ubuntu-server-on-virtualbox/). Installer un système d'exploitation est une compétence utile à avoir. _(Conseil : Lorsque VirtualBox vous demande de sélectionner le disque, faites-le allouer dynamiquement et d'au moins 50 Go. Cela vous évitera quelques maux de tête plus tard.)_
2. Assurez-vous que vous pouvez accéder à Internet depuis la machine virtuelle et configurez le serveur DNS :

![Image](https://cdn-media-1.freecodecamp.org/images/1VXQI9xykHzqgT9nDFIjTeUU5M0GasTMjVkS)
_Cliquez avec le bouton droit sur la machine puis Paramètres -> Réseau_

Pour configurer le serveur DNS, consultez cet [exemple](https://askubuntu.com/questions/346838/how-do-i-configure-my-dns-settings-in-ubuntu-server).

> Exemple : `dns-nameservers 8.8.8.8 8.8.4.4` Si vous pouvez pinguer Google, alors vous êtes prêt !

3. (Facultatif) Installez le serveur [OpenSSH](https://help.ubuntu.com/lts/serverguide/openssh-server.html) et [Samba](https://help.ubuntu.com/lts/serverguide/samba-fileserver.html). Cela rendra votre vie beaucoup plus facile.

4. **(Facultatif)** Activez le transfert de port. Pour vous connecter directement en SSH à votre machine virtuelle, vous devez activer le transfert de port. Par exemple, pour mapper le **port 2222** sur votre **machine hôte** au **port 22** de votre **machine virtuelle**.

![Image](https://cdn-media-1.freecodecamp.org/images/vxD8ttK0h7T3Rqr9-wsA0dEXaizQ84Zdc9CX)
_Activer le transfert de port : Paramètres -> Réseau -> Transfert de port_

Si vous avez activé le transfert de port, vous pouvez maintenant vous connecter en SSH à votre machine virtuelle depuis votre machine hôte comme illustré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/iZh3PIg0ZdEnaSqoCvfa8us076gknELpRYRX)
_FIG1 : ssh -p 2020 denis@localhost_

Remarque : Si vous êtes sous Windows, vous avez besoin de **Putty** pour vous connecter en SSH à la machine virtuelle.

5. Branchez votre NodeMCU et exécutez la commande suivante :

`tail -f /var/log/kern.log`

Cela devrait vous révéler que le périphérique a été identifié comme /dev/ttyUSB0. Si rien ne se passe, vous devez ajouter l'USB à la machine virtuelle. Après avoir ajouté l'USB, débranchez et rebranchez votre périphérique.

![Image](https://cdn-media-1.freecodecamp.org/images/rBbsqsBd84y-dgnFeS6phDTXlM-tOCaXyPiU)
_Ajout de l'USB : Paramètres -> Ports -> USB_

Si vous êtes arrivé à ce stade et que tout fonctionne, **félicitations** ! Vous êtes maintenant prêt à compiler le SDK et à exécuter l'exemple SmartConfig. Vous pouvez même m'envoyer un tweet à [https://twitter.com/metonymyqt](https://twitter.com/metonymyqt)

### **Compilation du SDK et flashage de la carte**

1. Installez les paquets requis (comme ci-dessous). Ces informations sont également disponibles dans le fichier readme.md du SDK.

```
sudo apt-get install make unrar-free autoconf automake libtool gcc g++ gperf flex bison texinfo gawk ncurses-dev libexpat-dev python-dev python python-serial sed git unzip bash help2man wget bzip2 libtool-bin
```

2. Créez un nouveau dossier et naviguez dedans : `mkdir Development && cd Development`

3. Clonez l'Open SDK : [https://github.com/pfalcon/esp-open-sdk](https://github.com/pfalcon/esp-open-sdk)

`git clone --recursive https://github.com/pfalcon/esp-open-sdk.git`

3. Exécutez make : `make`

**Attention : Cette étape prendra un certain temps à se terminer, soyez patient.** Sur ma machine virtuelle, cela a pris 50 minutes. Sur la vôtre, cela peut prendre plus ou moins de temps, mais avant de commencer, assurez-vous que vous êtes **connecté à Internet** et que le **DNS est correctement configuré**. La meilleure façon de vérifier cela est d'exécuter un ping vers Google ou un autre site si Google est bloqué dans votre région.

![Image](https://cdn-media-1.freecodecamp.org/images/rqBC76LdfeK2PStc1YiC1RCFArzHF4IjXXdi)
_Commande ping réussie : $ ping medium.com_

Si votre ping est réussi, vous pouvez minimiser les fenêtres et regarder un épisode de votre émission de télévision préférée. Revenez après environ 40 minutes (mais assurez-vous que votre ordinateur ne s'endort pas).

Après que le SDK ait été compilé avec succès, vous verrez un message vous indiquant de mettre quelque chose dans votre chemin. Pour ce faire, exécutez ce qui suit :

```
echo 'export PATH=/home/denis/Development/esp-open-sdk/xtensa-lx106-elf/bin:$PATH' >> ~/.profile
```

La commande ajoutera la chaîne au fichier **~/.profile**. Exécutez maintenant la commande suivante :

`xtensa-lx106-elf-gcc --version`

Si la commande s'exécute avec succès, alors vous êtes prêt !

4. Testez votre carte

Branchez votre NodeMCU et exécutez **lsusb** pour vérifier que votre périphérique est connecté. Après cela, exécutez **esptool.py chip_id**. Vous devriez maintenant voir l'identifiant de la puce de la carte.

![Image](https://cdn-media-1.freecodecamp.org/images/lf0BJC2bys9XbFPVEzc0B9LsUGtw6dbJtoOl)
_esptool.py chip_id_

5. Clonez [ESP8266_RTOS_SDK](https://github.com/espressif/ESP8266_RTOS_SDK)

```
git clone https://github.com/espressif/ESP8266_RTOS_SDK.git
```

6. Exportez le chemin du SDK et le chemin SDK/BIN en utilisant les commandes ci-dessous.

```
echo 'export SDK_PATH=/home/denis/Development/ESP8266_RTOS_SDK' >> ~/.profile
```

```
echo 'export BIN_PATH=/home/denis/Development/ESP8266_RTOS_SDK/bin' >> ~/.profile
```

7. Compilez l'exemple SmartConfig

```
cd /home/denis/Development/ESP8266_RTOS_SDK/examples/smart_config/
```

```
chmod +x ./gen_misc.sh
```

```
./gen_misc.sh
```

Acceptez maintenant les valeurs par défaut jusqu'à ce que vous soyez invité à entrer **SPI_SIZE_MAP.** C'est là que vous sélectionnez **4** car le NodeMCU a une taille de flash de 32 Mbit, ce qui se traduit par 4 Mo. _Vous pouvez également sélectionner SPI_SPEED 3=80Mhz_

Vous verrez quelque chose comme ceci :

```
!!!SDK_PATH: /home/denis/Development/ESP8266_RTOS_SDKBIN_PATH: /home/denis/Development/ESP8266_RTOS_SDK/bin
```

```
No boot needed.Generate eagle.flash.bin and eagle.irom0text.bin successully in BIN_PATHeagle.flash.bin ---→0x00000eagle.irom0text.bin →0x20000!!!
```

8. Flashez la carte

```
cd $BIN_PATH
```

```
esptool.py erase_flash
```

```
esptool.py write_flash 0x00000 $BIN_PATH/eagle.flash.bin 0x20000 $BIN_PATH/eagle.irom0text.bin 0x3FC000 $BIN_PATH/esp_init_data_default.bin
```

Maintenant, si vous réinitialisez la carte, vous ne devriez voir aucune LED clignoter.

9. Utilisez l'application téléphone

* [Application Android](https://play.google.com/store/apps/details?id=com.cmmakerclub.iot.esptouch&hl=en)
* [Application iPhone](https://itunes.apple.com/us/app/ti-wifi-smartconfig/id580969322?mt=8)

![Image](https://cdn-media-1.freecodecamp.org/images/xoDqT7zXJ7toeEl8Jm-ymdZQvmg7YnzeGwBM)
_Capture d'écran de mon appareil Android_

Ouvrez l'application, assurez-vous d'être connecté à un point d'accès WiFi, entrez votre mot de passe et appuyez sur confirmer. Après quelques secondes, l'ESP8266 devrait se connecter à votre point d'accès. C'est tout. Félicitations pour être arrivé à la fin !

Si vous souhaitez développer davantage avec l'ESP8266-RTOS-SDK, veuillez visiter les sites officiels. Vous y trouverez beaucoup de ressources et de documentation. De plus, veuillez consulter les autres exemples trouvés dans le dossier du SDK.

Merci beaucoup pour le temps que vous avez consacré à la lecture de cet article. Si vous souhaitez me contacter, vous pouvez le faire sur Twitter : [MetonymyQT](https://twitter.com/metonymyqt)

#### Ressources

* [Aperçu de l'ESP8266](https://www.espressif.com/en/products/hardware/esp8266ex/overview)
* [Ressources ESP8266](https://www.espressif.com/en/products/hardware/esp8266ex/resources)
* [Site Web FreeRTOS](https://www.freertos.org/)