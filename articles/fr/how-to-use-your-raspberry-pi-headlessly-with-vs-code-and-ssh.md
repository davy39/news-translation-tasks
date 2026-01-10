---
title: Comment utiliser votre Raspberry Pi sans écran avec VS Code et SSH (aucun moniteur
  nécessaire)
subtitle: ''
author: Josiah Adesola
co_authors: []
series: null
date: '2025-05-27T14:41:53.243Z'
originalURL: https://freecodecamp.org/news/how-to-use-your-raspberry-pi-headlessly-with-vs-code-and-ssh
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1748452192906/594a76a0-be8f-478b-a9ae-e3ba55850c65.png
tags:
- name: Raspberry Pi
  slug: raspberry-pi
- name: ssh
  slug: ssh
- name: vscode extensions
  slug: vscode-extensions
seo_title: Comment utiliser votre Raspberry Pi sans écran avec VS Code et SSH (aucun
  moniteur nécessaire)
seo_desc: 'The Raspberry Pi is a portable computer with an onboard processor that
  fits comfortably in the palm of your hand. Compared with general purpose computers,
  it’s an affordable option developed by the Raspberry Pi Foundation.

  The Raspberry Pi Model B wa...'
---

Le Raspberry Pi est un ordinateur portable avec un processeur intégré qui tient confortablement dans la paume de votre main. Comparé aux ordinateurs polyvalents, c'est une option abordable développée par la [Raspberry Pi Foundation](https://www.raspberrypi.org/).

Le Raspberry Pi Model B a été introduit en 2012 comme la première unité vendable, et la société a depuis sorti de nombreux autres modèles. Il existe même des modèles à bas coût comme la série Raspberry Pi Zero, qui est assez petite et adaptée aux applications de systèmes embarqués. Tous les modèles fonctionnent sur un système d'exploitation appelé Raspberry Pi OS, une version de Linux spécialement conçue pour les ordinateurs Raspberry Pi.

![Un ordinateur monocarte Raspberry Pi Model 4B avec des ports et composants visibles.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747912686077/498ff16a-c6a0-4774-b6e4-a0d573afd4f8.jpeg align="center")

Dans ce tutoriel, nous utiliserons le Raspberry Pi 4 Model pour une configuration sans écran via une connexion SSH en utilisant Visual Studio Code (VS Code). Le Raspberry Pi 4 Model dispose d'un SoC Quad-core ARM Cortex-A72 (64-bit) à 1,5 GHz, jusqu'à 8 Go de RAM, des entrées vidéo, un bouclier Ethernet, des ports USB, un slot pour carte MicroSD pour le stockage, une entrée d'alimentation USB-C et 40 broches d'entrée/sortie à usage général (GPIO). Impressionnant, n'est-ce pas ?

Vous pourrez utiliser le Raspberry Pi comme un ordinateur personnel, pour l'automatisation domestique et les projets IoT, les projets de robotique, les applications réseau, les outils éducatifs et les projets d'intelligence artificielle.

## Table des matières

