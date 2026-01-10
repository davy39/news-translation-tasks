---
title: Restez calme et pirater la boîte - Blocky
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2020-05-21T10:15:25.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-blocky
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/wallpaperflare.com_wallpaper-3.jpg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: hacking
  slug: hacking
- name: Linux
  slug: linux
- name: Security
  slug: security
seo_title: Restez calme et pirater la boîte - Blocky
seo_desc: Hack The Box (HTB) is an online platform allowing you to test your penetration
  testing skills. It contains several challenges that are constantly updated. Some
  of them are simulating real world scenarios and some of them lean more towards a
  CTF style...
---

Hack The Box (HTB) est une plateforme en ligne qui vous permet de tester vos compétences en matière de tests d'intrusion. Elle contient plusieurs défis qui sont constamment mis à jour. Certains d'entre eux simulent des scénarios réels et d'autres s'orientent plus vers un style de défi CTF.

**Note**. _Seuls les write-ups des machines HTB retirées sont autorisés._

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-19-at-22.23.48.png)

Blocky est assez simple dans l'ensemble et était basé sur une machine réelle. Il démontre les risques des mauvaises pratiques de mot de passe ainsi que l'exposition de fichiers internes sur un système public.

Nous allons utiliser les outils suivants pour pirater la boîte sur une [boîte Kali Linux](https://www.kali.org/) :

* nmap
* nikto
* gobuster
* wpscan
* jd-gui
* hash-identifier

Commençons.

J'ajoute blocky dans le fichier /etc/hosts

```bash
nano /etc/hosts
```

avec

```bash
10.10.10.37     blocky.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-21.05.19.png)

## Étape 1 - Reconnaissance

La première étape avant d'exploiter une machine est de faire un peu de scanning et de reconnaissance.

C'est l'une des parties les plus importantes car elle déterminera ce que vous pouvez essayer d'exploiter par la suite. Il est toujours préférable de passer plus de temps sur cette phase pour obtenir autant d'informations que possible.

## Scan des ports

Je vais utiliser **Nmap** (Network Mapper). Nmap est un utilitaire gratuit et open source pour la découverte de réseau et l'audit de sécurité. Il utilise des paquets IP bruts pour déterminer quels hôtes sont disponibles sur le réseau, quels services ces hôtes offrent, quels systèmes d'exploitation ils exécutent, quel type de filtres de paquets/pare-feu sont utilisés, et des dizaines d'autres caractéristiques.

Il existe de nombreuses commandes que vous pouvez utiliser avec cet outil pour scanner le réseau. Si vous souhaitez en savoir plus, vous pouvez consulter la documentation [ici](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.24.38.png)

J'utilise la commande suivante pour effectuer un scan intensif :

```bash
nmap -A -v blocky.htb
```

**-A :** Active la détection du système d'exploitation, la détection de version, le scan de script et le traceroute

**-v :** Augmente le niveau de verbosité

**blocky.htb :** nom d'hôte pour la boîte Blocky

Si vous trouvez les résultats un peu trop écrasants, vous pouvez faire une autre commande pour obtenir uniquement les ports ouverts.

```bash
nmap blocky.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.23.43.png)

Nous pouvons voir qu'il y a 3 ports ouverts :

**Port 21**, File Transfer Protocol (FTP) control (command)

**Port 22**, Secure Shell (SSH), connexions sécurisées, transferts de fichiers (scp, sftp) et redirection de port

**Port** 80, le plus souvent utilisé par Hypertext Transfer Protocol (HTTP)

## Scan des répertoires

J'utilise **Gobuster**. Gobuster est un scanner de répertoires écrit en Go. Plus d'informations sur l'outil [ici](https://tools.kali.org/web-applications/gobuster). Gobuster utilise des listes de mots sur Kali qui se trouvent dans le répertoire **/usr/share/wordlists**. J'utilise des listes de mots de **dirb** et **dirbuster**, mais vous pouvez télécharger plus de listes de mots depuis **SecLists** [ici](https://github.com/danielmiessler/SecLists)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.33.47.png)

J'utilise cette commande pour la liste de mots common.txt de dirb

```bash
gobuster dir -u blocky.htb -w /usr/share/wordlists/dirb/common.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.34.40.png)

Nous pouvons voir qu'il y a des répertoires **WordPress** (wp-admin, wp-content-wp-includes). Il y a aussi quelques autres pages intéressantes (/phpmyadmin et /plugins)

J'utilise **Nikto**. 

> Nikto est un scanner de serveur web Open Source qui effectue des tests complets contre les serveurs web pour plusieurs éléments, vérifie les versions obsolètes de plus de 1250 serveurs, et les problèmes spécifiques aux versions sur plus de 270 serveurs. Il vérifie également les éléments de configuration du serveur tels que la présence de plusieurs fichiers index, les options du serveur HTTP, et tentera d'identifier les serveurs web et logiciels installés. 

Plus d'informations sur l'outil [[ici](https://tools.kali.org/information-gathering/nikto)](null)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.29.51.png)

J'utilise cette commande pour lancer le scan

```bash
nikto -host blocky.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.30.37.png)

Je vois quelques répertoires qui pourraient être intéressants (/wp-content/uploads/ et /wp-login.php)

Enfin, j'utilise **WPScan**. WPScan est un scanner de vulnérabilités WordPress en boîte noire qui peut être utilisé pour scanner les installations WordPress distantes afin de trouver des problèmes de sécurité

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.27.12.png)

J'utilise cette commande pour lancer le scan

```bash
wpscan --url blocky.htb -e
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.27.42.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.28.05.png)

Nous avons un nom d'utilisateur, **Notch**

## Étape 2 - Visite de la page web

Visons les pages que nous avons trouvées lors de la phase de reconnaissance. Commençons par la page web principale. C'est un blog sur Minecraft - **BlockyCraft**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.38.18.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.39.29.png)

Je regarde la page **wiki**. Rien d'intéressant

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-21.19.40.png)

Je jette un coup d'œil à la page **/wp-content/uploads**. Rien d'intéressant

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.31.50.png)

Je trouve le panneau **admin**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.32.27.png)

ainsi que le panneau **phpMyAdmin**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.33.14.png)

Je navigue vers le dossier **/plugins** et trouve deux fichiers **jar**. 

> Un **JAR** est un format de fichier de package généralement utilisé pour agréger de nombreux fichiers de classe Java et des métadonnées et ressources associées en un seul fichier pour la distribution. Les fichiers JAR sont des fichiers d'archive qui incluent un fichier manifest spécifique à Java. Ils sont basés sur le format ZIP et ont généralement une extension de fichier .jar 

Je télécharge les deux fichiers zip sur ma boîte Kali

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.35.15.png)

J'utilise **JD-Gui** pour décompiler les fichiers java. JD-GUI est un utilitaire graphique autonome qui affiche les codes sources Java des fichiers « .class ». Plus d'informations sur l'outil [ici](https://tools.kali.org/reverse-engineering/jd-gui)

Je lance l'outil avec

```bash
jd-gui
```

Et je sélectionne la classe JAVA que je veux lire - **BlockyCore.class**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-21.04.55.png)

Je peux voir un nom d'utilisateur et un mot de passe

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.36.34.png)

Je reviens à **phpMyAdmin** et entre les identifiants que je viens de trouver. J'ai accès à la base de données

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.37.17.png)

Je regarde la table **wp_users** dans le dossier **wordpress** pour voir si je peux obtenir plus d'informations sur les utilisateurs du blog

La requête SQL

```bash
SELECT * FROM `wp_users`
```

qui peut être traduite par sélectionner tous les utilisateurs de la table wp_users ne nous donnerait qu'un seul résultat, **Notch**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.40.27.png)

J'utilise **hash-identifier** pour identifier le possible hash. Hash-identifier est un logiciel pour identifier les différents types de hachages utilisés pour crypter les données et surtout les mots de passe. Vous pouvez trouver plus d'informations [ici](https://tools.kali.org/password-attacks/hash-identifier).

Je lance hash-identifier avec la commande suivante :

```bash
hash-identifier
```

et je copie/colle le mot de passe haché que j'ai obtenu précédemment :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.41.04.png)

Nous voyons que le hachage est très probablement un **hachage MD5 (Wordpress)**

## Étape 3 - Utilisation du port 22

Je reviens sur mon terminal et me connecte en utilisant SSH

> Le protocole SSH (également appelé Secure Shell) est une méthode de connexion à distance sécurisée d'un ordinateur à un autre. Il offre plusieurs options alternatives pour une authentification forte, et il protège la sécurité et l'intégrité des communications avec un chiffrement fort. C'est une alternative sécurisée aux protocoles de connexion non protégés (tels que [**telnet**](https://www.ssh.com/ssh/telnet), rlogin) et aux méthodes de transfert de fichiers non sécurisées (telles que [**FTP**](https://www.ssh.com/ssh/ftp/)).

Plus d'informations [ici](https://www.ssh.com/ssh/protocol/) sur le protocole SSH

J'utilise la commande suivante

```bash
ssh notch@10.10.10.37
```

et j'entre le mot de passe que j'ai trouvé dans le fichier **BlockyCore.class** précédemment

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.41.56.png)

## **Étape 4 - Recherche du flag user.txt**

Je suis maintenant connecté en tant que Notch. Je liste tous les dossiers/fichiers

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.43.06.png)

Je trouve le fichier **user.txt** ! 

Pour lire le contenu du fichier, j'utilise la commande

```bash
cat user.txt
```

Maintenant que nous avons le flag utilisateur, trouvons le flag root !

## **Étape 5 -** Élévation de privilèges

Je vérifie l'utilisateur actuel avec **sudo**. 

> sudo est un programme pour les systèmes d'exploitation informatiques de type Unix qui permet aux utilisateurs d'exécuter des programmes avec les privilèges de sécurité d'un autre utilisateur, par défaut le superutilisateur. Il signifiait à l'origine « superutilisateur do » car les anciennes versions de `sudo` étaient conçues pour exécuter des commandes uniquement en tant que superutilisateur

Plus d'informations sur sudo [ici](https://en.wikipedia.org/wiki/Sudo)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-21.56.47.png)

Je liste les privilèges de l'utilisateur avec cette commande

```bash
sudo -l
```

J'utilise le même mot de passe que j'ai trouvé précédemment

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.44.08.png)

Je peux voir que Notch a des privilèges illimités et peut exécuter n'importe quelle commande sur le système. Je vérifie l'id. La **commande id** sous Linux est utilisée pour trouver les noms d'utilisateur et de groupe et les identifiants numériques de l'utilisateur actuel ou de tout autre utilisateur sur le serveur

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-22.01.37.png)

Je m'élève à root en utilisant cette commande

```bash
sudo su
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.45.35.png)

## **Étape 6 - Recherche du flag root.txt**

Je suis maintenant un utilisateur **root** et peux naviguer vers le dossier root

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.46.20.png)

Je trouve le fichier **root.txt** ! 

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.48.59.png)

Pour lire le contenu du fichier, j'utilise la commande

```bash
cat root.txt
```

Félicitations ! Vous avez trouvé les deux flags !

---

N'hésitez pas à commenter, poser des questions ou partager avec vos amis :)

Vous pouvez voir plus de mes articles [ici](https://www.freecodecamp.org/news/author/sonya/)

Vous pouvez me suivre sur [Twitter](https://twitter.com/SonyaMoisset) ou sur [LinkedIn](https://www.linkedin.com/in/sonyamoisset/)

Et n'oubliez pas de #**GetSecure**, #**BeSecure** & #**StaySecure** !

---

**Autres articles Hack The Box**

* [Restez calme et pirater la boîte - Lame](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-lame/)
* [Restez calme et pirater la boîte - Legacy](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-legacy/)
* [Restez calme et pirater la boîte - Devel](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-devel/)
* [Restez calme et pirater la boîte - Beep](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-beep/)
* [Restez calme et pirater la boîte - Optimum](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-optimum/)
* [Restez calme et pirater la boîte - Arctic](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-arctic/)
* [Restez calme et pirater la boîte - Grandpa](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-grandpa/)
* [Restez calme et pirater la boîte - Granny](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-granny/)
* [Restez calme et pirater la boîte - Bank](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-bank/)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/wallpaperflare.com_wallpaper-2.jpg)