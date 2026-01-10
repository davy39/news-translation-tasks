---
title: Scripts Nmap utiles pour les hackers éthiques
subtitle: Les scripts rendent l'outil Nmap encore plus puissant qu'il ne l'est déjà.
  Apprenons à travailler avec quelques-uns d'entre eux.
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-11-08T14:44:45.812Z'
originalURL: https://freecodecamp.org/news/useful-nmap-scripts-for-ethical-hackers
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1731077044881/75a0f1c6-0aae-4ed6-bcfd-777b2ae2b1b6.jpeg
tags:
- name: nmap
  slug: nmap
- name: Scripting
  slug: scripting
- name: networking
  slug: networking
- name: scanning
  slug: scanning
- name: cybersecurity
  slug: cybersecurity
seo_title: Scripts Nmap utiles pour les hackers éthiques
seo_desc: 'Nmap is short for Network Mapper. It’s an open-source Linux command-line
  tool for scanning IP addresses and ports in a network and detecting installed applications.

  Nmap allows network admins to identify devices running on their network, discover
  ope...'
---

Nmap est l'abréviation de Network Mapper. C'est un outil open-source en ligne de commande Linux pour scanner les adresses IP et les ports d'un réseau et détecter les applications installées.

Nmap permet aux administrateurs réseau d'identifier les appareils fonctionnant sur leur réseau, de découvrir les ports et services ouverts, et de détecter les vulnérabilités.

Voici la syntaxe de base pour utiliser nmap :

```plaintext
nmap <ip/url>
```

Faisons un scan rapide et voyons ce que nous pouvons trouver. Nous pouvons utiliser l'URL [scanme.nmap.org](http://scanme.nmap.org) pour essayer un scan. Nmap nous permet d'utiliser ce serveur pour pratiquer les scans.

