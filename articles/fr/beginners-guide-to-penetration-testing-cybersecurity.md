---
title: Qu'est-ce que le Test d'Intrusion en Cybersécurité ? Un Guide pour Débutants
subtitle: ''
author: P S Mohammed Ali
co_authors: []
series: null
date: '2025-02-07T16:07:37.257Z'
originalURL: https://freecodecamp.org/news/beginners-guide-to-penetration-testing-cybersecurity
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738941455446/843335c0-35a3-4173-bd4c-7baf0e630e8e.png
tags:
- name: Security
  slug: security
- name: hacking
  slug: hacking
- name: penetration testing
  slug: penetration-testing
- name: 'security testing '
  slug: security-testing
seo_title: Qu'est-ce que le Test d'Intrusion en Cybersécurité ? Un Guide pour Débutants
seo_desc: In today's digital world, almost every activity we engage in is intertwined
  with technology. From making payments via UPI and booking movie or travel tickets
  online to selling products through e-commerce platforms, technology has become an
  integral p...
---

Dans le monde numérique d'aujourd'hui, presque toutes les activités que nous entreprenons sont étroitement liées à la technologie. Que ce soit pour effectuer des paiements via UPI, réserver des billets de cinéma ou de voyage en ligne, ou vendre des produits sur des plateformes de commerce électronique, la technologie est devenue une partie intégrante de notre routine quotidienne.

Pour s'assurer que ces activités sont sûres et sécurisées, les équipes de développement doivent disposer d'un cadre de test de sécurité robuste. Cela permet d'identifier les vulnérabilités, de prévenir les cybermenaces et de maintenir l'intégrité des transactions numériques.

Dans cet article, vous apprendrez tout sur les tests d'intrusion : ce que c'est, pourquoi chaque phase du processus est importante, et les outils utilisés par les pentesteurs pour faire leur travail.

## Qu'est-ce que le Test d'Intrusion ?

Le test d'intrusion est une pratique utilisée par les professionnels de la sécurité pour aider les entreprises et les équipes à sécuriser leurs données. Une entreprise donne au professionnel de la sécurité l'autorisation d'essayer de trouver des vulnérabilités dans leur système. Le professionnel de la sécurité rapporte ensuite les éventuels points faibles qu'il trouve à l'entreprise afin qu'elle puisse les corriger. Cela aide ces entreprises à prévenir les attaques potentielles avant que les pirates n'aient accès à leurs données.

Si une entreprise ne parvient pas à effectuer des tests d'intrusion, cela peut entraîner de graves conséquences telles que des violations de politique, des amendes lourdes pour non-conformité, une perte de confiance des clients, et une baisse de la réputation et de la valeur globale de l'organisation.

Il existe quatre phases de test d'intrusion :

1. Reconnaissance
   
2. Scanning
   
3. Exploitation
   
4. Soumission du rapport
   

Passons en revue chacune d'entre elles afin que vous puissiez apprendre ce qui est impliqué dans l'ensemble du processus.

## Reconnaissance : L'Art de la Collecte d'Informations

La reconnaissance consiste à recueillir des informations sur le système ou le réseau cible. L'objectif d'un pentesteur ici est de collecter autant de données que possible sur la cible, ce qui l'aide à comprendre l'architecture de la cible, à identifier les vulnérabilités potentielles et à développer une stratégie d'attaque efficace.

En reconnaissance, les tests peuvent être effectués de diverses manières, telles que la consultation des réseaux sociaux pour obtenir des informations sur la cible, l'utilisation d'outils de collecte d'informations comme theHarvester pour explorer les sites web liés au domaine cible, et plus encore.

À ce stade, toutes les données disponibles, qu'elles soient techniques ou non techniques, sont collectées sans filtrage de pertinence. L'objectif est de collecter autant d'informations que possible, car même les détails apparemment insignifiants peuvent s'avérer utiles plus tard dans une attaque.

La reconnaissance est cruciale pour un test d'intrusion réussi. Elle peut donc être un processus chronophage, prenant souvent de quelques heures à plusieurs semaines, selon la complexité de la cible.

### **Types de Reconnaissance**

Nous pouvons catégoriser la reconnaissance en deux types principaux en fonction du niveau d'interaction avec le système cible :

Tout d'abord, nous avons la reconnaissance passive. Cela implique de recueillir des informations à partir de sources publiques **sans interagir directement** avec le système cible. Comme aucun contact direct n'est établi, elle est furtive et moins susceptible d'alerter la cible.

À ce stade, une question peut se poser : Si le test d'intrusion est effectué avec l'approbation préalable du domaine cible, pourquoi devrions-nous effectuer une reconnaissance passive pour minimiser l'interaction directe alors que nous avons la liberté de réaliser une reconnaissance active ?

Eh bien, un testeur d'intrusion doit penser du point de vue d'un pirate non éthique. Les attaquants s'appuient souvent fortement sur les techniques de reconnaissance passive pour recueillir des informations critiques sans alerter la cible, ce qui en fait une phase cruciale dans le piratage éthique également.

