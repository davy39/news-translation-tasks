---
title: Comment créer votre premier serveur sécurisé prêt pour la production
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-09T12:29:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-your-first-safe-server-ready-for-production-f1cc60eec69a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Rka-cGjoHmoOpLLNz8ANbA.jpeg
tags:
- name: Devops
  slug: devops
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment créer votre premier serveur sécurisé prêt pour la production
seo_desc: 'By Flavio H. Freitas

  In this tutorial, I will present some of the best practices to build your own first
  safe server. I’ll list the steps you’ll need to take to have a fully functional
  server that you can use in production for your app.

  Having a safe...'
---

Par Flavio H. Freitas

Dans ce tutoriel, je vais présenter certaines des meilleures pratiques pour construire votre propre premier **serveur sécurisé**. Je vais lister les étapes que vous devrez suivre pour avoir un serveur entièrement fonctionnel que vous pouvez utiliser en **production** pour votre application.

Avoir un serveur sécurisé ne repose pas seulement sur le suivi de certaines étapes. C'est une recherche constante de nouvelles ressources et une amélioration sans fin. Mais cet article peut être une étape 0 dans la construction de votre propre infrastructure.

Je vais utiliser Amazon EC2 pour exécuter ces tests, mais j'ai également utilisé Amazon LightSail, Digital Ocean, Vultr et quelques autres. Dans tous les cas, ils étaient les mêmes à configurer, donc vous pouvez utiliser le fournisseur que vous préférez.

