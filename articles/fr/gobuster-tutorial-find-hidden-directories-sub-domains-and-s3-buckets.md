---
title: Tutoriel Gobuster – Comment trouver des répertoires cachés, des sous-domaines
  et des compartiments S3
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2022-12-05T23:40:58.000Z'
originalURL: https://freecodecamp.org/news/gobuster-tutorial-find-hidden-directories-sub-domains-and-s3-buckets
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/Stealth-Security
seo_title: Tutoriel Gobuster – Comment trouver des répertoires cachés, des sous-domaines
  et des compartiments S3
---

Blog-Banner--25-.png
tags:
- name: Sécurité des applications
  slug: application-security
- name: cybersécurité
  slug: cybersecurity
- name: sécurité de l'information
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: Sécurité
  slug: security
seo_title: null
seo_desc: 'Il y a beaucoup plus à découvrir sur les serveurs web et les sites web que ce qui apparaît en surface.

La première étape qu'un attaquant utilise pour attaquer un site web est de trouver la liste des URL et des sous-domaines. Les développeurs web exposent souvent des fichiers sensibles, des chemins d'URL, ou même des sous-domaines lors de la construction ou de la maintenance d'un site.

Ceci est un excellent vecteur d'attaque pour les acteurs malveillants.

Par exemple, si vous avez un site web de commerce électronique, vous pourriez avoir un sous-domaine appelé « admin ». Celui-ci pourrait ne pas être lié quelque part sur le site, mais comme le mot-clé « admin » est courant, l'URL est très facile à trouver. C'est pourquoi vous devez souvent scanner vos sites web pour vérifier les actifs non protégés.

L'approche habituelle consiste à s'appuyer sur des sites d'énumération passive comme [crt.sh](http://crt.sh/) pour trouver des sous-domaines. Mais ces approches passives sont très limitées et peuvent souvent manquer des vecteurs d'attaque critiques.

Gobuster est un outil qui vous aide à effectuer un scanning actif sur les sites web et les applications. Les attaquants l'utilisent pour trouver des vecteurs d'attaque et nous pouvons l'utiliser pour nous défendre.

Dans cet article, nous apprendrons à installer et à travailler avec Gobuster. Nous examinerons également les options fournies par Gobuster en détail. Enfin, nous apprendrons comment nous défendre contre ces types d'attaques par force brute.

Note : **Tous mes articles sont à des fins éducatives.** Si vous utilisez ces informations de manière illégale et que vous avez des problèmes, je ne suis pas responsable. Obtenez toujours la permission du propriétaire avant de scanner / forcer / exploiter un système.

## **Qu'est-ce que Gobuster ?**

Écrit en langage [Go](https://go.dev/), Gobuster est un scanner agressif qui vous aide à trouver des répertoires cachés, des URL, des sous-domaines et des compartiments S3 de manière transparente.

C'est là que les gens demandent : [Et Ffuf](https://blog.stealthsecurity.io/fuzzing-web-applications-using-ffuf-c4ad74190b72) ?

Ffuf est un merveilleux fuzzer web, mais Gobuster est une alternative plus rapide et plus flexible. Gobuster dispose également d'un support pour les extensions avec lesquelles nous pouvons amplifier ses capacités. Gobuster peut également évoluer en utilisant plusieurs threads et effectuer des scans parallèles pour accélérer les résultats.

## **Comment installer Gobuster**

Voyons comment installer Gobuster. Si vous utilisez Kali ou Parrot OS, Gobuster sera préinstallé.

Si vous utilisez Ubuntu ou un OS basé sur Debian, vous pouvez utiliser `apt` pour installer Gobuster.

```
$ apt install gobuster
```

Pour installer Gobuster sur Mac, vous pouvez utiliser Homebrew.

```
$ brew install gobuster
```

Pour installer Gobuster sur Windows et d'autres versions de Linux, vous pouvez trouver les [instructions d'installation ici](https://github.com/OJ/gobuster).

Une fois que vous avez terminé l'installation, vous pouvez vérifier votre installation en utilisant la commande d'aide.

```
$ gobuster -h 
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-1.png)
_Commande d'aide de Gobuster_

## **Qu'est-ce que les listes de mots ?**

Si vous êtes nouveau dans les listes de mots, une liste de mots est une liste de termes couramment utilisés. Cela peut être une [liste de mots de passe](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt), une [liste de noms d'utilisateur](https://github.com/danielmiessler/SecLists/blob/master/Usernames/Names/names.txt), une liste de sous-domaines, etc. Vous pouvez trouver beaucoup de [listes de mots utiles ici](https://github.com/danielmiessler/SecLists).

Je vous recommande de télécharger [Seclists](https://github.com/danielmiessler/SecLists). Seclists est une collection de plusieurs types de listes utilisées lors des évaluations de sécurité. Cela inclut les noms d'utilisateur, les mots de passe, les URL, etc. Si vous utilisez Kali Linux, vous pouvez trouver seclists sous /usr/share/wordlists.

Pour essayer Gobuster en temps réel, vous pouvez soit utiliser votre propre site web, soit utiliser une application web de pratique comme [Damn Vulnerable Web App](https://github.com/digininja/DVWA) (DVWA). DVWA est une application web vulnérable intentionnellement mal configurée qui est utilisée par les testeurs d'intrusion pour pratiquer les attaques d'applications web.

## **Comment travailler avec Gobuster**

Maintenant que nous avons installé Gobuster et les listes de mots requises, commençons à utiliser Gobuster.

Note : J'ai DWVA en cours d'exécution à l'adresse 10.10.171.247 au port 80, donc je vais l'utiliser pour les exemples. Remplacez simplement cela par l'URL ou l'adresse IP de votre site web. J'utiliserai également Kali Linux comme machine d'attaque.

Si vous regardez la commande d'aide, nous pouvons voir que Gobuster a quelques modes.

1. dir — Mode d'énumération de répertoire.
2. dns — Mode d'énumération de sous-domaine.
3. fuzz — Mode de fuzzing.
4. s3 — Mode d'énumération S3.
5. vhost — Mode d'énumération de vhost.

Dans cet article, nous examinerons trois modes : les modes dir, dns et s3.

Chaque mode sert un objectif unique et nous aide à forcer et à trouver ce que nous cherchons. Examinons les trois modes en détail.

### Comment utiliser le mode répertoire (dir)

Le mode répertoire de Gobuster nous aide à rechercher des fichiers cachés et des chemins d'URL. Cela peut inclure des images, des fichiers de script et presque tous les fichiers exposés sur Internet.

Voici la commande pour exécuter le mode dir :

```
$ gobuster dir -u <url> -w <wordlist>
```

Nous pouvons également utiliser le mode d'aide pour trouver les drapeaux supplémentaires que Gobuster fournit avec le mode dir.

```
$ gobuster dir -h
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-2.png)
_Aide du mode dir de Gobuster_

