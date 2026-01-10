---
title: 10 Outils que tout ingénieur en cybersécurité devrait connaître
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-08-06T21:27:46.000Z'
originalURL: https://freecodecamp.org/news/10-tools-you-should-know-as-a-cybersecurity-engineer
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/wall.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
- name: penetration testing
  slug: penetration-testing
- name: Security
  slug: security
seo_title: 10 Outils que tout ingénieur en cybersécurité devrait connaître
seo_desc: "If you're a penetration tester, there are numerous tools you can use to\
  \ help you accomplish your goals. \nFrom scanning to post-exploitation, here are\
  \ ten tools you must know if you are into cybersecurity.\nWhat is Cybersecurity?\n\
  Being a cybersecurity ..."
---

Si vous êtes un testeur d'intrusion, il existe de nombreux outils que vous pouvez utiliser pour vous aider à atteindre vos objectifs. 

De l'analyse à la post-exploitation, voici dix outils que vous devez connaître si vous vous intéressez à la cybersécurité.

## Qu'est-ce que la cybersécurité ?

Être ingénieur en cybersécurité signifie être responsable d'un réseau entier. Ce réseau comprend des ordinateurs, des routeurs, des téléphones mobiles et tout ce qui se connecte à Internet.

Grâce à l'essor de l'[Internet des objets](https://en.wikipedia.org/wiki/Internet_of_things), nous voyons de plus en plus d'appareils se connecter à Internet chaque jour. Des services comme [Shodan](https://www.shodan.io/) prouvent à quel point il est dangereux d'avoir un appareil connecté à Internet sans sécurité adéquate.

Nous ne pouvons pas non plus compter sur les logiciels antivirus, étant donné la sophistication des pirates informatiques d'aujourd'hui. De plus, la plupart des attaques utilisent aujourd'hui l'[ingénierie sociale](https://www.csoonline.com/article/2124681/what-is-social-engineering.html) comme point d'entrée. Cela rend encore plus difficile pour les professionnels de la cybersécurité de détecter et de mitiger ces attaques.

La Covid-19 est devenue un autre catalyseur majeur pour la croissance des cyberattaques. Les employés travaillant à domicile n'ont pas accès aux mêmes architectures de sécurité de niveau entreprise que sur leur lieu de travail. 

Le nombre croissant de cyberattaques a également augmenté la demande de professionnels de la cybersécurité dans le monde. En raison de cette demande croissante, la cybersécurité a attiré de nombreux experts ainsi que des débutants.

Pour ceux d'entre vous qui sont nouveaux dans le domaine de la cybersécurité, le piratage n'est pas aussi cool qu'il en a l'air à la télévision. Et il y a une forte probabilité que vous finissiez en prison. 

Cependant, être un testeur d'intrusion ou un pirate informatique "white hat" est différent – et bénéfique – car vous utiliserez les mêmes outils que les pirates "black hat" (les méchants). Sauf que cette fois, c'est légal, et votre objectif est d'aider les entreprises à découvrir les vulnérabilités de sécurité afin qu'elles puissent les corriger. 

Vous pouvez [en apprendre davantage sur les types de pirates ici](https://www.tutorialspoint.com/ethical_hacking/ethical_hacking_hacker_types.htm).

Il est toujours difficile de trouver les bons outils pour commencer dans n'importe quel domaine, surtout si vous êtes débutant. Voici donc 10 outils pour vous aider à commencer en tant qu'ingénieur en cybersécurité.

## Top des outils pour les ingénieurs en cybersécurité débutants

### Wireshark

![Image](https://www.freecodecamp.org/news/content/images/2020/08/wireshark.png)

Avoir une solide base en réseau est essentiel pour devenir un bon testeur d'intrusion. Après tout, Internet est un ensemble de réseaux complexes qui communiquent entre eux. Si vous êtes nouveau dans le domaine des réseaux, je recommande [cette playlist de Network Direction](https://www.youtube.com/watch?v=cNwEVYkx2Kk&list=PLDQaRcbiSnqF5U8ffMgZzS7fq1rHUI3Q8).

Wireshark est le meilleur outil d'analyse de réseau au monde. C'est un logiciel open-source qui vous permet d'inspecter des données en temps réel sur un réseau actif.

Wireshark peut disséquer des paquets de données en trames et segments, vous donnant des informations détaillées sur les bits et les octets dans un paquet. 

Wireshark prend en charge tous les principaux protocoles réseau et types de médias. Wireshark peut également être utilisé comme outil de sniffing de paquets si vous êtes sur un réseau public. Wireshark aura accès à l'ensemble du réseau connecté à un routeur.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/wireshark2.png)
_Interface utilisateur de Wireshark_

Des sites comme Facebook et Twitter sont maintenant chiffrés, grâce à HTTPS. Cela signifie que même si vous pouvez capturer des paquets d'une machine victime en transit vers Facebook, ces paquets seront chiffrés. 

Cependant, pouvoir capturer des paquets de données en temps réel est une utilité importante pour un testeur d'intrusion.

### Nmap

![Image](https://www.freecodecamp.org/news/content/images/2020/08/nmap.png)

Nmap est le premier outil que vous rencontrerez lorsque vous commencerez votre carrière en tant que testeur d'intrusion. C'est un excellent outil d'analyse de réseau qui peut vous donner des informations détaillées sur une cible. Cela inclut les ports ouverts, les services et le système d'exploitation en cours d'exécution sur l'ordinateur de la victime.

Nmap est populaire parmi les testeurs d'intrusion pour de nombreuses raisons. Il est simple, flexible et extensible. Il offre une interface en ligne de commande simple où vous pouvez ajouter quelques indicateurs pour choisir différents types d'analyses. 

Nmap offre également des analyses de ping simples jusqu'à des analyses agressives qui fournissent des informations détaillées sur les ports et les services.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/zenmap.png)
_Interface utilisateur de Zenmap_

Nmap fournit également un outil GUI appelé Zenmap avec des utilitaires ajoutés. Vous pouvez construire des cartes de réseau visuelles et choisir des analyses via des menus déroulants. Zenmap est un excellent point de départ pour jouer avec les commandes Nmap si vous êtes débutant.

J'ai récemment écrit un article détaillé sur Nmap que [vous pouvez lire ici](https://medium.com/manishmshiva/nmap-a-guide-to-the-greatest-scanning-tool-of-all-time-3bd1a973a5e5).

### Ncat (anciennement Netcat)

![Image](https://www.freecodecamp.org/news/content/images/2020/08/netcat.jpg)

Netcat est souvent appelé le couteau suisse du réseau.

Netcat est un outil simple mais puissant qui peut afficher et enregistrer des données sur des connexions réseau TCP ou UDP. Netcat fonctionne comme un écouteur back-end qui permet l'analyse des ports et l'écoute des ports.

Vous pouvez également transférer des fichiers via Netcat ou l'utiliser comme une [porte dérobée vers votre machine victime](https://en.wikipedia.org/wiki/Backdoor_%28computing%29). Cela en fait un outil populaire de post-exploitation pour établir des connexions après des attaques réussies. Netcat est également extensible grâce à sa capacité à ajouter des scripts pour des tâches plus grandes ou redondantes.

Malgré la popularité de Netcat, il n'était pas activement maintenu par sa communauté. L'équipe Nmap a développé une version mise à jour de Netcat appelée [Ncat](https://nmap.org/ncat/) avec des fonctionnalités incluant le support pour SSL, IPv6, SOCKS et les proxys HTTP.

### Metasploit

![Image](https://www.freecodecamp.org/news/content/images/2020/08/metasploit-.jpg)

S'il y a un outil que j'adore, c'est Metasploit. Metasploit n'est pas seulement un outil, mais un framework complet que vous pouvez utiliser pendant tout le cycle de vie d'un test d'intrusion.

Metasploit contient des exploits pour la plupart des vulnérabilités dans la base de données [Common Vulnerabilities and Exposure](https://cve.mitre.org/). En utilisant Metasploit, vous pouvez envoyer des charges utiles à un système cible et y accéder via une interface de ligne de commande.

Metasploit est très avancé avec la capacité d'effectuer des tâches telles que l'analyse des ports, l'énumération et le scripting en plus de l'exploitation. Vous pouvez également construire et tester votre propre exploit en utilisant le langage de programmation Ruby.

Metasploit était open-source jusqu'en 2009, date à laquelle Rapid7 a acquis le produit. Vous pouvez toujours accéder à l'édition communautaire gratuite et utiliser toutes ses fonctionnalités.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/armitage.jpg)
_Interface utilisateur d'Armitage_

Metasploit était autrefois un outil purement en ligne de commande. Une interface graphique basée sur Java appelée Armitage a été publiée en 2013.

### Nikto

![Image](https://www.freecodecamp.org/news/content/images/2020/08/nikto.jpeg)

Nikto est un outil open-source capable de réaliser des analyses approfondies des serveurs web. Nikto peut vous aider à analyser les fichiers nuisibles, les mauvaises configurations, les installations de logiciels obsolètes, et ainsi de suite.

Il vérifie également la présence de plusieurs fichiers d'index, les configurations du serveur HTTP et le logiciel de serveur web installé.

Nikto est l'outil préféré pour les audits de sécurité généraux des serveurs web. Nikto est rapide, mais pas silencieux. Vous pouvez analyser un grand serveur web assez rapidement, mais les systèmes de détection d'intrusion repéreront facilement ces analyses. Cependant, il existe un support pour les plugins anti-IDS au cas où vous souhaiteriez effectuer des analyses furtives.

### Burp Suite

![Image](https://www.freecodecamp.org/news/content/images/2020/08/burpsuite.png)

En matière de tests d'intrusion des applications web, Burp Suite a toutes les réponses pour vous. Burp Suite vise à être un ensemble complet d'outils pour divers cas d'utilisation de tests d'intrusion des applications web. C'est également un outil populaire parmi les chercheurs en sécurité des applications web professionnelles et les chasseurs de primes de bogues.

Les outils de Burp Suite fonctionnent ensemble pour soutenir l'ensemble du cycle de vie des tests d'applications web. De l'analyse à l'exploitation, Burp Suite offre tous les outils dont vous avez besoin pour pénétrer les applications web.

L'une des principales caractéristiques de Burp Suite est sa capacité à intercepter les requêtes HTTP. Les requêtes HTTP vont généralement de votre navigateur à un serveur web, puis le serveur web envoie une réponse. Avec Burp Suite, vous pouvez effectuer des opérations de type "Man-in-the-middle" pour manipuler la requête et la réponse.

Burp Suite dispose d'une excellente interface utilisateur. Burp Suite dispose également d'outils d'automatisation pour rendre votre travail plus rapide et plus efficace.

En plus de ses fonctionnalités par défaut, Burp Suite est extensible en ajoutant des plugins appelés BApps.

### John the Ripper

![Image](https://www.freecodecamp.org/news/content/images/2020/08/john.png)

Les mots de passe sont toujours la norme de facto de l'authentification dans la plupart des systèmes. Même si vous parvenez à accéder à un serveur ou à une base de données, vous devrez déchiffrer le mot de passe pour obtenir une [élévation de privilèges](https://searchsecurity.techtarget.com/definition/privilege-escalation-attack).

John the Ripper est un outil simple utilisé pour craquer les mots de passe. C'est un craqueur de mots de passe ultra-rapide avec support pour des listes de mots personnalisées. Il peut fonctionner contre la plupart des types de méthodes de chiffrement comme MD5 et SHA.

### Aircrack-ng

![Image](https://www.freecodecamp.org/news/content/images/2020/08/aircrack.png)

Aircrack-ng est un ensemble d'outils qui vous aident à travailler avec des réseaux sans fil. Aircrack comprend des outils qui peuvent capturer des réseaux sans fil, craquer des clés WPA, injecter des paquets, et ainsi de suite.

Quelques outils de la suite Aircrack-ng incluent :

* airodump – Capture des paquets
* aireplay – Injection de paquets
* aircrack – Craquage de WEP et WPA
* airdecap – Déchiffrement de WEP et WPA

Aircrack contient d'excellents algorithmes pour craquer les mots de passe WiFi et capturer le trafic sans fil. Il peut également déchiffrer les paquets chiffrés, ce qui en fait une suite complète d'outils pour les tests d'intrusion sans fil. 

En bref, vous pouvez utiliser Aircrack pour surveiller, attaquer et déboguer tous les types de réseaux sans fil.

### Nessus

![Image](https://www.freecodecamp.org/news/content/images/2020/08/nessus.png)

Nessus est un scanner de vulnérabilités d'entreprise populaire. Nessus est conçu pour être un outil complet d'analyse et de reporting des vulnérabilités. Alors que vous pouvez scanner et trouver des ports ou des services en utilisant Nmap, Nessus vous indiquera la liste des vulnérabilités et comment elles peuvent être exploitées.

Nessus dispose d'une excellente interface utilisateur, de dizaines de milliers de plugins et prend en charge le scripting intégré. Il est souvent privilégié par les entreprises car il aide les entreprises à auditer diverses conformités comme PCI et HIPPA. Nessus vous indiquera également la gravité des vulnérabilités afin que vous puissiez vous concentrer sur ces menaces en conséquence.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/nessus-1-1.png)
_Interface utilisateur de Nessus_

Nessus n'est pas un logiciel gratuit, mais offre une édition domestique gratuite limitée. Nessus a une alternative open-source appelée [Open-Vas](https://www.openvas.org/) qui offre des fonctionnalités similaires.

### Snort

![Image](https://www.freecodecamp.org/news/content/images/2020/08/snort.png)

Snort est un logiciel open-source pour détecter et prévenir les intrusions dans un réseau. Il peut effectuer une analyse du trafic en direct et journaliser les paquets entrants pour détecter les scans de ports, les vers et autres comportements suspects.

Snort est utilisé pour la défense par rapport à la plupart des autres outils de cette liste. Cependant, Snort vous aide à comprendre les méthodes de l'attaquant en journalisant leur activité. Vous pouvez également construire des [DNS sinkholes](https://en.wikipedia.org/wiki/DNS_sinkhole) pour rediriger le trafic de l'attaquant tout en trouvant des vecteurs d'attaque via Snort.

Snort dispose également d'une interface graphique basée sur le web appelée BASE (Basic Analysis and Security Engine). BASE fournit une interface front-end web pour interroger et analyser les alertes provenant de Snort.

## Conclusion

Dans le monde en réseau d'aujourd'hui, tout le monde, des agences gouvernementales aux banques, stocke des informations critiques dans le cloud. Les cyberattaques ont même le potentiel de paralyser une nation entière. Par conséquent, protéger ces réseaux n'est pas un choix, mais une nécessité absolue.

Que vous soyez débutant ou ingénieur en cybersécurité expérimenté, vous trouverez ces dix outils inestimables. Bonne chance dans votre parcours pour devenir un testeur d'intrusion réussi. Apprenez davantage d'outils à partir du [Répertoire des outils de sécurité](https://sectools.org/).

_Je rédige régulièrement des articles sur l'apprentissage automatique, la cybersécurité et AWS. Vous pouvez vous inscrire à ma [newsletter hebdomadaire](https://www.manishmshiva.com/) ici._