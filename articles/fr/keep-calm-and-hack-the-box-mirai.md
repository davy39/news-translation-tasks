---
title: Restez calme et piratez la boîte - Mirai
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2020-08-28T19:41:51.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-mirai
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/cyberpunk-city-rt-2560x1440.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: Linux
  slug: linux
- name: penetration testing
  slug: penetration-testing
seo_title: Restez calme et piratez la boîte - Mirai
seo_desc: 'Hack The Box (HTB) is an online platform that allows you to test your penetration
  testing skills.

  It contains a number of challenges that are constantly updated. Some of them simulate
  real world scenarios and some of them lean more towards a CTF styl...'
---

Hack The Box (HTB) est une plateforme en ligne qui vous permet de tester vos compétences en matière de tests d'intrusion.

Elle contient un certain nombre de défis qui sont constamment mis à jour. Certains d'entre eux simulent des scénarios réels et d'autres s'orientent plus vers un style de défi CTF.

**Note** : _Seuls les write-ups des machines HTB retirées sont autorisés._

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-19-at-23.43.57.png)

Mirai est un bon exemple de la manière dont les appareils IoT mal configurés ont conduit à l'un des plus grands vecteurs d'attaque en 2016. Les appareils IoT sont activement exploités par des botnets et utilisés pour une persistance à long terme par les attaquants.

Nous allons utiliser les outils suivants pour pirater la boîte sur une [Kali Linux box](https://www.kali.org/) :

* nmap
* gobuster
* Medusa
* Commandes Linux

Commençons.

## **Étape 1 - Reconnaissance**

La première étape avant d'exploiter une machine est de faire un peu de scanning et de reconnaissance.

C'est l'une des parties les plus importantes car elle déterminera ce que vous pouvez essayer d'exploiter ensuite. Il est toujours préférable de passer plus de temps sur cette phase pour obtenir autant d'informations que possible.

### **Scan de ports**

Je vais utiliser **Nmap** (Network Mapper). Nmap est un utilitaire gratuit et open source pour la découverte de réseaux et l'audit de sécurité.

Il utilise des paquets IP bruts pour déterminer quels hôtes sont disponibles sur le réseau, quels services ces hôtes offrent, quels systèmes d'exploitation ils exécutent, quel type de filtres de paquets/pare-feu sont utilisés, et des dizaines d'autres caractéristiques.

Il existe de nombreuses commandes que vous pouvez utiliser avec cet outil pour scanner le réseau. Si vous souhaitez en savoir plus, vous pouvez consulter la documentation [ici](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-00.42.40.png)

J'utilise la commande suivante pour effectuer un scan intensif :

```bash
nmap -A -v 10.10.10.48
```

**`-A`** : Active la détection du système d'exploitation, la détection de version, le scan de scripts et le traceroute

**`-v`** : Augmente le niveau de verbosité

**`10.10.10.48`** : IP de la boîte Mirai

Si vous trouvez les résultats un peu trop écrasants, vous pouvez essayer ceci :

```bash
nmap 10.10.10.48
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-00.40.16.png)

Nous pouvons voir qu'il y a 3 ports ouverts :

**Port** 22. Secure Shell (SSH), connexions sécurisées, transferts de fichiers (scp, sftp) et redirection de port

**Port 53**. Domain Name System (DNS)

**Port** 80. Hypertext Transfer Protocol (HTTP). Ici, c'est un serveur IIS.

## **Scan de répertoires**

J'utilise **Gobuster**. Gobuster est un scanner de répertoires écrit en Go. Vous pouvez trouver plus d'informations sur l'outil [ici](https://tools.kali.org/web-applications/gobuster).

Gobuster utilise des listes de mots sur Kali qui se trouvent dans le répertoire **/usr/share/wordlists**. J'utilise des listes de mots de **dirb** et **dirbuster**, mais vous pouvez télécharger plus de listes de mots depuis **SecLists** [ici](https://github.com/danielmiessler/SecLists).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-20-at-20.33.47.png)

J'utilise cette commande pour la liste de mots common.txt de dirb :

```bash
gobuster dir -u 10.10.10.48 -w /usr/share/wordlists/dirb/common.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-00.46.18.png)