C'est pourquoi le test d'intrusion doit inclure la reconnaissance passive. Elle aide à identifier les fuites d'informations potentielles, telles que les annonces publiques d'une entreprise cible ou les employés publiant des doutes liés à la programmation sur des plateformes comme Substack, ce qui pourrait conduire à un accès non autorisé au système.

La reconnaissance active, en revanche, implique une **interaction directe** avec le système cible pour extraire des informations spécifiques. Les méthodes courantes incluent le balayage de ports, la capture de bannières et le sniffing de réseau.

Cette approche fournit des informations plus précises et détaillées, mais elle comporte un risque plus élevé - l'adresse IP ou l'empreinte numérique du testeur peut être enregistrée par le système cible.

Pour la phase de reconnaissance, de nombreux outils sont disponibles sur Internet. Mais quelques-uns sont considérés comme très efficaces et populaires parmi les testeurs d'intrusion. Certains d'entre eux incluent Medusa et theHarvester.

En guise d'exemple ici, nous utiliserons theHarvester pour recueillir des informations sur un domaine cible (Zudio.com) et analyser les différents types de données récupérées par l'outil.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1738871546984/dc7e71a4-e76d-42df-b895-4b2f626fe902.png align="center")

Vous pouvez voir que l'outil a exploré le moteur de recherche Brave et a découvert quelques adresses IP ainsi que des sous-domaines supplémentaires du domaine cible (Zudio.com). Ces résultats doivent être correctement documentés et inclus dans le rapport de reconnaissance de la cible.

