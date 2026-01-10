---
title: Comment Ajouter Wemo à Homekit Avec Cet Outil Puissant
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-03T21:42:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-wemo-to-homekit-with-this-powerful-tool
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/Copy-of-Dashboard.png
tags:
- name: smart home
  slug: smart-home
seo_title: Comment Ajouter Wemo à Homekit Avec Cet Outil Puissant
seo_desc: 'By Jared Wolff

  This post is originally from www.jaredwolff.com

  I’ve been nerding out. It’s something I just can’t stop sometimes.

  Most recently working on making our home more connected and efficient. Part of the
  effort was experimenting with some We...'
---

Par Jared Wolff

**Cet article provient à l'origine de [www.jaredwolff.com](https://www.jaredwolff.com/how-to-deploy-homebridge-on-raspberry-pi-w-resin/)**

Je me suis plongé dans la technologie. C'est quelque chose que je ne peux parfois pas m'empêcher de faire.

Récemment, j'ai travaillé à rendre notre maison plus connectée et efficace. Une partie de cet effort consistait à expérimenter avec quelques Wemos que j'avais achetés sur eBay il y a environ un mois. L'application Wemo fonctionne assez bien, mais il y a définitivement plus à désirer. (De plus, cela me fait grimacer de penser que chaque Wemo fonctionne avec DDWRT)

Le problème principal ? Wemo ne supporte pas Apple Homekit.

Alors, je me suis mis à faire des recherches et j'ai trouvé le projet [Homebridge](https://github.com/nfarina/homebridge) qui était exactement ce que je cherchais. Basiquement, il émule un appareil qui fonctionne sur le protocole HAP que Apple supporte pour Homekit. Dans Homebridge, vous pouvez configurer autant d'appareils via autant d'interfaces différentes que vous pouvez imaginer. Le déployer sur un Raspberry Pi, ou similaire, peut être problématique et semé d'erreurs. Alors, pourquoi ne pas prendre une approche différente ?

_Entrez Resin OS._

Certains avantages de Resin OS sont :