Je peux voir quelques dossiers intéressants. Je fais un autre scan de répertoire avec une liste de mots différente.

```bash
gobuster dir -u 10.10.10.48 -w /usr/share/worldlists/dirbuster/directory-list-lowercase-2.3-medium.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-14.31.32.png)

Le dossier **admin** est définitivement celui que je vais visiter !

## **Étape 2 - Visite de la page web**

À partir de la phase de reconnaissance, je décide de commencer par le port 80. Et j'obtiens une page blanche.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-00.57.33.png)

À partir de la phase de reconnaissance, j'ai trouvé le dossier **/admin** avec **Gobuster**. Je navigue vers cet endpoint :

```bash
10.10.10.48/admin
```

J'arrive sur un tableau de bord d'administration Pi-hole.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-01.00.10.png)

> **Pi-hole** est une application de blocage de publicités et de trackers Internet au niveau du réseau Linux qui agit comme un trou noir DNS et optionnellement un serveur DHCP, destinée à être utilisée sur un réseau privé.
>
>
> Pi-hole a la capacité de bloquer les publicités traditionnelles des sites web ainsi que les publicités dans des endroits non conventionnels, tels que les téléviseurs intelligents et les publicités des systèmes d'exploitation mobiles - Wikipedia

Vous pouvez lire plus d'informations [ici](https://en.wikipedia.org/wiki/Pi-hole) ou en apprendre davantage sur le [site officiel](https://pi-hole.net/).

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-14.36.48.png)

Je clique sur le bouton **Login** dans la barre latérale de gauche et je suis présenté avec un écran de connexion. Une recherche rapide sur Internet, et je peux supposer que la cible est une machine Raspberry Pi, et qu'elle exécute probablement [Raspbian](https://en.wikipedia.org/wiki/Raspberry_Pi_OS) (le système d'exploitation de Raspberry Pi).

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-01.00.27.png)

J'ai également découvert que le nom d'utilisateur par défaut devrait être "pi" avec le mot de passe "raspberry". J'essaie le mot de passe par défaut sur cet écran de connexion, mais il ne semble pas fonctionner. Nous devons trouver une autre façon.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-14.50.47.png)

## **Étape 3 - Connexion au Pi-hole via SSH**

Pendant la phase de reconnaissance, nous avons découvert que le port 22 était ouvert.

J'utilise **Medusa** pour vérifier si les identifiants par défaut fonctionnent avec ssh. Medusa est un outil de force brute de connexion rapide, parallèle et modulaire. Vous pouvez trouver plus d'informations [ici](https://en.kali.tools/?p=200) sur cet outil.

```bash
medusa -h 10.10.10.48 -u pi -p raspberry -M ssh
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-15.55.01.png)

Connectons-nous maintenant en utilisant SSH avec la commande suivante, car nous venons de valider que le mot de passe fonctionne :

```bash
ssh pi@10.10.10.48
```

Pour se connecter avec SSH, vous avez besoin du nom d'utilisateur et de l'adresse IP de l'hôte. Dans notre cas, ce serait "pi" pour le nom d'utilisateur et "10.10.10.48" pour l'adresse IP. Le mot de passe est "raspberry".

J'obtiens une session en tant que :

```bash
pi@raspberrypi
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-01.45.08.png)

Une fois connecté en tant qu'utilisateur, je peux vérifier si l'utilisateur appartient ou non au groupe sudo en utilisant soit la commande **id**, soit la commande **groups** :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-14.56.55.png)

L'utilisateur appartient au groupe **root**.

## **Étape 4 - Recherche du flag user.txt**

Je liste tous les fichiers/dossiers avec la commande suivante :

```bash
ls -la
```

Je me déplace ensuite vers le **Desktop** avec

```bash
cd Desktop
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-15.00.25.png)

