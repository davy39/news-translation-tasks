---
title: Restez Calme et Hack The Box – Valentine
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2021-05-25T22:43:11.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-valentine
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/vapor-synthwave-retro-city-4k-xu.jpeg
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
seo_title: Restez Calme et Hack The Box – Valentine
seo_desc: 'Hack The Box (HTB) is an online platform that allows you to test your penetration
  testing skills.

  It contains several challenges that are constantly updated. Some of them simulate
  real world scenarios and some of them lean more towards a CTF style of...'
---

Hack The Box (HTB) est une plateforme en ligne qui vous permet de tester vos compétences en tests d'intrusion.

Elle contient plusieurs défis qui sont constamment mis à jour. Certains d'entre eux simulent des scénarios du monde réel et d'autres penchent davantage vers un style de défi CTF.

**Note** : _Seuls les write-ups de machines HTB retirées sont autorisés._

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.44.32.png)

Valentine est une machine facile qui se concentre sur la vulnérabilité Heartbleed, qui a eu un impact dévastateur sur les systèmes à travers le monde.

Nous utiliserons les outils suivants pour compromettre la machine :

* Nmap
* Nmap Scripting Engine
* Gobuster
* Searchsploit
* xxd
* OpenSSL
* SSH
* tmux

C'est parti !

## **Étape 1 - Reconnaissance**

La première étape avant d'exploiter une machine est d'effectuer un peu de balayage et de reconnaissance.

C'est l'une des parties les plus importantes car elle déterminera ce que vous pourrez tenter d'exploiter par la suite. Il est toujours préférable de passer plus de temps sur cette phase pour obtenir autant d'informations que possible.

### **Scan de ports**

J'utiliserai **Nmap** (Network Mapper). Nmap est un utilitaire gratuit et open source pour la découverte de réseau et l'audit de sécurité.

Il utilise des paquets IP bruts pour déterminer quels hôtes sont disponibles sur le réseau, quels services ces hôtes offrent, quels systèmes d'exploitation ils utilisent, quel type de filtres de paquets/pare-feu sont utilisés, et des dizaines d'autres caractéristiques.

Il existe de nombreuses commandes que vous pouvez utiliser avec cet outil pour scanner le réseau. Si vous souhaitez en savoir plus, vous pouvez consulter la documentation [ici](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-22.57.05.png)

J'utilise la commande suivante pour effectuer un scan intensif :

```bash
nmap -A -v 10.129.1.190
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-22.57.29.png)

**-A :** Active la détection du système d'exploitation, la détection de version, le scan par script et le traceroute

**-v :** Augmente le niveau de verbosité

**10.129.1.190 :** IP de la machine Valentine

Nous pouvons voir qu'il y a 3 ports ouverts :

* **Port** 22. Secure Shell (SSH), connexions sécurisées, transferts de fichiers (scp, sftp) et redirection de port.
* **Port** 80. Hypertext Transfer Protocol (HTTP).
* **Port** 443. Hypertext Transfer Protocol Secure (HTTPS).

Je décide également de vérifier le nom d'hôte par rapport à la base de données de vulnérabilités de Nmap avec cette commande :

```bash
nmap --script vuln 10.129.1.190
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-23.00.38.png)