![Résultats de la collecte d'informations utilisant theHarvester](https://cdn.hashnode.com/res/hashnode/image/upload/v1738871767740/e0af88ca-35ec-435c-9196-2a0f173cb6fd.png align="center")

## Scanning : L'Art de Détecter les Failles

Les informations qu'un pentesteur recueille pendant la phase de reconnaissance servent d'entrée cruciale pour la phase de scanning. Ces données l'aident à obtenir des informations plus approfondies sur le système cible, lui permettant de cibler des zones et de filtrer les données nécessitant une analyse plus approfondie.

Avec une large gamme d'outils de scanning disponibles, les pentesteurs utilisent diverses techniques pour :

* Identifier les ports ouverts, car ils peuvent servir de points d'entrée potentiels.
   
* Surveiller l'activité du réseau pour détecter les vulnérabilités et les failles de sécurité.
   

### **Phases du Scanning**

Le scanning implique généralement deux étapes clés :

Tout d'abord, nous avons le **scanning de ports**, qui identifie les ports ouverts et fermés sur le système cible. Cela aide à déterminer quels services sont en cours d'exécution et sont potentiellement exploitables.

Les ports système servent de points d'entrée pour qu'un système informatique puisse effectuer diverses tâches. Il est crucial pour la sécurité de s'assurer que tous les ports inutiles sont fermés. Laisser des ports optionnels ouverts peut créer des points d'entrée potentiels pour les pirates.

Vous pouvez utiliser des outils comme **Nmap, Netcat, Masscan** à cette fin.

Pour une meilleure compréhension, scannons un domaine cible exemple (192.168.13.136) en utilisant Nmap et vérifions quels ports de service sont ouverts.

![Résultat du scan Nmap pour un domaine cible exemple montrant les ports ouverts](https://cdn.hashnode.com/res/hashnode/image/upload/v1738868226793/82cc30ab-7383-4b81-95ab-95e6a1b9bf07.png align="center")

Ensuite, nous avons le **scanning de vulnérabilités**, qui détecte les faiblesses dans les logiciels, les configurations et les services. Il aide les pentesteurs à évaluer les risques de sécurité associés aux ports et services identifiés.

Utilisons le même outil nmap pour détecter les vulnérabilités à partir des ports ouverts identifiés. Dans les résultats du scanning, vous pouvez voir que le port 21 est ouvert et ce port est spécifiquement utilisé pour le protocole de transfert de fichiers.

![Résultats du scan de vulnérabilités nmap](https://cdn.hashnode.com/res/hashnode/image/upload/v1738871075994/70823cf4-97ce-4cb7-b76b-0a8db3acb1bb.png align="center")

Ici, nous exécutons Nmap sur l'adresse cible (192.168.13.136) pour scanner le port FTP 21 en utilisant le script ftp-brute. Cela nous permet de vérifier si le service FTP est accessible en utilisant des noms d'utilisateur et des mots de passe par défaut.

Lors du scan, nous avons pu extraire des informations utiles supplémentaires, y compris des détails sur la version du serveur FTP (vsftpd 2.3.4). Ces informations peuvent être précieuses pour identifier les vulnérabilités potentielles dans cette version.

Enfin, l'outil a réussi à identifier une vulnérabilité dans le serveur en découvrant des noms d'utilisateur et des mots de passe valides à partir de la liste de dictionnaire incluse dans l'outil.

En général, la reconnaissance et le scanning sont souvent négligés par les analystes de sécurité, supposant qu'ils ne sont pas importants. Mais ces phases fournissent un ensemble de données précieux et une compréhension plus approfondie du domaine cible. Elles aident à filtrer et à diriger le processus d'exploitation, permettant aux testeurs d'intrusion de se concentrer sur des vulnérabilités spécifiques au lieu d'essayer aveuglément divers exploits.

Sauter ces phases conduit à une inefficacité, gaspillant du temps, des ressources et des efforts. Pour une exploitation réussie, il est essentiel de mener une collecte d'informations et un scanning approfondis avant de procéder plus loin.

## Exploitation : L'Art de la Simulation d'Attaque

Le résultat de la phase de scanning donne aux pentesteurs une compréhension claire des points d'entrée potentiels, communément appelés "portes ouvertes", à travers les ports et services identifiés. Ces informations aident les testeurs à déterminer quelles vulnérabilités peuvent être exploitées pour simuler une cyberattaque réelle.

Une fois les vulnérabilités identifiées, les testeurs déploient diverses techniques d'attaque pour évaluer leur impact. L'objectif est de démontrer comment un pirate malveillant pourrait obtenir un accès non autorisé et compromettre le système cible. Certaines méthodes d'attaque courantes incluent :

* **Injection SQL** - Exploitation des vulnérabilités de la base de données.
   
* **Cross-Site Scripting (XSS)** - Injection de scripts malveillants dans les applications web.
   
* **Débordement de tampon** - Écriture en mémoire pour exécuter du code malveillant.
   
* **Attaques par force brute** - Craquage de mots de passe faibles pour accéder au système.
   

Pour une compréhension plus claire, explorons comment les vulnérabilités de la base de données sont exploitées en utilisant des attaques par injection SQL.

Supposons qu'il y ait un champ de nom d'utilisateur et de mot de passe dans un formulaire de connexion. Typiquement, lorsque l'utilisateur entre ses identifiants, le système récupère ces valeurs d'entrée, construit une requête SQL et l'envoie au serveur pour authentification.

L'injection SQL fonctionne en manipulant cette requête pour contourner l'authentification. À un niveau basique, un attaquant peut entrer des valeurs spécialement conçues pour altérer la logique de la requête. Par exemple, considérons la requête SQL suivante :

```sql
SELECT * FROM PRODUCTS WHERE USERNAME = " OR 1=1 -- " AND PASSWORD = "1234"
```

Décomposons cet exploit pour voir ce qui se passe :

* La condition OR 1=1 s'évalue toujours à vrai, ce qui signifie que la requête récupère tous les enregistrements de la base de données.
   
* La séquence `--` est un opérateur de commentaire en SQL, qui ignore le reste de la requête (y compris la vérification du mot de passe).
   

En conséquence, l'attaquant obtient un accès sans identifiants valides, contournant ainsi l'authentification.

## Soumission du Rapport : L'Art de la Validation

La phase finale du test d'intrusion consiste à rapporter les vulnérabilités identifiées pendant le cycle de test de sécurité. Ces rapports sont cruciaux pour guider le processus de remédiation, garantissant que l'entreprise traite toute faiblesse avant qu'elle ne puisse être exploitée.

Les rapports de test d'intrusion incluent généralement des informations détaillées sur les attaques menées, les résultats respectifs et une évaluation des risques impliqués. Il est important de noter que le langage utilisé dans ces rapports est non technique, car les résultats sont souvent partagés avec différentes équipes au sein de l'organisation, y compris :

* La direction
   
* Les autorités supérieures
   
* Les équipes non techniques (comme les RH, le juridique, etc.)
   

Ces rapports doivent être facilement compréhensibles et confidentiels, car ils peuvent contenir des informations sensibles sur les vulnérabilités de l'organisation.

Le rapport doit inclure les paramètres clés suivants :

* Nombre d'employés impliqués
   
* Date de début et date de fin de l'évaluation
   
* Liste des domaines cibles
   
* Liste des ports ouverts (le cas échéant)
   
* Liste des vulnérabilités identifiées, classées par niveau de risque (Critique, Élevé, Moyen, Faible, Informationnel)
   
* Mesures préventives pour atténuer les risques
   
* Liste des outils utilisés pendant l'évaluation
   

Bien que la structure et le contenu de ces rapports puissent varier d'une organisation à l'autre, les paramètres ci-dessus sont obligatoires pour une évaluation de sécurité complète.

L'objectif est de s'assurer que les parties prenantes à tous les niveaux de l'organisation peuvent prendre des mesures appropriées, qu'il s'agisse de corriger une vulnérabilité, de réviser une politique ou de mettre à jour une stratégie de sécurité.

## Conclusion

Le cycle de vie du test d'intrusion est continu et c'est quelque chose que votre équipe doit effectuer périodiquement. Vous ne pouvez pas simplement le faire une fois, traiter ces préoccupations et l'oublier.

Alors que de nouvelles vulnérabilités émergent avec la sortie de versions mises à jour de logiciels, d'applications et de systèmes, le test d'intrusion reste essentiel pour identifier et traiter ces nouveaux risques.

Une approche proactive de la sécurité par le biais de tests d'intrusion continus est cruciale pour maintenir un environnement numérique sûr et sécurisé pour les organisations et leurs utilisateurs.