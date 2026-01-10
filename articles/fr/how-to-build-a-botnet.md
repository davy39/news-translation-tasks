---
title: Qu'est-ce qu'un Botnet – Définition et Comment se Défendre contre les Attaques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-09-02T14:52:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-botnet
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-pixabay-163064.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
- name: '#infosec'
  slug: infosec
seo_title: Qu'est-ce qu'un Botnet – Définition et Comment se Défendre contre les Attaques
seo_desc: "By Megan Kaczanowski\nA botnet is a collection of internet connected devices\
  \ (anything from PCs to IoT devices) which are infected by the same malware. \n\
  A hacker uses the malware the botnet is infected with to control it and launch botnet\
  \ attacks. The..."
---

Par Megan Kaczanowski

Un botnet est une collection de dispositifs connectés à Internet (allant des PC aux dispositifs IoT) qui sont infectés par le même malware.

Un pirate utilise le malware dont le botnet est infecté pour le contrôler et lancer des attaques de botnet. Les attaques sont plus efficaces lorsqu'elles sont lancées à partir de centaines, de milliers, voire de centaines de milliers de dispositifs liés.

## Quel est l'intérêt de construire un botnet ?

Les botnets peuvent être utilisés pour diverses attaques :

* Générer de faux clics publicitaires pour augmenter les revenus d'un site ou améliorer sa visibilité dans les classements de recherche
* Générer des e-mails de spam pour des clients
* Lancer des attaques DDoS (distributed denial of service)
* Valider des listes de credentials divulgués (attaques par bourrage de credentials) afin de prendre le contrôle de divers comptes.

### Pourquoi il est important de comprendre le fonctionnement des botnets

En tant que professionnel de la sécurité, comprendre les botnets est extrêmement important. Tout d'abord, il est probable que vous soyez chargé de défendre contre les attaques de botnets. Et vous devrez probablement gérer des systèmes infectés à l'intérieur de votre réseau et utilisés comme partie d'un botnet.

Afin de se défendre efficacement contre les botnets, les défenseurs du réseau doivent comprendre les tactiques, techniques et procédures (TTP) utilisées par les bot-herders afin d'identifier leurs attaques et les signes d'une compromission à l'intérieur de leur réseau.

Aucune équipe de sécurité ne souhaite découvrir qu'un certain nombre de leurs routeurs ou dispositifs réseau ont été compromis et sont utilisés dans des attaques contre d'autres organisations.

Cela, comme toute compromission, peut entraîner des problèmes potentiels avec les régulateurs, des dommages à la réputation et des pertes financières résultant du nettoyage des dégâts.

## Comment un futur bot-herder commence-t-il ?

Construire un botnet n'est pas seulement une entreprise technique – c'est une entreprise commerciale.

Construire un botnet réussi nécessite de réfléchir à l'objectif, qu'il s'agisse de créer un plan d'affaires durable, un public cible (dont les dispositifs vont être infectés, et quel appât les attirera ?), et des processus pour garantir que la distribution et les processus internes sont sécurisés.

Ensuite, un futur bot-herder doit commencer par un service VPN qui accepte des formes de paiement anonymes (éventuellement plusieurs services à alterner). Ces services doivent être peu susceptibles de transmettre rapidement les enregistrements clients et les logs à toute agence de maintien de l'ordre (un service 'bulletproof').

L'étape suivante consiste à obtenir un hébergement 'bulletproof' (soit une entreprise quelque peu légitime qui est *_inefficace_* dans le traitement des plaintes légales, soit une entreprise spécifiquement destinée aux opérateurs de malware).

Ensuite, le bot-herder a besoin de domaines provenant d'un registrar qui sera peu susceptible de transmettre les informations clients aux forces de l'ordre et qui accepte des méthodes de paiement anonymes.

Optionnellement, un bot-herder peut encore mieux dissimuler son activité avec une technique comme le fast flux. Le fast flux peut être simple ou double.

Le fast flux simple implique d'avoir de nombreuses IPs attachées à un seul domaine, en échangeant les adresses IP très rapidement avec des changements de DNS (en utilisant des valeurs de temps de vie (TTL) très courtes et un DNS round-robin).

Le double flux ajoute une deuxième couche en faisant également tourner les enregistrements de serveur de noms (NS). Essentiellement, le fast flux permet à un bot-herder de faire tourner rapidement les points de terminaison et les serveurs de noms, réduisant ainsi les points de défaillance et évitant les tentatives de suppression par les équipes de sécurité.

Comprendre le fonctionnement du fast flux peut aider les défenseurs à identifier quand il se produit et à prendre des mesures de protection.