Le Nmap Scripting Engine (NSE) est l'une des fonctionnalités les plus puissantes et les plus flexibles de Nmap. Il permet aux utilisateurs d'écrire (et de partager) des scripts simples (en utilisant le [langage de programmation Lua](http://lua.org/)) pour automatiser une grande variété de tâches réseau. Vous pouvez trouver plus d'informations [ici](https://nmap.org/book/man-nse.html).

Vous pouvez trouver les scripts sous :

```bash
/usr/share/nmap/scripts
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-23.08.41.png)

Vous pouvez également rechercher un script spécifique avec la commande **grep**. Plus d'infos sur la commande [ici](https://man7.org/linux/man-pages/man1/grep.1.html).

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-23.09.57.png)

Je regarde les résultats et je peux voir que la machine est vulnérable à **ssl-heartbleed** :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-23.01.56.png)

La section d'information nous donne quelques liens pour en savoir plus sur la vulnérabilité. Le premier lien redirige vers la **Base de données** des vulnérabilités et expositions communes de **MITRE** (CVE).

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-23.04.14.png)
_https://cve.mitre.org/cgi-bin/cvename.cgi?name=cve-2014-0160_

Le programme CVE identifie, définit et répertorie les vulnérabilités de cybersécurité divulguées publiquement.

Il y a un autre lien qui redirige vers l'avis de sécurité OpenSSL.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-23.05.39.png)
_https://www.openssl.org/news/secadv/20140407.txt_

## **Étape 2** – Qu'est-ce que la vulnérabilité **Heartbleed** ?

**Heartbleed** est un bug de sécurité dans la bibliothèque OpenSSL. Il a été introduit en 2012 et divulgué publiquement en avril 2014.

> Le bug Heartbleed permet à quiconque sur Internet de lire la mémoire des systèmes protégés par les versions vulnérables du logiciel OpenSSL. Cela permet aux attaquants d'écouter les communications, de voler des données directement auprès des services et des utilisateurs, et d'usurper l'identité des services et des utilisateurs. – Heartbleed.com

Vous pouvez en apprendre davantage sur Heartbleed sur ce site dédié [ici](https://heartbleed.com/).

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-17.58.12.png)
_https://heartbleed.com/_

Il y a aussi une excellente bande dessinée en ligne de **xkcd**

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-57.png)
_https://xkcd.com/1354/_

## **Étape** 3 – **Visiter la** p**age** W**eb**

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-58.png)
_https://en.wikipedia.org/wiki/Heartbleed_

À partir de la phase de reconnaissance, je décide de commencer par le port 80. Et j'obtiens une page avec une image. Je reconnais le logo Heartbleed sur le côté droit.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-23.12.16.png)

Je regarde le code source. Rien d'intéressant.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-23.14.43.png)

Je décide de lancer **Gobuster**. Gobuster est un scanner de répertoires écrit en Go. Vous pouvez trouver plus d'infos sur l'outil [ici](https://tools.kali.org/web-applications/gobuster).

Gobuster utilise des wordlists sur la machine HTB Parrot qui se trouvent dans le répertoire **/usr/share/wfuzz/wordlist/general/**. J'utilise les wordlists "**big.txt**" et "**megabeast.txt**", mais vous pouvez télécharger plus de wordlists depuis **SecLists** [ici](https://github.com/danielmiessler/SecLists).

J'utilise cette commande pour la wordlist **big.txt** :

```bash
gobuster dir -u 10.129.1.190 -w /usr/share/wfuzz/wordlist/general/big.txt -x php,html,txt
```

Je me concentre également sur les fichiers .php, .txt et .html avec le drapeau **-x** (extensions).

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-23.30.13.png)

J'utilise ensuite cette commande pour la wordlist **megabeast.txt** :

```bash
gobuster dir -u 10.129.1.190 -w /usr/share/wfuzz/wordlist/general/megabeast.txt -x php,html,txt
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-23.30.40.png)

Cela démontre la nécessité de choisir la bonne wordlist ou d'en exécuter au moins deux différentes pour s'assurer de capturer autant d'informations que possible.

Il y a quelques découvertes intéressantes. Je commence par vérifier le dossier **/dev/**.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-23.31.32.png)

Il y a deux fichiers. Je vérifie le contenu du fichier **hype_key**. Il semble s'agir de valeurs hexadécimales.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-23.31.54.png)

L'autre fichier, **notes.txt**, est une liste de tâches.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-23.32.15.png)

Je trouve également un décodeur sur **/decode**.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-23.33.12.png)

et un encodeur sur **/encode**.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-23.33.38.png)

## **Étape** 4 – Décrypter la clé

Je retourne sur mon terminal et je copie/colle le contenu de **hype_key** dans un fichier.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-23.38.58.png)

J'affiche le contenu pour m'assurer d'avoir tout copié correctement avec :

```bash
cat hype.key
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-23.39.32.png)

J'utilise le terminal pour décoder la clé, et plus précisément **xxd**. Plus d'infos sur cette commande [ici](https://www.tutorialspoint.com/unix_commands/xxd.htm). J'utilise la combinaison -r -p pour lire des dumps hexadécimaux bruts sans informations de numéro de ligne et sans mise en page particulière en colonnes.

J'utilise la commande :

```bash
cat hype.key | xxd -r -p
```

La sortie est une **clé RSA chiffrée**. Une clé RSA est une clé privée basée sur l'algorithme RSA. Une clé privée est utilisée pour l'authentification et un échange de clés symétriques lors de l'établissement d'une session SSL/TLS.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-23.44.01.png)

Je capture la sortie dans un nouveau fichier, **hype_key.rsa**, avec :

```bash
cat hype.key | xxd -r -p > hype_key.rsa
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-23.45.08.png)

Mais sans mot de passe, cette clé n'est pas très utile. Voyons si nous pouvons le trouver !

## **Étape** 5 – Trouver un exploit

D'après la phase de reconnaissance sur Nmap et la page web, nous avons découvert que la machine était vulnérable ou avait un lien avec Heartbleed.

J'utilise **Searchsploit** pour vérifier s'il existe un exploit connu. Searchsploit est un outil de recherche en ligne de commande pour la [Exploit Database](https://www.exploit-db.com/).

J'utilise la commande suivante :

```bash
searchsploit heartbleed
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.08.03.png)

Il y a quelques résultats. Je vais choisir le premier. J'obtiens plus de détails sur un exploit avec :

```bash
searchsploit -x 32764.py
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.08.57.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.08.41.png)

Vous pouvez également consulter l'**Exploit Database** pour trouver le même exploit si vous n'êtes pas à l'aise avec la lecture de la documentation sur le terminal.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-18.24.55.png)
_https://www.exploit-db.com/exploits/32764_

J'obtiens plus d'informations avec :