Essayons maintenant le mode dir. Voici la commande pour rechercher des URL avec la liste de mots commune.

```
$ gobuster dir -u 10.10.171.247:80 -w /usr/share/wordlists/dirb/common.txt
```

Et voici le résultat. Nous pouvons voir qu'il y a certains fichiers exposés dans le site web DVWA.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-3.png)
_Résultats de l'énumération de répertoire_

Si nous voulons rechercher uniquement des extensions de fichiers spécifiques, nous pouvons utiliser le drapeau -x. Voici une commande d'exemple pour filtrer les images :

```
$ gobuster dir -u 10.10.171.247:80 -w /usr/share/wordlists/dirb/common.txt -x jpg,png,jpeg
```

### Comment utiliser le mode DNS (dns)

Vous pouvez utiliser le mode DNS pour trouver des sous-domaines cachés dans un domaine cible. Par exemple, si vous avez un domaine nommé mydomain.com, des sous-domaines comme admin.mydomain.com, support.mydomain.com, etc., peuvent être trouvés en utilisant Gobuster.

Commençons par regarder la commande d'aide pour le mode dns.

```
$ gobuster dns -h
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-4.png)
_Aide DNS de Gobuster_

Pour exécuter une énumération DNS, nous pouvons utiliser la commande suivante :

```
$ gobuster dns -d mydomain.com -w /usr/share/wordlists/dirb/common.txt
```

Puisque nous ne pouvons pas énumérer les adresses IP pour les sous-domaines, nous devons exécuter ce scan uniquement sur les sites web que nous possédons ou ceux pour lesquels nous avons la permission de scanner.

```
$ gobuster s3 -h
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-5.png)
_Aide du mode S3 de Gobuster_

Le mode S3 a été récemment ajouté à Gobuster et est un excellent outil pour découvrir des compartiments S3 publics. Puisque les compartiments S3 ont des noms uniques, ils peuvent être énumérés en utilisant une liste de mots spécifique.

Par exemple, si nous avons une entreprise nommée Acme, nous pouvons utiliser une liste de mots avec acme-admin, acme-user, acme-images, etc. Cette liste de mots peut ensuite être alimentée dans Gobuster pour trouver s'il y a des compartiments publics correspondant aux noms de compartiments dans la liste de mots.

Voici la commande pour exécuter une énumération S3 en utilisant Gobuster :

```
$ gobuster s3 -w bucket_list.txt
```

## **Comment se défendre contre Gobuster**

Gobuster est un outil remarquable que vous pouvez utiliser pour trouver des répertoires cachés, des URL, des sous-domaines et des compartiments S3.

Mais cela permet également aux pirates malveillants de l'utiliser et d'attaquer vos actifs d'application web. Alors, comment nous défendons-nous contre Gobuster ?

Vous pouvez utiliser les étapes suivantes pour prévenir et arrêter les attaques par force brute sur votre application web.

1. **Auditez-vous vous-même :** Utilisez Gobuster sur vos propres applications et effectuez un audit. Cela vous aidera à trouver les informations qui seront visibles pour les attaquants.
2. **Appliquez des politiques de sécurité :** Pour empêcher les ressources comme S3 d'être exposées sur Internet, utilisez des politiques de compartiment AWS pour empêcher l'accès non autorisé.
3. **Utilisez des solutions de protection contre les bots :** Les services de protection contre les bots comme Cloudflare arrêteront toute attaque par force brute, rendant incroyablement difficile l'attaque de votre application web.

## **Conclusion**

Gobuster est un outil rapide de force brute pour découvrir des URL cachées, des fichiers et des répertoires au sein des sites web. Cela nous aidera à supprimer/sécuriser les fichiers cachés et les données sensibles.

Gobuster aide également à sécuriser les sous-domaines et les hôtes virtuels pour qu'ils ne soient pas exposés sur Internet. Dans l'ensemble, Gobuster est un outil fantastique pour vous aider à réduire la surface d'attaque de votre application.

_Aimez cet article ? Rejoignez le_ [Newsletter hebdomadaire Stealth Security](https://tinyletter.com/stealthsecurity) _et recevez des articles livrés dans votre boîte de réception chaque vendredi. Vous pouvez également_ [me contacter](https://www.linkedin.com/in/manishmshiva/) _sur LinkedIn._