- Déployer une image pré-optimisée pour la plateforme Yocto
- Aucune configuration de Linux nécessaire (sauf pour le config.json)
- Être opérationnel en quelques minutes (principalement le flashage et l'initialisation du conteneur)

J'ai initialement joué avec la plateforme en ligne de Resin qui montre quelques promesses. Pour les développeurs qui ne veulent pas passer de temps à écrire du code pour les mises à jour OTA et à construire des images Yocto manuellement, vous devriez définitivement jeter un œil à Resin.io.

(En passant, je n'ai aucune affiliation avec Resin, je pense qu'ils ont fait un excellent travail et qu'ils ont contribué de manière significative à la communauté avec leurs outils open source : [http://resinos.io](http://resinos.io/) , [https://etcher.io](https://etcher.io/) , [https://www.balena.io](https://www.balena.io/) )

![HomeKit sur iPhone](https://www.jaredwolff.com/how-to-deploy-homebridge-on-raspberry-pi-w-resin/images/1*duqqYCYgcr1F3f8MNkj0Sg.jpg)

_Alors, comment faire fonctionner un Wemo avec Homekit ?_

Resin eux-mêmes ont une documentation fantastique. J'ai à peine eu besoin de chercher ailleurs lorsque des messages d'erreur sont apparus lors du développement de ma première tentative de conteneur Docker. (J'utilisais initialement l'image _slim_ qui ne contient pas toutes les utilités nécessaires que Homebridge nécessite, il est plus facile d'utiliser l'image _latest_ à la place)

Les instructions sont les suivantes :

1. Installez les dépendances. Sur Mac, _Node_ est la seule chose que vous devrez peut-être installer. Homebrew fonctionne le mieux ici.

    ```
    brew install node
    ```

2. Téléchargez et installez le resin-cli :

    ```
    npm install --global --production resin-cli
    ```

3. Téléchargez votre image depuis le [lien de téléchargement](https://resinos.io/#downloads) si vous ne l'avez pas déjà fait.
4. Modifiez l'image à votre guise en utilisant le cli.

    ```
    $ sudo resin local configure ~/Downloads/resin.img
    ? Network SSID Wolff Den
    ? Network Key This is not our password.
    ? Do you want to set advanced settings? Yes
    ? Device Hostname resin
    ? Do you want to enable persistent logging? no
    Done!
    ```

5. "Flashez" l'image sur une carte SD. Assurez-vous d'avoir un périphérique libre pour écrire dessus !

    ```
    $ sudo resin local flash ~/Downloads/resin.img
    Password:
    ? Select drive (Use arrow keys)
    ✩ /dev/disk1 (32 GB) - RESIN
    ```

6. Attendez que le processus se termine, puis éjectez la carte. Insérez-la dans le périphérique pour lequel vous avez configuré l'image.
7. Une fois démarré, vous devriez pouvoir pinguer le périphérique.

    ```
    ping resin.local
    PING resin.local (192.168.7.45): 56 data bytes
    64 bytes from 192.168.7.45: icmp_seq=0 ttl=64 time=9.004 ms
    64 bytes from 192.168.7.45: icmp_seq=1 ttl=64 time=6.411 ms
    64 bytes from 192.168.7.45: icmp_seq=2 ttl=64 time=4.337 ms
    64 bytes from 192.168.7.45: icmp_seq=3 ttl=64 time=4.374 ms
    ```

8. Modifiez le fichier config.json à votre guise. Il est fortement suggéré de changer le code PIN en quelque chose de différent, car c'est celui que Homebridge utilise dans leurs exemples.
9. De plus, n'hésitez pas à modifier le Dockerfile pour correspondre à vos besoins. Dans cet exemple, la seule chose que vous pourriez vouloir changer est le nom de l'image. Par défaut, j'ai hummingboard-node:latest comme image principale.
10. Vous pouvez maintenant pousser le fichier Docker Homebridge inclus et les fichiers associés directement vers votre périphérique embarqué.

    ```
    sudo resin local push resin.local --source .
    ```

    _Note : cela prendra plusieurs minutes car il construira l'image docker sur le périphérique embarqué. Cela prend beaucoup moins de temps en utilisant la plateforme Resin.io car elle construit sur votre machine locale et l'envoie ensuite au périphérique embarqué en tant qu'image complète_

11. Attendez de voir la sortie de Homebridge indiquant qu'il est en cours d'exécution.
    rdt push completed successfully!

    ```
    Streaming application logs..
    *** WARNING *** The program 'node' uses the Apple Bonjour compatibility layer of Avahi.
    *** WARNING *** Please fix your application to use the native API of Avahi!
    *** WARNING *** For more information see <http://0pointer.de/avahi-compat?s=libdns_sd&e=node>
    *** WARNING *** The program 'node' called 'DNSServiceRegister()' which is not supported (or only supported partially) in the Apple Bonjour compatibility layer of Avahi.
    *** WARNING *** Please fix your application to use the native API of Avahi!
    *** WARNING *** For more information see <http://0pointer.de/avahi-compat?s=libdns_sd&e=node&f=DNSServiceRegister>
    [2017-11-2 02:09:43] Loaded plugin: homebridge-platform-wemo
    [2017-11-2 02:09:43] Registering platform 'homebridge-platform-wemo.BelkinWeMo'
    [2017-11-2 02:09:43] ---
    [2017-11-2 02:09:43] Loaded config.json with 0 accessories and 1 platforms.
    [2017-11-2 02:09:43] ---
    [2017-11-2 02:09:43] Loading 1 platforms...
    [2017-11-2 02:09:43] [WeMo Platform] Initializing BelkinWeMo platform...
    Scan this code with your HomeKit App on your iOS device to pair with Homebridge:

        ┌─────────────────┐
        │ 031-45-154     │
        └─────────────────┘

    [2017-11-2 02:09:43] Homebridge is running on port 51826.
    [2017-11-2 02:09:43] [WeMo Platform] Found: Master Den [123456789ABC]
    [2017-11-2 02:09:43] [WeMo Platform] Found: Jarchel Den [123456789BAC]
    [2017-11-2 02:09:43] [WeMo Platform] Found: Front Door Light [123456789CBA]
    [2017-11-2 02:09:44] [WeMo Platform] Jarchel Den - Get state: On
    ```

12. Ouvrez votre téléphone et recherchez un accessoire disponible dans HomeKit. Vous devrez probablement appuyer sur "Je n'ai pas de code ou je ne peux pas scanner ?" et entrer le numéro manuellement.

    ![Camera add accessory](https://www.jaredwolff.com/how-to-deploy-homebridge-on-raspberry-pi-w-resin/images/1*UuC6kIPSdoqRwc1nxssJ0g.jpg)

    ![Add accessory](https://www.jaredwolff.com/how-to-deploy-homebridge-on-raspberry-pi-w-resin/images/1*xEiX3rxFoTnR4uuZNNR_8Q.jpg)

13. Ajoutez votre accessoire en entrant le code d'accès affiché précédemment.

    ![Add accessory with code.](https://www.jaredwolff.com/how-to-deploy-homebridge-on-raspberry-pi-w-resin/images/1*GerWvbaN_jAiXQlHKRaP3Q.jpg)

    ![Homebridge added success!](https://www.jaredwolff.com/how-to-deploy-homebridge-on-raspberry-pi-w-resin/images/1*KcnojEomHxORpWHtCYC2yg.jpg)

Félicitations ! Tous vos appareils Wemo devraient maintenant apparaître. Profitez de l'utilisation de Siri avec vos appareils Wemo.

![Default screen](https://www.jaredwolff.com/how-to-deploy-homebridge-on-raspberry-pi-w-resin/images/1*dHFYz4MWLa5RKIP7w9O67w.jpg)


Vous avez trouvé ce tutoriel utile ? [Voici quelques-uns de mes autres articles liés à Raspberry Pi.](https://www.jaredwolff.com/tags/raspberry-pi/)