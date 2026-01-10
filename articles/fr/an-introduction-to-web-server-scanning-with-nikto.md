---
title: Analyse de serveur web avec Nikto – Un guide pour débutants
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2021-07-14T07:18:59.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-web-server-scanning-with-nikto
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Nikto.png
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: penetration testing
  slug: penetration-testing
- name: Security
  slug: security
seo_title: Analyse de serveur web avec Nikto – Un guide pour débutants
seo_desc: 'Websites are a critical part of almost every business or organization in
  the world. From your nearby florist to global brands, almost everyone uses a website
  as part of their branding.

  Unfortunately, websites are also one of the most unsecured gatewa...'
---

Les sites web sont une partie critique de presque toutes les entreprises ou organisations dans le monde. Du fleuriste local aux marques mondiales, presque tout le monde utilise un site web comme partie intégrante de leur image de marque.

Malheureusement, les sites web sont également l'une des passerelles les moins sécurisées par lesquelles un attaquant peut exploiter votre entreprise.

Étant donné que la plupart des sites web ne sont pas soutenus par des équipes techniques solides, il est important de comprendre la sécurité des sites web et des applications web pour protéger votre organisation.

## Présentation de Nikto

Nikto est un scanner de serveur web et d'applications web open source. Nikto peut effectuer des tests complets contre les serveurs web pour plusieurs menaces de sécurité, y compris plus de 6700 fichiers/programmes potentiellement dangereux. Nikto peut également effectuer des vérifications pour les logiciels de serveurs web obsolètes et les problèmes spécifiques à certaines versions.

Nikto a été écrit et maintenu par Sullo, CIRT, Inc. Il est écrit en Perl et a été initialement publié à la fin de l'année 2001.