```bash
searchsploit -p 32764.py
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.09.23.png)

Je peux voir où il se trouve sur la machine HTB Parrot. Je copie le fichier dans mon dossier **Valentine** avec :

```bash
cp /usr/share/exploitdb/exploits/multiple/remote/32764.py .
```

et je vérifie s'il a été copié dans ce dossier :

```bash
ls -la
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.09.57.png)

Je renomme le fichier en **heartbleed.py** avec :

```bash
mv 32764.py heartbleed.py
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.10.23.png)

Je lance ensuite l'exploit avec la commande suivante :

```bash
python2 heartbleed.py 10.129.1.190
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.12.26.png)

Il y a beaucoup d'informations, mais en les parcourant et en regardant sur le côté droit, je peux voir une chaîne intéressante :

```bash
$text=aGVhcnRibGVlZGJlbGlldmV0aGVoeXBlCg==
```

C'est du **base 64**. Essayons le décodeur que nous avons trouvé plus tôt sur **/decode**.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.14.28.png)

Je soumets la chaîne et j'obtiens un mot de passe en retour !

```bash
heartbleedbelievethehype
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.14.13.png)

Vous pouvez également le décoder sur votre terminal en utilisant la commande suivante.

```bash
echo aGVhcnRibGVlZGJlbGlldmV0aGVoeXBlCg== | base64 --decode
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.16.32.png)

J'essaie ce mot de passe nouvellement trouvé sur la clé RSA avec :

```bash
openssl rsa -in hype_key.rsa -out hype_key_decrypted.rsa
```

Je saisis le mot de passe lorsqu'on me le demande.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.29.05.png)

D'après la phase de reconnaissance, nous avons trouvé un port 22 ouvert. Connectons-nous en **SSH** à la machine. Je fais une supposition éclairée sur le nom d'utilisateur et je décide de choisir **hype** car j'ai trouvé ce nom sur la clé dans le dossier **/dev**.

Je me connecte en SSH à la machine avec :

```bash
ssh -i hype_key_decrypted.rsa hype@10.129.1.190
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.30.17.png)

Et je suis maintenant connecté en tant qu'utilisateur **hype**.

## **Étape** 6 **- Rechercher le flag user.txt**

Je commence à remonter jusqu'au répertoire /**home**.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.31.09.png)

Je continue dans le répertoire /**hype**.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.31.44.png)

Et je trouve le flag utilisateur ! Je peux vérifier le contenu du fichier avec :

```bash
cat user.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.32.40.png)

## **Étape** 7 **- Rechercher le flag root.txt**

Je retourne à la racine **/**. Je ne peux pas accéder au répertoire /**root**.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.33.13.png)

Je décide de retourner dans le répertoire de hype et je vois que le fichier **.bash_history** n'est pas un fichier de zéro octet.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.33.58.png)

J'affiche son contenu avec :

```bash
cat .bash_history
```

Le shell bash stocke l'historique des commandes que vous avez exécutées dans le fichier d'historique de votre compte utilisateur à ~/.bash_history par défaut.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-22.57.29.png)

Je peux voir quelques commandes avec **tmux**.

> **tmux** est un multiplexeur de terminaux open-source pour les systèmes d'exploitation de type Unix. Il permet d'accéder simultanément à plusieurs sessions de terminal dans une seule fenêtre. Il est utile pour exécuter plus d'un programme en ligne de commande en même temps. Il peut également être utilisé pour détacher des processus de leurs terminaux de contrôle, permettant aux sessions distantes de rester actives sans être visibles. - Wikipedia

Plus d'infos [ici](https://github.com/tmux/tmux/wiki).

Je lance **ps** et je peux voir que la session **tmux** a été lancée en tant qu'utilisateur root :

```bash
ps aux | grep tmux
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.35.00.png)

J'ai lancé la commande pour me connecter à la session, avec les privilèges root complets.

```bash
tmux -S /.devs/dev_sess
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.35.22.png)

Je suis maintenant root !

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.37.31.png)

Je peux naviguer vers le répertoire **root**. Je trouve le fichier root.txt et je vérifie son contenu avec :

```bash
cat root.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-25-at-00.38.50.png)

Félicitations ! Vous avez trouvé les deux flags.

## **Remédiations**

* Mettre à jour vers la dernière version d'OpenSSL
* Remplacer TOUTES les clés et certificats sur les serveurs web pour atténuer les risques d'une brèche de sécurité, et révoquer les anciens
* Appliquer le [principe du moindre privilège](https://en.wikipedia.org/wiki/Principle_of_least_privilege) à tous vos systèmes et services

N'hésitez pas à poser des questions ou à partager avec vos amis :)

Vous pouvez voir d'autres articles de la série **Keep Calm and Hack the Box** [ici](https://www.freecodecamp.org/news/search/?query=keep%20calm%20and%20hack%20the%20box).

Vous pouvez me suivre sur [Twitter](https://twitter.com/SonyaMoisset) ou sur [LinkedIn](https://www.linkedin.com/in/sonyamoisset/).

Et n'oubliez pas de #**GetSecure**, #**BeSecure** & #**StaySecure** !

![Image](https://www.freecodecamp.org/news/content/images/2021/05/vapor-synthwave-retro-city-4k-xu-1.jpeg)