Par exemple, une équipe de sécurité peut contacter un registrar de domaines et demander qu'ils suppriment le domaine ou bloquent l'accès aux domaines malveillants dans leur réseau.

Typiquement, une équipe de sécurité tentera de bloquer l'accès aux domaines malveillants dans leur réseau, car convaincre un registrar de supprimer un domaine est souvent un processus chronophage (et est souvent infructueux, car les registrars peu scrupuleux sont peu susceptibles de procéder à des suppressions de domaines sans pression des forces de l'ordre).

Ensuite, le bot-herder a besoin du framework de construction de botnet (comment contrôler les bots qu'il a créés). Il s'agira soit d'un framework qu'il a créé lui-même (très difficile et chronophage), soit d'un framework acheté sur un forum du dark web (souvent avec support client), soit d'une version gratuite (probablement plus ancienne et moins fiable) disponible en ligne.

Il peut également avoir besoin d'un ou deux 'injecteurs' (essentiellement des modules complémentaires qui indiquent aux bots quoi faire, comme effectuer des fraudes aux clics, des DDoS, etc.).

Enfin, il a besoin d'un outil ou service d'exploitation afin d'infecter les dispositifs sans déclencher d'alertes de sécurité. Encore une fois, il peut construire le sien (très difficile et chronophage), acheter (ou louer) sur un forum du dark web (souvent avec support client), ou utiliser une version gratuite (probablement plus ancienne et moins fiable) disponible en ligne.

Souvent, il s'agit de packages logiciels qui peuvent être installés sur un serveur web vers lequel l'attaquant peut diriger ses victimes (via du phishing).

De plus, afin d'éviter la détection, un bot-herder peut utiliser un malware 'dropper'. Ce malware chiffrera le malware afin de cacher sa signature de fichier et tout fichier identifiable.

Les services de crypteur (qui créent des 'droppers') sont librement disponibles en ligne ou peuvent être achetés sur un certain nombre de places de marché pour l'aspirant bot-herder. Certains incluront du code 'anti-sandbox' qui vise à détecter si le malware est ouvert sur une machine sandboxée ou une machine virtuelle afin d'éviter l'analyse par les équipes de sécurité.

Chacune de ces étapes est une chance pour les défenseurs d'identifier l'attaquant dans leur réseau.

La plupart des défenses des organisations auront plusieurs couches :

* antivirus et détection de point de terminaison pour identifier les malwares basés sur des 'signatures' et sur un comportement inhabituel,
* proxies pour bloquer le trafic vers des domaines malveillants connus,
* logs alimentés dans un outil de gestion des informations et événements de sécurité (SIEM) conçu pour identifier les comportements inhabituels du système et du réseau, etc.

Ces couches sont conçues pour attraper les différentes étapes et types de malwares utilisés par les attaquants.

## Maintenant, il est temps pour l'infection

Typiquement, un bot-herder enverra une campagne de phishing ou de spam ciblant un grand nombre de personnes, dans l'espoir qu'un petit pourcentage d'entre elles cliquera sur le lien et téléchargera un 'exploit kit'. Ce kit 'droppera' un malware sur le dispositif, ce qui permet au bot-herder de contrôler le dispositif.

Alternativement, le bot-herder peut scanner de grands blocs d'adresses IP, à la recherche de dispositifs IoT avec des noms d'utilisateur et mots de passe par défaut (le botnet Mirai a suivi ce chemin). Beaucoup de gens ne prennent jamais la peine de changer leurs credentials par défaut lors de la configuration des dispositifs IoT.

Les dangers d'être trop réussi sont que si trop de dispositifs sont infectés, le botnet risque d'attirer l'attention de diverses entreprises d'antivirus (AV) ou de sécurité.

À ce stade, cela devient une bataille constante entre les entreprises d'AV et les bot-herders, chacun essayant de mettre à jour son logiciel pour échapper à l'autre.

## Comment les bots communiquent-ils avec le bot-herder ?

Une fois infectés, les bots ont besoin d'un moyen de recevoir des commandes de leur bot-herder. Nous pouvons regrouper ces méthodes en deux catégories – soit en mode push ou pull, toutes deux nécessitant un serveur de commande et contrôle (C&C ou C2) pour communiquer avec les bots.

Un serveur peut envoyer ou 'pousser' une commande à tous les bots (par exemple un serveur IRC, avec un canal secret et protégé par mot de passe), ou les bots peuvent envoyer une requête (un 'pull') au serveur C&C pour des mises à jour (par exemple un serveur HTTPD).

Ces dernières années, il y a également eu une augmentation des réseaux pair-à-pair (P2P) qui sont utilisés pour proxyfier les commandes ou localiser un serveur. L'avantage du P2P est qu'il n'y a pas de point de défaillance unique (comme c'est le cas avec tout serveur C2 centralisé).

