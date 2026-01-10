---
title: Comment installer Kali Linux sur votre ordinateur
subtitle: ''
author: Daniel Iwugo
co_authors: []
series: null
date: '2022-09-15T19:37:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-kali-linux
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/install-kali-linux-article-image.png
tags:
- name: kali
  slug: kali
- name: Linux
  slug: linux
seo_title: Comment installer Kali Linux sur votre ordinateur
seo_desc: "Kali Linux (formerly known as BackTrack) is an open-source Linux distro\
  \ developed and funded by Offensive Security. \nIt’s basically an ethical hacker's\
  \ dream operating system, because it has most of the tools you'll ever need built-in.\
  \ From Metasploi..."
---

Kali Linux (anciennement connu sous le nom de BackTrack) est une distribution Linux open-source développée et financée par Offensive Security. 

C'est essentiellement le système d'exploitation de rêve d'un hacker éthique, car il possède la plupart des outils dont vous aurez jamais besoin intégrés. De Metasploit à JohntheRipper en passant par le célèbre Aircrack-ng, ce système d'exploitation a tout pour plaire. 

Mais assez de leçons d'histoire. Plongeons directement dans le vif du sujet et apprenons comment installer Kali Linux sur votre ordinateur.

# Prérequis

Avant de continuer, vous devez savoir que ce processus est destiné à l'installation sur le système nu lui-même et vous devez faire cela avec une extrême prudence. 

Si vous souhaitez faire un dual boot de votre machine, vous devrez partitionner votre disque dur pour donner à Kali au moins 20 Go d'espace disque et l'installer sur cette partition.

Maintenant, vous allez avoir besoin de quelques ingrédients pour ce chef-d'œuvre :

1. Un ordinateur (Configuration minimale : 20 Go d'espace disque, 2 Go de RAM, Intel Core i3 ou équivalent AMD E1)
2. Une clé USB (6 Go ou plus)
3. Un fichier .iso de Kali
4. Rufus (Pour créer un lecteur amorçable)
5. Une tête vraiment froide (Faites-moi confiance, vous en aurez besoin 🤪)

# Comment installer Kali Linux sur votre ordinateur – Étape par étape

### Étape 1 : Télécharger le fichier iso

Rendez-vous sur kali.org et cliquez sur le bouton de téléchargement.

![La page d'accueil de Kali](https://miro.medium.com/max/1400/1*MTx3vLNW5O0Gy_0EFUO1YA.png)
_La page d'accueil de Kali | Crédit : kali.org_

Ce que vous essayez d'obtenir est un fichier iso, qui est simplement un moyen d'emballer un logiciel. Les systèmes d'exploitation sont généralement emballés comme cela (mais aussi les logiciels malveillants, alors faites attention à l'endroit où vous les obtenez💀).

Ici, vous avez beaucoup d'options, mais choisissez « Bare Metal ». Il existe des options pour 64 bits, 32 bits et Apple M1 (bien que je n'aie aucune idée de pourquoi la dernière existe). Choisissez l'onglet applicable à votre système et téléchargez l'installateur. Pour les amateurs de torrent, le torrent est également disponible.