Il est actuellement maintenu par David Lodge ([vous pouvez trouver son blog ici](https://tautology.org.uk/blog/)), bien que d'autres contributeurs aient été impliqués dans le projet.

**Voici quelques-unes des choses intéressantes que Nikto peut faire :**

* Trouver des injections SQL, XSS et autres vulnérabilités courantes

* Identifier les logiciels installés (via les en-têtes, favicons et fichiers)

* Deviner les sous-domaines

* Inclut le support pour les sites SSL (HTTPS)

* Enregistre les rapports en texte brut, XML, HTML ou CSV

* "Pêcher" du contenu sur les serveurs web

* Signaler les en-têtes inhabituels

* Vérifier les éléments de configuration du serveur comme les multiples fichiers index, les options du serveur HTTP, etc.

* Dispose d'un support complet pour les proxys HTTP

* Deviner les identifiants pour l'autorisation (y compris de nombreuses combinaisons nom d'utilisateur/mot de passe par défaut)

* Est configuré avec un moteur de template pour personnaliser facilement les rapports

* Exporte vers Metasploit

## Comment installer Nikto

Puisque Nikto est un programme basé sur Perl, il peut fonctionner sur la plupart des systèmes d'exploitation avec l'interpréteur Perl nécessaire installé.

Si vous utilisez Kali Linux, Nikto est préinstallé et sera présent dans la catégorie "Analyse de vulnérabilités".

Si vous n'avez pas Nikto sur Kali (pour une raison quelconque), vous pouvez obtenir Nikto depuis [GitHub](https://github.com/sullo/nikto) ou simplement utiliser la commande "apt install nikto".

Pour installer Nikto sur Windows, vous devez d'abord installer l'interpréteur Perl. Il peut être téléchargé ici : [[https://www.activestate.com/activeperl](https://www.activestate.com/products/perl/)](null)

Pour MacOS, vous pouvez utiliser homebrew.

[Les instructions complètes d'installation pour toutes les plateformes peuvent être trouvées ici](https://github.com/sullo/nikto/wiki).

## Comment scanner avec Nikto

Maintenant que vous savez ce qu'est Nikto et comment l'installer, passons à l'exécution de quelques scans.

> Avertissement :
>
> Avant de commencer le scan, je veux souligner que je ne suis pas responsable des dommages que vous pourriez causer en tentant d'attaquer des systèmes. C'est illégal.
>
> Vous devez avoir une autorisation écrite avant d'essayer de scanner un système ou un réseau.

Puisque Nikto est un outil en ligne de commande, vous pouvez utiliser la commande d'aide pour obtenir une liste des options :

```javascript
> nikto -Help
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-63.png align="left")

### Comment scanner un domaine

Pour effectuer un scan de domaine simple, utilisez le flag `-h` (hôte) :

```javascript
> nikto -h scanme.nmap.org
```

Nikto effectuera un scan de base sur le port 80 pour le domaine donné et vous fournira un rapport complet basé sur les scans effectués :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-66.png align="left")

*Scan de domaine Nikto*

### Comment scanner un domaine avec SSL activé

Pour les domaines avec HTTPS activé, vous devez spécifier le flag `-ssl` pour scanner le port 443 :

```javascript
> nikto -h https://nmap.org -ssl
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-67.png align="left")

*Scan Nikto avec SSL activé*

### Comment scanner une adresse IP

Parfois, vous voulez simplement scanner une adresse IP où un serveur web est hébergé.

Pour ce faire, utilisez le même flag `-h` que vous avez utilisé pour le scan de domaine :

```javascript
> nikto -h 45.33.32.156
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-68.png align="left")

*Scan d'adresse IP Nikto*

### Comment scanner plusieurs adresses IP à partir d'un fichier texte

Pour scanner plusieurs adresses IP ou domaines, il suffit de les mettre dans un fichier texte séparés par des sauts de ligne. Nikto saura que le scan doit être effectué sur chaque domaine/adresse IP.

Supposons que nous avons un fichier nommé domains.txt avec deux noms de domaine :

* scanme.nmap.org

* nmap.org.

Pour scanner les deux avec Nikto, exécutez la commande suivante :

```javascript
> nikto -h domains.txt
```

Nikto commencera à scanner les domaines l'un après l'autre :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-69.png align="left")

*Scan multi-domaines Nikto*

### Comment exporter les résultats du scan

Les scans Nikto prennent un certain temps à se terminer. Lorsque vous êtes un testeur de pénétration professionnel, vous ne voulez pas répéter les scans très souvent sauf s'il y a des changements majeurs dans l'application web.

Pour exporter un résultat de scan, utilisez le flag `-o` suivi du nom du fichier :

```javascript
> nikto -h scanme.nmap.org -o scan.txt
```

Vous pouvez également utiliser le flag `-Format` pour spécifier un format de sortie. Vous pouvez choisir parmi CSV, HTML, nbe (format [Nessus](https://www.cs.cmu.edu/~dwendlan/personal/nessus.html)), SQL, txt et XML :

```javascript
> nikto -h scanme.nmap.org -o scan.csv -Format csv
```

![Image](https://www.freecodecamp.org/news/content/images/2021/07/image-65.png align="left")

*Formats de sortie Nikto*

## **Comment associer Nikto avec Metasploit**

Metasploit est un framework puissant qui vous permet de tout faire, de la numérisation à l'exploitation des systèmes. Les testeurs de pénétration professionnels utilisent Metasploit presque tous les jours. J'ai écrit un article sur Metasploit récemment que [vous pouvez trouver ici](https://www.freecodecamp.org/news/learn-metasploit-for-beginners/).

Nikto offre un moyen d'exporter les scans vers Metasploit afin de faciliter l'exploitation des systèmes basée sur les résultats des scans de Nikto.

Pour ce faire, ajoutez le flag `-Format msf+` à la fin d'un scan :

```javascript
$ nikto -h <domaine/ip> -Format msf+
```

## **Alternatives à Nikto**

Il est toujours bon d'avoir un outil de secours dans votre arsenal de test de pénétration. Certaines des meilleures alternatives à Nikto sont :

* [**Arachni**](https://www.arachni-scanner.com/) : Un framework Ruby open source, modulaire et haute performance, axé sur l'évaluation de la sécurité des applications web.

* [**OWASP Zed Attack Proxy (ZAP)**](https://www.zaproxy.org/) : Un outil de test de pénétration intégré qui fournit des scanners automatisés ainsi qu'un ensemble d'outils permettant de trouver des vulnérabilités de sécurité manuellement.

* [**Skipfish**](https://tools.kali.org/web-applications/skipfish) : Un outil de reconnaissance de sécurité des applications web entièrement automatisé et actif. Écrit en C pour être rapide, avec une gestion HTTP hautement optimisée et une empreinte CPU minimale, atteignant facilement 2000 requêtes par seconde avec des cibles réactives.

## TLDR;

Nikto est un scanner open source qui vous aide à trouver des menaces de sécurité potentielles dans vos sites web et applications web.

Il automatise entièrement la numérisation des vulnérabilités et peut trouver des problèmes comme les mauvaises configurations de service, les fichiers/programmes non sécurisés et des milliers d'autres problèmes de sécurité.

Les bonnes alternatives incluent Arachini, OWASP ZAP et Skipfish.

## Références

* [https://cirt.net/Nikto2](https://cirt.net/Nikto2)

* [https://github.com/sullo/nikto](https://github.com/sullo/nikto)

* [https://linuxhint.com/scanning_vulnerabilities_nikto/](https://linuxhint.com/scanning_vulnerabilities_nikto/)

Vous avez aimé cet article ? [**Rejoignez ma newsletter**](http://tinyletter.com/manishmshiva) et recevez un résumé de mes articles et vidéos chaque lundi matin. Vous pouvez également [**visiter mon site web ici**](https://www.manishmshiva.com/).