Et je trouve le flag utilisateur ! Je peux vérifier le contenu du fichier avec

```bash
cat user.txt
```

## **Étape 5 - Recherche du flag root.txt**

Trouvons maintenant le flag root. Je navigue jusqu'au dossier **/** . Vous pouvez vérifier où vous vous trouvez avec la commande

```bash
pwd
```

qui nous donne le répertoire de travail. Je me déplace ensuite vers le dossier **/root** mais l'accès est refusé.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-15.02.28.png)

Je dois changer pour l'utilisateur root pour accéder à ce dossier. J'utilise la commande

```bash
sudo -l
```

pour comprendre quelle commande je peux exécuter sur localhost.

L'utilisateur root a des privilèges illimités et peut exécuter n'importe quelle commande sur le système et nous savons que l'utilisateur pi fait partie du groupe root.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-01.48.25.png)

J'utilise la commande

```bash
sudo su
```

La commande **sudo** vous permet d'exécuter des programmes en tant qu'un autre utilisateur. Par défaut, l'utilisateur root. **su** signifie switch user.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-01.48.58.png)

Je peux maintenant naviguer vers le dossier **root**. Je trouve le fichier root.txt et vérifie son contenu avec

```bash
cat root.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-01.49.46.png)

Malheureusement pour nous, ce n'est pas le flag mais un message qui a été laissé à la place.

```bash
I lost my original root.txt! I think I may have a backup on my USB stick...
```

Je dois maintenant trouver où se trouve l'usb avec la commande

```bash
lsblk
```

pour lister les périphériques de stockage USB. Je peux voir qu'il y a une **usbstick** dans le dossier **/media** :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-15.25.26.png)

Je navigue vers ce dossier et trouve un autre message d'un utilisateur appelé **James**.

```bash
Damnit! Sorry man I accidentally deleted your files off the USB stick.
Do you know if there is any way to get them back?

-James
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-15.16.48.png)

Lorsque nous avons listé tous les périphériques de stockage, nous avons vu que l'usbstick était situé à **sdb**, qui est sous **/dev/sdb/**. Plus d'informations [ici](https://help.ubuntu.com/lts/installation-guide/armhf/apcs04.html) sur les disques et le partitionnement.

Si nous utilisons la commande suivante :

```bash
cat /dev/sdb
```

Nous aurons une longue sortie avec beaucoup de caractères bizarres. À la fin de cette entrée, vous devriez trouver le flag **root**.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-15.38.56.png)

Une manière plus élégante de voir le texte à l'intérieur d'un fichier binaire ou de données est d'utiliser la commande **strings**. Cette commande extrait ces morceaux de texte — appelés « strings ».

```bash
strings /dev/sdb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-15.41.41.png)

Félicitations ! Vous avez trouvé les deux flags.

## **Remédiations**

* Vous pouvez lire plus sur l'attaque du botnet DDoS Mirai [ici](https://www.imperva.com/blog/malware-analysis-mirai-ddos-botnet/)
* Ne pas utiliser de mots de passe par défaut/génériques
* Désactiver l'accès à distance à vos appareils lorsqu'il n'est pas nécessaire

N'hésitez pas à commenter, poser des questions ou partager avec vos amis :)

Vous pouvez voir plus d'articles de la série **Keep Calm and Hack the Box** [ici](https://www.freecodecamp.org/news/search/?query=keep%20calm%20and%20hack%20the%20box).

Vous pouvez me suivre sur [Twitter](https://twitter.com/SonyaMoisset) ou sur [LinkedIn](https://www.linkedin.com/in/sonyamoisset/).

Et n'oubliez pas de #**GetSecure**, #**BeSecure** & #**StaySecure** !

![Image](https://www.freecodecamp.org/news/content/images/2020/08/cyberpunk-city-rt-2560x1440-1.jpg)