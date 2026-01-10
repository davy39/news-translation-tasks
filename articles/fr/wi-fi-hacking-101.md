---
title: Wi-Fi Hacking 101 – Comment pirater WPA2 et se défendre contre ces attaques
subtitle: ''
author: Daniel Iwugo
co_authors: []
series: null
date: '2022-10-18T20:37:37.000Z'
originalURL: https://freecodecamp.org/news/wi-fi-hacking-101
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/image-74-1.png
tags:
- name: Ethical Hacking
  slug: ethical-hacking
- name: hacking
  slug: hacking
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: wifi
  slug: wifi
seo_title: Wi-Fi Hacking 101 – Comment pirater WPA2 et se défendre contre ces attaques
seo_desc: 'Welcome to the world of Wi-Fi hacking, everybody. 💻.

  In my previous article, we talked about some basic Linux skills and tricks. In this
  article you are going to learn a basic Wi-Fi hacking procedure using those skills.

  You''ll learn things such as h...'
---

Bienvenue dans le monde du piratage Wi-Fi, tout le monde. 🔛.

Dans mon [article précédent](https://www.freecodecamp.org/news/linux-basics/), nous avons parlé de quelques compétences et astuces de base sur Linux. Dans cet article, vous allez apprendre une procédure de piratage Wi-Fi de base en utilisant ces compétences.

Vous apprendrez des choses telles que comment :

1. Surveiller les réseaux Wi-Fi autour de vous
2. Effectuer une attaque DOS
3. Vous protéger contre les attaques Wi-Fi

**Avertissement : Ceci est strictement à des fins éducatives uniquement (et, bien sûr, pour un peu de plaisir). Ne vous servez en aucun cas, sous aucune condition ou sous l'influence d'amis imprudents, des hacks que vous apprenez ici contre des organisations, des individus ou votre voisin probablement énervant. Vous commettriez un crime et vous serez soit condamné à une amende, envoyé en prison, ou simplement embarrasserez vos parents.**

Et maintenant que nous avons cette belle introduction derrière nous, procédons. 👋

## Ce que nous allons couvrir :

Voici un aperçu de base de ce que contient ce tutoriel :

1. Introduction
2. Qu'est-ce qu'un paquet ?
3. Comment pirater WPA2
    - Prérequis
    - Comment mettre la carte réseau en mode moniteur
    - Comment chercher la cible
    - Comment capturer les paquets de handshake
    - Comment effectuer une attaque DOS
    - Comment obtenir le mot de passe (espérons-le)
4. Mesures de mitigation contre les attaques WiFi
5. Conclusion

## Introduction

![Un routeur](https://www.freecodecamp.org/news/content/images/2022/10/image-75.png)
_Un routeur § Crédit : Unsplash.com_

La fidélité sans fil (Wi-Fi) est une technologie courante que beaucoup d'entre nous utilisent dans notre vie quotidienne. Que ce soit à l'école, à la maison, ou simplement pour regarder Netflix en continu, il est de plus en plus rare de voir quelqu'un effectuer des activités liées à Internet sans elle.

Mais avez-vous déjà essayé de pirater le Wi-Fi ? 🤔 (Je suis sûr que vous avez été tenté 😏).

Pour pirater quelque chose, vous devez savoir comment cela fonctionne. Cela signifie que vous devez comprendre comment la technologie fonctionne en premier lieu. Alors commençons par les bases : Le Paquet.

## Qu'est-ce qu'un paquet ?

![Un paquet de base](https://www.freecodecamp.org/news/content/images/2022/10/image-76.png)
_Un paquet de base. Crédit : ResearchGate.com_

Un paquet est l'unité de base/le bloc de construction des données dans un réseau informatique. Lorsque des données sont transférées d'un ordinateur à un autre, elles sont décomposées et envoyées en paquets.

Pensez aux paquets comme à des blocs de construction Lego. Vous (l'ordinateur) recevez le set complet (les données complètes) en morceaux (paquets) du vendeur (un autre ordinateur). Vous assemblez ensuite les blocs pour construire la figure basée sur les instructions données afin de l'utiliser (ou dans ce cas, pour que toutes les données aient du sens).

Un paquet, également connu sous le nom de datagramme, est composé de deux parties de base :

1. Un en-tête
2. La charge utile/les données

L'en-tête contient des informations sur le paquet. Cela aide le réseau et l'ordinateur récepteur à savoir quoi en faire, comme les adresses IP source et de destination.

La charge utile est le contenu principal que le paquet contient. Il est également utile de mentionner que les paquets peuvent être chiffrés afin que leurs données ne puissent pas être lues si elles sont interceptées par un attaquant.

Dans un réseau, les paquets sont une exigence pour la commutation de paquets. La commutation de paquets signifie décomposer les données en paquets et les envoyer à divers ordinateurs en utilisant différentes routes. Une fois reçus, les ordinateurs peuvent alors assembler ces paquets pour en comprendre le sens. L'Internet est le plus grand réseau de commutation de paquets connu sur terre.

Maintenant, voyons comment nous pouvons appliquer cette connaissance aux réseaux sans fil.

## Comment pirater WPA2

![Un tas de code aléatoire](https://www.freecodecamp.org/news/content/images/2022/10/image-77.png)
_Un tas de code aléatoire. Crédit : Unsplash.com_

Le Wi-Fi peut utiliser un certain nombre de protocoles variés pour vous offrir une connexion Internet sécurisée. Du moins au plus sécurisé, ils sont :

1. Open
2. WEP (Wired Equivalent Privacy)
3. WPA2 (Wi-Fi Protected Access 2)
4. WPA3 (Wi-Fi Protected Access 3)

Un réseau ouvert est assez tel que le nom l'indique – ouvert. Il n'a pas de mot de passe et pratiquement n'importe qui peut s'y connecter.

Le WEP est un ancien protocole, rarement utilisé et nécessite un mot de passe comme ses successeurs.

Le WPA2 est le protocole le plus couramment utilisé dans le monde. Le WPA3 est le plus récent et le protocole le plus sécurisé connu à ce jour. Mais il est rarement utilisé et n'est disponible que sur les nouveaux appareils.

### Prérequis

Le Wi-Fi fonctionne en envoyant constamment des paquets de données à votre appareil authentifié. Pour le pirater, vous aurez besoin de :

1. Une machine Linux (de préférence Kali Linux)
2. Un adaptateur sans fil

Pour installer Kali à partir de zéro, vous pouvez suivre [ce tutoriel](https://www.freecodecamp.org/news/how-to-install-kali-linux/).

Si ce n'est pas déjà fait, vous devrez installer un outil appelé Aircrack-ng sur votre machine. Pour l'installer, tapez simplement la commande ci-dessous.

```
sudo apt install aircrack-ng
```

### Comment mettre la carte réseau en mode moniteur

Vous voulez d'abord obtenir des informations sur la cible. C'est ce que les hackers appellent la reconnaissance.

Pour ce faire, vous devez d'abord changer votre carte sans fil du mode 'managed' au mode 'monitor'. Cela la transformera d'une simple carte réseau en un lecteur de réseau sans fil.

Tout d'abord, vous devez trouver le nom de votre carte sans fil. Branchez votre adaptateur et exécutez la commande `iwconfig` pour le découvrir. C'est généralement le dernier de la liste.

![iwconfig](https://www.freecodecamp.org/news/content/images/2022/10/image-78.png)
_iwconfig. Crédit : Daniel Iwugo_

Comme vous pouvez le voir, la mienne est `wlan1`. Exécutez maintenant les commandes suivantes :

```
sudo airmon-ng check rfkillsudo
airmon-ng start <network interface>
```

`sudo` indique le besoin de privilèges root, `check rfkill` arrête les processus qui pourraient empêcher la carte de passer en mode moniteur, et `start` indique à airmon-ng quelle carte réseau exécuter. Remplacez `<network interface>` par le nom de votre carte sans fil.

`airmon-ng` est un script qui change instantanément votre carte en mode moniteur. Vous pouvez en fait le faire manuellement ou créer un script vous-même, mais je préfère personnellement quelque chose de plus simple.

### Comment chercher la cible

Pour voir quels réseaux sont autour de vous, exécutez la commande suivante :

```
sudo airodump-ng <network interface>
```

![Airodump](https://www.freecodecamp.org/news/content/images/2022/10/image-81.png)
_Airodump. Crédit : Daniel Iwugo_

`airodump-ng` fait partie de la suite `aircrack-ng` qui permet à une carte réseau de voir le trafic sans fil autour d'elle.

Comme vous pouvez le voir, nous obtenons beaucoup d'informations. Mais jetons un rapide coup d'œil à la colonne ESSID (Extended Service Set Identifier). Également connu sous le nom de nom du point d'accès (AP), cette colonne montre le nom du réseau cible, qui dans mon cas sera 'Asteroid'.

Vous voulez vous concentrer sur le point d'accès cible et ignorer le reste. Pour ce faire, appuyez sur Ctrl+C pour annuler la numérisation actuelle et cette fois, ajoutez le bssid du réseau avec le drapeau bssid comme montré ci-dessous.

```
sudo airodump-ng <network interface> --bssid <AP>
```

![Airodump en action](https://www.freecodecamp.org/news/content/images/2022/10/image-82.png)
_Airodump en action. Crédit : Daniel Iwugo_

Le BSSID signifie Basic Service Set Identifier, un nom fantaisiste pour l'adresse MAC de l'appareil. Vous l'utilisez pour identifier l'appareil sur un réseau, ainsi que l'ESSID (Nom du point d'accès). Techniquement, vous pourriez simplement utiliser le drapeau ESSID à la place, mais différents points d'accès pourraient avoir le même nom. Cependant, aucun deux points d'accès ne peuvent jamais avoir le même BSSID.

Ci-dessous se trouve un extrait de code de ce que vous taperiez pour obtenir des informations sur le point d'accès en utilisant uniquement l'ESSID.

```
sudo airodump-ng <network interface> --bssid <AP ESSID>
```

Remarque : Si le nom contient un espace, encadrez-le avec des guillemets. Par exemple, `--bssid "Asteroid 1"` .

Vous remarquerez que j'ai mis en évidence l'adresse MAC d'un client connecté au point d'accès sous la colonne 'Station'. À sa gauche se trouve l'adresse MAC du point d'accès auquel il est connecté.

### Comment capturer les paquets de handshake

L'étape suivante consiste à capturer les paquets de handshake (vous vous souvenez des paquets ? 👀). Les paquets de handshake sont les quatre premiers paquets envoyés par le point d'accès lorsqu'un appareil authentifié se connecte à un point d'accès.

Cela signifie que nous avons deux options :

1. Attendre qu'un appareil se connecte au point d'accès
2. Désauthentifier l'appareil puis le laisser se connecter au point d'accès

La deuxième option semble beaucoup plus amusante, alors choisissons-la.

![Un clavier LED](https://www.freecodecamp.org/news/content/images/2022/10/image-83.png)
_Un clavier LED. Crédit : Unsplash.com_

### Comment effectuer une attaque DOS

Vous pouvez utiliser `aireplay-ng` ou `mdk4` pour déconnecter les appareils des points d'accès pendant un certain temps. Cela s'appelle une attaque de désauthentification ou une attaque DOS (Denial-Of-Service) sans fil.

Voici le plan de jeu :

1. Configurer airodump-ng pour capturer les paquets et les sauvegarder
2. Désauthentifier l'appareil pendant un certain temps pendant que airodump-ng est en cours d'exécution
3. Capturer le handshake

Vous avez tout compris ? Bien. C'est parti. 👨‍💻👩‍💻

Tout d'abord, exécutez la commande pour capturer et sauvegarder les paquets :

```
sudo airodump-ng -c <channel number> --bssid <AP BSSID> <network interface> -w <path for saved packets file>
```

![Airodump capturant des paquets](https://www.freecodecamp.org/news/content/images/2022/10/image-84.png)
_Airodump capturant des paquets. Crédit : Daniel Iwugo_

Ici, nous utilisons le drapeau `-c` pour spécifier le canal à rechercher, le drapeau `--bssid` pour l'adresse MAC du point d'accès, et le drapeau `-w` pour donner un chemin où vous souhaitez sauvegarder les paquets capturés.

Leçon rapide : Les canaux réduisent les chances que les points d'accès interfèrent les uns avec les autres. Lorsque vous exécutez `airodump-ng`, vous pouvez identifier le numéro de canal sous la colonne CH.

Pendant que cela est en cours d'exécution, vous allez lancer votre attaque de désauthentification contre l'appareil qui y est connecté en utilisant la commande :

```
sudo aireplay-ng -a <BSSID of the AP> --deauth <time> <network interface>
```

Le drapeau `-a` spécifie l'adresse MAC du point d'accès, `--deauth` spécifie combien de temps vous souhaitez que l'attaque s'exécute en secondes, suivi de la carte réseau.

Une attaque de désauthentification consiste à utiliser votre propre carte réseau pour envoyer des paquets afin d'interrompre la communication entre le point d'accès et le client. Ce n'est pas parfait et parfois le client peut se reconnecter, mais seulement pour un court moment.

Si votre Wi-Fi agit de manière étrange et que vous semblez vous déconnecter et vous reconnecter aléatoirement, vous pourriez subir une attaque de désauthentification.

Dans la commande ci-dessus, vous ciblez le point d'accès et exécutez l'attaque. Notez que vous pouvez plutôt attaquer n'importe quel appareil connecté au point d'accès et vous devriez obtenir le même résultat. Tout ce que vous avez à faire est de changer le drapeau `-a` en l'adresse MAC de n'importe quel appareil connecté.

Pendant que l'attaque DOS est en cours, vérifiez votre scan airodump. Vous devriez voir en haut à droite : `WPA handshake: <mac address>`. Une fois que vous avez vérifié cela, vous pouvez arrêter l'attaque de relecture et le scan `airodump-ng`.

![Effectuer l'attaque de relecture pour obtenir le handshake](https://www.freecodecamp.org/news/content/images/2022/10/image-85.png)
_Effectuer l'attaque de relecture pour obtenir le handshake. Crédit : Daniel Iwugo_

### Comment obtenir le mot de passe (espérons-le)

Dans les étapes finales, vous allez exécuter une série de clés principales par paires générées (PMK) contre les paquets capturés pour obtenir le mot de passe. Laissez-moi vous expliquer.

Une PMK est essentiellement une combinaison algorithmique d'un mot et du nom du point d'accès. Notre intention est de générer en continu des PMK en utilisant une liste de mots contre le handshake. Si la PMK est valide, le mot utilisé pour la générer est le **mot de passe**. Si la PMK n'est pas valide, elle passe au mot suivant de la liste.

Je vais utiliser la liste de mots rockyou située dans le répertoire `/usr/share/wordlists`. Je pense que cela ne se trouve que dans Kali, donc si vous avez un autre système d'exploitation, vous pourriez en créer une vous-même manuellement ou en générer une en utilisant `crunch`.

Si elle n'est pas déjà extraite, exécutez simplement la commande :

```
sudo gunzip /usr/share/wordlists/rockyou.txt.gz
```

Petite leçon d'histoire : La liste de mots rockyou est un ensemble de mots de passe obtenus à partir de l'une des plus célèbres violations de données en cybersécurité qui a affecté une entreprise du même nom. Elle contient environ 14 millions de mots de passe uniques qui ont été utilisés dans plus de 32 millions de comptes et, à ce titre, est l'une des listes de mots les plus fiables de la planète.

Maintenant, exécutez la commande :

```
sudo aircrack-ng <captured file with .cap> -w <path to wordlist>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-86.png)
_Craquage de mot de passe. Crédit : Mercury_

Très bien, tout le monde – mission accomplie 😎.

Le mot de passe était, eh bien… 'password'. Plutôt décevant d'un point de vue sécurité, mais j'ai configuré ce réseau juste pour le plaisir dans le cadre de ce tutoriel. En réalité, cela pourrait prendre des minutes à des heures en fonction de la longueur et de la force du mot de passe.

Pour nettoyer, supprimez simplement les fichiers capturés, fermez vos terminaux et exécutez la commande `service NetworkManager restart` pour remettre votre carte réseau en mode géré afin de pouvoir vous connecter au Wi-Fi.

## Mesures de mitigation contre les attaques WiFi

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-87.png)
_Une configuration de base d'un espace de travail personnel § Crédit : Wallpaperflare.com_

La sécurité Wi-Fi de base devrait couvrir cette attaque d'un point de vue défensif. L'utilisation de WPA3, qui est un protocole plus récent, est votre meilleur atout contre une telle attaque. Pour atténuer les attaques de désauthentification, utilisez une connexion Ethernet si possible.

En supposant que cette option ne soit pas sur la table, vous pouvez utiliser une phrase de passe forte (et non un mot de passe) pour minimiser les chances de l'attaquant de l'obtenir. Une phrase de passe est une chaîne de mots simplement utilisée comme mot de passe. Les phrases de passe tendent à être plus longues que les mots de passe, plus faciles à retenir et sont une pratique plus rare. Par conséquent, elles seront rarement trouvées dans les listes de mots.

Par exemple, 'mercury' est plus susceptible d'être trouvé dans une liste de mots que 'mercurylovespluto'. Cette dernière est une phrase de passe de 15 caractères et aussi simple soit-elle, il serait difficile pour un attaquant de la trouver, de la deviner ou de la générer.

Une autre mesure de mitigation serait de désactiver le WPS (Wi-Fi Protected Setup) et d'éviter dans toutes les circonstances d'utiliser un routeur qui utilise le protocole WEP. Vous ne feriez que demander une attention non désirée, car il est beaucoup plus facile de pirater les deux que le WPA2.

## Conclusion

Faisons un résumé de ce que vous avez appris :

1. Changer l'adaptateur sans fil en mode moniteur en utilisant airmon-ng
2. Scanner le point d'accès cible en utilisant airodump-ng et capturer les paquets
3. Effectuer une attaque DOS sur le point d'accès pour obtenir les paquets de handshake
4. Mettre fin à l'attaque DOS une fois que vous avez vérifié avoir capturé le paquet nécessaire
5. Utiliser aircrack-ng pour générer des PMK à exécuter contre les paquets de handshake

Parfois, le mot de passe peut ne pas être dans la liste de mots. Dans ce cas, il existe de nombreuses autres façons d'obtenir le mot de passe, comme une attaque Evil Twin ou des variations de ce que vous avez appris ici. Je vous encourage également à pratiquer cela et de nombreuses autres attaques que vous découvrirez, car cela vous aide à devenir un hacker expert.

Rappelez-vous, ceci est **strictement à des fins éducatives**. Ne le faites que sur d'autres avec leur consentement, ou sur vos propres appareils.

Et avec cela, nous arrivons à la fin de cet article. J'espère que vous l'avez apprécié. Et comme je le dis toujours, Bon piratage ! 👋

### Ressources

1. [Un peu plus d'explications sur la théorie du handshake](https://www.javatpoint.com/handshake-theory)
2. [Plus de détails sur les paquets](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)
3. [WPA2 vs WPA3](https://www.diffen.com/difference/WPA2_vs_WPA3)

### Remerciements

Merci à [Anuoluwapo Victor](https://twitter.com/Anuoluwap__o?t=4Cv6VR2c2_wK5HLXwbvXCQ&s=09), [Chinaza Nwukwa](https://www.linkedin.com/in/chinaza-nwukwa-22a256230/), [Holumidey Mercy](https://www.linkedin.com/in/mercy-holumidey-88a542232/), [Favour Ojo](https://www.linkedin.com/in/favour-ojo-906883199/), [Georgina Awani](https://www.linkedin.com/in/georgina-awani-254974233/), et ma famille pour l'inspiration, le soutien et les connaissances utilisées pour mettre cet article ensemble. Vous êtes mes héros méconnus.

Crédit photo de couverture : Lego Gentlemen travaillant sur un routeur de Wallpaperflare.com