---
title: Qu'est-ce que SSH ? Signification de SSH dans Linux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-02T13:29:50.000Z'
originalURL: https://freecodecamp.org/news/ssh-meaning-in-linux
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Shittu-Olumide-What-is-SSH-SSH-Meaning-in-Linux.png
tags:
- name: computer network
  slug: computer-network
- name: Linux
  slug: linux
- name: ssh
  slug: ssh
seo_title: Qu'est-ce que SSH ? Signification de SSH dans Linux
seo_desc: "By Shittu Olumide\nSecure Shell (SSH) is a widely used network protocol\
  \ that provides a secure way to access remote servers and computers. \nIn Linux,\
  \ SSH is an essential tool for remote administration and file transfer. In this\
  \ article, we will go ove..."
---

Par Shittu Olumide

Secure Shell (SSH) est un protocole réseau largement utilisé qui offre un moyen sécurisé d'accéder à des serveurs et ordinateurs distants. 

Dans Linux, SSH est un outil essentiel pour l'administration à distance et le transfert de fichiers. Dans cet article, nous allons passer en revue la signification de SSH dans Linux, son histoire, ses fonctionnalités, sa configuration et ses cas d'utilisation.

## Qu'est-ce que SSH ?

SSH est un protocole réseau cryptographique qui permet une communication sécurisée entre des appareils en réseau. Il a été développé comme un remplacement pour [Telnet](https://en.wikipedia.org/wiki/Telnet), qui envoie toutes les données, y compris les mots de passe, en texte clair, le rendant susceptible d'être écouté et intercepté. 

SSH fournit des mécanismes de chiffrement et d'authentification pour protéger la confidentialité et l'intégrité des communications réseau.

## Brève histoire de SSH

La première version de SSH, SSH-1, a été développée par [Tatu Ylönen en 1995](https://www.usenix.org/conference/lisa13/speaker-or-organizer/tatu-yl%C3%B6nen-ssh-communications-security) en réponse à l'insécurité de Telnet et FTP. 

En 1996, SSH Communications Security a publié une version commerciale de SSH-1, qui est devenue largement utilisée dans l'industrie. 

Mais SSH-1 avait certaines vulnérabilités de sécurité, et en 1998, Ylönen a développé SSH-2, qui a résolu ces problèmes et est devenu la version la plus largement utilisée de SSH.

## Comment fonctionne SSH

SSH utilise une architecture client-serveur, où le client initie une connexion au serveur et demande un canal de communication sécurisé. Le serveur répond en générant une paire de clés cryptographiques, une publique et une privée.

La clé publique est envoyée au client, tandis que la clé privée est conservée en sécurité sur le serveur. Le client chiffre ensuite une clé de session aléatoire en utilisant la clé publique du serveur et l'envoie au serveur. Le serveur déchiffre la clé de session en utilisant sa clé privée et envoie un accusé de réception au client. À partir de ce moment, toutes les données transmises entre le client et le serveur sont chiffrées en utilisant la clé de session.

## Fonctionnalités de SSH

* **Chiffrement** : SSH utilise des algorithmes de chiffrement forts, tels que AES, pour protéger la confidentialité et l'intégrité des données transmises sur le réseau.
* **Transfert de fichiers sécurisé** : Il fournit des capacités de transfert de fichiers sécurisé (SFTP), qui permettent aux utilisateurs de transférer des fichiers entre des serveurs distants de manière sécurisée.
* **Connexion à distance** : SSH offre un moyen sécurisé de se connecter à des serveurs et ordinateurs distants, sans exposer les identifiants de connexion aux attaquants.
* **Redirection de port** : Il offre des capacités de redirection de port, qui permettent aux utilisateurs d'accéder à des services restreints sur des serveurs distants via un canal de communication sécurisé.
* **Redirection X11** : SSH offre des capacités de redirection X11, qui permettent aux utilisateurs d'exécuter des applications graphiques à distance, sans avoir à les installer localement.
* **Redirection d'agent** : Il offre également des capacités de redirection d'agent, qui permettent aux utilisateurs d'utiliser des clés SSH pour l'authentification sur des serveurs distants, sans avoir à entrer leur mot de passe à chaque fois.

## Configuration de SSH

La configuration de SSH implique divers paramètres et options qui peuvent être personnalisés pour optimiser la connexion SSH et améliorer la sécurité. Voici quelques tâches courantes de configuration SSH :

* **Génération de clés SSH** : Avant d'utiliser SSH, les utilisateurs doivent générer une paire de clés cryptographiques, une publique et une privée. La clé publique est partagée avec le serveur, tandis que la clé privée est conservée en sécurité sur l'ordinateur de l'utilisateur.
* **Édition des fichiers de configuration** : Les utilisateurs peuvent créer et éditer des fichiers de configuration SSH pour personnaliser leurs paramètres SSH, tels que la spécification de l'algorithme de chiffrement préféré ou la configuration de la redirection de port. Les fichiers de configuration SSH sont généralement situés dans le répertoire `/etc/ssh/`.
* **Méthodes d'authentification** : SSH prend en charge diverses méthodes d'authentification, telles que l'authentification par mot de passe, l'authentification par clé publique et l'authentification multifactorielle. Les utilisateurs peuvent choisir la méthode d'authentification la plus adaptée en fonction de leurs besoins de sécurité.
* **Configuration sécurisée de SSH** : Pour garantir une sécurité maximale, les utilisateurs doivent suivre les meilleures pratiques pour une configuration sécurisée de SSH, telles que la désactivation de la connexion root, l'application de mots de passe forts et la limitation du nombre de tentatives de connexion échouées. Les utilisateurs peuvent également utiliser des outils comme Fail2Ban pour prévenir les attaques par force brute sur SSH.
* **Activation de la redirection X11** : SSH offre des capacités de redirection X11, qui permettent aux utilisateurs d'exécuter des applications graphiques à distance, sans avoir à les installer localement. Pour activer la redirection X11, les utilisateurs peuvent ajouter le drapeau -X ou -Y lors de la connexion au serveur distant.
* **Redirection de port** : SSH permet aux utilisateurs de configurer la redirection de port, ce qui peut être utile pour accéder à des services restreints sur des serveurs distants via un canal de communication sécurisé. Les utilisateurs peuvent configurer une redirection de port locale ou distante, selon leurs besoins.
* **Compression** : SSH prend en charge la compression des données, ce qui peut améliorer les performances de la connexion SSH, en particulier lors du transfert de gros fichiers ou de l'exécution d'applications gourmandes en ressources. Les utilisateurs peuvent activer la compression en ajoutant le drapeau `-C` lors de la connexion au serveur distant.

## Exemples et cas d'utilisation de SSH

* **Administration de serveur distant** : SSH est couramment utilisé pour l'administration de serveurs distants, permettant aux utilisateurs d'exécuter des commandes et de gérer des serveurs depuis un emplacement distant.
* **Transfert de fichiers sécurisé** : SSH offre un moyen sécurisé de transférer des fichiers entre des serveurs distants, sans exposer les fichiers ou les identifiants de connexion aux attaquants.
* **Exécution d'applications graphiques à distance** : SSH permet aux utilisateurs d'exécuter des applications graphiques à distance, sans avoir à les installer localement, ce qui peut être utile pour des applications gourmandes en ressources ou lors de l'utilisation d'un appareil peu puissant.
* **Redirection de port pour accéder à des services restreints** : SSH permet aux utilisateurs d'accéder à des services restreints sur des serveurs distants via un canal de communication sécurisé, en configurant la redirection de port.
* **Tunneling pour une communication sécurisée** : SSH permet aux utilisateurs de configurer des tunnels chiffrés pour une communication sécurisée entre deux appareils en réseau, ce qui peut être utile pour accéder à des ressources sur un réseau privé.

## Conclusion

Pour conclure cet article, voici un récapitulatif de ce que nous avons couvert et de ce que vous devez savoir sur SSH :

* SSH est un protocole sécurisé pour la communication à distance dans Linux.
* SSH utilise le chiffrement pour protéger les données et des mécanismes d'authentification pour vérifier les utilisateurs.
* SSH est un moyen fiable et efficace de communiquer de manière sécurisée sur Internet, et est un outil vital pour l'administration et le développement de systèmes Linux.
* SSH offre des capacités de connexion à distance, de transfert de fichiers sécurisé, de redirection de port, de redirection X11 et de redirection d'agent.
* Pour utiliser SSH, les utilisateurs doivent générer une paire de clés cryptographiques, une publique et une privée.
* Les fichiers de configuration SSH peuvent être personnalisés pour optimiser la connexion SSH et améliorer la sécurité.
* SSH prend en charge diverses méthodes d'authentification, telles que l'authentification par mot de passe, l'authentification par clé publique et l'authentification multifactorielle.
* Pour garantir une sécurité maximale, les utilisateurs doivent suivre les meilleures pratiques pour une configuration sécurisée de SSH, telles que la désactivation de la connexion root, l'application de mots de passe forts et la limitation du nombre de tentatives de connexion échouées.
* SSH peut être utilisé pour l'administration de serveurs distants, le transfert de fichiers sécurisé, l'exécution d'applications graphiques à distance, la redirection de port et le tunneling pour une communication sécurisée.
* SSH est un protocole largement utilisé et pris en charge, avec de nombreux clients et serveurs SSH disponibles pour différentes plateformes.

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !