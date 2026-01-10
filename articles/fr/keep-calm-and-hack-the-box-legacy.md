---
title: Restez calme et pirater la boîte - Legacy
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2019-08-05T06:29:04.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-legacy
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/126410.jpg
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
seo_title: Restez calme et pirater la boîte - Legacy
seo_desc: Hack The Box (HTB) is an online platform allowing you to test your penetration
  testing skills. It contains several challenges that are constantly updated. Some
  of them simulating real world scenarios and some of them leaning more towards a
  CTF style ...
---

Hack The Box (HTB) est une plateforme en ligne vous permettant de tester vos compétences en tests d'intrusion. Elle contient plusieurs défis qui sont constamment mis à jour. Certains d'entre eux simulent des scénarios réels et d'autres s'orientent davantage vers un style de défi CTF.

**Note**. _Seuls les write-ups des machines HTB retirées sont autorisés._

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-16.55.11.png)

Legacy est la deuxième machine publiée sur Hack The Box et est destinée aux débutants, nécessitant seulement une exploitation pour obtenir l'accès root.

Nous allons utiliser les outils suivants pour pirater la boîte sur une [Kali Linux box](https://www.kali.org/)

* [nmap](https://nmap.org/)
* [zenmap](https://nmap.org/zenmap/)
* [searchsploit](https://www.exploit-db.com/searchsploit)
* [metasploit](https://www.metasploit.com/)

## **Étape 1 - Scanner le réseau**

La première étape avant d'exploiter une machine est de faire un peu de scanning et de reconnaissance.

C'est l'une des parties les plus importantes car elle déterminera ce que vous pouvez essayer d'exploiter par la suite. Il est toujours préférable de passer plus de temps sur cette phase pour obtenir autant d'informations que possible.

J'utiliserai Nmap (Network Mapper). Nmap est un utilitaire gratuit et open source pour la découverte de réseau et l'audit de sécurité. Il utilise des paquets IP bruts pour déterminer quels hôtes sont disponibles sur le réseau, quels services ces hôtes offrent, quels systèmes d'exploitation ils exécutent, quel type de filtres de paquets/pare-feu sont utilisés, et des dizaines d'autres caractéristiques.

Il existe de nombreuses commandes que vous pouvez utiliser avec cet outil pour scanner le réseau. Si vous souhaitez en savoir plus, vous pouvez consulter la documentation [ici](https://tools.kali.org/information-gathering/nmap)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-17.01.22.png)

J'utilise la commande suivante pour obtenir une idée de base de ce que nous scannons

```bash
nmap -sV -O -F --version-light 10.10.10.4
```

**-sV:** Sonde les ports ouverts pour déterminer les informations sur le service/la version

**-O:** Active la détection du système d'exploitation

**-F:** Mode rapide - Scanne moins de ports que le scan par défaut

**--version-light:** Limite aux sondes les plus probables (intensité 2)

**10.10.10.4:** Adresse IP de la boîte Legacy

Vous pouvez également utiliser Zenmap, qui est l'interface graphique officielle de Nmap Security Scanner. Il s'agit d'une application multiplateforme, gratuite et open source qui vise à rendre Nmap facile à utiliser pour les débutants tout en fournissant des fonctionnalités avancées pour les utilisateurs expérimentés de Nmap.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-17.40.09.png)

J'utilise presque le même ensemble de commandes pour effectuer un scan rapide plus. La seule différence est l'ajout du flag -T4

```bash
nmap -sV -T4 -O -F --version-light 10.10.10.4
```

**-T4:** Exécution plus rapide

Si vous trouvez les résultats un peu trop écrasants, vous pouvez passer à l'onglet **Ports/Hôtes** pour obtenir uniquement les ports ouverts

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-17.40.29.png)

Nous pouvons voir qu'il y a 2 ports ouverts:

**Port 139**. Service de session NetBIOS

**Port 445**. Microsoft-DS (Services d'annuaire) Partage de fichiers SMB

Faisons quelques recherches pour voir ce que nous pouvons trouver.

## **Étape 2 - Comprendre la vulnérabilité exploitable MS08-067**

Toujours sur Zenmap, nous recherchons toute vulnérabilité connue

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-18.02.52.png)

J'utilise la commande suivante

```bash
nmap -p 445 --script vuln 10.10.10.4
```

**-p:** Définit le(s) port(s) de destination

**445:** Le port ouvert que nous avons découvert précédemment

**--script vuln:** Vérifie les vulnérabilités spécifiques connues et ne rapporte généralement les résultats que si elles sont trouvées

**10.10.10.4:** Adresse IP de la boîte Legacy

Nous pouvons voir qu'il y a une vulnérabilité, **smb-vuln-ms08-067**, où le système Microsoft Windows est vulnérable à l'exécution de code à distance.

Voici le [CVE](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2008-4250) pour **MS08-067**.

Comprenons d'abord comment fonctionne la correction dans Microsoft et d'où vient cette convention de nommage.

Voici un extrait du [blog de rapid7](https://blog.rapid7.com/2014/02/03/new-ms08-067/)

> En novembre 2003, Microsoft a standardisé son cycle de publication de correctifs. En publiant ses correctifs le deuxième mardi de chaque mois, Microsoft espérait résoudre les problèmes résultant de la publication de correctifs de manière non uniforme. Cet effort est devenu connu sous le nom de Patch-Tuesday. De la mise en œuvre de Patch-Tuesday (novembre 2003) jusqu'en décembre 2008, Microsoft a publié un total de 10 correctifs qui n'ont pas été publiés un Patch-Tuesday, également connus sous le nom de correctifs "hors bande". Le 10ème correctif hors bande publié par Microsoft est décrit dans le [MS08-067](http://technet.microsoft.com/en-us/security/bulletin/ms08-067) bulletin de sécurité



![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2014-01-30-at-11.25.35-AM.png)
_[https://blog.rapid7.com/2014/02/03/new-ms08-067/](https://blog.rapid7.com/2014/02/03/new-ms08-067/)_

Consultons également le [Bulletin de sécurité Microsoft](https://docs.microsoft.com/en-us/security-updates/securitybulletins/2008/ms08-067) sur MS08-067

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-18.19.32.png)
_[https://docs.microsoft.com/en-us/security-updates/securitybulletins/2008/ms08-067](https://docs.microsoft.com/en-us/security-updates/securitybulletins/2008/ms08-067)_

Maintenant que nous avons un peu plus d'informations sur cette vulnérabilité, essayons de l'exploiter !

## **Étape 3 - Exploiter MS08-067**

Nous utilisons Searchsploit, un outil de recherche en ligne de commande pour la base de données Exploit, pour vérifier s'il existe une exploitation Metasploit disponible pour nous à utiliser

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-18.24.39.png)

J'utilise la commande suivante

```bash
searchsploit ms08-067
```

Je lance Metasploit et cherche la commande que je devrais utiliser pour lancer l'exploitation

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-18.34.54.png)

J'utilise la commande pour chercher toutes les charges utiles disponibles pour ms08-067

```bash
search ms08_067
```

Nous trouvons la charge utile pour exploiter la vulnérabilité

```bash
exploit/windows/smb/ms08_067_netapi
```

ms08_067_netapi est l'une des exploitations à distance les plus populaires contre Microsoft Windows. Elle est considérée comme une exploitation fiable et vous permet d'obtenir un accès en tant que SYSTEM, qui est le privilège Windows le plus élevé.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-18.40.33-1.png)

J'utilise la commande suivante pour l'exploitation

```bash
use exploit/windows/smb/ms08_067_netapi
```

Cela lancera l'exploitation. J'utilise cette commande pour afficher les options disponibles

```bash
show options
```

Vous pouvez voir que l'hôte distant (RHOSTS) n'est pas encore défini. Je vais définir l'hôte distant car cette information est nécessaire pour exécuter l'exploitation

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-18.43.05.png)

J'utilise la commande suivante pour définir l'hôte distant en utilisant l'adresse IP de la boîte HTB Legacy

```bash
set RHOSTS 10.10.10.4
```

Vous pouvez également faire une vérification avant d'exécuter l'exploitation et confirmer que la cible est vulnérable

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-18.44.30.png)

J'utilise la commande suivante pour faire la vérification

```bash
check
```

Nous pouvons maintenant exécuter l'exploitation

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-18.46.56.png)

Bingo ! Nous avons une session Meterpreter. Voyons ce que nous pouvons trouver :)

## **Étape 4 - Utiliser Meterpreter pour trouver le flag user.txt**

Du site Web d'Offensive Security, nous obtenons cette définition pour Meterpreter

> Meterpreter est une charge utile avancée, dynamiquement extensible qui utilise des injecteurs de DLL _en mémoire_ et est étendue sur le réseau au moment de l'exécution. Il communique via la socket de l'injecteur et fournit une API Ruby complète côté client. Il dispose d'un historique de commandes, d'une complétion par tabulation, de canaux, et plus encore.

Vous pouvez en savoir plus sur Meterpreter [ici](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/), et découvrir plus de commandes pour cet outil [ici](https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/)

Trouvons le flag user.txt

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-18.56.52.png)

J'utilise la commande suivante pour rechercher le fichier

```bash
search -f user.txt
```

**-f:** Nom du fichier

La commande **search** fournit un moyen de localiser des fichiers spécifiques sur l'hôte cible. La commande est capable de rechercher dans tout le système ou des dossiers spécifiques.

Nous devons maintenant naviguer vers

```bash
c:\Documents and Settings\john\Desktop\user.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-19.06.24.png)

Pour vérifier où vous êtes, vous pouvez utiliser la commande suivante

```bash
pwd
```

Je suis actuellement à

```bash
C:\WINDOWS\system32
```

J'utilise la commande suivante deux fois pour me déplacer vers le répertoire parent

```bash
cd ..
```

J'utilise la commande suivante pour lister tous les fichiers/dossiers lorsque je suis au niveau **C:\**

```bash
ls
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-19.11.06.png)

Je me déplace ensuite vers le dossier où se trouve le flag user.txt. J'utilise **ls** pour lister tous les fichiers sous le dossier **Desktop**

Nous avons trouvé le fichier **user.txt** ! Pour lire le contenu du fichier, j'utilise la commande

```bash
cat user.txt
```

Maintenant que nous avons le flag utilisateur, trouvons le flag root !

## **Étape 5 - Recherche du flag root.txt**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-19.16.04.png)

J'utilise la commande suivante pour rechercher le fichier

```bash
search -f root.txt
```

Nous devons maintenant naviguer vers

```bash
c:\Documents and Settings\Administrator\Desktop\root.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-04-at-19.16.41.png)

Retour à **C:\** pour naviguer vers le dossier **Administrator** puis le dossier **Desktop**. J'utilise **ls** pour lister tous les fichiers sous le dossier **Desktop**

Nous trouvons le fichier **root.txt** !

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

**Autres articles de cette série**

* [Restez calme et pirater la boîte - Lame](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-lame/)
* [Restez calme et pirater la boîte - Devel](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-devel/)
* [Restez calme et pirater la boîte - Beep](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-beep/)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/126410-3.jpg)