![Image](https://cdn-media-1.freecodecamp.org/images/oc74KOmG7JQiUS3NJ4fHjNM8S6BoKZLeyExz)
_Rendons-le sécurisé !_

Alors, commençons :

### Création des clés SSH publiques et privées

Avant de commencer, créons une paire de clés que certains hôtes demandent lors de l'installation du serveur. Cette étape et la suivante peuvent être omises si vous décidez de créer une paire de clés lors du lancement d'une instance de machine avec Amazon.

Créez une paire de clés SSH à l'aide de l'outil ssh-keygen.

```
$ ssh-keygen -t rsa -b 4096
```

Après cette étape, vous aurez les fichiers suivants : id_rsa et id_rsa.pub (clés privée et publique). **Ne** partagez jamais votre clé privée.

Un document plus détaillé sur la création des clés peut être trouvé [ici](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/).

### Importer la clé publique sur Amazon :

Nous allons importer la clé publique que nous venons de créer sur la plateforme Amazon.

1. Accédez à [Amazon Management Console](https://us-west-2.console.aws.amazon.com/console/home)
2. Cliquez sur AWS services > Compute > EC2
3. Cliquez sur le menu de gauche Network & Security > Key Pairs
4. Cliquez sur "Import Key Pair" et téléchargez votre clé publique (id_rsa.pub)

### **Créez votre machine**

Je vais installer une version Ubuntu sur Amazon EC2. Vous pouvez trouver une configuration complète à ce [lien](https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine). Les étapes sont les suivantes (mais pour simplifier, suivez ce [lien](https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine) pour plus d'explications) :

1. Accédez à [Amazon Management Console](https://us-west-2.console.aws.amazon.com/console/home)
2. Cliquez sur AWS services > Compute > EC2
3. Choisissez Launch Instance
4. Choisissez l'une des images. J'ai choisi Ubuntu Server 16.04 LTS (HVM), SSD Volume Type (mais choisissez en fonction de vos besoins)
5. Choisissez l'instance (encore une fois, selon vos besoins). Cliquez sur Review and Launch
6. Ouvrez un nouvel onglet et importez la clé publique créée sur Amazon.
7. Ici, on nous demande de "Sélectionner une paire de clés existante ou créer une nouvelle paire de clés". J'ai choisi "Choisir une paire de clés existante". Choisissez celle que vous avez téléchargée à l'étape précédente.
8. Cliquez sur "Launch Instances".
9. Cliquez sur le lien de l'instance que vous venez de créer.

Attention : Certaines des étapes ci-dessous pourraient être configurées sur cet écran initial d'Amazon. Mais comme je veux créer un tutoriel générique qui peut être utilisé pour d'autres hôtes, j'ai choisi les configurations par défaut.

### Connexion au nouveau serveur

Accédez à la machine avec ssh.

Tapez dans votre terminal :

```
$ ssh <USER>@<IP-ADDRESS> -p 22 -i <PATH-TO-PRIVATE-KEY>
```

* <USER> : L'utilisateur sur le système Linux. Pour Amazon, utilisez ubuntu, pour les autres, root
* <IP-ADDRESS> : L'adresse IP de la machine que vous avez créée. C'est le champ "Public DNS (IPv4)" dans l'onglet "Description" de votre instance.
* <PATH-TO-PRIVATE-KEY> : Le chemin complet vers la clé privée que vous avez générée à l'étape précédente (par exemple, /Users/flavio/.ssh/id_rsa).
* -i <PATH-TO-PRIVATE-KEY> : cette partie peut être omise si vous avez ajouté la clé à votre agent SSH.

### Donnez à votre nouvel utilisateur l'accès

Créez un nouveau compte utilisateur nommé « wizard »

```
$ sudo adduser wizard
```

Donnez à « wizard » la permission de sudo. Ouvrez le fichier

```
$ sudo nano /etc/sudoers.d/wizard
```

Et définissez le contenu :

```
wizard ALL=(ALL) NOPASSWD:ALL
```

Créez les répertoires suivants :

```
$ mkdir /home/wizard/.ssh# créez le fichier authorized_keys et copiez votre clé publique ici$ nano /home/wizard/.ssh/authorized_keys$ chown wizard /home/wizard/.ssh$ chown wizard /home/wizard/.ssh/authorized_keys
```

Copiez le contenu de la clé publique (PATH-TO-PUBLIC-KEY) et collez-le sur l'instance distante dans /home/wizard/.ssh/authorized_keys. Définissez les permissions :

```
$ chmod 700 /home/wizard/.ssh$ chmod 600 /home/wizard/.ssh/authorized_keys
```

### Sécurisation du système

Mettez à jour tous les paquets actuellement installés.

```
$ sudo apt-get update$ sudo apt-get upgrade
```

Changez le port SSH de 22 à 2201. Configurez le pare-feu (ufw, Uncomplicated Firewall, et il est vraiment simple) pour l'autoriser. Ouvrez le fichier /etc/ssh/sshd_config

```
$ sudo nano /etc/ssh/sshd_config
```

et changez les données suivantes :

```
Port 2201PermitRootLogin noPasswordAuthentication no
```

```
# ajoutez ceci pour éviter les problèmes avec plusieurs processus sshdClientAliveInterval 600ClientAliveCountMax 3
```

Redémarrez le service ssh :

```
$ sudo service ssh restart
```

Configurez l'Uncomplicated Firewall (UFW) pour n'autoriser que les connexions entrantes pour SSH (port 2201), HTTP (port 80) et NTP (port 123).

```
# fermez tous les ports entrants$ sudo ufw default deny incoming# ouvrez tous les ports sortants$ sudo ufw default allow outgoing# ouvrez le port ssh$ sudo ufw allow 2201/tcp# ouvrez le port http$ sudo ufw allow 80/tcp# ouvrez le port ntp : pour synchroniser l'horloge de votre machine$ sudo ufw allow 123/udp# activez le pare-feu$ sudo ufw enable
```

### Configurez l'horloge de votre serveur

Configurez le fuseau horaire local sur UTC :

```
$ sudo dpkg-reconfigure tzdata
```

Choisissez l'option « None of the Above » puis sélectionnez UTC.

### Déconnectez-vous et ajoutez votre clé à votre agent SSH

Déconnectez-vous de votre serveur et faites ce qui suit sur votre machine. Pour vous déconnecter :

```
$ exit
```

### Ajoutez l'autorisation de port d'accès sur Amazon

Cette étape est requise sur Amazon. Nous allons définir le port ssh que nous voulons utiliser sur Amazon également.

1. Accédez à [Amazon Management Console](https://us-west-2.console.aws.amazon.com/console/home)
2. Cliquez sur AWS services > Compute > EC2
3. Cliquez sur le menu de gauche Network & Security > Security Groups
4. Choisissez celui qui est attaché à votre instance
5. Cliquez sur Action > Edit Inbound Rules
6. Cliquez sur "Add Rule" et définissez : Type : Custom TCP, Port Range : 2201, Source : 0.0.0.0/0 et Description : SSH

### Connectez-vous avec les nouvelles identifiants

Maintenant, vous pouvez vous connecter à la machine avec l'utilisateur sur le nouveau port.

```
$ ssh wizard@<IP-ADDRESS> -p 2201 -i <PATH-TO-PRIVATE-KEY>
```

Vous avez un serveur prêt à exécuter votre application. Bientôt, j'écrirai un autre tutoriel sur la façon d'installer un environnement pour exécuter votre application Meteor en utilisant pm2. Je discuterai également de la configuration SSL, d'un proxy inverse, d'un équilibreur de charge et de Nginx. Mais cet article a montré comment créer un serveur générique plus sûr que vous pouvez utiliser pour exécuter ce dont vous avez besoin.

Si vous avez aimé cet article, n'oubliez pas de l'aimer et de me donner beaucoup d'applaudissements — cela signifie beaucoup pour l'auteur ? Et [suivez-moi](https://medium.com/@flaviohfreitas) si vous voulez lire plus d'articles sur la Culture, la Technologie et les Startups.

**Flávio H. de Freitas** est un entrepreneur, ingénieur, amateur de technologie, rêveur et voyageur. Il a travaillé en tant que **CTO** au **Brésil**, dans la **Silicon Valley et en Europe**.

Photo par [Ben White](https://unsplash.com/photos/1MHU3zpTvro?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)