En général, la meilleure option pour toute méthode de communication est celle qui utilise des protocoles standard, car il est plus difficile pour les outils de sécurité de détecter la différence entre le trafic normal et le trafic de botnet s'ils utilisent tous deux les mêmes protocoles (surtout avec HTTP, car la plupart des organisations ont un volume énorme de trafic HTTP légitime).

Ces dernières années, il y a eu une augmentation des bot-herders exploitant les réseaux de médias sociaux pour héberger leur plateforme C&C, ainsi que pour distribuer des malwares, exploitant le haut niveau de confiance que la plupart des gens placent dans leurs réseaux de médias sociaux.

Une façon pour les défenseurs de prévenir ce type de communication est de bloquer l'accès aux sites de médias sociaux, et de surveiller de près le trafic système normal.

Plus les défenseurs (et leurs outils) sont familiers avec l'apparence du trafic système normal, mieux ils sont préparés à identifier les pics inhabituels de trafic ou de comportement.

## Comment détecter les botnets

### Honeypots

Les honeypots sont des systèmes configurés pour ressembler à des machines vulnérables, mais qui n'ont pas accès à des informations sensibles. Typiquement, ils sont déployés par des équipes de sécurité/chercheurs afin d'identifier et de suivre les botnets lorsque les bot-herders tentent d'infecter les honeypots.

Puisque le honeypot n'est pas utilisé à des fins légitimes, tout trafic tentant de s'y connecter est probablement malveillant. Cela signifie qu'il est facile pour une équipe de sécurité de séparer le trafic malveillant du trafic normal, d'observer le comportement et de prendre des mesures.

### Signatures

Une signature de malware est un motif spécifique (comme quelques lignes de code qui lancent le malware ou une séquence d'octets spécifique) qui est utilisé pour identifier les codes malveillants connus.

Cela est encore utilisé comme une forme basique d'identification, mais les bot-herders utilisent de plus en plus des techniques d'obfuscation et des malwares en rapide évolution (de sorte que même les malwares connus semblent nouveaux et uniques pour les scanners) afin d'échapper à ces détections.

### IDS (Système de Détection d'Intrusion) et IPS (Système de Prévention d'Intrusion)

Ce sont des outils conçus pour identifier les comportements réseau (ou hôte) suspects et (dans le cas de l'IPS) les prévenir ou (dans le cas de l'IDS) alerter l'équipe de sécurité.

### Surveillance DNS Passive/Active

La surveillance DNS peut aider à détecter les domaines liés à l'activité des botnets, en fonction des caractéristiques lexicales des domaines et de leurs caractéristiques réseau (telles que le TTL et le nombre de sous-réseaux IP).

Puisque les bots devront initier des connexions (régulièrement) au serveur C&C, cela fournit une opportunité de suivi et de détection.

Typiquement, les domaines utilisés pour les botnets sont très rapidement recyclés et pas nécessairement destinés aux humains - ils peuvent même être des lettres et chiffres pseudo-aléatoires générés par un ordinateur (alors qu'un domaine légitime est probablement stable et lisible par l'homme). Ces caractéristiques d'identification peuvent aider à identifier les domaines de botnets.

Les botnets bien gérés peuvent être extrêmement difficiles à supprimer définitivement. Pour les supprimer, les forces de l'ordre et les organisations privées doivent généralement collaborer, souvent à travers les frontières.

Les équipes de sécurité sont plus susceptibles d'être chargées de gérer les conséquences des botnets, plutôt que de les supprimer. Elles peuvent devoir se défendre contre une attaque DDoS d'un botnet, ou leurs propres systèmes étant utilisés comme partie d'un botnet et donc peuvent devoir détecter la présence du botnet et contenir les machines infectées, mais ne sont pas susceptibles de pouvoir supprimer un botnet ('hacker en retour' est illégal dans la plupart des juridictions).

### Sources/Informations complémentaires :

* [Un guide pour débutants sur la construction de botnets](https://arstechnica.com/information-technology/2013/04/a-beginners-guide-to-building-botnets-with-little-assembly-required/3/)
* [Bots, Botnets, DDoS Attacks, and DDoS Attack Mitigation](https://engineering.purdue.edu/kak/compsec/NewLectures/Lecture29.pdf)
* [Detection and Classification of Different Botnet C&C Channels](http://www.cse.lehigh.edu/~chuah/publications/atc11_botnet.pdf)
* [Model for HTTP Botnet Detection Based on DNS Traffic Analysis](https://www.uvic.ca/engineering/ece/isot/assets/docs/Holistic%20Model%20for%20HTTP%20Botnet%20Detection%20Based%20on%20DNS.pdf)