![Exemple de scan Nmap](https://miro.medium.com/v2/resize:fit:1050/1*daqo4BGtxBZdWF2TLCxQHw.png align="left")

Comme vous pouvez le voir, nous avons trouvé quelques ports et services ouverts. Ceux-ci servent de points d'entrée pour une analyse ou une exploitation plus approfondie.

Nmap est généralement le premier outil que les hackers éthiques apprennent. [Voici un tutoriel complet si vous souhaitez en savoir plus sur Nmap](https://www.stealthsecurity.sh/p/nmap-tutorial).

## Moteur de script Nmap

Une fonctionnalité clé est le Nmap Scripting Engine (NSE). Il permet aux utilisateurs d'exécuter des scripts pour effectuer des scans réseau détaillés et recueillir des informations spécifiques.

Les scripts vous aident à effectuer une liste d'actions automatiquement au lieu de les effectuer étape par étape.

Ces scripts couvrent une gamme de fonctionnalités, de la détection de services au scan de vulnérabilités. Dans cet article, nous examinerons quelques scripts Nmap utiles.

Je vais vous guider à travers chaque script, expliquer ce qu'il fait et vous montrer comment l'utiliser. À la fin, vous aurez une solide compréhension de l'utilisation de ces scripts en tant que hacker éthique.

> ***Note :*** *Ce tutoriel est conçu pour vous aider à comprendre la sécurité réseau. Le piratage ou même le scan d'un autre serveur sans permission est illégal.*

# **HTTP-Enum**

Imaginez que vous êtes chargé de vérifier la sécurité d'un site web et que vous souhaitez voir s'il existe des pages ou des répertoires cachés. Vous suspectez qu'il pourrait y avoir des panneaux d'administration, des pages de connexion ou des fichiers de test qui ne sont pas liés au site principal.

Trouver ces zones cachées pourrait révéler des faiblesses de sécurité critiques, telles que des pages d'administration non protégées ou des anciens fichiers qui pourraient encore contenir des informations sensibles.

Le script `http-enum` est utilisé pour scanner un serveur web et trouver des répertoires et fichiers courants qui pourraient être cachés de la navigation principale du site.

Pensez à cela comme à l'ouverture de portes dans un bâtiment pour voir ce qu'il y a derrière chacune d'elles. Il recherche des chemins comme des pages de connexion, des panneaux d'administration, des fichiers de configuration et d'autres répertoires qui ne sont généralement pas liés au site web principal.

Par exemple, une page de connexion ou une section d'administration peut exister à des chemins spécifiques mais ne sont pas visibles pour les utilisateurs réguliers. Cette information est utile car connaître ces emplacements peut vous aider à identifier les points faibles de la sécurité.

Voici la commande pour exécuter le script http-enum :

```plaintext
nmap --script http-enum -p 80 <ip-cible>
```

![Exemple de réponse http-enum](https://cdn.hashnode.com/res/hashnode/image/upload/v1730379312717/5e6300c2-0030-4400-b998-e395c0b69a4f.png align="left")

Comme vous pouvez le voir, le résultat de l'exemple ci-dessus montre /login.php, /docs et d'autres chemins d'URL exposés. Ceux-ci peuvent être des points d'entrée pour trouver des informations restreintes sur un serveur web.

# **SMB-OS-Discovery**

Supposons que vous explorez le réseau d'une entreprise pour comprendre quel type de systèmes ils ont en place, spécifiquement dans un environnement Windows.

Connaître le système d'exploitation exact et la version de chaque serveur vous aide à évaluer les vulnérabilités. Par exemple, une ancienne version de Windows pourrait avoir des failles non corrigées qui nécessitent une attention particulière.

Le script `smb-os-discovery` cible les serveurs qui utilisent le protocole SMB, principalement trouvés dans les environnements Windows, pour recueillir des informations sur le système d'exploitation du serveur. Il peut révéler des détails comme la version de Windows, le nom du serveur et son domaine.

Ce script vous aide à comprendre avec quel type de système vous traitez, ce qui est clé pour vérifier les failles de sécurité spécifiques à ce système d'exploitation.

Voici la syntaxe pour exécuter le script smb-os-discovery.

```plaintext
nmap --script smb-os-discovery -p 445 <ip-cible>
```

![Exemple de résultat smb-os-discovery](https://cdn.hashnode.com/res/hashnode/image/upload/v1730444262829/c8f76aee-d0a6-4203-b572-17df1272211c.png align="left")

Comme vous pouvez le voir dans l'exemple de résultat ci-dessus, le script se connecte au service SMB sur la cible et récupère les informations du système d'exploitation. Cela peut vous aider à identifier rapidement la version de Windows et d'autres détails sur le serveur.

# **HTTP-Headers**

Imaginez que vous évaluez la configuration et les paramètres de sécurité d'un site web. Vous voulez savoir quel type de serveur il utilise, quelles méthodes sont autorisées et s'il impose des connexions HTTPS.

Ces détails vous donnent un aperçu de la configuration du serveur et de son alignement avec les meilleures pratiques, vous aidant à repérer les paramètres de sécurité manquants.

Le script `http-headers` vérifie les en-têtes envoyés par un serveur web lorsqu'un utilisateur s'y connecte. Les en-têtes vous indiquent le type de serveur (comme Apache ou NGINX), les paramètres de sécurité (comme les exigences HTTPS), les méthodes autorisées et les règles de mise en cache.

Ces détails sont comme le plan de communication du serveur, révélant souvent si le serveur a certaines protections activées.

Voici la syntaxe pour exécuter le script http-headers :

```plaintext
nmap --script http-headers -p 80 <ip-cible>
```

![Exemple de réponse http-headers](https://cdn.hashnode.com/res/hashnode/image/upload/v1730380306638/703870e4-de5b-4858-b1b2-20634a8598a9.png align="left")

Vous pouvez voir que la réponse de l'exemple montre des en-têtes comme `X-Powered-By`, `Set-Cookie`, et ainsi de suite. Ces en-têtes peuvent aider à trouver des problèmes de sécurité tels que le cross-site scripting (XSS) et le clickjacking.

# **SSH-Brute**

Disons que vous testez les défenses d'un serveur contre les accès non autorisés via SSH. Vous savez que les mots de passe faibles sont un risque courant, donc vous avez besoin d'un moyen de vérifier si des comptes ont des identifiants facilement devinables.

Ce test vous aidera à identifier les connexions SSH faibles qui nécessitent des mots de passe plus forts pour protéger le serveur.

Le script `ssh-brute` tente de se connecter à un serveur SSH en devinant des noms d'utilisateur et des mots de passe. SSH, ou Secure Shell, est souvent utilisé pour les connexions à distance.

Si les noms d'utilisateur et les mots de passe sont faciles à deviner, ce script pourrait trouver un moyen d'entrer. C'est un test utile pour voir si les identifiants de connexion sont suffisamment forts pour empêcher les accès non autorisés.

Voici la syntaxe pour exécuter le script ssh-brute :

```plaintext
nmap --script ssh-brute -p 22 <ip-cible>
```

![Exemple de réponse ssh-brute](https://cdn.hashnode.com/res/hashnode/image/upload/v1730811335746/c6f6ad27-37d7-467d-8f5c-cd71a37aff0f.jpeg align="left")

Comme vous pouvez le voir, ce script essaie différentes combinaisons nom d'utilisateur-mot de passe sur le serveur SSH. En cas de succès, il affichera les identifiants corrects.

# **DNS-Brute**

Imaginez que vous cartographiez le réseau d'une entreprise et que vous souhaitez voir s'ils ont des sous-domaines qui ne sont pas listés publiquement. Chaque sous-domaine peut servir un objectif différent, comme l'hébergement de serveurs de messagerie ou de sites de test internes.

Découvrir ces sous-domaines vous aide à vérifier si l'un d'eux expose des services sensibles.

Le script `dns-brute` vous aide à trouver des sous-domaines associés à un domaine donné en essayant des noms courants, comme "www", "mail" ou "ftp". Les sous-domaines peuvent héberger des services et applications séparés, chacun avec son propre ensemble de vulnérabilités.

Voici la syntaxe pour exécuter le script dns-brute :

```plaintext
nmap --script dns-brute <domaine-cible>
```

![Script dns-brute](https://cdn.hashnode.com/res/hashnode/image/upload/v1730379500675/c8c646c3-1d76-440a-8092-6ce26f9aa127.png align="left")

Comme vous pouvez le voir, le script tente de résoudre une liste de sous-domaines courants et en trouve un nom d'hôte interne. L'utilisation de ce script peut révéler des sous-domaines qui ne sont pas listés dans les enregistrements publics, vous aidant à obtenir une image plus complète de la structure du réseau d'une organisation.

# **Conclusion**

Ces scripts Nmap fournissent un moyen puissant d'auditer, de dépanner et de sécuriser les réseaux. En comprenant ce que fait chaque script et comment l'utiliser, vous serez en mesure de découvrir des problèmes cachés et de protéger votre infrastructure.

**Pour apprendre à construire une carrière dans la cybersécurité, consultez** [***The Hacker's Handbook***](https://book.stealthsecurity.sh/?utm_source=www.stealthsecurity.sh&utm_medium=newsletter&utm_campaign=top-cybersecurity-certifications-you-should-know-about)**. Pour pratiquer le piratage de systèmes réels et obtenir de l'aide d'autres hackers, rejoignez** [***The Hackers Hub***](https://www.skool.com/hackershub?utm_source=www.stealthsecurity.sh&utm_medium=newsletter&utm_campaign=top-cybersecurity-certifications-you-should-know-about)**.**