![L'option Installateur](https://miro.medium.com/max/1400/1*KVktfnfGlFhxwq48ZFDG7Q.png)
_L'option Installateur | Crédit : kali.org_

### Étape 2 : Créer un lecteur amorçable

Vous pouvez télécharger Rufus depuis [rufus.ie](https://www.freecodecamp.org/news/p/6d73416e-2b28-475d-b6b2-7c5dc3964de9/rufus.ie) (Rufus 3.18 au moment de la rédaction). Pour rendre la clé amorçable, nous allons exécuter Rufus et apporter quelques modifications. 

Connectez la clé et sélectionnez-la sous les options « Device ». Sous « Boot selection », sélectionnez votre fichier iso Kali nouvellement téléchargé. Maintenant, la partie délicate.

![Le logiciel Rufus](https://miro.medium.com/max/948/1*PcHN4n41T7vT_ASJKg-gsw.png)
_Le logiciel Rufus | Crédit : Mercury_

Avant de continuer, une petite leçon : un schéma/table de partition est le format dans lequel un disque dur sauvegarde les données. Pensez à cela comme vos fichiers vidéo sauvegardés en .mp4 ou .mkv – ce sont tous deux des vidéos mais dans des formats différents. 

La plupart des ordinateurs ont l'un des formats suivants : GPT (GUID Partition Table) ou MBR (Master Boot Record). Vous ne pourrez peut-être pas démarrer votre lecteur si vous choisissez la mauvaise option ici. 

Résumé de tout cela : Choisissez l'option MBR si l'ordinateur est ancien ou utilise un BIOS hérité. Choisissez GPT s'il s'agit d'un ordinateur plus récent et utilisant un BIOS UEFI. Si le lecteur n'apparaît pas dans le menu de démarrage, changez pour l'autre option et réessayez.

Vous pourriez également aller dans les propriétés avancées du lecteur et cocher la case « Add fixes for old BIOSes ». Cela devrait rendre le lecteur plus compatible avec votre ordinateur s'il est très ancien. Et par ancien, je veux dire antique 👴.

![Comment préparer la clé USB](https://miro.medium.com/max/1400/1*TD1nOvt2bDkjxmOek_DAJw.gif)
_Comment préparer la clé USB | Crédit : Mercury_

De retour sur un terrain plus facile, vous pouvez laisser les options de format par défaut. Cliquez sur le bouton Start et attendez que l'image soit écrite sur la clé (cela prend un certain temps, alors détendez-vous 😌).

### Étape 3 : Accéder au menu d'installation de Kali

Pour démarrer l'ordinateur à partir de la nouvelle clé USB Kali, vous devrez désactiver le démarrage sécurisé s'il est activé dans les paramètres du BIOS. 

Vous devrez peut-être faire quelques recherches sur la manière d'accéder à votre BIOS et au menu de démarrage. Cela implique généralement de spammer (appuyer continuellement) une touche de votre clavier lorsque l'ordinateur commence à démarrer. 

Comme mentionné précédemment, si vous faites un dual boot, notez la taille de la partition que vous avez faite pour Kali afin de ne pas écraser votre autre système d'exploitation (j'y suis passé, je l'ai fait 😢).

![Un BIOS hérité](https://miro.medium.com/max/1278/1*mDXhfALgd5keOGJ-EaqIRg.png)
_Un BIOS hérité | Crédit : VMware_

Après avoir désactivé le démarrage sécurisé, nous pouvons enfin démarrer sur le lecteur. Au démarrage, vous devrez accéder au menu de démarrage, puis choisir la clé que vous venez de créer. Vous devriez être accueilli avec le menu d'installation de Kali.

![Le menu d'installation de Kali](https://miro.medium.com/max/1280/1*jzUeRWajgAmI-fZDZHC__A.png)
_Le menu d'installation de Kali | Crédit : Mercury_

Note : Vous pouvez également modifier la configuration du menu de démarrage dans le menu du BIOS, mais cela est permanent et devra peut-être être changé après l'installation. Il est généralement préférable de trouver un moyen d'accéder au menu de démarrage lors du démarrage de l'ordinateur, car cela ne sera qu'une configuration temporaire.

Le menu de l'installateur n'autorise que le clavier pour la saisie, vous devrez donc utiliser les touches fléchées, Entrée et Échap pour le naviguer.

### Étape 4 : Commencer l'installation

Sélectionnez l'installation graphique, et vous pouvez maintenant utiliser votre souris. Sélectionnez votre langue préférée, votre région et la disposition de votre clavier dans les menus suivants :

![Menu de la langue](https://miro.medium.com/max/1400/1*NYEFJGMOfhqBxQXNB4T0sw.png)
_Menu de la langue | Crédit : Mercury_

![Menu de la région](https://miro.medium.com/max/1400/1*Mv9NdJx-fOQd-BWBKmI-0w.png)
_Menu de la région | Crédit : Mercury_

Votre ordinateur tentera de faire quelques configurations réseau, mais vous pouvez facilement les ignorer car elles ne seront pas nécessaires pour une installation hors ligne. 

Remplissez un nom d'hôte car cela identifiera votre ordinateur sur un réseau public. Vous pouvez ignorer la partie nom de domaine car cela n'est pas nécessaire. Ensuite, tapez votre nom complet pour votre nouveau compte utilisateur.

![Configuration du nom complet](https://miro.medium.com/max/1400/1*lsyFOCMClUzHtprvS4l26g.png)
_Configuration du nom complet | Crédit : Mercury_

Petite leçon : Sur le terminal, Linux vous permet d'envoyer et de recevoir des e-mails avec des commandes. Cependant, Gmail et Yahoo rendent l'envoi beaucoup plus facile de nos jours. Vous n'aurez peut-être jamais à utiliser cette fonctionnalité de votre vie.

Ensuite, tapez le nom d'utilisateur pour votre compte (ce pourrait être votre alias de hacker 😎).

![Configuration du nom d'utilisateur](https://miro.medium.com/max/1400/1*_tBWjY1VXwNIap2D2ZxdEA.png)
_Configuration du nom d'utilisateur | Crédit : Mercury_

Choisissez un mot de passe/phrase de passe fort à entrer dans le menu suivant.

![Configuration du mot de passe](https://miro.medium.com/max/1400/1*oo1HJdHuJROqIFqTWQFyeA.png)
_Configuration du mot de passe | Crédit : Mercury_

Sélectionnez votre fuseau horaire. Cela est important car cela pourrait affecter vos configurations réseau après l'installation.

![Image](https://miro.medium.com/max/1400/1*tfQU397sBK6jqj4TD5ukWw.png)
_Configuration du fuseau horaire | Crédit :_

### Étape 5 : Configurer le stockage

Ensuite, vous devrez sélectionner la méthode de partitionnement. Maintenant, pour la tête froide mentionnée précédemment. Si vous souhaitez formater l'ensemble du disque dur pour Kali, les options guidées seront les meilleures. 

LVM (Logic Volume Management) est une fonctionnalité qui vous permet d'avoir des partitions relativement flexibles. Cela signifie que vous pouvez étendre, réduire ou même fusionner des partitions pendant que le système d'exploitation est en cours d'exécution. C'est une fonctionnalité assez ingénieuse.

La fonctionnalité LVM chiffrée garde vos données en sécurité si quelqu'un d'non autorisé accède à votre disque dur. Notez simplement qu'il y a un compromis ici : votre disque dur tendra à être plus lent que s'il n'était pas chiffré. Donc, la plupart des gens optent pour l'option « Guided -use entire disk ».

![Méthode de partitionnement](https://miro.medium.com/max/1400/1*ar1ZHAmH9VaWZ8qmZ7qHHQ.png)
_Configuration de la méthode de partitionnement | Crédit : Mercury_

Si vous faites un dual boot, cependant, vous devrez choisir l'option manuelle et faire les configurations nécessaires. Je vais opter pour l'option d'utilisation de l'ensemble du disque ici.

Choisissez le disque dur sur lequel vous souhaitez installer Kali. J'utilise une machine virtuelle, donc ma seule option est un petit disque de 21 Go.

![Sélection du disque dur](https://miro.medium.com/max/1400/1*tRfnHIpCEArhsD6qEFmgeg.png)
_Sélection du disque dur | Crédit : Mercury_

Choisissez comment vous souhaitez que vos fichiers soient partitionnés. Chaque option diffère en séparant certains répertoires importants dans des partitions séparées (Plus d'informations à ce sujet dans un prochain article).

![Image](https://miro.medium.com/max/1400/1*zeEHKH-6fP37V1-N1Wkyug.png)
_Schéma de partitionnement | Crédit : Mercury_

Terminez les modifications de partitionnement.

![Modifications de partitionnement](https://miro.medium.com/max/1400/1*NykY9Az_TGa-CgJutaNSeA.png)
_Infos sur les modifications de partition | Crédit : Mercury_

Sélectionnez « Oui » pour écrire les modifications sur le disque.

![Vérification des partitions](https://miro.medium.com/max/1400/1*OrAElo4Z8TWXZNneinBb3g.png)
_Vérification des modifications de partition | Crédit : Mercury_

### Étape 5 : Choisir les logiciels et l'apparence du bureau

Maintenant, choisissez les logiciels que vous souhaitez installer. Cochez les options d'environnement de bureau et de collection d'outils, car celles-ci vous aideront à éviter d'avoir à installer beaucoup de choses plus tard.

Les environnements de bureau sont essentiellement l'apparence du bureau pour l'utilisateur. Kali propose Xfce (le plus courant), Gnome et KDE. Je suis un fan de Gnome, donc j'ai choisi cette option. Vous pouvez toujours installer les trois et configurer plus tard votre ordinateur pour choisir celui que vous préférez.

![Menu d'installation des logiciels](https://miro.medium.com/max/1400/1*PriqVPIylnMw2y4jVttyZQ.png)
_Menu d'installation des logiciels | Crédit : Mercury_

Vous pouvez cocher la sixième case pour installer les 10 outils les plus populaires sur Kali. Ce sont :  
 1. [Aircrack-ng](https://en.wikipedia.org/wiki/Aircrack-ng)  
 2. [Burpsuite](https://portswigger.net/burp)  
 3. [Crackmapexec](https://mpgn.gitbook.io/crackmapexec/)  
 4. [Hydra](https://en.wikipedia.org/wiki/Hydra_(software))  
 5. [Johntheripper](https://en.wikipedia.org/wiki/John_the_Ripper) (jtr)  
 6. [Metasploit](https://en.wikipedia.org/wiki/Metasploit_Project)  
 7. [Nmap (Network Mapper)](https://en.wikipedia.org/wiki/Nmap)  
 8. [Responder](https://medium.com/mii-cybersec/gaining-credentials-easily-with-responder-tool-b821f33e342b)  
 9. [Sqlmap](https://sqlmap.org/)  
 10. [Wireshark](https://en.wikipedia.org/wiki/Wireshark)

En tant que hacker, vous aurez définitivement besoin de l'un de ces outils tôt ou tard, il est donc préférable de cocher cette case. Vous pouvez cocher la case « default — recommended tools » si vous voulez une multitude d'outils sur votre système, mais notez que cela prendra beaucoup de temps et d'espace. Cliquez sur continuer et attendez.

Conseil rapide : Il est généralement recommandé de n'avoir que les outils dont vous avez absolument besoin sur votre ordinateur. Cela est dû au fait que des outils supplémentaires pourraient ralentir votre ordinateur, vous pourriez gaspiller des données en mettant à jour des outils que vous n'utilisez jamais, et vous êtes susceptible d'être plus vulnérable s'il y a une exploitation active en cours.

### Étape 6 : Installer le chargeur de démarrage GRUB

Le chargeur de démarrage GRUB est un logiciel qui vous permet de choisir quel système d'exploitation démarrer lorsque l'ordinateur démarre. Pour les lecteurs en mono-boot et en dual-boot, la meilleure option ici est « Oui ».

![Configuration du chargeur de démarrage Grub](https://miro.medium.com/max/1400/1*gv_rjUlcVZrlrdVPnXHilQ.png)
_Configuration du chargeur de démarrage Grub | Crédit : Mercury_

Sélectionnez votre disque dur.

![Image](https://miro.medium.com/max/1400/1*b85vz6AEzj_whbr59CP50g.png)
_Configuration du chargeur de démarrage Grub | Crédit : Mercury_

Mission accomplie 🎉🏆. Vous avez installé avec succès votre système d'exploitation Kali Linux. Cliquez sur continuer pour nettoyer et redémarrer votre ordinateur.

![Image](https://miro.medium.com/max/1400/1*H850ppmBcM7hX17PP_4asA.png)
_Configuration du chargeur de démarrage Grub | Crédit : Mercury_

Note : Si vous avez effectué un dual boot, vous devrez peut-être changer le menu de démarrage pour charger Kali en premier avant Windows afin d'avoir l'option de choisir quel système d'exploitation utiliser.

Une fois démarré, votre écran devrait ressembler à celui ci-dessous.

![Écran de connexion](https://miro.medium.com/max/1400/1*tTWw2J3Vkuk-YmbMhpakQA.png)
_Écran de connexion | Crédit : Mercury_

Si vous avez installé l'environnement de bureau xfce, vous devrez entrer votre nom d'utilisateur, entrer votre mot de passe, et vous devriez avoir un bureau bien présenté.

![Bureau Kali](https://miro.medium.com/max/1400/1*2UuoX7GI3gID0Ghekvt4OQ.png)
_Bureau Kali Linux | Crédit : Mercury_

## Conclusion

D'accord, faisons un rapide récapitulatif de ce que nous avons fait :

1. Téléchargé le fichier iso
2. Créé un lecteur amorçable
3. Accédé au menu d'installation de Kali
4. Commencé l'installation
5. Configuré le stockage
6. Installé le chargeur de démarrage GRUB

Et enfin, profitez de votre nouveau système d'exploitation. Bon hacking ! 👋

### Ressources utiles

1. Site web de Kali : [kali.org](http://kali.org)
2. Vous pouvez lire la différence entre MBR et GPT dans cet article de freeCodeCamp : [différence entre une partition MBR et une partition GPT](https://www.freecodecamp.org/news/mbr-vs-gpt-whats-the-difference-between-an-mbr-partition-and-a-gpt-partition-solved/).
3. Voici un article de Kali Linux sur la manière de changer votre environnement de bureau : [comment changer votre environnement de bureau](https://www.kali.org/docs/general-use/switching-desktop-environments/)

### Remerciements

Merci à [Chinaza Nwukwa](https://www.linkedin.com/in/chinaza-nwukwa-22a256230/), [Holumidey Mercy](https://www.linkedin.com/in/mercy-holumidey-88a542232/), [Georgina Awani](https://www.linkedin.com/in/georgina-awani-254974233/) et ma famille pour l'inspiration, le soutien et les connaissances utilisées pour mettre cet article ensemble. Vous êtes les vrais MVP.