* [Comprendre la configuration sans écran](#heading-comprendre-la-configuration-sans-ecran)
    
* [Prérequis](#heading-prerequis)
    
* [Préparation de la carte MicroSD](#heading-preparation-de-la-carte-microsd)
    
* [Comment démarrer le Raspberry Pi](#heading-comment-demarrer-le-raspberry-pi)
    
* [Comprendre la LED du Raspberry Pi pendant la configuration](#heading-comprendre-la-led-du-raspberry-pi-pendant-la-configuration)
    
* [Comment établir une connexion SSH](#heading-comment-etablir-une-connexion-ssh)
    
* [Comment configurer Visual Studio Code pour le développement à distance](#heading-comment-configurer-visual-studio-code-pour-le-developpement-a-distance)
    
* [Comment écrire et exécuter le code à distance](#heading-comment-ecrire-et-executer-le-code-a-distance)
    
* [Conclusion](#heading-conclusion)
    

## Comprendre la configuration sans écran

De nombreux ordinateurs Raspberry Pi sont vendus avec des périphériques supplémentaires, y compris un clavier, une souris et un moniteur, qui sont essentiels pour la configuration du Raspberry Pi. Une configuration sans écran est le processus de configuration du Raspberry Pi ou de préparation pour son utilisation sans avoir besoin de ces périphériques. Cela implique de faire fonctionner le Raspberry Pi via un protocole réseau comme SSH (Secure Shell) ou VNC (Virtual Network Computing).

Cela est vraiment utile lorsque vous n'avez pas besoin de périphériques, car cela vous permet d'utiliser votre ordinateur personnel pour vous connecter au Raspberry Pi sans avoir besoin d'acheter des périphériques spécialisés. C'est également excellent pour l'accès à distance. Cette configuration sans écran est également essentielle pour les systèmes de surveillance à distance, tels que les systèmes de surveillance avec accès à distance aux caméras, et les systèmes IoT.

[![Un Raspberry Pi 400 en cours d'utilisation sur un bureau, avec une souris et un moniteur connectés](https://assets.raspberrypi.com/static/neat-lg@2x-38697d13d9952791ca96da4891de9a12.jpg align="left")](https://www.raspberrypi.com/products/raspberry-pi-400/)

Le développement à distance vous permet d'écrire du code et de modifier votre Raspberry Pi et d'autres appareils connectés aux broches GPIO via une configuration sans écran via SSH.

SSH garantit une connexion sécurisée pour le transfert et la modification de fichiers, ainsi que pour le transfert et le débogage de commandes d'un ordinateur (votre ordinateur personnel) à un autre ordinateur (le Raspberry Pi). Il restreint l'accès non autorisé de tout autre système qui vise à intercepter le canal de communication.

## Prérequis

Voici ce dont vous aurez besoin pour suivre ce tutoriel :

### Configuration matérielle requise

1. Raspberry Pi 4 ou 5
    
2. Carte MicroSD (8 Go ou plus recommandé)
    
3. Clé USB avec slot pour carte SD ou un adaptateur pour carte MicroSD
    
4. Alimentation (5V 2A/3A)
    
5. Connexion réseau (Wi-Fi, Pi et ordinateur portable doivent être sur le même réseau)
    
6. Ordinateur personnel (Windows, macOS, Linux)
    

### Configuration logicielle requise

1. Système d'exploitation Raspberry Pi (Raspberry Pi OS)
    
2. Visual Studio Code
    
3. Extension Remote SSH dans VS Code
    

## Préparation de la carte MicroSD

Le Raspberry Pi nécessite une carte MicroSD qui sert de stockage pour le système d'exploitation Raspberry Pi OS en utilisant Raspberry Pi Imager. Le système d'exploitation du Raspberry Pi fournit une interface graphique pour interagir avec le Raspberry Pi, stocker des fichiers et des ensembles de données, et écrire des commandes pour faire fonctionner votre Raspberry Pi.

Mais le Raspberry Pi a besoin d'une carte MicroSD vide pour installer le Raspberry Pi OS dans la carte MicroSD. Voici quelques instructions étape par étape qui vous montreront comment préparer votre carte MicroSD avant de la réinsérer dans le Raspberry Pi pour la connexion SSH.

### Téléchargement et flashage du Raspberry Pi OS

#### Insérez votre carte MicroSD dans une clé USB avec un slot pour carte SD

En plus d'utiliser une clé USB avec un slot pour carte SD (afin de connecter la carte mémoire à l'ordinateur), vous pouvez également utiliser un adaptateur pour carte SD. Assurez-vous qu'elle est insérée dans votre ordinateur où vous avez téléchargé Raspberry PI Imager pour flasher – c'est-à-dire transférer l'OS dans la carte SD.

![Ma clé USB avec un slot pour carte SD](https://cdn.hashnode.com/res/hashnode/image/upload/v1747921369222/7deebdff-d0bc-4f08-9aab-07c562a712bd.jpeg align="center")

#### Téléchargez le [Raspberry Pi Imager](https://www.raspberrypi.com/software/) en fonction du système d'exploitation de votre PC

Cela implique de cliquer sur le lien et de sélectionner votre système d'exploitation (soit MacOS, Windows ou Linux). Le Raspberry Pi OS existe en ces variantes pour différents systèmes d'exploitation.

![Capture d'écran d'une page web de raspberrypi.com montrant des instructions pour installer Raspberry Pi OS en utilisant Raspberry Pi Imager. Elle inclut des liens de téléchargement pour Windows, macOS et Ubuntu. Il y a une commande pour l'installation sur Raspberry Pi OS et une image de l'interface de Raspberry Pi Imager.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747922079380/d1aa21cb-3166-4924-8f98-e2f16816fec6.png align="center")

#### Ensuite, installez et ouvrez le Raspberry Pi Imager

Cliquez sur le téléchargement de Raspberry Pi Imager, suivez toutes les instructions pendant le processus d'installation. Une fois que cet écran apparaît, vous êtes prêt à partir !

![L'image montre l'interface de Raspberry Pi Imager v1.8.5. Elle a des options pour "Choisir l'appareil", "Choisir le système d'exploitation" et "Choisir le stockage". Il y a aussi un bouton "Suivant" en bas. Le fond est d'une teinte de rouge framboise.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747922173921/02e58463-0634-41d6-bc85-0a1a3a199996.png align="center")

#### Choisissez votre appareil Raspberry Pi, le système d'exploitation et sélectionnez le stockage

Pour chacune des trois configurations, vous devez en sélectionner une séquentiellement. Sélectionnez un appareil en fonction du type de Raspberry Pi que vous avez, et diverses options apparaîtront. J'ai sélectionné le Raspberry Pi 4, car c'est mon appareil préféré. Vous pouvez choisir entre le Raspberry Pi 5 et le Raspberry Pi Zero 2 W, selon les exigences de votre appareil.

Ensuite, passez au système d'exploitation – je recommanderais de choisir la version 64-bit. Bien que beaucoup de gens optent pour la version legacy (32-bit), je pense que la version 64-bit est la meilleure. Une fois que vous avez terminé, vous pouvez choisir une option de stockage, et votre MicroSD devrait apparaître. Mon stockage est d'environ 128 Go, c'est pourquoi vous pouvez voir 125,1 Go affiché là dans la capture d'écran ci-dessous :

![Capture d'écran de l'interface de Raspberry Pi Imager v1.8.5. Elle montre des options pour sélectionner un appareil Raspberry Pi, un système d'exploitation et un stockage. Les appareils disponibles incluent Raspberry Pi 5, 4 et Zero 2 W. Les systèmes d'exploitation listés sont Raspberry Pi OS en versions 64-bit et 32-bit, et il y a un appareil USB listé pour le stockage.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747922610658/d5f4c750-ab40-47ed-8c0c-fe5951f68660.png align="center")

#### Cliquez sur « Suivant » et modifiez les paramètres

Il est courant de garder votre nom d'utilisateur comme "pi", mais ce n'est pas obligatoire. Le but est d'avoir quelque chose de simple et facile à retenir lors de la configuration de votre connexion SSH. Il est également utile de rendre votre mot de passe simple. J'ai utilisé 'roboticsai'.

Essayez d'éviter d'utiliser des nombres simplement pour faciliter les choses, car vous ne pourrez peut-être pas voir ce que vous entrez dans le terminal. Ensuite, assurez-vous que votre réseau local sans fil et votre SSID (nom du Wi-Fi ou du point d'accès si vous utilisez un téléphone, ainsi que le mot de passe pour votre Wi-Fi ou votre point d'accès) sont sur le même réseau que celui lié à votre ordinateur.

![Configuration du nom d'utilisateur et du mot de passe du Raspberry Pi](https://cdn.hashnode.com/res/hashnode/image/upload/v1747922797428/c1a1ae55-e109-4a35-878c-820d1ef3f406.png align="center")

#### Cliquez sur « SERVICES » et activez SSH. Ensuite, utilisez l'authentification par mot de passe pour la sécurité et cliquez sur « SAVE ».

Après avoir terminé les modifications dans la section générale, allez dans la section Services et cliquez sur le bouton de case à cocher « *Activer SSH* ». Une fois mis en surbrillance, assurez-vous de choisir « *Utiliser l'authentification par mot de passe* », évitez le bouton « *RUN SSH-KEYGEN* » pour le moment, puis cliquez sur Enregistrer.

![Capture d'écran d'une fenêtre de personnalisation du système d'exploitation sous l'onglet "Services". "Activer SSH" est coché, avec "Utiliser l'authentification par mot de passe" sélectionné. Une option pour "Autoriser uniquement l'authentification par clé publique" est disponible. Un bouton "RUN SSH-KEYGEN" désactivé et un bouton "SAVE" sont visibles.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747923037374/b6c63a5a-e3b6-4c9f-9612-53df7e566e41.png align="center")

#### Cliquez sur « YES » pour appliquer les personnalisations, et le Raspberry Pi OS devrait être flashé dans votre carte SD.

Suite à l'étape précédente, vous verrez divers boutons pour appliquer les ajustements que vous avez effectués. Choisissez oui, et le Raspberry Pi OS sera flashé ou transféré sur votre carte mémoire. Cela peut prendre entre 10 et 20 minutes pour passer du transfert à l'écriture ou à la personnalisation. Attendez et profitez du processus.

![Boîte de dialogue de Raspberry Pi Imager offrant d'appliquer les paramètres de personnalisation du système d'exploitation avec des options pour modifier, effacer, accepter ou refuser.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747923100214/d86fca18-e540-4844-9f26-5253ef5b04b8.png align="center")

#### Après une installation réussie sur le disque, retirez votre carte SD.

Vous recevrez une fenêtre contextuelle de succès comme celle montrée ci-dessous. Cela démontre que tous les processus ont été complétés avec succès, et le Raspberry Pi OS est maintenant installé.

![Une notification sur Raspberry Pi Imager v1.8.5 indique que Raspberry Pi OS (64-bit) a été écrit avec succès sur un périphérique de stockage de masse USB. Elle indique de retirer la carte SD et a un bouton "Continuer".](https://cdn.hashnode.com/res/hashnode/image/upload/v1747926095493/ed017dc6-e3a5-4cda-8b3c-6f6a2d74c1ac.png align="center")

## Comment démarrer le Raspberry Pi

### **Éjectez la MicroSD en toute sécurité de votre ordinateur**

Une fois l'installation réussie, éjectez la MicroSD en toute sécurité de l'ordinateur.

![La carte Raspberry Pi avec un slot pour carte micro SD est placée sur une surface en bois. Une carte micro SD SanDisk de 128 Go est posée à côté.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747926401040/a37dafbb-68ae-4884-9ffe-3c374e6b62b9.jpeg align="center")

### Insérez-la « à l'envers » dans le slot pour carte MicroSD de votre Raspberry Pi

Pour insérer correctement la carte MicroSD, placez-la délicatement dans le slot avec le côté arrière ou doré tourné vers le haut. Elle dépassera légèrement une fois insérée. Vous êtes prêt à partir !

![Un ordinateur monocarte Raspberry Pi placé sur une surface grise, affichant divers ports et composants, y compris des ports USB et un connecteur HDMI.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747926384277/f7a0c5e9-6a13-4cd2-b94a-65b329a08a5c.jpeg align="center")

### Connectez le port USB-C de votre Raspberry Pi à votre ordinateur. Donnez au Raspberry Pi un peu de temps pour charger

Prenez un câble USB-C et connectez une extrémité au port USB-C de votre Raspberry Pi et l'autre à un port d'ordinateur portable. Il devrait s'allumer en rouge, indiquant qu'il y a une source d'alimentation adéquate. Vous pouvez également alimenter votre Raspberry Pi directement en le branchant sur une prise murale.

![Un Raspberry Pi connecté à un ordinateur portable via un câble USB sur une surface en bois.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747926452530/b023abe6-5555-4d61-ab99-0d8e36a828a4.jpeg align="center")

Après un certain temps, la carte mémoire devrait commencer à démarrer sur le Raspberry Pi, et la LED verte clignotera pendant un certain temps. Dans la section suivante, nous parlerons des différents états des deux LED pendant et après un démarrage réussi.

## Comprendre l'état de la LED du Raspberry Pi pendant la configuration

Le tableau ci-dessous décrit les états des LED que vous pourriez voir lorsque vous allumez votre Raspberry Pi et que la carte SD est dans le slot.

| **Couleur de la LED** | **État/Motif** | **Signification/Recommandation** |
| --- | --- | --- |
| 🔴 Rouge | Allumé (ON) | Alimentation stable et suffisante |
| 🔴 Rouge | Éteint ou clignotant | Sous-tension détectée (Utilisez un chargeur de téléphone directement connecté à une prise) |
| 🟢 Vert | Clignotant (Motif irrégulier) | La carte SD est en cours de lecture/écriture (activité de démarrage normale) |
| 🟢 Vert | Allumé (ON) | Le Raspberry Pi est bloqué ou essaie de démarrer. |
| 🟢 Vert | Éteint | Aucune carte SD détectée ou démarrage terminé |
| 🟢 Vert | Motifs de clignotement répétés (par exemple 4 longs, 4 courts) | Code d'erreur indiquant des problèmes de firmware. |
| 🟢 Vert | Clignotement constant | Activité normale (le système d'exploitation Raspbian est en cours de chargement et fonctionne correctement) |

## Comment établir une connexion SSH

La connexion SSH (Secure Shell) est un protocole réseau qui permet à deux ordinateurs de communiquer en toute sécurité sans fuites d'informations. Elle est également utilisée pour l'exécution de commandes à distance et pour le transfert de fichiers entre deux ordinateurs.

Pour établir une connexion SSH, vous devrez suivre quelques étapes. Ensuite, j'expliquerai comment activer SSH en utilisant une extension Visual Studio Code.

### **Créez un fichier** `wpa_supplicant.conf.txt` **dans le même dossier de votre carte SD Raspberry Pi**

Insérez votre carte MicroSD dans l'ordinateur. Ensuite, les fichiers qui composent le Raspberry Pi OS apparaîtront sur votre ordinateur. Créez un nouveau document texte (.txt) sur votre ordinateur, similaire à l'image ci-dessous, dans la section de stockage de la carte SD.

Ajoutez le code ci-dessous, en vous assurant que "ssid" est le nom de votre réseau Wi-Fi et "psk" est le mot de passe de votre réseau.

```plaintext
country=NG # Votre code de pays à 2 chiffres
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
network={
    ssid="Josiah"
    psk="roboticsai"
    key_mgmt=WPA-PSK
}
```

### **Enregistrez le fichier sur la même carte SD**

Une fois que vous avez terminé de produire le fichier texte, enregistrez-le dans le stockage de la carte SD, comme montré dans l'image ci-dessous.

![Capture d'écran d'une fenêtre de l'explorateur de fichiers montrant le contenu du répertoire "bootfs (D:)". Divers fichiers système et de configuration sont listés, y compris des images du noyau et des fichiers .elf. Le fichier sélectionné est "wpa_supplicant.conf.txt".](https://cdn.hashnode.com/res/hashnode/image/upload/v1747928812199/fb766a84-7750-468d-ae78-1ff3c688a52b.jpeg align="center")

### **Créez un dossier .ssh**

Sur votre ordinateur personnel, créez un dossier `.ssh` s'il n'existe pas déjà sur votre ordinateur personnel.

S'il existe, le dossier `.ssh` doit contenir des fichiers comme `id_rsa`, `known_hosts` et `config`. Il ne doit pas être vide.

![Une fenêtre de l'explorateur de fichiers d'ordinateur montrant une liste de dossiers dans le répertoire "JOSIAH". Les noms de dossiers incluent ".matplotlib", ".mchp_cm", ".ssh", et d'autres, avec des détails comme la date de modification et le type. Le dossier ".ssh" est mis en évidence.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747928560247/d07f8cb9-ec22-47ff-a2a5-d18b614e9985.png align="center")

Après un démarrage réussi, ouvrez votre terminal ou votre application de ligne de commande sur votre ordinateur personnel.

![Fenêtre de l'invite de commande montrant "Microsoft Windows [Version 10.0.26100.3915]" et l'invite à "C:sersOSIAH>".](https://cdn.hashnode.com/res/hashnode/image/upload/v1747928958812/2c198297-08a5-4781-9a6a-45fd6c7e85d3.png align="center")

Assurez-vous que le Raspberry Pi est connecté au même réseau avant de continuer. Une fois que votre Wi-Fi ou votre point d'accès mobile est activé, assurez-vous qu'il s'agit du même mot de passe que celui du fichier `wpa_supplicant.conf.txt` et de la page des paramètres lors de l'installation du Raspberry Pi.

Tant que la carte SD est dans le Raspberry Pi et qu'il y a une alimentation adéquate pendant au moins 2 à 5 minutes, le Raspberry Pi se connectera au Wi-Fi ou à votre point d'accès mobile.

![Capture d'écran de l'interface des appareils connectés montrant une limite de 3 appareils. Deux appareils sont listés : "raspberrypi" avec l'adresse MAC d8:3a:dd:43:27:71, et "Josiah" avec l'adresse MAC dc:71:96:d0:d5:4a. Une option de liste de blocage est disponible pour voir les appareils non autorisés à se connecter.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747931364223/13947f34-c1a9-4b1c-b020-c236b4d377af.jpeg align="center")

### Comment résoudre les problèmes de connexion

S'il n'y a pas de connexion, réinstallez le Raspberry Pi OS Imager sur la carte SD. Ensuite, vous pouvez également changer la bande AP du réseau de 5 GHz à 2,5 GHz ou vice-versa. Cela peut être très délicat.

Il devrait se connecter après avoir essayé cela. Assurez-vous simplement que les mots de passe sont cohérents et que vous n'avez pas accidentellement activé la touche de verrouillage des majuscules en tapant, par exemple.

![Capture d'écran d'un écran de configuration de point d'accès portable montrant des champs pour le nom du réseau, le mot de passe, le paramètre de sécurité (WPA2-Personnel), la sélection de la bande AP (5 GHz), et une option pour masquer le SSID, qui est désactivée.](https://cdn.hashnode.com/res/hashnode/image/upload/v1748028008935/192fb282-93c7-4b65-86a2-c26cdfac9d53.jpeg align="center")

Pour confirmer si le Raspberry Pi est connecté en utilisant l'interface de ligne de commande, utilisez la commande `ping` - elle montre les appareils connectés à l'appareil.

```bash
ping raspberrypi.local
```

Après avoir exécuté la commande ci-dessus, vous devriez voir une image montrant la connexion une fois qu'elle est réussie comme ceci :

![Une fenêtre d'invite de commande montrant un test de ping vers "raspberrypi.local" avec une adresse IPv6. Quatre paquets sont envoyés et reçus sans perte. Les temps de trajet aller-retour varient de 6 ms à 125 ms, avec une moyenne de 36 ms.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747931544791/77217325-4f3e-4abb-a136-d4634b773f2d.png align="center")

Pour établir une connexion SSH en utilisant le terminal, exécutez le code ci-dessous :

```bash
ssh pi@raspberrypi.local
```

Cela entraînera une demande de mot de passe. Si cela montre une erreur comme l'image ci-dessous, cela signifie que vous devez supprimer les fichiers `known_hosts.old` et `known_hosts` s'ils existent dans le dossier `.ssh` de votre PC. Cela est dû au fait que les clés sont en conflit les unes avec les autres. Ensuite, réexécutez le code ci-dessus `ssh pi@raspberrypi.local` dans votre terminal.

![Message d'avertissement SSH indiquant un changement dans l'identification de l'hôte distant pour un Raspberry Pi, suggérant une possible écoute ou une mise à jour de la clé de l'hôte. Propose des instructions pour résoudre le problème en mettant à jour le fichier known_hosts.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747931933273/d8f111cc-3455-4de3-af0c-cf0a9814a877.png align="center")

Après une entrée réussie, tapez "`yes`" dans le terminal.

![Interface de ligne de commande montrant une tentative de connexion SSH à un Raspberry Pi. Elle invite l'utilisateur à confirmer l'authenticité de l'hôte avec une empreinte de clé donnée, demandant s'il souhaite continuer la connexion.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747932392301/a09ad065-8e1e-464f-baef-5529eee26ce4.png align="center")

`Connection Closed` devrait s'afficher lorsque la connexion est réussie.

![Capture d'écran d'une fenêtre de terminal montrant une tentative de connexion SSH d'un utilisateur à un Raspberry Pi. L'authenticité de l'hôte est remise en question, demandant une confirmation pour continuer. L'empreinte est affichée, indiquant qu'elle n'est pas connue précédemment. La connexion est ensuite ajoutée aux hôtes connus, avant de se fermer.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747932449402/bcd16bc6-18a1-4a84-82cf-d5c7431345e3.png align="center")

## Comment configurer Visual Studio Code pour le développement à distance

Téléchargez et installez [Visual Studio Code](https://code.visualstudio.com/) si vous ne l'avez pas déjà.

Ensuite, cliquez sur l'extension VS Code et recherchez `Remote - SSH` par Microsoft et installez-la sur votre machine.

![Capture d'écran de la place de marché des extensions Visual Studio Code affichant l'extension "Remote - SSH" par Microsoft. Elle montre les détails d'installation, les évaluations et les fonctionnalités comme l'utilisation d'une machine distante avec SSH pour le développement. La barre latérale de gauche liste les extensions connexes.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747933199343/2c181e3a-80bd-44d1-8b40-5e3cf6191f2b.png align="center")

Ensuite, cliquez sur l'icône "Remote Explorer" qui ressemble à un moniteur. Sélectionnez la configuration SSH dans votre fichier `C:\Users\{name}\.ssh\config`.

![Capture d'écran de Visual Studio Code montrant l'interface de l'extension Remote - SSH. La sélection du fichier de configuration SSH est ouverte, affichant les chemins de fichier. À droite, il y a une description et des détails d'installation pour l'extension, y compris la version et les informations de mise à jour. La barre latérale de gauche affiche une connexion à une machine SSH distante nommée "raspberrypi".](https://cdn.hashnode.com/res/hashnode/image/upload/v1747933364169/7eaa4a7b-294c-41ef-8ecb-fe80151e6399.png align="center")

Assurez-vous que la configuration contient cette commande :

```bash
Host raspberrypi.local
    HostName raspberrypi.local
    User pi
```

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1747933533204/611b6a3d-cd4c-4756-982b-76efb0aa25c9.png align="center")

Entrez votre nom d'utilisateur comme `raspberrypi.local` et saisissez votre mot de passe - le même que le mot de passe lors du chargement du système d'exploitation Raspbian.

![Interface de Visual Studio Code montrant une invite pour entrer un mot de passe pour "pi@raspberrypi.local" pour configurer un hôte SSH. L'arrière-plan présente un guide de raccourcis et une barre de chargement.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747933839359/7f43b231-5177-4b11-9d10-7234961db3f7.png align="center")

Après avoir saisi le mot de passe correct, il devrait commencer à télécharger le serveur.

![Interface de Visual Studio Code montrant des raccourcis clavier pour diverses commandes. Une barre de progression de téléchargement en bas indique "Téléchargement du serveur VS Code...".](https://cdn.hashnode.com/res/hashnode/image/upload/v1747933859344/0c87fd5c-071b-4016-b113-4fc88c166032.png align="center")

Félicitations ! L'image ci-dessous a un bouton rectangulaire bleu montrant `SSH:raspberrypi.local` qui montre une connexion SSH réussie via Visual Studio Code. Cela signifie également que vous pouvez commencer le développement à distance comme nous l'avons discuté précédemment dans ce tutoriel.

![Une capture d'écran de l'écran de bienvenue de Visual Studio Code. L'interface liste les options pour ouvrir un dossier ou cloner un dépôt. La section "Start" a des options comme "New File" et "Open Folder". La section "Recent" affiche une liste de projets récemment consultés. La zone "Walkthroughs" suggère des guides pour commencer. La barre latérale de gauche montre l'explorateur de fichiers et d'autres icônes. La barre d'état en bas indique une connexion SSH.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747933925369/a2aaf412-e465-47e9-8e97-129734f87534.png align="center")

## Comment écrire et exécuter le code à distance

Créez un nouveau fichier sur votre VS Code. De cette manière, vous créez des fichiers et écrivez directement dedans. Allez dans le terminal et tapez les commandes pour créer un dossier et un fichier :

![Capture d'écran de Visual Studio Code montrant une session de terminal et un éditeur de texte. Le terminal est ouvert en bas, avec des commandes pour créer un répertoire, naviguer vers celui-ci et l'ouvrir dans l'éditeur. La zone principale de l'éditeur invite à sélectionner une langue ou à ouvrir un autre éditeur. La barre latérale de l'explorateur est visible à gauche.](https://cdn.hashnode.com/res/hashnode/image/upload/v1747934210225/a6e7f454-6f65-4a87-8692-cadaa642b007.png align="center")

### **Créez un nouveau fichier et écrivez votre code**

Créez un nouveau fichier et nommez-le `led.py` sur votre Visual Studio Code. Il doit être dans le même dossier que `test-raspberry` sur le réseau distant Raspberry Pi via la connexion SSH sur VSCode.

Une fois que vous avez créé votre fichier, vous pouvez écrire votre code tel que le clignotement d'une LED sur un Raspberry Pi, comme vous pouvez le voir dans le code ci-dessous :

```python
from gpiozero import LED
from time import sleep

# Définir la broche GPIO où la LED est connectée
led = LED(17)  # Remplacer 17 par votre numéro de broche GPIO

# Faire clignoter la LED en boucle
while True:
    led.on()        # Allumer la LED
    sleep(1)        # Attendre 1 seconde
    led.off()       # Éteindre la LED
    sleep(1)        # Attendre 1 seconde
```

Après avoir écrit ce code dans le nouveau fichier que vous avez créé, exécutez le code en tapant la commande suivante dans votre terminal :

```bash
python led.py
```

Dès que cette commande est envoyée, la borne positive de la LED est connectée à la broche GPIO 17 selon le code et la borne négative est connectée à la broche GND GPIO du Raspberry Pi. L'image de [Random Nerd Tutorials](https://randomnerdtutorials.com/raspberry-pi-pinout-gpios/) ci-dessous montre les broches GPIO et leurs numéros pour comprendre la connexion. Notez simplement que la connexion de la LED est hors du cadre de ce tutoriel.

![Guide des broches Raspberry Pi : Comment utiliser les GPIOs du Raspberry Pi ? | Tutoriels Random Nerd](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2023/03/Raspberry-Pi-Pinout-Random-Nerd-Tutorials.png?quality=100&strip=all&ssl=1 align="left")

La LED devrait commencer à clignoter chaque seconde selon le code. Avec cela, vous pouvez maintenant contrôler votre Raspberry Pi (un petit ordinateur) avec un autre ordinateur (votre ordinateur personnel) via une connexion SSH sur Visual Studio Code.

## Conclusion

Dans ce tutoriel, vous avez parcouru tout le processus de configuration d'un Raspberry Pi sans écran pour le développement à distance en utilisant VS Code.

Cela offre une large gamme d'avantages : il n'y a pas besoin de périphériques externes, il fournit un accès à distance de n'importe où dans votre réseau, et il tire parti du codage et du débogage efficaces avec l'intégration de VS Code.

Vous pouvez utiliser cela pour déployer des serveurs web et des tableaux de bord IoT, et vous pouvez explorer l'automatisation des processus en utilisant des scripts Python et le contrôle GPIO.